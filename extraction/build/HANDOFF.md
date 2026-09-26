# Handoff: building the remaining chunks

Written 2026-09-26 by the session that ran the pilot. Read `CLAUDE.md` and `RECONSIDERATION-PLAN.md` first.

## The goal: Brandon ready to work from the cloud repo

The build is done when Brandon can open a session on `brandonjacuna/son-operational-buildout` from any device (claude.ai/code included), pick a chunk, and start the conversational working session, with every task in place. Concretely:

1. **All 30 chunks built and verified**: seven entries each, rules clean, every old item mapped once.
2. **Cross-chunk pass done**: dependencies, duplicates, phases, and the 29 leftover old items placed.
3. **ClickUp rebuilt**: `86akh1hdg` holds the 30 numbered chunks, each holding its typed tasks with phase tags and dependencies. Old subtasks handled per the mappings, the Carryover Register and old docs archived, all with Brandon's go-ahead.
4. **Repo README**: what this is, how a working session runs, the chunk index with status and phase, a suggested starting order, and the opening prompt for a working session.
5. **Cloud-ready**: everything a session needs is in the repo. Local-only things don't reach the cloud: the REST token (`~/.clickup_token`), Box, and Claude's memory files on the Mac. So working sessions use the ClickUp connector (a handful of calls each), and every rule lives in CLAUDE.md.
6. **Profiles copied** from Box and verified (optional for starting; useful from chapter 3 on).

Bulk ClickUp work (step 3) runs from the Mac, where the REST token is. Everything after that can run anywhere.

## State (all agents stopped, 2026-09-26)

Every agent from the prior session is stopped; none is running. On disk:

| Chunk | Files present | What's left |
|---|---|---|
| 2.1 | all | Done and verified (pilot) |
| 0, 1.2, 1.3, 1.4 | all six | Written by the old full-Fable pipeline; **not yet verified** (step 6) |
| 2.2 | book, considerations, tasks, mapping, decisions | `session.md` (step 3, session only). Verify `tasks.md` is complete: the agent was stopped around when it was writing a 41-task list |
| 2.3 | book, considerations, tasks, mapping, decisions | `session.md` (step 3, session only) |
| 1.1 | none | Full lean pipeline for 1.1 only (run `s01`; steps 1 and 2 cover the run, and the other chunks' files are already written) |
| 3.1, 3.2 | a Fable-written `book.md` | Full lean pipeline from step 1 (runs `s05`, `s06`); step 2 overwrites `book.md` |
| 3.3 to 6.3 | none | Full lean pipeline (runs `s07` to `s16`) |

For a step-3 job covering only part of a run, tell the Fable agent which chunks and which files to write, and to leave existing files alone.

Leftover old items: 29 belong to no single session (S2 items outside the 2.1 pilot, and carryovers meant for the old assembly session). The cross-chunk pass places them.

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
