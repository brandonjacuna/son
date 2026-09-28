# System design

The governing document for how Sŏn's module system works. Every decision here was made by Brandon in the Phase 3 discussion of the starting structure (`research/starting-structure-2026-09.md`), from his intake (`research/intake-2026-09.md`). Where this file and another framework file disagree, this file wins until the other file is updated.

Each decision records the question, the options on the table, the call, the reasoning, and what it changes. Question numbers refer to section 4 of the research.

## Decisions

### D1. Who owns people and training (question 1)

**Decided 2026-09-28.**

**Options on the table.** (a) The Maître d' owns people and training, as the white paper sets it (WP Part I). (b) The operations role owns them, as the intake first described. (c) The pair co-own with named sub-ownerships.

**Call.** None of the three. Brandon, as CEO, owns people and training for now. When Sŏn opens another location and the house must sustain itself, ownership moves into the house, and this decision is reopened.

**Reasoning.** The panel's one hard requirement was that the module system, the sign-off roster, and the talent blocks sit in exactly one place (Organizational Systems Architect). Founder ownership meets that during the founding phase, and it matches the intake: Brandon approves every module (group 6) and every gate override goes to him (group 4).

**What it changes.**
- Brandon owns the module system, module approval, the assessor roster, and gate overrides.
- How the Operations Manager and Maître d' split everything else is not decided here. Management titles stay `people.*` bindings.
- Trigger to reopen: a second location, or Brandon handing training to the house.

### D2. What unlocks the next module (question 2)

**Decided 2026-09-28.**

**Options on the table.** (a) Time in role, automatic. (b) Demonstrated mastery on the prerequisite. (c) Time as a floor under a mastery gate.

**Call.** A combination, set per module. Some modules unlock on time, some on progress or mastery.

**Reasoning.** One rule does not fit every branch. Some content is safe to open on a schedule; some reaches the customer and needs evidence first. The research and panel agree on one boundary: nothing lights on time alone where the skill will reach a customer unassessed, because the gates Brandon set (a spoken check and a practical before any customer contact, intake group 4) already require evidence there.

**What it changes.**
- Each module declares its unlock rule at design: time, mastery, or both.
- Any time period is a `fact.*` or `workflow.*` binding, never written as fact.
- `framework/module-spec.md` carries an `unlock` field in the `program` block (approved 2026-09-28).

### D3. Trunk and branches (question 3)

**Decided 2026-09-28.**

**Options on the table.** (a) A ladder that shows altitude. (b) Strands of equal standing. (c) The activity tree, choosing the view later.

**Call.** Branches. Core training modules everyone takes are the trunk. Everything else is endless branches, growing in different directions.

**Reasoning.** This keeps the white paper's "connections, not altitude" and Brandon's skill-tree picture (intake group 2) in one shape. The role paths Brandon named (food runner to back waiter to front server; barback to bartender; host into either team) are routes along branches, not rungs. Research supports it: adjacent-role chaining carries most of the benefit of cross-training, and rank displays can backfire.

**What it changes.**
- The program map is a trunk (the shared core) with branches, not a ladder. The map shows direction and adjacency, never height.
- A person's position on the map stays private (Learner Advocate).
- Leads (question 4) are read as a branch of their own role, not a top rung, unless decided otherwise.

### D4. Brand-surface rules and internal training (questions 21 and 22)

**Decided 2026-09-28, in part.**

**The conflict.** The Brand and Experiential Guidelines prohibit AI-generated imagery at one level of their authority hierarchy, and forbid glossing Korean terms on brand surfaces.

**Call.** Those rules govern brand surfaces. They do not concern internal documents and training.

**Reasoning.** Brandon's ruling: brand-surface rules are about how Sŏn presents itself to customers and the public, not how the team learns.

**What it changes.**
- AI presenters are allowed in internal training, modeled on the founders and on templates (intake group 5). Likeness consent for anyone else goes through HR. An AI presenter models; it never replaces rehearsal with feedback.
- Question 22 (teaching the Korean terms) was decided separately: see D23.

