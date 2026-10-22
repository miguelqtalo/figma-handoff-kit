#!/usr/bin/env python3
"""Token usage of one Claude Code session, read from its transcript.

Usage:
  python3 scripts/session-usage.py              latest session started in this folder
  python3 scripts/session-usage.py <session-id> one session (id or .jsonl path)

Every API response in the transcript has a usage block. This script adds them
up once per response id, and also lists the tools, skills and subagents used.
"""
import collections
import json
import re
import sys
from pathlib import Path

PROJECTS = Path.home() / ".claude" / "projects"


def transcript_path(arg):
    if arg and arg.endswith(".jsonl"):
        return Path(arg)
    folder = PROJECTS / re.sub(r"[^A-Za-z0-9]", "-", str(Path.cwd()))
    if arg:
        return folder / f"{arg}.jsonl"
    files = sorted(folder.glob("*.jsonl"), key=lambda p: p.stat().st_mtime)
    if not files:
        sys.exit(f"No transcripts found in {folder}")
    return files[-1]


def main():
    path = transcript_path(sys.argv[1] if len(sys.argv) > 1 else "")
    usage, tools, skills, agents = {}, collections.Counter(), [], []
    first = last = None
    peak = 0
    for line in path.open(encoding="utf-8"):
        try:
            d = json.loads(line)
        except ValueError:
            continue
        ts = d.get("timestamp")
        if ts:
            first, last = first or ts, ts
        if d.get("type") != "assistant":
            continue
        m = d.get("message") or {}
        u = m.get("usage")
        if u and m.get("id") not in usage:
            usage[m.get("id")] = u
            ctx = sum(u.get(k, 0) or 0 for k in ("input_tokens", "cache_read_input_tokens", "cache_creation_input_tokens"))
            peak = max(peak, ctx)
        for c in m.get("content", []):
            if c.get("type") == "tool_use":
                tools[c["name"]] += 1
                if c["name"] == "Skill":
                    skills.append(c["input"].get("skill"))
                if c["name"] in ("Agent", "Task"):
                    agents.append(c["input"].get("subagent_type"))
    keys = ["input_tokens", "output_tokens", "cache_creation_input_tokens", "cache_read_input_tokens"]
    totals = {k: sum((u.get(k) or 0) for u in usage.values()) for k in keys}
    print(f"Transcript: {path.name}")
    print(f"Time:       {first} -> {last}")
    print(f"API calls:  {len(usage)}")
    print(f"Peak context per call: {peak:,}")
    for k in keys:
        print(f"{k:30} {totals[k]:>12,}")
    print(f"{'TOTAL':30} {sum(totals.values()):>12,}")
    print("Skills:", ", ".join(s for s in skills if s) or "none")
    print("Subagents:", ", ".join(a for a in agents if a) or "none")
    print("Tools:", ", ".join(f"{n} x{c}" for n, c in tools.most_common()))
    print("Note: subagent tokens are in their own transcripts (subagents/ folder), not in this total.")


if __name__ == "__main__":
    main()
