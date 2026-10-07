# Stage 2: Extract (Sonnet extractors, parallel)

1. One extractor per source row in `01-sources.md`. Batch two or three short sources into one extractor only if each is under 10 pages. A long old profile (over 40 KB) gets two extractors split by section.
2. Brief: "Read `.claude/skills/profile-build/workers/extractor.md` and follow it. Build: <folder>. Source: <row>. Targets: <ids from the frame>. Card: `extract/NN-<name>.md`." Use `model: sonnet`. Send them all in one message.
3. Each returns a path, a row count, and a line. Do not open the cards. Run `python3 .claude/skills/profile-build/scripts/measure.py <build>` to check the 3 KB and 40 KB caps; re-brief any extractor whose card is over cap ("cut to the 15 rows that most change a decision").
4. Log tokens in `BUILD.md`.
