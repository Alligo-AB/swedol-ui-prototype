from notif import *

SLUG = 'banner'
FIG = fig_link(FIGMA % '13377-41997', 'Banner')
FIG_GUIDE = fig_link(FIGMA % '23432-270125', 'Banner component guide')

STYLE = STYLE + r'''
    .pg-figs { display: flex; flex-direction: column; gap: 32px; }
    .pg-fig { margin: 0; display: flex; flex-direction: column; gap: 12px; }
    .pg-fig img { display: block; width: 100%; height: auto; border: 1px solid var(--color-border-secondary); }
    .pg-fig--mobile img { max-width: 375px; }
    .pg-fig figcaption { font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-secondary); max-width: 720px; }
    #prio-table th[scope="row"] { width: 22%; min-width: 150px; }
    #prio-table td:nth-child(3) { width: 150px; white-space: nowrap; }
    #prio-table td:nth-child(4) { width: 22%; min-width: 150px; }
    /* Up to 1100px each row stacks: priority, banner, the Applies button, the result (labels come from data-label) */
    @media (max-width: 1100px) {
      #prio-table, #prio-table tbody, #prio-table tr, #prio-table th, #prio-table td { display: block; width: auto; min-width: 0; }
      #prio-table thead { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); }
      #prio-table tr { padding: 16px; border-bottom: 1px solid var(--color-border-secondary); }
      #prio-table tr:last-child { border-bottom: 0; }
      #prio-table th[scope="row"], #prio-table td { width: auto; min-width: 0; padding: 0; border: 0; }
      #prio-table td { margin-top: 12px; }
      #prio-table td[data-label]::before { content: attr(data-label); display: block; font-size: 12px; line-height: 16px; letter-spacing: 0.24px; font-weight: 600; text-transform: uppercase; color: var(--color-text-tertiary); margin-bottom: 4px; }
      #prio-table td:nth-child(3) { white-space: normal; }
      #prio-table th[scope="row"] .ds-na { display: block; white-space: normal; }
    }
    .ds-callout__art { padding: 56px 24px 56px 24px; width: 100%; box-sizing: border-box; }
    .ms-banner .measure__obj { width: 560px; max-width: 100%; }'''

playground = '<h2 class="ds-h2">Playground</h2>' + desc('Choose a size, status and emphasis and the banner and its code update. The × works: it closes the banner, and <strong>Show again</strong> brings it back.') + \
    '<div class="ds-playground"><div class="ds-stage ds-stage--center" id="pg-stage" style="align-items:stretch"><div id="pg-host" style="width:100%;align-self:center"></div></div><div class="ds-controls">' + \
    bp_field('pg-l-bp') + btn_group('pg-l-sz', 'Size', 'data-pg="size"', [('small', 'Small', True), ('large', 'Large', False), ('promotion', 'Promotion', False)]) + \
    sel_field('pg-l-st', 'sel-pg-l-st', 'Status', 'status', [('info', 'Informational'), ('success', 'Success'), ('warning', 'Warning'), ('error', 'Error')]).replace('<div class="ds-field form-field">', '<div class="ds-field form-field" id="f-status">', 1) + \
    '<div class="ds-field"><span class="form-label form-label--sm" id="pg-l-em">Emphasis</span><div class="btn-group" role="group" aria-labelledby="pg-l-em" id="pg-em"></div></div>' + \
    btn_group('pg-l-cl', 'Close button', 'data-pg="closable"', [('on', 'Shown', True), ('off', 'Hidden', False)]) + \
    txt_field('pg-title', 'Title (optional)', 'Planned maintenance', 'Title').replace('<label class="form-label form-label--sm"', '<label class="form-label form-label--sm" id="l-title"', 1) + \
    txt_field('pg-text', 'Text', 'The site is unavailable on Sunday 02:00–04:00.', 'Text').replace('<label class="form-label form-label--sm"', '<label class="form-label form-label--sm" id="l-text"', 1) + \
    icon_field() + txt_field('pg-sl', 'Inline link (optional)', 'Log out', 'Inline link', 'f-sl') + \
    btn_group('pg-l-ac', 'Actions', 'data-pg="acts"', [('buttons', 'Buttons', True), ('links', 'Inline links', False)]).replace('<div class="ds-field">', '<div class="ds-field" id="pg-acts-f" hidden>', 1) + \
    txt_field('pg-b2', 'Secondary button', 'Go to cart', 'Secondary button', 'pg-b2-f', True) + txt_field('pg-b1', 'Blank button', 'Choose accessories', 'Blank button', 'pg-b1-f', True) + \
    txt_field('pg-l1', 'Link 1', 'Text link', 'Link 1', 'pg-l1-f', True) + txt_field('pg-l2', 'Link 2', 'Read more', 'Link 2', 'pg-l2-f', True) + txt_field('pg-link', 'Link text', 'Go to campaign', 'Link text', 'f-link', True) + \
    motion_note('The animation when the × is clicked') + '<button type="button" class="btn btn--secondary btn--sm" id="pg-reset" style="align-self:flex-start"><span class="btn__label">Show again</span></button>' + \
    '</div></div><h3 class="ds-h3">Markup for this selection</h3>' + code_box('pg-code', 'HTML') + \
    note('The markup has no motion. Closing animation is set in <a href="#motion" class="inline-link inline-link--medium inline-link--secondary">Motion</a>.')

overview = '<h2 class="ds-h2">Overview</h2>' + desc('A banner carries a <strong>page-wide or system-level message</strong>: an outage, planned maintenance, a campaign or a notice to one customer group. It sits at the top and stays until it is closed or the situation changes.') + \
    desc('Banners are set up by an administrator, not by user actions. See <a class="inline-link inline-link--large inline-link--secondary" href="#placement-and-priority">Placement and priority</a> for where they go and which one wins. Feedback on a click belongs in a ' + link_large('toast.html', 'Toast') + '; status next to one form or block in an ' + link_large('inline.html', 'Inline notification') + '.') + \
    three_pages(SLUG, 'a banner', 'the values: tokens, sizes, measurements, states and requirements', 'how to build a banner and the CSS behind it')

