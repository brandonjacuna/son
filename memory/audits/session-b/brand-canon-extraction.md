# Brand canon extraction: experiential and Korean cultural material

Read-only extraction, 2026-10-07. For Brandon to mark keep / reference / cut per item.
Sources: ClickUp doc Brand Guidelines `2ky45bmy-15773` (all 17 pages read); repo `company/brand/design-system/` (readme, tokens, guidelines, docs, site, deck; refs/ and node_modules excluded).
Deck = `company/brand/design-system/guidelines-deck/Son Guidelines Deck.html` (stays; the -print.html twin has identical line numbers).

Options on every item: (A) keep as canon, (B) keep as reference only (not canon), (C) cut.
Blast radius: low / medium / high.

## Findings that change the question

1. The concept itself is described as Korean, in load-bearing places. "Korean fine dining restaurant" is the governing statement of Brand Architecture (ClickUp 02, `2ky45bmy-21933`), the readme's first line (readme.md:50) and the SKILL.md description. The live site hero is "One Korean room in Austin, Texas, open from first light to last call." (site/index.html:44, track/index.html:66, docs/copy.md:32, docs/build-spec.md:243-246, docs/type-decision.md:62,164). Cutting "Korean" from canon is a concept-level edit, not a tie-in removal. See POSITIONING items 1 and 2.
2. Not found anywhere: godwit, water deer letterform, and a persimmon / sumac / elderberry palette. Grep across the repo (excluding node_modules, refs) and all 17 ClickUp pages returns nothing. Only hits: "Persimmon, set overnight" as a sample menu line (ui_kits/good-energy/app.jsx:56; mirrored in _ds_bundle.js). The Mandarin duck exists only as a deferred, unexecuted bird mark (no asset, no token). The actual palette is eight colors with no Korean-named hues except Onggi (clay vessel). If those motifs exist, they live in refs/, Box, or another doc not in scope. Nothing to decide on them here.
3. The ClickUp doc already contains its own limit: page 08 forbids "traditional Korean garment forms," "motifs," "costume," and "anything that performs a culture rather than inhabits one." Page 03 prohibits minhwa, dancheong, folk painting. The existing canon is already restraint-based on motifs; it is the philosophy and vocabulary layer that is heavy.
4. The three frameworks are not isolated. Page 02 says they sit at Tier 1 with "veto power over every downstream decision" and "Nothing downstream overrides what is upstream." They are cited as the governing test in photography (page 10), digital error and empty states (page 12), deck layout (page 14), the Ma baseline page, and the Executive Chef hiring brief. Cutting them means rewriting those citations, not deleting a page.
5. Experiential content is about half of what is "decided" in the doc: pages 06, 07, 08 plus the Ma baseline page are the spatial, sonic and service spec for 207 E St. Elmo Rd. Much of it is operational design for the build-out (acoustic STC values, floor spec, uniform roles), not brand philosophy. Cutting from brand canon does not have to mean deleting; route-to-build-out is a fourth path worth considering (noted per item).

---

## EXPERIENTIAL

### 1. Page 06 Spatial and Environmental Design
- Lives in: ClickUp `2ky45bmy-22013`. Deck section 13, `Son Guidelines Deck.html` lines 1154-1296 (property, cross-zone principles, nine-beat sequence, materiality matrix, lighting, signage).
- What it is: Nine-beat arrival sequence, materiality matrix (white oak floor, honed limestone bar, oxidized steel), daypart lighting schedule, and the 6B signage decision. Key line: "One primary destination requires signage: the restrooms. Every other destination is delivered by spatial geometry, direct visibility, the maitre d', or staff walking." Pyeong-sang (floor-seating zone) appears as beat 7, "granted, not findable."
- Category: EXPERIENTIAL.
- Depends on it: deck section 13; build-out workstream (architect briefs, CD phase open items: pyeong-sang placement, bar back reflectivity, wall blocking for the sign); token themes for lighting (2700K).
- Blast radius: medium. Largely build-out specification. Also contains Korean-flavored terms (pyeong-sang, Sandoll bilingual sign rules).
- Options: A keep as canon / B reference only (move to build-out workstream as source spec) / C cut.

