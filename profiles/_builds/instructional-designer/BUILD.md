# Build: instructional-designer
mode: merge | started: 2026-10-09 | orchestrator: Opus 5.5 (batch 2)
cluster: learning-and-development | old: Instructional Designer.md + HighScope.md

## Worker log
| stage | worker | model | tokens (usage) | files written |
|---|---|---|---|---|
| 0 | frame + tests, all 6 seats (one agent) | fable | 146,414 shared (~24k per seat) | 00-frame.md, 00-tests.md |
| 2 | extract Instructional Designer (01) | sonnet (profile-extractor) | 37,882 | cards |
| 2 | extract HighScope (02) | sonnet (profile-extractor) | 30,649 | cards |
| 5 | baselines T1-T3, 5 seats in one runner | sonnet (profile-runner) | 23,366 shared (~4.7k per seat) | tests/T*-base.md |
| 3 | drafter | opus | 91,020 | agent.md 11,505 B; reference 7.8 KB; provenance 7.1 KB (53 sourced, 3 inferred, 6 project) |
| 4 | critic grounding | sonnet (profile-critic) | 34,629 | 04-critic-*.md |
| 4 | critic spec+rules (2 seats) | sonnet (profile-critic) | 35,552 shared | 04-critic-*.md |
| 4 | critic seams (2 seats) | sonnet (profile-critic) | 57,724 shared | 04-critic-*.md |
| 4 | merger, 6 seats in one agent | sonnet (profile-critic) | 54,671 shared (~9k per seat) | 04-flags.md 2396 B |
| 4 | Fable judge, 6 seats + seams in one agent | fable | 160,426 shared (~27k per seat) | 04-judgment.md |
| 4 | apply judgment edits, 2 seats | sonnet (general-purpose) | 86,768 shared | agent.md, provenance, reference |
| 5 | with-runs T1-T3 | sonnet (profile-runner) | 19,165 | tests/T*-with.md |
| 5 | grader, 6 seats in one agent | sonnet (profile-grader) | 49,555 shared (~8k per seat) | verdicts: T1-T3 pass |
| 5 | haiku tier check T1, T2 | haiku (profile-runner) | 25,015 | tests/T*-haiku.md |
