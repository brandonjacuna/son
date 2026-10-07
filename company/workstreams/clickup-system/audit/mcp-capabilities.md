# ClickUp MCP — Tool & Operator Capability Inventory

Server: `daa70cda-fb71-479a-9e27-a042277a02d7` (ClickUp). Loaded via `ToolSearch(query:"+clickup", max_results:30)`.
Classification: **R** = read-only, **W** = write/mutating (create/update/delete/move/merge/attach/comment/send/track-time), **R/W** = tool is read-only in effect today but the underlying operator class is a write (noted where relevant).

This audit called **only R tools**. No W tool was invoked at any point.

## Dedicated `clickup_*` tools (38 total loaded)

### Read-only (R)
| Tool | Purpose |
|---|---|
| `clickup_get_workspace_hierarchy` | Spaces/folders/lists tree, paginated |
| `clickup_get_workspace_members` | List members (id, name, email — no role) |
| `clickup_get_folder` | Folder metadata |
| `clickup_get_list` | List metadata + status definitions |
| `clickup_get_task` | Full task detail (optionally custom fields, description, attachments, checklists, dependencies, linked tasks, subtasks, watchers) |
| `clickup_get_task_comments` | Task comments |
| `clickup_get_threaded_comments` | Threaded comment view |
| `clickup_filter_tasks` | Structured filter query across tasks (paginated, 100/page) |
| `clickup_search` | Cross-workspace keyword search (tasks + docs); appears capped/sampled at 19 results in this workspace regardless of query |
| `clickup_get_custom_fields` | Custom field definitions at workspace/space/folder/list scope |
| `clickup_get_bulk_tasks_time_in_status` | Time-in-status for up to 100 tasks |
| `clickup_get_task_time_in_status` | Time-in-status for one task |
| `clickup_get_time_entries` | Time tracking entries |
| `clickup_get_current_time_entry` | Currently-running timer |
| `clickup_get_chat_channels` | List chat channels |
| `clickup_get_chat_channel_messages` | Messages in a channel |
| `clickup_get_chat_message_replies` | Thread replies to a message |
| `clickup_get_document_pages` / `clickup_list_document_pages` | Doc page tree/content |
| `clickup_list_document_page_attachments` | Attachment metadata on a doc page |
| `clickup_download_document_page_attachment` | Short-lived download URL for a doc attachment |
| `clickup_download_task_attachment` | Short-lived download URL for a task attachment |
| `clickup_search_reminders` | Reminders (own user only — no cross-user scoping) |
| `clickup_find_member_by_name` | Resolve a member by name/email |
| `clickup_resolve_assignees` | Resolve names/emails/"me" to numeric user IDs |
| `clickup_get_schema` | Would list Unified-API entity schemas — **returned "no enabled entities" in this workspace** |
| `clickup_get_operators` | Would list enabled Unified-API operators — **returned "no enabled operators" in this workspace** |

### Write/mutating (W) — present in the toolset, intentionally never called
| Tool | Effect |
|---|---|
| `clickup_create_task` | Create task |
| `clickup_create_document` | Create doc |
| `clickup_create_document_page` | Create doc page |
| `clickup_update_document_page` | Overwrite/append/prepend doc page content |
| `clickup_create_folder` | Create folder |
| `clickup_update_folder` | Rename/update folder |
| `clickup_create_list` | Create list in a space |
| `clickup_create_list_in_folder` | Create list in a folder |
| `clickup_update_list` | Rename/update list |
| `clickup_create_reminder` | Create personal reminder |
| `clickup_update_reminder` | Update reminder |
| `clickup_delete_task` | Delete task |
| `clickup_move_task` | Move task between lists |
| `clickup_merge_tasks` | Merge tasks |
| `clickup_add_task_to_list` | Add task to an additional list |
| `clickup_remove_task_from_list` | Remove task from a list |
| `clickup_add_task_dependency` / `clickup_remove_task_dependency` | Dependency edges |
| `clickup_add_task_link` / `clickup_remove_task_link` | Task-to-task links |
| `clickup_add_tag_to_task` / `clickup_remove_tag_from_task` | Tag a task |
| `clickup_update_task` | Update any task field |
| `clickup_create_comment` / `clickup_create_task_comment` (deprecated alias) | Post a comment |
| `clickup_update_comment` | Edit a comment |
| `clickup_delete_comment` | Delete a comment |
| `clickup_attach_task_file` | Attach a file to a task |
| `clickup_request_attachment_upload` | Request an upload slot for a local file |
| `clickup_add_time_entry` / `clickup_start_time_tracking` / `clickup_stop_time_tracking` | Time tracking writes |
| `clickup_send_chat_message` | Post a chat message |
| `clickup_execute_operator` | Runs one enabled Unified-API operator — **0 operators enabled in this workspace, so currently a no-op regardless of read/write intent** |

## Unified-API operators (`clickup_execute_operator` / `clickup_get_operators` / `clickup_get_schema`)

`clickup_get_schema()` and `clickup_get_operators()` were both called with no scoping arguments and both returned:
> "No enabled entities/operators match the request. Enabled entities/operators: none."

This means the Unified-API operator layer (which the server description says can expose additional entities/operators beyond the dedicated `clickup_*` tools, taxonomy: get/list/create/update/delete/get_many/list_children/duplicate/merge/archive/unarchive/restore/search/move/create_many/update_many/delete_many) is **fully disabled** for this connection — zero entities and zero operators enabled, read or write. `clickup_execute_operator` is therefore non-functional in this environment: any call to it will be rejected since no `model`/`operator` pair is enabled. This is the mechanism that would have exposed Teams/user-groups, automations, task-type management, and agent config if it were turned on — its being empty is the primary reason those areas are unreadable (see Section 9 of `00-workspace.md`).

## Net capability summary

- **Readable today:** hierarchy, members (partial), tasks + their custom fields/comments/time/attachments (metadata), search (partial/capped), chat channels + messages, docs (partial), reminders (own only).
- **Not readable at all, by any tool or operator:** member roles, Teams/user groups, task-type definitions list, status-definition editing surface, automations, ClickUp AI Agents/Super Agents config and logs, calendar-sync settings, AI/Notetaker settings, saved/filtered views.
- **Not exercised (write tools exist but were not called, per read-only mandate):** every tool in the "Write/mutating" table above, plus `clickup_execute_operator` (which is moot — no operators are enabled to run).
