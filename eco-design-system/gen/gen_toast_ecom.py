from notif import *

SLUG = 'toast-ecom'
FIG = fig_link(FIGMA % '13377-22983', 'E-Com Toast')

STYLE = STYLE + r'''
    .pg-grid { display: flex; flex-wrap: wrap; gap: 24px; align-items: flex-start; }
    .ds-callout__art { padding: 56px 24px 56px 24px; }
    .ms-ecom .measure__obj { max-width: 100%; }'''

playground = '<h2 class="ds-h2">Playground</h2>' + desc('Choose a variant and edit the text. Press <strong>Show toast</strong> to see it arrive in the corner of your window. With Auto-hide on it leaves after the chosen time (4 seconds by default); off, it stays until you close it.') + \
    '<div class="ds-playground"><div class="ds-stage ds-stage--center" id="pg-stage"><div id="pg-host" style="max-width:100%"></div></div><div class="ds-controls">' + \
    bp_field('pg-l-bp') + btn_group('pg-l-v', 'Variant', 'data-pg="variant"', [('cart', 'Add to cart', True), ('info', 'Informational', False)]) + \
    txt_field('pg-name', 'Product name (bold)', 'Carpenter Soul work pants stretch black', 'Product name') + txt_field('pg-text', 'Text', 'has been added to the cart.', 'Text') + \
    txt_field('pg-b2', 'Secondary (Blank) button', 'Choose accessories', 'Secondary', 'pg-b2-f') + txt_field('pg-b1', 'Primary button', 'Go to cart', 'Primary button', 'pg-b1-f') + \
    btn_group('pg-l-lk', '“View” link', 'data-pg="link"', [('on', 'Show', True), ('off', 'Hide', False)]).replace('<div class="ds-field">', '<div class="ds-field" id="pg-link-f" hidden>', 1) + \
    txt_field('pg-lk', 'Link text', 'View', 'Link text', 'pg-lk-f', True) + \
    btn_group('pg-l-ah', 'Auto-hide', 'data-pg="auto"', [('on', 'On', True), ('off', 'Off', False)]) + range_field() + \
    motion_note('The slide-in and slide-out animation') + '<button type="button" class="btn btn--primary btn--sm" id="pg-show" style="align-self:flex-start"><span class="btn__label">Show toast</span></button>' + \
    '</div></div><h3 class="ds-h3">Markup for this selection</h3>' + code_box('pg-code', 'HTML') + \
    note('The markup has no motion. Slide-in and slide-out animation is set in <a href="#motion" class="inline-link inline-link--medium inline-link--secondary">Motion</a>.')

action = '<h2 class="ds-h2">In action</h2>' + desc('<strong>Add to cart</strong> shows the cart toast with its two next steps. <strong>Add to wishlist</strong> shows the informational toast; press it again to remove. The toast closes after 4 seconds, with ×, or on a click outside it.') + \
    '<div class="ds-stage"><div class="pg-btns"><button type="button" class="btn btn--primary btn--sm" id="demo-add"><span class="btn__label">Add to cart</span></button><button type="button" class="btn btn--secondary btn--sm" id="demo-heart" aria-pressed="false"><span class="btn__label">Add to wishlist</span></button></div></div>' + \
    '<p class="pg-note" id="demo-log" aria-live="polite">Nothing happened yet.</p>'

overview = '<h2 class="ds-h2">Overview</h2>' + desc('An E-Com Toast confirms a <strong>shopping action</strong> without leaving the page: a product added to the cart, or saved to the wishlist. It has no status color; it speaks in the store’s own black and white.') + \
    desc('It is a task-generated notification, like the ' + link_large('toast.html', 'Toast') + ', and it enters the same way. System messages and errors use the Toast, never the E-Com Toast. Not sure which one to choose? Start at the ' + link_large('notifications.html', 'Notifications guide') + '.') + \
    three_pages(SLUG, 'an E-Com Toast', 'the values: tokens, sizes, measurements, states and requirements', 'how to show an E-Com Toast from script and the CSS behind it')

