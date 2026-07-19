import React from "react";

/**
 * The repeatable "request the briefing" call — a quiet hairline button
 * designed to appear at several beats of the narrative, all pointing to one
 * gated form. Hover shifts within the palette; no scale, no theatrics.
 */
export function SeededCTA({
  href = "#briefing",
  children = "Request the briefing",
  note,
  className = "",
  style = {},
  ...rest
}) {
  return (
    <div className={`son-seededcta ${className}`} style={{ display: "flex", flexDirection: "column", alignItems: "flex-start", gap: "var(--son-space-1)", ...style }}>
      <a
        href={href}
        className="son-btn son-btn--secondary"
        style={{
          display: "inline-flex", alignItems: "center",
          padding: "14px 28px",
          border: "var(--son-border-hairline) solid var(--son-border-strong)",
          borderRadius: "var(--son-radius-sm)",
          background: "transparent",
          color: "var(--son-text-primary)",
          fontFamily: "var(--son-font-serif)",
          fontSize: "var(--son-text-body)",
          letterSpacing: "var(--son-tracking-open)",
          textDecoration: "none",
          transition: "background var(--son-motion-standard) var(--son-ease-standard)",
        }}
        {...rest}
      >
        {children}
      </a>
      {note && <span style={{ fontFamily: "var(--son-font-body)", fontSize: "var(--son-text-fine)", color: "var(--son-text-primary)" }}>{note}</span>}
    </div>
  );
}
