# Module lifecycle

A module moves forward only when the current stage's exit criteria are met. Status lives in two places that must agree: `catalog/catalog.yaml` and the `status` field in the module's `module.md`.

| Stage | What happens | Exit criteria | Command |
|---|---|---|---|
| identified | A training need is logged. | Need stated as an observed gap in performance, not a topic. Front-end check done: is this a knowledge or skill gap, or is it tools, conditions, tempo, or motivation? If it is not instruction, it is routed out and the row is closed as `routed-out`. | `/identify` |
| concept | The need becomes a concept brief. | Transfer goal written as an autonomous performance ("on their own, a person can..."). Program slot named: domain, prerequisites, and whether this module Introduces, Reinforces, or Masters. Learners named (who, at what stage). Owner of the craft content named (Hospitality Craft Educator, chef-gated, or other). | `/ideate` |
| designed | The module is designed. | Objectives with observable verbs. The five teaching moves planned (activate, demonstrate, practice, retrieve, integrate). Novice and experienced paths if both learners take it. Medium chosen per component with a reason. Assessment plan: low-stakes checks versus any gate, with gate validity signed by the Assessment seat. Bindings listed. | `/design-module` |
| drafted | The source package is written. | Every component the design calls for exists. Every tool or workflow dependency is a declared binding. `python scripts/lint.py` passes. | `/draft-module` |
| reviewed | The panel has read it. | Every panel seat in `framework/review-panels.md` for this module type has a logged finding. Every finding is resolved, or marked founder-gated, chef-gated, or team-gated. | `/review-module` |
| parked | Complete except for bindings. | Lint passes. Every open item is a declared binding. Review log clean. **This is the target state until tools and workflows are set.** | `/park-module` |
| bound | Bindings filled. | Every binding in `bindings.yaml` has a value and a source. Figures came from Airtable. Chef-gated values confirmed by the chef. | `/bind` |
| rendered | Output produced for a platform. | Adapter run. Output in `exports/`. Any AI design or video prompt ran through the Design Translating Team. | `/render` |
| published | Live on the platform. | Link recorded in `module.md`. Frozen release snapshot in Box. | manual, then `/status` |
| measured | Evidence it works. | A behavior-level measure (Kirkpatrick level 3 or a success-case read), not only completion or a satisfaction survey. | manual |
| retired | Out of use. | Reason logged. | manual |

## Re-ideating a parked module

Parked modules are meant to be picked back up. To rework one, move it back to `concept` or `designed` in both places, log why in `review-log.md`, and walk it forward again. Git history keeps the earlier version.

## Gate decisions nobody can land here

Some calls belong to Brandon, the chef, or the team. A profile will say so. Record them in `review-log.md` with one of these marks and leave them open: `founder-gated`, `chef-gated`, `team-gated`. A module can park with gated items only if each one is also a declared binding.
