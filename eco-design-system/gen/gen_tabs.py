from build import *

F_ITEMS = 'https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=2166-63997'
F_BAR = 'https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=2515-77815'
F_INFO = 'https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=3521-126512'
SLUG = 'tabs'
FIGS = fig_link(F_ITEMS, 'Tab items') + ', ' + fig_link(F_BAR, 'Tab bar sizes') + ', ' + fig_link(F_INFO, 'Tab info')

STYLE = r'''    .pg-col { display: flex; flex-direction: column; align-items: stretch; gap: 24px; width: 100%; }
    .pg-note { font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-tertiary); }
    .pg-cap { font-size: 12px; line-height: 12px; letter-spacing: 0.48px; text-transform: uppercase; color: var(--color-text-tertiary); font-weight: 600; display: block; margin-bottom: 8px; }
    .pg-matrix td { vertical-align: middle; padding-top: 16px; padding-bottom: 16px; }
    .pg-panel { padding: 16px 0; font-size: 16px; line-height: 22px; color: var(--color-text-secondary); }
    .pg-narrow { width: 320px; max-width: 100%; border: 1px dashed var(--color-border-primary); }
    .tb-measure .tab-bar { padding: 0; margin: 0; border-bottom: 0; }   /* demo: the bar's focus-ring room and divider would move the shaded strips off the tab */
    .tb-measure { display: block; }
    .ds-callout__art { width: 100%; max-width: 420px; padding-right: 0; }'''

playground = '<h2 class="ds-h2">Playground</h2>' + desc('Click a tab or use the arrow keys, Home and End. <strong>Primary</strong> tabs sit at the top of a content page; <strong>Secondary</strong> tabs sit below them, inside a content area. Large and Medium look the same on desktop; Small is smaller.') + \
    '<div class="ds-playground"><div class="ds-stage" id="pg-stage"><div id="pg-host" style="width:100%"></div></div><div class="ds-controls">' + \
    bp_field('pg-l-bp') + btn_group('pg-l-name', 'Type', 'data-pg="name"', [('primary', 'Primary', True), ('secondary', 'Secondary', False)]) + \
    btn_group('pg-l-size', 'Size', 'data-pg="size"', [('lg', 'Large', True), ('md', 'Medium', False), ('sm', 'Small', False)]) + \
    btn_group('pg-l-conf', 'Content', 'data-pg="conf"', [('label', 'Label', False), ('both', 'Label + icon', True), ('icon', 'Icon only', False)]) + \
    btn_group('pg-l-status', 'Status', 'data-pg="status"', [('none', 'None', True), ('dot', 'Dot', False), ('count', 'Number', False)]) + \
    btn_group('pg-l-lead', 'Leading icon (label only)', 'data-pg="lead"', [('off', 'Off', True), ('on', 'On', False)]) + \
    btn_group('pg-l-bg', 'Background', 'data-pg="bg"', [('white', 'White', True), ('grey', 'Grey', False)]) + \
    btn_group('pg-l-acc', 'Accent colour (active line)', 'data-pg="accent"', [('black', 'Black', True), ('swedol', 'Swedol', False), ('tools', 'Tools', False)]) + \
    '</div></div><h3 class="ds-h3">Markup for this selection</h3>' + code_box('pg-code', 'HTML')

overview = '<h2 class="ds-h2">Overview</h2>' + desc('Tabs organise content across screens, data sets and interactions at the same level of hierarchy. A tab bar lets the user move between groups of related content without leaving the page. For content that must be read in order, use steps instead.') + \
    desc('Tabs come as Primary and Secondary, in three sizes, with a label, a label and an icon, or an icon only, and with an optional status dot or number. A bar either switches panels on the same page (content tabs) or links to other pages (navigation tabs).') + \
    three_pages(SLUG, 'tabs', 'the values: tokens, sizes, states and requirements', 'how to add a tab bar to a page')

usage = '<h2 class="ds-h2">Usage</h2><h3 class="ds-h3 ds-group">When to use</h3>' + desc('Use tabs to organise content at the same level of hierarchy. They control the region shown below them. Use them to:') + \
    bullets(['Move between pages or sections at the same level, as sub-navigation (for example the My Pages account menu)', 'Separate related content inside an area, such as a card, a sheet or an information pane', 'Show product information in groups: overview, details, reviews, support']) + \
    '<h3 class="ds-h3 ds-group">When not to use</h3><h3 class="ds-h3">For content that must be read in order</h3>' + desc('Use a stepper (steps) when the user goes through content in a fixed order. Use <code>eco-pill-segment-control</code> to switch between two to four views or filters of the same content, a button group for joined options in a toolbar, and <code>eco-radio</code> for a choice that is submitted.') + \
    '<h3 class="ds-h3">For more than two levels</h3>' + desc('Secondary tabs go below primary tabs, never above, and a page does not nest more than two levels.') + \
    fig_pair('<div class="pg-col" id="fig-do"></div>', 'Do put secondary tabs below the primary tabs.', '<div class="pg-col" id="fig-dont"></div>', 'Do not put secondary tabs above the primary tabs.') + \
    '<h3 class="ds-h3">Keep labels short</h3>' + desc('Tab labels sit in one row. A few short labels are read at a glance; long labels make the bar scroll sideways and hide tabs.') + \
    fig_pair('<div class="pg-col" id="fig-lab-do"></div>', 'Do keep the labels short and the tabs few.', '<div class="pg-col" id="fig-lab-dont"></div>', 'Do not use long labels: the bar scrolls and tabs are hidden.') + \
    '<h3 class="ds-h3 ds-group">Quick reference</h3>' + \
    table(['The user…', 'Use'], [['moves between pages or sections at the same level', 'Tabs'], ['switches between 2–4 views or filters of the same content', '<a class="inline-link inline-link--small" href="segment-control.html">Pill segment control</a>'], ['chooses between a few joined options in a toolbar', '<a class="inline-link inline-link--small" href="button-group.html">Button group</a>'], ['goes through content in a fixed order', 'Steps (stepper)'], ['makes a choice that is submitted', '<a class="inline-link inline-link--small" href="radio.html">Radio</a>']]) + \
    rules(['Group content at the same level of hierarchy.', 'Put secondary tabs below primary tabs, never above.', 'Keep labels short, in one row. Prefer scrollable tabs for long titles.', 'Use only globally known icons for icon-only tabs, with an <code>aria-label</code>.'],
          ['Use tabs for content that must be read in order.', 'Nest more than two levels of tabs.', 'Make a tab with a click handler on a <code>div</code>.', 'Copy the CSS into a page: link <code>tabs.css</code>.'])

