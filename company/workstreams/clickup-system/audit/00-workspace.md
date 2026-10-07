# Sŏn ClickUp Workspace Audit — Workspace Level

Workspace ID: `90131574430` | Plan: Business + AI add-on | Calendar sync: Google Calendar
Audit date: 2026-09-16 | Method: ClickUp MCP tools only, strictly read-only (no writes attempted)

---

## 1. Members

Only **2 workspace members** are readable via `clickup_get_workspace_members`:

| Name | User ID | Email | Role |
|---|---|---|---|
| Brandon John Acuña-Cardona | 144179365 | brandon@son.restaurant | not exposed by MCP |
| Dominic Thomas | 198005184 | dominic@son.restaurant | not exposed by MCP |

- No role/permission-level field (Owner/Admin/Member/Guest) is returned by this tool — see Capabilities gaps below.
- The 3rd partner mentioned in context is **not yet a workspace member**.
- A non-human actor, **user ID `-87977709`, username "Founders Meeting Assistant"**, appears as the `creator` of task `86akfka82` ("Weekly Founders Sync – 2026-09") and as the creator of a private DM channel (`2ky45bmy-13913`). This negative ID is characteristic of a ClickUp AI/bot actor, not a licensed seat — it does not appear in `clickup_get_workspace_members`. This is strong evidence an AI Notetaker / meeting-assistant integration is **already active** in this workspace, ahead of the planned Super Agent build. Recommend confirming its exact nature (ClickUp AI Notetaker vs. a custom automation) directly in ClickUp settings, since MCP cannot introspect bot/agent identities.

## 2. User Groups / Teams

**Not readable.** No MCP tool or enabled operator exposes ClickUp "Teams" (user groups). `clickup_get_workspace_members` returns only individual members, no group membership or group list. `clickup_get_schema` and `clickup_get_operators` (the two tools that could expose a Teams/groups model or operator) both return **"No enabled entities/operators match the request... Enabled entities/operators: none"** — i.e., the connected MCP server has zero schema entities and zero Unified-API operators enabled for this workspace. This is empirical evidence, not an assumption: both calls were made and both returned empty enabled-lists.

## 3. Custom Task Types

- `clickup_get_task` on task `86akfka82` shows `"task_type": "Meeting"` with `"custom_item_id": 1021` — confirming at least one custom task type named **Meeting** exists in the workspace (used on Founding Punch List). custom_item_id 1021 is a workspace-defined type (built-in types are low single-digit IDs).
- No tool enumerates the full list of custom task types defined workspace-wide (there is no `list_task_types` / `get_custom_item_types` tool, and `clickup_get_schema`/`clickup_get_operators` are empty as noted above). We only know what we can see stamped on individual tasks we happened to fetch.
- Other sampled tasks in Founding Punch List show `taskType: null` (default "Task" type).

## 4. Custom Fields

Checked with `clickup_get_custom_fields` at every available scope:

| Scope | Result |
|---|---|
| Workspace-level (`include_workspace: true`) | `workspace_fields: []` — none |
| Space: Founding Sŏn (90138396180) | `space_fields: []` — none |
| Space: Design & Visuals (90136725596) | `space_fields: []` — none |
| Space: Product (901312138543) | `space_fields: []` — none |
| List: Founding Punch List (901323485125) | **3 fields** (see below) |

List-level fields on Founding Punch List:
1. **Next Action** — type `text`
2. **Notes from BJAC** — type `short_text`
3. **Project** — type `drop_down`, options: Financials, White Paper, Pitch Deck, Research

No workspace- or space-level custom fields exist anywhere sampled; all custom field definition currently lives at the list level on one list. The planned **Owner** and **Classification** fields for the Founding Punch List (per project goals) do not exist yet.

## 5. Chat Channels

19 channels total (`clickup_get_chat_channels`, `has_more: false`, so this is the complete list):

