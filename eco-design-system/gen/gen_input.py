from build import *

FIGMA = 'https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=1475-44234'
SLUG = 'input'

STYLE = r'''    .pg-note { font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-tertiary); }
    .in-col { display: flex; flex-direction: column; gap: 24px; width: 100%; max-width: 360px; }
    .in-grid { display: grid; gap: 32px 24px; grid-template-columns: minmax(0, 1fr); width: 100%; }
    @media (min-width: 769px) { .in-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
    .in-matrix td { min-width: 280px; vertical-align: top; padding-top: 16px; padding-bottom: 16px; }
    .in-matrix .form-field { min-width: 240px; }
    .in-fig { width: 100%; max-width: 320px; }
    .in-measure { display: block; width: 280px; }   /* demo: a fixed width, so the padding strips have an input box to sit on */
    .ds-callout__art { padding-right: 24px; width: 100%; max-width: 360px; }'''

playground = '<h2 class="ds-h2">Playground</h2>' + desc('Choose a breakpoint, size and state and the field and its code update. Hover and focus are forced here so they can be seen; type in the field to get the Active state, and use the clear button to empty it.') + \
    '<div class="ds-playground"><div class="ds-stage ds-stage--center" id="pg-stage"><div class="in-col" id="pg-host"></div></div><div class="ds-controls">' + \
    bp_field('pg-l-bp') + \
    btn_group('pg-l-size', 'Size', 'data-pg="size" data-size-toggle', [('lg', 'Large', True), ('sm', 'Small', False), ('xs', 'XSmall', False)]) + \
    '<div class="ds-field form-field"><label class="form-label form-label--sm" for="sel-pg-l-st" id="pg-l-st">State</label><div class="input-wrap"><select class="form-select form-select--sm" data-pg="state" id="sel-pg-l-st"><option value="enabled">Enabled</option><option value="hover">Hover</option><option value="active">Active</option><option value="focus">Focus</option><option value="error">Error</option><option value="success">Success</option><option value="disabled">Disabled</option></select><span class="form-select-arrow" aria-hidden="true">arrow_drop_down</span></div></div>' + \
    btn_group('pg-l-left', 'Left icon', 'data-pg="left"', [('off', 'None', True), ('on', 'Search', False)]) + \
    btn_group('pg-l-right', 'Right icons', 'data-pg="right"', [('none', 'None', True), ('clear', 'Clear', False), ('both', 'Clear + actions', False)]) + \
    btn_group('pg-l-msg', 'Message icon', 'data-pg="msgIcon"', [('off', 'None', True), ('on', 'Icon', False)]) + \
    '<div class="ds-field form-field"><label class="form-label form-label--sm" for="pg-label">Label</label><div class="input-wrap"><div class="input-box input-box--sm"><input class="form-input" type="text" id="pg-label" value="Order number" placeholder="Label" /></div></div></div>' + \
    '<div class="ds-field form-field"><label class="form-label form-label--sm" for="pg-hint">Message</label><div class="input-wrap"><div class="input-box input-box--sm"><input class="form-input" type="text" id="pg-hint" value="Found on your order confirmation." placeholder="Message" /></div></div></div>' + \
    '</div></div><h3 class="ds-h3">Markup for this selection</h3>' + code_box('pg-code', 'HTML')

overview = '<h2 class="ds-h2">Overview</h2>' + desc('An input field lets the user enter free text, numbers or search terms. It can have a label, a left icon, right-hand action icons and a message that explains or validates the value.') + \
    desc('Input has three sizes on desktop (Large, Small, XSmall) and two on mobile (Large, Small), seven states, and optional clear and action icons.') + \
    three_pages(SLUG, 'an input field', 'the values: tokens, sizes, measurements, states and requirements', 'how to add one to a page')

