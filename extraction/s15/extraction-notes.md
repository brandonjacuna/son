# Session 15 extraction notes

Mechanical extraction for Session 15 (Ch5: Managing managers; Managing out, firing, and layoffs; Some final thoughts on management; the Chapter 5 exercises and templates; the Chapter 5 notes). Sources read only; nothing in `sources/` was modified. Method and output form follow Session 14 (`extraction/s14/extraction-notes.md`), which follows S12 and S13.

## Outputs

| File | Lines | Content |
|---|---|---|
| `extraction/s15/book-449-483.md` | 381 | Book pp. 449 to 483, 35 page markers; one bracketed context line at the top of p.449 (the end of S14's "Potential outcome 2", md line 7); prose pp. 449 to 466 in full; the appendix divider p.467 in full; one-line duplicate pointers for pp. 468 to 480 and the top of p.481; the Managing Out Checklist (pp. 481 to 482) in full; the Chapter 5 notes (p.483) in full |
| `extraction/s15/book-raw.txt` | 969 | Raw `page.get_text()` per page, pp. 449 to 483, with `===== Book page N =====` separators |
| `extraction/s15/workbook-s15.md` | 23 | Workbook p.124 in full (Managing Out Checklist), 1 page marker; census note for p.125 |
| `extraction/s15/figures/` | n/a | Not created: no image blocks or figures in range |

## Page mapping and boundaries

- Book: PDF page N = book page N (1-based; PyMuPDF index N-1), as S8 to S14 used. Confirmed: p.449 opens with "Usually, this decision comes out of the inquiry phase of your" (the continuation S14 recorded) and carries the 21.2pt head "Managing managers" (y 475.8).
- Start boundary (p.449): y 75.8 to 432.8 is S14's material (two paragraphs finishing "Potential outcome 2: Move roles or teams"), already quoted by S14 at `extraction/s14/book-419-448.md` line 471. Rendered here as one bracketed context line quoting both paragraphs verbatim (md line 7; checked against the p.449 text layer with line breaks joined and "customer-/facing" joined as a compound), then `## Managing managers` (md line 9). Excluded from the word comparison.
- Prose ends on p.466 ("...Maybe to them, but definitely to you."), the end of Chapter 5's text. "Some final thoughts on management" (p.465) is the chapter's closing section.
- "Outcome 3" of the low-performer phases (employee leaves the company), deferred by S14, is picked up explicitly on p.454: "Now we can return to Outcome 3 from the section on managing low performers" (md line 85).
- End boundary (p.483): the Chapter 5 notes page, notes 67 to 76, ending with the running footer "OceanofPDF.com". p.484 is outside the range (per the chapter map, S16 begins at p.484).

What each page is:

| Page | Content |
|---|---|
| 449 | S14 context (top); `## Managing managers` |
| 450 | Managing managers prose; `###` heads; footnote 76; foot: Table 10's empty header strip |
| 451 | Table 10 and caption; prose |
| 452 to 453 | Managing when you're not the expert; monospace "Working with Claire" excerpt (p.453) |
| 454 | `## Managing out, firing, and layoffs` |
| 455 to 461 | Managing out: three steps, pre-work, departure conversations (junior, senior), legal considerations, Crenn pull quote (p.460), gross misconduct and layoffs |
| 461 to 465 | When something bad happens to an employee (three situation types); Weiss pull quote (p.465) |
| 465 to 466 | `## Some final thoughts on management`; end of chapter text |
| 467 | Appendix divider: "EXERCISES AND TEMPLATES / Chapter 5", list of five exercises, workbook URL |
| 468 to 471 (top) | Performance Review Template: duplicate of workbook pp. 104 to 110 (S13) |
| 471 (foot) to 473 | Compensation Conversations Preparation and Guide: duplicate of workbook pp. 111 to 112 (S13) |
| 474 to 477 (top) | Performance Improvement Documentation Templates: duplicate of workbook pp. 113 to 117 (S12) |
| 477 (foot) to 481 (top) | Performance Improvement Plan Template: duplicate of workbook pp. 118 to 122 (S14) |
| 481 (y 327 on) to 482 | Managing Out Checklist (eight items): S15's, extracted in full |
| 483 | Chapter 5 notes, 67 to 76 |

S14's notes said the PIP template ran to PDF p.481; confirmed (its last lines and the two signature lines are at the top of p.481, inside the ruled box, y 66 to 276). The checklist shares p.481 with it.

## Book: tool, font census, layouts

PyMuPDF 1.26.5 only (`page.get_text("dict")`), no pypdf. Two typographic systems, as in S11's range:
- Prose pp. 449 to 466: the Type3 prose font (`Unnamed-T3`), color 0, flags 0 except the footnote superscript (flags 1). Table 10 cell text and caption (p.451) are in the same Type3 font name at 11.2, rendered blue in a monospace face (the text layer reports color 0 for the first span; the fill is blue in print).
- Appendix pp. 467 to 482: Neue Haas Grotesk (`NHaasGroteskTXPro-55Rg`, `-65Md`, `-75Bd`), color 0x335FAC (blue) on a lavender panel; the checkbox glyphs "□" and the divider label and dash on p.467 are Type3. The URL on p.467 is color 0x0000EE (link blue). p.483 (notes) is Type3.

Size census, pp. 449 to 483 (span counts; spans are roughly word-level, spaces included; p.449 counted whole, including the S14 context lines):

| Size (pt) | Spans (all) | Spans (prose pp. 449 to 466) | Role |
|---|---|---|---|
| 15.0 | 9,012 | 9,007 | Body text; bold subheads (roman and italic); bold lead-ins in bullets; monospace excerpt (p.453); appendix: the divider dash (p.467), two 15.0 lines on p.472 and one on p.473 are Neue Haas bold labels, and the "OceanofPDF.com" footer (p.483) |
| 11.2 | 947 | 177 | Table 10 cell text and caption (p.451); pull-quote attributions (pp. 460, 465); appendix body text (pp. 467 to 481); notes (p.483) |
| 16.9 | 349 | 317 | Pull quotes (Crenn p.460, Weiss p.465); appendix subheads; the checklist items and checkbox glyphs (pp. 481 to 482) |
| 21.2 | 21 | 21 | Section heads "Managing managers" (p.449), "Managing out, firing, and layoffs" (p.454), "Some final thoughts on management" (p.465) |
| 30.0 | 11 | 0 | Appendix titles ("Chapter 5" p.467; exercise titles pp. 468, 471, 474, 477; "Managing Out Checklist" p.481) |
| 25.0 | 1 | 0 | "Notes" head (p.483) |
| 8.7 | 1 | 1 | Footnote superscript 76 (p.450) |

Per page:

| Page | Span counts by size | Other |
|---|---|---|
| 449 | 15.0: 590; 21.2: 3 | S14 context (top 18 lines); section head |
| 450 | 15.0: 564; 8.7: 1 | 2 bold roman subheads; superscript 76 (renders blue with an underline); Table 10 empty header strip at page foot (y 714 to 746) |
| 451 | 15.0: 379; 11.2: 141 | Table 10 (2 columns, 9 round 3.75pt blue cell bullets), caption; 3 prose paragraphs |
| 452 | 15.0: 485 | Bold roman subhead; 6 bullet marks |
| 453 | 15.0: 565 | Monospace excerpt (7 lines, x=98) |
| 454 | 15.0: 566; 21.2: 9 | Section head |
| 455 | 15.0: 491 | Numbered list 1 to 3 (printed numerals, x 81.8); bold roman subhead; 2 bullet marks |
| 456 | 15.0: 458 | Bullet item continued from p.455; 1 bullet mark; bold roman subhead; bold italic subhead |
| 457 | 15.0: 591 | 2 bullet marks with bold lead-ins |
| 458 | 15.0: 544 | Bullet item continued from p.457; 2 bullet marks; bold italic subhead |
| 459 | 15.0: 589 | Bold roman subhead |
| 460 | 15.0: 308; 16.9: 132; 11.2: 19 | 2 bullet marks with bold lead-ins; pull quote (Crenn) and attribution; bold roman subhead; bold italic subhead at page foot |
| 461 | 15.0: 565 | Bold italic subhead; bold roman subhead at page foot |
| 462 | 15.0: 589 | 2 bold italic subheads (two lines each) |
| 463 | 15.0: 599 | Bold italic subhead (two lines) |
| 464 | 15.0: 581 | |
| 465 | 15.0: 337; 16.9: 185; 11.2: 17; 21.2: 9 | Pull quote (Weiss, two paragraphs) and attribution; section head |
| 466 | 15.0: 206 | End of chapter text |
| 467 | 30.0: 1; 15.0: 1; 11.2: 13 | Divider: label, dash, "Chapter 5", five titles, URL |
| 468 | 30.0: 2; 16.9: 1; 11.2: 25 | Performance Review Template (duplicate) |
| 469 | 16.9: 1; 11.2: 27 | Duplicate |
| 470 | 16.9: 1; 11.2: 31 | Duplicate |
| 471 | 30.0: 3; 16.9: 1; 11.2: 21 | Duplicate (Performance Review end; Compensation guide title) |
| 472 | 15.0: 2; 11.2: 25 | Duplicate |
| 473 | 15.0: 1; 11.2: 21 | Duplicate |
| 474 | 30.0: 2; 16.9: 1; 11.2: 23 | Duplicate (Documentation Templates) |
| 475 | 16.9: 2; 11.2: 22 | Duplicate |
| 476 | 16.9: 1; 11.2: 25 | Duplicate |
| 477 | 30.0: 2; 16.9: 1; 11.2: 22 | Duplicate (Documentation Templates end; PIP Template title and preamble) |
| 478 | 11.2: 29 | Duplicate |
| 479 | 11.2: 26 | Duplicate |
| 480 | 11.2: 35 | Duplicate |
| 481 | 30.0: 1; 16.9: 16; 11.2: 6 | PIP end (duplicate); Managing Out Checklist title and 6 items |
| 482 | 16.9: 7 | Checklist items 7 and 8 |
| 483 | 25.0: 1; 15.0: 1; 11.2: 419 | Chapter 5 notes 67 to 76; footer |

### Bold and italic detection

- Bold: per span mean horizontal stroke width (dark-pixel run length, grayscale render at 4x, threshold 128), normalized to 15pt; cut 8.2 px, as S11 to S14. In range at 15.0, regular spans reach at most 8.14 px (the token "HR" on pp. 454, 459, 463, which never reads bold; 8.13 on p.459); the lightest true bold span is 8.40 ("two" in the italic subhead "Junior-level conversations (one to two conversations)", p.456, and "lawsuit)" p.462), and bold spans run to 11.20 ("The", p.456). No single-word false bold occurred. Pull-quote text (16.9) normalizes to at most 7.41 and none reads bold. The 11.2 attribution names and the "Table 10." caption label normalize above the cut (9.2 to 12.1) because the size is scaled up; per S7 to S14 the attribution name and the table caption label are not bolded. The footnote superscript (flags 1) is excluded.
- Italic: glyph slant per line (shear that maximizes the column projection of ink), measured on every line carrying bold spans. In this implementation the bold italic subheads measure 0.20 to 0.25 and every bold roman head and bold lead-in measures 0.00 (S14's implementation used the opposite sign, -0.10; the split is equally clean). Confirmed against a render of p.456 ("Junior-level conversations..." italic). Italics other than slant-detected subheads are not preserved.
- Monospace: the "Working with Claire" excerpt (p.453) is in the same Type3 font name but a fixed-width face, set as an indented block (x=98 on every line, its own text block); confirmed by render.
- Bold lead-in punctuation: in print the period after the bold lead-ins "They’ll start re-litigating" and "They’ll start talking about next steps for their departure" (p.457) is regular weight but sits in the same text span as the last word, so it is inside the bold, as S13 and S14 did (same for the p.460 lead-ins).

### Heading map used

- 21.2 as `##`; 15.0 bold roman as `###`; 15.0 bold italic as `####`, per S8 to S14. Two-line bold italic heads (pp. 462, 463) are merged onto one line. Bold lead-ins as `**Lead-in.**` inside list items.
- Pull quotes (16.9) as blockquotes with the 11.2 attribution as `> —Name, role` after a `>` spacer line, per S12 to S14; the attribution name is not bolded. The Weiss quote has two paragraphs (line gap 35pt against 20pt), separated by a `>` line.
- Appendix (per S11): the divider label as `## Exercises and templates` plus `[Section label in source: "EXERCISES AND TEMPLATES"]`, "Chapter 5" (30.0) as `###`, the five titles as `- ` items; the checklist title (30.0) as `###`; checkbox items as `- □`; "Notes" (25.0) as `##` with the notes as a numbered list.

## Section heads (`book-449-483.md`)

| md line | Page | Heading |
|---|---|---|
| 1 | n/a | `# Scaling People, book pages 449 to 483 (Ch5: Managing managers, Managing out, firing, and layoffs, Some final thoughts on management, Exercises and templates, Notes)` |
| 9 | 449 | `## Managing managers` |
| 21 | 450 | `### How to think about managing managers` |
| 27 | 450 | `### Individual 1:1s versus manager 1:1s` (last line of p.450; Table 10 on p.451) |
| 47 | 452 | `### Managing when you’re not the expert` |
| 83 | 454 | `## Managing out, firing, and layoffs` |
| 105 | 455 | `### Pre-work: feedback, documentation, and preparation` |
| 121 | 456 | `### The departure conversation` |
| 129 | 456 | `#### Junior-level conversations (one to two conversations)` |
| 159 | 458 | `#### Senior-level departure conversations` |
| 173 | 459 | `### Legal considerations` |
| 189 | 460 | `### Gross misconduct and layoffs` |
| 193 | 460 | `#### Firing for gross misconduct` (last line of p.460; text on p.461) |
| 201 | 461 | `#### Layoffs` |
| 205 | 461 | `### When something bad happens to an employee` (last line of p.461; text on p.462) |
| 213 | 462 | `#### A one-time event (e.g., death of a family member or friend, miscarriage, severe injury, divorce, lawsuit)` |
| 217 | 462 | `#### An ongoing hardship (e.g., mental illness, a sick family member, a failing relationship, substance abuse)` |
| 229 | 463 | `#### An employee’s experience has legal ramifications (e.g., sexual harassment, discrimination)` |
| 255 | 465 | `## Some final thoughts on management` |
| 269 | 467 | `## Exercises and templates` |
| 273 | 467 | `### Chapter 5` |
| 339 | 481 | `### Managing Out Checklist` |
| 361 | 483 | `## Notes` |

Other navigation points: Table 10 at md lines 33 to 37 (caption line 37) with its p.450 header-strip note at line 29; the six non-skill areas where a manager adds value at md lines 53 to 63; the "Working with Claire" monospace excerpt at md line 71; the three managing-out steps (numbered) at md lines 99 to 103; the three preparation items at md lines 109 to 117 (split at the p.455 to 456 marker); the two responses to a junior departure decision (bold lead-ins) at md lines 143 to 149 (split at the p.457 to 458 marker); the two rare exceptions at md lines 153 to 155; the severance and negotiation paragraph at md line 171; the two legal points (bold lead-ins) at md lines 181 to 183; the Crenn pull quote at md lines 185 to 187; the Weiss pull quote at md lines 249 to 253; the checklist at md lines 341 to 357; note 76 at md line 381.

Heading-level notes (the md follows the type, as S13 and S14 did):
- Under `## Managing out, firing, and layoffs`, "Pre-work...", "The departure conversation", "Legal considerations", "Gross misconduct and layoffs" and "When something bad happens to an employee" are `###`. The first three follow the three numbered steps, but step 3, "Logistics and next steps", has no head of its own; logistics are covered inside the departure-conversation text and the checklist.
- "Junior-level conversations" and "Senior-level departure conversations" (`####`) are children of "The departure conversation"; "Firing for gross misconduct" and "Layoffs" (`####`) are children of "Gross misconduct and layoffs"; the three situation types (`####`) are children of "When something bad happens to an employee". Read by content, "Legal considerations" (`###`) sits inside the departure material (it follows the senior-level conversation and addresses threats of legal action during managing out).
- "When something bad happens to an employee" is not about performance or termination; it sits under the managing-out section by typography only.

## Table of contents: book (`book-449-483.md`)

| Page | Headings and topics | md lines |
|---|---|---|
| 449 | Context (S14); `## Managing managers`; captain to colonel | 7 to 13 |
| 450 | Coach, sounding board, unblocker; `### How to think about managing managers` (Five Whys `[^76]`); `### Individual 1:1s versus manager 1:1s`; Table 10 strip note | 17 to 29 |
| 451 | Table 10 and caption; technical to adaptive; the 1:1 is their time; how 1:1s should start | 33 to 43 |
| 452 | `### Managing when you’re not the expert`; non-skill value (6 bullets); find them help | 47 to 65 |
| 453 | "Working with Claire" excerpt; spend time on the ground; Stripe risk operations; "engineerication" | 69 to 77 |
| 454 | `## Managing out, firing, and layoffs`; Outcome 3; manage out versus fire; hiring right | 81 to 89 |
| 455 | Bad hires linger; fire fast but fire well; three steps; `### Pre-work...`; preparation (begins) | 93 to 113 |
| 456 | Preparation (ends); `### The departure conversation`; junior versus senior; `#### Junior-level conversations...` | 117 to 131 |
| 457 | Not up for discussion (exit package); two responses (begins) | 135 to 145 |
| 458 | Responses (end); two sittings, two exceptions; don't let it drag; `#### Senior-level departure conversations` | 149 to 163 |
| 459 | Two or three conversations; be firmer; negotiation, severance matrix; `### Legal considerations` | 167 to 175 |
| 460 | Two legal points; Crenn pull quote; `### Gross misconduct and layoffs`; `#### Firing for gross misconduct` | 179 to 193 |
| 461 | Code of conduct, same-day departure, investigation; `#### Layoffs`; `### When something bad happens to an employee` | 197 to 205 |
| 462 | Slack message; three types; `#### A one-time event...`; `#### An ongoing hardship...` | 209 to 219 |
| 463 | Sample check-in wording; nine times out of ten; balance empathy; `#### An employee’s experience has legal ramifications...` | 223 to 231 |
| 464 | Resources; don't compartmentalize; confidentiality; missing-employee example | 235 to 243 |
| 465 | Example ends; Weiss pull quote; `## Some final thoughts on management` | 247 to 259 |
| 466 | Envelope of notes; management touches people | 263 to 265 |
| 467 | `## Exercises and templates`; `### Chapter 5`; five titles; URL | 269 to 281 |
| 468 to 480 | One-line duplicate pointers | 285 to 333 (one line per page) |
| 481 | PIP-end pointer; `### Managing Out Checklist`; items 1 to 6 | 337 to 351 |
| 482 | Items 7 to 8 | 355 to 357 |
| 483 | `## Notes`; 67 to 76 | 361 to 381 |

## Book: image blocks and figures

None. `get_images` is empty on pp. 449 to 483 and there are no image blocks. Vector marks only: the 15 square bullet marks (4.5pt, x=84), Table 10's rules, header fills and 9 round cell bullets (pp. 450 to 451), the blue footnote-superscript underline (p.450), the appendix lavender panels, the PIP form box and signature rules (pp. 477 to 481), and each page's white background rectangle. `extraction/s15/figures/` was not created.

S14 recorded "a blue-ruled, lavender-filled box at the page foot (y 714)" on p.450. It is not a sidebar: it is the top of Table 10, an empty lavender header strip with blue rules (x 77.2 to 534.8, y 714 to 746). The table's header text and body print at the top of p.451 (header strip repeated there, y 66 to 97.5). The p.450 strip carries no text.

## Book: tables

- Table 10, "Example topics discussed in individual contributor 1:1s and manager 1:1s" (pp. 450 to 451): two columns (INDIVIDUAL CONTRIBUTOR 1:1, MANAGER 1:1), one body row with bulleted cells (4 items and 5 items, round 3.75pt blue bullets). Column bands from the rules (x 77.2, 276.8, 534.0); header row y 66 to 97.5, body y 97.5 to 240 on p.451. Rebuilt as a markdown table, items as `• item` separated by `<br>` per S10, header cells bolded per S8 and S11 (cell text is a monospace face in print, no bold), caption as `[caption] Table 10. ...` (md line 37). The empty header strip on p.450 is recorded as a bracketed note (md line 29), not as a table.

No other tables in the prose. The appendix forms (PIP form, pp. 477 to 481) are pointer-only.

## Book: other handling

- Lists: 15 square bullet marks, all first level (x=84), became `- ` items: p.452: 6; p.455: 2; p.456: 1; p.457: 2; p.458: 2; p.460: 2. The one numbered list (p.455) prints its numerals inline ("1." at x 81.8, same text block) and is kept as printed.
- List items split at a page marker (p.455 to 456 "Familiarizing yourself with local employment laws..."; p.457 to 458 "They’ll start talking about next steps..."): the continuation after the marker is indented two spaces.
- Paragraph breaks: text-layer blocks match the printed paragraphs (first-line indent x=98 or a gap). One unindented line break inside a block was split into its own paragraph after checking the render: p.455 "Your preparation should involve:" starts a new line after the short line "...related prior information and work product." (md lines 107 and 109). Paragraphs split at page markers (per S8 to S14): pp. 449 to 450, 452 to 453, 453 to 454, 454 to 455, 456 to 457, 458 to 459, 459 to 460, 462 to 463, 463 to 464, 464 to 465, 465 to 466; list items at 455 to 456 and 457 to 458. Headings at a page foot with text on the next page: p.450 "Individual 1:1s versus manager 1:1s" (Table 10 follows on p.451), p.460 "Firing for gross misconduct", p.461 "When something bad happens to an employee".
- Justified lines that the text layer split into single-word lines (p.449 "Now that we’ve discussed the primary actions and key"; p.456 "Start the conversation by summarizing the performance") were re-merged by baseline.
- Hyphenation: three line-end hyphens in the prose, all true compounds, kept and joined without a space: "low-performance" (p.455), "expectation-setting" (p.462), "off-putting" (p.465); plus "customer-facing" in the context line. One line-start em dash ("pay off / —but", p.466) joined without a space. The two attribution lines begin with an em dash and are not joined.
- Monospace passage: the "Working with Claire" excerpt (p.453, one paragraph) is a blockquote, per S8, S11 and S14 (md line 71). It is the same text as the "Working with Claire" exercise in Chapter 3 (S7).
- Pull quotes: Dominique Crenn (p.460, one paragraph), Dan Weiss (p.465, two paragraphs).
- Printed cross-references (printed page numbers run behind the PDF): "the self-awareness analysis of skills and capabilities in Chapter 1" (p.449, context only); "Operating Principle 1!" (p.452) refers to the operating principles (Operating Principle 1: Build self-awareness to build mutual awareness, as quoted in S9's range); "your “Working with Me” document" and "my “Working with Claire” document" (pp. 452 to 453) refer to the Chapter 3 exercises (S7, `### Working with Claire` at PDF p.253); "Outcome 3 from the section on managing low performers" (p.454) is "Potential outcome 3: Employee leaves the company" in the p.438 phase overview (S14); "the sections on coaching and feedback" (p.462) are S12's range; "the section on managing through uncertainty on page 323" (p.461) is `### Managing through uncertainty`, PDF p.350 (S11 range).
- Appendix divider (p.467): the decorative dash under the label is a text-layer "—" (15.0 Type3) and is dropped, per S11.
- Italics not preserved except slant-detected subheads, per S7 to S14.
- Dropped: running footer "OceanofPDF.com" (p.483); the p.467 decorative dash.

## Book: appendix duplicates

Each duplicated exercise was compared word for word, book text layer against workbook text layer (running head and page numbers removed; checkbox and bullet glyphs removed; word-break hyphens ignored):

| Book pages | Exercise | Workbook pages | Already extracted at | Result |
|---|---|---|---|---|
| 468 to 471 (to y ~330) | Performance Review Template | 104 to 110 | `extraction/s13/workbook-ch5.md` lines 11 to 224 | 729 words each, identical |
| 471 (foot) to 473 | Compensation Conversations Preparation and Guide | 111 to 112 | `extraction/s13/workbook-ch5.md` lines 225 to 274 | 483 against 484 words; only difference the workbook's "Notes" label |
| 474 to 477 (top) | Performance Improvement Documentation Templates | 113 to 117 | `extraction/s12/workbook-ch5.md` lines 29 to 133 | 626 against 628 words; same words: workbook "Notes" label; one line-break split ("[1:1/performance" in the book, "[1:1/ performance" in the workbook); the head "Insufficient progress (after a reasonable period)" sits at a different text-layer position (order artifact, not content) |
| 477 (foot) to 481 (top) | Performance Improvement Plan Template | 118 to 122 | `extraction/s14/workbook-s14.md` lines 5 to 131 | 955 against 961 words; differences are the workbook's two "Notes" labels and four form counters "1/4" to "4/4" |
| 481 to 482 | Managing Out Checklist | 124 | extracted here (both) | 72 words each, identical |

All four duplicates are content-identical to the workbook; each book page 468 to 480 carries a one-line bracketed pointer, and p.481 carries a pointer for its PIP portion before the checklist. One typo is common to both sources and was already in S12's extraction: "and they impact they had" (book p.475, workbook p.114).

## Footnotes

One marker in the prose: `[^76]` (p.450, md line 23, after "to get to the root of the issue."). The note text is on the Chapter 5 notes page, p.483 (note numbers and texts are separate text blocks; paired by y position, all 10 pairs verified against the md):

- 76: “Five Whys,” Wikipedia, last modified February 2, 2022, https://en.wikipedia.org/wiki/Five_whys. **Citation.** Not substantive.

p.483 carries notes 67 to 76 (the whole Chapter 5 notes section); the page is in range and is extracted in full as a numbered list (md lines 363 to 381). Notes 67 to 75 belong to earlier sessions' body text (74 and 75 are S14's; 67 to 73 fall in S12 and S13's pages). The only substantive note on the page is 72 (the Stripe engineer's feedback that the job ladder should focus on outcomes, not skills or inputs; md line 373), which belongs to S13's range; it is extracted verbatim in the md as part of the page. No substantive note belongs to S15.

## Counts

- Em dashes in the md prose bodies (context line excluded, pp. 449 to 466): 19, matching raw from the head "Managing managers" to the end of p.466 (19; includes the two attribution dashes). No en dashes in the prose. (Appendix and notes: the p.467 decorative dash is dropped; the one en dash on p.483, "32–33" in note 75, is kept.)
- "guest": 0 occurrences in range (book, raw, and workbook).

## Book: verification

- NUL bytes: 0. U+FFFD: 0 (in the md, `book-raw.txt` and `workbook-s15.md`).
- Page markers: all 35 present, in order, 449 to 483.
- Word-for-word comparison of every extracted page against raw `page.get_text()` (whitespace-normalized; line-end hyphens and em dashes joined, except before an attribution line; markdown syntax removed: heading hashes, list dashes, blockquote markers, continuation indent, `**`, table pipes and `<br>`, `[caption]`; `[^N]` compared as N; bracketed context, note and pointer lines excluded; checkbox and bullet glyphs removed): 5,149 raw words over pp. 449 to 467 and 481 to 483.
  - pp. 449 to 466: **all 18 pages identical** (p.449 compared from the head "Managing managers" on). No reordering, no dropped or added words.
  - p.467: identical except the dropped decorative dash (the section label is compared against the bracketed label line).
  - pp. 481 (from "Managing Out Checklist") and 482: identical.
  - p.483: identical as a word multiset (228 words; the text layer lists the ten note numbers before the ten note texts, so sequence order differs by construction); each of the ten "N. text" lines in the md matches its y-paired number and text block exactly.
  - pp. 468 to 480 and the PIP portion of p.481: not in the md by design; compared against the workbook instead (table above).
- The p.449 context line matches the p.449 text layer verbatim (both paragraphs).

## Figures and numbers in her material

The program never reproduces financial figures. Across book pp. 449 to 483 and workbook p.124 there is **no monetary amount, no percentage of pay, no salary band figure, no severance amount or formula, no equity figure, no compensation formula, and no headcount or layoff threshold**. Every place that names a pay element or states a number that could be read as financial or as a threshold:

| Page | md line | What it says | Financial? |
|---|---|---|---|
| Book 453 | 75 | Stripe "performs checks to ensure that the business is legitimate and that we’re able to process payments for them" | No: Stripe's product (payments processing), not pay; no figure |
| Book 453 | 75 | "You’ll also get a lot of bonus points for sharing your observations" | No: figure of speech, not a pay bonus |
| Book 457 | 139 | "In some countries, this also means negotiating an exit package. Either way, be firm." | Names a pay element (exit package); no figure |
| Book 457 | 143 | Re-litigating "happens less than 5 percent of the time" | No: a share of conversations |
| Book 458 | 161 | Senior departures: "Half of the time, the leader will see the writing on the wall" | No: a share of cases |
| Book 459 | 171 | Negotiation "anything from severance to medical insurance to the timing of their departure, especially if there are upcoming stock vesting dates"; "the best tool at your disposal is a severance matrix, the framework your HR and employment legal teams should have developed for what might be offered for a termination departure"; involve HR or legal "to help run interference and enforce the matrix" | Names pay elements (severance, medical insurance as a benefit, stock vesting, severance matrix); **no figure, no matrix values** |
| Book 461 | 203 | Layoffs: "a role elimination due to restructuring"; plan "best directed by the company’s HR and legal teams, or outside consultants" | No: no headcount, threshold or cost |
| Book 463 | 227 | Time off work "may mean hiring someone to fill in" | Implies a cost; no figure |
| Book 466 | 265 | "will pay off" | No: figure of speech |
| Book 468 (pointer; content at S13 wb md) | 285 | Performance Review Template: "diversity, equity, and inclusion"; "less than a half-year"; "H1, H2"; "2–3 projects", "1–2 strengths" | No: "equity" is DEI, not ownership; review periods and counts |
| Book 471 to 473 (pointers; content at S13 wb md) | 297, 301, 305 | Compensation Conversations guide: "link pay to performance"; "fact pages about your compensation program"; "the compensation philosophy"; "date of last uplevel, and the size of their last salary increase"; "promotion or increase"; "do not set the expectation that they will receive the same total increase"; "Money affects people personally"; "no change in compensation"; "Remind them of their current compensation"; "Share or affirm their base salary for the coming year"; "Share their target bonus for the coming year" | Names pay elements (compensation, salary increase, base salary, target bonus); **no figure** |
| Book 477 to 480 (pointers; content at S14 wb md) | 321, 333 | PIP: "at-will nature of your employment... with or without notice"; "The fact that you have entered into a PIP for [X] weeks in no way guarantees employment for that period of time" | Names notice (employment-law, not notice pay); no figure |
| Book 483 | 373 | Note 72: "an L3 engineer should be able to scope a project..." | No: a job level |
| Book 483 | 375 | Note 73: "10 Performance Review Biases" (article title) | No |
| Workbook 124 | 7 to 23 (`workbook-s15.md`) | Managing Out Checklist | No pay element; no number beyond its eight items |

Non-financial durations and counts (listed so they are not mistaken for thresholds): Five Whys, "at least five times" (p.450, md 23); "the final five minutes" (p.451, md 43); "a few hours", "two hours", "the prior two years" (p.453, md 73 to 75); "three to five days" engineerication (p.453, md 77); bad hires' impact "takes years to undo" (p.455, md 93); three managing-out steps (p.455, md 99 to 103); junior conversations "one to two conversations" (p.456, md 129); "complete the conversation in two sittings" (p.458, md 151); senior firing "over the course of a few months" (p.458, md 161); senior "at least two or three conversations" (p.459, md 167); "Michelin three-star restaurant" (p.460, md 187, a rating); gross misconduct: one conversation, "leave the same day" (p.461, md 197); investigation conclusion "within, say, 24 hours" (p.461, md 199); "Six words" (p.462, md 209); three types of tough situations (p.462, md 211); "after a few days" (p.462, md 215); "Nine times out of ten" (p.463, md 225); "a few days" absence (p.464, md 241); "months or even years later" (p.466, md 265); Table 10 "What is success in a year?" (p.451, md 35). Appendix (pointer pages): weekly check-ins "for the next [X] weeks", "the next few weeks" (documentation templates); PIP "typically four to six weeks", "3–5 points", "[X] weeks", weekly progress meetings (PIP template). Cross-reference "page 323" (p.461) is a page number.

## Workbook: census and extraction

| Page | Content | Handling |
|---|---|---|
| 124 | Managing Out Checklist: 36pt bold title, eight 12pt items each beside a vector checkbox (17.6pt stroked square), two decorative 0.5pt rules; no Notes area | **Extracted in full**, `workbook-s15.md` |
| 125 | Last page of the workbook: page number in the text layer; a vector-drawn Stripe Press colophon (logo; "Ideas for progress / South San Francisco, California / press.stripe.com", read from a render, not in the text layer) | Not extracted (not program content). S12's census said p.125 "carries only the page number"; that is true of the text layer only |

The workbook has 125 pages; Chapter 5 ends at p.124. The Managing Out Checklist is the last exercise in the workbook. Fonts: `NHaasGroteskTXPro-75Bd` 36.0 (title), `NHaasGroteskTXPro-55Rg` 12.0 (items), `SuisseIntl-Book` 6.5 (running head and page number, dropped). Conventions per S8, S12 and S14: title as `##`, checkbox items as `- [ ]` (S8), the three-line last item joined. Verification: word comparison of p.124 against raw `get_text()` (running head and page number removed): 72 words, identical. The workbook checklist and the book checklist (pp. 481 to 482) are word-identical; the book wraps the items differently (wider type) and prints "□" glyphs in its text layer, the workbook draws the boxes as vector squares.

Content notes for the synthesis writer: the checklist step "Hold the coaching-out conversation with your report" uses "coaching-out", where the book's prose says "managing out" and "managing-out conversation"; the checklist's eight steps map onto the book's three steps (pre-work: items 1 to 5; the departure conversation: item 6; logistics and next steps: items 7 and 8). The checklist has no step for gross-misconduct firing, layoffs, legal threats or severance negotiation.

## Anomalies and uncertainties

1. The top of p.449 is S14's material (context line, md line 7), not re-extracted.
2. The p.450 "box" S14 flagged is Table 10's empty header strip, not a sidebar; recorded as a bracketed note (md line 29) and the table rebuilt on p.451.
3. The three numbered managing-out steps (p.455) do not each get a head: "Logistics and next steps" has none; "Legal considerations" and "When something bad happens to an employee" are `###` siblings of the step heads by typography but not by content (see heading-level notes).
4. The bold lead-in periods on pp. 457 and 460 are regular weight in print but inside the bold span in the md (S13 and S14 convention).
5. "Your preparation should involve:" (p.455) is split into its own paragraph from an unindented line break confirmed by render; every other paragraph follows text-layer blocks.
6. p.483's text layer lists note numbers before note texts, so that page is verified as a word multiset plus a per-note y-pairing check rather than as a sequence.
7. The appendix duplicates (pp. 468 to 481 top) are pointer-only by instruction; their pay-element language (Compensation Conversations guide, pp. 471 to 473) is listed in the figures table above because it is in range, although its text lives in S13's workbook extraction.
8. The Five Whys note (76) is the only footnote in S15's prose, and it is a citation.
