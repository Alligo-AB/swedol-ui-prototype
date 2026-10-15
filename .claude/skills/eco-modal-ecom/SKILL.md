---
name: eco-modal-ecom
description: Use when building a modal (E-Com Modal) that requires confirmation or an active choice before the user can continue — not for short-lived feedback or status information in page context.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

> **Buttons and ×:** buttons and the close button follow `eco-button` (see `notifications-guide`, "Buttons and the close button"): `btn btn--primary|secondary|blank` with `<span class="btn__label">`, always 32px (XSmall from 769px, Small below), and the × is `icon-btn icon-btn--close` (`icon-btn--close-inverted` on dark/solid surfaces). Live CSS: `eco-design-system/notifications.css`.

## Notification – E-Com Modal (ECO Design System)

**Figma:** https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=13377-48335
**Documentation (three pages, converted 2026-10-13):** `eco-design-system/components/modal.html` (Examples & Guidelines), `modal-specifications.html`, `modal-code.html`; hub: `notifications.html`. Generator: `eco-design-system/gen/gen_modal.py` (starting point only: the pages are the real files).

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

### Choosing a size, and the responsive strategy

The modal comes in **two sizes to choose between: Small and Large**. Choose by the user's task and need for work area. The breakpoint does not change the choice; it decides how the chosen size is adapted to the screen. **There is no Medium** (removed 2026-10-13 from Figma, the docs and the CSS).
- **Small: short decisions and simple content.** A quick, bounded decision or short information, easy to overview, no extensive scrolling: confirm or cancel an action, approve a message, choose between a few simple options.
- **Large: tasks that need a work area.** Fill in a more extensive form, search or choose in a longer list, configure a product with several options, handle content with a more complex layout.
- **Rules:** start with Small, use Large when the task needs more work area. Do not choose Large only because the screen is large, narrow or the text is long. Choose Large if Small makes the content cramped, hard to overview or hard to work with. **Keep the same size choice across breakpoints for the same task**; the presentation adapts without changing the use. Rule of thumb: Small for short decisions, Large for tasks that need more work area.
- **Desktop (XLarge, Large, Medium breakpoints):** Small is compact, Large is a wider work area; height by content, limited by the available screen height.
- **Tablet (Small breakpoint):** same rules, width adapts to the available area, both sizes keep side margins.
- **Mobile (XSmall, below 640px):** Small has height by content and a **max width of 440px**; it is centered with at least 16px side margin on each side, and on narrower screens the width adapts to the available space (343px on a 375px viewport; 343px is not a fixed width). Large is a full-screen presentation; long content scrolls and the layout works with the keyboard open.
- **Common layout rules:** Small and Large have no fixed heights; avoid unnecessary empty space (except the full-screen view on mobile). Limit the height to the available screen area and allow scroll. Content and actions must be reachable in landscape and with the keyboard open. A short dialog must not be full width and vertically centered at once: a centered dialog uses side margins; a full-width bottom sheet is a separate presentation pattern (not part of this component). Clear title, button labels that name the action (Cancel, Delete). The footer is not sticky: when content is taller than the screen the whole panel scrolls.

### Sizes and widths per breakpoint

**Three setups, one per Figma breakpoint group** (the node `Notification / Modal`, 13377:48335, has 6 variants since the `Size=Medium` ones were removed 2026-10-13; XSmall Small is 343px wide, XSmall Large 375 × 813): Figma `Breakpoint=XLarge-Large-Medium` (desktop, Small 440 / Large 705), `Breakpoint=Small` (tablet sm 640–768px: Small 440, **Large 576**, height by content, mobile type, padding 24px) and `Breakpoint=XSmall` (mobile xs: **Large fills the screen** 375 × 813 with the buttons pinned to the bottom, Small is a centered card, 343px max on a 375px viewport). The docs table: `eco-design-system/components/modal.html` → Sizes, and `modal-specifications.html` → Sizes → Setup per breakpoint.

Desktop and Tablet: the modal is centered in the viewport. The background overlay is `var(--color-surface-opacity-black-20)`.

| Size | Desktop (`md:` 769px+) | Tablet (`sm:` 640–768px) | Mobile (`xs:` 0–639px) |
|---|---|---|---|
| **Small** | `440px` | `440px` | Centered card, height by content (not full screen), **max width `440px`, at least 16px side margin**: `343px` on a 375px viewport (`max-width: calc(100vw - 32px)`) |
| **Large** | `705px` | `576px` | Fills the whole viewport (`375px` × `813px` in Figma) |