### D5. Leads, and whether a lead signs alone (question 4)

**Decided 2026-09-28.**

**Options on the table.** (a) Leads co-rate; a manager holds every decision. (b) Leads sign alone after calibration and co-rated audits, inside scheduled paid time, with no authority over discipline or pay. (c) A separate paid certified-trainer position.

**Call.** (b).

**Reasoning.** It is the peer-led practical Brandon described (intake group 4), with the same bootstrap: a peer plus a manager until leads have completed their teaching and assessing training, then leads alone. Co-rated audits are what keep a lead's release trustworthy (Assessment & Competency Designer). Read with D3, a lead is a paid branch of their own role, not a rung above it, which reconciles the intake's promotable position with the white paper's "not permanent elevations."

**What it changes.**
- Leads are paid, promotable positions that can sign a practical alone once calibrated and audited.
- Calibration and audit sit in the teaching and assessing track (LEA modules).
- Assessing happens in scheduled paid time, outside service windows (Hospitality Operations Realist).
- Leads hold no authority over discipline or pay, and titles never imply it (Organizational Systems Architect).
- Open, not a training call: whether rating a practical counts as managing for an hourly employee. Routed to the HR seats before any lead signs alone.

### D6. What is paid in learning (question 5, earning line)

**Decided 2026-09-28, in principle.**

**Options on the table.** (a) Pay per module completed, as the white paper words it. (b) Pay for demonstrated mastery and teaching; completion earns feedback, not pay. (c) (b) plus pay for authoring modules.

**Call.** Mastery, teaching, and authoring are what earn. The type, amount, and timing are not set now. Brandon, in his words: "we'll have to look at everything holistically and decide: what's the pay scale, what's the rate change, what amount of work equates to how much money we think that knowledge is worth over the year."

**Reasoning.** Completion pay rewards the click-through Brandon distrusts (intake group 7), and the research finds expected, completion-contingent rewards undermine intrinsic motivation. Valuing knowledge in money needs the whole system in view first.

**What it changes.**
- Every module, gate, teaching role, and authoring role that could earn is flagged as it is built, with a `founder.*` binding for the pay rule and `fact.*` for any amount. Nothing is written as fact.
- Learning time itself stays paid (intake group 3).
- A holistic pay review comes once enough of the system is built. Tracked in ClickUp.

### D7. Take-home practice (question 5, take-home)

**Decided 2026-09-28.**

**Options on the table.** (a) Take-home kits with a paid practice allowance and a check-in. (b) All drills on site and paid. (c) Unpaid optional practice.

**Call.** Take-home practice is offered, optional, and unpaid, never mandatory, and only in a form that is fully compliant. It is presented as an invitation: take this home if you want to get better at it.

**Reasoning.** Home practice cannot be tracked, and Brandon will not pay for learning he cannot verify. Screen-based remote learning can be tracked, so it stays paid (intake group 3). People who want to practice will, if it is presented well.

**What it changes.**
- Any take-home kit is framed as optional and invited, never assigned.
- To stay compliant it cannot be required in effect: no gate, unlock, schedule, or evaluation may depend on having done it. Required practice happens on site and is paid.
- Before any kit ships, the HR seats confirm the framing is compliant (voluntary, not a condition of the job). Tracked in ClickUp.

### D8. How a gate is recorded (question 6)

**Decided 2026-09-28.**

**Options on the table.** (a) An Admin marks the gate complete in Trainual. (b) An external form records the gate, the rater, and the rubric; automation marks Trainual and opens the next module. (c) A learner-kept, co-signed practice record.

**Call.** (b).

**Reasoning.** Trainual has no assessor sign-off and an Admin mark does not name the rater, so rater consistency cannot be audited (Assessment & Competency Designer). A form names every rater and holds the anchored ratings the research says a reliable gate needs.

