# Box inventory, Sŏn phase 1 cleanup (read-only, 2026-10-07)

Nothing in Box was moved, copied, deleted, uploaded or commented. All IDs are live as of this run.
Sŏn root = 382452042459. Skeleton: 00 Start Here 420129563853, 01 Company and Legal 420130633931, 02 Capital Raise 420132877311, 03 Finance 420132046817, 04 Property and Build-Out 420132927884, 05 Brand and Creative 420132086334, 06 Operations 420132292570, 07 People 420131195036, 08 Technology and Systems 420130514216, 09 Events 420132460586, 10 AI Projects 393201935562, 99 Archive 420130619940.

## Batch 1: Experiential Guidelines PDF move

| Item | ID | Current path | Size |
|---|---|---|---|
| Sŏn — Brand and Experiential Guidelines.pdf | 2281626080747 | Sŏn / 10. AI Projects / Design (388972616815) | 584,741 bytes, created 2026-06-12 |

Note: the file is named "Brand and Experiential Guidelines", not "Experiential Guidelines". It sits next to design-system folders (Fonts 388972713490, Son Design System v1.0 389659903123, v2-2026-07-18-post-corrections 401372274561, v2.1-2026-07-19-defect-fix 401373652532).

Reference-type folders found:
- Only one folder named "Reference" exists in the whole account: "03. Reference" (421597286002), created 2026-09-26, EMPTY, located at Sŏn / 10. AI Projects / Industry Digest (421598750339) / 03. Reference. It belongs to the nerve digest structure. It is not a Sŏn-root reference folder.
- No "Guidelines" folder exists. No "Reference" folder at Sŏn root or in 05. Brand and Creative.

Candidate destinations (decision needed):
- A. 05. Brand and Creative / Identity and Design Assets, ID 420132746170 (empty, path Sŏn / 05. Brand and Creative / Identity and Design Assets). Best structural fit if the PDF is treated as a brand asset.
- B. 03. Reference, ID 421597286002. Name fits "reference file in Box", but it is under Industry Digest and the digest owns it. Only use if Brandon wants it there.
- C. Create a new "Reference" folder under 05. Brand and Creative (420132086334) or 00. Start Here (420129563853). Needs a create_folder, which is a write.

Proposed action: move file 2281626080747 to option A (420132746170), pending Brandon's choice. Tiebreak: CLAUDE.md says it is "a reference file in Box, never guidelines", so a Reference-named folder (option C) matches the label better than "Identity and Design Assets".

## Batch 2: Pullman LnD Import folder decision

Folder 400222760917, path Sŏn / 10. AI Projects / Research (388976730865) / Pullman LnD Import. Created 2026-07-15 13:51, last modified 13:55, by Brandon. Total size 222,008 bytes. Siblings in Research: Design Translator Research Runner 388973998929, Scaling People 399477650322.

Contents (one subfolder, 4 files, all created 2026-07-15):

| Name | Type | ID | Size |
|---|---|---|---|
| SOP Generator Project | folder | 400221385460 | (222,008 total) |
| Instructions.md | file | 2348831195527 | 2,917 |
| SOP Project Parameters.md | file | 2348839223795 | 18,445 |
| SOP Template.md | file | 2348831701923 | 27,359 |
| Universal Host Handbook from Claude.pdf | file | 2348829885162 | 173,287 |

What it is: a copy of Brandon's Pullman Market SOP document-builder project (a Claude project that builds branded PDF SOPs with ReportLab). Instructions.md opens "Pullman Market SOP Document Builder ... Pullman Market hospitality SOPs", pulls copy from a ClickUp doc "Updated SOP's" (2ky45bmy-13813). SOP Project Parameters.md is the spec: banners and colors for Pullman Market, Isidore, Mezquite, Fife & Farro, Nicosi (five Pullman-group concepts), subtitle "PULLMAN MARKET · SAN ANTONIO", Canva brand kit IDs. Universal Host Handbook PDF is the Pullman host handbook output (not opened, name only). SOP Template.md not opened.

