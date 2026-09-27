# Opus brief: apply the cross-chunk change list

Read `/Users/brandonacuna/Desktop/scaling-people:/CLAUDE.md` from disk first. Then read `extraction/build/cross/changes.md`. Apply every change in its "Changes by chunk" section, and the leftover-item rows, to the files under `manual/`. You apply; you don't re-judge. If a change is ambiguous or can't be applied as written, skip it and list it in your reply.

## How to apply each change type

- **REMOVE**: delete the task's `###` block from `tasks.md`. Everywhere in `manual/` and `kits/` that cites the removed number (Depends on lines, session briefs, considerations, mapping "Goes to" cells, decisions headings), repoint to the keeper. Move its "Replaces old items" IDs onto the keeper's line, and update those IDs' mapping rows to point at the keeper. In `session.md`, delete the removed task's brief and add one line to the keeper's brief: "Also covers what <removed title> asked (from <chunk>)." In `decisions.md`, delete its section (these are all still open).
- **NARROW**: rewrite the title and done-when as given; add the dependency. Update the matching heading in `session.md` and `decisions.md`.
- **PHASE**: change the Phase line.
- **DEPS**: edit the Depends on line as given.
- **SPLIT / ADD**: insert the new task block where the change says, with a placeholder number `<chunk>.X1`, `<chunk>.X2`, and so on (unique within the chunk). If it is a Decision, add an open section to `decisions.md` with the same placeholder heading. Don't write session briefs for new tasks; add a line to `session.md`'s parking lot: "New in the cross-chunk pass: <placeholder> <title>; brief to be written."
- **MERGE**: keep the first task's block with the new title and done-when; union the old items; remove the others as with REMOVE, repointing to the kept one.
- **MAPPING**: add or remove the row as given in that chunk's `mapping.md`. For a leftover item served by an existing task, also add its ID to that task's "Replaces old items" line.

Never touch a `decisions.md` section whose Status is not `open` (2.2 holds a recorded ruling). Don't edit `book.md`, or `considerations.md` beyond repointing numbers.

## Then renumber and check

1. Run `python3 extraction/build/renumber.py --dry`. If it reports stale references, repoint them (they cite a removed task) and run it again until clean.
2. Run `python3 extraction/build/renumber.py`. It renumbers every chunk in document order and rewrites every reference.
3. Run `python3 extraction/build/verify.py <run>` for every run (`s01 s03 s04 ... s16`, the folders in `extraction/build/`). Fix anything it reports.
4. Check the task count against `changes.md`'s "after" figure.

Don't commit. Reply with: changes applied by type, changes skipped and why, the final task count, and verify results.
