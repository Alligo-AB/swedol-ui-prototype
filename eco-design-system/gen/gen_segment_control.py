from build import *

FIGMA = 'https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=23144-268049'
SLUG = 'segment-control'
BADGE = '<span class="badge-basic badge-basic--warning badge-basic--weak" title="Built from the specification skill, not compared against the Figma design (linked in the intro).">Not verified with Figma</span>'

STYLE = r'''    .pg-row { display: flex; flex-wrap: wrap; align-items: center; gap: 16px 32px; }
    .pg-col { display: flex; flex-direction: column; align-items: flex-start; gap: 16px; }
    .pg-note { font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-tertiary); }
    .pg-matrix td { vertical-align: middle; padding-top: 16px; padding-bottom: 16px; }
    .pg-cap { font-size: 12px; line-height: 12px; letter-spacing: 0.48px; text-transform: uppercase; color: var(--color-text-tertiary); font-weight: 600; }
    .ds-stage--dark .pg-cap { color: var(--color-text-secondary-inverted); }
    .sg-fig { width: 100%; max-width: 320px; }
    .sg-measure { display: block; width: 280px; }   /* demo: a fixed width, so the control keeps its content width at every breakpoint */
    .sg-measure .pill-segment-control { width: auto; }
    .ds-callout__art { padding-right: 24px; }'''

playground = '<h2 class="ds-h2">Playground</h2>' + desc('Click a segment and the pill slides to it. Large is the page-level switcher; XSmall is for tight toolbars. Below 640px the control fills its parent; from 640px it shrinks to its content.') + \
    '<div class="ds-playground"><div class="ds-stage ds-stage--center" id="pg-stage"><div id="pg-host"></div></div><div class="ds-controls">' + \
    btn_group('pg-l-size', 'Size', 'data-pg="size"', [('lg', 'Large', False), ('md', 'Medium', True), ('sm', 'Small', False), ('xs', 'XSmall', False)]) + \
    btn_group('pg-l-n', 'Segments', 'data-pg="n"', [('2', '2', True), ('3', '3', False), ('4', '4', False)]) + \
    btn_group('pg-l-t', 'Pill', 'data-pg="thumb"', [('dark', 'Black', True), ('light', 'White', False)]) + \
    btn_group('pg-l-st', 'Track', 'data-pg="state"', [('enabled', 'Enabled', True), ('hover', 'Hover', False)]) + \
    '<p class="pg-note" style="margin:0">The animation is set in <a href="#motion" class="inline-link inline-link--small inline-link--tertiary">Motion</a>.</p></div></div><h3 class="ds-h3">Markup for this selection</h3>' + code_box('pg-code', 'HTML')

overview = '<h2 class="ds-h2">Overview</h2>' + desc('A pill segment control switches between two to four related views or filters in the same surface. A pill slides to the active segment.') + \
    desc('It has four sizes (Large, Medium, Small, XSmall), a black or a white pill, and a track that darkens on hover. It never replaces Tabs (navigation between pages) or Radio buttons (a choice that is submitted).') + \
    three_pages(SLUG, 'a pill segment control', 'the values: tokens, sizes, measurements, states and requirements', 'how to add one to a page')

