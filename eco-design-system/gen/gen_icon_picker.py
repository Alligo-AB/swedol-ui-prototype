from build import *

SLUG = 'icon-picker'
BADGE = '<span class="badge-basic badge-basic--warning badge-basic--weak" title="No Figma component exists. The pattern was designed in the repo (first used on the banner page).">Not verified with Figma</span>'

STYLE = r'''    .pg-note { font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-tertiary); }
    .pg-col { display: flex; flex-direction: column; align-items: flex-start; gap: 16px; }
    .pg-cap { font-size: 12px; line-height: 12px; letter-spacing: 0.48px; text-transform: uppercase; color: var(--color-text-tertiary); font-weight: 600; }
    .ip-measure { display: block; width: 320px; }   /* demo: a fixed width for the static panel */
    .ip-demo { position: static; width: 320px; max-width: 100%; box-shadow: var(--shadow-elevation-b-80); }   /* inline copy of the open panel; set again inline because icon-picker.js adds its own rules after this block */
    .ds-callout__art { width: 100%; max-width: 320px; padding-right: 0; }'''

playground = '<h2 class="ds-h2">Playground</h2>' + desc('A text field that holds a Material Symbols name. The picker opens on top of the field. The preview below is only for this page: the picker itself adds nothing to a page that shows the icon.') + \
    '<div class="ds-playground"><div class="ds-stage ds-stage--center" id="pg-stage"><div id="pg-host" class="pg-col" style="align-items:center"><span class="ms" id="pg-prev" aria-hidden="true" style="font-size:64px;color:var(--color-icon-primary)">local_shipping</span><span class="pg-cap" id="pg-name">local_shipping</span></div></div><div class="ds-controls">' + \
    '<div class="ds-field form-field"><label class="form-label form-label--sm" for="pg-icon">Icon name</label><div class="input-wrap"><div class="input-box input-box--sm"><input class="form-input" type="text" id="pg-icon" value="local_shipping" placeholder="Icon name" data-icon-picker autocomplete="off" /></div></div></div>' + \
    '<p class="pg-note" style="margin:0">Click or Tab into the field. Search all icons, or pick from Recent and Popular.</p></div></div><h3 class="ds-h3">Markup for this selection</h3>' + code_box('pg-code', 'HTML')

overview = '<h2 class="ds-h2">Overview</h2>' + desc('An icon picker is a text field that holds a Material Symbols name. A panel opens on top of it with instant search over all icons, Recent and Popular.') + \
    desc('It is for back-office and docs forms where a person chooses the icon of a banner, a notification, a menu item, a tile or a category. The picker stores the name, not a rendering. It has no Figma component: it was designed in the repo.') + \
    three_pages(SLUG, 'the icon picker', 'the values: tokens, dimensions, states and requirements', 'how to add it to a field')

usage = '<h2 class="ds-h2">Usage</h2><h3 class="ds-h3 ds-group">When to use</h3>' + desc('Use the icon picker for every field that holds a Material Symbols name. Use it to:') + \
    bullets(['Choose the icon of a banner, a notification, a menu item, a tile or a category', 'Choose the icon of a button in a prototype or a back-office form', 'Choose an icon in a docs playground']) + \
    '<h3 class="ds-h3 ds-group">When not to use</h3><h3 class="ds-h3">To only show an icon</h3>' + desc('To show an icon, use a <code>material-symbols-outlined</code> span. The picker is for choosing the name.') + \
    '<h3 class="ds-h3">For a few fixed options</h3>' + desc('To choose between a few fixed options use <code>eco-select</code> or <code>eco-radio</code>.') + \
    fig_pair('<div style="width:100%;max-width:280px"><div class="form-field"><label class="form-label form-label--sm" for="fig-ip-do">Icon</label><div class="input-wrap"><div class="input-box input-box--sm"><input class="form-input" type="text" id="fig-ip-do" value="local_shipping" placeholder="Icon name" data-icon-picker autocomplete="off" /></div></div></div></div>', 'Do use the icon picker for a field that holds an icon name. Click the field.', '<div style="width:100%;max-width:280px"><div class="form-field"><label class="form-label form-label--sm" for="fig-ip-dont">Icon name</label><div class="input-wrap"><div class="input-box input-box--sm"><input class="form-input" type="text" id="fig-ip-dont" placeholder="Type the exact name, for example local_shipping" /></div></div></div></div>', 'Do not use a plain text input for icon names.') + \
    '<h3 class="ds-h3 ds-group">Quick reference</h3>' + \
    table(['The field…', 'Use'], [['holds a Material Symbols name (banner, notification, menu item, tile, category)', 'Icon picker'], ['only shows an icon', 'A <code>material-symbols-outlined</code> span'], ['chooses between a few fixed options', '<code>eco-select</code> or <code>eco-radio</code>']]) + \
    rules(['Use it for every field that holds an icon name.', 'Store the name, not a rendering.', 'Fall back to the default icon when the name is empty or wrong.', 'Run the server from the repo root (root-absolute script path).'], ['Use a plain text input for icon names.', 'Build a second picker or fork the look on one page.', 'Add the data file by hand.', 'Ship the 1.4 MB data file to production as is.'])

