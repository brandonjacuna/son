# Session 10 extraction notes

Mechanical extraction for Session 10 (Ch4, Creating the team environment). Sources read only; nothing in `sources/` was modified.

## Outputs

| File | Lines | Content |
|---|---|---|
| `extraction/s10/book-304-330.md` | 487 | Book pp. 304 to 330, 27 page markers, plus the first paragraph of p.331 as context below the last marker |
| `extraction/s10/book-raw.txt` | 875 | Raw `page.get_text()` per page, pp. 304 to 330, with `===== Book page N =====` separators |
| `extraction/s10/figures/` | n/a | Empty: no image blocks or figures in this range |

No workbook extraction in this pass.

## Page mapping

- Book: PDF page N = book page N (zero offset), as `reference/chapter-map.md` states and as S8's and S9's markers use.
- Confirmed: p.303 ends on a complete paragraph ("...it’s time to build a collective whole whose impact is greater than the sum of its parts."); p.304 opens with the 21.2pt section head "Creating the team environment". No opening fragment is needed.
- p.330 does not end mid-sentence. It ends on the bold italic subhead "Thursday afternoon: one hour" (md line 485), whose paragraph is printed at the top of p.331. That paragraph ("This is more of a creator meeting; ... that can’t wait until Monday.") is placed at md line 487 as a bracketed context line, outside the page markers, mirroring S9's handling of the p.281 fragment.
- p.331 does not open with a heading: it opens with that body paragraph, then the bold italic subhead "Offsites: two full days every quarter" (y 270.8). The 21.2pt section head "Team-building complexities" falls lower on p.331 (y 661.8), where the chapter map puts S11's start.
- Section head in range: "Creating the team environment" p.304, where the chapter map puts it.

## Book: tool, font census, layouts

PyMuPDF 1.26.5 only (`page.get_text("dict")`), no pypdf. All text is one Type3 font (`Unnamed-T3`), color 0 and flags 0 on every span except the footnote superscripts (flags 1). Bold was detected by rendered stroke width and italic by rendered glyph slant (method below). No blue sidebar text in range: the blue on pp. 307 to 309 is table cell text, table rules (RGB 0.20, 0.37, 0.67) and caption labels; the only other colored vector marks are the footnote superscripts, which render blue with an underline.

Size census, pp. 304 to 330 (span counts; spans are roughly word-level, spaces included):

| Size (pt) | Spans | Role |
|---|---|---|
| 15.0 | 11,864 | Body text; bold subheads (roman and italic, including two indented bold italic subheads); bold list lead-ins |
| 11.2 | 1,556 | Table 7 and Table 8 cell text and captions (pp. 307 to 309); boxed callouts "Decision-making and personality types" (p.325) and "Expanding the senior leadership team" (p.330); pull-quote attributions |
| 16.9 | 445 | Pull quotes (p.305, p.325, pp. 329 to 330) |
| 8.7 | 10 | Footnote superscripts 44 to 53 |
| 21.2 | 7 | Section head "Creating the team environment" |

Per page:

| Page | Span counts by size | Other |
|---|---|---|
| 304 | 15.0: 523; 21.2: 7 | |
| 305 | 15.0: 313; 16.9: 169; 11.2: 17 | 3 bullet marks; pull quote |
| 306 | 15.0: 537; 8.7: 2 | |
| 307 | 11.2: 342 | Table 7: cell-fill rectangles (header row and PHASE column, RGB 0.94, 0.94, 0.97) and blue rules; 26 round cell bullets (3.75pt) at x=168.7 and x=357.0 |
| 308 | 15.0: 358; 11.2: 69; 8.7: 1 | Table 7 continues (to y 111.8); Table 8 begins (header fill y 565.5 to 597.0, rules) |
| 309 | 15.0: 459; 11.2: 37 | Table 8 continues (to y 143.3); 3 bullet marks |
| 310 | 15.0: 443 | 7 bullet marks |
| 311 | 15.0: 446 | 5 bullet marks |
| 312 | 15.0: 556; 8.7: 2 | |
| 313 | 15.0: 516 | 1 bullet mark |
| 314 | 15.0: 530 | 2 bullet marks |
| 315 | 15.0: 484 | 6 bullet marks |
| 316 | 15.0: 463 | 3 bullet marks |
| 317 | 15.0: 566 | 5 bullet marks |
| 318 | 15.0: 461 | |
| 319 | 15.0: 483; 8.7: 1 | 3 bullet marks |
| 320 | 15.0: 472 | 3 bullet marks |
| 321 | 15.0: 425 | 1 bullet mark; indented run of text begins (x=98) |
| 322 | 15.0: 559 | Indented run continues; 3 bullet marks at x=105 |
| 323 | 15.0: 492 | Indented run ends (y 588.8); 3 bullet marks at x=105 |
| 324 | 15.0: 467 | 5 bullet marks |
| 325 | 15.0: 103; 16.9: 178; 11.2: 332 | Pull quote; stroked box (77.6, 461.6, 534.4, 697.1) |
| 326 | 15.0: 580; 8.7: 3 | |
| 327 | 15.0: 555 | |
| 328 | 15.0: 630 | |
| 329 | 15.0: 436; 16.9: 76; 8.7: 1 | Pull quote begins and runs off the page |
| 330 | 11.2: 759; 16.9: 22; 15.0: 7 | Pull quote ends; stroked box (77.6, 164.6, 534.4, 667.9) |

