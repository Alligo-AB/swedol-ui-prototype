---
name: eco-input
description: Use when building or reviewing text input fields — sizes (Large/Small/XSmall), all states (enabled/hover/active/focus/error/success/disabled), and label/hint patterns per the ECO Design System.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Input Fields – Sizes & States (ECO Design System)

Input fields are used to enter free text, numbers, or other data. They can be combined with a left icon, right-hand action icons, hint text, and error messages.

Figma (ECO Design System): Text Input states `1547:51748`, Base Input (sizes × breakpoints, icon options) `1475:44234`, usage info `12137:375748`.

> All input fields share: `font-family: 'Breuer Condensed', sans-serif`, `font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1`, and `border-radius: 0` (sharp corners).

### When to use

> A field that holds a Material Symbols icon name uses `eco-icon-picker` (`data-icon-picker` on this input), not a plain input.

Inputs are interactive text fields for freeform short or long-form data (text, numbers, search). Single-line only here (multi-line text: use `eco-textarea`), with icons indicating input type and rules for accurate entry. Detection/pre-fill reduces errors; type-ahead can suggest values when the software cannot determine them. **Default and detected values and auto-completion text follow sentence case.** Not for choosing from a fixed list (use `eco-select`) or 2–3 mutually exclusive options (use `eco-radio`).

---

### Sizes per breakpoint

> Figma has two breakpoint variants: `XLarge-Large-Medium` (desktop, `md:` 769px+) with Large/Small/XSmall, and `Small-XSmall` (mobile/tablet, 0–768px) with Large/Small only. `sm` (640–768px) always uses the mobile variant.

#### Desktop (`md:`, 769px+)

| Size | Height | Padding (top/bottom, left, right) | Left icon | Label | Input text |
|---|---|---|---|---|---|
| **Large** | 48px | `space-8`, `space-12`, `space-8` | 24px | `label-md`: 16px/16px, 0.48px, Bold, uppercase | `body-md`: 17px/24px, 0.32px |
| **Small** | 40px | `space-8`, `space-8`, `space-4` | 20px | `label-sm`: 14px/14px, 0.56px, Bold, uppercase | `body-sm`: 14px/20px, 0.36px |
| **XSmall** | 32px | `space-8`, `space-8`, **6px** (literal, no token) | 20px | `label-sm`: 14px/14px, 0.56px, Bold, uppercase | `body-sm`: 14px/20px, 0.36px |

#### Mobile / Tablet (`xs`/`sm`, 0–768px)

| Size | Height | Padding (top/bottom, left, right) | Left icon | Label | Input text |
|---|---|---|---|---|---|
| **Large** | 40px | `space-8`, `space-8`, `space-4` | 24px | `label-sm` (mobile): 12px/12px, 0.48px, Bold, uppercase | `body-md` (mobile): 16px/22px, 0.32px |
| **Small** | 32px | `space-8`, `space-8`, **6px** (literal, no token) | 20px | `label-sm` (mobile): 12px/12px, 0.48px, Bold, uppercase | `body-sm`: 14px/20px, 0.36px |

(`space-N` = `var(--dimension-spacing-space-N)`; gap between left icon and text: 8px = `space-8`.)

> **Rule of thumb:** Desktop Large = 48px (standard forms), Desktop Small = 40px (compact surfaces), XSmall = 32px (dense tables/filters), Mobile Large = 40px, Mobile Small = 32px. Always choose the size that fits the breakpoint.

**Hint/message text** (below the input field, all sizes):
- `body-sm`: 14px/20px, letter-spacing 0.36px, Regular
- Left icon: 20px (Material Symbols Outlined, wght 300)

---

### States

Every state must be implemented each time an input field is created. States control border, background, text color, and helper text.

#### 1. Enabled (default)
| Property | Value |
|---|---|
| Border | `1px solid var(--color-border-input-default)` → `#939595` |
| Background | `var(--color-surface-raised-primary)` → `#ffffff` |
| Placeholder text | `var(--color-text-tertiary)` → `#737373` |
| Hint/message | `var(--color-text-tertiary)` → `#737373` |

