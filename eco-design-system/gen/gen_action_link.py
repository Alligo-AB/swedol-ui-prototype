from build import *

FIGMA = 'https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=1671-52811'
SLUG = 'action-link'
PARENT = ('links-guide.html', 'Links guide')

STYLE = r'''    .pg-note { font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-tertiary); }
    .pg-col { display: flex; flex-direction: column; align-items: flex-start; gap: 16px; width: 100%; }
    .pg-row { display: flex; flex-wrap: wrap; align-items: center; gap: 16px 32px; }
    .pg-line { display: flex; flex-wrap: wrap; align-items: center; gap: 8px 16px; width: 100%; }   /* links on one row, a divider between them */
    .pg-p { margin: 0; color: var(--color-text-primary); max-width: 560px; }
    .pg-matrix td { vertical-align: middle; padding-top: 16px; padding-bottom: 16px; }
    .pg-dark { background: var(--color-surface-100); }
    .pg-exs { width: 100%; }   /* the lines of one Do or Don't box, one example per line */
    .pg-ex { font-size: 16px; line-height: 22px; letter-spacing: 0.32px; font-weight: 400; color: var(--color-text-primary); font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1; }   /* body-md (16/22, 17/24 from 769px) */
    @media (min-width: 769px) { .pg-ex { font-size: 17px; line-height: 24px; } }
    .pg-ex + .pg-ex { margin-top: 12px; }
    #usage .ds-fig__stage { align-items: flex-start; }   /* every Do / Don't box of this page: content at the top */
    .pg-exfigs .ds-fig__stage { min-height: 0; padding: 16px 24px; justify-content: flex-start; align-items: flex-start; }   /* low boxes; JS makes a Do and a Don't box the same height */
    .ds-callout__art { padding-right: 24px; }'''

import re

def AX(t, lead=None):
    """A real action link (Medium, trailing chevron, optional leading icon) that goes nowhere: a writing example."""
    li = ('<span class="action-link__icon" aria-hidden="true">%s</span>' % lead) if lead else ''
    return '<a href="#" class="action-link action-link--medium" data-prevent>%s<span class="action-link__label">%s</span><span class="action-link__icon" aria-hidden="true">chevron_right</span></a>' % (li, t)


EXSEP = '</div><div class="pg-ex">'   # one example per line inside a box

CAPS = iter([
    ('Do use a verb-first action phrase or a destination noun.', 'Do not use a vague label.'),
    ('Do state the object of the action.', 'Do not use a bare verb when several links sit together.'),
    ('Do put the file type and size in the label.', 'Do not leave the type and size to a tooltip.'),
    ('Do keep the labels of a stack parallel.', 'Do not mix structures in one stack.'),
    ('Do use sentence case, with no trailing punctuation.', 'Do not capitalize every word or end with a full stop.')])


def ex_groups(rows):
    do_cap, dont_cap = next(CAPS)
    dos = EXSEP.join(r[0] for r in rows if r[0]); donts = EXSEP.join(r[1] for r in rows if r[1])
    box = lambda x: '<div class="pg-exs"><div class="pg-ex">%s</div></div>' % x
    return fig_pair(box(dos), do_cap, box(donts), dont_cap).replace('class="ds-figs"', 'class="ds-figs pg-exfigs"', 1)


playground = '<h2 class="ds-h2">Playground</h2>' + desc('Choose a size, weight, variant and state and the link and its code update. The link always has an icon: leading, trailing or both. Hover is forced here; the link itself is live.') + \
    '<div class="ds-playground"><div class="ds-stage ds-stage--center" id="pg-stage"><div id="pg-host"></div></div><div class="ds-controls">' + \
    bp_field('pg-l-bp') + btn_group('pg-l-size', 'Size', 'data-pg="size"', [('large', 'Large', False), ('medium', 'Medium', True), ('small', 'Small', False)]) + \
    btn_group('pg-l-w', 'Weight', 'data-pg="weight"', [('regular', 'Regular', True), ('medium', 'Medium', False), ('bold', 'Bold', False)]) + \
    btn_group('pg-l-v', 'Variant', 'data-pg="variant"', [('primary', 'Primary', True), ('inverted', 'Inverted', False)]) + \
    btn_group('pg-l-st', 'State', 'data-pg="state"', [('enabled', 'Enabled', True), ('hover', 'Hover', False), ('focus', 'Focus', False)]) + \
    btn_group('pg-l-i', 'Icons', 'data-pg="icons"', [('trailing', 'Trailing', False), ('leading', 'Leading', False), ('both', 'Both', True)]) + \
    '<div class="ds-field form-field"><label class="form-label form-label--sm" for="pg-label">Label</label><div class="input-wrap"><div class="input-box input-box--sm"><input class="form-input" type="text" id="pg-label" value="View all products" placeholder="Label" /></div></div></div>' + \
    '</div></div><h3 class="ds-h3">Markup for this selection</h3>' + code_box('pg-code', 'HTML')

overview = '<h2 class="ds-h2">Overview</h2>' + desc('An action link is a <strong>self-contained text link paired with icons</strong> that clarify what happens when it is activated: a leading icon, a trailing icon or both (a download icon, a chevron). It gives link-weight interactions, lighter than a button, a clear and scannable anchor outside body copy: under product descriptions, in specification sections and in lists of resources. It is used for lightweight actions like downloads and “view all” navigation, forward or backward.') + \
    desc('One line: a standalone, iconized text link for lightweight actions and forward or backward navigation, placed outside running text.') + \
    desc('Action link has three sizes (Large, Medium and Small), a regular and a bold weight, and two variants (Primary and Inverted). It is always paired with an icon, leading, trailing or both, in the same color as the link text. It is one of three link types: see the ' + link_large('links-guide.html', 'Links guide') + ' for how to choose.') + \
    three_pages(SLUG, 'an action link', 'the values: tokens, sizes, states and requirements', 'how to add one to a page')

