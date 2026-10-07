# Modules: culinary, leadership and teaching, administration (working draft, 2026-10-01)

Writer 4's areas of the spine (`research/position-paths/spine.md`, sections 5.5, 5.6 and 5.7). Nothing here is decided until Brandon signs the spine. Position abbreviations, groups (All, CF, Floor, Bar, K) and the R/O marks follow the spine. Hours are design estimates inside 40-hour paid weeks with no overtime, and they match the spine's arithmetic unless a note says otherwise.

How to read it:
- **Culinary is a draft for the executive chef** (D30). None of it is a Sŏn kitchen standard until the chef sets one. Kitchen titles are `people.*` bindings (naming conflict INT C17: the white paper's Steward, Station Lead, Chef on the line and Chef on prep against the intake's porter, commis, chef de partie, chef de tournant). Station specifics, recipes, plating, menu execution, the allergen matrix and every kitchen standard are `chef.*` bindings. Where the chef must supply the content, the module still states its structure and the known content, and names exactly what is needed under "Waits on".
- **Leaders' modules** never give a lead authority over discipline or pay (D5). Whether rating a practical counts as managing for an hourly employee is open with the HR seats; every module where a lead rates carries that dependency.
- **Every figure** (labor targets, costs, pars, pay, fees) is a `fact.*` binding, pulled from the tool at bind time, or unbound until a source is chosen (Airtable retired). Every tool step is a `tool.*` binding; every tool name is a candidate (D60, lead-only).
- **Sources.** Box canon is cited by label as the 2026-10-01 position drafts read it: the white paper (WP, file `2466517057642`) and the Brand Guidelines (canon line pending phase 1 session B) (BG, file `2281626080747`). Re-read each cited page in Box before a lesson is drafted. Kitchen evidence is carried from `research/phase2-working/12-back-of-house.md` with that file's marks. No ClickUp document was read. The Sŏn Operating System is out of scope. Brandon's lineage houses were not researched; his experience enters only through his interviews (D45).
- **Plain terms and program rules** (revised 2026-10-01 after the red team). The angel shift is Brandon's name for the gate shift where a trainer, the mentor, oversees the person the whole night (term pending his confirmation, `founder.term.angel_shift`). After sign-off come unsupervised shifts: support is on hand but nobody is watching (D9, D10). Booked check slots (`workflow.check_slots`) are the leader's protected times in which practicals, spoken checks and unblock conversations are booked (D13). Supervised services count at shift length (`workflow.shift_length.<position>`, about 6 h as the design assumption), with pre-shift, opening, closing and side work inside them; at least one is a full night (`workflow.full_night`), and a person is released only for the dayparts they were supervised in (D10). Prove-first (ORI-015): every non-safety module lets an experienced hire attempt the proof cold after reading the material; a failed cold attempt routes the person into the instruction and is not a recorded miss (D11). Safety elements never test out and pass on every attempt.
- **Interview topics** for Brandon are named as they appear in the back-of-house guide (section 8 of `12-back-of-house.md`): best night, broken night, the pass, the dish station, tasting, teaching a new cook, a correction that worked and one that did not, the seam, an unwritten standard, what you will not carry. Chef questions are numbered as in that file.

---

## 1. Culinary (draft for the executive chef)

### KIT-102 Starting in Sŏn's kitchen
- Area: culinary
- Positions and timing: K, every kitchen position. Readiness, day one, before any station or dish-area work. Part of Block K.
- What it teaches:
  - Who is who: the kitchen positions as the chef names them (`people.kitchen_titles`), who owns which station, who runs the pass (`people.expo`), who to ask for what, and who decides. The executive chef owns execution during service (WP p.10).
  - The non-negotiables in a kitchen, cited from BG 01 "Company non-negotiables": intensity and precision are kept; degradation of people is not. What that looks like on a bad night, in the chef's words.
  - Culinary identity belongs to the brand, and the chef executes inside it (BG 07, cited). For a cook: the spec is the floor, never a suggestion, and a change goes through the chef.
  - The house language rule holds in the kitchen: customer, never the other word (BG 01 "Language constant").
  - Ask before acting: an unknown ingredient, a spec in doubt, a safety question, a call you did not hear. Asking is a signed-off behavior. Three named situations and who to ask in each (`chef.ask_routes`).
  - How the kitchen learns: movements drilled apart from decisions (ORI-016); tasting with the chef; spoken checks; paired shifts; sign-off over a window of real shifts (D10); correction in private when it concerns the person (D22).
  - The kitchen's working languages, and how training reaches a multilingual team (`founder.kitchen_languages`).
  - Paths out of each kitchen seat: porter to commis, to food runner, or to a line rotation; commis to a first station; production (prep) as a full career a person can stay in (WP p.11). Asking for a direction (D13).
- What the person can do afterward: name their trainer, their station owner and the chef; say who they ask in three named situations; state the non-negotiables and one thing each looks like on a bad night.
- How it is proven: spoken check with the trainer on day one; recheck in week two. Prove-first: an experienced cook reads the material and takes the spoken check cold, skipping the remote session if passed; the on-site half hour with the trainer always runs, because it is where the person meets the people named.
- Time and place: 2 h (1.5 remote and paid, 0.5 on site with the trainer).
- Waits on: the chef (structure, titles, `chef.ask_routes`, what the chef will not tolerate); Brandon interview topics "what you will not carry" and "a correction that worked, and one that did not"; `founder.kitchen_languages`; INT C17 (titles).
- Absorbs: KIT-025; the kitchen side of CUL-025; the line-level part of KIT-044.

### KIT-101 What the kitchen must know about the floor
- Area: culinary
- Positions and timing: K. Readiness in Block K (cooks 2 h, porter 1 h). The floor shift that deepens it is KIT-061 (ongoing).
- What it teaches:
  - The service model: the floor reads the table, and the next approach follows the table, not a clock (BG 15 "Step-back architecture · three phases", cited). What that means for the line: a course is held because the table is not ready, not because the floor is slow.
  - The customer personas as calibration, never constraint (BG 05): David's kitchen visit is pre-authorized in the reservation system before service, never improvised; Mia does not want her food explained.
  - The floor's recovery range and who holds it (D25; `fact.recovery_range.*`, `people.*`), so a refire from the kitchen meets the make-good the floor offers.
  - The door upstream of the line: a wave of seatings becomes a wave of tickets (SVC-011). The pacing rules are `workflow.pacing.*`.
  - What tonight's book tells the kitchen before service: allergies and dietary needs, occasions, large parties, returning customers' food notes, kitchen visits (the kitchen versions of SYS-111 and SYS-112; read through the pre-service view or the POS ticket, `chef.preshift_use`, `tool.pos.ticket_notes`).
  - The threshold: nothing from the kitchen is heard in the room (BG 13, beat 8).
  - What the floor needs from the kitchen: honest times, early 86s, clear allergy marks (`chef.allergen_marking`), and a plate story the floor can tell (MNU-001).
  - Porter version (1 h): the threshold, the book's large parties and the surge times, and why the dish area's pace follows the door.
- What the person can do afterward: explain why a table's course was held; say what the floor does with a refire; name the items in tonight's book that change the line's preparation.
- How it is proven: spoken check with KS or the MD on a sample night's book. Prove-first: an experienced cook who passes the spoken check cold skips the remote block.
- Time and place: cooks 2 h (1.5 remote and paid, 0.5 on site for the check); porter 1 h remote and paid.
- Waits on: chef questions 14 and 17; `chef.preshift_use`; `fact.recovery_range.*`; `workflow.pacing.*`; `tool.reservations.preshift_view`, `tool.pos.ticket_notes`; Brandon interview topic "the seam".
- Absorbs: section 7.2 of `12-back-of-house.md`; the knowledge part of KIT-061.

