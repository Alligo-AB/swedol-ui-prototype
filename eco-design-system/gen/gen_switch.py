from build import *

FIGMA = 'https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=278-9676'
SLUG = 'switch'

STYLE = r'''    .pg-note { font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-tertiary); }
    .ds-stage--dark .ds-table, .ds-stage--dark .ds-table th, .ds-stage--dark .ds-table td { color: var(--color-text-primary-inverted); border-color: var(--color-surface-60); }
    .ds-stage--dark .ds-table thead th { background: transparent; }
    .ds-table-wrap.ds-stage--dark { padding: 0; background: var(--color-surface-100); }
    .pg-list { display: flex; flex-direction: column; gap: 16px; }
    .pg-row { display: flex; flex-wrap: wrap; gap: 24px; }
    .pg-matrix td { vertical-align: top; padding-top: 16px; padding-bottom: 16px; }
    .sw-fig { display: flex; flex-direction: column; align-items: flex-start; gap: 16px; width: 100%; max-width: 320px; }
    .ds-callout__art { padding-right: 24px; }'''

playground = '<h2 class="ds-h2">Playground</h2>' + desc('Choose a breakpoint, mode, size, state and value and the switch and its code update. Hover and focus are forced here. The switch is live: click it.') + \
    '<div class="ds-playground"><div class="ds-stage ds-stage--center" id="pg-stage"><div id="pg-host"></div></div><div class="ds-controls">' + \
    bp_field('pg-l-bp') + btn_group('pg-l-mode', 'Mode', 'data-pg="mode"', [('light', 'Light', True), ('dark', 'Dark', False)]) + \
    btn_group('pg-l-size', 'Size', 'data-pg="size"', [('lg', 'Large', True), ('sm', 'Small', False), ('xs', 'X-Small', False)]) + \
    btn_group('pg-l-st', 'State', 'data-pg="state"', [('enabled', 'Enabled', True), ('hover', 'Hover', False), ('focus', 'Focus', False), ('disabled', 'Disabled', False)]) + \
    btn_group('pg-l-val', 'Value', 'data-pg="value"', [('off', 'Off', True), ('on', 'On', False)]) + \
    '<div class="ds-field form-field"><label class="form-label form-label--sm" for="pg-label">Label</label><div class="input-wrap"><div class="input-box input-box--sm"><input class="form-input" type="text" id="pg-label" value="Email notifications" placeholder="Label" /></div></div></div>' + \
    '</div></div><h3 class="ds-h3">Markup for this selection</h3>' + code_box('pg-code', 'HTML')

overview = '<h2 class="ds-h2">Overview</h2>' + desc('A switch turns one setting on or off and applies the change at once. It is for a single binary choice, not for picking between options.') + \
    desc('Switch has three sizes (Large, Small, X-Small), a light and a dark mode, and four states, each off and on. It is a native <code>&lt;input type="checkbox" role="switch"&gt;</code>, so the keyboard behavior comes from the browser.') + \
    three_pages(SLUG, 'a switch', 'the values: tokens, sizes, measurements, states and requirements', 'how to add one to a page')

