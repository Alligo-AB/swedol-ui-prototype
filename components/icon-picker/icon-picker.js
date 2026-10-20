/* ECO icon picker (Material Symbols). Skill: eco-icon-picker. One script tag, no other files to include.
   Add data-icon-picker to a text input that holds a Material Symbols name. Click or Tab into it: a panel opens on top of
   the field with a search box (instant search over all icons by name and tags), Recent and Popular icons.
   Picking an icon writes its name into the input and fires an "input" event. The icon data loads on first open. */
(function () {
  /* window.ECO_ICONS = [[name, tags], ...] sorted by popularity (icon-picker-data.js next to this file, from the Google Fonts Material Symbols metadata) */
  var LIMIT = 60, DATA = [], ICONS = [];
  var base = document.currentScript ? document.currentScript.src.replace(/[^\/]*$/, '') : '';
  var waiting = null;
  function loadData(cb) {
    if (window.ECO_ICONS) { DATA = window.ECO_ICONS; ICONS = DATA.slice(0, LIMIT).map(function (r) { return r[0]; }); return cb(); }
    if (waiting) return waiting.push(cb);
    waiting = [cb];
    var s = document.createElement('script'); s.src = base + 'icon-picker-data.js';
    s.onload = function () { var q = waiting; waiting = null; q.forEach(function (f) { loadData(f); }); };
    document.head.appendChild(s);
  }
  var KEY = 'eco-icon-recent', MAX_RECENT = 8;

  function recent() { try { return JSON.parse(localStorage.getItem(KEY)) || []; } catch (e) { return []; } }
  function remember(name) {
    try { localStorage.setItem(KEY, JSON.stringify([name].concat(recent().filter(function (n) { return n !== name; })).slice(0, MAX_RECENT))); } catch (e) {}
  }

  var css = document.createElement('style');
  css.textContent =
    '.ip-wrap{position:relative}' +
    '.ip-wrap>input{width:100%;box-sizing:border-box}' +
    '.ip-panel{position:absolute;top:calc(-1 * var(--dimension-spacing-space-12,12px));left:calc(-1 * var(--dimension-spacing-space-12,12px));right:calc(-1 * var(--dimension-spacing-space-12,12px));z-index:20;display:flex;flex-direction:column;gap:var(--dimension-spacing-space-12,12px);padding:var(--dimension-spacing-space-12,12px);background:var(--color-surface-raised-primary);box-shadow:var(--shadow-elevation-b-80)}' +
    '.ip-panel[hidden]{display:none}' +
    '.ip-search{width:100%;box-sizing:border-box;height:42px;padding:var(--dimension-spacing-space-8,8px) var(--dimension-spacing-space-12,12px);font:inherit;font-size:16px;line-height:24px;color:inherit;background:var(--color-background-primary);border:1px solid var(--color-border-input-default)}' +
    '.ip-search:focus-visible{outline:2px solid var(--color-border-focus);outline-offset:2px}' +
    '.ip-search:focus{border-color:var(--color-border-selected)}' +
    '.ip-label{font-size:12px;line-height:18px;letter-spacing:0.24px;font-weight:600}' +
    '.ip-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(40px,1fr));gap:var(--dimension-spacing-space-4,4px);max-height:176px;overflow-y:auto}' +
    '.ip-panel.ip-mouse .ip-search[type="text"]:focus-visible{outline:0}' +
    '.ip-btn{display:flex;align-items:center;justify-content:center;height:40px;padding:0;color:var(--color-icon-primary);background:transparent;border:1px solid transparent;cursor:pointer}' +
    '.ip-btn:hover{background:var(--color-surface-navigation-hover)}' +
    '.ip-btn:focus-visible{outline:2px solid var(--color-border-focus);outline-offset:-2px}' +
    '.ip-btn[aria-pressed="true"]{border-color:var(--color-border-selected)}' +
    '.ip-btn .material-symbols-outlined{font-size:24px;font-variation-settings:"FILL" 0,"wght" 300,"GRAD" 0}' +
    '.ip-empty{font-size:14px;line-height:20px}';
  document.head.appendChild(css);

  function mk(tag, cls, text) { var n = document.createElement(tag); if (cls) n.className = cls; if (text != null) n.textContent = text; return n; }

  function attach(input) {
    var wrap = input.closest('.input-wrap');  /* eco-input: the panel covers the whole field, not just the <input> */
    if (wrap) wrap.classList.add('ip-wrap'); else { wrap = mk('div', 'ip-wrap'); input.parentNode.insertBefore(wrap, input); wrap.appendChild(input); }
    var panel = mk('div', 'ip-panel'); panel.hidden = true; wrap.appendChild(panel);
    input.setAttribute('autocomplete', 'off');
    var search = mk('input', 'ip-search'); search.type = 'text'; search.placeholder = 'Search icons'; search.setAttribute('aria-label', 'Search icons');
    var body = mk('div'); body.style.cssText = 'display:flex;flex-direction:column;gap:var(--dimension-spacing-space-12,12px)';
    panel.appendChild(search); panel.appendChild(body);

    var skip = false, mouse = false;   /* mouse open: no focus ring on the search box; keyboard (Tab) open keeps it */
    input.addEventListener('pointerdown', function () { mouse = true; });
    function pick(name) {
      input.value = name; remember(name);
      input.dispatchEvent(new Event('input', { bubbles: true }));
      close();
    }
    function group(label, names) {
      if (!names.length) return;
      body.appendChild(mk('div', 'ip-label', label));
      var g = mk('div', 'ip-grid');
      names.forEach(function (n) {
        var b = mk('button', 'ip-btn'); b.type = 'button'; b.title = n; b.setAttribute('aria-label', n); b.setAttribute('aria-pressed', String(n === input.value.trim()));
        var s = mk('span', 'material-symbols-outlined', n); s.setAttribute('aria-hidden', 'true'); b.appendChild(s);
        b.addEventListener('click', function () { pick(n); });
        g.appendChild(b);
      });
      body.appendChild(g);
    }
    function render() {
      var q = search.value.trim().toLowerCase().replace(/\s+/g, '_');
      body.textContent = '';
      if (!q) { group('Recent', recent()); group('Popular', ICONS); return; }
      /* rank: name starts with > a word of the name starts with > a tag word starts with. Data is sorted by popularity */
      var a = [], b = [], c = [], seen = {}, qs = q.replace(/_/g, ' ');
      DATA.forEach(function (r) {
        if (seen[r[0]]) return; seen[r[0]] = 1;
        if (r[0].indexOf(q) === 0) a.push(r[0]);
        else if (('_' + r[0]).indexOf('_' + q) !== -1) b.push(r[0]);
        else if ((' ' + r[1]).indexOf(' ' + qs) !== -1) c.push(r[0]);
      });
      var hits = a.concat(b, c), total = hits.length;
      hits = hits.slice(0, LIMIT);
      group(total ? 'Results (' + total + (total > LIMIT ? ', showing ' + LIMIT : '') + ')' : 'Results', hits);
      if (!total) body.appendChild(mk('div', 'ip-empty', 'No icons match "' + search.value.trim() + '".'));
    }
    function open() { loadData(function () { show(); }); }
    function show() { panel.classList.toggle('ip-mouse', mouse); mouse = false; search.value = ''; render(); panel.hidden = false; search.focus(); }
    function close() { panel.hidden = true; skip = true; input.focus(); skip = false; }

    input.addEventListener('focus', function () { if (!skip) open(); });
    input.addEventListener('click', function () { if (panel.hidden) open(); });
    search.addEventListener('input', render);
    wrap.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
    document.addEventListener('mousedown', function (e) { if (!wrap.contains(e.target)) panel.hidden = true; });
    wrap.addEventListener('focusout', function (e) { if (e.relatedTarget && !wrap.contains(e.relatedTarget)) panel.hidden = true; });
  }

  document.querySelectorAll('input[data-icon-picker]').forEach(attach);
  if (document.querySelector('input[data-icon-picker]')) setTimeout(function () { loadData(function () {}); }, 500);   /* preload so the first open is instant */
})();
