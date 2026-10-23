"""Layout: the second Foundation in the three-page structure (2026-10-22), after Colors.
Grid (layout.html) / Breakpoints (layout-breakpoints.html) / Spacing (layout-spacing.html) / Tokens (layout-tokens.html).
Uses the custom page set of build.py (pages=[...]) like gen_colors.py. Structure and text from the Supernova pages (Grid, Breakpoints, Spacing, Token),
Figma frames 3991:161037 (Breakpoint Values) and 3991:163229 (Responsive Layout); the design is ECO's. The Spacing tab is the old foundations/spacing.html (kept in old-source/spacing.html).
Shared script: ../layout-kit.js (breakpoint list, scaled grid figure, package reader)."""
import os
from html import escape
from build import *

HERE_ = os.path.dirname(os.path.abspath(__file__))
OUT_F = os.path.normpath(os.path.join(HERE_, '..', 'foundations'))
SLUG = 'layout'
FIGMA = 'https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=3991-163229'


def sec(href, text):
    return '<a class="inline-link inline-link--large inline-link--secondary" href="%s">%s</a>' % (href, text)


def code_static(id_, title, text):
    return '<div class="ds-code"><div class="ds-code__bar"><span>%s</span><button type="button" class="mo-copy" data-copy="%s" aria-label="Copy"><span class="mo-ic" aria-hidden="true">content_copy</span></button></div><pre id="%s">%s</pre></div>' % (title, id_, id_, escape(text, quote=False))


def lv(bp, what):   # a value read live from the package: filled by the page script
    return '<span data-lv="%s:%s">…</span>' % (bp, what)


# =============================================================== Grid
g_overview = '<h2 class="ds-h2">Overview</h2>' + \
    desc('To keep pages responsive and flexible in different browser widths and on different devices, every ECO layout is built on a grid. The grid has <strong>margins</strong>, <strong>gutters</strong> and <strong>columns</strong>, some with a fixed width and some with a fluid one.') + \
    '<h3 class="ds-h3 ds-group">Margins</h3>' + \
    desc('Margins have a fixed width. They are the empty space on the left and right side of the window, and they keep text and other content from running to the edge of the display. The margin grows with the window: it is smallest on a phone and largest on a desktop.') + \
    '<h3 class="ds-h3 ds-group">Gutters</h3>' + \
    desc('Gutters have a fixed width. They are the empty space between the columns, and they keep the content of one column apart from the next.') + \
    '<h3 class="ds-h3 ds-group">Columns</h3>' + \
    desc('Columns are fluid. They share the width that is left after the margins and gutters, which is what makes the layout responsive. The <em>number</em> of columns is fixed per breakpoint: 4, 8 or 12.') + \
    desc('The fixed values are not new numbers: margins and gutters are steps of the ' + sec('layout-spacing.html', 'spacing scale') + ', and the ' + sec('layout-breakpoints.html', 'breakpoints') + ' decide which set applies. All values are listed on the ' + sec('layout-tokens.html', 'Tokens') + ' tab.') + \
    desc('This documentation has four tabs. <strong>Grid</strong> (this page) explains the grid. ' + sec('layout-breakpoints.html', 'Breakpoints') + ' lists the five ranges and how to write them. ' + sec('layout-spacing.html', 'Spacing') + ' has the spacing scale. ' + sec('layout-tokens.html', 'Tokens') + ' lists every layout token from the package.')

g_anatomy = '<h2 class="ds-h2">Anatomy</h2>' + \
    desc('The grid of the Desktop breakpoint, drawn to scale from the tokens. The grey areas are margins, the blue areas are columns and the white between the columns is the gutter.') + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout" id="an-stage"><div class="ds-callout__art" id="an-art"></div></div></figure></div>' + \
    ol_parts([('Margin', 'The fixed space at the left and right edge of the window. It also frames the content area.'),
              ('Gutter', 'The fixed space between two columns.'),
              ('Column', 'A fluid track. Content is placed on one column or spans several.')])

g_bps = '<h2 class="ds-h2">Grid by breakpoint</h2>' + \
    desc('The grid changes at five breakpoints. Each figure below is the grid at one window width, drawn from the tokens at that breakpoint. The window of a phone has 4 columns, a tablet 8 and a desktop 12.') + \
    ''.join(
        '<h3 class="ds-h3">%s</h3>' % h + desc(d) + '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage"><div id="fig-%s"></div></div><figcaption class="ds-fig__cap" id="cap-%s"></figcaption></figure></div>' % (i, i) + \
        '<ul class="ds-bullets"><li><strong>Margin:</strong> %s <code>%s</code></li><li><strong>Gutter:</strong> %s <code>%s</code></li><li><strong>Column:</strong> %s, fluid width</li></ul>' % (lv(i, 'margin'), mt, lv(i, 'gutter'), gt, lv(i, 'cols') + ' columns')
        for i, h, d, mt, gt in [
            ('xs', 'XSmall: 0px to 639px', 'Below 640px the grid is a <strong>4-column</strong> grid (<code>bp-xs</code>). The smallest supported window is 375px. It uses the Mobile base styling.', 'site-margin-xs', 'gutter-xs'),
            ('sm', 'Small: 640px to 768px', 'From 640px to 768px the grid is an <strong>8-column</strong> grid (<code>bp-sm</code>). A tablet still uses the Mobile base styling.', 'site-margin-sm', 'gutter-sm'),
            ('md', 'Medium: 769px to 1023px', 'From 769px to 1023px the grid is a <strong>12-column</strong> grid (<code>bp-md</code>). This is the first breakpoint with the Desktop base styling.', 'site-margin-md', 'gutter-md'),
            ('lg', 'Large: 1024px to 1280px', 'From 1024px to 1280px the grid is a <strong>12-column</strong> grid (<code>bp-lg</code>), the same as Medium but with a wider margin.', 'site-margin-lg', 'gutter-lg'),
            ('xl', 'XLarge: 1281px and up', 'From 1281px the grid has the same settings as Large (<code>bp-xl</code>). The margin is <strong>infinite</strong>: the content area stops growing at 1200px and is centered, so the space on both sides takes up the rest. The figure shows the largest prototype width, 1440px.', 'site-margin-xl at 1440px', 'gutter-lg')])

