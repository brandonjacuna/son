# Sweep: company/workstreams/operations

Scope: `company/workstreams/operations` (345 grep hit lines, 1407 tracked files). No hits for Jun (as a person), June Shim, Josephine, Sanctuary, Event Co, Home Folder, Replacement Queue, Master Pointer Index, 2ky45bmy-16833, sync-profiles, son-build, son-nerve, son-learning-studio, Keychain outside the items below. Only Pullman hits: 2 (bio line, see section 3).

## 1. Summary

| verdict | count |
|---|---|
| DELETE | 2 lines |
| REWRITE | 26 lines |
| KEEP | 2 lines |
| HOLD-V7 | 4 lines (plus V7 grounding lines inside the 8 profiles) |
| HOLD-RAW | 119 files (extraction/ and archive/) |
| HOLD-PROFILE | 8 files |
| REPORT | 1 investor document (plus 1 text copy under extraction/) |

Note: `output/` (program outputs, superseded by `manual/`) is not on the raw list, so it is classified per line below. The owner may prefer to treat the whole `output/` tree as HOLD-RAW.

## 2. Per-line table (DELETE / REWRITE / KEEP / HOLD-V7)

Paths relative to `company/workstreams/operations/`.

| path:line | term | snippet | verdict | reason | proposed replacement |
|---|---|---|---|---|---|
| CLAUDE.md:109 | Business Strategies Notebook, Airtable | "ignore ... references to the V7 Business Strategies Notebook, the brand guidelines, or Airtable as authorities" | HOLD-V7 | Notebook canon status is open. Line is an ignore-instruction, not a canon pointer | n/a |
| CLAUDE.md:124 | Business Strategies Notebook, 2ky45bmy-11873 | Excluded list entry | HOLD-V7 | Same open question | n/a |
| CLAUDE.md:126 | Airtable | `- Airtable.` in Excluded list | DELETE | Airtable retired everywhere; an exclusion entry is moot | n/a |
| CLAUDE.md:174 | .clickup_token | "Use REST through `extraction/s13/cu.py` (token in `~/.clickup_token`) ..." | REWRITE | Mac-only token path | "Use REST through `extraction/s13/cu.py` (token in the CLICKUP_API_TOKEN environment variable; cloud sessions can also use the ClickUp connector) for bulk work. The MCP connector caps at 1,000 calls a day." Note: `extraction/s13/cu.py:3` hard-codes `~/.clickup_token`; change it to read `os.environ['CLICKUP_API_TOKEN']` or leave as raw |
| CLAUDE.md:198 | son-operational-buildout | "Repo: `brandonjacuna/son-operational-buildout` (private)." | REWRITE | Old repo name | "Repo: `son` (private). This workstream lives at `company/workstreams/operations`." |
| .gitignore:1 | experiential | "# Brand and experiential material: excluded from this program" | REWRITE | Experiential no longer a category | "# Brand material: excluded from this program (2026-09-26)" |
| .gitignore:11 | .clickup_token | `.clickup_token` ignore pattern | KEEP | Defensive token-file ignore, not a pointer | n/a |
| RECONSIDERATION-PLAN.md:9 | experiential | "Brand guidelines and the experiential deck are out of scope" | REWRITE | Experiential stripped from canon | "Brand guidelines are out of scope, because there is no property yet. The experiential guidelines are a Box reference file only." |
| RECONSIDERATION-PLAN.md:46 | experiential | "### Brand and experiential influence" | REWRITE | Heading | "### Brand influence" |
| RECONSIDERATION-PLAN.md:48 | experiential | "... brand canon, the deck, or experiential guidelines ..." | REWRITE | Drop experiential as a category | Replace "brand canon, the deck, or experiential guidelines" with "brand canon or the deck" |
| RECONSIDERATION-PLAN.md:57 | experiential | "Removed: brand and experiential detail, program machinery." | REWRITE | Same | "Removed: brand detail, program machinery." |
| RECONSIDERATION-PLAN.md:69 | experiential | "**Brand- and experiential-derived ideas.**" | REWRITE | Same | "**Brand-derived ideas.**" |
| RECONSIDERATION-PLAN.md:133 | son-operational-buildout | "private repo `brandonjacuna/son-operational-buildout`" | REWRITE | Old repo name | "Done: the work now lives in the private repo `son`, under `company/workstreams/operations`, baseline pushed without the brand files." |
| reference/standing-rules.md:77 | Business Strategies Notebook, 2ky45bmy-11873, Airtable | Exclusion list naming V1 through V7, Airtable, Box profile clusters | HOLD-V7 | Notebook status open. Separately, delete the word "Airtable," from this line once the owner rules on V7 | n/a |
| reference/standing-rules.md:95 | 2ky45bmy-11873 | "V7 notebook ... Both excluded. The record is ..." | HOLD-V7 | Open question | n/a |
| reference/standing-rules.md:98 | Airtable | `Financials | "from Airtable (appKHeje63inr1fLG) or absent" | Airtable excluded ...` | REWRITE | Names retired tool and a base ID | "\| Financials \| a stale profile instruction naming a retired data tool \| Financials come only from the current Investor Review workbook in Box (Sŏn / 02. Capital Raise). Not a context source for this program. State the gap and flag it \|" |
| reference/standing-rules.md:104 | Airtable | "...instruction to read V7, the archived ClickUp canon doc, Airtable, or a Box profile..." | REWRITE | Remove retired tool | "A session that encounters an instruction to read V7, the archived ClickUp canon doc, or a Box profile has hit a stale source. It does not follow it. It surfaces the conflict." (V7 mention stays pending the HOLD-V7 ruling) |
| manual/2.1-founding-documents/mapping.md:117 | experiential | "rested on the brand guidelines or the experiential deck" | REWRITE | Experiential not canon | "rested on the brand guidelines" |
| manual/2.2-the-operating-system/mapping.md:110 | experiential | same phrase | REWRITE | same | "rested on the brand guidelines" |
| manual/2.3-operating-cadence/mapping.md:113 | experiential | same phrase | REWRITE | same | "rested on the brand guidelines" |
| manual/3.1-recruiting/mapping.md:79 | experiential | "resting on the brand guidelines or the experiential deck" | REWRITE | same | "resting on the brand guidelines" |
| manual/3.2-hiring/mapping.md:98 | experiential | "drawn from the brand guidelines and experiential deck" | REWRITE | same | "drawn from the brand guidelines" |
| manual/5.4-the-formal-review-process/tasks.md:207 | Airtable | "(WP p. 21) Airtable is the hub for everything that is not CRM" | REWRITE | Live manual cites a retired tool as default | "(WP p. 21) a single data-layer hub holds everything that is not CRM; the tool the white paper names is no longer in use" |
| output/s01/work-items.md:91 | Airtable | "no figure is pulled from Airtable or anywhere else" | REWRITE | Retired tool named | "no figure is pulled from any source other than the Investor Review workbook" (Brandon-approved source is the workbook; confirm wording matches the original rule) |
| output/s02/operating-system-page.md:5 | experiential | "Deck is the brand and experiential guidelines deck by page" | REWRITE | Experiential as source | "Deck is the brand guidelines deck by page" |
| output/s02/operating-system-page.md:56 | experiential | "The deck's cover, marked GOVERNING, reads: 'Brand and experiential guidelines. The source of truth for every decision...'" paragraph | DELETE | Treats experiential guidelines as governing canon | n/a (delete the paragraph) |
| output/s02/operating-system-page.md:132 | Airtable | "The white paper names Airtable as the data-layer hub; Airtable is no longer in use." | REWRITE | Retired tool | "The white paper names a data-layer hub tool that is no longer in use." |
| output/s03/operating-system-page.md:817 | Airtable | Verbatim record quote "The data layer is Airtable as the hub..." | REWRITE | Retired tool inside quote | Replace "Airtable" with "[retired hub tool]" inside the quote |
| output/s03/operating-system-page.md:819 | Airtable | "Airtable is 'no longer in use for any purpose.' ... 'from Airtable, never from memory.'" | REWRITE | Retired tool | "This program's source boundary states that the hub tool is no longer in use. The profile for this seat, written before the current boundary, instructs it to pull every count from that tool, never from memory." |
| output/s05/operating-system-page.md:260 | experiential | forbidden-word list "... elevated, experiential, innovative ..." | KEEP | Generic English word on a banned-vocabulary list, not a pointer | n/a |
| output/s09/operating-system-page.md:3 | experiential | "Deck 3.0 is the brand and experiential guidelines deck" | REWRITE | Experiential as source | "Deck 3.0 is the brand guidelines deck" |
| output/s10/operating-system-page.md:3 | experiential | same sentence | REWRITE | same | "Deck 3.0 is the brand guidelines deck" |
| output/s13/RESUME-HERE.md:18 | .clickup_token | "personal token in `~/.clickup_token` (mode 600)" | REWRITE | Mac-only token path | "personal token (CLICKUP_API_TOKEN in cloud sessions)" |
| output/s13/RESUME-HERE.md:19 | Airtable | "...and point to Airtable. The page used neither..." | REWRITE | Retired tool | "...and point to a retired data tool. The page used neither..." |

