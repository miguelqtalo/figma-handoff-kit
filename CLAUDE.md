# CLAUDE.md: Figma Handoff Kit

This kit turns one finished Figma screen into a developer handoff spec.
A developer must be able to build the screen from the spec without a follow-up meeting.

## Never-ever rules

1. **Never invent design data.** Every value, string and state comes from Figma. If Figma does not show it, write `NOT IN DESIGN:` and a question for the designer.
2. **Never write a raw value where a token exists.** Use the Figma variable name. If the frame has no variables, say so in the Tokens section and list the raw values as "needs a token".
3. **Never send, post or share anything.** The kit only writes files in `handoffs/`. The designer reviews and shares them.

## Stack

- Claude Code (CLI or desktop app)
- Figma MCP server (remote, `https://mcp.figma.com/mcp`), set in `.mcp.json` (project scope)
- Python 3 for the hooks and scripts (standard library only)
- Output is Markdown. An HTML mockup is optional.

## Scope

- Read one Figma frame (read-only).
- Write `handoffs/<screen-slug>/handoff.md` with the `handoff-spec` skill.
- Run the `a11y-reviewer` subagent on the spec and save `a11y-review.md`.
- Log the run in `decisions.md`.

## Out of scope

- Writing production code in an app repo.
- Changing the Figma file (no `use_figma`, no write tools).
- Sending the spec to Jira, Slack or email. The designer does this by hand.

## Workflow (one run)

1. Read `prompts/brief.md` and follow it.
2. Use the `handoff-spec` skill.
3. Delegate the accessibility check to the `a11y-reviewer` subagent.
4. Add one line to `decisions.md`: date, screen, time, result, what was wrong.
5. If the reviewer or the designer found a mistake, fix the skill or this file so it does not happen again.

## Workspace structure

```
figma-handoff-kit/
├── CLAUDE.md                  this file (always loaded)
├── README.md                  install and run guide for teammates
├── decisions.md               memory: one line per run and per mistake
├── .mcp.json                  Figma MCP, project scope
├── prompts/brief.md           the task brief (5 prompting principles)
├── .claude/
│   ├── settings.json          hooks and permissions
│   ├── hooks/
│   │   ├── check-handoff.py   blocks a handoff with an empty required section
│   │   └── block-secrets.py   blocks reading .env and credential files
│   ├── skills/handoff-spec/   the handoff skill, template and contrast script
│   └── agents/a11y-reviewer.md read-only WCAG 2.2 AA reviewer
├── scripts/session-usage.py   token usage of a session, from its transcript
├── handoffs/<screen-slug>/    one folder per screen (output)
└── evidence/                  extra run evidence (raw outputs)
```

## Token habits

- Run `/context` before and after a long run. After the run, `python3 scripts/session-usage.py` gives the exact token numbers for `decisions.md`.
- Call `get_metadata` first. For a big frame, call `get_design_context` on the main sections, not the whole screen.
- Use `/clear` between two screens.
- Stay in the kit folder. Use absolute paths; never `cd` to another folder (subagent memory is saved relative to the session folder).