### 2. Page 07 Multi-Sensory Architecture
- Lives in: ClickUp `2ky45bmy-22033`. Deck section 14, lines 1297-1393 (sonic backbone, tempo mapping, curation governance, acoustic spec).
- What it is: Speaker system (point-source, DSP), RT60 and SPL targets, four playlist contexts with BPM ranges, person-triggered transitions only, service-door STC spec. Held items: scent (Olfactory Designer unslotted), tableware (7C, held for chef; names four Korean ceramic traditions: Bangjja Yugi, Baekja, Buncheong, Cheongja). Key line: "Person-triggered transitions only. No automated timers."
- Category: EXPERIENTIAL (tableware held item is also CULTURAL-VISUAL, see item 9).
- Depends on it: deck section 14; AV and acoustic engineer scope; build-out. Nothing in tokens or site.
- Blast radius: low to medium. Technical spec, almost no brand-system code depends on it.
- Options: A / B (move to build-out) / C.

### 3. Page 08 Service Choreography and Staff Presentation
- Lives in: ClickUp `2ky45bmy-22053`. Deck section 15, lines 1394-1484 (step-back architecture, floor authority, key protocols, uniform system at 1459).
- What it is: Service model built on Jeong + Nunchi ("Not omotenashi"), step-back model, floor authority, greeting script ("We have you."), David protocol, pyeong-sang protocol, the Bent Spoon principle, and the five-role uniform system. Key line: "Korean cultural expression: contemporary South Korean fashion sensibility - proportion, restraint, fabrication quality. No traditional garment forms, no historical silhouette references, no motifs."
- Category: EXPERIENTIAL, with a cultural-concept core (Jeong/Nunchi, see item 6) and a cultural-visual edge (uniform sourcing reference, "Korean fashion sensibility").
- Depends on it: deck section 15; SOP and training build-out (`company/operations`), Scaling People; uniform designer engagement (Finery LA). Service behavior would survive without the Korean framing.
- Blast radius: medium. The behavior spec is operational; only the framing is cultural.
- Options: A / B (keep behavior as operations reference, strip Korean framing) / C.

### 4. Ma / Yubaek-ui-mi Surface and Zone Baseline (standalone page)
- Lives in: ClickUp `2ky45bmy-26793`. Referenced as a hard input to Session 6A and as the completed Open item 7 on page 02.
- What it is: Brandon's pre-design decision document: per zone (entry, dining room, bar, patio, pyeong-sang, service threshold, circulation) what is present, absent, and why. Twelve non-negotiable requirements, e.g. "Counter-level bar," "One-directional sightline for pyeong-sang," "Entry maitre d' position at or outside the threshold." Cross-zone principles: "We walk, we never point." / "Net positive, net neutral, never net negative."
- Category: EXPERIENTIAL (spatial intent), titled and justified by CULTURAL-CONCEPT (Ma).
- Depends on it: build-out and architect briefs (it is the governing input), page 06 decisions, any Ma citations. Almost all content stands without the word "Ma."
- Blast radius: high for build-out (architect works "within these governing intentions"), low for brand tokens. Strongest candidate for "keep content, drop the Korean label."
- Options: A / B (retitle, move under build-out as design intent; drop Ma framing) / C.

## CULTURAL-CONCEPT

### 5. The three Tier-1 frameworks: Jaeyeonmi, Ma / Yubaek-ui-mi, Mahk
- Lives in: ClickUp `2ky45bmy-21913` (01, "Cultural Aesthetic Frameworks"), `2ky45bmy-21933` (02, Tier 1, "veto power"). Repo: readme.md:95-107 ("The three Tier-1 frameworks (always govern)"), readme.md:57-58 ("governed top-down by three Tier-1 cultural frameworks"). Deck lines 118-228 (Tier 1 authority, Jaeyeonmi 135, Ma 161, Mahk 186) and 538 (hierarchy row 1).
- What it is: Governing design philosophy. Jaeyeonmi: "Nothing in this space should conceal what it is, where it came from, or how long it has been here." Ma: "Empty is a specification, not a default." Mahk: "Food calibrated to please everyone produces Mahk for no one." They constrain materials, layout, kitchen, photography, and the adherence checks.
- Category: CULTURAL-CONCEPT.
- Depends on it: photography philosophy (page 10, photographer "cultural fluency" test), digital error/empty states (page 12), deck layout (page 14), voice rule "Specificity is the mechanism of memory (Mahk constant)," the Executive Chef hiring brief (Mahk standard), olfactory brief. Repo: readme preface, deck pages, SKILL.md.
- Blast radius: high. This is the root of the authority hierarchy. Cut means every downstream citation needs a replacement rationale (the underlying rules are plain English and mostly stand alone: no faux textures, empty space is specified, be specific).
- Options: A / B (keep the rules, demote the Korean names to "origin of the idea") / C (keep rules, rename and re-anchor).

