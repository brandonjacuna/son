# 12 — Opportunity Shortlist & Verification Verdicts (Lead Architect)

_Prepared 2026-09-16 by Fable from research/06–11 plus 00/03/04, STATE.md and DECISIONS.md. Read-only; nothing in ClickUp was touched. Every constraint in STATE.md/DECISIONS.md is respected: Scaling People tasks and the Carryover Register are untouched; department spaces stay as shells; all active tasks stay in the Founding Punch List until past funding + lease; ClickUp AI credit use is kept low and deliberate._

Confidence key: **CONFIRMED** = vendor doc or multiple consistent sources. **UNCERTAIN** = single/secondary source, inferred, or needs an in-app check.

---

## 1. Verification verdicts that change the design

### 1.1 Meetings engine owner — VERDICT: Hybrid, Claude-primary

**Options weighed**

| | A. ClickUp Super Agent + external MCP | B. Claude Cloud Routine | C. Hybrid (Claude engine, ClickUp front-end) |
|---|---|---|---|
| Google Calendar invites (guests + Meet + location) | **UNCERTAIN.** Only "check your schedule" / "External Search" is confirmed for agents. Event create/update/delete is confirmed only for the *Automations* subsystem, not as agent tools. No official Google Calendar MCP exists; community servers need self-hosting + Google OAuth app. | **CONFIRMED** full CRUD incl. guests, Meet links, recurring, RSVP via Anthropic's Google Calendar connector. | Same as B. |
| Granola notes ingest | Granola hosted MCP is OAuth and read-oriented; **UNCERTAIN** anyone has wired it to a Super Agent. | **CONFIRMED** first-party Granola connector (OAuth, Business plan). | Same as B. |
| Reliability (community, 2026) | **CONFIRMED complaints, Jan–Sep 2026:** agents "only hit it 80% of the time", one user burned 4K credits in a week on format drift; ClickUp PM acknowledged and is "actively working on agent reliability". | Runs autonomously, no approval prompts; content fetched mid-run stays untrusted. Headless local scripts have an OAuth bug — Routines avoid it. | Same as B for the engine. |
| Credit / cost | 100–300 Super Credits per run. ~10 meetings/mo × 2 runs (create + notes) = 2,000–6,000 credits/mo against a 1,500 (Brain AI) or 5,000 (Everything AI) per-user pool. Directly violates "keep ClickUp AI credit use low." | Draws on the claude.ai plan's normal usage (Max/Team-premium include scheduled runs up to 50% of weekly limits; Pro pays via usage credits). **UNCERTAIN** Brandon's plan tier. Zero ClickUp credits. | Optional Super Agent front-end costs 0 credits if it only uses Brain chat, 100–300 per run if given tools. |
| Identity | Workspace connection = Brandon as owner/admin. | Routine belongs to Brandon's claude.ai account; invites carry Brandon's Google identity — **matches the standing decision** "Invite organizer is Brandon's Google account." | Same as B. |
| Setup friction | UI-only; quick to try; **UNCERTAIN** whether native calendar tool group appears in "Add tools". | Needs a GitHub repo (even minimal) and account-level connectors on claude.ai; folder is not yet a git repo. | B's setup plus one optional agent. |

**Recommendation**

