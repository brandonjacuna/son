# Build: bar-designer
mode: new | started: 2026-10-09 | orchestrator: Opus 5.5 (batch 3)
cluster: build-out | old: none (Tobin Ellis kb in company/workstreams/build-out/kb/bar/tobin-ellis/)

## Worker log
| stage | worker | model | tokens (usage) | files written |
|---|---|---|---|---|
| 0 | frame + tests, all 6 seats (one agent) | fable | 222,842 shared (~37k per seat) | 00-frame.md, 00-tests.md |
| 2 | extract Tobin Ellis kb (01-03) | sonnet (profile-extractor) | 29,151 | 3 cards, 8.7 KB (book dimensions blank in kb; checklist all derived) |
| 5 | baselines T1-T3, 5 seats in one runner | sonnet (profile-runner) | 25,379 shared (~5k per seat) | tests/T*-base.md |
| 1 | scout, targets 1-5 in one agent | sonnet (general-purpose) | 81,854 | 01-sources.md |
