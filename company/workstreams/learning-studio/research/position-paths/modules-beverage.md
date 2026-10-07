# Beverage: the modules (working draft, 2026-10-01)

Writer 3's modules from the spine (`research/position-paths/spine.md`, section 5.4, with the knowledge tracks in section 4), in the module format from the task brief. Status: content-first working draft for Brandon. Nothing here is decided until Brandon signs it.

Governs: D52 to D60, carrying D5, D8, D10, D11, D13, D17, D24, D27, D39 to D41, D44, D46, D47 and D50.

How to read it:
- Hours are design estimates (40 paid hours a week, no overtime) and match the spine. Where a module's split differs from the spine, the difference is named.
- "Remote" means remote and paid. "On site" means on the clock (D41). Every drill and every tasting is on site.
- Canon is cited by label (WP = white paper, Box `2466517057642`; BG = Brand Guidelines (canon line pending phase 1 session B), Box `2281626080747`), carried from the drafts' reads, never restated. Re-read the cited section in Box before a lesson is drafted. The front-loaded program (batched work, espresso pulled in the back, no espresso machine on the front bar, the founder matcha method, liquid nitrogen and pressure holding) is WP pp.4 to 5 as the discovery inventory cites it, not re-read in this pass.
- Every spec, range, hold time, temperature target, pour size and list item is set by the head of beverage (D47) and written as a binding (`bev.*`, `people.head_of_beverage`). Every tool step is `tool.*`, every house convention not yet set is `workflow.*`, every figure and fee is `fact.*`, every holder is `people.*`, every founder call is `founder.*`, every policy is `policy.*`. Physical opening, closing and side work tied to the unbuilt space are placeholders (D58).
- External claims carry a mark: verified-primary, verified-secondary, lead-only or unverified. Marks carried from the research passes or the spine are marked "carried".
- Positions: H host, LH lead host, FR food runner, BW back waiter, FS front server, LS lead server, MD Maître d', OM operations manager; BB barback, BA barista, BT bartender, LB lead bartender, HB head of beverage. CF = customer-facing.
- Tasting alcohol on paid time, the legal age to taste, and the non-drinking route (smell and spit, never swallowed) apply to every tasting below: `policy.tasting_on_paid_time`, `compliance.alcohol_tasting`. No module requires anyone to swallow alcohol.
- Every track teaches both kinds of advocacy (D54): finding what this customer would enjoy (SVC-033, BEV-113), and product feedback the maker can trust (MNU-101, owned by writer 2; this file supplies the beverage examples). Every track module at every level names both: a "for the customer" element (who would enjoy it, from what they drink now, for which course) and one MNU-101 note that level must produce.
- Prove-first (ORI-015, red-team finding 5): every non-safety module lets an experienced hire attempt the proof cold after reading the material. A pass banks the module; a failed cold attempt routes the person into the instruction with no interval and no recorded miss (D11). Safety elements (sparkling, the steam wand, the knife, the ice well, allergens) are demonstrated on every attempt and never test out.
- Supervised services are counted at shift length (`workflow.shift_length.<position>`, about 6 h as the design assumption), so opening, closing and side work learned inside them (BEV-101) are inside counted time.
- Ongoing education, including every gate held before a window, is paid time placed in the schedule against `policy.ongoing_education_hours.<position>` (ADM-104, SYS-134). Time-in-seat estimates below assume that allowance; study never drifts home unpaid (D6, D41).
- Outside courses count only if delivered and tracked inside Trainual (D27). No beverage provider was found to do so (unverified, carried; ask each one). Until then each serves as a content benchmark and as prior-learning evidence for test-outs, never as the gate.

---

## Part 1. The bar team core (Block D: BB, BA, BT; parts for the floor and for HB)

### BEV-017 How the beverage program is built, and how to hold it
- Area: beverage
- Positions and timing: BB, BA, BT, LB, HB; readiness, day one or two of the bar block, before any drill. For experienced hires it is also the habit-correction step that ORI-033's bar part points to.
- What it teaches:
  - The program is front-loaded (WP pp.4 to 5, carried; re-read in Box). Three kinds of work, and which drinks fall in each (`bev.program_map`):
    - Batched in advance: components and whole drinks built by weight, labeled, held to a hold time.
    - Pulled in the back: espresso is batch-pulled as shared kitchen and bar work; there is no espresso machine on the front bar and no dialing in on the floor.
    - Finished at the bar: the last steps the customer sees (chill, dilute, texture, pour, garnish, present).
  - Why: the same drink every time at any tempo; a raised and held floor of quality; the maker's attention freed for the customer at the counter. Cite the WP reasoning by page; Brandon's own account of why comes from interview.
  - The habits experienced craft hires bring and drop here: adding steps at the counter (an extra shake, a re-garnish, a dash to "fix" a batch); free-pouring; a personal version of a house spec; treating a batched drink as lesser; re-dialing coffee by habit.
  - Who owns a spec: the head of beverage (D47). The lead bartender holds it on the shift. A change is proposed, blind-tested (BEV-022) and written (BEV-030); it is never made at the counter.
  - When a batch seems wrong: pull it and flag it (BEV-006), never adjust it in the glass.
  - What only trained preparers touch: liquid nitrogen and pressurized holding (SAF-003, renumbering pending, see Spine changes needed).
- What the person can do afterward: say in their own words why a batched component is not a shortcut, place any drink on the list in one of the three kinds of work, and name the counter step they will not add.
- How it is proven: a spoken check with LB or HB (about 15 minutes). Prove-first: an experienced hire reads the program map and takes the spoken check cold.
- Time and place: 2 h (1.5 remote, 0.5 on site for the check).
- Waits on: `founder.bev_program_method`; `chef.batch_espresso_method` (chef with HB); `bev.program_map`; Box re-read of WP pp.4 to 5; Brandon interview on why the program is built this way.
- Absorbs: BEV-017; part of LIB-008 (reading list).

### BEV-001 The four variables: temperature, dilution, texture, extraction
- Area: beverage
- Positions and timing: BA and a BT entering from outside, readiness, week one (a green external BA proves it first where possible; barback-first is the default barista route). BB ongoing, held before the BT window. Open to the floor by interest.
- What it teaches:
  - Temperature: colder mutes sweetness and aroma and hides alcohol heat; warmer releases aroma and makes sweetness and alcohol more obvious. Why a drink is served at its set temperature (`bev.spec.*`).
  - Dilution: ice chills by melting, so chilling and dilution travel together. Water is an ingredient: too little leaves a drink hot and sharp, too much leaves it thin and flat. Shaken drinks end colder, more diluted and aerated than stirred; built drinks keep diluting in the glass. The house targets are set by HB (`bev.spec.dilution_targets`).
  - Texture: aeration from shaking; foam from egg white or its alternatives (an allergen point); carbonation and how it is lost (warm glass, rough pour, stirring); body from sugar; milk proteins and fat in foam.
  - Extraction in coffee and tea: dose and ratio, grind or leaf size, water temperature, contact time, agitation. Under-extracted tastes sour and thin; over-extracted tastes bitter, drying and hollow.
  - Diagnosis: one variable drifting shows up in the glass in a recognizable way. Each point is taught over a deliberately flawed drink: an under-diluted stirred drink, an over-diluted shaken drink, a sparkling drink poured into a warm glass, an over-steeped green tea, a batch held past its time.
