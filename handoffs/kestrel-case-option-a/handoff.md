# Handoff: Kestrel Case (Response+Delivery) - Option A

## 1. Source

- Figma link: https://www.figma.com/design/KXDasTBnxU4SVR68K44kiV/MVP-3.0-Wireframes?node-id=6750-1705
- Frame name and node id: "Kestrel Case (Response+Delivery) - Option A", 6750:1705 (file MVP-3.0-Wireframes)
- Frame size: 1920 x 1511 px
- Date: 2026-10-22
- Components in use: one component instance only, "Brand Icon" (6750:1996 and 6750:2152, Slack logo, 24 px box, 16 px "Logo" inside). All other icons are plain frames named after Material Symbols: `search`, `reply`, `timer`, `arrow_downward_alt`, `check`, `keyboard_arrow_down`. Source logos (Slack, Gmail) are frames named "Icon svg". App logo: "QTalo-logo" (6750:1709, 32 px).
- Known constraints: the frame has no Figma variables (`get_variable_defs` returned `{}`), so every color, size and font below is a raw value and "needs a token". Only one frame size (1920 wide) exists. Only the Default state is drawn, plus one Selected queue row. Reference image: `figma-reference.png` in this folder.

Layout (from `get_metadata`):

| Area | Node | Size | Notes |
|---|---|---|---|
| Left rail | 6750:1707 | 70 x 1511 | Logo block 70 x 72. A "Filters" group (Slack, Gmail) exists but is hidden (6750:1711). |
| Rail divider | 6750:1733 | 1 x 1080 | Line stops at y 1080, not at the frame bottom (1511). |
| Queue panel | 6750:1734 | 926 x 1511 | Search bar 72 high, column header 48 high, 6 rows, footer 72 high at the bottom. |
| Panel divider | 6750:1916 | 1 x 1511 | Between queue and detail. |
| Detail panel | 6750:1917 | 921 x 1511 | Header 72 high, then two columns of 460.5 each: Response (6750:1935) and Delivery (6750:2095), split by line 6750:2094. |

## 2. States