usage = '<h2 class="ds-h2">Usage</h2><h3 class="ds-h3 ds-group">When to use</h3>' + desc('Use an input when the user types a value that is not picked from a list. Use it to:') + \
    bullets(['Enter free text, such as a name or an order number', 'Enter a number or a code', 'Search, with a left search icon and the clear button', 'Enter a value that can also be filled by an action, such as “Use my location” or “Scan a code” (action icons)']) + \
    '<h3 class="ds-h3 ds-group">When not to use</h3><h3 class="ds-h3">For a value picked from a list</h3>' + desc('When the user picks one value from a fixed list, use <code>eco-select</code>. For one of two or three options use <code>eco-radio</code>, and for any number of options <code>eco-checkbox</code>. For several lines of text use <code>eco-textarea</code>.') + \
    '<h3 class="ds-h3">For a label</h3>' + desc('A placeholder is not a label: it disappears when the user types, and it is easy to miss. Every field has a visible label.') + \
    fig_pair('<div class="in-fig" id="fig-do"></div>', 'Do give every field a visible label.', '<div class="in-fig" id="fig-dont"></div>', 'Do not use the placeholder as the label.') + \
    '<h3 class="ds-h3">Say what is wrong</h3>' + desc('An invalid field says what is wrong in the message, with the error icon. A red border alone is easy to miss and is not enough for everyone.') + \
    fig_pair('<div class="in-fig" id="fig-err-do"></div>', 'Do explain what is wrong in the message, with the error icon.', '<div class="in-fig" id="fig-err-dont"></div>', 'Do not rely on a red border alone.') + \
    '<h3 class="ds-h3 ds-group">Quick reference</h3>' + \
    table(['The user…', 'Use'], [['types free text, a number or a search term', 'Input'], ['types several lines of text', '<code>eco-textarea</code>'], ['picks one value from a fixed list', '<code>eco-select</code>'], ['picks one of two or three options', '<code>eco-radio</code>'], ['picks any number of options', '<code>eco-checkbox</code>']]) + \
    rules(['Give every field a visible label, in sentence case for values and uppercase for the label itself.', 'Pick the size by breakpoint: Large for standard forms, Small for compact surfaces, XSmall for dense tables.', 'Explain what is wrong in the message, with the error icon.', 'Use pre-filled or detected values where you can, in sentence case.'],
          ['Use a placeholder as the label.', 'Show the focus ring on mouse click, or remove it on keyboard focus.', 'Use color alone for error or success.', 'Hardcode the colors or the heights: use the tokens and the size classes.'])

anatomy = '<h2 class="ds-h2">Anatomy</h2><h3 class="ds-h3 ds-group">Input</h3>' + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout" id="in-anat" role="img" aria-label="Anatomy of an input field: 1 label, 2 left icon, 3 input text, 4 clear, 5 divider, 6 action icons, 7 message"><div class="ds-callout__art"><div class="in-col" id="a-host"></div></div></div></figure></div>' + \
    ol_parts([('Label', '<code>label-md</code> or <code>label-sm</code>, uppercase, 4px above the box.'), ('Left icon', '24px (Large) or 20px (Small, XSmall), 8px from the text. It shows the type of input; the default is search.'), ('Input text', '<code>body-md</code> (Large) or <code>body-sm</code>. The placeholder is <code>text-tertiary</code>.'),
              ('Clear', 'Only with a value. A real button with an <code>aria-label</code>.'), ('Divider', '1px × 16px, between clear and the action icons.'), ('Action icons', 'Optional buttons for actions such as “Scan a code”.'), ('Message', '<code>body-sm</code>, 4px below the box. Hint, error or success.')]) + \
    desc('The focus ring is a separate element around the box, 2px and 3px outside it, so focusing never changes the layout or the box size.')

variants = '<h2 class="ds-h2">Variants</h2>' + desc('An input can have a left icon, right-hand icons and a message. Enable only the ones the field needs. Sizes are under Sizes below.') + \
    '<h3 class="ds-h3 ds-group">Icons</h3>' + desc('A left icon shows the type of input (the default is search). Right-hand icons are optional: <strong>clear</strong> appears only when the field has a value, a <strong>divider</strong> separates clear from the <strong>action icons</strong>. Enable only the ones the field needs.') + \
    fig_one('<div class="in-grid" id="v-icons"></div>') + \
    '<h3 class="ds-h3 ds-group">Messages</h3>' + desc('The message sits below the field, in <code>body-sm</code>. Hint text is neutral, error and success change the color of the border and the message. The message icon is optional and up to you; an icon next to an error message helps so color is not the only signal.') + \
    fig_one('<div class="in-grid" id="v-messages"></div>')

sizes = '<h2 class="ds-h2">Sizes</h2>' + desc('Three sizes on desktop (Large 48px, Small 40px, XSmall 32px) and two on mobile (Large 40px, Small 32px). Figma has a Breakpoint property: Desktop is 769px and up, Mobile is below 769px. The component switches by itself; the Breakpoint toggle forces one for preview.') + \
    toolbar([('vb-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force')]) + \
    desc('<strong>Large</strong> is for standard forms, <strong>Small</strong> for compact surfaces, <strong>XSmall</strong> for dense tables and filters (desktop only: on mobile it is not available, use Small). Measurements are under ' + 'Sizes in ' + link_large('input-specifications.html#sizes', 'Specifications') + '.') + \
    fig_one('<div class="in-grid" id="v-sizes"></div>')

layout = '<h2 class="ds-h2">Layout &amp; Appearance</h2><h3 class="ds-h3 ds-group">Width</h3>' + desc('The field is as wide as its container: set the width on the container, not on the field. In the examples on this page the container is 360px or narrower.') + \
    '<h3 class="ds-h3 ds-group">Appearance</h3>' + desc('The box has a 1px border and a white fill. The border turns black when the field has a value, and the message and the border turn red or green for error and success. The focus ring is a 2px blue frame around the box. Token names and values are under ' + sec_link(SLUG, 'design-tokens', 'Design Tokens') + ' in Specifications.')

