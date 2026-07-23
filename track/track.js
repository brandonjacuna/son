// Sŏn track — the scroll model (pass 2) and the coda scrub (gate pass B).
//
// Travel is scrubbed, text is timed, feedback is untouched. The scroll
// driver is Lenis, pinned 1.3.8 and vendored, configured exactly per the
// ratified model (structure-motion-decision §4): lerp from the track
// token, easeOutExpo wheel smoothing, syncTouch false so touch stays
// native and is only smoothed. Lenis drives native window scroll, so
// ground seams stay hard cuts keyed to real scroll position, the
// paint-order wipe needs no script, and window.scrollY stays the one
// source of truth for every scrub key. Under prefers-reduced-motion the
// driver never initializes: native scroll, per the designed second path.
//
// The coda scrub is a pure function of scroll position: the final stretch
// of document travel maps linearly from the rest token to the coda token,
// so scrubbing back reverses the close and the close is the reader's own
// act. All values are tokens read from computed style; no value lives
// here. Entrances are pass 3; the reduced-motion hard cut at the P11
// boundary is pass 6.
//
// Invariant note: this file may never set a stacking-context-creating
// property on body, the track, or a dark panel (adherence/check-track.mjs
// enforces the CSS side; the JS side is held by review).

const rootStyles = getComputedStyle(document.documentElement);
const reducedMotion = matchMedia("(prefers-reduced-motion: reduce)");

/* ── The scroll driver ── */

const easeOutExpo = (t) => (t === 1 ? 1 : 1 - Math.pow(2, -10 * t));

const lenisLerp = parseFloat(rootStyles.getPropertyValue("--son-track-lenis-lerp"));

// No literal fallbacks: if a token fails to resolve, smoothing is skipped
// (native scroll is the honest degradation) rather than silently running
// on a shadow copy of a retuned value.
if (typeof Lenis === "function" && !reducedMotion.matches && Number.isFinite(lenisLerp)) {
  const lenis = new Lenis({
    lerp: lenisLerp,
    easing: easeOutExpo,
    smoothWheel: true,
    syncTouch: false,
  });
  const raf = (time) => {
    lenis.raf(time);
    requestAnimationFrame(raf);
  };
  requestAnimationFrame(raf);
}

/* ── The coda scrub ── */

const glyph = document.querySelector(".still-glyph");

let restOpacity = 0;
let codaOpacity = 1;
let scrubStart = Infinity;
let scrubLength = 1;
let ticking = false;

function apply() {
  ticking = false;
  const progress = Math.min(1, Math.max(0, (window.scrollY - scrubStart) / scrubLength));
  glyph.style.opacity = String(restOpacity + progress * (codaOpacity - restOpacity));
  bandApply();
}

function measure() {
  // Tokens re-read per measure so a conditional (media- or theme-scoped)
  // tune of the rest opacity is never shadowed by a stale inline value.
  const layerStyles = getComputedStyle(glyph);
  restOpacity = parseFloat(layerStyles.getPropertyValue("--son-seon-still-opacity"));
  codaOpacity = parseFloat(layerStyles.getPropertyValue("--son-seon-still-opacity-coda"));
  // The travel token is unitless vh-class (tokens/motion-track.css): the
  // scrub multiplies by innerHeight, end-anchored so the final frame is
  // guaranteed on every device; the dynamic-toolbar drift is the recorded
  // cost (docs/track-scratch.md).
  const codaTravel = parseFloat(rootStyles.getPropertyValue("--son-track-coda-travel"));
  const viewport = window.innerHeight;
  const end = document.documentElement.scrollHeight - viewport;
  if (!Number.isFinite(codaTravel) || end <= 0) {
    // No travel, no close: the layer rests and content keeps the frame.
    // Full opacity under content is the forbidden state (build-spec P11).
    scrubStart = Infinity;
    scrubLength = 1;
  } else {
    scrubLength = Math.min((codaTravel / 100) * viewport, end);
    scrubStart = end - scrubLength;
  }
  // The pin geometry: extra wrapper height beyond the panel is the pin
  // distance; zero on mobile and under reduced motion (no pin).
  pinStart = pinTrack.offsetTop;
  pinDistance = pinTrack.offsetHeight - modelPanel.offsetHeight;
  apply();
}

