# Chapter map

**Status: reconciled 2026-09-11** against the tracker protocol (`2ky45bmy-17233`). Generated from `CLAUDE.md`'s session-sequence and workbook tables, enriched with the PDF outlines read directly from the source files.

The tracker's session sequence matched this file row for row: same task IDs, same page ranges, same profile owners. No corrections were needed. Two details were taken from the tracker and added below: the chapter-level book ranges, and the gate on S17.

Chapter and section titles below are quoted verbatim from the book's own PDF outline. Where they contain em dashes, that is the source's punctuation, not this project's.

---

## Page addressing

Book and workbook page ranges in `CLAUDE.md` are **PDF page numbers with zero offset**. Verified against both outlines: every session boundary in the table below lands exactly on an outline entry, and every workbook boundary lands exactly on a chapter transition in the running heads.

No translation layer is needed. Read the page numbers as written, directly.

| Source | File | Pages |
|---|---|---|
| Book | `sources/scaling-people-book.pdf` | 531 |
| Workbook | `sources/scaling-people-workbook.pdf` | 125 |
| White paper | `sources/robert-lerma-white-paper.pdf` | 39 |
| Brand deck | `sources/brand-guidelines-deck.pdf` | 94 |
| Brand guidelines | `sources/brand-guidelines.md` | 990 lines |

### Verified in Session 1, 2026-09-11

Session 1 extracted book pp. 9 to 69 and workbook pp. 3 to 10 and 76 to 88. Zero offset confirmed. Two outline entries in the table below were corrected against the extraction and are marked in place:

- "Setting your metronome" is on p. 17, not p. 10. The introduction's body begins on p. 10 with no heading, and the metronome heading appears seven pages in.
- "Build self-awareness to build mutual awareness" is on p. 37, not p. 35. Chapter 1's unheaded opening runs p. 35 to p. 37.

Every other boundary held.

**Extraction tooling, a correctness note.** The book PDF renders ligatures as NUL bytes under pypdf: "office" becomes `o\x00ce`, "finance" becomes `\x00nance`. Hundreds of words are corrupted and the damage is silent. **Use PyMuPDF (fitz) for `scaling-people-book.pdf`.** Its layout dictionary also exposes font size and block geometry, which is what makes headings, pull quotes, and worksheet tables recoverable. The workbook and the white paper extract cleanly under pypdf; both were checked word for word.

Three pages in the book's S1 range carry figures as raster images with no text layer: p. 42 (the work-style quadrant grid), p. 45 (the Insights Discovery wheel), and p. 67 (the work-style placement grid). Captions extract; the figures do not. Any session needing a figure's contents reads the page visually.

**Font sizes are not constant across the book, a correction added by S5.** The heading-recovery thresholds that worked for the S3 range do not transfer. S3 recorded body at 15.0pt, section headings at 21.2pt, pull quotes at 16.9pt, and table text at 11.2pt. In the S5 range, book pp. 167 to 192, the scale is entirely different: body runs at 11.1pt, sidebar headings at 15.7pt, pull quotes at 12.5pt, and captions at 8.3pt, and no 21.2pt section heading appears anywhere in the range. Several section headings in that range ("Recruiting commitments," "New employee recruiting," "Screening processes," "Referrals," "New leader recruiting," "Determine what kind of leader you need," "Promoting from within or hiring from outside") sit at body size and are not recoverable by size at all; recover them by position and context, or by the PDF outline, which in this range anchors a few pages off the printed heading. Applying S3's thresholds to a later range silently mislabels every line in it. **Run a font census over the range before extracting** and set thresholds from what it returns. Expect figures to arrive as image blocks with text captions beside them: pp. 169, 170, 179, and 192 each carry one.

---

## Session sequence

| # | Task ID | Source | Book pages | Profile owner |
|---|---|---|---|---|
| 1 | `86ajgmhd7` | Intro, Ch1 | 9 to 69 | Architect |
| 2 | `86ajgmhfd` | Ch2, Founding documents | 70 to 83 | Architect |
| 3 | `86ajgmhgx` | Ch2, The operating system | 84 to 134 | Architect |
| 4 | `86ajgmhjr` | Ch2, Operating cadence + exercises | 135 to 166 | Architect + Realist |
| 5 | `86ajgmhm4` | Ch3, Recruiting | 167 to 192 | Designer + Realist |
| 6 | `86ajgmhnt` | Ch3, Hiring | 193 to 215 | Designer + Realist |
| 7 | `86ajgmhrz` | Ch3, Onboarding + exercises | 216 to 260 | Designer + Realist |
| 8 | `86ajgmhxx` | Ch4, Team structures | 261 to 281 | Architect + Realist |
| 9 | `86ajgmj07` | Ch4, Diagnosing, changes, rebuilding | 282 to 303 | Architect + Designer |
| 10 | `86ajgmj2u` | Ch4, Team environment | 304 to 330 | Designer + Realist |
| 11 | `86ajgmj7c` | Ch4, Complexities, inclusion, communication | 331 to 380 | Designer |
| 12 | `86ajgmjba` | Ch5, Coaching, hard feedback | 381 to 398 | Designer |
| 13 | `86ajgmjey` | Ch5, Formal review + compensation | 399 to 418 | Designer + Realist |
| 14 | `86ajgmjk1` | Ch5, High/middle/low performers | 419 to 448 | Designer + Realist |
| 15 | `86ajgmjpw` | Ch5, Managing managers, managing out | 449 to 483 | Designer |
| 16 | `86ajgmjz6` | Conclusion, You | 484 to 503 | Designer |
| 17 | `86ajgmk27` | Assembly, company wiki | not applicable | All |