usage = '<h2 class="ds-h2">Usage</h2><h3 class="ds-h3 ds-group">When to use</h3>' + desc('Use a banner for what concerns the whole page, the whole site or a customer group. Use it to:') + \
    bullets(['Report an outage, a disruption or planned maintenance', 'Announce a campaign, a price change or free shipping', 'Tell a signed-in customer or a customer group something that needs their attention, such as an unpaid invoice']) + \
    '<h3 class="ds-h3 ds-group">When not to use</h3><h3 class="ds-h3">For the page, not for a click</h3>' + desc('A banner stays until it is closed. The result of a click belongs in a Toast, next to where the user is working.') + \
    pair('fig-do-1', 'Do use a banner for something that concerns the whole site.', 'fig-dont-1', 'Do not use a banner for the result of a click. Use a Toast instead.') + \
    '<h3 class="ds-h3">Strong only for what is urgent</h3>' + desc('Weak is the default and Weaker suits general information and offers. Strong is a solid color: use it sparingly, for a critical outage, a blocked main flow or risk of data loss. See ' + link_large('notifications.html#emphasis', 'Choosing the emphasis') + '.') + \
    pair('fig-do-2', 'Do use Weaker for general information and offers.', 'fig-dont-2', 'Do not use Strong for an offer. Keep it for what is urgent.') + \
    '<h3 class="ds-h3">Large only on My Pages</h3>' + desc('Large is a richer message for a signed-in customer. For a one-line message use Small.') + \
    pair('fig-do-3', 'Do use Small for a one-line message.', 'fig-dont-3', 'Do not use Large for a one-line message.') + \
    '<h3 class="ds-h3 ds-group">Quick reference</h3>' + \
    which([['concerns the whole page or system, or a customer group', 'Banner (this page)'], ['is feedback on something the user just did', lk('toast.html', 'Toast')], ['belongs to one section or form', lk('inline.html', 'Inline')], ['needs a decision before the user can go on', lk('modal.html', 'Modal')]]) + \
    rules(['Use Strong only for what is urgent: outages, impersonation.', 'Use Weaker for general information and offers.', 'Use Large only on My Pages.', 'Match the icon to the status color.'],
          ['Show several banners in the same place. Priority picks one.', 'Use a banner for the result of a click. Use a Toast or Inline.', 'Hardcode a brand color in a Promotion banner. Use the accent tokens.', 'Use Large for a one-line message.'])

anatomy = '<h2 class="ds-h2">Anatomy</h2><h3 class="ds-h3 ds-group">Small</h3>' + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout" id="b-anat" role="img" aria-label="Anatomy of a Small banner: 1 left edge, 2 status icon, 3 title, 4 text, 5 inline link, 6 close"><div class="ds-callout__art"><div id="a-host"></div></div></div></figure></div>' + \
    ol_parts([('Left edge', '2px, in the status color.'), ('Status icon', '24px. Informational may take an icon of its own.'), ('Title', 'Optional. <code>label-sm</code>, bold, uppercase.'), ('Text', '<code>body-sm</code>, 14/20 (mobile 12/18).'), ('Inline link', 'Optional. Small Bold, 14/20, between the text and the ×.'), ('Close', 'A Blank icon button, 20px icon. Shown or hidden by the administrator.')]) + \
    '<h3 class="ds-h3 ds-group">Large</h3>' + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout" id="bl-anat" role="img" aria-label="Anatomy of a Large banner: 1 left edge, 2 status icon, 3 heading, 4 body, 5 actions, 6 close"><div class="ds-callout__art"><div id="al-host"></div></div></div></figure></div>' + \
    ol_parts([('Left edge', '8px on desktop, 4px below.'), ('Status icon', '48px (40px tablet, 24px mobile).'), ('Heading', '<code>title-md</code>, bold.'), ('Body', '<code>body-md</code>.'), ('Actions', 'Buttons <strong>or</strong> inline links, indented to line up under the text.'), ('Close', 'A Blank icon button.')]) + \
    '<h3 class="ds-h3 ds-group">Promotion</h3>' + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout" id="bp-anat" role="img" aria-label="Anatomy of a Promotion banner: 1 title, 2 link, 3 close"><div class="ds-callout__art"><div id="ap-host"></div></div></div></figure></div>' + \
    ol_parts([('Title', 'Uppercase, <code>label-md</code>. Followed by “ -” on desktop.'), ('Link', 'An inline link. The whole banner is the click target.'), ('Close', 'A Blank icon button (inverted on Dark).')])

variants = '<h2 class="ds-h2">Variants</h2>' + desc('Three kinds of banner. <strong>Small</strong> is the everyday banner for status and campaigns. <strong>Large</strong> is a richer message for signed-in customers, shown on My Pages only. <strong>Promotion</strong> is for brand campaigns and has no status.') + bp_toolbar('vb-l') + \
    '<h3 class="ds-h3 ds-group">Small</h3>' + desc('One line of text with an optional uppercase title and an optional <strong>inline link</strong> before the ×. Height 48px on desktop, 40px on mobile. The first two examples carry a link.') + fig_one_id('v-small') + \
    '<h3 class="ds-h3 ds-group">Large</h3>' + desc('A big icon, a heading, body copy and an action group with buttons and an optional link. Use it for a message to a signed-in customer or customer group, not for a one-line status.') + fig_one_id('v-large') + \
    '<h3 class="ds-h3 ds-group">Promotion</h3>' + desc('A centered campaign line in black, white or the brand’s own accent color. <strong>Strong</strong> and <strong>Weak</strong> read the accent tokens, so they are lime on Swedol and red on Tools without any extra code.') + fig_one_id('v-promo') + \
    '<h3 class="ds-h3 ds-group">Emphasis</h3>' + desc('Each status comes in three levels. <strong>Strong</strong> is a solid color with white text and is the loudest, <strong>Weak</strong> is tinted, <strong>Weaker</strong> is white with a colored edge and a shadow. Choose by how much the user must notice it: Weaker for general information and offers, Weak for something to notice, Strong only for what is urgent. All combinations are under ' + sec_link(SLUG, 'states', 'States') + ' in Specifications.')

sizes = '<h2 class="ds-h2">Sizes</h2>' + desc('Small is 48px high on desktop and 40px below. Large changes its icon, padding and text at each breakpoint. Promotion is 48px on desktop and 32px on mobile. All values are under ' + sec_link(SLUG, 'sizes', 'Sizes') + ' in Specifications.') + bp_toolbar('sb-l') + \
    '<h3 class="ds-h3 ds-group">Small</h3>' + fig_one_id('v-s-small') + '<h3 class="ds-h3 ds-group">Large</h3>' + fig_one_id('v-s-large') + '<h3 class="ds-h3 ds-group">Promotion</h3>' + fig_one_id('v-s-promo')

layout = '<h2 class="ds-h2">Layout &amp; Appearance</h2><h3 class="ds-h3 ds-group">Alignment</h3>' + desc('Everything in a Small banner is top-aligned on one row: the icon, the text, the inline link and the ×. In Large the actions start under the text. Promotion is centered on desktop; on mobile the title is on the left and the link and the × on the right.') + \
    '<h3 class="ds-h3 ds-group">Placement</h3>' + desc('Banners go at the top of the page: above or below the site header, beneath the breadcrumb, or on top of the My Pages dashboard. Where each size goes, and which banner wins when several fit, is under <a class="inline-link inline-link--large inline-link--secondary" href="#placement-and-priority">Placement and priority</a>.') + \
    '<h3 class="ds-h3 ds-group">Width</h3>' + desc('A banner is always 100% of its container.') + \
    '<h3 class="ds-h3 ds-group">Appearance</h3>' + desc('Every banner has the elevation <code>b-20</code>. Strong is a solid status color; Weak is tinted with a 1px edge; Weaker is white. Token names and values are under ' + sec_link(SLUG, 'design-tokens', 'Design Tokens') + ' in Specifications.')

