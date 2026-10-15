from build import *

FIGMA = 'https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=%s'
SLUG = 'list-item'

STYLE = r'''    .pg-note { font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-tertiary); }
    .pg-col { width: 100%; max-width: 408px; }
    .pg-grid { display: grid; gap: 24px; grid-template-columns: minmax(0, 1fr); width: 100%; }
    @media (min-width: 769px) { .pg-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
    .pg-cap { display: block; margin-bottom: 8px; font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-tertiary); }
    /* demo row = what eco-menu draws around a list item: the side padding and the Menu hover fill */
    .pg-box > .list-item, .pg-box > .pg-grp > .list-item { padding: var(--dimension-spacing-space-12) var(--dimension-spacing-space-16); }
    .pg-box .list-item:hover:not([aria-disabled="true"]) { background: var(--color-surface-navigation-hover); }
    .pg-box .list-item[role]:focus-visible { outline-offset: -2px; } /* inside the row, as in Menu */
    .pg-box { background: var(--color-surface-raised-primary); box-shadow: var(--shadow-elevation-b-80); }
    .pg-grp { display: flex; flex-direction: column; }
    .pg-matrix td { vertical-align: middle; min-width: 260px; }
    .li-fig { width: 100%; max-width: 360px; }
    .li-anat { width: 320px; max-width: 100%; }
    .ds-callout__art { padding-right: 24px; }'''


LEAD = [('none', 'None'), ('icon', 'Icon'), ('check', 'Check box'), ('radio', 'Radio button'), ('swatch', 'Color swatch'), ('tile', 'Color swatch + frame'), ('image', 'Image')]
TRAIL = [('none', 'None'), ('icon', 'Icon'), ('secondary', 'Text secondary'), ('tertiary', 'Text tertiary'), ('check', 'Check box'), ('radio', 'Radio button'), ('switch', 'Switch')]

playground = '<h2 class="ds-h2">Playground</h2>' + desc('Choose a breakpoint, size, leading element, label, overline, supporting text and trailing element. The list item and its markup update. The item sits in a demo row, as it would in a Menu. Click it to toggle it.') + \
    '<div class="ds-playground"><div class="ds-stage ds-stage--center"><div class="pg-col"><div class="pg-box" id="pg-host"></div></div></div><div class="ds-controls">' + \
    bp_field('pg-l-bp') + btn_group('pg-l-size', 'Size', 'data-pg="size"', [('lg', 'Large', True), ('sm', 'Small', False)]) + \
    sel('pg-l-lead', 'pg-lead', 'Leading', 'lead', LEAD, 'check') + btn_group('pg-l-label', 'Label', 'data-pg="label"', [('regular', 'Regular', True), ('bold', 'Bold', False), ('none', 'None', False)]) + \
    sel('pg-l-trail', 'pg-trail', 'Trailing', 'trail', TRAIL, 'secondary') + btn_group('pg-l-over', 'Overline', 'data-pg="over"', [('no', 'None', True), ('yes', 'Overline', False)]) + \
    btn_group('pg-l-sup', 'Supporting text', 'data-pg="sup"', [('none', 'None', True), ('one', '1 line', False), ('two', '2 lines', False)]) + \
    sel('pg-l-sel', 'pg-sel', 'Row', 'sel', [('no', 'Unselected'), ('yes', 'Selected'), ('dis', 'Disabled')], 'no') + \
    '</div></div><h3 class="ds-h3">Markup for this selection</h3>' + code_box('pg-code', 'HTML')

overview = '<h2 class="ds-h2">Overview</h2>' + desc('A list item is the <strong>content of one row</strong>: an optional leading element, a label and an optional trailing element. It is used inside ' + link_large('menu.html', 'Menu') + ', Overflow menu, List Picker, Drawer link and Filter sections in drawer content.') + \
    desc('List Item has two sizes (Large and Small), seven leading elements, seven trailing elements, a regular or bold label, and optional overline and supporting text. The row itself (height, padding, divider, hover and focus) belongs to the container.') + \
    three_pages(SLUG, 'a list item', 'the values: tokens, sizes, states and requirements', 'how to add one to a page')

