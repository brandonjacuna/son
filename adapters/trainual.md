# Adapter: Trainual

Researched 2026-09-26 from Trainual's help center, pricing page, and product updates. Trainual changes often. Run `/refresh-capabilities trainual` before relying on anything here for a real render, and update the `verified` column.

## The rule that governs every Trainual render

**Only two things report back to Trainual: native tests and SCORM packages.** Checklists record self-completion. Everything embedded (H5P, Genially, a form, a Synthesia player, a Google Slide) runs inside a page but records nothing. So:

- If the interaction only needs to teach, it can be embedded.
- If it needs a record (completion, score, pass or fail), it must be a native test, a SCORM package, or a live demonstration logged by an assessor.

## Content model

| Trainual level | Studio mapping | Notes | Verified |
|---|---|---|---|
| Subject | A module (or a short run of tightly linked modules) | Subjects sit in the Company, Policies, or Processes area | 2026-09-26 |
| Document | A section of the module, usually one of the five moves | Trainual renamed topics to documents | 2026-09-26 |
| Page | A single screen of content | Formerly steps | 2026-09-26 |
| Test | `assessment.md` knowledge checks | Added inside a subject | 2026-09-26 |
| Training path | A program sequence from `catalog/curriculum-map.md` | Role-based assignment; individual paths on Pro and above | 2026-09-26 |
| Standalone content | Job aids, checklists, flowcharts, SCORM, videos, files that live outside a subject | | 2026-09-26 |

## Native capabilities

| Capability | What it gives the studio | Modalities it serves | Plan note | Verified |
|---|---|---|---|---|
| Tests, five question types: single-select, multiple-select, true or false, written response (optional minimum word count), video response | Tracked retrieval and judgment checks; video response is the strongest native performance evidence | Spaced retrieval, free recall, situational judgment, video teach-back, role-play evidence | All plans | 2026-09-26 |
| Test settings: question order or randomization, question banks (show a subset), pass percentage | Real spaced retrieval with varied items on retake | Spaced retrieval set | All plans | 2026-09-26 |
| Media inside test questions: images, video, links, tables, files, iframes | Perception items: "what is wrong in this photo" as a tracked question | Spot the difference, cue identification | All plans | 2026-09-26 |
| AI-generated tests | Draft item pools fast; always rewrite against the objective | | | 2026-09-26 |
| Checklists: standalone or inside a subject, reorderable, resettable, completion record kept on reset | Repeatable procedures and post-shift prompts | Checklist, post-shift debrief | All plans. Self-completed only. Not an observer sign-off | 2026-09-26 |
| Flowcharts | Branching procedures as a native object | Flowchart walk | Confirm plan | 2026-09-26 |
| SCORM 1.2 and 2004 upload, up to 2 GB per zip, completion tracked, not editable in Trainual (re-upload to change) | The door to every rich interaction: branching scenarios, drag and drop, hotspots, simulations | Any interaction built in the repo player, H5P via Lumi, Synthesia, or an authoring tool | SCORM storage is plan-gated (Pro lists 5 GB) | 2026-09-26 |
| Quick Embed (700+ providers) and generic iframe | Show anything with a share link or embed code | Any `T-embed` modality | All plans | 2026-09-26 |
| In-app video recorder and Loom integration | Record a real team member modeling a skill | Behavior modeling, worked example | | 2026-09-26 |
| Video upload and hosting, auto transcripts, required-watch option | Host real footage; force full viewing where it matters | Behavior modeling | Pro and above | 2026-09-26 |
| Audio upload | Pronunciation of Korean terms and dish names | Flashcards, vocabulary | | 2026-09-26 |
| E-signatures | Acknowledgement records | Policy acknowledgement. Records only the signer's own acknowledgement, not an assessor's sign-off (corrected 2026-09-28) | Pro lists 300 per year | 2026-09-26 |
| Content feedback icon | Learners flag confusing or wrong content | Feeds the Learner Advocate review loop | | 2026-09-26 |
| Verification reminders, completion nudges | Owners re-verify content on a schedule; learners get reminders | Keeps bound content current | | 2026-09-26 |
| Translate content (smart tools) | Second-language support | Learners working in a second language | Confirm quality per module | 2026-09-26 |
| AI assistant and search | Point-of-need answers | Searchable answer. Cannot read SCORM content | | 2026-09-26 |
| Performance suite: praise and feedback, review cycles with custom questions | A possible home for competency sign-offs and review-linked evidence | Observed floor demonstration record | Separate suite; evaluate | 2026-09-26 |
| Operations suite: meetings, goals, scorecards, team updates | Outside the studio's scope; note for the operating system work | | Separate suite | 2026-09-26 |
| API and webhooks | Pull completions and people data; webhook on events | Measurement (Kirkpatrick level 3 joins) | Premium and Enterprise. **Cannot create or edit training content yet** (on Trainual's roadmap) | 2026-09-26 |
| MCP server | Claude can search and retrieve Trainual content | Checking what is live against the repo | **Read only** as documented | 2026-09-26 |

## What this means for publishing

Publishing is a guided manual step today. `/render MOD-ID trainual` produces an `exports/MOD-ID/trainual/` folder with a page-by-page paste guide, test items formatted for entry, SCORM zips, and a checklist of embeds to place. When Trainual opens content creation to the API, add a push step here and keep the source of truth in the repo.

## Recording a floor demonstration

The readiness gate ("no one touches a table until demonstrably ready") is a live, observed performance. Trainual has no native observer checklist. Options, for the Assessment & Competency Designer to choose from:

1. **E-signature (ruled out):** an e-signature is the assignee's own acknowledgement, so it cannot record an assessor's sign-off.
2. **Video response plus rubric:** learner submits a recorded demonstration as a video-response test question; the assessor grades it against the rubric. Good for skills that can be filmed; poor for tempo.
3. **Performance suite review question:** the demonstration outcome becomes a question in a review cycle. Evaluate once the suite is on the account.
4. **Outside Trainual:** a form (embedded) or the scheduling or HR system holds the observation record, and Trainual holds the learning. Decide at bind time.

**Decided 2026-09-28 (`framework/system-design.md` D8): option 4.** An external form records the gate, the rater, and the rubric; automation marks the Trainual subject complete and assigns the next one. The form tool is `tool.forms.gate_record`, bound until chosen. `founder.gate_record_system` resolves to this decision.

## Exercise plan: seeing every option before committing

Before the first real render, build one capability tour so the team has seen each option working, not just read about it. Use the example module in `modules/_example/EX-001-allergy-at-the-table/` as the content.

1. Start a Trainual trial or sandbox account.
2. Build one subject, "Capability tour," containing: a page with a quick-embedded H5P activity; a native test using all five question types, one with an image; a checklist; a flowchart; an uploaded SCORM package built by `python scripts/build_scorm.py modules/_example/EX-001-allergy-at-the-table`; a video-response question; and an e-signature.
3. Take it as a learner on a phone, then check what the reports show for each piece. Note which ones produced a record.
4. Log findings in `adapters/trainual-tour-log.md`, copy the log and any screenshots to Box folder `421832819408` (Learning Studio / Capability Tour), and update the `verified` column above.

The tour answers the questions no help article does: how each item feels on a phone mid-shift, and what a manager can actually see afterward.
