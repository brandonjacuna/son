# Session 9 extraction notes

Mechanical extraction for Session 9 (Ch4, Diagnosing team state, Team changes and restructuring, (Re)building the team). Sources read only; nothing in `sources/` was modified.

## Outputs

| File | Lines | Content |
|---|---|---|
| `extraction/s09/book-282-303.md` | 349 | Book pp. 282 to 303, 22 page markers, plus the closing fragment of p.281 as context above the first marker |
| `extraction/s09/book-raw.txt` | 632 | Raw `page.get_text()` per page, pp. 282 to 303, with `===== Book page N =====` separators |
| `extraction/s09/figures/p284-image.png` | n/a | Figure 18 (native image, 1001 x 601) |
| `extraction/s09/figures/p287-image.png` | n/a | Figure 19 (native image, 1001 x 601) |
| `extraction/s09/figures/p301-image.png` | n/a | Figure 20 (native image, 1001 x 601) |

No workbook extraction in this pass.

## Page mapping

- Book: PDF page N = book page N (zero offset), as `reference/chapter-map.md` states and as S8's markers use.
- Confirmed: p.281 ends mid-sentence "...and when"; p.282 opens "you’d like to hear back from them with any questions or feedback (ideally no more than a day or two)." The fragment from p.281 ("You’ll also want to inform them about next steps, including when you aim to finalize communications to the broader organization and when") is placed at md line 5 as a bracketed context line, outside the page markers.
- Section heads fall where the chapter map puts them: "Diagnosing team state" p.282, "Team changes and restructuring" p.286, "(Re)building the team" p.294. Page 304 opens "Creating the team environment" (S10), so p.303 closes the range on a complete paragraph.

## Book: tool, font census, layouts

PyMuPDF 1.26.5 only (`page.get_text("dict")`), no pypdf. All text is one Type3 font (`Unnamed-T3`), color 0 and flags 0 on every span except the footnote superscripts (flags 1). Bold was detected by rendered stroke width and italic by rendered glyph slant (method below). No blue (sidebar) text in this range: rendered ink color is neutral gray on every line.

Size census, pp. 282 to 303 (span counts; spans are roughly word-level, spaces included):

| Size (pt) | Spans | Role |
|---|---|---|
| 15.0 | 9,779 | Body text; bold subheads (roman and italic); bold list lead-ins |
| 11.2 | 972 | Boxed callouts "A word about solid and dotted lines" (p.282) and "DRIs" (pp. 297 to 298); figure captions; pull-quote attribution |
| 16.9 | 332 | Pull quote (p.297) |
| 21.2 | 17 | Section heads "Diagnosing team state", "Team changes and restructuring", "(Re)building the team" |
| 8.7 | 3 | Footnote superscripts 41 (p.283), 42 (p.284), 43 (p.300) |

Per page:

| Page | Span counts by size | Other |
|---|---|---|
| 282 | 15.0: 217; 11.2: 449; 21.2: 5 | Stroked box (77.6, 135.4, 534.4, 433.9) |
| 283 | 15.0: 644; 8.7: 1 | |
| 284 | 15.0: 249; 11.2: 9; 8.7: 1 | Image block |
| 285 | 15.0: 384 | 6 bullet marks |
| 286 | 15.0: 502; 21.2: 7 | 2 bullet marks |
| 287 | 15.0: 275; 11.2: 9 | Image block |
| 288 | 15.0: 538 | 1 bullet mark |
| 289 | 15.0: 579 | 1 bullet mark |
| 290 | 15.0: 611 | |
| 291 | 15.0: 636 | |
| 292 | 15.0: 495 | Printed numbered list |
| 293 | 15.0: 575 | |
| 294 | 15.0: 515; 21.2: 5 | |
| 295 | 15.0: 511 | 2 bullet marks |
| 296 | 15.0: 543 | 1 bullet mark |
| 297 | 15.0: 120; 16.9: 332; 11.2: 16 | Stroked box begins (77.6, 674.6) and runs off the page |
| 298 | 11.2: 482; 15.0: 211 | Stroked box continues (to y 402.4); 4 bullet marks |
| 299 | 15.0: 460 | 5 bullet marks |
| 300 | 15.0: 390; 8.7: 1 | 6 bullet marks |
| 301 | 15.0: 285; 11.2: 7 | Image block; 1 bullet mark |
| 302 | 15.0: 545 | 3 bullet marks |
| 303 | 15.0: 494 | 6 bullet marks |