g_play = '<h2 class="ds-h2">Try the grid</h2>' + \
    desc('Pick a window width and a layout to see how content lands on the columns, and the classes that produce it.') + \
    '<div class="ds-playground"><div class="ds-stage" id="pg-stage"><div id="pg-host"></div><p class="lg-read" id="pg-read" aria-live="polite"></p></div><div class="ds-controls">' + \
    sel('pg-l-w', 'sel-pg-w', 'Window width', 'w', [('lg', 'Large')], 'lg') + \
    btn_group('pg-l-lay', 'Layout', 'data-pg="lay"', [('full', 'Full', True), ('half', 'Halves', False), ('quarter', 'Quarters', False)]) + \
    '</div></div>' + \
    '<h3 class="ds-h3">Classes for this layout</h3>' + code_box('pg-code', 'Tailwind: item classes', 'pg-code')

g_code = '<h2 class="ds-h2">Build with the grid</h2>' + \
    desc('Write the frame mobile-first with Tailwind (the stack of this project): the margin as padding on the section, and the columns and gutters on a grid inside it. The numbers are the tokens of the breakpoint, see ' + sec('layout-tokens.html', 'Tokens') + '.') + \
    '<div id="code-tw-host"></div>' + \
    desc('Without Tailwind, use the same tokens in CSS. Write the token with its pixel fallback.') + \
    '<div id="code-css-host"></div>' + \
    '<p class="ds-desc ds-note">Never write a column width. Columns are fluid: a block spans a number of columns and the grid decides the width.</p>'

g_usage = '<h2 class="ds-h2">Usage</h2>' + \
    rules(['Build every page on the grid: margin on the section, columns and gutters inside it.',
           'Place content on whole columns. A block spans one or more columns.',
           'Write mobile-first and add <code>sm:</code>, <code>md:</code>, <code>lg:</code> and <code>xl:</code>.',
           'Use the margin and gutter tokens of the breakpoint, not a number that looks right.'],
          ['Set a fixed width on a column.',
           'Let content run into the margin, or add your own side padding on top of it.',
           'Use another number of columns than the breakpoint has (for example 12 on a phone).',
           'Make the content area wider than 1200px on large windows.'])

g_refs = '<h2 class="ds-h2">References</h2>' + refs([
    ('https://m3.material.io/foundations/layout/understanding-layout/overview', 'Material Design 3: Understanding layout', 'Google.'),
    ('https://carbondesignsystem.com/elements/2x-grid/overview/', 'Carbon Design System: 2x Grid', 'IBM.'),
    ('https://www.w3.org/WAI/WCAG22/Understanding/reflow.html', 'WCAG 2.2: Reflow', 'Success criterion 1.4.10: content reflows at a 320px window without scrolling in two directions.')])

grid_secs = [('overview', g_overview), ('anatomy', g_anatomy), ('grid-by-breakpoint', g_bps), ('try-the-grid', g_play), ('build-with-the-grid', g_code), ('usage', g_usage), ('references', g_refs)]

