A hairline tab row. The active label is primary text underlined by a single rule; the rest recede.

```jsx
<Tabs
  defaultValue="dinner"
  items={[
    { id: "morning", label: "Good Energy" },
    { id: "dosi", label: "Dosi" },
    { id: "dinner", label: "Sŏn" },
  ]}
  onChange={(id) => setView(id)}
/>
```

Controlled via `value`/`onChange` or uncontrolled via `defaultValue`.
