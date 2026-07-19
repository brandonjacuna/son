---
# DESIGN.MD — SŎN
# Future Nostalgia Hospitality Group
# 207 E St. Elmo Rd, Austin, Texas 78745
# Brand Guidelines v1.0 (updated) + Section 14 Deck Governing Principles
# Version: 3.0
# This file governs all AI-assisted design for the Sŏn brand and experiential guidelines deck.

brand:
  name: "Sŏn"
  glyph: "선"
  fallback-romanization: "Son"  # Never "Sohn" or "Seon"
  positioning:
    - "Korean restraint"
    - "Texas warmth"
    - "Polished but playful"
  positioning-note: "Three equal, unordered values. No hierarchy between them. Not a phrase — a set of governing qualities."
  location: "207 E St. Elmo Rd, Austin, Texas 78745"
  language-constant: "'Customer' is the brand's word. 'Guest' is not used in any context."

# ─────────────────────────────────────────────────────────────────────────────
# COLOR SYSTEM
# ─────────────────────────────────────────────────────────────────────────────

colors:
  palette-size: 8  # Eight colors. No tints. No shades. No exceptions.

  primitives:
    parchment:  { hex: "#DBC9B0", token: "son.color.parchment",  role: "Primary surface — warm" }
    bone:       { hex: "#EDE7D8", token: "son.color.bone",        role: "Secondary light surface — cooler neutral" }
    plum-ink:   { hex: "#120916", token: "son.color.plum-ink",    role: "Hero dark — dinner environment" }
    aubergine:  { hex: "#2E1F31", token: "son.color.aubergine",   role: "Secondary dark — late night environment" }
    jade:       { hex: "#8DA982", token: "son.color.jade",        role: "Signature sage — morning and late-night accent only" }
    peacock:    { hex: "#3E5640", token: "son.color.peacock",     role: "Deep green — structural and supporting hierarchy" }
    onggi:      { hex: "#804A33", token: "son.color.onggi",       role: "Earthen clay — Dosi" }
    pale-jade:  { hex: "#C8D4BE", token: "son.color.pale-jade",   role: "Derived morning token — NOT a palette color" }
    gold-foil:
      digital-rep: "#BC9A5C"
      physical:    "Pantone 871C / Kurz Luxor 220"
      token-paths: "son.menu.color.foil.physical ONLY — no flat-fill token exists by design"
      rule:        "Physical production specification only. NEVER as flat digital fill. In deck contexts: referenced as a named material, never simulated."

  daypart-themes:
    morning:
      light:        "#C8D4BE"  # pale-jade
      dark:         "#3E5640"  # peacock
      text-primary: "#120916"  # plum-ink — NEVER peacock (WCAG enforcement)
      border:       "#3E5640"  # peacock — border/icon only
      note: "Peacock on Pale Jade: display above 18pt/14pt bold and non-text ONLY. Prohibited for body text."
    dosi:
      light:        "#DBC9B0"  # parchment
      dark:         "#804A33"  # onggi
      text-primary: "#120916"  # plum-ink
    dinner:
      surface-primary: "#120916"  # plum-ink — the ground, always
      surface-layer:   "#2E1F31"  # aubergine — layered over plum-ink
      text-primary:    "#EDE7D8"  # bone
      accent:          none       # no accent in dinner register
      jade-restriction: "Jade does not appear in son.theme.dinner. Not as text, not as accent, not as glyph color, not as decoration. Jade appearing with Aubergine or Plum Ink as a pairing in any composition is a named failure mode."
    luxe:
      surface-primary: "#120916"  # plum-ink
      surface-layer:   "#2E1F31"  # aubergine
      text-primary:    "#EDE7D8"  # bone
      accent:          "#8DA982"  # jade — enters bar back at late-night transition only

  jade-context-rule: "Jade is a morning color and a late-night transition accent specifically at the bar back. It does not enter the dinner register at any time. Jade paired with Aubergine or Plum Ink as the two dominant visual colors in any composition is a named failure mode regardless of how the pairing arises."

  accessibility:
    standard: "WCAG 2.2 AA minimum. AAA target for type-heavy surfaces."
    enforcement: "Architectural — restricted combinations have no token path."
    restricted-pairs:
      - "Peacock (#3E5640) on Pale Jade (#C8D4BE) — body/running text: PROHIBITED"
      - "Gold Foil on Parchment — text at any size: PROHIBITED"
      - "Jade (#8DA982) on Bone (#EDE7D8) — text: PROHIBITED; decorative/non-text: approved"
      - "Onggi (#804A33) on Parchment (#DBC9B0) — display above 18pt/14pt bold ONLY"
    approval-condition: "All final color approvals under 2700K CRI 95+ installed lighting"

  prohibited:
    - "New colors beyond the palette of 8 + pale-jade"
    - "Tints or shades of any palette color"
    - "Gold Foil as flat digital fill — ever"
    - "Purple gradients of any kind"
    - "Blue as any accent"
    - "Jade and Aubergine as the two dominant colors in any composition"