usage = '<h2 class="ds-h2">Usage</h2><h3 class="ds-h3 ds-group">When to use</h3>' + desc('Use an E-Com Toast for a product interaction. Use it to:') + \
    bullets(['Confirm that a product was added to the cart, and offer the two natural next steps', 'Confirm light shopping feedback, such as a product added to or removed from the wishlist']) + \
    '<h3 class="ds-h3 ds-group">When not to use</h3><h3 class="ds-h3">Errors and system status</h3>' + desc('The E-Com Toast has no status color and no status icon, so it cannot carry a failure. Use the Toast for errors and system messages.') + \
    pair('fig-do-1', 'Do confirm a product in the cart with an E-Com Toast.', 'fig-dont-1', 'Do not report an error in an E-Com Toast. Use a Toast instead.') + \
    '<h3 class="ds-h3">Name the product</h3>' + desc('The product name is in bold and the text says what happened to it. A message with no product name leaves the user guessing.') + \
    pair('fig-do-2', 'Do name the product in bold and say what happened.', 'fig-dont-2', 'Do not leave out the product. “Added” alone says too little.') + \
    '<h3 class="ds-h3 ds-group">Quick reference</h3>' + \
    which([['confirms a product was added to the cart or wishlist', 'E-Com Toast (this page)'], ['confirms any other action, or reports an error', lk('toast.html', 'Toast')], ['needs the user to confirm before it happens', lk('modal.html', 'Modal')]]) + \
    rules(['Name the product in bold and say what happened.', 'Offer the two natural next steps on Add to cart.', 'Use the Informational variant for wishlist and similar light feedback.', 'Keep the toast to the top-right corner, like every toast.'],
          ['Show errors or system status. Use the Toast.', 'Ask the user to confirm something. Use a Modal.', 'Add a status color or icon. This toast has none.', 'Leave it open indefinitely.'])

anatomy = '<h2 class="ds-h2">Anatomy</h2><h3 class="ds-h3 ds-group">Add to cart</h3>' + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout" id="e-anat" role="img" aria-label="Anatomy of the Add to cart toast: 1 product image, 2 product name and text, 3 close, 4 secondary button, 5 primary button"><div class="ds-callout__art"><div id="a-host"></div></div></div></figure></div>' + \
    ol_parts([('Product image', '40×40px, <code>object-fit: contain</code>.'), ('Product name and text', 'The name in bold, then the text in regular.'), ('Close', 'A Blank icon button, 20px icon, 2px padding.'), ('Secondary button', 'Blank, no frame: “Choose accessories”.'), ('Primary button', '“Go to cart”. Fills the rest of the row.')]) + \
    '<h3 class="ds-h3 ds-group">Informational</h3>' + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout" id="i-anat" role="img" aria-label="Anatomy of the Informational toast: 1 name and text, 2 link, 3 close"><div class="ds-callout__art"><div id="ai-host"></div></div></div></figure></div>' + \
    ol_parts([('Name and text', 'White text on the black surface.'), ('Link', 'Optional. An inline link in the inverted color, underlined.'), ('Close', 'A Blank inverted icon button.')])

variants = '<h2 class="ds-h2">Variants</h2>' + desc('Two variants. There is no status or emphasis property: pick the variant by how much the user can do next.') + bp_toolbar('vb-l') + \
    '<h3 class="ds-h3 ds-group">Add to cart</h3>' + desc('White surface with the product image and two ways forward: choose accessories or go to the cart.') + fig_one_id('v-cart', None, 'pg-grid') + \
    '<h3 class="ds-h3 ds-group">Informational</h3>' + desc('Black surface with light text and an optional underlined link. For short information that needs little or no interaction, such as “added to wishlist”.') + fig_one_id('v-info', None, 'pg-grid')

sizes = '<h2 class="ds-h2">Sizes</h2>' + desc('Add to cart is 440px wide from 640px and 375px below; Informational is 375px at every breakpoint. Padding and text are listed under ' + sec_link(SLUG, 'sizes', 'Sizes') + ' in Specifications. Tablet (640–768px) already has the wide card and 24px padding; only the buttons are mobile-sized.') + bp_toolbar('sb-l') + fig_one_id('v-size', None, 'pg-grid')