JS_GRID = r'''
  var L = LAYOUT, BPS = L.BPS, byId = {};
  BPS.forEach(function (b) { byId[b.id] = b; });

  function fillValues() {   // every [data-lv="xs:margin"] shows the value read from the package
    $$('[data-lv]').forEach(function (n) {
      var p = n.dataset.lv.split(':'), v = L.vals(byId[p[0]]);
      n.textContent = p[1] === 'cols' ? v.cols : L.px(v[p[1]]);
    });
  }
  function figures() {
    BPS.forEach(function (bp) {
      var host = $('#fig-' + bp.id), v = L.vals(bp); clear(host); host.appendChild(L.gridFig(bp));
      var cap = $('#cap-' + bp.id);
      cap.textContent = bp.exampleLabel + (bp.infinite ? '. Margin ' + L.px(v.margin) + ' at this width, content area ' + L.CONTENT_MAX + 'px.' : '.');
    });
  }

  /* Anatomy: the Large grid with three markers on the real parts */
  function anatomy() {
    var host = $('#an-art'), f = L.gridFig(byId.lg);
    host.appendChild(f); L.fit(host);
    DK.callouts($('#an-stage'), [
      { n: 1, el: f._parts.margin, side: 'left', at: 'center', len: 56 },
      { n: 2, side: 'bottom', len: 48, box: function () { var a = f._parts.cols.children[0].getBoundingClientRect(), b = f._parts.cols.children[1].getBoundingClientRect(); return { left: a.right, top: a.top, width: b.left - a.right, height: a.height }; } },
      { n: 3, el: f._parts.cols.children[5], side: 'top', len: 48 }
    ]);
  }

  /* Playground */
  var state = { w: 'lg', lay: 'full' }, ITEMS = { full: [1], half: [0.5, 0.5], quarter: [0.25, 0.25, 0.25, 0.25] };
  function spanFor(bp, f) { return Math.max(1, Math.round(f * L.vals(bp).cols)); }
  function play() {
    var bp = byId[state.w], v = L.vals(bp), host = $('#pg-host');
    clear(host); var h = Math.max(160, Math.round(bp.example * 0.3));
    host.appendChild(L.gridFig(bp, { h: h, itemH: Math.round(h * 0.3), items: ITEMS[state.lay] })); L.fit(host);
    $('#pg-read').textContent = bp.name + ' (' + bp.token + ') · window ' + bp.example + 'px · ' + v.cols + ' columns · gutter ' + L.px(v.gutter) + ' · margin ' + L.px(v.margin) + (bp.infinite ? ' (infinite, shown at 1440px)' : '') + '.';
    var f = ITEMS[state.lay][0], a = spanFor(byId.xs, f), b = spanFor(byId.sm, f), c = spanFor(byId.md, f);
    $('#pg-code').textContent = '<div class="col-span-' + a + ' sm:col-span-' + b + ' md:col-span-' + c + '">…</div>\n\n/* ' + ITEMS[state.lay].length + ' item' + (ITEMS[state.lay].length > 1 ? 's' : '') + ' per row: ' + a + ' of ' + L.vals(byId.xs).cols + ' columns on XSmall, ' + b + ' of ' + L.vals(byId.sm).cols + ' on Small, ' + c + ' of ' + L.vals(byId.md).cols + ' from Medium. */';
  }
  function fillSelect() {
    var s = $('#sel-pg-w'); clear(s);
    BPS.forEach(function (bp) { var o = document.createElement('option'); o.value = bp.id; o.textContent = bp.name + ' · ' + bp.example + 'px'; if (bp.id === state.w) o.selected = true; s.appendChild(o); });
  }

  /* Code: Tailwind and CSS from the package values */
  function codes() {
    var x = L.vals(byId.xs), s = L.vals(byId.sm), m = L.vals(byId.md), l = L.vals(byId.lg), P = L.px;
    var tw = '<section class="mx-auto max-w-[1280px] px-[' + P(x.margin) + '] sm:px-[' + P(s.margin) + '] lg:px-[' + P(l.margin) + ']">\n' +
      '  <div class="grid grid-cols-' + x.cols + ' sm:grid-cols-' + s.cols + ' md:grid-cols-' + m.cols + ' gap-[' + P(x.gutter) + '] sm:gap-[' + P(s.gutter) + '] md:gap-[' + P(m.gutter) + ']">\n' +
      '    <div class="col-span-' + x.cols + ' sm:col-span-' + s.cols + ' md:col-span-' + m.cols + '">Full width</div>\n  </div>\n</section>';
    var css = '.page {\n  max-width: 1280px; margin-inline: auto;\n  padding-inline: var(--dimension-margin-site-margin-xs, ' + P(x.margin) + ');\n}\n.page__grid {\n  display: grid;\n  grid-template-columns: repeat(' + x.cols + ', minmax(0, 1fr));\n  column-gap: var(--dimension-gutter-xs, ' + P(x.gutter) + ');\n}\n' +
      '@media (min-width: 640px) {   /* sm */\n  .page { padding-inline: var(--dimension-margin-site-margin-sm, ' + P(s.margin) + '); }\n  .page__grid { grid-template-columns: repeat(' + s.cols + ', minmax(0, 1fr)); column-gap: var(--dimension-gutter-sm, ' + P(s.gutter) + '); }\n}\n' +
      '@media (min-width: 769px) {   /* md */\n  .page__grid { grid-template-columns: repeat(' + m.cols + ', minmax(0, 1fr)); column-gap: var(--dimension-gutter-md, ' + P(m.gutter) + '); }\n}\n' +
      '@media (min-width: 1024px) {  /* lg, and xl: the same, the page is centered */\n  .page { padding-inline: var(--dimension-margin-site-margin-lg, ' + P(l.margin) + '); }\n  .page__grid { column-gap: var(--dimension-gutter-lg, ' + P(l.gutter) + '); }\n}';
    var a = $('#code-tw-host'), b = $('#code-css-host'); clear(a); clear(b);
    [[a, 'Tailwind: section and grid', tw, 'code-tw'], [b, 'CSS with tokens', css, 'code-css']].forEach(function (c) {
      var box = document.createElement('div'); box.className = 'ds-code';
      box.innerHTML = '<div class="ds-code__bar"><span>' + c[1] + '</span><button type="button" class="mo-copy" data-copy="' + c[3] + '" aria-label="Copy"><span class="mo-ic" aria-hidden="true">content_copy</span></button></div><pre id="' + c[3] + '"></pre>';
      c[0].appendChild(box); $('#' + c[3]).textContent = c[2];
    });
  }

  function init() { fillValues(); figures(); anatomy(); fillSelect(); DK.wire(state, play); play(); codes(); L.fit(); }
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(init); else init();
'''

