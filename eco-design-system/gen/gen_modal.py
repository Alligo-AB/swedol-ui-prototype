from notif import *

SLUG = 'modal'
FIG = fig_link(FIGMA % '13377-48335', 'E-Com Modal')

STYLE = STYLE + r'''
    /* demo: the real modal is fixed to the window, so a preview is a static copy inside a stage (a flex item honors z-index even when static: z-index auto keeps it under the sticky nav) */
    .modal-preview { padding: 24px; display: flex; justify-content: center; width: 100%; overflow: hidden; box-sizing: border-box; }
    .modal-preview .modal { position: static; transform: none; top: auto; left: auto; max-width: 100%; max-height: none; height: auto; animation: none; z-index: auto; }
    body[data-bp="mobile"] .modal-preview .modal { width: 375px; }
    body[data-bp="mobile"] .modal-preview .modal--small { width: 343px; }   /* a 375px viewport minus 16px side margins */   /* the forced Mobile preview: Large fills the window in real use, here it is as wide as a phone */
    /* the full-screen Large of mobile (xs): a phone-sized screen in the figure (the real one is 100dvh) */
    body[data-bp="mobile"] .modal-preview--screen { height: 560px; width: 375px; max-width: 100%; margin-inline: auto; padding: 0; align-items: stretch; }
    body[data-bp="mobile"] .modal-preview--screen .modal { height: 100%; width: 100%; }
    @media (max-width: 639px) { body:not([data-bp]) .modal-preview--screen { height: 560px; padding: 0; align-items: stretch; } body:not([data-bp]) .modal-preview--screen .modal { height: 100%; } }
    .ds-callout__art { padding: 0; }
    #m-anat .ds-callout__art { padding: 56px 44px 72px 60px; max-width: 100%; box-sizing: border-box; background: var(--color-surface-opacity-black-20); }
    #m-anat .modal-preview { padding: 0; }
    .ms-modal .modal-preview { padding: 0; width: auto; overflow: visible; }'''

playground = '<h2 class="ds-h2">Playground</h2>' + desc('Choose size, label and content and the preview and its code update. Press <strong>Open modal</strong> to open the real one over this page.') + \
    '<div class="ds-playground"><div class="ds-stage ds-stage--center" style="padding:0"><div class="modal-preview" id="pg-host"></div></div><div class="ds-controls">' + \
    bp_field('pg-l-bp') + btn_group('pg-l-sz', 'Size', 'data-pg="size"', [('small', 'Small', True), ('large', 'Large', False)]) + \
    btn_group('pg-l-lb', 'Label', 'data-pg="label"', [('off', 'None', True), ('on', 'Label', False)]) + \
    txt_field('pg-title', 'Title', 'Delete this address?', 'Title') + txt_field('pg-body', 'Body', 'The address is removed from your address book. You cannot undo this.', 'Body') + \
    txt_field('pg-cancel', 'Cancel button', 'Cancel', 'Cancel button') + txt_field('pg-ok', 'Primary button', 'Delete', 'Primary button') + motion_note('The fade in and out') + \
    '<button type="button" class="btn btn--primary btn--sm" id="pg-open" style="align-self:flex-start"><span class="btn__label">Open modal</span></button>' + \
    '</div></div><p class="pg-note" id="pg-log" aria-live="polite"></p><h3 class="ds-h3">Markup for this selection</h3>' + code_box('pg-code', 'HTML')

action = '<h2 class="ds-h2">In action</h2>' + desc('Three situations that really need a decision. The line under the list tells you how the last modal was closed, because a modal must close in all of these ways: the ×, the ESC key and a click on the overlay.') + \
    '<div class="ds-stage" id="scenarios"></div><p class="pg-note" id="log" aria-live="polite">No modal opened yet.</p>'

overview = '<h2 class="ds-h2">Overview</h2>' + desc('A modal is the <strong>most disruptive</strong> notification. It blocks the page until the user makes a decision, so use it only when the user must confirm or choose before going on.') + \
    desc('It is shown over a dimmed page and it always closes with the ×, the ESC key and a click on the overlay. Feedback belongs in a ' + link_large('toast.html', 'Toast') + ', status in context in an ' + link_large('inline.html', 'Inline notification') + '. Not sure it is the right component? Start at the ' + link_large('notifications.html', 'Notifications guide') + '.') + \
    three_pages(SLUG, 'a modal', 'the values: tokens, sizes, measurements and requirements', 'how to open a modal from script and the CSS behind it')

