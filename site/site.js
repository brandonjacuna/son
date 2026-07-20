// Sŏn investor site — motion (pass 4).
// Timed reveal only: no pin, no scrub, no parallax, no smooth-scroll
// library. Transform and opacity only; the CSS in site.css carries the
// durations, rises, and the band wipe. This file only decides WHEN.
//
// Reduced motion is a designed path, not a kill switch: every element is
// set to its complete state immediately (the immersive kill rule in
// tokens/motion-immersive.css collapses the transitions themselves), so
// the band appears complete and the hero appears settled, and nothing is
// lost. Without JavaScript the page renders complete; the html.js gate
// keeps hidden states out of the no-JS path.

(() => {
  const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const marked = "[data-reveal], [data-reveal-band]";

  const arm = (el, i) => {
    const delay = el.dataset.delay !== undefined ? Number(el.dataset.delay) : i * 80;
    if (el.hasAttribute("data-reveal-band")) {
      el.style.setProperty("--beat-delay", `${delay}ms`);
    } else {
      el.style.transitionDelay = `${delay}ms`;
    }
    el.classList.add("is-in");
  };

  if (reduce) {
    document.querySelectorAll(marked).forEach((el) => el.classList.add("is-in"));
    return;
  }

  // The load beat: the hero entrance and the chrome fade. Once, on load,
  // nothing on scroll after it.
  const loadBeat = () => {
    document.querySelectorAll("[data-load]").forEach((el, i) => arm(el, i));
  };
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", () => requestAnimationFrame(loadBeat));
  } else {
    requestAnimationFrame(loadBeat);
  }

  // The scroll beats: IntersectionObserver on enter, at roughly 85% of the
  // viewport height, firing once and never re-firing.
  const io = new IntersectionObserver(
    (entries) => {
      for (const entry of entries) {
        if (!entry.isIntersecting) continue;
        io.unobserve(entry.target);
        const beat = entry.target;
        const items = [
          ...(beat.matches(marked) ? [beat] : []),
          ...beat.querySelectorAll(marked),
        ];
        items.forEach((el, i) => arm(el, i));
      }
    },
    { rootMargin: "0px 0px -15% 0px" }
  );
  document.querySelectorAll("[data-beat]").forEach((beat) => io.observe(beat));
})();