usage = '<h2 class="ds-h2">Usage</h2><h3 class="ds-h3 ds-group">When to use</h3>' + desc('Use a switch for one setting that turns on or off, where the change takes effect at once. Use it to:') + \
    bullets(['Turn a notification channel on or off', 'Turn a feature or a preference on or off in a list of settings', 'Change a setting in a table row (without a visible label, with an <code>aria-label</code>)']) + \
    '<h3 class="ds-h3 ds-group">When not to use</h3><h3 class="ds-h3">When a Save button is needed</h3>' + desc('A switch applies its change at once, so a list of settings needs no Save button. When the choice is saved on submit, use <code>eco-checkbox</code>.') + \
    fig_pair('<div class="sw-fig" id="fig-do"></div>', 'Do apply the change at once, with no Save button.', '<div class="sw-fig" id="fig-dont"></div>', 'Do not pair a switch with a Save button for the same setting.') + \
    '<h3 class="ds-h3">For a choice between options</h3>' + desc('To choose between options use <code>eco-radio</code>, and to switch between two related views or filters use <code>eco-pill-segment-control</code>.') + \
    '<h3 class="ds-h3">Label the setting, not the state</h3>' + desc('The label names the setting. The switch shows the state, so a label that says “On” or “Off” says it twice and goes out of date when the switch moves.') + \
    fig_pair('<div class="sw-fig"><label class="form-switch-item"><input type="checkbox" role="switch" checked /><span>Email notifications</span></label></div>', 'Do name the setting in the label.', '<div class="sw-fig"><label class="form-switch-item"><input type="checkbox" role="switch" checked /><span>On</span></label></div>', 'Do not change the label to “On” or “Off”.') + \
    '<h3 class="ds-h3 ds-group">Quick reference</h3>' + \
    table(['The user…', 'Use'], [['turns one setting on or off, with immediate effect', 'Switch'], ['picks any number of options, saved on submit', '<code>eco-checkbox</code>'], ['picks exactly one of several options', '<code>eco-radio</code>'], ['switches between two related views or filters', '<code>eco-pill-segment-control</code>']]) + \
    rules(['Describe the setting in the label, in sentence case.', 'Apply the change immediately.', 'Use <code>.form-switch-item--dark</code> on dark surfaces.', 'Test Space, Tab and label click.'],
          ['Pair a switch with a Save button for the same setting.', 'Change the label text to “On” or “Off”.', 'Use a switch to choose between options.', 'Use the dark markup on a light surface.'])

anatomy = '<h2 class="ds-h2">Anatomy</h2><h3 class="ds-h3 ds-group">Switch</h3>' + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout" id="sw-anat" role="img" aria-label="Anatomy of a switch: 1 track, 2 thumb, 3 label"><div class="ds-callout__art"><label class="form-switch-item"><input type="checkbox" role="switch" id="an-in" checked tabindex="-1" /><span id="an-lbl">Email notifications</span></label></div></div></figure></div>' + \
    ol_parts([('Track', 'A pill, 48×24px (X-Small 32×16px). Grey when off, green when on.'), ('Thumb', 'A 20px circle (X-Small 12px), 2px from the track edge, with a small shadow. It moves by <code>transform</code>.'), ('Label', '<code>body-md</code> (Large) or <code>body-sm</code>, 8px from the track. The whole label is the click target.')]) + \
    desc('The focus ring is 2px with a 2px offset around the track.')

variants = '<h2 class="ds-h2">Variants</h2>' + desc('Light and dark mode. Choose the mode to see every example on a light or a dark surface. Sizes are under Sizes below.') + \
    toolbar([('vm-l', 'Mode', 'data-mode-toggle', [('light', 'Light', True), ('dark', 'Dark', False)]), ('vb-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force')]) + \
    '<h3 class="ds-h3 ds-group">Settings list</h3>' + desc('A switch applies its change at once, so a list of settings needs no Save button. The label names the setting; the switch shows the state, so never change the label to “On” or “Off”.') + \
    fig_one('<div class="pg-list" id="v-list"></div>', stage_attr=' data-mode-stage') + \
    '<h3 class="ds-h3 ds-group">Without a visible label</h3>' + desc('Only when the setting is named by its surroundings, for example a row in a table. It needs an <code>aria-label</code>.') + \
    fig_one('<div class="pg-row" id="v-nolabel"></div>', stage_attr=' data-mode-stage')

sizes = '<h2 class="ds-h2">Sizes</h2>' + desc('<strong>Large</strong> and <strong>Small</strong> have the same 48×24px track and differ only in label size. <strong>X-Small</strong> (class <code>.form-switch-item--xs</code>) has a 32×16px track for dense layouts. The size does not change with the breakpoint; only the Large label does. Measurements are under ' + sec_link(SLUG, 'sizes', 'Sizes') + ' in Specifications.') + \
    fig_one('<div class="pg-list" id="v-sizes"></div>', stage_attr=' data-mode-stage')

layout = '<h2 class="ds-h2">Layout &amp; Appearance</h2><h3 class="ds-h3 ds-group">Alignment</h3>' + desc('In a list, put the switches on one left edge with the labels after them, one setting per row. Use the same size for every switch in a list.') + \
    '<h3 class="ds-h3 ds-group">Appearance</h3>' + desc('The track is grey when off and green when on, with a white thumb. Use the light version on light surfaces and the dark version (<code>.form-switch-item--dark</code>) on dark ones: <code>surface-100</code> or <code>surface-80</code>. Token names and values are under ' + sec_link(SLUG, 'design-tokens', 'Design Tokens') + ' in Specifications.')

