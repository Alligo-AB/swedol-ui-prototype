from build import *

FIGMA = 'https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=326-7714'
SLUG = 'tag'

STYLE = r'''    .pg-row { display: flex; flex-wrap: wrap; gap: 8px; align-items: center; }
    .pg-grid { display: grid; gap: 24px; grid-template-columns: minmax(0, 1fr); width: 100%; }
    @media (min-width: 769px) { .pg-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
    .pg-cell { display: flex; flex-direction: column; gap: 12px; align-items: flex-start; }
    .pg-cell > span:first-child { font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-tertiary); }
    .pg-grey { padding: 16px; background: var(--color-surface-raised-secondary); }'''


def tag(label, size='', white=False, remove=False, extra=''):
    cls = 'tag' + (' tag--sm' if size == 'sm' else '') + (' tag--white' if white else '') + (' tag--remove' if remove else '') + extra
    x = '<button type="button" class="tag__remove" aria-label="Remove %s"><span class="material-symbols-outlined" aria-hidden="true">close</span></button>' % label if remove else ''
    return '<span class="%s">%s%s</span>' % (cls, label, x)


playground = '<h2 class="ds-h2">Playground</h2>' + desc('Choose variant, size and state and the tag and its code update.') + \
    '<div class="ds-playground"><div class="ds-stage ds-stage--center" id="pg-stage"><div id="pg-host"></div></div><div class="ds-controls">' + \
    btn_group('pg-l-var', 'Variant', 'data-pg="variant"', [('grey', 'Grey', True), ('white', 'White', False)]) + \
    btn_group('pg-l-size', 'Size', 'data-pg="size"', [('md', 'Medium', True), ('sm', 'Small', False)]) + \
    btn_group('pg-l-state', 'State', 'data-pg="state"', [('default', 'Default', True), ('remove', 'Remove', False)]) + \
    '</div></div><h3 class="ds-h3">Markup for this selection</h3>' + code_box('pg-code', 'HTML')

overview = '<h2 class="ds-h2">Overview</h2>' + desc('A tag shows an <strong>active filter</strong>: one value the user has chosen to filter a product list or a search result by. Tags are used for this only.') + \
    desc('Tag has two variants (Grey and White), two sizes (Medium and Small) and two states: Remove, the normal state, with a × button that removes the filter, and Default, without ×, for an active filter that cannot be removed from the tag. Only the × is interactive; when it has keyboard focus, the whole tag gets a focus ring.') + \
    three_pages(SLUG, 'a tag', 'the values: tokens, sizes, measurements and requirements', 'how to add one to a page')

