from build import *

FIGMA = 'https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=1671-53188'
SLUG = 'tile-link'
PARENT = ('links-guide.html', 'Links guide')

STYLE = r'''    .pg-note { font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-tertiary); }
    .pg-row { display: flex; flex-wrap: wrap; align-items: center; gap: 16px 24px; }
    .pg-matrix td { vertical-align: middle; padding-top: 16px; padding-bottom: 16px; }
    .ds-callout__art { padding-right: 24px; }
    .tl-measure { display: block; }'''

KINDS = [('icon', 'Label + icon'), ('label', 'Label only'), ('brand', 'Brand')]

playground = '<h2 class="ds-h2">Playground</h2>' + desc('Choose content, size, placement and background. Brand tiles are Large only and ignore placement and label. Hover is forced here; the tile is live.') + \
    '<div class="ds-playground"><div class="ds-stage ds-stage--center" id="pg-stage"><div id="pg-host"></div></div><div class="ds-controls">' + \
    bp_field('pg-l-bp') + sel('pg-l-k', 'pg-kind', 'Content', 'kind', KINDS, 'icon') + btn_group('pg-l-size', 'Size', 'data-pg="size"', [('large', 'Large', True), ('small', 'Small', False)]) + \
    btn_group('pg-l-pl', 'Placement', 'data-pg="place"', [('vertical', 'Vertical', True), ('horizontal', 'Horizontal', False)]) + \
    btn_group('pg-l-bg', 'Background', 'data-pg="bg"', [('white', 'White', True), ('grey', 'Grey', False), ('black', 'Black', False)]) + \
    btn_group('pg-l-w', 'Label weight', 'data-pg="weight"', [('regular', 'Regular', True), ('medium', 'Medium', False), ('bold', 'Bold', False)]) + btn_group('pg-l-it', 'Label style', 'data-pg="italic"', [('no', 'Normal', True), ('yes', 'Italic', False)]) + \
    btn_group('pg-l-st', 'State', 'data-pg="state"', [('enabled', 'Enabled', True), ('hover', 'Hover', False)]) + \
    '<div class="ds-field form-field"><label class="form-label form-label--sm" for="pg-label">Label</label><div class="input-wrap"><div class="input-box input-box--sm"><input class="form-input" type="text" id="pg-label" value="Generator" placeholder="Label" /></div></div></div>' + \
    '</div></div><h3 class="ds-h3">Markup for this selection</h3>' + code_box('pg-code', 'HTML')

overview = '<h2 class="ds-h2">Overview</h2>' + desc('A tile link is a <strong>compact, tappable surface</strong> that takes the user to a destination: a brand page, a product category or a pre-filled search. It behaves as both a card and a button. Use it when links need a more graphic and more prominent presentation than a regular button gives, to highlight navigation destinations in grids and horizontal scrollers.') + \
    desc('It packages a single link target (an SVG or logo, an icon with a label, or a label alone) into one consistent tile shape, so groups of destinations can be laid out in scannable grids or carousels. One line: a clickable tile with a logo, an SVG, or an icon and a short label that links to a brand, a category or a search result page.') + \
    desc('Tile link has three kinds (Brand, Label + icon and Label only), two sizes (Large and Small), two placements (Vertical and Horizontal) and three backgrounds (White, Grey and Black; Black on the brand tile). The label has a weight (Regular, Medium or Bold) and an italic style. It is one of three link types: see the ' + link_large('links-guide.html', 'Links guide') + ' for how to choose.') + \
    three_pages(SLUG, 'a tile link', 'the values: tokens, sizes, measurements, states and requirements', 'how to add one to a page')

