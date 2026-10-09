# Profile build measurements

One row per build. Bytes are measured by `.claude/skills/profile-build/scripts/measure.py`; tokens are bytes / 4 unless marked "usage" (summed from worker usage lines in the build's `BUILD.md`). The per-call load is what a seat costs every time it is used: the agent core, plus the skill if it is a mode.

## Baseline (old seven-stage builder, measured 2026-10-07)
| Seat | Stage files written | Full profile rewrites | Per-call load | Inline tags in load | Plumbing in load | Orchestrator context | Worker tokens | Validation |
|---|---|---|---|---|---|---|---|---|
| Hospitality Craft Educator | 445 KB | 3 (draft 81, tagged 95, revised 95 KB) | 95.0 KB (~23,750 tok) | 16.0 KB (17%) | 6.4 KB (7%) | maxed out (Brandon) | not recorded | stage 6 skipped; stage 7 on the build model |
| Practice and Simulation Designer | 199 KB | 3 (draft 40, tagged 53, revised 53 KB) | 53.0 KB (~13,260 tok) | 9.7 KB (18%) | 5.1 KB (10%) | maxed out (Brandon) | not recorded | stages 6 and 7 skipped |

Measured facts behind the redesign: the tagged and revised files kept 99% of the draft's lines (tagging only appended tags and a tag audit; revision changed about 1% of lines), so two of the three full writes carried no new judgment. In the finished PSD profile, the every-call judgment (role, scope, cues, rules, anti-patterns, outputs) is 23.6 KB with tags, about 19 KB without.

## Caps of the new builder (`.claude/skills/profile-build/`)
Build folder about 75 KB or less (frame 6, sources 6, cards 40, flags 4, tests and BUILD.md about 20). Per-call load 12 KB cap (about 3,000 tokens), 10 KB target. Reference 30 KB, loaded on demand. Orchestrator under 60k tokens for the whole build. These are caps, not results: session B measures the first real build against them.

## Builds
| Date | Seat | Build folder | Cards | Per-call load | Reference | Worker tokens (usage) | Orchestrator context | Tests |
|---|---|---|---|---|---|---|---|---|
| 2026-10-07 | practice-simulation-designer (rebuild, test build) | 93.8 KB (56 KB of it test outputs) | 22.2 KB (+4.7 KB examples) | 11.7 KB (~3,000 tok) | 5.8 KB | 2.21M across 36 workers (frame 157k, extract 520k, draft 90k, red team 545k, test 894k) | not measured; never opened a source or card; session also carried session A | 5/5 on Sonnet (one after a fix); Haiku failed T3 |

## Result of the test build (Practice and Simulation Designer, 2026-10-07)
| Measure | Old builder | New builder | Change |
|---|---|---|---|
| Per-call load (every use of the seat) | 53.0 KB, ~13,260 tok | 11.7 KB, ~3,000 tok | -78% |
| Stage files written | 199 KB, profile written 3 times | 94 KB, profile drafted once (38 KB without test outputs) | -53% |
| Orchestrator context | maxed out | sources and cards never opened; reads were frame, source list, core, flags, verdict tables | the stated pain point removed |
| Worker tokens | not recorded (one context) | 2.21M across 36 subagents | new cost, now visible |
| Validation | stages 6 and 7 skipped | 5 blind critics, Fable judge (15 flags accepted, incl. 3 critical on employee records and consent), 5 tests vs baseline | lever restored |
| Grounding re-checked | none | 4 sources re-read; 2 old citations corrected; 2 overclaims cut | |

Worker cost driver: each subagent carries about 50k tokens of fixed overhead (system prompt, CLAUDE.md, tools), so 36 agents is most of the 2.21M. Batching small jobs (finding F7 in the build's BUILD.md) should cut it by roughly a third without losing blindness where it matters.

Smoke test, same day: the shipped agent, called by its slug, ran T1 for 16,063 tokens against 53k to 62k for general-purpose runners. The fixed overhead is mostly the general-purpose agent type; custom worker agents with minimal tools are the larger saving (finding F9).

## F9 measured (custom worker agents, 2026-10-07)
| Worker | General-purpose agent reading a worker file | Custom agent (`.claude/agents/`, minimal tools) | Change |
|---|---|---|---|
| Runner, T1 baseline | 53,032 tok | 11,513 tok | -78% |
| Grader | 60,297 to 66,117 tok (3 to 5 rows) | 12,110 tok (1 row) | about -80% |

Projection for the next build of PSD's size: about 20 workers after batching (F7), most of them custom, at roughly 12k to 25k each plus the Opus drafter and two Fable calls: about 0.5M to 0.7M worker tokens, against 2.21M in the test build. A projection, not a measurement; the next real build checks it.
| 2026-10-09 | hospitality-operations-realist | 63.4 KB | 13.3 KB | 10.7 KB (~2735 tok) | 5.4 KB | | | |
| 2026-10-09 | frontline-advocate | 81.0 KB | 23.8 KB | 11.5 KB (~2933 tok) | 5.6 KB | | | |
| 2026-10-09 | culture-implementer | 64.6 KB | 12.4 KB | 11.1 KB (~2853 tok) | 4.6 KB | | | |
| 2026-10-09 | hr-implementer | 89.1 KB | 17.7 KB | 10.7 KB (~2728 tok) | 4.3 KB | | | |
| 2026-10-09 | hr-systems-designer | 78.6 KB | 14.0 KB | 10.6 KB (~2722 tok) | 5.0 KB | | | |
| 2026-10-09 | performance-feedback-designer | 82.2 KB | 11.7 KB | 11.1 KB (~2845 tok) | 4.6 KB | | | |

## Batch 1 (operations and core panel), 2026-10-09
Six seats: hospitality-operations-realist (revise), frontline-advocate (merge with Emerging Leader Advocate), culture-implementer, hr-implementer, hr-systems-designer, performance-feedback-designer (revise; the three HR-facing seats at harsh intensity).
| Measure | Result |
|---|---|
| Per-call load | 10.6 to 11.5 KB each (about 2,700 to 2,950 tokens); old profiles 26 to 56 KB |
| Worker tokens | about 3.2M for the batch, about 540k per seat (first test build: 2.21M for one seat). Includes the harsh double red team (40 critics), statutory verification, and the white-paper check |
| Savings that worked | custom worker agents (11k to 25k per runner or critic vs 53k to 66k); one Fable agent framing six seats; one Fable judge for six seats; one runner per seat for all tests |
| Tests | 18 of 18 pass on Sonnet; no test the baseline also passes; culture-implementer T3 a partial catch |
| Red team | 96 merged flags; 94 accepted whole or part, 1 rejected, 1 to Brandon (recusal) |
| Grounding found | the old HR Implementer had 5 of 19 statutory items wrong or outdated (kb/domains/texas-employment.md) |
| Limits hit | the 20-agent concurrency cap and one session usage limit (five workers lost and rerun or recovered) |
| 2026-10-09 | assessment-competency-designer | 89.3 KB | 14.7 KB | 12.0 KB (~3068 tok) | 8.6 KB | | | |
| 2026-10-09 | curriculum-program-architect | 54.2 KB | 10.9 KB | 10.8 KB (~2767 tok) | 4.8 KB | | | |
| 2026-10-09 | materials-author-editor | 59.4 KB | 14.8 KB | 15.7 KB (~4024 tok) | 4.1 KB | | | |
| 2026-10-09 | instructional-designer | 80.6 KB | 31.6 KB | 11.9 KB (~3050 tok) | 8.1 KB | | | |
| 2026-10-09 | learner-advocate | 54.3 KB | 12.6 KB | 9.6 KB (~2458 tok) | 2.6 KB | | | |
| 2026-10-09 | tbri | 64.6 KB | 12.2 KB | 11.5 KB (~2950 tok) | 5.2 KB | | | |

## Batch 2 (learning-studio module seats), 2026-10-09
Six seats: assessment-competency-designer (revise, harsh), curriculum-program-architect, materials-author-editor (skill + agent), instructional-designer (merge with HighScope), learner-advocate, tbri (+ employee-harm lens).
| Measure | Result |
|---|---|
| Per-call load | 9.6 to 12.0 KB per agent (about 2,450 to 3,070 tokens). Materials: skill 5.6 KB in the session, agent 10.1 KB called separately (the 15.7 KB row adds both; they never load together) |
| Worker tokens | about 2.42M for the batch, about 400k per seat (batch 1: about 540k). By stage: frame 146k, extract 230k, draft 482k, red team and edits 1.20M, tests 356k |
| Savings that worked | one sonnet runner for five seats' baselines (23k); critics paired two seats per agent for standard lenses (20 critics instead of 26); one merger and one Fable judge for six seats; three Sonnet agents applied the judge's edits instead of the orchestrator |
| Tests | 18 of 18 pass; no test the baseline also passes; three thin margins noted in tests.md |
| Model line | instructional-designer moves to haiku (both hardest tests hold); learner-advocate holds on haiku; curriculum, materials, and tbri stay sonnet (haiku missed a recent-hire read, the pay sentence, and a disclosure-record protection); assessment stays sonnet by stakes (haiku passed but hedged on record wording) |
| Red team | 59 merged flags (3 critical) plus 18 cross-seat seams; 57 accepted whole or part, 2 rejected (runtime model), 1 to Brandon (retry cap: none, escalate by count) |
| Neighbor edits | five shipped seats edited to close seams: performance-feedback-designer, practice-simulation-designer, hospitality-operations-realist, hr-systems-designer, hr-implementer |
| 2026-10-09 | hospitality-craft-educator | 87.3 KB | 26.4 KB | 18.3 KB (~4683 tok) | 7.5 KB | | | |
| 2026-10-09 | values-belonging-designer | 86.4 KB | 21.5 KB | 11.9 KB (~3034 tok) | 6.7 KB | | | |
| 2026-10-09 | organizational-systems-architect | 67.1 KB | 12.8 KB | 11.9 KB (~3034 tok) | 5.5 KB | | | |
| 2026-10-09 | people-systems-designer | 70.1 KB | 12.4 KB | 12.0 KB (~3059 tok) | 6.5 KB | | | |
| 2026-10-09 | bar-designer | 70.0 KB | 17.5 KB | 11.8 KB (~3031 tok) | 5.4 KB | | | |
| 2026-10-09 | environmental-signage-specialist | 59.8 KB | 13.7 KB | 9.4 KB (~2416 tok) | 5.0 KB | | | |

## Batch 3 (structure and craft), 2026-10-09
Six seats: hospitality-craft-educator (rebuild; skill + agent), values-belonging-designer (merge with Culture Signal; harsh), organizational-systems-architect (revise; harsh), people-systems-designer (revise; harsh), bar-designer (new; build-out), environmental-signage-specialist (revise; moved to build-out).
| Measure | Result |
|---|---|
| Per-call load | 9.4 to 12.0 KB per agent; craft educator skill 6.4 KB loads only in the session that runs elicitation |
| Worker tokens | about 2.95M for the batch, about 490k per seat (batch 2: about 400k; batch 1: about 540k). By stage: frame 223k, scouts 160k, extract 477k, draft 518k, red team and edits 1.12M, tests 456k. Rebuild and new seats (research) ran 560k to 650k; revise seats 350k to 460k |
| Savings that worked | harsh critics covered three seats per agent (8 agents instead of 24); one merger and one Fable judge for six seats; scouts covered all of a seat's targets in one agent |
| Cost of mistakes | a container restart killed the first Fable judge (rerun, about 157k); runner briefs that pointed at tests files let runners see the expected catches, so five seats' with-runs were rerun blind (about 57k discarded); fixed in stage 5 |
| Tests | 18 of 18 pass after three row fixes (values T3, people systems T2, T3) and one replaced test (bar T2: the baseline also passed the mirror test) |
| Model line | craft educator moves opus to sonnet (both hardest tests hold); bar designer stays sonnet (haiku missed the health-code call and the station method); signage held on haiku but stays sonnet by stakes (it reads TAS and the sign code); the three harsh people seats stay sonnet |
| Red team | 82 merged flags (4 critical) plus 15 seams; 81 accepted, 1 rejected, 1 ask to Brandon (stay-interview runner) left open |
| Book ingest | Ellis chapters ingested during the batch (How Many Stations?, Identical Cockpits, The Pickup and The Well, Bar Geometry, Floor Sinks, A.D.A. Bar Counters); the bar seat's station-count block lifted |

## Next-session check, batches 1 to 3 (2026-10-09, after approval)
Six real agents called by slug with their T1 task (hr-implementer, culture-implementer, instructional-designer, learner-advocate, bar-designer, values-belonging-designer; two per batch, covering haiku and the build-out cluster). All six loaded and applied CLAUDE.md standing rules unprompted ("customer," no em dashes, Brandon decides personnel, counsel first where named). 13k to 52k tokens each. Outputs were tests only; nothing was written to any workstream.