# ─────────────────────────────────────────────────────────────────────────────
# TYPOGRAPHY
# ─────────────────────────────────────────────────────────────────────────────

typography:
  system: "Three typefaces. This ceiling is absolute."

  display-wordmark:
    family:     "GT Sectra Fine"
    foundry:    "Grilli Type"
    year:       2013
    weight:     "Book"
    subfamily:  "Fine"
    fallbacks:  ["Cormorant Garamond", "Georgia"]
    character:  "Calligraphic and blackletter construction. Warm editorial register. Not on Google Fonts."
    restrictions:
      - "Fine subfamily ONLY — Display and Standard prohibited for wordmark"
      - "Book weight ONLY — no lighter, no heavier"
      - "No all-caps at any scale"
      - "No italic used decoratively"
      - "Not below scale where calligraphic construction collapses"

  body:
    family:     "GT Alpina Fine Standard"
    foundry:    "Grilli Type"
    year:       2020
    weight-default: "Regular"
    weight-lead:    "Light"
    fallbacks:  ["Source Serif 4", "Georgia"]

  korean:
    family:     "Sandoll Myeongjo (산돌명조)"
    foundry:    "Sandoll, Seoul"
    usage:      "All Hangul. All contexts. No exceptions."
    scale-adjustment: "10–15% larger than paired GT Sectra for optical equivalence at viewing distance"
    restrictions:
      - "Noto Serif KR: PROHIBITED in all public-facing contexts"
      - "No mixing with any other Korean typeface on same surface"

  scale:
    wordmark:        { family: "GT Sectra Fine Book",             print: "Vector",   digital: "Vector" }
    headline:        { family: "GT Sectra Display Regular",       print: "48–72pt",  digital: "60–96px" }
    section-header:  { family: "GT Sectra Display Medium",        print: "28–36pt",  digital: "36–48px" }
    subhead:         { family: "GT Sectra Standard Regular",      print: "18–24pt",  digital: "22–30px" }
    eyebrow:         { family: "GT Sectra Standard Regular CAPS", print: "9–11pt",   digital: "11–13px" }
    lead:            { family: "GT Alpina Fine Standard Light",   print: "14–16pt",  digital: "16–20px" }
    body:            { family: "GT Alpina Fine Standard Regular", print: "10–12pt",  digital: "14–16px" }
    menu-descriptor: { family: "GT Alpina Fine Standard Regular", print: "9–11pt",   digital: "13–15px" }
    fine-detail:     { family: "GT Alpina Fine Standard Light",   print: "7–8pt",    digital: "11–12px" }

  rules:
    case:      "Sentence case always. UPPERCASE: single-line eyebrow text ONLY."
    measure:   "Body copy capped at 65 characters. Never uncapped above 75."

# ─────────────────────────────────────────────────────────────────────────────
# SPACING, BORDERS, MOTION
# ─────────────────────────────────────────────────────────────────────────────

spacing:
  base-unit: "8px"
  grid:      "8pt"

borders:
  default: "1px hairline"
  prohibited:
    - "2px borders"
    - "Decorative dividers"
    - "Colored left-border accent boxes"
    - "Double rules"

motion:
  durations: { fast: "100ms", standard: "200ms", slow: "400ms" }
  easing:
    standard: "cubic-bezier(0.4, 0, 0.2, 1)"
    enter:    "cubic-bezier(0, 0, 0.2, 1)"
    exit:     "cubic-bezier(0.4, 0, 1, 1)"
  rules:
    - "Motion marks state change — not importance"
    - "No fade-up-on-scroll"
    - "No pulsing or blinking for emphasis"

