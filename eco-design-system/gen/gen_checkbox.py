import re
from build import *

FIGMA = 'https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=1548-53635'
FIGMA_TILE = 'https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=14460-597851'

STYLE = r'''    .pg-note { font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-tertiary); }
    .ds-stage--dark .pg-note { color: var(--color-text-tertiary-inverted); }
    .pg-matrix td { vertical-align: middle; padding-top: 16px; padding-bottom: 16px; }
    .cb-pdp { display: flex; flex-direction: column; gap: 8px; padding: 24px; background: var(--color-surface-raised-secondary); }
    .cb-pdp__label { font-family: 'Breuer Condensed', sans-serif; font-size: 16px; font-weight: 600; line-height: 16px; letter-spacing: 0.48px; text-transform: uppercase; color: var(--color-text-primary); }
    .cb-pdp__name { font-family: 'Breuer Condensed', sans-serif; font-size: 16px; line-height: 22px; letter-spacing: 0.32px; color: var(--color-text-primary); margin-bottom: 4px; }
    .cb-filter { max-width: 420px; background: var(--color-surface-raised-primary); }
    .cb-filter__head { display: flex; align-items: center; justify-content: space-between; padding: 8px 0 16px; }
    .cb-filter__title { font-family: 'Breuer Condensed', sans-serif; font-size: 20px; font-weight: 600; line-height: 24px; color: var(--color-text-primary); } /* title-md */
    .cb-filter__chev { font-family: 'Material Symbols Outlined'; font-size: 24px; line-height: 1; font-variation-settings: 'FILL' 0, 'wght' 300, 'GRAD' 0, 'opsz' 24; }
    .cb-filter__more { display: inline-block; margin: 8px 0 24px; padding: 0; border: 0; background: none; cursor: pointer; font-family: 'Breuer Condensed', sans-serif; font-size: 16px; font-weight: 600; line-height: 22px; color: var(--color-text-primary); }
    .cb-filter__more:focus-visible { outline: 2px solid var(--color-border-focus); outline-offset: 2px; }
    .cb-filter__rule { border: 0; border-top: 1px solid var(--color-border-primary); margin: 0; }
    .cb-colorlist { display: grid; gap: 0 32px; grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); width: 100%; }
    .cb-colorlist > div { display: flex; align-items: center; gap: 8px; padding: 5px 0; border-bottom: 1px solid var(--color-border-primary); }
    .cb-colorlist__label { flex: 0 0 92.58px;  /* 92.58px: fixed label column, as in Figma */ font-family: 'Breuer Condensed', sans-serif; font-feature-settings: 'ss02' 1, 'ss03' 1; font-size: 16px; font-weight: 500; line-height: 16px; letter-spacing: 0.32px; text-transform: uppercase; color: var(--color-text-tertiary); } /* alt-label-lg: 16/16 mobile, 18/18 desktop */
    .cb-colorlist__swatch { width: 16px; height: 16px; background: var(--swatch); flex-shrink: 0; }
    @media (min-width: 769px) { .cb-colorlist__label { font-size: 18px; line-height: 18px; letter-spacing: 0.36px; } }
    .cb-tiles { display: flex; flex-wrap: wrap; gap: 8px; }
    .cb-row { display: flex; flex-wrap: wrap; gap: 12px 24px; align-items: center; }
    .cb-col { display: flex; flex-direction: column; gap: 4px; }
    .cb-group { border: 0; margin: 0; padding: 0; display: flex; flex-direction: column; gap: 0; }
    .cb-group legend { font-size: 16px; line-height: 18px; font-weight: 600; margin-bottom: var(--dimension-spacing-space-8); padding: 0; }   /* title-sm */
    .cb-group--wrap { flex-direction: row; flex-wrap: wrap; gap: 4px 24px; }
    .cb-group--wrap legend { width: 100%; }
    .cb-indent { margin-left: 24px; display: flex; flex-direction: column; }
    .cb-state { font-size: 14px; line-height: 20px; letter-spacing: 0.36px; margin-top: 12px; color: var(--color-text-tertiary); }
    .ds-stage--dark .cb-state { color: var(--color-text-tertiary-inverted); }
    .cb-table td, .cb-table th { text-align: center; }
    .cb-table .check-icon input { display: block; margin: 4px auto; } /* 24px area, so the row stays 48px */
    .cb-table td:first-child, .cb-table th:first-child { text-align: left; }
    .cb-fig { display: flex; flex-direction: column; gap: 4px; width: 100%; max-width: 320px; }
    .ds-callout__art { padding-right: 72px; }   /* room for marker 4 to the right of the label */
    .cb-measure { display: inline-flex; }
    .cb-sizes { display: flex; flex-wrap: wrap; align-items: flex-start; gap: 12px 48px; }
    .ds-table-wrap.ds-stage--dark { padding: 0; background: var(--color-surface-100); }
    .ds-stage--dark .ds-table, .ds-stage--dark .ds-table th, .ds-stage--dark .ds-table td { color: var(--color-text-primary-inverted); border-color: var(--color-surface-60); }
    .ds-stage--dark .ds-table thead th { background: transparent; }'''

# ------------------------------------------------------------------------------ Examples & Guidelines
playground = '''<h2 class="ds-h2">Playground</h2><p class="ds-desc">Choose a mode, value and state and the checkbox and its code update. Light mode is the default. Use dark mode only on a dark surface (<code>surface-100</code> or <code>surface-80</code>). The checkbox in the stage is live: click it to change its value.</p><div class="ds-playground"><div class="ds-stage ds-stage--center" id="pg-stage"><div id="pg-host"></div></div><div class="ds-controls">''' + \
    btn_group('pg-l-mode', 'Mode', 'data-pg="mode"', [('light', 'Light', True), ('dark', 'Dark', False)]) + \
    bp_field('pg-l-bp') + \
    btn_group('pg-l-size', 'Size', 'data-pg="size"', [('large', 'Large', True), ('small', 'Small', False)]) + \
    btn_group('pg-l-type', 'Type', 'data-pg="type"', [('standard', 'Standard', True), ('menu', 'Inline menu', False)]) + \
    btn_group('pg-l-val', 'Value', 'data-pg="value"', [('unchecked', 'Unchecked', True), ('checked', 'Checked', False), ('indeterminate', 'Mixed', False)]) + \
    btn_group('pg-l-st', 'State', 'data-pg="state"', [('enabled', 'Enabled', True), ('hover', 'Hover', False), ('focus', 'Focus', False), ('disabled', 'Disabled', False)]) + \
    '''<div class="ds-field form-field"><label class="form-label form-label--sm" for="pg-label">Label (standard only)</label><div class="input-wrap"><div class="input-box input-box--sm"><input class="form-input" type="text" id="pg-label" value="Label" placeholder="Label" /></div></div></div><p class="pg-note" id="pg-status" aria-live="polite" style="margin:0"></p></div></div><h3 class="ds-h3">Markup for this selection</h3>''' + \
    code_box('pg-code', 'HTML')

overview = '''<h2 class="ds-h2">Overview</h2><p class="ds-desc">A checkbox lets the user turn one or more options on or off, independently of each other. The choice is saved when the form is submitted.</p><p class="ds-desc">Checkbox has two sizes (Large, Small), a light and a dark mode, an Inline menu type for table headers, a read-only check icon for tables, and tiles (color swatch, image, number) for product pages and filtering.</p><p class="ds-desc">This documentation has three pages. <strong>Examples &amp; Guidelines</strong> (this page) shows when and how to use a checkbox. ''' + \
    link_large('checkbox-specifications.html', 'Specifications') + ''' holds the values: tokens, sizes, measurements, states and requirements. ''' + link_large('checkbox-code.html', 'Code') + ''' shows how to add a checkbox to a page.</p>'''