usage = '<h2 class="ds-h2">Usage</h2><h3 class="ds-h3 ds-group">When to use</h3>' + desc('Use a tag only to <strong>show the active filters</strong> above a product list or a search result. Each chosen filter value is one tag, labelled with the category or value name. The × removes that one filter and the list updates at once.') + \
    fig_one('<div class="pg-row">' + tag('Gloves', remove=True) + tag('Workwear', remove=True) + tag('Safety shoes', remove=True) + '</div>', 'Active filters above a product list. Each × removes one filter.') + \
    '<h3 class="ds-h3 ds-group">Active filters</h3>' + bullets(['Place: the row of tags directly above the result list', 'Label: the category or value name only, as in the filter (“Gloves”, not “Category: Gloves”) unless two filters share a value name', 'Order: the order the filters were chosen', '<strong>Clear filters</strong>: a link at the end of the row when two or more filters are active', 'Size: Medium; Small in dense places such as a filter drawer', 'Variant: Grey on white, White on a grey surface', 'State: Remove; Default only for a filter that cannot be removed from the tag']) + \
    '<h3 class="ds-h3 ds-group">When not to use</h3><h3 class="ds-h3">For categories or labels on content</h3>' + desc('Tags are not used to show the category of an article or a product. Show that as text or a link.') + \
    '<h3 class="ds-h3">For a status</h3>' + desc('A status, a count or a marker such as “New” or “In progress” is a ' + link_large('badge.html', 'Badge') + '.') + \
    '<h3 class="ds-h3">For choosing a filter</h3>' + desc('The user chooses filter values with a ' + link_large('checkbox.html', 'Checkbox') + ' (or a checkbox tile) in the filter panel. The tag only shows what is chosen.') + \
    '<h3 class="ds-h3">For an action</h3>' + desc('A tag does not navigate or submit. Use a ' + link_large('button.html', 'Button') + ' or a ' + link_large('action-link.html', 'link') + ' for an action. The only action on a tag is the ×.') + \
    fig_pair('<div class="pg-row">' + tag('Gloves', remove=True) + tag('Workwear', remove=True) + '</div>', 'Do use tags for the active filters.', '<div class="pg-row">' + tag('Save') + tag('Delete') + '</div>', 'Do not use a tag as a button.') + \
    '<h3 class="ds-h3">Keep labels short</h3>' + desc('One or two words, as in the filter. A tag never wraps to a second line.') + \
    '<h3 class="ds-h3 ds-group">Quick reference</h3>' + \
    table(['The user…', 'Use'], [['sees a filter they have chosen and can remove', 'Tag, Remove state'], ['chooses a value to filter by', 'Checkbox or checkbox tile (<code>eco-checkbox</code>)'], ['sees a status, count or marker', '<code>eco-badge</code>'], ['sees the category of an article or product', 'Text or a link, not a tag']]) + \
    rules(['Use tags only for the active filters.', 'Keep the label short: the value name as in the filter.', 'Give the × a label that names the filter: “Remove Gloves”.', 'Use the same size for every tag in a row.'],
          ['Use a tag for categories or labels on content.', 'Use a tag as a button or a link, or for a status.', 'Make the whole tag clickable to remove it: only the × removes.', 'Mix Medium and Small in one row.'])

anatomy = '<h2 class="ds-h2">Anatomy</h2><h3 class="ds-h3 ds-group">Tag with Remove</h3>' + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout" id="tg-anat" role="img" aria-label="Anatomy of a tag: 1 container, 2 label, 3 remove button"><div class="ds-callout__art"><span class="tag tag--remove" id="an-tag"><span id="an-label">Gloves</span><button type="button" class="tag__remove" id="an-x" tabindex="-1" aria-hidden="true"><span class="material-symbols-outlined">close</span></button></span></div></div></figure></div>' + \
    ol_parts([('Container', 'Grey or White surface, sharp corners, no border.'), ('Label', '14/14 Breuer Condensed Bold, normal case, never wraps.'), ('Remove button (optional)', 'A <code>close</code> icon in a real <code>&lt;button&gt;</code>. Only in the Remove state.')])

variants = '<h2 class="ds-h2">Variants</h2>' + desc('Two variants, each in Default and Remove.') + \
    '<h3 class="ds-h3 ds-group">Grey</h3>' + desc('The default. Use it on white surfaces.') + \
    fig_one('<div class="pg-row">' + tag('Tag') + tag('Tag', remove=True) + tag('Tag', 'sm') + tag('Tag', 'sm', remove=True) + '</div>') + \
    '<h3 class="ds-h3 ds-group">Focus</h3>' + desc('When the × has keyboard focus, a 2px focus ring is drawn around the whole tag, 2px outside it: the tag is the filter the × removes. A mouse click shows no ring.') + fig_one('<div class="pg-row">' + tag('Gloves', remove=True, extra='" data-state="focus') + tag('Gloves', 'sm', remove=True, extra='" data-state="focus') + '</div>') + '<h3 class="ds-h3 ds-group">White</h3>' + desc('Use it on grey surfaces, such as Surface Raised Secondary.') + \
    fig_one('<div class="pg-row pg-grey">' + tag('Tag', white=True) + tag('Tag', white=True, remove=True) + tag('Tag', 'sm', white=True) + tag('Tag', 'sm', white=True, remove=True) + '</div>')

sizes = '<h2 class="ds-h2">Sizes</h2>' + desc('Medium is the default; Small is for dense places such as a filter drawer. The text is 14px in both. The values are under ' + sec_link(SLUG, 'sizes', 'Sizes') + ' in Specifications.') + \
    fig_one('<div class="pg-grid"><div class="pg-cell"><span>Medium</span><div class="pg-row">' + tag('Tag') + tag('Tag', remove=True) + '</div></div><div class="pg-cell"><span>Small</span><div class="pg-row">' + tag('Tag', 'sm') + tag('Tag', 'sm', remove=True) + '</div></div></div>')

