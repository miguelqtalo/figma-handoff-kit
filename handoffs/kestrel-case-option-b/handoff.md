# Handoff: Kestrel Case (Response+Delivery) - Option B

## 1. Source

- Figma link: https://www.figma.com/design/KXDasTBnxU4SVR68K44kiV/MVP-3.0-Wireframes?node-id=6750-1196
- Frame name and node id: "Kestrel Case (Response+Delivery) - Option B", 6750:1196 (file MVP-3.0-Wireframes)
- Frame size: 1920 x 1606 px (inner frame 6750:1197 is 1917 x 1606)
- Date: 2026-10-22
- Components in use: one component instance only, "Brand Icon" (6750:1487 and 6750:1643, Slack logo, 24 px box, 16 px "Logo" inside, 13.4 px "Icon svg"). All other icons are plain frames named after Material Symbols: `search`, `reply`, `timer`, `arrow_downward_alt`, `check` (hidden), `keyboard_arrow_down`. Source logos (Slack, Gmail) are frames named "Icon svg" (Slack 16 x 16, Gmail 16.7 x 12.5). App logo: "QTalo-logo" (6750:1200, 32 px).
- Known constraints: the frame has no Figma variables (`get_variable_defs` returned `{}`), so every color, size and font below is a raw value and "needs a token". Only one frame size (1920 wide) exists. Only the Default state is drawn, plus one Selected queue row (row 1). Values come from `get_design_context` on 5 sections (6750:1198, 6750:1225, 6750:1409, 6750:1426, 6750:1586) and on 4 lines (6750:1224, 6750:1407, 6750:1424, 6750:1585). Line and dot colors come from the SVG assets that `get_design_context` returned. The top frame fill (6750:1196 / 6750:1197) was not read, so the page background is not confirmed (see Open questions). Reference image: `figma-reference.png` in this folder.

Layout (from `get_metadata`):

