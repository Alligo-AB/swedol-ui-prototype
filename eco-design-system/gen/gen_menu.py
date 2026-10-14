from build import *

FIGMA = 'https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=%s'
SLUG = 'menu'

STYLE = r'''    .pg-note { font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-tertiary); }
    .pg-col { width: 100%; max-width: 408px; }
    .pg-grid { display: grid; gap: 32px 24px; grid-template-columns: minmax(0, 1fr); width: 100%; }
    @media (min-width: 769px) { .pg-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
    .pg-cap { display: block; margin-bottom: 12px; font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-tertiary); }
    .pg-matrix td { vertical-align: top; padding-top: 16px; padding-bottom: 16px; min-width: 260px; }
    .mn-fig { width: 100%; max-width: 320px; }
    .mn-measure { display: block; width: 280px; }   /* demo: a fixed width, so the padding strips have a row to sit on */
    .ds-callout__art { padding-right: 24px; }'''

playground = '<h2 class="ds-h2">Playground</h2>' + desc('Choose a breakpoint, size, divider and selection type and the menu and its code update. The menu is live: hover a row, click to choose.') + \
    '<div class="ds-playground"><div class="ds-stage ds-stage--center"><div class="pg-col" id="pg-host"></div></div><div class="ds-controls">' + \
    bp_field('pg-l-bp') + btn_group('pg-l-size', 'Size', 'data-pg="size"', [('lg', 'Large', True), ('sm', 'Small', False)]) + \
    btn_group('pg-l-div', 'Divider', 'data-pg="divider"', [('inset', 'Middle-inset', True), ('full', 'Full-width', False), ('none', 'No', False)]) + \
    btn_group('pg-l-var', 'Selection', 'data-pg="variant"', [('select', 'Select', True), ('multi', 'Multi Select', False)]) + \
    btn_group('pg-l-dis', 'Row 3', 'data-pg="disabled"', [('no', 'Enabled', True), ('yes', 'Disabled', False)]) + \
    '<div class="ds-field form-field"><label class="form-label form-label--sm" for="pg-rows">Rows (1–20)</label><div class="input-wrap"><div class="input-box input-box--sm"><input class="form-input" type="number" id="pg-rows" min="1" max="20" value="5" placeholder="Rows" /></div></div></div>' + \
    '</div></div><h3 class="ds-h3">Markup for this selection</h3>' + code_box('pg-code', 'HTML')

overview = '<h2 class="ds-h2">Overview</h2>' + desc('A menu is the <strong>list surface</strong> that opens from a button or action (Dropdown menu) or from a Select field (Exposed dropdown menu). The two differ only in the element that opens the surface, so they share one component.') + \
    desc('Menu has two sizes (Large and Small), three divider styles (middle-inset, full-width and none) and two selection types (Select and Multi Select). Row content (leading element, label, trailing element) comes from the ' + link_large('list-item.html', 'List Item') + ' component; the menu draws the row, the divider, the hover and the check.') + \
    three_pages(SLUG, 'a menu', 'the values: tokens, sizes, measurements, states and requirements', 'how to add one to a page')