behavior = '<h2 class="ds-h2">Behavior</h2><h3 class="ds-h3 ds-group">Typing</h3>' + desc('When the user types a value the field becomes Active: the border turns black and the clear button appears.') + \
    '<h3 class="ds-h3 ds-group">Clear</h3>' + desc('The clear button empties the field and returns focus to it. It is a real <code>button</code> with an <code>aria-label</code>.') + \
    '<h3 class="ds-h3 ds-group">Hover and focus</h3>' + desc('Hover changes the border. Hover on a right icon gives a grey fill (Button) or turns the icon grey (Icon Button). The blue ring shows on keyboard focus only (<code>body.keyboard-nav</code>, set by a small script). All states are listed under ' + sec_link(SLUG, 'states', 'States') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Error and success</h3>' + desc('Set <code>aria-invalid="true"</code> on an invalid field and point <code>aria-describedby</code> at the message. The message says what is wrong.') + \
    '<h3 class="ds-h3 ds-group">Disabled</h3>' + desc('A disabled field is not focusable. It has a grey fill, a light border, and <code>text-disabled</code> for the text, the icons and the message.')

access = '<h2 class="ds-h2">Accessibility</h2>' + desc('All requirements are listed under ' + sec_link(SLUG, 'accessibility-requirements', 'Accessibility Requirements') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Keyboard support</h3>' + desc('Tab moves into and out of the field and to the icon buttons. The focus ring shows on keyboard focus only. Add the keyboard script once per page (see Code).') + \
    '<h3 class="ds-h3 ds-group">Screen reader support</h3>' + desc('Every field has a <code>label</code> with <code>for</code> and <code>id</code>. A search field without a visible label needs an <code>aria-label</code>. An invalid field gets <code>aria-invalid="true"</code> and <code>aria-describedby</code> that points at the message.')

related = '<h2 class="ds-h2">Related</h2><ul class="ds-bullets"><li><strong>' + link_large('textarea.html', 'Text area') + '</strong>. Several lines of text.</li><li><strong>' + link_large('select.html', 'Select') + '</strong>. One value from a list.</li><li><strong>' + link_large('radio.html', 'Radio button') + '</strong>. One of two or three options.</li><li><strong>' + link_large('checkbox.html', 'Checkbox') + '</strong>. Any number of options.</li><li><strong>' + link_large('button.html', 'Button') + '</strong>. The right-hand icons are Blank icon buttons.</li></ul>'

references = '<h2 class="ds-h2">References</h2>' + refs([
    ('https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html', 'WCAG 2.2: Labels or Instructions', 'Success criterion 3.3.2.'),
    ('https://www.w3.org/WAI/WCAG22/Understanding/error-identification.html', 'WCAG 2.2: Error Identification', 'Success criterion 3.3.1.'),
    ('https://www.nngroup.com/articles/form-design-placeholders/', 'Nielsen Norman Group: Placeholders in Form Fields Are Harmful', 'Why a placeholder is not a label.'),
    ('https://fluent2.microsoft.design/components/web/react/core/input/usage', 'Fluent 2: Input', 'Microsoft.'),
    ('https://m3.material.io/components/text-fields/overview', 'Material Design 3: Text fields', 'Google.'),
    ('https://carbondesignsystem.com/components/text-input/usage/', 'Carbon Design System: Text input', 'IBM.')])

ex = [('playground', playground), ('overview', overview), ('usage', usage), ('anatomy', anatomy), ('variants', variants), ('sizes', sizes), ('layout', layout), ('behavior', behavior), ('accessibility', access), ('related', related), ('references', references)]

# ---------------------------------------------------------------- Specifications
st_tok = '<h2 class="ds-h2">Design Tokens</h2>' + desc('Resolved from the live token package.') + \
    '<div class="ds-table-wrap"><table class="ds-table" id="tok-table"><thead><tr><th scope="col">State</th><th scope="col">Part</th><th scope="col">Token</th><th scope="col">Value</th></tr></thead><tbody></tbody></table></div>' + \
    note('Figma binds <code>icon/disabled</code>, which is not in <code>tokens.json</code>, so the disabled icon uses <code>text-disabled</code> (same value).')

st_sizes = '<h2 class="ds-h2">Sizes</h2>' + table(['Breakpoint · size', 'Height', 'Padding (left, right)', 'Left icon', 'Right icons', 'Label', 'Input text'], [
    ['Desktop · Large', '48px', '12px, 8px', '24px', 'Button (32px)', '<code>label-md</code> 16/16, 0.48px', '<code>body-md</code> 17/24, 0.32px'],
    ['Desktop · Small', '40px', '8px, 4px', '20px', 'Button (32px)', '<code>label-sm</code> 14/14, 0.56px', '<code>body-sm</code> 14/20, 0.36px'],
    ['Desktop · XSmall', '32px', '8px, 6px', '20px', 'Icon Button (20px)', '<code>label-sm</code> 14/14, 0.56px', '<code>body-sm</code> 14/20, 0.36px'],
    ['Mobile · Large', '40px', '8px, 4px', '24px', 'Button (32px)', '<code>label-sm</code> 12/12, 0.48px', '<code>body-md</code> 16/22, 0.32px'],
    ['Mobile · Small', '32px', '8px, 6px', '20px', 'Icon Button (20px)', '<code>label-sm</code> 12/12, 0.48px', '<code>body-sm</code> 14/20, 0.36px']]) + \
    note('Right-hand icons are 20px in every size, but the component that holds them differs. A <strong>Button</strong> (<code>eco-button</code>, Blank, icon only, 6px padding = 32px, grey fill on hover) holds them on Desktop Large, Desktop Small and Mobile Large. An <strong>Icon Button</strong> (just the 20px icon, it turns grey on hover) holds them on Desktop XSmall and Mobile Small. Icon color is <code>text-action-primary</code>. Padding top and bottom comes from the fixed height. The 6px values and the 10px gap before the icons on Mobile Large are literals: there is no spacing token for them.')


def mfig(n, name, cls):
    return ('<div class="measure__item"><span class="measure__name">%d · %s</span><div class="measure__obj"><span class="in-measure"><div class="input-box%s measure__subject"><span class="input-icon%s" aria-hidden="true">search</span><input class="form-input" type="text" placeholder="Placeholder" tabindex="-1" aria-label="%s" /></div></span>'
            '<i class="measure__pad measure__pad--t"></i><i class="measure__pad measure__pad--b"></i><i class="measure__pad measure__pad--l"></i><i class="measure__pad measure__pad--r"></i>'
            '<b class="measure__dim measure__dim--v measure__dim--t"><span></span></b><b class="measure__dim measure__dim--v measure__dim--b"><span></span></b><b class="measure__dim measure__dim--h measure__dim--l"><span></span></b><b class="measure__dim measure__dim--h measure__dim--r"><span></span></b></div></div>') % (
        n, name, cls, ' input-icon--lg' if not cls else '', name)


st_meas = '<h2 class="ds-h2">Measurements</h2><h3 class="ds-h3 ds-group">Dimensions</h3>' + desc('Padding of the input box at each size. The shaded areas are the padding to the left and right; the box is fixed in height, so there is no padding above or below. The numbers are read from the component.') + \
    toolbar([('mb-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force')]) + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-fig__stage--flush" style="padding:0;min-height:0"><div class="measure" role="img" aria-label="Padding of the input box: left and right, per size">' + mfig(1, 'Large', '') + mfig(2, 'Small', ' input-box--sm') + mfig(3, 'XSmall', ' input-box--xs') + '</div></div><figcaption class="ds-fig__cap">The input box at true size (1:1). Change the Breakpoint to see the mobile values.</figcaption></figure></div>' + \
    table(['Attribute', 'Large', 'Small', 'XSmall'], [
        ['Height, Desktop', '48px', '40px', '32px'], ['Height, Mobile', '40px', '32px', 'Not available (use Small)'], ['Padding, left and right, Desktop', '12px, 8px', '8px, 4px', '8px, 6px'], ['Padding, left and right, Mobile', '8px, 4px', '8px, 6px', 'Not available'],
        ['Left icon', '24px', '20px', '20px'], ['Gap, left icon to text', '8px', '8px', '8px'], ['Border', '<td colspan="3">1px</td>'], ['Corners', '<td colspan="3">Square</td>'], ['Divider', '<td colspan="3">1px × 16px</td>']]) + \
    '<h3 class="ds-h3 ds-group">Spacing</h3>' + desc('The same padding and distances as spacing tokens.') + \
    table(['Part', 'Value'], [['Label to box', '<code>space-4</code>'], ['Box to message', '<code>space-4</code>'], ['Padding left, Desktop Large', '<code>space-12</code>'], ['Padding left, Large mobile and Small, XSmall', '<code>space-8</code>'], ['Padding right, Desktop Large', '<code>space-8</code>'],
                         ['Padding right, Small desktop and Large mobile', '<code>space-4</code>'], ['Padding right, XSmall and Small mobile', '6px: literal, no token'], ['Gap between the icon and the text', '<code>space-8</code>'], ['Gap between right icons', '<code>space-4</code>'],
                         ['Gap before the right icons', 'Large desktop and Small desktop <code>space-4</code>; Large mobile 10px (literal); XSmall, and Small mobile <code>space-16</code>'], ['Focus ring', '2px line, 3px outside the box']])