The scale matches S8's range (body 15.0, heads 21.2), not S7's (body 11.1, heads 15.7). New in this range: a 16.9pt pull quote and two black-ruled 11.2pt boxed callouts.

### Bold and italic detection

- Bold: S8's line-level ink density does not separate inline bold lead-ins from the regular text on the same line, so bold was measured per span as mean horizontal stroke width (dark-pixel run length, grayscale render at 4x, threshold 128). At 15.0pt, regular spans measure about 5.7 to 7.6 px and bold spans about 8.3 to 11.6 px; the cut is 7.95 px scaled by size/15. Isolated single bold-reading words mid-line (capital-heavy or short tokens: "HR" twice, "DRI" three times, "5", "Be", "—a") were reset to regular unless the span is the first token of a bulleted item; each was checked against the rendered page. Non-alphanumeric spans (dashes, spaces) take bold only when both neighbors are bold.
- Italic: all fully bold 15.0pt lines were tested for glyph slant (shear that maximizes the column projection of ink). Bold italic lines measure shear 0.20; bold roman lines measure -0.04 to 0.00. Verified visually against crops of pp. 285, 288 to 292, 294, 296, 299, 302.

### Heading map used

- 21.2 black as `##` (no chapter opener in range).
- 15.0 bold roman as `###`.
- 15.0 bold italic as `####`.
- Boxed callout title (11.2 bold, inside a stroked box) as `> **Title**` in a blockquote, per S8's "Words to live by".
- Pull quote (16.9) as a blockquote; its 11.2 attribution as `> —Name, role`, per S7. The bold name in the attribution is not marked, per S7.
- Inline bold lead-ins as `- **Lead-in:** text`, per S7.
- Other italics (the book title on p.283, the quadrant labels) are not preserved, per S7 and S8.

## Book: image blocks and figures

| Page | Image bbox (pt) | Native px | What it is | Handling |
|---|---|---|---|---|
| 284 | (77.2, 318.0, 534.8, 593.3) | 1001 x 601 | Figure 18, skill-will matrix (quadrant diagram: HIGH/LOW SKILL vertical, LOW/HIGH WILL horizontal, four italic quadrant labels) | Native image extracted by xref and viewed; described at md line 41 |
| 287 | (77.2, 360.0, 534.8, 635.2) | 1001 x 601 | Figure 19, effort-impact matrix (HIGH/LOW EFFORT vertical, LOW/HIGH IMPACT horizontal, four italic quadrant labels) | Native image extracted and viewed; described at md line 95 |
| 301 | (77.2, 72.0, 534.8, 347.3) | 1001 x 601 | Figure 20, delegation framework (TRAPDOOR/ADJUSTABLE vertical, LOW/HIGH IMPACT horizontal; "Do" in bold in the upper right, "Delegate" in italic in the other three) | Native image extracted and viewed; described at md line 309 |

None of the three images has a text layer for its labels; all label text in the descriptions was read from the rendered images. Captions are in the text layer (11.2pt) and kept as `[caption] Figure N. ...` (md lines 43, 97, 311).

## Book: tables

None in range. No cell-fill rectangles or ruled grids on pp. 282 to 303. The two stroked rectangles are callout boxes, not tables.

## Book: other handling

