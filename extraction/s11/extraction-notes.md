# Session 11 extraction notes

Mechanical extraction for Session 11 (Ch4: Team-building complexities, Diversity and inclusion, Team communication, Exercises and templates, Notes). Sources read only; nothing in `sources/` was modified.

## Outputs

| File | Lines | Content |
|---|---|---|
| `extraction/s11/book-331-380.md` | 892 | Book pp. 331 to 380, 50 page markers, plus one bracketed context line (the p.330 subhead "Thursday afternoon: one hour") above the first marker |
| `extraction/s11/book-raw.txt` | 1,629 | Raw `page.get_text()` per page, pp. 331 to 380, with `===== Book page N =====` separators |
| `extraction/s11/figures/` | n/a | Empty: no image blocks or figures in this range |

No workbook extraction in this pass (the book's Chapter 4 exercises are compared against S8's `extraction/s08/workbook-ch4.md` below).

## Page mapping and boundaries

- Book: PDF page N = book page N (zero offset), as `reference/chapter-map.md` states and as S8 to S10's markers use. Confirmed again here: p.331 opens with the paragraph whose subhead ends p.330 in S10's extraction; the 21.2pt heads "Team-building complexities" (p.331), "Diversity and inclusion" (p.354) and "Team communication" (p.360), the "EXERCISES AND TEMPLATES" label (p.363) and the 25pt "Notes" head (p.378) all fall exactly where the chapter map puts them.
- Start boundary (p.331): S10's md (line 487) already carries p.331's first paragraph as context. Here all of p.331 is extracted in full: the paragraph "This is more of a creator meeting; ... that can’t wait until Monday." (md line 9), the bold italic subhead "Offsites: two full days every quarter" (md line 11, `####`, the third item of Stripe’s leadership meeting cadence, same level as S10's "Monday morning: three hours" and "Thursday afternoon: one hour"), its two paragraphs, then the 21.2pt section head "Team-building complexities" at the foot of the page (y 661.8; md line 17). The p.330 subhead "Thursday afternoon: one hour" is given as a bracketed context line above the first page marker (md line 5), outside the page markers, following S9's placement of cross-boundary context.
- End boundary (p.380): p.380 ends the Chapter 4 notes. It holds notes 65 and 66 only, then the running footer "OceanofPDF.com" (dropped). p.381 is not in range and opens Chapter 5: it is the full-page chapter opener image (one image block, "5 / Core Framework 4 / Feedback and Performance Mechanisms", plus the running footer), where the chapter map puts S12's start. Nothing from p.381 is included.
- Chapter 4 notes run 40 to 66. Note 40 is the first note of the chapter (p.264), so the notes section on pp. 378 to 380 is complete for Chapter 4 and contains no notes from other chapters.

## Book: tool, font census, layouts

PyMuPDF 1.26.5 only (`page.get_text("dict")`), no pypdf. Two typographic systems:

1. Prose pp. 331 to 362 and notes pp. 378 to 380: one Type3 font (`Unnamed-T3`), color 0 and flags 0 on every glyph span except footnote superscripts (flags 1). Sidebar blue appears only on inter-word space spans (color 3366828) and in the rendered ink; sidebars were delimited by their printed "SIDEBAR" label and closing short rule, as in S8. Bold was detected by rendered stroke width and italic by rendered glyph slant (method below).
2. Exercises pp. 363 to 377: set in real fonts (`NHaasGroteskTXPro-55Rg`, `-65Md`, `-75Bd`, `-56It`) on a lavender panel (fill RGB 0.93, 0.93, 1.0), with a few Type3 passages (the checkbox glyphs "□", the monospace welcome-email template on p.369, and the agenda table cells on pp. 369 to 370) and two `LiberationSerif` spans (p.370 "quarter and DRIs"; the ellipsis in the Solnit quote on p.350). Bold on these pages was read from font flags (bit 16) and checked against renders.

Size census, pp. 331 to 380 (span counts; spans are roughly word-level, spaces included):

| Size (pt) | Spans | Role |
|---|---|---|
| 15.0 | 16,744 | Body text; bold subheads (roman and italic); bold list lead-ins; sidebar body; exercise subheads (bold, real font) |
| 11.2 | 1,987 | Table 9 cell text and caption (pp. 336 to 337); SIDEBAR labels; exercise body text and checklist items; agenda table; Chapter 4 notes (pp. 378 to 380) |
| 21.2 | 34 | Section heads "Team-building complexities", "Diversity and inclusion", "Team communication"; sidebar titles "The challenges of collaborating across time zones" (two lines) and "Reid Hoffman on managing through crisis" |
| 8.7 | 13 | Footnote superscripts 54 to 66 |
| 30.0 | 7 | Exercise page head "Chapter 4" and exercise titles |
| 16.9 | 7 | Exercise section subheads (Duration, Approach, Planning checklist, Day-of-offsite templates, First, try to solve locally, How to unblock, Fictional example document) |
| 25.0 | 1 | "Notes" head (p.378) |

Per page:

| Page | Span counts by size | Other |
|---|---|---|
| 331 | 15.0: 498; 21.2: 3 | Section head at foot of page |
| 332 | 15.0: 472 | |
| 333 | 15.0: 453; 21.2: 12; 11.2: 1 | 3 bullet marks; SIDEBAR label and rule; blue sidebar begins (italic intro) |
| 334 | 15.0: 516; 8.7: 1 | Sidebar ends (printed numbered list 1 to 2; closing rule y 375.8) |
| 335 | 15.0: 566 | |
| 336 | 11.2: 289; 15.0: 212 | Table 9 begins: header fill (RGB 0.94, 0.94, 0.97) y 345 to 392, blue rules |
| 337 | 15.0: 325; 11.2: 104 | Table 9 ends (to y ~215), caption y 245.2; 3 bullet marks |
| 338 | 15.0: 586 | |
| 339 | 15.0: 498 | 2 bullet marks |
| 340 | 15.0: 618 | |
| 341 | 15.0: 578; 8.7: 1 | |
| 342 | 15.0: 567; 8.7: 2 | |
| 343 to 345 | 15.0 only | |
| 346 | 15.0: 563 | 7 bullet marks |
| 347 | 15.0: 588 | |
| 348 | 15.0: 538; 8.7: 1 | 2 bullet marks |
| 349 | 15.0: 598 | 2 bullet marks |
| 350 | 15.0: 520; 8.7: 1 | |
| 351 | 15.0: 605 | |
| 352 | 15.0: 515; 21.2: 11; 11.2: 1 | SIDEBAR label and rule; blue sidebar begins (italic intro) |
| 353 | 15.0: 537 | Sidebar continues; 2 bullet marks |
| 354 | 15.0: 568; 21.2: 5; 8.7: 1 | Sidebar ends (closing rule y 302.3); section head |
| 355 | 15.0: 596; 8.7: 1 | |
| 356 | 15.0: 457; 8.7: 1 | 3 bullet marks |
| 357 | 15.0: 570; 8.7: 1 | |
| 358 | 15.0: 574 | |
| 359 | 15.0: 577; 8.7: 2 | |
| 360 | 15.0: 440; 21.2: 3; 8.7: 1 | 3 bullet marks; section head |
| 361 | 15.0: 564 | |
| 362 | 15.0: 467 | |
| 363 | 11.2: 12; 15.0: 1; 30.0: 1 | Exercises divider page (label, rule, "Chapter 4", contents list, workbook URL) |
| 364 | 11.2: 26; 16.9: 2; 30.0: 1; 15.0: 1 | Career Conversations begins; numbered steps with indented scripts (x=140) |
| 365 | 11.2: 30; 15.0: 3 | Script continues; question subheads (bold 15.0 at x=119) |
| 366 | 11.2: 24; 15.0: 9 | |
| 367 | 11.2: 25; 15.0: 3; 30.0: 2; 16.9: 1 | Wrap-up; Planning and Running Your Offsite begins; 7 checkbox glyphs |
| 368 | 11.2: 34; 15.0: 4; 16.9: 1 | 15 checkbox glyphs |
| 369 | 11.2: 216; 15.0: 3 | Printed numbered list; monospace welcome-email template (Type3, "Purpose" and "Logistics" underlined); agenda table begins (header row filled blue, white bold text; first column bold) |
| 370 | 11.2: 159; 30.0: 2 | Agenda table ends; Leadership Team Snippets and Updates begins |
| 371 | 11.2: 18; 15.0: 6 | 14 bullet dots (one nested at x=127.5) |
| 372 | 11.2: 20; 15.0: 2; 30.0: 1; 16.9: 1 | 8 bullet dots; Stripe’s Unblocking Process begins |
| 373 | 11.2: 38; 16.9: 1 | Numbered steps with sub-items labeled 1.1 to 2.3 |
| 374 | 11.2: 31; 15.0: 3 | Numbered lists; bold question lead-ins |
| 375 | 11.2: 33; 15.0: 1 | Example narrative |
| 376 | 16.9: 1; 15.0: 1; 11.2: 25 | Stroked box (99, 117, 513, 803) holding the fictional document; 3 bullet dots |
| 377 | 11.2: 18 | Box continues (to y 155); 1 bullet dot; closing narrative |
| 378 | 11.2: 323; 25.0: 1 | Notes head; notes 40 to 51 |
| 379 | 11.2: 498 | Notes 52 to 64 |
| 380 | 11.2: 62; 15.0: 1 | Notes 65 to 66; running footer "OceanofPDF.com" (15.0, dropped) |

### Bold and italic detection (Type3 pages)

- Bold: per span mean horizontal stroke width (dark-pixel run length, grayscale render at 4x, threshold 128), normalized to 15pt. Cut set at 8.2 px (S9 and S10 used 7.95). Reason: in this range regular spans reach 8.01 to 8.11 px on isolated tokens ("Be" p.346 twice, "5" pp. 346 and 347, "HR" p.347), while the lightest true bold span is 8.32 ("every", p.331 subhead) and bold lead-ins measure 9.7 to 11.4. With the cut at 8.2 no single-word false bold occurs, so S10's isolated-word reset rule was not needed. Non-alphanumeric and space spans take bold only when both neighbors are bold. Footnote superscripts (flags 1) are excluded.
- Italic: every fully bold 15.0pt line and every sidebar line was tested for glyph slant (shear that maximizes the column projection of ink). Bold italic subheads and the two sidebar intro paragraphs measure shear 0.20; bold roman heads, body and the rest of the sidebar text measure -0.04 to 0.02; the section heads are roman.
- Sidebar body text renders lighter (blue), stroke width 4.2 to 5.9 px; no bold occurs inside either sidebar.

### Heading map used

- Prose: 21.2 black as `##`; 15.0 bold roman as `###`; 15.0 bold italic as `####`; sidebar title (21.2 blue) as `###` inside `[Sidebar]` / `[End sidebar]`; sidebar intro paragraph (italic) as `*italic*`, per S8. Inline bold lead-ins as `- **Lead-in.** text`, per S7 to S10.
- Exercises (per S7's exercise convention): the section as `## Exercises and templates` with `[Section label in source: "EXERCISES AND TEMPLATES"]`; "Chapter 4" (30.0) as `###`; exercise titles (30.0) as `###`; 16.9 bold as `####`; 15.0 bold as `#####`; 11.2 bold labels ("Script:", box field labels, "Actions status:", the three unblocking questions) kept as `**bold**`.
- Notes: 25.0 "Notes" as `## Notes`, per S7.

## Book: image blocks and figures

None in range. `get_images` is empty on every page 331 to 380, and no vector figures occur: the only non-glyph vector graphics are Table 9 and the agenda table rules and fills, the exercise panel fill, the stroked box on pp. 376 to 377, the sidebar rules, bullet marks, and footnote marks (Type3 glyphs also appear as filled paths in `get_drawings`). `extraction/s11/figures/` is empty. The first image block after the range is the Chapter 5 opener on p.381.

## Book: tables

- Table 9, "Types of remote teams and challenges" (pp. 336 to 337): two columns (TYPE OF REMOTE TEAM, PRIMARY CHALLENGE), four rows. Column bands from the rules (x 77.25, 189.75, 534.0); row bands from the rules (y 345.0, 392.25, 471.0, 612.75, then off the page). The third row's left cell ("A team split across two or three different offices and some remote locations, or" / "two teams that need to work across locations") breaks across the page; split at the page marker with "(cont.)" headers per S8 (md lines 93 to 97 and 101 to 104), caption at line 106 as `[caption] Table 9. ...`. Cell text is a monospace face in print, no bold; header cells bolded in md per S8 convention.
- Offsite agenda (pp. 369 to 370, under `##### Agenda`): five columns (Session, What we’ll be doing, Time, Length, Facilitator), eleven rows. Rebuilt from cell geometry (column bands x 98.2, 174.8, 335.2, 378.8, 437.2, 513.0). The "Break / Take a stretch / 11 a.m. / 15 minutes" row breaks across the page ("11", "15" on p.369; "a.m.", "minutes" on p.370); split at the marker with "(cont.)" headers (md lines 617 to 621 and 625 to 635). Header cells are bold in print (white on blue); first-column cells are bold in print and are bolded in md. No caption.

## Book: other handling

- Sidebars: "The challenges of collaborating across time zones" (pp. 333 to 334, md lines 45 to 65) and "Reid Hoffman on managing through crisis" (pp. 352 to 354, md lines 306 to 334). The SIDEBAR label and short rule are converted to `[Sidebar]`, the closing rule to `[End sidebar]`. Monospace code words in the first sidebar ("admin-plans-readers", pp. 333 to 334) are kept as plain text, not backticked. The first sidebar's numbered list (p.334) keeps its printed numerals.
- Exercise formatting: Career Conversations scripts (x=140) as blockquotes headed `> **Script:**` (md lines 465 to 479; the second script continues across the p.364 to 365 break and is split at the marker). The offsite welcome-email template (monospace, p.369) as a blockquote (md lines 603 to 613); the underlined labels "Purpose" and "Logistics" are kept as plain lines. Checklist items keep their printed checkbox glyph as `- □ item` (22 items, pp. 367 to 368). The unblocking sub-items keep their printed labels as nested items `   - 1.1 ...` to `   - 2.3 ...` (md lines 730 to 737). The fictional example document (stroked box, pp. 376 to 377) as a blockquote (md lines 789 to 822), split at the page marker, closed with `[End of boxed document]` (md line 824); its three author lines are joined with `<br>`.
- Printed "?" artifact: six unblocking sub-items on pp. 373 to 374 end with a stray "?" after their final period or parenthesis ("user).?", "considered.?", "help.?", "managers.?", "meeting.?", "overflows).?"). The "?" is printed on the page (visible in the render), not an extraction error; kept as printed. The workbook version (S8) does not have it.
- Other printed oddities kept as printed: "career conversion" for "career conversation" (p.355); "entrance.code" (p.368); cross-references that do not match PDF pages ("Table 9 on page 314" on p.333 refers to PDF pp. 336 to 337; "Table 6 on page 265" on p.349; "the chapter appendix on page 343" on p.349 refers to Stripe’s Unblocking Process at PDF p.372).
- Lists: 27 bullet marks (4.5pt filled squares at x=84) on prose pages became `- ` items; continuation lines at the item's text x (98) were joined into the item. On the exercise pages, 26 round 3.75pt bullet dots became `- ` items (the nested one at x=127.5 on p.371 and the three at x=143.2 in the box as indented items). Printed numbered lists keep their numerals.
- Paragraph breaks: first-line indent (x=98) or a vertical gap greater than 26pt on prose pages; gaps on exercise pages. Two exercise paragraphs that start a new line without a gap were split by sentence start ("Focus more on what their future work..." p.366; "This section ends up being useful..." p.367).
- Items and paragraphs that break across pages are split at the page marker, per S8 to S10; a continuation after the marker is a plain paragraph without a bullet (e.g., p.334 to 335, p.335 to 336, p.337 to 338, p.341 to 342, p.342 to 343, p.343 to 344, p.344 to 345, p.346 to 347, p.347 to 348, p.349 to 350, p.350 to 351, p.351 to 352, p.352 to 353 inside the sidebar, p.353 to 354, p.354 to 355, p.355 to 356, p.356 to 357, p.357 to 358, p.358 to 359, p.361 to 362, p.364 to 365, p.366 to 367, p.372 to 373, p.373 to 374 inside sub-item 2.3, p.374 to 375).
- Justified lines the text layer split into single-word lines (p.352 "acting on what we knew. From there, we methodically"; p.352 "conversation about leadership and management at"; p.355 "a diverse team also has less visually noticeable qualities.") were re-merged by baseline.
- Footnotes: 13 markers, `[^54]` (p.334), `[^55]` (p.341), `[^56]` and `[^57]` (p.342), `[^58]` (p.348), `[^59]` (p.350), `[^60]` (p.354), `[^61]` (p.355), `[^62]` (p.356), `[^63]` (p.357), `[^64]` and `[^65]` (p.359), `[^66]` (p.360). Note texts are in range (pp. 378 to 380) and given as `NN. text` entries.
- Hyphenation: line-end hyphens in the prose and exercises are all true compounds, kept and joined without a space: "high-growth" (p.332), "owner-approved" (p.333), "admin-plans-readers" (p.333 to 334), "cats-and-dogs" (p.336), "60-minute" (p.339), "relationship-building" (p.341), "all-remote" (p.342), "non-in-person" (p.344), "Post-lunch", "pre-reads", "team-building" (agenda, p.370), "company-wide" (p.371), "mass-market" (p.375). URL line breaks in the notes were joined without a space. Line-end em dashes joined without a space.
- Italics other than sidebar intros and slant-detected subheads are not preserved (e.g., book titles in the notes, the snippets template instruction on p.370), per S7 to S10.
- Dropped: running footer "OceanofPDF.com" (p.380); the decorative short rules (SIDEBAR rules and the p.363 rule under the section label); the exercise panel fill.

## Counts requested

- Em dashes in the md page bodies: 41 (raw text has 46; the 5 extra are the decorative "—" rules under the two SIDEBAR labels, the two sidebar closing rules, and the rule under the p.363 label). By page: 331: 1; 334: 1; 336: 3; 340: 1; 341: 3; 345: 2; 347: 6; 348: 1; 349: 2; 350: 1; 352: 1; 355: 2; 356: 3; 358: 3; 359: 2; 360: 1; 364: 1; 365: 1; 367: 2; 369: 1; 372: 1; 373: 2. Also 5 en dashes (ranges).
- "guest": 1 occurrence, p.371, Leadership Team Snippets and Updates template, discussion-topics item "User guest (10 mins)" (md line 655). No other occurrence in range.

## Book: verification

- NUL bytes: 0. U+FFFD: 0 (both in the md and in `book-raw.txt`).
- Page markers: all 50 present, in order, 331 to 380.
- Word-for-word comparison of every page against raw `page.get_text()` (whitespace-normalized; line-end hyphens and dashes joined; markdown syntax, `<br>`, table separator rows, "(cont.)" header rows, `[Sidebar]`, `[End sidebar]`, `[End of boxed document]` and `[caption] ` removed; `[^N]` compared as N; the context line excluded): 12,913 raw words over 50 pages. 39 pages identical. 11 pages differ, all intentional or ordering artifacts, with no dropped or added words:
  - pp. 333, 352: the SIDEBAR label and its rule converted to `[Sidebar]`; pp. 334, 354: the closing rule converted to `[End sidebar]` (the raw joiner attaches the rule to the next word, "—Cohesion", "—Diversity").
  - p.363: the `## Exercises and templates` heading added (the printed label is kept as the section-label line); the rule under the label dropped.
  - pp. 367, 368, 373, 378, 379, 380: same words in a different order (multiset-equal). The raw text layer emits the checkbox glyphs (pp. 367, 368), the sub-item labels 1.1 to 2.3 (p.373) and the note numbers (pp. 378 to 380) as a block before the text; the md places each beside its item. p.378 also emits "Notes" after the numbers.

## Exercises: book versus workbook (S8 `extraction/s08/workbook-ch4.md`)

Word-level diff of each book exercise (md ranges below) against the workbook extraction:

| Book exercise | Book pages | Book md lines | Workbook counterpart | Workbook md lines | Result |
|---|---|---|---|---|---|
| Career Conversations | 364 to 367 | 453 to 519 | Career Conversations (workbook pp. 90 to 92) | 18 to 85 | Identical text (similarity 0.998); the workbook adds a blank "Notes" area |
| Planning and Running Your Offsite (planning checklist, day-of-offsite templates, welcome email, agenda) | 367 to 370 | 521 to 635 | Planning and Running Your Offsite (workbook pp. 93 to 95) | 88 to 203 | Identical text; differences are checkbox rendering (`[ ]` in the workbook md, `□` here), the agenda table's page split, and the workbook's "Notes" area |
| Leadership Team Snippets and Updates | 370 to 372 | 637 to 705 | Leadership Team Snippets and Updates (workbook pp. 96 to 97) | 204 to 275 | Identical text; the workbook adds a "Notes" area |
| Stripe’s Unblocking Process (incl. example and fictional document) | 372 to 377 | 707 to 832 | Stripe’s Unblocking Process (workbook pp. 98 to 102) | 278 to 418 | Identical text except the book's six stray "?" after the unblocking sub-items (see above), absent in the workbook; workbook adds "Notes" areas |

No book exercise lacks a workbook counterpart, and none differs materially. The book's p.363 contents list names the same four exercises as the workbook's Chapter 4 divider (workbook md lines 7 to 15).

## Footnotes by session range

Chapter 4 notes are 40 to 66 (notes section pp. 378 to 380). Superscript pages were located in the PDF (flags-1 spans) and cross-checked against the S8, S9, S10 and S11 extractions; all agree.

| Session | Pages | Notes | Superscript pages |
|---|---|---|---|
| S8 | 261 to 281 | 40 | 40 (p.264) |
| S9 | 282 to 303 | 41 to 43 | 41 (p.283), 42 (p.284), 43 (p.300) |
| S10 | 304 to 330 | 44 to 53 | 44, 45 (p.306); 46 (p.308); 47, 48 (p.312); 49 (p.319); 50, 51, 52 (p.326); 53 (p.329) |
| S11 | 331 to 380 | 54 to 66 | 54 (p.334); 55 (p.341); 56, 57 (p.342); 58 (p.348); 59 (p.350); 60 (p.354); 61 (p.355); 62 (p.356); 63 (p.357); 64, 65 (p.359); 66 (p.360) |

Note text md lines in `book-331-380.md`: 40 to 51 at lines 836 to 858 (p.378), 52 to 64 at lines 862 to 886 (p.379), 65 and 66 at lines 890 and 892 (p.380). Note 58 is a substantive note (Carol Dweck via Frances Frei, "prepare the child for the path"), not a citation.

## Anomalies

1. Printed cross-references run behind PDF pages, consistent with S8 to S10 (see "Other handling").
2. Headings are mapped by typography. "Coordination", "Cohesion", "Participation" are bold roman `###`, the same level as "Managing distributed and remote teams"; the mitigation subheads that follow Table 9 ("Set structures and norms for inclusive meeting practices", "Level the playing field", "Make room for in-person time") are bold italic `####`, as are the four remote-worker factors and the course-correct steps.
3. "Set structures and norms for inclusive meeting practices", "Level the playing field" and "Make room for in-person time" each appear twice on p.337 to 339: first as bold lead-ins in a three-item list (p.337), then as `####` subheads.
4. The first sidebar's numbered list and the Reid Hoffman sidebar's bullets sit inside `[Sidebar]` blocks; the Hoffman sidebar is written in Hoffman's first person, not the author's.
5. The six stray "?" on pp. 373 to 374 are printed in the book (see "Other handling").
6. Table header cells and the agenda's first column are bolded in md; Table 9 is not bold in print.

## Table of contents: book (`book-331-380.md`)

| Page | Headings and topics | md lines |
|---|---|---|
| (330) | Context: subhead "Thursday afternoon: one hour" | 5 |
| 331 | Thursday paragraph; `#### Offsites: two full days every quarter`; distributed leadership team; `## Team-building complexities` | 9 to 17 |
| 332 | `### Managing distributed and remote teams`; three challenges; `### Coordination` | 21 to 33 |
| 333 | Audit (3 bullets, Table 9 pointer); `[Sidebar]` `### The challenges of collaborating across time zones` | 37 to 51 |
| 334 | Sidebar cont. (two learnings, numbered); `[End sidebar]`; `### Cohesion` (remote hub `[^54]`) | 55 to 71 |
| 335 | Cohesion cont.; `### Participation` | 75 to 83 |
| 336 | Documentation; Slack hallway; Table 9 begins | 87 to 97 |
| 337 | Table 9 cont. and caption; three mitigations (3 bullets); `#### Set structures and norms for inclusive meeting practices` | 101 to 118 |
| 338 | `#### Level the playing field` (remote meeting scenario; Automattic) | 122 to 128 |
| 339 | Stripe hardware and Slack norm; `#### Make room for in-person time` (2 bullets) | 132 to 140 |
| 340 | Revenue leads group; how often to meet in person | 144 to 148 |
| 341 | `### Going global` (Hofstede `[^55]`) | 152 to 160 |
| 342 | Cultural comparison at Stripe; `### Adding remote workers` (`[^56]` `[^57]`); `#### Maturity of operating system` | 164 to 174 |
| 343 | `#### Role`; `#### Manager support` | 178 to 188 |
| 344 | `#### Experience level`; intentional foundations | 192 to 198 |
| 345 | `### Underperforming teams`; `#### Investigate the root cause...`; `#### Have an open conversation...` | 202 to 216 |
| 346 | Four team questions (4 bullets); wrong goal steps (3 bullets); skill or collaboration issues | 220 to 236 |
| 347 | Collaboration conflicts; fractious team; dependencies | 240 to 244 |
| 348 | Clearing the path `[^58]`; `### Working with other teams` (2 bullets) | 248 to 256 |
| 349 | Embed, working group (2 bullets); constructive escalation; unblocking pointer | 260 to 268 |
| 350 | `### Managing through uncertainty` (Solnit `[^59]`); `#### Be transparent, to a point` | 272 to 284 |
| 351 | `#### Reiterate the vision`; `#### Move forward`; Covid example | 288 to 298 |
| 352 | Covid example cont.; `[Sidebar]` `### Reid Hoffman on managing through crisis` | 302 to 312 |
| 353 | Facebook Platform test (2 bullets) | 316 to 326 |
| 354 | Bumper Stickers; `[End sidebar]`; `## Diversity and inclusion` (`[^60]`) | 330 to 340 |
| 355 | Psychological safety `[^61]`; less visible diversity; getting to know the team | 344 to 348 |
| 356 | Three areas (3 bullets); Coqual `[^62]`; `### Hiring` | 352 to 368 |
| 357 | BCG `[^63]`; `### Performance assessment, reward, and recognition` | 372 to 380 |
| 358 | Equitable processes; `### Running teams` | 384 to 390 |
| 359 | Unleashed `[^64]`; Foster Wallace `[^65]`; shared qualities | 394 to 398 |
| 360 | Valdary `[^66]` (3 bullets); `## Team communication` | 402 to 416 |
| 361 | Formalizing information-sharing; pass-downs | 420 to 426 |
| 362 | Snippets doc; end-of-day communication | 430 to 434 |
| 363 | `## Exercises and templates`; `### Chapter 4` (contents, workbook URL) | 438 to 449 |
| 364 | `### Career Conversations`; Duration; Approach; Pre-conversation (2 steps, 2 scripts) | 453 to 473 |
| 365 | Script cont.; `##### Conversation`; question subheads | 477 to 491 |
| 366 | Question subheads cont. | 495 to 509 |
| 367 | `##### Wrap-up`; `### Planning and Running Your Offsite`; checklist (1+ month, 1 month) | 513 to 543 |
| 368 | Checklist (1 week, 1 day, day of, after); `#### Day-of-offsite templates` | 547 to 585 |
| 369 | Offsite structure; welcome email template; `##### Agenda` table begins | 589 to 621 |
| 370 | Agenda cont.; `### Leadership Team Snippets and Updates` | 625 to 641 |
| 371 | Actions; Discussion topics; Standing questions; Customer issues | 645 to 681 |
| 372 | Customer wins; Snippets; `### Stripe’s Unblocking Process`; `#### First, try to solve locally` | 685 to 715 |
| 373 | Unblocking rationale; `#### How to unblock` (steps 1 to 2, sub-items 1.1 to 2.3) | 719 to 737 |
| 374 | Bilateral vs unilateral; request to unblock; unilateral request questions | 741 to 763 |
| 375 | `##### Example` (Charlie, Alice, Chun, Aiden, Bharath) | 767 to 783 |
| 376 | `#### Fictional example document` (boxed "Stripe alignment model") | 787 to 818 |
| 377 | Box ends; resolution by Bharath | 822 to 830 |
| 378 | `## Notes`; notes 40 to 51 | 834 to 858 |
| 379 | Notes 52 to 64 | 862 to 886 |
| 380 | Notes 65 to 66 | 890 to 892 |

## Full heading list (`book-331-380.md`)

| md line | Page | Heading |
|---|---|---|
| 1 | n/a | `# Scaling People, book pages 331 to 380 (Ch4: Team-building complexities, Diversity and inclusion, Team communication, Exercises and templates, Notes)` |
| 11 | 331 | `#### Offsites: two full days every quarter` |
| 17 | 331 | `## Team-building complexities` |
| 23 | 332 | `### Managing distributed and remote teams` |
| 31 | 332 | `### Coordination` |
| 47 | 333 | `### The challenges of collaborating across time zones` |
| 67 | 334 | `### Cohesion` |
| 79 | 335 | `### Participation` |
| 116 | 337 | `#### Set structures and norms for inclusive meeting practices` |
| 124 | 338 | `#### Level the playing field` |
| 134 | 339 | `#### Make room for in-person time` |
| 154 | 341 | `### Going global` |
| 168 | 342 | `### Adding remote workers` |
| 172 | 342 | `#### Maturity of operating system` |
| 180 | 343 | `#### Role` |
| 184 | 343 | `#### Manager support` |
| 194 | 344 | `#### Experience level` |
| 204 | 345 | `### Underperforming teams` |
| 210 | 345 | `#### Investigate the root cause by asking some probing questions` |
| 214 | 345 | `#### Have an open conversation about the issue in your team meeting` |
| 250 | 348 | `### Working with other teams` |
| 274 | 350 | `### Managing through uncertainty` |
| 280 | 350 | `#### Be transparent, to a point` |
| 290 | 351 | `#### Reiterate the vision` |
| 294 | 351 | `#### Move forward` |
| 308 | 352 | `### Reid Hoffman on managing through crisis` |
| 336 | 354 | `## Diversity and inclusion` |
| 364 | 356 | `### Hiring` |
| 376 | 357 | `### Performance assessment, reward, and recognition` |
| 388 | 358 | `### Running teams` |
| 412 | 360 | `## Team communication` |
| 438 | 363 | `## Exercises and templates` |
| 442 | 363 | `### Chapter 4` |
| 453 | 364 | `### Career Conversations` |
| 455 | 364 | `#### Duration` |
| 459 | 364 | `#### Approach` |
| 461 | 364 | `##### Pre-conversation` |
| 481 | 365 | `##### Conversation` |
| 487 | 365 | `##### Tell me about where you grew up.` |
| 491 | 365 | `##### Tell me about where you went to school.` |
| 497 | 366 | `##### What did you do right after college? Why did you make that decision?` |
| 501 | 366 | `##### Tell me about your favorite job. Tell me about your least favorite job. How and why did you make the decisions you made when choosing what roles you wanted to pursue?` |
| 505 | 366 | `##### What sort of work do you see yourself doing in the future? Who are the people you’ll be working with? Where will you be living?` |
| 517 | 367 | `##### Wrap-up` |
| 521 | 367 | `### Planning and Running Your Offsite` |
| 523 | 367 | `#### Planning checklist` |
| 527 | 367 | `##### 1+ month before offsite` |
| 537 | 367 | `##### 1 month before` |
| 547 | 368 | `##### 1 week before` |
| 565 | 368 | `##### 1 day before` |
| 573 | 368 | `##### Day of offsite` |
| 577 | 368 | `##### After offsite` |
| 585 | 368 | `#### Day-of-offsite templates` |
| 589 | 369 | `##### Offsite structure` |
| 601 | 369 | `##### Offsite welcome email` |
| 615 | 369 | `##### Agenda` |
| 637 | 370 | `### Leadership Team Snippets and Updates` |
| 647 | 371 | `##### Actions` |
| 651 | 371 | `##### Discussion topics` |
| 669 | 371 | `##### Standing questions` |
| 679 | 371 | `##### Customer issues` |
| 685 | 372 | `##### Customer wins` |
| 689 | 372 | `##### Snippets` |
| 707 | 372 | `### Stripe’s Unblocking Process` |
| 711 | 372 | `#### First, try to solve locally` |
| 727 | 373 | `#### How to unblock` |
| 743 | 374 | `##### Unblocking should be bilateral but can be unilateral` |
| 749 | 374 | `##### Is this a request to unblock?` |
| 753 | 374 | `##### What to do if you get a unilateral request to unblock` |
| 769 | 375 | `##### Example` |
| 787 | 376 | `#### Fictional example document` |
| 789 | 376 | `> **Stripe alignment model**` |
| 834 | 378 | `## Notes` |
