from build import *

SLUG = 'button-group'
BADGE = '<span class="badge-basic badge-basic--warning badge-basic--weak" title="No Figma component is linked for the button group (section “Button group” in eco-button). This page documents the repo implementation.">In progress</span>'

STYLE = r'''    .pg-col { display: flex; flex-direction: column; align-items: flex-start; gap: 16px; }
    .pg-note { font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-tertiary); }
    .pg-matrix td { vertical-align: middle; padding-top: 16px; padding-bottom: 16px; }
    .bg-fig { width: 100%; overflow: hidden; padding: 4px; margin: -4px; box-sizing: content-box; }   /* demo: a fixed box, so a group that is too wide is cut off, not wrapped */
    .ds-callout__art { padding-right: 24px; }'''

playground = '<h2 class="ds-h2">Playground</h2>' + desc('Joined System buttons that work as a toggle group. Click one to select it. This is the control the playgrounds on this site use.') + \
    '<div class="ds-playground"><div class="ds-stage ds-stage--center" id="pg-stage"><div id="pg-host"></div></div><div class="ds-controls">' + \
    bp_field('pg-l-bp') + btn_group('pg-l-n', 'Options', 'data-pg="n"', [('2', '2', False), ('3', '3', True), ('4', '4', False)]) + \
    btn_group('pg-l-s', 'Selected', 'data-pg="sel"', [('1', '1', True), ('2', '2', False), ('3', '3', False)]) + \
    btn_group('pg-l-d', 'Disabled option', 'data-pg="dis"', [('off', 'None', True), ('last', 'Last', False)]) + \
    '<div class="ds-field form-field"><label class="form-label form-label--sm" for="pg-label">First label</label><div class="input-wrap"><div class="input-box input-box--sm"><input class="form-input" type="text" id="pg-label" value="Small" placeholder="First label" /></div></div></div>' + \
    '</div></div><h3 class="ds-h3">Markup for this selection</h3>' + code_box('pg-code', 'HTML')

overview = '<h2 class="ds-h2">Overview</h2>' + desc('A button group is a row of <strong>joined System buttons</strong> for choosing between two to four short options. The selected button has a black 12% fill.') + \
    desc('It is a toggle group: your script sets <code>aria-pressed</code> on the chosen button. It is the control the playgrounds on this site use, and it fits a toolbar or a filter row. It is not the sliding pill (see <a class="inline-link inline-link--large inline-link--secondary" href="segment-control.html">Pill segment control</a>).') + \
    three_pages(SLUG, 'a button group', 'the values: tokens, sizes, measurements, states and requirements', 'how to add one to a page')

usage = '<h2 class="ds-h2">Usage</h2><h3 class="ds-h3 ds-group">When to use</h3>' + desc('Use a button group to pick one of two to four short options in a toolbar, a filter row or a playground. Use it to:') + \
    bullets(['Switch between a few values of one setting, such as a size or a view', 'Filter a list in a compact toolbar, with a visible label beside the group']) + \
    '<h3 class="ds-h3 ds-group">When not to use</h3><h3 class="ds-h3">For more than four options</h3>' + desc('The group never wraps onto a second row, and it is never made smaller to fit. With more options, or when the group does not fit its container, show a select with the same options instead.') + \
    fig_pair('<div class="bg-fig" id="fig-do"></div>', 'Do use two to four short options.', '<div class="bg-fig" id="fig-dont"></div>', 'Do not use it for more than four options. Use a select instead.') + \
    '<h3 class="ds-h3">Keep labels short</h3>' + desc('The group shows all its options on one row. Short labels keep it narrow; long labels make it wider than its container.') + \
    fig_pair('<div class="bg-fig" id="fig-lab-do"></div>', 'Do keep the labels short.', '<div class="bg-fig" id="fig-lab-dont"></div>', 'Do not use long labels: the group grows wider than its container.') + \
    '<h3 class="ds-h3 ds-group">Quick reference</h3>' + \
    table(['The user…', 'Use'], [['picks one of 2–4 short options on a toolbar or in a playground', 'Button group'], ['switches the main view of a surface with a sliding pill', '<a class="inline-link inline-link--small" href="segment-control.html">Pill segment control</a>'], ['picks one of many options', '<a class="inline-link inline-link--small" href="select.html">Select</a>'], ['picks one and submits', '<a class="inline-link inline-link--small" href="radio.html">Radio</a>'], ['goes to another page', '<a class="inline-link inline-link--small" href="tabs.html">Tabs</a> or a link']]) + \
    rules(['Keep to 2–4 options with short labels.', 'Label the group with <code>aria-label</code> or a visible label.', 'Set <code>aria-pressed</code> on the selected button.', 'Link <code>button-group.css</code>.'],
          ['Wrap the group onto two rows.', 'Use it for page navigation.', 'Allow more than one selected unless you mean a multi-select toggle.', 'Copy its rules into the page.'])

