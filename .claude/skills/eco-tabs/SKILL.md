---
name: eco-tabs
description: Use when building or reviewing tabs — a tab bar of Primary or Secondary tab items that switches content in the same context, or serves as sub-navigation (e.g. the My Pages account nav), or navigates the sections of one long page (on-page navigation, `tab-bar--page`). Sizes (Large/Medium/Small), configurations (label, label + icon, icon only), states (enabled/hover/active), dot and number status, overflow. Not for sequential steps (use a stepper), not for a two-view toggle (use eco-pill-segment-control), not for choosing form values (use eco-radio / eco-select).
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Tabs (ECO Design System)

**Figma:** Tab Base Item `3034:330049`, Tab Items `2166:63997`, Tab Bar sizes `2515:77815`, Tab info `3521:126512` (file `42MgqJjV9vfplwQnrUB62r`).

Documentation: `eco-design-system/components/tabs.html`, `tabs-specifications.html`, `tabs-code.html` (three pages, see `eco-doc-page`). Shared files, link them, never copy:

```html
<link rel="stylesheet" href="/components/css/tabs.css">
<script src="/components/js/tabs.js"></script>   <!-- sliding line for all bars (content and link tabs) -->
```

### When to use / not to use

- Tabs organise content across screens, data sets and interactions at the **same level of hierarchy**. They control the region shown below them.
- Not for content that must be read in a fixed order: use a stepper (`Steps`).
- **Primary** tabs: top of a content page, as sub-navigation when the main navigation needs further levels, or as top-level navigation where there is no main navigation (campaign pages). They show the main content destinations.
- **Secondary** tabs: always **below** primary tabs, if any. They separate related content inside an area (a card, a sheet, an info pane, a carousel with categories, sections on one page, a brand page).
- Standalone icons (icon only): use only icons that are globally well known. Give each an `aria-label`.
- Labels sit in one row. A second line (with truncation) is allowed, but **scrollable tabs are preferred** for long titles. When the tabs exceed the viewport (e.g. at `xs`) the divider line runs the full width, left to right.
- Not for: a two-view or filter toggle (`eco-pill-segment-control`), joined option buttons (`eco-button`, Button group), a value chosen in a form (`eco-radio`, `eco-select`).

### Choosing Primary or Secondary

The same method is a chooser on the docs page (`tabs.html` → Usage → Primary or Secondary): up to five questions, the answer shows the type, why, and a live example. Ask in this order and take the first answer that decides it:

1. **Must the content be read in a fixed order?** Yes → not tabs: use a stepper (`Steps`; no ECO page yet).
2. **Are they views or filters of the same content (a list and a grid, all and key)?** Then **how many?** Two to four, and it stays so → not tabs: use `eco-pill-segment-control`. More, or the number is unknown and may grow → tabs (a tab bar has no upper limit: it scrolls sideways); carry on with 3.
3. **What do the tabs switch: the whole page, or one area of it?**
   - **The whole page → Primary.** With a main navigation they are sub-navigation (the main navigation divided into subcategories or pages); without one they are the top-level navigation (campaign pages). They show the main content destinations.
   - **One area of it → Secondary.** A card or a sheet, an information pane, a carousel with categories, or the sections of one page (an article with titles, a campaign page, a brand page). They establish hierarchy and control the region shown below them.
4. **Does the page already have primary tabs?** Then the secondary tabs go below them, never above, and there are never more than two levels.

Placement summary: Primary = top of the content page, one bar per page, 24px between tabs, line as wide as the label, active line 3px. Secondary = inside the area it controls (below the primary tabs when there are any), one per area, 16px padding on each side of a tab, line wider than the label, active line 2px.

### On-page navigation (`tab-bar--page`)

Secondary tabs can navigate a whole page, as the on-page tab bar of the docs does. **Any number of sections**: the bar scrolls sideways and keeps the current tab in view.

```html
<nav class="tab-bar tab-bar--secondary tab-bar--md tab-bar--page" aria-label="On this page">
  <a class="tab" href="#overview"><span class="tab__label">Overview</span></a>
  <a class="tab" href="#dimensions"><span class="tab__label">Dimensions</span></a>
  <!-- … one link per section, no limit -->
</nav>
<section id="overview">…</section>
<section id="dimensions">…</section>
```

