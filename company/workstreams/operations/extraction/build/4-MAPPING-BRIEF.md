# Opus brief: mapping.md for each chunk in one run

Read `/Users/brandonacuna/Desktop/scaling-people:/CLAUDE.md` from disk first. Then read `extraction/build/<run>/digest.md` (Part 2 lists every old item this run owns), each chunk's `tasks.md` and `considerations.md`, and `manual/2.1-founding-documents/mapping.md` as the example.

For each chunk, write `manual/<section>-<slug>/mapping.md`:
1. A table: `| Old ID | Old name (short) | Fate | Goes to | Reason |`. Fate is one of Kept, Rewritten, Merged, Routes to X.Y, Dropped, Received from 2.1. Every item in digest Part 2 appears in **exactly one** chunk's table across the run. Items flagged brand-dependent or machinery are Dropped, with the reason. An item that belongs to a chunk outside this run is "Routes to X.Y", with one line saying what that chunk should build.
2. Where each major topic of the old page went: into this chunk, routed to another chunk, or dropped.
3. A short "What was dropped and why."

Then check mechanically: every digest item ID appears exactly once across the run's mapping files, and every task number in "Goes to" exists in a tasks.md. Fix anything off. No em dashes. Write only the mapping files. Reply with counts by fate per chunk and any items you couldn't place.
