from build import *

F_BTN = 'https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=6098-342318'
F_ICON = 'https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=23990-132193'
F_BADGE = 'https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=23998-178299'
SLUG = 'button'
FIGS = fig_link(F_BTN, 'Button') + ', ' + fig_link(F_ICON, 'Icon buttons') + ', ' + fig_link(F_BADGE, 'Button dot &amp; badges')

STYLE = r'''    .bt-row { display: flex; flex-wrap: wrap; gap: 12px 16px; align-items: center; }
    .bt-vrow { display: flex; flex-wrap: wrap; align-items: center; gap: 12px 16px; padding: 12px 0; }
    .bt-vrow + .bt-vrow { border-top: 1px solid var(--color-border-primary); }
    .ds-stage--dark .bt-vrow + .bt-vrow { border-top-color: var(--color-surface-60); }
    .bt-vlabel { flex: 0 0 100%; font-size: 14px; line-height: 20px; letter-spacing: 0.36px; font-weight: 600; color: var(--color-text-tertiary); }
    .ds-stage--dark .bt-vlabel { color: var(--color-text-tertiary-inverted); }
    @media (min-width: 769px) { .bt-vlabel { flex-basis: 168px; } }
    .bt-dark { background: var(--color-surface-100); }
    .ds-matrix td.bt-dark, .ds-matrix th.bt-dark { color: var(--color-text-primary-inverted); border-color: var(--color-surface-60); }
    .ds-matrix td { text-align: center; }
    .ds-matrix td > .btn, .ds-matrix td > .icon-btn { vertical-align: middle; }
    .bt-pair { display: flex; flex-wrap: wrap; gap: var(--dimension-spacing-space-8); align-items: center; }
    .bt-fig { display: flex; flex-wrap: wrap; gap: 12px 16px; align-items: center; }
    .pg-note { font-size: 14px; line-height: 20px; letter-spacing: 0.36px; color: var(--color-text-tertiary); }
    .bt-icons td, .bt-icons th { text-align: center; }
    .bt-icons td:first-child, .bt-icons th:first-child { text-align: left; }
    .bt-icons td { min-width: 72px; }
    .bt-col { display: flex; flex-direction: column; align-items: center; gap: var(--dimension-spacing-space-16); width: 100%; }
    .bt-col .divider { width: 100%; margin: 0; }
    .bt-toast { width: 100%; }
    .bt-toast .ecom-toast--cart { position: static; width: 100%; }   /* demo: the real e-com toast card, in the flow and as wide as the figure */
    .ds-callout__art { padding-right: 56px; }'''


def fig_cls(inner, cap, stage_cls='', ic=None, kind=''):
    """A figure whose stage has an extra class (dark surface)."""
    capin = ('<span class="ds-fig__ic" aria-hidden="true">%s</span>' % ic if ic else '') + cap
    return '<figure class="ds-fig%s"><div class="ds-fig__stage%s">%s</div><figcaption class="ds-fig__cap">%s</figcaption></figure>' % (kind, (' ' + stage_cls) if stage_cls else '', inner, capin)


def pair_cls(do_inner, do_cap, dont_inner, dont_cap, stage_cls=''):
    return '<div class="ds-figs">' + fig_cls(do_inner, do_cap, stage_cls, 'check_circle', ' ds-fig--do') + fig_cls(dont_inner, dont_cap, stage_cls, 'cancel', ' ds-fig--dont') + '</div>'


def sel_field(lid, sid, label, pg, options=None):
    opts = ''.join('<option value="%s">%s</option>' % (v, t) for v, t in (options or []))
    return '<div class="ds-field form-field"><label class="form-label form-label--sm" for="%s" id="%s">%s</label><div class="input-wrap"><select class="form-select form-select--sm" data-pg="%s" id="%s">%s</select><span class="form-select-arrow" aria-hidden="true">arrow_drop_down</span></div></div>' % (sid, lid, label, pg, sid, opts)


def txt_field(id_, label, value, ph, extra=''):
    return '<div class="ds-field form-field"><label class="form-label form-label--sm" for="%s">%s</label><div class="input-wrap"><div class="input-box input-box--sm"><input class="form-input" type="text" id="%s" value="%s" placeholder="%s"%s /></div></div></div>' % (id_, label, id_, value, ph, extra)


playground = '<h2 class="ds-h2">Playground</h2>' + desc('Choose a variant, size, content and state and the button and its code update. The inverted variants are shown on a dark surface here so they are easy to see; choose them by context, visibility and contrast, not by background color alone. The button in the stage is live: click it, or press Tab to see the focus ring.') + \
    '<div class="ds-playground"><div class="ds-stage ds-stage--center" id="pg-stage"><div id="pg-host"></div></div><div class="ds-controls">' + \
    sel_field('pg-l-var', 'pg-variants', 'Variant', 'variant') + bp_field('pg-l-bp') + \
    btn_group('pg-l-size', 'Size', 'data-pg="size"', [('lg', 'Large', True), ('md', 'Medium', False), ('sm', 'Small', False), ('xs', 'XSmall', False)]) + \
    sel_field('pg-l-con', 'sel-pg-l-con', 'Content', 'content', [('label', 'Label'), ('lead', 'Icon + label'), ('trail', 'Label + icon'), ('both', 'Icon + label + icon'), ('icon', 'Icon only')]) + \
    btn_group('pg-l-bd', 'Badge', 'data-pg="badge"', [('none', 'None', True), ('number', 'Number', False), ('dot', 'Dot', False)]) + \
    txt_field('pg-count', 'Badge number (over 99 shows 99+)', '1', 'Badge number', ' inputmode="numeric" maxlength="5"') + \
    btn_group('pg-l-st', 'State', 'data-pg="state"', [('enabled', 'Enabled', True), ('hover', 'Hover', False), ('focus', 'Focus', False), ('disabled', 'Disabled', False)]) + \
    btn_group('pg-l-sel', 'Selected (System only)', 'data-pg="pressed"', [('off', 'Off', True), ('on', 'On', False)]) + \
    txt_field('pg-label', 'Label (not for icon only)', 'Button label', 'Label') + \
    '<p class="ds-swatch__meta" id="pg-status" aria-live="polite"></p></div></div><h3 class="ds-h3">Markup for this selection</h3>' + code_box('pg-code', 'HTML')

overview = '<h2 class="ds-h2">Overview</h2>' + desc('A button <strong>triggers an action</strong> or <strong>takes the user to another page</strong>. It lets the user make a choice with a single tap. Use a mix of styles on one page to point at the main action and still offer the alternatives.') + \
    desc('Button has nine variants (Primary, Secondary, Blank, Destructive, Accent, System and the three Inverted ones), four sizes (Large, Medium, Small, XSmall), a label, one or two icons or an icon only, an optional badge, and four states. The icon button (toggle icons and Close) is a single icon that is also a control.') + \
    desc('Choose a style by the role and importance of the action. The guidance for each style applies to all its sizes and states. Use clear, action-specific labels, keep the contrast accessible and the keyboard focus visible.') + \
    three_pages(SLUG, 'a button', 'the values: tokens, sizes, measurements, states and requirements', 'how to add one to a page')