usage = '<h2 class="ds-h2">Usage</h2><h3 class="ds-h3 ds-group">When to use</h3>' + desc('Use a pill segment control to switch between two related views or filters in the same surface, for example <em>User roles / Company plan</em> or <em>All features / Key features</em>. Use it to:') + \
    bullets(['Switch the view of one surface, at page level (Large) or in a drawer (Medium)', 'Filter a list or a table in a compact toolbar (Small, XSmall)']) + \
    '<h3 class="ds-h3 ds-group">When not to use</h3><h3 class="ds-h3">For more than four options</h3>' + desc('A segmented control is for two to four short, related options on one row. It never wraps onto a second row. For more options use <code>eco-select</code>, or <code>eco-radio</code> if all must stay visible.') + \
    fig_pair('<div class="sg-fig" id="fig-do"></div>', 'Do use two to four short options.', '<div class="sg-fig" id="fig-dont"></div>', 'Do not use it for more than four options.') + \
    '<h3 class="ds-h3">For navigation or a submitted choice</h3>' + desc('To move between pages or sections use <a class="inline-link inline-link--large inline-link--secondary" href="tabs.html">Tabs</a>. For a choice that is submitted use <code>eco-radio</code>. For a setting that turns on or off use <a class="inline-link inline-link--large inline-link--secondary" href="switch.html">Switch</a>.') + \
    '<h3 class="ds-h3">Keep labels short</h3>' + desc('The control shows all its segments on one row. Short labels keep it narrow; long labels make it wider than its container.') + \
    fig_pair('<div class="sg-fig" id="fig-lab-do"></div>', 'Do keep the labels short.', '<div class="sg-fig" id="fig-lab-dont"></div>', 'Do not use long labels: the control grows wider than its container.') + \
    '<h3 class="ds-h3 ds-group">Quick reference</h3>' + \
    table(['The user…', 'Use'], [['switches between 2–4 views or filters of the same content', 'Pill segment control'], ['switches between a few options in a toolbar, joined and framed', '<a class="inline-link inline-link--small" href="button-group.html">Button group</a>'], ['moves between pages or sections', '<a class="inline-link inline-link--small" href="tabs.html">Tabs</a>'], ['makes a choice that is submitted', '<code>eco-radio</code>'], ['turns one setting on or off', '<a class="inline-link inline-link--small" href="switch.html">Switch</a>']]) + \
    rules(['Use for two to four related views in one surface.', 'Choose the size by where it sits.', 'Listen for <code>segment-change</code> to swap the content.', 'Keep labels short.'], ['Replace tabs or radio buttons with it.', 'Add a second focus ring.', 'Let it wrap onto two rows.', 'Build your own thumb positioning: use the shared script.'])

anatomy = '<h2 class="ds-h2">Anatomy</h2><h3 class="ds-h3 ds-group">Pill segment control</h3>' + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout" id="sg-anat" role="img" aria-label="Anatomy of a pill segment control: 1 track, 2 pill, 3 active segment, 4 inactive segment"><div class="ds-callout__art"><div id="a-host"></div></div></div></figure></div>' + \
    ol_parts([('Track', 'The rounded frame. Its radius is half its height. It darkens on hover.'), ('Pill', 'The black (or white) shape behind the active segment. It is its own element and slides between the segments.'), ('Active segment', 'A button with <code>aria-pressed="true"</code>. White text on the black pill.'), ('Inactive segment', 'A transparent button with black text. It is underlined on hover.')])

variants = '<h2 class="ds-h2">Variants</h2>' + desc('The pill is black by default; use the white pill when the control already sits on a dark or grey surface. Sizes are under Sizes below.') + \
    '<h3 class="ds-h3 ds-group">White pill</h3>' + desc('For a control inside another, larger control, on a grey track. The active text stays black.') + fig_one('<div id="v-light"></div>', stage_attr=' style="background:var(--color-surface-15)"')

sizes = '<h2 class="ds-h2">Sizes</h2>' + desc('Four sizes, two to four segments. <strong>Large</strong> is the page-level view switcher, <strong>Medium</strong> a view switcher in a drawer, <strong>Small</strong> secondary filters and <strong>XSmall</strong> compact filters in a table toolbar. Measurements are under ' + sec_link(SLUG, 'sizes', 'Sizes') + ' in Specifications.') + \
    fig_one('<div class="pg-col" id="v-sizes" style="width:100%"></div>')

layout = '<h2 class="ds-h2">Layout &amp; Appearance</h2><h3 class="ds-h3 ds-group">Width</h3>' + desc('Below 640px the control is fluid: it fills its parent and the segments share the space evenly. From 640px it shrinks to its content. Height, padding and text do not change until 769px, so 640–768px still has the mobile size.') + \
    '<h3 class="ds-h3 ds-group">Appearance</h3>' + desc('A grey track with a black pill and uppercase labels. The pill has a small shadow. Token names and values are under ' + sec_link(SLUG, 'design-tokens', 'Design Tokens') + ' in Specifications.')