anatomy = '<h2 class="ds-h2">Anatomy</h2><h3 class="ds-h3 ds-group">Open panel</h3>' + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout" id="ip-anat" role="img" aria-label="Anatomy of the open icon picker panel: 1 panel, 2 search box, 3 group label, 4 icon cell, 5 selected icon"><div class="ds-callout__art"><div id="a-host"></div></div></div><figcaption class="ds-fig__cap">The panel is drawn here as a static copy. In use it opens on top of the field.</figcaption></figure></div>' + \
    ol_parts([('Panel', 'Opens on top of the field: same width, 12px padding, 12px between the parts. White, with the <code>elevation-b-80</code> shadow.'), ('Search box', '42px high, first and focused. Instant search over all icons.'), ('Group label', '<strong>Recent</strong> (the last 8 picks) and <strong>Popular</strong> (the top 60), or <strong>Results (n)</strong> while searching.'), ('Icon cell', '40px, with the icon at 24px. The name is the <code>aria-label</code> and the title.'), ('Selected icon', 'The icon that is in the field has a <code>border-selected</code> frame.')]) + \
    '<h3 class="ds-h3 ds-group">Field</h3>' + desc('The field under the panel is an <a class="inline-link inline-link--large inline-link--secondary" href="input.html">Input</a> with <code>data-icon-picker</code>. Inside an Input field the picker uses the <code>.input-wrap</code> as its anchor, so the panel covers the whole field.')

variants = '<h2 class="ds-h2">Variants</h2>' + note('Not applicable. The icon picker is one pattern with no variants: it looks and behaves the same on every page, and a page must not fork it. Its field is an Input; see <a class="inline-link inline-link--medium inline-link--secondary" href="input.html">Input</a> for the field sizes.')

layout = '<h2 class="ds-h2">Layout &amp; Appearance</h2><h3 class="ds-h3 ds-group">Placement</h3>' + desc('The panel opens on top of the field, not under it, so it never runs off the bottom of the window. It has the same width as the field, and sits 12px outside it on each side. Make the field at least as wide as the six icon cells you want to see in a row (about 280px).') + \
    '<h3 class="ds-h3 ds-group">Appearance</h3>' + desc('Colors, shadow and spacing in the picker are tokens only. Icons in the grid are Outlined, Fill 0, Weight 300, Grade 0, 24px: the same as icons in the components. Token names and values are under ' + sec_link(SLUG, 'design-tokens', 'Design Tokens') + ' in Specifications.')

