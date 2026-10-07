

# How This Works

# Sŏn — Master Pointer Index & Inventory

**Purpose.** Single source of truth for every resource that lives _outside_ Claude and can be pointed to and used in a session. Any Claude chat, and any collaborator, uses this doc to locate a resource, see which connector reaches it, and pull it.

**Why this exists (the thin-project model).** Claude Projects degrade when their knowledge base is stuffed with files: retrieval flips from full-context loading to lossy chunk-search. So the project knowledge stays near-empty and _points_ outward instead. This doc is the map. The territory (financials, strategy, profiles, assets) stays in Airtable, ClickUp, and Box.

## The two layers

1. **Bootstrap pointers** — a roughly 12-line block living in Claude project knowledge. Only near-static IDs: the Airtable bases, the top-level Box folder, and the ID of _this_ doc. Always loaded, zero connector hops. The canonical copy is on the "Bootstrap Block" page.
2. **This inventory (living)** — the full registry, maintained by hand here. Everything the bootstrap cannot hold because it changes.

The bootstrap is deliberately tiny. The smaller it is, the less it can drift from this master. Anything that changes often lives only here.

## Routing rules

*   **Financial data → Airtable.** Always query Airtable. Never generate, estimate, or repeat a financial figure from memory or a deck.
*   **Living truth (detailed strategy, anything that changes) → ClickUp.**
*   **Profiles and frozen / non-living assets (decks, PDFs, design exports) → Box.**
*   **Thin operating layer → Claude project knowledge** (bootstrap only).
*   Design flow: Claude Design → export to Canva → if a frozen version is needed, it lands in Box.

## Profile Update Protocol (standing rule)

Box holds the single canonical copy of every profile. Profiles are never edited in place inside a chat, and never duplicated across locations. When a profile changes:

1. Replace the file in Box (Box version history retains the prior version).
2. Add a row to the **Profile Replacement Queue** (page in this doc) flagging the file as updated.
3. Any session using that profile pulls the current Box file; any attached or cached copy elsewhere is refreshed.

A profile is not "updated" until the Box file is replaced and the queue row is logged. The reason: a connector or an attached copy does not auto-sync when the Box source changes. The queue is the manual trigger that catches stale copies.

## How a session uses this doc

1. Enable only the connector(s) the task needs (avoid context bloat).
2. Read the bootstrap (in project knowledge).
3. If the full map is needed, open this doc.
4. Locate the resource, confirm the connector, pull it.

* * *

_Maintained by: Brandon. Shared with: Dominic. Last structural update: 2026-06-24._

# Resource Registry

One row per resource. Rows marked **(verify)** were seeded from prior context — confirm the ID or path before relying on them. Box profile and asset rows are placeholders until folders are shared, except the clusters marked live in Box.

## Financials — Airtable

_Always query. Never generate figures._

| Resource | Pointer (base / table) | Connector | Status | What it's for |
| ---| ---| ---| ---| --- |
| Sŏn — St. Elmo Dashboard V2 (primary) | `appKHeje63inr1fLG` | Airtable | live-confirmed | Primary build base: CapEx, pre-opening |
| — CapEx LHI table | `tbliWim640bYKSHTx` | Airtable | (verify) | Leasehold improvement line items |
| — Pre-Opening Expenses table | `tblmtmB8y8eXy5B8E` | Airtable | (verify) | Pre-opening spend |
| Sŏn — Investor Dashboard | `appHj181Vju7No7GH` | Airtable | live-confirmed | Investor-facing figures |
| The Josephine — Josephine Events | `appn6pvhGYucER0kh` | Airtable | live-confirmed | Josephine events financials |

_Deprecated (do not use): Project Costs & Operations_ _`appKxSKKjCTBquec6`_, 207 St. Elmo Pro Forma _`appen66O5mpio3EYT`_.

## Living Strategy & Working Docs — ClickUp

**Spaces**

