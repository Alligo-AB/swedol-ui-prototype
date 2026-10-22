/* Shared by the Colors pages (foundations/colors-primitives.html, colors-tokens.html, colors.html):
   swatch card, table view, Cards / Table switch, and the primitive colors read live from the token package.
   Needs: pill-segment-control.css + .js, docs.css. Globals: COLORKIT. */
var COLORKIT = (function () {
  var PKG = 'https://unpkg.com/alligo-design-tokens@latest/dist/css/base/color.css';   // the package file that defines every color token
  var PRIM = '--color-primitive-color-';

  /* ── helpers ─────────────────────────────────────────────── */
  function el(tag, cls, text) {
    var n = document.createElement(tag);
    if (cls) n.className = cls;
    if (text != null) n.textContent = text;
    return n;
  }
  function parseHex(h) {           // #rgb | #rrggbb | #rrggbbaa -> [r,g,b,a]
    h = h.replace('#', '');
    if (h.length === 3) h = h.split('').map(function (c) { return c + c; }).join('');
    var n = parseInt(h.slice(0, 6), 16);
    return [(n >> 16) & 255, (n >> 8) & 255, n & 255, h.length === 8 ? parseInt(h.slice(6), 16) / 255 : 1];
  }
  function lum(rgb) {
    var c = rgb.slice(0, 3).map(function (v) { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); });
    return 0.2126 * c[0] + 0.7152 * c[1] + 0.0722 * c[2];
  }
  function contrast(a, b) {
    var l1 = lum(a), l2 = lum(b);
    return (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05);
  }
  function rgbText(rgb) {
    return rgb[3] < 1
      ? 'rgba(' + rgb[0] + ', ' + rgb[1] + ', ' + rgb[2] + ', ' + Math.round(rgb[3] * 100) / 100 + ')'
      : 'rgb(' + rgb[0] + ', ' + rgb[1] + ', ' + rgb[2] + ')';
  }
  function isDarkText(k) { return /inverted|on-black/.test(k); }

  var drift = 0, rootCS = null, probe = null;
  function ready() {
    if (probe) return;
    rootCS = getComputedStyle(document.documentElement);
    probe = document.body.appendChild(el('span'));
    probe.style.display = 'none';
  }
  function copyBtn(t) {
    var txt = 'var(' + t.var + ')', w = el('span', 'ds-copyname'), b = el('button', 'mo-copy');
    w.appendChild(el('span', 'ds-copyname__text', txt));
    b.type = 'button'; b.setAttribute('aria-label', 'Copy ' + txt);
    var ic = el('span', 'mo-ic', 'content_copy'); ic.setAttribute('aria-hidden', 'true'); b.appendChild(ic);
    b.addEventListener('click', function () {
      var done = function () { ic.textContent = 'check'; setTimeout(function () { ic.textContent = 'content_copy'; }, 1200); };
      if (navigator.clipboard) navigator.clipboard.writeText(txt).then(done, done); else done();
    });
    w.appendChild(b);
    return w;
  }
  function liveStatus(t, rgb) {     // compare tokens.json with what the CDN package really defines
    if (!rootCS.getPropertyValue(t.var).trim()) return 'Not in the current token package (tokens.json is out of date).';
    probe.style.color = 'var(' + t.var + ')';
    var m = getComputedStyle(probe).color.match(/[\d.]+/g).map(Number);
    var a = m.length > 3 ? m[3] : 1;
    if (Math.abs(m[0] - rgb[0]) > 1 || Math.abs(m[1] - rgb[1]) > 1 || Math.abs(m[2] - rgb[2]) > 1 || Math.abs(a - rgb[3]) > 0.02)
      return 'Live value differs: ' + (a < 1 ? 'rgba(' + m.join(', ') + ')' : 'rgb(' + m.slice(0, 3).join(', ') + ')') + '. tokens.json is out of date.';
    return '';
  }
  function getLive(t) {
    if (!rootCS.getPropertyValue(t.var).trim()) return null;
    probe.style.color = 'var(' + t.var + ')';
    var m = getComputedStyle(probe).color.match(/[\d.]+/g).map(Number);
    return [m[0], m[1], m[2], m.length > 3 ? m[3] : 1];
  }

  /* ── columns: one definition for the card rows and the table columns ─────────── */
  var COLS = {
    tok:     { label: 'Design token', cell: function (r) { return copyBtn(r.t); } },
    hex:     { label: 'Hex code',     cell: function (r) { return r.t.value; } },
    rgb:     { label: 'RGB Value',    cell: function (r) { return rgbText(parseHex(r.t.value)); } },
    purpose: { label: 'Purpose',      cell: function (r) { return r.t.description && r.t.description !== 'TBA' ? r.t.description : '-'; }, text: true },
    suit:    { label: 'Suitable for', cell: function () { return '-'; }, text: true },   // dash until the text is added
    used:    { label: 'Used by',      cell: function (r) { return r.used && r.used.length ? r.used.join(', ') : 'No semantic token uses it.'; }, text: true }
  };
  var SEMANTIC = ['tok', 'hex', 'rgb', 'purpose', 'suit'];
  var PRIMITIVE = ['tok', 'hex', 'rgb', 'used'];

  /* ── swatch card ─────────────────────────────────────────── */
  function card(r, cols) {
    var t = r.t, key = r.key, kind = r.kind, rgb = parseHex(t.value);
    var c = el('div', 'ds-swatch');
    var chip = el('div', 'ds-swatch__chip' + (rgb[3] < 1 ? ' ds-swatch__chip--checker' : ''));
    chip.setAttribute('aria-hidden', 'true');
    var fill = el('span');
    if (kind === 'text' || kind === 'icon') {
      var dark = isDarkText(key);
      chip.style.background = dark ? 'var(--color-surface-100)' : 'var(--color-surface-raised-primary)';
      fill.textContent = 'Aa';
      fill.style.cssText = 'color: var(' + t.var + '); font-size: 40px; line-height: 1; font-weight: 600;';
      if (kind === 'text') {
        var eff = getLive(t) || rgb;   // contrast uses what the package really renders
        var cr = contrast(eff, dark ? [0, 0, 0] : [255, 255, 255]);
        var badge = el('span', 'ds-swatch__aa', cr.toFixed(1) + ':1 · ' + (cr >= 7 ? 'AAA' : cr >= 4.5 ? 'AA' : cr >= 3 ? 'AA large' : 'Fail'));
        chip.style.flexDirection = 'column'; chip.style.justifyContent = 'space-between'; chip.style.alignItems = 'flex-start';
        fill.style.height = 'auto'; fill.style.width = 'auto';
        chip.appendChild(fill); chip.appendChild(badge);
      } else chip.appendChild(fill);
    } else if (kind === 'border') {
      fill.style.cssText = 'border: 6px solid var(' + t.var + '); background: var(--color-surface-raised-primary);';
      chip.appendChild(fill);
    } else {
      fill.style.background = 'var(' + t.var + ')';
      chip.appendChild(fill);
    }
    if (kind !== 'text') chip.style.padding = '8px';
    c.appendChild(chip);
    var body = el('div', 'ds-swatch__body');
    body.appendChild(el('span', 'ds-swatch__name', key));
    cols.forEach(function (id) {   // labelled rows
      var def = COLS[id], v = def.cell(r), row = el('div', 'ds-swatch__row');
      row.appendChild(el('span', 'ds-swatch__label', def.label));
      row.appendChild(typeof v === 'string' ? el('span', 'ds-swatch__val', v) : v);
      body.appendChild(row);
    });
    if (!r.prim) {   // semantic tokens: flag a value that tokens.json and the live package disagree on
      var warn = liveStatus(t, rgb);
      if (warn) { drift++; body.appendChild(el('span', 'ds-swatch__warn', warn)); }
    }
    c.appendChild(body);
    return c;
  }

  /* ── table view ──────────────────────────────────────────── */
  function previewCell(r) {      // small version of the card chip
    var rgb = parseHex(r.t.value), v = el('span', 'ds-ctable__prev');
    v.setAttribute('aria-hidden', 'true');
    if (rgb[3] < 1) v.className += ' ds-swatch__chip--checker';
    var f = el('span');
    if (r.kind === 'text' || r.kind === 'icon') {
      v.style.background = isDarkText(r.key) ? 'var(--color-surface-100)' : 'var(--color-surface-raised-primary)';
      f.textContent = 'Aa'; f.style.color = 'var(' + r.t.var + ')';
    } else if (r.kind === 'border') f.style.cssText = 'border: 4px solid var(' + r.t.var + '); background: var(--color-surface-raised-primary);';
    else f.style.background = 'var(' + r.t.var + ')';
    v.appendChild(f);
    return v;
  }
  function tableFor(recs, cols) {
    var wrap = el('div', 'ds-table-wrap ds-ctable'), tb = el('table', 'ds-table'), tr = el('tr');
    ['Swatch', 'Name'].concat(cols.map(function (id) { return COLS[id].label; })).forEach(function (h) {
      var th = el('th', null, h); th.scope = 'col'; if (h === 'Swatch') th.className = 'ds-ctable__prevcol'; tr.appendChild(th);
    });
    tb.appendChild(el('thead')).appendChild(tr);
    var body = tb.appendChild(el('tbody'));
    recs.forEach(function (r) {
      var row = el('tr'), td;
      td = el('td', 'ds-ctable__prevcol'); td.appendChild(previewCell(r)); row.appendChild(td);
      row.appendChild(el('th', null, r.key)); row.lastChild.scope = 'row';
      cols.forEach(function (id) {
        var def = COLS[id], v = def.cell(r);
        td = el('td', id === 'tok' ? 'ds-ctable__tok' : def.text ? 'ds-ctable__text' : null);
        if (typeof v === 'string') td.textContent = v; else td.appendChild(v);
        row.appendChild(td);
      });
      body.appendChild(row);
    });
    wrap.appendChild(tb);
    return wrap;
  }

  /* ── Cards / Table switch ────────────────────────────────── */
  var SEG = [['cards', 'Cards'], ['table', 'Table']];
  function segment(label, onPick) {
    var c = el('div', 'pill-segment-control pill-segment-control--sm'), th = el('span', 'pill-segment-control__thumb');
    c.setAttribute('role', 'group'); c.setAttribute('aria-label', label); th.setAttribute('aria-hidden', 'true'); c.appendChild(th);
    SEG.forEach(function (o, i) {
      var b = el('button', 'pill-segment-control__btn' + (i ? '' : ' pill-segment-control__btn--active'), o[1]);
      b.type = 'button'; b.dataset.view = o[0]; b.setAttribute('aria-pressed', String(!i)); c.appendChild(b);
    });
    c.addEventListener('segment-change', function (e) { onPick(e.detail.button.dataset.view); });
    return c;
  }
  function setView(sec, v) {
    sec.dataset.view = v;
    var c = sec.querySelector('.ds-viewbar .pill-segment-control');
    if (!c) return;
    c.querySelectorAll('.pill-segment-control__btn').forEach(function (b) {
      var on = b.dataset.view === v; b.classList.toggle('pill-segment-control__btn--active', on); b.setAttribute('aria-pressed', String(on));
    });
    ECO_SEGMENT.move(c);
  }
  function wireSection(sec) {    // h2 + switch on one row; the switch shows this section as cards or as a table
    if (sec.querySelector('.ds-viewbar')) return;
    var h2 = sec.querySelector('.ds-h2'), bar = el('div', 'ds-viewbar');
    h2.parentNode.insertBefore(bar, h2); bar.appendChild(h2);
    bar.appendChild(segment('View ' + h2.textContent + ' as', function (v) { sec.dataset.view = v; }));
    sec.dataset.view = 'cards';
    ECO_SEGMENT.init(bar);   // controls added after page load
  }

  /* ── is there room for the table? the text column must hold the seven columns (the Contents list takes 232px of the page) ── */
  var MIN_TABLE = 880;
  function fit() {
    var i = document.querySelector('.ds-doc .ds-inner'); if (!i) return;
    var cs = getComputedStyle(i), w = i.clientWidth - parseFloat(cs.paddingLeft) - parseFloat(cs.paddingRight);
    document.documentElement.classList.toggle('ck-wide', w >= MIN_TABLE);
  }
  window.addEventListener('resize', fit); window.addEventListener('load', fit);

  /* ── page API ────────────────────────────────────────────── */
  function clear(ids) {       // empty the grids before a re-render and drop the old tables
    ids.forEach(function (id) { var h = document.getElementById(id); h.textContent = ''; h._recs = null; });
    document.querySelectorAll('.ds-ctable').forEach(function (n) { n.remove(); });
    drift = 0;
  }
  function add(host, r) {     // one token: a card in the grid and a record for the table view
    ready();
    (host._recs = host._recs || []).push(r);
    if (host.classList.contains('ds-status')) return;
    host.appendChild(card(r, host._cols || SEMANTIC));
  }
  function finish(skipId) {   // tables next to every grid, a switch per section, one for the whole page
    document.querySelectorAll('.ds-grid, .ds-status').forEach(function (h) {
      if (h._recs && h._recs.length) h.parentNode.insertBefore(tableFor(h._recs, h._cols || SEMANTIC), h.nextSibling);
    });
    document.querySelectorAll('.ds-section[id]').forEach(function (sec) { if (sec.querySelector('.ds-grid, .ds-status')) wireSection(sec); });
    if (!document.querySelector('.ds-viewall')) {
      var all = el('div', 'ds-viewall');   // page-level switch: sets every section; each section can still be changed on its own
      all.appendChild(el('span', 'ds-viewall__label', 'Show all colors as'));
      all.appendChild(segment('Show all colors as', function (v) {
        document.querySelectorAll('.ds-section[data-view]').forEach(function (sec) { setView(sec, v); });
      }));
      document.querySelector('.ds-section--first .ds-inner').appendChild(all);
    }
    fit();
    return drift;
  }

  /* ── primitives: read from the package file (they are not in tokens.json) ── */
  function fetchPackage(ok, fail) {
    fetch(PKG).then(function (r) { if (!r.ok) throw new Error(r.status); return r.text(); }).then(function (css) {
      var prim = {}, used = {}, m, re = /(--color-primitive-color-[a-z0-9-]+):\s*(#[0-9a-fA-F]{3,8})\s*;/g;
      while ((m = re.exec(css))) prim[m[1].slice(PRIM.length)] = { var: m[1], value: m[2].toLowerCase() };
      re = /(--color-(?!primitive)[a-z0-9-]+):\s*var\(--color-primitive-color-([a-z0-9-]+)/g;   // a semantic token that points at a primitive
      while ((m = re.exec(css))) (used[m[2]] = used[m[2]] || []).push(m[1].slice('--color-'.length));
      Object.keys(used).forEach(function (k) { used[k].sort(); });
      ok({ prim: prim, used: used });
    }).catch(fail || function () {});
  }

  return { el: el, parseHex: parseHex, contrast: contrast, rgbText: rgbText, copyBtn: copyBtn, COLS: COLS, SEMANTIC: SEMANTIC, PRIMITIVE: PRIMITIVE, ready: ready,
           clear: clear, add: add, finish: finish, tableFor: tableFor, fetchPackage: fetchPackage, drift: function () { return drift; }, rootCS: function () { ready(); return rootCS; } };
})();
