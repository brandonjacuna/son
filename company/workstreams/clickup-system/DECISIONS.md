# DECISIONS (newest first)

## 2026-10-04 (capture)
- **Granola is retired.** It cannot ingest audio at all (live capture only), so external mics can never reach it, and its in-person speaker ID was unreliable.
- **Remote and phone meetings: Google Meet + ClickUp AI Notetaker** (native), until RingCentral or similar brings business call recording. Capture Source = AI Notetaker.
- **In-person Founders Meeting: Wispr Flow notetaking** on Brandon's paid account. It separated speaker 1 and 2 correctly even from a mono file; the earlier failure was a free-account usage limit, not the feature. Capture Source = Wispr Flow (add the option).
- **Ad-hoc calls:** Apple recording, filed only when pertinent.
- **Hardware fact kept for later:** the DJI Mic 3 receiver in Stereo mode presents 2 separate channels to the Mac (TX1 left, TX2 right, about 30 dB isolation, verified 2026-10-04). Channel-based transcription was dropped on 2026-10-04: AssemblyAI is not being used and scripts/meeting_transcript.py is dead code kept only as a record of the test. The hardware fact stays here in case attribution ever needs revisiting.
- **Filing path for any transcript that has no native route:** scripts/file_transcript.py writes it into the meeting type's notes Doc, sets Notes Doc Link and leaves the meeting at Held; filling that field triggers the agent to summarize and set Notes Synced.

## 2026-10-04 (capture stack settled, from the transcription session)
- **Granola is retired.**
- **Remote and phone meetings (Founders Standup, Investor/Lender):** Google Meet + ClickUp **AI Notetaker**. The founders moved the Thursday standup from a phone call to Meet, which closes the phone-call gap.
- **In person (Founders Meeting):** **Wispr Flow** (paid account) produces the transcript; it is filed onto the meeting task with `scripts/file_transcript.py`.
- **Ad hoc:** Apple voice recording, filed when pertinent.
- **AssemblyAI is not being used.** The DJI stereo + AssemblyAI experiment (scripts/meeting_transcript.py) is dead; keep the script only as a record of the test.
- **The Meet link is the switch:** no link on in-person events, so the Notetaker cannot join and burn hours. Notetaker auto-join is scoped to the "Sŏn Meetings" calendar only.
- Consequences for the build: Capture Source options become Wispr Flow / AI Notetaker / Apple recording / None (Granola removed); agent Job 5 no longer syncs Granola.

## 2026-09-21
- **Founders Meeting live agenda is the workflow.** Set "Add to Agenda = Founders Meeting" on a task; it appears in embedded Table views ("Founders agenda: Punch List", "Founders agenda: Investor CRM") inside the meeting template. 1 hour after the due time, an automation sets Held; the close-out automation (v2) sets "Discussed in" and clears Add to Agenda. The Action Items capture workflow is retired.
- **No agent or API ever edits a meeting description** (embeds are invisible to both and get deleted). All meetings use the template for their Meeting Type, applied by a "task created" automation. v2 creates bare tasks and sets fields only after the template applies (tested). Never reapply a template to an existing meeting, since that wipes its dates.
- **Meetings Agent v2** replaced the old Meetings Agent (old one deactivated, not deleted). Jobs: roll-forward, reminder + Prep Sent, reschedule, cancel, notes (no Action Items).
- **Two-way date sync (tested):** changing a meeting's start or due date in ClickUp moves the Google event (two automations → v2); moving the event in Google Calendar updates the task (Google Calendar trigger on the dedicated "Sŏn Meetings" calendar → v2). Each side does nothing if times already match, so no loops. New events are created on "Sŏn Meetings"; the 8 existing events stay on the primary calendar and are rescheduled through ClickUp or the agent until they age out (after Oct 15). Only the organizer (Brandon) can drag an event; Dominic reschedules in ClickUp or through the agent.
- The 7 upcoming meetings were replaced by template-built copies without touching Google events (no invites).

