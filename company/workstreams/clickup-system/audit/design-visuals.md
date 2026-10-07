# Design & Visuals Space Audit (90136725596)

## Summary

This space is small and entirely in "capture" mode — nothing has moved past the intake stage. The **Design Documents** folder is completely empty (no docs, no lists), and the only working list, **Design Capture** (19 tasks), holds a loose mix of print/physical-signage needs (business cards, wet-floor signs, matchbooks, celebration cards) and photo/video post-production setup work (Lightroom presets, LUTs, film simulation, Adobe account), almost all still sitting at a "revist" status. The space currently reads as a running idea-dump for a future designer/vendor to execute against, not an active production pipeline.

## Details

### Design Documents (folder, id 901318761389)
- No lists, no docs found. Empty container.

### Design Capture (list, id 901313738581)
- Statuses: revist, planning, in progress, complete, cancelled (the same workspace-wide 5-status Capture pattern seen in every other space).
- **19 tasks**, sampled all 19 (small enough to review in full).
  - 18 of 19 sit at **"revist"** — nothing has progressed to planning/in progress/complete.
  - 1 task ("create new CSS for son") is **cancelled**, and is the *only* task in the space with a real assignee (Dominic Thomas) and a due date.
- Content splits into two clusters that aren't distinguished by any field:
  - **Physical/print collateral**: Lapel Pins, Business Cards, All legal signage, Must Wash Hands Sign, Wet Floor Sign, Out of Order Sign (Bathroom), Celebration Cards, Thank You Cards, Matchbooks, Bathrooms.
  - **Digital photo/video workflow setup**, organized under one parent task "Content System Build Out" with 6 subtasks: Film Simulation Created, Create video LUT, Dial in LUT with kino, Create Lightroom Preset, Create Adobe Account, setup lightroom for workflow, setup export presets.
- Priority is used on a handful of the signage tasks (urgent on "Out of Order Sign, Bathroom"; low on "Wet Floor Sign," "Must Wash Hands Sign," "Bathrooms"; normal on the rest) — otherwise unset.
- No due dates except the one cancelled task.
- Custom fields available: Category (labels: Asset-Digital, Asset-Physical, Function, Idea) and Notes (text) — both are the same workspace-shared fields seen on every Capture list; not confirmed populated on any sampled task (values weren't exposed by the summary fetch — would need per-task inspection to confirm fill rate).
- No tags in use anywhere in this list.
- "Content System Build Out" is the only task with subtasks/checklists structure in the space — everything else is flat.

## Issues / opportunities

1. Design Documents folder is dead weight right now — empty, no docs.
2. Design Capture is functioning purely as a backlog; nothing has a next action, owner, or date except one cancelled task.
3. Physical signage/print items and digital photo-workflow setup are two very different workstreams sharing one flat list with no distinguishing field (Category exists but isn't visibly used to split them).
4. "Content System Build Out" subtasks (Adobe account, Lightroom, LUTs) look like a pre-req chain for photography but aren't sequenced with dependencies — order matters (e.g., "Create Adobe Account" logically precedes "setup lightroom for workflow") but nothing enforces or shows that order today.

## Questions for Brandon

1. Should Design Capture be split into two lists (print/signage vs. digital photo & video workflow), or is a Category field enough once it's actually being filled in?
2. Is anyone assigned to move these "revist" items forward, or are they waiting on the incoming third partner / a hired designer?
3. Is Design Documents intentionally empty for now, or should reference docs (brand guidelines, style references) be living there?
4. Should the Content System Build Out subtasks get dependency ordering (Adobe account → Lightroom setup → LUTs → presets)?
