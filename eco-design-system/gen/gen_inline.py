from notif import *

SLUG = 'inline'
FIG = fig_link(FIGMA % '13377-35659', 'Inline notification')

STYLE = STYLE + r'''
    .pg-grid { display: grid; gap: 16px 24px; grid-template-columns: minmax(0, 1fr); width: 100%; }
    @media (min-width: 1100px) { .pg-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
    .pg-matrix td { min-width: 300px; }
    .ds-callout__art { padding: 56px 24px 56px 56px; width: 100%; box-sizing: border-box; }
    .ms-inline .measure__obj { width: 480px; max-width: 100%; }'''

playground = '<h2 class="ds-h2">Playground</h2>' + desc('Choose size, status, emphasis and layout and the notification and its code update. The × works; <strong>Show again</strong> brings it back.') + \
    '<div class="ds-playground"><div class="ds-stage ds-stage--center" style="align-items:stretch"><div id="pg-host" style="width:100%;align-self:center"></div></div><div class="ds-controls">' + \
    btn_group('pg-l-sz', 'Size', 'data-pg="size"', [('large', 'Large', True), ('small', 'Small', False)]) + \
    sel_field('pg-l-st', 'sel-pg-l-st', 'Status', 'status', [('info', 'Informational'), ('success', 'Success'), ('warning', 'Warning'), ('error', 'Error')]) + \
    btn_group('pg-l-em', 'Emphasis', 'data-pg="emphasis"', [('strong', 'Strong', True), ('weak', 'Weak', False)]).replace('<div class="ds-field">', '<div class="ds-field" id="f-em">', 1) + \
    btn_group('pg-l-ly', 'Layout', 'data-pg="layout"', [('default', 'Default', True), ('actionable', 'Actionable', False)]).replace('<div class="ds-field">', '<div class="ds-field" id="f-ly">', 1) + \
    btn_group('pg-l-ac', 'Actions', 'data-pg="acts"', [('buttons', 'Buttons', True), ('links', 'Inline links', False)]).replace('<div class="ds-field">', '<div class="ds-field" id="pg-acts-f" hidden>', 1) + \
    btn_group('pg-l-ti', 'Title', 'data-pg="title"', [('off', 'None', True), ('on', 'Title', False)]) + btn_group('pg-l-cl', 'Close button', 'data-pg="closable"', [('on', 'Shown', True), ('off', 'Hidden', False)]) + \
    txt_field('pg-text', 'Text', 'Only 4 left in stock. Delivery in 2–3 days.', 'Text') + icon_field() + \
    txt_field('pg-b2', 'Secondary button', 'Change address', 'Secondary button', 'pg-b2-f', True) + txt_field('pg-b1', 'Primary button', 'Continue', 'Primary button', 'pg-b1-f', True) + \
    txt_field('pg-l1', 'Link 1', 'Delivery terms', 'Link 1', 'pg-l1-f', True) + txt_field('pg-l2', 'Link 2', 'Change address', 'Link 2', 'pg-l2-f', True) + \
    motion_note('The animation when the × is clicked') + '<button type="button" class="btn btn--secondary btn--sm" id="pg-reset" style="align-self:flex-start"><span class="btn__label">Show again</span></button>' + \
    '</div></div><p class="pg-note" id="pg-rule"></p><h3 class="ds-h3">Markup for this selection</h3>' + code_box('pg-code', 'HTML') + \
    note('The markup has no motion. Closing animation is set in <a href="#motion" class="inline-link inline-link--medium inline-link--secondary">Motion</a>.')

action = '<h2 class="ds-h2">In action</h2>' + desc('Two real situations. The notification appears <em>where the work is</em>, replaces the previous one, and stays until the user fixes the problem or closes it.') + \
    '<h3 class="ds-h3 ds-group">Change password (form feedback)</h3>' + desc('Each button submits the form with a different result. The notification replaces the previous one and stays until it is closed.') + \
    '<div class="ds-stage pg-form-stage" style="flex-direction:column;align-items:stretch;gap:16px"><div class="pg-form__region" id="pw-region" aria-live="polite"></div><div class="pg-btns" id="pw-btns"></div></div>' + \
    '<h3 class="ds-h3 ds-group">Quantity (product information)</h3>' + desc('Informational Weak with its own icon. The message follows the quantity.') + \
    '<div class="ds-stage pg-form-stage" style="flex-direction:column;align-items:stretch;gap:16px"><div class="pg-form__region" id="qty-region" aria-live="polite"></div><div class="pg-btns" id="qty-btns"></div></div>'

overview = '<h2 class="ds-h2">Overview</h2>' + desc('An inline notification gives <strong>feedback right where the user is working</strong>: next to a form, a quantity field or a delivery estimate. It stays in the page until the user acts or the state changes. It never disappears by itself.') + \
    desc('It is a task-generated notification. A brief confirmation belongs in a ' + link_large('toast.html', 'Toast') + ', and a message for the whole page or system in a ' + link_large('banner.html', 'Banner') + '. Not sure it is the right component? Start at the ' + link_large('notifications.html', 'Notifications guide') + '.') + \
    three_pages(SLUG, 'an inline notification', 'the values: tokens, sizes, measurements, states and requirements', 'how to build one and the CSS behind it')

