# State (in flight)

Rewrite freely. One line per item: what | owner | next step.

## Rebuild (started 2026-10-07)
- P1 Scaffold: pushed to github.com/brandonjacuna/son on 2026-10-07 | Claude | done
  - Imported with history: learning-studio (from unmerged cloud branch claude/blissful-einstein, not stale main), operations (son-operational-buildout main), nerve (from unmerged PR #1 branch claude/bold-goldberg; main only had BRIEF.md), design-system (Mac), local profile builds (Mac, in `imports/profile-builds-local/`)
  - Imported without history (no git): clickup-system, science/espresso-chiller
  - After push: archive the four old repos on GitHub (son-learning-studio, son-operational-buildout, son-nerve, agenticproject) once Brandon confirms
- P2 Construction handoff imported on branch `import/build-out` (PR open, not merged) | Brandon | review and merge; then run `company/workstreams/build-out/KICKOFF.md` in a new session
- Live automation outside the repo: ClickUp Meetings Agent v3 (Super Agent) runs roll-forward Mondays 7 AM, day-before reminders, close-out; checkpoints Oct 8 standup, Oct 12 roll-forward, Oct 13 meeting (see `company/workstreams/clickup-system/STATE.md`)
- P3 Cleanup: Jun, Josephine, Pullman-derived content, experiential, Airtable, stale paths across Box, ClickUp, profiles | Claude (agents) | every deletion shown to Brandon first
- P3 Account memory cleanup | Brandon | done 2026-10-07
- P3 Project instructions replaced | Brandon | done 2026-10-07
- P4 Profile system redesign (efficacy review, lean agents, token-lean build pipeline) | Claude on Fable | after P1 and P2
- P5 Operating skills: red-team, thread-log, session-close, task-tree, kb-refresh | Claude | after P1
- P6 ClickUp layer: verify what the GitHub integration exposes to Brain; Super Agent design within 10k credits | Claude | research first

## Open questions for Brandon
- Build-out migration (from build-out HANDOFF section 7; build-out's own open items are in `company/workstreams/build-out/decisions/open.md`):
  - M1 ClickUp ask rule: the guard asks before every non-capture ClickUp write repo-wide, including review drafts sent to ClickUp. Keep repo-wide, or limit to build-out work (delete/merge stay blocked everywhere)?
  - M2 Shared ClickUp tooling: keep `cu.py` and the ClickUp knowledge base inside build-out, or merge with `clickup-system` at repo level?
  - M3 Profile creation: `profile-forge` vs the P4 profile pipeline (handoff suggests P4 is master and profile-forge feeds it)
  - M4 Settings protection: the guard blocks edits to `.claude/settings.json` repo-wide without an unlock phrase. Keep, or scope to the hooks block?
  - M5 Command and skill names: `/deep`, `/gate`, `/capture`, `/sandbox`, `/promote`, `/lease-signed` vs P5 skills (no collisions today; revisit when P5 is built)
  - M6 Build-out kb location: keep at `company/workstreams/build-out/kb/` (current skill paths work) or move under `kb/`
- Where the line falls between Korean cultural tie-ins (remove) and the design deck (keep): godwit, water deer letterform, Mandarin duck palette, persimmon-sumac-elderberry. Show the extraction first.
- Monday Industry Digest has no scheduled task yet: create one?
