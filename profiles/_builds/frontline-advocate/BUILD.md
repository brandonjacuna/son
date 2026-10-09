# Build: frontline-advocate
mode: merge | started: 2026-10-09 | orchestrator: Opus 5.5 (batch 1; session also carried earlier phase 3 work)
cluster: people-and-culture | old: Frontline Advocate.md + Emerging Leader Advocate.md

## Worker log
| stage | worker | model | tokens (usage) | files written |
|---|---|---|---|---|
| 2 | extract Emerging Leader (02) | sonnet (profile-extractor) | 36,309 | 4 cards |
| 2 | extract Frontline (01) | sonnet (profile-extractor) | 37,470 | 4 cards |
| 0 | frames (all six, one agent) | fable | 151,260 shared | 00-frame.md, 00-tests.md |
| 5 | baselines T1-T3 | sonnet (profile-runner) | 13,995 | tests/T*-base.md |
| 3 | drafter | opus | 93,648 | agent.md 11,137 B; reference 5.5 KB; provenance 8.5 KB (50 sourced old, 1 inferred, 9 project) |
