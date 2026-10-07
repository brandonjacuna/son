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
| 2 | extract 02b (resumed 02) | sonnet | 820 (increment; 02 total 60,917) | extract/02b-old-rules.md, 4 rows |
| 2 | extract 05 Norman | sonnet | 61,433 | extract/05-norman.md ~3.08 KB, 8 rows; abstract only (publisher 403) |
| 2 | extract 07 Moore | sonnet | 66,905 | extract/07-moore.md ~3.3 KB, 12 rows; blog verified, book not read |
| 2 | extract 08 AI models | sonnet | 71,125 | extract/08-ai-models.md ~3.1 KB, 10 rows; arXiv full text, two abstracts; corrected two old citations |
| 2 | extract 06 Blume | sonnet | 77,300 | extract/06-blume.md ~3.1 KB, 9 rows; Grossman and Salas full text, Blume secondhand |

| 4 | critic rules | sonnet | 65,287 | 04-critic-rules.md: 1 minor |
| 4 | critic specificity | sonnet | 64,773 | 04-critic-specificity.md: 2 major, 6 minor |
| 4 | critic grounding | sonnet | 77,946 | 04-critic-grounding.md: 2 major, 6 minor; all sourced (old) rows match their cards |
| 4 | critic employee-harm | sonnet | 66,559 | 04-critic-employee-harm.md: 2 critical, 6 major, 1 minor |
| 4 | critic seams | sonnet | 84,289 | 04-critic-seams.md: 1 critical, 7 major, 2 minor |
| 4 | merger | sonnet | 59,333 | 04-flags.md 4,096 B: 2 critical, 12 major, 4 minor; 3 for other seats |
| 4 | judge | fable | 68,130 | decisions: 15 accepted (whole or part), 3 rejected, 0 to Brandon; orchestrator applied core edits (11,924 B) |
| 4 | provenance and reference edits | sonnet | 58,309 | provenance.md 10,722 B; models.md 2,498 B |
| 5 | baseline T1 | sonnet | 53,032 | tests/T1-base.md 2.6 KB |
| 5 | baseline T2 | sonnet | 53,595 | tests/T2-base.md |
| 5 | baseline T3 | sonnet | 52,889 | tests/T3-base.md 2.5 KB |
| 5 | baseline T4 | sonnet | 52,784 | tests/T4-base.md 2.5 KB |
| 5 | baseline T5 | sonnet | 52,817 | tests/T5-base.md 2.4 KB |
| 5 | with T2 | sonnet | 57,943 | tests/T2-with.md |
| 5 | with T3 | sonnet | 57,582 | tests/T3-with.md 2.9 KB |
| 5 | with T4 | sonnet | 57,581 | tests/T4-with.md 2.9 KB |
| 5 | with T1 | sonnet | 62,093 | tests/T1-with.md 2,982 B |
| 5 | with T5 | sonnet | 61,445 | tests/T5-with.md 2,978 B |
| 5 | grader | sonnet | 66,117 | verdicts: 5/5 pass by grader; T4 with-run partial (no prebrief check), so orchestrator edited R12 and reruns T4 |
| 5 | with T4 rerun | sonnet | 57,572 | tests/T4-with.md 2.7 KB (run 1 kept as T4-with-run1.md) |
| 5 | haiku T3 (model line) | haiku | 67,260 | tests/T3-with-haiku.md 2,952 B; runner glimpsed 5 lines of T1-base while listing (not used) |
| 5 | haiku T1 (model line) | haiku | 80,546 | tests/T1-with-haiku.md 2,964 B; found and reviewed the example module EX-001 |
| 5 | grader (T4 rerun, haiku) | sonnet | 60,297 | T4 pass; T1-haiku pass; T3-haiku fail (drill named, not built) |
## Builder findings (for the approval read-out)
- F1. The 3 KB card cap is too tight for an old-profile section: card 02 dropped 4 rules (one on the practice-vs-gate line), card 03 merged seams. Re-briefed 02 to write 02b. Proposed fix: old-profile section cards 5 KB cap.
- F2. Frame ran 6.8 KB against a 6 KB cap after the orchestrator added the Sŏn rules the seat carries (from the plumbing check). Proposed fix: 8 KB cap for rebuild frames, or carry seat rules in a separate short section counted outside the cap.
- F3. Six of nine cards landed 0 to 280 B over the 3,072 B card cap. Not re-briefed (cost over benefit). Proposed fix: card cap 3.5 KB for external sources, 5 KB for old-profile sections (F1).
- F4. measure.py held the examples card to the 3 KB cap; fixed in session to use the 8 KB examples cap and exclude it from the cards total.
- F5. Publisher paywalls (SAGE 403, Wiley 403) limit re-verification to abstracts or secondary full text. Extractors recorded this honestly in `read:`; the critics' grounding lens should treat abstract-level rows as partly verified.
| 3 | drafter | opus | 90,421 | agent.md 11,152 B; reference/examples.md 3,457 B; reference/models.md 2,538 B; provenance.md 8,615 B (59 rows: 28 sourced, 19 sourced old, 2 inferred, 10 project) |
- F6. Two test catches (T4, T5) predated frame updates (page 08 reference only; seams). Orchestrator aligned them before any run. Proposed fix: stage 0 writes tests after the frame's last edit, or stage 3 step 2 re-checks tests against the final frame.
- F7. Every subagent costs about 50k tokens of fixed overhead (system prompt, CLAUDE.md, tool definitions): baseline runners used ~53k each to write 2.5 KB. Worker cost scales with agent count, not content. Proposed fix: batch small jobs (one runner for 2 to 3 tests, one critic for two light lenses, one extractor for an old profile's sections), keep separate agents only where blindness or parallel speed earns it.
- F8. profile_lint.py accepted only lowercase letters, spaces, and parentheses in a provenance tag cell, so mixed tags ("sourced, inferred") failed. Fixed in session to allow , ; + /.

## Closing
- Mode rebuild; container agent; model sonnet (Haiku failed T3: named the classification drill but built a role-play). Models: frame and judge Fable; drafter Opus; extractors, critics, merger, runners, grader Sonnet; orchestrator Opus.
- Red team: 2 critical, 12 major, 4 minor merged; judge accepted 15 (whole or part), rejected 3, none to Brandon. Criticals fixed: no per-person practice records or use in review or sign-off; camera consent refusal costs nothing and practice is not recorded by default; practice observations walled off from sign-off.
- Tests: 5/5 pass on Sonnet; T4 passed after an R12 edit (prebrief check). Baselines missed or partly caught every test.
- For other seats (from 04-flags.md): owners for facilitator training, gate scenario authoring, and the definition of "trained" sit with instructional-designer, assessment-competency-designer, and operations seats.
- Open: next-session smoke test (stage 6 step 7) through the real agent; Brandon's approval of the seat and of the builder; findings F1 to F8 to fold into the builder.

## Smoke test (stage 6 step 7), 2026-10-07
- Ran T1 through the real agent (`subagent_type: practice-simulation-designer`) in the same session, which picked up the new agent without a restart. Pass: felt-risk barrier, decision scene over quiz, recovery path, `tool.*` and chef-gated bindings, gate kept separate. Standing rules applied in output ("customer", no em dashes); CLAUDE.md inheritance is consistent with this but not proven (the core also says "customer"). It did not find the example module EX-001 (searched "allergen"; the folder says "allergy").
- Cost: 16,063 tokens, against 53k to 62k for general-purpose runners on the same task.
- F9. Most of the per-agent overhead (F7) belongs to the general-purpose agent type (full tool set and its system prompt), not to subagents as such. A custom agent with a short definition and 4 tools cost about a quarter. Proposed fix: define the builder's workers (extractor, critic, runner, grader) as custom agents in `.claude/agents/` with minimal tools and fixed models, instead of general-purpose agents told to read a worker file. Expected effect: worker tokens down by well over half. Needs Brandon's approval (it adds agent files to `.claude/agents/`).
