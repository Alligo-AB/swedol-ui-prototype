---
name: eco-tooltip
description: Use when adding a tooltip to an icon button or other element with no visible text — shown on hover and on keyboard focus (:focus-visible), Esc hides it. Add data-tooltip="Label" (global tooltip, components/js/tooltip.js); never write a tooltip script of your own. Also the rules for when to use one and when not to (critical information, interactive content).
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Tooltip (ECO Design System)

**Figma:** https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=316-14656

Tooltips are usually documented as part of the component they belong to, not as standalone components. The only exception is the Definition Tooltip, which has its own documentation (not in this repo). Use one only when needed, to give quick context without cluttering the interface. The docs page shows the rules below with live examples: `eco-design-system/components/tooltip.html` (Overview). A draft of the split structure (Examples & Guidelines / Specifications / Code) is in `tooltip-new.html`, `tooltip-new-specifications.html`, `tooltip-new-code.html`; not adopted yet, the old page stays the reference.

### Anatomy

1. **Container**: the box that holds the label (surface-100 at 90% opacity, `elevation-b-40`).
2. **Label**: short text, one to three words, that names the trigger.
3. **Caret**: the beak, pointing at the center of the trigger, 4px from it. The Body type has none.
4. **Trigger**: the element the tooltip belongs to, usually an icon button.

The docs page shows the numbered diagram (Overview → Anatomy).

### When to use

Most components (Icon Buttons, Icon Tabs, Sliders, Copy Buttons) already include a built-in tooltip. In most cases there is no need to add one separately; customizing it is possible but generally not recommended. Use a tooltip to:

- show the name of a control that has no visible label
- provide helpful information about a focusable element
- give additional context or explanation when needed
- define a term or explain an inline item, with a **Definition Tooltip**: for labels, words in paragraphs and compact interfaces such as data tables, where extra icons would clutter

### When not to use

- **Critical information.** Never for information the user needs to complete a task. A tooltip disappears when the user moves away and is easily missed. Use always-visible helper text instead, especially for instructions and required fields.
- **Interactive content.** Never put buttons, links or images inside a tooltip: a tooltip cannot receive focus. If the user must interact with the extra content, use a Toggletip (TBA), which has proper focus management and keyboard navigation.
- Keep the text succinct and directive ("Edit", not a sentence).

### Positioning

**Alignment.** The tooltip container can be aligned to the start, center or end of its trigger, automatically or manually. This keeps the tooltip visible and stops it covering important content. The trigger and the caret (beak) are aligned with each other so the connection is clear, especially when several interactive elements sit close together. Start/end = `tooltip--top-start` / `--top-end` (above) and `tooltip--bottom-start` / `--bottom-end` (below); center = `tooltip--top` / `--bottom`. The docs page shows the three alignments side by side (Overview → Positioning).

**Placement.** Tooltips can sit on the top, right, bottom or left side of the trigger (`tooltip--top`, `--right`, `--bottom`, `--left`). Always keep the tooltip visible and never cover content the user needs for the task. For definition tooltips, do not cover the surrounding text, especially the words right before and after the trigger word. When active, the tooltip appears above other content and stays fully visible: not clipped by nearby components and not extending beyond the viewport. Tooltips use auto placement by default (Top and Bottom, see below). The docs page shows the four placements (Overview → Positioning → Placement).