**What it changes.**
- The gate record lives in a form tool: `tool.forms.gate_record`, bound until the tool is chosen.
- Automation is required, not optional: the Admin step is automated away (Organizational Systems Architect).
- Records and map updates happen at close, never on a device during service (Hospitality Operations Realist).
- `adapters/trainual.md` corrected (approved 2026-09-28): e-signature records only the signer's own acknowledgement, and option 4 is marked as the decided gate record.

### D9. The prove-it shift (question 7)

**Decided 2026-09-28.**

**Options on the table.** (a) Live team feedback throughout the night. (b) Private feedback collected at close. (c) The team watches in shift and speaks at close.

**Call.** None of the three as framed. The final gate shift is not a staged pressure test. It is the guardrails coming off: the learner steps into the real environment, and the team participates as it always does. Feedback flows the way it flows every night. Every piece of it does not have to be documented. Part of the point is that the team around the new person comes to feel good about them joining.

**Reasoning.** Brandon's aim is a house where everyone gives everyone feedback constantly (intake group 4). Until this shift the learner has been shielded from that environment; the last step is joining it, not being judged by it.

**What it changes.**
- The panel's concern stands as a design requirement, not a veto: this shift only works if the everyday critique culture already exists and is safe. The culture modules (open critique, how to give and take feedback across levels) sit in the trunk, ahead of any gate shift.
- The gate decision itself still rests on the gate record (D8), not on a team vote.
- TBRI reviews how this shift is introduced to the learner.

### D10. Release evidence (question 8)

**Decided 2026-09-28.**

**Options on the table.** (a) One angel shift and one eyes-off shift. (b) The angel shift, then a window of eyes-off shifts until one more would not change the call. (c) (b), plus the condition that a skill counts for coverage only once its live gates ran on a real, full night, with periodic rechecks.

**Call.** (c).

**Reasoning.** One observed shift is under-sampled; trust decisions draw on several occasions (Assessment & Competency Designer, Learner Advocate, program-structures research). A skill proven only on a quiet night has not been proven at tempo (Hospitality Operations Realist).

**What it changes.**
- Release follows a window of eyes-off shifts, not a single shift. The window closes when another shift would not change the call, recorded on the gate form (D8).
- A released skill counts toward coverage and the on deck reserve only after a real, full night. What counts as full is a `workflow.*` binding.
- Rechecks run on `workflow.recheck_cadence`.
- Released reads "released, reads still maturing" for the hospitality layer, which keeps growing with volume (Hospitality Craft Educator).

### D11. Fail limit and retries (question 9)

**Decided 2026-09-28, shape only.** The numbers are team-gated.

**Options on the table.** (a) A fixed number of attempts, then coaching. (b) No attempt count: a required interval between attempts and a changed practice plan; repeated misses trigger a conversation about fit. (c) Leave the shape to the team.

**Call.** (b).

**Reasoning.** Spacing research favors an interval between attempts, and a check framed as a verdict on ability raises threat for little gain. Brandon's "there will certainly be a fail limit" (intake group 4) is met by the fit conversation that repeated misses trigger.

**What it changes.**
- No attempt counter. Each miss sets a required interval and a changed practice plan.
- Repeated misses trigger an unblock conversation about fit, auto-scheduled like any other (question 11).
- Safety elements pass in every attempt. Movement drills may be banked; the integrated practical may not (Assessment & Competency Designer).
- The interval, what counts as repeated, and each gate's cut score are set with the hired leaders: `workflow.*` and `fact.*` bindings, team-gated.

### D12. Showing the skill tree (question 10)

**Decided 2026-09-28.**

**Options on the table.** (a) An external live page reading Trainual progress through the API. (b) A static map in Trainual plus a printed wall map. (c) A SCORM map inside Trainual.

**Call.** (a) with (b): a live personal page, plus a static map in Trainual and on the back-of-house wall that shows the structure only.

