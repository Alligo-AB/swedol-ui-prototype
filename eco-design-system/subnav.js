/* ECO doc pages: the sticky .ds-subnav gets .is-stuck (a hairline under it) while it is stuck to the
   top, and the chip for the section in view gets aria-current. */
(function () {
  var nav = document.querySelector('.ds-subnav');
  if (!nav || !('IntersectionObserver' in window)) return;

  var hdr = parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--dn-bar')) || 0;   // fixed mobile header of the doc navigation (docnav.css), 0 without it
  new IntersectionObserver(function (entries) {
    nav.classList.toggle('is-stuck', entries[0].intersectionRatio < 1);
  }, { threshold: [1], rootMargin: '-' + (1 + hdr) + 'px 0px 0px 0px' }).observe(nav);

  /* Swipeable row: fades at the edges + drag-to-scroll with a mouse */
  var row = nav.querySelector('.ds-toc, .tab-bar');
  function fades() {
    var over = row.scrollWidth > row.clientWidth + 1;
    row.classList.toggle('is-scrollable', over);
    row.style.setProperty('--fade-l', over && row.scrollLeft > 1 ? '24px' : '0px');
    row.style.setProperty('--fade-r', over && row.scrollLeft < row.scrollWidth - row.clientWidth - 1 ? '24px' : '0px');
  }
  row.addEventListener('scroll', fades, { passive: true });
  window.addEventListener('resize', fades);
  fades();
  var down = null, moved = false;
  row.addEventListener('pointerdown', function (e) {
    if (e.pointerType !== 'mouse' || e.button !== 0 || !row.classList.contains('is-scrollable')) return;
    down = { x: e.clientX, left: row.scrollLeft }; moved = false;
  });
  window.addEventListener('pointermove', function (e) {
    if (!down) return;
    var dx = e.clientX - down.x;
    if (!moved && Math.abs(dx) > 5) { moved = true; row.classList.add('is-dragging'); }
    if (moved) row.scrollLeft = down.left - dx;
  });
  window.addEventListener('pointerup', function () { down = null; row.classList.remove('is-dragging'); });
  row.addEventListener('click', function (e) { if (moved) { e.preventDefault(); e.stopPropagation(); moved = false; } }, true);

  var links = [].slice.call(nav.querySelectorAll('a[href^="#"]'));
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (e) {
      if (!e.isIntersecting) return;
      links.forEach(function (a) {
        var on = a.getAttribute('href') === '#' + e.target.id;
        if (on) a.setAttribute('aria-current', 'true'); else a.removeAttribute('aria-current');
        var row = a.closest('.ds-toc, .tab-bar');   // keep the active chip visible when the row scrolls sideways
        if (on && row.scrollWidth > row.clientWidth) row.scrollTo({ left: a.offsetLeft - 16, behavior: 'smooth' });
      });
    });
  }, { rootMargin: '-25% 0px -65% 0px' });
  links.forEach(function (a) { var s = document.getElementById(a.getAttribute('href').slice(1)); if (s) io.observe(s); });

  /* ── Smooth jump to a section (eco-motion) ──────────────────────────────────────────────
     Easing: decelerate-emphasized (content comes in fast and settles softly).
     Duration follows distance as share of the viewport: <=25% fast-4, <=50% medium-2, <=100% slow-1, more slow-4.
     Pages with <div class="ds-doc" data-subnav="tabs": ease-decelerate-generic (ease out) and one duration step faster:
     <=25% fast-3, <=50% fast-4, <=100% medium-2, more slow-1.
     Values are read from the CSS custom properties in docs.css. Reduced motion: instant jump. */
  var cs = getComputedStyle(document.documentElement);
  function ms(name, fallback) { return parseFloat(cs.getPropertyValue(name)) || fallback; }
  var quick = !!document.querySelector('.ds-doc[data-subnav="tabs"]');
  var bez = (cs.getPropertyValue(quick ? '--ease-decelerate-generic' : '--ease-decelerate-emphasized').match(/[\d.]+/g) || (quick ? [.16, .38, .58, 1] : [.16, 0, .16, 1])).map(Number);
  function cubic(t) {                       // CSS cubic-bezier(x1,y1,x2,y2): solve x(s)=t by bisection, return y(s)
    var lo = 0, hi = 1, s = t;
    for (var i = 0; i < 24; i++) {
      s = (lo + hi) / 2;
      var x = 3 * (1 - s) * (1 - s) * s * bez[0] + 3 * (1 - s) * s * s * bez[2] + s * s * s;
      if (x < t) lo = s; else hi = s;
    }
    return 3 * (1 - s) * (1 - s) * s * bez[1] + 3 * (1 - s) * s * s * bez[3] + s * s * s;
  }
  var raf = 0;
  function stop() { if (raf) { cancelAnimationFrame(raf); raf = 0; } }
  ['wheel', 'touchstart', 'keydown'].forEach(function (ev) { window.addEventListener(ev, stop, { passive: true }); });

  document.addEventListener('click', function (e) {   // the chip row and the side list (toc.js)
    var a = e.target.closest('.ds-subnav a[href^="#"], .ds-sidetoc a[href^="#"]');
    var target = a && document.getElementById(a.getAttribute('href').slice(1));
    if (!target || e.defaultPrevented || e.metaKey || e.ctrlKey || e.shiftKey) return;
    e.preventDefault();
    stop();
    var from = window.pageYOffset;
    var max = document.documentElement.scrollHeight - window.innerHeight;
    var sep = quick && target.previousElementSibling && target.previousElementSibling.querySelector('hr.divider');   // section divider right above the target
    var barH = nav.offsetParent === null ? 0 : nav.getBoundingClientRect().height;   // the sticky bar is hidden from 1024px
    var to = Math.max(0, Math.min(max, sep ? sep.getBoundingClientRect().top + from - Math.max(0, barH - 2) : target.getBoundingClientRect().top + from - (parseFloat(getComputedStyle(target).scrollMarginTop) || 0)));   // tabs pages: the divider line stops 1px further up, behind the bar and its own bottom line
    to = Math.max(0, to - (parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--dn-bar')) || 0));   // clear the fixed header
    var dist = Math.abs(to - from), share = dist / window.innerHeight;
    var dur = quick
      ? (share <= .25 ? ms('--duration-fast-3', 150) : share <= .5 ? ms('--duration-fast-4', 200) : share <= 1 ? ms('--duration-medium-2', 300) : ms('--duration-slow-1', 450))
      : (share <= .25 ? ms('--duration-fast-4', 200) : share <= .5 ? ms('--duration-medium-2', 300) : share <= 1 ? ms('--duration-slow-1', 450) : ms('--duration-slow-4', 600));
    history.pushState(null, '', a.getAttribute('href'));
    target.setAttribute('tabindex', '-1');
    target.focus({ preventScroll: true });
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches || !dist) { window.scrollTo({ top: to, left: 0, behavior: 'instant' }); return; }
    var t0 = performance.now();
    (function step(now) {
      var p = Math.min(1, (now - t0) / dur);
      window.scrollTo({ top: from + (to - from) * cubic(p), left: 0, behavior: 'instant' });   // instant: html { scroll-behavior: smooth } would otherwise smooth every frame and stretch the duration
      raf = p < 1 ? requestAnimationFrame(step) : 0;
    })(t0);
  });
})();

/* Keyboard focus ring for the doc text fields: html[data-kbd] is set after a Tab key and cleared on a pointer press (docs.css) */
(function () {
  var r = document.documentElement;
  document.addEventListener('keydown', function (e) { if (e.key === 'Tab') { r.setAttribute('data-kbd', ''); document.body.classList.add('keyboard-nav'); } }, true);
  document.addEventListener('pointerdown', function () { r.removeAttribute('data-kbd'); document.body.classList.remove('keyboard-nav'); }, true);  /* body.keyboard-nav: the focus ring of the shared components (eco-input …) */
})();
