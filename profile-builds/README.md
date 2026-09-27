# Profile builds

Workspace for building new specialist profiles before they go to Box. Each build runs the seven-stage synthesis procedure (ClickUp `2ky45bmy-16853`, page `2ky45bmy-27213`): `/build-profile <slug>` for stages 0 to 5, then `/validate-profile <slug>` in a fresh session for stages 6 and 7.

A finished profile leaves this folder for Box through the Profile Update Protocol. Nothing here is canonical. Delete a build folder's working files once the profile is live in Box, or keep them as the build record.

## Current builds

| Slug | Seat | Stage |
|---|---|---|
| `hospitality-craft-educator` | Hospitality Craft Educator | Live in Box `2491194239261` (2026-09-27). Stage 6 skipped by founder decision; Stage 7 passed 3 of 3 on the build model |
| `practice-simulation-designer` | Practice and Simulation Designer | Live in Box `2491190356107` (2026-09-27). Stages 6 and 7 skipped by founder decision |

Both seats are built. To validate either later, run `/validate-profile <slug>` per `RUNBOOK.md`, then replace the Box file through the Replacement Queue.

## Why these two seats

The Learning & Development cluster is strong on pedagogy and weak on hospitality. The Curriculum & Program Architect states that its grounding is mostly formal education and that its transfer to a hospitality workforce is reasoned, not validated. The Instructional Designer says the same of its lab-derived effects. The Hospitality Operations Realist knows the floor but tests tempo; it designs no learning. The Culture Implementer holds ritual. No seat owns **what the craft of hospitality is as a teachable discipline**, and no seat owns **how to build practice that rehearses hospitality judgment and performance**. Those are the two gaps.
