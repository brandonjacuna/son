# Build report: Sŏn Investor Workflow and Founder Docs (2026-09-19)

## Done
| Spec item | Result | By |
|---|---|---|
| §4 Statuses | 12 statuses in order: Relationship (not started); Qualifying through Funded + Paused (active); Passed, Disqualified (done); Investor (closed) | Brandon (UI) |
| §5 Fields | 12 new fields via API; renames: Indicated Amount, Relationship Origin, Materials Sent options (Financial Model (workbook), Disclosure change note, Subscription package). Existing values kept. Capitalization differs from the spec; Brandon chose to keep it | Claude (API) + Brandon (UI) |
| §6 Template | "Investor Lead" with 9 stage checklists (33 items) + "Q&A log" subtask | Claude draft, Brandon saved |
| §7 Automations | A1-A5 built; register and fallbacks written into the Investor CRM list description | Brandon (UI), Claude (description) |
| §7 Raise-level tasks | "Disclosure version control: 2026-09-05 original" (86akmenut) in the Punch List, recipients Robby Grubbs + Robert Jacob Lerma. "Form D and Texas notice filing" is created by A1 at the first acceptance. "Out-of-state notice filings" is added as subtasks of that task when it exists | Claude |
| §7 To-dos out of the CRM | 16 follow-ups recreated in the Founding Punch List, linked by a new "Investor" relationship field (Option 1: ClickUp has no statuses per task type) | Claude |
| §8 Views | Pipeline, Distribution log, Compliance clock, Follow-ups (calendar), Change notes owed | Claude (API), Brandon set the calendar date field |
| §9 Founder Agenda | Page 2ky45bmy-32513 replaced with the local master; the prior content saved to exports/founder-agenda-page-before-2026-09-19.md | Claude |

## Could not be automated
- Status definitions, field renames and option edits, task templates, and Automations have no public API; they were done in the UI.
- Required fields on a status change do not exist in ClickUp; the stage checklists are the gate.
- A5 cannot assign the relationship owner (a dropdown is not an assignee); it tags both founders.
- A4 creates a Punch List task instead of a subtask, because CRM subtasks inherit the pipeline statuses.
- The "Q&A log" subtask in the template still uses pipeline statuses (same limitation).

## Waiting on founder approval (agenda 1.6)
- Record cleanup: Robert Jacob Lerma (remove from the pipeline or Paused with the note); Adam Biechlin to Qualifying; Robby Grubbs Disclosure version sent = "2026-09-05 original" + Needs change note. Robby at Materials sent is deliberate (Brandon).
- Relationship origin and Relationship owner for all 11 investor records (founders fill these).
- Publish "Investor Workflow: Lead to Closed Investor" as a new Doc in Founding Sŏn.

## Integrity
- No task, doc or comment was deleted by Claude. Brandon deleted 6 stuck CRM subtasks while fixing statuses; all 6 were recreated from the baseline export in the Punch List, so no content was lost.
- Nothing related to The Josephine was touched. Read-only docs (2ky45bmy-16953, -16913, Capital Raise docs) were not edited. No phone or email values were changed.
- Automations A1-A5 are untested: a test would move a record's status or ping Dominic, so it needs a throwaway task and a heads-up to Dominic.
