# Sŏn ClickUp — Architect's Digest (Phase 1)

Prepared 2026-09-16 from 15 audit files (`/audit/`) and 5 research briefs (`/research/01`–`05`). Workspace 90131574430, Business plan + AI add-on, 2 members (Brandon, Dominic), 3rd partner pending. All audit calls were read-only; nothing in ClickUp was changed.

Confidence key: **H** = confirmed by audit data or vendor docs; **M** = confirmed in part / inferred; **L** = unverified or contradictory sources.

---

## 1. Current build: state of the workspace

### Headline diagnosis
The workspace is a 13-space, ~960-task shell built for a 20-person company and operated by two people. Roughly **60% of all tasks are machine-generated or ledger entries that nobody triages** (the ~330-task "Scaling People" governance backlog in Founding Punch List and the 241-row Function → SaaS Map). Real, moving work lives in about 120 tasks in one list, plus a handful of well-written Docs. Six of thirteen spaces hold zero or one task. The one genuinely modern pattern in the workspace — the Weekly Founders Sync / Thursday Standup recurring-meeting prototype — is the thing the Meetings project should generalize, not replace.

### What works (keep and build on)
| Asset | Evidence | Why it matters |
|---|---|---|
| **Recurring-meeting prototype** (Weekly Founders Sync, Founders Thursday Standup) | `founding-son.md`: series parent + dated occurrence children; `Meeting`/`Document` custom types in use; rich markdown agenda template (GCal event ID, owner, TZ, per-founder updates, decisions, action items, parking lot); future agendas pre-created for 09-22/09-29; bot creator "Founders Meeting Assistant" (`00-workspace.md` §1) | Already does 70% of the Meetings-space design. Someone (or some agent) is already running it — find out who/what before building. |
| **Live founders' operating list** (~120 tasks in Founding Punch List) | Assigned, due-dated, prioritized; `investor` tag on ~12 tasks | The real backlog; Owner/Classification/views should be designed around these tasks. |
| **Custom task types already exist**: Meeting (1021), Document, Idea (1019) | `00-workspace.md` §3, `product.md` | Workspace-wide types are already turned on; the type set just needs completing and enumerating. |
| **Structured schema in Function → SaaS Map** (Solution 57-option dropdown, AI Opportunity, Launch Phase, Integration Type) | `technology.md` | The only place in the workspace where custom fields carry real data; a model for field design when populated. |
| **Finished Docs**: FDN.01 training module, Finance & Technology Seat Operating Manual, Operating Agreement Pre-Counsel Brief, Sŏn Operating System canon | `people.md`, `finance.md`, `operations.md` | Real institutional content that Brain should be able to surface; proves Docs are the founders' natural writing surface. |

