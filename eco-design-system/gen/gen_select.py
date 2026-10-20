from build import *

FIGMA = 'https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=1475-44234'
SLUG = 'select'

STYLE = r'''    .pg-note { font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-tertiary); }
    .pg-matrix td { min-width: 260px; vertical-align: top; padding-top: 16px; padding-bottom: 16px; } .pg-matrix .form-field { min-width: 220px; }
    .pg-col { display: flex; flex-direction: column; gap: 24px; width: 100%; max-width: 360px; }
    .pg-grid { display: grid; gap: 32px 24px; grid-template-columns: minmax(0, 1fr); width: 100%; }
    @media (min-width: 769px) { .pg-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
    .sl-fig { width: 100%; max-width: 320px; }
    .sl-fig .form-radio-group { margin: 0; padding: 0; border: 0; }
    .sl-measure { display: block; width: 280px; }   /* demo: a fixed width, so the padding strips have a select to sit on */
    .sl-menu-room { min-height: 220px; }   /* room under the field for the open menu */
    .ds-callout__art { padding-right: 24px; width: 100%; max-width: 360px; }'''

playground = '<h2 class="ds-h2">Playground</h2>' + desc('Choose a breakpoint, size and state and the select and its code update. Hover and focus are forced here. The select is live: choose an option to get the Active state.') + \
    '<div class="ds-playground"><div class="ds-stage ds-stage--center"><div class="pg-col" id="pg-host"></div></div><div class="ds-controls">' + \
    bp_field('pg-l-bp') + btn_group('pg-l-size', 'Size', 'data-pg="size" data-size-toggle', [('lg', 'Large', True), ('sm', 'Small', False), ('xs', 'XSmall', False)]) + \
    '<div class="ds-field form-field"><label class="form-label form-label--sm" for="sel-pg-l-st" id="pg-l-st">State</label><div class="input-wrap"><select class="form-select form-select--sm" data-pg="state" id="sel-pg-l-st"><option value="enabled">Enabled</option><option value="hover">Hover</option><option value="active">Active</option><option value="focus">Focus</option><option value="error">Error</option><option value="success">Success</option><option value="disabled">Disabled</option></select><span class="form-select-arrow" aria-hidden="true">arrow_drop_down</span></div></div>' + \
    '<div class="ds-field form-field"><label class="form-label form-label--sm" for="pg-label">Label</label><div class="input-wrap"><div class="input-box input-box--sm"><input class="form-input" type="text" id="pg-label" value="Country" placeholder="Label" /></div></div></div>' + \
    '<div class="ds-field form-field"><label class="form-label form-label--sm" for="pg-hint">Message</label><div class="input-wrap"><div class="input-box input-box--sm"><input class="form-input" type="text" id="pg-hint" value="Where should we deliver?" placeholder="Message" /></div></div></div>' + \
    '</div></div><h3 class="ds-h3">Markup for this selection</h3>' + code_box('pg-code', 'HTML')

overview = '<h2 class="ds-h2">Overview</h2>' + desc('A select lets the user choose one option from a list. It looks and behaves like an input field, with a dropdown arrow. It opens the ECO Menu as its list.') + \
    desc('Select has three sizes on desktop (Large, Small, XSmall) and two on mobile (Large, Small), seven states and an optional message. It is a native <code>&lt;select&gt;</code>: the value, the label and the form submission come from the browser, and <code>select-menu.js</code> only replaces the popup.') + \
    three_pages(SLUG, 'a select', 'the values: tokens, sizes, measurements, states and requirements', 'how to add one to a page')