| Element | Default | Hover | Focus | Disabled | Loading | Empty | Error |
|---|---|---|---|---|---|---|---|
| Search field (6750:1735) | 24 px search icon + placeholder "Search", Inter Regular 16, #BFBFBF, padding 24, gap 8 | NOT IN DESIGN: what changes on hover? | NOT IN DESIGN: focus ring and typed-text color? | NOT IN DESIGN: can search be disabled? | NOT IN DESIGN: is there a loading indicator while results update? | NOT IN DESIGN: what shows when search finds no items? | NOT IN DESIGN: what shows if search fails? |
| Column header "Response" with sort arrow (6750:1748) | `reply` icon 24 + "Response" Inter Medium 14 #222222 + `arrow_downward_alt` 24 | NOT IN DESIGN: is the header clickable to sort? hover style? | NOT IN DESIGN: focus style? | NOT IN DESIGN: question, is sort ever disabled? | NOT IN DESIGN: loading while re-sorting? | NOT IN DESIGN: n/a or needed? | NOT IN DESIGN: n/a or needed? |
| Column header "Delivery" (6750:1757) | `timer` icon 24 + "Delivery" Inter Medium 14 #222222, no sort arrow | NOT IN DESIGN: is this header sortable too? | NOT IN DESIGN: focus style? | NOT IN DESIGN: question, disabled state? | NOT IN DESIGN: loading? | NOT IN DESIGN: n/a or needed? | NOT IN DESIGN: n/a or needed? |
| Queue row (6750:1765 and siblings) | Unselected: no fill, padding 24, row 97 high (121 when the subject wraps). Selected (row 1, 6750:1764): fill #FFFFFF, left border 5 px #FF4800, padding 24 / 19 so content does not move | NOT IN DESIGN: hover fill? | NOT IN DESIGN: keyboard focus style for a row? | NOT IN DESIGN: question, can a row be disabled? | NOT IN DESIGN: skeleton rows while the queue loads? | NOT IN DESIGN: what does the queue show with 0 items? | NOT IN DESIGN: what shows if the queue cannot load? |
| Button "Response sent" (6750:1981) | Border 1 px #000000, radius 4, padding 6, gap 4, `check` icon 16 + label Inter Semi Bold 12 #222222, 120 x 30 | NOT IN DESIGN: hover style? | NOT IN DESIGN: focus style? | NOT IN DESIGN: when is it disabled, and how does it look? | NOT IN DESIGN: loading after click? | NOT IN DESIGN: n/a or needed? | NOT IN DESIGN: what if saving fails? |
| Button "No response needed" (6750:1986) | Border 1 px #000000, radius 4, padding 6, label Inter Semi Bold 12 #222222, 134 x 29. Its `check` icon is hidden (6750:1987) | NOT IN DESIGN: hover style? | NOT IN DESIGN: focus style? | NOT IN DESIGN: disabled look? | NOT IN DESIGN: loading after click? | NOT IN DESIGN: does the hidden check icon mean a "chosen" state? | NOT IN DESIGN: what if saving fails? |
| Button "Mark completed" (6750:2137) | Same style as "Response sent", 129 x 30, `check` icon 16 | NOT IN DESIGN: hover style? | NOT IN DESIGN: focus style? | NOT IN DESIGN: disabled look? | NOT IN DESIGN: loading after click? | NOT IN DESIGN: n/a or needed? | NOT IN DESIGN: what if saving fails? |
| Dropdown button "Correct" (6750:2142) | Border 1 px #000000, radius 4, padding 6, gap 4, label Inter Semi Bold 12 #222222 + `keyboard_arrow_down` 16, 79 x 30 | NOT IN DESIGN: hover style? | NOT IN DESIGN: focus style? | NOT IN DESIGN: disabled look? | NOT IN DESIGN: loading? | NOT IN DESIGN: what options are in the menu? The menu is not drawn. | NOT IN DESIGN: what if saving fails? |
| "Evidence in #client-kestrel" toggle (6750:1994, 6750:2150) | 48 high, padding 24 / 12, Brand Icon 24 + "Evidence in" Inter Semi Bold 14 #999999 + "#client-kestrel" Inter Semi Bold 16 #222222, `keyboard_arrow_down` 24 on the right. Thread is shown open below it | NOT IN DESIGN: hover style? | NOT IN DESIGN: focus style? | NOT IN DESIGN: disabled look? | NOT IN DESIGN: loading while the thread loads? | NOT IN DESIGN: what shows when there is no evidence thread? | NOT IN DESIGN: what if the source (Slack) cannot load? |
| Thread message (for example 6750:2011) | Avatar 32, radius 6, fill #A8A8A8, white initial; name Inter Bold 16 #222222; time Inter Medium 14 #898989; body Inter Regular 16 #8B8B8B. Older messages: group opacity 60%. Latest message per column: full opacity | NOT IN DESIGN: is a message interactive (hover, link to source)? | NOT IN DESIGN: focus style if it is interactive? | NOT IN DESIGN: question, n/a? | NOT IN DESIGN: loading? | NOT IN DESIGN: n/a or needed? | NOT IN DESIGN: n/a or needed? |

## 3. Tokens

The frame has no Figma variables. Every value below is a raw value from `get_design_context`, so each one needs a token.

### Color

| Use | Token | Value |
|---|---|---|
| Primary text (titles, names, values, button labels) | needs a token | #222222 |
| Response reason, overdue timers, selected row border, "Response" tag | needs a token | #FF4800 |
| Delivery reason text, "Delivery" label, "Promise made" tag | needs a token | #B27E08 |
| Queue client name | needs a token | #666666 |
| Queue person name (under the timer) | needs a token | #7B7B7B |
| Section labels ("What QTalo found", "Who's waiting", "Evidence in") | needs a token | #999999 |
| Detail header client name | needs a token | #808080 |
| Thread time | needs a token | #898989 |
| Thread body | needs a token | #8B8B8B |
| Thread message tags ("• Original ask", "• Team acknowledge") | needs a token | #C1C1C1 |
| Avatar fill | needs a token | #A8A8A8 |
| Avatar initial, selected row fill, button fill | needs a token | #FFFFFF |
| Search placeholder | needs a token | #BFBFBF |
| Footer "6 items" | needs a token | #686868 |
| Footer "Last checked" and times | needs a token | #848484 |
| Left rail fill | needs a token | #FBFBFC |
| Queue column header fill | needs a token | #FDFDFD |
| Date pill border | needs a token | #DDDDDD |
| Button border | needs a token | #000000 |
| Divider lines (6750:1742, 1762, 1787, 1952, 2003 and others) | needs a token | NOT IN DESIGN: lines come back as SVG files with no color value. What is the divider color? |
| Page background behind the panels (frame 6750:1706) | needs a token | NOT IN DESIGN: no fill returned. The screenshot looks white. Confirm #FFFFFF? |

