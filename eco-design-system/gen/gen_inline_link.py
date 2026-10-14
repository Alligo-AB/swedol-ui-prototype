import re
from build import *

FIGMA = 'https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=1671-52629'
SLUG = 'inline-link'
PARENT = ('links-guide.html', 'Links guide')

STYLE = r'''    .pg-note { font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-tertiary); }
    .pg-col { display: flex; flex-direction: column; align-items: flex-start; gap: 16px; width: 100%; }
    .pg-p { margin: 0; color: var(--color-text-primary); max-width: 560px; }
    .ds-stage--dark .pg-p { color: var(--color-text-primary-inverted); }
    .pg-matrix td { vertical-align: middle; padding-top: 16px; padding-bottom: 16px; }
    .pg-dark { background: var(--color-surface-100); }
    .pg-dark .pg-p { color: var(--color-text-primary-inverted); }
    .pg-ex { font-size: 16px; line-height: 22px; letter-spacing: 0.32px; font-weight: 400; color: var(--color-text-primary); font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1; }   /* body-md: the writing examples (16/22, 17/24 from 769px) */
    @media (min-width: 769px) { .pg-ex { font-size: 17px; line-height: 24px; } }
    #usage .ds-fig__stage { align-items: flex-start; }   /* every Do / Don't box of this page: content at the top */
    .pg-exfigs .ds-fig__stage { min-height: 0; padding: 16px 24px; justify-content: flex-start; align-items: flex-start; }   /* low boxes for short examples; JS makes a Do and a Don't box the same height */
    .pg-exs { width: 100%; }   /* the lines of one Do or Don't figure, one example per line */
    .pg-ex + .pg-ex { margin-top: 12px; }
    .ds-callout__art { padding-right: 24px; }'''

SIZES = [('xlarge', 'XLarge'), ('large', 'Large'), ('medium', 'Medium'), ('small', 'Small')]
WEIGHTS = [('regular', 'Regular'), ('medium', 'Medium'), ('bold', 'Bold')]

def LK(t):
    """A real inline link (Medium) that goes nowhere: the words that carry the link in a writing example."""
    return '<a href="#" class="inline-link inline-link--medium" data-prevent>%s</a>' % t


EXSEP = '</div><div class="pg-ex">'   # one example per line inside a cell


CAPS = iter([
    ('Do link the words that say what the user gets.', 'Do not link filler words.'),
    ('Do let the linked words read as part of the sentence.', 'Do not add “here” as the link.'),
    ('Do use sentence case, and mirror the name of a page.', 'Do not capitalize every word.'),
    ('Do describe the page.', 'Do not use a web address as the link text.'),
    ('Do use the fewest words that make the destination obvious.', 'Do not turn the link into a sentence.'),
    ('Do differentiate links on the same page.', 'Do not repeat the same text for different destinations.'),
    ('Do name the exact action or document.', 'Do not use vague link text.')])


def ex_groups(rows):
    """Writing examples as Do / Don't figures (body-sm). rows: (do, dont); a row ('<strong>Title</strong>', '') starts a new group with its own heading.
    One Do box and one Don't box per category (or per flow), one example per line."""
    do_cap, dont_cap = next(CAPS)
    groups, title = [], None
    cur = []
    for d, n in rows:
        if n == '' and d.startswith('<strong>'):
            if cur or title:
                groups.append((title, cur))
            title, cur = d, []
        else:
            cur.append((d, n))
    groups.append((title, cur))
    out = ''
    def box(x):
        return '<div class="pg-exs"><div class="pg-ex">%s</div></div>' % x
    for t, g in groups:
        if t:
            out += '<h3 class="ds-h3">%s</h3>' % re.sub(r'</?strong>', '', t)
        dos = EXSEP.join(x[0] for x in g if x[0])
        donts = EXSEP.join(x[1] for x in g if x[1])
        out += fig_pair(box(dos), do_cap, box(donts), dont_cap).replace('class="ds-figs"', 'class="ds-figs pg-exfigs"', 1)   # one Do box and one Don't box per category, one example per line
    return out


playground = '<h2 class="ds-h2">Playground</h2>' + desc('The link sits in a sentence, as it should. Choose size, weight, style, underline, color and state and the sentence and its code update. Hover is forced here; the link is live.') + \
    '<div class="ds-playground"><div class="ds-stage ds-stage--center" id="pg-stage"><div id="pg-host"></div></div><div class="ds-controls">' + \
    bp_field('pg-l-bp') + sel('pg-l-size', 'pg-size', 'Size', 'size', SIZES, 'medium') + \
    sel('pg-l-c', 'pg-color', 'Color', 'color', [('primary', 'Primary'), ('secondary', 'Secondary'), ('tertiary', 'Tertiary'), ('inverted', 'Inverted')], 'primary') + \
    sel('pg-l-w', 'pg-weight', 'Weight', 'weight', WEIGHTS, 'regular') + btn_group('pg-l-it', 'Style', 'data-pg="italic"', [('no', 'Normal', True), ('yes', 'Italic', False)]) + \
    btn_group('pg-l-rv', 'Underline', 'data-pg="reverse"', [('no', 'Default', True), ('yes', 'Reverse', False)]) + \
    btn_group('pg-l-st', 'State', 'data-pg="state"', [('enabled', 'Enabled', True), ('hover', 'Hover', False)]) + \
    '<div class="ds-field form-field"><label class="form-label form-label--sm" for="pg-label">Label</label><div class="input-wrap"><div class="input-box input-box--sm"><input class="form-input" type="text" id="pg-label" value="product page" placeholder="Label" /></div></div></div>' + \
    '</div></div><h3 class="ds-h3">Markup for this selection</h3>' + code_box('pg-code', 'HTML')

