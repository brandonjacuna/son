> Moved from the build-out workspace on 2026-10-07 (decision M2: one shared ClickUp knowledge base). Merge its unique points into `clickup-knowledge-base.md`, then delete this file.

# ClickUp knowledge base

Portable reference for building in ClickUp with code plus AI. Everything here was verified against a live Business-plan workspace with the AI add-on between 2026-09-16 and 2026-09-21, either by API call or by a documented source. Re-verify before relying on a limit: ClickUp ships changes constantly.

Legend: **[V]** verified in this workspace · **[D]** documented by ClickUp · **[?]** unconfirmed.

---

## 1. Access

- **Personal API token**: ClickUp → avatar → Settings → Apps → Generate. Send it as the raw `Authorization` header, with no "Bearer" prefix. **[V]**
- **Store it outside the repo.** macOS Keychain works well:
  - save: `security add-generic-password -a <account> -s clickup-api-token -U -w`
  - read: `security find-generic-password -s clickup-api-token -w`
  - Code reads it at call time, so the token never lands in a file, a log, or a transcript. **[V]**
- **Base URLs**: `https://api.clickup.com/api/v2/` for most objects, `/api/v3/` for Docs and Chat. **[V]**
- **Rate limit**: 100 requests/minute on Business. Watch `X-RateLimit-Remaining`, retry 429s after ~15s. **[V]**

---

## 2. What the API can and cannot do

### Can
| Thing | Endpoint | Notes |
|---|---|---|
| Spaces, folders, lists | `POST /team/{id}/space`, `/space/{id}/folder`, `/space/{id}/list` | Space features are set with `PUT /space/{id}` `{features:{...}}` **[V]** |
| **Create custom fields** | `POST /list/{id}/field` | Undocumented but real. Fails with `FIELD_605` until the Custom Fields ClickApp is on for that space **[V]** |
| Relationship fields | same, `type: "list_relationship"`, `type_config.subcategory_id = <target list>` | The reciprocal side is not returned by the API but appears in the UI **[V]** |
| Set field values | `POST /task/{id}/field/{field_id}` | Labels/relationships take `{"value":{"add":[ids]}}`; dropdowns take the option id; dates take epoch ms **[V]** |
| Tasks | `POST/PUT /list/{id}/task`, `/task/{id}` | `custom_item_id` sets the task type; `markdown_description` writes markdown **[V]** |
| Create a task from a template | `POST /list/{id}/taskTemplate/{template_id}` | Keeps embedded views. Templates list: `GET /team/{id}/taskTemplate?page=0` **[V]** |
| Move a task to another list | `PUT /api/v3/workspaces/{wid}/tasks/{task_id}/home_list/{list_id}` | Body needs `status_mappings:[{source_status_id,destination_status_id}]`, plus `move_custom_fields:true` and `custom_fields_to_move:[ids]` to carry values **[V]** |
| Views | `POST/PUT /list/{id}/view`, read tasks with `GET /view/{id}/task` | See §3 for filter syntax **[V]** |
| Checklists | `POST /task/{id}/checklist`, `/checklist/{id}/checklist_item` | Items take name and assignee only, **no due dates** **[D]** |
| Docs | `POST /api/v3/workspaces/{wid}/docs`, `/docs/{id}/pages`, `PUT .../pages/{page_id}` | `content_format: "text/md"`; `parent.type`: 4 space, 5 folder, 6 list, 12 workspace **[V]** |
| Comments | `GET/POST /task/{id}/comment` | **[V]** |
| Chat, including DMs with Super Agents | `/api/v3/workspaces/{wid}/chat/channels`, `/channels/{id}/messages`, `/messages/{id}/replies` | Lets code prompt an agent and read its reply **[V]** |
| Tags | `DELETE /task/{id}/tag/{name}` | **[V]** |

### Cannot
| Thing | Reality |
|---|---|
| Rename a field or edit its options | No endpoint; `PUT /field/{id}` returns 405. UI only **[V]** |
| Create rollup fields | `FIELD_466` even with the ClickApp on. UI only, as view columns **[V]** |
| Create or edit statuses | UI only **[V]** |
| Create task types | UI only **[V]** |
| Create automations | UI only **[V]** |
| Apply a template to an existing task | No endpoint. Automations can (see §4) **[V]** |
| Move a subtask on its own | "Task cannot be moved to a new home list" **[V]** |
| See or write embedded views | Embeds read back as blank and any description write deletes them (see §6) **[V]** |
| Create Button custom fields | `FIELD_450`: a button must be created with its automation, in the UI **[V]** |

---

## 3. View filters (hard-won syntax)

```json
"filters": {"op":"AND","fields":[ ...clauses... ],"search":"","show_closed":false}
```

