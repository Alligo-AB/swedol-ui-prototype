from notif import *

SLUG = 'toast'
FIG = fig_link(FIGMA % '13377-29321', 'System Toast')

STYLE = STYLE + r'''
    .ds-callout__art { padding: 56px 24px 56px 64px; }
    .ms-toast .measure__obj { width: 375px; max-width: 100%; }'''

playground = '<h2 class="ds-h2">Playground</h2>' + desc('Choose status, emphasis and content and the toast and its code update. Press <strong>Show toast</strong> to see how it enters, stays and leaves in your window.') + \
    '<div class="ds-playground"><div class="ds-stage ds-stage--center" id="pg-stage"><div id="pg-host" style="max-width:100%"></div></div><div class="ds-controls">' + \
    bp_field('pg-l-bp') + \
    sel_field('pg-l-st', 'sel-pg-l-st', 'Status', 'status', [('info', 'Informational'), ('success', 'Success'), ('warning', 'Warning'), ('error', 'Error')]) + \
    btn_group('pg-l-em', 'Emphasis', 'data-pg="emphasis"', [('strong', 'Strong', False), ('weak', 'Weak', True)]) + \
    btn_group('pg-l-ly', 'Layout', 'data-pg="layout"', [('default', 'Default', True), ('actionable', 'Actionable', False)]) + \
    btn_group('pg-l-ac', 'Actions', 'data-pg="acts"', [('buttons', 'Buttons', True), ('links', 'Inline links', False)]).replace('<div class="ds-field">', '<div class="ds-field" id="pg-acts-f" hidden>', 1) + \
    btn_group('pg-l-ti', 'Title', 'data-pg="title"', [('off', 'None', True), ('on', 'Title', False)]) + \
    btn_group('pg-l-ah', 'Auto-hide', 'data-pg="auto"', [('on', 'On', True), ('off', 'Off', False)]) + range_field() + \
    txt_field('pg-text', 'Text', 'Your changes were saved.', 'Text') + icon_field() + \
    txt_field('pg-b2', 'Secondary button', 'Details', 'Secondary button', 'pg-b2-f', True) + txt_field('pg-b1', 'Primary button', 'Undo', 'Primary button', 'pg-b1-f', True) + \
    txt_field('pg-l1', 'Link 1', 'Learn more', 'Link 1', 'pg-l1-f', True) + txt_field('pg-l2', 'Link 2', 'Undo', 'Link 2', 'pg-l2-f', True) + \
    motion_note('The slide-in and slide-out animation') + '<button type="button" class="btn btn--primary btn--sm" id="pg-show" style="align-self:flex-start"><span class="btn__label">Show toast</span></button>' + \
    '</div></div><h3 class="ds-h3">Markup for this selection</h3>' + code_box('pg-code', 'HTML') + \
    note('The markup has no motion. Slide-in and slide-out animation is set in <a href="#motion" class="inline-link inline-link--medium inline-link--secondary">Motion</a>.')

action = '<h2 class="ds-h2">In action</h2>' + desc('Six real situations. Each button fires the toast the way production code would. Dismiss a toast with the ×, by clicking anywhere outside it, or wait for auto-hide. Where a toast offers an action, the action fires a second toast.') + \
    '<div class="ds-stage" id="scenarios"></div>' + note('Resize the window below 640px and trigger a toast again: it now slides in from the top and fills the width.')

overview = '<h2 class="ds-h2">Overview</h2>' + desc('A toast is <strong>short-lived feedback</strong> on something the user just did: saved, copied, failed. It slides in at the edge of the window, says its piece and leaves without blocking the page.') + \
    desc('It is a task-generated notification. System messages that concern the whole page belong in a ' + link_large('banner.html', 'Banner') + ', and messages that must stay next to the content in an ' + link_large('inline.html', 'Inline notification') + '. Not sure it is the right component? Start at the ' + link_large('notifications.html', 'Notifications guide') + '.') + \
    three_pages(SLUG, 'a toast', 'the values: tokens, sizes, measurements, states and requirements', 'how to show a toast from script and the CSS behind it')

