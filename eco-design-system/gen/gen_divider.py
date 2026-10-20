from build import *

FIGMA = 'https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=894-27082'
FIGMA_G = 'https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=18282-2867'
SLUG = 'divider'

STYLE = r'''    .pg-note { font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-tertiary); }
    .pg-col { display: flex; flex-direction: column; gap: 16px; width: 100%; max-width: 360px; }
    .pg-row { display: flex; gap: 24px; height: 112px; align-items: stretch; justify-content: center; }
    .pg-cell { display: flex; flex-direction: column; gap: 12px; width: 100%; }
    .pg-cell > span:first-child { font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-tertiary); }
    .pg-grid { display: grid; gap: 32px 24px; grid-template-columns: minmax(0, 1fr); width: 100%; }
    @media (min-width: 769px) { .pg-grid { grid-template-columns: repeat(3, minmax(0, 1fr)); } }
    .pg-list { display: flex; flex-direction: column; gap: 16px; width: 100%; max-width: 360px; }
    .pg-inline { display: flex; align-items: center; gap: 16px; }
    .pg-ph { height: 48px; background: var(--color-surface-05); }'''

playground = '<h2 class="ds-h2">Playground</h2>' + desc('Choose direction and color and the divider and its code update.') + \
    '<div class="ds-playground"><div class="ds-stage ds-stage--center" id="pg-stage"><div id="pg-host" style="width:100%;max-width:360px"></div></div><div class="ds-controls">' + \
    btn_group('pg-l-dir', 'Direction', 'data-pg="dir"', [('h', 'Horizontal', True), ('v', 'Vertical', False)]) + \
    btn_group('pg-l-col', 'Color', 'data-pg="color"', [('primary', 'Primary', True), ('secondary', 'Secondary', False), ('tertiary', 'Tertiary', False)]) + \
    '</div></div><h3 class="ds-h3">Markup for this selection</h3>' + code_box('pg-code', 'HTML')

overview = '<h2 class="ds-h2">Overview</h2>' + desc('A divider is a <strong>1px line</strong> that separates content groups, so users can scan and organize information. It is decorative: it carries no content and no interaction.') + \
    desc('Divider has two directions (horizontal and vertical) and three colors. It has no states and no size, and it looks the same on every breakpoint. The line fills its container, and the space around it comes from the parent <code>gap</code>.') + \
    three_pages(SLUG, 'a divider', 'the values: the line, the tokens and the requirements', 'how to add one to a page')

usage = '<h2 class="ds-h2">Usage</h2><h3 class="ds-h3 ds-group">When to use</h3>' + desc('Add a divider only when spacing alone does not separate the content. Use it to:') + \
    bullets(['Separate distinct content groups in a page or a container', 'Organize the rows of a list or a settings page', 'Create hierarchy where content lacks a clear separation', 'Separate form sections or interactive items, such as menu items']) + \
    '<h3 class="ds-h3 ds-group">When not to use</h3><h3 class="ds-h3">When whitespace is enough</h3>' + desc('Every line adds visual clutter. If the content is already grouped by space, a heading or a label, leave the line out.') + \
    fig_pair('<div class="pg-list" id="fig-do"></div>', 'Do separate unrelated groups with a divider.', '<div class="pg-list" id="fig-dont"></div>', 'Do not put a line between every row of related content.') + \
    '<h3 class="ds-h3">For a boundary between page sections</h3>' + desc('A full-width boundary between two page sections is not a divider. Use <code>.page-divider</code> from <code>eco-section</code>: it adds the page margin and padding around the same 1px line.') + \
    '<h3 class="ds-h3">Keep the space on the parent</h3>' + desc('Set the space above and below the line with the <code>gap</code> of the parent. A margin on the divider itself makes the space depend on where the divider is used.') + \
    fig_pair('<div class="pg-list" id="fig-do2"></div>', 'Do set the space with the parent <code>gap</code>.', '<div class="pg-list" id="fig-dont2"></div>', 'Do not add margin to the divider.') + \
    '<h3 class="ds-h3 ds-group">Quick reference</h3>' + \
    table(['The user…', 'Use'], [['sees two groups of content that need a clear boundary', 'Divider'], ['sees a boundary between two full-width page sections', '<code>.page-divider</code> (<code>eco-section</code>)'], ['sees a boundary between two menu rows', 'The row’s own divider (<code>eco-menu</code>)'], ['sees content that is grouped by a heading', 'No divider']]) + \
    rules(['Separate distinct groups when whitespace is not enough.', 'Create hierarchy between types of information.', 'Set the space around it from the parent <code>gap</code>.', 'Use Primary by default and Tertiary for short side-by-side items.'],
          ['Overuse dividers: they create visual clutter.', 'Add a line only for decoration.', 'Use a divider where a heading or label is clearer.', 'Add margin to the divider itself.'])

