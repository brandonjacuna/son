# Tobin Ellis: bar design sub knowledge base

Source body: Tobin Ellis (Studio Barmagic), *Bar Design Essentials: How to Design Bars That Work for Everyone* (Barmagic LLC), plus his public interviews, articles, and the Perlick Tobin Ellis Signature Series equipment he co-designed.

Brandon owns the ebook in Apple Books. Two Apple Books listings exist: "Bar Design" (released July 16, 2025, 211 pages) and "Bar Design Essentials" (the current edition, also sold as a 250-page hardcover). Check which one is on the shelf; `toc.yaml` follows the current edition's published table of contents.

## Source tiers (every fact is tagged)
| Tag | Meaning | Trust |
|---|---|---|
| `[book]` | From Brandon's own reading notes on the book, with page or topic reference | Highest. Ellis in his own framework |
| `[ellis-public]` | Ellis in his own words in an interview, article, or book excerpt he published | High |
| `[ellis-equipment]` | Spec sheets and descriptions of equipment Ellis co-designed with Perlick | High for dimensions of that equipment |
| `[perlick-training]` | Perlick's own bar design training, which teaches the same zero-step school | Medium. Aligned with Ellis, not authored by him |
| `[derived]` | Claude's application to Sŏn. Not Ellis. | Treat as a proposal |

## Files
- `principles.md`: the core philosophy, organized by the book's sections. Public layer now; book notes fill the gaps.
- `dimensions.md`: every number with its source. Book dimensions slot in as Brandon reads.
- `son-bar-review-checklist.md`: the test every Sŏn bar concept must pass. `[derived]` from the principles.
- `toc.yaml`: all book topics, priority for Sŏn, and status (public-covered, needs-book, done).
- `book-notes/`: one file per topic Brandon reads, from `book-notes/_template.md`.
- `sources.md`: every public source with date and URL.

## Rules for this folder
1. **Paraphrase only.** Never paste passages from the book into the repo, even from Brandon's highlights. Record the idea in your own words, the numbers, and the page. Short quoted phrases are fine when the exact term matters ("zero-step").
2. Dimensions, clearances, and counts are facts: record them exactly, with page and unit.
3. When a `[book]` note conflicts with a public or `[perlick-training]` fact, the book wins. Mark the older line `superseded`.
4. Book diagrams and page photos (if Brandon takes any for his own reference) live in Box, not the repo. The repo holds a pointer.
5. The `bar-designer` profile reads this folder first, then `kb/bar.md`.

## How Brandon's reading gets in
Run the `book-ingest` skill. It walks one topic at a time with pop-up questions, then writes the book note. Priority A topics in `toc.yaml` first: they are the ones that shape pre-lease bar concepts.
