from build import *

FIGMA = 'https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=1524-56967'
SLUG = 'textarea'

STYLE = r'''    .pg-note { font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-tertiary); }
    .ta-col { display: flex; flex-direction: column; gap: 24px; width: 100%; max-width: 360px; }
    .ta-grid { display: grid; gap: 32px 24px; grid-template-columns: minmax(0, 1fr); width: 100%; }
    @media (min-width: 769px) { .ta-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
    .ta-matrix td { min-width: 280px; vertical-align: top; padding-top: 16px; padding-bottom: 16px; }
    .ta-matrix .form-field { min-width: 240px; }
    .ta-fig { width: 100%; max-width: 320px; }
    .ta-measure { display: block; width: 280px; }   /* demo: a fixed width, so the padding strips have a text area to sit on */
    .ds-callout__art { padding-right: 24px; width: 100%; max-width: 360px; }'''

playground = '<h2 class="ds-h2">Playground</h2>' + desc('Choose a breakpoint and state and the field and its code update. Hover and focus are forced here so they can be seen; type in the field to get the Active state and see the word count change.') + \
    '<div class="ds-playground"><div class="ds-stage ds-stage--center" id="pg-stage"><div class="ta-col" id="pg-host"></div></div><div class="ds-controls">' + \
    bp_field('pg-l-bp') + \
    '<div class="ds-field form-field"><label class="form-label form-label--sm" for="sel-pg-l-st" id="pg-l-st">State</label><div class="input-wrap"><select class="form-select form-select--sm" data-pg="state" id="sel-pg-l-st"><option value="enabled">Enabled</option><option value="hover">Hover</option><option value="active">Active</option><option value="focus">Focus</option><option value="error">Error</option><option value="success">Success</option><option value="disabled">Disabled</option></select><span class="form-select-arrow" aria-hidden="true">arrow_drop_down</span></div></div>' + \
    btn_group('pg-l-cnt', 'Word count', 'data-pg="count"', [('on', 'Shown', True), ('off', 'Hidden', False)]) + \
    '<div class="ds-field form-field"><label class="form-label form-label--sm" for="pg-label">Label</label><div class="input-wrap"><div class="input-box input-box--sm"><input class="form-input" type="text" id="pg-label" value="Comment" placeholder="Label" /></div></div></div>' + \
    '<div class="ds-field form-field"><label class="form-label form-label--sm" for="pg-hint">Message</label><div class="input-wrap"><div class="input-box input-box--sm"><input class="form-input" type="text" id="pg-hint" value="Tell us what you think." placeholder="Message" /></div></div></div>' + \
    '</div></div><h3 class="ds-h3">Markup for this selection</h3>' + code_box('pg-code', 'HTML')

overview = '<h2 class="ds-h2">Overview</h2>' + desc('A text area lets the user enter text over multiple lines: comments, feedback or longer passages that need more room than a single-line input. It has a label, an optional word count, a resizer and a message that explains or validates the value.') + \
    desc('Text area has one size and seven states. The user can drag the corner to make the field taller.') + \
    three_pages(SLUG, 'a text area', 'the values: tokens, sizes, measurements, states and requirements', 'how to add one to a page')

usage = '<h2 class="ds-h2">Usage</h2><h3 class="ds-h3 ds-group">When to use</h3>' + desc('Use a text area when the user writes more than a short value. Use it to:') + \
    bullets(['Write a comment or a message', 'Give feedback or a review', 'Enter a longer passage, such as a description or a note']) + \
    '<h3 class="ds-h3 ds-group">When not to use</h3><h3 class="ds-h3">For a short value</h3>' + desc('A name, a number or a search term fits on one line. Use <code>eco-input</code>: a text area suggests that a long answer is expected.') + \
    fig_pair('<div class="ta-fig" id="fig-do"></div>', 'Do use a text area for a comment.', '<div class="ta-fig" id="fig-dont"></div>', 'Do not use a text area for a short single-line value.') + \
    '<h3 class="ds-h3">Say what is wrong</h3>' + desc('An invalid field says what is wrong in the message, with the error icon. A red border alone is easy to miss and is not enough for everyone.') + \
    fig_pair('<div class="ta-fig" id="fig-err-do"></div>', 'Do explain what is wrong in the message, with the error icon.', '<div class="ta-fig" id="fig-err-dont"></div>', 'Do not rely on a red border alone.') + \
    '<h3 class="ds-h3 ds-group">Quick reference</h3>' + \
    table(['The user…', 'Use'], [['writes a comment, feedback or a longer passage', 'Text area'], ['types a short value: a name, a number, a search term', '<code>eco-input</code>'], ['picks one value from a fixed list', '<code>eco-select</code>'], ['picks one of two or three options', '<code>eco-radio</code>']]) + \
    rules(['Give every field a visible label, uppercase, and sentence case for any pre-filled text.', 'Show the word count when there is a character limit, and set <code>maxlength</code> to match.', 'Explain what is wrong in the message, with the error icon.', 'Let the user resize the field vertically.'],
          ['Use a text area for a short single-line value.', 'Use a placeholder as the label.', 'Show the focus ring on mouse click, or remove it on keyboard focus.', 'Use color alone for error or success.'])

