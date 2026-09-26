# Session 12 extraction notes

Mechanical extraction for Session 12 (Ch5: Chapter opener, Hypothesis-based coaching, Giving hard feedback, Creating a culture of informal feedback). Sources read only; nothing in `sources/` was modified.

## Outputs

| File | Lines | Content |
|---|---|---|
| `extraction/s12/book-381-398.md` | 219 | Book pp. 381 to 398, 18 page markers, plus one bracketed context line after the last marker (the end of the p.398 pull quote and the first head of p.399) |
| `extraction/s12/book-raw.txt` | 519 | Raw `page.get_text()` per page, pp. 381 to 398, with `===== Book page N =====` separators |
| `extraction/s12/workbook-ch5.md` | 133 | Workbook Chapter 5 exercise census (pp. 103 to 125) at the top; extracted: p.103 (contents) and pp. 113 to 117 (Performance Improvement Documentation Templates), 6 page markers |
| `extraction/s12/figures/p381-image.png` | n/a | Chapter 5 opener image (native 900 x 1350) |

## Page mapping and boundaries

- Book: PDF page N = book page N (zero offset), as `reference/chapter-map.md` states and as S8 to S11's markers use. Confirmed: p.381 is the Chapter 5 opener image, as S11's notes recorded; the 21.2pt heads fall on pp. 385, 391 and 395; p.399 opens "The formal review process" region.
- Start boundary (p.381): p.381 is a full-page chapter opener image with no text layer for the title. Its only text is the running footer "OceanofPDF.com" (dropped). Handled as S8 handled the Chapter 4 opener (p.261): `[IMAGE BLOCK ...]`, a figure description, and an added `# Chapter 5: Core Framework 4: Feedback and Performance Mechanisms` (md line 11).
- The chapter's real text starts on p.382. Pages 382 to 385 are an untitled chapter introduction (Paul Bascobert, the campaign manager, the first Google review, the baseball coach, the Parcells quote with note 67). The chapter map and the task brief put "Hypothesis-based coaching" at p.382; the head itself is on p.385 (y 223.8, md line 47), after the introduction's last paragraph. Same pattern as S8's Chapter 4 (map 262, head 264).
- Section heads land: "Giving hard feedback" p.391 (y 517.8, md line 123), "Creating a culture of informal feedback" p.395 (y 307.8, md line 171), both where the brief expected them.
- End boundary (p.398): p.398 ends mid-section and mid-quote. The section "Creating a culture of informal feedback" (with its `###` "Asking for feedback") runs through the four bullet pointers, then a 16.9pt pull quote (Eric Yuan) begins at y 529.5 and runs off the page after "But if you really want to improve and become". p.399 (S13 range) opens with the quote's last two lines, "more self-aware, you need it. We’ve adopted a lot of this from Ray Dalio’s Principles book.70”" (y 73.5 to 111.7; superscript 70), the attribution "—Eric Yuan, founder and CEO, Zoom" (11.2, y 129.2), then the 21.2pt section head "The formal review process" (y 169.0). The quote continuation, attribution and head are given as a bracketed context line after the p.398 body (md line 219), following S10's placement of cross-boundary context (S10 md line 487). Nothing else from p.399 is included. So "Creating a culture of informal feedback" ends on p.399 with the close of the Yuan quote; S12's range captures all of the section's prose.

## Book: tool, font census, layouts

PyMuPDF 1.26.5 only (`page.get_text("dict")`), no pypdf. One typographic system in range: the Type3 prose font (`Unnamed-T3`), color 0 on every span, flags 0 except footnote superscripts (flags 1). One `LiberationSerif` span (p.394, the ellipsis in "For example …"). No sidebar blue, no SIDEBAR labels, no exercise panels, no tables.

Size census, pp. 381 to 398 (span counts; spans are roughly word-level, spaces included). Chapter 5 uses the same scale as S8 to S11's prose, so the S8 to S11 heading map holds:

