import React from "react";

/**
 * Sŏn tabs. A row of labels separated by a hairline, active marked by a single
 * rule beneath. Inactive labels recede; the active label is primary text.
 * Invites rather than routes.
 */
export function Tabs({
  items = [],
  value,
  defaultValue,
  onChange,
  className = "",
  style = {},
  ...rest
}) {
  const [internal, setInternal] = React.useState(defaultValue ?? items[0]?.id);
  const active = value !== undefined ? value : internal;

  const select = (id) => {
    if (value === undefined) setInternal(id);
    onChange && onChange(id);
  };

  return (
    <div
      className={`son-tabs ${className}`}
      role="tablist"
      style={{ display: "flex", gap: "28px", borderBottom: "1px solid var(--son-border-default)", ...style }}
      {...rest}
    >
      {items.map((it) => {
        const on = it.id === active;
        return (
          <button
            key={it.id}
            role="tab"
            aria-selected={on}
            className="son-tab"
            onClick={() => select(it.id)}
            style={{
              fontFamily: "var(--son-font-serif)",
              fontSize: "14px",
              letterSpacing: "0.02em",
              background: "transparent",
              border: "0",
              padding: "0 0 12px",
              marginBottom: "-1px",
              cursor: "pointer",
              color: on ? "var(--son-text-primary)" : "var(--son-text-secondary)",
              borderBottom: `1px solid ${on ? "var(--son-border-strong)" : "transparent"}`,
            }}
          >
            {it.label}
          </button>
        );
      })}
    </div>
  );
}
