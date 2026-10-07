import React from "react";

/**
 * The chapter-marker system: eyebrow plus kicker plus display statement.
 * Lines land with a per-line stagger of --son-imm-stagger over
 * --son-imm-settle when scrolled into view. Instant under reduced motion.
 */
export function SectionHeader({
  eyebrow,
  kicker,
  children,
  className = "",
  style = {},
  ...rest
}) {
  const ref = React.useRef(null);
  const [landed, setLanded] = React.useState(false);
  React.useEffect(() => {
    const io = new IntersectionObserver(([e]) => { if (e.isIntersecting) { setLanded(true); io.disconnect(); } }, { threshold: 0.3 });
    io.observe(ref.current);
    return () => io.disconnect();
  }, []);
  const line = (i) => ({
    opacity: landed ? 1 : 0,
    transform: landed ? "none" : "translateY(0.5em)",
    transition: `opacity var(--son-imm-settle, 0ms) var(--son-imm-ease, ease) calc(var(--son-imm-stagger, 0ms) * ${i}), transform var(--son-imm-settle, 0ms) var(--son-imm-ease, ease) calc(var(--son-imm-stagger, 0ms) * ${i})`,
  });
  return (
    <header ref={ref} className={`son-sectionheader ${className}`} style={{ display: "flex", flexDirection: "column", gap: "var(--son-space-3)", ...style }} {...rest}>
      {eyebrow && <span className="son-eyebrow" style={line(0)}>{eyebrow}</span>}
      {kicker && <p style={{ fontFamily: "var(--son-font-body)", fontSize: "var(--son-text-lead)", lineHeight: "var(--son-leading-snug)", margin: 0, maxWidth: "var(--son-measure-narrow)", ...line(1) }}>{kicker}</p>}
      <h2 style={{ fontFamily: "var(--son-font-display)", fontWeight: "var(--son-weight-book)", fontSize: "var(--son-text-section)", lineHeight: "var(--son-leading-tight)", letterSpacing: "var(--son-tracking-display)", margin: 0, maxWidth: "24ch", textWrap: "balance", ...line(kicker ? 2 : 1) }}>{children}</h2>
    </header>
  );
}
