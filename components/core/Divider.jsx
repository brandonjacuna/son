import React from "react";

/**
 * Sŏn divider. A single hairline rule. Optional centered eyebrow label
 * (a 선 glyph, a section marker). No double rules, no decorative dividers.
 */
export function Divider({
  label,
  spacing = "md",
  className = "",
  style = {},
  ...rest
}) {
  const m = spacing === "sm" ? "16px" : spacing === "lg" ? "48px" : "32px";
  const line = { flex: 1, height: 1, background: "var(--son-border-default)" };

  if (!label) {
    return <hr className={`son-divider ${className}`} style={{ border: 0, height: 1, background: "var(--son-border-default)", margin: `${m} 0`, ...style }} {...rest} />;
  }
  return (
    <div className={`son-divider ${className}`} role="separator" style={{ display: "flex", alignItems: "center", gap: "16px", margin: `${m} 0`, ...style }} {...rest}>
      <span style={line} />
      <span style={{ fontFamily: "var(--son-font-serif)", fontSize: "11px", textTransform: "uppercase", letterSpacing: "0.2em", color: "var(--son-text-secondary)", whiteSpace: "nowrap" }}>{label}</span>
      <span style={line} />
    </div>
  );
}
