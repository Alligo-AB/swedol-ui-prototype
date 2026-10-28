from build import *

FIGMA = 'https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=17345-30209'
FIGMA_B = 'https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=17345-30170'
SLUG = 'chip'

STYLE = r'''    .pg-states { display: grid; gap: 24px 32px; grid-template-columns: repeat(2, max-content); align-items: center; justify-content: center; }
    @media (min-width: 769px) { .pg-states { grid-template-columns: repeat(4, max-content); } }
    .pg-cell { display: flex; flex-direction: column; align-items: flex-start; gap: 12px; }
    .pg-cell > span:first-child { font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-tertiary); }'''


def chip(label='Chip label', cls='', state=None, pressed=None, icon=None, removable=False):
    c = 'chip' + ((' ' + cls) if cls else '') + (' chip--removable' if removable else '')
    a = (' data-state="%s"' % state) if state else ''
    a += (' aria-pressed="%s"' % pressed) if pressed is not None else ''
    a += (' aria-label="Remove %s"' % label) if removable else ''
    i = ('<span class="chip__icon" aria-hidden="true">%s</span>' % icon) if icon else ''
    return '<button type="button" class="%s"%s>%s<span class="chip__label">%s</span><span class="chip__close" aria-hidden="true">close</span></button>' % (c, a, i, label)


def states_row(cls):
    cells = [('Enabled', chip(cls=cls, pressed='false')), ('Hover', chip(cls=cls, state='hover', pressed='false')), ('Selected', chip(cls=cls, pressed='true')), ('Selected hover', chip(cls=cls, state='selected-hover', pressed='true'))]
    return '<div class="pg-states">' + ''.join('<div class="pg-cell"><span>%s</span>%s</div>' % (n, h) for n, h in cells) + '</div>'


playground = '<h2 class="ds-h2">Playground</h2>' + desc('Choose type, size and content, then click the chip. The chip and its code update.') + \
    '<div class="ds-playground"><div class="ds-stage ds-stage--center" id="pg-stage"><div id="pg-host" class="chip-group"></div></div><div class="ds-controls">' + \
    btn_group('pg-l-type', 'Type', 'data-pg="type"', [('filter', 'Filter', True), ('removable', 'Removable', False)]) + \
    btn_group('pg-l-size', 'Size', 'data-pg="size"', [('md', 'Medium', True), ('sm', 'Small', False)]) + \
    btn_group('pg-l-icon', 'Leading icon', 'data-pg="icon"', [('off', 'Off', True), ('on', 'On', False)]) + \
    '</div></div><h3 class="ds-h3">Markup for this selection</h3>' + code_box('pg-code', 'HTML')

overview = '<h2 class="ds-h2">Overview</h2>' + desc('A chip is a <strong>small, interactive element</strong> that represents an input, an attribute or an action. Most often it is a filter: the user clicks it to pick a value, and clicks it again to drop it.') + \
    desc('Chip has two sizes (Medium and Small), an optional leading icon and four states. A selected chip gets a grey surface and a close icon. On mobile, Medium uses the mobile body text; everything else is the same on every breakpoint.') + \
    three_pages(SLUG, 'a chip', 'the values: sizes, tokens, states and requirements', 'how to add chips to a page')

