# Stage 2: Extract (Sonnet extractors, parallel)

1. One extractor per source row in `01-sources.md`. Batch two or three short sources into one extractor only if each is under 10 pages. An old profile gets one extractor per section group (cues; decision rules and diagnostics; anti-patterns, uncertainty, and seams), each under the 3 KB card cap, plus one `NN-examples.md` card holding its worked examples verbatim (8 KB cap, outside the 40 KB total). The drafter writes `reference/examples.md` only from verbatim example cards or source cases, never from two-sentence summaries.
2. Brief: "Read `.claude/skills/profile-build/workers/extractor.md` and follow it. Build: <folder>. Source: <row>. Targets: <ids from the frame>. Card: `extract/NN-<name>.md`." Use `model: sonnet`. Send them all in one message.
3. Each returns a path, a row count, and a line. Do not open the cards. Run `python3 .claude/skills/profile-build/scripts/measure.py <build>` to check the 3 KB and 40 KB caps; re-brief any extractor whose card is over cap ("cut to the 15 rows that most change a decision").
4. Log tokens in `BUILD.md`.