usage = '<h2 class="ds-h2">Usage</h2><h3 class="ds-h3 ds-group">When to use</h3>' + desc('Use a list item to fill a row in a container that already exists. It is not a page element on its own. Use it:') + \
    bullets(['As the rows of a ' + link_large('menu.html', 'Menu') + ' or an overflow menu', 'In a list picker, a drawer link or a filter section, to choose a value', 'To show a label with a short value, an icon, a swatch, an image or a control']) + \
    '<h3 class="ds-h3 ds-group">When not to use</h3><h3 class="ds-h3">One leading type per list</h3>' + desc('Every row in a list starts with the same kind of element, so the labels line up and the list is easy to scan.') + \
    fig_pair('<div class="pg-box li-fig" id="fig-lead-do"></div>', 'Do use one leading type in a list.', '<div class="pg-box li-fig" id="fig-lead-dont"></div>', 'Do not mix check boxes and icons in the same list.') + \
    '<h3 class="ds-h3">Keep the label on one line</h3>' + desc('Use the trailing value only for a short number or text. A long label wraps and breaks the rhythm of the list.') + \
    fig_pair('<div class="pg-box li-fig" id="fig-lab-do"></div>', 'Do keep the label short and the trailing value to a number or a word.', '<div class="pg-box li-fig" id="fig-lab-dont"></div>', 'Do not write a label that wraps onto a second line.') + \
    '<h3 class="ds-h3">For a standalone form control</h3>' + desc('A check box, radio or switch that stands alone in a form is <code>eco-checkbox</code>, <code>eco-radio</code> or <code>eco-switch</code>. A list item draws the same look as a row’s content.') + \
    '<h3 class="ds-h3">For navigation, tables and cards</h3>' + desc('Page navigation links are in ' + link_large('links-guide.html', 'Links') + ', tabular data is a ' + link_large('../foundations/docs-table.html', 'Docs table') + ', and a long description with actions is a card or a section.') + \
    '<h3 class="ds-h3 ds-group">Quick reference</h3>' + \
    table(['The user…', 'Use'], [['chooses from a list that opens from a button or a Select', '<a class="inline-link inline-link--small" href="menu.html">Menu</a> with list items as rows'], ['picks a value in a filter or picker row', 'List item with a check box, radio or swatch'], ['sees one fixed label and value', 'Plain text, or a table (<code>eco-docs-table</code>)'], ['reads a long description with actions', 'Not a list item: use a card or section']]) + \
    rules(['Keep the label to one line.', 'Use one leading type per list: do not mix check boxes and icons.', 'Inside a Menu put the state (<code>aria-selected</code>) on the row. A standalone item with a control uses <code>role</code> and <code>aria-checked</code>.', 'Use the trailing value for a short number or text.'],
          ['Use a list item outside a container (Menu, picker, drawer).', 'Put a real <code>&lt;input&gt;</code> inside an option row: the leading box is presentational.', 'Add hover or divider styles to the list item: the container owns them.', 'Hardcode colors or sizes: use the tokens and size classes.'])

anatomy = '<h2 class="ds-h2">Anatomy</h2><h3 class="ds-h3 ds-group">List item</h3>' + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout" id="li-anat" role="img" aria-label="Anatomy of a list item: 1 leading element, 2 overline, 3 label, 4 supporting text, 5 trailing element"><div class="ds-callout__art li-fig" id="li-anat-art"></div></div></figure></div>' + \
    ol_parts([('Leading element', 'Optional: an icon, a check box, a radio button, a color swatch (alone or in a frame) or an image.'), ('Overline', 'Optional. A small uppercase line above the label, in <code>text-tertiary</code>.'), ('Label', '<code>body-md</code> (Large) or <code>body-sm</code> (Small), regular or bold. One line.'),
              ('Supporting text', 'Optional. <code>body-sm</code> in <code>text-tertiary</code> below the label, clipped after two lines.'), ('Trailing element', 'Optional: an icon, a short value in secondary or tertiary text, or a check box, radio or switch.')]) + \
    desc('The gap between the parts is 8px. The row height comes from the tallest part and the container.')

variants = '<h2 class="ds-h2">Variants</h2>' + desc('Seven leading elements and seven trailing elements combine freely, with a regular label, a bold label or no label, and optional overline and supporting text. Use the Breakpoint toggle to preview Desktop (769px and up) and Mobile (below 769px). Sizes are under Sizes below.') + \
    toolbar([('vb-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force')]) + \
    '<h3 class="ds-h3 ds-group">Leading</h3>' + desc('What comes before the label: nothing, an icon, a check box, a radio button, a color swatch (alone or in a frame) or an image.') + fig_one('<div class="pg-grid" id="v-lead"></div>') + \
    '<h3 class="ds-h3 ds-group">Trailing</h3>' + desc('What comes after: nothing, an icon, a short value in secondary or tertiary text, or a control (check box, radio, switch). A trailing control is presentational: the item or row carries the state. Click an item to toggle it.') + fig_one('<div class="pg-grid" id="v-trail"></div>') + \
    '<h3 class="ds-h3 ds-group">Overline and supporting text</h3>' + desc('One to three lines: an optional <strong>overline</strong> above the label (small uppercase, tertiary) and optional <strong>supporting text</strong> below it (<code>body-sm</code>, tertiary, clipped after two lines). The container row needs vertical padding for rows taller than one line.') + fig_one('<div class="pg-grid" id="v-text"></div>') + \
    '<h3 class="ds-h3 ds-group">Label weight</h3>' + desc('<strong>Regular</strong> is the default. <strong>Bold</strong> marks a heading-like row, often with a secondary value.') + fig_one('<div class="pg-grid" id="v-weight"></div>')

