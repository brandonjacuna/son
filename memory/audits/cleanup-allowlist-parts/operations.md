# Allowlist part: operations

Paths relative to `company/workstreams/operations/` unless noted. Grep scope: company/workstreams/operations, founders/operations-manual (no hits in founders/operations-manual).

## KEEP
- .gitignore:11 | .clickup_token | defensive ignore pattern that prevents committing a token
- output/s03/operating-system-page.md:817 | Airtable | verbatim white paper quote (WP p.21); retirement note added on line 819
- output/s03/operating-system-page.md:819 | Airtable | the added line "(Airtable is retired; financial figures come only from the Investor Review workbook.)" (verbatim quote with retirement note)
- output/s05/operating-system-page.md:260 | experiential | generic English word on a banned-vocabulary list
- RECONSIDERATION-PLAN.md:9 | experiential | "The experiential guidelines are a Box reference file only" (matches root CLAUDE.md scope rule)
- sources/extraction/** (all hits: Airtable, experiential, .clickup_token, son-operational-buildout, Pullman) | verbatim provenance, prior session records. Includes sources/extraction/s13/cu.py, which now reads CLICKUP_API_TOKEN first and keeps the old file path only as fallback (line 3).

## HOLD-PROFILE
- profiles/hospitality-operations-realist.md, profiles/organizational-systems-architect.md, profiles/people-systems-designer.md | Airtable, Business Strategies Notebook, 2ky45bmy-11873 | profile content, no edits
- profiles/learning-and-development/{educational-materials-author-and-editor,highscope,instructional-designer,learner-advocate,tbri}.md | Airtable, Business Strategies Notebook, 2ky45bmy-11873, experiential (generic pedagogy in highscope and instructional-designer) | profile content, no edits

## HOLD-V7
- CLAUDE.md:109 | Business Strategies Notebook, Airtable | ignore-instruction about V7 and retired tool; notebook canon status open
- CLAUDE.md:124 | Business Strategies Notebook, 2ky45bmy-11873 | Excluded list entry
- reference/standing-rules.md:77 | Business Strategies Notebook, 2ky45bmy-11873, Airtable | exclusion list; delete "Airtable," once V7 is ruled on
- reference/standing-rules.md:95 | 2ky45bmy-11873 | V7 notebook row

## HOLD-BRAND
(none)

## REPORT
- sources/son-investor-white-paper-sept-2026.pdf | Pullman, Airtable | investor document, no edits. Pullman sentence at about text line 102 ("He consulted at Pullman Market with the group behind Emmer and Rye"); Airtable at about line 876 ("The data layer is Airtable as the hub for everything that is not CRM"). Owner decides on a paper revision.
- sources/extraction/s05/white-paper.txt and sources/extraction/s01/record.md:53 | Pullman, Airtable | text copies of the same white paper content (also under KEEP as verbatim provenance)