## 2026-09-20
- **Investor CRM automations (tested 2026-09-20):** A1 Accepted creates the Form D task (due 14 days, Brandon chose a buffer day inside the 15-day legal clock, assigned to Dominic); A2 Materials sent comments to the Founders team; A3 Passed or Disqualified comments for the reason and materials held; A4 Needs change note creates the change-note task (7 days, Dominic); A5 Next Follow-up reminder (fires on the date, verify later). The `{task name}` variable must be inserted from the picker, not typed.
- **No Investor relationship on automation-created tasks** (the action only accepts a fixed task, and Brandon does not want it). The `investor` and `pre-funding` tags are retired from those automations.
- **Automation instructions are the override and the single source of truth.** Procedures live in the automation prompt, not in the agent profile. The agent keeps only standing guardrails. Job 6 was removed from the agent on 2026-09-20 after the duplicated copies conflicted (a stale prompt produced checklist items, and a run wiped the agenda section of a meeting description).
- **AI credits restored.** The Meetings Agent is live again; its instruction updates (Event Title, Job 4) are applied.
- **Agenda intake (approved design):** a Button custom field sets the Agenda value and its Automation calls the Meetings Agent (Automations can run a Super Agent as an action). The agent finds or creates the next occurrence, adds a checklist item with task name, status, owner and link under "Agenda items", sets the "Agenda for" relationship, clears the Agenda flag, and comments on the source task. Cost: one agent run per click.
- Supporting build (2026-09-20): Agenda dropdown field (Everything scope), "Agenda for" relationship fields on the Punch List and Investor CRM, Punch List "Agenda queue" view, meeting templates rewritten to open with attached agenda items.

## 2026-09-17 (no-AI build window)
- **AI credits are 0 during the ClickUp pricing negotiation.** No Super Agent or AI use until restored; Automations are unlimited. Plan: PLAN-2026-09-17-no-ai.md (approved; auto mode).
- **Investor CRM (approved design):** list "Investor CRM" in Founding Sŏn, default type Investor. Statuses: Prospect → Contacted → Meeting Scheduled → Diligence → Soft Commit · Passed (done) · Committed (closed). Fields: Organization, Email, Phone, Investor Type, Check Size, Committed Amount, Intro Source, Last Contact, Next Follow-up, Related Meetings (→ Meetings), Created By Notes. Follow-ups are subtasks. Views: Pipeline board, Table, Follow-ups Due, Committed. Dashboard optional later. **Investor tasks leave the Founding Punch List** (preview-approved migration). This replaces the separate Investors list (N2) and the Punch List "Investors" view.
- **Investor materials (Brandon, 2026-09-17):** property brochure · property deck · white paper · pro forma · investor disclosure. Built as a "Materials Sent" labels field on the Investor CRM.
- **Preview C APPLIED:** Classification on 188 live Punch List tasks. **Preview D APPLIED:** 9 Founder Decision tasks from the Operating Agreement.
- **SaaS rebuild SIGNED OFF (Brandon, 2026-09-17)** — gate #13(c). The Docs "Technology - Function → SaaS Map" and "Technology - SaaS Catalog" replace the lists. Removing/archiving the 241 + 46 tasks is a separate step Brandon does in the UI (Claude never deletes). Duplicate merges and vendor-name fixes happen in the Doc afterward.
- **Previews A and B APPLIED** (2026-09-17): investors moved into the Investor CRM; 3 past prototype meetings recreated as Meetings history records.
- **Prototype meeting tasks migrate into the Meetings list as history;** Brandon archives the originals afterward.
- **No reschedule/location Automations.** Location is always manual in Google Calendar; rescheduling is the agent's job (waits for credits).
- **Field cleanup is un-parked** (today).
- **Handoff Automations approved:** Action Items → Routed ⇒ move to Founding Punch List; Capture → Activated ⇒ add to Founding Punch List.

## 2026-09-16 (Phase 4, Stage 2 — cancel path SOLVED)
- **Automation delete works.** Google Calendar "Delete event" matches events by **Keywords (title search)**, not by ID. Set Keywords = the **Event Title** field (new short text field on the Meetings list). Brandon tested it: the status change to Canceled deleted the event immediately.
- **Final cancel path:** the agent sets status Canceled → the Automation deletes the event by Event Title. Everything runs through the agent. This supersedes "calendar deletion stays manual" below.
- **Requirement:** event titles must be unique and match Event Title exactly. The agent titles each event like its task name ("<Meeting Type> — YYYY-MM-DD"), and investor meetings add the investor's name.