- Boxed callouts: "A word about solid and dotted lines" (p.282, md lines 11 to 15; second paragraph marked by first-line indent at x=113.7). "DRIs" (p.297 title at md line 243; body on p.298, md line 247 onward). The DRIs box body has no first-line indents; paragraph breaks were taken where the previous line in the box ends short (after "...executing at speed." and "...get the decision made."). The box continues across the page break and is split at the page marker as two blockquotes.
- Pull quote: p.297, four paragraphs (one text block each) plus attribution, md lines 233 to 241.
- Lists: 38 bullet marks (4.5pt filled squares at x=84) became `- ` items; continuation lines at x=98 were joined into the item. The p.292 list is printed with numerals "0.", "1.", "2." at x=81.8 and kept as printed (md lines 161 to 165).
- Items and paragraphs that break across pages (p.288 to 289, p.296 to 297, p.298 to 299, p.301 to 302, p.302 to 303) are split at the page marker, per S8; the continuation after the marker is a plain paragraph without a bullet.
- Footnotes: three markers, `[^41]` (p.283), `[^42]` (p.284), `[^43]` (p.300). Note text is not in range (Ch4 notes fall at the chapter's end).
- Hyphenation: one line-end hyphen in range, "under-" / "delegating" (p.297), a true compound; kept, joined without a space. One line-end en dash, "high will–" / "low skill" (p.302), joined without a space to match "high skill–high will" on the same line. Line-end and line-start em dashes joined without a space.
- Justified lines the text layer split into single-word lines (p.289, "There’s a third trigger I’ve often seen misused: an") were re-merged by baseline.
- Dropped: nothing. No "OceanofPDF.com" footer or other running footer occurs on pp. 282 to 303.
- Printed cross-references are kept as printed. They do not match PDF page numbers in this range (e.g., "skill-will matrix I introduced on page 276" refers to the figure on PDF p.284; "team structures on page 262" to the head on PDF p.264; "team offsites on page 290" to material outside this range).

## Book: verification

- NUL bytes: 0. U+FFFD: 0 (both in the md and in `book-raw.txt`).
- Page markers: all 22 present, in order, 282 to 303.
- Word-for-word comparison of every page against raw `page.get_text()` (whitespace-normalized; line-end hyphens and dashes joined; markdown syntax, figure description and image block lines removed; `[^N]` compared as N): 5,832 raw words. 21 pages identical. One difference, p.297: the raw joiner attaches the attribution line to the quote ("why.”—Charles") because the attribution line begins with an em dash; the md keeps them as separate lines ("why.”" / "—Charles"). This is a comparison artifact, not a text difference. No reordering, no dropped or added words.

## Anomalies

1. Printed cross-references in the text run ahead of PDF pages (see "Other handling"). Consistent with S8's note that the chapter map lists "Team structures" at 262 while the head prints on 264.
2. "Why reorganize your team (or teams)?" and "When should you reorganize?" are set in the same bold roman as "Reorganizations", so all three are `###` although the first two read as parts of the third. Headings are mapped by typography, not by inferred hierarchy.
3. "Skill" and "Will" on p.285 are bold roman (`###`) with bold italic "Too little" / "Too much" beneath (`####`).
4. In the DRIs box, "...to meet objectives." fills its line, so whether "Commonly understood terms..." starts a new paragraph cannot be read from geometry; it is left joined to the preceding paragraph.

## Table of contents: book (`book-282-303.md`)

| Page | Headings and topics | md lines |
|---|---|---|
| (281) | Context fragment from p.281 | 5 |
| 282 | Close of p.281 paragraph; boxed callout "A word about solid and dotted lines"; paragraph on introducing the new layer; `## Diagnosing team state` | 7 to 21 |
| 283 | Assessing the team; operating system check; surveying; Lencioni's five dysfunctions `[^41]` | 23 to 31 |
| 284 | Model new behaviors; skill-will matrix `[^42]`; Figure 18 | 33 to 45 |
| 285 | Interpreting quadrants; `### Skill` (`#### Too little`, `#### Too much`); `### Will` (`#### Too little`) | 47 to 71 |
| 286 | `#### Too much`; lower-left, lower-right, upper-right, upper-left quadrants; `## Team changes and restructuring` | 73 to 85 |
| 287 | Plan vs execution; order of operations; Figure 19 | 87 to 97 |
| 288 | Managing stakeholder expectations; `### Reorganizations`; `### Why reorganize your team (or teams)?`; first trigger (bullet) | 99 to 113 |
| 289 | First trigger cont.; second trigger (bullet); misused third trigger; `### When should you reorganize?` | 115 to 125 |
| 290 | `#### Don’t leave the ice cream on the counter for too long`; `#### Structure versus stability` | 127 to 139 |
| 291 | Holding off cont.; `#### Is this the person you want to break your structure for?` | 141 to 151 |
| 292 | High performer exception cont.; `### The three phases of reorgs` (numbered 0 to 2); `#### Phase 0 ...`; `#### Phase 1 ...` | 153 to 175 |
| 293 | Phase 1 cont. (sharing the plan, conversations); `#### Phase 2 ...` | 177 to 185 |
| 294 | Phase 2 text; reorgs as dynamism; `## (Re)building the team`; `### Career conversations` | 187 to 199 |
| 295 | Career conversations: timing, not an interview, three purposes (2 bullets) | 201 to 213 |
| 296 | Third purpose (bullet); career conversation as reference point; `### Delegating`; two forms; under- and over-delegation | 215 to 227 |
| 297 | Signs of over- or under-delegating; pull quote (Charles Phillips); boxed callout title "DRIs" | 229 to 243 |
| 298 | DRIs box body; micromanagers; under-delegating signs (4 bullets) | 245 to 261 |
| 299 | Over-delegating (5 bullets); delegating inefficient then efficient; `#### When to delegate` | 263 to 285 |
| 300 | Framework axes (2 bullets) `[^43]`; four examples (4 bullets) | 287 to 303 |
| 301 | Figure 20; exceptions; three reasons (Modeling bullet) | 305 to 315 |
| 302 | Modeling cont.; Urgent work; Resource constraints; `### How to delegate, and to whom`; delegation conversation steps begin | 317 to 331 |
| 303 | Steps cont. (6 bullets); transition to building a collective whole | 333 to 349 |

## Full heading list (`book-282-303.md`)

| md line | Page | Heading |
|---|---|---|
| 1 | n/a | `# Scaling People, book pages 282 to 303 (Ch4: Diagnosing team state, Team changes and restructuring, (Re)building the team)` |
| 11 | 282 | `> **A word about solid and dotted lines**` (box title) |
| 19 | 282 | `## Diagnosing team state` |
| 51 | 285 | `### Skill` |
| 53 | 285 | `#### Too little` |
| 59 | 285 | `#### Too much` |
| 65 | 285 | `### Will` |
| 67 | 285 | `#### Too little` |
| 75 | 286 | `#### Too much` |
| 85 | 286 | `## Team changes and restructuring` |
| 103 | 288 | `### Reorganizations` |
| 109 | 288 | `### Why reorganize your team (or teams)?` |
| 123 | 289 | `### When should you reorganize?` |
| 129 | 290 | `#### Don’t leave the ice cream on the counter for too long` |
| 135 | 290 | `#### Structure versus stability` |
| 145 | 291 | `#### Is this the person you want to break your structure for?` |
| 157 | 292 | `### The three phases of reorgs` |
| 167 | 292 | `#### Phase 0 (one month): Decide whether you need a reorg and determine your new structure` |
| 173 | 292 | `#### Phase 1 (one to two weeks): Get buy-in from the key people who need to be involved` |
| 185 | 293 | `#### Phase 2 (one to two days): Create a communications plan and inform all of those affected` |
| 195 | 294 | `## (Re)building the team` |
| 199 | 294 | `### Career conversations` |
| 221 | 296 | `### Delegating` |
| 243 | 297 | `> **DRIs**` (box title) |
| 285 | 299 | `#### When to delegate` |
| 325 | 302 | `### How to delegate, and to whom` |
