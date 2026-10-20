from build import *

FIGMA = 'https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=11614-537671'
SLUG = 'pagination'

STYLE = r'''    .pg-note { font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-tertiary); }
    .pg-list { display: flex; flex-direction: column; gap: 8px; width: 100%; }
    #pg-list { max-height: 320px; overflow-y: auto; }   /* demo: a long list scrolls inside the stage */
    .pg-item { padding: 12px 16px; background: var(--color-surface-raised-primary); color: var(--color-text-primary); font-size: 16px; line-height: 22px; }
    .pg-snaps { display: grid; gap: 32px 24px; grid-template-columns: minmax(0, 1fr); width: 100%; }
    @media (min-width: 640px) { .pg-snaps { grid-template-columns: repeat(3, minmax(0, 1fr)); } }
    .pg-snap { display: flex; flex-direction: column; align-items: center; gap: 12px; }
    .pg-snap > span { font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-tertiary); }
    .pg-callout.ds-fig__stage.ds-callout { padding-left: 64px; padding-right: 64px; }
    .pg-callout .ds-callout__art { width: 190px; max-width: 100%; margin: 0 auto; }
    .pg-callout .pagination, .pg-snap .pagination, .ds-fig__stage .pagination { margin-top: 0; }   /* demo: the top spacing belongs to the page, not to a figure */
    .pg-stack { display: flex; flex-direction: column; gap: 16px; width: 100%; align-items: center; }
    .pg-ghost { font-size: 16px; line-height: 22px; color: var(--color-surface-60); text-align: center; }'''

playground = '<h2 class="ds-h2">Playground</h2>' + desc('A list of reviews with the real component under it. Press the button to load 10 more items at a time (10, 20, then 22 of 22): the counter and the bar follow, and the button becomes disabled when everything is shown.') + \
    '<div class="ds-playground"><div class="ds-stage" id="pg-stage" style="display:block"><div class="pg-list" id="pg-list"></div><div id="pg-host"></div></div><div class="ds-controls">' + \
    '<button type="button" class="btn btn--secondary btn--sm" id="pg-reset" style="align-self:flex-start"><span class="btn__label">Reset</span></button></div></div>' + \
    '<h3 class="ds-h3">Markup for this selection</h3>' + code_box('pg-code', 'HTML')

overview = '<h2 class="ds-h2">Overview</h2>' + desc('Pagination here is a <strong>“load more” pattern</strong>: a counter, a thin progress bar and one button that adds more items to a list without a page load. It tells the user how far through the list they are and gives one clear way to continue.') + \
    desc('The component is narrow (190px) and centered, whatever the width of its section. It has one layout and no variants. The counter and the bar come from two numbers, the items shown and the total, so the total must be known up front.') + \
    three_pages(SLUG, 'pagination', 'the values: tokens, spacing per breakpoint, measurements and requirements', 'how to add it to a list')

usage = '<h2 class="ds-h2">Usage</h2><h3 class="ds-h3 ds-group">When to use</h3>' + desc('Use it at the end of a list that is too long to show at once. Use it to:') + \
    bullets(['Load more reviews, products or orders into the same list', 'Show how much of the list is visible (the total count is known)', 'Keep the user on the page, in the same scroll position']) + \
    '<h3 class="ds-h3 ds-group">When not to use</h3><h3 class="ds-h3">When everything is already shown</h3>' + desc('A counter that says “6 of 6” and a bar that is full has nothing left to offer. Keep the component and disable the button, so the user sees the list is complete.') + \
    fig_pair('<div class="pg-stack" id="fig-do1"></div>', 'Do disable the button when every item is shown.', '<div class="pg-stack" id="fig-dont1"></div>', 'Do not remove the button and leave the counter and the bar alone.') + \
    '<h3 class="ds-h3">When the button is not Secondary</h3>' + desc('The action is supporting, not the main goal of the page. Keep the Secondary button at Medium size.') + \
    fig_pair('<div class="pg-stack" id="fig-do2"></div>', 'Do use the Secondary Medium button.', '<div class="pg-stack" id="fig-dont2"></div>', 'Do not use a Primary button: it competes with the main call to action.') + \
    '<h3 class="ds-h3 ds-group">Quick reference</h3>' + \
    table(['The list…', 'Use'], [['is long, more items load on request and the total is known', 'Pagination (load more)'], ['is already fully shown', 'Pagination with a disabled button'], ['needs numbered pages (1, 2, 3 …)', 'A different pattern (not built yet)']]) + \
    rules(['Place it last in the section or list.', 'Disable the button when all items are shown.', 'Compute the bar width from the numbers.', 'Use the Secondary Medium button.'],
          ['Add padding below the component.', 'Remove the button when all items are shown.', 'Stretch it to the section width.', 'Use a Primary button.'])

