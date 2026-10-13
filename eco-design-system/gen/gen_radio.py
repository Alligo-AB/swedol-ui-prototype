from build import *

FIGMA = 'https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=1548-70504'
SLUG = 'radio'

STYLE = r'''    .pg-note { font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-tertiary); }
    .pg-matrix .form-radio-group { min-width: 200px; }
    .pg-matrix td { vertical-align: top; padding-top: 16px; padding-bottom: 16px; }
    .pg-col { display: flex; flex-direction: column; gap: 24px; width: 100%; max-width: 360px; }
    .pg-grid { display: grid; gap: 32px 24px; grid-template-columns: minmax(0, 1fr); width: 100%; }
    @media (min-width: 769px) { .pg-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
    .rd-fig { width: 100%; max-width: 320px; }
    .rd-fig .form-radio-group, .rd-fig fieldset { margin: 0; padding: 0; border: 0; }
    .rd-measure { display: inline-flex; }
    .rd-cbgroup { border: 0; margin: 0; padding: 0; display: flex; flex-direction: column; gap: var(--dimension-spacing-space-4); }
    .rd-cbgroup legend { padding: 0; margin-bottom: var(--dimension-spacing-space-8); font-size: 12px; font-weight: 600; line-height: 12px; letter-spacing: 0.48px; text-transform: uppercase; }
    @media (min-width: 769px) { .rd-cbgroup legend { font-size: 16px; line-height: 16px; } }
    .ds-callout__art { padding-right: 72px; }'''

playground = '<h2 class="ds-h2">Playground</h2>' + desc('Choose a breakpoint, size, state and value and the radio and its code update. Hover and focus are forced here so they can be seen. The radio is live: click it.') + \
    '<div class="ds-playground"><div class="ds-stage ds-stage--center"><div class="pg-col" id="pg-host"></div></div><div class="ds-controls">' + \
    bp_field('pg-l-bp') + btn_group('pg-l-size', 'Size', 'data-pg="size"', [('lg', 'Large', True), ('sm', 'Small', False)]) + \
    btn_group('pg-l-st', 'State', 'data-pg="state"', [('enabled', 'Enabled', True), ('hover', 'Hover', False), ('focus', 'Focus', False), ('disabled', 'Disabled', False)]) + \
    btn_group('pg-l-val', 'Value', 'data-pg="value"', [('off', 'Unselected', True), ('on', 'Selected', False)]) + \
    '<div class="ds-field form-field"><label class="form-label form-label--sm" for="pg-label">Label</label><div class="input-wrap"><div class="input-box input-box--sm"><input class="form-input" type="text" id="pg-label" value="Standard delivery" placeholder="Label" /></div></div></div>' + \
    '<div class="ds-field form-field"><label class="form-label form-label--sm" for="pg-hint">Message (optional)</label><div class="input-wrap"><div class="input-box input-box--sm"><input class="form-input" type="text" id="pg-hint" value="Delivered in 3 to 5 business days." placeholder="Message" /></div></div></div>' + \
    '</div></div><h3 class="ds-h3">Markup for this selection</h3>' + code_box('pg-code', 'HTML')

overview = '<h2 class="ds-h2">Overview</h2>' + desc('A radio button lets the user choose exactly one of two or more mutually exclusive options. Choosing one clears the others in the group.') + \
    desc('Radio has two sizes (Large, Small), eight states and an optional hint message under the label. It is a native <code>&lt;input type="radio"&gt;</code>, so grouping and arrow-key navigation come from the browser.') + \
    three_pages(SLUG, 'a radio button', 'the values: tokens, sizes, measurements, states and requirements', 'how to add one to a page')

