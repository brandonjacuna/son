# Module source package

One folder per module: `modules/<domain>/<ID>-<slug>/`. Copy `templates/module/` to start one. Every file is plain Markdown or YAML so it renders anywhere and diffs cleanly.

## IDs and domains

`<DOMAIN>-<NNN>`, numbered in order of identification. Numbers never get reused.

| Domain | Prefix | Covers |
|---|---|---|
| Orientation | ORI | Why before how: mission, values, the standard, how the house works. |
| Service craft | SVC | Front-of-house hospitality: reading the table, pacing, recovery, the service sequence. |
| Beverage | BEV | Beverage knowledge and service. |
| Kitchen craft | KIT | Back-of-house craft. Heavily chef-gated. |
| Safety and compliance | SAF | Allergens, food safety, alcohol service, workplace safety. |
| Systems | SYS | The tools. Mostly bindings until tools are set. |
| Teaching and leadership | LEA | Teaching a module, coaching, leading a shift, the leadership strand. |
| Culture | CUL | Rituals, recognition, belonging as practiced. |

## Files

| File | Required | Holds |
|---|---|---|
| `module.md` | Always | Front matter (below) and the design rationale. |
| `content.md` | Always | The teaching content, organized by the five moves. |
| `scenarios.md` | If the design calls for judgment practice | Branching scenarios in the neutral format below. |
| `assessment.md` | Always | Low-stakes checks, and the gate if the module has one. |
| `job-aid.md` | If a point-of-need reference helps | One screen or one card. |
| `video-script.md` | If any component is video | Scene-by-scene script, tool-neutral. |
| `facilitator-guide.md` | If any component is live | For a pre-shift, a coaching session, or a peer teacher. |
| `bindings.yaml` | Always (may be empty) | Declared bindings. |
| `review-log.md` | Always | Findings, resolutions, gated items. |

## module.md front matter

```yaml
---
id: SVC-001
title: Reading the table
domain: service-craft
status: identified            # see framework/lifecycle.md
learners:
  - role: server
    stage: novice             # novice | experienced | cross-training
program:
  slot: introduce             # introduce | reinforce | master
  prerequisites: [ORI-001]
  unlock: mastery             # time | mastery | both (framework/system-design.md D2). Any time period is a binding.
  gate: false                 # true if this module is or feeds a readiness gate
transfer_goal: >
  On their own, a server can ...
objectives:
  - Observable verb, condition, criterion.
components: [content, scenarios, assessment, job-aid]
media:                        # one entry per component; see framework/modality-library.md
  content: text
  scenarios: scorm-scenario
modalities_considered:        # required from 'designed' onward
  practice: [branching scenario, role-play with rubric, situational judgment item]
  chosen: which, for which part
  why: >
    Tied to what the learner does on the floor, whether it needs feedback,
    and whether it needs a record.
mastery_score: 70             # used by SCORM builds
craft_owner: hospitality-craft-educator   # or chef-gated, or another seat
closing: One line the learner takes into the next shift.
profiles_consulted: []
published: null               # link once published
---
```

## content.md structure

Five headings, always in this order. They carry the pedagogy structurally so a peer author cannot skip a move.

1. `## Activate`: the reason before the mechanics. Why this matters to the customer and to the person learning it.
2. `## Demonstrate`: what good looks like, with the expert's thinking said out loud, not only the steps.
3. `## Practice`: what the learner does, with feedback. Points to `scenarios.md` or `facilitator-guide.md`.
4. `## Retrieve`: recall checks scheduled after the module (next shift, one week), not a re-read.
5. `## Integrate`: where this shows up on the floor and what to try on the next shift.

A module with an experienced-learner path marks sections with `### Novice` and `### Experienced` under the relevant heading.

## scenarios.md format

```
## Scenario S1: <title>

**Setup.** What the learner sees and hears. Two to four sentences.

**Cues present.** What an expert would notice here. (Supplied by the Hospitality Craft Educator.)

### Decision 1
Prompt: What do you do?
- A. <choice> -> go to 1A
- B. <choice> -> go to 1B
- C. <choice> -> go to 1C

### 1A
Consequence: what happens next, shown not told.
Feedback: why, tied to the cue the learner used or missed.
Expert rationale: what the expert noticed and why they chose what they chose.
Next: Decision 2 | End (strong) | End (recoverable) | End (failure)
```

Every scenario needs at least one recoverable path. Failure paths teach recovery, not only avoidance. Optional `Media: <url>` lines (on the setup as `**Media.** <url>`, or on any node) attach an image, a video file, or an embeddable video such as a Synthesia share link or real footage. Choices are shuffled by the player, so write them without relying on order, and keep the strong choice from being the longest or the obviously kind one. `python scripts/build_scorm.py` validates the structure.

## video-script.md format

A table per scene: scene number, purpose, narration or dialogue, on-screen text (only when it adds something the narration does not), visual direction, interaction point (button, branch, question, or none). Visual direction is a brief, not a prompt. The Design Translating Team turns it into a prompt at render time.