anatomy = '<h2 class="ds-h2">Anatomy</h2><h3 class="ds-h3 ds-group">Tab bar</h3>' + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout" id="tb-anat" role="img" aria-label="Anatomy of a tab bar: 1 tab, 2 icon and label, 3 active line, 4 status, 5 divider"><div class="ds-callout__art"><div id="a-host"></div></div></div></figure></div>' + \
    ol_parts([('Tab', 'A button (content tabs) or a link (navigation tabs). Primary tabs have 24px between them; Secondary tabs have 16px padding on each side.'), ('Icon and label', 'An optional 20px icon above an uppercase label. A label can also have a leading 24px icon. An icon-only tab needs an <code>aria-label</code>.'), ('Active line', 'Under the active tab: 3px on Primary, 2px on Secondary. It slides to the clicked tab. Black by default, or the accent colour.'),
              ('Status', 'A red dot or a red number after the label, 4px away. It marks something new, or says how many.'), ('Divider', 'A 1px line under the whole bar. It runs the full width, also when the bar scrolls.')])

variants = '<h2 class="ds-h2">Variants</h2>' + toolbar([('vb-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force')]) + \
    '<h3 class="ds-h3 ds-group">Primary and Secondary</h3>' + desc('<strong>Primary</strong> tabs are placed at the top of a content page, as sub-navigation when the main navigation needs more levels, or as top-level navigation where there is none (for example campaign pages). The line spans the label, 24px between tabs. <strong>Secondary</strong> tabs are always placed below primary tabs, if any. They separate related content inside an area (a card, a sheet, an information pane, sections on one page). Each tab has 16px side padding, so the line is wider than the label.') + fig_one('<div class="pg-col" id="v-types"></div>') + \
    '<h3 class="ds-h3 ds-group">Content</h3>' + desc('Label only, label with an icon above it, or icon only. Use standalone icons only when they are globally well known, and give each an <code>aria-label</code>.') + fig_one('<div class="pg-col" id="v-conf"></div>') + \
    '<h3 class="ds-h3 ds-group">Status and leading icon</h3>' + desc('A red dot marks something new in a tab. A red number badge says how many. Both sit after the label, 4px away. On an icon-only tab the dot sits at the icon’s top right. An icon can also lead the label: 24px, or 20px on Small below 769px.') + fig_one('<div class="pg-col" id="v-status"></div>') + \
    '<h3 class="ds-h3 ds-group">On a grey surface</h3>' + desc('Background Colored in Figma: the hover line is <code>surface-40</code> instead of <code>surface-10</code>, so it stays visible on grey. Add <code>.tab-bar--on-grey</code>.') + fig_one('<div class="pg-col" id="v-grey"></div>', stage_attr=' style="background:var(--color-background-secondary)"') + \
    '<h3 class="ds-h3 ds-group">Accent colour</h3>' + desc('The active line is black by default. Where a product uses its accent colour, set <code>--tab-line-active</code> on the bar. Swedol uses <code>--color-accent-default</code>; Tools is a primitive in the package (<code>--color-primitive-color-brand-tools-accent-brand</code>). Primary and Secondary tabs, content tabs and link tabs all follow it; the grey hover line does not change. Click a tab to see the line slide in the accent colour.') + fig_one('<div class="pg-col" id="v-accent"></div>') + \
    '<h3 class="ds-h3 ds-group">Many tabs</h3>' + desc('Tab labels appear in one row. Scrollable tabs are preferred when the titles do not fit: the bar scrolls sideways and the divider line runs the full width. Drag or scroll the bar below.') + fig_one('<div class="pg-col"><div class="pg-narrow" id="v-scroll"></div></div>')

sizes = '<h2 class="ds-h2">Sizes</h2>' + desc('Large, Medium and Small. Below 769px the labels are 16/16 (Large, Medium) and 14/14 (Small); from 769px 18/18 and 16/16. Large and Medium differ only in the gap to the line on mobile. Measurements are under ' + sec_link(SLUG, 'sizes', 'Sizes') + ' in Specifications.') + \
    toolbar([('sb-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force')]) + fig_one('<div class="pg-col" id="v-sizes"></div>')