usage = '<h2 class="ds-h2">Usage</h2><h3 class="ds-h3 ds-group">When to use</h3>' + desc('Use a tile link to highlight navigation destinations in a grid or a horizontal scroller, when a text link or a button is not visual enough. Use it for:') + \
    bullets(['A group of brand logos that link to the brand pages', 'Product categories, as an icon with a short label', 'A pre-filled search or another shortcut, as a label with or without an icon']) + \
    '<h3 class="ds-h3 ds-group">When not to use</h3><h3 class="ds-h3">Not for the main call to action</h3>' + desc('A tile is a quiet card, not a button. The main call to action is a <code>eco-button</code>.') + \
    fig_pair('<div class="pg-row" id="fig-use-do"></div>', 'Do use tiles for a group of shortcuts.', '<div class="pg-row" id="fig-use-dont"></div>', 'Do not use a tile for the main call to action. Use a Button instead.') + \
    '<h3 class="ds-h3">Keep a group in one size</h3>' + desc('Tiles in a group have the same size and background, so they read as one set.') + \
    fig_pair('<div class="pg-row" id="fig-sz-do"></div>', 'Do use one size and one background in a group.', '<div class="pg-row" id="fig-sz-dont"></div>', 'Do not mix Large and Small tiles in one group.') + \
    '<h3 class="ds-h3">For links in body text</h3>' + desc('A link in a sentence is an ' + link_large('inline-link.html', 'Inline link') + ', and a standalone link with an arrow is an ' + link_large('action-link.html', 'Action link') + '.') + \
    '<h3 class="ds-h3 ds-group">Quick reference</h3>' + \
    table(['The link…', 'Use'], [['is a card or logo presented graphically', 'Tile link'], ['stands alone with an arrow', '<a class="inline-link inline-link--small" href="action-link.html">Action link</a>'], ['is inside a sentence', '<a class="inline-link inline-link--small" href="inline-link.html">Inline link</a>'], ['is the main call to action', '<code>eco-button</code>']]) + \
    rules(['Use tiles for a group of brands, categories or shortcuts.', 'Give a brand tile an <code>alt</code> with the brand name.', 'Use the white logo version on the Black tile.', 'Keep the group in one size and background.'],
          ['Use a tile as a replacement for a button.', 'Use tiles for links in body text.', 'Mix Large and Small in one group.', 'Add a border directly on the container: the border layer is part of the component.'])

anatomy = '<h2 class="ds-h2">Anatomy</h2><h3 class="ds-h3 ds-group">Tile link</h3>' + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout" id="tl-anat" role="img" aria-label="Anatomy of a tile link: 1 icon, 2 label, 3 border, 4 background"><div class="ds-callout__art" id="tl-anat-art"></div></div></figure></div>' + \
    ol_parts([('Icon', 'Optional. A Material Symbol, 24px (vertical) or 20px (horizontal).'), ('Label', '<code>body-md</code> (Large) or <code>body-sm</code> (Small), one line, centered.'), ('Border', '1px, in its own layer, so it never changes the size of the tile.'), ('Background', 'White, Grey or Black. The whole tile is one link.')]) + \
    desc('A brand tile has a logo instead of an icon and a label. It is Large only.')

variants = '<h2 class="ds-h2">Variants</h2>' + desc('Three kinds of tile in three backgrounds. Use the Breakpoint toggle to preview Desktop (769px and up) and Mobile (below 769px). Sizes are under Sizes below.') + \
    toolbar([('vb-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force')]) + \
    '<h3 class="ds-h3 ds-group">Label and icon</h3>' + desc('Vertical stacks the icon over the label; Horizontal puts them side by side.') + fig_one('<div class="pg-row" id="v-icon"></div>') + \
    '<h3 class="ds-h3 ds-group">Label only</h3>' + desc('The label alone, with the horizontal padding.') + fig_one('<div class="pg-row" id="v-label"></div>') + \
    '<h3 class="ds-h3 ds-group">Brand</h3>' + desc('A logo in a tile, Large only. 112px high on desktop, 80px on mobile.') + fig_one('<div class="pg-row" id="v-brand"></div>') + \
    '<h3 class="ds-h3 ds-group">Label weight and style</h3>' + desc('The label is Regular by default. <code>tile-link--weight-medium</code> (500), <code>tile-link--bold</code> (600) and <code>tile-link--italic</code> change the label only, not the icon. Use one weight and one style in a group.') + fig_one('<div class="pg-row" id="v-weights"></div>') + \
    '<h3 class="ds-h3 ds-group">Backgrounds</h3>' + desc('White is the default. Grey and Black give a group more weight. Use the white logo version on the Black tile.') + fig_one('<div class="pg-row" id="v-bg"></div>')

sizes = '<h2 class="ds-h2">Sizes</h2>' + desc('<strong>Large</strong> and <strong>Small</strong> for Label + icon and Label only; Brand is Large only. The padding changes at 769px. The values are under ' + sec_link(SLUG, 'sizes', 'Sizes') + ' in Specifications.') + \
    toolbar([('sz-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force')]) + fig_one('<div class="pg-row" id="v-sizes"></div>')