placement = '<h2 class="ds-h2">Placement and priority</h2>' + desc('An administrator sets up each banner: its text and size, which pages it shows on, which customers or industries (SNI codes) it targets, and an optional date range. Three of those decisions are shown below.') + \
    '<h3 class="ds-h3 ds-group">Where a banner goes</h3>' + desc('Examples from the design (Figma: Banner placement examples). Placement and size depend on the page type; the table below sums it up.') + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage"><div class="pg-figs">' + \
    '<figure class="pg-fig"><img src="/images/banner-placement-home.png" alt="Home page with an error banner above the header and two informational banners below it" loading="lazy" /><figcaption><b>All pages, desktop.</b> <em>Header top:</em> an Error banner (Strong) directly above the site header. <em>Header bottom:</em> two informational Weak banners directly below it.</figcaption></figure>' + \
    '<figure class="pg-fig"><img src="/images/banner-placement-pdp-desktop.png" alt="Product page with a promotion banner above the header, an informational banner below it and a banner beneath the breadcrumb" loading="lazy" /><figcaption><b>PDP, desktop.</b> <em>Header top:</em> Promotion (accent, Strong). <em>Header bottom:</em> Informational Weak. <em>Beneath the breadcrumb:</em> a customer-specific Informational Weaker banner. In the buy box, Inline notifications carry product information.</figcaption></figure>' + \
    '<figure class="pg-fig pg-fig--mobile"><img src="/images/banner-placement-pdp-mobile.png" alt="Product page on mobile with the same banner stack" loading="lazy" /><figcaption><b>PDP, mobile.</b> The same placements on mobile, with the mobile sizes (40px Small banners).</figcaption></figure>' + \
    '<figure class="pg-fig"><img src="/images/banner-placement-mypages.png" alt="My Pages with an administrator banner and a promotion above the header and a Large banner on the dashboard" loading="lazy" /><figcaption><b>My pages, desktop.</b> <em>Header top:</em> Informational Strong (administrator acting as a customer) and a Promotion (Light). <em>In the dashboard:</em> a Large banner (Informational Weaker), on top of the dashboard content.</figcaption></figure>' + \
    '</div></div></figure></div>' + \
    table(['Page', 'Banner size', 'Placement', 'Targeting'], [['PDP', 'Small', 'Beneath the breadcrumb', 'Banner setting, SNI codes, customer IDs, dates'], ['PLP', 'Small', 'Beneath the breadcrumb', 'Banner setting, SNI codes, customer IDs, dates'], ['My pages', 'Large', 'In the context of the dashboard, on top of it', 'Banner setting, SNI codes, customer IDs, dates'], ['All pages', 'Small', 'Header top (directly above the site header) or header bottom (directly below it)', 'Banner setting, SNI codes, customer IDs, dates']]) + \
    note('Every banner can also target one or more SNI codes (industry codes), one or more customer IDs, and a start and end date. <strong>Norway and Finland</strong> use the equivalent industry classification of their own country where one exists (for example SN2007 in Norway and TOL 2008 in Finland), in the same field as the Swedish SNI code.') + \
    '<h3 class="ds-h3 ds-group">Which banner wins</h3>' + desc('When more than one banner matches the same visitor and place, <strong>only the one with the highest priority shows</strong>. The administrator labels each banner with one of four priorities: 1 is strongest. On top of those sits <strong>level 0, Opt-out</strong>: a company can choose to see no banners at all, and that choice overrides every level, alerts included.') + \
    '<h3 class="ds-h3" id="persona-h">Meet Axel Bonde AB</h3>' + desc('<strong>Persona:</strong> Axel Bonde AB is a signed-in customer who runs a farm. One visitor can fit several levels at once: Axel has a customer ID (so a banner can be written for him personally), his business has an SNI code for farming (so an industry banner fits), and he is a customer like everyone else (so the general campaign fits). Press a row below to say whether that banner applies to Axel, then read what he sees and why.') + \
    '<div class="ds-table-wrap"><table class="ds-table pg-matrix" id="prio-table"><thead><tr><th scope="col">Priority</th><th scope="col">Banner</th><th scope="col">Applies to Axel?</th><th scope="col">Result for Axel</th></tr></thead><tbody></tbody></table></div>' + \
    '<h3 class="ds-h3">What Axel sees</h3><div class="ds-stage" id="prio-stage" aria-live="polite" style="min-height:96px"></div>'

