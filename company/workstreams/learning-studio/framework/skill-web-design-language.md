# Skill web design language and constraints

The visual system and structure of Sŏn's training program map: the one sky that every surface of the skill web is drawn from. It is written so the live personal page, the phone view, the back-of-house wall map, print, and any brief to an AI design tool can be generated consistently from it, and so a new module can be placed on the map without a redesign.

**Status.** Proposed, 2026-09-28. Written from `framework/system-design.md` (D3, D10, D12, D28 to D31), `research/phase2-working/11-game-skill-trees.md`, intake group 2, Brandon's feedback on the first generated concept, the Brand and Experiential Guidelines v3.0 (Box `2281626080747`, the canonical PDF per D26), and the judgment of the Design Director, Web and UI Specialist, Brand Identity Specialist, Editorial and Layout Specialist, and Design Brief Translator seats. Every value marked **proposed** waits on Brandon (section 12). Where this file and `system-design.md` disagree, `system-design.md` wins.

**How to read the citations.** "BG 10" means Brand and Experiential Guidelines, section 10. A value with a BG citation is a brand fact. A value marked proposed is not; it is declared as a `brand.skyweb.*` binding until Brandon confirms it.

---

## 1. Purpose and what this governs

**Purpose.** The skill web lets a person see the whole program, choose a direction by interest, and know their next step. It shows disciplines (D28) as constellations around a shared trunk (D3), depth as distance from the trunk, roles as required sets of stars (D28), and a person's own lit stars, which light only from a recorded gate (D8, D10).

**It governs every surface of the skill web:**

| Surface | Decision | Shows a person's position? |
|---|---|---|
| Live personal page | D12 (a) | Yes, to that person only |
| Phone view of the live page | D12 (a) | Yes, to that person only |
| Back-of-house wall map | D12 (b) | Never: structure only |
| Static map in Trainual | D12 (b) | Never: structure only |
| Print (handouts, the wall map file) | D12 (b) | Never: structure only |
| Briefs to AI design and video tools | Standing rules, "Design prompts" | Structure and sample states only |

**What the skill web must never do.**

1. **Show rank or altitude.** No surface places one discipline, role, or person above another. Depth is distance outward in one direction, never height (D3). No discipline owns the top of the sky (section 3.2).
2. **Show anyone else's progress.** No names, no counts of who holds a star, no team view, no "people like you" comparisons (D12, D31). Leaders see what the gate record and scheduling need, through those tools, not through the web.
3. **Gamify.** No streaks, leaderboards, points, levels, badges, completion percentages for the sky, star totals, timers, or countdowns (D12; `tool.lms.gamification_setting` stays off unless Brandon turns it on).
4. **Carry filler.** A star is a capability someone could be proud of on a real shift. "Completed module X" is not a star. Many modules feed one star (section 9).
5. **Share.** No share button, export of a personal map, or public profile (D31). Celebration happens in person.
6. **Hide the structure.** No fog. Every star, bridge, and role thread is visible to everyone; only a person's own lights are private.
7. **Mark a miss.** A "not yet" never dims, reddens, or flags a star (starting structure, node states; D11). A star is lit, in practice, open, or not yet open. Nothing else.
8. **Light a star from completion.** Trainual completion can move a star to "in practice"; only the gate record lights it (D8).
9. **Celebrate on screen.** A newly lit star is confirmed, not celebrated: no confetti, glow bursts, or sound (BG 16, interaction principles).

---

## 2. Why the first concept failed

The first generated concept: a dark screen, amber stars, dots and thin lines radiating around a central trunk circle, labels scattered around it. Brandon found it terrible. The diagnosis, so the failure is designed against rather than repeated:

| Failure | Mechanism | Rule that prevents it |
|---|---|---|
| Nothing to read as a figure | Stars sat on spokes, so the eye found a wheel, not constellations. Constellations are memorable because the lines make a figure (H. A. Rey's redrawn figures exist because the traditional ones were hard to remember). | Each discipline is a drawn figure from a named template (3.4). |
| No grouping | One color and one dot size everywhere: every star belonged to everything. | One hue per discipline, applied to stars and lines, plus a region boundary (4.1, 3.2). |
| Hub-and-spoke | A central circle with lines to every star says "everything depends on the center equally," which is false and reads as an org chart. | One root line per constellation from the trunk; all other lines are internal to a figure (3.3). |
| Uniform dots | No grade, so no star was worth planning toward. | Shape by kind, size by grade; the signature star is the largest mark in its figure (5). |
| Label clutter | Every label shown at once, placed wherever it fit. | Labels by zoom level and priority, at fixed offsets (6.2). |
| Amber on dark | Warm gold dots on black read as generic "space UI" and imitate gold, which the brand keeps physical only (BG 10, Gold Foil). | Hues from an earthen set anchored in the brand palette; no glow, no metallic (4). |
| No entry point | The first view was everything, with no "you are here" and no next step. | The default personal view opens on the next step (7.4). |
| No hierarchy | Trunk, disciplines, stars, and labels all at the same visual weight. | A four-level hierarchy: sky, constellation, star, detail (7.2). |

The failure is the one the Web and UI seat names as the conceptual gap: a surface with no system under it. This file is the system.

---

## 3. Structural grammar

### 3.1 The sky

- The sky is a disc: a polar map with the trunk at the center, the planisphere form of star charts, including the Joseon stone chart Cheonsang Yeolcha Bunyajido, which uses a polar projection (reference only; see open call 12.9).
- The sky has no up. It is never tilted, perspective-rendered, or given a horizon, because any of those creates a top.
- The sky's orientation is fixed on every surface so that people build spatial memory: service craft is always in the same place on the phone, the page, and the wall.
- Ground: Plum Ink in the dark variant, Bone in the light variant (section 4.4).
- No decoration fills the sky: no background stars, nebulae, gradients, textures, or noise. Empty space is the specification (BG 02, Ma; BG 08, principle 05). The only marks are the program's own.

### 3.2 Regions and sectors

- Each discipline owns one sector of the disc, an angular wedge from the trunk's edge to the rim, like an IAU constellation boundary: everything inside the boundary belongs to that discipline.
- Sectors are equal in angle. No discipline gets more sky because it has more modules; density is handled by splitting (3.8).
- Sector order is D29's soft-locked order, clockwise: service craft and movement; the room and time; flavor and perception; liquid craft; teaching and leading; decisions; back of house. Neighbors that share craft sit side by side, so the natural bridges are short.
- **No discipline owns the top.** The sky is rotated so that a sector boundary, not a sector's center, sits at twelve o'clock (layout procedure, section 9.3).
- A region boundary is a single dotted hairline, supplementary only: identity is always carried by hue, position, figure, and label together.

### 3.3 The trunk

- The trunk is its own small constellation at the center, drawn in the neutral trunk color (Parchment on dark, Plum Ink on light), because it belongs to every discipline equally.
- Trunk stars sit on two inner circles. The trunk's outer edge carries one **door** per sector: the point where that discipline's root line leaves the trunk.
- Each discipline connects to the trunk by exactly one **root line**, from its door to the discipline's foundation star. No other line crosses the trunk edge. This is the difference between a trunk with branches and a hub with spokes.
- The trunk is lit for everyone who has passed its gates. It is never drawn as a filled circle or a disc: it is stars and lines like everything else.

### 3.4 Disciplines as constellations drawn as figures

- Each discipline is drawn as one or more **constellations**. Each constellation has a **figure**: a named silhouette built from its stars and lines, so it can be recognized and remembered (the Rey principle).
- Figures are built from a **figure template** (section 9.4): an ordered list of slots, each a depth ring and an angular offset. Stars fill slots in order. The template is chosen so the figure reads at every stage of growth, from its first three stars.
- Figures are line-and-tree shaped, not dense meshes. Constellation line figures across cultures are sparse networks, mostly chains and trees, and East Asian asterisms are the simplest of all (PLOS One, source 12). Rule: no star draws more than three lines; further prerequisites are listed in the star's detail, not drawn.
- Figure subjects come from each discipline's own material world (a vessel for liquid craft, a threshold for the room and time, and so on). The subjects are for Brandon to pick from the first concepts (open call 12.3). Figures are never the brand's reserved marks: never the 선 glyph, never the bird mark 원앙, never a tiled letterform (BG 08).

### 3.5 Depth as distance

Depth is the ring a star sits on. Distance from the trunk means depth in one discipline, never standing over anyone.

| Ring | Name | What sits there |
|---|---|---|
| 0 | Trunk | The shared core |
| 1 | Foundation | The discipline's entry stars; the root line lands here |
| 2 | Practice | Movement drills, decisions, and knowledge the performance needs |
| 3 | Performance | The signature star: the integrated performance at tempo (G2 to G4) |
| 4 | Mastery | Depth beyond the performance |
| 5 | Teaching | The assessor thread for this discipline (D5, LEA) |
| L | Library band | Library tracks, at the rim (3.10) |

A mastery star in flavor and a foundation star in service are equally far from anyone's reach in any sense that matters: they point different ways.

### 3.6 Cross-discipline bridges

- A **bridge** is a star that belongs to two adjacent disciplines (the Grim Dawn affinity idea, applied to craft): for example, palate calibration between flavor and liquid craft.
- A bridge sits on the boundary between its two sectors, at its depth ring, and is drawn split: each half in one discipline's hue.
- A bridge opens when its required stars on both sides are lit. It draws one line to each side.
- Only adjacent disciplines get drawn bridges. A crossing between non-adjacent disciplines is listed in both stars' details and drawn only while one of them is selected, as a curved hairline inside ring 1. If non-adjacent crossings become common, the sector order is wrong: raise it with Brandon (open call 12.8).

### 3.7 Role required sets as highlighted threads

- A role is not a region. It is a required set of stars at stated depths (D28), drawn as a **thread** only when selected.
- The thread starts at the role's door on the trunk edge and runs through its required stars in path order, following existing figure lines where they exist.
- The thread is neutral (Bone on dark, Plum Ink on light), because a role crosses disciplines; it never takes a discipline's hue.
- Required stars get the thread ring (5.3). Stars outside the set step back to their structure state for the duration.
- One thread at a time. A role title on screen is a `people.*` binding until titles are set.
- The thread and the role's job description render from the same role record (D28), so they cannot disagree.

### 3.8 Maximum stars, spacing, and splitting

| Rule | Value | Status |
|---|---|---|
| Stars per constellation | 12 maximum | proposed |
| Constellations per discipline | 3 maximum | proposed |
| Disciplines on the sky | 7 maximum (the categorical color limit) | proposed |
| Drawn lines per star | 3 maximum | proposed |
| Minimum distance between star centers, constellation zoom | 28px | proposed |
| Minimum distance between star centers, wall map | 14mm | proposed |

**When to split a constellation.** Split when any of these is true:
1. It would exceed 12 stars.
2. Its stars form two groups that connect only through the foundation star (two crafts sharing a name, such as bar and coffee inside liquid craft).
3. Its ring cannot hold its stars at minimum spacing.

A split divides the discipline's sector into equal sub-sectors, one per constellation, each with its own figure and name, all in the discipline's hue. A split is a versioned structure change: the wall map and Trainual map are regenerated, and the change is noted at pre-shift. A discipline that would need a fourth constellation, or an eighth discipline, is a program-structure decision for Brandon and the Curriculum & Program Architect, not a layout event.

### 3.9 The chef-gated back-of-house draft

- Back of house is drawn now (D30), as a draft, using the brand's own convention for held items: the hollow mark carries every item held for the executive chef (BG 17).
- Its stars are drawn in the held state (5.2): hollow, dashed, in the neutral ash hue. None can light until the chef redevelops and signs off the discipline, because no back-of-house module parks before then (D30).
- Star names that would carry station specifics, recipes, or menu execution show "Held for the chef" and bind with `chef.*`. The structure and the durable craft may be named.
- The sector's label reads "Back of house, draft". Its hue is assigned when the chef signs off (open call 12.7).

### 3.10 Library tracks

- Library content (D18, `library` type: reading and listening tracks, finished by a proven conversation) is open to anyone by interest and never gates a role.
- Library stars sit on the library band at the rim of their discipline's sector, as capsules joined by a dotted track line. A library track that serves several disciplines sits on the band at a sector boundary.
- Library stars light from the logged proven conversation, like any other star.
- The library band is shown at constellation zoom and deeper, never at sky zoom.

---

## 4. Color system

### 4.1 Principles

1. **One hue per discipline, applied to its stars and lines** (Valhalla's batching: red, blue, and yellow branches, each with matching gear, verified-primary on Ubisoft's page). Hue says "which discipline" at a glance.
2. **State is carried by fill and stroke, never by hue alone** (WCAG 2.2, 1.4.1). Every state has a shape signature that survives grayscale printing (5.2).
3. **Identity is never carried by hue alone either.** Every discipline is also carried by its fixed position, its figure, and its label (Okabe and Ito: redundant coding and direct labels).
4. **Neighbors differ in lightness as well as hue**, so adjacent sectors separate for color-blind readers and in grayscale (Datawrapper: colors should still be told apart printed in black and white). The dark set alternates light and mid values around the sky.
5. **No glow, gradient, drop shadow, or metallic.** Gradient fills and drop shadows are prohibited in the digital identity (BG 16); separation is by hairline (BG 08, principle 02). Gold Foil has no digital token by design (BG 10).
6. **Contrast floor.** Every star fill and line meets 3:1 against its ground (WCAG 2.2, 1.4.11). All text meets AA, targeting AAA (BG 10, accessibility).

### 4.2 The brand's rule, and the exception this needs

The brand palette is eight values, final: "No tints, no shades, no exceptions," and digital surfaces must never contain "any color outside the closed system" (BG 10, BG 16). The closed palette cannot give seven disciplines seven distinguishable hues on one ground: Plum Ink, Aubergine, and Peacock are grounds or near-grounds; Onggi on Plum Ink measures 2.74:1, under the 3:1 floor.

D4 rules that brand-surface rules do not govern internal training, so an internal set is permitted. To keep it inside the brand's own architecture, the discipline hues are proposed as **component-tier tokens**, the tier the guidelines reserve for exceptions "warranted when a role cannot carry the case" (BG 10, token architecture). Each is anchored to a brand primitive where one works. The whole set is `brand.skyweb.discipline_hues`, proposed, for Brandon to confirm or replace (open call 12.1).

### 4.3 Tokens

Naming follows the brand formula `son.[tier].[role].[state]`, with `bg` and `fg` the only abbreviations and the state always last and explicit (BG 10, naming and governance).

**Primitives from the brand (brand facts, BG 10).**

| Token | Value | Use on the skill web |
|---|---|---|
| `son.color.plum-ink` | `#120916` | Dark sky ground; ink on the light variant |
| `son.color.aubergine` | `#2E1F31` | Dark raised panels (detail panel, next-step card) |
| `son.color.bone` | `#EDE7D8` | Primary text on dark; light variant ground |
| `son.color.parchment` | `#DBC9B0` | Secondary text on dark; trunk on dark; print ground option |
| `son.color.jade` | `#8DA982` | Liquid craft, dark variant (Jade is the bar-back accent, BG 04 and BG 13) |
| `son.color.peacock` | `#3E5640` | Liquid craft, light variant ("structure and support", BG 10) |
| `son.color.onggi` | `#804A33` | Anchor for the service hue; not used directly (fails 3:1 on Plum Ink) |

**Proposed primitives (not brand facts; `brand.skyweb.discipline_hues`).** Measured with the WCAG relative-luminance formula and the Machado 2009 color-vision simulation; values rounded.

| Token | Dark variant | Contrast on Plum Ink | Light variant | Contrast on Bone | Anchor |
|---|---|---|---|---|---|
| `son.color.skyweb-clay` (service craft and movement) | `#C8694A` | 5.18:1 | `#9C4428` | 5.20:1 | Onggi, lifted |
| `son.color.skyweb-dusk` (the room and time) | `#A9CBE6` | 11.49:1 | `#4E7AA3` | 3.67:1 | none |
| `son.color.skyweb-ochre` (flavor and perception) | `#C99A3E` | 7.60:1 | `#7A5510` | 5.43:1 | none; flat, never metallic |
| `son.color.jade` / `son.color.peacock` (liquid craft) | `#8DA982` | 7.55:1 | `#3E5640` | 6.52:1 | brand primitives |
| `son.color.skyweb-iris` (teaching and leading) | `#8F74B8` | 4.98:1 | `#6A4A94` | 5.64:1 | Aubergine family |
| `son.color.skyweb-rose` (decisions) | `#F0B3C2` | 11.09:1 | `#A8506D` | 4.22:1 | none |
| `son.color.skyweb-ash` (back of house, held) | `#9C938A` | 6.46:1 | `#4F4843` | 7.27:1 | neutral until the chef signs off |
| `son.color.skyweb-dim` (not yet open, boundaries) | `#756D6D` | 3.87:1 | `#8A8381` | 3.02:1 | Bone over Plum Ink, and the reverse, mixed |

Measured separation of the dark set: the closest pair under deuteranopia simulation differs by CIELAB delta E 10.4, under protanopia 13.5, under tritanopia 11.3; adjacent sectors differ by at least 17.8 under every simulation. The light set's closest adjacent pair under deuteranopia (decisions and back of house) is carried by the held state's dashed outline as well as hue. Re-run the check whenever a hue changes; the check is part of the render adapter's pre-ship pass.

**Semantic tokens (proposed).**

| Token | Dark | Light (wall, print, light mode) |
|---|---|---|
| `son.semantic.bg.sky.default` | Plum Ink | Bone |
| `son.semantic.bg.panel.default` | Aubergine | Parchment |
| `son.semantic.fg.primary.default` | Bone | Plum Ink |
| `son.semantic.fg.secondary.default` | Parchment | Plum Ink, Alpina Light |
| `son.semantic.fg.dim.default` | `skyweb-dim` | `skyweb-dim` |
| `son.semantic.skyweb.trunk.default` | Parchment | Plum Ink |
| `son.semantic.skyweb.thread.selected` | Bone | Plum Ink |
| `son.semantic.skyweb.marker.next` | Bone | Plum Ink |
| `son.semantic.skyweb.boundary.default` | `skyweb-dim` | `skyweb-dim` |

**Component tokens (proposed, the exception tier).** One set per discipline, where `<d>` is the discipline key (`service`, `room`, `flavor`, `liquid`, `teaching`, `decisions`, `boh`):

| Token | Resolves to |
|---|---|
| `son.component.skyweb-<d>.fill.lit` | the discipline hue |
| `son.component.skyweb-<d>.stroke.open` | the discipline hue |
| `son.component.skyweb-<d>.stroke.not-open` | `skyweb-dim` |
| `son.component.skyweb-<d>.line.lit` | the discipline hue |
| `son.component.skyweb-<d>.line.structure` | the discipline hue, drawn at 1px |

### 4.4 Saturation and brightness for state

Brand primitives have no tints (BG 10), so the skill web does not express state by fading a hue. State is expressed by how much of the shape is filled and how the stroke is drawn, in the full hue:

| State | Fill | Stroke | Line to parent |
|---|---|---|---|
| Lit | Solid, discipline hue | none | Solid 1.5px, discipline hue |
| In practice | Lower half filled, discipline hue | 1.5px, discipline hue | Solid 1px, discipline hue |
| Open | none (ground shows through) | 1.5px, discipline hue | Solid 1px, discipline hue |
| Not yet open | none | 1px dashed, `skyweb-dim` | Dashed 1px, `skyweb-dim` |
| Structure (wall map, Trainual map, role mode off-thread) | none | 1px, discipline hue | Solid 1px, discipline hue |

The only "dimmed" value is `skyweb-dim`, a single proposed token, used for not-yet-open stars and boundaries. It clears 3:1 so a not-yet-open star is still readable: it is future, not failure.

### 4.5 Dark and light variants

- **Dark (default for the live page and phone).** Plum Ink ground, the brand's hero dark (BG 10). Open call 12.4 asks whether Aubergine is the better ground for an internal surface.
- **Light (wall map, print, and the page's light mode).** Bone ground, the cooler light surface (BG 10), or Parchment for print where warmth is wanted. All lines and text in Plum Ink; discipline hues from the light column.
- The page honors the operating system's color scheme and offers a manual switch. Both variants are tested on a physical device and in print proof, not in the design file (Web and UI seat).

---

## 5. Node grammar

### 5.1 Shapes by kind

Every shape is a single closed path, silhouette first, legible filled or hollow, the brand's rule for any icon (BG 08, iconography). No icon library is used (BG 08, BG 16).

| Kind | Learning job (`modality-library.md`) | Shape | Size, constellation zoom | Size, wall map |
|---|---|---|---|---|
| Knowledge | know, find | Circle | 10px | 5mm |
| Movement drill | do, hold | Square | 10px | 5mm |
| Decision | decide | Diamond (square on its point) | 12px | 6mm |
| Signature performance | do plus decide at tempo | Four-point star | 22px | 12mm |
| Teaching | teach | Hexagon | 14px | 7mm |
| Library | know | Capsule, horizontal | 14 by 8px | 7 by 4mm |
| Bridge | any | Circle split on the boundary axis, one hue per half | 14px | 7mm |
| Trunk | any | The shape of its kind, in the trunk color | as above | as above |

Size is grade: the signature star is the largest mark in its figure, the star people plan toward (Path of Exile's notables and keystones are larger; Grim Dawn's celestial-power stars are brighter). Only one signature star per constellation.

A signature star's figure lines draw in from the drills and decisions that feed it, so the picture teaches the rule that drills and decisions are practiced apart and merge in the performance.

### 5.2 States

Section 4.4 gives fill and stroke. Additional marks, each a distinct shape so none relies on color:

| Mark | Meaning | Drawing |
|---|---|---|
| Maturing | Released, reads still maturing (D10, hospitality-layer stars) | Lit, with a 1px ground-color ring inset inside the fill |
| Recheck due | A house rhythm, never suspicion (`workflow.recheck_cadence`) | Lit, with a small solid dot above the star, 3px, primary text color |
| Held | Chef-gated draft (3.9) | Hollow, 1px dashed, `skyweb-ash`; the brand's hollow mark for held items (BG 17) |
| New since your last visit | A star lit at close since the person last opened the page (D12) | A text note in the next-step card, shown once; the star itself is simply lit |

### 5.3 The next-step marker and selection

- **Next step.** Exactly one per person. A 1px ring in the next-step color, 6px outside the star, with a short hairline leader to the label "Next". It does not pulse or animate (BG 16: no pulse). If the next step has a booking link waiting (D13), the label reads "Next: book your practical" and the detail panel carries the link.
- **Selected.** A 1.5px ring in the primary text color, 3px outside the star, and the detail panel opens. Selection and next step can coincide; the rings nest.
- **Thread ring.** In role mode, each required star gets a 1px ring in the thread color, 4px outside the star, and a small depth tick if the role requires the star at a stated depth.
- **Hit area.** Every star has a 44 by 44px hit area on touch surfaces, whatever its drawn size (Web and UI seat). Where hit areas overlap, a tap opens a short chooser list rather than guessing.

---

## 6. Typography and labels

### 6.1 Faces and sizes

The brand's three typefaces, and only those (BG 09: "Three typefaces. The ceiling is absolute").

| Role on the skill web | Face and level (BG 09) | Digital size | Wall map size (proposed) |
|---|---|---|---|
| Page title | GT Sectra Display Medium, section header | 36 to 48px | 72pt |
| Discipline name | GT Sectra Standard Regular, subhead | 22 to 30px | 36pt |
| Constellation name | GT Sectra Standard Regular, subhead | 22px | 24pt |
| Star label | GT Alpina Fine Standard Regular, menu descriptor | 13 to 15px | 14pt |
| Ring label, legend, fine detail | GT Alpina Fine Standard Light, fine detail | 11 to 12px | 10pt |
| Detail panel body | GT Alpina Fine Standard Regular, body | 14 to 16px | not shown |
| Next-step card line | GT Alpina Fine Standard Light, lead | 16 to 20px | not shown |
| Any Hangul | Sandoll Myeongjo, 10 to 15 percent larger than the paired Latin (BG 09, rule 3) | | |

- Fallback stacks: GT Sectra, then Cormorant Garamond, then Georgia; GT Alpina, then Source Serif 4, then Georgia (BG 09). Noto Serif KR is prohibited (BG 09).
- Sentence case everywhere. Uppercase only for a single-line eyebrow (BG 06, BG 09); the skill web needs none, so it uses none.
- Detail panel measure capped at 65 characters (BG 09).
- Web embedding of GT Sectra and GT Alpina needs a web license: `tool.web.font_license`, proposed binding (open call 12.5).

### 6.2 Label rules that prevent clutter

Labels are placed, never scattered. Each label sits at one of four fixed offsets from its star (right, left, below, above, tried in that order), never on a line, and never rotated.

| Zoom | Labels shown |
|---|---|
| Sky | Discipline names only, set horizontally just outside the rim at each sector's center; the word "Trunk" at the center. Nothing else. |
| Constellation | Constellation name; then star labels by priority until the next would collide: selected, next step, signature, in practice, lit, open, not yet open. Ring names in the legend strip, not on the sky. |
| Star | No new labels on the canvas. Everything else goes in the detail panel. |
| Role mode (any zoom) | The role name at its door and labels for the required stars only. |

- A dropped label is never truncated with an ellipsis on the canvas. It is dropped whole and appears when the star is selected.
- Search (7.3) labels every matching star, overriding priority, and never fades other stars below `skyweb-dim`.

### 6.3 Naming conventions

- **Stars** are capabilities, named as a verb phrase, in sentence case, in the library voice held by the Educational Materials Author and Editor against BG 11 (Verbal Identity): "Reads the table before the approach," not "Table reading module." A good skill includes a verb (Kraj, GDKeys).
- Canvas label: the short form, at most 28 characters (proposed). The full name lives in the detail panel.
- No module IDs, role titles, figures, or times on the canvas.
- Korean terms appear without gloss on the canvas; their meaning appears in the detail panel from the founder glossary, `founder.glossary.<term>` (D23).
- **Disciplines** carry D29's working names until Brandon renames them.
- **Constellations** are named for their figure ("The vessel"), proposed per figure, Brandon's call (open call 12.3).
- Forbidden-lexicon words (BG 11) never appear in any name.

---

## 7. Motion and interaction

### 7.1 What may animate

Motion marks state change only, at the brand's three durations, standard easing, with `prefers-reduced-motion` honored (BG 16).

| Change | Duration | Reduced motion |
|---|---|---|
| Selection ring appears | 100ms | Instant |
| Filter, search, or role thread applies | 200ms | Instant |
| Zoom between levels | 400ms | Cut |
| A newly lit star fills, once, on the first visit after close | 400ms | Instant |

Never: pulse, bounce, twinkle, drifting stars, parallax, fade-up on scroll, confetti, particle trails, or animated lines "flowing" to a star (BG 16).

### 7.2 Zoom levels

Three discrete levels. Scroll, pinch, and double-tap snap between them; the geometry never changes, only the level of detail.

| Level | Shows | Question it answers |
|---|---|---|
| Sky | Trunk; every figure's lines; signature stars and bridges only; discipline names; the person's lit figure segments | Where is everything, and where am I lit? |
| Constellation | One discipline sector filling the view, its neighbors' edges visible; all its stars, states, library band | What is in this discipline, and what is open to me? |
| Star | The star centered, its parents and children, the detail panel | What is this, how does it light, and what do I do now? |

The detail panel gives: the full name; kind and depth; what lights it (the gate spec in plain words); its state for this person; the modules that feed it; the booking link when ready (D13); prerequisites not drawn as lines; the roles that require it.

### 7.3 Selection, search, and role highlight

- **Selection** opens the detail panel; one star at a time.
- **Search** matches star names, disciplines, and roles, and marks matches with the selection ring and a label, the fix Grim Dawn's developers added for new players and the way players navigate Path of Exile.
- **Role highlight** is a control listing roles; choosing one draws its thread (3.7), and choosing it again clears it. One at a time.
- **Interest.** A person can mark a star "I am interested," which suggests it as a next step when nothing required is open. Interest is private and never counts toward anything (D7 logic: nothing unrecorded gates anything).

### 7.4 The default personal view

The Duolingo lesson: learners stall when a map does not also answer "what do I do next" (Duolingo, 2022).

1. The page opens on a **next-step card** above the sky: the next star's name, why it is next (required by your role, or your interest), and the one action (start the module, or book the practical).
2. Below it, the sky opens at **constellation zoom** on the next step's constellation, with the trunk edge visible.
3. If there is no next step, the page opens at sky zoom with one line: "Choose a star to set your next step."
4. Nothing on the default view counts: no totals, no progress bars across the sky. Progress appears only against the person's own chosen or required thread, as lit stars on that thread.

### 7.5 Phone behavior

- Portrait first. The next-step card sits at the top; the sky sits below it.
- At constellation zoom, one discipline fills the width; a horizontal swipe moves to the neighboring discipline in sector order, so the ring is walked, not scrolled.
- Pinch out to sky; tap a sector at sky zoom to enter it.
- The detail panel is a bottom sheet with a fixed height at first, expandable.
- No hover-dependent information anywhere.
- An **accessible list view** mirrors the sky: disciplines, then constellations, then stars with their state in words. It is a full equivalent, not a fallback, and it is what screen readers get.
- Map data refreshes at close (D12), never live during service.

---

## 8. Surfaces

| Surface | Shows | Hides |
|---|---|---|
| **Live personal page** | Everything in sections 3 to 7: structure, the person's own states, next step, booking link, role threads, search, detail panel | Everyone else's states; any count or comparison; any share control |
| **Phone view** | The same data as the page, in the phone behavior of 7.5 | The same as the page |
| **Wall map** (back of house) | The whole sky in the light variant and the structure state; discipline, constellation, and signature star names; bridges; role doors labeled; a legend of shapes, rings, and hues with names; small multiples beside the sky, one per role, each showing that role's thread alone, the way a transit map lists lines | Every personal state, every name of a person, next-step marks, library band labels if they crowd (the band stays drawn) |
| **Trainual static map** | The wall map, exported as an image page | The same as the wall map |
| **Print** | The wall map at size; a single-discipline sheet per constellation for teaching use | Personal states always |

- The wall map is regenerated only when the structure changes, and never shows dates of who lit what.
- The wall map is a physical surface: its mounting, size, and material route to the Environmental and Signage seat through the Design Director. Whether it carries the 선 glyph is open call 12.10.
- The Trainual map is an image, so it records nothing; the live page is where personal state lives (`adapters/trainual.md`).

---

## 9. Generation rules

### 9.1 Data model

The structure lives in this repo and is the only source of structure; surfaces render from it and never define structure themselves. Personal state never lives in this repo.

```yaml
discipline:
  id: liquid                    # stable key; also the token key <d>
  name: Liquid craft            # D29 working name
  order: 4                      # position clockwise from the twelve o'clock boundary
  hue: son.color.jade           # a brand.skyweb.discipline_hues value
  status: active                # active | draft-chef-gated
  constellations: [liquid-bar, liquid-coffee]

constellation:
  id: liquid-bar
  discipline: liquid
  name: The vessel              # proposed, open call 12.3
  figure_template: vessel       # see 9.4
  version: 1                    # bumps on a split or template change

star:
  id: liquid-bar-007            # stable; never reused
  name: Builds a drink to spec at tempo   # verb phrase; full name
  label: Builds to spec at tempo           # canvas label, 28 characters maximum
  kind: signature               # knowledge | drill | decision | signature | teaching | library
  discipline: liquid
  constellation: liquid-bar
  depth: 3                      # 1 to 5, or L for the library band
  parents: [liquid-bar-003, liquid-bar-004]   # drawn up to 3 lines; the rest listed
  modules: [BEV-004, BEV-006]   # catalog ids that feed this star
  gate_spec: gates/liquid-bar-007.md          # what lights it (D8, D10, D18)
  unlock: mastery               # time | mastery | both (D2)
  hospitality_layer: false      # true shows the maturing mark when lit (D10)
  chef_gated: false             # true draws the held state (3.9)
  capability_test: >            # the filler guard: the on-shift capability, in one sentence
    Can build any drink on the current list to spec during a full service.

bridge:
  id: bridge-flavor-liquid-01
  name: Calibrates palate across food and drink
  disciplines: [flavor, liquid] # must be adjacent in sector order
  depth: 2
  requires: [flavor-005, liquid-bar-002]
  modules: []
  gate_spec: gates/bridge-flavor-liquid-01.md

role:
  id: bartender
  title: "{{bind:people.role_title.bartender}}"
  door: liquid                  # the trunk door the thread starts from
  required:
    - {star: liquid-bar-007, depth: 3}
    - {star: flavor-005, depth: 2}
  gates: [G1, G2, G3, G4]
```

The live page joins this structure with two outside sources, each bound: Trainual progress for "in practice" (`tool.lms.api_access`) and the gate record for "lit" (`tool.forms.gate_record`). It is hosted and signed in through `tool.web.host` and `tool.web.auth` (proposed bindings, research section 4.8).

**Validation before any render** (a check the render adapter runs, proposed):
- Every star has a `capability_test` and a `gate_spec`, and at least one module or a library conversation. No capability, no star.
- No constellation exceeds its maximum; no star draws more than three lines; every bridge joins adjacent disciplines.
- Every role's required stars exist; every thread is connected from its door.
- Every hue passes the contrast and color-vision check in 4.3.

### 9.2 Coordinates

All geometry is computed in one unit disc, center (0, 0), rim radius 1.0, then scaled to each surface. Angles run clockwise from twelve o'clock.

| Radius token | Value | Status |
|---|---|---|
| `skyweb.radius.trunk-inner` | 0.06 | proposed |
| `skyweb.radius.trunk-outer` | 0.12 | proposed |
| `skyweb.radius.door` | 0.16 | proposed |
| `skyweb.radius.ring-1` to `ring-5` | 0.30, 0.44, 0.58, 0.72, 0.86 | proposed |
| `skyweb.radius.library` | 0.95 | proposed |
| `skyweb.sector.gutter` | 0.06 of the sector's angle, each side | proposed |

### 9.3 Deterministic layout procedure

1. **Sectors.** With N disciplines, each sector spans 360 / N degrees. Sector i (by `order`, from 0) spans from i times 360 / N to (i + 1) times 360 / N, measured clockwise from twelve o'clock, so a boundary always sits at twelve o'clock and no sector owns the top.
2. **Sub-sectors.** A discipline with k constellations divides its sector into k equal sub-sectors, in constellation id order.
3. **Doors and root lines.** Each discipline's door sits on the door radius at its sector's center angle. Its root line runs from the door to the foundation star of its first constellation; further constellations root from that foundation star, not from the trunk.
4. **Slots.** Each constellation's figure template (9.4) lists slots in fill order. Each star, taken in id order, takes the first free slot on its depth ring. Stable ids and fill order mean a new star never moves an existing one.
5. **Overflow.** A star with no free template slot on its ring takes an overflow lane, alternating right then left of the outermost used slot at the minimum spacing. Two overflow stars on one ring trigger the split check (3.8).
6. **Bridges.** A bridge sits on the boundary angle between its two disciplines, at its depth ring. Two bridges at the same boundary and ring offset radially by half a ring step, outer one second.
7. **Library.** Library stars sit on the library radius in their sector, spaced evenly across the sector's inner span, in id order.
8. **Trunk.** Trunk stars fill the inner then outer trunk circles evenly, in catalog order, starting at twelve o'clock.
9. **Lines.** Draw each star's first three parents as straight lines. A line that would cross another figure's line is rerouted as a single bend at 45 degrees, the transit-map rule (Beck limited his lines to straight runs and 45 degree angles); if it still crosses, it is dropped to the detail panel.
10. **Labels.** Place labels by the priority and offsets in 6.2; drop on collision.
11. **Check.** Run the spacing, contrast, and validation checks; fail the render on any error rather than ship a crowded sky.

The same coordinates serve every surface. Only scale, variant, and the level of detail change.

### 9.4 Figure templates

A figure template is a named, ordered list of slots `(ring, offset)`, where offset is a fraction of the sub-sector's half-angle, from -1 to 1. Slot order is chosen so the figure reads from its first stars: the spine first (foundation to signature on offset 0), then the limbs that make the silhouette. Example, the shape of a vessel (a placeholder for the design team, not a decided figure):

```yaml
figure_template:
  id: vessel
  slots:            # fill order
    - {ring: 1, offset: 0.0}     # foot
    - {ring: 3, offset: 0.0}     # signature, the vessel's body center
    - {ring: 2, offset: -0.35}
    - {ring: 2, offset: 0.35}
    - {ring: 3, offset: -0.6}    # the widest point of the body
    - {ring: 3, offset: 0.6}
    - {ring: 4, offset: -0.3}    # shoulder
    - {ring: 4, offset: 0.3}
    - {ring: 5, offset: 0.0}     # the lip, the teaching star
    - {ring: 2, offset: 0.0}
    - {ring: 4, offset: 0.0}
    - {ring: 1, offset: -0.3}
```

The Design Translating Team proposes one template per discipline (section 11); Brandon picks; the chosen templates are committed here.

---

## 10. Complexity guard

Grim Dawn's devotion map is loved and found overwhelming. Players name why: transparent figure art of random sizes overlapping ("signs that start to mix with one another"), a small constellation hidden under a large one, "way too much stuff presented on the same screen," and having to click every star to learn what a constellation gives. They asked for color coding by affinity; the developers added search (Steam threads, verified-secondary as sentiment). Valhalla shows the other side: fog made planning impossible, and filler nodes made the chart "pointless make work" (Kotaku; Scientific Gamer).

**Keep from Grim Dawn:** a shared start at the center (the Crossroads), constellations as named figures, completing inner work opening outer work, bridges as affinity between neighbors, brighter stars for the stars that matter.

**Keep from Valhalla:** color batching by direction, and a reset that costs nothing (interest moves freely; lit stars stay lit, subject to recheck).

**Leave behind:** figure art drawn over the stars, figures of random size, all detail on one screen, tooltip hunting, fog, filler, and any second currency.

**The guard, as rules:**

1. **Sky-level ceiling.** At sky zoom, at most one signature star per constellation plus bridges, and at most 40 marks in total (proposed). Everything else waits for constellation zoom.
2. **Figure lines, not figure art.** The figure is the lines between stars. No illustration is drawn behind or over the sky.
3. **Equal sectors, capped constellations** (3.8), so no figure buries another.
4. **One of each.** One next step, one selected star, one role thread at a time.
5. **Summary before stars.** Each constellation's detail at constellation zoom opens with one line naming what it builds toward (its signature star), so nobody clicks every star to find out.
6. **Search and the list view** for anyone who wants to find rather than browse.
7. **The filler test** at validation (9.1): no capability, no star.

---

## 11. Brief for the Design Translating Team

Routed through the Design Director. The Design Brief Translator turns this into briefs, one per artifact; the Platform Prompt Specialist writes any tool prompts. This section is the brief input, not a prompt.

**Artifacts (one brief each).**
1. Live page, dark, sky zoom: whole sky, sample lit states for one fictional person.
2. Live page, dark, constellation zoom on liquid craft, with the next-step card and detail panel open.
3. Phone, portrait: next-step card, constellation zoom, bottom sheet.
4. Wall map, light variant, structure only, with legend and role small multiples.
5. Figure studies: two candidate figure templates per discipline, drawn in stars and lines only.

**Function.** Let a team member see the whole program, choose a direction, and know their next step, without ranking anyone. The single most important thing: the first view says "here is your next step" and the sky reads as seven recognizable figures, not a wheel of dots.

**Audience and context.** Sŏn's front-of-house, beverage, host, and back-of-house team, mostly on phones, before or after a shift, never during service; and anyone passing the wall in back of house, at a few steps' distance.

**Register (a compound).** Internal and peer-to-peer; quiet and legible; the dinner-room register of restraint (BG 01: "Korean restraint. Texas warmth. Polished but playful."), not game spectacle. A star chart made by a careful cartographer, not a space game.

**Content to carry verbatim.** D29 discipline names; ring names from 3.5; sample star names clearly marked as sample, never presented as real modules; role titles as placeholders.

**Constraints.** Every token, size, and rule in sections 3 to 7; the three brand typefaces (BG 09); the brand palette plus the proposed skyweb hues, marked proposed; the "must never" list in section 1; no glow, gradient, shadow, metallic, background stars, nebula, or texture; no icon library; no brand marks as figures; sentence case; no em dashes; customer, never the other word. Hand the code tools the token block in 4.3, not adjectives (Web and UI seat).

**References, this but not this.**

| Reference | Bring through | Leave behind |
|---|---|---|
| Grim Dawn devotion map | Figures as constellations, shared center, bright stars that matter, affinity between neighbors | Painted figure art, overlapping transparent art, random figure sizes, all-at-once density |
| Assassin's Creed Valhalla skill chart | One color per direction, batching at a glance | Fog, filler nodes, the glowing space-game finish |
| H. A. Rey's constellations | Lines that make the figure look like its name | Children's-book illustration style |
| Harry Beck's Underground diagram | Colored lines, straight runs and 45 degree bends, even spacing, legibility over literal geometry | A grid of stations; the transit look itself |
| Cheonsang Yeolcha Bunyajido (reference only, open call 12.9) | The polar chart, concentric circles, a sky set down with care | Any direct quotation of the stone chart, its figures, or its script |

**Mechanism statement (for the Translator to refine).** Readability comes from few marks with strong grouping: hue batches a discipline, lines make a figure, size marks the star that matters, and empty ground does the rest.

**Success criteria.**
- From the sky view, a new viewer can point to seven distinct figures and name which is which from hue and label alone within a glance, and again in a grayscale print.
- The next step is the first thing read on the default view.
- Nothing on any artifact reads as a ranking, a score, or a comparison.
- Every artifact passes the Web and UI last-10 percent checklist (contrast in browser, on a physical device) or the Editorial and Layout checklist for the wall map.

**Routing.** Live page and phone: Web and UI Specialist. Wall map and print: Editorial and Layout Specialist, with Environmental and Signage for the physical mount. Figures and the hue exception: Brand Identity Specialist reviews against canon. Imagery: none; the skill web uses no photography or generated imagery.

---

## 12. Open calls for Brandon

1. **Discipline hues outside the closed palette.** Approve the proposed component-tier set in 4.3 (`brand.skyweb.discipline_hues`), replace it, or restrict the web to the eight brand values and carry disciplines by position and figure alone (which loses the batching you liked in Valhalla).
2. **One mixed value for "not yet open."** `skyweb-dim` is a mix of two brand values, which the palette's no-tints rule forbids on brand surfaces. Approve it for this internal surface, or choose a dashed stroke in Parchment instead.
3. **Figures and constellation names.** Pick one figure per discipline from the design team's studies; name each constellation.
4. **Dark ground.** Plum Ink (the brand's hero dark) or Aubergine for an internal surface.
5. **Web fonts.** A web license for GT Sectra and GT Alpina (`tool.web.font_license`, proposed); until then the page uses the brand's fallback stacks.
6. **What the surface is called.** "Skill web" is the working name.
7. **Back of house hue.** Neutral ash while held; a hue assigned when the executive chef signs off.
8. **Sector order.** D29's order is soft-locked. Confirm after the module discovery research, and revisit if non-adjacent crossings become common.
9. **The Joseon star chart as a reference.** Whether a Korean cultural reference belongs in the design team's brief at all is a cultural call, and yours.
10. **The 선 glyph on the wall map.** The brand requires the glyph on every daypart surface (BG 07); whether an internal back-of-house map counts is yours to say.
11. **Ochre for flavor and perception.** Flat ochre is not Gold Foil, but it sits near amber, which the first concept used. Keep it or choose another.
12. **Limits.** Twelve stars per constellation, three constellations per discipline, a forty-mark sky ceiling: confirm, with the Curriculum & Program Architect.

Not open here, already decided: no sharing (D31), privacy of position (D12), lighting only from the gate record (D8), structure-only wall map (D12).

---

## Sources

Labels: **VP** verified-primary (read on the maker's or publisher's own page, or the canonical document); **VS** verified-secondary (read in independent coverage, a reference work, or a public dataset I opened); **LO** lead-only (seen in a search summary, or the page refused the fetch); **UV** unverified (inference).

| # | Source | Used for | Label |
|---|---|---|---|
| 1 | Brand and Experiential Guidelines v3.0, Box `2281626080747`, sections 01, 04, 06 to 11, 13, 16, 17 | Palette, token architecture and naming, accessibility pairs, type system and sizes, stacks, case, iconography, motion, prohibitions, held mark | VP (canonical, D26) |
| 2 | Grim Dawn official guide, grimdawn.com/guide/character/devotion | Crossroads start, starting star, affinity accumulates and gates constellations, brighter stars are celestial powers, refunds | VP |
| 3 | Grim Dawn affinity colors (ascendant purple, chaos red, eldritch green, order white, primordial blue) and tier requirements, via search summaries of the official wiki | Color batching by affinity; tiering | LO (wiki refused the fetch) |
| 4 | tednaleid/grimdawn-devotions, github.com | Each constellation a tree of stars rooted at a starting star; every star has a position on one shared canvas; figure art placed separately | VS |
| 5 | Steam, Grim Dawn discussions "Devotions are overwhelming" and "So i happened to open the Devotion tab and get overwhelmed" | Why players find it complex; asked-for color coding; search as the fix | VS (player sentiment) |
| 6 | Ubisoft, "Assassin's Creed Valhalla: which path is right for you?" | Wolf blue, Bear red, Raven yellow; gear sets match path color; free reset | VP |
| 7 | Kotaku, "How to easily uncover every skill in Assassin's Creed Valhalla" | Fog, constellation of one ability and stat nodes, reveal workaround | VS |
| 8 | Scientific Gamer, "Thoughts: Assassin's Creed Valhalla" | "Cargo-cult implementation," "pointless make work" | VS (critic opinion) |
| 9 | Ry Stevens, "A starving skill tree," Medium; TechRaptor guide; GameSpot guide | Filler criticism; constellations of about ten unlocks | LO (refused fetches; search summaries) |
| 10 | Path of Exile official passive tree planner | Class starts; notables larger; keystones; search, highlight shortest paths | VP |
| 11 | Wikipedia, "The Stars: A New Way to See Them" | Rey redrew figures to look like their names because the traditional ones were hard to remember | VS |
| 12 | "The network signature of constellation line figures," PLOS One, journal.pone.0272270 | Constellation figures are sparse, mostly chains and trees; East Asian figures simplest | VS (abstract and summary read) |
| 13 | Wikipedia, "Cheonsang Yeolcha Bunyajido" | Joseon stone star chart, polar projection | VS |
| 14 | Search summaries on IAU boundaries and chart conventions (dot size for magnitude, stepped boundaries) | Region-as-boundary; size as grade | LO |
| 15 | Wikipedia, "Harry Beck" | Colored routes, straight lines and 45 degree angles, even spacing, connections over geography | VS |
| 16 | W3C, Understanding WCAG 2.2, 1.4.1 Use of Color and 1.4.11 Non-text Contrast | State not by color alone; 3:1 for graphics | VP |
| 17 | Okabe and Ito, "Color Universal Design," jfly.uni-koeln.de/color | Redundant coding with shape and line type; direct labels | VP |
| 18 | Datawrapper, "A detailed guide to colors in data vis style guides" | Categorical colors differ in lightness, survive grayscale; test with a color-blind simulator | VS |
| 19 | Search summaries on categorical palette limits | Seven as a conservative category maximum | LO |
| 20 | Machado, Oliveira, and Fernandes, 2009, color-vision-deficiency simulation matrices, as implemented for this file | Separation figures in 4.3 | UV (own computation; re-run on any change) |
| 21 | Duolingo blog, 2022-05-06, and the Khan Academy Knowledge Map, via `research/phase2-working/11-game-skill-trees.md` | Next step first | VP (as recorded there) |
| 22 | Nicolas Kraj, GDKeys, via the same research file | A good skill includes a verb | VP (as recorded there) |

Repo inputs: `framework/system-design.md` (D2 to D5, D7, D8, D10 to D13, D18, D23, D26, D28 to D31), `research/phase2-working/11-game-skill-trees.md`, `research/intake-2026-09.md` group 2, `research/starting-structure-2026-09.md` (node states, supervision levels, gates), `framework/modality-library.md`, `adapters/trainual.md`. Seat judgment applied, not quoted: Design Director, Web and UI Specialist, Brand Identity Specialist, Editorial and Layout Specialist, Design Brief Translator.