EXTRA = (fig_pair('<div class="cb-fig"><div class="cb-group"><label class="form-checkbox-item"><input type="checkbox" checked /><span>Send me product news</span></label></div><button type="button" class="btn btn--primary btn--sm" style="align-self:flex-start;margin-top:12px"><span class="btn__label">Save</span></button></div>', 'Do use a checkbox when the choice is saved on submit.',
           '<div class="cb-fig"><div class="cb-group"><label class="form-checkbox-item"><input type="checkbox" checked /><span>Email notifications</span></label><label class="form-checkbox-item"><input type="checkbox" /><span>SMS notifications</span></label></div></div>', 'Do not use checkboxes for settings that apply at once. Use a switch instead.') +
  '<h3 class="ds-h3">Groups need a legend</h3><p class="ds-desc">Related checkboxes go in a <code>fieldset</code> with a <code>legend</code>, so a screen reader reads the question with each option.</p>' +
  fig_pair('<div class="cb-fig"><fieldset class="form-radio-group"><legend>Delivery options</legend><label class="form-checkbox-item"><input type="checkbox" checked /><span>Leave at door</span></label><label class="form-checkbox-item"><input type="checkbox" /><span>Text me on arrival</span></label><label class="form-checkbox-item"><input type="checkbox" /><span>Signature required</span></label></fieldset></div>', 'Do group related checkboxes in a fieldset with a legend.',
           '<div class="cb-fig"><div class="cb-group"><label class="form-checkbox-item"><input type="checkbox" checked /><span>Leave at door</span></label><label class="form-checkbox-item"><input type="checkbox" /><span>Text me on arrival</span></label><label class="form-checkbox-item"><input type="checkbox" /><span>Signature required</span></label></div></div>', 'Do not leave a group without a legend.') +
  '<h3 class="ds-h3">Mixed is for a select-all parent</h3><p class="ds-desc">The mixed state says that some, but not all, of the children are selected. A checkbox with no children is either checked or not.</p>' +
  fig_pair('<div class="cb-fig" id="fig-mix-do"></div>', 'Do use the mixed state on a select-all parent.', '<div class="cb-fig" id="fig-mix-dont"></div>', 'Do not use the mixed state on a single checkbox.'))

usage = '''<h2 class="ds-h2">Usage</h2><h3 class="ds-h3 ds-group">When to use</h3><p class="ds-desc">Use a checkbox when the user picks any number of options, or confirms one option, and the choice is saved when the form is submitted. Use it to:</p><ul class="ds-bullets"><li>Choose any number of options from a list</li><li>Select all or some items with a parent checkbox that shows the mixed state</li><li>Select rows in a table, with the Inline menu type in the table header</li><li>Show whether a role has a permission, with the read-only check icon in a table</li><li>Choose colors or pictures in a filter or on a product page, with a tile</li></ul><h3 class="ds-h3 ds-group">When not to use</h3><h3 class="ds-h3">Checkbox or radio button</h3><p class="ds-desc">Checkbox, radio and switch look alike but do different jobs. Use checkboxes when several options can be chosen. When exactly one of two or more options can be chosen, use <code>eco-radio</code>.</p><div class="ds-figs"><figure class="ds-fig ds-fig--do"><div class="ds-fig__stage"><div class="cb-fig"><fieldset class="form-radio-group"><legend>Show columns</legend><label class="form-checkbox-item"><input type="checkbox" checked /><span>Name</span></label><label class="form-checkbox-item"><input type="checkbox" checked /><span>Email</span></label><label class="form-checkbox-item"><input type="checkbox" /><span>Role</span></label></fieldset></div></div><figcaption class="ds-fig__cap"><span class="ds-fig__ic" aria-hidden="true">check_circle</span>Do use checkboxes when several options can be chosen.</figcaption></figure><figure class="ds-fig ds-fig--dont"><div class="ds-fig__stage"><div class="cb-fig"><fieldset class="form-radio-group"><legend>Show columns</legend><label class="form-radio-item"><input type="radio" name="fig-dont" checked /><span>Name</span></label><label class="form-radio-item"><input type="radio" name="fig-dont" /><span>Email</span></label><label class="form-radio-item"><input type="radio" name="fig-dont" /><span>Role</span></label></fieldset></div></div><figcaption class="ds-fig__cap"><span class="ds-fig__ic" aria-hidden="true">cancel</span>Do not use radio buttons for multi-select. Use checkboxes instead.</figcaption></figure></div><h3 class="ds-h3">For a setting that applies at once</h3><p class="ds-desc">A checkbox is saved when the form is submitted. For a setting that turns on or off with immediate effect, use <code>eco-switch</code>.</p>''' + EXTRA + '''<h3 class="ds-h3 ds-group">Quick reference</h3>''' + \
    table(['The user…', 'Use'], [['picks any number of options, saved on submit', 'Checkbox'], ['picks exactly one of two or more options', '<code>eco-radio</code>'], ['turns a setting on or off, with immediate effect', '<code>eco-switch</code>']]) + \
    rules(['Write labels that make sense when checked, in sentence case.', 'Group related checkboxes in a <code>fieldset</code> with a <code>legend</code>.', 'Use <code>.form-checkbox-item--dark</code> on dark surfaces.', 'Use the mixed state only for a “select all” parent.'],
          ['Use a checkbox for a choice between options. Use radio.', 'Use a checkbox for an on/off setting that applies at once. Use switch.', 'Put the light markup on a dark surface, or the dark markup on a light one.', 'Build the box from an image or SVG file, or hardcode its colors.'])

anatomy = '''<h2 class="ds-h2">Anatomy</h2><h3 class="ds-h3 ds-group">Checkbox</h3><div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout" id="cb-anat" role="img" aria-label="Anatomy of a checkbox: 1 area, 2 box, 3 checkmark, 4 label"><div class="ds-callout__art"><label class="form-checkbox-item"><input type="checkbox" id="an-in" checked tabindex="-1" /><span id="an-lbl">Label</span></label></div></div></figure></div><ol class="ds-bullets ds-bullets--num"><li><strong>Area.</strong> 24×24px: the box plus a 4px margin. The margin leaves exactly room for the focus ring (2px gap plus 2px line), so focusing never shifts the layout.</li><li><strong>Box.</strong> 16×16px with a 1px border. In dark mode the border is 2px on hover.</li><li><strong>Checkmark.</strong> White, drawn as an SVG background. Mixed shows a dash instead. Never an image file.</li><li><strong>Label.</strong> Breuer Condensed, <code>body-md</code>. 8px from the box. A checkbox without a label needs an <code>aria-label</code>.</li></ol><h3 class="ds-h3 ds-group">Inline menu</h3><p class="ds-desc">The box followed by a 24×24px dropdown arrow, with no label. Dimensions are under <a class="inline-link inline-link--large inline-link--secondary" href="checkbox-specifications.html#sizes">Sizes</a> in Specifications.</p><h3 class="ds-h3 ds-group">Tile</h3><div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout" id="tile-anat" role="img" aria-label="Anatomy of an image tile: 1 frame, 2 image"><div class="ds-callout__art"><label class="form-checkbox-tile form-checkbox-tile--image"><input type="checkbox" aria-label="Yellow / black" tabindex="-1" /><span class="form-checkbox-tile__box" id="tn-box"><img id="tn-img" src="/images/product-skaljacka-gul-svart.webp" alt="" /></span></label></div></div></figure></div><ol class="ds-bullets ds-bullets--num"><li><strong>Frame.</strong> The tile box, 48×48px (40×40px on mobile). A 1px border; selected is a 2px frame.</li><li><strong>Content.</strong> A picture 6px from the edge (image tile), a 16px swatch of the product color (color swatch) or the text “+10” (number tile).</li></ol>'''

variants = '''<h2 class="ds-h2">Variants</h2><p class="ds-desc">Two modes (light, dark) and two types (standard, inline menu), plus the read-only check icon for tables. Choose the mode to see every variant on a light or a dark surface. Tiles have their own section below. Figma also has a Breakpoint property, which only changes the Large label size: use the Breakpoint toggle to preview it.</p>''' + \
    toolbar([('vm-l', 'Mode', 'data-mode-toggle', [('light', 'Light', True), ('dark', 'Dark', False)]), ('vb-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force')]) + \
    '''<h3 class="ds-h3 ds-group">With label, without label</h3><p class="ds-desc">A visible label is the default. A checkbox without a label needs an <code>aria-label</code>, and is only for dense cases such as table rows.</p><div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage" data-mode-stage><div class="cb-row" id="v-single"></div></div></figure></div><h3 class="ds-h3 ds-group">Select all (mixed)</h3><p class="ds-desc">A parent checkbox shows the mixed state when only some children are selected. Click the parent to select or clear all. This is the only case where the mixed state is used.</p><div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage" data-mode-stage><div class="cb-col" id="v-parent"></div><p class="cb-state" id="v-parent-out" aria-live="polite"></p></div></figure></div><h3 class="ds-h3 ds-group">Inline menu</h3><p class="ds-desc">A checkbox with a dropdown arrow, for example a table header where the checkbox selects all rows and the arrow opens a menu (class <code>.form-checkbox-item--menu</code> markup below). It has no label, so it needs an <code>aria-label</code>. States: enabled, hover, focus and disabled, each unchecked, checked or mixed. The menu itself is not part of this component.</p><div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage" data-mode-stage><div class="cb-row" id="v-menu"></div></div></figure></div><h3 class="ds-h3 ds-group">Check icon in a table</h3><p class="ds-desc">Read-only, to show whether a role has a permission. Always disabled, light mode only (class <code>.check-icon</code> on the cell).</p>''' + \
    '''<div class="ds-table-wrap"><table class="ds-table cb-table"><thead><tr><th scope="col">Permission</th><th scope="col">Standard</th><th scope="col">Administrator</th></tr></thead><tbody><tr><th scope="row">View orders</th><td class="check-icon"><input type="checkbox" checked disabled aria-label="Standard: yes" /></td><td class="check-icon"><input type="checkbox" checked disabled aria-label="Administrator: yes" /></td></tr><tr><th scope="row">Manage users</th><td class="check-icon"><input type="checkbox" disabled aria-label="Standard: no" /></td><td class="check-icon"><input type="checkbox" checked disabled aria-label="Administrator: yes" /></td></tr></tbody></table></div>'''