anatomy = '<h2 class="ds-h2">Anatomy</h2><h3 class="ds-h3 ds-group">Pagination</h3>' + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout pg-callout" id="pg-anat" role="img" aria-label="Anatomy of pagination: 1 counter, 2 progress bar, 3 button"><div class="ds-callout__art" id="pg-anat-art"></div></div></figure></div>' + \
    ol_parts([('Counter', 'Shows how many items are visible and how many there are in all. Body-md, Surface 60, centered.'), ('Progress bar', 'A 2px track (Surface 10) with a fill (Surface 100). The fill width is visible ÷ total.'), ('Button', 'The eco-button Secondary, Medium, as wide as the component.')])

variants = '<h2 class="ds-h2">Variants</h2>' + desc('Pagination has no variants. It looks the same at every step of the list, only the numbers change. Three snapshots of the same component:') + \
    fig_one('<div class="pg-snaps" id="v-snap"></div>') + \
    note('When every item is shown the counter and the bar are full and the button is disabled, see Behavior.')

sizes = '<h2 class="ds-h2">Sizes</h2>' + desc('Pagination has one size: <strong>190px</strong> wide (<code>max-width: 100%</code>). The button inside is Medium: 40px high on mobile and tablet, 48px from 769px. All values are under ' + sec_link(SLUG, 'sizes', 'Sizes') + ' in Specifications.')