| Size (pt) | Spans | Role |
|---|---|---|
| 15.0 | 9,709 | Body text; bold subheads (roman and italic); bold list lead-ins; running footer (p.381) |
| 16.9 | 209 | Pull quotes (Don Hall p.396; Eric Yuan p.398, continuing to p.399) |
| 21.2 | 19 | Section heads "Hypothesis-based coaching", "Giving hard feedback", "Creating a culture of informal feedback" |
| 11.2 | 16 | Pull-quote attribution (p.396); superscript 69 inside the p.398 pull quote (flags 1) |
| 8.7 | 2 | Footnote superscripts 67 (p.385), 68 (p.389) |

p.399 for reference (not extracted): 15.0: 450; 16.9: 31; 11.2: 12; 21.2: 7 (quote tail, attribution, "The formal review process").

Per page:

| Page | Span counts by size | Other |
|---|---|---|
| 381 | 15.0: 1 | One image block (100.5, 72.0, 511.5, 687.8), 900 x 1350; the one span is the footer "OceanofPDF.com" |
| 382 | 15.0: 638 | Chapter text begins; no head |
| 383 | 15.0: 621 | |
| 384 | 15.0: 612 | |
| 385 | 15.0: 598; 21.2: 3; 8.7: 1 | Superscript 67; section head |
| 386 | 15.0: 602 | |
| 387 | 15.0: 525 | 3 bullet marks (bold lead-ins); bold italic subhead |
| 388 | 15.0: 578 | Bold italic subhead |
| 389 | 15.0: 592; 8.7: 1 | Superscript 68; bold italic subhead |
| 390 | 15.0: 626 | |
| 391 | 15.0: 548; 21.2: 5 | Section head |
| 392 | 15.0: 589 | Bold roman subhead at page top |
| 393 | 15.0: 539 | 2 bold italic subheads |
| 394 | 15.0: 609 | LiberationSerif ellipsis |
| 395 | 15.0: 586; 21.2: 11 | Section head |
| 396 | 15.0: 455; 16.9: 79; 11.2: 15 | Pull quote and attribution |
| 397 | 15.0: 565 | Bold roman subhead; 1 bullet mark |
| 398 | 15.0: 425; 16.9: 130; 11.2: 1 | 3 bullet marks; pull quote begins (superscript 69 at 11.2) and runs off the page |

### Bold and italic detection

- Bold: per span mean horizontal stroke width (dark-pixel run length, grayscale render at 4x, threshold 128), normalized to 15pt; cut 8.2 px, as S11. In this range regular spans reach 7.94 to 8.01 px on isolated tokens ("He" pp. 383 and 384, "Be" and "—to" p.387); the lightest true bold span is 8.39 ("your" in the p.389 italic subhead), and bold spans run to 12.55. No single-word false bold occurred. The footer "OceanofPDF.com" (8.59) was dropped before classification. Non-alphanumeric spans take bold only when both neighbors are bold. Footnote superscripts (flags 1) are excluded. Pull-quote text (16.9) normalizes to 5.69 to 7.43 and none reads bold.
- Italic: glyph slant per line (shear that maximizes the column projection of ink). The five bold italic subheads measure 0.22; body lines and the bold roman heads -0.04 to 0.00; the section heads -0.02. One pull-quote line on p.398 ("The Speed of Trust by Stephen Covey.") measures 0.10, a partially italic line (the book title); per S7 to S11, italics other than slant-detected subheads are not preserved.

### Heading map used

- Chapter opener as `#` (added, per S8). 21.2 as `##`; 15.0 bold roman as `###`; 15.0 bold italic as `####`. Inline bold lead-ins as `- **Lead-in.** text`, per S7 to S11.
- Pull quotes (16.9) as blockquotes with the 11.2 attribution as `> —Name, role`, per S7 to S10; the attribution name is not bolded.

## Section heads (`book-381-398.md`)

| md line | Page | Heading |
|---|---|---|
| 1 | n/a | `# Scaling People, book pages 381 to 398 (Ch5: Chapter opener, Hypothesis-based coaching, Giving hard feedback, Creating a culture of informal feedback)` |
| 11 | 381 | `# Chapter 5: Core Framework 4: Feedback and Performance Mechanisms` (added from the opener image) |
| 47 | 385 | `## Hypothesis-based coaching` |
| 81 | 387 | `#### Gather data` |
| 93 | 388 | `#### Form a hypothesis` |
| 105 | 389 | `#### Test your hypothesis` |
| 123 | 391 | `## Giving hard feedback` |
| 129 | 392 | `### Be an explorer, not a lecturer` |
| 143 | 393 | `#### Option 1: Ask an open-ended question` |
| 151 | 393 | `#### Option 2: Share an empathetic observation` |
| 171 | 395 | `## Creating a culture of informal feedback` |
| 197 | 397 | `### Asking for feedback` |

