# Accessibility review: Kestrel Case (Response+Delivery) - Option A
Result: FAIL (27 fails, 4 cannot verify, 14 pass)

Reviewer: `accessibility-reviewer` subagent, 2026-10-22. Saved by the main session (the subagent is read-only).

Source: handoff.md (frame 6750:1705) and figma-reference.png. Ratios come from the spec's Contrast table (scripts/contrast.py). I did not recompute them. All text is 20 px or smaller and none is 24 px, so the AA normal column (4.5:1) is the one that counts. No text is 18.66 px or larger and bold, except possibly the 20 px Bold statements, which only matter if they pass anyway.

## 1. Text contrast

| # | Check | Element | Result | Why | Fix or question |
|---|---|---|---|---|---|
| C1 | Contrast | #222222 primary text on #FFFFFF | Pass | 15.91:1 | None |
| C2 | Contrast | #222222 column header on #FDFDFD | Pass | 15.64:1 | None |
| C3 | Contrast | #666666 queue client name on #FFFFFF | Pass | 5.74:1 | None |
| C4 | Contrast | #FF4800 Response reason, timers, "Response" tag and title (6750:1782, 1944, 2092) on #FFFFFF | Fail | 3.40:1, needs 4.5:1. Text is 16 px Medium and 14 px Semi Bold | Designer: pick a darker orange for text. Keep #FF4800 for the border and icons. Re-run contrast.py |
| C5 | Contrast | #B27E08 Delivery reason, "Delivery" label, "Promise made" tag (6750:1785, 2104, 2190) on #FFFFFF | Fail | 3.57:1 | Darker gold for text. Re-run contrast.py |
| C6 | Contrast | #7B7B7B queue person name on #FFFFFF | Fail | 4.23:1 | Darken the gray a little |
| C7 | Contrast | #BFBFBF search placeholder (6750:1739) on #FFFFFF | Fail | 1.84:1, fails even large text | Much darker placeholder |
| C8 | Contrast | #686868 "6 items" on #FFFFFF | Pass | 5.57:1 | None |
| C9 | Contrast | #848484 "Last checked" and footer times on #FFFFFF | Fail | 3.74:1 | Darken to 4.5:1 or more |
| C10 | Contrast | #808080 detail header client name on #FFFFFF | Fail | 3.95:1 | Darken |
| C11 | Contrast | #999999 section labels ("What QTalo found", "Who's waiting", "Evidence in") on #FFFFFF | Fail | 2.85:1, fails even large text | Darken. This color is used in many places |
| C12 | Contrast | #898989 thread time, latest message on #FFFFFF | Fail | 3.50:1 | Darken |
| C13 | Contrast | #8B8B8B thread body, latest message on #FFFFFF | Fail | 3.41:1 | Darken |
| C14 | Contrast | #FFFFFF avatar initial on #A8A8A8 (latest message) | Fail | 2.38:1 | Darker avatar fill or dark initial |
| C15 | Contrast | #7A7A7A thread name, older message (60% opacity) | Fail | 4.29:1 | Do not use opacity to dim text, or keep text at 4.5:1 after dimming |
| C16 | Contrast | #B8B8B8 thread time, older message | Fail | 1.98:1 | Same as C15 |
| C17 | Contrast | #DADADA thread tag "• Original ask", "• Team acknowledge", older message | Fail | 1.40:1 | Same as C15 |
| C18 | Contrast | #B9B9B9 thread body, older message | Fail | 1.96:1 | Same as C15 |
| C19 | Contrast | #FFFFFF avatar initial on #CBCBCB, older message | Fail | 1.62:1 | Same as C15 |
| C20 | Contrast | Text colors with no row: "Subject" header text color, date pill text color (Monday, Tuesday, Today), and the hidden "/ 3h" in #A1A1A1 (6750:1821) | Fail | Pair not checked. The spec gives no color for "Subject" and the date pills. The Tokens section says the pill border is #DDDDDD but not the text color. #A1A1A1 is hidden (opacity 0) | Add the colors and rows. If the hidden text is not built, say so |

Notes: the page background #FFFFFF is an assumption in the spec (open question 3: "The screenshot looks white. Confirm #FFFFFF?"). All ratios depend on it. Non-text contrast (1.4.11) also needs a value for divider lines, the search icon color and the control borders. Dividers are "NOT IN DESIGN". The #000000 button border is fine by value.

## 2. Target size (24 x 24 CSS px or more)

| # | Check | Element | Result | Why | Fix or question |
|---|---|---|---|---|---|
| T1 | Target size | Buttons "Response sent" 120 x 30 (6750:1981), "No response needed" 134 x 29 (6750:1986), "Mark completed" 129 x 30 (6750:2137), "Correct" 79 x 30 (6750:2142) | Pass | All are above 24 x 24 | None |
| T2 | Target size | Queue rows (6750:1765 and siblings) | Pass | "row 97 high (121 when the subject wraps)", panel 926 wide | None |
| T3 | Target size | Search field (6750:1735) | Pass | Bar is 72 high and 926 wide | None |
| T4 | Target size | "Evidence in #client-kestrel" toggles (6750:1994, 2150) | Pass | "48 high", in a 412.5 px column | None |
| T5 | Target size | Column header "Response" with sort arrow (6750:1748) | Pass | Header is 48 high, cell about 215 px wide. Whether it is clickable is NOT IN DESIGN | Confirm if it is interactive |

## 3. Focus

