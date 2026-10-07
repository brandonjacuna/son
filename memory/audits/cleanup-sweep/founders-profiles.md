# Cleanup sweep: founders + profiles

Paths: `founders`, `profiles`. Read-only sweep, 367 hit lines in 53 files (founders/capital-raise 7 files, founders/profiles/_source 11 files, profiles/_source 35 files). No hits in `profiles/` outside `_source/`, none in `founders/` outside `capital-raise` and `profiles/_source`.

## 1. Summary

| verdict | count (files) | hit lines |
|---|---|---|
| DELETE | 0 | 0 |
| REWRITE | 0 | 0 |
| KEEP | 0 | 0 |
| HOLD-PROFILE | 46 | 223 |
| REPORT (investor docs) | 7 | 144 |
| HOLD-RAW / HOLD-V7 | 0 | 0 |

Note: the "Business Strategies Notebook / 2ky45bmy-11873" lines inside profile files are HOLD-V7 by the brief but live in HOLD-PROFILE files; counted once under HOLD-PROFILE and flagged in section 3 (30 files, 1 line each, do not propose deletion).

Term totals across both paths: Pullman 0, Jun 0, June Shim 0, Sanctuary 0, Event Co 0, Replacement Queue 0, sync-profiles 0, son-build/son-nerve/son-learning-studio/son-operational-buildout 0, Keychain 0, .clickup_token 0. Josephine 17 lines in 12 files, Home Folder 12 files, Master Pointer Index 1, experiential 4 files (all generic L&D), Airtable (every file except where noted), Business Strategies Notebook 30 files.

## 2. Per-line table (DELETE/REWRITE/KEEP)

None. Every hit is in a `_source` baseline (HOLD-PROFILE) or an investor document (REPORT).

## 3. HOLD-PROFILE (verbatim Box baseline, phase 3 rewrites)

Per-file term counts are in the table at the end of this file. Content that must be cut regardless:

### Josephine (restaurant/pop-up, must be cut; 17 lines)
- `founders/profiles/_source/investment/Pitch_Deck_Architect_Profile.md:197`: "The Josephine pop-up program supplies first-party traction and original photography for the market and experience slides; use real imagery, never stock..."
- `founders/profiles/_source/investment/Business_Plan_Architect_Profile.md:194`: "The Josephine pop-up program supplies first-party traction and comparable demand evidence for the market and concept sections; use real evidence..."
- `founders/profiles/_source/investment/Private_Raise_Compliance_Advisor_Profile.md:148`: "...has a raise been mentioned on the Son Instagram, the website, or at a Josephine pop-up. If yes, that is general solicitation..." (also :186: "The Josephine pop-up program is a public-facing brand surface; treat it as a live general-solicitation surface during any active raise...")
- `founders/profiles/_source/investment/Investor Targeting Strategist Profile.md:170`: "The Josephine pop-up program is a demand-proof and relationship instrument; pop-up traction and the loyal-customer base feed the friends-and-family and Reg CF tracks."
- `founders/profiles/_source/investment/Market Competitive Analyst Profile.md:10`: "The Josephine pop-up program is a live demand-validation instrument..." ; `:103`: "first-party (Josephine pop-up covers, reservation velocity, ...)" ; `:171`: "The Josephine pop-up program (San Antonio) is a live demand-validation instrument; pull pop-up traction as first-party evidence." Note this profile also bases its revenue-ramp skepticism on Josephine traction.
- `profiles/_source/voice/Vee_Conviction_Voice_Profile.md:171` and `House_Voice_Brandon_Profile.md:172`: "Applies across both ventures: Son (Korean fine dining, 207 E St. Elmo Rd, Austin) and The Josephine (pop-up events, San Antonio)."
- `profiles/_source/voice/Graham_Clarity_Voice_Profile.md:158` and `Gladwell_Narrative_Voice_Profile.md:156`: same, plus "When writing for The Josephine presented by Son, brand voice applies; when white-labeled, follow the white-label brief."
- `profiles/_source/narrative-and-structure/Narrative_Architect_Profile.md:189`: "Ventures: Son (Korean fine dining, 207 E St. Elmo Rd, Austin) and The Josephine (pop-up events, San Antonio)."
- `founders/profiles/_source/investment/Investor_Website_Architect_Profile.md:167` matched on "experiential" only (see below), not Josephine.

