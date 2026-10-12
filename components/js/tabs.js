/* ECO tabs behaviour. Skill: eco-tabs. Plain-script, no deps: <script src="/components/js/tabs.js"></script>
   Every .tab-bar gets one sliding line (.tab-bar__indicator) under the selected tab.
   - Content tabs ([role="tablist"]): click / arrow keys / Home / End select a tab (automatic activation), show the
     matching [role="tabpanel"] named by aria-controls, and the line slides to the tab.
   - Link tabs (<nav class="tab-bar"> with <a class="tab" aria-current="page">): a click keeps the hover look on the
     tab while the next page loads; on that page the line starts under the tab that was active and slides to the
     new active one (the previous index is kept in sessionStorage for 5 s).
   Runs on load; call ECO_TABS.init(root) for bars added later. */
(function () {
  var KEY = 'eco-tabs:', html = document.documentElement;
  /* Runs while <head> is parsed, before the first paint: a link tab was just clicked on the previous page, so the new current
     tab must start with the grey hover line (not its active line) until the sliding line arrives. */
  try {
    for (var k = 0; k < sessionStorage.length; k++) {
      var key = sessionStorage.key(k);
      if (key.indexOf(KEY) === 0 && Date.now() - JSON.parse(sessionStorage.getItem(key)).t < 5000) html.classList.add('tabs-arrive');
    }
  } catch (e) {}
  function current(list) { return list.querySelector('[role="tab"][aria-selected="true"], .tab[aria-current]'); }
  function barKey(list) { return KEY + (list.dataset.tabsId || list.getAttribute('aria-label') || 'bar'); }
  /* animate=false jumps (load, resize); animate=true slides. */
  function place(list, animate, target) {
    var ind = list.querySelector('.tab-bar__indicator'), t = target || current(list);
    if (!ind || !t || !t.offsetWidth) return;
    if (!animate) ind.classList.remove('is-ready');
    ind.style.width = t.offsetWidth + 'px';
    ind.style.transform = 'translateX(' + t.offsetLeft + 'px)';
    if (!animate) { void ind.offsetWidth; ind.classList.add('is-ready'); }
  }
  /* The tab the line is travelling to keeps its grey hover line until the sliding line arrives (class .tab--arriving). */
  function arrive(list, tab) {
    var ind = list.querySelector('.tab-bar__indicator'), tm;
    list.querySelectorAll('.tab--arriving').forEach(function (x) { x.classList.remove('tab--arriving'); });
    tab.classList.add('tab--arriving');
    function done() { html.classList.remove('tabs-arrive'); tab.classList.remove('tab--arriving'); ind.removeEventListener('transitionend', end); clearTimeout(tm); }
    function end(e) { if (e.propertyName === 'transform') done(); }
    ind.addEventListener('transitionend', end);
    tm = setTimeout(done, 600);   /* no transition (reduced motion) or interrupted */
  }
  function select(list, tab) {
    var before = current(list);
    list.querySelectorAll('[role="tab"]').forEach(function (t) {
      var on = t === tab;
      t.setAttribute('aria-selected', on ? 'true' : 'false');
      t.tabIndex = on ? 0 : -1;
      t.classList.toggle('tab--active', on);
      var p = t.getAttribute('aria-controls') && document.getElementById(t.getAttribute('aria-controls'));
      if (p) p.hidden = !on;
    });
    if (before !== tab) arrive(list, tab);
    place(list, true);
    tab.scrollIntoView({ block: 'nearest', inline: 'nearest' });
  }
  function init(root) {
    (root || document).querySelectorAll('.tab-bar').forEach(function (list) {
      if (list.dataset.tabsInit) return;
      list.dataset.tabsInit = '1';
      var tablist = list.getAttribute('role') === 'tablist';
      var ind = document.createElement('span'); ind.className = 'tab-bar__indicator'; ind.setAttribute('aria-hidden', 'true');
      list.appendChild(ind); list.dataset.slide = '';

      var cur = current(list), prev = null;
      if (!tablist) {   /* link tabs: where was the line on the previous page? */
        try {
          var s = JSON.parse(sessionStorage.getItem(barKey(list)) || 'null'); sessionStorage.removeItem(barKey(list));
          if (s && Date.now() - s.t < 5000) prev = list.querySelectorAll('.tab')[s.i];
        } catch (e) {}
      }
      var intro = prev && prev !== cur;
      if (!intro) html.classList.remove('tabs-arrive');
      if (intro) cur.classList.add('tab--arriving');   /* grey line under the new tab until the line slides over */   /* the line starts under the old tab; resize / font callbacks must not jump it before it has slid */
      place(list, false, intro ? prev : null);
      if (intro) requestAnimationFrame(function () { requestAnimationFrame(function () { intro = false; arrive(list, cur); place(list, true); }); });
      var jump = function () { if (!intro) place(list, false); };
      if (window.ResizeObserver) new ResizeObserver(jump).observe(list);
      if (document.fonts && document.fonts.ready) document.fonts.ready.then(jump);

      if (tablist) {
        list.addEventListener('click', function (e) {
          var t = e.target.closest('[role="tab"]');
          if (t) select(list, t);
        });
        list.addEventListener('keydown', function (e) {
          var tabs = Array.prototype.slice.call(list.querySelectorAll('[role="tab"]'));
          var i = tabs.indexOf(document.activeElement);
          if (i < 0) return;
          var n = { ArrowRight: i + 1, ArrowLeft: i - 1, Home: 0, End: tabs.length - 1 }[e.key];
          if (n === undefined) return;
          e.preventDefault();
          var t = tabs[(n + tabs.length) % tabs.length];
          t.focus(); select(list, t);
        });
      } else {
        /* scripts that move aria-current (an on-page scrollspy): the line follows */
        new MutationObserver(function () { if (!intro) place(list, true); }).observe(list, { attributes: true, attributeFilter: ['aria-current'], subtree: true });
        list.addEventListener('click', function (e) {
          var a = e.target.closest('a.tab');
          if (a && (a.getAttribute('href') || '#') === '#') { e.preventDefault(); return; }   /* placeholder tab, no page yet */
          if (a && /^#./.test(a.getAttribute('href'))) return;   /* on-page anchor: no page load, nothing to keep */
          if (!a || a.hasAttribute('aria-current') || e.defaultPrevented || e.button || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || a.target === '_blank') return;
          a.classList.add('tab--pending');   /* keeps the hover look until the page changes */
          try { sessionStorage.setItem(barKey(list), JSON.stringify({ i: Array.prototype.indexOf.call(list.querySelectorAll('.tab'), cur), t: Date.now() })); } catch (err) {}
        });
      }
    });
  }
  window.ECO_TABS = { init: init };
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', function () { init(); }); else init();
})();