Other navigation points: the three-step list (bold lead-ins "Gather data:", "Form a hypothesis:", "Test your hypothesis:") at md lines 71 to 75; the four feedback-asking pointers at md lines 201, 207, 209, 211; pull quotes at md lines 185 to 187 (Don Hall) and 213 to 217 (Eric Yuan, split off at the page end); boundary context at md line 219.

Heading-level notes: "Be an explorer, not a lecturer" and "Asking for feedback" are bold roman (`###`); the hypothesis steps and the two options are bold italic (`####`). The three step names appear twice (p.387): first as bold lead-ins in a bulleted list, then as `####` subheads, the same pattern S11 recorded for its mitigations.

## Table of contents: book (`book-381-398.md`)

| Page | Headings and topics | md lines |
|---|---|---|
| 381 | Chapter opener image; `# Chapter 5: ...` | 7 to 11 |
| 382 | Management as iterative; extreme coach vs forgot-to coach; “Feedback is a gift”; Paul Bascobert | 15 to 21 |
| 383 | “Think harder”; the Teresa and Mike coaching moment | 25 to 31 |
| 384 | Campaign manager; first formal review at Google; the baseball coach | 35 to 41 |
| 385 | Parcells `[^67]`; `## Hypothesis-based coaching`; intuition as hypothesis; Operating Principle 2 | 45 to 53 |
| 386 | Coaching as ally; deductive vs inductive; the career conversation as hypothesis source | 57 to 63 |
| 387 | Three steps (3 bullets); 80-20 example; `#### Gather data` (Anika) | 67 to 83 |
| 388 | Anika and Sonya, more data than you think; `#### Form a hypothesis` | 87 to 97 |
| 389 | Peacetime and wartime leader `[^68]`; trusting intuition, three to six months; `#### Test your hypothesis` | 101 to 107 |
| 390 | Observation, not judgment; self-awareness gap | 111 to 115 |
| 391 | The talented person who left; test duties before promoting; `## Giving hard feedback` | 119 to 125 |
| 392 | `### Be an explorer, not a lecturer`; two methods | 129 to 137 |
| 393 | `#### Option 1: Ask an open-ended question`; closed questions; `#### Option 2: Share an empathetic observation` | 141 to 153 |
| 394 | Supportive, objective, specific; holding up a mirror; cycling between options | 157 to 163 |
| 395 | Self-awareness and low performers; `## Creating a culture of informal feedback`; Stripe’s commenting culture and test-before-sending | 167 to 175 |
| 396 | Bidirectional feedback gap at Stripe; examine feedback culture; pull quote (Don Hall); team vs individual feedback | 179 to 189 |
| 397 | Solicit feedback; `### Asking for feedback`; first pointer (1 bullet) | 193 to 201 |
| 398 | Three pointers (3 bullets); pull quote (Eric Yuan) `[^69]`, runs off the page | 205 to 217 |
| (399) | Context: quote end `[^70]`, attribution, head “The formal review process” | 219 |

## Book: image blocks and figures

| Page | Image bbox (pt) | Native px | What it is | Handling |
|---|---|---|---|---|
| 381 | (100.5, 72.0, 511.5, 687.8) | 900 x 1350 | Chapter opener: "5", "Core Framework 4", "Feedback and Performance Mechanisms" (three lines) in blue on a pale lavender panel. No text layer for the title | Extracted natively to `figures/p381-image.png`; described at md line 9; `#` head added at md line 11 |

No other image blocks (`get_images` empty on pp. 382 to 398) and no vector figures: the only non-glyph vector marks are the 4.5pt square bullet marks at x=84 (Type3 glyphs also appear as filled paths in `get_drawings`).

## Book: tables

None in range.

## Book: other handling