1. **Claude Cloud Routine (Sonnet 5, weekly custom cron) owns every cross-app write:** the rolling schedule (first run creates 4 occurrences per series; then 1 per week at the 4-week mark; cancellations not backfilled), Google Calendar invites, cancel/reschedule reconciliation, and Granola → shared ClickUp Doc page under the Meeting task. ClickUp stays the system of record.
2. **Invites are created by the Routine through Anthropic's Google Calendar connector as four discrete events, not a Google recurrence** (sidesteps the confirmed "recurring tasks push only the current instance" gap and the prototype's delete-and-recreate-the-series behaviour). Default: Google Meet link, guests = Founders Team members expanded via the ClickUp Groups API, organizer = Brandon. **Store the Google event ID in a custom field, never in the description.**
3. **Location:** resolve the Phase 3 open item as *read, don't own*. Brandon edits location in Google Calendar; the Routine reads the event back on each weekly run and mirrors it onto the task. No ClickUp-side location field is authoritative.
4. **"Tell an agent" to cancel/reschedule** (standing decision) is satisfied two ways: (a) a ClickUp Automation on the Meeting task (status → Cancelled, or due date changed) fires a webhook to the Routine's API trigger with the task ID as the fire payload; (b) ad hoc natural language to Claude (chat or Code) with the same connectors. The saved Routine prompt must explicitly say to act on the fire payload, or it is inert (CONFIRMED).
5. **Optional ClickUp Super Agent = read-only front-end only:** @mention for "what's on Tuesday's agenda / summarize the last standup" using Brain chat (0 credits). Do **not** give it calendar write tools now.
6. **Re-open the Super Agent-as-engine question only if all three hold:** (i) the prototype's or a test agent's "Add tools" panel shows a native Google Calendar *create event with guests* tool (5-minute in-app check, [You]); (ii) Sŏn is on Everything AI; (iii) a 4-week side-by-side test shows ≥95% consistency. Until then the community evidence and the credit math say no.
7. **Capture tool: standardize on Granola for all meeting types** (desktop app on Google Meet for remote; outbound iOS call for the standup; Thursday quality test still stands). One ingest pipeline instead of two, and it avoids the CONFIRMED AI Notetaker trap (notes land in a private Doc visible only to the host). Keep Notetaker as a fallback only, and if it is ever used, the Meeting workflow must include an explicit "share/move the notes Doc into the Meetings space" step.

