import React from "react";

/**
 * A horizontal moving label row, used sparingly, sentence case — a single
 * repeated-label moment. The row is duplicated once and translated -50% in
 * a loop, so the motion is seamless. Static single row under reduced motion.
 */
export function Marquee({
  label,
  separator = "선",
  duration = 36,
  className = "",
  style = {},
  ...rest
}) {
  const reduced = typeof window !== "undefined" && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const cell = (
    <span style={{ display: "inline-flex", alignItems: "baseline", gap: "var(--son-space-4)", paddingRight: "var(--son-space-4)" }}>
      <span>{label}</span>
      <span className="son-glyph" aria-hidden="true" style={{ fontSize: "0.55em", alignSelf: "center" }}>{separator}</span>
    </span>
  );
  const row = (hidden) => (
    <span aria-hidden={hidden || undefined} style={{ display: "inline-flex", whiteSpace: "nowrap" }}>
      {[0, 1, 2, 3, 4, 5].map((i) => <React.Fragment key={i}>{cell}</React.Fragment>)}
    </span>
  );
  return (
    <div
      className={`son-marquee ${className}`}
      style={{
        overflow: "hidden", width: "100%",
        borderTop: "var(--son-border-hairline) solid var(--son-border-default)",
        borderBottom: "var(--son-border-hairline) solid var(--son-border-default)",
        padding: "var(--son-space-2) 0",
        fontFamily: "var(--son-font-display)",
        fontSize: "var(--son-text-section)",
        lineHeight: "var(--son-leading-tight)",
        color: "var(--son-text-primary)",
        ...style,
      }}
      {...rest}
    >
      {reduced ? (
        <span style={{ whiteSpace: "nowrap", display: "block", overflow: "hidden", textOverflow: "ellipsis" }}>{cell}</span>
      ) : (
        <div style={{ display: "inline-flex", whiteSpace: "nowrap", animation: `son-marquee ${duration}s linear infinite`, willChange: "transform" }}>
          {row(false)}
          {row(true)}
        </div>
      )}
    </div>
  );
}