behavior = '<h2 class="ds-h2">Behavior</h2><h3 class="ds-h3 ds-group">Switching</h3>' + desc('A click on a segment moves the pill to it, sets <code>aria-pressed</code> and fires a bubbling <code>segment-change</code> event with <code>detail.button</code>. Your page listens for the event and swaps the content.') + \
    '<h3 class="ds-h3 ds-group">Hover and focus</h3>' + desc('Hover darkens the track to <code>border-tertiary</code> and underlines the <strong>inactive</strong> segment. Focus has no style of its own: the buttons use the global keyboard focus ring. All states are listed under ' + sec_link(SLUG, 'states', 'States') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Motion</h3>' + desc('The pill slides with <code>duration-medium-2</code> and <code>ease-standard</code>. Try other values under <a class="inline-link inline-link--large inline-link--secondary" href="#motion">Motion</a> above.')

access = '<h2 class="ds-h2">Accessibility</h2>' + desc('All requirements are listed under ' + sec_link(SLUG, 'accessibility-requirements', 'Accessibility Requirements') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Keyboard support</h3>' + desc('Tab moves between the segments. Enter or Space chooses the focused one. The focus ring shows on keyboard focus only.') + \
    '<h3 class="ds-h3 ds-group">Screen reader support</h3>' + desc('The control is a <code>role="group"</code> with an <code>aria-label</code>. Each segment is a button with <code>aria-pressed</code>, so the active one is announced as pressed.')

related = '<h2 class="ds-h2">Related</h2><ul class="ds-bullets"><li><strong>' + link_large('tabs.html', 'Tabs') + '</strong>. Navigation between pages or sections.</li><li><strong>' + link_large('button-group.html', 'Button group') + '</strong>. Joined and framed options in a toolbar.</li><li><strong>' + link_large('radio.html', 'Radio button') + '</strong>. A choice that is submitted.</li><li><strong>' + link_large('switch.html', 'Switch') + '</strong>. One setting on or off.</li></ul>'

references = '<h2 class="ds-h2">References</h2>' + refs([
    ('https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html', 'WCAG 2.2: Non-text Contrast', 'Success criterion 1.4.11.'),
    ('https://www.nngroup.com/articles/toggle-switch-guidelines/', 'Nielsen Norman Group: Toggle-Switch Guidelines', 'Related guidance on switches and toggles.'),
    ('https://m3.material.io/components/segmented-buttons/overview', 'Material Design 3: Segmented buttons', 'Google.'),
    ('https://carbondesignsystem.com/components/content-switcher/usage/', 'Carbon Design System: Content switcher', 'IBM.')])

ex = [('playground', playground), ('overview', overview), ('usage', usage), ('anatomy', anatomy), ('variants', variants), ('sizes', sizes), ('layout', layout), ('behavior', behavior), ('accessibility', access), ('related', related), ('references', references)]

# ---------------------------------------------------------------- Specifications
st_tok = '<h2 class="ds-h2">Design Tokens</h2>' + desc('Resolved from the live token package.') + \
    '<div class="ds-table-wrap"><table class="ds-table" id="tok-table"><thead><tr><th scope="col">State</th><th scope="col">Part</th><th scope="col">Token</th><th scope="col">Value</th></tr></thead><tbody></tbody></table></div>' + \
    note('<strong>Open points:</strong> the Primary Inverted variant (for black surfaces) and the Square shape are in the Figma spec but not specified or built. The Disabled state must be pulled from Figma (<code>State=Disabled</code>) before it is built. The component is not yet compared against the Figma design.')

st_sizes = '<h2 class="ds-h2">Sizes</h2>' + table(['Size', 'Desktop (769px+)', 'Mobile and tablet', 'Used for'], [
    ['Large', '56px · padding 5px · radius 28px · pill padding 24px · 18/18, 0.18px', '48px · 4px · 24px · 20px · 16/16, 0.32px', 'Page-level view switcher'], ['Medium', '48px · 4px · 24px · 20px · 18/18, 0.18px', '40px · 4px · 20px · 16px · 16/16, 0.32px', 'View switcher in a drawer'],
    ['Small', '40px · 4px · 20px · 16px · 16/16, 0.48px', '32px · 3px · 16px · 12px · 14/14, 0.42px', 'Secondary filters'], ['XSmall', '32px · 3px · 16px · 12px · 14/14, 0.56px', '32px · 3px · 16px · 10px · 12/12, 0.48px', 'Compact filters in a table toolbar']]) + \
    note('Columns: height · track padding · track radius · pill padding · text. The track radius is always half the height; the pill radius is the track radius minus the track padding. sm (640–768px) still has the mobile size.')


def mfig(n, name, cls):
    return ('<div class="measure__item"><span class="measure__name">%d · %s</span><div class="measure__obj"><span class="sg-measure"><div class="pill-segment-control%s measure__subject" role="group" aria-label="%s"><span class="pill-segment-control__thumb" aria-hidden="true" style="width:0"></span><button type="button" class="pill-segment-control__btn pill-segment-control__btn--active" tabindex="-1">User roles</button><button type="button" class="pill-segment-control__btn" tabindex="-1">Company plan</button></div></span>'
            '<i class="measure__pad measure__pad--t"></i><i class="measure__pad measure__pad--b"></i><i class="measure__pad measure__pad--l"></i><i class="measure__pad measure__pad--r"></i>'
            '<b class="measure__dim measure__dim--v measure__dim--t"><span></span></b><b class="measure__dim measure__dim--v measure__dim--b"><span></span></b><b class="measure__dim measure__dim--h measure__dim--l"><span></span></b><b class="measure__dim measure__dim--h measure__dim--r"><span></span></b></div></div>') % (n, name, cls, name)


st_meas = '<h2 class="ds-h2">Measurements</h2><h3 class="ds-h3 ds-group">Dimensions</h3>' + desc('Padding of the track at each size: the space between the track and the pill. The numbers are read from the component.') + \
    toolbar([('mb-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force')]) + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-fig__stage--flush" style="padding:0;min-height:0"><div class="measure" role="img" aria-label="Padding of the track: per size">' + mfig(1, 'Large', '') + mfig(2, 'Medium', ' pill-segment-control--md') + mfig(3, 'Small', ' pill-segment-control--sm') + mfig(4, 'XSmall', ' pill-segment-control--xs') + '</div></div><figcaption class="ds-fig__cap">The track at true size (1:1). Change the Breakpoint to see the mobile values.</figcaption></figure></div>' + \
    table(['Attribute', 'Large', 'Medium', 'Small', 'XSmall'], [['Height, Desktop', '56px', '48px', '40px', '32px'], ['Height, Mobile', '48px', '40px', '32px', '32px'], ['Track padding, Desktop', '5px', '4px', '4px', '3px'], ['Track padding, Mobile', '4px', '4px', '3px', '3px'], ['Pill padding (left, right), Desktop', '24px', '20px', '16px', '12px'], ['Pill padding (left, right), Mobile', '20px', '16px', '12px', '10px'],
                                                                    ['Track radius', '<td colspan="4">Half the height</td>'], ['Pill radius', '<td colspan="4">Track radius minus the track padding</td>']]) + \
    '<h3 class="ds-h3 ds-group">Spacing</h3>' + desc('The spacing values as tokens.') + table(['Part', 'Value'], [['Track padding 4px', '<code>space-4</code>'], ['Track padding 3px and 5px', 'Literals: no spacing token for 3px and 5px'], ['Pill padding 12px, 16px, 20px, 24px', '<code>space-12</code>, <code>space-16</code>, <code>space-20</code> (literal), <code>space-24</code>; 10px is a literal']]) + \
    note('The segment padding is set in the CSS in pixels. <strong>Open point:</strong> bind 3px, 5px, 10px and 20px to tokens or add them to the spacing scale.')