| Space | ID |
| ---| --- |
| Founding Sŏn | `90138396180` |
| Technology | `90136733924` |
| Design & Visuals | `90136725596` |
| Operations | `90136733940` |
| People | `90136734650` |
| Finance | `90136733856` |
| Promotion | `90136688132` |
| Product | `901312138543` |
| Property | `90136733959` |
| Hospitality | `90136733933` |
| Business Intelligence | `90136734098` |
| Research | `90136698720` |
| Events | `90136733952` |
| The Josephine | `901313832794` |

**Key docs**

| Doc | ID | What it's for |
| ---| ---| --- |
| Brand Guidelines (Sŏn canon) | `2ky45bmy-15773` | Brand system source of truth |
| Business Strategies Notebook | `2ky45bmy-11873` | Strategic source of truth. Current version V7.0 (The Founders plus Parts I–V: The Foundation, The Organization That Compounds, The Customer That Compounds, The Brand That Compounds, The Platform). V1.0–V6.0 archived within the doc |
| Pitch Scripts | `2ky45bmy-13213` | Investor pitch scripts (some outdated) |
| Romero Study Guide | `2ky45bmy-14073` | Investor study materials |
| Claude System & Profile Methodology (Research Capture) | `2ky45bmy-16853` | Foundational research; seven-stage synthesis procedure on the Actionable Distillation page; also holds the Verified Market Claims page |
| Claude Project Review (migration source) | `2ky45bmy-16873` | The three projects being consolidated; Design Translator knowledge corpus |
| This doc — Master Pointer Index | `2ky45bmy-16833` | The map |
| Sŏn Operating Layer (Dominic handoff) | `2ky45bmy-17113` | Dominant technology position document; single page at 2ky45bmy-29573. Created and last edited 2026-06-30, no revision since; this is the specification date the operating layer program bounds its change checks against. Carries OmniAlert, which is a typo for Omnilert |
| Tech OS Build Hub | `2ky45bmy-17093` | Internal working source: Coqodaq bandwidth map, Synthesis 1, brain-dump batches, agent decision |
| Operating Layer Program Tracker | `2ky45bmy-17313` | Research, diligence, and build program for the technology layer. Program state, counsel queue, handoffs out, findings and method changes. Evidence lives in a local git repo run through Claude Code; review artifacts sync to Box folder `402905521507` |
| Sŏn Operating System | `2ky45bmy-17253` | The company operating system, built one page per session by the Scaling People program |
| Scaling People tracker | `2ky45bmy-17233` | Scaling People translation program: rebuild stop block, session map, decisions log, carryover |
| Learning & Development / People & Culture build tracker | `2ky45bmy-17273` | The two employee-facing profile clusters: purpose, roster, constraints, build status |

## Venture coordinates

**Sŏn** — Korean fine dining, 207 E St. Elmo Rd, Austin.

*   Financials: St. Elmo Dashboard V2 `appKHeje63inr1fLG`, Investor Dashboard `appHj181Vju7No7GH`
*   Brand canon: Brand Guidelines doc `2ky45bmy-15773`
*   Profiles + assets: Box — Sŏn Home Folder → Claude → Profiles

**The Josephine** — pop-up events, luxury apartment complex, San Antonio. Book-of-business play for investor credibility.

*   Living strategy: ClickUp space `901313832794`
*   Financials: Airtable base `appn6pvhGYucER0kh`
*   Assets: Box — TBD (no folder yet)

## Profiles — Box

_One row per profile, grouped by cluster. Clusters marked live in Box are built. Others populate as they are built._

**Voice cluster** — writing and persuasion. Each profile is dual-mode (generate or critique). Default to House for any investor- or audience-facing writing.

| Profile | Box path | Domain cluster | Status | What it's for |
| ---| ---| ---| ---| --- |
| House Voice (default) | `/Sŏn/.../Profiles/Voice/House_Voice_Brandon_Profile.md` | Voice | live in Box | Brandon's blended voice; default for all writing. Opens narrative, proves with rigor, closes with conviction. Moves the whole room |
| Gladwell Narrative Voice | `/Sŏn/.../Profiles/Voice/Gladwell_Narrative_Voice_Profile.md` | Voice | live in Box | Narrative and emotional resonance. Moves hearts. Opens and frames |
| Graham Clarity Voice | `/Sŏn/.../Profiles/Voice/Graham_Clarity_Voice_Profile.md` | Voice | live in Box | Compression, clarity, diligence pass. Moves wallets. Proves the business and rigor-checks the other voices before anything ships to an investor in writing |
| Vee Conviction Voice | `/Sŏn/.../Profiles/Voice/Vee_Conviction_Voice_Profile.md` | Voice | live in Box | Conviction and momentum. Moves brains, drives action. The close and the rally. Profanity spoken-only, never in text without an explicit per-piece override |

