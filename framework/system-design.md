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
- Question 22 (teaching the Korean terms): this ruling points to option (a), training may explain the terms in full. To be confirmed with Brandon when question 22 comes up.

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
