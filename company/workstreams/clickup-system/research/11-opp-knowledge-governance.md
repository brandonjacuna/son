# Opportunity Sweep 11 — Knowledge Architecture & Workspace Governance

Prepared 2026-09-16. Read-only — no ClickUp writes. Sources: ClickUp Help Center (vendor docs), feedback.clickup.com, and third-party/community sources (Reddit reporting via secondary write-ups, since help.clickup.com and reddit.com block direct fetch in this environment — see Coverage gaps). Confidence: **CONFIRMED** = stated directly by ClickUp's own docs/product pages or corroborated by multiple independent sources; **UNCERTAIN** = single source, community-reported, or contradicts another source.

---

## A. Knowledge architecture for Brain

### A1. Doc hierarchy / wiki structure
**CONFIRMED.** ClickUp Docs support parent pages with nested sub-pages, drag-and-drop reordering, and an explicit "Create a wiki" feature that promotes a Doc (and its nested pages) into a workspace-visible wiki with its own permissions layer. Recommended pattern from vendor and consultant guidance: mirror the ClickUp hierarchy (Space → Folder → List) in the Doc's page tree, and create one top-level "Start Here" or Home page per Doc that links out to every major section so the structure is navigable without search.
Sources: [Docs Hub – ClickUp Help](https://help.clickup.com/hc/en-us/articles/14235667017495-Docs-Hub), [Create a wiki – ClickUp Help](https://help.clickup.com/hc/en-us/articles/22082137400471-Create-a-wiki), [ClickUp Docs Guide – UpSys](https://www.upsys-consulting.com/en/blog-en/guide-how-to-use-clickup-docs)

**Applied to Sŏn:** the audit found Docs scattered one folder per space (Operations Documents, Finance Documents, People Notebooks, Tech Documents, etc.) with no cross-linking and a "Claude" folder mixing 25+ AI persona prompts with HVAC/grease-trap compliance content and a page tree unrelated to Sŏn. Candidate fix: one canonical "Sŏn Brain" Doc (or wiki) with a Home page linking every department's Docs, and physically separating persona/prompt content from operational reference content so Brain answers don't blend the two.

### A2. Naming conventions
**CONFIRMED** (consistent across every source). Recommended pattern: `[Category] - [Topic]` or `[System]: [Topic]` prefixes for Docs, "How to [action]" for procedure pages, most-important information first, and the convention itself documented in a pinned SOP so it self-enforces. For tasks: short, intuitive, front-loaded names; avoid embedding IDs or codes in the title (the Sŏn audit found calendar event IDs and session codes buried in task/Doc prose instead of fields — fragile on rename).
Sources: [Label naming conventions – ClickUp](https://clickup.com/p/how-to-create-knowledge-base-for-label-naming-conventions), [Understanding the ClickUp Hierarchy – Stackset](https://stackset.com/blog/understanding-the-clickup-hierarchy), digest R-item on prose-embedded IDs (`00-digest.md` §Structural smells #3)

### A3. Where meeting notes/transcripts live (shared vs. private) — HIGH PRIORITY GAP
**CONFIRMED, and this is a real risk for Sŏn**, not just theory. AI Notetaker output — including the "Personal Notetaker" mode most likely to be used — writes into a **private ClickUp Doc visible only to the meeting host** by default; it is explicitly *not* auto-shared with other attendees, and ClickUp's own feedback board has open requests to "automatically share with all meeting attendees" because this is a known gap. Brain search only surfaces content a given user can already see — so a private Notetaker Doc will not show up in the other founder's Brain answers even though it exists.
Sources: [Use AI Notetaker – ClickUp Help](https://help.clickup.com/hc/en-us/articles/28928137493015-Use-AI-Notetaker-to-take-notes-and-record-meetings), [ClickUp AI Note Taker Review – Jamie](https://www.meetjamie.ai/blog/clickup-ai-note-taker-review), [AI Notetaker feedback board](https://feedback.clickup.com/ai-notetaker)

**Applied to Sŏn:** this directly confirms and sharpens digest risk R9. With only 2-3 founders, an unshared Notetaker Doc is a single point of failure for institutional memory. Recommendation for the Meetings-space design: every Meeting task's workflow step should explicitly move/share the Notetaker Doc into the shared Meetings space (or link it via Relationship) — do not rely on default sharing. For Granola notes specifically (the chosen capture tool per DECISIONS.md), the existing plan to write them into a shared ClickUp Doc under the meeting task already avoids this trap — this finding is a reason to keep that design, not change it.

### A4. Doc templates
**CONFIRMED.** Docs support reusable page templates (duplicate-and-customize pattern); templates themselves can be tagged and organized in a template library. Recommendation: build one template per recurring artifact (meeting agenda — already prototyped; SOP page; investor-update page; vendor-reference page) rather than freeform Docs, so structure stays consistent as the 3rd partner and future staff start writing.
Sources: [Organize templates with tags – ClickUp Help](https://help.clickup.com/hc/en-us/articles/6304004307095-Organize-templates-with-tags), [ClickUp Docs Guide – UpSys](https://www.upsys-consulting.com/en/blog-en/guide-how-to-use-clickup-docs)

### A5. Tagging
**CONFIRMED.** ClickUp has a distinct "Doc tags" feature (separate from task tags) at two scopes: **Workspace Doc tags** (addable by any member, everyone sees them) and **Private Doc tags** (visible only to the tagger). Docs can be filtered by any/all tag combinations. This is a second tagging system from task tags — worth knowing so the eventual Classification taxonomy (DECISIONS.md) isn't assumed to also apply to Docs; Docs need their own (smaller) tag set.
Source: [Doc tags – ClickUp Help](https://help.clickup.com/hc/en-us/articles/6325220185495-Doc-tags)

### A6. Archiving Docs
**CONFIRMED.** Docs Hub has a Bulk Action Toolbar: select multiple Docs to tag, move, duplicate, archive, or delete in one action; archived Docs are hidden from the default view but restorable. Useful for closing out the "(Temporary)" and "staging for Box" pages the audit flagged in the Claude/Tech folder without losing them.
Source: [Manage Docs using the Bulk Action Toolbar – ClickUp Help](https://help.clickup.com/hc/en-us/articles/8037535221783-Manage-Docs-using-the-Bulk-Action-Toolbar)

### A7. Avoiding duplicate sources
**UNCERTAIN / no native dedup tool.** No ClickUp feature detects or merges duplicate Docs; the only native safeguard is that a *duplicated* Doc is auto-titled "(Copy)" so it's visible as a duplicate at creation time — it does not prevent two independently-written Docs covering the same topic (exactly the Function → SaaS Map vendor-name-mismatch problem the audit found, `technology.md`). Best available practice from vendor guidance is procedural, not technical: one Home page linking every canonical Doc, and a single named owner per topic area who is the only one authorized to create a new top-level Doc for that topic.
Sources: [Intro to Docs – ClickUp Help](https://help.clickup.com/hc/en-us/articles/6328174371351-Intro-to-Docs), digest §Technology data quality

---

## B. Workspace governance & hygiene

### B1. Roles/permissions for the 3rd partner
**CONFIRMED.** ClickUp has one Owner (currently Brandon, per the audit — cannot be shared) plus Admin and Member roles, all with identical *default* permissions on Business plan (full edit on public items); Admins additionally manage workspace settings/billing/members. Business Plus and Enterprise add **custom roles** with per-permission editing — not available on the current Business plan. For a 3rd founding partner with equal standing, **Admin** is the closest fit on the current plan (not Member, which by default is functionally similar but is the role ClickUp expects to demote later as the org grows); there is no partner-specific "co-owner" role on Business.
Sources: [Owner, admin, and member-type user roles – ClickUp Help](https://help.clickup.com/hc/en-us/articles/25710132309655-Owner-admin-and-member-type-user-roles), [Default user role permissions – ClickUp Help](https://help.clickup.com/hc/en-us/articles/26603207201431-Default-user-role-permissions)

### B2. Guest access for attorneys/designers/investors/contractors — WITH COST NOTE (HIGH PRIORITY)
**CONFIRMED, with an active billing trap.** ClickUp guest tiers:
- **View-only guest** — free, unlimited.
- **Permission-controlled guest** (comment/edit/full-edit on specific items) — counts against an included allowance that starts at **10 seats on Business** and grows **+5 per additional paid member**; exceeding it, or certain trigger conditions, converts the guest into a **billable "limited member" seat charged at the same rate as a full member**.
- **Conversion triggers reported in the wild:** authenticating via a company email domain alias, using the workspace's SSO, or holding edit/comment/approval permissions. Multiple independently reported cases (a secondary write-up citing Reddit/Capterra/ClickUp's own feedback forum) describe workspace bills **doubling to tripling**, one case going from ~$144/yr to ~$1,200/yr, after guests silently converted.
- Sŏn currently has a 2-person Business plan, so the guest allowance is only 10 seats to begin with (before the 3rd partner adds +5). Attorneys, designers, investors, and contractors who need to *comment or edit* (not just view) should be added deliberately as **view-only** wherever possible, with edit/comment access scoped narrowly and reviewed periodically — not left open-ended.

Sources: [ClickUp's Billing Surprise – Heimin](https://heimin.app/en/blog/clickup-billing-surprise) (secondary source reporting Reddit/Capterra/ClickUp-feedback-forum cases — flagged UNCERTAIN on the specific dollar figures, CONFIRMED on the mechanism), [ClickUp Pricing 2026 – SmartSuite](https://www.smartsuite.com/blog/clickup-pricing), [Guest-type user roles – ClickUp Help](https://help.clickup.com/hc/en-us/articles/6310022323991-Guest-type-user-roles) (title accessible; full body blocked by ClickUp's bot-protection in this environment — see Coverage gaps), [Manage Guest Roles – Consultevo](https://consultevo.com/clickup-guest-user-roles-guide/)

**Recommendation for Sŏn:** before inviting the attorney (Operating Agreement review) or any designer/investor/contractor, decide the permission level explicitly (view-only is the safe default), and check Settings → Billing after any guest invite for the first cycle to confirm it didn't silently convert.

### B3. Notification settings
**CONFIRMED, consultant-sourced consensus (not a single vendor doc).** Recurring recommendations: turn off "auto-watch tasks I'm involved in" for anyone who doesn't want to watch by default; unwatch tasks that don't need ongoing attention (keeps @mentions/assignments only); review notification settings monthly or on role change; use Do Not Disturb during focus blocks. For a 2-3 person team, this matters less at current task volume but will matter fast once the ~330-item Scaling People backlog and Carryover Register are active — un-triaged, they would flood both founders' notification feeds if left un-watched-off.
Sources: [ClickUp Notifications: Setup, Filters & Sanity Tips – UpSys](https://www.upsys-consulting.com/en/blog-en/guide-clickup-notifications), [Stop ClickUp Notification Overwhelm – Ask Yvi](https://askyvi.com/clickup/stop-clickup-notification-overwhelm-in-2025/)

### B4. ClickApps to enable/disable
**CONFIRMED (principle), UNCERTAIN (specific list for Sŏn).** ClickApps are Owner/Admin-toggleable, workspace- or space-scoped feature switches (Sprints, Time Tracking, LineUp, Time Tracking Mandatory, etc.); vendor and consultant guidance agrees on one principle: only enable what the team actually uses, since unused ClickApps add UI clutter and status/field noise. No tool exists to enumerate the full current ClickApp state for Sŏn's workspace (confirmed in `00-workspace.md` — not exposed via MCP), so this needs a manual settings screenshot before deciding what to toggle.
Sources: [Intro to ClickApps – ClickUp Help](https://help.clickup.com/hc/en-us/articles/6304327753111-Intro-to-ClickApps), [ClickApps EXPLAINED – ProcessDriven](https://processdriven.co/79/clickapps-explained-clickup-tutorial-for-workspace-admin-settings/)

### B5. Archive policy
**CONFIRMED.** Archiving (Spaces, Folders, Lists) hides an item from the sidebar but keeps all contents searchable and restorable indefinitely — distinct from Delete, which goes to a 30-day trash then is unrecoverable. Permission: Owners/Admins can archive or delete any Space; Members only ones they created; Guests cannot archive/delete. This directly supports DECISIONS.md's plan to quarantine the ~330-task governance backlog and the 6 empty spaces (BI, Property, Promotion, Personal, Finance, Product) — archiving, not deleting, is the correct native mechanism, and it's Admin-safe for a 3rd partner to do once granted that role.
Sources: [Archive or restore Spaces – ClickUp Help](https://help.clickup.com/hc/en-us/articles/6309342765079-Archive-or-restore-Spaces), [Archive or restore Folders, Subfolders, and Lists – ClickUp Help](https://help.clickup.com/hc/en-us/articles/6308811160599-Archive-or-restore-Folders-Subfolders-and-Lists)

### B6. Naming conventions for tasks/lists
See A2 above — same sources apply to tasks and lists as to Docs. One addition specific to lists/spaces: consultant guidance recommends keeping Space/Folder/List names as short, plain department nouns (which Sŏn's structure already mostly does) and reserving prefixes/codes for task-level naming only, so the top-level hierarchy stays scannable.
Source: [A Beginner's Guide to ClickUp Terminology – MakeUseOf](https://www.makeuseof.com/beginners-guide-clickup-terminology/)

### B7. Onboarding runbook (3rd partner / future hires)
**CONFIRMED (mechanics), UNCERTAIN (no ready-made runbook specific to a founder-tier addition).** Mechanically: Workspace avatar → People → "Invite people," email(s), assign role at invite time. ClickUp publishes free Employee/New-Hire Onboarding templates as a starting point, and community guidance recommends a scoped "First Month" list with the first week fully mapped. No source addresses onboarding a *co-founder* specifically (as opposed to an employee) — for Sŏn this should be a short custom runbook: (1) invite as Admin, (2) walk the Founding Punch List views and hard constraints (Scaling People/Carryover Register off-limits) before they touch anything, (3) add to the Founders Team once created (DECISIONS.md), (4) confirm their Granola Business seat and Google Workspace account, (5) point them at the Brain/Docs Home page (A1) as day-one reading.
Sources: [Invite people to your Workspace – ClickUp Help](https://help.clickup.com/hc/en-us/articles/6310498173079-Invite-people-to-your-Workspace), [Onboarding Checklist Template – ClickUp](https://clickup.com/templates/onboarding-checklist-t-2wpaqd3), [3 Ways to Add Users – Torii](https://www.toriihq.com/articles/how-to-add-user-to-team-clickup)

### B8. Security — 2FA and SSO
**CONFIRMED.** 2FA via authenticator app (TOTP) is available on every plan; 2FA via SMS requires Business plan or above (Sŏn already qualifies). Owners/Admins can force workspace-wide 2FA (Settings → Security & Permissions), with a 3-login grace period before enforcement kicks in for anyone not yet enrolled. SSO: Google SSO is available starting at Business plan (Sŏn qualifies, and founders likely already use Google Workspace for calendar); Microsoft, Okta, and custom SAML SSO require Enterprise — not available to Sŏn on its current plan.
**Recommendation:** enable workspace-wide 2FA now (low cost, 3 founders), and consider Google SSO given the existing Google Workspace dependency (Calendar, Granola auth path) — but note B2's finding that SSO-authenticated guests are one of the reported guest→billable-seat triggers, so don't extend SSO to guest accounts without checking billing impact first.
Sources: [Enable and manage two-factor authentication – ClickUp Help](https://help.clickup.com/hc/en-us/articles/6327741965591-Two-factor-authentication), [Google single sign-on – ClickUp Help](https://help.clickup.com/hc/en-us/articles/6305105918615-Google-single-sign-on), [ClickUp SSO/SAML Guide 2026 – ToolStack](https://toolstackpm.com/tools/clickup/features/sso-saml)

### B9. Backup / export
**CONFIRMED — this is a real gap, not just a nice-to-have to skip.** ClickUp has **no full-workspace backup/restore feature**. What exists: (1) task-data export to CSV from selected Spaces/Folders/Lists (fields, time estimates, comments, attachment links); (2) Docs export individually as PDF/HTML/Markdown — **no bulk Doc export**; (3) the REST API (100 req/min/token) for scripted export. A native full-backup feature request has been open on ClickUp's own feedback board since at least early 2026 and is still tagged "Future" (not started). **Given Sŏn holds legal documents (Operating Agreement drafts) and the entire operating-system build in ClickUp, this is worth a periodic manual export habit** (e.g., quarterly CSV export of the Founding Punch List + individual export of key Docs) rather than assuming ClickUp itself is the backup.
Sources: [How do I export my Workspace's data? – ClickUp Help](https://help.clickup.com/hc/en-us/articles/6310786693015) (title/URL confirmed; body blocked by bot-protection in this environment), [Full export/backup – ClickUp Feedback](https://feedback.clickup.com/feature-requests/p/full-exportbackup), [Export task data – ClickUp Help](https://help.clickup.com/hc/en-us/articles/6310551109527-Export-task-data)

---

## Candidate opportunities for the Fable shortlist (12)

1. **Notetaker/Granola-Doc sharing rule** — bake "move/share the notes Doc into the shared Meetings space" into the Meeting task workflow (A3). High confidence, directly closes digest risk R9.
2. **Brain/Docs Home page** — one canonical linking page so Brain answers stop blending persona prompts with compliance reference content (A1, A7).
3. **Guest-access policy** — default new external collaborators to view-only; a standing check-billing-after-invite habit (B2). High confidence, real dollar risk.
4. **2FA workspace-wide, now** — near-zero cost, 3 founders (B8).
5. **Quarterly manual export habit** for the Punch List + key Docs, given no native backup exists (B9).
6. **3rd-partner onboarding runbook** — 5-step custom version (B7), timed to land before the 3rd partner joins "within weeks" (STATE.md).
7. **Doc tag taxonomy** (separate, smaller, from the task Classification field) (A5) — sequence after Classification is decided (DECISIONS.md H3 still open).
8. **Archive the 6 empty/near-empty spaces** using native Archive (not delete) — mechanically ready now, pending the H1 collapse-vs-archive decision already flagged in the digest.

## Coverage gaps
- `help.clickup.com` and `reddit.com` return HTTP 403 to this session's fetch tool (bot-protection) — all Help Center facts above come from search-result snippets/secondary citations, not the primary page body. Recommend Brandon open the cited help.clickup.com URLs directly (logged in) to confirm wording, especially the guest-seat allowance math (B2) and the export scope (B9), before either is relied on for a cost decision.
- No Reddit thread was fetched directly (blocked); the guest-billing dollar figures are once-removed via a secondary blog citing Reddit/Capterra — treat the mechanism as CONFIRMED, the specific dollar amounts as illustrative/UNCERTAIN.
- ClickApp state and current SSO/2FA settings for Sŏn's actual workspace are not readable via MCP (confirmed in `00-workspace.md`) — B4 and B8 recommendations are generic until Brandon screenshots Settings → Security & Permissions and Settings → ClickApps.
