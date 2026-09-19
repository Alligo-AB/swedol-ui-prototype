---
name: eco-modal-ecom
description: Use when building a modal (E-Com Modal) that requires confirmation or an active choice before the user can continue — not for short-lived feedback or status information in page context.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Notification – E-Com Modal (ECO Design System)

**Figma:** https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=13377-48335

### Used when
- The action requires confirmation or an active choice before the user can continue
- Important information must be presented without the user being able to miss it
- The content requires focus and can't be shown inline without risk of misunderstanding

### NOT used when
- Short-lived feedback on an action → use **Toast**
- Status information in page context → use **System Inline**
- A page-wide message → use **System Banner**
- The error message is for a single form field → use `form-helper--error`

> **Content-led, no status variant.** Unlike Banner/Inline/Toast, Modal has no Informational/Success/Warning/Error emphasis — it's a single neutral-surface (white/grey) treatment with an action-hierarchy button pair. Usage guidance from the component guide: destructive flows (confirm account deletion), critical compliance notices, or high-risk cart updates — must present a clear primary decision (Confirm/Cancel), support ESC-key exit, and close on backdrop click.

---

### Sizes and widths per breakpoint

Desktop and Tablet: the modal is centered in the viewport. The background overlay is `var(--color-surface-opacity-black-20)`.

| Size | Desktop (`md:` 769px+) | Tablet (`sm:` 640–768px) | Mobile (`xs:` 0–639px) |
|---|---|---|---|
| **Small** | `440px` | `440px` | Fills the whole viewport |
| **Medium** | `600px` | `576px` | Fills the whole viewport |
| **Large** | `705px` | `576px` | Fills the whole viewport |

> Choose the size based on the amount of content. Small for simple confirmations, Medium/Large for more complex information.

> **xs (Mobile):** The modal is **not** centered. It fills the whole viewport: `position: fixed; top: 0; left: 0; width: 100%; height: 100dvh; padding: 16px`. The header+body section has `flex: 1` so the buttons are pinned to the bottom. A close button (`×`) is shown at the top.

---

### Anatomy

```
[LABEL (OPTIONAL)]                        [✕ close]
Title

Body text

[Cancel]   [Primary action              ]
```

- **Overlay**: `position: fixed; inset: 0; background: var(--color-surface-opacity-black-20); z-index: 9998`
- **Modal panel**: `position: fixed; z-index: 9999`, centered with `transform: translate(-50%, -50%); top: 50%; left: 50%`
- **Background**: `var(--color-surface-raised-primary)` (`surface-raised-primary`)
- **Shadow**: `elevation-b-100` = `var(--shadow-elevation-b-100)`
- **Gap**, header section: `8px` vertical
- **Header**: `gap: 12px` between Label+Title and the close button
- **Close button**: Blank xs, `close` icon 20px, `padding: 2px`
- **Buttons in footer**: `gap: 8px`, Cancel (Secondary xs, fixed width) + Primary (Primary xs, `flex: 1`)

---

### Typography per breakpoint

| Element | Desktop (`md:` 769px+) | Tablet + Mobile (`sm-xs` ≤768px) |
|---|---|---|
| **Label** (optional) | `alt-label-sm`: 14px/14px, 0.56px, Medium(500), uppercase, `text-secondary` var(--color-text-secondary) | 12px/12px, 0.48px |
| **Title** | `title-md`: 20px/24px, 0px, Bold | `title-md`: 18px/22px, 0px, Bold |
| **Body text** | `body-md`: 16px/24px, 0.32px, Regular, `text-secondary` var(--color-text-secondary) | 16px/22px, 0.32px |
| **Button text** | `label-sm`: 14px/14px, 0.56px, Bold, uppercase | `label-md`: 14px/14px, 0.48px, Bold, uppercase |

---

### Buttons per breakpoint

The buttons in the modal **always** follow the ECO Design System button sizes:
- **Desktop (lg-md, ≥769px):** button size **xs** → `height: 32px`, `padding: 6px`, `label-sm` 14px, 0.56px
- **Tablet + Mobile (sm-xs, ≤768px):** button size **sm** → `height: 32px`, `padding: 6px`, `label-md` 14px, 0.48px

Both variants (Cancel and Primary) are **always 32px tall** — regardless of breakpoint and button variant.

| | Desktop (`md:` 769px+) | Tablet + Mobile (`sm-xs` ≤768px) |
|---|---|---|
| Modal padding | `24px` | Tablet: `24px` / Mobile xs: `16px` |
| Button group top gap | `pt-32px` | `pt-24px` |
| Button height (both) | `32px` (xs button) | `32px` (sm button) |
| Button padding (both) | `6px` | `6px` |
| Button letter-spacing | `0.56px` (label-sm) | `0.48px` (label-md) |

---

### CSS template

