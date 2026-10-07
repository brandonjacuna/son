# Session 13 extraction notes

Mechanical extraction for Session 13 (Ch5: The formal review process, including Minimum viable people processes, Performance feedback, Calibration; Compensation, including Compensation conversations). Sources read only; nothing in `sources/` was modified. Method and output form follow Session 12 (`extraction/s12/extraction-notes.md`).

## Outputs

| File | Lines | Content |
|---|---|---|
| `extraction/s13/book-399-418.md` | 297 | Book pp. 399 to 418, 20 page markers; one bracketed context line at the top of p.399 (the tail of the p.398 pull quote, md line 7) and one after the last marker (the p.419 continuation and the next head, md line 297) |
| `extraction/s13/book-raw.txt` | 636 | Raw `page.get_text()` per page, pp. 399 to 418, with `===== Book page N =====` separators |
| `extraction/s13/workbook-ch5.md` | 274 | Workbook pp. 104 to 112 in full (Performance Review Template pp. 104 to 110; Compensation Conversations Preparation and Guide pp. 111 to 112), 9 page markers, with a page-range check at the top |
| `extraction/s13/figures/` | n/a | Empty: no image blocks or figures in range |

## Page mapping and boundaries

- Book: PDF page N = book page N (zero offset), as S8 to S12 used. Confirmed: p.399 opens with the tail of the Eric Yuan pull quote and then the 21.2pt head "The formal review process" (y 190.7), matching S12's recorded boundary.
- Start boundary (p.399): the quote's last two lines (16.9, y 91.5 to 111.7, superscript 70 at 11.2 flags 1) and the attribution "—Eric Yuan, founder and CEO, Zoom" (11.2, y 141.2) belong to S12's section and were already captured by S12 as a bracketed context line (S12 md line 219). Rendered here as a bracketed context line (md line 7), then the section head (md line 9). They are excluded from the word comparison.
- End boundary (p.418): p.418 ends mid-sentence inside `### Managing disappointment` ("...and probe whether they’re seeking a"). The section runs 7 lines onto p.419 (Session 14 range): the paragraph ends "...the accompanying rewards in the months to come." (y 217.1), then a closing paragraph for the whole formal review material, "Every company should have these basic people processes—performance feedback, calibration, and compensation—in place fairly early on..." (y 238.1 to 364.1). The 21.2pt head "Managing high performers" follows on p.419 at y 413.4, opening S14. Both p.419 passages are quoted verbatim in the bracketed context line after the p.418 body (md line 297), since they close S13's section; nothing else from p.419 is included. S14 should note that the top of its first page belongs to S13.
- Section structure: two 21.2pt heads in range, "The formal review process" (p.399) and "Compensation" (p.413). "Compensation" is set at the same size as the section head, so it is `##`, a sibling of "The formal review process", not a subsection.

## Book: tool, font census, layouts

PyMuPDF 1.26.5 only (`page.get_text("dict")`), no pypdf. One typographic system in range: the Type3 prose font (`Unnamed-T3`), color 0 on every span except the sidebar's inter-word spaces (color 3366828), flags 0 except footnote superscripts (flags 1). No `LiberationSerif` spans. One sidebar (blue ink, pp. 405 to 407). No tables, no exercise panels, no image blocks (`get_images` empty on every page), no vector figures.

Size census, pp. 399 to 418 (span counts; spans are roughly word-level, spaces included). Same scale as S8 to S12, so the heading map holds:

| Size (pt) | Spans | Role |
|---|---|---|
| 15.0 | 9,436 | Body text; bold subheads (roman and italic); bold lead-ins in the sidebar; sidebar body; SIDEBAR rules ("—") |
| 16.9 | 487 | Pull quotes (Eric Yuan tail p.399; Reid Hoffman pp. 400 to 401; Dominique Crenn p.402) |
| 11.2 | 52 | Pull-quote attributions (pp. 399, 401, 402); superscript 70 inside the p.399 quote tail (flags 1); SIDEBAR label (p.405) |
| 21.2 | 20 | Section heads "The formal review process", "Compensation"; sidebar title "A manager’s advice for delivering performance reviews" (two lines, blue) |
| 8.7 | 3 | Footnote superscripts 71 (p.405), 72 (p.409), 73 (p.410) |