| Channel | Type | Visibility | Creator |
|---|---|---|---|
| Sŏn | CHANNEL | PUBLIC | Brandon |
| Founding Punch List | CHANNEL | PUBLIC | Dominic |
| Sprint 0 (7/27–7/29) Redcar Response | CHANNEL | PUBLIC | Dominic |
| Josephine Pitch PunchList | CHANNEL | PUBLIC | Dominic |
| Programming Ideation | CHANNEL | PUBLIC | Brandon |
| Programming Pitch | CHANNEL | PUBLIC | Dominic |
| Event Team Personas | CHANNEL | PUBLIC | Dominic |
| Technology Capture | CHANNEL | PUBLIC | Brandon |
| Promotion Capture | CHANNEL | PUBLIC | Brandon |
| Promotion | CHANNEL | PUBLIC | Brandon |
| People Capture | CHANNEL | PUBLIC | Brandon |
| Operations Capture | CHANNEL | PUBLIC | Brandon |
| Events Capture | CHANNEL | PUBLIC | Brandon |
| Hospitality Capture | CHANNEL | PUBLIC | Brandon |
| Finance Capture | CHANNEL | PUBLIC | Brandon |
| The Josephine | CHANNEL | PUBLIC | Brandon |
| DM (unnamed) | DM | PRIVATE | user -87977709 ("Founders Meeting Assistant") |
| DM (unnamed) | DM | PRIVATE | Dominic |
| ASK_AI (unnamed) | ASK_AI | PRIVATE | Brandon |

Purpose inference from names and a light sample of messages:
- The **"Capture" channels** (one per space: People, Operations, Promotion, Events, Hospitality, Finance, Technology) mirror the "Capture" lists seen in the hierarchy — likely auto-notification/inbox channels tied to each space's capture list, not conversational channels.
- **"Sŏn"** and **"Founding Punch List"** are checked with a message sample: Founding Punch List channel returned 0 messages; the "Founders Meeting Assistant" DM contains one message, "A SyncUp Happened" (2026-09) — consistent with a meeting/notetaker bot posting a status ping.
- **"Josephine Pitch PunchList" / "The Josephine" / "Programming Ideation" / "Programming Pitch" / "Event Team Personas" / "Sprint 0 Redcar Response"** are named for specific initiatives/projects (deal or project code names) rather than general team chat.
- The **ASK_AI** channel is ClickUp's built-in AI chat surface, private to Brandon.
- No channel messages beyond the samples above were read (per audit scope: names/purpose only).

## 6. Docs

`clickup_search` (workspace-wide) surfaces at least one Doc directly:
- **"Scaling People: Translation Program"** — in the Operations space, filed under the **Operations Documents** folder, page "Program map and session tracker".

Doc *folders* visible in the hierarchy (these are ClickUp Docs container folders per space, confirmed via `clickup_get_workspace_hierarchy` and `clickup_get_folder`):
- Operations → **Operations Documents**
- Design & Visuals → **Design Documents**
- Finance → **Finance Documents**
- People → **People Notebooks**, **Education/Training Modules**
- Promotion → **Promotion Documents**
- Technology → **Tech Documents**, with sub-folders **Claude** and **Technology Build Out** (which itself contains two lists: "Function → SaaS Map" and "SaaS Catalog")

There is no dedicated "list all docs in workspace" MCP tool; `clickup_search` returns a mixed task/doc result set capped at 19 total results workspace-wide (same 19 came back for two different queries — the tool appears to return a fixed/sampled result set rather than a true paginated full-text index in this environment), so the doc inventory above is a lower bound, not a confirmed complete list. The **Claude** folder under Tech Documents (empty in the hierarchy snapshot) is worth a founder's manual look — its name suggests AI-tooling documentation that the MCP hierarchy call did not expand (folders can contain nested docs, not just lists/folders, which this hierarchy endpoint does not enumerate).

## 7. Reminders

`clickup_search_reminders` returned **0 reminders** workspace-wide (`total_count: 0`). Either none exist yet, or reminders are personal-to-user and only the authenticated user's (Brandon's) reminders are visible via this API — the tool has no parameter to query on Dominic's behalf.