usage = '<h2 class="ds-h2">Usage</h2><h3 class="ds-h3 ds-group">When to use</h3>' + desc('Use a select when the user picks one value from a list of more than about five options. Use it to:') + \
    bullets(['Choose a country, a region or a store from a long list', 'Pick one value where a list of radio buttons would take too much space', 'Filter or sort a list in a compact surface (Small or XSmall)']) + \
    '<h3 class="ds-h3 ds-group">When not to use</h3><h3 class="ds-h3">Select or radio buttons</h3>' + desc('For two to five options, show them all with <code>eco-radio</code>: the user sees every option without opening anything. For a longer list use a select, so the list does not take over the form.') + \
    fig_pair('<div class="sl-fig" id="fig-do"></div>', 'Do use a select for a long list of options.', '<div class="sl-fig" id="fig-dont"></div>', 'Do not list many options as radio buttons. Use a select instead.') + \
    '<h3 class="ds-h3">Label and placeholder</h3>' + desc('A placeholder is not a label: it is replaced once an option is chosen. Every select has a visible label, and the placeholder option only prompts the user.') + \
    fig_pair('<div class="sl-fig" id="fig-lab-do"></div>', 'Do give every select a visible label.', '<div class="sl-fig" id="fig-lab-dont"></div>', 'Do not use the placeholder as the label.') + \
    '<h3 class="ds-h3">For several values or free text</h3>' + desc('When the user picks any number of options, use <code>eco-checkbox</code>. When the user types free text, use <code>eco-input</code>.') + \
    '<h3 class="ds-h3 ds-group">Quick reference</h3>' + \
    table(['The user…', 'Use'], [['picks one value from a list of more than about five', 'Select'], ['picks one of two to five options', '<code>eco-radio</code>'], ['picks any number of options', '<code>eco-checkbox</code>'], ['types free text', '<code>eco-input</code>']]) + \
    rules(['Give every select a visible label.', 'Use a placeholder option with an empty value as the prompt.', 'Pick the size by breakpoint, like the input.', 'Show the message with the error icon.'],
          ['Use a select for two or three options: use radio.', 'Use the placeholder as the label.', 'Rely on color alone for error or success.', 'Hardcode colors or heights: use the tokens and size classes.'])

anatomy = '<h2 class="ds-h2">Anatomy</h2><h3 class="ds-h3 ds-group">Select</h3>' + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout" id="sl-anat" role="img" aria-label="Anatomy of a select: 1 label, 2 select text, 3 arrow, 4 message"><div class="ds-callout__art"><div class="pg-col" id="a-host"></div></div></div></figure></div>' + \
    ol_parts([('Label', '<code>label-md</code> or <code>label-sm</code>, uppercase, 4px above the box.'), ('Select text', '<code>body-md</code> (Large) or <code>body-sm</code>. The placeholder is <code>text-tertiary</code>.'), ('Arrow', 'A 24px Material Symbols icon, 12px from the right edge. The field keeps 40px of right padding so text never runs under it.'), ('Message', '<code>body-sm</code>, 4px below the box. Hint, error or success.')]) + \
    desc('The focus ring is a separate element around the box, 2px and 3px outside it, so focusing never changes the layout or the box size.') + \
    '<h3 class="ds-h3 ds-group">Menu</h3>' + desc('The list is the ECO Menu (<code>eco-menu</code>): it opens under the field, as wide as the field. A Large field opens a Large menu; Small and XSmall open a Small menu.')

variants = '<h2 class="ds-h2">Variants</h2>' + desc('A select has no type variants. What changes is the message and the state.') + \
    '<h3 class="ds-h3 ds-group">Messages</h3>' + desc('The message sits below the field in <code>body-sm</code>. Hint text is neutral; error and success change the border and message color. An error message has a leading icon so color is never the only signal.') + fig_one('<div class="pg-grid" id="v-messages"></div>')

sizes = '<h2 class="ds-h2">Sizes</h2>' + desc('Three sizes on desktop (Large 48px, Small 40px, XSmall 32px) and two on mobile (Large 40px, Small 32px). Use the Breakpoint toggle to preview Desktop (769px and up) and Mobile (below 769px).') + \
    toolbar([('vb-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force')]) + \
    desc('<strong>Large</strong> is for standard forms, <strong>Small</strong> for compact surfaces, <strong>XSmall</strong> for dense tables and filters (desktop only: on mobile it is not available, use Small). The list is the Menu: Large field opens a Large menu, Small and XSmall open a Small menu. Measurements are under ' + sec_link(SLUG, 'sizes', 'Sizes') + ' in Specifications.') + \
    fig_one('<div class="pg-grid" id="v-sizes"></div>')

layout = '<h2 class="ds-h2">Layout &amp; Appearance</h2><h3 class="ds-h3 ds-group">Width</h3>' + desc('The field is as wide as its container, and the menu is as wide as the field. Set the width on the container.') + \
    '<h3 class="ds-h3 ds-group">Appearance</h3>' + desc('The box has a 1px border and a white fill, like the input, with a dropdown arrow on the right. The border turns black when the field is in use or has a value. Token names and values are under ' + sec_link(SLUG, 'design-tokens', 'Design Tokens') + ' in Specifications.')

