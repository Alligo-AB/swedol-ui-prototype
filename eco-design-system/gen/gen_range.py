from build import *

SLUG = 'range'
BADGE = '<span class="badge-basic badge-basic--warning badge-basic--weak" title="No Figma component exists. The range was designed in the repo (first used in the toast and motion playgrounds).">Not verified with Figma</span>'

STYLE = r'''    .pg-note { font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-tertiary); }
    .pg-matrix td { vertical-align: middle; padding-top: 16px; padding-bottom: 16px; }
    .rg-wide { width: 100%; max-width: 480px; }
    .rg-fig { width: 100%; max-width: 320px; }
    .ds-callout__art { width: 100%; max-width: 480px; padding-right: 24px; }'''

playground = '<h2 class="ds-h2">Playground</h2>' + desc('A native range input with a label, the current value and tick labels. Drag, click the track or use the arrow keys. Hover and focus are live (they cannot be forced on a native slider thumb).') + \
    '<div class="ds-playground"><div class="ds-stage ds-stage--center" id="pg-stage"><div id="pg-host"></div></div><div class="ds-controls">' + \
    btn_group('pg-l-t', 'Type', 'data-pg="kind"', [('steps', 'Named steps', True), ('num', 'Numeric', False)]) + \
    btn_group('pg-l-r', 'Recommended', 'data-pg="rec"', [('off', 'None', False), ('on', 'Marked *', True)]) + \
    btn_group('pg-l-st', 'State', 'data-pg="state"', [('enabled', 'Enabled', True), ('disabled', 'Disabled', False)]) + \
    '<div class="ds-field form-field"><label class="form-label form-label--sm" for="pg-label">Label</label><div class="input-wrap"><div class="input-box input-box--sm"><input class="form-input" type="text" id="pg-label" value="Duration" placeholder="Label" /></div></div></div>' + \
    '</div></div><h3 class="ds-h3">Markup for this selection</h3>' + code_box('pg-code', 'HTML')

overview = '<h2 class="ds-h2">Overview</h2>' + desc('A range lets the user pick one value from an ordered series by dragging a thumb, with the current value shown as text.') + \
    desc('Range is a native <code>&lt;input type="range"&gt;</code> with a label, the value as text and optional tick labels. It is stepped over named values by default, but a numeric range between a minimum and a maximum works too. It has no Figma component: it was designed in the repo.') + \
    three_pages(SLUG, 'a range', 'the values: tokens, dimensions, states and requirements', 'how to add one to a page')

usage = '<h2 class="ds-h2">Usage</h2><h3 class="ds-h3 ds-group">When to use</h3>' + desc('Use a range when the value is a position on an ordered series and a precise number is not the point. Use it to:') + \
    bullets(['Pick an easing or a duration from named steps (the Motion sections of these docs)', 'Pick a number between a minimum and a maximum, such as an auto-hide time in seconds', 'Show a recommended step and let the user move away from it']) + \
    '<h3 class="ds-h3 ds-group">When not to use</h3><h3 class="ds-h3">For two or three options, or on and off</h3>' + desc('For two or three named options use <a class="inline-link inline-link--large inline-link--secondary" href="segment-control.html">Pill segment control</a> or <code>eco-radio</code>. For on and off use <a class="inline-link inline-link--large inline-link--secondary" href="switch.html">Switch</a>. For an exact number use <code>eco-input</code>.') + \
    fig_pair('<div class="rg-fig" id="fig-do"></div>', 'Do use a range for an ordered series of steps.', '<div class="rg-fig" id="fig-dont"></div>', 'Do not use a range for on and off. Use a switch.') + \
    '<h3 class="ds-h3 ds-group">Quick reference</h3>' + \
    table(['The user…', 'Use'], [['picks one value from an ordered series by dragging', 'Range'], ['picks one of two or three named options', '<a class="inline-link inline-link--small" href="segment-control.html">Pill segment control</a> or <code>eco-radio</code>'], ['turns something on or off', '<a class="inline-link inline-link--small" href="switch.html">Switch</a>'], ['types an exact number', '<code>eco-input</code>']]) + \
    rules(['Keep to about 4–12 steps in a 480px control.', 'Show the current value as text.', 'Mark the recommended step and explain the *.', 'Link <code>range.css</code> and <code>range.js</code>.'], ['Build a slider from <code>div</code>s.', 'Use it for two or three options.', 'Use it for exact numbers.', 'Let tick labels collide: use fewer via <code>data-ticks</code>.'])