usage = '<h2 class="ds-h2">Usage</h2><h3 class="ds-h3 ds-group">When to use</h3>' + desc('Use radio buttons when the user picks exactly one option from a short list and all options should be visible at once. Use them to:') + \
    bullets(['Present two or more mutually exclusive options where the user must pick exactly one', 'Choose a delivery method, a payment type or a size from a short list', 'Answer a yes/no question that is saved when the form is submitted']) + \
    desc('Preselect a default option in every group unless the user must choose consciously. It removes confusion and gives users a clear suggestion.') + \
    '<h3 class="ds-h3 ds-group">When not to use</h3><h3 class="ds-h3">Radio button or checkbox</h3>' + desc('A radio group allows only one choice. When several options can be chosen, use <code>eco-checkbox</code>.') + \
    fig_pair('<div class="rd-fig" id="fig-do"></div>', 'Do use radio buttons when only one option can be chosen.', '<div class="rd-fig" id="fig-dont"></div>', 'Do not use checkboxes for a choice between options. Use radio buttons instead.') + \
    '<h3 class="ds-h3">Always preselect a default</h3>' + desc('Preselect one option in every group unless the user must choose consciously. It removes confusion and gives users a clear suggestion.') + \
    fig_pair('<div class="rd-fig" id="fig-def-do"></div>', 'Do preselect a default option.', '<div class="rd-fig" id="fig-def-dont"></div>', 'Do not leave a group without a default.') + \
    '<h3 class="ds-h3">Stack the options</h3>' + desc('Stack options vertically: it is easier to scan. Horizontal only for two short options.') + \
    fig_pair('<div class="rd-fig" id="fig-ori-do"></div>', 'Do stack options vertically.', '<div class="rd-fig" id="fig-ori-dont"></div>', 'Do not lay out more than two options horizontally.') + \
    '<h3 class="ds-h3">For a setting, a view or a long list</h3>' + desc('For a setting that applies at once, use <code>eco-switch</code>. To switch between two related views or filters in the same surface, use <code>eco-pill-segment-control</code>. For one value from a long list, use <code>eco-select</code>.') + \
    '<h3 class="ds-h3 ds-group">Quick reference</h3>' + \
    table(['The user…', 'Use'], [['picks exactly one of two or more options', 'Radio'], ['picks any number of options, saved on submit', '<code>eco-checkbox</code>'], ['turns one setting on or off, with immediate effect', '<code>eco-switch</code>'], ['switches between two related views or filters', '<code>eco-pill-segment-control</code>'], ['picks one value from a long list', '<code>eco-select</code>']]) + \
    rules(['Preselect a default option in every group.', 'Stack options vertically and wrap input and text in one <code>label</code>.', 'Give the group a <code>legend</code>.', 'Use Small only in dense layouts.'],
          ['Use radios for multi-select. Use checkboxes instead.', 'Lay out more than two options horizontally.', 'Draw the circle with an image or SVG file.', 'Hardcode colors: use the tokens.'])

anatomy = '<h2 class="ds-h2">Anatomy</h2><h3 class="ds-h3 ds-group">Radio button</h3>' + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout" id="rd-anat" role="img" aria-label="Anatomy of a radio button: 1 area, 2 circle, 3 dot, 4 label, 5 message"><div class="ds-callout__art"><div class="form-radio-field"><label class="form-radio-item"><input type="radio" name="an" id="an-in" checked tabindex="-1" /><span id="an-lbl">Express</span></label><p class="form-radio-message" id="an-msg">Delivered next business day.</p></div></div></div></figure></div>' + \
    ol_parts([('Area', '24×24px: the circle plus a 4px margin. The margin leaves exactly room for the focus ring (2px gap plus 2px line), so focusing never shifts the layout.'), ('Circle', '16px with a 1px border (14px in Small).'), ('Dot', '6px, drawn as a radial gradient. It shows when the radio is selected.'),
              ('Label', '<code>body-md</code> (Large) or <code>body-sm</code>, 8px from the circle. The whole label is the click target.'), ('Message', 'Optional hint, <code>body-sm</code>, <code>text-tertiary</code>, 4px below the label.')])

variants = '<h2 class="ds-h2">Variants</h2>' + desc('Radio buttons are used in groups. The patterns below show the group with a default, the optional hint message and a disabled group. Use the Breakpoint toggle to preview the Large label on desktop (17/24) and mobile (16/22).') + \
    toolbar([('vb-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force')]) + \
    '<h3 class="ds-h3 ds-group">Group with a default</h3>' + desc('Related options sit in a <code>fieldset</code> with a <code>legend</code>, stacked vertically, with one option preselected. A hint message sits under the label of the option it explains.') + fig_one('<div class="pg-grid" id="v-group"></div>') + \
    '<h3 class="ds-h3 ds-group">Disabled</h3>' + desc('A disabled group keeps the selection visible.') + fig_one('<div class="pg-grid" id="v-disabled"></div>')

