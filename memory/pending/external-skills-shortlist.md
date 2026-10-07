# External skills and plugins: shortlist (pending, not agreed)

Searched 2026-10-07: Brandon's claude.ai plugin directory, account skills (none installed), anthropics/skills. Decide per item in phase 2 or 4. Rule for anything adopted: install at project scope for `son`, read its hooks before installing (hooks run code in every session and can collide with the build-out guard), and never add a second memory system.

## Strong fit
- skill-creator (Anthropic, claude-plugins-official): builds skills and runs evals on them. Phases 2 and 4 build about ten skills.
- Document skills (Anthropic, anthropics/skills `document-skills`): docx, xlsx, pdf, pptx. Box finals, the Investor Review workbook, PDFs.

## Worth testing, as tools or as raw material for our own skills
- Operations (Anthropic, knowledge-work-plugins): process-doc, runbook, risk-assessment, compliance-tracking, vendor-review, change-request. SOPs and vendor evaluation (phase 5).
- Human Resources (Anthropic, knowledge-work-plugins): onboarding, performance-review, comp-analysis, policy-lookup, draft-offer, org-planning. Maps to operations chunks 3.3, 5.4, 5.5. Harsh red team; Texas law not built in.
- Legal (Anthropic, knowledge-work-plugins): review-contract, triage-nda, vendor-check, compliance-check. Lease and vendor contracts; not legal advice.
- Design (Anthropic, knowledge-work-plugins): design-critique, design-system, accessibility-review, ux-copy, design-handoff. Design-system workstream.
- Brand Voice (Tribe AI, partner, in knowledge-work-plugins): discover voice from documents, generate guidelines, enforce. Compare against the House voice profiles in phase 3.

## Read for design ideas, do not install
- memory-toolkit (community): park, session-end, session-continue. Ideas for phase 2 session basics; installing it would create a second memory system.
- ClickUp plugin (by ClickUp): task-decomposition skill. Ideas for task-tree; its connector duplicates the existing one.

## Skip for now
- Other memory plugins (memory-agent, oak-memory, Kumiho, Mnemoverse, notion-memory, Productivity): duplicate the repo memory; several send data to outside services.
- Code review and security plugins: little code yet; revisit for nerve and the design system.
- Marketing and Product Marketing: revisit when Robert's promotion work starts.
- research-superpowers (community): heavy; possible later fit for science.
