import React from "react";

/**
 * Sŏn card. A held surface: hairline border, no drop shadow, near-square
 * corners. Padding is generous; the empty margin is part of the composition.
 */
export function Card({
  as: Tag = "div",
  surface = "primary",
  padding = "lg",
  children,
  className = "",
  style = {},
  ...rest
}) {
  const pad = padding === "none" ? 0 : padding === "sm" ? "16px" : padding === "md" ? "24px" : "32px";
  const bg = surface === "secondary" ? "var(--son-surface-secondary)" : "var(--son-surface-primary)";

  return (
    <Tag
      className={`son-card ${className}`}
      style={{
        background: bg,
        border: "1px solid var(--son-border-default)",
        borderRadius: "var(--son-radius-sm)",
        padding: pad,
        color: "var(--son-text-primary)",
        ...style,
      }}
      {...rest}
    >
      {children}
    </Tag>
  );
}