## 2026-09-16 (Phase 4, Stage 2 — cancel path REVISED)
- **Automation "Delete event" can't delete agent-created events:** AUTO_505 "Integration event not found" on all 3 test runs. It only works on events linked through ClickUp's own calendar integration.
- **Decision (Brandon): calendar deletion stays manual.** Brandon deletes the event from any calendar app (phone/Siri). The Meetings Agent does everything else: create, update/move, status Canceled + comment, and a reminder to delete the event. No calendar Automations. This supersedes the Stage 0.5 "Cancel = Rung 2" entry.

## 2026-09-16 (Phase 4, Stage 1)
- **Task types = Option A:** reuse existing **Process** (1023) for the Workflow role and **Founder Decision** (1022) for the Decision role. Only **Action Item** (1026) was created. The Operating Agreement review items use Founder Decision.
- Founders Team created (Brandon + Dominic).
- **Brandon turned on ClickUp's built-in Created By field.**
- **"Notes from BJAC" renamed to "Created By Notes"** (same field id 52c7d5a1; values kept). This replaces the planned Owner Notes field and the #16 migrate-then-delete step.
- **Classification (Labels ×9) created by Brandon.** API-verified options on the Founding Punch List.
- **No Owner field.** Assignee = the person executing; Created By = the owner of the task's creation and completion.
- **Cross-Department = ClickUp's native Tasks in Multiple Lists (TIML)**, not a field. Future department Teams will mostly see only their own space plus Meetings (People may be visible to several), so a cross-department task has to appear in each relevant list. Per ClickUp Help, anyone with access to any of a task's lists can see the task. The home list stays the Punch List during funding + lease; secondary lists only surface it. Claude can add a task to more lists via MCP (clickup_add_task_to_list).
- **No Punch List Phase field.** Founding Punch List views filter by task type. Brandon created dedicated **Investor** (1027) and **Real Estate** (1028) task types (supersedes Person/Account) and will re-type tasks himself. Today that's 10 Person tasks (investor relationships + Heejae Seo Galluccio, complete) and 1 Account task (207 St. Elmo Rd Lease). The 12 `investor`-tagged tasks are all complete and typed Task. Their handling moves to the tag-retirement step (preview first).
- **Punch List statuses (Brandon):** Inbox → Later (both Not Started; Later = prioritized out of Inbox, not yet active) → Next → Doing (Active) · Waiting · Done group + one Closed status. **No Soon.** Old mapping as applied: active queue→Next, up next→Later, in progress/ongoing/meetings→Doing, in review→Waiting. The 5 prototype `meetings` tasks sit in Doing for now (the status was deleted by accident).
- **Canceled = Done group; Done = the single Closed status** (applied). Views filter Canceled out.
- **Field definitions can be created by Claude via REST** (`POST /v2/list/{id}/field`, verified 2026-09-16). Field creation moves from [You] to [Claude]. Dropdown/label option edits are still to be confirmed.
- **Meetings Agent runs autonomously from day one** (Brandon): weekly Monday 7am roll-forward + summary; daily 8am day-before prep; daily 2pm + 7pm notes sync; @mention/message for reschedule/cancel. The first run seeds 4 weeks. Supervision = Brandon's review of the "what I did" notes for 4 weeks (#18).
- **Location lock check (#19) moves to the Meetings build.** The Location field belongs to meeting tasks, which don't exist yet.

## 2026-09-16 (Phase 4, Stage 0.5 — GATE #1 CLOSED)
- **Calendar engine:** the Super Agent handles create, update/move and guest messaging (Rung 1). Its only gap is deleting Google Calendar events.
- **Cancel = Rung 2 hybrid:** the agent sets the meeting task to Canceled → a ClickUp Automation (status trigger) runs Google Calendar **Delete event**. No Automation is used for creation.
- **Automations' Google Calendar surface (confirmed by Brandon):** triggers = event created or updated, event cancelled; actions = create, update, delete event. (Calendar-side triggers are available for syncing Google edits, such as location, back to ClickUp.)
- **Granola = Rung 1:** Granola MCP connected to the Super Agent; notes pull PASSED. Tools: get account info, list meeting folders, list meetings, query meetings, read meeting transcript, read meetings.
- Build-time check (Claude, not a question for Brandon): confirm how the Delete action identifies the event when wiring it.

## 2026-09-16 (post-audit)
- **Granola phone-call test PASSED** (Brandon ran it). Granola is confirmed for the standup.
- **`identified` is the Punch List's default new-task status,** so renaming it to Inbox is only a default-status name change. Brandon updates the Scaling People project on his own; nothing is needed from Claude.
- **Blueprint #3:** Brandon will create a personal ClickUp API token, which moves view creation to [Claude]. Brandon stores the token himself in local config; it is never pasted into chat.
- **Blueprint #2 (credits):** not a constraint and doesn't block anything. Brandon handles AI tier and credits.
- **Blueprint #18:** Brandon alone reviews the agent's weekly "what I did" notes for the first 4 weeks.
- **#4 APPROVED (explicit exception to Scaling People protection):** remap the Punch List status `identified` → `Inbox`. This changes ONLY the status of ~330 Scaling People tasks (done as a list status rename/mapping; nothing else about those tasks changes). Before applying, check whether Brandon's Code extraction pipeline writes status "identified" and update it.
- **#5:** add Capital/Budget and Brand/Design back, making Classification 9 labels.
- **#6:** add an `Action Item` task type, making 10 task types.
- **#7:** Investors pipeline stages built as proposed.
- **#8:** confirmed action items go to the Founding Punch List only during funding + lease. The agent suggests field values, not a department space.
- **#9:** the investor seed follows preview table → Brandon approves the exact list → set Investors value → remove the tag.
- **#10:** Brandon renames the leftover admin tasks and assigns owners himself in ClickUp. Claude does nothing here.
- **#11:** attorney review items have no Owner; the reviewer goes in Owner Notes. No guest invite.
- **#12:** delete the stray "Solution" field (copy any value into the description first).
- **#13:** Brandon confirms the function-area groupings once the export exists. The sign-off-before-removal gate still applies from the earlier lossless decision. Duplicate merges happen AFTER the Doc replaces the tasks (not selected; safest default, flagged to Brandon).
- **#14:** Brandon doesn't recognize the Claude-folder loose items ("(Temporary)", "Investment Thesis Architect", and one out-of-scope page). Leave them untouched and list them as unfiled; they're likely to be removed later. Brandon decides.
- **#16:** delete "Notes from BJAC" only after the SaaS export sign-off (values migrate to Owner Notes first).
- **#17:** delete old fields (Project, Category + Notes on Capture lists, Department Crossover) after a zero-value check. Report any field that has data before deleting it.
- **#19:** Location is read-only from Google Calendar. Lock the field if ClickUp allows it; otherwise it's a convention.
- **#20:** fundraising target = $2,500,000.
- **#21:** retire the prototype as planned: archive the old meeting tasks after side-by-side verification, and retire the agent after the new agent's 4-week review.
- **#22:** ARCHIVE the "Heejae" doc if ClickUp supports it. If not, Brandon deletes it himself (Claude does not delete).
- **All 22 blueprint approvals are resolved.** Where they differ from blueprint/00 §5 defaults (#4 remap, #5 9 labels, #6 Action Item type, #12, #20 target, #22), DECISIONS wins. Sync the blueprint files before building.
- **#15:** create Documents folders + shell template pages in BI, Events, Hospitality, Product and Property now.
- **Named exceptions to the "active tasks only in the Punch List" rule:** (1) Meetings space tasks (meeting series and occurrences, plus the Action Items inbox before items get confirmed into the Punch List); (2) the Investors record list in the Founding Sŏn space. There are no others.
- **Accepted trade-off:** Everything-scoped fields (Owner, Owner Notes, Classification, Cross-Department) show up empty on Personal-space tasks. No data is written there.
- **N8 APPROVED as a shell TEMPLATE,** not a heavy register. Keep it close to the current state of the shells. Content is driven by the Scaling People work, so the template gives structure (purpose, stages, activation signal, checklist) that Scaling People outputs fill in over time. Don't invent department content ahead of that work.
- **N9 REJECTED** (investor update drafter).
- **CORE PRINCIPLE: ClickUp-first.** The project is built around ClickUp. Super Agents, Brain, Automations and ClickUp's MCP abilities (Super Agent external MCP tools) are the default engine for every workflow, including the meetings engine. Claude does NOT take over ClickUp workflows. Claude's role: design, setup/build through the MCP, research, and a fallback ONLY where ClickUp verifiably can't do something (documented with evidence and approved by Brandon). The Phase 3a "Claude-primary hybrid" recommendation is REJECTED. Credit cost is accepted as a cost of the design; Brandon turns AI on per use case.
- **Shortlist picks:** N2 (investor record list + relationship fields) and N3 (fundraising & runway dashboard) APPROVED. N6 (Docs home + naming + Claude-folder separation) APPROVED. N8 and N9 need more detail. N1, N4, N5, N7 and N10 were not selected.
- **Classification (workspace-wide labels) APPROVED:** Build/Setup, Recurring/Operating, Governance, Legal/Compliance, Vendor/Procurement, R&D, Admin.
- **APPROVED:** retire the `investor` tag. Apply the Punch List "Investors" value first, then remove the tag. Scaling People tasks are not touched.
- **APPROVED:** the investor record list lives in the Founding Sŏn space.
- **Founding Punch List view labels are phase-scoped.** They exist ONLY for the current funding + lease round (active LOI, active investor work) and will never be reused. Build them as a list-scoped field on the Founding Punch List (values: Investors, Real Estate/Lease), NOT as workspace Classification values. Brandon adds more values himself if he needs another view. The workspace Classification field stays purely long-lived effort types.
- **Scope expansion approved:** research beyond what Brandon named (unused ClickUp features, department shells, Claude ecosystem, knowledge + governance). It runs before the blueprint, with a triage step so the blueprint only includes chosen items.
- **No Workstream field.** The space IS the department/workstream. Add a "Cross-Department" multi-select field linking the other departments (spaces) involved, so a task can surface across lists. Evaluate ClickUp's native Tasks in Multiple Lists alongside or instead of it. Open design issue: while every active task lives in the Founding Punch List, the Investors and Real Estate views need a department signal (e.g. Finance, Property) from this field or a home-department equivalent.
- **Classification = multi-select labels.** Research decides the value set (full coverage of effort types). Brandon has no preset values.
- **Capture item kinds use custom task types** (Deliverable, Structure, Workflow, Idea…), not a field.
- **Capture list statuses:** Captured → Developing → Ready → Activated, with Archived as the closed status. "Ready" = built out, waiting for the department to go live. "Activated" = promoted into real work.
- **The SaaS Map becomes a ClickUp Doc with tables,** one page per function area. Export losslessly before removing any task.
- **The Personal space is out of scope.** Leave it alone.
- **ARCHITECTURE PRINCIPLE (overrides the digest's "collapse spaces" hypotheses):** the workspace mirrors the FUTURE full build of the restaurant's departments. Department spaces (Operations = ops department, People = HR/people, etc.) are shells that fill in over time, and the structure stays in flux until near construction. Do NOT merge or collapse department spaces.
- **Until past the funding + lease phase, ALL active tasks live in the Founding Punch List.** No other space gets action tasks.
- **Capture lists stay, one per space.** Each is the department's catch-all for anything relevant (actions, deliverables, structures, workflows, ideas). Improve them with a better default task type, a type/classification field, and a better default view (table or similar), not by removing them.
- **"Scaling People" is a BOOK** used to inform Sŏn's operational design and strategy. It is not a program that ends. The Carryover Register is PROTECTED, same as the Scaling People tasks.
- **Operating Agreement review items** ("Dominic Review Required", "Attorney Review Required") become tracked tasks in the Founding Punch List.
- **Status set APPROVED for the Punch List** and as the candidate default for other spaces: Inbox → Later → Soon → Next → Doing → Waiting → Done / Canceled (closed).
- **Punch List views:** the DEFAULT view is "Action Items", holding everything not carved out into its own view, INCLUDING all Scaling People tasks and subtasks. Carved-out views: Investors & Fundraising, and Real Estate / Buildout. Scaling People never appears in carved-out views. Carve-outs are driven by a field value (Classification, or a similar field), not by task names.
- **Punch List status intent:** capture → a 3-deep planning queue (a baseball-style on-deck concept, renamed so a first-time reader understands it) → doing. Drop ongoing, meetings, final steps and in review. Proposal pending approval.
- **Fields:** add an "Owner Notes" text column. Migrate any existing "Notes from BJAC" values into it, then remove BJAC. Remove Project; its intent becomes the Classification field.
- **Leftover admin tasks are still live** ("transfer ownership from brandon" ×3, Gmail, Airtable, AirTable, ClickUp, Access Removal). Keep them; give them proper names and owners in the restructure.
- **OPEN:** mapping the "identified" status changes Scaling People tasks' status. This needs Brandon's explicit approval before anything happens.
- **Metrics section:** fundraising pipeline only, for now.
- **Standup uses a lean template:** open actions, per-founder updates, blockers, decisions needed, wrap-up.
- **Investor/lender meeting template:** agent prep brief from the investor's history, link to the investor record, materials-sent log, and a follow-up email drafted for review.
- **Teams:** create only a Founders team now. Department teams wait until there's staff.
- **Founders Meeting runs Tue 11:00–13:00.** The prototype's 11–2 was wrong.
- **Remote default is Google Meet** (the prototype used Zoom).
- **Agenda template additions:** last meeting's open action items (by owner), a required wrap-up block, a key metrics/pipeline section, and time-boxed topics (owner, minutes, outcome: decide/discuss/inform).
- **Prep:** the day before, the agent pre-fills carry-overs, open actions and the last summary, then pings both founders to add topics.
- **Prototype archived** to templates/prototype/. It already touched Google Calendar (series recreation, instance IDs); verify which tool it used.
- **Rolling schedule.** The first run creates 4 meetings per series. After that, a weekly job adds only the occurrence that falls 4 weeks out (1 per weekly series). Cancellations are not backfilled.
- **Meeting types:** Founders Meeting, Founders Standup, and Investor/Lender (ad hoc, not recurring).
- **Agenda template:** start from the prototype's Weekly Founders Sync template, then fill gaps through the interview.
- **Location:** Brandon edits it directly in Google Calendar. ClickUp should pick it up by reading the event (the agent reconciles before the meeting), or not store location at all. Decide in Phase 3.
- **Invite organizer is Brandon's Google account for now.** Later, create an officeadmin@ or organizer@ account and move the organizer role to it (parked).
- **Cancel and reschedule happen by telling an agent.** The agent updates both the ClickUp task and the Google event, so natural-language requests are the main interface.
- **Action items go through a flagged inbox, not AI auto-routing.** There's a single Action Items list in the Meetings space. Items come in 2 ways: an explicit spoken cue during the meeting ("action item: …" / "hey ClickUp …") and a wrap-up block at the end of every agenda. The agent extracts only flagged items and suggests a destination space. Founders confirm moves. Auto-routing gets revisited once accuracy is proven.
- **Brandon activated Granola Business** (2026-09-16), so the MCP, API and transcripts are available.
- **Standup capture stays on Granola.** Test an outbound call (Brandon calls Dominic, good signal, no Bluetooth). If the audio is still poor, fall back to a Meet call with Granola desktop running on Brandon's laptop.
- **Research gap fixed: ClickUp works as an MCP client.** Super Agents can add custom external MCP servers (public URL, set up in the browser app) through "Add tools" on the agent profile. This shipped 2026-07-01. The Phase 1 research missed it. It could let the Meetings Super Agent pull Granola notes directly, and possibly write to Google Calendar through a Calendar MCP. That weakens the "Claude Routine as orchestrator" recommendation, so re-evaluate in Phase 3. Still to verify: Granola MCP auth inside ClickUp, whose Granola account it uses, credit cost per call, whether a Google Calendar MCP server can create invites, and reliability reports.
- **Scaling People is off-limits.** The ~330 governance subtasks in the Founding Punch List are active work: Brandon is extracting them from the book in Code. Claude must not change, move, archive or bulk-edit any Scaling People task. Views may filter them out; nothing else happens to them.
- **The Function → SaaS Map stops being tasks.** It gets rebuilt as a Doc, table or other non-task format. Every field, mapping and note must be kept. Rebuild path: full export → verify nothing is lost → Brandon approves → remove the tasks.
- **"Founders Meeting Assistant" was Brandon's prototype.** Keep it until its setup and meeting tasks are saved to the local folder, then retire or repurpose it in Phase 4.
- **AI is on rollover credits.** AI features get turned on per use case. The design should keep ClickUp AI credit use low and deliberate, and document which use cases need credits.

## 2026-09-16
- **Research before building.** Several requirements (Google invites from ClickUp, what the API can edit, AI Notetaker and phone calls, Brain indexing) depend on platform facts that need verifying first.
- **Every step is tagged [Claude] or [You].** UI-only settings (Teams, task types, status templates, Super Agent config) are expected to be manual work.
- **Model tiers.** Sweeps run on cheaper models. Fable is reserved for synthesis and architecture.
- **Default meeting mode is remote.** Brandon adds a location manually when a meeting is in person.
