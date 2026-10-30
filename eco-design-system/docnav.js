/* ECO doc site navigation: builds the Navigation Rail + Secondary navigation panel (docnav.css, from 961px).
   Load it right after <body> (so the page does not jump) and link docnav.css. The page list below is the single source.
   Current page = file name without .html and without -specifications / -code / -storyblok. Pages in no category (the start page) get the rail only. */
document.documentElement.classList.add('ds-frame');   // framed layout on every page that has the navigation (docnav.css, from 961px)
(function () {
  var D = '/eco-design-system/';
  function c(id, t, extra) { var o = { id: id, t: t, href: D + 'components/' + id + '.html' }; for (var k in extra) o[k] = extra[k]; return o; }
  function f(id, t) { return { id: id, t: t, href: D + 'foundations/' + id + '.html' }; }

  function r(id, t) { return { id: id, t: t, href: D + 'resources/' + id + '.html' }; }

  var NAV = {
    foundations: {
      label: 'Foundations', icon: 'grid_view',
      overview: { id: 'foundations-overview', t: 'Foundations Overview', href: D + 'foundations-overview.html' },
      groups: [
        { items: [f('colors', 'Colors'), f('typography', 'Typography'), f('layout', 'Layout'), f('elevation', 'Shadows & Elevation'), f('motion', 'Motion')] }
      ]
    },
    components: {
      label: 'Components', icon: 'palette',
      overview: { id: 'components-overview', t: 'Component Overview', href: D + 'components-overview.html' },
      groups: [
        { title: 'Actions', items: [c('button', 'Button'), c('button-group', 'Button group')] },
        { title: 'Form', items: [c('checkbox', 'Checkbox'), c('chip', 'Chip'), c('input', 'Input'), c('textarea', 'Text area'), c('radio', 'Radio button'), c('select', 'Select'), c('switch', 'Switch'), c('tabs', 'Tabs'), c('segment-control', 'Pill segment control'), c('range', 'Range'), c('icon-picker', 'Icon picker')] },
        { title: 'Notifications', items: [c('notifications', 'Notifications', { children: [c('toast', 'Toast'), c('toast-ecom', 'E-Com Toast'), c('modal', 'Modal'), c('banner', 'Banner'), c('inline', 'Inline notification')] })] },
        { title: 'Menus, lists and dividers', items: [c('menu', 'Menu'), c('list-item', 'List Item'), c('divider', 'Divider')] },
        { title: 'Links', items: [c('links-guide', 'Links', { children: [c('inline-link', 'Inline link'), c('action-link', 'Action link'), c('tile-link', 'Tile link')] })] },
        { title: 'Status and navigation', items: [c('badge', 'Badge', { children: [c('badge-basic', 'Basic'), c('badge-dot', 'Dot'), c('badge-number', 'Number'), c('badge-product-discount', 'Product & Discount'), c('badge-purchase-info', 'Purchase Info')] }), c('breadcrumb', 'Breadcrumb', { children: [c('breadcrumb-base', 'Base')] }), c('pagination', 'Pagination'), c('tag', 'Tag'), c('tooltip', 'Tooltip')] },
        { title: 'Layout and content', items: [c('section', 'Section'), c('collapsible', 'Collapsible')] },
        { title: 'Cards', items: [c('cards', 'Cards', { children: [c('ah-group-card-widget-storyblok', 'Article Highlight Group Card', { sb: true }), c('ah-single-row-card-widget', 'Article Highlight Single Row Card')] })] },
        { title: 'Patterns', items: [c('patterns-overview', 'Patterns overview'), c('breadcrumb-bar', 'Breadcrumb Bar'), c('hero-banner-widget', 'Hero banner'), { id: 'splash-card-carousel', t: 'Splash card carousel', soon: true }] },
        { title: 'Storyblok widget', items: [c('hero-banner-widget-storyblok', 'Hero banner widget', { sb: true }), c('ah-group-card-widget-storyblok', 'AH Group widget', { sb: true }), c('ah-single-row-card-widget-storyblok', 'AH Single Row widget', { sb: true }), c('collapsible-storyblok', 'Collapsible', { sb: true })] },
        { title: 'Drafts', items: [c('role-tier-card', 'Role tier card')] }
      ]
    },
    tokens: {
      label: 'Tokens', icon: 'token', direct: true,   // one page, no Secondary navigation panel
      overview: { id: 'tokens', t: 'Design Tokens', href: D + 'tokens.html' },
      groups: []
    },
    resources: {
      label: 'Resources', icon: 'menu_book',
      overview: { id: 'resources-overview', t: 'Resources Overview', href: D + 'resources-overview.html' },
      groups: [
        { title: 'Libraries', items: [r('web', 'Web'), r('design', 'Design')] },
        { title: 'Help', items: [r('getting-help', 'Getting help')] },
        { title: 'User guides', items: [r('introduction-for-developers', 'Introduction for Developers'), r('introduction-for-stakeholders', 'Introduction for Stakeholders')] }
      ]
    }
  };

  window.ECO_NAV = NAV;   // read by the start page (index.html) to count the pages live

  var pageId = decodeURIComponent(location.pathname).replace(/\/+$/, '').split('/').pop().replace(/\.html$/, '').replace(/-(specifications|code|storyblok|usage|reference|primitives|tokens|breakpoints|spacing)$/, '');
  var fullId = decodeURIComponent(location.pathname).replace(/\/+$/, '').split('/').pop().replace(/\.html$/, '');   // file name incl. -storyblok: the Storyblok group items match on it
  var cur = null;   // { cat, id }
  Object.keys(NAV).forEach(function (k) {
    var n = NAV[k];
    if (n.overview.id === pageId) cur = { cat: k };
    n.groups.forEach(function (g) {
      g.items.forEach(function (it) {
        if (it.id === pageId) cur = { cat: k };
        (it.children || []).forEach(function (ch) { if (ch.id === pageId || ch.id === fullId) cur = { cat: k }; });
      });
    });
  });

  var root = document.documentElement;
  var hasPanel = !!cur && !NAV[cur.cat].direct;
  if (hasPanel) root.classList.add('dn-has-panel');

  /* Arriving through a link to a #heading on another page of the docs (same site, other page): the navigation comes in first, then the page fades in with a small scroll to the heading.
     The classes are set here, before the first paint, so the content never flashes. Reduced motion: nothing of this happens (the page jumps straight to the heading, toc.js). */
  var arriving = false;
  try {
    var rf = new URL(document.referrer);
    var nt = performance.getEntriesByType && performance.getEntriesByType('navigation')[0];   // a link click, not reload or back/forward
    var skip = +sessionStorage.getItem('dn-noarrive') || 0; sessionStorage.removeItem('dn-noarrive');   // set by a click inside the navigation itself (below)
    arriving = Date.now() - skip > 4000 && (!nt || nt.type === 'navigate') && rf.origin === location.origin && rf.pathname !== location.pathname && !window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  } catch (e) {}
  if (arriving) root.classList.add('dn-arriving');
  if (arriving && hasPanel && window.matchMedia('(min-width: 1600px)').matches) root.classList.add('dn-hold');   // from 1600px the pinned panel slides out
  if (arriving && window.matchMedia('(min-width: 961px) and (max-width: 1599px)').matches) root.classList.add('dn-hold-rail');   // 961-1599px: the Navigation Rail itself slides in from the left

  function esc(s) { return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;'); }
  function link(it, cls) {
    if (it.soon) return '<span class="dn-link dn-link--soon" aria-disabled="true">' + esc(it.t) + '</span>';
    var here = it.sb ? it.id === fullId : it.id === pageId && !/-storyblok$/.test(fullId);
    return '<a class="dn-link' + (cls ? ' ' + cls : '') + '" href="' + it.href + '"' + (here ? ' aria-current="page"' : '') + '><span class="dn-link__t">' + esc(it.t) + '</span></a>';
  }
  function panelHtml(key) {
    var n = NAV[key];
    // the overview is the start page of the category: category icon, arrow and a line below it set it apart from the pages (trial 2026-10-30)
    var o = n.overview;
    var h = '<div class="dn-item dn-item--overview"><a class="dn-link dn-link--overview" href="' + o.href + '"' + (o.id === pageId ? ' aria-current="page"' : '') + '>' +
      '<span class="dn-ms dn-link__ico" aria-hidden="true">' + n.icon + '</span><span class="dn-link__t">' + esc(o.t) + '</span></a></div>';
    // Trial 2026-10-28: no group titles, one A-Z list after the overview (group titles stay in NAV for search and the start page); Storyblok widget and Drafts keep their titles, last
    var all = [], kept = n.groups.filter(function (g) { return g.title === 'Storyblok widget' || g.title === 'Drafts'; });
    n.groups.forEach(function (g) { if (kept.indexOf(g) > -1) return; g.items.forEach(function (it) { if (!all.some(function (a) { return a.href && a.href === it.href; })) all.push(it); }); });
    all.sort(function (a, b) { return a.t.localeCompare(b.t, 'en', { sensitivity: 'base' }); });
    [{ items: all }].concat(kept).forEach(function (g) {
      if (g.title) h += '<div class="dn-group">' + esc(g.title) + '</div>';
      g.items.forEach(function (it) {
        if (!it.children) { h += '<div class="dn-item">' + link(it) + '</div>'; return; }
        var open = it.id === pageId || it.children.some(function (ch) { return ch.id === pageId || ch.id === fullId; });
        h += '<div class="dn-item dn-item--parent">' + link(it) +
          '<button class="dn-chev" type="button" aria-expanded="' + open + '" aria-label="' + esc(it.t) + ' pages"><span class="dn-ms" aria-hidden="true">expand_more</span></button></div>' +
          '<div class="dn-sub"' + (open ? '' : ' hidden') + '>' + it.children.map(function (ch) { return '<div class="dn-item">' + link(ch) + '</div>'; }).join('') + '</div>';
      });
    });
    return h;
  }

  var dest = Object.keys(NAV).map(function (k) {
    return '<a class="dn-dest" href="' + NAV[k].overview.href + '" data-cat="' + k + '"' + (cur && cur.cat === k ? ' aria-current="true"' : '') + '>' +
      '<span class="dn-ms" aria-hidden="true">' + NAV[k].icon + '</span><span>' + NAV[k].label + '</span></a>';
  }).join('');

  var wrap = document.createElement('div');
  wrap.className = 'dn';
  wrap.innerHTML =
    '<nav class="dn-rail" aria-label="ECO Design System">' +
      '<div class="dn-rail__top">' +
        '<a class="dn-home" href="' + D + '" aria-label="ECO Design System, start page"' + (pageId === 'index' ? ' aria-current="page"' : '') + '><span class="dn-home__mark"></span><span>ECO<br>Design<br>System<br>V.1</span></a>' +
        dest +
      '</div><div class="dn-rail__gap"></div>' +
      '<div class="dn-rail__tools"><button class="dn-dest" type="button" data-search><span class="dn-ms" aria-hidden="true">search</span><span>Search</span></button><hr><button class="dn-tool" type="button" aria-label="Dark mode" data-dark disabled><span class="dn-ms" aria-hidden="true">dark_mode</span></button></div>' +
    '</nav>' +
    '<nav class="dn-panel" id="dn-panel" aria-label="Pages"></nav>';
  document.body.insertBefore(wrap, document.body.firstChild);

  var panel = wrap.querySelector('.dn-panel'), shown = null, timer = 0;
  var pinned = window.matchMedia('(min-width: 1600px)');
  var cs = getComputedStyle(root), still = window.matchMedia('(prefers-reduced-motion: reduce)'), swap = 0;
  function ms(n, d) { return parseFloat(cs.getPropertyValue(n)) || d; }
  function fill(key) { panel.innerHTML = '<div class="dn-body">' + panelHtml(key) + '</div>'; panel.scrollTop = 0; }
  function show(key) {
    if (shown === key || NAV[key].direct) return;
    shown = key;
    var id = ++swap, old = panel.firstElementChild;
    if (!old || !wrap.classList.contains('is-ready') || still.matches || getComputedStyle(panel).visibility !== 'visible') { fill(key); return; }
    // visible panel: old list fades out (eco-motion accelerate-ish: standard, fast-4), new list fades in (decelerate-emphasized, medium-2); no movement
    var out = old.animate([{ opacity: 1 }, { opacity: 0 }], { duration: ms('--duration-fast-4', 200), easing: cs.getPropertyValue('--ease-standard') || 'ease', fill: 'forwards' });
    out.onfinish = function () {
      if (id !== swap) return;   // a newer hover took over
      fill(key);
      panel.firstElementChild.animate([{ opacity: 0 }, { opacity: 1 }],
        { duration: 400 /* between medium-2 (300) and slow-1 (450): tested value, no token */, easing: cs.getPropertyValue('--ease-decelerate-emphasized') || 'ease-out' });
    };
  }
  function open(key) { if (NAV[key].direct) { close(); return; } clearTimeout(timer); show(key); wrap.classList.add('is-open'); }
  function close() {
    clearTimeout(timer);
    wrap.classList.remove('is-open');
    if (hasPanel && pinned.matches) show(cur.cat);   // pinned: back to the category of this page
  }
  function later() { clearTimeout(timer); timer = setTimeout(close, 150); }

  if (hasPanel) { show(cur.cat); try { panel.scrollTop = +sessionStorage.getItem('dn-scroll') || 0; } catch (e) {} }
  function reveal() {   // keep the current page's item inside the panel (the panel may be hidden: measure by offset, not by rect)
    var on = panel.querySelector('[aria-current="page"]');
    if (!on) return;
    var top = on.getBoundingClientRect().top - panel.getBoundingClientRect().top + panel.scrollTop, h = on.offsetHeight;
    if (top < panel.scrollTop + 8 || top + h > panel.scrollTop + panel.clientHeight - 8) panel.scrollTop = top - panel.clientHeight / 2;
  }
  if (hasPanel) reveal();
  requestAnimationFrame(function () { requestAnimationFrame(function () { wrap.classList.add('is-ready'); root.classList.add('dn-anim'); }); });   // no slide on page load
  /* The window crosses 1600px: the pinned panel slides in or out. Animated here (Web Animations) rather than by the CSS transition, whose visibility delay left the panel invisible while the page had already moved (a white strip). */
  pinned.addEventListener('change', function () {
    if (still.matches || !panel.animate) return;
    var out = !pinned.matches, hidden = 'translateX(calc(-100% - var(--dn-rail)))';
    panel.animate(out ? [{ transform: 'none', visibility: 'visible' }, { transform: hidden, visibility: 'visible' }] : [{ transform: hidden, visibility: 'visible' }, { transform: 'none', visibility: 'visible' }],
      { duration: ms('--duration-medium-2', 300), easing: (out ? cs.getPropertyValue('--ease-accelerate-generic') : cs.getPropertyValue('--ease-decelerate-generic')) || (out ? 'cubic-bezier(.36,.09,1,.58)' : 'cubic-bezier(.16,.38,.58,1)') });   // eco-motion: in = decelerate-generic, out = accelerate-generic
  });

  if (arriving) (function () {
    var wide = hasPanel && pinned.matches;   // the pinned Secondary navigation panel (from 1600px) slides out; below 1600px the Navigation Rail slides in
    var bez = (cs.getPropertyValue('--ease-decelerate-emphasized').match(/[\d.]+/g) || [.16, 0, .16, 1]).map(Number);
    function cubic(t) { var lo = 0, hi = 1, q = t; for (var i = 0; i < 24; i++) { q = (lo + hi) / 2; var x = 3 * (1 - q) * (1 - q) * q * bez[0] + 3 * (1 - q) * q * q * bez[2] + q * q * q; if (x < t) lo = q; else hi = q; } return 3 * (1 - q) * (1 - q) * q * bez[1] + 3 * (1 - q) * q * q * bez[3] + q * q * q; }
    var railIn = root.classList.contains('dn-hold-rail'), navMs = railIn ? ms('--duration-medium-4', 400) : wide ? ms('--duration-medium-2', 300) : 0, fadeMs = ms('--duration-slow-3', 550), loaded = 0, navDone = false, landed = false;
    function release() { root.classList.remove('dn-arriving', 'dn-hold', 'dn-hold-rail'); }
    function land() {   // 2. the page fades in, with a small scroll to the heading (toc.js has already put the heading in place, behind the veil)
      if (landed) return; landed = true;
      var tg = document.getElementById(decodeURIComponent(location.hash.slice(1)));
      if (tg) tg.scrollIntoView({ block: 'start', behavior: 'instant' });   // the layout may have moved since the first jump (late font swap)
      var y = window.pageYOffset, off = Math.min(y, 120);
      root.classList.remove('dn-arriving'); root.classList.add('dn-landing');
      if (off > 2) {
        window.scrollTo({ top: y - off, left: 0, behavior: 'instant' });
        var t0 = performance.now();
        (function step(now) {
          var p = Math.min(1, (now - t0) / fadeMs);
          window.scrollTo({ top: y - off + off * cubic(p), left: 0, behavior: 'instant' });   // instant: html { scroll-behavior: smooth } would smooth every frame
          if (p < 1) requestAnimationFrame(step);
        })(t0);
      }
      setTimeout(function () { root.classList.remove('dn-landing'); if (wide) close(); }, fadeMs + 600);   // clears is-open again; the pinned panel stays
    }
    function nav() {    // 1. the navigation first: the Secondary navigation panel slides out from the left
      if (railIn) {   // below 1600px the Navigation Rail is the part that slides in (decelerate-emphasized)
        wrap.querySelector('.dn-rail').animate([{ transform: 'translateX(-100%)' }, { transform: 'none' }], { duration: navMs, easing: cs.getPropertyValue('--ease-decelerate-emphasized') || 'cubic-bezier(.16,0,.16,1)' });
      }
      root.classList.remove('dn-hold', 'dn-hold-rail');
      if (wide) open(cur.cat);   // pinned: is-open removes the visibility delay, so the panel really slides out
      setTimeout(function () { navDone = true; tryLand(); }, wide ? navMs + 120 : 0);   // from 1600px: after the panel has slid out; below: the page starts fading in together with the rail slide (fade length unchanged)
    }
    function tryLand() { if (navDone && loaded >= 2) land(); }
    function ready() { loaded++; tryLand(); }
    // wait for the first frames (the panel must have its transition), then the navigation, then the page (fonts and images loaded)
    requestAnimationFrame(function () { requestAnimationFrame(function () { setTimeout(nav, 80); }); });
    if (document.readyState === 'complete') ready(); else window.addEventListener('load', ready);
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(ready); else ready();
    setTimeout(function () { release(); land(); }, 5000);   // never leave the page hidden
  })();

  wrap.addEventListener('mouseover', function (e) {
    var d = e.target.closest('.dn-dest[data-cat]');
    if (d) open(d.getAttribute('data-cat'));
    else if (e.target.closest('.dn-rail')) later();   // another rail item: let the panel go
    else clearTimeout(timer);                         // inside the panel
  });
  wrap.addEventListener('mouseleave', later);
  wrap.addEventListener('focusin', function (e) {
    var d = e.target.closest('.dn-dest[data-cat]');
    if (d) open(d.getAttribute('data-cat'));
  });
  wrap.addEventListener('focusout', function (e) { if (!e.relatedTarget || !wrap.contains(e.relatedTarget)) later(); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });

  function sameUrl(a) { return a.origin === location.origin && a.pathname.replace(/\.html$/, '') === location.pathname.replace(/\.html$/, '') && (!a.hash || a.hash === location.hash); }
  document.addEventListener('click', function (e) {   // the tab bar of a component (Examples / Specifications / Code / Storyblok): the same component, no arrival sequence
    var t = e.target.closest && e.target.closest('.ds-tabs a.tab');
    if (t && !sameUrl(t)) { try { sessionStorage.setItem('dn-noarrive', Date.now()); } catch (err) {} }
  });
  wrap.querySelector('.dn-rail').addEventListener('click', function (e) {   // any category in the rail (hover has already opened its panel): no reload, no arrival sequence
    var d = e.target.closest('a.dn-dest[data-cat], a.dn-home');   // the home button too: the rail is already out, it must not slide in again
    if (!d) return;
    if (sameUrl(d)) { e.preventDefault(); return; }
    try { sessionStorage.setItem('dn-noarrive', Date.now()); } catch (err) {}
  });
  panel.addEventListener('click', function (e) {
    var ch = e.target.closest('.dn-chev');
    if (ch) {
      var sub = ch.parentNode.nextElementSibling, on = ch.getAttribute('aria-expanded') !== 'true';
      ch.setAttribute('aria-expanded', on); sub.hidden = !on;
      return;
    }
    var pa = e.target.closest('a');
    if (pa && sameUrl(pa)) { e.preventDefault(); return; }   // the page you are on: no reload
    if (pa) {
      try { sessionStorage.setItem('dn-scroll', panel.scrollTop); sessionStorage.setItem('dn-noarrive', Date.now()); } catch (err) {}   // a link in the panel: the panel stays, no arrival sequence
      wrap.classList.remove('is-open');   // slides back in while the next page loads
    }
  });
  /* ── Mobile (below 961px): header bar + drawer. Level 1 = categories, level 2 = the pages of one category ── */
  var cats = Object.keys(NAV);
  var bar = document.createElement('div');
  bar.innerHTML =
    '<header class="dn-bar">' +
      '<button class="btn btn--blank btn--md btn--icon dn-bar__btn" type="button" aria-expanded="false" aria-controls="dn-drawer" aria-label="Menu"><span class="btn__icon" aria-hidden="true">menu</span></button>' +
      '<span class="dn-bar__div" aria-hidden="true"></span>' +
      '<a class="btn btn--blank btn--md dn-bar__id" href="' + D + '"><span class="btn__label"><span class="dn-bar__mark"></span><span>ECO Design System <span class="dn-bar__v">V.1</span></span></span></a>' +
      '<button class="btn btn--blank btn--md btn--icon dn-bar__search" type="button" data-search aria-label="Search"><span class="btn__icon" aria-hidden="true">search</span></button></header>' +
    '<div class="dn-scrim"></div>' +
    '<nav class="dn-drawer" id="dn-drawer" aria-label="ECO Design System">' +
      '<div class="dn-drawer__bar">' +
        '<button class="btn btn--blank btn--md btn--icon dn-drawer__btn" type="button" aria-label="Close menu"><span class="btn__icon" aria-hidden="true">menu_open</span></button>' +
        '<span class="dn-bar__div" aria-hidden="true"></span>' +
        '<a class="btn btn--blank btn--md dn-bar__id" href="' + D + '"><span class="btn__label"><span class="dn-bar__mark"></span><span>ECO Design System <span class="dn-bar__v">V.1</span></span></span></a>' +
      '</div>' +
      '<div class="dn-lv dn-lv1">' +
        cats.map(function (k) {
          if (NAV[k].direct) return '<a class="dn-mrow" href="' + NAV[k].overview.href + '"' + (cur && cur.cat === k ? ' aria-current="true"' : '') + '><span class="dn-ms dn-ms--sm dn-mrow__ico" aria-hidden="true">' + NAV[k].icon + '</span><span class="dn-mrow__t">' + NAV[k].label + '</span></a>';
          return '<button class="dn-mrow" type="button" data-cat="' + k + '"' + (cur && cur.cat === k ? ' aria-current="true"' : '') + '><span class="dn-ms dn-ms--sm dn-mrow__ico" aria-hidden="true">' + NAV[k].icon + '</span><span class="dn-mrow__t">' + NAV[k].label + '</span><span class="dn-ms dn-ms--sm" aria-hidden="true">arrow_right_alt</span></button>';
        }).join('') +
        '<div class="dn-lv1__gap"></div>' +
        '<div class="dn-lv1__tools"><button class="dn-mrow" type="button" data-search><span class="dn-ms dn-ms--sm dn-mrow__ico" aria-hidden="true">search</span><span class="dn-mrow__t">Sök</span></button><hr><button class="dn-dark" type="button" data-dark disabled><span class="dn-ms" aria-hidden="true">dark_mode</span><span>Dark mode</span></button></div>' +
      '</div>' +
      '<div class="dn-lv dn-lv2"><button class="dn-mrow dn-back" type="button"><span class="dn-ms dn-ms--sm dn-mrow__ico" aria-hidden="true">arrow_back</span><span class="dn-mrow__t">Main menu</span></button><div class="dn-lv2__body"></div></div>' +
    '</nav>';
  while (bar.firstChild) wrap.appendChild(bar.firstChild);

  var drawer = wrap.querySelector('.dn-drawer'), btn = wrap.querySelector('.dn-bar__btn'), body2 = wrap.querySelector('.dn-lv2__body'), lv2 = wrap.querySelector('.dn-lv2'), lv1 = wrap.querySelector('.dn-lv1');
  var mobile = window.matchMedia('(max-width: 960px)');
  function level(key) {   // key = category (level 2) or null (level 1)
    if (key) body2.innerHTML = panelHtml(key);
    drawer.classList.toggle('is-l2', !!key);
    lv2.scrollTop = 0;
    var on = key && body2.querySelector('[aria-current="page"]');   // show the current page: scroll it to the middle of the drawer
    if (on) lv2.scrollTop = Math.max(0, on.getBoundingClientRect().top - lv2.getBoundingClientRect().top - (lv2.clientHeight - on.offsetHeight) / 2);
  }
  function openDrawer() {
    level(hasPanel ? cur.cat : null);   // on a page of a category the menu opens straight on its pages
    drawer.classList.add('is-open'); wrap.classList.add('is-drawer');
    requestAnimationFrame(function () { level(hasPanel ? cur.cat : null); });   // once more after layout/fonts have settled
    btn.setAttribute('aria-expanded', 'true'); btn.firstChild.textContent = 'menu_open'; root.classList.add('dn-lock');
  }
  function closeDrawer() {
    if (!drawer.classList.contains('is-open')) return;
    drawer.classList.remove('is-open'); wrap.classList.remove('is-drawer');
    btn.setAttribute('aria-expanded', 'false'); btn.firstChild.textContent = 'menu'; root.classList.remove('dn-lock');
  }
  btn.addEventListener('click', function () { if (drawer.classList.contains('is-open')) { closeDrawer(); } else { openDrawer(); } });
  wrap.querySelector('.dn-scrim').addEventListener('click', closeDrawer);
  drawer.addEventListener('click', function (e) {
    if (e.target.closest('.dn-drawer__btn')) { closeDrawer(); return; }
    var cat = e.target.closest('.dn-mrow[data-cat]');
    if (cat) { level(cat.getAttribute('data-cat')); return; }
    if (e.target.closest('.dn-back')) { drawer.classList.remove('is-l2'); return; }
    var ch = e.target.closest('.dn-chev');
    if (ch) { var on = ch.getAttribute('aria-expanded') !== 'true'; ch.setAttribute('aria-expanded', on); ch.parentNode.nextElementSibling.hidden = !on; return; }
    if (e.target.closest('a')) closeDrawer();
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') closeDrawer(); });
  var wide = window.matchMedia('(min-width: 961px)');
  (wide.addEventListener ? wide.addEventListener.bind(wide, 'change') : wide.addListener.bind(wide))(function () { if (wide.matches) closeDrawer(); });
  /* ── Search: modal with instant results, grouped by category (Components, Foundations) ── */
  /* Swedish search words per page (search only: results always show the English title). Comma separated; accents are ignored when matching. */
  var SV = {
    tokens: 'designtokens, tokens, variabler, css-variabler, värden, färgvärden, typografivärden',
    colors: 'färg, färger, färgpalett, nyans', typography: 'typografi, typsnitt, teckensnitt, text, rubrik, font', layout: 'layout, rutnät, grid, brytpunkt, brytpunkter, breakpoint, responsiv, kolumner, marginal, avstånd, mellanrum, luft, padding, spacing',
    elevation: 'skugga, skuggor, höjd, djup, lager', motion: 'rörelse, animation, animering, övergång, tid',
    button: 'knapp, knappar', 'button-group': 'knappgrupp, knappar, grupp', checkbox: 'kryssruta, kryssrutor, markera, bockruta', input: 'inmatning, inmatningsfält, textfält, fält, formulär',
    textarea: 'textruta, textområde, flerradig, kommentar', radio: 'radioknapp, alternativ, val, väljare', select: 'rullgardin, rullista, väljare, lista, dropdown', 'switch': 'reglage, brytare, omkopplare, växla',
    tabs: 'flikar, flik', 'segment-control': 'segmentkontroll, växlare, segment, pill', range: 'skjutreglage, reglage, intervall, slider', 'icon-picker': 'ikonväljare, ikon, ikoner, symbol',
    notifications: 'notiser, notis, meddelanden, avisering, aviseringar, status', toast: 'snackbar, notis, meddelande, popup', 'toast-ecom': 'varukorg, kundvagn, tillagd, notis',
    modal: 'dialog, dialogruta, modalruta, popup, fönster', banner: 'banderoll, kampanj, driftmeddelande, notis', inline: 'infogad, varning, felmeddelande, meddelande, notis',
    menu: 'meny, rullgardinsmeny, dropdown', 'list-item': 'listobjekt, listrad, rad, lista', divider: 'avdelare, skiljelinje, delare, linje, separator',
    'links-guide': 'länkar, länk, hyperlänk, guide', 'inline-link': 'textlänk, länk i text, brödtext', 'action-link': 'åtgärdslänk, länk, fristående',
    'tile-link': 'länkkort, bricka, kort, ikonlänk', badge: 'märke, etikett, tagg, status, markering', breadcrumb: 'brödsmula, brödsmulor, sökväg, navigering', cards: 'kort, kortgrupp, artikel, kampanj', 'patterns-overview': 'mönster, pattern, komponent, skillnad, översikt, sammansatt', 'breadcrumb-base': 'brödsmula, enskild nivå, nivå, länk', 'breadcrumb-bar': 'brödsmulor, sökväg, navigering, rad, spår',
    pagination: 'sidnumrering, paginering, ladda fler, visa fler, sidor', tag: 'tagg, etikett, kategori, märkning, filter', 'tooltip': 'verktygstips, tips, hjälptext, ballong', section: 'sektion, avsnitt, block, yta',
    web: 'webb, storybook, bibliotek, kod, html, css', design: 'figma, bibliotek, komponenter, variabler', 'getting-help': 'hjälp, support, slack, feedback, fråga', 'introduction-for-developers': 'introduktion, utvecklare, kom igång, github, chromatic, jira', 'introduction-for-stakeholders': 'introduktion, intressenter, storybook, guide, kom igång', collapsible: 'fällbar, dragspel, expanderbar, fäll ut, accordion, faq', table: 'tabell, rader, kolumner, data', 'role-tier-card': 'rollkort, nivåkort, roller, behörighet, kort'
  };
  function fold(x) { return x.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, ''); }   // å ä ö → a a o: "farg" finds "färg"
  var entries = [];
  ['components', 'foundations'].forEach(function (k) {
    NAV[k].groups.forEach(function (g) {
      g.items.forEach(function (it) {
        if (it.soon) return;
        entries.push({ t: it.t, href: it.href, cat: NAV[k].label, group: g.title || '', sv: fold(SV[it.id] || ''), svl: (SV[it.id] || '').split(/,\s*/) });
        (it.children || []).forEach(function (ch) { entries.push({ t: ch.t, href: ch.href, cat: NAV[k].label, group: g.title || '', sv: fold(SV[ch.id] || ''), svl: (SV[ch.id] || '').split(/,\s*/) }); });
      });
    });
  });
  entries.push({ t: NAV.tokens.overview.t, href: NAV.tokens.overview.href, cat: 'Tokens', group: '', sv: fold(SV.tokens), svl: SV.tokens.split(/,\s*/) });
  var sm = document.createElement('div');
  sm.className = 'dn-search';
  sm.hidden = true;
  sm.innerHTML =
    '<div class="dn-search__scrim"></div>' +
    '<div class="dn-search__box" role="dialog" aria-modal="true" aria-label="Search">' +
      '<div class="dn-search__head">' +
        '<div class="form-field dn-search__field"><div class="input-wrap"><div class="input-box">' +
          '<span class="input-icon input-icon--lg" aria-hidden="true">search</span>' +
          '<input class="form-input" type="text" placeholder="Search components and foundations" aria-label="Search components and foundations" autocomplete="off" spellcheck="false" role="combobox" aria-expanded="true" aria-controls="dn-results" aria-autocomplete="list">' +
          '<div class="input-actions"><button type="button" class="input-actions__btn input-actions__clear" aria-label="Clear"><span class="input-icon input-icon--fill" aria-hidden="true">cancel</span></button></div>' +
        '</div></div></div>' +
        '<button type="button" class="btn btn--blank btn--md btn--icon dn-search__close" aria-label="Close search"><span class="btn__icon" aria-hidden="true">close</span></button>' +
      '</div>' +
      '<div class="dn-search__body" id="dn-results" role="listbox" aria-label="Results"></div>' +
      '<p class="dn-search__live" aria-live="polite"></p>' +
    '</div>';
  wrap.appendChild(sm);
  var sInput = sm.querySelector('input'), sBody = sm.querySelector('.dn-search__body'), sLive = sm.querySelector('.dn-search__live'), sClose = sm.querySelector('.dn-search__close'), sClear = sm.querySelector('.input-actions__clear');
  var sFrom = null, sActive = -1, sOpts = [];

  function regexEsc(x) { return x.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); }
  function mark(text, tokens) {
    if (!tokens.length) return esc(text);
    var re = new RegExp(tokens.map(regexEsc).join('|'), 'gi'), out = '', last = 0, m;
    while ((m = re.exec(text))) { if (!m[0]) break; out += esc(text.slice(last, m.index)) + '<b>' + esc(m[0]) + '</b>'; last = m.index + m[0].length; }
    return out + esc(text.slice(last));
  }
  function score(e, tokens) {   // lower = better: title 0-2, Swedish word start 3, group 4, Swedish contains 5
    var t = e.t.toLowerCase(), g = e.group.toLowerCase(), sum = 0;
    for (var i = 0; i < tokens.length; i++) {
      var k = tokens[i], kf = fold(k), at = t.indexOf(k);
      if (at === 0) sum += 0;
      else if (at > 0 && /[\s\-]/.test(t.charAt(at - 1))) sum += 1;
      else if (at > 0) sum += 2;
      else if (new RegExp('(^|[\\s,])' + regexEsc(kf)).test(e.sv)) sum += 3;
      else if (g.indexOf(k) > -1) sum += 4;
      else if (e.sv.indexOf(kf) > -1) sum += 5;
      else return -1;
    }
    return sum;
  }
  function svWord(e, tokens) {   // the Swedish word that made this page match (only when the English title does not), else ''
    var t = e.t.toLowerCase();
    for (var i = 0; i < tokens.length; i++) {
      if (t.indexOf(tokens[i]) > -1) continue;
      var kf = fold(tokens[i]), best = '';
      for (var j = 0; j < e.svl.length; j++) {
        var w = fold(e.svl[j]);
        if (w.indexOf(kf) === 0) return e.svl[j].charAt(0).toUpperCase() + e.svl[j].slice(1);
        if (!best && w.indexOf(kf) > -1) best = e.svl[j];
      }
      if (best) return best.charAt(0).toUpperCase() + best.slice(1);
    }
    return '';
  }
  function setActive(n) {
    sActive = n;
    sOpts.forEach(function (o, i) { o.setAttribute('aria-selected', i === n ? 'true' : 'false'); });
    if (sOpts[n]) { sInput.setAttribute('aria-activedescendant', sOpts[n].id); sOpts[n].scrollIntoView({ block: 'nearest' }); } else sInput.removeAttribute('aria-activedescendant');
  }
  function render() {
    var q = sInput.value.trim(), tokens = q.toLowerCase().split(/\s+/).filter(Boolean);
    sm.classList.toggle('has-value', !!q);
    if (!tokens.length) { sBody.innerHTML = '<p class="dn-search__msg">Search for a component or a foundation.</p>'; sOpts = []; sLive.textContent = ''; setActive(-1); return; }
    var hits = [];
    entries.forEach(function (e, i) { var sc = score(e, tokens); if (sc > -1) hits.push({ e: e, sc: sc, i: i }); });
    hits.sort(function (a, b) { return a.sc - b.sc || a.i - b.i; });
    var html = '', n = 0;
    ['Components', 'Foundations', 'Tokens'].forEach(function (cat) {
      var list = hits.filter(function (h) { return h.e.cat === cat; });
      if (!list.length) return;
      html += '<div class="dn-search__group" role="presentation">' + cat + '</div>';
      list.forEach(function (h) {
        html += '<a class="dn-search__opt" role="option" id="dn-opt-' + n++ + '" aria-selected="false" href="' + h.e.href + '"><span class="dn-search__t">' + mark(h.e.t, tokens) + (svWord(h.e, tokens) ? ' <span class="dn-search__sv">(' + mark(svWord(h.e, tokens), tokens.map(fold)) + ')</span>' : '') + '</span>' + (h.e.group ? '<span class="dn-search__g">' + esc(h.e.group) + '</span>' : '') + '</a>';
      });
    });
    sBody.innerHTML = html || '<p class="dn-search__msg">No results for “' + esc(q) + '”.</p>';
    sOpts = [].slice.call(sBody.querySelectorAll('.dn-search__opt'));
    sLive.textContent = sOpts.length ? sOpts.length + ' results' : 'No results';
    setActive(sOpts.length ? 0 : -1);
  }
  function openSearch(from) {
    sFrom = from || document.activeElement;
    closeDrawer();
    sm.hidden = false;
    void sm.offsetWidth;   // let the fade start from 0
    sm.classList.add('is-open'); root.classList.add('dn-modal-open');
    sInput.value = ''; render(); sInput.focus();
  }
  function closeSearch() {
    if (sm.hidden) return;
    sm.classList.remove('is-open'); root.classList.remove('dn-modal-open');
    setTimeout(function () { if (!sm.classList.contains('is-open')) sm.hidden = true; }, ms('--duration-medium-2', 300));
    if (sFrom && sFrom.focus) sFrom.focus();
  }
  wrap.addEventListener('click', function (e) { if (e.target.closest('[data-search]')) openSearch(e.target.closest('[data-search]')); });
  sm.querySelector('.dn-search__scrim').addEventListener('click', closeSearch);
  sClose.addEventListener('click', closeSearch);
  sClear.addEventListener('click', function () { sInput.value = ''; render(); sInput.focus(); });
  sInput.addEventListener('input', render);
  sBody.addEventListener('mousemove', function (e) { var o = e.target.closest('.dn-search__opt'); if (o) { var i = sOpts.indexOf(o); if (i !== sActive) setActive(i); } });
  sBody.addEventListener('click', function (e) { if (e.target.closest('a')) closeSearch(); });
  sm.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') { e.preventDefault(); closeSearch(); return; }
    if (e.key === 'ArrowDown' || e.key === 'ArrowUp') {
      if (!sOpts.length) return;
      e.preventDefault(); setActive((sActive + (e.key === 'ArrowDown' ? 1 : -1) + sOpts.length) % sOpts.length);
    } else if (e.key === 'Enter' && sOpts[sActive] && e.target === sInput) {
      e.preventDefault(); location.href = sOpts[sActive].href;
    } else if (e.key === 'Tab') {   // keep Tab inside the dialog: input → clear (when shown) → close
      var f = [sInput, sClear, sClose].filter(function (x) { return x.offsetParent !== null; });
      var at = f.indexOf(document.activeElement);
      if (e.shiftKey && at <= 0) { e.preventDefault(); f[f.length - 1].focus(); }
      else if (!e.shiftKey && at === f.length - 1) { e.preventDefault(); f[0].focus(); }
    }
  });
  document.addEventListener('keydown', function (e) {
    if ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === 'k') { e.preventDefault(); if (sm.hidden) openSearch(document.activeElement); else closeSearch(); }
  });
  document.addEventListener('keydown', function (e) { if (e.key === 'Tab') { root.setAttribute('data-kbd', ''); document.body.classList.add('keyboard-nav'); } }, true);   // focus ring for the shared components (same as subnav.js)
  document.addEventListener('pointerdown', function () { root.removeAttribute('data-kbd'); document.body.classList.remove('keyboard-nav'); }, true);
})();

