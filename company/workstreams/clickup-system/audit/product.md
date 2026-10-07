# Product Space Audit (901312138543)

## Summary
Product is almost entirely unbuilt. It has one folderless list, **Product Capture** (901327291274), plus two empty folders, **Beverage** (901315418169) and **Culinary** (901315418173), that contain zero lists and zero tasks — they exist as placeholders only. Product Capture itself holds exactly **1 task**: "ClubHouse Ceramics for Coffee," status "revist," no assignee, no due date, no tags, using the custom task type "Idea." The space's only real content is a single capture field set (Notes text field, Category labels field) that's shared verbatim across every "Capture" list in the workspace. There is nothing here yet resembling a beverage or culinary menu-development system — the space is scaffolding waiting for the Founding Punch List restructure to populate it.

## Details

### Structure
- Space: Product (901312138543)
  - List: Product Capture (901327291274) — folderless (API reports it under an implicit hidden folder 901318280288)
  - Folder: Beverage (901315418169) — no lists, no tasks
  - Folder: Culinary (901315418173) — no lists, no tasks

### Statuses (Product Capture)
Space-default status set, shared with every other "Capture" list workspace-wide:
1. revist (open, gray)
2. planning (custom, gray)
3. in progress (custom, purple)
4. complete (done, teal)
5. cancelled (closed, green — note the closed status is colored green, not red/gray as is conventional)

### Custom fields (Product Capture)
- **Notes** — text
- **Category** — labels (multi-select): Asset, Digital / Asset, Physical / Function / Idea

### Task / item types
- Default "Task" type, plus one task using custom item type **"Idea"** (custom_item_id 1019) — confirms the workspace has custom task types configured, at least one of which ("Idea") is Product-relevant.

### Task counts
- 1 task total (open + closed, subtasks included). No subtasks, no checklists, no attachments, no tags, no assignees, no due dates, no priority set.

### Descriptions
Empty on the one sampled task.

### Docs
No docs found scoped to the Product space (search turned up nothing under Product).

## Issues / opportunities
- Beverage and Culinary folders are empty shells — either they were created ahead of content that never arrived, or menu-development work is happening somewhere else (a doc, another space, offline) and hasn't been migrated in. Worth confirming intent before the restructure builds lists inside them.
- The single task's custom type "Idea" suggests an intended taxonomy (Idea / Asset / Function, mirroring the Category field options) that never got applied consistently — only 1 of however-many Product ideas made it into ClickUp.
- No Owner, Classification, or any restructure-relevant field exists yet on this list — everything here will need the new custom fields when the workspace restructure lands.
- Product Capture's status set includes "planning" and "in progress" as if tasks progress through a pipeline, but the one task sitting in "revist" (the default capture status) suggests the pipeline isn't actually being used yet.

## Questions for Brandon
1. Is Beverage/Culinary content living somewhere else right now (Docs, Granola, a spreadsheet) and just needs to be imported, or has that work genuinely not started?
2. What's the intended difference between Beverage and Culinary as folders — separate menu lists each, or a shared "Product" task list split some other way (e.g., by dish vs. drink development stage)?
3. Should "Idea" be the standing task type for early-stage product concepts, with tasks promoted to a different type once past ideation?