# =============================================================== Breakpoints
b_overview = '<h2 class="ds-h2">Overview</h2>' + \
    desc('In responsive design a breakpoint is the window width at which the layout and the content adapt, so that the experience stays good on every screen size.') + \
    desc('The responsive grid changes the margins, the width of the content and the number of columns at each breakpoint, and the components change size with it. ECO has <strong>five</strong> breakpoints, and they are the same for every page and every component.') + \
    desc('Breakpoints work together with the ' + sec('layout.html', 'grid') + ', and the values of each one are listed on the ' + sec('layout-tokens.html', 'Tokens') + ' tab.')

b_here = '<h2 class="ds-h2">Where your window is</h2>' + \
    desc('The breakpoint of the window you are reading this in. Resize the window and it follows.') + \
    '<div class="ds-stage"><div class="lg-ruler" id="ruler" role="list"></div><p class="lg-read" id="here" aria-live="polite"></p></div>'

b_table = '<h2 class="ds-h2">Breakpoints</h2>' + \
    desc('ECO uses five breakpoints. The grid values are read from the token package.') + \
    '<div class="ds-table-wrap"><table class="ds-table" id="bp-table"><thead><tr><th scope="col">Breakpoint</th><th scope="col">Token</th><th scope="col">Range</th><th scope="col">Margin</th><th scope="col">Gutter</th><th scope="col">Columns</th><th scope="col">Base styling</th></tr></thead><tbody></tbody></table></div>' + \
    '<p class="ds-desc ds-note"><strong>Mobile base styling</strong> is used by XSmall and Small. <strong>Desktop base styling</strong> is used by Medium, Large and XLarge. On XLarge the margin is infinite: the content area is centered and stops at 1200px.</p>' + \
    '<h3 class="ds-h3 ds-group">Small is mobile</h3>' + \
    desc('The Desktop base styling starts at <strong>769px</strong>, not at 768px and not at 640px. A tablet (Small, 640px to 768px) has more columns and a wider margin than a phone, but its type and components are the Mobile ones. Never write the desktop style at <code>sm</code>.') + \
    '<h3 class="ds-h3 ds-group">Components can have more</h3>' + \
    desc('A component can change at other widths than these five. For example a ' + sec('../components/section-specifications.html#sizes', 'section') + ' changes its padding at 640, 769, 1024 and 1281px. Such breakpoints are specified with the component.')

b_base = '<h2 class="ds-h2">What changes at Desktop</h2>' + \
    desc('The breakpoint where the base styling switches is Medium, 769px. These are the main things that change there.') + \
    table(['What', 'Mobile base styling (XSmall, Small)', 'Desktop base styling (Medium and up)'], [
        ['Type styles', 'Mobile size of each style, for example body-md 16/22 and body-lg 18/24. See ' + sec('typography.html', 'Typography') + '.', 'Desktop size, for example body-md 17/24 and body-lg 20/28.'],
        ['Components', 'Mobile size of buttons, fields and other controls.', 'Desktop size. Each component page has a Breakpoint control and lists both values.'],
        ['Layout spacing', '<code>space-md</code> 24px, <code>space-lg</code> 32px, then steps up at 640px.', 'Steps up at 769px and 1024px, see ' + sec('layout-spacing.html#layout', 'Layout spacing') + '.'],
        ['Grid', '4 columns (XSmall) or 8 (Small), margin 16px or 32px.', '12 columns, margin 32px (Medium) or 40px (Large and up).']])

b_use = '<h2 class="ds-h2">Usage</h2>' + \
    desc('Write mobile first: the style with no prefix is the phone, and each larger breakpoint adds to it with a <code>min-width</code> query. The queries use the start of each range.') + \
    '<div id="code-mq-host"></div>' + \
    desc('In Tailwind the same five breakpoints are the screens of the config. <code>xs</code> is the default (no prefix).') + \
    '<div id="code-twc-host"></div>' + \
    '<h3 class="ds-h3 ds-group">Check a breakpoint</h3>' + \
    desc('A page is not done until it has been checked at the breakpoints, with the real values and not by eye.') + \
    bullets(['Check at least three widths: XSmall (about 375px), Small (about 700px) and Medium or Large (1024px or more).',
             'Read the computed values with <code>getComputedStyle</code>: Small must show the mobile values.',
             'Check the 769px edge: 768px is mobile and 769px is desktop.',
             'Test the interaction at every breakpoint, not just the look.'])

b_rules = '<h2 class="ds-h2">Dos and don’ts</h2>' + \
    rules(['Write mobile-first: the style with no prefix is XSmall.',
           'Switch to the Desktop styling at <code>md</code> (769px).',
           'Let a tablet look like mobile, with more columns and a wider margin.',
           'Specify extra component breakpoints with the component.'],
          ['Switch to the Desktop styling at 640px or 768px.',
           'Write a query for one device, for example an iPad.',
           'Use <code>max-width</code> queries for the main layout.',
           'Make a breakpoint of your own for one page.'])

b_refs = '<h2 class="ds-h2">References</h2>' + refs([
    ('https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_media_queries/Using_media_queries', 'MDN: Using media queries', 'Mozilla.'),
    ('https://tailwindcss.com/docs/responsive-design', 'Tailwind CSS: Responsive design', 'Mobile-first breakpoints.'),
    ('https://m3.material.io/foundations/layout/applying-layout/window-size-classes', 'Material Design 3: Window size classes', 'Google.')])