**Reasoning.** Trainual shows lists and locks content only in a straight line, so the trunk and branches must be presented outside it to be "presented as much as possible" (intake group 2). Individual position stays private (Learner Advocate); visible rankings can backfire.

**What it changes.**
- The live page needs Trainual API access, which may need a higher plan: `tool.lms.api_access`, a founder call at bind time.
- The wall map and the Trainual map show the tree, never anyone's place on it.
- Streaks and leaderboards stay off unless Brandon turns them on (`tool.lms.gamification_setting`).
- Map updates happen at close (Hospitality Operations Realist).

### D13. Self-scheduling practicals and unblock conversations (question 11)

**Decided 2026-09-28.**

**Options on the table.** (a) The learner gets a booking link when a module is finished. (b) Nobody books: automation books the first open talent-block slot. (c) Trainual's "Request" access.

**Call.** (a). Finishing a module sends the learner a single-use link to book a slot on a leader's talent block.

**Reasoning.** The learner never has to ask anyone for a practical or a conversation; the link simply arrives (intake group 2). A booking link is simpler to build and run than fully automatic booking.

**What it changes.**
- Completion triggers the link; the talent blocks are the only bookable slots. `workflow.gate_autoschedule`, `workflow.talent_block`, `tool.scheduling.platform`, all bound.
- The Organizational Systems Architect's caution stands as a known tradeoff: any step that waits on a person's action is where advancement can stall. An unbooked link resurfaces as a reminder rather than expiring silently (`workflow.unbooked_link_reminder`). Moving to automatic booking later is a change to the automation, not to the design.
- Every conversation ends in one of four recorded outcomes (LEA-006).

### D14. Measuring decision alignment and complacency (question 12)

**Decided 2026-09-28.**

**Options on the table.** (a) Agreement with a reference panel on judgment scenarios. (b) Behavior-level evidence: floor observation and success-case interviews. (c) A watchlist of positive and complacency signals.

**Call.** All three.

**Reasoning.** Brandon's measure is people making the decisions he would make (intake group 7). Scenario agreement tracks alignment, floor evidence is what the `measured` stage requires, and the watchlist catches the complacency and mere participation he distrusts.

**What it changes.**
- Scenario agreement: Brandon anchors a reference panel built per judgment, with minority views kept (Hospitality Craft Educator). It is a learning and alignment measure and never gates advancement until calibrated leads join the panel (Assessment & Competency Designer). The measurement item bank is separate from the practice bank (Practice and Simulation Designer). Source content comes from the founder decision-making interviews.
- Floor evidence runs in the weekly-meeting window after each launch (intake group 7; `workflow.post_launch_review_window`).
- Watchlist signals are prompts to look, never targets or marks against a person. "The same few voices" prompts a look for concealment, not a judgment of the quiet (Learner Advocate).

### D15. Module length (question 13)

**Decided 2026-09-28.**

**Options on the table.** (a) One objective and one learning job per critical-path unit, no time target. (b) Time caps per unit. (c) (a) plus a required spaced-recall schedule tied to the learner's next shifts.

**Call.** (c).

**Reasoning.** Efficacy drives length (intake group 3). The gains credited to short modules come from spacing, retrieval, and learner-paced segmenting, not shortness itself, and a time cap would be a figure.

**What it changes.**
- Each critical-path unit teaches one objective with one learning job, and carries a recall schedule anchored to the learner's next shifts (cap the longest gap rather than chase an interval).
- Off-path long-form (masterclass recordings, reading tracks) is unrestricted.
- Interleave near-miss visual discriminations; keep menu facts, specs, and scripts blocked (Instructional Designer, Practice and Simulation Designer).
- Pre-shift format and timing, where much retrieval lives, stay team-gated.

### D16. Keeping modules current (question 14)

**Decided 2026-09-28.**

**Options on the table.** (a) Date-based reminders only. (b) Volatility tags from bindings, with change events triggering review. (c) Both.

**Call.** (c).

