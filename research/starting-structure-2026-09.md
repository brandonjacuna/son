# Sŏn module system: a starting structure

**Date:** 2026-09-28
**What this is:** a proposal for Brandon to decide from in Phase 3. Nothing here is a decision. Every ID, title, sequence and gate is a candidate until `/identify` and `/ideate` confirm it, and every decision lands in `framework/system-design.md`, not here.
**Inputs:** the intake (`research/intake-2026-09.md`, verbatim answers of 2026-09-27 to 28); the internal read of the white paper and the brand guidelines in Box; external research on program structures, learning evidence, and the Trainual and scheduling platforms; the reading list read; and a panel read by eight seats.
**Caveat on the panel:** the Hospitality Craft Educator and the Practice and Simulation Designer seats are unvalidated (synthesis stage 6 skipped, and stage 7 too for the Practice Designer). Their reads are carried in full and marked. The other six seats are validated.
**Canon, cited and never restated.** White paper: Box `2466517057642`, "Sŏn Investor White Paper Sept 2026.pdf", in 02. Capital Raise / 00. Pitch Materials / White Paper (labeled WP below, cited by part, section label and page). Brand and Experiential Guidelines: Box `2281626080747`, the v3.0 PDF in 10. AI Projects / Design (labeled BG, cited by section number and label). A newer Markdown copy, `2356731001214`, is labeled BG-md and used only as a supplement. Which copies are canonical is an open question (question 25).
**Standing flags.** Every role title is a `people.*` binding until the naming session held open in WP Part I, "Open items" (p.15). Every figure is a `fact.*` binding. Coqodaq, Alinea, Gracious and Achatz are lineage: flagged for Brandon, never reconstructed.

---

## One-screen summary

**The proposed shape.**
- One activity tree, not a job ladder. Nodes are things a person can do alone ("run food to a table", "hold a small table alone", "work the bar well alone"). A role is a bundle of nodes. This lets one map hold both the ladder Brandon described and the strands the white paper describes until Brandon chooses.
- A shared core for every hire (why before how, the map, how decisions get made, using support, pre-shift, critique, care as craft, allergy routing, linked certifications), then three front-of-house branches: service (runner, back waiter, front server), beverage (barback, then one bartender-and-barista team on a shared liquid-craft spine), and host as the bridge between the two. Management and leads share one teaching-and-assessing path. Back of house is a chef-gated shell with no IDs.
- Gates sit per node, and the first two happen before any customer contact: a spoken knowledge check, a small-menu practical, the angel shift under direct observation, then a window of eyes-off shifts with support on request. A node lights only on evidence, never on completion.
- Assessors are trained before they sign: teaching, calibration, running the angel shift. Peer plus manager until a lead is calibrated and audited.
- Reading and listening tracks live in a separate library prefix, off the critical path, finished by a proven conversation.
- Job descriptions, the tree view and the interview transparency sheet all render from one role manifest.

**The calls Brandon most needs to make, in the order they shape the rest.**
1. Who owns people and training: the Maître d' (as the white paper says) or the operations role (as the intake says). This decides who owns the module system, the sign-off roster and the talent blocks.
2. What unlocks the next node: time in role, demonstrated mastery, or time as a floor under a mastery gate. The white paper and the intake disagree.
3. Strands of equal standing or a ladder. This decides whether the map shows adjacency or altitude.
4. Whether leads are paid promotable positions or per-shift designations, and (with HR) whether an hourly lead may sign a practical alone.
5. What "the more modules completed, the more earned" means. The evidence is against paying for completion and for paying for demonstrated mastery and teaching.
6. Where a passed gate is recorded and who may record it, because Trainual has no assessor sign-off.
7. How team feedback on the prove-it shift is timed and framed: in the moment, as the intake says, or collected at close and delivered privately, as the panel argues.

---

## 1. Proposed program map

### 1.0 Program outcomes

The Curriculum and Program Architect is right that the draft started from a module list rather than an end state. The terminal transfer goals below come first; every node's transfer goal must trace to one of them. Each is a hypothesis to test with the first cohort.

| Outcome | Written as an autonomous performance |
|---|---|
| House-wide decision alignment | On their own, a team member reads a situation the way the house's reference panel would, chooses the move the panel would rank first, and can say why. The panel is anchored by Brandon and is not only Brandon (question 12). Source: intake group 7. |
| Service branch | On their own, a front server owns the table relationship end to end (WP Part I, p.8 and p.13; BG 15, "Floor authority"), reads the table before a cue becomes a request, and recovers inside the authorized range. |
| Beverage branch | On their own, a bartender or barista builds any house drink to spec at tempo, adjusts it when conditions drift because they hold the why, and describes it honestly. |
| Host branch | On their own, a host paces the room from the book so the kitchen and floor never fall behind the door, and receives each customer inside the arrival choreography (BG 13, "Threshold"; BG 15, "Arrival choreography"). |
| Assessor and lead thread | On their own, a calibrated lead runs an angel shift, rates a practical on anchored criteria that agree with a second rater, and turns last night into teaching. |
| Internal succession | Over time, the building fills leadership from within (WP Part II, "Performance management", p.19). |

The Craft Educator adds one outcome the draft missed: every front-of-house hire can name the difference between service (checkable standards) and hospitality (reading this customer) and knows which layer they are working in. That objective is added to ORI-001.

### 1.1 Domains

The prefixes in `framework/module-spec.md` are kept: ORI, SVC, BEV, KIT, SAF, SYS, LEA, CUL. The host track sits in SVC.

One new prefix is proposed: **LIB**, the library (reading, listening, masterclass). The reading tracks are finished by a proven conversation, never gate the floor, and run long by design (intake group 3). Filing them under CUL or ORI would hide them inside required content and put the wrong panel on them. The CPA supports the prefix on one condition, adopted here: every LIB track maps to at least one node or one enduring understanding, or LIB becomes a pile. The cheaper alternative, a `track: library` tag inside CUL, loses the "never critical path" signal.

No new prefix for movement drills. Drills stay in their craft domain with a `job: do-drill` tag, so the split between movement and decision is visible without cutting a craft in two.

### 1.2 Structure: an activity tree

**Nodes are activities, not titles.** This follows the entrustable-activities model in medicine and the supervised-operating-experience rule in aviation (program structures B1, B2), both verified-primary. A role is a bundle of nodes.

**Ownership of the table below, per the panel's request:** sequence and prerequisites belong to the Curriculum and Program Architect; node structure, levels and reserve rules belong to the Organizational Systems Architect; readiness under tempo belongs to the Hospitality Operations Realist; gate validity belongs to the Assessment and Competency Designer.

**Node states.**

| State | Meaning | Owner |
|---|---|---|
| locked | Not yet available. | OSA |
| open | Available to start. | OSA |
| in practice | Being worked on. | CPA |
| released | Lit by evidence: a passed gate or a logged proven conversation. On hospitality-layer nodes it reads "released, reads still maturing" (Craft Educator). | Assessment |
| recheck due | Released, and due for a recheck. Framed as a house rhythm, never as suspicion (Learner Advocate). | Assessment, Realist |

A node never lights because content was completed (program structures F1 to F3; learning evidence §7). A "not yet" never displays as a failure state on a node.

**Supervision levels, per node.** Revised after the OSA: these are supervision levels on a node, not ranks, and the assessor level is a separate thread.

| Level | Meaning |
|---|---|
| L1 | Observe only. |
| L2 | Direct supervision: the trainer personally observes. The angel shift. |
| L3 | Indirect supervision: help on request. The eyes-off shifts. |
| L4 | Released on this node. |
| Assessor thread (was L5) | May assess and sign practicals on this node. Reached only through the LEA assessor path plus co-rated audits. The word "supervise" is dropped because it gives hourly leads managerial authority by wording (question 4). |

### 1.3 Shared core

Every front-of-house and beverage hire, and every host, takes the core. Everything on it is Introduce level and lean: one objective and one learning job per unit (learning evidence §1).

| Order | Module | Why here |
|---|---|---|
| 1 | ORI-001 Why before how | The reason before the mechanics (WP Part II, "Onboarding", p.18; program structures A6). |
| 2 | ORI-002 Your map | How progression, the reserve and the unblock conversation work. |
| 3 | SAF-002 Linked certifications and compliance | Enrolment in outside certifications starts early because they run on their own clock. |
| 4 | SAF-001 Taking an allergy at the table | The safety floor. Non-compensatory in every gate (Assessment). |
| 5 | ORI-003 How decisions get made here | The decision frame that SVC-007 and BEV-009 build on. |
| 6 | ORI-004 Using the support system | Asking is an assessable behavior, not a trait (Assessment, Learner Advocate). |
| 7 | CUL-003 Care as craft, and its cost | Care is labor with a cost, not a temperament (reading list §1.1). |
| 8 | CUL-001 Taking part in pre-shift | Where spaced retrieval lives. |
| 9 | CUL-002 Giving and receiving critique across roles | Practiced at low stakes long before it is aimed at anyone on a gate shift (Learner Advocate). |

Revised: ORI-005 "How flavor works" leaves the core. The CPA found no critical-path node depends on it and the Instructional Designer found it adds know-level load before any floor task needs it. It becomes the Introduce slot shared by SVC-008 and BEV-008.

The remote block delivers only the know-it and see-it pieces of the core, with retrieval returns scheduled into the first on-site sessions and first shifts, and short conversations between screen pieces (intake group 5; Instructional Designer). Nothing that needs correction ships screen-only. The block assumes second-language and low-literacy learners are present and concealing, so comprehension checks never require a learner to confess they could not read something (Learner Advocate).

### 1.4 Branches

**Service branch: food runner, then back waiter, then front server.** Front server and front waiter are one role (intake, group 1 confirmation).
- Runner: the handoff, the path, the carry.
- Back waiter: pour, clear and reset, supporting the section.
- Front server: reading the table, describing, pacing, owning the table relationship.
- Runner and back waiter may be hybrid stations depending on volume (intake group 1). The nodes are shared; only the station assignment is a `workflow.*` binding.
- Revised after the Craft Educator: the pyeong-sang protocol (BG 15, "Key protocols") is a pre-designed choreography and is drilled; dining-room entry and pacing are perceptual and are practiced as judgment, never scored on elapsed time. The step-back model (BG 15, "Step-back architecture · three phases") is triggered by attunement, not by a clock.

**Beverage branch: barback, then one bartender-and-barista team.**
- One liquid-craft spine (BEV-001): temperature, dilution, texture, extraction, pour control, economy of motion (reading list §4).
- Two specialty nodes hang off it: espresso and milk; bar build on the root-and-family grammar of *Cocktail Codex*.
- A bartender or barista opens the other specialty over time. That is an in-branch unlock, not cross-training. This is how the intake's wish that the two roles not divide (group 1) becomes structure.
- Beverage skill is taught and assessed in three parts, recognizing, categorizing and telling, grid first and story second (Craft Educator). The wine evidence is wine only; spirits, coffee and tea are inference.
- The head of beverage owns house specs with a dotted line over the bar team (`people.head_of_beverage`). Whether bar specs are chef-gated is a founder call.

**Host branch: the bridge.**
- Own nodes: the threshold and arrival, pacing the room from the book, reading the room.
- Two adjacent unlocks: the service entry node (runner) and the beverage entry node (barback). This is the host as the link between the two chains (program structures D1; intake group 2 clarification).
- Door ownership is open (question 18). Until it is decided, most host nodes are bindings.

**Leads: lead runner, lead server, lead bartender, lead host.** The intake makes them paid and promotable; WP Part I (p.10) makes Lead Host and Station Leads per-shift designations (question 4). Reaching the assessor thread requires L4 on the home branch's core nodes, the LEA assessor path (LEA-001, LEA-002, LEA-003), and a co-rated audit period. Lead shift scope is an HR ruling.

