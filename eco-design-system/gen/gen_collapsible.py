from build import *

SLUG = 'collapsible'
FIGMA = 'https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=%s'

STYLE = r'''    .pg-note { font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-tertiary); }
    .pg-grid { display: grid; gap: 32px 24px; grid-template-columns: minmax(0, 1fr); width: 100%; }
    @media (min-width: 769px) { .pg-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
    .pg-cap { display: block; margin-bottom: 12px; font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-tertiary); }
    .pg-matrix td { vertical-align: top; padding-top: 16px; padding-bottom: 16px; min-width: 300px; }
    .pg-matrix td.co-dark { background: var(--color-surface-100); }
    .co-fig { width: 100%; }
    .ds-doc .co-lines .collapsible-wrap:last-child:not(.collapsible-wrap--boxed):not(.collapsible-wrap--no-divider-bottom) { border-bottom: 1px solid var(--color-border-primary); }   /* demo: collapsible.css hides the last line when a list ends the page section; a docs section always does, so the demos keep it */
    .ds-doc .co-lines .collapsible-wrap.collapsible-wrap--dark:last-child:not(.collapsible-wrap--boxed):not(.collapsible-wrap--no-divider-bottom) { border-bottom-color: var(--color-border-dark); }
    .ds-doc .co-lines .collapsible-wrap.collapsible-wrap--disabled:last-child:not(.collapsible-wrap--boxed):not(.collapsible-wrap--no-divider-bottom) { border-bottom-color: var(--color-border-primary); }
    .co-measure { display: block; width: 280px; }   /* demo: a fixed width, so the strips have a row to sit on */
    .co-callout.ds-fig__stage.ds-callout { padding-right: 112px; }
    .co-callout .ds-callout__art { width: 100%; max-width: 560px; }
    .co-anat .collapsible-wrap, .co-anat .collapsible-item__content, .co-anat .collapsible-item__chevron .ms { transition: none; }   /* demo: the markers are drawn on the finished size */
    .co-narrow { width: 100%; max-width: 360px; }
    .sb-stage.ds-fig__stage { display: block; padding: 0; min-height: 0; background: var(--color-surface-raised-primary); }   /* a Storyblok screenshot with numbered markers on top */
    .sb-shot { position: relative; }
    .sb-shot img { display: block; width: 100%; height: auto; }
    .sb-pin { position: absolute; transform: translate(-50%, -50%); pointer-events: none; }
    .sb-pin--red { background: var(--color-surface-danger-default); }
    .sb-box { position: absolute; border: 3px solid var(--color-border-danger-default); pointer-events: none; }
    .sb-tip { display: flex; background: var(--color-surface-raised-primary); box-shadow: var(--shadow-elevation-b-20); }
    .sb-tip__ic { display: grid; place-items: center; flex: 0 0 96px; background: var(--color-surface-100); color: var(--color-accent-default); }
    .sb-tip__ic .mo-ic { font-size: 48px; }
    .sb-tip__body { padding: var(--dimension-spacing-space-16) var(--dimension-spacing-space-24); }
    .sb-tip__body .ds-h3 { margin: 0 0 var(--dimension-spacing-space-4); }
    .sb-tip__body p { margin: 0; }
    .sec-fig { --px-full: var(--dimension-spacing-space-24); width: 100%; }   /* demo: a fixed side margin, so a section fits a figure */
    .sec-in { padding: var(--dimension-spacing-space-24) 0; }
    .sec-ph { padding: var(--dimension-spacing-space-16); background: var(--color-surface-10); font-size: 14px; line-height: 20px; letter-spacing: 0.36px; }
    .sec-in > .ds-h3 { margin: 0 0 var(--dimension-spacing-space-8); }'''

# ---- the builder shared by the three pages: one markup function for playground, variants, matrix and code
CO_JS = r'''
  var BODY = '<p>It depends on the scope and which features you need. Contact your local sales representative and we will work out a solution that fits your business and your budget together.</p>';
  var uid = 0;
  function markup(o) {
    var id = 'co-' + (++uid), small = o.size === 'small', sw = o.sw, open = !!o.open;
    var cls = 'collapsible-wrap' + (small ? ' collapsible-wrap--small' : '') + (o.boxed ? ' collapsible-wrap--boxed' : '') + (o.filled ? ' collapsible-wrap--filled' : '') + (o.topLine && !o.boxed ? ' collapsible-wrap--divider-top' : '') + (o.noBottomLine && !o.boxed ? ' collapsible-wrap--no-divider-bottom' : '') + (o.bottomLine && !o.boxed ? ' collapsible-wrap--divider-bottom' : '') + (o.dark ? ' collapsible-wrap--dark' : '') + (o.disabled ? ' collapsible-wrap--disabled' : '') + (open ? ' collapsible-wrap--open' : '');
    var tag = sw ? 'div' : 'button', attr = (sw ? '' : ' type="button" aria-expanded="' + open + '" aria-controls="' + id + '"' + (o.disabled ? ' disabled' : '')) + (o.hover ? ' data-state="hover"' : '');
    var left = '';
    if (o.icon) left += '<span class="ms" aria-hidden="true">' + o.icon + '</span>\n';
    if (o.info || o.helper) {
      left += '<span class="collapsible-item__text">\n  <span class="collapsible-item__line">\n    <span class="collapsible-item__label">' + esc(o.title) + (o.info ? ':' : '') + '</span>\n' + (o.info ? '    <span class="collapsible-item__info">' + esc(o.info) + '</span>\n' : '') + '  </span>\n' + (o.helper ? '  <span class="collapsible-item__helper">' + esc(o.helper) + '</span>\n' : '') + '</span>\n';
    } else left += '<span class="collapsible-item__label">' + esc(o.title) + '</span>\n';
    if (o.iconEnd) left += '<span class="ms" aria-hidden="true">' + o.iconEnd + '</span>\n';
    var end = '';
    if (sw) end += '<label class="form-switch-item' + (small ? ' form-switch-item--xs' : '') + (o.dark ? ' form-switch-item--dark' : '') + '"><input type="checkbox" role="switch" aria-label="' + esc(o.title) + '"' + (o.disabled ? ' disabled' : '') + ' /></label>\n';
    if (o.badge) end += '<span class="badge-number ' + (small ? 'badge-number--sm' : 'badge-number--md') + '">1</span>\n';
    if (o.chevron !== false) end += '<span class="collapsible-item__chevron"><span class="ms" aria-hidden="true">expand_more</span></span>\n';
    function ind(s, n) { var p = new Array(n + 1).join(' '); return s.replace(/\n$/, '').split('\n').map(function (l) { return p + l; }).join('\n') + '\n'; }
    var body = o.body === undefined ? BODY : o.body;
    return '<div class="' + cls + '">\n  <' + tag + ' class="collapsible-item" onclick="toggleCollapsible(this)"' + attr + '>\n    <span class="collapsible-item__left">\n' + ind(left, 6) + '    </span>\n' + (end ? '    <span class="collapsible-item__end">\n' + ind(end, 6) + '    </span>\n' : '') + '  </' + tag + '>\n  <div class="collapsible-item__content" id="' + id + '">' + (o.boxed ? '<div class="collapsible-item__body">' + body + '</div>' : body) + '</div>\n</div>';
  }
  function printable(o) { return markup(o).replace(/ data-state="hover"/, '').replace(/co-\d+/g, 'faq-1'); }
  function row(o) {
    o.host.insertAdjacentHTML('beforeend', markup(o));
    var w = o.host.lastElementChild;
    if (o.open) { var c = w.querySelector('.collapsible-item__content'); c.style.maxHeight = c.scrollHeight + 'px'; }
    return w;
  }
  function refit() { $$('.collapsible-wrap--open .collapsible-item__content').forEach(function (c) { c.style.maxHeight = c.scrollHeight + 'px'; }); }   /* docs only: the real component sets max-height once, when the row opens */
  window.addEventListener('resize', refit);
'''

playground = '<h2 class="ds-h2">Playground</h2>' + desc('One row. Click the header to open and close it. Choose the size, the theme, the state and the parts of the header and the row and its code update.') + \
    '<div class="ds-playground"><div class="ds-stage" id="pg-stage"><div id="pg-host" class="co-lines" style="width:100%"></div></div><div class="ds-controls">' + \
    bp_field('pg-l-bp') + btn_group('pg-l-size', 'Size', 'data-pg="size"', [('large', 'Large', True), ('small', 'Small', False)]) + \
    btn_group('pg-l-box', 'Boxed', 'data-pg="boxed"', [('no', 'No', True), ('yes', 'Yes', False)]) + \
    btn_group('pg-l-fill', 'Header background', 'data-pg="fill"', [('no', 'None', True), ('yes', 'Grey', False)]) + \
    btn_group('pg-l-top', 'Top divider', 'data-pg="top"', [('off', 'Off', True), ('on', 'On', False)]) + \
    btn_group('pg-l-bot', 'Bottom divider', 'data-pg="bottom"', [('on', 'On', True), ('off', 'Off', False)]) + \
    btn_group('pg-l-theme', 'Theme', 'data-pg="theme"', [('light', 'Light', True), ('dark', 'Dark', False)]) + \
    btn_group('pg-l-state', 'State', 'data-pg="state"', [('enabled', 'Enabled', True), ('hover', 'Hover', False), ('disabled', 'Disabled', False)]) + \
    btn_group('pg-l-open', 'Row', 'data-pg="open"', [('closed', 'Closed', True), ('open', 'Open', False)]) + \
    '<div class="ds-field form-field"><label class="form-label form-label--sm" for="pg-title">Title</label><div class="input-wrap"><div class="input-box input-box--sm"><input class="form-input" type="text" id="pg-title" value="Title" placeholder="Title" /></div></div></div>' + \
    '<div class="ds-field form-field"><label class="form-label form-label--sm" for="pg-info">Descriptive text</label><div class="input-wrap"><div class="input-box input-box--sm"><input class="form-input" type="text" id="pg-info" value="Descriptive text" placeholder="Descriptive text" /></div></div></div>' + \
    btn_group('pg-l-help', 'Helper text', 'data-pg="helper"', [('off', 'None', True), ('on', 'Text', False)]) + \
    btn_group('pg-l-ico', 'Leading icon', 'data-pg="icon"', [('off', 'None', True), ('on', 'Icon', False)]) + \
    btn_group('pg-l-ie', 'Trailing icon', 'data-pg="iconend"', [('off', 'None', True), ('on', 'Icon', False)]) + \
    btn_group('pg-l-sw', 'Toggle switch', 'data-pg="sw"', [('off', 'None', True), ('on', 'Switch', False)]) + \
    btn_group('pg-l-bd', 'Number badge', 'data-pg="badge"', [('off', 'None', True), ('on', '1', False)]) + \
    btn_group('pg-l-ch', 'Chevron', 'data-pg="chevron"', [('on', 'Show', True), ('off', 'Hide', False)]) + \
    '<p class="pg-note" id="pg-warn" role="status" style="margin:0" hidden></p><p class="pg-note" style="margin:0">The animation is set in <a href="#motion" class="inline-link inline-link--small inline-link--tertiary">Motion</a>.</p>' + \
    '</div></div><h3 class="ds-h3">Markup for this selection</h3>' + code_box('pg-code', 'HTML')

