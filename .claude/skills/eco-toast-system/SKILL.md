---
name: eco-toast-system
description: Use when building a system-generated Toast notification — short-lived, time-based feedback on a user action (save/send/delete) that slides in/out and auto-closes.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

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
| **Success** | `var(--color-text-success)` | `var(--color-surface-success-weaker)` (`surface-success-weaker`) | `check_circle` |
| **Warning** | `var(--color-border-warning-default)` | `var(--color-surface-warning-weaker)` (`surface-warning-weaker`) | `warning_amber` |

#### Layout variants
| Variant | Content |
|---|---|
| **Default** | Status icon + [Title (optional) + body text] + Close button |
| **Actionable** | Same as Default + one or more Blank buttons below the text |

---

### Anatomy

```
[Status icon 24px] [Title (optional) — title-sm]   [✕ close 20px]
                  [Body text — body-md           ]
                  [Blank button (Actionable only)]
```

- **Left border**: `2px solid [status color]`, full height
- **Padding**: `16px` inside, `8px` gap between icon and text block
- **Close button**: Blank xs, `close` icon 20px, `padding: 2px`
- **Shadow**: `elevation-b-80` = `var(--shadow-elevation-b-80)`

---

### Typography

| Element | Token | Value |
|---|---|---|
| Title (optional) | `title-sm` | 16px/18px, Bold, 0px tracking, `text-primary` (var(--color-text-primary)) |
| Body text | `body-md` | 16px/24px, Regular, 0.32px tracking, `text-primary` (var(--color-text-primary)) |

---

### CSS template

```css
.toast {
  display: flex;
  flex-direction: column;
  width: 375px;
  box-shadow: var(--shadow-elevation-b-80);
}

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
}

.toast__body { flex: 1; display: flex; flex-direction: column; gap: 2px; }

.toast__title {
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 16px;
  font-weight: 700;
  line-height: 18px;
  letter-spacing: 0px;
  color: var(--color-text-primary);
  font-feature-settings: 'ss02' 1, 'ss03' 1;
}

.toast__text {
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 24px;
  letter-spacing: 0.32px;
  color: var(--color-text-primary);
  font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1;
}

.toast__close {
  flex-shrink: 0;
  background: transparent;
  border: none;
  cursor: pointer;
  padding: 2px;
  font-size: 20px;
  color: var(--color-text-primary);
}
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

> On `xs`, the toast animates in from the top instead of from the right. The width is always `375px` on sm and up, and fills the full viewport width on xs.

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
| Enter easing | `cubic-bezier(0.16, 0, 0.16, 1)` (`ease-decelerate-emphasized`) |
| Exit direction | To the right (`xs`: upward) |
| Exit easing | `cubic-bezier(0.36, 0.09, 1, 0.58)` (`ease-accelerate-generic`) |
| Duration | `300ms` |
| Auto-hide | `4000ms` |

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
      ? 'toast-slide-out-top 300ms cubic-bezier(.36,.09,1,.58) forwards'
      : 'toast-slide-out 300ms cubic-bezier(.36,.09,1,.58) forwards';
    setTimeout(function(){ toast.remove(); }, 300);
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