Derived-from or referencing hits (keyword "Pullman", "Universal Host Handbook", "SOP Generator" across Sŏn tree):
- Nothing in Box references the import folder by name or ID. The "Universal Host Handbook" and "SOP Generator" searches returned only unrelated files (Airtable export CSVs matched on loose terms such as Labor / Positions; no true derivative). Box content search only indexes text, so scanned or image-only PDFs could be missed.
- "Pullman" hits (4 files, 2 distinct documents, each in two copies):
  - 03. Sŏn Investor Diligence White Paper .pdf, 2468611192111, in 02. Capital Raise / 01. Investor Room Template (418384888111); copy 2468627027608 in 03. Investor Rooms / Adam Biechlin (418386765208). Context: "He consulted at Pullman Market with the group behind Emmer and Rye." That is a bio credential line, allowed.
  - 02. Sŏn Deck for 207 St. Elmo.pdf, 2468611194511 (Investor Room Template) and 2468627030008 (Adam Biechlin room), 19 MB. Matched on Pullman but I did not read it (too large; context not verified). Probably the same bio line. Check before concluding.
- Flag: the import folder itself is entirely Pullman Market IP and workflow, well beyond a bio credential. It is out of scope per CLAUDE.md and should not be carried over. It also contains ClickUp doc IDs and Canva kit IDs belonging to Pullman.

Proposed action (Brandon decides): remove from the Sŏn tree, either (a) delete 400222760917, or (b) move to a holding location outside Sŏn if he wants to keep a copy. Do not archive into 99. Archive (its own rule: "Non-Sŏn material never goes here"). Destination ID: none within Sŏn. No move is proposed to any Sŏn folder. Ask before delete (irreversible).

## Batch 3: Temp duplicate removal

- 2421148304456 `_tmp_repr_part1_copy.md`: path Sŏn / 10. AI Projects / Profiles (393577233571) / Investment (394310934375). 54,782 bytes, created 2026-08-22 17:25:44.
- Compared with 2421087690801 `St_Elmo_Exhibit_Build_Specification_2026-08-22_part1.md` in the same folder: 54,782 bytes and identical SHA1 `7de3cdb584e5c78866985c7c640891d48386076f`. It is a byte-identical duplicate.
- Proposed action: delete 2421148304456 (keep 2421087690801). Destination: none (trash). Safe, exact duplicate.

## Batch 4: Exhibit working files move (Profiles/Investment)

Folder 394310934375, 18 items, path Sŏn / 10. AI Projects / Profiles (393577233571) / Investment.

Actual profiles (11, stay; the Profiles folder is a read-only mirror of repo `profiles/`):
- Business_Plan_Architect_Profile.md 2311338205772
- Hospitality Investment Analyst Profile.md 2311218248473
- Investment Thesis Architect Profile.md 2311126794221
- Investor Targeting Strategist Profile.md 2311260661466
- Investor_Design_Director_Profile.md 2311941937676
- Investor_Financial_Exhibit_Architect_Profile.md 2400758223703
- Investor_Website_Architect_Profile.md 2311835178755
- Market Competitive Analyst Profile.md 2311222490205
- Operating_Systems_Futurist_Profile.md 2323405221445
- Pitch_Deck_Architect_Profile.md 2311331236649
- Private_Raise_Compliance_Advisor_Profile.md 2311367061082

Exhibit working files and review artifact (6, to move) plus duplicate (1, Batch 3):

| Name | ID | Size | Modified |
|---|---|---|---|
| St_Elmo_Classification_Appendix_2026-08-22_part1.md | 2421061537634 | 37,256 | 2026-08-22 |
| St_Elmo_Classification_Appendix_2026-08-22_part2.md | 2421037947695 | 34,921 | 2026-08-22 |
| St_Elmo_Classification_Main_2026-08-22.md | 2421062202959 | 33,984 | 2026-08-22 |
| St_Elmo_Exhibit_Build_Specification_2026-08-22_part1.md | 2421087690801 | 54,782 | 2026-08-22 |
| St_Elmo_Exhibit_Build_Specification_2026-08-22_part2.md | 2421093539322 | 61,879 | 2026-08-22 |
| Son Investor Materials - Internal Review.md | 2448024798796 | 12,867 | 2026-09-05 (v2) |
| _tmp_repr_part1_copy.md | 2421148304456 | 54,782 | see Batch 3 |

