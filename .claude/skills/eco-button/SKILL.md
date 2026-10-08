---
name: eco-button
description: Use when building, changing, or reviewing buttons (`<button>`, CTAs) and icon buttons in swedol-ui-prototype — all variants (Primary/Secondary/Blank/Destructive/Accent/System and the three Inverted ones), sizes (Large/Medium/Small/XSmall), content (label, icons, icon only, badge) and states (hover/focus/disabled) per the ECO Design System. Not for links (use links-guide) or a switch between two views (use eco-pill-segment-control).
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec. Documentation page with live examples: `eco-design-system/components/button.html`.

## Button (ECO Design System)

**Figma:** button section `6098:342318` (component set `2007:68126`, "Button base" `263:9395`), icon buttons `23990:132193`, usage text `1025:30180` (file `42MgqJjV9vfplwQnrUB62r`).

Figma has two versions of every button: **Breakpoint = XLarge-Large-Medium** (Desktop, from 769px) and **Small-XSmall** (Mobile, below 769px). Tablet (640–768px) uses the Mobile version, like everywhere in ECO.

### When to use / not to use

A button triggers an action or goes to another page, with a single tap. A page can show several buttons: combine variants so one action stands out and the others are quieter.

| Variant | Use it for |
|---|---|
| **Primary** | The main call to action in a page, banner or card ("Add to cart", "Next page" in onboarding). Use sparingly: **one primary action per major page section**. |
| **Primary Inverted** | Dark surfaces. Also usable together with Primary on a light background as a button of medium importance. |
| **Secondary** | A second action on the page. In a pair it is the "negative" action ("Cancel", "Back"). Also where a task needs more weight than a Blank button, e.g. "+ Add address" beside a Blank "icon + Update". |
| **Secondary Inverted** | Dark surfaces. |
| **Blank** | Less prominent, sometimes independent actions ("Read more" beside a strong "Buy now"). Also sub-tasks where a primary button holds the final action ("icon + Update"). |
| **Blank Inverted** | Dark surfaces. |
| **Destructive** | Removes something or cannot be undone. Never the default choice in a dialog. |
| **Accent** | A brand-colored call to action; use with care so it stays distinctive. |
| **System / System selected** | Filtering and navigation, mainly in filter sections or wherever many buttons are grouped, to lower the cognitive load. A toggle: use `aria-pressed`. |

The inverted variants are for dark surfaces (`surface-100`) only; never put a normal variant on a dark surface or an inverted one on a light surface (except Primary Inverted as above).

Not for: a standalone link (`eco-action-link`), a link in a sentence (`eco-inline-link`), a graphical tile (`eco-tile-link`), a switch between two views (`eco-pill-segment-control`), an immediate on/off setting (`eco-switch`).

### Size model

Fixed height, content centred. Padding is the space between the button edge and its content; the **label inset** is extra horizontal space around the label (`.btn__label`). Width = padding + icon/label + inset on both sides. **Always wrap the label in `<span class="btn__label">`**, also for buttons created in JS (`innerHTML`, and set the text on the span, never `button.textContent`, which removes the span): without it the label inset is missing and the text sits too close to the edge. The 1px frame of Secondary, System and the inverted ones is drawn **inside** the box (`box-shadow: inset`), so Primary and Secondary of the same size are equally wide (Large desktop 134px).

| Size | Desktop (769px+) height / padding / label inset | Mobile (<769px) height / padding / label inset | Icon |
|---|---|---|---|
| **Large** | 56px / 16px / 8px | 48px / 12px / 8px | 24px |
| **Medium** | 48px / 12px / 8px | 40px / 8px / 8px | 24px |
| **Small** | 40px / 8px / 8px | 32px / 4px / 6px | 24px |
| **XSmall** | 32px / 6px / 4px | 32px / 6px / 4px | 20px |

Icon-only buttons are squares: width = height (56 / 48 / 40 / 32 desktop, 48 / 40 / 32 / 32 mobile). No gap between icon and label: the label inset is the space. The focus ring is 2px with a 2px gap outside the button (4px outside in total).

### Badge (number or dot)

