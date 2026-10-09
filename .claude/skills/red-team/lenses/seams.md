# Lens: seams

Where the target meets its neighbors: what it decides that someone else owns, and what nobody owns.

Neighbors are named in the brief (other seats, other skills, other documents, a ClickUp list, a Box folder). Read only their scope: an agent's `description:` and Scope section, a skill's frontmatter and first heading, a document's headings. Never whole files.

Check:
- Overlap: a decision, trigger, or output the target claims that a neighbor already owns. Two owners means neither is accountable. Quote both claims.
- Gap: a decision the target hands off ("the chef decides", "goes to counsel", "the Head of Beverage owns") to a neighbor that does not exist yet or does not list it. A hand-off into a void is a flag.
- Trigger collision (skills only): phrases in the target's description that would also fire a row in `.claude/skills/REGISTRY.md`. One owner per trigger.
- Conflict: a rule in the target that contradicts a line in `memory/decisions.md` or a neighbor's rule. The decision wins; the flag names both lines.
- Interface shape: the target expects an input (a file, a field, a format) that no neighbor produces, or produces an output no neighbor consumes.

For a seat (agent or skill): the frame's seams table lists the neighbors. Check each row both ways: does the neighbor's `agent.md` agree about who owns what?

Zero flags is a valid result. Say which neighbors you read.
