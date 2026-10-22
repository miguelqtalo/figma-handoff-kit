# Handoff: Kestrel Case (Only Response)

## 1. Source

- Figma link: https://www.figma.com/design/KXDasTBnxU4SVR68K44kiV/MVP-3.0-Wireframes?node-id=6750-2222
- Frame name and node id: "Kestrel Case (Only Response)", 6750:2222
- Frame size: 1920 x 1080 px (inner content frame 6750:2223 is 1917 x 1080; the top frame has 3 px right padding)
- Date: 2026-10-22 (read from Figma on this date)
- Components in use: one component instance only: "Brand Icon" (6750:2500, Slack logo inside). Everything else is plain frames, text and vectors (Material-style icons named reply, timer, arrow_downward_alt, keyboard_arrow_down, check, search; Slack and Gmail logos as "Icon svg").
- Known constraints: the frame has no Figma variables (`get_variable_defs` returned `{}`), so every value below is a raw value marked "needs a token". Page background read from the root line of the frame's design context: `bg-white` = #FFFFFF (6750:2222). Reference image: `figma-reference.png` in this folder.

Layout (from `get_metadata`):

| Area | Node | Size | Notes |
|---|---|---|---|
| Left rail | 6750:2224 | 70 x 1080 | Fill #FBFBFC. QTalo logo 32 x 32 at top. "Filters" group (Slack, Gmail) is hidden (6750:2228). |
| Rail divider | 6750:2250 | 1 x 1080 | Stroke #D8D8DD |
| Queue column | 6750:2251 | 926 x 1080 | Search bar (72 high), list header (48 high), 6 rows, footer (72 high, pinned to the bottom by justify-between). |
| Column divider | 6750:2437 | 1 x 1080 | Stroke #B8B8B8 |
| Detail panel | 6750:2438 | 921 x 1080 | Header (72 high), then two columns of 460.5: Situation (6750:2456) and Evidence (6750:2496), split by a 1 px line #D8D8DD (6750:2495). |

## 2. States

Figma shows one static state of the screen: row 1 ("Contractor agreement review", Kestrel Apparel Co.) is selected and its detail is open. This frame is the "Only Response" variant: most Delivery cells in the queue are at opacity 0 (see Edge cases).