The scale matches S8's and S9's range (body 15.0, heads 21.2, callouts and captions 11.2, pull quotes 16.9). New in this range: an indented run of body text (pp. 321 to 323) with its own bold italic subheads, and ruled tables with bulleted cells.

### Bold and italic detection

- Bold: per span mean horizontal stroke width (dark-pixel run length, grayscale render at 4x, threshold 128), with S9's cut of 7.95 px scaled by size/15. At 15.0pt, regular spans measure up to 7.74 px ("Here", p.320) and bold spans 8.27 to 11.8 px (inline lead-ins 9.8 to 11.8; bold roman heads 9.5 to 11.1; bold italic heads 8.3 to 11.4). At 11.2pt (cut 5.96), regular box text measures up to 5.89 px and the box titles 7.8 to 8.3 px. At 16.9pt (cut 8.94), pull-quote text measures 8.09 to 8.32 px and none reads bold. One isolated single bold-reading word mid-line, "Be" (p.315, 7.98 px, "Model ownership. Be on time"), was reset to regular per S9's rule and checked against a rendered crop. Non-alphanumeric spans take bold only when both neighbors are bold. Footnote superscripts (flags 1) are excluded. Bold in the table caption labels ("Table 7", "Table 8") and in the attribution names is not marked, per S7 to S9.
- Italic: all fully bold 15.0pt lines were tested for glyph slant (shear that maximizes the column projection of ink). Bold italic lines measure shear 0.18 to 0.22; bold roman lines and the section head measure 0.00. Verified visually against renders and crops of pp. 309, 313, 318, 319, 321, 328, 330.

### Heading map used

- 21.2 black as `##` (no chapter opener in range).
- 15.0 bold roman as `###`.
- 15.0 bold italic at the text margin (x=77) as `####`.
- 15.0 bold italic inside the indented run (x=98; "Check-ins" p.321 and "Check-outs" p.323, under `#### Use check-ins and check-outs`) as `#####`. New level in this range.
- Boxed callout title (11.2 bold, inside a stroked box) as `> **Title**` in a blockquote, per S8 and S9.
- Pull quote (16.9) as a blockquote; its 11.2 attribution as `> —Name, role`, per S7 to S9. The bold name in the attribution is not marked.
- Inline bold lead-ins as `- **Lead-in:** text`, per S7 to S9.
- Other italics (the book title on p.329, "The Economist" in the p.330 attribution, "MTV Cribs" on p.310) are not preserved, per S7 to S9.

## Book: image blocks and figures

None in range. No image blocks on pp. 304 to 330 (`get_images` is empty on every page) and no vector figures: the only non-glyph vector graphics are the two tables, the two stroked callout boxes, bullet marks, and the footnote superscript marks. `extraction/s10/figures/` is empty.

## Book: tables

