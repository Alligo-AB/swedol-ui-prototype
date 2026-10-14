from build import *

SLUG = 'section'
BADGE = '<span class="badge-basic badge-basic--warning badge-basic--weak" title="The skill has no Figma link. The values are the project’s own section rules.">Not verified with Figma</span>'

STYLE = r'''    .pg-note { font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-tertiary); }
    .pg-grid { display: grid; gap: 32px 24px; grid-template-columns: minmax(0, 1fr); width: 100%; }
    @media (min-width: 769px) { .pg-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
    .pg-cap { display: block; margin-bottom: 12px; font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-tertiary); }
    .sec-fig { --px-full: var(--dimension-spacing-space-24); width: 100%; }   /* demo: a fixed side margin, so a section fits a figure */
    .sec-ph { padding: var(--dimension-spacing-space-16); background: var(--color-surface-10); font-size: 14px; line-height: 20px; letter-spacing: 0.36px; }
    .sec-measure { --px-full: var(--px-page); display: block; width: 280px; }   /* demo: the side margin of the page, in a figure of fixed width */
    .sec-callout.ds-fig__stage.ds-callout { padding-right: 112px; }
    .sec-callout .ds-callout__art { width: 100%; max-width: 420px; }
    .sec-read { display: block; margin-top: 8px; font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-tertiary); }
    .sec-bp { background: var(--color-surface-02); }'''

playground = '<h2 class="ds-h2">Playground</h2>' + desc('Choose the position, the surface and the padding and the section and its code update. The padding is read live from the real section, so it changes as you resize the window.') + \
    '<div class="ds-playground"><div class="ds-stage" id="pg-stage"><div id="pg-host" style="width:100%"></div></div><div class="ds-controls">' + \
    btn_group('pg-l-pos', 'Position', 'data-pg="pos"', [('other', 'Other', True), ('first', 'First', False)]) + \
    btn_group('pg-l-bg', 'Background', 'data-pg="bg"', [('primary', 'White', True), ('secondary', 'Grey', False)]) + \
    btn_group('pg-l-pad', 'Padding', 'data-pg="pad"', [('on', 'Built-in', True), ('off', 'Zeroed', False)]) + \
    '<p class="pg-note" id="pg-read" role="status" style="margin:0"></p></div></div><h3 class="ds-h3">Markup for this selection</h3>' + code_box('pg-code', 'HTML')

overview = '<h2 class="ds-h2">Overview</h2>' + desc('A section is a <strong>full-width block of a page</strong>. It divides the content into clear parts and gives each part the white space it needs, with a padding that steps at the five ECO breakpoints.') + \
    desc('A section has two surfaces (white and grey), a first-section variant with less top padding, and a zeroed variant for five special cases. The same file also holds the <strong>page divider</strong>, a thin line between two sections, and the <strong>My Pages title block</strong> with its fixed spacing.') + \
    three_pages(SLUG, 'a section', 'the values: tokens, padding per breakpoint, measurements and requirements', 'how to add one to a page')