usage = '<h2 class="ds-h2">Usage</h2><h3 class="ds-h3 ds-group">When to use</h3>' + desc('Use a button when the user starts something with a single tap. Use it to:') + \
    bullets(['Start an action, such as “Add to cart”, “Save” or “Delete”', 'Move on to the next step, or to another page, such as “Next” or “Go to checkout” (a link that looks like a button: <code>&lt;a class="btn …"&gt;</code>)', 'Filter or switch in a group of many buttons (System, with <code>aria-pressed</code>)']) + \
    '<h3 class="ds-h3 ds-group">When not to use</h3><h3 class="ds-h3">More than one Primary button</h3>' + desc('A page can show several buttons, but one action must stand out. Use <strong>at most one Primary button per screen, section or container</strong> and Secondary or Blank for the others. Too many Primary buttons cause confusion.') + \
    fig_pair('<div class="bt-fig" id="fig-p-do"></div>', 'Do use one Primary button and a quieter Secondary.', '<div class="bt-fig" id="fig-p-dont"></div>', 'Do not show several Primary buttons next to each other.') + \
    '<h3 class="ds-h3">The wrong variant for the context</h3>' + desc('Choose standard or Inverted by the surrounding context, visibility and contrast, not by the background color alone. An inverted variant keeps the role and priority of its standard variant, and it is not limited to dark or colored surfaces.') + \
    pair_cls('<div class="bt-fig" id="fig-d-do"></div>', 'Do choose the variant that has clear contrast on the surface.', '<div class="bt-fig" id="fig-d-dont"></div>', 'Do not use a variant that lacks contrast on the surface.', 'ds-stage--dark') + \
    '<h3 class="ds-h3">A destructive action</h3>' + desc('Use Destructive for an action that deletes, removes or otherwise causes a potentially harmful change to user data or content. Name the consequence in the label. For an irreversible or high-impact action, add a safeguard such as a confirmation, and allow undo where feasible. Never use Destructive only to draw attention.') + \
    fig_pair('<div class="bt-fig" id="fig-x-do"></div>', 'Do name the consequence in the label.', '<div class="bt-fig" id="fig-x-dont"></div>', 'Do not use a generic label such as “Confirm”.') + \
    '<h3 class="ds-h3">A business-critical action</h3>' + desc('Accent is a brand treatment, not a level in the action hierarchy. Use it selectively for brand personality or a non-business-critical action, and never let it compete with the Primary call to action.') + \
    fig_pair('<div class="bt-fig" id="fig-a-do"></div>', 'Do use Primary for “Add to cart”.', '<div class="bt-fig" id="fig-a-dont"></div>', 'Do not use Accent for “Add to cart”.') + \
    '<h3 class="ds-h3 ds-group">Writing button labels</h3>' + desc('A label says what the button does. Write it in sentence case in the HTML: the CSS makes it uppercase.') + bullets(['<strong>Start with a verb.</strong> Use a clear, specific action verb that describes exactly what the button does: Save, Send, Add user.', '<strong>Keep it short.</strong> Aim for one to three words, quick to scan: “View details”, not “Click here to view more information”.', '<strong>Be specific.</strong> Avoid vague labels such as “Submit” or “Confirm” and make the outcome explicit: “Request booking”.', '<strong>Name destructive actions clearly.</strong> Use a strong, unambiguous verb: Delete, Remove or Discard. Avoid Clear, Reset and Clean. “Delete user” is clear; “Remove” alone is too vague. Add supporting signals such as color, an icon or a confirmation where needed.', '<strong>Use the same verb everywhere.</strong> Choose one verb for a recurring action and keep it, for example Edit or Modify, not both.']) + \
    '<h3 class="ds-h3">A long label</h3>' + desc('A long label is slow to scan and makes the button wide. Start with a verb and keep it short.') + \
    fig_pair('<div class="bt-fig" id="fig-l-do"></div>', 'Do start with a verb and keep it short.', '<div class="bt-fig" id="fig-l-dont"></div>', 'Do not fill the button with a sentence.') + \
    '<h3 class="ds-h3">A vague label</h3>' + desc('A label such as “Submit” does not say what happens next. Name the outcome.') + \
    fig_pair('<div class="bt-fig" id="fig-v-do"></div>', 'Do name the outcome.', '<div class="bt-fig" id="fig-v-dont"></div>', 'Do not use a vague label such as “Submit”.') + \
    '<h3 class="ds-h3 ds-group">Quick reference</h3>' + \
    table(['The user…', 'Use'], [['starts an action or moves to the next step', 'Button'], ['follows a standalone link, such as “View all products”', '<a class="inline-link inline-link--small" href="action-link.html">Action link</a>'], ['follows a link inside a sentence', '<a class="inline-link inline-link--small" href="inline-link.html">Inline link</a>'], ['chooses a brand or category from a graphic tile', '<a class="inline-link inline-link--small" href="tile-link.html">Tile link</a>'],
                                  ['picks one of 2–4 short options in a toolbar', '<a class="inline-link inline-link--small" href="button-group.html">Button group</a>'], ['switches between two related views', '<a class="inline-link inline-link--small" href="segment-control.html">Pill segment control</a>'], ['turns a setting on or off at once', '<a class="inline-link inline-link--small" href="switch.html">Switch</a>']]) + \
    rules(['Use at most one Primary button per screen, section or container.', 'Use Secondary for “Cancel” and “Back”, and Blank for the quietest actions.', 'Write short labels that start with a verb.', 'Choose standard or inverted variants by context, visibility and contrast.', 'Name the consequence on a Destructive button.', 'Give every icon-only button an <code>aria-label</code>.'],
          ['Show several Primary buttons next to each other.', 'Use a button for navigation to another site section when a link fits. Use a link.', 'Use Destructive as the default choice in a dialog.', 'Use a variant that lacks clear contrast on its surface.', 'Use Accent for a business-critical action such as “Add to cart”.', 'Hardcode colors or sizes. Use the tokens and the size classes.'])

anatomy = '<h2 class="ds-h2">Anatomy</h2><h3 class="ds-h3 ds-group">Button</h3>' + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout" id="bt-anat" role="img" aria-label="Anatomy of a button: 1 container, 2 icon, 3 label, 4 badge"><div class="ds-callout__art"><div id="a-host"></div></div></div></figure></div>' + \
    ol_parts([('Container', 'A box of a fixed height with the content centred. Large is 56px high on desktop and 48px on mobile. The 1px frame of Secondary and System is drawn inside the box.'), ('Icon', 'Optional, before the label, after it, or on both sides. Material Symbols, 24px (20px in XSmall), with no gap to the label.'),
              ('Label', 'Breuer Condensed, uppercase, 600. It has its own 8px inset (4px in XSmall), so the width is the label plus both insets.'), ('Badge', 'Optional number in the top right corner, a count that shows “99+” over 99. It shows that something needs attention and is hidden from screen readers.')]) + \
    desc('An icon-only button is a square the same height as the text button.') + \
    '<h3 class="ds-h3 ds-group">Icon-only button with a dot</h3>' + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-callout" id="bt-anat2" role="img" aria-label="Anatomy of an icon-only button with a dot: 1 container, 2 icon, 3 dot"><div class="ds-callout__art"><div id="a-host2"></div></div></div></figure></div>' + \
    ol_parts([('Container', 'A square, as wide as it is high: 56px on desktop and 48px on mobile for Large. There is no label and no padding, so it needs an <code>aria-label</code>.'), ('Icon', 'The only content, centred. Material Symbols, 24px (20px in XSmall), <code>aria-hidden="true"</code>.'),
              ('Dot', 'A 6px circle in <code>surface-danger-default</code> in the top right corner. It shows that something is new, with no count, and is hidden from screen readers: put “new” in the <code>aria-label</code>. Its offset from the corner follows the size and breakpoint (12px for Large on desktop).')])