**Management pair: the operations role and the Maître d'.** Titles are `people.*`. Revised after the OSA: the draft's "elective emphasis" is withdrawn. The split is domain ownership, and ownership of the module system, the rosters and the talent blocks sits in exactly one domain (question 1). The shared management track holds assessing (LEA-002), the unblock conversation (LEA-006), running pre-shift (LEA-005), leading by example (LEA-007), last night into the library (LEA-008), interviewer training (WP Part II, "Talent acquisition", pp.17 to 18, because they hire together), and, added after the Realist, a pre-agreed rule for who calls a live failure that spans both domains mid-service (content founder-gated).

**Back of house: a chef-gated shell.** KIT nodes are named by the executive chef. The naming conflict (steward or porter; CDC, CDP, tournant) is INT C17 and is not resolved here. The tournant is a chaining role. The porter or steward node carries tension for the whole kitchen and is never treated as a node to cut (OSA). A server learning the kitchen (WP Part II, "Training infrastructure", p.19) is a cross-branch unlock that waits on the chef. No KIT IDs are proposed.

### 1.5 Skill-tree layers

| Layer | What it holds | How it opens | What lights it | Owner |
|---|---|---|---|---|
| Shared tracks | The core (1.3) plus each branch's spine | Assigned at hire | A gate or a proven conversation | CPA |
| Specialties | Role nodes within a branch | After the prerequisite node reaches L4 | The gates in 1.7 | CPA, Assessment |
| Electives | LIB tracks; wine (linked to an external credential, program structures C1); access; the other beverage specialty | Open to all after the core; beverage electives after spine L4 | A proven conversation logged by a lead. Never a floor gate. | CPA |
| Cross-training unlocks | The adjacent node in the chain: runner to back waiter to front server; barback to bar and espresso; host to runner or barback | After L4 in the home role (intake group 2; program structures D3) plus an unblock conversation that records "learning or move" | The same gates. Proven prior experience shortens the path only after a contrast check against the house standard (Craft Educator; question 2). | OSA |
| On deck reserve | People released on a node with no open seat (intake group 2 clarification; WP Part I, "ready-now pool", p.14) | Automatic on L4 in a node outside the home role, with one condition added after the Realist: the node's live gates ran on a real, full book, not a soft night | Membership requires a home team, an orientation for every station the person may cover, a named contact on each shift, and a way to be received rather than tolerated (program structures D2). Reserve nodes carry `workflow.recheck_cadence`. Whether the reserve ranks people for succession is open (question 1 lists it). | OSA, Realist |

Adjacent-role chaining, not everyone-in-everything, gives most of the flexibility benefit (program structures D1, verified-primary theory, untested in restaurants).

### 1.6 Sequence

Revised after the CPA (an epitome first), the Instructional Designer (spaced returns, integration before the gate), the Assessment seat (a window, not one shift) and the Realist (observers extra to staffing and out of paths).

1. **Paid practical interview** (WP Part II, pp.17 to 18). Revised: kept separate from gate evidence, because a selection instrument is an employment decision (Assessment; routed to HR).
2. **Remote onboarding, paid.** Know-it and see-it pieces of the core and the branch's Introduce modules only. Length is `workflow.onboarding_remote_length`.
3. **Whole-service observation (L1).** One shift watching a full service before any drill, so the parts hang on a whole the learner has seen. The observer is extra to staffing and stays out of paths and sightlines (SVC-004).
4. **Movement drills on site,** spread across several short sessions and interleaved across drills (learning evidence §4; Instructional Designer). Take-home kits where safe (question 5).
5. **Retrieval returns** on the core, at the first on-site sessions.
6. **Integration practice.** Whole-task practice on a real or closely simulated station, with feedback, so the gate checks a combination the learner has already practiced.
7. **G1, spoken knowledge check.**
8. **G2, small-menu practical.**
9. **G3, angel shift.**
10. **G4, a window of eyes-off shifts,** ending in release (L4).
11. **Reinforce modules,** with spaced retrieval tied to the learner's next shifts, not the calendar.
12. **Master modules, electives, adjacent unlocks.**
13. **Assessor and lead path.**

### 1.7 Where the gates sit

Gates are set per node. G1 and G2 happen before any customer contact, which is the intake's "test before impact" (group 4) and the reverse of the industry norm that tests after customer contact (program structures B6, lead-only).

Three item banks are kept apart throughout: practice items, gate items, and the alignment-measure items in question 12 (Practice Designer, citing Lievens, partially verified). Any item used in practice is retired from gates.

**G1, spoken knowledge check.**
- Off the floor, after the node's Introduce modules and retrieval sets.
- Set cases, behavioral anchors on content, and either more than one calibrated rater or enough separate cases (learning evidence §5). Content is scored, never fluency; a show-don't-tell route (pointing, demonstrating) is offered so language is not scored; a private rehearsal with a peer comes first (Assessment, Learner Advocate).
- It is a knowledge prerequisite and never certifies floor readiness.

**G2, small-menu practical.**
- Off the floor or in a mock setting, after integration practice. The closest external analog is the sommelier service practical (program structures C1, verified-primary), which sits at the "shows how" level and does not predict live performance on its own.
- Movement drills may be banked as prerequisites; the integrated performance is not banked in parts; safety elements are pass-required in every attempt (Assessment; the Learner Advocate accepts this).
- Menu content is chef-gated. Recorded per question 6.