behavior = '<h2 class="ds-h2">Behavior</h2><h3 class="ds-h3 ds-group">Opening the menu</h3>' + desc('A click opens the Menu under the field (no ring on mouse). Click a row to choose; click outside to close. Try it:') + \
    fig_one('<div class="sl-fig sl-menu-room" id="v-live"></div>') + \
    '<h3 class="ds-h3 ds-group">Placeholder</h3>' + desc('A first option with <code>value=""</code> (disabled, hidden) shows the placeholder in <code>text-tertiary</code>.') + \
    '<h3 class="ds-h3 ds-group">Hover and focus</h3>' + desc('Hover is <code>border-hover</code>. On keyboard focus the box keeps <code>border-input-default</code> and only the ring shows, like the input. All states are listed under ' + sec_link(SLUG, 'states', 'States') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Error, success and disabled</h3>' + desc('Set <code>aria-invalid="true"</code> on an invalid field and point <code>aria-describedby</code> at the message. A disabled select is not focusable: it has a grey fill, a light border and <code>text-disabled</code> text and arrow.')

access = '<h2 class="ds-h2">Accessibility</h2>' + desc('All requirements are listed under ' + sec_link(SLUG, 'accessibility-requirements', 'Accessibility Requirements') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Keyboard support</h3>' + desc('Enter, Space and the arrow keys open the Menu on the chosen row. Up and Down, Home and End move; Enter or Space choose; Escape closes and returns focus to the field; Tab closes.') + \
    '<h3 class="ds-h3 ds-group">Screen reader support</h3>' + desc('The control stays a native <code>select</code> with a <code>label</code> (<code>for</code> and <code>id</code>). The Menu list is a <code>listbox</code> with <code>option</code> rows, named by the label. An invalid field gets <code>aria-invalid="true"</code> and <code>aria-describedby</code> that points at the message.')

related = '<h2 class="ds-h2">Related</h2><ul class="ds-bullets"><li><strong>' + link_large('menu.html', 'Menu') + '</strong>. The list the select opens.</li><li><strong>' + link_large('input.html', 'Input') + '</strong>. Free text. Same sizes and states.</li><li><strong>' + link_large('radio.html', 'Radio button') + '</strong>. Two to five options, all visible.</li><li><strong>' + link_large('checkbox.html', 'Checkbox') + '</strong>. Any number of options.</li></ul>'

references = '<h2 class="ds-h2">References</h2>' + refs([
    ('https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html', 'WCAG 2.2: Labels or Instructions', 'Success criterion 3.3.2.'),
    ('https://www.w3.org/WAI/ARIA/apg/patterns/listbox/', 'WAI-ARIA Authoring Practices: Listbox', 'Keyboard and role requirements for the list.'),
    ('https://www.nngroup.com/articles/drop-down-menus/', 'Nielsen Norman Group: Drop-Down Menus', 'Use and misuse.'),
    ('https://fluent2.microsoft.design/components/web/react/core/select/usage', 'Fluent 2: Select', 'Microsoft.'),
    ('https://m3.material.io/components/menus/overview', 'Material Design 3: Menus', 'Google.'),
    ('https://carbondesignsystem.com/components/dropdown/usage/', 'Carbon Design System: Dropdown', 'IBM.')])

ex = [('playground', playground), ('overview', overview), ('usage', usage), ('anatomy', anatomy), ('variants', variants), ('sizes', sizes), ('layout', layout), ('behavior', behavior), ('accessibility', access), ('related', related), ('references', references)]

# ---------------------------------------------------------------- Specifications
st_tok = '<h2 class="ds-h2">Design Tokens</h2>' + desc('Resolved from the live token package.') + \
    '<div class="ds-table-wrap"><table class="ds-table" id="tok-table"><thead><tr><th scope="col">State</th><th scope="col">Part</th><th scope="col">Token</th><th scope="col">Value</th></tr></thead><tbody></tbody></table></div>' + \
    note('Hover is <code>border-hover</code> (<code>#333333</code>, the same value as <code>border-dark</code>). Active is read from the chosen option with <code>:has()</code>, so no script is needed.')

st_sizes = '<h2 class="ds-h2">Sizes</h2>' + table(['Breakpoint · size', 'Height', 'Padding (left, right)', 'Arrow', 'Label', 'Select text'], [
    ['Desktop · Large', '48px', '12px, 40px', '24px', '<code>label-md</code> 16/16, 0.48px', '<code>body-md</code> 17/24, 0.32px'], ['Desktop · Small', '40px', '8px, 40px', '24px', '<code>label-sm</code> 14/14, 0.56px', '<code>body-sm</code> 14/20, 0.36px'],
    ['Desktop · XSmall', '32px', '8px, 40px', '24px', '<code>label-sm</code> 14/14, 0.56px', '<code>body-sm</code> 14/20, 0.36px'], ['Mobile · Large', '40px', '8px, 40px', '24px', '<code>label-sm</code> 12/12, 0.48px', '<code>body-md</code> 16/22, 0.32px'],
    ['Mobile · Small', '32px', '8px, 40px', '24px', '<code>label-sm</code> 12/12, 0.48px', '<code>body-sm</code> 14/20, 0.36px']])


def mfig(n, name, cls):
    return ('<div class="measure__item"><span class="measure__name">%d · %s</span><div class="measure__obj"><span class="sl-measure"><div class="input-wrap"><select class="form-select%s measure__subject" tabindex="-1" aria-label="%s"><option>Choose an option</option></select><span class="form-select-arrow" aria-hidden="true">arrow_drop_down</span></div></span>'
            '<i class="measure__pad measure__pad--t"></i><i class="measure__pad measure__pad--b"></i><i class="measure__pad measure__pad--l"></i><i class="measure__pad measure__pad--r"></i>'
            '<b class="measure__dim measure__dim--v measure__dim--t"><span></span></b><b class="measure__dim measure__dim--v measure__dim--b"><span></span></b><b class="measure__dim measure__dim--h measure__dim--l"><span></span></b><b class="measure__dim measure__dim--h measure__dim--r"><span></span></b></div></div>') % (n, name, cls, name)


st_meas = '<h2 class="ds-h2">Measurements</h2><h3 class="ds-h3 ds-group">Dimensions</h3>' + desc('Padding of the select at each size. The shaded areas are the padding to the left and right (40px on the right leaves room for the arrow); the box is fixed in height. The numbers are read from the component.') + \
    toolbar([('mb-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force')]) + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-fig__stage--flush" style="padding:0;min-height:0"><div class="measure" role="img" aria-label="Padding of the select: left and right, per size">' + mfig(1, 'Large', '') + mfig(2, 'Small', ' form-select--sm') + mfig(3, 'XSmall', ' form-select--xs') + '</div></div><figcaption class="ds-fig__cap">The select at true size (1:1). Change the Breakpoint to see the mobile values.</figcaption></figure></div>' + \
    table(['Attribute', 'Large', 'Small', 'XSmall'], [['Height, Desktop', '48px', '40px', '32px'], ['Height, Mobile', '40px', '32px', 'Not available (use Small)'], ['Padding left, Desktop', '12px', '8px', '8px'], ['Padding left, Mobile', '8px', '8px', 'Not available'], ['Padding right', '<td colspan="3">40px: room for the arrow</td>'],
                                                 ['Arrow', '<td colspan="3">24px icon, 12px from the right edge, centered vertically</td>'], ['Border', '<td colspan="3">1px</td>'], ['Corners', '<td colspan="3">Square</td>']]) + \
    '<h3 class="ds-h3 ds-group">Spacing</h3>' + desc('The same padding and distances as spacing tokens.') + table(['Part', 'Value'], [['Label to box', '<code>space-4</code>'], ['Box to message', '<code>space-4</code>'], ['Padding left, Desktop Large', '<code>space-12</code>'], ['Padding left, otherwise', '<code>space-8</code>'], ['Padding right', '40px: literal, no token'], ['Arrow from the right edge', '<code>space-12</code>'], ['Menu below the field', '<code>space-4</code>'], ['Focus ring', '2px line, 3px outside the box']])