- Table 7, "Team development phases, descriptors, and guidance" (pp. 307 to 308): three columns (PHASE, DESCRIPTORS, GUIDANCE), four rows (FORMING, STORMING, NORMING, PERFORMING). Rebuilt from cell geometry: column bands from the vertical rules (x 77.2, 151.5, 339.8, 534.0), row bands from the horizontal rules (y 72.0, 103.5, 292.5, 465.8, 607.5). Cell items are marked by 3.75pt round bullets (13 per column); each item is kept as `• item` and items are separated by `<br>`, per S7's `<br>` convention. The PERFORMING row breaks across the page ("change is" / "likely just around the corner."); split at the page marker with "(cont.)" headers per S8 (md lines 59 to 64 and 68 to 70), caption at line 72.
- Table 8, "Examples of task-focused and team-focused activities" (pp. 308 to 309): two columns (TASK-FOCUSED, TEAM-FOCUSED), four rows, no cell bullets. Column bands x 77.2, 269.2, 534.0; row bands from the rules. The row "Retrospectives on completed" / "work product" breaks across the page; split at the page marker with "(cont.)" headers (md lines 82 to 86 and 90 to 93), caption at line 95.
- Cell text was checked against the rendered pages 307 to 309. Header cells are bolded in markdown per S8; they are not bold in print. Empty continuation cells are `|   |`, per S8.
- Captions are kept as `[caption] Table N. ...`, matching S9's caption lines.

## Book: other handling