**Investment cluster** — raise and business plan. Ten profiles, all live in Box. Standing rules baked into every profile: figures from Airtable only, tipless service model never asserted, labor always a range, no em dashes, "customer" never "guest," declarative over aspirational, brand facts deferred to Brand Guidelines `2ky45bmy-15773`.

| Profile | Box file ID | Status | What it's for |
| ---| ---| ---| --- |
| Investment Thesis Architect | — | live in Box | Keystone thesis; durable core plus re-weightable layer |
| Hospitality Investment Analyst | — | live in Box | Bottom-up revenue reconciliation, prime cost and DSCR, labor as a range |
| Market and Competitive Analyst | — | live in Box | Demand gate, three-ring competitive set, premium-Korean-Austin read |
| Investor Targeting Strategist | — | live in Box | Archetype-to-structure mapping, anchor-first sequencing |
| Pitch Deck Architect | `2311331236649` | live in Box | Deck format rubric and critique checklist |
| Business Plan Architect | `2311338205772` | live in Box | Business-plan format rubric; plan as diligence artifact |
| Private-Raise Compliance Advisor | — | live in Box | Reg D lens, not legal advice; lane before solicitation |
| Investor Website Architect | `2311835178755` | live in Box | Information architecture and funnel mechanics; three-tier withhold |
| Investor Design Director | `2311941937676` | live in Box | Design direction for the investor context |
| Operating Systems Futurist | `2323405221445` | live in Box | Technology position advocacy; trajectory and inevitability argument |

**Design Translating Team cluster** — nine profiles, all live in Box. Triggered automatically for any AI design-tool prompt. Standing rules baked in: no AI-generated imagery on any public surface, no em dashes, "customer" never "guest," declarative, brand facts deferred to Brand Guidelines. Knowledge corpus in ClickUp `2ky45bmy-16873`.

| Profile | Box file ID | Status |
| ---| ---| --- |
| 01 Design Brief Translator | `2311618340994` | live in Box |
| 02 Platform Prompt Specialist | `2311675286153` | live in Box |
| 03 Brand Identity Specialist | `2311675667006` | live in Box |
| 04 Editorial & Layout Specialist | `2311732945842` | live in Box |
| 05 Web & UI Specialist | `2311742214337` | live in Box |
| 06 Environmental & Signage Specialist | `2311747672593` | live in Box |
| 07 Image & Campaign Specialist | `2311750053271` | live in Box |
| 08 Design Director | `2311756458976` | live in Box |
| 09 Creative Director | `2311969448994` | live in Box |

**Scaling People cluster** — three profiles, live in Box, folder `400727361228`. The team that runs the Scaling People translation program. Each holds the rebuild frame (her-ask, Sŏn-holds, gap, decision), holds V7 as landed, marks rather than lands, and cross-references the others and the L&D and P&C clusters by Box file ID. Standing rules baked in: figures from Airtable only, customer never guest, no em dashes, declarative, no daypart code names, brand facts deferred to canon, profanity spoken-only.

| Profile | Box file ID | Owns | What it does |
| ---| ---| ---| --- |
| Organizational Systems Architect | `2352980282301` | Her Ch1, Ch2; the progression structure | Is the structure sound. Reads flow not chart. Dignan, Laloux, Edmondson, Hamel, Ashby |
| People Systems Designer | `2353165009738` | Her Ch3, Ch4, Ch5; psychological safety as org theory | Does the system produce the behavior it intends. Bock, Ton, Edmondson, Amabile, Scott |
| Hospitality Operations Realist | `2353380918688` | Cross-cutting tempo test across all chapters | Does it survive a Friday at 8:15 run by hourly staff. Keller, Bourdain, Guidara, Meyer |

