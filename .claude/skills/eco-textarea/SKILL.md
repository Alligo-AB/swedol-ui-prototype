---
name: eco-textarea
description: Use when building or reviewing a multi-line text area (comments, feedback, long free text) — label with optional word count, all states (enabled/hover/active/focus/error/success/disabled), resizer and message per the ECO Design System. Not for single-line text (use eco-input) or choosing from a list (use eco-select).
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Text Area (ECO Design System)

Figma (ECO Design System): Text Area states `1524:56967` (Desktop, 7 states), usage info `12137:385313`. The node ids in the first message of the request (`278:9676`, `12137:385340`) pointed at the Toggle Switch frame and a different info frame; the ids above are the ones the links actually open.

> Shares with `eco-input`: `font-family: 'Breuer Condensed', sans-serif`, `font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1`, `border-radius: 0`, the `.form-field` / `.form-label` / `.form-helper` / `.input-wrap` classes and the focus ring. Use the same classes so a text area sits in a form next to an input.

### When to use / not to use

A text area is an interactive form element for text over **multiple lines**: comments, feedback, or longer passages that need more room than a single-line input. Use `eco-input` for short single-line values (name, number, search), `eco-select` for choosing from a fixed list, `eco-radio` / `eco-checkbox` for options. Default and pre-filled text follows sentence case.

### Size model

There is **one size**; Figma has no Size axis and only a `Desktop` version.

| Part | Value |
|---|---|
| Width | fills its container (Figma example 240px) |
| Height / min height | 66px, initial and minimum (the user can drag it taller) = border 1 + padding 12 + one line 24 + padding 12 + resizer row 16 (8 + 8) + border 1. Literal, no token. |
| Padding | `space-12` all sides |
| Resizer | 8px handle at the bottom-right, 8px from the edges. Native `resize: vertical`, so the box can grow in height only. |
| Gap label → box → message | `space-4` |
| Focus ring | 2px, `inset: -3px` (outside the box) |

### Typography

| Part | Desktop (`md`, 769px+) | Mobile (`xs`/`sm`, 0–768px) |
|---|---|---|
| Label | `label-md`: 16px/16px, 0.48px, Bold, uppercase | `label-sm` mobile: 12px/12px, 0.48px |
| Word count | `body-sm`: 14px/20px, 0.36px | same |
| Text | `body-md`: 17px/24px, 0.32px | `body-md` mobile: 16px/22px, 0.32px |
| Message | `body-sm`: 14px/20px, 0.36px | same |

> Flag for design: Figma only defines the Desktop version. The mobile values are taken from `eco-input` (same label and body styles) until a Mobile frame exists.

### States

Every state must be implemented. Active means the field is being used (focus, or `[data-state="active"]` in docs demos). **Decision (2026-10-07):** a value alone, such as pre-filled text, keeps the default border; the selected border shows only while the field is active. Same rule as `eco-input` and `eco-select`.

| State | Border | Fill | Text | Label / word count | Message |
|---|---|---|---|---|---|
| **Enabled** | `border-input-default` | `surface-raised-primary` | placeholder `text-tertiary` | `text-primary` / `text-secondary` | `text-tertiary` |
| **Hover** | `border-hover` | `surface-raised-primary` | placeholder `text-tertiary` | same | `text-tertiary` |
| **Active** | `border-selected` | `surface-raised-primary` | `text-primary` | same | `text-tertiary` |
| **Focus** | `border-input-default` + ring `border-focus` (2px, 3px outside) | `surface-raised-primary` | placeholder `text-secondary` | same | `text-tertiary` |
| **Error** | `border-danger-default` | `surface-raised-primary` | `text-primary` | same | `text-danger-default` + 20px `error` icon, `gap: space-4` |
| **Success** | `border-success-default` | `surface-raised-primary` | `text-primary` | same | `text-success-default` |
| **Disabled** | `border-primary` | `surface-raised-secondary` | `text-disabled` | `surface-60` / `surface-60` | `text-disabled` |

The ring shows on keyboard focus only (`body.keyboard-nav`, same script as `eco-input`).

### HTML structure

Native `<textarea>` with a real `<label>`. The word count is optional; with `maxlength` the browser enforces the limit and a small script updates the text.

```html
<div class="form-field">
  <div class="form-field__head">
    <label class="form-label" for="comment">Comment</label>
    <span class="form-count" id="comment-count">0/100</span>
  </div>
  <div class="input-wrap">
    <textarea class="form-textarea" id="comment" maxlength="100" placeholder="Placeholder text" aria-describedby="comment-msg"></textarea>
  </div>
  <div class="form-helper" id="comment-msg">Message or hint text</div>
</div>

<!-- Error -->
<textarea class="form-textarea form-textarea--error" aria-invalid="true" aria-describedby="comment-msg">…</textarea>
<div class="form-helper form-helper--error" id="comment-msg"><span class="input-icon" aria-hidden="true">error</span>Message or hint text</div>

<!-- Disabled -->
<textarea class="form-textarea" disabled>…</textarea>
```

```js
// word count
ta.addEventListener('input', () => count.textContent = ta.value.length + '/' + ta.maxLength);
```

### CSS

Link the shared stylesheet. Never copy its rules into a page, and never write a parallel version:

```html
<link rel="stylesheet" href="/components/css/textarea.css">
```

`components/css/textarea.css` is the single source for this component. The docs page `eco-design-system/components/textarea.html` links the same file and prints it in its Code section. Mobile-first, desktop from 769px, `var(--…)` only. The `[data-state="…"]` selectors in it are only for the docs pages' forced-state demos and do nothing elsewhere. To change the component, edit that file.

The `.input-icon` class for the error icon is the Material Symbols Outlined (wght 300, 20px) rule from `eco-input`.

### Rules

1. Never hardcode design tokens: `var(--…)` from `tokens.json` (see `eco-tokens`). The only literal is the 66px min height.
2. Always a visible `<label for>`; a placeholder is never the label. Error: `aria-invalid="true"` and `aria-describedby` to the message, with the icon so colour is not the only signal.
3. Always implement every state; the focus ring only on keyboard navigation, drawn on `.input-wrap::after`, not as `outline` on the textarea.
4. Resize vertical only (`resize: vertical`); disabled has no resize.
5. Breakpoint test: verify at ~375px, ~700px (`sm` = mobile), ~1024px+ with `getComputedStyle` before delivery.

### Flags

> **Flag for design:** (1) Only a Desktop version exists in Figma; mobile type values are copied from `eco-input`. (2) Disabled border is `border-primary` (`#e5e5e5`) in Figma, whereas `eco-input` uses `border-disabled` (`#dad9d7`). This skill follows Figma. (3) Focus placeholder is `text-secondary` in Figma, `text-tertiary` in `eco-input`. This skill follows Figma. (4) Disabled label and word count bind `surface-60` (`#595959`), darker than the `text-disabled` used for the text and message; kept as in Figma. (5) Figma's message color is the primitive `Text/medium-emphasis` (`#737373`), the same value as `text-tertiary`, which is used. (6) Figma's resizer is a custom 8px icon; the native browser handle is used (size and look vary by browser). (7) Figma binds `body-*` `font-weight` 500 while the style says Regular; `400` is kept as in `eco-input`. (8) The 66px minimum height has no token.