usage = '<h2 class="ds-h2">Usage</h2><h3 class="ds-h3 ds-group">When to use</h3>' + desc('Use an action link for a link that stands on its own line, outside running text, when it needs more visual anchoring than an Inline link but less weight than a Button. Use it to:') + \
    bullets(['Link to downloadable resources: datasheets, manuals, certificates (“Download product sheet”)', 'Offer a “see more” or “view all” step at the end of a content section or a product list', 'List several parallel resources or destinations as stacked rows', 'Emphasize a contact action outside body copy: an email or phone link with a matching leading icon (<code>mailto:</code>, <code>tel:</code>)', 'Go on to a related page at the end of a section']) + \
    '<h3 class="ds-h3 ds-group">When not to use</h3><h3 class="ds-h3">Keep it out of running text</h3>' + desc('Inside a sentence the link is an ' + link_large('inline-link.html', 'Inline link') + '. An action link has an icon, has no underline until hover and sits outside the text: it is never embedded in prose.') + \
    fig_pair('<div class="pg-col" id="fig-ph-do"></div>', 'Do put an action link on its own line.', '<p class="pg-p" id="fig-ph-dont"></p>', 'Do not put an action link inside a paragraph. Use an Inline link instead.') + \
    '<h3 class="ds-h3">Not for the primary call to action</h3>' + desc('The main action on the surface (add to cart, check out) is a <code>eco-button</code>. Do not put an action link and a Button side by side for the same action: pick one weight.') + \
    '<h3 class="ds-h3">Not for a grid of peers</h3>' + desc('Destinations that form a visual grid of equals are ' + link_large('tile-link.html', 'Tile links') + '.') + \
    '<h3 class="ds-h3">Not for opening or closing content in place</h3>' + desc('An action link navigates or downloads; it does not disclose. If the trailing chevron would open or close content in place, use a <code>eco-button</code> or the component that owns the pattern: a ' + link_large('collapsible.html', 'Collapsible') + ' for expanding in place and a ' + link_large('modal.html', 'Modal') + ' for an overlay. Do not use the chevron as a disclosure icon.') + \
    '<h3 class="ds-h3">Do not disable an action link</h3>' + desc('Avoid disabled links. Hide the row, or show plain non-interactive text instead (“Product sheet missing”). If a disabled state must ship, it needs <code>aria-disabled</code> handling, and it is exempt from the contrast minimum but must still be recognizable. The shared CSS has no disabled style.') + \
    '<h3 class="ds-h3 ds-group">Icons and stacks</h3><h3 class="ds-h3">Pick the leading icon for the outcome</h3>' + desc('Use a download icon for files and the trailing chevron alone for navigation. Do not use a decorative icon that promises nothing.') + \
    fig_pair('<div class="pg-col" id="fig-ic-do"></div>', 'Do pick an icon that matches the outcome.', '<div class="pg-col" id="fig-ic-dont"></div>', 'Do not use a decorative icon that promises nothing.') + \
    '<h3 class="ds-h3">Keep a stack consistent</h3>' + desc('Stacked action links sit in one column with the same size and the same spacing on the 8px grid. Do not mix sizes or emphasis levels in one stack.') + \
    fig_pair('<div class="pg-col" id="fig-stack-do"></div>', 'Do use one size and equal spacing in a stack.', '<div class="pg-col" id="fig-stack-dont"></div>', 'Do not mix sizes in one stack.') + \
    '<h3 class="ds-h3">Links on the same row</h3>' + desc('Action links can also sit side by side on one row (the Divided layout). Separate them with a vertical ' + link_large('divider.html', 'Divider') + ' (Tertiary), use one size and keep the same space on both sides of each divider. Without a divider the links run together and read as one phrase.') + \
    fig_pair('<div class="action-link-group action-link-group--divided" id="fig-row-do"></div>', 'Do separate links on one row with a vertical divider.', '<div class="pg-line" id="fig-row-dont"></div>', 'Do not put links on one row with no divider between them.') + \
    '<h3 class="ds-h3">Use the strong variant once per stack</h3>' + desc('The Bold variant is the way to emphasize one link. Reserve it for at most one link per stack, and never make a link larger to emphasize it.') + \
    fig_pair('<div class="pg-col" id="fig-wt-do"></div>', 'Do use Bold for at most one link in a stack.', '<div class="pg-col" id="fig-wt-dont"></div>', 'Do not make every link Bold.') + \
    '<h3 class="ds-h3 ds-group">Writing link labels</h3>' + desc('A label is a verb-first action phrase or a destination noun, two to five words, such as “Download product sheet” or “View all accessories”. The examples are real action links that go nowhere. They are in English; on a Swedish page follow the same rules in the Swedish copy.') + \
    '<h3 class="ds-h3">Say what happens, and name the object</h3>' + desc('The label tells users what they get. Use a bare verb (“Download”) only when one link stands alone; when several links sit together, name the object of each.') + \
    ex_groups([(AX('Download product sheet', 'file_download') + EXSEP + AX('View all accessories'), AX('Click here') + EXSEP + AX('More info')), ]) + \
    ex_groups([(AX('Download assembly instructions', 'file_download') + EXSEP + AX('Download product sheet', 'file_download') + EXSEP + AX('Download safety datasheet', 'file_download'), AX('Download', 'file_download') + EXSEP + AX('Download', 'file_download') + EXSEP + AX('Download', 'file_download'))]) + \
    '<h3 class="ds-h3">Put the file type and size in the label</h3>' + desc('For a download, include the file type and size where they are known. They belong in the label, not in a tooltip.') + \
    ex_groups([(AX('Download manual (PDF, 2 MB)', 'file_download'), AX('Download manual', 'file_download') + EXSEP + 'Type and size only in a tooltip')]) + \
    '<h3 class="ds-h3">Keep the labels of a stack parallel</h3>' + desc('All labels in a stack are verb-first, or all are nouns.') + \
    ex_groups([(AX('Download product sheet', 'file_download') + EXSEP + AX('Download manual', 'file_download') + EXSEP + AX('Download safety datasheet', 'file_download'), AX('Download product sheet', 'file_download') + EXSEP + AX('Manual', 'file_download') + EXSEP + AX('Safety information', 'file_download'))]) + \
    '<h3 class="ds-h3">Use sentence case, with no trailing punctuation</h3>' + desc('Sentence case matches the copy around the link. No punctuation ends the label.') + \
    ex_groups([(AX('View all accessories'), AX('View All Accessories') + EXSEP + AX('View all accessories.'))]) + \
    '<h3 class="ds-h3">Plan for long labels</h3>' + desc('A label stays on one line when it can. Translated strings and compound words run long, so define what happens at small widths: truncate with an ellipsis, or allow a two-line wrap.') + \
    '<h3 class="ds-h3 ds-group">Quick reference</h3>' + \
    table(['The link…', 'Use'], [['stands alone, with an icon: “View all products”, “Download document”', 'Action link'], ['sits inside a sentence', '<a class="inline-link inline-link--small" href="inline-link.html">Inline link</a>'], ['is a card or a logo, presented graphically', '<a class="inline-link inline-link--small" href="tile-link.html">Tile link</a>'], ['runs an action in the page (save, send, open a modal)', '<code>eco-button</code>']]) + \
    rules(['Pick a leading icon that matches the outcome: a download icon for files, the chevron alone for navigation.', 'Let the label state the object (“Download assembly instructions”).', 'Keep stacked links in one column with the same size and equal spacing on the 8px grid.', 'Put links side by side on one row with a vertical divider between them, one size and equal space on both sides.', 'Use the strong (Bold) variant for at most one link per stack.', 'Use Primary on light surfaces and Inverted on dark ones. The icons have the same color as the link text.', 'Match the type size of the content the link follows, or the default body copy size of the page.', 'Use a real <code>&lt;a href&gt;</code>; for a download add the <code>download</code> attribute when the file is on the same origin.'],
          ['Put an action link inside a paragraph (use Inline link).', 'Use a decorative icon that promises nothing.', 'Use it as a button for an action that does not navigate, or as a disclosure chevron.', 'Use a bare verb (“Download”) when several links sit together.', 'Place an action link and a Button side by side for the same action.', 'Mix sizes or emphasis levels in one stack, or make every link Bold.', 'Put links on one row with no divider between them.', 'Make a link larger than the content it follows: use the strong variant for emphasis.', 'Underline the icon.'])

