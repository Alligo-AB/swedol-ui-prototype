/* ECO docs: shared helpers for the three Layout pages (global LAYOUT).
   The breakpoint list, the grid figure (scaled, built from the package tokens) and the live window readout.
   Values come from the token package CSS that every page already loads (custom properties on :root), never from numbers typed here.
   Skill: eco-doc-page, "Foundations in the new structure". */
(function (w) {
  var DOC = 'https://unpkg.com/alligo-design-tokens@latest/dist/css/base/dimension.css';
  var T = '--dimension-';
  /* One row per breakpoint. `from` / `to` are the window widths of the range (docs text, see CLAUDE.md); margin, gutter and columns are token names.
     xl has no tokens of its own for gutter and columns (it uses lg) and its margin is "infinite": the figure shows the 1440px prototype width, where the margin token is 120px. */
  var BPS = [
    { id: 'xs', name: 'XSmall', token: 'bp-xs', from: 0, to: 639, device: 'Mobile', base: 'Mobile', example: 375, exampleLabel: 'Mobile (minimum supported width 375px)', margin: T + 'margin-site-margin-xs', gutter: T + 'gutter-xs', cols: T + 'breakpoint-columns-column-xs' },
    { id: 'sm', name: 'Small', token: 'bp-sm', from: 640, to: 768, device: 'Tablet', base: 'Mobile', example: 768, exampleLabel: 'Tablet (iPad mini, 768px)', margin: T + 'margin-site-margin-sm', gutter: T + 'gutter-sm', cols: T + 'breakpoint-columns-column-sm' },
    { id: 'md', name: 'Medium', token: 'bp-md', from: 769, to: 1023, device: 'Desktop small', base: 'Desktop', example: 1023, exampleLabel: 'Desktop small (1023px)', margin: T + 'margin-site-margin-md', gutter: T + 'gutter-md', cols: T + 'breakpoint-columns-column-md' },
    { id: 'lg', name: 'Large', token: 'bp-lg', from: 1024, to: 1280, device: 'Desktop', base: 'Desktop', example: 1280, exampleLabel: 'Desktop (1280px)', margin: T + 'margin-site-margin-lg', gutter: T + 'gutter-lg', cols: T + 'breakpoint-columns-column-lg' },
    { id: 'xl', name: 'XLarge', token: 'bp-xl', from: 1281, to: null, device: 'Desktop large', base: 'Desktop', example: 1440, exampleLabel: 'Desktop large (1440px, the largest Figma prototype)', margin: T + 'margin-site-margin-xl', gutter: T + 'gutter-lg', cols: T + 'breakpoint-columns-column-lg', infinite: true }
  ];
  var CONTENT_MAX = 1200;   // docs and page templates: --max-w, the content area stops growing here (1280px window − 2 × 40px margin)
  var FRAME_H = 160;

  var root = document.documentElement, probe;
  function resolve(name) {   // a token like var(--dimension-spacing-space-40, 40px) → 40 (a number); a unitless token (columns) → its number
    var raw = getComputedStyle(root).getPropertyValue(name).trim();
    if (!raw) return NaN;
    if (/^-?\d+(\.\d+)?$/.test(raw)) return parseFloat(raw);
    if (!probe) { probe = document.createElement('div'); probe.style.cssText = 'position:absolute;visibility:hidden;pointer-events:none;height:0;overflow:hidden'; document.body.appendChild(probe); }
    probe.style.width = 'var(' + name + ')';
    return parseFloat(getComputedStyle(probe).width);
  }
  function vals(bp) { return { margin: resolve(bp.margin), gutter: resolve(bp.gutter), cols: resolve(bp.cols) }; }
  function bpFor(width) { for (var i = BPS.length - 1; i >= 0; i--) if (width >= BPS[i].from) return BPS[i]; return BPS[0]; }
  function px(n) { return isNaN(n) ? '–' : n + 'px'; }
  function el(tag, cls, text) { var n = document.createElement(tag); if (cls) n.className = cls; if (text != null) n.textContent = text; return n; }

  /* A scaled grid frame. opts: { h: frame height, itemH: height of a demo block, items: [spanFraction, …] } puts demo blocks on the columns (fraction of the columns: 1, 0.5, 0.25). */
  function gridFig(bp, opts) {
    opts = opts || {};
    var v = vals(bp), wrap = el('div', 'lg-fig'), scale = el('div', 'lg-scale'), frame = el('div', 'lg-frame');
    var W = bp.example, M = v.margin, H = opts.h || Math.max(FRAME_H, Math.round(W * 0.22));   // taller for the wide frames, so a scaled figure keeps some height
    wrap.dataset.w = W; wrap.dataset.h = H;
    frame.style.width = W + 'px'; frame.style.height = H + 'px';
    var ml = el('span', 'lg-margin lg-margin--l'), mr = el('span', 'lg-margin lg-margin--r');
    ml.style.width = mr.style.width = M + 'px';
    var cols = el('div', 'lg-cols');
    cols.style.left = cols.style.right = M + 'px'; cols.style.gap = v.gutter + 'px'; cols.style.gridTemplateColumns = 'repeat(' + v.cols + ', minmax(0, 1fr))';
    for (var i = 0; i < v.cols; i++) cols.appendChild(el('span', 'lg-col'));
    frame.appendChild(ml); frame.appendChild(mr); frame.appendChild(cols);
    if (opts.items) {
      var items = el('div', 'lg-items');
      items.style.left = items.style.right = M + 'px'; items.style.gap = v.gutter + 'px'; items.style.gridTemplateColumns = 'repeat(' + v.cols + ', minmax(0, 1fr))';
      opts.items.forEach(function (f, k) { var s = Math.max(1, Math.round(f * v.cols)), it = el('span', 'lg-item', s + ' of ' + v.cols); it.style.gridColumn = 'span ' + s; items.appendChild(it); });
      frame.appendChild(items);
    }
    scale.appendChild(frame); wrap.appendChild(scale);
    wrap._parts = { margin: ml, col: cols.firstChild, cols: cols, frame: frame, values: v };
    return wrap;
  }
  function fit(scope) {   // scale every .lg-fig to the width of its container (never above 1:1)
    (scope || document).querySelectorAll('.lg-fig').forEach(function (f) {
      var W = +f.dataset.w, H = +f.dataset.h, s = Math.min(1, f.clientWidth / W);
      f.firstChild.style.transform = 'scale(' + s + ')';
      f.style.height = Math.round(H * s) + 'px';
    });
  }
  var queue = [];
  function onFit(fn) { queue.push(fn); }
  function refit() { fit(); queue.forEach(function (fn) { fn(); }); }
  window.addEventListener('resize', refit);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(refit);

  /* The package file as text, for the Tokens page (value, reference and the description comment of each layout token). */
  function fetchDoc(ok, fail) {
    fetch(DOC).then(function (r) { if (!r.ok) throw 0; return r.text(); }).then(function (t) {
      var out = {}, last = '';
      t.split('\n').forEach(function (line) {
        var c = /^\s*\/\*\s*(.*?)\s*\*\/\s*$/.exec(line), d = /^\s*(--[a-z0-9-]+):\s*(.*?);\s*$/.exec(line);
        if (c) { last = c[1]; return; }
        if (d) { out[d[1]] = { raw: d[2], desc: last }; last = ''; }
      });
      ok(out);
    }).catch(fail || function () {});
  }

  w.LAYOUT = { BPS: BPS, CONTENT_MAX: CONTENT_MAX, resolve: resolve, vals: vals, bpFor: bpFor, px: px, el: el, gridFig: gridFig, fit: fit, onFit: onFit, refit: refit, fetchDoc: fetchDoc };
})(window);