st_states = '<h2 class="ds-h2">States</h2>' + desc('All seven states from Figma, with and without icons. Hover and focus are forced on this page; in your code they come from <code>:hover</code> and keyboard focus. Active means the field has a value.') + \
    toolbar([('sb-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force'), ('ss-l', 'Size', 'data-mx="size" data-size-toggle', [('lg', 'Large', True), ('sm', 'Small', False), ('xs', 'XSmall', False)])]) + \
    '<div class="ds-table-wrap"><table class="ds-table in-matrix" id="matrix"><thead><tr><th scope="col">State</th><th scope="col">Plain</th><th scope="col">Left icon</th><th scope="col">Left + right icons</th></tr></thead><tbody></tbody></table></div>'

st_typo = '<h2 class="ds-h2">Typography</h2>' + table(['Part', 'Type', 'Size / line height', 'Letter spacing', 'Weight'], [
    ['Label, Desktop Large', '<code>label-md</code>', '16/16', '0.48px', 'Bold, uppercase'], ['Label, Desktop Small, XSmall', '<code>label-sm</code>', '14/14', '0.56px', 'Bold, uppercase'], ['Label, Mobile', '<code>label-sm</code>', '12/12', '0.48px', 'Bold, uppercase'],
    ['Input text, Large', '<code>body-md</code>', '16/22 mobile, 17/24 from 769px', '0.32px', 'Regular'], ['Input text, Small, XSmall', '<code>body-sm</code>', '14/20', '0.36px', 'Regular'], ['Message', '<code>body-sm</code>', '14/20', '0.36px', 'Regular']]) + \
    note('Breuer Condensed with <code>ss02</code> and <code>ss03</code> (the message also <code>ss06</code>). The placeholder and the message use <code>text-tertiary</code>.')