**Prerequisites this verdict creates (all cheap):** `git init` the `/Users/brandonacuna/ClickUp` folder and push a private GitHub repo (the Routine requires one); confirm Brandon's claude.ai plan tier; add Google Calendar, Granola and ClickUp as account-level connectors on Brandon's claude.ai; confirm which ClickUp MCP server the Routine will use (official 6-tool vs this session's broader server — assume the narrower one).

### 1.2 Other verdicts

| # | Verdict | Effect on the blueprint |
|---|---|---|
| V2 | **Cross-Department field, not Tasks in Multiple Lists** (CONFIRMED: lifetime non-resetting cap; status and fields shared across all lists; Business cap UNCERTAIN). | Build Cross-Department as a Labels field at "Everything" scope. Multi-listing is deferred to post-lease when a task legitimately sits in two live lists. Answers the DECISIONS "alongside or instead" question: instead of, for now. |
| V3 | **Classification as Labels is correct** (CONFIRMED: Labels = multi-select, distinct from Tags). Carved-out view filters must be **inclusion-based** (Investor-Facing OR Real Estate/Buildout), never "exclude Governance". | Scaling People tasks are never edited, so they never carry a label and can never leak into a carved-out view. Digest H3 (single-select dropdown) is closed. |
| V4 | **Edit surface split** (CONFIRMED: field *values* via API; field *creation*, task types, statuses, views are UI or REST-token only). | Two build lanes. **[You]:** task types, status templates, Teams, Super Agent/Automation config, Dashboard. **[Claude]:** lists, tasks, Docs (Markdown tables CONFIRMED via `content_format: text/md`), field values — plus fields and views via REST **if Brandon issues a personal API token** (recommended; saves hours of UI clicking). |
| V5 | **AI tier still unconfirmed** (Brain AI 1,500 vs Everything AI 5,000 credits/user/mo). | Blocks the credit budget for every AI-touching item. Confirm in Settings → Billing before Phase 3b. Nothing in the "Recommend now" list below depends on ClickUp credits. |
| V6 | **Guest billing trap is real** (CONFIRMED mechanism; dollar figures UNCERTAIN). Permission-controlled guests count against 10 + 5/member and can convert to paid seats. | Attorney (Operating Agreement review) and designers get **view-only** by default; check billing after each invite. |
| V7 | **No native full-workspace backup** (CONFIRMED; feature request still "Future"). | Take a baseline CSV export of the Founding Punch List and key Docs **before** the Phase 4 restructure begins; repeat quarterly. |
| V8 | **Fundraising metric surface = Dashboard, not Goals** (both CONFIRMED native, no credits). | One "Fundraising & Runway" Dashboard fed by the Investors view; Goals only later as a single progress bar once pipeline data exists. |
| V9 | **Prototype's calendar tool is still unidentified** (UNCERTAIN). | 5-minute [You] check of the prototype agent's Skills → Add tools panel before it is retired in Phase 4. Whatever the answer, the Routine design above does not depend on it. |

---

## 2. Opportunity shortlist

Scoring: **Value** 1–5 for a 2–3-founder pre-opening team · **Effort** S (<1 hr) / M (half day) / L (multi-day) · **Credits** = ClickUp Super Credits or Claude plan usage · **Timing** Now / Construction (lease signed) / Opening (opening window set) · **Builder** [Claude] / [You]. Items Brandon already named (Meetings system, Punch List views/statuses, Owner, Classification, Cross-Department, Capture-list improvements, SaaS Map Doc, Founders Team, channel consolidation, Operating Agreement tasks, templates) are excluded; where a named decision needed a *mechanism* verdict it sits in §1.

### 2.1 Recommend for blueprint now (10)

| # | Opportunity | Value | Effort | Credits | Timing | Builder | Why now |
|---|---|---|---|---|---|---|---|
| N1 | **Git-init the `/ClickUp` folder + private GitHub repo** (config-as-code: DECISIONS.md diffs, skills, `.mcp.json`) | 5 | S | none | Now | [Claude] after Brandon's OK | Hard prerequisite for the Meetings Routine; gives DECISIONS.md rollback. |
| N2 | **Investor record list + Relationship & Rollup fields** (one task per investor/lender: stage, amount, last touch; rollup of meetings held / open follow-ups) | 5 | M | none | Now | [Claude] list, tasks, spec · [You] field creation (or [Claude] via REST token) | The approved Investor/Lender meeting template already assumes a "link to the investor record." Feeds N3. Records, not action tasks — proposed home: a second list in the Founding Sŏn space (needs Brandon's nod, see §4). |
| N3 | **Fundraising & Runway Dashboard** (pipeline by stage, committed vs target, follow-ups due) | 4 | S | none | Now (after N2 has data) | [You] | Native mechanism for the approved "metrics = fundraising pipeline" decision. |
| N4 | **Access policy bundle:** workspace-wide 2FA, Google SSO for founders only, guests default view-only, billing check after every invite | 4 | S | none | Now | [You] | Attorney/designer invites are imminent; real dollar risk (V6). |
| N5 | **3rd-partner onboarding runbook** (invite as Admin, hard-constraints briefing, Founders Team, Granola Business seat, Docs Home as day-one reading) | 4 | S | none | Now | [Claude] drafts · [You] executes | Partner joins "within weeks." No co-owner role exists on Business; Admin is the fit. |
| N6 | **Docs Home page + persona/compliance separation + naming convention** (one "Sŏn Home" Doc linking every department Doc; move the 25+ Claude persona pages out of the compliance folder; `[Category] - [Topic]` rule) | 4 | M | none | Now | [Claude] Home Doc + convention · [You] moves Docs (no MCP move-doc tool) | Brain answers currently blend prompts with grease-trap compliance; fixes discoverability for the 3rd partner. |
| N7 | **Baseline export before the restructure, then quarterly** (Punch List CSV + key Docs as Markdown/PDF) | 4 | S | none | Now (pre-Phase 4) | [Claude] via API/MCP reads · [You] UI export of Docs | No native backup (V7); the restructure is the riskiest moment. |
| N8 | **Department activation register** (one Doc page per shell: purpose, what it holds now vs Construction vs Opening, activation signal — lifted from research/09) | 4 | S | none | Now | [Claude] | Operationalizes "shells fill in over time" without building scaffolding; gives the founders a trigger list instead of empty lists. |
| N9 | **Investor-update drafting Skill** (`.claude/skills/`, reads the Investor-Facing view + N2 pipeline, drafts only — human sends) | 4 | M | Claude plan usage only | Now | [Claude] | Fundraising is the live workstream; buildable today with this session's tools; becomes shareable once N1 exists. |
| N10 | **Zero-setup intake:** connect Google Drive integration per founder, document each list's email-in address, confirm Brain Connected Search covers Drive | 3 | S | none | Now | [You] connect · [Claude] documents | Lease drafts and financial models attach to tasks instead of living as pasted links; vendor emails become tasks by forwarding. |

### 2.2 Later backlog

| Opportunity | Value | Effort | Credits | Timing | Builder | Trigger / note |
|---|---|---|---|---|---|---|
| Dependencies + Gantt + Critical Path on Real Estate/Buildout and Investor-Facing tasks | 5 | M | none | Construction | [Claude] proposes chain · [You] links | Lease signature gives real dates to sequence against. |
| Vendor registry: flat Vendors list + Vendor Application Form + email-in; flatten Events' 13 sponsor sub-subtasks into it | 4 | M | none (skip AI routing) | Construction | [Claude] list/migration · [You] form | Procurement needs a 4-month lead from lease; idle before then. |
| Property: Buildout list (Concept → Design → Permit → Procure → Build → Commission) + Permits & Licenses tracker | 5 | M | none | Construction | [Claude] · [You] statuses | Activation = lease signed. Confirm Sŏn's jurisdiction first (permit sequence is local). |
| Product: Beverage and Culinary lists with Concept → Costed → Tasted → Finalized, cost field per item | 4 | M | none | Construction | [Claude] · [You] statuses | Activation = kitchen equipment finalized. |
| People: Training Modules list (one task per FDN.xx) + candidate intake form | 4 | M | none | Opening (8 wks out) | [Claude] · [You] form | Activation = firm opening estimate. |
| Hospitality: Service Standards SOP Doc + **Scaling-People → SOP writer Skill** | 4 | M | Claude usage | Construction | [Claude] | Activation = floor plan finalized. Skill drafts only; never touches Scaling People tasks. |
| Promotion: Launch Marketing Plan Doc (PR 6 mo, digital 3 mo, content 2 mo, date 1 mo, media event 2 wks) | 4 | S | none | Opening window set | [Claude] | Correctly empty until a target window exists. |
| BI: Metrics & Dashboard Plan Doc (prime cost + labor first) | 3 | S | none | Opening | [Claude] | Needs POS/scheduling data. |
| Monthly Claude hygiene-audit Skill + ClickUp native stale-task automation as the always-on layer | 3 | M | Claude usage; ClickUp automation free | Now + 1 quarter | [Claude] · [You] automation | Wait until the restructure settles so the audit measures signal, not churn. Test `mcp__scheduled-tasks__*` before a full Routine. |
| Goals/Targets currency bar for the raise | 2 | S | none | After N2 populated | [You] | Companion to N3, not a replacement. |
| Doc tag taxonomy (Workspace Doc tags, small set) | 2 | S | none | After Classification lands | [You] | Separate system from task labels. |
| Templates center mining (Restaurant SOP / Project Plan / WBS) for headings only — never clone wholesale | 3 | S | none | Construction | [Claude] reads · [You] copies | Anti-scaffolding lesson from the audit. |
| Clips (screen/voice) for site walkthroughs | 3 | S | AI transcription credits (UNCERTAIN rate) | Construction | founders | Cost check against tier first. |
| Whiteboard for menu/concept ideation → `Idea` tasks | 2 | S | none | Opportunistic | founders | Only if menu dev is actually happening in ClickUp (digest Q23 unanswered). |
| Brain MAX desktop / Talk-to-Text | 2 | S | unlimited only on Everything AI | Opportunistic | founders | Depends on V5. |
| Notification settings review (unwatch defaults) | 2 | S | none | When Scaling People tasks get owners/dates | [You] | Noise is low today at 2 people. |
| ClickApps audit (disable unused) | 2 | S | none | After restructure | [You] | Not readable via MCP; needs a settings screenshot. |

### 2.3 Skip (one line each)

- **Reminders** — private and unauditable; works against Owner/shared-view transparency.
- **Archive the 6 empty spaces** — conflicts with the binding shells principle (see §4).
- **Tasks in Multiple Lists (now)** — lifetime cap, shared status, and it would surface "active" tasks inside shell spaces.
- **Cowork plugins** — research preview with documented auth flakiness, token burn and a file-deletion incident; Code + Skills covers the same ground read-only.
- **Box connector** — no evidence Sŏn uses Box beyond one "staging for Box" page; revisit if adopted.
- **Bear connector** — no evidence either founder uses Bear; don't add a tool for its own sake.
- **Self-hosted community Google Calendar MCP for a Super Agent** — unofficial, needs hosting + Google OAuth app + rotation; Claude's connector already does it.
- **ClickUp Super Agent as the meetings engine** — UNCERTAIN calendar write, CONFIRMED 2026 reliability complaints, 2,000–6,000 credits/mo (§1.1).
- **AI Notetaker as primary capture** — private-Doc trap; Granola single pipeline instead (fallback only).
- **Zapier Granola → ClickUp** — superseded by the first-party Granola connector; polling fallback only.
- **AI auto-classification of the Classification field** — burns credits and mis-sorts legitimate multi-label cases; populate deliberately.
- **Forms AI auto-routing** — already decided against (flagged inbox, human-confirmed moves).
- **Desktop scheduled tasks for the weekly roll-forward** — skips runs when the laptop sleeps.
- **`Reference` task type / "Operating System Backlog" quarantine list (digest H2/H5)** — Scaling People and the Carryover Register are protected; views filter, nothing moves.
- **Collapse 13 spaces to 6 (digest H1)** — overridden by the architecture principle.

---

## 3. Classification + task type proposal (for approval)

### 3.1 Classification — Labels field, "Everything" scope, 12 values

Multi-select; typical task carries 1–2, max 3. Replaces the retired Project field. Names shortened for column width and to avoid the Structure/Structure collision.

| # | Value | One-line definition |
|---|---|---|
| 1 | **Build / Setup** | Standing something up once — it ends when the thing exists. |
| 2 | **Recurring / Operating** | Repeats on a cadence once live (KTLO). Excludes Build. |
| 3 | **Governance** | How the org is organized and decides — roles, policies, Operating Agreement, org design. (Renamed from "Governance / Structure".) |
| 4 | **Founder Decision** | A judgment call only a founder can make; how Dominic/Attorney-Review items get found. |
| 5 | **Legal / Compliance** | Needs legal review, filing, licensing or regulatory compliance. |
| 6 | **Capital / Budget** | Money commitment, budget tracking, capital stack. |
| 7 | **Investor-Facing** | Anything an investor or lender sees or that tracks them. **Drives the Investors & Fundraising view.** |
| 8 | **Real Estate / Buildout** | Lease, construction, permits for the space, site logistics. **Drives the Real Estate / Buildout view.** |
| 9 | **Vendor / Procurement** | Selecting, contracting or managing an external vendor or SaaS tool. |
| 10 | **Research** | Open-ended investigation; the answer isn't known yet. |
| 11 | **Admin** | Low-stakes account/access/logistics cleanup (the leftover ownership-transfer and Gmail/Airtable tasks). |
| 12 | **Brand / Guest Experience** | What the guest sees and feels — brand system, menu, uniforms, guest-facing design. |

Rules: carved-out views filter **include-if 7 OR 8**; Scaling People tasks are never labeled (never edited) so they stay in the default Action Items view only; the `investor` Tag is retired once value 7 is populated (approval needed, §4); no AI auto-fill.

### 3.2 Task types — workspace-wide, ≤16 characters

| Type | Status | Use |
|---|---|---|
| Task | exists (default) | Anything that doesn't need a specific shape. |
| Meeting | exists | One occurrence or its series parent. |
| Document | exists | A doc-producing task. |
| Idea | exists | Unvetted capture; Capture-list default entry. |
| Deliverable | decided, unbuilt | A concrete artifact to produce. |
| Structure | decided, unbuilt | An org/process structure being defined. |
| Workflow | decided, unbuilt | A repeatable procedure being designed. |
| **Decision** | **new — recommend** | A discrete founder decision point with options (gives Dominic/Attorney-Review items a shape). |
| **Milestone** | **new — recommend (ClickUp native, just enable)** | Dated checkpoint with no deliverable: funding close, lease signed, opening date — the literal gate STATE.md refers to. |
| Action Item | optional — Brandon's call | Would let meeting-origin items keep identity after being moved to a destination space. Not required by the flagged-inbox decision; skip unless Brandon wants meeting-origin reporting. |

Type answers "what shape is this"; Classification answers "what kind of effort". Example: type = Decision + Classification = [Founder Decision, Legal / Compliance].

---

## 4. Conflicts with binding decisions (and clarifications)

| # | Item | Nature | Resolution proposed |
|---|---|---|---|
| C1 | **Archive the 6 empty spaces** (research/11 candidate #8; digest H1 alt) | **Conflict** with "department spaces are shells … never merge or collapse." Archiving hides shells from the sidebar, which defeats their signalling purpose. | Skip. Use N8 (activation register) to make shells legible instead. |
| C2 | **`investor` Tag vs Investor-Facing label** | Two parallel signals will drift. Tags were never decided in DECISIONS.md. | Migrate intent to the label on the ~12 tagged Punch List tasks (none are Scaling People), then stop using the tag. **Needs Brandon's approval.** |
| C3 | **Task type "Structure" vs label "Governance / Structure"** | Naming collision. | Label renamed to **Governance** (§3.1). |
| C4 | **Retired Project field's "Financials" value** | Splits across Capital / Budget and Investor-Facing. | Confirm the split before removing Project. |
| C5 | **Investor record list location** (N2) | "Until past funding + lease, ALL active tasks live in the Founding Punch List. No other space gets action tasks." Investor records are records, not action tasks, but they are tasks. | Place the Investors list in the **Founding Sŏn space** beside the Punch List (same space, no other space gains tasks). Action items about investors stay in the Punch List and link back. **Needs Brandon's nod.** |
| C6 | **"Cancel and reschedule happen by telling an agent"** | Clarification, not conflict: the "agent" becomes the Claude Routine (via Automation webhook or natural language), with an optional read-only ClickUp Super Agent for questions. | Adopt §1.1 wording in the blueprint. |
| C7 | **"Standup capture stays on Granola" + Notetaker for remote meetings (digest #8)** | Simplification: Granola for all meeting types, Notetaker fallback only. | Pending the Thursday Granola quality test. |
| C8 | **"Re-evaluate Claude Routine as orchestrator" (DECISIONS 2026-09-16)** | Re-evaluated in §1.1: Routine stays the engine. | Record the verdict in DECISIONS.md. |
| C9 | **Digest hypotheses H1/H2/H3/H5** (collapse spaces, Reference type, single-select dropdown, quarantine list) | Already superseded by DECISIONS.md. | Mark closed; no action. |
| C10 | **Vendor registry / flattening Events sponsors** | Would add structured tasks to a shell space pre-lease. | Deferred to Construction (§2.2), so no conflict arises now. |

---

## 5. Pre-blueprint checks for Brandon (all in-app, ~30 minutes total)

1. Settings → Billing: **AI tier** (Brain AI vs Everything AI) and seat count for 3 founders. _(V5)_
2. Prototype "Founders Meeting Assistant" → Skills → **Add tools**: is there a native Google Calendar *create event* tool? Screenshot. _(V9, §1.1 step 6)_
3. Decide on issuing a **personal ClickUp API token** so Claude can script fields and views. _(V4)_
4. Confirm **claude.ai plan tier** (Pro/Max/Team) for Routine usage, and add Google Calendar, Granola, ClickUp as account-level connectors. _(§1.1 prerequisites)_
5. Approve **N1 (git init + private GitHub repo)**, **C2 (retire `investor` tag)**, **C5 (Investors list location)**.
6. Thursday **Granola phone-call test** (already scheduled). _(C7)_

---

## Sources (this brief's own checks; the underlying briefs carry their full source lists)

- Super Agents feedback board and "Super Agent Not Ready for Primetime" thread (reliability, credit burn, PM response; Jan–Sep 2026): https://feedback.clickup.com/ai-super-agents · https://feedback.clickup.com/ai-super-agents/p/super-agent-not-ready-for-primetime · https://feedback.clickup.com/ai-super-agents/p/super-agent-credit-allowance
- Brain² changelog (agents "check your schedule"; MCP "read, write, and take action"; no explicit agent event-creation claim): https://feedback.clickup.com/changelog/brain-release-notes-takeover
- ClickUp release notes 4.04–4.07 via Releasebot (MCP servers for Super Agents, Aug 18 2026; hourly agent schedules, May 2026): https://releasebot.io/updates/clickup
- Google Calendar integration and Automations help articles (403 on direct fetch; snippet-level only): https://help.clickup.com/hc/en-us/articles/6336507264663-Google-Calendar-integration · https://help.clickup.com/hc/en-us/articles/29626553900951-Google-Calendar-Automations
- Super Credits consumption: https://help.clickup.com/hc/en-us/articles/37837088720151-How-are-AI-Super-Credits-consumed
- Claude Routines, connectors, Google Calendar CRUD, Granola connector: see research/04-claude-side.md and research/10-opp-claude-ecosystem.md sources.
- Everything else: research/06–11 as cited inline.