st_states = '<h2 class="ds-h2">States</h2>' + desc('All seven states from Figma. Hover and focus are forced on this page; in your code they come from <code>:hover</code> and keyboard focus.') + \
    toolbar([('sb-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force'), ('ss-l', 'Size', 'data-mx="size" data-size-toggle', [('lg', 'Large', True), ('sm', 'Small', False), ('xs', 'XSmall', False)])]) + \
    '<div class="ds-table-wrap"><table class="ds-table pg-matrix" id="matrix"><thead><tr><th scope="col">State</th><th scope="col">No value</th><th scope="col">Value chosen</th></tr></thead><tbody></tbody></table></div>' + \
    note('Active means an option is chosen. Click a field to open its Menu. Active without a value is not defined: it shows a dash.')

st_typo = '<h2 class="ds-h2">Typography</h2>' + table(['Part', 'Type', 'Size / line height', 'Letter spacing', 'Weight'], [
    ['Label, Desktop Large', '<code>label-md</code>', '16/16', '0.48px', 'Bold, uppercase'], ['Label, Desktop Small, XSmall', '<code>label-sm</code>', '14/14', '0.56px', 'Bold, uppercase'], ['Label, Mobile', '<code>label-sm</code>', '12/12', '0.48px', 'Bold, uppercase'],
    ['Select text, Large', '<code>body-md</code>', '16/22 mobile, 17/24 from 769px', '0.32px', 'Regular'], ['Select text, Small, XSmall', '<code>body-sm</code>', '14/20', '0.36px', 'Regular'], ['Message', '<code>body-sm</code>', '14/20', '0.36px', 'Regular']]) + note('Breuer Condensed with <code>ss02</code> and <code>ss03</code> (the select text and the message also <code>ss06</code>).')