- **Custom field**: `{"field":"cf_<field_id>","op":"EQ","values":["<option id>"]}` **[V]**
- **Task type**: `{"field":"customItems","op":"EQ"|"NOT","values":[1002,1003]}` **[V]**
- **Status by name**: `{"field":"status","op":"EQ","values":["held"]}` — **lowercase only**; a capitalised or unknown value makes ClickUp silently drop the whole filter set **[V]**
- **Hide done/closed statuses**: `{"field":"statusType","op":"NOT","values":["done"]}`. More reliable than filtering status ids, which get dropped on some lists **[V]**
- **Relative dates**: `{"field":"dueDate","op":"EQ","values":[{"op":"thisweek"}]}` **[V]**
- **Field is set**: `{"field":"cf_<id>","op":"IS SET","values":[]}` **[V]**
- **Always verify after writing**: read the view back and compare `len(filters.fields)` to what you sent, then count `GET /view/{id}/task`. Dropped clauses are silent. **[V]**
- `GET /view/{id}/task` returns **top-level tasks only**, so counts look low next to a list's task count. **[V]**
- Grouping by **List or Space is not supported** at any level. Sections by department mean one view per list. **[D]**

---

## 4. Automations

- **Triggers**: task created, status changes, custom field changes, date arrives (with before/after offsets), button clicked, Google Calendar event created/updated/cancelled. **[V]**
- **Actions** include: change status/assignee/priority/dates, set custom field, create task, create subtask, move or add to list, post comment, apply a template, call a webhook, **run a Super Agent**. **[V]**
- **Conditions** exist (2026) and can test custom fields. **[V]**
- **Apply a template** is the only way to put a template on a task programmatically. It is **all or nothing** and overwrites fields, so create the task bare, let the template land, then set fields. **[V]**
- **Google Calendar delete/update actions match events by title keywords, not by event id.** An event created outside ClickUp's own integration fails with `AUTO_505 "Integration event not found"`. Store the exact event title in a field and feed that field to the action. **[V]**
- **Cannot** clear a field reliably, and cannot point a relationship at "the task that triggered this automation" — relationship targets are picked at build time. **[V]**
- **Button custom fields** run an automation on click. One button can set fields and call an agent. **[D]**
- **Instruction box**: when an automation calls an agent, that box is the source of truth. Do not duplicate the procedure in the agent's own instructions; a stale copy in either place will win at random. **[V]**

---

## 5. Super Agents

- **Automations can run an agent**, passing the triggering task plus an instruction box. **[D]**
- **Tools are opt-in.** Useful ones: Default tools (search, read), Update task, Create task, Create subtask, Post task comment, Docs, Google Calendar (list/create/update), external MCP servers. **[V]**
- **No tool creates a task from a saved template.** Agents must create bare tasks and let an automation apply the template. **[V]**
- **No Google Calendar delete tool** (Outlook has one). Deletion has to run through an automation. **[V]**
- **Agents can edit relationship fields** (2026). **[D]**
- **Knowledge scope** is set per agent: spaces, lists, docs. Narrow scope means fewer wrong answers. **[V]**

### Lessons that cost time
1. **A broad agent drifts.** One agent with five jobs plus memory of retired rules produced inconsistent results; a fresh agent with one clear job did not. Rebuild rather than patch after a few pivots. **[V]**
2. **Agents report success they did not achieve.** One reported "already on the agenda" for an item that was not there. Verify through the API, never from the agent's reply. **[V]**
3. **Read-modify-write on a description is the weakest operation.** One run silently wiped a section. If an agent must edit text, make the rule: read first, copy verbatim, write, read back, and restore on any loss. Prefer append-only targets (comments, subtasks, fields). **[V]**
4. **Agent runs take 1 to 4 minutes.** Do not design per-click AI where a field write would do. **[V]**
5. **Prompting agents from code** via chat DMs works well for setup and testing: send a message, poll `/messages/{id}/replies`, then verify the result yourself. **[V]**

---

## 6. Task and description behaviour

- **Section order on desktop is fixed**: fields, description, subtasks, checklists, comments. Checklists cannot sit above the description. Mobile allows reordering. **[D]**
- **Embedded views** can live in a Doc **or a task description**, are live and editable inline (status, assignee, dates), and are inserted with `/list` or by pasting a view link. **[D]**
- **Embeds are invisible to the API and to agents** and are destroyed by any description write. Keep automated writers away from any description holding an embed. **[V]**
- **Markdown that survives an API write**: headings, bold/italic, inline code, links, blockquotes, tables, checkbox lists (`- [ ]`), numbered lists, dividers, fenced code. **[V]**
- **Markdown that does not**: `:::callout` blocks and `<details>` toggles are stored as literal text. **[V]**
- **Task links in a description unfurl** with live title and status and create a reference relationship. **[D]**
- **Statuses belong to the list**, not the task type. Subtasks always use their list's statuses, and "statuses by task type" is an open request. **[D]**
- **One Closed status per list**; the Done group can hold several. **[V]**
- A task left in a removed status after a status-set change lands in limbo: it disappears from list queries and the API refuses to set its status (`ITEM_114`). Fix it in the UI. **[V]**
- Task templates save description, checklists, subtasks, custom field values, dates, assignees, tags, task type. "Update existing template" overwrites irreversibly. **[D]**

