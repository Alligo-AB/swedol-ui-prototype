---
name: eco-chip
description: Use when building or reviewing a chip — a small interactive element that represents an input, attribute or action, most often a filter chip the user selects and unselects (toggle button with aria-pressed), or a removable chip (picked value, entered email address). Sizes Medium/Small, optional leading icon, states Enabled/Hover/Selected/Selected hover. Not for a category label (use eco-tag), a non-interactive status (use eco-badge), an action (use eco-button) or a two-view switch (use eco-pill-segment-control).
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, breakpoints, and the quality checklist.

## Chip (ECO Design System)

Figma: Chip with states `17345:30209`, Chip base (Icon variant) `17345:30170`, info frame `17345:28873` (source for usage text only, not linked on the docs pages). Read 2026-10-28.

Docs: `eco-design-system/components/chip.html` (+ `-specifications`, `-code`), built by `eco-design-system/gen/gen_chip.py`. Status **Live** (2026-10-28): no eyebrow badge, Live tag on the overview card; they change together.

## When to use / not to use

- **Use** to show picked filters or choices (values picked in a filter drawer or dropdown), user input as separate items (email addresses in a recipient field), or an action the user can undo (removable chip).
- Filter chips are unselected by default; the user clicks each to select as many as they like; clicking a selected chip (or its ×) unselects it.
- **Not** for a category/metadata label → `eco-tag`. **Not** for a status → `eco-badge`. **Not** for an action → `eco-button`. **Not** for two views → `eco-pill-segment-control`. **Not** for one choice in a form → `eco-radio`.

## Size model

| Size | Class | Height | Padding | Gap | Leading icon | Close icon |
|---|---|---|---|---|---|---|
| Medium (default) | `chip` | 32px | 0 8px | 4px | 16px | 14px |
| Small | `chip--sm` | 24px | 0 8px; **0 4px 0 8px** with the close icon | 4px | 16px | 14px |

Fixed height, label centred, so vertical padding is 0. Size does not change per breakpoint. Border 1px, square corners.

## Typography

| Size | Mobile (0–768px) | Desktop (769px+) |
|---|---|---|
| Medium | `body-md` 16/22, 0.32px | `body-md` 17/24, 0.32px |
| Small | `body-sm` 14/20, 0.36px | `body-sm` 14/20, 0.36px |

Weight 400 (Figma Regular), `ss02 ss03 ss06`, never wraps. Switches at `md` (769px), never `sm`.

## States

| State | Surface | Frame | Text / icon | Close icon |
|---|---|---|---|---|
| Enabled | none | `--color-border-primary` | `--color-text-primary` / `--color-icon-primary` | hidden |
| Hover | none | `--color-border-hover` | same | hidden |
| Selected (`aria-pressed="true"`) | `--color-surface-opacity-black-10` | none (transparent) | same | shown |
| Selected hover | `--color-surface-opacity-black-10` | `--color-border-selected-hover` | same | shown |
| Focus (`:focus-visible`) | as below | + 2px `--color-border-focus` outline, 2px offset (as `eco-button`) | same | as below |

No disabled state in Figma.

## HTML structure

```html
<link rel="stylesheet" href="/components/css/chip.css">
<script src="/components/js/chip.js" defer></script>

<div class="chip-group">
  <!-- filter chip: toggle button -->
  <button type="button" class="chip" aria-pressed="false">
    <span class="chip__label">Gloves</span>
    <span class="chip__close" aria-hidden="true">close</span>
  </button>
  <!-- Small, leading icon, selected -->
  <button type="button" class="chip chip--sm" aria-pressed="true">
    <span class="chip__icon" aria-hidden="true">assignment_turned_in</span>
    <span class="chip__label">Workwear</span>
    <span class="chip__close" aria-hidden="true">close</span>
  </button>
  <!-- removable chip: close icon always shown -->
  <button type="button" class="chip chip--removable" aria-label="Remove anna@example.com">
    <span class="chip__label">anna@example.com</span>
    <span class="chip__close" aria-hidden="true">close</span>
  </button>
</div>
```

## CSS / JS

One source: `components/css/chip.css` and `components/js/chip.js` (linked in `template.html` and `mypages/mypages-template.html`). Never copy the rules into a page. `chip.js` toggles `aria-pressed` on click and fires `chip:change` (`detail.selected`); a `.chip--removable` fires `chip:remove` and the page removes it (move focus to the next chip). `[data-state="hover|selected|selected-hover|focus"]` only serves the docs pages' forced-state demos.

## Rules

1. Always a native `<button type="button">`; a filter chip always has `aria-pressed`.
2. Always put chips in a `chip-group` (wrapping row, 8px gap); never scroll a chip row sideways.
3. Never mix Medium and Small in one row.
4. Keep labels to one or two words; never a sentence.
5. A removable chip always has `aria-label="Remove <label>"`; the icons are `aria-hidden`.
6. Never hardcode colours/spacing: `var(--…)` from `eco-tokens` only.
7. Never round the corners (ECO is sharp-cornered).
8. Breakpoint test: at ~375, ~700 and ~1024px Medium must be 16/22 at 375 and 700 and 17/24 at 1024; height 32/24 everywhere.

## Flags

- **Figma line height** 16 (Medium) and 14 (Small) is not a token pair; the CSS uses `body-md` 16/22 → 17/24 and `body-sm` 14/20. The fixed height keeps the chip size identical.
- **Figma 1px corner radius** on the Medium desktop border only; ignored (ECO square corners).
- **Selected padding**: Small drops to 4px right with the close icon, Medium keeps 8px (as in Figma; asymmetric between sizes, confirm with design).
- **No disabled state** in Figma.
- **Info frame unfinished**: the "Examples" list is empty and one paragraph (extra input via dropdown/bottom sheet) is struck through; that behaviour is left out.
- The active filters on `components-overview.html` use Remove tags (`eco-tag`), not chips (the old `.ds-fchip` was removed 2026-10-28).

Tag (`eco-tag`) and Chip are separate components (confirmed 2026-10-28): Tag labels content, Chip is interactive input/filter. Neither replaces the other.