### Spacing and size

| Use | Token | Value |
|---|---|---|
| Panel padding (search, header, rows, footer, detail sections) | needs a token | 24 px |
| Selected row inner padding (to keep content in place with the 5 px border) | needs a token | 24 px top/bottom, 19 px left/right |
| Selected row left border | needs a token | 5 px |
| Header bars (rail logo, search, detail header, footer) | needs a token | 72 px high |
| Queue column header | needs a token | 48 px high, padding 24 / 12 |
| Queue row height | needs a token | 97 px (121 px with a 2-line subject) |
| Queue: icon to subject gap | needs a token | 12 px |
| Queue: subject to client gap, timer to person gap | needs a token | 4 px |
| Queue: gap between Response and Delivery cells | needs a token | 8 px |
| Detail column header | needs a token | padding 16 top, 12 bottom, 24 sides, 52 px high |
| Detail section ("What QTalo found") | needs a token | padding 8 top, 20 bottom, 24 sides, gap 16 |
| Detail row (label + value) | needs a token | padding 20 / 24, gap 16, label width 110 px |
| Detail column bottom padding | needs a token | 16 px |
| Fixed heights to align the two columns | needs a token | "What QTalo found" block 157 px, "Promise made" row 116 px (Delivery column) |
| Button | needs a token | padding 6 px, gap 4 px, radius 4 px, border 1 px; gap between buttons 12 px |
| Date pill | needs a token | padding 12 / 6, radius 38 px, border 1 px; row padding 12 px top/bottom |
| Thread message | needs a token | padding 8 px top/bottom (last message 8 / 16), avatar to text gap 12 px, name row to body gap 8 px, name to time gap 8 px |
| Avatar | needs a token | 32 x 32 px, radius 6 px, padding 10 px |
| Icons | needs a token | 24 px (headers, toggles), 16 px (buttons, tags, queue source logo), 26 px (detail header source logo), 32 px (app logo) |
| Left rail | needs a token | 70 px wide; gap 43 px between logo block and hidden filters |
| Panel widths | needs a token | queue 926 px, detail 921 px, each detail column 460.5 px |

### Type

All text uses Inter, line height "normal" (no fixed line height in Figma).

| Use | Token | Family, size, weight, line height |
|---|---|---|
| Detail header subject | needs a token | Inter, 20, Bold 700, normal |
| "What QTalo found" statement | needs a token | Inter, 20, Bold 700, normal |
| Queue subject, rows 1 to 3 | needs a token | Inter, 20, Semi Bold 600, normal |
| Queue subject, rows 4 to 6 | needs a token | Inter, 20, Regular 400, normal |
| Queue client name | needs a token | Inter, 16, Regular 400, normal |
| Queue timer, reason and person | needs a token | Inter, 16, Medium 500, normal |
| Search placeholder | needs a token | Inter, 16, Regular 400, normal |
| Detail column title "Response" | needs a token | Inter, 16, Semi Bold 600, normal |
| Detail column title "Delivery" | needs a token | Inter, 16, Bold 700, normal |
| Detail column status ("47m overdue", "Delivery promise missed") | needs a token | Inter, 16, Medium 500, normal |
| Detail value ("Dylan Moore at Kestrel Apparel Co.", "Original ask" text) | needs a token | Inter, 16, Medium 500, normal |
| Next decision text | needs a token | Inter, 16, Semi Bold 600, normal |
| Section labels | needs a token | Inter, 14, Semi Bold 600, normal ("Owed by" is Regular 400, see open questions) |
| "#client-kestrel" | needs a token | Inter, 16, Semi Bold 600, normal |
| Thread name | needs a token | Inter, 16, Bold 700, normal |
| Thread time | needs a token | Inter, 14, Medium 500, normal |
| Thread tag | needs a token | Inter, 14, Semi Bold 600, normal |
| Thread body | needs a token | Inter, 16, Regular 400, normal |
| Avatar initial | needs a token | Inter, 16, Semi Bold 600, normal |
| Date pill | needs a token | Inter, 14, Semi Bold 600, normal |
| Button label | needs a token | Inter, 12, Semi Bold 600, normal |
| Queue column header ("Subject" Regular, "Response" and "Delivery" Medium) | needs a token | Inter, 14, Regular 400 / Medium 500, normal |
| Detail header client name | needs a token | Inter, 14, Semi Bold 600, normal |
| Footer | needs a token | Inter, 14, Regular 400, normal |

