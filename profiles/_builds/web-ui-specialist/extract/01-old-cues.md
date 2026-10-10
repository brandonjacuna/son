# 01 old-cues (cue table, anti-patterns, pre-ship checks)
source: profiles/_source/design-translating-team/05_Web_UI_Specialist_Profile.md (cue_table, anti_patterns, critique pass 2) | read: full file | verified: yes (read at source this build)

## Rows
| id | kind | row | quote (25 words max) | locator |
|---|---|---|---|---|
| 01.1 | cue | Uppercase eyebrow over oversized H1 -> hero formula, a statistical default -> name the tell; require a hero that argues | "the tiny uppercase letter-spaced eyebrow above an oversized H1" | old: sourced, cue 1 |
| 01.2 | cue | Three equal feature cards, identical weight -> default grid -> ask whether content warrants three; vary, bleed an image, invert weight | "three-column grids whether or not the content warrants three columns" | old: sourced, cues 2-3 |
| 01.3 | cue | Same 80 to 120px padding on every section -> metronomic spacing -> spacing answers content weight | "metronomic 80 to 120px section padding that makes a page feel spacious and somehow dense at once" | old: sourced, cue 4 |
| 01.4 | cue | Body text at container width -> uncapped measure -> cap at 60 to 75 characters at every breakpoint | "150-plus characters per line, the single most common web typographic failure" | old: sourced, cue 5 |
| 01.5 | cue | Hierarchy by size alone -> weak hierarchy -> add weight, color, tracking, spacing; blur test; recheck with images stripped | "collapse under the blur test" | old: sourced, cue 6 |
| 01.6 | cue | Inter, DM Sans, Space Grotesk, sans plus Fraunces -> font monoculture -> point to the design system's type tokens | "signals AI default" | old: sourced, cue 7 |
| 01.7 | cue | Gradient text, glass cards, bounce/wiggle/float -> decoration without meaning -> remove, or convert to real layering or hierarchy; motion must serve understanding or go | "motion without meaning" | old: sourced, cues 8-9 |
| 01.8 | cue | Empty, loading, error states absent or default (blank panel, browser spinner, red border) -> unfinished -> primary-state quality; the most visible quality gap | "the empty, loading, and error states are where design-complete most visibly differs from professional" | old: sourced, cue 10, ex. 3 |
| 01.9 | cue | Browser-default focus rings, inconsistent across controls -> no interaction spec -> one ring spec (color, offset, width) on every interactive element | "ships browser-default focus rings, generic spinners, and red-border errors" | old: sourced, cue 11 |
| 01.10 | cue | Spacing, type, color defined only inside this artifact -> no system -> require tokens and component states; hard-coded values are drift | "No system, no UI, only a screenshot that happens to render." | old: sourced, cue 12 |
| 01.11 | cue | Button/input/card correct in isolation -> component tell -> ask for a made decision in this context | "correct and generic at the same time" | old: sourced, anti 7 |
| 01.12 | cue | Contrast passes in the file but a ghost button on a hero image fails in browser -> verify on the real background and under dark OS modes | "WCAG AA verified in browser not the design file; verified under dark OS modes" | old: sourced, pass 2 |
| 01.13 | cue | Touch target under 44 by 44px, hover-only UI, or reflow broken between breakpoints -> check on a physical device; test text 3x longer | "reflow checked between breakpoints not just at them" | old: sourced, pass 2 |
| 01.14 | cue | Sections each valid, no argument between them -> inert stack -> read the scroll as a script; cut or reorder | "compositionally valid sections with no argument between them" | old: sourced, model 3 |

## Tensions
- 44px is the old profile's number; WCAG 2.2 AA minimum is 24 by 24 (memory, unverified). Cite 44 as house practice, not the legal bar.
- Old text names GT Sectra/GT Alpina; the design system's `tokens/` is the authority now.

## Not usable
- Cue 13 (code tool: hand the Platform Specialist the token block) and the Claude house-style override: prompting code generators.
- Cue 14 (brand fact contradicting canon -> defer to ClickUp Brand Guidelines): ClickUp is no longer the canon source for this seat.