**Learning & Development cluster** — seven profiles, live in Box, folder `400224498698`. The faculty that builds Sŏn's employee education as real pedagogy, degree paths not handoff docs. HighScope and TBRI are Brandon-supplied frameworks, each a dedicated seat. Standing rules baked in as above.

| Profile | Box file ID | Status |
| ---| ---| --- |
| Curriculum & Program Architect | `2349344483137` | live in Box |
| Instructional Designer | `2349382165394` | live in Box |
| Assessment & Competency Designer | `2349454588688` | live in Box |
| Educational Materials Author and Editor | `2349696639860` | live in Box |
| Learner Advocate | `2351610057004` | live in Box |
| HighScope | `2352049266786` | live in Box |
| TBRI | `2352103096330` | live in Box |

**People & Culture cluster** — eight profiles, live in Box, folder `400281721352`. The team for HR systems, performance and feedback, values and belonging, and culture as lived and administered. Sits downstream of the Scaling People People Systems Designer, which designs the machine; this cluster expresses it as employee-facing material. Standing rules baked in as above.

| Profile | Box file ID | Status |
| ---| ---| --- |
| HR Systems Designer | `2349736312546` | live in Box |
| HR Implementer | `2351472764828` | live in Box |
| Performance and Feedback Systems Designer | `2351121277228` | live in Box |
| Values and Belonging Designer | `2349793626447` | live in Box |
| Culture Signal Designer | `2351058484688` | live in Box |
| Culture Implementer | `2351549543759` | live in Box |
| Frontline Advocate | `2351902883096` | live in Box |
| Emerging Leader Advocate | `2351989463067` | live in Box |

**Reference, not grounding** — folder `400222760917` (Pullman LnD Import, under Claude / Research). Brandon's Pullman Market consulting prior-art. Used only as context for what profile seats the roster needed. Not a content source, not a template, not part of any build pipeline. Do not point a build at this folder as a source.

**Sŏn specialist roster** — to build. `/Sŏn/.../Profiles/Specialists/`. Brand and operational specialist profiles.

## External Assets — Box

_Decks, PDFs, design exports, specialist source corpora._

**Investor white papers** — folder `382453064958` ("Son - White Paper(s)"). Markdown source. Three archetype-tuned diligence papers in the Graham voice plus two general-use voice versions. All carry the two-engines thesis, figures from the model, the verified market claims, and the brand rules. Regenerate after Dom's tech-layer redefinition lands.

| Asset | Box file ID | Type | Status |
| ---| ---| ---| --- |
| Sŏn White Paper — Hospitality Capital | `2312023984117` | White paper (md) | live in Box |
| Sŏn White Paper — Private Capital | `2312070844315` | White paper (md) | live in Box |
| Sŏn White Paper — Venture | `2312072378071` | White paper (md) | live in Box |
| Sŏn White Paper — General (Vee voice) | `2312884955641` | White paper (md) | live in Box |
| Sŏn White Paper — General (Gladwell voice) | `2312878982250` | White paper (md) | live in Box |

**Operating Layer** — folder `402905521507`, under Claude. Review artifacts for the technology research, diligence, and build program. Tracker at ClickUp `2ky45bmy-17313`. Sessions sync here; the evidence itself lives in a local git repo.

| Folder | Box folder ID | What it holds |
| ---| ---| --- |
| Registry digests | `402905624494` | Milestone snapshots of the full vendor registry, uploaded manually by the operator at category 5 and category 12 |
| Session records | `402905047135` | Gap lists, change checks, counsel queue, validation reports, diligence instruments |

_Other assets (decks, design exports, frozen PDFs): paths to be added as folders are shared._

# Profile Replacement Queue

The operational flag for the Profile Update Protocol. When a profile's Box file is replaced, log it here so any stale attached or cached copy gets refreshed. This page is permanent (it does not retire with the review).