layout = '<h2 class="ds-h2">Layout &amp; Appearance</h2><h3 class="ds-h3 ds-group">Alignment</h3>' + desc('The content is centered in the tile, vertically and horizontally.') + \
    '<h3 class="ds-h3 ds-group">Placement</h3>' + desc('Vertical puts the icon above the label, Horizontal puts it beside it. A label-only tile is Horizontal. Put tiles of one group in a row or a grid with the same gap.') + \
    '<h3 class="ds-h3 ds-group">Width</h3>' + desc('As wide as the content plus the padding. Labels do not wrap (<code>white-space: nowrap</code>).') + \
    '<h3 class="ds-h3 ds-group">Appearance</h3>' + desc('A 1px border in <code>border-primary</code> on White and Grey, <code>border-action-1</code> on Black. Token names and values are under ' + sec_link(SLUG, 'design-tokens', 'Design Tokens') + ' in Specifications.')

behavior = '<h2 class="ds-h2">Behavior</h2><h3 class="ds-h3 ds-group">Hover</h3>' + desc('The border appears or darkens to <code>border-hover</code> (1px). On a Label + icon or Label only tile the label and the icon change to the action hover color. On a brand tile the logo is unchanged. The Black tile keeps its content and gets a 20% white overlay on <code>surface-action-1</code>.') + \
    '<h3 class="ds-h3 ds-group">Focus</h3>' + desc('A 2px ring shows on keyboard focus only (<code>body.keyboard-nav</code>).') + \
    '<h3 class="ds-h3 ds-group">Click and Enter</h3>' + desc('A click anywhere on the tile, or Enter, follows the link. All states are listed under ' + sec_link(SLUG, 'states', 'States') + ' in Specifications.')