usage = '<h2 class="ds-h2">Usage</h2><h3 class="ds-h3 ds-group">When to use</h3>' + desc('Use a toast for a brief message that needs little or no interaction. Use it to:') + \
    bullets(['Respond to a user action: save, send, delete, copy', 'Report a short system event that does not block the work, such as a background sync', 'Offer a quick way forward, such as <em>Retry</em> after an error or <em>Undo</em> after a delete']) + \
    '<h3 class="ds-h3 ds-group">When not to use</h3><h3 class="ds-h3">For feedback on a click, not a banner</h3>' + desc('A toast belongs to the action the user just took. A banner is for the whole page or system and stays until it is closed.') + \
    pair('fig-do-1', 'Do use a toast for the result of a click.', 'fig-dont-1', 'Do not use a banner for the result of a click. Use a toast instead.') + \
    '<h3 class="ds-h3">Weak is the default</h3>' + desc('Weak is white with the status color in the left edge only. It is right for normal feedback, also for a warning or an error. Strong has a tinted background and is used sparingly. A toast disappears, so never make it louder for something the user must notice: show that as a Banner or near the content. See ' + link_large('notifications.html#emphasis', 'Choosing the emphasis') + '.') + \
    pair('fig-do-2', 'Do use Weak for normal feedback.', 'fig-dont-2', 'Do not use Strong for a routine confirmation. Weak is the default.') + \
    '<h3 class="ds-h3">Keep the text short</h3>' + desc('A toast is read in a few seconds. Say what happened in a few words, and put detail somewhere that stays.') + \
    pair('fig-do-3', 'Do say what happened in a few words.', 'fig-dont-3', 'Do not put long text in a toast. It is gone before it is read.') + \
    '<h3 class="ds-h3">A toast does not ask</h3>' + desc('A toast reports something that has happened. When the user must confirm or choose before going on, use a Modal.') + \
    pair('fig-do-4', 'Do report what happened, with an undo if it helps.', 'fig-dont-4', 'Do not ask for confirmation in a toast. Use a Modal instead.') + \
    '<h3 class="ds-h3 ds-group">Quick reference</h3>' + \
    which([['confirms what the user just did, briefly', 'Toast (this page)'], ['confirms an add to cart or wishlist', lk('toast-ecom.html', 'E-Com Toast')], ['belongs to one section and must stay', lk('inline.html', 'Inline')], ['concerns the whole page or system', lk('banner.html', 'Banner')], ['needs a decision before the user can go on', lk('modal.html', 'Modal')]]) + \
    rules(['Confirm what happened in a few words: “Folder created”.', 'Match the status icon to the status color.', 'Put a Retry button inside an error toast.', 'Run the exit animation on every dismissal.'],
          ['Use a toast for a single form field. Use the field’s error message.', 'Put a permanent message in a toast. Use Inline or Banner.', 'Ask for confirmation in a toast. Use a Modal.', 'Stack several toasts. One at a time.'])

anatomy = '<h2 class="ds-h2">Anatomy</h2><h3 class="ds-h3 ds-group">Toast</h3>' + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout" id="t-anat" role="img" aria-label="Anatomy of a toast: 1 status icon, 2 title, 3 text, 4 close, 5 actions, 6 left edge"><div class="ds-callout__art"><div id="a-host"></div></div></div></figure></div>' + \
    ol_parts([('Status icon', '24px, in the status color. Informational may take an icon of its own.'), ('Title', 'Optional. <code>title-sm</code>, bold.'), ('Text', '<code>body-md</code>. One or two short lines.'), ('Close', 'A Blank icon button with a 20px icon.'), ('Actions', 'Actionable only: Secondary and Primary buttons <strong>or</strong> inline links, indented 32px so they line up under the text.'), ('Left edge', '2px, in the status color, full height.')])

variants = '<h2 class="ds-h2">Variants</h2>' + desc('Four statuses in two emphasis levels, each with a Default and an Actionable layout. The status decides the color and the icon; the emphasis decides how loud the toast is.') + bp_toolbar('vb-l') + \
    '<h3 class="ds-h3 ds-group">Strong and Weak</h3>' + desc('<strong>Weak</strong> is the default: white, with the status color in the 2px left edge only. <strong>Strong</strong> has a tinted background and is used sparingly.') + fig_one_id('v-emph', None, 'pg-grid') + \
    '<h3 class="ds-h3 ds-group">Actionable</h3>' + desc('Add buttons and an optional text link below the text, indented 32px to line up under it. Use it when the user needs a way forward, such as <em>Retry</em> after an error.') + fig_one_id('v-act', None, 'pg-grid') + \
    '<h3 class="ds-h3 ds-group">Actionable with inline links</h3>' + desc('The action area holds <strong>either buttons or inline links</strong>, not both. Use links for lighter choices such as <em>Undo</em> or <em>Learn more</em>.') + fig_one_id('v-links', None, 'pg-grid') + \
    '<h3 class="ds-h3 ds-group">Informational with your own icon</h3>' + desc('An Informational toast may carry an icon the author chooses instead of the default <code>info</code>: a Google Material Symbols name, shown as Outlined. Success, Warning and Error keep their own filled icon.') + fig_one_id('v-icon', None, 'pg-grid')

sizes = '<h2 class="ds-h2">Sizes</h2>' + desc('A toast has one size: 375px wide from 640px, and the full width of the window below. Measurements and the position are under ' + sec_link(SLUG, 'sizes', 'Sizes') + ' in Specifications.') + bp_toolbar('sb-l') + fig_one_id('v-size', None, 'pg-stack')

