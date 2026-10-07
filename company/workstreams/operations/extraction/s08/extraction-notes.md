# Session 8 extraction notes

Mechanical extraction for Session 8 (Ch4, Team structures). Sources read only; nothing in `sources/` was modified.

## Outputs

| File | Lines | Content |
|---|---|---|
| `extraction/s08/book-261-281.md` | 299 | Book pp. 261 to 281, 21 page markers |
| `extraction/s08/workbook-ch4.md` | 418 | Workbook pp. 89 to 102, 14 page markers |
| `extraction/s08/figures/p261-image.png` | n/a | Chapter opener image |
| `extraction/s08/figures/p270-image.png` | n/a | Figure 15 |
| `extraction/s08/figures/p272-image.png` | n/a | Figure 16 |
| `extraction/s08/figures/p274-image.png` | n/a | Figure 17 |

## Page mapping

- Book: PDF page N = book page N (zero offset), as `reference/chapter-map.md` states and as S7's markers use. Confirmed: p.261 is the Chapter 4 opener, p.264 carries the "Team structures" head (the chapter map lists the section at 262; 262 to 264 are the untitled chapter introduction, and the head itself falls on 264).
- Workbook: PDF page N = workbook page N; the running head on every page prints the same number. Marker format matches S6 (`===== Workbook page N =====`).

## Book: tool, font census, layouts

PyMuPDF 1.26.5 only (`page.get_text("dict")`), no pypdf. All text is in one Type3 font (`Unnamed-T3`) with no usable font flags or colors in the text layer, so bold was detected by rendered ink density and sidebar text by rendered color.

Size census, pp. 261 to 281 (span counts; spans here are roughly word-level):

| Size (pt) | Spans | Role |
|---|---|---|
| 15.0 | 4,474 | Body text; also bold subheads (single-line blocks, ink density 0.245 to 0.308 against body 0.114 to 0.188); also sidebar body (blue) |
| 11.2 | 495 | Table 6 cell text (monospace look, blue), figure and table captions, SIDEBAR label, "Words to live by" boxed callout |
| 21.2 | 6 | Section head "Team structures" (black) and sidebar titles "Code Yellows", "Business leads" (blue) |
| 8.7 | 1 | Footnote superscript "40" (p.264) |

The scale differs from S7's range (body 11.1, heads 15.7): this range's body is 15.0 and heads 21.2. One prose layout throughout, with two sidebar treatments (blue text between a "SIDEBAR" label and a closing short rule) and one ruled table. Per-page census: pp. 262, 263, 265, 266, 269, 271, 273, 275 to 281 are 15.0 only; p.264 adds 21.2, 11.2, 8.7; p.267 and p.268 are table pages (11.2 dominant); pp. 270, 272, 274 carry figures and 11.2 captions.

Heading map used: chapter opener as `#`; 21.2 black as `##`; 15.0 bold black as `###`; 21.2 blue sidebar title as `###` inside `[Sidebar]`/`[End sidebar]`; 15.0 bold blue sidebar subhead as `####`. Sidebar intro paragraphs (italic, first paragraph after the sidebar title) as `*italic*`. Other italics (e.g., the magazine title on p.264) are not preserved, consistent with S7. Bullets detected from 4.5pt square vector marks at x=84 (pp. 266, 269, 279).

## Book: image blocks and figures

| Page | Image bbox (pt) | Native px | What it is | Handling |
|---|---|---|---|---|
| 261 | (100.5, 72.0, 511.5, 687.8) | 900 x 1350 | Chapter opener: "4", "Core Framework 3", "Intentional Team Development" on a lavender panel. No text layer for the title | Rendered; described; `# Chapter 4: Core Framework 3: Intentional Team Development` added (md line 11) |
| 270 | (77.3, 396.0, 534.8, 671.3) | 1001 x 601 | Figure 15, vertical vs horizontal team structures (box schematic) | Rendered; described at md line 149 |
| 272 | (77.3, 72.0, 534.8, 228.0) | 1356 x 462 | Figure 16, regional sales verticals (APAC, EMEA, NA, LATAM) on a SALES OPS horizontal, with a Figure 15 key highlighting SALES | Rendered; described at md line 165 |
| 274 | (77.3, 72.0, 534.8, 352.5) | 1601 x 981 | Figure 17, hybrid org chart (CEO; CPO, CTO, COO, CRO; CFO, GC, Head of People; business unit with partner trio; product marketing shaded as the hinge; solid and dotted reporting lines) | Rendered from the native image and read at full resolution; described at md line 183 |