st_struct = '<h2 class="ds-h2">Structure</h2><h3 class="ds-h3 ds-group">Elements</h3>' + table(['Element', 'Class', 'Notes'], [
    ['Field', '<code>form-field</code>', 'Label, wrapper and message in a column, 4px apart.'], ['Label', '<code>form-label</code>, <code>form-label--sm</code>', 'Uppercase. <code>--sm</code> for Small and XSmall.'], ['Wrapper', '<code>input-wrap</code>', 'Carries the focus ring, the arrow and the open menu.'],
    ['Select', '<code>form-select</code>, <code>--sm</code>, <code>--xs</code>, <code>--error</code>, <code>--success</code>', 'The native <code>select</code>, <code>appearance: none</code>.'], ['Arrow', '<code>form-select-arrow</code>', 'Material Symbols <code>arrow_drop_down</code>, 24px.'],
    ['Message', '<code>form-helper</code>, <code>--error</code>, <code>--success</code>, <code>--disabled</code>', 'Optional icon (<code>form-helper-icon</code>).'], ['Menu', '<code>menu</code>, <code>menu--sm</code>', 'Added under the wrapper by <code>select-menu.js</code> while open.']]) + \
    '<h3 class="ds-h3 ds-group">Types</h3>' + desc('There is one type. The Menu size follows the field: Large opens a Large menu, Small and XSmall open a Small menu.') + '<h3 class="ds-h3 ds-group">Width</h3>' + desc('The field fills its container. The menu is as wide as the field.')

st_motion = '<h2 class="ds-h2">Motion</h2>' + table(['Property', 'Duration', 'Easing'], [['<code>border-color</code> of the select', '<code>duration-fast-3</code>', '<code>ease-standard</code>'], ['<code>opacity</code> of the focus ring', '<code>duration-fast-3</code>', '<code>ease-standard</code>']])

st_behavior = '<h2 class="ds-h2">Behavior</h2>' + table(['Input', 'Result'], [
    ['Click', 'Opens the Menu under the field (no ring on mouse). Click a row to choose; click outside to close.'], ['Tab', 'The blue ring shows on keyboard focus only (<code>body.keyboard-nav</code>).'],
    ['Enter, Space, Arrow keys', 'Open the Menu on the chosen row. Up and Down, Home and End move; Enter or Space choose; Escape closes and returns focus to the field; Tab closes.'], ['Placeholder', 'A first option with <code>value=""</code> (disabled, hidden) shows the placeholder in <code>text-tertiary</code>.'],
    ['Menu position', 'Under the field. It flips upwards when it does not fit below and there is more room above; otherwise its height is capped and it scrolls.'], ['Disabled', 'Not focusable. Grey fill, light border, <code>text-disabled</code> text and arrow.']])

st_access = '<h2 class="ds-h2">Accessibility Requirements</h2>' + table(['Topic', 'Requirement'], [
    ['Label', 'Always a <code>label</code> with <code>for</code> and <code>id</code>. A placeholder is never the label.'], ['Error', 'Set <code>aria-invalid="true"</code> and point <code>aria-describedby</code> at the message.'], ['List', 'The Menu is a <code>listbox</code> of <code>option</code> rows, with <code>aria-selected</code>, named by the label. The select gets <code>aria-expanded</code> while it is open.'],
    ['Focus', 'A 2px ring on keyboard focus (<code>border-focus</code>), not on mouse click (WCAG 2.4.7, 1.4.11). Escape returns focus to the field.'], ['Color', 'Error and success are not shown by color alone: the message says it, and the error message has an icon.'], ['Disabled', 'Not focusable. Disabled tokens are exempt from contrast requirements.']])

spec = [('design-tokens', st_tok), ('sizes', st_sizes), ('measurements', st_meas), ('states', st_states), ('typography', st_typo), ('structure', st_struct), ('motion', st_motion), ('behavior', st_behavior), ('accessibility-requirements', st_access)]

