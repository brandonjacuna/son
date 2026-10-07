# Review panels

`/review-module` loads the panel for the module's domain. Every module gets the core panel. Each seat reviews in its own lane and logs a finding in `review-log.md`, even if the finding is "no issue in my lane."

## Core panel (every module)

| Seat | Asks |
|---|---|
| Learner Advocate | Is this built for the learner in front of us, or for the designer? |
| Instructional Designer | Does it teach, or only inform? Retrieval, spacing, load, medium. |
| Educational Materials Author and Editor | Does it read right, in one voice, within canon? |
| Hospitality Operations Realist | Does the behavior this module teaches survive a Friday at 8:15 with a green crew? |
| Frontline Advocate | Will the hourly team find this respectful, useful, and worth their time? |

## Added by domain

| Domain | Add |
|---|---|
| ORI orientation | Values and Belonging Designer, Culture Implementer |
| SVC service craft | Hospitality Craft Educator, Practice and Simulation Designer |
| BEV beverage | Hospitality Craft Educator |
| KIT kitchen craft | Hospitality Craft Educator; chef sign-off required before `parked` |
| SAF safety and compliance | Assessment & Competency Designer (always), HR Implementer |
| SYS systems | none beyond core; most content is bindings |
| LEA teaching and leadership | Emerging Leader Advocate, Organizational Systems Architect, Performance and Feedback Systems Designer |
| CUL culture | Culture Implementer, Culture Signal Designer |

## Added by feature

| If the module | Add |
|---|---|
| is or feeds a readiness gate | Assessment & Competency Designer |
| includes correction, feedback, role-play, or team feedback | TBRI |
| uses plan-do-review or active participatory practice | HighScope |
| has a scenario, role-play, simulation, perception drill, or video component | Practice and Simulation Designer |
| changes the tree's structure, an unlock rule, or a role definition | Organizational Systems Architect (only then) |
| sits in the program sequence in a new place | Curriculum & Program Architect |

Seats marked `to-build` in `profiles/manifest.yaml` are skipped with a logged note until they exist in Box.

## Rules added by the system design

- Any module that feeds a gate: the Assessment & Competency Designer signs its gate spec at `designed` (D18).
- `library` rows: core panel only, plus the Hospitality Craft Educator where the track touches the craft.
- `linked` rows: no panel. The HR Implementer confirms the source meets the requirement.
- The authoring template's instructional soundness is a deliverable owned by the Instructional Designer.