usage = '<h2 class="ds-h2">Usage</h2><h3 class="ds-h3 ds-group">When to use</h3>' + desc('Use an inline notification for status that belongs to one place on the page and has to stay. Use it to:') + \
    bullets(['Give feedback on a form: a missing field, a weak password, a declined payment', 'Show helper information next to the content it is about, such as stock or delivery time', 'Offer a way to fix a problem from where it appears, with Actionable buttons or links']) + \
    '<h3 class="ds-h3 ds-group">When not to use</h3><h3 class="ds-h3">Next to the thing it is about</h3>' + desc('An inline notification sits in the region of the work. A banner at the top of the page is for the whole site, and is too far away from a form.') + \
    pair('fig-do-1', 'Do place the notification next to the form it is about.', 'fig-dont-1', 'Do not use a banner for feedback on a form. Use an inline notification instead.') + \
    '<h3 class="ds-h3">Strong for a problem the user must fix</h3>' + desc('Weak is the default, for feedback the user can already see, such as helper information. Strong is for a problem the user must fix. See ' + link_large('notifications.html#emphasis', 'Choosing the emphasis') + '.') + \
    pair('fig-do-2', 'Do use Strong for a problem the user must fix.', 'fig-dont-2', 'Do not use Strong for helper information. Weak is the default.') + \
    '<h3 class="ds-h3">It stays</h3>' + desc('An inline notification never disappears by itself. For a brief confirmation that leaves on its own, use a Toast.') + \
    pair('fig-do-3', 'Do use an inline notification for information that stays.', 'fig-dont-3', 'Do not use it for a brief confirmation. Use a Toast instead.') + \
    '<h3 class="ds-h3 ds-group">Quick reference</h3>' + \
    which([['belongs to one section, form or content block and must stay', 'Inline (this page)'], ['is a short confirmation of an action', lk('toast.html', 'Toast')], ['concerns the whole page or system', lk('banner.html', 'Banner')], ['needs a decision before the user can go on', lk('modal.html', 'Modal')]]) + \
    rules(['Place it next to the thing it is about.', 'Give an Error a way to fix it, in the text or as an action.', 'Use Informational for helper messages such as stock or delivery.', 'Announce it with <code>aria-live</code> when it appears after an action.'],
          ['Use it for a single field. Use the field’s own error message.', 'Use it for a brief confirmation. Use a Toast.', 'Add the Actionable layout to Small.', 'Use the Weaker emphasis. That is Banner only.'])

anatomy = '<h2 class="ds-h2">Anatomy</h2><h3 class="ds-group ds-h3">Inline notification</h3>' + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout" id="i-anat" role="img" aria-label="Anatomy of an inline notification: 1 left edge, 2 status icon, 3 title, 4 text, 5 close, 6 actions"><div class="ds-callout__art"><div id="a-host"></div></div></div></figure></div>' + \
    ol_parts([('Left edge', '2px, in the status color.'), ('Status icon', '24px (Small 20px). Informational may take an icon of its own.'), ('Title', 'Optional. <code>label-sm</code>, uppercase.'), ('Text', '<code>body-sm</code>, 14/20.'), ('Close', 'A Blank icon button, 20px icon.'), ('Actions', 'Actionable (Large only): buttons <strong>or</strong> inline links.')])

variants = '<h2 class="ds-h2">Variants</h2>' + desc('Two sizes, two emphasis levels and two layouts. Pick the size by how much room the message has, and the emphasis by how loud it should be: Weak for feedback the user can already see, Strong for a problem the user must fix. See ' + link_large('notifications.html#emphasis', 'Choosing the emphasis') + '.') + \
    '<h3 class="ds-h3 ds-group">Large</h3>' + desc('48px high with a 24px icon. The default for messages next to forms and content blocks.') + fig_one_id('v-large', None, 'pg-grid') + \
    '<h3 class="ds-h3 ds-group">Small</h3>' + desc('32px high with a 20px icon, for tight spaces such as next to a field. No Actionable layout. Weak exists only for Informational and Warning.') + fig_one_id('v-small', None, 'pg-grid') + \
    '<h3 class="ds-h3 ds-group">Actionable</h3>' + desc('Large only. Buttons under the text, indented 32px so they line up with it. Use it when the user can fix the problem from here.') + fig_one_id('v-act', None, 'pg-grid') + \
    '<h3 class="ds-h3 ds-group">Actionable with inline links</h3>' + desc('The action area holds <strong>either buttons or inline links</strong>, not both. Links suit lighter next steps.') + fig_one_id('v-links', None, 'pg-grid') + \
    '<h3 class="ds-h3 ds-group">Informational with your own icon</h3>' + desc('Informational Weak is white with a blue edge. Like any Informational notification it may carry an icon the author chooses instead of the default <code>info</code>: a Google Material Symbols name, shown as Outlined (Fill 0, Weight 300, Grade 0). Success, Warning and Error always keep their own filled icon.') + fig_one_id('v-icon', None, 'pg-grid')