## 3. HOLD-PROFILE (8 files, `profiles/`)

No Jun, Josephine, Sanctuary, or Pullman content in any profile.

| file | terms (count) |
|---|---|
| profiles/hospitality-operations-realist.md | Airtable 31, Business Strategies Notebook 1, 2ky45bmy-11873 1 |
| profiles/organizational-systems-architect.md | Airtable 22, Business Strategies Notebook 1, 2ky45bmy-11873 1 |
| profiles/people-systems-designer.md | Airtable 20, Business Strategies Notebook 1, 2ky45bmy-11873 1 |
| profiles/learning-and-development/educational-materials-author-and-editor.md | Airtable 1, Business Strategies Notebook 1, 2ky45bmy-11873 1 |
| profiles/learning-and-development/highscope.md | Airtable 1, Business Strategies Notebook 1, 2ky45bmy-11873 1, experiential 3 (Kolb, "experiential-learning theory": generic pedagogy, KEEP) |
| profiles/learning-and-development/instructional-designer.md | Airtable 1, Business Strategies Notebook 1, 2ky45bmy-11873 1, experiential 2 (generic "experiential emphasis" in 70-20-10 discussion: KEEP) |
| profiles/learning-and-development/learner-advocate.md | Airtable 1, Business Strategies Notebook 1, 2ky45bmy-11873 1 |
| profiles/learning-and-development/tbri.md | Airtable 3, Business Strategies Notebook 1, 2ky45bmy-11873 1 |