sizes = '<h2 class="ds-h2">Sizes</h2>' + desc('<strong>Large</strong> is the default. <strong>Small</strong> is for compact surfaces. The Large label changes at 769px; Small is the same on every breakpoint. The values are under ' + sec_link(SLUG, 'sizes', 'Sizes') + ' in Specifications.') + \
    toolbar([('sz-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force')]) + fig_one('<div class="pg-grid" id="v-sizes"></div>')

layout = '<h2 class="ds-h2">Layout &amp; Appearance</h2><h3 class="ds-h3 ds-group">Alignment</h3>' + desc('The leading element and the label stay together at the left. The trailing element sits at the far right. All parts are centered vertically, also in rows with an overline or supporting text.') + \
    '<h3 class="ds-h3 ds-group">Placement</h3>' + desc('A list item is placed inside a container row. The container draws the row height, the padding, the divider, the hover and the focus.') + \
    '<h3 class="ds-h3 ds-group">Width</h3>' + desc('The item fills the width of its row (<code>width: 100%</code>).') + \
    '<h3 class="ds-h3 ds-group">Appearance</h3>' + desc('The label is <code>text-primary</code> and trailing text is secondary or tertiary. A selected check box, radio or swatch frame looks like the matching ECO component. Token names and values are under ' + sec_link(SLUG, 'design-tokens', 'Design Tokens') + ' in Specifications.')

behavior = '<h2 class="ds-h2">Behavior</h2><h3 class="ds-h3 ds-group">Hover and focus</h3>' + desc('A list item has no hover or focus of its own: the container row draws them (see ' + link_large('menu.html', 'Menu') + '). A standalone item with a <code>role</code> gets a pointer and a 2px focus ring.') + \
    '<h3 class="ds-h3 ds-group">Selected</h3>' + desc('Inside a container the row carries <code>aria-selected</code>. A standalone item with a check box, radio or switch is itself <code>role="checkbox"</code>, <code>"radio"</code> or <code>"switch"</code> with <code>aria-checked</code>: a click, Space or Enter toggles it. A radio only selects, and Arrow keys move inside its <code>radiogroup</code>.') + \
    '<h3 class="ds-h3 ds-group">Disabled</h3>' + desc('A disabled item has <code>text-disabled</code> text and icons and is not focusable. All states are listed under ' + sec_link(SLUG, 'states', 'States') + ' in Specifications.')