overview = '<h2 class="ds-h2">Overview</h2>' + desc('An inline link is an underlined text link that flows <strong>within body copy, lists and UI text</strong>. The underline is its affordance: it is underlined when enabled, and on hover the underline goes and the color changes. It is never paired with icons.') + \
    desc('It inherits the typography of the text around it and shows that it can be used through the underline and the state changes. That makes it the default way to link from running text, footers, legal copy and helper text.') + \
    desc('Inline link has four sizes (XLarge, Large, Medium and Small), four colors (Primary, Secondary, Tertiary and Inverted), three weights (Regular, Medium and Bold), an italic style and a reverse underline (underlined on hover only). It is one of three link types: see the ' + link_large('links-guide.html', 'Links guide') + ' for how to choose.') + \
    three_pages(SLUG, 'an inline link', 'the values: tokens, sizes, states and requirements', 'how to add one to a page')

usage = '<h2 class="ds-h2">Usage</h2><h3 class="ds-h3 ds-group">When to use</h3>' + desc('Use an inline link when a word or a phrase in body copy, a list or UI text should take the user somewhere or do something. Use it to:') + \
    bullets(['Link from within body copy, product descriptions or help text', 'Give secondary navigation in footers, in text next to a breadcrumb or in legal copy (“Read more about our delivery terms”)', 'Link a single item in a list, such as related articles or policy documents', 'Jump to an element on the same page: anchor links, such as the entries of a table of contents', 'Link an email address or a phone number in copy (<code>mailto:</code>, <code>tel:</code>)', 'Go to another page in the site or to an external site']) + \
    desc('One line: an underlined text element that navigates to a destination while flowing inline with the surrounding content.') + \
    '<h3 class="ds-h3 ds-group">When not to use</h3>' + \
    '<h3 class="ds-h3">Keep it inside the sentence</h3>' + desc('An inline link on its own line is a standalone link. For that use an ' + link_large('action-link.html', 'Action link') + ' instead.') + \
    fig_pair('<p class="pg-p" id="fig-in-do"></p>', 'Do keep the link inside the sentence.', '<div class="pg-col" id="fig-in-dont"></div>', 'Do not use an inline link on its own line. Use an Action link instead.') + \
    '<h3 class="ds-h3">For the primary action on the surface</h3>' + desc('When the link is the main call to action, use a <code>eco-button</code> (or a link styled as a button).') + \
    '<h3 class="ds-h3">For destinations that are equal peers</h3>' + desc('Destinations that stand side by side in a grid or a scroller are ' + link_large('tile-link.html', 'Tile links') + '.') + \
    '<h3 class="ds-h3">For an action on the current page</h3>' + desc('A link always navigates. Expanding a section, opening a modal or revealing more text is not navigation: use a <code>eco-button</code>, or the component that owns the pattern, for example a ' + link_large('collapsible.html', 'Collapsible') + ' for expanding in place and a ' + link_large('modal.html', 'Modal') + ' for an overlay.') + \
    '<h3 class="ds-h3">For an icon-only trigger</h3>' + desc('A link has no icon. An icon-only trigger is an icon button (<code>eco-button</code>, Icon button), and a link that needs an icon is an ' + link_large('action-link.html', 'Action link') + '.') + \
    '<h3 class="ds-h3">Open new tabs only when needed</h3>' + desc('Do not open a new tab by default. When a link must (<code>target="_blank"</code>, for example a PDF), say so in the link or next to it, and add <code>rel="noopener"</code>.') + \
    '<h3 class="ds-h3">Give the link the style of the text around it</h3>' + desc('An inline link has the same style as its surrounding text: size, line height, letter spacing, weight and italic, on desktop and on mobile. It is not a way to emphasize a word: never make a link larger or bolder than its text. The Medium, Bold and Italic modifiers exist so a link can follow text that has that style.') + \
    fig_pair('<p class="pg-p" id="fig-sz-do"></p>', 'Do give the link the same style as the text around it.', '<p class="pg-p" id="fig-sz-dont"></p>', 'Do not make a link larger or bolder than the text around it.') + \
    '<h3 class="ds-h3">Do not disable a link</h3>' + desc('Avoid disabled links entirely. Remove the link, or show plain text instead. A disabled <code>&lt;a&gt;</code> has no standard semantics, so an inline link has no disabled state.') + \
    '<h3 class="ds-h3 ds-group">Writing link text</h3>' + desc('The link text describes the destination and makes sense out of context: screen reader users often move through the list of links on a page. In the examples the real inline link (Small) shows exactly which words carry the link. The links go nowhere on this page. The examples are in English; on a Swedish page follow the same rules in the Swedish copy around the link.') + \
    '<h3 class="ds-h3">Link the meaningful phrase</h3>' + desc('The link text tells users where the link goes and what they get if they click, also when it is read out of context by a screen reader. Link the words that carry the meaning, such as “read our workwear size guide”. Do not link filler words such as “click here” or “more info” alone.') + \
    ex_groups([('Read more about our work wear on the ' + LK('product page') + '.', 'To read more about our work wear, ' + LK('click here') + '.'), (LK('Track your order'), LK('Click here')), (LK('Read our workwear size guide'), LK('More info')), (LK('Which safety class do I need?'), LK('Click for details')), (LK('View battery compatibility chart'), LK('See more'))]) + \
    '<h3 class="ds-h3">Weave the link into the sentence</h3>' + desc('When a link sits in a sentence, the linked words read as part of the sentence. Never add “here” at the end as the link.') + \
    ex_groups([('You can update your delivery address in ' + LK('Account settings') + '.', 'Find your nearest store ' + LK('here') + '.'), ('Your card was declined. You can ' + LK('update your payment method') + ' or retry the purchase.', 'To add buyers to your account, ' + LK('go here') + '.'), ('Order before 2 pm for same-day pickup at ' + LK('your nearest store') + '.', '')]) + \
    '<h3 class="ds-h3">Use sentence case, except for names and titles</h3>' + desc('Use sentence case that matches the copy around the link, with no trailing punctuation inside the link. If the link points to a specific page, screen or feature, mirror how that destination is capitalized: “Order History” if that is the real name of the page.') + \
    ex_groups([(LK('Edit cart'), LK('Browse Hearing Protection')), ('Go to ' + LK('Order history'), ''), (LK('Browse hearing protection'), '')]) + \
    '<h3 class="ds-h3">Never paste a raw URL as the link text</h3>' + desc('A raw address is hard to read and scan and says nothing about the destination. Describe the page.') + \
    ex_groups([(LK('Visit our help center'), LK('https://support.swedol.se')), (LK('Download the safety datasheet'), LK('https://swedol.se/files/datasheet-4402.pdf'))]) + \
    '<h3 class="ds-h3">Keep it short</h3>' + desc('Use the fewest words that make the destination obvious, typically one to five. A link is a phrase, not a sentence, and never a whole paragraph. If the link approaches a full line, shorten the phrase, not the type size.') + \
    ex_groups([(LK('Apply invoice payment'), LK('Click on this link to set up invoice payment for your company account')), (LK('Compare impact drivers'), LK('Go to the page where you can compare different impact drivers'))]) + \
    '<h3 class="ds-h3">Do not repeat a link text for different destinations</h3>' + desc('Avoid the same link text with different destinations on one page, such as “Read more” five times. Differentiate them.') + \
    ex_groups([(LK('Read more about shipping') + EXSEP + LK('Read more about returns'), LK('Read more') + EXSEP + LK('Read more'))]) + \
    '<h3 class="ds-h3">Use a verb for an action, and name the document</h3>' + desc('Name the exact action or document the link opens, and for a quote or an order the stage the user is in. Include the quote number when you refer to a specific quote. Examples for common B2B flows, one example per line:') + \
    ex_groups([
        ('<strong>Company accounts and invoicing</strong>', ''),
        (LK('Manage company account') + EXSEP + LK('Add authorized buyers') + EXSEP + LK('Download invoice (PDF)') + EXSEP + LK('Set up invoice payment') + EXSEP + LK('View credit limit'), LK('Click here to manage your account') + EXSEP + LK('More about invoicing')),
        ('Your purchase order number will appear on the invoice. You can ' + LK('add a PO number') + ' at checkout.' + EXSEP + 'Need to add more buyers? Manage user permissions in ' + LK('Company settings') + '.', 'To add buyers to your account, ' + LK('go here') + '.'),
        ('<strong>Quotes and bulk orders</strong>', ''),
        (LK('Request a quote') + EXSEP + LK('View quote #48211') + EXSEP + LK('Accept quote') + EXSEP + LK('Convert quote to order') + EXSEP + LK('See volume pricing'), LK('Get more info about bulk discounts')),
        ('Ordering 50+ units? ' + LK('Request a volume quote') + ' and we’ll get back within one business day.' + EXSEP + 'Your quote expires on 15 August. ' + LK('Accept quote') + ' to lock in the price.', ''),
        ('<strong>Reordering and order history</strong>', ''),
        (LK('Reorder previous purchase') + EXSEP + LK('View order history') + EXSEP + LK('Create shopping list') + EXSEP + LK('Import order from file') + EXSEP + LK('Save as recurring order'), LK('Click to see past orders')),
        ('Running low on consumables? Set up a ' + LK('recurring order') + ' for automatic delivery.' + EXSEP + 'You bought this item in March. ' + LK('Reorder the same size') + ' or browse alternatives.', ''),
        ('<strong>Stock, stores and delivery</strong>', ''),
        (LK('Check store stock') + EXSEP + LK('Find your nearest store') + EXSEP + LK('Reserve for pickup') + EXSEP + LK('Track delivery') + EXSEP + LK('Change delivery address'), LK('Availability info here')),
        ('In stock at 12 stores near you. ' + LK('Reserve for pickup') + ' and collect today.' + EXSEP + 'Delivering to a worksite? ' + LK('Add worksite address') + ' at checkout.', ''),
        ('<strong>Workwear and sizing for teams</strong>', ''),
        (LK('Order team workwear') + EXSEP + LK('Add logo printing') + EXSEP + LK('View embroidery options') + EXSEP + LK('Download size chart (EU/SE)'), LK('Learn more about customization')),
        ('Outfitting your whole crew? ' + LK('Order team workwear') + ' with your company logo.' + EXSEP + 'Not sure about sizing? Compare measurements in the ' + LK('size chart') + ' before ordering.', ''),
        ('<strong>Product documentation and compliance</strong>', ''),
        (LK('Download safety datasheet') + EXSEP + LK('View EN 388 certification') + EXSEP + LK('Read user manual') + EXSEP + LK('Check warranty terms'), LK('Documents here')),
        ('This glove is rated for cut protection. ' + LK('View EN 388 certification') + ' for full test results.' + EXSEP + 'Registered your tool? Extend your warranty in ' + LK('My tools') + '.', '')]) + \
    '<h3 class="ds-h3 ds-group">Quick reference</h3>' + \
    table(['The link…', 'Use'], [['is inside a sentence or text block', 'Inline link'], ['stands alone, with an icon', '<a class="inline-link inline-link--small" href="action-link.html">Action link</a>'], ['is a card or a logo', '<a class="inline-link inline-link--small" href="tile-link.html">Tile link</a>'], ['does something in the page', '<code>eco-button</code>']]) + \
    rules(['Link the words that name the destination (“product page”), not “click here”.', 'Give the link the same style as the surrounding text: size, line height, letter spacing, weight and italic.', 'Remove the link or show plain text when the destination is not available.', 'Give the link the same color as the surrounding text: Primary, Secondary or Tertiary, with the matching hover color.', 'Use Inverted on dark surfaces.', 'Keep the underline on default links in running text: color alone is not enough (WCAG 1.4.1).', 'Keep the link text short: a phrase, not a sentence.', 'Use Medium, Bold or Italic only when the text around the link has that style.', 'If a link opens a new tab (PDF, for example), say so and add <code>rel="noopener"</code>.'],
          ['Add an icon to an inline link.', 'Remove the underline in the enabled state (use the reverse underline on purpose).', 'Make a link larger, bolder or more italic than its text for emphasis.', 'Disable a link.', 'Use an inline link on its own line (use Action link).', 'Link whole sentences or wrap a paragraph in a link.', 'Link filler words (“click here”, “read more” alone).', 'Use the default dark link on a dark background.', 'Bold every link.', 'Open new tabs by default.', 'Use a web address as the link text.'])

