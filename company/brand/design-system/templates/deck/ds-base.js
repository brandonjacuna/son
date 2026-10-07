// templates/deck/ds-base.js — load the Sŏn design system for this template.
// One file, one line to edit (the `base` path) if you relocate the template.
(() => {
  const base = '../..';
  for (const p of ['styles.css']) {
    const l = document.createElement('link');
    l.rel = 'stylesheet';
    l.href = base + '/' + p;
    document.head.appendChild(l);
  }
  const s = document.createElement('script');
  s.src = base + '/_ds_bundle.js';
  s.onerror = () => console.error('ds-base.js: failed to load ' + s.src +
    ' — in a consuming project point `base` at the bound _ds/<folder> tree relative to this page; in a fresh design system the bundle may simply not be compiled yet');
  document.head.appendChild(s);
})();