sizes = '<h2 class="ds-h2">Sizes</h2>' + desc('Large is 48px high with a 24px icon and 12px padding. Small is 32px high with a 20px icon and 4px padding. An inline notification is the same at every breakpoint. All values are under ' + sec_link(SLUG, 'sizes', 'Sizes') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Large</h3>' + fig_one_id('v-s-large') + '<h3 class="ds-h3 ds-group">Small</h3>' + fig_one_id('v-s-small')

layout = '<h2 class="ds-h2">Layout &amp; Appearance</h2><h3 class="ds-h3 ds-group">Alignment</h3>' + desc('The icon, the text and the × sit on one row, top-aligned. In the Actionable layout the buttons or links start 32px from the edge, under the text.') + \
    '<h3 class="ds-h3 ds-group">Placement</h3>' + desc('Next to the thing it is about: above or below a form, beside a quantity field or a delivery estimate. It is part of the page flow and moves the content around it.') + \
    '<h3 class="ds-h3 ds-group">Width</h3>' + desc('An inline notification takes the width of its container.') + \
    '<h3 class="ds-h3 ds-group">Appearance</h3>' + desc('Strong has a tinted background and a 1px outline; Weak is white. Both have a 2px status edge and the elevation <code>b-20</code>. Token names and values are under ' + sec_link(SLUG, 'design-tokens', 'Design Tokens') + ' in Specifications.')

behavior = '<h2 class="ds-h2">Behavior</h2><h3 class="ds-h3 ds-group">Dismissal</h3>' + desc('The × hides the notification with a fade and a height collapse, so no gap is left.') + \
    '<h3 class="ds-h3 ds-group">Persistence</h3>' + desc('It stays until the user acts, the state changes or it is closed. It never auto-hides.') + \
    '<h3 class="ds-h3 ds-group">Hover and focus</h3>' + desc('Only the ×, the buttons and the links have states. They take focus with a visible ring, on keyboard use only. All states are under ' + sec_link(SLUG, 'states', 'States') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Motion</h3>' + desc('Closing is a fade and a collapse: accelerate easing, 150ms. Try other values under <a class="inline-link inline-link--large inline-link--secondary" href="#motion">Motion</a> above, and see ' + sec_link(SLUG, 'motion', 'Motion') + ' in Specifications.')

access = '<h2 class="ds-h2">Accessibility</h2>' + desc('All requirements are listed under ' + sec_link(SLUG, 'accessibility-requirements', 'Accessibility Requirements') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Keyboard support</h3>' + desc('Tab moves to the ×, the buttons and the links, each with a visible focus ring.') + \
    '<h3 class="ds-h3 ds-group">Screen reader support</h3>' + desc('Put the notification in a region with <code>aria-live="polite"</code> (<code>role="alert"</code> for errors that block progress) so it is announced when it appears. The status is carried by the icon and the text, not by color alone.')

related = '<h2 class="ds-h2">Related</h2><ul class="ds-bullets"><li><strong>' + link_large('toast.html', 'Toast') + '</strong>. A brief confirmation that leaves by itself.</li><li><strong>' + link_large('banner.html', 'Banner') + '</strong>. A message for the whole page or system.</li><li><strong>' + link_large('modal.html', 'Modal') + '</strong>. A decision before the user can go on.</li><li><strong>' + link_large('notifications.html', 'Notifications guide') + '</strong>. Which notification to choose.</li></ul>'

references = '<h2 class="ds-h2">References</h2>' + refs([
    ('https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html', 'WCAG 2.2: Status Messages', 'Success criterion 4.1.3.'),
    ('https://www.w3.org/WAI/WCAG22/Understanding/error-identification.html', 'WCAG 2.2: Error Identification', 'Success criterion 3.3.1.'),
    ('https://carbondesignsystem.com/components/notification/usage/', 'Carbon Design System: Notification', 'IBM.'),
    ('https://spectrum.adobe.com/page/in-line-alert/', 'Adobe Spectrum: In-line alert', 'Adobe.')])

ex = [('playground', playground), ('in-action', action), ('overview', overview), ('usage', usage), ('anatomy', anatomy), ('variants', variants), ('sizes', sizes), ('layout', layout), ('behavior', behavior), ('accessibility', access), ('related', related), ('references', references)]

# ---------------------------------------------------------------- Specifications
st_tok = '<h2 class="ds-h2">Design Tokens</h2>' + desc('Resolved from the live token package.') + \
    '<div class="ds-table-wrap"><table class="ds-table" id="tok-table"><thead><tr><th scope="col">Status · emphasis</th><th scope="col">Part</th><th scope="col">Token</th><th scope="col">Value</th></tr></thead><tbody></tbody></table></div>'

st_sizes = '<h2 class="ds-h2">Sizes</h2>' + table(['Property', 'Large', 'Small'], [['Height', '48px', '32px'], ['Padding', '12px', '4px'], ['Icon', '24px', '20px'], ['Left edge', '2px', '2px'], ['Outline (Strong)', '1px, <code>border-{status}-weaker</code>, inside the height', 'Same'], ['Gap icon to text', '8px', '8px'],
    ['Title', '<code>label-sm</code> 14px, 0.56px, bold, uppercase', 'Same'], ['Text', '<code>body-sm</code> 14/20, 0.36px', 'Same'], ['Actionable', 'Indent 32px; buttons 16px below the text, 32px high; link 8px below the buttons', 'Not defined'], ['Shadow', '<code>var(--shadow-elevation-b-20)</code>', 'Same']]) + \
    note('An inline notification is the same at every breakpoint.')

st_meas = '<h2 class="ds-h2">Measurements</h2><h3 class="ds-h3 ds-group">Dimensions</h3>' + desc('The padding of a Large and a Small notification. The shaded area is the padding; the 2px status edge sits outside it. The numbers are read from the component.') + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-fig__stage--flush" style="padding:0;min-height:0"><div class="measure ms-inline" id="ms" role="img" aria-label="Padding of a Large and a Small inline notification"></div></div><figcaption class="ds-fig__cap">A Large and a Small notification at true size.</figcaption></figure></div>' + \
    table(['Attribute', 'Large', 'Small'], [['Padding', '12px', '4px (the header has 2px more on the left)'], ['Icon', '24px', '20px, 2px down'], ['Gap icon to text', '8px', '8px'], ['Left edge', '2px', '2px'], ['Space above buttons', '16px', 'Not defined'], ['Space above links', '16px (8px under buttons)', 'Not defined']]) + \
    '<h3 class="ds-h3 ds-group">Spacing</h3>' + desc('The same distances as spacing tokens.') + table(['Part', 'Value'], [['Padding, Large', '<code>space-12</code>'], ['Padding, Small', '<code>space-4</code>'], ['Icon to text', '<code>space-8</code>'], ['Left edge', '<code>space-2</code>'], ['Actions indent', '<code>space-32</code>'], ['Above the actions', '<code>space-16</code>'], ['Between buttons', '<code>space-8</code>'], ['Between links', '<code>space-8</code> row, <code>space-16</code> column']])

st_elev = '<h2 class="ds-h2">Elevation</h2>' + table(['Part', 'Token', 'Value'], [['Inline notification', '<code>shadow-elevation-b-20</code>', 'Every size and emphasis.']])

st_states = '<h2 class="ds-h2">States</h2>' + desc('Every status in both emphases. Combinations Figma does not define are marked. An inline notification has no hover or focus state of its own; its × and links do.') + \
    toolbar([('ms-l', 'Size', 'data-mx="size"', [('large', 'Large', True), ('small', 'Small', False)]), ('ml-l', 'Layout', 'data-mx="layout"', [('default', 'Default', True), ('actionable', 'Buttons', False), ('links', 'Inline links', False)])]) + \
    '<div class="ds-table-wrap"><table class="ds-table pg-matrix" id="matrix"><thead><tr><th scope="col">Status</th><th scope="col">Strong</th><th scope="col">Weak</th></tr></thead><tbody></tbody></table></div><p class="ds-desc ds-note" id="mx-note"></p>'

st_typo = '<h2 class="ds-h2">Typography</h2>' + table(['Element', 'Token', 'Value'], [['Title (optional)', '<code>label-sm</code>', '14/14, 0.56px, bold, uppercase'], ['Text', '<code>body-sm</code>', '14/20, 0.36px'], ['Inline link', '<code>body-sm</code> (Small)', '14/20'], ['Buttons', '<code>label-md</code> / <code>label-sm</code>', '14/14, 0.42px (mobile), 0.56px (desktop)']]) + note('The type is the same at every breakpoint.')

st_struct = '<h2 class="ds-h2">Structure</h2><h3 class="ds-h3 ds-group">Elements</h3>' + table(['Element', 'Class', 'Notes'], [
    ['Notification', '<code>inline-notification inline-notification--{status} inline-notification--{emphasis}</code>', 'Status: <code>info</code>, <code>success</code>, <code>warning</code>, <code>error</code>. Emphasis: <code>strong</code>, <code>weak</code>. Add <code>--small</code> for Small.'], ['Frame', '<code>__base</code>, <code>__left-border</code>, <code>__container</code>, <code>__inner</code>', 'Edge, outline and padding.'],
    ['Header', '<code>__header</code>, <code>__icon</code>, <code>__text</code>, <code>__title</code>', 'The icon is a <code>material-symbols-outlined</code> span.'], ['Actions', '<code>__actions</code> with <code>__btns</code> or <code>__links</code>', 'Large only. Buttons <strong>or</strong> inline links.'], ['Close', '<code>icon-btn icon-btn--close</code>', 'Optional.']]) + \
    '<h3 class="ds-h3 ds-group">Types</h3>' + desc('Large: Strong and Weak for all four statuses, Default or Actionable. Small: Strong for all four, Weak for Informational and Warning only, Default only.') + \
    '<h3 class="ds-h3 ds-group">Width</h3>' + desc('The width of the container.')

st_motion = '<h2 class="ds-h2">Motion</h2>' + table(['Property', 'Token', 'Value'], [['Close: <code>opacity</code>, <code>height</code>, margin and padding', '<code>--n-close-duration</code>', 'Default <code>duration-fast-3</code> (150ms)'], ['Easing', '<code>--n-close-ease</code>', 'Default <code>ease-accelerate-generic</code>'], ['Height collapse', '<code>data-n-close="fade"</code> on an ancestor turns it off', 'On by default']]) + \
    note('Reduced motion: hidden at once. Compare values in the live Motion section on <a class="inline-link inline-link--medium inline-link--secondary" href="inline.html#motion">Examples &amp; Guidelines</a>.')

st_behavior = '<h2 class="ds-h2">Behavior</h2>' + table(['Input', 'Result'], [['Click ×', 'Hides the notification.'], ['Persistence', 'It stays until the user acts, the state changes or it is closed. It never auto-hides.'], ['Tab', 'The ×, buttons and link take focus with a visible ring.'], ['Inline link', 'Underlined when enabled; on hover the underline goes and the color changes (<code>eco-inline-link</code>, Small).']])

st_access = '<h2 class="ds-h2">Accessibility Requirements</h2>' + table(['Topic', 'Requirement'], [
    ['Announcement', 'Put the notification in a region with <code>aria-live="polite"</code> (<code>role="alert"</code> for errors that block progress) so it is announced when it appears (WCAG 4.1.3).'], ['Status', 'The icon and the text carry the status, not the color alone (WCAG 1.4.1).'], ['Focus', 'The ×, buttons and links have a 2px ring, <code>border-focus</code>, on keyboard use (WCAG 2.4.7).'], ['Reduced motion', 'Hidden without a transition under <code>prefers-reduced-motion: reduce</code>.']])

spec = [('design-tokens', st_tok), ('sizes', st_sizes), ('measurements', st_meas), ('elevation', st_elev), ('states', st_states), ('typography', st_typo), ('structure', st_struct), ('motion', st_motion), ('behavior', st_behavior), ('accessibility-requirements', st_access)]

# ---------------------------------------------------------------- Code
c_basic = '<h2 class="ds-h2">Basic Usage</h2>' + desc('Link the shared files once per page. Never copy the rules into a page.') + table(['Step', 'What to do'], [
    ['1. Link', '<code>&lt;link rel="stylesheet" href="/eco-design-system/notifications.css"&gt;</code> and <code>&lt;script src="/eco-design-system/notifications.js"&gt;&lt;/script&gt;</code>. Link <code>button.css</code> first. The script makes the × work.'], ['2. Markup', 'Copy a recipe below and put it next to the thing it is about.'],
    ['3. Choose', 'Status class, emphasis class (<code>weak</code> is the default), and <code>inline-notification--small</code> for Small.'], ['4. Announce', 'Put it in a region with <code>aria-live="polite"</code> when it appears after an action.']])
c_inline = '<h2 class="ds-h2">Inline notification</h2><div id="recipes"></div>' + note('The markup has no motion. The closing animation is set in <a class="inline-link inline-link--medium inline-link--secondary" href="inline.html#motion">Motion</a> on Examples &amp; Guidelines.')
c_api = '<h2 class="ds-h2">API</h2><h3 class="ds-h3 ds-group">Classes</h3>' + table(['Class', 'Use'], [['<code>inline-notification--{info|success|warning|error}</code>', 'The status.'], ['<code>inline-notification--{strong|weak}</code>', 'The emphasis.'], ['<code>inline-notification--small</code>', 'Small. No Actionable layout.']]) + \
    '<h3 class="ds-h3 ds-group">Custom properties and attributes</h3>' + table(['Name', 'Use'], [['<code>--n-close-ease</code>, <code>--n-close-duration</code>', 'Closing motion. Defaults: <code>ease-accelerate-generic</code>, <code>duration-fast-3</code>.'], ['<code>data-n-close="fade"</code>', 'On the notification or an ancestor: fade only, no height collapse.'], ['<code>n-dismissed</code>', 'Event, bubbles, fired when the notification is hidden.']]) + \
    '<h3 class="ds-h3 ds-group">Things to know</h3>' + bullets(['The × is the Close icon button; the script hides the notification with <code>hidden</code>.', 'Small · Weak exists only for Informational and Warning.', 'Buttons inside a notification are always 32px high, also when <code>button.css</code> is on the page.'])
c_css = '<h2 class="ds-h2">CSS / Tailwind</h2>' + desc('The component is one CSS file and one script, shared by every notification. Link them, never copy them. The code below is read from the files the page links, so it is always what you see.') + '<div id="files"></div>'
code = [('basic-usage', c_basic), ('inline-notification', c_inline), ('api', c_api), ('css-tailwind', c_css, False)]

# ---------------------------------------------------------------- scripts
JS_SAMPLE = JS_PRE + r'''
  var TXT = { info: 'Only 4 left in stock. Delivery in 2–3 days.', success: 'Your password was changed.', warning: 'That password is easy to guess.', error: 'The payment was declined. Check your card details.' };
  function inl(o) { return mk(H.inline(o)); }
  function measureItem(name, el, subjSel, edge) {
    var it = document.createElement('div'); it.className = 'measure__item';
    var nm = document.createElement('span'); nm.className = 'measure__name'; nm.textContent = name;
    var obj = document.createElement('div'); obj.className = 'measure__obj'; obj.appendChild(el);
    var s = subjSel ? $(subjSel, el) : el; s.classList.add('measure__subject');
    if (edge === true) s.setAttribute('data-measure-edge', ''); else if (edge) $(edge, el).setAttribute('data-measure-edge', '');
    ['t', 'b', 'l', 'r'].forEach(function (d) { var i = document.createElement('i'); i.className = 'measure__pad measure__pad--' + d; obj.appendChild(i); });
    [['v', 't'], ['v', 'b'], ['h', 'l'], ['h', 'r']].forEach(function (p) { var b = document.createElement('b'); b.className = 'measure__dim measure__dim--' + p[0] + ' measure__dim--' + p[1]; b.appendChild(document.createElement('span')); obj.appendChild(b); });
    it.appendChild(nm); it.appendChild(obj); return it;
  }
'''

JS_EX = JS_SAMPLE + r'''
  /* Playground */
  var mo;  /* Motion section: re-rendered with the playground selection */
  var pg = { size: 'large', status: 'info', emphasis: 'strong', layout: 'default', acts: 'buttons', title: 'off', closable: 'on' };
  function pgOpts() {
    var o = { size: pg.size, status: pg.status, emphasis: pg.emphasis, text: $('#pg-text').value, closable: pg.closable === 'on' };
    if (pg.status === 'info' && $('#pg-ic').value.trim()) o.icon = $('#pg-ic').value.trim();
    if (pg.title === 'on') o.title = STATUS.filter(function (s) { return s[0] === pg.status; })[0][1];
    if (pg.layout === 'actionable' && pg.size === 'large') {
      if (pg.acts === 'links') o.links = [$('#pg-l1').value, $('#pg-l2').value].filter(Boolean);
      else { o.secondary = $('#pg-b2').value; o.primary = $('#pg-b1').value; }
    }
    return o;
  }
  function renderPg() {
    if (mo) mo.render();
    var small = pg.size === 'small';
    $('#f-ly').hidden = small; $('#f-ic').hidden = pg.status !== 'info';
    var act = !small && pg.layout === 'actionable'; $('#pg-acts-f').hidden = !act;
    ['b2', 'b1'].forEach(function (k) { $('#pg-' + k + '-f').hidden = !act || pg.acts !== 'buttons'; });
    ['l1', 'l2'].forEach(function (k) { $('#pg-' + k + '-f').hidden = !act || pg.acts !== 'links'; });
    var rule = '';
    if (small && pg.emphasis === 'weak' && (pg.status === 'success' || pg.status === 'error')) rule = 'Small · Weak is only defined for Informational and Warning. Shown here anyway to match Large.';
    if (small) rule = rule || 'Small has no Actionable layout.';
    $('#pg-rule').textContent = rule;
    var o = pgOpts(); clear($('#pg-host')).appendChild(inl(o)); $('#pg-code').textContent = H.inline(o);
  }
  DK.wire(pg, renderPg);
  ['#pg-text', '#pg-ic', '#pg-b2', '#pg-b1', '#pg-l1', '#pg-l2'].forEach(function (q) { $(q).addEventListener('input', renderPg); }); $('#pg-reset').addEventListener('click', renderPg);

  /* In action: buttons only */
  function region(host, o) { clear(host); if (o) host.appendChild(inl(o)); }
  function btns(host, list) { list.forEach(function (c) { var b = document.createElement('button'); b.type = 'button'; b.className = 'btn btn--secondary btn--sm'; b.innerHTML = '<span class="btn__label"></span>'; b.firstChild.textContent = c[0]; b.addEventListener('click', c[1]); host.appendChild(b); }); }
  var pw = $('#pw-region');
  btns($('#pw-btns'), [
    ['Submit empty', function () { region(pw, { size: 'large', status: 'error', emphasis: 'strong', title: 'Password missing', text: 'Enter a new password to continue.' }); }],
    ['Too short', function () { region(pw, { size: 'large', status: 'error', emphasis: 'strong', title: 'Too short', text: 'Use at least 8 characters.', links: ['Show requirements', 'Password tips'] }); }],
    ['Weak password', function () { region(pw, { size: 'large', status: 'warning', emphasis: 'strong', title: 'Weak password', text: TXT.warning + ' Choose something less common.' }); }],
    ['Good password', function () { region(pw, { size: 'large', status: 'success', emphasis: 'strong', text: TXT.success }); }]]);
  var qr = $('#qty-region');
  btns($('#qty-btns'), [
    ['Quantity 1', function () { region(qr, { size: 'large', status: 'info', emphasis: 'weak', icon: 'local_shipping', text: 'In stock. Delivery in 2–3 days.' }); }],
    ['Quantity 4', function () { region(qr, { size: 'large', status: 'info', emphasis: 'weak', icon: 'inventory_2', text: 'That is all we have in stock.' }); }],
    ['Quantity 5', function () { region(qr, { size: 'large', status: 'info', emphasis: 'weak', icon: 'inventory_2', text: 'Only 4 in stock. The rest ships when the next delivery arrives, in about 2 weeks.' }); }]]);

  /* Usage figures */
  clear($('#fig-do-1')).appendChild(inl({ size: 'large', status: 'error', emphasis: 'strong', title: 'Payment declined', text: 'Check your card details.', secondary: 'Change card', primary: 'Try again' }));
  clear($('#fig-dont-1')).appendChild(mk(H.banner({ size: 'small', status: 'error', emphasis: 'strong', text: 'Payment declined. Check your card details.' })));
  clear($('#fig-do-2')).appendChild(inl({ size: 'large', status: 'error', emphasis: 'strong', text: 'Enter a new password to continue.' }));
  clear($('#fig-dont-2')).appendChild(inl({ size: 'large', status: 'info', emphasis: 'strong', text: 'Delivery in 2–3 days.' }));
  clear($('#fig-do-3')).appendChild(inl({ size: 'large', status: 'info', emphasis: 'weak', icon: 'local_shipping', text: 'In stock. Delivery in 2–3 days.' }));
  clear($('#fig-dont-3')).appendChild(inl({ size: 'large', status: 'success', emphasis: 'weak', text: 'Copied to clipboard.' }));

  /* Anatomy */
  function rng(el) { return function () { var r = document.createRange(); r.selectNodeContents(el); return r.getBoundingClientRect(); }; }
  var ai = inl({ size: 'large', status: 'error', emphasis: 'strong', title: 'Title', text: 'Body text explains what to do.', secondary: 'Secondary', primary: 'Primary' });
  clear($('#a-host')).appendChild(ai);
  DK.callouts($('#i-anat'), [
    { n: 1, el: $('.inline-notification__left-border', ai), side: 'left', len: 36, at: 'edge' },
    { n: 2, el: $('.inline-notification__icon', ai), side: 'top', len: 40, at: 'center' },
    { n: 3, el: $('.inline-notification__title', ai), side: 'bottom', len: 40 },
    { n: 4, box: rng($('.inline-notification__text', ai)), side: 'top', len: 40 },
    { n: 5, el: $('.icon-btn--close', ai), side: 'top', len: 40, at: 'center' },
    { n: 6, el: $('.inline-notification__actions', ai), side: 'bottom', len: 40 }
  ]);

  /* Variants and sizes */
  STATUS.forEach(function (s) {
    ['strong', 'weak'].forEach(function (e) { $('#v-large').appendChild(inl({ size: 'large', status: s[0], emphasis: e, title: s[1], text: TXT[s[0]] })); });
    $('#v-small').appendChild(inl({ size: 'small', status: s[0], emphasis: 'strong', text: TXT[s[0]] }));
    if (s[0] === 'info' || s[0] === 'warning') $('#v-small').appendChild(inl({ size: 'small', status: s[0], emphasis: 'weak', text: TXT[s[0]] }));
    $('#v-act').appendChild(inl({ size: 'large', status: s[0], emphasis: s[0] === 'error' ? 'strong' : 'weak', title: s[1], text: TXT[s[0]], secondary: 'Secondary', primary: 'Primary' }));
    $('#v-links').appendChild(inl({ size: 'large', status: s[0], emphasis: 'strong', title: s[1], text: TXT[s[0]], links: ['Text link', 'Text link'] }));
  });
  $('#v-icon').appendChild(inl({ size: 'large', status: 'info', emphasis: 'weak', icon: 'local_shipping', text: 'Free delivery on orders over 1 000 kr.' }));
  $('#v-icon').appendChild(inl({ size: 'small', status: 'info', emphasis: 'weak', icon: 'local_shipping', text: 'Delivery in 2–3 days.' }));
  $('#v-s-large').appendChild(inl({ size: 'large', status: 'warning', emphasis: 'weak', title: 'Warning', text: TXT.warning }));
  $('#v-s-small').appendChild(inl({ size: 'small', status: 'warning', emphasis: 'weak', text: TXT.warning }));

  mo = DK.motion({ anchor: 'playground', prefix: 'n-close', rec: { ease: 'accelerate-generic', dur: 'fast-3', collapse: true }, role: 'exit', why: 'Closing removes the element: accelerate easing, fast fade, and the height collapses so no gap is left (eco-motion: element disappears).', preview: function () { return inl(pgOpts()); } });
''' + JS_MOTION_FIX + r'''
  renderPg();
'''

JS_SPEC = JS_SAMPLE + r'''
  DK.tokenTable($('#tok-table tbody'), [
    ['Informational · Strong', 'Background', 'surface-information-weaker'], ['Informational · Strong', 'Outline', 'border-information-weaker'], ['Informational · both', 'Left edge and icon', 'surface-information-default'],
    ['Weak', 'Background', 'surface-raised-primary'], ['All', 'Text', 'text-primary'], ['All', 'Shadow', 'shadow-elevation-b-20'],
    ['Error · Strong', 'Background', 'surface-danger-weaker'], ['Success · Strong', 'Background', 'surface-success-weaker'], ['Warning · Strong', 'Background', 'surface-warning-weaker']]);

  /* Measurements */
  $('#ms').appendChild(measureItem('Large', inl({ size: 'large', status: 'info', emphasis: 'weak', text: 'Message text.' }), '.inline-notification__inner', '.inline-notification__left-border'));
  $('#ms').appendChild(measureItem('Small', inl({ size: 'small', status: 'info', emphasis: 'weak', text: 'Message text.' }), '.inline-notification__inner', '.inline-notification__left-border'));

  /* States */
  var mx = { size: 'large', layout: 'default' };
  function matrix() {
    var tb = clear($('#matrix tbody')), small = mx.size === 'small';
    STATUS.forEach(function (s) {
      var tr = document.createElement('tr'), th = document.createElement('th'); th.scope = 'row'; th.textContent = s[1]; tr.appendChild(th);
      ['strong', 'weak'].forEach(function (e) {
        var td = document.createElement('td');
        if (small && (mx.layout !== 'default' || (e === 'weak' && (s[0] === 'success' || s[0] === 'error')))) { td.innerHTML = '<span class="ds-na">Not defined</span>'; }
        else td.appendChild(inl({ size: mx.size, status: s[0], emphasis: e, title: small ? '' : s[1], text: small ? 'Short message.' : 'Message text.', secondary: mx.layout === 'actionable' ? 'Secondary' : '', primary: mx.layout === 'actionable' ? 'Primary' : '', links: mx.layout === 'links' ? ['Link', 'Link'] : [] }));
        tr.appendChild(td);
      });
      tb.appendChild(tr);
    });
    $('#mx-note').textContent = small ? 'Small has no Actionable layout, and Weak exists only for Informational and Warning.' : 'Large has every combination.';
  }
  $$('[data-mx]').forEach(function (g) { DK.seg(g, function (v) { mx[g.dataset.mx] = v; matrix(); }); });
  matrix();
'''

JS_CODE = JS_PRE + r'''
  function inl(o) { return H.inline(o); }
  DK.recipes($('#recipes'), [
    ['Large · Informational · Strong', inl({ size: 'large', status: 'info', emphasis: 'strong', title: 'Title', text: 'Body text.' })],
    ['Large · Error · Actionable', inl({ size: 'large', status: 'error', emphasis: 'strong', title: 'Payment declined', text: 'Check your card details.', secondary: 'Change card', primary: 'Try again' })],
    ['Large · Informational · Actionable with inline links', inl({ size: 'large', status: 'info', emphasis: 'strong', title: 'Delivery', text: 'Your order ships tomorrow.', links: ['Track order', 'Change address'] })],
    ['Large · Informational · Weak with your own icon', inl({ size: 'large', status: 'info', emphasis: 'weak', icon: 'local_shipping', text: 'Delivery in 2–3 days.' })],
    ['Small · Warning · Weak', inl({ size: 'small', status: 'warning', emphasis: 'weak', text: 'That password is easy to guess.' })]]);
  DK.printFile($('#files'), '../notifications.css', [['CSS: Inline notification', ['inline']], ['CSS: shared icon, close button, link and buttons', ['base']]])
    .then(function () { return DK.printFile($('#files'), '../notifications.js', [['JavaScript: the × of Banner and Inline', ['runtime']]]); });
'''

C = dict(BASE, slug=SLUG, title='Inline notification',
    lead='An inline notification gives <strong>feedback right where the user is working</strong>: next to a form, a quantity field or a delivery estimate. It stays in the page until the user acts or the state changes. It never disappears by itself.',
    lead_ex='The buttons in <a class="inline-link inline-link--xlarge" href="#in-action">In action</a> show the statuses appearing in context. Figma: ' + FIG + '.',
    lead_spec='Tokens, sizes, measurements, states and requirements. Values come from the live token package and from ' + FIG + '.',
    lead_code='How to build an inline notification and the CSS behind it. The files are <code>eco-design-system/notifications.css</code> and <code>notifications.js</code>.',
    ex=ex, spec=spec, code=code, js_ex=JS_EX, js_spec=JS_SPEC, js_code=JS_CODE)
C['body_js'] = BODY + [ICON_PICKER]
C['style'] = STYLE

if __name__ == '__main__':
    emit(C)
