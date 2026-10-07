# [You] Checklist — click-paths, in build order

_Only the UI steps. Numbers match `blueprint/05-build-plan.md`; decision numbers (#n) match `blueprint/00-blueprint.md` §5. Tick each box when done and note anything that looked different from the path described — ClickUp's menus move; the target is what matters. Never open, edit or drag a Scaling People task or a Carryover Register entry while doing any of this._

**Where things live:** Workspace avatar (bottom-left) → **Settings** is the workspace-settings hub. A Space's `⋯` (hover the space name in the sidebar) holds Space settings. A List's `⋯` (hover the list name) holds List settings. **Docs Hub** and **Dashboards** are sidebar icons.

---

## Stage 0 — Baseline and proof test (~1 h) — ✅ ALL DONE 2026-09-16

- [x] **0.0 Personal API token (#3, approved).** Done — token stored outside the repo (CLICKUP_API_TOKEN in cloud sessions); unblocked Claude building fields/views via REST for the rest of the build.
- [x] **0.2 Export key Docs.** Done — all 8 pulled via REST, saved under `exports/2026-09-16-baseline/`.
- [x] **0.3a Task-type screenshot.** Done — informed the reconciliation in 1.1 (Action Item, Investor, Real Estate created without duplicating existing types).
- [x] **0.3b AI tier.** Done (informational only — not a gate, decision #2).
- [x] **0.3c Existing Automations.** Done.
- [x] **0.3d Prototype agent tools.** Done.
- [x] **0.4 Proof test.** Done — result (01 §0.2a): Rung 1 for create/update, Rung 2 (Automation) for delete, Granola MCP PASS. Test event/agent cleaned up.
- [x] **0.5 GATE #1.** Closed — rungs recorded in `DECISIONS.md` (2026-09-16). No Rung 3/4 needed.

## Stage 1 — UI prerequisites (~2.5 h) — mostly ✅ DONE 2026-09-16

- [x] **1.1 Task types.** DONE: Action Item (1026), Investor (1027, supersedes Person), Real Estate (1028, supersedes Account) created; Option A reuses Process + Founder Decision. Per-space enablement still pending.
- [x] **1.2 Founders Team.** DONE — Brandon, Dominic.
- [x] **1.3 Workspace fields, as redesigned.** DONE — only **Classification** was created (Labels: Build/Setup · Recurring/Operating · Governance · Legal/Compliance · Vendor/Procurement · R&D · Admin · Capital/Budget · Brand/Design → Everything). **No Owner or Owner Notes fields** — Assignee/built-in Created By cover ownership, and "Notes from BJAC" was renamed in place to **Created By Notes**. **No Cross-Department field** — cross-department reach is native Tasks in Multiple Lists (below), already on.
- [x] **1.4** ~~Punch List Phase field~~ — **not built, dropped.** Superseded by the Investor/Real Estate task types (1.1); Punch List views filter by task type.
- [x] **1.5** ~~Field-lock check (#19)~~ — **answered without a dedicated check.** ClickUp has no per-field read-only lock; Location stays a documented convention only.
- [x] **1.6 Punch List statuses (#4, approved: rename `identified` → `Inbox`).** DONE — 255 tasks renamed. Built: Not Started group `Inbox`, `Later` · Active group `Next`, `Doing`, `Waiting` · Done group `Canceled` · Closed `Done`. **No `Soon`** (dropped from the original draft). Old → new mapped per 02 §2c. Saved as template "Punch List".
- [x] **1.7 Capture statuses.** DONE on all 11 Capture lists: `Captured` (Not Started) · `Developing`, `Ready` (Active) · `Activated` (Done) · `Archived` (Closed), saved as template "Capture". Carryover Register, Function → SaaS Map and SaaS Catalog statuses confirmed unchanged.
- [x] **1.8 Meetings space + statuses.** DONE, as built:
  - [x] Meeting Series: `Active` (Active) · `Paused` (Active) · `Retired` (Closed).
  - [x] Meetings: `Scheduled`, `Prep Sent`, `Held` (Active) · `Canceled` (Done) · `Notes Synced` (Closed) — **no `Rescheduled` status**.
  - [x] Action Items: `Flagged` (Active) · `Dropped` (Done) · `Routed` (Closed).
- [ ] **1.9 Investor CRM statuses** (replaces "Investors statuses" — new design, DECISIONS 2026-09-17) — after 2.2: hover Investor CRM → `⋯` → Settings → Statuses → `Prospect` (Not Started) · `Contacted`, `Meeting Scheduled`, `Diligence`, `Soft Commit` (Active) · `Passed` (Done) · `Committed` (Closed) → Save as template "Investor CRM". **Not yet done** (~5 min, PLAN-2026-09-17-no-ai.md item 3).
- [x] **1.10 Google Calendar.** DONE.
- [x] **1.11 Granola MCP.** DONE — connected "For all members", tested PASS in the proof test.
- [x] **1.12 Meetings Super Agent.** DONE — Brandon built it directly with instructions (01 §3.1) and full scheduled triggers live from the start (Mon 7am roll-forward, daily 8am prep, 2pm/7pm notes sync, DM channel for reschedule/cancel), skipping the "shell first, triggers later" staging this line originally described.

_(1.13 API token moved to Stage 0, step 0.0 — already done by this point.)_

## Stage 2 — Your parts of the MCP builds

- [x] ~~**2.1 Meetings list fields**~~ — **SKIPPED, done differently.** Claude created every field directly via REST (`POST /v2/list/{id}/field`, confirmed creatable this way), so no manual field-building was needed. As-built set (lean, differs from the original draft): Meeting Type, Series relationship, GCal Event ID, **Event Title** (added post-proof-test for the cancel Automation), Capture Source, Location, Notes Doc Link, Attendees on Meetings; one **Schedule** field on Meeting Series (replacing the drafted Cadence/Day-Time/Duration/Default Location/Attendee Team/Active/Next Roll-Forward Date split); Source Meeting relationship + Suggested Destination on Action Items, default type **Action Item**. Statuses applied per 1.8.
- [ ] **2.2 Investor CRM fields** (replaces "Investors fields" — new design, DECISIONS 2026-09-17) — after Claude creates the list via REST. Organization, Email, Phone, Investor Type (Dropdown: Angel/Individual · Family Office · Fund · Lender · Strategic Partner), Check Size (Currency), Committed Amount (Currency), Intro Source, Last Contact (Date), Next Follow-up (Date) — all **[Claude/REST]**; no Owner field (reuses built-in Created By) and no Materials Sent field. Apply the 1.9 status template. **Not yet built.**
- [ ] **2.3 Related Meetings.** Investor CRM → Relationship → Tasks from a specific List → **Meetings** (the list, in the Meetings space) → name "Related Meetings"; the reciprocal field on Meetings is named **Investor**. **[Claude/REST]**, not yet built — depends on 2.2. No rollup columns (follow-ups are subtasks on the record, not a Punch List relationship).
- [ ] **2.5 Task templates.** In Meetings, create one task per file in `templates/` (paste the markdown body into the description; set Meeting Type) → task `⋯` → **Save as Template** → names "Founders Meeting", "Founders Standup", "Investor/Lender Meeting". List `⋯` → **Templates → Default task template → Founders Meeting**. **Not yet done** (PLAN-2026-09-17-no-ai.md item 7).
- [ ] **2.6 Docs Home.** Docs Hub → open "Sŏn Docs Home" → `•••` → **Create a wiki**. Then `•••` → **Pin** (or drag to Sidebar → Pinned). **Not yet done** (PLAN-2026-09-17-no-ai.md item 8).
- [x] **2.9 Agent tools** (per GATE #1) — **DONE for the cancel path.** AI Agents → Meetings Super Agent → Skills → Add tools: Google Calendar create/update (Rung 1) and Granola tools, both live. Meetings space → Automations → "Remove Event On Status Update": *When* status → Canceled ⇒ *Then* Google Calendar Delete event, Keywords = Event Title field — tested working. The originally-drafted separate "gate" Automations (roll-forward date arrives / due date tomorrow → run agent) were **not built** — Brandon's agent runs on its own scheduled triggers instead (1.12). No reschedule/location Automations exist or are planned (decision, 2026-09-17) — reschedule stays the agent's job, location stays manual. **Handoff Automations** (new, 2026-09-17): Action Items status → Routed ⇒ move task to Founding Punch List; Capture status → Activated ⇒ add task to Founding Punch List — build these, then Claude tests on throwaway tasks for you to delete.
- [x] ~~**2.10 Views**~~ — **SKIPPED.** Decision #3's API token moves all view creation to [Claude/REST] (Punch List — Action Items default + Real Estate by task type, no "Investors" view; Capture Table ×11; Meetings ×5; Action Items ×3; Investor CRM — Pipeline board default, Table, Follow-ups Due, Committed) — Claude builds these via `POST /v2/list/{list_id}/view`, nothing for you to do here. **Not yet built** (PLAN-2026-09-17-no-ai.md item 4).

## Stage 3 — Approvals and manual migration steps

- [ ] **3.2 Prototype side-by-side (#21a).** Open each new Meetings task next to its Punch List original — migrated **as history** (decision, 2026-09-17) — (Claude's preview file lists the pairs). If nothing is missing: on each original → `⋯` → **Archive** (not delete — Claude never deletes). Then Founding Punch List → `⋯` → Settings → Statuses → remove `meetings` (it should be empty).
- [ ] **3.5 Investor migration review (#9).** Edit Claude's preview table (which tasks migrate into the Investor CRM, as a record or a follow-up subtask, and which stay in the Punch List). Return the approved table. Part of the batched preview review (PLAN-2026-09-17-no-ai.md item 9).
- [ ] **3.6 Delete the `investor` tag definition** — after Claude reports every tagged task has migrated: hover Founding Sŏn space → `⋯` → **Settings → Tags** → `investor` → Delete (only if usage shows 0).
- [ ] **Before 3.8:** #5 is already resolved (Classification is 9 labels, see 00 §5) — nothing to answer. **#10 (leftover admin tasks) is entirely your own step in ClickUp** — rename each task and set Assignee/Classification yourself directly (02 §8); there's no mapping to send Claude, since Claude takes no action on these tasks.
- [ ] **3.9 Operating Agreement passages (#11).** Docs Hub → Operations Documents → Operating Agreement — Founder Pre-Counsel Brief → read each section; copy every "Dominic Review Required" / "Attorney Review Required" passage with its section title into a note for Claude. Do not edit the Doc.
- [ ] **3.10 Claude folder page moves (#14).** Docs Hub → Tech Documents → Claude → Claude Project Review → for each persona page: page `•••` → **Move** → "Claude - AI Persona Library"; for each compliance page → Move → "Technology - Compliance References". Decide "(Temporary)" / "staging for Box".
- [ ] **3.11 SaaS Map sign-off (#13).** Open "Technology - Function → SaaS Map" and "Technology - SaaS Catalog" Docs beside the CSV export Claude produced; check the five verification items in 04 §6 Step 3 are green; write the sign-off line into `DECISIONS.md`. **No list is removed today.**
- [ ] **3.12 Field deletions (#17)** — only after Claude confirms zero populated values: column header `⋯` → **Delete field** for Project (Founding Punch List) · Category and Notes (each Capture list — if the field is shared, one delete removes it everywhere; check the warning text) · Department Crossover (Events, Finance — superseded by native Tasks in Multiple Lists). No "Notes from BJAC" deletion — it was renamed in place to Created By Notes, not migrated-then-deleted.

## Stage 4 — Agent live — mostly ✅ DONE 2026-09-16, paused 2026-09-17 for credits

Brandon built the agent with all triggers live from day one instead of turning them on one a week; this stage's actual order was:

- [x] **4.1 GATE #18.** DONE — founders' 4-week review commitment recorded.
- [x] **4.2 Seed.** DONE — 8 occurrences created Sep 17–Oct 13, Meet links, both founders invited, GCal Event ID + Event Title set, no duplicates.
- [x] **4.3 Cancel/reschedule via DM/@mention.** DONE — tested: canceling a task deletes its event via the Event Title Automation.
- [x] **4.4 Weekly roll-forward — live, Mon 7am.** DONE.
- [x] **4.5 Day-before prep — live, daily 8am.** DONE, but **currently paused**: AI credits are at 0 during a pricing negotiation, so scheduled runs may be getting skipped (PLAN-2026-09-17-no-ai.md) — check and have the agent catch up once credits return.
- [x] **4.6 Notes sync — live, daily 2pm/7pm.** DONE, also paused. The agent's Event Title/Job 4 instruction update is still pending confirmation once credits return (STATE.md resume item 1).
- [ ] **4.7 Dashboard (#20)** — optional, later (DECISIONS 2026-09-17). Sidebar **Dashboards → + New Dashboard** → "Fundraising & Runway" → **+ Add Card** per 03 §N3.1: Pipeline by Stage (Bar/Pie, source **Investor CRM**, group by Status) · Committed to Date (Calculation, sum Committed Amount) · Committed vs Target (Calculation + type the target into the card description) · Follow-ups Due (Task list, Investor CRM, Next Follow-up ≤ 7 days) · Stalled Relationships (Task list, Investor CRM, Status not Committed/Passed, Last Contact > 21 days ago) · Check Size by Stage (Bar) · Recent Investor Meetings (Task list, Meetings list, Meeting Type = Investor/Lender, sort due date desc). No Materials Sent Tracker or Open Follow-up Tasks card — those fields/relationships don't exist in the current design.
- [ ] **4.8 Weekly review** ×4: in the Founders Meeting, read the agent's "what I did" comments on both Meeting Series tasks; log problems as Action Items. **Paused with the agent** during the no-AI window.

## Stage 5 — Close-out

- [ ] **5.4 Brain check as Dominic.** Dominic signs in → Brain → ask for last week's Founders Meeting decision and for a fact from the Finance Operating Manual → both should surface. Waits for AI credits.
- [ ] **5.5 Retire the prototype (#21b).** AI Agents → "Founders Meeting Assistant" → `⋯` → Delete (or Disable). Waits for the 4-week review to resume and complete.
- [ ] **5.6 Archive the SaaS lists** — only if #13(c) is signed: hover Function → SaaS Map → `⋯` → **Archive**; same for SaaS Catalog. Archive, never delete.
- [ ] **5.8 3rd partner** (when they join): Avatar → Settings → People → Invite as **Admin** → Teams → Founders → add · Billing → confirm AI seat · Granola Business seat · send them the Sŏn Docs Home link.
