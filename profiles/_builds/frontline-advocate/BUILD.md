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
| 4 | critic grounding | sonnet (profile-critic) | 36,154 | 5 minor |
| 4 | critics: spec+rules 28,435; harm 21,975; seams 54,977 | sonnet (profile-critic) | 105,387 | spec 8 minor; rules 3 minor; harm 4 major 1 minor; seams 3 major 5 minor |
| 4 | merger | sonnet | 58,873 | 04-flags.md: 0 critical, 7 major, 8 minor |
| 4 | judge (all six, one agent) | fable | 144,337 shared | 04-judgment.md |
| 4 | apply judged edits (3 seats, one agent) | sonnet | 91,793 shared | edits applied |
| 5 | with-runs T1-T3 | sonnet (profile-runner) | 20,208 | tests/T*-with.md |

## Closing
- Shipped to .claude/agents/frontline-advocate.md on 2026-10-09; 3/3 tests pass on Sonnet; red team and Fable judgment applied; shared files: counsel-gate, people-practices, records-and-routes. Batch totals in profiles/_builds/MEASUREMENTS.md.