# ─────────────────────────────────────────────────────────────────────────────
# DECK DESIGN GOVERNING PRINCIPLES — SECTION 14
# This section governs all presentation decks. It overrides any ambient
# assumptions about the brand's environmental register for this format.
# The deck is a document about the restaurant. It is not the restaurant.
# ─────────────────────────────────────────────────────────────────────────────

deck:
  register: "Most editorial expression of the brand. Reference: high-end architecture monographs, Kinfolk, Cereal, Apartamento. Not a hospitality brand presentation."
  audience: "Internal: investors, partners, vendors, operational teams. Never customer-facing."

  background-hierarchy:
    primary-default: "#EDE7D8"    # Bone — default content slide background
    secondary:       "#DBC9B0"    # Parchment — warm variation, secondary content
    section-titles:  "#120916"    # Plum Ink — section title slides ONLY; maximum one per section
    major-callouts:  "#2E1F31"    # Aubergine — major statement slides; maximum two or three per deck
    all-other-colors: "Accent use only — NEVER as slide background"

    rules:
      - "Bone (#EDE7D8) is the default background for the overwhelming majority of slides"
      - "Parchment (#DBC9B0) is the warm variation — secondary content slides"
      - "Plum Ink (#120916) is reserved for section title slides only — one per section maximum"
      - "Aubergine (#2E1F31) is reserved for major statement callout slides — two or three per deck maximum"
      - "NEVER: Aubergine or Plum Ink as background for content slides"
      - "NEVER: more than two consecutive dark-background slides without returning to a neutral"
      - "NEVER: gradient fills of any kind"
      - "NEVER: any color background that competes with the content for attention"

  temporal-arc-rule: "The temporal arc — Jade/Peacock opening the day, deepening to Plum Ink/Aubergine, Jade re-entering at late night — is a sensory environment principle for the restaurant. IT DOES NOT APPLY TO THE DECK. The deck's register is editorial, not environmental."

  layout:
    rule-one-idea: "One primary idea per slide. If two ideas need to appear together, one is subordinate — not equal."
    margins: "Minimum 10% of slide dimension on each side. The deck is not a container to be filled."
    alignment: "Left-aligned or asymmetric layouts read as editorial. Centered layouts read as decorative. Centering is a deliberate choice, not a default."
    asymmetry: "A single column of text on a slide with significant empty space to one side is correct. A balanced two-column grid is a template, not a decision."
    negative-space: "Empty slide margin is held intentionally. A slide that looks underbuilt is disciplined. Ma/Yubaek-ui-mi applies to the deck page as it applies to the physical environment."
    prohibits:
      - "Centered text as a default layout"
      - "Content extending to slide edges"
      - "Multiple competing visual elements at equal weight on one slide"
      - "Decorative frames or borders around content"
      - "Persistent header/footer chrome that adds visual noise without structural function"
      - "Drop shadows on text or images"
      - "Beveled or embossed elements"

  typography-deck:
    headlines: "GT Sectra Fine Book. Large. Generous leading. Does not compete with body copy — stands alone or dominates the upper register clearly."
    body: "GT Alpina Fine Standard Regular or Light. More generous leading than print — decks are read at distance. Tracking slightly open."
    minimum-sizes:
      headline: "48pt equivalent minimum"
      body:     "18pt equivalent minimum — anything smaller is illegible in presentation conditions"
    bullet-rule: "No bullet point forests. Maximum four items in any list. Each item is a complete thought. List does not occupy the entire slide. If content requires more than four items, it requires a different slide approach."
    prose-rule: "A single complete sentence in 72pt GT Sectra Fine Book on a Bone background is more powerful than eight bulleted fragments in 18pt body text. The deck makes arguments, not transmits data."
    no-em-dashes: "Same rule as all brand copy."

  color-in-deck:
    type-on-dark: "On Plum Ink or Aubergine slides: type in Bone (#EDE7D8) or Parchment (#DBC9B0) ONLY. No Jade or Peacock type on dark backgrounds."
    accents: "Jade, Peacock, and Onggi may appear as accent colors — a colored rule, a category label. They are never a dominant element."
    jade-deck-rule: "Jade does not appear as the 선 glyph color throughout the deck. The 선 glyph on light backgrounds (Bone/Parchment) renders in Plum Ink or Peacock — never Jade. Jade appearing everywhere as a structural element was a named failure mode in the first deck generation."
    선-glyph-color:
      on-bone-or-parchment: "Plum Ink (#120916)"
      on-plum-ink-or-aubergine: "Bone (#EDE7D8)"
      never: "Jade (#8DA982) as the 선 glyph color on any slide background in this deck"
    gold-foil: "Not applicable as a digital fill. Referenced as a named material in specification slides only. Never simulated as flat fill or gradient."
    prohibits:
      - "Gold Foil simulated as flat digital fill"
      - "Full-slide color backgrounds on consecutive content slides (dark-to-dark-to-dark)"
      - "More than one accent color in use on a single slide"
      - "Gradient fills of any kind"
      - "Jade as dominant visual color on any slide"
      - "Jade paired with Aubergine or Plum Ink as the two dominant colors — named failure mode"

  images-in-deck:
    sizing: "Full bleed or occupies at least 50% of the slide. Thumbnail photography next to a text block is a PowerPoint default, not a design decision."
    count: "One photograph per slide. Two photographs compete for attention."
    captions: "No captions unless functionally necessary. If required: single short line, GT Alpina Fine Standard Light, small, recessive."
    prohibits:
      - "Stock imagery"
      - "AI-generated imagery"
      - "Photographs with watermarks"
      - "Photograph thumbnails arranged in grids as slide filler"
      - "Any photograph violating Section 10 of the brand guidelines"

  deck-architecture:
    slide-count: "Slide count is not a measure of effort. The question is not 'what else can we add?' but 'what can we remove without losing the argument?'"
    section-dividers: "Plum Ink or Aubergine background. Single line GT Sectra Fine Book in Bone or Parchment. Generous negative space. No decorative elements. No icons. The section title is the entire content of the slide."
    opening-slide: "Brand mark and the single most important thing the deck is for. Nothing else."
    closing-slide: "Direct and complete. A clear call to action or a closing statement. Not a 'Thank you' slide."
    template-avoidance: "The deck should not read as templated. Varied layouts — full-bleed photograph, then single-statement text slide, then spare diagram — read as editorial. Same layout repeated sixteen times reads as a template output."

  deck-govering-test: "Could this slide appear in a premium editorial publication — a monograph, a brand book, a high-end print journal — without embarrassment? If yes: ready. If no: identify what makes it wrong and remove or redesign that element."

  outright-prohibitions:
    - "Full-slide gradient fills"
    - "Drop shadows on text or images"
    - "Beveled or embossed elements"
    - "Decorative frames or borders"
    - "Clip art or icon library illustrations"
    - "Charts with heavy grid lines, unnecessary data labels, or default application styling"
    - "Transitions or animations beyond the simplest fade"
    - "Multiple fonts beyond GT Sectra and GT Alpina"
    - "Any slide that requires the presenter to apologize for or explain — if confusing without narration, redesign the slide"