overview = '<h2 class="ds-h2">Overview</h2>' + desc('A collapsible is a <strong>row that opens and closes</strong> to show more content. The header names the section and can carry a descriptive text, helper text, icons, a toggle switch and a number badge. Rows stack into a list, such as an FAQ or a filter, and share one line between them.') + \
    desc('Collapsible has two sizes (Large and Small), a boxed variant (both sizes), a light and a dark theme, and the states enabled, hover and disabled. The content is free: text, a list of checkboxes, supporting text with an action. Each row opens on its own.') + \
    desc('In Storyblok this component is the <strong>Collapsible block</strong>. Its <strong>Open</strong> switch is the open state of a row (<code>collapsible-wrap--open</code>). The Storyblok widget has its own Storyblok tab in Supernova.') + \
    three_pages(SLUG, 'a collapsible', 'the values: tokens, sizes, measurements, states and requirements', 'how to add one to a page')

usage = '<h2 class="ds-h2">Usage</h2><h3 class="ds-h3 ds-group">When to use</h3>' + desc('Use a collapsible when the user skims a list and opens one part at a time. Use it for:') + \
    bullets(['To organize related content in a limited space, for example an FAQ that gives a clean overview of the most common questions', 'To hide complex or less important details, so the user can focus on the key points first', 'Filter groups, where each group holds a list of checkboxes', 'Long, optional content, such as delivery or return details']) + \
    '<h3 class="ds-h3 ds-group">When not to use</h3><h3 class="ds-h3">Do not use it to compare</h3>' + desc('When the user must see all the content at once, to compare or to understand the context, hiding part of it limits the understanding. Show the content side by side instead.') + \
    '<h3 class="ds-h3">Do not use it where people open and close a lot</h3>' + desc('Frequent opening and closing frustrates and overwhelms. Open the row that helps the user most from the start (<code>collapsible-wrap--open</code>; the Open switch in Storyblok), for example the first question in a grouped FAQ.') + \
    fig_one('<div class="co-fig co-lines" id="fig-open"></div>', 'The row that helps most is open from the start; the others stay closed.') + \
    '<h3 class="ds-h3">Do not hide what people must read</h3>' + desc('A closed row can be missed. Keep information that people need to continue in plain text.') + \
    fig_pair('<div class="co-fig co-lines" id="fig-hide-do"></div>', 'Do hide extra detail that only some people need.', '<div class="co-fig co-lines" id="fig-hide-dont"></div>', 'Do not hide terms that people must read before they continue.') + \
    '<h3 class="ds-h3">Keep the title short</h3>' + desc('Write the title as the question or the topic, so the user can scan the closed list. Put the current choice in the descriptive text, not a sentence in the title.') + \
    fig_pair('<div class="co-fig co-lines" id="fig-title-do"></div>', 'Do write a short title, and the choice as descriptive text.', '<div class="co-fig co-lines" id="fig-title-dont"></div>', 'Do not write a whole sentence as the title.') + \
    '<h3 class="ds-h3">Do not nest collapsibles</h3>' + desc('A collapsible inside a collapsible hides the content behind two clicks and harms usability. Use one level, or split the content into separate sections.') + \
    '<h3 class="ds-h3">For two views of the same content</h3>' + desc('A collapsible shows more of one thing. To switch between two views of the same content, use ' + link_large('segment-control.html', 'Pill segment control') + '. To move between pages, use ' + link_large('tabs.html', 'Tabs') + ' or navigation.') + \
    '<h3 class="ds-h3 ds-group">Best practices</h3>' + \
    bullets(['Keep item titles short and descriptive.', 'Use collapsibles to reduce visual clutter and help users focus on the key content.', 'Avoid many collapsibles in one view: they create a cluttered experience instead.', 'Give every collapsible a clear purpose that improves usability. Never use one only for decoration, or when all the content needs to be visible at once.', 'Keep the content from getting too wide. Review the line length (60–90 characters is ideal) under ' + link_large('../foundations/typography.html', 'Typography') + '.']) + \
    '<h3 class="ds-h3 ds-group">Quick reference</h3>' + \
    table(['The user…', 'Use'], [['skims a list of questions or sections and opens one at a time', 'Collapsible'], ['must see all the text', 'Plain text with headings'], ['switches between views of the same content', '<code>eco-pill-segment-control</code>'], ['moves between pages', 'Tabs or navigation']]) + \
    rules(['Use for FAQ, filters and long, optional content.', 'Keep titles short. Put the current choice in the descriptive text.', 'Use a <code>button</code> for the header, with <code>aria-expanded</code>.', 'Hide the last row’s line when the list ends the section.'],
          ['Hide content people must read to continue.', 'Nest collapsibles.', 'Use many collapsibles in one view, or one only for decoration.', 'Put a switch and a chevron in the same header: the control sits inside a control.', 'Animate with CSS height: it cannot reach <code>auto</code>.'])

anatomy = '<h2 class="ds-h2">Anatomy</h2><h3 class="ds-h3 ds-group">Header</h3>' + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout co-callout co-anat" id="co-anat-h" role="img" aria-label="Anatomy of a collapsible header: 1 leading icon, 2 title, 3 descriptive text, 4 helper text, 5 trailing icon, 6 toggle switch, 7 number badge, 8 chevron"><div class="ds-callout__art"><div id="an-head" class="co-lines"></div></div></div></figure></div>' + \
    ol_parts([('Leading icon', 'Optional. A Material Symbol before the title.'), ('Title', 'The name of the section. Bold.'), ('Descriptive text', 'Optional. The current choice or a short note, in regular weight on the same line.'), ('Helper text', 'Optional. A line of body-sm text under the title.'), ('Trailing icon', 'Optional. A Material Symbol after the text.'), ('Toggle switch', 'Optional. An on/off setting that belongs to the section.'), ('Number badge', 'Optional. For example the number of selected filters.'), ('Chevron', 'An <code>expand_more</code> icon that rotates 180° when the row is open.')]) + \
    '<h3 class="ds-h3 ds-group">Open row</h3>' + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout co-callout co-anat" id="co-anat-o" role="img" aria-label="Anatomy of an open collapsible: 1 header, 2 content, 3 line"><div class="ds-callout__art"><div id="an-open" class="co-lines"></div></div></div></figure></div>' + \
    ol_parts([('Header', 'The clickable row. At least 72px high (Large) or 56px (Small).'), ('Content', 'The answer or the options. It animates open with <code>max-height</code>; an open row has 32px of space below it.'), ('Line', 'A 1px line under the row, shared with the next row in the list.')])