| Area | Node | Size | Notes |
|---|---|---|---|
| Left rail | 6750:1198 | 70 x 1606 | Fill #FBFBFC. Logo block 70 x 72. A "Filters" group (Slack, Gmail) exists but is hidden (6750:1202). |
| Rail divider | 6750:1224 | 1 x 1080 | Stroke #D8D8DD. The line is 1080 high, not 1606, so it stops above the frame bottom. |
| Queue panel | 6750:1225 | 926 x 1606 | Search bar 72 high, column header 48 high, 6 rows in 2 groups (6750:1254 rows 1 to 3, 6750:1317 rows 4 to 6), footer 72 high at the bottom (6750:1382). |
| Panel divider | 6750:1407 | 1 x 1606 | Stroke #B8B8B8. Between queue and detail. |
| Detail panel | 6750:1408 | 921 x 1606 | Header 72 high (6750:1409), line under it (6750:1424, #D8D8DD), then two columns of 460.5 each: Response (6750:1426) and Delivery (6750:1586), split by line 6750:1585 (#D8D8DD). |
| Response column | 6750:1426 | 460.5 x 1534 | Summary block 588 high (6750:1427), divider #B8B8B8, "Evidence in" bar 48 high (6750:1484), thread 898 high (6750:1495), bottom-aligned, `overflow-y: auto`. |
| Delivery column | 6750:1586 | 460.5 x 1534 | Summary block 589 high (6750:1587), divider #B8B8B8, "Evidence in" bar 48 high (6750:1640), thread 897 high (6750:1651), bottom-aligned, `overflow-y: auto`. |

Queue rows (from `get_design_context` 6750:1225). "Hidden" means the text layer is in the file with opacity 0, so it is not visible in the render:

| Row | Node | Source icon | Subject weight | Response cell | Delivery cell |
|---|---|---|---|---|---|
| 1 (selected) | 6750:1255 | Slack | Semi Bold | "47m overdue" / "Dylan Moore" | "Delivery promise missed" / "Mara Ellis" |
| 2 | 6750:1279 | Gmail | Semi Bold | "1h 5m overdue" / "Camille Ross" | hidden: "Delivery promise missed" (6750:1296) |
| 3 | 6750:1298 | Gmail | Semi Bold | hidden: "1h 5m overdue / 3h" (6750:1312) | "Client asked again" / "Camille Ross" |
| 4 | 6750:1318 | Gmail | Regular | "17m until target" / "Julian Reyes" | hidden: "Delivery promise missed" (6750:1335) |
| 5 | 6750:1337 | Slack | Regular | "32m until  target" / "Ava Chen" | hidden group: "Delivery promise missed" / "Mara Ellis" (6750:1357) |
| 6 | 6750:1361 | Gmail | Regular | "Client dissatisfaction" / "Teresa Lang" | hidden group: "Client asked again" / "Camille Ross" (6750:1378) |

## 2. States

| Element | Default | Hover | Focus | Disabled | Loading | Empty | Error |
|---|---|---|---|---|---|---|---|
| Search field (6750:1226) | 24 px `search` icon (#BFBFBF) + placeholder "Search", Inter Regular 16 #BFBFBF, padding 24, gap 8, 72 high | NOT IN DESIGN: what changes on hover? | NOT IN DESIGN: focus ring and typed-text color? | NOT IN DESIGN: can search be disabled? | NOT IN DESIGN: is there a loading indicator while results update? | NOT IN DESIGN: what shows when search finds no items? | NOT IN DESIGN: what shows if search fails? |
| Column header "Subject" (6750:1237) | Inter Regular 14 #222222 on header fill #FDFDFD, padding 24 / 12 | NOT IN DESIGN: is it sortable? hover style? | NOT IN DESIGN: focus style? | NOT IN DESIGN: question, n/a? | NOT IN DESIGN: question, n/a? | NOT IN DESIGN: question, n/a? | NOT IN DESIGN: question, n/a? |
| Column header "Response" with sort arrow (6750:1239) | `reply` icon 24 (#FF4800) + "Response" Inter Medium 14 #222222, gap 8, + `arrow_downward_alt` 24 (#A3A3A3), gap 6 | NOT IN DESIGN: is the header clickable to sort? hover style? | NOT IN DESIGN: focus style? | NOT IN DESIGN: is sort ever disabled? | NOT IN DESIGN: loading while re-sorting? | NOT IN DESIGN: question, n/a? | NOT IN DESIGN: question, n/a? |
| Column header "Delivery" (6750:1248) | `timer` icon 24 (#B27E08) + "Delivery" Inter Medium 14 #222222, gap 8, no sort arrow | NOT IN DESIGN: is this header sortable too? | NOT IN DESIGN: focus style? | NOT IN DESIGN: disabled state? | NOT IN DESIGN: loading? | NOT IN DESIGN: question, n/a? | NOT IN DESIGN: question, n/a? |
| Queue row (6750:1279 and siblings) | Unselected: no fill, padding 24, 97 high (121 when the subject wraps, row 6). Bottom line 1 px #D8D8DD. Selected (row 1, 6750:1255): fill #FFFFFF, left border 5 px #FF4800, padding 19 / 24 so content does not move. Row 5 (6750:1337) has the same structure with a white 5 px border and white fill | NOT IN DESIGN: hover fill? | NOT IN DESIGN: keyboard focus style for a row? | NOT IN DESIGN: can a row be disabled? | NOT IN DESIGN: skeleton rows while the queue loads? | NOT IN DESIGN: what does the queue show with 0 items? Also: what does an empty Response or Delivery cell show (rows 2 to 6 have an invisible text layer there)? | NOT IN DESIGN: what shows if the queue cannot load? |
| Button "Response sent" (6750:1472) | Border 1 px #000000, radius 4, padding 6, label Inter Semi Bold 12 #222222, 100 x 29. Its `check` icon 16 is hidden (6750:1473) | NOT IN DESIGN: hover style? | NOT IN DESIGN: focus style? | NOT IN DESIGN: when is it disabled, and how does it look? | NOT IN DESIGN: loading after click? | NOT IN DESIGN: does the hidden check icon mean a "chosen" state? | NOT IN DESIGN: what if saving fails? |
| Button "No response needed" (6750:1477) | Same style, 134 x 29. Its `check` icon is hidden (6750:1478) | NOT IN DESIGN: hover style? | NOT IN DESIGN: focus style? | NOT IN DESIGN: disabled look? | NOT IN DESIGN: loading after click? | NOT IN DESIGN: does the hidden check icon mean a "chosen" state? | NOT IN DESIGN: what if saving fails? |
| Button "Mark completed" (6750:1628) | Same style, 109 x 29. Its `check` icon is hidden (6750:1629) | NOT IN DESIGN: hover style? | NOT IN DESIGN: focus style? | NOT IN DESIGN: disabled look? | NOT IN DESIGN: loading after click? | NOT IN DESIGN: does the hidden check icon mean a "chosen" state? | NOT IN DESIGN: what if saving fails? |
| Dropdown button "Correct" (6750:1633) | Border 1 px #000000, radius 4, padding 6, gap 4, label Inter Semi Bold 12 #222222 + `keyboard_arrow_down` 16 (#222222), 79 x 30 | NOT IN DESIGN: hover style? | NOT IN DESIGN: focus style? | NOT IN DESIGN: disabled look? | NOT IN DESIGN: loading? | NOT IN DESIGN: what options are in the menu? The menu is not drawn. | NOT IN DESIGN: what if saving fails? |
| "Evidence in #client-kestrel" bar (6750:1485, 6750:1641) | 48 high, padding 24 / 12, Brand Icon 24 + "Evidence in" Inter Semi Bold 14 #999999 + "#client-kestrel" Inter Semi Bold 16 #222222, gap 8, `keyboard_arrow_down` 24 (#222222) on the right. Line under it #E8E8EC. Thread is shown open below it | NOT IN DESIGN: is it a toggle? hover style? | NOT IN DESIGN: focus style? | NOT IN DESIGN: disabled look? | NOT IN DESIGN: loading while the thread loads? | NOT IN DESIGN: what shows when there is no evidence thread? | NOT IN DESIGN: what if the source (Slack) cannot load? |
| Thread message (for example 6750:1502) | Avatar 32, radius 6, fill #A8A8A8, padding 10, initial Inter Semi Bold 16 #FFFFFF; name Inter Bold 16 #222222; time Inter Medium 14 #898989; tag Inter Semi Bold 14 #C1C1C1; body Inter Regular 16 #8B8B8B; gap 12 avatar to text, gap 8 inside, padding 16 top and bottom. Older messages: group opacity 60% (6750:1501, 6750:1535, 6750:1559, 6750:1657). Latest message per column (6750:1570, 6750:1668): full opacity, with a colored tag ("Response" #FF4800 + `reply` 16, or "Promise made" #B27E08 + `timer` 16) | NOT IN DESIGN: is a message interactive (hover, link to source)? | NOT IN DESIGN: focus style if it is interactive? | NOT IN DESIGN: question, n/a? | NOT IN DESIGN: loading? | NOT IN DESIGN: question, n/a? | NOT IN DESIGN: question, n/a? |
| Date pill "Monday" / "Tuesday" / "Today" (6750:1498 and siblings) | Border 1 px #DDDDDD, radius 38, padding 12 / 6, Inter Semi Bold 12 #222222, lines #DDDDDD on both sides, row padding 6 (Response) or 24 / 8 (Delivery) | NOT IN DESIGN: question, n/a? | NOT IN DESIGN: question, n/a? | NOT IN DESIGN: question, n/a? | NOT IN DESIGN: question, n/a? | NOT IN DESIGN: question, n/a? | NOT IN DESIGN: question, n/a? |

## 3. Tokens

The frame has no Figma variables. Every value below is a raw value from `get_design_context` (or from its SVG assets for lines, dots and icons), so each one needs a token.

### Color

| Use | Token | Value |
|---|---|---|
| Primary text (titles, names, values, button labels, date pills) | needs a token | #222222 |
| Response: timers, "Response" label, "Needs response", selected row border, `reply` icon, latest-message tag | needs a token | #FF4800 |
| Delivery: reason text, "Delivery" label, "Promise made", `timer` icon | needs a token | #B27E08 |
| Queue client name | needs a token | #666666 |
| Queue person name (under the timer or reason) | needs a token | #7B7B7B |
| Section labels ("What QTalo found", "Who's waiting", "Owed by", "How it got here", "Next decision", "Evidence in") | needs a token | #999999 |
| Detail header client name | needs a token | #808080 |
| Timeline meta ("Mon 9:12 AM • Dylan Moore") | needs a token | #6D6D6D |
| Thread time | needs a token | #898989 |
| Thread body | needs a token | #8B8B8B |
| Thread message tags ("• Original ask", "• Team acknowledge") | needs a token | #C1C1C1 |
| Hidden "/ 3h" in row 3 (opacity 0 layer) | needs a token | #A1A1A1 |
| Avatar fill | needs a token | #A8A8A8 |
| Avatar initial, selected row fill, row 5 fill and border | needs a token | #FFFFFF |
| Search placeholder and `search` icon | needs a token | #BFBFBF |
| Sort arrow icon `arrow_downward_alt` | needs a token | #A3A3A3 |
| Footer "6 items" | needs a token | #686868 |
| Footer "Last checked" and times | needs a token | #848484 |
| Left rail fill | needs a token | #FBFBFC |
| Queue column header fill | needs a token | #FDFDFD |
| Button border | needs a token | #000000 |
| Queue lines, rail divider, detail header line, column divider | needs a token | #D8D8DD |
| Queue / detail panel divider, line above "Evidence in" | needs a token | #B8B8B8 |
| Summary dividers, line under "Evidence in" | needs a token | #E8E8EC |
| Date pill border and side lines | needs a token | #DDDDDD |
| Timeline connector line | needs a token | #C5C5C5 |
| Timeline dot, open (stroke 1.5, white fill) | needs a token | #0B0909 |
| Timeline dot, filled ("Team acknowledge") | needs a token | #222222 |
| Timeline dot, Response ("Needs response") | needs a token | #FF4800 |
| Timeline dot, Delivery ("Promise made") | needs a token | #B27E08 |
| Page / panel background | needs a token | NOT IN DESIGN: fill of 6750:1196 not read; the render looks white. Confirm #FFFFFF. |

### Spacing and size

| Use | Token | Value |
|---|---|---|
| Left rail width | needs a token | 70 |
| Top bars height (logo block, search bar, detail header, footer) | needs a token | 72 |
| Queue panel width | needs a token | 926 |
| Detail panel width / each column | needs a token | 921 / 460.5 |
| Main side padding (search, header, rows, columns, footer) | needs a token | 24 |
| Selected row: left border / side padding | needs a token | 5 / 19 |
| Column header padding | needs a token | 24 / 12, height 48 |
| Queue row padding / height | needs a token | 24, 97 high (121 with a 2-line subject) |
| Row icon box / gap icon to text | needs a token | 24 (pt 2) / 12 |
| Gap title to client, timer to person | needs a token | 4 |
| Gap between the two status cells | needs a token | 8 |
| Search icon to text gap | needs a token | 8 |
| Column summary header padding | needs a token | top 16, bottom 12, sides 24 |
| "What QTalo found" block padding / gap | needs a token | top 8, bottom 20, sides 24 / 16 |
| Summary section padding / gap ("Who's waiting", "How it got here", "Next decision") | needs a token | 24 / 20, gap 16 |
| Label column width ("Who's waiting", "Owed by") | needs a token | 110 |
| Timeline item gap / dot size / dot-to-text gap | needs a token | 12 / 12 / 8 |
| Next decision text to buttons | needs a token | 16 |
| Button padding / radius / gap between buttons | needs a token | 6 / 4 / 8 |
| Summary block bottom padding | needs a token | 16 |
| "Evidence in" bar | needs a token | 48 high, padding 24 / 12, gap 8 |
| Thread message padding / avatar gap / inner gap | needs a token | 16 top and bottom / 12 / 8 |
| Avatar size / radius / padding | needs a token | 32 / 6 / 10 |
| Date pill padding / radius | needs a token | 12 / 6, radius 38 |
| Footer right group gap / icon to time gap | needs a token | 16 / 4 |
| Icon sizes | needs a token | 24 (headers, rows), 16 (buttons, message tags), 26 (detail header logo in 48 box), 32 (app logo) |
| Line width | needs a token | 1 |

### Type

All text uses line height "normal" (`leading-[normal]`). No line height value is set in Figma.

| Use | Token | Family, size, weight, line height |
|---|---|---|
| Queue row subject, rows 1 to 3 | needs a token | Inter, 20, Semi Bold, normal |
| Queue row subject, rows 4 to 6 | needs a token | Inter, 20, Regular, normal |
| Detail header title | needs a token | Inter, 20, Bold, normal |
| "What QTalo found" finding | needs a token | Inter, 20, Bold, normal |
| Queue client, row timers and reasons, person names | needs a token | Inter, 16, Regular (client) / Medium (status cells), normal |
| Column label "Response" | needs a token | Inter, 16, Semi Bold, normal |
| Column label "Delivery" | needs a token | Inter, 16, Bold, normal |
| Column status ("47m overdue", "Delivery promise missed") | needs a token | Inter, 16, Medium, normal |
| "Who's waiting" / "Owed by" value | needs a token | Inter, 16, Medium, normal |
| Next decision text, "#client-kestrel" | needs a token | Inter, 16, Semi Bold, normal |
| Thread name | needs a token | Inter, 16, Bold, normal |
| Thread body | needs a token | Inter, 16, Regular, normal |
| Search placeholder | needs a token | Inter, 16, Regular, normal |
| Section labels | needs a token | Inter, 14, Semi Bold, normal ("Owed by" is Regular) |
| Column headers "Response", "Delivery" | needs a token | Inter, 14, Medium, normal |
| Column header "Subject", footer text | needs a token | Inter, 14, Regular, normal |
| Detail header client | needs a token | Inter, 14, Semi Bold, normal |
| Timeline label | needs a token | Inter, 14, Semi Bold, normal |
| Thread time | needs a token | Inter, 14, Medium, normal |
| Thread tag | needs a token | Inter, 14, Semi Bold, normal |
| Timeline meta | needs a token | Inter, 12, Regular, normal |
| Button label, date pill | needs a token | Inter, 12, Semi Bold, normal |
| Avatar initial | needs a token | Inter, 16, Semi Bold, normal |

### Contrast (from scripts/contrast.py)

One row per text use. Background is #FFFFFF where Figma sets no fill (not confirmed, see Open questions). Large text = 24 px, or 18.66 px bold.

| Text | Background | Ratio | AA normal | AA large |
|---|---|---|---|---|
| Search placeholder #BFBFBF (16) | FFFFFF | 1.84:1 | FAIL | FAIL |
| "Subject" header #222222 (14) | FDFDFD | 15.64:1 | pass | pass |
| "Response" / "Delivery" column headers #222222 (14) | FDFDFD | 15.64:1 | pass | pass |
| Sort arrow icon #A3A3A3 (non-text, needs 3:1) | FDFDFD | 2.48:1 | FAIL | FAIL |
| Queue row subject #222222 (20) | FFFFFF | 15.91:1 | pass | pass |
| Queue client name #666666 (16) | FFFFFF | 5.74:1 | pass | pass |
| Queue Response timer / "Client dissatisfaction" #FF4800 (16 Medium) | FFFFFF | 3.40:1 | FAIL | pass |
| Queue Delivery reason #B27E08 (16 Medium) | FFFFFF | 3.57:1 | FAIL | pass |
| Queue person name #7B7B7B (16) | FFFFFF | 4.23:1 | FAIL | pass |
| Footer "6 items" #686868 (14) | FFFFFF | 5.57:1 | pass | pass |
| Footer "Last checked" and times #848484 (14) | FFFFFF | 3.74:1 | FAIL | pass |
| Detail header title #222222 (20 Bold) | FFFFFF | 15.91:1 | pass | pass |
| Detail header client #808080 (14) | FFFFFF | 3.95:1 | FAIL | pass |
| Column label "Response" + "47m overdue" #FF4800 (16) | FFFFFF | 3.40:1 | FAIL | pass |
| Column label "Delivery" + "Delivery promise missed" #B27E08 (16) | FFFFFF | 3.57:1 | FAIL | pass |
| Section labels #999999 (14) | FFFFFF | 2.85:1 | FAIL | FAIL |
| "Evidence in" #999999 (14) | FFFFFF | 2.85:1 | FAIL | FAIL |
| Finding text #222222 (20 Bold) | FFFFFF | 15.91:1 | pass | pass |
| "Who's waiting" / "Owed by" value #222222 (16) | FFFFFF | 15.91:1 | pass | pass |
| Timeline label "Original ask" / "Team acknowledge" / "Client request" #222222 (14) | FFFFFF | 15.91:1 | pass | pass |
| Timeline label "Needs response" #FF4800 (14) | FFFFFF | 3.40:1 | FAIL | pass |
| Timeline label "Promise made" #B27E08 (14) | FFFFFF | 3.57:1 | FAIL | pass |
| Timeline meta #6D6D6D (12) | FFFFFF | 5.17:1 | pass | pass |
| Next decision text #222222 (16) | FFFFFF | 15.91:1 | pass | pass |
| Button labels #222222 (12) | FFFFFF | 15.91:1 | pass | pass |
| Button border #000000 (non-text, needs 3:1) | FFFFFF | 21.00:1 | pass | pass |
| "#client-kestrel" #222222 (16) | FFFFFF | 15.91:1 | pass | pass |
| Date pill text #222222 (12) | FFFFFF | 15.91:1 | pass | pass |
| Older message name #222222 at 60% = #7A7A7A (16 Bold) | FFFFFF | 4.29:1 | FAIL | pass |
| Older message time #898989 at 60% = #B8B8B8 (14) | FFFFFF | 1.98:1 | FAIL | FAIL |
| Older message tag #C1C1C1 at 60% = #DADADA (14) | FFFFFF | 1.40:1 | FAIL | FAIL |
| Older message body #8B8B8B at 60% = #B9B9B9 (16) | FFFFFF | 1.96:1 | FAIL | FAIL |
| Older message avatar initial #FFFFFF on #A8A8A8 at 60% = #CBCBCB (16) | CBCBCB | 1.62:1 | FAIL | FAIL |
| Latest message name #222222 (16 Bold) | FFFFFF | 15.91:1 | pass | pass |
| Latest message time #898989 (14) | FFFFFF | 3.50:1 | FAIL | pass |
| Latest message body #8B8B8B (16) | FFFFFF | 3.41:1 | FAIL | pass |
| Latest message tag "Response" #FF4800 (14) | FFFFFF | 3.40:1 | FAIL | pass |
| Latest message tag "Promise made" #B27E08 (14) | FFFFFF | 3.57:1 | FAIL | pass |
| Latest message avatar initial #FFFFFF on #A8A8A8 (16) | A8A8A8 | 2.38:1 | FAIL | FAIL |
| Hidden "/ 3h" #A1A1A1 (16, opacity 0 now) | FFFFFF | 2.58:1 | FAIL | FAIL |
| Rail logo block (no text) | FBFBFC | n/a | n/a | n/a |

Lines #D8D8DD (1.42:1), #DDDDDD (1.36:1) are dividers, not controls, so 3:1 may not apply. Timeline open dot #0B0909: 19.86:1.

## 4. Copy

Strings are exact from Figma, including the double space in "32m until  target" and the em dashes in thread messages. "Max length" is based on the box width in Figma; the character count is the longest string seen in that slot.

| Location | String (exact) | Max length |
|---|---|---|
| Search placeholder (6750:1230) | Search | 1 line, about 850 px free. NOT IN DESIGN: max query length? |
| Queue header (6750:1237) | Subject | 1 line, fixed label |
| Queue header (6750:1244) | Response | 1 line, fixed label |
| Queue header (6750:1252) | Delivery | 1 line, fixed label |
| Row subject (6750:1269, 6750:1351) | Contractor agreement review | Box 405 px. Longest seen: 46 chars on 2 lines (row 6). NOT IN DESIGN: max lines, and truncate or wrap after that? |
| Row subject (6750:1290) | Intake packet readiness | Same as above |
| Row subject (6750:1309) | Data-processing addendum | Same as above |
| Row subject (6750:1329) | Invoice account number | Same as above |
| Row subject (6750:1372) | ADP access issue payroll lead still locked out | Same as above (wraps to 2 lines, box 379 px with 24 px right padding) |
| Row client (6750:1270, 6750:1352) | Kestrel Apparel Co. | Box 405 px, 1 line (nowrap). Longest seen: 25 chars. NOT IN DESIGN: truncation? |
| Row client (6750:1291, 6750:1310) | Northstar Health Partners | Same as above |
| Row client (6750:1330) | Ridgeway Foods | Same as above |
| Row client (6750:1373) | Ironwood Logistics | Same as above |
| Row Response cell (6750:1273) | 47m overdue | Cell 216 px, 1 line. Longest seen: 22 chars ("Client dissatisfaction"). NOT IN DESIGN: wrap or truncate? |
| Row Response cell (6750:1294) | 1h 5m overdue | Same as above |
| Row Response cell (6750:1333) | 17m until target | Same as above |
| Row Response cell (6750:1355) | 32m until  target | Same as above. NOT IN DESIGN: is the double space on purpose? |
| Row Response cell (6750:1376) | Client dissatisfaction | Same as above |
| Row Response cell, hidden (6750:1312) | 1h 5m overdue / 3h | Opacity 0. NOT IN DESIGN: should this show? |
| Row Delivery cell (6750:1276) | Delivery promise missed | Cell 216 px, 1 line. Longest seen: 23 chars |
| Row Delivery cell (6750:1314) | Client asked again | Same as above |
| Row Delivery cell, hidden (6750:1296, 6750:1335, 6750:1358) | Delivery promise missed | Opacity 0. NOT IN DESIGN: should this show? |
| Row Delivery cell, hidden (6750:1379) | Client asked again | Opacity 0. NOT IN DESIGN: should this show? |
| Row person (6750:1274) | Dylan Moore | 1 line nowrap, cell 216 px. Longest seen: 12 chars |
| Row person (6750:1277, 6750:1359) | Mara Ellis | Same as above. Note: Figma has a trailing space "Mara Ellis " |
| Row person (6750:1295, 6750:1315, 6750:1380) | Camille Ross | Same as above |
| Row person (6750:1334) | Julian Reyes | Same as above |
| Row person (6750:1356) | Ava Chen | Same as above |
| Row person (6750:1377) | Teresa Lang | Same as above |
| Footer count (6750:1383) | 6 items | 1 line. NOT IN DESIGN: singular "1 item"? |
| Footer label (6750:1385) | Last checked | 1 line, fixed label |
| Footer Gmail time (6750:1394) | Friday 12:00 PM | 1 line nowrap, 15 chars. NOT IN DESIGN: date format for older checks? |
| Footer Slack time (6750:1406) | Friday 11:58 AM | Same as above |
| Detail header title (6750:1422) | Contractor agreement review | 1 line nowrap, about 571 px free next to the client. NOT IN DESIGN: truncation for long subjects? |
| Detail header client (6750:1423) | Kestrel Apparel Co. | 1 line nowrap. NOT IN DESIGN: truncation? |
| Response label (6750:1434) | Response | Fixed label |
| Response status (6750:1435) | 47m overdue | 1 line nowrap, right-aligned |
| Delivery label (6750:1594) | Delivery | Fixed label |
| Delivery status (6750:1595) | Delivery promise missed | 1 line nowrap, right-aligned |
| Section label (6750:1440, 6750:1600) | What QTalo found | Fixed label |
| Response finding (6750:1441) | Client request has no visible acknowledgement in this Slack thread before the 3-hour response window expired. | Box 412 px, 109 chars on 4 lines; block is 157 high. NOT IN DESIGN: max lines? |
| Delivery finding (6750:1601) | Due Wednesday · no delivery or updated ETA found | Box 412 px, 48 chars on 2 lines; block is fixed 157 high so both columns line up. NOT IN DESIGN: what if the text needs more than 4 lines? |
| Section label (6750:1445) | Who's waiting | Fixed label, 110 px |
| Who's waiting value (6750:1446) | Dylan Moore at Kestrel Apparel Co. | 1 line nowrap, about 270 px free, 34 chars. NOT IN DESIGN: wrap or truncate? |
| Section label (6750:1605) | Owed by | Fixed label, 110 px |
| Owed by value (6750:1606) | Mara Ellis | 1 line nowrap, about 270 px free |
| Section label (6750:1450, 6750:1610) | How it got here | Fixed label, 110 px |
| Timeline label (6750:1455) | Original ask | 1 line nowrap |
| Timeline meta (6750:1456) | Mon 9:12 AM • Dylan Moore | 1 line nowrap |
| Timeline label (6750:1459) | Team acknowledge | 1 line nowrap |
| Timeline meta (6750:1460) | Mon 9:40 AM, Tue 10:05 AM • Mara Ellis | 1 line nowrap, 38 chars. NOT IN DESIGN: what with 3 or more acknowledgements? |
| Timeline label (6750:1463) | Needs response | 1 line nowrap |
| Timeline meta (6750:1464) | Today 10:56 and 11:36 AM | 1 line nowrap |
| Timeline label (6750:1615) | Client request | 1 line nowrap |
| Timeline meta (6750:1616) | Mon 9:04 AM • Dylan Moore | 1 line nowrap |
| Timeline label (6750:1619) | Promise made | 1 line nowrap |
| Timeline meta (6750:1620) | Mon 9:18 AM • Mara Ellis • Due Wed 5:00 PM | 1 line nowrap, 42 chars, about 287 px free. Note: trailing space in Figma |
| Section label (6750:1468, 6750:1624) | Next decision | Fixed label, 110 px |
| Response next decision (6750:1470) | Confirm who should acknowledge the contractor agreement request. | Box 412 px, 64 chars on 2 lines. NOT IN DESIGN: max lines? |
| Delivery next decision (6750:1626) | Check status and update the client if delivery is not imminent. | Box 412 px, 63 chars on 2 lines. NOT IN DESIGN: max lines? |
| Button (6750:1476) | Response sent | 1 line, fixed label |
| Button (6750:1481) | No response needed | 1 line, fixed label |
| Button (6750:1632) | Mark completed | 1 line, fixed label |
| Dropdown (6750:1634) | Correct | 1 line, fixed label |
| Evidence label (6750:1488, 6750:1644) | Evidence in | Fixed label |
| Evidence channel (6750:1489, 6750:1645) | #client-kestrel | 1 line nowrap, 15 chars, about 270 px free. NOT IN DESIGN: long channel names, and Gmail sources (subject line?) |
| Date pill (6750:1499, 6750:1655) | Monday | 1 line |
| Date pill (6750:1533) | Tuesday | 1 line |
| Date pill (6750:1557) | Today | 1 line |
| Avatar initial (6750:1504 and others) | D | 1 character |
| Avatar initial (6750:1514 and others) | M | 1 character |
| Thread name (6750:1507 and others) | Dylan Moore | 1 line nowrap |
| Thread name (6750:1517 and others) | Mara Ellis | 1 line nowrap |
| Thread time (6750:1508) | 9:12 AM | 1 line nowrap |
| Thread time (6750:1518) | 9:40 AM | 1 line nowrap |
| Thread time (6750:1528) | 2:15 PM | 1 line nowrap |
| Thread time (6750:1542) | 10:05 AM | 1 line nowrap |
| Thread time (6750:1552) | 4:30 PM | 1 line nowrap |
| Thread time (6750:1566) | 10:58 AM | 1 line nowrap |
| Thread time (6750:1578) | 11:36 AM | 1 line nowrap |
| Thread time (6750:1664) | Mon 9:04 AM | 1 line nowrap. NOT IN DESIGN: why does the Delivery thread show the day and the Response thread not? |
| Thread time (6750:1676) | Mon, 9:18 AM | 1 line nowrap. NOT IN DESIGN: comma differs from "Mon 9:04 AM"; which format is right? |
| Thread tag (6750:1510) | • Original ask | 1 line nowrap |
| Thread tag (6750:1520, 6750:1544) | • Team acknowledge | 1 line nowrap |
| Thread tag, latest (6750:1583) | Response | 1 line nowrap |
| Thread tag, latest (6750:1681) | Promise made | 1 line nowrap |
| Thread body (6750:1511) | Heads up team, we've got a new contractor starting next week and will need the standard agreement reviewed before then. | Box 368 px, wraps, 119 chars on 3 lines. NOT IN DESIGN: max length or "show more"? |
| Thread body (6750:1521) | Thanks for the heads up, Dylan — send over the contractor specifics whenever you have them and we'll get the template pulled together. | Same, 134 chars on 3 lines |
| Thread body (6750:1529) | Sending the contractor details over now — let me know if anything else is needed on our end. | Same, 92 chars on 2 lines |
| Thread body (6750:1545) | Got it, thanks. Reviewing the NDA language against our standard clauses today. | Same, 78 chars on 2 lines |
| Thread body (6750:1553) | Any update on this? We'd like to get it locked before the work trial starts. | Same, 76 chars on 2 lines |
| Thread body (6750:1567) | Can someone review the contractor agreement before noon? We have the work trial starting tomorrow and need the NDA language confirmed today. | Same, 140 chars on 4 lines |
| Thread body (6750:1584) | Just checking this landed. We are blocked on sending the invite until we hear back. | Same, 83 chars on 2 lines |
| Thread body (6750:1665) | Can you send final redlines this week? We need the agreement before the contractor starts. | Same, 90 chars on 2 lines |
| Thread body (6750:1682) | Received. We will send final redlines by Wednesday at 5:00 PM. | Same, 62 chars on 2 lines |

## 5. Behavior

### Interactions

- Queue row 1 is drawn as selected (left border #FF4800, white fill). The detail panel shows that item. NOT IN DESIGN: confirm that clicking a row selects it and fills the detail panel.
- The Response column header has a sort arrow (`arrow_downward_alt`), so the queue looks sorted by Response, descending. NOT IN DESIGN: sort rules, and can the user change the sort?
- The detail panel shows Response and Delivery side by side for one item. The Response column and the Delivery column each have their own summary, decision buttons and evidence thread.
- Buttons "Response sent", "No response needed", "Mark completed" each have a hidden `check` icon. NOT IN DESIGN: what happens after a click (check shows, item leaves the queue, undo)?
- "Correct" has a down arrow, so it opens a menu. NOT IN DESIGN: menu items.
- "Evidence in #client-kestrel" has a down arrow and the thread is open. NOT IN DESIGN: does it collapse the thread?
- Thread areas are bottom-aligned (`justify-content: end`) and scroll (`overflow-y: auto`, `overflow-x: clip`). Older messages are 60% opacity; the message that triggers the alert is full opacity with a colored tag.
- Hidden layers in Figma: left rail "Filters" (6750:1202), `keyboard_arrow_down` in both column headers (6750:1436, 6750:1596), "Aviso" lines (6750:1568, 6750:1666), "Rectangle 11" (6750:1683, 6750:1684). NOT IN DESIGN: are any of these planned states?

### Breakpoints

- NOT IN DESIGN: only one frame, 1920 wide. What happens below 1920 (for example 1440 or 1280)? Do the queue and the two detail columns shrink, stack or scroll?
- The frame is 1606 high. NOT IN DESIGN: does the whole page scroll, or only the queue list and the two threads?

### Edge cases

- Empty status cells: rows 2 to 6 have an invisible (opacity 0) text in one cell. NOT IN DESIGN: should the cell be empty, or show a dash or "None"?
- Same subject twice: rows 1 and 5 are both "Contractor agreement review" at Kestrel Apparel Co., with different people and timers. NOT IN DESIGN: are these 2 separate items, or the same item?
- Row 5 has the "selected" structure with a white border. NOT IN DESIGN: is this a second selected state, or a left-over?
- Subject weight: rows 1 to 3 Semi Bold, rows 4 to 6 Regular. The 2 groups (6750:1254, 6750:1317) have no header. NOT IN DESIGN: does weight mean unread / read, or overdue / not yet due? Is there a group label?
- "17m until target" and "32m until  target" use the same red (#FF4800) as overdue items. NOT IN DESIGN: should "not yet due" have its own color?
- The Delivery column has a short thread (2 messages); the rest of the column is empty space above it. NOT IN DESIGN: is that on purpose?
- Long text: see "Max length" in Copy. Most single-line texts are `nowrap` in Figma and have no truncation rule.

## 6. Accessibility

Summary from the `a11y-reviewer` subagent (full review in `a11y-review.md`): **FAIL**. 50 checks: 12 pass, 26 fail, 12 cannot verify.

- Contrast: 16 fails. Response orange #FF4800 (3.40:1) and Delivery gold #B27E08 (3.57:1) fail for all 14 to 16 px text. Section labels #999999 (2.85:1), search placeholder (1.84:1), person names #7B7B7B, footer times, detail header client, and all thread text fail. Older messages at 60% opacity drop to 1.40 to 4.29:1.
- Note: the "AA large" column only applies to text of 24 px, or 18.66 px bold. For 14 to 16 px text use the "AA normal" column.
- Focus: no focus style is drawn for any control (5 fails). Focus order is not given.
- Labels: search has no accessible name; logos and icons have no alt text or "decorative" mark; the sort arrow has no sort state.
- Color alone: the selected row is shown only by the orange left border.
- Target size: all known targets pass (rows 97 high, buttons 29 to 30 high).
- Cannot verify: page background, non-text contrast of icons and dots, "Correct" menu, expanded state of "Evidence in", row names, hidden opacity 0 layers, reflow below 1920.

## 7. Open questions

1. Page and panel background: the top frame fill was not read. Is it #FFFFFF? (Contrast rows assume #FFFFFF.)
2. No Figma variables: which project tokens should each raw value map to?
3. States: hover, focus, disabled, loading, empty and error are not drawn for any element (see States table).
4. Invisible (opacity 0) status texts in rows 2 to 6: should they show, or should the cell be empty?
5. Rows 1 and 5 have the same subject and client: one item or two?
6. Row 5 white left border: a state or a left-over?
7. Subject weight (Semi Bold vs Regular) and the 2 row groups: what do they mean?
8. "until target" items use overdue red: is that right?
9. "32m until  target" has a double space: typo?
10. Thread time formats differ: "Mon 9:04 AM", "Mon, 9:18 AM", "9:12 AM".
11. Trailing spaces in "Mara Ellis " and "Mon 9:18 AM • Mara Ellis • Due Wed 5:00 PM ": safe to trim?
12. "Correct" menu items are not drawn.
13. What happens after each decision button is clicked?
14. Breakpoints below 1920 wide, and which areas scroll.
15. Rail divider (6750:1224) is 1080 high, not full height: on purpose?
16. Is the "Evidence in" bar a toggle? What does it show for a Gmail source?
