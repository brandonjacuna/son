# Events Space Audit (90136733952)

## Summary
Events is the most populated of the four audited spaces, but almost all of its volume comes from one deeply nested outline rather than distinct tasks. The space has one list, **Events Capture** (901313751988), no folders, holding **20 tasks total** — but the real count of independent ideas is closer to 6-7. A parent task "Design Pop Up Concepts" has 4 subtasks (the Meteor, E&R Restaurants, Collabs, Sponsors), and "Sponsors" itself has **13 sub-subtasks**, all vendor/supplier names (Beer via Lindsay, Wine via Kayla McAndrew, Spirits via Tyler Mallams, US Foods via Jason, DoorDash, SpotOn, Ben E Keith, 7R, Kettl Tea, Spirit Tea, GFN Coffee, Pullman Market, Douglas Kuehn III). Every task, at every level, sits in status "revist" with no assignee, no due date, no priority, no tags, and no description — this is a 3-level mind-map of pop-up/collab sponsor leads, not a tracked project plan.

## Details

### Structure
- Space: Events (90136733952)
  - List: Events Capture (901313751988) — only list, no folders

### Statuses
Standard Capture set: revist (open) → planning → in progress → complete (done) → cancelled (closed).

### Custom fields (list-level)
- **Department Crossover** — labels (multi-select), the full department taxonomy: Accounting, Beverage, Business Intelligence, Design & Visuals, Culinary, Events, Hospitality, Operations, People, Promotion, Property, Technology. (Different field from the Notes/Category pair used in Product/Hospitality — Events instead tags cross-department dependency.)

### Task/item types
All default "Task" type in the sample — no custom item types observed.

### Task counts and hierarchy
- 20 tasks total (open + closed, subtasks included), but structurally:
  - 6 flat top-level ideas outside the pop-up thread (Design Pop Up Concepts itself is one of these top-level tasks)
  - Under "Design Pop Up Concepts": 4 subtasks (the Meteor, E&R Restaurants, Collabs, Sponsors)
  - Under "Sponsors" (one of those 4): 13 sub-subtasks, all beverage/food vendor contacts
- No checklists anywhere; the checklist mechanism isn't used — nesting via subtasks is doing that job instead.

### Assignee / due date / priority / tag usage
None across the sample — zero assignees, zero due dates, zero priorities, zero tags on all 20 tasks.

### Descriptions
Empty on every sampled task.

### Docs
No docs found scoped to Events.

## Issues / opportunities
- The "Sponsors" sub-list (13 vendor names) is effectively a flat contact/lead list masquerading as subtasks three levels deep. It will not surface well in any view, report, or the Founding Punch List once that gets built, and it can't easily carry per-vendor status (all 13 share the same generic "revist").
- Three levels of subtasking (Design Pop Up Concepts → Sponsors → 13 vendors) is deeper than ClickUp's own subtask UI handles gracefully in list/board views — this may be invisible to Dominic/the third partner unless they expand each level manually.
- No use of the "Department Crossover" field on any sampled task despite it being the one custom field defined for this list — it's configured but not populated yet.
- Given Beverage/Culinary vendor names recur here (US Foods, Ben E Keith, Kettl Tea, GFN Coffee) there's a strong overlap with the (currently empty) Product > Beverage/Culinary folders — this vendor list may belong partly in Product once that space is built out.

## Questions for Brandon
1. Should the 13 Sponsors sub-tasks become their own flat list (e.g., "Sponsor/Vendor Leads") with real status per vendor, instead of nested three deep under one task?
2. Is "Design Pop Up Concepts" a single event concept, or is it really 4 separate initiatives (the Meteor, E&R Restaurants, Collabs, Sponsors) that should be split into top-level tasks or even their own list?
3. Should vendor/supplier tasks that are really Product/Beverage or Culinary leads (US Foods, Ben E Keith, coffee/tea vendors) get cross-linked or moved once the Product space is built out, or is Events meant to own all pop-up-related vendor relationships regardless of category?