### 6. Jeong and Nunchi (service philosophy) and "Not omotenashi"
- Lives in: ClickUp 01 (`2ky45bmy-21913`, "Service Philosophy"), 02 (Tier 3), 08 (`2ky45bmy-22053`). Repo: readme.md:144 (preferred terms). Deck lines 263-293 (Jeong, Nunchi, "This is not omotenashi. The Japanese model anticipates and perfects. Jeong accumulates and Nunchi reads."), persona pages 359-418 (Mia "Requires Nunchi").
- What it is: The named service philosophy. Jeong is accumulated relationship, not performed welcome; Nunchi is attunement, not diagnostic inquiry. The omotenashi contrast positions Sŏn against another culture's model.
- Category: CULTURAL-CONCEPT.
- Depends on it: service model (item 3), persona definitions (Mia and the "Nunchi requirement"), the bird mark referent (Jeong, item 8), SOP and training content, hiring criteria, the Korean Hospitality Consultant brief.
- Blast radius: medium to high. Behavior (attunement, accumulated relationship) is portable; the vocabulary threads through personas and training.
- Options: A / B / C (restate as plain-language service principles).

### 7. Korean terminology deployment rules and the preferred-terms list
- Lives in: ClickUp 04 (`2ky45bmy-21973`, Hangul Deployment Rules 1-3), 09 (`2ky45bmy-22073`, Preferred terms). Repo: readme.md:143-146, `adherence/check-copy.mjs` (font and copy checks), deck lines 757-783 (Hangul deployment) and 970-1000 (preferred terms).
- What it is: Rule 2: "Korean terminology stands without explanation in all brand contexts from day one, without exception." No translation, no gloss. Preferred list: Jeong, Nunchi, Jaeyeonmi, Ma, Mahk, Galbi, Dosirak, Banchan, Buncheong, Baekja, Pyeong-sang, Ganjang, Doenjang, Gochujang, 선. Menu rule: Korean dish name, no translation.
- Category: CULTURAL-CONCEPT (vocabulary policy).
- Depends on it: menu copy rules (Section 09 menu principles), in-space copy ("선 / 207 E St. Elmo Rd"), voice register matrix, the Dosi menu rule, the copy linter. Interacts with Brandon's own rule that legal/finance jargon gets defined; this rule says the opposite for Korean terms.
- Blast radius: medium. Affects all written output rules and the menu. Food names (Galbi, Banchan) are dish vocabulary, not tie-ins, and would likely stay under any option.
- Options: A / B (keep dish names, drop the no-gloss rule and the philosophy terms) / C.

## CULTURAL-VISUAL

### 8. The 선 glyph mark and the "sole mandatory structural constant" mandate
- Lives in: ClickUp 03 (`2ky45bmy-21953`, 선 Glyph Relationship), 02 (non-negotiable 8), 04 (`2ky45bmy-21973`, 선 Glyph Rendering Specification). Repo: readme.md:59-60, 270-272 ("The 선 glyph is the primary mark"); `components/brand/Wordmark.jsx/.d.ts/.prompt.md`; `components/immersive/AmbientField.*`, `Marquee.*`, `DaypartTakeover.jsx:75`; `components/core/Divider.*`, `Badge.*`; `tokens/seon.css`; `ui_kits/*/app.jsx`; `site/site.css:77-94`; `_adherence.oxlintrc.json` and `eslint.config.mjs` (selectors enforce the glyph and font); `docs/design-language.md:44-45` ("A Korean room that does not show its Korean mark in the opening loses the one signal..."). Deck lines 550-625 (mandate, glyph) and a glyph on nearly every slide.
- What it is: The Hangul syllable 선 (the Korean sounding of "Sŏn") set under the Latin wordmark on every surface at a constant scale. Key line: "선 appears on every daypart surface at a constant scale ratio. It cannot vary. It cannot be exempted."
- Category: CULTURAL-VISUAL (also the identity itself).
- Depends on it: the wordmark lock-up, every daypart surface, 10+ components, site, deck, adherence linting, signage and packaging briefs. The brand name "Sŏn" is itself the Korean word, so the glyph is the name written natively.
- Blast radius: high. This is the logo. Flag: likely the name and mark, not a tie-in. Brandon decides whether it counts.
- Options: A / B / C (cut means a redrawn wordmark, a system-wide component change, and a rule rewrite).