**Reasoning.** Brandon asked for date reminders, pre-launch tags on what could change, and learner flags (intake group 6). Dates alone are blind to what actually changed; the bindings already mark volatile content.

**What it changes.**
- ClickUp review reminders by creation date.
- Volatility tags derived at `drafted` from binding namespaces: `tool.*` and `fact.*` high, `workflow.*` and `chef.*` medium, durable content low.
- When a tool, workflow, or figure changes, every dependent module is flagged through the bindings registry.
- Learner flags: a form on each module's closing page creates a review task (`tool.forms.content_flag`, `workflow.flag_to_review_task`). Trainual's native flag is not a reliable automation trigger.

### D17. Outside compliance content (question 15)

**Decided 2026-09-28.**

**Options on the table.** (a) Trainual's add-on course library for what it covers. (b) An outside provider by link, with the certificate uploaded and verified. (c) A provider's SCORM package where Sŏn holds the rights.

**Call.** All three, each where it fits.

**Reasoning.** Sŏn does not write its own versions of certified or compliance content (intake group 1; standing rules, "Scope"). The add-on library covers topics such as harassment prevention and workplace safety; no food handler or alcohol-service course was confirmed in it, so those come from outside providers.

**What it changes.**
- Compliance items are catalog rows of type `linked`, with no durable content.
- Each required certification is mapped to its source: add-on, provider link (certificate uploaded, an Admin verifies), or provider SCORM where rights allow.
- Costs are `fact.*` bindings. Tracked in ClickUp under the external certifications review.

### D18. Lifecycle and review panels (question 16)

**Decided 2026-09-28: moderate changes.** Edits to `framework/lifecycle.md` and `framework/review-panels.md` approved and made the same day.

**Options on the table.** (A) Minimal: new catalog types only. (B) Moderate: (A) plus new exit criteria and panel rules. (C) (B) plus a `calibrated` checkpoint before any assessor release.

**Call.** (B).

**Reasoning.** The gate, measurement, and upkeep decisions above only hold if the lifecycle checks for them. A `calibrated` checkpoint is premature before any lead exists; D5 already requires calibration and audits before a lead signs alone.

**What it changes.**
- New catalog row types: `linked` (compliance, skips design and drafting), `library` (reading and listening tracks, finished by a proven conversation, light panel), `gate-spec` (per-skill gate criteria).
- `designed`: any module that feeds a gate carries a gate spec, signed by the Assessment & Competency Designer.
- `drafted`: volatility tags (D16) and a recall schedule (D15) present.
- `reviewed`: a novice-attempt test for every critical-path module, once receiving-end learners exist (elicitation-gated).
- Between `published` and `measured`: the post-launch review window (D14).
- Panels: TBRI on every module with team feedback or role-play; the Organizational Systems Architect only on modules that change the tree, unlock rules, or role definitions; any scenario module keeps separate practice, gate, and measurement item banks.
- The authoring template's instructional soundness becomes a deliverable owned by the Instructional Designer.

### D19. The opening bootstrap (question 17)

**Decided 2026-09-28.** Pre-opening itself stays deferred; this names how the first cohorts are assessed.

**Options on the table.** (a) Founders and managers run every practical for the first cohorts, capped. (b) Certify assessors before opening. (c) Hire experienced leads and calibrate them.

**Call.** A combination. Founders and managers assess the first cohorts. Assessors are identified and trained soon after opening, with at least one or two trained within the first few months.

**Reasoning.** No calibrated lead exists at opening, and by Brandon's own rule (intake group 4) every practical needs a manager present until one does. Training assessors on a live floor is faster and more real than mock services before opening.

**What it changes.**
- The first cohorts' practicals and gate shifts are run by founders and managers, with a cap on live gates per service (`workflow.live_gate_limit`) so green crews are not overloaded (Hospitality Operations Realist).
- The teaching and assessing track (LEA) is on the early build list, so assessors can be trained soon after opening. The timeline is `workflow.first_assessor_timeline`.
- The first cohort's struggle points are logged: the sequence is a hypothesis until then (Curriculum & Program Architect).