Figma: `23998:178299` ("Button dot & badges"). A badge sits in the top right corner of a button with a label or an icon-only button, in every size and variant. Two kinds: **number** (a count, up to "99+") and **dot** (something new, no count). Colors: `--color-surface-danger-default` fill, number `--color-text-action-primary-inverted`, uppercase, 600. The number is a pill (`border-radius: 100px`), as high as wide for one digit and wider for two or "99+". The dot is a 6px circle. Offsets are from the button's top and right edge. Set per size and breakpoint through `--btn-bd-*` / `--btn-dot-off` in the size classes.

| Size | Desktop: number offset / height / side padding / type · dot offset | Mobile: number offset / height / side padding / type · dot offset |
|---|---|---|
| Large | 4px / 20px / 5px / 14px 0.56px · 12px | 4px / 18px / 4px / 12px 0.48px · 8px |
| Medium | 4px / 20px / 5px / 14px 0.56px · 8px | 3px / 18px / 4px / 12px 0.48px · 7px |
| Small | 4px / 16px / 3px / 10px · 6px | 3px / 14px / 2px / 10px · 4px |
| XSmall | 3px (icon only 2px) / 16px / 3px / 10px · 4px | 3px (icon only 2px) / 14px / 2px / 10px · 4px |

Counts over 99 show **"99+"**: cap the value in the code that renders the badge (`n > 99 ? '99+' : n`); the docs page does this with `badgeText()`. In Small and XSmall the number overlaps the end of the label (as in Figma). The badge is `aria-hidden="true"`: put the count in the button's `aria-label`.

### Typography (all buttons)

Font `Breuer Condensed`, uppercase, `white-space: nowrap`, **font-weight 600 in CSS** (Figma says 700; CSS = Figma − 100, see memory).

| Size | Style | Desktop | Mobile | `ss02`/`ss03` |
|---|---|---|---|---|
| Large, Medium | `label-lg` | 18/18, 0.18px | 16/16, 0.32px | yes |
| Small | `label-md` | 16/16, 0.48px | 14/14, 0.42px | no (see flags) |
| XSmall | `label-sm` | 14/14, 0.56px | 12/12, 0.48px | yes |

Values are in `tokens.json` (`typography.label-*`: `mobile` + `desktopOverride` at 769px). There are no CSS variables for type, so write the values with a `label-lg` etc. comment.

### Variants

All text tokens are the **action** tokens (`text-action-*`), not `text-primary`.

| Variant | Fill | Label | Frame (1px, inside) |
|---|---|---|---|
| Primary | `--color-surface-action-1` | `--color-text-action-primary-inverted` | — |
| Primary Inverted | `--color-surface-action-2` | `--color-text-action-primary` | — |
| Secondary | `--color-surface-opacity-white-0` | `--color-text-action-primary` | `--color-border-action-1` |
| Secondary Inverted | `--color-surface-opacity-white-0` | `--color-text-action-primary-inverted` | `--color-border-action-2` |
| Blank | `--color-surface-opacity-white-0` | `--color-text-action-primary` | — |
| Blank Inverted | `--color-surface-opacity-white-0` | `--color-text-action-primary-inverted` | — |
| Destructive | `--color-surface-danger-default` | `--color-text-action-primary-inverted` | — |
| Accent | `--color-accent-default` | `--color-text-action-accent` | — |
| System | `--color-surface-opacity-white-0` | `--color-text-action-primary` | `--color-border-action-3` |
| System selected (`aria-pressed="true"`) | `--color-surface-opacity-black-12` | `--color-text-action-primary` | `--color-border-action-3` |

### States

