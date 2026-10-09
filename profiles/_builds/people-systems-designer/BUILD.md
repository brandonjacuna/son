# Build: people-systems-designer
mode: revise | started: 2026-10-09 | orchestrator: Opus 5.5 (batch 3)
cluster: scaling-people | old: People Systems Designer.md

## Worker log
| stage | worker | model | tokens (usage) | files written |
|---|---|---|---|---|
| 0 | frame + tests, all 6 seats (one agent) | fable | 222,842 shared (~37k per seat) | 00-frame.md, 00-tests.md |
| 2 | extract old profile (01) | sonnet (profile-extractor) | 40,796 | 4 cards (examples 2, 5, 6 not copied: cap) |
| 5 | baselines T1-T3, 5 seats in one runner | sonnet (profile-runner) | 25,379 shared (~5k per seat) | tests/T*-base.md |
