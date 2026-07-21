// Sŏn track — scrub-keyed still-layer opacity at the coda (gate pass B).
// The rest and coda opacities are the seon tokens, read from computed
// style so no value lives here. The scrub is a pure function of scroll
// position: the final stretch of document travel maps linearly from rest
// to full, so scrubbing back reverses the close by construction and the
// close is the reader's own act. Travel is native scroll until pass 2
// (Lenis); entrances are pass 3; the reduced-motion hard cut at the P11
// boundary is pass 6.
// Invariant note: this file may never set a stacking-context-creating
// property on body, the track, or a dark panel (adherence/check-track.mjs
// enforces the CSS side; the JS side is held by review).

const CODA_TRAVEL_VH = 80; // ~80vh of travel; token lands in tokens/motion-track.css at pass 2

const glyph = document.querySelector(".still-glyph");
const layerStyles = getComputedStyle(glyph);
const restOpacity = parseFloat(layerStyles.getPropertyValue("--son-seon-still-opacity"));
const codaOpacity = parseFloat(layerStyles.getPropertyValue("--son-seon-still-opacity-coda"));

let scrubStart = 0;
let scrubLength = 1;
let ticking = false;

function apply() {
  ticking = false;
  const progress = Math.min(1, Math.max(0, (window.scrollY - scrubStart) / scrubLength));
  glyph.style.opacity = String(restOpacity + progress * (codaOpacity - restOpacity));
}

function measure() {
  const viewport = window.innerHeight;
  const end = document.documentElement.scrollHeight - viewport;
  scrubLength = (CODA_TRAVEL_VH / 100) * viewport;
  scrubStart = end - scrubLength;
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