usage = usage.replace('class="ds-figs"', 'class="ds-figs pg-exfigs"')   # the remaining Do / Don't pairs get the low, equal-height boxes too

anatomy = '<h2 class="ds-h2">Anatomy</h2><h3 class="ds-h3 ds-group">Inline link</h3>' + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout" id="il-anat" role="img" aria-label="Anatomy of an inline link: 1 link text, 2 underline"><div class="ds-callout__art"><p class="pg-p" id="il-anat-p"></p></div></div></figure></div>' + \
    ol_parts([('Link text', 'The words that name the destination, in <code>text-action-primary</code> (Primary). The size follows the text around the link.'), ('Underline', 'Shown when enabled, removed on hover. It is never animated.')]) + \
    desc('An inline link has no icon (an Action link always has one), no padding and no background. It is a real <code>&lt;a href&gt;</code> inside the text.')

variants = '<h2 class="ds-h2">Variants</h2>' + desc('Four colors. A link has the same color as the text around it: Primary, Secondary or Tertiary, and Inverted on dark surfaces. Each has its own hover color (<code>text-action-primary-hover</code>, <code>text-action-secondary-hover</code>, <code>text-action-tertiary-hover</code> and <code>text-action-primary-inverted-hover</code>). Sizes are under Sizes below; weight, italic and reverse underline follow after Inverted.') + \
    '<h3 class="ds-h3 ds-group">Colors</h3>' + desc('A link has the same color as the text around it. In Primary text the link is Primary, in Secondary text Secondary, in Tertiary text Tertiary. The surrounding text has the same color as the link in the examples.') + fig_one('<div class="pg-col" id="v-colors"></div>') + \
    '<h3 class="ds-h3 ds-group">Inverted</h3>' + desc('On a dark surface. Use it where the Primary link would not have enough contrast.') + fig_one('<div class="pg-col" id="v-inv"></div>', stage_cls='ds-stage--dark') + \
    '<h3 class="ds-h3 ds-group">Weight</h3>' + desc('<strong>Regular</strong> is the default. <strong>Medium</strong> (500) and <strong>Bold</strong> (600) follow the weight of the text around the link: a link in a bold text is Bold. They are not a way to emphasize a link. Any size can have any weight.') + fig_one('<div class="pg-col" id="v-weights"></div>') + \
    '<h3 class="ds-h3 ds-group">Italic</h3>' + desc('Add <code>inline-link--italic</code> when the text around the link is italic. The font has an italic face for every weight.') + fig_one('<div class="pg-col" id="v-italic"></div>') + \
    '<h3 class="ds-h3 ds-group">Reverse underline</h3>' + desc('<code>inline-link--reverse</code> (Figma “Reverse”) has no underline when enabled and shows it on hover, like an Action link. Use it where the surrounding text already makes it clear that the words are a link; color alone is not enough (WCAG 1.4.1).') + fig_one('<div class="pg-col" id="v-reverse"></div>')

