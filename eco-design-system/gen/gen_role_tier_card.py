from build import *

SLUG = 'role-tier-card'
BADGE = '<span class="badge-basic badge-basic--warning badge-basic--weak" title="A test built on the comparison pages. It is not an official component, and no Figma component exists.">Experiment</span>'

STYLE = r'''    .pg-note { font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-tertiary); }
    .pg-matrix td { vertical-align: middle; padding-top: 16px; padding-bottom: 16px; }
    #pg-host .role-tier-pair { grid-template-columns: minmax(0, 1fr); }   /* demo: these stages are narrower than the window, so the pair stacks (the component only knows the window width) */
    .rt-callout.ds-fig__stage.ds-callout { padding: 72px 72px; }
    .rt-callout .ds-callout__art { width: 100%; max-width: 640px; }'''

playground = '<h2 class="ds-h2">Playground</h2>' + desc('Choose the link state, the number of features and the names of the two cards, and the pair and its code update. Below 640px each card stacks its features under the text; from 769px the two cards sit next to each other. Resize the window to see both.') + \
    '<div class="ds-playground"><div class="ds-stage" id="pg-stage"><div id="pg-host" style="width:100%"></div></div><div class="ds-controls">' + \
    btn_group('pg-l-st', 'Link', 'data-pg="state"', [('enabled', 'Enabled', True), ('hover', 'Hover', False)]) + \
    btn_group('pg-l-f', 'Features per card', 'data-pg="n"', [('3', '3', False), ('4', '4', True)]) + \
    '<div class="ds-field form-field"><label class="form-label form-label--sm" for="pg-n1">Base card name</label><div class="input-wrap"><div class="input-box input-box--sm"><input class="form-input" type="text" id="pg-n1" value="Standard" placeholder="Base card name" /></div></div></div>' + \
    '<div class="ds-field form-field"><label class="form-label form-label--sm" for="pg-n2">Dark card name</label><div class="input-wrap"><div class="input-box input-box--sm"><input class="form-input" type="text" id="pg-n2" value="Administrator" placeholder="Dark card name" /></div></div></div>' + \
    '</div></div><h3 class="ds-h3">Markup for this selection</h3>' + code_box('pg-code', 'HTML')

overview = '<h2 class="ds-h2">Overview</h2>' + desc('A role tier card pair introduces <strong>two tiers of one category</strong> side by side, for example Standard and Administrator, and links on to the full comparison table further down the page.') + \
    desc('It is an <strong>experiment</strong>, built on the comparison pages (<code>feature-comparison-roles.html</code>, <code>e-handelspartner.html</code>). There is no Figma component, so the values are the project’s own. A pair has a light card for the base tier and a dark card for the extended or administrative tier. Each card has a badge, a name, a description, a link and three or four feature strips.') + \
    three_pages(SLUG, 'a role tier card pair', 'the values: tokens, type, sizes, measurements and requirements', 'how to add one to a page')

usage = '<h2 class="ds-h2">Usage</h2><h3 class="ds-h3 ds-group">When to use</h3>' + desc('Use a card pair above a comparison table, to help the reader pick the right tier before the detail. Use it to:') + \
    bullets(['Introduce two tiers of one category side by side', 'Show three or four features that really set the tier apart', 'Send the reader to the matching tab of the comparison table']) + \
    '<h3 class="ds-h3 ds-group">When not to use</h3><h3 class="ds-h3">More than two tiers</h3>' + desc('A pair holds two cards, a light one and a dark one. For three or more tiers, go straight to the comparison table.') + \
    fig_pair('<div id="fig-do" style="width:100%"></div>', 'Do ground the feature strips in rows that exist in the table.', '<div id="fig-dont" style="width:100%"></div>', 'Do not invent features that the table does not show.') + \
    '<h3 class="ds-h3">One prominent link</h3>' + desc('A single graphical link is a ' + link_large('tile-link.html', 'Tile link') + ', not a card pair.') + \
    '<h3 class="ds-h3 ds-group">Quick reference</h3>' + \
    table(['You need…', 'Use'], [['to introduce two tiers of one category and link to the full table', 'Role tier card pair'], ['to compare many roles in detail', 'A comparison table (the product table component is planned; the table of these pages is the <a class="inline-link inline-link--small" href="../foundations/docs-table.html">Docs table</a>)'], ['one prominent link', '<a class="inline-link inline-link--small" href="tile-link.html">Tile link</a>']]) + \
    rules(['Use the dark card for the extended or administrative tier.', 'Ground the feature strips in the table below.', 'Switch the tab before scrolling.', 'Keep sharp corners and ECO colors.'],
          ['Invent features that are not in the table.', 'Use pill-shaped buttons.', 'Scroll without the header offset.', 'Use it for more than two tiers.'])

