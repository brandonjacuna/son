import React from "react";

/**
 * Sŏn select. Native control, hairline underline register to match Input.
 * Does not pre-select a default that encodes an assumption about the customer.
 * Error reads through border weight (hairline → strong) plus the message
 * line — never color alone; the palette has no red.
 */
export function Select({
  label,
  id,
  error,
  hint,
  children,
  className = "",
  style = {},
  ...rest
}) {
  const fieldId = id || (label ? `son-${label.replace(/\s+/g, "-").toLowerCase()}` : undefined);
  return (
    <div className={`son-select ${className}`} style={{ display: "flex", flexDirection: "column", gap: "8px", ...style }}>
      {label && (
        <label htmlFor={fieldId} style={{ fontFamily: "var(--son-font-serif)", fontSize: "11px", textTransform: "uppercase", letterSpacing: "0.16em", color: "var(--son-text-primary)" }}>
          {label}
        </label>
      )}
      <div style={{ position: "relative" }}>
        <select
          id={fieldId}
          className="son-field"
          aria-invalid={error ? true : undefined}
          style={{
            fontFamily: "var(--son-font-body)",
            fontSize: "16px",
            color: "var(--son-text-primary)",
            background: "transparent",
            border: "0",
            borderBottom: `1px solid ${error ? "var(--son-border-strong)" : "var(--son-border-default)"}`,
            borderRadius: 0,
            padding: "10px 24px 10px 2px",
            width: "100%",
            appearance: "none",
            WebkitAppearance: "none",
            cursor: rest.disabled ? "not-allowed" : "pointer",
          }}
          {...rest}
        >
          {children}
        </select>
        <span aria-hidden="true" style={{ position: "absolute", right: 4, top: "50%", transform: "translateY(-50%)", pointerEvents: "none", color: "var(--son-icon-default)", fontSize: 11, opacity: rest.disabled ? 0.45 : 1 }}>▾</span>
      </div>
      {(error || hint) && (
        <span className="son-field-error" style={{ fontFamily: "var(--son-font-body)", fontSize: "var(--son-text-fine)", color: "var(--son-text-primary)" }}>
          {error || hint}
        </span>
      )}
    </div>
  );
}