anatomy = '<h2 class="ds-h2">Anatomy</h2><h3 class="ds-h3 ds-group">Divider</h3>' + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout" id="dv-anat" role="img" aria-label="Anatomy of a divider: 1 line"><div class="ds-callout__art" style="width:100%;max-width:360px"><hr class="divider" id="an-line" /></div></div></figure></div>' + \
    ol_parts([('Line', 'One 1px line in a border color. A horizontal divider is as wide as its container; a vertical one is as high as its row.')]) + \
    desc('A divider has no label, no icon and no padding of its own. The space around it belongs to the parent.')

variants = '<h2 class="ds-h2">Variants</h2>' + desc('Two directions in three colors, six in all. A divider has no states.') + \
    '<h3 class="ds-h3 ds-group">Horizontal</h3>' + desc('Between sections, list rows or form groups. It fills the width of its container.') + \
    fig_one('<div class="pg-grid"><div class="pg-cell"><span>Border Primary (default)</span><hr class="divider" /></div><div class="pg-cell"><span>Border Secondary</span><hr class="divider divider--secondary" /></div><div class="pg-cell"><span>Border Tertiary</span><hr class="divider divider--tertiary" /></div></div>') + \
    '<h3 class="ds-h3 ds-group">Vertical</h3>' + desc('Between items placed side by side. Put it in a flex row; it stretches to the height of the row.') + \
    fig_one('<div class="pg-row"><span class="divider divider--vertical" role="separator" aria-orientation="vertical"></span><span class="divider divider--vertical divider--secondary" role="separator" aria-orientation="vertical"></span><span class="divider divider--vertical divider--tertiary" role="separator" aria-orientation="vertical"></span></div>') + \
    '<h3 class="ds-h3 ds-group">In a list</h3>' + desc('The space between the text and the line comes from the parent <code>gap</code>.') + \
    fig_one('<div class="pg-list"><span>Profile</span><hr class="divider" /><span>Addresses</span><hr class="divider" /><span>Users</span></div>')

sizes = '<h2 class="ds-h2">Sizes</h2>' + desc('A divider has no sizes. The line is always <strong>1px</strong> thick, and there is no spacing token for a hairline. The length is set by the container: the full width for a horizontal divider, the full height of the row for a vertical one. Figma shows 335px and 112px as example lengths, not fixed values. The values are under ' + sec_link(SLUG, 'sizes', 'Sizes') + ' in Specifications.')

layout = '<h2 class="ds-h2">Layout &amp; Appearance</h2><h3 class="ds-h3 ds-group">Alignment</h3>' + desc('A horizontal divider starts at the left edge of its container and runs to the right edge. A vertical one sits between two items in a flex row and takes the height of the row.') + \
    '<h3 class="ds-h3 ds-group">Appearance</h3>' + desc('Primary is the default. Secondary is less prominent and has very low contrast, so use it on white only. Tertiary is more prominent and suits short separations, such as values placed side by side. Token names and values are under ' + sec_link(SLUG, 'design-tokens', 'Design Tokens') + ' in Specifications.')

behavior = '<h2 class="ds-h2">Behavior</h2>' + desc('A divider is not interactive. It has no hover, focus or disabled state, it cannot be tabbed to, and it does not move or animate.') + \
    '<h3 class="ds-h3 ds-group">Breakpoints</h3>' + desc('It is the same on every breakpoint. There is no mobile or desktop value.')

