# Design to Code: AI-Optimized Recurring Task Flow

**Figma Handoff Kit**: a Claude Code kit for designers. Give it one finished Figma screen. It writes a **developer handoff spec** (states, tokens, copy, behavior) and an **accessibility review**. The goal: a developer can build the screen from the spec without a follow-up meeting.

Capstone project, "Automate Your Week", designer track. Author: Miguel Zabala.

## What the kit does

```
Figma link ──► Figma MCP (read-only) ──► handoff-spec skill ──► check-handoff hook ──► a11y-reviewer subagent ──► decisions.md
               metadata, variables,      writes handoff.md      blocks empty          WCAG 2.2 AA pass/fail     one line per run
               screenshot, context       (template + contrast)  sections
```

| Session block | File | What it does |
|---|---|---|
| S1 Prompting | `prompts/brief.md` | The task brief, written with the 5 principles |
| S2 Workspace | `CLAUDE.md` | 3 never-ever rules, scope, out of scope, folder map |
| S3 Skill | `.claude/skills/handoff-spec/` | Steps, handoff template, contrast script |
| S3 Hooks | `.claude/settings.json`, `.claude/hooks/` | `check-handoff.py` blocks a handoff with an empty section (after each write, and at the end of the turn for specs written in that session). `block-secrets.py` blocks `.env` and credential files. |
| S4 Subagent | `.claude/agents/a11y-reviewer.md` | Read-only reviewer (Read, Grep, Glob), `memory: project` |
| S4 Memory | `decisions.md` | Baseline, run log, mistakes and fixes |
| S5 MCP | `.mcp.json` | Figma MCP, project scope, read tools only |

## Install (about 10 minutes)

You need:
- Claude Code 2.x (`claude --version`)
- Python 3 (`python3 --version`), standard library only
- A Figma account with view access to the file

Steps:

1. Clone the repository and open the folder:
   ```bash
   git clone https://github.com/miguelqtalo/figma-handoff-kit.git
   cd figma-handoff-kit
   ```
2. Start Claude Code **in this folder**:
   ```bash
   claude
   ```
   The kit's hooks, skill and agent only load when Claude Code starts in this folder.
3. Connect Figma. Choose one way:
   - **You have the Figma plugin for Claude Code:** type `/mcp`, open `plugin:figma:figma`, and sign in. You can then skip the project server.
   - **You don't have the plugin:** Claude Code asks you to approve the `figma` server from `.mcp.json`. Approve it, type `/mcp`, open `figma`, and sign in.
4. Check: type `/mcp`. A Figma server must show "connected". Then start a **new** session (`/exit`, then `claude`) so the Figma tools load.
   Note: do this sign-in **inside the kit folder**, even if Figma already works in another project. In our test, the sign-in did not carry over to a new folder.

## Run (one screen)

1. In Figma, select the finished frame and copy its link (it has `node-id=` in it).
2. Type `/context` and note the numbers (before).
3. In Claude Code, type:
   ```
   Run the brief in prompts/brief.md for <Figma link>
   ```
4. Wait. The kit reads the frame, writes the spec, runs the reviewer and logs the run.
5. Type `/context` again (after). Then run:
   ```bash
   python3 scripts/session-usage.py
   ```
   It prints the total tokens, API calls, peak context, skills and subagents of the session.
6. **Review the spec yourself before you share it.** Read it all, check it against Figma, and try to break it. Log every mistake in `decisions.md`. Then fix the skill or `CLAUDE.md`.
7. Use `/clear` before the next screen.

Headless option (no chat):
```bash
claude -p "Run the brief in prompts/brief.md for <Figma link>" --permission-mode acceptEdits --output-format json
```

## Output

```
handoffs/<screen-slug>/
├── handoff.md            the spec for developers
├── a11y-review.md        the reviewer's pass/fail list
└── figma-reference.png   the frame, for reference
```

## Safety

- Figma write tools are denied in `.claude/settings.json`. The kit only reads Figma.
- `block-secrets.py` blocks reading or editing `.env`, keys and credential files.
- The kit never sends anything. You share the spec yourself, after your review.
- Commit before each session, so `git restore .` can undo a bad run.

## Troubleshooting

| Problem | Fix |
|---|---|
| "Figma MCP not connected" | `/mcp`, sign in to the Figma server, then start a new session |
| Hooks do not run | Start `claude` inside the kit folder, not a parent folder |
| `check-handoff` blocks the spec | Read the list it prints. Fill each item from Figma, or write `NOT IN DESIGN: <question>` |
| Very high token use | Big frames: the skill should call `get_design_context` per section. Check `decisions.md` for past numbers |

## Results so far

See `decisions.md`: baseline, every run (time, tokens, peak context, results), every mistake and its fix. Token numbers come from each session transcript, read by `scripts/session-usage.py`.