| Profile | Updated (date) | What changed | Box file / path | Status | Refreshed in active sessions? | Notes |
| ---| ---| ---| ---| ---| ---| --- |
| House Voice (Brandon) | 2026-07-05 | Redefined from a Gladwell-default blend into a three-seat room. Vee promoted from a close-only instrument to a standing seat that selects the high-traction, most-resonant beats and pushes conviction on them. Graham widened from the money-and-proof pole to positioning filter and refiner, finding the load-bearing claim and cutting what does not ladder to it. Gladwell holds tone, narrative, and the tonal default. All global hard rules and inherited guardrails carried unchanged. | `/Sŏn/Claude/Profiles/Voice/House_Voice_Brandon_Profile.md` (Box id `2308894143877`) | Pending | No attached copy; auto-refreshes on next fetch. This chat's context retains the pre-update version. | Voice cluster keystone, the default voice. Per Brandon spec 2026-07-05. |
| Operating Systems Futurist | 2026-07-02 | Initial build — research-then-synthesis method; anchored in Kelly ("The Inevitable"), McAfee/Brynjolfsson (frontier-laggard gap), Dignan ("Brave New Work"), Evans (adoption-as-transformation), Moore ("Crossing the Chasm"), Andreessen ("Software Is Eating the World"); NRA 2026 restaurant tech adoption data | `/Sŏn/Claude/Profiles/Investment/Operating_Systems_Futurist_Profile.md` (Box id `2323405221445`) | Replaced | Yes | Live in Box. Investment cluster Profile 10. Type 3 strategic advisor. Technology position advocacy, trajectory and inevitability argument, direction-not-complexity framing, objection diffusion, blank-page advantage, OS-level vs feature-level distinction, pitch-room readiness evaluation. Anchored to operating layer doc 2ky45bmy-17113 and V4.0 doc 2ky45bmy-11873 |
| Investment Thesis Architect | 2026-06-26 | Initial build (Profile 1 of 7, Investment cluster) | `/Sŏn/Claude/Profiles/Investment/Investment_Thesis_Architect_Profile.md` | Replaced | Yes | Live in Box |
| Hospitality Investment Analyst | 2026-06-26 | Initial build (Profile 2 of 7) | `/Sŏn/Claude/Profiles/Investment/Hospitality_Investment_Analyst_Profile.md` | Replaced | Yes | Live in Box |
| Market and Competitive Analyst | 2026-06-26 | Initial build (Profile 3 of 7) | `/Sŏn/Claude/Profiles/Investment/Market_and_Competitive_Analyst_Profile.md` | Replaced | Yes | Live in Box |
| Investor Targeting Strategist | 2026-06-26 | Initial build (Profile 4 of 7) | `/Sŏn/Claude/Profiles/Investment/Investor_Targeting_Strategist_Profile.md` | Replaced | Yes | Live in Box |
| Pitch Deck Architect | 2026-06-26 | Initial build (Profile 5 of 7) | `/Sŏn/Claude/Profiles/Investment/Pitch_Deck_Architect_Profile.md` | Replaced | Yes | Live in Box |
| Business Plan Architect | 2026-06-26 | Initial build (Profile 6 of 7) | `/Sŏn/Claude/Profiles/Investment/Business_Plan_Architect_Profile.md` | Replaced | Yes | Live in Box |
| Private-Raise Compliance Advisor | 2026-06-26 | Initial build (Profile 7 of 7) | `/Sŏn/Claude/Profiles/Investment/Private_Raise_Compliance_Advisor_Profile.md` | Replaced | Yes | Live in Box |
| Investor Website Architect | 2026-06-26 | Initial build — research-then-synthesis method; sourced from investor-funnel, hospitality-raise, withhold-mechanic, and data-room research | `/Sŏn/Claude/Profiles/Investment/Investor_Website_Architect_Profile.md` (Box id `2311835178755`) | Replaced | Yes | Live in Box. Investment cluster Profile 8. Three-tier withhold, funnel mechanics, one job per page |
| Investor Design Director | 2026-06-26 | Initial build — research-then-synthesis method; sourced from Matte/Gentle Monster/Kinfolk/silent-confidence design-DNA research | `/Sŏn/Claude/Profiles/Investment/Investor_Design_Director_Profile.md` (Box id `2311941937676`) | Replaced | Yes | Live in Box. Investment cluster Profile 9. Spatial sequencing, autoplay film, four-lever override, silent-confidence register |
| Creative Director | 2026-06-26 | Initial build — research-then-synthesis method; sourced from senior CD practice, luxury brand creative direction, and AI-workflow CD role research | `/Sŏn/Claude/Profiles/Design Translating Team/09_Creative_Director_Profile.md` (Box id `2311969448994`) | Replaced | Yes | Live in Box. Design Translating Team Profile 09. Standing member. Judgment over craft, subtractive irreducibility, point-of-view keeper, AI-abundance editor |

