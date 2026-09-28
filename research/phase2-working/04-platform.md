<!-- Phase 2 working output, run wf_c7d3565a-a0f, 2026-09-28. Raw agent return, not reviewed line by line. The synthesis is research/starting-structure-2026-09.md. -->

# Trainual capability research for Brandon's model (skill tree, conversational gates, self-scheduling)

Researched 2026-09-28. Status key: **VP** is verified-primary (Trainual's own help center or product docs, read directly). **VS** is verified-secondary. **LO** is lead-only (marketing, blog, or a search summary not confirmed on the page). **UV** is unverified.

## Sŏn canon located in Box (for citation only, not read or restated here)

- **White paper, in 00. Pitch Materials** (folder `388972799337`), subfolder White Paper (`382453064958`). It holds one file: **"Sŏn Investor White Paper Sept 2026.pdf", file `2466517057642`** (modified 2026-09-14). A separate "03. Sŏn Investor Diligence White Paper .pdf" also exists as `2468627027608` and `2468611194511`, both outside Pitch Materials. Brandon should confirm which one is canonical.
- **Brand Guidelines:** "Brand and Experiential Guidelines PDF", **file `2281626080747`**, in `Sŏn / 10. AI Projects / Design` (folder `388972616815`, modified 2026-06-12). Markdown copies named "Son Brand Guidelines v1 (1).md" sit in design-system version folders (`2281555280952` v1.0, `2356714319901` v2, `2356731001214` v2.1). Folder `05. Brand and Creative` (`420132086334`) holds only "Identity and Design Assets".
- **Conflict to resolve:** CLAUDE.md and `canon/pointers.md` name the ClickUp doc `2ky45bmy-15773` as canonical Brand Guidelines. This task allows Box only. `canon/pointers.md` needs Box rows for both files once Brandon names the canonical versions.
- Nothing below restates canon. This question does not need it.

---

## 1. Skill tree and branching progression

| Capability | Finding | Source | Status | Binding |
|---|---|---|---|---|
| Training paths | Admins or managers build a path out of ordered "sets". Sets can be released after a delay or on a scheduled date. Only people with group manager access, Admin+ permission, or direct reports can create paths. | https://help.trainual.com/en/training-paths | VP | `tool.lms.training_path` |
| "Complete in order" | Locks each next assignment until the previous one is done. This is linear sequencing only. There is no branching and no "any two of these unlock X". | same | VP | `tool.lms.sequence_lock` |
| Force order inside a subject | Later topics and tests stay locked until earlier ones are complete. The learner can open the subject but cannot jump ahead to locked items. | https://help.trainual.com/en/articles/5605381-force-order-single-subject-content | VP | `tool.lms.sequence_lock` |
| Group vs individual paths by plan | The lowest tier (Core) gets group-based training only. Pro and above add individual paths. Premium and Enterprise add path templates. | https://trainual.com/pricing | VP (the vendor describing its own plans) | `tool.lms.plan_tier` |
| Role or group assignment | Assignment runs through roles and groups. Zapier and Make can assign or unassign roles and subjects automatically. | https://help.trainual.com/en/articles/1986796-trainual-x-zapier-triggers ; https://apps.make.com/trainual | VP | `tool.lms.role_assignment` |
| Optional or elective content | A subject marked "Not required" becomes optional reference material with **no completion tracking**. | search summary of https://help.trainual.com/en/articles/5575360-manage-subject-content-access | LO (page not read directly) | `tool.lms.elective_mode` |
| Self-discovery | Each subject gets one of three settings. **Discoverable:** anyone can search it and view it immediately. **Request:** people can find it but need approval to view, and the request notifies all Admins. **Private:** only Admins and assignees can see it. Available on all plans. The article does not say whether completion is recorded for content a learner discovered rather than was assigned. | https://help.trainual.com/en/content-discoverability-unassigned-user-access | VP (completion behaviour UV) | `tool.lms.self_enroll`, `workflow.unlock_request_approver` |
| What the learner sees | The Home page shows three lists: to-do, completed, and optional. It also shows overdue and due-soon items, a streak timeline, and rings for completion rate, training time, and tests. The learner can sort the lists. The page describes **no map or tree view**. | https://help.trainual.com/en/articles/8098477-the-home-page | VP | n/a |
| Gamification | Streaks, leaderboards, and achievement notifications. These reward completion volume, not mastery. That cuts against Brandon's "not click-through" intent, so the program should decide deliberately whether to turn them on. | https://help.trainual.com/en/articles/6661672-notifications-list (VP); https://trainual.com/manual/trainual-wrapped-2025-the-product-features-and-improvements-shaping-more-productive-teams (LO) | VP / LO | `tool.lms.gamification_setting` (`founder.` call) |

**Verdict:** Trainual can hold a skill tree's content and gate its nodes. It cannot show the learner the tree. Branching unlocks have to be built outside Trainual: a completion event triggers automation, and the automation assigns the next subject.

## 2. What records completion and score, and who can record a live gate

| Mechanism | Records | Who records | Source | Status | Binding |
|---|---|---|---|---|---|
| Native tests: single-select, multi-select, true or false, written response, video response | Pass or fail against a pass mark. Written responses **cannot be auto-graded**. With no minimum word count set, a written answer is automatically marked correct. The docs say nothing about how video responses are graded. | Learner submits. A manager reviews results under Reports. | https://help.trainual.com/en/articles/4109343-choosing-test-question-types ; https://help.trainual.com/en/articles/5607765-view-test-results | VP (video grading UV) | `tool.lms.test_config` |
| SCORM 1.2 and 2004 | Completion is documented. **Recording of score and pass or fail is not documented.** The package cannot be edited in Trainual, so every change means a re-upload. Per-file size cap and plan-gated storage. | The package itself | https://help.trainual.com/en/scorm-uploads | VP (score display UV; confirm in the capability tour) | `tool.lms.scorm_score_display` |
| E-signature | Applies at document level only. The **assignee** signs ("Sign and complete"). Nothing lets a manager sign for a learner. Copies go to the learner's manager, the content owner, or Billing Admins. Pro has an annual cap. Premium and Enterprise are unlimited. The e-signature article says "unlimited" without naming a tier. | Learner | https://help.trainual.com/en/e-signature ; https://trainual.com/pricing | VP | `tool.lms.esign` |
| Admin override: mark complete | Admin+ can mark subjects, topics, and tests complete for a person or a group. **E-signed items cannot be marked complete this way.** The docs do not say whether the record shows who marked it. | Admin+ only | https://help.trainual.com/en/articles/6428685-update-completion-percentages | VP (attribution UV) | `tool.lms.manual_complete` |
| Checklists | Self-completed only. | Learner | adapters/trainual.md (2026-09-26); no current help article found | VS (repo) | n/a |
| Observer or skill-verification checklist | **No such feature was found in Trainual.** A search summary credited Trainual with "observation checklists". Trainual's own comparison page gives that feature to **iSpring**, not Trainual. | https://trainual.com/manual/trainual-vs-ispring | VP (as a negative) | n/a |
| Performance suite: recognition and feedback, reviews | Marketed as praise, feedback, and review cycles. Recognition and feedback is listed as "coming soon". No help documentation on recording a competency pass. | https://trainual.com/ | LO | `tool.lms.performance_suite` |

**Can a live conversational check or practical be recorded as passed, and by whom?** Not natively, in a way that names the assessor. Options, each a `founder.gate_record_system` call:
- **(a) Admin+ marks the gate topic complete.** Only Admin+ can do it, so an hourly positional lead cannot record it without being given Admin+ rights. Brandon flagged using leads as managers as a compliance risk, so this belongs with the HR seats.
- **(b) Assign an attestation document to the assessor.** The assessor e-signs "I observed X meet criterion". This is an inference, not documented. The record lands on the **assessor's** profile, not the learner's. Unverified.
- **(c) External form,** for example a ClickUp Form (`tool.forms.gate_record`). It holds the record. Zapier then assigns the next Trainual subject, and an Admin marks the gate complete.
- **(d) Video response plus manual review.** Grading behaviour is unverified.

**Correction to `adapters/trainual.md`:** its line "e-signature can record an assessor's sign-off" is contradicted by the primary docs, because only the assignee signs.

## 3. Triggers, notifications, webhooks, and APIs on completion

| Capability | Finding | Source | Status | Binding |
|---|---|---|---|---|
| Zapier triggers | Subject Completed, Topic Completed, All Subjects Completed, Test Passed, Test Failed. | https://help.trainual.com/en/articles/1986796-trainual-x-zapier-triggers | VP | `tool.lms.completion_trigger` |
| Zapier actions | Assign or unassign roles, assign or unassign subjects, invite user. This is enough to build "complete A, then assign B" for branching unlocks. | same; https://zapier.com/apps/trainual/integrations/trainual/24372/assign-trainual-subject-when-another-trainual-subject-is-completed | VP | `workflow.unlock_rule` |
| Make | Actions only (assign, get, list, "Make an API Call"). **No triggers listed.** | https://apps.make.com/trainual | VS | `tool.automation.platform` |
| Native webhooks | Set up under Account > Developer, HTTPS only, with a signing secret. Events are chosen from a list, but the help page does not list them. A per-account webhook cap applies. | https://help.trainual.com/en/articles/5953050-trainual-api | VP (event list UV) | `tool.lms.webhook_events` |
| API | Reads users, groups, assignments, completions, and content. Writes assignments and users. **Cannot create or edit content** ("on our roadmap"). Operations-suite-only subscriptions lose the assignments, completions, and content endpoints. | https://help.trainual.com/en/trainuals-api-and-webhooks | VP | `tool.lms.api` |
| **Plan conflict** | The help center and the 2026-07-14 product update say API, webhooks, and MCP come with **Premium and Enterprise**. The pricing page lists "API access & custom integration support" under **Enterprise only**. Confirm with sales before relying on either. | https://trainual.com/product-updates/connect-trainual-integrations ; https://trainual.com/pricing | VP (conflicting) | `tool.lms.plan_tier` |
| Native notifications | Assignments, requests, comments, mentions, updates, reminders, nudges (with a CC to the manager), and gamification. Sent by email, the mobile app, Slack, or a daily round-up. **No native calendar or scheduling action.** | https://help.trainual.com/en/articles/6661672-notifications-list | VP | `tool.lms.notifications` |

**Implication:** a Test Passed or Subject Completed event can start an automation that books a practical or an unblock conversation. That needs Zapier on any plan, or native webhooks on Premium or Enterprise per the help center. Trainual cannot schedule anything itself.

## 4. Self-scheduling onto managers' standing talent blocks (binding candidates, not decisions)

| Tool | What it can do for this | Source | Status | Binding |
|---|---|---|---|---|
| Calendly: event type limited to block hours, round robin or collective pools | Availability can be restricted to the talent-block windows. Pooling type exposes round robin across leaders. Single-use links can be generated through the API, and unused links expire. | https://developer.calendly.com/api-docs/4b8195084e287-create-single-use-scheduling-link ; https://developer.calendly.com/how-to-get-scheduling-page-links-for-team-members-across-the-organization | VP | `tool.scheduling.platform`, `tool.scheduling.talent_block_event` |
| Calendly Scheduling API | `POST /invitees` books directly with no Calendly UI, and `GET /event_type_available_times` returns open slots. Needs a paid plan. Round robin and collective support is not addressed. | https://developer.calendly.com/docs/api-guides/schedule-events-with-ai-agents | VP (pooling UV) | `tool.scheduling.auto_book` |
| Google Calendar appointment schedules | A booking page per person that respects real-time availability, with buffers and a scheduling window. No booking API was found. | https://support.google.com/calendar/answer/10729749 | VP (API absence UV) | `tool.scheduling.platform` |
| Microsoft Bookings | The Graph API creates appointments for **shared** booking businesses only, not personal pages. | https://learn.microsoft.com/en-us/graph/api/resources/booking-api-overview?view=graph-rest-1.0 | VP | `tool.scheduling.platform` |
| 7shifts | Zapier triggers cover schedule published, time punches, users, and payroll. Searches cover shifts and reports. **No booking, event, or task creation.** It fits reading shift context, not booking conversations. | https://zapier.com/apps/7shifts/integrations | VS | `tool.scheduling.shift_system` |

**Chain options** (`workflow.gate_autoschedule`):
- **(A) Learner books.** Test Passed → Zapier → Calendly single-use link for the talent-block event → sent through Trainual-adjacent Slack or email. Moderate friction, because the learner still has to pick a time.
- **(B) Nobody books.** Test Passed → Zapier or webhook → Calendly availability lookup → `POST /invitees` books the first open talent-block slot. The event appears on both calendars. This is closest to "it just appears", and it needs a paid Calendly plan plus custom automation.
- **Open design question for both:** who fills the assessor seat (peer plus manager, per Group 4). This needs `workflow.assessor_pairing`.
- **Unconfirmed names:** the length of the talent block and how many blocks each leader holds are `workflow.talent_block`. Whether leads' calendars count as scheduling them as managers is an HR-seat question.

## 5. Presenting the skill tree alongside Trainual

| Option | Can show | Can record | Notes | Binding |
|---|---|---|---|---|
| Static map page inside Trainual (image or flowchart on a reference subject) | The whole tree, per track | Nothing. As an optional subject it has no completion tracking. | Native flowcharts exist. Updates are manual. | `tool.lms.map_page` |
| SCORM-packaged interactive map | A clickable tree with node descriptions | Completion of the map as one unit. **It cannot read the learner's Trainual progress** because SCORM runs sandboxed per package. It would show a generic tree, not "your" tree. | Built with the repo player or H5P. Every change means a re-upload. | `tool.lms.map_scorm` |
| External live page (iframe embed) reading Trainual completions through the API | A personalized tree: what is unlocked, done, or next | Nothing inside Trainual. It reads completions but writes none. | Needs API access (plan conflict above). Auth and hosting needed. The strongest fit for "presented as much as possible". | `tool.map.external_page`, `tool.lms.api` |
| Printed poster or back-of-house wall map | The whole program at a glance, social visibility | Nothing | Suits pre-shift conversations and "prove it to the team". | `tool.print.program_map` |

## 6. Audio (masterclass recordings)

- **Uploaded audio files show as a hyperlink** that opens and plays in a separate browser tab. There is a per-file size cap. For in-app playback, Trainual suggests hosting on SoundCloud and using Quick Embed. The article says nothing about tracking listening. Source: https://help.trainual.com/en/articles/4112568-upload-audio-files (VP; the article is dated around 2023, so re-check). `tool.lms.audio_hosting`
- **Tracking:** neither route records listening. Two options to confirm in the capability tour:
  - Publish each recording as hosted video (audio over a still image) to use hosted video's required-watch option and auto transcripts (Pro and above). Source: https://trainual.com/pricing (VP). The workaround itself is UV.
  - Wrap the audio in SCORM (UV).
- A completion checkbox is a self-report only. `tool.lms.audio_tracking`
- **Before any masterclass recording ships:** consent from the people recorded is an HR and legal binding, `workflow.recording_consent`.

## 7. Compliance content catalog

- **It exists.** It is the "Premium courses" **add-on**, available on all plans. Source: https://trainual.com/pricing (VP).
- **Category level:** compliance, safety, soft skills, and upskilling, "certified, current". Courses can go into training paths. Marketing lists state-mandated harassment prevention, DEI, OSHA workplace safety, HIPAA, and cybersecurity, with automatic updates, certificates, and recurring due dates. Sources: https://trainual.com/courses ; https://trainual.com/products/premium-courses. The catalog's existence and path linking are VP. The course lists and "certified" claims are LO.
- **No food handler or alcohol-service course was confirmed.** Brandon's plan to run food handler training "inside of Trainual" may therefore need an outside provider. That provider would come in as SCORM, which requires owning the content per https://help.trainual.com/en/scorm-uploads, or as an external link with the certificate uploaded.
- Bindings: `tool.lms.premium_courses`, `tool.compliance.food_handler_provider`, `tool.compliance.alcohol_service_provider`.

## 8. Learner flagging of confusing or outdated content

- **Native:** Pro and above have "content quality feedback". It is available in View mode, where commenting is not. Source: https://trainual.com/pricing ; https://help.trainual.com/en/commenting (VP).
- **How it works:** a one-click flag for outdated or confusing content that notifies the owner and appears in the Home action queue. Source: https://trainual.com/manual/trainual-wrapped-2025-the-product-features-and-improvements-shaping-more-productive-teams (LO). No dedicated help article could be read.
- **Content verification reminders** (all plans) prompt owners to re-verify content on a schedule. Source: https://help.trainual.com/en/articles/8802603-set-content-verification-reminders (VP).
- **Routing to ClickUp:**
  - Feedback is **not** among the Zapier triggers.
  - Whether it is a webhook event is UV.
  - Fallback 1: an embedded ClickUp Form on each subject's closing page. The form creates a review task in ClickUp, but Trainual records nothing. Sources: https://help.trainual.com/en/articles/4112469-embed-a-form (VP); https://help.clickup.com/hc/en-us/articles/6306186099223-Zapier-integration (VP).
  - Fallback 2: a person triages the Trainual action queue into ClickUp.
- Bindings: `tool.lms.content_feedback`, `workflow.flag_to_review_task`, `tool.forms.content_flag`.

---

## Hard constraints the program map must design around

1. **No learner-facing tree.** Trainual shows lists (to-do, completed, optional) and linear locked sequences. The skill tree has to be shown outside it: an external page, a poster, or a static map.
2. **Branching lives in automation.** Unlocks such as "master A, then B and C open" need Zapier (Test Passed or Subject Completed → Assign Subjects) or webhooks plus the API. Native locking only works in a straight line.
3. **Only Admin+ can record a live gate as passed, and attribution is undocumented.** No native assessor or observer sign-off exists. The e-signature is the learner's own. Every conversational practical therefore needs `founder.gate_record_system`, and the HR seats must rule on whether an hourly lead may record gates.
4. **Electives marked "Not required" record nothing.** A tracked elective has to be an assigned required subject, delivered through automation or through Request access, which routes to Admins and not to leaders.
5. **The record is thin.** It holds tests, SCORM completion, and e-signatures, but SCORM score display is unconfirmed and written responses auto-pass unless someone reviews them. The "decisions the way Brandon would" evidence has to come from conversations, logged outside Trainual or through the Admin mark.
6. **No auto-scheduling in Trainual.** It needs a scheduling tool (Calendly's Scheduling API is the only verified book-without-UI route) plus automation. 7shifts cannot book.
7. **Plan tier gates the design.** Individual paths need Pro. E-signatures are capped on Pro and unlimited on Premium. API and webhooks are Premium or Enterprise (help center) or Enterprise only (pricing page), which is unresolved. Premium courses are an add-on.
8. **Content cannot be pushed by API.** Publishing stays manual. SCORM changes mean a re-upload.
9. **Audio is untracked and not inline** unless it is re-hosted as video or SCORM, which is to be confirmed.
10. **Food handler and alcohol service are not confirmed in Trainual's catalog.** Plan on an outside provider.
11. **The content flag stays in Trainual.** Automatic ClickUp review tasks need a form embed or confirmation of a webhook event.
12. **Gamification rewards completion, not mastery.** Enabling it is a `founder.` call.
13. **Run `/refresh-capabilities trainual` and the capability tour** (Box folder `421832819408`) to settle every UV item: SCORM score display, video-response grading, audit trail on Admin marks, webhook event list, completion on discovered content, and audio tracking.

No brand, lineage (Coqodaq, Alinea, Gracious), or chef-gated content was touched.