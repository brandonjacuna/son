<!-- Phase 2 working output, run wf_c7d3565a-a0f, 2026-09-28. Raw agent return, not reviewed line by line. The synthesis is research/starting-structure-2026-09.md. -->

# Sŏn module structure: starting proposal for Brandon

Status: a proposal for Brandon to decide on. Nothing here is decided. Titles, IDs and sequence stay proposals until `/identify` and `/ideate`.

**Citation keys.**
- **INT**: internal research, with conflicts C1 to C18 and questions Q1 to Q20.
- **PS**: external program structures, A1 to F6.
- **LE**: learning evidence, §1 to §9, plus design rules R1 to R22.
- **PL**: Trainual and scheduling, §1 to §8, plus hard constraints HC1 to HC13.
- **RL**: reading list, §1 to §7, plus tracks T1 to T8.

**Canon, cited and not restated.**
- White paper: Box `2466517057642` (WP).
- Brand and Experiential Guidelines: Box `2281626080747` (BG, v3.0 PDF).
- Newer Markdown copy of the guidelines: `2356731001214` (BG-md). Which Box copy is canonical is open (see 4.13).

**Standing flags.**
- Every role title is a `people.*` binding until the naming session in WP Part I, "Open items" (p.15) (INT C5).
- Any figure is a `fact.*` binding.
- Lineage (Coqodaq, Alinea, Gracious, Achatz) is flagged and never reconstructed.

---

## 1. Program map

### 1.1 Domains

I use the prefixes from `framework/module-spec.md`: ORI, SVC, BEV, KIT, SAF, SYS, LEA, CUL. The host track sits in SVC, because it is front-of-house hospitality.

**One new prefix is proposed: LIB (library: reading, listening, masterclass).**
- **Why a new prefix:** the reading tracks (RL §6, T1 to T8) are not craft modules.
  - They are finished by a proven conversation, not by passing a gate.
  - They never gate floor access.
  - They run long by design (LE §1; intake group 3).
  - Filing them under CUL or ORI would hide them among required content, and would put the wrong review panel on them.
- **Alternative:** keep them in CUL with a `track: library` tag. This is cheaper but loses the "never critical path" signal.

**No new prefix for movement drills.** Drills stay in their craft domain (SVC or BEV) and carry a `job: do-drill` tag. That makes the split between movement and decision visible without cutting the craft in two.

### 1.2 Structure: an activity tree, not a job ladder

**Nodes are activities, not job titles** (PS B2; LE §6; LE R15). Examples:
- "run food to a table on your own"
- "carry stemware on a tray at tempo"
- "hold a two-top alone"
- "work the bar well alone"
- "sign off another person's practical"

**A role is a bundle of nodes.** This lets one tree serve the ladder Brandon described (intake group 2) and the WP's strands (WP Part I, "The service team structure: complementary strands"; INT C3) until C3 is decided.

**Node states:**

| State | Meaning |
|---|---|
| locked | Not yet available. |
| open | Available to start. |
| in practice | Being worked on. |
| proven | Lit by evidence only: a passed gate, or a logged proven conversation. |
| recheck due | Proven, but due for a periodic practical or refresher. |

A node never lights up because content was completed (PS F1 to F3; LE §7; LE R18 and R19).

**Supervision levels on each node** (PS B1, B2):

| Level | Meaning |
|---|---|
| L1 | Observe. |
| L2 | Direct supervision. This is the angel shift. |
| L3 | Indirect supervision, with help on request. This is the prove-it shift. |
| L4 | Released. |
| L5 | May supervise others and sign off practicals. Leads only, after the LEA assessor path. |

### 1.3 Shared core (every front-of-house and beverage hire, and the host)

Everything here is Introduce level, critical path, and lean (LE §1, R1):

- ORI-001 Why before how
- ORI-002 Your map (tree and on deck reserve)
- ORI-003 How decisions get made here
- ORI-004 Using the support system
- ORI-005 How flavor works
- CUL-001 Taking part in pre-shift
- CUL-002 Giving and receiving critique
- CUL-003 Care as craft, and its cost
- SAF-001 Taking an allergy at the table
- SAF-002 Linked certifications and compliance

**Order within the core:** the "why" comes first (WP Part II, "Onboarding"; PS A6). Safety and linked certifications follow. Then the decision core.

### 1.4 Branches

**Service branch: food runner, then back waiter, then front server.** Front server and front waiter are one role (intake, confirmation after group 1).
- **Specialties:**
  - runner: the handoff, the path, the carry
  - back waiter: pour, clear and reset, supporting the section
  - front server: reading the table, describing, pacing, owning the table relationship (WP p.8, p.13; BG 15, "Floor authority")