**Status values**

*   **Pending** — Box file replaced; downstream copies (attached or cached) not yet refreshed.
*   **Replaced** — all known copies refreshed; profile fully updated.

A profile is not considered updated until its row here reads **Replaced**.

# Migration & Review Tracker (Temporary)

Active during the profile and knowledge review only. One row per existing item across all external Claude projects (Homebase, Design Translator, and the others). When review closes and approved versions are organized in Box, this page retires: each item's Verdict resolves, approved items move into the **Resource Registry**, and retired items are archived.

| Source project | Resource | Type | Verdict | Target location | Reviewer notes | Done? |
| ---| ---| ---| ---| ---| ---| --- |
| Homebase | e.g. Brand Strategist profile | Profile | — | Box: /path | — | ☐ |
| Design Translator | e.g. Gladwell Style filter | Profile | — | Box: /path | — | ☐ |

**Type**: Profile · Knowledge file · Asset

**Verdict**

*   **Keep** — approved as-is, migrate to Box.
*   **Revise** — edit, then approve and migrate.
*   **Re-research** — rebuild via the synthesis procedure (NotebookLM grounding → CTA extraction → typed template → adversarial validation).
*   **Retire** — archive, do not migrate.

**Workflow**: organize and classify all items here → resolve verdicts → place approved/updated versions in Box → archive the source projects → retire this page.

# Bootstrap Pointers (reference — see Custom Instructions)

**Superseded by the Custom Instructions page.** Now that the project's custom instructions carry all pointers and rules, there is no need for a separate bootstrap file in project knowledge. **Project knowledge stays empty.** Paste the Custom Instructions page into the project's instruction field; that is the single operating layer.

Retained below as a quick-reference pointer list (multi-venture):

```
# Operating Layer — Pointers (reference)
# Full living inventory: ClickUp Master Pointer Index doc 2ky45bmy-16833

FINANCIALS (Airtable) — always query, never generate:
  Sŏn — St. Elmo Dashboard V2 (primary): appKHeje63inr1fLG
  Sŏn — Investor Dashboard:              appHj181Vju7No7GH
  The Josephine — Josephine Events:      appn6pvhGYucER0kh

LIVING STRATEGY (ClickUp):
  The Josephine space: 901313832794
  Sŏn: multiple spaces (see Master Inventory)

BRAND CANON (Sŏn): ClickUp doc 2ky45bmy-15773 (Brand Guidelines) — source of truth

PROFILES + ASSETS (Box):
  Profiles: Sŏn Home Folder -> Claude -> Profiles
  The Josephine assets: TBD (no folder yet)

CONNECTORS: enable only what the task needs (Airtable / ClickUp / Box).
```

# Consolidated Project — Custom Instructions (paste into project)

This is the canonical copy of the consolidated project's custom instructions. Paste the block below into the new Claude Project's instruction field. Dominic mirrors from this same page. Update here first, then update the project.

The project is a single thin operating layer for all current ventures. It holds almost no files. It points outward.

* * *