st_states = '<h2 class="ds-h2">States</h2>' + desc('Hover darkens the track to <code>border-tertiary</code> and underlines the <strong>inactive</strong> segment. Focus has no style of its own: the buttons use the global keyboard focus ring. Hover is forced on this page.') + \
    '<div class="ds-table-wrap"><table class="ds-table pg-matrix" id="matrix"><thead><tr><th scope="col">State</th><th scope="col">Control</th><th scope="col">Rule</th></tr></thead><tbody></tbody></table></div>'

st_typo = '<h2 class="ds-h2">Typography</h2>' + table(['Size', 'Type', 'Desktop (769px+)', 'Mobile and tablet'], [['Large', '<code>label-lg</code>', '18/18, 0.18px', '16/16, 0.32px'], ['Medium', '<code>label-lg</code>', '18/18, 0.18px', '16/16, 0.32px'], ['Small', '<code>label-md</code>', '16/16, 0.48px', '14/14, 0.42px'], ['XSmall', '<code>label-sm</code>', '14/14, 0.56px', '12/12, 0.48px']]) + \
    note('Breuer Condensed, weight 600, uppercase, with <code>ss02</code> and <code>ss03</code>.')

st_struct = '<h2 class="ds-h2">Structure</h2><h3 class="ds-h3 ds-group">Elements</h3>' + table(['Element', 'Class', 'Notes'], [
    ['Track', '<code>pill-segment-control</code>, <code>--md</code>, <code>--sm</code>, <code>--xs</code>', '<code>role="group"</code> with an <code>aria-label</code>. Large is the default.'], ['Pill', '<code>pill-segment-control__thumb</code>, <code>--light</code>', 'A separate element. <code>pill-segment-control.js</code> sets its width and <code>translateX</code>.'], ['Segment', '<code>pill-segment-control__btn</code>, <code>--active</code>', 'A <code>button</code> with <code>aria-pressed</code>.']]) + \
    '<h3 class="ds-h3 ds-group">Types</h3>' + table(['Type', 'Class', 'Use'], [['Black pill', 'Default', 'On light surfaces.'], ['White pill', '<code>pill-segment-control__thumb--light</code>', 'When the control already sits on a dark or grey surface.'], ['Primary Inverted', '—', 'In Figma, not built.'], ['Square shape', '—', 'In Figma, not built.']]) + \
    '<h3 class="ds-h3 ds-group">Width</h3>' + desc('Fluid (<code>width: 100%</code>) only below 640px, where the segments share the space evenly. From 640px it shrinks to its content (<code>width: auto</code>, <code>align-self: flex-start</code>). Count: two to four short options on one row.')