# ─────────────────────────────────────────────────────────────────────────────
# IDENTITY SYSTEM
# ─────────────────────────────────────────────────────────────────────────────

identity:
  wordmark:
    선-position:  "Centered-below the Latin wordmark. Specific gap. Not right-adjacent. Not integrated into letterforms."
    선-mandatory: "선 appears on every daypart surface at constant scale ratio. Cannot vary. Cannot be exempted."
    responsive:
      primary:    "Full vertical lock-up"
      secondary:  "Latin wordmark alone"
      minimum:    "선 alone — icon and minimum-scale state"

  pattern:
    role:    "Edge and accent scale only — not dominant surface, not ground fill"
    source:  "Structural geometry of the Sŏn wordmark — proportional relationships, curve radii"
    prohibits:
      - "Letterforms or 선 as pattern units"
      - "Wordmark tiled at any scale"
      - "Pattern as dominant surface"
      - "Symmetry as structural default"

# ─────────────────────────────────────────────────────────────────────────────
# VOICE
# ─────────────────────────────────────────────────────────────────────────────

voice:
  language-constant: "'Customer' — absolute, all contexts. 'Guest' is prohibited."
  case:              "Sentence case always. UPPERCASE: single-line eyebrow only."
  prohibited-marks:  "Em dashes. Exclamation points in written brand voice. Emojis in written brand voice."
  binary-tests:
    1: "Names its own effect? → Out."
    2: "Primary noun replaceable by category sibling? → Out."
    3: "Continues past last load-bearing word? → Cut from there."
    4: "Answers a question not yet asked? → Out."
    5: "Could appear unchanged in competitor copy? → Out."
    6: "Sentence two explains sentence one? → One is wrong. Fix that one."
  forbidden-always:
    - "elevated, experiential, innovative, disruptive, authentic, delicious, mouthwatering,
      vibrant, seasonal, chef-driven, hand-crafted, house-made, community-driven, passion,
      journey, curated, farm-to-table, artisanal, crafted, must-try, amazing, incredible,
      thoughtful, intentional, memorable, unforgettable, beautiful, stunning"
    - "barbecue as genre descriptor"
    - "any emoji in written brand voice"
    - "exclamation points in written brand voice"

