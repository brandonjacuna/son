<!-- Phase 2 working output, 2026-09-28. Research on video game skill trees and skill webs, to shape the structure and visual of Sŏn's program (system-design D3, D12, D28). Raw agent return, not reviewed line by line. -->

# Game skill trees and skill webs, and what Sŏn should take from them

## Method and confidence

- **Brief.** Brandon's intake group 2 (training should feel like the skill trees of a AAA game such as Horizon: several stacks leaning into different playstyles; master one, several, or all) and `framework/system-design.md` D3, D12, D28 (disciplines, not roles; roles are sets of disciplines at depths; Brandon prefers a constellation or skill web over a tree).
- **Sources.** Designers' own words where reachable (GDC abstracts, developer interviews, official game pages, a developer blog), then respected design writers (Sid Meier's GDC talk as reported, David Sirlin, Daniel Cook, Nicolas Kraj at GDKeys, Stanislav Costiuc), then reviews and wikis for mechanics, then forum threads for player sentiment only.
- **Labels.** **VP** verified-primary: read on the designer's, studio's or publisher's own page, or a direct quote in a named interview I opened. **VS** verified-secondary: read in independent coverage or a reference work I opened. **LO** lead-only: seen in a search result or snippet, not opened, or opened and the page did not carry it. **UV** unverified: my own recollection or inference.
- **Access limits.** Several key pages refused fetches (PC Gamer, GameSpot, UESP, Fandom wikis, Bungie.net article body, the Famitsu FFX interview translation, a Khan Academy help thread). Where a claim rests on those, it is marked LO. GDC Vault talks were read as abstracts only; no talk video was watched.
- **Numbers.** Game node counts and costs appear only where they explain a design; none is offered as a standard for Sŏn. Node counts on official pages and wikis disagree (Path of Exile's own planner and Wikipedia give different totals), which is itself a lesson: huge webs change every season.

---

## 1. The examples

### 1.1 Horizon Zero Dawn and Horizon Forbidden West (Brandon's reference)

**Structure.**
- Zero Dawn: three trees named for playstyles, Prowler (stealth), Brave (direct combat), Forager (support, health, resources) (LO, consistent across several guides). Small enough that a thorough player fills most of it (UV).
- Forbidden West: the old tree was "completely thrown out the window," in director Mathijs de Jonge's words; the new one "is designed to support many different play styles, and each play style has Valor Surges that you can unlock" (VP, de Jonge to Game Informer and GamingBolt, 2021-06-03). Six trees: Warrior (spear and melee), Trapper, Hunter (ranged, the largest), Survivor (healing), Infiltrator (stealth), Machine Master (overriding machines) (VS, Gfinity).
- **Valor Surges:** each tree carries three; a surge is a powerful temporary ability you select and charge by playing well, not by waiting. The bar fills from "tactical" play: headshots, knocking components off machines (VP, Game Informer). You must unlock the connected skills before the surge (VS, Gfinity).
- **Weapon techniques:** active moves per weapon type bought in the trees and fired with stamina (LO).

**Visual.** Tabs across the top, one per playstyle; each tab a branching tree flowing out from a root; the surge sits as a large node inside its tree (UV from memory of the UI).

**Praise and criticism.**
- Praised: the playstyle framing is legible at a glance; you know what "being a Trapper" means before you spend anything (UV, common in reviews).
- Criticized as padded: players describe "1 to 2 too many skill branches," and more than half the nodes as "tiny passive buffs" (VS for the thread's content, ResetEra "worst skill trees" thread; player sentiment, not critics). Points arrive faster than meaningful things to spend them on (LO).

**Lesson for Sŏn.** Take the named playstyle stacks and the "signature move" at the end of each stack (the surge maps to the integrated performance a discipline builds toward). Do not take the filler between them.

### 1.2 Path of Exile: one vast shared web, many doors

**Structure.** One passive web shared by every class; each class starts at a different spot on it, aligned to its attributes; the Scion starts in the middle, touching all three (VS, Wikipedia; VP, the official planner page lists the seven classes at different positions). Three node grades: small passives, **Notables** (named, larger, significant), and **Keystones** that "fundamentally change the way a character is played by altering the game rules" (VP, pathofexile.com planner).

**Visual and readability.** The official planner offers zoom, full screen, **search with highlight of matching nodes and shortest paths**, and a shareable link to a planned tree (VP). The community built a separate planner (Path of Building) and a build-statistics site (poe.ninja) that shows which trees top players run and lets anyone copy one (VS, poe.ninja and guides about it).

**Praise and criticism.**
- Praised for depth and for making class a starting point, not a cage (VS, Wikipedia reception).
- Criticized as hostile to newcomers: Game Informer's review said the game "throws a lot at you with little direction" (VS, via Wikipedia). An interviewer put it to Chris Wilson that the tree is "a little infamous for being this gigantic grid that's a little overwhelming" (LO, Fandom interview snippet; the page refused the fetch). A reported design idea: a simpler view of the tree for new players, with depth unfolding over time (LO).
- Build-statistics sites push players toward copying the top builds, which narrows variety (VS for the copy feature; the convergence effect is UV inference, widely discussed).
- Chris Wilson's GDC 2019 talk, "Designing Path of Exile to Be Played Forever," is about long-term retention and seasonal structure; its abstract does not mention the tree (VP, GDC Vault abstract).

**Lesson for Sŏn.** This is the closest structural match to D28: one shared web, roles as different doors into it, with named milestone nodes and rule-changing nodes. It is also the clearest warning: the full web on first view overwhelms, and players navigate it with search, highlighted paths and outside planners.

### 1.3 Final Fantasy X: the Sphere Grid

**Structure.** One pre-set grid of connected nodes shared by the whole party. Each character starts in a different region matched to their role (Tidus speed, Yuna white magic, Lulu black magic), and can cross into another's region; locked nodes, opened by **key spheres**, block the crossings until later (VS, EIP Gaming and Wikipedia). Kimahri's region connects to almost everyone's, making him the deliberate generalist (VS). The player can turn "the White Mage-roled Yuna into a physical powerhouse and the swordsman Auron into a healer" (VS, Wikipedia). The International version's Expert grid starts everyone in the middle with fewer nodes overall (VS, Wikipedia).

**Intent.** Producer Yoshinori Kitase: the grid's purpose was to let players "observe the development of those attributes firsthand" (VS, quoted in Wikipedia). Kitase liked board games and wanted the feel of moving pieces and filling a board (LO, from the 20th anniversary Famitsu interview summary; translation page did not load). Battle director Toshiro Tsuchida handled the system (LO).

**Praise and criticism.** GamePro called it "one of the best innovations in the series"; some reviewers felt it "took up too much of the game" (VS, Wikipedia). Players criticize the Standard grid as a hallway that looks like a web: each character's region is effectively linear until the key spheres open (VS, ResetEra thread).

**Lesson for Sŏn.** The best existing model for "roles are starting points on one shared map, and cross-training means walking into a neighbor's region." The key sphere is the right metaphor for Brandon's unblock conversation: the lock on a crossing is a conversation, not a wall. The warning: if each region is a single line, the web is decoration.

### 1.4 Skyrim: skills rise by use, perks are stars

**Structure.** Eighteen skills in three groups (combat, magic, stealth); each skill rises by doing it (crafting a dagger raises Smithing; bow damage raises Archery); enough skill rises give a character level and one perk point, spent in that skill's perk tree (VS, Wikipedia). No class is chosen at the start (VS). Legendary skills, added in a 2013 patch, removed the level cap (VS; that making a skill Legendary refunds its perks is LO).

**Visual.** Each skill is a constellation in a night sky; perks are its stars; the stars link as the perks are taken (VS, Wikipedia and wikis).

**Praise.** Critics praised perks as "a great method to make your character feel even more unique and personal" (Steve Butts, The Escapist) and a system that "forms around the way you play, but allows for tweaking so that you retain a sense of control" (Kevin VanOrd, GameSpot); Eurogamer's John Bedford noted it suited both all-rounders and specialists (VS, all via Wikipedia).

**Criticism.** Use-based growth invites grinding on low-value repetitions: players forge hundreds of iron daggers to max Smithing, and feel the system cheated them once they find out (VS, HubPages essay and player threads; sentiment, not critic). Todd Howard's stated aim was to "remove confusion" (VP, Game Developer interview), not to prove mastery.

**Lesson for Sŏn.** The constellation per discipline is exactly the visual Brandon is reaching for, and "you are what you do" is right in spirit. But counting uses is not proof: Skyrim's daggers are the argument for Sŏn's rule that a node lights on evidence, never on repetitions.

### 1.5 Starfield: challenges gate the ranks

**Structure.** Five categories (Physical, Social, Combat, Science, Tech), four tiers each; a higher tier needs points spent in lower tiers of the same category; every skill has four ranks; "the first rank of each Skill has no Challenge, each subsequent rank requires completing a relevant challenge before a skill point can be spent to rank up" (VS, Starfield Wiki). Backgrounds give three starting skills (VS, search coverage of GameSpot; LO for the article itself, which refused the fetch). Todd Howard described it as combining "the best" of earlier Bethesda systems (LO, GameSpot headline).

**Visual.** The skills screen is a tiered grid of embroidered patch badges per category, with border styles marking rank (VS for the rank borders, Starfield Wiki). It is not a star chart; "Constellation" is the name of the game's explorer faction (UV from memory of the UI; flag if Brandon's reference is to that screen).

**Criticism.** Cody Perez (Siliconera, 2023-09-03): the hybrid of points plus challenges "disrupts" pacing; challenge progress does not count until you have bought the prior rank, so work done early is wasted; difficulty is inconsistent (Piloting needs a long grind of ship kills, Leadership is "hilariously easy" though higher tier); key features sit behind grind (VS).

**Lesson for Sŏn.** The best game precedent for "a rank is earned by proving it, not by clicking," and the clearest list of how to get it wrong: do not charge twice (a point and a proof), do not discard evidence gathered before the node was formally opened, and calibrate gates so equal-looking nodes demand comparable proof.

### 1.6 Grim Dawn: a constellation map with a shared center

**Structure.** Devotion points come from restoring shrines found across the world. They are spent on a celestial map of constellations; everyone begins at the **Crossroads**, which opens paths outward; "each Constellation has a starting Star"; completing a constellation earns **affinity** in one of five colors, and "when you have gathered enough Affinity, new Constellations will light up"; affinity is not spent (VP, grimdawn.com official guide). Tiers run from center to edge: cheap inner constellations give affinity, outer ones need a lot of it (VS, Grim Dawn wiki via search; LO for the exact thresholds). Points can be unlearned for a fee, or all reset with a rare tonic (VP).

**Praise and criticism.** Regarded as one of the game's best features (LO); players rely on outside devotion planners to read it (VS, several community planner tools exist).

**Lesson for Sŏn.** Almost a direct template: a shared center (the trunk), constellations (disciplines), completing inner clusters opening outer ones, and affinity as "you have enough foundation across neighbors to reach this cross-discipline star." It also shows that a real constellation map reads well at the level of whole constellations and poorly at the level of single stars, hence the planners.

### 1.7 Assassin's Creed Valhalla: the widely criticized constellation

**Structure.** A "skill star chart" of constellations in three directions; each constellation holds one ability and a handful of stat boosts; most of the chart starts under fog and is revealed only by spending points near it (VS, Kotaku, Ari Notis, 2020-11-19). Points in a revealed cluster can be freely reassigned (VS).

**Criticism.** Critics and players single it out: the constellation backdrop "fits well visually, but it lacks any real substance," progression "through arbitrary stats," "quantity over quality" (LO, Medium essay by Ry Stevens, fetch refused; consistent with search summaries). Players quote nodes like a tiny damage bonus after sprinting for a set time with an axe equipped as the emblem of filler (VS, ResetEra thread). Kotaku's own guide is a workaround to defeat the fog, because planning was impossible without it (VS).

**Lesson for Sŏn.** The proof that a beautiful constellation visual does not save a web of filler. Fog that hides the whole map kills planning; every star must be a capability someone would be proud to have.

### 1.8 Civilization VI: tech tree, civics web, and boosts earned by doing

**Structure.** Two parallel trees, technology (science) and civics (culture) (VS, Wikipedia). Most nodes carry a **Eureka** or **Inspiration**: a small in-world goal tied to the subject that, when met, pays a large part of that node's cost (VS). Lead designer Ed Beach: "We want to break people out of their consistent playstyles"; the new approach "takes a sledgehammer to the old method, to stop people from doing the same thing every time they play"; "you can't just burn through the tech tree the same way in every game because the map is going to force you to think through things" (VP, Game Developer interview, 2016-05-11).

**Lesson for Sŏn.** Doing the thing on the floor can speed a node without lighting it. In Sŏn terms: floor exposure opens practice, earns the booking link sooner, or unlocks the next module under D2's time-and-progress rules, but only the gate lights the star. Also: a web that responds to what a person actually does is how games break "everyone takes the same path."

### 1.9 Others, briefly

| Game | Structure | What it shows | Label |
|---|---|---|---|
| World of Warcraft (Mists of Pandaria redesign) | Replaced big talent trees with one choice of three every few levels, swappable. Greg Street: "we tried the talent tree model for seven years. We think it's fundamentally flawed and unfixable"; picking a 10-point bonus over a 5-point one "isn't interesting"; fewer choices, "more choices that matter." | The designer's own case against filler and cookie-cutter builds. | VS (Engadget, 2011-12-08, quoting Street) |
| Diablo III | No tree. Skill slots, runes, and free instant respec. David Sirlin called it the "biggest comeback in system design": Diablo II's point hoarding was a trap for new players, its trees produced guide-copied builds, and no respec punished experiment. Jay Wilson (director) dismissed Diablo II's stat allocation as a poor customization system. | Remove permanent commitment and exploration grows. | VS (Sirlin on Game Developer, 2012-05-07) |
| Diablo IV | Skill tree, then Paragon boards at endgame. Players and commentators say normal board nodes "hardly play any role," experimentation is a "tedious click fest," and progression feels empty once Paragon takes over. | Filler connectors between the few nodes that matter. | VS for player sentiment (Blizzard forums); LO for the Icy Veins analysis (403) |
| Ghost of Tsushima | Four stances, each strong against one enemy type, each with its own technique tree; stances unlock by observing or killing Mongol leaders, not by points. Stanislav Costiuc praises the pacing that spaces out new mechanics. A reviewer notes it gets less interesting once favorites are mastered mid-game. | Unlock tied to a demonstrated act in the world; each tree answers a real situation. | VS (guides for the leader unlock; Costiuc, Game Developer, 2022-02-28); VS for the reviewer via search summary, LO for the page |
| The Witcher 3 | Four color-coded trees (combat, signs, alchemy, general); many skills can be bought but only a limited set are active at once, swappable; mutagen slots boost matching colors; points can be refunded. The remaster was framed as fixing builds that "didn't feel powerful until far into that branch." | Breadth of what you know versus a small loadout of what you run; slow payoff is a known fault. | VS (Fextralife wiki); LO (remaster coverage) |
| Deus Ex: Human Revolution | Augmentations by body part, bought with Praxis; four supported approaches: combat, stealth, hacking, social. Boss fights, outsourced under time pressure, forced combat and were uniformly criticized for ignoring the stealth or social build a player had made; the Director's Cut fixed them. | A final test that does not honor the path the player built breaks trust in the whole system. | VS (Wikipedia; Kotaku and PC Gamer via search) |
| Mass Effect 2 / Andromeda | ME2 cut ME1's long lists of small increments to a few powers with more ranks (LO). Andromeda lets you invest across all trees and switch "profiles" that re-weight your passives (VS, guides). | Fewer, weightier nodes; letting a hybrid swap emphasis without a rebuild. | LO / VS |
| Borderlands 2 | Three trees per character, each a playstyle; a capstone at the bottom of each needs heavy investment; mixing trees is often better than maxing one. | Capstones as visible long-term goals. | VS (Borderlands wiki via search) |
| Ori and the Will of the Wisps | Replaced the first game's ability tree with Spirit Shards found in the world and equipped as a loadout. Thomas Mahler (Moon Studios): "We saw Spirit Shards as the natural evolution to the Ability Tree System." | Players dislike being forced through nodes they do not want to reach the ones they do. | VP (Game Developer Q&A, 2020-05-18) |
| Star Wars Jedi: Survivor | Three trees (Lightsaber, Force, Survival), with five stances each having branches; reviewers broadly liked specificity. | Clean, legible per-domain trees. | LO |
| Hades (Mirror of Night) | Each talent has an alternate you swap to but cannot hold at the same time; alternates unlock through a character relationship, not currency. Reset is widely reported as free. | Paired either-or choices; exploration without penalty. | VS (Fextralife) for pairs; LO for free reset |
| Destiny 2 (subclass 3.0) | Fixed trees replaced by Aspects (class-specific) and Fragments (shared) that mix and match. Destiny 1 used talent grids whose nodes unlocked by accumulated experience. | Move from grinding nodes open to composing a loadout. | VS (guides); LO for Bungie's stated intent (article body did not load) |
| Fallout 4 | All perks shown at once on one poster-style chart: columns by attribute, rows by required level. | Showing everything up front makes planning easy and creates desire. | VS (fan charts via search), UV for intent |
| No Man's Sky | Technology blueprints bought from a rotating list, not a visible tree. | Mostly a counterexample: little visible long-term goal. | VS (NMS wiki via search) |

### 1.10 Two learning products that tried a constellation (the most relevant warning)

- **Khan Academy's Knowledge Map (2010 to about 2013).** Exercises as stars on a starry sky built on Google Maps, colored by proficiency and recommendation. Engineer Ben Kamens: it existed to "clearly show students which exercises they should be working on and where progress has been made" (VP, bjk5.com, 2010-11-23). It was removed after mission and course mastery systems arrived; a staff reply is reported as saying most students and teachers found linear course progression works best, and the map's Google Maps dependency also ended (LO, help-center threads refused the fetch). Users kept asking for it back for years (VS, thread titles).
- **Duolingo, 2022.** Replaced its skill tree with a single path, because learners were "not sure whether they're using Duolingo the 'correct' or 'best' way"; the path gives "a clear path to follow" and orders lessons for spaced repetition (VP, Duolingo blog, 2022-05-06). The blog gives no outcome data (VP); a later company white paper claims improved outcomes (LO).

**Lesson for Sŏn.** Webs are loved for orientation and desire, and learners stall when the web does not also answer "what do I do next." Both products kept the wish for the map and moved the daily experience to a path. Sŏn needs both: the web to see and choose, a lit next step to act.

---

## 2. Design principles that recur

| Principle | What the games show | Sources |
|---|---|---|
| **Meaningful choice over a checklist of small bonuses** | Choices are interesting when they involve tradeoffs, fit the situation, express the player, and are informed; a choice everyone makes the same way is not a choice (Meier). Choosing between a larger and a smaller flat damage bonus "isn't interesting" (Street). "A good skill includes a verb. An awesome skill includes a unique verb" (Kraj). | Meier GDC 2012 via Game Developer (VS); Street via Engadget (VS); GDKeys (VP for Kraj's own article) |
| **Visible long-term goals** | Capstones (Borderlands), Keystones (Path of Exile), surges (Forbidden West), outer constellations (Grim Dawn) are the stars people plan toward. Fallout 4 shows the whole chart at once. | See section 1 |
| **Many starting points into one shared web** | Path of Exile classes, Sphere Grid characters, Starfield backgrounds. Class sets where you begin, not where you may go. | 1.2, 1.3, 1.5 |
| **Unlock by use versus by points** | Use (Skyrim) feels earned but invites grind; points (most games) feel like shopping; boosts (Civ VI) let doing the thing speed a node; challenge gates (Starfield) prove a rank but fail when doubled with points or miscalibrated. | 1.4, 1.5, 1.8 |
| **Proven mastery gates a rank** | Starfield's challenges and Ghost of Tsushima's leader-based stance unlocks tie a rank to a deed. Sŏn goes further: the deed is observed and rated, not counted. | 1.5, 1.9 |
| **Respec and forgiving exploration** | Diablo III's free respec (Sirlin), Hades' free reset, Valhalla's refund within a revealed cluster, Grim Dawn's paid unlearn. Kraj recommends full respec "at high cost" to keep commitment. Players rage at irreversible early mistakes (Path of Exile 2 complaints). | VS; LO |
| **Show locked content to create desire, and to allow planning** | Fallout 4 shows everything; Valhalla's fog is the most-cited frustration; Kraj: visible teases engage planning, hidden structure creates discovery. | 1.7; GDKeys (VP) |
| **Avoid grind and completionism** | Skyrim daggers; Starfield Piloting; Diablo IV Paragon click-fest. Filling the whole map is not the point in Borderlands (mixing beats maxing). | 1.4, 1.5, 1.9 |
| **Readability of huge webs** | Zoom, search with highlight, shortest-path highlight, shareable plans (Path of Exile's own planner); node grades by size (small, Notable, Keystone); color families (Witcher 3); clusters as constellations (Skyrim, Grim Dawn); outside planners appear whenever the in-game view fails. | 1.2, 1.6, 1.9 |
| **Identity and playstyle** | Horizon names stacks by playstyle; Skyrim critics praised a character that "forms around the way you play." Ozzie Smith warns against progression that inflates character numbers while the player's own skill stays flat. | 1.1, 1.4; Game Developer, 2013-02-05 (VS) |
| **How games avoid "everyone takes the same path"** | Situational demand (Civ VI's map changes the best route; Ghost of Tsushima's enemy types each need a stance); swappable loadouts so one best build matters less (WoW, Witcher 3, Destiny 2); fewer, weightier choices. Public build statistics push the other way (poe.ninja). | 1.8, 1.9, 1.2 |
| **Social comparison** | Most online games let others inspect your build, and sites aggregate top players' trees for copying; this feeds a narrow "meta." Single-player constellations (Skyrim, Grim Dawn) are private by nature. No verified source found on games deliberately hiding trees for well-being. | VS for poe.ninja; UV for the effect |
| **A skill map is a learning map** | Daniel Cook's skill atoms and skill chains: each atom is action, simulation, feedback, and the player's growing model; linked atoms form "directed graphs" that show how players learn and where they stall or burn out. | VP (Lostgarden, 2007) |

---

## 3. Failure modes

1. **Bloated webs.** More nodes than meaningful things to do (Forbidden West per players, Valhalla, Diablo IV Paragon). For Sŏn: the web shows capabilities, not modules. Many modules feed one star; a star without a real on-shift capability does not exist.
2. **Trap choices.** A path that looks useful and quietly leaves you weaker: Diablo II's hoarded stat points and early points spent before you understand the game (Sirlin); Deus Ex's boss fights that punished stealth builds. For Sŏn: a trap is a star that counts toward no role, no coverage, and no pay rule while looking like it does, or a gate that only one route (for example, spoken fluency) can pass. The show-don't-tell route on G1 already addresses the second.
3. **Filler nodes.** Small increments with no verb (Street's 10 versus 5 point example; Valhalla's sprint-with-axe bonus). For Sŏn: "reads module X" is filler; "pours to line by feel at tempo" is a star.
4. **Overwhelming first view.** Path of Exile's reputation; Khan and Duolingo retreating from open maps. For Sŏn: the first view is the trunk plus one lit next step, and the web opens by zooming out.
5. **Grind.** Use counts (Skyrim), inconsistent challenge demand (Starfield), connector nodes you must buy to reach the ones you want (Diablo IV, the Ori rationale). For Sŏn: no counters and no connector stars; a prerequisite is on the map only if it is itself worth having.
6. **Hidden map.** Valhalla's fog. For Sŏn: nothing about the structure is hidden. Only a person's position is private.
7. **Decoration over mechanism.** A constellation skin on a linear list (Sphere Grid Standard criticism; Valhalla). For Sŏn: if every role path is one line with no real crossings, draw it as a path and stop pretending.

---

## 4. Mapping to Sŏn

### 4.1 Disciplines as constellations in one sky, trunk at the center

Take Grim Dawn's Crossroads and Path of Exile's shared web. The trunk (D3) is the center cluster every hire lights: why before how, the map itself, how decisions get made, using support, pre-shift, critique culture, care as craft, allergy routing, linked certifications. Around it, each discipline (D28) is a constellation in its own sector. Working names from the brief, for Brandon to confirm or rename (founder call):

- flavor and perception (the gastrophysics foundation D28 names sits in the trunk; its depth lives here)
- liquid craft (bar and barista on one spine, per the starting structure)
- service craft and movement
- the room and time (door, arrival, pacing from the book; D20 delegated door work)
- decision-making (the judgment scenarios, D14)
- teaching and leading (the assessor thread, LEA path, D5 and D21)
- back of house as a chef-gated region: drawn as an outline with no stars until the chef fills it (`chef.*`)

Sector order matters: put neighbors that genuinely share craft next to each other (flavor beside liquid craft; service beside the room; decision-making beside teaching and leading), so the natural cross-training bridges are short lines.

### 4.2 Roles as starting points and required paths on the same sky

Take the Sphere Grid and Path of Exile. A role is not a tree; it is (a) a door on the edge of the trunk facing its home constellation, and (b) a required set of stars at stated depths, drawn as a highlighted thread when you select the role (Path of Exile's shortest-path highlight). From the intake's clarification:

- Food runner enters at service craft and movement; back server and front server are deeper stars in the same constellation, plus required stars in the room and time and decision-making.
- Barback enters at liquid craft; bartender and barista are deeper stars there, plus required flavor and perception stars.
- Host enters at the room and time, which is drawn between service and liquid craft so the host can "go in either direction."
- Leads read as a thread into teaching and leading, not a top rung (D3).

Job descriptions render from the same role manifest (D28), so the highlighted thread and the job description can never disagree.

### 4.3 Stars lit only by proven mastery

Take Starfield's challenge-gated ranks and remove what Perez criticized. A star lights only from the gate record (D8): the spoken check, the small-menu practical, the angel shift, and the eyes-off window as the node's gate spec requires. Never from finishing modules.

- No second currency. No points; the proof is the price.
- Evidence gathered is never discarded for being early (Perez's "non-retroactive" complaint); it is logged on the gate record and counts when the gate is run.
- Calibrate across stars so stars of the same depth demand comparable proof (Piloting versus Leadership). This is the Assessment & Competency Designer's gate spec job at `designed` (D18).
- Floor exposure can act like a Civ VI boost: it can open practice or trigger the booking link (D2, D13), never light the star.
- Gate content answers the route the learner built (the Deus Ex lesson): show-don't-tell on G1, content scored not fluency.

### 4.4 Depth inside a discipline; cross-links as cross-training

- **Depth is distance from the trunk,** in rings: foundation (the trunk's edge), practice, integrated performance (the discipline's signature star, like a Valor Surge or Keystone), mastery, and the teaching ring (the assessor thread). Radial distance reads as depth in one discipline, not height over other people, which keeps D3's "direction and adjacency, never height." A mastery star in flavor sits no higher than a foundation star in service; it is further out in a different direction.
- **Cross-links are bridge stars** between neighboring constellations (Grim Dawn affinity): for example, a palate-calibration bridge between flavor and liquid craft, a pacing bridge between service and the room. A bridge opens when the foundation stars on both sides are lit.
- **The lock on a crossing is a conversation** (the Sphere Grid key sphere). Crossing into a neighbor's constellation for a role move, as opposed to learning, triggers the unblock conversation, auto-booked on a talent block (D13), ending in one of the four recorded outcomes (LEA-006). Learning for interest never needs the key: library and Introduce content is open to anyone by interest (D28).

### 4.5 Node types: drills and decisions look different

Brandon splits physical macro movements from decisions (intake group 3), and Cook's skill atoms say each is a different feedback loop. Give them different shapes, with size for grade as in Path of Exile:

| Shape | Node type | Learning job | How it lights |
|---|---|---|---|
| Small filled dot | Knowledge | know, find | Spoken check (G1) or proven conversation |
| Square | Movement drill | do, hold | Practiced to fluency; may be banked (D11) |
| Diamond | Decision | decide | Scenario judgment; later the alignment measure (D14, never a gate until calibrated) |
| Large star | Integrated performance | do plus decide at tempo | Practical, angel shift, eyes-off window, full night (D10) |
| Hollow circle | Library | know, teach | Proven conversation (D18 `library` type) |
| Ringed star | Teaching | teach | Assessor path plus co-rated audits (D5) |

A large star's lines draw in from the squares and diamonds that feed it, so the picture itself teaches Brandon's rule: drills and decisions are practiced apart and merge in the performance.

### 4.6 States, respec, and what a "miss" looks like

- Star states from the starting structure: not started (outline, always visible), in practice (partial ring), released (lit), released with reads still maturing (lit with a soft halo on hospitality-layer stars), recheck due (lit with a small marker, framed as a house rhythm). A "not yet" never dims or marks a star (D11 and the starting structure).
- Respec: changing direction costs nothing. Interest can move freely; released stars stay released subject to recheck. No attempt counter (D11).
- No completion percentage for the whole sky, no star count, no streaks or leaderboards (D12, `tool.lms.gamification_setting`). Completion is shown only against a person's own chosen or required thread.

### 4.7 Privacy

- A person's lit stars are private by default (D12, Learner Advocate). Leaders see what the gate record (D8) and scheduling need, not a browsable map of everyone.
- The wall map and the Trainual map show the sky's structure only: constellations, stars, bridges, role doors and threads. No names, no counts of who holds what.
- This also blocks the poe.ninja effect: nobody copies the "top build" when nobody's build is on display.
- Founder calls not landed here: whether a person may choose to share their own map (with a mentor, or publicly), and whether releases are celebrated in pre-shift. Mark as `founder.*` if pursued.

### 4.8 What Trainual can show, and what the live page needs

Trainual shows lists and straight-line locking, and only native tests and SCORM report back (`adapters/trainual.md`). So the sky lives on the external live page (D12 option a) plus a static map (option b). The page needs:

1. **The sky definition from this repo:** stars, types, depth ring, constellation, bridges, and which modules feed each star. The catalog and role manifests are the source; the page never defines structure itself.
2. **Role manifests** for doors and threads, the same file job descriptions render from (D28).
3. **Trainual progress per person per module** through the API (`tool.lms.api_access`), used only for the "in practice" state and for next-step suggestions.
4. **Gate records from the form tool** (`tool.forms.gate_record`, D8) for the lit state. This is the key point: Trainual completion never lights a star.
5. **Recheck timing** (`workflow.recheck_cadence`) for the recheck marker, and the full-night condition (D10) for coverage.
6. **Booking links** (`workflow.gate_autoschedule`, `tool.scheduling.platform`, D13) surfaced on the star that is ready.
7. **Per-person sign-in** so each person sees only their own lights; host and sign-in method are new bindings (proposed `tool.web.host`, `tool.web.auth`; not yet declared anywhere).
8. **Update at close** (D12, Realist), not live during service.
9. **Readability features:** zoom from sky to constellation to star; search with highlight; select a role to highlight its thread; a "next step" lit path as the default view (the Duolingo and Khan lesson); a phone layout, since most learners will be on a phone; state carried by shape and label, not color alone.
10. **A static export** of the structure-only sky for the wall and for a Trainual image page, regenerated when the structure changes.

---

## 5. Recommendation

### Recommended: one sky, trunk at the center, disciplines as constellations, roles as doors and threads

Grim Dawn's center and constellations, Path of Exile's shared web and grades, the Sphere Grid's doors and key-sphere crossings, Skyrim's star-per-perk look, Starfield's proof-gated ranks minus the points, and a Duolingo-style next step as the default view.

```
                         teaching and leading
                        (T)      *
                          \     / \
             decision-     <>--*   \          liquid craft
             making       /    |    *---[]---(*)  bartender / barista
                 <>--<>--*     |   /      |     \
                          \    |  /       o      [] barback door
                           \   | /       /
    back of house   . . .   +-----------+  bridge: palate    (*)--*
    (chef-gated,    . . .   |   TRUNK   |--------------------*   flavor and
     outline only)          | core, care|                    |   perception
                           /| critique  |\                   o
                          / +-----------+ \
                         /       |  host   \
            service   []        (door)      <>   the room and time
            craft and  \         |           \
            movement   (*)--*    *---<>---*--(*)  lead host
          runner door   |    bridge: pacing
          back server   *
          front server (*)

  Legend:  o knowledge   [] movement drill   <> decision   * star (released capability)
           (*) integrated performance (signature star)   (T) teaching ring
           . . . chef-gated outline   distance from TRUNK = depth in that discipline, not rank
  Selecting a role lights its thread; the default personal view shows only the trunk,
  the person's lit stars, and one "next step" star with its booking link.
```

**Why.** It is the only shape that holds all of D28 at once: one program, many disciplines, depth without altitude, roles as sets on a shared map, and cross-training as walking to a neighbor. It is also the picture Brandon asked for.

**Costs and risks.** Hardest to draw legibly and to keep current; needs the live page to earn its keep; risks Valhalla's fate if stars are padded; first view must be tamed. Mitigations are in 3 and 4.8.

### Alternative A: a constellation per discipline (the Skyrim model)

Each discipline is its own star chart on its own screen; a home screen shows the trunk and the ring of constellations as tiles; cross-links appear as "also opens" references on a star rather than as drawn lines.

- **Gains:** far easier to draw, print, and read on a phone; each constellation can be a Trainual image page; new disciplines slot in as a new tile.
- **Loses:** the sense of one shared web; cross-training becomes a footnote rather than a visible bridge; roles become lists of stars across tiles, which drifts back toward role-shaped pockets (the thing D28 rejected).
- **Choose it if** the live page is delayed or `tool.lms.api_access` is refused, as the static fallback.

### Alternative B: a board (the Sphere Grid and Fallout 4 model)

A regular grid (hexes or a lattice) with fixed positions: trunk tiles in the middle, discipline regions as colored zones, depth as rows outward, role doors as starting tiles, key tiles on the region borders.

- **Gains:** most readable and printable at wall scale; every tile has an address; Kitase's board-game feel suits a team that likes progress you can point at; easy to show everything with no fog.
- **Loses:** looks like a game board, not a sky; regular geometry forces equal-looking tiles and tempts filler to fill the grid (the Diablo IV Paragon problem); the Standard Sphere Grid shows a lattice can still be a hallway.
- **Choose it if** the wall map matters more than the phone view, or if Brandon prefers a planning tool to an atmosphere.

### What to decide (for Brandon; nothing here is decided)

1. Shape: the one-sky web, a constellation per discipline, or a board.
2. Discipline names and sector order (founder call; brand voice through the Brand Guidelines Verbal Identity page).
3. Whether back of house appears as an outlined region now (chef-gated).
4. Whether people may opt to share their own map, and whether releases are celebrated in pre-shift (`founder.*`).
5. Whether the live page is built before or after the first cohort; Alternative A as the fallback.

---

## Sources

| # | Source | Used for | Label |
|---|---|---|---|
| 1 | Game Informer, "How Horizon Forbidden West's new Valor Surges work," 2021-06-03, gameinformer.com/2021/06/03/how-horizon-forbidden-wests-new-valor-surges-work | de Jonge quotes; surge mechanics | VP (interview) |
| 2 | GamingBolt, "Horizon Forbidden West's skill tree has been completely redesigned," 2021-06-03, gamingbolt.com | de Jonge quote | VP (interview) |
| 3 | Gfinity, "Forbidden West skill tree," gfinityesports.com/article/forbidden-west-skill-tree | Six trees, surge unlocks | VS |
| 4 | ResetEra, "What are the worst skill trees you've seen?" page 2, resetera.com/threads/what-are-the-worst-skill-trees-youve-seen.1080465/page-2 | Player sentiment on Forbidden West, Valhalla, FFX | VS (sentiment only) |
| 5 | pathofexile.com/passive-skill-tree (official planner) | Classes, node grades, search, shortest path, sharing | VP |
| 6 | Wikipedia, "Path of Exile" | Shared tree, class starts, reception | VS |
| 7 | GDC Vault, Chris Wilson, "Designing Path of Exile to Be Played Forever," GDC 2019, gdcvault.com/play/1025784 | Talk scope | VP (abstract) |
| 8 | Fandom, "Interview: Chris Wilson on Path of Exile 2's origins" | "Overwhelming" tree question | LO (fetch refused) |
| 9 | poe.ninja and guides describing it | Build aggregation and copying | VS |
| 10 | Wikipedia, "Final Fantasy X" | Sphere Grid mechanics, Expert grid, Kitase intent, reception | VS |
| 11 | EIP Gaming, "Final Fantasy X: the Sphere Grid," eip.gg | Character regions, key spheres | VS (search summary) / LO |
| 12 | Frontline JP, FFX 20th anniversary interview part 2, 2021-07-28 | Board-game inspiration, Tsuchida | LO (page empty on fetch) |
| 13 | Wikipedia, "The Elder Scrolls V: Skyrim" | Use-based skills, perks, reception quotes | VS |
| 14 | Game Developer, "Interview: Todd Howard on the scope, vision of Skyrim" | "Remove confusion" | VP |
| 15 | HubPages, "A tale of two exploits: skill perks and character leveling in Skyrim"; Steam threads | Iron dagger grind | VS (sentiment) |
| 16 | Starfield Wiki, starfieldwiki.net/wiki/Starfield:Skills | Categories, tiers, ranks, challenges, badge borders | VS |
| 17 | Siliconera, Cody Perez, "Starfield skills rank up challenges disrupt level up pacing," 2023-09-03 | Criticism of challenges | VS |
| 18 | GameSpot, "Starfield character creator includes optional traits, skill system that combines the best..." | Howard framing, backgrounds | LO (403) |
| 19 | grimdawn.com/guide/character/devotion (official) | Shrines, Crossroads, constellations, affinity, reset | VP |
| 20 | Grim Dawn wiki (via search); community devotion planners | Tier thresholds; planners | LO / VS |
| 21 | Kotaku, Ari Notis, "How to easily uncover every skill in Assassin's Creed Valhalla," 2020-11-19 | Fog, refunds, workaround | VS |
| 22 | Medium, Ry Stevens, "Assassin's Creed Valhalla: a starving skill tree" | Criticism quotes | LO (403) |
| 23 | Game Developer, "Civilization VI's lead designer wants to shake up players," 2016-05-11 | Ed Beach quotes | VP (interview) |
| 24 | Wikipedia, "Civilization VI" | Two trees, boosts | VS |
| 25 | Game Developer, "GDC 2012: Sid Meier on how to see games as sets of interesting decisions" | Interesting decisions | VS |
| 26 | Engadget, "Ghostcrawler on seeing the forest for the talent trees," 2011-12-08 | Greg Street quotes | VS |
| 27 | Game Developer, David Sirlin, "Diablo 3's ability system," 2012-05-07 | Respec, trap choices, Jay Wilson | VS |
| 28 | Blizzard Diablo IV forums; Steam discussions | Paragon sentiment | VS (sentiment) |
| 29 | Icy Veins, "Why Paragon may be a bigger problem than Diablo 4's skill tree" | Paragon analysis | LO (403) |
| 30 | Game Developer, Stanislav Costiuc, "Ghost of Tsushima design analysis," 2022-02-28 | Stances, pacing | VS |
| 31 | TheGamer and NME guides on Ghost of Tsushima stances | Leader-based unlock | VS (search summary) / LO |
| 32 | Fextralife, The Witcher 3 "Skills and Talent Trees" | Trees, active slots, mutagens, refunds | VS |
| 33 | Wikipedia, "Deus Ex: Human Revolution"; Kotaku and PC Gamer on outsourced bosses | Four approaches; boss criticism | VS |
| 34 | Game Developer, "Q&A: designing ... Ori and the Will of the Wisps," 2020-05-18 | Thomas Mahler quote | VP (interview) |
| 35 | Fextralife, Hades "Mirror of Night" | Paired talents | VS |
| 36 | Destiny 2 subclass 3.0 guides (GGRecon, Dexerto, TheGamer); Bungie TWAB 2022-02-10 | Aspects, fragments | VS / LO (Bungie body did not load) |
| 37 | Borderlands wiki (via search) | Three trees, capstones | VS (search summary) |
| 38 | Fallout 4 perk chart coverage (Windows Central, others) | All perks shown | VS (search summary) |
| 39 | GDKeys, Nicolas Kraj, "Keys to meaningful skill trees" | Verbs, respec, tree size, visibility | VP (author's own article) |
| 40 | Game Developer, Ozzie Smith, "Player skill, character skill, and skill progression systems," 2013-02-05 | Player versus character skill | VS |
| 41 | Lostgarden, Daniel Cook, "The chemistry of game design," 2007-07-19 | Skill atoms and chains | VP |
| 42 | bjk5.com, Ben Kamens, "Constellation knowledge," 2010-11-23 | Khan Knowledge Map intent | VP |
| 43 | Khan Academy help-center threads on the Knowledge Map | Removal and reasons | LO (403) |
| 44 | Duolingo blog, "New Duolingo home screen design," 2022-05-06 | Tree to path rationale | VP |
| 45 | IntechOpen, Tibor Guzsvinecz, progression systems taxonomy, 2025 | Taxonomy; note on educational skill trees | VS |

Repo inputs: `research/intake-2026-09.md` (groups 2 and 3), `framework/system-design.md` (D2, D3, D5, D8, D10 to D14, D18, D20, D21, D28), `research/starting-structure-2026-09.md` (gates G1 to G4, node states, supervision levels), `adapters/trainual.md`.
