# Worker: runner

If a seat path is given, read `<seat>/agent.md` (and `skill/SKILL.md` if present) and act as that seat: its rules are your instructions. Read its `reference/` files only if its Output section says the task needs them. If the seat is "none", do the task as a capable generalist.

Do the task exactly as written. Do not look at `tests.md`, `provenance.md`, the build folder, or any other test's output.

Write your answer to the output path, 3 KB maximum. Return only the path and one line.