st_struct = '<h2 class="ds-h2">Structure</h2><h3 class="ds-h3 ds-group">Elements</h3>' + table(['Element', 'Class', 'Notes'], [
    ['Field', '<code>form-field</code>', 'Label, input wrapper and message in a column, 4px apart.'], ['Label', '<code>form-label</code>, <code>form-label--sm</code>', 'Uppercase. <code>--sm</code> for Small and XSmall.'], ['Input wrapper', '<code>input-wrap</code>', 'Carries the focus ring (2px, 3px outside the box).'],
    ['Input box', '<code>input-box</code>, <code>--sm</code>, <code>--xs</code>, <code>--error</code>, <code>--success</code>', 'Border, fill and height. Holds the icon, the input and the right icons.'], ['Left icon', '<code>input-icon</code>, <code>--lg</code>', 'Material Symbols. <code>--lg</code> is 24px (Large).'],
    ['Input', '<code>form-input</code>', 'The native input.'], ['Right icons', '<code>input-actions</code>, <code>__btn</code>, <code>__clear</code>, <code>__divider</code>', 'Clear shows only while the field has a value.'], ['Message', '<code>form-helper</code>, <code>--error</code>, <code>--success</code>, <code>--disabled</code>', 'Optional icon (<code>input-icon</code>).']]) + \
    '<h3 class="ds-h3 ds-group">Types</h3>' + table(['Type', 'Left icon', 'Right icons'], [['Plain', 'No', 'No'], ['Left icon', 'Yes', 'No'], ['Left and right icons', 'Yes', 'Clear, divider and action icons'], ['Clear only', 'Optional', 'Clear'], ['Actions only', 'Optional', 'Action icons (no clear, no divider)']]) + \
    '<h3 class="ds-h3 ds-group">Width</h3>' + desc('The field fills its container.')

st_motion = '<h2 class="ds-h2">Motion</h2>' + table(['Property', 'Duration', 'Easing'], [['<code>opacity</code> of the focus ring', '<code>duration-fast-3</code>', '<code>ease-standard</code>']])

st_behavior = '<h2 class="ds-h2">Behavior</h2>' + table(['Input', 'Result'], [
    ['Type a value', 'The field becomes Active: black border and the clear button appears.'], ['Clear button', 'Empties the field and returns focus to it. It is a real <code>button</code> with an <code>aria-label</code>.'],
    ['Tab', 'The blue ring shows on keyboard focus only (<code>body.keyboard-nav</code>, set by a small script).'], ['Hover on a right icon', 'Button: grey fill (<code>surface-opacity-black-05</code>). Icon Button: the icon turns <code>text-action-primary-hover</code>.'],
    ['Disabled', 'Not focusable. Grey fill, light border, <code>text-disabled</code> for text, icons and message.']])

st_access = '<h2 class="ds-h2">Accessibility Requirements</h2>' + table(['Topic', 'Requirement'], [
    ['Label', 'Always a <code>label</code> with <code>for</code> and <code>id</code>. Search fields without a visible label need an <code>aria-label</code>.'], ['Error', 'Set <code>aria-invalid="true"</code> and point <code>aria-describedby</code> at the message.'],
    ['Icon buttons', 'Real <code>button</code> elements with an <code>aria-label</code>. The decorative icons are <code>aria-hidden="true"</code>.'], ['Focus', 'A 2px ring on keyboard focus (<code>border-focus</code>), not on mouse click (WCAG 2.4.7, 1.4.11).'],
    ['Color', 'Error and success are not shown by color alone: the message says it, and an icon helps.'], ['Disabled', 'Not focusable. Disabled tokens are exempt from contrast requirements.']]) + \
    note('<strong>Open point:</strong> multi-line text fields are a separate component: see ' + '<a class="inline-link inline-link--medium inline-link--secondary" href="textarea.html">Text area</a>.')

