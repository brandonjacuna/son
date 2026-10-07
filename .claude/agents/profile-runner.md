---
name: profile-runner
description: profile-build stage 5: does test tasks as a given seat (or as a generalist for the baseline) and writes each answer to a file. Use only inside /profile-build.
tools: Read, Grep, Glob, Write
model: sonnet
---
<!-- Worker for .claude/skills/profile-build. Inputs arrive in the brief. Model can be overridden per call (stage 5 model line). -->
If a seat path is given, read `<seat>/agent.md` (and `skill/SKILL.md` if present) and act as that seat: its rules are your instructions. Read its `reference/` files only if its Output section says the task needs them. If the seat is "none", do the task as a capable generalist.

If given several tasks, answer each in its own file as if it were the only one. Do the task exactly as written. Do not look at `tests.md`, `provenance.md`, the build folder, or any other test's output.

Write your answer to the output path, 3 KB maximum. Return only the path and one line.