tiles = '''<h2 class="ds-h2">Tiles</h2><p class="ds-desc">Checkbox tiles are used first and foremost on product pages (PDP) and in filtering, where the choice is a picture or a color instead of a text label. They are native checkboxes, so several can be chosen. Three kinds: <strong>Color swatch</strong>, <strong>Image</strong> and <strong>Number</strong> (the “+10” tile that shows how many more there are). They have no label, so each needs an <code>aria-label</code>. Figma: ''' + \
    '<a class="inline-link inline-link--large inline-link--secondary" href="%s" target="_blank" rel="noopener">Color swatch</a> and <a class="inline-link inline-link--large inline-link--secondary" href="%s" target="_blank" rel="noopener">Image and Number</a>.</p>' % ('https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=4650-209393', FIGMA_TILE) + \
    toolbar([('tb-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force')]) + \
    '''<h3 class="ds-h3 ds-group">Color swatch in a filter list</h3><p class="ds-desc">A 24×24px tile with a 16px square of the product color. The same size on desktop and mobile. The color is the product’s own, set with the <code>--swatch</code> variable. In filtering several colors can be chosen, so these are checkboxes.</p><div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage"><div class="cb-filter" id="t-filter"></div></div></figure></div><p class="ds-desc">The same tiles as a compact grid, all 26 product colors:</p><div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage"><fieldset class="cb-group" id="t-color"></fieldset></div></figure></div><p class="ds-desc">The swatch shows the product color, including the glossy gradients and finishes (gold, mirror lens, semi shiny, transparent, pattern). The library below has all 26 product colors from Figma, each with its name in <code>alt-label-lg</code> style (Medium, uppercase, <code>text-tertiary</code>) and a 16px swatch. In the real filter the hex value comes from the product data.</p><div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage"><div class="cb-colorlist" id="t-colorlist" role="list"></div></div></figure></div><h3 class="ds-h3 ds-group">Image on a product page</h3><p class="ds-desc">The product picture inside a 48px tile (40px on mobile), with 6px around the image. On a product page (PDP) only <strong>one</strong> can be chosen at a time, so the tiles are <code>radio</code> inputs with the same tile styling (use checkboxes only when several can be chosen, as in filtering). The Number tile (“+10”) has the same size and sits last in the row. States of every tile are under <a class="inline-link inline-link--large inline-link--secondary" href="checkbox-specifications.html#states">States</a> in Specifications.</p><div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage"><div class="cb-pdp" id="t-image"></div></div></figure></div>'''

sizes = '''<h2 class="ds-h2">Sizes</h2><p class="ds-desc">A checkbox has two sizes. <strong>Large</strong> is the default. <strong>Small</strong> (class <code>.form-checkbox-item--sm</code>) is for dense layouts such as tables and filters. Measurements are under <a class="inline-link inline-link--large inline-link--secondary" href="checkbox-specifications.html#sizes">Sizes</a> in Specifications.</p><div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage" data-mode-stage><div class="cb-sizes" id="v-sizes"></div></div><figcaption class="ds-fig__cap">Large and Small in every value. The Mode toggle under Variants applies here too.</figcaption></figure></div>'''

layout = '''<h2 class="ds-h2">Layout &amp; Appearance</h2><h3 class="ds-h3 ds-group">Grouping</h3><p class="ds-desc">Related options go in a <code>fieldset</code> with a <code>legend</code>. Stack them in a column, or wrap them in a row when the labels are short.</p><div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage" data-mode-stage><div class="cb-row" style="align-items:flex-start;gap:32px 48px"><fieldset class="cb-group" id="v-group-col"></fieldset><fieldset class="cb-group cb-group--wrap" id="v-group-row" style="max-width:420px"></fieldset></div></div><figcaption class="ds-fig__cap">A column and a wrapping row. A disabled option stays in the group.</figcaption></figure></div><h3 class="ds-h3 ds-group">Appearance</h3><p class="ds-desc">A checkbox is a 16px box with a 1px grey border that fills black when selected. Use the light version on light surfaces and the dark version (<code>.form-checkbox-item--dark</code>) on dark ones: <code>surface-100</code> or <code>surface-80</code>. Never mix them. The label is 16/22 on mobile and 17/24 from 769px. Token names and values are under <a class="inline-link inline-link--large inline-link--secondary" href="checkbox-specifications.html#design-tokens">Design Tokens</a> in Specifications.</p>'''

behavior = '''<h2 class="ds-h2">Behavior</h2><h3 class="ds-h3 ds-group">Selecting</h3><p class="ds-desc">A click on the box or the label toggles the checkbox. Clearing the mixed state also makes it checked. Space toggles the focused checkbox.</p><h3 class="ds-h3 ds-group">Hover and focus</h3><p class="ds-desc">Hover changes the fill and the border color. The focus ring (2px line, 2px offset) shows with <code>:focus-visible</code> only, so a mouse click does not draw it. The 4px margin around the box leaves room for it. All states are listed under <a class="inline-link inline-link--large inline-link--secondary" href="checkbox-specifications.html#states">States</a> in Specifications.</p><h3 class="ds-h3 ds-group">Mixed</h3><p class="ds-desc">The mixed state belongs to a “select all” parent. It shows when only some of the children are selected, and is set with <code>input.indeterminate = true</code> in JavaScript: it cannot be set in HTML.</p><h3 class="ds-h3 ds-group">Disabled</h3><p class="ds-desc">A disabled checkbox cannot be focused and has no hover. The label turns <code>text-disabled</code> through <code>:has(input:disabled)</code>.</p>'''

access = '''<h2 class="ds-h2">Accessibility</h2><p class="ds-desc">A checkbox is a native <code>&lt;input type="checkbox"&gt;</code>, so the browser and the screen reader do most of the work. All requirements are listed under <a class="inline-link inline-link--large inline-link--secondary" href="checkbox-specifications.html#accessibility-requirements">Accessibility Requirements</a> in Specifications.</p><h3 class="ds-h3 ds-group">Keyboard support</h3><p class="ds-desc">Tab and Shift+Tab move between checkboxes. Space toggles the focused one. The focus ring shows with <code>:focus-visible</code>.</p><h3 class="ds-h3 ds-group">Screen reader support</h3><p class="ds-desc">Every checkbox needs a name: a visible label in the <code>label</code> element, or an <code>aria-label</code> when there is none (Inline menu, tiles, table rows). Group related checkboxes in a <code>fieldset</code> with a <code>legend</code>. Never build the box from an image or an SVG file.</p>'''

related = '''<h2 class="ds-h2">Related</h2><ul class="ds-bullets"><li><strong>''' + link_large('radio.html', 'Radio button') + '''</strong>. Exactly one of two or more options.</li><li><strong>''' + link_large('switch.html', 'Switch') + '''</strong>. An on/off setting with immediate effect.</li><li><strong>''' + link_large('list-item.html', 'List Item') + '''</strong>. A checkbox as the leading or trailing element of a list row.</li><li><strong>''' + link_large('table.html', 'Table') + '''</strong>. Where the Inline menu and the check icon are used.</li></ul>'''