st_motion = '<h2 class="ds-h2">Motion</h2>' + table(['Property', 'Duration', 'Easing'], [['Pill: <code>transform</code> and <code>width</code>', '<code>duration-medium-2</code> (300ms), set through <code>--sg-duration</code>', '<code>ease-standard</code>, set through <code>--sg-ease</code>'], ['Track <code>background-color</code> on hover', '<code>duration-fast-3</code>', '<code>ease-standard</code>'], ['Segment text <code>color</code>', '<code>duration-fast-3</code>', '<code>ease-standard</code>']]) + \
    note('The pill travels a visible distance, so it is slower than a hover. Compare other easing and duration values in the live Motion section on <a class="inline-link inline-link--medium inline-link--secondary" href="segment-control.html#motion">Examples &amp; Guidelines</a>.')

st_behavior = '<h2 class="ds-h2">Behavior</h2>' + table(['Topic', 'Rule'], [
    ['Sliding pill', 'The pill is its own <code>.pill-segment-control__thumb</code>. <code>pill-segment-control.js</code> sets its width and <code>translateX</code> from the active button’s <code>offsetWidth</code> and <code>offsetLeft</code>, because the buttons can have different widths. It re-measures on resize and load.'], ['Event', 'A bubbling <code>segment-change</code> event with <code>detail.button</code>.'],
    ['Count', '2–4 short options on one row. More: <code>eco-select</code> or <code>eco-radio</code>.'], ['Disabled', 'Not specified. Pull <code>State=Disabled</code> from Figma before building it.']])