### KIT-002 The pass: call, callback, handoff
- Area: culinary
- Positions and timing: cooks and whoever works the pass, readiness (CDP window 2 h); FR floor side, readiness (2 h; BW and FS inherit it); LFR expo part, readiness for the lead seat (1 h). Drilled on site before working a station or running food solo.
- What it teaches:
  - The closed loop: the caller names the receiver and the item; the receiver repeats it; the caller confirms. Nothing is assumed heard (closed-loop communication, AHRQ TeamSTEPPS, lead-only; Gomez et al.'s "running?" and "yes, two minutes", verified-primary, both carried from `12-back-of-house.md`).
  - The house call list: fire, pick up, time remaining, refire, 86, allergy-modified plate, on the fly (`workflow.pass.call_lexicon`). What each call obliges the receiver to do.
  - Threshold volume: calls are built so kitchen sound does not cross into the room (BG 13, beat 8).
  - Cook side: answering a fire and a time call; handing a plate to the pass; calling a plate that will be late before it is late; never sending a plate the pass has not accepted.
  - Floor side: what the runner confirms before lifting (table, seat position, any modification marked, `workflow.pass.handoff`, `chef.allergen_marking`); never lifting an unconfirmed allergy plate; what to say when a plate is wrong, late or missing; where the floor stands and does not stand at the pass.
  - Expo part (LFR): directing runners under the expo's call, never beside it; calling a table's plates together; telling the expo when no runner is free.
- What the person can do afterward: call and answer every call in a live drill at service tempo with no dropped loop; hand off and receive plates with the confirmation every time.
- How it is proven: a drill run on both sides of the pass together, then observed on paired and supervised shifts; recheck after the first full week. Test-out: experienced cooks and runners run the drill once at tempo, signed off if no loop drops. The allergy-modified handoff never tests out and passes on every attempt (D11).
- Time and place: 2 h of drills on site in two or three short sessions, paid (LFR expo part 1 h); observation inside paired shifts.
- Waits on: `workflow.pass.call_lexicon`, `workflow.pass.handoff`, `tool.kds.*`; the chef's call on who expos (`people.expo`); the space (D58); Brandon interview topic "the pass".
- Absorbs: KIT-002; SVC-014 and SVC-022 (with SVC-013); part of KIT-016. This is the single source for KIT-002, floor side included; the service file points here and counts no KIT-002 hours.

### KIT-010 The porter's craft: keeping the kitchen continuous
- Area: culinary
- Positions and timing: P, readiness. Cooks by the chef's call (`chef.porter_rotation`).
- What it teaches:
  - What continuity means: wares, equipment, space and the flow of materials ready so no station waits. The role "owns the continuity of the kitchen environment... It is not a support role" (WP p.11, cited).
  - The flow movements, drilled one at a time and then joined: scrape, sort, rack, load, run, unload, return. Each at slow, fast and changing tempo (ORI-016 method).
  - Return points and order for each station's wares (`chef.ware_returns`, `chef.kitchen_layout`).
  - The machine and the sinks: wash, rinse, sanitize, and why each step exists; the house's sanitizing check (`tool.dish_machine.*`, `workflow.porter.sanitize_check`). The chemical rules are CMP-111.
  - Priority when calls collide. Draft order for the chef to set: service needs first, then backlog, then deep cleaning (`chef.porter_priority`).
  - Reading the kitchen: which station is about to run short of pans, plates or small wares, and moving before it asks.
  - Fine ware and glass: handling, chips, and when a piece is retired (`chef.ware_retirement`).
  - When to stop and ask: an unknown chemical, a machine fault, an unlabeled container, a food-safety doubt.
  - The night close of the dish area: placeholder (D58, `workflow.kitchen.close`).
- What the person can do afterward: keep wares flowing through a full night so no station waits, and say what they cleared first at three named moments and why.
- How it is proven: flow drills signed off on site; a practical on a paired shift; unsupervised shifts after sign-off, at least one a full night (D10); recheck after a month. Test-out: an experienced porter runs the flow and machine practical on the first paired shift. The sanitizing check and the chemical steps never test out.
- Time and place: 6 h of drills and walk-throughs on site, paid; then inside paired shifts.
- Waits on: the space (D58); `chef.kitchen_layout`, `chef.ware_returns`, `chef.porter_priority`, `chef.ware_retirement`; `tool.dish_machine.*`; chef questions 6 and 7; Brandon interview topic "the dish station".
- Absorbs: KIT-010.

### KIT-012 Knife and body (drills)
- Area: culinary
- Positions and timing: C, CDP, CT, readiness, drilled from week one. Floor people on a kitchen rotation take the safety part (KIT-060).
- What it teaches:
  - Grip, stance, the guiding hand, board setup and stability.
  - The house cut list, one cut at a time, slow to fast, in short spaced sessions (`chef.cut_list`).
  - Knife care: honing, the sharpening rule, storage, carrying, washing (`chef.knife_policy`).
  - The body: standing, reaching, lifting and turning with heat and knives; fatigue, and when to reset.
  - Self-review: a mirror or a short clip against the reference; practice the weak cuts, not the comfortable ones (ORI-016).
- What the person can do afterward: produce each listed cut to the reference, at the house tempo, safely, three times running.
- The knife-safety element, its own line on every attempt: grip and guard hand (fingertips tucked, knuckle guiding the blade); a board that cannot slide (damp cloth or mat under it); knife carried point down at the side, called on the move (KIT-016); passed by setting it down, never hand to hand; a falling knife is let fall.
- How it is proven: a practical with cuts the assessor chooses on the day (the UK chef de partie standard's method, verified-primary, carried); recheck in week three. Test-out: the same practical on day one, cuts only. The knife-safety element never tests out: it is observed and must pass on every attempt, test-out included, and a miss on it is a not-yet whatever the cuts score (D11).
- Time and place: 10 h on site across two weeks in 30 to 45 minute blocks, paid. Never take-home (D41).
- Waits on: `chef.cut_list`, `chef.knife_policy`, `chef.drill_product` (what is cut in drills, and where it goes afterward); chef question 11.
- Absorbs: KIT-012; the kitchen form of ORI-016.

### KIT-013 Mise en place, the line check and clean as you go
- Area: culinary
- Positions and timing: C, CDP, readiness. P takes clean as you go inside KIT-010.
- What it teaches:
  - Mise en place as readiness: planning first, arranging the space, first moves, finishing actions, call and callback, inspect and correct (Charnas, *Work Clean*, verified-secondary, carried).
  - The station map: what goes where and why (reach, order of use, heat, cross-contact) (`chef.station.<name>.mise`).
  - The spoken line check: short, said aloud, owned by the station, done every service (`chef.line_check`). A checklist works when the team owns it and says it; as paperwork it may not (Haynes 2009, verified-secondary; Urbach 2014, lead-only, carried).
  - Clean as you go between tasks; the organized withdrawal; the dish area is never storage (ACF, verified-primary, carried).
  - The kitchen's own food-safety controls beyond the code (moved here from CMP-110, which now holds only the code-derived items): the house's line rules the chef sets, such as tasting-spoon practice, towel and cloth rules, what may sit at a station between uses, and the station's checks between services (`chef.food_safety_rules`). These are house standards, taught as the chef's, never presented as law (D57).
- What the person can do afterward: set a station to its map, say its line check aloud without missing an item, keep it clean through service, and work every house food-safety rule on the station.
- How it is proven: a timed setup and the spoken line check; observed on paired shifts; recheck. Test-out: an experienced cook is observed on the first paired shift and signed off if met. The house food-safety rules are observed in full on every attempt.
- Time and place: 4.5 h on site (walk-through, timed setups, the house rules), paid; then inside paired shifts.
- Waits on: `chef.station.<name>.mise`, `chef.line_check`, `chef.food_safety_rules`; chef question 9.
- Absorbs: KIT-011, KIT-013, KIT-014.

### KIT-015 Receiving, storing, labeling, rotating
- Area: culinary
- Positions and timing: P (3 h) and C (2 h), readiness. KO at full depth through ADM-105's kitchen part and KIT-041. The record in the tool is SYS-136.
- What it teaches:
  - Checking a delivery against the order: count, condition, temperature, packaging, dates; what is refused, and who decides (`workflow.receiving`).
  - Storage order and why: raw below ready-to-eat, allergen segregation, first in first out, the storage map (`chef.storage_map`).
  - Labels: what goes on one and why (`chef.label_standard`).
  - Logging temperatures and receipts (`tool.food_safety.logging`, `tool.inventory.receiving`).
  - A short or wrong delivery: who handles the credit (`workflow.receiving.credits`).
  - Porter extra hour: lifting and moving deliveries, walk-in order, and keeping the receiving door clear.
- What the person can do afterward: receive, check, store and label a mixed delivery correctly and log it.
- How it is proven: a practical on a real delivery; recheck. Test-out: the practical on the first delivery. The food-safety elements are observed in full every time.
- Time and place: P 3 h, C 2 h, on site and paid, plus real deliveries inside paired shifts.
- Waits on: `workflow.receiving`, `workflow.receiving.credits`, `chef.storage_map`, `chef.label_standard`, `tool.inventory.*`, `tool.food_safety.logging`; suppliers and delivery windows; the space (D58).
- Absorbs: KIT-015 (the floor and bar half went to ADM-105; the tool half to SYS-136).

### KIT-016 Moving and calling in the kitchen
- Area: culinary
- Positions and timing: K, readiness, week one (Block K). Anyone who enters the kitchen (runners, bar staff carrying batch work) takes the floor's version inside SAF-007.
- What it teaches:
  - The kitchen's movement calls and their answers, built on SAF-007 (`workflow.kitchen.call_lexicon`; the shared words are `chef.call_language`).
  - Carrying hot, sharp and heavy loads through a working line.
  - Door, corner and pass etiquette; where floor staff may and may not stand.
  - Routes and pinch points, as placeholders until the space exists (D58).
- What the person can do afterward: move through a full kitchen at service tempo, using and answering every call.
- How it is proven: a drill, then observed on paired shifts; signed off once. No test-out: house-specific, and a safety item.
- Time and place: 2 h on site, paid.
- Waits on: the space (D58); `workflow.kitchen.call_lexicon`, `chef.call_language`.
- Absorbs: KIT-016; the kitchen side of SAF-007.

### KIT-020 Prep production: list, par, sequence
- Area: culinary
- Positions and timing: C, readiness. CDP and CT for their station's prep. KO at full depth (KIT-041).
- What it teaches:
  - The prep list and pars: where they come from (the forecast, the book, events) and how they change (`chef.prep_list`, `fact.par.*`). Working the generated list in the tool is SYS-141.
  - Sequencing: longest lead time first; service-critical items before the rest; batch against à la minute; holding times (`chef.hold_times`).
  - Reading the day's book for prep: large parties, allergies, occasions (`tool.reservations.*`). Cover counts are a `fact.*` value, never estimated.
  - Calling a shortfall early, before it becomes an 86, and to whom.
- What the person can do afterward: plan and run a prep day so service starts fully set, and explain the order chosen.
- How it is proven: a sequencing scenario on a sample day; a practical on a real prep shift; recheck. Test-out: the scenario plus one observed prep shift.
- Time and place: 3 h (1.5 remote and paid for the scenarios, 1.5 on site), then inside paired prep shifts.
- Waits on: `chef.prep_list`, `fact.par.*`, `chef.hold_times`, `tool.kitchen.prep_planning`.
- Absorbs: KIT-020 (the tool side went to SYS-141).

### KIT-021 Recipes as specs and as reasons
- Area: culinary
- Positions and timing: C and CDP, readiness for the recipes they are assigned; ongoing as the menu changes.
- What it teaches:
  - Each assigned recipe as a spec: quantities, method, the order of steps, the result (`chef.recipe.*`). A technical card "is not a recipe" but a precise framework (Gomez et al., verified-primary, carried).
  - Each recipe's reasons: why this heat, this rest, this order, this salt timing.
  - What drifts in the ingredient (season, supplier, size) and the known adjustment; what never changes without the chef.
  - Reading the house recipe format (`tool.recipe_management`, SYS-141).
- What the person can do afterward: make each assigned recipe to spec and say why each step exists; name the adjustment for a common drift.
- How it is proven: a spoken check on recipes the chef chooses; a practical; recheck at the next menu change. Test-out: the spoken check after self-study.
- Time and place: 3 h (2 remote and paid for the first set, 1 on site), then practice inside prep shifts.
- Waits on: `chef.recipe.*` (the chef supplies every recipe and its reasons); BG 17 session 1B (culinary philosophy, held).
- Absorbs: KIT-021.

### KIT-022 Tasting and seasoning to the house
- Area: culinary
- Positions and timing: C and CDP, readiness for the first calibration; ongoing calibration on a standing rhythm.
- What it teaches:
  - When to taste: before, during and after.
  - The levers: salt, acid, fat, heat, sweetness, bitterness, texture.
  - Tasting against the house reference, not personal preference; "the duck broth tastes like duck" (ACF, verified-primary, carried).
  - Stating the adjustment aloud before applying it, then tasting against the reference.
  - Near-miss pairs: a component on spec beside one just off.
- What the person can do afterward: taste a component, name what it needs, adjust, and land within the chef's reference.
- How it is proven: calibration tastings with the chef, many short trials; a spoken check; recheck across shifts. Prove-first: an experienced cook takes the first trials cold against the house reference; landing within it on the set number of trials signs the first calibration and skips the rest of the session. (The calibration method is inference, unverified as a kitchen method.)
- Time and place: 2 h on site in short sessions, paid; then a standing rhythm.
- Waits on: `chef.taste_reference.*`; chef question 8; Brandon interview topic "tasting".
- Absorbs: KIT-022.

### KIT-023.x Station modules, one per station
- Area: culinary
- Positions and timing: CDP for the first station owned (readiness); CT for each station (the first in readiness, the rest ongoing). KO, KS and CDC walk and cook every station under the executive chef in onboarding (16 h, the walk part).
- What it teaches (per station, every item `chef.station.<name>.*`):
  - The station's items, components, timings and holds.
  - Plates and garnish to the plate standard (`chef.plate_standard.*`), and the tableware each goes on (`chef.tableware.*`).
  - The station's mise map and line check (KIT-013).
  - The station's repeated movements, drilled apart from service.
  - Its failure points and the recovery for each.
  - Its allergen controls (SAF-013 applied to the station).
  - Its cleaning and close (D58 placeholder).
- What the person can do afterward: run the station solo to the standard on a named non-peak service; KIT-030 then carries them to peak nights.
- What "solo" means for a cook (D55): released on the station for a named non-peak service (`workflow.kitchen.nonpeak_service`, set by the chef), working without a paired cook, with the station owner or the pass able to see the station. Peak nights follow under KIT-030, after the window. Without this line, a cook's readiness window has no defined end.
- How it is proven: drills for the repeated movements; a small-menu practical; paired service; release for the named non-peak service; then unsupervised shifts after sign-off and KIT-030 for peak nights (D10). Test-out: an experienced cook passes the small-menu practical cold; the paired service and release still run.
- Time and place: 16 h per station (drills and the practical), on site and paid; most of the remaining learning sits inside paired service. Flagged to the chef as optimistic for a kitchen held to this standard: the 16 h per station and the paired-service unit (counted at 4 h in the spine; at shift length it is about 6 h) are the chef's to reset.
- Waits on: the chef: the station list and every station's content; station hours and paired-shift length; `workflow.kitchen.nonpeak_service`; the space (D58); chef question 4.
- Absorbs: KIT-023.x.

### KIT-024 Cooking to the call
- Area: culinary
- Positions and timing: CDP, readiness; CT inherits it; the pass uses it.
- What it teaches:
  - How the call sets the timing; working back from the pass time.
  - Holding windows and what degrades first (`chef.timing.*`, `chef.hold_times`).
  - Correcting toward the other stations so a table's plates land together (ensemble timing, Wing et al. 2014, verified-primary, carried).
  - Telling the pass early, in one line, when a component will be late.
  - Reading the display for course, seat and modification (SYS-132).
- What the person can do afterward: deliver their components to the pass with the rest of the table's, across a full ticket rail.
- How it is proven: timing drills with live calls; observed on paired service. Test-out: observed on the first paired service.
- Time and place: 4 h of drills on site, paid; then inside service.
- Waits on: `chef.timing.*`, `chef.hold_times`, `tool.kds.*`.
- Absorbs: KIT-024.

### KIT-031 Entering a station without disrupting it
- Area: culinary
- Positions and timing: CT, readiness. CDP and anyone giving breaks, ongoing.
- What it teaches:
  - The entry sequence: read the board and the rail; ask the owner; repeat back the named task; take it; hand back with its status.
  - Where to stand, and what never to move on another cook's station.
  - Break and relief cover (`workflow.kitchen.breaks`).
  - The handover model: a pit-crew style handover (Catchpole et al., lead-only, carried).
- What the person can do afterward: step into a running station mid-service and take a task without slowing it.
- How it is proven: drilled entries, then observed live relief on each station. Test-out: observed relief on the first shift.
- Time and place: 2 h of drills on site, paid; observation inside service.
- Waits on: chef question 4; `workflow.kitchen.breaks`.
- Absorbs: KIT-031.

### KIT-103 Daypart transitions in one kitchen
- Area: culinary
- Positions and timing: CDP and CT, readiness when scheduled across two running dayparts. D24, stated once as in every file: training covers every daypart's register from the start; which dayparts actually run at opening, and when, is `workflow.daypart_schedule`; content for a daypart not yet running is built and parked. Until two dayparts run, this module is parked.
- What it teaches:
  - What changes on the line between dayparts: menu, stations, equipment, mise, staffing.
  - The changeover sequence and its owner (`workflow.daypart_transition.kitchen`).
  - Why it is hard: running distinct dayparts out of one kitchen "requires absorbing an enormous amount of coordination" (WP pp.33 to 34, cited).
  - Dayparts are named by plain descriptors only; internal daypart names never appear.
- What the person can do afterward: run their part of a changeover on time and to the standard.
- How it is proven: a practical on a real changeover. Prove-first: an experienced cook skips the walk-through and is observed on the first real changeover; the practical is the same.
- Time and place: 1 h on site (walk-through), paid; the practical runs inside paired shifts.
- Waits on: `workflow.daypart_schedule` (D24); `workflow.daypart_transition.kitchen`; chef question 28.
- Absorbs: none (new).

### KIT-104 Opening and closing the kitchen (placeholder)
- Area: culinary
- Positions and timing: K, readiness, inside paired shifts.
- What it teaches (the durable part only; every sequence is bound, D58):
  - Why each opening and closing task exists: food safety, the next shift's start, equipment life, the morning's first service.
  - What done looks like for each area, and who signs it.
  - The temperature checks at open and close (SYS-139).
  - What is never left overnight.
  - The handoff note to the next shift.
- What the person can do afterward: open or close their area to the house standard and write a handoff the next shift can act on.
- How it is proven: a practical on a real open or close.
- Time and place: inside paired shifts, paid.
- Waits on: the space (D58); `workflow.kitchen.open`, `workflow.kitchen.close`; the chef.
- Absorbs: none (new).

### SAF-013 Allergens and cross-contact in production
- Area: culinary (house safety, chef-led; not certificate content)
- Positions and timing: cooks and the pass (3 h); porter (1 h). Readiness, Block K.
- What it teaches:
  - The whole chain: the reservation note and the order (SAF-001, SYS-110), the ticket (SYS-132), production, the pass, the delivery to the seat (SAF-004). Where each link can break.
  - The allergen matrix and where it lives (`chef.allergen_matrix`).
  - Cross-contact controls in storage, prep, cooking and plating: separate tools, boards, oil, surfaces and order of work (`chef.cross_contact_controls`).
  - Marking a modified plate (`chef.allergen_marking`) and handing it off with confirmation (KIT-002).
  - When to refuse a modification, and how to tell the floor so the customer hears no and an alternative, never a promise.
  - Any doubt at any link stops the plate.
  - Porter version: allergen segregation in storage and wares, and what to do with a ware marked for an allergy plate.
- What the person can do afterward: produce an allergy-modified plate through every control and hand it off with confirmation.
- How it is proven: a decision-point scenario and a practical; observed every time a modified plate occurs during readiness. No test-out: safety. Passes on every attempt.
- Time and place: cooks 3 h (2 remote and paid, 1 on site); porter 1 h (0.5 remote, 0.5 on site).
- Waits on: `chef.allergen_matrix`, `chef.cross_contact_controls`, `chef.allergen_marking`, `workflow.allergy_entry`; chef question 13.
- Absorbs: SAF-013 (the everyone part sits in SAF-001).

### KIT-030 Owning a station through a full night
- Area: culinary
- Positions and timing: CDP, ongoing: after release on a named non-peak service (KIT-023.x), this carries the cook to peak nights. Inside the window for an experienced cook only where it allows.
- What it teaches:
  - Everything above joined on real, full nights.
  - Process (organization, cleanliness, waste, timing) and product (taste, doneness, presentation) rated apart, as ACF and the Bocuse d'Or do (carried).
  - What a full night is at Sŏn (`workflow.full_night_definition`).
- What the person can do afterward: hold a station on a full night with nobody watching.
- How it is proven: unsupervised shifts after sign-off across several full nights, closed when another night would not change the call (D10); periodic rechecks. No test-out: the nights themselves are the evidence of release, not instruction a person could skip.
- Time and place: service shifts, paid.
- Waits on: `workflow.full_night_definition`; chef question 12.
- Absorbs: KIT-030.

### KIT-033 Yield and total utilization
- Area: culinary
- Positions and timing: C and CDP, ongoing. KO at full depth.
- What it teaches:
  - Yield and what moves it: cut, trim, cooking loss, portioning.
  - A full-use plan for each product: where trim goes (`chef.yield_reference`).
  - Waste categories and logging every discard (SYS-140).
  - Why waste data is read, not guessed. Costs are `fact.*` figures (unbound until a source is chosen (Airtable retired)), never estimated.
- What the person can do afterward: plan a product's full use and log its waste correctly.
- How it is proven: a practical breakdown of one product; a spoken check. Test-out: the spoken check plus one observed breakdown.
- Time and place: 4 h on site, paid.
- Waits on: `chef.yield_reference`, `chef.waste_categories`, `tool.waste_tracking`, `fact.*`.
- Absorbs: KIT-033.

### KIT-034 Recovery from the kitchen side
- Area: culinary
- Positions and timing: CDP, ongoing (calling a refire is already inside KIT-002 at readiness).
- What it teaches:
  - Refire and remake rules (`chef.refire_rules`): when a plate is fixed, remade or refused.
  - Where a refire goes on a full rail.
  - Telling the floor the true time, once, in one line.
  - Matching the floor's make-good (D25, SVC-002).
  - The private, process-focused review afterward: "the first question is not who failed" (WP p.17, cited; D22).
- What the person can do afterward: recover a wrong or failed plate fast and honestly, keeping the floor informed.
- How it is proven: scenarios; observed on service; recheck. Test-out: the scenario check.
- Time and place: 2 h (1 remote and paid for scenarios, 1 on site).
- Waits on: `chef.refire_rules`, `fact.recovery_range.*`.
- Absorbs: KIT-034.

### KIT-040 Running the pass
- Status: identified, chef to define. The content below is the known frame; the pass standard itself is the chef's to write, and the module carries no hours until then.
- Area: culinary
- Positions and timing: KS and CDC, ongoing; KO as cover; CT by the chef's unlock. Who expos is a chef call.
- What it teaches:
  - The pass as the place a plate is accepted or stopped (Gomez et al., verified-primary, carried).
  - What is checked on each plate (`chef.plate_standard.*`), the allergy mark first.
  - Reading the rail and the room's pace together; pacing calls to stations.
  - Talking to the floor at threshold volume; working with the lead food runner (SVC-066, SVC-075).
  - Stopping a plate: what is said, to whom, and how fast.
- What the person can do afterward: run the pass through a full night with every plate to the standard and the room kept in time.
- How it is proven: observed runs of the pass with the executive chef; a conversation on chosen moments. Test-out: the chef's call once the module is defined.
- Time and place: open; service shifts, paid.
- Waits on: the chef's call on who expos (`people.expo`); `chef.plate_standard.*`; Brandon interview topic "the pass".
- Absorbs: KIT-040.

### KIT-042 Developing a dish inside the brand
- Status: identified, chef to define. R&D method, time and place are the chef's (chef question 26); no hours until then.
- Area: culinary
- Positions and timing: KS and EC, ongoing; CDP by election.
- What it teaches:
  - Exploration kept apart from service in time and place.
  - Keeping failed tests and their notes.
  - Writing each dish's why.
  - Mahk, "specificity as the mechanism of memory" (BG 02, cited); the brand frameworks a dish answers to (BG 07; the BG 17 held items).
  - How a new dish reaches the floor: the tasting, the dish card, MNU-002.
- What the person can do afterward: take a dish from idea to a codified, tested spec the executive chef and Brandon can approve.
- How it is proven: a conversation with the executive chef and Brandon on a developed dish. Test-out: the chef's call once the module is defined.
- Time and place: open; scheduled development time on site, paid.
- Waits on: `chef.culinary_philosophy`; the BG 17 held sessions; chef question 26 (R&D time and place).
- Absorbs: KIT-042.

### KIT-043 Codifying the kitchen
- Status: identified, chef to define. The library mechanics (capturing a night's call, writing a note another person can apply, where it lives, who approves) moved to LEA-037's kitchen part. What stays here is the chef's codification standard: the house recipe-with-reasons format and what the chef requires recorded after a menu change. No hours until the chef writes it.
- Area: culinary
- Positions and timing: KO, KS, CDC and EC, ongoing; CDP contributes.
- What it teaches:
  - Writing recipes with reasons, not only quantities, in the chef's format (`chef.recipe_format`).
  - What the chef requires recorded after a menu change or a failed test (`chef.codification_rules`).
  - Why: knowledge held only in people leaves with them; "a restaurant built around a specific chef is a dependency, not a business" (WP p.37, cited).
- What the person can do afterward: write a recipe with its reasons that another cook can make to spec.
- How it is proven: a conversation on submitted entries. No test-out: a standing practice.
- Time and place: open; short paid blocks after service.
- Waits on: `chef.recipe_format`, `chef.codification_rules`; `tool.recipe_management`.
- Absorbs: KIT-043 (its library mechanics went to LEA-037).

### KIT-045 The kitchen's part in pre-shift
- Area: culinary
- Positions and timing: KS and CDC, ongoing and standing; a CDP may lead the station's part.
- What it teaches:
  - What the kitchen brings to the shared pre-shift, in order and briefly: 86s, allergen changes first, specials, the book's kitchen flags, kitchen visits (`workflow.preshift.kitchen`).
  - Teaching a new dish to the floor with a tasting (MNU-001, MNU-002).
  - The floor's palate as a source: hearing what the floor tastes and what customers said (MNU-101).
- What the person can do afterward: deliver the kitchen's part of pre-shift clearly inside the time set, with a tasting when a dish changes.
- How it is proven: an observed pre-shift and a conversation.
- Time and place: standing, inside pre-shift, paid.
- Waits on: `workflow.preshift.kitchen`; chef questions 15 and 16.
- Absorbs: KIT-045; the kitchen side of KIT-004; the kitchen side of FLV-006.

### KIT-060 A rotation through the kitchen
- Area: culinary
- Positions and timing: Floor, an elective after release, ongoing.
- What it teaches:
  - The required safety pieces first: KIT-016, CMP-111's floor version, SAF-013's porter version.
  - A supervised path through the porter's flow, prep basics, and a watch beside the pass.
  - How floor habits (a late fire, an unclear modification, a lingering runner) change the kitchen's night.
- What the person can do afterward: name how their floor habits change the kitchen's night; decide with a lead whether to continue toward a kitchen position.
- How it is proven: a conversation; the kitchen readiness drills if the person continues.
- Time and place: 8 h, scheduled paid shifts on site.
- Waits on: `chef.cross_training.scope`.
- Absorbs: KIT-060; the floor half of CUL-017.

### KIT-061 A shift on the floor
- Area: culinary
- Positions and timing: K, an elective for any cook signed off on a station or on production, within the first months.
- What it teaches:
  - Running food with a floor mentor, after SVC-003's carrying basics and SAF-004's handoff.
  - Watching tables receive plates; hearing customers' questions about dishes; seeing a refire land.
  - A debrief at the pass with KS.
- What the person can do afterward: name three things the floor needs from their station that they did not know, and change one habit.
- How it is proven: the debrief conversation. No test-out: the value is the shift itself.
- Time and place: 8 h (one paid service plus the debrief), on site.
- Waits on: the floor items needed to carry food safely; schedule placement.
- Absorbs: KIT-061; the kitchen half of CUL-017.

---

## 2. Leadership and teaching

### LEA-001 Teaching on the floor
- Area: leadership and teaching
- Positions and timing: LH, LFR, LS, LB, readiness for the lead seat (3 h). Mentors (D21) before their first mentee. MD: first month, with LEA-101, before the first mentee or the first observed teach the MD signs (moved out of the MD window; see Spine changes needed).
- What it teaches:
  - The teaching sequence for a floor or bar task (cognitive apprenticeship, Collins, Brown and Newman, verified-secondary): model it aloud (say the cue you are reading, not just the move); coach while they do it; scaffold (take part of the task so they can do the rest); fade the support on a plan; have them explain it back and reflect.
  - Breaking a task down: the movement apart from the decision (ORI-016); the one cue that decides each step.
  - Three choices in the moment, and the sign for each: step in (safety, an allergy, a customer about to be harmed or embarrassed); teach (a miss that will repeat and there is a quiet beat); let it run (a recoverable miss the learner will see themselves, talked through at close).
  - Never "just watch me": every demonstration names what to watch.
  - Teaching on a live night: one point per pass, at the side, never in front of a customer; the rest saved for close.
  - The trailing log the learner keeps (ORI-015) and what the teacher adds to it.
- What the person can do afterward: take a learner through one task from modeling to faded support across a shift, and say at each point why they stepped in, taught or let it run.
- How it is proven: a practical: teach a short task to a learner (a teammate or a new hire) observed by the MD or a calibrated lead, then a conversation on the three choices using two moments from it. Prove-first: an experienced trainer reads the material and takes the observed teach cold; if it meets the anchors, the remote and coached hours are skipped.
- Time and place: 3 h (1 remote and paid, 2 on site, including the observed teach).
- Waits on: Brandon interview topic "teaching a new cook" (its floor equivalent); `founder.mentor_criteria`; the movement library per position (ORI-016).
- Absorbs: LEA-001, LEA-012, LEA-020.

### LEA-011 Coaching a movement drill
- Area: leadership and teaching
- Positions and timing: LFR and LB, readiness for the lead seat (3 h); kitchen leads (CDP and above who coach a station's drills) by the chef's call.
- What it teaches:
  - The drill method from the coach's side: isolate the pattern; run it slow, fast and slow to fast; vary the conditions so it transfers; return it to the whole task (ORI-016; Duke, Simmons and Cash 2009, verified-secondary).
  - Finding the one error that matters, and changing one thing at a time.
  - Feedback that fades: frequent at first, then summary feedback after a set, then the learner's own self-review against the reference.
  - Cues aimed at the result (the stream, the plate landing level), not the body part.
  - Banking a drill: when a run-through counts toward a practical (D11), and what is recorded.
  - Running the warm-up drill at pre-shift (CUL-001, D44).
- What the person can do afterward: run a drill session in which the learner's drill measurably improves, and record it as banked evidence.
- How it is proven: a coached-drill check: a learner's run-through before and after the session, rated by a calibrated rater against the drill's anchors. Prove-first: the coached-drill check taken cold. Where the drill carries a safety element (hot plates, the knife), the coach is checked on stopping an unsafe rep every time; that part never tests out.
- Time and place: 3 h on site, paid.
- Waits on: the drill anchors for SVC-003, BEV-002, BEV-012 and the kitchen drills; `tool.forms.gate_record` for banked runs.
- Absorbs: LEA-011.

### LEA-018 Holding the standard as a peer
- Area: leadership and teaching
- Positions and timing: every lead (LH, LFR, LS, LB), readiness for the lead seat (1.5 h).
- What it teaches:
  - The standard walk: what a lead looks at before doors and once an hour (the set room, the bar station, the pass side), against the standards book (D46).
  - Saying it without policing: one line, to the person, out of the customer's earshot, about the task (CUL-002).
  - When a miss is coaching and when it goes to a manager. A lead holds no authority over discipline or pay (D5), and never implies it.
  - Holding the standard on your own work first: the lead is held to the recheck too (D44).
  - Peer to peer across teams: a lead runner naming a bar miss, a lead bartender naming a floor miss (intake group 4).
- What the person can do afterward: walk a section, name the faults, and correct one with a peer in a way that fixes it and keeps the relationship.
- How it is proven: a role-play of two corrections (one easy, one with a senior teammate); an observed standard walk. Prove-first: both taken cold after reading the material.
- Time and place: 1.5 h on site, paid.
- Waits on: the standards book, floor half (D46); the HR ruling on hourly leads (D5).
- Absorbs: LEA-018.

### LEA-005 Running pre-shift as teaching
- Area: leadership and teaching
- Positions and timing: MD (2 h, readiness); LH (host-updates part, 1 h, readiness for the lead seat); LB (bar-update part, 1 h). OM: first month (2 h), before the OM first leads a pre-shift alone; in the window the OM attends the MD's pre-shifts.
- What it teaches:
  - Pre-shift is teaching and improvement, not announcements (D22). One gathering, led by the MD, the OM or the lead host.
  - A running order: the warm-up drill (D44); what changed (menu and list changes, allergens first, MNU-002); the book (the door's part); one thing that went wrong last night and the change; the teaching slot; the night's intent in one line (LEA-027).
  - The teaching slot rotates to any rank, is voluntary, is part of the paid shift and never counts toward promotion (D22, D43). How to help a volunteer prepare (LEA-019).
  - Recall over telling: asking two people to say the standard aloud instead of reading it out.
  - Keeping it inside its time (`team.preshift_format`).
  - Host-updates part (LH): the book in a few lines: pacing pinch points, large parties, allergies and occasions, flags, kitchen visits (SYS-116).
  - Bar-update part (LB): batch status, 86s, list changes, the drink to describe tonight, the palate note from tasting (BEV-019).
- What the person can do afterward: run a pre-shift inside its time that teaches one thing and leaves every person with the night's changes.
- How it is proven: an observed pre-shift with a short debrief; for the parts, an observed update. Prove-first: an experienced manager or lead reads the format and runs the observed pre-shift cold.
- Time and place: MD 2 h; parts 1 h; on site, paid.
- Waits on: `team.preshift_format`; the kitchen's part (KIT-045); D44's warm-up content per position.
- Absorbs: LEA-005; CUL-016 and CUL-026 (with CUL-001); the pre-shift frame of LEA-019.

### LEA-019 Teaching one thing at pre-shift
- Area: leadership and teaching
- Positions and timing: anyone who volunteers for the rotating slot (D43), ongoing.
- What it teaches:
  - Choosing one point small enough for the slot.
  - Showing it, not reading it: a demonstration or a single example.
  - Ending with a question the team answers aloud.
  - Asking the MD or a lead for help preparing.
- What the person can do afterward: teach one point at pre-shift inside the slot.
- How it is proven: a short conversation with the pre-shift leader afterward. Never counted toward promotion (D43).
- Time and place: 1 h, on site, paid.
- Waits on: `team.preshift_format`.
- Absorbs: LEA-019 (the teacher's side).

### LEA-015 Mentoring a new hire through the path
- Area: leadership and teaching
- Positions and timing: designated mentors (`founder.mentor_criteria`), readiness before the first mentee. LS and LB ongoing.
- What it teaches:
  - The mentor's role (D21): the trainer on the angel shift (Brandon's name for the gate shift where the trainer oversees the person the whole night) and the mentor are one person, through the readiness window and the first ninety days.
  - The tension, named: the mentor both advocates and judges. The release decision rests on the gate record (D8), and a second rater joins any gate the mentor rates.
  - Before day one: contact made, what the person needs to arrive with, the readiness plan read (LEA-103).
  - The trailing: what the mentor says aloud; model then coach; when support fades (LEA-001).
  - The trailing log and the weekly check-in: what is going well, what is stuck, the next booking.
  - Spotting struggle early, and that struggle in readiness is normal (ORI-015); a not-yet extends the paid window and is not a verdict on ability, and the mentor says so; routing a stuck path to an unblock conversation (LEA-006).
  - The trainee is extra to staffing on trailing and angel shifts (`workflow.angel_shift_staffing`).
- What the person can do afterward: take a new hire from day one to release with a current log, weekly check-ins and nothing stuck for more than a week.
- How it is proven: a conversation with the MD on a mock trailing log; the first mentee's path reviewed at release. Prove-first: the mock-log conversation taken cold; the first mentee's review always runs.
- Time and place: 2 h (1 remote and paid, 1 on site).
- Waits on: `founder.mentor_criteria`; `workflow.angel_shift_staffing`; the readiness plans from this rebuild.
- Absorbs: LEA-015; LIB-003's reading becomes its reading list.

### LEA-003 Running the angel shift
- Area: leadership and teaching
- Positions and timing: mentors, leads and managers who run angel shifts, ongoing (LH, LFR and LB after release as leads; MD and OM).
- What it teaches:
  - What the angel shift is: the learner runs the shift, the mentor is beside them and steps in only on the step-in signs (LEA-001).
  - Before: the cases to watch for, agreed with the learner.
  - During: supervising without taking over; what the mentor notes, and where (never on a device during service, D8).
  - After: the close conversation; what is recorded in the gate record at close; when unsupervised shifts after sign-off start (D10).
  - What a release covers: at least one supervised service is a full night (`workflow.full_night`), and the person is released only for the dayparts they were supervised in (D10).
- What the person can do afterward: run an angel shift where the learner did the work, and leave a record that supports the release call.
- How it is proven: co-run one angel shift with the MD, then a conversation on the record. Prove-first: an experienced trainer runs the first one with the MD present as co-rater; the conversation on the record is the same.
- Time and place: 1 h on site, paid, plus the co-run.
- Waits on: `tool.forms.gate_record`; the gate specs per position.
- Absorbs: LEA-003.

### LEA-002 Assessing a practical
- Area: leadership and teaching
- Positions and timing: MD and OM in the first month, before the first booked check slot (D19). HB in the readiness window (6 h): at opening the HB signs every bar practical, so the HB must be calibrated before the bar staff's windows start; the MD and OM assess floor and office gates only after their own windows, so the first month is enough for them. LS, LFR, LH, LB, kitchen leads, after calibration and audit (D5), before signing alone. Kitchen part: kitchen assessors the executive chef names, and the EC.
- What it teaches:
  - Frame-of-reference calibration: rating recorded examples against the gate spec's anchors until the rater's scores match the reference.
  - Process and product rated apart (ACF and Bocuse d'Or practice, carried).
  - Safety elements pass on every attempt; a safety miss is a not-yet regardless of other scores (D11).
  - Banked drill runs against the integrated practical: movement drills may be banked, the integrated practical may not (D11).
  - A second rater on any gate the mentor rates (D21); co-rated audits, and what happens when two raters disagree.
  - Rechecks: what is checked and how a recheck miss is handled.
  - Writing the gate record at close (D8): the rater named, each anchor scored, the evidence noted.
  - Kitchen part: techniques chosen by the assessor on the day (the UK chef de partie standard's method, verified-primary, carried); the kitchen's own anchors.
- What the person can do afterward: rate a practical so that a calibrated co-rater agrees, and record it correctly.
- How it is proven: rating recorded clips against the anchors; co-rated live audits; signing alone only after the audits agree (D5). Prove-first: an experienced assessor rates the clips cold; if the ratings match the reference, the remote session is skipped. The co-rated live audits always run, because they are the calibration on Sŏn's anchors.
- Time and place: 6 h (3 remote and paid, 3 on site).
- Waits on: the gate specs and anchors per module (Assessment and Competency Designer); `tool.forms.gate_record`; the chef's anchors for the kitchen part; the HR ruling on hourly leads (D5).
- Absorbs: LEA-002, LEA-013, KIT-051.

### LEA-014 Holding a spoken check
- Area: leadership and teaching
- Positions and timing: same as LEA-002 and for the same reason (MD and OM first month; HB in the window, 2.5 h, because the HB holds bar spoken checks from opening; leads after calibration).
- What it teaches:
  - Set cases and neutral questions; following the customer's questions rather than a script (D40).
  - Scoring the content, not the fluency or the accent.
  - Sampling across the unit rather than quizzing one fact; the full current menu and pairings at depth where the check covers them (D40).
  - Separate practice and check banks so the check is not memorized (D14).
  - Non-compensatory items: an allergen error fails the check whatever else is right.
  - Recording the result and the not-yet plan (LEA-016).
- What the person can do afterward: run a spoken check that is fair, specific and recorded.
- How it is proven: a recorded mock check reviewed by Brandon. Prove-first: the recorded mock check taken cold after reading the material.
- Time and place: 2.5 h (1.5 remote and paid, 1 on site).
- Waits on: the case banks per module; `tool.forms.gate_record`.
- Absorbs: LEA-014.

### LEA-016 Delivering a not-yet and the changed practice plan
- Area: leadership and teaching
- Positions and timing: MD, readiness (1.5 h), because the MD holds the first floor gates at release. OM in the first month, with LEA-002, since the OM delivers no not-yet before assessing. Every assessor before signing alone (ongoing).
- What it teaches:
  - "Not yet" is a changed practice plan, never a verdict (D11).
  - The conversation: what was seen, against the anchor; what is already solid; the one or two things that change; the plan.
  - The plan: what to practice, how, with whom; the required interval before the next attempt (`workflow.retry_interval`); the booking link (D13).
  - Repeated misses trigger an unblock conversation about fit (LEA-006, LEA-017), never a counter.
  - A not-yet extends the paid window; it is normal and is never read as a verdict on ability (ORI-015). A failed cold attempt under prove-first is not a not-yet: it routes the person into the instruction with no interval and no recorded miss.
  - Delivered privately, at close or in a booked check slot, never on the floor.
- What the person can do afterward: deliver a not-yet the learner can repeat back as a plan, and record it.
- How it is proven: a role-play with two cases (a near miss and a safety miss); a recorded plan reviewed. Prove-first: the role-play taken cold.
- Time and place: 1.5 h on site, paid.
- Waits on: `workflow.retry_interval` and the fail-limit shape (`team.fail_limit`, D11); TBRI review.
- Absorbs: LEA-016.

### LEA-006 The unblock conversation
- Area: leadership and teaching
- Positions and timing: MD, OM and leads, ongoing.
- What it teaches:
  - When it happens: a learner asks for a direction, a path is stuck, or misses repeat (D13).
  - Ten to fifteen minutes, booked from the link into a booked check slot.
  - The first question: is this to learn or to move? It is recorded, because the answer changes what is offered.
  - The four recorded outcomes (D13; the wording below is the working draft carried from `research/phase2-working/06-draft.md`, to confirm with Brandon as `workflow.unblock_outcomes`):
    - Learning opened: a track or elective is opened for study by interest, with no change of position (for example a food runner starting the spirits track).
    - A move opened: the next or adjacent position's path is opened, with its readiness plan built (LEA-103) and a start date.
    - Reserve: the person joins the paid cover pool for another position they are released on, chosen, never conscripted.
    - Not now: with the reason stated in plain words, what would change the answer, and a date or trigger to reopen it.
  - Never ending without one of the four, and never leaving "not now" without its reason and reopen trigger.
  - The annual recommitment conversation (formerly CUL-024) runs as a step in this same format (`workflow.recommitment`, `founder.recommitment_format`): it is a people process, not a module.
  - Recording it at close.
- What the person can do afterward: run an unblock conversation and leave one of the four recorded outcomes, with its next step or its reason and reopen trigger.
- How it is proven: co-run one with the MD. Prove-first: an experienced manager runs the first one with the MD present; the record is reviewed the same way.
- Time and place: 1 h on site, paid.
- Waits on: `workflow.unblock_outcomes` (Brandon to confirm the four); `workflow.check_slots`; `workflow.recommitment`.
- Absorbs: LEA-006; CUL-024 as a workflow step, not a module.

### LEA-101 Running booked check slots
- Area: leadership and teaching
- Positions and timing: MD and OM, first month (outside the window, before the first booked check slot); calibrated leads, ongoing.
- What it teaches:
  - Booked check slots (`workflow.check_slots`) are the only bookable times for practicals, spoken checks and unblock conversations (D13). They are protected on the calendar and never eaten by service.
  - Preparing from the learner's record before the slot: the module, the last attempt, the not-yet plan.
  - Running mixed bookings on time.
  - The live-gate cap per service (`workflow.live_gate_limit`, D19), and counting assessor hours per cohort against it: at opening every new hire needs the same few assessors at once, so the pre-opening calendar (`workflow.preopening_calendar`) starts managers before line staff and the HB before bar staff.
  - The standing recheck (formerly CUL-023, now a mechanism, not a module): rechecks on `workflow.recheck_cadence` are booked into these slots or run inside the warm-up.
  - Writing the gate record at close (D8).
  - The unbooked-link reminder, and what to do when blocks run out (`workflow.unbooked_link_reminder`).
- What the person can do afterward: run a full block of mixed bookings on time and leave every record complete.
- How it is proven: co-run one set of slots, then run one observed. Prove-first: an experienced manager skips the remote hour and runs the observed set first; the co-run is dropped if it meets the standard.
- Time and place: 3 h (1 remote and paid, 2 on site).
- Waits on: `tool.scheduling.platform`; `workflow.check_slots`; `workflow.preopening_calendar`; `workflow.live_gate_limit`; `tool.forms.gate_record`.
- Absorbs: none.

### LEA-102 The manager's side of the learning system
- Area: leadership and teaching
- Positions and timing: MD and OM, first month.
- What it teaches:
  - Reading the learning system's reports and the gate records.
  - Assigning paths and variants: green hire, experienced hire, internal move.
  - Running test-outs (D56): which modules allow them, how the evidence is checked, and that safety never tests out.
  - Recording prove-first attempts: a failed cold attempt is logged as routed to instruction, never as a miss (D11).
  - Recording release by daypart, and the unsupervised shifts after sign-off (D10).
  - Scheduling rechecks (`workflow.recheck_cadence`; the former CUL-023 runs here) and re-proofs on every menu or list change (D40).
  - Seeing that each person's weekly ongoing-education hours (`policy.ongoing_education_hours.<position>`) are on the schedule and used, so no study drifts home unpaid (D41).
  - Routing every override to Brandon (D1). What managers do not do: approve modules or change the assessor roster.
- What the person can do afterward: keep every learner's record current and route the decisions that are not theirs.
- How it is proven: a practical on a staged roster with planted issues (an expired recheck, a skipped safety item, an override, a failed cold attempt recorded as a miss). Prove-first: the staged-roster practical taken cold.
- Time and place: 3 h (2 remote and paid, 1 on site).
- Waits on: `tool.lms.*`; `tool.forms.gate_record`; the automation (D8).
- Absorbs: the manager part of LEA-040 (the owner part stays with Brandon, D1).

### LEA-103 Building a new hire's readiness plan
- Area: leadership and teaching
- Positions and timing: MD, readiness (2 h), because the MD builds the floor's plans at opening. OM: first month. The kitchen pair (KO, KS, CDC): before the first cook's start date or in the first month, whichever comes first (`workflow.preopening_calendar`).
- What it teaches:
  - Choosing the variant: green hire, experienced hire with its test-outs, internal move (which never repeats a signed-off module and re-proves only currency).
  - Laying out the window: 40 paid hours a week, part remote, no overtime, two weeks preferred and three at most (D55); the position's module list and hours from the spine.
  - Planning room for a retry: a two-week route is planned to about 72 h and a three-week route to about 100 h, so one supervised service plus one recheck fit if a not-yet happens. A not-yet extends the paid window and is normal (ORI-015).
  - Supervised services counted at shift length (`workflow.shift_length.<position>`), at least one a full night, and only the dayparts the person will work (D10).
  - A day-by-day sequence: the safety items and the service calls before the first supervised service; remote work kept to about 3 h a day; drills from day two (spine section 2.6).
  - The levers when a plan runs over: the certificate timing (`founder.compliance_timing`), moving modules to the first month, prove-first attempts (D56; safety never tests out).
  - Booking the assessor hours the plan needs against `workflow.live_gate_limit`.
  - Assigning the mentor (D21); the trainee extra to staffing.
  - The ninety-day plan with check-ins (WP Part II "Onboarding", cited).
  - Keeping readiness and ongoing education apart, and placing the position's weekly ongoing-education hours (`policy.ongoing_education_hours.<position>`) from release on.
- What the person can do afterward: produce a readiness plan for each variant of a position that fits the window and names the mentor.
- How it is proven: a practical: two plans (a green food runner, an experienced bartender) reviewed by Brandon, each showing its retry room. Prove-first: the two plans built cold.
- Time and place: 2 h (1 remote and paid, 1 on site).
- Waits on: the signed spine; `founder.compliance_timing`; `founder.mentor_criteria`; `policy.ongoing_education_hours.<position>`; `workflow.shift_length.<position>`.
- Absorbs: none.

### LEA-024 Reading the team's load
- Area: leadership and teaching
- Positions and timing: LS and MD, readiness (2 h): from the first night they run the floor solo, reading who is going under is part of the job, so it cannot wait for the first month. LB ongoing.
- What it teaches:
  - The signs someone is going under before it shows at a table: shortened answers, a skipped callback, a section where three tables wait at once, a person stuck at the pass or the POS, a drop in the small checks.
  - Reading the book and the floor together: which sections and stations will be hit and when.
  - What help looks like: moving a task, not taking the table (SVC-067); calling it early.
  - Depletion over weeks, not just one night (CUL-003).
- What the person can do afterward: name, on a live night, who is closest to going under and the one move that helps.
- How it is proven: an observed full shift with a debrief on three moments. Prove-first: an experienced lead or manager goes straight to the observed shift.
- Time and place: 2 h on site, paid.
- Waits on: Brandon interview (how he reads a team's load).
- Absorbs: LEA-024, CUL-014.

### LEA-027 Giving intent, not instructions
- Area: leadership and teaching
- Positions and timing: MD and OM (readiness, 1.5 h); KO, KS and CDC (onboarding).
- What it teaches:
  - Stating intent so the team can act when the script breaks: what we are trying to achieve tonight, and why (commander's intent, ADP 6-0, verified-secondary).
  - The one-line intent at pre-shift.
  - Matching the house's decision order (`founder.decision_order`, ORI-003).
  - Judging the call, not the result, when someone acted on intent.
- What the person can do afterward: give a night's intent in one line that a teammate could act on in a case nobody planned for.
- How it is proven: a spoken check on three cases: give the intent, then predict what a teammate does with it. Prove-first: the spoken check taken cold.
- Time and place: 1.5 h (0.5 remote and paid, 1 on site).
- Waits on: `founder.decision_order`; Brandon's decision interviews (D45).
- Absorbs: LEA-027.

### LEA-028 The parallel pair in service
- Area: leadership and teaching
- Positions and timing: MD and OM, readiness (2 h).
- What it teaches:
  - The split (WP Part I "The management layer", cited): the OM answers for labor, cost, compliance, vendors and the facility; the MD for the room, the team's development, customer relationships and recovery. Neither reports to the other.
  - What each holds on the night, and the handoffs between them.
  - Covering each other's day off.
  - The office half of the split is ADM-101.
- What the person can do afterward: say who holds each of ten named moments on a service night.
- How it is proven: a spoken check on the ten moments, taken together as a pair. Prove-first: the pair read the split and take the spoken check cold.
- Time and place: 2 h on site, paid.
- Waits on: Brandon's decision on how the pair split everything else (D1).
- Absorbs: LEA-028 (the service half).

### LEA-029 Owning the room, delegating the door
- Area: leadership and teaching
- Positions and timing: MD, readiness (3 h).
- What it teaches:
  - Responsibility and presence split (D20): the MD holds responsibility for everything, the door included; during service the door is delegated to the lead host.
  - Owning the room is neither being a super-server nor a host: where the MD stands, what they watch, when they move.
  - The handback triggers, named before service (BG 15 "Floor authority", cited; SVC-068).
  - Stepping into the door on the named cues, and stepping out again.
  - Where BG 15 and D20 disagree, the module cites D20 until Brandon's canon edit (D51).
- What the person can do afterward: run a service owning the room, stepping into the door only on the named cues, and say why at each step-in.
- How it is proven: an observed full service with Brandon, debriefed on each step-in. Prove-first: an experienced Maître d' skips the remote hour; the observed service always runs.
- Time and place: 3 h (1 remote and paid, 2 on site), plus the observed service counted in the MD window.
- Waits on: Brandon interview (the MD's step-in cues); the canon edit (D51).
- Absorbs: LEA-029, LEA-030; LIB-002's reading becomes its reading list.

### LEA-010 Calling a live failure across domains
- Area: leadership and teaching
- Positions and timing: MD and OM, readiness (1 h).
- What it teaches:
  - Failures that cross both domains: a sensor alarm mid-service, a POS outage, a short-staffed night, an injury on the floor.
  - The rule the pair agrees: who calls it, who supports, who tells Brandon (`workflow.cross_domain_call`).
  - Calling it fast and once.
- What the person can do afterward: name the caller and the first move in four cross-domain cases.
- How it is proven: a spoken check with both managers together. Prove-first: the spoken check taken cold.
- Time and place: 1 h on site, paid.
- Waits on: `workflow.cross_domain_call` (the pair sets it with Brandon).
- Absorbs: LEA-010.

### LEA-021 Running a private incident review
- Area: leadership and teaching
- Positions and timing: MD, OM and kitchen leaders (KS, CDC, EC), ongoing.
- What it teaches:
  - Process first: "the first question is not who failed" (WP p.17, cited); blame the process, fix the process (WP Part II).
  - Just culture: separating error, at-risk choice and reckless choice (Reason and Dekker, verified-secondary).
  - Running it: the record (ADM-110); the timeline; the participant explains what happened in the process; contributing conditions; one change and its owner.
  - Kept private and apart from open everyday feedback (D22). Harassment complaints go to the HR seat, never here.
- What the person can do afterward: run a review that ends in one process change and leaves the people in it able to keep working.
- How it is proven: co-run one review on a staged incident with Brandon; TBRI reviews the module. Prove-first: an experienced manager runs the staged review cold with Brandon.
- Time and place: 3 h (1 remote and paid, 2 on site).
- Waits on: `founder.incident_policy`; TBRI and Culture seats review; who runs kitchen reviews (chef question 21).
- Absorbs: CUL-018 (the review side).

### LEA-022 Stewarding everyday critique
- Area: leadership and teaching
- Positions and timing: leads (LS, LFR, LH), ongoing.
- What it teaches:
  - Keeping open critique open and safe: the house protocol (CUL-002), modeled by the lead.
  - Noticing who never speaks, and asking privately rather than calling on them in public (D14 caution).
  - Stopping a critique that has turned to the person.
- What the person can do afterward: steer an after-service round so the notes stay on the task and more than the same few voices speak.
- How it is proven: an observed after-service round and a conversation. Prove-first: an experienced lead goes straight to the observed round.
- Time and place: 1.5 h on site, paid.
- Waits on: TBRI and Culture seats review.
- Absorbs: LEA-022.

### LEA-023 Noticing drift
- Area: leadership and teaching
- Positions and timing: MD, OM and leads, ongoing.
- What it teaches:
  - Complacency and normalized shortcuts: the step that quietly disappears on an ordinary night.
  - The watchlist signals (D14; the list is the one D14 adopted from `research/starting-structure-2026-09.md` question 12, plus the drift signals the red team named), each a prompt to look, never a target or a mark against a person:
    - Healthy signs: people asking for practicals or rechecks unprompted; errors raised at pre-shift by the person who made them; critique across roles (a runner naming a bar miss).
    - Complacency signs: modules completed with no practical requested after; ratings with no spread across a team; the same few voices answering in every critique round, or silence in the rounds.
    - Drift signs: a step skipped on an ordinary night that is kept on a busy one (a callback dropped, a table not reset to the setting); a pattern of recheck misses on the same item across people; a shortcut that has a name on the floor.
  - What each sign asks the leader to do: look and ask privately, never announce it; "the same few voices" prompts a look for concealment, not a judgment of the quiet (D14).
  - Using the recheck and the standards walk to find drift (D44, LEA-018), and turning a confirmed drift into one improvement (LEA-025).
- What the person can do afterward: name one drifted practice in their area, the sign that showed it, and the recheck that would catch it.
- How it is proven: a conversation with the MD on a month's observations, naming the signs seen and what was done about each. Prove-first: an experienced manager brings the month's observations without the on-site session.
- Time and place: 1.5 h on site, paid.
- Waits on: the D14 watchlist as Brandon confirms it; `workflow.recheck_cadence`.
- Absorbs: LEA-023, ORI-031.

### LEA-025 Leading one improvement at a time
- Area: leadership and teaching
- Positions and timing: leads, ongoing (LFR named in the spine).
- What it teaches:
  - Picking one improvement from the nightly review or the floor.
  - Stating how you will know it worked, measured without a business figure (a count of misses, a time, a check result).
  - Running it for a set time, then closing it: kept, changed or dropped.
- What the person can do afterward: lead one improvement from choice to close and report it at the weekly meeting.
- How it is proven: the closed improvement, presented to the MD. Prove-first: an experienced lead skips the session; the closed improvement is the proof for everyone.
- Time and place: 2 h on site, paid, then the improvement inside shifts.
- Waits on: the weekly meeting format.
- Absorbs: LEA-025.

### LEA-046 The nightly review of the service
- Area: leadership and teaching
- Positions and timing: MD runs it; LH and LS take part. Ongoing, standing.
- What it teaches:
  - What went right, what went wrong, one change (TC 25-20 after-action review, verified-secondary).
  - The decision note: a call made tonight worth keeping for the library (LEA-037).
  - What feeds tomorrow's pre-shift.
  - Writing it to the documentation standard (ADM-109).
- What the person can do afterward: run a nightly review inside its time that ends in one change and one note.
- How it is proven: observed reviews in the first month. Prove-first: the first observed reviews are the proof; the session is skipped if they meet the standard.
- Time and place: standing, a few minutes at close, paid.
- Waits on: `workflow.day_close`; the library's home.
- Absorbs: LEA-046 (its documentation half sits in ADM-109).

### LEA-036 Explaining the call: the reference panel
- Status: parked until the D14 reference panel exists. Its content is the panel mechanism, and it carries no hours until then. "Explaining a call" to a teammate moved to LEA-037.
- Area: leadership and teaching
- Positions and timing: MD and EC, ongoing.
- What it teaches:
  - The reference panel (D14): judgment cases built from Brandon's interviews, with minority views kept.
  - Anchoring a case: the cue, the move, the reason.
  - It measures alignment; it never gates advancement until calibrated leads join (D14).
- What the person can do afterward: anchor a panel case and explain the call to a team member.
- How it is proven: panel cases reviewed with Brandon. No test-out.
- Time and place: open, on site, paid.
- Waits on: Brandon's decision interviews (D45).
- Absorbs: LEA-036 (the explaining part went to LEA-037).

### LEA-037 Capturing a decision for the house library
- Area: leadership and teaching
- Positions and timing: MD ongoing; LH ongoing. Kitchen part: KO, KS, CDC and EC, ongoing; CDP contributes.
- What it teaches:
  - The decision interview method in short form: the incident, the cues, the options, the call (Critical Decision Method, as D45 uses it).
  - Writing a decision note another person could apply.
  - Explaining a call to a teammate (moved from LEA-036): the cue you saw, the move you made, the reason, and what would have changed it, said in under a minute and away from the customer.
  - Where it lives, and who approves it.
  - Kitchen part (moved from KIT-043): after-service capture of a night's lesson on the line; the same note format; entries reviewed by the executive chef before they enter the library; recipes themselves follow the chef's format (KIT-043).
- What the person can do afterward: turn a night's call into a library entry, and explain the call to a teammate so they could make it next time.
- How it is proven: two entries reviewed by Brandon (kitchen entries by the executive chef) and one observed explanation to a teammate. Prove-first: an experienced manager submits the two entries without the session.
- Time and place: 2 h on site, paid.
- Waits on: the library's home (Box); D45 transcripts; the chef for the kitchen part.
- Absorbs: LEA-037, LEA-008, LEA-049; the explaining part of LEA-036; the library mechanics of KIT-043.

### LEA-045 Inspecting the house as a customer would
- Area: leadership and teaching
- Positions and timing: MD, ongoing.
- What it teaches:
  - The inspection walk, taken as a customer would, from outside to the door again. Each stop and what is checked (standards cited to the canon page or bound, never written here as fact):
    - Arrival and approach: what the customer sees first from the street and the entrance, signage and light, anything out of place (`brand.*` exterior; the space, D58).
    - The wait at the door: how long before a greeting, what the customer sees and hears while waiting, whether the book matched them (SVC-010).
    - The threshold: the point where the street ends and the room begins; whether kitchen or back-of-house sound crosses it (BG 13, beat 8).
    - The walk to the table: the route, the pace, what the customer passes.
    - The set table: the setting against the standard, cleanliness, chairs, the position numbering (`workflow.floor.setting`).
    - Sound and light: music level and light against the presets for the daypart, and whether they have drifted with the room (SVC-069).
    - The restroom: clean, stocked, the same standard as the room.
    - The bar sightline: what the bar shows the room, what a seated customer sees of the back bar and the work.
    - Departure: coats, the door, the last words, the street again.
  - Outside eyes: what a first-time visitor notices that the team no longer does.
  - Turning findings into one change each, with an owner, through LEA-025.
- What the person can do afterward: run the walk through every stop and bring three findings, each with a change and an owner.
- How it is proven: a presented walk to Brandon, stop by stop. Prove-first: an experienced Maître d' presents a walk without the on-site session.
- Time and place: 3 h on site, paid.
- Waits on: `founder.inspection_policy` (D50): who walks, how often, and whether outside visitors are used; the space (D58); BG 13 and BG 14 re-read in Box.
- Absorbs: LEA-045, ORI-013, CUL-027.

### LEA-007 Taking critique and repairing a lapse in front of the team
- Area: leadership and teaching
- Positions and timing: MD, OM and leads, ongoing, in the first months in the seat.
- What it teaches (the leader's side only; the everyone part of taking a note is CUL-002):
  - Why it is harder from the top: a leader's defensiveness teaches the whole team that critique upward is unsafe, and the same few voices stop speaking (D14).
  - Taking a note from below in public: listen to the end, ask one question to understand, thank the person by name, and say when you will answer. No explanation in the moment, no correction of the person's tone.
  - Closing the loop: coming back to the person and, where the note was public, to the team, with what you decided and why, even when the answer is no.
  - Never paying it back: no change in the person's shifts, sections or tone toward them after a note. A suspicion of retaliation routes through the HR route (CMP-103), not to the leader.
  - Critique of a leader is invited, never required (D42).
  - Repairing a lapse (a raised voice, a cutting line, a correction in front of a customer): name it, own it, no "but"; say what you will do differently; do it soon and privately, and in front of the team if it happened in front of them.
  - Where repair is not enough: anything that may be harassment or discrimination goes to the HR route (CMP-103), and the repair conversation never replaces it.
- What the person can do afterward: take a public note from a team member without defending and close the loop; repair a lapse so the person and the team can keep working with them.
- How it is proven: a role-play of two cases (a public note at the after-service round, and a lapse at the pass witnessed by the team) and a conversation on what each case taught. TBRI reviews the module. Prove-first: the two role-plays taken cold.
- Time and place: 1.5 h on site, paid.
- Waits on: TBRI review; the HR route (CMP-103).
- Absorbs: LEA-007, LEA-047.

### LEA-017 The fit conversation after repeated misses
- Area: leadership and teaching
- Positions and timing: MD and OM, ongoing.
- What it teaches:
  - When it happens: repeated misses on a gate (D11), never a counter.
  - Honest and private, with a path: another practice plan, another position, or a different route.
  - What managers decide and what goes to Brandon (D1) and the HR seats.
- What the person can do afterward: hold a fit conversation that the person leaves knowing their options.
- How it is proven: a role-play reviewed by Brandon. Prove-first: the role-play taken cold.
- Time and place: 1.5 h on site, paid.
- Waits on: `team.fail_limit`; HR seats review; TBRI review.
- Absorbs: LEA-017.

### LEA-041 Governing the house's customer relationships
- Area: leadership and teaching
- Positions and timing: MD, ongoing.
- What it teaches:
  - The record belongs to the house, so a customer relationship does not drift or leave with a person.
  - The regulars policy (`founder.regulars_policy`): what servers may keep, and what must live in the house record.
  - Reviewing the record's quality with the lead host (SYS-117).
  - The tool and permission side is SYS-120.
- What the person can do afterward: say who holds each important customer relationship and confirm it is in the record.
- How it is proven: a review of the record with Brandon. Prove-first: the review without the session.
- Time and place: 2 h on site, paid.
- Waits on: `founder.regulars_policy`; `founder.customer_data_policy`.
- Absorbs: LEA-041 (the tool side went to SYS-120); SVC-040's governance.

### LEA-004 Writing and reviewing a module
- Status: parked with SYS-144 until Brandon opens authoring (D1). It is a studio skill with no position need yet, and it leaves the module count until then.
- Area: leadership and teaching
- Positions and timing: authors Brandon names, ongoing, once he opens authoring.
- What it teaches:
  - The module source format and the bindings rule (CLAUDE.md, `framework/bindings.md`).
  - Designing a practice: the movement apart from the decision; anchors; a check bank apart from the practice bank.
  - The library voice; the standing rules.
  - The review panel and the lifecycle (`framework/lifecycle.md`).
- What the person can do afterward: draft a module that passes review.
- How it is proven: a drafted module through review. No test-out.
- Time and place: open, paid.
- Waits on: Brandon opening authoring (D1).
- Absorbs: LEA-004, LEA-038, LEA-042.

### LEA-104 Leading a kitchen without harm
- Area: leadership and teaching
- Positions and timing: KO, KS, CDC and EC, readiness (onboarding, 4 h); CDP ongoing.
- What it teaches:
  - The documented pattern of abuse in elite kitchens and why it is tolerated (Burrow et al., verified-secondary; Bloisi and Hoel, lead-only, carried).
  - BG 01 as overriding authority: intensity and precision kept, degradation not.
  - Correction aimed at the task, in private when it concerns the person (D22); one line in service, the rest at close.
  - Fatigue and bandwidth (WP pp.16 to 17, cited); "bandwidth is at zero" is a design problem.
  - Repair after a lapse (LEA-007).
- What the person can do afterward: correct a mistake mid-service in a way that fixes the plate and keeps the person.
- How it is proven: role-play and a conversation; observed in service. No test-out: treated as a safety module for people. It targets habits experienced kitchen leaders bring with them, a role-play passed cold does not show the habit under service pressure, and BG 01 makes the line a non-negotiable.
- Time and place: 4 h on site, paid.
- Waits on: chef question 20; Brandon interview topics "a correction that worked, and one that did not" and "what you will not carry".
- Absorbs: LEA-104 (draft LEA-171), KIT-044.

### LEA-105 Briefing, coaching and teaching at the station
- Area: leadership and teaching
- Positions and timing: CT and the kitchen pair (KO, KS, CDC), readiness (3 h), counted in their windows: they brief and coach at the station from their first service. CDP ongoing.
- What it teaches:
  - The station brief before service: what changed, what to watch, who is where.
  - Coaching during service: one line, at the station, about the task.
  - Teaching a new cook: model aloud, coach, scaffold, fade, then have them explain and reflect (Collins, Brown and Holum, verified-primary, carried); never "just watch me".
- What the person can do afterward: bring a new cook to station sign-off with a planned fading of support.
- How it is proven: an observed teach and a conversation. Prove-first: an experienced chef goes straight to the observed teach.
- Time and place: 3 h on site, paid.
- Waits on: Brandon interview topic "teaching a new cook"; the chef.
- Absorbs: LEA-105 (draft LEA-172), KIT-032, KIT-050.

### LEA-106 The executive chef's onboarding to the people and training system
- Area: leadership and teaching
- Positions and timing: EC, inside the EC's onboarding (not a readiness window), before the first cook's start date (`workflow.preopening_calendar`).
- What it teaches:
  - Who owns what: Brandon owns people and training for now (D1); the chef owns kitchen content, standards and every `chef.*` binding (D30); what is founder-gated, chef-gated or team-gated, and how a gated call is marked rather than landed.
  - The readiness window as it applies to the kitchen (D55): 40 paid hours a week, part remote and paid, no overtime ever, two weeks preferred and three at most, with retry room planned (LEA-103). A cook is released solo on a named non-peak service; peak nights follow under KIT-030.
  - How proof works: spoken check, practical, recheck; safety elements pass on every attempt; prove-first for experienced cooks (a failed cold attempt is not a miss); a not-yet is a changed practice plan with an interval, never a verdict (D11); release only after a real full night and only for the dayparts supervised (D10).
  - Booked check slots, the live-gate cap per service (`workflow.live_gate_limit`) and the gate record written at close, never on a device during service (D8).
  - What the EC signs: the kitchen anchors (LEA-002 kitchen part); station sign-offs or who signs them; kitchen entries to the house library (LEA-037); the list of `chef.*` bindings the kitchen modules wait on (section 6 of this file), with a date for each.
  - The house rules for correction and critique in a kitchen: correction aimed at the task, private when it concerns the person (D22), BG 01 as the line; LEA-104 as the standard every kitchen leader is held to.
  - Paths and ongoing education for the kitchen: porter to commis, commis to a station, production as a full career (WP p.11); the unblock conversation and its four outcomes (LEA-006); each kitchen position's ongoing-education hours (`policy.ongoing_education_hours.<position>`).
- What the person can do afterward: walk a green commis's readiness plan from day one to release and say who signs each step; name every `chef.*` binding the kitchen modules wait on and when each will be supplied.
- How it is proven: a conversation with Brandon on one cook's plan and the bindings list; the EC rates two recorded kitchen practicals with Brandon as co-rater. Prove-first: the plan walk-through taken cold; the session with Brandon on what the EC signs always runs, because it sets the split between them.
- Time and place: about 6 h (2 remote and paid, 4 on site with Brandon). Brandon to confirm.
- Waits on: the signed spine; D1 and D30 as Brandon applies them to the chef; `workflow.preopening_calendar`; the EC's hire.
- Absorbs: none (new; fills the people-system part of the EC's onboarding).

---

## 3. Administration

### ADM-101 The office day
- Area: administration
- Positions and timing: MD and OM, readiness (12 h; one shadowed and one led office day). Leads take the short version inside ADM-117.
- What it teaches:
  - The day's rhythm as a sequence, with the order bound (`workflow.office_day`):
    - read the overnight outputs: sales and labor dashboards, exceptions, deliveries due, repair tickets, unread correspondence, today's and tomorrow's book;
    - agree the day's handoffs between the pair;
    - clear exceptions before service;
    - protect booked check slots (LEA-101);
    - write the shift close at night (ADM-109, ADM-113).
  - The split (WP Part I "The management layer", cited): the OM answers for labor, cost, compliance, vendors and the facility; the MD for the room, the team's development, customer relationships and recovery. Each knows the other's dashboard well enough to cover a day off.
  - The OM oversees the systems and "is accountable to their outputs, not their manual production" (WP Part I, cited). There is no back-office administrator; cash, payroll, HR, compliance and vendor coordination run in software (WP Part II).
  - The failure to watch for (WP Part I, cited): one manager doing the other's work, or doing by hand what a system should do. The fix is restoring the split or fixing the system, not working longer.
  - Work belongs at the desk. Nothing administrative happens on a device during service (D8).
  - The weekly cadence: the weekly meeting; the post-launch review window for new modules (D14, `workflow.post_launch_review_window`); the schedule post (`workflow.schedule_post_day`).
- What the person can do afterward: run a full office day unaided, with every exception closed or assigned to a named owner, and hand off to the other manager in a note the other can act on without asking a question.
- How it is proven: a spoken check on the split and the failure modes; one office day shadowed, one led and reviewed with Brandon. Test-out: an experienced manager leads one office day on Sŏn's systems and passes the spoken check, saving the shadowed day. Nobody tests out of the house split.
- Time and place: 12 h (4 remote and paid, 8 on site across the two office days).
- Waits on: Brandon interview on what the pair must never hand to software and never do by hand; `workflow.office_day`; `people.schedule_owner`; the pair's remaining split (D1).
- Absorbs: the office half of LEA-028.

### ADM-102 Reading labor
- Area: administration
- Positions and timing: OM, readiness (4 h); MD and HB, ongoing.
- What it teaches:
  - Labor as an asset, not a cost (BG 01; WP Part II "Labor as asset, not cost", cited). Read the labor numbers for load and coverage first, cost second.
  - The parts of a labor read: scheduled hours against forecast demand; actual against scheduled; hours approaching overtime (none is the rule); breaks taken against the rule (`compliance.break_rule`); learning hours kept apart and never cut to make a number; the trainee extra to staffing (`workflow.angel_shift_staffing`).
  - Why a labor ratio lags, and what leads it (WP Part II leading indicators, cited; working definitions shared with ORI-023, to confirm against the white paper in Box):
    - Employee NPS: how likely each team member says they would be to recommend Sŏn as a place to work, asked in a short anonymous survey; read by the founders and managers as a team, never person by person.
    - Cultural labor score: the white paper's measure of whether the team's working conditions are holding up; the questions or counts it combines are read from WP Part II before drafting; read by the founders and the OM.
    - Who is going under on a full night (LEA-024).
  - The sign the team has no capacity left (WP Part I, cited: "bandwidth is at zero"): fix the design, not the hours. The fix removes friction (a step, a handoff, a tool fault), never adds hours.
  - Every target and threshold is a `fact.*` binding (unbound until a source is chosen (Airtable retired)). No number is recalled or estimated.
- What the person can do afterward: read a week's labor report aloud and name the one action it calls for, if any; say which part of a gap is demand, scheduling or execution; refuse a cut that removes learning time or the trainee's extra seat.
- How it is proven: a spoken check on three anonymized reports built from the bound targets (practice and check banks kept apart); recheck when the targets change. Test-out: the spoken check, for a manager with prior labor ownership.
- Time and place: 4 h (3 remote and paid, 1 on site).
- Waits on: `fact.labor_targets.*`; `tool.data.labor_dashboard` (source unbound until a source is chosen (Airtable retired)); `compliance.break_rule`; `founder.open_book_scope`.
- Absorbs: none (ORI-023 is the version for everyone).

### ADM-103 Reading cost, sales and the business
- Area: administration
- Positions and timing: OM, readiness (5 h); MD, HB and LB, ongoing.
- What it teaches:
  - The terms, with every house value bound: cost of goods (food and beverage); prime cost; theoretical against actual cost, and what the gap means; comps, voids and recovery spend as separate lines; waste, including what customers leave uneaten (WP Part II).
  - Lagging against leading indicators: revenue, labor and food cost lag; employee NPS and the cultural labor score (defined in ADM-102) and the customer recognition rate lead (WP Part II, cited). Customer recognition rate: how often a returning customer is recognized and served as known on a return visit, counted from the book (SYS-121); read by the MD and OM (working definition shared with ORI-023, to confirm in Box).
  - What moves each number and who can move it: a cost gap traced to receiving (ADM-105), to portioning (`chef.*`), or to pricing (Brandon).
  - The AI layer's read is a prompt, not a verdict; AI does analysis, never anything load-bearing (WP Part II).
  - Where numbers never go: blame on a person, or a cut to a learning hour.
- What the person can do afterward: explain a period's cost gap to Brandon in plain words, separate a real signal from a counting or receiving error, and bring one recommended action.
- How it is proven: a spoken check on a staged variance case; ongoing, a presentation of one real period to Brandon. Test-out: the spoken check, for an OM with prior P and L ownership.
- Time and place: 5 h (4 remote and paid, 1 on site).
- Waits on: `fact.cost_targets.*`; `tool.accounting.platform` (candidates Restaurant365, QuickBooks); Brandon interview on which numbers the pair act on without asking him.
- Absorbs: the shared method behind BEV-032.

### ADM-104 Building and running the schedule
- Area: administration
- Positions and timing: the schedule owner (`people.schedule_owner`), readiness. If the OM owns it, the OM window adds 7 h: ADM-104 6 plus SYS-134's tool steps 1, with one shared practical. The other manager learns to read and cover it, ongoing.
- What it teaches:
  - Scheduling against demand from the book's forecast (SYS-121) and the kitchen's production plan.
  - Coverage by position and skill: only people released on a skill count toward coverage, after a real full night (D10).
  - What the schedule protects: each position's weekly ongoing-education hours, paid and on the schedule (`policy.ongoing_education_hours.<position>`), so wine and other track study never drifts home unpaid (D41; 29 CFR 785.27 to 785.29, verified-primary); managers' booked check slots (`workflow.check_slots`); leads' paid assessing time outside service (D5); new hires' readiness hours, 40 a week with no overtime (D55); the trainee extra to staffing; the live-gate cap per service (`workflow.live_gate_limit`); a certified food protection manager on site during all hours of operation (25 TAC 228.31, verified-secondary; CMP-108).
  - Fair and predictable posting (`workflow.schedule_post_day`); availability, requests and swaps, and who approves a swap (`people.swap_approver`; swaps only to someone released on that position).
  - Overtime and break rules as compliance (`compliance.*`).
  - Schedules kept two years (29 CFR 516.6, verified-secondary).
  - The tool steps are SYS-134.
- What the person can do afterward: build a week's schedule that meets demand and every protection above, and show where each protection sits on it.
- How it is proven: one shared practical with SYS-134 (this module owns it): build a week from a set book and roster with three new hires in their window and two people on a track with ongoing-education hours, checked against a list, then entered in the tool (SYS-134's half); the first two live schedules co-reviewed by the other manager. Test-out: the practical alone. The protections are house rules and are never waived.
- Time and place: 6 h (3 remote and paid, 3 on site).
- Waits on: `people.schedule_owner`, `people.swap_approver`; `tool.scheduling.platform`; `workflow.schedule_post_day`, `workflow.check_slots`; `policy.ongoing_education_hours.<position>`; `compliance.break_rule`, `compliance.predictive_scheduling`.
- Absorbs: none.

### ADM-105 Ordering, receiving, inventory and variance
- Area: administration
- Positions and timing: OM and HB, readiness (6 h each); LB, readiness for the lead seat (bar part, 4 h, written with writer 3); KO, the kitchen part, inside KIT-041. Leads who order (`people.ordering_roles`), readiness.
- What it teaches:
  - The cycle: par and reorder logic; the forecast from the book; the order; the delivery window; receiving; storage and rotation; the count; variance.
  - Receiving: quantity, quality, temperature where it applies, and substitutions checked against the order before signing; shorts and damage noted on the invoice; the credit requested the same day.
  - Counts: when, by whom, the method, a second counter on high-value product (`workflow.count_method`).
  - Variance and its causes, told apart: count error, receiving error, waste, comps, over-pouring, loss, the wrong recipe in the system. Investigate before concluding.
  - Bar part (LB): bar pars and the order cycle for spirits, wine, mixers and garnish; counting open bottles and partials (`workflow.partial_method`); transfers between bar and kitchen recorded; batch yields against what was poured.
  - The tool steps are SYS-136.
- What the person can do afterward: place an order from the system; receive a delivery and catch a short or a substitution; run a count another counter would match; explain a variance with evidence.
- How it is proven: practical receiving of a staged delivery with planted errors; a blind double count of one section; a spoken check on one variance. Test-out: the staged receiving and count practicals.
- Time and place: OM and HB 6 h (2 remote and paid, 4 on site); LB 4 h (1 remote and paid, 3 on site).
- Waits on: `tool.inventory.platform`, `tool.purchasing.platform` (candidate Restaurant365); `workflow.count_method`, `workflow.partial_method`; `fact.par_levels.*`, `fact.count_tolerance`; `chef.receiving` for kitchen product; the storage layout (D58).
- Absorbs: the floor and bar half of KIT-015; BEV-032's inventory inputs; the variance content of the systems draft's SYS-128 to SYS-130.

### ADM-106 Payroll handoffs and time records
- Area: administration
- Positions and timing: OM, readiness (4 h). MD covers approvals on the OM's day off (ongoing). Leads learn only what to escalate (ADM-117).
- What it teaches:
  - The handoffs: time records reviewed and approved before the payroll cutoff (`workflow.payroll_cutoff`); missed punches corrected with the employee's confirmation, never silently; rate and role changes entered only on Brandon's approval (`people.*`); new hire and exit data; final pay timing (`compliance.final_pay`).
  - The never-do list: editing time without the employee knowing; recording training as unpaid (D41; 29 CFR 785.27 to 785.29, verified-primary); scheduling learning into overtime.
  - Records kept three years for payroll and two for time cards (29 CFR 516.5 and 516.6, verified-secondary).
  - How the team is paid is set in WP Part II ("How the team is paid", cited); explaining pay uses the transparency sheet (`founder.transparency_sheet`), never a recalled number.
  - The tool steps are SYS-133.
- What the person can do afterward: close a pay period's approvals correctly and on time; fix a missed punch with a record the employee confirmed; answer "why is my check different" by finding the record.
- How it is proven: a practical on a staged pay period with planted errors (a missed punch, unapproved overtime, an unpaid training block); a spoken check on the never-do list. No test-out on the never-do list (compliance); the mechanics test out by the practical.
- Time and place: 4 h (2 remote and paid, 2 on site).
- Waits on: `tool.payroll.platform` (candidate Rippling); `workflow.payroll_cutoff`; `compliance.final_pay`; `founder.transparency_sheet`; HR seats review.
- Absorbs: none.

### ADM-108 Hiring paperwork and onboarding before the first shift
- Area: administration
- Positions and timing: OM, readiness (3 h); MD, ongoing cover.
- What it teaches:
  - The sequence, with steps bound (`workflow.onboarding`): offer and acceptance; employment eligibility, with Form I-9 Section 2 completed within three business days of the first day of work for pay (USCIS, verified-secondary); tax and payroll setup; policy acknowledgements (CMP-106); the food handler certificate within the legal window or the house rule (CMP-101, `founder.compliance_timing`); TABC certification for alcohol roles (CMP-102).
  - Before the first shift (WP Part II "Onboarding", cited): the mentor connected (D21); locker, uniform and tools ready; the remote hours assigned and paid; the readiness plan built (LEA-103).
  - Why comes before how.
  - Every certificate tracked per person (CMP-109).
- What the person can do afterward: take a hire from offer to first shift with every legal record complete on time and everything ready when the person arrives.
- How it is proven: a checklist audit of a staged new hire with planted gaps. No test-out on the legal steps.
- Time and place: 3 h (2 remote and paid, 1 on site).
- Waits on: `tool.payroll.platform` and HR; `tool.lms.*` assignment; `workflow.onboarding`; `founder.compliance_timing`; HR seats.
- Absorbs: the enrollment half of SAF-002.

### ADM-109 The documentation standard
- Area: administration
- Positions and timing: MD, OM and every lead (LH, LFR, LS, LB), readiness (3 h). The everyone version is SYS-101.
- What it teaches:
  - Knowledge lives in the system, not in people; an incident handled but not documented happens again (WP Part I failure modes, cited).
  - The record types, each with one home: the shift close; the incident record; repair tickets; customer notes (SYS-112); coaching and gate records (D8); decision notes from the nightly review (LEA-046); vendor issues.
  - The writing standard: facts before judgment; who, what, when, where, and what was done; no adjectives about a person; written once, where it belongs, at close and never during service (D8).
  - What never goes in writing: a customer's private information outside the policy (`founder.customer_data_policy`); speculation about a person; profanity.
  - Retention and access (`compliance.records_retention`).
- What the person can do afterward: write a shift close and an incident note that a manager who was not there can act on without calling anyone.
- How it is proven: a written practical on two staged nights, reviewed against the standard; a spot recheck of real closes in the first month. Test-out: the written practical.
- Time and place: 3 h (2 remote and paid, 1 on site).
- Waits on: `tool.ops_log.platform`; `founder.customer_data_policy` (D50); `compliance.records_retention`.
- Absorbs: the documentation half of LEA-046.

### ADM-110 Incident records and the duty to report
- Area: administration (the reporting duties are named as compliance, D57)
- Positions and timing: MD and OM, readiness (4 h). Leads take the first-response part inside ADM-117.
- What it teaches:
  - Incident types and first moves: a customer injury or illness; an allergic reaction; an employee injury; an alcohol incident; a property or security incident; a harassment or discrimination complaint.
  - Care for the person first, the record second (SAF-006 for the first minute).
  - Who is notified, by role, in order (`workflow.incident_escalation`).
  - The record: facts, witnesses, times, actions, the follow-up owner.
  - Legal reporting: every employer reports a work-related fatality, in-patient hospitalization, amputation or loss of an eye to OSHA (29 CFR 1904, verified-secondary); the windows are bound (`compliance.osha_report_window`, lead-only). Full-service restaurants are partly exempt from routine injury logs unless asked in writing (verified-secondary). Insurance and workers' compensation handoffs are `compliance.*`.
  - Harassment complaints route to the HR seat, never to the incident review.
  - The record feeds the private review (LEA-021) and is never mixed with open everyday feedback (D22).
- What the person can do afterward: handle a staged incident from first response to a complete record and the right notifications, and route a complaint to the right place.
- How it is proven: a decision-point practical across four incident types; a spoken check on the reporting duties; recheck on `workflow.recheck_cadence`. No test-out: safety and legal duty.
- Time and place: 4 h (2 remote and paid, 2 on site).
- Waits on: `workflow.incident_escalation`; `compliance.osha_report_window`, `compliance.insurance_reporting`; `founder.incident_policy`; HR seats; `tool.ops_log.platform`.
- Absorbs: the record side of SAF-005.

### ADM-111 Vendor relations
- Area: administration
- Positions and timing: OM, HB and MD, ongoing.
- What it teaches:
  - The vendor as a partner in the standard: specs in writing; quality issues raised the same day with evidence; credits tracked to closure.
  - Delivery windows set around service and the team's load.
  - Producer relationships whose stories the floor can tell, verified by the producer (feeds MNU-003 and the beverage tracks).
  - Negotiation at a principle level; terms are `fact.*`.
  - Gifts and samples (`founder.vendor_gifts_policy`).
  - When to change a vendor, and who decides: Brandon on core product, the chef on kitchen product (`chef.*`), the HB on beverage.
  - Vendor performance is part of the OM's accountability (WP Part I, cited).
- What the person can do afterward: raise and close a quality issue with a vendor in writing, and explain any vendor's standing from the record.
- How it is proven: a written practical on a staged quality issue; ongoing, a vendor review presented to Brandon. Test-out: the written practical.
- Time and place: 1.5 h remote and paid; review time on site after.
- Waits on: `founder.vendor_gifts_policy`; the vendor list; `tool.purchasing.platform`.
- Absorbs: none.

### ADM-112 Facility, maintenance and repair
- Area: administration
- Positions and timing: OM, readiness (2 h). Leads report through ADM-117; everyone reports through SYS-101. The tool is SYS-142.
- What it teaches:
  - Triage: safety first, then service impact, then cosmetic.
  - The preventive maintenance calendar (`workflow.pm_calendar`).
  - Pest control and waste service records.
  - Kitchen equipment is the chef's call (`chef.*`).
  - The facility is held to the room's standard, not to "working."
  - Placeholders for the space's systems until it exists (D58).
- What the person can do afterward: log, triage and close repairs, and keep the maintenance calendar current.
- How it is proven: a walk-through with planted faults and spoken triage. Test-out: the walk-through.
- Time and place: 2 h (1 remote and paid, 1 on site).
- Waits on: `tool.maintenance.platform` (candidate ResQ); `workflow.pm_calendar`; the space (D58).
- Absorbs: none.

### ADM-113 Closing the day
- Area: administration
- Positions and timing: MD and OM, readiness (3 h). Closing leads only if `people.close_roles` includes them: the lead's close version, 2 h, readiness for the lead seat (the cash count and deposit steps stay with managers); SYS-131's POS steps (2 h) count in writer 1's file.
- What it teaches:
  - The end-of-day sequence (`workflow.day_close`): open checks closed; voids, comps and recovery entries reviewed against who approved them; payments reconciled; cash counted with two people where cash exists; deposits recorded; the shift close written.
  - An unexplained difference is recorded and escalated, never absorbed.
  - The POS steps are SYS-131.
  - Lead's close version: open checks closed; voids, comps and recovery entries checked against who approved them; differences recorded and handed to the manager in the close note (ADM-109). No cash count or deposit.
- What the person can do afterward: close a day with every difference explained or escalated.
- How it is proven: a practical close on a staged day with planted differences, done twice. Test-out: one clean staged close on Sŏn's POS.
- Time and place: 3 h (1 remote and paid, 2 on site); lead's close version 2 h (0.5 remote and paid, 1.5 on site).
- Waits on: `tool.pos.platform` (candidate Toast; the POS spine is open, WP Part II); `tool.cash_handling`; `workflow.day_close`; `people.close_roles`.
- Absorbs: none.

### ADM-114 After the visit: correspondence, reviews and the loop
- Area: administration
- Positions and timing: MD, ongoing; LH by delegation, ongoing.
- What it teaches:
  - Reading and answering correspondence and public reviews in the house register (BG 11 "Register matrix", correspondence; the digital touchpoint hierarchy, cited).
  - What goes back into the customer record (SYS-112).
  - When a reply moves to a call.
  - Turning a pattern into one teaching point for pre-shift.
- What the person can do afterward: answer a hard review and a request in writing to the house standard, and log what changes.
- How it is proven: written practicals reviewed by Brandon. Prove-first: the written practicals taken cold after reading the register.
- Time and place: 2 h remote and paid, then ongoing.
- Waits on: `tool.reputation.platform`; `founder.public_reply_policy`; `brand.*` register.
- Absorbs: the written half of SVC-062.

### ADM-115 Reading the system's outputs and acting on exceptions
- Area: administration
- Positions and timing: OM, readiness (3 h); HB, readiness (2 h, the beverage dashboards); MD, ongoing.
- What it teaches:
  - The model (WP Part II, cited): software does the reliable, scheduled, auditable work; managers oversee its outputs; AI reads across the hub and is never load-bearing.
  - Each dashboard: what normal looks like and which exceptions need action (a sensor alarm, a missed delivery, a labor overrun, a profile merge conflict, an unbooked check-slot link).
  - Act, watch or ignore; a system fault against an operational fault.
  - The paper or manual fallback for each critical function (`workflow.fallback.*`).
  - Feeding tool problems into the feedback channel so the loop closes.
- What the person can do afterward: sort a set of staged dashboard states into act, watch and ignore, and act correctly.
- How it is proven: a spoken check on staged states; a fallback drill on site. Test-out: the spoken check. The fallback drill never tests out.
- Time and place: OM 3 h (2 remote and paid, 1 drill on site); HB 2 h.
- Waits on: `tool.data.*`; `workflow.fallback.*`.
- Absorbs: none.

### ADM-117 The lead's administrative duties
- Area: administration
- Positions and timing: every lead (LH, LFR, LS, LB), readiness for the lead seat (2.5 h).
- What it teaches:
  - The lead's close note (to ADM-109's standard).
  - Opening and closing sign-offs for the station (`workflow.*`, D58).
  - Reporting repairs (ADM-112, SYS-142).
  - Helping with counts (ADM-105).
  - First response and handoff on an incident: care for the person, the manager called, the facts noted (ADM-110).
  - Covering a swap by the rules (SYS-104).
  - Where a lead's authority stops: no pay, no time edits, no discipline (D5). Those go to a manager.
- What the person can do afterward: write a close a manager can act on, and say which calls are theirs and which go up.
- How it is proven: a written close practical and a spoken check on scope. Test-out: the same checks.
- Time and place: 2.5 h (1.5 remote and paid, 1 on site).
- Waits on: the HR ruling on hourly leads (D5); `workflow.*` per station.
- Absorbs: LEA-009 (the scope card).

### ADM-118 Events and private bookings
- Status: identified, parked on Brandon's events answer (does Sŏn take private dining, buyouts or events, and in which dayparts). The single events ID across the files: it replaces SVC-102 and the house file's events proposal. Content is drafted so it can be populated the day the answer comes.
- Area: administration (with a floor part and a host part)
- Positions and timing: MD and OM, the office part, before the first event is booked; LH and the host team, the host part; the floor (FR, BW, FS, LS) and the bar on the night, the floor part, before working a first event; KO and the chef for the kitchen's part (`chef.event_menus`). Ongoing education, not readiness, unless events run from opening.
- What it teaches:
  - Office part (MD, OM): the path from inquiry to follow-up: the inquiry routed (`workflow.events_routing`); what is offered and what is not (`founder.events_policy`); the deposit, minimum and cancellation terms as `fact.*` values, never recalled; the menu set with the chef (`chef.event_menus`); staffing built for the event without breaking any schedule protection (ADM-104); the event sheet, and what it must hold (the host's contact person, the timeline, the menu, every allergy and need, who speaks for the house on the night, the bar plan); the day itself; the follow-up and the record (ADM-114, SYS-112).
  - Host part (LH, host team): routing an inquiry and never quoting terms (SYS-114, SVC-062); entering the event in the book (`tool.reservations.events`); collecting allergies and needs ahead and confirming them at the door (SAF-001).
  - Floor part (from the service file's SVC-102 content): the event briefing at pre-shift (the fixed menu, the timeline, the host's contact person, who speaks for the house); allergies and needs collected ahead and confirmed at the door (SAF-001); serving a fixed menu in sequence across a large table (SVC-019, SVC-035); holding service around toasts and speeches; who at the event can change the plan, and who on the floor can agree to it.
- What the person can do afterward: office part: take a staged inquiry to a complete event sheet that the chef, the floor and the bar can each work from without a question; host part: route and book an event correctly; floor part: work an event to its sheet, including a change asked for mid-event.
- How it is proven: office part: a staged inquiry to a finished event sheet, reviewed by Brandon; host part: a role-played inquiry; floor part: a briefing role-play and the first event worked under a lead's observation. Prove-first: each part's proof taken cold. The allergy confirmation is observed on every attempt and never tests out.
- Time and place: design estimates, set when unparked: office part about 3 h (2 remote and paid, 1 on site); host part about 1 h on site; floor part about 1.5 h on site, paid.
- Waits on: Brandon's events answer; `founder.events_policy`; `fact.*` event terms; `chef.event_menus`; `workflow.events_routing`; `tool.reservations.events`; the space (D58).
- Absorbs: SVC-102; the house file's events proposal.

### LEA-032 Interviewing together
- Area: administration (hiring with the pair)
- Positions and timing: MD and OM, ongoing, before their first interview. Leads observe and later interview.
- What it teaches:
  - The white paper hiring system (WP Part II "Talent acquisition", cited): candidates self-schedule and choose language and format; they are told what to expect at each step; "no one is ghosted," including at the no.
  - Structured interviews with documented questions and a shared rating scale per position; structured interviews predict best (Sackett 2022, verified-secondary).
  - Each interviewer rates independently before the pair compare; disagreements are discussed, not averaged away.
  - What to read for: competencies, cultural alignment, growth potential, and whether the house can give this person what they need.
  - Lawful questions (`compliance.interview_questions`).
  - The transparency sheet given at the first interview (`founder.transparency_sheet`): the org chart, the direct lead, compensation and benefits (`fact.*`), communication expectations, the training plan with pay dates, the advancement path.
  - Internal moves and the ready-now pool first, where they fit (WP Part I).
  - The tool steps are SYS-135.
- What the person can do afterward: run a paired interview from the guide, rate independently, reach a documented decision and close the loop with every candidate.
- How it is proven: a recorded mock interview with a calibrated rating; the first two real interviews co-rated with Brandon. Prove-first: the mock interview taken cold; the two co-rated real interviews run for everyone, because they calibrate on the house's scale.
- Time and place: 6 h (3 remote and paid, 3 on site).
- Waits on: per-position interview guides (Brandon interview); `compliance.interview_questions`; `founder.transparency_sheet`; `tool.recruiting.platform` (candidate Greenhouse).
- Absorbs: LEA-032; the door variant (what to look for in a host).

### LEA-033 Running the paid practical interview
- Area: administration (hiring with the pair)
- Positions and timing: MD, OM and HB (bar candidates), ongoing, before running one. Kitchen variant: KO and EC for cooks and porters.
- What it teaches:
  - The paid practical replaces the unpaid tryout (WP Part II, cited). It is on the clock, and the candidate is told the tasks in advance. Unpaid working interviews have been found to violate the FLSA (US DOL, reported by HR Dive 2018, verified-secondary, carried).
  - The procedure is fixed before anyone is judged: same tasks, same scale, two raters.
  - It is an audition, never a shift that covers labor.
  - Hiring evidence is kept apart from training sign-off.
  - The leadership final round is dinner in the room (WP Part II).
  - Kitchen variant: tasks set by the executive chef (`chef.practical_interview_tasks`), the candidate's choice of language and format (WP p.17).
- What the person can do afterward: set up, run and rate a paid practical that a second rater would score the same way.
- How it is proven: co-run one practical; run one with a co-rater whose ratings are compared. HR confirms compliance. Prove-first: an experienced manager runs the first one with the co-rater, skipping the co-run.
- Time and place: 2 h remote and paid, plus the first live run.
- Waits on: per-position practical tasks (Brandon, HB, the chef); `fact.practical_interview_pay`; `compliance.*` review.
- Absorbs: LEA-033; KIT-052 (draft LEA-174).

### BEV-032 Program economics
- Area: administration (with beverage)
- Positions and timing: HB, ongoing; LB elective.
- What it teaches:
  - Pour cost, waste and yield as decision inputs, read with ADM-103's method; every value `fact.*`.
  - Where a beverage number moves: the spec, the pour (BEV-002), batch yield, comps and gifted pours (`founder.gifted_pour_range`), breakage, the order.
  - Pricing is Brandon's; the HB brings the evidence.
  - Feeding the list decision with what customers actually choose (SYS-122, MNU-101).
- What the person can do afterward: present one beverage decision (keep, change, drop) with the inputs behind it.
- How it is proven: a presentation to Brandon and the OM. Prove-first: the presentation without the sessions.
- Time and place: 4 h (2 remote and paid, 2 on site).
- Waits on: `fact.*` (unbound until a source is chosen (Airtable retired)); `founder.gifted_pour_range`; the inventory tool (SYS-136).
- Absorbs: BEV-032 (the inventory tool side went to SYS-136; reconciliation sits in ADM-105).

### KIT-041 Kitchen production and operations
- Area: administration (chef-led)
- Positions and timing: KO, readiness (4 h); CDC and EC, ongoing.
- What it teaches:
  - From forecast to prep plan: the book's forecast (SYS-121), events and large parties into the prep list (KIT-020, SYS-141).
  - Ordering to par, receiving and counts for kitchen product (ADM-105's kitchen part; SYS-136).
  - Labor inside policy and with no overtime (`policy.overtime`); building the kitchen schedule (ADM-104, SYS-134).
  - Maintenance and equipment records (ADM-112).
  - Waste and yield review (KIT-033, SYS-140).
  - Every figure comes from the tool (`fact.*`; unbound until a source is chosen (Airtable retired)) and none is estimated. Why the role exists: "The Executive Chef is placing linen orders" (WP p.13, cited).
- What the person can do afterward: run a full production cycle (forecast, order, receive, prep, count, review) without the executive chef doing clerical work.
- How it is proven: an observed production cycle and a conversation on the decisions made. Test-out: an experienced sous chef runs one cycle in the house tools.
- Time and place: 4 h (2 remote and paid, 2 on site); then live cycles.
- Waits on: `tool.inventory.*`, `tool.kitchen.prep_planning`, `tool.scheduling.platform`; `workflow.ordering`; `policy.overtime`; `fact.*`; the chef.
- Absorbs: KIT-041 (the tool half went to SYS-136 and SYS-141).

---

## 4. Readiness hours from these modules, by position

Readiness hours only (R, or the R part of R/O), from this file's modules. Supervised and observed shifts, CMP-103's supervisor version, SYS-142 and other writers' modules are counted in the spine, not here. Parked and "chef to define" modules (LEA-004, LEA-036, KIT-040, KIT-042, KIT-043, ADM-118) carry no hours.

| Position | Modules and hours | Total |
|---|---|---|
| FR | KIT-002 floor side 2 | 2 |
| LH | LEA-001 3, LEA-018 1.5, LEA-005 host part 1, ADM-117 2.5, ADM-109 3 | 11 (13 if a closing lead, with ADM-113 lead version 2) |
| LFR | LEA-011 3, LEA-001 3, LEA-018 1.5, KIT-002 expo 1, ADM-117 2.5, ADM-109 3 | 14 |
| LS | LEA-024 2, LEA-001 3, LEA-018 1.5, ADM-117 2.5, ADM-109 3 | 12 (14 if a closing lead, with ADM-113 lead version 2; SYS-131 2 more in writer 1's count) |
| LB | LEA-011 3, LEA-001 3, LEA-018 1.5, LEA-005 bar part 1, ADM-117 2.5, ADM-109 3, ADM-105 bar 4 | 18 |
| HB | LEA-002 6, LEA-014 2.5 (in the window because the HB signs every bar practical and spoken check from opening), ADM-105 6, ADM-115 2 | 16.5 |
| MD | LEA-028 2, LEA-029 3, LEA-005 2, LEA-027 1.5, LEA-010 1, LEA-016 1.5, LEA-103 2, LEA-024 2, ADM-101 12, ADM-109 3, ADM-110 4, ADM-113 3 | 37 (plus 17.5 in the first month: LEA-101 3, LEA-002 6, LEA-014 2.5, LEA-102 3, LEA-001 3) |
| OM | LEA-028 2, LEA-010 1, LEA-027 1.5, ADM-101 12, ADM-102 4, ADM-103 5, ADM-105 6, ADM-106 4, ADM-108 3, ADM-109 3, ADM-110 4, ADM-112 2, ADM-113 3, ADM-115 3 | 53.5 (59.5 if schedule owner with ADM-104 6, plus SYS-134 1 in writer 1's count; plus 20 in the first month: LEA-101 3, LEA-002 6, LEA-014 2.5, LEA-102 3, LEA-005 2, LEA-016 1.5, LEA-103 2) |
| P | KIT-102 2, KIT-101 1, KIT-016 2, SAF-013 1, KIT-010 6, KIT-015 3 (KIT-104 inside paired shifts) | 15 |
| C | KIT-102 2, KIT-101 2, KIT-016 2, SAF-013 3, KIT-012 10, KIT-013 4.5, KIT-015 2, KIT-020 3, KIT-021 3, KIT-022 2 | 33.5 |
| CDP, internal from C | KIT-002 2, KIT-023.x 16, KIT-024 4, KIT-103 1 (only once two dayparts run) | 23 (22 with KIT-103 parked) |
| CDP, experienced external | Block K culinary 9, the commis set by prove-first (KIT-012, KIT-013, KIT-021, KIT-022), KIT-002 2, KIT-023.x 16, KIT-024 4, KIT-103 1 | 32 plus prove-first attempts |
| CT, internal | KIT-031 2 and LEA-105 3 on the first move, KIT-023.x 16 per added station | 21, then 16 per station |
| KO, KS, CDC | Block K culinary 9, LEA-027 1.5, LEA-104 4, LEA-105 3, the KIT-023.x walk 16; KO adds KIT-041 4. LEA-103 (2) before the first cook's start date | 33.5 (KO 37.5) |
| EC | LEA-106 about 6 and LEA-002 kitchen part, inside onboarding | not a window |

Block K culinary 9 is KIT-102 2, KIT-101 2, KIT-016 2 and SAF-013 3. CMP-110, CMP-111, SYS-139 and SYS-140 complete Block K and are writer 1's.

## 5. Spine changes needed

From the 2026-10-01 red team, for the spine (sections 2, 3, 5.5 to 5.7, 5.10) and the placement map:

1. **MD window (2.2).** LEA-001 moves to the first month with LEA-101 (first-month total 17.5 h). LEA-024 (2) is MD readiness and must be counted: the MD runs the floor solo from release, and reading who is going under is part of that. From this file the MD's readiness is 37 h. Supervised and observed services at shift length, CMP-103 supervisor (+1) and SYS-142 (1) are also uncounted; the red team's corrected MD is about 140 h, about 125 h after its fixes. Brandon to decide whether D55 applies to the manager pair or a four-week manager standard is set.
2. **OM window (2.2) and the table rows for LEA-005, LEA-016 and LEA-103.** All three are OM first month, not OM readiness (about 5.5 h), in the spine table, 2.2 and the placement map. OM first-month total 20 h. The schedule add is 7 h (ADM-104 6 plus SYS-134 1, one shared practical owned by ADM-104), not "about 6".
3. **HB (2.3).** Keep LEA-002 (6) and LEA-014 (2.5) in the HB window and state the reason in the spine: at opening the HB signs every bar practical and spoken check, so calibration cannot wait for the first month as it does for the MD and OM.
4. **Leads (2.2, 2.3).** LS closing lead: ADM-113 lead version 2 plus SYS-131 2 is 4 h, not 3 (cash and deposit stay with managers). LH takes the same 2 h if `people.close_roles` includes the lead host. Add CMP-103 supervisor (+1) and SYS-142 (1) to every lead window, and count observed lead shifts at shift length.
5. **Kitchen (2.4).**
   - Count LEA-105 (3) in the CT and KO, KS, CDC windows; LEA-103 (2) for the kitchen pair before the first cook's start date; CMP-103 supervisor (+1) for every kitchen leader.
   - Define cook release as solo on a station on a named non-peak service (`workflow.kitchen.nonpeak_service`), with KIT-030 closing peak nights after the window.
   - Flag to the chef: 16 h per station and the paired-service unit (4 h in the spine; about 6 h at shift length) look optimistic for this standard; the chef resets both.
   - SYS-133: KO takes it in full (3 h); KS and CDC take only the timecard-approval part (1 h) if named in `people.timecard_approvers`. Align 2.4 with the house file.
   - KIT-013 rises to 4.5 h (the chef's own food-safety controls moved from CMP-110); C window 33.5 from this file. Check CMP-110's hours for the matching reduction.
   - KIT-103: use the single D24 statement (training covers every daypart's register; which dayparts run at opening is `workflow.daypart_schedule`; content for a daypart not running is built and parked). KIT-103 is parked until two dayparts run.
   - EC onboarding: add LEA-106 (about 6 h, with Brandon).
6. **Module list changes (5.6, 5.7, 5.10, and the placement map's outcomes and counts).**
   - LEA-047 merged into LEA-007, retitled "Taking critique and repairing a lapse in front of the team" (1.5 h). Placement map: LEA-047 "Merged into LEA-007".
   - LEA-036 parked until the D14 panel exists; its explaining part folded into LEA-037. LEA-004 parked with SYS-144 until Brandon opens authoring. Both leave the module count.
   - KIT-040, KIT-042, KIT-043: "identified, chef to define", no hours. KIT-043's library mechanics folded into LEA-037's kitchen part.
   - LEA-101 retitled "Running booked check slots"; it now carries CUL-023's recheck cadence (with LEA-102) and the assessor-hours count against `workflow.live_gate_limit`.
   - LEA-006 names its four outcomes (learning opened, a move opened, reserve, not now with a reason and a reopen trigger; Brandon to confirm) and carries CUL-024 as the `workflow.recommitment` step.
   - New: LEA-106 (5.6). ADM-118 is the single events ID (5.10, identified, parked on Brandon's events answer), with office, host and floor parts; it closes open item 10 and replaces SVC-102 and the house file's proposal.
7. **Program rules carried in these modules, for the spine to state once.** Prove-first for every non-safety module (LEA-104 is held as a safety module for people; ADM-106's never-do list, ADM-108's legal steps and ADM-110 stay no test-out). Supervised and observed services counted at shift length. Retry room: two-week routes planned to about 72 h and three-week routes to about 100 h (LEA-103). Weekly ongoing-education hours (`policy.ongoing_education_hours.<position>`) placed on the schedule by ADM-104 and SYS-134 and tracked by LEA-102. A pre-opening calendar (`workflow.preopening_calendar`) with managers at least four weeks before line staff and the HB at least two weeks before bar staff, and assessor hours per cohort counted against `workflow.live_gate_limit` (LEA-101).
8. **CMP-108** becomes a hiring requirement for MD, OM, HB, KO, KS, CDC and EC, or carries a dated post-hire deadline with `workflow.cfpm_coverage` (ADM-104 already protects a certified person on every hour).
9. **Plain terms.** "Talent blocks" become booked check slots (`workflow.check_slots`) and "eyes-off" becomes unsupervised shifts after sign-off in every row this file owns; `workflow.talent_block` is replaced by `workflow.check_slots`.
10. **KIT-034** stays ongoing; calling a refire at readiness is inside KIT-002. **KIT-003** sits with writer 2; this file supplies its chef content: modifications the kitchen can and cannot make (`chef.modification_policy`), honest times, early 86s, fire when the table is ready, kitchen visits set in the book before service. **Kitchen hours** are every one the chef's to reset; titles wait on INT C17.

## 6. What could not be made specific, and who supplies it

- **The chef** (every culinary module): titles; the station list and each station's items, holds and plates (KIT-023.x); station hours, paired-shift length and the named non-peak service for cook release; recipes and their reasons, the recipe format and codification rules (KIT-021, KIT-043); the cut list and drill product (KIT-012); taste references (KIT-022); the line check, mise maps and the house food-safety rules (KIT-013); porter priority and ware returns (KIT-010); the allergen matrix, cross-contact controls and marking (SAF-013); refire rules (KIT-034); who expos and the pass standard (KIT-040); R&D method (KIT-042); the call lexicon (KIT-002, KIT-016); the kitchen's pre-shift part (KIT-045); anchors for kitchen practicals (LEA-002); practical interview tasks (LEA-033); event menus (ADM-118).
- **Brandon's interviews** (D45): what the pair must never hand to software (ADM-101); which numbers the pair act on without asking (ADM-103); how he reads a team's load (LEA-024); the MD's step-in cues (LEA-029); the decision order (LEA-027); per-position interview guides (LEA-032); "teaching a new cook" (LEA-001, LEA-105); "a correction that worked, and one that did not" and "what you will not carry" (KIT-102, LEA-104); the four unblock outcomes (LEA-006); the watchlist as he confirms it (LEA-023); the EC split (LEA-106).
- **Policies** (D50): incident policy (LEA-021, ADM-110); regulars and customer data (LEA-041, ADM-109); vendor gifts (ADM-111); public replies (ADM-114); inspection (LEA-045); mentor criteria (LEA-015); the fail-limit shape (LEA-016, LEA-017); transparency sheet (ADM-106, LEA-032); gifted-pour range (BEV-032); events (ADM-118); recommitment format (LEA-006); ongoing-education hours per position (ADM-104, LEA-102, LEA-103).
- **People decisions:** schedule owner, swap approver, close roles, ordering roles, timecard approvers (ADM-104, ADM-105, ADM-113, SYS-133); the pair's remaining split (ADM-101, LEA-028); the HR ruling on hourly leads rating practicals (D5), which gates LEA-002, LEA-014, LEA-018 and ADM-117's scope; whether D55 applies to the manager pair.
- **Figures:** every labor, cost, par, pay, tolerance and event term is `fact.*` (unbound until a source is chosen (Airtable retired)).
- **Definitions to confirm in Box:** employee NPS, cultural labor score and customer recognition rate (WP Part II), worded here as working definitions shared with ORI-023.
