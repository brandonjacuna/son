# 03 print production (Vistaprint, StationeryHQ, 4OVER4)
source: vistaprint.com/hub/business-card-file-prep; stationeryhq.com/pages/mastering-cmyk-for-uncoated-paper-the-stationery-designer-s-production-guide; v2.4over4.com/guide/a-guide-to-creating-commercial-print-ready-files | read: full text of each via summarizing fetch (quotes as returned, not page-checked) | verified: yes (read at source this build); the 4over4.com/guide/ and stationeryhq.com short URLs 404, pages above are the live ones

## Rows
| id | kind | row | quote (25 words max) | locator |
|---|---|---|---|---|
| 03.1 | rule | If any color, photo or background touches an edge, build 0.125 in bleed past trim; because cutting drifts and shows white | "add 0.125 in of bleed past the trim" | 4OVER4 |
| 03.2 | rule | Keep text, logos and anything unrecoverable 0.125 in inside trim (Vistaprint card example 3.25 x 1.75 in safe on 3.5 x 2 in) | "The safe margin is 0.125 in inside the trim" | 4OVER4; Vistaprint |
| 03.3 | rule | If the printer publishes a template, use its trim, bleed and safe values over any article; every figure here is an example | "Check the product's minimum text and line sizes, too." | Vistaprint |
| 03.4 | cue | Small text or thin rules set in a four-color mix -> registration shows as fringes -> use 100K | "keep small text a true black rather than a four-color mix" | 4OVER4 |
| 03.5 | rule | Large solid black areas get a rich black (C60 M40 Y40 K100 per 4OVER4 and Vistaprint); because plain K looks weak at area | "Build large solid blacks as C60 M40 Y40 K100 instead of plain K." | 4OVER4 |
| 03.6 | anti | Rejects 100 in every channel (400% ink); too much ink | "setting every channel to 100% can lay down too much ink" | Vistaprint |
| 03.7 | rule | On uncoated, cap total ink at 260% and audit dark fills; above it ink offsets and tracks | "never exceeds 260%." | StationeryHQ |
| 03.8 | model | Uncoated absorbs ink: a 50% dot prints 65% or more, so midtones darken and gamut shrinks | "can expand to cover 65% or more on uncoated stocks." | StationeryHQ |
| 03.9 | rule | Preview uncoated work under an uncoated profile (U.S. Sheetfed Uncoated v2 or PSO Uncoated ISO12647), not the screen look | "U.S. Sheetfed Uncoated v2 or PSO Uncoated ISO12647" | StationeryHQ |
| 03.10 | rule | Hairline floor on uncoated: fine line art 0.5 pt minimum; thin lines and tiny text fill in | "minimum thickness of 0.5 points" | StationeryHQ |
| 03.11 | rule | Reversed type on dark ground: 1.5 pt minimum stroke and looser tracking; ink spread fills counters | "minimum line weight of 1.5 points" | StationeryHQ |
| 03.12 | cue | Soft image at 100% zoom -> will print soft -> replace; images 300 DPI at final size | "Aim for at least 300 DPI" | 4OVER4; Vistaprint |
| 03.13 | rule | On folded work, treat each panel as its own page with its own safe margin; keep type off folds; inner panel is narrower | "Keep important text and logos away from the folds themselves" | 4OVER4 |
| 03.14 | decision | Color-critical job: order a proof or paper sample before the run; screen cannot confirm ink on stock | "order free paper samples or a proof" | 4OVER4 |
| 03.15 | rule | Before export: outline or embed fonts, flatten, CMYK, read every line at 100% | "Flatten transparency, zoom to 100 percent, and read every line of copy" | 4OVER4 |

## Tensions
- Rich black differs: StationeryHQ example C60 M40 Y30 K100 (230%) for uncoated, other pages C60 M40 Y40 K100 (240%). Printer's spec wins.
- Vistaprint and 4OVER4 give no hairline or reversed floors; the only numbers (0.5 pt, 1.5 pt) come from one vendor's stationery guide.
- 4OVER4 calls 0.125 in safe; its checklist elsewhere says 0.125 to 0.25 in. Printer's template wins.

## Not usable
- Creep: 4OVER4 names it for tri-folds but gives no value; no numeric creep allowance found.
- StationeryHQ 5% to 8% midtone lightening and stock-specific tips (Savoy, Mohawk): vendor-specific, unverified as general rule.
- Vistaprint 3.61 x 2.11 in and 3.36 x 1.86 in figures: product-specific.