**Automatic alignment (default for `tooltip--top` and `tooltip--bottom`):** the tooltip is centered on its trigger. When a centered tooltip would leave the viewport sideways (8px margin) `tooltip.js` adds `tooltip--align-start` / `--align-end`: the same geometry as the Start/End types under Positioning (beak 16px from the tooltip's edge, on the trigger's center, so the tooltip lines up with the trigger's outer edge). The beak is a fixed child `::before` anchored to the trigger, so it always points at the trigger's center. Add `tooltip--manual` to keep it fixed and centered. **Above/below flip:** `components/js/tooltip.js` (link it on a page with tooltips) adds `tooltip--flip` when a Top/Bottom tooltip opens (`pointerover` on `.tooltip-wrap`) with too little room on its side and more on the other; the beak flips with it. A page with a sticky header sets `--tooltip-safe-top` (px, its height) on `:root`, so room above counts from below the header (done on `mypages/users*.html`, from 769px). Not done in CSS: `position-try-fallbacks: flip-block` was tried and removed, because Chrome decides the fallback from the layout-time scroll position, so on a page that scrolls the tooltip flips wrongly and stays flipped. Without the script the tooltip stays on its declared side (Bottom in toolbars, Top in table rows). CSS anchor positioning (`position-area`, `anchor-scope`) inside `@supports`; the tooltip becomes `position: fixed`, so a clipping container cannot cut it off (but a `transform` on an ancestor makes fixed relative to that ancestor). Without support it stays manual and centered. Start/end/left/right types are always manual. Layer: `z-index: var(--tooltip-z, 300)`; a page with a sticky header sets `--tooltip-z` below the header's z-index (done on `mypages/users*.html`, `:root { --tooltip-z: 98 }`) so a tooltip never paints over the menu. These pages no longer carry their own copy of the `.tooltip` CSS: they use the shared file. A page must not position a tooltip with its own script (inline `left`/`transform`): if it really must keep a fixed tooltip, use `tooltip--manual`; no page does at the moment. Also listed on the docs page (Specs → Behavior and accessibility).

Tooltips show on hover over icon-only buttons and give a short label explaining the button's function. Used at **all** breakpoints.

---

### Sizes

| Size | Padding | Font | Line-height | Letter-spacing |
|---|---|---|---|---|
| **Small** | `8px 16px` | 14px, Regular | 20px | 0.36px |
| **Large** (`tooltip--lg`) | `12px 16px` | 18px, Regular | 26px | 0.36px |

> Always use **Small** for icon buttons in toolbars and table rows.

---

### Width

`width: max-content` (one line when the text fits, so a short label is as wide as its text) and `max-width: min(280px, 100vw − 16px)`: longer text wraps, left aligned, and the tooltip never gets wider than 280px or the viewport minus the 8px edge margin. 280px is the maximum the pages' wrapping tooltips already used; it is not in Figma. Keep the text to 1–3 words: a tooltip that wraps belongs in helper text. A page must not set its own `width`/`white-space` on `.tooltip`. The old `tooltip--wrap` modifier (280px max, 220px min) is gone: its pages (`e-handelspartner.html`, `feature-comparison-roles*.html`) now use `data-tooltip` on the role name, so the width comes from this rule.

### Appearance

| Property | Value |
|---|---|
| Background | `rgba(0,0,0,0.9)` (`surface-100` at 90% opacity) |
| Text color | `var(--color-text-primary-inverted)` (`text-primary-inverted`) |
| Font | `Breuer Condensed Regular` |
| `font-feature-settings` | `'ss02' 1, 'ss03' 1, 'ss06' 1` |
| `white-space` | `nowrap` |
| Shadow | `elevation-b-40`: `var(--shadow-elevation-b-40)` |
| Beak | CSS triangle, 6px tall, ~12.7px wide |
| Distance | The tip of the beak is **4px** from the element (`--dimension-spacing-space-4`), so the tooltip block sits 10px away (6px beak + 4px). |

---

### Global tooltip (`data-tooltip`) — the default for buttons

Add `data-tooltip="Label"` (and `aria-label` with the same text) to any element. `components/js/tooltip.js` shows ONE shared tooltip for it: a popover in the top layer (no `overflow`, `z-index` or stacking context can clip or hide it), centered on the element, sliding along the screen edge, flipping above/below by the room left at the moment it opens. Works for elements added later (delegated events). `data-tooltip-position="bottom"` puts it below (default above): Bottom in toolbars, Top in table rows. Plain text only. Hover only; on touch it shows on tap. Implementation: `.tooltip--global` in `tooltip.css`; the element being hovered gets `anchor-name: --tooltip-global`. Without anchor positioning the script centers it with inline `left`/`top`.

Use the markup form (`.tooltip-wrap` > `.tooltip`) only when you need a type the global one does not have (start, end, left, right, Large, Body) or the tooltip is part of the page markup.

**Never write a tooltip script or `.tooltip`/`.row-tooltip` CSS of your own on a page.** Replace one: delete it, keep the `data-tooltip` attributes, add `data-tooltip-position="bottom"` where the old one opened below. Done on the users pages, addressbook and reviews. Also migrated: `mypages/addressbook.html`, `reviews.html`, `reviews_backup_2.html`, `e-handelspartner.html`, `feature-comparison-roles.html`, `feature-comparison-roles_backup.html` (role-name info tooltips: `data-tooltip` + `data-tooltip-position="bottom"` on `.compare-role-col__name`; the anchor is the whole name block, not the info icon). No page has its own tooltip script any more; a new one must not add one. `template.html` and `mypages/mypages-template.html` link `tooltip.css` and `tooltip.js`.

The docs page describes all of this for developers (Code section: steps, settings table, things to know).

---

### Positions

| Type | Description | Beak direction |
|---|---|---|
| **Top** | Tooltip above the element | Beak points down (below the tooltip block) |
| **Bottom** | Tooltip below the element | Beak points up (above the tooltip block) |
| **Left** | Tooltip to the left | Beak points right (right side of the tooltip) |
| **Right** | Tooltip to the right | Beak points left (left side of the tooltip) |

> **Figma names the beak side, not the placement.** CSS class = where the tooltip sits next to the element. All built in `tooltip.css`, Small and (`tooltip--lg`) Large:
>
> | Figma type | Class |
> |---|---|
> | Body (no beak) | `tooltip--body` |
> | Bottom / Bottom Left / Bottom Right | `tooltip--top` / `--top-start` / `--top-end` |
> | Top / Top Left / Top Right | `tooltip--bottom` / `--bottom-start` / `--bottom-end` |
> | Left Middle / Right Middle | `tooltip--right` / `--left` |
> | Left Top / Right Top (Small only) | `tooltip--right-start` / `--left-start` |
>
> Start/end types put the beak 16px from the edge and center it on the element. Beak 6 x 12.696px. Gap beak tip to element 4px. Examples: `eco-design-system/components/tooltip.html`.

> Choose the position based on where there's room. Default: **Bottom** for buttons in toolbars (room below), **Top** for buttons in table rows (room above).

---

### Interaction

- The tooltip shows on **hover** and on **keyboard focus** (CSS `opacity: 1` via `.tooltip-wrap:is(:hover, :has(:focus-visible)) .tooltip`; the global tooltip: `focusin` on a `:focus-visible` trigger in `tooltip.js`). Not on the focus a mouse click gives. Decided 2026-10-12, after Carbon, Spectrum and Polaris (all show on focus) and WCAG 2.2 1.4.13.
- **Esc** hides it without moving focus or pointer (`.tooltip-wrap.is-dismissed`, set by `tooltip.js`; the global tooltip is hidden). It comes back on the next hover or focus. Focus leaving hides it.
- Easing: `ease-standard` (`cubic-bezier(.35,0,.35,1)`), `duration-fast-2` (`100ms`).
- **Open point (WCAG 1.4.13 hoverable):** the tooltip has `pointer-events: none`, so the pointer cannot move onto it. Dismissible and persistent are met. Hoverable would need a pointer-reachable tooltip. To be decided.
- `pointer-events: none` on the tooltip element so it doesn't interfere with mouse interaction.

---

### HTML structure

```html
<!-- Button with a Bottom tooltip -->
<div class="tooltip-wrap">
  <button class="action-btn" aria-label="Add user">
    <span class="ms">person_add</span>
  </button>
  <span class="tooltip tooltip--bottom">Add user</span>
</div>

<!-- Button with a Top tooltip -->
<div class="tooltip-wrap">
  <button class="btn-row-action" aria-label="Edit">
    <span class="ms">edit</span>
  </button>
  <span class="tooltip tooltip--top">Edit</span>
</div>
```

> `aria-label` on the button is mandatory and must have the same text as the tooltip content.

---

### Tooltip on a button that has a label

Use this when the button already shows text and the tooltip only adds detail (for example `duration-fast-4 · 200ms` on a duration button). The button itself is the wrapper, so it fits inside a joined `btn-group`, where an extra wrapper element would break the shared frame:

```html
<button type="button" class="tooltip-wrap" aria-label="duration-fast-4 · 200ms">
  Fast 4
  <span class="tooltip tooltip--top" aria-hidden="true">duration-fast-4 · 200ms</span>
</button>
```

- `aria-label` has the same text as the tooltip (as everywhere). The tooltip is `aria-hidden`, so the text is not read twice.
- A tooltip is never all caps. It sets `text-transform: none` itself, so it stays in normal case even inside an uppercase button (buttons are uppercase).
- Hover only, as always. Do not use the browser's `title` attribute for this.

---

### CSS

Link the shared stylesheet. Never copy its rules into a page, and never write a parallel version:

```html
<link rel="stylesheet" href="/components/css/tooltip.css">
```

`components/css/tooltip.css` is the single source for this component. Mobile-first, desktop from 769px, `var(--…)` only. To change the component, edit that file.

---
