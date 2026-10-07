# 00 — Sŏn ClickUp Blueprint (Phase 3b)

_Lead-architect integration, 2026-09-16. Binding inputs: STATE.md and DECISIONS.md (newest wins). Sections 01–04 were drafted in parallel and reconciled here; where they disagreed, the section files were edited directly and this file records the resolution (§4). Nothing in ClickUp has been changed — this session is read-only. Every build step in 05-build-plan.md is tagged **[You]** (ClickUp UI) or **[Claude]** (ClickUp MCP in the build session)._

---

## 1. Executive overview

**What this blueprint builds.** One new operating space (**Meetings**) run by a ClickUp **Super Agent**, one new records list (**Investor CRM**) in Founding Sŏn (an optional native **Fundraising & Runway Dashboard** later), a workspace-wide field and status layer (built-in **Created By**/**Created By Notes** as owner/notes — no separate Owner or Owner Notes fields, Classification ×9, native **Tasks in Multiple Lists** for cross-department reach instead of a Cross-Department field; the Punch List and Capture status sets; 10 task types, which also drive the Punch List's views instead of a Punch List Phase field), the Founding Punch List's views by task type, a **Docs Home** with a naming convention, a **Department Shell** page in every department space, the **Function → SaaS Map** rebuilt as Docs (lossless, approval-gated), the `investor` tag retired as part of migrating investor tasks out of the Punch List into the Investor CRM, and the Operating Agreement's review flags turned into tracked `Founder Decision` tasks.

**What it does not touch.** Scaling People tasks (~242 tasks incl. the S1–S17 chapters) and the Carryover Register (125 tasks) are never edited, moved, re-statused or bulk-touched; views filter around them. Department spaces stay as shells — no merging, no collapsing, no action tasks in them until the funding + lease gate passes. The Personal space is out of scope.

**Engine.** ClickUp-first: Super Agents, Brain, Automations and ClickUp's MCP abilities are the engine for every workflow. Claude designs, builds via the ClickUp MCP, and is a fallback only where ClickUp verifiably cannot do something — with evidence filed and Brandon's approval. The research/12 "Claude-primary meetings engine" recommendation is rejected; its facts are reused, its verdict is not.

**The one thing everything waits on.** A 30-minute **proof test** (01 §0) settles whether a Super Agent's native Google Calendar tool can create/update/cancel events with guests + Meet + location, whether Granola's MCP works when wired to a Super Agent, and whether a single recurring instance can be patched. Its result picks a rung on the fallback ladder (native tool → ClickUp Automation → community MCP → Claude, last resort) and unblocks Stage 2 of the build plan. Until it runs, the space/list/field layer can be built; the agent's tooling cannot.

**Build shape.** Six stages (05-build-plan.md): 0 proof test + baseline export · 1 [You] UI prerequisites · 2 [Claude] MCP builds · 3 migrations with preview + approval gates · 4 agent live, triggers turned on one at a time · 5 verification. Roughly 3–4 hours of [You] clicking spread over two weeks, the rest [Claude].

---

## 2. Target workspace map

Legend: **NEW** = created by this blueprint · **CHANGED** = existing object, settings/fields/statuses/views change · **UNTOUCHED** = exists, no change · **PROTECTED** = hard constraint, never modified · **OUT OF SCOPE** = Personal space · **RETIRE (gated)** = removed only after export + Brandon sign-off. IDs from `audit/*.md`.

### Workspace level (90131574430)
| Object | Status | Notes |
|---|---|---|
| Task types: Task, Meeting (1021), Document, Idea (1019) | UNTOUCHED (exist) | UI check for hidden duplicates before adding more (02 §1) |
| Task types: Action Item (1026), Investor (1027), Real Estate (1028) NEW; Deliverable, Structure, Process (as Workflow), Founder Decision (as Decision) already existed | ✅ DONE 2026-09-16 | [You] Workspace Settings → Task Types; Investor/Real Estate replace the planned Punch List Phase field — Punch List views filter by task type instead |
| Task type: Milestone | NEW (enable native) | Not custom-built |
| Owner / Owner Notes fields | DROPPED — no new fields | Built-in **Created By** (Brandon turned it on) = owner; Assignee = executor. "Notes from BJAC" was renamed **Created By Notes** in place (same field id 52c7d5a1, values kept) — not a new field, no migrate-then-delete step |
| Field **Classification** (Labels ×9, Everything) | ✅ DONE 2026-09-16 | Build/Setup · Recurring/Operating · Governance · Legal/Compliance · Vendor/Procurement · R&D · Admin · Capital/Budget · Brand/Design |
| Field **Cross-Department** | DROPPED — no new field | Cross-department reach is native ClickUp **Tasks in Multiple Lists** (ClickApp, ✅ DONE 2026-09-16, on), not a field |
| Field **Punch List Phase** | DROPPED — no new field | Superseded by task types (Investor 1027, Real Estate 1028); Punch List views filter by task type |
| Status templates: **Punch List set**, **Capture set**, **Meeting Series**, **Meetings**, **Action Items**, **Investor CRM pipeline** | Punch List/Capture/Meetings ✅ DONE 2026-09-16; Investor CRM pending | Punch List: Inbox (renamed from identified, 255 tasks) → Later → Next → Doing · Waiting · Canceled (done) · Done (closed) — no Soon. Capture: Captured → Developing → Ready → Activated (done) / Archived (closed), applied to all 11 lists |
| Team **Founders** | NEW | Brandon, Dominic, 3rd partner on join |
| Super Agent **Meetings Super Agent** | ✅ DONE (built by Brandon) | 01 §3; scheduled triggers live (Mon 7am roll-forward, daily 8am prep, 2pm/7pm notes sync, DMs for reschedule/cancel); no Rung 3/4 |
| Super Agent **Founders Meeting Assistant** (prototype, bot user -87977709) | CHANGED → retire | Kept until the new agent passes 4 weeks of review (01 §2 step 8) |
| Automations (cancel-path delete; handoff Automations) | Cancel ✅ DONE; handoff NEW | Cancel: status → Canceled ⇒ Google Calendar Delete event, Keywords = Event Title field (title search — ID matching doesn't work, AUTO_505). Handoff: Action Items → Routed ⇒ move to Founding Punch List; Capture → Activated ⇒ add to Founding Punch List |
| Dashboard **Fundraising & Runway** | NEW, optional/later | Reads the Investor CRM list once it has data (03 §N3) |
| Doc **Sŏn Docs Home** (Everything scope, promoted to wiki) | NEW | 04 §1 |
| Chat channels (19) | UNTOUCHED | Channel consolidation not selected in triage |
| Google Calendar integration, Granola MCP workspace connection | NEW connections | Stage 1 |

### Founding Sŏn (90138396180)
| Object | Status | Notes |
|---|---|---|
| **Founding Punch List** (901323485125) | CHANGED | Statuses → Punch List set ✅ DONE (`identified` renamed to **Inbox**, 255 tasks — it was already the list's default new-task status, decision #4) → Later → Next → Doing · Waiting · Canceled (done) · Done (closed), no Soon; Classification field ✅ DONE; owner/notes via built-in Created By/Created By Notes (no new fields); cross-department reach via native TIML (no field); no Punch List Phase field — views filter by task type instead (Real Estate = type 1028); remove Project after zero-value check; views **Action Items** (default, incl. all Scaling People) and **Real Estate**; `investor` tag retired as part of migrating investor tasks to the **Investor CRM** (below); new `Founder Decision` tasks for Operating Agreement review items; leftover admin tasks renamed by Brandon (#10) |
| ↳ Scaling People: Sŏn Operational Build Out + ~242 tasks incl. S1–S17 | **PROTECTED** — status rename ✅ DONE 2026-09-16 | Never edited; status `identified` renamed to `Inbox` (list-status rename only, decision #4 — nothing else about these tasks changes; Brandon updates his own Code extraction pipeline) |
| ↳ Prototype meeting tasks (86ake5ud3, 86akfka82, 86akgez3c, 86akfkagr, 86akgw0zn, 09-22/09-29 agendas) | CHANGED → migrate, then archive (gated) | Copied to Meetings space first as history; originals archived by Brandon only after side-by-side check (01 §2) |
| **Investor CRM** list | NEW | Founding Sŏn, sibling to Founding Punch List; default type **Investor**; status = pipeline stage (Prospect → Contacted → Meeting Scheduled → Diligence → Soft Commit (active) · Passed (done) · Committed (closed)); lean fields incl. Related Meetings relationship + Created By Notes; follow-ups are subtasks. **Replaces** the earlier Investors list (N2), its "Related Punch List Tasks" relationship, and the Punch List "Investors" view — investor tasks leave the Punch List via a preview + approval migration (design DECISIONS 2026-09-17; 03 §N2) |

### Meetings (NEW space) — ✅ DONE 2026-09-16
| Object | Status | Notes |
|---|---|---|
| **Meeting Series** list | ✅ DONE | 2 tasks (Founders Meeting, Founders Standup), type `Meeting`; statuses Active/Paused/Retired (closed) |
| **Meetings** list | ✅ DONE | One task per occurrence, type `Meeting`; statuses Scheduled → Prep Sent → Held → Canceled (done) · Notes Synced (closed) — no Rescheduled; lean fields (Meeting Type, Series relationship, GCal Event ID, Event Title, Location, Notes Doc Link, Capture Source, Attendees); 5 views; default task templates from `templates/*.md` |
| **Action Items** list | ✅ DONE | Flagged inbox, type `Action Item` (decision #6, was `Task`); statuses Flagged → Dropped (done) · Routed (closed); destination = Founding Punch List via a handoff Automation (Routed ⇒ move task) |
| Meeting-notes Doc (one page per occurrence) | NEW | Shared Doc, linked via Notes Doc Link URL field |

### Operations (90136733940)
| Object | Status | Notes |
|---|---|---|
| **Carryover Register** (901327884538) | **PROTECTED** | Statuses, tasks, fields untouched; Capture template applied at *list* level elsewhere so nothing cascades here |
| Operations Capture (901327291225) | CHANGED | Capture status set; Table default view; Category/Notes fields removed; task types enabled |
| Operations Documents (folder) — Sŏn Operating System, Scaling People: Translation Program, Founder Bios, Operating Agreement Pre-Counsel Brief | UNTOUCHED + 1 NEW page | Department Shell page added; Operating Agreement Doc is read (by Brandon) to extract review items, not edited |

### People (90136734650)
| Object | Status | Notes |
|---|---|---|
| People Capture (901327291241) | CHANGED | Capture set, Table view, field cleanup |
| Education/Training Modules (folder) — FDN.01 | UNTOUCHED | Linked from Docs Home |
| People Notebooks (folder) — Interviews Notebook | UNTOUCHED + 1 NEW page | Shell page added here |
| "Heejae" Doc at space root | RETIRE (gated) | ARCHIVE if ClickUp supports doc archiving (decision #22); if not, Brandon deletes it himself — Claude never deletes it |

### Finance (90136733856)
| Object | Status | Notes |
|---|---|---|
| Finance Capture (901313751831) | CHANGED | Capture set, Table view; space-level "Department Crossover" field deleted after Cross-Department exists |
| Finance Documents (folder) — Finance & Technology Operating Manual | UNTOUCHED + 1 NEW page | Shell page |

### Technology (90136733924)
| Object | Status | Notes |
|---|---|---|
| Technology Capture (901327291281) | CHANGED | Capture set, Table view, field cleanup |
| Tech Documents (901318761463) — Technology OS – Build Hub | UNTOUCHED + NEW Docs | Shell page; "Technology - Function → SaaS Map", "Technology - SaaS Catalog" Docs land here |
| ↳ Claude sub-folder (901318509389) — Claude Project Review, Methodology, Investment Thesis Architect | CHANGED | Split into "Claude - AI Persona Library" + "Technology - Compliance References" (NEW Docs); pages moved by [You]; "(Temporary)" / staging-for-Box left for Brandon |
| ↳ Technology Build Out (901315929256) → **Function → SaaS Map** (901323733488, 241 tasks) | RETIRE (gated) | Full CSV export → Doc → verification → Brandon sign-off → then removal. Statuses retire with it |
| ↳ Technology Build Out → **SaaS Catalog** (901327544218, 46 tasks) | RETIRE (gated) | Same gate |

### Design & Visuals (90136725596)
| Design Capture (901313738581) | CHANGED | Capture set, Table view, field cleanup |
|---|---|---|
| Design Documents (901318761389, empty) | UNTOUCHED + 1 NEW page | Shell page |

### Events (90136733952)
| Events Capture (901313751988, 20 tasks) | CHANGED | Capture set, Table view; "Department Crossover" field deleted after Cross-Department; 3-deep Sponsors nesting left as-is (vendor registry deferred to Construction) |
|---|---|---|
| Documents folder | NEW (decision #15) | Created now, with shell page |

### Hospitality (90136733933)
| Hospitality Capture (901313751954, 4 tasks) | CHANGED | Capture set, Table view; stray "Solution" field on "First timer gift" — [Claude] copies its value into the task description, then [You] deletes the field definition (decision #12) |
|---|---|---|
| Documents folder | NEW (decision #15) | |

### Product (901312138543)
| Product Capture (901327291274, 1 task) | CHANGED | Capture set, Table view |
|---|---|---|
| Beverage (901315418169), Culinary (901315418173) folders | UNTOUCHED | Empty shells, stay |
| Documents folder | NEW (decision #15) | |

### Promotion (90136688132)
| Promotion Capture (901327291261, 0 tasks) | CHANGED | Capture set, Table view |
|---|---|---|
| Promotion Documents (901318761442) | UNTOUCHED + 1 NEW page | Shell page |

### Property (90136733959)
| Property Capture (901327291277, 0 tasks) | CHANGED | Capture set, Table view |
|---|---|---|
| Documents folder | NEW (decision #15) | Shell page = the worked example in 04 §5 |

### Business Intelligence (90136734098)
| B.I. Capture (901313752244, 0 tasks) | CHANGED | Capture set (fixes the `revist` typo), Table view |
|---|---|---|
| Documents folder | NEW (decision #15) | |

### Personal (901313974752)
| List (901328175544), Parked folder (901318674002) | **OUT OF SCOPE** | Not touched, not audited further |
|---|---|---|

---

## 3. Component index

| # | Component | File | Owner tags | Depends on |
|---|---|---|---|---|
| C1 | Proof test + fallback ladder | [01 §0](01-meetings-system.md) | [You] | — |
| C2 | Meetings space: lists, fields, statuses, views, templates | [01 §1](01-meetings-system.md) | [You] space/fields/statuses · [Claude] lists/tasks/docs | C1 for agent tooling only |
| C3 | Prototype migration | [01 §2](01-meetings-system.md) | [Claude] copy · [You] review/archive | C2 |
| C4 | Meetings Super Agent (instructions, tools, triggers, guardrails, credits) | [01 §3–5](01-meetings-system.md) | [You] | C1, C2 |
| C5 | Agenda templates | [templates/](../templates/) `founders-meeting.md`, `founders-standup.md`, `investor-meeting.md` | [You] save as default task templates | C2 |
| C6 | Task types (10) | [02 §1](02-workspace-structure.md) | [You] | UI duplicate check |
| C7 | Status sets + crosswalk | [02 §2](02-workspace-structure.md) | [You] | #4 for `identified` |
| C8 | Fields: Classification (✅ DONE); owner/notes via built-in Created By/Created By Notes (✅ DONE, no Owner/Owner Notes fields); cross-department via native TIML (✅ DONE, no field); no Punch List Phase field (superseded by task types); removals | [02 §3](02-workspace-structure.md) | [You] create · [Claude] migrate values | #5 |
| C9 | Punch List views (by task type) + Capture Table views | [02 §4](02-workspace-structure.md) | [Claude/REST] (personal API token, #3) | C8 |
| C10 | `investor` tag retirement, via the investor-task migration into the Investor CRM | [02 §5](02-workspace-structure.md) | [Claude] filter/migrate/remove · [You] review + delete tag def | C13, #9 |
| C11 | Operating Agreement review → `Founder Decision` tasks | [02 §6](02-workspace-structure.md) | [You] extract · [Claude] create | C6, C8, #11 |
| C12 | Leftover admin tasks rename | [02 §8](02-workspace-structure.md) | [You] only — Brandon renames and assigns owners himself (decision #10) | — |
| C13 | Investor CRM list (replaces N2's Investors list) | [03 §N2](03-fundraising.md) | [You] statuses · [Claude/REST] fields/views · [Claude] migration | #7, #9 |
| C14 | Fundraising & Runway Dashboard (N3) — optional, later | [03 §N3](03-fundraising.md) | [You] | C13 (+ C2 for meetings card) |
| C15 | Docs Home + naming convention | [04 §1–2](04-knowledge-docs.md) | [Claude] docs · [You] wiki + pin | — |
| C16 | Claude folder split | [04 §3](04-knowledge-docs.md) | [Claude] new Docs · [You] page moves | #14 |
| C17 | Meeting-notes sharing rule | [04 §4](04-knowledge-docs.md) | design rule → C4 | — |
| C18 | Department Shell template (N8) | [04 §5](04-knowledge-docs.md) | [Claude] | #15 |
| C19 | SaaS Map → Doc rebuild (lossless, gated) | [04 §6](04-knowledge-docs.md) | [Claude] export/Docs · [You] approval | #13 |
| C20 | Build sequence | [05-build-plan.md](05-build-plan.md) | both | all |
| C21 | [You] click-path checklist | [runbooks/you-checklist.md](../runbooks/you-checklist.md) | [You] | C20 |

---

## 4. Cross-section resolutions (edited into the section files)

| Conflict found | Resolution applied |
|---|---|
| 01 used an `Action Item` task type; 02's approved set was 9 types without it | RESOLVED (#6, approved): `Action Item` is the 10th task type; the Action Items list uses it as its default type |
| 01 gave Meeting Series `Task`/`Structure`; 02 defines `Meeting` as "occurrence **or series parent**" | Meeting Series = `Meeting` |
| Series names: prototype "Weekly Founders Sync"/"Founders Thursday Standup" vs DECISIONS' meeting types "Founders Meeting"/"Founders Standup" | Series and Meeting Type share the names **Founders Meeting** / **Founders Standup**; prototype names kept as legacy aliases in descriptions; templates updated |
| Standup template said "moved to Google Meet"; DECISIONS keeps the phone call with a Meet fallback | Template header now: phone call (Brandon calls Dominic, Granola iOS), Meet + Granola desktop as fallback, Thu 11:00–11:45 |
| 01 created an `Investor` Relationship on Meetings; 03 created `Related Meetings` on Investors | One Relationship pair, created once from the Investors side after the Meetings list exists; reciprocal column named `Investor` |
| 03 rollup counted meetings "status Complete"; 01 has no such status | Rollup counts `Held` or `Notes Synced` |
| 03 added a "Relationship Owner" People field; 02 defines a workspace `Owner` | Investors reuses `Owner` |
| 04 §4 called the notes link a Relationship field; 01 uses a URL field (Relationships target tasks) | URL field `Notes Doc Link` everywhere |
| 04 §1 placed the SaaS Map Doc under Founding Sŏn; 04 §6 builds it in Technology; several § cross-refs pointed at the wrong sections | Technology; cross-refs fixed; Doc names follow the `[Space/Topic] - [purpose]` convention |
| 01 said list creation is [You]; MCP has `clickup_create_list` | [You] creates the space, [Claude] the lists |
| 02 intro claimed custom fields have "full CRUD via API" (from research/02); research/06 and developer.clickup.com show no create endpoint | Field/type/status definitions = [You]; values = [Claude]; list views = [Claude/REST] — Brandon is issuing a personal API token (decision #3, confirmed), so this is no longer conditional (`POST /v2/list/{list_id}/view` confirmed) |
| Action Items "suggests a destination **space**" (DECISIONS) vs "no other space gets action tasks until past funding + lease" | Destination is the Founding Punch List while the gate holds; Suggested Destination carries Classification / Cross-Department / Punch List Phase hints (decision #8) |
| Retiring the `identified` status would re-status ~242 Scaling People tasks | RESOLVED (#4, approved as an explicit exception): `identified` → `Inbox` is a status **rename**, not a remap — it was already the list's default new-task status, so this changes only the status name on the ~242 Scaling People tasks and nothing else about them |
| Capture status template applied at space level in Operations/Technology would cascade onto the Carryover Register and SaaS lists | Apply at list level only; verify protected lists' statuses after each apply |
| "Notes from BJAC" deletion (02) vs its live data on the SaaS Map/Catalog lists (04) | Check whether it is one shared field ID; if so, delete only after the SaaS Map export is approved (decision #16) |
| 01's unidentified parent `86ake5ud3` | Identified from audit/00-workspace §8 as "Weekly Founders Sync – Series"; confirm during migration |
| Investor-meeting template pointed action items at an "Investors & Fundraising" view; 02 names the view "Investors" | Views are named exactly as the Punch List Phase values: **Investors**, **Real Estate/Lease** |

---

## 5. Decisions needing Brandon's approval (consolidated, numbered)

**All 22 are resolved, per DECISIONS.md (2026-09-16, post-audit).** The table below shows the resolved decision for each — most confirm the original default as-is; #4, #5, #6, #10, #12, #20 and #22 differ from the default and are noted as such. Gate letters show which build stage the answer unblocks (05-build-plan.md).

| # | Decision | Resolved decision | Gate |
|---|---|---|---|
| 1 | **Proof-test result and fallback rung** (01 §0). Rungs 1–2 (native agent tool / ClickUp Automation) need only your go-ahead; **Rung 3 (community Google Calendar MCP) or Rung 4 (Claude) require your explicit approval with the screenshots filed**, per the CORE PRINCIPLE. Same question separately for the Granola pull. | Runs as planned in Stage 0; rung picked from the result. Separately, the related **Granola phone-call standup-capture test already PASSED** (2026-09-16) — standup capture is confirmed on Granola, independent of this proof test. | S0 → S2 |
| 2 | **AI tier.** Confirm Brain AI (1,500 credits/user/mo) vs Everything AI (5,000). | **Not a constraint, not a blocker — Brandon handles AI tier and credits directly.** No gate here; §6's credit estimates remain informational only. | — |
| 3 | **Personal ClickUp API token** for the build session — moves view creation (Punch List ×3, Capture Table ×11, Meetings ×5, Action Items ×3, Investors) from [You] to [Claude]. | **YES** — Brandon is creating a personal API token now, stored outside the repo: CLICKUP_API_TOKEN in cloud sessions (or the ClickUp connector), a local secret store on a Mac; never in chat/tasks/docs. View creation moves to **[Claude/REST]**. Field/type/status **definitions** stay [You] regardless (no public API for those). | S0 |
| 4 | **`identified` status** on the Founding Punch List: (a) keep as a retained legacy status or (b) remap → Inbox. | **(b) APPROVED** — explicit exception to Scaling People protection. `identified` → `Inbox` is a **rename**, not a remap (it was already the list's default new-task status), so this changes only the status name on the ~242 Scaling People tasks; nothing else about them changes. Brandon updates his own Scaling People extraction pipeline. | S1 |
| 5 | **Classification gap:** route capital/budget and brand/design items into the existing 7 values, or add values back. | **Add values back** — Classification is **9 labels**: Build/Setup · Recurring/Operating · Governance · Legal/Compliance · Vendor/Procurement · R&D · Admin · Capital/Budget · Brand/Design. No fallback routing needed. | S3 |
| 6 | Optional 10th task type **`Action Item`** (meeting-origin items keep identity after moving to the Punch List). | **YES, created** — 10th task type, enabled on Meetings + Founding Sŏn; default type on the Action Items list (was `Task`). | S1 |
| 7 | **Investors pipeline stages** Prospecting → Contacted → Meeting Scheduled → Diligence → Soft Commit → Committed / Passed (closed). | **Build as proposed.** | S1 |
| 8 | **Action-item destination rule:** confirmed items go only to the Founding Punch List until the funding + lease gate passes; the agent's hint carries field values, not a department space. | **Yes.** | S2 |
| 9 | **Investor seed set → Investor CRM.** Review the ~45 candidate tasks once [Claude] produces the preview table. | **Preview table → Brandon approves the exact list → migrate approved investor tasks out of the Founding Punch List into the Investor CRM → remove the tag** (in that order; design in DECISIONS 2026-09-17). | S3 |
| 10 | **Leftover admin tasks:** supply real names + owners for the three "transfer ownership from brandon", Gmail, Airtable, AirTable, ClickUp, Access Removal. | **Brandon renames and assigns owners himself in ClickUp — Claude does nothing here.** | S3 |
| 11 | **Operating Agreement review items:** you extract each "Dominic Review Required" / "Attorney Review Required" passage (human read); confirm attorney items keep Assignee unset with the reviewer named instead rather than inviting an outside guest. | **Assignee unset + reviewer named in Created By Notes (the renamed "Notes from BJAC" field — no separate Owner Notes field exists); no guest invite.** | S3 |
| 12 | **Stray "Solution" field** on Hospitality "First timer gift": delete or keep. | **DELETE** — [Claude] first copies any value into the task's description, then [You] deletes the field definition. | S3 |
| 13 | **SaaS Map → Doc:** (a) confirm the function-area grouping once the 241-row export is in hand; (b) confirm duplicates/mismatches are merged *after* the Doc replaces the tasks; (c) **final sign-off against the CSV export before any task is removed — recorded in DECISIONS.md.** | **(a) Confirmed after export, (b) merges happen after, (c) sign-off required before removal** — all as proposed. | S3 |
| 14 | **Claude folder loose threads:** "(Temporary)" tracker, "Investment Thesis Architect (staging for Box)". | **Left in place, listed on Docs Home as "unfiled"** — Brandon doesn't recognize them; likely removed later, Brandon decides. | S3 |
| 15 | **Documents folders** for the five doc-less shells (BI, Events, Hospitality, Product, Property): create now for the shell page, or wait for real content. | **Create now** — one empty folder + one page per shell, nothing else. | S2 |
| 16 | ~~**"Notes from BJAC" deletion timing**~~ — SUPERSEDED | The field was **renamed in place** to **Created By Notes** (same field id 52c7d5a1, values kept), not migrated to a new Owner Notes field and deleted. No migrate-then-delete step remains. | — |
| 17 | **Field deletions** after zero-value confirmation: Project (Punch List), Category + Notes (11 Capture lists), Department Crossover (Events, Finance space-level). | **Delete once `clickup_filter_tasks` shows zero populated values; report any field with data before deleting it.** | S3 |
| 18 | **First-4-weeks human review:** you and Dominic read the agent's "what I did" comments weekly before it runs unsupervised. | **Required** — Brandon alone reviews the agent's weekly notes for the first 4 weeks. | S4 |
| 19 | **Location field is read-only by convention only** unless the UI offers a field lock (2-minute check in Stage 1). | **Accept convention if no lock exists**; Location is read-only from Google Calendar. | S1 |
| 20 | **Fundraising target figure** for the "Committed vs Target" card (typed once; no Goal object yet). | **$2,500,000** — used directly on the Committed vs Target card. | S4 |
| 21 | **Prototype retirement:** archive the old Punch List meeting tasks after the side-by-side check; retire "Founders Meeting Assistant" after the new agent's 4-week review. | **As stated.** | S3 / S5 |
| 22 | **"Heejae" Doc** at the People space root. | **ARCHIVE** if ClickUp supports doc archiving; if not, Brandon deletes it himself — Claude never deletes it. | S3 |

Already approved in DECISIONS.md and therefore *not* re-asked: Meetings space + Super Agent engine; 10 task types (incl. Investor/Real Estate); Punch List and Capture status sets; Classification ×9 (built-in Created By/Created By Notes cover owner/notes, no Owner/Owner Notes fields; native TIML covers cross-department, no Cross-Department field; task types cover the old Punch List Phase field); Punch List views by task type; Investor CRM list in Founding Sŏn (replaces the earlier "Investors list" plan); N3 dashboard (optional, later); N6 Docs Home; N8 shell template; SaaS Map → Doc; `investor` tag retirement via migration into the Investor CRM; Founders Team only; Operating Agreement items as tasks; Granola as capture; Google Meet default; Tue 11:00–13:00; rolling 4-week rule; flagged-inbox action items.

---

## 6. Credit budget

All figures are ClickUp AI Super Credits unless stated; rates from research/06 §5 (secondary sources — confirm against Settings → Billing). Everything in this blueprint other than the Meetings Super Agent costs **0 credits**: Brain chat/search, Automations (plan-metered actions, not credits — Business-plan monthly action cap UNCERTAIN, check Settings → Automations), Dashboards, Docs, list/field/view building, MCP reads and writes by Claude, and all migrations. No AI custom fields, no AI auto-classification, no AI Notetaker metering (Granola is the capture tool).

| Item | When | Credits |
|---|---|---|
| Proof test (01 §0.2 steps 2–5, ~6 agent runs) | Stage 0, one-off | 600–1,800 |
| Migration / seeding / Docs build by Claude via MCP | Stages 2–3 | 0 |
| Meetings Super Agent — weekly roll-forward (Automation-gated) | ~4 runs/mo | 400–600 |
| Meetings Super Agent — day-before prep | ~8–10 runs/mo | 1,000–2,000 |
| Meetings Super Agent — cancel/reschedule (@mention) | ~1–2 runs/mo | 100–300 |
| Meetings Super Agent — post-meeting Granola sync | ~8–10 runs/mo | 1,500–3,000 |
| First-month shakedown allowance (re-runs, format drift) | Month 1 only | +1,000 |
| **Steady-state total** | per month | **~3,000–5,900** |

**Against the pools.** Brain AI: 1,500/user → 3,000 (2 founders) or 4,500 (3). Everything AI: 5,000/user → 10,000 or 15,000. On Brain AI the agent alone can exhaust the pool; on Everything AI it uses 20–60%. Overage is sold at $0.001/credit in $10 = 10,000-credit blocks, so the worst-case *marginal* cost of staying on Brain AI is roughly one $10 block per month — cheaper than an Everything AI upgrade ($19/user/mo more) unless the founders also want unlimited Notetaker/Brain MAX. Per decision #2, AI tier and credits are Brandon's call directly — not a blocker or a gate for this blueprint; the figures below are informational only.

**Turn-on order (Stage 4)** to keep spend deliberate, per the "AI on per use case" decision: cancel/reschedule on @mention (near-zero idle cost) → weekly roll-forward (gated) → day-before prep → post-meeting sync. Each trigger is enabled only after the previous one has produced clean "what I did" comments for a full week.

**Guardrail in the agent instructions:** stop and comment rather than retry when a run would exceed its budget (01 §3.1).