layout = '<h2 class="ds-h2">Layout &amp; Appearance</h2><h3 class="ds-h3 ds-group">Alignment</h3>' + desc('The icon, the text and the × sit on one row, top-aligned. In the Actionable layout the buttons or links start 32px from the left edge of the content, under the text.') + \
    '<h3 class="ds-h3 ds-group">Placement</h3>' + desc('A toast is fixed to the window and always enters from the right: 40px from the top and the right edge from 1024px, 32px below. Below 640px it fills the width and enters from the top. Only one toast is shown at a time; a new one replaces the old. The values are under ' + sec_link(SLUG, 'sizes', 'Sizes') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Width</h3>' + desc('375px, never wider than the window. The text wraps; the toast grows in height.') + \
    '<h3 class="ds-h3 ds-group">Appearance</h3>' + desc('A white or tinted surface, a 2px status edge and the highest shadow (<code>elevation-b-80</code>). Token names and values are under ' + sec_link(SLUG, 'design-tokens', 'Design Tokens') + ' in Specifications.')

behavior = '<h2 class="ds-h2">Behavior</h2><h3 class="ds-h3 ds-group">Dismissal</h3>' + desc('A toast closes with the ×, with a click anywhere outside it, or by itself. Success and Informational auto-hide after 4 seconds. Warning and Error stay until they are dismissed, so the user does not miss them. An Actionable toast closes when one of its actions is chosen.') + \
    '<h3 class="ds-h3 ds-group">One at a time</h3>' + desc('A second toast replaces the first one at once. Do not queue them.') + \
    '<h3 class="ds-h3 ds-group">Hover and focus</h3>' + desc('The ×, the buttons and the links take focus with the visible focus ring, on keyboard use only. Links lose their underline on hover. All states are under ' + sec_link(SLUG, 'states', 'States') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Motion</h3>' + desc('The toast only slides: it enters with decelerate emphasized and leaves with accelerate, both 300ms. Try other values under <a class="inline-link inline-link--large inline-link--secondary" href="#motion">Motion</a> above, and see ' + sec_link(SLUG, 'motion', 'Motion') + ' in Specifications. With reduced motion it appears and leaves without sliding.')

access = '<h2 class="ds-h2">Accessibility</h2>' + desc('All requirements are listed under ' + sec_link(SLUG, 'accessibility-requirements', 'Accessibility Requirements') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Keyboard support</h3>' + desc('Tab moves to the ×, the buttons and the links, each with a visible focus ring. Enter or Space activates the focused control. A toast does not take focus when it appears.') + \
    '<h3 class="ds-h3 ds-group">Screen reader support</h3>' + desc('The toast area is <code>role="status"</code> with <code>aria-live="polite"</code>, so a new toast is announced without moving focus. The status is carried by the icon and the text, not by color alone.')

related = '<h2 class="ds-h2">Related</h2><ul class="ds-bullets"><li><strong>' + link_large('toast-ecom.html', 'E-Com Toast') + '</strong>. Confirms a shopping action: add to cart or wishlist.</li><li><strong>' + link_large('inline.html', 'Inline notification') + '</strong>. Feedback that stays next to the content.</li><li><strong>' + link_large('banner.html', 'Banner') + '</strong>. A message for the whole page or system.</li><li><strong>' + link_large('modal.html', 'Modal') + '</strong>. A decision before the user can go on.</li><li><strong>' + link_large('notifications.html', 'Notifications guide') + '</strong>. Which notification to choose.</li></ul>'

references = '<h2 class="ds-h2">References</h2>' + refs([
    ('https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html', 'WCAG 2.2: Status Messages', 'Success criterion 4.1.3.'),
    ('https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable.html', 'WCAG 2.2: Timing Adjustable', 'Success criterion 2.2.1, for messages that go away by themselves.'),
    ('https://carbondesignsystem.com/components/notification/usage/', 'Carbon Design System: Notification', 'IBM.'),
    ('https://spectrum.adobe.com/page/toast', 'Adobe Spectrum: Toast', 'Adobe.'),
    ('https://material.io/components/snackbars', 'Material Design: Snackbars', 'Google.'),
    ('https://www.sap.com/design-system/fiori-design-web/v1-151/ui-elements/toast-web-component/usage', 'SAP Fiori: Toast', 'SAP.')])

ex = [('playground', playground), ('in-action', action), ('overview', overview), ('usage', usage), ('anatomy', anatomy), ('variants', variants), ('sizes', sizes), ('layout', layout), ('behavior', behavior), ('accessibility', access), ('related', related), ('references', references)]

# ---------------------------------------------------------------- Specifications
st_tok = '<h2 class="ds-h2">Design Tokens</h2>' + desc('Resolved from the live token package.') + \
    '<div class="ds-table-wrap"><table class="ds-table" id="tok-table"><thead><tr><th scope="col">Status · emphasis</th><th scope="col">Part</th><th scope="col">Token</th><th scope="col">Value</th></tr></thead><tbody></tbody></table></div>'

st_sizes = '<h2 class="ds-h2">Sizes</h2><h3 class="ds-h3 ds-group">Dimensions</h3>' + table(['Property', 'Value'], [
    ['Width', '<code>375px</code> from 640px. Below 640px the full viewport width.'], ['Padding', '16px, with 8px between icon and text'], ['Left edge', '2px solid, status color'], ['Shadow', '<code>var(--shadow-elevation-b-80)</code>'],
    ['Actionable footer', 'Indent 32px, 16px above the buttons, buttons 32px high, Primary fills the rest of the row. Or inline links, 16px gap between them. Buttons and links are alternatives.'], ['Z-index', '9999']]) + \
    '<h3 class="ds-h3 ds-group">Position</h3>' + desc('The toast is <code>position: fixed</code> and always enters from the right, except on mobile where it enters from the top.') + \
    table(['Breakpoint', 'Top', 'Right', 'Width', 'Enters from'], [['lg (1024px+)', '40px', '40px', '375px', 'The right'], ['md (769–1023px)', '32px', '32px', '375px', 'The right'], ['sm (640–768px)', '32px', '32px', '375px', 'The right'], ['xs (0–639px)', '0', '0 (left 0)', 'Full viewport width', 'The top']])

st_meas = '<h2 class="ds-h2">Measurements</h2><h3 class="ds-h3 ds-group">Dimensions</h3>' + desc('The padding of the toast. The shaded area is the padding; the 2px status edge sits outside it. The numbers are read from the component. A toast is the same at every breakpoint.') + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-fig__stage--flush" style="padding:0;min-height:0"><div class="measure ms-toast" id="ms" role="img" aria-label="Padding of the toast: 16 on every side"></div></div><figcaption class="ds-fig__cap">An Informational toast at true size.</figcaption></figure></div>' + \
    table(['Attribute', 'Value'], [['Padding', '16px on every side'], ['Left edge', '2px, outside the padding'], ['Gap icon to text', '8px'], ['Gap between title and text', '2px'], ['Close', '24px box, 20px icon, 2px padding']]) + \
    '<h3 class="ds-h3 ds-group">Spacing</h3>' + desc('The same distances as spacing tokens.') + table(['Part', 'Value'], [['Padding', '<code>space-16</code>'], ['Icon to text', '<code>space-8</code>'], ['Title to text', '<code>space-2</code>'], ['Left edge', '<code>space-2</code>'], ['Actions indent', '<code>space-32</code>'], ['Text to actions', '<code>space-16</code>'], ['Between buttons', '<code>space-8</code>'], ['Between links', '<code>space-8</code> row, <code>space-16</code> column']])

st_elev = '<h2 class="ds-h2">Elevation</h2>' + table(['Part', 'Token', 'Value'], [['Toast', '<code>shadow-elevation-b-80</code>', 'The highest bottom shadow: the toast floats above everything except a modal.']])

st_states = '<h2 class="ds-h2">States</h2>' + desc('Every status in both emphasis levels. A toast has no hover or disabled state of its own: the ×, the buttons and the links have. Its lifecycle (enter, visible, exit) is under <a class="inline-link inline-link--large inline-link--secondary" href="#motion">Motion</a>.') + \
    toolbar([('sl-l', 'Layout', 'data-mx="layout"', [('default', 'Default', True), ('actionable', 'Buttons', False), ('links', 'Inline links', False)]), ('sb-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force')]) + \
    '<div class="ds-table-wrap"><table class="ds-table pg-matrix" id="matrix"><thead><tr><th scope="col">Status</th><th scope="col">Strong</th><th scope="col">Weak</th></tr></thead><tbody></tbody></table></div>'

st_typo = '<h2 class="ds-h2">Typography</h2>' + table(['Element', 'Token', 'Mobile and tablet', 'Desktop (769px+)'], [['Title (optional)', '<code>title-sm</code>', '16/18, bold', '16/18, bold'], ['Text', '<code>body-md</code>', '16/22, 0.32px', '17/24, 0.32px'], ['Buttons', '<code>label-md</code> / <code>label-sm</code>', '14/14, 0.42px', '14/14, 0.56px'], ['Inline link', '<code>body-md</code>', '16/22', '17/24']])

st_struct = '<h2 class="ds-h2">Structure</h2><h3 class="ds-h3 ds-group">Elements</h3>' + table(['Element', 'Class', 'Notes'], [
    ['Toast', '<code>toast toast--{status} toast--{emphasis}</code>', 'Status: <code>info</code>, <code>success</code>, <code>warning</code>, <code>error</code>. Emphasis: <code>strong</code>, <code>weak</code>.'], ['Content', '<code>toast__inner</code>, <code>toast__row</code>, <code>toast__body</code>', 'Padding, edge and the icon / text / × row.'],
    ['Icon, title, text', '<code>toast__icon</code>, <code>toast__title</code>, <code>toast__text</code>', 'The icon is a <code>material-symbols-outlined</code> span.'], ['Close', '<code>icon-btn icon-btn--close</code>', 'Blank icon button, <code>aria-label="Close"</code>.'],
    ['Actions', '<code>toast__actions</code> with <code>toast__btns</code> or <code>toast__links</code>', 'Buttons <strong>or</strong> inline links.'], ['Position', '<code>toast-host</code>', 'Added by <code>ECO_N.showToast</code>; fixed, <code>role="status"</code>.']]) + \
    '<h3 class="ds-h3 ds-group">Types</h3>' + desc('Eight combinations: four statuses × Strong and Weak, each Default or Actionable.') + \
    '<h3 class="ds-h3 ds-group">Width</h3>' + desc('375px from 640px, the full width below. Never wider than the window.')

st_motion = '<h2 class="ds-h2">Motion</h2>' + table(['Motion', 'Value'], [
    ['Duration', '<code>var(--duration-medium-2)</code> (300ms) enter and exit; no fade, the toast only slides'], ['Enter easing', '<code>var(--ease-decelerate-emphasized)</code> (<code>cubic-bezier(0.16, 0, 0.16, 1)</code>)'], ['Exit easing', '<code>var(--ease-accelerate-generic)</code> (<code>cubic-bezier(0.36, 0.09, 1, 0.58)</code>)'],
    ['Auto-hide', '4000ms for System Toast'], ['Reduced motion', 'The toast appears and leaves without sliding']]) + \
    note('Compare other easing and duration values in the live Motion section on <a class="inline-link inline-link--medium inline-link--secondary" href="toast.html#motion">Examples &amp; Guidelines</a>.')

st_behavior = '<h2 class="ds-h2">Behavior</h2>' + table(['Input', 'Result'], [
    ['Click ×', 'Runs the exit animation, then removes the toast.'], ['Click outside', 'Same. The listener starts on the next tick so the click that opened the toast does not close it.'], ['Wait', 'Auto-hide after 4 seconds (Success and Informational). Warning and Error stay until dismissed.'],
    ['Tab', 'The × and any button or link take focus with a visible ring.'], ['Inline link', 'Underlined when enabled; on hover the underline goes and the color changes (<code>eco-inline-link</code>, Medium).'], ['Second toast', 'Replaces the first one at once. Only one toast is on screen.']])

st_access = '<h2 class="ds-h2">Accessibility Requirements</h2>' + table(['Topic', 'Requirement'], [
    ['Announcement', 'The toast area is <code>role="status"</code> with <code>aria-live="polite"</code>, so new toasts are announced without moving focus (WCAG 4.1.3).'], ['Status', 'The icon and the text carry the status, not the color alone (WCAG 1.4.1).'],
    ['Focus', 'The ×, buttons and links have a 2px ring, <code>border-focus</code>, on keyboard use (WCAG 2.4.7).'], ['Timing', 'Success and Informational leave after 4 seconds; Warning and Error stay until dismissed. Anything the user must act on does not auto-hide (WCAG 2.2.1).'], ['Reduced motion', 'No slide under <code>prefers-reduced-motion: reduce</code>.']])

spec = [('design-tokens', st_tok), ('sizes', st_sizes), ('measurements', st_meas), ('elevation', st_elev), ('states', st_states), ('typography', st_typo), ('structure', st_struct), ('motion', st_motion), ('behavior', st_behavior), ('accessibility-requirements', st_access)]

# ---------------------------------------------------------------- Code
c_basic = '<h2 class="ds-h2">Basic Usage</h2>' + desc('Link the shared files once per page. Never copy the rules into a page.') + table(['Step', 'What to do'], [
    ['1. Link', '<code>&lt;link rel="stylesheet" href="/eco-design-system/notifications.css"&gt;</code> and <code>&lt;script src="/eco-design-system/notifications.js"&gt;&lt;/script&gt;</code>. Link <code>button.css</code> first.'], ['2. Show a toast', 'Call <code>ECO_N.showToast({ status, text })</code>. The script adds the fixed host, the slide and the dismissal.'],
    ['3. Choose', 'Status <code>info | success | warning | error</code>. Emphasis <code>weak</code> (default) or <code>strong</code> (sparingly).'], ['4. Actions', 'Optional: <code>actions.primary</code> and <code>actions.secondary</code> as buttons, <strong>or</strong> <code>actions.links</code> as inline links.'], ['5. Auto-hide', '<code>autoHide: 4000</code> for a confirmation. Leave it out for a Warning or an Error.']])
c_toast = '<h2 class="ds-h2">Toast</h2><div id="recipes"></div>' + note('The markup has no motion. The slide is set in <a class="inline-link inline-link--medium inline-link--secondary" href="toast.html#motion">Motion</a> on Examples &amp; Guidelines.')
c_api = '<h2 class="ds-h2">API</h2><h3 class="ds-h3 ds-group">Settings of showToast</h3>' + table(['Setting', 'Use'], [
    ['<code>status</code>', '<code>info</code> (default), <code>success</code>, <code>warning</code>, <code>error</code>.'], ['<code>emphasis</code>', '<code>weak</code> (default) or <code>strong</code>.'], ['<code>title</code>, <code>text</code>', 'Optional title and the text.'], ['<code>icon</code>', 'Informational only: a Material Symbols name, shown as Outlined.'],
    ['<code>actions</code>', '<code>{ primary, secondary }</code> (each <code>{ label, onClick }</code>) or <code>{ links: [{ label, onClick }] }</code>.'], ['<code>autoHide</code>', 'Milliseconds; <code>0</code> or empty = stays until dismissed.']]) + \
    '<h3 class="ds-h3 ds-group">Custom properties</h3>' + table(['Name', 'Use'], [['<code>--toast-in-ease</code>, <code>--toast-in-duration</code>', 'Enter. Defaults: <code>ease-decelerate-emphasized</code>, <code>duration-medium-2</code>.'], ['<code>--toast-out-ease</code>, <code>--toast-out-duration</code>', 'Exit. Defaults: <code>ease-accelerate-generic</code>, <code>duration-medium-2</code>.']]) + \
    '<h3 class="ds-h3 ds-group">Things to know</h3>' + bullets(['Only one toast is on screen: <code>showToast</code> replaces the current one.', 'Set the custom properties on <code>&lt;html&gt;</code> or on <code>.toast-host</code>.', '<code>ECO_N.dismissToast()</code> closes the current toast.', 'Buttons inside a toast are always 32px high, also when <code>button.css</code> is on the page.'])
c_css = '<h2 class="ds-h2">CSS / Tailwind</h2>' + desc('The component is one CSS file and one script, shared by every notification. Link them, never copy them. The code below is read from the files the page links, so it is always what you see.') + '<div id="files"></div>'
code = [('basic-usage', c_basic), ('toast', c_toast), ('api', c_api), ('css-tailwind', c_css, False)]

# ---------------------------------------------------------------- scripts
JS_SAMPLE = JS_PRE + r'''
  var DEMO = { info: 'Syncing files in the background…', success: 'Your changes were saved.', warning: 'Poor network connection. Retrying…', error: 'Failed to upload attachment.' };
  function sample(o) { return mk(H.toast(o)); }
  function mkT(status, emphasis, actionable, extra) {
    var o = { status: status, emphasis: emphasis, text: DEMO[status] };
    if (extra && extra.title) o.title = STATUS.filter(function (s) { return s[0] === status; })[0][1];
    if (actionable === 'links') o.links = ['Learn more', 'Undo'];
    else if (actionable) { o.secondary = 'Details'; o.primary = status === 'error' ? 'Retry' : 'Undo'; }
    return sample(o);
  }
'''

JS_EX = JS_SAMPLE + r'''
  /* Playground */
  var pg = { status: 'info', emphasis: 'weak', layout: 'default', acts: 'buttons', title: 'off', auto: 'on' };
  function pgOpts() {
    var o = { status: pg.status, emphasis: pg.emphasis, text: $('#pg-text').value };
    if (pg.status === 'info' && $('#pg-ic').value.trim()) o.icon = $('#pg-ic').value.trim();
    if (pg.title === 'on') o.title = STATUS.filter(function (s) { return s[0] === pg.status; })[0][1];
    if (pg.layout === 'actionable') {
      if (pg.acts === 'links') o.links = [$('#pg-l1').value, $('#pg-l2').value].filter(Boolean);
      else { o.secondary = $('#pg-b2').value; o.primary = $('#pg-b1').value; }
    }
    return o;
  }
  function renderPg() {
    $('#f-ic').hidden = pg.status !== 'info'; $('#pg-time-f').hidden = pg.auto === 'off';
    var act = pg.layout === 'actionable'; $('#pg-acts-f').hidden = !act;
    ['b2', 'b1'].forEach(function (k) { $('#pg-' + k + '-f').hidden = !act || pg.acts !== 'buttons'; });
    ['l1', 'l2'].forEach(function (k) { $('#pg-' + k + '-f').hidden = !act || pg.acts !== 'links'; });
    var o = pgOpts(); clear($('#pg-host')).appendChild(sample(o)); $('#pg-code').textContent = H.toast(o);
  }
  DK.wire(pg, renderPg);
  ['#pg-text', '#pg-ic', '#pg-b2', '#pg-b1', '#pg-l1', '#pg-l2'].forEach(function (q) { $(q).addEventListener('input', renderPg); });
  $('#pg-show').addEventListener('click', function () {
    var o = pgOpts(), a = null;
    if (o.primary || o.secondary) { a = {}; if (o.primary) a.primary = { label: o.primary }; if (o.secondary) a.secondary = { label: o.secondary }; }
    else if (o.links && o.links.length) a = { links: o.links.map(function (t) { return { label: t }; }) };
    N.showToast({ status: o.status, emphasis: o.emphasis, title: o.title, icon: o.icon, text: o.text, actions: a, autoHide: pg.auto === 'on' ? $('#pg-time').value * 1000 : 0 });
  });

  /* In action */
  var SC = [
    { t: 'Save settings', d: 'Success, Weak. Confirms the action and leaves by itself after 4 seconds.', run: function () { N.showToast({ status: 'success', emphasis: 'weak', text: 'Settings saved.', autoHide: 4000 }); } },
    { t: 'Copy to clipboard', d: 'Success, Weak. The shortest useful message and normal feedback.', run: function () { N.showToast({ status: 'success', emphasis: 'weak', text: 'Copied to clipboard.', autoHide: 4000 }); } },
    { t: 'Background sync', d: 'Informational, Weak. Passive status; no action needed.', run: function () { N.showToast({ status: 'info', emphasis: 'weak', text: 'Syncing files in the background…', autoHide: 4000 }); } },
    { t: 'Poor connection', d: 'Warning, Weak. A soft error that can be handled locally. Stays until the user dismisses it or carries on.', run: function () { N.showToast({ status: 'warning', emphasis: 'weak', text: 'Poor network connection. Retrying…', actions: { links: [{ label: 'Check connection' }] } }); } },
    { t: 'Upload failed', d: 'Error, Weak, Actionable. A failed action that can be tried again. Stays on screen with a Retry button. Press Retry to see the success toast that follows.', run: function () {
        N.showToast({ status: 'error', emphasis: 'weak', title: 'Upload failed', text: 'Failed to upload attachment.', actions: { primary: { label: 'Retry', onClick: function () { setTimeout(function () { N.showToast({ status: 'success', text: 'Attachment uploaded.', autoHide: 4000 }); }, 350); } }, secondary: { label: 'Dismiss' } } }); } },
    { t: 'Undo a delete', d: 'Informational, Weak, Actionable. A quick undo inside the toast.', run: function () {
        N.showToast({ status: 'info', emphasis: 'weak', text: 'Address deleted.', autoHide: 6000, actions: { links: [{ label: 'Undo', onClick: function () { setTimeout(function () { N.showToast({ status: 'success', text: 'Address restored.', autoHide: 4000 }); }, 350); } }] } }); } }
  ];
  SC.forEach(function (s) {
    var row = document.createElement('div'); row.className = 'pg-row';
    row.innerHTML = '<div class="pg-row__txt"><b></b><span></span></div>';
    row.querySelector('b').textContent = s.t; row.querySelector('span').textContent = s.d;
    var b = document.createElement('button'); b.type = 'button'; b.className = 'btn btn--primary btn--sm'; b.innerHTML = '<span class="btn__label">Show toast</span>'; b.addEventListener('click', s.run);
    row.appendChild(b); $('#scenarios').appendChild(row);
  });

  /* Usage figures: the do and the don't of each rule are live components */
  clear($('#fig-do-1')).appendChild(sample({ status: 'success', emphasis: 'weak', text: 'Settings saved.' }));
  clear($('#fig-dont-1')).appendChild(mk(H.banner({ size: 'small', status: 'success', emphasis: 'weak', text: 'Settings saved.' })));
  clear($('#fig-do-2')).appendChild(sample({ status: 'success', emphasis: 'weak', text: 'Copied to clipboard.' }));
  clear($('#fig-dont-2')).appendChild(sample({ status: 'success', emphasis: 'strong', text: 'Copied to clipboard.' }));
  clear($('#fig-do-3')).appendChild(sample({ status: 'success', emphasis: 'weak', text: 'Folder created.' }));
  clear($('#fig-dont-3')).appendChild(sample({ status: 'success', emphasis: 'weak', text: 'Your folder was created and is now available to everyone in your organisation. You can change who has access later in the folder settings.' }));
  clear($('#fig-do-4')).appendChild(sample({ status: 'info', emphasis: 'weak', text: 'Address deleted.', links: ['Undo'] }));
  clear($('#fig-dont-4')).appendChild(sample({ status: 'warning', emphasis: 'weak', text: 'Delete this address?', secondary: 'Cancel', primary: 'Delete' }));

  /* Anatomy */
  var at = sample({ status: 'error', emphasis: 'strong', title: 'Upload failed', text: 'Failed to upload attachment.', secondary: 'Details', primary: 'Retry' });
  clear($('#a-host')).appendChild(at);
  function rng(el) { return function () { var r = document.createRange(); r.selectNodeContents(el); return r.getBoundingClientRect(); }; }
  DK.callouts($('#t-anat'), [
    { n: 1, el: $('.toast__icon', at), side: 'top', len: 44, at: 'center' },
    { n: 2, box: rng($('.toast__title', at)), side: 'right', len: 44 },
    { n: 3, box: rng($('.toast__text', at)), side: 'right', len: 44 },
    { n: 4, el: $('.icon-btn--close', at), side: 'top', len: 44, at: 'center' },
    { n: 5, el: $('.toast__actions', at), side: 'bottom', len: 44 },
    { n: 6, box: function () { var r = $('.toast__inner', at).getBoundingClientRect(); return { left: r.left, top: r.top, width: 2, height: r.height }; }, side: 'left', len: 44 }
  ]);

  /* Variants and size */
  STATUS.forEach(function (s) {
    $('#v-emph').appendChild(mkT(s[0], 'strong')); $('#v-emph').appendChild(mkT(s[0], 'weak'));
    $('#v-act').appendChild(mkT(s[0], s[0] === 'error' || s[0] === 'warning' ? 'strong' : 'weak', true, { title: true }));
    $('#v-links').appendChild(mkT(s[0], 'strong', 'links'));
  });
  $('#v-icon').appendChild(sample({ status: 'info', emphasis: 'weak', icon: 'local_shipping', text: 'Your order has shipped.' }));
  $('#v-size').appendChild(sample({ status: 'success', emphasis: 'weak', text: 'Your changes were saved.' }));

  /* Motion (live easing and duration): enter and exit */
  DK.motion({ anchor: 'playground', parts: [{ title: 'Enter', prefix: 'toast-in', rec: { ease: 'decelerate-emphasized', dur: 'medium-2' } }, { title: 'Exit', prefix: 'toast-out', rec: { ease: 'accelerate-generic', dur: 'medium-2' }, exit: true }], collapse: false, role: 'exit',
    why: 'The toast only slides, with no fade. It enters with decelerate emphasized and leaves with accelerate, both Medium 2 (eco-motion: element enters / element disappears).', show: function () { N.showToast({ status: 'success', text: 'Your changes were saved.', autoHide: 4000 }); } });
''' + JS_MOTION_FIX + r'''
  DK.bp(); renderPg();
'''

JS_SPEC = JS_SAMPLE + r'''
  var T = [];
  STATUS.forEach(function (s) {
    var k = s[0] === 'error' ? 'danger' : s[0] === 'info' ? 'information' : s[0];
    T.push([s[1] + ' · Strong', 'Background', 'surface-' + k + '-weaker'], [s[1] + ' · both', 'Left edge and icon', 'surface-' + k + '-default']);
  });
  T.push(['Weak', 'Background', 'surface-raised-primary'], ['All', 'Text', 'text-primary'], ['All', 'Shadow', 'shadow-elevation-b-80']);
  DK.tokenTable($('#tok-table tbody'), T);

  /* Measurements */
''' + r'''
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
  $('#ms').appendChild(measureItem('Toast', sample({ status: 'info', emphasis: 'weak', text: 'Your changes were saved.' }), '.toast__inner', true));
  DK.bp(function () { if (window.ECO_MEASURE) ECO_MEASURE.init(); });

  /* States */
  var mx = { layout: 'default' };
  function matrix() {
    var tb = clear($('#matrix tbody'));
    STATUS.forEach(function (s) {
      var tr = document.createElement('tr'), th = document.createElement('th'); th.scope = 'row'; th.textContent = s[1]; tr.appendChild(th);
      ['strong', 'weak'].forEach(function (e) { var td = document.createElement('td'); td.appendChild(mkT(s[0], e, mx.layout === 'actionable' ? true : mx.layout === 'links' ? 'links' : false)); tr.appendChild(td); });
      tb.appendChild(tr);
    });
  }
  DK.seg($('[data-mx="layout"]'), function (v) { mx.layout = v; matrix(); });
  matrix();
'''

JS_CODE = JS_PRE + r'''
  DK.recipes($('#recipes'), [
    ['Default', H.toast({ status: 'success', emphasis: 'weak', text: 'Your changes were saved.' })],
    ['Actionable error', H.toast({ status: 'error', emphasis: 'weak', title: 'Upload failed', text: 'Failed to upload attachment.', secondary: 'Details', primary: 'Retry' })],
    ['Actionable with inline links', H.toast({ status: 'info', emphasis: 'weak', text: 'Address deleted.', links: ['Undo', 'Learn more'] })],
    ['Show it from script', "ECO_N.showToast({\n  status: 'success',      // info | success | warning | error\n  emphasis: 'weak',       // weak (default) | strong (sparingly)\n  text: 'Your changes were saved.',\n  autoHide: 4000          // 0 = stays until dismissed\n});\n\n// Actionable\nECO_N.showToast({\n  status: 'error', title: 'Upload failed', text: 'Failed to upload attachment.',\n  actions: { primary: { label: 'Retry', onClick: retry }, secondary: { label: 'Dismiss' } }   // or { links: [{ label: 'Undo', onClick: undo }] }\n});"]]);
  DK.printFile($('#files'), '../notifications.css', [['CSS: toast', ['toast']], ['CSS: shared close button, link and buttons', ['base']]])
    .then(function () { return DK.printFile($('#files'), '../notifications.js', [['JavaScript: showToast', ['runtime']]]); });
'''

C = dict(BASE, slug=SLUG, title='Toast',
    lead='A toast is <strong>short-lived feedback</strong> on something the user just did: saved, copied, failed. It slides in, says its piece and leaves without blocking the page.',
    lead_ex='Every example is the real component, and every “Show toast” button fires a real toast in the corner of your window. Figma: ' + FIG + '.',
    lead_spec='Tokens, sizes, measurements, states and requirements. Values come from the live token package and from ' + FIG + '.',
    lead_code='How to show a toast from script and the CSS behind it. The files are <code>eco-design-system/notifications.css</code> and <code>notifications.js</code>.',
    ex=ex, spec=spec, code=code, js_ex=JS_EX, js_spec=JS_SPEC, js_code=JS_CODE)
C['body_js'] = BODY + [ICON_PICKER]
C['style'] = STYLE

if __name__ == '__main__':
    emit(C)