bp_secs = [('overview', b_overview), ('where-your-window-is', b_here), ('breakpoints', b_table), ('what-changes-at-desktop', b_base), ('usage', b_use), ('dos-and-donts', b_rules), ('references', b_refs)]

JS_BP = r'''
  var L = LAYOUT, BPS = L.BPS;
  function rng(b) { return b.to == null ? b.from + 'px and up' : b.from + 'px to ' + b.to + 'px'; }
  function table() {
    var tb = $('#bp-table tbody'); clear(tb);
    BPS.forEach(function (b) {
      var v = L.vals(b), tr = document.createElement('tr');
      tr.innerHTML = '<th scope="row">' + b.name + '<br><span class="ds-na">' + b.device + '</span></th><td><code>' + b.token + '</code></td><td>' + rng(b) + (b.id === 'xs' ? '<br><span class="ds-na">supported from 375px</span>' : '') + '</td><td>' + (b.infinite ? 'Infinite<br><span class="ds-na">' + L.px(v.margin) + ' at 1440px</span>' : L.px(v.margin)) + '</td><td>' + L.px(v.gutter) + '</td><td>' + v.cols + '</td><td>' + b.base + '</td>';
      tb.appendChild(tr);
    });
  }
  function ruler() {
    var r = $('#ruler'); clear(r);
    BPS.forEach(function (b) {
      var s = document.createElement('div'); s.className = 'lg-step'; s.setAttribute('role', 'listitem'); s.dataset.id = b.id;
      s.innerHTML = '<b>' + b.id + '</b><span>' + rng(b) + '</span>'; r.appendChild(s);
    });
  }
  function here() {
    var w = window.innerWidth, b = L.bpFor(w), v = L.vals(b);
    $$('.lg-step').forEach(function (s) { s.setAttribute('aria-current', String(s.dataset.id === b.id)); });
    $('#here').textContent = 'Window ' + w + 'px: ' + b.name + ' (' + b.token + '), ' + b.base + ' base styling, ' + v.cols + ' columns, gutter ' + L.px(v.gutter) + ', margin ' + (b.infinite ? 'infinite (content area ' + L.CONTENT_MAX + 'px)' : L.px(v.margin)) + '.';
  }
  function codes() {
    var mq = '/* XSmall: the style with no query */\n.card { padding: var(--dimension-spacing-space-16); }\n\n' +
      BPS.slice(1).map(function (b) { return '@media (min-width: ' + b.from + 'px) { /* ' + b.name.toLowerCase() + ' */ }'; }).join('\n') +
      '\n\n/* Mobile only, when a style must not reach the desktop */\n@media (max-width: ' + (BPS[2].from - 1) + 'px) { }';
    var tw = 'module.exports = {\n  theme: {\n    screens: {\n' + BPS.slice(1).map(function (b) { return '      ' + b.id + ': \'' + b.from + 'px\',   // ' + b.device; }).join('\n') + '\n    },\n  },\n}';
    [['#code-mq-host', 'CSS: media queries', mq, 'code-mq'], ['#code-twc-host', 'Tailwind config', tw, 'code-twc']].forEach(function (c) {
      var host = $(c[0]); clear(host);
      var box = document.createElement('div'); box.className = 'ds-code';
      box.innerHTML = '<div class="ds-code__bar"><span>' + c[1] + '</span><button type="button" class="mo-copy" data-copy="' + c[3] + '" aria-label="Copy"><span class="mo-ic" aria-hidden="true">content_copy</span></button></div><pre id="' + c[3] + '"></pre>';
      host.appendChild(box); $('#' + c[3]).textContent = c[2];
    });
  }
  function init() { table(); ruler(); here(); codes(); }
  window.addEventListener('resize', here);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(init); else init();
'''

# =============================================================== Spacing (the old foundations/spacing.html, moved here)
sp_overview = '<h2 class="ds-h2">Overview</h2>' + \
    desc('Apply the scale to all margins, padding and position coordinates, on both the vertical and horizontal edges. Use it when you build a component or a page template. It must be used in all Alligo components and designs.') + \
    desc('The margins and gutters of the ' + sec('layout.html', 'grid') + ' are steps of this scale, so the grid and the components share one set of values.') + \
    '<p class="ds-desc ds-note">Most values are multiples of 8px. The 1px, 2px and 4px units are for detail level, and 12px is a complement when needed.</p>' + \
    '<div class="ds-table-wrap"><table class="ds-table"><thead><tr><th>Group</th><th>Tokens</th><th>Range</th><th>Typical use</th></tr></thead><tbody id="groups-table"></tbody></table></div>'

sp_scale = '<h2 class="ds-h2">Scale</h2>' + \
    desc('A systematic set for margins, padding, position coordinates and layout gaps. Each square is the real token size. Click a token to copy its variable.') + \
    '<div class="ds-table-wrap"><table class="ds-table sp-table"><thead><tr><th>Example</th><th>Description</th><th class="ds-tokcell">Token</th></tr></thead><tbody id="scale-table"></tbody></table></div>' + \
    '<p class="ds-desc ds-note" id="coverage"></p>'