anatomy = '<h2 class="ds-h2">Anatomy</h2><h3 class="ds-h3 ds-group">Role tier card</h3>' + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout rt-callout" id="rt-anat" role="img" aria-label="Anatomy of a role tier card: 1 icon and badge, 2 name, 3 description, 4 link, 5 feature strips, 6 card"><div class="ds-callout__art" id="an-host"></div></div></figure></div>' + \
    ol_parts([('Icon and badge', 'A 24px Material Symbols icon and a Basic badge that names the tier.'), ('Name', 'The tier name, Title Large, weight 600.'), ('Description', 'One or two sentences, Body Medium.'), ('Link', 'An action link with a downward arrow. It switches the table tab and scrolls to the table.'), ('Feature strips', 'Three or four rows that set the tier apart. Body Small, centered.'), ('Card', 'A 1px border, sharp corners and a surface. The dark card has its own colors.')]) + \
    desc('The info block (1 to 4) and the feature strips (5) sit side by side from 640px and stack below it.')

variants = '<h2 class="ds-h2">Variants</h2>' + desc('Pairs stack one under another, one per category. The order of the pairs follows the order of the tabs in the comparison table below them.') + \
    '<h3 class="ds-h3 ds-group">Stacked pairs</h3>' + fig_one('<div id="v-pairs" style="width:100%"></div>') + \
    '<h3 class="ds-h3 ds-group">Quick links</h3>' + desc('A compact row with one small System-style link per role, above the cards. It uses the same <code>goToCompareView()</code> as the card links.') + \
    fig_one('<div class="role-quicklinks" style="margin:0" id="v-quick"></div>')

states = '<h2 class="ds-h2">States</h2>' + desc('The only interactive part is the link. It has no underline when enabled; the label is underlined on hover and the color changes. Hover is forced on this page; in your code it comes from <code>:hover</code>.') + \
    '<div class="ds-table-wrap"><table class="ds-table pg-matrix" id="matrix"><thead><tr><th scope="col">State</th><th scope="col">Base card</th><th scope="col">Dark card</th></tr></thead><tbody></tbody></table></div>'

sizes = '<h2 class="ds-h2">Sizes</h2>' + desc('A card has no sizes. It fills half of the row from 769px and the whole row below it, and its parts keep their size. The values are under ' + sec_link(SLUG, 'sizes', 'Sizes') + ' in Specifications.')

layout = '<h2 class="ds-h2">Layout &amp; Appearance</h2><h3 class="ds-h3 ds-group">Layout</h3>' + desc('The two cards sit in one column below 769px and in two columns from 769px. Inside a card the text block takes 55% and the feature strips 45% from 640px; below 640px the strips sit under the text.') + \
    '<h3 class="ds-h3 ds-group">Appearance</h3>' + desc('The light card uses the white surface and primary text. The dark card uses <code>surface-100</code> with the accent color on the name and the icon. Token names and values are under ' + sec_link(SLUG, 'design-tokens', 'Design Tokens') + ' in Specifications.')

behavior = '<h2 class="ds-h2">Behavior</h2>' + desc('The link is the only interactive part. It switches the active tab of the comparison table <strong>before</strong> it scrolls, by calling the table’s own <code>setCompareView()</code>, and it scrolls to the table with the header offset.') + \
    '<h3 class="ds-h3 ds-group">Breakpoints</h3>' + desc('The cards change at 640px (strips beside or under the text) and at 769px (one or two cards per row, larger type and padding). Tablet (640 to 768px) shows the strips beside the text, but one card per row.') + \
    note('The Specifications page has no Breakpoint control: the card changes at 640 and 769px, and the control only switches at 769px. Resize the window instead.')

