---
name: handoff-spec
description: Writes a developer handoff spec for one finished Figma screen (states, tokens, copy, behavior) from a Figma link, using the Figma MCP. Use when the user asks for a "handoff", "dev handoff", "handoff spec", "spec for developers" or "document this screen", or gives a figma.com design link and wants it documented for developers. Always uses the template in references/handoff-template.md and the contrast script in scripts/contrast.py.
---

# Handoff spec

Turn one finished Figma frame into `handoffs/<screen-slug>/handoff.md`.
A developer must be able to build the screen from this file without a meeting.

## Steps

1. **Get the link.** Read the file key and node id from the URL (`node-id=12-34` becomes `12:34`). If there is no link, ask for one and stop.
2. **Read the frame with the Figma MCP (read-only).** The tools are named `mcp__figma__*` (from `.mcp.json`) or `mcp__plugin_figma_figma__*` (from the Figma plugin). Use whichever is connected. If neither is connected, stop and say so. If the Figma plugin asks you to load its `figma-design-to-code` skill before `get_design_context`, load it.
   - `get_metadata`: the layer tree and the main sections.
   - `get_variable_defs`: the Figma variables (tokens). If it returns `{}`, the frame has no variables. Say so in the Tokens section.
   - Read the **page background**: the fill of the top frame. A leaf node does not carry its parent's fill, so read the first (root) line of the frame's design context. If the Figma MCP saves a large output to a file, you may read that file (only the lines you need, for example with `head` or `jq`). Do not assume white.
   - `get_screenshot`: save it as `handoffs/<screen-slug>/figma-reference.png`.
   - `get_design_context`: exact values and text. For a big frame (more than about 6 main sections), call it on each main section, not the whole frame. This keeps the context small.
3. **Use the template.** Read `references/handoff-template.md`. Write `handoffs/<screen-slug>/handoff.md` in ONE Write call, already filled in, with every heading kept. Do not write the empty template first: the `check-handoff` hook checks every write.
4. **Fill each section from Figma only.**
   - States: for each interactive element, fill Default, Hover, Focus, Disabled, Loading, Empty, Error. If Figma does not show a state, write `NOT IN DESIGN:` and a question.
   - Tokens: use the variable name. A raw value with no variable is listed as "needs a token".
   - Copy: every string, exactly as in Figma, with a max length. Base the max length on the space in the layout; if it is not clear, write `NOT IN DESIGN:`.
   - Behavior: interactions, breakpoints and edge cases that the frame or its notes show.
5. **Check contrast with the script.** For every text and background pair, run:
   `python3 .claude/skills/handoff-spec/scripts/contrast.py <text-hex> <bg-hex> --size <px> [--bold]`
   - Always give `--size` (and `--bold` for weight 700 or more). The script then prints the one AA rule that applies.
   - Icons, dots and borders that carry meaning (status, selection): run with `--icon` (needs 3:1). One row each. Icon colors are inside the SVG assets: read the `fill` from the asset URL in the design context (`curl -s <url> | grep -o 'fill="#[0-9A-Fa-f]*"'`). For a multi-color logo, check the color with the lowest contrast.
   - A fill and its text both inside one opacity group (for example an avatar letter): add `--inner-bg <fill-hex>` with `--opacity`.
   - Text inside a group or layer with opacity: add `--opacity <value>`, for example `--opacity 0.6`. The script blends the color first.
   - Write **one row per text use** in the Copy table (for example "Subject header" and "date pill" get their own rows, even if they share a color). The reviewer checks each use.
   Paste each printed row into the Contrast table, with the text use in the first column.
6. **Count, don't estimate.** Any number in the spec or the summary (NOT IN DESIGN questions, fails) comes from `grep -c`, not from memory.
7. **Ask the `a11y-reviewer` subagent** to review the spec. Recount its pass, fail and "cannot verify" rows with `grep -c` and correct its summary if needed. Save its answer as `handoffs/<screen-slug>/a11y-review.md`, and copy its summary into the Accessibility section.
8. **Optional: HTML mockup.** Only if the user asks, build `handoffs/<screen-slug>/mockup.html` from the same values, with tokens as CSS custom properties on `:root`.

## Rules

- Never invent a value, string or state.
- Never write a raw value where a token exists.
- The `check-handoff` hook will block the file if a required section is empty. Fix the section; do not delete the heading.
