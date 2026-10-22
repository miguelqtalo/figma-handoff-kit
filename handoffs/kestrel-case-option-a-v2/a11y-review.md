# Accessibility review: Kestrel Case (Response+Delivery) - Option A
Result: FAIL (28 fails)

Reviewer: `a11y-reviewer` subagent, 2026-10-22, on `handoff.md` in this folder. Saved by the main session (the reviewer is read-only).

Rows are grouped by element. A group row counts as one result.

| # | Check | Element | Result | Why | Fix or question |
|---|---|---|---|---|---|
| 1 | Contrast | Search placeholder and search icon (6750:1739, 1736) | fail | Table: #BFBFBF on #FFFFFF = 1.84:1, needs 4.5:1 (text) and 3:1 (icon) | Use a darker gray, 4.5:1 or more for the placeholder, 3:1 or more for the icon |
| 2 | Contrast | Row Response clock or reason (6750:1782, 1803, 1842, 1864, 1885) | fail | Table: #FF4800 on #FFFFFF, 16px = 3.40:1, needs 4.5:1 | Darker orange for text. Keep #FF4800 only for borders and icons |
| 3 | Contrast | Row person names (6750:1783, 1804, 1786, 1824, 1843, 1865, 1886) | fail | Table: #7B7B7B on #FFFFFF, 16px = 4.23:1, needs 4.5:1 | Darken a little, for example to #767676 or darker |
| 4 | Contrast | Row Delivery reason (6750:1785, 1823) | fail | Table: #B27E08 on #FFFFFF, 16px = 3.57:1 | Darker gold for text |
| 5 | Contrast | Footer "Last checked" and timestamps (6750:1894, 1903, 1915) | fail | Table: #848484 on #FFFFFF, 14px = 3.74:1 | Darken to 4.5:1 or more |
| 6 | Contrast | Detail header customer "Kestrel Apparel Co." (6750:1932) | fail | Table: #808080 on #FFFFFF, 14px = 3.95:1 | Darken to 4.5:1 or more |
| 7 | Contrast | Response panel title, clock and thread "Response" tag (6750:1943, 1944, 2092) | fail | Table: #FF4800 on #FFFFFF = 3.40:1 (16px and 14px) | Same fix as row 2 |
| 8 | Contrast | Delivery panel title, reason and "Promise made" tag (6750:2103, 2104, 2190) | fail | Table: #B27E08 on #FFFFFF = 3.57:1. Bold 16px is not large text | Same fix as row 4 |
| 9 | Contrast | Field labels, "Owed by", "Evidence in" (6750:1949, 1954, 2215, 1977, 2109, 2219, 2133, 2114, 1997, 2153) | fail | Table: #999999 on #FFFFFF, 14px = 2.85:1 | Darken to 4.5:1 or more |
| 10 | Contrast | Older thread messages at 60% opacity: name, time, tag, body, avatar letter (6750:2016 to 2076, 2172 to 2174) | fail | Table: 4.29:1 (name), 1.98:1 (time), 1.40:1 (tag), 1.96:1 (body), 1.62:1 (avatar letter). Needs 4.5:1 | Do not use opacity to show "older". Use a darker color that stays at 4.5:1 or more, or another cue |
| 11 | Contrast | Last message time, body and avatar letter (6750:2087, 2185, 2093, 2191, 2082, 2180) | fail | Table: #898989 = 3.50:1, #8B8B8B = 3.41:1, white on #A8A8A8 = 2.38:1 | Darken the text and the avatar fill |
| 12 | Contrast | Sort arrow icon (6750:1754) | fail | Table: #A3A3A3 on #FDFDFD = 2.48:1, needs 3:1 | Darken to 3:1 or more |
| 13 | Contrast | Primary text #222222, row customer #666666, footer count #686868, titles, buttons, dates, channel names | pass | Table: 5.57:1 to 15.91:1 | None |
| 14 | Contrast | Non-text: reply and timer icons, selected row border, Slack/Gmail logos, check and arrow icons, button borders | pass | Table: 3.34:1 to 21.00:1, needs 3:1 | None |
| 15 | Target size | Buttons "Response sent", "No response needed", "Mark completed", "Correct" | pass | Spec: "120 x 30", "134 x 29", "129 x 30", "79 x 30" | None |
| 16 | Target size | Queue rows | pass | Spec: "97 px (one-line title), 121 px (two-line title, row 6)", 926 px wide | None |
| 17 | Target size | Evidence bar and expand arrow (6750:1994, 2150) | pass | Spec: "462 x 48" | None |
| 18 | Target size | Sort arrow (6750:1754) and search field | pass | Spec: "arrow_downward_alt 24 x 24"; "Search bar (72 high)". Meets 24 x 24 | If the arrow is a button, make the whole header cell the target |
| 19 | Target size | Hidden controls: panel collapse arrows (6750:1945, 2105), source filters (6750:1711), "Correct" menu items | cannot verify | Filters are "48 x 48" but hidden. Collapse arrows and menu items have no size | Tell us if these ship, and give sizes |
| 20 | Focus | Search field | fail | Spec: "NOT IN DESIGN: what does the focus ring look like" | Q: focus style, 2 px outline at 3:1 or more? |
| 21 | Focus | Sort arrow | fail | Spec: "NOT IN DESIGN: focus style?" | Q: focus style? Is it keyboard operable? |
| 22 | Focus | Queue rows (selected and not selected) | fail | Spec: "NOT IN DESIGN: focus style of a row?" | Q: focus style, and keyboard to select a row? |
| 23 | Focus | Four action buttons | fail | Spec: "NOT IN DESIGN: focus style?" (all four) | Q: focus style for buttons? |
| 24 | Focus | Evidence bar (both columns) | fail | Spec: "NOT IN DESIGN: focus style?" | Q: focus style? |
| 25 | Focus | Evidence thread scroll area | fail | Spec: "NOT IN DESIGN: can the thread get keyboard focus to scroll?" | Q: should the area be focusable, with a visible focus style? |
| 26 | Focus | Focus order | fail | The spec has no focus order. Visual reading order is search, list, Response column, Delivery column | Specify: search, sort, rows, Response buttons, Response evidence, Delivery buttons, Delivery evidence |
| 27 | Labels | Search field | fail | Only the placeholder "Search". No visible label or accessible name in spec | Add the accessible name, for example "Search items" |
| 28 | Labels | Sort arrow (6750:1754) | fail | Icon-only, no name or state. Spec: "does it sort by Response urgency?" | Add the name and state, for example "Sort by Response, descending" |
| 29 | Labels | Row source icons Slack and Gmail (6750:1768, 1792 ...) | fail | No alt text, no decorative mark | Alt "Slack" or "Gmail", or mark decorative if the source is in the text |
| 30 | Labels | Slack Brand Icon in detail header and evidence bars (6750:1921, 1996, 2152) | fail | No alt text in spec | Alt "Slack", or decorative inside "Evidence in #client-kestrel" |
| 31 | Labels | QTalo logo (6750:1709) | fail | No alt text. The spec says "a logo, not a control" only for contrast | Give alt "QTalo", or the link name if it is a link |
| 32 | Labels | Reply, timer, check and arrow icons next to text | fail | Spec does not mark them decorative | Mark as decorative (aria-hidden) |
| 33 | Labels | Avatar letters "D" and "M" | fail | Not marked decorative or named. The name is next to it | Mark decorative |
| 34 | Labels | Evidence bar expand arrow | fail | Spec: "what does the arrow ... do (collapse the thread, or open in Slack)?" No expanded state | Define the behavior and aria-expanded, or a link name |
| 35 | Labels | Four action buttons | pass | Visible labels: "Response sent", "No response needed", "Mark completed", "Correct" | None |
| 36 | Labels | "Correct" dropdown menu | cannot verify | Spec: "what options are in the menu?" No menu role or name | Give the options and the menu name |
| 37 | Color alone | Selected row (6750:1764) | fail | Selection is shown by the 5 px #FF4800 border; the fill is #FFFFFF, same as other rows | Add a second cue (fill or weight) and aria-current |
| 38 | Color alone | "overdue" vs "until target" | pass | Same #FF4800 but the text says "47m overdue" / "17m until target" | None |
| 39 | Color alone | Response vs Delivery | pass | Color plus icon (reply, timer) and label text | None |
| 40 | Color alone | Row title weight Semi Bold vs Regular (rows 1 to 3 vs 4 to 6) | cannot verify | Spec: "does the weight mean unread or something else?" If it means unread, weight alone is not enough | Answer the question. Add a text or icon cue if it means unread |

Notes for the designer:
- Fix the colors first. 25 text uses and 2 icons fail contrast. The fixes group into four: #FF4800 text, #B27E08 text, light grays (#999999, #BFBFBF, #848484, #808080, #898989, #8B8B8B, #7B7B7B, #A3A3A3), and the 60% opacity on older messages.
- No state is designed for focus, error, loading or empty on any control. Focus is a WCAG 2.2 AA need (2.4.7 and 2.4.11), so design it once and apply it to every control.
- Hidden opacity-0 texts are not checked. If any renders, check it. The "/ 3h" part is #A1A1A1 and would fail on white.
- Not checked: date pill border #DDDDDD and dividers, because text and layout carry the meaning. Tell us if a border is the only way to see an edge.
- Answer the open Behavior questions (click row, sort, buttons, evidence arrow). Several accessible names, roles and states depend on them.
- This automated review supports a manual check. It does not replace it. Test with a keyboard, a screen reader and zoom on the built screen.

Reference image viewed: the visible text matches the Copy table.

Count: 28 fail, 3 cannot verify, 9 pass (40 grouped rows)