layout = '<h2 class="ds-h2">Layout &amp; Appearance</h2><h3 class="ds-h3 ds-group">Placement</h3>' + desc('Primary tabs go at the top of a content page. Secondary tabs go below them, inside the content area they control. The bar is as wide as its container.') + \
    '<h3 class="ds-h3 ds-group">Overflow</h3>' + desc('The bar scrolls sideways with the scrollbar hidden, and the active tab is scrolled into view. The divider runs the full width. The overflow “more” button is not built yet.') + \
    '<h3 class="ds-h3 ds-group">Appearance</h3>' + desc('Labels are uppercase Breuer Condensed. The active tab has a black label and a black line; hover gives a grey line. Token names and values are under ' + sec_link(SLUG, 'design-tokens', 'Design Tokens') + ' in Specifications.')

behavior = '<h2 class="ds-h2">Behavior</h2><h3 class="ds-h3 ds-group">Switching</h3>' + desc('A click on a tab, or arrow-key focus, opens that tab. On content tabs the active line slides to the clicked tab. On navigation tabs the line slides across the page change.') + \
    '<h3 class="ds-h3 ds-group">Hover and focus</h3>' + desc('Hover gives a grey 3px line and greys the label and the icon. Focus is a 2px ring around icon and label, on an enabled or an active tab alike; the line stays visible below it. All states are listed under ' + sec_link(SLUG, 'states', 'States') + ' in Specifications. Figma has no disabled state, so none is built.') + \
    '<h3 class="ds-h3 ds-group">Motion</h3>' + desc('The sliding line uses <code>duration-medium-2</code> with <code>ease-standard</code> and is off under reduced motion. Details are under ' + sec_link(SLUG, 'motion', 'Motion') + ' in Specifications.')

