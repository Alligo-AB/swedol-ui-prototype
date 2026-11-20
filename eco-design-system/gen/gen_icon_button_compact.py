from build import *

FIGMA = 'https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=23990-132193'
SLUG = 'icon-button-compact'

STYLE = r'''    .pg-states { display: grid; gap: 24px 32px; grid-template-columns: repeat(2, max-content); align-items: center; justify-content: center; }
    @media (min-width: 769px) { .pg-states { grid-template-columns: repeat(4, max-content); } }
    .pg-cell { display: flex; flex-direction: column; align-items: flex-start; gap: 12px; }
    .pg-cell > span:first-child { font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-tertiary); }
    .ibc-row { display: flex; flex-wrap: wrap; gap: 24px 32px; align-items: center; justify-content: center; }'''

ON = '<svg class="icon %s icon-btn-compact__on" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M8 19.6501L6.95 18.5751L9.775 15.7501H2.25V14.2501H9.775L6.95 11.4251L8 10.3501L12.65 15.0001L8 19.6501ZM16 13.6501L11.35 9.0001L16 4.3501L17.05 5.4251L14.225 8.2501H21.75V9.7501H14.225L17.05 12.5751L16 13.6501Z"/><path d="M22 20.0001C22 22.2093 20.2091 24.0001 18 24.0001C15.7909 24.0001 14 22.2093 14 20.0001C14 17.791 15.7909 16.0001 18 16.0001C20.2091 16.0001 22 17.791 22 20.0001Z"/><path d="M17.1347 22.0001L15.3333 20.2465L15.9235 19.6747L17.1347 20.8377L20.0765 18.0001L20.6667 18.5813L17.1347 22.0001Z" fill="white"/></svg>'


def ib(icon='favorite', label='Favourite', large=False, state=None, pressed=None, fill=False, on_icon=False, extra='', on_font=None):
    sz = 'icon--md' if large else 'icon--sm'
    c = 'icon-btn-compact' + (' icon-btn-compact--fill-hover' if fill else '') + extra
    a = (' data-state="%s"' % state) if state else ''
    a += (' aria-pressed="%s"' % pressed) if pressed is not None else ''
    inner = '<span class="icon %s%s" aria-hidden="true">%s</span>' % (sz, ' icon-btn-compact__off' if (on_icon or on_font) else '', icon)
    if on_icon:
        inner += ON % sz
    if on_font:
        inner += '<span class="icon %s icon-btn-compact__on" aria-hidden="true">%s</span>' % (sz, on_font)
    return '<button type="button" class="%s"%s aria-label="%s">%s</button>' % (c, a, label, inner)


def fav(**k): return ib('favorite', 'Favourite', fill=True, **k)
def cmp(**k): return ib('compare_arrows', 'Compare', on_icon=True, **k)
def favlist(**k): return ib('favorite', 'Add to list', fill=True, on_font='edit', **k)
def edit(**k): return ib('edit', 'Edit', fill=True, **k)


def states_row(maker, large):
    cells = [('Enabled', maker(large=large, pressed='false')), ('Hover', maker(large=large, state='hover', pressed='false')), ('Selected', maker(large=large, pressed='true')), ('Selected hover', maker(large=large, state='selected-hover', pressed='true'))]
    return '<div class="pg-states">' + ''.join('<div class="pg-cell"><span>%s</span>%s</div>' % (n, h) for n, h in cells) + '</div>'


ICONS = [('compare_arrows', 'Compare'), ('favorite', 'Favourite'), ('edit', 'Edit'), ('close', 'Close'), ('cancel', 'Clear'), ('location_on', 'Location'), ('qr_code_scanner', 'Scan'), ('list_alt', 'List selected')]

playground = '<h2 class="ds-h2">Playground</h2>' + desc('Choose icon and size, then click the button. The button and its code update.') + \
    '<div class="ds-playground"><div class="ds-stage ds-stage--center" id="pg-stage"><div id="pg-host"></div></div><div class="ds-controls">' + \
    sel('pg-l-icon', 'pg-s-icon', 'Icon', 'icon', [('favorite', 'Favourite'), ('favorite_list', 'Favourite to list'), ('compare_arrows', 'Compare'), ('edit', 'Edit'), ('close', 'Close'), ('location_on', 'Location'), ('qr_code_scanner', 'Scan')], 'favorite') + \
    btn_group('pg-l-size', 'Size', 'data-pg="size"', [('sm', 'Small (20px)', True), ('lg', 'Large (24px)', False)]) + \
    '</div></div><h3 class="ds-h3">Markup for this selection</h3>' + code_box('pg-code', 'HTML')

