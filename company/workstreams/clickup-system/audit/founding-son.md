# Founding Sŏn — Audit

## Summary

Founding Sŏn (space 90138396180) contains exactly one list, **Founding Punch List** (901323485125) — no folders, no other lists, no docs found. That single list holds **491 tasks** (including subtasks; open + closed). It reads as two very different things stapled together:

1. **A live founders' operating list** (~120 tasks): investor outreach and relationships, real estate/lease, legal/entity formation, budget/FF&E/OS&E line items, brand & design workstreams, staffing/uniform prep, tool-migration decisions, and — newest — a recurring-meetings system (Weekly Founders Sync, Founders Thursday Standup) with Google-Calendar-backed agenda tasks that already show the `Meeting` and `Document` custom task types and a "Founders Meeting Assistant" bot creator.
2. **A massive auto-generated governance backlog** (~350 tasks, virtually all subtasks of one parent, "Scaling People: Sŏn Operational Build Out"), every one in status **identified**, unassigned, no due dates, no priority pattern beyond a default spray of urgent/high/normal/low. These follow a rigid naming template — `Structure:`, `Instrument:`, `Process:`, `Founder decision:`, `Document:` — plus a 17-part "S1–S17" book-chapter checklist (a leadership/scaling-org book, now complete). This looks like the output of an AI planning pass translating a management-framework document into ClickUp tasks, not something either founder is triaging today.

Statuses (space-inherited on this list): identified (open), active queue, up next (unstarted), meetings, in progress, stalled, ongoing, final steps (all custom "in progress" family), in review (done), complete (closed) — 10 total, unusually many for one list.

Custom fields on the list: **Next Action** (text), **Notes from BJAC** (short text), **Project** (dropdown: Financials / White Paper / Pitch Deck / Research) — defined but, in every task sampled, **unset**. No space-level custom fields.

Task types in use: default (blank) type on most tasks; **Meeting** and **Document** custom types appear on the newer recurring-meeting/document tasks.

## Details

