# Accessibility review: Kestrel Case (Response+Delivery) - Option B

Frame 6750:1196, handoff at handoffs/kestrel-case-option-b/handoff.md
Result: FAIL (26 fails)

Reviewer: `a11y-reviewer` subagent (read-only), 2026-10-22. Saved by the main session, text unchanged.

Method: I used only values in the spec and the reference image. Contrast ratios come from the Contrast table (contrast.py); I did not recalculate them. Each table row is one result. Rows that cover several nodes count once.

Important note on the Contrast table: the "AA large" column says "pass" for many 14 to 16 px texts. Large text is 24 px or more, or 18.66 px or more and bold. Only the 20 px Bold texts qualify. So for 14 to 16 px text I use the "AA normal" column only.

## 1. Text contrast (WCAG 1.4.3, 1.4.11)

| # | Check | Element (node) | Result | Why | Fix or question |
|---|---|---|---|---|---|
| 1 | Contrast | Search placeholder and `search` icon (6750:1230, 6750:1226) | FAIL | "Search placeholder #BFBFBF (16) / FFFFFF / 1.84:1 / FAIL" | Use a color of 4.5:1 or more (icon: 3:1 or more). |
| 2 | Contrast | Sort arrow `arrow_downward_alt` (6750:1239) | FAIL | "Sort arrow icon #A3A3A3 ... FDFDFD / 2.48:1" (needs 3:1) | Darken the arrow to 3:1 or more. |
| 3 | Contrast | Dark #222222 texts: "Subject" header 6750:1237, "Response"/"Delivery" headers 6750:1244 and 6750:1252, row subjects, detail title 6750:1422, findings 6750:1441 and 6750:1601, values 6750:1446 and 6750:1606, timeline labels, next decision 6750:1470 and 6750:1626, button labels, "#client-kestrel" 6750:1489 and 6750:1645, date pills, latest message name | PASS | 15.64:1 and 15.91:1 | None. |
| 4 | Contrast | Queue client name #666666 (6750:1270), "6 items" #686868 (6750:1383), timeline meta #6D6D6D (6750:1456) | PASS | 5.74:1, 5.57:1, 5.17:1 | None. |
| 5 | Contrast | Queue Response timer and "Client dissatisfaction" #FF4800, 16 Medium (6750:1273, 6750:1294, 6750:1333, 6750:1355, 6750:1376) | FAIL | "3.40:1 / FAIL" normal. 16 Medium is not large text. | Darker orange, or ask the designer for an AA orange. |
| 6 | Contrast | Queue Delivery reason #B27E08, 16 Medium (6750:1276, 6750:1314) | FAIL | "3.57:1 / FAIL" normal | Darker gold. |
| 7 | Contrast | Queue person names #7B7B7B (6750:1274, 6750:1277, 6750:1295, 6750:1315, 6750:1334, 6750:1356, 6750:1377, 6750:1380) | FAIL | "4.23:1 / FAIL" | Use #666666 or darker (5.74:1 in spec). |
| 8 | Contrast | Footer "Last checked" and times #848484, 14 (6750:1385, 6750:1394, 6750:1406) | FAIL | "3.74:1 / FAIL" | Use #686868 (5.57:1 in spec). |
| 9 | Contrast | Detail header client #808080, 14 (6750:1423) | FAIL | "3.95:1 / FAIL" | Darken. |
| 10 | Contrast | Response label and status #FF4800, 16 (6750:1434, 6750:1435) | FAIL | "3.40:1 / FAIL" | Same as row 5. |
| 11 | Contrast | Delivery label and status #B27E08, 16 (6750:1594, 6750:1595) | FAIL | "3.57:1 / FAIL" | Same as row 6. |
| 12 | Contrast | Section labels #999999, 14 ("What QTalo found" 6750:1440 and 6750:1600, "Who's waiting" 6750:1445, "Owed by" 6750:1605, "How it got here" 6750:1450 and 6750:1610, "Next decision" 6750:1468 and 6750:1624) | FAIL | "2.85:1 / FAIL" | Darken to 4.5:1 or more. |
| 13 | Contrast | "Evidence in" #999999, 14 (6750:1488, 6750:1644) | FAIL | "2.85:1 / FAIL" | Same as row 12. |
| 14 | Contrast | Timeline "Needs response" #FF4800 (6750:1463) and "Promise made" #B27E08 (6750:1619), 14 | FAIL | "3.40:1" and "3.57:1", both FAIL normal | Darken. |
| 15 | Contrast | Older messages at 60% opacity: name 4.29:1, time 1.98:1, tag 1.40:1, body 1.96:1, avatar initial 1.62:1 (groups 6750:1501, 6750:1535, 6750:1559, 6750:1657) | FAIL | All FAIL normal in the table. The body text of the thread is hard to read. | Do not lower opacity on text. Use a solid color of 4.5:1 or more to show "older". |
| 16 | Contrast | Latest message time #898989 (3.50:1) and body #8B8B8B (3.41:1) (6750:1570, 6750:1668) | FAIL | Both FAIL normal | Darken to 4.5:1 or more. |
| 17 | Contrast | Latest message tags "Response" #FF4800 (6750:1583) and "Promise made" #B27E08 (6750:1681), 14 | FAIL | "3.40:1", "3.57:1" | Darken. |
| 18 | Contrast | Latest message avatar initial #FFFFFF on #A8A8A8, 16 (6750:1566 and 6750:1664 area) | FAIL | "2.38:1 / FAIL" | Darker avatar fill. |
| 19 | Contrast | Button border #000000 (6750:1472, 6750:1477, 6750:1628, 6750:1633) | PASS | "21.00:1" (needs 3:1) | None. |
| 20 | Contrast | Hidden "/ 3h" #A1A1A1 (6750:1312) | CANNOT VERIFY | "opacity 0 now". If it is ever shown it fails at 2.58:1. | Remove the layer, or give it a passing color. |
| 21 | Contrast | Background of all rows (6750:1196) | CANNOT VERIFY | "fill of 6750:1196 not read; the render looks white" (Open question 1). Every row assumes #FFFFFF. | Confirm the fill. |
| 22 | Contrast | Non-text pairs with no table row: `reply` #FF4800, `timer` #B27E08, `keyboard_arrow_down`, timeline dots #FF4800 and #B27E08 and #222222, connector #C5C5C5 (6750:1239, 6750:1248, 6750:1485, 6750:1641) | CANNOT VERIFY | The table does not list these pairs. Only the open dot (19.86:1) is given. | Add rows. Icons that carry meaning need 3:1. |

