# Technology Space Audit (90136733924)

## Summary

Technology is dominated by one enormous working document: the **Function → SaaS Map** list (241 tasks, not the "100 business functions" its own description claims) paired with a **SaaS Catalog** list (46 tasks, one per vendor). Together these are Brandon's tech-stack planning tool — mapping restaurant business functions to SaaS solutions, ahead of a "Dominic tech review session." The mechanism is clever (dropdown of 57 vendors, AI-opportunity flag, integration type, launch phase) but the data is inconsistently filled in, has ~15-20 duplicate/near-duplicate function rows, and the SaaS Catalog is missing most of the custom fields its own description promises. The **Technology Capture** inbox list is empty (unused). The **Tech Documents** folder holds two sub-folders: **Technology Build Out** (the lists above) and **Claude**, a large, loosely organized library of AI-persona profiles and restaurant compliance knowledge files built for Claude Projects, plus a "Technology OS — Build Hub" doc that reads as raw session/brain-dump notes. No custom task types, no assignees, no due dates anywhere in the space; ClickUp's People-assignment feature isn't used at all — "assigned/not assigned" is just a status label, not a real assignee.

## Details

### Technology Capture (list, id 901327291281)
- Statuses: revist, planning, in progress, complete, cancelled (same 5-status pattern used on every space's "Capture" list workspace-wide).
- **0 tasks.** Completely unused as an inbox/capture mechanism.
- Custom fields available: Notes from BJAC (short text), Notes (text), Category (labels: Asset-Digital, Asset-Physical, Function, Idea) — these look like workspace-shared fields reused across every space's Capture list, not Technology-specific.

### Tech Documents (folder, id 901318761463)
- No lists directly in the folder (just the two sub-folders below).
- 1 Doc directly in the folder: **"Technology OS — Build Hub"** — pages include "Session capture — before the brain-dump tangent," "Dump batch 2 — HR / Payroll / Scheduling," "Dump batch 3 — Customer CRM / Reservations / Loyalty," "The thesis in three voices: pitch examples." Reads as unedited working/scratch notes, not a finished reference doc.

### Claude (sub-folder, id 901318509389)
- No lists — pure document library. 4 docs found (likely more pages not fully paginated):
  - **"Claude Project Review"** — the biggest doc by far. Under a page hierarchy split into "Sŏn Home Base" and a second page tree unrelated to Sŏn (out of scope, not catalogued here), it catalogs 25+ AI persona/role profiles (Brand Designer, Lighting Designer, Sound/Audio Designer, Interior Architect, Typographer, Fashion Designer, Olfactory Designer, Acoustic Engineer, etc.) — but also has restaurant compliance knowledge-base pages mixed into the same tree (HVAC/Walk-In Cooler/Acoustics compliance, Plumbing/Grease Interceptor compliance, Solid Fuel Exhaust Ventilation, Outdoor BBQ Pit compliance, Flooring compliance). Personas and compliance references are commingled under one doc/page tree with no apparent separation.
  - **"Sŏn Master Pointer Index & Inventory"** (retired pointer doc, superseded by the repo `profiles/` master copies) — pages: "How This Works," "Consolidated Project — Custom Instructions (paste into project)," and a page literally named **"Migration & Review Tracker (Temporary)"** that's still live.
  - **"Sŏn — Claude System & Profile Methodology (Research Capture)"** — e.g. "Leg 1 — Thin Pointer-Based Project Architecture (full report)."
  - **"Investment Thesis Architect — Profile (staging for Box)"** — name signals it's meant to move to Box but hasn't.

### Technology Build Out (sub-folder, id 901315929256)

**Function → SaaS Map** (list, id 901323733488)
- Statuses: not assigned / assigned / locked in. ("assigned" here is a status value, not a ClickUp assignee — no task in the space has a real assignee.)
- **241 tasks total** (100 + 100 + 41 across paginated calls), despite the list description stating "100 business functions mapped to confirmed SaaS solutions."
- No priorities, no due dates on any sampled task. Tags used sparingly and inconsistently: `architecture`, `finance`, `ops` on a scattered subset of rows (most rows have none).
- Custom fields: Solution (dropdown, 57 vendor options), Notes from BJAC (short text), AI Opportunity (No/Possible/Yes), Launch Phase (Phase 1/2/3/Pre-Open), Integration Type (Native/API/Manual/TBD). Sampled tasks show inconsistent completion — some have all fields set (e.g. "Google Workspace" review task, well-documented markdown description), others have only "Solution" set with the rest blank.
- **Duplicate / near-duplicate rows**: "Reservation Management" appears twice, "Inventory Management" twice, "Performance Management" twice, "Tip Management" twice, "Payroll" and "Payroll Processing" as separate rows, "POS" and "Point of Sale (POS)" as separate rows, "HRIS" and "HR Information System (HRIS)" as separate rows, "Learning Management (LMS)" and "Learning Management System" as separate rows, "S.O.P Creation" and "S.O.P Storage" as separate near-duplicates. This looks like at least two passes of brainstorming merged without de-duplication.
- Descriptions, where present, are genuinely useful (markdown, well-written, e.g. Google Workspace / Superhuman relationship writeup) — quality is high when filled in, but coverage is uneven.

**SaaS Catalog** (list, id 901327544218)
- Statuses: to do, planning, in progress, at risk, update required, on hold, complete, cancelled (8 statuses defined) — but every sampled task (46/46 reviewed) sits at **"to do."** None of the other 7 statuses appear to be in use yet.
- Priority is used per-vendor (urgent/high/normal/low) — looks like an intentional triage ranking of which vendor to lock in first, a nice touch.
- **Custom-field gap:** the list description promises "category, primary function, functions handled, native integrations, AI native capability, contract status, and launch phase" fields, but the list only actually has **one** custom field defined: "Notes from BJAC" (short text). None of the promised structured fields exist — the description is aspirational/stale relative to the schema.
- **Naming mismatches vs. the Solution dropdown** used in Function → SaaS Map (same vendor, different spelling in each place): "Eleven Labs" (catalog) vs. "ElevenLabs" (dropdown); "Google Business" (catalog) has no matching Solution option; "Restaurant365" (catalog) vs. "Restaurant 365" (dropdown); "APG Solutions — Smart Till" (catalog, em dash) vs. "APG Solutions - Smart Till" (dropdown, hyphen); "Synthesia" (catalog) doesn't exist in the Solution dropdown at all. These will silently break any attempt to cross-reference the two lists.

## Issues / opportunities

1. Function → SaaS Map has real duplication (~10+ pairs) inflating the "100 functions" framing to 241 rows — worth a de-dup pass before the Dominic review session.
2. SaaS Catalog's description references fields that don't exist; either build those custom fields or rewrite the description.
3. Vendor-name spelling is inconsistent between the two lists in the same folder — this defeats the "Filter by Solution to see any tool's full footprint" workflow the list description promises.
4. Technology Capture list is a dead/unused inbox — either wire it into a real capture habit or remove it.
5. The Claude folder mixes two very different content types (AI persona profiles vs. restaurant compliance references) in one doc tree, and carries a page explicitly marked "(Temporary)" that's stuck around.
6. "Investment Thesis Architect — Profile (staging for Box)" signals unfinished migration work.
7. No assignees, due dates, or task types used anywhere in the space — everything currently lives in status + custom fields only.

## Questions for Brandon

1. Is the 241-row Function → SaaS Map count intentional (expanded scope) or should the ~10 duplicate pairs be merged?
2. Should the SaaS Catalog custom fields (category, integrations, AI capability, contract status) actually be built, or should the list description be trimmed to match what exists today?
3. Is the Technology Capture list meant to be used going forward, or is Technology Build Out effectively replacing it?
4. Can "Investment Thesis Architect — Profile" move to Box now, and can the "(Temporary)" migration tracker be closed out?