overview = '<h2 class="ds-h2">Overview</h2>' + desc('A compact icon button is a <strong>frameless, icon-only button</strong> that is as big as its icon: 20px (Small) or 24px (Large). It is for places where the regular icon button (40px, with padding) is too big: a product card, a table row, a field.') + \
    desc('It has four states: enabled, hover, selected and selected hover. A toggle such as favourite, compare, favourite to list or edit keeps its selected state with <code>aria-pressed</code>. Size is the same on every breakpoint.') + \
    three_pages(SLUG, 'a compact icon button', 'sizes, tokens, states and requirements', 'how to add one to a page')

usage = '<h2 class="ds-h2">Usage</h2><h3 class="ds-h3 ds-group">When to use</h3>' + \
    bullets(['For an icon-only action on a small surface: compare and favourite on a product card.', 'Inside a field or a list row: clear, edit, location, scan.', 'For a toggle that shows its state by changing the icon: favourite (outline to solid) and compare (arrows to added).']) + \
    '<h3 class="ds-h3 ds-group">When not to use</h3>' + \
    table(['The user…', 'Use instead'], [['starts the main action on the page', link_large('button.html', 'Button')], ['needs a larger icon button (40px or 48px)', link_large('button.html', 'Button') + ' with <code>btn--icon</code>'], ['follows a link with a text label', link_large('action-link.html', 'Action link')], ['switches between two views', link_large('segment-control.html', 'Pill segment control')]]) + \
    '<h3 class="ds-h3 ds-group">Name it</h3>' + desc('There is no text, so every compact icon button needs an <code>aria-label</code>, and a tooltip (<code>data-tooltip</code>) so sighted users learn what it does.') + \
    rules(['Give it an <code>aria-label</code> and a tooltip.', 'Use <code>aria-pressed</code> when it is a toggle.', 'Keep 12px between two compact icon buttons in a row.'],
          ['Use it for the main action: use a button.', 'Use it when there is room for a regular icon button.', 'Put a background or border in the component: a page may put it on a surface, the component stays frameless.'])

variants = '<h2 class="ds-h2">Variants</h2>' + desc('Figma has one component set per icon. All have the same sizes and states. The icons are Material Symbols (outline; solid when selected).') + \
    fig_one('<div class="ibc-row">' + ''.join(ib(i, l) for i, l in ICONS) + '</div>') + \
    '<h3 class="ds-h3 ds-group">Close, with a surface on hover</h3>' + desc('Close has no selected state. A surface appears on hover instead (<code>icon-btn-compact--surface-hover</code>): the button is 24px, a 20px icon with 2px around it. On a dark surface add <code>icon-btn-compact--inverted</code>.') + \
    fig_one('<div class="ibc-row">' + ib('close', 'Close', extra=' icon-btn-compact--surface-hover') + ib('close', 'Close', state='hover', extra=' icon-btn-compact--surface-hover') + '</div>') + \
    fig_one('<div class="ibc-row">' + ib('close', 'Close', extra=' icon-btn-compact--surface-hover icon-btn-compact--inverted') + ib('close', 'Close', state='hover', extra=' icon-btn-compact--surface-hover icon-btn-compact--inverted') + '</div>', stage_cls='ds-stage--dark') + \
    '<h3 class="ds-h3 ds-group">Toggles</h3>' + desc('Four buttons keep a selected state with <code>aria-pressed</code>. Favourite and edit turn solid. Compare changes to the custom icon <code>compare_added_custom</code> (arrows with a check). Favourite to list changes to the solid <code>edit</code> icon: first it adds the product to a list, then it edits the list.') + \
    fig_one('<div class="ibc-row">' + fav(pressed='false') + fav(pressed='true') + cmp(pressed='false') + cmp(pressed='true') + favlist(pressed='false') + favlist(pressed='true') + edit(pressed='false') + edit(pressed='true') + '</div>')

sizes = '<h2 class="ds-h2">Sizes</h2>' + desc('Small (20px) and Large (24px). The values are under ' + sec_link(SLUG, 'sizes', 'Sizes') + ' in Specifications.') + \
    fig_one('<div class="ibc-row">' + fav(pressed='false') + fav(large=True, pressed='false') + '</div>')

states = '<h2 class="ds-h2">States</h2>' + desc('Hover turns the icon grey. A selected icon is solid. On a favourite, hover also fills the heart, but keeps the colour. Keyboard focus shows the ECO focus ring.') + \
    '<h3 class="ds-h3 ds-group">Favourite, Small</h3>' + fig_one(states_row(fav, False)) + '<h3 class="ds-h3 ds-group">Compare, Small</h3>' + fig_one(states_row(cmp, False)) + \
    '<h3 class="ds-h3 ds-group">Favourite to list, Small</h3>' + fig_one(states_row(favlist, False)) + '<h3 class="ds-h3 ds-group">Edit, Small</h3>' + fig_one(states_row(edit, False)) + \
    '<h3 class="ds-h3 ds-group">Favourite, Large</h3>' + fig_one(states_row(fav, True))