layout = '<h2 class="ds-h2">Layout &amp; Appearance</h2><h3 class="ds-h3 ds-group">Alignment</h3>' + desc('The image, the text and the × sit on one row, top-aligned. The buttons are on a row below, with the Primary button filling the rest. In Informational the link wraps after the text with an 8px and a 12px gap.') + \
    '<h3 class="ds-h3 ds-group">Placement</h3>' + desc('The same as the Toast: fixed in the top-right corner of the window, and from the top at the full width on mobile. One toast at a time.') + \
    '<h3 class="ds-h3 ds-group">Width</h3>' + desc('440px (Add to cart) or 375px (Informational) from 640px, never wider than the window. Below 640px both fill the width.') + \
    '<h3 class="ds-h3 ds-group">Appearance</h3>' + desc('Add to cart is white; Informational is black with an inverted text and a 1px edge. Both use the highest shadow. Token names and values are under ' + sec_link(SLUG, 'design-tokens', 'Design Tokens') + ' in Specifications.')

behavior = '<h2 class="ds-h2">Behavior</h2><h3 class="ds-h3 ds-group">Dismissal</h3>' + desc('The toast closes with the ×, with a click outside it, or by itself after 4 seconds. A click on a button or the link runs its action and closes the toast.') + \
    '<h3 class="ds-h3 ds-group">Hover and focus</h3>' + desc('Buttons, the link and the × take focus with a visible ring, on keyboard use only. In Informational the link loses its underline on hover. All states are under ' + sec_link(SLUG, 'states', 'States') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Motion</h3>' + desc('Same as the Toast: it only slides, 300ms. Try other values under <a class="inline-link inline-link--large inline-link--secondary" href="#motion">Motion</a> above, and see ' + sec_link(SLUG, 'motion', 'Motion') + ' in Specifications.')

access = '<h2 class="ds-h2">Accessibility</h2>' + desc('All requirements are listed under ' + sec_link(SLUG, 'accessibility-requirements', 'Accessibility Requirements') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Keyboard support</h3>' + desc('Tab moves to the buttons, the link and the ×, each with a visible focus ring. The toast does not take focus when it appears.') + \
    '<h3 class="ds-h3 ds-group">Screen reader support</h3>' + desc('The toast area is <code>role="status"</code> with <code>aria-live="polite"</code>, so the message is announced without moving focus. The product image is decorative (<code>alt=""</code>): the name is in the text.')

related = '<h2 class="ds-h2">Related</h2><ul class="ds-bullets"><li><strong>' + link_large('toast.html', 'Toast') + '</strong>. System messages and errors.</li><li><strong>' + link_large('modal.html', 'Modal') + '</strong>. A decision before the user can go on.</li><li><strong>' + link_large('notifications.html', 'Notifications guide') + '</strong>. Which notification to choose.</li></ul>'

references = '<h2 class="ds-h2">References</h2>' + refs([
    ('https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html', 'WCAG 2.2: Status Messages', 'Success criterion 4.1.3.'),
    ('https://www.w3.org/WAI/WCAG22/Understanding/timing-adjustable.html', 'WCAG 2.2: Timing Adjustable', 'Success criterion 2.2.1.'),
    ('https://material.io/components/snackbars', 'Material Design: Snackbars', 'Google.')])

ex = [('playground', playground), ('in-action', action), ('overview', overview), ('usage', usage), ('anatomy', anatomy), ('variants', variants), ('sizes', sizes), ('layout', layout), ('behavior', behavior), ('accessibility', access), ('related', related), ('references', references)]

# ---------------------------------------------------------------- Specifications
st_tok = '<h2 class="ds-h2">Design Tokens</h2>' + desc('Resolved from the live token package.') + \
    '<div class="ds-table-wrap"><table class="ds-table" id="tok-table"><thead><tr><th scope="col">Variant</th><th scope="col">Part</th><th scope="col">Token</th><th scope="col">Value</th></tr></thead><tbody></tbody></table></div>'

st_sizes = '<h2 class="ds-h2">Sizes</h2><h3 class="ds-h3 ds-group">Dimensions</h3>' + desc('Tablet is 640 to 768px. The Figma axes are Variant and Breakpoint.') + table(['Property', 'Desktop (769px+)', 'Tablet (640–768px)', 'Mobile (below 640px)'], [
    ['Width, Add to cart', '440px', '440px', '375px'], ['Width, Informational', '375px', '375px', '375px'], ['Padding', '24px', '24px', '16px'],
    ['Text', 'Name bold 16/18 + text <code>body-md</code> 17/24, 0.32px, at every breakpoint', 'same', 'same'],
    ['Buttons', '32px high, <code>label-sm</code> 14px, 0.56px, padding 6px', '32px high, <code>label-md</code> 14px, 0.42px, padding 4px', 'same as tablet'],
    ['Informational link', '<code>body-md</code> 17/24, underlined, wraps after the text with 8px / 12px gaps', '17/24', '16/22'], ['Gap image to text', '16px', '16px', '16px'], ['Gap content to close', '12px', '12px', '12px'], ['Shadow', '<code>var(--shadow-elevation-b-80)</code>', 'same', 'same']]) + \
    '<h3 class="ds-h3 ds-group">Position</h3>' + desc('Same as the Toast: fixed in the top-right corner (from the top, full width, on mobile).') + table(['Breakpoint', 'Top', 'Right', 'Width'], [['lg (1024px+)', '40px', '40px', '440px or 375px'], ['md (769–1023px)', '32px', '32px', '440px or 375px'], ['sm (640–768px)', '32px', '32px', '440px or 375px'], ['xs (0–639px)', '0', '0 (left 0)', 'Full viewport width']])

st_meas = '<h2 class="ds-h2">Measurements</h2><h3 class="ds-h3 ds-group">Dimensions</h3>' + desc('The padding of the Add to cart toast. The numbers are read from the component.') + bp_toolbar('mb-l') + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-fig__stage--flush" style="padding:0;min-height:0"><div class="measure ms-ecom" id="ms" role="img" aria-label="Padding of the Add to cart toast"></div></div><figcaption class="ds-fig__cap">Add to cart at true size. Change the Breakpoint to see the mobile values.</figcaption></figure></div>' + \
    table(['Attribute', 'Desktop (769px+) and tablet', 'Mobile (below 640px)'], [['Padding, Add to cart', '24px', '16px'], ['Padding, Informational', '24px, of which 1px is the edge (23px + 1px)', '16px, of which 1px is the edge (15px + 1px)'], ['Gap image to text', '16px', '16px'], ['Gap content to close', '12px', '12px'], ['Above the buttons', '16px', '16px'], ['Between the buttons', '8px', '8px']]) + \
    '<h3 class="ds-h3 ds-group">Spacing</h3>' + desc('The same distances as spacing tokens.') + table(['Part', 'Value'], [['Padding, tablet and desktop', '<code>space-24</code>'], ['Padding, mobile', '<code>space-16</code>'], ['Image to text', '<code>space-16</code>'], ['Content to close', '<code>space-12</code>'], ['Above the buttons', '<code>space-16</code>'], ['Between the buttons', '<code>space-8</code>']])

st_elev = '<h2 class="ds-h2">Elevation</h2>' + table(['Part', 'Token', 'Value'], [['E-Com Toast', '<code>shadow-elevation-b-80</code>', 'The same shadow as the Toast.']])

st_states = '<h2 class="ds-h2">States</h2>' + desc('Both variants. An E-Com Toast has no hover or disabled state of its own: the buttons, the link and the × have. Its lifecycle is under <a class="inline-link inline-link--large inline-link--secondary" href="#motion">Motion</a>.') + bp_toolbar('sb-l') + \
    '<div class="ds-table-wrap"><table class="ds-table pg-matrix" id="matrix"><thead><tr><th scope="col">Variant</th><th scope="col">Example</th></tr></thead><tbody></tbody></table></div>'

st_typo = '<h2 class="ds-h2">Typography</h2>' + table(['Element', 'Token', 'Mobile and tablet', 'Desktop (769px+)'], [['Product name', '<code>title-sm</code>', '16/18, bold', '16/18, bold'], ['Text', '<code>body-md</code>', '17/24, 0.32px', '17/24, 0.32px'], ['Buttons', '<code>label-md</code> / <code>label-sm</code>', '14/14, 0.42px', '14/14, 0.56px'], ['Informational link', '<code>body-md</code>', '16/22', '17/24']]) + \
    note('The text is 17/24 at every breakpoint, as in Figma. This pair is <code>body-md</code> on desktop.')

st_struct = '<h2 class="ds-h2">Structure</h2><h3 class="ds-h3 ds-group">Elements</h3>' + table(['Element', 'Class', 'Notes'], [
    ['Toast', '<code>ecom-toast ecom-toast--cart</code> or <code>--info</code>', 'Add to cart or Informational.'], ['Header', '<code>ecom-toast__header</code>, <code>ecom-toast__image-text</code>', 'Image, text and ×. Add to cart only.'], ['Image', '<code>ecom-toast__img</code>', '40×40px, <code>alt=""</code>.'],
    ['Text', '<code>ecom-toast__text</code>, <code>ecom-toast__name</code>', 'The name is bold.'], ['Footer', '<code>ecom-toast__footer</code>', 'Blank and Primary buttons, 32px high.'], ['Informational', '<code>ecom-toast__info-content</code>, <code>ecom-toast__info-text</code>', 'Text and optional link.'], ['Close', '<code>icon-btn icon-btn--close</code>', 'Add <code>icon-btn--close-inverted</code> on Informational.']]) + \
    '<h3 class="ds-h3 ds-group">Types</h3>' + desc('Two variants: Add to cart and Informational. No status and no emphasis.') + \
    '<h3 class="ds-h3 ds-group">Width</h3>' + desc('440px (Add to cart) or 375px (Informational) from 640px; the full width below.')

st_motion = '<h2 class="ds-h2">Motion</h2>' + table(['Property', 'Value'], [['Slide in / out', '<code>var(--duration-medium-2)</code> (300ms), <code>var(--ease-decelerate-emphasized)</code> in, <code>var(--ease-accelerate-generic)</code> out'], ['Auto-hide', '4000ms (same as System Toast)'], ['Position', 'Fixed. Top 40px / right 40px at 1024px+, 32px below, top and full width on mobile']]) + \
    note('Compare other easing and duration values in the live Motion section on <a class="inline-link inline-link--medium inline-link--secondary" href="toast-ecom.html#motion">Examples &amp; Guidelines</a>.')

st_behavior = '<h2 class="ds-h2">Behavior</h2>' + table(['Input', 'Result'], [
    ['Click ×, click outside, wait', 'Exit animation, then removed. Auto-hide after 4 seconds.'], ['Click a button or the link', 'Runs its action and closes the toast.'], ['Tab', 'Buttons, link and × take focus with a visible ring.'],
    ['Inline link', 'Informational: Inline Link, inverted (white). Underlined when enabled; on hover the underline goes and the color changes.']])

st_access = '<h2 class="ds-h2">Accessibility Requirements</h2>' + table(['Topic', 'Requirement'], [
    ['Announcement', 'Announced politely through <code>role="status"</code> and <code>aria-live="polite"</code>; focus is not moved (WCAG 4.1.3).'], ['Image', 'The product image is decorative: <code>alt=""</code>. The name is in the text.'], ['Focus', 'Buttons, link and × have a 2px ring, <code>border-focus</code>, on keyboard use (WCAG 2.4.7).'],
    ['Contrast', 'White text on <code>surface-100</code> in Informational. Link and × use the inverted tokens.'], ['Reduced motion', 'No slide under <code>prefers-reduced-motion: reduce</code>.']])

spec = [('design-tokens', st_tok), ('sizes', st_sizes), ('measurements', st_meas), ('elevation', st_elev), ('states', st_states), ('typography', st_typo), ('structure', st_struct), ('motion', st_motion), ('behavior', st_behavior), ('accessibility-requirements', st_access)]

# ---------------------------------------------------------------- Code
c_basic = '<h2 class="ds-h2">Basic Usage</h2>' + desc('Link the shared files once per page. Never copy the rules into a page.') + table(['Step', 'What to do'], [
    ['1. Link', '<code>&lt;link rel="stylesheet" href="/eco-design-system/notifications.css"&gt;</code> and <code>&lt;script src="/eco-design-system/notifications.js"&gt;&lt;/script&gt;</code>. Link <code>button.css</code> first.'], ['2. Show a toast', 'Call <code>ECO_N.showEcomToast({ variant, name, text })</code>.'],
    ['3. Variant', '<code>cart</code> (image and two buttons) or <code>info</code> (black, optional link).'], ['4. Actions', '<code>primary</code> and <code>secondary</code> for the cart, <code>link</code> for the informational toast, each <code>{ label, onClick }</code>.']])
c_toast = '<h2 class="ds-h2">E-Com Toast</h2><div id="recipes"></div>' + note('The markup has no motion. The slide is set in <a class="inline-link inline-link--medium inline-link--secondary" href="toast-ecom.html#motion">Motion</a> on Examples &amp; Guidelines.')
c_api = '<h2 class="ds-h2">API</h2><h3 class="ds-h3 ds-group">Settings of showEcomToast</h3>' + table(['Setting', 'Use'], [['<code>variant</code>', '<code>cart</code> (default) or <code>info</code>.'], ['<code>name</code>, <code>text</code>', 'The product name (bold) and the text after it.'], ['<code>img</code>', 'Add to cart: the product image URL.'], ['<code>primary</code>, <code>secondary</code>', 'Add to cart: buttons, each <code>{ label, onClick }</code>.'], ['<code>link</code>', 'Informational: <code>{ label, onClick }</code>.'], ['<code>autoHide</code>', 'Milliseconds; default 4000, <code>0</code> = stays until dismissed.']]) + \
    '<h3 class="ds-h3 ds-group">Things to know</h3>' + bullets(['It uses the same host, motion and custom properties as the Toast: <code>--toast-in-ease</code>, <code>--toast-in-duration</code>, <code>--toast-out-ease</code>, <code>--toast-out-duration</code>.', 'Only one toast is on screen: a new toast replaces the current one, also a System Toast.', 'Buttons inside the toast are always 32px high, also when <code>button.css</code> is on the page.'])
c_css = '<h2 class="ds-h2">CSS / Tailwind</h2>' + desc('The component is one CSS file and one script, shared by every notification. Link them, never copy them. The code below is read from the files the page links, so it is always what you see.') + '<div id="files"></div>'
code = [('basic-usage', c_basic), ('e-com-toast', c_toast), ('api', c_api), ('css-tailwind', c_css, False)]

# ---------------------------------------------------------------- scripts
JS_SAMPLE = JS_PRE + r'''
  function sample(o) { return mk(H.ecom(o)); }
  var CART = { variant: 'cart', name: 'Carpenter Soul work pants stretch black', text: 'has been added to the cart.', img: IMG, secondary: 'Choose accessories', primary: 'Go to cart' };
  var INFO = { variant: 'info', name: 'Belt stretch black', text: 'added to your wishlist.', link: 'View' };
'''

JS_EX = JS_SAMPLE + r'''
  /* Playground */
  var pg = { variant: 'cart', link: 'on', auto: 'on' };
  function pgOpts() {
    var o = pg.variant === 'cart' ? Object.assign({}, CART) : Object.assign({}, INFO);
    o.name = $('#pg-name').value; o.text = $('#pg-text').value;
    if (pg.variant === 'cart') { o.secondary = $('#pg-b2').value; o.primary = $('#pg-b1').value; }
    else if (pg.link === 'off') delete o.link; else o.link = $('#pg-lk').value;
    return o;
  }
  function renderPg() {
    var o = pgOpts(); clear($('#pg-host')).appendChild(sample(o)); $('#pg-code').textContent = H.ecom(o);
    $('#pg-link-f').hidden = pg.variant !== 'info'; $('#pg-time-f').hidden = pg.auto === 'off'; $('#pg-lk-f').hidden = pg.variant !== 'info' || pg.link === 'off'; $('#pg-b2-f').hidden = $('#pg-b1-f').hidden = pg.variant !== 'cart';
  }
  $$('[data-pg]').forEach(function (g) { DK.seg(g, function (v) {
    pg[g.dataset.pg] = v;
    if (g.dataset.pg === 'variant') { var d = v === 'cart' ? CART : INFO; $('#pg-name').value = d.name; $('#pg-text').value = d.text; }
    renderPg();
  }); });
  ['#pg-name', '#pg-text', '#pg-b2', '#pg-b1', '#pg-lk'].forEach(function (s) { $(s).addEventListener('input', renderPg); });
  $('#pg-show').addEventListener('click', function () {
    var o = pgOpts();
    N.showEcomToast({ variant: o.variant, name: o.name, text: o.text, img: IMG, primary: o.primary && { label: o.primary }, secondary: o.secondary && { label: o.secondary }, link: o.link && { label: o.link }, autoHide: pg.auto === 'on' ? $('#pg-time').value * 1000 : 0 });
  });

  /* In action */
  var log = $('#demo-log'), wished = false;
  $('#demo-add').addEventListener('click', function () {
    log.textContent = 'Added to cart.';
    N.showEcomToast({ variant: 'cart', name: CART.name, text: CART.text, img: IMG,
      secondary: { label: CART.secondary, onClick: function () { log.textContent = 'Went to accessories.'; } },
      primary: { label: CART.primary, onClick: function () { log.textContent = 'Went to the cart.'; } } });
  });
  $('#demo-heart').addEventListener('click', function () {
    wished = !wished; this.setAttribute('aria-pressed', String(wished)); this.firstChild.textContent = wished ? 'Remove from wishlist' : 'Add to wishlist';
    log.textContent = wished ? 'Added to wishlist.' : 'Removed from wishlist.';
    N.showEcomToast({ variant: 'info', name: 'Carpenter Soul work pants', text: wished ? 'added to your wishlist.' : 'removed from your wishlist.', link: wished ? { label: 'View', onClick: function () { log.textContent = 'Went to the wishlist.'; } } : null });
  });

  /* Usage figures */
  clear($('#fig-do-1')).appendChild(sample({ variant: 'cart', name: 'Belt stretch black', text: 'has been added to the cart.', img: IMG, secondary: 'Choose accessories', primary: 'Go to cart' }));
  clear($('#fig-dont-1')).appendChild(sample({ variant: 'info', name: 'Upload failed.', text: 'Try again later.' }));
  clear($('#fig-do-2')).appendChild(sample({ variant: 'info', name: 'Belt stretch black', text: 'added to your wishlist.' }));
  clear($('#fig-dont-2')).appendChild(sample({ variant: 'info', name: '', text: 'Added to your wishlist.' }));

  /* Anatomy */
  var ac = sample(CART); clear($('#a-host')).appendChild(ac);
  function rng(el) { return function () { var r = document.createRange(); r.selectNodeContents(el); return r.getBoundingClientRect(); }; }
  DK.callouts($('#e-anat'), [
    { n: 1, el: $('.ecom-toast__img', ac), side: 'top', len: 44, at: 'center' },
    { n: 2, el: $('.ecom-toast__name', ac), side: 'top', len: 44 },
    { n: 3, el: $('.icon-btn--close', ac), side: 'top', len: 44, at: 'center' },
    { n: 4, el: $('.btn--blank', ac), side: 'bottom', len: 44 },
    { n: 5, el: $('.btn--primary', ac), side: 'bottom', len: 44 }
  ]);
  var ai = sample(INFO); clear($('#ai-host')).appendChild(ai);
  DK.callouts($('#i-anat'), [
    { n: 1, box: rng($('.ecom-toast__info-text', ai)), side: 'top', len: 44 },
    { n: 2, el: $('.inline-link', ai), side: 'bottom', len: 44 },
    { n: 3, el: $('.icon-btn--close', ai), side: 'top', len: 44, at: 'center' }
  ]);

  /* Variants and sizes */
  $('#v-cart').appendChild(sample(CART)); $('#v-info').appendChild(sample(INFO)); $('#v-info').appendChild(sample({ variant: 'info', name: 'Belt stretch black', text: 'removed from your wishlist.' }));
  $('#v-size').appendChild(sample(CART)); $('#v-size').appendChild(sample(INFO));

  DK.motion({ anchor: 'playground', parts: [{ title: 'Enter', prefix: 'toast-in', rec: { ease: 'decelerate-emphasized', dur: 'medium-2' } }, { title: 'Exit', prefix: 'toast-out', rec: { ease: 'accelerate-generic', dur: 'medium-2' }, exit: true }], collapse: false, role: 'exit',
    why: 'Same motion as the System Toast: the toast only slides, with no fade. It enters with decelerate emphasized and leaves with accelerate, both Medium 2 (eco-motion: element enters / element disappears).', show: function () { N.showEcomToast({ variant: 'cart', name: CART.name, text: CART.text, img: IMG, secondary: { label: CART.secondary }, primary: { label: CART.primary } }); } });
''' + JS_MOTION_FIX + r'''
  DK.bp(); renderPg();
'''

JS_SPEC = JS_SAMPLE + r'''
  DK.tokenTable($('#tok-table tbody'), [
    ['Add to cart', 'Background', 'surface-raised-primary'], ['Add to cart', 'Text', 'text-primary'], ['Add to cart', 'Blank button text', 'text-action-primary'], ['Add to cart', 'Primary button', 'surface-action-1'],
    ['Informational', 'Background', 'surface-100'], ['Informational', 'Edge', 'border-secondary'], ['Informational', 'Text, link, close', 'text-primary-inverted'], ['Both', 'Shadow', 'shadow-elevation-b-80']]);
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
  $('#ms').appendChild(measureItem('Add to cart', sample(CART), null, false));
  DK.bp(function () { if (window.ECO_MEASURE) ECO_MEASURE.init(); });
  var tb = $('#matrix tbody');
  [['Add to cart', CART], ['Informational, with a link', INFO], ['Informational, without a link', { variant: 'info', name: 'Belt stretch black', text: 'removed from your wishlist.' }]].forEach(function (r) {
    var tr = document.createElement('tr'), th = document.createElement('th'); th.scope = 'row'; th.textContent = r[0]; tr.appendChild(th);
    var td = document.createElement('td'); td.appendChild(sample(r[1])); tr.appendChild(td); tb.appendChild(tr);
  });
'''

JS_CODE = JS_PRE + r'''
  var CART = { variant: 'cart', name: 'Carpenter Soul work pants stretch black', text: 'has been added to the cart.', img: IMG, secondary: 'Choose accessories', primary: 'Go to cart' };
  var INFO = { variant: 'info', name: 'Belt stretch black', text: 'added to your wishlist.', link: 'View' };
  DK.recipes($('#recipes'), [
    ['Add to cart', H.ecom(CART)], ['Informational', H.ecom(INFO)],
    ['Show it from script', "ECO_N.showEcomToast({\n  variant: 'cart',\n  name: 'Carpenter Soul work pants stretch black',\n  text: 'has been added to the cart.',\n  img: '/images/product-hantverksbyxa.jpg',\n  secondary: { label: 'Choose accessories', onClick: toAccessories },\n  primary: { label: 'Go to cart', onClick: toCart }\n});\n\nECO_N.showEcomToast({ variant: 'info', name: 'Belt stretch black', text: 'added to your wishlist.', link: { label: 'View', onClick: toWishlist } });"]]);
  DK.printFile($('#files'), '../notifications.css', [['CSS: E-Com Toast', ['ecom']], ['CSS: toast position, shared close button, link and buttons', ['toast', 'base']]])
    .then(function () { return DK.printFile($('#files'), '../notifications.js', [['JavaScript: showEcomToast', ['runtime']]]); });
'''

C = dict(BASE, slug=SLUG, title='E-Com Toast',
    lead='An E-Com Toast confirms a <strong>shopping action</strong> without leaving the page: a product added to the cart, or saved to the wishlist. It has no status color; it speaks in the store’s own black and white.',
    lead_ex='Every example is the real component, and every “Show toast” button fires a real toast in the corner of your window. System messages and errors use the ' + lead_link('toast.html', 'Toast') + '. Specification: <code>.claude/skills/eco-toast-ecom/SKILL.md</code>. Figma: ' + FIG + '.',
    lead_spec='Tokens, sizes, measurements, states and requirements. Values come from the live token package and from ' + FIG + '.',
    lead_code='How to show an E-Com Toast from script and the CSS behind it. The files are <code>eco-design-system/notifications.css</code> and <code>notifications.js</code>.',
    ex=ex, spec=spec, code=code, js_ex=JS_EX, js_spec=JS_SPEC, js_code=JS_CODE, select_menu=False)
C['style'] = STYLE

if __name__ == '__main__':
    emit(C)
