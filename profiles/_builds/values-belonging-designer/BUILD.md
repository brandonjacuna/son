# Build: values-belonging-designer
mode: merge | started: 2026-10-09 | orchestrator: Opus 5.5 (batch 3)
cluster: people-and-culture | old: Values and Belonging Designer.md + Culture Signal Designer.md

## Worker log
| stage | worker | model | tokens (usage) | files written |
|---|---|---|---|---|
| 0 | frame + tests, all 6 seats (one agent) | fable | 222,842 shared (~37k per seat) | 00-frame.md, 00-tests.md |
| 2 | extract Values and Belonging (01) | sonnet (profile-extractor) | 32,919 | 4 cards |
| 2 | extract Culture Signal (02) | sonnet (profile-extractor) | 39,752 | 4 cards |
| 5 | baselines T1-T3, 5 seats in one runner | sonnet (profile-runner) | 25,379 shared (~5k per seat) | tests/T*-base.md |
| 3 | drafter | opus | 99,208 | agent.md 11,143 B; reference, provenance |
