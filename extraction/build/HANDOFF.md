# Handoff: building the remaining chunks

Written 2026-09-26 by the session that ran the pilot. Read `CLAUDE.md` and `RECONSIDERATION-PLAN.md` first.

## State

- **Done:** 2.1 (pilot, all files). 0 (built by the old full-Fable pipeline).
- **May still be running, or finished, from the prior session** (old pipeline; Fable wrote every file): run `s01` (1.1 to 1.4), `s03` (2.2), `s04` (2.3). Check each folder in `manual/` for all six files plus `notes/`. If a folder is incomplete, finish it with the lean pipeline below: skip steps already done, and run step 3 only for the missing thinking files.
- **Stopped mid-write to save budget:** `s05` (3.1) and `s06` (3.2). Each has at most a Fable-written `book.md`. Run the lean pipeline from step 1; step 2 overwrites `book.md`.
- **Not started:** `s07` to `s16` (3.3 to 6.3).
- **Leftover old items:** 29 old items belong to no single session. They're listed at the end of `extraction/item-sessions.json` processing, and `RECONSIDERATION-PLAN.md` covers them. The cross-chunk pass places them.

## The lean pipeline, per run (`extraction/build/<run>/`)

| Step | Model | Brief | Output |
|---|---|---|---|
| 1 | Sonnet | `1-DIGEST-BRIEF.md` | `digest.md` in the run folder |
| 2 | Sonnet | `2-BOOK-BRIEF.md` | each chunk's `book.md` |
| 3 | Fable | `3-THINKING-BRIEF.md` | each chunk's `tasks.md`, `considerations.md`, `session.md` |
| 4 | Opus | `4-MAPPING-BRIEF.md` | each chunk's `mapping.md` |
| 5 | Script | `python3 extraction/build/seed.py` | `decisions.md`, `notes/inbox.md` |
| 6 | Controller | Verify, then commit and push | |

Steps 1 and 2 can run in parallel, and ahead of Fable for several runs at once. At most two Fable jobs run at once. Check the 5-hour window (`get_usage`) between batches.

Spawn each agent with a one-line prompt: "Read `<brief path>` and follow it exactly. Your run is `<run>`: inputs are in `extraction/build/<run>/`."

## Verify (step 6)

- All seven entries present in each chunk folder.
- No em dashes, "guest", retired marks, "Ratify", or daypart names in any file.
- Every owned old-item ID appears in exactly one mapping across the run.
- Every task number referenced in any file is defined.

## After all runs

1. **Cross-chunk pass (Fable, from the task lists only):** dependencies between chunks, duplicates, phase consistency, placing the 29 leftover old items, and confirming all 547 old items have exactly one fate.
2. **ClickUp rebuild (script via REST, `extraction/s13/cu.py`):** create the chunks as numbered subtasks of `86akh1hdg`, then their tasks with type, phase tag, and dependencies. Show Brandon the full list **before** deleting any old item. Then handle old items per the mappings.
3. **Retire:** archive the Carryover Register (`901327884538`) and the two old docs, each with Brandon's go-ahead. Write the repo README.
4. **Profiles:** copy the three approved Box folders (see CLAUDE.md), verified by byte size, and report sensitive-content findings before committing. Two partial, unverified copies are on disk and gitignored; replace them.

## Opening prompt for the fresh session

> Sŏn operational buildout. Read extraction/build/HANDOFF.md and continue the chunk build with the lean pipeline.