spec = [('design-tokens', st_tok), ('sizes', st_sizes), ('measurements', st_meas), ('states', st_states), ('typography', st_typo), ('structure', st_struct), ('motion', st_motion), ('behavior', st_behavior), ('accessibility-requirements', st_access)]

# ---------------------------------------------------------------- Code
c_basic = '<h2 class="ds-h2">Basic Usage</h2>' + desc('Link the shared stylesheet once per page, and add the keyboard script. Never copy the rules into a page.') + table(['Step', 'What to do'], [
    ['1. Link', '<code>&lt;link rel="stylesheet" href="/components/css/input.css"&gt;</code>. Both templates already have it.'], ['2. Markup', 'A <code>form-field</code> with a <code>label</code>, an <code>input-wrap</code> around an <code>input-box</code> holding the <code>input</code>, and an optional <code>form-helper</code> message.'],
    ['3. Size', 'Large is the default. Add <code>input-box--sm</code> and <code>form-label--sm</code> for Small, <code>input-box--xs</code> for XSmall (desktop only).'], ['4. Keyboard focus', 'Add the script under CSS / Tailwind once per page. Without it the ring never shows on keyboard focus.']])
c_in = '<h2 class="ds-h2">Input</h2>' + desc('Copy the markup you need. Hover and focus come from <code>:hover</code> and keyboard focus; the <code>[data-state]</code> selectors in the CSS exist only so the documentation can force a state.') + '<div id="recipes"></div>'
c_def = '<h2 class="ds-h2">Related fields</h2>' + note('To be added. Number, password and date fields have no variants of their own yet. Multi-line text is <a class="inline-link inline-link--medium inline-link--secondary" href="textarea-code.html">Text area</a>.')
c_api = '<h2 class="ds-h2">API</h2><h3 class="ds-h3 ds-group">Classes</h3>' + table(['Class', 'Use'], [
    ['<code>form-field</code>', 'The column: label, wrapper, message.'], ['<code>form-label</code>, <code>form-label--sm</code>', 'The label. <code>--sm</code> for Small and XSmall.'], ['<code>input-wrap</code>', 'The wrapper that draws the focus ring.'],
    ['<code>input-box</code>, <code>--sm</code>, <code>--xs</code>', 'The box. Large, Small, XSmall.'], ['<code>input-box--error</code>, <code>--success</code>', 'Red or green border.'], ['<code>form-input</code>', 'The native input.'],
    ['<code>input-icon</code>, <code>--lg</code>, <code>--fill</code>', 'A Material Symbols icon. <code>--lg</code> is 24px, <code>--fill</code> is the filled clear icon.'], ['<code>input-actions</code>, <code>__btn</code>, <code>__clear</code>, <code>__divider</code>', 'The right-hand icons.'],
    ['<code>form-helper</code>, <code>--error</code>, <code>--success</code>, <code>--disabled</code>', 'The message.']]) + \
    '<h3 class="ds-h3 ds-group">Things to know</h3>' + bullets(['The clear button shows only while the field has a value, through <code>:placeholder-shown</code>. The placeholder is therefore required, even if it is a single space.', 'The Active border (black) also comes from <code>:placeholder-shown</code>.', 'A button next to a field uses the matching size: Input Large → <code>btn--md</code>, Small → <code>btn--sm</code>, XSmall → <code>btn--xs</code>.', 'The docs controls (playgrounds) are Small inputs (<code>input-box--sm</code>).', 'The <code>[data-state]</code> selectors do nothing outside the documentation pages.'])
c_css = '<h2 class="ds-h2">CSS / Tailwind</h2>' + desc('The component is one CSS file, shared by every page. Link it, never copy it. The CSS below is read from the file the page links, so it is always what you see.') + code_box('css-code', 'CSS (components/css/input.css)') + '<div style="margin-top:16px">' + code_box('js-code', 'JavaScript (focus ring on keyboard only)') + '</div>'

code = [('basic-usage', c_basic), ('input', c_in), ('related-fields', c_def), ('api', c_api), ('css-tailwind', c_css, False)]

# ---------------------------------------------------------------- scripts
FIELD_JS = old_js('input', "  var uid = 0, ACTIONS", "  /* ── Breakpoint preview")
HINT_JS = "  var HINT = { enabled: 'Helper text', hover: 'Helper text', active: 'Helper text', focus: 'Helper text', error: 'Enter a valid order number.', success: 'Order number found.', disabled: 'This field cannot be edited.' };\n"
FIELD_JS = FIELD_JS.replace("  /* Keyboard focus ring: only after Tab */\n  document.addEventListener('keydown', function (e) { if (e.key === 'Tab') document.body.classList.add('keyboard-nav'); });\n  document.addEventListener('mousedown', function () { document.body.classList.remove('keyboard-nav'); });\n", '')

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

