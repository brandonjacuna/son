# 04 — Knowledge, Docs & Governance

Section of the Phase 3b blueprint. Covers: N6 (Docs Home + naming + Claude-folder split + meeting-notes sharing), N8 (department shell template), and the Function → SaaS Map → Doc rebuild (with export/verification/approval gate). Grounded in `audit/*.md`, `research/06`, `research/07`, `research/09`, `research/11`, `research/12-opportunity-shortlist.md`, STATE.md, DECISIONS.md. Nothing here touches Scaling People tasks or the Carryover Register; no department content is invented — the one filled shell example (§3) uses only facts already in `audit/property.md` and `research/09-opp-department-shells.md`.

Every step below is tagged **[You]** (ClickUp UI, no MCP tool exists) or **[Claude]** (this session's ClickUp MCP: `clickup_create_document`, `clickup_create_document_page`, `clickup_update_document_page`, `clickup_list_document_pages` / `clickup_get_document_pages`, `clickup_filter_tasks`, `clickup_get_task`, `clickup_search`). Claude is READ-ONLY in this session — every [Claude] step below is a proposed action for the build phase, not something executed while drafting this blueprint.

---

## 1. Docs Home page (N6)

### Current state (audit facts)
Docs are scattered one folder per space with no cross-linking: Operations Documents, Design Documents, Finance Documents, People Notebooks + Education/Training Modules, Promotion Documents, Tech Documents (with sub-folders Claude and Technology Build Out) — `00-workspace.md` §6. There is no "list all docs" MCP tool and no existing Home/index page. Real, finished content already lives here and would benefit immediately from a single entry point: the FDN.01 training module (`people.md`), the Finance & Technology Operating Manual (`finance.md`), the Operating Agreement Pre-Counsel Brief (`operations.md`), the Sŏn Operating System canon (`operations.md`).

### Design
One canonical Doc, **"Sŏn Docs Home,"** created at workspace ("Everything") scope so it is visible to every space, promoted to a ClickUp **wiki** (CONFIRMED native feature — `research/11` §A1) so it carries its own permissions layer and shows as the workspace's front door. Its home page is a single-screen index, one row per space, linking every Doc/Doc-folder found for that space in the audit:

| Space | Docs linked from Home |
|---|---|
| Founding Sŏn | Founding Punch List (Action Items / Investors / Real Estate-Lease views), Investors list (03 §N2), Fundraising & Runway Dashboard (03 §N3) |
| Meetings | Meetings list, Action Items inbox, the meeting-notes Doc pages (01 §1) |
| Operations | Operations Documents (Sŏn Operating System, Scaling People: Translation Program, Founder Bios, Operating Agreement Pre-Counsel Brief) |
| People | People Notebooks (Interviews Notebook), Education/Training Modules (FDN.01), "Heejae" (currently at space root — flag for Brandon, not moved) |
| Finance | Finance Documents (Finance & Technology Operating Manual) |
| Technology | Tech Documents → Technology OS – Build Hub; Claude sub-folder split (§3); "Technology - Function → SaaS Map" and "Technology - SaaS Catalog" Docs once built (§6) |
| Design & Visuals | Design Documents (currently empty — link placeholder) |
| Promotion | Promotion Documents (currently empty — link placeholder) |
| Operations/People/Finance/Design/Promotion/Technology/BI/Events/Hospitality/Product/Property | Each shell's Department Shell Doc page once built (§5) |

A "Start Here" convention (CONFIRMED pattern, `research/11` §A1) — the Home page is the only Doc anyone should open first; everything else is reached by clicking through it, not by searching the sidebar.

### Build steps
1. **[Claude]** `clickup_create_document` — name "Sŏn Docs Home," parent = workspace ("Everything"), `create_page: true`.
2. **[Claude]** `clickup_create_document_page` — build the index table above as the home page, `content_format: text/md` (Markdown tables render as ClickUp Doc tables — CONFIRMED, `research/06` §4).
3. **[You]** Docs Hub → open "Sŏn Docs Home" → **Create a wiki** (promotes the Doc; sets workspace-visible permissions). Click-path: Docs Hub sidebar icon → the Doc's `•••` menu → "Create a wiki."
4. **[Claude]** Both `clickup_list_document_pages` and `clickup_get_document_pages` require a `document_id`, not a folder ID — there is no MCP tool that lists the Docs living inside a Folder, so "check each folder" has to go through `clickup_search` first: `clickup_search` with `filters.asset_types: ["doc"]` and `filters.location.categories: [<folder_id>]` to discover each folder's Doc IDs, then `clickup_list_document_pages`/`clickup_get_document_pages` per discovered `document_id` to confirm every linked Doc still resolves (the audit's doc inventory is a lower bound — `clickup_search` is capped at ~19 results regardless of query, `00-workspace.md` §6 — so this pass may surface Docs the audit missed, and may also *miss* Docs past the cap; add anything found to the index rather than silently dropping it, and flag the cap to Brandon if a folder is suspected to hold more Docs than the search returns).
5. **[You]** Pin "Sŏn Docs Home" in the sidebar (Business plan supports pinning a Doc) so it's the first thing either founder sees on login.

