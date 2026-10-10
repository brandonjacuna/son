# Print production (read for any job that will be printed)

Governing rule: where sources disagree, or where this file and a printer's template differ, the specific printer's template wins. Every number below is an example from a general guide, not a Sŏn spec. The design system carries no print values (no CMYK, Pantone, ICC profile, bleed, safe area, trim, or stock for the screen colors); say so rather than state one.

## What Sŏn's own system gives
| id | row |
|---|---|
| P1 | No print conversion exists for the screen palette. Ask the printer for the conversion and preview it on the proof; never derive CMYK from the hex values and present it as canon. |
| P2 | Gold Foil is a physical production spec only (Pantone 871C, Kurz Luxor 220), never a flat digital fill. A proof showing foil as flat gold or a simulated gradient is blocked. |
| P3 | The foil spec is said to live in `son.menu` component tokens, which the uploads cite but `tokens/` does not define. Flag the missing file; do not invent it. |
| P4 | Print point sizes in the brand guidelines: body 10 to 12, fine detail 7 to 8 in Light. Fine Light at 7 to 8 pt is where ink spread bites; with no stock specified, verify it on the proof. |
| P5 | The only hairline token is 1px on screen; there is no print rule weight. Proof every rule. |
| P6 | The deck template prints via `@page` at design size, margin 0, exact color: an RGB screen-to-PDF path with no bleed, marks, or conversion. It is not a press file. |

## General pre-press (printer's template overrides)
| id | row |
|---|---|
| P7 | Anything touching a trim edge (color, photo, background) extends past trim into bleed, commonly 0.125 in, because cutting drifts and shows white. |
| P8 | Text, logos, and anything that cannot be lost sit inside a safe margin, commonly 0.125 in inside trim (some guides say up to 0.25 in). |
| P9 | Small text and thin rules in a four-color mix show registration fringes: set them in 100K. |
| P10 | Large solid black areas take a rich black (one guide gives C60 M40 Y40 K100, another C60 M40 Y30 K100 for uncoated); plain K reads weak at area. Never 100 in every channel: too much ink. |
| P11 | On uncoated stock, total ink is capped (one guide: 260 percent); audit every dark fill against the printer's limit. |
| P12 | Uncoated stock absorbs ink: a 50 percent dot can print 65 percent or more, so midtones darken and the gamut shrinks. Preview under an uncoated profile (U.S. Sheetfed Uncoated v2 or PSO Uncoated ISO12647), not the screen look. |
| P13 | Hairline floor on uncoated: about 0.5 pt for fine line art. Reversed type on a dark ground: about 1.5 pt minimum stroke and looser tracking, because spread fills counters. (Single-vendor numbers.) |
| P14 | A soft image at 100 percent zoom prints soft: replace it. Images at 300 DPI at final size. |
| P15 | Folded work: each panel is its own page with its own safe margin; type stays off folds; the inner panel is narrower. No reliable creep figure found: ask the printer. |
| P16 | Before export: fonts outlined or embedded, transparency flattened, CMYK, every line read at 100 percent. |
| P17 | A color-critical job gets a printed proof or paper sample before the run. The verdict stays blocked until Brandon approves that proof. |

## Proof checklist (in order)
1. Trim, bleed, and safe area match the printer's template (P7, P8, P15).
2. Fine Light type, hairlines, and reversed type hold on this stock (P4, P5, P13).
3. Color against the printer's conversion and an uncoated preview where relevant; blacks built correctly (P1, P9 to P12).
4. Foil is foil; no faux textures (P2).
5. Images sharp at 100 percent (P14); export parity: no font substitution or compression artifacts (P16).
6. Every name, price, date, and figure matches the source exactly.
