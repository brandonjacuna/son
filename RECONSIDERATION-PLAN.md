# Scaling People: reconsideration plan

Draft for Brandon's review, 2026-09-26. Nothing in ClickUp has been changed. Everything described here is proposed.

## 1. The goal, restated

The book is the manual. The output is the work it tells you to do: one parent task in ClickUp ([Sŏn Operational Systems Build Out](https://app.clickup.com/t/86akh1hdg)), with lettered chunks in the book's order, and inside each chunk the **decisions**, **actions**, and **deliverables**. No decisions made for you. Where the white paper gives a reasonable answer, the decision task carries it as a labelled **default assumption** to save you time. The research, context, and considerations live as markdown in a GitHub repo, not in ClickUp.

Brand guidelines and the experiential deck are out of scope, because there is no property yet.

## 2. What exists today

A full, verbatim export was taken this morning, read-only, before anything else: `archive/clickup-export-2026-09-26/`. Every item below is in it, including comments.

| Where | What | Size |
|---|---|---|
| ClickUp, Operating System doc | 17 pages: an index plus one synthesis page per session (S1 to S16) | about 3.0 million characters |
| ClickUp, tracker doc | 1 page: program protocol and context ledger | 135,000 characters |
| ClickUp, build-out parent | 400 subtasks, 399 open | 418,000 characters of descriptions, 213 comments |
| ClickUp, Carryover Register | 147 tasks, all open | 168,000 characters of descriptions, 116 comments (123,000 characters) |
| ClickUp, session tasks | 17 (S1 to S16 done, S17 open) | small |
| Local | clean text extraction of the book (pp. 9 to 503) and workbook, by session; Fable briefs; local copies of every page; scripts | about 28 MB |

### What's in the synthesis pages

Each session page has four kinds of material mixed together:

1. **What the book says.** Her concepts, frameworks, and exercises, by chapter. Valuable: this is the manual.
2. **Research and considerations.** How a concept lands in a 120-seat restaurant with four service periods, a revenue share instead of tips, and a chef partnership. Floor realities, legal and counsel questions (31 logged), failure modes, sequencing. Valuable: this is what saves you time.
3. **Team positions.** Roughly 700 items marked "Recommended," about 130 "Founder-gated," and about 45 "Chef-gated." This is the drift: verdicts written for you to ratify.
4. **Program machinery.** Carryover routing, ledger bindings, the 213-row readiness test, and cross-session rulings. It served the extraction process, not the build.

### What's in the 400 build-out subtasks

| Type | Count | Note |
|---|---|---|
| Founder decision | 118 | Many are "Ratify X" rather than "Decide X" |
| Instrument | 94 | Nearly all "gated on `86ajgn2z5`" |
| Process | 60 | |
| Structure | 25 | |
| Document | 22 | |
| Untyped (early sessions) | 81 | Also mostly "Ratify ..." or "Rule whether ..." |

At least 65 task names ask you to *ratify* a team position. The descriptions usually hold good context (the book's point, the white paper's commitment, the open question) and then the team's verdict.

### Brand and experiential influence

A keyword count finds about 180 direct references to brand canon, the deck, or experiential guidelines across the pages, plus 13 subtasks and 6 carryovers. That undercounts it. The deeper influence is vocabulary and assumptions carried from the brand work: named rooms, rituals, "the house's languages," and seat names. Finding that takes reading, not searching, so the reconsideration pass reads each chunk in full.

## 3. What happens to each thing

Nothing is deleted until its content is preserved in the repo and you've approved the chunk.

| Thing | Fate |
|---|---|
| Book and workbook extractions | Kept. They become each chunk's `book.md` source. |
| Session synthesis pages | Rewritten into the repo, one folder per chunk. Kept: what the book says, research, considerations, counsel questions. Converted: each team position becomes an **option with its reasoning**, not a verdict. Removed: brand and experiential detail, program machinery. Originals stay verbatim in the archive. |
| 400 subtasks | Each one is mapped to a chunk and given a fate in a table in the repo: *keep as is*, *rewrite* (e.g. "Ratify X" becomes "Decide X", with the white-paper default), *merge*, or *drop* (brand-driven, machinery, or duplicate). Old tasks are deleted only after the new ones exist and the mapping is approved. |
| Carryover Register | Yes, it was only for the extraction sessions: it carried context from one session to the next. Anything in it that matters to the build gets folded into the chunk it touches as a "related" note. Then the list is archived. |
| Operating System doc and tracker doc | Once their content is in the repo, archived in ClickUp. I recommend archiving rather than deleting, so old links don't break. |
| Session tasks | Closed and left as a record, or archived with the doc. |
| CLAUDE.md | Rewritten for the new program: the book as manual, the white paper as the only Sŏn context, no positions, and brand files excluded. |

## 4. What could be lost

Be clear-eyed about these before approving:

- **Verdicts.** When a position becomes an option, the team's "we'd do it this way" drops out of the working manual. The reasoning stays. The original verdict stays in the archive.
- **Brand- and experiential-derived ideas.** Some may matter later, once there's a property. They leave the working manual but stay in the archive, searchable.
- **Live ClickUp history.** Comment threads, task links, and created dates on deleted tasks. They survive only in the export JSON, not in ClickUp. ClickUp keeps deleted tasks in trash for 30 days.
- **Cross-session connections.** The carryovers tied early decisions to late ones. The repo keeps them as "related" links between chunks, but only the ones that matter to the build.
- **The readiness test (213 rows).** This is a pre-opening checklist built as program machinery. Proposal: keep it as a deliverable file in the repo, stripped of brand rows, and let you decide whether it becomes a task.

## 5. The chunks

The sixteen sessions already map one to one onto the book's sections, so each chunk has a clean source:

| Chunk | Book section | From session |
|---|---|---|
| A. Founder operating principles and working styles | Intro, Ch1 | S1 |
| B. Founding documents | Ch2 | S2 |
| C. The operating system: goals, planning, metrics | Ch2 | S3 |
| D. Operating cadence | Ch2 | S4 |
| E. Recruiting | Ch3 | S5 |
| F. Hiring and interviewing | Ch3 | S6 |
| G. Onboarding | Ch3 | S7 |
| H. Team structures and roles | Ch4 | S8 |
| I. Diagnosing and changing teams | Ch4 | S9 |
| J. Team environment and culture | Ch4 | S10 |
| K. Communication and inclusion | Ch4 | S11 |
| L. Coaching and feedback | Ch5 | S12 |
| M. Performance reviews and compensation | Ch5 | S13 |
| N. High, middle, and low performers | Ch5 | S14 |
| O. Managing managers and managing out | Ch5 | S15 |
| P. Founder sustainability | Conclusion | S16 |

Each chunk in ClickUp: a subtask named "A. Founder operating principles and working styles", holding tertiary tasks named `A1. Decide ...`, `A2. Write ...`, and so on, each typed decision, action, or deliverable.

Each chunk in the repo:

```
manual/A-founder-operating-principles/
  book.md            what the book says, and the workbook exercises
  considerations.md  research, options, white-paper assumptions, counsel questions
  tasks.md           the chunk's decisions, actions, deliverables (mirrors ClickUp)
  mapping.md         fate of every old subtask and carryover that touched this chunk
```

## 6. Sequence, with your checkpoints

1. **Export snapshot.** Done.
2. **GitHub.** Create a private repo and push the current folder as the baseline, minus the brand files, so history starts before any rewrite. You need to do one step here: the GitHub CLI isn't installed on this Mac, so either install it and sign in, or create an empty private repo and send me its URL.
3. **Pilot chunk A.** Fable reads the chunk-A book text, the S1 page, the subtasks and carryovers that touch it, and the white paper, then produces the four files. **You review it.** That review sets the pattern for the other fifteen.
4. **Chunks B to P.** Run in batches, each reviewed.
5. **ClickUp rebuild.** Create the lettered chunks and their tasks, then delete old subtasks per the approved mapping.
6. **Retire.** Archive the Carryover Register, the Operating System doc, and the tracker doc. Rewrite CLAUDE.md.

Cost note: step 3 onward is the heavy Fable work, about 3 million characters of synthesis re-read across sixteen chunks. The pilot shows the real cost per chunk before committing to the rest.