- **Opt in with `tab-bar--page`.** Other link bars with `#anchor` hrefs are left alone (the docs' own on-page bar is handled by `subnav.js`).
- **Sticky.** The bar sticks to the top. Set `--tab-sticky-top` on it when a fixed header sits above (default `0px`). Background `--tab-bar-bg` (default `--color-background-primary`; `tab-bar--on-grey` uses `--color-background-secondary`); `--tab-sticky-z` (default 2).
- **Scrollspy.** The current tab is the last section whose top is above a line 25% down the visible area; at the end of the page the last section. It gets `aria-current="location"` and the line slides to it.
- **Click.** Scrolls so the section starts under the bar (plus the section's `scroll-margin-top`): 150 / 200 / 300 / 450 ms by distance (`duration-fast-3`, `fast-4`, `medium-2`, `slow-1`), `ease-decelerate-generic`; instant under reduced motion; wheel, touch or a key stops it. Focus moves to the section (`tabindex="-1"`) and the `#hash` is added with `pushState`. `data-tabs-hash="off"` keeps the address.
- **Scroll box.** If the sections sit in a scrolling element (a card, a pane), the nearest scrollable parent of the sections is used instead of the window.
- Secondary tabs only by design; the sections are the content of one page, never more than two levels of tabs.

### Anatomy

`.tab-bar` (the row + 1px divider `--color-border-primary`) holds `.tab` items. A tab has an optional `.tab__icon` (20px, above the label), a `.tab__label` (uppercase, optional leading 24px icon, `.tab__dot` or `.tab__count` after the text, optional leading icon before it) and an indicator line (the `::after`) along the bottom edge.

| Modifier | Effect |
|---|---|
| `.tab-bar--primary` | 24px gap between tabs (`--dimension-spacing-space-24`); indicator spans the label only; active line 3px |
| `.tab-bar--secondary` | no gap, each tab has 16px side padding (`--dimension-spacing-space-16`), indicator spans label + padding; active line 2px |
| `.tab-bar--md` / `.tab-bar--sm` | size Medium / Small. Default (no class) = Large |
| `.tab-bar--on-grey` | Background Colored = True: hover line `--color-surface-40` instead of `--color-surface-10` |
| `.tab--icon-only` | icon only, indicator under the icon; dot sits at the icon's top right |
| `.tab--active` | or `aria-selected="true"` / `aria-current` (all three give the active look) |

### Size model

Height of one tab = icon 20 + 8 gap + label line + gap + 2 indicator. Switches at `md` (769px); `sm` (640–768px) is mobile.

| Size | Mobile (≤768px) label | Gap label→line | Desktop (`md:`) label | Gap |
|---|---|---|---|---|
| **Large** | `label-lg` mobile 16/16, 0.32px | 10px | `label-lg` 18/18, 0.18px | 12px |
| **Medium** | `label-lg` mobile 16/16, 0.32px | 8px | `label-lg` 18/18, 0.18px | 12px |
| **Small** | `label-md` mobile 14/14, 0.42px | 8px | `label-md` 16/16, 0.48px | 8px |

Resulting tab heights (label + icon): Large 56 / 60, Medium 54 / 60, Small 52 / 54. Label-only bar heights incl. the 1px divider: Large 29 / 33, Medium 27 / 33, Small 25 / 27. Icon only: tab 30px (34px desktop Large/Medium), gap icon→line 8px (12px desktop Large/Medium).

### Typography

Breuer Condensed, weight `600` (Figma bold 700 − 100), uppercase, `font-feature-settings: 'ss02' 1, 'ss03' 1`. Styles from `eco-typography` (`label-lg`, `label-md`) as in the table above. Number badge text: 10px/10px.

### States

| State | Label | Icon | Indicator line |
|---|---|---|---|
| **Enabled** | `--color-text-primary` | `--color-text-secondary` | none (only the bar divider) |
| **Hover** | `--color-text-tertiary` | `--color-text-tertiary` | 3px `--color-surface-10` (`--color-surface-40` on grey) |
| **Active** | `--color-text-primary` | `--color-icon-primary` | `--tab-line-active` (default `--color-surface-100`, black; set it to the accent colour where the product uses it, see **Accent colour** below); Primary 3px, Secondary 2px |
| **Focus** (keyboard, on any state: Focus / Active Focus / Enabled Focus) | unchanged (an enabled tab stays `--color-text-primary`, not the hover grey) | unchanged | unchanged and still visible below the ring |

**Focus ring** (Figma Focus, Active Focus, Enabled Focus; same principle for every variant): 2px solid `--color-border-focus`, square corners, drawn by `.tab::before` around icon + label: 4px clear above, left and right (ring 8px wider than the tab: Primary 36 → 44, Secondary 68 → 76), bottom 6px above the tab's bottom edge so the indicator line stays outside the ring. Shown on `:focus-visible` (and `data-state="focus"` for docs). The bar has `padding: 4px 4px 0; margin: -4px -4px 0` so the scroll container does not clip the ring and nothing shifts.

**Accent colour** (the active line only; the Examples page has a Black / Swedol / Tools toggle in the Playground and an Accent colour block under Variants): the line is black by default. Set `--tab-line-active` on the bar to the product's accent. Swedol: `var(--color-accent-default)` (`#c7d300`). Tools is a primitive in the token package: `--color-primitive-color-brand-tools-accent-brand` (`#cd1125`). The My Pages prototype pages use `var(--brand)`, their own alias of the Swedol accent. Works for Primary and Secondary, content tabs and link tabs. The grey hover line and the grey line under the arriving tab do not change with the accent. Never restyle `.tab::after` or `.tab-bar__indicator`.

Status (Figma Tab Bar sizes, label-only bars): `.tab__dot` 6px circle and `.tab__count` red pill with a number (16px high, 10px text, no letter-spacing) sit after the label text with a 4px gap; both `--color-surface-danger-default`, count text `--color-text-primary-inverted`. An optional leading icon (`<span class="ms">`, 24px; 20px on Small below 769px) sits before the label text, 4px gap. `.tab__label` is locked to the line height, so the icon overflows evenly and neither the tab height nor the label position changes.

Motion: content tabs (`role="tablist"`): when another tab is clicked or reached by keyboard, the active line **slides** to it (one `.tab-bar__indicator` per bar, added by `tabs.js`; `transform` + `width`, `--duration-medium-2`, `--ease-standard`; none under `prefers-reduced-motion`). The bar gets `data-slide`, which hides the per-tab active line. Link tabs (`<nav class="tab-bar">` with `<a class="tab">`, a page load per tab) slide across the page change: a click adds `.tab--pending` (keeps the hover label and the hover line `surface-10` while the next page loads) and stores the index of the tab that was active in `sessionStorage` (5 s); on the new page `tabs.js` puts the line under that tab, then slides it to the new `aria-current` tab. Needs the same `aria-label` on the bar on every page (it is the storage key; or set `data-tabs-id`). Modified clicks (Ctrl, Cmd, Shift, middle button, `target="_blank"`) do nothing special. The tab the line travels to keeps its grey hover line (`.tab--arriving`, set by `tabs.js`) until the sliding line has arrived. Across a page change `tabs.js` also sets `html.tabs-arrive` while `<head>` is parsed (so `tabs.js` must be in `<head>`), which makes the new `aria-current` tab grey from the first paint, before the script runs and before the line is placed, on content tabs and across a page change alike. Hover line: grows from the bottom (`scaleY`, `--duration-medium-2`, `--ease-decelerate-generic`), line colour fades in `--duration-medium-2` `--ease-standard`. Label and icon colours change instantly (same behaviour as the original My Pages nav: only the line animates, from `scaleY(0)` to `scaleY(1)`). The Secondary active line is the same 3px element at `scaleY(0.6667)` = 2px.

### HTML structure

Content tabs (switch panels on the same page): `role="tablist"` + buttons. `tabs.js` handles click, Left/Right (wraps), Home/End and shows the panel named by `aria-controls`. Selected tab `tabindex="0"`, others `-1`.

```html
<div class="tab-bar tab-bar--primary" role="tablist" aria-label="Product information">
  <button class="tab tab--active" role="tab" id="t1" aria-selected="true" aria-controls="p1">
    <span class="ms tab__icon" aria-hidden="true">construction</span>
    <span class="tab__label">Overview</span>
  </button>
  <button class="tab" role="tab" id="t2" aria-selected="false" aria-controls="p2" tabindex="-1">
    <span class="ms tab__icon" aria-hidden="true">construction</span>
    <span class="tab__label">Details <span class="tab__count">1</span></span>
  </button>
</div>
<div class="tab-panel" role="tabpanel" id="p1" aria-labelledby="t1">…</div>
<div class="tab-panel" role="tabpanel" id="p2" aria-labelledby="t2" hidden>…</div>
```

Navigation tabs (each goes to a page, e.g. My Pages account nav): plain links, current page = `aria-current="page"`. Link `tabs.js` too: it slides the line from the previous tab to the new one across the page load. Keep the same `aria-label` on the bar on every page.

```html
<nav class="tab-bar tab-bar--secondary" aria-label="Account">
  <a class="tab" href="/mypages/users.html" aria-current="page"><span class="tab__label">Users</span></a>
  <a class="tab" href="/mypages/addressbook.html"><span class="tab__label">Address book</span></a>
</nav>
```

Icon only: `<button class="tab tab--icon-only" role="tab" aria-label="Settings">` with just the `.tab__icon` (and `<span class="tab__dot">` for status). The icon class `.ms` (Material Symbols) comes from the page, as in the templates.

### Rules

1. Always link `/components/css/tabs.css`, never copy the rules into a page. Changing tabs = editing that file.
2. Tokens only (`var(--…)`), no hex/px for colour or spacing (CLAUDE.md rule 6). Mobile-first; the switch is at `769px`, `sm` looks like mobile.
3. Tabs are `<button role="tab">` (content tabs) or `<a>` (navigation). Never a `div` with a click handler. Keep exactly one active tab.
4. Secondary tabs go below primary tabs, never above.
5. Prefer scrollable tabs (the bar scrolls sideways, scrollbar hidden) over wrapping or hiding tabs. Keep the active tab in view (`tabs.js` does `scrollIntoView`).
6. Icon-only tabs need an `aria-label`. Status dot/number needs a text alternative where the meaning is not clear from context.
7. Test at ~375px, ~700px and ≥1024px with `getComputedStyle`, and with real hover and keyboard (Tab, arrows).

### On-page navigation (docs)

Link tabs whose `href` is an `#anchor` work as an on-page nav (`eco-design-system/toc.js`, `data-subnav="tabs"`, see `eco-doc-page`): `tabs.js` does not add the pending look or keep a previous position for them, and a script that moves `aria-current` (a scrollspy) makes the line slide to the new tab (a `MutationObserver` on `aria-current` in link bars). The doc pages set the line to the ECO DS accent (`--ds-accent`, `#E94E19`) on that bar; it is a docs colour, products use `--tab-line-active` as above.

### Flags for design

- **Large = Medium on desktop** in Figma (same 18px label, 12px gap, same heights). Mobile differs only in the gap (10 vs 8px). Intended, or should Medium be smaller?
- **Primary active line is 3px, Secondary active 2px** in Figma (Primary variants carry "Black 3px", Secondary "Black 2px"). Implemented as in Figma.
- **No disabled state** in Figma, so none is built.
- **Enabled icon colour** is not bound to a token in the Figma export (renders `#4f4f4f`). Mapped to `--color-text-secondary`; there is no `icon-secondary` token. Hover icon colour is assumed equal to the hover label colour.
- **Enabled line**: Figma has a hidden line in `--color-text-disabled`, clipped by the bar. Rendered as nothing; the 1px bar divider shows.
- **Focus ring height**: Figma frames are 55px (Active Focus) and 56px (Enabled Focus, Secondary Focus); implemented as 56px. Figma clips the indicator line inside the focus frame; decided: the indicator stays visible below the ring (the active tab stays readable while focused). Focus frames exist for Label & Icon only (also Background Colored); icon-only follows the same principle, not drawn in Figma.
- **Divider overhang**: because of the focus-ring room the bar's divider sticks out 4px past the content column on each side.
- **Bar width**: Figma bars hug their content (the divider ends at the last tab). Implemented as full width, per the info text for overflow. Say if hugging is wanted.
- **My Pages account nav is migrated** (`mypages-template`, `users`, `users_V1`, `users-dashboard`, `addressbook`, `dashboard_test`): `<nav class="tab-bar tab-bar--primary" aria-label="Kontomeny">` of `<a class="tab">`, active = `aria-current="page"`, active line brand coloured via `--tab-line-active: var(--brand)` (Swedol and Tools set `--brand`), line 12px under the label (was 15px). Only Adressbok and Användare have pages; the others are placeholders (`href="#"`, `tabs.js` ignores them). Each page still carries its own overflow "more" menu script (`.tab-more…`, not part of the component). The nav has its own divider, so the bar's divider is off there (`border-bottom: 0`). The label (not label + line) is centred in the 48px row, level with the more button: `align-self: flex-start; margin-top: 11px` on the bar (label centre = 4px bar padding + half the 18px line). `partials/account-nav-drawer.html` reads `.account-nav .tab-bar .tab` and `aria-current`.
- **Overflow "more" button** (`more_vert`, Figma `showMoreButton`) is not built. The existing My Pages bar has its own overflow menu (`.tab-more…` in `mypages/mypages-template.html`); migrate it when My Pages moves to this component.
- **Status and leading icon** are drawn in Figma only on the label-only bars (all sizes, Primary and Secondary). Confirmed: dot and number also sit after the label on a label + icon tab; the leading icon is 24px, except Small on mobile (below 769px): 20px. Figma places the leading icon a few px lower than the label (auto-layout artefact); built centred, confirmed. Not tested: leading icon together with an icon above the label.
- The active line is black by default (Figma) and accent coloured where a product sets `--tab-line-active` (see **Accent colour**). No contrast check is made: a light accent such as the Swedol lime is a line, not text, but on white it is low contrast. Say if a darker variant (`accent-dark`) should be offered.
- Primitives `#d90000` (dot/count) = `--color-surface-danger-default`; `Black 3px` primitives map to `--color-surface-100`.
