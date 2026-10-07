---
name: eco-toast-system
description: Use when building a system-generated Toast notification — short-lived, time-based feedback on a user action (save/send/delete) that slides in/out and auto-closes.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

> **Buttons and ×:** buttons and the close button follow `eco-button` (see `notifications-guide`, "Buttons and the close button"): `btn btn--primary|secondary|blank` with `<span class="btn__label">`, always 32px (XSmall from 769px, Small below), and the × is `icon-btn icon-btn--close` (`icon-btn--close-inverted` on dark/solid surfaces). Live CSS: `eco-design-system/notifications.css`.

> **Custom icon (Informational only):** the author may replace the default `info` icon with another from the gallery. The author enters the Google Material Symbols name; it renders as **Outlined, Fill 0, Weight 300, Grade 0** (`font-variation-settings: 'FILL' 0, 'wght' 300, 'GRAD' 0`, class `icon-outline`); the default status icons stay filled. See `notifications-guide`.

## Notification – System Toast (ECO Design System)

**Figma:** https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=13377-29321

### Used when
- Responding to a user action (save, send, delete)
- A system event that needs the user's attention
- A short-lived message that doesn't block the interface

### NOT used when
- The error message is for a single form field → use `form-helper--error` instead
- The message is permanent → use an inline notification or a banner
- The action requires confirmation → use a Modal

---

### Usage guidance per status

| Status | Usage guidance | Action |
|---|---|---|
| **Informational** | Passive background status confirmations, such as "Syncing files in background…". Immediate action isn't required — the toast can auto-dismiss after a set time or persist depending on content. | Supports quick undo actions or a small dismiss "×". |
| **Success** | Confirms an immediate positive outcome: "Product added to cart", "Copied to clipboard", "Folder created". | Typically no further action needed — can resolve automatically or persist without causing disruption. |
| **Warning** | Warns of soft errors, e.g. "Poor network connection. Retrying…". | May remain on screen until the user dismisses it or proceeds with their task. Dismissible or persistent depending on content. |
| **Error** | Brief alerts about a background process crash: "Failed to upload attachment". | Probably requires immediate action — should include a retry CTA directly inside the toast. Stays until the user dismisses it or the error is resolved. |

All four statuses support **Strong / Weak** emphasis.

---

### Variants

#### Emphasis
| Emphasis | Background | Left border |
|---|---|---|
| **System Strong** | The status color's weak background (see table below) | `2px solid [status color]` |
| **System Weak** | `var(--color-surface-raised-primary)` (`surface-raised-primary`) | `2px solid [status color]` |

#### Status + colors

| Status | Border / Icon color | Strong background | Material Symbol |
|---|---|---|---|
| **Informational** | `var(--color-border-information-default)` | `var(--color-surface-information-weaker)` (`surface-information-weaker`) | `info` |
| **Error** | `var(--color-border-danger-default)` | `var(--color-surface-danger-weaker)` (`surface-danger-weaker`) | `error` |
| **Success** | `var(--color-text-success-default)` | `var(--color-surface-success-weaker)` (`surface-success-weaker`) | `check_circle` |
| **Warning** | `var(--color-border-warning-default)` | `var(--color-surface-warning-weaker)` (`surface-warning-weaker`) | `warning` |

#### Layout variants
| Variant | Content |
|---|---|
| **Default** | Status icon + [Title (optional) + body text] + Close button |
| **Actionable** | Same as Default + an action area below the text (indent `32px`, `16px` above it) that holds **either buttons or inline links**, not both. Links: `.toast__links`, `8px` row / `16px` column gap |

---

### Anatomy

```
[Status icon 24px] [Title (optional) — title-sm]   [✕ close 20px]
                  [Body text — body-md           ]
                  [Secondary button] [Primary button]   ← Actionable only
                  [Inline link] [Inline link]            ← Actionable only, instead of the buttons
```