sizes = '<h2 class="ds-h2">Sizes</h2>' + desc('<strong>Large</strong> is the default. <strong>Small</strong> (class <code>.form-radio-item--sm</code>) is for dense layouts. The size does not change with the breakpoint; only the Large label does. Measurements are under ' + sec_link(SLUG, 'sizes', 'Sizes') + ' in Specifications.') + \
    fig_one('<div class="pg-grid" id="v-sizes"></div>')

layout = '<h2 class="ds-h2">Layout &amp; Appearance</h2><h3 class="ds-h3 ds-group">Orientation</h3>' + desc('Stack options vertically: it is easier to scan. Horizontal only for two short options: it hides the link between radio and label for longer lists.') + fig_one('<div class="pg-grid" id="v-orient"></div>') + \
    '<h3 class="ds-h3 ds-group">Appearance</h3>' + desc('A radio is a 16px circle with a 1px grey border. When it is selected the border turns black and a 6px dot appears. Token names and values are under ' + sec_link(SLUG, 'design-tokens', 'Design Tokens') + ' in Specifications.')

behavior = '<h2 class="ds-h2">Behavior</h2><h3 class="ds-h3 ds-group">Selecting</h3>' + desc('A click on the circle or the label selects that option and clears the others in the group.') + \
    '<h3 class="ds-h3 ds-group">Hover and focus</h3>' + desc('Hover gives the circle a grey fill and a darker border. The focus ring shows with <code>:focus-visible</code> only. All states are listed under ' + sec_link(SLUG, 'states', 'States') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Default</h3>' + desc('Preselect one option in every group unless the user must choose consciously.') + \
    '<h3 class="ds-h3 ds-group">Disabled</h3>' + desc('A disabled radio is not focusable. It has a grey fill, a light border and a <code>text-disabled</code> label and message.')

access = '<h2 class="ds-h2">Accessibility</h2>' + desc('All requirements are listed under ' + sec_link(SLUG, 'accessibility-requirements', 'Accessibility Requirements') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Keyboard support</h3>' + desc('Tab enters the group once, on the selected radio or on the first one. The arrow keys move to and select the next or previous option. This works when every radio shares one <code>name</code>.') + \
    '<h3 class="ds-h3 ds-group">Screen reader support</h3>' + desc('Put the group in a <code>fieldset</code> with a <code>legend</code>, so the question is read together with each option. Wrap the input and the text in one <code>label</code>.')

related = '<h2 class="ds-h2">Related</h2><ul class="ds-bullets"><li><strong>' + link_large('checkbox.html', 'Checkbox') + '</strong>. Any number of options. The checkbox tiles can also be used as radios on a product page.</li><li><strong>' + link_large('switch.html', 'Switch') + '</strong>. An on/off setting with immediate effect.</li><li><strong>' + link_large('segment-control.html', 'Pill segment control') + '</strong>. A switch between two related views.</li><li><strong>' + link_large('select.html', 'Select') + '</strong>. One value from a long list.</li></ul>'

references = '<h2 class="ds-h2">References</h2>' + refs([
    ('https://www.w3.org/WAI/ARIA/apg/patterns/radio/', 'WAI-ARIA Authoring Practices: Radio Group', 'Keyboard and role requirements.'),
    ('https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html', 'WCAG 2.2: Non-text Contrast', 'Success criterion 1.4.11, for the circle border and the focus ring.'),
    ('https://www.nngroup.com/articles/checkboxes-vs-radio-buttons/', 'Nielsen Norman Group: Checkboxes vs. Radio Buttons', 'When to use which.'),
    ('https://fluent2.microsoft.design/components/web/react/core/radio/usage', 'Fluent 2: Radio', 'Microsoft.'),
    ('https://m3.material.io/components/radio-button/overview', 'Material Design 3: Radio button', 'Google.'),
    ('https://carbondesignsystem.com/components/radio-button/usage/', 'Carbon Design System: Radio button', 'IBM.')])

ex = [('playground', playground), ('overview', overview), ('usage', usage), ('anatomy', anatomy), ('variants', variants), ('sizes', sizes), ('layout', layout), ('behavior', behavior), ('accessibility', access), ('related', related), ('references', references)]

# ---------------------------------------------------------------- Specifications
st_tok = '<h2 class="ds-h2">Design Tokens</h2>' + desc('Resolved from the live token package.') + \
    '<div class="ds-table-wrap"><table class="ds-table" id="tok-table"><thead><tr><th scope="col">State</th><th scope="col">Part</th><th scope="col">Token</th><th scope="col">Value</th></tr></thead><tbody></tbody></table></div>'

st_sizes = '<h2 class="ds-h2">Sizes</h2>' + table(['Size', 'Total area', 'Circle', 'Margin', 'Dot', 'Label'], [
    ['Large', '24×24px', '16px', '4px', '6px', '<code>body-md</code>: 16/22, from 769px 17/24, 0.32px'], ['Small', '20×20px', '14px', '3px', '6px', '<code>body-sm</code>: 14/20, 0.36px']]) + \
    note('Only Large and Small exist. The hint message is <code>body-sm</code> (14/20, 0.36px) in both. The 1px border has no width token (<code>--border-brd-1</code> is a full shorthand), so <code>1px</code> is written out.')


def mfig(n, name, cls):
    return ('<div class="measure__item"><span class="measure__name">%d · %s</span><div class="measure__obj"><span class="rd-measure"><label class="form-radio-item%s"><input type="radio" name="m%d" class="measure__subject" data-measure-margin tabindex="-1" aria-label="%s" /></label></span>'
            '<i class="measure__pad measure__pad--t"></i><i class="measure__pad measure__pad--b"></i><i class="measure__pad measure__pad--l"></i><i class="measure__pad measure__pad--r"></i>'
            '<b class="measure__dim measure__dim--v measure__dim--t"><span></span></b><b class="measure__dim measure__dim--v measure__dim--b"><span></span></b><b class="measure__dim measure__dim--h measure__dim--l"><span></span></b><b class="measure__dim measure__dim--h measure__dim--r"><span></span></b></div></div>') % (n, name, cls, n, name)


st_meas = '<h2 class="ds-h2">Measurements</h2><h3 class="ds-h3 ds-group">Dimensions</h3>' + desc('Circle and margin of each size. The shaded area is the 4px margin (3px in Small) that leaves room for the focus ring; the lines show its value.') + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-fig__stage--flush" style="padding:0;min-height:0"><div class="measure" role="img" aria-label="Margin of the radio button: Large 4 on every side, Small 3 on every side" style="--k:4">' + mfig(1, 'Large', '') + mfig(2, 'Small', ' form-radio-item--sm') + '</div></div><figcaption class="ds-fig__cap">The circle at 4× size. The numbers are read from the component and are real pixels.</figcaption></figure></div>' + \
    table(['Attribute', 'Large', 'Small (<code>.form-radio-item--sm</code>)'], [['Area', '24×24px', '20×20px'], ['Circle', '16px, 1px border', '14px, 1px border'], ['Margin around the circle', '4px', '3px'], ['Dot', '<td colspan="2">6px, a radial gradient</td>'], ['Focus ring', '2px line, 2px offset', '2px line, 2px offset'], ['Gap, circle to label', '8px', '8px'], ['Gap, label to message', '4px', '4px']]) + \
    '<h3 class="ds-h3 ds-group">Spacing</h3>' + desc('The same margin and gaps as spacing tokens.') + table(['Part', 'Large', 'Small'], [['Margin around the circle', '<code>space-4</code>', '3px: no spacing token'], ['Gap circle to label', '<code>space-8</code>', '<code>space-8</code>'], ['Gap label to message', '<code>space-4</code>', '<code>space-4</code>'], ['Gap between options in a group', '<code>space-4</code>', '<code>space-4</code>']]) + \
    note('There is no spacing token for 3px. The Small margin is 3px in Figma. <strong>Open point:</strong> keep 3px, or add a token.')

st_states = '<h2 class="ds-h2">States</h2>' + desc('All eight states from Figma. Hover and focus are forced on this page; in your code they come from <code>:hover</code> and <code>:focus-visible</code>. “Selected” rows are Selected, Selected hover, Selected focus and Disabled selected.') + \
    toolbar([('sb-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force'), ('ss-l', 'Size', 'data-mx="size"', [('lg', 'Large', True), ('sm', 'Small', False)])]) + \
    '<div class="ds-table-wrap"><table class="ds-table pg-matrix" id="matrix"><thead><tr><th scope="col">State</th><th scope="col">Unselected</th><th scope="col">Selected</th></tr></thead><tbody></tbody></table></div>'

st_typo = '<h2 class="ds-h2">Typography</h2>' + table(['Part', 'Type', 'Size / line height', 'Letter spacing', 'Weight'], [
    ['Label, Large', '<code>body-md</code>', '16/22 mobile, 17/24 from 769px', '0.32px', 'Regular'], ['Label, Small', '<code>body-sm</code>', '14/20', '0.36px', 'Regular'], ['Message', '<code>body-sm</code>', '14/20', '0.36px', 'Regular'],
    ['Legend', '<code>label-sm</code> (mobile), <code>label-md</code> (desktop)', '12/12 mobile, 16/16 from 769px', '0.48px', 'Bold, uppercase']]) + note('Breuer Condensed with <code>ss02</code>, <code>ss03</code> and <code>ss06</code> for the label. The disabled label and message use <code>text-disabled</code>.')

st_struct = '<h2 class="ds-h2">Structure</h2><h3 class="ds-h3 ds-group">Elements</h3>' + table(['Element', 'Class', 'Notes'], [
    ['Group', '<code>form-radio-group</code>', 'A <code>fieldset</code> with a <code>legend</code>. Vertical by default, options 4px apart.'], ['Option', '<code>form-radio-item</code>, <code>--sm</code>', 'The <code>label</code> around the input and the text.'], ['Circle and dot', '<code>input[type="radio"]</code>', '<code>appearance: none</code> on the native input. The dot is a radial gradient.'],
    ['Option with message', '<code>form-radio-field</code>', 'Wraps the option and its message.'], ['Message', '<code>form-radio-message</code>', 'Optional hint, 4px below the label.']]) + \
    '<h3 class="ds-h3 ds-group">Types</h3>' + table(['Type', 'How', 'Use'], [['Vertical group', 'Default', 'Any number of options.'], ['Horizontal group', '<code>flex-direction: row</code> on the group', 'Two short options only.'], ['With message', '<code>form-radio-field</code>', 'An option that needs an explanation.'], ['Small', '<code>form-radio-item--sm</code>', 'Dense layouts.']]) + \
    '<h3 class="ds-h3 ds-group">Width</h3>' + desc('An option is as wide as its label. The click target is the whole label.')

st_motion = '<h2 class="ds-h2">Motion</h2>' + note('None. The radio changes state at once, with no transition and no animation.')

st_behavior = '<h2 class="ds-h2">Behavior</h2>' + table(['Input', 'Result'], [
    ['Click circle or label', 'Selects that option and clears the others in the group.'], ['Tab', 'Enters the group once (the selected radio, or the first). The ring shows on keyboard focus only.'], ['Arrow keys', 'Move and select the next or previous option in the group. Native: needs the same <code>name</code>.'],
    ['Group', '<code>fieldset</code> with a <code>legend</code>; every radio shares one <code>name</code>.'], ['Disabled', 'Not focusable. Grey fill, light border, <code>text-disabled</code> label and message.'], ['Default', 'Preselect one option in every group unless the user must choose consciously.']])

st_access = '<h2 class="ds-h2">Accessibility Requirements</h2>' + table(['Topic', 'Requirement'], [
    ['Element', 'A native <code>&lt;input type="radio"&gt;</code>. The role, the state and the arrow-key behavior come from the browser.'], ['Group', 'A <code>&lt;fieldset&gt;</code> with a <code>&lt;legend&gt;</code>; every radio shares one <code>name</code>.'], ['Name', 'The input and the text are wrapped in one <code>&lt;label&gt;</code>.'],
    ['Focus', 'Ring with <code>border-focus</code>, 2px, offset 2px, on <code>:focus-visible</code> (WCAG 2.4.7, 1.4.11).'], ['Color', 'Selected is not shown by color alone: the dot is a shape and the border is thicker in color.'], ['Disabled', 'Not focusable. Disabled tokens are exempt from contrast requirements.']])

spec = [('design-tokens', st_tok), ('sizes', st_sizes), ('measurements', st_meas), ('states', st_states), ('typography', st_typo), ('structure', st_struct), ('motion', st_motion), ('behavior', st_behavior), ('accessibility-requirements', st_access)]

# ---------------------------------------------------------------- Code
c_basic = '<h2 class="ds-h2">Basic Usage</h2>' + desc('Link the shared stylesheet once per page. Never copy the rules into a page, and never draw the circle with an image.') + table(['Step', 'What to do'], [
    ['1. Link', '<code>&lt;link rel="stylesheet" href="/components/css/radio.css"&gt;</code>. Both templates already have it.'], ['2. Markup', 'A <code>fieldset.form-radio-group</code> with a <code>legend</code>. Each option is a <code>label.form-radio-item</code> around an <code>input[type="radio"]</code> and a <code>span</code>.'],
    ['3. Group', 'Give every radio in the group the same <code>name</code>, and preselect one with <code>checked</code>.'], ['4. Size', 'Large is the default. Add <code>form-radio-item--sm</code> for Small.']])
c_rd = '<h2 class="ds-h2">Radio button</h2>' + desc('Copy the markup you need. Hover and focus come from <code>:hover</code> and <code>:focus-visible</code>; the <code>[data-state]</code> selectors in the CSS exist only so the documentation can force a state.') + '<div id="recipes"></div>'
c_api = '<h2 class="ds-h2">API</h2><h3 class="ds-h3 ds-group">Classes</h3>' + table(['Class', 'Use'], [
    ['<code>form-radio-group</code>', 'The <code>fieldset</code>. Vertical by default.'], ['<code>form-radio-item</code>', 'The option label. Large.'], ['<code>form-radio-item--sm</code>', 'Small size.'], ['<code>form-radio-field</code>', 'Wraps an option and its message.'], ['<code>form-radio-message</code>', 'The hint under the label.']]) + \
    '<h3 class="ds-h3 ds-group">Things to know</h3>' + bullets(['The circle is the native input with <code>appearance: none</code>. The dot is a radial gradient, so no image file is loaded.', 'Arrow-key navigation needs the same <code>name</code> on every radio of a group.', 'For a horizontal group set <code>flex-direction: row</code> on the <code>fieldset</code> (two short options only).', 'Breakpoint: the Large label is 16/22 below 769px and 17/24 from 769px. The CSS does this by itself.', 'The <code>[data-state]</code> selectors do nothing outside the documentation pages.'])
c_css = '<h2 class="ds-h2">CSS / Tailwind</h2>' + desc('The component is one CSS file, shared by every page. Link it, never copy it. The CSS below is read from the file the page links, so it is always what you see.') + code_box('css-code', 'CSS (components/css/radio.css)')
code = [('basic-usage', c_basic), ('radio-button', c_rd), ('api', c_api), ('css-tailwind', c_css, False)]

# ---------------------------------------------------------------- scripts
RADIO_JS = "  var uid = 0;\n" + old_js('radio', "  /* Build a real radio item.", "  /* Playground */")

JS_EX = RADIO_JS + r'''
  var pg = { size: 'lg', state: 'enabled', value: 'off' };
''' + old_js('radio', "  function renderPg() {", "  $$('[data-pg]').forEach") + r'''
  DK.wire(pg, renderPg);
  $('#pg-label').addEventListener('input', renderPg); $('#pg-hint').addEventListener('input', renderPg);
  DK.bp();

  /* Usage figures: radios for one choice (do), radios for a multi-select question (don't) */
  clear($('#fig-do')).appendChild(group('Delivery', [radio({ checked: true, label: 'Standard', name: 'fdo' }), radio({ label: 'Express', name: 'fdo' }), radio({ label: 'Pick up', name: 'fdo' })]));
  var dn = clear($('#fig-dont')); dn.innerHTML = '<fieldset class="rd-cbgroup"><legend>Delivery</legend></fieldset>'; ['Standard', 'Express', 'Pick up'].forEach(function (t, n) { var l = document.createElement('label'); l.className = 'form-checkbox-item'; l.innerHTML = '<input type="checkbox"' + (n === 0 ? ' checked' : '') + ' /><span></span>'; l.querySelector('span').textContent = t; $('fieldset', dn).appendChild(l); });

  var opts4 = ['Standard', 'Express', 'Pick up', 'Courier'];
  function four(name, hz, none) { return group('Delivery', opts4.map(function (t, i) { return radio({ checked: !none && i === 0, label: t, name: name }); }), hz); }
  clear($('#fig-def-do')).appendChild(group('Delivery', [radio({ checked: true, label: 'Standard', name: 'fdd' }), radio({ label: 'Express', name: 'fdd' }), radio({ label: 'Pick up', name: 'fdd' })]));
  clear($('#fig-def-dont')).appendChild(group('Delivery', [radio({ label: 'Standard', name: 'fdn' }), radio({ label: 'Express', name: 'fdn' }), radio({ label: 'Pick up', name: 'fdn' })]));
  clear($('#fig-ori-do')).appendChild(four('fod', false));
  clear($('#fig-ori-dont')).appendChild(four('fon', true));
  var g = clear($('#v-group'));
  g.appendChild(group('Delivery method', [radio({ checked: true, label: 'Standard', hint: 'Delivered in 3 to 5 business days.', name: 'gm' }), radio({ label: 'Express', hint: 'Delivered next business day.', name: 'gm' }), radio({ label: 'Pick up in store', name: 'gm' })]));
  g.appendChild(group('Delivery method, small', [radio({ size: 'sm', checked: true, label: 'Standard', hint: 'Delivered in 3 to 5 business days.', name: 'gs' }), radio({ size: 'sm', label: 'Express', hint: 'Delivered next business day.', name: 'gs' })]));
  var dg = clear($('#v-disabled'));
  dg.appendChild(group('Delivery method, unavailable', [radio({ state: 'disabled', checked: true, label: 'Standard', name: 'dg' }), radio({ state: 'disabled', label: 'Express', name: 'dg' })]));
  var sz = clear($('#v-sizes'));
  [['lg', 'Large'], ['sm', 'Small']].forEach(function (s) {
    var n = 'sz-' + s[0];
    sz.appendChild(group(s[1], [radio({ size: s[0], checked: true, label: 'Standard', name: n }), radio({ size: s[0], label: 'Express', name: n }), radio({ size: s[0], label: 'Pick up', name: n })]));
  });
  var or = clear($('#v-orient'));
  or.appendChild(group('Vertical (default)', [radio({ checked: true, label: 'Standard', name: 'ov' }), radio({ label: 'Express', name: 'ov' }), radio({ label: 'Pick up', name: 'ov' })]));
  or.appendChild(group('Horizontal: two short options', [radio({ checked: true, label: 'Yes', name: 'hz' }), radio({ label: 'No', name: 'hz' })], true));

  /* Anatomy */
  function txt(el) { return function () { var r = document.createRange(); r.selectNodeContents(el); return r.getBoundingClientRect(); }; }
  var an = $('#an-in');
  DK.callouts($('#rd-anat'), [
    { n: 1, side: 'left', len: 48, box: function () { var r = an.getBoundingClientRect(); return { left: r.left - 4, top: r.top - 4, width: 24, height: 24 }; } },
    { n: 2, el: an, side: 'top', len: 40 },
    { n: 3, side: 'bottom', len: 40, box: function () { var r = an.getBoundingClientRect(); return { left: r.left + 5, top: r.top + 5, width: 6, height: 6 }; } },
    { n: 4, box: txt($('#an-lbl')), side: 'top', len: 40 },
    { n: 5, box: txt($('#an-msg')), side: 'right', len: 48 }
  ]);
  renderPg();
'''

JS_SPEC = RADIO_JS + r'''
  var mx = { size: 'lg' };
  var ROWS = [['Enabled', 'enabled'], ['Hover / Selected hover', 'hover'], ['Focus / Selected focus', 'focus'], ['Disabled / Disabled selected', 'disabled']];
  function buildMatrix() {
    var tb = clear($('#matrix tbody'));
    ROWS.forEach(function (r) {
      var tr = document.createElement('tr'), th = document.createElement('th'); th.scope = 'row'; th.textContent = r[0]; tr.appendChild(th);
      [false, true].forEach(function (on) {
        var td = document.createElement('td'), n = 'mx-' + (uid++);
        td.appendChild(group('Group', [radio({ size: mx.size, state: r[1], checked: on, label: on ? 'Selected' : 'Unselected', name: n })])); tr.appendChild(td);
      });
      tb.appendChild(tr);
    });
  }
  DK.seg($('[data-mx="size"]'), function (v) { mx.size = v; buildMatrix(); });
  buildMatrix();
  DK.tokenTable($('#tok-table tbody'), [
    ['Enabled', 'Border', 'border-input-control-default'], ['Enabled', 'Fill', 'surface-raised-primary'],
    ['Hover', 'Fill', 'surface-opacity-black-05'], ['Hover', 'Border', 'border-hover'],
    ['Focus', 'Ring (2px, offset 2px)', 'border-focus'],
    ['Selected', 'Border', 'border-selected'], ['Selected', 'Dot', 'surface-100'], ['Selected hover', 'Border', 'border-selected-hover'],
    ['Disabled', 'Fill', 'surface-disabled'], ['Disabled', 'Border', 'border-disabled'], ['Disabled', 'Label, message', 'text-disabled'], ['Disabled selected', 'Dot', 'surface-50'],
    ['All', 'Label', 'text-primary'], ['All', 'Message', 'text-tertiary']]);
  DK.bp(function () { ECO_MEASURE.init(); });
'''

JS_CODE = r'''
  DK.recipes($('#recipes'), [
    ['Group with a default', '<fieldset class="form-radio-group">\n  <legend>Delivery method</legend>\n  <label class="form-radio-item">\n    <input type="radio" name="delivery" value="standard" checked />\n    <span>Standard</span>\n  </label>\n  <label class="form-radio-item">\n    <input type="radio" name="delivery" value="express" />\n    <span>Express</span>\n  </label>\n</fieldset>'],
    ['With a hint message', '<div class="form-radio-field">\n  <label class="form-radio-item">\n    <input type="radio" name="delivery" value="express" />\n    <span>Express</span>\n  </label>\n  <p class="form-radio-message">Delivered next business day.</p>\n</div>'],
    ['Small', '<label class="form-radio-item form-radio-item--sm">\n  <input type="radio" name="delivery" value="pickup" />\n  <span>Pick up</span>\n</label>'],
    ['Disabled', '<label class="form-radio-item">\n  <input type="radio" name="delivery" value="pickup" disabled />\n  <span>Pick up</span>\n</label>']
  ]);
  DK.printCss($('#css-code'), 'radio', [[/:is\(:hover, \[data-state="hover"\]\)/g, ':hover'], [/:is\(:focus-visible, \[data-state="focus"\]\)/g, ':focus-visible'], [/^ {4}/gm, '']]);
'''

C = dict(
    slug=SLUG, title='Radio button', eyebrow='Components · Form',
    lead='A radio button lets the user choose <strong>exactly one</strong> of two or more mutually exclusive options. Choosing one clears the others in the group.',
    lead_ex='Every example on this page is the real component, not a picture. Click, tab and use the arrow keys to try it. Specification: <code>.claude/skills/eco-radio/SKILL.md</code>. Figma: ' + fig_link(FIGMA, 'Radio Button') + '.',
    lead_spec='Tokens, sizes, measurements, states and requirements. Values come from the live token package and from Figma: ' + fig_link(FIGMA, 'Radio Button') + '.',
    lead_code='How to add a radio button to a page. The file is <code>components/css/radio.css</code>.',
    css=['radio', 'checkbox'], style=STYLE, ex=ex, spec=spec, code=code, js_ex=JS_EX, js_spec=JS_SPEC, js_code=JS_CODE)

if __name__ == '__main__':
    emit(C)