usage = '<h2 class="ds-h2">Usage</h2><h3 class="ds-h3 ds-group">When to use</h3>' + desc('Use a modal when the decision cannot wait. Use it to:') + \
    bullets(['Confirm a destructive action, such as deleting an account or an address', 'Ask for a choice that the user must make before going on', 'Show crucial information the user must not miss, such as updated terms']) + \
    '<h3 class="ds-h3 ds-group">When not to use</h3><h3 class="ds-h3">For a decision, not for feedback</h3>' + desc('A modal stops the user. Feedback on something that has already happened does not need that: use a Toast.') + \
    pair('fig-do-1', 'Do use a modal for a decision the user must make.', 'fig-dont-1', 'Do not use a modal for feedback. Use a Toast instead.', 'modal-preview') + \
    '<h3 class="ds-h3">Name the action</h3>' + desc('The primary button says what will happen: “Delete”, not “OK”. The cancel button says how to back out.') + \
    pair('fig-do-2', 'Do name the action on the button.', 'fig-dont-2', 'Do not use a vague label such as “OK”.', 'modal-preview') + \
    '<h3 class="ds-h3 ds-group">Quick reference</h3>' + \
    which([['needs a confirmation or a choice before the user can continue', 'Modal (this page)'], ['confirms what happened, briefly', lk('toast.html', 'Toast')], ['is status information in page context', lk('inline.html', 'Inline')], ['concerns the whole page or system', lk('banner.html', 'Banner')]]) + \
    rules(['Ask one clear question and give one primary action.', 'Name the action on the button: “Delete”, not “OK”.', 'Close on ×, ESC and a click on the overlay, every time.', 'Move focus into the dialog and back to the opener on close.', 'Start with Small; use Large when the task needs more work area, at every breakpoint.'],
          ['Use a modal for feedback. Use a Toast.', 'Use it for status in page context. Use Inline.', 'Open one on page load.', 'Open a modal from a modal.', 'Use Large only because the screen is large or narrow, or the text is long.'])

anatomy = '<h2 class="ds-h2">Anatomy</h2><h3 class="ds-h3 ds-group">Modal</h3>' + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout" id="m-anat" role="img" aria-label="Anatomy of a modal: 1 label, 2 title, 3 close, 4 body, 5 cancel, 6 primary action, 7 overlay"><div class="ds-callout__art"><div class="modal-preview" id="a-host"></div></div></div></figure></div>' + \
    ol_parts([('Label', 'Optional. <code>alt-label-sm</code>, uppercase, in <code>text-secondary</code>.'), ('Title', '<code>title-md</code>, bold.'), ('Close', 'A Blank icon button, 20px icon. Always present.'), ('Body', '<code>body-md</code>, <code>text-secondary</code>.'), ('Cancel', 'A Blank button, 32px high.'), ('Primary action', 'A Primary button that fills the rest of the row.'), ('Overlay', '<code>surface-opacity-black-20</code>, covers the page. The dimmed area in the figure.')])

variants = '<h2 class="ds-h2">Variants</h2>' + desc('A modal has no status or emphasis. It varies in <strong>size</strong> (under Sizes) and in whether it carries a <strong>label</strong>.') + bp_toolbar('vb-l') + \
    '<h3 class="ds-h3 ds-group">Without a label</h3>' + desc('The default: a title, a body and two buttons.') + fig_one_id('v-nolabel', None, 'modal-preview') + \
    '<h3 class="ds-h3 ds-group">With a label</h3>' + desc('A small uppercase label above the title names the area the question belongs to, such as “Account” or “Cart”.') + fig_one_id('v-label', None, 'modal-preview')

SETUP = table(['', 'Desktop (769px+)', 'Tablet, sm (640–768px)', 'Mobile, xs (below 640px)'], [
    ['Figma breakpoint', 'XLarge-Large-Medium', 'Small', 'XSmall (Large and Small only)'],
    ['Small', '440px wide, centered', '440px wide (adapts to the available width), centered', 'Centered card, height by content, <strong>at least 16px side margin</strong>: max width 440px; <strong>343px on a 375px viewport</strong>'],
    ['Large', '705px wide, centered', '576px wide (adapts to the available width), centered', '<strong>Fills the whole screen</strong> (375 × 100dvh): content on top, buttons pinned to the bottom'],
    ['Height', 'By content, limited by the available screen height', 'By content, limited by the available screen height', 'Small: by content, limited by the screen height. Large: 100dvh'],
    ['Padding', '24px', '24px', '16px'],
    ['Type', 'Desktop sizes (label 14, title 20, body 17)', 'Mobile sizes (label 12, title 18, body 16)', 'Mobile sizes'],
    ['Space above the buttons', '32px', '24px', '24px'],
    ['Overlay', 'Dims the page', 'Dims the page', 'Small: dims the page. Large: covers it completely']])

