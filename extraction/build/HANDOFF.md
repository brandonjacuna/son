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

## State (updated 2026-09-27)

- **All 33 chunks built and verified.** The book yields 33 chunks, not 30.
- **Cross-chunk pass done** (`extraction/build/cross/changes.md`, applied): 781 tasks became 764. All 547 old items have exactly one fate and a landing task. Judgment calls for Brandon are in section 5 of `changes.md`.
- New tasks from the pass have no session brief yet; each is listed in its chunk's `session.md` parking lot ("New in the cross-chunk pass").
- **Next: the ClickUp rebuild**, from the Mac (REST token). Show Brandon the full list before deleting any old item. Then retire the old docs and write the README.

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
4. **Profiles:** copy the approved Box files still missing (see CLAUDE.md), verify by byte size, and report sensitive-content findings before committing. Current state:
   - Learning & Development: 5 of 7 in the repo, verified byte-exact, with no sensitive findings. Still missing: `assessment-and-competency-designer.md` (Box `2349454588688`, 39743 bytes) and `curriculum-and-program-architect.md` (Box `2349344483137`, 23725 bytes). The permission check blocked both fetches.
   - People & Culture: 1 of 8 on disk, unverified and gitignored (`emerging-leader-advocate.md`; it may carry a stray trailing `</output>` tag). Re-fetch all 8.
   - Founder Development Plan: none copied (6 files).
   - Copying tip: the Box connector's result wrapper can leak a trailing `</output>` into the written file, and the Write tool can add a trailing newline. Check byte size and trim.

## Opening prompt for the fresh session

> Sŏn operational buildout. Read extraction/build/HANDOFF.md and continue the chunk build with the lean pipeline.
