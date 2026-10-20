from bc import *

SLUG = 'breadcrumb-bar'
BASE = 'breadcrumb-base'

playground = '<h2 class="ds-h2">Playground</h2>' + desc('Choose a breakpoint, the number of crumbs and the current page, and the bar and its code update. Hover is forced on the first crumb; the links are live.') + \
    '<div class="ds-playground"><div class="ds-stage ds-stage--center" id="pg-stage"><div id="pg-host" style="width:100%"></div></div><div class="ds-controls">' + \
    bp_field('pg-l-bp') + \
    btn_group('pg-l-n', 'Crumbs', 'data-pg="n"', [('2', '2', False), ('3', '3', True), ('4', '4', False), ('5', '5', False), ('6', '6', False)]) + \
    btn_group('pg-l-st', 'State', 'data-pg="state"', [('enabled', 'Enabled', True), ('hover', 'Hover', False)]) + \
    '<div class="ds-field form-field"><label class="form-label form-label--sm" for="pg-label">Current page</label><div class="input-wrap"><div class="input-box input-box--sm"><input class="form-input" type="text" id="pg-label" value="Carpenter pants" placeholder="Current page" /></div></div></div>' + \
    '</div></div><h3 class="ds-h3">Markup for this selection</h3>' + code_box('pg-code', 'HTML')

overview = '<h2 class="ds-h2">Overview</h2>' + desc('A breadcrumb bar shows <strong>where the page sits</strong> in the site and lets the user go back up in one click. It is a row of ' + link_large(BASE + '.html', 'Breadcrumb Base') + ' crumbs with a “/” between them. Every crumb but the last is a link; the last is the current page.') + \
    desc('The bar holds two to six crumbs and has two sizes, Mobile (up to 768px) and Desktop (769px and up). It sits directly under the header, as the first element of the page.') + \
    three_pages(SLUG, 'a breadcrumb bar', 'the values: tokens, sizes, measurements and requirements', 'how to add one to a page')

usage = '<h2 class="ds-h2">Usage</h2><h3 class="ds-h3 ds-group">When to use</h3>' + desc('Use a breadcrumb bar when the page sits more than one step down the navigation tree:') + \
    bullets(['Category, product list, product and landing pages', 'Pages in My Pages that sit below another page', 'Any page where the user may want to go up a level without the browser’s back button']) + \
    '<h3 class="ds-h3 ds-group">When not to use</h3><h3 class="ds-h3">Skip it on the home page</h3>' + desc('The home page has no level above it, and a page directly under Home has no level in between. A bar with one crumb adds nothing.') + \
    fig_pair('<div id="fig-do"></div>', 'Do use a bar when there is a level between Home and the page.', '<div id="fig-dont"></div>', 'Do not show a bar with only the current page.') + \
    '<h3 class="ds-h3">One way back, not two</h3>' + desc('When tabs or a clear back link already lead the user up a level, leave the bar out. Two ways to do the same thing make the page harder to read.') + \
    '<h3 class="ds-h3">Separate the levels with a slash</h3>' + desc('The separator is the “/” character. Never use an icon or a chevron between the crumbs.') + \
    fig_pair('<div id="fig-do2"></div>', 'Do separate the crumbs with “/”.', '<div id="fig-dont2"></div>', 'Do not use arrows or chevrons as separators.') + \
    '<h3 class="ds-h3 ds-group">Quick reference</h3>' + \
    table(['The page is…', 'Use'], [['more than one step below Home', 'Breadcrumb bar'], ['the home page, or directly under Home', 'No bar'], ['a view that tabs or a back link already cover', 'No bar: avoid two'], ['a single level inside the bar', link_large(BASE + '.html', 'Breadcrumb Base')]]) + \
    rules(['Put it first in the page, right under the header.', 'Make every crumb but the last a real link.', 'Set <code>aria-label</code> on the bar and <code>aria-current</code> on the last crumb.', 'Let the block after the bar zero its top padding.'],
          ['Underline the crumbs in the enabled state.', 'Use chevrons or icons between the crumbs.', 'Make the current page a link.', 'Hardcode the side padding.'])