behavior = '<h2 class="ds-h2">Behavior</h2><p class="ds-desc">The same behavior on every page.</p><h3 class="ds-h3 ds-group">Opening</h3>' + desc('Click or Tab into the field. A panel opens <strong>on top of the field</strong> (same width, 12px padding). The search box comes first and has focus. The focus ring on the search box is hidden when the panel was opened with the mouse, and shown when opened with Tab.') + \
    '<h3 class="ds-h3 ds-group">Searching</h3>' + desc('With the search box empty, the panel shows <strong>Recent</strong> (the last 8 picks, kept in <code>localStorage</code> and shared by all pages) and <strong>Popular</strong> (the top 60). Typing gives an instant search over all icons. Ranked: name starts with, then a name word starts with, then a tag word starts with; each group by popularity. Up to 60 are shown; the header says <code>Results (n)</code>. No match: “No icons match …”.') + \
    '<h3 class="ds-h3 ds-group">Picking and closing</h3>' + desc('A click on an icon puts the name in the field, fires an <code>input</code> event, closes the panel and returns focus to the field. Esc or a click outside closes the panel without changing the value.')

access = '<h2 class="ds-h2">Accessibility</h2>' + desc('All requirements are listed under ' + sec_link(SLUG, 'accessibility-requirements', 'Accessibility Requirements') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Keyboard support</h3>' + desc('Tab into the field opens the panel with the search box focused. Tab moves through the icons. Enter or Space picks one. Esc closes the panel and keeps the value.') + \
    '<h3 class="ds-h3 ds-group">Screen reader support</h3>' + desc('The field needs a visible label. The search box has an <code>aria-label</code>, and every icon is a button named by its icon name, with <code>aria-pressed</code> on the one in the field. The glyphs are <code>aria-hidden</code>.')

related = '<h2 class="ds-h2">Related</h2><ul class="ds-bullets"><li><strong>' + link_large('input.html', 'Input') + '</strong>. The field the picker is attached to.</li><li><strong>' + link_large('select.html', 'Select') + '</strong>. A few fixed options.</li><li><strong>' + link_large('radio.html', 'Radio button') + '</strong>. A few fixed options, all visible.</li><li><strong>' + link_large('menu.html', 'Menu') + '</strong>. Another surface that opens from a field.</li></ul>'

references = '<h2 class="ds-h2">References</h2>' + refs([
    ('https://fonts.google.com/icons', 'Google Fonts: Material Symbols', 'The icon set and its names.'),
    ('https://www.w3.org/WAI/ARIA/apg/patterns/combobox/', 'WAI-ARIA Authoring Practices: Combobox', 'A related pattern for a field with a popup.'),
    ('https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html', 'WCAG 2.2: Name, Role, Value', 'Success criterion 4.1.2.')])

ex = [('playground', playground), ('overview', overview), ('usage', usage), ('anatomy', anatomy), ('layout', layout), ('behavior', behavior), ('accessibility', access), ('related', related), ('references', references)]

# ---------------------------------------------------------------- Specifications
st_tok = '<h2 class="ds-h2">Design Tokens</h2>' + desc('Resolved from the live token package.') + \
    '<div class="ds-table-wrap"><table class="ds-table" id="tok-table"><thead><tr><th scope="col">State</th><th scope="col">Part</th><th scope="col">Token</th><th scope="col">Value</th></tr></thead><tbody></tbody></table></div>' + \
    note('<strong>Open points:</strong> no Figma component. The dimensions were decided in code. Colors, shadow and spacing in the picker are tokens only.')

st_sizes = '<h2 class="ds-h2">Sizes</h2>' + table(['Part', 'Value'], [['Panel', 'Top of the field, same width, 12px padding'], ['Search box', '42px high'], ['Icon cell', '40px'], ['Grid height', '176px (it scrolls)'], ['Results', 'Up to 60']]) + note('The same on every breakpoint.')


def mfig():
    return ('<div class="measure__item"><span class="measure__name">1 · Panel</span><div class="measure__obj"><span class="ip-measure" id="ip-meas"></span>'
            '<i class="measure__pad measure__pad--t"></i><i class="measure__pad measure__pad--b"></i><i class="measure__pad measure__pad--l"></i><i class="measure__pad measure__pad--r"></i>'
            '<b class="measure__dim measure__dim--v measure__dim--t"><span></span></b><b class="measure__dim measure__dim--v measure__dim--b"><span></span></b><b class="measure__dim measure__dim--h measure__dim--l"><span></span></b><b class="measure__dim measure__dim--h measure__dim--r"><span></span></b></div></div>')


st_meas = '<h2 class="ds-h2">Measurements</h2><h3 class="ds-h3 ds-group">Dimensions</h3>' + desc('Padding of the open panel. The shaded area is the 12px padding; the lines show its value. The panel is a static copy here.') + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-fig__stage--flush" style="padding:0;min-height:0"><div class="measure" role="img" aria-label="Padding of the icon picker panel: 12 on every side">' + mfig() + '</div></div><figcaption class="ds-fig__cap">The panel at true size (1:1). The numbers are read from the component.</figcaption></figure></div>' + \
    table(['Attribute', 'Value'], [['Panel padding', '12px on every side'], ['Gap between the parts', '12px'], ['Search box', '42px high, full width, 1px border'], ['Icon cell', '40px high; the grid fits as many 40px columns as the width allows'], ['Gap between cells', '4px'], ['Grid', 'Up to 176px high, then it scrolls'], ['Panel position', 'Top and sides 12px outside the field (<code>top: -12px; left: -12px; right: -12px</code>)'], ['Corners', 'Square']]) + \
    '<h3 class="ds-h3 ds-group">Spacing</h3>' + desc('The same padding and gaps as spacing tokens.') + table(['Part', 'Value'], [['Panel padding and gap between the parts', '<code>space-12</code>'], ['Gap between icon cells', '<code>space-4</code>'], ['Search box padding', '<code>space-8</code> above and below, <code>space-12</code> left and right']])

st_states = '<h2 class="ds-h2">States</h2>' + desc('The field is an Input and has the Input states. The panel and its icons have the states below. Hover and focus come from the browser and are described here.') + \
    '<div class="ds-table-wrap"><table class="ds-table pg-matrix" id="matrix"><thead><tr><th scope="col">State</th><th scope="col">Part</th><th scope="col">Look</th></tr></thead><tbody></tbody></table></div>'

st_typo = '<h2 class="ds-h2">Typography</h2>' + table(['Part', 'Size / line height', 'Letter spacing', 'Weight'], [['Search text', '16/24', 'inherited', 'Regular'], ['Group label', '12/18', '0.24px', '600'], ['Icon', '24px Material Symbols, Outlined, Fill 0, Weight 300, Grade 0', '—', '—'], ['No match message', '14/20', 'inherited', 'Regular']]) + note('The sizes are set in the script’s CSS in pixels. <strong>Open point:</strong> bind them to type tokens if the picker moves into a design token pass.')

st_struct = '<h2 class="ds-h2">Structure</h2><h3 class="ds-h3 ds-group">Elements</h3>' + table(['Element', 'Class', 'Notes'], [['Anchor', '<code>ip-wrap</code>', 'Added to the <code>.input-wrap</code> of the field, or to a wrapper made around a bare input.'], ['Panel', '<code>ip-panel</code>', 'Hidden until the field opens. <code>ip-mouse</code> when opened with the mouse.'], ['Search box', '<code>ip-search</code>', 'A text input with <code>aria-label="Search icons"</code>.'], ['Group label', '<code>ip-label</code>', 'Recent, Popular or Results.'], ['Grid and cell', '<code>ip-grid</code>, <code>ip-btn</code>', '<code>aria-pressed</code> on the picked icon.'], ['No match', '<code>ip-empty</code>', 'The message under Results.']]) + \
    '<h3 class="ds-h3 ds-group">Types</h3>' + desc('There is one type.') + '<h3 class="ds-h3 ds-group">Width</h3>' + desc('The panel has the width of the field.') + \
    '<h3 class="ds-h3 ds-group">Data and loading</h3>' + table(['Topic', 'Detail'], [['Script', '<code>components/icon-picker/icon-picker.js</code>. It loads <code>icon-picker-data.js</code> (all names and search tags, sorted by popularity) from its own folder 0.5 s after page load. Never add the data file by hand.'], ['Data size', '1.4 MB, a copy of the Google Fonts Material Symbols metadata (August 2026). Fine for a prototype; serve a smaller list or search on the server in production.'], ['Refresh', 'Download <code>https://fonts.google.com/metadata/icons?key=material_symbols&amp;incomplete=true</code> and rewrite the file as <code>window.ECO_ICONS=[[name,"tags"],…]</code> sorted by <code>popularity</code>.'], ['Font', 'The page needs the Material Symbols Outlined font (in both page templates).']])

st_motion = '<h2 class="ds-h2">Motion</h2>' + note('None. The panel opens and closes at once, with no transition and no animation.')

st_behavior = '<h2 class="ds-h2">Behavior</h2>' + table(['Moment', 'What happens'], [
    ['Click or Tab into the field', 'A panel opens <strong>on top of the field</strong> (same width, 12px padding). The search box comes first and has focus.'], ['Search box empty', '<strong>Recent</strong> (the last 8 picks, kept in <code>localStorage</code> and shared by all pages) and <strong>Popular</strong> (the top 60).'],
    ['Typing', 'Instant search over all icons. Ranked: name starts with, then a name word starts with, then a tag word starts with; each group by popularity. Up to 60 shown; the header says <code>Results (n)</code>. No match: “No icons match …”.'], ['Click an icon', 'The name goes into the field, an <code>input</code> event fires, the panel closes and focus returns to the field.'],
    ['Esc, click outside', 'Closes without changing the value.'], ['Focus ring on the search box', 'Hidden when the panel was opened with the mouse, shown when opened with Tab.']])

st_access = '<h2 class="ds-h2">Accessibility Requirements</h2>' + table(['Topic', 'Requirement'], [
    ['Field', 'A visible <code>label</code> with <code>for</code> and <code>id</code>, as for every Input.'], ['Search box', '<code>aria-label="Search icons"</code>.'], ['Icons', 'Real <code>button</code> elements named by the icon name (<code>aria-label</code> and <code>title</code>), with <code>aria-pressed</code> on the picked one. The glyph is <code>aria-hidden="true"</code>.'], ['Focus', '2px ring <code>border-focus</code> on the search box and the icons on keyboard focus (WCAG 2.4.7, 1.4.11).'], ['Dismissal', 'Esc closes the panel and keeps the value.'], ['Open point', 'The panel is not announced as a dialog or a combobox listbox. <strong>Open point:</strong> add the roles if the picker is used outside back-office forms.']])

spec = [('design-tokens', st_tok), ('sizes', st_sizes), ('measurements', st_meas), ('states', st_states), ('typography', st_typo), ('structure', st_struct), ('motion', st_motion), ('behavior', st_behavior), ('accessibility-requirements', st_access)]

# ---------------------------------------------------------------- Code
c_basic = '<h2 class="ds-h2">Basic Usage</h2>' + desc('One script tag. Style the input with <code>eco-input</code>: inside an Input field the picker anchors on the <code>.input-wrap</code>, so the panel covers the whole field. Never copy the picker into a page.') + table(['Step', 'What to do'], [
    ['1. Link', '<code>&lt;script src="/components/icon-picker/icon-picker.js"&gt;&lt;/script&gt;</code> (from docs pages: <code>../../components/icon-picker/icon-picker.js</code>) and <code>/components/css/input.css</code>.'], ['2. Markup', 'An Input field with <code>data-icon-picker</code> on the <code>input</code>.'], ['3. Font', 'The page needs the Material Symbols Outlined font (already in both templates).'], ['4. React', 'Listen for the <code>input</code> event to re-render a preview or save the value.'], ['5. Server', 'Run the server from the repo root (<code>npx serve .</code>) for the root-absolute script path.']])
c_ip = '<h2 class="ds-h2">Icon picker</h2><div id="recipes"></div>'
c_api = '<h2 class="ds-h2">API</h2><h3 class="ds-h3 ds-group">Attributes and events</h3>' + table(['Name', 'Use'], [['<code>data-icon-picker</code>', 'On the text input that holds the name. The script attaches to every such input on load.'], ['<code>input</code> event', 'Fired on the input when an icon is picked. The value is the Material Symbols name.'], ['<code>localStorage["eco-icon-recent"]</code>', 'The last 8 picks, shared by all pages.']]) + \
    '<h3 class="ds-h3 ds-group">Things to know</h3>' + bullets(['The picker stores a name, not a rendering. Validate or fall back where the icon is shown (empty is the component’s default icon).', 'Never fork the look or behavior on one page. Change <code>components/icon-picker/icon-picker.js</code> instead; every page gets it.', 'The icon data loads from <code>icon-picker-data.js</code> next to the script, 0.5 s after load. Never add that file by hand.', 'Without an eco-input field the script wraps the bare input in <code>.ip-wrap</code> and makes it 100% wide.'])
c_css = '<h2 class="ds-h2">CSS / Tailwind</h2>' + desc('The picker has no CSS file: its styles are injected by the script, with tokens only. The script is shared by every page. Link it, never copy it.') + code_box('js-code', 'JS (components/icon-picker/icon-picker.js)')
code = [('basic-usage', c_basic), ('icon-picker', c_ip), ('api', c_api), ('css-tailwind', c_css, False)]

# ---------------------------------------------------------------- scripts
PANEL_JS = r'''
  /* A static, non-interactive copy of the open panel, built from the picker's own classes (the script injects their CSS) */
  function icoBtn(n, on) { return '<button type="button" class="ip-btn" tabindex="-1" aria-pressed="' + on + '" aria-label="' + n + '"><span class="material-symbols-outlined" aria-hidden="true">' + n + '</span></button>'; }
  function staticPanel(extra) {
    var rec = ['local_shipping', 'store', 'info', 'star'], pop = ['home', 'search', 'settings', 'check_circle', 'close', 'menu', 'person', 'favorite'];
    return '<div class="ip-panel' + (extra || '') + '" style="position:static;display:flex;width:100%;max-width:320px" inert><input class="ip-search" type="text" placeholder="Search icons" aria-label="Search icons" tabindex="-1" /><div style="display:flex;flex-direction:column;gap:var(--dimension-spacing-space-12,12px)">' +
      '<div class="ip-label">Recent</div><div class="ip-grid">' + rec.map(function (n, i) { return icoBtn(n, i === 0); }).join('') + '</div><div class="ip-label">Popular</div><div class="ip-grid">' + pop.map(function (n) { return icoBtn(n, false); }).join('') + '</div></div></div>';
  }
  function txt(el) { return function () { var r = document.createRange(); r.selectNodeContents(el); return r.getBoundingClientRect(); }; }
'''

JS_EX = PANEL_JS + r'''
  var inp = $('#pg-icon');
  function renderPg() { var v = inp.value.trim() || 'local_shipping'; $('#pg-prev').textContent = v; $('#pg-name').textContent = v; $('#pg-code').textContent = '<label for="icon">Icon</label>\n<input id="icon" type="text" data-icon-picker value="' + esc(v) + '" placeholder="Icon name">\n<script src="/components/icon-picker/icon-picker.js"><\/script>'; }
  inp.addEventListener('input', renderPg);

  /* Anatomy */
  var ah = clear($('#a-host')); ah.insertAdjacentHTML('beforeend', staticPanel(''));
  var panel = $('.ip-panel', ah);
  DK.callouts($('#ip-anat'), [
    { n: 1, el: panel, side: 'bottom', len: 44 },
    { n: 2, el: $('.ip-search', ah), side: 'top', len: 44, at: 'center' },
    { n: 3, box: txt($('.ip-label', ah)), side: 'right', len: 64 },
    { n: 4, el: $$('.ip-btn', ah)[3], side: 'right', len: 40 },
    { n: 5, el: $('.ip-btn', ah), side: 'left', len: 44 }
  ]);
  renderPg();
'''

JS_SPEC = PANEL_JS + r'''
  $('#ip-meas').insertAdjacentHTML('beforeend', staticPanel(' measure__subject'));
  var tb = $('#matrix tbody');
  [['Field, closed', 'Input', 'The Input field with the icon name. States as in <a class="inline-link inline-link--small" href="input-specifications.html#states">Input</a>.', null],
   ['Panel, open', 'Panel', 'White <code>surface-raised-primary</code>, <code>elevation-b-80</code> shadow, on top of the field.', null],
   ['Icon cell, enabled', 'Icon', 'Transparent, 1px transparent border, <code>icon-primary</code> glyph.', [false]],
   ['Icon cell, hover', 'Icon', 'Fill <code>surface-navigation-hover</code>. Hover an icon to see it.', null],
   ['Icon cell, picked', 'Icon', '1px <code>border-selected</code> frame (<code>aria-pressed="true"</code>).', [true]],
   ['Icon cell, keyboard focus', 'Icon', '2px <code>border-focus</code> ring, drawn inside the cell. Press Tab to see it.', null],
   ['Search box, focus', 'Search', 'Border <code>border-selected</code>; the ring (2px, 2px offset) shows when the panel was opened with Tab, not with the mouse.', null],
   ['No match', 'Results', '“No icons match …” in <code>body-sm</code>.', null]].forEach(function (r) {
    var tr = document.createElement('tr'), th = document.createElement('th'); th.scope = 'row'; th.textContent = r[0]; tr.appendChild(th);
    var p = document.createElement('td'); p.innerHTML = r[1]; tr.appendChild(p);
    var d = document.createElement('td'); d.innerHTML = r[2]; if (r[3]) { var w = document.createElement('span'); w.style.cssText = 'display:inline-block;width:40px;margin-right:12px;vertical-align:middle'; w.innerHTML = icoBtn('local_shipping', r[3][0]); d.insertBefore(w, d.firstChild); } tr.appendChild(d); tb.appendChild(tr);
  });
  DK.tokenTable($('#tok-table tbody'), [['Panel', 'Fill', 'surface-raised-primary'], ['Panel', 'Shadow', 'shadow-elevation-b-80'], ['Search box', 'Fill', 'background-primary'], ['Search box', 'Border', 'border-input-default'], ['Search box', 'Border, focus', 'border-selected'], ['Search box', 'Ring', 'border-focus'], ['Icon', 'Glyph', 'icon-primary'], ['Icon', 'Hover fill', 'surface-navigation-hover'], ['Icon', 'Picked frame', 'border-selected'], ['Icon', 'Focus ring', 'border-focus']]);
'''

JS_CODE = r'''
  DK.recipes($('#recipes'), [['Field with the picker', '<link rel="stylesheet" href="/components/css/input.css">\n\n<div class="form-field">\n  <label class="form-label" for="icon">Icon</label>\n  <div class="input-wrap">\n    <div class="input-box">\n      <input class="form-input" id="icon" type="text" data-icon-picker placeholder="Icon name" autocomplete="off" />\n    </div>\n  </div>\n</div>\n<script src="/components/icon-picker/icon-picker.js"><\/script>'],
    ['Read the choice', "document.getElementById('icon').addEventListener('input', function (e) {\n  preview.textContent = e.target.value;   // the Material Symbols name\n});"]]);
  fetch('../../components/icon-picker/icon-picker.js', { cache: 'no-cache' }).then(function (r) { return r.text(); }).then(function (t) { $('#js-code').textContent = t; });
'''

C = dict(
    slug=SLUG, title='Icon picker', eyebrow='Components · Form', eyebrow_extra=BADGE,
    lead='An icon picker is a text field that holds a <strong>Material Symbols name</strong>. A panel opens on top of it with instant search over all icons, Recent and Popular.',
    lead_ex='Every example on this page is the real component, not a picture. There is no Figma component: the pattern was designed in the repo.',
    lead_spec='Tokens, dimensions, states and requirements. There is no Figma component: values come from the live token package and the specification skill.',
    lead_code='How to add the icon picker to a field. The file is <code>components/icon-picker/icon-picker.js</code>.',
    css=[], body_js=['../../components/icon-picker/icon-picker.js'], select_menu=False, style=STYLE, ex=ex, spec=spec, code=code, js_ex=JS_EX, js_spec=JS_SPEC, js_code=JS_CODE)

if __name__ == '__main__':
    emit(C)
