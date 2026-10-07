import React from "react";

/**
 * A slow-moving flat-color ground that keeps a section subtly alive.
 * No gradient, no texture overlay, ever: one flat panel of the theme's
 * secondary surface drifts over the primary surface. Optional module: the
 * 선 glyph at large scale in slow motion, gated behind --son-glyph-motion
 * (switch the flag off and the module disappears without touching
 * anything else). Static under reduced motion.
 */
export function AmbientField({
  theme,
  glyph = false,
  speed = 48,
  className = "",
  style = {},
  children,
  ...rest
}) {
  const rootRef = React.useRef(null);
  const [glyphOn, setGlyphOn] = React.useState(false);
  const reduced = typeof window !== "undefined" && window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  React.useEffect(() => {
    if (!glyph || !rootRef.current) return;
    const flag = getComputedStyle(rootRef.current).getPropertyValue("--son-glyph-motion").trim();
    setGlyphOn(flag === "on");
  }, [glyph]);

  return (
    <div
      ref={rootRef}
      data-theme={theme}
      className={`son-ambient ${className}`}
      style={{
        position: "relative", overflow: "hidden",
        background: "var(--son-surface-primary)", color: "var(--son-text-primary)",
        ...style,
      }}
      {...rest}
    >
      <div
        aria-hidden="true"
        style={{
          position: "absolute", left: "-15%", top: "-20%", width: "80%", height: "120%",
          background: "var(--son-surface-secondary)",
          animation: reduced ? "none" : `son-imm-drift ${speed}s var(--son-imm-ease, ease-in-out) infinite alternate`,
          willChange: "transform",
        }}
      ></div>
      {glyph && glyphOn && !reduced && (
        <span
          className="son-glyph"
          aria-hidden="true"
          style={{
            position: "absolute", right: "-4%", bottom: "-12%", fontSize: "56vh",
            opacity: 0.14,
            animation: `son-imm-glyph-drift ${speed * 1.5}s var(--son-imm-ease, ease-in-out) infinite alternate`,
            willChange: "transform",
          }}
        >선</span>
      )}
      <div style={{ position: "relative" }}>{children}</div>
    </div>
  );
}