# ---------------------------------------------------------------- Code
c_basic = '<h2 class="ds-h2">Basic Usage</h2>' + desc('Link the shared files once per page. Never copy the rules into a page.') + table(['Step', 'What to do'], [
    ['1. Link', '<code>select.css</code> and <code>menu.css</code> in <code>/components/css/</code>, and <code>/components/js/select-menu.js</code>. Both templates already have them.'], ['2. Markup', 'A <code>form-field</code> with a <code>label</code>, an <code>input-wrap</code> around a native <code>select.form-select</code> and the <code>form-select-arrow</code> span, and an optional <code>form-helper</code> message.'],
    ['3. Placeholder', 'Start the options with <code>&lt;option value="" disabled selected hidden&gt;</code>.'], ['4. Size', 'Large is the default. Add <code>form-select--sm</code> and <code>form-label--sm</code> for Small, <code>form-select--xs</code> for XSmall (desktop only).'], ['5. Keyboard focus', 'Add the keyboard script under CSS / Tailwind once per page.']])
c_sl = '<h2 class="ds-h2">Select</h2>' + desc('Copy the markup you need. Hover and focus come from <code>:hover</code> and keyboard focus; the <code>[data-state]</code> selectors in the CSS exist only so the documentation can force a state.') + '<div id="recipes"></div>'
c_api = '<h2 class="ds-h2">API</h2><h3 class="ds-h3 ds-group">Classes</h3>' + table(['Class', 'Use'], [
    ['<code>form-field</code>, <code>form-label</code>, <code>form-label--sm</code>', 'The column and the label.'], ['<code>input-wrap</code>', 'The wrapper: focus ring, arrow and open menu.'], ['<code>form-select</code>, <code>--sm</code>, <code>--xs</code>', 'The select. Large, Small, XSmall.'], ['<code>form-select--error</code>, <code>--success</code>', 'Red or green border.'],
    ['<code>form-select-arrow</code>', 'The arrow icon, after the select inside the wrapper.'], ['<code>form-helper</code>, <code>--error</code>, <code>--success</code>, <code>--disabled</code>, <code>form-helper-icon</code>', 'The message.']]) + \
    '<h3 class="ds-h3 ds-group">Things to know</h3>' + bullets(['<code>select-menu.js</code> opens the ECO Menu instead of the browser list. The <code>select</code> stays the form control: its value, label and <code>disabled</code> state do not change.', 'The Active border is read from the chosen option with <code>:has()</code>, so no script is needed.', 'Without <code>select-menu.js</code> the select works with the browser’s own list.', 'The <code>[data-state]</code> selectors do nothing outside the documentation pages.'])
c_css = '<h2 class="ds-h2">CSS / Tailwind</h2>' + desc('The component is two CSS files and one script, shared by every page. Link them, never copy them. The code below is read from the files the page links, so it is always what you see.') + \
    code_box('css-code', 'CSS (components/css/select.css)') + '<div style="margin-top:16px">' + code_box('menu-css-code', 'CSS for the menu (from eco-menu, plus the opening position)') + '</div><div style="margin-top:16px">' + code_box('menu-js-code', 'JavaScript (components/js/select-menu.js: opens the menu from the select)') + '</div><div style="margin-top:16px">' + code_box('js-code', 'JavaScript (focus ring on keyboard only)') + '</div>'
code = [('basic-usage', c_basic), ('select', c_sl), ('api', c_api), ('css-tailwind', c_css, False)]

# ---------------------------------------------------------------- scripts
SEL_JS = "  var uid = 0, OPTS = ['Sweden', 'Norway', 'Denmark', 'Finland'];\n" + old_js('select', "  function icon(name, cls)", "  var pg = { size")

SYNC = r'''
  var bpNow = 'auto';
  function syncSizes() {   /* XSmall does not exist on mobile */
    $$('[data-size-toggle]').forEach(function (g) {
      var x = $('[data-v="xs"]', g); x.disabled = bpNow === 'mobile';
      if (bpNow === 'mobile' && x.getAttribute('aria-pressed') === 'true') { var s = $('[data-v="sm"]', g); s.click(); }
    });
  }
  DK.bp(function (v) { bpNow = v; syncSizes(); if (window.ECO_MEASURE) ECO_MEASURE.init(); });
'''

