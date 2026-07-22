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
  apply();
}

function onScroll() {
  if (!ticking) {
    ticking = true;
    requestAnimationFrame(apply);
  }
}

addEventListener("scroll", onScroll, { passive: true });
addEventListener("resize", measure);
measure();