# ─────────────────────────────────────────────────────────────────────────────
# PHOTOGRAPHY
# ─────────────────────────────────────────────────────────────────────────────

photography:
  ai-generated:  "PROHIBITED on all public-facing surfaces. ABSOLUTE. No exceptions."
  ai-assisted:   "Permitted under Harvard SEAS disclosure tag convention: noise reduction, lens correction, distortion/perspective correction within actual capture geometry ONLY."
  ai-prohibited:
    - "Sky replacement, object generation, background extension, skin synthesis, generative fill"
    - "Artificial patina, texture enhancement, or aging added in post"
  people-rule:   "Present in every frame. Never altered posture, expression, or gaze in response to camera."
  food-rule:     "Only in transactional context. Vessel and hands always present. Food alone: PROHIBITED."
  light:         "Found light only — window light, candlelight, installed 2700K CRI 95+, firelight, ambient outdoor glow"
  light-prohibited: "Strobe, flash, ring lights, softboxes, beauty dishes, reflector panels, any crew-introduced source"
  grain:         "Preserved, not removed. ISO 800–3200 consistent grain is a specification, not a defect."
  artificial-grain: "Applied grain in post is a Jaeyeonmi violation."
  composition:
    - "Decentered — primary element at or outside inner thirds intersection"
    - "Imperfect — horizon not level, visible motion blur, no tripod with plumb line"
    - "Closer than comfortable — move forward until something important is cropped"
  color-grade:
    - "Skin warms to Onggi"
    - "Shadows deepen to Aubergine — not cool blue-black"
    - "Highlights hold in Parchment/Bone"
    - "Outdoor greens hold in Jade/Peacock"
    - "Cooling and blue shadows: PROHIBITED"

# ─────────────────────────────────────────────────────────────────────────────
# SYSTEM ANTI-PATTERNS
# Named failure modes. Never reproduce in any output.
# ─────────────────────────────────────────────────────────────────────────────

anti-patterns:
  jade-everywhere: "Jade appearing as the structural accent color throughout a deck — as 선 glyph color, as eyebrow label color, as status indicator — was the primary failure mode of the first Sŏn deck generation. It produced a jade-and-aubergine pairing that reads as neither the brand nor any of its daypart registers."
  dinner-register-deck: "The deck is not the restaurant interior. Plum Ink and Aubergine as the dominant deck surfaces was the second primary failure mode. The deck lives in a warm editorial register — Bone and Parchment — with dark surfaces controlled and reserved."
  AI-aesthetic-gravity:
    - "Inter or system sans as default typeface"
    - "Purple gradients on white"
    - "Blue as default accent"
    - "Card-based layouts with drop shadows as only spatial differentiator"
    - "Centered hero + three feature cards + testimonials as default page structure"
    - "Fade-up-on-scroll as the only motion language"
    - "Left-border callout boxes with tinted fills"
    - "Lucide icons decorating every content block"
    - "Uniform card padding across content of unequal weight"
  claude-default-register: "Claude defaults to warm cream/off-white backgrounds, editorial serif display, terracotta/amber. The Sŏn system overlaps with this default in some areas. Accept no additions, no tints, no defaults bleeding in from outside the closed palette of 8 + pale-jade."