access = '<h2 class="ds-h2">Accessibility</h2>' + desc('All requirements are listed under ' + sec_link(SLUG, 'accessibility-requirements', 'Accessibility Requirements') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Keyboard support</h3>' + desc('Tab moves into the bar. Left and Right switch tab (they wrap), Home and End go to the first and last. A tab opens as soon as it is focused. <code>tabs.js</code> does this.') + \
    '<h3 class="ds-h3 ds-group">Screen reader support</h3>' + desc('Content tabs use <code>role="tablist"</code>, <code>role="tab"</code> with <code>aria-selected</code> and <code>aria-controls</code>, and <code>role="tabpanel"</code> with <code>aria-labelledby</code>. Navigation tabs are links in a <code>nav</code>, with <code>aria-current="page"</code> on the current one. An icon-only tab needs an <code>aria-label</code>.')

related = '<h2 class="ds-h2">Related</h2><ul class="ds-bullets"><li><strong>' + link_large('segment-control.html', 'Pill segment control') + '</strong>. Two to four views or filters of the same content.</li><li><strong>' + link_large('button-group.html', 'Button group') + '</strong>. Joined options in a toolbar.</li><li><strong>' + link_large('radio.html', 'Radio button') + '</strong>. A choice that is submitted.</li><li><strong>' + link_large('badge.html', 'Badge') + '</strong>. The status dot and number on a tab.</li></ul>'

references = '<h2 class="ds-h2">References</h2>' + refs([
    ('https://www.w3.org/WAI/ARIA/apg/patterns/tabs/', 'WAI-ARIA Authoring Practices: Tabs', 'Keyboard and role requirements.'),
    ('https://www.nngroup.com/articles/tabs-used-right/', 'Nielsen Norman Group: Tabs, Used Right', 'When tabs help and when they hide content.'),
    ('https://fluent2.microsoft.design/components/web/react/core/tablist/usage', 'Fluent 2: Tab list', 'Microsoft.'),
    ('https://m3.material.io/components/tabs/overview', 'Material Design 3: Tabs', 'Google.'),
    ('https://carbondesignsystem.com/components/tabs/usage/', 'Carbon Design System: Tabs', 'IBM.')])

ex = [('playground', playground), ('overview', overview), ('usage', usage), ('anatomy', anatomy), ('variants', variants), ('sizes', sizes), ('layout', layout), ('behavior', behavior), ('accessibility', access), ('related', related), ('references', references)]

# ---------------------------------------------------------------- Specifications
st_tok = '<h2 class="ds-h2">Design Tokens</h2>' + desc('Resolved from the live token package.') + \
    '<div class="ds-table-wrap"><table class="ds-table" id="tok-table"><thead><tr><th scope="col">State</th><th scope="col">Part</th><th scope="col">Token</th><th scope="col">Value</th></tr></thead><tbody></tbody></table></div>' + \
    note('<strong>Open points:</strong> the enabled icon colour has no token in the Figma export; <code>text-secondary</code> is used. Figma shows the Primary active line at 3px and the Secondary at 2px; both are built as shown. Large and Medium are identical on desktop in Figma. The overflow “more” button is not built yet (scrolling is).')

st_sizes = '<h2 class="ds-h2">Sizes</h2>' + table(['Size', 'Mobile and tablet (below 769px)', 'Desktop (769px+)'], [
    ['Large', 'Label 16/16, 0.32px · gap to line 10px · tab 56px (label only: bar 29px)', 'Label 18/18, 0.18px · gap 12px · tab 60px (bar 33px)'], ['Medium', 'Label 16/16, 0.32px · gap 8px · tab 54px (bar 27px)', 'Label 18/18, 0.18px · gap 12px · tab 60px (bar 33px)'],
    ['Small', 'Label 14/14, 0.42px · gap 8px · tab 52px (bar 25px)', 'Label 16/16, 0.48px · gap 8px · tab 54px (bar 27px)'], ['Icon only', 'Tab 30px · icon 20px · gap 8px', 'Tab 34px (Large, Medium) or 30px (Small) · gap 12px or 8px']]) + \
    note('Tab = icon 20px + 8px + label + gap + the 2px line; a bar adds the 1px divider. Label only has no icon. Primary: 24px between tabs. Secondary: 16px padding each side, no gap. sm (640–768px) still has the mobile size.')


def mfig(n, name, bar, extra, inner):
    return ('<div class="measure__item"><span class="measure__name">%d · %s</span><div class="measure__obj"><span class="tb-measure"><div class="tab-bar %s" role="tablist" aria-label="%s">%s</div></span>'
            '<i class="measure__pad measure__pad--t"></i><i class="measure__pad measure__pad--b"></i><i class="measure__pad measure__pad--l"></i><i class="measure__pad measure__pad--r"></i>'
            '<b class="measure__dim measure__dim--v measure__dim--t"><span></span></b><b class="measure__dim measure__dim--v measure__dim--b"><span></span></b><b class="measure__dim measure__dim--h measure__dim--l"><span></span></b><b class="measure__dim measure__dim--h measure__dim--r"><span></span></b></div></div>') % (n, name, bar, name, inner)


st_meas = '<h2 class="ds-h2">Measurements</h2><h3 class="ds-h3 ds-group">Dimensions</h3>' + desc('Padding of one tab. Below the label (or the icon) sits the gap to the line plus the 2px line: 14px on desktop Large and Medium. Secondary tabs also have 16px on each side, so the line is wider than the label. Primary tabs have no side padding: the gap between them is 24px. The numbers are read from the component.') + \
    toolbar([('mb-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force')]) + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-fig__stage--flush" style="padding:0;min-height:0"><div class="measure" role="img" aria-label="Padding of a tab: Secondary label tab and icon-only tab">' + \
    mfig(1, 'Secondary · label', 'tab-bar--secondary', '', '<button class="tab tab--active measure__subject" role="tab" aria-selected="true" tabindex="-1"><span class="tab__label">Overview</span></button>') + \
    mfig(2, 'Primary · icon only', 'tab-bar--primary', '', '<button class="tab tab--active tab--icon-only measure__subject" role="tab" aria-selected="true" aria-label="Info" tabindex="-1"><span class="ms tab__icon" aria-hidden="true">info</span></button>') + \
    '</div></div><figcaption class="ds-fig__cap">A tab at true size (1:1). Change the Breakpoint to see the mobile values.</figcaption></figure></div>' + \
    table(['Attribute', 'Value'], [['Tab, label only (Large)', '56px with an icon, 29px bar without (mobile); 60px and 33px from 769px'], ['Padding below the label or icon', 'Gap to the line plus the 2px line: Large 10 + 2 mobile, 12 + 2 desktop; Medium 8 + 2 mobile, 12 + 2 desktop; Small 8 + 2'], ['Padding, left and right, Primary', 'None. 24px between tabs'], ['Padding, left and right, Secondary', '16px, no gap between tabs'], ['Icon-only tab', 'Same bottom padding (10px mobile, 14px desktop for Large and Medium); no side padding'],
                                  ['Icon', '20px, 8px above the label'], ['Leading icon in the label', '24px (20px on Small below 769px), 4px before the text'],
                                  ['Active line', '3px Primary, 2px Secondary'], ['Bar divider', '1px'], ['Focus ring', '2px, 4px clear above, left and right; 6px above the tab’s bottom edge']]) + \
    '<h3 class="ds-h3 ds-group">Spacing</h3>' + desc('The same distances as spacing tokens.') + table(['Part', 'Value'], [['Between Primary tabs', '<code>space-24</code>'], ['Secondary tab padding, left and right', '<code>space-16</code>'], ['Icon to label, status to label, leading icon to text', '<code>space-8</code> and <code>space-4</code>'], ['Label to line', '8px, 10px or 12px (see Sizes): literals'], ['Focus ring room', '4px: the bar has <code>padding: 4px 4px 0; margin: -4px -4px 0</code>']]) + \
    note('Because of the focus-ring room the bar’s divider sticks out 4px past the content column on each side.')

