# Handoff: Kestrel Case (Response+Delivery) - Option A

## 1. Source

- Figma link: https://www.figma.com/design/KXDasTBnxU4SVR68K44kiV/MVP-3.0-Wireframes?node-id=6750-1705
- Frame name and node id: "Kestrel Case (Response+Delivery) - Option A", 6750:1705
- Frame size: 1920 x 1511 px (inner content frame 6750:1706 is 1917 x 1511; the top frame has 3 px right padding)
- Date: 2026-10-22 (read from Figma on this date)
- Components in use: one component instance only: "Brand Icon" (6750:1996 and 6750:2152, Slack logo inside). Everything else is plain frames, text and vectors (Material-style icons named reply, timer, arrow_downward_alt, keyboard_arrow_down, check, search).
- Known constraints: the frame has no Figma variables (`get_variable_defs` returned `{}`), so every value below is a raw value marked "needs a token". Page background read from the top frame fill: `bg-white` = #FFFFFF (6750:1705). Reference image: `figma-reference.png` in this folder.

Layout (from `get_metadata`):

| Area | Node | Size | Notes |
|---|---|---|---|
| Left rail | 6750:1707 | 70 x 1511 | Fill #FBFBFC. QTalo logo 32 x 32 at top. "Filters" group (Slack, Gmail) is hidden (6750:1711). |
| Rail divider | 6750:1733 | 1 x 1080 | Stroke #D8D8DD. Only 1080 px tall in a 1511 px frame. |
| Queue column | 6750:1734 | 926 x 1511 | Search bar (72 high), list header (48 high), 6 rows, footer (72 high). |
| Column divider | 6750:1916 | 1 x 1511 | Stroke #B8B8B8 |
| Detail panel | 6750:1917 | 921 x 1511 | Header (72 high), then two columns of 460.5: Response (6750:1935) and Delivery (6750:2095), split by a 1 px line #D8D8DD (6750:2094). |

## 2. States

Figma shows one static state of the screen: row 1 ("Contractor agreement review", Kestrel Apparel Co.) is selected and its detail is open.