layout = '<h2 class="ds-h2">Layout &amp; Appearance</h2><h3 class="ds-h3 ds-group">Alignment</h3>' + desc('The component is centered in its section and never stretched to the section width, however wide the section is. Text is centered.') + \
    '<h3 class="ds-h3 ds-group">Placement</h3>' + desc('Place it as the last element of the section or list it belongs to. It has <strong>no bottom spacing of its own</strong>: the padding of the section below it gives the air. Adding padding or margin below it doubles the space.') + \
    '<h3 class="ds-h3 ds-group">Spacing above</h3>' + desc('The space above the component is page spacing, so it follows the five ECO breakpoints: 24px on mobile, 32px on tablet and 40px from 769px. It steps at 640px, while the component itself keeps mobile styling until 769px. The values are under ' + sec_link(SLUG, 'measurements', 'Measurements') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Appearance</h3>' + desc('Counter text in Surface 60, a Surface 10 track with a Surface 100 fill, and a Secondary button. Token names are under ' + sec_link(SLUG, 'design-tokens', 'Design Tokens') + ' in Specifications.')

behavior = '<h2 class="ds-h2">Behavior</h2><h3 class="ds-h3 ds-group">Load more</h3>' + desc('A click on the button adds the next items to the list and calls <code>updatePagination(key, visible, total)</code>. The counter text and the bar fill update together. The fill animates its width with <code>duration-medium-2</code> and <code>ease-standard</code>.') + \
    '<h3 class="ds-h3 ds-group">Items per click</h3>' + desc('One click loads <strong>10 more items</strong>. The last click loads the rest: 10, 20, then 22 of 22.') + '<h3 class="ds-h3 ds-group">All items shown</h3>' + desc('When <code>visible</code> reaches <code>total</code>, the script sets <code>disabled</code> on the button. The counter and the bar stay, full.') + \
    '<h3 class="ds-h3 ds-group">Breakpoints</h3>' + desc('Counter text and button follow mobile styling below 769px (<code>sm</code> looks like mobile). The space above steps at 640px and 769px.')

access = '<h2 class="ds-h2">Accessibility</h2>' + desc('All requirements are listed under ' + sec_link(SLUG, 'accessibility-requirements', 'Accessibility Requirements') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Keyboard support</h3>' + desc('The button is a native <code>&lt;button&gt;</code>: Tab reaches it, Enter and Space load more. It has the eco-button focus ring.') + \
    '<h3 class="ds-h3 ds-group">Screen reader support</h3>' + desc('Mark the counter as a polite live region (<code>aria-live="polite"</code>) so the new count is announced. The bar repeats the counter, so hide it from assistive technology with <code>aria-hidden="true"</code>. A button that becomes disabled loses focus: move focus to the first new item first.')

related = '<h2 class="ds-h2">Related</h2><ul class="ds-bullets"><li><strong>' + link_large('button.html', 'Button') + '</strong>. The load-more button is Secondary, Medium.</li><li><strong>' + link_large('section.html', 'Section') + '</strong>. The section gives the space below the component.</li></ul>' + \
    note('To be added: numbered page navigation (1, 2, 3 …) is a different pattern and is not built yet.')

references = '<h2 class="ds-h2">References</h2>' + refs([
    ('https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html', 'WCAG 2.2: Status Messages', 'Success criterion 4.1.3: announce the new count without moving focus.'),
    ('https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html', 'WCAG 2.2: Focus Order', 'Success criterion 2.4.3: where focus goes when the button disappears.'),
    ('https://carbondesignsystem.com/components/pagination/usage/', 'Carbon Design System: Pagination', 'IBM.'),
    ('https://design-system.service.gov.uk/components/pagination/', 'GOV.UK Design System: Pagination', 'GOV.UK.')])

ex = [('playground', playground), ('overview', overview), ('usage', usage), ('anatomy', anatomy), ('variants', variants), ('sizes', sizes), ('layout', layout), ('behavior', behavior), ('accessibility', access), ('related', related), ('references', references)]

# ---------------------------------------------------------------- Specifications
st_tok = '<h2 class="ds-h2">Design Tokens</h2>' + desc('Resolved from the live token package.') + \
    '<div class="ds-table-wrap"><table class="ds-table" id="tok-table"><thead><tr><th scope="col">Part</th><th scope="col">Use</th><th scope="col">Token</th><th scope="col">Value</th></tr></thead><tbody></tbody></table></div>' + \
    '<h3 class="ds-h3">Open points</h3>' + desc('<code>pagination.css</code> writes the gaps (24px, 16px), the 190px width and the counter text (16/22, 17/24 from 769px) as pixels. The values match the spacing scale and the <code>body-md</code> pair, but are not yet written as tokens.')

st_sizes = '<h2 class="ds-h2">Sizes</h2>' + table(['Property', 'Value'], [
    ['Width', '190px, <code>max-width: 100%</code>, centered, never stretched'], ['Gap: info block to button', '24px'], ['Gap: counter to bar', '16px'], ['Progress bar height', '2px'],
    ['Button', '<a class="inline-link inline-link--small" href="button.html">Button</a> Secondary, Medium: 40px high below 769px, 48px from 769px, full width']]) + \
    note('The component is one size. Only the space above it steps with the breakpoint, see Measurements.')

st_meas = '<h2 class="ds-h2">Measurements</h2><h3 class="ds-h3 ds-group">Dimensions</h3>' + table(['Attribute', 'Value'], [['Counter text', 'Body-md: 16/22 below 769px, 17/24 from 769px, letter spacing 0.32px'], ['Progress bar', '2px'], ['Button label', 'Label-lg: 16/16 below 769px, 18/18 from 769px']]) + \
    note('The component has no padding of its own, so there is no measurement figure. The space above it is a margin and is listed below.') + \
    '<h3 class="ds-h3 ds-group">Spacing</h3>' + table(['Breakpoint', 'Space above', 'Token', 'Space below (the section)'], [
        ['xs, 0–639px', '24px', '<code>space-24</code>', '40px'], ['sm, 640–768px', '32px', '<code>space-32</code>', '48px'], ['md, 769–1023px', '40px', '<code>space-40</code>', '64px'], ['lg, 1024–1280px', '40px', '<code>space-40</code>', '80px'], ['xl, 1281px and up', '40px', '<code>space-40</code>', '80px']]) + \
    note('The space above is page spacing, so it steps at 640px, not at <code>space-md</code>. The space below is the bottom padding of the section the component sits in (<code>eco-section</code>), never padding on the component.')

st_states = '<h2 class="ds-h2">States</h2>' + desc('The component has no states of its own. The button has the states of the <a class="inline-link inline-link--large inline-link--secondary" href="button-specifications.html#states">Secondary button</a>. When all items are shown, the button is <strong>disabled</strong> (Figma Secondary disabled) and the counter and the bar show the full count.')

st_type = '<h2 class="ds-h2">Typography</h2>' + table(['Element', 'Style', 'Mobile', 'Desktop (769px)'], [['Counter text', 'body-md, regular, 0.32px', '16/22', '17/24'], ['Button label', 'label-lg, bold, uppercase', '16/16, 0.32px', '18/18, 0.18px']])

st_struct = '<h2 class="ds-h2">Structure</h2><h3 class="ds-h3 ds-group">Elements</h3>' + table(['Element', 'Class', 'Notes'], [
    ['Component', '<code>pagination</code> (+ <code>id="pagination-{key}"</code>)', 'Flex column, 190px, centered. The button is disabled when all items are shown.'], ['Info block', '<code>pagination__info</code>', 'Counter and bar.'],
    ['Counter', '<code>pagination__count</code>', 'Holds <code>&lt;span id="{key}-pagination-count"&gt;</code>.'], ['Progress', '<code>pagination__progress</code>', 'The 2px track.'], ['Fill', '<code>pagination__progress-bar</code> (+ <code>id="{key}-pagination-bar"</code>)', 'Width set by script.'], ['Button', '<code>btn btn--secondary btn--md</code>', 'The eco-button, full width of the component.']]) + \
    '<h3 class="ds-h3 ds-group">Width</h3>' + desc('190px, or the width of the parent when that is narrower.')

st_motion = '<h2 class="ds-h2">Motion</h2>' + table(['Property', 'Token', 'Value'], [['Fill width', '<code>ease-standard</code>', 'Changes over <code>duration-medium-2</code>']]) + \
    note('The width change is a state change in place, so it uses the standard easing. Reduced motion is not handled in the component CSS (open point).')

st_behavior = '<h2 class="ds-h2">Behavior</h2>' + table(['Topic', 'Rule'], [
    ['Fill width', 'Always <code>(visible / total) × 100%</code>, set by <code>updatePagination(key, visible, total)</code>. The first value may be rendered by the server.'],
    ['All shown', 'The <code>disabled</code> attribute goes on the button. The component is never hidden and the button never removed.'], ['Ids', 'The script reads <code>{key}-pagination-count</code>, <code>{key}-pagination-bar</code> and <code>pagination-{key}</code>.'], ['Breakpoint', 'Text and button change at 769px. The space above changes at 640px and 769px.']])

st_access = '<h2 class="ds-h2">Accessibility Requirements</h2>' + table(['Topic', 'Requirement'], [
    ['Button', 'A native <code>&lt;button&gt;</code> with a specific label (“Show more reviews”). Keyboard: Tab, Enter, Space. Visible focus ring from eco-button.'],
    ['Status message', 'Put <code>aria-live="polite"</code> on the counter so the new count is announced without moving focus (WCAG 4.1.3).'],
    ['Progress bar', 'It repeats the counter, so give it <code>aria-hidden="true"</code>. Never rely on the bar alone (WCAG 1.4.1).'],
    ['Focus', 'A button that becomes disabled loses focus: move focus to the first item that was just loaded (WCAG 2.4.3).'],
    ['Contrast', 'Counter text is Surface 60 on white. The track (Surface 10) is decoration, the count carries the meaning.']])

spec = [('design-tokens', st_tok), ('sizes', st_sizes), ('measurements', st_meas), ('states', st_states), ('typography', st_type), ('structure', st_struct), ('motion', st_motion), ('behavior', st_behavior), ('accessibility-requirements', st_access)]

# ---------------------------------------------------------------- Code
c_basic = '<h2 class="ds-h2">Basic Usage</h2>' + desc('Link the shared files once per page. Never copy the rules into a page.') + table(['Step', 'What to do'], [
    ['1. Link', '<code>&lt;link rel="stylesheet" href="/components/css/button.css"&gt;</code> and <code>pagination.css</code>, then <code>&lt;script src="/components/js/pagination.js"&gt;&lt;/script&gt;</code>.'],
    ['2. Place', 'Put the component last in the section or list. Add no padding below it.'], ['3. Key', 'Pick a key (for example <code>products</code>). The ids <code>{key}-pagination-count</code>, <code>{key}-pagination-bar</code> and <code>pagination-{key}</code> must exist.'],
    ['4. Update', 'After loading items call <code>updatePagination(key, visible, total)</code>.']])
c_comp = '<h2 class="ds-h2">Pagination</h2>' + desc('Copy the markup you need.') + '<div id="recipes"></div>'
c_api = '<h2 class="ds-h2">API</h2><h3 class="ds-h3 ds-group">Classes</h3>' + table(['Class', 'Use'], [['<code>pagination</code>', 'The component: 190px, centered, space above.'], ['<code>pagination__info</code>', 'Counter and bar.'], ['<code>pagination__count</code>', 'The counter text.'], ['<code>pagination__progress</code>', 'The 2px track.'], ['<code>pagination__progress-bar</code>', 'The fill, width set by script.']]) + \
    '<h3 class="ds-h3 ds-group">Function</h3>' + table(['Function', 'What it does'], [['<code>updatePagination(key, visible, total)</code>', 'Sets the counter, the fill width and disables the button when <code>visible &gt;= total</code>.']]) + \
    '<h3 class="ds-h3 ds-group">Things to know</h3>' + bullets(['No padding or margin below the component: the section provides it.', 'The button is always <code>btn btn--secondary btn--md</code>.', 'When everything is shown the button is disabled, never hidden or removed.'])
c_css = '<h2 class="ds-h2">CSS / Tailwind</h2>' + desc('The component is one CSS file and one JS file, shared by every page. Link them, never copy them. The code below is read from the files the page links, so it is always what you see.') + \
    code_box('css-code', 'CSS (components/css/pagination.css)') + '<div style="height:24px"></div>' + code_box('js-code', 'JS (components/js/pagination.js)')
code = [('basic-usage', c_basic), ('pagination', c_comp), ('api', c_api), ('css-tailwind', c_css, False)]

# ---------------------------------------------------------------- scripts
PAG = r'''
  function pag(key, visible, total, host, btnCls) {
    var d = document.createElement('div'); d.className = 'pagination'; d.id = 'pagination-' + key; var dis = visible >= total;
    d.innerHTML = '<div class="pagination__info"><p class="pagination__count" aria-live="polite">Showing <span id="' + key + '-pagination-count">' + visible + '</span> of ' + total + ' reviews</p><div class="pagination__progress" aria-hidden="true"><div class="pagination__progress-bar" id="' + key + '-pagination-bar" style="width:' + (visible / total * 100) + '%"></div></div></div><button type="button" class="btn ' + (btnCls || 'btn--secondary') + ' btn--md"' + (dis ? ' disabled' : '') + '><span class="btn__label">Show more reviews</span></button>';
    host.appendChild(d); return d;
  }
'''

JS_EX = PAG + r'''
  var TOTAL = 22, shown = 10, STEP = 10;
  function list() {
    var l = clear($('#pg-list'));
    for (var i = 1; i <= shown; i++) { var r = document.createElement('div'); r.className = 'pg-item'; r.textContent = 'Review ' + i + ': “Good fit, strong seams.”'; l.appendChild(r); }
  }
  function renderPg() {
    var total = TOTAL, step = STEP; shown = Math.min(shown, total);
    list(); var d = pag('pg', shown, total, clear($('#pg-host')));
    $('button', d).addEventListener('click', function () { shown = Math.min(total, shown + step); list(); updatePagination('pg', shown, total); });
    $('#pg-code').textContent = '<div class="pagination" id="pagination-pg">\n  <div class="pagination__info">\n    <p class="pagination__count" aria-live="polite">Showing <span id="pg-pagination-count">' + shown + '</span> of ' + total + ' reviews</p>\n    <div class="pagination__progress" aria-hidden="true">\n      <div class="pagination__progress-bar" id="pg-pagination-bar" style="width:' + (shown / total * 100).toFixed(4) + '%"></div>\n    </div>\n  </div>\n  <button type="button" class="btn btn--secondary btn--md"'+(shown >= total ? ' disabled' : '')+'><span class="btn__label">Show more reviews</span></button>\n</div>\n\n<script>updatePagination(\'pg\', visible, ' + total + ');<\/script>';
  }
  $('#pg-reset').addEventListener('click', function () { shown = 10; renderPg(); });

  /* Snapshots */
  var sn = clear($('#v-snap'));
  [['s1', 2, 6], ['s2', 4, 6], ['s3', 5, 6]].forEach(function (s) { var c = document.createElement('div'); c.className = 'pg-snap'; var w = document.createElement('div'); w.style.width = '100%'; c.appendChild(w); var l = document.createElement('span'); l.textContent = s[1] + ' of ' + s[2]; c.appendChild(l); sn.appendChild(c); pag(s[0], s[1], s[2], w); });

  /* Usage figures */
  function items(host, n) { for (var i = 1; i <= n; i++) { var r = document.createElement('div'); r.className = 'pg-item'; r.style.width = '100%'; r.textContent = 'Review ' + i; host.appendChild(r); } }
  items($('#fig-do1'), 2); items($('#fig-dont1'), 2); pag('d1', 6, 6, $('#fig-do1'));
  var left = document.createElement('p'); left.className = 'pg-ghost'; left.innerHTML = 'Showing 6 of 6 reviews'; var bar = document.createElement('div'); bar.style.cssText = 'width:190px;max-width:100%;height:2px;background:var(--color-surface-100)'; $('#fig-dont1').appendChild(left); $('#fig-dont1').appendChild(bar);
  pag('d2', 4, 6, $('#fig-do2')); pag('d3', 4, 6, $('#fig-dont2'), 'btn--primary');

  /* Anatomy */
  var art = $('#pg-anat-art'); pag('an', 2, 6, art);
  function rng(el) { return function () { var r = document.createRange(); r.selectNodeContents(el); return r.getBoundingClientRect(); }; }
  DK.callouts($('#pg-anat'), [
    { n: 1, box: rng($('.pagination__count', art)), side: 'left', len: 48, at: 'edge' },
    { n: 2, el: $('.pagination__progress', art), side: 'right', len: 48 },
    { n: 3, el: $('button', art), side: 'left', len: 48 }
  ]);
  renderPg();
'''

JS_SPEC = r'''
  DK.tokenTable($('#tok-table tbody'), [
    ['Counter text', 'Text of the counter', 'surface-60'], ['Bar track', 'The 2px track', 'surface-10'], ['Bar fill', 'The visible share', 'surface-100'],
    ['Space above (xs)', 'Margin top below 640px', 'dimension-spacing-space-24'], ['Space above (sm)', 'Margin top 640–768px', 'dimension-spacing-space-32'], ['Space above (md and up)', 'Margin top from 769px', 'dimension-spacing-space-40']]);
'''

JS_CODE = r'''
  DK.recipes($('#recipes'), [
    ['Component (link button.css, pagination.css and pagination.js)', '<div class="pagination" id="pagination-products">\n  <div class="pagination__info">\n    <p class="pagination__count" aria-live="polite">Showing <span id="products-pagination-count">4</span> of 6 reviews</p>\n    <div class="pagination__progress" aria-hidden="true">\n      <div class="pagination__progress-bar" id="products-pagination-bar" style="width:66.6667%"></div>\n    </div>\n  </div>\n  <button type="button" class="btn btn--secondary btn--md" onclick="showMore(\'products\', this)">\n    <span class="btn__label">Show more reviews</span>\n  </button>\n</div>'],
    ['Update after loading', 'function showMore(key, btn) {\n  // 1. add the next items to the list, 2. then:\n  updatePagination(key, visibleCount, totalCount);\n  // 3. when everything is shown, the button becomes disabled:\n  //    move focus to the first new item first\n}']
  ]);
  DK.printCss($('#css-code'), 'pagination', [[/^\n+/, '']]);
  fetch('../../components/js/pagination.js', { cache: 'no-cache' }).then(function (r) { return r.text(); }).then(function (t) { $('#js-code').textContent = t; });
'''

C = dict(
    slug=SLUG, title='Pagination', eyebrow='Components · Status and navigation',
    lead='Pagination here is a <strong>“load more” pattern</strong>: a counter, a thin progress bar and a button that adds more items to a list without a page load.',
    lead_ex='Every example on this page is the real component, not a picture. Figma: ' + fig_link(FIGMA, 'Pagination') + '.',
    lead_spec='The tokens, the spacing per breakpoint, the measurements and the requirements. Values come from the live token package and from Figma: ' + fig_link(FIGMA, 'Pagination') + '.',
    lead_code='How to add pagination to a list. The files are <code>components/css/pagination.css</code> and <code>components/js/pagination.js</code>.',
    select_menu=False, css=['pagination'], body_js=['../../components/js/pagination.js'],
    style=STYLE, ex=ex, spec=spec, code=code, js_ex=JS_EX, js_spec=JS_SPEC, js_code=JS_CODE)

if __name__ == '__main__':
    emit(C)