anatomy = '<h2 class="ds-h2">Anatomy</h2><h3 class="ds-h3 ds-group">Bar</h3>' + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout" id="bc-anat" role="img" aria-label="Anatomy of a breadcrumb bar: 1 bar, 2 crumb, 3 separator, 4 current page"><div class="ds-callout__art" id="bc-anat-art" style="padding-top:8px;padding-bottom:8px"></div></div></figure></div>' + \
    ol_parts([('Bar', 'The <code>nav</code> and its flex row. It wraps when the trail does not fit, and keeps 8px between its parts.'), ('Crumb', 'A parent level: a link in a bordered box (' + link_large(BASE + '.html', 'Breadcrumb Base') + ').'), ('Separator', 'A “/” in <code>text-tertiary</code>, 4px wide, 32px high on desktop and 24px on mobile.'), ('Current page', 'The last crumb: bold, black, not clickable.')])

variants = '<h2 class="ds-h2">Variants</h2>' + desc('The bar has no variant classes. What changes is the number of crumbs, from two to six, and the page background behind it.') + \
    '<h3 class="ds-h3 ds-group">Number of crumbs</h3>' + desc('Two to six crumbs. The last one is always the current page.') + \
    fig_one('<div class="pg-col" style="gap:8px" id="v-levels"></div>') + \
    '<h3 class="ds-h3 ds-group">Long names wrap</h3>' + desc('When the trail does not fit, the crumbs wrap to a second row. Each crumb stays whole and the label never wraps inside a crumb.') + \
    fig_one('<div id="v-wrap" style="width:100%;max-width:420px"></div>') + \
    '<h3 class="ds-h3 ds-group">Page background</h3>' + desc('The bar has no background of its own: it takes the background of the page. Public pages are white. My Pages pages are grey on purpose.') + \
    '<div class="ds-figs"><figure class="ds-fig"><div class="ds-fig__stage ds-fig__stage--bar" id="v-white"></div><figcaption class="ds-fig__cap">Public page: <code>background-primary</code></figcaption></figure><figure class="ds-fig"><div class="ds-fig__stage ds-fig__stage--bar pg-grey" id="v-grey"></div><figcaption class="ds-fig__cap">My Pages: <code>background-secondary</code></figcaption></figure></div>'

sizes = '<h2 class="ds-h2">Sizes</h2>' + desc('The bar has two sizes, set by the breakpoint and never by a class: Mobile (xs and sm, up to 768px) and Desktop (769px and up). The bar height, the side padding and the extra bottom padding are in the tables under ' + sec_link(SLUG, 'sizes', 'Sizes') + ' in Specifications.')

layout = '<h2 class="ds-h2">Layout &amp; Appearance</h2><h3 class="ds-h3 ds-group">Placement</h3>' + desc('The bar is the first element in <code>.page</code>, directly under the header and before the title block or the first section. It has its own vertical padding, so the element after it zeroes its top padding: <code>.breadcrumb + .main-content</code>, <code>.breadcrumb + .section</code> and <code>.breadcrumb + .section--first</code> are already set in <code>breadcrumb.css</code>.') + \
    '<h3 class="ds-h3 ds-group">Alignment</h3>' + desc('The crumbs start at the left page margin, <code>var(--px-page)</code>, and run in one row. A trail that is too long wraps to the next row, aligned to the same margin.') + \
    '<h3 class="ds-h3 ds-group">Appearance</h3>' + desc('No background, no shadow. White on public pages, grey on My Pages. Colors and token names are under ' + sec_link(SLUG, 'design-tokens', 'Design Tokens') + ' in Specifications.')

behavior = '<h2 class="ds-h2">Behavior</h2><h3 class="ds-h3 ds-group">Wrapping</h3>' + desc('The bar is a flex row with <code>flex-wrap: wrap</code>. When the next crumb or separator does not fit, it moves to a new row. A crumb is never cut or shortened.') + \
    '<h3 class="ds-h3 ds-group">Hover and focus</h3>' + desc('These belong to the crumb: see ' + link_large(BASE + '.html', 'Breadcrumb Base') + '.') + \
    '<h3 class="ds-h3 ds-group">Breakpoints</h3>' + desc('At 769px the crumbs and the separator get larger, the bar gets taller and the extra bottom padding grows. A tablet (640–768px) looks like mobile.')

