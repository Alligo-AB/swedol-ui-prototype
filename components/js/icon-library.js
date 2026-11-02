/* ECO icon library behaviour (skill eco-icon, CSS components/css/icon.css, data components/icon-library/icon-library-data.js).
   Markup: <div data-icon-library> with [data-il-search] (input), [data-il-cat] (select: all | material | custom), [data-il-sub] (a chip group, filled by the script),
   [data-il-count] (live region) and [data-il-grid] (the grid). A click on an item copies the icon name. */
(function () {
  var L = window.ECO_ICON_LIB;
  var root = document.querySelector('[data-icon-library]');
  if (!L || !root) return;
  var $ = function (s) { return root.querySelector(s); };
  var search = $('[data-il-search]'), cat = $('[data-il-cat]'), sub = $('[data-il-sub]'), count = $('[data-il-count]'), grid = $('[data-il-grid]');
  var GROUPS = { custom: [['custom', 'Customized symbols'], ['brand', 'Brand'], ['social', 'Social'], ['logo', 'Logo']] };
  var items = [];
  L.outline.forEach(function (a) { items.push({ n: a[0], l: a[1], g: 'outline', c: 'material' }); });
  /* Fill icons (L.fill) are not offered here: they are for developers, as the active state of an icon (see the Icon page) */
  L.custom.forEach(function (a) { items.push({ n: a[0], g: a[1], c: 'custom', vb: a[2], s: a[3], v: a[4] }); });
  var RESERVED = ['verified_500_custom', 'assignment_turned_in_500_custom', 'history_500_custom'];   // reserved for the Product & Discount badges: never use them for anything else
  var ORDER = [['outline', 'Material Symbols'], ['custom', 'Custom icons: Customized symbols'], ['brand', 'Custom icons: Brand'], ['social', 'Custom icons: Social'], ['logo', 'Custom icons: Logo']];
  var state = { q: '', cat: 'all', sub: 'all' };

  function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/"/g, '&quot;'); }
  function glyph(it) {
    if (it.c === 'custom') { var v = it.v && it.v['40']; return '<svg class="icon icon--lg" viewBox="' + (v ? v[0] : it.vb) + '" fill="currentColor" aria-hidden="true"' + (it.g === 'logo' && /white/.test(it.n) ? ' style="background:var(--color-surface-opacity-black-80)"' : '') + '>' + (v ? v[1] : it.s) + '</svg>'; }
    return '<span class="icon icon--lg' + (it.g === 'fill' ? ' icon--fill' : '') + '" aria-hidden="true">' + esc(it.l) + '</span>';
  }
  function render() {
    var q = state.q.trim().toLowerCase().replace(/\s+/g, '_');
    var list = items.filter(function (it) { return (state.cat === 'all' || it.c === state.cat) && (state.sub === 'all' || it.g === state.sub) && (!q || it.n.toLowerCase().indexOf(q) > -1); });
    function item(it) {
      var res = RESERVED.indexOf(it.n) > -1;
      return '<button type="button" class="icon-item" data-name="' + esc(it.n) + '" aria-label="Copy name ' + esc(it.n) + (res ? ', reserved for Product &amp; Discount badges' : '') + '">' + (res ? '<span class="badge-basic badge-basic--warning badge-basic--weak icon-item__tag" title="Reserved for the Product &amp; Discount badges. Do not use for anything else.">Reserved</span>' : '') + '<span class="icon-item__copy"><span class="icon icon--sm" aria-hidden="true">content_copy</span></span><span class="icon-item__glyph">' + glyph(it) + '</span><span class="icon-item__name">' + esc(it.n) + '</span></button>';
    }
    grid.innerHTML = ORDER.map(function (g) {
      var m = list.filter(function (it) { return it.g === g[0]; });
      return m.length ? '<h3 class="ds-h3 ds-group il-heading">' + g[1] + ' <span class="il-n">(' + m.length + ')</span></h3><div class="il-grid">' + m.map(item).join('') + '</div>' : '';
    }).join('');
    count.textContent = list.length + (list.length === 1 ? ' icon' : ' icons');
    if (!list.length) grid.innerHTML = '<p class="ds-desc ds-note" style="">No icons match “' + esc(state.q) + '”.</p>';
  }
  function renderSub() {
    var g = GROUPS[state.cat];
    sub.hidden = !g;
    if (!g) { sub.innerHTML = ''; return; }
    sub.innerHTML = [['all', 'All']].concat(g).map(function (x) { return '<button type="button" class="chip" data-sub="' + x[0] + '" aria-pressed="' + (state.sub === x[0]) + '"><span class="chip__label">' + x[1] + '</span></button>'; }).join('');
  }
  search.addEventListener('input', function () { state.q = search.value; render(); });
  cat.addEventListener('change', function () { state.cat = cat.value; state.sub = 'all'; renderSub(); render(); });
  sub.addEventListener('chip:change', function (e) {   // single choice: the chip that was clicked wins, a click on the chosen one keeps it
    state.sub = e.detail.selected ? e.target.closest('.chip').getAttribute('data-sub') : state.sub;
    [].forEach.call(sub.querySelectorAll('.chip'), function (c) { c.setAttribute('aria-pressed', c.getAttribute('data-sub') === state.sub); });
    render();
  });
  grid.addEventListener('click', function (e) {
    var b = e.target.closest('.icon-item'); if (!b) return;
    var name = b.getAttribute('data-name'), label = b.querySelector('.icon-item__name');
    function done(ok) { label.textContent = ok ? 'Copied' : 'Copy failed'; setTimeout(function () { label.textContent = name; }, 1200); }
    if (navigator.clipboard && window.isSecureContext) navigator.clipboard.writeText(name).then(function () { done(true); }, function () { done(false); });
    else { var t = document.createElement('textarea'); t.value = name; document.body.appendChild(t); t.select(); var ok = false; try { ok = document.execCommand('copy'); } catch (x) {} document.body.removeChild(t); done(ok); }
  });
  renderSub(); render();
})();
