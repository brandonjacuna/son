# 02 — Workspace Structure

Blueprint section. Read with STATE.md and DECISIONS.md (newest entries win). Sources: audit/*.md, research/07-classification.md, research/02-clickup-structure.md.

Every step below is tagged **[You]** (UI-only, ClickUp gives no API surface for it) or **[Claude]** (doable through this session's ClickUp MCP). Edit-surface facts, checked against developer.clickup.com on 2026-09-16 (this corrects research/02-clickup-structure.md's "full CRUD" claim for custom fields): custom-field **definitions** (create, delete, edit dropdown options) and **task types** and **status definitions** have no public API endpoint → **[You]**; custom-field **values** are settable via MCP/API → **[Claude]**; **views** can be created via REST (`POST /v2/list/{list_id}/view`) → **[Claude/REST]** — Brandon is issuing a personal API token (decision #3, confirmed). Nothing here executes yet — Claude is READ-ONLY in ClickUp this session.

---

## 1. Task types — the 10 approved, plus Investor/Real Estate

Task types are workspace-scoped (created once in **Workspace Settings → Task Types**, then enabled per Space). Name ≤16 chars, description ≤100 chars, icon + color. **[You]** create all 10; **[Claude]** can assign an existing type to a task via the `task_type` parameter (by name — e.g. `"Meeting"`, not the numeric `custom_item_id`; the MCP's `clickup_create_task`/`clickup_update_task` tools take the type name and resolve it internally) on create/update once types exist.

| Type | Icon (suggested) | Description (≤100 chars) | Default in |
|---|---|---|---|
| **Task** | ☐ checkbox | Anything that doesn't need a specific type — the fallback. | Every list (workspace default) |
| **Meeting** | 🗓 calendar | A meeting occurrence or its recurring-series parent. Already in use (Founding Punch List). | Meetings space (new, out of this section's scope) |
| **Document** | 📄 page | A doc-producing task — agenda, template, write-up to be authored. Already in use. | Docs-adjacent tasks, any space |
| **Idea** | 💡 lightbulb | An unvetted idea captured for later triage. Entry point for Capture lists. | Capture lists (all spaces) |
| **Deliverable** | 📦 box | A concrete artifact to be produced — a plan, a packet, a design file. | Capture lists |
| **Structure** | 🏗 building blocks | An org/process structure being defined (a role, a reporting line, a system). Distinct from the Classification value "Governance" — this is the *item kind*, Classification is the *effort nature*. | Capture lists |
| **Process** (existing, id 1023; plays the Workflow role — decision 2026-09-16) | 🔁 loop arrows | A repeatable process/procedure being designed. | Capture lists |
| **Founder Decision** (existing, id 1022; plays the Decision role — decision 2026-09-16) | ⚖️ scale | A discrete founder decision point with options — not a deliverable, not a meeting. This is the type for "Dominic Review Required" / "Attorney Review Required" items (§6). | Founding Punch List |
| **Milestone** | 🚩 flag | A dated checkpoint with no deliverable of its own (funding close, lease signed, opening day). ClickUp ships this as a native default type — enable it, don't custom-build it. | Founding Punch List |
| **Action Item** | 📥 inbox tray | A flagged item captured during a meeting (spoken cue or wrap-up block). Keeps its identity when it moves from the Meetings Action Items list into the Founding Punch List after confirmation — it doesn't get re-typed as `Task`. Decision #6 (approved), id 1026. | Meetings Action Items list (default, was `Task`) — ✅ DONE 2026-09-16 |
| **Investor** | 🤝 (Brandon's choice) | An investor/lender relationship record. Supersedes the pre-existing native `Person` type. Id 1027, ✅ DONE 2026-09-16. Default type on the **Investor CRM** list (03 §N2); also used to drive the (now-dropped) idea of a Punch List "Investors" view via task type rather than a field. | Investor CRM list; Founding Punch List (until investor tasks migrate out, 03 §N2) |
| **Real Estate** | 🏠 (Brandon's choice) | A lease/buildout task for the current funding + lease round. Supersedes the pre-existing native `Account` type. Id 1028, ✅ DONE 2026-09-16. **Replaces the planned Punch List Phase field** — the Founding Punch List's "Real Estate" view filters `task type = Real Estate (1028)` directly, no dropdown field needed. | Founding Punch List |

**[You]** Click-path: Workspace avatar (bottom left) → **Settings** → **Task Types** → **+ Add Task Type** (name, icon, color, optional description) for each of Meeting, Document, Idea, Deliverable, Structure, Workflow, Decision, Action Item, Investor, Real Estate — Task ships by default; for Milestone, toggle on the native "Milestone" type instead of creating a new one. Then, per Space: open the Space → **⋯ → Settings → Task Types** and enable the ones relevant to it (Capture-list types everywhere; Meeting/Document/Decision/Milestone/Action Item/Investor/Real Estate on Founding Punch List / the Meetings space / Investor CRM as applicable).

**Open question:** Meeting and Document already exist in the live workspace with real `custom_item_id` values (1021 for Meeting, confirmed in audit/00-workspace.md). Before creating anything, **[You]** must confirm in the UI whether Idea (custom_item_id 1019, confirmed on the Product space's one task), Deliverable, Structure, Workflow already exist under different names/ids — the MCP has no "list all task types" tool, so this can't be verified via [Claude]. Reconcile in the UI first to avoid creating duplicates.

---

## 2. Status sets

### 2a. Punch List set — ✅ DONE 2026-09-16 (as built, drops `Soon`)
**Inbox → Later → Next → Doing · Waiting · Canceled (done) · Done (closed)**

Status groups: **Inbox and Later are both Not Started/open.** Next, Doing, Waiting = Active (the on-deck queue — the original 3-deep draft's `Soon` was dropped as built). Canceled = Done group (not Closed as originally drafted). Done = the single Closed status.

### 2b. Capture set — ✅ DONE 2026-09-16, applied to all 11 Capture lists
**Captured → Developing → Ready → Activated (done) / Archived (closed)**

Status groups: Captured = open. Developing = Active. Ready = Active ("built out, waiting for the department to go live"). Activated = Done group ("promoted into real work"). Archived = Closed.

Both are built as **Status Templates** (**[You]**: configure the statuses on one list first, then **List Settings → Statuses → Save as Template**, name it, reuse on every other list/space that needs it) so they don't have to be hand-built per list.

**[You]** Click-path per list: open the list → **⋯ (list options) → Settings → Statuses → Edit** → rebuild to match the target set (add/rename/reorder/delete, assign each to its status group) → **Save as Template** the first time, **Apply Template** everywhere after.

**Apply at LIST level, never at Space level, in Operations and Technology.** Statuses inherit Space → Folder → List. The Carryover Register (Operations) and the Function → SaaS Map / SaaS Catalog lists (Technology) must keep their current statuses untouched; applying the Capture template at the Operations or Technology *space* level could cascade onto them. In the other nine spaces the Capture list is the only list, so list-level application is simply the uniform, safe habit. Verification after each apply: `clickup_get_list` on the Carryover Register (`901327884538`) and both Technology Build Out lists must return unchanged status sets.

### 2c. Status crosswalk — every existing status in every list

**Capture-pattern lists** (identical 5-status set on B.I. Capture, Design Capture, Events Capture, Finance Capture, Hospitality Capture, Operations Capture, People Capture, Product Capture, Promotion Capture, Property Capture, Technology Capture — 11 lists, per audit): revist / planning / in progress / complete / cancelled.

| Old status | → New Capture status | Rationale |
|---|---|---|
| revist | **Captured** | Default open/entry status, matches "not yet reviewed" |
| planning | **Developing** | Actively being thought through |
| in progress | **Developing** | Collapsed with planning — no Capture-list task in the audit ever reached "in progress" with real content, so no data loss |
| complete | **Ready** | "Built out" — matches the approved Ready definition |
| cancelled | **Archived** | Closed group |

Affected task volume: near-zero real content (per audit, almost every Capture-list task sits at "revist"; the only exception is the one "cancelled" task in Design Capture). **No approval needed** — no Scaling People or Carryover Register overlap.

**Technology Build Out sub-folder** (statuses: not assigned / assigned / locked in) — **not mapped**. This sub-folder holds the "Function → SaaS Map" and "SaaS Catalog" lists, which DECISIONS.md retires into a Doc (see §7). Its statuses are retired along with the lists, not migrated.

**Founding Punch List** (10 statuses: identified, active queue, up next, meetings, in progress, stalled, ongoing, final steps, in review, complete):

| Old status | → New Punch List status | Rationale |
|---|---|---|
| identified | **Inbox** | Status **rename** (decision #4, approved) — `identified` was already the list's default new-task status; renaming it changes only the status name on the ~242 Scaling People tasks, nothing else |
| active queue | **Later** | Queued, not imminent |
| up next | **Next** | Closest to being worked, name maps directly |
| meetings | **retire as a status** | Superseded by the Meeting task type; each occurrence gets re-triaged individually into Next/Doing/Waiting/Done based on its actual state — not a blanket crosswalk |
| in progress | **Doing** | Direct match |
| stalled | **Waiting** | Blocked/paused reads as Waiting |
| ongoing | **Doing** | Recurring work is live-in-motion; its recurring *nature* now lives in the Classification field ("Recurring/Operating"), not the status |
| final steps | **Doing** | Still active, closing out |
| in review | **Waiting** | Waiting on someone else's review/feedback |
| complete | **Done** | Direct match |
| *(none currently)* | **Canceled** *(new)* | No existing equivalent status — added for future use; nothing migrates into it |

**APPROVED (#4) — the "identified" → "Inbox" rename.** All ~242 Scaling People governance-backlog tasks (plus 13 non-Scaling-People tasks — 255 in `identified` total per the 2026-09-16 baseline export; the audit's ~330 was an overestimate) sit at status "identified." Per DECISIONS.md (2026-09-16, post-audit), Brandon explicitly approved this as an exception to Scaling People protection: **rename** the status `identified` to `Inbox`. This is a status-name change only — `identified` was already the list's default new-task status, so no task is re-mapped into a different status bucket, just relabeled. Nothing else about the ~242 tasks (name, fields, assignees, dates) changes. Brandon updates his own Scaling People extraction pipeline (which writes status "identified") to match. The Punch List set reads `Inbox → Later → Next → Doing · Waiting · Canceled (done) · Done (closed)` — no `Soon`, no separate legacy status.

**Note for downstream steps (§3, §4):** since `Inbox` is also the default status any new task lands in, it is no longer a unique signal for "this is a Scaling People task" the way `identified` was pre-rename. Anywhere this document used status `identified` as a proxy to find/exclude Scaling People tasks, prefer the parent-task relationship (parent "Sŏn Operational Build Out," or one of the S1–S17 chapter parents) instead, cross-checked against status `Inbox` rather than relying on status alone.

**Carryover Register** (126 tasks, all status "to do"; 7 other statuses defined and unused: planning/in progress/at risk/update required/on hold/complete/cancelled) — **not touched, at all, under any circumstance.** Hard constraint. No crosswalk is proposed for this list; its statuses stay exactly as they are.

**Personal space** (to do / in progress / complete) — out of scope per hard constraint; no crosswalk proposed.

---

## 3. Fields

### Owner / Owner Notes — DROPPED, superseded by built-in fields (decision, 2026-09-16 Stage 1)
No new Owner or Owner Notes fields are created. **Assignee** = the person executing the task; **Created By** (ClickUp's built-in field, Brandon turned it on) = the owner of the task's creation and completion — this is the accountable-DRI signal the Owner field was meant to provide, at zero build cost.

"Notes from BJAC" was **renamed in place** to **Created By Notes** (same field id `52c7d5a1`, values kept) rather than being replaced by a new Owner Notes field that values would need migrating into. This removes the entire migrate-then-delete sequence the original design called for (was steps 1–5 here, and decision #16): there is nothing to migrate and nothing to delete. The renamed field still carries the Function → SaaS Map / SaaS Catalog data those lists' Doc rebuild (04 §6) needs, unaffected by the rename.

**[You]** did the rename directly in the UI (field **⋯ → Rename**), 2026-09-16 — ✅ DONE. No further action needed here.

### Classification — 9 workspace-wide labels (multi-select), APPROVED — ✅ DONE 2026-09-16
Per DECISIONS.md ("post-audit"), the approved set is these 9 — this supersedes the 12-value draft in research/07-classification.md, which is kept only as background reasoning. The original approval was 7 values; decision #5 (2026-09-16, post-audit) added **Capital/Budget** and **Brand/Design** back:

| Value | Definition |
|---|---|
| **Build/Setup** | Standing something up once — buildout, a system, a vendor onboarding, a process being created for the first time. Ends when the thing exists. |
| **Recurring/Operating** | Ongoing work that repeats on a cadence once live — the "run the business" half of run vs. change. Commonly paired with the Meeting task type, but not identical to it. |
| **Governance** | Org design and decision-making structure — roles, policies, the Operating Agreement, the Scaling People backlog's Structure/Instrument/Process items, and founder decision points. |
| **Legal/Compliance** | Requires legal review, filing, or regulatory/licensing compliance. |
| **Vendor/Procurement** | Selecting, contracting, or managing an external vendor or SaaS tool. |
| **R&D** | Open-ended investigation where the answer isn't known yet — entity-structure research, market research, this Phase 3 research track itself. |
| **Admin** | Low-stakes account/access/logistics cleanup — not a decision, not a deliverable, just needs doing. Home for the leftover admin tasks (§8). |
| **Capital/Budget** | Capital spend and budget items — the old Project field's "Financials" option (equipment/FF&E purchases, budget lines, capital allocation decisions). |
| **Brand/Design** | Brand and guest-experience creation — the 1A–12A brand register, uniforms, visual identity work. |

**[You]** create as a workspace-scoped **Labels** field named **Classification**, scope "Everything," with all 9 options.

**Resolved (decision #5):** the original 7-value approval dropped separate *Investor/Fundraising-Facing*, *Real Estate/Buildout-Facing*, *Capital Spend/Budget*, and *Brand/Design/Guest Experience* values. Investor- and Real Estate-facing work is carried by the **Investor** and **Real Estate** task types instead (§1) — Classification stays purely long-lived effort types. Capital/Budget and Brand/Design are now back as dedicated values — no fallback routing to Build/Setup or Vendor/Procurement is needed.

### Cross-Department — DROPPED, superseded by native Tasks in Multiple Lists (TIML)
No new Cross-Department field is created. Per DECISIONS.md (2026-09-16 Stage 1): cross-department reach is ClickUp's native **Tasks in Multiple Lists** ClickApp (✅ DONE, turned on) — a task can simply appear in each relevant department list directly, rather than carrying a labels field naming the other departments it touches. Per ClickUp Help, anyone with access to any of a task's lists can see it. The home list stays the Founding Punch List during funding + lease; secondary lists only surface the task. **[Claude]** can add a task to additional lists via `clickup_add_task_to_list`.

The two existing space-level "Department Crossover" fields (Events, Finance) are still removed — see "Fields to remove" below — since their intent is now fully covered by TIML, not by a replacement field.

### Punch List Phase field — DROPPED, superseded by task types
No Punch List Phase field is created. Per DECISIONS.md (2026-09-16 Stage 1): Brandon created dedicated **Investor** (1027) and **Real Estate** (1028) task types instead (§1) — the Founding Punch List's views filter by task type, not by a dropdown value. This also means investor-related Punch List tasks aren't distinguished by a phase value at all; they instead migrate out of the Punch List entirely into the **Investor CRM** list (03 §N2, design DECISIONS 2026-09-17) — see §5 below.

### Fields to remove
- **Project** (dropdown: Financials/White Paper/Pitch Deck/Research, Founding Punch List) — unpopulated on every sampled task (audit/founding-son.md). Its intent splits across Classification (Governance/R&D/etc.) and the Investor/Real Estate task types. **[You]** delete after confirming zero populated values — **[Claude]** can confirm via `clickup_filter_tasks` scoped to this field before deletion is approved.
- **Category** (labels: Asset Digital/Physical, Function, Idea — every Capture list) — superseded by the new task types (Idea, Deliverable, Structure, Process now do this job directly, at the item level, instead of a field). Unpopulated everywhere sampled. **[You]** delete.
- **Notes** (text — every Capture list, distinct from "Notes from BJAC"/Created By Notes) — unpopulated everywhere sampled; superseded by adding Classification + Created By Notes to the Capture lists. **[You]** delete.
- **Department Crossover** (labels, Events and Finance space-level) — superseded by native TIML (above). **[You]** delete once confirmed unpopulated.
- **"Solution"** field (found only on Hospitality's "First timer gift" task, a ~57-option vendor dropdown that doesn't belong to any list's defined field set) — **DELETE** (decision #12). **[Claude]** first copies any existing value on "First timer gift" into that task's description, then **[You]** deletes the field definition.

**Every "confirm zero populated values" check above must, without exception:** (1) pass `include_closed: true` on the `clickup_filter_tasks` call — confirmed empirically that this defaults to excluding closed tasks, so a value sitting on a Done/Canceled/Archived task would otherwise be invisible and the field would read as empty when it isn't; and (2) run once against a field/value combination already known to be populated (a positive control) immediately before trusting a "zero" result — `clickup_filter_tasks`'s own tool description warns that "one unrecognized field_id makes the API silently drop ALL custom field filters in the call and return unfiltered results," with no error raised, so a stale or mistyped field_id from `clickup_get_custom_fields` would not fail loudly. Both checks are cheap; skipping either turns an irreversible field deletion into a silent-data-loss risk.

---

## 4. Views

Per decision #3 (personal API token, confirmed), every view below is **[Claude/REST]** (`POST /v2/list/{list_id}/view`), not [You]. The click-paths are kept as a description of the target shape and as the [You] fallback if the token is ever unavailable.

### Founding Punch List
- **"Action Items" (default view).** Everything not carved out into Real Estate, **including all Scaling People tasks and subtasks** (per DECISIONS.md, Scaling People must always remain visible here — it is never filtered out of the default view). Filter: `Task Type is not Real Estate`. No exclusion based on Classification or task name. (There is no "Investors" carve-out view anymore — investor tasks migrate out of the Punch List entirely into the Investor CRM, §5.)
- **"Real Estate."** Filter: `Task Type = Real Estate` (id 1028). Per DECISIONS.md, carve-outs must be field/type-driven, and Scaling People (Classification = Governance, status Inbox per decision #4's rename) must never leak in here — since this view is an *include* filter on task type, that's structurally guaranteed as long as no Scaling People task is ever given the Real Estate type.

**[You]** Click-path: open Founding Punch List → **+ View → List** → name it → **Filter → Add Filter → Task Type → is/is not → Real Estate** → save. Repeat for each of the 2.

### Capture list default views (all 11 Capture lists)
Default view: **Table**, since these are audit-and-triage lists, not kanban work queues.

Columns (left to right): Task Name, **Task Type** (Idea/Deliverable/Structure/Process), **Status** (Captured/Developing/Ready/Activated/Archived), **Assignee**, **Created By**, **Classification**, **Created By Notes**, Date Created.

**[You]** Click-path: list → **View options (⋯) → Columns** → add/reorder to match, remove Category/Notes/Project-derived columns once those fields are deleted.

---

## 5. Investor tag retirement — now via migration into the Investor CRM

Per DECISIONS.md (2026-09-17): the separate Investors list (N2), its "Related Punch List Tasks" relationship, the Punch List "Investors" view and the investor-tag → Phase-value plan below are all **replaced** by migrating investor tasks out of the Founding Punch List into the **Investor CRM** list (Founding Sŏn, 03 §N2). There is no Punch List Phase field and no Classification value for "Investors" — the tag's intent moves with the tasks themselves, not onto a field.

1. **[Claude]** `clickup_filter_tasks` for every task carrying the `investor` tag (audit found ~12) **and** cross-reference against the audit's broader "~45 investor-related tasks" grouping (named-individual outreach, pitch deck, white paper, investor website — most of these are currently untagged) so the migration doesn't just replicate the tag's incomplete coverage.
2. **[Claude]** produce a preview table: each candidate task → proposed Investor CRM record (new or existing) → whether it becomes a follow-up subtask there or stays in the Punch List (e.g., general fundraising collateral work like "Create Pitch Deck 1.0" is not investor-relationship work and stays put).
3. **[You]** (Brandon) reviews and approves the exact list — deciding which of the ~45 actually migrate is a judgment call, not a mechanical one (decision #9's preview-table gate).
4. **[Claude]** creates/updates Investor CRM records for the approved set, moves the approved Punch List tasks/subtasks into the Investor CRM (or links them as follow-up subtasks per the CRM design), and verifies nothing is lost.
5. **[Claude]** `clickup_remove_tag_from_task` to strip `investor` from every task that had it, once its migration is confirmed (no task loses its investor signal in the gap between steps).
6. **[You]** confirm in **Space Settings → Tags** that `investor` no longer appears on any task; delete the tag definition itself from that same screen if ClickUp still lists it as unused (no MCP tool manages tag *definitions*, only task-level add/remove).

## 6. Operating Agreement review tasks

"Dominic Review Required" and "Attorney Review Required" sections currently live only as text inside the Operating Agreement Doc (Operations Documents folder, per audit/operations.md), not as tracked tasks. Per DECISIONS.md, these become tracked tasks in the Founding Punch List.

- **[You]** (needs a human read of the Doc to extract each flagged section — not mechanically scrapeable) identify every "Dominic Review Required" / "Attorney Review Required" passage and its section title.
- **[Claude]** `clickup_create_task` on the Founding Punch List for each: type = **Founder Decision**, Classification = [Governance, Legal/Compliance], Assignee = Dominic (for "Dominic Review Required"); for "Attorney Review Required" — no attorney is a workspace member, so per decision #11, Assignee stays **unset** with the reviewer named in **Created By Notes** instead (the renamed "Notes from BJAC" field — no separate Owner Notes field exists), and no guest is invited — description linking back to the Doc page.
- **[You]** confirm no other legal-review flags exist elsewhere in Operations Documents' 16 pages beyond what's already been read.

## 7. SaaS Map → Doc (cross-reference)

Not this section's primary scope (see the Docs-home section of the blueprint for the rebuild plan), but its status-set retirement is noted in §2c: once the "Function → SaaS Map" and "SaaS Catalog" lists under Technology Build Out are exported and verified per DECISIONS.md's required export-before-delete step, their statuses (not assigned / assigned / locked in) retire with them — no crosswalk needed.

## 8. Leftover admin tasks

Per DECISIONS.md: keep the leftover admin tasks (three "transfer ownership from brandon," Gmail, Airtable, AirTable, ClickUp, Access Removal — audit/founding-son.md §Issues), give them proper names and owners. **Per decision #10, Brandon does this himself directly in ClickUp — Claude does nothing here.**

- **[You]** decide what each single-word task actually refers to (the audit couldn't determine intent from the name alone — e.g., which of the 3 "transfer ownership from brandon" tasks covers which account), then rename each task and set Assignee + Classification = Admin directly in the UI.

---

## Open questions / risks for Brandon

1. **RESOLVED (#4, approved):** "identified" → "Inbox" is a status rename, an explicit exception to Scaling People protection. Only the status name changes on the ~242 Scaling People tasks (255 counted in the 2026-09-16 baseline export).
2. **RESOLVED (#5):** Classification gap closed — Capital/Budget and Brand/Design added back, making 9 values. No fallback routing needed.
3. **RESOLVED (§1):** task types reconciled in the UI 2026-09-16 — Action Item (1026), Investor (1027, supersedes Person), Real Estate (1028, supersedes Account) all created; Process/Founder Decision reused for Workflow/Decision. No duplicates.
4. **RESOLVED (§5):** investor coverage is no longer a tag→field copy — it's a Claude-produced preview table (task → Investor CRM record) that Brandon approves before any migration, deliberately wider than the ~12 tagged tasks (decision #9, design DECISIONS 2026-09-17).
5. **RESOLVED (#11):** Assignee stays unset on Attorney Review items, with the reviewer named in Created By Notes; no guest invite.
6. **RESOLVED (#12):** delete the stray "Solution" field on Hospitality's "First timer gift" task — Claude copies its value into the task description first, then [You] deletes the field definition.