#### 2. Hover
| Property | Value |
|---|---|
| Border | `1px solid var(--color-border-hover)` → `#333333` |
| Background | `var(--color-surface-raised-primary)` → `#ffffff` |
| Placeholder text | `var(--color-text-tertiary)` → `#737373` |
| Hint/message | `var(--color-text-tertiary)` → `#737373` |

#### 3. Active (the field is being used)
> **Decision (2026-10-07):** the selected border shows only while the field is active (focus, or `[data-state="active"]` for docs demos). A value alone, such as a pre-filled field, keeps the default border. The clear icon still follows the value.

| Property | Value |
|---|---|
| Border | `1px solid var(--color-border-selected)` → `#000000` |
| Background | `var(--color-surface-raised-primary)` → `#ffffff` |
| Input text | `var(--color-text-primary)` → `#000000` |
| Clear icon | Shown (cancel icon, filled, 20px) + divider `1px, var(--color-border-tertiary)` (see "Right-hand icons") |
| Hint/message | `var(--color-text-tertiary)` → `#737373` |

#### 4. Focus (keyboard focus, no ring on select)
| Property | Value |
|---|---|
| Border (input box) | `1px solid var(--color-border-input-default)` → `#939595` |
| Focus ring (outer) | `2px solid var(--color-border-focus)` → `#455efb`, `inset: -3px` (offset outside) |
| Background | `var(--color-surface-raised-primary)` → `#ffffff` |
| Placeholder text | `var(--color-text-tertiary)` → `#737373` |

> The focus ring is placed as an absolute element `inset: -3px` outside the input box – not as an `outline` on the input element itself.

#### 5. Error
| Property | Value |
|---|---|
| Border | `1px solid var(--color-border-danger-default)` → `#d90000` |
| Background | `var(--color-surface-raised-primary)` → `#ffffff` |
| Input text | `var(--color-text-primary)` → `#000000` |
| Message | `var(--color-text-danger-default)` → `#eb0000` + **optional** 20px message icon (Material Symbols Outlined, wght 300, e.g. `error`) to the left of the text, `gap: space-4`. Icon is a user/developer choice, not required; message works with text only. |

#### 6. Success
| Property | Value |
|---|---|
| Border | `1px solid var(--color-border-success-default)` → `#248616` |
| Background | `var(--color-surface-raised-primary)` → `#ffffff` |
| Input text | `var(--color-text-primary)` → `#000000` |
| Message | `var(--color-text-success-default)` → `#17730d` |

#### 7. Disabled
| Property | Value |
|---|---|
| Border | `1px solid var(--color-border-disabled)` → `#dad9d7` |
| Background | `var(--color-surface-raised-secondary)` → `#f6f6f6` |
| Placeholder text | `var(--color-text-disabled)` → `#939595` |
| Left icon | `var(--color-text-disabled)` → `#939595` (Figma binds `icon/disabled`, not in `tokens.json` – see Flags) |
| Message | `var(--color-text-disabled)` → `#939595` |
| Cursor | `not-allowed` |

---

### Anatomy

```
[Label]                      ← label-md/sm, uppercase, text-primary
[Icon] [Input text...]  [✕|⊕] ← input box with optional left icon + right clear+divider+action
[Hint/error message]         ← body-sm, tertiary / danger / success
```

- **Label**: Always uppercase, Bold font. Placed above the input box with `gap: var(--dimension-spacing-space-4, 4px)`.
- **Left icon** (optional, default `search`): Material Symbols Outlined, wght 300, 24px (Large) / 20px (Small/XSmall). Can be swapped for another icon.
- **Right-hand icons** (optional "Pair Icons right"): see below.
- **Message**: Always `body-sm` (14px), shown below the input box with `gap: var(--dimension-spacing-space-4, 4px)`.

---

### Right-hand icons ("Pair Icons right")

Optional group at the right end of the input, `display: flex; align-items: center; justify-content: flex-end; gap: var(--dimension-spacing-space-4, 4px)`. Each part is individually toggleable in Figma (`cancel`, `divider`, `locationOn`, `qrCodeReader`, `photo`) and appears in this order:

