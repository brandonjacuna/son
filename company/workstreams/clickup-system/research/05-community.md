# Community Builds & Utilization Strategy — Research Brief
Researched 2026-09-16. Topic: meeting hub builds, Super Agent real-world use, small-team workspace architecture, task/classification schemes, restaurant pre-opening structures.

## Key findings

1. **CONFIRMED** — ClickUp sells purpose-built meeting templates (Recurring Meeting Agenda, Meeting Notes, Meeting Minutes) built on Docs, with Board/Calendar/Document views and notes that convert into tasks/Kanban cards live. [ClickUp Recurring Meetings template](https://clickup.com/templates/meeting-agenda/recurring-meetings)
2. **CONFIRMED** — ClickUp AI Notetaker joins Zoom/Meet/Teams (and native SyncUps), transcribes, summarizes, and can create tasks from notes — but that task-creation quality depends on ClickUp Brain being enabled; without Brain it's noticeably weaker. [Votars review](https://votars.ai/en/blog/clickup-ai-notetaker-review/)
3. **CONFIRMED/GOTCHA** — AI Notetaker caps video recording at 60 minutes; meetings that run past that get audio-only, no live transcription during the call (transcript comes after), and note quality degrades on long meetings. English-only currently, multilingual "in development." [Jamie review](https://www.meetjamie.ai/blog/clickup-ai-note-taker-review), [ClickUp feedback board](https://feedback.clickup.com/feature-requests/p/ai-notetaker-recordings-longer-than-60-minutes)
4. **CONFIRMED** — AI features (Brain, Notetaker, Super Agents) are a paid add-on layered on top of a plan, not bundled free — matches your existing AI add-on purchase. [summarizemeeting.com ClickUp review](https://summarizemeeting.com/en/app-reviews/clickup)
5. **CONFIRMED** — ClickUp markets "Meeting Scheduler," "Calendar Management," and "Scheduling Automation" AI agents that find mutual availability, send/confirm invites, and reschedule on conflicts, plus drag-and-drop reschedule in Calendar view — directly maps to your one Super Agent handling create/cancel/reschedule. [ClickUp Meeting Scheduler agent](https://clickup.com/p/ai-agents/meeting-scheduler)
6. **UNCERTAIN** — Independent, hands-on user reports of Super Agent (not vendor marketing) are thin as of Sept 2026; the clearest independent signal is a complaint of inconsistent output format day-to-day with "no prompting" behind it, and a general critique that most published use cases are demoed, not shown running live. Treat Super Agent as **early/beta-grade for anything beyond simple, well-scoped triggers** — build it narrowly (create/cancel/reschedule only) and verify output for the first several weeks rather than trusting it unattended. [Vellum, ClickUp Super Agent alternatives](https://www.vellum.ai/blog/best-clickup-ai-super-agents-alternatives)
7. **CONFIRMED** — Reddit-specific threads on Super Agent were not surfaced by search (may be too new/low-volume); do not over-index on Reddit sentiment for Super Agent specifically — evidence base is vendor docs + a few reviewer blogs only.
8. **CONFIRMED** — A May 2026 consultant guide for a 20-person team (Velox Consulting) recommends **4–6 Spaces organized by department/function**, not by client or project, explicitly warning that "a Space per client" (here: per meeting, per initiative) creates navigation problems at even moderate scale. Folders = one per client/initiative; Lists = individual project boards with consistent status sets. [Velox Consulting, May 25 2026](https://velox.consulting/blog/how-to-set-up-clickup-for-a-20-person-team)
9. **CONFIRMED** — Same source: keep custom fields minimal — Owner (distinct from Assignee), Priority, Due Date, Effort Estimate — and push most classification into **Folder/List location** rather than proliferating fields. This directly bears on your planned Classification field: consider whether some of that distinction (e.g. meeting type) is better expressed as List structure or Task Type than as a field.
10. **CONFIRMED** — ClickUp's own hierarchy guidance: Space-level settings (statuses, etc.) cascade to Folders/Lists; Folder settings cascade to Lists — supports your "statuses per space/list" plan being layered top-down rather than set independently everywhere. [ClickUp Help: Set up your Workspace](https://help.clickup.com/hc/en-us/articles/10636005013271-Set-up-your-team-s-Workspace-from-scratch)
11. **CONFIRMED** — Custom Task Types let each type carry its own Custom Fields and statuses, and multiple Task Types can coexist in one List — useful for a Meetings space where "Meeting" and "Action Item" could be distinct task types in the same list rather than separate lists. [ClickUp Help: Custom task types](https://help.clickup.com/hc/en-us/articles/17564381376919-Custom-task-types)
12. **CONFIRMED** — ClickUp guidance on Teams (user groups): reserve Teams for **stable, long-term groups**; avoid spinning up a Team for every short-lived project — use tags/views instead. For a 2-3-person founding group this argues for very few Teams (e.g. "Founders," maybe "All Staff" once hiring starts) rather than a Team per meeting type. [consultevo.com, ClickUp Teams guide](https://consultevo.com/clickup-manage-teams-guide/)
13. **CONFIRMED** — Granola is popular specifically because it captures audio without a bot joining the call (good for in-person/phone), which matches your split: Granola for in-person/phone, ClickUp AI Notetaker (bot-based) for remote meetings. Third-party connectors (e.g. Carly) exist to pipe Granola notes into ClickUp tasks automatically if native import proves weak. [zackproser.com Granola review](https://zackproser.com/granola), [usecarly.com](https://www.usecarly.com/blog/granola-alternatives/)
14. **CONFIRMED** — ClickUp restaurant-specific templates exist (Project Plan, Project Charter, Work Breakdown Structure) covering permits, buildout, hiring, menu R&D, and marketing as the standard phase set for pre-opening — a reasonable starting checklist skeleton for the Founding Punch List. [ClickUp Restaurant Project Plan](https://clickup.com/templates/project-plan/restaurant)
15. **UNCERTAIN** — Could not confirm a specific day-count (e.g. "90-day") critical-path structure from a live, accessible source in this pass (RestaurantOwner.com's 90-Day chart and thehotelblueprint.com's 350+-task checklist are gated/paywalled); use the ClickUp restaurant templates plus your own timeline rather than relying on an unseen external checklist.

## Detailed notes

**Meeting hub patterns.** The common pattern across ClickUp's own templates and third-party builds is: one Doc (or List item) per meeting series holding a living agenda, a Calendar view for the schedule, and a Board/List view where each agenda line converts directly into an assignable task carrying due dates — i.e., notes and action items are not separate systems, the notes *are* the task source. This matches your rolling 4-week recurring-meeting plan: the ClickUp template pattern of "recurring agenda doc + auto-generated tasks" is designed for exactly this.

**Super Agent caution.** Marketing content (12 workflow examples, agent catalog, "Meetings Manager"/"Team Scheduler"/"Deadline Tracker" agents) is extensive, but independently verified real-world usage reports are sparse as of this research pass — most search results are ClickUp's own blog/product pages or SEO-review sites paraphrasing them. The one independent complaint found (inconsistent day-to-day output format, unprompted) is a signal to build your Meetings Super Agent with tight, explicit instructions and to spot-check its output regularly rather than assuming stability.

**Workspace architecture consensus.** Multiple independent sources (ClickUp's own onboarding docs, a paid consultant's 2026 guide, and general help docs) converge on the same shape for a small-to-mid team: few Spaces by function, Folders as the real organizing unit (per client/initiative/here: per meeting series or program), Lists for the actual work, and a lean custom-field set. This argues against a Space-per-something-granular structure for Sŏn and toward: a small number of Spaces (e.g., Meetings, Founding Punch List, Ops) with Folders underneath for structure/classification.

**Granola + Notetaker split.** This is a genuinely common combination in the wild — Granola for its no-bot, private capture (good in person and on the phone, where a bot can't join anyway), paired with a project-management tool's own bot-based notetaker for remote/video meetings where a participant bot is acceptable. Several third-party connectors exist purely to bridge Granola output into task managers, which is worth having as a fallback if ClickUp's own Granola import/sync proves weak.

## Gotchas / limits

- AI Notetaker: 60-minute video cap (audio-only + no live transcript beyond that), English-only, and node quality drop on long meetings — plan meeting lengths or split long sessions accordingly.
- Task-creation-from-notes quality is contingent on ClickUp Brain being active; you already have the AI add-on, but confirm Brain (not just Notetaker) is turned on in workspace settings.
- Super Agent evidence base is weak/early — do not architect the single Meetings Super Agent as a "set and forget" system; build narrow, testable instructions and monitor its first several weeks of real output.
- AI features are a separately licensed add-on layer — verify current seat/plan coverage before assuming all 3 (soon) founders have Super Agent + Notetaker access.
- No confirmed independent Reddit/forum threads specifically on ClickUp Super Agent were found — this space is too new for community consensus; re-check in a few months as more users report in.
- Restaurant-specific external critical-path checklists (RestaurantOwner.com, thehotelblueprint.com) are gated/paywalled — could not verify their phase structure directly; don't cite specific day-counts from them without accessing the paid document.

## Implications for Sŏn

- Build the Meetings space as: recurring meeting Doc/agenda + auto-generated action-item tasks, not a separate "notes" and "tasks" system — mirrors the template pattern that's proven out.
- Keep Granola for in-person/phone (already planned) and ClickUp AI Notetaker for remote by default; watch meeting length against the 60-minute cap, and check whether Brain is enabled workspace-wide for task extraction to work well.
- Scope the single Meetings Super Agent tightly (create/cancel/reschedule only, explicit trigger conditions) and manually verify its output for the first month rather than trusting it as autonomous — evidence suggests inconsistency is a live risk.
- For the workspace restructure: favor few Spaces (function-level: e.g., Meetings, Founding Punch List, Operations) with Folders doing the real classification work, keep custom fields lean (Owner, Classification, Priority/Status — avoid field sprawl), and use Custom Task Types (e.g., "Meeting," "Action Item") within shared Lists rather than fragmenting into many Lists.
- Reserve Teams/user groups for stable long-term groupings (Founders now, All Staff later) rather than creating a Team per meeting type or per short-lived initiative; use filtered views instead for that granularity.
- Use ClickUp's restaurant-specific templates (Project Plan, Charter, WBS) as the skeleton for the Founding Punch List's permit/buildout/hiring/menu R&D/investor tracks, then layer your own critical-path dates rather than sourcing an unverified external day-count checklist.

## Sources

- [ClickUp Recurring Meeting Agenda Template](https://clickup.com/templates/meeting-agenda/recurring-meetings)
- [ClickUp Client Meeting Notes Templates](https://clickup.com/blog/client-meeting-notes-templates/)
- [Stackset: Free ClickUp Template for Team Meeting Management](https://stackset.com/blog/free-clickup-template-team-meeting-management)
- [Vellum: 10 Best ClickUp AI Super Agents Alternatives (2026)](https://www.vellum.ai/blog/best-clickup-ai-super-agents-alternatives)
- [ClickUp: AI Super Agent Workflow Examples](https://clickup.com/blog/super-agent-workflow-examples/)
- [ClickUp Feedback: AI Super Agents](https://feedback.clickup.com/ai-super-agents)
- [ClickUp Meeting Scheduler AI Agent](https://clickup.com/p/ai-agents/meeting-scheduler)
- [consultevo.com: Manage Teams in ClickUp](https://consultevo.com/clickup-manage-teams-guide/)
- [Velox Consulting: How to Set Up ClickUp for a 20-Person Team (May 25, 2026)](https://velox.consulting/blog/how-to-set-up-clickup-for-a-20-person-team)
- [ClickUp Help: Set up your team's Workspace from scratch](https://help.clickup.com/hc/en-us/articles/10636005013271-Set-up-your-team-s-Workspace-from-scratch)
- [ClickUp Help: Custom task types](https://help.clickup.com/hc/en-us/articles/17564381376919-Custom-task-types)
- [ClickUp Help: Create Custom Fields by task type](https://help.clickup.com/hc/en-us/articles/30974227164311-Create-Custom-Fields-by-task-type)
- [Votars: ClickUp AI Notetaker Review](https://votars.ai/en/blog/clickup-ai-notetaker-review/)
- [Jamie: ClickUp AI Note Taker Review](https://www.meetjamie.ai/blog/clickup-ai-note-taker-review)
- [ClickUp Feedback: AI Notetaker recordings longer than 60 minutes](https://feedback.clickup.com/feature-requests/p/ai-notetaker-recordings-longer-than-60-minutes)
- [summarizemeeting.com: ClickUp Review 2026](https://summarizemeeting.com/en/app-reviews/clickup)
- [zackproser.com: Granola review, 12 months in](https://zackproser.com/granola)
- [usecarly.com: 12 Granola Alternatives](https://www.usecarly.com/blog/granola-alternatives/)
- [ClickUp Restaurant Project Plan Template](https://clickup.com/templates/project-plan/restaurant)
- [ClickUp Restaurant Project Charter Template](https://clickup.com/templates/project-charter/restaurant)
- [ClickUp Restaurant Work Breakdown Structure Template](https://clickup.com/templates/work-breakdown-structure/restaurant)
- [thehotelblueprint.com: Restaurant Pre-Opening Critical Path Checklist (landing page only, gated)](https://thehotelblueprint.com/document/restaurant-pre-opening-critical-path-checklist/)
