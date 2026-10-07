# Claude (Anthropic) as an Automation Layer — Sŏn Meetings System
Researched 2026-09-16. Current as of September 2026 where noted; several features (Routines, ClickUp MCP) are in beta/research preview and may change.

## Key findings

1. **CONFIRMED** — Anthropic ships three distinct scheduling surfaces with different tradeoffs: **Cloud Routines** (Anthropic-managed cloud, runs even if your laptop is off, connectors "configured per task," no approval prompts, min interval 1 hour), **Desktop scheduled tasks** (local, machine must be on and app open, configurable permissions, min interval 1 minute, has local file access), and **`/loop`** (session-scoped, in-CLI polling). [code.claude.com/docs/en/desktop-scheduled-tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks)
2. **CONFIRMED** — A weekly 4-week-rolling meeting job should be a **Cloud Routine**, not a Desktop task: Desktop tasks skip a run entirely if the computer is asleep at the scheduled time (only one catch-up run in the last 7 days is auto-fired), which is a real risk for a weekly job on a laptop. [code.claude.com/docs/en/desktop-scheduled-tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks)
3. **CONFIRMED** — Routines run **fully autonomously with no approval prompts** during a run — "there is no permission-mode picker and no approval prompts during a run" — and "Claude can use every tool from an included connector, including writes, without asking for permission." This is both the reason Routines can own recurring writes and the reason to scope connectors tightly per routine. [code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines)
4. **CONFIRMED** — Routines are gated to **Pro, Max, Team, and Enterprise plans** (not Free), require a claude.ai subscription login (not API-key/Bedrock/Vertex auth), and `/schedule` in the CLI will fail with an auth error otherwise. Minimum interval is 1 hour; a true weekly cadence needs a custom cron via `/schedule update`. [code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines)
5. **CONFIRMED** — Routine connectors are your **claude.ai account-level connectors** (claude.ai/customize/connectors), not locally added `claude mcp add` servers — those stay on your machine and won't be available to a cloud routine unless re-added as a claude.ai connector or committed via `.mcp.json` in the repo the routine clones. This matters because Sŏn's setup likely has MCP servers configured locally in Claude Code CLI sessions. [code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines)
6. **CONFIRMED — official connectors exist for all four target apps**: Google Calendar, Gmail, and Google Drive (GA since ~Feb 2026, works in Claude and Claude Desktop) and Granola (first-party MCP connector, added ~Jan 2026, OAuth sign-in, no API keys). [support.claude.com](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors), [claude.com/connectors/granola](https://claude.com/connectors/granola), [granola.ai/blog/granola-mcp](https://www.granola.ai/blog/granola-mcp)
7. **CONFIRMED** — ClickUp's connector to Claude is **official** (ClickUp's own hosted MCP server at `mcp.clickup.com`), currently in **public beta**, free on all ClickUp plans. Auth is **OAuth only** — "you cannot authenticate using your own API keys or Auth access tokens." [developer.clickup.com](https://developer.clickup.com/docs/connect-an-ai-assistant-to-clickups-mcp-server), [usecarly.com/blog/clickup-mcp](https://www.usecarly.com/blog/clickup-mcp/)
8. **CONFIRMED — ClickUp official MCP write surface is narrow**: create task, update task (status/assignee/due date/description), create comment, time tracking, and Docs read/write, plus workspace search. **No deletion tools** (safety-by-design) and **no custom field creation** through MCP (custom field *values* can be read/set on existing fields, but creating new custom fields still requires the REST API). List/Space/Folder creation is not part of the documented 6-tool official set. [developer.clickup.com](https://developer.clickup.com/docs/connect-an-ai-assistant-to-clickups-mcp-server)
9. **UNCERTAIN but relevant** — a much larger community/third-party ClickUp MCP server (e.g., `clickup-cli`, ~144 tools) covers close to 100% of the ClickUp API, including lists, custom fields, etc. This session already has a ClickUp MCP connector (`daa70cda-...clickup_*`) with a far broader toolset than the official 6 — confirm with Dominic/Brandon which server is actually wired to the Meetings Super Agent, since "official ClickUp connector" and "the MCP tools available in this session" are not the same server. [mcpservers.org](https://mcpservers.org/servers/imjoshnewton/clickup-mcp-server)
10. **CONFIRMED** — ClickUp MCP rate limits are aggressive without the "Everything AI" add-on: 50 calls/24h on Free, 300 calls/24h on Unlimited+. A weekly roll-forward creating/updating many recurring meeting tasks plus a notetaker workflow could hit this quickly; the Everything AI add-on removes the special MCP cap and matches normal Public API limits. [developer.clickup.com](https://developer.clickup.com/docs/connect-an-ai-assistant-to-clickups-mcp-server)
11. **CONFIRMED — Claude's plain chat ClickUp connector has no autonomy**: "it only works in a conversation you start... nothing fires on a ClickUp event." This rules out chat-connector-only automation; the weekly roll-forward must be driven by a Routine (or the ClickUp MCP tools directly from a script/task), not by "asking Claude in chat." [usecarly.com/blog/claude-clickup-integration](https://www.usecarly.com/blog/claude-clickup-integration/)
12. **CONFIRMED — Routine prompts are "attested," not live user input**: a fired routine's stored prompt is treated as an authorized task, not as untrusted content — but content Claude *fetches during the run* (e.g., a ClickUp comment, a Granola note) keeps normal untrusted-content handling. Design the roll-forward prompt to not blindly execute instructions found inside meeting notes or task descriptions it reads mid-run. [code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines)
13. **CONFIRMED — model tiers, Sept 2026 API pricing**: Haiku 4.5 ($1/$5 per M tok), Sonnet 5 ($2/$10), Opus 5 ($5/$25), Fable 5.1 ($10/$50). For a recurring, well-specified job like weekly roll-forward (structured create/cancel/reschedule + Calendar invites), **Sonnet 5** is the right default — cheap enough for weekly runs, strong enough for multi-tool orchestration (ClickUp + Calendar + Granola). Reserve Opus 5 for the post-meeting notes → action-items extraction step if Sonnet's summarization quality proves insufficient on messy Granola transcripts. Routine subscription plans (Pro/Max/Team) bundle usage rather than metering per-call, so exact per-run cost is less material than staying under the daily routine-run cap. [tminusai.com](https://www.tminusai.com/blog/claude-api-pricing-monthly-cost-2026), [code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines)
14. **CONFIRMED — headless auth is fragile for locally-run automation**, separate from Routines: a filed Claude Code issue documents that non-interactive (`--print`/SDK) local CLI sessions can spuriously report healthy OAuth connectors as needing re-auth, and `claude setup-token` bootstrap tokens don't auto-refresh. This is a reason to prefer cloud Routines (which route connector calls through Anthropic's servers using your already-authenticated claude.ai connectors) over a self-hosted headless Claude Code script for this job. [github.com/anthropics/claude-code/issues/77534](https://github.com/anthropics/claude-code/issues/77534)
15. **CONFIRMED — GitHub App and repo requirement**: every Routine clones one or more GitHub repositories, even if the routine's actual work is against ClickUp/Calendar, not code. For a Meetings Super Agent that isn't code-centric, you'll still need a (even minimal/empty) repo to satisfy the routine's repository requirement. [code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines)

## Detailed notes

### Scheduling surface comparison (from official docs table)
| | Cloud Routine | Desktop scheduled task | `/loop` |
|---|---|---|---|
| Runs on | Anthropic cloud | Your machine | Your machine |
| Machine must be on | No | Yes | Yes |
| Survives restart | Yes | Yes | Mostly (resume-based) |
| Local file access | No (fresh clone) | Yes | Yes |
| MCP/connectors | Per-routine claude.ai connectors | Config files + connectors | Inherits session |
| Permission prompts | None (autonomous) | Configurable | Inherits session |
| Min interval | 1 hour | 1 minute | 1 minute |

Source: [code.claude.com/docs/en/desktop-scheduled-tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks)

### Auth model per connector
- **Google Calendar/Gmail/Drive**: official Anthropic connectors, GA, available on Claude.ai and Desktop, works with Routines via account-level connector. Confirmed capable of create/update/delete events, recurring meetings, RSVP, Meet links. [support.claude.com](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors), [usecarly.com/blog/claude-google-calendar-integration](https://www.usecarly.com/blog/claude-google-calendar-integration/)
- **Granola**: official MCP connector, OAuth, Business plan needed for full workspace history/folders/transcripts (Free/Basic only gets 30 days, no transcripts) — relevant since Sŏn wants Granola notes in Brain search. [granola.ai/blog/granola-mcp](https://www.granola.ai/blog/granola-mcp)
- **ClickUp**: official MCP, OAuth-only, public beta, 6-tool surface (search, create task, update task, comment, time tracking, docs). No delete, no custom-field creation, no list/space creation documented.

### Routine mechanics worth designing around
- Prompts are saved once and fired as an "assigned task," not live chat — write the roll-forward prompt to be fully self-contained (what weeks to open, what template to use, who's on each Team, cancel logic, invite defaults).
- `text` passed via API trigger or Run Now arrives wrapped as **untrusted** `<routine-fire-payload>` — the saved prompt must explicitly say to act on it, or it's inert. Useful if the Super Agent is also invokable ad hoc (e.g., "cancel next week's ops meeting") via an API trigger with `text`.
- Routines "belong to your individual account" — not shared with teammates. With Brandon + Dominic + soon a 3rd partner, decide **whose account owns the Meetings Super Agent routine** now, since connector actions (Calendar invites, ClickUp writes) appear as that person's identity.

## Gotchas / limits

- Desktop scheduled tasks **skip runs entirely** if asleep — do not use for the weekly roll-forward; only for local/manual convenience tasks.
- Routine minimum interval is 1 hour; for true weekly cadence you must use `/schedule update` with a custom cron (UI presets top out at "Weekly").
- Local `claude mcp add` MCP servers are invisible to cloud Routines — must be registered as claude.ai connectors or shipped via committed `.mcp.json`.
- ClickUp MCP (official) has no delete tools and no custom-field-creation — if the Meetings Super Agent needs to create new custom fields (e.g., a "Classification" field) as part of workspace restructure, that step needs the ClickUp web UI or REST API, not MCP.
- ClickUp MCP rate limits (50–300 calls/24h without Everything AI add-on) are easy to hit with a Super Agent doing search + multiple creates/updates weekly across many meetings — check whether the workspace already has the Everything AI add-on (workspace context says "Business plan + AI add-on," which likely satisfies this).
- Confirm which ClickUp MCP server this environment's `daa70cda-...` connector actually is (official 6-tool vs. broader third-party) before assuming certain write operations (e.g., create_list, add_tag) are officially supported/stable.
- Routines require a GitHub repo attached even for non-code automation — minor friction to set up once.
- Headless/local automation (running Claude Code as a script rather than via Routines) has a documented OAuth-reporting bug for non-interactive sessions — avoid this path for the production job; prefer Routines.

## Implications for Sŏn

- **Weekly meeting roll-forward + Calendar invites**: implement as a **Claude Code Cloud Routine** on Sonnet 5, custom weekly cron, connectors scoped to ClickUp + Google Calendar only. This satisfies "runs even if laptop is off," avoids Desktop's asleep-skip risk, and needs no standing local process.
- **Cancel/reschedule**: can live in the same Routine via an **API trigger** (so it's callable on demand, e.g. from a ClickUp automation or a simple form) with the fire `text` holding which meeting/week to change — remembering the prompt must explicitly reference the fire payload to act on it.
- **Post-meeting notes → action items**: best as a **second Routine** (or a step in the same one) triggered after Granola/AI Notetaker produces notes — reads Granola via its connector, extracts action items, writes them back as ClickUp tasks/comments via the ClickUp connector. Consider Opus 5 only if Sonnet 5's extraction quality on real Granola transcripts proves weak; start with Sonnet 5.
- **Ownership split recommendation**: Claude Routines should own the *scheduling and write mechanics* (create/cancel/reschedule tasks + Calendar invites, notes-to-action-items), while ClickUp itself (recurring tasks, custom fields, Teams/views) should own the *system of record and structure*. Don't try to make a "ClickUp Super Agent" (e.g. ClickUp Automations/AI) do the Google Calendar invite + Granola ingestion work — ClickUp's own automation layer has no first-party Google Calendar/Granola connectors as capable as Claude's; Claude Routines is the better home for the cross-app orchestration, with ClickUp as the data target.
- **Account/identity decision needed**: pick one workspace member's claude.ai account (likely whichever founder is designated as the operational owner) to host the Meetings Super Agent Routine, since all its connector actions will carry that person's identity — flag this explicitly to Brandon/Dominic before building.
- **Add Everything AI add-on check**: verify it's active (workspace context says it should be) to avoid ClickUp MCP's low daily call caps throttling the Super Agent.

## Sources

- [Automate work with routines — Claude Code Docs](https://code.claude.com/docs/en/routines)
- [Schedule recurring tasks in Claude Code Desktop — Claude Code Docs](https://code.claude.com/docs/en/desktop-scheduled-tasks)
- [ClickUp's MCP Server — developer.clickup.com](https://developer.clickup.com/docs/connect-an-ai-assistant-to-clickups-mcp-server)
- [ClickUp MCP: The Official Server at mcp.clickup.com — usecarly.com](https://www.usecarly.com/blog/clickup-mcp/)
- [ClickUp MCP Server | Awesome MCP Servers — mcpservers.org](https://mcpservers.org/servers/imjoshnewton/clickup-mcp-server)
- [Claude + ClickUp: What the Integration Can (and Can't) Do in 2026 — usecarly.com](https://www.usecarly.com/blog/claude-clickup-integration/)
- [Claude + Google Calendar: What the Integration Can (and Can't) Do in 2026 — usecarly.com](https://www.usecarly.com/blog/claude-google-calendar-integration/)
- [Use Google Workspace connectors — Claude Help Center](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors)
- [Granola Connector | Claude by Anthropic](https://claude.com/connectors/granola)
- [Granola MCP: Connect your meeting notes to Claude, ChatGPT, and Cursor — granola.ai](https://www.granola.ai/blog/granola-mcp)
- [Claude API Pricing (September 2026) — T-Minus AI](https://www.tminusai.com/blog/claude-api-pricing-monthly-cost-2026)
- [MCP: headless (--print) sessions emit spurious "requires authentication" — GitHub Issue #77534](https://github.com/anthropics/claude-code/issues/77534)
- [Claude Code Routines: The Complete Guide (2026) — makerkit.dev](https://makerkit.dev/blog/tutorials/claude-code-routines-guide)