variants = '<h2 class="ds-h2">Variants</h2>' + desc('Nine variants in four sizes. The Breakpoint toggle previews what Figma calls Desktop (769px and up) and Mobile (below 769px). The component switches by itself at 769px, so you never set it yourself.') + \
    toolbar([('vb-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force')]) + \
    '<h3 class="ds-h3 ds-group">Hierarchy</h3>' + desc('A page can show more than one button. Combine styles so one action stands out and the others are quieter. Large, Medium, Small and XSmall are shown on each row.') + \
    fig_one('<div id="v-light"></div>') + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-stage--dark"><div id="v-dark"></div></div></figure></div>' + \
    note('The inverted variants (Primary, Secondary and Blank) keep the role and priority of the standard ones. They are shown on a dark surface here. Choose between standard and inverted by context, visibility and contrast, not by background color alone.') + \
    '<h3 class="ds-h3 ds-group">When to use each variant</h3>' + table(['Variant', 'Use when', 'Avoid when'], [
        ['Primary', 'The most important, highest-priority action, typically the user’s main goal: completing a task or moving forward in a process, such as “Add to cart”, “Proceed to checkout”, “Continue” or “Submit”. Use <strong>at most one Primary button per screen, section or container</strong> (for example a banner or a card), so buttons do not compete and the way forward is clear.', 'Several high-priority actions appear together. Use Secondary or Blank to set the hierarchy.'],
        ['Secondary', 'Supporting actions that matter but are not the main task, such as “More info”, “Edit” or “Export”. It works next to a Primary button as a complement without competing with it, or alone when no Primary action is needed. Also when a task needs more weight than a Blank button, for example “+ Add address” beside a Blank “Update”.', 'It sits among other visually heavy actions, where a lighter option (Blank or System) fits better.'],
        ['Blank (tertiary)', 'Low-emphasis actions that stay available without dominating the interface: in headers, filter panels and table tools, or beside a Primary button as “Cancel” in a dialog, or “Read more” next to “Buy now”. Choose Blank by the action’s importance, not by the number of buttons in a group. It can appear several times in one view.', 'The flow is critical (checkout, form steps) and clarity and emphasis matter, for the main call to action, or for actions that must be easy to discover. Users may fail to recognize it as clickable.'],
        ['Destructive', 'Actions that delete, remove or otherwise cause a potentially harmful change to user data or content. Use it with caution, with a specific label such as “Delete project”. For irreversible or high-impact actions add a safeguard such as a confirmation, and allow undo where feasible.', 'As a default action, or only to draw attention to a non-destructive action.'],
        ['Accent', 'Selective use to express brand personality or highlight a non-business-critical action. A brand treatment, not an extra level in the hierarchy. It uses the brand colors in the semantic tokens: <code>accent-default</code> for the background and <code>text-action-accent</code> for the label.', 'Business-critical actions such as “Add to cart”, or where it would compete with the Primary call to action.'],
        ['System', 'A low- to medium-emphasis action that must be clickable without competing with more important ones. For dense interfaces where many buttons appear at once: lists with many actions (rows and cards), filters, tables and data-dense views, and low business-priority actions such as “Show details”, expand, open tools or open settings. It keeps the hierarchy between Primary and Secondary clear and the interface calm.', 'High-priority actions (use Primary). Business-critical but secondary actions (use Secondary). Destructive actions (use Destructive). A button that must stand out in a busy context such as a modal, a step or checkout.'],
        ['System selected', 'A System button that is an active mode, turned on or off with an immediate effect: a mode switch for views, filters, tools and functions, such as activating a filter chip or choosing a sorting mode. The selected look stays until the selection changes. Use <code>aria-pressed</code>.', 'An on/off setting (use a Switch). An action that needs confirmation, such as deleting or a critical change (use Primary or Destructive). An action without immediate effect (use a checkbox and an Apply button). A one-time action.'],
        ['Inverted', 'Primary, Secondary and Blank Inverted have the same role and priority as the standard ones. Choose them when their appearance gives clear visibility and enough contrast in the surrounding context. Not limited to dark or colored surfaces.', 'The standard variant already has clear contrast on the surface.']]) + \
    '<h3 class="ds-h3 ds-group">With icons</h3>' + desc('Each variant can be used with a leading icon, a trailing icon, both, or an icon only for compact or utility-focused interactions. A leading icon is the usual choice; a trailing icon, or both, is not common but an option when needed. The icon is 24px (20px in XSmall), with no gap to the label. Icons here are Material Symbols.') + fig_one('<div id="v-icons"></div>') + \
    '<h3 class="ds-h3 ds-group">Icon only</h3>' + desc('Use an icon-only button where space is constrained. It is a square the same height as the text button, it needs an <code>aria-label</code>, and it is always accompanied by a <a class="inline-link inline-link--large inline-link--secondary" href="tooltip.html">tooltip</a> that describes the action. The tooltip is shown after a 300ms hover delay (see ' + sec_link(SLUG, 'behavior', 'Behavior') + ' in Specifications).') + \
    '<h3 class="ds-h3 ds-group">Badge</h3>' + desc('A badge sits in the top right corner and shows that something needs attention, such as items in a cart. It is a <strong>number</strong> (a count that shows “99+” for anything over 99, so type 150 in the playground and you get 99+) or a <strong>dot</strong> (something new, no count). It works on a button with a label and on an icon-only button, in every size. Size and position follow the button size and breakpoint (see ' + sec_link(SLUG, 'sizes', 'Sizes') + ' in Specifications).') + fig_one('<div id="v-badge"></div>') + \
    note('In Small and XSmall the number badge overlaps the end of the label, as in Figma. Prefer an icon-only button when the label is long. The badge is decoration for the eye: put the count in the <code>aria-label</code> and mark the badge <code>aria-hidden="true"</code>.') + \
    '<h3 class="ds-h3 ds-group">System buttons and selected</h3>' + desc('System buttons toggle: click one to select or clear it. Selected has a <code>surface-opacity-black-12</code> surface and the same quiet frame.') + fig_one('<div class="bt-row" id="v-system" role="group" aria-label="Filter example"></div>') + \
    '<h3 class="ds-h3 ds-group">Combining variants</h3>' + desc('A general rule is to pair a high-emphasis button with a lower-emphasis one. In most cases that is a Primary with a Secondary: Secondary is the go-to partner of a Primary.') + bullets(['<strong>Multiple actions.</strong> In layouts with many actions, such as page headers, data lists or dashboards, group the low-emphasis buttons together to keep the visual balance. Use the same low-emphasis variant for all of them, typically System buttons.', '<strong>Dialogs and panels.</strong> Use a Primary button for the confirmation, a Secondary for supporting actions, and Blank for lesser supporting actions such as Cancel or Back.']) + \
    '<div class="ds-figs">' + fig_cls('<div class="bt-col" id="fig-c1"></div>', 'Do use the same low-emphasis variant when multiple actions are required.', '', 'check_circle', ' ds-fig--do') + fig_cls('<div class="bt-toast"><div class="ecom-toast ecom-toast--cart"><div class="ecom-toast__header"><div class="ecom-toast__image-text"><img class="ecom-toast__img" src="/images/product-hantverksbyxa.jpg" alt="" /><p class="ecom-toast__text"><span class="ecom-toast__name">Carpenter Soul work pants stretch black</span> has been added to the cart.</p></div><button type="button" class="icon-btn icon-btn--close" aria-label="Close"><span class="btn__icon" aria-hidden="true">close</span></button></div><div class="ecom-toast__footer"><button type="button" class="btn btn--blank btn--xs"><span class="btn__label">Accessories</span></button><button type="button" class="btn btn--primary btn--xs"><span class="btn__label">Go to cart</span></button></div></div></div>', 'Do pair a Primary button with a lower-emphasis button, here Blank in the E-Com Toast.', '', 'check_circle', ' ds-fig--do') + '</div>' + \
    fig_one('<div class="bt-pair" id="v-pairs" style="gap:32px 48px"></div>', 'More combinations: Primary with Blank, Primary with Secondary, Secondary with Blank, and a dialog set (Primary, Secondary, Blank).')

