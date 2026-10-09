# T2 (skill)

## Position

I do not fix the fifty in place. Two rules apply. Procedure step 7: a peer author's draft goes back to the paid author with redlines, not rewritten here. Agent C10, A4: fifty drafts failing the same way (flat, third person, "shall") means the template is likely producing the failure, so fifty hand edits would leave the cause running.

## What I do instead

1. Fix the source first. Find what the template, style guide, or forbidden list says (or fails to say) that leads authors to "the team member shall." Likely causes: the template's sample sentence is in manual voice, or there is no good/bad pair.
2. Draft the fix in library voice, short per agent R9 (a cook must be able to read it):
   - A template line: "Write to the person as 'you' and the house as 'we.'"
   - A forbidden-list voice entry: "the team member shall," "must be completed by," passive with no doer.
   - One bad/good pair: "Verification of allergen protocols must be completed prior to the commencement of service." / "Before service, check tonight's menu against the allergen sheet."
3. Route it. Template, style-guide, and forbidden-list changes go to instructional-designer for instructional soundness, then to Brandon. The voice entries are drafted here; nothing is applied before Brandon says so.
4. Triage the fifty. Run `scripts/lint.py` on all of them. Sample 5 to 8 for the shared pattern and confirm it is one failure. Rank the densest few by hand; do not use a readability score as pass/fail (R6).
5. Return drafts to their paid authors with one short batch note: the pattern, the two-line bad/good pair, and the new template line. Per-draft redlines only where a draft has something beyond the shared pattern (buried verbs, unglossed terms, synonyms for one thing).
6. Check shape first. Any draft that wanders or has a wrong slot goes "developmental first" or routes to curriculum-program-architect before any line edit.

## Watch for

- Rewriting "shall" into "you" can strip nuance or invent facts. Keep every `tool.*`, `fact.*`, `brand.*`, `chef.*` binding as a binding.
- Do not delete craft terms; gloss them (A5).

## Question for Brandon

Is the template change approved to go to instructional-designer now, so authors can revise against it?
