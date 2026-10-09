# Build: environmental-signage-specialist
mode: revise | started: 2026-10-09 | orchestrator: Opus 5.5 (batch 3)
cluster: build-out | old: 06_Environmental_Signage_Specialist_Profile.md

## Worker log
| stage | worker | model | tokens (usage) | files written |
|---|---|---|---|---|
| 0 | frame + tests, all 6 seats (one agent) | fable | 222,842 shared (~37k per seat) | 00-frame.md, 00-tests.md |
| 2 | extract old profile (01) | sonnet (profile-extractor) | 28,990 | 4 cards (ADA dims and LRV figures marked no source) |
