<!-- Phase 2 working output, run wf_c7d3565a-a0f, 2026-09-28. Raw agent return, not reviewed line by line. The synthesis is research/starting-structure-2026-09.md. -->

# Profile panel read: Instructional Designer, Assessment & Competency Designer, Learner Advocate

**Basis.**
- Profiles read in full from `profiles/cache/`:
  - `instructional-designer.md`, Box `2349382165394`
  - `assessment-competency-designer.md`, Box `2349454588688`
  - `learner-advocate.md`, Box `2351610057004`
- All three are validated seats. The stage-6 caveat does not apply to them. Where a read hands work to the Hospitality Craft Educator or the Practice and Simulation Designer, those two seats are unvalidated, and that is noted where it happens.
- Also read: the intake (`research/intake-2026-09.md`), `framework/*`, `catalog/catalog.yaml` and `canon/standing-rules.md`.
- Every external research claim below comes from a seat's own corpus and was not re-read in this pass. Status is **unverified** throughout. It becomes verified-primary only once the source is opened.

---

## 1. Instructional Designer (`instructional-designer`)

**Read in its lane.**
- **Right: splitting movement from decision (1.6, and the `job: do-drill` tag).** This matches stage-dependent support and teaching a skill's parts before combining them. Brandon's music analogy in intake group 5 points the same way. Evidence: Fitts & Posner; Sweller on how many things a learner must hold at once. Unverified.
- **Right: "one objective, one learning job" on the critical path, with a required retrieval schedule (4.8 option c).** This rule is on the evidence and is not a time cap. Evidence: retrieval and spacing (Make It Stick; Cepeda). Unverified.
- **Right: measuring behavior on the floor (4.7 b)** rather than completion. This is the Kirkpatrick level 3 standard the seat already holds.
- **Wrong: every Introduce module assumes a novice learner.** Brandon hires "highly capable people" (intake group 7), and the proposal gives no experienced-hire path. Guidance that helps a novice hurts an expert (Kalyuga/Sweller, the expertise-reversal effect). Unverified.
- **Wrong: onboarding is massed into one block.** Step 2 of 1.6 loads the whole ORI and CUL core, plus each branch's Introduce modules, into a single remote session. With no spaced return before G1, it will not hold.
- **Wrong: some catalog rows are not instruction gaps.** Several rows describe environment, tool or policy problems, which fail the front-end check.
- **Wrong: 1.7 G2 makes the gate the first time movement and decision combine.** Combining them should first happen in practice with feedback, so G2 checks a combination the learner has already practiced.

**What it would challenge.**
- **All I-slot modules on the critical path (SVC-003, SVC-005, BEV-002, BEV-004, SVC-006, and the core).**
  - Require `### Novice` and `### Experienced` paths under `module-spec.md`.
  - Add an explicit "contrast and unlearn" step for veterans whose old habits conflict with the house standard.
  - Move the "proven prior experience can shorten the path" idea (PS B1) out of the cross-training row in 1.5 and apply it to every entry node.
- **1.6 step 2 (remote onboarding).**
  - Limit the remote block to know-it and see-it pieces.
  - Schedule retrieval returns into the first on-site sessions and first shifts.
  - Put short conversations between the screen pieces, as Brandon asked in group 5.
  - Nothing that needs correction ships as screen-only.
- **1.7 G2.** Add an integration practice step after the drills and before G2: whole-task, on a real or closely simulated station. G2 then checks the combination; it does not introduce it.
- **SVC-003, SVC-004, SVC-005 drills.**
  - Interleave the three across sessions instead of blocking each one.
  - Hold practice on the real floor surface wherever possible, because near transfer needs shared surface features (Baldwin & Ford). Unverified.
- **4.5 b (take-home kits).**
  - A video exemplar models the movement but cannot give feedback, and a self-rating is not feedback either.
  - The check-in has to include a teach-back or observed rep with correction. That is the approximation of deliberate practice the seat accepts (Ericsson; Collins). Unverified.
- **Front-end check, rows to route out or recast:**

  | Row | Problem | What it wants |
  |---|---|---|
  | BEV-007 | "Reactive restock" is a par and workflow condition. | A job aid after the workflow is set, not a module. |
  | SYS-001 | A tool procedure (`bindings.md`: "mostly bindings" means a job aid later). | Should not sit on the runner's critical path as a module that cannot be built. |
  | SVC-009 | The stated need, "house response is undefined", is a policy gap. | Instruction follows the policy and cannot replace it. |
  | SVC-004 | Layout is unsettled, which is an environment dependency. | Hold at `identified`. |

- **ORI-005 on the critical path (load).**
  - It adds know-level load before the first shift, with no floor task that needs it on day one.
  - The seat flags the load and routes the placement question to the Curriculum & Program Architect. Placement is not this seat's call.
