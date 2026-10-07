import React from "react";

/**
 * Sŏn badge / category label. Small, recessive, eyebrow register.
 * Default is a hairline outline; accent uses the theme accent as a thin rule.
 * Never a filled pill demanding attention.
 */
export function Badge({
  variant = "outline",
  children,
  className = "",
  style = {},
  ...rest
}) {
  const base = {
    fontFamily: "var(--son-font-serif)",
    fontSize: "11px",
    textTransform: "uppercase",
    letterSpacing: "0.18em",
    lineHeight: 1,
    padding: "6px 10px",
    display: "inline-flex",
    alignItems: "center",
    borderRadius: "var(--son-radius-sm)",
  };
  const variants = {
    outline: {
      border: "1px solid var(--son-border-default)",
      color: "var(--son-text-secondary)",
    },
    accent: {
      border: "1px solid var(--son-accent)",
      color: "var(--son-accent)",
    },
    solid: {
      border: "1px solid var(--son-surface-inverse)",
      background: "var(--son-surface-inverse)",
      color: "var(--son-surface-primary)",
    },
  };
  return (
    <span className={`son-badge ${className}`} style={{ ...base, ...variants[variant], ...style }} {...rest}>
      {children}
    </span>
  );
}