## 2. Target size (WCAG 2.5.8)

| # | Check | Element (node) | Result | Why | Fix or question |
|---|---|---|---|---|---|
| 23 | Target size | Search field (6750:1226) | PASS | "72 high"; the queue panel is 926 wide | None. |
| 24 | Target size | Queue rows (6750:1255, 6750:1279, 6750:1298, 6750:1318, 6750:1337, 6750:1361) | PASS | "97 high (121 when the subject wraps)" in a 926 wide panel | None. |
| 25 | Target size | Buttons "Response sent" 6750:1472, "No response needed" 6750:1477, "Mark completed" 6750:1628, "Correct" 6750:1633 | PASS | "100 x 29", "134 x 29", "109 x 29", "79 x 30" | None. |
| 26 | Target size | "Evidence in" bar (6750:1485, 6750:1641) | PASS | "48 high", column is 460.5 wide. Only if it is a toggle. | Confirm it is interactive. |
| 27 | Target size | Column headers "Response" 6750:1239 and "Delivery" 6750:1248 | CANNOT VERIFY | Header is 48 high, but the spec says "NOT IN DESIGN: is the header clickable to sort?" | Answer the sort question. |

## 3. Focus (WCAG 2.4.3, 2.4.7)

| # | Check | Element (node) | Result | Why | Fix or question |
|---|---|---|---|---|---|
| 28 | Focus visible | Search field (6750:1226) | FAIL | "NOT IN DESIGN: focus ring and typed-text color?" | Draw the focus ring (3:1 or more against the background). |
| 29 | Focus visible | Queue rows (6750:1255 and siblings) | FAIL | "NOT IN DESIGN: keyboard focus style for a row?" The selected style (orange left border) cannot double as focus. | Design a focus style that is different from selected. |
| 30 | Focus visible | Buttons 6750:1472, 6750:1477, 6750:1628 and dropdown 6750:1633 | FAIL | "NOT IN DESIGN: focus style?" for all four | Draw focus for button and dropdown. |
| 31 | Focus visible | "Evidence in" bars (6750:1485, 6750:1641) | FAIL | "NOT IN DESIGN: focus style?" | Draw focus. |
| 32 | Focus visible | Column headers 6750:1239, 6750:1248 (and "Subject" 6750:1237) | FAIL | "NOT IN DESIGN: focus style?" | Draw focus if they are interactive. |
| 33 | Focus | "Correct" menu (6750:1633) | CANNOT VERIFY | "The menu is not drawn." No focus handling is possible to judge. | Design the menu, with focus and Escape behavior. |
| 34 | Focus order | Whole screen | CANNOT VERIFY | The spec does not give a focus order. | Proposed order: search, queue rows (top to bottom), Response column (decision buttons, evidence bar, thread), Delivery column (same). Confirm. |
| 35 | Focus | Thread scroll areas (6750:1495, 6750:1651) | CANNOT VERIFY | "overflow-y: auto" with no note on keyboard scrolling | Make the area focusable if it scrolls, with a visible focus style. |

## 4. Labels and alt text (WCAG 1.1.1, 1.3.1, 4.1.2)