variants = '<h2 class="ds-h2">Variants</h2>' + desc('Rows stack into a list and share one line between them. Each row opens on its own.') + \
    '<h3 class="ds-h3 ds-group">Header content</h3>' + desc('Title only, with a descriptive text, with a leading icon, with helper text and with a number badge. Combine the parts as the row needs.') + \
    fig_one('<div class="co-fig co-lines" id="v-head"></div>') + \
    '<h3 class="ds-h3 ds-group">With a toggle switch</h3>' + desc('A row can hold a setting that turns on and off, such as “Sale items”. Leave out the chevron: a switch inside a header that also opens is a control inside a control.') + \
    fig_one('<div class="co-fig co-lines" id="v-switch"></div>') + \
    '<h3 class="ds-h3 ds-group">Size</h3>' + desc('<strong>Large</strong> (72px) is the default. <strong>Small</strong> (56px) has smaller type and 20px icons, for dense layouts such as filters.') + \
    fig_one('<div class="co-fig co-lines" id="v-size"></div>') + \
    '<h3 class="ds-h3 ds-group">Boxed</h3>' + desc('A frame around the row, in both sizes. When it is open, a line separates the header from the content, which sits on white. The header is grey only when Header background is on (see Background below).') + \
    fig_one('<div class="co-fig co-lines" id="v-boxed"></div>') + \
    '<h3 class="ds-h3 ds-group" id="variants-dividers">Dividers</h3>' + desc('The line under the row is on by default, so rows in a list share it. The line above is off. Switch each on or off on its own: <code>collapsible-wrap--divider-top</code> adds the top line, <code>collapsible-wrap--no-divider-bottom</code> removes the bottom line. A boxed row has its frame instead.') + \
    '<div class="pg-grid"><div><span class="pg-cap">Default: bottom only</span><div class="ds-stage"><div class="co-fig co-lines" id="v-d-default"></div></div></div><div><span class="pg-cap">Top and bottom</span><div class="ds-stage"><div class="co-fig co-lines" id="v-d-both"></div></div></div><div><span class="pg-cap">Top only</span><div class="ds-stage"><div class="co-fig co-lines" id="v-d-top"></div></div></div><div><span class="pg-cap">None</span><div class="ds-stage"><div class="co-fig co-lines" id="v-d-none"></div></div></div></div>' + \
    '<h3 class="ds-h3 ds-group">Background</h3>' + desc('A row can have a background, <code>surface-raised-secondary</code>, on the header only. It is an add-on in the header part. The content stays on white. Use it to set one row apart in a list, or to give a boxed row a grey header, closed or open. Without it no row is grey, open or closed. The header gets 16px of side padding so the text keeps off the edge, and the content gets the same so it lines up. The content text starts 24px (Large) or 16px (Small) below the grey header.') + \
    fig_one('<div class="co-fig co-lines" id="v-filled"></div>') + \
    '<h3 class="ds-h3 ds-group">Theme</h3>' + desc('On a black surface use the dark theme. The line, the text and the number badge change; the layout does not. A filled row in the dark theme has a <code>surface-90</code> header, and the body and the content stay on the black surface. On hover the title and the descriptive text dim; the helper text stays white.') + \
    fig_one('<div class="co-fig co-lines" id="v-dark"></div>', stage_cls='ds-stage--dark') + \
    '<h3 class="ds-h3 ds-group">Disabled</h3>' + desc('A disabled row cannot be opened. Text, icons and the badge turn to the disabled colors.') + \
    fig_one('<div class="co-fig co-lines" id="v-disabled"></div>') + \
    '<h3 class="ds-h3 ds-group">Content</h3>' + desc('The content is free. These are the compositions in Figma.') + \
    '<h3 class="ds-h3">Text</h3>' + fig_one('<div class="co-fig co-lines" id="c-text"></div>') + \
    '<h3 class="ds-h3">Checkbox list</h3>' + desc('Each option has a number of results. A supporting text and a “Show more” action can follow the list.') + fig_one('<div class="co-narrow co-lines" id="c-list"></div>') + \
    '<h3 class="ds-h3">Filter list</h3>' + desc('A filter panel is a list of Large rows. The first row has a top divider. A row can show the current choice as descriptive text, hold a toggle switch with no chevron, or carry a trailing icon and a number of selected values. An open row can start with a search field, followed by the checkbox list.') + fig_one('<div class="co-narrow co-lines" id="c-filter" style="max-width:440px"></div>') + \
    '<h3 class="ds-h3">Supporting text and action</h3>' + desc('Supporting text with a “Show more” action and, when the section has a main action, a Secondary button (XSmall).') + fig_one('<div class="co-fig co-lines" id="c-support"></div>') + \
    '<h3 class="ds-h3">Boxed with expanded content</h3>' + desc('An intro text and a list of items on grey surfaces, each with a bold title and extra information. The header uses the grey Header background, as in Figma.') + fig_one('<div class="co-fig co-lines" id="c-boxed"></div>')

sizes = '<h2 class="ds-h2">Sizes</h2>' + desc('A collapsible has two sizes. <strong>Large</strong> is 72px high and <strong>Small</strong> is 56px high. Boxed exists in both sizes. The values are under ' + sec_link(SLUG, 'sizes', 'Sizes') + ' in Specifications.')

layout = '<h2 class="ds-h2">Layout &amp; Appearance</h2><h3 class="ds-h3 ds-group">Alignment</h3>' + desc('The icon and the text sit on the left, the switch, the badge and the chevron on the right with 16px between them. The content lines up with the left edge of the row.') + \
    '<h3 class="ds-h3 ds-group">Placement</h3>' + desc('A list sits inside a section. When the list is the last block in its section, the last row’s line is hidden, so no line hangs right above the section’s own padding. When something follows the list, such as a call to action, the line stays. A boxed row always keeps its frame.') + \
    '<div class="ds-figs"><figure class="ds-fig"><div class="ds-fig__stage" style="align-items:stretch;flex-direction:column"><section id="pl-last" style="width:100%"><div id="pl-last-list"></div></section></div><figcaption class="ds-fig__cap">The list ends the section: the last line is hidden.</figcaption></figure>' + \
    '<figure class="ds-fig"><div class="ds-fig__stage" style="align-items:stretch;flex-direction:column"><section id="pl-cta" class="co-lines" style="width:100%"><div id="pl-cta-list"></div><div class="pg-note" style="margin-top:16px">A call to action follows the list.</div></section></div><figcaption class="ds-fig__cap">Something follows the list: the last line stays.</figcaption></figure></div>' + \
    '<h3 class="ds-h3 ds-group">Width</h3>' + desc('A collapsible is as wide as its container. Long titles wrap onto a second line and the header grows.') + \
    '<h3 class="ds-h3 ds-group">Surface</h3>' + desc('A collapsible can sit on a white or on a grey section (<code>section--secondary</code>). The grey Header background has the same color as the grey section, so do not combine them.') + \
    fig_one('<div class="sec-fig" id="l-surface"></div>') + \
    '<h3 class="ds-h3 ds-group" id="layout-dividers">Dividers</h3>' + desc('Use dividers only where they add clarity. In a list the line under each row separates the rows. Switch the lines on and off one by one (see Variants) and follow these rules. A list in a panel or drawer, such as a filter list, starts with a top divider on the first row.') + \
    '<h3 class="ds-h3">In a list</h3>' + desc('Put lines between the rows only: none above the first row and none under the last. The last row in a section loses its bottom line by itself.') + \
    fig_pair('<div class="sec-fig" id="dv-list-do"></div>', 'Do use dividers only between the rows.', '<div class="sec-fig" id="dv-list-dont"></div>', 'Do not add a line above the first row or under the last row of a group.') + \
    '<h3 class="ds-h3">A single collapsible</h3>' + desc('A section with only one collapsible has no neighbours to share a line with, so it gets both the top and the bottom line (<code>--divider-top</code> and <code>--divider-bottom</code>). Not on a colored section: the surface already separates it.') + \
    fig_pair('<div class="sec-fig" id="dv-one-do"></div>', 'Do use the top and the bottom divider in a section with only one collapsible.', '<div class="sec-fig" id="dv-one-dont"></div>', 'Do not add dividers to a single collapsible on a colored surface that differs from the areas around it.') + \
    '<h3 class="ds-h3">With a headline</h3>' + desc('When the section has an optional headline above the collapsible, skip the top divider: the headline already opens the group. On a colored section the row then has no dividers at all.') + \
    fig_pair('<div class="sec-fig" id="dv-title-do"></div>', 'Do skip the top divider when the optional headline is used: the row has no dividers on the colored section.', '<div class="sec-fig" id="dv-title-dont"></div>', 'Do not put a top divider between the headline and the collapsible.') + \
    '<h3 class="ds-h3 ds-group">Appearance</h3>' + desc('The title and the icons are black and turn grey on hover. The content is black. Helper text is dark grey and turns lighter on hover; counts and notes are grey. Token names and values are under ' + sec_link(SLUG, 'design-tokens', 'Design Tokens') + ' in Specifications.')

behavior = '<h2 class="ds-h2">Behavior</h2><h3 class="ds-h3 ds-group">Click</h3>' + desc('A click on the header opens or closes the row. The content grows from zero to its full height and the chevron turns 180°. An open row gets 32px of extra space below the content. A click on the toggle switch changes the switch and does not open the row.') + \
    '<h3 class="ds-h3 ds-group">Hover</h3>' + desc('The title, the descriptive text, the icons and the chevron turn to the action hover color. The whole header reacts, not only the text.') + \
    '<h3 class="ds-h3 ds-group">Several rows</h3>' + desc('The rows are independent. Opening one does not close another.') + \
    '<h3 class="ds-h3 ds-group">Disabled</h3>' + desc('A disabled row does not react to hover or click and cannot be reached with Tab.')