Destination candidates (all under 02. Capital Raise 420132877311):
- Best: 02. Capital Raise / 00. Pitch Materials (388972799337) / Investment (420133510941). Currently holds only "Investor Liquidity Disclosure" (415085423749), the investor disclosure. Create a subfolder such as "Exhibit Working Files" there, or move straight in.
- Alternative: 02. Data Room Master (420131540465), empty, but investor-facing in intent; working files do not belong there.
- Alternative for the Internal Review only: it is an internal review artifact ("Keep this review internal"). Box routing says Box holds review artifacts, so it can sit with the exhibit files in 420133510941 or stay put. Not investor-visible; do not place anywhere an investor room can reach.

Proposed action: move the 5 St_Elmo_* files and the Internal Review to 420133510941 (or a new subfolder inside it). Needs Brandon's confirm of destination; a create_folder is a write.

## Batch 5: Other out-of-scope hits (keyword searches across Sŏn tree, limit 200)

| Term | Hits | Detail |
|---|---|---|
| Josephine | 0 | none |
| June Shim | 0 | none |
| Sanctuary | 0 | none |
| Event Co | 0 | none |
| Pullman | 4 files | see Batch 2 (bio credential in White Paper; deck not verified) |
| Airtable | 18 | listed below |

Caveat: Box search is full text only on indexed text. Zero hits means nothing indexed; scanned PDFs and the 19 MB deck are not guaranteed covered. Folder-name matches count as hits.

Airtable, top 10 of 18 (all in 99. Archive / St. Elmo Dashboard V2 420664079734 / 2026-09-22 Airtable Export 420667891155 unless noted):
1. 03 Airtable Documentation (folder) 420666087682
2. 2026-09-22 Airtable Export (folder) 420667891155
3. 50 — Refresh — Assumptions.csv 2483963063180 (01 CSV Tables 420667195052)
4. START HERE.txt 2483964153516 (export root)
5. README.txt 2483958366284 (export root)
6. 01 — P&L Model.csv 2483963740551 (01 CSV Tables)
7. Start Here.md 2480417968712 at Sŏn / 00. Start Here. Context: states "Financial figures live in Airtable", the opposite of CLAUDE.md (Airtable retired; workbook only). Stale routing rule.
8. Field Reference.html 2483959365538 (03 Airtable Documentation)
9. 02. Sŏn Deck for 207 St. Elmo.pdf 2468627030008 (Capital Raise / 03. Investor Rooms / Adam Biechlin 418386765208)
10. 02 — Years 1-5 Projections.csv 2483959312738 (01 CSV Tables)
Remaining 8: 37 Model Assumptions.csv, 35 Lease Rent Burden Analysis.csv, St. Elmo Dashboard V2.xlsx (2483953451169, 00 Readable Archive), 02. Sŏn Deck (Investor Room Template copy 2468611194511), records.json, schema.json, VERIFICATION REPORT.json, 03 Scenario Configurator.csv.

Proposed action: no Airtable file needs moving, the export is correctly in 99. Archive. Update Start Here.md (2480417968712) rule text; that is an edit, not performed. No Batch 5 items for Josephine / June Shim / Sanctuary / Event Co. Nothing to move.

## Surprises
1. Start Here.md (00. Start Here) still routes financial figures to Airtable. Contradicts CLAUDE.md. It is also dated 2026-09-21 and mentions a "!! DELETE - Review and Remove" folder at root, which does not exist at Sŏn root now.
2. The Internal Review (2026-09-05) says Profiles/Investment held 17 files including "one exact duplicate" of an older doc; there are now 18 (the Review itself added). The duplicate it names is likely _tmp_repr_part1_copy.md (created 2026-08-22), confirmed identical.
3. The only "Reference" folder is empty and lives under Industry Digest, so the PDF has no ready-made reference home.
4. Pullman LnD Import is clearly Pullman Market operational IP (five Pullman-group concepts), not a bio line.
5. Several Box folders returned empty (Claude 420131528486 under 08, Data Room Master, Decks 420132537139, Identity and Design Assets), consistent with a skeleton still being filled, but "AI Projects / Claude" being empty conflicts with Start Here.md saying it is moved last.
6. Two copies each of the Deck and White Paper exist (Investor Room Template and Adam Biechlin room), same sizes.