---

## 2. Naming conventions (docs, tasks, lists)

Per `research/11` §A2 (CONFIRMED, consistent across every source) and the digest's own finding that IDs get buried in prose instead of fields (`00-digest.md` structural smell #3):

| Object | Convention | Why |
|---|---|---|
| **Doc** | `[Space/Topic] - [Doc purpose]` — e.g. "Finance - Operating Manual," "Property - Buildout Skeleton" | Sorts and scans by department first; matches the audit's own naming for the strongest existing doc ("The Finance and Technology Seat: Operating Manual"). |
| **Doc page (procedure)** | `How to [action]` — e.g. "How to reschedule a Founders meeting" | CONFIRMED convention (`research/11` §A2); makes SOP pages self-describing in a page-tree view. |
| **Task** | Short, front-loaded, no embedded IDs/codes — the calendar event ID, session code, or doc reference goes in a **field** (GCal Event ID field, Relationship field), never in the title or description prose | Directly fixes the confirmed pattern where Carryover Register session codes and meeting-agenda calendar IDs are typed into text and break silently on rename (`00-digest.md` structural smell #3; `research/06` §2). |
| **List** | Plain department noun, no prefix/code (Sŏn's structure already mostly follows this) | Reserves prefixes for task-level naming only, keeps the sidebar hierarchy scannable (`research/11` §B6). |
| **Doc tags** | A separate, smaller tag set from the task Classification field — Docs have their own native "Doc tags" feature (Workspace vs Private scope), distinct from task tags (CONFIRMED, `research/11` §A5) | Prevents assuming the 7-value Classification field also applies to Docs; sequence a Doc-tag set only after Classification is locked. |

This convention itself should be **written down as the first page of Sŏn Docs Home** (self-enforcing per `research/11` §A2) — **[Claude]** adds it as a page when building the Home doc (§1 step 2).

---

## 3. Technology > Claude folder: separate personas from compliance references

### Current state (audit fact, `technology.md` §Claude sub-folder)
One doc, **"Claude Project Review,"** carries 25+ AI persona/role profiles (Brand Designer, Lighting Designer, Sound/Audio Designer, Interior Architect, Typographer, Fashion Designer, Olfactory Designer, Acoustic Engineer, etc.) **commingled in the same page tree** as restaurant compliance knowledge-base pages (HVAC/Walk-In Cooler/Acoustics, Plumbing/Grease Interceptor, Solid Fuel Exhaust Ventilation, Outdoor BBQ Pit, Flooring compliance) — plus a second, unrelated business ("Event Co – The Josephine") nested under the same tree, a page named literally **"(Temporary)"** still live, and **"Investment Thesis Architect — Profile (staging for Box)"** signaling an unfinished migration. This is the exact case `research/11` §A3 warns about: Brain search returns whatever is in scope for a query with no separation, so an HVAC compliance question and a persona prompt can surface side by side.

### Design
Split the **Claude** sub-folder into two Docs (not two folders full of loose pages — ClickUp Docs support nested sub-pages, so each becomes one Doc with its own page tree):

1. **"Claude - AI Persona Library"** — every persona/role profile page, the Master Pointer Index & Inventory, the Profile Replacement Queue, the Claude System & Profile Methodology research.
2. **"Technology - Compliance References"** — every HVAC/Walk-In Cooler, Plumbing/Grease Interceptor, Solid Fuel Exhaust Ventilation, Outdoor BBQ Pit, and Flooring compliance page, filed as Technology/Property-facing reference material, not AI tooling.

(Names follow the `[Space/Topic] - [Doc purpose]` convention in §2.)

"Event Co – The Josephine" stays where Brandon decides (a separate initiative, not part of Sŏn's build — flagged, not moved, without his call) but must not remain nested inside either new Doc.

### Build steps
1. **[You]** Open "Claude Project Review" in the Docs editor and confirm the full page tree (the audit's hierarchy call doesn't expand doc-internal pages — `00-workspace.md` §6 — so a human pass is needed to see every page before moving anything).
2. **[Claude]** `clickup_create_document` ×2 — "Claude - AI Persona Library" and "Technology - Compliance References," both parented under Tech Documents.
3. **[You]** Move each existing page into the matching new Doc (no MCP move-page tool exists — confirmed gap, same class of limitation as `research/12` N6's "[You] moves Docs"). Click-path: open the source page → `•••` → "Move page" → pick destination Doc.
4. **[You]** Decide and act on: "(Temporary)" migration tracker (close out or keep), "Investment Thesis Architect — Profile (staging for Box)" (move to Box or leave), "Event Co – The Josephine" (its own space, or stays parked here) — three open questions the Technology audit already raised (`technology.md` §Questions) that this split forces a decision on.
5. **[Claude]** Add both new Docs to the Sŏn Docs Home index (§1) under Technology.

---

## 4. Meeting notes: shared and Brain-indexed

### Risk (CONFIRMED, `research/11` §A3)
AI Notetaker output — including Personal Notetaker mode — writes to a **private Doc visible only to the meeting host** by default; it is not auto-shared with other attendees, and Brain search only surfaces content a user can already see. With 2–3 founders, an unshared Notetaker Doc is a single point of failure for institutional memory (sharpens digest risk R9, `00-digest.md`).

### Design
The Meetings-space workflow (owned by the separate Meetings blueprint section) must treat "share/index the notes" as a mandatory step on every Meeting task, not a default to trust:
- **Granola path (the chosen primary capture tool per DECISIONS.md):** notes are written into a **shared ClickUp Doc page under the Meeting task**, not a private Doc — this is already the plan and already avoids the Notetaker trap; this section's contribution is naming it explicitly as a knowledge-architecture requirement, not just a meetings-mechanism detail.
- **Notetaker path (fallback only, per DECISIONS.md):** if ever used, the Meeting task's workflow must include an explicit "move/share the Notetaker Doc into the shared Meetings space" step before the task can be marked notes-synced. **[You]** verify Brain visibility with Dominic's login after the first Notetaker-fallback use, since sharing a Doc doesn't retroactively confirm the other founder's Brain index picked it up.
- Every meeting-notes Doc gets linked from the Sŏn Docs Home index once the Meetings space exists, and every Meeting task keeps its **Notes Doc Link (URL field, 01 §1.3)** pointing at its notes Doc page — a URL field, not a Relationship field, because Relationship custom fields target tasks, not Doc pages (per the naming convention in §2 — no notes-doc IDs in task description prose).

This is a cross-reference into the Meetings blueprint section, recorded here because it is fundamentally a knowledge-governance rule (what gets indexed and who can find it), not a scheduling mechanism.

---

## 5. Department Shell Template (N8)

Per DECISIONS.md: approved as a **template, not a heavy register** — stays close to the shells' current state; content gets filled in by the Scaling People work over time; **do not invent department content ahead of that work.**

### Template shape
One Doc page per department shell, added to each space's existing Documents folder (Operations Documents, Design Documents, Finance Documents, People Notebooks, Promotion Documents, Tech Documents, plus a first Documents folder for the currently doc-less shells: BI, Events, Hospitality, Product, Property). Four fixed sections, deliberately short:

```
# [Department] — Shell

## Purpose
One or two sentences: what this department will own once it's live.

## Now / Construction / Opening
- Now: what exists in ClickUp today (facts only — cite the audit).
- At construction: what activates once the lease is signed and buildout begins.
- At opening: what activates once the space is running.

## Activation signal
The single concrete event that flips this shell from dormant to active.

## Activation checklist
- [ ] (left empty — filled in by the Scaling People work / founders, not invented here)
```

The "Now / Construction / Opening" and "Activation signal" language is drawn directly from `research/09-opp-department-shells.md`'s per-department proposals, which were themselves built only from `audit/*.md` facts plus general restaurant-pre-opening sourcing — this template reuses that structure but the **checklist stays blank** at build time, honoring "don't invent department content."

### Build steps
1. **[Claude]** `clickup_create_document_page` requires a `document_id` — it cannot target a Folder directly, so a page can't be dropped "inside that space's Documents folder" without a Doc to hold it first. For each of the 11 department spaces: `clickup_create_document` (parent = that space's Documents folder, `type: "5"` — creating a minimal Documents folder first via `clickup_create_folder` for the 5 shells that don't have one: BI, Events, Hospitality, Product, Property), then `clickup_create_document_page` inside that new Doc, using the template above filled in **only** with the "Now" facts already in `audit/*.md` and the Purpose/Activation-signal language already drafted in `research/09` (not new invented content). (Matches `05-build-plan.md` Stage 2.7, which already sequences this correctly — this step was reworded to match, not to introduce a new step.)
2. **[You]** Review each filled shell page; the Activation checklist rows are added later, by Brandon/Dominic or as the Scaling People extraction reaches relevant chapters — not by this build pass.
3. **[Claude]** Link every shell page from Sŏn Docs Home (§1).

### Filled example — Property

This is the one worked example, built only from `audit/property.md` and `research/09-opp-department-shells.md` (§Property), both already-approved reference material:

```
# Property — Shell

## Purpose
Owns the lease, landlord relationship, the buildout/construction project, permits tied to
the physical space, and facility maintenance once open.

## Now / Construction / Opening
- Now: functionally empty. One list, Property Capture (901327291277), 0 tasks. No folders,
  no docs, no other content found via space search. Same 5-status Capture template as every
  other space (revist/planning/in progress/complete/cancelled), unused since the list is empty.
- At construction: becomes the busiest department in the workspace. FF&E/OS&E procurement
  must start the moment the lease is signed (confirmed 4-month lead time for standard items,
  longer for custom-branded items), not when construction finishes. Phased permitting
  (shell permits submitted before full interior plans) can compress the schedule.
- At opening: final inspections cluster right before opening (health pre-opening → fire
  final → building final, in that order) and gate the soft opening.

## Activation signal
Lease signed. Per STATE.md, this is also the trigger for the workspace-wide rule that all
active tasks live in the Founding Punch List to lift.

## Activation checklist
- [ ] (left blank — filled in when the lease is signed, not before)
```

Note: the "Buildout" list and "Permits & Licenses" tracker `research/09` proposes for Property are **skeleton ideas for after lease signature**, not something this template pre-builds — consistent with "all active tasks stay in the Founding Punch List until past funding + lease" (STATE.md hard constraint). The shell page documents the shape; it does not create the list.

---

## 6. Function → SaaS Map → Doc rebuild (lossless, with verification gate)

### Current state (audit facts, `technology.md`)
- **Function → SaaS Map** (list `901323733488`): 241 tasks (not the "100 functions" the list description claims). Fields: Solution (57-option dropdown), Notes from BJAC (short text), AI Opportunity (No/Possible/Yes), Launch Phase (Phase 1/2/3/Pre-Open), Integration Type (Native/API/Manual/TBD). Status: not assigned / assigned / locked in. Tags used sparingly: `architecture`, `finance`, `ops`. Descriptions present on some tasks are well-written markdown; coverage is uneven. ~10+ duplicate/near-duplicate function-name pairs (Reservation Management ×2, Inventory Management ×2, Performance Management ×2, Tip Management ×2, Payroll vs Payroll Processing, POS vs Point of Sale, HRIS vs HR Information System, Learning Management (LMS) vs Learning Management System, S.O.P Creation vs S.O.P Storage).
- **SaaS Catalog** (list `901327544218`): 46 tasks, all at status "to do." Priority used per-vendor (urgent/high/normal/low). Only one custom field actually exists — Notes from BJAC — though the list description promises category/primary function/functions handled/native integrations/AI native capability/contract status/launch phase (aspirational, not built).
- **Cross-reference breaks today:** vendor-name spelling mismatches between the two lists (Eleven Labs vs ElevenLabs; Google Business in Catalog has no Solution match; Restaurant365 vs Restaurant 365; APG Solutions em-dash vs hyphen; Synthesia in Catalog doesn't exist in the Solution dropdown at all).
- **Related doc:** "Technology OS — Build Hub" (Tech Documents folder) contains raw brain-dump pages already organized by function-area batch — "Dump batch 2 — HR / Payroll / Scheduling," "Dump batch 3 — Customer CRM / Reservations / Loyalty" — the closest existing evidence of a natural function-area grouping axis, to be confirmed against the actual 241 rows at build time rather than assumed complete here.

### Design principle
DECISIONS.md and STATE.md are explicit: **export → verify nothing lost → Brandon approves → only then remove tasks.** Every field, mapping, and note must be kept. This plan does not merge or drop the ~10 duplicate pairs during the rebuild — duplicates get carried into the Doc as-is, flagged, and left for Brandon to merge afterward in the Doc (merging before export risks silently losing one side of a pair; "lossless" means the Doc has to contain everything the tasks had, even messy).

### Step 1 — Full field-by-field export (baseline, before any Doc work)
**[Claude]** Confirmed empirically (this session, read-only call against a 4-task list): `clickup_filter_tasks` returns only a compact per-task summary — id, name, status, priority, assignees, tags, due_date, dates, list — **no custom field values and no description**, and it has no `include`/expand parameter to add them. A "full field-by-field export" therefore needs two passes, not one: (a) `clickup_filter_tasks` (paginated, `include_closed: true`) over both lists to enumerate every task ID (241 + 46 rows) — tags and status *do* come back at this stage, so no second call is needed for those two fields; (b) `clickup_get_task(task_id, include: ["custom_fields", "description"])` **per task ID** to pull the actual custom field values (Solution, Notes from BJAC, AI Opportunity, Launch Phase, Integration Type; Priority is already in (a)) and the full markdown description. That's ~287 individual `get_task` calls, not a handful of paginated `filter_tasks` calls — size the time estimate in `05-build-plan.md` accordingly. Written to a local CSV (one for each list) — this is the audit-trail baseline both the verification checklist and DECISIONS.md's "export it" mandate point at, kept independent of the Doc.

### Step 2 — Doc structure: one page per function area
- **[Claude]** `clickup_create_document` — "Technology - Function → SaaS Map" Doc, parent = Technology space (Tech Documents folder), `create_page: true`.
- One page per function area (grouping confirmed against the actual 241 rows at build time, using the Build-Hub dump-batch categories as a starting axis — e.g., HR/Payroll/Scheduling, Customer CRM/Reservations/Loyalty, Finance/Accounting, Operations/BOH, Marketing/Guest-facing, Architecture/Infrastructure — not finalized here since it must be checked against real data, not assumed).
- Each page holds a Markdown table, one row per function-map task, columns = every field from Step 1 (Function name, Solution, AI Opportunity, Launch Phase, Integration Type, Notes from BJAC, Status, Tags, Description excerpt or link to full text if too long for a cell).
- A second Doc, **"Technology - SaaS Catalog,"** same pattern: one table, all 46 vendors, every field including Priority.
- A **"Duplicates & Mismatches"** page carries the ~10 duplicate pairs and the vendor-name spelling mismatches verbatim from the audit, as open items for Brandon — not silently resolved by the rebuild.

### Step 3 — Verification checklist (before any task is touched)
1. **Count reconciliation:** Doc table row count == exported CSV row count == live ClickUp task count, for both lists (241 + 46), checked **after** every page is written, not assumed from the export alone.
2. **Field-by-field spot check:** for a sample (all 46 Catalog rows, since that's small enough to check in full; a random ~10% sample plus all rows carrying a filled Solution field for the 241-row map) — every custom field value in the Doc matches the corresponding value in the CSV export and in the live task.
3. **Description fidelity:** markdown descriptions render correctly as Doc content (no truncation, no lost formatting) — spot-checked against the well-documented examples the audit already flagged (e.g., the Google Workspace review task).
4. **Duplicate/mismatch carry-through:** every duplicate pair and every naming mismatch identified in `technology.md` appears on the Duplicates & Mismatches page — nothing quietly merged or dropped.
5. **Cross-reference integrity:** every Solution-dropdown value used in the Function → SaaS Map table has a corresponding row (however misspelled) in the SaaS Catalog table, and vice versa — confirms the Doc actually replaces the "filter by Solution" workflow the original list description promised, once names are reconciled.

### Step 4 — Approval gate
**[You]** Brandon reviews the finished Doc against the Step-1 CSV export (and, if desired, the live tasks) and signs off explicitly — recorded as a DECISIONS.md entry — before any Function → SaaS Map or SaaS Catalog task is removed. Nothing is deleted as part of this build step; task removal is a separate, later action gated on this sign-off, not bundled into the rebuild.

### Step 5 — After approval (not part of this rebuild's scope, flagged for later)
- Merge/dedupe the ~10 duplicate pairs and reconcile vendor-name spelling **in the Doc**, where Brandon can review the merge before it's final (per the Technology audit's own recommendation, `technology.md` §Issues #1–3).
- Only then: **[You]** or **[Claude]** (if Brandon issues a personal API token, per `research/06` §4 field/task edit surface) removes the now-redundant tasks from the two lists.
- Link the finished "Technology - Function → SaaS Map" and "Technology - SaaS Catalog" Docs from Sŏn Docs Home (§1) and from the Technology department shell page (§5).
- **Also gated on this approval:** deleting the "Notes from BJAC" field if it turns out to be one shared field ID across lists (02 §3, Owner Notes step 5).

---

## Open questions for Brandon (this section)

1. Function-area grouping for the SaaS Map Doc's per-page split — confirm the Build-Hub dump-batch categories are the right axis, or propose different groupings once the full 241-row export is in hand.
2. Whether to merge the ~10 duplicate pairs and reconcile vendor-name spelling **before** or **after** the Doc replaces the tasks (this plan defaults to after, in the Doc, per the lossless principle — confirm).
3. "Event Co – The Josephine" inside the Claude folder split (§3) — separate space, stays parked, or something else; not decided here.
4. Whether "(Temporary)" migration tracker and "staging for Box" profile (§3) can close out now or need to wait on something.
5. Whether any of the 5 doc-less shells (BI, Events, Hospitality, Product, Property) should get their Documents folder created now (as part of N8's build) or wait until the shell has real content to justify it.