sizes = '<h2 class="ds-h2">Sizes</h2>' + desc('The modal comes in two sizes to choose between: <strong>Small</strong> and <strong>Large</strong>. Choose by the user’s task and need for work area. The breakpoint does not change that choice: it decides how the chosen size is adapted to the screen.') + \
    '<h3 class="ds-h3 ds-group">Small: short decisions and simple content</h3>' + desc('Use Small when the user is to make a quick, bounded decision or take in short information. The content is easy to overview and needs no extensive scrolling. Examples:') + \
    bullets(['Confirm or cancel an action, such as removing a product.', 'Approve a message that needs an active approval.', 'Choose between a few simple options.']) + \
    '<h3 class="ds-h3 ds-group">Large: tasks that need a work area</h3>' + desc('Use Large when the user needs more room to read, choose or enter information. Examples:') + \
    bullets(['Fill in a more extensive form.', 'Search or choose in a longer list.', 'Configure a product with several options.', 'Handle content with a more complex layout.']) + \
    '<h3 class="ds-h3 ds-group">Rules for choosing a size</h3>' + \
    bullets(['<strong>Start with Small.</strong> Use Large when the task needs more work area.', 'Do not choose Large only because the screen is large or the text is long.', 'Choose Large if Small makes the content cramped, hard to overview or hard to work with, for example when it needs a lot of scrolling or gives too little room for input.', 'Keep the same size choice across breakpoints for the same task. The responsive presentation adapts without changing what the modal is used for.', 'Do not use Large for a short confirmation only because the screen is narrow.']) + \
    '<p class="ds-desc"><strong>Rule of thumb:</strong> Small for short decisions. Large for tasks that need more work area.</p>' + \
    '<h3 class="ds-h3 ds-group">Responsive behavior</h3>' + desc('The breakpoint controls how the chosen size is presented. The table sums up the three setups (the Figma breakpoint groups); exact values are under ' + sec_link(SLUG, 'sizes', 'Sizes') + ' in Specifications. The figures below follow the Breakpoint toolbar.') + SETUP + \
    '<h3 class="ds-h3 ds-group">Desktop (XLarge, Large and Medium breakpoints)</h3>' + desc('Small is a compact dialog. Large is a wider work area. The height follows the content and is limited by the available screen height.') + \
    '<h3 class="ds-h3 ds-group">Tablet (Small breakpoint, 640–768px)</h3>' + desc('The same usage rules apply, but the width adapts to the available area. Both sizes keep their side margins.') + \
    '<h3 class="ds-h3 ds-group">Mobile (XSmall, below 640px)</h3>' + bullets(['<strong>Small:</strong> a height that fits the content and a <strong>maximum width of 440px</strong>. The dialog is centered with at least 16px side margin on each side. On narrower screens the width adapts to the available space: on a 375px viewport it is at most 343px wide, so 343px is not a fixed width for the whole breakpoint.', '<strong>Large:</strong> a full-screen presentation for tasks that need a larger work area. Long content scrolls, and the layout has to work with the keyboard open.']) + \
    bp_toolbar('sb-l') + \
    '<h3 class="ds-h3">Small</h3>' + fig_one_id('v-s-small', None, 'modal-preview') + '<h3 class="ds-h3">Large</h3>' + fig_one_id('v-s-large', None, 'modal-preview modal-preview--screen') + \
    note('Choose <strong>Mobile</strong> in the Breakpoint toolbar to see Large as a full-screen view (a 375 × 560px screen here; the real one is 100dvh). Under Window the figure follows the width of your window.') + \
    '<h3 class="ds-h3 ds-group">Common layout rules</h3>' + \
    bullets(['Small and Large do not have fixed heights. Avoid unnecessary empty space, except in the full-screen view on mobile.', 'Limit the height to the available screen area and allow scroll when the content does not fit.', 'Make sure the content and the actions can be reached in landscape orientation and when the keyboard is open.', 'A short dialog must not fill the whole screen width and at the same time be vertically centered. A centered dialog uses side margins; a full-width bottom sheet is a separate presentation pattern, not a Small modal.', 'Use a clear title and button labels that name the action, such as Cancel and Delete.']) + \
    note('The footer is not sticky: when the content is taller than the screen, the whole panel scrolls, buttons included. On a full-screen Large with short content the buttons sit at the bottom of the screen.')

layout = '<h2 class="ds-h2">Layout &amp; Appearance</h2><h3 class="ds-h3 ds-group">Alignment</h3>' + desc('The label and the title sit on the left with the × on the right, top-aligned. The buttons are on one row at the bottom: Cancel on the left, and the Primary button fills the rest.') + \
    '<h3 class="ds-h3 ds-group">Placement</h3>' + desc('Desktop and tablet: the modal is centered in the window over a dimmed overlay. Mobile (below 640px): Small stays a centered card with side margins; Large is not centered, they fill the whole screen. See the table and the layout rules under <a class="inline-link inline-link--large inline-link--secondary" href="#sizes">Sizes</a>.') + \
    '<h3 class="ds-h3 ds-group">Width</h3>' + desc('Small 440px (on mobile too: max width 440px, never closer than 16px to the screen edges, so 343px on a 375px viewport). Large 705px on desktop, 576px on tablet, full screen on mobile.') + \
    '<h3 class="ds-h3 ds-group">Appearance</h3>' + desc('A white panel with the highest shadow, over a 20% black overlay. Token names and values are under ' + sec_link(SLUG, 'design-tokens', 'Design Tokens') + ' in Specifications.')