# ─────────────────────────────────────────────────────────────────────────────
# CULTURAL FRAMEWORKS — ALWAYS TIER 1
# ─────────────────────────────────────────────────────────────────────────────

cultural-frameworks:
  authority: "Tier 1 — overrides all downstream decisions without exception. These three frameworks have veto power over any design decision in this system, regardless of cost, aesthetics, photography, or any other consideration."
  jaeyeonmi:
    name: "자연미 — Beauty of the Natural"
    principle: "Nothing should conceal what it is, where it came from, or how long it has been here."
    deck-application: "The deck does not simulate materials it cannot produce. No digital grain overlays, faux textures, faux foil. If Gold Foil is referenced in the deck, it is named as a physical material — not simulated as a fill."
  ma-yubaek:
    name: "여백의 미 — Beauty of Meaningful Negative Space"
    principle: "Empty space is active, held, intentional. Empty is a specification, not a default."
    deck-application: "A slide that looks underbuilt is not underbuilt — it is disciplined. The empty margin is held. The deck does not fill space because it feels unfinished."
  mahk:
    name: "맛 — Taste as Memory"
    principle: "Specificity is the mechanism of memory. Generic experiences produce Mahk for no one."
    deck-application: "The deck makes specific arguments, not generic ones. A slide that could appear in any hospitality brand presentation has failed the Mahk standard."

---

# RATIONALE — HOW THE SŎN DECK SYSTEM WORKS

## The Single Most Important Correction from v1.0

The first deck was generated in the dinner register — Plum Ink and Aubergine as dominant surfaces. This was wrong. The brand guidelines (Section 14) are unambiguous: the deck is an editorial document. Its primary surfaces are **Bone (#EDE7D8) and Parchment (#DBC9B0)**. It reads like a high-end architecture monograph. It does not look like the restaurant interior.

The dinner register (dark surfaces) is reserved and controlled:
- Plum Ink: section title slides only, maximum one per section
- Aubergine: major statement callout slides only, maximum two or three per deck

This is not a minor color adjustment. It changes the character of the entire document.

## The Jade Problem

Jade was present on every slide of the first deck — as the 선 glyph color, as eyebrow label color, as status indicator dots. This produced a jade-and-aubergine pairing across every screen. The pairing belongs to neither the brand nor any of its daypart registers.

**The 선 glyph in the deck renders in:**
- Plum Ink (#120916) on light (Bone/Parchment) slide backgrounds
- Bone (#EDE7D8) on dark (Plum Ink/Aubergine) slide backgrounds

Jade does not appear as the 선 glyph color. Jade does not appear as the structural accent color throughout the deck. Jade may appear as a minor accent element (a ruled line, a category label) — it is never dominant.

## The Temporal Arc Does Not Govern the Deck

The temporal arc — Jade/Peacock opening the day, deepening to Plum Ink/Aubergine at dinner, Jade re-entering at late night — is a sensory environment principle for the restaurant. It governs color, lighting, sound, uniforms, and typography weight as a continuous time-based movement. It does not apply to a presentation document. A deck is not a sensory environment moving through time. It is a page.

## What the Deck Looks Like

Primary surface: warm off-white. Generous negative space. Large editorial type. One idea per slide. Photography at full bleed or dominant scale. Section dividers in deep dark (Plum Ink) with a single GT Sectra Fine Book headline in Bone. Content slides that look like they belong in a monograph about a considered place.

The governing test: could this slide appear in a premium editorial publication without embarrassment? If not, remove what makes it wrong.

## What This System Must Never Produce in Deck Context

- Dark backgrounds on content slides
- Jade as the primary accent color throughout
- The 선 glyph in Jade on any slide
- Gradient fills of any kind
- Centered layouts as default
- Bullet point lists of more than four items
- Thumbnail photography in grids
- Drop shadows on any element
- Decorative frames or borders
- Left-border callout boxes
- Any layout that reads as a PowerPoint template
- Any slide that could belong to a generic hospitality brand