access = '<h2 class="ds-h2">Accessibility</h2>' + desc('All requirements are listed under ' + sec_link(SLUG, 'accessibility-requirements', 'Accessibility Requirements') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Keyboard support</h3>' + desc('The link is reached with Tab and opened with Enter. It shows a 2px focus ring on keyboard focus.') + \
    '<h3 class="ds-h3 ds-group">Screen reader support</h3>' + desc('The icon is decorative (<code>aria-hidden="true"</code>). The link label names the tier it compares, for example “Compare Administrator in the table”.')

related = '<h2 class="ds-h2">Related</h2><ul class="ds-bullets"><li><strong>' + link_large('../foundations/docs-table.html', 'Docs table') + '</strong>. The table these pages use; a product table component is planned.</li><li><strong>' + link_large('tile-link.html', 'Tile link') + '</strong>. One prominent graphical link.</li><li><strong>' + link_large('action-link.html', 'Action link') + '</strong>. The type the card link is based on.</li><li><strong>' + link_large('badge-basic.html', 'Basic badge') + '</strong>. The badge in the card.</li></ul>'

ex = [('playground', playground), ('overview', overview), ('usage', usage), ('anatomy', anatomy), ('variants', variants), ('states', states), ('sizes', sizes), ('layout', layout), ('behavior', behavior), ('accessibility', access), ('related', related)]

# ---------------------------------------------------------------- Specifications
st_tok = '<h2 class="ds-h2">Design Tokens</h2>' + desc('Resolved from the live token package.') + \
    '<div class="ds-table-wrap"><table class="ds-table" id="tok-table"><thead><tr><th scope="col">Card</th><th scope="col">Part</th><th scope="col">Token</th><th scope="col">Value</th></tr></thead><tbody></tbody></table></div>' + \
    '<h3 class="ds-h3 ds-group">Colors</h3>' + table(['Part', 'Base card', 'Dark card (<code>.role-tier--dark</code>)'], [
        ['Background', '<code>surface-raised-primary</code>', '<code>surface-100</code>'], ['Border', '<code>border-primary</code>', '<code>surface-90</code>'], ['Title and icon', '<code>text-primary</code>', '<code>accent-default</code>'],
        ['Description', '<code>text-secondary</code>', '<code>text-secondary-inverted</code>'], ['Link', '<code>text-action-primary</code>, hover <code>-hover</code>', '<code>text-action-primary-inverted</code>, hover <code>-hover</code>'],
        ['Feature strips', '<code>surface-05</code>, lines <code>border-primary</code>', '<code>surface-90</code>, lines white at 12%']]) + \
    note('<strong>Open point:</strong> the line between the feature strips on the dark card is <code>rgba(255, 255, 255, 0.12)</code>. There is no token for white at 12%, so it is written out with a comment in the CSS.')

st_typo = '<h2 class="ds-h2">Typography</h2>' + table(['Element', 'Token', 'Mobile', 'Desktop (769px+)'], [
    ['Name', '<code>title-lg</code>, weight 600', '20/24, 0', '24/28, 0'], ['Description', '<code>body-md</code>', '16/22, 0.32px', '17/24, 0.32px'],
    ['Link', 'Action link, Medium, Bold (600), 24px icon, gap 6px', '16/24, 0.32px', '17/24, 0.32px'], ['Feature', '<code>body-sm</code>', '14/20, 0.36px', '14/20, 0.36px'],
    ['Quick link', 'System, small', '14/14, 0.56px, uppercase, 600', 'The same']])

st_sizes = '<h2 class="ds-h2">Sizes</h2>' + table(['Part', 'Value'], [
    ['Pair', '1 column below 769px, 2 columns from 769px, gap 24px; stacked pairs 24px (xs) and 32px (md and up) apart'], ['Card', 'Column below 640px, row from 640px; 1px border, sharp corners'],
    ['Info block', '24px padding (32px from 769px), gap 8px, 55% of the width'], ['Feature strip', 'Min height 56px, 16px padding, text centered; 45% of the width'], ['Quick link', 'Height 32px, padding 6px 12px, gap 6px, icon 16px']]) + \
    note('A card has one size. The parts change with the breakpoint, as the table shows.')

st_meas = '<h2 class="ds-h2">Measurements</h2><h3 class="ds-h3 ds-group">Dimensions</h3>' + table(['Attribute', 'Mobile (below 769px)', 'Desktop (769px+)'], [
    ['Info block padding', '24px', '32px'], ['Gap inside the info block', '8px', '8px'], ['Gap between badge row and name', '12px (8px gap + 4px margin)', '12px'], ['Link top margin', '8px', '8px'],
    ['Feature strip', 'min 56px high, 16px padding', 'The same'], ['Card border', '1px', '1px'], ['Gap between the two cards', '24px', '24px'], ['Gap between stacked pairs', '24px', '32px']]) + \
    note('The card changes at 640px and at 769px, and the Breakpoint control only switches at 769px, so there is no measurement figure and no Breakpoint control. The values are read from the component.') + \
    '<h3 class="ds-h3 ds-group">Spacing</h3>' + desc('The values as spacing tokens.') + table(['Part', 'Value'], [['Info block padding, mobile', '<code>space-24</code>'], ['Info block padding, desktop', '<code>space-32</code>'], ['Gap in the info block, link top margin', '<code>space-8</code>'], ['Feature strip padding', '<code>space-16</code>'], ['Gap, icon to link label', '6px (no spacing token)']])

st_states = '<h2 class="ds-h2">States</h2>' + table(['State', 'Link', 'Rest of the card'], [['Enabled', 'No underline. Base: <code>text-action-primary</code>. Dark: <code>text-action-primary-inverted</code>.', 'Static.'], ['Hover', 'Label underlined. Color moves to the <code>-hover</code> token of its card.', 'Static.'], ['Focus', '2px ring, <code>border-focus</code>, 2px outside (keyboard only).', 'Static.']]) + \
    desc('The card itself has no hover, active or disabled state.')

st_struct = '<h2 class="ds-h2">Structure</h2><h3 class="ds-h3 ds-group">Elements</h3>' + table(['Element', 'Class', 'Notes'], [
    ['Pair', '<code>role-tier-pair</code>', 'A grid of two cards. Several pairs stack.'], ['Card', '<code>role-tier</code>, <code>role-tier--dark</code>', 'Light by default; <code>--dark</code> for the extended tier.'],
    ['Info block', '<code>role-tier__info</code>', 'Holds the badge row, name, description and link.'], ['Badge row', '<code>role-tier__badge-row</code>', '<code>role-tier__icon</code> and a <code>badge-basic</code>.'],
    ['Name, description', '<code>role-tier__name</code>, <code>role-tier__desc</code>', 'Paragraphs.'], ['Link', '<code>role-tier__link</code>', '<code>role-tier__link-label</code> and <code>role-tier__link-icon</code>.'],
    ['Feature strips', '<code>role-tier__features</code>, <code>role-tier__feature</code>', 'Three or four rows.'], ['Quick links', '<code>role-quicklinks</code>, <code>role-quicklink</code>', 'A row of small links above the cards.']]) + \
    '<h3 class="ds-h3 ds-group">Width</h3>' + desc('A pair fills its container. Two cards share the row equally from 769px.')

st_behavior = '<h2 class="ds-h2">Behavior</h2>' + table(['Topic', 'Rule'], [
    ['Link', 'Switches the active tab in the table <strong>before</strong> scrolling, by calling the table’s own <code>setCompareView()</code>. Call <code>event.preventDefault()</code> so the anchor does not snap mid-scroll.'],
    ['Scroll offset', 'Scroll to the section with the <code>--header-top-h</code> offset, never a plain <code>scrollIntoView()</code>.'], ['Feature strips', 'Three or four rows taken from rows that really exist in the comparison table and are specific to that role.'],
    ['Order', 'The pairs follow the order of the tabs.'], ['Motion', 'The link color changes with <code>duration-fast-3</code> and <code>ease-standard</code>.']]) + \
    note('<strong>Open points:</strong> no Figma component. The card is built for the comparison pages, and the link needs their table script.')

st_access = '<h2 class="ds-h2">Accessibility Requirements</h2>' + table(['Topic', 'Requirement'], [
    ['Link', 'A real <code>&lt;a&gt;</code> with a label that names the tier. The click handler calls <code>preventDefault()</code> and moves focus or scroll to the table.'], ['Icons', 'The tier icon and the arrow are decorative: <code>aria-hidden="true"</code>.'],
    ['Focus', 'Keyboard focus shows a 2px ring (<code>border-focus</code>) 2px outside the link.'], ['Contrast', 'Text on the dark card uses the inverted tokens (<code>text-secondary-inverted</code> on <code>surface-100</code>).'], ['Order', 'The reading order is badge, name, description, link, then the features.']])

spec = [('design-tokens', st_tok), ('typography', st_typo), ('sizes', st_sizes), ('measurements', st_meas), ('states', st_states), ('structure', st_struct), ('behavior', st_behavior), ('accessibility-requirements', st_access)]

# ---------------------------------------------------------------- Code
c_basic = '<h2 class="ds-h2">Basic Usage</h2>' + desc('Link the shared stylesheets once per page. Never copy the rules into a page.') + table(['Step', 'What to do'], [
    ['1. Link', '<code>&lt;link rel="stylesheet" href="/components/css/role-tier.css"&gt;</code> and <code>badge.css</code>. The page also needs the Material Symbols font.'], ['2. Pair', 'One <code>.role-tier-pair</code> with two <code>.role-tier</code> cards. Add <code>role-tier--dark</code> to the second.'],
    ['3. Content', 'Badge row, name, description, link and three or four <code>.role-tier__feature</code> rows, taken from the comparison table.'], ['4. Link logic', 'Add <code>goToCompareView()</code> (below) to the page and call it from each link.']])
c_pair = '<h2 class="ds-h2">Role tier card</h2>' + desc('Copy the markup you need.') + '<div id="recipes"></div>'
c_api = '<h2 class="ds-h2">API</h2><h3 class="ds-h3 ds-group">Classes</h3>' + table(['Class', 'Use'], [['<code>role-tier-pair</code>', 'The grid that holds two cards.'], ['<code>role-tier</code>', 'A card. The base tier.'], ['<code>role-tier--dark</code>', 'The extended or administrative tier.'], ['<code>role-tier__link</code>', 'The action link. <code>data-state="hover"</code> forces hover (docs only).'], ['<code>role-quicklinks</code>, <code>role-quicklink</code>', 'A row of small links above the cards.']]) + \
    '<h3 class="ds-h3 ds-group">Things to know</h3>' + bullets(['The card changes at 640px and at 769px.', 'The link needs the table’s own script (<code>setCompareView()</code>). Without it, only the scroll works.', 'The dark card’s feature line is the one value without a token (white at 12%).'])
c_css = '<h2 class="ds-h2">CSS / Tailwind</h2>' + desc('The component is one CSS file, shared by every page. Link it, never copy it. The CSS below is read from the file the page links, so it is always what you see.') + code_box('css-code', 'CSS (components/css/role-tier.css)')
code = [('basic-usage', c_basic), ('role-tier-card', c_pair), ('api', c_api), ('css-tailwind', c_css, False)]

# ---------------------------------------------------------------- scripts
CARD_JS = old_js('role-tier-card', '  function card(o)', '  var st = {')

JS_EX = CARD_JS + r'''
  function noJump(sel) { $$(sel + ' a').forEach(function (x) { x.addEventListener('click', function (e) { e.preventDefault(); }); }); }
  var st = { state: 'enabled', n: '4' };
  function renderPg() {
    var o = { n: +st.n, hover: st.state === 'hover' };
    var a = Object.assign({}, BASE, { name: $('#pg-n1').value }), b = Object.assign({}, DARK, { name: $('#pg-n2').value });
    $('#pg-host').innerHTML = pair(a, b, o); noJump('#pg-host');
    $('#pg-code').textContent = (o.hover ? '<!-- hover is forced here for preview; in production it comes from :hover -->\n' : '') + '<div class="role-tier-pair">\n  <div class="role-tier">\n    <div class="role-tier__info">\n      <div class="role-tier__badge-row">\n        <span class="role-tier__icon" aria-hidden="true">person</span>\n        <span class="badge-basic badge-basic--neutral-grey badge-basic--weaker">Standard access</span>\n      </div>\n      <p class="role-tier__name">' + esc(a.name) + '</p>\n      <p class="role-tier__desc">…</p>\n      <a href="#compare" class="role-tier__link" onclick="goToCompareView(event, \'roles\')">\n        <span class="role-tier__link-label">Compare ' + esc(a.name) + ' in the table</span>\n        <span class="role-tier__link-icon" aria-hidden="true">arrow_downward</span>\n      </a>\n    </div>\n    <div class="role-tier__features">\n      <div class="role-tier__feature">Place orders</div>\n      …\n    </div>\n  </div>\n  <div class="role-tier role-tier--dark">…same structure…</div>\n</div>';
  }
  DK.wire(st, renderPg); $('#pg-n1').addEventListener('input', renderPg); $('#pg-n2').addEventListener('input', renderPg);

  /* Usage figures */
  $('#fig-do').innerHTML = card(Object.assign({}, BASE, { name: 'Standard', n: 3 })); noJump('#fig-do');
  $('#fig-dont').innerHTML = card(Object.assign({}, BASE, { name: 'Standard', n: 3, features: ['Everything in the world', 'Free coffee forever', 'A personal chauffeur'] })); noJump('#fig-dont');

  /* Anatomy */
  $('#an-host').innerHTML = card(Object.assign({}, BASE, { name: 'Standard', n: 3 })); noJump('#an-host');
  var A = $('#an-host');
  DK.callouts($('#rt-anat'), [
    { n: 1, el: $('.role-tier__badge-row', A), side: 'top', len: 64, at: 'center' },
    { n: 2, el: $('.role-tier__name', A), side: 'left', len: 64 },
    { n: 3, el: $('.role-tier__desc', A), side: 'left', len: 64 },
    { n: 4, el: $('.role-tier__link', A), side: 'left', len: 64 },
    { n: 5, el: $('.role-tier__features', A), side: 'right', len: 40 },
    { n: 6, el: $('.role-tier', A), side: 'bottom', len: 40 }
  ]);

  /* Variants */
  $('#v-pairs').innerHTML = pair(BASE, DARK, { name: 'x' }).replace('>x<', '>Standard<').replace('>x<', '>Administrator<') +
    pair({ icon: 'apartment', badge: 'Company', name: 'Company standard', desc: 'For companies that buy through one shared account.', link: 'Compare in the table', features: ['Shared order history', 'Company prices', 'Invoice payment', 'Delivery addresses'] },
         { dark: true, icon: 'domain_add', badge: 'Special terms', name: 'Company special', desc: 'For companies with an agreement and their own price list.', link: 'Compare in the table', features: ['Agreement prices', 'Own price list', 'Credit limit', 'Dedicated contact'] }, {});
  noJump('#v-pairs');
  $('#v-quick').innerHTML = ['Standard', 'Administrator', 'Company standard'].map(function (n) { return '<a href="#" class="role-quicklink"><span>' + n + '</span><span class="role-quicklink__icon" aria-hidden="true">arrow_downward</span></a>'; }).join('');
  noJump('#v-quick');

  /* States */
  var tb = $('#matrix tbody');
  [['Enabled', false], ['Hover', true]].forEach(function (r) {
    var tr = document.createElement('tr'), th = document.createElement('th'); th.scope = 'row'; th.textContent = r[0]; tr.appendChild(th);
    [BASE, DARK].forEach(function (c) { var td = document.createElement('td'); td.style.textAlign = 'left'; td.innerHTML = card(Object.assign({}, c, { name: c.dark ? 'Administrator' : 'Standard', n: 0, hover: r[1] })); tr.appendChild(td); });
    tb.appendChild(tr);
  });
  noJump('#matrix');
  renderPg();
'''

JS_SPEC = r'''
  DK.tokenTable($('#tok-table tbody'), [['Base', 'Background', 'surface-raised-primary'], ['Base', 'Border', 'border-primary'], ['Base', 'Name and icon', 'text-primary'], ['Base', 'Description', 'text-secondary'], ['Base', 'Feature background', 'surface-05'],
    ['Dark', 'Background', 'surface-100'], ['Dark', 'Border', 'surface-90'], ['Dark', 'Name and icon', 'accent-default'], ['Dark', 'Description', 'text-secondary-inverted'], ['Dark', 'Feature background', 'surface-90'], ['Dark', 'Feature text', 'text-primary-inverted'],
    ['Both · hover', 'Link', 'text-action-primary-hover'], ['Dark · hover', 'Link', 'text-action-primary-inverted-hover'], ['Both · focus', 'Ring', 'border-focus']]);
'''

JS_CODE = r'''
  DK.recipes($('#recipes'), [
    ['Card pair (link role-tier.css, badge.css and the Material Symbols font)', '<div class="role-tier-pair">\n  <div class="role-tier">\n    <div class="role-tier__info">\n      <div class="role-tier__badge-row">\n        <span class="role-tier__icon" aria-hidden="true">person</span>\n        <span class="badge-basic badge-basic--neutral-grey badge-basic--weaker">Standard access</span>\n      </div>\n      <p class="role-tier__name">Standard</p>\n      <p class="role-tier__desc">Standard users can shop and follow their own orders.</p>\n      <a href="#compare" class="role-tier__link" onclick="goToCompareView(event, \'roles\')">\n        <span class="role-tier__link-label">Compare Standard in the table</span>\n        <span class="role-tier__link-icon" aria-hidden="true">arrow_downward</span>\n      </a>\n    </div>\n    <div class="role-tier__features">\n      <div class="role-tier__feature">Place orders</div>\n      <div class="role-tier__feature">Quick order</div>\n      <div class="role-tier__feature">Own favourite lists</div>\n    </div>\n  </div>\n  <div class="role-tier role-tier--dark">… same structure …</div>\n</div>'],
    ['Link logic (uses the table’s own setCompareView)', "function goToCompareView(event, view) {\n  if (event) event.preventDefault();\n  var btn = document.querySelector('.compare-view-btn[data-view=\"' + view + '\"]');\n  if (btn) setCompareView(view, btn);\n  var target = document.getElementById('compare');\n  var headerH = parseFloat(getComputedStyle(document.documentElement).getPropertyValue('--header-top-h')) || 0;\n  window.scrollTo({ top: target.getBoundingClientRect().top + window.scrollY - headerH, behavior: 'smooth' });\n}"],
    ['Quick links', '<div class="role-quicklinks">\n  <a href="#compare" class="role-quicklink" onclick="goToCompareView(event, \'roles\')">\n    <span>Standard</span><span class="role-quicklink__icon" aria-hidden="true">arrow_downward</span>\n  </a>\n</div>']]);
  DK.printCss($('#css-code'), 'role-tier');
'''

C = dict(
    slug=SLUG, title='Role tier card', eyebrow='Drafts · Cards', eyebrow_extra=BADGE,
    lead='A role tier card pair introduces <strong>two tiers of one category</strong> side by side, for example Standard and Administrator, and links on to the full comparison table.',
    lead_ex='Every example on this page is the real component, not a picture. Specification: <code>.claude/skills/eco-role-tier-card/SKILL.md</code>. There is no Figma component.',
    lead_spec='Tokens, type, sizes, measurements and requirements. The values come from the live token package and from the comparison pages; there is no Figma component.',
    lead_code='How to add a card pair to a page. The file is <code>components/css/role-tier.css</code>.',
    select_menu=False,
    css=['role-tier'], style=STYLE, ex=ex, spec=spec, code=code, js_ex=JS_EX, js_spec=JS_SPEC, js_code=JS_CODE)

if __name__ == '__main__':
    emit(C)