icons = '<h2 class="ds-h2">Icon buttons</h2>' + desc('An icon button is a single icon that is also a control, with no label and no frame. It is used where the action is well known from the icon: favourite, edit, show on a map, scan, close. Do not use it where the icon alone would be unclear. Use a tooltip (<a class="inline-link inline-link--large inline-link--secondary" href="tooltip.html">Tooltip</a>) and an <code>aria-label</code>.') + \
    '<h3 class="ds-h3 ds-group">Toggle icons</h3>' + desc('Eight icons in Figma. Each has Enabled, Hover, Selected and Selected hover, in Large (24px) and Small (20px). Selected shows the filled icon. The icons on this page are Material Symbols stand-ins for the exact Figma drawings. Every state is under ' + sec_link(SLUG, 'states', 'States') + ' in Specifications.') + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage"><div class="bt-row" id="v-ib" role="group" aria-label="Toggle icons"></div></div><figcaption class="ds-fig__cap">Click an icon to select it.</figcaption></figure></div>' + \
    '<h3 class="ds-h3 ds-group">Close</h3>' + desc('A 24px box with a 20px icon, for closing a modal, drawer, banner or toast. It has a Blank and a Blank inverted version (for contexts where the standard one lacks contrast). Hover adds a surface. The size is the same on desktop and mobile.') + \
    '<div class="ds-figs">' + fig_cls('<div class="bt-row" id="v-close"></div>', 'Blank, on a light surface.') + fig_cls('<div class="bt-row" id="v-close-inv"></div>', 'Blank inverted, on a dark surface.', 'ds-stage--dark') + '</div>'

sizes = '<h2 class="ds-h2">Sizes</h2>' + desc('Four sizes. Large, Medium and Small change at 769px; XSmall is 32px high on both. Figma has two versions of every button: “XLarge–Large–Medium” (Desktop, 769px and up) and “Small–XSmall” (Mobile, below 769px). The tablet range (640 to 768px) uses the Mobile version. The breakpoint behavior of each size is the same for every variant and grid density. Measurements are under ' + sec_link(SLUG, 'sizes', 'Sizes') + ' in Specifications.') + \
    toolbar([('sb-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force')]) + fig_one('<div id="v-sizes"></div>')

layout = '<h2 class="ds-h2">Layout &amp; Appearance</h2><h3 class="ds-h3 ds-group">Alignment</h3>' + note('To be added to the Foundations (Layout) page: where the Primary button goes, how buttons stack when they do not fit side by side, and what to do with a label that does not fit. Pairs of buttons are under ' + '<a class="inline-link inline-link--medium inline-link--secondary" href="#variants">Variants</a>' + ', Combining variants.') + \
    '<h3 class="ds-h3 ds-group">Width</h3>' + desc('A button is as wide as its content: padding, icon or label, and the label inset, on both sides. An icon-only button is a square. There is no minimum width and no modifier for a full-width button: a button that must fill its container gets its width from the page layout.') + \
    '<h3 class="ds-h3 ds-group">Appearance</h3>' + desc('Square corners, a fixed height per size, and an uppercase label in Breuer Condensed, 600. Primary, Destructive and Accent are filled; Secondary and System have a 1px frame; Blank has neither. Token names and values are under ' + sec_link(SLUG, 'design-tokens', 'Design Tokens') + ' in Specifications.')

behavior = '<h2 class="ds-h2">Behavior</h2><h3 class="ds-h3 ds-group">Hover</h3>' + desc('A layer dissolves in over the base color: <code>surface-opacity-white-20</code> on Primary, Destructive and Accent, <code>surface-opacity-black-12</code> on Primary inverted, <code>surface-opacity-black-05</code> on Secondary and Blank, and <code>surface-opacity-white-20</code> on the inverted Secondary and Blank. System hover and System selected hover are the same: a <code>surface-opacity-black-12</code> surface and a <code>border-hover</code> frame.') + \
    '<h3 class="ds-h3 ds-group">Focus</h3>' + desc('The ring is a 2px <code>border-focus</code> line with a 2px gap, drawn outside the button, so it never moves anything. It shows on keyboard use only: <code>body.keyboard-nav</code> is set on Tab and removed on mousedown and touchstart, the same as the form controls.') + \
    '<h3 class="ds-h3 ds-group">Disabled</h3>' + desc('Use the <code>disabled</code> attribute. A disabled button is not focusable and has no hover. Secondary, Secondary inverted and System keep a frame in <code>border-disabled</code> with no fill; Blank has neither; the others get <code>surface-disabled</code>. Say why in nearby text when the reason is not obvious.') + \
    '<h3 class="ds-h3 ds-group">Selected (System)</h3>' + desc('A System button is a toggle. A click sets or clears <code>aria-pressed</code>; your script does it, the CSS does not. It must not be used for page navigation. Selected is a persistent state, not hover, focus or a temporary pressed state, and it stays until the selection changes. Do not use it for a one-time action.') + \
    '<h3 class="ds-h3 ds-group">Destructive actions</h3>' + desc('For an irreversible or high-impact action, add a safeguard such as a confirmation, and allow the user to undo it where feasible. Never make Destructive the default choice in a dialog.') + \
    '<h3 class="ds-h3 ds-group">Icon only</h3>' + desc('An icon-only button has no visible text, so it is always accompanied by a tooltip that describes the action. The tooltip appears after a 300ms delay when the user hovers the button. A disabled button never has a tooltip.') + \
    '<h3 class="ds-h3 ds-group">Motion</h3>' + desc('The hover layer dissolves in over 100ms with <code>ease-standard</code>. Details are under ' + sec_link(SLUG, 'motion', 'Motion') + ' in Specifications.') + \
    note('All states are listed under ' + sec_link(SLUG, 'states', 'States') + ' in Specifications.')

access = '<h2 class="ds-h2">Accessibility</h2>' + desc('All requirements are listed under ' + sec_link(SLUG, 'accessibility-requirements', 'Accessibility Requirements') + ' in Specifications.') + \
    '<h3 class="ds-h3 ds-group">Keyboard support</h3>' + desc('Tab moves between buttons. Enter or Space runs the action (a link that looks like a button runs on Enter). The focus ring shows on keyboard use only.') + \
    '<h3 class="ds-h3 ds-group">Screen reader support</h3>' + desc('Use a label that names the action, such as “Delete project”, not “Confirm”. Use <code>&lt;button&gt;</code> for actions and <code>&lt;a class="btn …"&gt;</code> for navigation. An icon-only button needs an <code>aria-label</code>, and its icon is <code>aria-hidden="true"</code>. A badge is hidden too: put the count in the <code>aria-label</code>. A System button announces its state through <code>aria-pressed</code>.')

related = '<h2 class="ds-h2">Related</h2><ul class="ds-bullets"><li><strong>' + link_large('button-group.html', 'Button group') + '</strong>. Joined System buttons for choosing between two to four short options.</li><li><strong>' + link_large('action-link.html', 'Action link') + '</strong>. A standalone link with an optional icon.</li><li><strong>' + link_large('inline-link.html', 'Inline link') + '</strong>. A link inside a sentence.</li><li><strong>' + link_large('tile-link.html', 'Tile link') + '</strong>. A graphical link, such as a brand logo.</li><li><strong>' + link_large('segment-control.html', 'Pill segment control') + '</strong>. A switch between two related views.</li><li><strong>' + link_large('switch.html', 'Switch') + '</strong>. An immediate on or off setting.</li><li><strong>' + link_large('tooltip.html', 'Tooltip') + '</strong>. The short name of an icon-only button.</li></ul>'

references = '<h2 class="ds-h2">References</h2>' + refs([
    ('https://www.w3.org/WAI/ARIA/apg/patterns/button/', 'WAI-ARIA Authoring Practices: Button', 'Keyboard and role requirements.'),
    ('https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html', 'WCAG 2.2: Non-text Contrast', 'Success criterion 1.4.11.'),
    ('https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html', 'WCAG 2.2: Target Size (Minimum)', 'Success criterion 2.5.8.'),
    ('https://fluent2.microsoft.design/components/web/react/core/button/usage', 'Fluent 2: Button', 'Microsoft.'),
    ('https://m3.material.io/components/buttons/overview', 'Material Design 3: Buttons', 'Google.'),
    ('https://carbondesignsystem.com/components/button/usage/', 'Carbon Design System: Button', 'IBM.')])

ex = [('playground', playground), ('overview', overview), ('usage', usage), ('anatomy', anatomy), ('variants', variants), ('icon-buttons', icons), ('sizes', sizes), ('layout', layout), ('behavior', behavior), ('accessibility', access), ('related', related), ('references', references)]