references = '<h2 class="ds-h2">References</h2>' + refs([
    ('https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html', 'WCAG 2.2: Non-text Contrast', 'Success criterion 1.4.11, for the box border and the focus ring.'),
    ('https://www.w3.org/WAI/ARIA/apg/patterns/checkbox/', 'WAI-ARIA Authoring Practices: Checkbox', 'Keyboard and role requirements, including the mixed state.'),
    ('https://www.nngroup.com/articles/checkboxes-vs-radio-buttons/', 'Nielsen Norman Group: Checkboxes vs. Radio Buttons', 'When to use which.'),
    ('https://fluent2.microsoft.design/components/web/react/core/checkbox/usage', 'Fluent 2: Checkbox', 'Microsoft.'),
    ('https://m3.material.io/components/checkbox/overview', 'Material Design 3: Checkbox', 'Google.'),
    ('https://carbondesignsystem.com/components/checkbox/usage/', 'Carbon Design System: Checkbox', 'IBM.')])

ex = [('playground', playground), ('overview', overview), ('usage', usage), ('anatomy', anatomy), ('variants', variants), ('tiles', tiles), ('sizes', sizes),
      ('layout', layout), ('behavior', behavior), ('accessibility', access), ('related', related), ('references', references)]

# ------------------------------------------------------------------------------ Specifications
st_tok = '<h2 class="ds-h2">Design Tokens</h2><p class="ds-desc">Resolved from the live token package.</p>' + \
    '<div class="ds-table-wrap"><table class="ds-table" id="tok-table"><thead><tr><th scope="col">Mode</th><th scope="col">Part · state</th><th scope="col">Token</th><th scope="col">Value</th></tr></thead><tbody></tbody></table></div>' + \
    '<p class="ds-desc ds-note">The checkmark and dash are SVG data URIs, which cannot use <code>var()</code>. Their colors (white, black, <code>#939595</code> for the disabled check) are set in the SVG and match <code>icon-inverted</code>, <code>surface-100</code> and <code>surface-40</code>.</p>'

st_sizes = '<h2 class="ds-h2">Sizes</h2>' + table(['Size', 'Area', 'Box', 'Margin', 'Gap to label', 'Label'], [
    ['Large · Desktop', '24×24px', '16×16px', '4px', '8px', '<code>body-md</code>: 17/24, 0.32px (769px and up)'],
    ['Large · Mobile', '24×24px', '16×16px', '4px', '8px', '<code>body-md</code>: 16/22, 0.32px (below 769px)'],
    ['Small · both', '20×20px', '14×14px', '3px', '4px', '<code>body-sm</code>: 14/20'],
    ['Inline menu', '<td colspan="5">Box as above, then a 24×24px dropdown arrow (<code>icon-primary</code>, dark: <code>icon-inverted</code>). Gap 8px Large, 4px Small. No label.</td>']]) + \
    '<p class="ds-desc ds-note"><strong>Breakpoint.</strong> Figma has two versions of every checkbox: “XLarge–Large–Medium” (Desktop) and “Small–XSmall” (Mobile). In Figma the box, area, gap and Small label are the same in both; only the Large label differs, following <code>body-md</code> (17/24 on Desktop, 16/22 on Mobile). The component switches at 769px by itself. The Breakpoint toggle in the Playground on Examples &amp; Guidelines forces one of them for preview only.</p>' + \
    '<h3 class="ds-h3 ds-group">Tile sizes</h3>' + table(['Tile', 'Desktop', 'Mobile', 'Inside', 'Border (enabled)'], [
        ['Color swatch', '24×24px', '24×24px', '16px swatch, 2px padding', '1px <code>border-secondary</code>'],
        ['Image', '48×48px', '40×40px', 'image 6px from the edge, <code>object-fit: contain</code>', '1px <code>border-primary</code>'],
        ['Number', '48×48px', '40×40px', '<code>label-md</code> 16/16, 0.48px, Bold, uppercase', '1px <code>border-secondary</code>']]) + \
    '<p class="ds-desc ds-note">Hover is 1px <code>border-hover</code>, selected is a 2px <code>border-selected</code> frame, selected hover is a 2px <code>border-selected-hover</code> frame. The fill is <code>surface-raised-primary</code>. In Figma the mobile Color Swatch has a 20×18px swatch box in the selected states; this page uses the 16px swatch for every state and breakpoint.</p>'


def mfig(label, cls, n):
    return ('<div class="measure__item"><span class="measure__name">%d · %s</span><div class="measure__obj"><span class="cb-measure"><label class="form-checkbox-item%s"><input type="checkbox" class="measure__subject" data-measure-margin tabindex="-1" aria-label="%s" /></label></span>'
            '<i class="measure__pad measure__pad--t"></i><i class="measure__pad measure__pad--b"></i><i class="measure__pad measure__pad--l"></i><i class="measure__pad measure__pad--r"></i>'
            '<b class="measure__dim measure__dim--v measure__dim--t"><span></span></b><b class="measure__dim measure__dim--v measure__dim--b"><span></span></b><b class="measure__dim measure__dim--h measure__dim--l"><span></span></b><b class="measure__dim measure__dim--h measure__dim--r"><span></span></b></div></div>') % (n, label, cls, label)

st_meas = '<h2 class="ds-h2">Measurements</h2><h3 class="ds-h3 ds-group">Dimensions</h3><p class="ds-desc">Box and margin of each size. The shaded area is the 4px margin (3px in Small) that leaves room for the focus ring; the lines show its value.</p>' + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-fig__stage--flush" style="padding:0;min-height:0"><div class="measure" role="img" aria-label="Margin of the checkbox: Large 4 on every side, Small 3 on every side" style="--k:4">' + \
    mfig('Large', '', 1) + mfig('Small', ' form-checkbox-item--sm', 2) + '</div></div><figcaption class="ds-fig__cap">The box at 4× size. The numbers are read from the component and are real pixels.</figcaption></figure></div>' + \
    table(['Attribute', 'Large', 'Small (<code>.form-checkbox-item--sm</code>)'], [
        ['Area', '24×24px', '20×20px'], ['Box', '16×16px, 1px border (dark mode: 2px on hover)', '14×14px'], ['Margin around the box', '4px', '3px'],
        ['Focus ring', '2px line, 2px offset (fills the 4px margin)', '2px line, 1px offset (fills the 3px margin)'], ['Gap to the label', '8px', '4px'],
        ['Checkmark', '16px mark in the box', '12px (<code>background-size</code>)'], ['Corners', '<td colspan="2">Square</td>']]) + \
    '<h3 class="ds-h3 ds-group">Spacing</h3><p class="ds-desc">The same margin and gap values as spacing tokens.</p>' + \
    table(['Part', 'Large', 'Small'], [['Margin around the box', '<code>space-4</code>', '3px: no spacing token'], ['Gap box to label', '<code>space-8</code>', '<code>space-4</code>'], ['Gap box to arrow (Inline menu)', '<code>space-8</code>', '<code>space-4</code>']]) + \
    '<p class="ds-desc ds-note">There is no spacing token for 3px. The Small margin is 3px in Figma. <strong>Open point:</strong> keep 3px, or add a token.</p>'

states_html = '<h2 class="ds-h2">States</h2><p class="ds-desc">Every state for each value. Hover and focus are forced on this page with <code>data-state</code> so they can be seen at the same time; in your code they come from <code>:hover</code> and <code>:focus-visible</code>. The cells are live, so click to change the value (disabled cells do not respond).</p>' + \
    toolbar([('sm-l', 'Mode', 'data-mode-toggle', [('light', 'Light', True), ('dark', 'Dark', False)]), ('sb-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force'),
             ('sm-s', 'Size', 'data-mx="size"', [('large', 'Large', True), ('small', 'Small', False)]), ('sm-t', 'Type', 'data-mx="type"', [('standard', 'Standard', True), ('menu', 'Inline menu', False)])]) + \
    '<div class="ds-table-wrap" data-mode-stage-bg><table class="ds-table ds-matrix" id="matrix"><thead><tr><th scope="col">State</th><th scope="col">Unchecked</th><th scope="col">Checked</th><th scope="col">Mixed</th></tr></thead><tbody></tbody></table></div>' + \
    '<p class="ds-desc ds-note">A checked checkbox in hover is “Selected hover”, in focus “Selected focus”. Every state in Figma is shown: nothing is left out for any size, mode or type.</p>' + \
    '<h3 class="ds-h3 ds-group">Tiles</h3><p class="ds-desc">Enabled, hover, selected and selected hover for each tile. Hover is forced on this page. The Number tile only has enabled and hover in Figma.</p>' + \
    '<div class="ds-table-wrap"><table class="ds-table ds-matrix" id="tile-matrix"><thead><tr><th scope="col">State</th><th scope="col">Color swatch</th><th scope="col">Image</th><th scope="col">Number</th></tr></thead><tbody></tbody></table></div>' + \
    '<p class="ds-desc ds-note">Selected is a 2px frame, drawn as a 1px border plus a 1px inset line so the tile never changes size. Disabled is not defined in Figma for tiles.</p>'