### D20. Who holds the door (question 18)

**Decided 2026-09-28.**

**The conflict.** The white paper gives the door to the Lead Host and frees the Maître d' from it. The brand guidelines have no host stand and the Maître d' receiving each customer at the top of the steps.

**Call.** Responsibility and presence are split. The Maître d' holds responsibility for everything, the door included. During service the Maître d' delegates the door, and some tasks, to the host team, and they fall to the lead host. In physical presence through service, the lead host holds the door and the Maître d' holds the room. The lead host sits a step below the Maître d'.

**Reasoning.** Brandon's ruling, reconciling the two sources: ownership stays with the Maître d'; the door is delegated work.

**What it changes.**
- Host-branch modules (door, arrival, pacing the room from the book) are the lead host's and host team's craft, taught as delegated work inside the Maître d''s responsibility.
- Maître d' modules cover owning the room and delegating the door, including when to step in.
- The Brand and Experiential Guidelines' arrival choreography describes the Maître d' at the threshold. Aligning that canon text to this decision is Brandon's edit to make, not the studio's; until then, modules cite this decision and bind specifics with `brand.*`.

### D21. Mentor and angel-shift trainer (question 19)

**Decided 2026-09-28.**

**Options on the table.** (a) One person: the angel-shift trainer is the mentor. (b) Two people: an assessor runs the angel shift, a separate cultural-steward mentor holds the relationship. (c) (b), with the mentor also the named contact on reserve shifts.

**Call.** (a). One person.

**Reasoning.** One relationship per new hire, and one person who knows how they are progressing. Simpler to staff in a small house.