usage = '<h2 class="ds-h2">Usage</h2><h3 class="ds-h3 ds-group">When to use</h3>' + desc('Use a section for every distinct part of a page layout. Use it to:') + \
    bullets(['Divide a page into clear parts, such as a hero, a product list and an FAQ', 'Give each part the white space that separates it from the next', 'Mark a clear change of content with a grey surface', 'Make the side margin follow the grid and the 1200px maximum width']) + \
    '<h3 class="ds-h3 ds-group">When not to use</h3><h3 class="ds-h3">Keep the built-in padding</h3>' + desc('The padding is the white space that divides the content. Turn it off only in the five cases under Variants, and with a clear purpose. Everywhere else the content needs the air.') + \
    fig_pair('<div class="sec-fig" id="fig-pad-do"></div>', 'Do keep the built-in padding, so each part has its own air.', '<div class="sec-fig" id="fig-pad-dont"></div>', 'Do not zero the padding of ordinary content: the parts run together.') + \
    '<h3 class="ds-h3">Do not stack the air</h3>' + desc('A page divider has its own 48px of padding. Between two sections that already have padding, zero the divider’s vertical padding, or the two amounts of air add up.') + \
    fig_pair('<div class="sec-fig" id="fig-div-do"></div>', 'Do zero the divider’s own padding between two sections.', '<div class="sec-fig" id="fig-div-dont"></div>', 'Do not leave the divider’s 48px on top of the section padding.') + \
    '<h3 class="ds-h3">For a line inside content</h3>' + desc('A page divider is a boundary between two page sections. To separate items inside content, such as list rows, use the ' + link_large('divider.html', 'Divider') + ' component.') + \
    '<h3 class="ds-h3 ds-group">Quick reference</h3>' + \
    table(['The block…', 'Use'], [['is a full-width part of a page layout', 'Section'], ['separates two sections of one color lightly', 'Page divider'], ['separates items inside content', '<code>eco-divider</code>'], ['is the page title on a My Pages page', '<code>.main-content</code> and <code>.page-preamble</code>'], ['is the page frame (header, footer)', 'The page template']]) + \
    rules(['Write the xs padding first, then add sm, md, lg and xl.', 'Mark the first section with <code>.section--first</code>.', 'Use <code>--px-full</code> for the sides.', 'Zero the padding only for the five cases.'],
          ['Use another background without design approval.', 'Use <code>--px-page</code> for the divider’s sides.', 'Stack a divider’s 48px on a section’s own padding.', 'Use zeroed padding without a clear purpose.'])

anatomy = '<h2 class="ds-h2">Anatomy</h2><h3 class="ds-h3 ds-group">Section</h3>' + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout sec-callout" id="sec-anat" role="img" aria-label="Anatomy of a section: 1 padding top, 2 padding bottom, 3 surface, 4 content container"><div class="ds-callout__art"><section class="section sec-fig" id="an-sec" style="--px-full:24px;background:var(--color-surface-raised-primary)"><div class="sec-ph" id="an-content">Content</div></section></div></div></figure></div>' + \
    ol_parts([('Padding, top', 'The space above the content. It steps at each breakpoint, and the first section has less.'), ('Padding, bottom', 'The space below the content. It steps at each breakpoint.'), ('Surface', 'The background: white (<code>surface-raised-primary</code>) or grey (<code>surface-raised-secondary</code>).'), ('Content container', 'The content area. The side margin comes from <code>--px-full</code>, so the content stays inside the grid.')])