| State | Rule |
|---|---|
| **Enabled** | The table above. |
| **Hover transition (all)** | The hover layer **dissolves in**: Figma interaction "Dissolve", custom bezier `0.35, 0, 0.35, 1` (= `ease-standard`), **100ms** (`duration-fast-2`). Built as a `::before` layer (`opacity` 0 → 1) on `isolation: isolate`, so it fades over the fill and under the label. A gradient `background-image` cannot be animated, so do not use one. |
| **Hover – Primary, Destructive, Accent** | `--color-surface-opacity-white-20` layer over the fill (`--btn-hover`). |
| **Hover – Primary Inverted** | `--color-surface-opacity-black-12` layer over the white fill. |
| **Hover – Secondary, Blank** | `--color-surface-opacity-black-05` surface. The Secondary frame is unchanged. |
| **Hover – Secondary Inverted, Blank Inverted** | `--color-surface-opacity-white-20` surface. The Secondary Inverted frame is unchanged. |
| **Hover – System and System selected** | Surface `--color-surface-opacity-black-12` (System selected already has it, so its layer is transparent) and frame `--color-border-hover` (the frame fades with `box-shadow`). The two look the same. |
| **Focus** | Keyboard only: `body.keyboard-nav .btn:focus`, ring `outline: 2px solid var(--color-border-focus); outline-offset: 2px`. `keyboard-nav` is set on Tab and removed on `mousedown`/`touchstart` (same as the form elements). **Never `:focus-visible` for buttons.** Measured from the outer edge, so the gap is the same with or without a frame. |
| **Disabled – Primary, Primary Inverted, Destructive, Accent** | Fill `--color-surface-disabled`, label `--color-text-disabled`, no frame. |
| **Disabled – Secondary, Secondary Inverted, System, System selected** | No fill, frame `--color-border-disabled`, label `--color-text-disabled`. |
| **Disabled – Blank, Blank Inverted** | No fill, no frame, label `--color-text-disabled`. |
| **Disabled (all)** | `cursor: not-allowed`, the `disabled` attribute (not focusable, no hover). |

### HTML structure

```html
<!-- label only -->
<button type="button" class="btn btn--primary btn--lg">
  <span class="btn__label">Add to cart</span>
</button>

<!-- icon + label, label + icon, or both: icons are Material Symbols, 24px (20px XSmall) -->
<button type="button" class="btn btn--secondary btn--md">
  <span class="btn__icon" aria-hidden="true">shopping_cart</span>
  <span class="btn__label">Add to cart</span>
</button>

<!-- icon only: a square, needs aria-label -->
<button type="button" class="btn btn--primary btn--lg btn--icon" aria-label="Cart, 99+ items">
  <span class="btn__icon" aria-hidden="true">shopping_cart</span>
  <span class="btn__badge" aria-hidden="true">99+</span>   <!-- or <span class="btn__dot" aria-hidden="true"></span> -->
</button>

<!-- label + badge (the same badge markup works with a label) -->
<button type="button" class="btn btn--primary btn--lg" aria-label="Messages, 1 new">
  <span class="btn__label">Messages</span>
  <span class="btn__badge" aria-hidden="true">1</span>
</button>

<!-- System: a toggle -->
<button type="button" class="btn btn--system btn--md" aria-pressed="true"><span class="btn__label">Size</span></button>

<!-- navigation: same classes on a link -->
<a href="/checkout" class="btn btn--primary btn--md"><span class="btn__label">Go to checkout</span></a>
```

Write labels in sentence case (CSS makes them uppercase), short, starting with a verb. Classes: `btn--primary | primary-inverted | secondary | secondary-inverted | blank | blank-inverted | destructive | accent | system` and `btn--lg | md | sm | xs`.

### CSS

Link the shared stylesheet. Never copy its rules into a page, and never write a parallel version:

```html
<link rel="stylesheet" href="/components/css/button.css">
```

`components/css/button.css` is the single source for this component. The docs page `eco-design-system/components/button.html` links the same file and prints it in its Code section. Mobile-first, desktop from 769px, `var(--…)` only. The `[data-state="…"]` selectors in it are only for the docs pages' forced-state demos and do nothing elsewhere. To change the component, edit that file.

Every size class sets **every** `--btn-*` property in both the mobile block and the 769px block, so the media block can replace them one by one. Per-variant rules (hover layer, System hover frame, disabled variants) are in the page file.

### Icon buttons (`.icon-btn`)

A single icon that is also a control, no label and no frame. Figma: `23990:132193`.

| Version | Size | Rule |
|---|---|---|
| **Toggle icon** (compare, add_card_favourite, add_favourite_to_list, edit, location_on, cancel_filled, qr_code_scanner, list_selected) | Large 24px icon, Small 20px icon | Enabled `--color-icon-primary`. Hover: icon color `--color-text-action-primary-hover` (no surface). Selected (`aria-pressed="true"`): the filled icon. Selected hover: the filled icon in the hover color. `cancel_filled` is always filled. |
| **Close, Blank** | 24px box, 20px icon, 2px padding | Hover: `--color-surface-opacity-black-05` surface. Same on desktop and mobile. |
| **Close, Blank Inverted** | same | Icon `--color-icon-inverted`, hover `--color-surface-opacity-white-20`. |

Focus: same ring as the button. Add `aria-label` always, and an `eco-tooltip` where the icon alone is unclear.

