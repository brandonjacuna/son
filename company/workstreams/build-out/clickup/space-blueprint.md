# ClickUp construction space: blueprint (draft, used at P1)

Status: DRAFT. Location in ClickUp is an open decision (see decisions/open.md #1).
Built only by `/lease-signed`, as a preview file first, then created and read back.
Follow `company/workstreams/clickup-system/kb/clickup-knowledge-base.md`: statuses, task types, automations, and rollups are UI-only;
the API can create spaces, folders, lists, custom fields, tasks, views, and docs.

## Structure (proposal)
- Folders by phase: P1 Design, P2 Permitting, P3 Construction, P4 Closeout
- Lists inside each folder by trade: General / Architecture, Bar, Kitchen and Equipment, Live Fire and Ventilation, Plumbing and Water, Electrical, Lighting, HVAC, AV and Network, Storage and Millwork, Fabrication, Permits and Inspections
- Custom fields: Trade (dropdown), Repo path (text), Box link (url), Contractor (text), Drawing ref (text), Decision ref (text)
- Views: "This week" (due this week, not done), "Waiting on others", "Open RFIs", "Inspections"

## Manual UI steps Brandon does first (API cannot)
1. Create statuses: to do, in progress, waiting, in review, done, closed
2. Create task types if wanted: RFI, Submittal, Inspection, Punch item, Change order
3. Turn on the Custom Fields ClickApp for the space (avoids FIELD_605)

## Rules
- Seed tasks come only from repo decisions and gate reviews, never invented.
- Every task links back to the repo file or decision that created it.
