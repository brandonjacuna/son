# Phase 2: Session basics

## Goal
Every session keeps memory clean without relying on anyone remembering to.

## Work
1. **`session-close` skill.** Lands the session's branch on `main` per the CLAUDE.md rule (merge routine work; pull request for system changes and sandboxes). Rewrites `memory/state.md` (in flight, owner, next step); appends to `memory/decisions.md` only what Brandon agreed to, read back to him for confirmation; parks open threads in `memory/threads.md`; lists anything worth promoting from a workstream's notes into root memory; commits and pushes. Asks before committing to `main` if the session worked on a sandbox branch.
2. **`thread` skill.** When Brandon branches into a tangent: log it in `memory/threads.md` immediately (date, thread, where it came from), say how it connects to the core work, then offer as a pop-up: follow it now, or park it and return. Never kills the tangent; never lets it silently replace the core work.
3. **`chat-handoff` intake.** Sorts a package dropped in `imports/` into the right workstream, records what came in, scrubs out-of-scope terms, and flags facts for `memory/context.md` or `founders/context.md`.
4. **Sandbox convention.** Document in CLAUDE.md: experiments and changes to the system itself go on `sandbox/<name>` branches; merge only on Brandon's word; `session-close` reports open sandboxes.
5. **Optional hook.** A Stop or SessionEnd reminder if `memory/state.md` was not touched in a session that changed files.

## Done when
The three skills exist in `.claude/skills/`, each tested in one real session, and CLAUDE.md points to them.

## Red team
Light.