- **LEA-004 (Writing a module).**
  - The five moves live in the authoring template's structure. LEA-004 teaches authors to use the template; it does not replace it.
  - The seat owns the template's instructional soundness and wants it listed as a separate deliverable in §2.
- **LEA-005 (Running pre-shift).** Add a retrieval schedule mapped to shift rhythm. Pre-shift is where spacing actually lives, even though it does not count toward progression.
- **SVC-006 and SVC-008 (integrative craft).** Keep these whole-task, with a modeled example and coaching. Do not break them into checkbox objectives. SAF-001 is the opposite case: one crisp behavioral objective with a criterion.

**Gated items.**
- **Founder-gated:**
  - Whether experienced hires get credit on entry nodes (INT C2, the unlock rule).
  - Whether take-home practice is paid, and how (`fact.take_home_allowance`). This one is also an HR matter.
- **Chef-gated:** G2 small-menu content, SVC-005 plating, and the SAF-001 matrix.
- **Team-gated:** pre-shift format and timing, and the drill session cadence (`workflow.*`).
- **Elicitation-gated:**
  - ORI-003, SVC-007 and BEV-009 cannot be designed until Brandon's decision interviews run.
  - Any incident that touches Coqodaq, Alinea or Gracious is flagged for Brandon and not reconstructed.
  - The on-floor "cues present" for SVC-006 depend on the Hospitality Craft Educator, whose seat is unvalidated (stage 6 skipped).

**Disagreements.**
- **With the proposal (1.7 G2 wording):** G2 as the first point of integration.
- **With the Assessment seat, mild:** the ID puts retrieval sets before G1 as learning devices. The Assessment seat is right that G1 is not the readiness gate. Both seats agree on that boundary.
- **With Brandon's "don't spend paid time on drills" (intake group 5):** the ID holds that movement skill needs corrected reps. Cutting on-site reps without a feedback substitute trades time for retention.

---

## 2. Assessment & Competency Designer (`assessment-competency-designer`)

**Read in its lane.**
- **Right:**
  - Nodes light on evidence only. Completion never lights a node. This rejects completion as competence (Popham; mastery-based models). Unverified.
  - The L1 to L5 supervision levels map to entrustment-supervision scales, and entrustment looks forward (ten Cate). Unverified.
  - G3 and G4 move the release decision to real performance in the real setting, the "does" level (Miller). Unverified.
  - Team feedback at G4 is formative and never a vote.
  - A manager co-rates near the cut line and where rater and candidate are close. That is sound structure.
- **Wrong: the L4 release is under-sampled.** L4 rests on one L3 shift (G4). G3 is L2 direct supervision, so it is not evidence for independent work. One occasion at the level being entrusted is ad hoc entrustment, not a summative sign-off.
- **Wrong: G1 moves on things that are not readiness.** A spoken knowledge check carries fluency, nerves, second-language load and rapport with the rater. The LE R13 note ("content scored, not fluency") is the right intent, but the proposal has no anchors to enforce it.
- **Wrong: the activity tree and role manifest (§5) list tasks.** A list of tasks is not a competency model. Nothing in the proposal defines what separates a clearly-ready performer from a not-yet one on each node.

**What it would challenge.**
- **1.6 steps 7 and 8, and 1.7 G4.**
  - Change G4 from "the second live shift" to a window of L3 shifts.
  - Keep collecting until one more observation would not change the call (saturation), with more than one rater where the stakes warrant.
  - State L4 as a forward-looking entrustment level, not a pass mark.
- **1.7 G1.**
  - Keep it as a knowledge prerequisite. Never let it certify floor readiness.
  - Write behavioral anchors on content.
  - Allow a show-don't-tell response, pointing or demonstrating, so language is not scored.
  - Once pass rates exist, run the four-fifths screen by group (Messick; EEOC Uniform Guidelines). Unverified.
- **SAF-001 inside G1.** A spoken knowledge check reaches only "knows" and "knows how". Allergy routing must also be shown at G2 and observed at G3, and it must be non-compensatory: a miss on allergy cannot be offset by strengths elsewhere.
- **4.3 c (banking versus one sitting).**
  - Isolated movement drills can be banked as prerequisites.
  - The integrated G2 performance cannot be banked in parts, because a step checklist hides the integrated judgment (critique of OSCE checklists).
  - Safety elements are pass-required in every attempt.