anatomy = '<h2 class="ds-h2">Anatomy</h2><h3 class="ds-h3 ds-group">Range</h3>' + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout" id="rg-anat" role="img" aria-label="Anatomy of a range: 1 label, 2 value, 3 track, 4 thumb, 5 tick labels"><div class="ds-callout__art"><div id="a-host"></div></div></div></figure></div>' + \
    ol_parts([('Label', 'Always visible, linked with <code>for</code> and <code>id</code>. <code>label-sm</code>, <code>text-secondary</code>.'), ('Value', 'The current value as text, right of the label. <code>body-sm</code>. It comes from <code>data-labels</code>, or the number plus <code>data-unit</code>.'), ('Track', '2px high, <code>border-primary</code>, inside a 24px high hit area.'), ('Thumb', 'A 16px circle, <code>surface-100</code>. A 4px halo shows on hover.'), ('Tick labels', 'Optional, one per step, 12/16 <code>text-tertiary</code>. The recommended step gets a <code>*</code>.')])

variants = '<h2 class="ds-h2">Variants</h2>' + desc('Stepped over named values, or numeric between a minimum and a maximum.') + \
    '<h3 class="ds-h3 ds-group">Named steps with a recommended value</h3>' + fig_one('<div class="rg-wide" id="v-steps"></div>') + \
    '<h3 class="ds-h3 ds-group">Numeric with a unit</h3>' + fig_one('<div class="rg-wide" id="v-num"></div>')

sizes = '<h2 class="ds-h2">Sizes</h2>' + desc('There is one size, the same on every breakpoint: a 24px hit area, a 2px track and a 16px thumb. The touch size on mobile is smaller than the usual 44px target; raise the input height at <code>xs</code> and <code>sm</code> if design wants it. Dimensions are under ' + sec_link(SLUG, 'sizes', 'Sizes') + ' in Specifications.')

layout = '<h2 class="ds-h2">Layout &amp; Appearance</h2><h3 class="ds-h3 ds-group">Width</h3>' + desc('The range fills its container. The examples use a 480px control. Keep to about 4 to 12 steps in a 480px control, and use fewer tick labels via <code>data-ticks</code> if they collide.') + \
    '<h3 class="ds-h3 ds-group">Appearance</h3>' + desc('A thin grey track with a black round thumb. There is no dark-mode variant. Token names and values are under ' + sec_link(SLUG, 'design-tokens', 'Design Tokens') + ' in Specifications.')