- **Volume note:** runner and back waiter may merge into hybrid stations depending on volume. So the runner and back waiter nodes are shared, and only their station assignment is a `workflow.*` binding.

**Beverage branch: barback, then bartender and barista as one homogenous team** (intake group 1).
- **One "liquid craft" spine** (RL §4) covers temperature, dilution, texture, extraction, pour control and economy of motion.
- **Two specialty nodes** hang off it: espresso and milk, and bar build (the Codex root and family grammar).
- A bartender or barista is expected to open the other specialty over time. That is an in-branch unlock, not cross-training.
- The head of beverage owns house specs, with a dotted line over the bar team (`people.head_of_beverage`).

**Host branch: the bridge** (PS D1; intake group 2 clarification).
- **Own specialty nodes:** the threshold and arrival, reading the book and pacing the room, and reading the room.
- **Two adjacent unlocks:** the service entry node (runner) and the beverage entry node (barback). This makes the host the link in the chain between the two branches.
- **Door ownership is open.** Whether the host or the Maître d' holds the threshold (INT C6) is unresolved, so these host nodes are mostly bindings.

**Leads: lead food runner, lead server, lead bartender, lead host.** These are paid and promotable per the intake, and conflict with WP p.10 (INT C4).
- **Unlock requires:**
  - L4 on the home branch's core nodes
  - the LEA teaching path: LEA-001 Teaching at Sŏn, LEA-002 Assessing a practical (calibration), LEA-003 Running the angel shift
  - a co-rated audit period
- **Only then does a lead reach L5 and may sign practicals alone** (intake group 4; LE §5, R12 and R14; PS B4, C4).
- The lead's shift scope is an HR ruling (4.4).

**Management pair: Operations Manager and Maître d'.** Titles are `people.*` (INT C5). Who owns people and training is open (INT C1).
- **Shared management track:** assessing (LEA-002), the unblock conversation (LEA-006), running pre-shift (LEA-005), leading by example (LEA-007), last night into the library (LEA-008), and the talent-block workflow.
- **Split of focus.** Brandon's left-hand and right-hand split (intake group 1) becomes an elective emphasis:
  - Operations: systems, compliance, the rosters.
  - Maître d': the experience, recovery standards, the service culture.
- **They hire together**, so interviewer training (WP p.17 to 18, "Talent acquisition") sits on both paths.
- **This track needs little new content.** Its own content is mostly the LEA library plus bindings.

**Back of house: a chef-gated shell only.**
- `KIT` branch, with nodes to be named by the executive chef. Names conflict: steward vs porter, CDC, CDP, tournant (INT C17).
- The tournant is itself a chaining role (PS D1).
- A server learning the kitchen (WP Part II, "Training infrastructure") is a cross-branch unlock that waits on the chef.
- No KIT IDs are proposed.

### 1.5 Skill-tree layers

| Layer | What it holds | How it opens | Evidence that lights it |
|---|---|---|---|
| Shared tracks | Core (1.3) plus each branch's spine | Assigned at hire | Gate or proven conversation |
| Specialties | Role nodes within a branch | Open after the prerequisite node reaches L4 | The four gates (1.7) |
| Electives | LIB tracks; wine (linked to an external credential, PS C1); access; espresso for a bartender, bar build for a barista | Open to all after the core. Wine and beverage electives open after spine L4. | A proven conversation, logged by a lead (RL §6). No floor gate. |
| Cross-training unlocks | The adjacent node in the chain (PS D1): runner to back waiter to front server; barback to bar and espresso; host to runner or barback | After mastery (L4) in the home role (intake group 2; PS D3), plus an unblock conversation that records "learning or move" | The same four gates. Proven prior experience can shorten the path (PS B1). |
| On deck reserve | People proven on a node who have no open seat (intake group 2 clarification; WP p.14 "ready-now pool") | Automatic on L4 in a node outside the home role | Membership needs a home team, an orientation for each station they may cover, and a named contact on each shift (PS D2). Whether it ranks people for succession is open (INT Q4). |

### 1.6 Sequence

1. **Paid practical interview** (WP pp.17 to 18). This is designed together with gate 2 so it is not duplicated (PS B7).
2. **Remote onboarding, paid.** Its length is `workflow.onboarding_remote_length` (intake group 3). It covers the ORI and CUL core, SAF-002 enrolment, and the branch's Introduce modules.
3. **Movement drills on site**, with take-home kits where safe (4.5). They are spread across several short sessions (LE §4, R8).
4. **Gate 1, spoken knowledge check.**
5. **Gate 2, small-menu practical.**
6. **Gate 3, angel shift.**
7. **Gate 4, prove-it shift.**
8. **Node released (L4).** Reinforce modules follow, with spaced retrieval tied to shifts (LE §2, R2).
9. **Master modules, electives, and adjacent unlocks.**
10. **Lead path** (1.4).