JS_EX = SEL_JS + SYNC + r'''
  var pg = { size: 'lg', state: 'enabled' };
''' + old_js('select', "  function renderPg() {", "  $$('[data-pg]').forEach") + r'''
  DK.wire(pg, renderPg);
  $('#pg-label').addEventListener('input', renderPg); $('#pg-hint').addEventListener('input', renderPg);

  /* Usage figures */
  var longList = clear($('#fig-do')); longList.appendChild(field({ size: 'lg', label: 'Country', hint: '' }));
  $('select', longList).innerHTML = '<option value="" disabled selected hidden>Choose an option</option>' + ['Sweden', 'Norway', 'Denmark', 'Finland', 'Iceland', 'Estonia', 'Latvia', 'Lithuania'].map(function (t) { return '<option value="' + t.toLowerCase() + '">' + t + '</option>'; }).join('');
  var dont = clear($('#fig-dont')), rg = document.createElement('fieldset'); rg.className = 'form-radio-group'; rg.innerHTML = '<legend>Country</legend>';
  ['Sweden', 'Norway', 'Denmark', 'Finland', 'Iceland', 'Estonia', 'Latvia', 'Lithuania'].forEach(function (t, n) { var l = document.createElement('label'); l.className = 'form-radio-item'; l.innerHTML = '<input type="radio" name="fig-long"' + (n === 0 ? ' checked' : '') + ' /><span></span>'; l.querySelector('span').textContent = t; rg.appendChild(l); });
  dont.appendChild(rg);

  clear($('#fig-lab-do')).appendChild(field({ size: 'lg', label: 'Country', hint: '' }));
  var labDont = clear($('#fig-lab-dont')); labDont.appendChild(field({ size: 'lg', hint: '', aria: 'Country' }));
  $('option', labDont).textContent = 'Country';
  var ms = clear($('#v-messages'));
  [['enabled', 'Hint'], ['error', 'Error'], ['success', 'Success'], ['disabled', 'Disabled']].forEach(function (m) { ms.appendChild(field({ label: m[1], state: m[0], hint: HINT[m[0]], value: m[0] === 'success' })); });
  var sz = clear($('#v-sizes'));
  [['lg', 'Large'], ['sm', 'Small'], ['xs', 'XSmall']].forEach(function (s) { sz.appendChild(field({ size: s[0], label: s[1], hint: 'Helper text' })); });
  clear($('#v-live')).appendChild(field({ size: 'lg', label: 'Country', hint: 'Click the field to open the Menu.' }));

  var ah = clear($('#a-host'));
  ah.appendChild(field({ size: 'lg', label: 'Label', state: 'active', hint: 'Message' }));
  function txt(el) { return function () { var r = document.createRange(); r.selectNodeContents(el); return r.getBoundingClientRect(); }; }
  DK.callouts($('#sl-anat'), [
    { n: 1, box: txt($('.form-label', ah)), side: 'top', len: 40 },
    { n: 2, box: function () { var r = $('.form-select', ah).getBoundingClientRect(); return { left: r.left + 12, top: r.top, width: 40, height: r.height }; }, side: 'bottom', len: 72 },
    { n: 3, el: $('.form-select-arrow', ah), side: 'top', len: 40 },
    { n: 4, box: txt($('.form-helper', ah)), side: 'bottom', len: 40 }
  ]);
  renderPg(); syncSizes();
'''

JS_SPEC = SEL_JS + SYNC + r'''
  var mx = { size: 'lg' };
  var ROWS = [['Enabled', 'enabled'], ['Hover', 'hover'], ['Active', 'active'], ['Focus', 'focus'], ['Error', 'error'], ['Success', 'success'], ['Disabled', 'disabled']];
  function buildMatrix() {
    var tb = clear($('#matrix tbody'));
    ROWS.forEach(function (r) {
      var tr = document.createElement('tr'), th = document.createElement('th'); th.scope = 'row'; th.textContent = r[0]; tr.appendChild(th);
      [false, true].forEach(function (v) {
        var td = document.createElement('td');
        if (r[1] === 'active' && !v) { td.textContent = '—'; td.className = 'ds-na'; }
        else td.appendChild(field({ size: mx.size, state: r[1], label: 'Label', hint: HINT[r[1]], value: v })); tr.appendChild(td);
      });
      tb.appendChild(tr);
    });
  }
  DK.seg($('[data-mx="size"]'), function (v) { mx.size = v; buildMatrix(); });
  buildMatrix();
  DK.tokenTable($('#tok-table tbody'), [
    ['Enabled', 'Border', 'border-input-default'], ['Enabled', 'Fill', 'surface-raised-primary'], ['Enabled', 'Placeholder, message', 'text-tertiary'],
    ['Hover', 'Border', 'border-hover'], ['Active', 'Border', 'border-selected'], ['Active', 'Select text', 'text-primary'],
    ['Focus', 'Ring (2px, 3px outside)', 'border-focus'], ['Error', 'Border', 'border-danger-default'], ['Error', 'Message', 'text-danger-default'],
    ['Success', 'Border', 'border-success-default'], ['Success', 'Message', 'text-success-default'],
    ['Disabled', 'Border', 'border-disabled'], ['Disabled', 'Fill', 'surface-raised-secondary'], ['Disabled', 'Text, arrow, message', 'text-disabled'],
    ['All', 'Arrow', 'icon-primary'], ['All', 'Label', 'text-primary']]);
'''