## 8. Automations, Super Agents, Calendar Sync, AI settings

**Nothing here is readable through MCP.** No automation, agent, calendar-sync-configuration, or AI-settings tool exists in the loaded ClickUp toolset, and the two introspection tools that could reveal such entities are both empty:
- `clickup_get_schema` → `"No enabled entities match the request. Enabled entities: none"`
- `clickup_get_operators` → `"No enabled operators match the request. Enabled operators: none"`

Indirect evidence found while auditing tasks/chat (not a substitute for real settings visibility):
- The task **"Weekly Founders Sync – 2026-09"** (task type **Meeting**) contains a structured markdown body describing a live Google Calendar sync: calendar event ID, calendar owner (brandon@son.restaurant), timezone (America/Chicago), a Zoom link, and a manually-recorded reschedule exception (Sep 15 → Sep 16). This reads as either a manual convention the founders are keeping by hand, or the output of an early/partial automation — it is **not** proof of a working Super Agent, since nothing in this task references an agent ID, run log, or automation trail we can independently verify.
- A companion subtask **"Weekly Founders Sync Agenda 2026-09-16"** and a referenced parent **"Weekly Founders Sync – Series"** (`86ake5ud3`) suggest a monthly-container + dated-occurrence pattern already in informal use for at least one recurring meeting — relevant prior art for the planned rolling 4-week meeting scheduler.
- The bot-like creator `-87977709` "Founders Meeting Assistant" (section 1) is the closest thing to visible Super Agent/Notetaker activity, but its configuration (what triggers it, what it's allowed to write) is invisible to MCP.

**Conclusion: Automations, ClickUp AI Agents/Super Agents, and Calendar-sync settings must be audited manually in the ClickUp web app (Settings → Automations / Settings → Integrations → Calendar / the AI Agents panel), not through this MCP connector.**

## 9. What the MCP/API can and cannot read or change (with evidence)

**Cannot read or change (confirmed by a failed attempt or a missing operator/tool):**
| Area | Evidence |
|---|---|
| Task-type / custom-item-type definitions (list all types) | No tool to enumerate them; only ever seen incidentally via `task_type` on a fetched task |
| Space/list/folder status definitions — *create/edit* | No update-status tool exists; `clickup_get_list`/`clickup_get_task(expand_statuses)` are read-only views of existing statuses |
| Teams / user groups | No tool; `clickup_get_schema`/`clickup_get_operators` return zero enabled entities/operators |
| Member roles (Owner/Admin/Member/Guest) | `clickup_get_workspace_members` returns id/name/email/profilePicture only, no role field |
| Automations (rules, triggers, actions) | No tool; confirmed via empty `clickup_get_schema` / `clickup_get_operators` |
| ClickUp AI Agents / Super Agents (config, run logs) | No tool; confirmed via empty schema/operators |
| Calendar sync settings/configuration | No tool; only visible indirectly as text inside a task description |
| AI/Notetaker settings | No tool; only visible indirectly as a bot user ID and one DM message |
| Views (filtered/board/gantt view definitions) | No tool to list or read view configurations |
| Full workspace-wide doc inventory | No "list all docs" tool; `clickup_search` returns a capped, seemingly fixed 19-result set regardless of query, so doc coverage is partial |
| Reminders for a teammate other than the authenticated user | `clickup_search_reminders` has no user-scoping parameter beyond the authenticated user |
| Any create/update/delete operation | Not attempted, per this audit's read-only mandate — all mutating tools (create_task, update_task, create_folder, etc.) exist in the toolset but were intentionally never called |

**Can read (used successfully in this audit):**
Workspace hierarchy (spaces/folders/lists) and space/folder metadata; workspace members (id/name/email only); custom fields at workspace/space/folder/list scope; individual tasks (including custom fields, statuses available on their list, task type); task search/filter across the workspace; chat channel list and channel messages; document search (partial); reminders (own only, currently empty).

---

*See also: `/Users/brandonacuna/ClickUp/audit/mcp-capabilities.md` for the full tool/operator inventory with read/write classification.*