### Pullman, Jun / June Shim, Sanctuary
Zero hits (case-insensitive recheck for pullman, shim, sanctuary, jun also zero) in both paths.

### Experiential
Generic L&D / brand English, not the Experiential Guidelines. No canon pointer found. Files: `profiles/_source/learning-and-development/` Curriculum & Program Architect (63, 141), HighScope (72, 172, 211, Kolb), Instructional Designer (73, 120). `founders/profiles/_source/investment/Investor_Website_Architect_Profile.md` has 1 hit (line 167 region, brand wording). Treat as KEEP-equivalent at phase 3.

### Stale pointers (rewrite at phase 3)
- "Son Home Folder" path: 10 files `profiles/_source/design-translating-team/01..10_*` (one line each; e.g. `06_Environmental_Signage_Specialist_Profile.md:178` and `08_Design_Director_Profile.md:173`: "Profiles live in Box, Son Home Folder, Claude, Profiles, Design Translating Team.") plus `founders/profiles/_source/investment/Investor_Design_Director_Profile.md:184`.
- Master Pointer Index: `founders/profiles/_source/investment/Hospitality Investment Analyst Profile.md:167`: "Financials: St. Elmo Dashboard V2 (appKHeje63inr1fLG) primary; Investor Dashboard (appHj181Vju7No7GH). Pre-Opening Expenses and LHI tables as referenced in the Master Pointer Index." This line is both a stale pointer and an Airtable financial source.
- Airtable as a financial source: 11 founders investment profiles (6 to 19 lines each) and 24 profiles/_source files in learning-and-development, people-and-culture, scaling-people, narrative, voice (heaviest: Hospitality Operations Realist 19, Hospitality Investment Analyst 19, Investor_Financial_Exhibit_Architect 17, Investment Thesis Architect 15). All must be repointed to the Investor Review workbook in Box (Sŏn / 02. Capital Raise).

### HOLD-V7 lines inside profiles (do not propose deletion)
"Business Strategies Notebook" / `2ky45bmy-11873` appears once in each of 30 files: learning-and-development (Assessment & Competency Designer 208, Curriculum & Program Architect 191, Educational Materials Author and Editor 219, HighScope 218, Hospitality Craft Educator 344, Instructional Designer 218, Learner Advocate 201, TBRI 199), people-and-culture (all 8 files, lines 217-246 region), scaling-people (Organizational Systems Architect 204, Hospitality Operations Realist 245, People Systems Designer 252), and founders `Operating_Systems_Futurist_Profile.md:215` ("V4.0 Business Strategies Notebook (ClickUp doc 2ky45bmy-11873)..."). All are "Project grounding" lines. Canon status is an open owner question.

## 4. REPORT: founders/capital-raise (no edits proposed)

Files and terms (all Airtable, hit-line counts):

| file | Airtable lines |
|---|---|
| working-files/Son Investor Materials - Internal Review.md | 3 (lines 7, 16, 19) |
| working-files/St_Elmo_Classification_Main_2026-08-22.md | 1 (118) |
| working-files/St_Elmo_Classification_Appendix_2026-08-22_part1.md | 7 |
| working-files/St_Elmo_Classification_Appendix_2026-08-22_part2.md | 32 |
| working-files/St_Elmo_Exhibit_Build_Specification_2026-08-22_part1.md | 8 |
| working-files/St_Elmo_Exhibit_Build_Specification_2026-08-22_part2.md | 9 |
| working-files/_tmp_repr_part1_copy.md | 8 (byte-identical to Exhibit_Build_Specification part1; cmp confirms) |

Observation only: these are the 22 Aug 2026 read-only Airtable classifications and exhibit specs, and the Internal Review reconciles "current Airtable Refresh records". They predate or conflict with the "Airtable retired, workbook only" rule. Owner decides whether they are superseded.