Figure captions are in the text layer (11.2pt) and are kept as `[caption] Figure N. ...`, following the S5 convention for image blocks. One judgment call in Figure 17: a second dotted arrow into ENGINEERING descends alongside the CTO line and reads as originating on the CTO line's horizontal run; the description says so rather than asserting its source.

## Book: tables rebuilt

- Table 6, "Teams, projects, and working groups" (pp. 267 to 268): five columns (TYPE, STRUCTURE, TIME FRAME, CONSIDERATIONS & INVESTMENT, TASK OR MISSION), three rows (TEAMS, PROJECTS, WORKING GROUPS). Rebuilt from cell geometry (column x-bands, row y-bands from the row labels). The WORKING GROUPS row breaks across the page; split at the page marker with "(cont.)" headers per S7 (md lines 85 to 89 and 93 to 95), caption at line 97.
- "Words to live by" (p.264) is a ruled box, not a table: rendered as a blockquote with its bold title (md line 45), footnote marker `[^40]` inline.

## Book: other handling

- Footnotes: one marker, `[^40]` (p.264). The chapter's notes are not in range (Ch4 notes fall at the chapter's end, after p.380), so no note text is included.
- Hyphenation: 11 line-end hyphens in range, all true compounds (high-growth, team-focused, shorter-term, long-term, cross-functional x2, sub-team, mission-oriented, cross-section, 30-day, dotted-line). All kept, lines joined without a space.
- Justified lines on p.272 that the text layer split into separate word lines were re-merged by baseline.
- Dropped: running footer "OceanofPDF.com" (p.261), the short decorative rule under each SIDEBAR label, the closing rules (converted to `[End sidebar]`).
- The last paragraph on p.281 ends mid-sentence ("...and when") and continues on p.282, which is Session 9's range.

## Book: verification

- NUL bytes: 0. U+FFFD: 0.
- Page markers: all 21 present, in order, 261 to 281.
- Word-for-word comparison against raw `page.get_text()` (whitespace-normalized, line-end hyphens joined): three random pages (seed 8: pp. 269, 273, 274) plus pp. 264, 267, 268 checked individually; then all 21 pages. 4,957 raw words; zero unexpected differences. The only differences are intentional: the SIDEBAR label converted to `[Sidebar]` (pp. 268, 274), the "(cont.)" table header repeated on p.268, and the chapter title heading added on p.261 from the image.

## Workbook: tool and handling

PyMuPDF with span fonts (real embedded fonts: NHaasGroteskTXPro 75Bd/55Rg/56It, A2RecordGothicMono, SuisseIntl). Census: 36pt bold page titles (`##`), 18pt bold section heads (`###`), 9pt regular body with 9pt bold lead-ins (inline `**bold**`) and one 9pt italic line, 8.5pt bold "Notes" labels over blank writing boxes (`#### Notes` plus `[Blank notes area]`), 8.0 and 7.5pt table text on p.95, 12pt SuisseIntl checkbox glyphs on p.93, 9pt monospace email template on p.94 (rendered as blockquote), 6.5pt running head (dropped). No image blocks.