behavior = '<h2 class="ds-h2">Behavior</h2><h3 class="ds-h3 ds-group">Dismissal</h3>' + desc('The × hides the banner with a fade and a height collapse, so no gap is left. Whether the × exists at all is decided by the banner’s owner, not by the component.') + \
    '<h3 class="ds-h3 ds-group">Persistence</h3>' + desc('A banner never disappears by itself. It stays until it is closed or the state changes.') + \
    '<h3 class="ds-h3 ds-group">Hover and focus</h3>' + desc('Only the ×, the buttons and the links have states. They take focus with a visible ring, on keyboard use only. In Promotion the whole banner is the click target. All states are under ' + sec_link(SLUG, 'states', 'States') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Motion</h3>' + desc('Closing is a fade and a collapse: accelerate easing, 150ms. Try other values under <a class="inline-link inline-link--large inline-link--secondary" href="#motion">Motion</a> above, and see ' + sec_link(SLUG, 'motion', 'Motion') + ' in Specifications.')

access = '<h2 class="ds-h2">Accessibility</h2>' + desc('All requirements are listed under ' + sec_link(SLUG, 'accessibility-requirements', 'Accessibility Requirements') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Keyboard support</h3>' + desc('Tab moves to the ×, the buttons and the links, each with a visible focus ring. In Promotion the ring follows the clickable banner.') + \
    '<h3 class="ds-h3 ds-group">Screen reader support</h3>' + desc('A Strong or Error banner for an outage should use <code>role="alert"</code>; other banners need no role. Place the banner at the top of the content in the DOM so screen reader users meet it first. The status is carried by the icon and the text, not by color alone.')

related = '<h2 class="ds-h2">Related</h2><ul class="ds-bullets"><li><strong>' + link_large('toast.html', 'Toast') + '</strong>. Feedback on something the user just did.</li><li><strong>' + link_large('inline.html', 'Inline notification') + '</strong>. Status that belongs to one section or form.</li><li><strong>' + link_large('modal.html', 'Modal') + '</strong>. A decision before the user can go on.</li><li><strong>' + link_large('notifications.html', 'Notifications guide') + '</strong>. Which notification to choose.</li></ul>'

references = '<h2 class="ds-h2">References</h2>' + refs([
    ('https://www.w3.org/WAI/WCAG22/Understanding/status-messages.html', 'WCAG 2.2: Status Messages', 'Success criterion 4.1.3.'),
    ('https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html', 'WCAG 2.2: Use of Color', 'Success criterion 1.4.1.'),
    ('https://carbondesignsystem.com/components/notification/usage/', 'Carbon Design System: Notification', 'IBM.'),
    ('https://spectrum.adobe.com/page/in-line-alert/', 'Adobe Spectrum: In-line alert', 'Adobe.')])

ex = [('playground', playground), ('overview', overview), ('usage', usage), ('anatomy', anatomy), ('variants', variants), ('sizes', sizes), ('layout', layout), ('placement-and-priority', placement), ('behavior', behavior), ('accessibility', access), ('related', related), ('references', references)]

# ---------------------------------------------------------------- Specifications
st_tok = '<h2 class="ds-h2">Design Tokens</h2>' + desc('Resolved from the live token package. <code>{status}</code> is <code>information</code>, <code>success</code>, <code>warning</code> or <code>danger</code> (Error).') + \
    '<h3 class="ds-h3 ds-group">Emphasis</h3>' + table(['Emphasis', 'Background', 'Left edge', 'Text', 'Shadow'], [['Strong', '<code>surface-{status}-default</code>', '<code>surface-{status}-weaker</code>', '<code>text-primary-inverted</code>', 'Large only'], ['Weak', '<code>surface-{status}-weaker</code>', '<code>surface-{status}-default</code>', '<code>text-primary</code>', 'Large only'], ['Weaker', '<code>surface-raised-primary</code>', '<code>surface-{status}-default</code>', '<code>text-primary</code>', 'Always (<code>elevation-b-20</code>)']]) + \
    '<h3 class="ds-h3 ds-group">Tokens</h3>' + '<div class="ds-table-wrap"><table class="ds-table" id="tok-table"><thead><tr><th scope="col">Emphasis</th><th scope="col">Part</th><th scope="col">Token</th><th scope="col">Value</th></tr></thead><tbody></tbody></table></div>'

st_sizes = '<h2 class="ds-h2">Sizes</h2>' + table(['Property', 'Desktop (769px+)', 'Tablet (640–768px)', 'Mobile (below 640px)'], [
    ['Small height', '48px min', '40px min', '40px min'], ['Small padding', '12px / 16px', '8px / 16px', '8px / 16px'], ['Small text', '14/20, 0.36px; title 14px, 0.56px', '12/18, 0.24px; title 12px, 0.48px', '12/18; title 12px'],
    ['Large left edge', '8px', '4px', '4px'], ['Large icon', '48px', '40px', '24px'], ['Large padding', '24px', '16px', '12px, 12px, 16px (top, sides, bottom)'], ['Large gap icon to text', '12px', '12px', '8px'],
    ['Large heading / body', '20/24 / 17/24', '18/22 / 16/22', '18/22 / 16/22'], ['Large action indent', '60px', '52px', '32px'], ['Promotion height', '48px', '40px', '32px'], ['Width', '100% of the container', '100%', '100%']]) + \
    note('Promotion on tablet keeps the mobile layout (title left, link and × right); the Figma heights are 48px desktop and 32px mobile.')

st_meas = '<h2 class="ds-h2">Measurements</h2><h3 class="ds-h3 ds-group">Dimensions</h3>' + desc('The padding of a Small and a Large banner. The shaded area is the padding; the status edge sits outside it. The numbers are read from the component.') + bp_toolbar('mb-l') + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-fig__stage--flush" style="padding:0;min-height:0"><div class="measure ms-banner" id="ms" role="img" aria-label="Padding of a Small and a Large banner"></div></div><figcaption class="ds-fig__cap">A Small and a Large banner. Change the Breakpoint to see the tablet and mobile values.</figcaption></figure></div>' + \
    table(['Attribute', 'Desktop (769px+)', 'Tablet (640–768px)', 'Mobile (below 640px)'], [['Small padding', '12px above and below, 16px sides', '8px above and below, 16px sides', 'same as tablet'], ['Large padding', '24px', '16px', '12px, 12px, 16px (top, sides, bottom)'], ['Large left edge', '8px', '4px', '4px'], ['Large gap icon to text', '12px', '12px', '8px'], ['Large space above the actions', '24px', '24px', '24px'], ['Promotion padding', '12px above and below, 48px sides', '4px above and below, 8px sides', 'same as tablet']]) + \
    '<h3 class="ds-h3 ds-group">Spacing</h3>' + desc('The same distances as spacing tokens.') + table(['Part', 'Value'], [['Small padding, desktop', '<code>space-12</code> and <code>space-16</code>'], ['Small padding, mobile', '<code>space-8</code> and <code>space-16</code>'], ['Large padding, desktop', '<code>space-24</code>'], ['Large padding, tablet', '<code>space-16</code>'], ['Large padding, mobile', '<code>space-12</code> and <code>space-16</code>'], ['Icon to text', '<code>space-8</code> (Large: <code>space-12</code> from 640px)'], ['Left edge, Small', '<code>space-2</code>']])

st_elev = '<h2 class="ds-h2">Elevation</h2>' + table(['Part', 'Token', 'Value'], [['Every banner', '<code>shadow-elevation-b-20</code>', 'Small, Large and Promotion, all emphasis levels. Set once on <code>.banner-notification</code>.']])

st_states = '<h2 class="ds-h2">States</h2>' + desc('Each status in three emphasis levels. A banner has no hover or focus state of its own; only the × and its links do. Choose the level by how much the user must notice it: see ' + link_large('notifications.html#emphasis', 'Choosing the emphasis') + '.') + \
    toolbar([('ss-l', 'Size', 'data-mx="size"', [('small', 'Small', True), ('large', 'Large', False)]), ('sb-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force')]) + \
    '<div class="ds-table-wrap"><table class="ds-table pg-matrix" id="matrix"><thead><tr><th scope="col">Status</th><th scope="col">Strong</th><th scope="col">Weak</th><th scope="col">Weaker</th></tr></thead><tbody></tbody></table></div>'

st_typo = '<h2 class="ds-h2">Typography</h2>' + table(['Element', 'Token', 'Mobile and tablet', 'Desktop (769px+)'], [['Small title', '<code>label-sm</code>, bold, uppercase', '12/12, 0.48px', '14/14, 0.56px'], ['Small text', '<code>body-sm</code>', '12/18, 0.24px', '14/20, 0.36px'], ['Inline link, Small', 'Small Bold', '14/20', '14/20'], ['Large heading', '<code>title-md</code>', '18/22, bold', '20/24, bold'], ['Large body', '<code>body-md</code>', '16/22, 0.32px', '17/24, 0.32px'], ['Promotion title', '<code>label-md</code>', '14/16, 0.42px', '18/18, 0.18px'], ['Promotion link', '<code>body-sm</code> / <code>body-md</code>', '14/16, 0.36px', '17/24, 0.32px']])

st_struct = '<h2 class="ds-h2">Structure</h2><h3 class="ds-h3 ds-group">Elements</h3>' + table(['Element', 'Class', 'Notes'], [
    ['Banner', '<code>banner-notification banner-notification--{status} banner-notification--{emphasis}</code>', 'Emphasis: <code>strong</code>, <code>weak</code>, <code>weaker</code>. Add <code>--large</code> for Large.'], ['Small', '<code>__base</code>, <code>__left-border</code>, <code>__container</code>, <code>__inner</code>, <code>__content</code>', 'Edge, container, text row.'],
    ['Icon, title, text', '<code>__icon</code>, <code>__title</code>, <code>__text</code>', 'The icon is a <code>material-symbols-outlined</code> span.'], ['Inline link', '<code>__links</code>', 'Small: between the text and the ×.'], ['Large', '<code>__main</code>, <code>__textblock</code>, <code>__heading</code>, <code>__body</code>, <code>__footer</code>, <code>__btns</code>', 'Icon, heading, body, actions.'],
    ['Promotion', '<code>banner-notification--promotion banner-notification--{dark|light|accent-strong|accent-weak}</code>', 'No status. <code>__promo</code> holds the title and the link.'], ['Close', '<code>icon-btn icon-btn--close</code>', 'Add <code>icon-btn--close-inverted</code> on Strong and Dark.']]) + \
    '<h3 class="ds-h3 ds-group">Types</h3>' + table(['Kind', 'Emphasis', 'Statuses'], [['Small', 'Strong, Weak, Weaker', 'Informational, Success, Warning, Error'], ['Large (My Pages only)', 'Strong, Weak, Weaker', 'Informational, Success, Warning, Error'], ['Promotion', 'Dark, Light, Strong (accent), Weak (accent)', 'None']]) + \
    '<h3 class="ds-h3 ds-group">Width</h3>' + desc('Always 100% of the container.')

st_motion = '<h2 class="ds-h2">Motion</h2>' + table(['Property', 'Token', 'Value'], [['Close: <code>opacity</code>, <code>height</code>, margin and padding', '<code>--n-close-duration</code>', 'Default <code>duration-fast-3</code> (150ms)'], ['Easing', '<code>--n-close-ease</code>', 'Default <code>ease-accelerate-generic</code>'], ['Height collapse', '<code>data-n-close="fade"</code> on an ancestor turns it off', 'On by default']]) + \
    note('Reduced motion: the banner is hidden at once. Slow durations (450ms or more) and decelerate easings are wrong for an exit. Compare values in the live Motion section on <a class="inline-link inline-link--medium inline-link--secondary" href="banner.html#motion">Examples &amp; Guidelines</a>.')

st_behavior = '<h2 class="ds-h2">Behavior</h2>' + table(['Input', 'Result'], [
    ['Click ×', 'Hides the banner. Whether the × exists is decided by the banner’s owner.'], ['Persistence', 'A banner never disappears by itself. It stays until it is closed or the state changes.'], ['Tab', 'The ×, buttons and links take focus with a visible ring.'],
    ['Inline link', 'Underlined when enabled; on hover the underline goes and the color changes (<code>eco-inline-link</code>, Medium; inverted on Strong and Promotion Dark). Brand-accent Promotion keeps its text color on hover.'], ['Order', 'Place the banner at the top of the content in the DOM so screen reader users meet it first.']])

st_access = '<h2 class="ds-h2">Accessibility Requirements</h2>' + table(['Topic', 'Requirement'], [
    ['Markup', 'A Strong or Error banner for an outage should use <code>role="alert"</code>; other banners need no role.'], ['Status', 'The icon and the text carry the status, not the color alone (WCAG 1.4.1).'], ['Focus', 'The ×, buttons and links have a 2px ring, <code>border-focus</code>, on keyboard use (WCAG 2.4.7).'],
    ['Contrast', 'Strong uses white text on the solid status color; Weak and Weaker use <code>text-primary</code>.'], ['Reduced motion', 'The banner is hidden without a transition under <code>prefers-reduced-motion: reduce</code>.']])

spec = [('design-tokens', st_tok), ('sizes', st_sizes), ('measurements', st_meas), ('elevation', st_elev), ('states', st_states), ('typography', st_typo), ('structure', st_struct), ('motion', st_motion), ('behavior', st_behavior), ('accessibility-requirements', st_access)]

# ---------------------------------------------------------------- Code
c_basic = '<h2 class="ds-h2">Basic Usage</h2>' + desc('Link the shared files once per page. Never copy the rules into a page.') + table(['Step', 'What to do'], [
    ['1. Link', '<code>&lt;link rel="stylesheet" href="/eco-design-system/notifications.css"&gt;</code> and <code>&lt;script src="/eco-design-system/notifications.js"&gt;&lt;/script&gt;</code>. Link <code>button.css</code> first. The script makes the × work.'], ['2. Markup', 'Copy a recipe below. Put the banner at the top of the content.'],
    ['3. Choose', 'Status class, emphasis class (<code>weak</code> is the default), size (Small, or <code>--large</code> on My Pages) or Promotion.'], ['4. Close button', 'Leave out the × when the banner may not be closed.']])
c_banner = '<h2 class="ds-h2">Banner</h2><div id="recipes"></div>' + note('The markup has no motion. The closing animation is set in <a class="inline-link inline-link--medium inline-link--secondary" href="banner.html#motion">Motion</a> on Examples &amp; Guidelines.')
c_api = '<h2 class="ds-h2">API</h2><h3 class="ds-h3 ds-group">Classes</h3>' + table(['Class', 'Use'], [['<code>banner-notification--{info|success|warning|error}</code>', 'The status.'], ['<code>banner-notification--{strong|weak|weaker}</code>', 'The emphasis.'], ['<code>banner-notification--large</code>', 'Large (My Pages only).'], ['<code>banner-notification--promotion</code> and <code>--{dark|light|accent-strong|accent-weak}</code>', 'Promotion.']]) + \
    '<h3 class="ds-h3 ds-group">Custom properties and attributes</h3>' + table(['Name', 'Use'], [['<code>--n-close-ease</code>, <code>--n-close-duration</code>', 'Closing motion. Defaults: <code>ease-accelerate-generic</code>, <code>duration-fast-3</code>.'], ['<code>data-n-close="fade"</code>', 'On the banner or an ancestor: fade only, no height collapse.'], ['<code>n-dismissed</code>', 'Event, bubbles, fired when the banner is hidden.']]) + \
    '<h3 class="ds-h3 ds-group">Things to know</h3>' + bullets(['The × is the Close icon button; the script hides the banner with <code>hidden</code>.', 'A Promotion banner takes its accent from the brand tokens: do not hardcode a color.', 'Buttons inside a banner are always 32px high, also when <code>button.css</code> is on the page.'])
c_css = '<h2 class="ds-h2">CSS / Tailwind</h2>' + desc('The component is one CSS file and one script, shared by every notification. Link them, never copy them. The code below is read from the files the page links, so it is always what you see.') + '<div id="files"></div>'
code = [('basic-usage', c_basic), ('banner', c_banner), ('api', c_api), ('css-tailwind', c_css, False)]

# ---------------------------------------------------------------- scripts
JS_SAMPLE = JS_PRE + r'''
  var TXT = { info: 'Free shipping on orders over 1 000 kr.', success: 'Your price list was updated.', warning: 'Planned maintenance on Sunday 02:00–04:00.', error: 'The site is slow right now. We are working on it.' };
  function ban(o) { return mk(H.banner(o)); }
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
  var EM = { small: [['strong', 'Strong'], ['weak', 'Weak'], ['weaker', 'Weaker']], large: [['strong', 'Strong'], ['weak', 'Weak'], ['weaker', 'Weaker']], promotion: [['dark', 'Dark'], ['light', 'Light'], ['accent-strong', 'Strong'], ['accent-weak', 'Weak']] };
  var pg = { size: 'small', status: 'info', emphasis: 'weak', acts: 'buttons', closable: 'on' };
  function pgOpts() {
    var o = { size: pg.size, status: pg.status, emphasis: pg.emphasis, closable: pg.closable === 'on' };
    if (pg.size !== 'promotion' && pg.status === 'info' && $('#pg-ic').value.trim()) o.icon = $('#pg-ic').value.trim();
    if (pg.size === 'small') { o.title = $('#pg-title').value; o.text = $('#pg-text').value; if ($('#pg-sl').value) o.links = [$('#pg-sl').value]; }
    if (pg.size === 'large') { o.heading = $('#pg-title').value; o.body = $('#pg-text').value; if (pg.acts === 'links') o.links = [$('#pg-l1').value, $('#pg-l2').value].filter(Boolean); else { o.secondary = $('#pg-b2').value; o.primary = $('#pg-b1').value; } }
    if (pg.size === 'promotion') { o.title = $('#pg-title').value; o.link = $('#pg-link').value; }
    return o;
  }
  function emSeg() {
    var g = clear($('#pg-em'));
    EM[pg.size].forEach(function (e) { var b = document.createElement('button'); b.type = 'button'; b.dataset.v = e[0]; b.textContent = e[1]; b.setAttribute('aria-pressed', String(e[0] === pg.emphasis)); g.appendChild(b); });
  }
  function renderPg() {
    if (mo) mo.render();
    var o = pgOpts(); clear($('#pg-host')).appendChild(ban(o)); $('#pg-code').textContent = H.banner(o);
    $('#f-ic').hidden = pg.size === 'promotion' || pg.status !== 'info';
    var lg = pg.size === 'large'; $('#pg-acts-f').hidden = !lg; $('#f-sl').hidden = pg.size !== 'small';
    ['b2', 'b1'].forEach(function (k) { $('#pg-' + k + '-f').hidden = !lg || pg.acts !== 'buttons'; });
    ['l1', 'l2'].forEach(function (k) { $('#pg-' + k + '-f').hidden = !lg || pg.acts !== 'links'; });
    $('#f-status').hidden = pg.size === 'promotion'; $('#f-link').hidden = pg.size !== 'promotion';
    $('#l-title').textContent = pg.size === 'large' ? 'Heading' : pg.size === 'promotion' ? 'Campaign title' : 'Title (optional)';
    $('#l-text').textContent = pg.size === 'large' ? 'Body' : 'Text'; $('#l-text').parentNode.hidden = pg.size === 'promotion';
  }
  DK.seg($('[data-pg="size"]'), function (v) {
    pg.size = v; pg.emphasis = EM[v].map(function (e) { return e[0]; }).indexOf(pg.emphasis) > -1 ? pg.emphasis : EM[v][0][0];
    if (v === 'large') { $('#pg-title').value = 'We have gone paperless with invoices'; $('#pg-text').value = 'Invoices are always attached to your delivery confirmation email. You can also download them from your order history.'; }
    if (v === 'small') { $('#pg-title').value = 'Planned maintenance'; $('#pg-text').value = TXT.warning; }
    if (v === 'promotion') { $('#pg-title').value = 'Autumn campaign'; }
    emSeg(); renderPg();
  });
  ['status', 'acts', 'closable'].forEach(function (k) { DK.seg($('[data-pg="' + k + '"]'), function (v) { pg[k] = v; renderPg(); }); });
  DK.seg($('#pg-em'), function (v) { pg.emphasis = v; renderPg(); });
  ['#pg-title', '#pg-text', '#pg-ic', '#pg-sl', '#pg-link', '#pg-b2', '#pg-b1', '#pg-l1', '#pg-l2'].forEach(function (s) { $(s).addEventListener('input', renderPg); });
  $('#pg-reset').addEventListener('click', renderPg);

  /* Usage figures */
  clear($('#fig-do-1')).appendChild(ban({ size: 'small', status: 'warning', emphasis: 'weak', title: 'Planned maintenance', text: 'The site is unavailable on Sunday 02:00–04:00.' }));
  clear($('#fig-dont-1')).appendChild(ban({ size: 'small', status: 'success', emphasis: 'weak', text: 'Settings saved.' }));
  clear($('#fig-do-2')).appendChild(ban({ size: 'small', status: 'info', emphasis: 'weaker', icon: 'package_2', title: 'Free delivery', text: 'Free delivery on all orders. Valid 1/7 – 1/11.' }));
  clear($('#fig-dont-2')).appendChild(ban({ size: 'small', status: 'info', emphasis: 'strong', icon: 'package_2', title: 'Free delivery', text: 'Free delivery on all orders. Valid 1/7 – 1/11.' }));
  clear($('#fig-do-3')).appendChild(ban({ size: 'small', status: 'info', emphasis: 'weak', text: 'You are logged in as an administrator.' }));
  clear($('#fig-dont-3')).appendChild(ban({ size: 'large', status: 'info', emphasis: 'weak', heading: 'You are logged in', body: 'You are logged in as an administrator.' }));

  /* Anatomy */
  function rng(el) { return function () { var r = document.createRange(); r.selectNodeContents(el); return r.getBoundingClientRect(); }; }
  var as = ban({ size: 'small', status: 'warning', emphasis: 'weak', title: 'Title', text: 'Body text explains what is happening.', links: ['Link'] });
  clear($('#a-host')).appendChild(as);
  DK.callouts($('#b-anat'), [
    { n: 1, el: $('.banner-notification__left-border', as), side: 'left', len: 36, at: 'edge' },
    { n: 2, el: $('.banner-notification__icon', as), side: 'top', len: 40, at: 'center' },
    { n: 3, el: $('.banner-notification__title', as), side: 'bottom', len: 40 },
    { n: 4, box: rng($('.banner-notification__text', as)), side: 'top', len: 40 },
    { n: 5, el: $('.banner-notification__links', as), side: 'bottom', len: 40 },
    { n: 6, el: $('.icon-btn--close', as), side: 'top', len: 40, at: 'center' }
  ]);
  var al = ban({ size: 'large', status: 'info', emphasis: 'weaker', icon: 'nest_eco_leaf', heading: 'We have gone paperless with invoices', body: 'Invoices are always attached to your delivery confirmation email.', secondary: 'Go to cart', primary: 'Choose accessories' });
  clear($('#al-host')).appendChild(al);
  DK.callouts($('#bl-anat'), [
    { n: 1, el: $('.banner-notification__left-border', al), side: 'left', len: 36, at: 'edge' },
    { n: 2, el: $('.banner-notification__icon', al), side: 'top', len: 40, at: 'center' },
    { n: 3, box: rng($('.banner-notification__heading', al)), side: 'top', len: 40 },
    { n: 4, box: rng($('.banner-notification__body', al)), side: 'bottom', len: 40 },
    { n: 5, el: $('.banner-notification__footer', al), side: 'bottom', len: 40 },
    { n: 6, el: $('.icon-btn--close', al), side: 'top', len: 40, at: 'center' }
  ]);
  var ap = ban({ size: 'promotion', emphasis: 'dark', title: 'Autumn campaign', link: 'View campaign' });
  clear($('#ap-host')).appendChild(ap);
  DK.callouts($('#bp-anat'), [
    { n: 1, el: $('.banner-notification__title', ap), side: 'top', len: 40 },
    { n: 2, el: $('.inline-link', ap), side: 'bottom', len: 40 },
    { n: 3, el: $('.icon-btn--close', ap), side: 'top', len: 40, at: 'center' }
  ]);

  /* Variants and sizes */
  STATUS.forEach(function (s, i) { $('#v-small').appendChild(ban({ size: 'small', status: s[0], emphasis: ['strong', 'weak', 'weaker', 'weak'][i], title: s[1], text: TXT[s[0]], links: i < 2 ? ['Log out'] : undefined })); });
  [['info', 'strong', 'nest_eco_leaf'], ['warning', 'weak'], ['success', 'weaker']].forEach(function (c) {
    $('#v-large').appendChild(ban({ size: 'large', status: c[0], emphasis: c[1], icon: c[2], heading: c[0] === 'info' ? 'We have gone paperless with invoices' : c[0] === 'warning' ? 'Your agreement ends soon' : 'Your account is verified', body: 'Invoices are always attached to your delivery confirmation email. You can also download them from your order history.', secondary: 'Go to cart', primary: 'Choose accessories' }));
  });
  $('#v-large').appendChild(ban({ size: 'large', status: 'success', emphasis: 'weaker', heading: 'Your account is verified', body: 'You can now order on account. This Large banner uses inline links instead of buttons.', links: ['View account', 'Read more'] }));
  [['dark', 'Dark'], ['light', 'Light'], ['accent-strong', 'Strong'], ['accent-weak', 'Weak']].forEach(function (e) { $('#v-promo').appendChild(ban({ size: 'promotion', emphasis: e[0], title: 'Autumn campaign', link: 'View campaign' })); });
  $('#v-s-small').appendChild(ban({ size: 'small', status: 'warning', emphasis: 'weak', title: 'Planned maintenance', text: TXT.warning, links: ['Read more'] }));
  $('#v-s-large').appendChild(ban({ size: 'large', status: 'info', emphasis: 'weaker', icon: 'nest_eco_leaf', heading: 'We have gone paperless with invoices', body: 'Invoices are always attached to your delivery confirmation email. You can also download them from your order history.', secondary: 'Go to cart', primary: 'Choose accessories' }));
  $('#v-s-promo').appendChild(ban({ size: 'promotion', emphasis: 'dark', title: 'Autumn campaign', link: 'View campaign' }));

  /* Priority */
  var PR = [{ k: 'optout', n: '0 · Opt-out', d: 'The company has chosen not to see any banners. Overrides every other level.', o: null },
            { k: 'alert', n: '1 · Alert', d: 'Error, warning, success or information. Concerns every visitor.', o: { size: 'small', status: 'error', emphasis: 'strong', title: 'Problem', text: 'The site is slow right now.' } },
            { k: 'cust', n: '2 · Customer specific', d: 'Written for one customer ID: Axel Bonde AB.', o: { size: 'small', status: 'info', emphasis: 'weaker', title: 'Free delivery for Axel Bonde AB', text: 'Free delivery on all orders. Valid 1/7 – 1/11.', icon: 'package_2' } },
            { k: 'sni', n: '3 · SNI code', d: 'Aimed at an industry: farmers (SNI 01). Axel runs a farm.', o: { size: 'small', status: 'info', emphasis: 'weaker', title: 'Free delivery for all farmers', text: 'Free delivery on all orders. Valid 1/7 – 1/11.', icon: 'package_2' } },
            { k: 'def', n: '4 · Default', d: 'The general campaign every visitor gets.', o: { size: 'small', status: 'info', emphasis: 'weaker', title: 'Free delivery', text: 'Free delivery on all orders. Valid 1/7 – 1/11.', icon: 'package_2' } }];
  var WHY = {
    optout: 'Axel Bonde AB has asked not to see any banners, so the opt-out applies to the whole company. It overrides every other level, alerts included.',
    alert: 'An alert about the site applies to every visitor, Axel included, and an alert always outranks banners aimed at a customer, an industry or everyone. It tells him something is wrong right now, so nothing else competes with it.',
    cust: 'This banner is written for Axel Bonde AB by customer ID. A banner aimed at one named customer is more relevant than one for a whole industry or for everyone, so it wins over the farmer banner and the general campaign.',
    sni: 'No banner is addressed to Axel personally, but he runs a farm (SNI 01). An industry banner is more specific than the general campaign, so it wins over Default.',
    def: 'Nothing more specific applies to Axel, so he sees the general campaign that every visitor gets.' };
  var on = { optout: false, alert: false, cust: true, sni: true, def: true };
  function prio() {
    var win = null, rank = -1;
    PR.forEach(function (p, i) { if (on[p.k] && !win) { win = p; rank = i; } });  /* level 0 (opt-out) is first, so it wins over everything */
    var tb = clear($('#prio-table tbody'));
    PR.forEach(function (p, i) {
      var tr = document.createElement('tr'), th = document.createElement('th'); th.scope = 'row'; th.innerHTML = '<b></b><br><span class="ds-na"></span>'; $('b', th).textContent = p.n; $('span', th).textContent = p.d; tr.appendChild(th);
      var tb2 = document.createElement('td'); if (p.o) tb2.appendChild(ban(p.o)); else tb2.innerHTML = '<span class="ds-na">No banner is shown at all</span>'; tr.appendChild(tb2);
      var tm = document.createElement('td'), btn = document.createElement('button'); tm.dataset.label = 'Applies to Axel?'; btn.type = 'button'; btn.className = 'btn btn--sm ' + (on[p.k] ? 'btn--primary' : 'btn--secondary'); btn.setAttribute('aria-pressed', String(on[p.k]));
      btn.innerHTML = '<span class="btn__label"></span>'; $('span', btn).textContent = on[p.k] ? 'Applies' : 'Does not apply';
      btn.addEventListener('click', function () { on[p.k] = !on[p.k]; prio(); }); tm.appendChild(btn); tr.appendChild(tm);
      var tr2 = document.createElement('td'); tr2.dataset.label = 'Result for Axel';
      if (!on[p.k]) tr2.innerHTML = '<span class="ds-na">Does not apply to Axel</span>';
      else if (p === win) tr2.innerHTML = p.o ? '<b>Axel sees this</b>' : '<b>Axel sees no banners</b>';
      else tr2.textContent = 'Hidden: outranked by ' + win.n.slice(4) + ' (level ' + rank + ')';
      tr.appendChild(tr2); tb.appendChild(tr);
    });
    var st = clear($('#prio-stage'));
    if (win && !win.o) {
      var z = document.createElement('p'); z.className = 'pg-note'; z.innerHTML = '<b>Axel sees no banners at all.</b> <b>Why:</b> ' + WHY.optout + ' <b>Not shown to Axel:</b> every banner that otherwise applies to him.'; st.appendChild(z);
    } else if (win) {
      st.appendChild(ban(win.o));
      var hidden = PR.filter(function (p) { return on[p.k] && p !== win; }).map(function (p) { return p.n.slice(4); });
      var n = document.createElement('p'); n.className = 'pg-note'; n.innerHTML = '<b>Why:</b> ' + WHY[win.k] + (hidden.length ? ' <b>Not shown to Axel:</b> ' + hidden.join(', ') + ', because ' + (hidden.length > 1 ? 'they are' : 'it is') + ' outranked.' : ' No other banner applies, so there is nothing to hide.');
      st.appendChild(n);
    } else { var m = document.createElement('p'); m.className = 'pg-note'; m.textContent = 'No banner applies to Axel, so he sees none.'; st.appendChild(m); }
  }

  mo = DK.motion({ anchor: 'playground', prefix: 'n-close', rec: { ease: 'accelerate-generic', dur: 'fast-3', collapse: true }, role: 'exit', why: 'Closing removes the element: accelerate easing, fast fade, and the height collapses so no gap is left (eco-motion: element disappears).', preview: function () { return ban(pgOpts()); } });
''' + JS_MOTION_FIX + r'''
  DK.bp(); emSeg(); renderPg(); prio();
'''

JS_SPEC = JS_SAMPLE + r'''
  DK.tokenTable($('#tok-table tbody'), [
    ['Strong · Informational', 'Background', 'surface-information-default'], ['Weak · Informational', 'Background', 'surface-information-weaker'], ['Weak · Informational', 'Edge', 'border-information-weaker'], ['Weak · Informational', 'Icon', 'text-information-default'],
    ['Weaker', 'Background', 'surface-raised-primary'], ['Weaker', 'Shadow', 'shadow-elevation-b-20'], ['Promotion · Dark', 'Background', 'surface-100'],
    ['Promotion · Strong', 'Background (brand accent)', 'accent-default'], ['Promotion · Strong', 'Text', 'text-action-accent'], ['Promotion · Weak', 'Background (brand accent)', 'accent-light'], ['Promotion · Weak', 'Text', 'text-action-primary']]);

  /* Measurements */
  $('#ms').appendChild(measureItem('Small', ban({ size: 'small', status: 'warning', emphasis: 'weak', title: 'Title', text: 'Body text explains what is happening.' }), '.banner-notification__inner', '.banner-notification__left-border'));
  $('#ms').appendChild(measureItem('Large', ban({ size: 'large', status: 'info', emphasis: 'weaker', icon: 'nest_eco_leaf', heading: 'Heading', body: 'Body text explains what is happening.', secondary: 'Secondary', primary: 'Blank' }), '.banner-notification__inner', '.banner-notification__left-border'));
  DK.bp(function () { if (window.ECO_MEASURE) ECO_MEASURE.init(); });

  /* States */
  var mx = { size: 'small' };
  function matrix() {
    var tb = clear($('#matrix tbody'));
    STATUS.forEach(function (s) {
      var tr = document.createElement('tr'), th = document.createElement('th'); th.scope = 'row'; th.textContent = s[1]; tr.appendChild(th);
      ['strong', 'weak', 'weaker'].forEach(function (e) {
        var td = document.createElement('td');
        td.appendChild(ban(mx.size === 'small' ? { size: 'small', status: s[0], emphasis: e, title: s[1], text: 'Banner text.', links: ['Link'] } : { size: 'large', status: s[0], emphasis: e, heading: s[1], body: 'Short body copy for the Large banner.', secondary: 'Action' }));
        tr.appendChild(td);
      });
      tb.appendChild(tr);
    });
  }
  DK.seg($('[data-mx="size"]'), function (v) { mx.size = v; matrix(); });
  matrix();
'''

JS_CODE = JS_PRE + r'''
  function ban(o) { return H.banner(o); }
  DK.recipes($('#recipes'), [
    ['Small · Informational · Weak', ban({ size: 'small', status: 'info', emphasis: 'weak', title: 'Title', text: 'Body text.' })],
    ['Small · with an inline link', ban({ size: 'small', status: 'info', emphasis: 'weak', title: 'Title', text: 'Body text.', links: ['Log out'] })],
    ['Small · Error · Strong (outage)', ban({ size: 'small', status: 'error', emphasis: 'strong', title: 'Problem', text: 'The site is slow right now.' })],
    ['Large (My Pages)', ban({ size: 'large', status: 'info', emphasis: 'strong', icon: 'nest_eco_leaf', heading: 'We have gone paperless with invoices', body: 'Invoices are attached to your delivery confirmation email.', secondary: 'Go to cart', primary: 'Choose accessories' })],
    ['Large · Weak · Actionable with inline links', ban({ size: 'large', status: 'success', emphasis: 'weak', heading: 'Your account is verified', body: 'You can now order on account.', links: ['View account', 'Read more'] })],
    ['Promotion · Strong (brand accent)', ban({ size: 'promotion', emphasis: 'accent-strong', title: 'Autumn campaign', link: 'View campaign' })]]);
  DK.printFile($('#files'), '../notifications.css', [['CSS: Banner', ['banner']], ['CSS: shared icon, close button, link and buttons', ['base']]])
    .then(function () { return DK.printFile($('#files'), '../notifications.js', [['JavaScript: the × of Banner and Inline', ['runtime']]]); });
'''

C = dict(BASE, slug=SLUG, title='Banner',
    lead='A banner carries a <strong>page-wide or system-level message</strong>: an outage, planned maintenance, a campaign or a notice to one customer group. It sits at the top and stays until it is closed or the situation changes.',
    lead_ex='Banners are set up by an administrator, not by user actions. Every example is the real component. Figma: ' + FIG + ', ' + FIG_GUIDE + '.',
    lead_spec='Tokens, sizes, measurements, states and requirements. Values come from the live token package and from ' + FIG + '.',
    lead_code='How to build a banner and the CSS behind it. The files are <code>eco-design-system/notifications.css</code> and <code>notifications.js</code>.',
    ex=ex, spec=spec, code=code, js_ex=JS_EX, js_spec=JS_SPEC, js_code=JS_CODE)
C['body_js'] = BODY + [ICON_PICKER]
C['style'] = STYLE

if __name__ == '__main__':
    emit(C)
