# STATE — where we are

_Last updated: 2026-10-04_

## Current
_Last updated: 2026-10-04. Next session: Thursday 2026-10-08, after the standup._

**Live and working**
- **Meetings system:** Meetings space (Meeting Series / Meetings / Action Items), v5 templates with embedded live agenda views, two-way Google Calendar date sync, cancel-by-Event-Title automation, template-on-create automations, Held 1 hour after the due time, close-out that records "Discussed in" and clears "Add to Agenda".
- **Agenda flow:** set "Add to Agenda = Founders Meeting" on a Punch List or Investor CRM task; it appears in the embedded views inside the meeting task; close-out files it afterwards.
- **Meetings Agent v3** is the only active agent (v2 deactivated, old Meetings Agent and prototype deactivated). Jobs: roll-forward, reschedule, cancel, notes, close-out, day-before reminder. Messaging policy: the day-before reminder is the only routine message; otherwise it speaks only when something fails.
- **Capture:** Granola retired, AssemblyAI dropped. Founders Meeting = in person, no Meet link, Wispr Flow (agent reads it through the Wispr MCP). Founders Standup and Investor/Lender = Meet link, ClickUp AI Notetaker. Ad hoc = Apple recording, filed by hand (scripts/file_transcript.py).
- **Calendar:** every event on the "Sŏn Meetings" calendar, Dominic the only guest (Brandon owns the calendar, so inviting him duplicated events). The Meet link is the only switch that lets the AI Notetaker attend.
- **Workspace:** task types, statuses, Classification on 188 tasks, Investor CRM (11 records, 12-status pipeline, A1-A5 automations), Docs Home + 11 department shells, SaaS Map and Catalog as Docs (lists archived), views on every list.

**Verified 2026-10-04:** the six upcoming meetings all sit on Sŏn Meetings with correct IDs, titles, dates, guests, Meet links and Capture Source.

**Thursday test (Oct 8) now also has to answer two new facts (research 2026-10-04, kb §11)**
- ClickUp's help table says **Shared and Workspace Notetaker types are not on the Business plan**; Personal only would make the note private to Brandon, which breaks the shared-notes design. Check the Notetaker type on the standup note.
- **Auto-schedule is Personal type and primary calendars only**, so scoping auto-join to "Sŏn Meetings" may not behave as assumed. If the bot does not join Thursday, add it to the event from Planner instead.
- Better hook found: Notetaker admin settings include **"Share all meeting notes" with a chosen Super Agent**. Point that at Meetings Agent v3 and the agent receives notes directly instead of trying to read a private Doc.

**Checkpoints**
1. **Thu Oct 8 standup** — proves the AI Notetaker path: note copied into "Founders Standup Notes", Notes Doc Link set, status Notes Synced, and whether the agent could read a private Notetaker note at all.
2. **Tue Oct 13 meeting** — proves the Wispr Flow path through the MCP, and the live agenda in a real meeting.
3. **Mon Oct 12 7am** — proves roll-forward under v3 (bare task, template applies, fields set, event with the right link) and the quieter messaging.

**Open**
- Brandon's own tasks: investor record cleanup, Relationship Origin and owner on 11 records, publish the Investor Workflow doc (86akmhace / 86akmhacf / 86akmhacg).
- Investor CRM A5 (follow-up reminder) still unverified.
- Capture → Activated automation: deferred.
- Housekeeping: refresh Docs Home with the newer Docs, sync the blueprint files with the 09-19 to 10-04 decisions.
- Remove the unused "Granola" option from Capture Source whenever convenient.

**Key references:** DECISIONS.md (newest first) · PLAN-2026-10-04-meetings-v3.md · kb/clickup-knowledge-base.md · templates/meetings-agent-v3-build-prompt.md · logs/YYYY-MM-DD.md

## Parked threads
_(side topics we left, to come back to)_
- **Agent skills (parked 2026-10-04):** three chat-triggered skills drafted but not built — schedule an investor meeting, make a meeting remote or in person, file a transcript. Text in templates/meetings-agent-v3-skills.md.
- **Field cleanup (parked 2026-09-16 by Brandon):** add Classification + Created By Notes to all 11 Capture lists; Brandon deletes Project (Punch List, 0 values), Notes + Category (8 Capture lists, 0 values), Department Crossover (Finance/Events/Promotion, 0). Next Action = option A: Claude copies its one value (207 St. Elmo Rd, task 86aj3u3g8) into Created By Notes, then Brandon deletes the field. Check first whether Technology Capture's Notes/Category are shared with the SaaS lists.
- Granola API + MCP opportunities (raised 2026-09-16 during 0.4): Granola folders ↔ meeting series matching, transcript-based action-item cue detection, cross-meeting query for investor prep, one-time historical backfill via API [Claude setup]. Fold into Phase 6 design after the proof test.
- Create an officeadmin@/organizer@ Google account and move the organizer role to it (later)

## Key facts
- Sŏn = pre-opening restaurant. Workspace members: Brandon + Dominic. A 3rd partner joins within weeks. Everyone is a founder for the foreseeable future.
- ClickUp Business plan + AI add-on. Google Calendar.
- Master plan: ~/.claude/plans/this-chat-will-focus-zazzy-reef.md (mirrored in ROADMAP.md)

## Verify before the Phase 3 blueprint
- ClickUp Super Agent + external MCP: Granola MCP auth, Google Calendar MCP invite creation, credits, reliability (sources: help.clickup.com article 38503227973655, feedback.clickup.com super-agent-access-to-mcp-servers)
- Granola phone-call quality test on Thursday

## Hard constraints
- ClickUp-first: Super Agents, Brain, Automations and ClickUp MCP are the engine. Claude is a proven-gap fallback only.
- Do NOT modify any Scaling People tasks, or the Carryover Register (Operations).
- Department spaces are shells mirroring the future build: never merge or collapse them. Active tasks go only in the Founding Punch List until past funding + lease.
- Before removing any SaaS Map task, export it and verify nothing is lost.