/* Footer for every doc page that has the navigation: three columns (How you can help, Resources, Support) and the credit line.
   Built here so the text lives in one place; styles are .ds-footer in docs.css. Skipped when a page already has a .ds-footer. */
(function () {
  var SLACK = 'https://alligo-it.slack.com/archives/C07QRNLU1L1';
  var STORYBOOK = 'https://www.chromatic.com/build?appId=67b6063b450f52d85d87d37f&number=106';   // Storybook build on Chromatic (a build number: update it when the link should point to a newer build)
  var FIGMA = 'https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?m=auto&t=AwSiA8PReQo5qH9J-6';   // the ECO Design System file
  function build() {
    if (document.querySelector('.ds-footer')) return;
    var f = document.createElement('footer');
    f.className = 'ds-footer';
    f.innerHTML =
      '<div class="ds-footer__grid">' +
        '<div class="ds-footer__col ds-footer__col--help"><h2 class="ds-footer__title">How you can help</h2>' +
          '<p>The ECO Design System has just started its journey. Your feedback and contributions help us refine the design system and make it better for everyone. If you got a question or if there are something you feel is missing or if you notice something out of the ordinary. Please connect with ECO team through our <a class="inline-link inline-link--medium inline-link--secondary" href="' + SLACK + '" target="_blank" rel="noopener">Slack channel</a>.</p>' +
          '<p class="ds-footer__made">Made with <span class="mo-ic" aria-label="love">favorite</span> by Alligo E-com © ' + new Date().getFullYear() + '</p></div>' +
        '<div class="ds-footer__col"><h2 class="ds-footer__title">Resources</h2><ul class="ds-footer__list">' +
          '<li><a class="inline-link inline-link--medium inline-link--secondary" href="' + STORYBOOK + '" target="_blank" rel="noopener">Storybook</a></li>' +
          '<li><a class="inline-link inline-link--medium inline-link--secondary" href="' + FIGMA + '" target="_blank" rel="noopener">Figma</a></li>' + '</ul></div>' +
        '<div class="ds-footer__col"><h2 class="ds-footer__title">Support</h2><ul class="ds-footer__list">' +
          '<li><a class="inline-link inline-link--medium inline-link--secondary" href="' + SLACK + '" target="_blank" rel="noopener">ECO Slack Channel</a></li>' + '</ul></div>' +
      '</div>';
    (window.matchMedia('(min-width: 961px)').matches ? document.documentElement : document.body).appendChild(f);   // desktop: the footer sits outside the white panel, on the grey surround
  }
  /* Back to top: one icon button, fixed bottom right, shown once the page has been scrolled (a long page). Smooth scroll (instant under reduced
     motion), then focus moves to the page title so keyboard users start at the top. Its tooltip uses the shared tooltip.js. */
  function top() {
    if (document.getElementById('ds-top')) return;
    var b = document.createElement('button');
    b.type = 'button'; b.id = 'ds-top'; b.className = 'btn btn--secondary btn--md btn--icon ds-top';
    b.setAttribute('aria-label', 'Back to top'); b.setAttribute('data-tooltip', 'Back to top');
    b.innerHTML = '<span class="btn__icon" aria-hidden="true">arrow_upward</span>';
    document.body.appendChild(b);
    function show() { b.classList.toggle('is-visible', window.pageYOffset > window.innerHeight * 0.75); }
    window.addEventListener('scroll', show, { passive: true }); window.addEventListener('resize', show); show();
    b.addEventListener('click', function () {
      var still = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      window.scrollTo({ top: 0, left: 0, behavior: still ? 'auto' : 'smooth' });
      var h = document.querySelector('h1');
      if (h) { h.setAttribute('tabindex', '-1'); h.focus({ preventScroll: true }); }
    });
    if (!document.querySelector('script[src*="tooltip.js"]')) { var t = document.createElement('script'); t.src = '/components/js/tooltip.js'; document.body.appendChild(t); }
  }
  function init() { build(); top(); }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();

/* Framed pages (html.ds-frame): the overlay panel's right edge is a line that starts under the content panel's corner at the top of the page
   (gap + radius) and runs up to the window edge once the page is scrolled. --dn-line is where that line starts, in px from the top of the window. */
(function () {
  var root = document.documentElement;
  if (!root.classList.contains('ds-frame')) return;
  function set() { var r = parseFloat(getComputedStyle(root).getPropertyValue('--dn-radius')) || 0; root.style.setProperty('--dn-line', Math.max(0, 16 + r - window.pageYOffset) + 'px'); }   // 16px gap + the corner radius
  window.addEventListener('scroll', set, { passive: true }); set();
})();

/* Mobile header (below 961px): it scrolls away with the page and comes back as the user scrolls back up, the same distance as it left.
   --dn-hide = how many px of the header are hidden (0 to its height). Paused while the drawer is open (the page is locked then). */
(function () {
  var root = document.documentElement, mq = window.matchMedia('(max-width: 960px)'), last = window.pageYOffset, hide = 0, tick = false;
  function bar() { return parseFloat(getComputedStyle(root).getPropertyValue('--dn-bar')) || 64; }
  function apply() {
    tick = false;
    var y = Math.max(0, window.pageYOffset), h = bar();
    if (!mq.matches || root.classList.contains('dn-lock')) { hide = 0; } else { hide = Math.min(h, Math.max(0, hide + y - last)); }
    last = y;
    root.style.setProperty('--dn-hide', hide + 'px');
  }
  window.addEventListener('scroll', function () { if (!tick) { tick = true; requestAnimationFrame(apply); } }, { passive: true });
  window.addEventListener('resize', apply);
})();
