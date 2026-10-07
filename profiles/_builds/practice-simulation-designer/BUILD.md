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
| 5 | baseline T1 | sonnet | 53,032 | tests/T1-base.md 2.6 KB |
| 5 | baseline T2 | sonnet | 53,595 | tests/T2-base.md |
| 5 | baseline T3 | sonnet | 52,889 | tests/T3-base.md 2.5 KB |
| 5 | baseline T4 | sonnet | 52,784 | tests/T4-base.md 2.5 KB |
| 5 | baseline T5 | sonnet | 52,817 | tests/T5-base.md 2.4 KB |
## Builder findings (for the approval read-out)
- F1. The 3 KB card cap is too tight for an old-profile section: card 02 dropped 4 rules (one on the practice-vs-gate line), card 03 merged seams. Re-briefed 02 to write 02b. Proposed fix: old-profile section cards 5 KB cap.
- F2. Frame ran 6.8 KB against a 6 KB cap after the orchestrator added the Sŏn rules the seat carries (from the plumbing check). Proposed fix: 8 KB cap for rebuild frames, or carry seat rules in a separate short section counted outside the cap.
- F3. Six of nine cards landed 0 to 280 B over the 3,072 B card cap. Not re-briefed (cost over benefit). Proposed fix: card cap 3.5 KB for external sources, 5 KB for old-profile sections (F1).
- F4. measure.py held the examples card to the 3 KB cap; fixed in session to use the 8 KB examples cap and exclude it from the cards total.
- F5. Publisher paywalls (SAGE 403, Wiley 403) limit re-verification to abstracts or secondary full text. Extractors recorded this honestly in `read:`; the critics' grounding lens should treat abstract-level rows as partly verified.
| 3 | drafter | opus | 90,421 | agent.md 11,152 B; reference/examples.md 3,457 B; reference/models.md 2,538 B; provenance.md 8,615 B (59 rows: 28 sourced, 19 sourced old, 2 inferred, 10 project) |
- F6. Two test catches (T4, T5) predated frame updates (page 08 reference only; seams). Orchestrator aligned them before any run. Proposed fix: stage 0 writes tests after the frame's last edit, or stage 3 step 2 re-checks tests against the final frame.
- F7. Every subagent costs about 50k tokens of fixed overhead (system prompt, CLAUDE.md, tool definitions): baseline runners used ~53k each to write 2.5 KB. Worker cost scales with agent count, not content. Proposed fix: batch small jobs (one runner for 2 to 3 tests, one critic for two light lenses, one extractor for an old profile's sections), keep separate agents only where blindness or parallel speed earns it.