**What it changes.**
- The angel-shift trainer is the new hire's mentor through their path. The white paper's mentor role (WP Part II, onboarding) is carried by this person.
- The known tension, named so it is designed for: the same person both advocates for the learner and judges readiness. The release decision rests on the gate record and its audits (D8, D10), not on the mentor alone, and a second rater joins any gate the mentor rates.
- The trailing this person runs is specified: what they say aloud, how they model then coach, when support fades (Hospitality Craft Educator).
- What makes someone a good mentor (the white paper's cultural steward) is Brandon's to set: `founder.mentor_criteria`.

### D22. Critique rituals and pre-shift teaching (question 20)

**Decided 2026-09-28.**

**Options on the table.** (a) Two rituals: private, process-focused incident review and open, task-focused everyday feedback. (b) One open ritual for both. (c) (a), plus pre-shift teaching rotated to any rank.

**Call.** (c).

**Reasoning.** The white paper's private, process-focused review (WP Part II) and Brandon's open, cross-level critique (intake group 4) do different jobs. Feedback aimed at the person rather than the task reduces performance, and speaking up does not cost everyone the same, so both need a taught protocol. Rotating who teaches at pre-shift spreads teaching as a transmission method (Hospitality Craft Educator).

**What it changes.**
- Two rituals, designed so neither is mistaken for the other: private incident review (LEA module) and open everyday feedback (culture module in the trunk).
- Cross-level critique is practiced at low stakes before it is aimed at anyone on a gate shift (Learner Advocate). TBRI and the Culture seats review both.
- Pre-shift stays led by the Maître d', the operations manager, or the lead host (intake group 5); the teaching slot inside it rotates to any rank. Rotation never counts toward progression, as Brandon set (intake group 5).

### D23. Teaching the Korean terms (question 22)

**Decided 2026-09-28.**

**Options on the table.** (a) Training explains the terms in full. (b) Training teaches through cases without a gloss. (c) A founder-written internal glossary that is itself canon.

**Call.** (c). Brandon writes an internal glossary of the Korean terms and persona labels, and training uses it.

**Reasoning.** Brand surfaces keep the no-gloss rule (Brand and Experiential Guidelines, Hangul deployment). Inside, the team needs the meaning, and the meaning is Brandon's to set, not the studio's to infer.

**What it changes.**
- Until the glossary exists, modules cite the term and bind its explanation: `founder.glossary.<term>`.
- The glossary is internal canon. Where it lives is Brandon's call (Box, per the source rule). Tracked in ClickUp.

### D24. Daypart scope (question 23)

**Decided 2026-09-28.**

**Options on the table.** (a) Dinner and late night first, later dayparts as new branches. (b) All dayparts now. (c) Dinner only first.

**Call.** (b). Training covers every daypart's register from the start.

**Reasoning.** Brandon's call. The brand guidelines describe one behavioral logic across all dayparts with distinct registers, and the program is built as ongoing training, not only for the opening menu of services.

**What it changes.**
- Service and beverage branches carry each daypart's register, including the pyeong-sang protocol and late night, where canon defines them.
- Daypart names on any surface follow the standing rule: no internal daypart code names, and Sŏn is never a daypart name. Modules use plain descriptors.
- Which dayparts actually run at opening, and when, stays a `workflow.*` binding; content for a daypart not yet running is built and parked.
- Whether each daypart is its own team or one team (Organizational Systems Architect) is not decided here.

### D25. Service recovery (question 24)

**Decided 2026-09-28.**

**Options on the table.** (a) Bounded: a known range and named escalation triggers, set before service. (b) Bounded by role: a wider range for the Maître d', a narrower one for the floor. (c) Open: whatever it takes, reviewed after.

**Call.** (b).

**Reasoning.** Pre-authorized discretion inside known limits (Brand and Experiential Guidelines, floor authority) lets people act without asking, and matching the range to the role keeps the generous end with the person who holds the room.

**What it changes.**
- Recovery modules teach each role its range and its escalation triggers. Every range and threshold is a `fact.*` binding from Airtable; who holds each range is `people.*`.
- The durable craft is how to recover (match the make-good to the kind of loss, how the person is treated, closing the loop), not the amounts (Hospitality Craft Educator).
- A pre-authorized gesture needs a named owner and the slack to carry it out on a full night (`workflow.recovery_owner`); the module teaches what to do when no one is free (Hospitality Operations Realist).
- The food side of any recovery is chef-gated.

### D26. Canonical brand guidelines copy (question 25)

**Decided 2026-09-28.**

**Call.** The June v3.0 PDF in Box (file `2281626080747`) is canonical. The July markdown copy (`2356731001214`) is a supplement for text extraction only; where the two differ, the PDF wins.

**What it changes.** Nothing in the pointers: `canon/pointers.md` and CLAUDE.md already name the PDF. Brandon's source rule (internal sources from Box, never ClickUp documents) stands.

### D27. Outside course libraries must live inside Trainual (Barista Hustle)

**Decided 2026-09-28.**

**Context.** Barista Hustle is the leading coffee training source and a candidate for linked beverage content (`research/phase2-working/10-barista-hustle.md`). As researched, its courses run on its own site, courses cannot be assigned per person, progress stays with the individual, no SCORM or LMS connection was found, and its terms forbid re-hosting content without written permission.

**Call.** Sŏn uses an outside library's modules only if they can be used and tracked inside Trainual. No external teaching tool. A Barista Hustle certificate may count as prior learning toward a Sŏn skill (open, not required); it never replaces Sŏn's own practical. No preference yet on adapting its scoresheets.

**What it changes.**
- Barista Hustle stays a candidate, not a source, until it confirms a way to deliver and track inside Trainual (SCORM, an LMS integration, or written permission to host). Tracked in ClickUp as a question to put to Barista Hustle.
- Until then, the beverage branch is built in Sŏn's own content, in Barista Hustle's spirit where useful (measurable drills, a named movement vocabulary, scoresheets that open with the learner stating their plan).
- The same test applies to any outside course library: usable and tracked inside Trainual, or not used. Linked certifications (D17) are the exception only where a legal certificate must come from an outside provider; the certificate is still uploaded and tracked in Trainual.