p.419 for reference (not extracted): 15.0: 524; 21.2: 5 ("Managing high performers"); 8.7: 1 (superscript 74).

Per page:

| Page | Span counts by size | Other |
|---|---|---|
| 399 | 15.0: 450; 16.9: 31; 11.2: 12; 21.2: 7 | Quote tail and attribution (S12 context); section head |
| 400 | 15.0: 245; 16.9: 182 | 5 bullet marks; pull quote (Hoffman) begins |
| 401 | 15.0: 420; 16.9: 93; 11.2: 20 | Pull quote ends, attribution (two lines); bold roman subhead |
| 402 | 15.0: 307; 16.9: 181; 11.2: 19 | Bold roman subhead; pull quote (Crenn) and attribution |
| 403 | 15.0: 438 | Bold italic subhead; 4 bullet marks; justified line split into single words (re-merged) |
| 404 | 15.0: 392 | 2 bold italic subheads; 8 first-level bullet marks; 2 second-level bullet marks (x=105) |
| 405 | 15.0: 389; 21.2: 12; 11.2: 1; 8.7: 1 | 3 second-level bullet marks; superscript 71; SIDEBAR label and rule; blue sidebar begins (italic intro) |
| 406 | 15.0: 508 | Sidebar continues; 2 bold lead-ins on indented paragraphs; 2 blue bullet marks at x=105 |
| 407 | 15.0: 548 | Sidebar ends (closing rule y 296.2); bold roman subhead; justified line re-merged |
| 408 | 15.0: 548 | |
| 409 | 15.0: 475; 8.7: 1 | Superscript 72; numbered list begins (items 1 to 3) |
| 410 | 15.0: 514; 8.7: 1 | Numbered items 4 to 9; superscript 73 |
| 411 | 15.0: 490 | Numbered items 10 to 11; bold italic subhead at page foot |
| 412 | 15.0: 576 | |
| 413 | 15.0: 508; 21.2: 1 | Section head "Compensation" |
| 414 | 15.0: 392 | Bold roman subhead; 2 bullet marks; bold italic subhead; justified line re-merged |
| 415 | 15.0: 515 | 2 bold italic subheads |
| 416 | 15.0: 568 | Bold italic subhead |
| 417 | 15.0: 515 | 2 bold roman subheads; justified line re-merged |
| 418 | 15.0: 580 | Ends mid-sentence; section continues on p.419 |

### Bold and italic detection

- Bold: per span mean horizontal stroke width (dark-pixel run length, grayscale render at 4x, threshold 128), normalized to 15pt; cut 8.2 px, as S11 and S12. In range, regular body spans reach at most 8.14 px (the token "HR" on pp. 410, 411, 417, which never reads bold); the lightest true bold span is 8.21 ("review" in the italic subhead "Manager review", p.404) and bold spans run to 11.29 on the section heads. No single-word false bold occurred. Pull-quote attributions normalize above the cut (10.3 to 12.0) because the 11.2 size is scaled up; per S7 to S12 the attribution name is not bolded. Footnote superscripts (flags 1) are excluded.
- Italic: glyph slant per line (shear that maximizes the column projection of ink). The eight bold italic subheads and the two sidebar intro lines measure at the italic end of the scan; the bold roman heads, body lines, section heads and sidebar body measure 0.00 to 0.02. Confirmed against renders (pp. 401, 403, 414). Italics other than slant-detected subheads and the sidebar intro are not preserved.

### Heading map used

- 21.2 black as `##`; 15.0 bold roman as `###`; 15.0 bold italic as `####`; sidebar title (21.2 blue) as `###` inside `[Sidebar]` / `[End sidebar]`; sidebar intro paragraph (italic) as `*italic*`, per S8 and S11. Bold lead-ins as `**Lead-in:**`.
- Pull quotes (16.9) as blockquotes with the 11.2 attribution as `> —Name, role` after a `>` spacer line, per S12; the attribution name is not bolded.

## Section heads (`book-399-418.md`)