- Lines rejoined into paragraphs by line spacing (14pt leading within a paragraph, 20pt between).
- Soft hyphens (U+00AD) removed. 24 line-end hyphens: 23 dropped where the joined word is a dictionary word (un-derstand, con-sider, whatev-er, graduat-ing, col-laboratively, char-gers, etc.), 1 kept as a true compound (get-to-know-you, p.90).
- List markers (1., 1.1, A., bullets, checkboxes) rebuilt as markdown list items; checkboxes as `- [ ]`.
- Table rebuilt: p.95 offsite agenda (Session, What we'll be doing, Time, Length, Facilitator; 11 rows) at md lines 188 to 200.
- Boxed example document on p.101 marked `[Boxed example document]` / `[End boxed example]` (md lines 366 to 406).
- Source text preserved as printed, including "entrance.code" on p.93.

## Workbook: verification

- NUL bytes: 0. U+FFFD: 0. Soft hyphens remaining: 0.
- Page markers: all 14 present, 89 to 102.
- Character-sequence comparison against raw `page.get_text()` (running head, page number, list glyphs, whitespace, hyphens, and markdown syntax removed): pp. 90 to 102 identical; p.89 identical as a character multiset (the contents list is reordered to pair each title with its page number).

## Anomalies

1. Workbook contents page (p.89) prints page references 89, 92, 95, 97; the sections actually start on 90, 93, 96, 98. The printed references are off by one. The md keeps the printed numbers and the page markers show the true pages.
2. Book chapter map lists "Team structures" at p.262; the head is printed on p.264. Pages 262 to 264 are the untitled Chapter 4 introduction, which belongs to S8's range either way.
3. Book p.281 ends mid-paragraph; the paragraph finishes on p.282 (S9).
4. Workbook Chapter 4 contains no material on team structures proper (see below).

## Table of contents: book (`book-261-281.md`)

| Page | Headings and topics | md lines |
|---|---|---|
| 261 | Chapter opener image; `# Chapter 4: Core Framework 3: Intentional Team Development` | 5 to 11 |
| 262 | Chapter introduction: groups vs. teams; Tracey Franklin (Moderna) on team-focused performance tools; team development as habits; new people joining | 13 to 23 |
| 263 | Introduction cont.: absorbing change; determine group type, diagnose, restructure, build environment; complexities later in the chapter | 25 to 33 |
| 264 | Introduction close; `## Team structures` (start with strategy); boxed callout "Words to live by" `[^40]` | 35 to 49 |
| 265 | Structure matches strategy; solid-line vs dotted-line leverage; preserve optionality, reexamine yearly; `### Teams, working groups, and projects` | 51 to 61 |
| 266 | Terms used interchangeably; three questions (objectives, skills, duration); being wrong about duration; temporary structures persisting too long | 63 to 79 |
| 267 | Two problems of persistence; Table 6 (TEAMS, PROJECTS, WORKING GROUPS begins) | 81 to 89 |
| 268 | Table 6 cont. (WORKING GROUPS), caption; `[Sidebar]` `### Code Yellows` intro; `#### What is it?` | 91 to 105 |
| 269 | Code Yellow definition; `#### What does it entail?` (7 bullets); `#### How long should a Code Yellow last?` | 107 to 131 |
| 270 | 10-week limit; `#### How can you trigger a Code Yellow?`; `[End sidebar]`; `### Structuring teams` (functional vs product/business line; horizontal vs vertical); Figure 15 | 133 to 151 |
| 271 | Functional structures in early-stage companies; functional as vertical; vertical and horizontal team examples (APAC sales, Stripe support) | 153 to 159 |
| 272 | Figure 16; business units, why divisions are rarely clean, hybrid structure, the hinge | 161 to 169 |
| 273 | Hybrid example (product/business lead owns P&L); product marketing as the common hinge; moving the hinge as products expand | 171 to 177 |
| 274 | Figure 17 (hybrid org chart); `[Sidebar]` `### Business leads` intro; `#### Introduction` | 179 to 195 |
| 275 | BL reporting cont.; `#### Eligibility`; `#### Reporting` (product development families; dual reporting) | 197 to 211 |
| 276 | Dotted lines the other way (bizops, product ops); oversight functions report centrally; dotted-line roles agreed with functional lead; QBR people section; `#### Headcount accounting` | 213 to 225 |
| 277 | Ring-fenced headcount; `#### Forums`; `#### Goal setting` (dotted-line goals; sales comp plans) | 227 to 241 |
| 278 | `#### Performance management` (BL calibration; no BL ladder; team charter); cohesive product and central infrastructure; `#### Integration with engineering` | 243 to 257 |
| 279 | BL engineering alignment (3 bullets); self-serve on shared stack; `[End sidebar]`; managers tracking macro structure, embedding in hybrid orgs | 259 to 275 |
| 280 | Structures evolve; `### Number of reports` (flat vs "I" structures, bandwidth); `### Layering your team` (introducing a layer) | 277 to 291 |
| 281 | Sketch structure without names, narrative first; who is scaling to the call; HR partner feedback; communicating the change to each affected person (continues on p.282) | 293 to 299 |

## Table of contents: workbook (`workbook-ch4.md`)

Relevance key: **Structures** = team structures (org design, reporting lines, spans, team types, structure choices), S8. **Later** = diagnosing and changing teams, team environment, inclusion, communication, which belong to S9 to S11.

| Page | Headings and topics | md lines | Relevance |
|---|---|---|---|
| 89 | `## Chapter 4`; contents list (Career Conversations, Offsite, Snippets and Updates, Unblocking Process) | 5 to 14 | Neither (contents) |
| 90 | `## Career Conversations`; `### Duration`; `### Approach`; Pre-conversation steps 1 and 2 with scripts | 16 to 40 | Later: diagnosing team members (S9) |
| 91 | Conversation guidance; five question prompts (grew up, school, after college, favorite and least favorite job, future work) | 42 to 70 | Later: diagnosing team members (S9) |
| 92 | Future-work prompt cont.; Wrap-up; Notes | 72 to 84 | Later: diagnosing team members (S9) |
| 93 | `## Planning and Running Your Offsite`; `### Planning checklist` (1+ month, 1 month, 1 week, 1 day, day of, after) | 86 to 148 | Later: team environment (S10) |
| 94 | `### Day-of-offsite templates`; offsite structure; welcome email template; Notes | 150 to 182 | Later: team environment (S10) |
| 95 | `### Agenda` (sample offsite agenda table) | 184 to 200 | Later: team environment (S10) |
| 96 | `## Leadership Team Snippets and Updates`; actions; discussion topics; standing questions; customer issues and wins | 202 to 250 | Later: team environment and communication (S10, S11); touches leadership-team operating cadence |
| 97 | Snippets template (executive team member fields); Notes | 252 to 274 | Later: communication (S11) |
| 98 | `## Stripe's Unblocking Process`; `### First, try to solve locally` (reversible decisions; five-business-day commitment); Notes | 276 to 296 | Later: working across teams and communication (S11). Adjacent to structures: escalation runs up reporting lines |
| 99 | `### How to unblock` (document, email managers, recursive escalation); bilateral vs unilateral; manager's three questions | 298 to 338 | Later (S11). Adjacent to structures: escalation follows the management chain to a shared manager |
| 100 | Example: Charlie (widget) and Alice (storage), different managers, shared manager Bharath; Notes | 340 to 360 | Later (S11). Adjacent to structures: cross-team disagreement between two reporting lines |
| 101 | `### Fictional example document` (boxed: authors, goal, decision sought, options A and B, trade-offs) | 362 to 406 | Later (S11) |
| 102 | Example resolution: joint email, meeting, escalation to Bharath, decision; Notes | 408 to 418 | Later (S11). Adjacent to structures |

No workbook page in Chapter 4 bears directly on team structures. The nearest material is the Unblocking Process (pp. 98 to 102), whose escalation path runs along reporting lines between teams with different managers; S8 may read it for how structure routes cross-team decisions, but its home is S11.