st_typo = '<h2 class="ds-h2">Typography</h2>' + table(['Part', 'Type', 'Size / line height', 'Letter spacing', 'Weight'], [
    ['Label, Large', '<code>body-md</code>', '16/22 mobile, 17/24 from 769px', '0.32px', 'Regular'], ['Label, Small', '<code>body-sm</code>', '14/20', '0.36px', 'Regular'],
    ['Number tile', '<code>label-md</code>', '16/16', '0.48px', 'Bold, uppercase'], ['Filter row name and count', '<code>body-md</code>', '16/22 mobile, 17/24 from 769px', '0.32px', 'Regular'],
    ['Color name in the library', '<code>alt-label-lg</code>', '16/16 mobile, 18/18 from 769px', '0.32px / 0.36px', 'Medium, uppercase']]) + \
    '<p class="ds-desc ds-note">Breuer Condensed. The disabled label uses <code>text-disabled</code>.</p>'

st_struct = '<h2 class="ds-h2">Structure</h2><h3 class="ds-group ds-h3">Elements</h3>' + table(['Element', 'Property', 'Value'], [
    ['Area', 'Size', '24×24px (Large), 20×20px (Small): the box plus margin'], ['Box', 'Shape', 'Square, 1px border, <code>appearance: none</code> on the native input'],
    ['Checkmark and dash', 'Drawing', 'SVG data URI as <code>background-image</code>. Never an image file.'], ['Label', 'Element', '<code>&lt;span&gt;</code> inside the <code>&lt;label&gt;</code>; 8px (Large) or 4px (Small) from the box'],
    ['Arrow (Inline menu)', 'Size', '24×24px, <code>.cb-arrow</code>, <code>icon-primary</code> (dark: <code>icon-inverted</code>)']]) + \
    '<h3 class="ds-group ds-h3">Types</h3>' + table(['Type', 'Class', 'Use'], [
        ['Standard', '<code>.form-checkbox-item</code>', 'Box and label.'], ['Small', '<code>.form-checkbox-item--sm</code>', 'Dense layouts: tables, filters.'], ['Dark', '<code>.form-checkbox-item--dark</code>', 'On <code>surface-100</code> or <code>surface-80</code>.'],
        ['Inline menu', '<code>.form-checkbox-item--menu</code> with <code>.cb-arrow</code>', 'Table header: select all and open a menu. No label.'], ['Check icon', '<code>.check-icon</code> on the cell', 'Read-only permission in a table. Always disabled, light only.'],
        ['Tile: color swatch', '<code>.form-checkbox-tile</code>', 'Filtering and PDP. Needs <code>--swatch</code>.'], ['Tile: image', '<code>.form-checkbox-tile--image</code>', 'PDP: one at a time with <code>radio</code>.'], ['Tile: number', '<code>.form-checkbox-tile--number</code>', 'A <code>&lt;button&gt;</code> with “+10”.'],
        ['Filter row', '<code>.form-checkbox-tile--row</code>', 'Color tile with name and count; the whole row is the click target.']])

st_motion = '<h2 class="ds-h2">Motion</h2><p class="ds-desc ds-note">None. The checkbox changes state at once, with no transition and no animation.</p>'

st_behavior = '<h2 class="ds-h2">Behavior</h2>' + table(['Input', 'Result'], [
    ['Click box or label', 'Toggles checked. Clearing the mixed state also makes it checked.'], ['Tab / Shift+Tab', 'Moves between checkboxes. The focus ring shows with <code>:focus-visible</code> only.'], ['Space', 'Toggles the focused checkbox.'],
    ['Mixed', 'Set <code>input.indeterminate = true</code> in JavaScript. It cannot be set in HTML.'], ['Disabled', 'Not focusable, no hover. The label turns <code>text-disabled</code> through <code>:has(input:disabled)</code>.'],
    ['Without label', 'Add <code>aria-label</code>. Never use an image or SVG file for the box.']])

st_access = '<h2 class="ds-h2">Accessibility Requirements</h2>' + table(['Topic', 'Requirement'], [
    ['Element', 'A native <code>&lt;input type="checkbox"&gt;</code>. The role, the state and the keyboard behavior come from the browser.'], ['Name', 'A visible <code>&lt;label&gt;</code>, or <code>aria-label</code> when there is no text (Inline menu, tiles, table rows).'],
    ['Group', 'Related checkboxes in a <code>&lt;fieldset&gt;</code> with a <code>&lt;legend&gt;</code>.'], ['Mixed', 'Set with <code>indeterminate</code> in JavaScript, so assistive technology reads “mixed”.'],
    ['Focus', 'Ring with <code>border-focus</code>, 2px, offset 2px, on <code>:focus-visible</code> (WCAG 2.4.7, 1.4.11).'], ['Disabled', 'Not focusable. The label and the box use disabled tokens, which are exempt from contrast requirements.'],
    ['Tiles', 'No visible label: <code>aria-label</code> is required. On a PDP, show the name of the chosen option next to the group so the choice is not carried by the picture alone.'], ['Color', 'Selected is not shown by color alone: it adds a checkmark (box) or a thicker frame (tile).']])

spec = [('design-tokens', st_tok), ('sizes', st_sizes), ('measurements', st_meas), ('states', states_html), ('typography', st_typo), ('structure', st_struct), ('motion', st_motion), ('behavior', st_behavior), ('accessibility-requirements', st_access)]

# ------------------------------------------------------------------------------ Code
c_basic = '<h2 class="ds-h2">Basic Usage</h2><p class="ds-desc">Link the shared stylesheet once per page. Never copy the rules, and never write a parallel version of the checkbox.</p>' + table(['Step', 'What to do'], [
    ['1. Link', '<code>&lt;link rel="stylesheet" href="/components/css/checkbox.css"&gt;</code>. Both templates (<code>template.html</code>, <code>mypages/mypages-template.html</code>) already have it.'],
    ['2. Markup', 'A <code>&lt;label class="form-checkbox-item"&gt;</code> around an <code>&lt;input type="checkbox"&gt;</code> and a <code>&lt;span&gt;</code> with the label text.'],
    ['3. Dark surface', 'Add <code>form-checkbox-item--dark</code> on <code>surface-100</code> or <code>surface-80</code>. Never the light markup on a dark surface.'],
    ['4. Mixed', 'Set <code>input.indeterminate = true</code> in JavaScript. It cannot be set in HTML.']])
c_cb = '<h2 class="ds-h2">Checkbox</h2><p class="ds-desc">Copy the markup you need. Hover and focus come from <code>:hover</code> and <code>:focus-visible</code>; the <code>[data-state]</code> selectors in the CSS exist only so the documentation can force a state.</p><div id="recipes"></div>'
c_tiles = '<h2 class="ds-h2">Tiles</h2><p class="ds-desc">Tiles have no visible label, so <code>aria-label</code> is required. Several can be chosen with <code>checkbox</code>; on a product page where only one can be chosen, use <code>radio</code> with the same markup.</p><div id="recipes-tiles"></div>'
c_def = '<h2 class="ds-h2">Definition Checkbox</h2><p class="ds-desc ds-note">To be added. No such sibling exists in Figma yet.</p>'
c_api = '<h2 class="ds-h2">API</h2><h3 class="ds-h3 ds-group">Classes</h3>' + table(['Class', 'Use'], [
    ['<code>form-checkbox-item</code>', 'The label around the input and the text. Large, light.'], ['<code>form-checkbox-item--sm</code>', 'Small size.'], ['<code>form-checkbox-item--dark</code>', 'Dark mode, for dark surfaces.'],
    ['<code>form-checkbox-item--menu</code>, <code>cb-arrow</code>', 'Inline menu: the box plus a dropdown arrow, no label.'], ['<code>check-icon</code>', 'On a table cell: a read-only checkmark.'],
    ['<code>form-checkbox-tile</code>, <code>--image</code>, <code>--number</code>, <code>--row</code>', 'Tiles. Inside: <code>form-checkbox-tile__box</code>, <code>__swatch</code> (with <code>--swatch</code>), <code>__text</code>, <code>__count</code>.']]) + \
    '<h3 class="ds-h3 ds-group">Things to know</h3><ul class="ds-bullets"><li>The box is the native input with <code>appearance: none</code>. The checkmark and dash are SVG data URIs, so no image file is loaded.</li><li>A label that contains an input is enough: no <code>for</code>/<code>id</code> pair is needed.</li><li>Breakpoint: the Large label is 16/22 below 769px and 17/24 from 769px. The CSS does this by itself.</li><li>The <code>[data-state="hover"]</code> and <code>[data-state="focus"]</code> selectors do nothing outside the documentation pages.</li><li>A checkbox does not submit when it is unchecked: handle that on the server if a value is needed.</li></ul>'