sp_layout = '<h2 class="ds-h2">Layout spacing</h2>' + \
    desc('Two tokens change value with the breakpoint. Use them for the air <em>between</em> a section’s own content blocks, for example heading, card grid and buttons. Use the fixed scale above for margins and gutters.') + \
    '<div class="ds-table-wrap"><table class="ds-table"><thead><tr><th>Token</th><th>xs <span class="ds-na">0–639</span></th><th>sm <span class="ds-na">640–768</span></th><th>md <span class="ds-na">769–1023</span></th><th>lg <span class="ds-na">1024–1280</span></th><th>xl <span class="ds-na">1281+</span></th></tr></thead><tbody>' + \
    '<tr><th scope="row"><code>space-lg</code></th><td>32px</td><td>40px</td><td>48px</td><td>56px</td><td>56px</td></tr><tr><th scope="row"><code>space-md</code></th><td>24px</td><td>32px</td><td>40px</td><td>48px</td><td>48px</td></tr></tbody></table></div>' + \
    '<p class="ds-desc ds-note">These two are not in <code>tokens.json</code>. Link <code>/components/css/spacing.css</code> and use <code>var(--dimension-spacing-space-md)</code> or <code>var(--dimension-spacing-space-lg)</code>: the value changes at each breakpoint by itself, so never write the pixel values by hand. They apply to every page, not only to parts built in Storyblok. No <code>space-xs</code>, <code>space-sm</code> or <code>space-xl</code> exists yet.</p>'

sp_how = '<h2 class="ds-h2">How to use</h2>' + \
    desc('Spacing is applied by combining a token with a consumer class.') + \
    '<h3 class="ds-h3">01 · Choose a spacing token</h3>' + desc('A token defines the size only. It maps directly to a pixel value in the spacing scale.') + '<div class="sp-chips" id="chips"></div>' + \
    '<h3 class="ds-h3">02 · Choose a consumer (where the space applies)</h3>' + desc('The consumer says which edge or axis gets the space.') + \
    '<div class="ds-table-wrap"><table class="ds-table"><thead><tr><th>Group</th><th>Class</th><th>Applies to</th></tr></thead><tbody id="consumers"></tbody></table></div>'

sp_examples = '<h2 class="ds-h2">Examples</h2>' + desc('One token and one consumer class per pattern.') + \
    code_static('ex-margin', 'Margin', '<div class="space-24 mb-space">\n  Element\n</div>') + '<p class="ds-desc ds-note">Adds 24px space below the element.</p>' + \
    code_static('ex-padding', 'Padding', '<div class="space-12 px-space">\n  Content\n</div>') + '<p class="ds-desc ds-note">Adds 12px padding left and right.</p>' + \
    code_static('ex-gap', 'Gap', '<div class="space-24 gap-space">\n  <div>A</div>\n  <div>B</div>\n</div>') + '<p class="ds-desc ds-note">Adds 24px spacing between child elements in both directions.</p>'

sp_ref = '<h2 class="ds-h2">Reference</h2>' + \
    desc('A strict directional reference. Each diagram maps one consumer class to one exact edge or axis. Blue marks the applied space; grey is the affected element or its children. Pick a token to redraw every diagram.') + \
    '<div class="ds-toolbar"><span class="ds-toolbar__label" id="ref-l">Token</span><div class="btn-group" role="group" aria-labelledby="ref-l" id="ref-token"></div></div>' + \
    '<div class="sp-cols" id="ref"></div>' + \
    '<p class="ds-desc ds-note">Use one token for external margin, internal padding and the distance between children. X combines left + right and Y combines top + bottom.</p>'

sp_code = '<h2 class="ds-h2">Code</h2>' + desc('Always write the token with its pixel fallback. The list is generated from <code>tokens.json</code>.') + \
    '<div class="ds-code"><div class="ds-code__bar"><span>All spacing tokens</span><button type="button" class="mo-copy" data-copy="code-all" aria-label="Copy"><span class="mo-ic" aria-hidden="true">content_copy</span></button></div><pre id="code-all"></pre></div>' + \
    code_static('code-use', 'Use in CSS', '.card { padding: var(--dimension-spacing-space-16, 16px); }\n.item { margin: var(--dimension-spacing-space-24, 24px) var(--dimension-spacing-space-8, 8px); }\n.grid { display: grid; gap: var(--dimension-spacing-space-24, 24px); }') + \
    code_static('code-bp', 'Page margin and gap per breakpoint (mobile first)', 'section { padding: 0 var(--dimension-spacing-space-16, 16px); }                 /* xs */\n@media (min-width: 640px)  { section { padding: 0 var(--dimension-spacing-space-32, 32px); } }  /* sm, md */\n@media (min-width: 1024px) { section { padding: 0 var(--dimension-spacing-space-40, 40px); } }  /* lg */') + \
    '<p class="ds-desc ds-note">The page margin and the grid gutter have their own tokens, <code>site-margin-*</code> and <code>gutter-*</code>, see ' + sec('layout-tokens.html', 'Tokens') + '.</p>'

sp_usage = '<h2 class="ds-h2">Usage</h2>' + rules(
    ['Use a token for every margin, padding and gap.', 'Prefer 8px multiples; use 1, 2, 4 and 12px only for detail.', 'Use <code>space-md</code> / <code>space-lg</code> between a section’s own content blocks.', 'Write the token with its pixel fallback.'],
    ['Type a pixel value that has a token.', 'Stack two spacing values where one token would do.', 'Add a gap on top of an element’s own margin or padding.', 'Use a fixed token where the space should change per breakpoint.'])