- What the person can do afterward: taste a flawed drink, name which variable moved, and name the fix and who makes it.
- How it is proven: a spoken check over three flawed drinks. Test-out: the same check, cold, on day one.
- Time and place: 2.5 h (1 remote, 1.5 on site at a tasting).
- Waits on: HB's specs and targets (`bev.spec.*`); the flawed-drink set built by HB.
- Absorbs: BEV-001; LIB-006 (its sources become this module's reading list).

### BEV-002 Pour control (drills)
- Area: beverage
- Positions and timing: BB, BA, BT; readiness, week one, split across days. The floor part is readiness for BW (from FR) and is held by FS.
- What it teaches:
  - Brandon's water-pitcher sequence, in his telling: slowest until empty, fastest until empty, slow to fast, then height changes. The movement is drilled until it no longer needs attention (ORI-016 method).
  - Flow made measurable: pour for a set count into a measuring vessel and compare with the target; stream width and height compared against a reference clip. Cues are aimed at the stream, not the wrist.
  - Jigger: held level, filled to the line in one motion, emptied completely; both jigger sides; two jiggers at once only after one is automatic (BEV-012).
  - Bottle: label out, a steady stream, a turn of the wrist to stop the drip, the neck wiped per the standards book (D46).
  - The milk stream, as the base for BEV-004.
  - Floor part: water from a pitcher and from the bottle, still and sparkling; the pour level for each house glass (`bev.pour_levels`, standards book D46); pouring without crossing in front of a customer (side of service `workflow.service_side`, D48); never pouring over a plate; sparkling poured down the side so it keeps its bubbles; reading the glass and the table before a refill (SVC-006).
- What the person can do afterward: hit a target volume and line, repeatably, at three tempos; on the floor, pour water and still or sparkling at the table to level with no drip while talking.
- How it is proven: a banked drill run-through, then a recheck inside the warm-up (D44). Test-out: the same run-through at entry (D39).
- Time and place: 4 h on site (bar); 2 h on site (floor part).
- Waits on: `bev.pour_levels`, `bev.pour_sizes` (HB); the standards book (D46); `workflow.service_side` (D48); Brandon recording the pitcher drill story (shared with ORI-016).
- Absorbs: BEV-002, SVC-026.

### BEV-003 Station and body (drill)
- Area: beverage
- Positions and timing: BB, BA, BT; readiness, week one.
- What it teaches:
  - The station as set (`workflow.bar.station_layout`, placeholder until the space exists, D58): everything for the common builds reachable without bending, turning away from the counter or crossing another maker.
  - The order of reach for a build: glass, ice, ingredients by measure, tool, garnish, set down; and back to the start position after every drink.
  - Two-handed working: the second hand is never idle (it holds the tin, opens the next bottle, sets the next glass).
  - The body: lifting crates, ice and kegs without strain; standing so the back stays neutral at the well; where the feet go so a teammate can pass.
  - Why the setup is a condition, not a preference: a moved bottle costs every maker a reach, and at tempo a reach becomes a spill.
- What the person can do afterward: work a sequence of drinks without a wasted step and reset the station between drinks, observed at two tempos.
- How it is proven: a banked drill. Test-out: the same drill at entry.
- Time and place: 2.5 h on site.
- Waits on: `workflow.bar.station_layout` (D58); HB's station map.
- Absorbs: BEV-003.

### BEV-016 Moving together behind the bar, and the calls
- Area: beverage
- Positions and timing: BB, BA, BT; readiness, week one. The service-well part is taken by BW through SVC-013 (writer 2 holds the floor side), and by FR only if runners carry drinks (`workflow.drink_running`); if they do, FR readiness gains about 0.5 h.
- What it teaches:
  - The house calls behind the bar (draft set for the team to confirm: behind, corner, hot, sharp, glass, ice down, burning the well) and the callback: say it, hear it answered, then move. The words are shared with the kitchen (`chef.call_language`, `team.call_vocabulary`).
  - Passing lanes and who yields. Draft rule for the team to confirm: the maker at the well holds position; the person moving yields; anyone carrying glass, ice or a full tray gets the lane.
  - Handoff at the service well: the maker calls the ticket; the drink goes to the pickup point (`workflow.bar.pickup`); the runner or back waiter confirms ticket, table and seat aloud before lifting; nothing leaves unconfirmed. Allergy-flagged drinks are handed off by name, the same as a modified plate (SAF-004).
  - What happens when it breaks: a dropped call is repeated, never assumed; a collision is reset with one word, not an argument.
- What the person can do afterward: move through a three-person bar at tempo with every call made and answered and no collision; hand off at the well on the closed loop.
- How it is proven: a practical in a simulated rush, then observed in supervised services. Prove-first for an experienced external BT: read the call list, then pass the simulated rush cold; supervised-service observation stays.
- Time and place: 2 h on site (service-well part about 0.5 h, counted inside SVC-013).
- Waits on: `team.call_vocabulary` (team-gated); `chef.call_language`; `workflow.bar.pickup`; the space (D58).
- Absorbs: BEV-016; the bar side of SAF-007.

### BEV-014 Glass and ice: the contamination call
- Area: beverage
- Positions and timing: BB, BA, BT; readiness, week one, before working the well.
- What it teaches:
  - The rule: any glass that breaks in, over or near the ice well, or any chip that could have reached it, means the well is burned and refilled. No exceptions, no weighing it against tempo or cost.
  - Why: a shard in ice is invisible and reaches a customer's mouth.
  - How to burn safely: call it ("burning the well") so the team switches to the backup ice source (`workflow.bar.backup_ice`); empty the well with the scoop into a container, never by hand; melt the rest with hot water; check the empty well under light for shards; wipe and dry; refill from clean ice.
  - Prevention: ice is scooped only with the scoop, never with a glass; the scoop handle stays out of the ice; glass is never chilled in the service ice.
- What the person can do afterward: make the call without hesitation in a costly scenario (a full rush, a full well), and burn the well correctly.
- How it is proven: a scenario item that must pass in every attempt (D11), and the burn done once on site. No test-out: safety.
- Time and place: 1 h on site.
- Waits on: `workflow.bar.backup_ice`; the space (D58).
- Absorbs: BEV-014.

### BEV-024 Working in the sightline
- Area: beverage
- Positions and timing: BB, BA, BT; readiness, week one.
- What it teaches:
  - Every seat sees the bar (BG 13 bar zone and BG 15, cited). The bar is part of the room's intent, not a back office.
  - What reads as mess: towels on show, bottles off their marks, a phone, a personal drink, eating, leaning, turning one's back to talk, a full bin, wet surfaces.
  - Onstage and backstage zones (`workflow.bar.zones`, D58): what may be done where.
  - The uniform standard (`brand.uniform`; BG cited) and the self-check between rushes.
  - The reset: a short routine after each rush to return the station and oneself to standard.
- What the person can do afterward: reset the station and themselves to standard between rushes, unprompted.
- How it is proven: observation in supervised services against a short checklist. Prove-first for an experienced external BT: after reading the zones and the uniform standard, the observation in supervised services is the proof and the instruction hour is skipped.
- Time and place: 1 h on site.
- Waits on: BG 13 and BG 15 re-read; `brand.uniform`; `workflow.bar.zones` (D58).
- Absorbs: BEV-024.

### BEV-033 Bar prep to spec
- Area: beverage
- Positions and timing: BB full; BA and BT the house portion; readiness, week one into two.
- What it teaches:
  - Reading the prep list (`workflow.bar.prep_list`): what is due, the par, what is made first because it needs time.
  - Citrus: juicing method, straining, the hold time and why it matters (`bev.spec.citrus_hold`).
  - Syrups and cordials by recipe and by weight; the scale zeroed every time.
  - Garnish: cuts, sizes, storage, and when a garnish is past use.
  - The ice program: the house ice types, handling, storage, and when ice is lost (`bev.ice_program`).
  - Labels: name, date and time made, maker, use-by, allergens (nut, dairy, egg and others HB lists). First in, first out.
  - Batching within the preparer's limits: by recipe, by weight, the batch checked and tasted against the reference before it goes to the station. High-hazard techniques are excluded (SAF-003).
  - Drift: what an old or wrong component looks, smells and tastes like; pull it and tell LB.
  - Knife safety at the bar board: grip, the guard hand, a board that cannot slide, carrying and passing a knife, where it rests.
- What the person can do afterward: complete a full prep list to spec within the set time, labeled and rotated, with one batch matching the reference.
- How it is proven: a practical scored on accuracy, consistency across repeated batches, time management and total time, with the person stating the plan aloud first. Test-out: knife and juicing technique only; the house recipes and labels are always proven. The knife-safety element (grip, guard hand, board stability, carrying and passing) is demonstrated on every attempt and never tests out.
- Time and place: 6 h on site (BB); 3 h on site (BA, BT).
- Waits on: `bev.prep_recipes.*` (HB; `chef.*` where prep is shared with the kitchen); `bev.spec.citrus_hold`; `bev.ice_program`; `workflow.bar.prep_list`; any time limit as `fact.*`.
- Absorbs: BEV-033.

### BEV-101 Opening, closing and side work at the bar (placeholder)
- Area: beverage
- Positions and timing: BB, BA, BT; readiness, learned inside the supervised services.
- What it teaches (the durable part only; the sequences are `workflow.bar.opening`, `workflow.bar.closing`, `workflow.bar.side_work`, D58):
  - Why each task exists and what done looks like: what is checked before doors (batches tasted, labels in date, ice full, glass inspected, refrigeration logged, SYS-139), what is never left overnight (open dairy, cut fruit past use, a wet well), what is locked away.
  - The handoff note: what the next shift needs to know (low stock, a drifted batch pulled, a repair reported).
  - Who signs it off (`people.bar_close_signoff`; LB, ADM-117).
- What the person can do afterward: open and close the bar to standard with the checklist.
- How it is proven: a practical inside the supervised services. Prove-first: an experienced hire opens or closes once to the checklist on a supervised service.
- Time and place: inside the supervised services, which carry it only because they are counted at full shift length (`workflow.shift_length.<position>`); if services are counted shorter, this needs its own hours.
- Waits on: the space (D58); the three `workflow.bar.*` sequences; SYS-139 for refrigeration logs.
- Absorbs: none (new).

### FLV-002 The smell library
- Area: beverage
- Positions and timing: BA and an external BT, the core set is readiness, week one; BB ongoing, held before the BT window. Beyond the core it is ongoing for everyone, run as a warm-up (D44).
- What it teaches:
  - The core aromas found in the house's drinks, named from reference kits (`bev.aroma_kit`): citrus, red fruit, stone fruit, tropical fruit, floral, herbal, spice, nut, roast, fermented and savory (soy and jang notes, lactic), oak and vanilla, earth.
  - Near-miss pairs: lemon and lime, cherry and raspberry, clove and cinnamon, vanilla and coconut, toast and smoke.
  - Faults as smells: musty wet cardboard (cork taint), bruised apple and nuttiness in a fresh wine (oxidation), stale or papery coffee, sour milk, a dirty-line smell in beer.
  - The house words for each, kept consistent with BEV-008.
- What the person can do afterward: name the core set blind, and say what a drifted batch smells like.
- How it is proven: a spoken check at the kit; recheck in warm-ups. Test-out available on the core set.
- Time and place: 2 h on site; ongoing inside warm-ups.
- Waits on: `bev.aroma_kit` (HB chooses); the kit cost as `fact.*`.
- Absorbs: FLV-002.

### BEV-027 Reading the bar ahead
- Area: beverage
- Positions and timing: BB; readiness, then ongoing at volume. This is the barback's own job (ice, glass and run-outs are what fail first on a busy night), so it stays in the window; BEV-001 and FLV-002 move to BB ongoing instead.
- What it teaches:
  - The cues: a large party seated (the pre-service view, SYS-111); the late-night turn coming; a run on one drink or component; tickets building at the service well; the morning window opening.
  - What each cue means for stock: glass, ice, citrus, batches, garnish, napkins, the backup well.
  - Moving before the call: restock and reset without crossing a maker's path (BEV-003, BEV-016).
  - Telling the maker what was done, in one line.
- What the person can do afterward: restock before anyone asks on a busy night.
- How it is proven: observation in supervised services, including at least one full night (`workflow.full_night`, D10), and the first unsupervised shifts after sign-off. Prove-first for an experienced barback: the observation is the proof and the 2 h instruction is skipped.
- Time and place: 2 h on site, then ongoing.
- Waits on: the pre-service view (SYS-111); the space (D58).
- Absorbs: BEV-027.

---

## Part 2. The drink list

### BEV-102 The current drink list, at your position's depth
- Area: beverage
- Positions and timing: every CF position; readiness at position depth; re-proven on every list change (D40). Depths and hours: H 1; FR 1.5; BW +3 (4.5 in all); FS +2 (6.5 in all); BB 2; BA 2; BT 6 from outside, +4 from BB (the barback already holds 2 h of the same list); MD 6.5 (FS depth, prove-first); HB 6 (BT depth, normally proven first at hire).
- What it teaches:
  - For every drink on the list (`bev.list.*`): name and pronunciation; category and base; taste in plain words; allergens and dietary status (nut syrups, dairy, egg white, gluten-bearing bases, honey, others HB lists); a one-line and a longer description; who it suits; the dish it goes with where there is one. For the bar: the full spec (glass, ice, method, measures, dilution target, garnish) and the reason for each choice.
  - By position:
    - H: names each drink, knows the list's shape, hands questions to the floor or bar; allergens routed, never answered from memory.
    - FR: one line per drink and the glass it goes in; by-the-glass wines in one line (grape or base, place, style).
    - BW: the by-the-glass wine list at depth (grape, place, style, serving temperature, why it is listed, the dish it is poured with); the rest of the list at one-to-two lines.
    - FS and MD: describe and recommend from every list, with the dish. The MD holds the same depth as the FS, since the MD covers any table.
    - HB: every drink to full spec and the reason for it (HB writes the specs; the check confirms the HB can teach the list as written).
    - BB: name, glass, garnish and ice for every drink; allergens.
    - BA: coffee, tea and non-alcoholic in full.
    - BT: every drink to full spec, wine at back-waiter depth.
  - Category primers, so a description has something to stand on: the six tea categories (white, green, yellow, oolong, black, dark) and that herbal infusions are not tea; spirit bases (grain, agave, cane, grape, botanicals); beer (ale and lager, light to dark, hop-led and malt-led), only if listed; the Korean drinks on the list in one line each (soju, makgeolli, yakju, cheongju; founder-sourced); the coffee service (what Sŏn pours, batched and pulled in the back).
  - The standard answer when unsure: "let me find out", then the bar or the floor lead.
  - Method: study cards per drink, tasting on site (non-drinking route available), spaced recall across the window.
- What the person can do afterward: answer the customer's questions about any drink at their depth, never guess on an allergen, and (bar) build any drink on request.
- How it is proven: a spoken check that follows a lead playing a customer, with a sampled set of drinks; for the bar, the person then builds two. The allergen element passes in every attempt. Recheck on every list change. Prove-first: the list is house-specific, so there is no outside credential, but an experienced hire who studies the cards and passes the spoken check (and, for the bar, the two builds) cold skips the instruction hours; the allergen element is never banked from a cold pass alone and passes in every attempt.
- Time and place: as listed above; study remote, tasting and check on site.
- Waits on: the list and every spec (`bev.list.*`, `bev.spec.*`, HB); `founder.glossary.sool.*` and `founder.glossary.tea.*` (sources unverified); `menu.beer.*`; `compliance.alcohol_tasting`; `brand.*` for any reason a drink is on the list.
- Absorbs: BEV-101 of the beverage-team draft (the drink list, cold); BEV-101 of the other-tracks research (the floor primer); the spec-memory part of BEV-005.

---

## Part 3. The barista-shared set (BA full; BT on the move from BB)

### BEV-103 The house coffee program
- Area: beverage
- Positions and timing: BA full, BT short; readiness. Level 1 of the coffee track.
- What it teaches:
  - What Sŏn pours (`bev.coffee.*`): each coffee, its roaster, origin and process at a short depth (washed, natural, honey; what each does to taste), the roast style, decaf and how it is decaffeinated.
  - Where and how it is pulled: batch-pulled in the back (WP pp.4 to 5, carried; the pulling itself is trained in BEV-120), how it reaches the bar, and its hold time (`bev.spec.espresso.hold`).
  - What drift looks and tastes like in the held product (links to BEV-006).
  - Describing it: one line and a longer version, by what the customer already likes (bright and fruity, round and chocolatey).
  - For the customer: which coffee suits which customer (the one who takes it black and light, the one who wants something rich after a long meal, the caffeine-sensitive customer, the customer who orders decaf late) and which course (with dessert, after it, at the morning window), and how to ask one question to find out.
  - The questions a coffee-literate customer asks, and honest answers: "Why is there no espresso machine at the bar?"; "When was it roasted?"; "Is it single origin?"; "How strong is it?"; caffeine and decaf.
  - Milk and alternative milks as an allergen and dietary route.
- What the person can do afterward: answer three follow-up questions about any coffee on the list, accurately and plainly, and suggest the coffee that suits a described customer and course.
- How it is proven: a spoken check, including two described customers to match to a coffee. Test-out: general coffee knowledge only (an SCA or Barista Hustle certificate, carried as evidence); the house program is always checked.
- Time and place: BA 3 h (2 remote, 1 on site tasting); BT 1.5 h (1 remote, 0.5 on site).
- Waits on: `founder.bev_program_method`; `chef.batch_espresso_method`; `bev.coffee.*`; roaster choice (`vendor.roaster.*`); Brandon interview on the coffee method; Box re-read of WP pp.4 to 5.
- Absorbs: BEV-109 of the beverage-team draft; the coffee half of the old BEV-006 dialing-in row.

### BEV-120 Pulling and holding the batch espresso
- Area: beverage (taught with the kitchen where the pull is shared)
- Positions and timing: whoever pulls the batch espresso in the back; the owner position is set by the chef and HB (`people.espresso_puller`: BA, a kitchen position, or both). Readiness for that position, before the first service on which they pull. BA and BT who only serve it take the hold and drift parts inside BEV-103 and BEV-006.
- What it teaches:
  - Why it is pulled in the back and batched (WP pp.4 to 5, carried; re-read in Box): one standard at any tempo, no dialing in on the floor.
  - The spec and only the spec (`bev.spec.espresso.dose`, `bev.spec.espresso.yield`, `bev.spec.espresso.time`, `bev.spec.espresso.hold`, `bev.spec.espresso.temp`): the dose weighed every time, the yield weighed, the time watched, the batch chilled or held as the spec says, labeled with time pulled, puller and use-by.
  - The method as the chef and HB write it (`chef.batch_espresso_method`), including the equipment steps (`tool.kitchen.espresso_equipment`).
  - Tasting the batch against the reference before release, with the palate checked first (FLV-005).
  - The drift log (`tool.qc_log`): every batch's dose, yield, time and taste call; what a pattern of drift means (grind moving, beans aging, water) and who adjusts it (HB, never the puller alone).
  - Cleaning: what is cleaned after every batch, at close and on the cadence (`workflow.espresso.cleaning`); why old coffee oils taste in the next batch.
  - Hot equipment and hot liquid: the safety steps of the equipment (`tool.kitchen.espresso_equipment`), demonstrated every attempt.
- What the person can do afterward: pull, taste, label, log and hold a batch to spec, and catch a drifting batch before it leaves the back.
- How it is proven: a practical (two batches pulled to spec on separate days, logged, tasted against the reference with HB or LB). Prove-first: an experienced barista pulls one batch cold; the house spec, the log and the equipment safety steps are always demonstrated.
- Time and place: about 2.5 h on site, in the readiness window of whichever position owns it.
- Waits on: `chef.batch_espresso_method` (chef with HB); `bev.spec.espresso.*`; `people.espresso_puller`; `tool.kitchen.espresso_equipment`; `workflow.espresso.cleaning`; `tool.qc_log`; roaster choice (`vendor.roaster.*`); Box re-read of WP pp.4 to 5.
- Absorbs: none (new; fills the gap where `chef.batch_espresso_method` was bound with no module to hold it).

### BEV-104 Tea and matcha to the house standard
- Area: beverage
- Positions and timing: BA, BT; readiness. Level 1 of the tea track.
- What it teaches:
  - Every tea on the list (`bev.tea.*`): category, origin and process at a short depth, caffeine, and a two-line description.
  - For the customer: which tea suits which customer (a coffee drinker who wants something with weight, a customer avoiding caffeine at night, someone who wants something light after a rich course) and which course it goes with (`chef.menu.*` for the dish side), found with one question rather than a recital.
  - The brewing variables and what each does: leaf weight, water temperature, steep time, water quality, re-steeps; the house spec for each tea (`bev.spec.tea.*`). Too hot or too long gives bitter and drying; too cool or too short gives thin.
  - The founder matcha method (`founder.matcha_method`): sifting, water, whisking, texture, and the finished standard.
  - Vessels and presentation per the standards book (D46).
  - Herbal and grain infusions (including Korean grain teas if listed): not tea, usually caffeine-free; allergens (barley and others).
- What the person can do afterward: prepare each tea and matcha drink to spec, say why each variable is set where it is, and suggest a tea for a described customer and course.
- How it is proven: a practical (each tea brewed to spec, one re-steep) and a spoken check that includes two described customers to match to a tea. Test-out: brewing technique only; the matcha method never tests out.
- Time and place: 3.5 h (1 remote, 2.5 on site).
- Waits on: `founder.matcha_method`; `bev.tea.*` and `bev.spec.tea.*` (HB); Korean tea sources (unverified; founder-sourced); `tool.bar.equipment` (kettles, scales).
- Absorbs: BEV-105 of the beverage-team draft; the readiness part of BEV-037.

### BEV-004 Finishing on house-textured milk (drill)
- Area: beverage
- Positions and timing: BA, BT; readiness, conditional on `tool.bar.equipment`. If the front bar has no milk-texturing equipment, this module moves to wherever milk is textured (and to whoever does it), or drops.
- What it teaches:
  - Steam wand safety, first and every time: purge before and after, the tip below the surface before the steam opens, the steam closed before the tip leaves the milk, the hand clear of the wand and the jet, the wand wiped with a cloth, never a bare hand, a hot pitcher held by its handle.
  - Water first: the pour movement drilled with water until steady (BEV-002 method).
  - The milk: the house texture and temperature targets (`bev.spec.milk`), how the house textures it on the bar's equipment (`tool.bar.equipment`; confirm what the front bar has, since there is no espresso machine there).
  - Placing and cutting: the cup angle, where the stream lands, the moment to drop the pitcher, the cut, done before any other movement.
  - The house finish pattern or patterns, set by HB, built from simplified forms first and one element added at a time.
  - Alternative milks (`bev.milk_list`): how each behaves (foam stability, temperature tolerance, splitting) and each one's allergens.
- What the person can do afterward: finish every house milk drink consistently across repeated makes.
- How it is proven: a practical judged on repeated consistency (the same drink several times in a row). Test-out: the same practical at entry. The steam wand safety element is demonstrated on every attempt and never tests out.
- Time and place: 3.5 h on site.
- Waits on: `tool.bar.equipment`; `bev.spec.milk`; `bev.milk_list`; HB's finish standard.
- Absorbs: BEV-004.

### BEV-006 Reading the dispensed product
- Area: beverage
- Positions and timing: BA, BT; readiness. LB owns the pull call on the shift.
- What it teaches:
  - Contrast pairs, side by side, of in-spec and drifted product: batched espresso, matcha, cold coffee, batched cocktails, prepared components.
  - The cues: temperature, oxidation (dull, flat, stale or papery), separation, texture, color, aroma, time on the label.
  - The move: pull it, flag it to LB, log it (`tool.qc_log`), use the backup; never fix it at the counter.
  - Saying it without blame: drift is a process signal, reported to the maker or HB as fact.
- What the person can do afterward: catch drifted product before it reaches a customer.
- How it is proven: a blind contrast check. Prove-first: an experienced hire takes the blind contrast check cold after seeing the references once.
- Time and place: 2 h on site.
- Waits on: HB's drift references; `tool.qc_log`; `chef.batch_espresso_method`.
- Absorbs: BEV-006.

### BEV-025 The customer not drinking alcohol
- Area: beverage
- Positions and timing: BA, BT; readiness. FS takes the floor part, readiness, inside the move from BW.
- What it teaches:
  - Equal ceremony: the same glass quality, care, garnish, description and pace as any drink; offered without spotlight; never a lesser default.
  - Never asking why. Pregnancy, recovery, faith, health, driving, preference: none of it is the house's business.
  - Every non-alcoholic drink on the list (`bev.list.na.*`), in full; any non-alcoholic pairing and how it is presented.
  - What replaces alcohol's body and length in the house drinks: acid, tannin from tea, bitterness, spice heat, salt, sugar's body, carbonation, aroma (taught in depth in BEV-040).
  - Trace alcohol: which drinks carry it (fermented drinks, some bitters, some extracts) and how to say so plainly (`compliance.alcohol_trace`).
  - One non-alcoholic build at the bar.
- What the person can do afterward: serve and recommend a non-alcoholic drink with the same care and depth as any other, without a single question about why.
- How it is proven: a role-play (three customers, one who does not say they are not drinking) and a build. Prove-first: an experienced hire reads the non-alcoholic list and takes the role-play and the build cold.
- Time and place: 2 h on site (BA, BT); 1 h on site (FS floor part).
- Waits on: the non-alcoholic list and pairing (HB); `compliance.alcohol_trace`; `founder.glossary` for the house's word for these drinks.
- Absorbs: BEV-025.

### FLV-005 Checking your palate before you judge
- Area: beverage
- Positions and timing: BA, BT; readiness. Anyone who tastes for quality takes it before their first quality call.
- What it teaches:
  - A fixed reference tasted before any quality call (`bev.palate_reference`): if it does not taste as it should, the palate is off, not the product.
  - What shifts a palate that day: coffee, mint or toothpaste, smoking, a spicy staff meal, sugar, illness, fatigue.
  - Rinse water between tastes; one clean spoon or straw per taste.
  - When unsure, defer to a second taster. A quality call made on a shifted palate is not made.
- What the person can do afterward: run the check unprompted before tasting product for quality.
- How it is proven: observation in supervised services. Prove-first: an experienced hire reads the routine and is observed running it; the instruction hour is skipped.
- Time and place: 1 h on site.
- Waits on: `bev.palate_reference` (HB).
- Absorbs: FLV-005.

### BEV-020 Holding the spec or moving it
- Area: beverage
- Positions and timing: BA, BT; readiness.
- What it teaches:
  - When conditions change: citrus that is sharper or flatter than usual, a different ice, a batch near its hold time, a humid night.
  - What may move, and within what range (`bev.spec.ranges`, HB): stir or shake time for dilution, a citrus adjustment within its range, the ice choice.
  - What never moves: the base, the ratios outside their range, allergen-bearing ingredients, glass and garnish.
  - Who to tell: LB on the shift, logged for HB.
  - What is never freelanced: a new ingredient, a substitution for an out-of-stock item (that goes to LB, and the floor is told).
- What the person can do afterward: make the call in a scenario and give the reason.
- How it is proven: a branching scenario, compared with HB's own answers. Prove-first for an experienced external BT: read the ranges, then take the scenario cold.
- Time and place: 1.5 h (0.5 remote, 1 on site).
- Waits on: `bev.spec.ranges` (HB).
- Absorbs: BEV-020.

### BEV-026 The morning window
- Area: beverage
- Positions and timing: BA, and whoever works the window; readiness, when mornings run (D24).
- What it teaches:
  - The walk-up window in the mornings (BG 14, cited) and the morning register (ORI-020): quick, warm, spare.
  - Standing orders and regulars: recognizing them by a check, never a memory gamble; the record (SYS-111, SYS-112).
  - The pace at the window, and what is never cut: the allergen question, the read-back, the spec, the glass or cup standard.
  - Queue triage: taking orders in sequence, building by build time, calling names clearly, telling the next customer the honest wait.
  - Payment at the window (SYS-130 counter part).
- What the person can do afterward: run the window at morning tempo without dropping the standard.
- How it is proven: a role-play at tempo, then supervised morning services. Prove-first: an experienced hire takes the role-play cold; the supervised morning services stay (a person is released only for the dayparts in which they were supervised, D10).
- Time and place: 3 h on site.
- Waits on: `workflow.daypart.morning` (D24); whether mornings run at opening; `tool.reservations.*` and `tool.pos.*` for regulars and payment; BG 14 re-read.
- Absorbs: BEV-026.

---

## Part 4. The bartender set, and the gate items held as a barback

### BEV-008 The house tasting grid
- Area: beverage
- Positions and timing: BB ongoing, a hard gate to BT; BA ongoing; BW and FS take it inside the wine levels (BEV-110, BEV-111).
- What it teaches:
  - One grid for every drink, adapted from published grids (WSET Systematic Approach to Tasting, CMS Deductive Tasting Method; both verified-primary, carried):
    - Sight: clarity, color, intensity.
    - Nose: condition (clean or faulty), intensity, aroma families (FLV-002).
    - Palate: sweetness, acidity, bitterness, tannin or astringency, alcohol or body, texture, flavor intensity, flavors.
    - Finish: length.
    - Conclusion: quality, and fit for Sŏn and its food.
  - Two languages. Team words make calibration and product feedback possible. Customer words carry the same meaning plainly: acidity as "bright, mouthwatering"; tannin as "drying, like strong tea"; body as "light like skim milk or full like cream" (carried from the wine research). Non-experts rarely share the meaning of expert terms (Food Quality and Preference 2021, verified-secondary, carried), so team words are never spoken at the table.
- What the person can do afterward: describe a drink on the grid to the team, then again in plain words to a customer.
- How it is proven: a spoken check over three drinks, each described twice. Test-out: the same check cold.
- Time and place: 2 h on site.
- Waits on: HB adopting the grid and the house words; `policy.tasting_on_paid_time`.
- Absorbs: BEV-008; FLV-001.

### BEV-012 The build (drills)
- Area: beverage
- Positions and timing: BB ongoing, a hard gate to BT; BT holds it on entry.
- What it teaches:
  - Hands separately, then together: measuring with each hand, then two jiggers, then measuring while the other hand sets glass and ice.
  - Shake: ice fill, seal, a hard full-length shake, the house length (`bev.spec.shake`), open cleanly; dry and reverse-dry shakes for foam.
  - Stir: ice, spoon movement that turns the ice without chipping it, the house time or count (`bev.spec.stir`).
  - Strain: hawthorne, julep, fine strain, and when each is used.
  - Built drinks and toppers: soda added last and not stirred flat.
  - Every method checked against dilution and temperature targets with a scale and a thermometer (`bev.spec.dilution_targets`).
  - The tempo ladder: slow and correct, then faster, then several drinks at once, then with a customer talking.
- What the person can do afterward: build any house drink to spec at tempo with dilution and temperature inside the range.
- How it is proven: a banked drill and a practical with measured targets. Test-out: the same practical at entry.
- Time and place: 8 h on site, in short blocks over weeks.
- Waits on: `bev.spec.*` targets (HB); bar equipment (`tool.bar.equipment`).
- Absorbs: BEV-012, BEV-013.

### BEV-005 Classic drinks and their families
- Area: beverage
- Positions and timing: BB ongoing, a hard gate to BT; BT holds it on entry; BA by analogy, open.
- What it teaches:
  - The cocktail families (WSET Spirits Level 2 framing, verified-primary, carried): spirit-forward, short sours, highballs, long sours; and the classic drink each family grows from.
  - Each classic's template (`bev.spec.templates`): what is strong, what is sweet, what is sour or bitter, what is diluting.
  - Balance and seasoning: sweet against sour, strength against dilution, bitterness and salt as seasoning.
  - Each house drink mapped to its classic, and why it departs from it.
  - How a reasoned variation is built: change one element, rebalance the rest, taste, write it (BEV-030).
- What the person can do afterward: explain why a house spec is built as it is and propose a reasoned variation.
- How it is proven: a spoken check, then one variation built and explained. Test-out: the spoken check cold.
- Time and place: 6 h (3 remote, 3 on site).
- Waits on: `bev.spec.templates`, the list (HB).
- Absorbs: BEV-005 (the reasoning part; spec memory moved to BEV-102).

### BEV-105 Spirits on the back bar
- Area: beverage
- Positions and timing: full part held before the BT window (BB ongoing, a hard gate to BT); readiness only for an experienced external BT. Recognition part: BB and BA, readiness, counted in Block D. Level 1 of the spirits track.
- What it teaches:
  - Production in four stages (WSET framing, verified-primary, carried): raw material, fermentation, distillation, what happens after (aging, blending, flavoring). Pot and column stills in taste terms. Aged and unaged.
  - The categories by base: whisky, vodka, gin, rum, tequila and mezcal, brandy, liqueurs, aromatized wines, and any Korean spirits on the back bar.
  - For every bottle on the back bar (`bev.back_bar.*`): category, base, origin, how it is made, how it tastes, an alternative to offer, allergen status as HB records it, and the neat pour (measure, glass, ice or water).
  - Walking a customer one step from what they drink now.
  - Product feedback: one MNU-101 note on a back-bar bottle (how it tastes against its neighbors, who asks for it, whether it earns its place), given to HB.
  - Where each bottle lives (`workflow.bar.back_bar_map`, D58).
  - Recognition part (BB, BA): find any bottle by name, know its category, and hand questions to the bartender.
- What the person can do afterward: find, name and describe any bottle in seconds, suggest a neighbor to a customer's usual, pour neat to spec, and give HB one reasoned note on a bottle.
- How it is proven: a spoken walk of the back bar with LB, a blind category set, and a recheck on every back-bar change. Test-out: category knowledge (WSET Spirits Level 2 or similar, carried as evidence); the house back bar is always checked.
- Time and place: BT 6 h (2 remote, 4 on site); recognition 2 h on site.
- Waits on: `bev.back_bar.*` (HB); `workflow.bar.back_bar_map` (D58); `compliance.alcohol_tasting`.
- Absorbs: BEV-107 of the beverage-team draft; the readiness part of BEV-035.

### BEV-015 Opening and pouring wine and sparkling (drill)
- Area: beverage
- Positions and timing: BW ongoing, part of the hard gate to FS; FS holds it on entry; BT bar part, readiness.
- What it teaches:
  - Presenting the bottle: label to the person who ordered, vintage confirmed aloud.
  - Still wine: the foil cut cleanly below the lip, the corkscrew set straight, the cork drawn quietly in two steps, the neck wiped, the cork checked (and presented if the standards book says so, D46).
  - Sparkling, with safety first: the thumb stays on the cork from the moment the cage loosens; the bottle points away from every person; the bottle is turned, not the cork; the cork eased out with no pop; poured in two motions so it does not foam over.
  - The tasting pour to the person who ordered, then the pour order around the table (`workflow.pour_order`) and the pour level (`bev.pour_levels`).
  - Decanting: for sediment (poured steadily, watched at the neck under light, stopped at the sediment) or for air; always offered in the customer's interest, never as theater.
  - A refused bottle: fault or preference, what the person may do, and who decides (`policy.returned_bottle`); never arguing with the customer.
  - Open-bottle care for by-the-glass wine: stopper, date and time on the bottle, the house preservation method (`tool.bar.wine_preservation`), when an open bottle is retired (`bev.spec.open_bottle_hold`).
  - Drill method: the movements drilled apart from the talk, then joined (ORI-016).
- What the person can do afterward: open, present, pour and decant still and sparkling wine smoothly and safely while talking with the customer.
- How it is proven: a practical at a mock table with a lead; recheck on the drill cadence. Test-out: experienced people skip the drill hours and demonstrate live; the sparkling safety element is always demonstrated and never tests out.
- Time and place: 6 h on site (BW); 2 h on site (BT bar part).
- Waits on: `workflow.pour_order`, `bev.pour_levels`, `policy.returned_bottle`, `tool.bar.wine_preservation`, `bev.spec.open_bottle_hold`; `people.wine_service_owner`; the standards book (D46).
- Absorbs: BEV-015; the wine-glass part of SVC-071; the opening half of BEV-108 of the beverage-team draft.

### BEV-023 Hosting the counter
- Area: beverage
- Positions and timing: BT; readiness. BA at the window draws on it.
- What it teaches:
  - The counter as a table: the same arrival, read and step-back service as the floor (BG 15, cited), at arm's length.
  - Acknowledging a customer at once, even mid-build, with a look or a word; water and the menu.
  - Reading a solo customer: wants conversation or not (a book, a phone, posture, how they answer the first question); reading a pair or a group.
  - When to talk and when to step back; never performing; never explaining to someone who knows more.
  - Pacing a counter meal if the bar sells food: order capture (SVC-032 counter part), firing with the kitchen, clearing (`workflow.bar.counter_food`).
  - The waiting customer bridged from the door (SVC-059 bar part) and handed back when the table is ready.
- What the person can do afterward: host a full counter at tempo while making.
- How it is proven: observation in supervised services, with a short debrief per shift. Prove-first for an experienced external BT: the observation is the proof and the instruction hours are skipped; a miss routes the person into the instruction.
- Time and place: 2.5 h (0.5 remote, 2 on site).
- Waits on: BG 15 re-read; `workflow.bar.counter_food`; the counter layout (D58).
- Absorbs: BEV-023.

### BEV-021 Two queues: the counter and the service well
- Area: beverage
- Positions and timing: BT; readiness. BA at the morning rush draws on it.
- What it teaches:
  - Two customers at once: the counter in front of you, and the tables behind the service-well tickets.
  - Ticket age against the counter: the house limit for a ticket's age (`workflow.bar.ticket_age_limit`) and the counter's honest wait.
  - Triage: acknowledge the counter at once; group similar builds; fire the oldest ticket; never let one queue starve.
  - Calling for help early: the barback for stock, LB for a hand at the well (SVC-079 principle).
  - Telling the floor when the well is behind, so the server can tell the table.
- What the person can do afterward: hold both queues in a simulated rush with no ticket past the limit and no counter customer unacknowledged.
- How it is proven: a simulation, then supervised services. Prove-first for an experienced external BT: the simulation cold, then the supervised-service observation.
- Time and place: 2 h on site.
- Waits on: `workflow.bar.ticket_age_limit`; `workflow.bar.well_staffing`.
- Absorbs: BEV-021.

### BEV-116 Beer: serving, styles and freshness
- Area: beverage
- Positions and timing: only if beer is listed (`menu.beer.*`). Serving part: readiness for BT and BB. Style part: ongoing, open. Owner step: only if beer becomes a program.
- What it teaches:
  - Serving part:
    - The beer-clean glass and its tests (sheeting water, salt test, lacing, no bubbles clinging to the wall).
    - Pouring draft (glass angled, tap opened fully, straightened to build the head) and bottle or can; the head right for the style.
    - Line and keg basics; when to call for line cleaning (`workflow.bar.draft_lines`).
    - Bad pours and what they look and taste like: flat, overfoamed, a buttery or sour note from a dirty line.
    - The three common ways beer is ruined after the brewery: light, heat and time, oxygen (Cicerone Certified Beer Server syllabus, verified-primary, carried).
  - Style part (matched to the Certified Beer Server syllabus, verified-primary, carried): style families and flavor language; pairing basics with the menu; recommending from what the customer drinks now (a lager drinker one step toward a pilsner or a rice lager, a wine drinker toward a sour or a saison, a customer who says "I don't like beer"); one MNU-101 note on a listed beer (freshness on arrival, how it sits with the food, what customers said).
  - Owner step (matched to Certified Cicerone scope, verified-primary, carried): off-flavors, the draft system, tasting and evaluation.
- What the person can do afterward: pour and serve every beer to standard and describe it plainly; at the style level, recommend a beer from what the customer drinks now and give HB one reasoned note on a listed beer.
- How it is proven: a serving practical; a spoken style check; the owner step by tasting and demonstration with HB. Test-out: a Certified Beer Server skips the style check; the serving practical stays.
- Time and place: serving 3 h on site; style part 6 to 8 h; owner step about 60 h.
- Waits on: whether beer is listed (`menu.beer.*`); the draft system (D58); the D27 answer from Cicerone; fees as `fact.fee.cicerone.*`.
- Absorbs: BEV-106 and BEV-108 of the earlier drafts; BEV-038, BEV-039; the beer part of BEV-035.

### BEV-028 Korean drinks: soju, makgeolli, yakju and cheongju
- Area: beverage
- Positions and timing: short part, readiness for BT if listed; floor level for BW and FS, a soft gate to FS; full part, ongoing, open.
- What it teaches:
  - Short part: what each Korean drink on the list is (soju, diluted and traditionally distilled; makgeolli, cloudy and living; yakju and cheongju, clear and refined), how each tastes, how it is stored, how it is poured and served at the Korean table (`founder.glossary.sool.*`), and its allergens.
  - Full part: fermentation with nuruk compared with koji; regional producers; the history told accurately, never as marketing; pairing with the menu; serving a customer who knows these drinks better than you, as a peer.
  - For the customer, at both levels: recommending from what the customer drinks now (a sake drinker toward yakju or cheongju, a natural wine or sour beer drinker toward makgeolli, a vodka or shochu drinker toward a traditionally distilled soju), not only by pairing.
  - Product feedback: one MNU-101 note on a listed Korean drink (how it held after opening, how customers took to it, how it met the dish).
  - Sources: none verified (carried). Content is founder-sourced and verified before drafting. WSET Sake (lead-only, carried) is an analog for rice fermentation only.
- What the person can do afterward: describe and serve each Korean drink correctly, tell its story honestly in plain words, suggest one from what a customer drinks now, and give HB one reasoned note.
- How it is proven: a spoken check with LB or HB; the full part through a conversation. Test-out: the spoken check, for those with prior knowledge.
- Time and place: short part 2 h (1 remote, 1 on site); full part about 15 h.
- Waits on: whether these drinks are listed; `founder.glossary.sool.*`; verified sources; Brandon interview.
- Absorbs: BEV-028; the sool part of BEV-035.

---

## Part 5. The wine track (gates hardest; ongoing education, never inside a window, D55)

Design rules for the whole track (carried from the wine research):
- Knowledge goes to full depth.
- Translating for the customer and reading the customer are separate, required elements that never test out.
- Expert vocabulary is a team tool; its absence at the table is graded.
- Selling and recommending practice sits inside the track. Orlowski 2022 (International Hospitality Review; verified-primary, carried): WSET Level 2 raised knowledge but not wine sales against control units, and trainees named missing selling practice.
- A CMS or WSET certificate counts toward theory test-outs only. Whether Sŏn pays for an outside exam is `policy.wine_cert_sponsorship`.
- Product feedback for every level goes through MNU-101.

### BEV-110 Wine 1: what is in the glass and how to say it
- Area: beverage
- Positions and timing: FR, ongoing after release; a hard gate to BW. Open to H, BB, BA by request (a short unblock conversation, D13).
- What it teaches:
  - How wine is made, in plain words: grape, fermentation, still, sparkling, fortified; why a wine is white, red, rosé or orange.
  - The structure words a customer understands, each tasted: sweet or dry; acidity as mouthwatering; tannin as drying, like strong tea; body as light like skim milk or full like cream; oak.
  - The eight principal grapes as a reference set (Chardonnay, Sauvignon Blanc, Riesling, Pinot Grigio or Gris, Cabernet Sauvignon, Merlot, Pinot Noir, Syrah or Shiraz; the WSET Level 2 set, verified-primary, carried), each with one plain sentence on style.
  - Sŏn's by-the-glass list: each wine's name, color, style in one sentence, and the dish it is poured with (`bev.wine_list.by_the_glass`).
  - Glassware: which glass for which wine; held by the stem, never the bowl rim (standards book, D46).
  - Handling: serving temperature by style in plain terms (`bev.spec.wine_temps`); recognizing a wine that looks or smells wrong, so it is handed off.
  - Answering "what is this?" in one honest sentence, and "let me bring someone who knows it best" instead of guessing.
  - For the customer: who on our floor would order each by-the-glass wine (the customer who wants something crisp with the first courses, the red drinker at a seafood-led meal, the customer who wants one glass and no fuss), so the runner can say a true sentence about it when asked.
  - Product feedback: after a staff tasting, one MNU-101 note on a by-the-glass wine (what it tasted like next to the dish, who you think would order it).
  - Smell work built on FLV-002; the grid at this level (BEV-008).
- What the person can do afterward: name and describe any by-the-glass wine plainly at the table, say who would enjoy it, match glass to wine, catch an obviously off glass, hand off a deeper question, and write one useful note on a wine.
- How it is proven: a spoken check with HB or LB (describe three house wines to a lead playing a customer); a sighted tasting placing each wine on sweet, acid, tannin and body in customer words only; the facts as a Trainual native test (it records a score); a recheck on every by-the-glass change. Test-out: a CMS Introductory or WSET Level 2 holder, or an experienced fine-dining runner, skips the study hours; the spoken check and tasting on Sŏn's list stay. An experienced external BW (who arrives above this gate) proves it the same way in a cold check of about 2 h, so an outside hire holds the same gate an internal runner must hold.
- Time and place: about 10 h (5 remote, 4 on site in tastings, 1 for the check), inside scheduled weeks.
- Waits on: the HB hire (`people.head_of_beverage`); `bev.wine_list.*`; `bev.spec.wine_temps`; the standards book (D46); `policy.tasting_on_paid_time`; the non-drinking route confirmed with Brandon; `policy.promotion_gates`.
- Absorbs: the entry part of BEV-010; the wine application of FLV-002 and SVC-008.

### BEV-111 Wine 2: the whole list by style, the pour, the pairing reason
- Area: beverage
- Positions and timing: BW, ongoing; with BEV-015, a hard gate to FS. BT full level, a soft gate to LB. An external FS proves it before release (the Trainual test, the spoken check, the faulted-sample tasting and the pour practical, prove-first; about 4 h).
- What it teaches:
  - WSET Level 2 depth (verified-primary, carried), taught through Sŏn's own list:
    - The principal grapes and the regional grapes on the list.
    - How climate, place and winemaking shape style: cool and warm climate, oak or none, lees, sweetness levels, sparkling methods at an introductory level.
    - The regions and label terms that appear on the list.
  - Every wine on the list by style group: a plain description, who would enjoy it, and which dishes it suits (`bev.wine_list.*`, `chef.menu.*`).
  - Why each current pairing works: what in the dish meets what in the wine, and the plain sentence said at the table (food side `chef.pairing_components`).
  - Pouring and top-ups: read the customer's pace, ask before pouring, read the bottle level, never empty a bottle without offering; the pour volume (`bev.pour_sizes`); changing glasses between wines (`workflow.glass_change`).
  - Faults: cork taint, oxidation, heat damage; what to do (remove the glass, tell the server or the wine seat, never argue).
  - First-level product feedback through MNU-101: after a staff tasting, one useful note on a wine (who on Sŏn's floor would order it, what it goes with, what customers said).
- What the person can do afterward: describe any wine on the list plainly and say who would like it; explain every current pairing in one or two sentences; top up and change glasses to the standard; catch a faulted bottle.
- How it is proven: a spoken check (a lead names three wines and two pairings; the person explains them to a "customer"); a tasting of three wines including one faulted sample; a pour practical inside a paid drill service; a Trainual native test on the facts; recheck on each list or menu change. Test-out: a WSET Level 2 or CMS Introductory holder tests out of the theory hours by passing the Trainual test; no test-out for the Sŏn list, the pairings or the pour practical.
- Time and place: about 30 h over several weeks (12 remote, 14 on site in tastings and pour drills, 4 for checks).
- Waits on: HB; `bev.wine_list.*`; `chef.menu.*`, `chef.pairing_components`; `bev.pour_sizes`; `workflow.glass_change`; `people.wine_service_owner` (whether BW pours bottles); `policy.tasting_on_paid_time`, `policy.promotion_gates`.
- Absorbs: BEV-102 of the wine research; the wine applications of BEV-008 and FLV-005; the explaining half of BEV-042.

### BEV-112 Wine 3: Sommelier 1-level knowledge on Sŏn's list
- Area: beverage
- Positions and timing: BW, ongoing, a hard gate to FS and a condition of the FS role; a required re-proof for an external FS (the integrated spoken check and tasting, about 6 h); LS holds it. For the MD it is proposed as a hiring requirement, proven at the paid practical interview or the first week, pending Brandon's call on whether D55 applies to the manager pair.
- What it teaches:
  - The full scope of the CMS Introductory curriculum (verified-primary, carried): the major regions of the world with their classic appellations, classifications and label law; grape growing and winemaking in depth; sparkling methods and fortified wines; beer, sake and spirits at an introductory level; pairing principles; service standards. The region-by-region depth sits in the CMS workbook behind enrollment (lead-only, carried); HB sets Sŏn's depth against it.
  - A deductive tasting method used inside the team (BEV-008 grid) for calibration and feedback, never recited to a customer.
  - Sŏn's whole list in depth: producer, place, how it was made, why it is on the list, who it is for (`bev.wine_list.*`; brand reasons only from the Brand Guidelines or `brand.*`).
  - Translation: the same wine described twice, once in team language and once in customer language. Customer language uses comparisons the person already knows, says what the wine will feel like with the dish, and leaves no unexplained term.
  - Keeping current: a new vintage, a wine running out, its replacement.
  - Product feedback at list level: one MNU-101 note on the list as a whole (a gap the list leaves for a kind of customer or a dish, or a wine customers avoid, and why).
  - Paced in dated sections set by HB against the list (`bev.wine_list.sections`; for example sparkling, white, red, sweet and fortified, other beverages), each with its own short check, so a back waiter studying while working full time has a sequence of reachable steps rather than one large gate.
- What the person can do afterward: answer an expert customer's second and third question accurately; explain any wine to a nervous customer with no jargon; talk through the list's logic; taste a wine and place it with the team.
- How it is proven: dated section checks (a Trainual native test and a short spoken check per section), each banked when passed; then the integrated check, never banked: a spoken check with HB (a conversation across the list and the world's regions, not a recitation) and a tasting of three wines, each described twice, the customer version graded on clarity and honesty; the list-level MNU-101 note is reviewed with HB. Recheck on list changes and on the recheck cadence. Test-out: a CMS Introductory, Certified or WSET Level 3 holder tests out of the theory hours by passing the section tests and the spoken check. The translation and Sŏn-list elements are always proven; prove-first is allowed.
- Time and place: about 60 h (30 remote, 24 on site in tastings and list sessions, 6 for checks), paced by `policy.ongoing_education_hours.bw`; at 4 paid hours a week that is about 15 weeks. For scale, WSET Level 3 sets a minimum of 84 study hours (verified-primary, carried).
- Waits on: HB; `bev.wine_list.*`, `bev.wine_list.sections`; `brand.*`; `policy.promotion_gates`; `policy.tasting_on_paid_time`; `policy.ongoing_education_hours.*`; Brandon on whether level 3 is a hiring requirement for the MD; Brandon interview on what "Sommelier 1 level" means to him in practice.
- Absorbs: BEV-103 of the wine research; the depth part of BEV-010.

### BEV-113 Recommending wine: reading the customer and choosing with them
- Area: beverage (taught with service; kept consistent with SVC-033)
- Positions and timing: FS, part of the hard gate and ongoing after it; BW a light version for by-the-glass questions; BT where the bar sells wine.
- What it teaches:
  - Opening questions that find what the customer wants: what they love to drink, what they had last that they liked, the occasion, how adventurous they feel tonight.
  - Reading the table: who is choosing, a split table, an expert testing you, a nervous or embarrassed customer.
  - Budget without naming a number: pointing at the list and letting the customer set the range (`policy.price_conversation`).
  - Two or three options with plain reasons, including the less expensive choice when it fits better.
  - Honesty: saying when a wine will not suit the dish or the customer; never overselling.
  - The table that does not want wine: the non-alcoholic and by-the-glass alternatives (BEV-025).
  - Afterward: checking back after the first sip; the note for the next visit (SYS-112).
  - Evidence behind the design: Orlowski 2022 (verified-primary, carried); suggesting a food pairing lowers the customer's sense of risk in choosing (Terrier and Jaquinet 2016, lead-only, carried; not cited to a learner until verified).
- What the person can do afterward: lead a table from "I don't know wine" to a choice they are glad of, without jargon or pressure, and serve an expert customer as a peer.
- How it is proven: role-play with a prebrief against set customer profiles, a lead playing each (the first-timer, the expert, the split table, the budget-conscious host, the customer who rejects the first suggestion), graded on questions asked, listening, plain language, fit, and whether the customer kept control of the choice; then observed on the floor with a debrief. Prove-first for an experienced FS: the same role-play set, cold (about 2 h); a pass banks the role-play, and floor observation with a debrief follows after release. No outside certificate counts here, since none examines this skill.
- Time and place: about 10 h on site (role-play blocks, plus observation inside normal shifts).
- Waits on: `policy.price_conversation`; `people.wine_service_owner` (who closes the bottle sale); SYS-112 note standard; Brandon interview on how Sŏn recommends.
- Absorbs: BEV-104 of the wine research; the wine applications of SVC-033, SVC-008 and SVC-016.

### BEV-042 Presenting the pairing
- Area: beverage
- Positions and timing: FS, readiness inside the move from BW, then re-proven on every pairing change; MD in the MD window; BT where the bar pours the pairing.
- What it teaches:
  - Each current pairing (`bev.pairings.*`): what in the dish meets what in the wine or drink, named on the grid.
  - The one-breath version said at the table, and the longer version for the curious customer.
  - Adjusting for a customer who dislikes the pour, or who is not drinking (the non-alcoholic pairing, BEV-025).
  - Tasting each pairing together, with the food, before it goes live.
- What the person can do afterward: present every current pairing so the customer understands why it is there, and adjust it graciously.
- How it is proven: each pairing tasted with HB and the chef, then presented to them; recheck on every change. Prove-first: the pairings are Sŏn's, but an experienced hire who tastes them once may present cold; the tasting with the food always happens.
- Time and place: 2 h on site per change.
- Waits on: `chef.menu.*`, `chef.pairing_components`, `bev.pairings.*`, HB, `people.wine_service_owner`.
- Absorbs: BEV-042.

### BEV-114 Wine beyond the front server
- Area: beverage
- Positions and timing: elective, open to anyone who holds BEV-112; the path toward a wine seat if one is created (`people.wine_service_owner`). HB holds above this level at hire and teaches it.
- What it teaches:
  - Study toward CMS Certified or WSET Level 3 depth (verified-primary, carried): blind tasting to a standard; regions in more depth; the hospitality and service practical CMS Certified examines.
  - Running a staff tasting and teaching BEV-110 and BEV-111.
  - Helping HB on the list: tasting submissions, writing list notes, product feedback at program level (MNU-101).
- What the person can do afterward: taste blind to the Certified standard, teach the first two wine levels, and hold the wine seat if it exists.
- How it is proven: a spoken check and a blind tasting with HB. An outside certificate counts as evidence only if uploaded and tracked in Trainual.
- Time and place: open; paid study time set by policy.
- Waits on: `policy.wine_cert_sponsorship`; `fact.fee.cms.*`, `fact.fee.wset.*`; the D27 answer from providers; `people.wine_service_owner`.
- Absorbs: BEV-106 of the wine research; the elective part of BEV-010.

---

## Part 6. The other tracks: ongoing education

### BEV-035 Spirits in depth
- Area: beverage
- Positions and timing: part one, a soft gate from BW to FS (after-dinner spirits) and a proposed hard gate from BT to LB; the full module for LB and HB; open to anyone. Ongoing.
- What it teaches:
  - Part one (matched to WSET Spirits Level 2, verified-primary, carried): the four production stages in more depth; whisky, vodka, tequila, mezcal, rum, gin, liqueurs and aromatized wines; cocktail families; after-dinner spirits on Sŏn's list and how to offer them with dessert, starting from what the customer drinks now; one MNU-101 note on a back-bar bottle.
  - Full (matched to WSET Spirits Level 3, verified-primary, carried): production choices and their effect on style (raw material, yeast, still type, cut points, cask type and age, blending); legal categories and labeling for the main spirits; the named global spirits; blind assessment of quality on the shared grid (BEV-008); plain description for a customer; reasoned product feedback to HB (MNU-101).
- What the person can do afterward: part one, describe and recommend the after-dinner list and any category, and give HB one reasoned note on a bottle; full, blind-describe and place two spirits, judge their quality, and explain a production choice to a customer without jargon.
- How it is proven: part one, a spoken check and a tasting; full, a blind tasting of two spirits and a spoken explanation of one production choice; recheck yearly. Test-out: WSET Spirits Level 2 or Level 3 holders take only the house-list conversation at the matching level.
- Time and place: part one about 20 h; full about 70 h over six to nine months. Reading remote and paid; tastings on site.
- Waits on: the D27 answer from WSET providers; `fact.fee.wset.spirits.*`; `policy.outside_certification_funding`; `compliance.alcohol_tasting`.
- Absorbs: BEV-035 (spirits part; its beer part went to BEV-116, its sool part to BEV-028, its readiness part to BEV-105).

### BEV-036 Coffee craft
- Area: beverage
- Positions and timing: BA within the first months after release (soft); BT and LB on the way to lead; open to anyone. Level 2 of the coffee track. Ongoing. The readiness need for espresso is the back pull, trained in BEV-120; this module is the understanding behind it.
- What it teaches:
  - Extraction and strength as two separate measures; under- and over-extraction by taste; the refractometer as a check.
  - Grind, dose, ratio, time and temperature, and how each moves taste.
  - Water as an ingredient: hardness and alkalinity, and why scale protection and flavor pull opposite ways.
  - Espresso mechanics and channeling, applied to the batch pull in the back (BEV-120): reading the pulled product, what a drifting dose or yield does to taste, and what to report. Percolation and immersion; batch brew.
  - Elective, conditional on equipment (`tool.bar.equipment`): hand espresso and manual brewing, only if such equipment exists on site; never a readiness item.
  - Freshness and storage; milk chemistry basics.
  - Describing coffee by what the customer already likes, and recommending one for a customer and a course.
  - Product feedback: one level-2 note to HB on a coffee (how it held across a service, how customers took to it, what it needs from the roaster), the step before roaster feedback in BEV-117.
  - Scope matched to SCA Barista Skills and Brewing at the intermediate level, and Barista Hustle Barista One, Percolation, Immersion and part of Advanced Coffee Making (verified-primary, carried).
- What the person can do afterward: dial a coffee to a target by taste and measurement, explain the change to a peer, recommend a coffee from a customer's stated taste, and give HB one reasoned note on a coffee.
- How it is proven: a practical (dial in a supplied coffee to a target recipe; a blind triangle on extraction faults); a spoken explanation of one change; recheck yearly. Test-out: an SCA Barista Skills intermediate (or higher) certificate or a Barista Hustle Baseline certificate, plus the practical.
- Time and place: about 40 h over three to six months (about 15 remote; drills and practicals on site).
- Waits on: BEV-120 and `chef.batch_espresso_method`; whether any hand espresso or brewing equipment exists on site (`tool.bar.equipment`); `policy.ongoing_education_hours.ba`; `policy.outside_certification_funding`; the D27 answer from SCA providers and Barista Hustle; `fact.fee.*`.
- Absorbs: BEV-036; the coffee slice of BEV-001.

### BEV-117 Owning the coffee program
- Area: beverage
- Positions and timing: whoever is named coffee program owner (`people.coffee_program_owner`): HB, LB, or a barista chosen for it; soft gate for that role; ongoing. Level 3 of the coffee track.
- What it teaches:
  - Cupping and calibration on a fixed protocol (SCA cupping and the Barista Hustle Cupping Protocols as reference, verified-primary, carried); a shared descriptive vocabulary.
  - Quality control across a shift: when to taste, what to log (`tool.qc_log`), when to pull.
  - Working with the roaster: roast feedback, rotation, freshness windows (`vendor.roaster.*`).
  - The water specification for the site.
  - Structuring a coffee menu: range, rotation, decaf and caffeine-free options, pairing with dessert (`chef.*`). Cost inputs as `fact.*` only.
  - Training and calibrating others.
  - Benchmark: SCA Barista Skills professional level plus Sensory Skills intermediate, or Barista Hustle Advanced Coffee Making, Coffee Quality Control and The Water Course (verified-primary, carried). The Q Grader is not needed unless Sŏn buys green coffee (CQI, verified-primary, carried).
- What the person can do afterward: hold the coffee standard across makers and days, give the roaster usable feedback, and propose a coffee menu change with reasons.
- How it is proven: a presentation to Brandon and HB (a menu proposal with tasting); one calibration session run while observed; recheck yearly. Test-out: SCA professional-level or Coffee Diploma holders present directly.
- Time and place: 80 to 120 h over six to twelve months; tasting and calibration on site, reading remote and paid.
- Waits on: Brandon on whether the role exists and its title; roaster choice; `tool.qc_log`; the HB hire.
- Absorbs: BEV-105 of the other-tracks research; the coffee slices of BEV-019 and BEV-030.

### BEV-037 Tea craft and tea service
- Area: beverage
- Positions and timing: BA and BT within the first months (soft); FS floor level, a soft gate from BW; open. Level 2 of the tea track. Ongoing.
- What it teaches:
  - How processing makes the six categories; cultivar and place in brief.
  - Brewing: leaf ratio, water temperature, time, vessel, re-steeps; Western and gongfu-style brewing.
  - Water for tea.
  - Korean tea: the teas on the list and how tea is served at the Korean table (`founder.glossary.tea.*`; sources unverified, verified before drafting).
  - Matcha and powdered tea (the house method stays founder-gated, BEV-104).
  - Tea with food; tea in mixed drinks; caffeine questions; describing tea to a coffee drinker.
  - Scope matched to the World Tea Academy Certified Tea Specialist (core) and the UK Tea Academy Tea Sommelier Award, Service and Innovation (verified-primary, carried).
  - Floor level (FS): each tea on the list, its category, how it tastes, which customer it suits and which course it goes with.
  - Product feedback: one level-2 note to HB on a tea (how it held across re-steeps in service, how it met the course, what customers said).
- What the person can do afterward: brew every listed tea to spec, explain its category and taste plainly, suggest a tea for a customer and a course, and give HB one reasoned note on a tea.
- How it is proven: a brewing practical on two teas with re-steeps; a recommendation role-play; recheck when the tea list changes. Test-out: WTA or UKTA award holders take only the spoken check and the house practical.
- Time and place: about 30 h over two to four months; floor level about 6 h. Remote reading paid; tastings on site.
- Waits on: the tea list (HB); verified Korean tea sources; the D27 answer from WTA and UKTA; `fact.fee.*`.
- Absorbs: BEV-037.

### BEV-118 Owning the tea program (parked until `people.tea_program_owner` exists)
- Area: beverage
- Positions and timing: parked. Opens only if Brandon names a tea owner (`people.tea_program_owner`, often the coffee owner); then ongoing. Level 3 of the tea track. Until then the tea list is held by HB under BEV-017 and BEV-037.
- What it teaches (outline, to the depth of BEV-117, ready if the role is created):
  - Sourcing criteria: harvest and season, freshness on arrival, the supplier's storage and transit, consistency between lots, sample-before-order (`vendor.tea.*`).
  - Storage on site: away from light, heat, moisture and strong smells; opened stock rotated and dated.
  - Calibration on a fixed protocol: the same leaf weight, water and time for every taster, a shared vocabulary (BEV-008), results logged (`tool.qc_log`).
  - List structure: range across the six categories and the herbal and grain infusions, caffeine options for the evening, a Korean tea where the founder sources one, and where each sits in the meal (`chef.*` for the pairing side). Cost inputs as `fact.*` only.
  - Supplier feedback: a lot that arrived stale or off-spec, said as fact with the tasting record.
  - Training and calibrating others.
  - Benchmark: UKTA Service and Innovation award level or the WTA advanced designations (verified-primary, carried).
- What the person can do afterward: keep the tea standard, propose list changes with reasons, and train makers.
- How it is proven: a list proposal presented with tasting; one observed calibration session. Test-out: UKTA Level 3 award or WTA advanced holders present directly.
- Time and place: 40 to 60 h over about six months; on site and remote, paid.
- Waits on: Brandon on whether tea has its own owner; suppliers (`vendor.tea.*`).
- Absorbs: BEV-106 of the other-tracks research.

### BEV-040 Non-alcoholic craft in depth
- Area: beverage
- Positions and timing: BA, BT; ongoing. LB and HB use it when writing non-alcoholic specs (BEV-030).
- What it teaches:
  - What alcohol does in a drink: body, warmth, carrying aroma, bitterness, length.
  - What replaces each: acids (citric, malic, lactic, tartaric) and their different tastes; tannin from tea and grape skins; bitterness; spice heat (ginger, chile, pepper); salt; sugar's body and other texture builders; carbonation; aromatic infusions and non-alcoholic distillates; fermentation (and its trace alcohol, `compliance.alcohol_trace`).
  - Korean ingredients if used (for example omija, yuja, sikhye, sujeonggwa; founder-sourced, unverified).
  - Building a non-alcoholic list with range (dry to sweet, light to rich) and a non-alcoholic pairing with the menu.
- What the person can do afterward: build and explain a non-alcoholic drink with the length and structure of a cocktail, and propose one for the list.
- How it is proven: a build and a spoken explanation to LB or HB; a proposed drink written to the BEV-030 format.
- Time and place: about 10 h on site, ongoing.
- Waits on: HB; `founder.glossary` for Korean ingredients; `compliance.alcohol_trace`.
- Absorbs: BEV-040.

---

## Part 7. Running and developing the bar

### BEV-019 Calibrating palates as a team, and tasting the bar on a shift
- Area: beverage
- Positions and timing: LB runs it (learning to run a session is part of the LB window); HB owns it; the bar team takes part, ongoing.
- What it teaches:
  - Triangle tests as practice, not statistics: three samples, two the same; find the odd one and say why.
  - Agreeing on what is in spec: tasting against the reference, the shared words (BEV-008), where the team disagrees and why.
  - A rhythm of tasting on the shift: every batch before doors, spot checks during service, every new batch, each taster's palate checked first (FLV-005); results logged (`tool.qc_log`).
  - Running a session: preparing samples blind, timing, recording, closing with one agreed change.
- What the person can do afterward: (LB) run a calibration session and a shift tasting rhythm; (team) agree in-spec calls with the reference.
- How it is proven: LB co-runs a session with HB, then runs one observed.
- Time and place: LB 3 h on site in the window; then standing on the cadence.
- Waits on: `workflow.bar.calibration_cadence`; `tool.qc_log`; HB.
- Absorbs: BEV-019, BEV-029; the bar side of FLV-006.

### BEV-119 Cellar, storage and stock condition
- Area: beverage
- Positions and timing: HB and LB, ongoing; and whoever receives wine and spirits (`people.receiving_roles`), the receiving part before they first receive.
- What it teaches:
  - Receiving bottles against the order (ADM-105, SYS-136 for the tool side): counting, matching vintage and producer to the order, and checking condition: seepage around the capsule, a raised or pushed cork, a sticky bottle, a low fill, a case that arrived hot.
  - What to do with a bottle that fails: set aside, recorded, reported to HB, returned through the supplier route (`workflow.receiving.returns`); never put into service to "see if it is fine".
  - Storage conditions (`bev.spec.cellar`): steady cool temperature, darkness, humidity, no vibration, bottles laid down where corked, away from strong smells; why swings in temperature hurt wine more than a steady slightly warm room.
  - Organizing and rotating: every bottle in its place on the map (`workflow.cellar_map`, D58), first in first out, the by-the-glass reserve kept apart, older vintages tracked.
  - Vintage changes and run-outs: checking the new vintage before it is poured, tasting it against the old, and telling the floor (BEV-102 and BEV-112 recheck) before a customer is served something the floor did not taste.
  - Spirits and other stock: open-bottle life of aromatized wines and liqueurs (`bev.spec.open_bottle_hold`), what goes in the cold.
  - Product feedback: one MNU-101 note on stock condition from a supplier or a lot (what arrived, in what state, what it cost the floor).
- What the person can do afterward: receive a delivery and catch a damaged bottle; keep the cellar to spec and in order; tell the floor about a vintage change before service.
- How it is proven: a receiving practical on a real delivery with HB; a walk of the cellar against the map and the conditions log; recheck on the cadence. Prove-first: an experienced sommelier or cellar hand takes the receiving practical and the walk cold.
- Time and place: about 3 h on site, ongoing.
- Waits on: `bev.spec.cellar`; `workflow.cellar_map` and the space (D58); `people.receiving_roles`; `workflow.receiving.returns`; ADM-105 and SYS-136 for the receiving tool steps.
- Absorbs: none (accepted from the proposed additions after the red team).

### BEV-018 Back-of-house beverage prep and its quality check
- Area: beverage
- Positions and timing: HB, LB; ongoing.
- What it teaches:
  - Batch production in the back: scaling recipes by weight, adding dilution as water by weight, labeling, hold times, storage (`bev.batch.*`).
  - The quality check before release: tasted against the reference, measured where the spec says (temperature, sugar reading, alcohol content `bev.spec.*`), logged.
  - Liquid nitrogen and pressurized holding only inside SAF-003 and the house procedure.
  - Shared space with the kitchen: who prepares what, when, on which equipment (`chef.*`).
- What the person can do afterward: produce and release a batch to spec with a record HB can audit.
- How it is proven: a practical batch with HB's sign-off; spot audits of the log.
- Time and place: 6 h on site.
- Waits on: SAF-003; `bev.batch.*`; `chef.*` for shared space; the space (D58).
- Absorbs: BEV-018.

### BEV-022 Blind-testing a method before it changes
- Area: beverage
- Positions and timing: BT, LB, HB; ongoing.
- What it teaches:
  - No method changes on belief: a blind test comes first.
  - Setting up a test: one question, one variable, blind samples, a triangle or a paired preference, enough tasters, a record.
  - Reading the result and deciding: change, keep, or test again; writing it into the spec (BEV-030).
  - Example questions: does a re-garnish at the counter change anything a customer notices; does a longer shake change the drink; does fresh citrus beat held citrus at the end of its hold time.
- What the person can do afterward: design and run a blind test and report a decision HB can act on.
- How it is proven: one test designed, run and presented to HB.
- Time and place: 4 h on site.
- Waits on: HB.
- Absorbs: BEV-022; FLV-004.

### BEV-030 Writing a spec someone else can execute
- Area: beverage
- Positions and timing: LB, HB; ongoing.
- What it teaches:
  - The spec format (`bev.spec_format`): name; glass; ice; method; ingredients by measure; dilution and temperature targets; garnish; allergens; the ranges for what may move (BEV-020); a reason for each element; the batch version and its hold time; prep it depends on; a photo reference.
  - The test of a spec: someone else builds it from the page alone, and HB tastes it against the original.
  - Versions: a change is dated, its reason stated, and the floor told (BEV-102 recheck).
  - From bench to proposal: development happens on paid time set aside, never during service (`workflow.bar.rd_time`); an idea goes from bench trials to a blind test (BEV-022), a written spec, cost through `fact.*`, the chef for any pairing, and HB's decision; the record keeps what was tried and why it was dropped.
- What the person can do afterward: write a spec that another bartender builds correctly on the first attempt, and take one idea from bench to a proposal HB can decide on.
- How it is proven: one spec written and built by another person, tasted by HB; one proposal presented to HB.
- Time and place: 4 h (1 remote, 3 on site); development then runs on scheduled paid time.
- Waits on: `bev.spec_format` (HB); the training system's home for specs (`tool.*`); `workflow.bar.rd_time`; the space (D58).
- Absorbs: BEV-030; BEV-031 (folded here: its only unique content was when development happens).

---

## Beverage readiness hours by position (this file's modules only)

These count only the modules in this file; the blocks and other areas are in the spine. Supervised services are counted in the spine at shift length (`workflow.shift_length.<position>`), not here. Where these differ from the current spine, the difference is listed under "Spine changes needed".

| Position and route | Beverage readiness hours | Modules |
|---|---|---|
| H | 1 | BEV-102 host depth |
| FR | 1.5 (2 if runners carry drinks) | BEV-102 runner depth; BEV-016 service-well part 0.5 only if `workflow.drink_running` |
| BW (from FR) | 5, plus the BEV-016 service-well part inside SVC-013 | BEV-002 floor part 2, BEV-102 +3 |
| BW (experienced external) | 9.5 | BEV-002 floor part 2, BEV-102 4.5, a cold BEV-110 check 2, BEV-016 service-well part 1 (with SVC-013). The green external BW route is proposed closed: everyone enters service as a runner. |
| FS (from BW) | 5 | BEV-042 2, BEV-102 +2, BEV-025 floor part 1 |
| FS (external) | about 22.5 | BEV-102 6.5, BEV-042 2, BEV-025 floor part 1, BEV-111 proof 4, BEV-112 integrated re-proof 6, BEV-113 role-play 2 (prove-first), BEV-015 live demonstration 1 |
| MD | 8.5 | BEV-102 6.5 (FS depth, prove-first), BEV-042 2; BEV-112 proposed as a hiring requirement |
| BB (green) | 24.5 | Block D beverage modules 18.5 (BEV-017, BEV-002, BEV-003, BEV-016, BEV-014, BEV-024, BEV-033 full), BEV-102 2, BEV-027 2, BEV-105 recognition 2. BEV-001 and FLV-002 move to BB ongoing. |
| BA (from BB, the default route) | 21.5, plus 4.5 if BEV-001 and FLV-002 are not yet held | Barista set 21.5 (BEV-004, BEV-103 full, BEV-104, BEV-006, BEV-025, FLV-005, BEV-102, BEV-026, BEV-020); BEV-120 2.5 if the BA owns the pull |
| BA (green external) | 43.5 | Block D beverage modules 20 (BEV-001 and FLV-002 prove-first where possible, BEV-033 house portion), barista set 21.5, BEV-105 recognition 2; BEV-120 2.5 if the BA owns the pull |
| BT (from BB) | 30.5 (25.5 if neither beer nor Korean drinks are listed) | Shared set 15 (BEV-004, BEV-103 short, BEV-104, BEV-006, BEV-025, FLV-005, BEV-020); bartender set 15.5 (BEV-102 +4, BEV-015 bar part 2, BEV-116 serving 3, BEV-028 short 2, BEV-023 2.5, BEV-021 2). Less 3.5 if BEV-004 drops (no milk on the bar). |
| BT (experienced external) | spine figure less about 9 | Prove-first on BEV-016 2, BEV-020 1.5, BEV-021 2, BEV-023 2.5, BEV-024 1; BEV-105 full part counts as readiness for this route only |
| LB | 3 | BEV-019 running a session |
| HB | 12 | BEV-017 2; familiarity walk on BEV-016, BEV-014, BEV-024 (4); BEV-102 at BT depth 6 (normally proven first) |
| Whoever pulls the batch espresso | 2.5 | BEV-120 (owner set by the chef and HB) |

Gate items held before a window opens (ongoing education, outside it, paid against `policy.ongoing_education_hours.<position>`). Time in seat is shown at an assumed 4 paid hours a week, to be replaced when Brandon sets the allowance:
- FR to BW: BEV-110 (10 h); about 3 weeks.
- BB to BT: BEV-105 full, BEV-012, BEV-005, BEV-008, BEV-001, FLV-002 (26.5 h); about 7 weeks.
- BW to FS, hard gates: BEV-111, BEV-015, BEV-112, BEV-113 (106 h); about 27 weeks. With the soft gates (BEV-035 part one about 20 h, BEV-037 floor level about 6 h, BEV-028 floor level), about 33 weeks. At 2 hours a week the hard gates alone take about a year, so the allowance decides whether a back waiter can reach front server.

---

## Spine changes needed

1. 5.4: add BEV-120 "Pulling and holding the batch espresso" (about 2.5 h, readiness for `people.espresso_puller`, owner set by the chef and HB). Add it to whichever window owns it (BA, or the kitchen position).
2. 5.4: add BEV-119 "Cellar, storage and stock condition" under HB and LB, ongoing (about 3 h), with a receiving part for `people.receiving_roles`.
3. 5.4: remove BEV-034 from the module list; carry "Does Sŏn run two bars?" as an open question. Remove BEV-031 (folded into BEV-030 as "From bench to proposal"). Mark BEV-118 parked until `people.tea_program_owner` exists. Mark BEV-004 conditional on `tool.bar.equipment`.
4. 5.4 titles: BEV-005 "Classic drinks and their families"; BEV-022 "Blind-testing a method before it changes".
5. 2.3 Barback: keep BEV-027 in readiness; move BEV-001 (2.5) and FLV-002 (2) to BB ongoing and add both to the BB to BT gate list; add the BEV-105 recognition part (2) to Block D for BB and BA. BB beverage hours become 24.5 (was 27).
6. 2.3 Bartender from BB: count BEV-102 at +4, not 6. 2.3 Barista: barista-first route is from BB by default; a green external BA takes BEV-001 and FLV-002 prove-first; add the 2 h recognition part. 2.3 external BT: prove-first on BEV-016, BEV-020, BEV-021, BEV-023, BEV-024 recovers about 9 h; BEV-105 full is readiness only for this route.
7. 2.3 HB: add BEV-102 at BT depth (6).
8. 2.2 MD: BEV-102 at FS depth 6.5 (prove-first), not 2; BEV-112 (wine level 3) a hiring requirement for the MD, pending Brandon's call on D55 for the manager pair. Section 4: replace "MD holds level 3" with that.
9. 2.2 BW: close the green external BW route; an experienced external BW takes a cold BEV-110 check (about 2 h).
10. 2.2 FS external: count BEV-111 proof at about 4 h, BEV-112 integrated re-proof about 6 h, BEV-113 as the role-play check only (about 2 h, prove-first), BEV-015 as a live demonstration (about 1 h).
11. 5.2 and SVC-013: BEV-016 service-well part goes to FR only if runners carry drinks (`workflow.drink_running`), adding 0.5 h to FR readiness if so.
12. Section 3 (time in seat) and a new policy: add `policy.ongoing_education_hours.<position>` and publish the gate time-in-seat estimates above (FR to BW, BB to BT, BW to FS). Add BEV-105, BEV-012 and BEV-005 to the BA ongoing row so the BA to BT route reaches its gate items.
13. Section 4 track tables: add an "Advocacy and feedback" column per level, using the customer element and the MNU-101 note now written into BEV-110, BEV-111, BEV-112 (list level), BEV-105 and BEV-035 part one (a back-bar bottle), BEV-103 and BEV-036 (coffee), BEV-104 and BEV-037 (tea), BEV-116 style part, BEV-028 and BEV-119.
14. BEV-112: record that it runs in dated sections (`bev.wine_list.sections`) with banked section checks and an unbanked integrated check, paced by `policy.ongoing_education_hours.bw`.
15. BEV-101: holds only if supervised services are counted at shift length (finding 1); otherwise it needs its own hours.
16. SAF-003 renumbering (CMP-112 or a house SAF part): BEV-017 and BEV-018 cite SAF-003 and will follow whatever ID the spine adopts.
17. Placement map: BEV-005 and BEV-022 new titles; BEV-031 "Folded into BEV-030"; BEV-034 "Dropped as a module: open question"; BEV-027 kept in BB readiness; BEV-001 and FLV-002 barback part to ongoing; BEV-118 parked; add BEV-119 and BEV-120 as new rows.

## Open for Brandon (beverage)

1. Is beer on the list (BEV-116), and are Korean drinks (BEV-028)? Each changes the bartender window by 2 to 3 h.
2. Do baristas serve alcohol (`workflow.bar.morning_alcohol`), and is the barista a separate hire, or does every barista start as a barback?
3. Does a coffee program owner exist, and a separate tea owner (BEV-117, BEV-118)?
4. Confirm the hard gates: BEV-110; BEV-111 with BEV-015; BEV-112; BEV-113; BEV-105, BEV-012, BEV-005, BEV-008, BEV-001, FLV-002; BEV-035 part one for LB.
5. Tasting on paid time, the minimum age to taste, and the non-drinking route (`policy.tasting_on_paid_time`, `compliance.alcohol_tasting`).
6. May the studio ask CMS, WSET, SCA providers, Barista Hustle, Cicerone, WTA and UKTA about delivery and tracking inside Trainual (D27); does Sŏn fund outside exams?
7. Interviews: the program's reasoning; the coffee method; what "Sommelier 1 level" means in practice; how Sŏn recommends; the water-pitcher drill story.
8. Does Sŏn run two bars (the front bar plus the walk-up window or a back bar)? If so, a module on what is identical at both and how a maker moves between them gets specified then.
9. How many paid hours a week go to ongoing education per position (`policy.ongoing_education_hours`)? It sets how long a back waiter takes to reach front server.
10. Who pulls the batch espresso (`people.espresso_puller`), and is there milk-texturing equipment on the front bar (BEV-004)?
11. Is wine level 3 (BEV-112) a hiring requirement for the Maître d'?
12. Do food runners carry drinks from the service well?