c_css = '<h2 class="ds-h2">CSS / Tailwind</h2><p class="ds-desc">The component is one CSS file, shared by every page. Link it, never copy it. The CSS below is read from the file the page links, so it is always what you see.</p>' + code_box('css-code', 'CSS (components/css/checkbox.css)')

code = [('basic-usage', c_basic), ('checkbox', c_cb), ('tiles', c_tiles), ('definition-checkbox', c_def), ('api', c_api), ('css-tailwind', c_css, False)]

# ------------------------------------------------------------------------------ scripts
JS_BUILDER = r'''
  /* Build a real component. o: {dark, checked, mixed, disabled, state, label, aria} */
  function cb(o) {
    var l = document.createElement('label');
    l.className = 'form-checkbox-item' + (o.dark ? ' form-checkbox-item--dark' : '') + (o.small ? ' form-checkbox-item--sm' : '') + (o.menu ? ' form-checkbox-item--menu' : '');
    var i = document.createElement('input');
    i.type = 'checkbox'; i.checked = !!o.checked; i.indeterminate = !!o.mixed; i.disabled = !!o.disabled;
    if (o.state === 'hover' || o.state === 'focus') i.dataset.state = o.state;
    if (o.aria) i.setAttribute('aria-label', o.aria);
    l.appendChild(i);
    if (o.menu) {
      var a = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
      a.setAttribute('class', 'cb-arrow'); a.setAttribute('viewBox', '0 0 24 24'); a.setAttribute('aria-hidden', 'true');
      a.innerHTML = '<path d="M7 10l5 5 5-5z"/>'; l.appendChild(a);
    } else if (o.label != null) { var s = document.createElement('span'); s.textContent = o.label; l.appendChild(s); }
    return l;
  }
'''

COLORS_JS = None  # filled from the old page


def old_colors():
    src = open(OLD + 'checkbox.html').read()
    m = re.search(r'  var COLORS = .*?\n  var IMAGES = .*?\n', src, re.S)
    return m.group(0)


