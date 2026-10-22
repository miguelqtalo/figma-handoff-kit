#!/usr/bin/env python3
"""Hook: a handoff spec must not have an empty required section.

Runs in two places (see .claude/settings.json):
- PostToolUse on Write|Edit: checks the handoff.md that was just written and
  tells Claude what is missing (exit 2 sends the message back to Claude).
- Stop: blocks the end of the turn while a handoff.md written in THIS
  session is incomplete (exit 2 keeps Claude working). Specs from past runs
  are kept as they were, so they do not block new sessions. The PostToolUse
  call records each written spec in .claude/hooks/state/<session_id>.txt.

A section is empty when it has no real content: only headings, table
headers, "- Label:" lines with no value, or placeholders like TODO / <...>.
A table row with an empty cell also fails: write NOT IN DESIGN: instead.
"""
import json
import os
import re
import sys
from pathlib import Path

REQUIRED = ["Source", "States", "Tokens", "Copy", "Behavior", "Accessibility"]
REQUIRED_SUB = {
    "Behavior": ["Interactions", "Breakpoints", "Edge cases"],
    "Accessibility": ["Focus order", "Names and alt text", "Review summary"],
}
PLACEHOLDER = re.compile(r"\bTODO\b|\bTBD\b|<[a-z][^>]*>", re.IGNORECASE)


def split_sections(text, level):
    marker = "#" * level + " "
    sections, name, buf = {}, None, []
    for line in text.splitlines():
        if line.startswith(marker):
            if name is not None:
                sections[name] = buf
            name = re.sub(r"^\d+\.\s*", "", line[len(marker):]).strip()
            buf = []
        elif name is not None:
            buf.append(line)
    if name is not None:
        sections[name] = buf
    return sections


def problems_in(lines, label):
    found, content = [], False
    in_table, after_sep = False, False
    for raw in lines:
        line = raw.strip()
        if not line or line.startswith("#"):
            in_table = after_sep = False
            continue
        if line.startswith("|"):
            if not in_table:
                in_table, after_sep = True, False
                continue  # header row
            if re.fullmatch(r"\|[\s:|-]+\|", line):
                after_sep = True
                continue
            if after_sep:
                cells = [c.strip() for c in line.strip("|").split("|")]
                if any(not c for c in cells):
                    found.append(f"{label}: table row has an empty cell: {line[:80]}")
                content = True
            continue
        in_table = after_sep = False
        m = re.match(r"^[-*]\s+([^:]+):\s*(.*)$", line)
        if m and not m.group(2).strip():
            found.append(f"{label}: '{m.group(1).strip()}' has no value")
            continue
        content = True
    if not content:
        found.append(f"{label}: section is empty")
    return found


def check(path):
    text = Path(path).read_text(encoding="utf-8")
    issues = []
    for m in PLACEHOLDER.finditer(text):
        issues.append(f"placeholder left in the file: {m.group(0)}")
    sections = split_sections(text, 2)
    for name in REQUIRED:
        if name not in sections:
            issues.append(f"missing section: ## {name}")
            continue
        issues += problems_in(sections[name], name)
        for sub in REQUIRED_SUB.get(name, []):
            subs = split_sections("\n".join(sections[name]), 3)
            if sub not in subs:
                issues.append(f"{name}: missing ### {sub}")
            else:
                issues += problems_in(subs[sub], f"{name} > {sub}")
    return issues


def report(path, issues):
    sys.stderr.write(
        f"check-handoff: {path} is not complete.\n"
        + "\n".join(f"- {i}" for i in issues)
        + "\nFill each item from Figma, or write 'NOT IN DESIGN: <question>'. Do not delete headings.\n"
    )


def main():
    data = json.load(sys.stdin)
    event = data.get("hook_event_name", "")
    root = Path(os.environ.get("CLAUDE_PROJECT_DIR", "."))
    state = root / ".claude" / "hooks" / "state" / f"{data.get('session_id', 'unknown')}.txt"
    if event == "Stop":
        if data.get("stop_hook_active") or not state.exists():
            return 0
        bad = 0
        for p in sorted(set(state.read_text().split())):
            if Path(p).exists():
                issues = check(p)
                if issues:
                    report(p, issues)
                    bad += 1
        return 2 if bad else 0
    path = (data.get("tool_input") or {}).get("file_path", "")
    if not re.search(r"/handoffs/[^/]+/handoff\.md$", path) or not Path(path).exists():
        return 0
    state.parent.mkdir(parents=True, exist_ok=True)
    with state.open("a") as f:
        f.write(path + "\n")
    issues = check(path)
    if issues:
        report(path, issues)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