# ---------------------------------------------------------------- Specifications
st_tok = '<h2 class="ds-h2">Design Tokens</h2>' + desc('Resolved from the live token package.') + \
    '<div class="ds-table-wrap"><table class="ds-table" id="tok-table"><thead><tr><th scope="col">Variant · part</th><th scope="col">Where</th><th scope="col">Token</th><th scope="col">Value</th></tr></thead><tbody></tbody></table></div>' + \
    note('<strong>Open points:</strong> Figma sets <code>ss02</code> and <code>ss03</code> on <code>label-lg</code> and <code>label-sm</code> but not on <code>label-md</code> (Small): the CSS follows Figma, confirm that is meant. Disabled Primary inverted and Accent were read from the screenshot (grey <code>surface-disabled</code> fill). Figma uses both <code>text-primary-inverted</code> and <code>text-action-primary-inverted</code> for the white of the badge number: the CSS uses the action token. The badge pill uses a literal <code>100px</code> radius. The toggle icon button has no focus or disabled state in Figma: disabled uses <code>text-disabled</code>, because <code>icon/disabled</code> (#939595) has no token.')

st_sizes = '<h2 class="ds-h2">Sizes</h2>' + desc('Heights and type per size and breakpoint. The table is generated from the same numbers the Breakpoint toggle previews.') + \
    '<div class="ds-table-wrap"><table class="ds-table" id="size-table"><thead><tr><th scope="col">Size</th><th scope="col">Height</th><th scope="col">Padding</th><th scope="col">Label inset</th><th scope="col">Icon</th><th scope="col">Label style</th></tr></thead><tbody></tbody></table></div>' + \
    note('Icon-only buttons are squares: width equals height (56 / 48 / 40 / 32px on desktop, 48 / 40 / 32 / 32px on mobile). The 1px frame of Secondary, System and their inverted versions is drawn inside the box, so it never changes the size: Primary and Secondary of the same size are equally wide. The tablet range (640 to 768px) uses the Mobile values.') + \
    '<h3 class="ds-h3 ds-group">Badge sizes</h3>' + desc('Number badge: a pill, as high as it is wide for one digit and wider for two or “99+”. Offsets are from the top and right edge of the button. Same numbers for a button with a label and an icon-only button, except XSmall icon only (2px).') + \
    '<div class="ds-table-wrap"><table class="ds-table" id="badge-table"><thead><tr><th scope="col">Size · breakpoint</th><th scope="col">Number: offset</th><th scope="col">Height</th><th scope="col">Side padding</th><th scope="col">Digits</th><th scope="col">Dot: offset</th></tr></thead><tbody></tbody></table></div>' + \
    note('The badge is <code>surface-danger-default</code> with a white number (<code>text-action-primary-inverted</code>), uppercase, 600. The dot is a 6px circle in the same color.') + \
    '<h3 class="ds-h3 ds-group">Icon buttons</h3>' + table(['Version', 'Box', 'Icon'], [['Toggle icon, Large', '24px', '24px'], ['Toggle icon, Small', '20px', '20px'], ['Close', '24px (2px padding)', '20px']]) + \
    note('Close is 24px in Figma, below the usual 44px touch target, and Figma has no larger hit-area version. It meets the WCAG 2.2 minimum (24px).')


def mfig(n, name, size):
    return ('<div class="measure__item"><span class="measure__name">%d · %s</span><div class="measure__obj"><button type="button" class="btn btn--secondary btn--%s measure__subject" tabindex="-1"><span class="btn__label">Button label</span></button>'
            '<i class="measure__pad measure__pad--t"></i><i class="measure__pad measure__pad--b"></i><i class="measure__pad measure__pad--l"></i><i class="measure__pad measure__pad--r"></i>'
            '<b class="measure__dim measure__dim--v measure__dim--t"><span></span></b><b class="measure__dim measure__dim--v measure__dim--b"><span></span></b><b class="measure__dim measure__dim--h measure__dim--l"><span></span></b><b class="measure__dim measure__dim--h measure__dim--r"><span></span></b></div></div>') % (n, name, size)


st_meas = '<h2 class="ds-h2">Measurements</h2><h3 class="ds-h3 ds-group">Dimensions</h3>' + desc('The padding of each size: the space between the edge of the button and its content. The label has an extra inset on top of it (see the table). The numbers are read from the component.') + \
    toolbar([('mb-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force')]) + \
    '<div class="ds-figs ds-figs--one"><figure class="ds-fig"><div class="ds-fig__stage ds-fig__stage--flush" style="padding:0;min-height:0"><div class="measure" style="--k:2" role="img" aria-label="Padding of a button, left and right, per size">' + \
    mfig(1, 'Large', 'lg') + mfig(2, 'Medium', 'md') + mfig(3, 'Small', 'sm') + mfig(4, 'XSmall', 'xs') + \
    '</div></div><figcaption class="ds-fig__cap">A Secondary button at 2× size. Change the Breakpoint to see the mobile values.</figcaption></figure></div>' + \
    table(['Attribute', 'Large', 'Medium', 'Small', 'XSmall'], [
        ['Height, desktop', '56px', '48px', '40px', '32px'], ['Height, mobile', '48px', '40px', '32px', '32px'], ['Padding left and right, desktop', '16px', '12px', '8px', '6px'], ['Padding left and right, mobile', '12px', '8px', '4px', '6px'],
        ['Label inset, left and right, desktop', '8px', '8px', '8px', '4px'], ['Label inset, left and right, mobile', '8px', '8px', '6px', '4px'], ['Icon', '24px', '24px', '24px', '20px'], ['Padding above and below', 'None: the height is fixed and the content is centred', 'None', 'None', 'None'],
        ['Frame', '1px, inside the box', '1px, inside the box', '1px, inside the box', '1px, inside the box'], ['Focus ring', '2px line, 2px gap, outside the box', '2px line, 2px gap', '2px line, 2px gap', '2px line, 2px gap']]) + \
    note('An icon-only button has no padding: it is a square the size of its height, with the icon centred. The icon button has no padding either (Close has 2px).') + \
    '<h3 class="ds-h3 ds-group">Spacing</h3>' + desc('The padding and the label inset as spacing tokens.') + table(['Part', 'Value'], [['Padding, Large desktop', '<code>space-16</code>'], ['Padding, Large mobile and Medium desktop', '<code>space-12</code>'], ['Padding, Medium mobile and Small desktop', '<code>space-8</code>'], ['Padding, Small mobile', '<code>space-4</code>'], ['Padding, XSmall', '6px: literal, no spacing token'],
                                                                                                                                                        ['Label inset', '<code>space-8</code> (Large, Medium, Small desktop), <code>space-4</code> (XSmall); Small mobile 6px: literal, no spacing token']])