| md line | Page | Heading |
|---|---|---|
| 1 | n/a | `# Scaling People, book pages 399 to 418 (Ch5: The formal review process, Calibration, Compensation)` |
| 9 | 399 | `## The formal review process` |
| 45 | 401 | `### Minimum viable people processes` |
| 57 | 402 | `### Performance feedback` |
| 77 | 403 | `#### Peer reviews` |
| 91 | 404 | `#### Self-assessment` |
| 101 | 404 | `#### Manager review` |
| 133 | 405 | `### A manager’s advice for delivering performance reviews` (sidebar title; `[Sidebar]` md line 131, `[End sidebar]` md line 159) |
| 161 | 407 | `### Calibration` |
| 213 | 411 | `#### Calibration roles` (last line of p.411; its text starts on p.412) |
| 229 | 413 | `## Compensation` |
| 241 | 414 | `### Compensation conversations` |
| 251 | 414 | `#### Educate yourself` |
| 259 | 415 | `#### Instill trust in your systems` |
| 263 | 415 | `#### Understand the motivators` |
| 271 | 416 | `#### Have the conversation` |
| 281 | 417 | `### Comparisons` |
| 285 | 417 | `### Managing disappointment` |

Other navigation points: the six-item "To do this, you need" list at md lines 21 to 31; pull quotes at md lines 33 to 41 (Reid Hoffman, split at the p.400 to 401 marker) and 61 to 65 (Dominique Crenn); the five performance designations (second-level bullets) at md lines 115 to 125, split at the p.404 to 405 marker; the sidebar's bold lead-ins at md lines 143 and 145; the eleven calibration steps at md lines 183 to 207 (numbered, printed numerals kept); boundary context at md lines 7 and 297.

Heading-level notes: the typography makes "Comparisons" and "Managing disappointment" bold roman (`###`), siblings of "Compensation conversations", while the four guidelines under "Compensation conversations" ("Educate yourself" to "Have the conversation") are bold italic (`####`). Read by content, "Comparisons" and "Managing disappointment" continue the compensation-conversation guidance; the md follows the type. Likewise "Peer reviews", "Self-assessment", "Manager review" (under "Performance feedback") and "Calibration roles" (under "Calibration") are `####`.

## Table of contents: book (`book-399-418.md`)

| Page | Headings and topics | md lines |
|---|---|---|
| 399 | Context: Yuan quote end `[^70]`; `## The formal review process`; against abolishing reviews; transparent assessment | 7 to 15 |
| 400 | What you need (6 bullets); pull quote (Hoffman) begins | 19 to 35 |
| 401 | Pull quote ends; manager's role, no surprises, never promise rewards; `### Minimum viable people processes`; Stripe offsite | 39 to 49 |
| 402 | Perfect as the enemy of good; three elements; `### Performance feedback`; pull quote (Crenn) | 53 to 67 |
| 403 | Review cadence; `#### Peer reviews` (4 prompts) | 71 to 87 |
| 404 | `#### Self-assessment` (3 prompts); `#### Manager review` (5 prompts); designations begin | 91 to 117 |
| 405 | Designations end; fewer categories; talent review `[^71]`; sequencing; `[Sidebar]` and title | 121 to 135 |
| 406 | Sidebar: pre-meeting, review meeting (10 and 40 minutes), avoid arguments | 139 to 151 |
| 407 | Sidebar ends; `### Calibration`; purpose; timing | 155 to 165 |
| 408 | Off-cycle promotions; data analysis vs roll-up; calibration leader | 169 to 173 |
| 409 | Gut-checking designations; politics; steps intro `[^72]`; steps 1 to 3 | 177 to 187 |
| 410 | Steps 4 to 9 (bias `[^73]` at step 5) | 191 to 201 |
| 411 | Steps 10 to 11; bias check; HR tool, two-week delivery; `#### Calibration roles` | 205 to 213 |
| 412 | Manager's role; division leader runs calibration; check biases, normal curve | 217 to 221 |
| 413 | Lines between designations; guarding against politics; `## Compensation`; philosophy | 225 to 233 |
| 414 | Equity; framework and market data; `### Compensation conversations` (2 bullets); `#### Educate yourself` | 237 to 253 |
| 415 | `#### Instill trust in your systems`; `#### Understand the motivators` | 257 to 265 |
| 416 | `#### Have the conversation`; no-change conversations | 269 to 275 |
| 417 | Appendix pointer; `### Comparisons`; `### Managing disappointment` | 279 to 287 |
| 418 | Disappointment cases; reframing; promotion path (runs onto p.419) | 291 to 295 |
| (419) | Context: continuation, closing paragraph, head "Managing high performers" | 297 |