JS_EX = JS_BUILDER + r'''
  var mode = 'light';
  /* ── Playground ── */
  var pg = { mode: 'light', size: 'large', type: 'standard', value: 'unchecked', state: 'enabled' };
  function renderPg() {
    var dark = pg.mode === 'dark', label = $('#pg-label').value;
    $('#pg-stage').classList.toggle('ds-stage--dark', dark);
    var menu = pg.type === 'menu', small = pg.size === 'small';
    var aria = menu ? 'Select all' : (label ? null : 'Checkbox');
    $('#pg-label').disabled = menu;
    var node = cb({ dark: dark, small: small, menu: menu, checked: pg.value === 'checked', mixed: pg.value === 'indeterminate', disabled: pg.state === 'disabled', state: pg.state, label: label, aria: aria });
    clear($('#pg-host')).appendChild(node);
    var input = $('input', node);
    input.addEventListener('change', function () { status(input); });
    status(input);
    var html = '<label class="form-checkbox-item' + (dark ? ' form-checkbox-item--dark' : '') + (small ? ' form-checkbox-item--sm' : '') + (menu ? ' form-checkbox-item--menu' : '') + '">\n  <input type="checkbox"' +
      (pg.value === 'checked' ? ' checked' : '') + (pg.state === 'disabled' ? ' disabled' : '') + (aria ? ' aria-label="' + aria + '"' : '') + ' />\n' +
      (menu ? '  <svg class="cb-arrow" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 10l5 5 5-5z"/></svg>\n' : label ? '  <span>' + esc(label) + '</span>\n' : '') + '</label>';
    if (pg.value === 'indeterminate') html += '\n\n<script>\n  document.querySelector(\'input\').indeterminate = true; // cannot be set in HTML\n<\/script>';
    if (pg.state === 'hover' || pg.state === 'focus') html = '<!-- ' + pg.state + ' is forced here for preview; in production it comes from :' + (pg.state === 'hover' ? 'hover' : 'focus-visible') + ' -->\n' + html;
    $('#pg-code').textContent = html;
  }
  function status(i) { $('#pg-status').textContent = 'Now: ' + (i.indeterminate ? 'mixed' : i.checked ? 'checked' : 'unchecked') + (i.disabled ? ', disabled' : ''); }
  DK.wire(pg, renderPg); $('#pg-label').addEventListener('input', renderPg);
  DK.bp();

  /* ── Variants, Sizes, Layout ── */
  function buildVariants() {
    var d = mode === 'dark';
    var sz = clear($('#v-sizes'));
    [['Large', false], ['Small', true]].forEach(function (z) {
      var c = document.createElement('div'); c.className = 'cb-col';
      var cap = document.createElement('div'); cap.className = 'ds-stage__cap'; cap.textContent = z[0]; c.appendChild(cap);
      c.appendChild(cb({ dark: d, small: z[1], label: 'Unchecked' }));
      c.appendChild(cb({ dark: d, small: z[1], checked: true, label: 'Checked' }));
      c.appendChild(cb({ dark: d, small: z[1], mixed: true, label: 'Mixed' }));
      c.appendChild(cb({ dark: d, small: z[1], disabled: true, label: 'Disabled' }));
      sz.appendChild(c);
    });
    var mn = clear($('#v-menu'));
    [false, true].forEach(function (sm) {
      mn.appendChild(cb({ dark: d, small: sm, menu: true, aria: 'Select all' }));
      mn.appendChild(cb({ dark: d, small: sm, menu: true, checked: true, aria: 'Select all, checked' }));
      mn.appendChild(cb({ dark: d, small: sm, menu: true, mixed: true, aria: 'Select all, some selected' }));
    });
    var s = clear($('#v-single'));
    s.appendChild(cb({ dark: d, label: 'With label' }));
    s.appendChild(cb({ dark: d, checked: true, label: 'Checked' }));
    s.appendChild(cb({ dark: d, aria: 'No visible label' }));
    s.appendChild(cb({ dark: d, checked: true, aria: 'No visible label, checked' }));
    function group(host, legend, items) {
      clear(host);
      var lg = document.createElement('legend'); lg.textContent = legend; host.appendChild(lg);
      items.forEach(function (it) { host.appendChild(cb({ dark: d, label: it[0], checked: it[1], disabled: it[2] })); });
    }
    group($('#v-group-col'), 'Delivery options', [['Leave at door', true], ['Text me on arrival'], ['Call me on arrival'], ['Signature required', false, true]]);
    group($('#v-group-row'), 'Show columns', [['Name', true], ['Email', true], ['Role'], ['Last login']]);
    var host = clear($('#v-parent'));
    var parent = cb({ dark: d, label: 'Select all' }), pi = $('input', parent);
    var kids = ['Orders', 'Invoices', 'Reports'].map(function (t, n) { return cb({ dark: d, label: t, checked: n === 0 }); });
    host.appendChild(parent);
    var wrap = document.createElement('div'); wrap.className = 'cb-indent';
    kids.forEach(function (k) { wrap.appendChild(k); });
    host.appendChild(wrap);
    function sync() {
      var on = kids.filter(function (k) { return $('input', k).checked; }).length;
      pi.checked = on === kids.length; pi.indeterminate = on > 0 && on < kids.length;
      $('#v-parent-out').textContent = on + ' of ' + kids.length + ' selected → parent is ' + (pi.indeterminate ? 'mixed' : pi.checked ? 'checked' : 'unchecked');
    }
    pi.addEventListener('change', function () { kids.forEach(function (k) { $('input', k).checked = pi.checked; }); sync(); });
    kids.forEach(function (k) { $('input', k).addEventListener('change', sync); });
    sync();
  }
  DK.mode(function (m) { mode = m; buildVariants(); });
  buildVariants();

''' + old_colors() + r'''
  /* o: {kind color|image|number, name, color, src, checked, state hover|focus, text} */
  function tile(o) {
    var box = document.createElement('span'); box.className = 'form-checkbox-tile__box';
    var el;
    if (o.kind === 'number') {
      el = document.createElement('button'); el.type = 'button'; el.className = 'form-checkbox-tile form-checkbox-tile--number'; el.setAttribute('aria-label', o.name || 'Show 10 more');
      box.textContent = o.text || '+10'; el.appendChild(box);
    } else {
      el = document.createElement('label'); el.className = 'form-checkbox-tile' + (o.kind === 'image' ? ' form-checkbox-tile--image' : '');
      var i = document.createElement('input'); i.type = o.radio ? 'radio' : 'checkbox'; if (o.radio) i.name = o.radio; i.checked = !!o.checked; i.setAttribute('aria-label', o.name); el.appendChild(i);
      if (o.kind === 'image') { var im = document.createElement('img'); im.src = o.src; im.alt = ''; box.appendChild(im); }
      else { var sw = document.createElement('span'); sw.className = 'form-checkbox-tile__swatch'; sw.style.setProperty('--swatch', o.color); box.appendChild(sw); }
      el.appendChild(box);
    }
    if (o.state) el.dataset.state = o.state;
    return el;
  }
  /* A row: tile + name + count (the whole row toggles) */
  function tileRow(o) {
    var el = tile({ kind: 'color', name: o.name, color: o.color, checked: o.checked });
    el.classList.add('form-checkbox-tile--row');
    var t = document.createElement('span'); t.className = 'form-checkbox-tile__text'; t.textContent = o.name;
    var c = document.createElement('span'); c.className = 'form-checkbox-tile__count'; c.textContent = o.count;
    el.appendChild(t); el.appendChild(c); el.querySelector('input').removeAttribute('aria-label');
    return el;
  }
  function buildTiles() {
    var f = clear($('#t-filter'));
    var hd = document.createElement('div'); hd.className = 'cb-filter__head'; hd.innerHTML = '<span class="cb-filter__title">Color</span><span class="cb-filter__chev" aria-hidden="true">expand_less</span>'; f.appendChild(hd);
    var fs0 = document.createElement('fieldset'); fs0.className = 'cb-group'; var lg0 = document.createElement('legend'); lg0.textContent = 'Color'; lg0.style.cssText = 'position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)'; fs0.appendChild(lg0); f.appendChild(fs0);
    [['Beige', 16, true], ['Blue', 419], ['Brown', 10], ['Grey', 149], ['Green', 77]].forEach(function (r) {
      var cd = COLORS.filter(function (x) { return x[0] === r[0]; })[0]; fs0.appendChild(tileRow({ name: r[0], color: cd[1], count: r[1], checked: !!r[2] }));
    });
    var mo = document.createElement('button'); mo.type = 'button'; mo.className = 'cb-filter__more'; mo.textContent = 'Show more'; f.appendChild(mo);
    f.appendChild(document.createElement('hr')).className = 'cb-filter__rule';
    var c = clear($('#t-color')); var lg = document.createElement('legend'); lg.textContent = 'Color'; c.appendChild(lg);
    var cr = document.createElement('div'); cr.className = 'cb-tiles'; c.appendChild(cr);
    COLORS.forEach(function (x, n) { cr.appendChild(tile({ kind: 'color', name: x[0], color: x[1], checked: n === 0 || n === 4 })); });
    var cl = clear($('#t-colorlist'));
    COLORS.forEach(function (x) { var r = document.createElement('div'), l = document.createElement('span'), w = document.createElement('span'); l.className = 'cb-colorlist__label'; l.textContent = x[0]; w.className = 'cb-colorlist__swatch'; w.style.setProperty('--swatch', x[1]); w.setAttribute('aria-hidden', 'true'); r.appendChild(l); r.appendChild(w); cl.appendChild(r); });
    var m = clear($('#t-image'));
    var lab = document.createElement('div'); lab.className = 'cb-pdp__label'; lab.textContent = 'More options'; m.appendChild(lab);
    var nm = document.createElement('div'); nm.className = 'cb-pdp__name'; nm.id = 'pdp-name'; nm.setAttribute('aria-live', 'polite'); nm.textContent = IMAGES[2][0]; m.appendChild(nm);
    var fs = document.createElement('fieldset'); fs.className = 'cb-group'; var lg2 = document.createElement('legend'); lg2.textContent = 'Color'; lg2.style.cssText = 'position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0)'; fs.appendChild(lg2);
    var mr = document.createElement('div'); mr.className = 'cb-tiles'; fs.appendChild(mr); m.appendChild(fs);
    IMAGES.forEach(function (x, n) { var t = tile({ kind: 'image', radio: 'pdp-color', name: x[0], src: x[1], checked: n === 2 }); t.querySelector('input').addEventListener('change', function () { nm.textContent = x[0]; }); mr.appendChild(t); });
    mr.appendChild(tile({ kind: 'number', name: 'Show 10 more colors' }));
  }
  buildTiles();

  /* Usage figures: mixed */
  var fm = clear($('#fig-mix-do')), mp = cb({ label: 'Select all', mixed: true }), mw = document.createElement('div'); mw.className = 'cb-indent';
  [['Orders', true], ['Invoices'], ['Reports']].forEach(function (k) { mw.appendChild(cb({ label: k[0], checked: !!k[1] })); });
  fm.appendChild(mp); fm.appendChild(mw);
  clear($('#fig-mix-dont')).appendChild(cb({ label: 'I accept the terms', mixed: true }));

  /* ── Anatomy ── */
  var an = $('#an-in');
  DK.callouts($('#cb-anat'), [
    { n: 1, side: 'left', len: 48, box: function () { var r = an.getBoundingClientRect(); return { left: r.left - 4, top: r.top - 4, width: 24, height: 24 }; } },
    { n: 2, el: an, side: 'top', len: 40 },
    { n: 3, side: 'bottom', len: 40, box: function () { var r = an.getBoundingClientRect(); return { left: r.left + 3, top: r.top + 4, width: 10, height: 8 }; } },
    { n: 4, el: $('#an-lbl'), side: 'right', len: 56, at: 'edge' }
  ]);
  DK.callouts($('#tile-anat'), [
    { n: 1, el: $('#tn-box'), side: 'top', len: 40 },
    { n: 2, el: $('#tn-img'), side: 'bottom', len: 40, at: 'center' }
  ]);
  renderPg();
'''

