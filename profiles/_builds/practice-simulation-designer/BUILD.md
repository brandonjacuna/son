# Build: practice-simulation-designer
mode: rebuild | started: 2026-10-07T19:43Z | orchestrator: Opus 5.5 (session also carried phase 3 session A, so orchestrator context is inflated)
cluster: learning-and-development | old profile: profiles/_source/learning-and-development/Practice and Simulation Designer.md (53,045 B)

## Worker log
| stage | worker | model | tokens (usage) | files written |
|---|---|---|---|---|
| 0 | plumbing gap check | sonnet | 71,223 | none (12 gaps returned; memory/pending/2026-10-07-ld-plumbing-gaps.md) |
| 0 | frame | fable | 86,034 | 00-frame.md 6,078 B; 00-tests.md 3,033 B |
| 2 | extract 04 examples | sonnet | 55,493 | extract/04-examples.md 4.7 KB |
| 2 | extract 01 old cues | sonnet | 61,909 | extract/01-old-cues.md 2.98 KB, 19 rows |
| 2 | extract 03 old scope/seams | sonnet | 64,672 | extract/03-old-scope.md ~3.1 KB, 16 rows (over cap by ~0.1 KB) |
| 2 | extract 02 old rules | sonnet | 60,097 | extract/02-old-rules.md 3.07 KB, 14 rows; dropped 4 rules to fit cap |
| 2 | extract 05 Norman | sonnet | 61,433 | extract/05-norman.md ~3.08 KB, 8 rows; abstract only (publisher 403) |

## Builder findings (for the approval read-out)
- F1. The 3 KB card cap is too tight for an old-profile section: card 02 dropped 4 rules (one on the practice-vs-gate line), card 03 merged seams. Re-briefed 02 to write 02b. Proposed fix: old-profile section cards 5 KB cap.
- F2. Frame ran 6.8 KB against a 6 KB cap after the orchestrator added the Sŏn rules the seat carries (from the plumbing check). Proposed fix: 8 KB cap for rebuild frames, or carry seat rules in a separate short section counted outside the cap.