anatomy = '<h2 class="ds-h2">Anatomy</h2><h3 class="ds-h3 ds-group">Text area</h3>' + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout" id="ta-anat" role="img" aria-label="Anatomy of a text area: 1 label, 2 word count, 3 text, 4 resizer, 5 message"><div class="ds-callout__art"><div class="ta-col" id="a-host"></div></div></div></figure></div>' + \
    ol_parts([('Label', '<code>label-md</code> (mobile <code>label-sm</code>), uppercase, 4px above the box.'), ('Word count', '<code>body-sm</code>, right-aligned on the label row. Optional.'), ('Text', '<code>body-md</code>, 12px padding, 66px minimum height. The placeholder is <code>text-tertiary</code>.'),
              ('Resizer', 'The handle in the bottom-right corner. Vertical resize only.'), ('Message', '<code>body-sm</code>, 4px below the box. Hint, error or success.')]) + \
    desc('The focus ring is a separate element around the box, 2px and 3px outside it, so focusing never changes the layout or the box size.')

variants = '<h2 class="ds-h2">Variants</h2>' + desc('A text area has no size or type variants. What changes is the word count and the message.') + \
    '<h3 class="ds-h3 ds-group">Word count</h3>' + desc('The word count sits on the label row, on the right. Use it when the text has a limit (<code>maxlength</code>); leave it out when there is none.') + fig_one('<div class="ta-grid" id="v-count"></div>') + \
    '<h3 class="ds-h3 ds-group">Messages</h3>' + desc('The message sits below the field, in <code>body-sm</code>. Hint text is neutral; error and success change the color of the border and the message. An error message has a leading icon so color is never the only signal.') + fig_one('<div class="ta-grid" id="v-messages"></div>')

sizes = '<h2 class="ds-h2">Sizes</h2>' + desc('There is one size. Figma defines only the Desktop version; below 769px the label and text use the smaller mobile type styles (same as the input). The component switches by itself; the Breakpoint toggle forces one for preview. Measurements are under ' + sec_link(SLUG, 'sizes', 'Sizes') + ' in Specifications.') + \
    toolbar([('vb-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force')]) + fig_one('<div class="ta-fig" id="v-size"></div>')

layout = '<h2 class="ds-h2">Layout &amp; Appearance</h2><h3 class="ds-h3 ds-group">Width</h3>' + desc('The field fills its container: set the width on the container, not on the field. In the examples on this page the container is 360px or narrower.') + \
    '<h3 class="ds-h3 ds-group">Appearance</h3>' + desc('The box has a 1px border and a white fill, with 12px padding. The border turns black when the field has a value, and the message and the border turn red or green for error and success. The focus ring is a 2px blue frame around the box. Token names and values are under ' + sec_link(SLUG, 'design-tokens', 'Design Tokens') + ' in Specifications.')