usage = '<h2 class="ds-h2">Usage</h2><h3 class="ds-h3 ds-group">When to use</h3>' + \
    bullets(['To show the filters or choices the user has picked, for example the values picked in a filter drawer or a dropdown.', 'To show what the user has typed as separate items, for example email addresses in a recipient field.', 'As an action the user can undo, for example a removable chip with a close icon.']) + \
    '<h3 class="ds-h3 ds-group">When not to use</h3>' + \
    table(['The user…', 'Use instead'], [['starts an action (save, add to cart)', link_large('button.html', 'Button')], ['switches between two views', link_large('segment-control.html', 'Pill segment control')], ['picks one option in a form', link_large('radio.html', 'Radio button')], ['reads a status that is not interactive', link_large('badge.html', 'Badge')]]) + \
    '<h3 class="ds-h3 ds-group">Filter chips</h3>' + desc('Filter chips are unselected by default. The user clicks each chip to select as many as they like. Clicking a selected chip, or its close icon, unselects it.') + \
    fig_pair('<div class="chip-group">' + chip('Gloves', pressed='true') + chip('Safety shoes', pressed='false') + chip('Workwear', pressed='true') + chip('Hearing protection', pressed='false') + '</div>', 'Do keep the labels short, one or two words.',
             '<div class="chip-group">' + chip('Show all gloves that are in stock in your store', pressed='false') + '</div>', 'Do not write a sentence in a chip.') + \
    rules(['Keep the label short: one or two words.', 'Put chips of the same kind in one row (<code>chip-group</code>), so they wrap together.', 'Use the same size for every chip in a row.'],
          ['Use a chip as a call to action: use a button.', 'Mix Medium and Small in one row.', 'Use a chip for a status that cannot be clicked: use a badge.'])

anatomy = '<h2 class="ds-h2">Anatomy</h2>' + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout" id="ch-anat" role="img" aria-label="Anatomy of a chip: 1 frame, 2 leading icon, 3 label, 4 close icon"><div class="ds-callout__art"><span id="an-chip">' + chip(icon='assignment_turned_in', pressed='true') + '</span></div></div></figure></div>' + \
    ol_parts([('Frame', 'A 1px Border Primary line. A selected chip has no line and a grey 10% surface instead.'), ('Leading icon', 'Optional, 16px. It adds meaning to the label.'), ('Label', 'Body text: body-md on Medium, body-sm on Small.'), ('Close icon', '14px. Shown on a selected chip and on a removable chip.')])

variants = '<h2 class="ds-h2">Variants</h2><h3 class="ds-h3 ds-group">Label only</h3>' + desc('The default chip. The close icon appears when it is selected.') + \
    fig_one('<div class="chip-group">' + chip(pressed='false') + chip(pressed='true') + '</div>') + \
    '<h3 class="ds-h3 ds-group">With a leading icon</h3>' + desc('An icon before the label, for example to show the type of value.') + \
    fig_one('<div class="chip-group">' + chip(icon='assignment_turned_in', pressed='false') + chip(icon='assignment_turned_in', pressed='true') + '</div>') + \
    '<h3 class="ds-h3 ds-group">Removable</h3>' + desc('An input or action chip that always shows the close icon. A click removes the chip (<code>chip--removable</code>).') + \
    fig_one('<div class="chip-group">' + chip('anna@example.com', removable=True) + chip('erik@example.com', removable=True) + '</div>')

sizes = '<h2 class="ds-h2">Sizes</h2>' + desc('Medium (32px, default) and Small (24px). The values are under ' + sec_link(SLUG, 'sizes', 'Sizes') + ' in Specifications.') + \
    fig_one('<div class="chip-group" style="align-items:center">' + chip(pressed='false') + chip(cls='chip--sm', pressed='false') + chip(pressed='true') + chip(cls='chip--sm', pressed='true') + '</div>')

states = '<h2 class="ds-h2">States</h2>' + desc('Four states. Hover darkens the frame; a selected chip has a grey surface and a close icon; hover on a selected chip adds a grey frame. Keyboard focus shows the ECO focus ring.') + \
    '<h3 class="ds-h3 ds-group">Medium</h3>' + fig_one(states_row('')) + '<h3 class="ds-h3 ds-group">Small</h3>' + fig_one(states_row('chip--sm'))