sp_secs = [('overview', sp_overview), ('scale', sp_scale), ('layout', sp_layout), ('how-to', sp_how), ('examples', sp_examples), ('reference', sp_ref), ('code', sp_code), ('usage', sp_usage)]

JS_SP = old_js('spacing', "var TOKENS_URL", "})();\n</script>\n<script src=\"../subnav.js")
JS_SP = JS_SP.replace("""  document.querySelectorAll('[data-copy]').forEach(function (b) {
    wireCopy(b, function () { return document.getElementById(b.getAttribute('data-copy')).textContent; }, 'Copy');
  });
""", '')   # doc-kit.js copies every [data-copy] button already
JS_SP = JS_SP.replace("document.getElementById('n-tokens').textContent = n;", "var nt = document.getElementById('n-tokens'); if (nt) nt.textContent = n;")

# =============================================================== Tokens
t_about = '<h2 class="ds-h2">About the layout tokens</h2>' + \
    desc('The layout tokens set up the ' + sec('layout.html', 'grid') + ' for each ' + sec('layout-breakpoints.html', 'breakpoint') + ': the window widths, the site margin, the gutter and the number of columns. They are in the token package <code>alligo-design-tokens</code>, and the tables below are read from it when the page loads.') + \
    desc('The margin and gutter tokens point at a step of the ' + sec('layout-spacing.html', 'spacing scale') + ' (the column “Points at”), so a change to the scale reaches the grid. The spacing sizes themselves are on the Spacing tab.') + \
    '<div id="tk-live-msg"></div>'

def tgroup(id_, title, text):
    return '<h2 class="ds-h2">%s</h2>' % title + desc(text) + '<div class="ds-table-wrap"><table class="ds-table lg-tok" id="tk-%s"><thead><tr><th scope="col">Token</th><th scope="col">Value</th><th scope="col">Points at</th><th scope="col">Description</th></tr></thead><tbody></tbody></table></div>' % id_

t_bp = tgroup('bp', 'Breakpoint', 'The window widths. The value of <code>bp-sm</code>, <code>bp-md</code> and <code>bp-lg</code> is the <em>end</em> of its range, <code>bp-xs</code> is the smallest supported width and <code>bp-xl</code> is the <em>start</em> of its range. <code>bp-xl-figma</code> is the width of the largest Figma prototype.')
t_margin = tgroup('margin', 'Margin', 'The space at the left and right of the window, per breakpoint. On XLarge the margin is considered infinite: the content area stops at 1200px and is centered. <code>site-margin-xl</code> is the margin at 1440px, the largest prototype width.')
t_gutter = tgroup('gutter', 'Gutter', 'The space between columns, per breakpoint. There is no <code>gutter-xl</code>: XLarge uses <code>gutter-lg</code>.')
t_cols = tgroup('cols', 'Column', 'The number of columns per breakpoint. There is no <code>column-xl</code>: XLarge uses <code>column-lg</code>.')
t_section = tgroup('section', 'Section padding', 'The top and bottom padding of the full-width sections. The package holds one set of these, the one of the Large breakpoint. The padding per breakpoint is on the ' + sec('../components/section-specifications.html#sizes', 'Section') + ' page.')
t_white = tgroup('white', 'Layout whitespace', 'The air between groups of components. These are the values of the Large breakpoint; <code>space-md</code> and <code>space-lg</code> of the ' + sec('layout-spacing.html#layout', 'Layout spacing') + ' step with the window.')
t_cov = '<h2 class="ds-h2">Coverage</h2><p class="ds-desc" id="tk-cov"></p><h3 class="ds-h3">Open points in the package</h3>' + bullets([
    'The values of <code>bp-sm</code>, <code>bp-md</code> and <code>bp-lg</code> are range ends, not the width where the breakpoint starts. Use the start values in code (640, 769, 1024 and 1281px).',
    'The column count exists twice: <code>--dimension-breakpoint-columns-column-*</code> (a number) and <code>--dimension-column-*</code> (with a px unit). Read the number one.',
    'The package has one value for the tokens that have no breakpoint in their name (<code>--dimension-breakpoint-margin</code>, <code>-gutter</code>, <code>-column</code>): the Large one.',
    '<code>space-md</code> and <code>space-lg</code> are not in the package, they come from <code>components/css/spacing.css</code>.'])

tok_secs = [('about', t_about), ('breakpoint', t_bp), ('margin', t_margin), ('gutter', t_gutter), ('column', t_cols), ('section-padding', t_section), ('layout-whitespace', t_white), ('coverage', t_cov)]