JS_EX = FIELD_JS + SYNC + r'''
  /* ── Playground ── */
  var pg = { size: 'lg', state: 'enabled', left: 'off', right: 'none', msgIcon: 'off' };
''' + old_js('input', "  function renderPg() {", "  $$('[data-pg]').forEach") + r'''
  DK.wire(pg, renderPg);
  $('#pg-label').addEventListener('input', renderPg); $('#pg-hint').addEventListener('input', renderPg);

  /* ── Usage figures ── */
  clear($('#fig-do')).appendChild(field({ size: 'sm', label: 'Order number', placeholder: 'Enter the number', hint: 'Found on your order confirmation.' }));
  clear($('#fig-dont')).appendChild(field({ size: 'sm', placeholder: 'Order number', aria: 'Order number' }));
  [['#fig-err-do', 'Enter a valid email address.'], ['#fig-err-dont', '']].forEach(function (e) { var n = field({ size: 'sm', state: 'error', label: 'Email', placeholder: 'name@example.com', hint: e[1] }); clear($(e[0])).appendChild(n); $('input', n).value = 'name@'; });

  /* ── Variants and sizes ── */
  var sz = clear($('#v-sizes'));
  [['lg', 'Large'], ['sm', 'Small'], ['xs', 'XSmall']].forEach(function (s) {
    sz.appendChild(field({ size: s[0], label: s[1], placeholder: 'Placeholder', left: 'search', hint: 'Helper text' }));
  });
  var ic = clear($('#v-icons'));
  ic.appendChild(field({ label: 'Left icon', placeholder: 'Search', left: 'search' }));
  ic.appendChild(field({ label: 'Clear', placeholder: 'Placeholder', state: 'active', value: 'Value', right: 'clear' }));
  ic.appendChild(field({ label: 'Clear + actions', placeholder: 'Placeholder', state: 'active', value: 'Value', left: 'search', right: 'both' }));
  ic.appendChild(field({ label: 'Actions only', placeholder: 'Placeholder', right: 'actions' }));
  var ms = clear($('#v-messages'));
  [['enabled', 'Hint'], ['error', 'Error'], ['success', 'Success'], ['disabled', 'Disabled']].forEach(function (m) {
    ms.appendChild(field({ label: m[1], placeholder: 'Placeholder', state: m[0], hint: HINT[m[0]] }));
  });

  /* ── Anatomy ── */
  var ah = clear($('#a-host'));
  ah.appendChild(field({ size: 'lg', label: 'Label', placeholder: 'Placeholder', state: 'active', value: 'Value', left: 'search', right: 'both', hint: 'Message' }));
  var an = $('#in-anat');
  function txt(el) { return function () { var r = document.createRange(); r.selectNodeContents(el); return r.getBoundingClientRect(); }; }
  function union(sel) { return function () { var els = $$(sel, ah), a = els[0].getBoundingClientRect(), z = els[els.length - 1].getBoundingClientRect(); return { left: a.left, top: a.top, width: z.right - a.left, height: a.height }; }; }
  DK.callouts(an, [
    { n: 1, box: txt($('.form-label', ah)), side: 'top', len: 40 },
    { n: 2, el: $('.input-icon', ah), side: 'left', len: 48 },
    { n: 3, box: function () { var r = $('.form-input', ah).getBoundingClientRect(); return { left: r.left, top: r.top, width: 40, height: r.height }; }, side: 'bottom', len: 72 },
    { n: 4, el: $('.input-actions__clear', ah), side: 'top', len: 40 },
    { n: 5, el: $('.input-actions__divider', ah), side: 'bottom', len: 40 },
    { n: 6, box: union('.input-actions__btn:not(.input-actions__clear)'), side: 'top', len: 40 },
    { n: 7, box: txt($('.form-helper', ah)), side: 'bottom', len: 40 }
  ]);
  renderPg(); syncSizes();
'''