fig_labels_do = '<div class="mn-fig" id="fig-lab-do"></div>'
usage = '<h2 class="ds-h2">Usage</h2><h3 class="ds-h3 ds-group">When to use</h3>' + desc('Use a menu to show a temporary list of choices or actions. Use it:') + \
    bullets(['As a <strong>Dropdown menu</strong>, opened by a button or another control, to list actions or choices', 'As an <strong>Exposed dropdown menu</strong>, opened by a Select field, to list the values the field can have']) + \
    '<h3 class="ds-h3 ds-group">When not to use</h3><h3 class="ds-h3">Keep each label on one line</h3>' + desc('A row is one line high. A long label wraps and breaks the rhythm of the list, so shorten it or choose another component.') + \
    fig_pair(fig_labels_do, 'Do keep every label short enough for one line.', '<div class="mn-fig" id="fig-lab-dont"></div>', 'Do not write labels that wrap onto a second line.') + \
    '<h3 class="ds-h3">Keep the list short</h3>' + desc('The menu shows up to 14 rows and then scrolls. A long list is hard to scan, so use it only when the user needs the full set.') + \
    fig_pair('<div class="mn-fig" id="fig-len-do"></div>', 'Do keep the list to the choices the user needs.', '<div class="mn-fig" id="fig-len-dont"></div>', 'Do not put a long list in a menu without a clear need: it scrolls.') + \
    '<h3 class="ds-h3">For page navigation</h3>' + desc('A menu is not the header menu or a drawer. Use those for navigation between pages.') + \
    '<h3 class="ds-h3">For two to five visible options</h3>' + desc('When the options are few and should always be visible, use <code>eco-radio</code> (one choice) or <code>eco-checkbox</code> (several).') + \
    '<h3 class="ds-h3 ds-group">Quick reference</h3>' + \
    table(['The user…', 'Use'], [['picks one value in a form field', '<code>eco-select</code> (the closed field), opening a Menu (Exposed dropdown)'], ['opens a list of actions or choices from a button', 'Menu (Dropdown menu)'], ['picks one of two to five visible options', '<code>eco-radio</code>'], ['picks any number of visible options', '<code>eco-checkbox</code>']]) + \
    rules(['Keep labels short so they fit one line.', 'Use Multi Select only when more than one choice is valid.', 'Let the opener set the menu width.', 'Set <code>aria-selected</code> to match the check.', 'Keep a disabled row in the list (with <code>aria-disabled</code>) when the user should know it exists.'],
          ['Use a menu for page navigation.', 'Put more than about 14 rows in without a clear need: the list scrolls.', 'Mix divider styles in one menu.', 'Hardcode colors or row heights: use the tokens and size classes.'])

anatomy = '<h2 class="ds-h2">Anatomy</h2><h3 class="ds-h3 ds-group">Menu</h3>' + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout" id="mn-anat" role="img" aria-label="Anatomy of a menu: 1 surface, 2 row, 3 label, 4 check icon, 5 divider"><div class="ds-callout__art mn-fig" id="mn-anat-art"></div></div></figure></div>' + \
    ol_parts([('Surface', 'A white box with the <code>elevation-b-80</code> shadow. It is as wide as the opener.'), ('Row', 'One option. 48px high on desktop and 40px on mobile (Large), with 16px side padding.'), ('Label', '<code>body-md</code> (Large) or <code>body-sm</code> (Small), one line.'),
              ('Check icon', 'A <code>check_circle</code> on the chosen row. Multi Select shows a circle on every row. 24px on desktop Large, 20px otherwise.'), ('Divider', 'A 1px line inside the row height. Middle-inset keeps 16px on each side.')]) + \
    desc('A scrollbar appears only when the list has more than 14 rows.')

variants = '<h2 class="ds-h2">Variants</h2>' + desc('Three divider styles and two selection types. Use the Breakpoint toggle to preview Desktop (769px and up) and Mobile (below 769px). Sizes are under Sizes below.') + \
    toolbar([('vb-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force')]) + \
    '<h3 class="ds-h3 ds-group">Dividers</h3>' + desc('<strong>Middle-inset</strong> keeps 16px on each side and is the default. <strong>Full-width</strong> runs edge to edge. <strong>No</strong> removes the line.') + fig_one('<div class="pg-grid" id="v-dividers"></div>') + \
    '<h3 class="ds-h3 ds-group">Selection</h3>' + desc('<strong>Select</strong> chooses one row and marks it with a check. <strong>Multi Select</strong> shows a circle on every row and a check on the chosen ones.') + fig_one('<div class="pg-grid" id="v-select"></div>') + \
    '<h3 class="ds-h3 ds-group">Scrolling</h3>' + desc('The menu shows up to 14 rows. With more, the list scrolls and a 12px scrollbar appears.') + fig_one('<div class="pg-grid" id="v-scroll"></div>')

sizes = '<h2 class="ds-h2">Sizes</h2>' + desc('<strong>Large</strong> is the default for forms and the Select field. <strong>Small</strong> is for compact surfaces. Both change at 769px: Large rows are 48px on desktop and 40px on mobile, Small rows 40px and 32px. The values are under ' + sec_link(SLUG, 'sizes', 'Sizes') + ' in Specifications.') + \
    toolbar([('sz-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force')]) + fig_one('<div class="pg-grid" id="v-sizes"></div>')