function onScroll() {
  if (!ticking) {
    ticking = true;
    requestAnimationFrame(apply);
  }
}

/* ── Entrances (pass 3) ──
   Registry values are the track tokens, read once (they are static per
   load). Sequencing: sibling stagger in DOM order; per-line stagger
   inside strophes; data-enter-slot pins an element to an absolute slot
   (the P7 glyph with the lead, the P8 right column at +2); data-enter-hold
   inserts the hero's hold after the strophe completes. Hidden strophe
   variants are armed without advancing the clock so a band switch after
   arrival shows the completed state. Entrances fire once per panel at
   ~85% active and never re-fire. */

const STAGGER = parseFloat(rootStyles.getPropertyValue("--son-track-stagger")) || 0;
const HOLD = parseFloat(rootStyles.getPropertyValue("--son-track-hold")) || 0;
const LINE_DURATION = parseFloat(rootStyles.getPropertyValue("--son-track-line-duration")) || 0;

const isShown = (el) => getComputedStyle(el).display !== "none";

function armGroup(items, startT) {
  let t = startT;
  const movers = [];
  items.forEach((item) => {
    const pinned = item.dataset.enterSlot !== undefined;
    const start = pinned ? Number(item.dataset.enterSlot) * STAGGER : t;
    if (item.dataset.enter === "lines") {
      const lines = item.querySelectorAll(".line");
      lines.forEach((line, i) => {
        line.style.setProperty("--enter-delay", `${start + i * STAGGER}ms`);
        const mover = line.querySelector(".line-mover");
        if (mover) movers.push(mover);
      });
      if (isShown(item) && !pinned) {
        const lastStart = start + (lines.length - 1) * STAGGER;
        t = item.hasAttribute("data-enter-hold")
          ? lastStart + LINE_DURATION + HOLD
          : lastStart + STAGGER;
      }
    } else {
      item.style.setProperty("--enter-delay", `${start}ms`);
      movers.push(item.querySelector(".line-mover, .enter-mover") || item);
      if (isShown(item) && !pinned) t = start + STAGGER;
    }
    item.classList.add("is-in");
  });
  // Performance floor: will-change scoped to the animation window, cleared.
  movers.forEach((m) => { m.style.willChange = "transform, opacity"; });
  setTimeout(() => movers.forEach((m) => { m.style.willChange = ""; }), t + 1400);
  return t;
}

const heroPanel = document.querySelector('[data-panel="p1"]');
const enteringPanels = [...document.querySelectorAll(".panel")].filter(
  (p) => p !== heroPanel && p.querySelector("[data-enter]")
);

// ~85% active (the registry token): the panel's top has crossed into the
// top 15% band, so the seam is across the viewport before the text rises.
// Ground leads, content follows.
const activeThreshold =
  parseFloat(rootStyles.getPropertyValue("--son-track-active-threshold")) || 0.85;

const io = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      // Manual items (band labels, the release body) are fired by the band
      // controller; under reduced motion there is no build to wait on and
      // they arm with the panel.
      const selector = reducedMotion.matches
        ? "[data-enter]"
        : "[data-enter]:not([data-enter-manual])";
      armGroup(entry.target.querySelectorAll(selector), 0);
      io.unobserve(entry.target);
    });
  },
  { rootMargin: `0px 0px -${activeThreshold * 100}% 0px` }
);
enteringPanels.forEach((p) => io.observe(p));

/* ── The arrival (build-spec §2.3) ──
   The arrival is the first frame of the hero: Plum Ink, the wordmark at
   its chrome position (instant via the inlined subset), the still layer
   at rest. Choreography begins when the display faces are loaded and the
   floor has passed, from this exact frame; the wordmark never moves. Past
   the ceiling the page renders complete instead: display never fires on
   unloaded fonts. Under reduced motion the arrival arms immediately and
   the reduced-motion rules make it instant and opacity-only. */