```css
/* Overlay */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: var(--color-surface-opacity-black-20);
  z-index: 9998;
}

/* Modal panel */
.modal {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 9999;
  background: var(--color-surface-raised-primary);
  padding: 24px;
  display: flex;
  flex-direction: column;
  box-shadow: var(--shadow-elevation-b-100);
  width: 440px;       /* Small — default */
  max-width: 800px;
  min-width: 440px;
  box-sizing: border-box;
}

/* Sizes */
.modal--medium { width: 600px; }
.modal--large  { width: 705px; }

/* Tablet */
@media (min-width: 640px) and (max-width: 768px) {
  .modal--medium,
  .modal--large { width: 576px; }
  .modal { padding: 24px; }
}

/* Mobile */
@media (max-width: 639px) {
  .modal,
  .modal--medium,
  .modal--large {
    width: 375px;
    min-width: 375px;
    max-width: calc(100vw - 32px);
    padding: 16px;
  }
}

/* Header */
.modal__header {
  display: flex;
  gap: 12px;
  align-items: flex-start;
  width: 100%;
}

.modal__header-text {
  display: flex;
  flex-direction: column;
  gap: 8px;
  flex: 1;
  padding-top: 2px;
}

/* Label (optional) */
.modal__label {
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 14px;          /* alt-label-sm Desktop */
  font-weight: 500;
  line-height: 14px;
  letter-spacing: 0.56px;
  text-transform: uppercase;
  color: var(--color-text-secondary);           /* text-secondary */
  font-feature-settings: 'ss02' 1, 'ss03' 1;
}

@media (max-width: 768px) {
  .modal__label { font-size: 12px; line-height: 12px; letter-spacing: 0.48px; }
}

/* Title */
.modal__title {
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 20px;          /* title-md Desktop */
  font-weight: 700;
  line-height: 24px;
  letter-spacing: 0px;
  color: var(--color-text-primary);
  font-feature-settings: 'ss02' 1, 'ss03' 1;
}

@media (max-width: 768px) {
  .modal__title { font-size: 18px; line-height: 22px; }
}

/* Close button */
.modal__close {
  flex-shrink: 0;
  background: transparent;
  border: none;
  cursor: pointer;
  padding: 2px;
  font-size: 20px;
  color: var(--color-text-primary);
}

/* Body */
.modal__body {
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 16px;          /* body-md */
  font-weight: 400;
  line-height: 24px;
  letter-spacing: 0.32px;
  color: var(--color-text-secondary);           /* text-secondary */
  font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1;
  margin-top: 8px;
}

@media (max-width: 768px) {
  .modal__body { line-height: 22px; }
}

/* Button group */
.modal__footer {
  display: flex;
  gap: 8px;
  align-items: center;
  padding-top: 32px;
  width: 100%;
}

@media (max-width: 768px) {
  .modal__footer { padding-top: 24px; }
}

/* Cancel — Secondary xs */
.modal__btn-cancel {
  flex-shrink: 0;
  background: transparent;
  border: 1px solid var(--color-border-selected);
  cursor: pointer;
  padding: 6px;
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 14px;
  font-weight: 700;
  line-height: 14px;
  letter-spacing: 0.56px;
  text-transform: uppercase;
  color: var(--color-text-primary);
  white-space: nowrap;
  font-feature-settings: 'ss02' 1, 'ss03' 1;
}

@media (max-width: 768px) {
  .modal__btn-cancel { padding: 8px; font-size: 16px; line-height: 16px; letter-spacing: 0.32px; }
}

@media (max-width: 639px) {
  .modal__btn-cancel { padding: 4px; font-size: 14px; line-height: 14px; letter-spacing: 0.42px; }
}

/* Primary action — Primary xs, flex: 1 */
.modal__btn-primary {
  flex: 1;
  background: var(--color-surface-100);
  border: none;
  cursor: pointer;
  padding: 6px;
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 14px;
  font-weight: 700;
  line-height: 14px;
  letter-spacing: 0.56px;
  text-transform: uppercase;
  color: var(--color-text-primary-inverted);
  text-align: center;
  white-space: nowrap;
  font-feature-settings: 'ss02' 1, 'ss03' 1;
}

@media (max-width: 768px) {
  .modal__btn-primary { padding: 4px; font-size: 14px; line-height: 14px; letter-spacing: 0.42px; }
}
```

### HTML example (Small, Desktop)

```html
<!-- Overlay -->
<div class="modal-overlay" onclick="closeModal()"></div>

<!-- Modal -->
<div class="modal" role="dialog" aria-modal="true" aria-labelledby="modal-title">
  <div class="modal__header">
    <div class="modal__header-text">
      <p class="modal__label">Label (optional)</p>
      <h2 class="modal__title" id="modal-title">Title</h2>
    </div>
    <button class="modal__close" aria-label="Close" onclick="closeModal()">
      <span class="material-symbols-outlined">close</span>
    </button>
  </div>
  <p class="modal__body">Body text.</p>
  <div class="modal__footer">
    <button class="modal__btn-cancel" onclick="closeModal()">Cancel</button>
    <button class="modal__btn-primary">Confirm</button>
  </div>
</div>
```

---