JS_CODE = r'''
  DK.recipes($('#recipes'), [
    ['Standard', '<div class="form-field">\n  <label class="form-label form-label--sm" for="country">Country</label>\n  <div class="input-wrap">\n    <select class="form-select form-select--sm" id="country">\n      <option value="" disabled selected hidden>Choose an option</option>\n      <option value="sweden">Sweden</option>\n      <option value="norway">Norway</option>\n    </select>\n    <span class="form-select-arrow" aria-hidden="true">arrow_drop_down</span>\n  </div>\n  <div class="form-helper">Helper text</div>\n</div>'],
    ['Error', '<select class="form-select form-select--error" id="country" aria-invalid="true" aria-describedby="country-msg">…</select>\n<div class="form-helper form-helper--error" id="country-msg"><span class="form-helper-icon" aria-hidden="true">error</span>Choose a country.</div>'],
    ['Small and XSmall', '<select class="form-select form-select--sm">…</select>   <!-- Small; label: form-label--sm -->\n<select class="form-select form-select--xs">…</select>   <!-- XSmall, desktop only -->'],
    ['Disabled', '<select class="form-select form-select--sm" disabled>…</select>\n<div class="form-helper form-helper--disabled">This field cannot be edited.</div>']
  ]);
  var strip = function (t) { return t.replace(/:is\(:hover, \[data-state="hover"\]\)/g, ':hover').replace(/:is\(:focus-visible, \[data-state="focus"\]\)/g, ':focus-visible').replace(/, \[data-state="active"\]\)/g, ')').replace(/,\n    \.input-wrap\[data-state="focus"\]::after/g, '').replace(/^\n+/, '').replace(/^ {4}/gm, ''); };
  var get = function (n) { return fetch('../../components/css/' + n + '.css', { cache: 'no-cache' }).then(function (r) { return r.text(); }); };
  get('select').then(function (t) { $('#css-code').textContent = strip(t); });
  Promise.all([get('menu'), get('select')]).then(function (a) { $('#menu-css-code').textContent = strip(a[0].replace(/\s+$/, '') + '\n\n' + a[1].slice(a[1].indexOf('    /* Exposed dropdown'))); });
  fetch('../../components/js/select-menu.js', { cache: 'no-cache' }).then(function (r) { return r.text(); }).then(function (t) { $('#menu-js-code').textContent = t.replace(/^\n+/, '').replace(/\n+$/, ''); });
  $('#js-code').textContent = "document.addEventListener('keydown', function (e) { if (e.key === 'Tab') document.body.classList.add('keyboard-nav'); });\ndocument.addEventListener('mousedown', function () { document.body.classList.remove('keyboard-nav'); });";
'''

C = dict(
    slug=SLUG, title='Select', eyebrow='Components · Form',
    lead='A select lets the user choose <strong>one option from a list</strong>. It looks and behaves like an input field, with a dropdown arrow. It opens the ECO <strong>Menu</strong> as its list.',
    lead_ex='Every example on this page is the real component, not a picture. Click, tab and choose an option to try it. Figma: ' + fig_link(FIGMA, 'Base Input') + ' (shared with Input).',
    lead_spec='Tokens, sizes, measurements, states and requirements. Values come from the live token package and from Figma: ' + fig_link(FIGMA, 'Base Input') + '.',
    lead_code='How to add a select to a page. The files are <code>components/css/select.css</code>, <code>components/css/menu.css</code> and <code>components/js/select-menu.js</code>.',
    css=['select', 'menu', 'radio'], style=STYLE, ex=ex, spec=spec, code=code, js_ex=JS_EX, js_spec=JS_SPEC, js_code=JS_CODE)

if __name__ == '__main__':
    emit(C)
