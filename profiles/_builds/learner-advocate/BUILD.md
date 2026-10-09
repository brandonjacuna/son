# Build: learner-advocate
mode: revise | started: 2026-10-09 | orchestrator: Opus 5.5 (batch 2)
cluster: learning-and-development | old: Learner Advocate.md

## Worker log
| stage | worker | model | tokens (usage) | files written |
|---|---|---|---|---|
| 0 | frame + tests, all 6 seats (one agent) | fable | 146,414 shared (~24k per seat) | 00-frame.md, 00-tests.md |
| 2 | extract old profile | sonnet (profile-extractor) | 32,159 | cards |
| 5 | baselines T1-T3 | haiku (profile-runner) | 13,328 | tests/T*-base.md |