access = '<h2 class="ds-h2">Accessibility</h2>' + desc('All requirements are listed under ' + sec_link(SLUG, 'accessibility-requirements', 'Accessibility Requirements') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Keyboard support</h3>' + desc('A <code>button</code> header is reached with Tab and opens with Enter or Space. Closed content cannot be reached: it is hidden until the row is open.') + \
    '<h3 class="ds-h3 ds-group">Screen reader support</h3>' + desc('The header announces its state through <code>aria-expanded</code> and points to its content with <code>aria-controls</code>. A header with a toggle switch is not a button: the switch is announced on its own, and the row does not open.')

related = '<h2 class="ds-h2">Related</h2><ul class="ds-bullets"><li><strong>' + link_large('segment-control.html', 'Pill segment control') + '</strong>. Switch between two related views of the same content.</li><li><strong>' + link_large('tabs.html', 'Tabs') + '</strong>. Move between parts of a page or sub-pages.</li><li><strong>' + link_large('checkbox.html', 'Checkbox') + '</strong>. The options in a filter row.</li><li><strong>' + link_large('switch.html', 'Switch') + '</strong>. The toggle in a header.</li><li><strong>' + link_large('badge-number.html', 'Badge Number') + '</strong>. The number in a header.</li><li><strong>' + link_large('section.html', 'Section') + '</strong>. A list usually sits inside a section.</li></ul>'

references = '<h2 class="ds-h2">References</h2>' + refs([
    ('https://www.w3.org/WAI/ARIA/apg/patterns/accordion/', 'WAI-ARIA Authoring Practices: Accordion', 'The button header, <code>aria-expanded</code> and keyboard behavior.'),
    ('https://www.w3.org/WAI/WCAG22/Understanding/name-role-value.html', 'WCAG 2.2: Name, Role, Value', 'Success criterion 4.1.2: the state of a control must be available to assistive technology.'),
    ('https://www.nngroup.com/articles/accordions-on-desktop/', 'Nielsen Norman Group: Accordions on desktop', 'When an accordion helps and when it hides too much.'),
    ('https://fluent2.microsoft.design/components/web/react/core/accordion/usage', 'Fluent 2: Accordion', 'Microsoft.'),
    ('https://carbondesignsystem.com/components/accordion/usage/', 'Carbon Design System: Accordion', 'IBM.')])

ex = [('playground', playground), ('overview', overview), ('usage', usage), ('anatomy', anatomy), ('variants', variants), ('sizes', sizes), ('layout', layout), ('behavior', behavior), ('accessibility', access), ('related', related), ('references', references)]

# ---------------------------------------------------------------- Specifications
st_tok = '<h2 class="ds-h2">Design Tokens</h2>' + desc('Resolved from the live token package.') + \
    '<div class="ds-table-wrap"><table class="ds-table" id="tok-table"><thead><tr><th scope="col">State</th><th scope="col">Part</th><th scope="col">Token</th><th scope="col">Value</th></tr></thead><tbody></tbody></table></div>'

st_sizes = '<h2 class="ds-h2">Sizes</h2>' + desc('Two sizes. Large changes at 769px, Small has the same values at every breakpoint.') + \
    table(['Part', 'Large', 'Small'], [['Header height', 'Minimum 72px', 'Minimum 56px'], ['Header padding', '24px top and bottom', '16px top and bottom'], ['Gap, text to the right group', '16px', '16px'], ['Gap, icon to text', '8px', '8px'], ['Gap, title to descriptive text', '2px', '2px'], ['Leading and trailing icon, chevron', '24px', '20px'], ['Toggle switch', '48 × 24px (Large)', '32 × 16px (X-Small)'], ['Number badge', '<code>badge-number--md</code>: 20px desktop, 18px mobile', '<code>badge-number--sm</code>: 16px desktop, 14px mobile'], ['Line under the row', '1px', '1px'], ['Open row, space below the content', '32px', '32px'], ['Header text to content text', '24px (header padding 24px)', '24px (header padding 16px + 8px)'], ['Boxed: body padding', '24px on all sides', '16px on all sides'], ['Filled: content top', '24px between the grey header and the content text', '16px between the grey header and the content text']]) + \
    '<h3 class="ds-h3 ds-group">Boxed</h3>' + table(['Part', 'Value'], [['Frame', '1px <code>border-primary</code> around the row'], ['Header padding', '24px on all sides (Large), 16px (Small)'], ['Open: header', 'No background of its own (grey only with the Header background option), with a 1px line under it (an inset shadow, so it takes no space)'], ['Open: body', 'White (<code>background-primary</code>), padding 24px (Large) or 16px (Small) on all sides, on desktop and mobile, 12px between the parts']]) + \
    note('The header uses <code>min-height</code>, not <code>height</code>, so it can grow when the title wraps.')

CO_MEAS = ('<div class="measure__item"><span class="measure__name">%d · %s</span><div class="measure__obj"><span class="co-measure"><div class="collapsible-wrap%s"><button type="button" class="collapsible-item measure__subject" style="pointer-events:none" tabindex="-1"><span class="collapsible-item__left"><span class="collapsible-item__label">Delivery times</span></span><span class="collapsible-item__chevron"><span class="ms" aria-hidden="true">expand_more</span></span></button><div class="collapsible-item__content"></div></div></span>'
           '<i class="measure__pad measure__pad--t"></i><i class="measure__pad measure__pad--b"></i><i class="measure__pad measure__pad--l"></i><i class="measure__pad measure__pad--r"></i>'
           '<b class="measure__dim measure__dim--v measure__dim--t"><span></span></b><b class="measure__dim measure__dim--v measure__dim--b"><span></span></b><b class="measure__dim measure__dim--h measure__dim--l"><span></span></b><b class="measure__dim measure__dim--h measure__dim--r"><span></span></b></div></div>')

st_meas = '<h2 class="ds-h2">Measurements</h2><h3 class="ds-h3 ds-group">Dimensions</h3>' + desc('Padding of the header at each size. The shaded areas are the padding. The numbers are read from the real component.') + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-fig__stage--flush" style="padding:0;min-height:0"><div class="measure" role="img" aria-label="Padding of a collapsible header: Large, Small and Boxed">' + CO_MEAS % (1, 'Large', '') + CO_MEAS % (2, 'Small', ' collapsible-wrap--small') + CO_MEAS % (3, 'Boxed, Large', ' collapsible-wrap--boxed') + CO_MEAS % (4, 'Boxed, Small', ' collapsible-wrap--small collapsible-wrap--boxed') + '</div></div><figcaption class="ds-fig__cap">The header at true size (1:1). The padding is the same at every breakpoint.</figcaption></figure></div>' + \
    table(['Attribute', 'Value'], [['Padding, Large', '24px top and bottom, none at the sides'], ['Padding, Small', '16px top and bottom, none at the sides'], ['Padding, Boxed', '24px on all sides (Large), 16px (Small)'], ['Minimum height', '72px (Large and Boxed Large), 56px (Small and Boxed Small)'], ['Gap, text to right group', '16px'], ['Gap, icon to text', '8px'], ['Header text to content text', '24px in every size (<code>--co-content-gap</code>); boxed: header padding plus body padding, 48px (Large) or 32px (Small)'], ['Open row, space below the content', '32px (Boxed: none, the body has 24px or 16px padding)'], ['Line', '1px'], ['Corners', 'Square']]) + \
    '<h3 class="ds-h3 ds-group">Spacing</h3>' + desc('The same distances as spacing tokens.') + table(['Part', 'Value'], [['Padding, Large', '<code>space-24</code>'], ['Padding, Boxed Large', '<code>space-24</code>'], ['Padding, Small and Boxed Small', '<code>space-16</code>'], ['Gap, text to right group', '<code>space-16</code>'], ['Gap, icon to text', '<code>space-8</code>'], ['Open row, space below', '<code>space-32</code>'], ['Checkbox list: gap, bottom', '<code>space-24</code>, <code>space-24</code>'], ['Header text to content text', '<code>space-24</code> in every size; boxed: 48px / 32px']])

st_states = '<h2 class="ds-h2">States</h2>' + desc('The title, the descriptive text, the icons and the chevron turn to the action hover color (dark theme: the title, the descriptive text and the icons dim, the helper text does not). An open row turns the chevron 180° and adds 32px of space below. Hover is forced on this page; in your code it comes from <code>:hover</code>.') + \
    toolbar([('mx-bp', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force'), ('mx-size', 'Size', 'data-mx="size"', [('large', 'Large', True), ('small', 'Small', False)]), ('mx-th', 'Theme', 'data-mx="theme"', [('light', 'Light', True), ('dark', 'Dark', False)])]) + \
    '<div class="ds-table-wrap"><table class="ds-table pg-matrix" id="matrix"><thead><tr><th scope="col">State</th><th scope="col">Closed</th><th scope="col">Open</th></tr></thead><tbody></tbody></table></div>' + \
    note('<strong>Disabled</strong> is defined once in Figma, under Theme Dark, with the disabled text color and the light line (<code>border-primary</code>). Here it is shown on both themes. Focus: a 2px ring on keyboard focus (<code>border-focus</code>).')

st_typo = '<h2 class="ds-h2">Typography</h2>' + table(['Element', 'Token', 'Mobile', 'Desktop (769px+)', 'Color'], [
    ['Title, Large', '<code>title-md</code>, weight 600', '18/22, 0', '20/24, 0', '<code>text-primary</code>, hover <code>text-action-primary-hover</code>'], ['Descriptive text, Large', 'regular, same size as the title', '18/24, 0', '20/24, 0', 'same as the title'],
    ['Title, Small', '<code>title-sm</code>, weight 600', '16/18, 0', '16/18, 0', 'same as the title'], ['Descriptive text, Small', '<code>body-md</code>, weight 400', '16/22, 0.32px', '17/24, 0.32px', 'same as the title'],
    ['Helper text', '<code>body-sm</code>, weight 400', '14/20, 0.36px', '14/20, 0.36px', '<code>text-secondary</code>, hover <code>text-tertiary</code>; dark <code>text-primary-inverted</code> (no hover change)'], ['Content', '<code>body-md</code>, weight 400', '16/22, 0.32px', '17/24, 0.32px', '<code>text-primary</code>; 12px between paragraphs'],
    ['Note under a list', '<code>body-sm</code>', '14/20, 0.36px', '14/20, 0.36px', '<code>text-tertiary</code>'], ['Count beside a checkbox', '16/22', '16/22, 0.32px', '16/22, 0.32px', '<code>text-tertiary</code>'], ['“Show more”', '<code>body-md</code>, weight 600', '16/22, 0.32px', '17/24, 0.32px', '<code>text-primary</code>, underlined on hover']]) + \
    note('Breuer Condensed. The CSS weight is Figma minus 100.')

st_struct = '<h2 class="ds-h2">Structure</h2><h3 class="ds-h3 ds-group">Elements</h3>' + table(['Element', 'Class', 'Notes'], [
    ['Row', '<code>collapsible-wrap</code>', 'One row, with the line under it. <code>--open</code> when open; <code>--small</code>, <code>--boxed</code>, <code>--filled</code>, <code>--divider-top</code>, <code>--divider-bottom</code>, <code>--no-divider-bottom</code>, <code>--dark</code>, <code>--disabled</code> are modifiers.'], ['Header', '<code>collapsible-item</code>', 'A <code>&lt;button&gt;</code> (recommended). The older <code>&lt;div onclick&gt;</code> still works. Not a button when it holds a switch.'], ['Left group', '<code>collapsible-item__left</code>', 'The icon, the text and the trailing icon.'],
    ['Text group', '<code>collapsible-item__text</code>, <code>__line</code>', 'Title and descriptive text on one line, helper text under it. Optional.'], ['Title', '<code>collapsible-item__label</code>', 'Bold.'], ['Descriptive text', '<code>collapsible-item__info</code>', 'Regular, after the title.'], ['Helper text', '<code>collapsible-item__helper</code>', 'Optional.'],
    ['Right group', '<code>collapsible-item__end</code>', 'The switch, the badge and the chevron.'], ['Chevron', '<code>collapsible-item__chevron</code>', 'An <code>expand_more</code> icon (<code>ms</code>). Leave it out for a row that does not open.'], ['Content', '<code>collapsible-item__content</code>', 'Must follow the header directly: the script reads <code>nextElementSibling</code>.'],
    ['Boxed body', '<code>collapsible-item__body</code>', 'Inside the content of a boxed row.'], ['Content patterns', '<code>collapsible-item__list</code>, <code>__row</code>, <code>__count</code>, <code>__support</code>, <code>__note</code>, <code>__more</code>', 'A checkbox list with counts, supporting text and a “Show more” action.']]) + \
    '<h3 class="ds-h3 ds-group">Types</h3>' + table(['Type', 'Markup', 'Use'], [['Large', 'Default', 'FAQ lists and page sections.'], ['Small', '<code>collapsible-wrap--small</code>', 'Dense layouts such as filters.'], ['Boxed', '<code>collapsible-wrap--boxed</code> (Large), <code>collapsible-wrap--small collapsible-wrap--boxed</code> (Small)', 'A framed row. The header is grey only with <code>--filled</code>.'], ['Top divider', '<code>collapsible-wrap--divider-top</code>', 'A 1px line above the row (off by default).'], ['No bottom divider', '<code>collapsible-wrap--no-divider-bottom</code>', 'Removes the line under the row (on by default).'], ['Bottom divider forced', '<code>collapsible-wrap--divider-bottom</code>', 'Keeps the line under the last row in a section, for example a section with one collapsible.'], ['Filled', '<code>collapsible-wrap--filled</code>', 'A <code>surface-raised-secondary</code> background on the header. The content stays white.'], ['Dark', '<code>collapsible-wrap--dark</code>', 'On a black surface.'], ['Disabled', '<code>collapsible-wrap--disabled</code> and <code>disabled</code> on the button', 'A row that cannot be opened.']]) + \
    '<h3 class="ds-h3 ds-group">Width</h3>' + desc('As wide as the container.')

st_motion = '<h2 class="ds-h2">Motion</h2>' + table(['Property', 'Duration', 'Easing'], [['Content <code>max-height</code>', '<code>duration-fast-4</code> (200ms), set through <code>--co-duration</code>', '<code>ease-standard</code>, set through <code>--co-ease</code>'], ['Chevron <code>transform</code>', 'the same', 'the same'], ['Row <code>padding-bottom</code>', 'the same', 'the same'], ['Title, text and icon <code>color</code> on hover', '<code>duration-fast-3</code> (150ms)', '<code>ease-standard</code>']]) + \
    note('Opening is a state change on the spot, so it uses standard easing and a short duration (<code>eco-motion</code>). With <code>prefers-reduced-motion: reduce</code> every transition is off. Compare other values in the live Motion section on <a class="inline-link inline-link--medium inline-link--secondary" href="collapsible.html#motion">Examples &amp; Guidelines</a>.')

st_behavior = '<h2 class="ds-h2">Behavior</h2>' + table(['Input', 'Result'], [['Click the header, Enter or Space', '<code>toggleCollapsible(this)</code> toggles <code>.collapsible-wrap--open</code>, sets <code>aria-expanded</code> and sets <code>max-height</code> to the content’s <code>scrollHeight</code>. CSS cannot animate to <code>auto</code>.'], ['Click the toggle switch', 'Changes the switch only. A click on a link or on an element with <code>data-collapsible-ignore</code> in the header does the same.'], ['Hover', 'Title, text and icons change color.'], ['Disabled', 'No hover, no click, no Tab.'], ['Several rows', 'Independent: opening one does not close another.'], ['Breakpoint', 'Large changes size at 769px.'], ['Window resize while open', '<strong>Open point.</strong> The height is set once, when the row opens. If the text wraps differently after a resize, the height is not updated.']])

st_access = '<h2 class="ds-h2">Accessibility Requirements</h2>' + table(['Topic', 'Requirement'], [
    ['Header element', 'Use a <code>button</code>, so it is reached with Tab and works with Enter and Space (WCAG 2.1.1, 4.1.2). Older pages still use a <code>div</code> with <code>onclick</code>: it cannot take focus.'], ['State', 'Set <code>aria-expanded</code> on the header; the script keeps it in sync. Link it to the content with <code>aria-controls</code>.'],
    ['Switch in the header', 'A button cannot hold another control. A row with a toggle switch uses a <code>div</code> and has no chevron, or the switch moves out of the header. <strong>Open point:</strong> Figma shows a switch and a chevron together.'], ['Focus', 'A 2px ring on keyboard focus (<code>border-focus</code>), 2px outside the header.'], ['Content', 'Closed content is <code>visibility: hidden</code>, so it is not read and cannot be focused.'], ['Contrast', 'The disabled text color is exempt (WCAG 1.4.3). Helper text and counts use <code>text-tertiary</code> (4.5:1 on white).'], ['Motion', 'Reduced motion: all transitions are off.']])

spec = [('design-tokens', st_tok), ('sizes', st_sizes), ('measurements', st_meas), ('states', st_states), ('typography', st_typo), ('structure', st_struct), ('motion', st_motion), ('behavior', st_behavior), ('accessibility-requirements', st_access)]

# ---------------------------------------------------------------- Code
c_basic = '<h2 class="ds-h2">Basic Usage</h2>' + desc('Link the shared stylesheet and the script once per page. Never copy the rules into a page.') + table(['Step', 'What to do'], [
    ['1. Link', '<code>&lt;link rel="stylesheet" href="/components/css/collapsible.css"&gt;</code> and <code>&lt;script src="/components/js/collapsible.js"&gt;&lt;/script&gt;</code>. A switch needs <code>switch.css</code>, a number <code>badge.css</code>.'], ['2. Row', 'A <code>.collapsible-wrap</code> with a <code>&lt;button class="collapsible-item"&gt;</code> and a content element that follows it directly.'],
    ['3. State', 'Set <code>aria-expanded</code> and <code>aria-controls</code> (the content’s <code>id</code>) on the button. The script updates <code>aria-expanded</code>.'], ['4. List', 'Stack several rows in one wrapper. They share the line between them.'], ['5. Size, background and theme', 'Add <code>collapsible-wrap--small</code>, <code>--boxed</code>, <code>--filled</code> (a <code>surface-raised-secondary</code> header background) or <code>--dark</code> to the row.'], ['6. Open', 'Add <code>collapsible-wrap--open</code> and set <code>max-height</code> on the content to start open.']])
c_co = '<h2 class="ds-h2">Collapsible</h2>' + desc('Copy the markup you need.') + '<div id="recipes"></div>' + note('The markup has no motion. The open and close animation is set in <a href="collapsible.html#motion" class="inline-link inline-link--medium inline-link--secondary">Motion</a> on Examples &amp; Guidelines.')
c_api = '<h2 class="ds-h2">API</h2><h3 class="ds-h3 ds-group">Classes</h3>' + table(['Class', 'Use'], [['<code>collapsible-wrap</code>', 'One row with the line under it.'], ['<code>--open</code>, <code>--small</code>, <code>--boxed</code>, <code>--filled</code>, <code>--divider-top</code>, <code>--divider-bottom</code>, <code>--no-divider-bottom</code>, <code>--dark</code>, <code>--disabled</code>', 'Modifiers on the row.'], ['<code>collapsible-item</code>', 'The header.'], ['<code>__left</code>, <code>__text</code>, <code>__line</code>, <code>__label</code>, <code>__info</code>, <code>__helper</code>, <code>__end</code>, <code>__chevron</code>', 'The parts of the header.'], ['<code>collapsible-item__content</code>, <code>__body</code>', 'The content. Animated with <code>max-height</code>.'], ['<code>__list</code>, <code>__row</code>, <code>__count</code>, <code>__support</code>, <code>__note</code>, <code>__more</code>', 'Content patterns.']]) + \
    '<h3 class="ds-h3 ds-group">Script</h3>' + table(['Function', 'Use'], [['<code>toggleCollapsible(header)</code>', 'Toggles the open class on the header’s parent, updates <code>aria-expanded</code> and sets <code>max-height</code> on the next sibling. It does nothing for a disabled row or for a click on a switch or a link in the header.']]) + \
    '<h3 class="ds-h3 ds-group">CSS variables</h3>' + table(['Variable', 'Use'], [['<code>--co-ease</code>', 'The easing of the open and close animation. Default <code>var(--ease-standard)</code>.'], ['<code>--co-duration</code>', 'The duration. Default <code>var(--duration-fast-4)</code>.'], ['<code>--co-content-gap</code>', 'The space from the header text to the content text. Default 24px, the same for every size.']]) + \
    '<h3 class="ds-h3 ds-group">Things to know</h3>' + bullets(['The content must be the next sibling of the header.', 'The last row’s line is hidden when the list is the last block in its section (not for a boxed row). Add <code>collapsible-wrap--divider-bottom</code> to keep it, for a section with one collapsible.', 'Boxed works in both sizes: add <code>collapsible-wrap--boxed</code> (Large) or <code>collapsible-wrap--small collapsible-wrap--boxed</code> (Small).', 'A header with a switch is a <code>div</code>, not a button. Prefer a row with a switch and no chevron.'])
c_css = '<h2 class="ds-h2">CSS / Tailwind</h2>' + desc('The component is one CSS file and one script, shared by every page. Link them, never copy them. The code below is read from the files the page links, so it is always what you see.') + code_box('css-code', 'CSS (components/css/collapsible.css)') + '<div style="height:24px"></div>' + code_box('js-code', 'JS (components/js/collapsible.js)')
code = [('basic-usage', c_basic), ('collapsible', c_co), ('api', c_api), ('css-tailwind', c_css, False)]

# ---------------------------------------------------------------- scripts
JS_EX = CO_JS + r'''
  var st = { size: 'large', boxed: 'no', fill: 'no', top: 'off', bottom: 'on', theme: 'light', state: 'enabled', open: 'closed', helper: 'off', icon: 'off', iconend: 'off', sw: 'off', badge: 'off', chevron: 'on' };
  function sync(key) { $$('[data-pg="' + key + '"] button').forEach(function (b) { b.setAttribute('aria-pressed', String(b.dataset.v === st[key])); }); }
  function opts() {
    return { title: $('#pg-title').value, info: $('#pg-info').value, helper: st.helper === 'on' ? 'Description or helper text' : '', size: st.size, boxed: st.boxed === 'yes', filled: st.fill === 'yes', topLine: st.top === 'on', noBottomLine: st.bottom === 'off', dark: st.theme === 'dark', disabled: st.state === 'disabled', hover: st.state === 'hover',
      open: st.open === 'open', icon: st.icon === 'on' ? 'tune' : '', iconEnd: st.iconend === 'on' ? 'tune' : '', sw: st.sw === 'on', badge: st.badge === 'on', chevron: st.chevron === 'on' };
  }
  function renderPg() {
    $$('[data-pg="top"] button, [data-pg="bottom"] button').forEach(function (b) { b.disabled = st.boxed === 'yes'; });
    $('#pg-stage').classList.toggle('ds-stage--dark', st.theme === 'dark');
    var o = opts(); o.host = clear($('#pg-host')); row(o);
    var warn = $('#pg-warn'); warn.hidden = !(st.sw === 'on' && st.chevron === 'on');
    warn.textContent = 'Warning: a switch and a chevron in one header put a control inside a control. Hide the chevron, or move the switch out of the header.';
    $('#pg-code').textContent = (o.hover ? '<!-- hover is forced here for preview; in production it comes from :hover -->\n' : '') + printable(opts());
  }
  DK.wire(st, renderPg); $('#pg-title').addEventListener('input', renderPg); $('#pg-info').addEventListener('input', renderPg);
  DK.bp(refit);

  /* Usage figures */
  row({ host: clear($('#fig-hide-do')), title: 'Delivery times', open: true, body: '<p>Orders placed before 14:00 leave the warehouse the same day.</p>' });
  row({ host: clear($('#fig-hide-dont')), title: 'Terms of the agreement', body: '<p>The agreement runs for 24 months and renews automatically.</p>' });
  row({ host: clear($('#fig-title-do')), title: 'Sort', info: 'Relevance', body: '<p>Relevance, price, name.</p>' });
  row({ host: clear($('#fig-title-dont')), title: 'I would like to sort the products by relevance', body: '<p>Relevance, price, name.</p>' });

  /* Open from the start + dividers + surface (section figures) */
  function band(host, cls, build) { var s = document.createElement('section'); s.className = 'section section--flush' + (cls ? ' ' + cls : ''); var d = document.createElement('div'); d.className = 'sec-in'; s.appendChild(d); host.appendChild(s); if (build) build(d); return d; }
  function ph(host, label) { band(host, '', function (d) { d.innerHTML = '<div class="sec-ph">' + label + '</div>'; }); }
  var QS = ['How do I start shopping online?', 'How does the address book work?', 'How do I change my password?'];
  function rows(d, list, o) { list.forEach(function (q, i) { var r = { host: d, title: q, body: '<p>Orders placed before 14:00 leave the warehouse the same day.</p>' }; var x = o ? o(i, list.length) : null; if (x) for (var k in x) r[k] = x[k]; row(r); }); }
  rows(clear($('#fig-open')), QS, function (i) { return { open: i === 0 }; });
  var f;
  f = clear($('#dv-list-do')); ph(f, 'Page content'); band(f, '', function (d) { rows(d, QS); }); ph(f, 'Page content');
  f = clear($('#dv-list-dont')); f.classList.add('co-lines'); ph(f, 'Page content'); band(f, '', function (d) { rows(d, QS, function (i) { return i === 0 ? { topLine: true } : null; }); }); ph(f, 'Page content');
  f = clear($('#dv-one-do')); ph(f, 'Page content'); band(f, '', function (d) { rows(d, [QS[0]], function () { return { topLine: true, bottomLine: true }; }); }); ph(f, 'Page content');
  f = clear($('#dv-one-dont')); f.classList.add('co-lines'); ph(f, 'Page content'); band(f, 'section--secondary', function (d) { rows(d, [QS[0]], function () { return { topLine: true, bottomLine: true }; }); }); ph(f, 'Page content');
  function titled(host, bad) { band(host, 'section--secondary', function (d) { d.insertAdjacentHTML('beforeend', '<h3 class="ds-h3">Optional title</h3>'); rows(d, [QS[0]], function () { return bad ? { topLine: true, bottomLine: true } : { noBottomLine: true }; }); }); }
  f = clear($('#dv-title-do')); ph(f, 'Page content'); titled(f, false); ph(f, 'Page content');
  f = clear($('#dv-title-dont')); f.classList.add('co-lines'); ph(f, 'Page content'); titled(f, true); ph(f, 'Page content');
  f = clear($('#l-surface')); f.classList.add('co-lines'); band(f, '', function (d) { rows(d, [QS[0], QS[1]]); }); band(f, 'section--secondary', function (d) { rows(d, [QS[0], QS[1]]); });

  /* Anatomy */
  function rng(el) { return function () { var r = document.createRange(); r.selectNodeContents(el); return r.getBoundingClientRect(); }; }
  var aw = row({ host: clear($('#an-head')), icon: 'tune', iconEnd: 'tune', title: 'Title', info: 'Descriptive text', helper: 'Description or helper text', sw: true, badge: true, body: '' });
  var lead = $('.collapsible-item__left .ms', aw), trail = $$('.collapsible-item__left .ms', aw)[1], lab = $('.collapsible-item__label', aw), inf = $('.collapsible-item__info', aw), hlp = $('.collapsible-item__helper', aw), swi = $('.form-switch-item', aw), bdg = $('.badge-number', aw), chev = $('.collapsible-item__chevron', aw);
  DK.callouts($('#co-anat-h'), [
    { n: 1, el: lead, side: 'top', len: 44, at: 'center' },
    { n: 2, box: rng(lab), side: 'top', len: 44 },
    { n: 3, box: rng(inf), side: 'top', len: 44 },
    { n: 4, box: rng(hlp), side: 'bottom', len: 44 },
    { n: 5, el: trail, side: 'bottom', len: 44, at: 'center' },
    { n: 6, el: swi, side: 'top', len: 44, at: 'center' },
    { n: 7, el: bdg, side: 'bottom', len: 44, at: 'center' },
    { n: 8, el: chev, side: 'top', len: 44, at: 'center' }
  ]);
  var ow = row({ host: clear($('#an-open')), title: 'Title', open: true, body: '<p>It depends on the scope and which features you need.</p>' });
  DK.callouts($('#co-anat-o'), [
    { n: 1, el: $('.collapsible-item', ow), side: 'left', len: 44 },
    { n: 2, box: rng($('.collapsible-item__content p', ow)), side: 'right', len: 56 },
    { n: 3, box: function () { var r = ow.getBoundingClientRect(); return { left: r.left, top: r.bottom - 1, width: r.width, height: 1 }; }, side: 'bottom', len: 44, at: 'center' }
  ]);

  /* Variants */
  var vh = clear($('#v-head'));
  row({ host: vh, title: 'Title', body: '' }); row({ host: vh, title: 'Sort', info: 'Relevance', body: '' }); row({ host: vh, icon: 'tune', title: 'Filter', info: 'Descriptive text', body: '' }); row({ host: vh, title: 'Availability', helper: 'Description or helper text', body: '' }); row({ host: vh, title: 'Brand', badge: true, body: '' });
  row({ host: clear($('#v-switch')), title: 'Sale items', sw: true, chevron: false, body: '' });
  var vz = clear($('#v-size')); row({ host: vz, title: 'Large', info: 'Descriptive text', icon: 'tune', badge: true, body: '' }); row({ host: vz, size: 'small', title: 'Small', info: 'Descriptive text', icon: 'tune', badge: true, body: '' });
  var vb = clear($('#v-boxed')); vb.style.cssText = 'display:flex;flex-direction:column;gap:16px;max-width:640px;width:100%';
  [['large', false], ['large', true], ['small', false], ['small', true]].forEach(function (b) { row({ host: vb, boxed: true, size: b[0], open: b[1], icon: 'assignment_turned_in', title: 'Contract assortment', info: 'The product is in 2 assortments', body: '<p>Text.</p>' }); });
  [['default', {}], ['both', { topLine: true }], ['top', { topLine: true, noBottomLine: true }], ['none', { noBottomLine: true }]].forEach(function (d) { var o = { host: clear($('#v-d-' + d[0])), title: 'Title', info: 'Descriptive text', body: '' }; for (var k in d[1]) o[k] = d[1][k]; row(o); });
  var vf = clear($('#v-filled')); row({ host: vf, filled: true, icon: 'tune', title: 'Title', info: 'Descriptive text', body: '' }); row({ host: vf, filled: true, open: true, title: 'Open row', body: '<p>Orders placed before 14:00 leave the warehouse the same day.</p>' }); vf.style.cssText = 'display:flex;flex-direction:column;gap:16px';
  var vd = clear($('#v-dark')); row({ host: vd, dark: true, icon: 'tune', title: 'Title', info: 'Descriptive text', badge: true, body: '' }); row({ host: vd, dark: true, hover: true, icon: 'tune', title: 'Title', info: 'Descriptive text (hover)', badge: true, body: '' });
  vd.style.cssText = 'display:flex;flex-direction:column;gap:16px'; row({ host: vd, dark: true, boxed: true, title: 'Title', info: 'Descriptive text', body: '<p>Content text.</p>' }); row({ host: vd, dark: true, boxed: true, open: true, title: 'Title', info: 'Descriptive text', body: '<p>Content text.</p>' }); row({ host: vd, dark: true, filled: true, open: true, title: 'Title', info: 'Descriptive text', body: '<p>Content text.</p>' });
  row({ host: clear($('#v-disabled')), disabled: true, icon: 'tune', title: 'Brand', info: 'Descriptive text', badge: true, body: '' });

  /* Content */
  row({ host: clear($('#c-text')), title: 'Contact customer support', open: true, body: '<p>If you are already a Swedol customer, contact web support and we will help you with your login details. Have your customer number ready.</p><p>Best regards,<br />The Swedol team</p>' });
  function cbRow(l, n) { return '<div class="collapsible-item__row"><label class="form-checkbox-item"><input type="checkbox" /><span>' + l + '</span></label><span class="collapsible-item__count">' + n + '</span></div>'; }
  row({ host: clear($('#c-list')), title: 'Price', open: true, body: '<div class="collapsible-item__list">' + [['0 – 999 kr', 50], ['1 000 – 3 999 kr', 100], ['4 000 – 5 999 kr', 75], ['6 000 – 8 999 kr', 5], ['9 000 – 10 999 kr', 5], ['11 000 + kr', 2]].map(function (r) { return cbRow(r[0], r[1]); }).join('') + '</div><div class="collapsible-item__support"><p class="collapsible-item__note">Prices are shown excluding VAT. Your agreement prices apply when you are logged in.</p><button type="button" class="collapsible-item__more">Show more</button></div>' });
  (function () {
    var h = clear($('#c-filter')), search = '<div class="input-wrap"><div class="input-box"><span class="input-icon input-icon--lg" aria-hidden="true">search</span><input class="form-input" type="text" placeholder="Search assortment" aria-label="Search assortment" /></div></div>';
    function cb(l, n, on) { return '<div class="collapsible-item__row"><label class="form-checkbox-item"><input type="checkbox"' + (on ? ' checked' : '') + ' /><span>' + l + '</span></label><span class="collapsible-item__count">' + n + '</span></div>'; }
    var list = '<div class="collapsible-item__list">' + [['Sneakers', 4, 0], ['Plumber', 0, 0], ['Electrician', 200, 1], ['Asphalt layer', 0, 0], ['Cement', 0, 0]].map(function (r) { return cb(r[0], r[1], r[2]); }).join('') + '</div>';
    row({ host: h, topLine: true, title: 'Sorting', info: 'Most popular', body: '' });
    row({ host: h, title: 'Campaign', sw: true, chevron: false, body: '' });
    row({ host: h, title: 'Assortment', body: '' });
    row({ host: h, title: 'Contract assortment', iconEnd: 'assignment_turned_in', badge: true, open: true, body: search + list });
    row({ host: h, title: 'Product category', body: '' });
    row({ host: h, title: 'Brand', badge: true, body: '' });
  })();
  row({ host: clear($('#c-support')), title: 'Support', open: true, body: '<div class="collapsible-item__support"><p class="collapsible-item__note">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque eget euismod elit.</p><button type="button" class="collapsible-item__more">Show more</button><button type="button" class="btn btn--secondary btn--xs"><span class="btn__label">Button label</span></button></div>' });
  function agree(t) { return '<div style="background:var(--color-surface-02);padding:12px"><div style="font-size:14px;line-height:20px;letter-spacing:.36px;font-weight:600">' + t + '</div><div style="font-size:17px;line-height:24px;letter-spacing:.32px;color:var(--color-text-tertiary)">Extra info?</div></div>'; }
  var cb = clear($('#c-boxed')); cb.style.maxWidth = '640px';
  row({ host: cb, boxed: true, filled: true, size: 'small', open: true, icon: 'assignment_turned_in', title: 'Contract assortment', info: 'The product is in 2 assortments', body: '<p style="font-size:14px;line-height:20px;letter-spacing:.36px;color:var(--color-text-secondary)">The following agreements and settings in your customer profile give you unique discounts or tailored assortments on this product:</p>' + agree('IKEA Global Assortment') + agree('SBAB Office &amp; Profile') });

  /* Placement */
  ['#pl-last-list', '#pl-cta-list'].forEach(function (id) { var h = $(id); ['Delivery', 'Returns'].forEach(function (t) { row({ host: h, title: t, body: '<p>Orders placed before 14:00 leave the warehouse the same day.</p>' }); }); });

  DK.motion({ anchor: 'playground', prefix: 'co', collapse: false, always: true, rec: { ease: 'standard', dur: 'fast-4' }, why: 'Opening and closing is a state change on the spot: standard easing (eco-motion: Collapsible) and a short fade of 200 ms. The row opens by itself in the preview; click the header to close it.',
    preview: function () { var h = document.createElement('div'); h.style.width = '100%'; var w = row({ host: h, title: 'Delivery times', body: '<p>Orders placed before 14:00 leave the warehouse the same day.</p>' }); setTimeout(function () { w.firstElementChild.click(); }, 60); return h; } });
  /* the split pages are all white with a divider between sections: DK.motion alternates backgrounds, so undo that */
  $$('.ds-doc > section.ds-section').forEach(function (s) { s.classList.remove('ds-section--secondary'); });
  $('#motion').insertAdjacentHTML('beforebegin', '<div class="ds-sep"><hr class="divider" /></div>');
  renderPg();
'''

JS_SPEC = CO_JS + r'''
  DK.tokenTable($('#tok-table tbody'), [
    ['Light, enabled', 'Title, text, icons, chevron', 'text-primary'], ['Light, hover', 'Title, text, icons, chevron', 'text-action-primary-hover'], ['Light, enabled', 'Helper text', 'text-secondary'], ['Light, hover', 'Helper text', 'text-tertiary'], ['Light', 'Note, count', 'text-tertiary'], ['Light', 'Content', 'text-primary'], ['Light', 'Line, boxed frame', 'border-primary'],
    ['Filled', 'Header background', 'surface-raised-secondary'], ['Filled', 'Content background', 'background-primary'], ['Boxed, open', 'Body surface', 'background-primary'], ['Boxed, open', 'Intro text', 'text-secondary'],
    ['Dark, enabled', 'Title, descriptive text, icons', 'text-action-primary-inverted'], ['Dark, hover', 'Title, descriptive text, icons', 'text-action-primary-inverted-hover'], ['Dark', 'Helper text, content', 'text-primary-inverted'], ['Dark', 'Line, boxed frame', 'border-dark'], ['Dark, filled', 'Header background', 'surface-90'], ['Dark', 'Number badge', 'surface-raised-primary'], ['Dark', 'Number badge text', 'text-primary'],
    ['Disabled', 'Title, descriptive text, helper text, icons', 'text-disabled'], ['Disabled', 'Line', 'border-primary'], ['Disabled', 'Number badge', 'surface-disabled']]);
  var mx = { size: 'large', theme: 'light' };
  function buildMatrix() {
    var tb = clear($('#matrix tbody')), dark = mx.theme === 'dark';
    [['Enabled', {}], ['Hover', { hover: true }], ['Disabled', { disabled: true }]].forEach(function (r) {
      var tr = document.createElement('tr'), th = document.createElement('th'); th.scope = 'row'; th.textContent = r[0]; tr.appendChild(th);
      [false, true].forEach(function (open) {
        var td = document.createElement('td'); if (dark) td.className = 'co-dark'; var h = document.createElement('div'); td.appendChild(h); tr.appendChild(td);
        var o = { host: h, size: mx.size, dark: dark, open: open, icon: 'tune', title: 'Title', info: 'Descriptive text', badge: true, body: '<p>Orders placed before 14:00 leave the warehouse the same day.</p>' };
        for (var k in r[1]) o[k] = r[1][k];
        row(o);
      });
      tb.appendChild(tr);
    });
  }
  $$('[data-mx]').forEach(function (g) { DK.seg(g, function (v) { mx[g.dataset.mx] = v; buildMatrix(); }); });
  buildMatrix();
  DK.bp(function () { refit(); if (window.ECO_MEASURE) ECO_MEASURE.init(); });
'''

JS_CODE = CO_JS + r'''
  DK.recipes($('#recipes'), [
    ['One row (link collapsible.css and collapsible.js)', printable({ title: 'What does it cost to set up a custom webshop?', body: '<p>It depends on the scope and which features you need.</p>' })],
    ['Title with descriptive text, icon and badge', printable({ icon: 'tune', title: 'Sort', info: 'Relevance', badge: true, body: '<p>Relevance, price, name.</p>' })],
    ['Small', printable({ size: 'small', title: 'Brand', badge: true, body: '<p>…</p>' })],
    ['Boxed (Large)', printable({ boxed: true, icon: 'assignment_turned_in', title: 'Contract assortment', info: 'The product is in 2 assortments', body: '<p>…</p>' })],
    ['Boxed, Small', printable({ size: 'small', boxed: true, icon: 'assignment_turned_in', title: 'Contract assortment', info: 'The product is in 2 assortments', body: '<p>…</p>' })],
    ['Top divider on, bottom divider off', printable({ topLine: true, noBottomLine: true, title: 'Title', body: '<p>…</p>' })],
    ['Filled (grey header)', printable({ filled: true, title: 'Title', body: '<p>…</p>' })],
    ['Dark', printable({ dark: true, title: 'Title', body: '<p>…</p>' })],
    ['Disabled', printable({ disabled: true, title: 'Brand', body: '' })],
    ['A row with a toggle switch (no chevron, does not open)', printable({ title: 'Sale items', sw: true, chevron: false, body: '' })],
    ['Open from the start', printable({ open: true, title: 'Delivery times', body: '<p>Orders placed before 14:00 leave the warehouse the same day.</p>' }).replace('<div class="collapsible-item__content" id="faq-1">', '<div class="collapsible-item__content" id="faq-1" style="max-height: 200px">')],
    ['Checkbox list in the content', '<div class="collapsible-item__content" id="price">\n  <div class="collapsible-item__list">\n    <div class="collapsible-item__row">\n      <label class="form-checkbox-item"><input type="checkbox" /><span>0 – 999 kr</span></label>\n      <span class="collapsible-item__count">50</span>\n    </div>\n  </div>\n  <div class="collapsible-item__support">\n    <p class="collapsible-item__note">Prices are shown excluding VAT.</p>\n    <button type="button" class="collapsible-item__more">Show more</button>\n  </div>\n</div>'],
    ['Other easing or duration (set on a wrapper)', '.your-wrapper {\n  --co-ease: var(--ease-standard);\n  --co-duration: var(--duration-fast-4);\n}']]);
  DK.printCss($('#css-code'), 'collapsible');
  fetch('../../components/js/collapsible.js', { cache: 'no-cache' }).then(function (r) { return r.text(); }).then(function (t) { $('#js-code').textContent = t; });
'''

# ---------------------------------------------------------------- Storyblok
def shot(src, alt, pins=(), box=None, cap=None):
    inner = '<img src="/images/%s" alt="%s" />' % (src, alt)
    if box:
        inner += '<span class="sb-box" style="left:%s%%;top:%s%%;width:%s%%;height:%s%%"></span>' % box
    for n, x, y, red in pins:
        inner += '<span class="badge-number sb-pin%s" style="left:%s%%;top:%s%%">%s</span>' % (' sb-pin--red' if red else '', x, y, n)
    return '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage sb-stage"><div class="sb-shot">%s</div></div>%s</figure></div>' % (inner, ('<figcaption class="ds-fig__cap">%s</figcaption>' % cap) if cap else '')

sb_over = '<h2 class="ds-h2">Collapsible block</h2>' + desc('The <strong>Collapsible block</strong> is the Storyblok widget for the Collapsible component. An editor builds a group of collapsible rows in a section: first the container, then one <strong>Collapsible item</strong> for each row. The block works on a white or a grey section.') + \
    desc('This page shows the editing in Storyblok. For when to use a collapsible and how it looks, see ' + link_large('collapsible.html', 'Examples &amp; Guidelines') + '.') + \
    '<h3 class="ds-h3 ds-group">Steps</h3>' + ol_parts([('Add the block', 'Insert the Collapsible block in a section.'), ('Set up the container', 'Give the group an optional headline and add the items.'), ('Set up each item', 'Write the title, add the content, and choose Open and the two dividers.'), ('Add the content', 'Fill the item with a content block.')])

sb_add = '<h2 class="ds-h2">Add the block</h2>' + desc('In the section, choose <strong>Add block</strong> and pick <strong>Collapsible</strong> in the Insert block list. The block has the technical name <code>collapsible</code>.') + \
    shot('storyblok-collapsible-insert-block.png', 'The Insert block list in Storyblok with the Collapsible block marked', box=('72.3', '27.8', '23.8', '6.8'), cap='The Collapsible block in the Insert block list.')

sb_cont = '<h2 class="ds-h2">Collapsible block container</h2>' + desc('The container holds the group. It has an optional headline and a list of items.') + \
    shot('storyblok-collapsible-container.png', 'The Collapsible block container in Storyblok with the headline field and the Add Block button', pins=((1, '74.8', '38.5', False), (2, '74.8', '53.4', False)), cap='The container: the headline and the list of items.') + \
    ol_parts([('Headline', 'Optional. The title above the group, for example “Order and delivery”. When a headline is used, skip the top divider on the first item.'), ('Add Block', 'Adds a <strong>Collapsible item</strong> to the group. Each item is one row. Add one item for each question or topic.')])

sb_item = '<h2 class="ds-h2">Collapsible item</h2>' + desc('Each item is one row of the group. Set the title, add the content and choose how the row behaves.') + \
    shot('storyblok-collapsible-item.png', 'A Collapsible item in Storyblok with the headline, the content, the Open switch and the two divider switches', pins=((1, '74.8', '47.1', False), (2, '74.8', '57.2', True), (3, '74.8', '72.1', False), (4, '74.8', '80.0', False), (5, '74.8', '87.9', False)), cap='The item: title, content and the three switches.') + \
    ol_parts([('Headline', 'Required. The title of the row. Keep it short and descriptive; for an FAQ, write the question.'), ('Content', 'Add Block. The content of the row: open it with Add Block and choose a content block. See the next step.'), ('Open', 'Off by default. Turn it on to show the row open when the page loads. Use it for the row that helps the user most, for example the first question in a grouped FAQ.'), ('Bottom divider', 'On by default. The line under the row. Rows in a group share it.'), ('Top divider', 'Off by default. The line above the row. Use it for the first row of a list in a panel, or for a single collapsible.')]) + \
    '<h3 class="ds-h3 ds-group">In the component</h3>' + desc('The switches set the same states as the component classes.') + \
    table(['Storyblok', 'Default', 'Component'], [['Open', 'Off', '<code>collapsible-wrap--open</code>'], ['Bottom divider', 'On', 'The default line under the row. Off: <code>collapsible-wrap--no-divider-bottom</code>. The last row in a section loses its line unless <code>collapsible-wrap--divider-bottom</code> is set.'], ['Top divider', 'Off', '<code>collapsible-wrap--divider-top</code>']]) + \
    note('When to switch the dividers on or off is described under <a class="inline-link inline-link--medium inline-link--secondary" href="collapsible.html#layout-dividers">Dividers</a> in Examples &amp; Guidelines: dividers only where they add clarity, none above the first or under the last row of a group, top and bottom for a single collapsible, and none on a colored section.')

sb_content = '<h2 class="ds-h2">Content in a collapsible item</h2>' + desc('The content of an item is a content block. Open <strong>Add Block</strong> under Content and choose <strong>Content</strong>. The block has a rich text editor, so the text can have formatting such as bold, lists and links. The preview shows the row open while it is edited.') + \
    shot('storyblok-collapsible-content.png', 'A Collapsible item with a Content block in Storyblok, the item open in the preview', pins=((2, '74.8', '30.3', True),), cap='A Content block in an item. The preview shows the open row.') + \
    desc('Keep the text short enough to digest. Review the line length (60–90 characters is ideal) under ' + link_large('../foundations/typography.html', 'Typography') + '.')

sb_width = '<h2 class="ds-h2">Section column width</h2>' + desc('The width of the group is set on the section, not on the block. In the section settings, <strong>Column Width Medium</strong> is <code>col-10</code> and <strong>Column Width Large</strong> is <code>col-8</code> for the group in the examples.') + \
    '<div class="sb-tip"><div class="sb-tip__ic"><span class="mo-ic" aria-hidden="true">lightbulb</span></div><div class="sb-tip__body"><h3 class="ds-h3">Pro tip</h3><p class="ds-desc">Use the section column width settings to make the content of a group of collapsibles easier to digest.</p></div></div>'

sb_related = '<h2 class="ds-h2">Related</h2><ul class="ds-bullets"><li><strong>' + link_large('collapsible.html', 'Examples &amp; Guidelines') + '</strong>. When to use a collapsible, the dividers and the best practices.</li><li><strong>' + link_large('collapsible-specifications.html', 'Specifications') + '</strong>. Sizes, tokens and states.</li><li><strong>' + link_large('collapsible-code.html', 'Code') + '</strong>. The markup and the classes.</li></ul>'

sb = [('overview', sb_over), ('add-the-block', sb_add), ('container', sb_cont), ('item', sb_item), ('content', sb_content), ('section-column-width', sb_width), ('related', sb_related)]

C = dict(
    slug=SLUG, title='Collapsible', eyebrow='Components · Layout and content',
    lead='A collapsible is a <strong>row that opens and closes</strong> to show more content, used for FAQ lists and filters. The header can carry a descriptive text, icons, a toggle switch and a number badge. The content animates open.',
    lead_ex='Every example on this page is the real component, not a picture. Figma: ' + fig_link(FIGMA % '535-15947', 'Base / Collapsible') + ', ' + fig_link(FIGMA % '3375-138321', 'Collapsible & Collapsible open') + ', ' + fig_link(FIGMA % '8657-125202', 'Support + Visa mer') + ', ' + fig_link(FIGMA % '23386-26225', 'boxed setup') + ' and, for the Storyblok context, ' + fig_link('https://www.figma.com/design/QYaY33c8HK3xKVLcpnzlh6/Storyblok?node-id=5060-131758', 'Collapsible context examples') + '.',
    lead_spec='Tokens, sizes, measurements, states and requirements. Values come from the live token package and from Figma: ' + fig_link(FIGMA % '535-15947', 'Base / Collapsible') + '.',
    lead_code='How to add a collapsible to a page. The files are <code>components/css/collapsible.css</code> and <code>components/js/collapsible.js</code>.',
    lead_sb='How an editor adds and sets up the Collapsible block in Storyblok. The block is the Storyblok widget for the Collapsible component.', sb=sb,
    select_menu=False,
    css=['collapsible', 'range', 'switch', 'checkbox', 'section'], body_js=['../../components/js/collapsible.js', '../../components/js/range.js'], style=STYLE, ex=ex, spec=spec, code=code, js_ex=JS_EX, js_spec=JS_SPEC, js_code=JS_CODE)

if __name__ == '__main__':
    emit(C)
