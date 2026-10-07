---
name: book-ingest
description: "Turn Brandon's reading of a reference book (first use: Tobin Ellis, Bar Design Essentials) into structured, paraphrased notes in a kb sub-folder. Use when he says he read a chapter or topic, pastes highlights, or sends photos of a diagram."
---
# Book ingest

Target folder for Ellis: `kb/bar/tobin-ellis/`. Read its README first; follow its rules.

## Steps
1. **Pick the topic.** If Brandon did not name one, open `toc.yaml` and offer the next three Priority A topics with `needs-book` status in one AskUserQuestion.
2. **Collect his input.** Any of these:
   - He dictates what he took from it (answer "Other" in the pop-ups).
   - He pastes his own highlights into the chat. Read them for meaning; never store them verbatim.
   - He sends photos of a diagram or dimension table. Extract only the numbers and labels; tell him to file the photo in Box `…/04. Property and Build-Out/Reference/Bar Design Essentials/`.
3. **Interview, one question at a time** (the `interview` skill rules apply). Cover:
   - What is the core idea, in one sentence?
   - What numbers or dimensions does it give? (Ask for units and page.)
   - What does Ellis say not to do?
   - Does this change anything in our current bar concept? (Offer: "Yes, changes the layout" / "Yes, adds a requirement" / "No change" / "Not sure")
4. **Write** `book-notes/<topic-slug>.md` from `book-notes/_template.md`, in paraphrase. Set `toc.yaml` status to `done`.
5. **Propagate.**
   - New numbers go to `dimensions.md` book table with page.
   - Update or supersede lines in `principles.md` (tag `[book]`, cite the page).
   - If the idea should become a test, add it to `son-bar-review-checklist.md`.
   - If it changes a current design, add a line to `decisions/open.md` and name the sandbox affected.
6. **Report** in three lines: what was captured, what changed, what to read next.

## Limits
- No copied passages from the book in any repo file. Short terms of art in quotes are fine.
- Model: Sonnet. Dimension extraction from photos can go to the `intake-triage` subagent (Haiku).