access = '<h2 class="ds-h2">Accessibility</h2>' + desc('All requirements are listed under ' + sec_link(SLUG, 'accessibility-requirements', 'Accessibility Requirements') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Keyboard support</h3>' + desc('None. A divider is not focusable.') + \
    '<h3 class="ds-h3 ds-group">Screen reader support</h3>' + desc('An <code>&lt;hr&gt;</code> is announced as a separator, so use it when the line separates content for everyone. A line that is only visual, inside a component, gets <code>aria-hidden="true"</code>.')

related = '<h2 class="ds-h2">Related</h2><ul class="ds-bullets"><li><strong>' + link_large('menu.html', 'Menu') + '</strong>. Its rows carry their own divider (middle-inset, full-width or none).</li><li><strong>' + link_large('section.html', 'Section') + '</strong>. <code>.page-divider</code> for the boundary between page sections.</li><li><strong>' + link_large('../foundations/docs-table.html', 'Docs table') + '</strong>. Row lines are part of the table.</li></ul>'

references = '<h2 class="ds-h2">References</h2>' + refs([
    ('https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html', 'WCAG 2.2: Info and Relationships', 'Success criterion 1.3.1: structure must not depend on a line alone.'),
    ('https://www.w3.org/WAI/ARIA/apg/practices/names-and-descriptions/', 'WAI-ARIA Authoring Practices: Names and descriptions', 'The separator role.'),
    ('https://fluent2.microsoft.design/components/web/react/core/divider/usage', 'Fluent 2: Divider', 'Microsoft.'),
    ('https://m3.material.io/components/divider/overview', 'Material Design 3: Divider', 'Google.'),
    ('https://carbondesignsystem.com/elements/color/usage/', 'Carbon Design System: Color', 'IBM. Border colors for separation.')])

ex = [('playground', playground), ('overview', overview), ('usage', usage), ('anatomy', anatomy), ('variants', variants), ('sizes', sizes), ('layout', layout), ('behavior', behavior), ('accessibility', access), ('related', related), ('references', references)]

# ---------------------------------------------------------------- Specifications
st_tok = '<h2 class="ds-h2">Design Tokens</h2>' + desc('Resolved from the live token package.') + \
    '<div class="ds-table-wrap"><table class="ds-table" id="tok-table"><thead><tr><th scope="col">Color</th><th scope="col">Use</th><th scope="col">Token</th><th scope="col">Value</th></tr></thead><tbody></tbody></table></div>'

st_sizes = '<h2 class="ds-h2">Sizes</h2>' + table(['Variant', 'Thickness', 'Length'], [['Horizontal', '1px (height)', 'Fills the container (<code>width: 100%</code>)'], ['Vertical', '1px (width)', 'Fills the row height (<code>align-self: stretch</code>)']]) + \
    note('The thickness is a hairline: there is no spacing token for it, and a divider is never thicker. The size does not change with the breakpoint.')

st_meas = '<h2 class="ds-h2">Measurements</h2><h3 class="ds-h3 ds-group">Dimensions</h3>' + table(['Attribute', 'Value'], [['Thickness', '1px'], ['Horizontal length', 'The width of the container'], ['Vertical length', 'The height of the row'], ['Padding and margin', 'None: the space comes from the parent <code>gap</code>']]) + \
    note('A divider has no padding or margin of its own, so there is no measurement figure.') + \
    '<h3 class="ds-h3 ds-group">Spacing</h3>' + desc('The space around a divider belongs to the parent. Use a spacing token for the <code>gap</code>.') + table(['Part', 'Value'], [['Space above and below a horizontal divider', 'The parent <code>gap</code>, a spacing token such as <code>space-16</code>'], ['Space beside a vertical divider', 'The parent <code>gap</code>, a spacing token such as <code>space-24</code>']])

st_states = '<h2 class="ds-h2">States</h2>' + desc('A divider has no states: no hover, focus, active or disabled.')

st_struct = '<h2 class="ds-h2">Structure</h2><h3 class="ds-h3 ds-group">Elements</h3>' + table(['Element', 'Class', 'Notes'], [
    ['Line', '<code>divider</code>', 'An <code>&lt;hr&gt;</code> (horizontal) or a <code>span</code> (vertical). Primary color.'], ['Color', '<code>divider--secondary</code>, <code>divider--tertiary</code>', 'Replace the Primary color.'], ['Direction', '<code>divider--vertical</code>', 'A 1px wide line that stretches to the height of a flex row.']]) + \
    '<h3 class="ds-h3 ds-group">Types</h3>' + table(['Type', 'Class', 'Use'], [['Horizontal', '<code>divider</code>', 'Between sections, list rows or form groups.'], ['Vertical', '<code>divider divider--vertical</code>', 'Between items in a flex row.']]) + \
    '<h3 class="ds-h3 ds-group">Width</h3>' + desc('A horizontal divider is as wide as its container.')

st_behavior = '<h2 class="ds-h2">Behavior</h2>' + table(['Topic', 'Result'], [['Input', 'None. A divider has no hover, focus or click.'], ['Breakpoint', 'The same on every breakpoint.'], ['Motion', 'None.']])

st_access = '<h2 class="ds-h2">Accessibility Requirements</h2>' + table(['Topic', 'Requirement'], [
    ['Semantics', 'Use <code>&lt;hr&gt;</code> (or <code>role="separator"</code>) when the line separates content for everyone. Use <code>aria-hidden="true"</code> when it is only visual.'], ['Vertical', 'Set <code>role="separator"</code> and <code>aria-orientation="vertical"</code>.'],
    ['Color', 'Never rely on color alone. If the line carries meaning, the structure (headings, lists) must also show the grouping (WCAG 1.3.1).'], ['Contrast', 'Ensure enough contrast if the line carries meaning (WCAG 1.4.11). Prefer Primary or Tertiary over Secondary.']])

spec = [('design-tokens', st_tok), ('sizes', st_sizes), ('measurements', st_meas), ('states', st_states), ('structure', st_struct), ('behavior', st_behavior), ('accessibility-requirements', st_access)]

# ---------------------------------------------------------------- Code
c_basic = '<h2 class="ds-h2">Basic Usage</h2>' + desc('Link the shared stylesheet once per page. Never copy the rules into a page.') + table(['Step', 'What to do'], [
    ['1. Link', '<code>&lt;link rel="stylesheet" href="/components/css/divider.css"&gt;</code>. Both templates already have it.'], ['2. Horizontal', 'An <code>&lt;hr class="divider"&gt;</code> between the two groups.'],
    ['3. Vertical', 'A <code>span.divider.divider--vertical</code> with <code>role="separator"</code> inside a flex row.'], ['4. Color', 'Primary is the default. Add <code>divider--secondary</code> or <code>divider--tertiary</code>.'], ['5. Space', 'Set it with the <code>gap</code> of the parent, never with margin on the divider.']])
c_div = '<h2 class="ds-h2">Divider</h2>' + desc('Copy the markup you need.') + '<div id="recipes"></div>'
c_api = '<h2 class="ds-h2">API</h2><h3 class="ds-h3 ds-group">Classes</h3>' + table(['Class', 'Use'], [['<code>divider</code>', 'The line: 1px, Primary color, full width.'], ['<code>divider--secondary</code>', 'Secondary border color.'], ['<code>divider--tertiary</code>', 'Tertiary border color.'], ['<code>divider--vertical</code>', 'A vertical line inside a flex row.']]) + \
    '<h3 class="ds-h3 ds-group">Things to know</h3>' + bullets(['A divider is the same on every breakpoint.', 'The divider sets <code>margin: 0</code>. Put the space on the parent with <code>gap</code>.', 'A boundary between full-width page sections is <code>.page-divider</code> (<code>eco-section</code>), not a divider.'])
c_css = '<h2 class="ds-h2">CSS / Tailwind</h2>' + desc('The component is one CSS file, shared by every page. Link it, never copy it. The CSS below is read from the file the page links, so it is always what you see.') + code_box('css-code', 'CSS (components/css/divider.css)')
code = [('basic-usage', c_basic), ('divider', c_div), ('api', c_api), ('css-tailwind', c_css, False)]

# ---------------------------------------------------------------- scripts
JS_EX = r'''
  var pg = { dir: 'h', color: 'primary' };
  function renderPg() {
    var cls = 'divider' + (pg.color === 'primary' ? '' : ' divider--' + pg.color) + (pg.dir === 'v' ? ' divider--vertical' : '');
    var host = clear($('#pg-host')), el = document.createElement(pg.dir === 'h' ? 'hr' : 'span'); el.className = cls;
    if (pg.dir === 'v') { el.setAttribute('role', 'separator'); el.setAttribute('aria-orientation', 'vertical'); host.style.cssText = 'display:flex;gap:24px;height:112px;max-width:360px;width:100%;justify-content:center'; }
    else host.style.cssText = 'width:100%;max-width:360px';
    host.appendChild(el);
    $('#pg-code').textContent = pg.dir === 'h' ? '<hr class="' + cls + '" />' : '<span class="' + cls + '" role="separator" aria-orientation="vertical"></span>';
  }
  DK.wire(pg, renderPg);

  /* Usage figures */
  function list(host, items, line) { clear($(host)); items.forEach(function (t, i) { var s = document.createElement('span'); s.textContent = t; $(host).appendChild(s); if (i < items.length - 1 && line(i)) $(host).appendChild(Object.assign(document.createElement('hr'), { className: 'divider' })); }); }
  list('#fig-do', ['Profile', 'Name and email', 'Addresses', 'Billing address'], function (i) { return i === 1; });
  list('#fig-dont', ['Profile', 'Name and email', 'Addresses', 'Billing address'], function () { return true; });
  list('#fig-do2', ['Profile', 'Addresses'], function () { return true; });
  list('#fig-dont2', ['Profile', 'Addresses'], function () { return true; });
  $$('#fig-dont2 hr').forEach(function (h) { h.style.margin = '24px 0'; });

  /* Anatomy */
  DK.callouts($('#dv-anat'), [{ n: 1, el: $('#an-line'), side: 'top', len: 40, at: 'center' }]);
  renderPg();
'''

JS_SPEC = r'''
  DK.tokenTable($('#tok-table tbody'), [
    ['Border Primary (default)', 'Default separation', 'border-primary'], ['Border Secondary', 'Less prominent, still present. White surfaces only.', 'border-secondary'], ['Border Tertiary', 'Short or side-by-side separations', 'border-tertiary']]);
'''

JS_CODE = r'''
  DK.recipes($('#recipes'), [
    ['Horizontal', '<hr class="divider" />\n<hr class="divider divider--secondary" />\n<hr class="divider divider--tertiary" />'],
    ['Vertical, inside a flex row', '<div style="display: flex; gap: 24px">\n  <span>Size</span>\n  <span class="divider divider--vertical" role="separator" aria-orientation="vertical"></span>\n  <span>Weight</span>\n</div>'],
    ['Visual only', '<span class="divider" aria-hidden="true"></span>']
  ]);
  DK.printCss($('#css-code'), 'divider', [[/^ {4}/gm, '']]);
'''

C = dict(
    slug=SLUG, title='Divider', eyebrow='Components · Menus, lists and dividers',
    lead='A divider is a <strong>1px line</strong> that separates content groups, so users can scan and organize information. It is decorative and never interactive.',
    lead_ex='Every example on this page is the real component, not a picture. Figma: ' + fig_link(FIGMA, 'Divider') + ' and ' + fig_link(FIGMA_G, 'guidelines') + '.',
    lead_spec='The line, the tokens and the requirements. Values come from the live token package and from Figma: ' + fig_link(FIGMA, 'Divider') + '.',
    lead_code='How to add a divider to a page. The file is <code>components/css/divider.css</code>.',
    select_menu=False,
    css=[], style=STYLE, ex=ex, spec=spec, code=code, js_ex=JS_EX, js_spec=JS_SPEC, js_code=JS_CODE)

if __name__ == '__main__':
    emit(C)