usage = usage.replace('class="ds-figs"', 'class="ds-figs pg-exfigs"')   # low, equal-height boxes, as on the Inline link page

anatomy = '<h2 class="ds-h2">Anatomy</h2><h3 class="ds-h3 ds-group">Action link</h3>' + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout" id="al-anat" role="img" aria-label="Anatomy of an action link: 1 leading icon, 2 link text, 3 trailing chevron"><div class="ds-callout__art" id="al-anat-art"></div></div></figure></div>' + \
    ol_parts([('Leading icon', 'Leading, trailing or both (at least one). A Material Symbol for the type of action, such as <code>file_download</code>. 24px (Large) or 20px.'), ('Link text', 'Regular or bold. It is the only part that gets the underline on hover.'), ('Trailing chevron', 'Leading, trailing or both (at least one): <code>chevron_right</code>, 24px (Large) or 20px. It shows forward movement.')]) + \
    desc('The gap between the parts is 8px (Large) or 4px (Medium and Small).')

variants = '<h2 class="ds-h2">Variants</h2>' + desc('Primary on a light surface and Inverted on a dark one, each in Regular and Bold. Sizes are under Sizes below.') + \
    '<h3 class="ds-h3 ds-group">Primary</h3>' + desc('<code>text-action-primary</code>, with <code>text-action-primary-hover</code> on hover.') + fig_one('<div class="pg-col" id="v-primary"></div>') + \
    '<h3 class="ds-h3 ds-group">Leading icon, trailing icon or both</h3>' + desc('A leading icon (for example <code>file_download</code>) says what the link does before the text is read. Use it for downloads and similar actions. The trailing chevron shows forward movement. The icons always have the same color as the link text.') + fig_one('<div class="pg-col" id="v-icon"></div>') + \
    '<h3 class="ds-h3 ds-group">Weight</h3>' + desc('<strong>Regular</strong> is the default. <strong>Medium</strong> (500) and <strong>Bold</strong> (600) are the other weights. Use one weight in a group, and Bold for at most one link per stack. An action link is never italic.') + fig_one('<div class="pg-col" id="v-weights"></div>') + \
    '<h3 class="ds-h3 ds-group">Inverted</h3>' + desc('For dark surfaces, in the inverted text colors.') + fig_one('<div class="pg-col" id="v-inv"></div>', stage_cls='ds-stage--dark')

sizes = '<h2 class="ds-h2">Sizes</h2>' + desc('<strong>Large</strong>, <strong>Medium</strong> and <strong>Small</strong>, each in Regular and Bold. Large and Medium change at 769px; Small is the same on every breakpoint. The link size matches the type size of the content it follows; a link that stands apart from other content matches the default body copy size of the page. Do not up-size a link for emphasis: use the strong (Bold) variant, at most once per stack. The values are under ' + sec_link(SLUG, 'sizes', 'Sizes') + ' in Specifications.') + \
    toolbar([('sz-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force')]) + fig_one('<div class="pg-col" id="v-sizes"></div>')