st_access = '<h2 class="ds-h2">Accessibility Requirements</h2>' + table(['Topic', 'Requirement'], [
    ['Markup', '<code>role="group"</code> with an <code>aria-label</code>; the buttons carry <code>aria-pressed</code>.'], ['Focus', 'No own style: the buttons use the global focus ring on keyboard focus (<code>border-focus</code>). Never add a second ring (WCAG 2.4.7).'], ['Color', 'The active segment is also shown by the pill, not by color alone.'], ['Motion', 'Reduced motion: the pill slide should be turned off. <strong>Open point:</strong> the CSS does not yet have a <code>prefers-reduced-motion</code> rule.']])

spec = [('design-tokens', st_tok), ('sizes', st_sizes), ('measurements', st_meas), ('states', st_states), ('typography', st_typo), ('structure', st_struct), ('motion', st_motion), ('behavior', st_behavior), ('accessibility-requirements', st_access)]

# ---------------------------------------------------------------- Code
c_basic = '<h2 class="ds-h2">Basic Usage</h2>' + desc('Link the shared files once per page. Never copy the rules into a page, and never position the pill yourself.') + table(['Step', 'What to do'], [
    ['1. Link', '<code>&lt;link rel="stylesheet" href="/components/css/pill-segment-control.css"&gt;</code> and <code>&lt;script src="/components/js/pill-segment-control.js"&gt;&lt;/script&gt;</code>. Both templates already have them.'], ['2. Markup', 'A <code>div.pill-segment-control[role="group"]</code> with an <code>aria-label</code>, a <code>span.pill-segment-control__thumb</code> and two to four <code>button.pill-segment-control__btn</code>.'],
    ['3. Active segment', '<code>pill-segment-control__btn--active</code> and <code>aria-pressed="true"</code> on one button.'], ['4. React', 'Listen for the <code>segment-change</code> event and swap the content.'], ['5. Size', 'Large is the default. Add <code>pill-segment-control--md</code>, <code>--sm</code> or <code>--xs</code>.']])
c_sg = '<h2 class="ds-h2">Pill segment control</h2><div id="recipes"></div>' + note('The markup has no motion. The pill’s slide is set in <a class="inline-link inline-link--medium inline-link--secondary" href="segment-control.html#motion">Motion</a> on Examples &amp; Guidelines.')
c_api = '<h2 class="ds-h2">API</h2><h3 class="ds-h3 ds-group">Classes</h3>' + table(['Class', 'Use'], [['<code>pill-segment-control</code>', 'The track. Large.'], ['<code>pill-segment-control--md</code>, <code>--sm</code>, <code>--xs</code>', 'Medium, Small, XSmall.'], ['<code>pill-segment-control__thumb</code>, <code>--light</code>', 'The pill. <code>--light</code> is the white pill.'], ['<code>pill-segment-control__btn</code>, <code>--active</code>', 'A segment.']]) + \
    '<h3 class="ds-h3 ds-group">Events and custom properties</h3>' + table(['Name', 'Use'], [['<code>segment-change</code>', 'Bubbling event on the button’s ancestors. <code>e.detail.button</code> is the segment that was clicked.'], ['<code>--sg-duration</code>, <code>--sg-ease</code>', 'Duration and easing of the pill. Defaults: <code>duration-medium-2</code> and <code>ease-standard</code>.'], ['<code>ECO_SEGMENT.init(root)</code>', 'Wires controls added later.']]) + \
    '<h3 class="ds-h3 ds-group">Things to know</h3>' + bullets(['The script measures the active button, so the pill follows buttons of different widths.', 'Below 640px the control is fluid; from 640px it shrinks to its content. If the parent is a flex column with <code>align-items: stretch</code>, <code>align-self: flex-start</code> is needed (it is in the CSS).', 'Hover is forced on the documentation pages with <code>data-state="hover"</code>; it does nothing elsewhere.'])