| Element | Default | Hover | Focus | Disabled | Loading | Empty | Error |
|---|---|---|---|---|---|---|---|
| Search field (6750:1735) | Search icon 24 px #BFBFBF + placeholder "Search" 16 px Inter Regular #BFBFBF, no border, no fill | NOT IN DESIGN: is there a hover style? | NOT IN DESIGN: what does the focus ring look like, and does the placeholder change? | NOT IN DESIGN: can search be disabled? | NOT IN DESIGN: is there a loading state while results come in? | NOT IN DESIGN: what does the list show when no item matches? | NOT IN DESIGN: what shows if search fails? |
| Response sort arrow (6750:1754) | arrow_downward_alt 24 x 24, #A3A3A3, next to "Response" header | NOT IN DESIGN: hover style? | NOT IN DESIGN: focus style? | NOT IN DESIGN: is it ever disabled? | NOT IN DESIGN | NOT IN DESIGN: is the arrow shown when the list is empty? | NOT IN DESIGN |
| Delivery column header (6750:1757) | timer icon 24 px #B27E08 + "Delivery" 14 px Medium #222222, no sort arrow | NOT IN DESIGN: can the list also sort by Delivery? | NOT IN DESIGN | NOT IN DESIGN | NOT IN DESIGN | NOT IN DESIGN | NOT IN DESIGN |
| Queue row, selected (6750:1764) | Fill #FFFFFF, left border 5 px #FF4800, padding 24 px top/bottom and 19 px left/right | NOT IN DESIGN: hover style of a selected row? | NOT IN DESIGN: focus style of a row? | NOT IN DESIGN | NOT IN DESIGN | Not applicable (a row always has data) | NOT IN DESIGN: what shows if the item cannot load? |
| Queue row, not selected (6750:1788, 1807, 1827, 1870) | No fill (page #FFFFFF shows through), no left border, padding 24 px | NOT IN DESIGN: hover style? | NOT IN DESIGN: focus style? | NOT IN DESIGN | NOT IN DESIGN | Not applicable | NOT IN DESIGN |
| Queue row 5 (6750:1846) | Fill #FFFFFF and left border 5 px #FFFFFF (white on white, so it looks like a not-selected row) | NOT IN DESIGN: is the white border a leftover, or a different state (for example "read")? | NOT IN DESIGN | NOT IN DESIGN | NOT IN DESIGN | Not applicable | NOT IN DESIGN |
| Queue list (6750:1763, 1826) | 6 rows, footer "6 items" | Not applicable | Not applicable | Not applicable | NOT IN DESIGN: what shows while the queue loads? | NOT IN DESIGN: what shows when there are 0 items? | NOT IN DESIGN: what shows if the queue fails to load? |
| "Response sent" button (6750:1981) | 120 x 30, border 1 px #000000, radius 4 px, padding 6 px, check icon 16 px #1C1B1F + label 12 px Semi Bold #222222 | NOT IN DESIGN: hover style? | NOT IN DESIGN: focus style? | NOT IN DESIGN: is it disabled after use? | NOT IN DESIGN: is there a loading state after click? | Not applicable | NOT IN DESIGN: what shows if the action fails? |
| "No response needed" button (6750:1986) | 134 x 29, border 1 px #000000, radius 4 px, padding 6 px, label 12 px Semi Bold #222222. It has a hidden check icon (6750:1987). | NOT IN DESIGN: hover style? | NOT IN DESIGN: focus style? | NOT IN DESIGN: disabled style? | NOT IN DESIGN: loading style? | Not applicable | NOT IN DESIGN: error after click? |
| "Mark completed" button (6750:2137) | 129 x 30, border 1 px #000000, radius 4 px, padding 6 px, check icon 16 px #1C1B1F + label 12 px Semi Bold #222222 | NOT IN DESIGN: hover style? | NOT IN DESIGN: focus style? | NOT IN DESIGN: disabled style? | NOT IN DESIGN: loading style? | Not applicable | NOT IN DESIGN: error after click? |
| "Correct" dropdown button (6750:2142) | 79 x 30, border 1 px #000000, radius 4 px, padding 6 px, label 12 px Semi Bold #222222 + keyboard_arrow_down 16 px #222222 | NOT IN DESIGN: hover style? | NOT IN DESIGN: focus style? | NOT IN DESIGN: disabled style? | NOT IN DESIGN: loading style? | NOT IN DESIGN: what options are in the menu? | NOT IN DESIGN: error after a choice? |
| "Evidence in #client-kestrel" bar with expand arrow (6750:1994, 2150) | 462 x 48, Slack Brand Icon 24 px + "Evidence in" + channel name + keyboard_arrow_down 24 px #222222 at the right | NOT IN DESIGN: hover style? | NOT IN DESIGN: focus style? | NOT IN DESIGN | NOT IN DESIGN | NOT IN DESIGN: what shows if there is no evidence thread? | NOT IN DESIGN: what shows if the source cannot load? |
| Evidence thread (6750:2004, 2160) | Scrolls in y (Figma: overflow-y auto, overflow-x clip), content sits at the bottom (justify end). Older messages at 60% opacity, latest message at 100%. | Not applicable | NOT IN DESIGN: can the thread get keyboard focus to scroll? | Not applicable | NOT IN DESIGN: loading state of the thread? | NOT IN DESIGN: empty thread? | NOT IN DESIGN: error state of the thread? |
| Panel collapse arrows (6750:1945, 2105) | Hidden in Figma | NOT IN DESIGN: are these arrows part of the build? | NOT IN DESIGN | NOT IN DESIGN | NOT IN DESIGN | NOT IN DESIGN | NOT IN DESIGN |
| Source filters in rail (6750:1711) | Hidden in Figma (Slack and Gmail, 48 x 48 each) | NOT IN DESIGN: are these filters part of the build? | NOT IN DESIGN | NOT IN DESIGN | NOT IN DESIGN | NOT IN DESIGN | NOT IN DESIGN |

## 3. Tokens

### Color

No Figma variables in this frame. Every color needs a token.

| Use | Token | Value |
|---|---|---|
| Page background (6750:1705), selected row fill, rows 1 and 5 | needs a token | #FFFFFF |
| Left rail fill (6750:1707) | needs a token | #FBFBFC |
| List header fill (6750:1743) | needs a token | #FDFDFD |
| Primary text: titles, values, headers, names, button labels, date pills | needs a token | #222222 |
| Row customer name | needs a token | #666666 |
| Row person names | needs a token | #7B7B7B |
| Response color: selected row border, clocks, Response title, reply icons, Response tag | needs a token | #FF4800 |
| Delivery color: reasons, Delivery title, timer icons, Promise made tag | needs a token | #B27E08 |
| Hidden "/ 3h" text (opacity 0, 6750:1821) | needs a token | #A1A1A1 |
| Footer count "6 items" | needs a token | #686868 |
| Footer "Last checked" and timestamps | needs a token | #848484 |
| Detail header customer name | needs a token | #808080 |
| Field labels, "Evidence in" | needs a token | #999999 |
| Thread timestamps | needs a token | #898989 |
| Thread body text | needs a token | #8B8B8B |
| Thread tags "Original ask", "Team acknowledge" | needs a token | #C1C1C1 |
| Avatar fill | needs a token | #A8A8A8 |
| Avatar letter | needs a token | #FFFFFF |
| Search placeholder and search icon | needs a token | #BFBFBF |
| Sort arrow icon | needs a token | #A3A3A3 |
| Check icon | needs a token | #1C1B1F |
| Button border | needs a token | #000000 |
| Date pill border and date pill side lines | needs a token | #DDDDDD |
| Queue dividers (lines 4, 6, 7), rail divider, column-split line 3 | needs a token | #D8D8DD |
| Detail field dividers and evidence bar bottom line | needs a token | #E8E8EC |
| Queue/detail vertical line 2 and divider above evidence bar (6750:1991, 2147) | needs a token | #B8B8B8 |
| QTalo logo | needs a token | #6663FF |
| Slack logo (brand, 4 colors) | needs a token (brand asset, keep as SVG) | #E01E5A, #36C5F0, #2EB67D, #ECB22E |
| Gmail logo (brand, 5 colors) | needs a token (brand asset, keep as SVG) | #EA4335, #C5221F, #FBBC04, #34A853, #4285F4 |

### Spacing and size

| Use | Token | Value |
|---|---|---|
| Left rail width | needs a token | 70 px |
| Top bars height (rail logo area, search bar, detail header, footer) | needs a token | 72 px |
| Queue column width | needs a token | 926 px |
| Detail panel width / each column | needs a token | 921 px / 460.5 px |
| Outer side padding (search, rows, panel, footer) | needs a token | 24 px |
| Search bar padding / icon-to-text gap | needs a token | 24 px all sides / 8 px |
| List header padding | needs a token | 12 px top/bottom, 24 px left/right (48 px high) |
| List header: gap between Response and Delivery groups / icon-to-label | needs a token | 8 px / 8 px (6 px between "Response" and sort arrow) |
| Queue row padding | needs a token | 24 px (selected row: 24 px top/bottom, 19 px left/right plus 5 px left border) |
| Queue row: source icon box / icon | needs a token | 24 x 24 box with 2 px top padding; Slack icon 16 x 16, Gmail icon 16.7 x 12.5 |
| Queue row: icon to text gap / title to customer gap | needs a token | 12 px / 4 px |
| Queue row: gap between Response and Delivery meta / clock to person gap | needs a token | 8 px / 4 px |
| Queue row height | needs a token | 97 px (one-line title), 121 px (two-line title, row 6) |
| Selected row left border | needs a token | 5 px |
| Footer padding / gap between footer items / icon-to-time gap | needs a token | 24 px / 16 px / 4 px |
| Detail header padding / icon box / icon / gap | needs a token | 12 px top/bottom, 24 px left/right / 48 x 48 / 26 x 26 / 8 px, title-to-customer 16 px |
| Panel title row padding | needs a token | 16 px top, 12 px bottom, 24 px left/right |
| "What QTalo found" block padding / gap | needs a token | 8 px top, 20 px bottom, 24 px left/right / 16 px |
| Field rows padding / label width / label-to-value gap | needs a token | 20 px top/bottom, 24 px left/right / 110 px / 16 px |
| Panel summary bottom padding | needs a token | 16 px |
| "Next decision" block gap / button gap | needs a token | 16 px / 12 px |
| Button padding / radius / icon-to-label gap | needs a token | 6 px / 4 px / 4 px |
| Evidence bar padding / height | needs a token | 12 px top/bottom, 24 px left/right / 48 px |
| Date pill padding / radius / row padding | needs a token | 6 px top/bottom, 12 px left/right / 38 px / 12 px top/bottom |
| Message padding / avatar-to-text gap / name-row gap / name-to-body gap | needs a token | 8 px top/bottom (last message: 8 px top, 16 px bottom) / 12 px / 8 px / 8 px |
| Avatar size / radius / padding | needs a token | 32 x 32 / 6 px / 10 px |
| Thread tag icon / icon-to-label gap | needs a token | 16 x 16 / 6 px |
| Older messages opacity | needs a token | 60% |
| Divider line weight | needs a token | 1 px |

### Type

All text is Inter, line height "normal" (Figma `leading-[normal]`).

| Use | Token | Family, size, weight, line height |
|---|---|---|
| Detail header title, "What QTalo found" finding text | needs a token | Inter, 20 px, Bold 700, normal |
| Queue row title (rows 1 to 3) | needs a token | Inter, 20 px, Semi Bold 600, normal |
| Queue row title (rows 4 to 6) | needs a token | Inter, 20 px, Regular 400, normal |
| Delivery panel title, thread names | needs a token | Inter, 16 px, Bold 700, normal |
| Response panel title, Next decision text, channel name, avatar letter | needs a token | Inter, 16 px, Semi Bold 600, normal |
| Row clocks and reasons, row person names, panel clock/reason, field values | needs a token | Inter, 16 px, Medium 500, normal |
| Row customer name, search placeholder, thread body | needs a token | Inter, 16 px, Regular 400, normal |
| Field labels (except "Owed by"), "Evidence in", date pills, thread tags, detail header customer | needs a token | Inter, 14 px, Semi Bold 600, normal |
| List header "Response", "Delivery", thread times | needs a token | Inter, 14 px, Medium 500, normal |
| List header "Subject", field label "Owed by", footer text | needs a token | Inter, 14 px, Regular 400, normal |
| Button labels | needs a token | Inter, 12 px, Semi Bold 600, normal |

### Contrast (from scripts/contrast.py)

Background: page #FFFFFF (read from the top frame fill, 6750:1705), list header #FDFDFD (6750:1743). Opacity rows use `--opacity 0.6`. Icons use `--icon` (3:1). One row per text use.

| Use | Color | Background | Size | Ratio | Needs | Result |
|---|---|---|---|---|---|---|
| Search placeholder (6750:1739) | #BFBFBF | #FFFFFF | 16px | 1.84:1 | 4.5:1 | FAIL |
| Subject header (6750:1746) | #222222 | #FDFDFD | 14px | 15.64:1 | 4.5:1 | pass |
| Response column header (6750:1753) | #222222 | #FDFDFD | 14px | 15.64:1 | 4.5:1 | pass |
| Delivery column header (6750:1761) | #222222 | #FDFDFD | 14px | 15.64:1 | 4.5:1 | pass |
| Row title, semibold (6750:1778, 1799, 1818) | #222222 | #FFFFFF | 20px | 15.91:1 | 4.5:1 | pass |
| Row title, regular (6750:1838, 1860, 1881) | #222222 | #FFFFFF | 20px | 15.91:1 | 4.5:1 | pass |
| Row customer name (6750:1779, 1800, 1819, 1839, 1861, 1882) | #666666 | #FFFFFF | 16px | 5.74:1 | 4.5:1 | pass |
| Row Response clock or reason (6750:1782, 1803, 1842, 1864, 1885) | #FF4800 | #FFFFFF | 16px | 3.40:1 | 4.5:1 | FAIL |
| Row Response person (6750:1783, 1804, 1843, 1865, 1886) | #7B7B7B | #FFFFFF | 16px | 4.23:1 | 4.5:1 | FAIL |
| Row Delivery reason (6750:1785, 1823) | #B27E08 | #FFFFFF | 16px | 3.57:1 | 4.5:1 | FAIL |
| Row Delivery person (6750:1786, 1824) | #7B7B7B | #FFFFFF | 16px | 4.23:1 | 4.5:1 | FAIL |
| Footer count (6750:1892) | #686868 | #FFFFFF | 14px | 5.57:1 | 4.5:1 | pass |
| Footer Last checked (6750:1894) | #848484 | #FFFFFF | 14px | 3.74:1 | 4.5:1 | FAIL |
| Footer timestamps (6750:1903, 1915) | #848484 | #FFFFFF | 14px | 3.74:1 | 4.5:1 | FAIL |
| Detail header title, bold (6750:1931) | #222222 | #FFFFFF | 20px bold | 15.91:1 | 3:1 | pass |
| Detail header customer, semibold (6750:1932) | #808080 | #FFFFFF | 14px | 3.95:1 | 4.5:1 | FAIL |
| Response panel title, semibold (6750:1943) | #FF4800 | #FFFFFF | 16px | 3.40:1 | 4.5:1 | FAIL |
| Response panel clock (6750:1944) | #FF4800 | #FFFFFF | 16px | 3.40:1 | 4.5:1 | FAIL |
| Delivery panel title, bold (6750:2103) | #B27E08 | #FFFFFF | 16px bold | 3.57:1 | 4.5:1 | FAIL |
| Delivery panel reason (6750:2104) | #B27E08 | #FFFFFF | 16px | 3.57:1 | 4.5:1 | FAIL |
| Field labels, semibold (6750:1949, 1954, 2215, 1977, 2109, 2219, 2133) | #999999 | #FFFFFF | 14px | 2.85:1 | 4.5:1 | FAIL |
| Field label Owed by, regular (6750:2114) | #999999 | #FFFFFF | 14px | 2.85:1 | 4.5:1 | FAIL |
| Evidence in label (6750:1997, 2153) | #999999 | #FFFFFF | 14px | 2.85:1 | 4.5:1 | FAIL |
| Finding text, bold (6750:1950, 2110) | #222222 | #FFFFFF | 20px bold | 15.91:1 | 3:1 | pass |
| Field values, medium (6750:1955, 2216, 2115, 2220) | #222222 | #FFFFFF | 16px | 15.91:1 | 4.5:1 | pass |
| Next decision text, semibold (6750:1979, 2135) | #222222 | #FFFFFF | 16px | 15.91:1 | 4.5:1 | pass |
| Action button labels, semibold (6750:1985, 1990, 2141, 2143) | #222222 | #FFFFFF | 12px | 15.91:1 | 4.5:1 | pass |
| Channel name (6750:1998, 2154) | #222222 | #FFFFFF | 16px | 15.91:1 | 4.5:1 | pass |
| Date pills (6750:2008, 2042, 2066, 2164) | #222222 | #FFFFFF | 14px | 15.91:1 | 4.5:1 | pass |
| Thread name at 60%, bold (6750:2016, 2026, 2036, 2050, 2060, 2074, 2172) | #222222 at 60% = #7A7A7A | #FFFFFF | 16px bold | 4.29:1 | 4.5:1 | FAIL |
| Thread time at 60% (6750:2017, 2027, 2037, 2051, 2061, 2075, 2173) | #898989 at 60% = #B8B8B8 | #FFFFFF | 14px | 1.98:1 | 4.5:1 | FAIL |
| Thread tag at 60% (6750:2019, 2029, 2053) | #C1C1C1 at 60% = #DADADA | #FFFFFF | 14px | 1.40:1 | 4.5:1 | FAIL |
| Thread body at 60% (6750:2020, 2030, 2038, 2054, 2062, 2076, 2174) | #8B8B8B at 60% = #B9B9B9 | #FFFFFF | 16px | 1.96:1 | 4.5:1 | FAIL |
| Avatar letter at 60% (6750:2013, 2023, 2033, 2047, 2057, 2071, 2169): white on avatar #A8A8A8 at 60% = #CBCBCB | #FFFFFF | #CBCBCB | 16px | 1.62:1 | 4.5:1 | FAIL |
| Avatar letter, last message (6750:2082, 2180) | #FFFFFF | #A8A8A8 | 16px | 2.38:1 | 4.5:1 | FAIL |
| Last message name, bold (6750:2086, 2184) | #222222 | #FFFFFF | 16px bold | 15.91:1 | 4.5:1 | pass |
| Last message time (6750:2087, 2185) | #898989 | #FFFFFF | 14px | 3.50:1 | 4.5:1 | FAIL |
| Last message Response tag, semibold (6750:2092) | #FF4800 | #FFFFFF | 14px | 3.40:1 | 4.5:1 | FAIL |
| Last message Promise made tag, semibold (6750:2190) | #B27E08 | #FFFFFF | 14px | 3.57:1 | 4.5:1 | FAIL |
| Last message body (6750:2093, 2191) | #8B8B8B | #FFFFFF | 16px | 3.41:1 | 4.5:1 | FAIL |
| List header reply icon (6750:1750) | #FF4800 | #FDFDFD | icon | 3.34:1 | 3:1 | pass |
| List header sort arrow (6750:1754) | #A3A3A3 | #FDFDFD | icon | 2.48:1 | 3:1 | FAIL |
| List header timer icon (6750:1758) | #B27E08 | #FDFDFD | icon | 3.51:1 | 3:1 | pass |
| Selected row left border 5px (6750:1764) | #FF4800 | #FFFFFF | icon | 3.40:1 | 3:1 | pass |
| Search icon (6750:1736) | #BFBFBF | #FFFFFF | icon | 1.84:1 | 3:1 | FAIL |
| Slack source icon, darkest part (6750:1768, 1850, 1906, 1921, Brand Icon) | #E01E5A | #FFFFFF | icon | 4.66:1 | 3:1 | pass |
| Gmail source icon, darkest part (6750:1792, 1811, 1831, 1874, 1897) | #C5221F | #FFFFFF | icon | 5.80:1 | 3:1 | pass |
| Response panel reply icon (6750:1940) | #FF4800 | #FFFFFF | icon | 3.40:1 | 3:1 | pass |
| Delivery panel timer icon (6750:2100) | #B27E08 | #FFFFFF | icon | 3.57:1 | 3:1 | pass |
| Check icon in buttons (6750:1982, 2138) | #1C1B1F | #FFFFFF | icon | 17.13:1 | 3:1 | pass |
| Button border 1px (6750:1981, 1986, 2137, 2142) | #000000 | #FFFFFF | icon | 21.00:1 | 3:1 | pass |
| Expand and dropdown arrows (6750:1999, 2155, 2144) | #222222 | #FFFFFF | icon | 15.91:1 | 3:1 | pass |
| Thread Response tag icon (6750:2089) | #FF4800 | #FFFFFF | icon | 3.40:1 | 3:1 | pass |
| Thread Promise made tag icon (6750:2187) | #B27E08 | #FFFFFF | icon | 3.57:1 | 3:1 | pass |

Not checked, with reason: the QTalo logo (#6663FF, 6750:1709) is a logo, not a control or status. Dividers (#D8D8DD, #E8E8EC, #B8B8B8, #DDDDDD) only separate areas and do not carry meaning. The hidden texts at opacity 0 are not visible.

## 4. Copy

Strings are exact, including the trailing spaces and the double space that Figma has. Max length is based on the width of the text box in Figma and Inter at that size. Where the box hugs its text (no fixed width), the max length is NOT IN DESIGN.

| Location | String (exact) | Max length |
|---|---|---|
| Search placeholder (6750:1739) | Search | NOT IN DESIGN: the box hugs the text; what is the max query length? |
| List header (6750:1746) | Subject | NOT IN DESIGN: fixed label, hugs text |
| List header (6750:1753) | Response | NOT IN DESIGN: fixed label, hugs text |
| List header (6750:1761) | Delivery | NOT IN DESIGN: fixed label, hugs text |
| Row 1 title (6750:1778) | Contractor agreement review | 405.5 px wide, wraps (row 6 shows 2 lines). NOT IN DESIGN: max number of lines, and truncate or wrap after that? |
| Row 1 customer (6750:1779) | Kestrel Apparel Co. | NOT IN DESIGN: one line, no wrap set (nowrap); what happens when a customer name is longer than 405 px? |
| Row 1 Response clock (6750:1782) | 47m overdue | 216.75 px wide column. NOT IN DESIGN: wrap or truncate? |
| Row 1 Response person (6750:1783) | Dylan Moore | NOT IN DESIGN: nowrap; max width is the 216.75 px column |
| Row 1 Delivery reason (6750:1785) | Delivery promise missed | 216.75 px wide column. NOT IN DESIGN: wrap or truncate? |
| Row 1 Delivery person (6750:1786) | Mara Ellis  (with a trailing space in Figma) | NOT IN DESIGN: nowrap; max width is the 216.75 px column |
| Row 2 title (6750:1799) | Intake packet readiness | 407 px wide, wraps |
| Row 2 customer (6750:1800) | Northstar Health Partners | NOT IN DESIGN: nowrap |
| Row 2 Response clock (6750:1803) | 1h 5m overdue | 215.5 px column |
| Row 2 Response person (6750:1804) | Camille Ross | NOT IN DESIGN: nowrap |
| Row 2 Delivery text, opacity 0 (6750:1805) | Delivery promise missed | Hidden (opacity 0). NOT IN DESIGN: should this render? |
| Row 3 title (6750:1818) | Data-processing addendum | 407 px wide, wraps |
| Row 3 customer (6750:1819) | Northstar Health Partners | NOT IN DESIGN: nowrap |
| Row 3 Response text, opacity 0 (6750:1821) | 1h 5m overdue / 3h | Hidden (opacity 0). "/ 3h" part is #A1A1A1. NOT IN DESIGN: should this render? |
| Row 3 Delivery reason (6750:1823) | Client asked again | 215.5 px column |
| Row 3 Delivery person (6750:1824) | Camille Ross | NOT IN DESIGN: nowrap |
| Row 4 title (6750:1838) | Invoice account number | 407 px wide, wraps |
| Row 4 customer (6750:1839) | Ridgeway Foods | NOT IN DESIGN: nowrap |
| Row 4 Response clock (6750:1842) | 17m until target | 215.5 px column |
| Row 4 Response person (6750:1843) | Julian Reyes | NOT IN DESIGN: nowrap |
| Row 4 Delivery text, opacity 0 (6750:1844) | Delivery promise missed | Hidden (opacity 0). NOT IN DESIGN: should this render? |
| Row 5 title (6750:1860) | Contractor agreement review | 405.5 px wide, wraps |
| Row 5 customer (6750:1861) | Kestrel Apparel Co. | NOT IN DESIGN: nowrap |
| Row 5 Response clock (6750:1864) | 32m until  target  (two spaces between "until" and "target" in Figma) | 216.75 px column. NOT IN DESIGN: is the double space a typo? |
| Row 5 Response person (6750:1865) | Ava Chen | NOT IN DESIGN: nowrap |
| Row 5 Delivery block, opacity 0 (6750:1867, 1868) | Delivery promise missed / Mara Ellis  | Hidden (opacity 0). NOT IN DESIGN: should this render? |
| Row 6 title (6750:1881) | ADP access issue payroll lead still locked out | 379 px used of 403 px (24 px right padding), 2 lines shown |
| Row 6 customer (6750:1882) | Ironwood Logistics | NOT IN DESIGN: nowrap |
| Row 6 Response reason (6750:1885) | Client dissatisfaction | 215.5 px column |
| Row 6 Response person (6750:1886) | Teresa Lang | NOT IN DESIGN: nowrap |
| Row 6 Delivery block, opacity 0 (6750:1888, 1889) | Client asked again / Camille Ross | Hidden (opacity 0). NOT IN DESIGN: should this render? |
| Footer count (6750:1892) | 6 items | NOT IN DESIGN: hugs text; what is the singular form ("1 item")? |
| Footer label (6750:1894) | Last checked | NOT IN DESIGN: fixed label, hugs text |
| Footer Gmail time (6750:1903) | Friday 12:00 PM | NOT IN DESIGN: date format rule (day name only, or a date after one week?) |
| Footer Slack time (6750:1915) | Friday 11:58 AM | NOT IN DESIGN: same date format question |
| Detail header title (6750:1931) | Contractor agreement review | NOT IN DESIGN: nowrap; it shares 875.5 px with the customer name. Truncate? |
| Detail header customer (6750:1932) | Kestrel Apparel Co. | NOT IN DESIGN: nowrap |
| Response panel title (6750:1943) | Response | NOT IN DESIGN: fixed label |
| Response panel clock (6750:1944) | 47m overdue | NOT IN DESIGN: nowrap, right aligned |
| Response label (6750:1949) | What QTalo found | 412.5 px |
| Response finding (6750:1950) | Client request has no visible acknowledgement in this Slack thread before the 3-hour response window expired. | 412.5 px wide, 4 lines in a 96 px box (20 px bold). NOT IN DESIGN: max lines? |
| Response label (6750:1954) | Who's waiting | 110 px label column |
| Response value (6750:1955) | Dylan Moore at Kestrel Apparel Co. | NOT IN DESIGN: nowrap; 286.5 px left after the label. Wrap or truncate? |
| Response label (6750:2215) | Original ask  (with a trailing space in Figma) | 110 px label column |
| Response value (6750:2216) | Heads up team, we've got a new contractor starting next week and will need the standard agreement reviewed before then. | 286.5 px wide, 4 lines in a 76 px box. NOT IN DESIGN: max lines? |
| Response label (6750:1977) | Next decision | 110 px label column |
| Response next decision (6750:1979) | Confirm who should acknowledge the contractor agreement request. | 412.5 px wide, 2 lines |
| Button (6750:1985) | Response sent | NOT IN DESIGN: button hugs text |
| Button (6750:1990) | No response needed | NOT IN DESIGN: button hugs text |
| Evidence label (6750:1997) | Evidence in | NOT IN DESIGN: fixed label |
| Evidence channel (6750:1998) | #client-kestrel | NOT IN DESIGN: nowrap; max channel name length? |
| Date pill (6750:2008, 2164) | Monday | NOT IN DESIGN: pill hugs text |
| Date pill (6750:2042) | Tuesday | NOT IN DESIGN: pill hugs text |
| Date pill (6750:2066) | Today | NOT IN DESIGN: pill hugs text |
| Thread name (6750:2016, 2036, 2060, 2074, 2086, 2172) | Dylan Moore | NOT IN DESIGN: nowrap |
| Thread name (6750:2026, 2050, 2184) | Mara Ellis | NOT IN DESIGN: nowrap |
| Thread time (6750:2017) | 9:12 AM | NOT IN DESIGN: hugs text |
| Thread time (6750:2027) | 9:40 AM | NOT IN DESIGN: hugs text |
| Thread time (6750:2037) | 2:15 PM | NOT IN DESIGN: hugs text |
| Thread time (6750:2051) | 10:05 AM | NOT IN DESIGN: hugs text |
| Thread time (6750:2061) | 4:30 PM | NOT IN DESIGN: hugs text |
| Thread time (6750:2075) | 10:58 AM | NOT IN DESIGN: hugs text |
| Thread time (6750:2087) | 11:36 AM | NOT IN DESIGN: hugs text |
| Thread time, Delivery (6750:2173) | Mon 9:04 AM | NOT IN DESIGN: hugs text |
| Thread time, Delivery (6750:2185) | Mon, 9:18 AM | NOT IN DESIGN: hugs text; note the comma differs from "Mon 9:04 AM" |
| Thread tag (6750:2019) | • Original ask | NOT IN DESIGN: hugs text |
| Thread tag (6750:2029, 2053) | • Team acknowledge | NOT IN DESIGN: hugs text |
| Thread tag with reply icon (6750:2092) | Response | NOT IN DESIGN: hugs text |
| Thread tag with timer icon (6750:2190) | Promise made | NOT IN DESIGN: hugs text |
| Thread avatar letters (6750:2013, 2033, 2057, 2071, 2082, 2169) | D | 1 character |
| Thread avatar letters (6750:2023, 2047, 2180) | M | 1 character |
| Thread body (6750:2020) | Heads up team, we've got a new contractor starting next week and will need the standard agreement reviewed before then. | 368 px wide, wraps. NOT IN DESIGN: max lines, or show the full message? |
| Thread body (6750:2030) | Thanks for the heads up, Dylan — send over the contractor specifics whenever you have them and we'll get the template pulled together. | 368 px wide, wraps |
| Thread body (6750:2038) | Sending the contractor details over now — let me know if anything else is needed on our end. | 368 px wide, wraps |
| Thread body (6750:2054) | Got it, thanks. Reviewing the NDA language against our standard clauses today. | 368 px wide, wraps |
| Thread body (6750:2062) | Any update on this? We'd like to get it locked before the work trial starts. | 368 px wide, wraps |
| Thread body (6750:2076) | Can someone review the contractor agreement before noon? We have the work trial starting tomorrow and need the NDA language confirmed today. | 368 px wide, wraps |
| Thread body (6750:2093) | Just checking this landed. We are blocked on sending the invite until we hear back. | 368 px wide, wraps |
| Delivery panel title (6750:2103) | Delivery | NOT IN DESIGN: fixed label |
| Delivery panel reason (6750:2104) | Delivery promise missed | NOT IN DESIGN: nowrap, right aligned |
| Delivery label (6750:2109) | What QTalo found | 412.5 px |
| Delivery finding (6750:2110) | Due Wednesday · no delivery or updated ETA found | 412.5 px wide, 2 lines (20 px bold) |
| Delivery label (6750:2114) | Owed by | 110 px label column |
| Delivery value (6750:2115) | Mara Ellis | NOT IN DESIGN: nowrap |
| Delivery label (6750:2219) | Promise made  (with a trailing space in Figma) | 110 px label column |
| Delivery value (6750:2220) | Final redlines by Wednesday 5:00 PM | 286.5 px wide, wraps |
| Delivery label (6750:2133) | Next decision | 110 px label column |
| Delivery next decision (6750:2135) | Check status and update the client if delivery is not imminent. | 412.5 px wide, 2 lines |
| Button (6750:2141) | Mark completed | NOT IN DESIGN: button hugs text |
| Button (6750:2143) | Correct | NOT IN DESIGN: button hugs text |
| Evidence label (6750:2153) | Evidence in | NOT IN DESIGN: fixed label |
| Evidence channel (6750:2154) | #client-kestrel | NOT IN DESIGN: nowrap |
| Delivery thread body (6750:2174) | Can you send final redlines this week? We need the agreement before the contractor starts. | 368 px wide, wraps |
| Delivery thread body (6750:2191) | Received. We will send final redlines by Wednesday at 5:00 PM. | 368 px wide, wraps |

## 5. Behavior

### Interactions

What the frame shows:

- The queue lists 6 items. Row 1 is selected (white fill, 5 px #FF4800 left border) and its detail is open on the right.
- Each row shows a Response part (clock or reason + person) and a Delivery part (reason + person). Some rows have no visible Delivery or Response part (the layer is there at opacity 0).
- The list header has a down arrow next to "Response" (6750:1754). NOT IN DESIGN: does it sort by Response urgency, and can the user change the direction?
- The detail panel has two columns side by side: Response (left) and Delivery (right). Each column has: title with clock or reason, "What QTalo found", one key field (Who's waiting / Owed by), the source line (Original ask / Promise made), "Next decision" with action buttons, and an "Evidence in #client-kestrel" bar with the Slack thread under it.
- In the thread, older messages are at 60% opacity. The last message is at 100% and has a tag: "Response" (reply icon, #FF4800) in the Response column, "Promise made" (timer icon, #B27E08) in the Delivery column.
- NOT IN DESIGN: what happens when the user clicks a row (select only, or also mark as read)?
- NOT IN DESIGN: what do "Response sent" and "No response needed" do (remove the item, change the clock, show a confirmation)? Is there an undo?
- NOT IN DESIGN: what does "Mark completed" do, and what options are in the "Correct" menu?
- NOT IN DESIGN: what does the arrow on "Evidence in #client-kestrel" do (collapse the thread, or open the thread in Slack)?
- NOT IN DESIGN: does clicking the channel name or a message open it in Slack?
- NOT IN DESIGN: what does the search field search (titles, customers, people, message text)?

### Breakpoints

- Figma has one frame at 1920 x 1511. The queue column is a fixed 926 px and the detail panel takes the rest (921 px, `flex-1`).
- NOT IN DESIGN: what happens below 1920 px wide (for example 1440 or 1280)? Do the Response and Delivery columns stack?
- NOT IN DESIGN: is there a tablet or mobile layout?

### Edge cases

- Long row title: wraps to 2 lines (row 6, 121 px high row). NOT IN DESIGN: what after 2 lines?
- Long thread: the thread area scrolls in y (`overflow-y-auto`), and content is pinned to the bottom (`justify-end`). In the Delivery column the content starts low (at y 609 of 834), so there is empty space at the top.
- Row with no Delivery or no Response: Figma keeps the text at opacity 0 (6750:1805, 1821, 1844, 1866, 1887). The developer should know this is a hidden layer, not real data. NOT IN DESIGN: should the empty half show a dash, nothing, or a label?
- Rows 1 and 5 both have the title "Contractor agreement review" for "Kestrel Apparel Co." with different people (Dylan Moore / Ava Chen) and clocks (47m overdue / 32m until target). NOT IN DESIGN: are these two different items, and how does the user tell them apart?
- "until target" (rows 4 and 5) uses the same #FF4800 as "overdue". NOT IN DESIGN: should an item that is not yet overdue use a different color?
- Row titles in rows 1 to 3 are Semi Bold; rows 4 to 6 are Regular. NOT IN DESIGN: does the weight mean unread or something else?
- The rail divider (6750:1733) is only 1080 px tall while the frame is 1511 px. NOT IN DESIGN: should it run the full height?
- "Owed by" (6750:2114) is Regular while the other field labels are Semi Bold. NOT IN DESIGN: is this on purpose?
- Thread times use two formats: "Mon 9:04 AM" and "Mon, 9:18 AM", and Response-thread times have no day. NOT IN DESIGN: which date format is correct?
- NOT IN DESIGN: what happens to the detail panel when no row is selected?

## 6. Accessibility

Summary from the accessibility-reviewer subagent (full review in `accessibility-review.md`): **FAIL, 28 fails, 3 cannot verify, 9 pass** (40 grouped rows).

- Contrast: 25 text uses and 2 icons fail (12 grouped rows). Groups: #FF4800 text, #B27E08 text, light grays (#999999, #BFBFBF, #848484, #808080, #898989, #8B8B8B, #7B7B7B, #A3A3A3), and the 60% opacity on older thread messages.
- Target size: buttons, rows, evidence bar and sort arrow pass (24 x 24 or more). Hidden controls cannot be verified.
- Focus: every control has no focus style (NOT IN DESIGN), and the spec has no focus order. Suggested order: search, sort, rows, Response buttons, Response evidence, Delivery buttons, Delivery evidence.
- Labels: search field and sort arrow have no accessible name; Slack, Gmail and QTalo logos have no alt text; icons next to text and avatar letters are not marked decorative; the evidence arrow has no expanded state.
- Color alone: the selected row is shown only by the #FF4800 left border; add a second cue and `aria-current`.
- This automated review supports a manual check; it does not replace it.

## 7. Open questions

All `NOT IN DESIGN:` items above are open questions for the designer. The main ones:

1. All states except Default are missing for every control (hover, focus, disabled, loading, empty, error).
2. No Figma variables: all colors, spacing and type need tokens.
3. 25 text uses and 2 icons fail AA contrast (see the Contrast table), mainly #FF4800 and #B27E08 text, #999999 labels, #848484 footer text and all 60% thread text.
4. What the buttons "Response sent", "No response needed", "Mark completed" and "Correct" do.
5. Hidden opacity-0 texts in rows 2 to 6: render or not?
6. Breakpoints below 1920 px.
