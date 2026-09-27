# Fable brief: the cross-chunk pass

All 33 chunks are built. Each was written on its own, so the whole has seams: tasks that duplicate each other across chunks, dependencies that point at a later phase, a few gaps, and 29 old items no chunk owned. You read across the whole task list and decide how each seam closes. You write a change list; an Opus job applies it. Don't edit the chunk files yourself.

## Read, in this order

1. `/Users/brandonacuna/Desktop/scaling-people:/CLAUDE.md` from disk. It governs.
2. `extraction/build/cross/task-index.md`: every task in every chunk, condensed (number, title, type, phase, depends on, repeatable, old items replaced). This is your main input. Open a chunk's `manual/<chunk>/tasks.md` only for a specific task when the index isn't enough to judge it.
3. `extraction/build/cross/phase-inversions.md`: 319 cases, found by script, where a task depends on a task in another chunk with a later phase.
4. `extraction/build/cross/leftovers.md`: the 29 old items with no fate.
5. `extraction/build/cross/multi-rows.md`: 17 old items with more than one mapping row.
6. The "Notes for the cross-chunk pass" line in `extraction/build/HANDOFF.md`: seams the build already noticed.

Don't read considerations, session guides, digests, the white paper, or the archive. This pass works from the task lists.

## What to decide

**1. Duplicates.** Find tasks in different chunks that ask the same question or produce the same thing. The known ones are in the handoff notes; there will be more (founders' interviewer training, career conversation guides and kits, review kits, the lead's plan, counsel registers, check-in and coaching inserts, working-with-me additions). For each: which task keeps the work (usually the chunk the book puts it in, or the earlier phase), and what happens to the other: **remove** it (its dependents point at the keeper), or **narrow** it (rewrite its title and done-when to the part that is genuinely that chunk's, and make it depend on the keeper). Prefer narrowing when the second chunk adds a real angle; remove when it adds nothing. One kit per repeatable deliverable.

**2. Phase inversions.** Triage all 319. Most will be one of:
- *Loose*: the dependency is context, not a prerequisite. Change: drop it from "Depends on" (or reword as "reads" in done-when).
- *Partial*: only the policy half is needed early. Change: split the prerequisite into a policy task (earlier phase) and a practice task, or move the dependent later.
- *Real and mis-phased*: one of the two tasks has the wrong phase. Change: move it.
Group by pattern where you can ("all dependencies on 5.5 mechanism tasks from before-the-first-hire tasks in 3.x: ..."); you don't need a separate paragraph per line, but every inversion must be covered by some change or an explicit "loose, drop dependency" group.

The phase rule: *Before the first hire* covers anything a candidate sees or relies on at the first interview, and the two operating leads are the first hires. Policies promised to candidates or legally required come before the first hire even when the practice is after opening.

**3. Gaps.** Things the whole needs that no chunk holds. At least: the "not currently available" state (17tn048qg2a); the rule that the house never rewrites or translates a person's own words (17tn048qc3y); the optional candidate pulse (old S5 section 6.4). Add a task in the right chunk, or say why it's not needed.

**4. The 29 leftover old items.** For each, one fate: served by an existing task (name it; it gets the ID on its "Replaces old items" line), a new task (write it in full, in the tasks.md format), or dropped (brand-dependent, machinery, or duplicate; say which). Record which chunk's `mapping.md` gets the row (the chunk whose task serves it; for drops, the nearest chunk).

**5. The 17 multi-row items.** For each, confirm the pairing is a route and its receipt (fine as is) or say which row to remove.

**6. Volume.** 781 tasks is a lot to put in ClickUp. Where a chunk has several deliverables that would always be built together (4.8.18 to 4.8.22 is the named case), propose merging them into one. Never merge decisions: one real decision per Decision task stays the rule.

## What to write

One file: `extraction/build/cross/changes.md`. Sections, in this order:

1. **Summary**: counts of each change type, and the task count before and after.
2. **Changes by chunk**, in chunk order. Under each chunk, one bullet per change, each self-contained so an Opus agent can apply it without judgment:
   - `REMOVE 3.2.13. Keeper: 3.1.15. Repoint dependents to 3.1.15. Move its old items to 3.1.15.`
   - `NARROW 4.6.25. New title: ... New done-when: ... Add dependency: 4.4.15.`
   - `PHASE 5.5.13: Before the first hire -> Hiring and training. Reason: ...`
   - `DEPS 3.3.12: drop 5.5.21 (loose).`
   - `SPLIT 5.5.8 into 5.5.8 (policy, Before the first hire: title, done-when) and new task (practice, phase: title, done-when, depends on 5.5.8).`
   - `ADD <chunk>: new task, full text in tasks.md format, placed after <number>.`
   - `MERGE 4.8.18, 4.8.19, 4.8.20 into 4.8.18. New title: ... New done-when: ... Old items: union.`
   - `MAPPING <chunk>: add row | id | name | fate | goes to | reason |` or `remove row for <id>`.
   Don't renumber in your list; the apply step renumbers each chunk at the end and rewrites every reference.
3. **Leftover items**: a table, one row per ID: fate, task, mapping chunk.
4. **Judgment calls**: short list of anything you weren't sure about, for Brandon to see.

## Rules

- The rule in CLAUDE.md holds: you are restructuring the work list, not deciding anything for Brandon. When two duplicate tasks framed a decision differently, keep the framing that leaves the most options open, and note the other framing as an option to carry in the keeper's session brief (list these in "Judgment calls"; the apply step won't touch session files).
- Plain English, sentence case, no em dashes, "customer" never "guest", no daypart code names, no financial figures, no retired marks, no task titled "Ratify". New task titles start with a verb.

## When you finish

Grep `changes.md` for em dashes and the banned words and fix any hits. Reply briefly: counts by change type, task count before and after, how the 29 leftovers landed (served, new, dropped), and the judgment calls.