access = '<h2 class="ds-h2">Accessibility</h2>' + desc('All requirements are listed under ' + sec_link(SLUG, 'accessibility-requirements', 'Accessibility Requirements') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Keyboard support</h3>' + desc('Tab moves between tiles. Enter follows the focused tile. The focus ring shows on keyboard focus.') + \
    '<h3 class="ds-h3 ds-group">Screen reader support</h3>' + desc('The whole tile is one <code>&lt;a href&gt;</code>. The icon is <code>aria-hidden</code>. A brand tile needs an <code>alt</code> on the logo with the brand name, because that is the link text.')

related = '<h2 class="ds-h2">Related</h2><ul class="ds-bullets"><li><strong>' + link_large('links-guide.html', 'Links guide') + '</strong>. How to choose a link type.</li><li><strong>' + link_large('inline-link.html', 'Inline link') + '</strong>. A link inside a sentence.</li><li><strong>' + link_large('action-link.html', 'Action link') + '</strong>. A standalone link with an arrow.</li><li><strong>' + link_large('button.html', 'Button') + '</strong>. The main call to action.</li></ul>'

references = '<h2 class="ds-h2">References</h2>' + refs([
    ('https://www.w3.org/WAI/WCAG22/Understanding/link-purpose-in-context.html', 'WCAG 2.2: Link Purpose (In Context)', 'Success criterion 2.4.4.'),
    ('https://www.w3.org/WAI/WCAG22/Understanding/non-text-content.html', 'WCAG 2.2: Non-text Content', 'Success criterion 1.1.1: the alt text of a logo.'),
    ('https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html', 'WCAG 2.2: Non-text Contrast', 'Success criterion 1.4.11: the border and the focus ring.'),
    ('https://carbondesignsystem.com/components/tile/usage/', 'Carbon Design System: Tile', 'IBM. Clickable tiles.'),
    ('https://m3.material.io/components/cards/overview', 'Material Design 3: Cards', 'Google.')])

ex = [('playground', playground), ('overview', overview), ('usage', usage), ('anatomy', anatomy), ('variants', variants), ('sizes', sizes), ('layout', layout), ('behavior', behavior), ('accessibility', access), ('related', related), ('references', references)]

# ---------------------------------------------------------------- Specifications
st_tok = '<h2 class="ds-h2">Design Tokens</h2>' + desc('Resolved from the live token package.') + \
    '<div class="ds-table-wrap"><table class="ds-table" id="tok-table"><thead><tr><th scope="col">Background · state</th><th scope="col">Part</th><th scope="col">Token</th><th scope="col">Value</th></tr></thead><tbody></tbody></table></div>' + \
    note('The border is a separate layer (<code>inset: 0</code>), so it never changes the tile size.')

st_sizes = '<h2 class="ds-h2">Sizes</h2><h3 class="ds-h3 ds-group">Label and icon, label only</h3>' + table(['Size · placement', 'Desktop padding', 'Desktop gap', 'Mobile padding', 'Mobile gap', 'Icon'], [
    ['Large · vertical', '10px 16px', '4px', '9px 16px', '4px', '24px'], ['Large · horizontal', '8px 16px', '8px', '9px 16px', '4px', '20px'], ['Small · vertical', '8px 16px', '4px', '6px 8px', '4px', '24px'], ['Small · horizontal', '6px 16px', '8px', '6px 8px', '4px', '20px']]) + \
    note('Label only uses the horizontal padding, without an icon. <code>sm</code> (640 to 768px) looks like mobile.') + \
    '<h3 class="ds-h3 ds-group">Brand</h3>' + table(['Breakpoint', 'Height', 'Horizontal padding', 'Logo height'], [['Desktop (769px+)', '112px', '48px', '48px'], ['Mobile and tablet', '80px', '32px', '24px']])

TILE_MEAS = ('<div class="measure__item"><span class="measure__name">%d · %s</span><div class="measure__obj"><a class="tile-link tile-link--%s tile-link--%s tile-link--white tl-measure" tabindex="-1" aria-label="%s"><div class="tile-link__inner measure__subject">%s</div></a>'
             '<i class="measure__pad measure__pad--t"></i><i class="measure__pad measure__pad--b"></i><i class="measure__pad measure__pad--l"></i><i class="measure__pad measure__pad--r"></i>'
             '<b class="measure__dim measure__dim--v measure__dim--t"><span></span></b><b class="measure__dim measure__dim--v measure__dim--b"><span></span></b><b class="measure__dim measure__dim--h measure__dim--l"><span></span></b><b class="measure__dim measure__dim--h measure__dim--r"><span></span></b></div></div>')


def mfig(n, name, size, place, icon=True):
    inner = ('<span class="tile-link__icon" aria-hidden="true">bolt</span>' if icon else '') + '<span class="tile-link__label">Generator</span>'
    return TILE_MEAS % (n, name, size, place, name, inner)


st_meas = '<h2 class="ds-h2">Measurements</h2><h3 class="ds-h3 ds-group">Dimensions</h3>' + desc('Padding of the tile at each size and placement. The shaded areas are the padding; the border is drawn in its own layer and does not change the size. The numbers are read from the component. A brand tile has a fixed height and only horizontal padding, so it is listed in the table.') + \
    toolbar([('mb-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force')]) + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-fig__stage--flush" style="padding:0;min-height:0"><div class="measure" role="img" aria-label="Padding of the tile link: per size and placement">' + mfig(1, 'Large vertical', 'large', 'vertical') + mfig(2, 'Large horizontal', 'large', 'horizontal') + mfig(3, 'Small vertical', 'small', 'vertical') + mfig(4, 'Small horizontal', 'small', 'horizontal') + '</div></div><figcaption class="ds-fig__cap">The tile at true size (1:1). Change the Breakpoint to see the mobile values.</figcaption></figure></div>' + \
    table(['Attribute', 'Value'], [['Padding', 'See the figure and Sizes: per size, placement and breakpoint'], ['Gap, icon to label', '4px, or 8px for Horizontal on desktop'], ['Border', '1px, in its own layer (<code>inset: 0</code>)'], ['Brand tile height', '112px desktop, 80px mobile'], ['Corners', 'Square'], ['Focus ring', '2px, 2px outside the tile']]) + \
    '<h3 class="ds-h3 ds-group">Spacing</h3>' + desc('The gap as a spacing token. The tile paddings (10, 9, 8 and 6px) have no spacing token.') + table(['Part', 'Value'], [['Gap, 4px', '<code>space-4</code>'], ['Gap, 8px', '<code>space-8</code>'], ['Padding, 16px', '<code>space-16</code>'], ['Focus ring offset', '2px']])

st_states = '<h2 class="ds-h2">States</h2>' + desc('Hover is forced on this page; in your code it comes from <code>:hover</code>.') + \
    '<h3 class="ds-h3 ds-group">Brand (SVG)</h3>' + bullets(['<strong>Enabled:</strong> a White container with a subtle border and the logo at full contrast; or a Black container with no visible border and the logo at full contrast.', '<strong>Hover, White:</strong> the border appears or darkens (<code>border-hover</code>, 1px). The logo is unchanged.', '<strong>Hover, Black:</strong> the surface is <code>surface-action-1</code> with <code>surface-opacity-white-20</code> on top. The logo is unchanged.']) + \
    '<h3 class="ds-h3 ds-group">Label + icon and Label only</h3>' + bullets(['<strong>Enabled:</strong> a White or Grey container with a subtle border and the content at full contrast.', '<strong>Hover:</strong> the border appears or darkens (<code>border-hover</code>, 1px), and the label and the icon shift to the action hover color.']) + \
    '<h3 class="ds-h3 ds-group">All states</h3>' + \
    toolbar([('sb-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force'), ('k-l', 'Kind', 'data-mx="kind"', [('icon', 'Label + icon', True), ('label', 'Label only', False), ('brand', 'Brand', False)])]) + \
    '<div class="ds-table-wrap"><table class="ds-table pg-matrix" id="matrix"><thead><tr><th scope="col">State</th><th scope="col">White</th><th scope="col">Grey</th><th scope="col">Black</th></tr></thead><tbody></tbody></table></div>'

st_typo = '<h2 class="ds-h2">Typography</h2><h3 class="ds-h3 ds-group">Size</h3>' + table(['Size', 'Type token', 'Desktop', 'Mobile'], [['Large', '<code>body-md</code>', '17/24, 0.32px', '16/22, 0.32px'], ['Small', '<code>body-sm</code>', '14/20, 0.36px', '14/20, 0.36px']]) + note('Breuer Condensed with <code>ss02</code>, <code>ss03</code> and <code>ss06</code>.') + \
    '<h3 class="ds-h3 ds-group">Weight and style</h3>' + table(['Modifier', 'Class', 'CSS'], [['Regular', '(none)', '<code>font-weight: 400</code>'], ['Medium', '<code>tile-link--weight-medium</code>', '<code>font-weight: 500</code>'], ['Bold', '<code>tile-link--bold</code>', '<code>font-weight: 600</code>'], ['Italic', '<code>tile-link--italic</code>', '<code>font-style: italic</code>']]) + \
    note('The modifiers change the label only. The font package ships 300, 400, 500 and 700, each with an italic face, so 600 renders with the 700 face.')

st_struct = '<h2 class="ds-h2">Structure</h2><h3 class="ds-h3 ds-group">Elements</h3>' + table(['Element', 'Class', 'Notes'], [
    ['Link', '<code>tile-link</code>', 'A real <code>&lt;a href&gt;</code>, <code>display: inline-flex</code>.'], ['Inner', '<code>tile-link__inner</code>', 'The tile. Holds the background, the padding and the border layer.'], ['Icon', '<code>tile-link__icon</code>', 'A Material Symbol, <code>aria-hidden</code>.'], ['Label', '<code>tile-link__label</code>', 'One line.'], ['Logo', '<code>img</code> in the inner element', 'Brand tiles only, with an <code>alt</code>.'],
    ['Modifiers', '<code>tile-link--large</code>, <code>--small</code>, <code>--vertical</code>, <code>--horizontal</code>, <code>--brand</code>, <code>--white</code>, <code>--grey</code>, <code>--black</code>', ''], ['Label weight, style', '<code>tile-link--weight-medium</code>, <code>--bold</code>, <code>--italic</code>', 'Change the label only.']]) + \
    '<h3 class="ds-h3 ds-group">Types</h3>' + table(['Type', 'Class', 'Use'], [['Label + icon', '<code>tile-link--large tile-link--vertical</code> (or horizontal, small)', 'An icon over or beside a label.'], ['Label only', '<code>tile-link--horizontal</code>', 'The label alone.'], ['Brand', '<code>tile-link--brand tile-link--large</code>', 'A logo. Large only.']]) + \
    '<h3 class="ds-h3 ds-group">Width</h3>' + desc('The tile is as wide as its content plus the padding.')

st_motion = '<h2 class="ds-h2">Motion</h2>' + table(['Property', 'Duration', 'Easing'], [['<code>border-color</code>', '<code>duration-fast-3</code>', '<code>ease-standard</code>']])

st_behavior = '<h2 class="ds-h2">Behavior</h2>' + table(['Input', 'Result'], [['Click anywhere on the tile', 'Follows the link.'], ['Enter, Tab', 'Follows the link; 2px focus ring on keyboard focus.'], ['Hover', 'The border darkens. A Label + icon or Label only tile also changes the color of the label and the icon; a brand logo is unchanged. The Black tile gets a 20% white overlay.'], ['Markup', 'The whole tile is one <code>&lt;a href&gt;</code>. Brand tiles need an <code>alt</code> with the brand name.']])

st_access = '<h2 class="ds-h2">Accessibility Requirements</h2>' + table(['Topic', 'Requirement'], [
    ['Element', 'One <code>&lt;a href&gt;</code> for the whole tile. Links navigate; buttons act.'], ['Name', 'The label is the link text. On a brand tile the <code>alt</code> of the logo is the link text (WCAG 1.1.1, 2.4.4).'], ['Focus', 'A 2px ring with <code>border-focus</code> and 2px offset, on keyboard focus (WCAG 2.4.7, 1.4.11).'],
    ['Contrast', 'The border and text meet the contrast requirements on White, Grey and Black. Use the white logo version on the Black tile.']])

spec = [('design-tokens', st_tok), ('sizes', st_sizes), ('measurements', st_meas), ('states', st_states), ('typography', st_typo), ('structure', st_struct), ('motion', st_motion), ('behavior', st_behavior), ('accessibility-requirements', st_access)]

# ---------------------------------------------------------------- Code
c_basic = '<h2 class="ds-h2">Basic Usage</h2>' + desc('Link the shared stylesheet once per page. Never copy the rules into a page.') + table(['Step', 'What to do'], [
    ['1. Link', '<code>&lt;link rel="stylesheet" href="/components/css/tile-link.css"&gt;</code>. The page needs the Material Symbols Outlined font.'], ['2. Markup', 'An <code>&lt;a href&gt;</code> with <code>tile-link</code>, a size, a placement and a background, around a <code>div.tile-link__inner</code>.'],
    ['3. Content', 'An icon and a label, a label alone, or a logo <code>img</code> with an <code>alt</code> (brand).'], ['4. Group', 'Use one size and one background for tiles in a group.']])
c_tl = '<h2 class="ds-h2">Tile link</h2>' + desc('Copy the markup you need. Hover comes from <code>:hover</code>; the <code>[data-state]</code> selectors in the CSS exist only so the documentation can force a state.') + '<div id="recipes"></div>'
c_api = '<h2 class="ds-h2">API</h2><h3 class="ds-h3 ds-group">Classes</h3>' + table(['Class', 'Use'], [['<code>tile-link</code>', 'The link.'], ['<code>tile-link--large</code>, <code>--small</code>', 'Size.'], ['<code>tile-link--vertical</code>, <code>--horizontal</code>', 'Placement of the icon.'], ['<code>tile-link--white</code>, <code>--grey</code>, <code>--black</code>', 'Background.'], ['<code>tile-link--brand</code>', 'A logo tile. Large only.'], ['<code>tile-link--weight-medium</code>, <code>--bold</code>, <code>--italic</code>', 'Label weight and style.'], ['<code>tile-link__inner</code>, <code>__icon</code>, <code>__label</code>', 'Parts.']]) + \
    '<h3 class="ds-h3 ds-group">Things to know</h3>' + bullets(['Breakpoint: the padding, the gap and the brand height change at 769px. The CSS does this by itself.', 'White is the default background when no color class is given; add one anyway for clarity.', 'The border is its own layer: do not add a border to the container.', 'The focus ring needs <code>body.keyboard-nav</code>, which the templates set on the first Tab press.', 'The <code>[data-state]</code> selectors do nothing outside the documentation pages.'])
c_css = '<h2 class="ds-h2">CSS / Tailwind</h2>' + desc('The component is one CSS file, shared by every page. Link it, never copy it. The CSS below is read from the file the page links, so it is always what you see.') + code_box('css-code', 'CSS (components/css/tile-link.css)')
code = [('basic-usage', c_basic), ('tile-link', c_tl), ('api', c_api), ('css-tailwind', c_css, False)]

# ---------------------------------------------------------------- scripts
TL_JS = r'''
  var WT = { regular: '', medium: ' tile-link--weight-medium', bold: ' tile-link--bold' };
  function cls(o) { return 'tile-link ' + (o.kind === 'brand' ? 'tile-link--brand tile-link--large' : 'tile-link--' + o.size + ' tile-link--' + (o.kind === 'label' ? 'horizontal' : o.place)) + ' tile-link--' + o.bg + (o.kind === 'brand' ? '' : WT[o.weight || 'regular'] + (o.italic ? ' tile-link--italic' : '')); }
  function tile(o) {
    var a = document.createElement('a'); a.href = '#'; a.className = cls(o); if (o.state === 'hover') a.dataset.state = 'hover';
    a.addEventListener('click', function (e) { e.preventDefault(); });
    var inner = document.createElement('div'); inner.className = 'tile-link__inner';
    if (o.kind === 'brand') { var im = document.createElement('img'); im.src = '../../images/' + (o.bg === 'black' ? 'bjornklader-logo-white.svg' : 'bjornklader-logo.svg'); im.alt = 'Björnkläder'; inner.appendChild(im); }
    else {
      if (o.kind === 'icon') { var ic = document.createElement('span'); ic.className = 'tile-link__icon'; ic.setAttribute('aria-hidden', 'true'); ic.textContent = o.icon || 'bolt'; inner.appendChild(ic); }
      var l = document.createElement('span'); l.className = 'tile-link__label'; l.textContent = o.label; inner.appendChild(l);
    }
    a.appendChild(inner); return a;
  }
'''

JS_EX = TL_JS + r'''
  var st = { kind: 'icon', size: 'large', place: 'vertical', bg: 'white', state: 'enabled', weight: 'regular', italic: 'no' };
  function markup(o) {
    var body = o.kind === 'brand' ? '    <img src="/images/' + (o.bg === 'black' ? 'bjornklader-logo-white.svg' : 'bjornklader-logo.svg') + '" alt="Björnkläder" />'
      : (o.kind === 'icon' ? '    <span class="tile-link__icon" aria-hidden="true">bolt</span>\n' : '') + '    <span class="tile-link__label">' + esc(o.label) + '</span>';
    return '<a href="#" class="' + cls(o) + '">\n  <div class="tile-link__inner">\n' + body + '\n  </div>\n</a>';
  }
  function renderPg() {
    var o = { kind: st.kind, size: st.size, place: st.place, bg: st.bg, state: st.state, weight: st.weight, italic: st.italic === 'yes', label: $('#pg-label').value };
    clear($('#pg-host')).appendChild(tile(o));
    var h = markup(o); if (o.state === 'hover') h = '<!-- hover is forced here for preview; in production it comes from :hover -->\n' + h;
    $('#pg-code').textContent = h;
  }
  DK.wire(st, renderPg); $('#pg-label').addEventListener('input', renderPg);
  DK.bp();

  var vi = clear($('#v-icon'));
  [['large', 'vertical', 'Large vertical'], ['large', 'horizontal', 'Large horizontal'], ['small', 'vertical', 'Small vertical'], ['small', 'horizontal', 'Small horizontal']].forEach(function (z) { vi.appendChild(tile({ kind: 'icon', size: z[0], place: z[1], bg: 'white', label: z[2] })); });
  var vl = clear($('#v-label')); [['large', 'Large'], ['small', 'Small']].forEach(function (z) { vl.appendChild(tile({ kind: 'label', size: z[0], bg: 'white', label: z[1] + ' label only' })); });
  var vb = clear($('#v-brand')); ['white', 'grey', 'black'].forEach(function (b) { vb.appendChild(tile({ kind: 'brand', bg: b })); });
  var vw = clear($('#v-weights')); [['regular', false, 'Regular'], ['medium', false, 'Medium'], ['bold', false, 'Bold'], ['regular', true, 'Italic'], ['bold', true, 'Bold italic']].forEach(function (z) { vw.appendChild(tile({ kind: 'icon', size: 'large', place: 'vertical', bg: 'white', weight: z[0], italic: z[1], label: z[2] })); });
  var vg = clear($('#v-bg')); ['white', 'grey', 'black'].forEach(function (b) { vg.appendChild(tile({ kind: 'icon', size: 'large', place: 'vertical', bg: b, label: b.charAt(0).toUpperCase() + b.slice(1) })); });
  var vs = clear($('#v-sizes')); [['large', 'vertical', 'Large'], ['small', 'vertical', 'Small'], ['large', 'horizontal', 'Large'], ['small', 'horizontal', 'Small']].forEach(function (z) { vs.appendChild(tile({ kind: 'icon', size: z[0], place: z[1], bg: 'white', label: z[2] })); });

  /* Usage figures */
  function group(host, list) { var h = clear($(host)); list.forEach(function (t) { h.appendChild(tile({ kind: 'icon', size: t[3] || 'large', place: 'vertical', bg: 'white', label: t[0], icon: t[1] })); }); }
  group('#fig-use-do', [['Work wear', 'checkroom'], ['Tools', 'construction']]);
  var dd = clear($('#fig-use-dont')); dd.appendChild(tile({ kind: 'label', size: 'large', bg: 'black', label: 'Add to cart' }));
  group('#fig-sz-do', [['Work wear', 'checkroom'], ['Tools', 'construction']]);
  group('#fig-sz-dont', [['Work wear', 'checkroom', null, 'large'], ['Tools', 'construction', null, 'small']]);

  /* Anatomy */
  var at = tile({ kind: 'icon', size: 'large', place: 'vertical', bg: 'white', label: 'Generator' }); clear($('#tl-anat-art')).appendChild(at);
  function rng(el) { return function () { var r = document.createRange(); r.selectNodeContents(el); return r.getBoundingClientRect(); }; }
  DK.callouts($('#tl-anat'), [
    { n: 1, el: $('.tile-link__icon', at), side: 'left', len: 72, at: 'edge' },
    { n: 2, side: 'bottom', len: 48, box: rng($('.tile-link__label', at)), at: 'edge' },
    { n: 3, el: at, side: 'right', len: 48, at: 'edge' },
    { n: 4, side: 'top', len: 40, at: 'center', box: function () { var r = $('.tile-link__inner', at).getBoundingClientRect(); return { left: r.left + 6, top: r.top + 6, width: 1, height: 1 }; } }
  ]);
  renderPg();
'''

JS_SPEC = TL_JS + r'''
  var mx = { kind: 'icon' };
  function buildMatrix() {
    var tb = clear($('#matrix tbody'));
    [['Enabled', 'enabled'], ['Hover', 'hover']].forEach(function (r) {
      var tr = document.createElement('tr'), th = document.createElement('th'); th.scope = 'row'; th.textContent = r[0]; tr.appendChild(th);
      ['white', 'grey', 'black'].forEach(function (b) { var td = document.createElement('td'); td.appendChild(tile({ kind: mx.kind, size: 'large', place: 'vertical', bg: b, state: r[1], label: 'Generator' })); tr.appendChild(td); });
      tb.appendChild(tr);
    });
  }
  DK.seg($('[data-mx="kind"]'), function (v) { mx.kind = v; buildMatrix(); });
  DK.bp(function () { buildMatrix(); if (window.ECO_MEASURE) ECO_MEASURE.init(); });
  buildMatrix();
  DK.tokenTable($('#tok-table tbody'), [
    ['White', 'Background', 'surface-raised-primary'], ['Grey', 'Background', 'surface-05'], ['Black', 'Background', 'surface-100'],
    ['White, Grey · enabled', 'Border', 'border-primary'], ['White, Grey · hover', 'Border', 'border-hover'], ['Black · enabled, hover', 'Border', 'border-action-1'],
    ['White, Grey · enabled', 'Label and icon', 'text-primary'], ['White, Grey · hover', 'Label and icon', 'text-action-primary-hover'], ['Black · all', 'Label and icon', 'text-primary-inverted'],
    ['Black · hover', 'Overlay', 'surface-opacity-white-20'], ['Keyboard focus', 'Ring', 'border-focus']]);
'''

JS_CODE = r'''
  DK.recipes($('#recipes'), [
    ['Label and icon, Large, vertical', '<a href="/generators" class="tile-link tile-link--large tile-link--vertical tile-link--white">\n  <div class="tile-link__inner">\n    <span class="tile-link__icon" aria-hidden="true">bolt</span>\n    <span class="tile-link__label">Generator</span>\n  </div>\n</a>'],
    ['Label and icon, Small, horizontal, grey', '<a href="/search" class="tile-link tile-link--small tile-link--horizontal tile-link--grey">\n  <div class="tile-link__inner">\n    <span class="tile-link__icon" aria-hidden="true">search</span>\n    <span class="tile-link__label">Search</span>\n  </div>\n</a>'],
    ['Label only', '<a href="/generators" class="tile-link tile-link--large tile-link--horizontal tile-link--white">\n  <div class="tile-link__inner">\n    <span class="tile-link__label">Generator</span>\n  </div>\n</a>'],
    ['Bold italic label', '<a href="/generators" class="tile-link tile-link--large tile-link--horizontal tile-link--white tile-link--bold tile-link--italic">\n  <div class="tile-link__inner">\n    <span class="tile-link__label">Generator</span>\n  </div>\n</a>'],
    ['Brand, black', '<a href="/brands/bjornklader" class="tile-link tile-link--brand tile-link--large tile-link--black">\n  <div class="tile-link__inner">\n    <img src="/images/bjornklader-logo-white.svg" alt="Björnkläder" />\n  </div>\n</a>']
  ]);
  DK.printCss($('#css-code'), 'tile-link', [[/:is\(:hover, \[data-state="hover"\]\)/g, ':hover']]);
'''

C = dict(
    slug=SLUG, title='Tile link', parent=PARENT, eyebrow='Components · Links',
    lead='A tile link is a clickable, <strong>graphical link</strong> with an SVG graphic or an icon with a label. It highlights navigation destinations in grids and horizontal scrollers.',
    lead_ex='Every example on this page is the real component, not a picture. Specification: <code>.claude/skills/eco-tile-link/SKILL.md</code>. Figma: ' + fig_link(FIGMA, 'Tile link') + '.',
    lead_spec='Tokens, sizes, measurements, states and requirements. Values come from the live token package and from Figma: ' + fig_link(FIGMA, 'Tile link') + '.',
    lead_code='How to add a tile link to a page. The file is <code>components/css/tile-link.css</code>.',
    select_menu=True,
    css=['tile-link'], style=STYLE, ex=ex, spec=spec, code=code, js_ex=JS_EX, js_spec=JS_SPEC, js_code=JS_CODE)

if __name__ == '__main__':
    emit(C)