const ARRIVAL_FLOOR_MS = 800;
const FONT_CEILING_MS = 5000;
const ARRIVAL_FACES = [
  '400 1em "GT Sectra Display"',
  '400 1em "GT Sectra Fine"',
  '400 1em "GT Sectra"',
  '400 1em "GT Alpina Fine"',
  '300 1em "GT Alpina Fine"',
];

function armArrival() {
  const tEnd = armGroup(heroPanel.querySelectorAll("[data-enter]"), 0);
  armGroup(document.querySelectorAll(".chrome [data-enter]"), tEnd);
}

function arriveComplete() {
  arrived = true;
  document.documentElement.classList.add("arrive-complete");
  document.querySelectorAll("[data-enter]").forEach((el) => el.classList.add("is-in"));
  // The reduced path renders the band complete: clear any scrubbed state
  // so the stripes return to their built default.
  stripes.forEach((s) => s.style.removeProperty("--stripe-build"));
  io.disconnect();
}

const waitMs = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

if (reducedMotion.matches) {
  armArrival();
} else {
  const fontsSettled = Promise.all(ARRIVAL_FACES.map((f) => document.fonts.load(f))).then(
    () => "loaded",
    () => "hang"
  );
  Promise.all([
    Promise.race([fontsSettled, waitMs(FONT_CEILING_MS).then(() => "hang")]),
    waitMs(ARRIVAL_FLOOR_MS),
  ]).then(([fonts]) => {
    if (fonts === "hang") arriveComplete();
    else armArrival();
  });
}

/* ── The band (pass 4, build-spec §2.5) ──
   The site's one bounded pin-and-scrub. Desktop: progress is the pin
   travel (sticky engage to release); the four stripes build left to
   right, scrub-keyed and reversible, each over its quarter of the
   distance. Mobile: no pin; the stacked band builds top to bottom as it
   passes through the viewport. Each label lands TIMED as its stripe
   completes, and the release is announced by the body's entrance: travel
   scrubbed, text timed, the two-system split inside the set piece.
   Labels and body fire once and never un-enter; scrubbing back re-runs
   only the stripes. Under reduced motion (and the font-hang complete
   render) the controller stands down and the band's default state is
   built. */

const pinTrack = document.querySelector(".pin-track");
const modelPanel = document.querySelector('[data-panel="p9"]');
const band = document.querySelector(".daypart-band");
const stripes = [...document.querySelectorAll(".stripe")];
const stripeLabels = stripes.map((s) => s.querySelector(".stripe-label"));
const modelBodyItems = document.querySelectorAll(".model-body [data-enter]");
const labelFired = stripes.map(() => false);
let bandReleased = false;
let arrived = false;
let pinStart = 0;
let pinDistance = 0;

function bandProgress() {
  if (pinDistance > 1) {
    return (window.scrollY - pinStart) / pinDistance;
  }
  // No pin: build keyed to the band's own passage through the viewport,
  // completing while the band's bottom is still inside the same 15% margin
  // the entrance system activates in (1 - the activation threshold token).
  const rect = band.getBoundingClientRect();
  const tail = window.innerHeight * (1 - activeThreshold);
  return (window.innerHeight - rect.top) / (rect.height + tail);
}

function bandApply() {
  if (reducedMotion.matches || arrived) return;
  const p = Math.min(1, Math.max(0, bandProgress()));
  stripes.forEach((stripe, i) => {
    const built = Math.min(1, Math.max(0, p * stripes.length - i));
    stripe.style.setProperty("--stripe-build", String(built));
    if (built >= 1 && !labelFired[i]) {
      labelFired[i] = true;
      armGroup([stripeLabels[i]], 0);
    }
  });
  if (p >= 1 && !bandReleased) {
    bandReleased = true;
    armGroup(modelBodyItems, 0);
  }
}

/* ── Bootstrap ── */
addEventListener("scroll", onScroll, { passive: true });
addEventListener("resize", measure);
measure();
// Panel heights can move when the web fonts settle; the scrub and pin
// anchors follow them (inert today, every panel holds its svh floor, but
// the door is closed rather than watched).
document.fonts.ready.then(measure);
