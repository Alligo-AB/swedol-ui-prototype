/* ECO doc pages: builds the on-page navigation from the headings of a page with a .ds-doc wrapper.
   Level 1 = each section (its .ds-h2), level 2 = each .ds-h3.ds-group heading inside it (given an id if it has none).
   Plain .ds-h3 headings are not listed.
   - from 1024px: a sticky "Contents" list in the right margin (.ds-sidetoc), the item in view is marked (aria-current)
   - below 1024px: the chip row (.ds-subnav, sections only), which subnav.js makes sticky and scrolls.
     <div class="ds-doc" data-subnav="tabs"> renders it as a secondary tab bar (eco-tabs) instead of chips
   Load it before subnav.js (which handles the chip row and the smooth jump for both lists). */
(function () {
  var doc = document.querySelector('.ds-doc');
  if (!doc) return;
  var base = document.currentScript ? document.currentScript.src.replace(/toc\.js.*$/, '') : '';   // eco-design-system/, for the lazy notifications files

  function slug(s) { return s.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, ''); }
  var items = [];
  doc.querySelectorAll('section.ds-section[id]').forEach(function (sec) {
    var h = sec.querySelector('.ds-h2');
    if (!h) return;
    items.push({ id: sec.id, text: h.textContent, level: 1, el: h });
    sec.querySelectorAll('.ds-h3.ds-group').forEach(function (g) {
      if (!g.id) g.id = sec.id + '-' + slug(g.textContent);
      items.push({ id: g.id, text: g.textContent, level: 2, el: g });
    });
  });
  if (!items.length) return;
  function esc(s) { return s.replace(/&/g, '&amp;').replace(/</g, '&lt;'); }

  // chips (below 1024px): sections only
  var chips = document.createElement('nav');
  chips.className = 'ds-subnav ds-subnav--auto';
  chips.setAttribute('aria-label', 'On this page');
  var asTabs = doc.getAttribute('data-subnav') === 'tabs';   // opt-in: secondary tab bar (eco-tabs) instead of chips
  var secs = items.filter(function (i) { return i.level === 1; });
  if (asTabs) {
    chips.classList.add('ds-subnav--tabs');
    chips.innerHTML = '<div class="tab-bar tab-bar--secondary tab-bar--md" data-tabs-id="onpage">' + secs.map(function (i) {
      return '<a class="tab" href="#' + i.id + '"><span class="tab__label">' + esc(i.text) + '</span></a>';
    }).join('') + '</div>';
  } else {
    chips.innerHTML = '<ul class="ds-toc">' + secs.map(function (i) {
      return '<li><a href="#' + i.id + '">' + esc(i.text) + '</a></li>';
    }).join('') + '</ul>';
  }
  doc.parentNode.insertBefore(chips, doc);

  // side list (from 1024px)
  var side = document.createElement('nav');
  side.className = 'ds-sidetoc';
  side.setAttribute('aria-label', 'Contents');
  side.innerHTML = '<div class="ds-sidetoc__in"><p class="ds-sidetoc__title">Contents</p><ul class="ds-sidetoc__list">' + items.map(function (i) {
    return '<li class="ds-sidetoc__item ds-sidetoc__item--' + i.level + '"><a href="#' + i.id + '">' + esc(i.text) + '</a></li>';
  }).join('') + '</ul></div>';
  doc.insertBefore(side, doc.firstChild);

  // heading anchors: a link icon on every Contents heading copies the URL of that heading and shows a success toast.
  // The toast is the ECO system toast (notifications.js / notifications.css), loaded on the first click. The stylesheet goes BEFORE docs.css,
  // so docs.css and the component files win (notifications.css has its own .btn base).
  function withToast(fn) {
    if (window.ECO_N) return fn();
    var docs = document.querySelector('link[href$="docs.css"]'), css = document.createElement('link');
    css.rel = 'stylesheet'; css.href = base + 'notifications.css?v=16'; docs ? docs.parentNode.insertBefore(css, docs) : document.head.appendChild(css);
    var js = document.createElement('script'); js.src = base + 'notifications.js'; js.onload = fn; document.body.appendChild(js);
  }
  function copyFallback(t) {
    var ta = document.createElement('textarea'), ok = false; ta.value = t; ta.setAttribute('readonly', ''); ta.style.cssText = 'position:fixed;opacity:0';
    document.body.appendChild(ta); ta.select(); try { ok = document.execCommand('copy'); } catch (e) {} ta.remove(); return ok;
  }
  function copyText(t) {   // resolves true when copied, false when the browser refused
    if (navigator.clipboard && window.isSecureContext) return navigator.clipboard.writeText(t).then(function () { return true; }, function () { return copyFallback(t); });
    return Promise.resolve(copyFallback(t));
  }
  items.forEach(function (it) {
    var b = document.createElement('button');
    b.type = 'button'; b.className = 'icon-btn ds-anchor'; b.setAttribute('aria-label', 'Copy link to ' + it.text); b.setAttribute('data-tooltip', 'Copy link to heading');
    b.innerHTML = '<span class="btn__icon" aria-hidden="true">link</span>';
    b.addEventListener('click', function () {
      var url = location.origin + location.pathname + location.search + '#' + it.id;
      history.replaceState(null, '', '#' + it.id);
      copyText(url).then(function (ok) { withToast(function () { ECO_N.showToast(ok ? { status: 'success', emphasis: 'weak', text: 'URL to heading copied', autoHide: 4000 } : { status: 'error', emphasis: 'weak', text: 'Could not copy the URL. Copy it from the address bar.', autoHide: 6000 }); }); });
    });
    it.el.appendChild(b);
  });

  // scrollspy: the last heading that has passed the top third of the window
  var links = [].slice.call(side.querySelectorAll('a'));
  function spy() {
    var at = window.innerHeight * 0.33, cur = 0;
    items.forEach(function (it, n) { if (it.el.getBoundingClientRect().top <= at) cur = n; });
    if (window.innerHeight + window.pageYOffset >= document.documentElement.scrollHeight - 2) cur = items.length - 1;
    links.forEach(function (a, n) { if (n === cur) a.setAttribute('aria-current', 'true'); else a.removeAttribute('aria-current'); });
    var on = links[cur], box = side.querySelector('.ds-sidetoc__in');
    if (on && box.scrollHeight > box.clientHeight) { // keep the marked item visible when the list itself scrolls
      var top = on.offsetTop, bot = top + on.offsetHeight;   // the box is the offset parent (it is sticky)
      if (top < box.scrollTop) box.scrollTop = top; else if (bot > box.scrollTop + box.clientHeight) box.scrollTop = bot - box.clientHeight;
    }
  }
  window.addEventListener('scroll', spy, { passive: true });
  window.addEventListener('resize', spy);
  spy();
})();

/* A link with a #hash (a copied heading URL, a cross link between the pages of a set): the page content is built by scripts after load, so the browser's own jump lands too early.
   Jump again when everything is built, and once more after the fonts and the images have loaded and the layout has settled. */
(function () {
  var id = decodeURIComponent(location.hash.slice(1));
  if (!id) return;
  var touched = false;   // the reader scrolled: stop correcting
  ['wheel', 'touchstart', 'keydown', 'mousedown'].forEach(function (ev) { window.addEventListener(ev, function () { touched = true; }, { passive: true, once: true }); });
  function go() { if (touched) return; var t = document.getElementById(id); if (t) t.scrollIntoView({ block: 'start', behavior: 'instant' }); }
  go();
  window.addEventListener('load', function () { go(); setTimeout(go, 400); });   // the late font swap can still move the page after the load event
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { go(); setTimeout(go, 400); });
})();