- Lists: 7 bullet marks (4.5pt filled squares at x=84: 3 on p.387, 1 on p.397, 3 on p.398) became `- ` items; each item's continuation lines (x=98) were joined into the item. The first "Asking for feedback" pointer breaks across pp. 397 to 398 and is split at the page marker; the continuation after the marker ("successful?” Thank the person...", md line 205) is a plain paragraph without a bullet, per S8 to S11.
- Paragraph breaks: text-layer blocks match the printed paragraphs one to one in this range (first-line indent x=98 or a gap over 26pt); no block contains a mid-block indent. Bullet marks split items within a block.
- Paragraphs split at page markers (per S8 to S11): pp. 382 to 383, 385 to 386, 386 to 387, 387 to 388, 388 to 389, 390 to 391, 392 to 393, 393 to 394, 394 to 395, 395 to 396, 396 to 397, 397 to 398 (inside the first pointer). The p.387 subhead "Gather data" is followed by one line of text before the page break.
- Pull quotes: p.396 (Don Hall), one paragraph plus attribution (md lines 185 to 187); p.398 (Eric Yuan), three paragraphs, the third cut off at the page end (md lines 213 to 217). Superscript 69 inside the Yuan quote is set at 11.2 (flags 1) and kept as `[^69]`.
- Footnotes: 3 markers in range, `[^67]` (p.385, md line 45), `[^68]` (p.389, md line 101), `[^69]` (p.398, md line 213); `[^70]` falls on p.399 and appears only in the context line (md line 219). The note texts are not in range: the Chapter 5 notes section starts on p.483 (25pt "Notes" head), which lists 67 as "Lewis, “Bill Parcells.”", 68 as Ben Horowitz, “Peacetime CEO/Wartime CEO” (Future, 2011), 69 as Covey and Merrill, The Speed of Trust (2006), and 70 as Ray Dalio, Principles (2017). They are citations, not substantive notes.
- Hyphenation: two line-end hyphens, both true compounds, kept and joined without a space: "self-awareness" (p.390), "self-aware" (p.395). Line-end em dashes (pp. 384, 385, 395) and line-initial em dashes (pp. 387, 393, 397) joined without a space.
- Printed cross-reference running behind the PDF: p.395 "managing low performers on page 386" refers to the low-performers material in S14's range (pp. 419 to 448). "The career conversation outlined in Chapter 4" (p.386) refers to S11's p.364 exercise; "the Michael Lewis article about Bill Parcells I mentioned in Chapter 4" (p.385); "Operating Principle 2: Say the thing you think you cannot say" (p.385) refers back to the operating principles.
- Italics not preserved except slant-detected subheads (e.g., the book title The Speed of Trust in the p.398 pull quote), per S7 to S11.
- Dropped: running footer "OceanofPDF.com" (p.381, the only page in range that carries it).

## Counts

- Em dashes in the md page bodies: 30, matching raw (30). By page: 382: 3; 383: 1; 384: 3; 385: 2; 386: 3; 387: 4; 388: 2; 389: 2; 390: 1; 393: 2; 394: 1; 395: 2; 396: 3 (one is the attribution dash); 397: 1. No en dashes.
- "guest": 0 occurrences in range.

## Book: verification

- NUL bytes: 0. U+FFFD: 0 (both in the md and in `book-raw.txt`).
- Page markers: all 18 present, in order, 381 to 398.
- Word-for-word comparison of every page against raw `page.get_text()` (whitespace-normalized; line-end hyphens and dashes joined; markdown syntax removed; `[^N]` compared as N; footer and context line excluded): 5,216 raw words over pp. 382 to 398. 16 pages identical. One difference, p.396, the comparison artifact S9 and S10 recorded: the raw joiner attaches the pull-quote attribution to the quote's last word ("brutal.”—Don") because the attribution line begins with an em dash; the md keeps them as separate lines. No reordering, no dropped or added words. p.381 has no text other than the footer.

## Workbook: census and extraction

