# ClickUp Structural Features and Best Practice — Research Brief

Prepared 2026-09-16 for Sŏn's ClickUp workspace restructure (workspace 90131574430, Business plan + AI add-on, Google Calendar).

## Key findings

1. **CONFIRMED** — Custom task types are created workspace-wide (Workspace Settings > Task Types); a Space can enable/disable which types show, but the type itself lives at the workspace level, not per-space. [ClickUp Help](https://help.clickup.com/hc/en-us/articles/17564381376919-Custom-task-types)
2. **CONFIRMED** — Custom task type limits: name max 16 characters, description max 100 characters; up to 100 custom task types per workspace on all plans; Free plan caps usage at 20 tasks set to a custom type, all paid plans (Unlimited/Business/Business Plus/Enterprise, which covers Sŏn) are unlimited. [ClickUp Help](https://help.clickup.com/hc/en-us/articles/30661182619671-Custom-task-types-feature-availability-and-limits)
3. **CONFIRMED** — Custom task types can be filtered on in List/Board/Calendar views, added as a sortable column, and used as Automation triggers/conditions/actions — so a "Meeting" task type can drive its own filtered views and automations. [ClickUp Help](https://help.clickup.com/hc/en-us/articles/6310206119575-Filter-and-search-tasks-in-List-view)
4. **UNCERTAIN, no API endpoint** — Custom task types can only be *created* via the UI. The API's `custom_item_id` field on Create Task/Update Task lets you assign an *existing* type to a task, and Get Custom Task Types lets you read them, but there is no create/edit endpoint — this is an open feature request. [ClickUp API docs](https://developer.clickup.com/docs/custom-task-types), [feature request](https://clickup.canny.io/feature-requests/p/custom-task-types-via-api)
5. **CONFIRMED** — Statuses inherit down the hierarchy: Lists without a Folder inherit the Space's statuses; a Folder inherits the Space's statuses unless given custom ones; a Sub-Folder inherits its parent Folder's custom statuses, or the Space's if the Folder has none. Any level can override with "custom statuses." [ClickUp Help](https://help.clickup.com/hc/en-us/articles/6308803927831-Statuses-for-Folders)
6. **CONFIRMED** — Every status belongs to one of four status groups: Not Started (opt-in ClickApp, available on all plans), Active, Done, Closed (tasks in Closed are hidden from views by default). Status Templates (Kanban, Scrum, Marketing, etc., plus custom "Save as template") can be applied to any Space/Folder/Sub-Folder/List and are available on every plan. [ClickUp Help](https://help.clickup.com/hc/en-us/articles/6309452618647-Manage-task-statuses), [Status templates](https://help.clickup.com/hc/en-us/articles/6309533958935-Status-templates)
7. **CONFIRMED** — Teams (ClickUp's name for user groups) can only be created by Workspace owners/admins; a user can belong to unlimited Teams; Teams can be assigned to tasks, @mentioned in comments/descriptions (type `@` + the team's initials), added as followers, and assigned checklist items. Sŏn's Business plan includes Teams. [ClickUp Help](https://help.clickup.com/hc/en-us/articles/6326036524823-Create-user-groups-with-Teams), [Teams feature availability](https://help.clickup.com/hc/en-us/articles/30914854991255-Teams-feature-availability-and-limits)
8. **UNCERTAIN** — Whether a Team can be added directly as a Calendar-event/meeting attendee (vs. only assigned/mentioned on tasks) is not clearly documented; search results confirm Teams can be added as task followers and mentioned, but explicit "add Team as calendar invite attendee" behavior wasn't confirmed in current docs. Treat as needing a live UI check before building the Super Agent's invite logic.
9. **CONFIRMED, API** — Create/Update/Get "Group" (Teams) endpoints exist in the public API (`createusergroup`, `getteams1`/Get Groups, `updateusergroup`) — so Teams/user-group membership can plausibly be managed by the Meetings Super Agent via API, not just UI. [ClickUp API — Create Group](https://developer.clickup.com/reference/createusergroup)
10. **CONFIRMED** — Custom Fields have a "People" field type distinct from the built-in Assignee field: People tracks additional stakeholders (e.g., an "Owner") without making them the task's assignee, useful for a dedicated Owner column that shouldn't collide with meeting/task assignees. [ClickUp Help](https://help.clickup.com/hc/en-us/articles/6303536766231-Intro-to-Custom-Fields)
11. **CONFIRMED** — Dropdown = single-select; Labels = multi-select version of the same concept. For a "Classification" field with mutually-exclusive categories, Dropdown is the right choice; use Labels only if a task can belong to more than one classification simultaneously. [ProcessDriven](https://processdriven.co/clickup/how-to-use-clickup/label-vs-tag-in-clickup-whats-the-difference/)
12. **CONFIRMED** — Custom Fields can be scoped at List, Folder, Space, or "Everything" (workspace) level, and the same field definition can be added to additional locations after creation, so one "Owner" and one "Classification" field can be defined once and reused workspace-wide without duplicating field IDs. [ClickUp Help](https://help.clickup.com/hc/en-us/articles/16544932876311-Add-a-Custom-Field-to-a-new-location)
13. **CONFIRMED** — Relationship fields link tasks either "Any task in your Workspace" or "Tasks from a specific List" (the latter is locked once set — a new field is needed to relate to a different List), and List-to-List relationships can pull in rollup columns from the related List's fields. [ClickUp Help](https://help.clickup.com/hc/en-us/articles/14276813483031-Create-Relationship-Custom-Fields)
14. **CONFIRMED, API** — Views (List/Board/Calendar/etc.) can be created, updated, deleted, and configured with filters/grouping/sorting via the public API at any hierarchy level, and Custom Fields are filterable using `cf_{field_id}` — so the Founding Punch List's filtered views (by Owner, Classification, status) can be scripted rather than hand-built. [ClickUp API — Views](https://developer.clickup.com/docs/views), [Filter Views](https://developer.clickup.com/docs/filter-views)
15. **CONFIRMED, best practice** — Recommended small-team hierarchy: one Space per team/department, Folders as optional groupings for major initiatives, Lists as the working unit; avoid over-splitting into many sub-20-task Lists, and let structure grow organically rather than building it all up front. [ClickUp Help — Hierarchy best practices](https://help.clickup.com/hc/en-us/articles/20480724378135-Hierarchy-best-practices)

## Detailed notes

### Custom task types
- Created in Workspace Settings > Task Types (owner/admin only per most docs); icon + color + name (≤16 chars) + optional description (≤100 chars).
- Applied per task via the task type selector or API `custom_item_id`; no bulk-create or edit via API today.
- Because they're workspace-scoped, Sŏn can define a "Meeting" custom task type once and it will be available (toggle-able) in every Space — good fit for a dedicated Meetings space plus reuse elsewhere if needed later.
- They integrate with filters, saved views, Automations, and (per help center) can drive different Custom Fields shown per task type ("Set Custom Fields by task type").

### Statuses
- Inheritance chain: Space → Folder/Sub-Folder → List, with an explicit "use custom statuses" opt-out at each level.
- Status Templates are reusable named sets (built-in: Kanban, Scrum, Marketing, etc.) that can be saved from any List/Folder/Space's current statuses and re-applied elsewhere — useful for giving the Meetings List a distinct status set (e.g., Scheduled / Notes Pending / Notes Synced / Cancelled) without hand-configuring every future list.
- Status groups (Not Started/Active/Done/Closed) are a separate axis from templates — every individual status is bucketed into one of these four groups, which controls default visibility (Closed is hidden by default) and progress-bar behavior.

### Teams / user groups
- Only owners/admins create Teams; members can belong to unlimited Teams.
- Usable for: task assignment, checklist-item assignment, comment/description @mentions, task followers.
- Public API supports Group CRUD (`createusergroup`/Create Group, Get Groups, Update Group) — confirms group membership can be programmatically maintained, which matters for the Meetings Super Agent auto-inviting "Team: Kitchen" style groups.
- Explicit "Team as a Google Calendar invite attendee" behavior needs a live check in Sŏn's own workspace before the Super Agent relies on it — the docs found describe Team mentions/assignment on tasks, not confirmed calendar-invite attendee behavior for a Team as a single addressable entity.

### Custom fields: Owner and Classification
- **Owner column**: use a **People** custom field, not Assignee. Assignee is a built-in field tied to "who does the work"; People is a custom field for tracking a separate role (owner/DRI, reviewer, stakeholder) independent of who's assigned. This avoids overloading Assignee semantics when a task's doer and its accountable owner differ.
- **Classification field**: use **Dropdown** (single-select) unless Sŏn genuinely needs multi-tagging, in which case use **Labels** (multi-select). Both are visually similar; the distinction is purely single vs. multi-select.
- **Field location/scope**: define each custom field once, then attach it at whatever scope needed — List, Folder, Space, or "Everything" (workspace-wide). Reusing the same field (rather than recreating per-list) keeps field IDs consistent for filtering/reporting and for API automation.
- **Relationship fields**: choose "Tasks from a specific List" to build structured cross-references (e.g., linking a Meeting task to its related Founding Punch List item) with optional rollup columns; choose "Any task in Workspace" for a looser, unscoped link. The specific-List choice is locked in once set.

### Views, filters, saved views
- Views can be filtered, grouped, and sorted per ClickUp attributes or `cf_{field_id}` for custom fields; operators include EQ, ANY, LT/GT, and relative-date functions (e.g., "yesterday").
- Community best practice: keep a small number of high-value saved views per list (e.g., "This Week," "Overdue," "My Team") rather than many overlapping filters; expose only the fields people actually need (6–8) in a List view; consider a "View Templates" reference folder to restore a view if someone edits it accidentally.
- Views are fully scriptable via the public API (create/update/delete, filters/grouping/sorting) — relevant for building the Founding Punch List's filtered views by Owner/Classification programmatically instead of by hand, and for keeping them reproducible if Sŏn rebuilds structure later.

### Space/Folder/List hierarchy for a small team
- Recommended default: one Space per major functional area (e.g., "Meetings," "Founding Punch List," "Operations"); Folders are optional and best used to group related Lists (e.g., a Folder per meeting cadence type, or per project); Lists are the actual working unit holding tasks.
- Anti-pattern flagged by ClickUp and consultants: too many Lists with under ~20 active tasks each signals over-fragmentation — for a 2–3-person founding team, prefer fewer, broader Lists over deeply nested Folders.
- Build organically — don't over-architect Spaces/Folders before real usage patterns emerge; this matters for Sŏn given the team will grow from 2 to 3 founders soon and structure may need to flex.

### Templates
- **Task templates**: capture all fields/properties/checklists of a task; can be set as the *default* task template for a List so quick-created tasks in that List (e.g., a "Meetings" List) auto-populate with the agenda/notes structure.
- **List templates**: capture a List's setup (default views, statuses, etc.) for reuse.
- **Recurring tasks + templates**: recurring tasks are a scheduling property on an individual task (frequency, or "when status changes"), not itself a template feature — commentary in the community (e.g., Cloudwards' 2026 guide) notes ClickUp's recurrence engine doesn't integrate as tightly with task templates, subtasks, and Automations as users would like; test carefully before relying on "recurring task created from a template on a rolling schedule" as a turnkey mechanism — a custom Automation or the Meetings Super Agent itself doing the rolling 4-week creation is the safer design.
- **Doc templates** exist in ClickUp Docs for standardized documents (e.g., meeting-agenda templates ClickUp itself publishes) but weren't the focus of the searches above; treat as a smaller, separate confirmation item if Sŏn wants agenda Docs templated.

### Calendar / Google Calendar integration
- ClickUp's native Calendar view supports adding participants to events (search & select, repeatable), and displays future recurring-task instances on paid plans.
- Community sources (Unito, a third-party sync tool) describe near-real-time two-way sync between ClickUp tasks and Google Calendar events (time/date changes propagate both directions) via ClickUp's own integration — but there are longstanding user feature requests for more robust 2-way sync, implying edge cases/reliability gaps exist. **UNCERTAIN** exactly how robust native (non-Unito) 2-way sync is as of September 2026 — validate directly in Sŏn's workspace before depending on it for the "rolling 4-week meeting creation with Google Calendar invites" goal.

### Public API v2/v3 coverage summary
| Structural feature | API support | Notes |
|---|---|---|
| Custom task types | Read + assign only | No create/edit endpoint; UI-only creation |
| Statuses / status templates | Partial | Statuses are set per Space/Folder/List via existing endpoints; explicit "apply status template" API not confirmed in this research — verify before scripting |
| Teams / user groups | Yes | Create Group, Get Groups, Update Group endpoints exist |
| Custom fields (incl. People, Dropdown, Labels, Relationship) | Yes | Full CRUD via Custom Fields API; set via `cf_{field_id}` on tasks and in view filters |
| Views (List/Board/Calendar) + filters | Yes | Create/update/delete/filter/group/sort via API at any hierarchy level |
| Calendar / Google Calendar invites | Native ClickUp integration, not documented as a distinct public API surface in this research | Treat as UI/native-integration behavior; confirm before automating invite creation via API |

## Gotchas / limits

- Custom task types cap at 100 per workspace and can only be created/edited through the UI — plan the taxonomy (e.g., Meeting, Prep Task, Decision) up front since the Super Agent can't provision new types on the fly via API.
- Free-plan task-type usage cap (20) is irrelevant to Sŏn (Business plan) but confirms plan gating exists — double-check nothing else in the restructure assumes Free-tier behavior.
- Relationship field's "Tasks from a specific List" binding is permanent once set — choose the target List carefully (e.g., binding Meetings → Founding Punch List) since changing it means creating a new field, not editing the existing one.
- Status "Closed" group tasks are hidden from views by default — if Sŏn uses a Closed-group status for completed/cancelled meetings, filtered views need to explicitly include Closed or those meetings will silently disappear from the default view.
- Recurring-task/template/Automation integration is reportedly weak (per 2026 community commentary) — don't assume "recurring task from template" alone delivers the rolling 4-week meeting creation with fresh Google Calendar invites; this likely needs custom Automation or Super Agent logic rather than native recurrence settings.
- Team-as-calendar-attendee and "apply status template via API" are both unconfirmed — flag as verification tasks before the Meetings Super Agent build, not assumptions to build on.
- Two-way Google Calendar sync reliability has open community feature requests as of the sources found — build in a verification/reconciliation step rather than trusting silent sync for meeting reschedules/cancellations.

## Implications for Sŏn

- **Custom task types**: create a workspace-wide "Meeting" (and possibly "Decision"/"Prep Task") custom task type once via UI; the Super Agent can assign it via API (`custom_item_id`) on task creation, and Founding Punch List views can filter on it.
- **Statuses**: give the Meetings List its own custom status set (e.g., Scheduled → Notes Pending → Notes Synced → Cancelled/Closed) built as a saved Status Template, distinct from the Founding Punch List's Not Started/Active/Done/Closed statuses; make sure any "Cancelled" status sits in the Closed group deliberately and that default filtered views account for that.
- **Owner field**: implement as a **People** custom field (workspace/"Everything" scope) so it's consistent across Meetings and Founding Punch List, without overloading Assignee.
- **Classification field**: implement as a **Dropdown** (single-select) at workspace scope unless a real multi-category need emerges, in which case switch to Labels — decide before populating tasks, since converting Dropdown↔Labels isn't a clean built-in operation (per open feature request "Convert Labels to Dropdowns").
- **Teams**: since Business plan includes Teams and the API supports Group CRUD, model "Team" attendee groups (e.g., Front of House, Kitchen, Founders) as ClickUp Teams now, even with only 2 founders, so the 3rd partner and future hires slot into existing groups; verify in the live workspace whether a Team can be attached directly as a Calendar invite attendee or whether the Super Agent must expand the Team to individual members before creating the Google Calendar invite.
- **Views/Founding Punch List**: build filtered views (by Owner, Classification, status) using the API so they're reproducible/scriptable as the workspace structure evolves, rather than manually configured and fragile to accidental edits; consider a small "View Templates" reference area as a fallback restore mechanism.
- **Hierarchy**: keep Meetings as its own Space (matches the stated goal); avoid deep Folder nesting for a 2–3 person team — Lists (e.g., "Recurring Meetings," "One-off Meetings") directly in the Meetings Space is likely sufficient rather than adding Folders prematurely.
- **Rolling 4-week meeting creation**: do not rely solely on ClickUp's native recurring-task settings to regenerate Google Calendar invites cleanly — design the Meetings Super Agent to explicitly create/cancel/reschedule tasks and their calendar events on the 4-week rolling window, using the Views/Custom Fields/Teams API surfaces confirmed above, and validate actual Google Calendar attendee/sync behavior live before finalizing that design.

## Sources

- [Custom task types – ClickUp Help](https://help.clickup.com/hc/en-us/articles/17564381376919-Custom-task-types)
- [Custom task types feature availability and limits – ClickUp Help](https://help.clickup.com/hc/en-us/articles/30661182619671-Custom-task-types-feature-availability-and-limits)
- [Custom Task Types via API — feature request](https://clickup.canny.io/feature-requests/p/custom-task-types-via-api)
- [Custom Task Types – ClickUp API docs](https://developer.clickup.com/docs/custom-task-types)
- [Filter and search tasks in List view – ClickUp Help](https://help.clickup.com/hc/en-us/articles/6310206119575-Filter-and-search-tasks-in-List-view)
- [Statuses for Folders – ClickUp Help](https://help.clickup.com/hc/en-us/articles/6308803927831-Statuses-for-Folders)
- [Manage task statuses – ClickUp Help](https://help.clickup.com/hc/en-us/articles/6309452618647-Manage-task-statuses)
- [Status templates – ClickUp Help](https://help.clickup.com/hc/en-us/articles/6309533958935-Status-templates)
- ["Not Started" Status Group – ClickUp Changelog](https://feedback.clickup.com/changelog/not-started-status-group-clickapp)
- [Create user groups with Teams – ClickUp Help](https://help.clickup.com/hc/en-us/articles/6326036524823-Create-user-groups-with-Teams)
- [Teams feature availability and limits – ClickUp Help](https://help.clickup.com/hc/en-us/articles/30914854991255-Teams-feature-availability-and-limits)
- [Create Group – ClickUp API reference](https://developer.clickup.com/reference/createusergroup)
- [Get Groups – ClickUp API reference](https://developer.clickup.com/reference/getteams1)
- [Intro to Custom Fields – ClickUp Help](https://help.clickup.com/hc/en-us/articles/6303536766231-Intro-to-Custom-Fields)
- [Label vs Tag in ClickUp – ProcessDriven](https://processdriven.co/clickup/how-to-use-clickup/label-vs-tag-in-clickup-whats-the-difference/)
- [Convert Labels to Dropdowns — feature request](https://feedback.clickup.com/feature-requests/p/convert-labels-to-dropdowns)
- [Add a Custom Field to a new location – ClickUp Help](https://help.clickup.com/hc/en-us/articles/16544932876311-Add-a-Custom-Field-to-a-new-location)
- [Create Relationship Custom Fields – ClickUp Help](https://help.clickup.com/hc/en-us/articles/14276813483031-Create-Relationship-Custom-Fields)
- [Relationships should allow choosing from selected list(s) — feature request](https://feedback.clickup.com/feature-requests/p/relationships-should-allow-to-choose-from-selected-list-or-lists-not-just-from-a)
- [Views – ClickUp API docs](https://developer.clickup.com/docs/views)
- [Filter Views – ClickUp API docs](https://developer.clickup.com/docs/filter-views)
- [Saving view filters – ClickUp Help](https://help.clickup.com/hc/en-us/articles/6311659064983-Saving-view-filters)
- [Hierarchy best practices – ClickUp Help](https://help.clickup.com/hc/en-us/articles/20480724378135-Hierarchy-best-practices)
- [Set a default task template for Lists – ClickUp Help](https://help.clickup.com/hc/en-us/articles/13225295700759-Set-a-default-task-template-for-Lists)
- [Use task templates – ClickUp Help](https://help.clickup.com/hc/en-us/articles/6309918176535-Use-task-templates)
- [Apply template to recurring tasks — feature request](https://feedback.clickup.com/feature-requests/p/apply-template-to-recurring-tasks)
- [How to Create ClickUp Recurring Tasks [2026 Guide] – Cloudwards](https://www.cloudwards.net/clickup-recurring-tasks/)
- [Recurring Meeting Agenda Template – ClickUp](https://clickup.com/templates/meeting-agenda/recurring-meetings)
- [Create events and schedule meetings from your Planner – ClickUp Help](https://help.clickup.com/hc/en-us/articles/35975552416023-Create-events-and-schedule-meetings-from-your-Planner)
- [ClickUp Google Calendar Integration – Unito](https://unito.io/integrations/clickup-google-calendar/)
- [2-way sync for Google Calendar — feature request](https://feedback.clickup.com/feature-requests/p/2-way-sync-for-google-calendar)