behavior = '<h2 class="ds-h2">Behavior</h2><h3 class="ds-h3 ds-group">Toggling</h3>' + desc('A click on the switch or the label toggles it, and the change applies at once. Space toggles the focused switch.') + \
    '<h3 class="ds-h3 ds-group">Hover and focus</h3>' + desc('Hover changes the track color. The ring shows with <code>:focus-visible</code> only, for both off and on. All states are listed under ' + sec_link(SLUG, 'states', 'States') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Disabled</h3>' + desc('A disabled switch is not focusable. It has a muted track, no thumb shadow and a <code>text-disabled</code> label.') + \
    '<h3 class="ds-h3 ds-group">Motion</h3>' + desc('The track color and the thumb move with a short transition. Reduced motion turns it off. Values are under ' + sec_link(SLUG, 'motion', 'Motion') + ' in Specifications.')

access = '<h2 class="ds-h2">Accessibility</h2>' + desc('All requirements are listed under ' + sec_link(SLUG, 'accessibility-requirements', 'Accessibility Requirements') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Keyboard support</h3>' + desc('Tab moves between switches. Space toggles the focused one. The focus ring shows with <code>:focus-visible</code>.') + \
    '<h3 class="ds-h3 ds-group">Screen reader support</h3>' + desc('The control is a native <code>input type="checkbox" role="switch"</code> inside a <code>label</code>, so the name, the role and the on/off state are announced. Never build it from a <code>div</code> or a <code>button</code>. A switch without a visible label needs an <code>aria-label</code>.')

related = '<h2 class="ds-h2">Related</h2><ul class="ds-bullets"><li><strong>' + link_large('checkbox.html', 'Checkbox') + '</strong>. Any number of options, saved on submit.</li><li><strong>' + link_large('radio.html', 'Radio button') + '</strong>. Exactly one of several options.</li><li><strong>' + link_large('segment-control.html', 'Pill segment control') + '</strong>. A switch between two related views.</li><li><strong>' + link_large('list-item.html', 'List Item') + '</strong>. A switch as the trailing element of a list row.</li></ul>'

references = '<h2 class="ds-h2">References</h2>' + refs([
    ('https://www.w3.org/WAI/ARIA/apg/patterns/switch/', 'WAI-ARIA Authoring Practices: Switch', 'Keyboard and role requirements.'),
    ('https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html', 'WCAG 2.2: Non-text Contrast', 'Success criterion 1.4.11.'),
    ('https://www.nngroup.com/articles/toggle-switch-guidelines/', 'Nielsen Norman Group: Toggle-Switch Guidelines', 'When to use a switch and how to label it.'),
    ('https://fluent2.microsoft.design/components/web/react/core/switch/usage', 'Fluent 2: Switch', 'Microsoft.'),
    ('https://m3.material.io/components/switch/overview', 'Material Design 3: Switch', 'Google.'),
    ('https://carbondesignsystem.com/components/toggle/usage/', 'Carbon Design System: Toggle', 'IBM.')])

ex = [('playground', playground), ('overview', overview), ('usage', usage), ('anatomy', anatomy), ('variants', variants), ('sizes', sizes), ('layout', layout), ('behavior', behavior), ('accessibility', access), ('related', related), ('references', references)]

# ---------------------------------------------------------------- Specifications
st_tok = '<h2 class="ds-h2">Design Tokens</h2>' + desc('Resolved from the live token package.') + \
    '<div class="ds-table-wrap"><table class="ds-table" id="tok-table"><thead><tr><th scope="col">Mode · state</th><th scope="col">Part</th><th scope="col">Token</th><th scope="col">Value</th></tr></thead><tbody></tbody></table></div>' + \
    note('<strong>Open points:</strong> two colors have no token: the hover On track (<code>#71b790</code>) and the disabled On track (<code>rgba(36, 134, 22, 0.5)</code>). They are written out with a comment.')

st_sizes = '<h2 class="ds-h2">Sizes</h2>' + table(['Size', 'Track', 'Thumb', 'Inset', 'Travel', 'Label'], [
    ['Large', '48×24px', '20px', '2px', '24px', '<code>body-md</code>: 16/22, from 769px 17/24, 0.32px'], ['Small', '48×24px', '20px', '2px', '24px', '<code>body-sm</code>: 14/20, 0.36px'], ['X-Small', '32×16px', '12px', '2px', '16px', '<code>body-sm</code>: 14/20, 0.36px']]) + \
    note('The size does not change with the breakpoint; only the Large label does.')

st_meas = '<h2 class="ds-h2">Measurements</h2><h3 class="ds-h3 ds-group">Dimensions</h3>' + table(['Attribute', 'Large and Small', 'X-Small'], [
    ['Track', '48×24px, a pill (<code>border-radius: 999px</code>)', '32×16px'], ['Thumb', '20px circle', '12px circle'], ['Inset, thumb to track edge', '2px', '2px'], ['Travel of the thumb', '24px', '16px'], ['Gap to the label', '8px', '8px'], ['Focus ring', '2px line, 2px offset', '2px line, 2px offset'], ['Label line height', '22px mobile, 24px from 769px (Large); 20px (Small)', '20px']]) + \
    note('A switch has no padding or margin of its own, so there is no measurement figure: the track is the box and the thumb sits 2px inside it.') + \
    '<h3 class="ds-h3 ds-group">Spacing</h3>' + desc('The gap to the label as a spacing token.') + table(['Part', 'Value'], [['Gap, track to label', '<code>space-8</code>'], ['Thumb inset', '2px: literal, no spacing token'], ['Focus ring offset', '2px']])

st_states = '<h2 class="ds-h2">States</h2>' + desc('Enabled, hover, focus and disabled, each off and on. Hover and focus are forced on this page; in your code they come from <code>:hover</code> and <code>:focus-visible</code>.') + \
    toolbar([('sm-l', 'Mode', 'data-mode-toggle', [('light', 'Light', True), ('dark', 'Dark', False)]), ('sb-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force'), ('ss-l', 'Size', 'data-mx="size"', [('lg', 'Large', True), ('sm', 'Small', False), ('xs', 'X-Small', False)])]) + \
    '<div class="ds-table-wrap" data-mode-stage-bg><table class="ds-table pg-matrix" id="matrix"><thead><tr><th scope="col">State</th><th scope="col">Off</th><th scope="col">On</th></tr></thead><tbody></tbody></table></div>'

st_typo = '<h2 class="ds-h2">Typography</h2>' + table(['Part', 'Type', 'Size / line height', 'Letter spacing', 'Weight'], [['Label, Large', '<code>body-md</code>', '16/22 mobile, 17/24 from 769px', '0.32px', 'Regular'], ['Label, Small and X-Small', '<code>body-sm</code>', '14/20', '0.36px', 'Regular']]) + \
    note('Breuer Condensed with <code>ss02</code>, <code>ss03</code> and <code>ss06</code>. Some desktop Small and X-Small variants in Figma imply a smaller width than the 14px label: the CSS uses 14/20 for both.')

st_struct = '<h2 class="ds-h2">Structure</h2><h3 class="ds-h3 ds-group">Elements</h3>' + table(['Element', 'Class', 'Notes'], [
    ['Item', '<code>form-switch-item</code>, <code>--sm</code>, <code>--xs</code>, <code>--dark</code>', 'The <code>label</code> around the input and the text.'], ['Track and thumb', '<code>input[type="checkbox"][role="switch"]</code>', '<code>appearance: none</code> on the native input. The thumb is its <code>::before</code>.'], ['Label text', '<code>span</code>', 'Optional. Without it the input needs an <code>aria-label</code>.']]) + \
    '<h3 class="ds-h3 ds-group">Types</h3>' + table(['Type', 'Class', 'Use'], [['Large', '<code>form-switch-item</code>', 'The default.'], ['Small', '<code>form-switch-item--sm</code>', 'Same track, smaller label.'], ['X-Small', '<code>form-switch-item--xs</code>', 'Dense layouts: 32×16px track.'], ['Dark', '<code>form-switch-item--dark</code>', 'On <code>surface-100</code> or <code>surface-80</code>.']]) + \
    '<h3 class="ds-h3 ds-group">Width</h3>' + desc('An item is as wide as the track plus its label.')

st_motion = '<h2 class="ds-h2">Motion</h2>' + table(['Property', 'Duration', 'Easing'], [['<code>background-color</code> of the track', '<code>duration-fast-3</code>', '<code>ease-standard</code>'], ['<code>transform</code> of the thumb', '<code>duration-fast-3</code>', '<code>ease-standard</code>']]) + \
    note('Reduced motion (<code>prefers-reduced-motion: reduce</code>) turns the transition off. Figma specifies no thumb animation: this is the default for form elements in <code>eco-motion</code>. <strong>Open point:</strong> confirm with design.')

st_behavior = '<h2 class="ds-h2">Behavior</h2>' + table(['Input', 'Result'], [
    ['Click switch or label', 'Toggles on and off, and the change applies at once.'], ['Space', 'Toggles the focused switch.'], ['Tab', 'The ring shows on keyboard focus only (<code>:focus-visible</code>), for both off and on.'],
    ['Markup', 'A native <code>input type="checkbox" role="switch"</code> inside a <code>label</code>. Never a <code>div</code> or <code>button</code> imitation.'], ['Disabled', 'Not focusable. Muted track, no thumb shadow, <code>text-disabled</code> label.'], ['Motion', 'Reduced motion turns the transition off.']])

st_access = '<h2 class="ds-h2">Accessibility Requirements</h2>' + table(['Topic', 'Requirement'], [
    ['Element', 'A native <code>&lt;input type="checkbox" role="switch"&gt;</code> in a <code>&lt;label&gt;</code>. The name, the role and the on/off state are announced.'], ['Name', 'A visible label, or <code>aria-label</code> when the setting is named by its surroundings.'], ['Focus', 'Ring with <code>border-focus</code>, 2px, offset 2px, on <code>:focus-visible</code> (WCAG 2.4.7, 1.4.11).'],
    ['Color', 'On and off differ in the position of the thumb as well as the track color (WCAG 1.4.1).'], ['Effect', 'The change applies at once. A switch that needs a Save button is a checkbox.'], ['Motion', 'Reduced motion turns the transition off (WCAG 2.3.3).'], ['Disabled', 'Not focusable. Disabled tokens are exempt from contrast requirements.']])

spec = [('design-tokens', st_tok), ('sizes', st_sizes), ('measurements', st_meas), ('states', st_states), ('typography', st_typo), ('structure', st_struct), ('motion', st_motion), ('behavior', st_behavior), ('accessibility-requirements', st_access)]

# ---------------------------------------------------------------- Code
c_basic = '<h2 class="ds-h2">Basic Usage</h2>' + desc('Link the shared stylesheet once per page. Never copy the rules into a page, and never build the switch from a <code>div</code> or a <code>button</code>.') + table(['Step', 'What to do'], [
    ['1. Link', '<code>&lt;link rel="stylesheet" href="/components/css/switch.css"&gt;</code>. Both templates already have it.'], ['2. Markup', 'A <code>label.form-switch-item</code> around an <code>input type="checkbox" role="switch"</code> and a <code>span</code> with the label text.'],
    ['3. Size', 'Large is the default. Add <code>form-switch-item--sm</code> or <code>form-switch-item--xs</code>.'], ['4. Dark surface', 'Add <code>form-switch-item--dark</code> on <code>surface-100</code> or <code>surface-80</code>.'], ['5. Effect', 'Listen for <code>change</code> and apply the setting at once.']])
c_sw = '<h2 class="ds-h2">Switch</h2>' + desc('Copy the markup you need. Hover and focus come from <code>:hover</code> and <code>:focus-visible</code>; the <code>[data-state]</code> selectors in the CSS exist only so the documentation can force a state.') + '<div id="recipes"></div>'
c_api = '<h2 class="ds-h2">API</h2><h3 class="ds-h3 ds-group">Classes</h3>' + table(['Class', 'Use'], [['<code>form-switch-item</code>', 'The label around the input and the text. Large, light.'], ['<code>form-switch-item--sm</code>', 'Small: same track, 14/20 label.'], ['<code>form-switch-item--xs</code>', 'X-Small: 32×16px track.'], ['<code>form-switch-item--dark</code>', 'Dark mode, for dark surfaces.']]) + \
    '<h3 class="ds-h3 ds-group">Things to know</h3>' + bullets(['The track is the native input with <code>appearance: none</code>; the thumb is its <code>::before</code>.', 'Breakpoint: the Large label is 16/22 below 769px and 17/24 from 769px. The CSS does this by itself.', 'Two colors have no token (the hover and disabled On track). They are written out in the CSS with a comment.', 'The <code>[data-state]</code> selectors do nothing outside the documentation pages.'])
c_css = '<h2 class="ds-h2">CSS / Tailwind</h2>' + desc('The component is one CSS file, shared by every page. Link it, never copy it. The CSS below is read from the file the page links, so it is always what you see.') + code_box('css-code', 'CSS (components/css/switch.css, light and dark)')
code = [('basic-usage', c_basic), ('switch', c_sw), ('api', c_api), ('css-tailwind', c_css, False)]

# ---------------------------------------------------------------- scripts
SW_JS = "  var uid = 0;\n" + old_js('switch', "  function sw(o) {", "  function applyMode()")

JS_EX = SW_JS + r'''
  var mode = 'light';
  var pg = { mode: 'light', size: 'lg', state: 'enabled', value: 'off' };
  var CLS = { lg: '', sm: ' form-switch-item--sm', xs: ' form-switch-item--xs' };
''' + old_js('switch', "  function renderPg() {", "  $$('[data-pg]').forEach") + r'''
  DK.wire(pg, renderPg); $('#pg-label').addEventListener('input', renderPg);
  DK.bp();

  function buildVariants() {
    var d = mode === 'dark';
    var s = clear($('#v-sizes'));
    [['lg', 'Large'], ['sm', 'Small'], ['xs', 'X-Small']].forEach(function (z) { s.appendChild(sw({ size: z[0], dark: d, on: z[0] !== 'sm', label: z[1] })); });
    var l = clear($('#v-list'));
    [['Email notifications', true], ['SMS notifications', false], ['Order updates', true], ['Newsletter', false]].forEach(function (r) { l.appendChild(sw({ dark: d, on: r[1], label: r[0] })); });
    l.appendChild(sw({ dark: d, state: 'disabled', label: 'Required service messages' }));
    var n = clear($('#v-nolabel'));
    n.appendChild(sw({ dark: d, aria: 'Row one' })); n.appendChild(sw({ dark: d, on: true, aria: 'Row two' })); n.appendChild(sw({ dark: d, size: 'xs', aria: 'Row three' }));
  }
  DK.mode(function (m) { mode = m; buildVariants(); });
  buildVariants();

  /* Usage figures */
  var fd = clear($('#fig-do')); fd.appendChild(sw({ on: true, label: 'Email notifications' })); fd.appendChild(sw({ label: 'SMS notifications' }));
  var fn = clear($('#fig-dont')); fn.appendChild(sw({ on: true, label: 'Email notifications' })); fn.appendChild(sw({ label: 'SMS notifications' }));
  var sv = document.createElement('button'); sv.type = 'button'; sv.className = 'btn btn--primary btn--sm'; sv.innerHTML = '<span class="btn__label">Save</span>'; fn.appendChild(sv);

  /* Anatomy */
  var an = $('#an-in');
  DK.callouts($('#sw-anat'), [
    { n: 1, el: an, side: 'top', len: 40, at: 'center' },
    { n: 2, side: 'bottom', len: 40, box: function () { var r = an.getBoundingClientRect(); return { left: r.left + 26, top: r.top + 2, width: 20, height: 20 }; } },
    { n: 3, el: $('#an-lbl'), side: 'top', len: 40, at: 'edge' }
  ]);
  renderPg();
'''

JS_SPEC = SW_JS + r'''
  var mode = 'light';
  var mx = { size: 'lg' };
  var ROWS = [['Enabled', 'enabled'], ['Hover', 'hover'], ['Focus', 'focus'], ['Disabled', 'disabled']];
  function buildMatrix() {
    var tb = clear($('#matrix tbody')), d = mode === 'dark';
    $('[data-mode-stage-bg]').classList.toggle('ds-stage--dark', d);
    ROWS.forEach(function (r) {
      var tr = document.createElement('tr'), th = document.createElement('th'); th.scope = 'row'; th.textContent = r[0]; tr.appendChild(th);
      [false, true].forEach(function (on) { var td = document.createElement('td'); td.appendChild(sw({ size: mx.size, dark: d, state: r[1], on: on, label: on ? 'On' : 'Off' })); tr.appendChild(td); });
      tb.appendChild(tr);
    });
  }
  DK.seg($('[data-mx="size"]'), function (v) { mx.size = v; buildMatrix(); });
  DK.mode(function (m) { mode = m; buildMatrix(); });
  DK.bp();
  buildMatrix();
  DK.tokenTable($('#tok-table tbody'), [
    ['Light · off', 'Track', 'surface-20'], ['Light · off hover', 'Track', 'surface-15'], ['Light · on', 'Track', 'surface-success-default'],
    ['Light · all', 'Thumb', 'surface-raised-primary'], ['Light · all', 'Focus ring', 'border-focus'], ['Light · all', 'Label', 'text-primary'],
    ['Light · disabled', 'Off track', 'surface-disabled'], ['Light · disabled', 'Label', 'text-disabled'],
    ['Dark · off', 'Track', 'surface-60'], ['Dark · off hover', 'Track', 'surface-50'], ['Dark · disabled', 'Off track', 'surface-80'], ['Dark · disabled', 'Thumb', 'surface-40'],
    ['Dark · all', 'Label', 'text-primary-inverted']]);
  DK.rows($('#tok-table tbody'), [
    ['Light · on hover', 'Track', '<em>no token</em>', '<span class="ds-dot" style="background:#71b790" aria-hidden="true"></span>#71b790'],
    ['Light · disabled', 'On track', '<em>no token</em>', '<span class="ds-dot" style="background:rgba(36, 134, 22, 0.5)" aria-hidden="true"></span>rgba(36, 134, 22, 0.5)'],
    ['Dark · on hover', 'Track', '<em>no token</em>', '<span class="ds-dot" style="background:#71b790" aria-hidden="true"></span>#71b790'],
    ['Dark · disabled', 'On track', '<em>no token</em>', '<span class="ds-dot" style="background:rgba(36, 134, 22, 0.5)" aria-hidden="true"></span>rgba(36, 134, 22, 0.5)']]);
'''

JS_CODE = r'''
  DK.recipes($('#recipes'), [
    ['Standard', '<label class="form-switch-item">\n  <input type="checkbox" role="switch" checked />\n  <span>Email notifications</span>\n</label>'],
    ['Small and X-Small', '<label class="form-switch-item form-switch-item--sm">\n  <input type="checkbox" role="switch" />\n  <span>Small</span>\n</label>\n<label class="form-switch-item form-switch-item--xs">\n  <input type="checkbox" role="switch" />\n  <span>X-Small</span>\n</label>'],
    ['Dark surface', '<label class="form-switch-item form-switch-item--dark">\n  <input type="checkbox" role="switch" />\n  <span>Dark mode</span>\n</label>'],
    ['Without a visible label', '<label class="form-switch-item">\n  <input type="checkbox" role="switch" aria-label="Email notifications for this row" />\n</label>'],
    ['Disabled', '<label class="form-switch-item">\n  <input type="checkbox" role="switch" checked disabled />\n  <span>Required service messages</span>\n</label>']
  ]);
  DK.printCss($('#css-code'), 'switch', [[/:is\(:hover, \[data-state="hover"\]\)/g, ':hover'], [/:is\(:focus-visible, \[data-state="focus"\]\)/g, ':focus-visible'], [/^ {4}/gm, '']]);
'''

C = dict(
    slug=SLUG, title='Switch', eyebrow='Components · Form',
    lead='A switch turns <strong>one setting on or off</strong> and applies the change at once. It is for a single binary choice, not for picking between options.',
    lead_ex='Every example on this page is the real component, not a picture. Click, tab and press Space to try it. Figma: ' + fig_link(FIGMA, 'Toggle Switch') + '.',
    lead_spec='Tokens, sizes, measurements, states and requirements. Values come from the live token package and from Figma: ' + fig_link(FIGMA, 'Toggle Switch') + '.',
    lead_code='How to add a switch to a page. The file is <code>components/css/switch.css</code>.',
    css=['switch'], style=STYLE, ex=ex, spec=spec, code=code, js_ex=JS_EX, js_spec=JS_SPEC, js_code=JS_CODE)

if __name__ == '__main__':
    emit(C)
