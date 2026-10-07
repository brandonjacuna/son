# 03 — Fundraising

Covers the fundraising items in the current design: the **Investor CRM** list (replaces the earlier **N2** "Investors" design below it) and the optional, later **N3** (Fundraising & Runway Dashboard). ClickUp-native throughout — no fallback needed for either. Every step below is tagged **[You]** (UI-only, click-path given) or **[Claude]** (this session's ClickUp MCP / REST, once a build session starts).

**Design change (2026-09-17):** the original N2 plan below — a list called "Investors," seeded by *linking* to the ~45 Punch List investor tasks while those tasks stayed in the Punch List — is **replaced**. Per DECISIONS.md (2026-09-17), investor work doesn't belong in the Founding Punch List at all: approved investor tasks **migrate out** of the Punch List into a proper CRM record. This also **removes the "Investors" Punch List Phase view** and the "Related Punch List Tasks" relationship field (02 §4–5) — neither exists anymore.

---

## N2 — Investor CRM list (current design, DECISIONS 2026-09-17)

### What it is

A list, **Investor CRM**, sitting beside Founding Punch List directly in the Founding Sŏn space (no folder — matches the Punch List's own pattern). Default task type **Investor** (id 1027, 02 §1). One task = one investor or lender relationship, person or firm. Follow-ups (e.g. "Send investor packet") are **subtasks** under the investor record, not separate Punch List tasks — there is no longer a companion action-item list for fundraising work.

### N2.1 — Create the list

- **[Claude]** `clickup_create_list` in the Founding Sŏn space (id `90138396180`), name **"Investor CRM"**, sibling to Founding Punch List — no folder. Default task type **Investor**.

### N2.2 — Status template = Stage

Use the list's native **Status** field as Stage — the ClickUp-native mechanism for a single-select pipeline position, driving board view, the dashboard's pipeline-by-stage card, and every filter for free.

Approved statuses (DECISIONS 2026-09-17; open → closed):

`Prospect → Contacted → Meeting Scheduled → Diligence → Soft Commit (active) · Passed (done) · Committed (closed)`

- **[You]** ~5 min: List Settings → Edit Statuses on the new Investor CRM list → build the template above.

### N2.3 — Custom fields (Claude/REST)

Field creation is **[Claude/REST]** via `POST /v2/list/{id}/field`, using Brandon's personal API token — confirmed creatable this way (decision, 2026-09-16).

| Field | Type | Notes |
|---|---|---|
| Organization | Text | Firm/fund name, if any (blank for individual angels). |
| Email | Text (or Email type if available) | |
| Phone | Text | |
| Investor Type | Dropdown | Angel/Individual, Family Office, Fund, Lender, Strategic Partner. |
| Check Size | Currency | Target range for this investor/lender. |
| Committed Amount | Currency | 0 until Soft Commit/Committed. Feeds the dashboard's Committed vs Target card, if built. |
| Intro Source | Text | Who/what led to this relationship. |
| Last Contact | Date | Set manually after each interaction. |
| Next Follow-up | Date | Set manually — the follow-up trigger. Drives the Follow-ups Due view. |
| Related Meetings | Relationship → Meetings list | See §N2.4. |
| Created By Notes | *(reuse — the renamed "Notes from BJAC" field, not a new field)* | Free-text notes; no separate Owner or Owner Notes field exists (02 §3). |

### N2.4 — Related Meetings relationship

One Relationship field, **Related Meetings**, on the Investor CRM list, scoped to **"Tasks from a specific List"** → the **`Meetings` list in the Meetings space** (01 §1.2, already built). A Relationship field's list binding is permanent once set. Name the automatic reciprocal column on the Meetings list **`Investor`** — this is the single field pair 01 §1.3 refers to; do not create a second Relationship field from the Meetings side.

- **[Claude/REST]** create the field once the Investor CRM list exists (the Meetings list already does).

### N2.5 — Views (Claude/REST)

- **Pipeline board** (default) — grouped by Status.
- **Table** — all fields visible.
- **Follow-ups Due** — filter: Next Follow-up is today or overdue.
- **Committed** — filter: Status = Committed.

### N2.6 — Migration from the Founding Punch List (preview + approval, replaces the old "link, don't migrate" N2.5)

The audit (audit/founding-son.md) groups roughly 45 Punch List tasks/subtasks as "Investors & fundraising" — the `investor`-tagged cluster plus named-individual outreach tasks (Robby Grubbs, Robert Jacob Lerma, Brett Morgan, Adam Biechlin, Chris St. Peter, Doug Zell, Chris Null, David Tapia, Kevin Fink, Basu, Anthony/Jimmy, John Heffington, and others). None of these are Scaling People tasks.

1. **[Claude]** preview table: each candidate task → proposed Investor CRM record (new or existing) → destination (an Investor CRM record, a follow-up subtask under one, or **stays in the Punch List** if it's general fundraising collateral work rather than relationship work — e.g. "Create Pitch Deck 1.0").
2. **[You]** (Brandon) reviews and approves the exact list (decision #9's preview-table gate) — the audit's grouping is directional (task names, not a database query), so a few tasks may need manual re-homing.
3. **[Claude]** creates/updates the approved Investor CRM records, migrates the approved tasks (subtasks become follow-up subtasks under the matching record), and verifies field/status values carried over correctly.
4. **[Claude]** `clickup_remove_tag_from_task` strips `investor` from every migrated task, once its migration is confirmed.
5. **[You]** confirms the tag is unused in **Space Settings → Tags** and deletes the tag definition.

### N2.7 — How investor meetings link to it

Once an Investor/Lender meeting occurs (Meeting Type = Investor/Lender, 01 §1.3, already built):

1. Every Investor/Lender meeting task gets its **Investor** field (the reciprocal of Related Meetings, §N2.4) set back to the relevant Investor CRM record.
2. The approved investor-meeting template ("agent prep brief from the investor's history, link to the investor record, materials-sent log, and a follow-up email drafted for review") reads the Investor CRM record directly — prep brief pulls Stage, Last/Next Contact, and the rollup of prior meetings from that one task, a single source of truth instead of re-entering history per meeting. (This part of the agent's job is paused during the no-AI/no-credits window, PLAN-2026-09-17-no-ai.md.)
3. After each Investor/Lender meeting, **Last Contact** updates on the Investor CRM record (manual) and **Next Follow-up** is set.

---

## N3 — Fundraising & Runway Dashboard

### What it is

One native ClickUp Dashboard, **"Fundraising & Runway"** — optional, later (DECISIONS 2026-09-17) — built entirely from cards reading the Investor CRM list and the Meetings space. Confirmed native, zero AI credits (V8, research/12). No Goals object yet — DECISIONS keeps metrics to "fundraising pipeline only, for now," and the backlog explicitly holds a Goal-based progress bar for later, once the CRM has real data.

### N3.1 — Cards (optional, later — DECISIONS 2026-09-17)

| Card | Type | Source | Manual or calculated |
|---|---|---|---|
| Pipeline by Stage | Pie or Bar chart, grouped by Status | Investor CRM list | **Calculated** — live off Status. |
| Committed to Date | Calculation card (sum) | Investor CRM → Committed Amount | **Calculated** — sums automatically as Committed Amount is entered. |
| Committed vs Target | Calculation card, or manual progress note in the dashboard description, until a Goal exists | Committed to Date vs a target figure | **Hybrid** — the sum is calculated; the target number is typed in once as **$2,500,000** (decision #20; no Goal object yet, per DECISIONS). Revisit as a Goal-based progress bar once the CRM is populated (backlog item, research/12 §2.2). |
| Follow-ups Due | Task list card, filtered: Investor CRM, Next Follow-up ≤ today (or ≤ 7 days) | Investor CRM list | **Calculated** filter — **manual** input (someone has to set Next Follow-up after each touch for this to mean anything). |
| Stalled Relationships | Task list card, filtered: Investor CRM, Status not in {Committed, Passed}, Last Contact > 21 days ago | Investor CRM list | **Calculated** filter — depends on manually-updated Last Contact. |
| Check Size by Stage | Bar chart | Investor CRM → Check Size, grouped by Status | **Calculated.** |
| Recent Investor Meetings | Task list card, filtered `Meeting Type = Investor/Lender`, sorted by due date desc | Meetings space → `Meetings` list | **Calculated**, via the Related Meetings/Investor relationship (§N2.4, already built). |

Dropped from the original draft: a Materials Sent Tracker and an "Open Follow-up Tasks via rollup" card — the Investor CRM has no Materials Sent field and no Related Punch List Tasks relationship (follow-ups are subtasks under each record now, visible directly on the record, not via a rollup).

### N3.2 — Build steps

- **[You]** Workspace sidebar → **Dashboards** → **+ New Dashboard** → name "Fundraising & Runway" → add each card above via **+ Add Card**, pointing every card's source at the Investor CRM list (and Meetings). Dashboard card creation and filter configuration is UI-only — there is no MCP/API surface for it (V4).
- **[Claude]** Nothing to build here directly; N3 is entirely a [You] step, optional and later, once the Investor CRM has real data.

### N3.3 — What's manual vs calculated, summarized

**Fully calculated, no upkeep:** Pipeline by Stage, Committed to Date, Check Size by Stage — these read fields that are already required for the pipeline to function.

**Calculated shell, manual fuel:** Follow-ups Due, Stalled Relationships — the cards themselves need no maintenance, but they're only as good as Brandon/Dominic keeping Last Contact and Next Follow-up current on each Investor CRM record after every interaction. This is the dashboard's real dependency, not a ClickUp limitation.

**Manual by design (no ClickUp object holds it yet):** the fundraising target figure for Committed vs Target — **$2,500,000** (decision #20) — there's no live number ClickUp can pull for "how much are we trying to raise," so it's typed once and updated as the round is repriced, until a Goal object is added later.

---

## Open questions and risks

1. **RESOLVED, superseded:** the six-stage pipeline is now `Prospect → Contacted → Meeting Scheduled → Diligence → Soft Commit (active) · Passed (done) · Committed (closed)` (DECISIONS 2026-09-17, replacing the earlier Prospecting/Committed-Passed-both-closed draft).
2. **RESOLVED:** the Investor CRM ↔ Meetings relationship (§N2.4) is already built, since the Meetings list landed first (01, ✅ DONE 2026-09-16). No sequencing risk remains.
3. **Migration mapping is directional, not exact** — the ~45-task investor cluster came from a full manual read of task names (audit/founding-son.md), not a query; a handful of tasks may land on the wrong Investor CRM record and need a manual fix after migration (decision #9's preview-table gate covers this).
4. **RESOLVED (#3):** Brandon's personal ClickUp API token moved field and view creation to [Claude/REST] for the Investor CRM (§N2.3–N2.5). Status and type **definitions** stay [You] regardless — ClickUp exposes no public API for those, token or not.
5. **Committed vs Target's target figure is set — $2,500,000 (decision #20)** — but there's still no native Goal object to hold it; it stays a typed-once value on the card until DECISIONS revisits Goals, and until the dashboard itself is built (optional, later).
6. **RESOLVED:** retiring the `investor` tag now happens as part of the investor-task migration into the Investor CRM (§N2.6), not as a separate Punch List field/tag cleanup.