access = '<h2 class="ds-h2">Accessibility</h2>' + desc('All requirements are listed under ' + sec_link(SLUG, 'accessibility-requirements', 'Accessibility Requirements') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Keyboard support</h3>' + bullets(['<strong>Tab</strong> moves through the parent crumbs from left to right.', '<strong>Enter</strong> follows a link.', 'The current page is skipped.']) + \
    '<h3 class="ds-h3 ds-group">Screen reader support</h3>' + desc('The <code>nav</code> is announced as a landmark named “Breadcrumb”. The current page is read with <code>aria-current="page"</code>. The “/” is only visual and is hidden from screen readers.')

related = '<h2 class="ds-h2">Related</h2><ul class="ds-bullets"><li><strong>' + link_large(BASE + '.html', 'Breadcrumb Base') + '</strong>. One level of the trail.</li><li><strong>' + link_large('breadcrumb.html', 'Breadcrumb') + '</strong>. The guide to the crumb and the bar.</li><li><strong>' + link_large('section.html', 'Section') + '</strong>. The first section after the bar zeroes its top padding.</li><li><strong>' + link_large('tabs.html', 'Tabs') + '</strong>. Sub-navigation in the same context.</li><li><strong>' + link_large('action-link.html', 'Action link') + '</strong>. A standalone “back” link.</li></ul>'

references = '<h2 class="ds-h2">References</h2>' + refs([
    ('https://www.w3.org/WAI/ARIA/apg/patterns/breadcrumb/', 'WAI-ARIA Authoring Practices: Breadcrumb pattern', 'The landmark, the list of links and aria-current.'),
    ('https://www.w3.org/WAI/WCAG22/Understanding/location.html', 'WCAG 2.2: Location', 'Success criterion 2.4.8: show where the user is.'),
    ('https://www.nngroup.com/articles/breadcrumbs/', 'Nielsen Norman Group: Breadcrumbs', 'Guidelines for location breadcrumbs.'),
    ('https://fluent2.microsoft.design/components/web/react/core/breadcrumb/usage', 'Fluent 2: Breadcrumb', 'Microsoft.'),
    ('https://carbondesignsystem.com/components/breadcrumb/usage/', 'Carbon Design System: Breadcrumb', 'IBM.')])

ex = [('playground', playground), ('overview', overview), ('usage', usage), ('anatomy', anatomy), ('variants', variants), ('sizes', sizes), ('layout', layout), ('behavior', behavior), ('accessibility', access), ('related', related), ('references', references)]

# ---------------------------------------------------------------- Specifications
st_tok = '<h2 class="ds-h2">Design Tokens</h2>' + desc('Resolved from the live token package. The crumb tokens are the same as in ' + link_large(BASE + '-specifications.html#design-tokens', 'Breadcrumb Base') + '; the separator is the only token of the bar itself.') + \
    '<div class="ds-table-wrap"><table class="ds-table" id="tok-table"><thead><tr><th scope="col">Part</th><th scope="col">Use</th><th scope="col">Token</th><th scope="col">Value</th></tr></thead><tbody></tbody></table></div>'

st_sizes = '<h2 class="ds-h2">Sizes</h2>' + table(['Breakpoint', 'Bar height', 'Crumb padding', 'Text', 'Separator height', 'Side padding', 'Extra bottom padding'], [
    ['xs (0–639px)', '56px', '6px 7px', '12/12, 0.24px', '24px', '16px', '0'], ['sm (640–768px)', '56px', '6px 7px', '12/12, 0.24px', '24px', '32px', '0'],
    ['md (769–1023px)', '72px', '9px 10px', '14/14, 0.28px', '32px', '32px', '8px'], ['lg and xl (1024px+)', '80px', '9px 10px', '14/14, 0.28px', '32px', '40px', '16px']]) + \
    note('The bar height is the crumb height plus 16px above and below (<code>.breadcrumb__bar</code> padding 16px 0). sm still looks like mobile. Side padding is always <code>var(--px-page)</code>, never a fixed value, and never <code>var(--px-full)</code>.')

st_meas = '<h2 class="ds-h2">Measurements</h2><h3 class="ds-h3 ds-group">Dimensions</h3>' + desc('Padding of the bar, drawn on the real <code>.breadcrumb__bar</code>: 16px above and below the crumbs. The side padding and the extra bottom padding belong to the <code>.breadcrumb</code> block and are in the table. Change the Breakpoint to re-measure.') + \
    toolbar([('mb-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force')]) + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage" style="padding:0;min-height:0"><div class="measure" role="img" aria-label="Padding of the breadcrumb bar"><div class="measure__item"><span class="measure__name">1 · Bar, 3 crumbs</span><div class="measure__obj"><div class="measure__subject" id="ms-bar" style="display:block;width:max-content;max-width:100%"></div>' + \
    '<i class="measure__pad measure__pad--t"></i><i class="measure__pad measure__pad--b"></i><i class="measure__pad measure__pad--l"></i><i class="measure__pad measure__pad--r"></i>' + \
    '<b class="measure__dim measure__dim--v measure__dim--t"><span></span></b><b class="measure__dim measure__dim--v measure__dim--b"><span></span></b><b class="measure__dim measure__dim--h measure__dim--l"><span></span></b><b class="measure__dim measure__dim--h measure__dim--r"><span></span></b></div></div></div></div><figcaption class="ds-fig__cap">The bar at true size (1:1).</figcaption></figure></div>' + \
    table(['Attribute', 'Value'], [['Padding of the bar row', '16px top and bottom, none at the sides'], ['Side padding of the block', '<code>var(--px-page)</code>: 16px xs, 32px sm and md, 40px lg and xl'], ['Extra bottom padding of the block', '0 below 769px, 8px at md, 16px from 1024px'], ['Gap between parts', '8px'], ['Bar height', '56px mobile, 72px md, 80px lg and xl'], ['Separator', '4px wide, 24px high on mobile, 32px on desktop']]) + \
    '<h3 class="ds-h3 ds-group">Spacing</h3>' + desc('The vertical and gap values as spacing tokens.') + table(['Part', 'Value'], [['Bar padding, top and bottom', '<code>space-16</code>'], ['Gap between parts', '<code>space-8</code>'], ['Side padding', '<code>var(--px-page)</code> (the grid margin)'], ['Extra bottom, md', '<code>space-8</code>'], ['Extra bottom, lg and xl', '<code>space-16</code>']])

st_states = '<h2 class="ds-h2">States</h2>' + desc('The bar has no state of its own. Enabled, hover and current page belong to each crumb: see ' + link_large(BASE + '-specifications.html#states', 'Breadcrumb Base') + '.')

st_typo = '<h2 class="ds-h2">Typography</h2>' + table(['Part', 'Font', 'Size / line', 'Letter spacing', 'Weight'], [['Crumb, desktop', 'Breuer Condensed', '14px / 14px', '0.28px', 'Regular 400, current 600'], ['Crumb, mobile', 'Breuer Condensed', '12px / 12px', '0.24px', 'Regular 400, current 600'], ['Separator', 'Breuer Condensed', '14px', '0.28px', 'Regular 400']]) + \
    note('Open points against Figma: the desktop separator is <code>body-sm</code> in Figma (14/20, 0.36px) and has font feature <code>ss06</code>; <code>breadcrumb.css</code> writes 0.28px and no <code>ss06</code> for both sizes. Not changed here: the shared file is changed only when you ask.')

st_struct = '<h2 class="ds-h2">Structure</h2><h3 class="ds-h3 ds-group">Elements</h3>' + table(['Element', 'Class', 'Notes'], [['Block', '<code>breadcrumb</code>', 'The <code>nav</code> with <code>aria-label="Breadcrumb"</code>. Side padding <code>var(--px-page)</code>.'], ['Bar', '<code>breadcrumb__bar</code>', 'Flex row, wraps, 8px gap, 16px padding above and below.'], ['Crumb', '<code>breadcrumb-item</code>', 'A link in a bordered box.'], ['Current page', '<code>breadcrumb-item--active</code>', 'The last crumb.'], ['Separator', '<code>breadcrumb-sep</code>', 'A “/” character.']]) + \
    '<h3 class="ds-h3 ds-group">Types</h3>' + table(['Crumbs', 'Markup'], [['2 (Home, current page)', '1 link, 1 separator, 1 current'], ['3 to 6', 'Parent links with a separator between each, then the current page']]) + \
    '<h3 class="ds-h3 ds-group">Width</h3>' + desc('The bar is as wide as the page content. The crumbs keep their own width and wrap to the next row when the row is full.')

st_motion = '<h2 class="ds-h2">Motion</h2>' + desc('The bar does not move. Only the text color of a crumb changes on hover: see ' + link_large(BASE + '-specifications.html#motion', 'Breadcrumb Base') + '.')

st_behavior = '<h2 class="ds-h2">Behavior</h2>' + table(['Topic', 'Result'], [['Placement', 'First in <code>.page</code>, directly under the header, before the title block. The block that follows zeroes its top padding.'], ['Wrapping', 'The crumbs wrap to a new row when the trail is too long. A crumb never wraps its label.'], ['Breakpoint', 'The sizes change at 769px. sm looks like mobile.'], ['Background', 'None. It takes the page background: white or, on My Pages, grey.']])

st_access = '<h2 class="ds-h2">Accessibility Requirements</h2>' + table(['Topic', 'Requirement'], [
    ['Landmark', '<code>nav[aria-label="Breadcrumb"]</code>.'], ['Links', 'Every crumb but the last is an <code>&lt;a href&gt;</code>. The last is a <code>span</code> with <code>aria-current="page"</code>.'],
    ['Separator', 'A “/” character that adds no meaning. Hide it from screen readers when you build the markup with a list; the shipped markup keeps it as text.'], ['Order', 'The crumbs are in DOM order from Home to the current page.'],
    ['Focus', 'A visible focus ring on every link (WCAG 2.4.7).'], ['Contrast', 'Text must reach 4.5:1 on the page background, white or grey (WCAG 1.4.3).']])

spec = [('design-tokens', st_tok), ('sizes', st_sizes), ('measurements', st_meas), ('states', st_states), ('typography', st_typo), ('structure', st_struct), ('motion', st_motion), ('behavior', st_behavior), ('accessibility-requirements', st_access)]

# ---------------------------------------------------------------- Code
c_basic = '<h2 class="ds-h2">Basic Usage</h2>' + desc('Link the shared stylesheet once per page. Never copy the rules into a page.') + table(['Step', 'What to do'], [
    ['1. Link', '<code>&lt;link rel="stylesheet" href="/components/css/breadcrumb.css"&gt;</code>. Both templates already have it.'], ['2. Place it', 'First in <code>.page</code>, directly under the header, before the title block or the first section.'],
    ['3. Crumbs', 'A link for every parent level, a <code>breadcrumb-sep</code> between each, and the current page as the last item.'], ['4. Next block', 'The block after the bar has its top padding zeroed by the shared file. Do not add your own.']])
c_div = '<h2 class="ds-h2">Breadcrumb Bar</h2>' + desc('Copy the markup you need.') + '<div id="recipes"></div>'
c_api = '<h2 class="ds-h2">API</h2><h3 class="ds-h3 ds-group">Classes</h3>' + table(['Class', 'Use'], [['<code>breadcrumb</code>', 'The <code>nav</code>: side padding and the extra bottom padding.'], ['<code>breadcrumb__bar</code>', 'The row: flex, wrap, 8px gap, 16px padding above and below.'], ['<code>breadcrumb-item</code>', 'A crumb. See Breadcrumb Base.'], ['<code>breadcrumb-item--active</code>', 'The current page.'], ['<code>breadcrumb-sep</code>', 'The “/” between two crumbs.']]) + \
    '<h3 class="ds-h3 ds-group">Things to know</h3>' + bullets(['The bar needs <code>--px-page</code> from the page (16, 32 and 40px per breakpoint). Both templates define it.', 'Use <code>var(--px-page)</code> for the side padding, never <code>var(--px-full)</code>.', 'The bar has no background of its own.', 'The sizes change at 769px. There are no size classes.'])
c_css = '<h2 class="ds-h2">CSS / Tailwind</h2>' + desc('The component is one CSS file, shared by every page. Link it, never copy it. The CSS below is read from the file the page links, so it is always what you see.') + code_box('css-code', 'CSS (components/css/breadcrumb.css)')
code = [('basic-usage', c_basic), ('breadcrumb-bar', c_div), ('api', c_api), ('css-tailwind', c_css, False)]

# ---------------------------------------------------------------- scripts
JS_EX = JS_BUILD + r'''
  function put(sel, node) { clear($(sel)).appendChild(node); }
  var st = { n: '3', state: 'enabled' };
  function renderPg() {
    var last = $('#pg-label').value || 'Carpenter pants';
    put('#pg-host', bar(+st.n, last, st.state === 'hover'));
    var h = barMarkup(+st.n, last); if (st.state === 'hover') h = '<!-- hover is forced here for preview; in production it comes from :hover -->\n' + h;
    $('#pg-code').textContent = h;
  }
  DK.wire(st, renderPg); $('#pg-label').addEventListener('input', renderPg);
  DK.bp();

  var lv = clear($('#v-levels')); [2, 3, 4, 5, 6].forEach(function (n) { lv.appendChild(bar(n, 'Carpenter pants')); });
  put('#v-wrap', bar(4, 'Carpenter pants for winter work in cold storage'));
  put('#v-white', bar(3, 'Work pants')); put('#v-grey', bar(3, 'Work pants'));

  /* Usage figures */
  put('#fig-do', bar(3, 'Work pants')); put('#fig-dont', bar(1, 'Home'));
  put('#fig-do2', bar(3, 'Work pants'));
  var bad = bar(3, 'Work pants'); $$('.breadcrumb-sep', bad).forEach(function (s) { s.textContent = '>'; }); put('#fig-dont2', bad);

  /* Anatomy */
  var a = bar(3, 'Work pants'); put('#bc-anat-art', a);
  DK.callouts($('#bc-anat'), [
    { n: 1, el: $('.breadcrumb__bar', a), side: 'top', len: 40, at: 'edge' },
    { n: 2, el: $('.breadcrumb-item', a), side: 'bottom', len: 40, at: 'edge' },
    { n: 3, el: $('.breadcrumb-sep', a), side: 'top', len: 40, at: 'center' },
    { n: 4, el: $('.breadcrumb-item--active', a), side: 'bottom', len: 40, at: 'edge' }
  ]);
  renderPg();
'''

JS_SPEC = JS_BUILD + r'''
  DK.tokenTable($('#tok-table tbody'), [
    ['Crumb, all states', 'Border', 'border-action-3'], ['Crumb, enabled', 'Text', 'text-tertiary'], ['Crumb, hover', 'Text', 'text-action-primary'], ['Current page', 'Text', 'text-primary'], ['Separator', 'Text', 'text-tertiary'], ['Keyboard focus', 'Ring', 'border-focus']]);
  var host = $('#ms-bar'); var b = bar(3, 'Work pants'); var inner = $('.breadcrumb__bar', b); b.style.padding = '0'; host.classList.remove('measure__subject'); inner.classList.add('measure__subject'); inner.style.cssText = 'width:max-content;max-width:100%'; host.appendChild(inner);
  DK.bp(function () { if (window.ECO_MEASURE) ECO_MEASURE.init(); });
'''

JS_CODE = r'''
  DK.recipes($('#recipes'), [
    ['Two levels', '<nav class="breadcrumb" aria-label="Breadcrumb">\n  <div class="breadcrumb__bar">\n    <a href="/" class="breadcrumb-item">Home</a>\n    <span class="breadcrumb-sep">/</span>\n    <span class="breadcrumb-item breadcrumb-item--active" aria-current="page">Reviews</span>\n  </div>\n</nav>'],
    ['Several levels', '<nav class="breadcrumb" aria-label="Breadcrumb">\n  <div class="breadcrumb__bar">\n    <a href="/" class="breadcrumb-item">Home</a>\n    <span class="breadcrumb-sep">/</span>\n    <a href="/clothing" class="breadcrumb-item">Clothing and protective gear</a>\n    <span class="breadcrumb-sep">/</span>\n    <a href="/clothing/pants" class="breadcrumb-item">Work pants</a>\n    <span class="breadcrumb-sep">/</span>\n    <span class="breadcrumb-item breadcrumb-item--active" aria-current="page">Carpenter pants</span>\n  </div>\n</nav>'],
    ['In a page', '<div class="page">\n  <nav class="breadcrumb" aria-label="Breadcrumb">…</nav>\n  <div class="main-content">…</div>   <!-- top padding zeroed by breadcrumb.css -->\n</div>']
  ]);
  DK.printCss($('#css-code'), 'breadcrumb');
'''

C = dict(
    slug=SLUG, title='Breadcrumb Bar', eyebrow='Patterns · Navigation', parent=('../components-overview.html#patterns', 'Patterns'),
    lead='A breadcrumb bar shows <strong>where the page sits</strong> in the site and lets the user go back up in one click. Two to six crumbs, separated by a slash.',
    lead_ex='Every example on this page is the real component, not a picture. Figma: ' + fig_link(FIGMA_BAR, 'Breadcrumb Bar') + ' and ' + fig_link(FIGMA_RESP, 'responsive behavior') + '.',
    lead_spec='Tokens, sizes, measurements and requirements. Values come from the live token package and from Figma: ' + fig_link(FIGMA_BAR, 'Breadcrumb Bar') + '.',
    lead_code='How to add a breadcrumb bar to a page. The file is <code>components/css/breadcrumb.css</code>.',
    select_menu=False, css=['breadcrumb'], style=STYLE, ex=ex, spec=spec, code=code, js_ex=JS_EX, js_spec=JS_SPEC, js_code=JS_CODE)

if __name__ == '__main__':
    emit(C)
