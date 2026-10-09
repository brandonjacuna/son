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
| 2 | extract saturation (03) | see worker | 22,457 | |
| 2 | extract table cues + tasting (05, 06) | see worker | 30,450 | |
| 2 | extract transmission (04) | see worker | 74,785 | |
| 4 | critic grounding | see worker | 30,893 | |
| 4 | critic spec+rules+seams | see worker | 56,013 | |
| 4 | merger, 6 seats | see worker | 71,092 shared | |
| 4 | Fable judge, 6 seats + seams (rerun after restart) | see worker | 157,169 shared | |
| 4 | apply judgment edits (3 seats) | see worker | 111,042 shared | |
| 5 | with-runs T1-T3 (opus) | see worker | 20,854 | |
| 5 | grader | see worker | 58,864 shared | |
| 5 | sonnet tier check T1, T3 | see worker | 21,336 | |
| 5 | grader, tier checks | see worker | 30,291 shared | |

## Closing (2026-10-09)
- Mode: rebuild; container both (skill elicits by pop-up, agent turns transcripts into craft). Models: frame and judge fable; scouts, extract, critics, merger, runners, grader sonnet; drafter opus; edits applied by sonnet.
- Flags: 14 accepted, 1 rejected. Cross-seat seams: profiles/_builds/batch3-seams-judgment.md.
- Tests: T1-T3 pass (see tests.md).
- Model line: sonnet: T1 and T3 hold on sonnet (opus guess dropped).
- Open: Transcript folder company/workstreams/learning-studio/research/elicitation/ is the drafter's choice; crew elicitation rounds deferred until Brandon names who runs them; REGISTRY row added. Approval by Brandon pending; next-session check (stage 6 step 7) pending.