**Hierarchy.** Space → one list, no folders. (Tasks report a "hidden" system folder in their raw payload — this is ClickUp's automatic wrapper for a list sitting directly under a space, not a real folder someone created.)

**Statuses.** 10 statuses on one list is a lot: identified → active queue → up next → meetings → in progress → stalled → ongoing → final steps → in review → complete. "Meetings" functions less as a workflow stage and more as a type marker for agenda tasks (parent recurring task + one task per occurrence).

**Assignees.** Only two people (Brandon, Dominic) are assignable. The ~120 "live" tasks are assigned reasonably (many to Brandon alone, several jointly, a cluster of tool/vendor-decision tasks to Dominic alone). The ~350-task governance backlog is **entirely unassigned**.

**Due dates / priority.** The live tasks mostly carry due dates and a priority. The governance backlog has **no due dates at all** and priorities that look randomly assigned (urgent/high/normal/low scattered with no visible logic) — a strong signal they were bulk-generated rather than planned.

**Tags.** Only one tag exists and is used: `investor`, applied to ~12 completed fundraising-materials/outreach tasks. Everything else is untagged.

**Descriptions.** Mixed. Most tasks (especially the governance backlog and old checklist items) have empty descriptions — the task name carries all the meaning. The newer meeting-agenda tasks have a rich, consistent markdown template (time/location, Google Calendar mapping, per-founder update sections, live-notes/decisions/action-items/parking-lot sections) — clearly built by an automation, and it's a good template. One major task (Operating Agreement V1.0) has a real hand-written description; most don't.

**Subtasks/checklists.** Checklists are essentially unused (0 on every task sampled). Subtasks are the main structural device — one giant task ("Scaling People: Sŏn Operational Build Out") appears to parent the bulk of the 350-task governance backlog; recurring-meeting series tasks (e.g., "Weekly Founders Sync – Series" → "…Agenda 2026-09-16") also use parent/child.

**Recurring meetings already in motion.** There are two live recurring series: **Weekly Founders Sync** and **Founders Thursday Standup**, each with a "Series" or dated parent task and one child task per occurrence (past occurrences marked complete, future ones pre-created — e.g., agendas already exist for 09-22 and 09-29). These are exactly the pattern the Meetings-space project should generalize, and they're a good reference for the agenda template to reuse.

**Docs.** None found attached to this space via search.

### Founding Punch List — natural groupings (approximate counts, 491 tasks total)

| Group | ~Count | Notes |
|---|---|---|
| Governance/ops backlog ("Scaling People" Structure/Instrument/Process/Founder decision/Document subtasks) | ~330 | All status "identified", unassigned, no due dates — auto-generated from a scaling/management framework |
| "Scaling People" book chapters (S1–S17) | 17 | Mostly complete; a reading/extraction checklist |
| Investors & fundraising (outreach, relationships, packets, pitch deck, white paper, investor website) | ~45 | Includes the `investor`-tagged cluster and named-individual outreach tasks (Robby Grubbs, Robert Jacob Lerma, Brett Morgan, Adam Biechlin, Chris St. Peter, Doug Zell, Chris Null, David Tapia, Kevin Fink, Basu, Anthony/Jimmy, John Heffington) |
| Legal / entity / operating agreement | ~30 | Operating Agreement V1.0 and its ~20 clause-drafting subtasks, partnership agreement, entity structure research |
| Budget / capital stack / FF&E / OS&E / reserves | ~25 | Numbered "Budget Review" series, historical re-forecasts, line-item reconciliations |
| Real estate / lease / construction | ~12 | 207 St. Elmo Rd lease, rent terms, HVAC/grease trap/as-built checks |
| Brand & design workstream (1A–12A role-based design register, brand guidelines, design system) | ~30 | All complete; reads as an early vendor/role-sequencing checklist for brand development |
| Staffing / uniforms / scheduling | ~14 | Shift schedules, uniform lookbook, labor model |
| Website | ~7 | Multiple "Update Website" / investor-website tasks over time |
| Recurring meetings (Weekly Founders Sync, Thursday Standup, and their agenda occurrences) | ~13 | The live meetings pattern described above |
| Tool/platform migration & admin (ClickUp vs Notion, Box, bank account moves, billing, ownership transfers, access removal) | ~25 | Several single-word tasks (Gmail, Airtable, StoryDoc, Pitch.com…) read like a checklist being worked live in a meeting |
| Personal/misc follow-ups (trip planning, ad hoc "follow up" tasks) | ~8 | Not clearly homed elsewhere |

(Counts are estimates from a full read of all 491 task names/status/assignee — not a database query — so treat them as directional, not exact.)

## Issues / opportunities

- **The ~330-task auto-generated backlog dominates the list and buries the ~120 tasks that are actually being worked.** Every filtered/sorted view of "Founding Punch List" today is mostly noise unless it explicitly excludes status "identified" with no assignee. This is the single biggest usability problem in this space.
- **10 statuses on one list, several of which ("active queue," "up next," "ongoing," "final steps," "meetings") overlap in meaning** — a candidate for consolidation when the workspace restructure defines statuses per space/list.
- **Custom fields (Next Action, Notes from BJAC, Project) are defined but unused** — either start populating them or drop them; as-is they add list overhead with no payoff.
- **Only one tag (`investor`) exists and it's applied inconsistently** — many clearly investor-related tasks (e.g., the "Investor Outreach" named tasks, "Robby Grubbs Signed as Investor") aren't tagged, while some tagged tasks are unremarkable admin notes.
- **Duplicate-looking tasks**: three tasks all named "transfer ownership from brandon," several single-word admin tasks (Gmail, Airtable, AirTable, ClickUp, Access Removal) that look like an unstructured checklist rather than real tasks — worth checking if they're deprecated leftovers.
- **The recurring-meeting pattern (Weekly Founders Sync, Thursday Standup) is a good working prototype** for the Meetings Super Agent — it already does Google Calendar mapping, agenda template, and parent/occurrence structure. Worth reviewing before building the new system so it doesn't reinvent a worse version.
- **No Owner column / Classification field yet** — consistent with the planned workspace restructure, but worth noting this list has zero systematic ownership tracking beyond ClickUp's native Assignee.
- **The list currently lives directly in the space with no folder**, and the founding punch list mixes fundamentally different content types (a live task list, a book-notes checklist, and an AI-generated framework backlog) in one flat list — a strong candidate for splitting via custom task types, filtered views, or separate lists during the restructure.

## Questions for Brandon

1. Is the ~330-task "Scaling People" governance backlog something you intend to work through task-by-task, or is it reference material that should move out of the active punch list (e.g., into a doc, or an archived/backlog list) so it stops crowding the real work?
2. Should "investor" become a formal Tag or Classification value applied consistently, given how much of this list is investor-relationship tracking?
3. Are the three "transfer ownership from brandon" tasks and the single-word admin tasks (Gmail, Airtable, ClickUp, etc.) still live, or safe to close/delete as leftover meeting notes?
4. Do you want the Next Action / Notes from BJAC / Project custom fields actually used going forward, or should they be removed in the restructure?
5. Should the Weekly Founders Sync / Thursday Standup pattern already in this list be the template the new Meetings Super Agent replicates for all other recurring meetings, or is a different structure planned?