layout = '<h2 class="ds-h2">Layout &amp; Appearance</h2><h3 class="ds-h3 ds-group">Groups of tags</h3>' + desc('Put tags in a wrapping flex row with an 8px gap (<code>space-8</code>). The tag is as wide as its label.') + \
    '<h3 class="ds-h3 ds-group">Appearance</h3>' + desc('Sharp corners and no border, like every ECO surface. Grey is a 10% black overlay, so it works on any light surface. Token names and values are under ' + sec_link(SLUG, 'design-tokens', 'Design Tokens') + ' in Specifications.')

behavior = '<h2 class="ds-h2">Behavior</h2>' + desc('The tag itself is not interactive: no hover and no click. In the Remove state the × is a button; when it has keyboard focus the focus ring is drawn around the whole tag. The ×: a click or Enter/Space removes the tag, and focus moves to the next tag, or to the previous one when it was the last.') + \
    '<h3 class="ds-h3 ds-group">Breakpoints</h3>' + desc('Only the gap between the label and the × changes: 6px below 769px and 8px from 769px (Medium Remove). Everything else is the same on every breakpoint.') + \
    fig_one('<div class="pg-row" id="rm-demo">' + tag('Gloves', remove=True) + tag('Safety shoes', remove=True) + tag('Hand tools', remove=True) + '</div>', 'Try it: remove a tag with the mouse or the keyboard.')