JS_TOK = r'''
  var L = LAYOUT, ORDER = ['xs', 'sm', 'md', 'lg', 'xl'];
  var GROUPS = [
    ['bp', /^--dimension-breakpoint-bp-|^--dimension-breakpoint-width$|^--dimension-layout-max-width-/],
    ['margin', /^--dimension-margin-site-margin-|^--dimension-breakpoint-margin$/],
    ['gutter', /^--dimension-gutter-|^--dimension-breakpoint-gutter$/],
    ['cols', /^--dimension-breakpoint-columns-column-|^--dimension-column-|^--dimension-breakpoint-column$/],
    ['section', /^--dimension-breakpoint-section-paddings-/],
    ['white', /^--dimension-layout-vertical-whitespace-/]
  ];
  function key(n) { var m = /-(xs|sm|md|lg|xl)(?:-|$)/.exec(n); return m ? ORDER.indexOf(m[1]) : 9; }
  function copyName(text) {
    var w = document.createElement('span'); w.className = 'ds-copyname';
    w.innerHTML = '<span class="ds-copyname__text"></span><button type="button" class="mo-copy" aria-label="Copy ' + text + '"><span class="mo-ic" aria-hidden="true">content_copy</span></button>';
    w.firstChild.textContent = text;
    w.lastChild.addEventListener('click', function () { var ic = w.lastChild.firstChild, done = function () { ic.textContent = 'check'; setTimeout(function () { ic.textContent = 'content_copy'; }, 1200); }; if (navigator.clipboard) navigator.clipboard.writeText('var(' + text + ')').then(done, done); else done(); });
    return w;
  }
  function fallback(n) {   // the package has no comment on these: say what each one is
    var m = /-(xs|sm|md|lg|xl)$/.exec(n); if (!m) return '-';
    var bp = 'bp-' + m[1];
    if (/site-margin/.test(n)) return 'Left and right site margin at ' + bp + '.';
    if (/gutter/.test(n)) return 'Space between columns at ' + bp + '.';
    if (/breakpoint-columns/.test(n)) return 'Number of columns at ' + bp + '.';
    if (/^--dimension-column-/.test(n)) return 'Number of columns at ' + bp + ', written with a px unit.';
    return '-';
  }
  function value(name, raw) {
    var v = L.resolve(name);
    if (isNaN(v)) return raw;
    return /px\b/.test(raw) || /var\(/.test(raw) ? v + 'px' : String(v);
  }
  function pointsAt(raw) {
    var m = /var\((--[a-z0-9-]+)/.exec(raw); if (!m) return '-';
    return m[1].replace('--dimension-spacing-', '').replace('--dimension-layout-max-width-', 'max-width-').replace('--dimension-', '');
  }
  L.fetchDoc(function (doc) {
    var names = Object.keys(doc), shown = 0;
    GROUPS.forEach(function (g) {
      var rows = names.filter(function (n) { return g[1].test(n); }).sort(function (a, b) { return key(a) - key(b); });
      var tb = document.querySelector('#tk-' + g[0] + ' tbody'); tb.textContent = '';
      rows.forEach(function (n) {
        var tr = document.createElement('tr'), c1 = document.createElement('th'); c1.scope = 'row'; c1.appendChild(copyName(n)); tr.appendChild(c1);
        [value(n, doc[n].raw), pointsAt(doc[n].raw), doc[n].desc || fallback(n)].forEach(function (t) { var td = document.createElement('td'); td.textContent = t; tr.appendChild(td); });
        tb.appendChild(tr); shown++;
      });
    });
    $('#tk-cov').textContent = shown + ' layout tokens from the package are shown on this page. Source: the package file dist/css/base/dimension.css, read when the page loads.';
  }, function () {
    var m = document.createElement('p'); m.className = 'ds-desc'; m.textContent = 'Could not load the token package (alligo-design-tokens) from the CDN. Check the connection and reload.';
    $('#tk-live-msg').appendChild(m);
  });
'''

C = dict(
    slug=SLUG, title='Layout', eyebrow='Foundations', out=OUT_F, first_plain=True,
    crumb_group=('../foundations-overview.html', 'Foundations'),
    lead='The layout is the foundation for all visual elements. It guides creative choices, supports the content and gives every page the same <strong>flexible</strong> frame: a grid, five breakpoints and one spacing scale.',
    select_menu=True, style='', css=[],
    body_js=['../layout-kit.js'],
    pages=[
        dict(kind='grid', suffix='', label='Grid', secs=grid_secs, js=JS_GRID,
             lead='Every page sits on a grid of margins, gutters and columns that adapts to the window. This tab explains the grid and shows it at each breakpoint.'),
        dict(kind='bp', suffix='-breakpoints', label='Breakpoints', secs=bp_secs, js=JS_BP,
             lead='Five breakpoints decide when the layout and the components change. Learn the ranges, how to write them in code and how to check a page.'),
        dict(kind='space', suffix='-spacing', label='Spacing', secs=sp_secs, js=JS_SP,
             lead='The spacing scale gives every margin, padding and gap a <strong>predictable</strong> size. It has <span id="n-tokens">17</span> tokens built on an <strong>8px</strong> base; 1px, 2px, 4px and 12px are for detail. Every bar and diagram on this page is drawn with the <code>var(--…)</code> from the package. See <code>.claude/skills/eco-spacing</code> for the rules.'),
        dict(kind='tok', suffix='-tokens', label='Tokens', secs=tok_secs, js=JS_TOK,
             lead='Every layout token from <code>alligo-design-tokens</code>: the breakpoints, the site margin, the gutter and the columns, read live from the package.'),
    ])
# the Spacing tab reads tokens.json: its script needs ECO.watch (tokens-loader.js) before it runs
C['body_js'] = ['../tokens-loader.js', '../layout-kit.js']

if __name__ == '__main__':
    emit(C)
