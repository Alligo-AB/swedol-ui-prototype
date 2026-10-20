"""Shared pieces of the Breadcrumb page sets: the hub (gen_breadcrumb.py) and the two types Base (gen_breadcrumb_base.py) and Bar (gen_breadcrumb_bar.py).
Figma: Base 1986:64264, Bar 332:8639 (checked 2026-10-19)."""
from build import *

FIGMA_BASE = 'https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=1986-64264'
FIGMA_BAR = 'https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=332-8639'
FIGMA_RESP = 'https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=9071-123361'
PARENT = ('breadcrumb.html', 'Breadcrumb')

STYLE = r'''    .pg-note { font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-tertiary); }
    .pg-col { display: flex; flex-direction: column; align-items: flex-start; gap: 16px; width: 100%; }
    .pg-row { display: flex; flex-wrap: wrap; align-items: center; gap: 16px 32px; }
    .pg-cell { display: flex; flex-direction: column; align-items: flex-start; gap: 8px; }
    .pg-cell > .pg-note { margin: 0; }
    .pg-matrix td { vertical-align: middle; padding-top: 16px; padding-bottom: 16px; }
    .pg-grey { background: var(--color-background-secondary); }
    .pg-cap { font-size: 12px; line-height: 12px; letter-spacing: 0.48px; text-transform: uppercase; color: var(--color-text-tertiary); font-weight: 600; }
    .ds-stage .breadcrumb, .ds-fig__stage .breadcrumb { padding-left: 0; padding-right: 0; padding-bottom: 0; }   /* the page margin and the built-in bottom padding belong to a real page, not to a docs stage */
    .ds-stage .breadcrumb__bar, .ds-fig__stage .breadcrumb__bar { padding: 0; }
    .ds-fig__stage--bar { align-items: flex-start; justify-content: flex-start; }
    .measure .breadcrumb__bar { padding: 16px 0; }   /* the Measurements figure draws the real bar padding */
    .ds-callout__art { padding-right: 24px; }'''

# shared page script: real components, one builder each so the Playground, the Variants and the matrix share one markup
JS_BUILD = r'''
  var ALL = ['Home', 'Clothing and protective gear', 'Work pants', 'Carpenter pants', 'Winter pants', 'Insulated winter pants'];
  function el(tag, cls, text) { var n = document.createElement(tag); if (cls) n.className = cls; if (text != null) n.textContent = text; return n; }
  /* one crumb: state = enabled | hover (forced for the demo) | active (the current page) */
  function crumb(text, state) {
    var c;
    if (state === 'active') { c = el('span', 'breadcrumb-item breadcrumb-item--active', text); c.setAttribute('aria-current', 'page'); return c; }
    c = el('a', 'breadcrumb-item', text); c.href = '#'; if (state === 'hover') c.dataset.state = 'hover';
    c.addEventListener('click', function (e) { e.preventDefault(); });
    return c;
  }
  function sep() { return el('span', 'breadcrumb-sep', '/'); }
  /* the bar: n crumbs (2 to 6), the last one is the current page */
  function bar(n, last, hover) {
    var nav = el('nav', 'breadcrumb'), b = el('div', 'breadcrumb__bar'); nav.setAttribute('aria-label', 'Breadcrumb'); nav.appendChild(b);
    ALL.slice(0, n - 1).concat([last]).forEach(function (t, i) { if (i) b.appendChild(sep()); b.appendChild(crumb(t, i === n - 1 ? 'active' : (hover && i === 0 ? 'hover' : 'enabled'))); });
    return nav;
  }
  function barMarkup(n, last) {
    var h = '<nav class="breadcrumb" aria-label="Breadcrumb">\n  <div class="breadcrumb__bar">\n';
    ALL.slice(0, n - 1).forEach(function (t) { h += '    <a href="#" class="breadcrumb-item">' + esc(t) + '</a>\n    <span class="breadcrumb-sep">/</span>\n'; });
    return h + '    <span class="breadcrumb-item breadcrumb-item--active" aria-current="page">' + esc(last) + '</span>\n  </div>\n</nav>';
  }
  function rng(n) { return function () { var r = document.createRange(); r.selectNodeContents(n); return r.getBoundingClientRect(); }; }
'''