```
# Operating Layer — All Ventures

## What this project is
This is the single operating layer for all current ventures. It holds almost no files. It points outward: financials in Airtable, living strategy in ClickUp, profiles and frozen assets in Box. Pull what a task needs. Do not load knowledge into this project.

## Start of every session
1. Identify the active venture (Sŏn or The Josephine). If unclear, ask.
2. Enable only the connectors the task needs (Airtable / ClickUp / Box). Keep the rest off. Enable "Load tools when needed."
3. For the full resource map, open the Master Pointer Index (ClickUp doc 2ky45bmy-16833).

## Routing (all ventures)
- Financial figures: query Airtable. Never generate, estimate, or repeat a number from memory or a deck. If the table is not accessible, say so rather than substituting.
- Living strategy and working docs: ClickUp.
- Profiles and frozen assets (decks, PDFs, design exports): Box.
- When a fact might have changed, pull it live rather than recalling it.

## Working with profiles
- Profiles live in Box: Sŏn Home Folder -> Claude -> Profiles.
- Profiles are organized in clusters: Voice (writing and persuasion), Investment (raise and business plan), Design Translator (triggered set), and the Sŏn specialist roster. Fetch the cluster a task needs.
- To activate a specialist, fetch or attach the current Box file. Never edit a profile in-chat.
- Updating a profile follows the Replacement Queue protocol (Master Pointer Index): replace the Box file, log the queue row, refresh any attached copy.
- Building a NEW profile follows the seven-stage synthesis procedure (Research Capture doc 2ky45bmy-16853, Actionable Distillation page). Research targets the role's judgment, not a survey of its field.

## Voice system (writing and persuasion)
For any investor- or audience-facing writing or persuasion, default to the House voice. It is Brandon's own blended voice, not an outside author. Four voices live in Box (Profiles/Voice), each dual-mode (generate or critique):
- House — Brandon's native blend and the default. Opens with narrative, proves with rigor, closes with conviction. Selects and braids the three registers below to fit the moment.
- Gladwell — narrative and emotional resonance. Moves hearts. Opens and frames.
- Graham — compression, clarity, and a diligence pass that refuses unsourced claims or skipped steps. Moves wallets. Proves the business, and rigor-checks the other voices before anything ships to an investor in writing.
- Vee — conviction and momentum. Moves brains, drives action. The close, the rally, the room.
Invoke a single pole when the moment is purely that register; otherwise House selects and braids. Run critique mode to audit existing copy against the voice and its failure modes.
Global hard rule: profanity is spoken-only. It never appears in written output, in any voice, unless Brandon gives an explicit per-piece override. Default off, always.

## Design prompt trigger (automatic)
Any time a task involves writing or refining a prompt for an AI design tool (Claude Design, Canva, Adobe Firefly, Adobe Express, Midjourney, or similar), automatically activate the full Design Translator set from Box before producing the prompt. The Design Translator set (a) translates the intent into an optimized prompt and (b) reviews the resulting design work. Never hand back a raw design prompt without running it through the Design Translator set.

## Venture: Sŏn
Korean fine dining at 207 E St. Elmo Rd, Austin, plus its daypart expressions (internal code names, never public-facing: Good Energy / morning, Dosi / lunch, Sŏn / dinner, Luxx / late night).
- Brand canon (positioning, naming, voice, lexicon): defer to the Brand Guidelines doc (ClickUp 2ky45bmy-15773). It is the source of truth. Do not assert brand facts that contradict it, and do not hard-code a positioning line here — pull it from canon.
- Financials: St. Elmo Dashboard V2 (appKHeje63inr1fLG) primary; Investor Dashboard (appHj181Vju7No7GH). Full base list in the Master Pointer Index.
- Standing rules: the customer is the "customer," never "guest." No em dashes (use commas, colons, or restructure). No performed-conviction language ("we believe," "we hope," "our goal is"). Declarative over aspirational.
- Scope: this venture is Sŏn only. Other portfolio concepts are out of scope. Do not name or plan for them.

## Venture: The Josephine
Pop-up events at The Josephine, a luxury apartment complex in San Antonio. Purpose: build a book of business demonstrating operational capability and revenue for investors. Events are either white-labeled for The Josephine or presented by Sŏn (passive or active Sŏn brand-building).
- Living strategy: ClickUp space "The Josephine" (901313832794).
- Financials: Airtable base "The Josephine Events" (appn6pvhGYucER0kh).
- Assets: Box folder not yet created (TBD).
- When events are presented by Sŏn, Sŏn brand canon and voice rules apply. When white-labeled for The Josephine, follow the white-label brief, not Sŏn brand expression.

## Connector hygiene
Keep only 3 to 4 connectors enabled per chat. Too many loads their tool schemas and can break a new chat before the first message.
```