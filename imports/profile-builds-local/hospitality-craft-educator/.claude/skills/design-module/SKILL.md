---
name: design-module
description: Design a module from its concept brief: objectives, the five teaching moves, learner paths, modality choice per component with reasons, assessment plan, and bindings.
---

# Design module

Load: Instructional Designer, Assessment & Competency Designer, Practice and Simulation Designer (if live), plus HighScope or TBRI if the module involves plan-do-review, correction, or role-play.

1. Read the concept brief.
2. Objectives: observable verb, condition, criterion. Crisp behavioral objectives for provable standards; whole-task practice for integrative craft.
3. Plan the five moves (activate, demonstrate, practice, retrieve, integrate) and the novice and experienced paths if both take it.
4. **Modality choice.** For each practice component, list at least three candidates from `framework/modality-library.md` and apply the three questions (what the learner does on the floor, whether it needs feedback, whether it needs a record). Record the choice and the reason in `modalities_considered`. Check `adapters/trainual.md` for what each delivery option can actually record.
5. Assessment: separate the learning checks (mine to build) from any gate (the Assessment seat decides validity and form).
6. List every binding in `bindings.yaml`.
7. Update `module.md`, set status `designed` in both places.
8. Run `python scripts/status.py variety` and flag if the program is drifting toward the same few modalities.

Commit: `ID designed: <modalities chosen>`.