### Contrast (from scripts/contrast.py)

Background is #FFFFFF where the frame returned no fill (see the page background question). For the older thread messages (group opacity 60%), the color was first blended 60% over #FFFFFF with a small Python line, then checked with the script.

| Text | Background | Ratio | AA normal | AA large |
|---|---|---|---|---|
| #222222 primary text | #FFFFFF | 15.91:1 | pass | pass |
| #222222 column header | #FDFDFD | 15.64:1 | pass | pass |
| #666666 queue client name | #FFFFFF | 5.74:1 | pass | pass |
| #FF4800 Response reason and timers | #FFFFFF | 3.40:1 | FAIL | pass |
| #B27E08 Delivery reason | #FFFFFF | 3.57:1 | FAIL | pass |
| #7B7B7B queue person | #FFFFFF | 4.23:1 | FAIL | pass |
| #BFBFBF search placeholder | #FFFFFF | 1.84:1 | FAIL | FAIL |
| #686868 "6 items" | #FFFFFF | 5.57:1 | pass | pass |
| #848484 "Last checked" and times | #FFFFFF | 3.74:1 | FAIL | pass |
| #808080 detail header client name | #FFFFFF | 3.95:1 | FAIL | pass |
| #999999 section labels | #FFFFFF | 2.85:1 | FAIL | FAIL |
| #898989 thread time (latest message) | #FFFFFF | 3.50:1 | FAIL | pass |
| #8B8B8B thread body (latest message) | #FFFFFF | 3.41:1 | FAIL | pass |
| #FFFFFF avatar initial (latest message) | #A8A8A8 | 2.38:1 | FAIL | FAIL |
| #7A7A7A thread name, older message (#222222 at 60%) | #FFFFFF | 4.29:1 | FAIL | pass |
| #B8B8B8 thread time, older message (#898989 at 60%) | #FFFFFF | 1.98:1 | FAIL | FAIL |
| #DADADA thread tag, older message (#C1C1C1 at 60%) | #FFFFFF | 1.40:1 | FAIL | FAIL |
| #B9B9B9 thread body, older message (#8B8B8B at 60%) | #FFFFFF | 1.96:1 | FAIL | FAIL |
| #FFFFFF avatar initial, older message (on #A8A8A8 at 60% = #CBCBCB) | #CBCBCB | 1.62:1 | FAIL | FAIL |

## 4. Copy

Max length is the space the layout gives. Figma does not set a character limit or a truncation rule; see open questions.