access = '<h2 class="ds-h2">Accessibility</h2>' + desc('All requirements are listed under ' + sec_link(SLUG, 'accessibility-requirements', 'Accessibility Requirements') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Keyboard support</h3>' + table(['Key', 'Action'], [['Tab', 'Moves focus to the next × button; the focus ring is drawn around its tag. A tag without × is skipped.'], ['Enter / Space', 'Removes the tag.']]) + \
    '<h3 class="ds-h3 ds-group">Screen reader support</h3>' + desc('The label is plain text. The × has an <code>aria-label</code> that names the tag, for example “Remove Gloves”; the icon is <code>aria-hidden</code>.')

related = '<h2 class="ds-h2">Related</h2><ul class="ds-bullets"><li><strong>' + link_large('badge.html', 'Badge') + '</strong>. A status, count or marker, never interactive.</li><li><strong>' + link_large('checkbox.html', 'Checkbox') + '</strong>. Choosing filter values, including the tile variants.</li><li><strong>' + link_large('button.html', 'Button') + '</strong>. For actions.</li></ul>'

references = '<h2 class="ds-h2">References</h2>' + refs([
    ('https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html', 'WCAG 2.2: Name, Role, Value', 'Success criterion 4.1.2: the × needs an accessible name.'),
    ('https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html', 'WCAG 2.2: Focus Order', 'Success criterion 2.4.3: where focus goes after a tag is removed.'),
    ('https://carbondesignsystem.com/components/tag/usage/', 'Carbon Design System: Tag', 'IBM.'),
    ('https://atlassian.design/components/tag/examples', 'Atlassian Design System: Tag', 'Atlassian.')])

ex = [('playground', playground), ('overview', overview), ('usage', usage), ('anatomy', anatomy), ('variants', variants), ('sizes', sizes), ('layout', layout), ('behavior', behavior), ('accessibility', access), ('related', related), ('references', references)]

# ---------------------------------------------------------------- Specifications
st_tok = '<h2 class="ds-h2">Design Tokens</h2>' + desc('Resolved from the live token package.') + \
    '<div class="ds-table-wrap"><table class="ds-table" id="tok-table"><thead><tr><th scope="col">Part</th><th scope="col">Use</th><th scope="col">Token</th><th scope="col">Value</th></tr></thead><tbody></tbody></table></div>' + \
    note('Figma binds <code>border-secondary</code> to the White tag, but with a border width of 0, so no border is drawn.')

st_sizes = '<h2 class="ds-h2">Sizes</h2>' + table(['Size', 'State', 'Height', 'Padding (top right bottom left)', 'Gap', 'Icon'], [
    ['Medium', 'Default', '32px', '9 12 9 12', '–', '–'], ['Medium', 'Remove', '32px (fixed, <code>space-32</code>)', '8 8 8 12', '6px mobile, 8px from 769px', '16px'],
    ['Small', 'Default', '24px', '5 8 5 8', '–', '–'], ['Small', 'Remove', '24px', '4 6 4 8', '4px', '16px']]) + \
    note('Values from Figma. Medium is 32px in both states; Medium Remove has a fixed height (<code>space-32</code>) around 8px padding. The × icon is 16px in both sizes.')

def mfig(n, name, html):
    return ('<div class="measure__item"><span class="measure__name">%d · %s</span><div class="measure__obj">%s'
            '<i class="measure__pad measure__pad--t"></i><i class="measure__pad measure__pad--b"></i><i class="measure__pad measure__pad--l"></i><i class="measure__pad measure__pad--r"></i>'
            '<b class="measure__dim measure__dim--v measure__dim--t"><span></span></b><b class="measure__dim measure__dim--v measure__dim--b"><span></span></b><b class="measure__dim measure__dim--h measure__dim--l"><span></span></b><b class="measure__dim measure__dim--h measure__dim--r"><span></span></b></div></div>') % (n, name, html)

def msub(size, remove):
    return tag('Tag', size, remove=remove, extra=' measure__subject').replace('class="tag__remove"', 'class="tag__remove" tabindex="-1"')

st_meas = '<h2 class="ds-h2">Measurements</h2>' + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-fig__stage--flush" style="padding:0;min-height:0"><div class="measure" role="img" aria-label="Padding of the tag in four configurations" style="--k:3">' + \
    mfig(1, 'Medium', msub('', False)) + mfig(2, 'Medium, Remove', msub('', True)) + mfig(3, 'Small', msub('sm', False)) + mfig(4, 'Small, Remove', msub('sm', True)) + \
    '</div></div><figcaption class="ds-fig__cap">The tag at 3× size. The numbers are read from the component and are real pixels.</figcaption></figure></div>' + \
    '<h3 class="ds-h3 ds-group">Spacing</h3>' + table(['Part', 'Value'], [['Gap between label and × (Medium)', '6px below 769px, <code>space-8</code> from 769px'], ['Gap between label and × (Small)', '<code>space-4</code>'], ['Gap between tags in a row', '<code>space-8</code>, set on the parent']]) + \
    note('9px, 6px and 5px have no spacing token; they are as drawn in Figma and written with a comment in <code>tag.css</code>.')

st_states = '<h2 class="ds-h2">States</h2>' + table(['State', 'Container', 'Label', 'Icon', 'Notes'], [
    ['Default, Grey', '<code>surface-opacity-black-10</code>', '<code>text-primary</code>', '–', 'Not interactive.'],
    ['Default, White', '<code>surface-action-2</code>', '<code>text-primary</code>', '–', 'Not interactive.'],
    ['Remove, Grey', '<code>surface-opacity-black-10</code>', '<code>text-primary</code>', '<code>close</code>, <code>icon-primary</code>', 'The × is a button.'],
    ['Remove, White', '<code>surface-action-2</code>', '<code>text-primary</code>', '<code>close</code>, <code>icon-primary</code>', 'The × is a button.'],
    ['Focus (× has keyboard focus)', '2px <code>border-focus</code> ring around the whole tag, 2px offset', '<code>text-primary</code>', 'No own ring', 'Only on <code>:focus-visible</code>, not on a mouse click.']]) + \
    note('Figma has no focus or hover state yet. The focus ring uses the same token, width and offset as the other ECO components; a hover state is open for design.')

st_typo = '<h2 class="ds-h2">Typography</h2>' + table(['Part', 'Font', 'Size / line height', 'Letter spacing', 'Weight', 'Case'], [['Label', 'Breuer Condensed', '14/14', '0.28px', '600 (Figma Bold)', 'Normal']]) + \
    note('No ECO text style is 14/14 with 0.28px letter spacing (Label Large mobile and Alt-Label Small are 14/14 with 0.56px, uppercase). Flagged for design. The same on every breakpoint.')

st_struct = '<h2 class="ds-h2">Structure</h2>' + table(['Element', 'Class', 'Notes'], [
    ['Container', '<code>tag</code>', 'A <code>span</code>: Medium, Grey.'], ['Variant', '<code>tag--white</code>', 'White surface.'], ['Size', '<code>tag--sm</code>', 'Small.'],
    ['State', '<code>tag--remove</code>', 'Padding for the ×.'], ['Remove button', '<code>tag__remove</code>', 'A <code>button</code> with <code>aria-label</code> and a <code>close</code> Material Symbol.']])

st_behavior = '<h2 class="ds-h2">Behavior</h2>' + table(['Topic', 'Result'], [['Input', 'Only the × reacts: click, Enter or Space removes the tag.'], ['Focus after removing', 'The next ×, or the previous one when it was the last.'], ['Breakpoint', 'Medium Remove gap: 6px below 769px, 8px from 769px.'], ['Motion', 'None.']])

st_access = '<h2 class="ds-h2">Accessibility Requirements</h2>' + table(['Topic', 'Requirement'], [
    ['Semantics', 'The tag is text, never a <code>button</code> or a link. The × is a native <code>&lt;button type="button"&gt;</code>.'], ['Name', 'The × has <code>aria-label="Remove &lt;label&gt;"</code> (WCAG 4.1.2).'],
    ['Focus', 'When the × has <code>:focus-visible</code>, a ring is drawn around the whole tag (WCAG 2.4.7). After removing, focus moves to a neighbour, never to the page start (WCAG 2.4.3).'], ['Target size', 'The × is 16px. Leave space around it, so the target with its spacing reaches 24×24px (WCAG 2.5.8).']])

spec = [('design-tokens', st_tok), ('sizes', st_sizes), ('measurements', st_meas), ('states', st_states), ('typography', st_typo), ('structure', st_struct), ('behavior', st_behavior), ('accessibility-requirements', st_access)]

# ---------------------------------------------------------------- Code
c_basic = '<h2 class="ds-h2">Basic Usage</h2>' + desc('Link the shared stylesheet once per page. Never copy the rules into a page.') + table(['Step', 'What to do'], [
    ['1. Link', '<code>&lt;link rel="stylesheet" href="/components/css/tag.css"&gt;</code>. Both templates already have it.'], ['2. Tag', 'A <code>span.tag</code> with the label.'],
    ['3. Variant and size', 'Add <code>tag--white</code> and/or <code>tag--sm</code>.'], ['4. Remove', 'Add <code>tag--remove</code> and a <code>button.tag__remove</code> after the label. Your script removes the tag and moves focus.']])
c_tag = '<h2 class="ds-h2">Tag</h2>' + desc('Copy the markup you need.') + '<div id="recipes"></div>'
c_api = '<h2 class="ds-h2">API</h2><h3 class="ds-h3 ds-group">Classes</h3>' + table(['Class', 'Use'], [['<code>tag</code>', 'The tag: Medium, Grey.'], ['<code>tag--white</code>', 'White surface, for grey backgrounds.'], ['<code>tag--sm</code>', 'Small.'], ['<code>tag--remove</code>', 'Remove state: padding for the ×.'], ['<code>tag__remove</code>', 'The × button.']]) + \
    '<h3 class="ds-h3 ds-group">Things to know</h3>' + bullets(['There is no shared script: removing a tag is page logic.', 'Put tags in a flex row with <code>gap: var(--dimension-spacing-space-8)</code> and <code>flex-wrap: wrap</code>.', 'The class <code>ds-tag</code> belongs to the docs pages; it is not this component.'])
c_css = '<h2 class="ds-h2">CSS / Tailwind</h2>' + desc('The component is one CSS file, shared by every page. Link it, never copy it. The CSS below is read from the file the page links, so it is always what you see.') + code_box('css-code', 'CSS (components/css/tag.css)')
code = [('basic-usage', c_basic), ('tag', c_tag), ('api', c_api), ('css-tailwind', c_css, False)]

# ---------------------------------------------------------------- scripts
JS_REMOVE = r'''
  /* Remove: click or Enter/Space on the ×; focus moves to the next ×, else the previous one */
  document.addEventListener('click', function (e) {
    var x = e.target.closest('#rm-demo .tag__remove'); if (!x) return;
    var t = x.closest('.tag'), all = $$('#rm-demo .tag__remove'), i = all.indexOf(x), next = all[i + 1] || all[i - 1];
    t.remove(); if (next) next.focus();
  });
'''

JS_EX = r'''
  var pg = { variant: 'grey', size: 'md', state: 'default' };
  function renderPg() {
    var cls = 'tag' + (pg.size === 'sm' ? ' tag--sm' : '') + (pg.variant === 'white' ? ' tag--white' : '') + (pg.state === 'remove' ? ' tag--remove' : '');
    var html = '<span class="' + cls + '">Gloves' + (pg.state === 'remove' ? '<button type="button" class="tag__remove" aria-label="Remove Gloves"><span class="material-symbols-outlined" aria-hidden="true">close</span></button>' : '') + '</span>';
    $('#pg-host').innerHTML = html;
    $('#pg-stage').style.background = pg.variant === 'white' ? 'var(--color-surface-raised-secondary)' : '';
    $('#pg-code').textContent = html.replace('Gloves<button', 'Gloves\n  <button').replace('</button></span>', '</button>\n</span>');
  }
  DK.wire(pg, renderPg);
  DK.callouts($('#tg-anat'), [{ n: 1, el: $('#an-tag'), side: 'bottom', len: 32, at: 'start' }, { n: 2, el: $('#an-label'), side: 'top', len: 32, at: 'center' }, { n: 3, el: $('#an-x'), side: 'right', len: 32, at: 'center' }]);
  renderPg();
''' + JS_REMOVE

JS_SPEC = r'''
  DK.tokenTable($('#tok-table tbody'), [
    ['Container, Grey', 'Default background', 'surface-opacity-black-10'], ['Container, White', 'On grey surfaces', 'surface-action-2'],
    ['Label', 'Text', 'text-primary'], ['× icon', 'Remove button', 'icon-primary'], ['Focus', 'Ring around the tag', 'border-focus']]);
'''

JS_CODE = r'''
  DK.recipes($('#recipes'), [
    ['Default', '<span class="tag">Gloves</span>\n<span class="tag tag--sm">Gloves</span>\n<span class="tag tag--white">Gloves</span>'],
    ['Remove', '<span class="tag tag--remove">Gloves\n  <button type="button" class="tag__remove" aria-label="Remove Gloves"><span class="material-symbols-outlined" aria-hidden="true">close</span></button>\n</span>'],
    ['A group of tags', '<div style="display: flex; flex-wrap: wrap; gap: var(--dimension-spacing-space-8)">\n  <span class="tag">Workwear</span>\n  <span class="tag">Safety</span>\n</div>']
  ]);
  DK.printCss($('#css-code'), 'tag', [[/^ {4}/gm, ''], [/:is\(:has\(\.tag__remove:focus-visible\), \[data-state="focus"\]\)/g, ':has(.tag__remove:focus-visible)']]);
'''

C = dict(
    slug=SLUG, title='Tag', eyebrow='Components · Status and navigation', eyebrow_extra='<span class="badge-basic badge-basic--warning badge-basic--weak">In progress</span>',
    lead='A tag shows an <strong>active filter</strong> above a product list or a search result. Its × button removes the filter.',
    lead_ex='Every example on this page is the real component, not a picture. Figma: ' + fig_link(FIGMA, 'Tag') + '.',
    lead_spec='Tokens, sizes, measurements, states and requirements. Values come from the live token package and from Figma: ' + fig_link(FIGMA, 'Tag') + '.',
    lead_code='How to add a tag to a page. The file is <code>components/css/tag.css</code>.',
    select_menu=False,
    css=['tag'], style=STYLE, ex=ex, spec=spec, code=code, js_ex=JS_EX, js_spec=JS_SPEC, js_code=JS_CODE)

if __name__ == '__main__':
    emit(C)
