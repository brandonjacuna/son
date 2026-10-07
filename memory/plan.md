# Rebuild plan

Agreed with Brandon 2026-10-07. The repo is the home for all Sŏn work; the claude.ai Sŏn Home Base Project is now only a pointer to it.

## Order and why

| # | Phase | Why here | Model | Brief |
|---|---|---|---|---|
| 1 | Cleanup | Strip out-of-scope material (Jun, Josephine, Pullman-derived, experiential, Airtable) and stale pointers before anything is built on top of it | Opus coordinating, Sonnet agents | `briefs/1-cleanup.md` |
| 2 | Session basics | Every later session needs session-close and the thread log to keep memory clean | Opus | `briefs/2-session-basics.md` |
| 3 | Profiles | Workstreams are built around specialist seats, so the profile system comes first. Starts from what each workstream needs. The red-team skill is designed here, since profile validation is red teaming | Fable designs, Opus and Sonnet execute | `briefs/3-profiles.md` |
| 4 | Operating skills | Task tree, knowledge refresh, walk-mode decisions, scheduled prompt sync | Opus | `briefs/4-operating-skills.md` |
| 5 | Workstream builds | Take every workstream to work-ready (or sandbox-ready) against the finished profile and skill system | Opus, Fable only where a brief says so | `briefs/5-workstreams.md` |
| 6 | ClickUp manager layer | Brain and Super Agents for managers; before the first manager hire | Fable designs, Opus builds | `briefs/6-clickup-layer.md` |

Build-out has its own phases (P0 concept to P4 closeout, in `company/workstreams/build-out/PHASE.yaml`). Those are construction phases, unrelated to this list. This list uses numbers 1 to 6 only.

## Before phase 1 (Brandon)
- Merge pull request #1 (`import/build-out`). Until then the build-out hooks, skills, commands, and workflows are not on `main`.
- Create the Claude Code cloud environment for `son`: paste `scripts/setup_cloud.sh` into the Setup script field; make sure the ClickUp and Box connectors are connected in claude.ai settings.

## Before phase 3 (Brandon)
- In Box, download the folder Sŏn / 10. AI Projects / Profiles as a zip to the Mac Desktop. (Direct Box downloads are blocked from cloud sessions, and copying 64 profiles through the model would cost hundreds of thousands of tokens and risk altering text.)

## Before nerve switches on (phase 5, Brandon)
- Register free API keys: FRED, BLS, Socrata, Census, EIA.

## How every session runs
1. Open a fresh Claude Code session on `son`. Keep one phase (or one part of a phase) per session.
2. Opening prompt: `Read CLAUDE.md, memory/state.md, memory/plan.md. Tell me in five lines where we are. Then start the next step of phase N from memory/briefs/.`
3. Subagents do reading and extraction; the session model coordinates; Fable only where the brief says.
4. Decisions go to Brandon as pop-ups with full context.
5. End with session-close (until phase 2 builds the skill: update `memory/state.md`, append agreed decisions to `memory/decisions.md`, park threads in `memory/threads.md`, commit, push).
6. Experiments and changes to the system itself happen on a `sandbox/<name>` branch and merge only when Brandon says so.

## Reviving an old chat
Use `prompts/chat-handoff.md` in the old chat. Put the package in `imports/`. A session sorts it into the right workstream.