Phase 3 notes: the three team profiles also carry V7-derived and figure content, e.g. a "roughly 21.5 percent" compensation figure (realist l.154/211, people-systems l.41/153/220, architect l.180) that is not from the Investor Review workbook, and "V7 commits ..." readings (realist l.145, 207). Every profile ends with "Project grounding" naming V7 and ClickUp page IDs (HOLD-V7).

## 4. REPORT (investor document)

- `sources/son-investor-white-paper-sept-2026.pdf`: Pullman at text line ~102: "He consulted at Pullman Market with the group behind Emmer and Rye." This is a bio credential about Brandon but names a second business (Emmer and Rye) and says "consulted", not a single clean credential line. Airtable at ~876: "The data layer is Airtable as the hub for everything that is not CRM". The current investor white paper names a retired tool. No Jun, Josephine, Sanctuary hits.
- `extraction/s05/white-paper.txt` (lines 107 Pullman, Airtable 1) and `extraction/s01/record.md:53` (same Pullman sentence) are text copies of the same white-paper content (HOLD-RAW).

## 5. HOLD-RAW (119 files; file | terms x count)

Owner decides delete vs archive folder. Totals: archive/ and extraction/ carry about 270 of the 345 hits, nearly all Airtable (tracker/ledger/brief copies) and "experiential" (tracker-before/after/live copies, one per session folder s04 to s17).

