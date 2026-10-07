import React from "react";

/**
 * Large GT Sectra Display type, sentence case, that enters and settles as
 * its own beat over --son-imm-settle with --son-imm-ease (or scrubbed via
 * the progress prop). The large-text-as-event mechanism. Position/opacity
 * settle, no fade-up theatrics elsewhere — this is the sanctioned entrance.
 * Instant under reduced motion (tokens collapse to 0ms).
 */
export function KineticDisplay({
  as: Tag = "h2",
  size = "display",
  progress,
  children,
  className = "",
  style = {},
  ...rest
}) {
  const ref = React.useRef(null);
  const [landed, setLanded] = React.useState(false);
  const scrubbed = typeof progress === "number";

  React.useEffect(() => {
    if (scrubbed) return;
    const io = new IntersectionObserver(([e]) => { if (e.isIntersecting) { setLanded(true); io.disconnect(); } }, { threshold: 0.4 });
    io.observe(ref.current);
    return () => io.disconnect();
  }, [scrubbed]);

  const p = scrubbed ? Math.min(1, Math.max(0, progress)) : landed ? 1 : 0;
  return (
    <Tag
      ref={ref}
      className={`son-kinetic ${className}`}
      style={{
        fontFamily: "var(--son-font-display)",
        fontWeight: "var(--son-weight-book)",
        fontSize: size === "headline" ? "var(--son-text-headline)" : "var(--son-text-display)",
        lineHeight: "var(--son-leading-display)",
        letterSpacing: "var(--son-tracking-display)",
        margin: 0,
        textWrap: "balance",
        opacity: p,
        transform: `translateY(${(1 - p) * 0.35}em)`,
        transition: scrubbed ? "none" : "opacity var(--son-imm-settle, 0ms) var(--son-imm-ease, ease), transform var(--son-imm-settle, 0ms) var(--son-imm-ease, ease)",
        ...style,
      }}
      {...rest}
    >
      {children}
    </Tag>
  );
}