| Element | Default | Hover | Focus | Disabled | Loading | Empty | Error |
|---|---|---|---|---|---|---|---|
| Search field (6750:2252) | Search icon 24 px #BFBFBF + placeholder "Search" 16 px Inter Regular #BFBFBF, no border, no fill, padding 24 px, gap 8 px | NOT IN DESIGN: is there a hover style? | NOT IN DESIGN: what does the focus ring look like, and does the placeholder change? | NOT IN DESIGN: can search be disabled? | NOT IN DESIGN: loading state while results come in? | NOT IN DESIGN: what does the list show when no item matches? | NOT IN DESIGN: what shows if search fails? |
| Response column header with sort arrow (6750:2269) | reply icon 24 px #FF4800 + "Response" 14 px Medium #222222 + arrow_downward_alt 24 px #A3A3A3 | NOT IN DESIGN: hover style? | NOT IN DESIGN: focus style? | NOT IN DESIGN: is the sort ever disabled? | NOT IN DESIGN | NOT IN DESIGN: is the arrow shown when the list is empty? | NOT IN DESIGN |
| Delivery column header (6750:2278) | timer icon 24 px #B27E08 + "Delivery" 14 px Medium #222222, no sort arrow | NOT IN DESIGN: is it clickable (sort by Delivery)? | NOT IN DESIGN | NOT IN DESIGN | NOT IN DESIGN | NOT IN DESIGN | NOT IN DESIGN |
| Queue row, selected (6750:2285) | Fill #FFFFFF, left border 5 px #FF4800, padding 24 px top/bottom, 19 px left/right, bottom line 1 px #D8D8DD | NOT IN DESIGN: hover style of a selected row? | NOT IN DESIGN: focus style of a row? | NOT IN DESIGN | NOT IN DESIGN | Not applicable (a row always has data) | NOT IN DESIGN: what shows if the item cannot load? |
| Queue row, not selected (6750:2328, 2348, 2391) | No fill (page #FFFFFF shows through), no left border, padding 24 px | NOT IN DESIGN: hover style? | NOT IN DESIGN: focus style? | NOT IN DESIGN | NOT IN DESIGN | Not applicable | NOT IN DESIGN |
| Queue rows 2 and 5 (6750:2309, 6750:2367) | Left border 5 px #FFFFFF (white on white), padding left 19 px. Row 5 also has fill #FFFFFF; row 2 has none. They look like not-selected rows. | NOT IN DESIGN: is the white border a leftover, or a different state (for example "read")? | NOT IN DESIGN | NOT IN DESIGN | NOT IN DESIGN | Not applicable | NOT IN DESIGN |
| Row title weight (6750:2299, 2320, 2339 Semi Bold; 6750:2359, 2381, 2402 Regular) | Rows 1 to 3 titles are Inter Semi Bold 20 px; rows 4 to 6 are Inter Regular 20 px | NOT IN DESIGN | NOT IN DESIGN | NOT IN DESIGN | NOT IN DESIGN | NOT IN DESIGN | NOT IN DESIGN: does the weight mean a state (for example unread vs read, or the two groups 6750:2284 and 6750:2347)? |
| Queue list (6750:2284, 6750:2347) | 6 rows in two groups (3 + 3), footer "7 items" | Not applicable | Not applicable | Not applicable | NOT IN DESIGN: what shows while the queue loads? | NOT IN DESIGN: what shows when there are 0 items? | NOT IN DESIGN: what shows if the queue fails to load? |
| "Response sent" button (6750:2608) | 120 x 30, border 1 px #000000, radius 4 px, padding 6 px, gap 4 px, check icon 16 px #1C1B1F + label 12 px Semi Bold #222222 | NOT IN DESIGN: hover style? | NOT IN DESIGN: focus style? | NOT IN DESIGN: is it disabled after use? | NOT IN DESIGN: loading state after click? | Not applicable | NOT IN DESIGN: what shows if the action fails? |
| "No response needed" button (6750:2613) | 134 x 29, border 1 px #000000, radius 4 px, padding 6 px, label 12 px Semi Bold #222222. It has a hidden check icon (6750:2614). | NOT IN DESIGN: hover style? | NOT IN DESIGN: focus style? | NOT IN DESIGN: disabled style? | NOT IN DESIGN: loading style? | Not applicable | NOT IN DESIGN: error after click? |
| Response reason header (6750:2458) | reply icon 24 px #FF4800 + "Response" 16 px Semi Bold #FF4800 + "47m overdue" 16 px Medium #FF4800. Expand arrow keyboard_arrow_down (6750:2466) is hidden. | NOT IN DESIGN: is the header clickable when the arrow is visible? | NOT IN DESIGN | NOT IN DESIGN | NOT IN DESIGN | NOT IN DESIGN | NOT IN DESIGN |
| "Evidence in #client-kestrel" bar (6750:2498) | 462 x 48, Slack Brand Icon 24 px + "Evidence in" 14 px Semi Bold #999999 + "#client-kestrel" 16 px Semi Bold #222222. Expand arrow keyboard_arrow_down (6750:2503) is hidden. | NOT IN DESIGN: is the bar clickable (open in Slack, or expand)? | NOT IN DESIGN: focus style? | NOT IN DESIGN | NOT IN DESIGN | NOT IN DESIGN: what shows if there is no evidence thread? | NOT IN DESIGN: what shows if the source cannot load? |
| Evidence thread (6750:2508) | Scrolls in y (Figma: overflow-y auto, overflow-x clip), content sits at the bottom (justify end). Older messages and the Monday and Tuesday date rows at 60% opacity; the "Today" date row and the latest message (11:36 AM) at 100%. | Not applicable | NOT IN DESIGN: can the thread get keyboard focus to scroll? | Not applicable | NOT IN DESIGN: loading state of the thread? | NOT IN DESIGN: empty thread? | NOT IN DESIGN: error state of the thread? |
| Left rail filters (6750:2228, hidden) | Hidden in this frame: Slack and Gmail filter tiles 48 x 48 with labels 'Slack' and 'Gmail' | NOT IN DESIGN | NOT IN DESIGN | NOT IN DESIGN | NOT IN DESIGN | NOT IN DESIGN | NOT IN DESIGN: should the developer build the hidden filters at all? |

## 3. Tokens

The frame has no Figma variables. Every value below is a raw value from `get_design_context` and **needs a token**.

### Color

| Use | Token | Value |
|---|---|---|
| Page and detail background (6750:2222) | needs a token | #FFFFFF |
| Left rail fill (6750:2224) | needs a token | #FBFBFC |
| List header row fill (6750:2264) | needs a token | #FDFDFD |
| Primary text (titles, header labels, values, buttons, date pills) | needs a token | #222222 |
| Row customer name (6750:2300 and others) | needs a token | #666666 |
| Responsible person name in rows (6750:2304 and others) | needs a token | #7B7B7B |
| Response / urgency color: clocks, reason text, reply icon, selected row bar | needs a token | #FF4800 |
| Delivery color: "Client asked again", timer icon | needs a token | #B27E08 |
| Hidden secondary part of clock "/ 3h" (6750:2342, opacity 0) | needs a token | #A1A1A1 |
| Search placeholder and search icon | needs a token | #BFBFBF |
| Sort arrow (6750:2275) | needs a token | #A3A3A3 |
| Footer "7 items" (6750:2413) | needs a token | #686868 |
| Footer "Last checked" and times (6750:2415, 2424, 2436) | needs a token | #848484 |
| Detail header customer (6750:2453) | needs a token | #808080 |
| Section labels "What QTalo found", "Who's waiting", "Original ask", "Next decision", "Evidence in" | needs a token | #999999 |
| Message time (6750:2521 and others) | needs a token | #898989 |
| Message body (6750:2522 and others) | needs a token | #8B8B8B |
| Avatar fill (6750:2516 and others) | needs a token | #A8A8A8 |
| Avatar letter | needs a token | #FFFFFF |
| Button border (6750:2608, 2613) | needs a token | #000000 |
| Check icon (6750:2609) | needs a token | #1C1B1F |
| Date pill border (6750:2511, 2541, 2563) | needs a token | #DDDDDD |
| Date row lines (Line 21, 22, 23) | needs a token | #DDDDDD |
| Dividers: rail, queue lines, detail header line, Situation/Evidence split | needs a token | #D8D8DD |
| Queue / detail column divider (6750:2437) | needs a token | #B8B8B8 |
| Detail section dividers and evidence bar line (Divider, 6750:2506) | needs a token | #E8E8EC |
| QTalo logo (6750:2226) | needs a token | #6663FF |
| Slack logo colors (brand, keep as is) | NOT IN DESIGN: brand asset, tokenize or not? | #2EB67D, #36C5F0, #E01E5A, #ECB22E |
| Gmail logo colors (brand, keep as is) | NOT IN DESIGN: brand asset, tokenize or not? | #34A853, #4285F4, #C5221F, #EA4335, #FBBC04 |
| Extra fill inside Material icon SVGs (search, sort arrow, timer, check) | NOT IN DESIGN: probably the icon mask layer, confirm it is not visible | #D9D9D9 |

### Spacing and size

| Use | Token | Value |
|---|---|---|
| Left rail width | needs a token | 70 px |
| Left rail logo area height | needs a token | 72 px |
| Queue column width | needs a token | 926 px |
| Detail panel width | needs a token | 921 px (two columns of 460.5 px) |
| Search bar padding / gap | needs a token | 24 px / 8 px |
| List header padding | needs a token | 24 px left/right, 12 px top/bottom; height 48 px |
| List header gaps (Response group / header icon to label) | needs a token | 6 px / 8 px |
| Queue row padding | needs a token | 24 px (rows with a 5 px left border: 19 px left) |
| Selected row left border | needs a token | 5 px |
| Row icon box / gap to text | needs a token | 24 x 24 px, padding-top 2 px / 12 px |
| Row title to customer gap | needs a token | 4 px |
| Row right half gap (between Response and Delivery cells) | needs a token | 8 px |
| Footer padding / gap between footer items / icon to text | needs a token | 24 px / 16 px / 4 px |
| Detail header padding / gap / icon box | needs a token | 24 px left/right, 12 px top/bottom / 8 px / 48 x 48 px |
| Detail header title to customer gap | needs a token | 16 px |
| Situation column padding bottom | needs a token | 16 px |
| Response reason header padding / gap | needs a token | 16 px top, 12 px bottom, 24 px left/right / 13 px (icon group to clock), 8 px (icon to label) |
| "What QTalo found" block padding / gap | needs a token | 8 px top, 20 px bottom, 24 px left/right / 16 px |
| Label rows ("Who's waiting", "Original ask") padding / gap / label width | needs a token | 20 px top/bottom, 24 px left/right / 16 px / 110 px |
| "Next decision" block padding / gaps | needs a token | 20 px / 24 px, gap 16 px; buttons gap 12 px |
| Button padding / radius / border | needs a token | 6 px / 4 px / 1 px |
| Evidence bar padding / gap / height | needs a token | 24 px left/right, 12 px top/bottom / 8 px / 48 px |
| Evidence thread side padding | needs a token | 24 px |
| Date row padding / pill padding / pill radius | needs a token | 6 px top/bottom / 12 px left/right, 6 px top/bottom / 38 px |
| Message row padding / gap | needs a token | 8 px top/bottom (latest message 16 px) / 12 px |
| Avatar size / padding / radius | needs a token | 32 x 32 px / 10 px / 6 px |
| Message header gap / name to body gap | needs a token | 8 px / 8 px |
| "Response" tag in latest message: icon / gap | needs a token | 16 px / 6 px |
| Icon sizes | needs a token | 24 px (search, reply, timer, sort arrow, keyboard_arrow_down), 16 px (check, small reply, Slack logo in rows), 26 px (Slack logo in detail header), 32 px (QTalo logo) |
| Divider stroke | needs a token | 1 px |

### Type

All text is Inter, line height `normal`.

| Use | Token | Family, size, weight, line height |
|---|---|---|
| Detail title (6750:2452), finding sentence (6750:2471) | needs a token | Inter, 20 px, Bold 700, normal |
| Row title, rows 1 to 3 | needs a token | Inter, 20 px, Semi Bold 600, normal |
| Row title, rows 4 to 6 | needs a token | Inter, 20 px, Regular 400, normal |
| Row customer, search placeholder, message body | needs a token | Inter, 16 px, Regular 400, normal |
| Row clocks, reasons and person names; "Who's waiting" and "Original ask" values; reason clock "47m overdue" | needs a token | Inter, 16 px, Medium 500, normal |
| Reason label "Response" (6750:2464), next decision sentence, "#client-kestrel", avatar letter | needs a token | Inter, 16 px, Semi Bold 600, normal |
| Message sender name | needs a token | Inter, 16 px, Bold 700, normal |
| List header labels "Response", "Delivery"; message time | needs a token | Inter, 14 px, Medium 500, normal |
| List header "Subject", footer texts | needs a token | Inter, 14 px, Regular 400, normal |
| Section labels, detail customer, "Response" tag in latest message | needs a token | Inter, 14 px, Semi Bold 600, normal |
| Buttons, date pills | needs a token | Inter, 12 px, Semi Bold 600, normal |

### Contrast (from scripts/contrast.py)

One row per text use. Backgrounds: page #FFFFFF, list header #FDFDFD, left rail #FBFBFC. Semi Bold 600 is not "bold" for WCAG, so 20 px Semi Bold needs 4.5:1.

| Use | Color | Background | Size | Ratio | Needs | Result |
|---|---|---|---|---|---|---|
| Search placeholder "Search" (6750:2256) | #BFBFBF | #FFFFFF | 16px | 1.84:1 | 4.5:1 | FAIL |
| Column header "Subject" (6750:2267) | #222222 | #FDFDFD | 14px | 15.64:1 | 4.5:1 | pass |
| Column header "Response" (6750:2274) | #222222 | #FDFDFD | 14px | 15.64:1 | 4.5:1 | pass |
| Column header "Delivery" (6750:2282) | #222222 | #FDFDFD | 14px | 15.64:1 | 4.5:1 | pass |
| Row title, semibold (6750:2299, 2320, 2339) | #222222 | #FFFFFF | 20px | 15.91:1 | 4.5:1 | pass |
| Row title, regular (6750:2359, 2381, 2402) | #222222 | #FFFFFF | 20px | 15.91:1 | 4.5:1 | pass |
| Row customer name (6750:2300, 2321, 2340, 2360, 2382, 2403) | #666666 | #FFFFFF | 16px | 5.74:1 | 4.5:1 | pass |
| Response clock or reason (6750:2303, 2324, 2363, 2385, 2406) | #FF4800 | #FFFFFF | 16px | 3.40:1 | 4.5:1 | FAIL |
| Responsible person (6750:2304, 2325, 2364, 2386, 2407) | #7B7B7B | #FFFFFF | 16px | 4.23:1 | 4.5:1 | FAIL |
| Delivery reason "Client asked again", visible (6750:2344) | #B27E08 | #FFFFFF | 16px | 3.57:1 | 4.5:1 | FAIL |
| Delivery person "Camille Ross", visible (6750:2345) | #7B7B7B | #FFFFFF | 16px | 4.23:1 | 4.5:1 | FAIL |
| Footer "7 items" (6750:2413) | #686868 | #FFFFFF | 14px | 5.57:1 | 4.5:1 | pass |
| Footer "Last checked" (6750:2415) | #848484 | #FFFFFF | 14px | 3.74:1 | 4.5:1 | FAIL |
| Footer times (6750:2424, 2436) | #848484 | #FFFFFF | 14px | 3.74:1 | 4.5:1 | FAIL |
| Detail title (6750:2452) | #222222 | #FFFFFF | 20px bold | 15.91:1 | 3:1 | pass |
| Detail customer (6750:2453) | #808080 | #FFFFFF | 14px | 3.95:1 | 4.5:1 | FAIL |
| Reason label "Response" (6750:2464) | #FF4800 | #FFFFFF | 16px | 3.40:1 | 4.5:1 | FAIL |
| Reason clock "47m overdue" (6750:2465) | #FF4800 | #FFFFFF | 16px | 3.40:1 | 4.5:1 | FAIL |
| Section label "What QTalo found" (6750:2470) | #999999 | #FFFFFF | 14px | 2.85:1 | 4.5:1 | FAIL |
| Finding sentence (6750:2471) | #222222 | #FFFFFF | 20px bold | 15.91:1 | 3:1 | pass |
| Section label "Who's waiting" (6750:2475) | #999999 | #FFFFFF | 14px | 2.85:1 | 4.5:1 | FAIL |
| Who's waiting value (6750:2476) | #222222 | #FFFFFF | 16px | 15.91:1 | 4.5:1 | pass |
| Section label "Original ask" (6750:2480) | #999999 | #FFFFFF | 14px | 2.85:1 | 4.5:1 | FAIL |
| Original ask value (6750:2481) | #222222 | #FFFFFF | 16px | 15.91:1 | 4.5:1 | pass |
| Section label "Next decision" (6750:2604) | #999999 | #FFFFFF | 14px | 2.85:1 | 4.5:1 | FAIL |
| Next decision sentence (6750:2606) | #222222 | #FFFFFF | 16px | 15.91:1 | 4.5:1 | pass |
| Button "Response sent" (6750:2612) | #222222 | #FFFFFF | 12px | 15.91:1 | 4.5:1 | pass |
| Button "No response needed" (6750:2617) | #222222 | #FFFFFF | 12px | 15.91:1 | 4.5:1 | pass |
| Evidence label "Evidence in" (6750:2501) | #999999 | #FFFFFF | 14px | 2.85:1 | 4.5:1 | FAIL |
| Evidence channel "#client-kestrel" (6750:2502) | #222222 | #FFFFFF | 16px | 15.91:1 | 4.5:1 | pass |
| Date pill "Monday", group 60% (6750:2512) | #222222 at 60% = #7A7A7A | #FFFFFF | 12px | 4.29:1 | 4.5:1 | FAIL |
| Date pill "Tuesday", group 60% (6750:2542) | #222222 at 60% = #7A7A7A | #FFFFFF | 12px | 4.29:1 | 4.5:1 | FAIL |
| Date pill "Today", no opacity (6750:2564) | #222222 | #FFFFFF | 12px | 15.91:1 | 4.5:1 | pass |
| Avatar letter, 60% groups (6750:2517, 2525, 2533, 2547, 2555, 2569) | #FFFFFF at 60% = #FFFFFF | #A8A8A8 at 60% on #FFFFFF = #CBCBCB | 16px | 1.62:1 | 4.5:1 | FAIL |
| Avatar letter, last message (6750:2580) | #FFFFFF | #A8A8A8 | 16px | 2.38:1 | 4.5:1 | FAIL |
| Sender name, 60% groups (6750:2520, 2528, 2536, 2550, 2558, 2572) | #222222 at 60% = #7A7A7A | #FFFFFF | 16px bold | 4.29:1 | 4.5:1 | FAIL |
| Message time, 60% groups (6750:2521, 2529, 2537, 2551, 2559, 2573) | #898989 at 60% = #B8B8B8 | #FFFFFF | 14px | 1.98:1 | 4.5:1 | FAIL |
| Message body, 60% groups (6750:2522, 2530, 2538, 2552, 2560, 2574) | #8B8B8B at 60% = #B9B9B9 | #FFFFFF | 16px | 1.96:1 | 4.5:1 | FAIL |
| Last message sender (6750:2584) | #222222 | #FFFFFF | 16px bold | 15.91:1 | 4.5:1 | pass |
| Last message time "11:36 AM" (6750:2585) | #898989 | #FFFFFF | 14px | 3.50:1 | 4.5:1 | FAIL |
| Last message tag "Response" (6750:2590) | #FF4800 | #FFFFFF | 14px | 3.40:1 | 4.5:1 | FAIL |
| Last message body (6750:2591) | #8B8B8B | #FFFFFF | 16px | 3.41:1 | 4.5:1 | FAIL |
| Selected row left bar (6750:2285 border-left) | #FF4800 | #FFFFFF | icon | 3.40:1 | 3:1 | pass |
| Search icon (6750:2253) | #BFBFBF | #FFFFFF | icon | 1.84:1 | 3:1 | FAIL |
| Reply icon, column header (6750:2271) | #FF4800 | #FDFDFD | icon | 3.34:1 | 3:1 | pass |
| Sort arrow (6750:2275) | #A3A3A3 | #FDFDFD | icon | 2.48:1 | 3:1 | FAIL |
| Timer icon, column header (6750:2279) | #B27E08 | #FDFDFD | icon | 3.51:1 | 3:1 | pass |
| Reply icon, detail (6750:2461) | #FF4800 | #FFFFFF | icon | 3.40:1 | 3:1 | pass |
| Reply icon, last message (6750:2587) | #FF4800 | #FFFFFF | icon | 3.40:1 | 3:1 | pass |
| Check icon in "Response sent" (6750:2609) | #1C1B1F | #FFFFFF | icon | 17.13:1 | 3:1 | pass |
| Button border (6750:2608, 2613) | #000000 | #FFFFFF | icon | 21.00:1 | 3:1 | pass |
| Slack logo, lowest color (6750:2289, 2371, 2427, 2442, 2500) | #ECB22E | #FFFFFF | icon | 1.91:1 | 3:1 | FAIL |
| Gmail logo, lowest color (6750:2313, 2332, 2352, 2395, 2418) | #FBBC04 | #FFFFFF | icon | 1.71:1 | 3:1 | FAIL |
| QTalo logo (6750:2226) | #6663FF | #FBFBFC | icon | 4.24:1 | 3:1 | pass |

Not checked: text at opacity 0 (hidden Delivery cells and the hidden clock in row 3). If these become visible, run the script again for them.

## 4. Copy

Strings are exact, including trailing spaces, double spaces and em dashes that Figma has. Max length is based on the width of the text box in Figma. Where the box hugs its text (no fixed width), the max length is NOT IN DESIGN.

| Location | String (exact) | Max length |
|---|---|---|
| Search placeholder (6750:2256) | Search | NOT IN DESIGN: box hugs the text; what is the max query length? |
| List header (6750:2267) | Subject | NOT IN DESIGN: fixed label, hugs text |
| List header (6750:2274) | Response | NOT IN DESIGN: fixed label, hugs text |
| List header (6750:2282) | Delivery | NOT IN DESIGN: fixed label, hugs text |
| Row 1 title (6750:2299) | Contractor agreement review | 405.5 px wide, wraps (row 6 shows 2 lines). NOT IN DESIGN: max number of lines, and truncate or wrap after that? |
| Row 1 customer (6750:2300) | Kestrel Apparel Co. | NOT IN DESIGN: nowrap; what happens when it is longer than 405 px? |
| Row 1 Response clock (6750:2303) | 47m overdue | 216.75 px column. NOT IN DESIGN: wrap or truncate? |
| Row 1 Response person (6750:2304) | Dylan Moore | NOT IN DESIGN: nowrap; max is the 216.75 px column |
| Row 1 Delivery reason, opacity 0 (6750:2306) | Delivery promise missed | 216.75 px column. NOT IN DESIGN: hidden in this frame; render or not? |
| Row 1 Delivery person, opacity 0 (6750:2307) | Mara Ellis  (trailing space) | NOT IN DESIGN: hidden; nowrap |
| Row 2 title (6750:2320) | Intake packet readiness | 407 px wide, wraps. NOT IN DESIGN: max lines? |
| Row 2 customer (6750:2321) | Northstar Health Partners | NOT IN DESIGN: nowrap; max 407 px |
| Row 2 Response clock (6750:2324) | 1h 5m overdue | 215.5 px column. NOT IN DESIGN: wrap or truncate? |
| Row 2 Response person (6750:2325) | Camille Ross | NOT IN DESIGN: nowrap; max 215.5 px |
| Row 2 Delivery reason, opacity 0 (6750:2326) | Delivery promise missed | 215.5 px. NOT IN DESIGN: hidden; render or not? |
| Row 3 title (6750:2339) | Data-processing addendum | 407 px wide, wraps. NOT IN DESIGN: max lines? |
| Row 3 customer (6750:2340) | Northstar Health Partners | NOT IN DESIGN: nowrap; max 407 px |
| Row 3 Response clock, opacity 0 (6750:2342) | 1h 5m overdue / 3h  (two spans: "1h 5m overdue " in #FF4800, "/ 3h" in #A1A1A1) | 215.5 px. NOT IN DESIGN: hidden; why is the Response cell hidden in an "Only Response" frame? |
| Row 3 Delivery reason, visible (6750:2344) | Client asked again | 215.5 px column. NOT IN DESIGN: wrap or truncate? |
| Row 3 Delivery person, visible (6750:2345) | Camille Ross | NOT IN DESIGN: nowrap; max 215.5 px |
| Row 4 title (6750:2359) | Invoice account number | 407 px wide, wraps. NOT IN DESIGN: max lines? |
| Row 4 customer (6750:2360) | Ridgeway Foods | NOT IN DESIGN: nowrap; max 407 px |
| Row 4 Response clock (6750:2363) | 17m until target | 215.5 px column. NOT IN DESIGN: wrap or truncate? |
| Row 4 Response person (6750:2364) | Julian Reyes | NOT IN DESIGN: nowrap; max 215.5 px |
| Row 4 Delivery reason, opacity 0 (6750:2365) | Delivery promise missed | 215.5 px. NOT IN DESIGN: hidden; render or not? |
| Row 5 title (6750:2381) | Contractor agreement review | 405.5 px wide, wraps. NOT IN DESIGN: max lines? |
| Row 5 customer (6750:2382) | Kestrel Apparel Co. | NOT IN DESIGN: nowrap; max 405.5 px |
| Row 5 Response clock (6750:2385) | 32m until  target  (two spaces between "until" and "target") | 216.75 px column. NOT IN DESIGN: is the double space a typo? |
| Row 5 Response person (6750:2386) | Ava Chen | NOT IN DESIGN: nowrap; max 216.75 px |
| Row 5 Delivery reason, opacity 0 (6750:2388) | Delivery promise missed | 216.75 px. NOT IN DESIGN: hidden; render or not? |
| Row 5 Delivery person, opacity 0 (6750:2389) | Mara Ellis  (trailing space) | NOT IN DESIGN: hidden; nowrap |
| Row 6 title (6750:2402) | ADP access issue payroll lead still locked out | 379 px text box (403 px frame minus 24 px right padding), 2 lines in Figma. NOT IN DESIGN: max lines? |
| Row 6 customer (6750:2403) | Ironwood Logistics | NOT IN DESIGN: nowrap; max 403 px |
| Row 6 Response reason (6750:2406) | Client dissatisfaction | 215.5 px column. NOT IN DESIGN: wrap or truncate? |
| Row 6 Response person (6750:2407) | Teresa Lang | NOT IN DESIGN: nowrap; max 215.5 px |
| Row 6 Delivery reason, opacity 0 (6750:2409) | Client asked again | 215.5 px. NOT IN DESIGN: hidden; render or not? |
| Row 6 Delivery person, opacity 0 (6750:2410) | Camille Ross | NOT IN DESIGN: hidden; nowrap |
| Footer count (6750:2413) | 7 items | NOT IN DESIGN: hugs text; also the list shows 6 rows, not 7 |
| Footer label (6750:2415) | Last checked | NOT IN DESIGN: fixed label, hugs text |
| Footer Gmail time (6750:2424) | Friday 12:00 PM | NOT IN DESIGN: hugs text; what date format for other days? |
| Footer Slack time (6750:2436) | Friday 11:58 AM | NOT IN DESIGN: hugs text; what date format for other days? |
| Detail title (6750:2452) | Contractor agreement review | NOT IN DESIGN: nowrap, frame 6750:2451 is 435 px with the customer name; what happens with a long title? |
| Detail customer (6750:2453) | Kestrel Apparel Co. | NOT IN DESIGN: nowrap, hugs text |
| Reason label (6750:2464) | Response | NOT IN DESIGN: fixed label, hugs text |
| Reason clock (6750:2465) | 47m overdue | NOT IN DESIGN: hugs text |
| Section label (6750:2470) | What QTalo found | 412.5 px wide, 1 line in Figma. NOT IN DESIGN: fixed label |
| Finding sentence (6750:2471) | Client request has no visible acknowledgement in this Slack thread before the 3-hour response window expired. | 412.5 px wide, 4 lines in Figma (96 px high). NOT IN DESIGN: max lines or characters? |
| Section label (6750:2475) | Who's waiting | 110 px label column |
| Who's waiting value (6750:2476) | Dylan Moore at Kestrel Apparel Co. | NOT IN DESIGN: nowrap; space left is about 286.5 px (460.5 minus 24, 110, 16, 24); wrap or truncate? |
| Section label (6750:2480) | Original ask  (trailing space) | 110 px label column |
| Original ask value (6750:2481) | Heads up team, we've got a new contractor starting next week and will need the standard agreement reviewed before then. | 286.5 px wide, 4 lines in Figma (76 px high). NOT IN DESIGN: max lines? Quote in full or truncate? |
| Section label (6750:2604) | Next decision | 110 px label column |
| Next decision sentence (6750:2606) | Confirm who should acknowledge the contractor agreement request. | 412.5 px wide, 2 lines in Figma. NOT IN DESIGN: max lines? |
| Button (6750:2612) | Response sent | NOT IN DESIGN: button hugs text |
| Button (6750:2617) | No response needed | NOT IN DESIGN: button hugs text |
| Evidence label (6750:2501) | Evidence in | NOT IN DESIGN: fixed label, hugs text |
| Evidence channel (6750:2502) | #client-kestrel | NOT IN DESIGN: hugs text; long channel names? |
| Date pill (6750:2512) | Monday | NOT IN DESIGN: pill hugs text |
| Date pill (6750:2542) | Tuesday | NOT IN DESIGN: pill hugs text |
| Date pill (6750:2564) | Today | NOT IN DESIGN: pill hugs text |
| Avatar letters (6750:2517, 2525, 2533, 2547, 2555, 2569, 2580) | D / M / D / M / D / D / D | 1 character (32 px avatar) |
| Message 1 sender / time (6750:2520, 2521) | Dylan Moore / 9:12 AM | NOT IN DESIGN: nowrap, hugs text |
| Message 1 body (6750:2522) | Heads up team, we've got a new contractor starting next week and will need the standard agreement reviewed before then. | 368 px wide, wraps (3 lines). NOT IN DESIGN: max lines or "show more"? |
| Message 2 sender / time (6750:2528, 2529) | Mara Ellis / 9:40 AM | NOT IN DESIGN: nowrap, hugs text |
| Message 2 body (6750:2530) | Thanks for the heads up, Dylan — send over the contractor specifics whenever you have them and we'll get the template pulled together. | 368 px wide, wraps (3 lines). NOT IN DESIGN: max lines? |
| Message 3 sender / time (6750:2536, 2537) | Dylan Moore / 2:15 PM | NOT IN DESIGN: nowrap, hugs text |
| Message 3 body (6750:2538) | Sending the contractor details over now — let me know if anything else is needed on our end. | 368 px wide, wraps (2 lines). NOT IN DESIGN: max lines? |
| Message 4 sender / time (6750:2550, 2551) | Mara Ellis / 10:05 AM | NOT IN DESIGN: nowrap, hugs text |
| Message 4 body (6750:2552) | Got it, thanks. Reviewing the NDA language against our standard clauses today. | 368 px wide, wraps (2 lines). NOT IN DESIGN: max lines? |
| Message 5 sender / time (6750:2558, 2559) | Dylan Moore / 4:30 PM | NOT IN DESIGN: nowrap, hugs text |
| Message 5 body (6750:2560) | Any update on this? We'd like to get it locked before the work trial starts. | 368 px wide, wraps (2 lines). NOT IN DESIGN: max lines? |
| Message 6 sender / time (6750:2572, 2573) | Dylan Moore / 10:58 AM | NOT IN DESIGN: nowrap, hugs text |
| Message 6 body (6750:2574) | Can someone review the contractor agreement before noon? We have the work trial starting tomorrow and need the NDA language confirmed today. | 368 px wide, wraps (4 lines). NOT IN DESIGN: max lines? |
| Message 7 sender / time (6750:2584, 2585) | Dylan Moore / 11:36 AM | NOT IN DESIGN: nowrap, hugs text |
| Message 7 tag (6750:2590) | Response | NOT IN DESIGN: fixed label, hugs text |
| Message 7 body (6750:2591) | Just checking this landed. We are blocked on sending the invite until we hear back. | 368 px wide, wraps (2 lines). NOT IN DESIGN: max lines? |
| Hidden rail filter labels (6750:2240, 6750:2249) | Slack / Gmail | NOT IN DESIGN: hidden group; 70 px rail |

## 5. Behavior

### Interactions

- Selecting a queue row opens its detail on the right. Shown by Figma only as a static state (row 1 selected, left bar #FF4800, detail of "Contractor agreement review"). NOT IN DESIGN: click, keyboard (arrow keys?) and what the detail shows for rows 2 to 6.
- Response column sort: the arrow_downward_alt (6750:2275) next to "Response" suggests the list is sorted by Response, descending. NOT IN DESIGN: is the arrow clickable, and what does ascending look like?
- "Response sent" (6750:2608) and "No response needed" (6750:2613): NOT IN DESIGN: what happens after a click (row leaves the queue? confirmation? undo?).
- "No response needed" has a hidden check icon (6750:2614). NOT IN DESIGN: does the check show after it is chosen (selected state)?
- Evidence bar "Evidence in #client-kestrel": the expand arrow (6750:2503) is hidden. NOT IN DESIGN: does the bar open the Slack thread in Slack, or expand/collapse?
- Response reason header (6750:2458): the expand arrow (6750:2466) is hidden. NOT IN DESIGN: can the Situation column collapse?
- Evidence thread scrolls vertically (overflow-y auto) and is aligned to the bottom (newest message last).
- The latest message (6750:2577) has a "Response" tag with a reply icon (#FF4800): it marks the client message that needs a response. NOT IN DESIGN: rule for which message gets the tag.
- Footer "Last checked" shows one time per source: Gmail icon + "Friday 12:00 PM", Slack icon + "Friday 11:58 AM". NOT IN DESIGN: does it update live, and is it clickable (refresh)?
- Search: NOT IN DESIGN: what fields it searches, and if it filters live.

### Breakpoints

- Figma shows only one size: 1920 x 1080. NOT IN DESIGN: behavior below 1920 px (for example 1440, 1280, tablet). Which column shrinks first (queue 926 px fixed, detail flex)?
- NOT IN DESIGN: the detail panel has two fixed columns of 460.5 px; do they stack on narrow screens?

### Edge cases

- "Only Response" variant: the Delivery cells in rows 1, 2, 4, 5 and 6 are at opacity 0 (6750:2305, 2326, 2365, 2387, 2408), so they keep their space but are not visible. NOT IN DESIGN: should the developer render them hidden (keeping layout) or not render them? Screen readers would still read opacity-0 text.
- Row 3 (6750:2328) is the opposite: its Response clock "1h 5m overdue / 3h" is at opacity 0 (6750:2342) and its Delivery cell "Client asked again / Camille Ross" is visible. NOT IN DESIGN: is this intended in an "Only Response" frame?
- The "Delivery" column header (6750:2278) is still visible in this variant. NOT IN DESIGN: keep it?
- Footer says "7 items" but the list shows 6 rows. NOT IN DESIGN: which is correct?
- Rows 1 and 5 have the same title and customer ("Contractor agreement review", Kestrel Apparel Co.) with different clocks and people. NOT IN DESIGN: are they two different items?
- Row 4 shows "17m until target" (not overdue yet) in the same #FF4800 color as overdue rows. NOT IN DESIGN: should not-yet-overdue use a different color?
- Row 6 reason is "Client dissatisfaction" instead of a clock. NOT IN DESIGN: rule for when a reason replaces the clock.
- Long text: row titles wrap (row 6 shows 2 lines, row height grows to 121 px). Names and customers are nowrap. NOT IN DESIGN: truncation rules.
- Two "Divider" frames sit at the same y (6750:2482 and 6750:2487), so two 1 px lines overlap. NOT IN DESIGN: leftover, or one divider only?
- Hidden layers: "Filters" in the rail (6750:2228), both keyboard_arrow_down arrows (6750:2466, 6750:2503), the "Aviso" line (6750:2575), the check in "No response needed" (6750:2614). NOT IN DESIGN: build them or not?
- Copy contains em dashes in Slack messages (6750:2530, 6750:2538): these are client-source quotes and should stay as written.

## 6. Accessibility

### Focus order

Figma has no focus order. NOT IN DESIGN: the designer must confirm. A proposed order, from the visual layout (left to right, top to bottom), for the designer to confirm:

1. Search field (6750:2252)
2. Response sort arrow (6750:2275), if it is interactive
3. Delivery column header (6750:2278), if it is interactive
4. Queue rows 1 to 6 (6750:2285, 2309, 2328, 2348, 2367, 2391), as one list (arrow keys inside?)
5. Footer "Last checked" (6750:2414), if it is interactive
6. "Response sent" button (6750:2608)
7. "No response needed" button (6750:2613)
8. "Evidence in #client-kestrel" bar (6750:2498), if it is interactive
9. Evidence thread scroll area (6750:2508), if it needs keyboard scroll

NOT IN DESIGN: where focus goes after "Response sent" or "No response needed" is used.

### Names and alt text

| Element | Accessible name or alt text | Decorative? |
|---|---|---|
| QTalo logo (6750:2226) | NOT IN DESIGN: "QTalo" or a link to home? | No |
| Search field (6750:2252) | NOT IN DESIGN: label, for example "Search"; the placeholder alone is not a label | No |
| Search icon (6750:2253) | Not needed if the field has a label | Yes |
| Reply icon in list header (6750:2271) | Not needed, text "Response" is next to it | Yes |
| Sort arrow (6750:2275) | NOT IN DESIGN: for example "Sort by Response, descending" | No, if interactive |
| Timer icon in list header (6750:2279) | Not needed, text "Delivery" is next to it | Yes |
| Slack logo in rows (6750:2289, 2371) | NOT IN DESIGN: "Slack" (the source of the item) | No |
| Gmail logo in rows (6750:2313, 2332, 2352, 2395) | NOT IN DESIGN: "Gmail" (the source of the item) | No |
| Selected row bar (6750:2285 border) | NOT IN DESIGN: selection must also be in code, for example `aria-current` or `aria-selected` | Not applicable |
| Footer Gmail icon (6750:2418) | NOT IN DESIGN: "Gmail" (time belongs to this source) | No |
| Footer Slack icon (6750:2427) | NOT IN DESIGN: "Slack" (time belongs to this source) | No |
| Slack logo in detail header (6750:2442) | NOT IN DESIGN: "Slack" | No |
| Reply icon in reason header (6750:2461) | Not needed, text "Response" is next to it | Yes |
| Check icon in "Response sent" (6750:2609) | Not needed, button text names it | Yes |
| "Response sent" button (6750:2608) | Response sent | No |
| "No response needed" button (6750:2613) | No response needed | No |
| Slack Brand Icon in evidence bar (6750:2500) | Not needed, text "Evidence in #client-kestrel" is next to it. NOT IN DESIGN: confirm the source name "Slack" is said elsewhere | Yes |
| Avatars (6750:2516 and others) | Not needed, the sender name is next to it | Yes |
| Reply icon in last message tag (6750:2587) | Not needed, text "Response" is next to it | Yes |
| Divider lines and date row lines | Not needed | Yes |

### Review summary

Summary from the accessibility-reviewer subagent (full review in `accessibility-review.md`): **FAIL, 23 fails, 13 pass, 11 cannot verify** (47 grouped checks, counted with `grep`).

- Contrast: 25 text rows and 4 icon rows fail (13 grouped fails). Causes: #FF4800 and #B27E08 text, light grays (#999999, #BFBFBF, #848484, #808080, #898989, #8B8B8B, #7B7B7B, #A3A3A3), white on #A8A8A8 avatars, and the 60% opacity on older thread messages. Slack and Gmail logos fail 3:1 unless they are treated as essential brand marks.
- Target size: buttons, rows, search bar, sort arrow, evidence bar and logo pass. Delivery header and footer cannot be verified (no size).
- Focus: no focus style on any control, no rule for focus after "Response sent" / "No response needed", and the evidence thread scroll area needs keyboard access. The proposed focus order follows the reading order but must be confirmed.
- Names: search field, sort arrow, QTalo logo, Slack and Gmail logos (rows, footer, detail header) and the selected row have no confirmed name. Button names and decorative icons pass.
- Color alone: selected row is shown only by the #FF4800 bar; add a second cue.
- Open: opacity-0 cells must not be read by screen readers; headings, landmarks, live region messages and reflow below 1920 px are not specified.
- This automated review supports a manual check; it does not replace it.

## 7. Open questions

All `NOT IN DESIGN:` items above are open questions for the designer. The main ones:

1. All states except Default are missing for every control (hover, focus, disabled, loading, empty, error).
2. No Figma variables: all colors, spacing and type need tokens.
3. 25 text rows and 4 icon rows fail AA contrast (counted with `grep`) (see the Contrast table), mainly #FF4800 and #B27E08 text, #999999 labels, #848484 and #808080 text, and all 60% thread text.
4. "Only Response" variant: render the opacity-0 Delivery cells or not? Why is row 3 the opposite (Response hidden, Delivery visible)?
5. "7 items" vs 6 visible rows.
6. What the buttons "Response sent" and "No response needed" do, and where focus goes after.
7. Meaning of Semi Bold vs Regular row titles (rows 1 to 3 vs 4 to 6).
8. Breakpoints below 1920 px.
