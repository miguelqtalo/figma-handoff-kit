# Brief: developer handoff for one Figma screen

Paste this brief to start a run, or type: `Run the brief in prompts/brief.md for <Figma link>`.
Each part below follows one of the 5 prompting principles from Session 1.

## 0. Before you start

Check that a Figma MCP server is connected: search for the Figma tools (`get_metadata`). If there are none, stop at once and tell me: "Figma is not connected. Type /mcp, sign in to Figma, then start a new session." Do not read any other file first.

## 1. Single Responsibility

Write the developer handoff for **one** Figma frame: `<FIGMA_LINK>`.
Do not do anything else in this session. No code in an app repo, no edits in Figma, no messages to anyone.

## 2. Context First

- I am a product designer. The developers build from my handoff docs.
- Today a handoff takes me at least 8 hours by hand per screen, without iterations or changes (my estimate). Developers often come back with questions about states, spacing tokens and copy length.
- The frame is finished and approved. Treat Figma as the source of truth.
- Project rules are in `CLAUDE.md`. Past runs and known mistakes are in `decisions.md`. Read both first.

## 3. Tool Directives

- Use the **Figma MCP** only to read: `get_metadata` first, then `get_variable_defs`, `get_screenshot` and `get_design_context`. For a big frame, call `get_design_context` per main section.
- Load the **`handoff-spec` skill with the Skill tool** (not by reading SKILL.md), so the run log shows it was used. Use its template exactly.
- Use the skill's `scripts/contrast.py` for every text and background color pair. Do not calculate contrast in your head.
- Delegate the accessibility check to the **`accessibility-reviewer` subagent**. Do not review accessibility yourself.
- Do not use web search. Do not read files outside this kit folder, except a file the Figma MCP saves for its own large output, and the Figma asset URLs.

## 4. Definition of Done

The run is done when all of these are true:

- [ ] `handoffs/<screen-slug>/handoff.md` exists, and the `check-handoff` hook accepts it (no empty required section).
- [ ] Every state in the template has a value or a `NOT IN DESIGN:` question.
- [ ] Every color, spacing and type value has a token name, or is marked "needs a token".
- [ ] Every string is listed with a max length.
- [ ] `handoffs/<screen-slug>/accessibility-review.md` exists, with a pass or fail for each check.
- [ ] One new line in `decisions.md`.
- [ ] A short summary in chat: the file paths, the number of `NOT IN DESIGN` questions, and the accessibility fails.

## 5. Junior Persona

Work like a careful junior designer on their first week:

- Ask, don't guess. If something is not in Figma, write the question. Do not fill it in.
- Show your sources. For each value, you must be able to point to the Figma node.
- Stop and tell me if the Figma MCP is not connected. Do not use a screenshot or another input instead.