### 9. Korean companion typeface: Sandoll Myeongjo (with Nanum Myeongjo substitute) and Hangul scale
- Lives in: ClickUp 04 (`2ky45bmy-21973`), 05 (`2ky45bmy-21993`, `son.font.family.korean`). Repo: `tokens/typography.css:69-72` (`--son-font-korean`), `:212-213` (`--son-korean-scale: 1.12`), `tokens/fonts.css:4-19,48`, `tokens/base.css:49-58` (Hangul rule), `guidelines/type-korean.html`, `readme.md:196-199, 289-294`, `_adherence.oxlintrc.json:46,284,296,376,401,442`, `eslint.config.mjs:58`. Deck lines 691-756.
- What it is: One Korean typeface for all Hangul, "no mixing," Noto Serif KR prohibited. Currently unlicensed for web; Nanum Myeongjo is the flagged substitute and the binaries are pending a hand-copy from Box.
- Category: CULTURAL-VISUAL.
- Depends on it: the 선 glyph (item 8), any Hangul text, font tokens, lint rules, the open license purchase. If Hangul is limited to the glyph and a few dish names, the typeface is a small dependency.
- Blast radius: medium. Tokens and lint rules are tied to it, but removal is mechanical. Decision is coupled to item 8.
- Options: A / B / C.

### 10. Pattern system (Joseon-era baekja lineage), iconography rules, and the mandarin duck (원앙) bird mark
- Lives in: ClickUp 03 (`2ky45bmy-21953`: Pattern System 3B, Iconography System 3B, bird mark referent). Repo: readme.md:273-279 (future marks, pattern deferred), deck lines 626-681 (Pattern and texture 626, Iconography 647, Bird mark 662-681, "The mandarin duck. Mate for life."). `docs/` has no executed asset; the pattern and bird mark are unbuilt.
- What it is: Pattern is edge-scale only, derived from the wordmark geometry, with baekja as "cultural precedent; does not supply the geometry." The bird mark referent is confirmed as the mandarin duck: "Devoted partnership, a pair that stays. It connects directly to Jeong." Visual execution is deferred. The iconography rules prohibit minhwa, woodblock, dancheong and folk-painting traditions.
- Category: CULTURAL-VISUAL.
- Depends on it: nothing executed. No tokens, components, or assets. Only deck pages, the readme paragraph, and future packaging, emboss and seal briefs ("documented Korean cultural referent" is a required rule for any future mark, so the rule itself needs rewriting if cut).
- Blast radius: low. All unbuilt.
- Options: A / B / C. Easiest clean cut in the visual set.