Common pattern: every `extraction/sNN/tracker-{before,after,live,live-after}.md` has Airtable x2 plus experiential x1. Every `extraction/sNN/ledger-chunks/*.md` has Airtable x1 and/or experiential x1.

Notable raw files with stale pointers (token path, old repo):
- extraction/s13/cu.py (.clickup_token x1; live script, still hard-codes the Mac path)
- extraction/clickup-build/build.py (son-operational-buildout x1; hard-coded GitHub URL)
- extraction/build/HANDOFF.md (.clickup_token x2, son-operational-buildout x1)
- extraction/s14/HANDOFF-from-s13.md (.clickup_token x2), s15/HANDOFF-from-s14.md and s16/HANDOFF-from-s15.md (.clickup_token x1 each)
- archive/CLAUDE-extraction-program.md (2ky45bmy-11873 x1, Airtable x1, Business Strategies Notebook x1, Experiential x1, experiential x1)

Full per-file list:

- extraction/s11/ledger-chunks/t01.md | Airtable  x1; experiential  x1; 
- extraction/s11/ledger-chunks/t03.md | Airtable  x1; 
- extraction/s11/ledger-chunks/t03b.md | Airtable  x1; 
- extraction/s11/tracker-live-after.md | Airtable  x2; experiential  x1; 
- extraction/s11/fable-brief.md | Airtable  x1; 
- extraction/s11/tracker-before.md | Airtable  x2; experiential  x1; 
- extraction/s11/tracker-after.md | Airtable  x2; experiential  x1; 
- extraction/pilot-2.1/old-items.md | Airtable  x2; 
- extraction/pilot-2.1/fable-brief.md | experiential  x2; 
- extraction/pilot-2.1/session-brief.md | experiential  x1; 
- extraction/s15/ledger-chunks/l01.md | Airtable  x1; 
- extraction/s15/ledger-chunks/l08.md | Airtable  x1; 
- extraction/s15/ledger-chunks/l02.md | experiential  x1; 
- extraction/s15/HANDOFF-from-s14.md | .clickup_token  x1; 
- extraction/s15/tracker-live-after.md | Airtable  x2; experiential  x1; 
- extraction/s15/tracker-before.md | Airtable  x2; experiential  x1; 
- extraction/s15/tracker-after.md | Airtable  x2; experiential  x1; 
- extraction/s02/record-brief.md | Airtable  x2; experiential  x1; 
- extraction/s10/ledger-chunks/t01.md | Airtable  x1; experiential  x1; 
- extraction/s10/ledger-chunks/t03.md | Airtable  x1; 
- extraction/s10/tracker-live.md | Airtable  x2; experiential  x1; 
- extraction/s10/tracker-live-after.md | Airtable  x2; experiential  x1; 
- extraction/s10/fable-brief.md | Airtable  x1; 
- extraction/s10/chunks/c01.md | experiential  x1; 
- extraction/s10/tracker-before.md | Airtable  x2; experiential  x1; 
- extraction/s10/tracker-after.md | Airtable  x2; experiential  x1; 
- extraction/s10/page-live.md | experiential  x1; 
- extraction/s09/ledger-chunks/t01.md | Airtable  x1; experiential  x1; 
- extraction/s09/ledger-chunks/t03.md | Airtable  x1; 
- extraction/s09/tracker-live.md | Airtable  x2; experiential  x1; 
- extraction/s09/tracker-live-after.md | Airtable  x2; experiential  x1; 
- extraction/s09/fable-brief.md | Airtable  x1; 
- extraction/s09/chunks/c01.md | experiential  x1; 
- extraction/s09/tracker-before.md | Airtable  x2; experiential  x1; 
- extraction/s09/tracker-after.md | Airtable  x2; experiential  x1; 
- extraction/s09/page-live.md | experiential  x1; 
- extraction/s13/cu.py | .clickup_token  x1; 
- extraction/s13/ledger-chunks/t01.md | Airtable  x1; 
- extraction/s13/ledger-chunks/t07.md | Airtable  x1; 
- extraction/s13/ledger-chunks/t02.md | experiential  x1; 
- extraction/s13/carryovers.md | Airtable  x1; 
- extraction/s13/tracker-live-after.md | Airtable  x2; experiential  x1; 
- extraction/s13/tracker-before.md | Airtable  x2; experiential  x1; 
- extraction/s13/tracker-after.md | Airtable  x2; experiential  x1; 
- extraction/s13/tracker-live-before-upload.md | Airtable  x2; experiential  x1; 
- extraction/s12/ledger-chunks/t01.md | Airtable  x1; 
- extraction/s12/ledger-chunks/t07.md | Airtable  x1; 
- extraction/s12/ledger-chunks/t02.md | experiential  x1; 
- extraction/s12/tracker-live-after.md | Airtable  x2; experiential  x1; 
- extraction/s12/fable-brief.md | Airtable  x1; 
- extraction/s12/tracker-before.md | Airtable  x2; experiential  x1; 
- extraction/s12/tracker-after.md | Airtable  x2; experiential  x1; 
- extraction/s17/tracker-live-after.md | Airtable  x2; experiential  x1; 
- extraction/s17/live-check.md | Airtable  x1; 
- extraction/s17/tracker-before.md | Airtable  x2; experiential  x1; 
- extraction/s17/tracker-after.md | Airtable  x2; experiential  x1; 
- extraction/s03/brief.md | Airtable  x2; 
- extraction/s04/brief.md | Airtable  x1; 
- extraction/s04/tracker-before.md | Airtable  x2; experiential  x1; 
- extraction/s04/tracker-after.md | Airtable  x2; experiential  x1; 
- extraction/s16/ledger-chunks/l01.md | Airtable  x1; 
- extraction/s16/ledger-chunks/l08.md | Airtable  x1; 
- extraction/s16/ledger-chunks/l02.md | experiential  x1; 
- extraction/s16/tracker-live-after.md | Airtable  x2; experiential  x1; 
- extraction/s16/tracker-before.md | Airtable  x2; experiential  x1; 
- extraction/s16/tracker-after.md | Airtable  x2; experiential  x1; 
- extraction/s16/HANDOFF-from-s15.md | .clickup_token  x1; 
- extraction/build/s10/old-page.md | experiential  x1; 
- extraction/build/BUILD-BRIEF.md | Airtable  x1; 
- extraction/build/s09/old-page.md | experiential  x1; 
- extraction/build/s13/old-items.md | Airtable  x1; 
- extraction/build/s03/old-page.md | Airtable  x3; 
- extraction/build/HANDOFF.md | .clickup_token  x2; son-operational-buildout  x1; 
- extraction/build/1-DIGEST-BRIEF.md | experiential  x1; 
- extraction/build/cross/leftovers.md | Airtable  x2; 
- extraction/build/s05/old-page.md | experiential  x1; 
- extraction/build/s06/digest.md | experiential  x1; 
- extraction/s05/white-paper.txt | Airtable  x1; Pullman  x1; 
- extraction/s05/fable-brief-part1.md | Airtable  x1; 
- extraction/clickup-build/build.py | son-operational-buildout  x1; 
- extraction/s06/DRAFT-fable-brief-from-s05-chat.md | Airtable  x1; 
- extraction/s06/fable-brief.md | Airtable  x1; 
- extraction/s08/ledger-chunks/t01.md | Airtable  x1; experiential  x1; 
- extraction/s08/ledger-chunks/t03.md | Airtable  x1; 
- extraction/s08/tracker-live.md | Airtable  x2; experiential  x1; 
- extraction/s08/fable-brief.md | Airtable  x1; 
- extraction/s08/tracker-before.md | Airtable  x2; experiential  x1; 
- extraction/s08/tracker-after.md | Airtable  x2; experiential  x1; 
- extraction/s07/ledger-chunks/t01.md | Airtable  x1; experiential  x1; 
- extraction/s07/ledger-chunks/t02.md | Airtable  x1; 
- extraction/s07/tracker-live.md | Airtable  x2; experiential  x1; 
- extraction/s07/fable-brief.md | Airtable  x1; experiential  x1; 
- extraction/s07/tracker-before.md | Airtable  x2; experiential  x1; 
- extraction/s07/tracker-after.md | Airtable  x2; experiential  x1; 
- extraction/s01/record.md | Airtable  x1; Pullman  x1; 
- extraction/s14/HANDOFF-from-s13.md | .clickup_token  x2; 
- extraction/s14/ledger-chunks/t01.md | Airtable  x1; 
- extraction/s14/ledger-chunks/t07.md | Airtable  x1; 
- extraction/s14/ledger-chunks/t02.md | experiential  x1; 
- extraction/s14/tracker-live-after.md | Airtable  x2; experiential  x1; 
- extraction/s14/tracker-before.md | Airtable  x2; experiential  x1; 
- extraction/s14/tracker-after.md | Airtable  x2; experiential  x1; 
- archive/CLAUDE-extraction-program.md | 2ky45bmy-11873  x1; Airtable  x1; Business Strategies x1; Experiential  x1; experiential  x1; 
- archive/clickup-export-2026-09-26/buildout-subtasks.json | Airtable  x6; 
- archive/clickup-export-2026-09-26/tasks/86akh2r4k.json | Airtable  x3; 
- archive/clickup-export-2026-09-26/tasks/86ajgmhfd.json | Airtable  x6; 
- archive/clickup-export-2026-09-26/tasks/86akh3tp5.json | Airtable  x3; 
- archive/clickup-export-2026-09-26/tasks/86ajgmh9a.json | Airtable  x3; 
- archive/clickup-export-2026-09-26/tasks/86ajgmjey.json | Airtable  x3; 
- archive/clickup-export-2026-09-26/tasks/86ajgmhd7.json | Airtable  x3; 
- archive/clickup-export-2026-09-26/session-tasks.json | Airtable  x15; 
- archive/clickup-export-2026-09-26/tracker-doc/01-2ky45bmy-30353.md | Airtable  x2; experiential  x1; 
- archive/clickup-export-2026-09-26/carryover-register.json | Airtable  x9; 
- archive/clickup-export-2026-09-26/operating-system-doc/11-2ky45bmy-31853.md | experiential  x1; 
- archive/clickup-export-2026-09-26/operating-system-doc/04-2ky45bmy-31693.md | Airtable  x3; 
- archive/clickup-export-2026-09-26/operating-system-doc/06-2ky45bmy-31733.md | experiential  x1; 
- archive/clickup-export-2026-09-26/operating-system-doc/10-2ky45bmy-31833.md | experiential  x1; 
- archive/clickup-export-2026-09-26/operating-system-doc/01-2ky45bmy-30373.md | experiential  x1; 
- archive/clickup-export-2026-09-26/operating-system-doc/03-2ky45bmy-31673.md | Airtable  x2; experiential  x2; 

## 6. Surprising / notable

- No Jun/Josephine/Sanctuary/Event Co content anywhere in this workstream; the only Pullman text is the white-paper bio sentence (and its copies).
- The investor white paper PDF (and `manual/5.4` citing it) still names Airtable as the data-layer hub. REPORT only; owner decides whether the paper gets a revision.
- The three team profiles hard-wire "figures from Airtable only" and a 21.5 percent compensation figure. Phase 3 must replace with the workbook rule and drop the figure.
- `CLAUDE.md:109-126` and `reference/standing-rules.md` still describe an extraction-program regime (Box profile copy table with folder IDs, `profiles/people-and-culture/` destinations that do not exist, Excluded lists). The whole section looks stale against the single-repo layout; flagged for owner, not classified further.
- `.gitignore` lists `sources/brand-guidelines.md`, `sources/brand-guidelines-deck.pdf`, `extraction/s02/deck.md`, `extraction/s05/brand-deck.txt`; none are tracked or present (only the three PDFs in `sources/` exist). Brand-deck-derived text may still sit in extraction/s02 record-brief and output pages.
- No founder-only material found under this workstream by these terms.
