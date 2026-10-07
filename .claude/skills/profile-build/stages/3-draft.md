# Stage 3: Draft (Opus drafter, one pass)

1. Spawn one drafter, `model: opus`. Brief: "Read `.claude/skills/profile-build/workers/drafter.md` and follow it. Build: <folder>. Master: `profiles/<cluster>/<slug>/`. Container: <agent|skill|both>."
2. On return, run `python3 .claude/skills/profile-build/scripts/profile_lint.py profiles/<cluster>/<slug>`. Fix lint errors yourself with targeted Edits (they are mechanical). If the core is over cap, send the drafter back once with: "Move <sections> to reference; the core is <n> KB."
3. Read `agent.md` (and `skill/SKILL.md`) yourself now. These are the only master files the orchestrator reads, and they are small by design.
4. Log tokens and bytes in `BUILD.md`.
