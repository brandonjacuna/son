# Frame: Design Brief Translator
mode: merge (01 + 02 + 08) | cluster: design | founder-only: no | red-team intensity: standard

Reason: the seat writes briefs and routes; nothing it decides is hard to undo, touches employees, or carries money.

## Seat (one sentence)
This seat decides, before any design work starts, what a new Sŏn surface must do and for whom, which register and constraints bind it, what a reference image actually teaches, how a multi-artifact request splits, which seat makes each piece, and what the maker is handed as its constraint floor, producing one brief per artifact and a routing line.

## Container
skill. It shapes how the main conversation frames a request before a craft seat runs; no independent conclusion to run blind. Auto-trigger scoped by decision 2026-10-07 (new surfaces, reference images, multi-artifact requests; edits to existing components skip it); about 8 KB.
Model: none (a skill). Stage 5 tests on sonnet, the review's guess for the cheapest model that holds the mode.

## Decisions it owns (highest stakes first)
1. The trigger gate: does this request need a brief at all? New surface, reference image, or several artifacts: yes. An edit to an existing component, a copy fix, a token change: no, and the skill says so in one line and steps aside. Novice: briefs everything (an 8 KB tax on every design turn) or nothing.
2. Content integrity: upstream content (dish names, dates, the address, claims) is carried verbatim; a figure, claim, or decision that belongs elsewhere is a named gap, never filled. Investor and founder material never enters this seat; it is named and routed to the founder seats. Novice: fills the gap or pulls a figure.
3. Function before form: the one thing the artifact must do leads the brief; every parameter follows from it. Novice: restates the request ("a menu that feels premium").
4. Reference extraction: a reference is a revealed system; the brief carries its decision logic and portable parameters (ratio, density, accent coverage, hierarchy mechanism) and never its typeface, palette, or subjects, which would also break the closed eight-color system. "This but not this" on every reference. Novice: matches the reference's font and colors.
5. Register as a compound (economic register, emotional tone, relationship to the viewer) and mechanism in place of adjective. Novice: "high-end".
6. Split and route: one artifact, one brief; route by medium to the owning seat (`editorial-layout-specialist`, `web-ui-specialist`, `image-campaign-specialist`, `environmental-signage-specialist`, `artifact-design` for a claude.ai artifact) and name the seam when two share a piece. Novice: one brief for a page, a card, and a photo set.
7. The constraint floor for the maker (from 02): name who or what makes it (a coding session reading the design system, a claude.ai artifact, a real photographer or printer) and hand it the design system's files (`styles.css`, `tokens/`, the component `.prompt.md` files) by path, never a description or an invented value; override defaults with alternatives, not negations; flag what will not translate. Novice: "clean, minimal, Korean-inspired" plus a hex code.
8. Canon deference: the brand source is `company/brand/design-system`, pointed to, never restated. A conflict between it and CLAUDE.md (the guide's company name, its daypart code names) is flagged to Brandon in one line, never resolved or repeated. The Korean canon line binds every brief (concept yes; the five influences inform, never veto; Korean terms only as dish and ingredient names; pages 06 to 08, the Ma surface, the duck, baekja, and the ceramic traditions are reference only; the glyph travels with the logo). Novice: briefs a baekja pattern or a glossed term as brand.

## Seams
| neighbor | they own | this seat owns |
|---|---|---|
| `web-ui-specialist`, `editorial-layout-specialist`, `image-campaign-specialist` (agents, this batch) | the craft call and the critique of the made thing | the brief they design from, and which of them gets it |
| `creative-director` (skill, this batch) | the point of view, the signature decision, what dies | encoding the point of view it is handed into the brief; never selecting between directions |
| `environmental-signage-specialist` | whether a sign works physically | the brief for a sign's function and register; nothing about placement or material |
| `artifact-design` (account skill) | the page contract of any claude.ai artifact | whether an artifact is the right medium for a Sŏn surface, and its brief; an internal tracker or dashboard never triggers this seat |
| `intake` skill and `intake-triage` | a photo, sketch, markup, or spec sheet of the property or equipment | a reference image for a surface ("make it feel like this"); a photo of the St. Elmo space is intake |
| `interview` skill | pop-ups for any unresolved decision | a brief with an open decision uses `interview` rather than inventing the answer |
| `materials-author-editor` | learning-studio prose and its voice | a module page's layout brief, once Brandon starts that work |
| founder seats (pitch deck, investor design, financial exhibits) | every investor deck, exhibit, and surface | nothing; named and routed, no brief built |
| the design system (`company/brand/design-system`) | every brand fact, token, type, color, voice test, deck rule, photography rule | pointing at it by path |

## Research targets (gaps only)
1. What a brief must still decide when the maker is a coding session that reads the design system (what tokens, components, and `docs/codified-patterns.md` already answer; what remains a brief decision: function, audience, hierarchy, register, states, content). Known sources: `company/brand/design-system/readme.md`, `components/*.prompt.md`, `docs/codified-patterns.md`, `docs/content-architecture.md`. Why the old files cannot ground it: 02 assumes image generators and a "Claude Design" product, 01 a prompt specialist downstream; neither briefs a maker that already holds the system in code.

## Old material
| file | size | keep as source? | known problems |
|---|---|---|---|
| `profiles/_source/design-translating-team/01_Design_Brief_Translator_Profile.md` | 21.6 KB | yes: role_anchor, scope, mental models, decision_rules, construct_procedure, worked examples 1 to 3 | ClickUp Brand Guidelines as source (now the design system); Design Director and Platform Prompt Specialist as separate seats; standing rules duplicated from CLAUDE.md; example 1 is investor material (shape only) |
| `.../02_Platform_Prompt_Specialist_Profile.md` | 26.0 KB | partly: anti-default discipline, paste tokens not adjectives, override with alternatives, flag non-translation | the tool survey is date-stamped (`kb/tools/` or nowhere); "Claude Design" claims volatile; three-variant rule is bloat; "internal only" AI imagery is now "never" on any Sŏn surface |
| `.../08_Design_Director_Profile.md` | 24.4 KB | partly: route by who owns it, content integrity, seams in multi-discipline work | an orchestration layer for ten seats, now five; canon enforced through a ClickUp doc; assumes generation tools downstream |
| `.../03_Brand_Identity_Specialist_Profile.md` (retires) | 21.8 KB | headings read once; no merge | one row may move here: "designed is not delivered" (minimum-size variants, print color parity, prohibited-use notes). See open questions |

## Behavioral tests
In `00-tests.md`. The drafter never reads it.

## Open questions for Brandon
- Tool prompts: when a request names an image or code generation tool for internal mood frames or comps, does this seat still write the tool-specific prompt (02's old job), or does it stop at naming the maker and the constraint floor and write no prompts at all? (Keep prompt-writing / drop it / drop it except for Claude Code itself.)
- 03 retires. Move its "designed is not delivered" row (minimum-size variants, print color parity, prohibited-use documentation) into this seat's brief constraints, leave it to the design system to carry, or drop it? (Move here / design system / drop.)
- What do you NOT want this seat to do?

## Brandon's answers
- 2026-10-10: Tool prompts: drop every tool-specific prompt except Claude Code; other tools are named with the maker and the constraint floor, and their grammar moves to a kb/tools reference page.
- 2026-10-10: From retired 03: 'designed is not delivered' moves into this seat's brief constraints (every mark or print piece carries minimum-size variants, print color parity, and prohibited-use notes).
- 2026-10-10: The son-design guide in company/brand/design-system stays reference only, read by path; it never triggers.
- 2026-10-10: Not wanted: make the artifact itself; fire on edits to existing pieces; question Brandon before every brief (ask only when an answer changes the brief, otherwise write under stated assumptions); touch investor or founder material.
- 2026-10-10: No AI-generated imagery anywhere in the pipeline, internal mood frames included; mood is shown with real reference photographs and words.