- Mapping: PDF page N = workbook page N; the running head on every page prints the same number (as S8 found for Chapter 4). Chapter 5 starts at workbook p.103 (the divider and contents page, 36pt "Chapter 5"), as the chapter map says, and runs to p.124; p.125 carries only a page number. The workbook has 125 pages.
- The p.103 contents page's printed page references run one behind the actual pages except the first (Performance Review Template 104, actual 104; Compensation 110, actual 111; Performance Improvement Documentation 112, actual 113; PIP 117, actual 118; Managing Out 123, actual 124). S8's Chapter 4 contents page shows the same offset (89, 92, 95, 97 against actual 90, 93, 96, 98).
- Fonts: Neue Haas Grotesk (`NHaasGroteskTXPro-55Rg`, `-75Bd`) with font flags; running head in 6.5pt. Sizes: 36.0 exercise titles; 18.0 section heads; 12.0 (the labels "Development areas" p.109 and "Promotion proposal: yes or no" p.110; the p.124 checklist items); 9.0 body; 8.5 template letters (pp. 113 to 116), the PIP form (pp. 118 to 122) and "Notes" labels; 5.0 PIP page counters ("1/4" to "4/4") and 8.0 signature lines (p.122).

| Exercise | Workbook pages | Section heads (18pt) | Session | Extracted |
|---|---|---|---|---|
| Performance Review Template | 104 to 110 | Impact (p.105); Strengths (p.108); Development areas and Promotion proposal (pp. 109 to 110, 12pt labels) | S13 | No |
| Compensation Conversations Preparation and Guide | 111 to 112 | Timeline and resources; Preparation (p.111); Outline of a compensation discussion (p.112) | S13 | No |
| Performance Improvement Documentation Templates | 113 to 117 | Initial documentation of feedback after meeting (p.113); Progress update (p.114); Employee getting back on track (p.115); Insufficient progress (after a reasonable period) (p.116); Notes (p.117) | S12 (hard feedback, written record); primary home S14 | Yes, `workbook-ch5.md` lines 29 to 133 |
| Performance Improvement Plan Template | 118 to 123 | Performance improvement plan (p.119); Notes (p.123) | S14 | No |
| Managing Out Checklist | 124 | none (eight checklist items) | S15 | No |

- Relevance judgment: no Chapter 5 workbook exercise addresses coaching, hypothesis-based coaching, informal feedback, feedback culture or asking for feedback. The Performance Improvement Documentation Templates were extracted because the first template is the written recap of a constructive-feedback 1:1 and all four frame feedback as situation, observable behaviors and impact. This is a judgment call: their primary home is S14 (low performers), and S14 will need them again. Not extracted but touching feedback: Performance Review Template "Development areas" (p.109, S13) and the Managing Out Checklist's first two items (p.124, S15).
- Handling in `workbook-ch5.md`: census table and relevance note at the top (lines 5 to 15); p.103 contents (lines 17 to 27); each template letter sits in a ruled box (stroked rectangle) and is a blockquote between `[Boxed template]` and `[End boxed template]`; bullets as nested list items; line-end word-break hyphens rejoined and dropped (develop-ment, as-sessment, crit-ical, expecta-tion, meet-ing, ex-pectations, behav-iors); "[1:1/" + "performance review]" joined without a space at the slash. On p.116 the text layer emits the 18pt head "Insufficient progress (after a reasonable period)" after the letter; it is printed at the top of the page (y 68) and is placed there.
- Workbook verification: word comparison of pp. 113 to 117 against raw `get_text()` (running head, page number and bullets removed; hyphen breaks joined): pp. 114, 115, 117 identical; p.116 same words, head moved to its printed position; p.113 differs only in the slash join above.
- Printed typo kept: "they impact they had" (p.114, second template).

## Anomalies and uncertainties

1. "Hypothesis-based coaching" is on p.385, not p.382 as the brief and chapter map say; pp. 382 to 385 are an untitled introduction. The introduction's content (the extreme coach and forgot-to coach, "Feedback is a gift", coaching moments, why formal reviews still matter) is within S12's range and extracted in full.
2. The session's last section runs 4 lines onto p.399: the Eric Yuan pull quote ends and is attributed there. Given as context only (md line 219), with note 70.
3. Heading levels come from typography: `###` bold roman ("Be an explorer, not a lecturer", "Asking for feedback") and `####` bold italic (the three hypothesis steps, the two options). "Asking for feedback" is a `###` under `## Creating a culture of informal feedback`, not a new section.
4. The workbook selection (one exercise, primary home S14) is a judgment call; see the workbook section.
5. The p.395 cross-reference "page 386" does not match a PDF page on the low-performers material; printed references run behind the PDF throughout, as S8 to S11 recorded.
