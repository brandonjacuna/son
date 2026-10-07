import React from "react";

/**
 * Sŏn text field. Hairline underline-forward register. Label sits above in the
 * eyebrow voice. Error state names the specific problem, never apologizes.
 * Error reads through border weight (hairline → strong) plus the message
 * line — never color alone; the palette has no red.
 */
export function Input({
  label,
  id,
  type = "text",
  error,
  hint,
  className = "",
  style = {},
  ...rest
}) {
  const fieldId = id || (label ? `son-${label.replace(/\s+/g, "-").toLowerCase()}` : undefined);
  return (
    <div className={`son-input ${className}`} style={{ display: "flex", flexDirection: "column", gap: "8px", ...style }}>
      {label && (
        <label htmlFor={fieldId} style={{ fontFamily: "var(--son-font-serif)", fontSize: "11px", textTransform: "uppercase", letterSpacing: "0.16em", color: "var(--son-text-primary)" }}>
          {label}
        </label>
      )}
      <input
        id={fieldId}
        type={type}
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
          padding: "10px 2px",
          width: "100%",
          appearance: "none",
        }}
        {...rest}
      />
      {(error || hint) && (
        <span className="son-field-error" style={{ fontFamily: "var(--son-font-body)", fontSize: "var(--son-text-fine)", color: "var(--son-text-primary)" }}>
          {error || hint}
        </span>
      )}
    </div>
  );
}