| Location | String (exact) | Max length |
|---|---|---|
| Search placeholder (6750:1739) | Search | 1 line, fills the 926 px bar |
| Queue column header (6750:1746) | Subject | 1 line, 439 px column |
| Queue column header (6750:1753) | Response | 1 line, about 215 px cell with icons |
| Queue column header (6750:1761) | Delivery | 1 line, about 215 px cell with icon |
| Queue row subject (6750:1778, 1860, 1931) | Contractor agreement review | Queue: wraps in 405.5 px (row 6 shows 2 lines). Detail header: 1 line, no wrap |
| Queue row subject (6750:1799) | Intake packet readiness | wraps in 407 px |
| Queue row subject (6750:1818) | Data-processing addendum | wraps in 407 px |
| Queue row subject (6750:1838) | Invoice account number | wraps in 407 px |
| Queue row subject (6750:1881) | ADP access issue payroll lead still locked out | wraps in 379 px, 2 lines shown |
| Queue client name (6750:1779, 1861, 1932) | Kestrel Apparel Co. | 1 line, no wrap |
| Queue client name (6750:1800, 1819) | Northstar Health Partners | 1 line, no wrap |
| Queue client name (6750:1839) | Ridgeway Foods | 1 line, no wrap |
| Queue client name (6750:1882) | Ironwood Logistics | 1 line, no wrap |
| Queue Response cell (6750:1782, 1944) | 47m overdue | Queue: 216.75 px cell. Detail: 1 line |
| Queue Response cell (6750:1803) | 1h 5m overdue | 215.5 px cell |
| Queue Response cell, hidden at opacity 0 (6750:1821) | 1h 5m overdue / 3h | 215.5 px cell ("/ 3h" in #A1A1A1) |
| Queue Response cell (6750:1842) | 17m until target | 215.5 px cell |
| Queue Response cell (6750:1864) | 32m until  target | 216.75 px cell (two spaces before "target" in Figma) |
| Queue Response cell (6750:1885) | Client dissatisfaction | 215.5 px cell |
| Queue Delivery cell (6750:1785, 2104; hidden copies 1805, 1844, 1867) | Delivery promise missed | Queue: 216.75 px cell. Detail: 1 line |
| Queue Delivery cell (6750:1823; hidden copy 1888) | Client asked again | 215.5 px cell |
| Queue person (6750:1783) | Dylan Moore | 1 line, no wrap |
| Queue person (6750:1786, hidden copy 1868) | Mara Ellis (with a trailing space in Figma) | 1 line, no wrap |
| Queue person (6750:1804, 1824, hidden copy 1889) | Camille Ross | 1 line, no wrap |
| Queue person (6750:1843) | Julian Reyes | 1 line, no wrap |
| Queue person (6750:1865) | Ava Chen | 1 line, no wrap |
| Queue person (6750:1886) | Teresa Lang | 1 line, no wrap |
| Footer count (6750:1892) | 6 items | 1 line |
| Footer label (6750:1894) | Last checked | 1 line |
| Footer Gmail time (6750:1903) | Friday 12:00 PM | 1 line |
| Footer Slack time (6750:1915) | Friday 11:58 AM | 1 line |
| Detail header client (6750:1932) | Kestrel Apparel Co. | 1 line, no wrap |
| Detail column title (6750:1943) | Response | 1 line |
| Detail column title (6750:2103) | Delivery | 1 line |
| Section label (6750:1949, 2109) | What QTalo found | 1 line, 412.5 px |
| Response finding (6750:1950) | Client request has no visible acknowledgement in this Slack thread before the 3-hour response window expired. | wraps in 412.5 px, 4 lines shown in a 157 px block |
| Delivery finding (6750:2110) | Due Wednesday · no delivery or updated ETA found | wraps in 412.5 px, 2 lines shown in a 157 px block |
| Section label (6750:1954) | Who's waiting | 110 px label column |
| Value (6750:1955) | Dylan Moore at Kestrel Apparel Co. | 1 line, no wrap, about 286 px space |
| Section label (6750:2215) | Original ask (with a trailing space in Figma) | 110 px label column |
| Value (6750:2216) | Heads up team, we've got a new contractor starting next week and will need the standard agreement reviewed before then. | wraps in 286.5 px, 4 lines shown |
| Section label (6750:2114) | Owed by | 110 px label column |
| Value (6750:2115) | Mara Ellis | 1 line, no wrap |
| Section label (6750:2219) | Promise made (with a trailing space in Figma) | 110 px label column |
| Value (6750:2220) | Final redlines by Wednesday 5:00 PM | wraps in 286.5 px, row fixed at 116 px |
| Section label (6750:1977, 2133) | Next decision | 110 px |
| Next decision, Response (6750:1979) | Confirm who should acknowledge the contractor agreement request. | wraps in 412.5 px, 2 lines shown |
| Next decision, Delivery (6750:2135) | Check status and update the client if delivery is not imminent. | wraps in 412.5 px, 2 lines shown |
| Button (6750:1985) | Response sent | 1 line, no wrap |
| Button (6750:1990) | No response needed | 1 line, no wrap |
| Button (6750:2141) | Mark completed | 1 line, no wrap |
| Dropdown button (6750:2143) | Correct | 1 line, no wrap |
| Evidence label (6750:1997, 2153) | Evidence in | 1 line |
| Evidence channel (6750:1998, 2154) | #client-kestrel | 1 line, no wrap |
| Date pill (6750:2008, 2164) | Monday | 1 line |
| Date pill (6750:2042) | Tuesday | 1 line |
| Date pill (6750:2066) | Today | 1 line |
| Avatar initial (6750:2013, 2033, 2057, 2071, 2082, 2169) | D | 1 character |
| Avatar initial (6750:2023, 2047, 2180) | M | 1 character |
| Thread name (6750:2016, 2036, 2060, 2074, 2086, 2172) | Dylan Moore | 1 line, no wrap |
| Thread name (6750:2026, 2050, 2184) | Mara Ellis | 1 line, no wrap |
| Thread time (6750:2017) | 9:12 AM | 1 line |
| Thread time (6750:2027) | 9:40 AM | 1 line |
| Thread time (6750:2037) | 2:15 PM | 1 line |
| Thread time (6750:2051) | 10:05 AM | 1 line |
| Thread time (6750:2061) | 4:30 PM | 1 line |
| Thread time (6750:2075) | 10:58 AM | 1 line |
| Thread time (6750:2087) | 11:36 AM | 1 line |
| Thread time (6750:2173) | Mon 9:04 AM | 1 line |
| Thread time (6750:2185) | Mon, 9:18 AM | 1 line |
| Thread tag (6750:2019) | • Original ask | 1 line |
| Thread tag (6750:2029, 2053) | • Team acknowledge | 1 line |
| Thread tag with `reply` icon (6750:2092) | Response | 1 line |
| Thread tag with `timer` icon (6750:2190) | Promise made | 1 line |
| Thread body (6750:2020) | Heads up team, we've got a new contractor starting next week and will need the standard agreement reviewed before then. | wraps in 368 px, 3 lines shown |
| Thread body (6750:2030) | Thanks for the heads up, Dylan — send over the contractor specifics whenever you have them and we'll get the template pulled together. | wraps in 368 px, 3 lines shown |
| Thread body (6750:2038) | Sending the contractor details over now — let me know if anything else is needed on our end. | wraps in 368 px, 2 lines shown |
| Thread body (6750:2054) | Got it, thanks. Reviewing the NDA language against our standard clauses today. | wraps in 368 px, 2 lines shown |
| Thread body (6750:2062) | Any update on this? We'd like to get it locked before the work trial starts. | wraps in 368 px, 2 lines shown |
| Thread body (6750:2076) | Can someone review the contractor agreement before noon? We have the work trial starting tomorrow and need the NDA language confirmed today. | wraps in 368 px, 4 lines shown |
| Thread body (6750:2093) | Just checking this landed. We are blocked on sending the invite until we hear back. | wraps in 368 px, 2 lines shown |
| Thread body (6750:2174) | Can you send final redlines this week? We need the agreement before the contractor starts. | wraps in 368 px, 2 lines shown |
| Thread body (6750:2191) | Received. We will send final redlines by Wednesday at 5:00 PM. | wraps in 368 px, 2 lines shown |

## 5. Behavior

### Interactions

- Queue row: the first row is drawn as selected (white fill, 5 px #FF4800 left border) and the detail panel shows that item. Clicking a row to select it is implied by the layout but not drawn as a flow. NOT IN DESIGN: confirm that a click on a row opens it in the detail panel.
- Queue sort: an `arrow_downward_alt` icon sits next to the "Response" column header, so the queue looks sorted by Response. NOT IN DESIGN: sort rule, and whether headers are clickable.
- Response decision buttons: "Response sent" and "No response needed". Delivery decision buttons: "Mark completed" and a "Correct" dropdown. NOT IN DESIGN: what happens after each click (the item leaves the queue? a confirmation? undo?).
- "Evidence in #client-kestrel" has a `keyboard_arrow_down` icon, so it looks like a collapse/expand toggle. The thread is drawn open. NOT IN DESIGN: default open or closed, and the closed look.
- Evidence thread: older messages are at 60% opacity; the latest message in each column (the one that triggered the reason) is at full opacity with a colored tag ("Response" in #FF4800, "Promise made" in #B27E08).
- Thread container (6750:2004, 6750:2160) uses vertical scroll (`overflow-y: auto`) and pins content to the bottom (`justify-content: flex-end`), so the newest message sits at the bottom.

### Breakpoints

NOT IN DESIGN: only one frame size exists (1920 x 1511). How should the three panels behave below 1920 px (for example 1440 or 1280)? Should the two detail columns stack?

### Edge cases

- Long queue subject wraps to 2 lines (row 6, "ADP access issue payroll lead still locked out"); the row grows from 97 to 121 px.
- An item can have a Response reason only (rows 2, 4, 5, 6), a Delivery reason only (row 3) or both (row 1). The empty cell keeps its width.
- Several cells hold text at opacity 0 (6750:1805, 1821, 1844, 1866, 1887). They are invisible but still take space. NOT IN DESIGN: should developers render them at all?
- The two detail columns use fixed heights (157 px "What QTalo found", 116 px "Promise made") so the rows line up across columns. NOT IN DESIGN: what happens when the text is longer than the fixed height?
- NOT IN DESIGN: what does the detail panel show when no row is selected?
- NOT IN DESIGN: how are very long names, client names or channel names truncated (ellipsis or wrap)?
- Hidden layers in the frame (not part of the visible screen): "Filters" in the rail (6750:1711), `keyboard_arrow_down` in each detail column header (6750:1945, 2105), "Aviso" lines (6750:2077, 2175), "Rectangle 11" (6750:2192, 2193).

## 6. Accessibility

Summary from the `accessibility-reviewer` subagent (full review: `accessibility-review.md` in this folder). Result: FAIL.

- 45 checks: 14 pass, 27 fail, 4 cannot verify.
- Contrast: 16 of 20 rows fail AA normal (4.5:1). Main groups: the status colors #FF4800 (3.40) and #B27E08 (3.57), the light grays (#999999 labels 2.85, #BFBFBF placeholder 1.84) and all thread text at 60% opacity (1.40 to 4.29). The "Subject" header and date pill text colors are not in the spec, so they could not be checked.
- Focus: no focus style is in the design for any control (search, headers, rows, 4 buttons, evidence toggles). The focus order is not written down.
- Labels: no alt text or "decorative" mark for the Slack and Gmail logos, the sort arrow, Material icons, avatars and the app logo. The search field has only a placeholder, no accessible name.
- Pass: target size for all controls (all 24 x 24 or more), visible button labels, and status is not shown by color alone.
- This is an automated review. A manual keyboard and screen reader check is still needed.

## 7. Open questions

1. No Figma variables in the frame. Should the developer map these raw values to the app's `--qt-*` tokens? Note: the app has `--qt-fire` = #FF4B33, but Figma uses #FF4800 for the Response color. Which one is right?
2. Divider line color is not returned (lines are SVG). What color should dividers use?
3. Page background behind the panels has no fill in Figma. Is it #FFFFFF?
4. Queue subjects in rows 1 to 3 are Semi Bold and rows 4 to 6 are Regular. Does this mean unread vs read, or something else?
5. Rows 1 and 5 have the same subject and client ("Contractor agreement review", "Kestrel Apparel Co.") with different people (Dylan Moore, Ava Chen). Is this intended: two items, or one item shown twice?
6. "32m until  target" has two spaces. Typo?
7. Several labels have a trailing space ("Original ask ", "Promise made ", "Mara Ellis "). Safe to trim?
8. "Owed by" label is Regular 400; the other section labels are Semi Bold 600. Intended?
9. Detail column title "Response" is Semi Bold 600 and "Delivery" is Bold 700. Intended?
10. Thread time formats differ: "9:12 AM" (Response column), "Mon 9:04 AM" and "Mon, 9:18 AM" (Delivery column). Which format is correct?
11. The rail divider (6750:1733) is 1080 px high, but the frame is 1511 px high. Should it run the full height?
12. The selected row border is #FF4800 (Response color) even though row 1 has both reasons. What color should a row with only a Delivery reason use when selected?
13. Hover, focus, disabled, loading, empty and error states are not drawn for any element (see States). Can design add them, or should the developer use the app's standard states?