> Choose the size by the user's task, not the amount of content (see Choosing a size above).

> **xs (Mobile), Large:** The modal is **not** centered. It fills the whole viewport (Small stays a centered card, max `440px`, with `padding: 16px` and `24px` above the buttons): `position: fixed; top: 0; left: 0; width: 100%; height: 100dvh; padding: 16px`. The header+body section has `flex: 1` so the buttons are pinned to the bottom. A close button (`×`) is shown at the top.

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
- **Buttons in footer**: `gap: 8px`, Cancel (Blank xs, fixed width) + Primary (Primary xs, `flex: 1`)

---

### Typography per breakpoint

| Element | Desktop (`md:` 769px+) | Tablet + Mobile (`sm-xs` ≤768px) |
|---|---|---|
| **Label** (optional) | `alt-label-sm`: 14px/14px, 0.56px, Medium(500), uppercase, `text-secondary` var(--color-text-secondary) | 12px/12px, 0.48px |
| **Title** | `title-md`: 20px/24px, 0px, Bold | `title-md`: 18px/22px, 0px, Bold |
| **Body text** | `body-md`: 17px/24px, 0.32px, Regular, `text-secondary` var(--color-text-secondary) | 16px/22px, 0.32px |
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
.modal--large  { width: 705px; }

/* Tablet */
@media (min-width: 640px) and (max-width: 768px) {
  .modal--large { width: 576px; }
  .modal { padding: 24px; }
}

/* Mobile */
@media (max-width: 639px) {
  .modal,
  .modal--large {
    width: 440px;                    /* Small: max width 440px at every width */
    max-width: calc(100vw - 32px);   /* at least 16px to the edges: 343px on a 375px viewport; no min-width */
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
  font-weight: 600;
  line-height: 24px;
  letter-spacing: 0px;
  color: var(--color-text-primary);
  font-feature-settings: 'ss02' 1, 'ss03' 1;
}

@media (max-width: 768px) {
  .modal__title { font-size: 18px; line-height: 22px; }
}


/* Body */
.modal__body {
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 17px;          /* body-md desktop; 16px/22px below 769px */
  font-weight: 400;
  line-height: 24px;
  letter-spacing: 0.32px;
  color: var(--color-text-secondary);           /* text-secondary */
  font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1;
  margin-top: 8px;
}

@media (max-width: 768px) {
  .modal__body { font-size: 16px; line-height: 22px; }
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




/* Buttons and ×: eco-button classes (.btn, .icon-btn.icon-btn--close); live CSS in eco-design-system/notifications.css */
.modal__footer .btn--primary { flex: 1; }
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
    <button type="button" class="icon-btn icon-btn--close" aria-label="Close"><span class="btn__icon" aria-hidden="true">close</span></button>
  </div>
  <p class="modal__body">Body text.</p>
  <div class="modal__footer">
    <button type="button" class="btn btn--blank" onclick="closeModal()"><span class="btn__label">Cancel</span></button>
    <button type="button" class="btn btn--primary"><span class="btn__label">Confirm</span></button>
  </div>
</div>
```

---

---

### Motion

The overlay fades; the panel fades and moves **48px** (`space-48`, via `translate`, so the centering `transform` is untouched): up when it comes in, down when it leaves. **A trial (2026-10-13):** 8px and 24px were tried first. No scale. **Why 48px and no token:** the move is short, so the Fast durations apply. The distance is `space-48` in the keyframes, with no distance token or custom property: Carbon, Spectrum and Atlassian tokenize duration and easing only and leave the travel distance to the component. Add a shared distance scale only when a second component needs the same move. Everything below is for both. **Enter:** `--ease-decelerate-emphasized`, `--duration-fast-4` (200 ms). **Exit (added 2026-10-13):** `--ease-accelerate-generic`, `--duration-fast-3` (150 ms): an element that disappears accelerates, and a modal closes faster than it opens (as Material, Carbon and Atlassian do; Material also scales 0.9 to 1, ECO does not). Override with `--modal-in-ease` / `--modal-in-duration` / `--modal-out-ease` / `--modal-out-duration` on `<html>`. `openModal` adds `is-leaving` to the panel and the overlay and removes them when the animation has run (`.modal.is-leaving`, `@keyframes modal-out`); `onClose`, the scroll unlock and the focus return happen at once. Reduced motion: no fade, removed at once. Live comparison: the **Motion** section on `eco-design-system/components/modal.html`.
