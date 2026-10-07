# Meetings rebuild plan (drafted 2026-10-04, nothing executed)

Principle: the **Meet link is the only switch** that decides whether ClickUp's AI Notetaker attends. No link, no Notetaker. The calendar an event sits on is organisation, not control.

## 1. Target state, calendar side

| Meeting type | Calendar | Meet link | Guests | Capture |
|---|---|---|---|---|
| Founders Meeting (Tue, in person) | Sŏn Meetings | **No** | Dominic only | Wispr Flow |
| Founders Standup (Thu, remote) | Sŏn Meetings | **Yes** | Dominic only | AI Notetaker |
| Investor / Lender (ad hoc, remote) | Sŏn Meetings | **Yes** | Dominic + the investor | AI Notetaker |
| Any meeting made remote on request | unchanged | link added | unchanged | switch to AI Notetaker |

Brandon is not a guest on any of them: he owns the Sŏn Meetings calendar, and inviting him creates the duplicate copy he is seeing. Dominic is invited because it is not his calendar.

### Event work needed
| Event | Now | Action |
|---|---|---|
| Tue Oct 6, Founders Meeting | Sŏn Meetings, no link, Brandon + Dominic guests | Remove Brandon as guest |
| Thu Oct 8, Founders Standup | Sŏn Meetings, link, both guests | Remove Brandon as guest |
| Tue Oct 13, Founders Meeting | Primary calendar, link, stored event ID stale | Delete; rebuild on Sŏn Meetings, no link, Dominic only |
| Thu Oct 15, Founders Standup | Primary calendar, link, stored ID stale | Delete; rebuild on Sŏn Meetings, link, Dominic only |
| Tue Oct 20, Founders Meeting | Sŏn Meetings, **link** | **Delete** (Meet links cannot be removed); agent rebuilds with no link, Dominic only |
| Thu Oct 22, Founders Standup | Sŏn Meetings, link, both guests | Remove Brandon as guest |

Agent limits: it **cannot delete** calendar events and cannot remove a Meet link, so every event that needs its link gone must be deleted by Brandon and rebuilt by the agent. It **can** remove a guest (update event, remove_attendees), so guest-only fixes need no deletion.

## 2. Target state, ClickUp side

- **Capture Source** options become: Wispr Flow · AI Notetaker · Apple recording · None (Granola removed). Field options are UI-only.
- Values: Founders Meeting = Wispr Flow; Founders Standup and Investor/Lender = AI Notetaker.
- **Add to Agenda** (dropdown, Everything scope) stays as the agenda flag; the two embedded Table views stay.
- **Discussed in** relationship stays as the history record.
- Task statuses unchanged: Scheduled, Prep Sent, Held, Notes Synced, Canceled.

## 3. Automations: keep, change, retire

| # | Automation | Verdict |
|---|---|---|
| 1 | Meetings: status Canceled → Google Calendar Delete event (matched on Event Title) | Keep |
| 2 | Meetings: due date arrives + 1 hour, status Scheduled or Prep Sent → set Held | Keep |
| 3 | Meetings: status Held → agent close-out (set Discussed in, clear Add to Agenda) | Keep, repoint to v3 |
| 4 | Meetings: task created + Meeting Type Founders Meeting → apply template | Keep |
| 5 | Meetings: task created + Meeting Type Founders Standup → apply template | Keep |
| 6 | Meetings: due date changes → agent updates the event | Keep, repoint to v3 |
| 7 | Meetings: start date changes → agent updates the event | Keep, repoint to v3 |
| 8 | Google Calendar event created/updated on Sŏn Meetings → agent updates task dates | Keep, repoint to v3 |
| 9 | Action Items: status Routed → move to Punch List | Already off; delete |
| 10 | Investor CRM A1 to A5 | Keep, unrelated |

Prep job note: automations 6, 7 and 8 each cost an agent run. They are idempotent, so a single reschedule costs at most two runs.

## 4. Agent v3

Rebuild rather than patch: v2 has absorbed a dozen instruction changes, which is what caused drift last time.

**Jobs**
1. **Roll-forward** (Mon 7:00am): keep 4 weeks of occurrences per Active series. Create bare (name + Meeting Type), wait for the template automation, then set status, dates, Series, Capture Source, and create the event on Sŏn Meetings with Dominic as the only guest and a Meet link only for Standup and Investor/Lender.
2. **Reschedule** (on request or when automations 6 to 8 call it): update the same event, never delete and recreate; keep the title.
3. **Cancel** (on request): set status Canceled, comment once. The automation deletes the event.
4. **Notes**: AI Notetaker meetings, file a shared copy into the right notes Doc and set Notes Doc Link, then Notes Synced. Wispr Flow meetings, read the transcript through the Wispr MCP, write the page, set the link and Notes Synced. Apple recording meetings, wait for a founder to file it.
5. **Close-out** (called by automation 3): set Discussed in on every flagged task, clear Add to Agenda.
6. **Day-before reminder** (daily 8:00am, only when a meeting is tomorrow): one @mention asking both founders to set Add to Agenda on anything they want discussed, then set Prep Sent.

**Dropped from v2**: per-run "what I did" comments, Action Items extraction, any description editing. **Kept**: the day-before reminder to add agenda items, and nothing else.

**Notification policy (new, explicit)**
- The only routine message is the day-before reminder to add agenda items.
- Otherwise comment only when something failed or needs a human: a template that did not apply, a transcript still missing a day after a meeting, a conflict it could not resolve.
- Never report success. No weekly summary, no per-run logs, no confirmation when notes are filed.
- Never @mention a founder unless a founder asked it something or a job failed.

**Tools**: Default tools, Create task, Update task, Post task comment, Docs (create page, update), Google Calendar (list, create, update), Wispr Flow MCP (read-only).
**Knowledge**: Meetings space, the three notes Docs, Founding Punch List, Investor CRM.
**Triggers**: Monday 7:00am (roll-forward); daily 8:00am (reminder, only if a meeting is tomorrow); daily 2:00pm and 7:00pm (notes); DMs and @mentions; plus the automations above.

**Retire**: v2 deactivated, not deleted, after one clean week. The old Meetings Agent and the prototype are already deactivated and can be deleted whenever.

## 5. Order of execution (nothing starts until approved)

1. Brandon: Capture Source options; delete three events (Oct 13, Oct 15, Oct 20).
2. Brandon: build v3 from the prompt file; connect the Wispr MCP to it; leave v2 active but triggerless.
3. Claude: set Capture Source on the six upcoming meetings.
4. Brandon: repoint automations 3, 6, 7, 8 to v3; delete automation 9.
5. Claude: have v3 rebuild the Oct 13 and Oct 15 events and strip Brandon as guest from Oct 6, 8, 20, 22.
6. Verify: Thu Oct 8 proves the Notetaker path; Tue Oct 13 proves Wispr Flow; the following Monday proves roll-forward and the weekly summary.
7. After one clean week: deactivate v2.

## 6. Answered (2026-10-04)
1. **Keep the day-before reminder** to add agenda items. Everything else the agent used to say goes.
2. **Only report failures.** No comment when something works as designed, including notes being filed.
3. **Investor meetings on request only,** created by asking the agent.
