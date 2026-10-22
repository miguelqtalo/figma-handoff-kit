---
name: recurring-handoff-accessibility-patterns
description: Patterns seen in handoff specs from this kit (Figma wireframes with no variables, no focus states, light gray text); check these first
metadata:
  type: project
---

First review: kestrel-case-option-a (2026-10-22). Result: FAIL, 27 fails of 45 checks.
Second review: kestrel-case-option-a-v2 (2026-10-22). Same screen family, same gaps. Result: FAIL, 28 fails, 3 cannot verify, 9 pass (grouped rows).

Third review: kestrel-case-only-response (2026-10-22). FAIL, 23 fails, 13 pass, 12 cannot verify (grouped by color/control). Same gaps again, plus: selected row shown by border bar only, opacity-0 Delivery cells (screen readers still read them), search field has placeholder only and no border, source logos with no names. Spec counts (25 text, 4 icon fails) matched my recount.
- Focus, hover, disabled, error states are usually all "NOT IN DESIGN" in Figma wireframes. Expect a focus fail on every control.
- Light gray text (#999999, #BFBFBF, #8B8B8B, #848484) and orange/gold status text (#FF4800, #B27E08) fail 4.5:1 on white.
- Older chat messages shown at 60% opacity fail contrast; the spec blends the color before checking.
- Source logos (Slack, Gmail), sort arrows and Material icons usually have no alt text or decorative mark in the spec.
- Spec does not state focus order, avatar alt, or aria-expanded for expand arrows. Selected row is shown by border color only.
- Section 6 of handoff.md says "Pending"; the reviewer text replaces it.
- Spec contrast tables were internally consistent when I spot-checked (#7B7B7B 4.23, #FF4800 3.40). Spec section 7 says "25 text uses and 2 icons fail"; this matched my count.
- Hidden opacity-0 text (for example #A1A1A1 "/ 3h") is not checked; flag it if it ever renders.

**Why:** these gaps repeated across the whole screen, so they are likely for the next screens.
**How to apply:** check these first, then check the rest of the spec.

Process note: the caller asks to save accessibility-review.md, but my instructions say read-only and return text. I return the full review in the final message (via SubagentHandback) for the main session to save.