behavior = '<h2 class="ds-h2">Behavior</h2><h3 class="ds-h3 ds-group">Dismissal</h3>' + desc('A modal always closes in three ways: the ×, the ESC key and a click on the overlay. A click inside the panel does not close it.') + \
    '<h3 class="ds-h3 ds-group">Focus</h3>' + desc('When the modal opens, focus moves into the dialog and the page scroll is locked. Tab and Shift+Tab stay inside the dialog. On close, focus returns to the button that opened it.') + \
    '<h3 class="ds-h3 ds-group">On mobile (XSmall)</h3>' + desc('Small is a centered card that keeps at least 16px to the screen edges and has the height of its content; if the content grows beyond the screen, the card gets a maximum height and scrolls inside. Large fills the screen: the content scrolls, the buttons stay pinned to the bottom, and the layout has to work in landscape and when the keyboard is open. The choice between them is under <a class="inline-link inline-link--large inline-link--secondary" href="#sizes">Sizes</a>.') + \
    '<h3 class="ds-h3 ds-group">Hover and focus</h3>' + desc('Buttons and the × take focus with a visible ring, on keyboard use only. All values are under ' + sec_link(SLUG, 'behavior', 'Behavior') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Motion</h3>' + desc('The overlay fades; the panel fades and moves 64px, up when it comes in (200ms, decelerate emphasized) and down when it leaves (150ms, accelerate): a modal closes faster than it opens. Try other values under <a class="inline-link inline-link--large inline-link--secondary" href="#motion">Motion</a> above, and see ' + sec_link(SLUG, 'motion', 'Motion') + ' in Specifications. With reduced motion there is no fade.')

access = '<h2 class="ds-h2">Accessibility</h2>' + desc('All requirements are listed under ' + sec_link(SLUG, 'accessibility-requirements', 'Accessibility Requirements') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Keyboard support</h3>' + desc('Tab and Shift+Tab move between the controls and stay inside the dialog. Esc closes it. Enter or Space activates the focused button.') + \
    '<h3 class="ds-h3 ds-group">Screen reader support</h3>' + desc('The panel is <code>role="dialog"</code> with <code>aria-modal="true"</code> and <code>aria-labelledby</code> pointing at the title, so the dialog is announced with its name.')

related = '<h2 class="ds-h2">Related</h2><ul class="ds-bullets"><li><strong>' + link_large('toast.html', 'Toast') + '</strong>. Feedback on something that has happened.</li><li><strong>' + link_large('inline.html', 'Inline notification') + '</strong>. Status that stays next to the content.</li><li><strong>' + link_large('banner.html', 'Banner') + '</strong>. A message for the whole page or system.</li><li><strong>' + link_large('notifications.html', 'Notifications guide') + '</strong>. Which notification to choose.</li></ul>'

references = '<h2 class="ds-h2">References</h2>' + refs([
    ('https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/', 'WAI-ARIA Authoring Practices: Dialog (Modal)', 'Keyboard, focus and roles.'),
    ('https://www.w3.org/WAI/WCAG22/Understanding/focus-order.html', 'WCAG 2.2: Focus Order', 'Success criterion 2.4.3.'),
    ('https://carbondesignsystem.com/components/modal/usage/', 'Carbon Design System: Modal', 'IBM.'),
    ('https://m3.material.io/components/dialogs/overview', 'Material Design 3: Dialogs', 'Google.')])

ex = [('playground', playground), ('in-action', action), ('overview', overview), ('usage', usage), ('anatomy', anatomy), ('variants', variants), ('sizes', sizes), ('layout', layout), ('behavior', behavior), ('accessibility', access), ('related', related), ('references', references)]

# ---------------------------------------------------------------- Specifications
st_tok = '<h2 class="ds-h2">Design Tokens</h2>' + desc('Resolved from the live token package.') + \
    '<div class="ds-table-wrap"><table class="ds-table" id="tok-table"><thead><tr><th scope="col">Part</th><th scope="col">Role</th><th scope="col">Token</th><th scope="col">Value</th></tr></thead><tbody></tbody></table></div>'

st_sizes = '<h2 class="ds-h2">Sizes</h2><h3 class="ds-h3 ds-group">Setup per breakpoint</h3>' + desc('Two sizes to choose between, Small and Large (see Sizes on Examples &amp; Guidelines). The modal has three setups, one per Figma breakpoint group. Tablet (sm) is not the desktop setup and not the mobile one: it has the narrower Large (576px) and the mobile type, but still a centered card.') + SETUP + \
    note('The panel is never wider than the window: <code>max-width: calc(100vw - 32px)</code> and <code>max-height: calc(100dvh - 32px)</code>; longer content scrolls inside the panel. On mobile Small keeps 16px to the edges (<code>max-width: calc(100vw - 32px)</code>, 343px on a 375px viewport). Large is <code>top: 0; left: 0; width: 100%; height: 100dvh; max-width: none</code>, so it has no margin to the screen.')

st_meas = '<h2 class="ds-h2">Measurements</h2><h3 class="ds-h3 ds-group">Dimensions</h3>' + desc('The padding of the modal panel. The numbers are read from the component.') + bp_toolbar('mb-l') + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-fig__stage--flush" style="padding:0;min-height:0"><div class="measure ms-modal" id="ms" role="img" aria-label="Padding of a Small modal"></div></div><figcaption class="ds-fig__cap">A Small modal at true size. Change the Breakpoint to see the mobile values.</figcaption></figure></div>' + \
    table(['Attribute', 'Desktop (769px+) and tablet', 'Mobile (below 640px)'], [['Padding', '24px', '16px'], ['Space above the buttons', '32px (tablet: 24px)', '24px'], ['Header gap, label to title', '8px', '8px'], ['Title to body', '8px (desktop 8px)', '8px'], ['Gap between the buttons', '8px', '8px'], ['Buttons', '32px high', '32px high']]) + \
    '<h3 class="ds-h3 ds-group">Spacing</h3>' + desc('The same distances as spacing tokens.') + table(['Part', 'Value'], [['Padding, tablet and desktop', '<code>space-24</code>'], ['Padding, mobile', '<code>space-16</code>'], ['Above the buttons, desktop', '<code>space-32</code>'], ['Above the buttons, mobile', '<code>space-24</code>'], ['Label, title and body gaps', '<code>space-8</code>'], ['Between the buttons', '<code>space-8</code>'], ['Header to ×', '<code>space-12</code>']])

st_elev = '<h2 class="ds-h2">Elevation</h2>' + table(['Part', 'Token', 'Value'], [['Panel', '<code>shadow-elevation-b-100</code>', 'The highest bottom shadow.'], ['Overlay', '<code>surface-opacity-black-20</code>', 'Dims the page behind the panel. Z-index 9998; the panel is 9999.']])

st_typo = '<h2 class="ds-h2">Typography and spacing</h2>' + table(['Element', 'Desktop (769px+)', 'Tablet and mobile'], [
    ['Label', '<code>alt-label-sm</code> 14/14, 0.56px, 500, uppercase', '12/12, 0.48px'], ['Title', '<code>title-md</code> 20/24, bold', '18/22, bold'], ['Body', '<code>body-md</code> 17/24, 0.32px', '16/22, 0.32px'],
    ['Buttons', '32px high, <code>label-sm</code> 14px, 0.56px', '32px high, 14px, 0.42px'], ['Space above buttons', '32px', '24px'], ['Gap label to title, header to body', '8px', '8px']])

st_struct = '<h2 class="ds-h2">Structure</h2><h3 class="ds-h3 ds-group">Elements</h3>' + table(['Element', 'Class', 'Notes'], [
    ['Overlay', '<code>modal-overlay</code>', 'Fixed, covers the page.'], ['Panel', '<code>modal modal--small|large</code>', '<code>role="dialog"</code>, <code>aria-modal="true"</code>, <code>aria-labelledby</code>.'], ['Header', '<code>modal__header</code>, <code>modal__header-text</code>', 'Label, title and the ×.'],
    ['Label, title, body', '<code>modal__label</code>, <code>modal__title</code>, <code>modal__body</code>', 'The label is optional.'], ['Footer', '<code>modal__footer</code>', 'Blank Cancel and Primary buttons.'], ['Close', '<code>icon-btn icon-btn--close</code>', 'Always present.']]) + \
    '<h3 class="ds-h3 ds-group">Types</h3>' + desc('Two sizes: Small and Large. With or without a label. No status and no emphasis.') + \
    '<h3 class="ds-h3 ds-group">Width</h3>' + desc('See Sizes above.')

st_motion = '<h2 class="ds-h2">Motion</h2>' + table(['Motion', 'Property', 'Duration', 'Easing'], [['Enter', 'Overlay: <code>opacity</code>. Panel: <code>opacity</code> and <code>translate</code> from 64px below (<code>space-64</code>) to 0', '<code>duration-fast-4</code> (200ms), <code>--modal-in-duration</code>', '<code>ease-decelerate-emphasized</code>, <code>--modal-in-ease</code>'], ['Exit', 'Overlay: <code>opacity</code>. Panel: <code>opacity</code> and <code>translate</code> from 0 to 64px below (<code>space-64</code>)', '<code>duration-fast-3</code> (150ms), <code>--modal-out-duration</code>', '<code>ease-accelerate-generic</code>, <code>--modal-out-ease</code>']]) + \
    note('A short move (64px) with the fade, no scale. <strong>Why 64px, and why no token:</strong> the move is short (a small share of the view), so it uses the Fast durations of <code>eco-motion</code>; 64px is a <strong>trial</strong> (24px was the first value): it is a clear lift, and still a short move, so the Fast durations apply. The value is <code>space-64</code>, an existing spacing token, written in the keyframes. There is no distance token and no custom property for it: Carbon, Adobe Spectrum and Atlassian keep duration and easing as the motion tokens and leave the travel distance to the component (Atlassian puts it inside a per-component token such as <code>motion.modal.enterModal</code>). Add a shared distance scale only if a second component needs the same move. The panel uses <code>translate</code>, not <code>transform</code>, so the centering is untouched. The exit is shorter than the enter and accelerates, as when an element disappears (eco-motion); Material, Carbon and Atlassian also close faster than they open. The script adds <code>is-leaving</code> and removes the dialog when the animation has run. Reduced motion: no fade, removed at once. Compare other values in the live Motion section on <a class="inline-link inline-link--medium inline-link--secondary" href="modal.html#motion">Examples &amp; Guidelines</a>.')

st_behavior = '<h2 class="ds-h2">Behavior</h2>' + table(['Input', 'Result'], [
    ['Click ×', 'Closes the modal.'], ['ESC', 'Closes the modal.'], ['Click the overlay', 'Closes the modal. A click inside the panel does not.'], ['Open', 'Focus moves into the dialog. Page scroll is locked (<code>body.has-modal</code>).'], ['Tab / Shift+Tab', 'Stays inside the dialog.'],
    ['Close', 'Focus returns to the button that opened it.'], ['Markup', '<code>role="dialog"</code>, <code>aria-modal="true"</code>, <code>aria-labelledby</code> pointing at the title.']])

st_access = '<h2 class="ds-h2">Accessibility Requirements</h2>' + table(['Topic', 'Requirement'], [
    ['Markup', '<code>role="dialog"</code>, <code>aria-modal="true"</code>, <code>aria-labelledby</code> pointing at the title.'], ['Focus', 'Moves into the dialog on open, is trapped inside it and returns to the opener on close (WCAG 2.4.3). The ring is 2px, <code>border-focus</code> (WCAG 2.4.7).'],
    ['Close', 'Three ways, always: ×, ESC and the overlay.'], ['Scroll', 'The page behind does not scroll while the modal is open.'], ['Reduced motion', 'No fade under <code>prefers-reduced-motion: reduce</code>.']])

spec = [('design-tokens', st_tok), ('sizes', st_sizes), ('measurements', st_meas), ('elevation', st_elev), ('typography', st_typo), ('structure', st_struct), ('motion', st_motion), ('behavior', st_behavior), ('accessibility-requirements', st_access)]

# ---------------------------------------------------------------- Code
c_basic = '<h2 class="ds-h2">Basic Usage</h2>' + desc('Link the shared files once per page. Never copy the rules into a page.') + table(['Step', 'What to do'], [
    ['1. Link', '<code>&lt;link rel="stylesheet" href="/eco-design-system/notifications.css"&gt;</code> and <code>&lt;script src="/eco-design-system/notifications.js"&gt;&lt;/script&gt;</code>. Link <code>button.css</code> first.'], ['2. Open', 'Call <code>ECO_N.openModal({ size, title, body, cancel, confirm })</code>. The script adds the overlay, the focus trap, the scroll lock and the three ways to close.'],
    ['3. React', '<code>onConfirm</code> runs when the primary button is pressed; <code>onClose(reason)</code> runs on every close.']])
c_modal = '<h2 class="ds-h2">Modal</h2><div id="recipes"></div>'
c_api = '<h2 class="ds-h2">API</h2><h3 class="ds-h3 ds-group">Settings of openModal</h3>' + table(['Setting', 'Use'], [['<code>size</code>', '<code>small</code> (default) or <code>large</code>.'], ['<code>label</code>', 'Optional uppercase label above the title.'], ['<code>title</code>, <code>body</code>', 'The title and the body text.'], ['<code>cancel</code>, <code>confirm</code>', 'The button labels. Defaults: Cancel, Confirm.'], ['<code>onConfirm</code>', 'Runs when the primary button is pressed.'], ['<code>onClose(reason)</code>', 'Reason: <code>close</code>, <code>esc</code>, <code>overlay</code>, <code>cancel</code> or <code>confirm</code>.']]) + \
    '<h3 class="ds-h3 ds-group">Custom properties</h3>' + table(['Name', 'Use'], [['<code>--modal-in-ease</code>, <code>--modal-in-duration</code>', 'Enter. Defaults: <code>ease-decelerate-emphasized</code>, <code>duration-fast-4</code>.'], ['<code>--modal-out-ease</code>, <code>--modal-out-duration</code>', 'Exit. Defaults: <code>ease-accelerate-generic</code>, <code>duration-fast-3</code>. Set on <code>&lt;html&gt;</code>.']]) + \
    '<h3 class="ds-h3 ds-group">Things to know</h3>' + bullets(['<code>openModal</code> returns <code>{ close, el }</code>.', 'Page scroll is locked with <code>body.has-modal</code>. <code>onClose</code> and the focus return run at once; the dialog is removed after the fade out.', 'Buttons inside the modal are always 32px high, also when <code>button.css</code> is on the page.', 'Do not open a modal from a modal.'])
c_css = '<h2 class="ds-h2">CSS / Tailwind</h2>' + desc('The component is one CSS file and one script, shared by every notification. Link them, never copy them. The code below is read from the files the page links, so it is always what you see.') + '<div id="files"></div>'
code = [('basic-usage', c_basic), ('modal', c_modal), ('api', c_api), ('css-tailwind', c_css, False)]

# ---------------------------------------------------------------- scripts
JS_SAMPLE = JS_PRE + r'''
  function sample(o) { return mk(H.modal(o).replace(/<div class="modal-overlay"[^>]*><\/div>\n/, '')); }
  var SIZES = [['small', 'Small', 'Delete this address?', 'The address is removed from your address book.'],
               ['large', 'Large', 'We have updated our terms', 'We have updated our terms of purchase and our privacy policy. The changes cover how we handle returns for business customers, how long we keep order history, and how we contact you about deliveries. Read the summary and accept to continue using My Pages.']];
'''

JS_EX = JS_SAMPLE + r'''
  /* Playground */
  var pg = { size: 'small', label: 'off' };
  function pgOpts() { return { size: pg.size, label: pg.label === 'on' ? 'Address book' : '', title: $('#pg-title').value, body: $('#pg-body').value, cancel: $('#pg-cancel').value, confirm: $('#pg-ok').value }; }
  function renderPg() { var o = pgOpts(); clear($('#pg-host')).appendChild(sample(o)); $('#pg-code').textContent = H.modal(o); }
  DK.wire(pg, renderPg);
  ['#pg-title', '#pg-body', '#pg-cancel', '#pg-ok'].forEach(function (s) { $(s).addEventListener('input', renderPg); });
  $('#pg-open').addEventListener('click', function () { var o = pgOpts(); o.onClose = function (r) { $('#pg-log').textContent = 'Closed with: ' + r + '.'; }; N.openModal(o); });

  /* In action */
  var log = $('#log');
  function closed(r) { log.textContent = 'Closed with: ' + ({ close: 'the × button', esc: 'the ESC key', overlay: 'a click on the overlay', cancel: 'Cancel', confirm: 'the primary button' }[r] || r) + '.'; }
  var SC = [
    { t: 'Confirm a deletion', d: 'Small. A destructive action: the user must confirm. Confirming shows a toast.', run: function () {
        N.openModal({ size: 'small', label: 'Account', title: 'Delete your account?', body: 'Your orders, addresses and saved lists are deleted. This cannot be undone.', cancel: 'Cancel', confirm: 'Delete account', onClose: closed,
          onConfirm: function () { setTimeout(function () { N.showToast({ status: 'success', emphasis: 'weak', text: 'Your account was deleted.', autoHide: 4000 }); }, 200); } }); } },
    { t: 'Cart has changed', d: 'Small. Important information the user must not miss before checkout.', run: function () {
        N.openModal({ size: 'small', label: 'Cart', title: 'Your cart has changed', body: 'Two items in your cart changed price or availability since you added them. Review the changes before you continue to checkout.', cancel: 'Back to cart', confirm: 'Continue to checkout', onClose: closed }); } },
    { t: 'Updated terms', d: 'Large. A compliance notice with more text. Below 640px it fills the screen.', run: function () {
        N.openModal({ size: 'large', title: SIZES[1][2], body: SIZES[1][3], cancel: 'Read later', confirm: 'Accept', onClose: closed }); } }];
  SC.forEach(function (s) {
    var row = document.createElement('div'); row.className = 'pg-row';
    row.innerHTML = '<div class="pg-row__txt"><b></b><span></span></div>';
    row.querySelector('b').textContent = s.t; row.querySelector('span').textContent = s.d;
    var b = document.createElement('button'); b.type = 'button'; b.className = 'btn btn--primary btn--sm'; b.innerHTML = '<span class="btn__label">Open modal</span>'; b.addEventListener('click', s.run);
    row.appendChild(b); $('#scenarios').appendChild(row);
  });

  /* Usage figures */
  clear($('#fig-do-1')).appendChild(sample({ size: 'small', title: 'Delete this address?', body: 'The address is removed from your address book.', cancel: 'Cancel', confirm: 'Delete' }));
  clear($('#fig-dont-1')).appendChild(sample({ size: 'small', title: 'Settings saved', body: 'Your changes were saved.', cancel: 'Cancel', confirm: 'OK' }));
  clear($('#fig-do-2')).appendChild(sample({ size: 'small', title: 'Delete this address?', body: 'The address is removed from your address book.', cancel: 'Cancel', confirm: 'Delete' }));
  clear($('#fig-dont-2')).appendChild(sample({ size: 'small', title: 'Delete this address?', body: 'The address is removed from your address book.', cancel: 'No', confirm: 'OK' }));

  /* Anatomy */
  var am = sample({ size: 'small', label: 'Label (optional)', title: 'Title', body: 'Body text explains what the user decides.', cancel: 'Cancel', confirm: 'Confirm' });
  clear($('#a-host')).appendChild(am);
  DK.callouts($('#m-anat'), [
    { n: 1, el: $('.modal__label', am), side: 'left', len: 44, at: 'edge' },
    { n: 2, el: $('.modal__title', am), side: 'left', len: 44, at: 'edge' },
    { n: 3, el: $('.icon-btn--close', am), side: 'right', len: 44, at: 'edge' },
    { n: 4, el: $('.modal__body', am), side: 'left', len: 44, at: 'edge' },
    { n: 5, el: $('.btn--blank', am), side: 'bottom', len: 36 },
    { n: 6, el: $('.btn--primary', am), side: 'bottom', len: 36 },
    { n: 7, el: $('.ds-callout__art', $('#m-anat')), side: 'right', len: 28, at: 'edge' }
  ]);

  /* Variants and sizes */
  clear($('#v-nolabel')).appendChild(sample({ size: 'small', title: SIZES[0][2], body: SIZES[0][3], cancel: 'Cancel', confirm: 'Delete' }));
  clear($('#v-label')).appendChild(sample({ size: 'small', label: 'Address book', title: SIZES[0][2], body: SIZES[0][3], cancel: 'Cancel', confirm: 'Delete' }));
  SIZES.forEach(function (s, i) { clear($('#v-s-' + s[0])).appendChild(sample({ size: s[0], label: '', title: s[2], body: s[3], cancel: 'Cancel', confirm: 'Confirm' })); });
  DK.motion({ anchor: 'playground', parts: [{ title: 'Enter', prefix: 'modal-in', rec: { ease: 'decelerate-emphasized', dur: 'fast-4' } }, { title: 'Exit', prefix: 'modal-out', rec: { ease: 'accelerate-generic', dur: 'fast-3' }, exit: true }], collapse: false, role: 'exit', showLabel: 'Open modal', hint: 'The modal opens over the page. Press Open modal, then close it with the ×, ESC or the overlay to see the motion.',
    why: 'The overlay fades; the panel fades and moves 64px, up in and down out. It enters with decelerate emphasized (200 ms) and leaves with accelerate (150 ms): closing is faster than opening (eco-motion: element enters / element disappears).', show: function () { N.openModal({ size: 'small', title: 'Delete this address?', body: 'The address is removed from your address book.', cancel: 'Cancel', confirm: 'Delete' }); } });
'''  + JS_MOTION_FIX + r'''
  DK.bp(); renderPg();
'''

JS_SPEC = JS_SAMPLE + r'''
  DK.tokenTable($('#tok-table tbody'), [['Panel', 'Background', 'surface-raised-primary'], ['Panel', 'Shadow', 'shadow-elevation-b-100'], ['Overlay', 'Background', 'surface-opacity-black-20'], ['Title', 'Text', 'text-primary'], ['Label and body', 'Text', 'text-secondary'], ['Cancel (Blank)', 'Text', 'text-action-primary'], ['Primary', 'Background', 'surface-action-1']]);
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
  var wrap = document.createElement('div'); wrap.className = 'modal-preview'; wrap.appendChild(sample({ size: 'small', label: 'Label', title: 'Title', body: 'Body text explains what the user decides.', cancel: 'Cancel', confirm: 'Confirm' }));
  $('#ms').appendChild(measureItem('Small modal', wrap, '.modal', false));
  DK.bp(function () { if (window.ECO_MEASURE) ECO_MEASURE.init(); });
'''

JS_CODE = JS_PRE + r'''
  DK.recipes($('#recipes'), [
    ['Markup', H.modal({ size: 'small', label: 'Account', title: 'Delete your account?', body: 'Your orders and addresses are deleted. This cannot be undone.', cancel: 'Cancel', confirm: 'Delete account' })],
    ['Open it from script', "var dialog = ECO_N.openModal({\n  size: 'small',                 // small | large\n  label: 'Account',              // optional\n  title: 'Delete your account?',\n  body: 'This cannot be undone.',\n  cancel: 'Cancel',\n  confirm: 'Delete account',\n  onConfirm: deleteAccount,\n  onClose: function (reason) {}  // close | esc | overlay | cancel | confirm\n});"]]);
  DK.printFile($('#files'), '../notifications.css', [['CSS: Modal', ['modal']], ['CSS: shared close button and buttons', ['base']]])
    .then(function () { return DK.printFile($('#files'), '../notifications.js', [['JavaScript: openModal', ['runtime']]]); });
'''

C = dict(BASE, slug=SLUG, title='Modal',
    lead='A modal is the <strong>most disruptive</strong> notification. It blocks the page until the user makes a decision, so use it only when the user must confirm or choose before going on.',
    lead_ex='Every “Open modal” button opens the real dialog: try ESC, a click on the dark overlay, Tab and the × to close it. Specification: <code>.claude/skills/eco-modal-ecom/SKILL.md</code>. Figma: ' + FIG + '.',
    lead_spec='Tokens, sizes, measurements and requirements. Values come from the live token package and from ' + FIG + '.',
    lead_code='How to open a modal from script and the CSS behind it. The files are <code>eco-design-system/notifications.css</code> and <code>notifications.js</code>.',
    ex=ex, spec=spec, code=code, js_ex=JS_EX, js_spec=JS_SPEC, js_code=JS_CODE, select_menu=False)
C['style'] = STYLE

if __name__ == '__main__':
    emit(C)