### What is broken or noisy
| Problem | Evidence | Impact |
|---|---|---|
| **Governance backlog buries live work** — ~330 subtasks under "Scaling People: Sŏn Operational Build Out", all status `identified`, unassigned, undated, random priorities | `founding-son.md` | Every default view of Founding Punch List is ~70% noise. This is the single biggest usability failure. |
| **Same program split across three places**: Founding Punch List (~330 subtasks), Operations Carryover Register (126 dense ledger tasks, all `to do`), Operations Docs (Sŏn Operating System) + People folders | `founding-son.md`, `operations.md`, `people.md` | No single home for the operating-system build; cross-references live only in free text and will break on rename/delete. |
| **Six spaces are empty or near-empty**: BI (0), Property (0), Promotion (0), Personal (0), Finance (0 tasks, 1 doc), Product (1 task, two empty folders) | space audits | 13 spaces, 19 chat channels, ~13 Capture lists for two people — navigation cost with no return. |
| **"Capture" template cloned to every space, unused everywhere**: 5 statuses (`revist` typo, `cancelled` colored green), Category/Notes fields never populated, matching per-space "X Capture" chat channels with no messages | all space audits, `00-workspace.md` §5 | Structure that signals process but records nothing; the typo appears in every space's default status. |
| **No ownership, no dates, no status movement outside Founding Punch List** — 0 assignees in Operations/People/Product/Hospitality/Events/Technology; Design has one (on a cancelled task); nothing has ever left the default status in Operations, Technology (SaaS Catalog 46/46 `to do`), or any Capture list | space audits | The planned Owner column has no data to seed; 5–10 statuses per list are dead weight. |
| **Status sprawl without semantics** — Founding Punch List has 10 statuses (`meetings` is a type marker, not a stage; `active queue`/`up next`/`ongoing`/`final steps` overlap); SaaS Catalog has 8 | `founding-son.md`, `technology.md` | Per-space/list statuses cannot be defined until each list's actual workflow is named. |
| **Custom fields exist only at list level; zero workspace/space fields** | `00-workspace.md` §4 | Owner/Classification must be created at workspace ("Everything") scope from scratch. |
| **Field bleed-through**: Hospitality task "First timer gift" carries the 57-option vendor `Solution` dropdown and `Notes from BJAC` from another list | `hospitality.md` | Evidence of tasks moved between lists without field hygiene; shows why fields should be defined once at workspace scope. |
| **Technology data quality**: 241 rows vs "100 functions" claimed; ~10 duplicate pairs (POS/Point of Sale, HRIS/HR Information System…); vendor names spelled differently between SaaS Catalog and the Solution dropdown; SaaS Catalog description promises 7 fields that don't exist | `technology.md` | Cross-list filtering by vendor silently fails; the Dominic tech review will run on dirty data. |
| **Docs loosely filed**: "Heejae" at People root; Claude folder mixes 25+ AI persona profiles with HVAC/grease-trap compliance pages and a page tree unrelated to Sŏn; a page still titled "(Temporary)"; a profile "staging for Box" | `people.md`, `technology.md` | Brain search will return persona prompts alongside restaurant compliance answers. |
| **Events**: 13 vendor leads as third-level subtasks under Design Pop Up Concepts → Sponsors | `events.md` | Invisible in list/board views; overlaps the empty Product › Beverage/Culinary folders. |
| **Legal draft in a shared Docs folder** — Operating Agreement Pre-Counsel Brief with open "Dominic Review Required"/"Attorney Review Required" sections lives in Operations Documents | `operations.md` | Sensitivity and follow-through both untracked; nothing links it to a dated task. |

### Structural smells (patterns, not single defects)
1. **Template-first, work-second.** Spaces, lists, statuses, fields and channels were all stamped from a template before anyone knew what work would land in them. Result: scaffolding everywhere, throughput nowhere.
2. **Subtasks as filing system.** Checklists are unused workspace-wide; nesting (3 levels in Events, ~330 children under one parent in Founding) is doing the job of lists, tags, or a Classification field.
3. **Meaning in prose, not fields.** Session codes, task IDs, doc names and calendar event IDs are embedded in descriptions (Carryover Register, meeting agendas) instead of Relationship/custom fields — searchable, but not filterable, and fragile.
4. **Finance and Technology are one seat** in practice (the Operating Manual says so in its title) but two spaces in ClickUp; likewise Operations and People share one program.
5. **The AI layer is present but opaque.** A negative-ID bot ("Founders Meeting Assistant") is already creating Meeting tasks and posting "A SyncUp Happened" — but the Unified-API layer returned zero entities, so nothing about automations, agents, Teams, roles, views, or task-type definitions is readable through MCP (`mcp-capabilities.md`).

---

## 2. Feasibility matrix

**Headline: 18 requirements → 10 native ClickUp · 5 need Claude · 2 need a 3rd party (Granola) · 1 not possible as specified (workaround available).**

Column notes: "Native" = ClickUp can do it with UI/API/native AI. "Claude" = a Claude Cloud Routine or Claude Code session is the recommended executor. "3rd party" = Granola/Zapier or hardware. Builder: **[Claude]** = can be done through this session's MCP/REST or a Routine; **[You]** = requires the ClickUp web UI, admin rights, or an account decision.

