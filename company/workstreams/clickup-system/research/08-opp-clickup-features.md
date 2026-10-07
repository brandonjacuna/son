# Opportunity Sweep — ClickUp features Brandon hasn't named

Prepared 2026-09-16. Scope: features not already part of the named build (Meetings, Punch List, Owner/Classification fields). Sŏn is on **Business plan + AI add-on** (tier unconfirmed: Brain AI vs Everything AI — open item since Phase 1), 2 founders + 1 pending, pre-opening, no construction/lease yet. Read-only sweep; nothing in ClickUp was touched.

Confidence key: **CONFIRMED** (vendor doc/help article or consistent multi-source) · **UNCERTAIN** (single source, inferred, or conflicting).

---

## 1. Dashboards

**What it is:** Widget-based reporting surface — pull data from tasks/custom fields across spaces into charts, counters, and calculated views. **Unlimited dashboards on Business plan.** CONFIRMED — [ClickUp Dashboards feature](https://clickup.com/features/dashboards); Business plan feature list ([eesel AI pricing breakdown](https://www.eesel.ai/blog/clickup-pricing), [usecarly pricing](https://www.usecarly.com/blog/clickup-pricing/)).

**Sŏn use case:** A single "Fundraising & Runway" dashboard pulling from the Investors view (pipeline stage, amount committed, follow-up due) plus a Critical Path widget for the Real Estate/Buildout classification once dependencies exist (see §5). This is exactly the "Metrics section: fundraising pipeline only, for now" decision already in DECISIONS.md — a Dashboard is the native mechanism for it, not a separate build.

**Effort:** Low — no field creation beyond what's already planned (Classification, Owner); a founder builds it in the UI in under an hour once the Investors view has stage/amount fields. **[You]** UI-only (no MCP dashboard-create tool per the Phase 1 audit).

**Credit cost:** None — dashboards are native reporting, not an AI feature, unless an "AI Dashboard summary" widget is added (uncounted separately; treat as optional).

**When:** **Now** — it's cheap, it directly serves the approved "fundraising pipeline" metrics decision, and it doesn't depend on construction or lease.

---

## 2. Forms

**What it is:** A public or internal form that creates a task on submission, with conditional fields and configurable routing. Included on Business plan (form view is a standard List view type). CONFIRMED — [ClickUp Forms feature](https://clickup.com/features/forms); [Form-based intake overview](https://clickup.com/learn/topic/operations/tools/features/intake-forms/).

**Sŏn use case:** Two concrete forms, both low-effort:
- **Vendor/vendor-lead intake** — replaces the current pattern of vendor leads buried as third-level subtasks under Events → Sponsors (a known problem in the Phase 1 digest, §"What is broken"). A public form feeds a flat Vendors list with Solution/Category fields already modeled in the SaaS Map.
- **Candidate/staffing intake** (pre-hire, once staffing starts) — captures name, role, resume link, referral source directly into a People-space list instead of email threads.

ClickUp ships a **Vendor Application Form Template** ([clickup.com/templates/form/vendor-application](https://clickup.com/templates/form/vendor-application)) that's a reasonable starting point.

**Effort:** Low-medium — building the form and its destination list/fields is a 1–2 hour UI task; **[You]** (no MCP form-create tool).

**Credit cost:** None unless AI auto-routing/categorization is turned on (mentioned as an option — [ClickUp Brain form routing](https://clickup.com/blog/form-view/)); skip that for now per the "AI on per-use-case" constraint.

**When:** **Now** for vendor intake (Events space is active and messy today); **at construction/opening** for candidate intake once hiring actually starts.

---

## 3. Goals / Targets

**What it is:** Objectives ("Goals") broken into measurable "Targets" — four types: number, task-based, currency, true/false. CONFIRMED — [ClickUp Goals help](https://help.clickup.com/hc/en-us/articles/6325733579671-Create-a-Goal); [Goals feature page](https://clickup.com/features/goals).

**Sŏn use case:** A currency-type Target for the fundraising round ("$X raised of $Y goal") and a true/false or number-based Target set for pre-opening milestones (lease signed, permits filed, GC selected). This is a lighter-weight alternative or companion to the Dashboard in §1 — Goals give a single progress bar founders can put front-and-center, while Dashboards give the detail view.

**Effort:** Low — a handful of Targets, 30 minutes. **[You]** UI (Goals aren't in the audited MCP toolset).

**Credit cost:** None (native, non-AI).

**When:** **Now**, but only after the fundraising pipeline has real stage/amount data in the Investors view — otherwise it's another empty scaffold like the Capture lists the audit flagged. Low priority relative to Dashboards; consider skipping until the Investors view is populated.

---

## 4. Relationships + Rollups (lightweight investor/vendor CRM)

**What it is:** A custom field type linking tasks across Lists (many-to-many), with optional rollup fields that pull data (sum/average/count) from the linked list onto the parent task. CONFIRMED — [Custom Relationships help](https://help.clickup.com/hc/en-us/articles/6309153663639-Custom-Relationships); [Rollup fields help](https://help.clickup.com/hc/en-us/articles/11816472778775-Add-rollup-fields-to-List-view); community tutorial confirms the CRM pattern — [ProcessDriven: Build a ClickUp CRM](https://processdriven.co/hub/build-a-clickup-crm-relationships-rollups-use-case-tutorial).

**Sŏn use case:** An **Investors** list (one task per investor/lender: contact, stage, last touch) related to **Meeting** tasks and to **Action Item** tasks — so an investor's task shows a rollup of "meetings held" and "open follow-ups" without re-typing anything. This directly extends the already-approved Investor/Lender meeting template decision (DECISIONS.md: "agent prep brief from the investor's history, link to the investor record"). The Relationship field *is* that link.

**Limitation to flag:** Rollup fields currently only work List-to-List and cannot feed formula fields — [Feature Request: rollup values in formula fields](https://feedback.clickup.com/feature-requests/p/make-rollups-from-relationships-available-for-formula-fields) confirms this gap is still open in the backlog, so don't design around computed rollup-of-rollup fields.

**Effort:** Medium — needs a new Investors list, the Relationship field, and 1-2 rollup fields; **[You]** for field creation (no MCP field-create tool per R8 in the digest), **[Claude]** can draft the field spec.

**Credit cost:** None (native fields, not AI).

**When:** **Now** — this is the mechanical piece the Investor/Lender meeting template already assumes exists ("link to the investor record"). Building it now avoids re-doing the meeting template later.

---

## 5. Dependencies / Gantt / Critical Path

**What it is:** Task-to-task dependency links (waiting-on / blocking), visualized in Gantt view, with an optional Critical Path overlay showing which chain of dependent tasks determines the earliest finish date; available on the free plan and up. CONFIRMED — [ClickUp Gantt help: critical path](https://help.clickup.com/hc/en-us/articles/40982447293207-How-to-use-Gantt-charts-for-project-planning); [Gantt chart feature](https://clickup.com/features/gantt-chart-view).

**Sŏn use case:** Real Estate/Buildout and Fundraising classification tasks in the Founding Punch List have real sequencing today (lease signature blocks permit filing blocks GC mobilization blocks buildout). A Gantt view filtered to those two Classification values, with dependencies set and Critical Path turned on, tells the founders which single task, if late, actually pushes the opening date — versus which delays have slack. This is the single most concrete "when is opening at risk" tool available natively.

**Effort:** Medium — dependencies must be set task-by-task (no bulk API creation confirmed); **[You]** does the linking as tasks are created/reviewed, **[Claude]** can propose the dependency chain from task names/dates for Brandon to confirm.

**Credit cost:** None (native, non-AI).

**When:** **At funding + lease** — dependencies are only worth the setup cost once there's a real lease-signature date and permit timeline to sequence against. Premature now (per DECISIONS.md: "all active tasks live in the Founding Punch List until past funding + lease" — this is exactly the kind of structure that should wait for that same milestone). Flag it now, build it then.

---

## 6. Whiteboards

**What it is:** Freeform visual canvas (mind-mapping, diagramming) with one-click conversion of any object into a task; private whiteboards included on Business plan. CONFIRMED — [Whiteboards guide](https://clickup.com/blog/guide-to-whiteboards-in-clickup/); Business plan whiteboard inclusion ([eesel pricing](https://www.eesel.ai/blog/clickup-pricing)).

**Sŏn use case:** Menu/beverage concept development and floor-plan/vendor-layout brainstorming — both currently undocumented in ClickUp per the Phase 1 digest's open question ("Is menu/beverage development happening outside ClickUp today?"). A Whiteboard is a better fit than a Doc or task list for this kind of nonlinear, spatial ideation, and converts directly into `Idea`-type tasks (a type that already exists in the workspace).

**Effort:** Low — no field/list setup, just opening a canvas. **[You]**/founders directly.

**Credit cost:** None unless "AI-powered templates" (roadmap item, not yet shipped per [ClickUp Whiteboards blog](https://clickup.com/blog/whiteboarding/)) is used.

**When:** **Now**, opportunistically — no dependency on funding or lease, and it's a genuine gap (menu/concept work has no current home). Not urgent; low cost either way.

---

## 7. Clips (screen + voice recording)

**What it is:** In-app screen/voice recording, auto-transcribed by AI, embeddable in Docs/Comments/Chat, with one-click "convert to Task." CONFIRMED — [Clips feature](https://clickup.com/features/clips); [Clip screen recordings help](https://help.clickup.com/hc/en-us/articles/6311242882967-Clip-screen-recordings). Chrome/Firefox only, no mobile — [Clips availability and limits](https://help.clickup.com/hc/en-us/articles/32213057971095-Clips-feature-availability-and-limits).

**Sŏn use case:** Two founders working async (one on-site at the build, one remote) can record a 2-minute walkthrough — a vendor quote comparison, a floor-plan question — instead of writing a long comment or waiting for a sync meeting. More useful once buildout is active (site walkthroughs) than right now.

**Effort:** Low, zero setup — it's a button in the task/comment composer.

**Credit cost:** Voice/video transcription is an AI feature and will draw Super Credits (exact per-clip cost not published; likely priced like other AI Fields, ~10 credits per transcription based on the AI Fields cost data in §9). Confirm actual cost before habitual use, given the AI-on-rollover-credits constraint.

**When:** **At construction** — most valuable for site walkthroughs and vendor-comparison recordings once buildout starts; low priority now.

---

## 8. Chat channels (per-space, currently unused)

**What it is:** Native messaging — channels, DMs, threaded replies, audio/video SyncUps — already provisioned per space (19 channels exist workspace-wide per the Phase 1 audit) but empty. AI in Chat can summarize a channel and has a "Catch Me Up" unread-summary feature. CONFIRMED — [ClickUp Chat review 2026](https://work-management.org/productivity-tools/clickup-chat-review/); Phase 1 audit (`00-workspace.md` §5) confirms 19 channels exist with no messages.

**Sŏn use case:** DECISIONS.md already calls for retiring the per-space Capture channels in favor of one `Inbox` channel plus per-initiative channels (Programming) — this sweep confirms that's the right call rather than trying to revive 13 dead channels. The "Catch Me Up" AI summary feature is worth keeping in mind for the Inbox channel once it's actually used, so a founder returning from a few days off site can catch up in one query instead of scrolling.

**Effort:** Low — channel consolidation is a UI cleanup task, already decided.

**Credit cost:** "Catch Me Up" and channel-summary AI features draw credits per use; low-frequency for a 2-3 person team so not a real budget risk.

**When:** **Now**, as part of the already-approved channel consolidation (H9) — this section adds no new decision, just confirms it and flags the AI summary feature as a future nicety, not a build requirement.

---

## 9. AI Fields & Autopilot (Super) Agents — credit-cost detail

**What it is:** AI Fields are per-task custom fields computed by AI (e.g., auto-summarize, auto-classify) — roughly **10 Super Credits per use**. Autopilot/Super Agents run multi-step workflows and cost **roughly 100–300 credits per invocation** depending on complexity. Brain AI tier = 1,500 credits/seat/month; Everything AI = 5,000 credits/seat/month, plus Everything AI unlocks AI Fields, AI-driven automations/dashboards, and 3x Super Agent usage vs Brain AI. CONFIRMED — [ClickUp AI/Brain guide, ZenPilot](https://www.zenpilot.com/clickup-ai/); [ClickUp AI credits explainer, usecarly](https://www.usecarly.com/blog/clickup-ai/); pricing mechanics ([ClickUp Super Credits pricing model help](https://help.clickup.com/hc/en-us/articles/37837088720151-Super-Credits-pricing-model)). UNCERTAIN which tier (Brain AI vs Everything AI) Sŏn actually has — this was already an open verification item in STATE.md/digest R3 and this sweep did not resolve it.

**Sŏn use case / why it matters now:** This is math, not a feature to adopt — it's the budget backdrop for every other AI-touching recommendation in this brief (Forms auto-routing, Clips transcription, Chat summaries, the Meetings Routine). At 10 credits/AI-field-use and 100–300/agent-run, a single weekly Autopilot Agent doing the meeting roll-forward could burn 400–1,200 credits/month on its own — a meaningful bite of a 1,500-credit Brain AI allowance for 2-3 seats. **Recommendation: confirm the AI tier in Settings → Billing (still open from Phase 1) before turning on any AI Field or Autopilot Agent**, and budget Everything AI once the 3rd partner joins, consistent with existing risk R3.

**Effort:** N/A (verification only, not a build).

**When:** **Now** — verify before Phase 3b blueprint locks in any AI-dependent design (Meetings Routine, form auto-routing, Clips transcription), since the credit math changes the recommended design if the tier is Brain AI, not Everything AI.

---

## 10. Templates center

**What it is:** ClickUp's public template library, including restaurant-specific ones: Restaurant Project Plan, Restaurant Project Charter, Restaurant SOP, Restaurant Business Plan, Vendor Application Form. CONFIRMED — [ClickUp restaurant templates](https://clickup.com/blog/restaurant-business-plan-templates/); [Restaurant SOP Template](https://clickup.com/templates/sop/restaurants); [Restaurant Project Charter](https://clickup.com/templates/project-charter/restaurant). No single "restaurant pre-opening" template found by that exact name — closest fit is the **Restaurant Project Plan Template**, which the vendor describes as covering hiring, licensing, vendor coordination, and pre-opening marketing phases.

**Sŏn use case:** Rather than a wholesale import (the workspace already has too much unused scaffolding per the Phase 1 diagnosis — "template-first, work-second" is explicitly named as the core structural smell), mine the **Restaurant SOP Template** and **Restaurant Project Charter Template** for section headings/checklists to backfill known gaps — e.g., the FDN.xx training modules in People, or SOP content once buildout nears. Do not clone a template wholesale into a live space.

**Effort:** Low — read-through and selective copy, not a structural change.

**Credit cost:** None.

**When:** **At construction/opening** for the SOP template (SOPs matter once there's staff and a working kitchen); low priority now given the anti-template-scaffolding lesson already learned.

---

## 11. Email-in (create tasks via email)

**What it is:** Every List/Space has an auto-generated email address; forwarding or sending to it creates a task (subject → task name, body → description, attachments carried over). Available on every plan, including free. Also a Gmail Chrome extension and Outlook add-in for attaching emails to existing tasks. CONFIRMED — [Create tasks and comments via email](https://help.clickup.com/hc/en-us/articles/6309707288599-Create-tasks-and-comments-via-email); [Gmail Chrome extension](https://help.clickup.com/hc/en-us/articles/6304865820951-Create-tasks-with-the-Gmail-Chrome-extension).

**Sŏn use case:** Vendor/broker emails (real estate, contractors, SaaS vendors) land directly as tasks in the relevant Capture list or the new Vendors list (§2) without manual re-typing — a founder just forwards the email. Complements the Forms-based vendor intake in §2 for cases where the vendor emails first rather than filling a form.

**Effort:** Very low — the email address already exists per list; someone just needs to know and use it. Could be documented in a short README/Doc.

**Credit cost:** None (native, non-AI).

**When:** **Now** — zero setup cost, directly reduces the "vendor leads buried as subtasks" problem already flagged.

---

## 12. Reminders

**What it is:** Personal, non-task reminders (not visible to teammates by default) tied to a date/time, separate from task due dates. Read-only note: the audit already flagged Dominic's reminders as an unverified gap ("Dominic's reminders and private items — own-user scope only").

**Sŏn use case:** Low-value for a 2-3 person founder team where almost everything should be a shared, assigned task rather than a private reminder — using Reminders instead of tasks would recreate the "meaning in prose, not fields" and "no visibility" problems the digest already flags. Not recommending adoption; flagging only because it was named in the sweep brief.

**Effort:** N/A.

**When:** **Skip** — task-based tracking (Punch List) is the better fit for a team this size; reminders add a private, unauditable parallel channel that works against the transparency goals already set (Owner field, shared views).

---

## 13. Brain MAX desktop app

**What it is:** A native (non-Electron) desktop companion — universal search across ClickUp + connected apps (Google Drive, Gmail, Slack, GitHub, Google Calendar, Figma), "Talk to Text" voice dictation, and multi-model access (GPT, Claude, Gemini, DeepSeek) from one sidebar. Free at $0 extra if already on an AI tier; unlimited Talk to Text requires Everything AI ($28/user/month.) CONFIRMED — [Brain MAX desktop app help](https://help.clickup.com/hc/en-us/articles/33292791578263-What-is-the-Brain-MAX-desktop-app); [Brain MAX review](https://dupple.com/tools/clickup-brain-max).

**Sŏn use case:** Talk-to-Text is the most concrete fit — a founder walking a construction site or driving between vendor meetings can dictate notes that land as text in a ClickUp task or a Doc without typing. Universal search (across Gmail + Drive + ClickUp) also directly reduces the "which tool has this file" friction typical of a scattered pre-opening build.

**Effort:** Low — install per founder, no workspace-level setup.

**Credit cost:** Talk-to-Text is unlimited only on Everything AI; on Brain AI it likely draws from the shared credit pool per use (unconfirmed exact rate). Revisit once the AI tier question (§9) is resolved.

**When:** **Now**, opportunistically for whichever founder is most often out of the office/on-site — cheap to try, easy to drop if unused. Not a structural dependency for anything else in the blueprint.

---

## 14. Google Drive / Gmail / Box integrations

**What it is:** Native Google Drive attach-to-task/Doc integration (unlimited on paid plans); native Box file attachment; Gmail via Chrome extension (task creation, email-to-task) or Zapier for deeper automation. CONFIRMED — [Google Drive integration help](https://help.clickup.com/hc/en-us/articles/14841781940759-Google-Drive-integration); [ClickUp integrations page](https://clickup.com/integrations).

**Sŏn use case:** The workspace already runs on Google Workspace — attaching Drive files (lease drafts, financial models, vendor contracts) directly to the relevant Punch List task instead of pasting links in descriptions closes the "meaning in prose, not fields" gap the digest flags for document references. Box is lower priority — only relevant if Sŏn is actually storing files there (unconfirmed; not mentioned elsewhere in the audit, so likely not in active use).

**Effort:** Very low — the Drive integration is a one-time OAuth connect per user; attaching files is then a normal task action.

**Credit cost:** None (native, non-AI).

**When:** **Now** — no dependency on funding/lease, directly usable today for the fundraising and lease documents already in flight.

---

## Summary table

| Feature | Effort | Credit cost | When |
|---|---|---|---|
| Dashboards | Low | None | Now |
| Forms (vendor intake) | Low-Med | None (skip AI routing) | Now |
| Forms (candidate intake) | Low-Med | None | At opening |
| Goals/Targets | Low | None | Now, after Investors view has data |
| Relationships + Rollups (Investor CRM) | Medium | None | Now |
| Dependencies/Gantt/Critical Path | Medium | None | At funding + lease |
| Whiteboards | Low | None | Now, opportunistic |
| Clips | Low | AI transcription draws credits | At construction |
| Chat channels | Low | Minor (summary features) | Now (already decided, H9) |
| AI Fields/Autopilot Agents | N/A (verify tier) | 10/use field; 100–300/run agent | Now — verify tier first |
| Templates center | Low | None | At construction/opening |
| Email-in | Very low | None | Now |
| Reminders | N/A | None | Skip |
| Brain MAX desktop | Low | Uncertain on Brain AI tier | Now, opportunistic |
| Google Drive/Gmail/Box | Very low | None | Now |

## Open items for triage with Brandon

1. AI tier (Brain AI vs Everything AI) is still unconfirmed — resolve before costing out any of the AI-touching items above (§9, Clips, Brain MAX Talk-to-Text, Forms auto-routing).
2. Relationships/Rollups (§4) should be decided alongside the already-open "Investors record" design question from the Meetings/Investor template decision — they're the same piece of work.
3. Dashboards (§1) and Goals (§3) both serve the approved "fundraising pipeline" metric — recommend Dashboards as primary, Goals as a lightweight companion, not both built out in full.