JS_SPEC = JS_BUILDER + r'''
  var mode = 'light';
  /* ── State matrix ── */
  var ROWS = [['Enabled', 'enabled'], ['Hover', 'hover'], ['Focus', 'focus'], ['Disabled', 'disabled']];
  var mx = { size: 'large', type: 'standard' };
  $$('[data-mx]').forEach(function (g) { DK.seg(g, function (v) { mx[g.dataset.mx] = v; buildMatrix(); }); });
  var COLS = ['unchecked', 'checked', 'mixed'];
  function buildMatrix() {
    var d = mode === 'dark', tb = clear($('#matrix tbody'));
    $('[data-mode-stage-bg]').classList.toggle('ds-stage--dark', d);
    var menu = mx.type === 'menu', small = mx.size === 'small';
    ROWS.forEach(function (r) {
      var tr = document.createElement('tr'), th = document.createElement('th');
      th.scope = 'row'; th.textContent = r[0] + (r[1] === 'hover' ? ' / Selected hover' : r[1] === 'focus' ? ' / Selected focus' : '');
      tr.appendChild(th);
      COLS.forEach(function (c) {
        var td = document.createElement('td');
        td.appendChild(cb({ dark: d, small: small, menu: menu, checked: c === 'checked', mixed: c === 'mixed', disabled: r[1] === 'disabled', state: r[1], aria: r[0] + ', ' + c, label: menu ? null : undefined }));
        tr.appendChild(td);
      });
      tb.appendChild(tr);
    });
  }
  DK.mode(function (m) { mode = m; buildMatrix(); });
  buildMatrix();

''' + old_colors() + r'''
  function tile(o) {
    var box = document.createElement('span'); box.className = 'form-checkbox-tile__box';
    var el;
    if (o.kind === 'number') {
      el = document.createElement('button'); el.type = 'button'; el.className = 'form-checkbox-tile form-checkbox-tile--number'; el.setAttribute('aria-label', o.name || 'Show 10 more');
      box.textContent = o.text || '+10'; el.appendChild(box);
    } else {
      el = document.createElement('label'); el.className = 'form-checkbox-tile' + (o.kind === 'image' ? ' form-checkbox-tile--image' : '');
      var i = document.createElement('input'); i.type = 'checkbox'; i.checked = !!o.checked; i.setAttribute('aria-label', o.name); el.appendChild(i);
      if (o.kind === 'image') { var im = document.createElement('img'); im.src = o.src; im.alt = ''; box.appendChild(im); }
      else { var sw = document.createElement('span'); sw.className = 'form-checkbox-tile__swatch'; sw.style.setProperty('--swatch', o.color); box.appendChild(sw); }
      el.appendChild(box);
    }
    if (o.state) el.dataset.state = o.state;
    return el;
  }
  var tb = clear($('#tile-matrix tbody'));
  [['Enabled', null, false], ['Hover', 'hover', false], ['Selected', null, true], ['Selected hover', 'hover', true]].forEach(function (r) {
    var tr = document.createElement('tr'), th = document.createElement('th'); th.scope = 'row'; th.textContent = r[0]; tr.appendChild(th);
    [['color', COLORS[4]], ['image', IMAGES[0]], ['number', null]].forEach(function (k) {
      var td = document.createElement('td');
      if (k[0] === 'number' && r[2]) { td.className = 'ds-na'; td.textContent = 'Not defined'; }
      else td.appendChild(tile({ kind: k[0], name: k[1] ? k[1][0] : 'Show 10 more', color: k[0] === 'color' ? k[1][1] : null, src: k[0] === 'image' ? k[1][1] : null, checked: r[2], state: r[1] }));
      tr.appendChild(td);
    });
    tb.appendChild(tr);
  });

  /* ── Token table (resolved live) ── */
  DK.tokenTable($('#tok-table tbody'), [
    ['Light', 'Box border · enabled', 'border-input-control-default'], ['Light', 'Box fill · enabled', 'surface-raised-primary'],
    ['Light', 'Box border · hover', 'border-hover'], ['Light', 'Box fill · hover', 'surface-raised-secondary'],
    ['Light', 'Box fill · checked / mixed', 'surface-100'], ['Light', 'Box fill · checked / mixed hover', 'surface-50'],
    ['Light', 'Box border · disabled', 'border-disabled'], ['Light', 'Box fill · disabled', 'surface-disabled'],
    ['Light', 'Focus ring', 'border-focus'], ['Light', 'Label', 'text-primary'], ['Light', 'Label · disabled', 'text-disabled'],
    ['Dark', 'Box border · enabled / checked', 'border-action-2'], ['Dark', 'Box fill · enabled', 'surface-opacity-white-0'],
    ['Dark', 'Box fill · checked / mixed', 'surface-action-2'], ['Dark', 'Box fill · checked hover', 'surface-40'],
    ['Dark', 'Box border / fill · disabled', 'surface-60'], ['Dark', 'Label', 'text-primary-inverted'], ['Dark', 'Label · disabled', 'text-disabled'],
    ['Tile', 'Border · enabled (swatch, number)', 'border-secondary'], ['Tile', 'Border · enabled (image)', 'border-primary'], ['Tile', 'Border · hover', 'border-hover'],
    ['Tile', 'Frame · selected (2px)', 'border-selected'], ['Tile', 'Frame · selected hover (2px)', 'border-selected-hover'], ['Tile', 'Fill', 'surface-raised-primary'], ['Tile', 'Number text', 'text-primary']
  ]);
  DK.bp(function () { ECO_MEASURE.init(); });
'''

JS_CODE = r'''
  DK.recipes($('#recipes'), [
    ['Standard', '<label class="form-checkbox-item">\n  <input type="checkbox" />\n  <span>Label</span>\n</label>'],
    ['Checked / disabled', '<label class="form-checkbox-item">\n  <input type="checkbox" checked disabled />\n  <span>Label</span>\n</label>'],
    ['Small', '<label class="form-checkbox-item form-checkbox-item--sm">\n  <input type="checkbox" />\n  <span>Label</span>\n</label>'],
    ['Inline menu', '<label class="form-checkbox-item">\n  <input type="checkbox" aria-label="Select all" />\n  <svg class="cb-arrow" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 10l5 5 5-5z"/></svg>\n</label>'],
    ['Dark surface', '<label class="form-checkbox-item form-checkbox-item--dark">\n  <input type="checkbox" />\n  <span>Label</span>\n</label>'],
    ['Group', '<fieldset>\n  <legend>Delivery options</legend>\n  <label class="form-checkbox-item"><input type="checkbox" /><span>Leave at door</span></label>\n  <label class="form-checkbox-item"><input type="checkbox" /><span>Signature required</span></label>\n</fieldset>'],
    ['Mixed (set in JavaScript)', 'document.querySelector(\'#select-all\').indeterminate = true;'],
    ['Table check icon', '<td class="check-icon"><input type="checkbox" checked disabled aria-label="Administrator: yes" /></td>']
  ]);
  DK.recipes($('#recipes-tiles'), [
    ['Tile: color swatch', '<fieldset>\n  <legend>Color</legend>\n  <label class="form-checkbox-tile">\n    <input type="checkbox" aria-label="Blue" />\n    <span class="form-checkbox-tile__box"><span class="form-checkbox-tile__swatch" style="--swatch: #0066ff"></span></span>\n  </label>\n</fieldset>'],
    ['Tile: image', '<label class="form-checkbox-tile form-checkbox-tile--image">\n  <input type="checkbox" aria-label="Yellow / black" />\n  <span class="form-checkbox-tile__box"><img src="/images/product-skaljacka-gul-svart.webp" alt="" /></span>\n</label>'],
    ['Tile: color row in a filter list', '<label class="form-checkbox-tile form-checkbox-tile--row">\n  <input type="checkbox" />\n  <span class="form-checkbox-tile__box"><span class="form-checkbox-tile__swatch" style="--swatch: #0066ff"></span></span>\n  <span class="form-checkbox-tile__text">Blue</span>\n  <span class="form-checkbox-tile__count">419</span>\n</label>'],
    ['Tile: image on a PDP (one at a time)', '<fieldset>\n  <legend>Color</legend>\n  <label class="form-checkbox-tile form-checkbox-tile--image">\n    <input type="radio" name="color" aria-label="Yellow / black" checked />\n    <span class="form-checkbox-tile__box"><img src="/images/product-skaljacka-gul-svart.webp" alt="" /></span>\n  </label>\n  <label class="form-checkbox-tile form-checkbox-tile--image">\n    <input type="radio" name="color" aria-label="Yellow / navy" />\n    <span class="form-checkbox-tile__box"><img src="/images/product-skaljacka-gul-marin.webp" alt="" /></span>\n  </label>\n</fieldset>'],
    ['Tile: number', '<button type="button" class="form-checkbox-tile form-checkbox-tile--number" aria-label="Show 10 more colors">\n  <span class="form-checkbox-tile__box">+10</span>\n</button>']
  ]);
  DK.printCss($('#css-code'), 'checkbox', [[/:is\(:hover, \[data-state="hover"\]\)/g, ':hover'], [/:is\(:focus-visible, \[data-state="focus"\]\)/g, ':focus-visible'], [/,\n    \.form-checkbox-tile\[data-state="focus"\] \.form-checkbox-tile__box/g, ''], [/^ {4}/gm, '']]);
'''

C = dict(
    slug='checkbox', title='Checkbox', eyebrow='Components · Form',
    lead='A checkbox lets the user turn <strong>one or more options</strong> on or off, independently of each other. The choice is saved when the form is submitted.',
    lead_ex='Every example on this page is the real component, not a picture. Click, tab and press Space to try it. Specification: <code>.claude/skills/eco-checkbox/SKILL.md</code>. Figma: <a class="inline-link inline-link--xlarge" href="%s" target="_blank" rel="noopener">Checkbox</a>.' % FIGMA,
    lead_spec='Tokens, sizes, measurements, states and requirements. Values come from the live token package and from Figma: <a class="inline-link inline-link--xlarge" href="%s" target="_blank" rel="noopener">Checkbox</a>.' % FIGMA,
    lead_code='How to add a checkbox to a page. The file is <code>components/css/checkbox.css</code>.',
    css=['checkbox', 'radio'], style=STYLE, ex=ex, spec=spec, code=code, js_ex=JS_EX, js_spec=JS_SPEC, js_code=JS_CODE, tooltip=False,
)

if __name__ == '__main__':
    emit(C)