behavior = '<h2 class="ds-h2">Behavior</h2><h3 class="ds-h3 ds-group">Dragging</h3>' + desc('Drag the thumb or click the track and the thumb moves; the value text updates. The input fires the normal <code>input</code> event, so your page listens for it to apply the value.') + \
    '<h3 class="ds-h3 ds-group">Hover and focus</h3>' + desc('Hover shows a 4px halo around the thumb. Focus is a 2px ring that shows on keyboard focus only. States are listed under ' + sec_link(SLUG, 'states', 'States') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Disabled</h3>' + desc('A disabled range is not focusable and has a <code>not-allowed</code> cursor. The track, the thumb and the texts use disabled tokens.')

access = '<h2 class="ds-h2">Accessibility</h2>' + desc('All requirements are listed under ' + sec_link(SLUG, 'accessibility-requirements', 'Accessibility Requirements') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Keyboard support</h3>' + desc('The arrow keys, Home, End, PageUp and PageDown are the native keyboard control. Tab shows the focus ring.') + \
    '<h3 class="ds-h3 ds-group">Screen reader support</h3>' + desc('The control is the native <code>&lt;input type="range"&gt;</code> with a visible label. The tick labels are <code>aria-hidden</code>; the value is read through <code>aria-valuetext</code>, so a step is announced by its name.')

related = '<h2 class="ds-h2">Related</h2><ul class="ds-bullets"><li><strong>' + link_large('segment-control.html', 'Pill segment control') + '</strong>. Two to four named views.</li><li><strong>' + link_large('radio.html', 'Radio button') + '</strong>. Two or three named options.</li><li><strong>' + link_large('switch.html', 'Switch') + '</strong>. On or off.</li><li><strong>' + link_large('input.html', 'Input') + '</strong>. An exact number.</li></ul>'

references = '<h2 class="ds-h2">References</h2>' + refs([
    ('https://www.w3.org/WAI/ARIA/apg/patterns/slider/', 'WAI-ARIA Authoring Practices: Slider', 'Keyboard and role requirements.'),
    ('https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html', 'WCAG 2.2: Target Size (Minimum)', 'Success criterion 2.5.8.'),
    ('https://fluent2.microsoft.design/components/web/react/core/slider/usage', 'Fluent 2: Slider', 'Microsoft.'),
    ('https://m3.material.io/components/sliders/overview', 'Material Design 3: Sliders', 'Google.'),
    ('https://carbondesignsystem.com/components/slider/usage/', 'Carbon Design System: Slider', 'IBM.')])

ex = [('playground', playground), ('overview', overview), ('usage', usage), ('anatomy', anatomy), ('variants', variants), ('sizes', sizes), ('layout', layout), ('behavior', behavior), ('accessibility', access), ('related', related), ('references', references)]

# ---------------------------------------------------------------- Specifications
st_tok = '<h2 class="ds-h2">Design Tokens</h2>' + desc('Resolved from the live token package.') + \
    '<div class="ds-table-wrap"><table class="ds-table" id="tok-table"><thead><tr><th scope="col">State</th><th scope="col">Part</th><th scope="col">Token</th><th scope="col">Value</th></tr></thead><tbody></tbody></table></div>' + \
    note('<strong>Open points:</strong> no Figma component. The sizes were decided in code. No dark-mode variant.')

st_sizes = '<h2 class="ds-h2">Sizes</h2>' + table(['Part', 'Value'], [['Hit area', '24px high input'], ['Track', '2px, <code>border-primary</code>'], ['Thumb', '16px circle, <code>surface-100</code>'], ['Hover halo', '4px, <code>surface-opacity-black-12</code>'], ['Label', '<code>label-sm</code>: 14/20, 0.28px, weight 600'], ['Value', '<code>body-sm</code>: 14/20, 0.36px'], ['Ticks', '12/16, 0.3px, <code>text-tertiary</code>']]) + \
    note('The same on every breakpoint. The 24px hit area is below the usual 44px touch target; raise the input height at xs and sm if design wants it.')

st_meas = '<h2 class="ds-h2">Measurements</h2><h3 class="ds-h3 ds-group">Dimensions</h3>' + table(['Attribute', 'Value'], [['Control height', 'Head row (20px line) + 4px + hit area 24px + 4px + ticks 16px'], ['Hit area', '24px, full width of the container'], ['Track', '2px high'], ['Thumb', '16px circle, centered on the track (7px above the track top)'], ['Halo', '4px around the thumb, on hover'], ['Focus ring', '2px line, 2px offset, around the input'], ['Corners', 'Round thumb, square track']]) + \
    note('A range has no padding of its own, so there is no measurement figure.') + \
    '<h3 class="ds-h3 ds-group">Spacing</h3>' + desc('The gaps between the parts as spacing tokens.') + table(['Part', 'Value'], [['Gap between head, input and ticks', '<code>space-4</code>'], ['Gap between label and value', '<code>space-8</code> minimum'], ['Halo, focus ring offset', '4px and 2px: literals']])

st_states = '<h2 class="ds-h2">States</h2>' + desc('Four states. Enabled and Disabled are shown. Hover and focus come from the browser: hover the thumb for the halo, press Tab for the ring.') + \
    '<div class="ds-table-wrap"><table class="ds-table pg-matrix" id="matrix"><thead><tr><th scope="col">State</th><th scope="col">Control</th><th scope="col">Look</th></tr></thead><tbody></tbody></table></div>'

st_typo = '<h2 class="ds-h2">Typography</h2>' + table(['Part', 'Type', 'Size / line height', 'Letter spacing', 'Weight'], [['Label', '<code>label-sm</code>', '14/20', '0.28px', '600'], ['Value', '<code>body-sm</code>', '14/20', '0.36px', 'Regular'], ['Ticks', '—', '12/16', '0.3px', 'Regular']]) + note('Breuer Condensed with <code>ss02</code>, <code>ss03</code> and <code>ss06</code>. The same on every breakpoint.')

st_struct = '<h2 class="ds-h2">Structure</h2><h3 class="ds-h3 ds-group">Elements</h3>' + table(['Element', 'Class', 'Notes'], [['Block', '<code>form-range</code> with <code>data-range</code>', 'Column of head, input and ticks. <code>[hidden]</code> hides it.'], ['Head', '<code>form-range__head</code>', 'Label on the left, value on the right.'], ['Label', '<code>form-range__label</code>', 'A <code>label</code> with <code>for</code>.'], ['Value', '<code>form-range__value</code>', 'An <code>output</code>.'], ['Input', '<code>form-range__input</code>', 'The native range input.'], ['Ticks', '<code>form-range__ticks</code>', 'Optional. Filled by <code>range.js</code>.']]) + \
    '<h3 class="ds-h3 ds-group">Types</h3>' + table(['Type', 'Attributes', 'Use'], [['Named steps', '<code>data-labels</code>, <code>data-ticks</code>, optional <code>data-recommended</code>', 'An ordered list of named values.'], ['Numeric', '<code>data-unit</code>', 'A number between a minimum and a maximum.']]) + \
    '<h3 class="ds-h3 ds-group">Attributes</h3>' + table(['Attribute on <code>[data-range]</code>', 'Meaning'], [['<code>data-labels="A|B|C"</code>', 'Value text per step, shown right of the label and set as <code>aria-valuetext</code>. Without it the number is shown (plus <code>data-unit</code>).'], ['<code>data-ticks="a|b|c"</code>', 'Tick labels under the track, one per step. Defaults to <code>data-labels</code>. Omit the <code>.form-range__ticks</code> div for none.'], ['<code>data-recommended="1"</code>', 'Step index of the recommended default. Its tick gets a <code>*</code>; explain the * near the control.'], ['<code>data-unit="px"</code>', 'Suffix for numeric ranges without <code>data-labels</code>.']]) + \
    '<h3 class="ds-h3 ds-group">Width</h3>' + desc('The range fills its container.')

st_motion = '<h2 class="ds-h2">Motion</h2>' + table(['Property', 'Duration', 'Easing'], [['<code>box-shadow</code> of the thumb (the halo), hover in and out', '<code>duration-fast-2</code>', '<code>ease-standard</code>']])

st_behavior = '<h2 class="ds-h2">Behavior</h2>' + table(['Input', 'Result'], [['Drag, click the track', 'Moves the thumb; the value text updates.'], ['Arrow keys, Home, End, PageUp, PageDown', 'Native keyboard control.'], ['Tab', 'Focus ring on keyboard focus only.'], ['Event', 'The normal <code>input</code> event on the <code>&lt;input&gt;</code>. For blocks added later: <code>ECO_RANGE.init(container)</code>.'], ['Hide', 'The <code>hidden</code> attribute on the <code>.form-range</code> block.']])

st_access = '<h2 class="ds-h2">Accessibility Requirements</h2>' + table(['Topic', 'Requirement'], [['Element', 'Always the native <code>&lt;input type="range"&gt;</code>, never a <code>div</code> imitation. Keyboard and screen readers then work for free.'], ['Label', 'A visible label linked with <code>for</code> and <code>id</code>.'], ['Value', 'Ticks are <code>aria-hidden</code>; the value is read through <code>aria-valuetext</code>.'], ['Focus', '2px ring <code>border-focus</code> on <code>:focus-visible</code> (WCAG 2.4.7, 1.4.11).'], ['Target size', 'The 24px hit area meets WCAG 2.5.8 (24px) but not the 44px recommendation.'], ['Disabled', 'Not focusable. Disabled tokens are exempt from contrast requirements.']])

spec = [('design-tokens', st_tok), ('sizes', st_sizes), ('measurements', st_meas), ('states', st_states), ('typography', st_typo), ('structure', st_struct), ('motion', st_motion), ('behavior', st_behavior), ('accessibility-requirements', st_access)]

# ---------------------------------------------------------------- Code
c_basic = '<h2 class="ds-h2">Basic Usage</h2>' + desc('Link the shared files once per page. Never copy the rules into a page, and never build a slider from <code>div</code>s.') + table(['Step', 'What to do'], [
    ['1. Link', '<code>&lt;link rel="stylesheet" href="/components/css/range.css"&gt;</code> and <code>&lt;script src="/components/js/range.js"&gt;&lt;/script&gt;</code> (from docs pages: <code>../../components/js/range.js</code>).'], ['2. Markup', 'A <code>div.form-range[data-range]</code> with a head (label and <code>output</code>), the <code>input.form-range__input</code> and, for tick labels, an empty <code>div.form-range__ticks</code>.'],
    ['3. Values', 'Named steps: <code>data-labels</code> and <code>data-ticks</code>. Numeric: <code>data-unit</code>.'], ['4. React', 'Listen for the <code>input</code> event on the input.']])
c_rg = '<h2 class="ds-h2">Range</h2><div id="recipes"></div>'
c_api = '<h2 class="ds-h2">API</h2><h3 class="ds-h3 ds-group">Attributes</h3>' + table(['Attribute on <code>[data-range]</code>', 'Meaning'], [['<code>data-labels="A|B|C"</code>', 'Value text per step. Also <code>aria-valuetext</code>.'], ['<code>data-ticks="a|b|c"</code>', 'Tick labels, one per step. Defaults to <code>data-labels</code>.'], ['<code>data-recommended="1"</code>', 'Step index of the recommended default. Its tick gets a <code>*</code>.'], ['<code>data-unit="px"</code>', 'Suffix for numeric ranges without <code>data-labels</code>.']]) + \
    '<h3 class="ds-h3 ds-group">Script</h3>' + table(['Name', 'Use'], [['<code>ECO_RANGE.init(container)</code>', 'Wires range blocks added after load.']]) + \
    '<h3 class="ds-h3 ds-group">Things to know</h3>' + bullets(['The CSS alone gives a styled native range; the script adds the value text, the tick labels and the recommended mark.', 'The input fires the normal <code>input</code> event. The value is the step index for named steps.', '<code>.form-range[hidden] { display: none }</code> is in the CSS, so the <code>hidden</code> attribute works.', 'The track and thumb pseudo-elements are the only place where the browser prefixes (<code>-webkit-</code>, <code>-moz-</code>) are needed.'])
c_css = '<h2 class="ds-h2">CSS / Tailwind</h2>' + desc('The component is one CSS file and one script, shared by every page. Link them, never copy them.') + code_box('css-code', 'CSS (components/css/range.css)') + '<div style="margin-top:16px">' + code_box('js-code', 'JS (components/js/range.js)') + '</div>'
code = [('basic-usage', c_basic), ('range', c_rg), ('api', c_api), ('css-tailwind', c_css, False)]

# ---------------------------------------------------------------- scripts
RG_JS = old_js('range', "  var rid = 0,", "  var st = { kind")

JS_EX = RG_JS + r'''
  var st = { kind: 'steps', rec: 'on', state: 'enabled' };
  function renderPg() {
    var o = { kind: st.kind, rec: st.rec === 'on', dis: st.state === 'disabled', label: $('#pg-label').value, min: 2, max: 10, val: 5 };
    var h = clear($('#pg-host')); h.style.cssText = 'width:100%;max-width:480px'; h.appendChild(rng(o)); $('#pg-code').textContent = mk(o);
  }
  DK.wire(st, renderPg); $('#pg-label').addEventListener('input', renderPg);
  clear($('#v-steps')).appendChild(rng({ kind: 'steps', rec: true, label: 'Duration' }));
  clear($('#v-num')).appendChild(rng({ kind: 'num', label: 'Auto-hide time', min: 2, max: 10, val: 5, unit: ' s' }));

  /* Usage figures */
  clear($('#fig-do')).appendChild(rng({ kind: 'num', label: 'Auto-hide time', min: 2, max: 10, val: 5, unit: ' s' }));
  var dont = clear($('#fig-dont')), d = document.createElement('div'); d.innerHTML = '<div class="form-range" data-range data-labels="Off|On" data-ticks="Off|On"><div class="form-range__head"><label class="form-range__label" for="rg-dont">Notifications</label><output class="form-range__value" for="rg-dont"></output></div><input class="form-range__input" id="rg-dont" type="range" min="0" max="1" step="1" value="1"><div class="form-range__ticks"></div></div>'; ECO_RANGE.init(d); dont.appendChild(d.firstChild);

  /* Anatomy */
  var ah = clear($('#a-host')); ah.appendChild(rng({ kind: 'steps', rec: true, label: 'Duration' }));
  function txt(el) { return function () { var r = document.createRange(); r.selectNodeContents(el); return r.getBoundingClientRect(); }; }
  var inp = $('.form-range__input', ah), thumbX = function () { var r = inp.getBoundingClientRect(), p = (inp.value - inp.min) / (inp.max - inp.min); return r.left + 8 + p * (r.width - 16); };
  DK.callouts($('#rg-anat'), [
    { n: 1, box: txt($('.form-range__label', ah)), side: 'top', len: 40 },
    { n: 2, box: txt($('.form-range__value', ah)), side: 'top', len: 40 },
    { n: 3, side: 'bottom', len: 72, box: function () { var r = inp.getBoundingClientRect(); return { left: r.left + r.width * 0.12, top: r.top + 11, width: 20, height: 2 }; } },
    { n: 4, side: 'top', len: 72, box: function () { var r = inp.getBoundingClientRect(); return { left: thumbX() - 8, top: r.top + 4, width: 16, height: 16 }; } },
    { n: 5, box: function () { var r = $('.form-range__ticks', ah).getBoundingClientRect(); return { left: r.left + r.width * 0.78, top: r.top, width: 24, height: r.height }; }, side: 'bottom', len: 44 }
  ]);
  renderPg();
'''

JS_SPEC = RG_JS + r'''
  var tb = $('#matrix tbody');
  [['Enabled', false, '2px track <code>border-primary</code>, 16px round thumb <code>surface-100</code>.'], ['Hover', null, '4px halo around the thumb, <code>surface-opacity-black-12</code>. Hover the thumb to see it.'], ['Focus (keyboard)', null, '2px <code>border-focus</code> ring with a 2px offset. Press Tab to see it.'], ['Disabled', true, 'Track <code>border-disabled</code>, thumb and text <code>text-disabled</code>, <code>not-allowed</code> cursor.']].forEach(function (r) {
    var tr = document.createElement('tr'), th = document.createElement('th'); th.scope = 'row'; th.textContent = r[0]; tr.appendChild(th);
    var td = document.createElement('td'); td.style.cssText = 'text-align:left;min-width:240px'; td.appendChild(rng({ kind: 'num', label: 'Value', min: 2, max: 10, val: 5, unit: ' s', dis: r[1] === true })); tr.appendChild(td);
    var d = document.createElement('td'); d.innerHTML = r[2]; tr.appendChild(d); tb.appendChild(tr);
  });
  DK.tokenTable($('#tok-table tbody'), [['Enabled', 'Track', 'border-primary'], ['Enabled', 'Thumb', 'surface-100'], ['Hover', 'Halo', 'surface-opacity-black-12'], ['Keyboard focus', 'Ring', 'border-focus'], ['Disabled', 'Track', 'border-disabled'], ['Disabled', 'Thumb and text', 'text-disabled'], ['All', 'Label', 'text-secondary'], ['All', 'Ticks', 'text-tertiary']]);
'''

JS_CODE = r'''
  DK.recipes($('#recipes'), [['Named steps (link range.css and range.js)', '<div class="form-range" data-range\n     data-labels="Fast 2 · 100 ms|Fast 3 · 150 ms|Fast 4 · 200 ms"\n     data-ticks="100|150|200" data-recommended="1">\n  <div class="form-range__head">\n    <label class="form-range__label" for="dur">Duration</label>\n    <output class="form-range__value" for="dur"></output>\n  </div>\n  <input class="form-range__input" id="dur" type="range" min="0" max="2" step="1" value="1">\n  <div class="form-range__ticks"></div>\n</div>'],
    ['Numeric with a unit', '<div class="form-range" data-range data-unit=" s">\n  <div class="form-range__head">\n    <label class="form-range__label" for="hide">Auto-hide time</label>\n    <output class="form-range__value" for="hide"></output>\n  </div>\n  <input class="form-range__input" id="hide" type="range" min="2" max="10" step="1" value="5">\n</div>'],
    ['React to a change', "document.getElementById('dur').addEventListener('input', function (e) {\n  console.log(e.target.value);   // the step index\n});"]]);
  DK.printCss($('#css-code'), 'range');
  fetch('../../components/js/range.js', { cache: 'no-cache' }).then(function (r) { return r.text(); }).then(function (t) { $('#js-code').textContent = t; });
'''

C = dict(
    slug=SLUG, title='Range', eyebrow='Components · Form', eyebrow_extra=BADGE,
    lead='A range lets the user pick <strong>one value from an ordered series</strong> by dragging a thumb, with the current value shown as text.',
    lead_ex='Every example on this page is the real component, not a picture. There is no Figma component: the range was designed in the repo.',
    lead_spec='Tokens, dimensions, states and requirements. There is no Figma component: values come from the live token package and the specification skill.',
    lead_code='How to add a range to a page. The files are <code>components/css/range.css</code> and <code>components/js/range.js</code>.',
    css=['range'], body_js=['../../components/js/range.js'], select_menu=False, style=STYLE, ex=ex, spec=spec, code=code, js_ex=JS_EX, js_spec=JS_SPEC, js_code=JS_CODE)

if __name__ == '__main__':
    emit(C)
