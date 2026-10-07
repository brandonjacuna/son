# Stage 5: Behavioral test (Sonnet runners, Haiku grader)

A new agent file is not callable until the next session starts, so runners load the master by reading it.

1. For each test in `tests.md` (3 to 5), spawn two runners in one message, both writing into `profiles/_builds/<slug>/tests/`:
   - with: `model: <the frame's model guess>`. Brief: "Read `.claude/skills/profile-build/workers/runner.md`. Seat: <master path>. Task: <task text>. Output: `tests/Tn-with.md`."
   - baseline (first build of a seat, and any test that failed before): `model: same`. Brief: same, with "Seat: none" and output `tests/Tn-base.md`.
2. Spawn one grader, `model: haiku`: "Read `.claude/skills/profile-build/workers/grader.md`. Tests: <path to tests.md>. Outputs: <build>/tests/." It returns a verdict table.
3. Pass means: the with-run produces the expected catch by its own reasoning (citing or clearly applying the cue or rule), AND the baseline misses it or catches it weaker. A test the baseline also passes cleanly proves nothing about the seat: replace it with a harder one, once.
4. On a fail: read only that test's with-output, find the missing or weak row, Edit it (or add one, with a provenance row), rerun that test only. Two fails on the same test go to Brandon.
5. Model line: if every test passes on the guess, rerun the cheapest lower tier on the two hardest tests. Keep the cheapest tier that passes. Record the reason in `BUILD.md`.
6. Write the verdicts into the `result` column of `tests.md`. Log tokens in `BUILD.md`.
