# Modality library

The menu of ways a learner can engage with a module. Organized by the learning job each one does, not by tool, so the design decision comes first and the platform follows.

`/design-module` must consider at least three modalities for each practice component and record why it chose one. `python scripts/status.py variety` flags any program whose modules lean on the same two or three modalities.

**Why this file exists.** The default failure of hospitality training is a stack of text, a video, and a multiple-choice quiz. That combination teaches recognition, not performance. The Instructional Designer names it directly: a view is not competence, and recognition is not recall. Most of what matters at Sŏn is perception, judgment, and performance under load, and those need different modalities.

## How to read an entry

- **Job:** the learning job it does.
- **Use when:** the kind of skill it fits.
- **Evidence:** `strong` (replicated research), `moderate` (good research, narrower), `principle` (sound design reasoning, not a tested effect in this setting).
- **Delivery:** where it can run. `T-native` Trainual built-in and tracked. `T-embed` embedded in Trainual, runs but does **not** report completion or score. `SCORM` packaged and uploaded to Trainual, tracked. `Live` on the floor or in a pre-shift. `Synthesia` AI video. See `adapters/`.

---

## 1. Know it (build and keep knowledge)

| Modality | Job | Use when | Evidence | Delivery |
|---|---|---|---|---|
| Spaced retrieval set | Pull knowledge back from memory days apart | Facts that must hold: menu, allergens, vocabulary | strong | T-native test (randomized question bank), SCORM, Live (pre-shift call-and-response) |
| Free recall prompt | Write or say everything you remember, then check | Consolidating a whole topic | strong | T-native written response, Live |
| Flashcards / dialog cards | Self-test with immediate check | Vocabulary, pairings, Korean terms, dish components | strong (as retrieval) | T-embed (H5P dialog cards), SCORM |
| Tasting with recall | Taste, describe, then recall later | Menu and beverage knowledge | principle | Live, then T-native written or video response |
| Elaborative "why" prompt | Explain why a rule exists | Rules people bend under pressure | moderate | T-native written response, Live |

## 2. See it (train perception)

The skill of noticing: reading a table, spotting a setup fault, catching the cue before it becomes a complaint. Rarely trained, and central to how the Brand Guidelines frame service (pull the Service Choreography page before designing here).

| Modality | Job | Use when | Evidence | Delivery |
|---|---|---|---|---|
| Spot the difference | Compare correct and incorrect | Table setup, plating, station standard | moderate (perceptual learning) | T-native (image in test), T-embed (H5P image hotspots), SCORM |
| Hotspot / "what's wrong here" | Find the fault in a real photo | Setup precision, safety hazards | moderate | T-embed (H5P find-the-hotspot), SCORM |
| Cue identification clip | Watch a short scene, name what the expert would notice | Reading a table, pacing signals | moderate | Synthesia or real footage plus T-native written response, SCORM |
| Contrast pairs | Many quick near-miss examples | Fine distinctions (ready vs almost ready) | moderate (perceptual learning) | SCORM, T-embed |
| Walk-through observation | Stand where the expert stands and name what you see | Floor awareness | principle | Live |

## 3. Decide it (train judgment)

| Modality | Job | Use when | Evidence | Delivery |
|---|---|---|---|---|
| Branching scenario | Make choices, live with consequences, recover | Service recovery, the ambiguous table, escalations | moderate | SCORM (repo player or H5P), Synthesia (branching buttons), T-embed |
| Expert-comparison (ShadowBox style) | Decide, then compare your reasoning to experts' | Judgment calls with no single right answer | moderate | SCORM, T-native written response then reveal, Live debrief |
| Situational judgment item | Rank or pick the best of several responses | Quick judgment checks; also usable in a gate | moderate | T-native single or multiple select, SCORM |
| "What would you do" pre-shift | One scenario, spoken answers, lead gives the rationale | Keeping judgment warm across the team | principle | Live |
| Case from last night | A real (anonymized) moment, debriefed | Turning service into curriculum | principle | Live, T-native written reflection |

## 4. Do it (train procedure and performance)

| Modality | Job | Use when | Evidence | Delivery |
|---|---|---|---|---|
| Worked example, then faded | Full example, then partial, then solo | Novices on any multi-step skill | strong | Any. Text, SCORM, Live |
| Sequencing / sort the steps | Put the steps in order | Procedures where order matters | moderate | T-embed (H5P drag and drop), SCORM |
| Flowchart walk | Trace a decision path | Procedures with branches | principle | T-native flowchart |
| Behavior modeling | Watch a credible model, practice, get feedback | Interpersonal skills: greeting, recovery, upsell without pressure | strong (behavior modeling training) | Real footage or Synthesia, then Live practice |
| Role-play with rubric | Rehearse with a partner against explicit criteria | Conversations with the customer or a teammate | moderate | Live, T-native video response |
| Video teach-back | Record yourself explaining or doing it | Proving understanding in your own words | principle | T-native video response question, in-app recorder |
| Shadow, then reverse shadow | Watch an expert, then be watched by one | Floor stations | principle (cognitive apprenticeship) | Live |
| Observed floor demonstration | Perform at tempo while an assessor scores it | Readiness gates | strong as a gate form (assessment seat decides validity) | Live, recorded via assessor sign-off (see adapters/trainual.md) |

## 5. Hold it (reflection and integration)

| Modality | Job | Use when | Evidence | Delivery |
|---|---|---|---|---|
| Plan-do-review | Plan the shift, do it, review it | Building self-directed improvement (HighScope seat) | moderate | Live, T-native written response |
| Post-shift debrief prompt | Three questions after service | Converting experience into learning | principle | Live, T-native checklist plus written response |
| Try-this-shift card | One behavior to try next shift | Transfer to the floor | moderate (transfer research) | T-native page, job aid, Live |

## 6. Find it (reference at the point of need)

Not teaching. Support for when the learner is already on the floor. The Instructional Designer's rule: a reference used under load beats a linear clip.

| Modality | Job | Delivery |
|---|---|---|
| Job aid card | One screen, one task | T-native page, print, mobile |
| Checklist | Repeatable sequence, self-completed | T-native checklist |
| Flowchart | Branching procedure | T-native flowchart |
| Searchable answer | "How do we..." | Trainual search and AI assistant (not SCORM content, which the assistant cannot read) |

## 7. Teach it (peer teaching)

Members can author and teach modules. Teaching is also one of the strongest ways to learn.

| Modality | Job | Delivery |
|---|---|---|
| Micro-lesson at pre-shift | A peer teaches five minutes | Live, facilitator guide |
| Peer-authored module | A qualified member builds a module from the template | This repo |
| Teach-back to a new hire | Cross-trained member teaches the station they just learned | Live |

---

## Choosing: the three questions

1. **What does the learner have to do on the floor?** Know, see, decide, do, hold, or find. Pick from that section first.
2. **Does it need feedback?** If the skill needs correction in real time, it needs a person. Video models, a coach corrects.
3. **Does it need a record?** If yes, it must be `T-native` (test, checklist, e-signature) or `SCORM`, or a live demonstration logged by an assessor. `T-embed` interactions teach but leave no record.

## Adding a modality

When research or practice turns up a new one, add a row here with its evidence level and delivery options, and note the source in the commit message.