anatomy = '<h2 class="ds-h2">Anatomy</h2><h3 class="ds-h3 ds-group">Button group</h3>' + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout" id="bg-anat" role="img" aria-label="Anatomy of a button group: 1 group, 2 selected button, 3 button that is not selected, 4 shared frame"><div class="ds-callout__art"><div id="a-host"></div></div></div></figure></div>' + \
    ol_parts([('Group', 'A <code>role="group"</code> row of buttons. It is <code>inline-flex</code> and never wider than its parent.'), ('Selected button', '<code>aria-pressed="true"</code>: a black 12% fill and the same frame.'), ('Button', 'A System button with an uppercase label. Hover darkens the frame and adds the fill.'), ('Shared frame', 'A 1px frame is drawn inside each button and shared between neighbours with <code>margin-left: -1px</code>.')])

variants = '<h2 class="ds-h2">Variants</h2>' + desc('Two to four short options on one row. The group never wraps. With more options, use a select.') + \
    '<h3 class="ds-h3 ds-group">Option counts</h3>' + fig_one('<div class="pg-col" id="v-counts"></div>') + \
    '<h3 class="ds-h3 ds-group">With a label, as in a toolbar</h3>' + fig_one('<div class="ds-toolbar" style="margin:0"><span class="ds-toolbar__label" id="vt-l">View</span><div class="btn-group" role="group" aria-labelledby="vt-l" id="v-tool"></div></div>')

sizes = '<h2 class="ds-h2">Sizes</h2>' + desc('The button group has one size: Small System buttons, 32px high on mobile and 40px from 769px. The tablet range (640 to 768px) uses the mobile size. Measurements are under ' + sec_link(SLUG, 'sizes', 'Sizes') + ' in Specifications.') + \
    toolbar([('sb-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force')]) + fig_one('<div id="v-size"></div>')

layout = '<h2 class="ds-h2">Layout &amp; Appearance</h2><h3 class="ds-h3 ds-group">Width</h3>' + desc('The group is as wide as its buttons and never wider than its parent. Buttons share their 1px frame. When the group does not fit, for example in a narrow controls column, show a select with the same options and keep the two in sync.') + \
    '<h3 class="ds-h3 ds-group">Alignment</h3>' + desc('A group sits at the start of its row (<code>align-self: flex-start</code>). In a toolbar put the visible label before it.') + \
    '<h3 class="ds-h3 ds-group">Appearance</h3>' + desc('A light frame, an uppercase label and a black 12% fill for the selected button. Token names and values are under ' + sec_link(SLUG, 'design-tokens', 'Design Tokens') + ' in Specifications.')

