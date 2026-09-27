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

Chunks follow the book's own sections, numbered so they sort in book order in ClickUp. (An earlier draft used A to P, one per extraction session. The sessions were page-budget splits, not the book's structure, so that was dropped on 2026-09-26.)

| # | Chunk | Book pages |
|---|---|---|
| 0 | Management basics checklist | 30 |
| 1.1 | Build self-awareness to build mutual awareness | 35 |
| 1.2 | Say the thing you think you cannot say | 52 |
| 1.3 | Distinguish between management and leadership | 56 |
| 1.4 | Come back to your operating system | 60 |
| 2.1 | Founding documents | 71 |
| 2.2 | The operating system | 84 |
| 2.3 | Operating cadence | 135 |
| 3.1 | Recruiting | 171 |
| 3.2 | Hiring | 193 |
| 3.3 | Onboarding | 216 |
| 3.4 | Hiring mistakes | 224 |
| 4.1 | Team structures | 262 |
| 4.2 | Diagnosing team state | 282 |
| 4.3 | Team changes and restructuring | 286 |
| 4.4 | (Re)building the team | 294 |
| 4.5 | Creating the team environment | 304 |
| 4.6 | Team-building complexities | 331 |
| 4.7 | Diversity and inclusion | 354 |
| 4.8 | Team communication | 360 |
| 5.1 | Hypothesis-based coaching | 382 |
| 5.2 | Giving hard feedback | 391 |
| 5.3 | Creating a culture of informal feedback | 395 |
| 5.4 | The formal review process | 399 |
| 5.5 | Compensation | 413 |
| 5.6 | Managing high performers | 419 |
| 5.7 | The steady middle | 431 |
| 5.8 | Managing low performers | 432 |
| 5.9 | Managing managers | 449 |
| 5.10 | Managing out, firing, and layoffs | 454 |
| 6.1 | Manage your time and energy | 485 |
| 6.2 | Foster relationships | 491 |
| 6.3 | Consider your career | 498 |

Each chapter's exercises and templates become deliverables inside the section they serve. Every section boundary coincides with an old session boundary, so each old session page splits cleanly across the new chunks.

**Build order is carried by a phase tag, not by the chunk order.** The extraction organized the build around opening: the hiring calendar (S6), the readiness test (213 pre-opening checks), and the gates on every page. Every task gets one phase: *before the first hire*, *hiring and training*, *before opening*, or *after opening*. ClickUp can group by phase to show what's next, while the names keep the book's order for lookup. Hard dependencies (e.g. 5.5 compensation before 3.1 recruiting) become ClickUp dependencies.

In ClickUp: a chunk subtask named "2.1 Founding documents", holding tertiary tasks named "2.1.1 Decide ...", "2.1.2 Write ...", each typed decision, action, or deliverable and tagged with its phase.

In the repo:

```
manual/2.1-founding-documents/
  book.md            what the book says, and the workbook exercises
  considerations.md  research, options, white-paper assumptions, counsel questions
  tasks.md           the chunk's decisions, actions, deliverables (mirrors ClickUp)
  mapping.md         fate of every old subtask and carryover that touched this chunk
```

## 6. Sequence, with your checkpoints

1. **Export snapshot.** Done.
2. **GitHub.** Done: private repo `brandonjacuna/son-operational-buildout`, baseline pushed without the brand files.
3. **Pilot chunk 2.1 (founding documents).** Fable reads the section's book text, the S2 page, the subtasks and carryovers that touch it, and the white paper, then produces the four files. **You review it.** That review sets the pattern for the other fifteen.
4. **The remaining chunks.** Run in batches, each reviewed.
5. **ClickUp rebuild.** Create the lettered chunks and their tasks, then delete old subtasks per the approved mapping.
6. **Retire.** Archive the Carryover Register, the Operating System doc, and the tracker doc. Rewrite CLAUDE.md.

Cost note: step 3 onward is the heavy Fable work, about 3 million characters of synthesis re-read across about thirty chunks. The pilot shows the real cost per chunk before committing to the rest.

## 7. Build status

Updated 2026-09-26. Working sessions start only after the whole build below is complete. Chunk 2.1 was the example that set the pattern.

| Step | Status |
|---|---|
| 2.1 pilot (example) | Done |
| Chunks from S1, S3, S4, S5, S6 (0, 1.1 to 1.4, 2.2, 2.3, 3.1, 3.2) | Building |
| Chunks from S7 to S16 (3.3 to 6.3) | Queued |
| Cross-chunk pass (dependencies, duplicates, phases, the 29 unowned old items) | Done 2026-09-27 (764 tasks) |
| ClickUp rebuild (chunks, tasks, phase tags, dependencies; old items per mapping) | Built 2026-09-27; old items moved to a holding task, deletion pending approval |
| Archive Carryover Register and old docs; repo README | Queued |
| Box profile copies (blocked in this session; run in a fresh one) | Queued |

Build inputs live in `extraction/build/<run>/`; the shared brief is `extraction/build/BUILD-BRIEF.md`. Old-item ownership by session is in `extraction/item-sessions.json`.
