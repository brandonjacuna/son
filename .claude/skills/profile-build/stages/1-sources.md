# Stage 1: Sources (Sonnet scouts, Brandon checkpoint)

In `revise` mode do step 3 only (write the old-profile rows), then go to stage 2.

1. One scout per research target in `00-frame.md`, all in one message so they run in parallel. Brief: "Read `.claude/skills/profile-build/workers/scout.md` and follow it. Build: <folder>. Target: <text>. Known: <sources>." Use `model: sonnet`.
2. Scouts return tables (1.5 KB each). Curate into `01-sources.md`: 5 to 15 sources total (rebuilds: the old profile plus 3 to 8 new), each row `NN | citation | grounds which target | readable at | verified`. Add an "Excluded" list with one reason each.
3. Rebuild, revise, merge: list each old profile as a source row (`NN | old: <file> | all targets | repo path | n/a`).
4. Checkpoint: one pop-up to Brandon showing the list (citations only) with three options: go, cut some (he names them), add some. This is the one checkpoint that shapes everything after it.
5. Log scout tokens in `BUILD.md`.