behavior = '<h2 class="ds-h2">Behavior</h2><h3 class="ds-h3 ds-group">Selection</h3>' + desc('One button is selected at a time. Your script sets <code>aria-pressed</code>; the CSS does not toggle it.') + \
    '<h3 class="ds-h3 ds-group">Hover and focus</h3>' + desc('Hover darkens the frame to <code>border-hover</code> and, when the button is not selected, adds the fill. The focus ring is 2px with a 2px gap and shows on keyboard use only (<code>body.keyboard-nav</code>). All states are listed under ' + sec_link(SLUG, 'states', 'States') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Disabled</h3>' + desc('A disabled button is not focusable. Its label and frame use the disabled tokens.') + \
    '<h3 class="ds-h3 ds-group">Motion</h3>' + desc('The frame and the fill change over 100ms. Values are under ' + sec_link(SLUG, 'motion', 'Motion') + ' in Specifications.')

access = '<h2 class="ds-h2">Accessibility</h2>' + desc('All requirements are listed under ' + sec_link(SLUG, 'accessibility-requirements', 'Accessibility Requirements') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Keyboard support</h3>' + desc('Tab moves between the buttons. Enter or Space chooses the focused one. The focus ring shows on keyboard use only.') + \
    '<h3 class="ds-h3 ds-group">Screen reader support</h3>' + desc('The group is a <code>role="group"</code> with an <code>aria-label</code> or <code>aria-labelledby</code>. Each button is a real <code>&lt;button type="button"&gt;</code> with <code>aria-pressed</code>, so the chosen one is announced as pressed.')

related = '<h2 class="ds-h2">Related</h2><ul class="ds-bullets"><li><strong>' + link_large('button.html', 'Button') + '</strong>. The System button that the group is built from.</li><li><strong>' + link_large('segment-control.html', 'Pill segment control') + '</strong>. A switch between two related views, with a sliding pill.</li><li><strong>' + link_large('select.html', 'Select') + '</strong>. One of many options.</li><li><strong>' + link_large('radio.html', 'Radio button') + '</strong>. One option that is submitted.</li><li><strong>' + link_large('tabs.html', 'Tabs') + '</strong>. Navigation between sections.</li></ul>'

references = '<h2 class="ds-h2">References</h2>' + refs([
    ('https://www.w3.org/WAI/ARIA/apg/patterns/button/', 'WAI-ARIA Authoring Practices: Button', 'Keyboard and role requirements, including toggle buttons.'),
    ('https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html', 'WCAG 2.2: Non-text Contrast', 'Success criterion 1.4.11.'),
    ('https://m3.material.io/components/segmented-buttons/overview', 'Material Design 3: Segmented buttons', 'Google.'),
    ('https://carbondesignsystem.com/components/content-switcher/usage/', 'Carbon Design System: Content switcher', 'IBM.')])

ex = [('playground', playground), ('overview', overview), ('usage', usage), ('anatomy', anatomy), ('variants', variants), ('sizes', sizes), ('layout', layout), ('behavior', behavior), ('accessibility', access), ('related', related), ('references', references)]

# ---------------------------------------------------------------- Specifications
st_tok = '<h2 class="ds-h2">Design Tokens</h2>' + desc('Resolved from the live token package.') + \
    '<div class="ds-table-wrap"><table class="ds-table" id="tok-table"><thead><tr><th scope="col">State</th><th scope="col">Part</th><th scope="col">Token</th><th scope="col">Value</th></tr></thead><tbody></tbody></table></div>'

st_sizes = '<h2 class="ds-h2">Sizes</h2>' + table(['Breakpoint', 'Height', 'Padding', 'Label'], [['Mobile and tablet', '32px', '0 10px', '14/14, 0.42px, uppercase, weight 600'], ['Desktop (769px+)', '40px', '0 16px', '16/16, 0.48px, uppercase, weight 600']]) + \
    note('The tablet range (640 to 768px) uses the mobile values. The 1px frame is drawn inside each button (<code>inset box-shadow</code>) and shared between neighbours with <code>margin-left: -1px</code>. The group is <code>inline-flex</code> and never wider than its parent.')


def mfig():
    return ('<div class="measure__item"><span class="measure__name">1 · Button</span><div class="measure__obj"><div class="btn-group" role="group" aria-label="Option"><button type="button" class="measure__subject" aria-pressed="true" tabindex="-1">Option</button></div>'
            '<i class="measure__pad measure__pad--t"></i><i class="measure__pad measure__pad--b"></i><i class="measure__pad measure__pad--l"></i><i class="measure__pad measure__pad--r"></i>'
            '<b class="measure__dim measure__dim--v measure__dim--t"><span></span></b><b class="measure__dim measure__dim--v measure__dim--b"><span></span></b><b class="measure__dim measure__dim--h measure__dim--l"><span></span></b><b class="measure__dim measure__dim--h measure__dim--r"><span></span></b></div></div>')


st_meas = '<h2 class="ds-h2">Measurements</h2><h3 class="ds-h3 ds-group">Dimensions</h3>' + desc('The padding of one button, left and right. The numbers are read from the component.') + \
    toolbar([('mb-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force')]) + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-fig__stage--flush" style="padding:0;min-height:0"><div class="measure" style="--k:2" role="img" aria-label="Padding of a button in a button group">' + mfig() + '</div></div><figcaption class="ds-fig__cap">A button at 2× size. Change the Breakpoint to see the mobile values.</figcaption></figure></div>' + \
    table(['Attribute', 'Mobile and tablet', 'Desktop (769px+)'], [['Height', '32px', '40px'], ['Padding left and right', '10px', '16px'], ['Padding above and below', 'None: the height is fixed and the content is centred', 'None'], ['Frame', '1px, inside the box, shared with the neighbour (<code>margin-left: -1px</code>)', 'The same'], ['Focus ring', '2px line, 2px gap, outside the box', 'The same']]) + \
    '<h3 class="ds-h3 ds-group">Spacing</h3>' + desc('The side padding as a spacing token.') + table(['Part', 'Value'], [['Padding, desktop', '<code>space-16</code>'], ['Padding, mobile', '10px: literal, no spacing token']])

st_states = '<h2 class="ds-h2">States</h2>' + desc('Selected is a black 12% fill (<code>aria-pressed="true"</code>). Hover darkens the frame and, when not selected, adds the fill. Hover and focus are forced on this page; in your code they come from <code>:hover</code> and the keyboard focus rule.') + \
    toolbar([('sb2-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force')]) + \
    '<div class="ds-table-wrap"><table class="ds-table pg-matrix" id="matrix"><thead><tr><th scope="col">State</th><th scope="col">Not selected</th><th scope="col">Selected</th></tr></thead><tbody></tbody></table></div>'

st_typo = '<h2 class="ds-h2">Typography</h2>' + table(['Part', 'Type', 'Mobile and tablet', 'Desktop (769px+)'], [['Label', '<code>label-md</code>', '14/14, 0.42px', '16/16, 0.48px']]) + \
    note('Breuer Condensed, weight 600, uppercase through CSS, so write the label in sentence case in the HTML. No font features, as for the Small button.')

st_struct = '<h2 class="ds-h2">Structure</h2><h3 class="ds-h3 ds-group">Elements</h3>' + table(['Element', 'Class', 'Notes'], [['Group', '<code>btn-group</code>', '<code>role="group"</code> with <code>aria-label</code> or <code>aria-labelledby</code>. <code>inline-flex</code>, <code>max-width: 100%</code>.'], ['Button', '<code>button</code> inside the group', 'A real <code>&lt;button type="button"&gt;</code>. Selected is <code>aria-pressed="true"</code>.']]) + \
    '<h3 class="ds-h3 ds-group">Width</h3>' + desc('The group is as wide as its buttons and never wider than its parent. It never wraps. Two to four options.')

st_motion = '<h2 class="ds-h2">Motion</h2>' + table(['Property', 'Duration', 'Easing'], [['Fill: <code>opacity</code> of <code>::before</code>', '<code>duration-fast-2</code> (100ms)', '<code>ease-standard</code>'], ['Frame: <code>box-shadow</code>', '<code>duration-fast-2</code>', '<code>ease-standard</code>'], ['Focus ring: <code>outline-color</code>', '<code>duration-fast-2</code>', '<code>ease-standard</code>']]) + \
    note('The same dissolve as the Button. Under <code>prefers-reduced-motion: reduce</code> the transition is turned off.')

st_behavior = '<h2 class="ds-h2">Behavior</h2>' + table(['Topic', 'Rule'], [
    ['Selection', 'One selected at a time, set by your script via <code>aria-pressed</code>. The CSS does not toggle it.'], ['Markup', '<code>role="group"</code> with <code>aria-label</code> or <code>aria-labelledby</code>; real <code>&lt;button type="button"&gt;</code>.'], ['Tab', 'Each button is focusable; 2px focus ring with a 2px gap on keyboard focus.'],
    ['Not navigation', 'A System button group toggles state. Page navigation uses links.'], ['Count', 'Two to four options. More: a select. When the group is wider than its container, show a select with the same options and keep the two in sync; never shrink, wrap or scroll the group.']])

st_access = '<h2 class="ds-h2">Accessibility Requirements</h2>' + table(['Topic', 'Requirement'], [
    ['Markup', '<code>role="group"</code> with an accessible name; real buttons with <code>aria-pressed</code>.'], ['Focus', '2px ring <code>border-focus</code> with a 2px gap, on keyboard use (WCAG 2.4.7, 1.4.11). It is set with <code>body.keyboard-nav</code>.'], ['State', 'The selected button differs by its fill and by <code>aria-pressed</code>, not by color alone (WCAG 1.4.1).'], ['Disabled', 'Not focusable. Disabled tokens are exempt from contrast requirements.']])

spec = [('design-tokens', st_tok), ('sizes', st_sizes), ('measurements', st_meas), ('states', st_states), ('typography', st_typo), ('structure', st_struct), ('motion', st_motion), ('behavior', st_behavior), ('accessibility-requirements', st_access)]

# ---------------------------------------------------------------- Code
c_basic = '<h2 class="ds-h2">Basic Usage</h2>' + desc('Link the shared stylesheet once per page. Never copy the rules into a page.') + table(['Step', 'What to do'], [
    ['1. Link', '<code>&lt;link rel="stylesheet" href="/components/css/button-group.css"&gt;</code>. Both templates already have it.'], ['2. Markup', 'A <code>div.btn-group[role="group"]</code> with an accessible name, and one <code>button</code> per option.'], ['3. Selected', 'Set <code>aria-pressed="true"</code> on one button and <code>"false"</code> on the others.'],
    ['4. Select one', 'Your script moves <code>aria-pressed</code> on click. The CSS does not.'], ['5. Focus ring', 'Add the small script that sets <code>body.keyboard-nav</code> on Tab, as for the Button.']])
c_grp = '<h2 class="ds-h2">Button group</h2><div id="recipes"></div>'
c_api = '<h2 class="ds-h2">API</h2><h3 class="ds-h3 ds-group">Classes</h3>' + table(['Class', 'Use'], [['<code>btn-group</code>', 'The group. The buttons inside are styled by the group, with no class of their own.']]) + \
    '<h3 class="ds-h3 ds-group">Things to know</h3>' + bullets(['Two to four short options. More options: use a select.', 'When the group is wider than its container, show a select with the same options and keep the two in sync. Never shrink, wrap or scroll the group.', 'Breakpoint: the buttons are 32px high below 769px and 40px from 769px; 640–768px is still mobile.', 'The <code>[data-state]</code> selectors do nothing outside the documentation pages.'])
c_css = '<h2 class="ds-h2">CSS / Tailwind</h2>' + desc('The component is one CSS file, shared by every page. Link it, never copy it. The CSS below is read from the file the page links, so it is always what you see.') + code_box('css-code', 'CSS (components/css/button-group.css)')
code = [('basic-usage', c_basic), ('button-group', c_grp), ('api', c_api), ('css-tailwind', c_css, False)]

# ---------------------------------------------------------------- scripts
GRP_JS = old_js('button-group', "  var LAB =", "  var st = {")

JS_EX = GRP_JS + r'''
  function grpL(labels, sel) {
    var g = document.createElement('div'); g.className = 'btn-group'; g.setAttribute('role', 'group'); g.setAttribute('aria-label', 'Options');
    labels.forEach(function (t, i) { var b = document.createElement('button'); b.type = 'button'; b.textContent = t; b.setAttribute('aria-pressed', String(i === sel)); g.appendChild(b); });
    g.addEventListener('click', function (e) { var b = e.target.closest('button'); if (!b) return; $$('button', g).forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); }); });
    return g;
  }
  var st = { n: '3', sel: '1', dis: 'off' };
''' + old_js('button-group', "  function renderPg() {", "  DK.wire(st, renderPg);") + r'''
  DK.wire(st, renderPg); $('#pg-label').addEventListener('input', renderPg);
  DK.bp();
  var vc = clear($('#v-counts')); [2, 3, 4].forEach(function (n) { vc.appendChild(grpEl(n, 1)); });
  var vt = $('#v-tool'); [['List', 'true'], ['Grid', 'false'], ['Map', 'false']].forEach(function (r) { var b = document.createElement('button'); b.type = 'button'; b.textContent = r[0]; b.setAttribute('aria-pressed', r[1]); vt.appendChild(b); });
  vt.addEventListener('click', function (e) { var b = e.target.closest('button'); if (!b) return; $$('button', vt).forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); }); });
  clear($('#v-size')).appendChild(grpEl(3, 1));

  /* Usage figures */
  clear($('#fig-do')).appendChild(grpL(['Small', 'Medium', 'Large'], 0));
  clear($('#fig-dont')).appendChild(grpL(['Small', 'Medium', 'Large', 'Extra large', 'Huge', 'Giant'], 0));
  clear($('#fig-lab-do')).appendChild(grpL(['List', 'Grid'], 0));
  clear($('#fig-lab-dont')).appendChild(grpL(['All features and services', 'Only the features that are included'], 0));

  /* Anatomy */
  var ag = grpEl(3, 1), ah = clear($('#a-host')); ah.appendChild(ag); var abs = $$('button', ag);
  DK.callouts($('#bg-anat'), [
    { n: 1, el: ag, side: 'left', len: 56, at: 'edge' },
    { n: 2, el: abs[0], side: 'top', len: 44, at: 'center' },
    { n: 3, el: abs[2], side: 'bottom', len: 44, at: 'center' },
    { n: 4, side: 'top', len: 44, at: 'edge', box: function () { var r = abs[2].getBoundingClientRect(); return { left: r.left, top: r.top, width: 1, height: r.height }; } }
  ]);
  renderPg();
'''

JS_SPEC = r'''
  var tb = $('#matrix tbody');
  [['Enabled', ''], ['Hover', 'hover'], ['Focus', 'focus'], ['Disabled', 'disabled']].forEach(function (r) {
    var tr = document.createElement('tr'), th = document.createElement('th'); th.scope = 'row'; th.textContent = r[0]; tr.appendChild(th);
    [false, true].forEach(function (sel) {
      var td = document.createElement('td'), g = document.createElement('div'); g.className = 'btn-group'; g.setAttribute('role', 'group'); g.setAttribute('aria-label', r[0]); g.style.alignSelf = 'center';
      var b = document.createElement('button'); b.type = 'button'; b.textContent = 'Option'; b.setAttribute('aria-pressed', String(sel)); if (r[1] === 'disabled') b.disabled = true; else if (r[1]) b.dataset.state = r[1];
      g.appendChild(b); td.appendChild(g); tr.appendChild(td);
    });
    tb.appendChild(tr);
  });
  DK.tokenTable($('#tok-table tbody'), [['Enabled', 'Text', 'text-action-primary'], ['All', 'Frame', 'border-action-3'], ['Hover', 'Frame', 'border-hover'], ['Hover, not selected', 'Fill', 'surface-opacity-black-12'], ['Selected', 'Fill', 'surface-opacity-black-12'], ['Focus', 'Ring', 'border-focus'], ['Disabled', 'Text', 'text-disabled'], ['Disabled', 'Frame', 'border-disabled']]);
  DK.bp(function () { if (window.ECO_MEASURE) ECO_MEASURE.init(); });
'''

JS_CODE = r'''
  DK.recipes($('#recipes'), [['Three options, one selected', '<div class="btn-group" role="group" aria-label="Size">\n  <button type="button" aria-pressed="true">Small</button>\n  <button type="button" aria-pressed="false">Medium</button>\n  <button type="button" aria-pressed="false">Large</button>\n</div>'],
    ['With a visible label (toolbar)', '<span id="view-label">View</span>\n<div class="btn-group" role="group" aria-labelledby="view-label">\n  <button type="button" aria-pressed="true">List</button>\n  <button type="button" aria-pressed="false">Grid</button>\n</div>'],
    ['Disabled option', '<div class="btn-group" role="group" aria-label="Size">\n  <button type="button" aria-pressed="true">Small</button>\n  <button type="button" aria-pressed="false" disabled>Large</button>\n</div>'],
    ['Select one (your script)', "group.addEventListener('click', function (e) {\n  var b = e.target.closest('button'); if (!b) return;\n  group.querySelectorAll('button').forEach(function (x) { x.setAttribute('aria-pressed', String(x === b)); });\n});"]]);
  DK.printCss($('#css-code'), 'button-group', [[/:is\(:hover, \[data-state="hover"\]\)/g, ':hover'], [/\.btn-group button\[data-state="focus"\], /g, '']]);
'''

C = dict(
    slug=SLUG, title='Button group', eyebrow='Components · Actions', eyebrow_extra=BADGE,
    lead='A button group is a row of <strong>joined System buttons</strong> for choosing between two to four short options. The selected button has a black 12% fill.',
    lead_ex='Every example on this page is the real component, not a picture.',
    lead_spec='Tokens, sizes, measurements, states and requirements. Values come from the live token package and from the specification skill: no Figma component is linked.',
    lead_code='How to add a button group to a page. The file is <code>components/css/button-group.css</code>.',
    css=[], select_menu=False, style=STYLE, ex=ex, spec=spec, code=code, js_ex=JS_EX, js_spec=JS_SPEC, js_code=JS_CODE)

if __name__ == '__main__':
    emit(C)