st_states = '<h2 class="ds-h2">States</h2>' + desc('Enabled, hover, active and focus. Focus is a 2px ring around icon and label, on an enabled or an active tab alike; the line stays visible below it. Hover and focus are forced on this page. Figma has no disabled state, so none is built.') + \
    toolbar([('sm-t', 'Type', 'data-matrix="name"', [('primary', 'Primary', True), ('secondary', 'Secondary', False)]), ('sm-s', 'Size', 'data-matrix="size"', [('lg', 'Large', True), ('md', 'Medium', False), ('sm', 'Small', False)]), ('sm-b', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force')]) + \
    '<div class="ds-table-wrap"><table class="ds-table pg-matrix" id="matrix"><thead><tr><th scope="col">State</th><th scope="col">Label + icon</th><th scope="col">Label</th><th scope="col">Icon only</th><th scope="col">Rule</th></tr></thead><tbody></tbody></table></div>'

st_typo = '<h2 class="ds-h2">Typography</h2>' + table(['Size', 'Type', 'Mobile (below 769px)', 'Desktop (769px+)'], [['Large', '<code>label-lg</code>', '16/16, 0.32px', '18/18, 0.18px'], ['Medium', '<code>label-lg</code>', '16/16, 0.32px', '18/18, 0.18px'], ['Small', '<code>label-md</code>', '14/14, 0.42px', '16/16, 0.48px'], ['Number badge', '—', '10/10, no letter spacing', '10/10, no letter spacing']]) + \
    note('Breuer Condensed, weight 600 (Figma bold 700 − 100), uppercase, with <code>ss02</code> and <code>ss03</code>.')

st_struct = '<h2 class="ds-h2">Structure</h2><h3 class="ds-h3 ds-group">Elements</h3>' + table(['Element', 'Class', 'Notes'], [
    ['Bar', '<code>tab-bar</code>', 'The row plus the 1px divider (<code>border-primary</code>).'], ['Tab', '<code>tab</code>, <code>tab--active</code>, <code>tab--icon-only</code>', 'A <code>button</code> (content) or <code>a</code> (navigation).'], ['Icon', '<code>tab__icon</code> with <code>ms</code>', '20px, above the label.'], ['Label', '<code>tab__label</code>', 'Uppercase. Optional leading <code>ms</code> icon.'],
    ['Status', '<code>tab__dot</code>, <code>tab__count</code>', '6px dot, or a red pill with a number (16px high).'], ['Sliding line', '<code>tab-bar__indicator</code>', 'Added by <code>tabs.js</code>.'], ['Panel', '<code>tab-panel</code>', 'Content of a content tab. <code>role="tabpanel"</code>.']]) + \
    '<h3 class="ds-h3 ds-group">Types</h3>' + table(['Modifier', 'Effect'], [['<code>.tab-bar--primary</code>', '24px gap between tabs; line spans the label only; active line 3px'], ['<code>.tab-bar--secondary</code>', 'No gap, each tab has 16px side padding, line spans label and padding; active line 2px'], ['<code>.tab-bar--md</code>, <code>.tab-bar--sm</code>', 'Medium and Small. Default (no class) is Large.'], ['<code>.tab-bar--on-grey</code>', 'Hover line <code>surface-40</code> instead of <code>surface-10</code>'],
                                                                                 ['<code>--tab-line-active</code>', 'Custom property: colour of the active line (default <code>surface-100</code>)']]) + \
    '<h3 class="ds-h3 ds-group">Width</h3>' + desc('Figma bars hug their content (the divider ends at the last tab). The component fills its container, per the overflow information in Figma. Say if hugging is wanted.')

st_motion = '<h2 class="ds-h2">Motion</h2>' + table(['Property', 'Duration', 'Easing'], [['Sliding active line: <code>transform</code> and <code>width</code>', '<code>duration-medium-2</code>', '<code>ease-standard</code>'], ['Hover line grows from the bottom', '<code>duration-medium-2</code>', '<code>ease-decelerate-generic</code>'], ['Hover line colour fades', '<code>duration-medium-2</code>', '<code>ease-standard</code>'], ['Label and icon colour', 'Instant', '—']]) + \
    note('Content tabs: the line slides to the clicked tab (<code>tabs.js</code> moves one <code>.tab-bar__indicator</code>). Link tabs slide across the page change: a click keeps the hover look, the next page starts the line under the old tab and slides it to the new one (the old index is kept in <code>sessionStorage</code> for 5 s; the bar needs the same <code>aria-label</code> on every page). The tab the line is travelling to keeps its grey hover line until the sliding line has arrived over it. All of it is off under reduced motion.')

st_behavior = '<h2 class="ds-h2">Behavior</h2>' + table(['Topic', 'Rule'], [
    ['Keyboard', 'Tab moves into the bar, Left and Right switch tab (they wrap), Home and End go to the first and last. A tab opens as soon as it is focused. <code>tabs.js</code> does this.'], ['Content tabs', 'The selected tab has <code>tabindex="0"</code>, the others <code>-1</code>. Exactly one tab is active.'], ['Navigation tabs', 'Links in a <code>nav</code>, the current page has <code>aria-current="page"</code>. Link <code>tabs.js</code> for the sliding line.'],
    ['Accent colour', 'The active line is black (<code>surface-100</code>) by default. Where a product uses its accent colour, set <code>--tab-line-active</code> on the bar: Swedol <code>--color-accent-default</code>; Tools is a primitive in the package (<code>--color-primitive-color-brand-tools-accent-brand</code>). The My Pages prototype pages use <code>var(--brand)</code>, their own accent alias. Never restyle <code>.tab::after</code> or <code>.tab-bar__indicator</code>.'],
    ['Overflow', 'The bar scrolls sideways with the scrollbar hidden; the active tab is scrolled into view. The divider runs the full width.'], ['On-page navigation', 'Link tabs whose <code>href</code> is an <code>#anchor</code> work as an on-page nav (<code>toc.js</code>, see <code>eco-doc-page</code>).']])

st_access = '<h2 class="ds-h2">Accessibility Requirements</h2>' + table(['Topic', 'Requirement'], [
    ['Content tabs', '<code>role="tablist"</code> on the bar, <code>role="tab"</code> on each tab (<code>button</code>) with <code>aria-selected</code> and <code>aria-controls</code>, <code>role="tabpanel"</code> with <code>aria-labelledby</code> on the content. The selected tab has <code>tabindex="0"</code>, the others <code>-1</code>.'], ['Navigation tabs', 'Links in a <code>nav</code> with an <code>aria-label</code>; the current page has <code>aria-current="page"</code>.'],
    ['Icon only', 'Needs an <code>aria-label</code>. A status dot or number needs a text alternative where its meaning is not clear.'], ['Focus', '2px ring <code>border-focus</code> on <code>:focus-visible</code> (WCAG 2.4.7, 1.4.11). The active line stays visible.'], ['Motion', 'The sliding line is off under <code>prefers-reduced-motion</code> (WCAG 2.3.3).'], ['Never', 'A tab as a <code>div</code> with a click handler.']])

spec = [('design-tokens', st_tok), ('sizes', st_sizes), ('measurements', st_meas), ('states', st_states), ('typography', st_typo), ('structure', st_struct), ('motion', st_motion), ('behavior', st_behavior), ('accessibility-requirements', st_access)]

# ---------------------------------------------------------------- Code
c_basic = '<h2 class="ds-h2">Basic Usage</h2>' + desc('Link the shared files once per page. Never copy the rules into a page.') + table(['Step', 'What to do'], [
    ['1. Link', '<code>&lt;link rel="stylesheet" href="/components/css/tabs.css"&gt;</code> and <code>&lt;script src="/components/js/tabs.js"&gt;&lt;/script&gt;</code> (the sliding line, for content tabs and link tabs). Both templates already have them.'], ['2. Choose', '<strong>Content tabs</strong> switch panels on the same page: <code>role="tablist"</code> with <code>button.tab</code>. <strong>Navigation tabs</strong> go to another page: a <code>nav.tab-bar</code> with <code>a.tab</code>.'],
    ['3. Type and size', '<code>tab-bar--primary</code> or <code>tab-bar--secondary</code>; Large is the default, add <code>tab-bar--md</code> or <code>tab-bar--sm</code>.'], ['4. Icons', 'The icon class <code>ms</code> (Material Symbols) comes from the page, as in the templates.']])
c_tabs = '<h2 class="ds-h2">Tabs</h2><div id="recipes"></div>'
c_api = '<h2 class="ds-h2">API</h2><h3 class="ds-h3 ds-group">Classes</h3>' + table(['Class', 'Use'], [
    ['<code>tab-bar</code>', 'The bar. Needs <code>tab-bar--primary</code> or <code>tab-bar--secondary</code>.'], ['<code>tab-bar--md</code>, <code>tab-bar--sm</code>', 'Medium and Small. Default is Large.'], ['<code>tab-bar--on-grey</code>', 'For grey surfaces.'], ['<code>tab</code>, <code>tab--active</code>, <code>tab--icon-only</code>', 'A tab. <code>tab--active</code>, <code>aria-selected="true"</code> and <code>aria-current</code> all give the active look.'],
    ['<code>tab__icon</code>, <code>tab__label</code>, <code>tab__dot</code>, <code>tab__count</code>', 'Parts of a tab.'], ['<code>tab-panel</code>', 'The content of a content tab.']]) + \
    '<h3 class="ds-h3 ds-group">Things to know</h3>' + bullets(['Always a <code>button</code> (content tabs) or an <code>a</code> (navigation tabs). Never a <code>div</code> with a click handler.', 'Keep exactly one active tab.', 'Breakpoint: values switch at 769px; 640–768px is still mobile.', 'Set <code>--tab-line-active</code> on the bar for the accent colour. Never restyle <code>.tab::after</code> or <code>.tab-bar__indicator</code>.', 'Keep the same <code>aria-label</code> on a navigation bar on every page, so the line can slide across the page change.', 'The My Pages account menu is migrated: <code>nav.tab-bar.tab-bar--primary</code> of <code>a.tab</code>, with <code>--tab-line-active: var(--brand)</code>.'])
c_css = '<h2 class="ds-h2">CSS / Tailwind</h2>' + desc('The component is one CSS file and one script, shared by every page. Link them, never copy them.') + code_box('css-code', 'CSS (components/css/tabs.css)') + '<div style="margin-top:16px">' + code_box('js-code', 'JS (components/js/tabs.js)') + '</div>'
code = [('basic-usage', c_basic), ('tabs', c_tabs), ('api', c_api), ('css-tailwind', c_css, False)]

# ---------------------------------------------------------------- scripts
TAB_JS = old_js('tabs', "  var LABELS =", "  function renderPg() {")

JS_EX = TAB_JS + r'''
  function renderPg() {
    var o = { name: st.name, size: st.size, conf: st.conf, status: st.status, lead: st.lead === 'on', accent: st.accent };
    $('#pg-stage').style.background = st.bg === 'grey' ? 'var(--color-background-secondary)' : '';
    var host = clear($('#pg-host')); mount(host, { name: o.name, size: o.size, conf: o.conf, status: o.status, lead: o.lead, accent: o.accent, grey: st.bg === 'grey' }, true); wire(host);
    var code = html({ name: o.name, size: o.size, conf: o.conf, status: o.status, lead: o.lead, accent: o.accent, grey: st.bg === 'grey', uid: 'p-' }, false);
    $('#pg-code').textContent = code;
  }
  DK.wire(st, renderPg); DK.bp();

  function cap(host, text) { var c = document.createElement('span'); c.className = 'pg-cap'; c.textContent = text; host.appendChild(c); }
  function block(host, text, o) { var d = document.createElement('div'); cap(d, text); mount(d, o, false); wire(d); host.appendChild(d); return d; }
  var vt = clear($('#v-types'));
  block(vt, 'Primary', { name: 'primary', size: 'lg', conf: 'label' }); block(vt, 'Primary with icons', { name: 'primary', size: 'lg', conf: 'both' });
  block(vt, 'Secondary', { name: 'secondary', size: 'lg', conf: 'label' }); block(vt, 'Secondary with icons', { name: 'secondary', size: 'lg', conf: 'both' });
  var vs = clear($('#v-sizes')); [['lg', 'Large'], ['md', 'Medium'], ['sm', 'Small']].forEach(function (z) { block(vs, z[1] + ' · primary', { name: 'primary', size: z[0], conf: 'both' }); block(vs, z[1] + ' · secondary', { name: 'secondary', size: z[0], conf: 'label' }); });
  var vc = clear($('#v-conf')); block(vc, 'Label', { name: 'primary', size: 'lg', conf: 'label' }); block(vc, 'Label + icon', { name: 'primary', size: 'lg', conf: 'both' }); block(vc, 'Icon only', { name: 'primary', size: 'lg', conf: 'icon' });
  var vst = clear($('#v-status')); block(vst, 'Dot', { name: 'primary', size: 'lg', conf: 'label', status: 'dot' }); block(vst, 'Number', { name: 'primary', size: 'lg', conf: 'label', status: 'count' }); block(vst, 'Leading icon', { name: 'primary', size: 'lg', conf: 'label', lead: true }); block(vst, 'Dot, icon only', { name: 'primary', size: 'lg', conf: 'icon', status: 'dot' });
  var vg = clear($('#v-grey')); block(vg, 'Primary, hover on the second tab', { name: 'primary', size: 'lg', conf: 'label', grey: true, hover: 1 }); block(vg, 'Secondary, hover on the second tab', { name: 'secondary', size: 'lg', conf: 'label', grey: true, hover: 1 });
  var vac = clear($('#v-accent')); Object.keys(ACCENT).forEach(function (k) { block(vac, ACCENT[k][1] ? ACCENT[k][0] + ' · ' + ACCENT[k][1] : ACCENT[k][0] + ' · --color-surface-100', { name: 'primary', size: 'lg', conf: 'label', accent: k }); });
  var vsc = clear($('#v-scroll')); (function () { var d = document.createElement('div'); mount(d, { name: 'secondary', size: 'lg', conf: 'label', n: 4 }, false); wire(d); var bar = $('.tab-bar', d); ['Warranty', 'Downloads', 'Spare parts', 'Accessories'].forEach(function (l) { var b = document.createElement('button'); b.className = 'tab'; b.setAttribute('role', 'tab'); b.setAttribute('aria-selected', 'false'); b.tabIndex = -1; b.innerHTML = '<span class="tab__label">' + l + '</span>'; bar.appendChild(b); }); vsc.appendChild(d); })();

  /* Usage figures: secondary below primary (do) and above (don't) */
  function pair(host, first, second) { var a = block(host, '', first), b = block(host, '', second); $$('.pg-cap', host).forEach(function (c) { c.remove(); }); return [a, b]; }
  pair(clear($('#fig-do')), { name: 'primary', size: 'md', conf: 'label', n: 3 }, { name: 'secondary', size: 'md', conf: 'label', n: 3 });
  pair(clear($('#fig-dont')), { name: 'secondary', size: 'md', conf: 'label', n: 3 }, { name: 'primary', size: 'md', conf: 'label', n: 3 });

  /* Keep labels short */
  var sh = clear($('#fig-lab-do')); block(sh, '', { name: 'primary', size: 'md', conf: 'label', n: 3 }); $$('.pg-cap', sh).forEach(function (c) { c.remove(); });
  var lg = clear($('#fig-lab-dont')), lgb = block(lg, '', { name: 'primary', size: 'md', conf: 'label', n: 4 }); $$('.pg-cap', lg).forEach(function (c) { c.remove(); });
  $$('.tab__label', lgb).forEach(function (l, i) { l.textContent = ['Technical specifications', 'Frequently asked questions', 'Customer reviews', 'Warranty and returns'][i]; });

  /* Anatomy */
  var ah = clear($('#a-host'));
  mount(ah, { name: 'primary', size: 'lg', conf: 'both', n: 3, status: 'count' }, false); wire(ah);
  var tabs = $$('.tab', ah), bar = $('.tab-bar', ah);
  DK.callouts($('#tb-anat'), [
    { n: 1, el: tabs[0], side: 'top', len: 44, at: 'edge' },
    { n: 2, el: $('.tab__icon', tabs[0]), side: 'left', len: 56 },
    { n: 3, side: 'bottom', len: 44, box: function () { var r = tabs[0].getBoundingClientRect(); var l = $('.tab__label', tabs[0]).getBoundingClientRect(); return { left: l.left, top: r.bottom - 3, width: l.width, height: 3 }; } },
    { n: 4, el: $('.tab__count', ah), side: 'top', len: 44 },
    { n: 5, side: 'bottom', len: 44, box: function () { var r = bar.getBoundingClientRect(); return { left: r.right - 40, top: r.bottom - 1, width: 40, height: 1 }; } }
  ]);
  renderPg();
'''

JS_SPEC = TAB_JS + r'''
  var mt = { name: 'primary', size: 'lg' };
  var STATES = [['Enabled', {}, 'Label <code>text-primary</code>, icon <code>text-secondary</code>. No line (only the bar divider).'], ['Hover', { hover: 1 }, 'Label and icon <code>text-tertiary</code>, a 3px line <code>surface-10</code> (<code>surface-40</code> on grey).'], ['Active', { active: 0 }, 'Label <code>text-primary</code>, icon <code>icon-primary</code>, line <code>surface-100</code>: 3px primary, 2px secondary.'], ['Focus, enabled', { focus: 1 }, '2px ring <code>border-focus</code> around icon and label. Colours stay as enabled.'], ['Focus, active', { focus: 0, active: 0 }, 'The same ring on the active tab; the line stays visible below it.'], ['Disabled', null, '']];
  function matrix() {
    var tb = clear($('#matrix tbody'));
    STATES.forEach(function (r) {
      var tr = document.createElement('tr'), th = document.createElement('th'); th.scope = 'row'; th.textContent = r[0]; tr.appendChild(th);
      ['both', 'label', 'icon'].forEach(function (c) {
        var td = document.createElement('td'); td.style.textAlign = 'left';
        if (r[1]) { var d = document.createElement('div'); mount(d, { name: mt.name, size: mt.size, conf: c, n: 2, hover: r[1].hover, focus: r[1].focus }, false); td.appendChild(d); } else td.innerHTML = '<span class="ds-na">Not defined</span>';
        tr.appendChild(td);
      });
      var d2 = document.createElement('td'); d2.innerHTML = r[2] || 'Not in Figma, so not built.'; tr.appendChild(d2); tb.appendChild(tr);
    });
  }
  $$('[data-matrix]').forEach(function (g) { DK.seg(g, function (v) { mt[g.dataset.matrix] = v; matrix(); }); });
  matrix();
  DK.tokenTable($('#tok-table tbody'), [['Enabled', 'Label', 'text-primary'], ['Enabled', 'Icon', 'text-secondary'], ['Hover', 'Label and icon', 'text-tertiary'], ['Hover', 'Line (white surface)', 'surface-10'], ['Hover', 'Line (grey surface)', 'surface-40'], ['Active', 'Label', 'text-primary'], ['Active', 'Icon', 'icon-primary'], ['Active', 'Line (default)', 'surface-100'], ['Active', 'Line, accent: Swedol', 'accent-default'], ['Active', 'Line, accent: Tools', 'primitive-color-brand-tools-accent-brand'], ['All', 'Bar divider', 'border-primary'], ['Focus', 'Ring', 'border-focus'], ['Status', 'Dot and number badge', 'surface-danger-default'], ['Status', 'Number text', 'text-primary-inverted']]);
  DK.bp(function () { if (window.ECO_MEASURE) ECO_MEASURE.init(); });
'''

JS_CODE = TAB_JS + r'''
  DK.recipes($('#recipes'), [
    ['Content tabs, primary (link the CSS and the JS)', html({ name: 'primary', size: 'lg', conf: 'both', n: 2, uid: 'r-' }, false)],
    ['Navigation tabs, secondary (links)', html({ name: 'secondary', size: 'md', conf: 'label', n: 2, kind: 'nav' }, false)],
    ['Accent colour of the active line (page CSS)', '.your-tab-bar {\n  --tab-line-active: var(--color-accent-default);   /* default: var(--color-surface-100), black */\n}'],
    ['Link the shared files', '<link rel="stylesheet" href="/components/css/tabs.css">\n<script src="/components/js/tabs.js"><\/script>   <!-- the sliding line, for content tabs and link tabs -->']]);
  DK.printCss($('#css-code'), 'tabs');
  fetch('../../components/js/tabs.js', { cache: 'no-cache' }).then(function (r) { return r.text(); }).then(function (t) { $('#js-code').textContent = t; });
'''

C = dict(
    slug=SLUG, title='Tabs', eyebrow='Components · Navigation',
    lead='Tabs organise content across screens, data sets and interactions at the <strong>same level of hierarchy</strong>. A tab bar lets the user move between groups of related content without leaving the page. For content that must be read in order, use steps instead.',
    lead_ex='Every example on this page is the real component, not a picture. Specification: <code>.claude/skills/eco-tabs/SKILL.md</code>. Figma: ' + FIGS + '.',
    lead_spec='Tokens, sizes, measurements, states and requirements. Values come from the live token package and from Figma: ' + FIGS + '.',
    lead_code='How to add a tab bar to a page. The files are <code>components/css/tabs.css</code> and <code>components/js/tabs.js</code>.',
    css=[], style=STYLE, ex=ex, spec=spec, code=code, js_ex=JS_EX, js_spec=JS_SPEC, js_code=JS_CODE, select_menu=False)

if __name__ == '__main__':
    emit(C)