- **4.3 (fail limit).** Separate the criterion from the cut. Whatever the attempt rule, set the cut per node by contrasting groups: leads sort clearly-ready and clearly-not-yet people on the anchored dimensions, and the cut sits where the groups separate. Set it on importance, not difficulty, and document it (Hambleton & Pitoniak). Unverified.
- **4.11 Option A, `gate-spec` row.**
  - Make a per-node gate spec an exit criterion at `designed` for any module that feeds a gate.
  - The spec holds the construct definition, the anchors, the evidence level, and the number of occasions and raters.
  - SVC-001 cannot be designed until the gate specs for its nodes exist. This seat defines "ready", and SVC-001 teaches toward that definition.
- **LEA-002 (Assessing a practical).**
  - The need is framed as a rater-training problem. The seat holds that structure does more: anchors, standard-setting and sampling come first, and calibration training is partial insurance.
  - Evidence: an RCT on rater training (Kogan et al.) and work on rater thinking (Govaerts). Unverified.
  - Reword the need, and make the co-rated audits the load-bearing part of L5 release.
- **1.7 periodic practical.**
  - Separate a refresher (learning) from a recheck (a decision).
  - A short G1 plus G2 in an early-arrival window is below the "does" level. It cannot revoke an L4 entrustment on its own.
  - Name what a recheck miss triggers before it runs.
- **1.7 CEO override.** An override sits outside the validity argument. Log each one with a reason, and track downstream floor performance for people who were overridden as a consequence signal.
- **1.7 G4 team feedback.** Calibrated raters should not see the synthesized team feedback before they record their own rating. Otherwise popularity and rapport leak into the decision.
- **ORI-004 ("humility as an assessable trust condition").** A trait word cannot be rated reliably. Anchor it to observable behavior, for example "asks before acting on an unfamiliar allergy call", or drop it from G4 criteria.
- **4.7 a (SJT agreement with an expert panel).** Acceptable as a learning and alignment measure. While the panel is one person it is single-source, and it must never gate advancement until the panel includes calibrated leads.
- **1.6 step 1 (paid practical interview "designed together with gate 2").**
  - A selection instrument is an employment decision, and adverse-impact monitoring applies to it with more force.
  - Keep it separate from G2 evidence, and route it to the HR seats.
- **4.2.** Option (a) fails in this lane because the record does not name the assessor, so decision consistency cannot be audited. Options (b) and (c) both carry rater identity and anchored ratings. The system choice is Brandon's.

**Gated items.**
- **Founder-gated:**
  - The gate record system (`founder.gate_record_system`) and the override path.
  - Whether pay attaches to gates (4.12, C8). If it does, stakes rise, the evidence requirements rise, and so does the risk of teaching to the gate.
  - Confirming the "angel shift" name.
- **Team-gated:**
  - The fail limit (intake group 4).
  - The cut per node. Contrasting groups needs leads who exist, so this waits on hiring.
- **Chef-gated:** G2 small-menu content, and the SAF-001 matrix (`chef.*`).
- **HR:**
  - Hourly leads rating alone (4.4).
  - The paid practical interview as a selection tool.
  - Adverse-impact monitoring.
- **Elicitation-gated:** node competency models need a superior-versus-not-yet comparison that cannot run before opening. Until then, the seat names procedural defensibility (multiple observers, anchors, aggregation) as a stand-in for a computed decision-consistency figure.

**Disagreements.**
- **With Brandon's conversation-only knowledge portion (intake group 4):** the seat accepts spoken format as a founder call. It flags that format as the most likely source of variance that has nothing to do with readiness, and wants the anchors and a non-verbal route.
- **With the proposal's reliance on LEA-002 calibration** (see above).
- **With the Instructional Designer:** they agree that retrieval checks are learning devices and not gates.
- **With the Learner Advocate:** they meet on G1 and G4 from two directions. Something that raises threat is, for this seat, variance unrelated to readiness, and for the Advocate, a harm to the learner.
- **With the Practice and Simulation Designer (unvalidated, stage 6 skipped):** the proposal's G2 analog, the sommelier service practical (PS C1), sits at the "shows how" level. How closely it predicts live floor performance is untested, so G2 cannot stand in for G3 and G4.

---

## 3. Learner Advocate (`learner-advocate`)

**Read in its lane.**
- **Right: the design gives learners autonomy.**
  - An activity tree the learner can see.
  - Electives off the critical path.
  - "Learning or move", with both answers fine.
  - "Not now, with a reason" as a named outcome.
  - This reads as informing the learner rather than controlling them (Deci & Ryan). Unverified.
- **Right: per-node states avoid a single aggregate readiness score.** That suits learners who are strong in one area and weak in another (Rose). Unverified.
- **Right: G4 team feedback is private, task-focused, synthesized by a lead, and never a vote.**
- **Wrong: G4 as written is a public display of not-yet competence.** "Prove it to your team", on the trainee's second live shift, in front of the whole crew, is the highest-threat moment in the house. Threat competes with the task for working memory, so a competent trainee can fail on composure (anxiety and working-memory research; Schmader & Johns). Unverified.
- **Wrong: remote onboarding meets the learner alone.** The learner is on their own device, sometimes reading in a second language, with no one to ask. Concealment is the default response, so silence will read as comprehension.
- **Wrong: nothing puts a real novice in the room before a module ships.** The 4.11 panel changes add seats but never a receiving-end learner.