variants = '<h2 class="ds-h2">Variants</h2>' + desc('A section varies in surface, position and padding. The page divider and the My Pages title block are part of the same file.') + \
    '<h3 class="ds-h3 ds-group">Surface</h3>' + desc('White is the default. A page should start with a white section or use white only. Grey marks a clear change of content.') + \
    '<div class="ds-stage" style="padding:0"><div class="sec-fig" id="v-surface"></div></div>' + \
    '<h3 class="ds-h3 ds-group">Position</h3>' + desc('The first section on a page has less top padding, because the breadcrumb or the header sits right above it. Mark it with <code>.section--first</code>.') + \
    '<div class="pg-grid"><div><span class="pg-cap">Other section (<code>section</code>)</span><div class="ds-stage" style="padding:0"><div class="sec-fig" id="v-other"></div></div></div><div><span class="pg-cap">First section (<code>section section--first</code>)</span><div class="ds-stage" style="padding:0"><div class="sec-fig" id="v-first"></div></div></div></div>' + \
    '<h3 class="ds-h3 ds-group">Zeroed padding</h3>' + desc('The built-in padding is normally always on. Turn it off with <code>.section--flush</code> only in these five cases.') + \
    '<div class="pg-grid"><div><span class="pg-cap">Built-in</span><div class="ds-stage" style="padding:0"><div class="sec-fig" id="v-builtin"></div></div></div><div><span class="pg-cap">Zeroed (<code>section--flush</code>)</span><div class="ds-stage" style="padding:0"><div class="sec-fig" id="v-flush"></div></div></div></div>' + \
    table(['#', 'Case', 'Use when'], [['1', 'Divider inside a section', 'Two parts with the same background, no clear break wanted, but the content should keep the section padding.'], ['2', 'Adjacent topic with an in-between section', 'Two sections cover one topic and a semi-topic section (cross-sell, product placement) sits between them.'], ['3', 'Fluid hero banner', 'The section is the container of a full-width banner for new products or a campaign.'], ['4', 'First section next to a component with built-in spacing', 'Zero the top padding when the content follows a breadcrumb.'], ['5', 'First section with a fluid banner first', 'Zero top and bottom when the page starts with a full-width banner or image.']]) + \
    '<h3 class="ds-h3 ds-group">Page divider</h3>' + desc('A thin line between two sections of the same color, when a full section break would feel heavy. It is a <code>div</code>, not a section, and it uses <code>--px-full</code> so the line stops where the content stops.') + \
    '<h3 class="ds-h3">Replacing a section boundary</h3>' + desc('With its own 48px of padding above and below.') + \
    '<div class="ds-stage" style="padding:0"><div class="sec-fig" id="v-div1"></div></div>' + \
    '<h3 class="ds-h3">Between two sections that already have padding</h3>' + desc('Zero the divider’s vertical padding, or the air stacks.') + \
    '<div class="ds-stage" style="padding:0"><div class="sec-fig" id="v-div2"></div></div>' + \
    '<h3 class="ds-h3 ds-group">My Pages title block</h3>' + desc('On My Pages the page title block has fixed spacing that must always be used: <code>.main-content</code> above the title and <code>.page-preamble</code> below it.') + \
    '<div class="ds-stage" style="padding:0"><div class="sec-fig" id="v-mypages"></div></div>'

sizes = '<h2 class="ds-h2">Sizes</h2>' + desc('A section has no sizes. Its padding changes with the breakpoint and with the position (first or other), at all five ECO breakpoints. The values are under ' + sec_link(SLUG, 'sizes', 'Sizes') + ' in Specifications, with the row for your window width marked.')

layout = '<h2 class="ds-h2">Layout &amp; Appearance</h2><h3 class="ds-h3 ds-group">Alignment</h3>' + desc('The content starts at the side margin <code>--px-full</code> and ends at the same margin on the other side. The margin follows the grid (16px xs, 32px sm and md, 40px lg) and centers the content against the 1200px maximum width on wide screens.') + \
    '<h3 class="ds-h3 ds-group">Placement</h3>' + desc('The first section on a page follows the breadcrumb directly and carries <code>.section--first</code>. Later sections follow each other with no gap: the padding of each is the white space between the parts. On My Pages, the page title block comes before the first section.') + \
    '<h3 class="ds-h3 ds-group">Width</h3>' + desc('A section is always as wide as the window. Only the content inside it is limited to 1200px.') + \
    '<h3 class="ds-h3 ds-group">Appearance</h3>' + desc('The default surface is white. By making white the base color of the page, a clear and calm structure is created, and a grey section stands out as a change. Exceptions exist, such as product list pages and My Pages. Other backgrounds need design approval.')

behavior = '<h2 class="ds-h2">Behavior</h2>' + desc('A section is not interactive. It has no hover, focus or disabled state and it does not animate.') + \
    '<h3 class="ds-h3 ds-group">Breakpoints</h3>' + desc('The padding steps at 640px, 769px, 1024px and 1281px, so a section has five sets of values. Unlike most components, <code>sm</code> (640 to 768px) has its own values. The side margin also follows the breakpoint.')