JS_SPEC = FIELD_JS + SYNC + r'''
  /* ── States matrix ── */
  var mx = { size: 'lg' };
  var ROWS = [['Enabled', 'enabled'], ['Hover', 'hover'], ['Active', 'active'], ['Focus', 'focus'], ['Error', 'error'], ['Success', 'success'], ['Disabled', 'disabled']];
  var COLS = [{ left: null, right: 'none' }, { left: 'search', right: 'none' }, { left: 'search', right: 'both' }];
  function buildMatrix() {
    var tb = clear($('#matrix tbody'));
    ROWS.forEach(function (r) {
      var tr = document.createElement('tr'), th = document.createElement('th'); th.scope = 'row'; th.textContent = r[0]; tr.appendChild(th);
      COLS.forEach(function (c) {
        var td = document.createElement('td');
        td.appendChild(field({ size: mx.size, state: r[1], label: 'Label', placeholder: 'Placeholder', left: c.left, right: c.right, hint: HINT[r[1]] }));
        tr.appendChild(td);
      });
      tb.appendChild(tr);
    });
  }
  DK.seg($('[data-mx="size"]'), function (v) { mx.size = v; buildMatrix(); });
  buildMatrix();
  DK.tokenTable($('#tok-table tbody'), [
    ['Enabled', 'Border', 'border-input-default'], ['Enabled', 'Fill', 'surface-raised-primary'], ['Enabled', 'Placeholder, message', 'text-tertiary'],
    ['Hover', 'Border', 'border-hover'], ['Active', 'Border', 'border-selected'], ['Active', 'Input text', 'text-primary'], ['Active', 'Divider', 'border-tertiary'],
    ['Focus', 'Ring (2px, 3px outside)', 'border-focus'], ['Error', 'Border', 'border-danger-default'], ['Error', 'Message', 'text-danger-default'],
    ['Success', 'Border', 'border-success-default'], ['Success', 'Message', 'text-success-default'],
    ['Disabled', 'Border', 'border-disabled'], ['Disabled', 'Fill', 'surface-raised-secondary'], ['Disabled', 'Text, icons, message', 'text-disabled'],
    ['All', 'Left icon', 'icon-primary'], ['All', 'Right icons', 'text-action-primary'], ['All', 'Right icon hover (Icon Button)', 'text-action-primary-hover'], ['All', 'Right icon hover (Button fill)', 'surface-opacity-black-05'], ['All', 'Label', 'text-primary']
  ]);
'''

JS_CODE = r'''
  DK.recipes($('#recipes'), [
    ['Standard', '<div class="form-field">\n  <label class="form-label form-label--sm" for="name">Name</label>\n  <div class="input-wrap">\n    <div class="input-box">\n      <input class="form-input" id="name" type="text" placeholder="Placeholder" />\n    </div>\n  </div>\n  <div class="form-helper">Helper text</div>\n</div>'],
    ['Error', '<div class="form-field">\n  <label class="form-label form-label--sm" for="email">Email</label>\n  <div class="input-wrap">\n    <div class="input-box input-box--error">\n      <input class="form-input" id="email" type="email" placeholder="name@example.com" aria-invalid="true" aria-describedby="email-msg" />\n    </div>\n  </div>\n  <div class="form-helper form-helper--error" id="email-msg"><span class="input-icon" aria-hidden="true">error</span>Enter a valid email address.</div>\n</div>'],
    ['Search with left icon', '<div class="form-field">\n  <div class="input-wrap">\n    <div class="input-box">\n      <span class="input-icon input-icon--lg" aria-hidden="true">search</span>\n      <input class="form-input" type="text" placeholder="Search" aria-label="Search" />\n    </div>\n  </div>\n</div>'],
    ['Clear and action icons', '<div class="input-box">\n  <input class="form-input" id="q" type="text" placeholder="Placeholder" />\n  <div class="input-actions">\n    <button type="button" class="input-actions__btn input-actions__clear" aria-label="Clear"><span class="input-icon input-icon--fill" aria-hidden="true">cancel</span></button>\n    <span class="input-actions__divider"></span>\n    <button type="button" class="input-actions__btn" aria-label="Scan a code"><span class="input-icon" aria-hidden="true">qr_code_scanner</span></button>\n  </div>\n</div>\n<!-- clear shows only while the field has a value; wire it: clear.onclick = () => { input.value = ""; input.focus(); } -->'],
    ['Small and XSmall', '<!-- Small -->\n<div class="input-box input-box--sm">...</div>\n<label class="form-label form-label--sm">...</label>\n<!-- XSmall (desktop only) -->\n<div class="input-box input-box--xs">...</div>']
  ]);
  DK.printCss($('#css-code'), 'input', [[/:is\(:hover, \[data-state="hover"\]\)/g, ':hover'], [/,\n    \.input-wrap\[data-state="focus"\]::after/g, ''], [/^ {4}/gm, '']]);
  $('#js-code').textContent = "document.addEventListener('keydown', function (e) { if (e.key === 'Tab') document.body.classList.add('keyboard-nav'); });\ndocument.addEventListener('mousedown', function () { document.body.classList.remove('keyboard-nav'); });";
'''

C = dict(
    slug=SLUG, title='Input', eyebrow='Components · Form',
    lead='An input field lets the user enter <strong>free text, numbers or search terms</strong>. It can have a label, a left icon, right-hand action icons and a message that explains or validates the value.',
    lead_ex='Every example on this page is the real component, not a picture. Type, click, tab and clear the value to try it. Figma: ' + fig_link(FIGMA, 'Base Input') + '.',
    lead_spec='Tokens, sizes, measurements, states and requirements. Values come from the live token package and from Figma: ' + fig_link(FIGMA, 'Base Input') + '.',
    lead_code='How to add an input field to a page. The file is <code>components/css/input.css</code>.',
    css=[], style=STYLE, ex=ex, spec=spec, code=code, js_ex=JS_EX, js_spec=JS_SPEC, js_code=JS_CODE)

if __name__ == '__main__':
    emit(C)
