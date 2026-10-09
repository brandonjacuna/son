# Build: hospitality-craft-educator
mode: rebuild | started: 2026-10-09 | orchestrator: Opus 5.5 (batch 3)
cluster: learning-and-development | old: Hospitality Craft Educator.md

## Worker log
| stage | worker | model | tokens (usage) | files written |
|---|---|---|---|---|
| 0 | frame + tests, all 6 seats (one agent) | fable | 222,842 shared (~37k per seat) | 00-frame.md, 00-tests.md |
| 2 | extract old profile (01) | sonnet (profile-extractor) | 61,960 | 4 cards, 13.0 KB (page 08 authority dropped; example 5 left out for cap) |
| 1 | scout, targets 1-4 in one agent | sonnet (general-purpose) | 77,730 | 01-sources.md |
| 5 | baselines T1-T3 | opus (profile-runner) | 16,379 | tests/T*-base.md |
| 3 | drafter | opus | 101,943 | agent.md 12,176 B; skill 5,801 B; reference 7.5 KB; provenance 7.4 KB |