| # | Check | Element | Result | Why | Fix or question |
|---|---|---|---|---|---|
| F1 | Focus | Search field (6750:1735) | Fail | "NOT IN DESIGN: focus ring and typed-text color?" | Design a visible focus ring |
| F2 | Focus | "Response" sort header (6750:1748) and "Delivery" header (6750:1757) | Fail | "NOT IN DESIGN: focus style?" | Design focus. Say if the headers are buttons |
| F3 | Focus | Queue rows | Fail | "NOT IN DESIGN: keyboard focus style for a row?" | Design row focus. The selected look (5 px border) must not be the only focus cue |
| F4 | Focus | Buttons "Response sent", "No response needed", "Mark completed", "Correct" | Fail | "NOT IN DESIGN: focus style?" for all four | Design focus once as a shared button style |
| F5 | Focus | Evidence toggles (6750:1994, 2150) | Fail | "NOT IN DESIGN: focus style?" | Design focus |
| F6 | Focus | "Correct" dropdown menu | Fail | "The menu is not drawn" | Draw the menu, its options and focus inside it |
| F7 | Focus | Thread messages | Cannot verify | "NOT IN DESIGN: is a message interactive?" | Answer first. If interactive, add focus |
| F8 | Focus | Focus order | Cannot verify | The spec has no focus order. Reading order from the screenshot is: rail, search, headers, rows, footer, detail header, Response column (buttons, evidence), Delivery column (buttons, evidence) | Write the focus order in section 6. Check that the two detail columns are read one after the other |

## 4. Labels and alt text

| # | Check | Element | Result | Why | Fix or question |
|---|---|---|---|---|---|
| L1 | Labels | The 4 buttons | Pass | Visible text labels: "Response sent", "No response needed", "Mark completed", "Correct" | None |
| L2 | Labels | Search field (6750:1735) | Fail | Only a placeholder "Search" with a search icon. No visible label or accessible name in the spec | Add an accessible name, for example "Search the queue". Confirm the text |
| L3 | Labels | Source logos in queue rows (Slack, Gmail, "Icon svg" frames) | Fail | Meaningful (they show the source). No alt text in the spec | Add alt text such as "Slack" or "Gmail". Designer to confirm |
| L4 | Labels | Detail header Slack logo (26 px) and "Brand Icon" in the evidence toggles (6750:1996, 2152) | Fail | No alt text or decorative mark | Alt text, or mark decorative if the text next to it says the source |
| L5 | Labels | Sort arrow `arrow_downward_alt` (6750:1748) | Fail | It shows a sort, but the spec has no name or sort direction. "NOT IN DESIGN: sort rule" | Add a name and the direction ("sorted by Response, descending") |
| L6 | Labels | Evidence toggles name | Pass | Visible text "Evidence in #client-kestrel" | None |
| L7 | Labels | Evidence toggle open/closed state, "Correct" dropdown semantics | Cannot verify | "NOT IN DESIGN: default open or closed, and the closed look." Dropdown menu is not drawn | Add the expanded and collapsed states and what is announced |
| L8 | Labels | Other icons (`reply`, `timer`, `check`, `keyboard_arrow_down`), avatars with initials, app logo "QTalo-logo" | Fail | Not marked as decorative or given alt text | Mark `check`, `keyboard_arrow_down` and avatars decorative (the name is next to them). Give "QTalo" alt text if the logo is a link. State it in the spec |

## 5. Color alone

| # | Check | Element | Result | Why | Fix or question |
|---|---|---|---|---|---|
| K1 | Color alone | Selected queue row | Pass | "left border 5 px #FF4800" is a shape cue, not only hue. The orange border on white is 3.40:1, above the 3:1 needed for non-text | Add a programmatic selected state (aria-selected or current) in section 6 |
| K2 | Color alone | Response vs Delivery reasons and overdue status | Pass | The cells have text ("47m overdue", "Delivery promise missed") and the column headers have icons and names | None. The cells in the queue have no icon, so a screen reader needs the column name |
| K3 | Color alone | Latest vs older thread messages | Pass | The latest message has a tag with icon and text ("Response", "Promise made"). Dimming is extra | None |
| K4 | Color alone | Unread or read look: subjects rows 1 to 3 Semi Bold, rows 4 to 6 Regular | Cannot verify | Open question 4: meaning not known. It is weight, not color, but may carry meaning | Say what it means. If it means unread, add text or a name for screen readers |

## Notes for the designer

- 16 of 20 contrast rows fail. The biggest groups: the two status colors (#FF4800, #B27E08), the light grays (#999999, #BFBFBF, #8B8B8B, #848484, #898989) and all 60% opacity messages. A short list of 3 or 4 darker text colors would fix most rows. Please re-run contrast.py after the change.
- Do not use opacity to dim text. Use a color that still passes.
- No focus, hover, disabled or error state is drawn (spec open question 13). Focus is required for AA. A shared focus ring for all controls is the fastest fix.
- Please add alt text or "decorative" for every icon and logo, and a name for the search field and the sort control.
- Spec questions that block checks: are the column headers clickable, are thread messages interactive, what is in the "Correct" menu, what does the Semi Bold subject mean.
- Not covered because the spec has no information: breakpoints (only 1920 px; reflow and zoom 1.4.10 cannot be checked), the dividers color, error and empty states, and any motion.
- This is an automated review. It supports a manual check with a keyboard and a screen reader. It does not replace it.