- Boxed callouts: "Decision-making and personality types" (p.325, md lines 415 to 419; second paragraph marked by first-line indent at x=113.7). "Expanding the senior leadership team" (p.330, md lines 475 to 483; four paragraphs, three first-line indents at x=113.7). Box body text is at x=92.7.
- Pull quotes: p.305, two paragraphs plus attribution (md lines 35 to 39); p.325, two paragraphs plus attribution (md lines 409 to 413); pp. 329 to 330, one paragraph split at the page marker plus attribution (md lines 467 and 471 to 473).
- Indented run (p.321 from "Check-ins" to p.323 "particular phrase."): body at x=98 with first-line indents at x=119 and bullets at x=105 (text at x=119). Rendered as ordinary paragraphs and list items under the `#####` subheads; the indent itself is not represented.
- Lists: 53 bullet marks (4.5pt filled squares at x=84, or x=105 in the indented run) became `- ` items; continuation lines at the item's text x were joined into the item. No printed numbered lists in range.
- Items and paragraphs that break across pages (p.305 to 306, p.309 to 310, p.311 to 312, p.312 to 313, p.313 to 314 inside the DRI list item, p.315 to 316, p.318 to 319, p.319 to 320, p.321 to 322, p.322 to 323, p.323 to 324, p.324 to 325, p.326 to 327, p.328 to 329, and the pull quote p.329 to 330) are split at the page marker, per S8 and S9; a continuation after the marker is a plain paragraph without a bullet. Section-ending subheads that fall at a page foot ("Why have an offsite?" p.304, "Mutual meeting ownership" p.314, "Thursday afternoon: one hour" p.330) stay on their printed page.
- Footnotes: ten markers, `[^44]` and `[^45]` (p.306), `[^46]` (p.308), `[^47]` and `[^48]` (p.312), `[^49]` (p.319), `[^50]`, `[^51]`, `[^52]` (p.326), `[^53]` (p.329). Note text is not in range (Ch4 notes fall at the chapter's end).
- Hyphenation: six line-end hyphens in range, all true compounds, kept and joined without a space: "ill-" / "defined" and "risk-" / "taking" (Table 7 cells, p.307), "off-" / "color" (p.310), "over-" / "program" (p.319), "action-" / "oriented" (p.328), and "decision-" / "making" across the p.328 to p.329 page break (kept split at the marker as printed: p.328 ends "decision-", p.329 begins "making."). Line-end and line-start em dashes joined without a space.
- Justified lines the text layer split into single-word lines (p.321, "with everyone’s active participation, create mutual") were re-merged by baseline.
- Dropped: nothing. No "OceanofPDF.com" footer or other running footer occurs on pp. 304 to 330.
- Printed cross-references are kept as printed. They do not match PDF page numbers in this range (e.g., "restructuring on page 278" refers to material on PDF pp. 286 to 294; "the box on DRIs on page 286" to the box on PDF pp. 297 to 298; "leadership team meetings on page 308" to the head on PDF p.328; the appendix references "page 338" and "page 341" point outside this range).

## Book: verification

- NUL bytes: 0. U+FFFD: 0 (both in the md and in `book-raw.txt`).
- Page markers: all 27 present, in order, 304 to 330.
- Word-for-word comparison of every page against raw `page.get_text()` (whitespace-normalized; line-end hyphens and dashes joined; markdown syntax, `• ` cell markers, `<br>`, table separator rows and "(cont.)" header rows removed; `[^N]` compared as N; context line excluded): 7,332 raw words. 24 pages identical. Three differences, pp. 305, 325 and 330, all the same comparison artifact S9 recorded: the raw joiner attaches each pull-quote attribution line to the quote's last word ("them.”—Dan", "”—Dan", "immediately.”—Zanny") because the attribution line begins with an em dash; the md keeps them as separate lines. No reordering, no dropped or added words.

## Anomalies

1. Printed cross-references in the text run behind PDF pages (see "Other handling"), consistent with S8 and S9.
2. Headings are mapped by typography, not inferred hierarchy. "Offsites" and the subsections that read as parts of it ("Why have an offsite?", "Which type of offsite is most appropriate?", "What is your team’s development stage?", "Plan and run your offsite") are all bold roman `###`. Likewise "Meetings" and "Groundwork", "Building common understanding", "Meeting roles", "Mutual meeting ownership", "Meeting purpose and structure", "Meeting norms", "Operator mode versus creator mode", "Running the meeting", "A note on leadership team meetings" are all `###`.
3. "Check-ins" and "Check-outs" each appear twice: as `####` in the offsites material (pp. 309, 311) and as `#####` in the indented run under "Use check-ins and check-outs" (pp. 321, 323).
4. Stripe's leadership meeting cadence straddles the S10/S11 boundary: "Monday morning: three hours" and the "Thursday afternoon: one hour" subhead are on pp. 329 to 330; the Thursday paragraph, "Offsites: two full days every quarter" and the rest of the cadence are on p.331 (S11 range). Only the Thursday paragraph is given here, as context.
5. p.308 says "Table 8 on the next page", but Table 8 begins lower on p.308 and continues onto p.309.
6. Table header cells are bolded in the md per S8's convention, not because they are bold in print.

## Table of contents: book (`book-304-330.md`)

| Page | Headings and topics | md lines |
|---|---|---|
| 304 | `## Creating the team environment`; `### Offsites` (Stripe leadership offsites); `### Why have an offsite?` | 7 to 19 |
| 305 | Three offsite objectives (3 bullets); taking people out of routine; pull quote (Dan Weiss); offsites not for talent issues | 23 to 41 |
| 306 | `### Which type of offsite is most appropriate?`; `### What is your team’s development stage?` (Tuckman phases `[^44]`, psychological safety `[^45]`) | 45 to 55 |
| 307 | Table 7 (FORMING, STORMING, NORMING, PERFORMING) | 59 to 64 |
| 308 | Table 7 cont. and caption; forming and storming examples; task versus team balance; `### Plan and run your offsite` (shared planning document `[^46]`); Table 8 begins | 68 to 86 |
| 309 | Table 8 cont. and caption; shared doc benefits (3 bullets); appendix pointer; `#### Check-ins` | 90 to 107 |
| 310 | Check-in story cont.; `#### Icebreakers` (3 bullets); `#### Agenda structure` (4 bullets) | 111 to 133 |
| 311 | Notetaker; `#### Check-outs`; offsite as shared memory; `### Meetings`; meeting purposes (5 bullets) | 137 to 161 |
| 312 | Cost of meetings; staff meeting talk `[^47]`; bad and good meetings `[^48]`; two components; `### Groundwork` | 165 to 175 |
| 313 | Groundwork cont.; `### Building common understanding`; `### Meeting roles`; DRI (bullet) | 179 to 191 |
| 314 | DRI cont.; Facilitator, Notetaker (2 bullets); meeting notes; `### Mutual meeting ownership` | 195 to 205 |
| 315 | Owner signs (3 bullets); ways to create ownership (3 bullets); pedagogy; `### Meeting purpose and structure` | 209 to 229 |
| 316 | One or two purposes; PAL (3 bullets); `### Meeting norms`; `#### Figure out logistics` | 233 to 247 |
| 317 | Logistics (5 bullets); `#### No topics are undiscussable` | 251 to 263 |
| 318 | `#### Be inclusive`; `#### Disagree and commit`; `#### Have a parking lot`; `#### Respect action items` | 267 to 283 |
| 319 | `#### Reconfigure the meeting every three to six months` (3 bullets); `### Operator mode versus creator mode` `[^49]` | 287 to 303 |
| 320 | Operator and creator mix at Stripe; `### Running the meeting`; `#### Structure the meeting` (3 bullets) | 307 to 325 |
| 321 | Decisions (bullet); `#### Make it engaging`; `#### Use check-ins and check-outs`; `##### Check-ins` | 329 to 343 |
| 322 | Work check-ins (3 bullets); personal check-ins; presence rating | 347 to 361 |
| 323 | `##### Check-outs` (3 bullets); one-word check-out; `#### Achieve your purpose` | 365 to 381 |
| 324 | Closing out topics; `#### Clarify the decision-making process`; decision methods (5 bullets) | 385 to 403 |
| 325 | Stating the decision process; pull quote (Dan Weiss); boxed callout "Decision-making and personality types" | 407 to 419 |
| 326 | Senior person speaks last; `#### Use a decision-making framework` `[^50]` `[^51]` `[^52]`; decision logs | 423 to 429 |
| 327 | Decision logs cont.; `#### Honor your meeting norms`; `#### Correct bad meeting behavior` | 433 to 443 |
| 328 | Correcting behavior publicly and privately; `### A note on leadership team meetings` | 447 to 453 |
| 329 | First team `[^53]`; Stripe leadership cadence; `#### Monday morning: three hours`; pull quote begins (Zanny Minton Beddoes) | 457 to 467 |
| 330 | Pull quote ends; boxed callout "Expanding the senior leadership team"; `#### Thursday afternoon: one hour` | 471 to 485 |
| (331) | Context paragraph from p.331 | 487 |

## Full heading list (`book-304-330.md`)

| md line | Page | Heading |
|---|---|---|
| 1 | n/a | `# Scaling People, book pages 304 to 330 (Ch4: Creating the team environment)` |
| 7 | 304 | `## Creating the team environment` |
| 11 | 304 | `### Offsites` |
| 19 | 304 | `### Why have an offsite?` |
| 47 | 306 | `### Which type of offsite is most appropriate?` |
| 51 | 306 | `### What is your team’s development stage?` |
| 78 | 308 | `### Plan and run your offsite` |
| 105 | 309 | `#### Check-ins` |
| 113 | 310 | `#### Icebreakers` |
| 123 | 310 | `#### Agenda structure` |
| 139 | 311 | `#### Check-outs` |
| 145 | 311 | `### Meetings` |
| 173 | 312 | `### Groundwork` |
| 181 | 313 | `### Building common understanding` |
| 187 | 313 | `### Meeting roles` |
| 205 | 314 | `### Mutual meeting ownership` |
| 227 | 315 | `### Meeting purpose and structure` |
| 241 | 316 | `### Meeting norms` |
| 245 | 316 | `#### Figure out logistics` |
| 261 | 317 | `#### No topics are undiscussable` |
| 269 | 318 | `#### Be inclusive` |
| 273 | 318 | `#### Disagree and commit` |
| 277 | 318 | `#### Have a parking lot` |
| 281 | 318 | `#### Respect action items` |
| 289 | 319 | `#### Reconfigure the meeting every three to six months` |
| 299 | 319 | `### Operator mode versus creator mode` |
| 313 | 320 | `### Running the meeting` |
| 317 | 320 | `#### Structure the meeting` |
| 333 | 321 | `#### Make it engaging` |
| 337 | 321 | `#### Use check-ins and check-outs` |
| 341 | 321 | `##### Check-ins` |
| 367 | 323 | `##### Check-outs` |
| 379 | 323 | `#### Achieve your purpose` |
| 387 | 324 | `#### Clarify the decision-making process` |
| 415 | 325 | `> **Decision-making and personality types**` (box title) |
| 425 | 326 | `#### Use a decision-making framework` |
| 437 | 327 | `#### Honor your meeting norms` |
| 441 | 327 | `#### Correct bad meeting behavior` |
| 451 | 328 | `### A note on leadership team meetings` |
| 463 | 329 | `#### Monday morning: three hours` |
| 475 | 330 | `> **Expanding the senior leadership team**` (box title) |
| 485 | 330 | `#### Thursday afternoon: one hour` |