1. **Clear** (cancel, filled) – only when the field has a value (Active state).
2. **Divider** – `1px` wide, `16px` tall, `var(--color-border-tertiary)`. Shown only together with clear + at least one action icon.
3. **Action icons** – `location_on`, `qr_code_scanner`, `photo_camera` (examples; use only the ones the field needs).

Each icon is a real `<button type="button">` with an `aria-label`. Figma (Icon Button `23990:132193`, Base Input `1475:44234`) holds the icons in **two different components, by size and breakpoint**:

| Breakpoint · size | Icon holder | Hit area | Gap before the icons |
|---|---|---|---|
| Desktop (`XLarge-Large-Medium`) · Large | **Button** (`eco-button`, Blank, icon only, `padding: 6px`) | 32px | 4px (`space-4`) |
| Desktop · Small | **Button** | 32px | 4px |
| Desktop · XSmall | **Icon Button** (the 20px icon itself) | 20px | 16px (`space-16`) |
| Mobile (`Small-XSmall`) · Large | **Button** | 32px | 10px (literal) |
| Mobile · Small | **Icon Button** | 20px | 16px |

Button hover: `background: var(--color-surface-opacity-black-05)` (the Blank / icon-button hover in `eco-button`). Icon Button hover: no fill, the icon turns `var(--color-text-action-primary-hover)`. Icon color in both: `var(--color-text-action-primary)`; disabled: `var(--color-text-disabled)`. Icon Button sizes are Small (20px) and Large (24px); the input uses Small. Icons are 20px in **all** sizes; only the left search icon scales to 24px on Large. The icons used are `cancel` (filled), `location_on`, `qr_code_scanner` and `photo_camera`.

> Flag for design: the 32px Large hit area comes from `padding: 6px` in Figma (`Button base`), a literal with no spacing token. The Figma "Base Input" with all icons is shown with every toggle on; real fields should enable only what is needed.

---

> **CSS:** `components/css/input.css` is the live, tested stylesheet (mobile-first, desktop from 769px). It puts the border, fill and height on an **`.input-box`** that holds the left icon, the `.form-input` and the right-hand icons in one flex row; states are `.input-box:hover`, `:focus-within` / `[data-state="active"]` (Active), `.input-box--error` / `--success` and `:has(.form-input:disabled)`; the focus ring stays on `.input-wrap::after`. Where the HTML below and the CSS differ, follow the CSS file.

### CSS

Link the shared stylesheet. Never copy its rules into a page, and never write a parallel version:

```html
<link rel="stylesheet" href="/components/css/input.css">
```

`components/css/input.css` is the single source for this component. The docs page `eco-design-system/components/input.html` links the same file and prints it in its Code section. Mobile-first, desktop from 769px, `var(--…)` only. The `[data-state="…"]` selectors in it are only for the docs pages' forced-state demos and do nothing elsewhere. To change the component, edit that file.

Clear icon shows only while the input has a value (e.g. `.input-wrap:has(.form-input:not(:placeholder-shown)) .input-actions__clear { display: flex; }`, hidden otherwise).

---

### Rules

1. Never hardcode design tokens – `var(--…)` from `tokens.json` (see `eco-tokens`); the two flagged literals are the only exceptions.
2. Always associate the `<label>` with the input (`for`/`id`); icon buttons need `aria-label`.
3. Always implement every state; focus ring only on keyboard navigation (`body.keyboard-nav`).
4. Breakpoint test: verify at ~375px, ~700px (`sm` = mobile sizing), ~1024px+ with `getComputedStyle` before delivery.

### Flags

> **Flag for design:** (1) Figma binds `icon/disabled` (`#939595`) – no such token in `tokens.json`; `--color-text-disabled` has the same value and is used instead. (2) Right padding `6px` (XSmall desktop, Small mobile) and the `6px` icon-button padding are literals with no spacing token. (3) Figma binds `body-*` `font-weight` 500 while the style name says Regular; the template keeps the existing `400`/Regular. (4) Mobile Large label uses `label-sm` (12px) in Figma, whereas the old skill had `label-md` mobile (14px) – skill now follows Figma. (5) Error message color is `text-danger-default` `#eb0000` (the old skill said `#d90000`, which is the *border* token).

---