st_states = '<h2 class="ds-h2">States</h2><h3 class="ds-h3 ds-group">Button</h3>' + desc('Every state for every variant. Hover and focus are forced on this page with <code>data-state</code> so they show at the same time; in your code they come from <code>:hover</code> and the keyboard focus rule. The buttons are live (the disabled ones do not respond).') + \
    '<h3 class="ds-h3">What each state means</h3>' + table(['State', 'Description'], [
        ['Enabled', 'The standard state of a button: it is available for interaction and is not currently selected. It includes Hover and Focus of the button type.'],
        ['Hover', 'Shown when the user hovers the cursor over the button, to show that the component is interactive.'],
        ['Focus', 'The visual style shown when the button is reached with the keyboard (often with Tab). It shows that the button is ready to be activated. It is a blue outline (<code>border-focus</code>), so users can move through the interface without a mouse.'],
        ['Disabled', 'A disabled button prevents interaction: hover, focus and click. It is not focusable, so Tab skips it. Screen readers may still announce it as unavailable when the user browses the page. Do not associate a <a class="inline-link inline-link--small" href="tooltip.html">tooltip</a> with a disabled button.'],
        ['Selected', 'Used by the System button in some cases. A selected button has been actively chosen, toggled on, or is the item currently in focus within a group of options. It shows which option is active and confirms that the user’s action was registered.']]) + \
    toolbar([('sb2-l', 'Breakpoint', 'data-bp-toggle', BP_BUTTONS, ' data-bp-force'), ('sm-s', 'Size', 'data-mx="size"', [('lg', 'Large', True), ('md', 'Medium', False), ('sm', 'Small', False), ('xs', 'XSmall', False)])]) + \
    '<div class="ds-table-wrap"><table class="ds-table ds-matrix" id="matrix"><thead><tr><th scope="col">Variant</th><th scope="col">Enabled</th><th scope="col">Hover</th><th scope="col">Focus</th><th scope="col">Disabled</th></tr></thead><tbody></tbody></table></div>' + \
    note('Hover: Primary, Destructive and Accent get a <code>surface-opacity-white-20</code> layer on top of their color, Primary inverted a <code>surface-opacity-black-12</code> layer. Secondary and Blank get <code>surface-opacity-black-05</code>, the inverted ones <code>surface-opacity-white-20</code>. System hover and System selected hover are the same: a <code>surface-opacity-black-12</code> surface and a <code>border-hover</code> frame. The focus ring is a 2px <code>border-focus</code> line with a 2px gap, drawn outside the button. Disabled: Secondary, Secondary inverted and System keep a frame in <code>border-disabled</code> with no fill; Blank has neither; the others get <code>surface-disabled</code>.') + \
    '<h3 class="ds-h3 ds-group">Toggle icons</h3>' + desc('Eight icons. Each has Enabled, Hover, Selected and Selected hover, in Large (24px) and Small (20px).') + \
    toolbar([('ib-s', 'Size', 'data-ib="size"', [('lg', 'Large', True), ('sm', 'Small', False)])]) + \
    '<div class="ds-table-wrap"><table class="ds-table ds-matrix bt-icons" id="ib-matrix"><thead><tr id="ib-head"></tr></thead><tbody></tbody></table></div>' + \
    note('Hover changes the icon color to <code>text-action-primary-hover</code>; there is no surface. Selected hover is the filled icon in that color. Figma has no focus or disabled state for these icons: focus follows the button rule, disabled uses <code>text-disabled</code>. The “cancel” icon is always filled.') + \
    '<h3 class="ds-h3 ds-group">Close</h3>' + \
    '<div class="ds-table-wrap"><table class="ds-table ds-matrix" id="close-matrix"><thead><tr><th scope="col">Version</th><th scope="col">Enabled</th><th scope="col">Hover</th><th scope="col">Focus</th><th scope="col">Disabled</th></tr></thead><tbody></tbody></table></div>' + \
    note('Figma only defines Enabled and Hover for Close. Focus follows the shared rule; disabled is not defined and is not used for a close control.')

st_typo = '<h2 class="ds-h2">Typography</h2>' + table(['Size', 'Type', 'Mobile (below 769px)', 'Desktop (769px+)', 'Font features'], [
    ['Large', '<code>label-lg</code>', '16/16, 0.32px', '18/18, 0.18px', '<code>ss02</code>, <code>ss03</code>'], ['Medium', '<code>label-lg</code>', '16/16, 0.32px', '18/18, 0.18px', '<code>ss02</code>, <code>ss03</code>'], ['Small', '<code>label-md</code>', '14/14, 0.42px', '16/16, 0.48px', 'None'], ['XSmall', '<code>label-sm</code>', '12/12, 0.48px', '14/14, 0.56px', '<code>ss02</code>, <code>ss03</code>']]) + \
    note('Breuer Condensed, weight 600 (Figma bold 700 − 100), uppercase through CSS, so write the label in sentence case in the HTML. The badge number is 12/12 (Large and Medium mobile) or 14/14 (desktop), and 10/10 in Small and XSmall; see the badge sizes under ' + sec_link(SLUG, 'sizes', 'Sizes') + '.')

st_struct = '<h2 class="ds-h2">Structure</h2><h3 class="ds-h3 ds-group">Elements</h3>' + table(['Element', 'Class', 'Notes'], [
    ['Button', '<code>btn</code>', 'A <code>button</code> for actions, an <code>a</code> for navigation.'], ['Label', '<code>btn__label</code>', 'Always wrap the label in it: it carries the label inset. Without it the text sits too close to the edge.'], ['Icon', '<code>btn__icon</code>', 'Material Symbols, <code>aria-hidden="true"</code>.'], ['Badge number', '<code>btn__badge</code>', 'Top right corner, <code>aria-hidden="true"</code>.'], ['Badge dot', '<code>btn__dot</code>', '6px circle, <code>aria-hidden="true"</code>.'],
    ['Icon button', '<code>icon-btn</code>, <code>icon-btn--sm</code>, <code>icon-btn--filled</code>', 'A single icon that is a control. <code>aria-pressed</code> gives the filled icon.'], ['Close', '<code>icon-btn icon-btn--close</code>, <code>icon-btn--close-inverted</code>', '24px box, 20px icon.']]) + \
    '<h3 class="ds-h3 ds-group">Types</h3>' + table(['Class', 'Use'], [['<code>btn--primary</code>, <code>btn--primary-inverted</code>', 'Main call to action. Inverted: the same role, where the standard variant lacks contrast.'], ['<code>btn--secondary</code>, <code>btn--secondary-inverted</code>', 'Second action, with a frame.'], ['<code>btn--blank</code>, <code>btn--blank-inverted</code>', 'The quietest action, no fill and no frame.'], ['<code>btn--destructive</code>', 'Removes something.'], ['<code>btn--accent</code>', 'Brand-colored call to action.'], ['<code>btn--system</code>', 'A toggle in a group of buttons, with <code>aria-pressed</code>.'],
                                                                          ['<code>btn--lg</code>, <code>btn--md</code>, <code>btn--sm</code>, <code>btn--xs</code>', 'Size. Each sets every <code>--btn-*</code> property, in the mobile block and again from 769px.'], ['<code>btn--icon</code>', 'Icon only: a square, needs an <code>aria-label</code>.']]) + \
    '<h3 class="ds-h3 ds-group">Width</h3>' + desc('A button hugs its content. An icon-only button is a square. Full width comes from the page layout, not from a modifier.')

st_motion = '<h2 class="ds-h2">Motion</h2>' + table(['Property', 'Duration', 'Easing'], [['Hover layer: <code>opacity</code> of <code>::before</code>', '<code>duration-fast-2</code> (100ms)', '<code>ease-standard</code>'], ['Focus ring: <code>outline-color</code>', '<code>duration-fast-2</code>', '<code>ease-standard</code>'], ['Frame: <code>box-shadow</code> (System hover frame)', '<code>duration-fast-2</code>', '<code>ease-standard</code>']]) + \
    note('Figma calls this transition “Dissolve”: a custom bezier .35, 0, .35, 1 over 100ms, which is <code>ease-standard</code>. Under <code>prefers-reduced-motion: reduce</code> the transition is turned off.')

st_behavior = '<h2 class="ds-h2">Behavior</h2>' + table(['Input', 'Result'], [
    ['Click, Enter, Space', 'Runs the action. Use <code>&lt;button&gt;</code> for actions and <code>&lt;a class="btn …"&gt;</code> for navigation.'], ['Tab / Shift+Tab', 'Moves between buttons. The focus ring shows only when <code>body.keyboard-nav</code> is set (on Tab, removed on mousedown and touchstart), the same as the form controls.'], ['Disabled', 'Use the <code>disabled</code> attribute. It is not focusable and has no hover. Say why in nearby text when the reason is not obvious.'],
    ['System selected', 'Set <code>aria-pressed="true"</code>. It is a toggle, so it must not be used for page navigation.'], ['Icon only', 'Add <code>aria-label</code>, and hide the icon with <code>aria-hidden="true"</code>.'], ['Label', 'Uppercase through CSS, so write it in sentence case in the HTML. Keep it short and start with a verb.'], ['Icon only tooltip', 'Always with a tooltip, shown after a 300ms hover delay (design guidance). <strong>Open point:</strong> the shared tooltip (<code>components/js/tooltip.js</code>) has no hover delay yet, so it appears at once. Never on a disabled button.']])