layout = '<h2 class="ds-h2">Layout &amp; Appearance</h2><h3 class="ds-h3 ds-group">Alignment</h3>' + desc('Labels are left-aligned and the check icon sits at the right edge of the row. Use one divider style in a menu.') + \
    '<h3 class="ds-h3 ds-group">Placement</h3>' + desc('The menu opens directly under its opener. The opener owns the position and the open and close behavior; this page shows the surface only.') + \
    '<h3 class="ds-h3 ds-group">Width</h3>' + desc('The menu fills the width the opener gives it. For a Select field it is as wide as the field.') + \
    '<h3 class="ds-h3 ds-group">Appearance</h3>' + desc('A white surface with the <code>elevation-b-80</code> shadow and square corners. Token names and values are under ' + sec_link(SLUG, 'design-tokens', 'Design Tokens') + ' in Specifications.')

behavior = '<h2 class="ds-h2">Behavior</h2><h3 class="ds-h3 ds-group">Hover</h3>' + desc('The row fill changes to <code>surface-navigation-hover</code>. In Multi Select an unselected row previews the check.') + \
    '<h3 class="ds-h3 ds-group">Focus</h3>' + desc('Rows are focusable. A 2px ring shows inside the row on keyboard focus. Arrow keys move between rows and skip a disabled row.') + \
    '<h3 class="ds-h3 ds-group">Selection</h3>' + desc('A click, Enter or Space chooses the row. Select replaces the choice; Multi Select toggles it.') + \
    '<h3 class="ds-h3 ds-group">Disabled row</h3>' + desc('A disabled row has <code>text-disabled</code> text and icon, no hover fill, and is not focusable. A click or Enter does nothing.') + \
    '<h3 class="ds-h3 ds-group">Dismissal</h3>' + desc('The opener closes the menu and returns focus to itself on Escape. All states are listed under ' + sec_link(SLUG, 'states', 'States') + ' in Specifications.')