behavior = '<h2 class="ds-h2">Behavior</h2>' + bullets(['A filter chip is a toggle button. A click or <kbd>Space</kbd>/<kbd>Enter</kbd> selects it or unselects it.', 'A removable chip is removed by a click. Move the focus to the next chip, or to the field, after it is removed.', 'Chips in a row wrap to the next line; they never scroll sideways.']) + \
    '<h3 class="ds-h3 ds-group">Breakpoints</h3>' + desc('The size is the same on every breakpoint. Medium uses body-md, which is 16px on mobile and 17px from 769px.')

access = '<h2 class="ds-h2">Accessibility</h2>' + desc('All requirements are listed under ' + sec_link(SLUG, 'accessibility-requirements', 'Accessibility Requirements') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Keyboard support</h3>' + table(['Key', 'Action'], [['<kbd>Tab</kbd>', 'Moves the focus to the next chip.'], ['<kbd>Space</kbd>, <kbd>Enter</kbd>', 'Selects or unselects a filter chip; removes a removable chip.']]) + \
    '<h3 class="ds-h3 ds-group">Screen reader support</h3>' + desc('A filter chip is a <code>&lt;button&gt;</code> with <code>aria-pressed</code>, so it is read as a toggle button, pressed or not pressed. A removable chip gets <code>aria-label="Remove …"</code>. The icons are hidden from screen readers.')

related = '<h2 class="ds-h2">Related</h2><ul class="ds-bullets"><li><strong>' + link_large('badge.html', 'Badge') + '</strong>. A status or label that is not interactive.</li><li><strong>' + link_large('button.html', 'Button') + '</strong>. For actions.</li><li><strong>' + link_large('checkbox.html', 'Checkbox') + '</strong>. Many choices in a form or filter list.</li></ul>'

references = '<h2 class="ds-h2">References</h2>' + refs([
    ('https://m3.material.io/components/chips/overview', 'Material Design 3: Chips', 'Google.'),
    ('https://www.w3.org/WAI/ARIA/apg/patterns/button/', 'WAI-ARIA Authoring Practices: Button', 'Toggle buttons and aria-pressed.'),
    ('https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html', 'WCAG 2.2: Target Size (Minimum)', 'Success criterion 2.5.8: 24 by 24px.')])

ex = [('playground', playground), ('overview', overview), ('usage', usage), ('anatomy', anatomy), ('variants', variants), ('sizes', sizes), ('states', states), ('behavior', behavior), ('accessibility', access), ('related', related), ('references', references)]

# ---------------------------------------------------------------- Specifications
st_tok = '<h2 class="ds-h2">Design Tokens</h2>' + desc('Resolved from the live token package.') + \
    '<div class="ds-table-wrap"><table class="ds-table" id="tok-table"><thead><tr><th scope="col">Part</th><th scope="col">Use</th><th scope="col">Token</th><th scope="col">Value</th></tr></thead><tbody></tbody></table></div>'

st_sizes = '<h2 class="ds-h2">Sizes</h2>' + table(['Size', 'Height', 'Padding', 'Text', 'Close icon'], [
    ['Medium (default)', '32px', '0 8px', 'body-md: 16/22 mobile, 17/24 from 769px', '14px'], ['Small (<code>chip--sm</code>)', '24px', '0 8px; 0 4px 0 8px with the close icon', 'body-sm: 14/20', '14px']]) + \
    note('The height is fixed and the label is centred, so the vertical padding is 0. The leading icon is 16px and the gap between the parts is 4px on both sizes.')

MEAS_ITEM = '<div class="measure__item"><span class="measure__name">%s</span><div class="measure__obj">%s<i class="measure__pad measure__pad--l"></i><i class="measure__pad measure__pad--r"></i><b class="measure__dim measure__dim--h measure__dim--l"><span></span></b><b class="measure__dim measure__dim--h measure__dim--r"><span></span></b></div></div>'
st_meas = '<h2 class="ds-h2">Measurements</h2><h3 class="ds-h3 ds-group">Dimensions</h3>' + desc('Side padding of both sizes, enabled and selected. The shaded areas are the padding; the lines show its value.') + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-fig__stage--flush" style="padding:0;min-height:0"><div class="measure" role="img" aria-label="Side padding of the chip: 8px; Small selected 8px left and 4px right">' + \
    ''.join(MEAS_ITEM % (n, chip(cls=c + ' measure__subject', pressed=p)) for n, c, p in [('1 · Medium', '', 'false'), ('2 · Medium, selected', '', 'true'), ('3 · Small', 'chip--sm', 'false'), ('4 · Small, selected', 'chip--sm', 'true')]) + \
    '</div></div><figcaption class="ds-fig__cap">At true size (1:1). The numbers are read from the component.</figcaption></figure></div>' + \
    table(['Attribute', 'Medium', 'Small'], [['Height', '32px', '24px'], ['Padding, left', '8px', '8px'], ['Padding, right', '8px', '8px; 4px with the close icon'], ['Gap', '4px', '4px'], ['Border', '1px', '1px'], ['Corners', 'Square', 'Square']]) + \
    '<h3 class="ds-h3 ds-group">Spacing</h3>' + table(['Part', 'Token'], [['Side padding', '<code>space-8</code>'], ['Right padding, Small with close icon', '<code>space-4</code>'], ['Gap between icon and label', '<code>space-4</code>'], ['Gap between chips (<code>chip-group</code>)', '<code>space-8</code>']])

st_states = '<h2 class="ds-h2">States</h2>' + table(['State', 'Surface', 'Frame', 'Text and icon', 'Close icon'], [
    ['Enabled', 'None', '<code>border-primary</code>', '<code>text-primary</code>, <code>icon-primary</code>', 'Hidden'],
    ['Hover', 'None', '<code>border-hover</code>', 'Same', 'Hidden'],
    ['Selected', '<code>surface-opacity-black-10</code>', 'None', 'Same', 'Shown'],
    ['Selected hover', '<code>surface-opacity-black-10</code>', '<code>border-selected-hover</code>', 'Same', 'Shown'],
    ['Focus (keyboard)', 'As the state below it', 'Plus a 2px <code>border-focus</code> ring, 2px out', 'Same', 'As the state below it']]) + \
    note('Figma has no disabled state. Hide a chip that cannot be used.')

st_type = '<h2 class="ds-h2">Typography</h2>' + table(['Size', 'Mobile (0–768px)', 'Desktop (769px+)'], [['Medium', 'body-md 16/22, 0.32px', 'body-md 17/24, 0.32px'], ['Small', 'body-sm 14/20, 0.36px', 'body-sm 14/20, 0.36px']]) + \
    note('Weight Regular (400). Figma sets the line height to 16 (Medium) and 14 (Small); the page uses the token pairs, and the fixed height keeps the chip the same size.')

st_struct = '<h2 class="ds-h2">Structure</h2>' + table(['Element', 'Class', 'Notes'], [
    ['Chip', '<code>chip</code>', 'A <code>&lt;button type="button"&gt;</code>. Filter chip: add <code>aria-pressed</code>.'], ['Size', '<code>chip--sm</code>', 'Small. Medium is the default.'],
    ['Removable', '<code>chip--removable</code>', 'Always shows the close icon; a click removes it.'], ['Leading icon', '<code>chip__icon</code>', 'Material Symbols, 16px, <code>aria-hidden</code>.'],
    ['Label', '<code>chip__label</code>', ''], ['Close icon', '<code>chip__close</code>', 'Material Symbols <code>close</code>, 14px, <code>aria-hidden</code>.'], ['Row', '<code>chip-group</code>', 'Wrapping flex row, 8px gap.']])

st_behavior = '<h2 class="ds-h2">Behavior</h2>' + table(['Topic', 'Result'], [['Click on a filter chip', 'Toggles <code>aria-pressed</code> and fires <code>chip:change</code> (<code>components/js/chip.js</code>).'], ['Click on a removable chip', 'Fires <code>chip:remove</code>; the page removes the chip.'], ['Breakpoint', 'Only the Medium text changes, at 769px.'], ['Motion', 'Frame and surface change with <code>duration-fast-2</code>, <code>ease-standard</code>.']])

st_access = '<h2 class="ds-h2">Accessibility Requirements</h2>' + table(['Topic', 'Requirement'], [
    ['Role', 'A native <code>&lt;button&gt;</code>. A filter chip has <code>aria-pressed="true|false"</code>.'], ['Name', 'The label. A removable chip: <code>aria-label="Remove &lt;label&gt;"</code>.'],
    ['Focus', 'Visible ring on <code>:focus-visible</code> (WCAG 2.4.7).'], ['Target size', 'Small is 24px high: the minimum (WCAG 2.5.8). Keep 8px between chips.'],
    ['Selected', 'Never only color: the close icon and <code>aria-pressed</code> also show it.']])

spec = [('design-tokens', st_tok), ('sizes', st_sizes), ('measurements', st_meas), ('states', st_states), ('typography', st_type), ('structure', st_struct), ('behavior', st_behavior), ('accessibility-requirements', st_access)]

# ---------------------------------------------------------------- Code
c_basic = '<h2 class="ds-h2">Basic Usage</h2>' + desc('Link the shared files once per page. Never copy the rules into a page.') + table(['Step', 'What to do'], [
    ['1. Link', '<code>&lt;link rel="stylesheet" href="/components/css/chip.css"&gt;</code> and <code>&lt;script src="/components/js/chip.js" defer&gt;&lt;/script&gt;</code>. Both templates already have them.'],
    ['2. Row', 'Put the chips in a <code>div.chip-group</code>.'], ['3. Chip', 'A <code>button.chip</code> with <code>aria-pressed="false"</code>, a label span and a close icon span.'], ['4. Listen', 'React to <code>chip:change</code> (filter) or <code>chip:remove</code> (removable).']])
c_chip = '<h2 class="ds-h2">Chip</h2>' + desc('Copy the markup you need.') + '<div id="recipes"></div>'
c_api = '<h2 class="ds-h2">API</h2>' + table(['Class / event', 'Use'], [['<code>chip</code>', 'Medium chip.'], ['<code>chip--sm</code>', 'Small chip.'], ['<code>chip--removable</code>', 'Close icon always shown; click fires <code>chip:remove</code>.'], ['<code>chip-group</code>', 'Wrapping row with 8px gap.'], ['<code>chip:change</code>', 'Fired on a filter chip after a click; <code>event.detail.selected</code>.'], ['<code>chip:remove</code>', 'Fired on a removable chip; remove it and move the focus.']])
c_css = '<h2 class="ds-h2">CSS / Tailwind</h2>' + desc('The component is one CSS file, shared by every page. Link it, never copy it. The CSS below is read from the file the page links.') + code_box('css-code', 'CSS (components/css/chip.css)')
code = [('basic-usage', c_basic), ('chip', c_chip), ('api', c_api), ('css-tailwind', c_css, False)]

# ---------------------------------------------------------------- scripts
JS_EX = r'''
  var pg = { type: 'filter', size: 'md', icon: 'off' };
  function markup() {
    var cls = 'chip' + (pg.size === 'sm' ? ' chip--sm' : '') + (pg.type === 'removable' ? ' chip--removable' : '');
    var a = pg.type === 'removable' ? ' aria-label="Remove Chip label"' : ' aria-pressed="false"';
    var ic = pg.icon === 'on' ? '\n  <span class="chip__icon" aria-hidden="true">assignment_turned_in</span>' : '';
    return '<button type="button" class="' + cls + '"' + a + '>' + ic + '\n  <span class="chip__label">Chip label</span>\n  <span class="chip__close" aria-hidden="true">close</span>\n</button>';
  }
  function renderPg() { var m = markup(); $('#pg-host').innerHTML = m; $('#pg-code').textContent = m; }
  $('#pg-host').addEventListener('chip:remove', function () { renderPg(); });   /* the demo puts it back */
  DK.wire(pg, renderPg);
  $$('[data-state]').forEach(function (c) { c.setAttribute('tabindex', '-1'); c.style.pointerEvents = 'none'; });   /* forced-state demos are pictures */
  $$('.ds-fig .chip--removable').forEach(function (c) { c.addEventListener('chip:remove', function () { c.remove(); }); });

  DK.callouts($('#ch-anat'), [
    { n: 1, el: $('#an-chip .chip'), side: 'bottom', len: 40, at: 'start' },
    { n: 2, el: $('#an-chip .chip__icon'), side: 'top', len: 40, at: 'center' },
    { n: 3, el: $('#an-chip .chip__label'), side: 'bottom', len: 40, at: 'center' },
    { n: 4, el: $('#an-chip .chip__close'), side: 'top', len: 40, at: 'center' }]);
  renderPg();
'''

JS_SPEC = r'''
  DK.tokenTable($('#tok-table tbody'), [
    ['Frame', 'Enabled', 'border-primary'], ['Frame', 'Hover', 'border-hover'], ['Frame', 'Selected hover', 'border-selected-hover'],
    ['Surface', 'Selected', 'surface-opacity-black-10'], ['Text', 'Label', 'text-primary'], ['Icon', 'Leading and close icon', 'icon-primary'], ['Focus ring', 'Keyboard focus', 'border-focus']]);
'''

JS_CODE = r'''
  DK.recipes($('#recipes'), [
    ['Filter chips', '<div class="chip-group">\n  <button type="button" class="chip" aria-pressed="false">\n    <span class="chip__label">Gloves</span>\n    <span class="chip__close" aria-hidden="true">close</span>\n  </button>\n  <button type="button" class="chip" aria-pressed="true">\n    <span class="chip__label">Workwear</span>\n    <span class="chip__close" aria-hidden="true">close</span>\n  </button>\n</div>'],
    ['Small, with a leading icon', '<button type="button" class="chip chip--sm" aria-pressed="false">\n  <span class="chip__icon" aria-hidden="true">assignment_turned_in</span>\n  <span class="chip__label">Chip label</span>\n  <span class="chip__close" aria-hidden="true">close</span>\n</button>'],
    ['Removable', '<button type="button" class="chip chip--removable" aria-label="Remove anna@example.com">\n  <span class="chip__label">anna@example.com</span>\n  <span class="chip__close" aria-hidden="true">close</span>\n</button>\n<script>\n  document.addEventListener(\'chip:remove\', function (e) { e.target.remove(); });\n<\/script>']
  ]);
  DK.printCss($('#css-code'), 'chip', [[/^ {4}/gm, '']]);
'''

C = dict(
    slug=SLUG, title='Chip', eyebrow='Components · Form',
    lead='A chip is a <strong>small, interactive element</strong> that represents an input, an attribute or an action, most often a filter the user can select and unselect.',
    lead_ex='Every example on this page is the real component, not a picture. Figma: ' + fig_link(FIGMA, 'Chip with states') + ' and ' + fig_link(FIGMA_B, 'Chip') + '.',
    lead_spec='Sizes, tokens, states and requirements. Values come from the live token package and from Figma: ' + fig_link(FIGMA, 'Chip with states') + '.',
    lead_code='How to add chips to a page. The files are <code>components/css/chip.css</code> and <code>components/js/chip.js</code>.',
    select_menu=False,
    css=['chip'], body_js=['../../components/js/chip.js'], style=STYLE, ex=ex, spec=spec, code=code, js_ex=JS_EX, js_spec=JS_SPEC, js_code=JS_CODE)

if __name__ == '__main__':
    emit(C)