Parent task for the session subtasks: `86ajgmh9a`. Parent task for typed post-extraction work items: `86akh1hdg`.

**S17 is gated on the document methodology, task `86ajgn2z5`.** Assembly does not run until that lands.

---

## Book chapters, coarse index

The session ranges above are the operative ones. This table is the chapter-level view, for orienting a session that needs to know where a chapter starts and stops as a whole.

| Chapter | Pages |
|---|---|
| Introduction | 9 to 33 |
| 1. Essential Operating Principles | 34 to 69 |
| 2. Foundations and Planning | 70 to 166 |
| 3. A Comprehensive Hiring Approach | 167 to 260 |
| 4. Intentional Team Development | 261 to 380 |
| 5. Feedback and Performance Mechanisms | 381 to 483 |
| Conclusion: You | 484 to 503 |

---

## Book outline, by session

Section titles and their first page, as read from the PDF outline. Use this to confirm a session's range covers what its title claims.

### Session 1, pages 9 to 69

| Section | Page |
|---|---|
| Introduction | 9 |
| Setting your metronome | 17 |
| The core frameworks | 20 |
| Who is this book for? | 24 |
| How to read this book | 24 |
| Exercises and templates | 30 |
| Notes | 33 |
| Chapter 1—Essential Operating Principles | 34 |
| 1. Build self-awareness to build mutual awareness | 37 |
| 2. Say the thing you think you cannot say | 52 |
| 3. Distinguish between management and leadership | 56 |
| 4. Come back to your operating system | 60 |
| Exercises and templates | 63 |
| Notes | 69 |

### Session 2, pages 70 to 83

| Section | Page |
|---|---|
| Chapter 2—Core Framework 1: Foundations and Planning for Goals and Resources | 70 |
| Founding documents | 71 |

### Session 3, pages 84 to 134

| Section | Page |
|---|---|
| The operating system | 84 |

### Session 4, pages 135 to 166

| Section | Page |
|---|---|
| Operating cadence | 135 |
| Exercises and templates | 144 |
| Notes | 166 |

### Session 5, pages 167 to 192

| Section | Page |
|---|---|
| Chapter 3—Core Framework 2: A Comprehensive Hiring Approach | 167 |
| Recruiting | 171 |

### Session 6, pages 193 to 215

| Section | Page |
|---|---|
| Hiring | 193 |

### Session 7, pages 216 to 260

| Section | Page |
|---|---|
| Onboarding | 216 |
| Hiring mistakes | 224 |
| Exercises and templates | 228 |
| Notes | 260 |

### Session 8, pages 261 to 281

| Section | Page |
|---|---|
| Chapter 4—Core Framework 3: Intentional Team Development | 261 |
| Team structures | 262 |

### Session 9, pages 282 to 303

| Section | Page |
|---|---|
| Diagnosing team state | 282 |
| Team changes and restructuring | 286 |
| (Re)building the team | 294 |

### Session 10, pages 304 to 330

| Section | Page |
|---|---|
| Creating the team environment | 304 |

### Session 11, pages 331 to 380

| Section | Page |
|---|---|
| Team-building complexities | 331 |
| Diversity and inclusion | 354 |
| Team communication | 360 |
| Exercises and templates | 363 |
| Notes | 378 |

### Session 12, pages 381 to 398

| Section | Page |
|---|---|
| Chapter 5—Core Framework 4: Feedback and Performance Mechanisms | 381 |
| Hypothesis-based coaching | 382 |
| Giving hard feedback | 391 |
| Creating a culture of informal feedback | 395 |

Note: the session title in `CLAUDE.md` names coaching and hard feedback only. The range also carries "Creating a culture of informal feedback." Treat it as in scope for S12.

### Session 13, pages 399 to 418

| Section | Page |
|---|---|
| The formal review process | 399 |
| Compensation | 413 |

### Session 14, pages 419 to 448

| Section | Page |
|---|---|
| Managing high performers | 419 |
| The steady middle | 431 |
| Managing low performers | 432 |

### Session 15, pages 449 to 483

| Section | Page |
|---|---|
| Managing managers | 449 |
| Managing out, firing, and layoffs | 454 |
| Some final thoughts on management | 465 |
| Exercises and templates | 467 |
| Notes | 483 |

### Session 16, pages 484 to 503

| Section | Page |
|---|---|
| Conclusion—You | 484 |
| Manage your time and energy | 485 |
| Foster relationships | 491 |
| Consider your career | 498 |
| Notes | 503 |

### Outside the session sequence

| Section | Page |
|---|---|
| Bibliography | 504 |
| Acknowledgments | 506 |
| Index | 511 |
| About the Author | 531 |

---

## Workbook

Chapter boundaries confirmed against the running heads on each boundary page.

| Chapter | Workbook pages | Confirmation |
|---|---|---|
| Chapter 1 | 3 to 10 | p3 opens Ch1, p10 is the last Ch1 page |
| Chapter 2 | 11 to 41 | p11 opens Ch2, p41 is the last Ch2 page |
| Chapter 3 | 42 to 88 | p42 opens Ch3, p88 is the last Ch3 page |
| Chapter 4 | 89 to 102 | p89 opens Ch4, p102 is the last Ch4 page |
| Chapter 5 | 103 to 125 | p103 opens Ch5, p125 is the last page |

Pages 1 and 2 are front matter.

---

## Optional profiles

If a session hits depth gaps in subject matter, most likely S8 or S12 to S14, prompt Brandon before loading. These live in Box folder `400281721352` and load only on explicit approval.

- Performance and Feedback Systems Designer
- HR Systems Designer