---

## 7. Patterns that work

**Live agenda (flag → live view → close-out).**
A dropdown field flags a task for a meeting. Table views filtered on that field, embedded in the meeting task, are the agenda; everything stays editable and real. An automation sets the meeting to Held one hour after its due date, and one agent run records a "Discussed in" relationship on each flagged task and clears the flag. No AI touches text, and a failed run leaves visible carry-over instead of lost data. **[V]**

**Two-way calendar sync without the native integration.**
Task dates change → automation → agent updates the same Google event. Event changes → Google Calendar trigger → agent updates the task's dates. Each side does nothing when the times already match, so changes bounce once and stop. Point the calendar trigger at a dedicated calendar, or it fires on every personal event. **[V]**

**Delete a calendar event from a status change.**
Agents cannot delete events. Store the exact event title in a field, and have an automation on status Canceled run the Google Calendar Delete action matched on that field. **[V]**

**Template-built tasks from an agent.**
Agent creates the task with name and the one field the automation's condition needs → automation applies the template → agent waits until the template's header text appears → agent sets the remaining fields → agent re-reads to confirm. Survives an all-or-nothing template. **[V]**

**Lossless export before restructuring.**
`GET /list/{id}/task` with `include_closed=true&subtasks=true&include_timl=true&include_markdown_description=true` returns custom field values and descriptions in one paginated call, which is far cheaper than per-task reads. Save the JSON, then diff against it after every migration: names, statuses, list, task type, tags, and especially `date_updated`, which proves nothing was edited. **[V]**

**Bulk writes with a preview.**
Generate a preview file (one row per task with the proposed value), get sign-off, apply, then verify by re-reading every task and comparing to the plan. Refuse to run when a task's ancestry hits a protected tree. **[V]**

---

## 8. Safety rules worth keeping

1. **Never delete.** Archive, or hand deletion to a human. Deletions have a 30-day Trash window; restoring from Trash keeps ids, comments and history, which recreating does not.
2. **Protect named trees** (a governance backlog, a register) by checking each task's top-level ancestor before any write.
3. **Verify every automated change through the API**, including agent work.
4. **Status renames are safe; status remaps are not.** Renaming keeps every task in place, which makes it the cheap way to reshape a status set.
5. **Never reapply a template to an existing task** unless you intend to wipe its fields.
6. **Log every change** with ids, and keep a dated file of decisions. Six sessions in, the log is what settles "why is this like this".

---

## 9. Minimal client

```python
"""cu.py — tiny ClickUp REST helper; token from Keychain, never printed."""
import json, subprocess, urllib.request, urllib.error, time
WID = "<workspace id>"
_T = subprocess.run(["security","find-generic-password","-s","clickup-api-token","-w"],
                    capture_output=True, text=True, check=True).stdout.strip()

def req(method, path, body=None, v=2):
    base = f"https://api.clickup.com/api/v{v}/"
    for _ in range(5):
        r = urllib.request.Request(base+path, method=method,
            headers={"Authorization": _T, "Content-Type": "application/json"},
            data=json.dumps(body).encode() if body is not None else None)
        try:
            with urllib.request.urlopen(r, timeout=60) as resp:
                txt = resp.read()
                return json.loads(txt) if txt else {}
        except urllib.error.HTTPError as e:
            if e.code == 429:
                time.sleep(15); continue
            raise RuntimeError(f"{method} {path} -> {e.code} {e.read()[:300]!r}")

def tasks(list_id, closed=True):
    out, page = [], 0
    while True:
        d = req("GET", f"list/{list_id}/task?include_closed={str(closed).lower()}"
                       f"&subtasks=true&include_timl=true&page={page}")
        out += d.get("tasks", [])
        if d.get("last_page", True) or not d.get("tasks"):
            return out
        page += 1
```

Prompting an agent and reading its reply:

```python
m = req("POST", f"workspaces/{WID}/chat/channels/{CHANNEL}/messages",
        {"type":"message","content_format":"text/md","content": prompt}, v=3)
replies = req("GET", f"workspaces/{WID}/chat/messages/{m['id']}/replies"
                     f"?content_format=text/md", v=3)["data"]
```

---

## 10. Error codes seen

| Code | Meaning | Fix |
|---|---|---|
| `FIELD_605` | Custom Fields ClickApp off for that space | `PUT /space/{id}` with `features.custom_fields.enabled = true` |
| `FIELD_466` | Rollups not available to the API | Build the rollup as a view column in the UI |
| `FIELD_450` | Button field needs an automation | Create it in the UI |
| `ITEM_114` | Status does not exist for that task | Task sits in a removed status; fix in the UI |
| `ITEM_013` | Task not found, deleted | Check Trash |
| `AUTO_505` | Integration event not found | The calendar action matches by title, not id |
| 405 on `PUT /field/{id}` | Field definitions are read-only over the API | UI |