c_css = '<h2 class="ds-h2">CSS / Tailwind</h2>' + desc('The component is one CSS file and one script, shared by every page. Link them, never copy them.') + code_box('css-code', 'CSS (components/css/pill-segment-control.css)') + '<div style="margin-top:16px">' + code_box('js-code', 'JS (components/js/pill-segment-control.js)') + '</div>'
code = [('basic-usage', c_basic), ('pill-segment-control', c_sg), ('api', c_api), ('css-tailwind', c_css, False)]

# ---------------------------------------------------------------- scripts
SG_JS = old_js('segment-control', "  var NAMES =", "  function renderPg() {")

JS_EX = SG_JS + r'''
  function renderPg() {
    var o = { size: st.size, n: +st.n, thumb: st.thumb, hover: st.state === 'hover' };
    $('#pg-stage').style.background = o.thumb === 'light' ? 'var(--color-surface-15)' : '';
    mount(clear($('#pg-host')), o); $('#pg-code').textContent = markup(o);
  }
  DK.wire(st, renderPg);
  var vs = clear($('#v-sizes')); [['lg', 'Large'], ['md', 'Medium'], ['sm', 'Small'], ['xs', 'XSmall']].forEach(function (z) { var d = document.createElement('div'); d.className = 'pg-col'; d.style.gap = '8px'; var cap = document.createElement('span'); cap.className = 'pg-cap'; cap.textContent = z[1]; d.appendChild(cap); mount(d, { size: z[0], n: 2 }); vs.appendChild(d); });
  mount(clear($('#v-light')), { size: 'md', n: 3, thumb: 'light' });

  /* Usage figures */
  mount(clear($('#fig-do')), { size: 'sm', n: 2 });
  var many = clear($('#fig-dont')), c5 = ctl({ size: 'xs', n: 4 }); many.appendChild(c5);
  var extra = document.createElement('button'); extra.type = 'button'; extra.className = 'pill-segment-control__btn'; extra.setAttribute('aria-pressed', 'false'); extra.textContent = 'Other'; c5.appendChild(extra); ECO_SEGMENT.init(many);
  many.style.overflow = 'hidden';

  mount(clear($('#fig-lab-do')), { size: 'sm', n: 2 });
  var ll = clear($('#fig-lab-dont')); ll.style.overflow = 'hidden'; mount(ll, { size: 'sm', n: 2 });
  $$('.pill-segment-control__btn', ll).forEach(function (b, i) { b.textContent = ['All features and services', 'Only the features that are included'][i]; }); ECO_SEGMENT.init(ll);

  /* Anatomy */
  var ah = clear($('#a-host')), ac = mount(ah, { size: 'lg', n: 2 }), abtn = $$('.pill-segment-control__btn', ac);
  DK.callouts($('#sg-anat'), [
    { n: 1, el: ac, side: 'top', len: 44, at: 'edge' },
    { n: 2, el: $('.pill-segment-control__thumb', ac), side: 'bottom', len: 44 },
    { n: 3, box: function () { var r = abtn[0].getBoundingClientRect(); return { left: r.left, top: r.top, width: r.width, height: r.height }; }, side: 'top', len: 76 },
    { n: 4, el: abtn[1], side: 'bottom', len: 76 }
  ]);
  renderPg();

  /* Motion (live easing and duration) */
  DK.motion({ anchor: 'playground', prefix: 'sg', collapse: false, always: true, rec: { ease: 'standard', dur: 'medium-2' }, why: 'The pill travels a visible distance between segments: standard easing (calm start, fast middle, calm finish) and 300 ms, slower than a hover (eco-pill-segment-control). The preview moves the pill by itself; click a segment to move it again.',
    preview: function () { var h = document.createElement('div'); h.style.cssText = 'display:flex;justify-content:center'; mount(h, { size: 'md', n: 3 }); setTimeout(function () { var b = $$('.pill-segment-control__btn', h); b[(b.indexOf($('.pill-segment-control__btn--active', h)) + 1) % b.length].click(); }, 80); return h; } });
  /* the split pages are all white with a divider between sections: DK.motion alternates backgrounds, so undo that */
  $$('.ds-doc > section.ds-section').forEach(function (s) { s.classList.remove('ds-section--secondary'); });
  $('#motion').insertAdjacentHTML('beforebegin', '<div class="ds-sep"><hr class="divider" /></div>');
'''