sizes = '<h2 class="ds-h2">Sizes</h2>' + desc('An inline link matches the context it is in: XLarge, Large, Medium or Small, aligned to <code>body-xl</code>, <code>body-lg</code>, <code>body-md</code> or <code>body-sm</code>. It must match the size, line height and letter spacing of its surrounding text, and follow the Desktop or Mobile base styles that text follows. <strong>Never make a link larger or bolder than its text for emphasis.</strong> If a link stands apart from other content, its size matches the default body copy size of the page. XLarge, Large and Medium change at 769px; Small is the same on every breakpoint. The values are under ' + sec_link(SLUG, 'sizes', 'Sizes') + ' in Specifications.') + \
    toolbar([('sz-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force')]) + fig_one('<div class="pg-col" id="v-sizes"></div>')

layout = '<h2 class="ds-h2">Layout &amp; Appearance</h2><h3 class="ds-h3 ds-group">Alignment</h3>' + desc('An inline link is part of the text flow: it wraps with the text and takes its line height from the size.') + \
    '<h3 class="ds-h3 ds-group">Placement</h3>' + desc('Only inside running text: body copy, a list or UI text. A link on its own line is an Action link.') + \
    '<h3 class="ds-h3 ds-group">Width</h3>' + desc('As wide as its text (<code>display: inline</code>).') + \
    '<h3 class="ds-h3 ds-group">Appearance</h3>' + desc('Underlined when enabled. On hover the underline goes and the color changes. This is the reverse of the Action link, unless the reverse underline is used (underline on hover only). Token names and values are under ' + sec_link(SLUG, 'design-tokens', 'Design Tokens') + ' in Specifications.')