access = '<h2 class="ds-h2">Accessibility</h2>' + desc('All requirements are listed under ' + sec_link(SLUG, 'accessibility-requirements', 'Accessibility Requirements') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Keyboard support</h3>' + desc('A standalone item is one tab stop. Space or Enter toggles it. In a radio group the checked radio is the tab stop, and the Arrow keys move and select. Inside a Menu the container handles the keys.') + \
    '<h3 class="ds-h3 ds-group">Screen reader support</h3>' + desc('The check box, radio and switch parts are <code>aria-hidden</code>. The state comes from <code>aria-selected</code> on the row or <code>aria-checked</code> on a standalone item with a role. Never put a real <code>&lt;input&gt;</code> inside an option row.')

related = '<h2 class="ds-h2">Related</h2><ul class="ds-bullets"><li><strong>' + link_large('menu.html', 'Menu') + '</strong>. The container that owns the row.</li><li><strong>' + link_large('checkbox.html', 'Checkbox') + '</strong>. The standalone control the check box part copies.</li><li><strong>' + link_large('radio.html', 'Radio button') + '</strong>. The standalone control the radio part copies.</li><li><strong>' + link_large('switch.html', 'Switch') + '</strong>. The track and thumb of the trailing switch.</li><li><strong>' + link_large('../foundations/docs-table.html', 'Docs table') + '</strong>. For rows and columns of data.</li></ul>'

references = '<h2 class="ds-h2">References</h2>' + refs([
    ('https://www.w3.org/WAI/ARIA/apg/patterns/checkbox/', 'WAI-ARIA Authoring Practices: Checkbox', 'Role and keyboard requirements.'),
    ('https://www.w3.org/WAI/ARIA/apg/patterns/radio/', 'WAI-ARIA Authoring Practices: Radio Group', 'Arrow keys and the single tab stop.'),
    ('https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html', 'WCAG 2.2: Name, Role, Value', 'Success criterion 4.1.2.'),
    ('https://m3.material.io/components/lists/overview', 'Material Design 3: Lists', 'Google. Overline, supporting text and trailing controls come from here.'),
    ('https://fluent2.microsoft.design/components/web/react/core/list/usage', 'Fluent 2: List', 'Microsoft.'),
    ('https://carbondesignsystem.com/components/list/usage/', 'Carbon Design System: List', 'IBM.')])

ex = [('playground', playground), ('overview', overview), ('usage', usage), ('anatomy', anatomy), ('variants', variants), ('sizes', sizes), ('layout', layout), ('behavior', behavior), ('accessibility', access), ('related', related), ('references', references)]

# ---------------------------------------------------------------- Specifications
st_tok = '<h2 class="ds-h2">Design Tokens</h2>' + desc('Resolved from the live token package.') + \
    '<div class="ds-table-wrap"><table class="ds-table" id="tok-table"><thead><tr><th scope="col">Part</th><th scope="col">Use</th><th scope="col">Token</th><th scope="col">Value</th></tr></thead><tbody></tbody></table></div>'

st_sizes = '<h2 class="ds-h2">Sizes</h2>' + table(['Breakpoint · size', 'Text', 'Trailing icon', 'Check box / radio area'], [
    ['Desktop · Large', '<code>body-md</code> 17/24, 0.32px', '24px', '24px (16px box)'], ['Mobile · Large', '<code>body-md</code> 16/22, 0.32px', '20px', '24px (16px box)'], ['Desktop and mobile · Small', '<code>body-sm</code> 14/20, 0.36px', '20px', '20px (14px box)']]) + \
    note('<code>sm</code> (640 to 768px) looks like mobile. Small is the same on every breakpoint.') + \
    '<h3 class="ds-h3 ds-group">Leading elements</h3>' + table(['Leading', 'Size', 'Notes'], [
    ['Icon', '20px', 'Material Symbols Outlined, weight 300, <code>icon-primary</code>'], ['Check box', '16px box in a 24px area', 'Same box as <code>eco-checkbox</code>; presentational'], ['Radio button', '16px circle in a 24px area', 'Same circle as <code>eco-radio</code>; presentational'],
    ['Color swatch', '16px', 'Swatch only, no frame'], ['Color swatch + frame', '24px frame, 16px swatch', '1px <code>border-secondary</code>; 2px <code>border-selected</code> when selected'], ['Image', '48px', 'Product or brand image, <code>object-fit: cover</code>']]) + \
    '<h3 class="ds-h3 ds-group">Trailing controls</h3>' + table(['Trailing', 'Size', 'Notes'], [['Check box, radio', '16px in a 24px area (Small 14px in 20px)', 'Same as the leading ones'], ['Switch', 'Large 48×24px, Small 32×16px', 'Track and thumb as <code>eco-switch</code>; on = <code>surface-success-default</code>']])

st_meas = '<h2 class="ds-h2">Measurements</h2><h3 class="ds-h3 ds-group">Dimensions</h3>' + table(['Attribute', 'Value'], [
    ['Gap between leading, label and trailing', '8px'], ['Row height', 'Set by the container; the tallest part is the image (48px)'], ['Padding and margin of the item', 'None: the container sets the row padding'], ['Check box and radio margin', '4px (Large), 3px (Small), so the area is 24px / 20px']]) + \
    note('A list item has no padding of its own, so there is no measurement figure. The row padding belongs to the container (a Menu row has 16px on each side).') + \
    '<h3 class="ds-h3 ds-group">Spacing</h3>' + desc('The gap as a spacing token.') + table(['Part', 'Value'], [['Gap between the parts', '<code>space-8</code>'], ['Leading and trailing icon, check box, radio, swatch, image', 'Figma sizes: literal, no spacing token']])

st_states = '<h2 class="ds-h2">States</h2>' + desc('A list item has no hover or focus of its own: the container row draws them. The item reflects <strong>selected</strong> and <strong>disabled</strong>. Every item here is live and sits in a demo row that shows the Menu hover (<code>surface-navigation-hover</code>); the hover belongs to the row, not to the list item.') + \
    toolbar([('sb-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force'), ('ss-l', 'Size', 'data-mx="size"', [('lg', 'Large', True), ('sm', 'Small', False)])]) + \
    '<div class="ds-table-wrap"><table class="ds-table pg-matrix" id="matrix"><thead><tr><th scope="col">Part</th><th scope="col">Unselected</th><th scope="col">Selected</th><th scope="col">Disabled</th></tr></thead><tbody></tbody></table></div>' + \
    note('Figma shows the enabled item only. <strong>Derived here, not in Figma:</strong> the selected check box, radio and swatch frame (same look as <code>eco-checkbox</code>, <code>eco-radio</code> and the color swatch tile), and the disabled item.')

st_typo = '<h2 class="ds-h2">Typography</h2>' + table(['Part', 'Style', 'Color'], [
    ['Overline', '<code>alt-label-sm</code> uppercase, 12/12 mobile, 14/14 desktop', '<code>text-tertiary</code>'], ['Label', '<code>body-md</code> / <code>body-sm</code>, regular or bold', '<code>text-primary</code>'], ['Trailing text', 'Same as the label', '<code>text-secondary</code> or <code>text-tertiary</code>'], ['Supporting text', '<code>body-sm</code> 14/20, max 2 lines', '<code>text-tertiary</code>']]) + \
    note('Breuer Condensed with <code>ss02</code>, <code>ss03</code> and <code>ss06</code>. The bold label is weight 600 (Figma 700 minus 100 in this CSS).')

st_struct = '<h2 class="ds-h2">Structure</h2><h3 class="ds-h3 ds-group">Elements</h3>' + table(['Element', 'Class', 'Notes'], [
    ['Item', '<code>list-item</code>, <code>list-item--sm</code>', 'A flex row.'], ['Fill', '<code>list-item__fill</code>', 'Holds the leading element and the label. Grows to push the trailing element to the right.'], ['Leading', '<code>list-item__icon</code>, <code>__check</code>, <code>__radio</code>, <code>__swatch</code>, <code>__swatch--tile</code>, <code>__image</code>', 'One of these.'],
    ['Text', '<code>list-item__text</code>, <code>__overline</code>, <code>__label</code>, <code>__label--bold</code>, <code>__support</code>', '<code>__text</code> is a column for overline, label and supporting text.'], ['Trailing', '<code>list-item__trail-icon</code>, <code>__trail-text--secondary</code>, <code>__trail-text--tertiary</code>, <code>__check</code>, <code>__radio</code>, <code>__switch</code>', 'One of these.']]) + \
    '<h3 class="ds-h3 ds-group">Types</h3>' + table(['Type', 'Class', 'Use'], [['Large', '<code>list-item</code>', 'The default.'], ['Small', '<code>list-item--sm</code>', 'Compact surfaces.'], ['Standalone control', '<code>list-item</code> with <code>role="checkbox"</code>, <code>"radio"</code> or <code>"switch"</code>', 'A pointer and a focus ring; the state is <code>aria-checked</code>.']]) + \
    '<h3 class="ds-h3 ds-group">Width</h3>' + desc('The item is <code>width: 100%</code> of its container.')

st_behavior = '<h2 class="ds-h2">Behavior</h2>' + table(['Input', 'Result'], [
    ['Click, Space, Enter', 'On a standalone item: toggles <code>aria-checked</code>. A radio only selects and clears the others in its <code>radiogroup</code>.'], ['Arrow keys', 'In a radio group: move to the next or previous radio and select it (wraps).'], ['Tab', 'One tab stop per item. In a radio group the checked radio is the tab stop.'],
    ['Disabled', '<code>aria-disabled="true"</code> and <code>tabindex="-1"</code>: clicks and keys are ignored.'], ['Inside a Menu', 'The row handles clicks, keys, hover and focus.']])

st_access = '<h2 class="ds-h2">Accessibility Requirements</h2>' + table(['Topic', 'Requirement'], [
    ['Role', 'A standalone item with a control is <code>role="checkbox"</code>, <code>"radio"</code> or <code>"switch"</code> (switch wins over check, check over radio) with <code>aria-checked</code>.'], ['State', 'Inside a container: <code>aria-selected</code> and <code>aria-disabled</code> on the row. The visual (check, dot, frame, switch) must match the attribute (WCAG 4.1.2).'],
    ['Presentational parts', 'The check box, radio, swatch and switch are <code>aria-hidden</code>. Never put a real <code>&lt;input&gt;</code> inside an option row.'], ['Focus', 'A 2px ring with <code>border-focus</code>, offset 2px, on a standalone item (WCAG 2.4.7, 1.4.11).'],
    ['Color', 'The state is not shown by color alone: the check, the dot or the thumb position changes too (WCAG 1.4.1).'], ['Disabled', 'Not focusable. Disabled tokens are exempt from contrast requirements.']])

spec = [('design-tokens', st_tok), ('sizes', st_sizes), ('measurements', st_meas), ('states', st_states), ('typography', st_typo), ('structure', st_struct), ('behavior', st_behavior), ('accessibility-requirements', st_access)]

# ---------------------------------------------------------------- Code
c_basic = '<h2 class="ds-h2">Basic Usage</h2>' + desc('Link the shared stylesheet once per page. Never copy the rules into a page.') + table(['Step', 'What to do'], [
    ['1. Link', '<code>&lt;link rel="stylesheet" href="/components/css/list-item.css"&gt;</code>. Both templates already have it.'], ['2. Markup', 'A <code>div.list-item</code> with a <code>span.list-item__fill</code> (leading element and label) and an optional trailing element.'],
    ['3. Container', 'Put the item inside a container row (<code>li.menu__item</code>). The row sets padding, divider, hover and focus.'], ['4. State', 'Inside a row: <code>aria-selected</code> on the row. Standalone: <code>role</code> and <code>aria-checked</code> on the item, plus the toggle script.'], ['5. Size', 'Large is the default. Add <code>list-item--sm</code> for Small.']])
c_li = '<h2 class="ds-h2">List item</h2>' + desc('Copy the markup you need.') + '<div id="recipes"></div>'
c_api = '<h2 class="ds-h2">API</h2><h3 class="ds-h3 ds-group">Classes</h3>' + table(['Class', 'Use'], [['<code>list-item</code>', 'The item. Large.'], ['<code>list-item--sm</code>', 'Small.'], ['<code>list-item__fill</code>', 'Leading element and label.'], ['<code>list-item__label--bold</code>', 'A bold label.'], ['<code>list-item__text</code>', 'A column for overline, label and supporting text.']]) + \
    '<h3 class="ds-h3 ds-group">Things to know</h3>' + bullets(['Breakpoint: the Large label is 16/22 below 769px and 17/24 from 769px. The CSS does this by itself.', 'Never add height, divider or hover styles to a list item: the container owns them.', 'Swatch colors are product data: set them with <code>style="--swatch: …"</code>.', 'The toggle behavior of a standalone item is a small script; copy it from the recipe on this page.', 'The <code>[data-state]</code> selectors do nothing outside the documentation pages.'])
c_css = '<h2 class="ds-h2">CSS / Tailwind</h2>' + desc('The component is one CSS file, shared by every page. Link it, never copy it. The CSS below is read from the file the page links, so it is always what you see.') + code_box('css-code', 'CSS (components/css/list-item.css)')
code = [('basic-usage', c_basic), ('list-item', c_li), ('api', c_api), ('css-tailwind', c_css, False)]

# ---------------------------------------------------------------- scripts
TOGGLE_OLD = '$$(\'[data-pg="sel"] button\').forEach(function (b) { b.setAttribute(\'aria-pressed\', String(b.dataset.v === pg.sel)); });'
TOGGLE_NEW = "var sd = $('#pg-sel'); if (sd) { sd.value = pg.sel; sd.dispatchEvent(new Event('change')); }"   # the Row control is an eco-select now, not a button group
_old = old_js('list-item', "  var SW = '#1651aa';", "  function item(o)")
assert TOGGLE_OLD in _old
LI_JS = "  var uid = 0;\n" + _old.replace(TOGGLE_OLD, TOGGLE_NEW) + r'''
  function item(o) { var d = document.createElement('div'); d.innerHTML = markup(o); return d.firstChild; }
  function boxed(node) { var b = document.createElement('div'); b.className = 'pg-box'; b.appendChild(node); return b; }
  function cell(cap, node) { var d = document.createElement('div'); var c = document.createElement('span'); c.className = 'pg-cap'; c.textContent = cap; d.appendChild(c); var b = document.createElement('div'); b.className = 'pg-box'; b.appendChild(node); d.appendChild(b); return d; }
  var base = { size: 'lg', lead: 'none', label: 'regular', trail: 'none', sel: 'no', over: 'no', sup: 'none' };
  function o(x) { var r = {}; for (var k in base) r[k] = base[k]; for (k in x) r[k] = x[k]; return r; }
  var pg = o({ lead: 'check', trail: 'secondary' });
  var LEAD = [['none', 'None (label only)'], ['icon', 'Icon'], ['check', 'Check box'], ['radio', 'Radio button'], ['swatch', 'Color swatch'], ['tile', 'Color swatch + frame'], ['image', 'Image']];
  var TRAIL = [['none', 'None'], ['icon', 'Icon'], ['secondary', 'Text secondary'], ['tertiary', 'Text tertiary'], ['check', 'Check box'], ['radio', 'Radio button'], ['switch', 'Switch']];
'''

JS_EX = LI_JS + r'''
  function renderPg() { var h = clear($('#pg-host')); var it = item(pg); it.id = 'pg-item'; h.appendChild(it); $('#pg-code').textContent = markup(pg); }
  DK.wire(pg, renderPg);
  DK.bp();

  LEAD.forEach(function (x) { $('#v-lead').appendChild(cell(x[1], item(o({ lead: x[0], trail: 'secondary', label: x[0] === 'swatch' ? 'none' : 'regular' })))); });
  TRAIL.forEach(function (x) { $('#v-trail').appendChild(cell(x[1], item(o({ lead: 'icon', trail: x[0] })))); });
  var grp = document.createElement('div'); grp.setAttribute('role', 'radiogroup'); grp.setAttribute('aria-label', 'Delivery'); grp.className = 'pg-grp';
  ['Standard', 'Express', 'Pick-up'].forEach(function (t, i) { var r = item(o({ lead: 'radio', sel: i === 0 ? 'yes' : 'no' })); r.querySelector('.list-item__label').textContent = t; if (i) r.tabIndex = -1; grp.appendChild(r); });
  $('#v-trail').appendChild(cell('Radio group: pick one (arrow keys move)', grp));
  [['One line + overline', { lead: 'icon', over: 'yes' }], ['Label + supporting text', { lead: 'icon', sup: 'one', trail: 'tertiary' }], ['Overline + label + 2 lines', { lead: 'image', over: 'yes', sup: 'two', trail: 'icon' }], ['Small, supporting text', { size: 'sm', lead: 'icon', sup: 'one' }]]
    .forEach(function (x) { $('#v-text').appendChild(cell(x[0], item(o(x[1])))); });
  [['Regular label', { label: 'regular', trail: 'tertiary' }], ['Bold label', { label: 'bold', trail: 'secondary' }], ['Small, regular', { size: 'sm', trail: 'tertiary' }], ['Small, bold', { size: 'sm', label: 'bold', trail: 'secondary' }]]
    .forEach(function (x) { $('#v-weight').appendChild(cell(x[0], item(o(x[1])))); });
  [['Large, regular', { trail: 'secondary', lead: 'icon' }], ['Small, regular', { size: 'sm', trail: 'secondary', lead: 'icon' }], ['Large, check box', { lead: 'check', trail: 'tertiary' }], ['Small, check box', { size: 'sm', lead: 'check', trail: 'tertiary' }]]
    .forEach(function (x) { $('#v-sizes').appendChild(cell(x[0], item(o(x[1])))); });

  /* Usage figures */
  function rows(host, list) { var h = clear($(host)); list.forEach(function (r) { var it = item(o(r[0])); it.querySelector('.list-item__label').textContent = r[1]; h.appendChild(it); }); }
  rows('#fig-lead-do', [[{ lead: 'check' }, 'Cotton'], [{ lead: 'check' }, 'Leather'], [{ lead: 'check' }, 'Nylon']]);
  rows('#fig-lead-dont', [[{ lead: 'check' }, 'Cotton'], [{ lead: 'icon' }, 'Leather'], [{ lead: 'radio' }, 'Nylon']]);
  rows('#fig-lab-do', [[{ lead: 'check', trail: 'tertiary' }, 'Safety shoes'], [{ lead: 'check', trail: 'tertiary' }, 'Gloves']]);
  rows('#fig-lab-dont', [[{ lead: 'check', trail: 'tertiary' }, 'Safety shoes with a steel toe cap and a slip-resistant sole'], [{ lead: 'check', trail: 'tertiary' }, 'Gloves']]);

  /* Anatomy */
  var ai = item(o({ lead: 'icon', over: 'yes', sup: 'one', trail: 'tertiary' })); var ab = boxed(ai); ab.classList.add('li-anat'); clear($('#li-anat-art')).appendChild(ab);
  function rng(el) { return function () { var r = document.createRange(); r.selectNodeContents(el); return r.getBoundingClientRect(); }; }
  DK.callouts($('#li-anat'), [
    { n: 1, el: $('.list-item__icon', ai), side: 'left', len: 48, at: 'edge' },
    { n: 2, side: 'top', len: 40, box: rng($('.list-item__overline', ai)), at: 'edge' },
    { n: 3, side: 'right', len: 72, box: rng($('.list-item__label', ai)), at: 'edge' },
    { n: 4, side: 'bottom', len: 40, box: rng($('.list-item__support', ai)), at: 'edge' },
    { n: 5, el: $('.list-item__trail-text', ai), side: 'top', len: 40, at: 'center' }
  ]);
  renderPg();
'''

JS_SPEC = LI_JS + r'''
  var mx = { size: 'lg' };
  function buildMatrix() {
    var tb = clear($('#matrix tbody'));
    function row(name, x) {
      var tr = document.createElement('tr'), th = document.createElement('th'); th.scope = 'row'; th.textContent = name; tr.appendChild(th);
      ['no', 'yes', 'dis'].forEach(function (s) { var td = document.createElement('td'); var cfg = {}; for (var k in x) cfg[k] = x[k]; cfg.sel = s; cfg.size = mx.size; td.appendChild(boxed(item(o(cfg)))); tr.appendChild(td); });
      tb.appendChild(tr);
    }
    LEAD.filter(function (x) { return ['check', 'radio', 'tile', 'icon'].indexOf(x[0]) > -1; }).forEach(function (x) { row(x[1], { lead: x[0], trail: 'secondary' }); });
    [['Trailing check box', 'check'], ['Trailing radio', 'radio'], ['Trailing switch', 'switch']].forEach(function (x) { row(x[0], { lead: 'none', trail: x[1] }); });
  }
  DK.seg($('[data-mx="size"]'), function (v) { mx.size = v; buildMatrix(); });
  DK.bp(function () { buildMatrix(); });
  buildMatrix();
  DK.tokenTable($('#tok-table tbody'), [
    ['Label', 'Text', 'text-primary'], ['Trailing text', 'Secondary', 'text-secondary'], ['Trailing text', 'Tertiary', 'text-tertiary'], ['Icons', 'Leading and trailing', 'icon-primary'],
    ['Check box, radio', 'Border (unselected)', 'border-input-control-default'], ['Check box, radio', 'Fill (unselected)', 'surface-raised-primary'], ['Check box', 'Fill (selected)', 'surface-100'], ['Radio', 'Border (selected)', 'border-selected'],
    ['Swatch frame', 'Border', 'border-secondary'], ['Swatch frame', 'Border (selected)', 'border-selected'], ['Overline, supporting text', 'Text', 'text-tertiary'], ['Switch', 'Track off', 'surface-20'], ['Switch', 'Track on', 'surface-success-default'], ['Disabled', 'Text and icons', 'text-disabled'], ['Gap', '8px', 'dimension-spacing-space-8']]);
'''

JS_CODE = r'''
  DK.recipes($('#recipes'), [
    ['Check box + label + trailing text', '<div class="list-item" role="checkbox" tabindex="0" aria-checked="false">\n  <span class="list-item__fill">\n    <span class="list-item__check" aria-hidden="true"></span>\n    <span class="list-item__label">0 – 999 kr</span>\n  </span>\n  <span class="list-item__trail-text list-item__trail-text--tertiary">24</span>\n</div>'],
    ['Icon + label + trailing icon', '<div class="list-item">\n  <span class="list-item__fill">\n    <span class="list-item__icon" aria-hidden="true">person</span>\n    <span class="list-item__label">Label text</span>\n  </span>\n  <span class="list-item__trail-icon" aria-hidden="true">check_circle</span>\n</div>'],
    ['Overline, label, supporting text', '<div class="list-item">\n  <span class="list-item__fill">\n    <span class="list-item__text">\n      <span class="list-item__overline">Overline</span>\n      <span class="list-item__label">Label text</span>\n      <span class="list-item__support">Supporting text</span>\n    </span>\n  </span>\n</div>'],
    ['Trailing switch', '<div class="list-item" role="switch" tabindex="0" aria-checked="true">\n  <span class="list-item__fill"><span class="list-item__label">Email notifications</span></span>\n  <span class="list-item__switch" aria-hidden="true"></span>\n</div>'],
    ['Radio group', '<div role="radiogroup" aria-label="Delivery">\n  <div class="list-item" role="radio" tabindex="0" aria-checked="true">…<span class="list-item__radio" aria-hidden="true"></span>…</div>\n  <div class="list-item" role="radio" tabindex="-1" aria-checked="false">…</div>\n</div>\n<!-- one tab stop (the checked radio); arrow keys move and select; click selects -->'],
    ['Behavior (script)', 'document.addEventListener(\'click\', function (e) {\n  var li = e.target.closest(\'.list-item[role]\');\n  if (!li || li.getAttribute(\'aria-disabled\') === \'true\') return;\n  if (li.getAttribute(\'role\') === \'radio\') { /* clear the others in the radiogroup, then check this one */ }\n  else li.setAttribute(\'aria-checked\', String(li.getAttribute(\'aria-checked\') !== \'true\'));\n});\n// plus: Space/Enter toggles; arrow keys move in a radiogroup.'],
    ['Inside a Menu row', '<li class="menu__item" role="option" tabindex="0" aria-selected="true">\n  <div class="list-item">…</div>\n</li>\n<!-- the row sets padding, divider, hover and focus; the list item only fills it -->'],
    ['Variants', '<div class="list-item list-item--sm">…</div>   <!-- Small -->\n<span class="list-item__label list-item__label--bold">…</span>   <!-- Bold label -->\n<span class="list-item__radio" aria-hidden="true"></span>   <!-- Radio -->\n<span class="list-item__swatch list-item__swatch--tile" style="--swatch: #1651aa"></span>   <!-- Swatch + frame -->\n<img class="list-item__image" src="…" alt="" />   <!-- Image 48px -->']
  ]);
  DK.printCss($('#css-code'), 'list-item', [[/^ {4}/gm, '']]);
'''

C = dict(
    slug=SLUG, title='List Item', eyebrow='Components · Menus, lists and dividers',
    lead='A list item is the <strong>content of one row</strong>: an optional leading element, a label and an optional trailing element. It is used inside Menu, Overflow menu, List Picker, Drawer link and Filter sections in drawer content.',
    lead_ex='Every example on this page is the real component, not a picture. The row itself (height, padding, divider, hover, focus) belongs to the container. Specification: <code>.claude/skills/eco-list-item/SKILL.md</code>. Figma: ' + fig_link(FIGMA % '3140-104687', 'List Item Content') + '.',
    lead_spec='Tokens, sizes, states and requirements. Values come from the live token package and from Figma: ' + fig_link(FIGMA % '3137-104383', 'Base List Item') + '.',
    lead_code='How to add a list item to a page. The file is <code>components/css/list-item.css</code>.',
    select_menu=True,
    css=['list-item', 'menu'], style=STYLE, ex=ex, spec=spec, code=code, js_ex=JS_EX, js_spec=JS_SPEC, js_code=JS_CODE)

if __name__ == '__main__':
    emit(C)