### Rules

1. **Never hardcode** a color, spacing or shadow: use `var(--…)` from `tokens.json` (rule 6 in `CLAUDE.md`). The only literal pixel values are the ones with no spacing token (6px padding/inset) and are commented.
2. **Breakpoint:** the size switches at `769px` (`md`), never `sm`. `sm` (640–768px) looks like mobile. Check with `getComputedStyle` at ~375, ~700 and ~1024px+.
3. **Focus ring:** the `body.keyboard-nav` pattern with `outline`, never `:focus-visible` and never `::after` with `inset` (the gap would differ with a frame).
4. **One Primary per major section.** Inverted variants on dark surfaces only. Destructive is never the default.
5. **Icon-only buttons** need `aria-label`; icons are `aria-hidden="true"`. A badge is `aria-hidden` too: put the count in the label.
6. **Disabled:** use the `disabled` attribute, not a class alone.
7. **Navigation** goes in `<a class="btn …">`, actions in `<button>`. System selected is `aria-pressed`, so a System group is not page navigation.
8. Old prototype pages have their own `.btn-primary` / `.btn-blank` classes (e.g. in `template.html`). New work uses the classes above; do not copy the old ones.

### Flags

> **Flag for design** (kept so they are not forgotten; nothing here was guessed silently):
> 1. **`ss02`/`ss03`:** Figma sets these font features on `label-lg` and `label-sm` but not on `label-md` (Small). The old skill said "lg/md". The page follows Figma; confirm that Small is meant to have none.
> 2. **Badges** are now specified for all sizes and both breakpoints (see the Badge section). Unverified: Large mobile icon-only (assumed the same as with a label), badge on hover/focus, and the badge `text-primary-inverted` vs `text-action-primary-inverted` token (Figma uses both for the same white; the page uses the action token). The pill uses a literal `100px` radius.
> 3. **Toggle icon buttons:** Figma has no focus and no disabled state. The page uses `text-disabled` for disabled because `icon/disabled` (#939595 in Figma) has no token in `tokens.json`. Glyphs on the page are Material Symbols stand-ins, not the exact Figma drawings.
> 4. **Close** has only Enabled and Hover in Figma, and a 24px box: below the usual 44px touch target. Figma has no larger hit-area version.
> 5. **Disabled Primary Inverted and Accent** were read from the screenshot (grey `surface-disabled` fill); their node definitions were not opened.
> 6. **Old skill corrections:** Mobile Small is 4px padding / 6px label inset / 14/14 0.42px (was 6px / 0.48px); Mobile XSmall is `label-sm` 12/12 0.48px (was 14px 0.56px); label tokens are `text-action-*` (was `text-primary`); the frame is inside the box (was a `border`); all hover and disabled variants were missing or wrong.
> 7. **Not tested:** hover/focus of the badge states, the tablet breakpoint of icon buttons, and screen-reader output.


## Button group (toggle group)

Joined System buttons for choosing between 2–4 short, related options on one row (playground option groups, toolbars). Not the pill: that is `eco-pill-segment-control`. Documentation page: `eco-design-system/components/button-group.html`. Shared file: **`components/css/button-group.css`** (`<link rel="stylesheet" href="/components/css/button-group.css">`).

```html
<div class="btn-group" role="group" aria-label="Size">
  <button type="button" aria-pressed="true">Small</button>
  <button type="button" aria-pressed="false">Large</button>
</div>
```

Selected = `aria-pressed="true"` (black-12 fill). 1px frame shared between neighbours, hover frame `border-hover`, keyboard focus ring (`body.keyboard-nav`). 32px high on mobile, 40px from 769px. More than 4 options: use `eco-select`.

**Does not fit: use a select.** Never shrink the padding, wrap or scroll a group to make it fit (the button design stays as is). When the group is wider than its container (e.g. a narrow playground controls column), show an `eco-select` with the same options instead, and keep the two in sync. Reference: the playground in `eco-design-system/components/button.html` ("Playground button groups that do not fit…"): builds a `form-select--sm` per `.ds-controls .btn-group`, toggles on `g.scrollWidth > field.clientWidth` at load and on `resize`, and forwards the select's `change` as a click on the matching button. Hide with `style.display`, not the `hidden` attribute (`.btn-group` sets `display`, which overrides `[hidden]`).