### Pullman check (phase 1 step 7)
- `founders/capital-raise`: zero Pullman mentions (also zero Josephine, Sanctuary, Shim). `investors/adam-biechlin.md` and `robby-grubbs.md` contain no Pullman.
- Neither the "207 St. Elmo deck" nor a deck file exists under founders or profiles. The only deck-like items: the Internal Review refers to "The separate June HTML pitch deck is materially stale and should not be sent unchanged with them." (line 7) and "The official pair, Airtable and June deck were not changed by this review." (line 19). Here "June" is a month, not a person. The deck itself is not in these paths; `company/brand/design-system/guidelines-deck/` is the brand guidelines deck, not the investor deck.
- Investor Diligence White Paper exists outside my paths as `company/workstreams/operations/sources/son-investor-white-paper-sept-2026.pdf` and its text extraction `company/workstreams/operations/extraction/s05/white-paper.txt`. Pullman mentions found in the extraction (lines 107, and again at 102 in a second pass copy of the text), single quote:
  - "He consulted at Pullman Market with the group behind Emmer and Rye." (white-paper.txt:107, in a sentence list of Brandon's career: "He ran opening service at Coqodaq, a Korean concept in New York from the group behind Cote... He consulted at Pullman Market with the group behind Emmer and Rye. He has run multi-concept operations across more than one market.")
  - Confirmed in both forms: the PDF (pdftotext, line 102) and the extraction (line 107) each contain exactly one Pullman mention, the same sentence, framed as a bio credential about Brandon. It is not Pullman-derived material. It goes slightly beyond a bare bio line by naming the group behind Emmer and Rye; owner may want to look.

## 5. Surprising

- `founders/capital-raise/working-files/_tmp_repr_part1_copy.md` is a byte-identical temp duplicate of `St_Elmo_Exhibit_Build_Specification_2026-08-22_part1.md` (name prefix `_tmp_`). Report only (investor material).
- Profile baselines carry Josephine as a live demand-validation and general-solicitation surface (Private_Raise_Compliance_Advisor, Market Competitive Analyst, Investor Targeting Strategist, Pitch Deck, Business Plan). The compliance profile's 506(b) logic is built on the Josephine pop-up as a public surface; cutting it changes the advice and needs a rewrite, not just a strike.
- Market Competitive Analyst profile line 10 builds its core stance ("require disproportionate demand evidence before underwriting the revenue ramp") next to the Josephine claim.
- Airtable app IDs (appKHeje63inr1fLG, appHj181Vju7No7GH) are hardcoded in the Hospitality Investment Analyst profile and in the capital-raise specs.
- No founder-only material found under `profiles/`; `founders/profiles` is correctly under founders.

## Per-file summary (HOLD-PROFILE)

| file | terms (hit-lines) |
|---|---|
| founders/profiles/_source/investment/Business_Plan_Architect_Profile.md | Josephine=1, Airtable=12 |
| founders/profiles/_source/investment/Hospitality Investment Analyst Profile.md | Airtable=19, Master Pointer Index=1 |
| founders/profiles/_source/investment/Investment Thesis Architect Profile.md | Airtable=15 |
| founders/profiles/_source/investment/Investor Targeting Strategist Profile.md | Josephine=1, Airtable=10 |
| founders/profiles/_source/investment/Investor_Design_Director_Profile.md | Airtable=2, Home Folder=1 |
| founders/profiles/_source/investment/Investor_Financial_Exhibit_Architect_Profile.md | Airtable=17 |
| founders/profiles/_source/investment/Investor_Website_Architect_Profile.md | [Ee]xperiential=1, Airtable=10 |
| founders/profiles/_source/investment/Market Competitive Analyst Profile.md | Josephine=3, Airtable=8 |
| founders/profiles/_source/investment/Operating_Systems_Futurist_Profile.md | Airtable=6, Business Strategies Notebook=1, 2ky45bmy-11873=1 |
| founders/profiles/_source/investment/Pitch_Deck_Architect_Profile.md | Josephine=1, Airtable=11 |
| founders/profiles/_source/investment/Private_Raise_Compliance_Advisor_Profile.md | Josephine=2, Airtable=10 |
| profiles/_source/design-translating-team/01_Design_Brief_Translator_Profile.md | Home Folder=1 |
| profiles/_source/design-translating-team/02_Platform_Prompt_Specialist_Profile.md | Home Folder=1 |
| profiles/_source/design-translating-team/03_Brand_Identity_Specialist_Profile.md | Home Folder=1 |
| profiles/_source/design-translating-team/04_Editorial_Layout_Specialist_Profile.md | Home Folder=1 |
| profiles/_source/design-translating-team/05_Web_UI_Specialist_Profile.md | Home Folder=1 |
| profiles/_source/design-translating-team/06_Environmental_Signage_Specialist_Profile.md | Home Folder=1 |
| profiles/_source/design-translating-team/07_Image_Campaign_Specialist_Profile.md | Home Folder=1 |
| profiles/_source/design-translating-team/08_Design_Director_Profile.md | Home Folder=1 |
| profiles/_source/design-translating-team/09_Creative_Director_Profile.md | Home Folder=1 |
| profiles/_source/design-translating-team/10_Motion_Interaction_Specialist_Profile.md | Home Folder=1 |
| profiles/_source/learning-and-development/Assessment & Competency Designer.md | Airtable=2, Business Strategies Notebook=1, 2ky45bmy-11873=1 |
| profiles/_source/learning-and-development/Curriculum & Program Architect.md | [Ee]xperiential=2, Airtable=1, Business Strategies Notebook=1, 2ky45bmy-11873=1 |
| profiles/_source/learning-and-development/Educational Materials Author and Editor.md | Airtable=1, Business Strategies Notebook=1, 2ky45bmy-11873=1 |
| profiles/_source/learning-and-development/HighScope.md | [Ee]xperiential=3, Airtable=1, Business Strategies Notebook=1, 2ky45bmy-11873=1 |
| profiles/_source/learning-and-development/Hospitality Craft Educator.md | Airtable=3, Business Strategies Notebook=1, 2ky45bmy-11873=1 |
| profiles/_source/learning-and-development/Instructional Designer.md | [Ee]xperiential=2, Airtable=1, Business Strategies Notebook=1, 2ky45bmy-11873=1 |
| profiles/_source/learning-and-development/Learner Advocate.md | Airtable=1, Business Strategies Notebook=1, 2ky45bmy-11873=1 |
| profiles/_source/learning-and-development/Practice and Simulation Designer.md | Airtable=2 |
| profiles/_source/learning-and-development/TBRI.md | Airtable=3, Business Strategies Notebook=1, 2ky45bmy-11873=1 |
| profiles/_source/narrative-and-structure/Narrative_Architect_Profile.md | Josephine=1, Airtable=2 |
| profiles/_source/people-and-culture/Culture Implementer.md | Airtable=4, Business Strategies Notebook=1, 2ky45bmy-11873=1 |
| profiles/_source/people-and-culture/Culture Signal Designer.md | Airtable=6, Business Strategies Notebook=1, 2ky45bmy-11873=1 |
| profiles/_source/people-and-culture/Emerging Leader Advocate.md | Airtable=12, Business Strategies Notebook=1, 2ky45bmy-11873=1 |
| profiles/_source/people-and-culture/Frontline Advocate.md | Airtable=12, Business Strategies Notebook=1, 2ky45bmy-11873=1 |
| profiles/_source/people-and-culture/HR Implementer.md | Airtable=7, Business Strategies Notebook=1, 2ky45bmy-11873=1 |
| profiles/_source/people-and-culture/HR Systems Designer.md | Airtable=5, Business Strategies Notebook=1, 2ky45bmy-11873=1 |
| profiles/_source/people-and-culture/Performance and Feedback Systems Designer.md | Airtable=5, Business Strategies Notebook=1, 2ky45bmy-11873=1 |
| profiles/_source/people-and-culture/Values and Belonging Designer.md | Airtable=3, Business Strategies Notebook=1, 2ky45bmy-11873=1 |
| profiles/_source/scaling-people/Hospitality Operations Realist.md | Airtable=19, Business Strategies Notebook=1, 2ky45bmy-11873=1 |
| profiles/_source/scaling-people/Organizational Systems Architect.md | Airtable=12, Business Strategies Notebook=1, 2ky45bmy-11873=1 |
| profiles/_source/scaling-people/People Systems Designer.md | Airtable=12, Business Strategies Notebook=1, 2ky45bmy-11873=1 |
| profiles/_source/voice/Gladwell_Narrative_Voice_Profile.md | Josephine=1, Airtable=6 |
| profiles/_source/voice/Graham_Clarity_Voice_Profile.md | Josephine=1, Airtable=6 |
| profiles/_source/voice/House_Voice_Brandon_Profile.md | Josephine=1, Airtable=6 |
| profiles/_source/voice/Vee_Conviction_Voice_Profile.md | Josephine=1, Airtable=5 |
(Airtable and other counts above are hit-line counts per file.)