- **Left border**: `2px solid [status color]`, full height
- **Padding**: `16px` inside, `8px` gap between icon and text block
- **Close button**: Blank xs, `close` icon 20px, `padding: 2px`
- **Actionable footer** (2026-09 Figma): Secondary + Primary button (`gap: 8px`, Primary `flex: 1`) and an Inline Link `body-md` underlined below. Buttons: desktop = xs (`padding: 6px`, `label-sm`), tablet/mobile = sm (`padding: 4px`, `label-md`), both 32px tall.
- **Shadow**: `elevation-b-80` = `var(--shadow-elevation-b-80)`

---

### Typography

| Element | Token | Value |
|---|---|---|
| Title (optional) | `title-sm` | 16px/18px, Bold, 0px tracking, `text-primary` (var(--color-text-primary)) |
| Body text | `body-md` | Desktop 17px/24px, Mobile/Tablet 16px/22px, Regular, 0.32px tracking, `text-primary` (var(--color-text-primary)) |

---

### CSS template

```css
.toast {
  display: flex;
  flex-direction: column;
  width: 100%;                /* xs (below 640px): the toast fills the whole viewport width, in the page as well as in a preview */
  box-shadow: var(--shadow-elevation-b-80);
}
@media (min-width: 640px) { .toast { width: 375px; max-width: 100%; } }

.toast__inner {
  display: flex;
  align-items: flex-start;
  padding: 16px;
  gap: 8px;
  border-left: 2px solid var(--status-color);
  position: relative;
}

/* System Strong — colored background */
.toast--strong.toast--info    { background: var(--color-surface-information-weaker); --status-color: var(--color-surface-information-default); }
.toast--strong.toast--error   { background: var(--color-surface-danger-weaker);      --status-color: var(--color-surface-danger-default); }
.toast--strong.toast--success { background: var(--color-surface-success-weaker);     --status-color: var(--color-surface-success-default); }
.toast--strong.toast--warning { background: var(--color-surface-warning-weaker);     --status-color: var(--color-surface-warning-default); }

/* System Weak — white background */
.toast--weak.toast--info    { background: var(--color-surface-raised-primary); --status-color: var(--color-surface-information-default); }
.toast--weak.toast--error   { background: var(--color-surface-raised-primary); --status-color: var(--color-surface-danger-default); }
.toast--weak.toast--success { background: var(--color-surface-raised-primary); --status-color: var(--color-surface-success-default); }
.toast--weak.toast--warning { background: var(--color-surface-raised-primary); --status-color: var(--color-surface-warning-default); }

.toast__icon {
  font-size: 24px;
  color: var(--status-color);
  flex-shrink: 0;
  font-variation-settings: 'FILL' 1, 'wght' 300, 'GRAD' 0, 'opsz' 24;  /* Filled, wght 300: without this a plain Material Symbols span renders outline */
}

.toast__body { flex: 1; display: flex; flex-direction: column; gap: 2px; }

.toast__title {
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 16px;
  font-weight: 600;
  line-height: 18px;
  letter-spacing: 0px;
  color: var(--color-text-primary);
  font-feature-settings: 'ss02' 1, 'ss03' 1;
}

.toast__text {
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 17px;          /* body-md desktop; 16px/22px below 769px */
  font-weight: 400;
  line-height: 24px;
  letter-spacing: 0.32px;
  color: var(--color-text-primary);
  font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1;
}

@media (max-width: 768px) {
  .toast__text { font-size: 16px; line-height: 22px; }
}



/* Buttons and ×: eco-button classes (.btn, .icon-btn.icon-btn--close); live CSS in eco-design-system/notifications.css */
```

---

### Position per breakpoint

The toast is `position: fixed`. Always slides in from the right — except on `xs`, where it comes from the top.

| Breakpoint | Top | Right | Left | Width |
|---|---|---|---|---|
| `lg` (1024px+) | `40px` | `40px` | auto | `375px` |
| `md` (769–1023px) | `32px` | `32px` | auto | `375px` |
| `sm` (640–768px) | `32px` | `32px` | auto | `375px` |
| `xs` (0–639px) | `0px` | `0px` | `0px` | `100vw` (fills the full viewport width) |

> **xs (below 640px):** the toast **fills the whole viewport width**, flush with the top, left and right edges, and **enters from the top and leaves upward** (`toast-slide-in-top` / `toast-slide-out-top`); there is no gap to the screen edge. The width is `375px` from 640px and up. The same applies to the E-Com Toast (Add to cart and Informational) and to a toast shown as a static preview: below 640px a `.toast` is `width: 100%`, not a fixed 375px card. Checked at 375, 500 and 639px (the 15px difference seen in a desktop browser is the scrollbar).