| # | Requirement | Native ClickUp? | Needs Claude? | Needs 3rd party? | Not possible | Recommended owner | Builds | Conf. | Source |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **Meetings space** (space + lists + fields) | Yes | Optional | No | — | ClickUp (system of record) | **[You]** create the Space (MCP has no create_space); **[Claude]** lists, tasks, docs via MCP | H | `mcp-capabilities.md`; `02` §hierarchy |
| 2 | **Recurring meetings with agendas** | Yes — recurring tasks + default task template per list; prototype already live | Yes, for generating a fresh dated agenda per occurrence | No | — | ClickUp structure + Claude generation | [Claude] | H | `founding-son.md`; `01` #15; `02` §templates |
| 3 | **Rolling 4-week creation** | No native "rolling window"; native recurrence shows only the current instance in GCal | **Yes** — weekly Cloud Routine creates tasks + calendar events 4 weeks out | No | — | Claude Cloud Routine (Sonnet 5, weekly cron) | [Claude] | H | `03` #5 #9; `04` #1–#2; `02` #15 |
| 4 | **Google invites with guests, Meet link, location** | Yes via Planner *event* creation (UI) — but no public calendar API, and Super Agent calendar *write* is unconfirmed | **Yes** — Claude's Google Calendar connector does full CRUD incl. guests/Meet | No | — | Claude via Google Calendar connector; ClickUp task holds the event ID | [Claude] | H (Claude path) / L (Super Agent path) | `03` #1 #7; `01` #3; `04` #6 |
| 5 | **Remote default + manual location** | Yes — Planner event has location + video-provider fields | Yes if automated (set `location` on the GCal event; default = Meet link) | No | — | Claude sets defaults; founder overrides on the ClickUp task → Routine syncs | [Claude] | H | `03` #1; `04` §auth model |
| 6 | **Granola IRL notes → ClickUp** | No native Granola integration | **Yes** — Granola connector (Claude) → ClickUp Doc page under the meeting task | Yes — Granola **Business plan ($14/user)** for API/MCP/transcripts; Zapier is the fallback | — | Claude Routine (polling; Granola has no webhooks) | [Claude] + **[You]** confirm Granola tier | M | `03` #10–#11; `04` #6; `05` #13 |
| 7 | **Granola phone notes** | No | Same pipeline as #6 | Yes — Granola iOS: **outbound-only**, one number per account, verification call | Inbound calls cannot be captured (iOS restriction) | Granola on the *calling* founder's phone | **[You]** | M | `03` #12–#13 |
| 8 | **AI Notetaker for remote meetings** | Yes — Zoom/Meet/Teams + SyncUps; needs Planner connected to Google Calendar | No | No | — | ClickUp native | **[You]** enable/verify | H (limits: 60-min video cap, English-only, notes land in a *private* Doc) | `01` #9–#11; `05` #2–#3 |
| 9 | **Thursday phone standup capture** | No | No | Only via Granola outbound (#7) or hardware (Plaud) | **Not possible as an inbound/either-direction cellular call** | Convert standup to Google Meet (Notetaker or Granola desktop) — consistent with "remote by default" | **[You]** decision | H | `03` #12 #15; `01` #9 |
| 10 | **Brain search across notes + transcripts** | Yes — Brain indexes Docs, tasks, comments, chat, attachments | Yes, indirectly: Granola notes must be written into ClickUp Docs (#6) to be indexed | No | — | ClickUp Brain; Claude feeds it | [Claude] pipeline; **[You]** verify Brain enabled + Notetaker private-Doc sharing | M | `01` #7; `05` #3 |
| 11 | **Single Meetings Super Agent with sub-agents** | ClickUp Super Agent: triggers/instructions confirmed; **agent-to-agent handoff not documented**; calendar write unconfirmed | **Yes** — one Claude Cloud Routine as the orchestrator (Claude subagents inside a run are fine) | No | Sub-agents *inside ClickUp* — treat as not available | Claude Routine = brain; optional ClickUp Super Agent = @mention front-end only | [Claude] + **[You]** (whose claude.ai account owns it; GitHub repo) | M | `01` #1 #6; `04` #3 #13–#15; `05` #6 |
| 12 | **Cancel / reschedule handling** | Partial — status change / drag in Calendar; recurring-instance edits don't propagate to GCal reliably | **Yes** — Routine API trigger with fire-payload text, or reconcile ClickUp task ↔ GCal event on each weekly run | No | — | Claude Routine (reconciliation loop) | [Claude] | M | `04` #10; `03` #5–#6; `01` #12 |
| 13 | **Attendees by Team** | Yes for task assignment/@mention (Business plan; Group CRUD in API). **Team as a calendar-invite attendee: unconfirmed** | Yes — Routine expands Team → member emails via Get Groups API before creating the invite | No | — | ClickUp Teams as source of truth; Claude expands | **[You]** create Teams (owner/admin, UI); [Claude] expansion | M | `02` #7–#9; `05` #12 |
| 14 | **Custom task types** | Yes — workspace-wide, ≤16-char names, ≤100 types | No | No | — | ClickUp | **[You]** (UI-only creation; no API) then [Claude] assigns `custom_item_id` | H | `02` #1–#4 |
| 15 | **Statuses per space/list** | Yes — inherit Space→Folder→List; Status Templates reusable; 4 status groups | No (Claude drafts the spec) | No | — | ClickUp | **[You]** apply in UI (no MCP tool; API partial) | H | `02` #5–#6; `05` #10 |
| 16 | **Owner column** | Yes — **People** custom field at "Everything" scope | No | No | — | ClickUp | [Claude] via REST API with a personal token, or **[You]** in UI (MCP cannot create fields) | H | `02` #10 #12; `04` #8 |
| 17 | **Classification field** | Yes — **Dropdown** (single-select) at "Everything" scope; Dropdown↔Labels conversion is not clean | No | No | — | ClickUp | Same as #16 | H | `02` #11–#12; `05` #9 |
| 18 | **Founding Punch List filtered views** | Yes — views fully scriptable via REST API (`cf_{field_id}` filters) | No | No | — | ClickUp | [Claude] via REST (not MCP) or **[You]** UI | H | `02` #14 |

---

## 3. Key risks and blockers

| # | Risk / blocker | Why it matters | Recommended workaround |
|---|---|---|---|
| R1 | **ClickUp Super Agent may not be able to write to Google Calendar** (docs confirm search only). | The whole "Super Agent creates/cancels/reschedules invites" premise hinges on it. | Make the orchestrator a **Claude Cloud Routine** using Anthropic's Google Calendar connector (confirmed full CRUD). Keep a ClickUp Super Agent only as an optional @mention interface. 15-minute live test by Brandon settles it either way. |
| R2 | **No ClickUp calendar API + recurring tasks push only the current instance to GCal.** | Native recurrence cannot deliver a 4-week rolling window of real invites. | Routine creates **four discrete GCal events** (not a GCal recurrence) and four ClickUp Meeting tasks per series each week, storing the GCal event ID in a custom field for reconciliation. |
| R3 | **AI tier and rate limits unknown.** "AI add-on" could be Brain AI (1,500 credits, MCP capped ~300 calls/day) or Everything AI (5,000 credits, unlimited Notetaker, no MCP cap). | A weekly roll-forward plus notes ingestion can exhaust Brain AI credits or the MCP daily cap. | Confirm tier in Settings → Billing. Budget for **Everything AI** once the 3rd partner joins; keep the Routine's ClickUp call count low (batch reads, one write per task). |
| R4 | **Identity: a Routine belongs to one claude.ai account; invites and ClickUp writes carry that person's name; Google Calendar connector is personal.** | Whoever owns the Routine becomes the de facto meeting organizer; leaving/rotating breaks everything. | Decide now (likely Brandon, whose calendar already owns the Sync event). Consider a shared `meetings@son.restaurant` Google account as organizer later. |
| R5 | **Phone standup is not capturable inbound.** Granola iOS is outbound-only, one number per account. | The Thursday standup as a cellular call cannot be reliably recorded by both sides. | Move it to Google Meet (Notetaker or Granola desktop). If cellular must stay: fixed rule "Brandon calls Dominic," Granola registered on Brandon's phone. |
| R6 | **Granola → ClickUp has no native path and no webhooks.** Connector/API need Granola Business ($14/user). | Notes arrive by polling with lag; free tier gives 30-day history and no transcripts. | Confirm Granola Business for all founders. Routine polls the "Sŏn Meetings" Granola folder after each scheduled meeting end time + 30 min; Zapier as fallback. |
| R7 | **Governance backlog (~330) + Carryover Register (126) will pollute every new view, Brain answer, and Owner rollout.** | Restructure applied on top of noise just produces filtered noise. | Decide their fate first (Section 4, H5): archive list, `Reference` task type, or Doc. Do not create Owner/Classification values for them. |
| R8 | **MCP cannot create Spaces, custom fields, statuses, Teams, views, or task types; Unified-API layer is disabled.** | A large share of the restructure is UI-only or needs the REST API. | Two paths: (a) Brandon does UI steps from a Claude-written checklist; (b) Brandon issues a personal API token so Claude scripts fields/views via REST. Task types and Teams stay UI-only regardless. |
| R9 | **Notetaker output lands in a private Doc of the meeting host.** | Other founders (and Brain answers for them) may not see the notes. | Routine or automation moves/links the Notetaker Doc into the Meetings space and shares it; verify Brain visibility with Dominic's login. |
| R10 | **Super Agent / AI output consistency is early-stage; Routines run with no approval prompts and can act on text found in notes.** | Silent bad writes to calendars/tasks. | Narrow scope (create/cancel/reschedule only), idempotent logic (check before create), a weekly "what I did" comment on a control task, and an explicit instruction to treat fetched note content as data. Human review for the first 4 weeks. |
| R11 | **`Cancelled` in the Closed status group is hidden from views by default.** | Cancelled meetings vanish, then get recreated by the roll-forward. | Put `Cancelled` in the Done group or add "include closed" to Meetings views; Routine checks cancelled occurrences before creating. |
| R12 | **3rd partner not yet a member.** | Teams, AI seats, Granola seats, and Owner options all need a third identity. | Design Teams/Owner as role-based (Founders team), add the person on join; confirm AI add-on seat count covers 3. |

---

## 4. Early structural recommendations (hypotheses for Phase 2 interviews)

**H1 — Collapse 13 spaces to ~6.** Test: Founding Sŏn (Punch List) · **Meetings** (new) · Operations & People (one program today) · Guest Experience (Hospitality + Events + Product/Beverage/Culinary — vendor leads already overlap) · Brand & Growth (Design & Visuals + Promotion) · Finance & Technology (the Operating Manual already treats them as one seat; BI folds in). Property and Personal: archive until buildout begins / until a per-founder private need is real. Alternative to test: keep spaces, archive the six empties.

**H2 — Task-type set (≤16 chars):** `Task` (default), `Meeting`, `Action Item`, `Decision`, `Document`, `Idea`, `Reference`. Meeting/Document/Idea already exist. `Action Item` distinguishes meeting outputs from planned work; `Reference` absorbs the governance backlog rows that are knowledge, not work. Enumerate existing types first (UI).

**H3 — Classification = one workspace-wide Dropdown (single-select) on a "workstream" axis**, seeded from the audit's natural groupings: Fundraising · Legal & Entity · Capital & Budget · Real Estate & Buildout · Brand & Design · People & Staffing · Web & Tech Admin · Operating System · Guest Experience · Meetings · Admin/Misc. Test against the alternative of reusing the existing 12-department "Department Crossover" taxonomy so there is one taxonomy, not two. Decide before populating — Dropdown↔Labels is not convertible.

**H4 — Owner = workspace-wide People field, single value; Assignee stays "who does the next action."** Seed with existing assignees on the ~120 live tasks.

**H5 — Quarantine the generated content.** Move the ~330 governance subtasks and the 126 Carryover Register entries into one "Operating System Backlog" list (or `Reference` type, hidden by default view filter), cross-linked to the Sŏn Operating System Doc. Punch List then shrinks to ~150 real items.

**H6 — Meetings space shape:** one list `Meetings` with task type `Meeting`, one task per occurrence, series parent task per cadence (mirrors the prototype). Custom fields: Series, Meeting Type (dropdown), Attendee Team (People/Team), Location (short text, default "Google Meet"), GCal Event ID, Capture Method (Notetaker/Granola/None), Notes Doc (Relationship). Statuses (own template): Scheduled → Prep → Held / Notes Pending → Notes Synced → Cancelled (Done group, see R11). Action items are `Action Item` tasks in the *relevant workstream list*, linked back via Relationship — not stored in Meetings.

**H7 — Three status templates, applied top-down:** *Capture* (Inbox → Triaged → Active → Done → Dropped) · *Work* (Backlog → Next → In Progress → Blocked → Review → Done → Cancelled) · *Meetings* (H6). Fix `revist`; retire the 10-status Punch List set.

**H8 — Teams: one `Founders` Team now**, `Leadership` later; no Team per meeting type. Routine expands Team membership to emails for invites.

**H9 — Retire the per-space Capture channels;** one `Inbox` channel plus per-initiative channels (Programming) that already have identity.

**H10 — Punch List views (scriptable):** My Work · By Owner · By Classification · Investors · Meetings (type = Meeting) · Backlog/Reference (hidden by default).

**H11 — Architecture split:** Claude Cloud Routine owns cross-app mechanics (roll-forward, invites, cancel/reschedule reconciliation, Granola ingest); ClickUp owns structure and record. Test whether a ClickUp Automation "Meeting status → Cancelled" can call the Routine's API trigger via a webhook action, giving founders an in-ClickUp cancel path with no extra UI.

---

## 5. Discovery interview questions for Phase 2 (prioritized)

### A. Meetings system (highest priority)
1. **Who or what is "Founders Meeting Assistant" (user -87977709)?** A ClickUp Super Agent you built, the AI Notetaker, or a manual convention? What does it currently do on Weekly Founders Sync?
2. Which AI tier is active — Brain AI or Everything AI — and does the seat count cover the 3rd partner? (Settings → Billing.)
3. Which recurring meetings exist or should exist? For each: cadence, duration, attendees, remote/IRL default, and capture method (Notetaker vs Granola).
4. Will you move the Thursday standup to Google Meet, or keep it cellular with a fixed "who calls whom" rule?
5. Whose claude.ai account (and Google Calendar) should own the Meetings Routine — Brandon's, or a shared `meetings@` account?
6. Do all founders have (or will they get) Granola Business? Is there a "Sŏn Meetings" folder convention already?
7. When a meeting is cancelled or moved, where do you want to do it — in ClickUp, in Google Calendar, or by telling the agent? (Determines the reconciliation direction.)
8. Should action items live in the Meetings space or in the workstream lists with a link back? Should the existing agenda template stay as-is?
9. How far ahead should invites exist — exactly 4 weeks, or "always the next 4 occurrences"?
10. Is a ClickUp Super Agent front-end (@mention to cancel/reschedule) wanted, or is a ClickUp status change / Calendar edit enough?

### B. Founding Sŏn / Punch List
11. Fate of the ~330-task governance backlog: work it, archive it, convert to a Doc, or `Reference` type? Same for the S1–S17 chapter checklist.
12. Which of the audit's ~11 natural groupings should become Classification values? Keep `investor` as a tag, a Classification value, or both?
13. Keep or drop Next Action / Notes from BJAC / Project fields? Are the "transfer ownership from brandon" ×3 and single-word admin tasks (Gmail, Airtable…) still live?
14. Which of the 10 statuses actually mean something to you today? Which views do you open first each morning?

### C. Operations & People
15. Is the Carryover Register a permanent ledger or a backlog to burn down? Should it merge with the Punch List governance backlog into one Operating System list?
16. Should Operations and People be one space while the Scaling People program is the only content?
17. Who owns the Operating Agreement's open "Dominic Review / Attorney Review" sections, and should it become a dated task? Is Operations Documents the right home for legal drafts?
18. More FDN.xx training modules planned? Should each get a build/review task pipeline, or stay Docs-only? Where should "Heejae" and other candidate notes live?

### D. Technology, Finance, BI
19. Finance and Technology: one seat, one space? Does BI have a purpose yet, or fold it into Finance & Tech?
20. Function → SaaS Map: merge the ~10 duplicate pairs and normalize vendor names before the Dominic review? Build the 7 promised SaaS Catalog fields or trim the description?
21. Claude folder: split personas from compliance references? Can "(Temporary)" and "staging for Box" close out?

### E. Guest Experience (Product, Hospitality, Events)
22. Should Product/Hospitality/Events collapse into one Guest Experience space, with vendor leads (13 Sponsors subtasks) as a flat Vendors list shared with Beverage/Culinary?
23. Is menu/beverage development happening outside ClickUp today (Granola, Docs, spreadsheet)? Import or leave?
24. Does `Idea` remain the type for early concepts, promoted to `Task` once approved?

### F. Brand & Growth (Design & Visuals, Promotion)
25. Is promotion/marketing planning happening elsewhere (agency, deck)? Should Design and Promotion share a space?
26. Split Design Capture into print/signage vs. digital workflow by list, or by Classification?

### G. Property, Personal, workspace hygiene
27. Does lease/buildout work (207 St. Elmo Rd) belong in Property, or stay in the Punch List until construction starts?
28. Personal: private per founder, shared, or delete? What was "Parked" for?
29. Are the per-space Capture channels used at all, or can they go?
30. What roles do you and Dominic hold (Owner/Admin)? What role will the 3rd partner get, and when do they join?

---

## 6. Coverage gaps and how to close them

| Gap | Why it's unverified | How to verify | Who |
|---|---|---|---|
| Teams/user groups, member roles | No MCP tool; Unified API disabled | Settings → People / Teams; screenshot | Brandon (UI) |
| Full custom task-type list | No enumeration tool | Workspace Settings → Task Types; list names + IDs | Brandon |
| Automations, ClickUp Super Agents, and the "Founders Meeting Assistant" bot | Not exposed via MCP | Space Automations panel + AI Agents panel; export/screenshot each rule and agent's instructions | Brandon |
| Calendar sync settings (task sync vs Planner events), Notetaker settings, Brain enabled | Not exposed | Settings → Integrations → Calendar; Planner settings; Brain toggle | Brandon |
| AI add-on tier, credit balance, MCP daily cap | Not exposed | Settings → Billing → AI | Brandon |
| Saved views on Founding Punch List | No views tool | Screenshot view tabs + filters | Brandon |
| Complete Docs inventory (Claude folder, Promotion Documents, Design Documents, Finance Documents) | `clickup_search` capped at 19 fixed results | Open each Docs folder in the UI; or Docs Hub export | Brandon |
| Dominic's reminders and private items | Own-user scope only | Dominic runs `/reminders` or exports | Dominic |
| **Super Agent can create/modify GCal events** (R1) | Docs confirm search only | 15-min test: create a test Super Agent with Calendar tool, ask it to create/move/cancel a test event | Brandon |
| **Team as GCal invite attendee** | Undocumented | Create `Founders` Team; add as participant on a Planner event; check invite recipients | Brandon |
| **Planner recurring event → GCal invite reliability** | Docs vs 5-year-old sync complaint | Create a 4-week recurring Planner event with Meet + guest; check Dominic's Google Calendar | Brandon + Dominic |
| **Notetaker on SyncUps and private-Doc visibility** | Community claim unconfirmed | Run one SyncUp and one Meet with Notetaker; check where Docs land and whether Dominic can find them in Brain | Both founders |
| Which ClickUp MCP server powers this session (official 6-tool vs broader) and whether a REST token is available | Session tool count (38) ≠ documented official set | Check claude.ai connector settings; decide on issuing a personal API token for field/view scripting | Brandon |
| claude.ai account-level connectors (Google Calendar, Granola, ClickUp) for the Routine owner | Routines see only account-level connectors | claude.ai/customize/connectors on the chosen owner account; Routine plan (Pro/Max/Team) | Routine owner |
| Granola plan tier, registered phone number, folder conventions | Not in scope of audit | Granola Settings → Plan; iOS phone-call setup | Each founder |
| help.clickup.com wording on Super Agents/Notetaker | 403 on direct fetch; snippets only | Open the six Help articles cited in `01` while logged in | Brandon (or Claude via browser when allowed) |
| Whether "Department Crossover" is a space-level field in Finance/Events or list-level | `00-workspace.md` says zero space fields but only sampled 3 spaces; `finance.md` says space-level | `clickup_get_custom_fields` on Finance and Events space IDs | Claude (read-only, next session) |
| Exact task counts per grouping in Founding Punch List | Estimated from names, not queried | `clickup_filter_tasks` by parent ID + status once Classification exists | Claude |