layout = '<h2 class="ds-h2">Layout &amp; Appearance</h2><h3 class="ds-h3 ds-group">Alignment</h3>' + desc('The link is an inline flex row: the icon, the text and the chevron are centered on one line. Several links stack in one column, or sit side by side on one row with a vertical Divider between them.') + \
    '<h3 class="ds-h3 ds-group">Placement</h3>' + desc('On its own line, outside body text: below a list, at the end of a section or in a footer. Not inside a sentence.') + \
    '<h3 class="ds-h3 ds-group">Width</h3>' + desc('As wide as its content (<code>display: inline-flex</code>).') + \
    '<h3 class="ds-h3 ds-group">Appearance</h3>' + desc('No underline when enabled. On hover the text gets the underline and the color changes; the icons are never underlined. This is the reverse of the Inline link. Token names and values are under ' + sec_link(SLUG, 'design-tokens', 'Design Tokens') + ' in Specifications.')

behavior = '<h2 class="ds-h2">Behavior</h2><h3 class="ds-h3 ds-group">Hover</h3>' + desc('The text is underlined and the color changes for the whole link, icons included. The color changes over <code>duration-fast-3</code> with <code>ease-standard</code>.') + \
    '<h3 class="ds-h3 ds-group">Focus</h3>' + desc('A 2px ring in <code>border-focus</code>, 2px from the link, shows on keyboard focus only (<code>body.keyboard-nav</code>). Shown forced below; press Tab on this page to see it live.') + fig_one('<div class="pg-col" id="v-focus"></div>') + fig_one('<div class="pg-col" id="v-focus-inv"></div>', stage_cls='ds-stage--dark') + \
    '<h3 class="ds-h3 ds-group">Click and Enter</h3>' + desc('A click on the text or an icon, or Enter, follows the link. The whole row is the target. All states are listed under ' + sec_link(SLUG, 'states', 'States') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Layout of a group: stacked or divided</h3>' + desc('A group of action links has two layouts, and the author chooses one on every breakpoint. <strong>Stacked</strong> puts the links in one column. <strong>Divided</strong> puts the links one after another on a row, with a vertical Divider between them, where there is room, and the row wraps onto the next line when it is full. A divided group does not turn into a column by itself on mobile: choose Stacked when the links need a column. The group classes draw the layout and the dividers.') + \
    '<h3 class="ds-h3">Stacked</h3>' + fig_one('<div class="action-link-group action-link-group--stacked" id="v-stacked"></div>') + \
    '<h3 class="ds-h3">Divided</h3>' + fig_one('<div class="action-link-group action-link-group--divided" id="v-divided"></div>') + \
    desc('The divider sits only between two links on the same line: when the row wraps, no divider is left at the start or the end of a line. Use the classes <code>action-link-group--stacked</code> and <code>action-link-group--divided</code>.')

access = '<h2 class="ds-h2">Accessibility</h2>' + desc('All requirements are listed under ' + sec_link(SLUG, 'accessibility-requirements', 'Accessibility Requirements') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Keyboard support</h3>' + desc('Tab moves between links. Enter follows the focused link. The focus ring shows on keyboard focus.') + \
    '<h3 class="ds-h3 ds-group">Screen reader support</h3>' + desc('A real <code>&lt;a href&gt;</code> is announced as a link, with its text. The icons are <code>aria-hidden</code>, so the link text must say where the link goes.')

related = '<h2 class="ds-h2">Related</h2><ul class="ds-bullets"><li><strong>' + link_large('links-guide.html', 'Links guide') + '</strong>. How to choose a link type.</li><li><strong>' + link_large('inline-link.html', 'Inline link') + '</strong>. A link inside a sentence.</li><li><strong>' + link_large('tile-link.html', 'Tile link') + '</strong>. A graphical, prominent link.</li><li><strong>' + link_large('button.html', 'Button') + '</strong>. For an action that does not navigate.</li></ul>'

references = '<h2 class="ds-h2">References</h2>' + refs([
    ('https://www.w3.org/WAI/WCAG22/Understanding/link-purpose-in-context.html', 'WCAG 2.2: Link Purpose (In Context)', 'Success criterion 2.4.4.'),
    ('https://www.w3.org/WAI/WCAG22/Understanding/focus-visible.html', 'WCAG 2.2: Focus Visible', 'Success criterion 2.4.7.'),
    ('https://www.nngroup.com/articles/guidelines-for-visualizing-links/', 'Nielsen Norman Group: Guidelines for Visualizing Links', 'How a link should look and behave.'),
    ('https://fluent2.microsoft.design/components/web/react/core/link/usage', 'Fluent 2: Link', 'Microsoft.'),
    ('https://carbondesignsystem.com/components/link/usage/', 'Carbon Design System: Link', 'IBM.')])

ex = [('playground', playground), ('overview', overview), ('usage', usage), ('anatomy', anatomy), ('variants', variants), ('sizes', sizes), ('layout', layout), ('behavior', behavior), ('accessibility', access), ('related', related), ('references', references)]

# ---------------------------------------------------------------- Specifications
st_tok = '<h2 class="ds-h2">Design Tokens</h2>' + desc('Resolved from the live token package.') + \
    '<div class="ds-table-wrap"><table class="ds-table" id="tok-table"><thead><tr><th scope="col">State</th><th scope="col">Part</th><th scope="col">Token</th><th scope="col">Value</th></tr></thead><tbody></tbody></table></div>'

st_sizes = '<h2 class="ds-h2">Sizes</h2>' + table(['Size', 'Type token', 'Desktop (769px+)', 'Mobile and tablet', 'Gap', 'Icon'], [
    ['Large', '<code>body-lg</code>', '20/28, 0.18px', '18/24, 0.18px', '8px', '24px'], ['Medium', '<code>body-md</code>', '17/24, 0.32px', '16/22, 0.32px', '4px', '20px'], ['Small', '<code>body-sm</code>', '14/20, 0.36px', '14/20, 0.36px', '4px', '20px']]) + \
    note('<code>sm</code> (640 to 768px) looks like mobile. Small is the same on every breakpoint. Weight is 400 (Regular) or 600 (Bold: Figma 700 minus 100 in this CSS).')

st_meas = '<h2 class="ds-h2">Measurements</h2><h3 class="ds-h3 ds-group">Dimensions</h3>' + table(['Attribute', 'Large', 'Medium', 'Small'], [['Height', 'The line height: 28px desktop, 24px mobile', '24px desktop, 22px mobile', '20px'], ['Gap between icon and text', '8px', '4px', '4px'], ['Icon size', '24px', '20px', '20px'], ['Padding and margin', '<td colspan="3">None</td>'], ['Hit area (invisible)', '28px / 24px (the link itself)', '24px (22px on mobile: grown by 2px)', '24px (20px: grown by 4px)'], ['Focus ring', '<td colspan="3">2px, 2px outside the link</td>']]) + \
    note('An action link has no padding or margin of its own, so there is no measurement figure.') + \
    '<h3 class="ds-h3 ds-group">Spacing</h3>' + desc('The gap as a spacing token.') + table(['Part', 'Value'], [['Gap, Large', '<code>space-8</code>'], ['Gap, Medium and Small', '<code>space-4</code>'], ['Focus ring offset', '2px']])

st_states = '<h2 class="ds-h2">States</h2>' + desc('<strong>Enabled</strong> has no underline: the placement and the icons carry the affordance. This is the reverse of the Inline link, whose underline is what tells it apart from the text it sits next to; an action link stands alone and is never embedded in prose. <strong>Hover</strong> is a color shift, and the underline appears under the label; the icons are never underlined. There is <strong>no Disabled state</strong>: hide the row or show plain text (see Usage). Hover is forced on this page; in your code it comes from <code>:hover</code>.') + \
    toolbar([('sb-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force'), ('ss-l', 'Size', 'data-mx="size"', [('large', 'Large', False), ('medium', 'Medium', True), ('small', 'Small', False)])]) + \
    '<div class="ds-table-wrap"><table class="ds-table pg-matrix" id="matrix"><thead><tr><th scope="col">State</th><th scope="col">Primary</th><th scope="col">Primary bold</th><th scope="col">Inverted</th><th scope="col">Inverted bold</th></tr></thead><tbody></tbody></table></div>'

st_typo = '<h2 class="ds-h2">Typography</h2><h3 class="ds-h3 ds-group">Features</h3>' + table(['Size', 'Type token', 'font-feature-settings'], [['Large', '<code>body-lg</code>', '<code>ss02</code>, <code>ss03</code>'], ['Medium', '<code>body-md</code>', '<code>ss02</code>, <code>ss03</code>, <code>ss06</code>'], ['Small', '<code>body-sm</code>', '<code>ss02</code>, <code>ss03</code>, <code>ss06</code>']]) + \
    '<h3 class="ds-h3 ds-group">Weight</h3>' + table(['Modifier', 'Class', 'CSS'], [['Regular', '(none)', '<code>font-weight: 400</code>'], ['Medium', '<code>action-link--weight-medium</code>', '<code>font-weight: 500</code>'], ['Bold', '<code>action-link--bold</code>', '<code>font-weight: 600</code>']]) + \
    note('Figma weights are 100 higher than the CSS (see <code>eco-typography</code>). The font package ships 300, 400, 500 and 700. ') + note('Breuer Condensed. Sizes and line heights are under Sizes.')

st_struct = '<h2 class="ds-h2">Structure</h2><h3 class="ds-h3 ds-group">Elements</h3>' + table(['Element', 'Class', 'Notes'], [
    ['Link', '<code>action-link</code>', 'A real <code>&lt;a href&gt;</code>, <code>display: inline-flex</code>.'], ['Label', '<code>action-link__label</code>', 'Always wrap the text in this span: the underline sits on it, so the icons never get one.'], ['Icon', '<code>action-link__icon</code>', 'A Material Symbol, <code>aria-hidden</code>. Leading, trailing (the chevron) or both; at least one.'],
    ['Size', '<code>action-link--large</code>, <code>--medium</code>, <code>--small</code>', ''], ['Weight, variant', '<code>action-link--bold</code>, <code>--inverted</code>', 'Regular and Primary are the defaults.']]) + \
    '<h3 class="ds-h3 ds-group">Types</h3>' + table(['Type', 'Class', 'Use'], [['Primary', '<code>action-link</code>', 'Light surfaces.'], ['Inverted', '<code>action-link action-link--inverted</code>', 'Dark surfaces.']]) + \
    '<h3 class="ds-h3 ds-group">Width</h3>' + desc('As wide as its content.')

st_motion = '<h2 class="ds-h2">Motion</h2>' + table(['Property', 'Duration', 'Easing'], [['<code>color</code>', '<code>duration-fast-3</code>', '<code>ease-standard</code>']]) + note('The underline is not transitioned.')

st_behavior = '<h2 class="ds-h2">Behavior</h2>' + table(['Input', 'Result'], [
    ['Click text or icon', 'Follows the link. The whole row is the target.'], ['Enter', 'Follows the focused link.'], ['Tab', 'The 2px focus ring shows on keyboard focus only (<code>body.keyboard-nav</code>).'], ['Icons', 'Never underlined: the underline is on <code>.action-link__label</code> only.'], ['Group of links', 'Stacked (<code>action-link-group--stacked</code>): one column, 8px between the links. Divided (<code>action-link-group--divided</code>): one row, a vertical divider only between two links on the same line, wrapping where the row is full. The author chooses the layout; it does not change with the breakpoint.'], ['Disabled', 'None. Hide the row or show plain text. If a disabled state must ship: <code>aria-disabled="true"</code>, exempt from the contrast minimum but still recognizable.'], ['Markup', 'A real <code>&lt;a href&gt;</code>. Icons are <code>aria-hidden</code>.']])

st_access = '<h2 class="ds-h2">Accessibility Requirements</h2>' + table(['Topic', 'Requirement'], [
    ['Element', 'A real <code>&lt;a href&gt;</code>, also for a download (add the <code>download</code> attribute when the file is on the same origin). If an instance triggers a JavaScript action with no navigation, it must be a <code>&lt;button&gt;</code> styled the same way: never fake it with an <code>&lt;a&gt;</code>.'], ['Name', 'The visible label, extended where needed so it still begins with the visible text (WCAG 2.5.3 Label in Name): “Download product sheet, PDF 2 megabytes”. Both icons are decorative: <code>aria-hidden="true"</code>, no alt text (WCAG 2.4.4).'], ['Downloads', 'Announce the file behavior in the accessible name: do not rely on the icon alone.'], ['Target size', 'A standalone link needs at least 24×24px (WCAG 2.5.8), and at least 8px between stacked links. The drawn size stays 20px (Small) and 22px (Medium on mobile), but an invisible layer (<code>.action-link::after</code>, at least 24px high) makes the clickable area 24px. Keep at least 8px between stacked links so the areas do not overlap.'], ['Focus', 'A 2px ring around the whole link with <code>border-focus</code> (4.9:1 on white) and 2px offset, on keyboard focus (WCAG 2.4.7, 1.4.11).'],
    ['Color', 'The default state has no underline, so the icons and the placement are the affordance. An action link must therefore never appear inside body copy, where it would rely on color alone (WCAG 1.4.1).'], ['Contrast', 'Label and icons need at least 4.5:1 in the default and hover states (WCAG 1.4.3). On white: Primary 21:1, Primary hover (<code>#737373</code>) 4.7:1 (4.4:1 on <code>#f6f6f6</code>), Inverted on black 21:1 and Inverted hover about 12:1. <strong>Open point:</strong> Inverted hover on a mid-gray such as <code>#737373</code> is 2.8:1. Confirm with design.']])

spec = [('design-tokens', st_tok), ('sizes', st_sizes), ('measurements', st_meas), ('states', st_states), ('typography', st_typo), ('structure', st_struct), ('motion', st_motion), ('behavior', st_behavior), ('accessibility-requirements', st_access)]

# ---------------------------------------------------------------- Code
c_basic = '<h2 class="ds-h2">Basic Usage</h2>' + desc('Link the shared stylesheet once per page. Never copy the rules into a page.') + table(['Step', 'What to do'], [
    ['1. Link', '<code>&lt;link rel="stylesheet" href="/components/css/action-link.css"&gt;</code>. Both templates already have it. The page needs the Material Symbols Outlined font.'], ['2. Markup', 'A real <code>&lt;a href&gt;</code> with <code>class="action-link action-link--medium"</code>.'],
    ['3. Label', 'Wrap the text in <code>&lt;span class="action-link__label"&gt;</code>, so the icons never get the underline.'], ['4. Icons', 'Add <code>&lt;span class="action-link__icon" aria-hidden="true"&gt;chevron_right&lt;/span&gt;</code>, and a leading icon when needed. The link has at least one icon: for a link with no icon in a text use an Inline link (also its reverse underline, <code>inline-link--reverse</code>).'], ['5. Variant', 'Add <code>action-link--bold</code>, <code>--weight-medium</code> or <code>--inverted</code> (on a dark surface).']])
c_al = '<h2 class="ds-h2">Action link</h2>' + desc('Copy the markup you need. Hover comes from <code>:hover</code>; the <code>[data-state]</code> selectors in the CSS exist only so the documentation can force a state.') + '<div id="recipes"></div>'
c_api = '<h2 class="ds-h2">API</h2><h3 class="ds-h3 ds-group">Classes</h3>' + table(['Class', 'Use'], [['<code>action-link</code>', 'The link.'], ['<code>action-link--large</code>, <code>--medium</code>, <code>--small</code>', 'Size.'], ['<code>action-link--bold</code>, <code>--weight-medium</code>', 'Bold or Medium weight. Regular is the default.'], ['<code>action-link--inverted</code>', 'For a dark surface.'], ['<code>action-link__label</code>', 'The text. Carries the hover underline.'], ['<code>action-link__icon</code>', 'An icon.'], ['<code>action-link-group</code>, <code>--stacked</code>', 'A group in one column, 8px between the links.'], ['<code>action-link-group--divided</code>', 'A group on one row with a vertical divider between the links, wrapping where the row is full.']]) + \
    '<h3 class="ds-h3 ds-group">Things to know</h3>' + bullets(['Breakpoint: Large and Medium change at 769px. The CSS does this by itself.', 'Always wrap the text in <code>action-link__label</code>: text-decoration on the link itself would also underline the icons.', 'A link with no <code>action-link__icon</code> is not styled: the CSS reverts it to the browser’s default link on purpose. Use an Inline link (<code>inline-link--reverse</code> for underline on hover only) when no icon is wanted.', 'The divided group draws its dividers as pseudo-elements in the gap before each link and clips what sits outside its left edge, so a divider never sits at the start or the end of a line. It has <code>overflow: hidden</code> with 4px of padding (and the same negative margin) so the focus ring is not cut off. The links must be direct children of the group (or wrapped one level, such as <code>li</code>).', 'The hit area is at least 24px high: <code>.action-link::after</code> is an invisible layer that grows the clickable area of a Small link (20px) and of a Medium link on mobile (22px) without changing the drawn size. Keep 8px between stacked links.', 'The focus ring needs <code>body.keyboard-nav</code>, which the templates set on the first Tab press.', 'The <code>[data-state]</code> selectors do nothing outside the documentation pages.'])
c_css = '<h2 class="ds-h2">CSS / Tailwind</h2>' + desc('The component is one CSS file, shared by every page. Link it, never copy it. The CSS below is read from the file the page links, so it is always what you see.') + code_box('css-code', 'CSS (components/css/action-link.css)')
code = [('basic-usage', c_basic), ('action-link', c_al), ('api', c_api), ('css-tailwind', c_css, False)]

# ---------------------------------------------------------------- scripts
AL_JS = r'''
  function icon(n) { var s = document.createElement('span'); s.className = 'action-link__icon'; s.setAttribute('aria-hidden', 'true'); s.textContent = n; return s; }
  function al(o) {
    var a = document.createElement('a'); a.href = '#';
    a.className = 'action-link action-link--' + o.size + (o.bold ? ' action-link--bold' : '') + (o.medium ? ' action-link--weight-medium' : '') + (o.inv ? ' action-link--inverted' : '');
    if (o.state && o.state !== 'enabled') a.dataset.state = o.state;
    if (o.leading) a.appendChild(icon(o.icon || 'file_download'));
    var lb = document.createElement('span'); lb.className = 'action-link__label'; lb.textContent = o.label; a.appendChild(lb); if (o.trailing !== false) a.appendChild(icon('chevron_right'));
    a.addEventListener('click', function (e) { e.preventDefault(); });
    return a;
  }
'''

JS_EX = AL_JS + r'''
  var st = { size: 'medium', weight: 'regular', variant: 'primary', state: 'enabled', icons: 'both' };
  function markup(o) {
    return '<a href="#" class="action-link action-link--' + o.size + (o.bold ? ' action-link--bold' : '') + (o.medium ? ' action-link--weight-medium' : '') + (o.inv ? ' action-link--inverted' : '') + '">\n' +
      (o.leading ? '  <span class="action-link__icon" aria-hidden="true">file_download</span>\n' : '') + '  <span class="action-link__label">' + esc(o.label) + '</span>\n' + (o.trailing !== false ? '  <span class="action-link__icon" aria-hidden="true">chevron_right</span>\n' : '') + '</a>';
  }
  function renderPg() {
    var o = { size: st.size, bold: st.weight === 'bold', medium: st.weight === 'medium', inv: st.variant === 'inverted', state: st.state, leading: st.icons !== 'trailing', trailing: st.icons !== 'leading', label: $('#pg-label').value };
    $('#pg-stage').classList.toggle('ds-stage--dark', o.inv);
    clear($('#pg-host')).appendChild(al(o));
    var h = markup(o);
    if (o.state !== 'enabled') h = '<!-- ' + o.state + ' is forced here for preview; in production it comes from ' + (o.state === 'focus' ? 'keyboard focus (body.keyboard-nav :focus-visible)' : ':hover') + ' -->\n' + h;
    $('#pg-code').textContent = h;
  }
  DK.wire(st, renderPg); $('#pg-label').addEventListener('input', renderPg);
  DK.bp();

  function rowsOf(host, label, extra) {
    var s = clear($(host));
    [['large', 'Large'], ['medium', 'Medium'], ['small', 'Small']].forEach(function (z) {
      var r = document.createElement('div'); r.className = 'pg-row';
      var base = extra || {};
      r.appendChild(al({ size: z[0], inv: base.inv, leading: base.leading, label: label || z[1] + ' regular' })); r.appendChild(al({ size: z[0], bold: true, inv: base.inv, leading: base.leading, label: label || z[1] + ' bold' })); s.appendChild(r);
    });
  }
  var wv = clear($('#v-weights')); [['', 'Regular'], ['medium', 'Medium'], ['bold', 'Bold']].forEach(function (z) { var r = document.createElement('div'); r.className = 'pg-row'; r.appendChild(al({ size: 'medium', medium: z[0] === 'medium', bold: z[0] === 'bold', label: z[1] })); wv.appendChild(r); });
  rowsOf('#v-sizes'); rowsOf('#v-primary', 'View all products'); rowsOf('#v-icon', 'Download document', { leading: true }); rowsOf('#v-inv', 'Read more', { inv: true });
  var fo = clear($('#v-focus')), fi = clear($('#v-focus-inv')); [['large', 'Large'], ['medium', 'Medium'], ['small', 'Small']].forEach(function (z) { fo.appendChild(al({ size: z[0], state: 'focus', label: z[1] })); fi.appendChild(al({ size: z[0], inv: true, state: 'focus', label: z[1] })); });

  $$('[data-prevent]').forEach(function (a) { a.addEventListener('click', function (e) { e.preventDefault(); }); });
  /* Usage figures */
  var d1 = clear($('#fig-ph-do')); d1.appendChild(al({ size: 'medium', label: 'View all products' }));
  var p = clear($('#fig-ph-dont')); p.appendChild(document.createTextNode('Read more about our work wear. ')); p.appendChild(al({ size: 'medium', label: 'View all products' }));
  p.lastChild.style.verticalAlign = 'bottom';
  var w1 = clear($('#fig-wt-do')); [['Download product sheet', true], ['Download manual', false], ['Download safety datasheet', false]].forEach(function (t) { w1.appendChild(al({ size: 'medium', leading: true, bold: t[1], label: t[0] })); });
  var w2 = clear($('#fig-wt-dont')); ['Download product sheet', 'Download manual', 'Download safety datasheet'].forEach(function (t) { w2.appendChild(al({ size: 'medium', leading: true, bold: true, label: t })); });
  var i1 = clear($('#fig-ic-do')); i1.appendChild(al({ size: 'medium', leading: true, icon: 'file_download', label: 'Download product sheet' })); i1.appendChild(al({ size: 'medium', label: 'View all accessories' }));
  var i2 = clear($('#fig-ic-dont')); i2.appendChild(al({ size: 'medium', leading: true, icon: 'star', label: 'Download product sheet' })); i2.appendChild(al({ size: 'medium', leading: true, icon: 'bolt', label: 'View all accessories' }));
  var DIV_unused = function () { var d = document.createElement('span'); d.className = 'divider divider--vertical divider--tertiary'; d.setAttribute('role', 'separator'); d.setAttribute('aria-orientation', 'vertical'); return d; };
  var r1 = clear($('#fig-row-do')); [['Order', 'file_download'], ['Waybill', 'link']].forEach(function (t) { r1.appendChild(al({ size: 'medium', leading: true, icon: t[1], label: t[0] })); });
  var r2 = clear($('#fig-row-dont')); [['Order', 'file_download'], ['Waybill', 'link']].forEach(function (t) { r2.appendChild(al({ size: 'medium', leading: true, icon: t[1], label: t[0] })); });
  var GRP = [['Order', 'file_download'], ['Waybill', 'link'], ['Packing instructions', 'attach_file']];
  var rs = clear($('#v-stacked')); GRP.forEach(function (t) { rs.appendChild(al({ size: 'medium', leading: true, icon: t[1], label: t[0] })); });
  var rd = clear($('#v-divided')); GRP.forEach(function (t) { rd.appendChild(al({ size: 'medium', leading: true, icon: t[1], label: t[0] })); });
  var k1 = clear($('#fig-stack-do')); ['Download product sheet', 'Download manual', 'Download safety datasheet'].forEach(function (t) { k1.appendChild(al({ size: 'medium', leading: true, label: t })); });
  var k2 = clear($('#fig-stack-dont')); [['large', 'Download product sheet'], ['small', 'Download manual'], ['medium', 'Download safety datasheet']].forEach(function (t) { k2.appendChild(al({ size: t[0], leading: true, label: t[1] })); });

  /* Anatomy */
  var aa = al({ size: 'large', leading: true, label: 'Download document' }); clear($('#al-anat-art')).appendChild(aa);
  var ics = $$('.action-link__icon', aa);
  function rng(el) { return function () { var r = document.createRange(); r.selectNodeContents(el); return r.getBoundingClientRect(); }; }
  DK.callouts($('#al-anat'), [
    { n: 1, el: ics[0], side: 'top', len: 48, at: 'edge' },
    { n: 2, side: 'bottom', len: 48, box: rng($('.action-link__label', aa)), at: 'edge' },
    { n: 3, el: ics[1], side: 'top', len: 48, at: 'edge' }
  ]);
  /* matching Do and Don't boxes have the same height (two columns only) */
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
'''

JS_SPEC = AL_JS + r'''
  var mx = { size: 'medium' };
  function buildMatrix() {
    var tb = clear($('#matrix tbody'));
    [['Enabled', 'enabled'], ['Hover', 'hover'], ['Focus', 'focus']].forEach(function (r) {
      var tr = document.createElement('tr'), th = document.createElement('th'); th.scope = 'row'; th.textContent = r[0]; tr.appendChild(th);
      [[false, false], [true, false], [false, true], [true, true]].forEach(function (c) {
        var td = document.createElement('td'); if (c[1]) td.className = 'pg-dark';
        td.appendChild(al({ size: mx.size, bold: c[0], inv: c[1], state: r[1], label: 'View all' })); tr.appendChild(td);
      });
      tb.appendChild(tr);
    });
  }
  DK.seg($('[data-mx="size"]'), function (v) { mx.size = v; buildMatrix(); });
  DK.bp(); buildMatrix();
  DK.tokenTable($('#tok-table tbody'), [
    ['Primary · enabled', 'Text and icons', 'text-action-primary'], ['Primary · hover', 'Text and icons', 'text-action-primary-hover'],
    ['Inverted · enabled', 'Text and icons', 'text-action-primary-inverted'], ['Inverted · hover', 'Text and icons', 'text-action-primary-inverted-hover'],
    ['Keyboard focus', 'Ring', 'border-focus']]);
'''

JS_CODE = r'''
  DK.recipes($('#recipes'), [
    ['Large, with a leading icon', '<a href="/downloads" class="action-link action-link--large">\n  <span class="action-link__icon" aria-hidden="true">file_download</span>\n  <span class="action-link__label">Download document</span>\n  <span class="action-link__icon" aria-hidden="true">chevron_right</span>\n</a>'],
    ['Medium', '<a href="/products" class="action-link action-link--medium">\n  <span class="action-link__label">View all products</span>\n  <span class="action-link__icon" aria-hidden="true">chevron_right</span>\n</a>'],
    ['Medium weight, trailing icon only', '<a href="/news" class="action-link action-link--medium action-link--weight-medium">\n  <span class="action-link__label">Read more</span>\n  <span class="action-link__icon" aria-hidden="true">chevron_right</span>\n</a>'],
    ['A group of links, stacked', '<div class="action-link-group action-link-group--stacked">\n  <a href="/order" class="action-link action-link--medium">…</a>\n  <a href="/waybill" class="action-link action-link--medium">…</a>\n</div>'],
    ['A group of links, divided', '<div class="action-link-group action-link-group--divided">\n  <a href="/order" class="action-link action-link--medium">…</a>\n  <a href="/waybill" class="action-link action-link--medium">…</a>\n</div>\n<!-- the divider is drawn by the group: no extra element between the links -->'],
    ['Small, bold, inverted (on a dark surface)', '<a href="/news" class="action-link action-link--small action-link--bold action-link--inverted">\n  <span class="action-link__label">Read more</span>\n  <span class="action-link__icon" aria-hidden="true">chevron_right</span>\n</a>']
  ]);
  DK.printCss($('#css-code'), 'action-link', [[/:is\(:hover, \[data-state="hover"\]\)/g, ':hover'], [/, \.[\w-]+\[data-state="focus"\]/g, '']]);
'''

C = dict(
    slug=SLUG, title='Action link', parent=PARENT, eyebrow='Components · Links',
    lead='An action link is a <strong>standalone link</strong> for lightweight actions like downloads and “view all” navigation, with a leading icon, a trailing icon or both. It is underlined on hover.',
    lead_ex='Every example on this page is the real component, not a picture. Figma: ' + fig_link(FIGMA, 'Action link') + '.',
    lead_spec='Tokens, sizes, states and requirements. Values come from the live token package and from Figma: ' + fig_link(FIGMA, 'Action link') + '.',
    lead_code='How to add an action link to a page. The file is <code>components/css/action-link.css</code>.',
    select_menu=False,
    css=['action-link'], style=STYLE, ex=ex, spec=spec, code=code, js_ex=JS_EX, js_spec=JS_SPEC, js_code=JS_CODE)

if __name__ == '__main__':
    emit(C)