st_access = '<h2 class="ds-h2">Accessibility Requirements</h2>' + table(['Topic', 'Requirement'], [
    ['Element', 'A native <code>&lt;button type="button"&gt;</code> for an action, an <code>&lt;a class="btn …"&gt;</code> for navigation. Never a <code>div</code> with a click handler.'], ['Name', 'A visible label, or an <code>aria-label</code> on an icon-only button. A badge is <code>aria-hidden="true"</code>: put the count in the <code>aria-label</code>.'], ['Focus', '2px ring <code>border-focus</code> with a 2px gap, on keyboard use (WCAG 2.4.7, 1.4.11). It is set with <code>body.keyboard-nav</code>, never <code>:focus-visible</code>.'],
    ['State', 'System selected is <code>aria-pressed</code>. A disabled button uses the <code>disabled</code> attribute.'], ['Target size', 'The smallest button is 32px high; Close is 24px, which meets WCAG 2.5.8 (24px) but is below the usual 44px touch target.'], ['Contrast', 'Choose standard or inverted variants by context, visibility and contrast, not by background color alone. Disabled tokens are exempt from contrast requirements.']])

spec = [('design-tokens', st_tok), ('sizes', st_sizes), ('measurements', st_meas), ('states', st_states), ('typography', st_typo), ('structure', st_struct), ('motion', st_motion), ('behavior', st_behavior), ('accessibility-requirements', st_access)]

# ---------------------------------------------------------------- Code
c_basic = '<h2 class="ds-h2">Basic Usage</h2>' + desc('Link the shared stylesheet once per page. Never copy the rules into a page, and never write a parallel version.') + table(['Step', 'What to do'], [
    ['1. Link', '<code>&lt;link rel="stylesheet" href="/components/css/button.css"&gt;</code>. Both templates already have it. The icons need the Material Symbols Outlined font, as in the templates.'], ['2. Markup', 'A <code>button.btn</code> (or <code>a.btn</code>) with a variant and a size class, and the label in <code>span.btn__label</code>.'], ['3. Variant and size', '<code>btn--primary</code>, <code>btn--secondary</code>, … and <code>btn--lg</code>, <code>btn--md</code>, <code>btn--sm</code> or <code>btn--xs</code>. The size switches at 769px by itself.'],
    ['4. Focus ring', 'Add the small script once per page: it sets <code>body.keyboard-nav</code> on Tab.'], ['5. Next to a field', 'Use the matching size: Input Large with Medium, Small with Small, XSmall with XSmall.']])
c_btn = '<h2 class="ds-h2">Button</h2>' + desc('Copy the markup you need. Hover and focus come from <code>:hover</code> and the keyboard focus rule; the <code>[data-state]</code> selectors in the CSS exist only so the documentation can force a state.') + '<div id="recipes"></div>'
c_icon = '<h2 class="ds-h2">Icon button</h2><div id="recipes-icon"></div>'
c_api = '<h2 class="ds-h2">API</h2><h3 class="ds-h3 ds-group">Classes</h3>' + table(['Class', 'Use'], [
    ['<code>btn</code>', 'The button. Needs a variant and a size.'], ['<code>btn--primary</code> | <code>primary-inverted</code> | <code>secondary</code> | <code>secondary-inverted</code> | <code>blank</code> | <code>blank-inverted</code> | <code>destructive</code> | <code>accent</code> | <code>system</code>', 'Variant.'], ['<code>btn--lg</code> | <code>md</code> | <code>sm</code> | <code>xs</code>', 'Size.'], ['<code>btn--icon</code>', 'Icon only: a square. Needs <code>aria-label</code>.'],
    ['<code>btn__label</code>, <code>btn__icon</code>, <code>btn__badge</code>, <code>btn__dot</code>', 'Parts of a button.'], ['<code>icon-btn</code>, <code>icon-btn--sm</code>, <code>icon-btn--filled</code>, <code>icon-btn--close</code>, <code>icon-btn--close-inverted</code>', 'The icon button.']]) + \
    '<h3 class="ds-h3 ds-group">Things to know</h3>' + bullets(['Always wrap the label in <code>span.btn__label</code>, also for buttons built in JS (<code>innerHTML</code>, and set the text on the span, never <code>button.textContent</code>).', 'Breakpoint: the sizes switch at 769px; 640–768px is still mobile.', 'Cap the badge count in your code: <code>n &gt; 99 ? \'99+\' : n</code>.', 'Never <code>:focus-visible</code> for buttons: use <code>body.keyboard-nav</code>.', 'Old prototype pages have their own <code>.btn-primary</code> and <code>.btn-blank</code> classes. New work uses the classes above.', 'The <code>[data-state]</code> selectors do nothing outside the documentation pages.'])
c_css = '<h2 class="ds-h2">CSS / Tailwind</h2>' + desc('The component is one CSS file, shared by every page. Link it, never copy it. The CSS below is read from the file the page links, so it is always what you see.') + code_box('css-code', 'CSS (components/css/button.css, button and icon button)') + \
    '<h3 class="ds-h3">Focus ring script</h3>' + '<div id="recipes-focus"></div>'
code = [('basic-usage', c_basic), ('button', c_btn), ('icon-button', c_icon), ('api', c_api), ('css-tailwind', c_css, False)]

# ---------------------------------------------------------------- scripts
SHARED = old_js('button', "  var VARIANTS = [", "  /* Breakpoint preview (this page only)") + old_js('button', "  /* Build a real button.", "  /* ── Breakpoint preview: one setting")
IBJS = old_js('button', "  var IB = [", "  var ib = { size: 'lg' };")
MATRIX = old_js('button', "  /* ── State matrix ── */", "  /* ── Icon buttons ── */")
ICONS = old_js('button', "  var ib = { size: 'lg' };", "  /* ── Anatomy + size table ── */")