access = '<h2 class="ds-h2">Accessibility</h2>' + desc('All requirements are listed under ' + sec_link(SLUG, 'accessibility-requirements', 'Accessibility Requirements') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Keyboard support</h3>' + desc('None. A section and a page divider are not focusable.') + \
    '<h3 class="ds-h3 ds-group">Screen reader support</h3>' + desc('Give each section a heading, so the parts of the page can be found. A <code>&lt;section&gt;</code> becomes a landmark only when it has an accessible name, for example with <code>aria-labelledby</code> that points to its heading. The page divider is an empty <code>div</code> and is not announced.')

related = '<h2 class="ds-h2">Related</h2><ul class="ds-bullets"><li><strong>' + link_large('divider.html', 'Divider') + '</strong>. A line between items inside content.</li><li><strong>' + link_large('breadcrumb.html', 'Breadcrumb') + '</strong>. Sits above the first section.</li><li><strong>' + link_large('collapsible.html', 'Collapsible') + '</strong>. An FAQ list is often the content of a section.</li></ul>'

references = '<h2 class="ds-h2">References</h2>' + refs([
    ('https://www.w3.org/WAI/WCAG22/Understanding/info-and-relationships.html', 'WCAG 2.2: Info and Relationships', 'Success criterion 1.3.1: the structure of the page must be in the markup.'),
    ('https://www.w3.org/WAI/WCAG22/Understanding/reflow.html', 'WCAG 2.2: Reflow', 'Success criterion 1.4.10: content must fit a narrow window without sideways scrolling.'),
    ('https://developer.mozilla.org/en-US/docs/Web/HTML/Element/section', 'MDN: the section element', 'When to use it and how to name it.'),
    ('https://www.w3.org/WAI/ARIA/apg/patterns/landmarks/examples/region.html', 'WAI-ARIA Authoring Practices: Region landmark', 'A section with an accessible name.'),
    ('https://m3.material.io/foundations/layout/understanding-layout/overview', 'Material Design 3: Understanding layout', 'Google. Margins and regions.'),
    ('https://carbondesignsystem.com/elements/spacing/overview/', 'Carbon Design System: Spacing', 'IBM. A fixed scale for the white space.')])

ex = [('playground', playground), ('overview', overview), ('usage', usage), ('anatomy', anatomy), ('variants', variants), ('sizes', sizes), ('layout', layout), ('behavior', behavior), ('accessibility', access), ('related', related), ('references', references)]

# ---------------------------------------------------------------- Specifications
st_tok = '<h2 class="ds-h2">Design Tokens</h2>' + desc('Resolved from the live token package.') + \
    '<div class="ds-table-wrap"><table class="ds-table" id="tok-table"><thead><tr><th scope="col">Part</th><th scope="col">Use</th><th scope="col">Token</th><th scope="col">Value</th></tr></thead><tbody></tbody></table></div>' + \
    '<h3 class="ds-h3 ds-group">Spacing</h3>' + desc('The padding values are on the fixed spacing scale (<code>eco-spacing</code>).') + \
    table(['Value', 'Token', 'Used for'], [['16px', '<code>space-16</code>', 'Top padding, first section (xs). Side margin (xs).'], ['24px', '<code>space-24</code>', 'My Pages title (xs and sm).'], ['32px', '<code>space-32</code>', 'Top padding (xs), first section (sm, md). Side margin (sm, md).'], ['40px', '<code>space-40</code>', 'Bottom padding (xs), first section (lg). Side margin (lg).'], ['48px', '<code>space-48</code>', 'Top and bottom (sm), first section (xl). Page divider.'], ['56px', '<code>space-56</code>', 'Top padding (md).'], ['64px', '<code>space-64</code>', 'Bottom padding (md).'], ['72px', '<code>space-72</code>', 'Top padding (lg, xl).'], ['80px', '<code>space-80</code>', 'Bottom padding (lg, xl).']]) + \
    note('<strong>Open point:</strong> <code>section.css</code> writes these values as pixels, not as <code>var(--dimension-spacing-space-…)</code>. The values are the same; the file is not changed yet.')

st_sizes = '<h2 class="ds-h2">Sizes</h2>' + desc('The padding steps at the five ECO breakpoints. The row for the current window width is marked.') + \
    '<h3 class="ds-h3 ds-group">First section</h3>' + table(['Breakpoint', 'Top', 'Bottom'], [['xs · 0–639px', '16px', '40px'], ['sm · 640–768px', '32px', '48px'], ['md · 769–1023px', '32px', '64px'], ['lg · 1024–1280px', '40px', '80px'], ['xl · 1281px+', '48px', '80px']], id_='t-first') + \
    '<h3 class="ds-h3 ds-group">Other sections</h3>' + table(['Breakpoint', 'Top', 'Bottom'], [['xs · 0–639px', '32px', '40px'], ['sm · 640–768px', '48px', '48px'], ['md · 769–1023px', '56px', '64px'], ['lg · 1024–1280px', '72px', '80px'], ['xl · 1281px+', '72px', '80px']], id_='t-other') + \
    '<h3 class="ds-h3 ds-group">Side margin</h3>' + desc('<code>var(--px-full)</code>: the grid margin that also centers the content against the 1200px maximum width.') + \
    table(['Breakpoint', 'Margin'], [['xs', '16px'], ['sm and md', '32px'], ['lg', '40px'], ['xl', 'Centered: the larger of 40px and half of the window minus 1200px']]) + \
    '<h3 class="ds-h3 ds-group">Page divider</h3>' + table(['Part', 'Value'], [['Padding, top and bottom', '48px (zero it between two sections that have padding)'], ['Padding, sides', '<code>var(--px-full)</code>'], ['Line', '1px']]) + \
    '<h3 class="ds-h3 ds-group">My Pages title block</h3>' + table(['Breakpoint', '<code>.main-content</code> padding-top', '<code>.page-preamble</code> margin-bottom'], [['xs', '24px', '24px'], ['sm', '24px', '32px'], ['md and up', '40px', '40px']])

SEC_MEAS = ('<div class="measure__item"><span class="measure__name">%d · %s</span><div class="measure__obj"><span class="sec-measure"><section class="section%s measure__subject" style="background:var(--color-surface-raised-primary)"><div class="sec-ph">Content</div></section></span>'
            '<i class="measure__pad measure__pad--t"></i><i class="measure__pad measure__pad--b"></i><i class="measure__pad measure__pad--l"></i><i class="measure__pad measure__pad--r"></i>'
            '<b class="measure__dim measure__dim--v measure__dim--t"><span></span></b><b class="measure__dim measure__dim--v measure__dim--b"><span></span></b><b class="measure__dim measure__dim--h measure__dim--l"><span></span></b><b class="measure__dim measure__dim--h measure__dim--r"><span></span></b></div></div>')

st_meas = '<h2 class="ds-h2">Measurements</h2><h3 class="ds-h3 ds-group">Dimensions</h3>' + desc('Padding of a section at the current window width. The shaded areas are the padding. The numbers are read from the real component, so they change when you resize the window.') + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-fig__stage--flush" style="padding:0;min-height:0"><div class="measure" role="img" aria-label="Padding of a section: other section and first section">' + SEC_MEAS % (1, 'Other section', '') + SEC_MEAS % (2, 'First section', ' section--first') + '</div></div><figcaption class="ds-fig__cap">A section at true size (1:1), in a figure 280px wide. The side margin is the page margin of the window.</figcaption></figure></div>' + \
    note('There is no Breakpoint toolbar: the padding steps at four widths, and the toolbar only switches at 769px. Resize the window, or read the table under Sizes.') + \
    table(['Attribute', 'Value'], [['Padding, top and bottom', 'See the figure and Sizes: per position and breakpoint'], ['Padding, sides', '<code>var(--px-full)</code>: 16, 32 or 40px, then centered'], ['Width', 'The full width of the window'], ['Content maximum width', '1200px'], ['Corners', 'Square']]) + \
    '<h3 class="ds-h3 ds-group">Spacing</h3>' + desc('The padding as spacing tokens is listed under <a class="inline-link inline-link--large inline-link--secondary" href="#design-tokens">Design Tokens</a>.')

st_states = '<h2 class="ds-h2">States</h2>' + desc('A section has no states: no hover, focus, active or disabled.')

st_struct = '<h2 class="ds-h2">Structure</h2><h3 class="ds-h3 ds-group">Elements</h3>' + table(['Element', 'Class', 'Notes'], [
    ['Section', '<code>section</code>', 'A <code>&lt;section&gt;</code>. White surface, padding per breakpoint, sides <code>var(--px-full)</code>.'], ['Surface', '<code>section--secondary</code>', 'Grey surface (<code>surface-raised-secondary</code>).'], ['Position', '<code>section--first</code>', 'Less top padding, for the first section on a page.'], ['Padding', '<code>section--flush</code>', 'Zero top and bottom padding.'],
    ['Page divider', '<code>page-divider</code> and <code>page-divider__line</code>', 'A <code>div</code> with a 1px line.'], ['My Pages title', '<code>main-content</code> and <code>page-preamble</code>', 'The spacing around the page title.']]) + \
    '<h3 class="ds-h3 ds-group">Types</h3>' + table(['Type', 'Class', 'Use'], [['White', '<code>section</code>', 'The default.'], ['Grey', '<code>section section--secondary</code>', 'A clear change of content.'], ['First', '<code>section section--first</code>', 'The first section of a page.'], ['Zeroed', '<code>section section--flush</code>', 'The five cases only.']]) + \
    '<h3 class="ds-h3 ds-group">Width</h3>' + desc('A section is as wide as the window. The content is limited to 1200px by the side margin.')

st_behavior = '<h2 class="ds-h2">Behavior</h2>' + table(['Topic', 'Result'], [['Input', 'None. A section has no hover, focus or click.'], ['Breakpoint', 'The padding steps at 640, 769, 1024 and 1281px.'], ['Window width', 'The side margin follows <code>--px-full</code>, so the content stays centered against 1200px.'], ['Motion', 'None.']])

st_access = '<h2 class="ds-h2">Accessibility Requirements</h2>' + table(['Topic', 'Requirement'], [
    ['Headings', 'Give every section a heading, so the structure is in the markup and not only in the padding (WCAG 1.3.1).'], ['Landmark', 'A <code>&lt;section&gt;</code> is a landmark only with an accessible name (<code>aria-labelledby</code> or <code>aria-label</code>). Add one when the part is important to navigate to.'],
    ['Color', 'Never use the grey surface as the only sign of a change. The heading must also show it.'], ['Reflow', 'The content must fit 320px without sideways scrolling (WCAG 1.4.10). The side margin is 16px at xs.'], ['Page divider', 'An empty <code>div</code>: decorative and not announced. It must not carry meaning.']])

spec = [('design-tokens', st_tok), ('sizes', st_sizes), ('measurements', st_meas), ('states', st_states), ('structure', st_struct), ('behavior', st_behavior), ('accessibility-requirements', st_access)]

# ---------------------------------------------------------------- Code
c_basic = '<h2 class="ds-h2">Basic Usage</h2>' + desc('Link the shared stylesheet once per page. Never copy the rules into a page.') + table(['Step', 'What to do'], [
    ['1. Link', '<code>&lt;link rel="stylesheet" href="/components/css/section.css"&gt;</code>. Both templates already have it.'], ['2. Side margin', 'The page defines <code>--px-full</code>. The templates already do; a page without it has no side margin.'],
    ['3. First section', 'Add <code>section--first</code> to the first section after the breadcrumb.'], ['4. Surface', 'White is the default. Add <code>section--secondary</code> for a grey section.'], ['5. Zeroed padding', 'Add <code>section--flush</code> only for the five cases.']])
c_sec = '<h2 class="ds-h2">Section</h2>' + desc('Copy the markup you need.') + '<div id="recipes"></div>'
c_api = '<h2 class="ds-h2">API</h2><h3 class="ds-h3 ds-group">Classes</h3>' + table(['Class', 'Use'], [['<code>section</code>', 'The block: padding per breakpoint, white surface, sides <code>var(--px-full)</code>.'], ['<code>section--first</code>', 'Less top padding.'], ['<code>section--secondary</code>', 'Grey surface.'], ['<code>section--flush</code>', 'Zero top and bottom padding.'], ['<code>page-divider</code>, <code>page-divider__line</code>', 'A line between two sections.'], ['<code>main-content</code>, <code>page-preamble</code>', 'The My Pages page title block.']]) + \
    '<h3 class="ds-h3 ds-group">Things to know</h3>' + bullets(['<code>--px-full</code> must be defined by the page. Use it, never <code>--px-page</code>, for a divider’s sides.', 'The shared file marks the first section with <code>.section--first</code> only; <code>:first-of-type</code> is not in the file.', 'Between two sections that have padding, set <code>padding-top: 0; padding-bottom: 0</code> on the page divider.', 'Mobile-first: write xs with no prefix, then add sm, md, lg and xl.'])
c_css = '<h2 class="ds-h2">CSS / Tailwind</h2>' + desc('The component is one CSS file, shared by every page. Link it, never copy it. The CSS below is read from the file the page links, so it is always what you see.') + code_box('css-code', 'CSS (components/css/section.css)')
code = [('basic-usage', c_basic), ('section', c_sec), ('api', c_api), ('css-tailwind', c_css, False)]

# ---------------------------------------------------------------- scripts
SEC_JS = r'''
  function bpName() { var w = innerWidth; return w >= 1281 ? 'xl' : w >= 1024 ? 'lg' : w >= 769 ? 'md' : w >= 640 ? 'sm' : 'xs'; }
  function sec(cls, label, extra) { return '<section class="section ' + cls + '"' + (extra || '') + '><div class="sec-ph">' + label + '</div></section>'; }
'''

JS_EX = SEC_JS + r'''
  var st = { pos: 'other', bg: 'primary', pad: 'on' };
  function cls() { return 'section' + (st.pos === 'first' ? ' section--first' : '') + (st.bg === 'secondary' ? ' section--secondary' : '') + (st.pad === 'off' ? ' section--flush' : ''); }
  function renderPg() {
    var host = clear($('#pg-host'));
    host.innerHTML = '<section class="' + cls() + '" style="--px-full:24px"><div class="sec-ph">Content</div></section>';
    var cs = getComputedStyle(host.firstChild);
    $('#pg-read').textContent = 'At ' + bpName() + ' (' + innerWidth + 'px): top ' + cs.paddingTop + ', bottom ' + cs.paddingBottom + '.';
    $('#pg-code').textContent = '<section class="' + cls() + '">\n  <!-- content -->\n</section>';
  }
  DK.wire(st, renderPg); window.addEventListener('resize', renderPg);

  /* Usage figures */
  $('#fig-pad-do').innerHTML = sec('section--first', 'Hero') + sec('', 'Product list');
  $('#fig-pad-dont').innerHTML = sec('section--first section--flush', 'Hero') + sec('section--flush', 'Product list');
  var ds = '<div class="page-divider" style="padding-top:0;padding-bottom:0"><div class="page-divider__line"></div></div>';
  $('#fig-div-do').innerHTML = sec('section--first', 'Product list') + ds + sec('', 'Delivery');
  $('#fig-div-dont').innerHTML = sec('section--first', 'Product list') + '<div class="page-divider"><div class="page-divider__line"></div></div>' + sec('', 'Delivery');

  /* Anatomy */
  var an = $('#an-sec'), ac = $('#an-content');
  function pad(side) { return function () { var r = an.getBoundingClientRect(), p = parseFloat(getComputedStyle(an)['padding' + side]); return { left: r.left, top: side === 'Top' ? r.top : r.bottom - p, width: r.width, height: p }; }; }
  DK.callouts($('#sec-anat'), [
    { n: 1, box: pad('Top'), side: 'left', len: 44, at: 'center' },
    { n: 2, box: pad('Bottom'), side: 'left', len: 44, at: 'center' },
    { n: 3, el: an, side: 'bottom', len: 56 },
    { n: 4, el: ac, side: 'right', len: 56, at: 'center' }
  ]);

  /* Variants */
  $('#v-surface').innerHTML = sec('section--first', 'White: surface-raised-primary') + sec('section--secondary', 'Grey: surface-raised-secondary');
  function read(id, html) { var h = $(id); h.innerHTML = html + '<span class="sec-read"></span>'; }
  read('#v-other', sec('', 'Content'));
  read('#v-first', sec('section--first', 'Content'));
  read('#v-builtin', sec('section--secondary', 'Content'));
  read('#v-flush', sec('section--secondary section--flush', 'Content'));
  $$('.sec-read').forEach(function (r) { var s = r.previousElementSibling; r.dataset.for = '1'; r._s = s; });
  function readouts() { $$('.sec-read').forEach(function (r) { var cs = getComputedStyle(r._s); r.textContent = 'Padding: top ' + cs.paddingTop + ', bottom ' + cs.paddingBottom; }); }
  readouts(); window.addEventListener('resize', readouts);
  $('#v-div1').innerHTML = sec('section--first', 'Content above') + '<div class="page-divider"><div class="page-divider__line"></div></div>' + sec('', 'Content below');
  $('#v-div2').innerHTML = sec('section--first', 'Content above') + ds + sec('', 'Content below');
  $('#v-mypages').innerHTML = '<div class="main-content"><div class="page-preamble"><h3 class="ds-h3" style="margin:0">My page title</h3></div><div class="sec-ph">Content</div></div>';
  renderPg();
'''

JS_SPEC = r'''
  function bpName() { var w = innerWidth; return w >= 1281 ? 'xl' : w >= 1024 ? 'lg' : w >= 769 ? 'md' : w >= 640 ? 'sm' : 'xs'; }
  DK.tokenTable($('#tok-table tbody'), [['Section', 'Surface (default)', 'surface-raised-primary'], ['Section', 'Surface, grey', 'surface-raised-secondary'], ['Page divider', 'Line', 'border-primary']]);
  function mark() {
    var b = bpName();
    ['#t-first', '#t-other'].forEach(function (id) {
      $$(id + ' tbody tr').forEach(function (r) { var on = r.firstChild.textContent.split(' ')[0] === b; r.classList.toggle('sec-bp', on); if (on) r.setAttribute('aria-current', 'true'); else r.removeAttribute('aria-current'); });
    });
  }
  mark(); window.addEventListener('resize', mark);
'''

JS_CODE = r'''
  DK.recipes($('#recipes'), [
    ['First section, then another (link section.css)', '<section class="section section--first">…</section>\n<section class="section section--secondary">…</section>'],
    ['Zeroed padding (a fluid hero banner)', '<section class="section section--flush">\n  <img src="hero.jpg" alt="" style="display:block;width:100%" />\n</section>'],
    ['Page divider between two sections of one color', '<div class="page-divider"><div class="page-divider__line"></div></div>'],
    ['Page divider between two sections that have padding', '<div class="page-divider" style="padding-top:0;padding-bottom:0"><div class="page-divider__line"></div></div>'],
    ['A section with a landmark name', '<section class="section" aria-labelledby="faq-title">\n  <h2 id="faq-title">Questions and answers</h2>\n</section>'],
    ['My Pages title block', '<div class="main-content">\n  <div class="page-preamble">…</div>\n</div>']]);
  DK.printCss($('#css-code'), 'section');
'''

C = dict(
    slug=SLUG, title='Section', eyebrow='Components · Layout and content', eyebrow_extra=BADGE,
    lead='A section is a <strong>full-width block of a page</strong>. Its padding adjusts at each breakpoint and its surface is white or grey.',
    lead_ex='Every example on this page is the real component, not a picture. Specification: <code>.claude/skills/eco-section/SKILL.md</code>.',
    lead_spec='The tokens, the padding per breakpoint, the measurements and the requirements. Values come from the live token package and from the specification skill.',
    lead_code='How to add a section to a page. The file is <code>components/css/section.css</code>.',
    select_menu=False,
    css=['section'], style=STYLE, ex=ex, spec=spec, code=code, js_ex=JS_EX, js_spec=JS_SPEC, js_code=JS_CODE)

if __name__ == '__main__':
    emit(C)
