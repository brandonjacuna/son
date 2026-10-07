# Session 14 extraction notes

Mechanical extraction for Session 14 (Ch5: Managing high performers, The steady middle, Managing low performers, including the phases of managing low performers and the performance improvement plan). Sources read only; nothing in `sources/` was modified. Method and output form follow Session 13 (`extraction/s13/extraction-notes.md`), which follows Session 12.

## Outputs

| File | Lines | Content |
|---|---|---|
| `extraction/s14/book-419-448.md` | 471 | Book pp. 419 to 448, 30 page markers; one bracketed context line at the top of p.419 (the end of S13's formal review material, md line 7) and one after the last marker (the p.449 continuation of "Potential outcome 2" and the next head, md line 471) |
| `extraction/s14/book-raw.txt` | 938 | Raw `page.get_text()` per page, pp. 419 to 448, with `===== Book page N =====` separators |
| `extraction/s14/workbook-s14.md` | 136 | Workbook pp. 118 to 123 in full (Performance Improvement Plan Template: preamble and Notes p.118; the four-page PIP form pp. 119 to 122; Notes p.123), 6 page markers |
| `extraction/s14/figures/` | n/a | Not created: no image blocks or figures in range |

## Page mapping and boundaries

- Book: PDF page N = book page N (1-based; PyMuPDF index N-1), as S8 to S13 used. Confirmed: p.419 opens with "clearer path to the next level." (the end of S13's p.418 paragraph) and carries the 21.2pt head "Managing high performers" (y 391.8 to 413.4), matching S13's recorded boundary.
- Start boundary (p.419): the first 14 lines of p.419 (y 75 to 364) belong to S13: the end of the "Managing disappointment" paragraph ("...the accompanying rewards in the months to come.") and the closing paragraph of the formal review material ("Every company should have these basic people processes... within the system you’ve built."). S13 already quoted both in full (S13 md line 297). Rendered here as one bracketed context line quoting both verbatim (md line 7), then `## Managing high performers` (md line 9). Excluded from the word comparison.
- End boundary (p.448): p.448 ends at a paragraph end ("...and how to seek them out.") inside `### Potential outcome 2: Move roles or teams` (head at p.448 y 552.8). The section is not finished: it runs two more paragraphs onto p.449 (S15 range), "Usually, this decision comes out of the inquiry phase..." and "This approach can be tricky... internal mobility into open roles." (p.449 y 75.8 to 432.8), before the 21.2pt head "Managing managers" (p.449 y 475.8), which opens S15. **By content the two p.449 paragraphs are S14's material** (the second outcome of the low-performer phases: moving the person to a better-fitting role, time-bound, with HR and recruiting involved). Both are quoted verbatim in the bracketed context line after the p.448 body (md line 471); nothing else from p.449 is included. S15 should treat the top of p.449 as S14 material.
- "Potential outcome 3: Employee leaves the company" has no head of its own in range. The book defers it: "The section on managing out, firing, and layoffs later in this chapter will cover situations where it’s time for someone to leave the company" (p.444, md line 413). That material is S15's.

## Book: tool, font census, layouts

PyMuPDF 1.26.5 only (`page.get_text("dict")`), no pypdf. One typographic system in range: the Type3 prose font (`Unnamed-T3`), color 0 on every span, flags 0 except footnote superscripts (flags 1). One `LiberationSerif` span: the ellipsis in "apprenticeship…" (p.426), as S11 and S12 saw. No sidebars (no blue ink), no tables, no exercise panels, no image blocks (`get_images` empty on every page), no vector figures (the only non-glyph vector marks are the 4.5pt square bullet marks and the full-page white background rectangle).

Size census, pp. 419 to 448 (span counts; spans are roughly word-level, spaces included; p.419 counted whole, including the S13 context lines). Same scale as S8 to S13, verified:

| Size (pt) | Spans | Role |
|---|---|---|
| 15.0 | 15,824 | Body text; bold subheads (roman and italic); bold lead-ins in bullets and the phase list; monospace sample email and sample conversation (same Type3 font name, fixed advance) |
| 16.9 | 105 | Pull quote (Sam Hawgood, p.428) |
| 21.2 | 15 | Section heads "Managing high performers" (p.419), "The steady middle" (p.431), "Managing low performers" (p.432) |
| 11.2 | 15 | Pull-quote attribution (p.428) |
| 8.7 | 2 | Footnote superscripts 74 (p.419), 75 (p.436) |

p.449 for reference (not extracted): 15.0: 590; 21.2: 3 ("Managing managers"). p.450: 15.0: 564; 8.7: 1 (superscript 76); a blue-ruled, lavender-filled box at the page foot (y 714), S15's.

Per page:

| Page | Span counts by size | Other |
|---|---|---|
| 419 | 15.0: 524; 21.2: 5; 8.7: 1 | S13 context (top 14 lines); section head; superscript 74 |
| 420 | 15.0: 569 | Bold roman subhead; justified line re-merged |
| 421 | 15.0: 365 | Bold roman subhead; 10 bullet marks |
| 422 | 15.0: 380 | Bullet item continued from p.421; bold roman subhead; 13 bullet marks |
| 423 | 15.0: 557 | 6 bullet marks; bold italic subhead |
| 424 | 15.0: 522 | Bold italic subhead; 1 bullet mark (bold lead-in over two lines) |
| 425 | 15.0: 542 | Bullet item continued from p.424; 3 bullet marks (bold lead-ins); bold italic subhead at page foot |
| 426 | 15.0: 593 | LiberationSerif ellipsis; bold italic subhead; justified line re-merged |
| 427 | 15.0: 632 | Bold italic subhead |
| 428 | 15.0: 427; 16.9: 105; 11.2: 15 | Pull quote (Hawgood) and attribution; bold roman subhead |
| 429 | 15.0: 577 | Bold roman subhead at page foot |
| 430 | 15.0: 611 | |
| 431 | 15.0: 548; 21.2: 5 | Section head "The steady middle" |
| 432 | 15.0: 529; 21.2: 5 | Section head "Managing low performers" |
| 433 | 15.0: 555 | 2 bold roman subheads |
| 434 | 15.0: 556 | Bold italic subhead |
| 435 | 15.0: 620 | Bold italic subhead |
| 436 | 15.0: 511; 8.7: 1 | Bold italic subhead; superscript 75 |
| 437 | 15.0: 502 | Bold italic subhead at page top; bold roman subhead |
| 438 | 15.0: 390 | Phase list (4 bold lead-ins, 6 bullet marks, 3 with bold lead-ins); bold italic subhead (two lines) |
| 439 | 15.0: 564 | Numbered list 1 to 3; bold italic subhead at page foot |
| 440 | 15.0: 496 | Numbered list 1 to 2; bold roman subhead; bold italic subhead |
| 441 | 15.0: 634 | |
| 442 | 15.0: 585 | Bold italic subhead; 2 bullet marks (bold question lead-ins) |
| 443 | 15.0: 532 | Bullet item continued from p.442; 1 bullet mark; bold roman subhead; monospace sample email begins |
| 444 | 15.0: 506 | Monospace email ends; bold italic subhead; numbered list 1 to 3 |
| 445 | 15.0: 490 | Bold italic subhead then bold roman subhead (two lines); 5 bullet marks (2 with bold lead-ins) |
| 446 | 15.0: 483 | Bullet item continued from p.445; 1 bullet mark; justified line re-merged; bold italic subhead (two lines) |
| 447 | 15.0: 425 | Monospace sample conversation (5 paragraphs); appendix pointer |
| 448 | 15.0: 599 | Bold roman subhead; ends at a paragraph end, section continues on p.449 |

### Bold and italic detection

- Bold: per span mean horizontal stroke width (dark-pixel run length, grayscale render at 4x, threshold 128), normalized to 15pt; cut 8.2 px, as S11 to S13. In range, regular body spans reach at most 8.16 px (the token "HR" on pp. 433, 434, 436, which never reads bold; also "PIP" 7.93 and "I" 8.05, p.447); the lightest true bold span is 8.26 ("will" in the italic subhead "Anticipate when the work will become boring", p.423), and bold spans run to 12.63 ("HR" in the head "The role of HR teams", p.433). No single-word false bold occurred. The pull-quote attribution names normalize above the cut (10.6 to 11.6) because the 11.2 size is scaled up; per S7 to S13 the attribution name is not bolded. Footnote superscripts (flags 1) are excluded. Pull-quote text (16.9) normalizes to 6.1 to 7.4 and none reads bold.
- Italic: glyph slant per line (shear that maximizes the column projection of ink), measured on every line carrying bold spans. The bold italic subheads all measure at the italic end of the scan (-0.10 in this implementation's sign convention); every bold roman head, bold lead-in and section head measures 0.00. Confirmed against a render of p.438 (the roman phase-list lead-ins against the italic "Phase 0" subhead). Italics other than slant-detected subheads are not preserved (for example the book title Radical Candor, p.436).
- Monospace: the two sample passages are in the same Type3 font name but set in a fixed-width face (confirmed by render, pp. 443 and 447). Detected by per-word advance (standard deviation under 0.05pt per character, mean 7.8pt, on lines with at least three measurable words); short last lines of each paragraph joined by text block.

### Heading map used

- 21.2 as `##`; 15.0 bold roman as `###`; 15.0 bold italic as `####`, per S8 to S13. Bold lead-ins as `**Lead-in:**` inside list items and the phase list; in print the colon after "Phase 0" to "Phase 3" and after "Potential outcome 1" to "3" on p.438 is regular weight but sits in the same text span as the numeral, so it is inside the bold, as S13 did for its sidebar lead-ins.
- Pull quote (16.9) as a blockquote with the 11.2 attribution as `> —Name, role` after a `>` spacer line, per S12 and S13; the attribution name is not bolded.

## Section heads (`book-419-448.md`)

| md line | Page | Heading |
|---|---|---|
| 1 | n/a | `# Scaling People, book pages 419 to 448 (Ch5: Managing high performers, The steady middle, Managing low performers)` |
| 9 | 419 | `## Managing high performers` |
| 19 | 420 | `### Pushers and pullers` |
| 33 | 421 | `### Pushers` |
| 73 | 422 | `### Pullers` |
| 115 | 423 | `#### Anticipate when the work will become boring` |
| 123 | 424 | `#### Remember: There’s more opportunity than you think` |
| 139 | 425 | `#### Let go` (last line of p.425; its text starts on p.426) |
| 147 | 426 | `#### Manage for potential, not experience` |
| 159 | 427 | `#### Conduct pre-exit interviews and retros` |
| 173 | 428 | `### Retaining top talent` |
| 187 | 429 | `### Telling a high performer they won’t be promoted` (last line of p.429; text on p.430) |
| 201 | 431 | `## The steady middle` |
| 213 | 432 | `## Managing low performers` |
| 229 | 433 | `### Edge cases` |
| 235 | 433 | `### The role of HR teams` |
| 247 | 434 | `#### No surprises` |
| 257 | 435 | `#### Use documentation to foster clarity and trust` |
| 267 | 436 | `#### Show compassion` |
| 275 | 437 | `#### Move deliberately` |
| 281 | 437 | `### Phases of managing low performers` |
| 313 | 438 | `#### Phase 0: Your one-off feedback becomes a pattern; form a hypothesis on the outcome` |
| 331 | 439 | `#### Phase 1: Get aligned about the performance challenge` (last line of p.439; text on p.440) |
| 343 | 440 | `### Delivering the feedback` |
| 349 | 440 | `#### Response 1: denial` |
| 367 | 442 | `#### Response 2: relief and a readiness to problem-solve` |
| 383 | 443 | `### Document your discussion` |
| 399 | 444 | `#### Phase 2: Agree on next steps` |
| 417 | 445 | `#### Phase 3: Create an action plan` |
| 419 | 445 | `### Potential outcome 1: Agree on and execute a performance improvement plan` |
| 443 | 446 | `#### Sample conversation introducing the performance improvement plan` |
| 467 | 448 | `### Potential outcome 2: Move roles or teams` |

Other navigation points: the pushers lists (at their best, at their worst, to support) at md lines 35 to 71 and the pullers lists at md lines 75 to 111 (the "To support pullers" list starts on p.423); the four high-performer latitude examples with bold lead-ins at md lines 127 to 137; the Sam Hawgood pull quote at md lines 169 to 171; the phase overview (bold roman lead-ins, not heads) at md lines 289 to 309; the three likely outcomes at md lines 323 to 327; the two additions to one-off feedback at md lines 337 to 339; the three problem-solving questions (bold lead-ins) at md lines 371 to 379; the sample documentation email (monospace blockquote) at md lines 389 to 395, split at the p.443 to 444 marker; the three next steps at md lines 407 to 411; the three PIP contents at md lines 423 to 427; the three types of fixes (bold lead-ins) at md lines 431 to 439; the sample PIP conversation (monospace blockquote) at md lines 449 to 457; boundary context at md lines 7 and 471.

Heading-level notes (the md follows the type, as S13 did):
- Under `### Phases of managing low performers`, the four phases are `####` (bold italic), but "Delivering the feedback" and "Document your discussion" (inside Phase 1) and "Potential outcome 1" and "Potential outcome 2" (inside Phase 3) are `###` (bold roman). Read by content, all four are children of their phase, and "Response 1" and "Response 2" (`####`) are children of "Delivering the feedback"; the typography inverts the nesting. "Sample conversation introducing the performance improvement plan" (`####`) is a child of "Potential outcome 1".
- The p.438 phase overview repeats the four phase names and three outcomes as bold roman lead-ins in a list; they are not heads.
- Under "Managing high performers", "Pushers and pullers", "Pushers", "Pullers", "Retaining top talent" and "Telling a high performer they won’t be promoted" are `###`; the six tactics from "Anticipate when the work will become boring" to "Conduct pre-exit interviews and retros" are `####` and read by content as children of the "additional tactics" sentence at the end of "Pullers" (md line 113). "Edge cases" and "The role of HR teams" are `###`; the four principles "No surprises" to "Move deliberately" are `####`.

## Table of contents: book (`book-419-448.md`)

| Page | Headings and topics | md lines |
|---|---|---|
| 419 | Context (S13); `## Managing high performers`; 80-20 rule `[^74]`; understand what drives them | 7 to 13 |
| 420 | `### Pushers and pullers`; pushers, pullers; disproportionate impact | 17 to 27 |
| 421 | `### Pushers`: at their best (5), at their worst (4), to support (begins) | 31 to 59 |
| 422 | Support pushers (ends); `### Pullers`: at their best (5), at their worst (4) | 63 to 97 |
| 423 | Support pullers (6); additional tactics; `#### Anticipate when the work will become boring` | 101 to 117 |
| 424 | Played the person; `#### Remember: There’s more opportunity than you think`; leadership without management roles | 121 to 127 |
| 425 | Org structures, type of work, your job; `#### Let go` | 131 to 139 |
| 426 | Let go; `#### Manage for potential, not experience`; "interesting" talent | 143 to 151 |
| 427 | Gmail peer-to-peer support example; `#### Conduct pre-exit interviews and retros` | 155 to 163 |
| 428 | Retrospectives; pull quote (Hawgood); `### Retaining top talent` | 167 to 177 |
| 429 | Planning projects for high performers; capped teams; `### Telling a high performer they won’t be promoted` | 181 to 187 |
| 430 | Promoting too quickly; owning the decision; late constructive feedback | 191 to 195 |
| 431 | Setting expectations at high growth; `## The steady middle`; talent portfolio; terminal level | 199 to 207 |
| 432 | Celebrating consistency; `## Managing low performers`; context; two reasons; cost | 211 to 221 |
| 433 | Goal; `### Edge cases`; `### The role of HR teams` | 225 to 237 |
| 434 | HR as resource, manager responsible; `#### No surprises` | 241 to 251 |
| 435 | Exceptions; `#### Use documentation to foster clarity and trust` | 255 to 261 |
| 436 | Written record; `#### Show compassion`; ruinous empathy `[^75]` | 265 to 271 |
| 437 | `#### Move deliberately` (three months); `### Phases of managing low performers` | 275 to 283 |
| 438 | Phase overview; `#### Phase 0` | 287 to 315 |
| 439 | Hypothesis; three likely outcomes; `#### Phase 1` | 319 to 331 |
| 440 | Two additions; `### Delivering the feedback`; `#### Response 1: denial` | 335 to 351 |
| 441 | Handling denial | 355 to 361 |
| 442 | Gather data; `#### Response 2`; problem-solving questions | 365 to 373 |
| 443 | Questions end; `### Document your discussion`; sample email begins | 377 to 391 |
| 444 | Sample email ends; appendix pointer; `#### Phase 2`; three next steps | 395 to 413 |
| 445 | `#### Phase 3`; `### Potential outcome 1`; PIP contents; types of fixes | 417 to 433 |
| 446 | Fixes end; measuring progress; `#### Sample conversation...` | 437 to 445 |
| 447 | Sample PIP conversation; appendix pointer | 449 to 459 |
| 448 | PIP conclusions (99 percent); `### Potential outcome 2: Move roles or teams` (runs onto p.449) | 463 to 469 |
| (449) | Context: two continuation paragraphs, head "Managing managers" | 471 |

## Book: image blocks and figures

None. `get_images` is empty on pp. 419 to 448, there are no image blocks, and `get_drawings` shows only the 48 square bullet marks (4.5pt, x=84) and each page's white background rectangle. `extraction/s14/figures/` was not created.

## Book: tables

None in range.

## Book: other handling

- Lists: 48 bullet marks, all first level (x=84), became `- ` items: p.421: 10; p.422: 13; p.423: 6; p.424: 1; p.425: 3; p.438: 6; p.442: 2; p.443: 1; p.445: 5; p.446: 1. The three numbered lists (pp. 439, 440, 444) print their numerals ("1." at x 81.8, continuation at x 98 in a separate text block) and are rebuilt as numbered items with continuations joined.
- List items split at a page marker (p.421 to 422 "Praise them... Promote them. / Give them raises."; p.424 to 425; p.442 to 443; p.445 to 446): the continuation after the marker is indented two spaces as a continuation of the item, not a new item.
- Phase overview (p.438): "Phase 0:" to "Phase 3:" are bold lead-ins on unbulleted lines at x=77 and are rendered as plain paragraphs starting `**Phase N:**`; the bullets under Phase 1 and Phase 3 (the latter with bold "Potential outcome N:" lead-ins) are `- ` items.
- Monospace passages: the sample documentation email (pp. 443 to 444, two paragraphs, split at the marker, the continuation with `>`) and the sample PIP conversation (p.447, five paragraphs) are blockquotes, per S8 (workbook email template) and S11 (welcome-email template). Their bracketed placeholders ("[list areas of improvement highlighted in the PIP; ...]", "[list the achievements or milestones provided in the PIP]") are kept as printed.
- Pull quote: Hawgood (p.428), one paragraph plus attribution.
- Paragraph breaks: text-layer blocks match the printed paragraphs (first-line indent x=98 or a gap). Paragraphs split at page markers (per S8 to S13): pp. 419 to 420, 420 to 421, 426 to 427, 427 to 428, 428 to 429, 431 to 432, 432 to 433, 433 to 434, 435 to 436, 437 to 438, 438 to 439, 441 to 442; list items at 421 to 422, 424 to 425, 442 to 443, 445 to 446; the monospace email at 443 to 444; and 448 to 449 (context line; there the break falls at a paragraph end but inside the section). Headings at a page foot with text on the next page: p.425 "Let go", p.429 "Telling a high performer...", p.439 "Phase 1".
- Justified lines that the text layer split into single-word lines (p.420 "state the less obvious: Great employees can have a"; p.426 "about it. Maybe it’s new projects, education courses,"; p.446 "and the how—work process, including collaboration and") were re-merged by baseline.
- Hyphenation: one line-end hyphen in range, "time-constrained" (p.427), a true compound, kept and joined without a space. (p.449's "customer-facing" in the context line is joined the same way.) Line-end em dashes joined without a space.
- Printed cross-references running behind the PDF (as S8 to S13 recorded): "the section on career conversations on page 283" (p.423) refers to the career-conversations material in Chapter 4 (a 15pt "Career conversations" subhead sits at PDF p.294; not verified further); "Operating Principle 3: Distinguish between management and leadership" (p.424) refers to the operating principles; "the section on giving hard feedback on page 355" (p.440) is "Giving hard feedback", PDF p.391 (S12 range); "the chapter appendix on page 418 for more email templates" (p.444) is the Performance Improvement Documentation Templates, PDF p.474 (same material as workbook pp. 113 to 117); "the chapter appendix on page 422 for a sample PIP template" (p.447) is the Performance Improvement Plan Template, PDF pp. 477 to 481 (same material as workbook pp. 118 to 122); "the self-awareness analysis of skills and capabilities in Chapter 1" (p.449, context only) refers to Chapter 1.
- Italics not preserved except slant-detected subheads, per S7 to S13.
- Dropped: nothing. No running footer "OceanofPDF.com" in range.

## Footnotes

Two markers in range: `[^74]` (p.419, md line 11, after "the Pareto principle,") and `[^75]` (p.436, md line 269, after “ruinous empathy.”). Note 76 falls on p.450 (S15). The note texts are in the Chapter 5 notes section on book p.483 (the note numbers and texts are separate text blocks; matched by y position). Noted there, not extracted:

- 74: “Pareto Principle,” Wikipedia (URL, last modified January 21, 2022). **Citation.**
- 75: Scott, Radical Candor, 32–33. **Citation.**

Neither is substantive. (For reference, 76 is “Five Whys,” Wikipedia, a citation, S15's.)

## Counts

- Em dashes in the md page bodies (context lines excluded): 20, matching raw from the head "Managing high performers" to the end of p.448 (20). One en dash ("10–20 percent", p.428).
- "guest": 0 occurrences in range (book and workbook).

## Book: verification

- NUL bytes: 0. U+FFFD: 0 (in the md and in `book-raw.txt`).
- Page markers: all 30 present, in order, 419 to 448.
- Word-for-word comparison of every page against raw `page.get_text()` (whitespace-normalized; line-end hyphens and em dashes joined; markdown syntax removed: heading hashes, list dashes, blockquote markers, continuation indent, `**`; `[^N]` compared as N; the p.419 S13 lines before the head excluded; both bracketed context lines excluded): 8,269 raw words over pp. 419 to 448. **All 30 pages identical.** No reordering, no dropped or added words.
- The two context lines were built from the p.419 and p.449 text layers (line breaks joined, "customer-/facing" joined as a compound) and match them verbatim.

## Figures and numbers in her material

The program never reproduces financial figures. Across book pp. 419 to 448 and workbook pp. 118 to 123 there is **no monetary amount, no percentage of pay, no salary band figure, no equity figure, no compensation formula, and no headcount threshold**. Places that name a pay element or state a number that could be read as financial, so the synthesis writer can steer around them:

| Page | md line | What it says | Financial? |
|---|---|---|---|
| Book 419 | 11 | A CFO's 80-20 rule: "20 percent of employees do 80 percent of the work" | No: a claim about workload share, not money (the speaker is a CFO) |
| Book 420 | 23 | Pushers use reviews to ask why they "aren’t getting a larger raise" | Names a pay element; no figure |
| Book 421 to 422 | 59, 63 | To support pushers: "Encourage and reward them... Promote them." / "Give them raises." | Names a pay element; no figure |
| Book 427 | 161 | Interview "your top 10 percent of talent" once a year | No: a talent share |
| Book 428 | 167 | "Your top 10–20 percent of performers make or break your company" | No: a talent share |
| Book 431 | 207 | Terminal level: "might not get promoted beyond, say, Level 4" | No: a job level, not a band figure |
| Book 432 | 211 | Celebrate consistent performance, "which may look less like compensation rewards and more like verbal recognition and special assignments" | Names compensation; no figure |
| Book 432 | 221 | The organization "has already expended a big cost on recruiting, hiring, and onboarding" a low performer | Names a cost; no figure |
| Book 433 | 231 | "financial hardship" as an edge case in an employee's personal life | Not company finance; no figure |
| Book 440 | 351 | Denial should be "a small percentage (say, 10 percent) of responses" | No: a share of conversations |
| Book 445 | 431 | Operational fixes include "meeting sales quotas"; a quota may need time "because most sales deals close by the end of a set period, usually a quarter" | Names sales quotas; no figure |
| Book 448 | 465 | Employees who refuse to believe the feedback exit "99 percent of the time" | No: an outcome rate |

Non-financial numbers that could be mistaken for thresholds (listed for completeness): phase timings "less than three weeks", "one to three conversations, two weeks", "one to two conversations, one week", "one to three months" (book 438, md lines 291 to 303); "no more than three months", "one month" to resolve a performance issue (book 437, md line 277); PIP tracking "over the next 30 days" (book 444, md lines 401 and 403); assess fit "within one to two months", behavioral fit "within two or three weeks" (book 445 to 446, md lines 433 and 439); "at least two or three feedback conversations" before a PIP (book 434, md line 249); "three to five" pre-exit conversations (book 427, md line 161); "peer feedback from five people" (book 446, md line 441); "six months" horizons (book 423, 429, 430); "five years" (book 425). Workbook: PIP duration "typically four to six weeks" (p.118); "3–5 points" of role expectations (p.119); "[X] weeks" (p.121). The only headcount threshold near the range is S13's "Once you exceed 20 or 30 employees" (p.419, inside the S13 context line, md line 7).

## Workbook: census and pointer

S12's census (`extraction/s12/workbook-ch5.md` lines 5 to 15; `extraction/s12/extraction-notes.md` workbook section) holds and was re-checked against the PDF. Chapter 5 exercises by session:

| Exercise | Workbook pages | Session | Where extracted |
|---|---|---|---|
| Performance Review Template | 104 to 110 | S13 | `extraction/s13/workbook-ch5.md` |
| Compensation Conversations Preparation and Guide | 111 to 112 | S13 | `extraction/s13/workbook-ch5.md` |
| Performance Improvement Documentation Templates (Initial documentation of feedback after meeting; Progress update; Employee getting back on track; Insufficient progress (after a reasonable period); Notes) | 113 to 117 | **S14** (low performers: the documentation emails the book's "Document your discussion" points to; S12 also used them) | Already in full at **`extraction/s12/workbook-ch5.md` lines 29 to 133**; not re-extracted |
| Performance Improvement Plan Template (preamble; four-page PIP form; Notes) | 118 to 123 | **S14** (Potential outcome 1, the PIP) | **Extracted here**, `extraction/s14/workbook-s14.md` (was missing) |
| Managing Out Checklist (eight steps) | 124 | S15 (managing out) | Not extracted |

There is no workbook exercise on high performers, pushers and pullers, or medium performers. The book's appendix carries the same two S14 exercises at PDF pp. 474 to 476 (documentation templates) and 477 to 481 (PIP template).

Workbook extraction (`workbook-s14.md`), handled per S12's conventions:
- Fonts: Neue Haas Grotesk (`NHaasGroteskTXPro-55Rg`, `-75Bd`); running head 6.5pt (dropped). Sizes: 36.0 title (p.118); 18.0 section head "Performance improvement plan" (p.119); 8.5 body, bold 8.5 form labels (Role expectations, Areas for improvement, Area of improvement 1 to 3 (twice), Improvement goals and targets, Milestones, Resources, Progress checks and evaluation, Summary) and bold "Notes" (pp. 118, 123); 8.0 signature labels (p.122); 5.0 form page counters "1/4" to "4/4".
- Ruled boxes: p.118 a Notes frame (y 504 to 756); pp. 119 to 122 one form frame each (x 72 to 492, y 126 to 667), rendered as one blockquote between `[Boxed form]` and `[End boxed form]`, split at the page markers; p.122 two short signature rules (y 531, 583); p.123 a full-page Notes frame.
- The form's bold labels are `**bold**` lines inside the blockquote (not headings), since they sit inside the boxed form. Bullets rebuilt as `> - ` items. Form page counters kept as `[Form page N/4]`.
- Line-end hyphens rejoined and dropped: suc-cessfully (p.118); improve-ment, fol-lowing, com-pany, per-son (p.119); dead-lines, en-courage, dis-cuss, guar-antees, na-ture (p.121); perfor-mance (p.122). "at-will" kept.
- Verification: word comparison of pp. 118 to 123 against raw `get_text()` (running head and page number removed; bullets removed; hyphen breaks joined; bracketed markers removed): pp. 118 to 121 and 123 identical; p.122 same words, the "4/4" counter moved from its text-layer position (before the signature labels) to its printed position (y 652, below them).
- Content notes for the synthesis writer: the PIP preamble calls the PIP "a signed, standalone document"; the form states that the PIP "does not change the at-will nature of your employment" and that the manager "may terminate the PIP at any time prior to its conclusion" (US employment-law framing; the preamble notes the template "may need to be adapted for different geographical jurisdictions").

## Anomalies and uncertainties

1. The top of p.419 is S13's material (context line, md line 7). The top of p.449 is S14's material by content (context line, md line 471); S15 should not re-extract it as its own.
2. Heading levels follow typography and invert the content nesting inside "Phases of managing low performers" (see heading-level notes).
3. "Potential outcome 3" (leaving the company) has no section in range; the book defers it to "managing out, firing, and layoffs" (S15).
4. The two monospace passages share the Type3 font name with the body; they were identified by fixed character advance and confirmed by render.
5. The PIP Template (workbook pp. 118 to 123) was not in S12's or S13's extractions and is extracted here; the documentation templates (pp. 113 to 117) are pointed to, not repeated.