behavior = '<h2 class="ds-h2">Behavior</h2><h3 class="ds-h3 ds-group">Hover</h3>' + desc('The underline is removed and the color changes to the hover color of the variant. The color changes over <code>duration-fast-3</code> with <code>ease-standard</code>; the underline is not transitioned.') + \
    '<h3 class="ds-h3 ds-group">Click and Enter</h3>' + desc('A click or Enter follows the link. All states are listed under ' + sec_link(SLUG, 'states', 'States') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Focus</h3>' + desc('A 2px ring shows on keyboard focus only (<code>body.keyboard-nav</code>), the same as on the Action link and the Tile link.')

access = '<h2 class="ds-h2">Accessibility</h2>' + desc('All requirements are listed under ' + sec_link(SLUG, 'accessibility-requirements', 'Accessibility Requirements') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Keyboard support</h3>' + desc('Tab moves between links. Enter follows the focused link.') + \
    '<h3 class="ds-h3 ds-group">Screen reader support</h3>' + desc('A real <code>&lt;a href&gt;</code> is announced as a link, with its text. Write link text that makes sense out of context. Links navigate; buttons act.')

related = '<h2 class="ds-h2">Related</h2><ul class="ds-bullets"><li><strong>' + link_large('links-guide.html', 'Links guide') + '</strong>. How to choose a link type.</li><li><strong>' + link_large('action-link.html', 'Action link') + '</strong>. A standalone link with an icon.</li><li><strong>' + link_large('tile-link.html', 'Tile link') + '</strong>. A graphical, prominent link.</li><li><strong>' + link_large('button.html', 'Button') + '</strong>. For an action that does not navigate.</li></ul>'

references = '<h2 class="ds-h2">References</h2>' + refs([
    ('https://www.w3.org/WAI/WCAG22/Understanding/use-of-color.html', 'WCAG 2.2: Use of Color', 'Success criterion 1.4.1: the underline is why a link is visible without color.'),
    ('https://www.w3.org/WAI/WCAG22/Understanding/link-purpose-in-context.html', 'WCAG 2.2: Link Purpose (In Context)', 'Success criterion 2.4.4.'),
    ('https://www.nngroup.com/articles/guidelines-for-visualizing-links/', 'Nielsen Norman Group: Guidelines for Visualizing Links', 'Why links are underlined.'),
    ('https://fluent2.microsoft.design/components/web/react/core/link/usage', 'Fluent 2: Link', 'Microsoft.'),
    ('https://carbondesignsystem.com/components/link/usage/', 'Carbon Design System: Link', 'IBM.')])

ex = [('playground', playground), ('overview', overview), ('usage', usage), ('anatomy', anatomy), ('variants', variants), ('sizes', sizes), ('layout', layout), ('behavior', behavior), ('accessibility', access), ('related', related), ('references', references)]

# ---------------------------------------------------------------- Specifications
st_tok = '<h2 class="ds-h2">Design Tokens</h2>' + desc('Resolved from the live token package.') + \
    '<div class="ds-table-wrap"><table class="ds-table" id="tok-table"><thead><tr><th scope="col">Color</th><th scope="col">Part</th><th scope="col">Token</th><th scope="col">Value</th></tr></thead><tbody></tbody></table></div>' + \
    note('A link has the same color as the text around it, so the enabled colors are the text colors (Secondary and Tertiary are the same values as <code>text-action-secondary</code> and <code>text-action-tertiary</code>). The hover colors are the three action hover tokens: <code>text-action-primary-hover</code>, <code>text-action-secondary-hover</code> and <code>text-action-tertiary-hover</code>.')

st_sizes = '<h2 class="ds-h2">Sizes</h2>' + table(['Size', 'Type token', 'Desktop (769px+)', 'Mobile and tablet', 'Weight'], [
    ['XLarge', '<code>body-xl</code>', '24/32, 0', '20/26, 0', '400'], ['Large', '<code>body-lg</code>', '20/28, 0.18px', '18/24, 0.18px', '400'], ['Medium', '<code>body-md</code>', '17/24, 0.32px', '16/22, 0.32px', '400'],
    ['Small', '<code>body-sm</code>', '14/20, 0.36px', '14/20, 0.36px', '400']]) + \
    note('<code>sm</code> (640 to 768px) looks like mobile. The weight is a modifier, see Typography. The old <code>inline-link--small-bold</code> is kept: it is Small with the Bold weight.')

st_meas = '<h2 class="ds-h2">Measurements</h2><h3 class="ds-h3 ds-group">Dimensions</h3>' + table(['Attribute', 'Value'], [['Height', 'The line height of the text: 32, 28, 24 or 20px (desktop)'], ['Padding and margin', 'None'], ['Underline', 'The browser’s default 1px underline'], ['Icon', 'Never']]) + \
    note('An inline link has no padding or margin of its own, so there is no measurement figure. It takes its box from the text around it.')

st_states = '<h2 class="ds-h2">States</h2>' + desc('The reverse of the action link: underlined when enabled, the underline is <strong>removed</strong> on hover and the color changes. Hover is forced on this page; in your code it comes from <code>:hover</code>.') + \
    toolbar([('sb-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force')]) + \
    '<div class="ds-table-wrap"><table class="ds-table pg-matrix" id="matrix"><thead><tr><th scope="col">State</th><th scope="col">Primary</th><th scope="col">Secondary</th><th scope="col">Tertiary</th><th scope="col">Inverted</th></tr></thead><tbody></tbody></table></div>' + \
    note('<strong>Enabled</strong> is underlined text (Default) or text with no underline (Reverse). <strong>Hover</strong> is a reduced-contrast text: the color shifts and the underline goes (Default), or the underline appears (Reverse). <strong>There is no Disabled state:</strong> remove the link or show plain text.') + \
    note('The last two rows are the reverse underline (Figma “Reverse=yes”): no underline when enabled, underline on hover.')

st_typo = '<h2 class="ds-h2">Typography</h2><h3 class="ds-h3 ds-group">Features</h3>' + table(['Size', 'font-feature-settings'], [['XLarge, Large', '<code>ss02</code>, <code>ss03</code>'], ['Medium, Small', '<code>ss02</code>, <code>ss03</code>, <code>ss06</code>']]) + \
    '<h3 class="ds-h3 ds-group">Weight and style</h3>' + table(['Modifier', 'Class', 'CSS'], [['Regular', '(none)', '<code>font-weight: 400</code>'], ['Medium', '<code>inline-link--weight-medium</code>', '<code>font-weight: 500</code>'], ['Bold', '<code>inline-link--bold</code>', '<code>font-weight: 600</code>'], ['Italic', '<code>inline-link--italic</code>', '<code>font-style: italic</code>']]) + \
    note('Figma weights are 100 higher than the CSS (confirmed by design, see <code>eco-typography</code>). The font package ships 300, 400, 500 and 700, each with an italic face, so 600 renders with the 700 face. A weight or italic only makes a link follow the text around it, never emphasize it.') + \
    note('Breuer Condensed. The type token, size and line height of each size are under Sizes.')

st_struct = '<h2 class="ds-h2">Structure</h2><h3 class="ds-h3 ds-group">Elements</h3>' + table(['Element', 'Class', 'Notes'], [['Link', '<code>inline-link</code>', 'A real <code>&lt;a href&gt;</code>. <code>display: inline</code>, underlined.'], ['Size', '<code>inline-link--xlarge</code>, <code>--large</code>, <code>--medium</code>, <code>--small</code>', 'Follows the text around the link.'], ['Color', '<code>inline-link--secondary</code>, <code>--tertiary</code>, <code>--inverted</code>', 'Primary is the default (no class).'], ['Weight, style, underline', '<code>inline-link--weight-medium</code>, <code>--bold</code>, <code>--italic</code>, <code>--reverse</code>', 'Modifiers on any size and color. Regular, normal and underlined when enabled are the defaults.']]) + \
    '<h3 class="ds-h3 ds-group">Types</h3>' + desc('There is one type. A link with an icon is an ' + link_large('action-link.html', 'Action link') + '.') + \
    '<h3 class="ds-h3 ds-group">Width</h3>' + desc('As wide as its text. It wraps with the text.')

st_motion = '<h2 class="ds-h2">Motion</h2>' + table(['Property', 'Duration', 'Easing'], [['<code>color</code>', '<code>duration-fast-3</code>', '<code>ease-standard</code>']]) + note('<code>text-decoration</code> is not transitioned.')

st_behavior = '<h2 class="ds-h2">Behavior</h2>' + table(['Input', 'Result'], [
    ['Click, Enter', 'Follows the link. A link always navigates: an action in the page is a button.'], ['Tab', 'Moves to the link. A 2px ring shows on keyboard focus only (<code>body.keyboard-nav</code>).'], ['Underline', 'On when enabled, removed on hover. Never transitioned. With the reverse underline: off when enabled, on on hover.'], ['Hover', 'Reduced contrast: a color shift and the underline removal.'], ['Disabled', 'None. Remove the link or show plain text.'], ['Icons', 'Never. A link with an icon is an Action link.'], ['Markup', '<code>display: inline</code>, a real <code>&lt;a href&gt;</code> inside the text.']])

st_access = '<h2 class="ds-h2">Accessibility Requirements</h2>' + table(['Topic', 'Requirement'], [
    ['Element', 'A real <code>&lt;a href&gt;</code> only. Links navigate; anything else is a <code>&lt;button&gt;</code>. Never <code>href="#"</code> with a JavaScript handler (the documentation examples use it only to keep the page from jumping).'], ['Accessible name', 'The visible text. When more context is needed, extend it with an <code>aria-label</code> that begins with the visible text (WCAG 2.5.3 Label in Name), for example the visible “Delivery terms” with <code>aria-label="Delivery terms (PDF)"</code>.'], ['New tab or file', 'A link that opens a new tab or a file says so in its accessible name (“opens in a new tab”), and has <code>rel="noopener"</code>.'], ['Target size', 'Inline links in a text block are exempt from the 24px minimum (WCAG 2.5.8 inline exception). A standalone list of links (a footer list) needs an effective height of at least 24px, from the line height or padding.'], ['Name', 'The link text names the destination and makes sense out of context (WCAG 2.4.4). Never “click here”.'], ['Color', 'The underline separates the link from the text, so color is not the only signal (WCAG 1.4.1).'],
    ['Contrast', 'Text needs at least 4.5:1 against its background in every state, hover included (WCAG 1.4.3). The link color against the surrounding text needs at least 3:1 or a non-color indicator: the underline is that indicator, another reason to keep it. Use Inverted on dark surfaces. <strong>Open point:</strong> measured on white, Tertiary hover (<code>#939595</code>) is 3.0:1 and fails; Primary hover, Secondary hover and Tertiary (<code>#737373</code>) are 4.7:1 on white but 4.4:1 on <code>#f6f6f6</code>. Confirm with design.'], ['Disabled', 'Never disable a link: a disabled <code>&lt;a&gt;</code> has no standard semantics. Remove it or render plain text.'], ['Style', 'The size, line height, letter spacing, weight and italic match the surrounding text. A link is never larger or bolder than its text for emphasis.'], ['Focus', 'A 2px ring with <code>border-focus</code> and 2px offset, on keyboard focus (WCAG 2.4.7, 1.4.11).']])

spec = [('design-tokens', st_tok), ('sizes', st_sizes), ('measurements', st_meas), ('states', st_states), ('typography', st_typo), ('structure', st_struct), ('motion', st_motion), ('behavior', st_behavior), ('accessibility-requirements', st_access)]

# ---------------------------------------------------------------- Code
c_basic = '<h2 class="ds-h2">Basic Usage</h2>' + desc('Link the shared stylesheet once per page. Never copy the rules into a page.') + table(['Step', 'What to do'], [
    ['1. Link', '<code>&lt;link rel="stylesheet" href="/components/css/inline-link.css"&gt;</code>. Both templates already have it.'], ['2. Markup', 'A real <code>&lt;a href&gt;</code> with <code>class="inline-link inline-link--medium"</code> inside the text.'],
    ['3. Size', 'Choose the size that matches the text around the link.'], ['4. Color', 'The same color as the text around the link: Primary (no class) in Primary text, <code>inline-link--secondary</code> in Secondary text, <code>--tertiary</code> in Tertiary text, <code>--inverted</code> on a dark surface.'], ['5. Icons', 'None. For an icon use an Action link.']])
c_il = '<h2 class="ds-h2">Inline link</h2>' + desc('Copy the markup you need. Hover comes from <code>:hover</code>; the <code>[data-state]</code> selectors in the CSS exist only so the documentation can force a state.') + '<div id="recipes"></div>'
c_api = '<h2 class="ds-h2">API</h2><h3 class="ds-h3 ds-group">Classes</h3>' + table(['Class', 'Use'], [['<code>inline-link</code>', 'The link. Primary color, underlined.'], ['<code>inline-link--xlarge</code>, <code>--large</code>, <code>--medium</code>, <code>--small</code>', 'Size.'], ['<code>inline-link--weight-medium</code>, <code>--bold</code>', 'Weight (any size). <code>--small-bold</code> is kept: Small and Bold.'], ['<code>inline-link--italic</code>', 'Italic style.'],  ['<code>inline-link--reverse</code>', 'No underline when enabled, underline on hover.'], ['<code>inline-link--secondary</code>, <code>--tertiary</code>', 'Colors for grey text.'], ['<code>inline-link--inverted</code>', 'For a dark surface.']]) + \
    '<h3 class="ds-h3 ds-group">Things to know</h3>' + bullets(['Breakpoint: XLarge, Large and Medium change at 769px. The CSS does this by itself.', 'The color is the color of the text around the link: Primary (<code>text-primary</code>), <code>--secondary</code> in <code>text-secondary</code> text, <code>--tertiary</code> in <code>text-tertiary</code> text. The hover colors are <code>text-action-primary-hover</code>, <code>text-action-secondary-hover</code> and <code>text-action-tertiary-hover</code>.', 'Never add an icon: use an Action link.', 'The focus ring needs <code>body.keyboard-nav</code>, which the templates set on the first Tab press.', 'The <code>[data-state]</code> selectors do nothing outside the documentation pages.'])
c_css = '<h2 class="ds-h2">CSS / Tailwind</h2>' + desc('The component is one CSS file, shared by every page. Link it, never copy it. The CSS below is read from the file the page links, so it is always what you see.') + code_box('css-code', 'CSS (components/css/inline-link.css)')
code = [('basic-usage', c_basic), ('inline-link', c_il), ('api', c_api), ('css-tailwind', c_css, False)]

# ---------------------------------------------------------------- scripts
IL_JS = r'''
  var CLS = { primary: '', secondary: ' inline-link--secondary', tertiary: ' inline-link--tertiary', inverted: ' inline-link--inverted' };
  $$('[data-prevent]').forEach(function (a) { a.addEventListener('click', function (e) { e.preventDefault(); }); });
  var WT = { regular: '', medium: ' inline-link--weight-medium', bold: ' inline-link--bold' };
  function cls(o) { return 'inline-link inline-link--' + o.size + CLS[o.color] + (WT[o.weight || 'regular']) + (o.italic ? ' inline-link--italic' : '') + (o.reverse === 'yes' ? ' inline-link--reverse' : ''); }
  function link(o) { var a = document.createElement('a'); a.href = '#'; a.className = cls(o); a.textContent = o.label; if (o.state === 'hover') a.dataset.state = 'hover'; a.addEventListener('click', function (e) { e.preventDefault(); }); return a; }
  /* The text around a link has the same type as the link: size, line height, letter spacing and features are copied from the link (also under a forced breakpoint) */
  function syncText(root) {
    $$('.pg-p', root || document).forEach(function (p) {
      if (p.hasAttribute('data-nosync')) return;
      var a = p.querySelector('a.inline-link'); if (!a) return; var c = getComputedStyle(a);
      ['fontSize', 'lineHeight', 'letterSpacing', 'fontFeatureSettings'].forEach(function (k) { p.style[k] = c[k]; });
    });
  }
  window.addEventListener('resize', function () { syncText(); });
  function sentence(o) {
    var p = document.createElement('p'); p.className = 'pg-p';
    var PC = { secondary: 'var(--color-text-secondary)', tertiary: 'var(--color-text-tertiary)' }; if (PC[o.color]) p.style.color = PC[o.color];   /* the text has the color of the link */
    if (o.weight === 'medium') p.style.fontWeight = '500'; else if (o.weight === 'bold') p.style.fontWeight = '600'; if (o.italic) p.style.fontStyle = 'italic';   /* the text has the style of the link */
    p.appendChild(document.createTextNode('Read more about our products on the ')); p.appendChild(link(o)); p.appendChild(document.createTextNode('.')); return p;
  }
'''

JS_EX = IL_JS + r'''
  var st = { size: 'medium', color: 'primary', state: 'enabled', weight: 'regular', italic: 'no', reverse: 'no' };
  function renderPg() {
    var o = { size: st.size, color: st.color, state: st.state, weight: st.weight, italic: st.italic === 'yes', reverse: st.reverse, label: $('#pg-label').value };
    $('#pg-stage').classList.toggle('ds-stage--dark', o.color === 'inverted');
    clear($('#pg-host')).appendChild(sentence(o));
    var h = '<p>Read more about our products on the\n  <a href="#" class="' + cls(o) + '">' + esc(o.label) + '</a>.\n</p>';
    if (o.state === 'hover') h = '<!-- hover is forced here for preview; in production it comes from :hover -->\n' + h;
    $('#pg-code').textContent = h;
    syncText($('#pg-host'));
  }
  DK.wire(st, renderPg); $('#pg-label').addEventListener('input', renderPg);
  DK.bp(function () { syncText(); });

  var sz = clear($('#v-sizes')); [['xlarge', 'XLarge'], ['large', 'Large'], ['medium', 'Medium'], ['small', 'Small']].forEach(function (z) { sz.appendChild(sentence({ size: z[0], color: 'primary', label: z[1] + ' link' })); });
  var wt = clear($('#v-weights')); [['regular', 'Regular'], ['medium', 'Medium'], ['bold', 'Bold']].forEach(function (z) { wt.appendChild(sentence({ size: 'medium', color: 'primary', weight: z[0], label: z[1] + ' link' })); });
  var it = clear($('#v-italic')); it.appendChild(sentence({ size: 'medium', color: 'primary', italic: true, label: 'Italic link' })); it.appendChild(sentence({ size: 'medium', color: 'primary', italic: true, weight: 'bold', label: 'Bold italic link' })); $$('.pg-p', it).forEach(function (p) { p.style.fontStyle = 'italic'; });
  var rv = clear($('#v-reverse')); rv.appendChild(sentence({ size: 'medium', color: 'primary', reverse: 'yes', label: 'Reverse link' })); rv.appendChild(sentence({ size: 'medium', color: 'primary', reverse: 'yes', state: 'hover', label: 'Reverse link, hover' }));
  var co = clear($('#v-colors')); [['primary', 'Primary'], ['secondary', 'Secondary'], ['tertiary', 'Tertiary']].forEach(function (z) { co.appendChild(sentence({ size: 'medium', color: z[0], label: z[1] + ' link' })); });
  clear($('#v-inv')).appendChild(sentence({ size: 'medium', color: 'inverted', label: 'Inverted link' }));
  $('#v-inv .pg-p').style.color = 'var(--color-text-primary-inverted)';

  /* Usage figures */
  function say(host, parts) { var p = clear($(host)); parts.forEach(function (x) { p.appendChild(typeof x === 'string' ? document.createTextNode(x) : link({ size: 'medium', color: 'primary', label: x[0] })); }); }
  say('#fig-in-do', ['Read more about our work wear on the ', ['product page'], '.']);
  var d = clear($('#fig-in-dont')); d.appendChild(link({ size: 'medium', color: 'primary', label: 'View all products' }));

  var sz1 = clear($('#fig-sz-do')); sz1.appendChild(document.createTextNode('Read more about our work wear on the ')); sz1.appendChild(link({ size: 'medium', color: 'primary', label: 'product page' })); sz1.appendChild(document.createTextNode('.'));
  var sz2 = clear($('#fig-sz-dont')); sz2.setAttribute('data-nosync', ''); sz2.appendChild(document.createTextNode('Read more about our work wear on the ')); sz2.appendChild(link({ size: 'xlarge', color: 'primary', weight: 'bold', label: 'product page' })); sz2.appendChild(document.createTextNode('.'));


  /* Anatomy */
  var ap = $('#il-anat-p');
  ap.appendChild(document.createTextNode('Read more about our products on the ')); var al = link({ size: 'large', color: 'primary', label: 'product page' }); ap.appendChild(al); ap.appendChild(document.createTextNode('.'));
  DK.callouts($('#il-anat'), [
    { n: 1, el: al, side: 'top', len: 48, at: 'edge' },
    { n: 2, side: 'bottom', len: 48, at: 'edge', box: function () { var r = al.getBoundingClientRect(); return { left: r.left, top: r.bottom - 4, width: r.width, height: 1 }; } }
  ]);
  /* matching Do and Don't boxes of the writing examples have the same height (two columns only) */
  function eqBoxes() {
    $$('.pg-exfigs').forEach(function (g) {
      var st = $$('.ds-fig__stage', g); st.forEach(function (x) { x.style.minHeight = '0'; });
      if (st.length < 2 || st[0].getBoundingClientRect().top !== st[1].getBoundingClientRect().top) return;
      var h = Math.max.apply(null, st.map(function (x) { return x.getBoundingClientRect().height; }));
      st.forEach(function (x) { x.style.minHeight = h + 'px'; });
    });
  }
  window.addEventListener('resize', eqBoxes); eqBoxes();
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(eqBoxes);
  renderPg();
  syncText();
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { syncText(); });
'''

JS_SPEC = IL_JS + r'''
  var tb = $('#matrix tbody');
  function buildMatrix() {
    clear(tb);
    [['Enabled', 'enabled', 'no'], ['Hover', 'hover', 'no'], ['Reverse · enabled', 'enabled', 'yes'], ['Reverse · hover', 'hover', 'yes']].forEach(function (r) {
      var tr = document.createElement('tr'), th = document.createElement('th'); th.scope = 'row'; th.textContent = r[0]; tr.appendChild(th);
      ['primary', 'secondary', 'tertiary', 'inverted'].forEach(function (c) { var td = document.createElement('td'); if (c === 'inverted') td.className = 'pg-dark'; td.appendChild(sentence({ size: 'medium', color: c, state: r[1], reverse: r[2], label: 'link' })); tr.appendChild(td); });
      tb.appendChild(tr);
    });
  }
  buildMatrix(); syncText(); DK.bp(function () { syncText(); });
  DK.tokenTable($('#tok-table tbody'), [
    ['Primary', 'Enabled', 'text-action-primary'], ['Primary', 'Hover', 'text-action-primary-hover'],
    ['Secondary', 'Enabled', 'text-secondary'], ['Secondary', 'Hover', 'text-action-secondary-hover'],
    ['Tertiary', 'Enabled', 'text-tertiary'], ['Tertiary', 'Hover', 'text-action-tertiary-hover'],
    ['Inverted', 'Enabled', 'text-primary-inverted'], ['Inverted', 'Hover', 'text-action-primary-inverted-hover']]);
'''

JS_CODE = r'''
  DK.recipes($('#recipes'), [
    ['In body text (Primary, Medium)', '<p>Read more about our products on the\n  <a href="/products" class="inline-link inline-link--medium">product page</a>.\n</p>'],
    ['Secondary and Tertiary', '<p>See <a href="/terms" class="inline-link inline-link--medium inline-link--secondary">full terms</a> for details.</p>'],
    ['Weight: Medium and Bold', '<a href="/news" class="inline-link inline-link--small inline-link--weight-medium">Read more</a>\n<a href="/news" class="inline-link inline-link--small inline-link--bold">Read more</a>'],
    ['Italic', '<p><em>See <a href="/terms" class="inline-link inline-link--medium inline-link--italic">full terms</a>.</em></p>'],
    ['Reverse underline', '<a href="/news" class="inline-link inline-link--medium inline-link--reverse">Read more</a>'],
    ['Inverted, on a dark surface', '<p style="color: var(--color-text-primary-inverted)">Contact us at\n  <a href="mailto:info@example.com" class="inline-link inline-link--medium inline-link--inverted">info@example.com</a>.\n</p>']
  ]);
  DK.printCss($('#css-code'), 'inline-link', [[/:is\(:hover, \[data-state="hover"\]\)/g, ':hover'], [/^ {4}/gm, '']]);
'''

C = dict(
    slug=SLUG, title='Inline link', parent=PARENT, eyebrow='Components · Links',
    lead='An inline link is an underlined text link that flows <strong>within body copy, lists and UI text</strong>. The underline is its affordance, and it is never paired with icons.',
    lead_ex='Every example on this page is the real component, not a picture. Specification: <code>.claude/skills/eco-inline-link/SKILL.md</code>. Figma: ' + fig_link(FIGMA, 'Inline link') + '.',
    lead_spec='Tokens, sizes, states and requirements. Values come from the live token package and from Figma: ' + fig_link(FIGMA, 'Inline link') + '.',
    lead_code='How to add an inline link to a page. The file is <code>components/css/inline-link.css</code>.',
    select_menu=True,
    css=['inline-link'], style=STYLE, ex=ex, spec=spec, code=code, js_ex=JS_EX, js_spec=JS_SPEC, js_code=JS_CODE)

if __name__ == '__main__':
    emit(C)
