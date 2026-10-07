# Session 16 extraction notes

Mechanical extraction for Session 16 (Conclusion: You). Sources read only; nothing in `sources/` was modified. PyMuPDF (fitz), per the chapter map's tooling note.

## Outputs

| File | Content |
|---|---|
| `extraction/s16/book-484-503.md` | Book pp. 484 to 503, 20 page markers (`<!-- p.N -->`). `##` marks the 21.2pt section heads; `>` marks 16.9pt pull quotes; `<small>` marks 11.2pt attributions and note markers. Pull quotes that cross a page break are split across two `>` lines |
| `extraction/s16/book-raw.txt` | Raw `page.get_text()` per page with `===== Book page N =====` separators |
| `extraction/s16/p484.png` | Render of p.484 |

## Census and boundaries

- Font census, pp. 484 to 503: body 15.0pt; pull quotes 16.9pt; attributions and notes 11.2pt; section heads 21.2pt; one 25.0pt head ("Notes", p.503). Same scale as S3's range, not S5's.
- p.484 is a full-page image with no text layer: the chapter title page, "6 / Conclusion / You" (confirmed visually). The PDF outline titles it "Conclusion—You".
- Outline: Manage your time and energy (p.485), Foster relationships (p.491), Consider your career (p.498), Notes (p.503). p.504 opens the Bibliography, outside the range.
- The prose ends on p.503 with her closing on fundamentals; note 77 (a Horowitz citation) is on p.503.
- Pull quotes: Dan Weiss (pp. 490 to 491, contains profanity: do not reproduce), Charles Phillips (pp. 492 to 493), Sam Hawgood (pp. 494 to 495), Dongping Zhao (p.502).
- No figures in range other than the title page. No financial figures in range.

## Workbook

The workbook has no Conclusion section. Its last exercise is the Managing Out Checklist (p.124); p.125 is the publisher's back page. A text search of all 125 pages for "Conclusion", "time and energy", "your career", "Foster relationships", and "energy audit" found no "You" exercise. The Chapter 1 exercises (workbook pp. 3 to 10: the values exercise, work style, strengths) are the ones her Conclusion points back to; Session 1 answered them (`extraction/s01/workbook.md`, S1 page section 8).