JS_EX = "  var uid = 0;\n" + SHARED + IBJS + old_js('button', "  var pg = {", "  $$('[data-pg]').forEach(function (g) {") + r'''
  DK.wire(pg, renderPg);
  $('#pg-label').addEventListener('input', renderPg);
  $('#pg-count').addEventListener('input', renderPg);
  DK.bp();

''' + old_js('button', "  /* Playground button groups that do not fit", "  /* ── Variants ── */") + old_js('button', "  /* ── Variants ── */", "  /* ── State matrix ── */") + r'''
  /* Sizes */
  var vsz = clear($('#v-sizes'));
  ['lg', 'md', 'sm', 'xs'].forEach(function (s) {
    var r = row(SIZE_NAME[s]);
    r.appendChild(btn({ variant: 'primary', size: s, label: 'Button label' }));
    r.appendChild(btn({ variant: 'secondary', size: s, content: 'lead', label: 'Button label' }));
    r.appendChild(btn({ variant: 'primary', size: s, content: 'icon', aria: 'Add to cart' }));
    vsz.appendChild(r);
  });

  /* Icon buttons */
  var vib = clear($('#v-ib'));
  IB.forEach(function (x) { vib.appendChild(ibtn({ glyph: x[1], filled: x[2], aria: x[0], pressed: false })); });
  clear($('#v-close')).appendChild(ibtn({ glyph: 'close', aria: 'Close', cls: 'icon-btn--close' }));
  clear($('#v-close-inv')).appendChild(ibtn({ glyph: 'close', aria: 'Close', cls: 'icon-btn--close icon-btn--close-inverted' }));

  /* Usage figures */
  var fp = clear($('#fig-p-do')); fp.appendChild(btn({ variant: 'primary', size: 'md', label: 'Save' })); fp.appendChild(btn({ variant: 'secondary', size: 'md', label: 'Cancel' }));
  var fq = clear($('#fig-p-dont')); fq.appendChild(btn({ variant: 'primary', size: 'md', label: 'Save' })); fq.appendChild(btn({ variant: 'primary', size: 'md', label: 'Cancel' }));
  clear($('#fig-l-do')).appendChild(btn({ variant: 'primary', size: 'md', label: 'Add to cart' }));
  clear($('#fig-l-dont')).appendChild(btn({ variant: 'primary', size: 'md', label: 'Click here to add to cart' }));
  clear($('#fig-v-do')).appendChild(btn({ variant: 'primary', size: 'md', label: 'Request booking' }));
  clear($('#fig-v-dont')).appendChild(btn({ variant: 'primary', size: 'md', label: 'Submit' }));
  clear($('#fig-x-do')).appendChild(btn({ variant: 'destructive', size: 'md', label: 'Delete project' }));
  clear($('#fig-x-dont')).appendChild(btn({ variant: 'destructive', size: 'md', label: 'Confirm' }));
  clear($('#fig-a-do')).appendChild(btn({ variant: 'primary', size: 'md', label: 'Add to cart' }));
  clear($('#fig-a-dont')).appendChild(btn({ variant: 'accent', size: 'md', label: 'Add to cart' }));
  clear($('#fig-d-do')).appendChild(btn({ variant: 'primary-inverted', size: 'md', label: 'Shop now' }));
  clear($('#fig-d-dont')).appendChild(btn({ variant: 'primary', size: 'md', label: 'Shop now' }));

  /* Anatomy */
  var ah = clear($('#a-host')), ab = btn({ variant: 'primary', size: 'lg', content: 'lead', label: 'Button label', badge: 'number', count: '3' });
  ab.tabIndex = -1; ah.appendChild(ab);
  DK.callouts($('#bt-anat'), [
    { n: 1, el: ab, side: 'left', len: 56, at: 'edge' },
    { n: 2, el: $('.btn__icon', ab), side: 'top', len: 48, at: 'center' },
    { n: 3, side: 'bottom', len: 48, at: 'center', box: function () { var r = document.createRange(); r.selectNodeContents($('.btn__label', ab)); return r.getBoundingClientRect(); } },
    { n: 4, el: $('.btn__badge', ab), side: 'right', len: 48, at: 'edge' }
  ]);
  var ah2 = clear($('#a-host2')), ab2 = btn({ variant: 'primary', size: 'lg', content: 'icon', badge: 'dot', aria: 'Cart, new items' });
  ab2.tabIndex = -1; ah2.appendChild(ab2);
  DK.callouts($('#bt-anat2'), [
    { n: 1, el: ab2, side: 'left', len: 56, at: 'edge' },
    { n: 2, el: $('.btn__icon', ab2), side: 'bottom', len: 48, at: 'center' },
    { n: 3, el: $('.btn__dot', ab2), side: 'right', len: 48, at: 'edge' }
  ]);
  renderPg(); buildVariants();
  (function () {
    var c = clear($('#fig-c1')), r = document.createElement('div'); r.className = 'bt-pair';
    r.appendChild(btn({ variant: 'secondary', size: 'md', label: 'Shop women' })); r.appendChild(btn({ variant: 'secondary', size: 'md', label: 'Shop men' })); c.appendChild(r);
    var hr = document.createElement('hr'); hr.className = 'divider'; c.appendChild(hr);
    var r2 = document.createElement('div'); r2.className = 'bt-pair';
    [['Select all', 'select_all'], ['Deselect all', 'deselect']].forEach(function (x) { var b = btn({ variant: 'system', size: 'sm', content: 'trail', label: x[0] }); $('.btn__icon', b).textContent = x[1]; r2.appendChild(b); });
    c.appendChild(r2);
  })();
  (function () {
    var host = $('#v-pairs');
    function pair(list) { var d = document.createElement('div'); d.className = 'bt-pair'; list.forEach(function (b) { d.appendChild(btn({ variant: b[0], size: 'md', label: b[1] })); }); host.appendChild(d); }
    pair([['primary', 'Save changes'], ['secondary', 'Edit'], ['blank', 'Cancel']]);
  })();
'''

JS_SPEC = "  var uid = 0;\n" + SHARED + IBJS + MATRIX + ICONS + r'''
  var SZ = Object.keys(SIZES);
  var st = $('#size-table tbody');
  SZ.forEach(function (s) {
    [['d', 'Desktop (769px and up)'], ['m', 'Mobile (below 769px)']].forEach(function (b) {
      var v = SIZES[s][b[0]], tr = document.createElement('tr'), th = document.createElement('th'); th.scope = 'row'; th.textContent = SIZE_NAME[s] + ' · ' + b[1]; tr.appendChild(th);
      [v.h + 'px', v.pad + 'px', v.tx + 'px', v.icon + 'px', '<code>' + v.style + '</code> ' + v.fs + '/' + v.lh + ', ' + v.ls + 'px'].forEach(function (t) { var td = document.createElement('td'); td.innerHTML = t; tr.appendChild(td); });
      st.appendChild(tr);
    });
  });
  var bt = $('#badge-table tbody');
  SZ.forEach(function (s) {
    [['d', 'Desktop'], ['m', 'Mobile']].forEach(function (b) {
      var v = SIZES[s][b[0]], x = v.bd, tr = document.createElement('tr'), th = document.createElement('th'); th.scope = 'row'; th.textContent = SIZE_NAME[s] + ' · ' + b[1]; tr.appendChild(th);
      [x.off + 'px' + (x.offIcon ? ' (icon only ' + x.offIcon + 'px)' : ''), x.h + 'px', x.px + 'px', x.fs + 'px' + (x.ls ? ', ' + x.ls + 'px' : ''), v.dot + 'px'].forEach(function (t) { var td = document.createElement('td'); td.textContent = t; tr.appendChild(td); });
      bt.appendChild(tr);
    });
  });
''' + old_js('button', "  var TOK = [", "  var cs = getComputedStyle") + r'''
  DK.tokenTable($('#tok-table tbody'), TOK);
  DK.bp(function () { if (window.ECO_MEASURE) ECO_MEASURE.init(); });
  buildMatrix(); buildIcons();
'''

JS_CODE = old_js('button', "  var RECIPES = [", "  var rh = $('#recipes');") + r'''
  var ICN = RECIPES.filter(function (r) { return /^(Icon button|Close)/.test(r[0]); });
  var FOC = RECIPES.filter(function (r) { return /^Focus ring/.test(r[0]); });
  var BTN = RECIPES.filter(function (r) { return ICN.indexOf(r) < 0 && FOC.indexOf(r) < 0; });
  DK.recipes($('#recipes'), BTN); DK.recipes($('#recipes-icon'), ICN); DK.recipes($('#recipes-focus'), FOC);
  DK.printCss($('#css-code'), 'button', [[/:is\(:hover, \[data-state="hover"\]\)/g, ':hover'], [/,\n    \.btn\[data-state="focus"\]/g, ''], [/,\n    \.icon-btn\[data-state="focus"\]/g, ''], [/^ {4}/gm, '']]);
'''

C = dict(
    slug=SLUG, title='Button', eyebrow='Components · Actions',
    lead='A button <strong>triggers an action</strong> or <strong>takes the user to another page</strong>. It lets the user make a choice with a single tap. Use a mix of styles on one page to point at the main action and still offer the alternatives.',
    lead_ex='Every example on this page is the real component, not a picture. Click, hover and press Tab to try it. Specification: <code>.claude/skills/eco-button/SKILL.md</code>. Figma: ' + FIGS + '.',
    lead_spec='Tokens, sizes, measurements, states and requirements. Values come from the live token package and from Figma: ' + FIGS + '.',
    lead_code='How to add a button to a page. The file is <code>components/css/button.css</code>.',
    css=['menu'], head_extra='\n  <link rel="stylesheet" href="../notifications.css?v=16">', style=STYLE, ex=ex, spec=spec, code=code, js_ex=JS_EX, js_spec=JS_SPEC, js_code=JS_CODE)

if __name__ == '__main__':
    emit(C)