```css
.toast-container {
  position: fixed;
  z-index: 9999;
  top: 40px;
  right: 40px;
  width: 375px;
}

@media (max-width: 1023px) {
  .toast-container { top: 32px; right: 32px; }
}

@media (max-width: 639px) {
  .toast-container {
    top: 0;
    right: 0;
    left: 0;
    width: 100vw;
  }
}
```

---

### Animation

| Property | Value |
|---|---|
| Enter direction | From the right (`xs`: from the top) |
| Enter easing | `var(--ease-decelerate-emphasized)` (`cubic-bezier(.16, 0, .16, 1)`, `eco-motion`) |
| Exit direction | To the right (`xs`: upward) |
| Exit easing | `var(--ease-accelerate-generic)` (`cubic-bezier(.36, .09, 1, .58)`, `eco-motion`) |
| Duration | `var(--duration-medium-2)` (`300ms`), enter and exit |
| Override | `--toast-in-ease` / `--toast-in-duration` / `--toast-out-ease` / `--toast-out-duration` (on `<html>` or `.toast-host`); the defaults above are the fallbacks. Live controls: Motion section on `eco-design-system/components/toast.html`. The playground and the code block there link to it (`#motion`). Auto-hide (4s) is not part of it. |
| Auto-hide | `4000ms` (default; `autoHide: <ms>` per call, `0` = stays). The playground on `eco-design-system/components/toast.html` has an Auto-hide On/Off group plus an `eco-range` "Auto-hide time" (2–10 s, step 1, default 4) shown only while On |

**Dismiss triggers:** close button, click outside the toast, auto-hide. All three should run the exit animation — never call `remove()` directly without animating out.

> Start the click-outside listener with `setTimeout(..., 0)` so the click that created the toast (e.g. a confirm button in a modal) doesn't close it immediately.

```css
/* Enter — from the right (lg/md/sm), no fade */
@keyframes toast-slide-in {
  from { transform: translateX(calc(100% + 40px)); }
  to   { transform: translateX(0); }
}
/* Exit — to the right (lg/md/sm), no fade */
@keyframes toast-slide-out {
  from { transform: translateX(0); }
  to   { transform: translateX(calc(100% + 40px)); }
}

/* Enter — from the top (xs), no fade */
@keyframes toast-slide-in-top {
  from { transform: translateY(-100%); }
  to   { transform: translateY(0); }
}
/* Exit — upward (xs), no fade */
@keyframes toast-slide-out-top {
  from { transform: translateY(0); }
  to   { transform: translateY(-100%); }
}
```

```js
function showToast(/* ... */) {
  var isXs = window.innerWidth <= 639;
  var dismissed = false;
  var autoTimer = null;

  // Create and position the toast...
  // xs: top:0; left:0; right:0; width:100vw; animation: toast-slide-in-top ...
  // sm+: top:40px; right:40px; width:375px; animation: toast-slide-in ...

  function dismiss() {
    if (dismissed) return;
    dismissed = true;
    clearTimeout(autoTimer);
    document.removeEventListener('click', outsideClick);
    toast.style.animation = isXs
      ? 'toast-slide-out-top var(--duration-medium-2) var(--ease-accelerate-generic) forwards'
      : 'toast-slide-out var(--duration-medium-2) var(--ease-accelerate-generic) forwards';
    // wait for the exit animation: its length is the duration token set in the CSS, so read it instead of hardcoding 300
    var ms = parseFloat(getComputedStyle(toast).animationDuration) * 1000 || 0;
    setTimeout(function(){ toast.remove(); }, ms + 20);
  }

  function outsideClick(e) {
    if (!toast.contains(e.target)) dismiss();
  }

  closeBtn.addEventListener('click', dismiss);
  document.body.appendChild(toast);
  setTimeout(function(){ document.addEventListener('click', outsideClick); }, 0);
  autoTimer = setTimeout(dismiss, 4000);
}
```

---
