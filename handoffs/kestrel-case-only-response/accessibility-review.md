# Accessibility review: Kestrel Case (Only Response)
Result: FAIL (23 fails, 13 pass, 11 cannot verify)

> Note from the main session: the reviewer wrote "12 cannot verify". `grep` on the table rows counts 11 (23 + 13 + 11 = 47 checks), so the count is corrected here and in the notes below. The rows are unchanged.

Spec: handoffs/kestrel-case-only-response/handoff.md. I also read figma-reference.png. Related rows are grouped, so one row can cover several elements. I spot-checked the 60% blends (#222222 at 60% on white = #7A7A7A) and the fail counts. The spec's "25 text and 4 icon rows fail" matches my recount.

## 1. Text and non-text contrast

| # | Check | Element | Result | Why (spec quote) | Fix or question |
|---|---|---|---|---|---|
| 1 | Contrast | Search placeholder "Search" | fail | #BFBFBF on #FFFFFF, 16px, 1.84:1, needs 4.5:1 | Darken the placeholder. The reference shows it very pale. |
| 2 | Contrast | Orange text #FF4800: row clocks and reasons, "Response" and "47m overdue" in the detail, "Response" tag on the latest message | fail | 3.40:1 at 14 to 16px Medium or Semi Bold (not large), needs 4.5:1 | Use a darker orange for text. The icon and bar can stay, because they pass 3:1. |
| 3 | Contrast | "Client asked again" #B27E08 | fail | 3.57:1, needs 4.5:1 | Darken the gold for text. |
| 4 | Contrast | Person names #7B7B7B (rows 1 to 6 and Camille Ross in row 3) | fail | 4.23:1, needs 4.5:1 | Use #747474 or darker. |
| 5 | Contrast | Footer "Last checked" and the two times, #848484, 14px | fail | 3.74:1, needs 4.5:1 | Use the same gray as "7 items" (#686868, 5.57:1). |
| 6 | Contrast | Detail customer "Kestrel Apparel Co." #808080, 14px | fail | 3.95:1, needs 4.5:1 | Darken the text. |
| 7 | Contrast | Section labels #999999 ("What QTalo found", "Who's waiting", "Original ask", "Next decision", "Evidence in"), 14px | fail | 2.85:1 for all 5, needs 4.5:1 | Use a gray of 4.5:1 or more. |
| 8 | Contrast | Thread text at 60% opacity: date pills "Monday" and "Tuesday" (4.29:1), sender names (4.29:1), times (1.98:1), bodies (1.96:1), avatar letters (1.62:1) | fail | The spec blends the color before checking. All are below 4.5:1. | Do not dim read text with opacity. Use a solid color that passes, or mark "older" some other way. |
| 9 | Contrast | Latest message time #898989 (3.50:1) and body #8B8B8B (3.41:1) | fail | Both below 4.5:1 at 14 and 16px | Darken both. The body is the most important text in the thread. |
| 10 | Contrast | Avatar letter in the last message, white on #A8A8A8 | fail | 2.38:1, needs 4.5:1 | Darken the avatar fill. Or confirm the avatar is purely decorative, since the name is next to it. |
| 11 | Contrast | Search icon #BFBFBF | fail | 1.84:1, needs 3:1 | Darken the icon. |
| 12 | Contrast | Sort arrow #A3A3A3 | fail | 2.48:1, needs 3:1. It is the only sign of the sort direction. | Darken the arrow. |
| 13 | Contrast | Slack logo (#ECB22E, 1.91:1) and Gmail logo (#FBBC04, 1.71:1), "icon" rows | fail | The spec marks both FAIL against 3:1. | Brand logos may be exempt as essential. Designer decides. The source name is not written as text anywhere in the rows, so I keep this as a fail until the name is in the accessible name (see row 31). |
| 14 | Contrast | #222222 text (titles, headers, values, buttons, "Today" pill), #666666 customer names, #686868 "7 items" | pass | 5.74:1 to 15.91:1 | None. |
| 15 | Contrast | Bold large text (detail title, finding sentence) and icons: reply, timer, check, button border, selected bar, QTalo logo | pass | "20px bold" 15.91:1 against 3:1. Icons 3.34:1 to 21:1 against 3:1. | None. |
| 16 | Contrast | Search field boundary | cannot verify | "no border, no fill" (States). The field has an icon and placeholder, but no visible edge. | Question: does the field need a visible boundary? |
| 17 | Contrast | Text at opacity 0 (hidden Delivery cells, the row 3 clock "/ 3h" #A1A1A1) | cannot verify | "Not checked: text at opacity 0" | If these become visible, they must be checked first. |

## 2. Target size

| # | Check | Element | Result | Why | Fix or question |
|---|---|---|---|---|---|
| 18 | Target | "Response sent" 120 x 30, "No response needed" 134 x 29 | pass | Both above 24 x 24 | None. |
| 19 | Target | Queue rows 6 (926 wide, 24 px padding, row 6 is 121 px high) | pass | Large rows | None. |
| 20 | Target | Search bar | pass | "Search bar (72 high)", icon 24 px | None. |
| 21 | Target | Sort arrow 24 px | pass | "24 px" icon size | None. |
| 22 | Target | Evidence bar 462 x 48, if clickable | pass | "462 x 48" | None. Whether it is clickable is open (row 30). |
| 23 | Target | QTalo logo 32 x 32 (if it is a link) | pass | "32 x 32" | None. |
| 24 | Target | "Delivery" header (if sortable) and footer "Last checked" (if refresh) | cannot verify | The spec gives no width or height for these. Header row is 48 high. | Size not in spec. Give the size if they will be interactive. |

## 3. Focus

| # | Check | Element | Result | Why | Fix or question |
|---|---|---|---|---|---|
| 25 | Focus style | Search, sort header, Delivery header, rows (selected and not), both buttons, evidence bar, footer | fail | Focus column: "NOT IN DESIGN: focus style?" on every control. Section 6: "Figma has no focus order." | Design a visible focus ring. It must have 3:1 contrast and not be hidden by neighbors. |
| 26 | Focus after action | After "Response sent" or "No response needed" | fail | "NOT IN DESIGN: where focus goes after..." | Say where focus goes, for example to the next row. |
| 27 | Keyboard | Evidence thread scroll area (6750:2508) | fail | "overflow-y auto" and "NOT IN DESIGN: can the thread get keyboard focus to scroll?" | A scroll area needs keyboard access (tabindex 0 and an accessible name). Confirm. |
| 28 | Focus order | Proposed order 1 to 9 | cannot verify | The order follows the reading order (search, headers, rows, footer, buttons, evidence). But the spec marks it "NOT IN DESIGN: the designer must confirm". The footer comes before the detail panel, which is correct left to right. | Designer confirms. Also decide the row list: arrow keys or Tab per row. |
| 29 | Focus not obscured (2.4.11) | Rows and buttons | cannot verify | No sticky layers in the spec, but there is no focus design to test. | Check in the build. |

## 4. Labels, names and alt text

| # | Check | Element | Result | Why | Fix or question |
|---|---|---|---|---|---|
| 30 | Name and role | Evidence bar | cannot verify | The text "Evidence in #client-kestrel" gives a name. The role is open: "NOT IN DESIGN: is the bar clickable (open in Slack, or expand)?" | Decide button, link or static text. Add aria-expanded if it expands. |
| 31 | Alt text | Slack and Gmail logos in rows (6750:2289, 2371, 2313, 2332, 2352, 2395) | fail | "NOT IN DESIGN: 'Slack' (the source of the item)" | The source is meaning, not decoration. Confirm the names "Slack" and "Gmail". |
| 32 | Alt text | Footer Gmail and Slack icons, Slack logo in detail header | fail | Each is "NOT IN DESIGN" | Confirm the names. The times in the footer belong to a source, so the name matters. |
| 33 | Label | Search field | fail | "the placeholder alone is not a label" | Give a visible label or an accessible name, for example "Search". |
| 34 | Label | Sort arrow | fail | "NOT IN DESIGN: for example 'Sort by Response, descending'" | Confirm the name, and aria-sort on the header. |
| 35 | Alt text | QTalo logo | fail | "NOT IN DESIGN: 'QTalo' or a link to home?" | Decide. |
| 36 | Name | Selected row | fail | "NOT IN DESIGN: selection must also be in code" | Define aria-current or aria-selected. |
| 37 | Label | Buttons "Response sent", "No response needed" | pass | The accessible names are given, and the check icon is marked decorative. | None. |
| 38 | Decorative marks | Search, reply, timer, check icons, avatars, dividers, Brand Icon in the evidence bar | pass | Marked "Yes" decorative with a reason (text next to them). The Brand Icon note asks to confirm "Slack" is said elsewhere. | Resolve with rows 31 and 32. |
| 39 | Hidden content | Opacity-0 Delivery cells and the hidden Response clock in row 3 | cannot verify | "Screen readers would still read opacity-0 text." Open question about rendering. | If the cells stay in the DOM, use hidden or aria-hidden, or do not render them. |
| 40 | Structure | Headings, landmarks, list roles for the queue and thread | cannot verify | The spec gives none. | Specify them. |
| 41 | Status message (4.1.3) | Result of the two buttons, row leaving the queue, "Last checked" update | cannot verify | "NOT IN DESIGN: what happens after a click" | Define a polite live region message. |

## 5. Color alone

| # | Check | Element | Result | Why | Fix or question |
|---|---|---|---|---|---|
| 42 | Color alone | Selected row | fail | The only sign is a 5 px #FF4800 left bar. The title weight is not tied to selection. | Add a second sign (background tint, or aria-selected plus a visible mark). |
| 43 | Color alone | "overdue" vs "until target" (same orange) | pass | The text says the state: "47m overdue", "17m until target". | None. |
| 44 | Color alone | Response vs Delivery | pass | Each has an icon, a column header and different text, not only color (orange vs gold). | None. |
| 45 | Color alone | Latest message "Response" tag | pass | Reply icon plus the word "Response" | None. |
| 46 | Color alone | Semi Bold vs Regular titles | cannot verify | "NOT IN DESIGN: does the weight mean a state" | If it means unread, weight alone is a weak sign. Add text or a dot with a name. |

## 6. Other WCAG 2.2 AA items

| # | Check | Element | Result | Why | Fix or question |
|---|---|---|---|---|---|
| 47 | Reflow and resize (1.4.10, 1.4.4, 1.4.12) | Whole screen | cannot verify | Only 1920 x 1080. Fixed widths 926 and 921, and "NOT IN DESIGN: behavior below 1920 px". | Define behavior at 320 px wide and at 200% zoom. Fixed heights must not clip text with larger spacing. |

Notes for the designer:
- Main cause of fails: light grays (#999999, #BFBFBF, #848484, #808080, #8B8B8B, #898989), orange and gold text (#FF4800, #B27E08), and the 60% opacity on older messages. Fix the tokens once and most rows pass. The frame has no variables, so this is the moment to create them.
- Dimmed older messages are the largest group of fails (rows 8 to 9). Dimming by opacity cannot pass for text.
- Every control has no focus design. Design one focus ring and apply it to all.
- Selection needs a second sign, not only the orange bar.
- Decide about the opacity-0 cells (Delivery in "Only Response", and the hidden Response clock in row 3) before development. Hidden text must not be read by screen readers.
- Counts: 23 fail, 13 pass, 11 cannot verify (47 grouped checks; corrected from 12 by the main session). Fail rows are 1 to 13, 25 to 27, 31 to 36, 42. Underlying counts: 25 text and 4 icon contrast rows fail in the spec.
- This automated review supports a manual check; it does not replace it. A person with a screen reader and keyboard must test the built screen. The spec is the only source here, plus one static image.
- I could not check hover, loading, empty and error states, because the spec has them all as NOT IN DESIGN. That also blocks accessible error messages (3.3.1).
