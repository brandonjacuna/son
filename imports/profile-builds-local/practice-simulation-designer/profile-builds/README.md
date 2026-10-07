# Profile builds

Workspace for building new specialist profiles before they go to Box. Each build runs the seven-stage synthesis procedure (ClickUp `2ky45bmy-16853`, page `2ky45bmy-27213`): `/build-profile <slug>` for stages 0 to 5, then `/validate-profile <slug>` in a fresh session for stages 6 and 7.

A finished profile leaves this folder for Box through the Profile Update Protocol. Nothing here is canonical. Delete a build folder's working files once the profile is live in Box, or keep them as the build record.

## Current builds

| Slug | Seat | Stage |
|---|---|---|
| `hospitality-craft-educator` | Hospitality Craft Educator | 0 framed. Head start on 1 to 3 from chat (unvalidated, see HEAD-START.md). Build in Claude Code per RUNBOOK.md |
| `practice-simulation-designer` | Practice and Simulation Designer | 0 framed. Build in Claude Code per RUNBOOK.md, after the Hospitality Craft Educator |

Run the builds from `RUNBOOK.md` in this folder.

## Why these two seats

The Learning & Development cluster is strong on pedagogy and weak on hospitality. The Curriculum & Program Architect states that its grounding is mostly formal education and that its transfer to a hospitality workforce is reasoned, not validated. The Instructional Designer says the same of its lab-derived effects. The Hospitality Operations Realist knows the floor but tests tempo; it designs no learning. The Culture Implementer holds ritual. No seat owns **what the craft of hospitality is as a teachable discipline**, and no seat owns **how to build practice that rehearses hospitality judgment and performance**. Those are the two gaps.
