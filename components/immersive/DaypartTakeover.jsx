import React from "react";

const pad = (n) => String(n).padStart(2, "0");
const toMin = (t) => { const [h, m] = String(t).split(":").map(Number); return h * 60 + (m || 0); };
const fmt = (min) => `${pad(Math.floor(((min % 1440) + 1440) % 1440 / 60))}:${pad(Math.round(min) % 60)}`;
// Approximation of --son-imm-ease (cubic-bezier(0.22, 1, 0.36, 1)) for the rAF clock.
const easeOut = (t) => 1 - Math.pow(1 - t, 5);

/**
 * The full-screen interstitial between chapters — the signature component.
 * Rolls the timestamp forward (e.g. 06:30 to 12:45) and cross-fades the
 * semantic tokens (surface, text, accent, glyph, border) from the outgoing
 * data-theme to the incoming one over --son-imm-takeover with --son-imm-ease:
 * the outgoing and incoming grounds are layered and the incoming fades in,
 * so every token register shifts in sync with the clock. The clock IS the
 * transition. Plays once when scrolled into view (auto), or scrub it
 * externally via the progress prop. Hard-cuts under reduced motion.
 */
export function DaypartTakeover({
  from = "dinner",
  to = "luxe",
  fromTime = "18:00",
  toTime = "22:30",
  auto = true,
  progress,
  label,
  onComplete,
  className = "",
  style = {},
  ...rest
}) {
  const rootRef = React.useRef(null);
  const [p, setP] = React.useState(progress ?? 0);
  const playedRef = React.useRef(false);
  const scrubbed = typeof progress === "number";

  React.useEffect(() => { if (scrubbed) setP(Math.min(1, Math.max(0, progress))); }, [progress, scrubbed]);

  React.useEffect(() => {
    if (scrubbed || !auto) return;
    const root = rootRef.current;
    const io = new IntersectionObserver(([e]) => {
      if (!e.isIntersecting || playedRef.current) return;
      playedRef.current = true;
      const ms = parseFloat(getComputedStyle(root).getPropertyValue("--son-imm-takeover")) || 0;
      const reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
      if (reduced || ms <= 0) { setP(1); onComplete && onComplete(); return; } // hard cut
      const t0 = performance.now();
      const tick = (now) => {
        const t = Math.min(1, (now - t0) / ms);
        setP(easeOut(t));
        if (t < 1) requestAnimationFrame(tick);
        else onComplete && onComplete();
      };
      requestAnimationFrame(tick);
    }, { threshold: 0.55 });
    io.observe(root);
    return () => io.disconnect();
  }, [auto, scrubbed, onComplete]);

  const a = toMin(fromTime), b = toMin(toTime);
  const clock = fmt(a + (b - a) * p);
  const layer = (theme, opacity) => (
    <div
      data-theme={theme}
      style={{
        position: "absolute", inset: 0, opacity,
        background: "var(--son-surface-primary)", color: "var(--son-text-primary)",
        display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center",
        gap: "var(--son-space-3)",
      }}
    >
      <span style={{ fontFamily: "var(--son-font-display)", fontWeight: "var(--son-weight-book)", fontSize: "var(--son-text-display)", letterSpacing: "var(--son-tracking-display)", lineHeight: "var(--son-leading-display)", fontVariantNumeric: "tabular-nums" }}>{clock}</span>
      {label && <span style={{ fontFamily: "var(--son-font-serif)", fontSize: "var(--son-text-eyebrow)", letterSpacing: "var(--son-tracking-eyebrow)", textTransform: "uppercase" }}>{label}</span>}
      <span className="son-glyph" style={{ position: "absolute", bottom: "var(--son-space-4)", fontSize: "26px" }}>선</span>
    </div>
  );

  return (
    <div
      ref={rootRef}
      data-theme={p < 1 ? from : to}
      className={`son-takeover ${className}`}
      style={{ position: "relative", width: "100vw", marginLeft: "calc(50% - 50vw)", height: "100vh", overflow: "hidden", ...style }}
      {...rest}
    >
      {layer(from, 1)}
      {layer(to, p)}
    </div>
  );
}