### 1.7 Where the gates sit

Gates are set per node, not per job title. Gates 1 and 2 happen before any customer contact, which is Brandon's "test before impact" (intake group 4; PS B6 contrast).

**G1. Spoken knowledge check** (intake group 4)
- **Where:** off the floor, after the node's Introduce modules and retrieval sets.
- **Form:** set cases, an anchored rubric, and either a second calibrated rater or enough separate cases (LE §5, R11). Content is scored, not fluency of talk (R13).
- **Recorded:** see 4.2.

**G2. Practical with a small menu** (intake group 4)
- **Where:** off the floor, or in a mock setting. It follows G1.
- **Form:** a simulated service at the table. Macro movements and decisions are combined here for the first time (LE §4, R7). The analog is the sommelier service practical (PS C1).
- **Recorded:** peer plus manager until the peer is at L5.

**G3. Angel shift** (Brandon's term; confirm it, PS B6)
- **Where:** the first live shift.
- **Form:** direct supervision at L2. The trainer personally observes. The trainee is extra to scheduled staffing (`workflow.angel_shift_staffing`, PS B1). Coaching tapers off as the shift goes (PS C6).
- **Recorded:** the trainer attests. Reflection time after the shift is part of the gate (PS B4).

**G4. Prove-it-to-your-team shift** (intake group 4)
- **Where:** the second live shift.
- **Form:** indirect supervision at L3, help on request. Using support well is assessed as a trust condition (PS B2).
- **Team feedback is formative only.** Each teammate answers one shared global question, task-focused, collected privately, and a lead synthesizes the answers (PS B3; LE §6, R16).
- **It is never a vote.** The release decision stays with the calibrated raters.
- **Recorded:** calibrated rater(s) plus a CEO override path. An override goes up a step to Brandon.

**Periodic practical and refresher** (intake group 4; PS A4)
- **Where:** after release, on a cadence bound as `workflow.recheck_cadence`.
- **Form:** a short G1 plus G2 on site, in pre-shift early-arrival windows (`workflow.refresher_window`).
- **Recorded:** as for G1 and G2.

**Assessor release** (LE §5, R12 and R14; PS B4)
- **Where:** at the lead's move to L5.
- **Form:** frame-of-reference calibration, then co-rated audits.
- **Recorded:** a manager co-signs until release.

**Management co-rater rule.** A manager co-rates in any of these cases, whatever the peer's level (LE §5):
- gates to the customer, while the peer is uncalibrated
- ratings near the cut line
- close relationships between rater and candidate

---

## 2. Candidate module list

**Column keys.**
- **Slot:** I = Introduce, R = Reinforce, M = Master.
- **CP** = on the critical path; keep it lean (one objective, one learning job; LE R1).
- **Build now** = durable craft content, writable today.
- **Mostly bindings** = waits on tools or workflows; park as `identified`, per `framework/bindings.md`.

The needs below are anticipated gaps. Sŏn has not opened, so each one is confirmed at `/identify`.

| ID (proposed) | Title | Need (observed gap) | Domain | Slot | Learners | Build status | Notes |
|---|---|---|---|---|---|---|---|
| ORI-001 | Why before how | New people learn mechanics without the reason, so they bend the standard under pressure | ORI | I, CP | All | Build now | Seed, kept (§3) |
| ORI-002 | Your map: the tree and the on deck reserve | New people cannot see how to advance or unlock, so they wait to be asked | ORI | I, CP | All | Mostly bindings | Durable: how progression works. Bound: `founder.unlock_rule` (C2), `tool.map.*` (4.1) |
| ORI-003 | How decisions get made here | Team members escalate or freeze on calls Brandon would make on the spot | ORI | I, CP | All | Build now | Built from Brandon's Critical Decision Method interviews (LE §8, R20). Waits on the interviews; lineage incidents flagged |
| ORI-004 | Using the support system | New people hide uncertainty instead of asking, most of all on early shifts | ORI | I, CP | All | Build now | Humility as an assessable trust condition (PS B2). Feeds G4 |
| ORI-005 | How flavor works | The team repeats flavor myths and describes taste as fact | ORI | I, CP | All FOH, BEV, host | Build now | RL §2, "Teach" rows only. Wansink never. "Psychotaste" as house label only |
| CUL-001 | Taking part in pre-shift | Team members treat pre-shift as announcements, so retrieval and error-raising do not happen | CUL | I, CP | All | Build now | Seed, split (§3). Format team-gated |
| CUL-002 | Giving and receiving critique across roles | People hold back from naming another role's mistake, or aim critique at the person rather than the task | CUL | I, CP | All | Build now | TBRI. Structural protocol (RL §1.3; LE §6). Includes a "reading a teammate" see-it drill (RL §1.3) |
| CUL-003 | Care as craft, and its cost | People treat depletion as private failure and care as a trait they lack | CUL | I | All | Build now | RL §1.1. Cites WP Part II, "The cooling system" |
| CUL-004 | Receiving someone who floats in | Reserve members get treated as outsiders on a borrowed shift | CUL | R | All, leads | Build now | PS D2 |
| SAF-001 | Taking an allergy at the table | Allergy routing depends on a server judging severity | SAF | I, CP | All FOH, BEV, host | Build now | Seed, kept. Matrix is `chef.*`. Feeds G1 |
| SAF-002 | Linked certifications and compliance | Certified and compliance content does not exist in-house and must be linked and tracked | SAF | I, CP | All, by role | Mostly bindings | Not written by us (intake group 1). `tool.compliance.*`, `tool.lms.premium_courses` (PL §7) |
| SVC-001 | Getting to table-ready | Learners cannot say what ready looks like, or which gate comes next | SVC | I, CP | Runner, back waiter, front server, host | Build now | Seed, reframed as the gate module for G1 and G2. Menu content `chef.*` |
| SVC-003 | Tray and stemware carry (drill) | New runners carry with tension and eyes on the tray, not the room | SVC | I, CP | Runner, back waiter, front server, barback | Build now | Movement drill, at tempo, several short sessions. On site (intake group 5) |
| SVC-004 | Moving through the room (drill) | New people cross the room in ways that block sightlines and paths | SVC | I, CP | All FOH, host | Mostly bindings | Cite BG 13 "Cross-zone governing principles" and BG-md 06. Layout unsettled (BG 13 "Pre-CD open items") |
| SVC-005 | The handoff at the table | Runners hesitate at the table over who receives what | SVC | I, CP | Runner, back waiter | Mostly bindings | Position and pass workflow are `workflow.*`. Plating is chef-gated |
| SVC-006 | Reading the table | Servers miss cues until they become requests | SVC | I then R | Back waiter, front server, host, bartender | Build now | See-it modalities. Cite BG 03 "Jeong and Nunchi" and BG 05 personas (calibrate, never constrain) |
| SVC-007 | Service decisions: compare with the expert | On ambiguous tables, servers decide differently from Brandon | SVC | R then M | Back waiter, front server | Build now | ShadowBox-style bank from the decision interviews. Panel-keyed SJT check (LE §8) |
| SVC-008 | Describing honestly | Descriptions oversell or pronounce, and so shape the customer's taste dishonestly | SVC | R | Front server, host, bartender, barista | Build now | RL §2 (price and color studies, framed as ethics). Menu terms `chef.*` |
| SVC-002 | Recovering a mistake well | Recovery is improvised, and gestures go beyond or fall short of what the house authorizes | SVC | R | Back waiter, front server, bartender, host | Build now | Seed, kept. Range bound `founder.recovery_range` (C11) |
| SVC-009 | When a customer crosses a line | Staff absorb mistreatment alone because the house response is undefined | SVC | I | All | Build now | Durable: the house owns the response. Bound: `founder.mistreatment_policy`, `workflow.escalation.mistreatment` (RL §1.3) |
| SVC-010 | The threshold and arrival | New hosts improvise the first moments of the customer's arrival | SVC | I, CP | Host, lead host, Maître d' | Mostly bindings | C6 open. Cite BG 13 "Threshold", BG 15 "Arrival choreography" |
| SVC-011 | Pacing the room from the book | Hosts seat by availability, not by the room's pace | SVC | I then R | Host, lead host | Mostly bindings | `tool.reservations.*`. Includes who sets protocol flags (INT Q19) |
| SVC-012 | Access at the table and in the room | Staff are unsure how to serve customers with sensory or mobility needs without assumptions | SVC | R | All FOH, host | Build now | RL §5 access sources, once verified |
| BEV-001 | Liquid craft: temperature, dilution, texture, extraction | Drinks drift when conditions change because the maker lacks the why | BEV | I, CP | Barback, bartender, barista | Build now | Shared spine (RL §4, *Liquid Intelligence* as the why layer). High-hazard techniques go to SAF |
| BEV-002 | Pour control (drill) | New makers pour with an unsteady stream and wasted product | BEV | I, CP | Barista, bartender, barback; back waiter and front server optional | Build now | Brandon's water-pitcher drill (intake group 5). Take-home kit option (4.5) |
| BEV-003 | Station and body (drill) | Makers reach, bend and cross over, and slow under tempo | BEV | I, CP | Barback, bartender | Build now | Economy of motion (RL §4, Ellis: vendor features only). Layout `workflow.bar.station_layout` |
| BEV-004 | Milk: steam and pour (drill) | Texture and pour vary drink to drink | BEV | I, CP | Barista; bartender on unlock | Build now | SCA-style isolated movements (PS C3, lead-only). Equipment `tool.bar.equipment` |
| BEV-005 | Root drinks and their families | Makers memorize specs but cannot adjust or build a variation | BEV | I then R | Bartender; barista by analogy | Build now | Core, balance and seasoning grammar. House specs `people.head_of_beverage`. Whether they are chef-gated is a founder call |
| BEV-006 | Dialing in espresso | Baristas follow a recipe and cannot correct drift | BEV | R | Barista; bartender on unlock | Build now | Brandon's own batch coffee and matcha method (WP p.4) is founder- and chef-gated |
| BEV-007 | Barback flow and restock | Wells run short at peak because restock is reactive | BEV | I, CP | Barback | Mostly bindings | Par levels and layout are `workflow.*` or `fact.*` |
| BEV-008 | Tasting and describing | The beverage team pronounces rather than describes | BEV | R | Bartender, barista; servers as elective | Build now | Retronasal technique, judge-inconsistency humility (RL §2) |
| BEV-009 | Beverage decisions: compare with the expert | Beverage calls diverge from how Brandon or the head of beverage would decide | BEV | R then M | Bartender, barista | Build now | From the decision interviews |
| BEV-010 | Wine (elective) | Beverage and service staff who want wine have no path | BEV | M, elective | Bartender, barista, front server | Mostly bindings | External credential linked (PS C1). House list bound |
| SYS-001 | The tools by role | People learn the POS and other tools by trial on shift | SYS | I, CP | All, by role | Mostly bindings | Park as `identified` (`framework/bindings.md`) |
| SYS-002 | Using the learning system | Learners do not know how to flag content, see their map, or get a practical booked | SYS | I, CP | All | Mostly bindings | `tool.lms.*`, `workflow.gate_autoschedule` |
| LEA-001 | Teaching at Sŏn | Peers who teach default to "watch me" and never fade support | LEA | M | Candidate leads, leads, managers | Build now | Seed, split (§3). Structured OJT (LE §3, R5; PS C6) |
| LEA-002 | Assessing a practical | Raters score the same performance differently, and reward fluency over content | LEA | M | Candidate leads, leads, managers | Build now | Frame-of-reference calibration, bias (LE §5). Prerequisite for L5 |
| LEA-003 | Running the angel shift | Trainers trade observation against coverage and skip the reflection | LEA | M | Leads, managers | Build now | PS B1, B4. Staffing bound |
| LEA-004 | Writing a module | New authors skip the five moves, write tool steps as fact, and fragment the voice | LEA | M | Approved authors (founders first) | Build now | Unlocked by assigned request (intake group 6) |
| LEA-005 | Running pre-shift | The teaching slot collapses into announcements when time is short | LEA | R | Leads, managers | Build now | Operational half is `workflow.*`. Format team-gated (intake group 3). One shared topic across the house (PS A1) |
| LEA-006 | The unblock conversation | Requests to learn or move stall, or end without clear expectations | LEA | R | Managers, leads | Build now | "Learning or move" (intake group 2). Scheduling bound |
| LEA-007 | Leading by example | Leaders police behaviors they do not model | LEA | M | Leads, managers | Build now | RL §1.2. Owning past harm |
| LEA-008 | Last night into the library | What the floor learns on a shift is lost | LEA | M | Leads, managers | Build now | Case-from-last-night, codify (RL §3, elBulli) |
| LEA-009 | Leading your position on a shift | New leads are unsure where lead scope ends and management begins | LEA | I | Lead runner, server, bartender, host | Mostly bindings | Scope is an HR ruling (4.4). `people.*` titles |
| LIB-001 to LIB-007 | Reading tracks T1 to T7 | People who want depth have no path, and no one hears what they learned | LIB | Elective | All, by interest | Build now | Discussion guides only. Unverified sources are read before inclusion (RL §5). T5 carries the Achatz lineage flag |
| LIB-008 | House masterclass (listening) | Founder and partner conversations are lost to the team | LIB | Elective | All | Mostly bindings | `workflow.recording_consent`. Audio is untracked (PL §6) |
| KIT (shell) | Back-of-house branch | Chef-defined | KIT | Chef-gated | Chef-defined | Chef-gated | No IDs until the executive chef is engaged |

**Lean critical path, by role.** Each role's path is the shared core, then the branch's I-slot CP drills and decisions, then G1 to G4.

| Role | Branch modules on the critical path |
|---|---|
| Runner | SVC-001, SVC-003, SVC-004, SVC-005, SYS-001 |
| Back waiter | adds SVC-006 and BEV-002 via adjacent unlock |
| Barback | BEV-001, BEV-002, BEV-003, BEV-007 |
| Barista | BEV-001, BEV-002, BEV-004 |
| Bartender | BEV-001, BEV-002, BEV-003, BEV-005 (I) |
| Host | SVC-001, SVC-004, SVC-010, SVC-011 |

---

## 3. The six seed modules

| Seed | Call | Reason |
|---|---|---|
| ORI-001 Why before how | **Keep** | Supported by WP Part II, "Onboarding" (p.18), and PS A6. Keep it lean and on the critical path. Add care as craft, not temperament (RL §1.1). Re-cite `source` to WP Box `2466517057642`, p.18, instead of V7 through profiles (INT Q20). |
| LEA-001 Teaching at Sŏn | **Split into three** | The seed bundles three jobs with different learners and gates: (1) LEA-001 teaching on the floor, meaning structured OJT and fading; (2) LEA-002 assessing, meaning calibration, the prerequisite for L5; (3) LEA-004 authoring, which is founders only at first and unlocked by request (intake group 6; INT C9). Trainer and assessor training is the active ingredient in the external models (PS B4, C4). Authoring is a separate gate. The WP's "paid to teach" line sits with 4.12. |
| SVC-001 Getting to table-ready | **Keep, reframed** | It becomes the gate module for the service and host branches. It says what ready looks like per activity node, and prepares for G1 and G2. G3 and G4 are run through LEA-003 facilitator guides. The WP says "No one touches a table until they are actually ready" but not what ready is (INT §1). This module is where "ready" gets defined. The beverage branch gets its own gate module only if the per-node criteria differ enough; otherwise SVC-001 covers both through `learners`. |
| SVC-002 Recovering a mistake well | **Keep, narrowed** | Recovery craft is durable. The gesture range is unresolved between WP p.13, WP p.26, BG 15 and BG-md 08 (INT C11). Bind it as `founder.recovery_range`, with any threshold as `fact.*`. Move mistreatment by a customer to SVC-009: that is a different problem, and its policy is founder-gated and HR-gated. |
| SAF-001 Taking an allergy at the table | **Keep** | This is a safety floor and a G1 component. The matrix is `chef.*`. Build the routing principle now. Assessment and chef seats are still required before `parked`. |
| CUL-001 The pre-service brief | **Split** | Two learners and two objects. CUL-001 keeps the learner's side: retrieval call-and-response, raising errors, the team-making ritual. LEA-005 takes running the brief, with the operational half (86s, allergies, VIPs, gaps) as `workflow.*` bindings. Pre-shift teaching does not count toward progression (intake group 5), so neither half is a gate. Format and timing are team-gated (intake group 3). |

---

## 4. Open system-design questions

Each question lists options and tradeoffs. Gate marks: F = founder-gated, T = team-gated, HR = HR seats.

**4.1 Presenting the skill tree, given that Trainual shows only lists (PL §5, HC1, HC2)**
- **(a) External live page reading Trainual completions through the API.**
  - For: a personal tree, which is closest to "presented as much as possible".
  - Against: needs API access, which is unresolved between tiers (PL §3), plus hosting and auth. It records nothing inside Trainual.
- **(b) Static map subject in Trainual plus a printed back-of-house wall map.**
  - For: cheap and socially visible, which suits pre-shift.
  - Against: not personal, and updates are manual.
- **(c) SCORM map.**
  - Against: generic, cannot read the learner's progress, and every change means a re-upload.
- **In every option,** nodes light on evidence only. Trainual streaks and leaderboards stay off unless Brandon decides otherwise (PL §1; LE R19; `tool.lms.gamification_setting`, F).

**4.2 How gates are recorded and who signs (PL §2, HC3)**
- **(a) Admin+ marks the gate complete in Trainual.**
  - For: native.
  - Against: hourly leads would need Admin+ rights (a compliance risk, HR), and the record does not name the assessor.
- **(b) External form as the record** (`tool.forms.gate_record`), then automation assigns the next subject, then an Admin marks it.
  - For: names every rater and holds the rubric.
  - Against: the record lives outside the LMS.
- **(c) Learner-kept, co-signed practice record, carried in the form** (PS C4).
  - For: platform-neutral and portable, and it can carry Open Badges-style criteria and evidence (PS F4).
- **Signers under every option:**
  - peer plus manager until the peer reaches L5
  - a lead alone after calibration and audits
  - override goes up to the CEO (intake group 4)
- The system choice is `founder.gate_record_system` (F).

**4.3 Fail limit and retries (T; intake group 4)**
- **(a) A fixed number of attempts per gate, then a coaching plan and a conversation** (PS A4).
  - For: clear.
  - Against: a hard stop can feel punitive to the TBRI seat.
- **(b) No attempt count.** A required interval between attempts plus a changed practice plan; repeated misses trigger an unblock conversation about fit.
  - For: fits spacing (LE §2) and dignity.
  - Against: open-ended cost.
- **(c) Scoring rule, separate from (a) or (b): pass every part in one sitting** (PS C1) **or bank parts that are passed.**
  - One sitting is more rigorous. Banking suits the split between movement and decision.
- The count and interval are `fact.*` or `workflow.*`.

**4.4 Hourly positional leads running practicals (HR; intake group 4; LE §5 compliance flag)**
- **(a) Leads co-rate; a manager holds the decision.**
  - For: safest on compliance.
  - Against: management bandwidth becomes the bottleneck, and at opening this is certain (PS E2).
- **(b) Leads sign alone after calibration,** inside scheduled paid time, with no supervisory authority over discipline or pay.
  - For: matches Brandon's peer-led intent.
  - Against: needs an HR ruling that rating is not managing.
- **(c) A separate paid certified-trainer rung, distinct from lead** (PS A4).
  - For: cleaner role line.
  - Against: adds a rung and may conflict with WP p.10 (INT C4).

**4.5 Paid take-home practice versus on-the-clock learning (HR, F; intake groups 3 and 5; LE §4, R9)**
- **(a) All drills on site and paid.**
  - For: simplest, and fully consistent with "always paid".
  - Against: uses paid floor time, which Brandon wants to limit.
- **(b) Take-home kits with a bound paid practice allowance** (`fact.take_home_allowance`), a video exemplar, a self-rating, and a scheduled check-in.
  - For: spaced reps at home improved retention in surgical trainees (LE §4).
  - Against: adherence in a paid hourly setting is unknown, and time tracking is needed.
- **(c) Take-home kits as unpaid optional practice.**
  - Conflicts with the intake's "always paid" and carries wage-law exposure. Listed for completeness; not recommended.

**4.6 The unblock conversation and self-scheduling (PL §3, §4, HC6; intake group 2)**
- **(a) Learner books.** A trigger sends a single-use Calendly link for the talent-block event.
  - Against: the learner still has to act.
- **(b) Nobody books.** A trigger books the first open talent-block slot through the scheduling API.
  - For: closest to "it just appears".
  - Against: needs a paid plan and custom automation. Pooled scheduling is unverified.
- **(c) Trainual "Request" access.**
  - Against: the request routes to Admins, not to leaders. Weakest option.
- **In every option,** the conversation records "learning or move", sets expectations, and ends in one of four states: elective open, adjacent unlock, reserve membership, or not now with a reason (LEA-006).
- Talent block length and count are `workflow.talent_block`. Assessor pairing is `workflow.assessor_pairing`.

**4.7 Measuring decision alignment and detecting complacency (intake group 7; LE §8, §9)**
- **(a) Agreement with an expert panel on scenario and SJT items, tracked over time.**
  - Anchored on Brandon's decision-interview rationale, widening to calibrated leads.
  - Items where the panel disagrees become discussion cases.
  - Against: a single-source risk while the panel is one person.
- **(b) Behavior-level evidence.** Observation on the floor, plus success-case interviews (LE §9, Brinkerhoff) inside the weekly review window (`workflow.post_launch_review_window`).
  - For: this is what `measured` requires.
  - Against: costs leader time.
- **(c) A signal watchlist.**
  - Positive signals: voluntary practical requests, errors raised in pre-shift, cross-role critique.
  - Complacency signals: completion with no later requests, uniform ratings with no spread, the same few voices answering.
  - These are prompts to investigate, never targets (LE R22).
- (a) plus (b) is the proposal. (c) is a supplement.

**4.8 Module length rules (LE §1)**
- **(a) One objective and one learning job per critical-path unit.** No time target. Off-path long-form is unrestricted.
- **(b) Time caps per unit.**
  - Against: a cap is a figure, and there is no evidence it is better than an objective rule.
- **(c) As (a), plus a required retrieval schedule on every critical-path unit** (LE R2, R3).
- **Proposal: (c).**

**4.9 Review cadence and volatility tagging (intake group 6)**
- **(a) Date-based reminders from the creation date,** in ClickUp, as Brandon asked. Trainual's native content verification reminders are an alternative (PL §8).
  - Against: blind to what actually changed.
- **(b) Volatility tags derived from binding namespaces at `drafted`.** Rough ranking: `tool.*` and `fact.*` high, `workflow.*` and `chef.*` medium, durable content low. Change events in a tool or workflow trigger review of every dependent module through the bindings registry.
- **(c) Both.** Date-based as a floor, tag-based on change.
- **In every option,** a learner flag creates a review task. Trainual's content flag is not a Zapier trigger, so the fallback is an embedded form (`tool.forms.content_flag`, PL §8).

**4.10 How external and Trainual compliance content links in (intake group 1; PL §7, HC10)**
- **(a) Trainual Premium courses add-on,** for what it covers (harassment prevention, workplace safety).
  - For: native tracking.
  - Against: an add-on cost, bound as `fact.*`.
- **(b) Outside provider through an external link, with the certificate uploaded.** Food handler and alcohol service are not confirmed in Trainual's catalog.
  - Against: completion is self-reported unless an Admin verifies it.
- **(c) Provider SCORM.**
  - Only if Sŏn holds rights to the content (PL §7).
- **In every option,** these are catalog rows of type "linked": no durable content, never re-taught (standing rules, "Scope").

**4.11 Whether the lifecycle and review panels need changes**
- **Option A, minimal:** add catalog row types only.
  - `linked`, which skips designed, drafted and reviewed.
  - `library`, completed by proven conversation, with a light panel.
  - `gate-spec`, per-node gate criteria reviewed by the Assessment seat.
- **Option B, moderate:** A, plus these changes:
  - volatility tags and a retrieval schedule become exit criteria at `drafted`
  - the post-launch review window becomes a `workflow.*` hold between `published` and `measured`
  - TBRI is added to every module with team feedback
  - Organizational Systems Architect is added to every module that changes a tree node
- **Option C:** B, plus a new `calibrated` checkpoint on rater-facing LEA modules before any L5 release.
- **Proposal: B.** A leaves gates unreviewed. C may be overbuilt before any lead exists.

**4.12 Other decisions this map depends on, from the research (F unless marked)**
- **People ownership (INT C1).** Who owns the module system, sign-off rosters and talent blocks: the Maître d' (WP p.10) or the operations role (intake group 1)?
- **Unlock rule (INT C2).** Time in role, demonstrated mastery, or time as a floor with mastery as the gate?
- **Strands or ladder (INT C3).** Decides whether the tree shows altitude or adjacency.
- **Leads (INT C4).** Promotable positions or per-shift designations?
- **Pay for modules completed (WP Part II, "Training infrastructure"; INT C8; PS F; LE §7, R18).** The evidence favors paying for demonstrated mastery and teaching, not completion.
- **Mentor vs angel-shift trainer (INT C18).**
- **Private post-mortems vs the open prove-it shift (INT C14).** Designed as different rituals. TBRI review.
- **AI presenters in internal video under BG 07 (INT C7).** Needs an explicit canon carve-out.
- **Teaching the Korean terms under BG 09, "Rule 2 · No translation" (INT Q14).**
- **Daypart scope (INT C12).**
- **Late-night trigger owner (INT Q18).**
- **Which Box copies of the white paper and guidelines are canonical (INT, PL, RL §0).** `canon/pointers.md` still points to ClickUp.

---

## 5. Job descriptions generated from the path

**Mechanism: one role manifest per role is the source for three outputs.** The outputs are the job description, the tree view, and the transparency sheet (WP pp.17 to 18, "Talent acquisition"; INT Q17). They are never written separately.

**The manifest.** Proposed as `catalog/roles/<role>.yaml`. It lists:
- `people.*` title binding
- `people.*` reporting line
- the node list, with each node's module IDs and transfer goals ("on their own, a person can ...")
- the entry node and the paid practical interview
- the supervision level required for release
- electives open to the role
- adjacent unlocks (the chain)
- the lead path

**Rendering.** A script (proposed) builds the job description from the manifest:
- **Purpose:** the role's line from WP p.10 to 11, cited by label and not restated.
- **What you will do:** the L4 transfer goals of the role's nodes.
- **How you get there:** the gates and the training plan, with pay dates bound as `fact.*` or `workflow.*`.
- **Where it leads:** adjacent unlocks, the on deck reserve, the lead path.
- **Pay and benefits:** `fact.*` from Airtable only.

**Why this works.**
- Every responsibility in a job description traces to a transfer goal someone can be assessed on. A job description cannot promise what the program does not teach, and a module added to a node updates the job description on the next render.

**Gates.**
- Titles wait on the naming session (WP p.15).
- KIT roles are chef-gated.
- Lead and management job descriptions need the HR rulings in 4.4 and INT C1 and C4 before rendering.