## Book: image blocks and figures

None. `get_images` is empty on pp. 399 to 418 and there are no image blocks. The only non-glyph vector marks are the 4.5pt square bullet marks (x=84 first level, x=105 second level; the two on p.406 are blue) and the sidebar rules (Type3 glyphs also appear as filled paths in `get_drawings`). `extraction/s13/figures/` is empty.

## Book: tables

None in range.

## Book: other handling

- Lists: 21 bullet marks became `- ` items (first level: 5 on p.400, 4 on p.403, 8 on p.404, 2 on p.414; the 5 performance designations at x=105 on pp. 404 to 405 as nested `   - ` items under the last manager-review prompt). The calibration steps are printed as numerals ("1." to "11.", x 81.8 and 73.5, continuation at x 98 in separate text blocks) and are rebuilt as numbered items with their continuations joined.
- Sidebar (pp. 405 to 407): "SIDEBAR" label and short rule converted to `[Sidebar]`, closing rule to `[End sidebar]`. The intro ("This section is adapted from a note by Hannah Pritchett, a former Stripe manager...") is italic and split at the p.405 to 406 marker, each part wrapped in `*...*`. "Pre-meeting:" and "During the review meeting:" are bold lead-ins on paragraphs printed indented (x=98) without bullet marks; they are rendered as plain paragraphs with `**Pre-meeting:**` and `**During the review meeting:**` (in print the colon after each is regular weight). The two items under "During the review meeting:" carry blue bullet marks at x=105 and are rendered as `- ` items.
- Pull quotes: Hoffman (pp. 400 to 401), three paragraphs, split at the page marker, attribution on two printed lines joined; Crenn (p.402), two paragraphs plus attribution. Crenn is identified as "owner and chef, Atelier Crenn, Michelin three-star restaurant".
- Paragraph breaks: text-layer blocks match the printed paragraphs (first-line indent x=98 or a gap over 26pt). Paragraphs split at page markers (per S8 to S12): pp. 399 to 400, 401 to 402, 402 to 403, 405 to 406 (sidebar intro), 406 to 407 (sidebar), 407 to 408, 408 to 409, 411 to 412 (subhead at page foot, text on p.412), 412 to 413, 413 to 414, 414 to 415, 415 to 416, 416 to 417, 417 to 418, and 418 to 419 (context line).
- Justified lines that the text layer split into single-word lines (p.403 "conversations and talk about your employees’ long-term"; p.407 "Calibration should accompany any formal performance"; p.414 "does your company’s compensation compare to market"; p.417 "for a guide to preparing for and holding compensation") were re-merged by baseline.
- Hyphenation: three line-end hyphens, all true compounds, kept and joined without a space: "backward-looking" (p.405), "roll-up" (p.408), "entry-level" (p.410). Line-end and line-initial em dashes joined without a space.
- Printed cross-references running behind the PDF (as S8 to S12 recorded): "the section on job levels and ladders on page 179" (p.400) and "Table 3 on page 179" (p.414) refer to the Chapter 3 job-levels material in S5's range; "the chapter appendix on page 413" (p.409, calibration packet example) and "the chapter appendix on page 416" (p.417, compensation conversation guide) refer to the Chapter 5 appendix at book pp. 467 to 473 (Performance Review Template pp. 468 to 471, Compensation Conversations Preparation and Guide pp. 472 to 473), which is the same material as the workbook pages extracted here. The book appendix does not appear to contain a separate calibration packet example beyond the Performance Review Template; not verified further. "As I said in Chapter 3" (p.413) refers back to the compensation discussion in Chapter 3. "Review our operating principles" (p.403) refers to the operating principles.
- Italics not preserved except slant-detected subheads and the sidebar intro, per S7 to S12.
- Dropped: nothing. No running footer "OceanofPDF.com" in range.