JS_SPEC = SG_JS + r'''
  var tb = $('#matrix tbody');
  [['Enabled', { }, 'Track <code>surface-disabled</code>. Active: black pill, white text. Inactive: black text.'], ['Hover', { hover: true }, 'Track <code>border-tertiary</code>. The inactive segment is underlined; the active one does not change.'], ['Focus', { }, 'No own style. The buttons use the global ring on keyboard focus (<code>border-focus</code>).'], ['Disabled', null, '']].forEach(function (r) {
    var tr = document.createElement('tr'), th = document.createElement('th'); th.scope = 'row'; th.textContent = r[0]; tr.appendChild(th);
    var td = document.createElement('td'); td.style.textAlign = 'left'; if (r[1]) { var h = document.createElement('div'); td.appendChild(h); mount(h, { size: 'sm', n: 2, hover: r[1].hover }); } else td.innerHTML = '<span class="ds-na">Not defined</span>';
    var d = document.createElement('td'); d.innerHTML = r[2] || 'Not specified in the skill. Pull <code>State=Disabled</code> from Figma before building it.';
    tr.appendChild(td); tr.appendChild(d); tb.appendChild(tr);
  });
  DK.tokenTable($('#tok-table tbody'), [['Enabled', 'Track', 'surface-disabled'], ['Hover', 'Track', 'border-tertiary'], ['All', 'Pill (black)', 'surface-100'], ['All', 'Pill (white)', 'surface-raised-primary'], ['Active', 'Text (black pill)', 'text-action-primary-inverted'], ['Inactive', 'Text', 'text-action-primary'], ['Keyboard focus', 'Ring', 'border-focus']]);
  DK.bp(function () { if (window.ECO_MEASURE) ECO_MEASURE.init(); });
'''

JS_CODE = SG_JS + r'''
  DK.recipes($('#recipes'), [
    ['Medium, two segments (link the CSS and the JS)', '<div class="pill-segment-control pill-segment-control--md" role="group" aria-label="Select view">\n  <span class="pill-segment-control__thumb" aria-hidden="true"></span>\n  <button type="button" class="pill-segment-control__btn pill-segment-control__btn--active" aria-pressed="true">User roles</button>\n  <button type="button" class="pill-segment-control__btn" aria-pressed="false">Company plan</button>\n</div>'],
    ['React to a change', "document.addEventListener('segment-change', function (e) {\n  var button = e.detail.button;   // the segment that was clicked\n  // show or hide the matching view\n});"]]);
  DK.printCss($('#css-code'), 'pill-segment-control');
  fetch('../../components/js/pill-segment-control.js', { cache: 'no-cache' }).then(function (r) { return r.text(); }).then(function (t) { $('#js-code').textContent = t; });
'''

C = dict(
    slug=SLUG, title='Pill segment control', eyebrow='Components · Form', eyebrow_extra=BADGE,
    lead='A pill segment control switches between <strong>two to four related views or filters</strong> in the same surface. A pill slides to the active segment.',
    lead_ex='Every example on this page is the real component, not a picture. Specification: <code>.claude/skills/eco-pill-segment-control/SKILL.md</code>. Figma: ' + fig_link(FIGMA, 'Pill segment control') + '.',
    lead_spec='Tokens, sizes, measurements, states and requirements. Values come from the live token package and from the specification skill: ' + fig_link(FIGMA, 'Pill segment control') + '.',
    lead_code='How to add a pill segment control to a page. The files are <code>components/css/pill-segment-control.css</code> and <code>components/js/pill-segment-control.js</code>.',
    css=['pill-segment-control', 'range'], body_js=['../../components/js/pill-segment-control.js', '../../components/js/range.js'], select_menu=False, style=STYLE, ex=ex, spec=spec, code=code, js_ex=JS_EX, js_spec=JS_SPEC, js_code=JS_CODE)
C['body_js_spec'] = None

if __name__ == '__main__':
    emit(C)