### 11. Onggi palette color (and tableware ceramic traditions)
- Lives in: ClickUp 05 (`2ky45bmy-21993`: Onggi #804A33 "Earthen clay - Dosi ground"), 07 (`2ky45bmy-22033`: Bangjja Yugi / Baekja / Buncheong / Cheongja tableware, held for chef), 09 (preferred terms Buncheong, Baekja; "onggi clay not traditional vessels"). Repo: `tokens/colors.css:25,77-91`, `guidelines/colors-accents.html`, `guidelines/colors-daypart.html:24-25`, `site/site.css:289`, `track/track.css:525`, `templates/deck/index.html:28`, `slides/07-menu.html:13`.
- What it is: Of eight palette colors, one carries a Korean cultural name: Onggi, the Korean earthenware clay vessel. It is the Dosi (lunch) ground and the secondary accent. The color is a hex value; the Korean reference is only in the name and rationale. The four ceramic traditions in the held tableware session are a chef-hiring criterion, not a built asset.
- Category: CULTURAL-VISUAL.
- Depends on it: lunch-daypart theme, lunch stripe, semantic tokens (surface-inverse, border, accent, focus ring). Photo grading ("skin tones warm toward Onggi").
- Blast radius: medium if the name is cut and the color kept (rename token), high if the color is cut. Recommend: the color stays under any option; only the name and rationale are the decision.
- Options: A / B (rename to a neutral hue name, e.g. "Clay") / C (drop the tableware tradition criterion).

## POSITIONING (flag: may be the concept itself, not a tie-in)

### 12. "Korean fine dining restaurant" and "Korean restraint" (positioning value)
- Lives in: ClickUp 01 (`2ky45bmy-21913`: "Positioning: Korean restraint / Texas warmth / Polished but playful"), 02 (`2ky45bmy-21933`: governing statement "Sŏn is a Korean fine dining restaurant... governed by three Korean aesthetic frameworks"; Tier 2 "Korean restraint, Texas warmth, executed with rigor"; "The frameworks are the Korean expression of the [Playground] philosophy"). Repo: readme.md:50 ("A Korean fine-dining restaurant in Austin"), readme.md:62 (three equal, unordered values), SKILL.md:3, `templates/deck/index.html:127`, deck lines 52-60 (Positioning slide, "Korean restraint. Texas warmth. Polished but playful."). Site and copy: `site/index.html:44,77`, `track/index.html:66-72,158`, `docs/copy.md:32,87`, `docs/build-spec.md:243-246,309`, `docs/type-decision.md:62,164`, `docs/design-language.md:87,242`, `docs/structure-decision.md:94`. Also ecosystem names: Dosi is "Korean QSR / dosirak" and "Korean lunch"; Good Energy sells "Korean pastry" (ClickUp 01 concept table; deck lines 92-117).
- What it is: This is the concept. Key lines: "Sŏn is a Korean fine dining restaurant and the equity anchor of a multi-concept hospitality ecosystem" and the live hero "One Korean room in Austin, Texas, open from first light to last call." The mobile hero strophe was locked 2026-07-20 and is type-fitted around the words "One Korean / room in Austin, Texas."
- Category: POSITIONING. Treat separately from all the items above.
- Depends on it: site hero and market-claim copy ("Korean food and the city of Austin are climbing the same curve"), the type-fit of the hero (docs/type-decision.md), the readme and SKILL.md descriptions, the deck positioning slide, the daypart menu concepts (Dosi is a Korean lunch), restaurant identity in legal and capital-raise material outside this repo scope.
- Blast radius: high. Changes what the restaurant is, not just how the brand thinks. It is also the only item with live public site copy.
- Options: A keep as canon / B keep as reference only (describe the cuisine as Korean in menu and food copy but not in positioning or governing statements) / C cut (rewrite hero, readme, positioning, governing statement). Question for Brandon: is "Korean" a statement about the food and the founder's heritage (stays) or a brand-philosophy layer (cut)?

---

## Suggested decision order (dependencies)
1. Item 12 first (concept vs tie-in). It sets the frame for the rest.
2. Items 8 and 9 together (glyph and Korean typeface are coupled).
3. Items 5, 6, 7 together (philosophy and vocabulary; 5 and 6 are what the 2026-10-07 decision most likely meant by "Korean cultural tie-ins").
4. Items 1-4 (experiential), considering a route-to-build-out option rather than a binary cut.
5. Items 10 and 11 (low blast radius, can be cut or kept with no downstream work).

## One-line index
1. Page 06 Spatial and Environmental Design: EXPERIENTIAL, medium
2. Page 07 Multi-Sensory Architecture: EXPERIENTIAL, low to medium
3. Page 08 Service Choreography and Staff Presentation: EXPERIENTIAL, medium
4. Ma / Yubaek-ui-mi Surface and Zone Baseline page: EXPERIENTIAL, high (build-out input)
5. Three Tier-1 frameworks (Jaeyeonmi, Ma, Mahk): CULTURAL-CONCEPT, high
6. Jeong, Nunchi, "not omotenashi": CULTURAL-CONCEPT, medium to high
7. Korean terminology rules and preferred terms: CULTURAL-CONCEPT, medium
8. 선 glyph mark and mandate: CULTURAL-VISUAL, high (may be the name and logo)
9. Sandoll Myeongjo Korean companion typeface and Hangul scale: CULTURAL-VISUAL, medium
10. Baekja pattern system, iconography rules, mandarin duck bird mark: CULTURAL-VISUAL, low (unbuilt)
11. Onggi color name and ceramic traditions: CULTURAL-VISUAL, medium
12. "Korean fine dining" and "Korean restraint" positioning: POSITIONING, high (the concept itself, live site copy)