## Footnotes

Four markers touch the range: `[^70]` (p.399, inside the Yuan quote tail, context line md line 7 only), `[^71]` (p.405, md line 127), `[^72]` (p.409, md line 181), `[^73]` (p.410, step 5, md line 193). `[^74]` falls on p.419 (S14). The note texts are not in range: the Chapter 5 notes section is on book p.483 and later. Noted there, not extracted:

- 70: Ray Dalio, Principles (2017). Citation.
- 71: Sigma Assessment Systems’ 9-Box Grid (URL). Citation for "a more comprehensive rubric for assessing performance and potential".
- 72: Not a citation. A substantive note: a Stripe engineer found the initial engineering job ladder disempowering and argued ladders should describe outcomes rather than skills or inputs; the author agrees and advises against over-prescriptive expectations. Bears on the job-ladder and rubric material; the synthesis writer may want it read directly from p.483.
- 73: Culture Amp, "10 Performance Review Biases and How to Avoid Them" (URL). Citation.

## Counts

- Em dashes in the md page bodies (context lines excluded): 16, matching raw (19 less the p.399 attribution dash in the context and the two SIDEBAR rules). By page: 399: 3; 400: 2; 401: 3 (one is the Hoffman attribution dash); 402: 2 (one is the Crenn attribution dash); 403: 1; 407: 1; 412: 2; 413: 2. No en dashes in the book md.
- "guest": 0 occurrences in range (book and workbook).

## Book: verification

- NUL bytes: 0. U+FFFD: 0 (in the md and in `book-raw.txt`).
- Page markers: all 20 present, in order, 399 to 418.
- Word-for-word comparison of every page against raw `page.get_text()` (whitespace-normalized; line-end hyphens and dashes joined; markdown syntax removed; `[^N]` compared as N; SIDEBAR label and rules removed; the p.399 quote tail and attribution excluded as context): 5,249 raw words over pp. 399 to 418. All 20 pages identical. No reordering, no dropped or added words.
- The p.419 context passages were checked against p.419 raw text: both match verbatim.

## Workbook: census and extraction

- Mapping: PDF page N = workbook page N; the running head carries the same number. The workbook has 125 pages.
- Page ranges confirmed as briefed and as S12's census recorded: Performance Review Template pp. 104 to 110; Compensation Conversations Preparation and Guide pp. 111 to 112. No adjustment. p.113 opens Performance Improvement Documentation Templates (S12).
- Fonts: Neue Haas Grotesk (`NHaasGroteskTXPro-55Rg`, `-75Bd`); running head `SuisseIntl-Book` 6.5pt. Sizes: 36.0 exercise titles (p.104, p.111); 18.0 section heads ("Impact" p.105, "Strengths" p.108, "Timeline and resources" and "Preparation" p.111, "Outline of a compensation discussion" p.112); 12.0 bold labels ("Development areas" p.109, "Promotion proposal: yes or no" p.110); 9.0 body and bold field labels (24 bold spans); 8.5 bold "Notes" (p.112). No italics.
- Answer boxes: every stroked rectangle (45 in total, pp. 104 to 110 and the p.112 Notes area) is marked `[Answer box]` where it sits. On p.104 the first three boxes sit beside their labels (Name, Current level, Start date in role) and are marked on the label line; the rest sit below their prompt. p.111 has only the header rule; p.112 has one large box under "Notes" to the foot of the page.
- Structure: the three "Area for impact" pages (pp. 105 to 107) repeat the same four prompts; Strengths (p.108) has two strengths with two prompts each; Development areas (p.109) two areas with three prompts each, including "Ideas for how to improve"; Promotion proposal (p.110) has "If no" (two prompts) and "If yes" (three prompts). The compensation guide (pp. 111 to 112) is prose and bulleted checklists under bold labels, with no answer boxes except Notes.
- Bold-label handling: where only the label is bold and the rest of the line regular (e.g., "**Proposed promotion** (yes or no):", "**Area for impact 1**: Describe briefly here."), the bold span is kept as printed. On p.111 the inline lead-ins "If the person received a promotion or increase:", "If a misalignment of expectations arises:" and "Other tips:" are regular weight in the PDF and are not bolded.
- Line-end hyphens rejoined and dropped: ap-proximate, consid-er (p.108); pro-vide, per-son (p.109); docu-ment, rein-force, per-sonally (p.111); High-light, perfor-mance (p.112).
- Workbook verification: word comparison of pp. 104 to 112 against raw `get_text()` (running head and page number removed; bullets removed; hyphen breaks joined; colon spacing normalized): all 9 pages identical.