| # | Check | Element (node) | Result | Why | Fix or question |
|---|---|---|---|---|---|
| 36 | Label | Search field (6750:1226) | FAIL | Only the placeholder "Search"; no visible label or accessible name in the spec | Give an accessible name (for example "Search queue"). Do not rely on the placeholder. |
| 37 | Alt text | Source logos: Slack and Gmail in rows, detail header Slack logo, Brand Icon 6750:1487 and 6750:1643, footer Gmail and Slack icons beside the times (6750:1394, 6750:1406) | FAIL | They tell the source, but the spec has no alt text. In the footer, the time has no source name in text. | Add alt text ("Slack", "Gmail"). |
| 38 | Alt text | `reply`, `timer`, `keyboard_arrow_down`, `search`, `check` icons and avatar initials D and M | FAIL | Not marked as decorative, and no alt text. The spec only names them as Material Symbols. | Mark as decorative where a text label sits beside them. |
| 39 | Name | Sort arrow (6750:1239) | FAIL | The arrow shows sort direction, but the spec has no name or sort state | Add sort state ("sorted by Response, descending"). |
| 40 | Label | Buttons 6750:1476, 6750:1481, 6750:1632, 6750:1634 | PASS | Visible labels "Response sent", "No response needed", "Mark completed", "Correct" | None. |
| 41 | Name and state | "Correct" dropdown and "Evidence in" bar | CANNOT VERIFY | Down arrow, but no expanded or collapsed state in the spec. | Say what the toggle state is. |
| 42 | Name | Queue row accessible name and selected state | CANNOT VERIFY | The spec does not say how a row is announced or how "selected" is announced | Define the row name and the selected state. |
| 43 | Name | Hidden layers (6750:1296, 6750:1312, 6750:1335, 6750:1358, 6750:1379; rail "Filters" 6750:1202) | CANNOT VERIFY | Opacity 0 text may still be read by a screen reader | Hide from the accessibility tree or remove. |

## 5. Color alone (WCAG 1.4.1)

| # | Check | Element (node) | Result | Why | Fix or question |
|---|---|---|---|---|---|
| 44 | Color alone | Selected row (6750:1255) | FAIL | "left border 5 px #FF4800, fill #FFFFFF"; the unselected row has no fill and the page is white. So selected is shown by orange color only. | Add a second cue (fill, bold, icon) and `aria-current`. |
| 45 | Color alone | Response vs Delivery | PASS | Text labels "Response" / "Delivery" plus icons | None. |
| 46 | Color alone | "overdue" vs "until target" | PASS | Text says "47m overdue" and "17m until target", not only red. The shared red is a design question (Open question 8). | None for a11y. |
| 47 | Color alone | Timeline dots (6750:1455 to 6750:1464, 6750:1615 to 6750:1620) | PASS | Each dot has a text label beside it | None. |
| 48 | Color alone | Latest message vs older (6750:1570, 6750:1668) | PASS | Colored tag has text ("Response", "Promise made") and an icon | None. |
| 49 | Color alone | Error or status states | CANNOT VERIFY | No error state is drawn | Design error states with text and an icon. |

## 6. Other

| # | Check | Element | Result | Why | Fix or question |
|---|---|---|---|---|---|
| 50 | Reflow and resize (1.4.4, 1.4.10) | Whole screen | CANNOT VERIFY | "only one frame, 1920 wide" | Show behavior at 1280 and at 200% zoom. |

Notes for the designer:
- The biggest problem is contrast. Orange #FF4800 and gold #B27E08 are the brand colors for Response and Delivery. Both are about 3.4 to 3.6:1 on white, so they fail at 14 to 16 px. Pick darker versions for text, and keep the current ones for icons and dots only if they reach 3:1.
- Thread text is the most unreadable part (1.4 to 3.5:1). The 60% opacity for older messages is the main cause. Use a solid color instead.
- No focus state exists for any control. Please draw one focus style and reuse it. Keep selected and focus visibly different.
- The table "AA large" column can mislead: 14 to 16 px Medium text is not large text.
- Please add alt text or "decorative" for every logo and icon, and an accessible name for the search field.
- Selected row needs a second cue besides the orange border.
- Open questions that block checks: page background (row 21), whether column headers and the evidence bar are interactive, "Correct" menu, focus order.
- This automated review supports a manual check. It does not replace it. Keyboard, screen reader and zoom tests are still needed on the built screen.

## Summary

Total 50 checks: 12 pass, 26 fail, 12 cannot verify.
- Contrast: 3 pass (rows 3, 4, 19), 16 fail, 3 cannot verify.
- Target size: 4 pass, 0 fail, 1 cannot verify.
- Focus: 0 pass, 5 fail, 3 cannot verify.
- Labels and alt text: 1 pass, 4 fail, 3 cannot verify.
- Color alone: 4 pass, 1 fail, 1 cannot verify.
- Other: 1 cannot verify.