behavior = '<h2 class="ds-h2">Behavior</h2><h3 class="ds-h3 ds-group">Typing</h3>' + desc('When the user types a value the field becomes Active (black border). The word count updates; <code>maxlength</code> stops typing at the limit.') + \
    '<h3 class="ds-h3 ds-group">Resizing</h3>' + desc('The user can drag the corner handle to make the field taller (vertical only). It never goes below the 66px minimum. A disabled field cannot be resized.') + fig_one('<div class="ta-grid" id="v-resize"></div>') + \
    '<h3 class="ds-h3 ds-group">Hover and focus</h3>' + desc('Hover changes the border. The blue ring shows on keyboard focus only (<code>body.keyboard-nav</code>, set by a small script). All states are listed under ' + sec_link(SLUG, 'states', 'States') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Error and success</h3>' + desc('Set <code>aria-invalid="true"</code> on an invalid field and point <code>aria-describedby</code> at the message.') + \
    '<h3 class="ds-h3 ds-group">Disabled</h3>' + desc('A disabled field is not focusable. It has a grey fill, a light border, <code>text-disabled</code> for the text and the message, and no resize.')

access = '<h2 class="ds-h2">Accessibility</h2>' + desc('All requirements are listed under ' + sec_link(SLUG, 'accessibility-requirements', 'Accessibility Requirements') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Keyboard support</h3>' + desc('Tab moves into and out of the field. The focus ring shows on keyboard focus only. Add the keyboard script once per page (see Code).') + \
    '<h3 class="ds-h3 ds-group">Screen reader support</h3>' + desc('Every field has a <code>label</code> with <code>for</code> and <code>id</code>. A placeholder is never the label. An invalid field gets <code>aria-invalid="true"</code> and <code>aria-describedby</code> that points at the message.')

related = '<h2 class="ds-h2">Related</h2><ul class="ds-bullets"><li><strong>' + link_large('input.html', 'Input') + '</strong>. A single line of text.</li><li><strong>' + link_large('select.html', 'Select') + '</strong>. One value from a list.</li><li><strong>' + link_large('radio.html', 'Radio button') + '</strong>. One of two or three options.</li></ul>'

references = '<h2 class="ds-h2">References</h2>' + refs([
    ('https://www.w3.org/WAI/WCAG22/Understanding/labels-or-instructions.html', 'WCAG 2.2: Labels or Instructions', 'Success criterion 3.3.2.'),
    ('https://www.w3.org/WAI/WCAG22/Understanding/error-identification.html', 'WCAG 2.2: Error Identification', 'Success criterion 3.3.1.'),
    ('https://www.nngroup.com/articles/form-design-placeholders/', 'Nielsen Norman Group: Placeholders in Form Fields Are Harmful', 'Why a placeholder is not a label.'),
    ('https://m3.material.io/components/text-fields/overview', 'Material Design 3: Text fields', 'Google.'),
    ('https://carbondesignsystem.com/components/text-area/usage/', 'Carbon Design System: Text area', 'IBM.')])

ex = [('playground', playground), ('overview', overview), ('usage', usage), ('anatomy', anatomy), ('variants', variants), ('sizes', sizes), ('layout', layout), ('behavior', behavior), ('accessibility', access), ('related', related), ('references', references)]

# ---------------------------------------------------------------- Specifications
st_tok = '<h2 class="ds-h2">Design Tokens</h2>' + desc('Resolved from the live token package.') + \
    '<div class="ds-table-wrap"><table class="ds-table" id="tok-table"><thead><tr><th scope="col">State</th><th scope="col">Part</th><th scope="col">Token</th><th scope="col">Value</th></tr></thead><tbody></tbody></table></div>'

st_sizes = '<h2 class="ds-h2">Sizes</h2>' + table(['Breakpoint', 'Min height', 'Padding', 'Label', 'Text', 'Word count, message'], [
    ['Desktop (769px+)', '66px', '12px', '<code>label-md</code> 16/16, 0.48px', '<code>body-md</code> 17/24, 0.32px', '<code>body-sm</code> 14/20, 0.36px'],
    ['Mobile (below 769px)', '66px', '12px', '<code>label-sm</code> 12/12, 0.48px', '<code>body-md</code> 16/22, 0.32px', '<code>body-sm</code> 14/20, 0.36px']]) + \
    note('There is one size. Figma has no Size axis and only a Desktop version, so the mobile type values are taken from <code>eco-input</code> (same label and body styles) until a Mobile frame exists.')

st_meas = '<h2 class="ds-h2">Measurements</h2><h3 class="ds-h3 ds-group">Dimensions</h3>' + desc('Padding of the text area. The shaded area is the padding; the lines show its value. It is the same at every breakpoint.') + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-fig__stage--flush" style="padding:0;min-height:0"><div class="measure" role="img" aria-label="Padding of the text area: 12 on every side"><div class="measure__item"><span class="measure__name">1 · Text area</span><div class="measure__obj"><span class="ta-measure"><textarea class="form-textarea measure__subject" placeholder="Placeholder text" tabindex="-1" aria-label="Text area"></textarea></span>' + \
    '<i class="measure__pad measure__pad--t"></i><i class="measure__pad measure__pad--b"></i><i class="measure__pad measure__pad--l"></i><i class="measure__pad measure__pad--r"></i><b class="measure__dim measure__dim--v measure__dim--t"><span></span></b><b class="measure__dim measure__dim--v measure__dim--b"><span></span></b><b class="measure__dim measure__dim--h measure__dim--l"><span></span></b><b class="measure__dim measure__dim--h measure__dim--r"><span></span></b></div></div></div></div><figcaption class="ds-fig__cap">The text area at true size (1:1). The numbers are read from the component.</figcaption></figure></div>' + \
    table(['Attribute', 'Value'], [['Padding', '12px on every side'], ['Minimum height', '66px (a literal: there is no token)'], ['Border', '1px'], ['Corners', 'Square'], ['Width', 'Fills the container'], ['Resize', 'Vertical only, never below 66px']]) + \
    '<h3 class="ds-h3 ds-group">Spacing</h3>' + desc('The same padding and distances as spacing tokens.') + table(['Part', 'Value'], [['Padding', '<code>space-12</code>'], ['Label row to box', '<code>space-4</code>'], ['Box to message', '<code>space-4</code>'], ['Label to word count', '<code>space-8</code> minimum'], ['Focus ring', '2px line, 3px outside the box']])

st_states = '<h2 class="ds-h2">States</h2>' + desc('All seven states from Figma, with and without the word count. Hover and focus are forced on this page; in your code they come from <code>:hover</code> and keyboard focus. Active means the field has a value.') + \
    toolbar([('sb-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force')]) + \
    '<div class="ds-table-wrap"><table class="ds-table ta-matrix" id="matrix"><thead><tr><th scope="col">State</th><th scope="col">With word count</th><th scope="col">Without word count</th></tr></thead><tbody></tbody></table></div>'

st_typo = '<h2 class="ds-h2">Typography</h2>' + table(['Part', 'Type', 'Size / line height', 'Letter spacing', 'Weight'], [
    ['Label, Desktop', '<code>label-md</code>', '16/16', '0.48px', 'Bold, uppercase'], ['Label, Mobile', '<code>label-sm</code>', '12/12', '0.48px', 'Bold, uppercase'], ['Text, Desktop', '<code>body-md</code>', '17/24', '0.32px', 'Regular'], ['Text, Mobile', '<code>body-md</code>', '16/22', '0.32px', 'Regular'],
    ['Word count, message', '<code>body-sm</code>', '14/20', '0.36px', 'Regular']]) + note('Breuer Condensed with <code>ss02</code> and <code>ss03</code> (the text and the message also <code>ss06</code>).')

st_struct = '<h2 class="ds-h2">Structure</h2><h3 class="ds-h3 ds-group">Elements</h3>' + table(['Element', 'Class', 'Notes'], [
    ['Field', '<code>form-field</code>', 'Label row, wrapper and message in a column, 4px apart.'], ['Label row', '<code>form-field__head</code>', 'Label on the left, word count on the right.'], ['Label', '<code>form-label</code>', 'Uppercase.'], ['Word count', '<code>form-count</code>', 'Optional. <code>0/100</code> format.'],
    ['Wrapper', '<code>input-wrap</code>', 'Carries the focus ring (2px, 3px outside the box).'], ['Text area', '<code>form-textarea</code>, <code>--error</code>, <code>--success</code>', 'The native <code>textarea</code>. Border, fill and height.'], ['Message', '<code>form-helper</code>, <code>--error</code>, <code>--success</code>, <code>--disabled</code>', 'Optional icon (<code>input-icon</code>).']]) + \
    '<h3 class="ds-h3 ds-group">Types</h3>' + desc('There is one type. The word count is optional.') + '<h3 class="ds-h3 ds-group">Width</h3>' + desc('The field fills its container.')

st_motion = '<h2 class="ds-h2">Motion</h2>' + table(['Property', 'Duration', 'Easing'], [['<code>opacity</code> of the focus ring', '<code>duration-fast-3</code>', '<code>ease-standard</code>']])

st_behavior = '<h2 class="ds-h2">Behavior</h2>' + table(['Input', 'Result'], [
    ['Type a value', 'The field becomes Active (black border). The word count updates; <code>maxlength</code> stops typing at the limit.'], ['Drag the corner', 'The field grows or shrinks in height only. It never goes below the 66px minimum.'],
    ['Tab', 'The blue ring shows on keyboard focus only (<code>body.keyboard-nav</code>, set by a small script).'], ['Disabled', 'Not focusable. Grey fill, light border, <code>text-disabled</code> for text and message, no resize.']])

st_access = '<h2 class="ds-h2">Accessibility Requirements</h2>' + table(['Topic', 'Requirement'], [
    ['Label', 'Always a <code>label</code> with <code>for</code> and <code>id</code>. A placeholder is never the label.'], ['Error', 'Set <code>aria-invalid="true"</code> and point <code>aria-describedby</code> at the message.'], ['Focus', 'A 2px ring on keyboard focus (<code>border-focus</code>), not on mouse click (WCAG 2.4.7, 1.4.11).'],
    ['Color', 'Error and success are not shown by color alone: the message says it, and the error message has an icon.'], ['Disabled', 'Not focusable. Disabled tokens are exempt from contrast requirements.']]) + \
    note('<strong>Open points:</strong> Figma has only a Desktop version, so the mobile type values are taken from the input. Disabled uses <code>border-primary</code> and focus uses a <code>text-secondary</code> placeholder, both as in Figma and both different from the input. The resizer is the browser’s own handle, not the 8px Figma icon. Details are in the skill’s Flags.')

spec = [('design-tokens', st_tok), ('sizes', st_sizes), ('measurements', st_meas), ('states', st_states), ('typography', st_typo), ('structure', st_struct), ('motion', st_motion), ('behavior', st_behavior), ('accessibility-requirements', st_access)]

# ---------------------------------------------------------------- Code
c_basic = '<h2 class="ds-h2">Basic Usage</h2>' + desc('Link the shared stylesheet once per page, and add the keyboard script and, for a word count, the count script. Never copy the rules into a page.') + table(['Step', 'What to do'], [
    ['1. Link', '<code>&lt;link rel="stylesheet" href="/components/css/textarea.css"&gt;</code>. Both templates already have it.'], ['2. Markup', 'A <code>form-field</code> with a <code>label</code>, an <code>input-wrap</code> around the <code>textarea.form-textarea</code>, and an optional <code>form-helper</code> message.'],
    ['3. Word count', 'Put the label and a <code>span.form-count</code> in a <code>div.form-field__head</code>, set <code>maxlength</code>, and bind the count (script under CSS / Tailwind).'], ['4. Keyboard focus', 'Add the script under CSS / Tailwind once per page. Without it the ring never shows on keyboard focus.']])
c_ta = '<h2 class="ds-h2">Text area</h2>' + desc('Copy the markup you need. Hover and focus come from <code>:hover</code> and keyboard focus; the <code>[data-state]</code> selectors in the CSS exist only so the documentation can force a state.') + '<div id="recipes"></div>'
c_api = '<h2 class="ds-h2">API</h2><h3 class="ds-h3 ds-group">Classes</h3>' + table(['Class', 'Use'], [
    ['<code>form-field</code>', 'The column: label row, wrapper, message.'], ['<code>form-field__head</code>', 'The label row, with the word count on the right.'], ['<code>form-label</code>', 'The label. Use <code>form-label--sm</code> from <code>input.css</code> for the small label of a docs control.'],
    ['<code>form-count</code>', 'The word count.'], ['<code>input-wrap</code>', 'The wrapper that draws the focus ring.'], ['<code>form-textarea</code>, <code>--error</code>, <code>--success</code>', 'The text area and its error and success border.'], ['<code>form-helper</code>, <code>--error</code>, <code>--success</code>, <code>--disabled</code>', 'The message.']]) + \
    '<h3 class="ds-h3 ds-group">Things to know</h3>' + bullets(['The Active border (black) comes from <code>:placeholder-shown</code>, so the placeholder is required.', 'Resize is vertical only (<code>resize: vertical</code>) and never goes below 66px.', 'The word count is not automatic: bind it with the script under CSS / Tailwind and set <code>maxlength</code> to match.', 'The <code>[data-state]</code> selectors do nothing outside the documentation pages.'])
c_css = '<h2 class="ds-h2">CSS / Tailwind</h2>' + desc('The component is one CSS file, shared by every page. Link it, never copy it. The CSS below is read from the file the page links, so it is always what you see.') + code_box('css-code', 'CSS (components/css/textarea.css)') + '<div style="margin-top:16px">' + code_box('js-code', 'JavaScript (focus ring on keyboard only, word count)') + '</div>'
code = [('basic-usage', c_basic), ('text-area', c_ta), ('api', c_api), ('css-tailwind', c_css, False)]

# ---------------------------------------------------------------- scripts
FIELD_JS = "  var uid = 0, MAX = 100;\n" + old_js('textarea', "  function icon(name)", "  /* ── Breakpoint preview")

JS_EX = FIELD_JS + r'''
  /* ── Playground ── */
  var pg = { state: 'enabled', count: 'on' };
''' + old_js('textarea', "  function renderPg() {", "  $$('[data-pg]').forEach") + r'''
  DK.wire(pg, renderPg);
  $('#pg-label').addEventListener('input', renderPg); $('#pg-hint').addEventListener('input', renderPg);
  DK.bp();

  clear($('#fig-do')).appendChild(field({ label: 'Comment', count: true, hint: 'Tell us what you think.' }));
  [['#fig-err-do', 'Enter at least 10 characters.'], ['#fig-err-dont', '']].forEach(function (e) { clear($(e[0])).appendChild(field({ state: 'error', label: 'Comment', value: 'Too short', hint: e[1] })); });
  var shortOne = field({ label: 'Name', hint: '' }); clear($('#fig-dont')).appendChild(shortOne);

  var c = clear($('#v-count'));
  c.appendChild(field({ label: 'With word count', count: true, hint: 'Message or hint text' }));
  c.appendChild(field({ label: 'Without word count', hint: 'Message or hint text' }));
  var ms = clear($('#v-messages'));
  [['enabled', 'Hint'], ['error', 'Error'], ['success', 'Success'], ['disabled', 'Disabled']].forEach(function (m) {
    ms.appendChild(field({ label: m[1], count: true, state: m[0], hint: HINT[m[0]] }));
  });
  clear($('#v-size')).appendChild(field({ label: 'Comment', count: true, hint: 'Message or hint text' }));
  var rz = clear($('#v-resize'));
  rz.appendChild(field({ label: 'Resizable', count: true }));
  rz.appendChild(field({ label: 'Disabled, no resize', count: true, state: 'disabled' }));

  var ah = clear($('#a-host'));
  ah.appendChild(field({ state: 'active', label: 'Label', count: true, hint: 'Message or hint text', value: 'Text' }));
  function txt(el) { return function () { var r = document.createRange(); r.selectNodeContents(el); return r.getBoundingClientRect(); }; }
  DK.callouts($('#ta-anat'), [
    { n: 1, box: txt($('.form-label', ah)), side: 'top', len: 40 },
    { n: 2, el: $('.form-count', ah), side: 'top', len: 40 },
    { n: 3, box: function () { var r = $('.form-textarea', ah).getBoundingClientRect(); return { left: r.left, top: r.top, width: 40, height: r.height }; }, side: 'left', len: 48 },
    { n: 4, box: function () { var r = $('.form-textarea', ah).getBoundingClientRect(); return { left: r.right - 14, top: r.bottom - 14, width: 14, height: 14 }; }, side: 'right', len: 48 },
    { n: 5, box: txt($('.form-helper', ah)), side: 'bottom', len: 40 }
  ]);
  renderPg();
'''

JS_SPEC = FIELD_JS + r'''
  var ROWS = [['Enabled', 'enabled'], ['Hover', 'hover'], ['Active', 'active'], ['Focus', 'focus'], ['Error', 'error'], ['Success', 'success'], ['Disabled', 'disabled']];
  var tb = clear($('#matrix tbody'));
  ROWS.forEach(function (r) {
    var tr = document.createElement('tr'), th = document.createElement('th'); th.scope = 'row'; th.textContent = r[0]; tr.appendChild(th);
    [true, false].forEach(function (cnt) {
      var td = document.createElement('td');
      td.appendChild(field({ state: r[1], label: 'Label', count: cnt, hint: HINT[r[1]] }));
      tr.appendChild(td);
    });
    tb.appendChild(tr);
  });
  DK.tokenTable($('#tok-table tbody'), [
    ['Enabled', 'Border', 'border-input-default'], ['Enabled', 'Fill', 'surface-raised-primary'], ['Enabled', 'Placeholder, message', 'text-tertiary'],
    ['All', 'Label', 'text-primary'], ['All', 'Word count', 'text-secondary'],
    ['Hover', 'Border', 'border-hover'], ['Active', 'Border', 'border-selected'], ['Active', 'Text', 'text-primary'],
    ['Focus', 'Ring (2px, 3px outside)', 'border-focus'], ['Focus', 'Placeholder', 'text-secondary'],
    ['Error', 'Border', 'border-danger-default'], ['Error', 'Message', 'text-danger-default'],
    ['Success', 'Border', 'border-success-default'], ['Success', 'Message', 'text-success-default'],
    ['Disabled', 'Border', 'border-primary'], ['Disabled', 'Fill', 'surface-raised-secondary'], ['Disabled', 'Text, message', 'text-disabled'], ['Disabled', 'Label, word count', 'surface-60']
  ]);
  DK.bp();
'''

JS_CODE = r'''
  DK.recipes($('#recipes'), [
    ['Standard', '<div class="form-field">\n  <label class="form-label form-label--sm" for="comment">Comment</label>\n  <div class="input-wrap">\n    <textarea class="form-textarea" id="comment" placeholder="Placeholder text"></textarea>\n  </div>\n  <div class="form-helper">Message or hint text</div>\n</div>'],
    ['With word count', '<div class="form-field">\n  <div class="form-field__head">\n    <label class="form-label form-label--sm" for="comment">Comment</label>\n    <span class="form-count" id="comment-count">0/100</span>\n  </div>\n  <div class="input-wrap">\n    <textarea class="form-textarea" id="comment" maxlength="100" placeholder="Placeholder text"></textarea>\n  </div>\n</div>\n<script>bindCount(document.getElementById("comment"), document.getElementById("comment-count"));<\/script>'],
    ['Error', '<div class="form-field">\n  <label class="form-label form-label--sm" for="feedback">Feedback</label>\n  <div class="input-wrap">\n    <textarea class="form-textarea form-textarea--error" id="feedback" aria-invalid="true" aria-describedby="feedback-msg">Too short</textarea>\n  </div>\n  <div class="form-helper form-helper--error" id="feedback-msg"><span class="input-icon" aria-hidden="true">error</span>Enter at least 10 characters.</div>\n</div>'],
    ['Disabled', '<div class="form-field">\n  <label class="form-label form-label--sm" for="note">Note</label>\n  <div class="input-wrap">\n    <textarea class="form-textarea" id="note" placeholder="Placeholder text" disabled></textarea>\n  </div>\n  <div class="form-helper form-helper--disabled">This field cannot be edited.</div>\n</div>']
  ]);
  DK.printCss($('#css-code'), 'textarea', [[/:is\(:hover, \[data-state="hover"\]\)/g, ':hover'], [/,\n    \.input-wrap\[data-state="focus"\]::after/g, ''], [/^ {4}/gm, '']]);
  $('#js-code').textContent = "document.addEventListener('keydown', function (e) { if (e.key === 'Tab') document.body.classList.add('keyboard-nav'); });\ndocument.addEventListener('mousedown', function () { document.body.classList.remove('keyboard-nav'); });\n\n// word count: one textarea + its .form-count\nfunction bindCount(ta, count) {\n  var update = function () { count.textContent = ta.value.length + '/' + ta.maxLength; };\n  ta.addEventListener('input', update); update();\n}";
'''

C = dict(
    slug=SLUG, title='Text area', eyebrow='Components · Form',
    lead='A text area lets the user enter <strong>text over multiple lines</strong>: comments, feedback or longer passages that need more room than a single-line input.',
    lead_ex='Every example on this page is the real component, not a picture. Type, click and tab to try it. Figma: ' + fig_link(FIGMA, 'Text Area') + '.',
    lead_spec='Tokens, sizes, measurements, states and requirements. Values come from the live token package and from Figma: ' + fig_link(FIGMA, 'Text Area') + '.',
    lead_code='How to add a text area to a page. The file is <code>components/css/textarea.css</code>.',
    css_before=['textarea'], css=[], style=STYLE, ex=ex, spec=spec, code=code, js_ex=JS_EX, js_spec=JS_SPEC, js_code=JS_CODE)

if __name__ == '__main__':
    emit(C)