## Figures and numbers in her material

The program never reproduces financial figures. Across book pp. 399 to 418 and workbook pp. 104 to 112 there is **no monetary amount, no percentage of pay, no salary band figure, no equity figure, and no compensation formula**. Every compensation reference is qualitative. The places that carry a compensation-related number, or name a compensation element without a figure, so the synthesis writer can steer around them:

| Page | md line | What it says | Type |
|---|---|---|---|
| Book 418 | 295 | Example line to a disappointed high performer: “You’re receiving a larger increase than 75 percent of the company” | The only compensation-related number in range: a percentile of pay increases, given as an example script. Do not quote the figure |
| Book 411 | 207 | Senior leadership checks that "the percentage of employees being promoted feels equitable and in line with compensation budgets" | Mentions promotion percentage and compensation budgets; no figure |
| Book 408 | 171 | Calibration data analysis can "track average designations for a given group or promotion percentages" by gender and remote status | Promotion percentages as a metric; no figure |
| Book 413 | 233 | Sample philosophy "Compensation should be market-competitive... with higher rewards for higher performance"; "Pay for performance"; salaries fixed, bonus variable | Philosophy wording, no figure (also "pay for performance" at book 400, md line 21) |
| Book 414 | 237, 239 | Additional equity "beyond the new hire grant"; market data (names the compensation data vendor Radford) to set "salary bands and equity targets"; update market data "at least annually"; bonus or equity refresh program | Names band and equity elements; no figures |
| Book 401 | 43 | Formal reward "like a promotion, a raise, or a cash bonus" | No figure |
| Book 416 | 273 | Share a raise or bonus in person | No figure |
| Workbook 111 | 241 | Prepare with "the size of their last salary increase" | Refers to an individual's figure; none given |
| Workbook 111 | 247 | Do not set the expectation of "the same total increase moving forward" | No figure |
| Workbook 112 | 263, 264 | "Remind them of their current compensation"; "Share or affirm their base salary for the coming year"; "Share their target bonus for the coming year" | Script steps that would disclose individual figures; none given |

Non-financial numbers that could be mistaken for thresholds (not compensation, listed for completeness): performance distribution should be a normal curve "once your company has over 30 people" (book 412, md line 221); start these processes "once you exceed 20 or 30 employees" (p.419, context line md line 297); peers "three to five" (book 403, md line 79); review meeting timings "24 hours", "10 minutes", "40 minutes" (sidebar, book 406, md lines 143 to 149); "two-week period" to deliver reviews (book 411, md line 211); "six months from now" (book 418, md line 293); levels "Level 1" to "Level 5" in calibration examples (book 408 and 410); "H1, H2" timing (workbook 110, md line 203); "2–3 projects", "1–2 strengths" and similar (workbook 105 to 110).

## Anomalies and uncertainties

1. The formal review material runs onto p.419 (S14 range): the end of the "Managing disappointment" paragraph and a closing paragraph that summarizes the whole formal review process. Given in full as context (md line 297). S14's extraction should treat these p.419 lines as S13 material.
2. "Compensation" (p.413) is a 21.2pt section head, a sibling of "The formal review process". The brief's framing "formal review + compensation" matches.
3. Heading levels follow typography: "Comparisons" and "Managing disappointment" are `###` (bold roman), though by content they continue the compensation-conversation guidance set under `####` heads.
4. Note 72 (on the job ladder) is substantive, not a citation; see Footnotes.
5. The sidebar's "Pre-meeting" and "During the review meeting" are indented paragraphs without bullet marks in print; rendered as plain paragraphs with bold lead-ins.
6. Cross-references to "page 413" and "page 416" point to the book's Chapter 5 appendix (pp. 467 to 473), whose content matches the workbook pages extracted here.
