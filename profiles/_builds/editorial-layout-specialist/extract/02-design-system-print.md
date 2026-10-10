# 02 Sŏn design system, print values
source: company/brand/design-system/ (tokens/, guidelines/colors-special.html, templates/deck/deck-stage.js, uploads/Son Brand Guidelines v1 (1).md, uploads/Design System Guidelines.md) | read: grep for CMYK, Pantone, bleed, print, foil, @page; targeted reads | verified: yes (read at source this build)

## Rows
| id | kind | row | quote (25 words max) | locator |
|---|---|---|---|---|
| 02.1 | model | ABSENCE: no CMYK, no Pantone for the seven screen colors, no ICC profile, bleed, safe area, trim, or stock spec anywhere in tokens/, guidelines/, uploads/. Print conversion is an open gap; the seat states no print value. | | tokens/ (no hit) |
| 02.2 | model | Only physical value is Gold Foil (Pantone 871C / Kurz Luxor 220). A spec, not a token. | "Physical production specification only. NEVER as flat digital fill." | Design System Guidelines.md l. 41 |
| 02.3 | rule | If a proof shows foil as flat gold or a simulated gradient, block; foil is a named material because no flat-fill token exists. | "Foil only — never flat fill" | Brand Guidelines v1, palette table |
| 02.4 | rule | A foil spec belongs in `son.menu` tokens, which the uploads cite but tokens/ does not define. Flag the missing file; do not invent it. | "exclusively in `son.menu` component tokens" | Brand Guidelines v1 l. 347 |
| 02.5 | anti | Faux letterpress, deboss, foil, or digital grain on print: reject; texture is a material choice. | "faux letterpress, faux deboss, faux foil" | Brand Guidelines v1 l. 242 |
| 02.6 | cue | Print pt sizes exist (body 10-12, menu descriptor 9-11, fine detail 7-8 Light). Fine Light at 7-8pt is where ink spread bites; stock is unspecified, so verify on the proof. | | Brand Guidelines v1 l. 281-291 |
| 02.7 | cue | Only hairline is 1px on screen. No print rule weight given; proof it. | | tokens/spacing.css l. 48 |
| 02.8 | model | Deck template prints via `@page` at design size, margin 0, `print-color-adjust: exact`. RGB screen-to-PDF only: no bleed, marks, or conversion. Not a press path. | | deck-stage.js l. 1056-1058 |
| 02.9 | decision | Menu format is unconfirmed, and the print production session was never run. | "Neither confirmed." | Brand Guidelines v1 l. 822 |
| 02.10 | rule | Pattern never goes on primary menu covers; check any pattern on a cover proof. | "Does not apply to: primary menu covers" | Brand Guidelines v1 l. 234 |

## Tensions
- Frame says "eight screen tokens". colors.css has seven palette values plus derived pale-jade; the eighth palette color is Gold Foil, which has no screen token.
- Menu descriptor is 9-11pt print but 14px in typography.css: no fixed ratio.

## Not usable
- Deck dark-slide and Jade pairing rules: color composition, not print.
- Daypart names conflict with CLAUDE.md canon (frame decision 8); flag, do not repeat.
- Needs an outside source: CMYK per color, bleed, safe area, stock, ink limits, rule weight, proof checklist.