**What it would challenge.**
- **1.7 G4.**
  - Change the frame from proving oneself to the team being there as support.
  - Tell the learner in advance what feedback will be collected, from whom, and how it reaches them.
  - The learner sees only the lead's synthesis, privately, pointed at task steps (Kluger & DeNisi, task versus self). Unverified.
  - Cross-role critique (CUL-002) must be practiced at low stakes before it is ever aimed at someone on a gate shift.
- **1.7 G1.**
  - Add a private rehearsal with a peer before the spoken check.
  - Offer a show-don't-tell route.
  - Frame the check as a current, improvable skill, not a read on ability. Framing a check as diagnostic of ability raises belonging threat (Steele; Walton & Cohen). The effect size is contested; the fix is kept because it costs almost nothing. Unverified.
- **SVC-001 (gate module).** Add a "how not-yet is delivered" requirement: the verdict names the next task step and keeps the person out of the sentence, and early misses are normalized as common. This seat writes none of it; the Assessment seat owns the wording, but it does not ship without it.
- **1.2 node states.**
  - "Recheck due" can read as suspicion of the learner. Framing is a direction for the owning seat.
  - A "not yet" must never display as a failure state on a node.
- **4.1 b (wall map).** A public map of individual positions invites social comparison and shows who is behind. The wall map may show the structure of the tree; individual progress stays private by default. The seat agrees with leaving leaderboards and streaks off.
- **4.3 (fail limit).**
  - A hard attempt count framed as elimination is the diagnostic threat the seat warns against.
  - It favors option (b), an interval plus a changed practice plan.
  - The "conversation about fit" after repeated misses must not read as a verdict on ability.
- **1.6 step 2 and ORI-001 to ORI-005 (remote block).**
  - Cut the text and the jargon.
  - Assume second-language and low-literacy learners are present and concealing.
  - Use a comprehension check that does not require the learner to confess "I could not read this".
  - Add a first on-site check-in that surfaces gaps without exposing anyone.
- **ORI-004 and the G4 humility criterion.** Rating humility rates the person. Recast it as an observable task behavior.
- **4.11 (lifecycle changes).**
  - Add a novice-attempt test as an exit criterion at `reviewed` for every critical-path module: a recent receiving-end learner tries the module cold, and their points of confusion become the defect list.
  - This matters most for LEA-004 peer authoring, where the strongest server is the likeliest to skip foundational steps (the curse of knowledge; Hinds). Unverified.
- **4.7 and SVC-007 / BEV-009 ("decisions the way Brandon would").** The expert-comparison reveal should show the reasoning ("what the expert noticed"), not "you were wrong". Otherwise alignment training reads as control.
- **4.7 c (complacency signals).** "The same few voices answering" is a prompt to look for concealment. It must never be recorded as a mark against an individual.

**Gated items and routing.**
- **Founder- and team-gated:** the G4 format. It is Brandon's idea (intake group 4), and its final shape is the team's call. This seat names the harm and does not decide the format.
- **Team-gated:** the fail limit.
- **Elicitation-gated:** the novice-attempt test needs real receiving-end learners. None exist before opening, so the first cohort, or hires from comparable backgrounds, fill it later. Brandon deferred learner-experience tracking (intake group 7). This requirement is consistent with that deferral because it is in-design testing, not a survey system.
- **Routed out of lane, not annexed:**
  - Take-home practice pay (4.5) and early-arrival refresher time go to the Frontline Advocate and HR.
  - Lead shift scope (LEA-009, 4.4) goes to the Emerging Leader Advocate.
  - The mistreatment policy behind SVC-009 goes to the founder and HR. This seat keeps only how the module meets the learner who has been mistreated.

**Disagreements.**
- **With Brandon's whole-team critique vision for the last shift (intake group 4):** the seat supports the cross-role critique culture as a goal. It disagrees with making a trainee's gate shift the first place that culture is aimed at a person.
- **With proposal 4.1 b:** the wall map.
- **With the Instructional Designer:** they are aligned. Interleaving and desirable difficulty will feel worse to learners, so the seat asks that struggle be named as expected and normal, not that the practice be softened.
- **With the Assessment seat:**
  - Converging: both require the evidence spread across more than one lower-threat occasion.
  - A mild tension: the Assessment seat rules out banking parts of the integrated G2. The Advocate supports banking for movement parts because learners are uneven across skills, and accepts that the combined performance and safety elements cannot be banked.