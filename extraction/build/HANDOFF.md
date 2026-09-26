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

## State (updated 2026-09-26, second build session)

- Steps 1 and 2 (digest, book.md) are done for every run.
- Verified and complete: 0, 1.2, 1.3, 1.4, 2.1, 2.2, 2.3.
- Everything else needs step 3 (Fable), then step 4 (Opus mapping), step 5 (seed.py), step 6 (verify). For s01, step 3 and 4 cover 1.1 only; its seven unmapped items are 86akh2qua, 86akh2qvr, 86akh2r18, 86akh2r2x, 86akh7rp2, 86akhb2t7, 86akht17t.
- Fable order: s08 and s01 started first, then book order: s05, s06, s07, s09, s10, s11, s12, s13, s14, s15, s16. Check `git log` and each chunk folder for which files exist.
- Notes for the cross-chunk pass: Chapter 4 exercises (career conversations, offsite planning, snippets, unblocking) are summarized in more than one of 4.4, 4.5, 4.6; the working-with-me document appears in 1.1, 3.3, and 5.9's book summaries (1.1 owns it); 2.3.24 and 2.2.41 overlap (weekly note and quarterly memo).

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
4. **Profiles:** copy the approved Box files still missing (see CLAUDE.md), verify by byte size, and report sensitive-content findings before committing. Current state:
   - Learning & Development: 5 of 7 in the repo, verified byte-exact, with no sensitive findings. Still missing: `assessment-and-competency-designer.md` (Box `2349454588688`, 39743 bytes) and `curriculum-and-program-architect.md` (Box `2349344483137`, 23725 bytes). The permission check blocked both fetches.
   - People & Culture: 1 of 8 on disk, unverified and gitignored (`emerging-leader-advocate.md`; it may carry a stray trailing `</output>` tag). Re-fetch all 8.
   - Founder Development Plan: none copied (6 files).
   - Copying tip: the Box connector's result wrapper can leak a trailing `</output>` into the written file, and the Write tool can add a trailing newline. Check byte size and trim.

## Opening prompt for the fresh session

> Sŏn operational buildout. Read extraction/build/HANDOFF.md and continue the chunk build with the lean pipeline.