behavior = '<h2 class="ds-h2">Behavior</h2>' + bullets(['A toggle flips <code>aria-pressed</code> on click or <kbd>Space</kbd>/<kbd>Enter</kbd>. The page script does it; the component has no script.', 'The size is the same on every breakpoint.', 'The click area equals the icon. Keep space around it so a finger does not hit its neighbour.'])

access = '<h2 class="ds-h2">Accessibility</h2>' + desc('All requirements are listed under ' + sec_link(SLUG, 'accessibility-requirements', 'Accessibility Requirements') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Keyboard support</h3>' + table(['Key', 'Action'], [['<kbd>Tab</kbd>', 'Moves the focus to the next button.'], ['<kbd>Space</kbd>, <kbd>Enter</kbd>', 'Runs the action, or flips a toggle.']]) + \
    '<h3 class="ds-h3 ds-group">Screen reader support</h3>' + desc('A native <code>&lt;button&gt;</code> named by <code>aria-label</code>. A toggle is read as pressed or not pressed. The icon is hidden from screen readers.')

related = '<h2 class="ds-h2">Related</h2><ul class="ds-bullets"><li><strong>' + link_large('button.html', 'Button') + '</strong>. The regular icon button (<code>btn--icon</code>, 40px and 48px).</li><li><strong>' + link_large('action-link.html', 'Action link') + '</strong>. A link with a text label and an icon.</li><li><strong>' + link_large('icon.html', 'Icon') + '</strong>. Icon names, sizes and the library.</li><li><strong>' + link_large('tooltip.html', 'Tooltip') + '</strong>. Names the button.</li></ul>'

references = '<h2 class="ds-h2">References</h2>' + refs([
    ('https://www.w3.org/WAI/ARIA/apg/patterns/button/', 'WAI-ARIA Authoring Practices: Button', 'Toggle buttons and aria-pressed.'),
    ('https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html', 'WCAG 2.2: Target Size (Minimum)', 'Success criterion 2.5.8: 24 by 24px.')])

ex = [('playground', playground), ('overview', overview), ('usage', usage), ('variants', variants), ('sizes', sizes), ('states', states), ('behavior', behavior), ('accessibility', access), ('related', related), ('references', references)]

st_tok = '<h2 class="ds-h2">Design Tokens</h2>' + desc('Resolved from the live token package.') + \
    '<div class="ds-table-wrap"><table class="ds-table" id="tok-table"><thead><tr><th scope="col">Part</th><th scope="col">Use</th><th scope="col">Token</th><th scope="col">Value</th></tr></thead><tbody></tbody></table></div>'
st_sizes = '<h2 class="ds-h2">Sizes</h2>' + table(['Size', 'Icon class', 'Button size'], [['Small', '<code>icon--sm</code>', '20 × 20px'], ['Large', '<code>icon--md</code>', '24 × 24px']]) + \
    note('No padding, border or background. The size is the same on every breakpoint. The click area equals the icon (20px is below the 24px minimum of WCAG 2.5.8; Figma has no larger area, so keep 12px between buttons).')
st_states = '<h2 class="ds-h2">States</h2>' + table(['State', 'Icon', 'Color'], [
    ['Enabled', 'Outline', '<code>text-action-primary</code>'], ['Hover', 'Outline (solid on a favourite)', '<code>text-action-primary-hover</code>; favourite: <code>text-action-primary</code>'],
    ['Selected', 'Solid (compare: <code>compare_added_custom</code>; favourite to list: <code>edit</code>)', '<code>text-action-primary</code>'], ['Selected hover', 'Solid', '<code>text-action-primary-hover</code>'], ['Hover, <code>--surface-hover</code> (close)', 'Same', '<code>icon-primary</code> on <code>surface-opacity-black-05</code>; inverted: <code>icon-inverted</code> on <code>surface-opacity-white-20</code>'],
    ['Focus (keyboard)', 'Same', 'Plus a 2px <code>border-focus</code> ring, 2px out']]) + \
    note('Figma has no disabled state. Hide a button that cannot be used.')
st_struct = '<h2 class="ds-h2">Structure</h2>' + table(['Element', 'Class', 'Notes'], [
    ['Button', '<code>icon-btn-compact</code>', 'A <code>&lt;button type="button"&gt;</code> with <code>aria-label</code>. A toggle: add <code>aria-pressed</code>.'],
    ['Icon', '<code>icon icon--sm</code> / <code>icon--md</code>', 'Material Symbols (<code>components/css/icon.css</code>), <code>aria-hidden</code>.'],
    ['Fill on hover', '<code>icon-btn-compact--fill-hover</code>', 'Favourite: the outline icon turns solid on hover.'],
    ['Surface on hover', '<code>icon-btn-compact--surface-hover</code>', 'Close: 2px padding (24px), 5% black surface on hover, the icon keeps its colour. Add <code>icon-btn-compact--inverted</code> on a dark surface (white icon, 20% white surface).'],
    ['Own icon when selected', '<code>icon-btn-compact__off</code> + <code>icon-btn-compact__on</code>', 'Compare (custom SVG) and favourite to list (<code>edit</code>): both icons in the button; the second shows when selected.']])
st_access = '<h2 class="ds-h2">Accessibility Requirements</h2>' + table(['Topic', 'Requirement'], [
    ['Role', 'A native <code>&lt;button&gt;</code>. A toggle has <code>aria-pressed="true|false"</code>.'], ['Name', '<code>aria-label</code> (there is no text), plus a tooltip.'],
    ['Focus', 'Visible ring on <code>:focus-visible</code> (WCAG 2.4.7).'], ['Target size', 'The icon (20px or 24px). Keep 12px between buttons.'], ['Selected', 'Never only the icon: <code>aria-pressed</code> also says it.']])
spec = [('design-tokens', st_tok), ('sizes', st_sizes), ('states', st_states), ('structure', st_struct), ('accessibility-requirements', st_access)]

c_basic = '<h2 class="ds-h2">Basic Usage</h2>' + desc('Link the shared file once per page. Never copy the rules into a page.') + table(['Step', 'What to do'], [
    ['1. Link', '<code>&lt;link rel="stylesheet" href="/components/css/icon-button-compact.css"&gt;</code> (and <code>icon.css</code>). Both templates already have them.'],
    ['2. Button', 'A <code>button.icon-btn-compact</code> with <code>aria-label</code> and an <code>icon</code> span.'], ['3. Toggle', 'Add <code>aria-pressed="false"</code> and flip it in your script.']])
c_recipes = '<h2 class="ds-h2">Compact Icon Button</h2>' + desc('Copy the markup you need.') + '<div id="recipes"></div>'
c_api = '<h2 class="ds-h2">API</h2>' + table(['Class / attribute', 'Use'], [['<code>icon-btn-compact</code>', 'The button.'], ['<code>icon--sm</code> / <code>icon--md</code>', 'On the icon: 20px or 24px.'], ['<code>icon-btn-compact--fill-hover</code>', 'The icon turns solid on hover (favourite).'], ['<code>icon-btn-compact--surface-hover</code>', 'A surface on hover instead of a grey icon (close). 24px.'], ['<code>icon-btn-compact--inverted</code>', 'On a dark surface.'], ['<code>icon-btn-compact__off</code> / <code>__on</code>', 'Icon for the enabled and for the selected state.'], ['<code>aria-pressed</code>, <code>.is-on</code>', 'Selected state.']])
c_css = '<h2 class="ds-h2">CSS / Tailwind</h2>' + desc('The component is one CSS file, shared by every page. Link it, never copy it. The CSS below is read from the file the page links.') + code_box('css-code', 'CSS (components/css/icon-button-compact.css)')
code = [('basic-usage', c_basic), ('compact-icon-button', c_recipes), ('api', c_api), ('css-tailwind', c_css, False)]

JS_EX = r'''
  var pg = { icon: 'favorite', size: 'sm' };
  var NAMES = { favorite: 'Favourite', favorite_list: 'Add to list', compare_arrows: 'Compare', edit: 'Edit', close: 'Close', location_on: 'Location', qr_code_scanner: 'Scan' };
  var ON = %s;
  function markup() {
    var sz = pg.size === 'lg' ? 'icon--md' : 'icon--sm', tog = pg.icon === 'favorite' || pg.icon === 'favorite_list' || pg.icon === 'compare_arrows' || pg.icon === 'edit', fl = pg.icon === 'favorite_list', name = fl ? 'favorite' : pg.icon;
    var cls = 'icon-btn-compact' + (pg.icon === 'favorite' || fl || pg.icon === 'edit' ? ' icon-btn-compact--fill-hover' : '');
    var cmpOn = pg.icon === 'compare_arrows';
    return '<button type="button" class="' + cls + '"' + (tog ? ' aria-pressed="false"' : '') + ' aria-label="' + NAMES[pg.icon] + '">\n  <span class="icon ' + sz + (cmpOn || fl ? ' icon-btn-compact__off' : '') + '" aria-hidden="true">' + name + '</span>' + (fl ? '\n  <span class="icon ' + sz + ' icon-btn-compact__on" aria-hidden="true">edit</span>' : '') + (cmpOn ? '\n  <svg class="icon ' + sz + ' icon-btn-compact__on" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">…</svg>' : '') + '\n</button>';
  }
  function renderPg() {
    var m = markup(); $('#pg-code').textContent = m;
    var sz = pg.size === 'lg' ? 'icon--md' : 'icon--sm', cmpOn = pg.icon === 'compare_arrows';
    $('#pg-host').innerHTML = m.replace('…', '').replace(/<svg[\s\S]*?<\/svg>/, ON.replace('SZ', sz));
  }
  $('#pg-host').addEventListener('click', function (e) { var b = e.target.closest('[aria-pressed]'); if (b) b.setAttribute('aria-pressed', b.getAttribute('aria-pressed') !== 'true'); });
  DK.wire(pg, renderPg);
  $$('[data-state]').forEach(function (c) { c.setAttribute('tabindex', '-1'); c.style.pointerEvents = 'none'; });   /* forced-state demos are pictures */
  $$('.ds-fig [aria-pressed]:not([data-state])').forEach(function (b) { b.addEventListener('click', function () { b.setAttribute('aria-pressed', b.getAttribute('aria-pressed') !== 'true'); }); });
  renderPg();
''' % repr(ON % 'SZ')

JS_SPEC = r'''
  DK.tokenTable($('#tok-table tbody'), [
    ['Icon', 'Enabled, selected', 'text-action-primary'], ['Icon', 'Hover, selected hover', 'text-action-primary-hover'], ['Surface', 'Hover, close', 'surface-opacity-black-05'], ['Surface', 'Hover, close inverted', 'surface-opacity-white-20'], ['Icon', 'Close, close inverted', 'icon-primary, icon-inverted'], ['Focus ring', 'Keyboard focus', 'border-focus']]);
'''

JS_CODE = r'''
  DK.recipes($('#recipes'), [
    ['Action', '<button type="button" class="icon-btn-compact" aria-label="Edit" data-tooltip="Edit">\n  <span class="icon icon--sm" aria-hidden="true">edit</span>\n</button>'],
    ['Favourite (toggle)', '<button type="button" class="icon-btn-compact icon-btn-compact--fill-hover" aria-pressed="false" aria-label="Add to favourites" data-tooltip="Add to favourites">\n  <span class="icon icon--sm" aria-hidden="true">favorite</span>\n</button>\n<script>\n  document.addEventListener(\'click\', function (e) {\n    var b = e.target.closest(\'.icon-btn-compact[aria-pressed]\');\n    if (b) b.setAttribute(\'aria-pressed\', b.getAttribute(\'aria-pressed\') !== \'true\');\n  });\n<\/script>'],
    ['Compare (own icon when selected)', '<button type="button" class="icon-btn-compact" aria-pressed="false" aria-label="Compare" data-tooltip="Compare">\n  <span class="icon icon--sm icon-btn-compact__off" aria-hidden="true">compare_arrows</span>\n  <svg class="icon icon--sm icon-btn-compact__on" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">…compare_added_custom…</svg>\n</button>']
  ]);
  DK.printCss($('#css-code'), 'icon-button-compact', [[/^ {4}/gm, '']]);
'''

C = dict(
    slug=SLUG, title='Compact Icon Button', eyebrow='Components · Actions', eyebrow_extra='<span class="badge-basic badge-basic--warning badge-basic--weak">In progress</span>',
    lead='A compact icon button is a <strong>frameless, icon-only button</strong> as big as its icon (20px or 24px), for places too small for a regular icon button.',
    lead_ex='Every example on this page is the real component, not a picture. Figma: ' + fig_link(FIGMA, 'Compact Icon Button') + '.',
    lead_spec='Sizes, tokens, states and requirements. Values come from the live token package and from Figma: ' + fig_link(FIGMA, 'Compact Icon Button') + '.',
    lead_code='How to add a compact icon button to a page. The file is <code>components/css/icon-button-compact.css</code>.',
    select_menu=True, tooltip=True,
    css=['icon', 'icon-button-compact'], body_js=[], style=STYLE, ex=ex, spec=spec, code=code, js_ex=JS_EX, js_spec=JS_SPEC, js_code=JS_CODE)

if __name__ == '__main__':
    emit(C)