access = '<h2 class="ds-h2">Accessibility</h2>' + desc('All requirements are listed under ' + sec_link(SLUG, 'accessibility-requirements', 'Accessibility Requirements') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Keyboard support</h3>' + desc('Tab reaches the rows. Up and Down arrows move between them, Enter or Space chooses, and Escape closes the menu through the opener.') + \
    '<h3 class="ds-h3 ds-group">Screen reader support</h3>' + desc('The list is a <code>listbox</code> and each row an <code>option</code> with <code>aria-selected</code>. Multi Select sets <code>aria-multiselectable="true"</code>. A disabled row has <code>aria-disabled="true"</code>.')

related = '<h2 class="ds-h2">Related</h2><ul class="ds-bullets"><li><strong>' + link_large('select.html', 'Select') + '</strong>. The closed field that opens a menu.</li><li><strong>' + link_large('list-item.html', 'List Item') + '</strong>. The content of one row.</li><li><strong>' + link_large('divider.html', 'Divider') + '</strong>. A standalone line between groups.</li><li><strong>' + link_large('radio.html', 'Radio button') + '</strong>. Two to five visible options.</li><li><strong>' + link_large('checkbox.html', 'Checkbox') + '</strong>. Any number of visible options.</li></ul>'

references = '<h2 class="ds-h2">References</h2>' + refs([
    ('https://www.w3.org/WAI/ARIA/apg/patterns/listbox/', 'WAI-ARIA Authoring Practices: Listbox', 'Keyboard and role requirements.'),
    ('https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html', 'WCAG 2.2: Focus Visible', 'Success criterion 2.4.7.'),
    ('https://www.nngroup.com/articles/drop-down-menus/', 'Nielsen Norman Group: Drop-Down Menus', 'When a menu helps and when it hides options.'),
    ('https://fluent2.microsoft.design/components/web/react/core/menu/usage', 'Fluent 2: Menu', 'Microsoft.'),
    ('https://m3.material.io/components/menus/overview', 'Material Design 3: Menus', 'Google.'),
    ('https://carbondesignsystem.com/components/menu/usage/', 'Carbon Design System: Menu', 'IBM.')])

ex = [('playground', playground), ('overview', overview), ('usage', usage), ('anatomy', anatomy), ('variants', variants), ('sizes', sizes), ('layout', layout), ('behavior', behavior), ('accessibility', access), ('related', related), ('references', references)]

# ---------------------------------------------------------------- Specifications
st_tok = '<h2 class="ds-h2">Design Tokens</h2>' + desc('Resolved from the live token package.') + \
    '<div class="ds-table-wrap"><table class="ds-table" id="tok-table"><thead><tr><th scope="col">State</th><th scope="col">Part</th><th scope="col">Token</th><th scope="col">Value</th></tr></thead><tbody></tbody></table></div>'

st_sizes = '<h2 class="ds-h2">Sizes</h2>' + table(['Breakpoint · size', 'Row height', 'Max height (14 rows)', 'Check icon', 'Text'], [
    ['Desktop · Large', '48px', '672px', '24px', '<code>body-md</code> 17/24, 0.32px'], ['Desktop · Small', '40px', '560px', '20px', '<code>body-sm</code> 14/20, 0.36px'],
    ['Mobile · Large', '40px', '560px', '20px', '<code>body-md</code> 16/22, 0.32px'], ['Mobile · Small', '32px', '448px', '20px', '<code>body-sm</code> 14/20, 0.36px']]) + \
    note('<code>sm</code> (640 to 768px) looks like mobile. The scrollbar is 12px wide.')


def mfig(n, name, cls):
    return ('<div class="measure__item"><span class="measure__name">%d · %s</span><div class="measure__obj"><span class="mn-measure"><div class="menu%s"><ul class="menu__items" role="presentation"><li class="menu__item measure__subject"><span class="menu__item-label">Label text</span></li></ul></div></span>'
            '<i class="measure__pad measure__pad--t"></i><i class="measure__pad measure__pad--b"></i><i class="measure__pad measure__pad--l"></i><i class="measure__pad measure__pad--r"></i>'
            '<b class="measure__dim measure__dim--v measure__dim--t"><span></span></b><b class="measure__dim measure__dim--v measure__dim--b"><span></span></b><b class="measure__dim measure__dim--h measure__dim--l"><span></span></b><b class="measure__dim measure__dim--h measure__dim--r"><span></span></b></div></div>') % (n, name, cls)


st_meas = '<h2 class="ds-h2">Measurements</h2><h3 class="ds-h3 ds-group">Dimensions</h3>' + desc('Padding of one row at each size. The shaded areas are the 16px padding to the left and right; the row height comes from the size, not from padding. The numbers are read from the component.') + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-fig__stage--flush" style="padding:0;min-height:0"><div class="measure" role="img" aria-label="Padding of a menu row: left and right, per size">' + mfig(1, 'Large', '') + mfig(2, 'Small', ' menu--sm') + '</div></div><figcaption class="ds-fig__cap">A row at true size (1:1).</figcaption></figure></div>' + \
    table(['Attribute', 'Large', 'Small'], [['Row height, Desktop', '48px', '40px'], ['Row height, Mobile', '40px', '32px'], ['Padding left and right', '<td colspan="2">16px</td>'], ['Padding top and bottom', '<td colspan="2">0 (the row has a minimum height)</td>'], ['Gap, label to icon', '<td colspan="2">8px</td>'], ['Divider', '<td colspan="2">1px, inside the row height</td>'], ['Divider inset, middle-inset', '<td colspan="2">16px on each side</td>'], ['Focus ring', '<td colspan="2">2px, inside the row</td>']]) + \
    '<h3 class="ds-h3 ds-group">Spacing</h3>' + desc('The same padding and distances as spacing tokens.') + table(['Part', 'Value'], [['Row padding, left and right', '<code>space-16</code>'], ['Gap, label to icon', '<code>space-8</code>'], ['Divider inset', '<code>space-16</code>']])

st_elev = '<h2 class="ds-h2">Elevation</h2>' + table(['Part', 'Token'], [['Menu surface', '<code>elevation-b-80</code>']]) + note('The shadow is listed with the other tokens under Design Tokens.')

st_states = '<h2 class="ds-h2">States</h2>' + desc('Enabled, hover, focus, selected and disabled for both selection types. Hover and focus are forced on this page; in your code they come from <code>:hover</code> and keyboard focus (<code>:focus-visible</code>).') + \
    toolbar([('sb-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force'), ('ss-l', 'Size', 'data-mx="size"', [('lg', 'Large', True), ('sm', 'Small', False)])]) + \
    '<div class="ds-table-wrap"><table class="ds-table pg-matrix" id="matrix"><thead><tr><th scope="col">State</th><th scope="col">Select</th><th scope="col">Multi Select</th></tr></thead><tbody></tbody></table></div>' + \
    note('Figma defines Enabled, Hover, Selected and <strong>Disabled · selected</strong> (Select, all sizes), and Multi Select for Large on desktop only. <strong>Derived here, not in Figma:</strong> the Focus ring (2px <code>border-focus</code> inside the row, as in the other form components), the plain Disabled row, Disabled in Multi Select, and Multi Select for Small and mobile (same 20px icon as the Select variant on those sizes).')

st_typo = '<h2 class="ds-h2">Typography</h2>' + table(['Part', 'Type', 'Size / line height', 'Letter spacing', 'Weight'], [['Label, Large', '<code>body-md</code>', '16/22 mobile, 17/24 from 769px', '0.32px', 'Regular'], ['Label, Small', '<code>body-sm</code>', '14/20', '0.36px', 'Regular']]) + \
    note('Breuer Condensed with <code>ss02</code>, <code>ss03</code> and <code>ss06</code>.')

st_struct = '<h2 class="ds-h2">Structure</h2><h3 class="ds-h3 ds-group">Elements</h3>' + table(['Element', 'Class', 'Notes'], [
    ['Menu', '<code>menu</code>, <code>menu--sm</code>, <code>--multi</code>, <code>--full</code>, <code>--none</code>', 'The white surface with the shadow.'], ['List', '<code>menu__items</code>', 'A <code>ul</code> with <code>role="listbox"</code>. Scrolls after 14 rows.'], ['Row', '<code>menu__item</code>', 'An <code>li</code> with <code>role="option"</code> and <code>aria-selected</code>.'],
    ['Label', '<code>menu__item-label</code>', 'Fills the row.'], ['Check icon', '<code>menu__item-icon</code>', 'Draws <code>circle</code> or <code>check_circle</code> with a pseudo-element. Empty in the markup.']]) + \
    '<h3 class="ds-h3 ds-group">Types</h3>' + table(['Type', 'Class', 'Use'], [['Select', '<code>menu</code>', 'One choice, marked with a check.'], ['Multi Select', '<code>menu menu--multi</code>', 'Several choices: a circle on every row, a check on the chosen ones.'], ['Small', '<code>menu--sm</code>', 'Compact surfaces.'], ['Full-width divider', '<code>menu--full</code>', 'The line runs edge to edge.'], ['No divider', '<code>menu--none</code>', 'No line between rows.']]) + \
    '<h3 class="ds-h3 ds-group">Width</h3>' + desc('The menu is <code>width: 100%</code> of the container the opener gives it.')

st_behavior = '<h2 class="ds-h2">Behavior</h2>' + table(['Input', 'Result'], [
    ['Hover', 'Row fill changes. In Multi Select an unselected row previews the check.'], ['Click, Enter, Space', 'Chooses the row. Select replaces the choice; Multi Select toggles it.'], ['Tab', 'Rows are focusable. A 2px ring shows inside the row on keyboard focus.'],
    ['Arrow keys', 'Up and Down move between rows and skip a disabled row.'], ['Disabled row', '<code>aria-disabled="true"</code>: <code>text-disabled</code> text and icon, no hover fill, not focusable, click and Enter ignored.'], ['Escape', 'The opener closes the menu and returns focus to itself.'], ['Scrolling', 'After 14 rows the list scrolls.']]) + \
    note('Open and close behavior belongs to the opener (button or Select field). This page shows the surface only.')

st_access = '<h2 class="ds-h2">Accessibility Requirements</h2>' + table(['Topic', 'Requirement'], [
    ['Roles', '<code>role="listbox"</code> on the list, <code>role="option"</code> and <code>aria-selected</code> on each row, <code>aria-multiselectable="true"</code> for Multi Select. Name the list with <code>aria-label</code>.'], ['Focus', 'Rows are focusable. A 2px ring on keyboard focus (<code>border-focus</code>) (WCAG 2.4.7, 1.4.11).'],
    ['Keyboard', 'Arrow keys, Enter and Space work. Escape closes through the opener.'], ['State', 'The check icon is not the only signal: <code>aria-selected</code> carries the state for assistive technology (WCAG 1.4.1).'], ['Disabled', 'A disabled row is <code>aria-disabled</code> and not focusable. Disabled tokens are exempt from contrast requirements.']])

spec = [('design-tokens', st_tok), ('sizes', st_sizes), ('measurements', st_meas), ('elevation', st_elev), ('states', st_states), ('typography', st_typo), ('structure', st_struct), ('behavior', st_behavior), ('accessibility-requirements', st_access)]

# ---------------------------------------------------------------- Code
c_basic = '<h2 class="ds-h2">Basic Usage</h2>' + desc('Link the shared stylesheet once per page. Never copy the rules into a page.') + table(['Step', 'What to do'], [
    ['1. Link', '<code>&lt;link rel="stylesheet" href="/components/css/menu.css"&gt;</code>. Both templates already have it.'], ['2. Markup', 'A <code>div.menu</code> with a <code>ul.menu__items[role="listbox"]</code> of <code>li.menu__item[role="option"]</code> rows.'],
    ['3. Row', 'Each row has a <code>span.menu__item-label</code> and an empty <code>span.menu__item-icon</code>. Set <code>aria-selected</code>.'], ['4. Variants', 'Add <code>menu--sm</code>, <code>menu--multi</code>, <code>menu--full</code> or <code>menu--none</code>.'], ['5. Behavior', 'Choosing, keyboard and closing belong to the opener. A Select field uses <code>components/js/select-menu.js</code>.']])
c_menu = '<h2 class="ds-h2">Menu</h2>' + desc('Copy the markup you need. Hover and focus come from <code>:hover</code> and <code>:focus-visible</code>; the <code>[data-state]</code> selectors in the CSS exist only so the documentation can force a state.') + '<div id="recipes"></div>'
c_api = '<h2 class="ds-h2">API</h2><h3 class="ds-h3 ds-group">Classes</h3>' + table(['Class', 'Use'], [['<code>menu</code>', 'The surface. Large, Select, middle-inset divider.'], ['<code>menu--sm</code>', 'Small rows.'], ['<code>menu--multi</code>', 'Multi Select: a circle on every row.'], ['<code>menu--full</code>', 'Full-width divider.'], ['<code>menu--none</code>', 'No divider.'], ['<code>menu__items</code>', 'The list. Scrolls after 14 rows.'], ['<code>menu__item</code>', 'One row.']]) + \
    '<h3 class="ds-h3 ds-group">Things to know</h3>' + bullets(['Breakpoint: Large rows are 40px below 769px and 48px from 769px. The CSS does this by itself.', 'The check icon is drawn with a pseudo-element; keep the <code>menu__item-icon</code> span empty.', 'Put a <code>.list-item</code> inside a row when it needs a leading element or trailing text.', 'The <code>[data-state]</code> selectors do nothing outside the documentation pages.'])
c_css = '<h2 class="ds-h2">CSS / Tailwind</h2>' + desc('The component is one CSS file, shared by every page. Link it, never copy it. The CSS below is read from the file the page links, so it is always what you see.') + code_box('css-code', 'CSS (components/css/menu.css)')
code = [('basic-usage', c_basic), ('menu', c_menu), ('api', c_api), ('css-tailwind', c_css, False)]

# ---------------------------------------------------------------- scripts
MENU_JS = "  var uid = 0;\n" + old_js('menu', "  function menu(o) {", "  var pg = {")

JS_EX = MENU_JS + r'''
  var pg = { size: 'lg', divider: 'inset', variant: 'select', disabled: 'no' };
  function renderPg() {
    var rows = Math.max(1, Math.min(20, parseInt($('#pg-rows').value, 10) || 5)), multi = pg.variant === 'multi';
    clear($('#pg-host')).appendChild(menu({ size: pg.size, divider: pg.divider, multi: multi, rows: rows, selected: [1], disabled: pg.disabled === 'yes' ? [2] : [] }));
    var cls = 'menu' + (pg.size === 'sm' ? ' menu--sm' : '') + (multi ? ' menu--multi' : '') + (pg.divider === 'full' ? ' menu--full' : pg.divider === 'none' ? ' menu--none' : '');
    var items = '';
    for (var i = 0; i < Math.min(rows, 3); i++) items += '      <li class="menu__item" role="option" tabindex="0" aria-selected="' + (i === 1) + '"' + (i === 2 && pg.disabled === 'yes' ? ' aria-disabled="true"' : '') + '>\n        <span class="menu__item-label">Label text</span><span class="menu__item-icon" aria-hidden="true"></span>\n      </li>\n';
    $('#pg-code').textContent = '<div class="' + cls + '">\n  <ul class="menu__items" role="listbox" aria-label="Options"' + (multi ? ' aria-multiselectable="true"' : '') + '>\n' + items + (rows > 3 ? '      <!-- … ' + (rows - 3) + ' more rows -->\n' : '') + '  </ul>\n</div>';
  }
  DK.wire(pg, renderPg); $('#pg-rows').addEventListener('input', renderPg);
  DK.bp();

  var s = clear($('#v-sizes'));
  [['lg', 'Large'], ['sm', 'Small']].forEach(function (x) { s.appendChild(cell(x[1], menu({ size: x[0], rows: 4, selected: [1] }))); });
  var d = clear($('#v-dividers'));
  [['inset', 'Middle-inset'], ['full', 'Full-width'], ['none', 'No divider']].forEach(function (x) { d.appendChild(cell(x[1], menu({ divider: x[0], rows: 4, selected: [1] }))); });
  var t = clear($('#v-select'));
  t.appendChild(cell('Select', menu({ rows: 4, selected: [1] }))); t.appendChild(cell('Multi Select', menu({ multi: true, rows: 4, selected: [0, 2] })));
  clear($('#v-scroll')).appendChild(cell('16 rows', menu({ rows: 16, selected: [1] })));

  /* Usage figures: a menu with real labels */
  function labelled(host, labels, sel) {
    var m = menu({ rows: labels.length, selected: sel || [] }); $$('.menu__item-label', m).forEach(function (l, i) { l.textContent = labels[i]; }); clear($(host)).appendChild(m);
  }
  labelled('#fig-lab-do', ['Price: low to high', 'Price: high to low', 'Newest first', 'Most popular'], [0]);
  labelled('#fig-lab-dont', ['Show the products with the lowest price first and the highest last', 'Show the newest products at the top of the list, then the older ones', 'Most popular'], [0]);
  labelled('#fig-len-do', ['Newest first', 'Price: low to high', 'Price: high to low', 'Most popular'], [0]);
  labelled('#fig-len-dont', ['Newest first', 'Price: low to high', 'Price: high to low', 'Most popular', 'Best rated', 'Most reviewed', 'Name A–Z', 'Name Z–A', 'In stock first', 'On sale first', 'Brand A–Z', 'Brand Z–A', 'Relevance', 'Recently viewed', 'Recommended', 'Staff picks'], [0]);
  $('#fig-len-dont .menu__items').style.maxHeight = '176px';   /* the figure shows the scroll after a few rows, not 14 */

  /* Anatomy */
  var am = menu({ rows: 3, selected: [1] }); clear($('#mn-anat-art')).appendChild(am);
  var row = $$('.menu__item', am)[1];
  DK.callouts($('#mn-anat'), [
    { n: 1, el: am, side: 'top', len: 40, at: 'edge' },
    { n: 2, el: $$('.menu__item', am)[0], side: 'left', len: 56, at: 'edge' },
    { n: 3, side: 'left', len: 56, box: function () { var r = document.createRange(); r.selectNodeContents($('.menu__item-label', row)); return r.getBoundingClientRect(); } },
    { n: 4, el: $('.menu__item-icon', row), side: 'right', len: 40, at: 'center' },
    { n: 5, side: 'bottom', len: 40, at: 'center', box: function () { var r = $$('.menu__item', am)[2].getBoundingClientRect(); return { left: r.left + 16, top: r.bottom - 1, width: r.width - 32, height: 1 }; } }
  ]);
  renderPg();
'''

JS_SPEC = MENU_JS + r'''
  var mx = { size: 'lg' };
  var ROWS = [['Enabled', {}], ['Hover', { hover: [0] }], ['Focus', { focus: [0] }], ['Selected', { selected: [0] }], ['Disabled', { disabled: [0] }], ['Disabled · selected', { disabled: [0], selected: [0] }]];
  function buildMatrix() {
    var tb = clear($('#matrix tbody'));
    ROWS.forEach(function (r) {
      var tr = document.createElement('tr'), th = document.createElement('th'); th.scope = 'row'; th.textContent = r[0]; tr.appendChild(th);
      [false, true].forEach(function (multi) {
        var td = document.createElement('td');
        td.appendChild(menu({ size: mx.size, multi: multi, rows: 1, hover: r[1].hover, focus: r[1].focus, selected: r[1].selected, disabled: r[1].disabled, divider: 'inset' }));
        tr.appendChild(td);
      });
      tb.appendChild(tr);
    });
  }
  DK.seg($('[data-mx="size"]'), function (v) { mx.size = v; buildMatrix(); });
  DK.bp(function () { buildMatrix(); });
  buildMatrix();
  DK.tokenTable($('#tok-table tbody'), [
    ['All', 'Fill', 'surface-raised-primary'], ['All', 'Text', 'text-primary'], ['All', 'Divider', 'border-secondary'],
    ['Hover', 'Row fill', 'surface-navigation-hover'], ['Hover (Multi)', 'Preview check', 'text-action-tertiary'],
    ['Enabled (Multi)', 'Circle icon', 'text-action-tertiary'], ['Selected', 'Check icon', 'text-action-primary'], ['Focus', 'Ring (2px, inside)', 'border-focus'],
    ['Disabled', 'Text and icon', 'text-disabled'], ['Scrollbar', 'Track', 'surface-02'], ['Scrollbar', 'Track edge', 'border-primary'], ['Scrollbar', 'Handle', 'surface-30'],
    ['Container', 'Shadow', 'shadow-elevation-b-80']]);
'''

JS_CODE = r'''
  DK.recipes($('#recipes'), [
    ['Dropdown menu (Select)', '<div class="menu">\n  <ul class="menu__items" role="listbox" aria-label="Sort by">\n    <li class="menu__item" role="option" tabindex="0" aria-selected="false">\n      <span class="menu__item-label">Label text</span><span class="menu__item-icon" aria-hidden="true"></span>\n    </li>\n    <li class="menu__item" role="option" tabindex="0" aria-selected="true">\n      <span class="menu__item-label">Label text</span><span class="menu__item-icon" aria-hidden="true"></span>\n    </li>\n  </ul>\n</div>'],
    ['Multi Select', '<div class="menu menu--multi">\n  <ul class="menu__items" role="listbox" aria-multiselectable="true">…</ul>\n</div>'],
    ['Disabled row', '<li class="menu__item" role="option" tabindex="-1" aria-selected="false" aria-disabled="true">…</li>'],
    ['Small, divider variants', '<div class="menu menu--sm">…</div>        <!-- Small -->\n<div class="menu menu--full">…</div>      <!-- Full-width divider -->\n<div class="menu menu--none">…</div>      <!-- No divider -->'],
    ['A List Item inside a row', '<li class="menu__item" role="option" tabindex="0" aria-selected="true">\n  <div class="list-item">…</div>\n</li>\n<!-- the row sets padding, divider, hover and focus; the list item only fills it -->']
  ]);
  DK.printCss($('#css-code'), 'menu', [[/:is\(:hover, \[data-state="hover"\]\)/g, ':hover'], [/:is\(:focus-visible, \[data-state="focus"\]\)/g, ':focus-visible'], [/^ {4}/gm, '']]);
'''

C = dict(
    slug=SLUG, title='Menu', eyebrow='Components · Menus, lists and dividers',
    lead='A menu is the <strong>list surface</strong> that opens from a button or action (Dropdown menu) or from a Select field (Exposed dropdown menu). The two differ only in the element that opens the surface, so they share one component.',
    lead_ex='Every example on this page is the real component, not a picture. Hover, click and tab to try it. Specification: <code>.claude/skills/eco-menu/SKILL.md</code>. Figma: ' + fig_link(FIGMA % '2724-88966', 'Menu') + '. Row content comes from ' + fig_link('list-item.html', 'List Item').replace(' target="_blank" rel="noopener"', '') + '.',
    lead_spec='Tokens, sizes, measurements, states and requirements. Values come from the live token package and from Figma: ' + fig_link(FIGMA % '2723-85186', 'Base Item') + ' and ' + fig_link(FIGMA % '2728-86374', 'Menu Item Divider') + '.',
    lead_code='How to add a menu to a page. The file is <code>components/css/menu.css</code>.',
    select_menu=False,
    css=['menu'], style=STYLE, ex=ex, spec=spec, code=code, js_ex=JS_EX, js_spec=JS_SPEC, js_code=JS_CODE)

if __name__ == '__main__':
    emit(C)
