/* ECO tabs behaviour. Skill: eco-tabs. Plain-script, no deps: <script src="/components/js/tabs.js"></script>
   Every .tab-bar gets one sliding line (.tab-bar__indicator) under the selected tab.
   - Content tabs ([role="tablist"]): click / arrow keys / Home / End select a tab (automatic activation), show the
     matching [role="tabpanel"] named by aria-controls, and the line slides to the tab.
   - Link tabs (<nav class="tab-bar"> with <a class="tab" aria-current="page">): a click keeps the hover look on the
     tab while the next page loads; on that page the line starts under the tab that was active and slides to the
     new active one (the previous index is kept in sessionStorage for 5 s).
   - On-page navigation (<nav class="tab-bar tab-bar--page"> with <a class="tab" href="#section">): the bar sticks to the top,
     the line follows the section in view (scrollspy, aria-current="location") and a click scrolls to the section with
     eco-motion easing, moves focus to it and adds the #hash (data-tabs-hash="off" keeps the URL as it is).
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

  /* ── On-page navigation (.tab-bar--page) ─────────────────────────────────────────────── */
  function scrollParent(el) {
    for (var p = el.parentElement; p && p !== document.body && p !== html; p = p.parentElement) {
      var o = getComputedStyle(p).overflowY;
      if ((o === 'auto' || o === 'scroll') && p.scrollHeight > p.clientHeight + 1) return p;
    }
    return window;
  }
  function token(name, fb) { return parseFloat(getComputedStyle(html).getPropertyValue(name)) || fb; }
  function pageNav(list) {
    var tabs = Array.prototype.slice.call(list.querySelectorAll('a.tab'));
    var targets = tabs.map(function (a) { var h = a.getAttribute('href') || ''; return /^#./.test(h) ? document.getElementById(decodeURIComponent(h.slice(1))) : null; });
    var first = targets.filter(Boolean)[0];
    if (!first) return;
    var scroller = scrollParent(first), win = scroller === window, cur = -1, lock = false, raf = 0, tick = false;
    function vTop() { return win ? 0 : scroller.getBoundingClientRect().top + scroller.clientTop; }   /* the sticky bar sits inside the border */
    function vH() { return win ? window.innerHeight : scroller.clientHeight; }
    function pos() { return win ? window.pageYOffset : scroller.scrollTop; }
    function max() { return win ? html.scrollHeight - window.innerHeight : scroller.scrollHeight - scroller.clientHeight; }
    function jumpTo(y) { if (win) window.scrollTo({ top: y, left: 0, behavior: 'instant' }); else scroller.scrollTo({ top: y, left: 0, behavior: 'instant' }); }   /* instant: a smooth scroll-behavior in the page CSS would stretch every frame */
    /* where the bar's lower edge is while it is stuck: what a section must clear */
    function offset() { return (parseFloat(getComputedStyle(list).top) || 0) + list.getBoundingClientRect().height; }
    function pick() {
      var line = vTop() + offset() + (vH() - offset()) * 0.25, idx = targets.indexOf(first);
      targets.forEach(function (t, i) { if (t && t.getBoundingClientRect().top <= line) idx = i; });
      if (pos() >= max() - 2 && pos() > 0) for (var i = targets.length - 1; i >= 0; i--) if (targets[i]) { idx = i; break; }   /* the end of the page: the last section, even when it is too short to reach the line */
      return idx;
    }
    function setCurrent(i, quiet) {
      if (i === cur) return;
      var was = cur; cur = i;
      tabs.forEach(function (t, k) { if (k === i) t.setAttribute('aria-current', 'location'); else t.removeAttribute('aria-current'); });
      /* any number of sections: when the bar scrolls sideways the current tab is kept in view */
      function reveal(smooth) { if (list.scrollWidth > list.clientWidth + 1) list.scrollTo({ left: tabs[i].offsetLeft - 16, behavior: smooth ? 'smooth' : 'instant' }); }
      if (quiet || was < 0) { place(list, false); reveal(false); return; }
      arrive(list, tabs[i]); place(list, true); reveal(true);
    }
    function spy() { if (!lock) setCurrent(pick()); }
    function onScroll() { if (tick || lock) return; tick = true; requestAnimationFrame(function () { tick = false; spy(); }); }
    function stop() { if (raf) cancelAnimationFrame(raf); raf = 0; lock = false; }
    (win ? window : scroller).addEventListener('scroll', onScroll, { passive: true });
    ['wheel', 'touchstart', 'keydown'].forEach(function (ev) { (win ? window : scroller).addEventListener(ev, stop, { passive: true }); });
    window.addEventListener('resize', function () { setCurrent(pick(), true); });

    var bez = (getComputedStyle(html).getPropertyValue('--ease-decelerate-generic').match(/[\d.]+/g) || [.16, .38, .58, 1]).map(Number);
    function ease(t) {   /* CSS cubic-bezier(x1,y1,x2,y2): solve x(s)=t by bisection, return y(s) */
      var lo = 0, hi = 1, s = t;
      for (var n = 0; n < 24; n++) { s = (lo + hi) / 2; var x = 3 * (1 - s) * (1 - s) * s * bez[0] + 3 * (1 - s) * s * s * bez[2] + s * s * s; if (x < t) lo = s; else hi = s; }
      return 3 * (1 - s) * (1 - s) * s * bez[1] + 3 * (1 - s) * s * s * bez[3] + s * s * s;
    }
    list.addEventListener('click', function (e) {
      var a = e.target.closest('a.tab'), i = tabs.indexOf(a), t = targets[i];
      if (!a || !t || e.defaultPrevented || e.button || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
      e.preventDefault(); stop(); lock = true; setCurrent(i);
      var from = pos(), to = Math.max(0, Math.min(max(), from + t.getBoundingClientRect().top - vTop() - offset() - (parseFloat(getComputedStyle(t).scrollMarginTop) || 0)));
      var dist = Math.abs(to - from), share = dist / vH();   /* the duration follows the distance: fast-3, fast-4, medium-2, slow-1 */
      var dur = share <= .25 ? token('--duration-fast-3', 150) : share <= .5 ? token('--duration-fast-4', 200) : share <= 1 ? token('--duration-medium-2', 300) : token('--duration-slow-1', 450);
      if (list.dataset.tabsHash !== 'off') history.pushState(null, '', a.getAttribute('href'));
      t.setAttribute('tabindex', '-1'); t.focus({ preventScroll: true });
      if (matchMedia('(prefers-reduced-motion: reduce)').matches || !dist) { jumpTo(to); lock = false; return; }
      var t0 = performance.now();
      (function step(now) {
        var p = Math.min(1, (now - t0) / dur);
        jumpTo(from + (to - from) * ease(p));
        if (p < 1) raf = requestAnimationFrame(step); else { raf = 0; lock = false; }
      })(t0);
    });
    setCurrent(pick(), true);
    window.addEventListener('load', function () { setCurrent(pick(), true); });
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { setCurrent(pick(), true); });
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

      if (list.classList.contains('tab-bar--page')) pageNav(list);

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