**G3, angel shift.** ("Angel shift" did not appear in documented sources and may be Brandon's own term; confirm.)
- The first live shift at L2. The trainer personally observes, the trainee is extra to scheduled staffing (`workflow.angel_shift_staffing`; program structures B1), and coaching tapers as the shift goes (program structures C6).
- Revised after the Practice Designer: a prebrief sets the container, and a structured debrief follows, using advocacy with inquiry and a chosen strategy (facilitate a judgment gap, teach a knowledge gap, self-assess only where the learner can see the gap), covering what went right as well as what went wrong. Reflection time is part of the gate (program structures B4).
- The trailing structure is specified in LEA-003: what the trainer says aloud, when support fades, exposure beyond one station (Craft Educator).

**G4, the eyes-off window.**
- Revised after the Assessment seat: not one shift but a window of L3 shifts, with observations collected until one more would not change the call, and more than one rater where stakes warrant. L4 is a forward-looking entrustment, not a pass mark.
- Using support well is assessed as an observable behavior ("asks before acting on an unfamiliar allergy call"), never as the trait "humility" (Assessment, Learner Advocate).
- **Team feedback is formative only.** Each teammate answers one shared, task-focused global question (program structures B3), collected privately, synthesized by a lead, and seen by the learner only as the lead's synthesis. Calibrated raters record their own rating before they see the synthesis (Assessment). It is never a vote and never a gate.
- The whole team is prebriefed. The learner is told in advance what will be collected, from whom, and how it reaches them. The frame is the team being there as support, not a proving (Learner Advocate).
- Timing of the collection is a genuine tradeoff between the intake and the Realist, moved to question 7.
- `workflow.live_gate_limit` caps how many live-shift gates run on one service (Realist).
- Recorded by the calibrated raters. A CEO override goes up one step to Brandon, is logged with a reason, and downstream floor performance of overridden people is tracked as a consequence signal (Assessment).

**Recheck and refresher, separated** (Assessment).
- A refresher is learning: a short retrieval and drill set in an early-arrival window (`workflow.refresher_window`) that never displaces the operational readiness brief (Realist).
- A recheck is a decision: on `workflow.recheck_cadence`, with what a miss triggers named before it runs. A short G1 plus G2 in an early-arrival window is below the "does" level and cannot revoke L4 on its own.

**Assessor release.** Frame-of-reference calibration (LEA-002), then co-rated audits as the load-bearing part, with a manager co-signing until release (learning evidence §5; program structures B4, C4).

**Management co-rater rule.** A manager co-rates, whatever the peer's level, on any gate to the customer while the peer is uncalibrated, on ratings near the cut, and where rater and candidate are close (learning evidence §5).

---

## 2. Candidate module list

**Column keys.** Slot: I = Introduce, R = Reinforce, M = Master; CP = on the critical path, kept to one objective and one learning job. Build: *now* means durable content writable today; *frame now* means the two-layer split, knowledge-kind classification and transmission plan are writable, but the cues and expert rationale wait on Brandon's decision interviews and are elicitation-gated (Craft Educator); *mostly bindings* means it parks as `identified` per `framework/bindings.md`; *hold* means the front-end check routes it out until a policy, layout or workflow exists (Instructional Designer). Form: the practice form named per module (Practice Designer): drilled rehearsal, classification drill, expert comparison, branching scenario, role-play with prebrief and debrief, or discussion.

The needs below are anticipated gaps in a house that has not opened. Each is confirmed or rejected at `/identify`.

### Shared core

| ID | Title | Need | Domain | Slot | Learners | Build | Form | Notes |
|---|---|---|---|---|---|---|---|---|
| ORI-001 | Why before how | New people learn mechanics without the reason and bend the standard under pressure | ORI | I, CP | All | now | discussion | Seed, kept (§3). Adds the service-versus-hospitality distinction and care as craft, not temperament. Cite WP Part II, "Onboarding", p.18 |
| ORI-002 | Your map: the tree, the reserve, the unblock conversation | New people cannot see how to advance and wait to be asked | ORI | I, CP | All | mostly bindings | discussion | Durable: how progression works. Bound: `founder.unlock_rule`, `tool.map.*` |
| ORI-003 | How decisions get made here | Team members escalate or freeze on calls the house would make on the spot | ORI | I, CP | All | frame now | expert comparison | Built from Critical Decision Method interviews with Brandon (learning evidence §8). Lineage incidents flagged, never written |
| ORI-004 | Using the support system | New people hide uncertainty instead of asking, most of all on early shifts | ORI | I, CP | All | now | role-play | Targets the felt risk of asking, not missing knowledge. Anchored to observable behavior for G4 |
| CUL-001 | Taking part in pre-shift | Pre-shift is treated as announcements, so retrieval and error-raising do not happen | CUL | I, CP | All | now | discussion | Seed, split (§3). Format and timing team-gated |
| CUL-002 | Giving and receiving critique across roles | People hold back from naming another role's mistake, or aim critique at the person | CUL | I, CP | All | now | role-play with prebrief, stop rule, TBRI | Model a right and a wrong way, state the rules, rehearse on cases learners bring. The teammate-reading drill has no elicited source yet |
| CUL-003 | Care as craft, and its cost | Depletion is treated as private failure and care as a trait one lacks | CUL | I, CP | All | now | discussion | Never promises to install care. Trains named moves (reappraise, take the customer's perspective, redirect attention) over several shifts. Cite WP Part II, "The cooling system" |
| SAF-001 | Taking an allergy at the table | Allergy routing depends on a server judging severity | SAF | I, CP | All FOH, BEV, host | now | branching scenario around the decision | Seed, kept. Matrix is `chef.*`. Non-compensatory at G1, shown at G2, observed at G3. Facts live in the job aid |
| SAF-002 | Linked certifications and compliance | Certified content is outside content and must be linked and tracked | SAF | I, CP | All, by role | mostly bindings | none | Never re-taught (standing rules, "Scope"). `tool.compliance.*`, `tool.lms.premium_courses` |
| ORI-005 | How flavor works | The team repeats flavor myths and describes taste as fact | ORI | I (off CP) | All FOH, BEV, host | now | classification drill | Moved off the core. Introduce slot for SVC-008 and BEV-008. "Teach" rows of reading list §2 only; Wansink never; "psychotaste" is a house label, not a field |
| CUL-004 | Receiving someone who floats in | Reserve members are treated as outsiders on a borrowed shift | CUL | R | All, leads | frame now | discussion, modeling | Mostly collective knowledge acquired inside the team (Craft Educator). Serves the reserve condition in 1.5 (program structures D2) |

### Service branch (including host)

| ID | Title | Need | Domain | Slot | Learners | Build | Form | Notes |
|---|---|---|---|---|---|---|---|---|
| SVC-001 | Getting to table-ready | Learners cannot say what ready looks like per node or which gate comes next | SVC | I, CP | Runner, back waiter, front server, host | now, after gate specs | discussion | Seed, reframed as the gate module (§3). Cannot be designed until the per-node gate spec exists (Assessment). Includes how a "not yet" is delivered |
| SVC-003 | Tray and stemware carry (drill) | New runners carry with tension and eyes on the tray | SVC | I, CP | Runner, back waiter, front server, barback | now | drilled rehearsal at varied tempo | On site under load (Realist). Precision presented as the floor, not as rehearsal (Craft Educator) |
| SVC-004 | Moving through the room (drill) | New people cross the room in ways that block sightlines and paths | SVC | I, CP | All FOH, host | hold | drilled rehearsal | Layout unsettled (BG 13, "Pre-CD open items"). Mostly collective and bodily knowledge. Cite BG 13, "Cross-zone governing principles" |
| SVC-005 | The handoff at the table | Runners hesitate at the table over who receives what | SVC | I, CP | Runner, back waiter | mostly bindings | drilled rehearsal | Pass workflow `workflow.*`; plating chef-gated |
| SVC-006 | Reading the table | Servers miss cues until they become requests | SVC | I then R | Back waiter, front server, host, bartender | frame now | classification drill | Many short varied trials with feedback; interleave the hardest-to-distinguish states; briefed stills through the Design Translating Team before opening. Placed behind the standard, the menu and pacing on each branch (CPA). Cite BG 03, "Jeong and Nunchi"; BG 05 personas calibrate, never constrain |
| SVC-007 | Service decisions: compare with the panel | On ambiguous tables, servers decide differently from the house | SVC | R then M | Back waiter, front server | frame now | expert comparison | Practice bank separate from gate and measure banks. The reveal shows what the panel noticed, not "you were wrong" (Learner Advocate). Linked to ORI-003 and BEV-009 as one decision frame |
| SVC-008 | Describing honestly | Descriptions oversell or pronounce and shape the customer's taste dishonestly | SVC | R | Front server, host, bartender, barista | frame now | discussion, recall across shifts | Shared competency with BEV-008: one node, branch-specific practice (CPA). Each item attached to a causal story; blocked, not interleaved. Menu terms chef-gated |
| SVC-002 | Recovering a mistake well | Recovery is improvised, and gestures go beyond or fall short of what the house authorizes | SVC | R | Back waiter, front server, bartender, host | now | role-play with trained peers, prebrief and debrief | Seed, narrowed (§3). Range `founder.recovery_range`, owner `workflow.recovery_owner` (Realist). Teaches what to do when nobody is free. Linked to SVC-009 |
| SVC-009 | When a customer crosses a line | Staff absorb mistreatment alone because the house response is undefined | SVC | I | All | hold, then now | role-play with prebrief, stop rule, TBRI | The need is a policy gap; instruction follows the policy (Instructional Designer). `founder.mistreatment_policy`, `workflow.escalation.mistreatment`. Reading list §1.3 |
| SVC-010 | The threshold and arrival | New hosts improvise the customer's first moments | SVC | I, CP | Host, lead host, Maître d' | mostly bindings | drilled rehearsal (task side), judgment (treatment side) | Door ownership open (question 18). Task side scripted with the people who use it and taught when to deviate; canon arrival language kept, no other required phrases (Craft Educator). Cite BG 13, "Threshold"; BG 15, "Arrival choreography" |
| SVC-011 | Pacing the room from the book | Hosts seat by availability, not by the room's pace | SVC | I then R | Host, lead host | mostly bindings | branching scenario | Strongly backed by the Realist: door pacing is an upstream cause of kitchen failure. Pacing rules are `workflow.*` and `tool.reservations.*`, not host judgment. Includes who sets protocol flags before service |
| SVC-012 | Access at the table and in the room | Staff are unsure how to serve customers with sensory or mobility needs without assumptions | SVC | R | All FOH, host | now, once sources verified | discussion | Reading list §5 access candidates |

### Beverage branch

| ID | Title | Need | Domain | Slot | Learners | Build | Form | Notes |
|---|---|---|---|---|---|---|---|---|
| BEV-001 | Liquid craft: temperature, dilution, texture, extraction | Drinks drift when conditions change because the maker lacks the why | BEV | I, CP | Barback, bartender, barista | now | discussion, recall | Shared spine. High-hazard techniques go to SAF |
| BEV-002 | Pour control (drill) | New makers pour with an unsteady stream and wasted product | BEV | I, CP | Barista, bartender, barback; servers optional | now | drilled rehearsal at varied tempo | Brandon's water-pitcher drill (intake group 5). Take-home kit with self-recorded clip against an exemplar or a peer check, never a self-rating alone (question 5) |
| BEV-003 | Station and body (drill) | Makers reach, bend and cross over, and slow under tempo | BEV | I, CP | Barback, bartender | now | drilled rehearsal | Economy of motion (reading list §4; vendor features only). Layout `workflow.bar.station_layout`, team-gated |
| BEV-004 | Milk: steam and pour (drill) | Texture and pour vary drink to drink | BEV | I, CP | Barista; bartender on unlock | now | drilled rehearsal | Isolated movements (program structures C3, lead-only). Equipment `tool.bar.equipment` |
| BEV-005 | Root drinks and their families | Makers memorize specs but cannot adjust or build a variation | BEV | I then R | Bartender; barista by analogy | now | recall, blocked | Core, balance and seasoning grammar. House specs `people.head_of_beverage`; chef-gating a founder call |
| BEV-006 | Dialing in espresso | Baristas follow a recipe and cannot correct drift | BEV | R | Barista; bartender on unlock | now | drilled rehearsal | Brandon's own batch coffee and matcha method (WP p.4) is founder- and chef-gated |
| BEV-007 | Barback flow and restock | Wells run short at peak because restock is reactive | BEV | I, CP | Barback | hold: job aid | none | Routed out by the front-end check: a par and workflow condition, a job aid after the workflow is set (Instructional Designer). The Realist keeps restock as mise on the critical path, which the job aid serves |
| BEV-008 | Tasting and describing | The beverage team pronounces rather than describes | BEV | R | Bartender, barista; servers elective | frame now | classification drill, recall | Recognizing, categorizing, telling, in that order. Retronasal technique; judge-inconsistency humility (reading list §2). Shared node with SVC-008 |
| BEV-009 | Beverage decisions: compare with the panel | Beverage calls diverge from the house reference read | BEV | R then M | Bartender, barista | frame now | expert comparison | From the decision interviews; head of beverage on the panel |
| BEV-010 | Wine (elective) | Staff who want wine have no path | BEV | M, elective | Bartender, barista, front server | mostly bindings | recommendation role-play | External credential linked (program structures C1). The credential builds knowledge; recommending needs practiced conversation and floor follow-through (Craft Educator) |

### Systems

| ID | Title | Need | Domain | Slot | Learners | Build | Form | Notes |
|---|---|---|---|---|---|---|---|---|
| SYS-001 | The tools by role | People learn the POS and other tools by trial on shift | SYS | I, CP | All, by role | hold: job aids | none | A tool procedure; parks as `identified` and becomes job aids at bind time. It is not a module on the runner's critical path (Instructional Designer) |
| SYS-002 | Using the learning system | Learners do not know how to flag content, see their map, or get a practical booked | SYS | I, CP | All | mostly bindings | none | `tool.lms.*`, `workflow.gate_autoschedule` |

### Teaching, assessing and leading

| ID | Title | Need | Domain | Slot | Learners | Build | Form | Notes |
|---|---|---|---|---|---|---|---|---|
| LEA-001 | Teaching on the floor | Peers who teach default to "watch me" and never fade support | LEA | M | Candidate leads, leads, managers | now | modeling with role-play | Seed, split (§3). Structured on-the-job training: named trainer, task breakdown, planned fading (learning evidence §3). Includes prebrief and debrief facilitation |
| LEA-002 | Assessing a practical | Anchors, standard-setting and sampling are missing, and raters reward fluency over content | LEA | M | Candidate leads, leads, managers | now | frame-of-reference calibration | Reworded after the Assessment seat: structure first, calibration as partial insurance, co-rated audits load-bearing. Prerequisite for the assessor thread |
| LEA-003 | Running the angel shift | Trainers trade observation against coverage and skip the debrief | LEA | M | Leads, managers | now | modeling, debrief strategy triage | Program structures B1, B4. Staffing bound. Specifies the trailing structure |
| LEA-004 | Writing a module | New authors skip the five moves, write tool steps as fact, and fragment the voice | LEA | M | Approved authors, founders first | now | worked examples | Unlocked by assigned request (intake group 6). Teaches the authoring template; the template itself is a separate deliverable owned by the Instructional Designer |
| LEA-005 | Running pre-shift | The teaching slot collapses into announcements when time is short | LEA | R | Leads, managers | now | modeling | Operational half `workflow.*`. One shared topic across the house per day (program structures A1). A retrieval schedule mapped to shift rhythm. Format team-gated |
| LEA-006 | The unblock conversation | Requests to learn or move stall, or end without clear expectations | LEA | R | Managers, leads | now | role-play | Ends in one of four states: elective open, adjacent unlock, reserve membership, or not now with a recorded reason visible to the learner and an automatic re-open trigger (OSA) |
| LEA-007 | Leading by example | Leaders police behaviors they do not model | LEA | M | Leads, managers | now | discussion | Reading list §1.2, including owning past harm |
| LEA-008 | Last night into the library | What the floor learns on a shift is lost | LEA | M | Leads, managers | now | structured review | Short and structured, covering what went right too (Practice Designer). Codify (reading list §3, elBulli) |
| LEA-009 | Leading your position on a shift | New leads are unsure where lead scope ends and management begins | LEA | I | Lead runner, server, bartender, host | mostly bindings | discussion | Scope is an HR ruling (question 4). Routed to the Emerging Leader Advocate |
| LEA-010 | Calling a live failure across domains | Mid-service failures that span both management domains have no pre-agreed caller | LEA | R | Managers | mostly bindings | branching scenario | Added after the Realist. Content founder-gated |

### Library (electives, never critical path)

| ID | Title | Need | Domain | Slot | Learners | Build | Form | Notes |
|---|---|---|---|---|---|---|---|---|
| LIB-001 to LIB-007 | Reading tracks T1 to T7 (care as labor; who holds the room; paths and leadership; how flavor works; designing experience; liquid craft; access) | People who want depth have no path, and no one hears what they learned | LIB | elective | All, by interest | now | discussion guide, proven conversation | Each track maps to a named node or understanding (CPA). Unverified sources are read before inclusion. T5 carries the Achatz and Alinea lineage flag |
| LIB-008 | House masterclass (listening) | Founder and partner conversations are lost to the team | LIB | elective | All | mostly bindings | listening, proven conversation | `workflow.recording_consent` (HR). Audio is untracked in Trainual (platform §6) |

### Back of house

| ID | Title | Need | Domain | Slot | Learners | Build | Form | Notes |
|---|---|---|---|---|---|---|---|---|
| KIT (shell) | Back-of-house branch | Chef-defined | KIT | chef-gated | Chef-defined | chef-gated | chef-defined | No IDs until the executive chef is engaged |

**Count:** fifty-three candidate rows carry an ID or a range (eleven core and culture, twelve service and host, ten beverage, two systems, ten teaching and leading, eight library counted as LIB-001 to LIB-008), plus the KIT shell. Four rows are held by the front-end check (SVC-004, SVC-009, BEV-007, SYS-001) and two are relabeled to job aids.

**Lean critical path by role.** Each role's path is the core, then the branch's I-slot CP drills and decisions, then G1 to G4.

| Role | Branch modules on the critical path |
|---|---|
| Runner | SVC-001, SVC-003, SVC-004 (when released from hold), SVC-005, SYS-001 job aids |
| Back waiter | adds SVC-006 and BEV-002 through the adjacent unlock |
| Barback | BEV-001, BEV-002, BEV-003, BEV-007 job aid |
| Barista | BEV-001, BEV-002, BEV-004 |
| Bartender | BEV-001, BEV-002, BEV-003, BEV-005 (I) |
| Host | SVC-001, SVC-004 (when released from hold), SVC-010, SVC-011 |

Every I-slot module on the critical path carries `### Novice` and `### Experienced` paths under `module-spec.md`, with a contrast-and-unlearn step for veterans whose prior house anticipates before the customer signals (BG 03, "This is not omotenashi") (Instructional Designer, Craft Educator).

---

## 3. What the six seed modules become

| Seed | Call | Reason |
|---|---|---|
| ORI-001 Why before how | **Keep** | Backed by WP Part II, "Onboarding" (p.18) and independently by the Cornell field study (program structures A6, verified-primary). Stays lean and on the critical path. Two objectives added: the service-versus-hospitality distinction (Craft Educator) and care as craft, not temperament (reading list §1.1), with no promise to install care. Re-cite `source` to WP Box `2466517057642`, p.18, instead of V7 through profiles (INT Q20). |
| LEA-001 Teaching at Sŏn | **Split into three** | The seed bundles three jobs with different learners and gates: teaching on the floor (LEA-001, structured on-the-job training and fading); assessing (LEA-002, anchors and calibration, the prerequisite for the assessor thread); and authoring (LEA-004, founders first, unlocked by request; intake group 6; INT C9). Trainer and assessor training is the active ingredient in every external model read (program structures B4, C4, verified-primary). The white paper's "paid to teach" line goes to question 5. |
| SVC-001 Getting to table-ready | **Keep, reframed, and sequenced behind the gate specs** | It becomes the gate module for the service and host branches: what ready looks like per node, and how to prepare for G1 and G2. The white paper says "No one touches a table until they are actually ready" (Part II, "Training infrastructure", p.19) and does not say what ready is. Revised after the Assessment seat: the seat defines ready in a per-node gate spec, and SVC-001 teaches toward it, so SVC-001 cannot be designed first. Revised after the CPA: the beverage branch gets its own stated readiness criteria rather than inheriting service criteria through `learners`. Adds how a "not yet" is delivered (Learner Advocate). |
| SVC-002 Recovering a mistake well | **Keep, narrowed** | Recovery craft is durable. The gesture range is unresolved across WP p.13, WP p.26, BG 15 and BG-md 08 (INT C11): bound as `founder.recovery_range`, with any threshold as `fact.*` and an owner as `workflow.recovery_owner` (Realist). Mistreatment by a customer moves to SVC-009, a different failure with a different owner. Practice is role-play with trained peers, prebriefed, with a debrief that draws out how the server read the failure (Practice Designer). |
| SAF-001 Taking an allergy at the table | **Keep** | The safety floor. The matrix is `chef.*`. Build the routing principle now, around the decision (the customer's aside mid-order and the pull to keep moving), with facts in the job aid. Non-compensatory in every gate: shown at G2, observed at G3, never offset by strengths elsewhere. Routing also belongs in the pre-service checklist the rush cannot delete (Realist). Assessment and chef seats required before `parked`. |
| CUL-001 The pre-service brief | **Split** | Two learners and two objects. CUL-001 keeps the learner's side: retrieval call-and-response, raising errors, the team-making ritual. LEA-005 takes running the brief, with the operational half (86s, allergies, VIPs, gaps) as `workflow.*`. The seam is stated so a learner does not hold two unrelated ideas of pre-shift (CPA). Pre-shift teaching does not count toward progression (intake group 5). Format and timing are team-gated (intake group 3). |

---

## 4. Open system-design questions

Each question stands alone for a one-at-a-time Phase 3 discussion. Gate marks: F = founder-gated, T = team-gated, C = chef-gated, HR = HR seats, E = elicitation-gated (waits on interviews or a first cohort).

### 1. Who owns people and training, and how the management pair splits (F)

**The conflict.** WP Part I (p.10) gives team development, training and the invisible advocate to the Maître d' and gives labor, cost, compliance, vendors and facility to the Operations Lead. The intake (group 1) says "Operations is more people-focused" and the Maître d' is "everything that's not operations". These are opposite (INT C1). A third management name, "floor manager", appears in BG 15, "Floor authority" (INT C5).
**Options.**
- (a) The Maître d' owns people and training, as the white paper says. Operations owns systems, compliance, the rosters as records.
- (b) The operations role owns people and training, as the intake says. The Maître d' owns the experience, recovery standards and service culture.
- (c) The pair co-own, with named sub-ownerships.
**Tradeoffs.** (a) and (b) each put the module system, the sign-off roster and the talent blocks in one domain, which the OSA requires. (c) rebuilds the "node overload" the white paper itself names (Part I, p.14) and leaves the roster without an owner.
**What the research says.** Trained preceptors and trainers are the active ingredient (program structures B4, C4), so whoever owns training also owns assessor calibration and the audit. Leaders must be aligned beforehand for transfer to happen (learning evidence §3).
**What the panel says.** The OSA: the draft's "elective emphasis" softened a structural split into a preference; state domain ownership and put the module system in exactly one domain; the seat will not land which. The Realist: add a pre-agreed rule for who calls a live failure that spans both domains (LEA-010). The CPA: the ownership question sits above sequence and must be settled before the assessor thread is built.
**Also in scope here.** The management titles (Operations Lead, operations manager, Maître d', floor manager), bound `people.*` until the naming session; and whether the on deck reserve ranks people for succession (WP p.14), which the OSA accepts only with visible, evidence-based criteria, or not at all.

### 2. What unlocks the next node (F)

**The conflict.** WP Part I (p.11): "After a set period in any role, the next skill set unlocks automatically", and advancement never waits on a manager's judgment. Intake (group 2): unlocks follow interest and mastery, gated by conversations (INT C2).
**Options.**
- (a) Time in role. Automatic, blind to readiness.
- (b) Demonstrated mastery (L4 on the prerequisite node). Evidence-lit, needs an assessor.
- (c) Time as a floor under a mastery gate, with the unblock conversation recording "learning or move".
**Tradeoffs.** (a) is the only fully automatic option and the only one that lights a node without evidence, which every seat rejects. (b) makes advancement wait on assessor capacity, which is the bootstrap problem in question 17. (c) keeps the automatic trigger for the conversation and the evidence rule for the release.
**What the research says.** Visible counters steer behavior toward what is counted; nodes should light on evidence (program structures F1 to F6). Learner control over sequencing adds almost nothing to achievement, while choice over which path and when supports motivation (learning evidence §7). So give choice over branch and timing, keep structure inside a skill.
**What the panel says.** The CPA rejects progression by seat time unless time is only a floor. The OSA holds that any mechanism routing through a person's attention is a discretion point where hierarchy regrows, so the conversation must auto-schedule (question 11) and "not now" must carry a recorded reason and a re-open trigger. The Instructional Designer and Craft Educator add the experienced-hire case: proven prior experience may shorten the path (program structures B1) only after a contrast check against the house standard, because a hire whose prior house anticipates before the customer signals must unlearn, not skip.
**Bindings.** `founder.unlock_rule`; any time floor is `fact.*`.

### 3. Strands or ladder (F)

**The conflict.** WP Part I, "The service team structure: complementary strands" (pp.10 to 11): outward and inward strands are "not a promotion sequence" and progression is "connections, not altitude". Intake (group 2 clarification): service runs food runner, then back waiter, then front server; bar runs barback, then bartender (INT C3).
**Options.**
- (a) A ladder. The tree shows altitude.
- (b) Strands of equal standing. The tree shows adjacency; cross-strand fluency is the development marker.
- (c) The activity tree as proposed, which can render either, with the choice made at the map view.
**Tradeoffs.** (a) matches how Brandon described the floor and makes leads a natural top. (b) matches the white paper and the OSA's grounding, and makes the runner-to-front-server path a chain of adjacent nodes rather than steps up. (c) defers the call but the map view and the job descriptions cannot render until it is made.
**What the research says.** Adjacent-role chaining gives most of the flexibility benefit (program structures D1), which fits either shape. Leaderboards and rank comparison carry small and unstable motivational effects and can backfire (learning evidence §7), which argues against showing altitude.
**What the panel says.** The OSA's grounding holds strands and adjacency and marks this as data, not a contest. The CPA needs the answer to show prerequisites honestly. The Learner Advocate wants individual position private either way.

### 4. Leads: promotable positions or per-shift designations, and whether an hourly lead may sign alone (F, HR)

**The conflict.** WP Part I (p.10) makes Lead Host, Head of Beverage and Station Leads functional designations, "not permanent elevations". The intake (group 1) makes leads paid, promotable positions (INT C4). The intake (group 4) also flags that positional leads are hourly and must not be used as managers.
**Options.**
- (a) Leads co-rate; a manager holds every decision. Safest on compliance; management bandwidth becomes the bottleneck, certain at opening.
- (b) Leads sign alone after calibration and audits, inside scheduled paid time, with no authority over discipline or pay. Matches the intake's peer-led intent; needs an HR ruling that rating is not managing.
- (c) A separate paid certified-trainer rung, distinct from lead (program structures A4, verified-secondary, dated). Cleaner role line; adds a rung and may conflict with WP p.10.
**What the research says.** Peer marks agree with expert marks best on global judgments against well-understood criteria, and agreement is weaker for professional practice than for products (program structures B3); peer-only sign-off is defensible once the peer is calibrated, uses anchored global ratings and co-rated audits keep agreement high (learning evidence §5).
**What the panel says.** The OSA: rename the assessor level so "supervise" does not hand hourly leads managerial authority by wording (done in 1.2), and treat bandwidth as a requisite-variety test that needs the leadership line count and load from Airtable, with no verdict without them. The Assessment seat: co-rated audits are the load-bearing part of release. The Realist: talent blocks must sit outside service windows or they are not real. The Learner Advocate routes lead scope (LEA-009) to the Emerging Leader Advocate.

### 5. Pay for learning, completion, teaching, and take-home practice (F, HR)

**The conflict.** WP Part II, "Training infrastructure" (p.19): "The more modules completed, the more earned", and any qualified member is paid to teach. Intake: efficacy drives length, completion is not proof (group 7), learning is always paid (group 3), take-home kits are welcome (group 5), and pre-shift teaching does not count toward progression (group 5) (INT C8, C9).
**Options for the earning line.**
- (a) Pay per module completed, literally. Rewards exactly the click-through Brandon distrusts.
- (b) Pay for demonstrated mastery (a passed gate, a new node) and for teaching; recognize completion with specific feedback only.
- (c) Pay authors per module written, once authoring opens.
**Options for take-home practice.**
- (a) All drills on site and paid. Simplest and fully consistent with "always paid"; uses paid floor time.
- (b) Take-home kits with a bound paid practice allowance (`fact.take_home_allowance`), a video exemplar, a self-recorded clip or peer check at a scheduled check-in. Spaced home practice improved retention in surgical trainees; adherence in a paid hourly setting is unknown.
- (c) Unpaid optional practice. Conflicts with the intake and carries wage-law exposure. Not recommended.
**What the research says.** Expected, completion-contingent tangible rewards undermine intrinsic motivation, and intrinsic motivation predicts quality while incentives predict quantity (learning evidence §7, verified-primary, with the reward finding contested). Home practice bunches at the start and end and is guided by required elements and tests, not by self-rating (learning evidence §4).
**What the panel says.** The Assessment seat: if pay attaches to gates, stakes and evidence requirements rise, and so does teaching to the gate. The Practice Designer and Instructional Designer: a self-rating fails silently on faults the learner cannot see (tray tension, eyes on the tray), so the check-in must include an observed rep or a clip against the exemplar. The Realist: tray and stemware carry at tempo still needs on-site sessions under load. The Craft Educator: precision drills are the floor, never framed as rehearsal for hospitality.

### 6. How a gate is recorded and who may record it (F, HR)

**The constraint.** Trainual has no observer or assessor sign-off. Only Admin+ can mark a subject complete for someone, attribution is undocumented, and e-signature is the assignee's own (platform §2, verified-primary; the adapter's line that e-signature can record an assessor's sign-off is wrong and must be corrected).
**Options.**
- (a) Admin+ marks the gate complete. Native; hourly leads would need Admin+ rights; the record does not name the assessor, so consistency cannot be audited.
- (b) An external form is the record (`tool.forms.gate_record`), automation assigns the next subject, and the Trainual mark is automated. Names every rater and holds the rubric; the record lives outside the LMS.
- (c) A learner-kept, co-signed practice record carried in the form, in the German dual-system pattern (program structures C4), which can carry Open Badges-style criteria and evidence (program structures F4).
**What the research says.** Gate reliability depends on how many cases are sampled and whether raters are calibrated, so the record must hold rater identity and anchored ratings (learning evidence §5).
**What the panel says.** The Assessment seat rules out (a). The OSA backs (b) or (c) only if the Admin step is automated or removed. The Realist: records and tree updates happen at close, never on a device during service. The Practice Designer, against CLAUDE.md's steer toward `build_scorm.py` for tracking: practice is low-stakes and tracking a practice score invites reuse as a gate; a record matters only where the Assessment seat rules something a gate.
**Binding.** `founder.gate_record_system`.

### 7. Team feedback on the prove-it shift: timing and framing (F, T)

**The conflict.** The intake (group 4): "the entire team can give feedback throughout the night", and the last shift should be "prove it to the rest of your team". The Realist: at tempo, mid-service feedback pulls attention from the work; collect at close. The Learner Advocate: a public proving on the second live shift is the highest-threat moment in the house, and threat competes with the task for working memory.
**Options.**
- (a) In the moment, throughout the shift, as the intake describes. Closest to Brandon's picture; costs attention at tempo and raises threat.
- (b) Collected privately at shift close, one shared task-focused question, synthesized by a lead, delivered privately. Lower threat and reliable enough as formative input; loses the live, communal quality.
- (c) Prebriefed in-shift observation with collection at close: the team knows what to watch, says nothing mid-service, answers the one question at close.
**What the research says.** Multi-source feedback is reliable only with many raters across groups, and one shift's team is too few for a decision; improvement after it is small and likelier when the recipient sees a need and reacts positively; a substantial share of feedback interventions reduce performance, and effectiveness drops as feedback moves from the task toward the self (learning evidence §6). Peer judgments are most accurate as one global judgment on taught criteria (program structures B3). Psychological safety is the precondition for the critique norm Brandon wants (learning evidence §6, Edmondson).
**What the panel says.** All three seats that touched it converge on formative-only, never a vote, raters recording before seeing the synthesis, and a prebrief. The Practice Designer marks in-the-moment versus after as Brandon's call and defers to TBRI on how it lands. The Learner Advocate names the harm and does not decide the format. The whole critique culture must be practiced at low stakes (CUL-002) before it is aimed at a person on a gate shift.
**Binding.** `workflow.g4_feedback_window`. TBRI review required.

### 8. Release evidence: one shift or a window, and what the reserve requires (T, E)

**The issue.** The draft released a node after one eyes-off shift. The Assessment seat calls that ad hoc entrustment, not a summative decision.
**Options.**
- (a) One angel shift and one eyes-off shift, as the intake describes. Cheapest; under-sampled.
- (b) One angel shift, then a window of eyes-off shifts until one more observation would not change the call. More defensible; longer time to release.
- (c) (b), plus the reserve condition that a node counts for coverage only if its live gates ran on a real, full book, with `workflow.recheck_cadence`.
**What the research says.** One observed repetition is not readiness (program structures C5); trust decisions draw on multiple sources and occasions (program structures B2); direct-observation tools have thin validity evidence and the most evidenced format should be adapted rather than invented (learning evidence §5).
**What the panel says.** The Assessment seat and Learner Advocate converge: spread the evidence over more than one lower-threat occasion. The Realist adds the tempo condition and the OSA accepts automatic reserve membership as structurally sound; both seats call their disagreement data. The Craft Educator: the hospitality layer matures only through volume and articulated trailing, so release should read "released, reads still maturing". Proposal: (c).

### 9. Fail limit, retries and banking (T)

**The intake** (group 4): there will be a fail limit, decided with the leaders and managers Sŏn hires; overrides go up a step to the CEO.
**Options.**
- (a) A fixed number of attempts per gate, then a coaching plan and a conversation (program structures A4). Clear; can read as elimination.
- (b) No attempt count: a required interval between attempts plus a changed practice plan; repeated misses trigger an unblock conversation about fit. Fits spacing and dignity; open-ended cost.
- (c) A scoring rule independent of (a) or (b): pass every part in one sitting (program structures C1) or bank passed parts.
**What the research says.** Spacing favors an interval between attempts (learning evidence §2). Framing a check as diagnostic of ability raises belonging threat; the effect size is contested but the fix is nearly free (learning evidence §5; Learner Advocate).
**What the panel says.** The Assessment seat: separate the criterion from the cut; set each node's cut by contrasting groups on anchored dimensions, on importance not difficulty, documented; that waits on leads who exist. Movement drills may be banked; the integrated G2 performance may not; safety elements pass in every attempt. The Learner Advocate favors (b) and accepts the banking limits. The Realist and Craft Educator mark the limit team-gated.
**Bindings.** The count and interval are `fact.*` or `workflow.*`.

### 10. Presenting the skill tree when Trainual shows only lists (F)

**The constraint.** Trainual shows to-do, completed and optional lists and locks content only in a straight line; branching lives in automation; there is no learner-facing tree (platform §1, §5, hard constraints 1 and 2).
**Options.**
- (a) An external live page reading Trainual completions through the API. Personal and closest to "presented as much as possible"; needs API access, which the help center gives to Premium and Enterprise and the pricing page to Enterprise only, plus hosting and auth.
- (b) A static map subject in Trainual plus a printed back-of-house wall map. Cheap and socially visible; not personal; manual updates.
- (c) A SCORM map. Generic, cannot read progress, re-upload on every change.
**What the research says.** No rigorous workplace study shows visible competency matrices drive self-directed learning; treat it as a hypothesis (program structures F6). Visible metrics steer behavior in unwanted directions (F2).
**What the panel says.** The Learner Advocate: the wall map may show the structure of the tree; individual progress stays private by default, and streaks and leaderboards stay off. The Realist: tree updates happen at close. Revised proposal: (a) when the plan allows, with (b) showing structure only, and Trainual gamification off unless Brandon turns it on (`tool.lms.gamification_setting`).

### 11. Self-scheduling the practical and the unblock conversation (F; T for block design)

**The intake** (group 2): the learner never asks; conversations appear on managers' standing talent blocks.
**Options.**
- (a) The learner books: a completion trigger sends a single-use scheduling link for the talent-block event. The learner still has to act.
- (b) Nobody books: a trigger looks up availability and books the first open talent-block slot through the scheduling API. Closest to "it just appears"; needs a paid plan and custom automation; pooled scheduling unverified (platform §4).
- (c) Trainual "Request" access. Routes to Admins, not leaders. Weakest.
**What the research says.** The invisible advocate as the white paper frames it removes the manager's attention from advancement (WP Part I, p.11), which only (b) does fully. Autonomy support is strongly linked to autonomous motivation (learning evidence §7).
**What the panel says.** The OSA treats (b), or its equivalent, as the only structurally sound option. The Realist: blocks sit outside service windows or they are not real. Every option ends the conversation in one of four recorded states (LEA-006).
**Bindings.** `workflow.gate_autoschedule`, `workflow.talent_block`, `workflow.assessor_pairing`, `tool.scheduling.platform`.

### 12. Measuring decision alignment and detecting complacency (F, E)

**The intake** (group 7): the measure is people making decisions the way Brandon would; distrusted signals are complacency and mere participation.
**Options.**
- (a) Agreement with a reference panel on scenario and situational-judgment items, tracked over time, with disagreements becoming discussion cases. Single-source risk while the panel is one person.
- (b) Behavior-level evidence: floor observation and success-case interviews inside the weekly review window (`workflow.post_launch_review_window`). This is what `measured` requires; costs leader time.
- (c) A signal watchlist. Positive: voluntary practical requests, errors raised in pre-shift, cross-role critique. Complacency: completion with no later requests, uniform ratings with no spread, the same few voices answering. Prompts to investigate, never targets.
**What the research says.** Incident-based cognitive task analysis, then decide-and-compare training against a panel, then situational-judgment checks with instructions matched to the construct (learning evidence §8). Satisfaction reactions predict transfer poorly; usefulness reactions and behavior-level evaluation do better (learning evidence §9). Mandated checklists without cultural uptake changed nothing (learning evidence §9). Once a measure becomes a target it stops working as a measure (a principle, not tested).
**What the panel says.** The Craft Educator: one read is not a standard; Brandon anchors a panel built per judgment for fit with canon, with minority views kept. The Assessment seat: (a) is a learning and alignment measure and never gates advancement until the panel includes calibrated leads. The Practice Designer: the measurement bank is separate from the practice bank. The Learner Advocate: "the same few voices" is a prompt to look for concealment and never a mark against an individual. Proposal: (a) plus (b), with (c) as a supplement.

### 13. Module length rules

**Options.**
- (a) One objective and one learning job per critical-path unit; no time target; off-path long-form unrestricted.
- (b) Time caps per unit. A cap is a figure and no evidence shows short is better in itself.
- (c) (a) plus a required spaced-retrieval schedule on every critical-path unit, anchored to the learner's next shifts.
**What the research says.** Microlearning has no agreed definition and no behavior-level evidence; the gains credited to it come from spacing, retrieval and learner-paced segmenting (learning evidence §1, §2). No study tests spacing on irregular hourly shifts; cap the longest gap rather than chase an interval.
**What the panel says.** The Instructional Designer backs (c) and asks that interleaving be applied to near-miss visual discriminations and that menu facts, specs and scripts stay blocked (with the Practice Designer). Proposal: (c). Format and timing of pre-shift, where retrieval lives, stay team-gated.

### 14. Review cadence, volatility tags and learner flags

**The intake** (group 6): reminders in ClickUp by creation date; a scan that tags volatile content before it goes live; a learner flag that creates a review task automatically.
**Options.**
- (a) Date-based reminders only. Blind to what changed.
- (b) Volatility tags derived from binding namespaces at `drafted` (`tool.*` and `fact.*` high, `workflow.*` and `chef.*` medium, durable low), with a change event in a tool or workflow triggering review of every dependent module through the bindings registry.
- (c) Both.
**Platform facts.** Trainual has native content-verification reminders and a content-quality flag on Pro and above, but the flag is not a Zapier trigger and its webhook status is unverified, so the fallback is an embedded form on each subject's closing page (platform §8).
**What the panel says.** No seat challenged (c). Proposal: (c), with `tool.forms.content_flag` and `workflow.flag_to_review_task`.

### 15. How outside compliance content links in

**The intake** (group 1): food handler and other certifications are taken inside Trainual and never written by Sŏn.
**Platform facts.** Trainual's Premium courses add-on exists on all plans and covers harassment prevention, workplace safety and similar; no food handler or alcohol-service course was confirmed, so plan on an outside provider through an external link with the certificate uploaded, or SCORM only where Sŏn holds the rights (platform §7).
**Options.** (a) the add-on for what it covers; (b) an outside provider by link, completion verified by an Admin; (c) provider SCORM where rights allow.
**In every option** these are catalog rows of type "linked" with no durable content (standing rules, "Scope"). Costs are `fact.*`.

### 16. Whether the lifecycle and panels change

**Options.**
- (A) Minimal: add catalog row types `linked` (skips designed, drafted, reviewed), `library` (finished by proven conversation, light panel) and `gate-spec` (per-node gate criteria reviewed by the Assessment seat).
- (B) Moderate: (A), plus a per-node gate spec as an exit criterion at `designed` for any module that feeds a gate (Assessment); volatility tags and a retrieval schedule as exit criteria at `drafted`; a novice-attempt test as an exit criterion at `reviewed` for every critical-path module, once receiving-end learners exist (Learner Advocate, elicitation-gated); the post-launch review window as a `workflow.*` hold between `published` and `measured`; TBRI on every module with team feedback or role-play; the OSA only on modules that change node structure, unlock rules or role definitions (OSA); separate practice, gate and measure banks required of any scenario module (Practice Designer).
- (C) (B), plus a `calibrated` checkpoint on rater-facing LEA modules before any assessor release.
**Tradeoffs.** (A) leaves gates unreviewed. (C) may be overbuilt before any lead exists.
**Proposal:** (B). The authoring template's instructional soundness becomes a listed deliverable owned by the Instructional Designer.

### 17. The opening bootstrap: no calibrated leads, trainers or talent blocks exist at launch (F, T)

**The issue.** Every seat in panel group 1 flags it. By the intake's own rule (group 4), until a lead has completed the assessor path every practical needs a manager present; at opening, every first cohort hits G3 at once on green shifts. Pre-opening is out of scope (intake group 1), but the ongoing program has to name the gap.
**Options.**
- (a) Founders and managers run every G2 to G4 for the first cohorts; accept the bottleneck and cap live gates per service.
- (b) Certify a first assessor cohort before opening through the LEA path plus co-rated audits on mock services, so some leads reach the assessor thread on opening day.
- (c) Hire a small number of experienced leads whose prior calibration is checked against the house standard (question 2's contrast check) and audited early.
**What the research says.** Opening programs lead with culture and use mock services as the group version of the practical (program structures E1, E2). Structured programs with trained preceptors improve competence and retention (program structures B4).
**What the panel says.** The Realist: the load lands on green crews; bind `workflow.live_gate_limit`. The OSA: bandwidth is a requisite-variety test that needs Airtable figures. The CPA: the whole sequence is a hypothesis until the first cohort's struggle points are logged. The Learner Advocate: the novice-attempt test can run on the first cohort.

### 18. Who holds the door, and who holds the protocol triggers (F)

**The conflict.** WP Part I (p.10): the Lead Host owns the door and the host-stand function and the Maître d' is freed from it. BG 15, "Arrival choreography" and BG 13, "Threshold": no host stand; the Maître d' receives each customer at the top of the steps and seats them (INT C6). Related: BG 15, "Key protocols" makes the dinner-to-late-night shift "same person, same moment" and treats the David protocol and similar as system decisions set before service in the reservation tool (INT Q18, Q19).
**Options.** (a) The Maître d' holds the threshold, hosts pace the room from the book. (b) The lead host holds the door, the Maître d' holds the room. (c) The Maître d' at the threshold at dinner, the lead host at other dayparts.
**What it changes.** How much of SVC-010 and SVC-011 is content and how much is binding; who is trained to set protocol flags and who to act on them; who holds the late-night trigger (`people.*`). The Realist marks door pacing as an upstream cause of kitchen failure, so whichever role paces the room needs SVC-011 on its critical path.

### 19. Mentor, angel-shift trainer, or one person (F)

**The conflict.** WP Part II, "Onboarding" (p.18) pairs every hire with a mentor chosen as a cultural steward rather than the strongest performer. The intake names an angel-shift trainer and peer practicals and no mentor (INT C18).
**Options.** (a) One person: the angel-shift trainer is the mentor. (b) Two people: a trained assessor runs the angel shift; a cultural-steward mentor holds the relationship and the reflection. (c) The mentor is the reserve member's named contact on borrowed shifts as well (program structures D2).
**What the research says.** A designated contact protects floating staff (program structures D2); reflection time is an ingredient, not a nicety (B4). Selecting for cultural stewardship over performance fits the "cultural steward" line but needs criteria.
**What the panel says.** No seat challenged the split; the Craft Educator wants the trailing structure specified whoever runs it. Criteria for "cultural steward" are Brandon's.

### 20. Critique rituals and who teaches at pre-shift (F, T)

**The conflict.** WP Part II (p.17): post-mortems are private and process-focused, and management absorbs blame. Intake (group 4): an open whole-team critique shift and cross-level critique as a norm (INT C14). Intake (group 5): pre-shift is led by the Maître d', the operations role or the lead host; the Craft Educator wants teaching rotated across ranks as a transmission method.
**Options.** (a) Two rituals: private process-focused incident review (LEA-008) and open task-focused readiness feedback (G4, CUL-002), designed so neither is mistaken for the other. (b) One open ritual for both. (c) (a), plus a rotation of pre-shift teaching to any rank that never counts toward progression.
**What the research says.** Feedback aimed at the self reduces performance; task-focus and safety are the conditions (learning evidence §6). Speaking up does not cost everyone the same (reading list §1.3), so critique needs a protocol and shared language taught on both sides.
**What the panel says.** TBRI and the Culture seats must review. The Learner Advocate: cross-role critique is practiced at low stakes first. The Craft Educator marks the rotation as compatible with Brandon's exclusion of pre-shift teaching from progression.

### 21. AI presenters in internal training video (F)

**The conflict.** BG 07, "The six-tier authority hierarchy": AI-generated imagery is prohibited at the Tier 4 level with no public-facing qualifier; BG 12 and BG-md 10 limit the ban to public-facing surfaces. The intake (group 5) allows AI presenters modeled on the founders and templates (INT C7).
**Options.** (a) An explicit canon carve-out for internal training surfaces. (b) Real footage and founders on camera only. (c) AI presenters as the model in demonstrations only, never in place of rehearsal.
**What the panel says.** The Practice Designer: allowed in principle, the carve-out is Brandon's to write, and an AI presenter serves as the model and never replaces rehearsal. Likeness consent for anyone other than the founders is HR (`founder.ai_presenter_policy`, `workflow.recording_consent`).

### 22. Teaching the Korean terms and the personas (F)

**The conflict.** BG 09, "Hangul deployment", "Rule 2 · No translation" forbids glossing on brand surfaces. Learners must understand Jeong, Nunchi, Mahk, Jaeyeonmi, Ma and the persona labels to work inside them (INT Q14).
**Options.** (a) Internal training may explain the terms in full, as training is not a brand surface. (b) Training cites the canon label and teaches the concept through cases without a gloss. (c) A founder-written internal glossary that is itself canon.
**What it changes.** ORI-001, SVC-006 and the LIB tracks. BG 05 personas calibrate and never constrain in any option. The Craft Educator's canon translation layer depends on this.

### 23. Daypart scope at opening (F)

**The conflict.** BG 01 and BG-md 01 describe four dayparts including a lunch expression, and BG-md 08 carries a daytime uniform line; WP Part V (pp.35 to 36) runs dinner alone for a set period with lunch and brunch held in reserve (INT C12).
**Options.** (a) Train for dinner and late night only at opening; daypart registers as bindings. (b) Train all registers now. (c) (a), with each additional daypart as a later branch.
**What it changes.** Which registers, uniform lines and protocols (late night, pyeong-sang) training covers, and, per the OSA, whether each daypart is its own team or one team.

### 24. The recovery range and its owner (F, C for food)

**The conflict.** WP p.26: "whatever it takes, do not negotiate, lead with more than expected", with bottles and spirits carried for gifting; WP p.13: an authorized generosity range; BG 15: recovery is "pre-authorized inside known limits" with escalation triggers set before service; BG-md 08 lists triggers including a financial threshold (INT C11).
**Options.** (a) Bounded: a known range and named triggers, any threshold as `fact.*`. (b) Open: whatever it takes, with a post-hoc review. (c) Bounded by role: a wider range for the Maître d', a narrower one for the floor.
**What the panel says.** The Realist: a pre-authorized gesture needs a named owner and the slack to carry it out on a full night (`workflow.recovery_owner`); SVC-002 teaches what to do when nobody is free. The Craft Educator: bounded discretion with limits kept out of durable content; the food side of any recovery is chef-gated.

### 25. Which Box copies are canonical (F)

**The issue.** Box holds the Pitch Materials white paper (`2466517057642`, modified 2026-09-14) and two "03. Sŏn Investor Diligence White Paper" copies modified a day later (`2468611192111` in the Investor Room Template; `2468627027608` in an investor room). Box holds the BG v3.0 PDF (`2281626080747`, 2026-06-12) and three later Markdown copies labeled v1 (`2281555280952`, `2356714319901`, `2356731001214`, the last dated 2026-07-19). The two BG copies differ in section numbering, the uniform table, escalation detail and several Playground clauses (INT C13). Both files name ClickUp `2ky45bmy-15773` as the record of truth.
**Already decided (Brandon, 2026-09-28, during this run).** Internal sources are read from Box, never from ClickUp documents. CLAUDE.md, `canon/pointers.md`, `canon/standing-rules.md` and `framework/bindings.md` now point at the BG PDF `2281626080747` (with `2356731001214` as a text fallback) and the Pitch Materials white paper `2466517057642`. What stays open is only which copy is canonical where copies diverge: the June v3.0 PDF or the later July Markdown.
**Options.** (a) Keep the PDF as canonical, as the pointers now say, and treat the Markdown as a supplement. (b) Make the July Markdown canonical, since it is newer, and update the pointers. (c) Freeze a dated snapshot per release in the frozen-releases folder.
**What it changes.** Every module citing uniforms, the nine-beat sequence or escalation cites labels only and binds specifics until this is settled. The catalog `source` fields for ORI-001, LEA-001 and SVC-001 can cite the Box white paper directly and never ClickUp (INT Q20).

---

## 5. Panel reads

**Curriculum and Program Architect (validated).** In its lane, the seat supports nodes as activities, mastery-lit progression, the depth tiers and LIB off the critical path. It challenged the absence of a program-level end state and it was right: section 1.0 now states terminal transfer goals first. It was right that the sequence opened with fragments, so a whole-service observation now comes before the drills. It was right that ORI-005 was a familiarity item placed in the lean core, so it moved. It asked for named threshold concepts as hypotheses ("the customer experience is produced by every function at once", "anyone may critique anyone", the movement-decision split), which are carried as hypotheses to test with the first cohort, and for pairs linked on the map (SVC-008 with BEV-008, SVC-007 and BEV-009 with ORI-003, SVC-002 with SVC-009, CUL-001 with LEA-005), which are linked in the table. It holds that the whole sequence is a hypothesis until recent-hire accounts exist. Its anchors are from K-12 and higher education and it marks its calls as reasoned, not proven in hospitality.

**Organizational Systems Architect (validated).** The seat backs the activity tree, evidence-lit nodes, automatic reserve membership and the role manifest as the single source, and it reads the runner-and-back-waiter station binding as reading the flow rather than the chart. It challenged every mechanism that routes through a person's attention: the Admin mark, learner-booked scheduling, "Request" access and an unrecorded "not now". Those are revised (LEA-006 records the reason and re-opens automatically; the Admin step must be automated or removed; nobody-books is the proposed scheduling shape). It was right that "supervise" in the old L5 handed hourly leads managerial authority by wording, so the assessor thread is now separate. It was right that "elective emphasis" softened a domain split, so the management pair is now domain ownership with the owner open in question 1. It limits its own review seat to modules that change structure. It holds strands and adjacency, marks the intake's ladder and promotable leads as unlanded conflicts, and notes that its own landed claims cite V7 in ClickUp and need re-anchoring to the Box white paper before they count as canon.

**Hospitality Operations Realist (validated).** The seat backs gates before customer contact, angel-shift slack funded by design, the movement-decision split, the pre-shift split and the bound recovery range. It challenged in-the-moment team feedback at tempo (now question 7), paper readiness for the reserve (now a full-book condition with a recheck cadence), and a sequence that assumes trainers and talent blocks exist at opening (now question 17). Its bindings are adopted: `workflow.live_gate_limit`, talent blocks outside service windows, refreshers that never displace the readiness brief, `workflow.recovery_owner`, a rule for live failures across both domains (LEA-010). It strongly backs SVC-011 and asks that the module teach the connection to kitchen tempo while the pacing rules stay operating-system decisions. It accepts the observation shift only if the observer is extra to staffing and out of paths. Its anchors are elite fine-dining and memoir sources held as reasoned, and it states that untested is not the same as will not survive.

**Instructional Designer (validated).** The seat backs the movement-decision split, one objective and one learning job with a required retrieval schedule, and behavior-level measurement. It was right that every Introduce module assumed a novice, so novice and experienced paths with a contrast-and-unlearn step are now required on every critical-path Introduce module. It was right that onboarding was massed into one remote block, so the block is now know-it and see-it only with spaced returns and conversations between pieces. It was right that G2 was the first point of integration, so an integration practice step now precedes it. Its front-end check holds four rows (SVC-004, SVC-009, BEV-007, SYS-001) as environment, policy or tool problems rather than instruction gaps. It wants the drills interleaved across sessions and practiced on the real floor surface, take-home check-ins to include an observed rep, and the authoring template listed as its own deliverable. It disagrees mildly with the intake's wish to limit paid drill time: cutting corrected reps without a feedback substitute trades time for retention.

**Assessment and Competency Designer (validated).** The seat backs evidence-lit nodes, entrustment levels, release at the "does" level, formative-only team feedback and the co-rater rule. It was right that L4 rested on one shift, so release is now a window of eyes-off shifts (question 8). It was right that the spoken check carried fluency, nerves and second-language load, so G1 now has content anchors, a show-don't-tell route and a knowledge-only role. It was right that a task list is not a competency model, so a per-node gate spec (construct, anchors, evidence level, occasions and raters) becomes an exit criterion at `designed` and SVC-001 waits on it. Adopted: SAF-001 non-compensatory and shown at G2; movement parts bankable, the integrated performance not; refresher separated from recheck; overrides logged with downstream tracking; raters rate before seeing the team synthesis; humility recast as observable behavior; LEA-002 reworded so structure comes first and audits carry release; the paid practical interview kept apart from gate evidence and routed to HR; the alignment measure never gates advancement while the panel is one person. It accepts the spoken format as a founder call while naming it the likeliest source of variance unrelated to readiness. Its external anchors are unverified this pass.

**Learner Advocate (validated).** The seat backs learner autonomy in the tree, per-node states, "learning or move" with both answers fine, and private synthesized feedback. It was right that G4 as written was a public display of not-yet competence, so the frame is now support, with a prebrief, advance notice and private delivery, and the timing is question 7. It was right that remote onboarding met the learner alone, so the block assumes concealment and checks comprehension without confession. It was right that no receiving-end learner touched a module before it shipped, so a novice-attempt test enters the lifecycle at `reviewed`, elicitation-gated. Adopted: private rehearsal before G1; "not yet" never a failure state; "recheck due" framed as rhythm; the wall map shows structure and never individual position; the fail limit as interval plus changed plan; the expert-comparison reveal shows reasoning, not "you were wrong"; "the same few voices" as a concealment prompt, never a mark. It routes take-home pay, lead scope and the mistreatment policy out of its lane. It agrees with the Instructional Designer that desirable difficulty should be named as expected, not softened.

**Hospitality Craft Educator (unvalidated; stage 6 skipped).** The seat backs the movement-decision routing, the narrowed SVC-002 and the incident-sourced decision modules. It was right that "Build now" was mislabeled on the judgment modules, so those rows now read "frame now, cues elicitation-gated", and it notes that pre-opening elicitation draws only on Brandon, whose incident pool is largely lineage. It was right that no module named the service-versus-hospitality distinction, so ORI-001 gains that objective. It was right that the pyeong-sang choreography and responsive dining-room service were treated as one craft, so they are split and the step-back model is triggered by attunement, not timed. Adopted: three-part beverage skill (recognize, categorize, tell); release on hospitality-layer nodes reads "reads still maturing"; scripted task side and flexed treatment side for the host modules; care as named cognitive moves, never installed; menu items attached to causal stories. It challenges the intake's single-reader standard (one read is not a standard; Brandon anchors a panel built for fit with minority views kept), the research's shortcut for experienced hires (contrast check first), and the Realist profile's "precision as rehearsal" (precision is the floor). Its claims stand unchecked; the beverage evidence is wine only.

**Practice and Simulation Designer (unvalidated; stages 6 and 7 skipped; consumes the Craft Educator's content).** The seat backs drills recombined at the practical, expert comparison with minority views, low-fidelity kits and mock settings, and peer-led practicals. It was right that practice items and measurement items were mixed, so three banks are now kept apart. It was right that G3's reflection and G4's feedback were named but not designed, so prebriefs, advocacy-with-inquiry debriefs, a strategy triage and a review of what went right are now in the gates and in LEA-001 to LEA-003. It was right that a self-rating cannot see tray tension, so take-home feedback is a clip against an exemplar or a peer check. It was right that most modules named no practice form, so the module table carries one. Adopted: SAF-001 built around the decision with distractors from real errors; SVC-006 as a classification drill on briefed stills; menu facts blocked; role-play with a prebrief and a stop rule for SVC-009 and CUL-002 (the stop rule is its own inference); practice instructions ask for the most effective move. It challenges CLAUDE.md's steer toward tracked SCORM for practice, holding that a tracked practice score invites reuse as a gate, and it defers the in-shift feedback question to TBRI.

---

## Job descriptions generated from the path

Brandon asked at intake that job descriptions for every role fall out of this work. The white paper's transparency sheet at the first interview (WP Part II, "Talent acquisition", pp.17 to 18: org chart, direct lead, compensation and benefits, communication expectations, training plan with pay dates, advancement path) is the same artifact from the candidate's side (INT Q17). One source renders all three.

**The role manifest.** Proposed as `catalog/roles/<role>.yaml`, one per role. It lists the `people.*` title and reporting line; the node list with each node's module IDs and transfer goals ("on their own, a person can..."); the entry node and the paid practical interview; the supervision level required for release; the electives open to the role; the adjacent unlocks in the chain; and the assessor and lead path.

**Rendering.** A script (proposed) builds the job description from the manifest: purpose, the role's line from WP Part I (pp.10 to 11) cited by label; what you will do, the L4 transfer goals of the role's nodes; how you get there, the gates and the training plan with pay dates bound as `fact.*` or `workflow.*`; where it leads, the adjacent unlocks, the on deck reserve and the lead path; pay and benefits, `fact.*` from Airtable only. The same manifest renders the tree view and the transparency sheet.

**Why this works.** Every responsibility in a job description traces to a transfer goal someone can be assessed on, so a job description cannot promise what the program does not teach, and adding a module to a node updates the description on the next render. The OSA reads this as keeping the knowledge in the system and closing skill invisibility; the Assessment seat adds that the manifest lists tasks and the gate spec, not the manifest, defines competence.

**Gates.** Titles wait on the naming session (WP p.15). KIT roles are chef-gated. Lead and management descriptions wait on questions 1 and 4. Which shape the tree renders waits on question 3.

---

## 6. Sources

### Internal sources (Box)

| Source | Box file id and section | What it supports | Status |
|---|---|---|---|
| Sŏn Investor White Paper Sept 2026 | `2466517057642`, Part I, "Individual progression: the inverted web" (p.11); "The service team structure: complementary strands" (pp.10 to 11); "Open items" (p.15); Part II, "Labor as asset, not cost", "Employees are the users", "Blame the process, fix the process" (pp.16 to 17); "Talent acquisition" (pp.17 to 18); "Onboarding" (p.18); "Training infrastructure" (pp.18 to 19); "Performance management" (p.19); "How the team is paid" (p.20); "No hierarchy of importance" (p.20); "Cultural impact" (pp.22 to 23); "The cooling system"; Part III, "Belonging"; Part V dayparts (pp.35 to 36) | Roles, advancement mechanism, readiness gate, peer authoring and paid teaching, onboarding order, pay principle, measurement, dayparts | verified-primary (read in full; figures noted by location only) |
| Diligence white paper copies | `2468611192111`, `2468627027608` | Existence only; not compared | unverified |
| Brand and Experiential Guidelines v3.0 PDF | `2281626080747`: 01 "Company non-negotiables", "Language constant"; 02 "Jaeyeonmi", "Ma · Yubaek-ui-mi", "Mahk", "The bent spoon"; 03 "Playground Philosophy", "Jeong and Nunchi", "This is not omotenashi"; 05 personas and "Persona-to-daypart matrix"; 06 "Master register · the six constants", "Present without performing"; 07 "The six-tier authority hierarchy"; 09 "Hangul deployment", "Rule 2 · No translation"; 11 "Six rules", "Six binary tests", "Forbidden lexicon", "Preferred terms"; 13 "The nine-beat spatial sequence", "Threshold", "Reveal", "Departure", "Cross-zone governing principles", "Pre-CD open items"; 14 "Sonic governance tiers"; 15 "Step-back architecture · three phases", "Floor authority", "Arrival choreography", "Key protocols", "Uniform system"; 16 "Interaction principles"; 17 and 18 "Held items" | Labels that constrain training design; door and threshold; recovery limits; uniform; chef-gated held items | verified-primary (read in full) |
| Brand Guidelines Markdown copy | `2356731001214`: 01 (Playground training clauses, Ma and Mahk staff clauses), 06 (daypart lighting, "We walk, we never point"), 08 (service model, escalation triggers, uniform lines), 09 (verbal identity additions) | Supplementary clauses only; content differs from the PDF | verified-primary for sections read; version relation unverified |
| Older Markdown copies | `2356714319901`, `2281555280952` | Existence only | unverified |
| Trainual capability tour folder | `421832819408` | Named as where unverified platform items get settled | lead-only |

### External evidence

| Source | What it supports | Status |
|---|---|---|
| ten Cate, "Entrustment as Assessment", J Grad Med Educ 2016; ten Cate et al., AMEE Guide 99, 2015; Hauer et al. 2014 | Nodes as activities, supervision levels, trust conditions, criteria per task | verified-primary |
| 14 CFR 121.434(e) | Supervised operating experience: observer present, trainee extra to crew, simulation credit, prior-experience waiver | verified-primary |
| Falchikov and Goldfinch 2000 | One global peer judgment on taught criteria; weaker agreement for practice | verified-primary (abstract) |
| NCSBN transition-to-practice study | Trained preceptors, reflection time, program length as active ingredients | verified-primary (results page) |
| Wright competency model | Validation methods beyond checklists | lead-only |
| Restaurant shadow, reverse shadow, sign-off | Industry norm tests after customer contact | lead-only |
| Court of Master Sommeliers, Certified exam | Knowledge plus service practical; pass all parts in one sitting | verified-primary |
| USBG Master Accreditation | Written exam unlocks live practical | verified-primary |
| SCA Coffee Skills Program | Isolated movement practicals; points toward a diploma | lead-only |
| BIBB, German dual system | Certified trainers; house plan off a stable standard; learner-kept co-signed record | verified-primary |
| Kotsis and Chung 2013; McGaghie et al. 2011 | One rep is not readiness; deliberate practice and simulation | verified-primary; verified-secondary |
| NIST MEP, Training Within Industry | Prepare, present, test, follow up with tapering coaching; versatility matrix | verified-secondary; matrix lead-only |
| Jordan and Graves 1995; Hopp, Tekin and Van Oyen 2004 | Adjacent-role chaining | verified-primary (abstracts; untested in restaurants) |
| Suarez et al. 2026, float pools | Home team, orientation, named contact, debrief | verified-primary (small qualitative) |
| Tracey, Hinkin et al. 2015, Cornell Hospitality Quarterly | Culture before technical; passive methods common; cross-training practice; pre-opening | verified-primary (self-report, small sample) |
| Kalloch, Silver and Ton, HBR 2023 | Cross-training stabilizes the workforce | lead-only (summary read) |
| NIST Baldrige blog on Ritz-Carlton 2017 | Daily line-up with one shared topic; coach; recommitment | verified-secondary (company self-report) |
| Boston Hospitality Review, Simpson 2023 | Hire on hospitality quotient | verified-secondary |
| Workforce Management 2006, Cheesecake Factory | Retake limit, recertification, paid trainer rung | verified-secondary (dated) |
| Starbucks Global Academy, Coffee Master | Visible mastery marker; manager selection | verified-primary |
| Eleven Madison Park Dream Weaver | Enabler role | lead-only |
| Hamari 2017; Moldon et al. 2021; Deci, Koestner and Ryan 1999; Cerasoli et al. 2014; Sailer and Homner 2020; Hanus and Fox 2015 | Badges raise volume not quality; visible metrics steer behavior; completion rewards undermine intrinsic motivation; incentives predict quantity; gamification small and unstable | verified-secondary; verified-primary; verified-primary (contested); verified-primary; verified-primary; verified-secondary |
| 1EdTech Open Badges 3.0; UKHospitality skills passport | Criteria and evidence in credentials; portability | verified-secondary; lead-only |
| De Gagne et al. 2019; Monib et al. 2024; Rey et al. 2019 | Microlearning undefined; segmenting effect | verified-primary |
| Cepeda et al. 2006, 2008; Adesope et al. 2017; Rawson and Dunlosky 2022; Kerfoot et al. 2007; Brunmair and Richter 2019 | Spacing, retrieval, successive relearning, spaced questions for working residents, interleaving | verified-primary except Cepeda 2008 and Rawson (verified-secondary) |
| Blume et al. 2010; Salas et al. 2012; Jacobs structured OJT; Collins, Brown and Newman | Transfer climate; structured on-the-job training; cognitive apprenticeship | verified-primary (full); verified-secondary; verified-secondary (direction only); verified-secondary |
| van Merriënboer 4C/ID; Wightman and Lintern 1985; Wulf and Shea 2002; Czyż et al. 2024; Moulton et al. 2006; Joosten et al. 2022; Thinggaard et al. 2017; Driskell et al. 1994; Toth et al. 2020; Macnamara et al. 2014; Chua et al. 2021; McKay et al. 2023 | Part-task inside whole-task; reintegration plan; complexity; contextual interference near-null in applied settings; distributed motor practice; home practice; mental practice small; deliberate practice framing; attentional focus contested | verified-secondary; verified-secondary; verified-primary; verified-primary; verified-secondary; verified-primary; verified-primary; verified-secondary; verified-secondary; verified-secondary; verified-secondary; verified-secondary |
| Wass et al. 2003; Brannick et al. 2011; Kogan, Holmboe and Hauer 2009; Roberts et al. 2000; Memon et al. 2010; Woehr and Huffcutt 1994; Double et al. 2020; Speyer et al. 2011 | Structured orals, OSCE reliability, direct observation, oral-exam fairness, frame-of-reference training, formative peer assessment | verified-primary except Roberts and Woehr (verified-secondary) |
| Donnon et al. 2014; Smither et al. 2005; Kluger and DeNisi 1996; Edmondson 1999 | Multi-source feedback needs many raters; small improvement; feedback can reduce performance; psychological safety | verified-primary; verified-primary (full); verified-secondary; verified-primary |
| Slemp et al. 2018; Karich et al. 2014 | Autonomy support; learner control near-null | verified-primary |
| Klein et al. 1989; Tofel-Grehl and Feldon 2013; Edwards et al. 2021; Klein and Borders 2016; Tallentire et al. 2026; McDaniel et al. 2007; Lievens on SJT coaching | Critical Decision Method; CTA-based training; ShadowBox; SJT validity and instructions; practice exposure inflates scores | verified-secondary; verified-secondary; verified-primary; verified-secondary (developer-run); verified-primary; verified-secondary; partially verified |
| Alliger et al. 1997; Saks and Burke 2012; Brinkerhoff 2005; Urbach et al. 2014; Mayer et al. 2016; Dixon-Woods et al. 2011; Neal and Griffin 2006 | Reactions predict transfer poorly; behavior-level evaluation; success case; checklists without uptake; compliance versus participation | verified-primary except Saks and Burke (verified-secondary) |
| Rudolph (advocacy with inquiry); Eppich and Cheng (debrief strategy); Ellis and Davidi; Tannenbaum and Cerasoli; Hamstra; Norman; Golubovskaya | Debrief design; review of what went right; structure over length; low fidelity; service-versus-hospitality language gap | partially verified; verified-primary; verified-secondary; unverified; unverified; unverified; verified-secondary (abstract) |
| Seat-held anchors (Wiggins and McTighe, Reigeluth, Meyer and Land, Freeman, Ashby, Dignan, Laloux, Fitts and Posner, Sweller, Kalyuga, Baldwin and Ford, Ericsson, Popham, Miller, Messick, Hambleton and Pitoniak, Govaerts, Deci and Ryan, Rose, Schmader and Johns, Steele, Walton and Cohen, Hinds, Keller, Bourdain, Guidara, Meyer, Sorgule) | Cited by the panel from profile corpora | unverified this pass |

### Platform documentation

| Source | What it supports | Status |
|---|---|---|
| Trainual help center: training paths, complete in order, force order, content discoverability, the Home page, notifications list, test question types, view test results, SCORM uploads, e-signature, update completion percentages, Zapier triggers, API and webhooks, upload audio files, embed a form, content verification reminders, commenting | Linear locking only, no tree view, gamification, native tests, SCORM completion, learner-only e-signature, Admin+ mark, completion triggers, API scope, audio as link, form embed, reminders, content flag on Pro | verified-primary (vendor documenting its own product); score display, video grading, mark attribution, webhook event list and audio tracking unverified |
| Trainual pricing and product updates; Trainual vs iSpring page; Premium courses and courses pages; Wrapped 2025 post | Plan tiers (with an API-tier conflict between help center and pricing page); no observation checklist; compliance add-on; content flag mechanics | verified-primary for plans and the negative; course lists and flag mechanics lead-only |
| Make app listing; Zapier Trainual and 7shifts listings | Actions only on Make; assign-on-completion; 7shifts cannot book | verified-secondary |
| Calendly developer docs (single-use links, team links, Scheduling API); Google Calendar appointment schedules; Microsoft Graph Bookings | Book-without-UI route; booking page limits; shared-business-only API | verified-primary (Calendly pooling and Google API absence unverified) |
| ClickUp help: Zapier integration | Form-to-task route for flags | verified-primary |
| `adapters/trainual.md` (repo, 2026-09-26) | Checklists self-completed; contains the incorrect e-signature line | verified-secondary (repo) |

### Reading list

| Source | What it supports | Status |
|---|---|---|
| Erica Catubig, "Why Tipping Gives You the Ick" (2026-08-07); "The Grass is Greener... Where You Ethically Farm It" (2026-07-29); "Hey... Are You Okay?" (2026-08-15) | Care as costly labor; paths and leaders' example; who reads the worker; mistreatment cases | verified-primary (full text read at source); part two of the tipping series not yet read |
| Danny Meyer, *Setting the Table*; Will Guidara, *Unreasonable Hospitality* | The lens Catubig writes against | unverified this pass (named in intake) |
| Spence, *Cell* 2015; Spence, *Flavour* 2015; Shepherd, *Nature* 2006 and *Neurogastronomy* 2012; tongue-map review (PMC8956797); Morrot et al. 2001; Plassmann et al. 2008 and Schmidt et al. 2017; Hodgson 2008; Yan and Dando 2015; Crisinel and Spence 2010, 2012; North 2012; Zampini and Spence 2004; Piqueras-Fiszman et al. 2012; Spence and Van Doorn 2017; Hayes and Keast 2011 | Flavor is multisensory; smell dominates; myths to drop; color and price shape taste; judge inconsistency; sound, vessel and plate effects (contested or chef-gated); individual variation | verified-secondary (abstracts), tongue-map review verified-primary |
| Wansink menu-label and bottomless-bowl studies | Never taught; retracted | verified-secondary (retraction record) |
| Eliasson (MoMA 2001; Institut für Raumexperimente); Es Devlin (*Abstract* 2017); Rockwell, *Drama* 2021; Ferran Adrià and elBulli (elBullifoundation synthesis and Sapiens; Capdevila et al. 2015); Albert Adrià; Cas Holman; Grant Achatz biography (NPR 2011) | Lenses on perception, time, ensemble, codification, essence, kit-of-parts, sensory sequencing (Achatz flagged as lineage) | verified-secondary; lead-only; verified-secondary; verified-primary and verified-secondary; verified-secondary (quote lead-only); verified-secondary; verified-secondary |
| Tobin Ellis, Perlick station; *Cocktail Codex* 2018; *Liquid Intelligence* 2014 | Station ergonomics; root-and-family grammar; the why layer | verified-secondary (vendor features); verified-secondary; verified-secondary |
| Harris and Giuffre, *Taking the Heat* 2015; Paules, *Dishing It Out* 1991; Druckman, *Skirt Steak* 2012; Hochschild, *The Managed Heart* 1983; Sherman, *Class Acts* 2007; Wilson, *Front of the House, Back of the House* 2020; Jayaraman, *Behind the Kitchen Door* 2013; Zelizer, *The Purchase of Intimacy* | Candidate perspectives on women, labor and race in restaurants | verified-secondary except Druckman, Hochschild, Jayaraman and Zelizer (unverified this pass) |
| Gallaudet DeafSpace guidelines; Holmes, *Mismatch* 2018; Wong, *Disability Visibility* 2020 | Candidate access perspectives | verified-secondary; unverified; unverified |
