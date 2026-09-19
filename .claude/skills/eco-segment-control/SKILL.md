---
name: eco-segment-control
description: Use when building or reviewing a segmented control (pill toggle) for switching between two related views/filters in the same surface — sizes, the sliding-pill interaction, and states. Never replaces Tabs or Radio buttons.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Segment Control (ECO Design System)

**Figma:** https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=23144-268049

Segment Control (segmented control / "pill toggle") is used to switch between two related views or filters in the same surface — e.g. `User roles / Company plan` or `All features / Key features`. Should **not** be used as a replacement for Tabs (navigation between different pages/content) or Radio buttons (submitted form choices).

> Example implementation: `.compare-view-toggle`/`.compare-view-btn` (Large) and `.compare-filter-toggle`/`.compare-filter-btn` (Small) in `feature-comparison-roles.html`.

### Variants

| Variant | Background (track) | Used on |
|---|---|---|
| **Primary** | `var(--color-surface-15)`→hover, `var(--color-surface-disabled)` `var(--color-surface-disabled)` enabled | Light background (standard) |
| **Primary Inverted** | Corresponding dark variant | Dark/black background |

**Shape:** `Pill` (fully rounded corners — `border-radius: height / 2`, default choice) or `Square` (sharp corners, `border-radius: 0`, used sparingly).

### Sizes

Track padding scales with size (~1px less on mobile than desktop for each size). The track's `border-radius` is always `height / 2`; the active segment's pill radius is `track radius − track padding`.

**Width:** The control is **fluid (`width: 100%`) only at `breakpoint-xs`** (0–639px) — it fills its parent's width, and the two segments share the space evenly (`flex: 1` on each `.segment-control__btn`). Already at `sm:` (640px+) it stops being fluid and shrinks to its content (`width: auto`, `flex: none` on the buttons) — height/padding/font don't change until `md:` (769px+), though, so sm still has mobile size but content-based width. If the control sits in a flex-column parent with default `align-items: stretch` (e.g. `.compare-header-row__right`), `align-self: flex-start` is also required from `sm:` onward — otherwise the parent stretches it out despite `width: auto`. See `.compare-view-toggle`/`.compare-filter-toggle` in `feature-comparison-roles.html` for the verified implementation.

| Size | Height Desktop (`md:` 769px+) | Height Mobile (≤768px) | Text | Used for |
|---|---|---|---|---|
| **Large** | 56px, padding `5px`, radius `28px`, pill radius `23px`, pill padding `24px`, `label-lg` (18px/18px, 0.18px) | 48px, padding `4px`, radius `24px`, pill radius `20px`, pill padding `20px`, `label-lg` mobile (16px/16px, 0.32px) | `label-lg` | Primary view switcher (page level) |
| **Medium** | 48px, padding `4px`, radius `24px`, pill radius `20px`, pill padding `20px`, `label-lg` (18px/18px, 0.18px) | 40px, padding `4px`, radius `20px`, pill radius `16px`, pill padding `16px`, `label-lg` mobile (16px/16px, 0.32px) | `label-lg` | Medium-sized view switcher (e.g. in a drawer) |
| **Small** | 40px, padding `4px`, radius `20px`, pill radius `16px`, pill padding `16px`, `label-md` (16px/16px, 0.48px) | 32px, padding `3px`, radius `16px`, pill radius `13px`, pill padding `12px`, `label-md` mobile (14px/14px, 0.42px) | `label-md` | Secondary filters within a surface (e.g. "Key features") |
| **XSmall** | 32px, padding `3px`, radius `16px`, pill radius `13px`, pill padding `12px`, `label-sm` (14px/14px, 0.56px) | 32px, padding `3px`, radius `16px`, pill radius `13px`, pill padding `10px`, `label-sm` mobile (12px/12px, 0.48px) | `label-sm` | Compact filters in a tight surface (e.g. a table toolbar) |

> XSmall has the same height (32px) on both desktop and mobile — only pill padding (12px/10px) and font size (14px/12px) differ between breakpoints.

### States

| State | Visual rule |
|---|---|
| **Enabled** | Track: `var(--color-surface-disabled)` `var(--color-surface-disabled)`. Active segment: black pill (`var(--color-surface-100)`) with an `elevation-input_control-switch` shadow, white text. Inactive segment: transparent, black text, no underline. The pill is its **own, separate `.segment-control__thumb` element** that slides between the segments — see **Interaction (sliding pill)** below — not a background set directly on the active button. |
| **Hover** | The track darkens to `var(--color-border-tertiary)` `var(--color-border-tertiary)`. The **inactive** segment's text gets `text-decoration: underline` (same hover principle as Action Link). The active segment doesn't change. |
| **Focus** | **No dedicated focus style on the control.** The individual segment buttons are regular `<button>` elements and inherit the project's global focus ring (see **Button Styling → States → Focus**: `body.keyboard-nav button:focus { outline-color: var(--color-border-focus) }`), visible only on keyboard navigation. **Never** build a separate `::after`/border-based focus ring for Segment Control — that would diverge from the established outline method and duplicate the focus indication. |
| **Disabled** | Rarely used for this component in the product — if needed, pull the exact spec from the Figma node (`State=Disabled`) before implementing. |

### Interaction (sliding pill)

The active segment's pill is **not** a background set directly on the button — it's its own `.segment-control__thumb` element positioned absolutely behind the buttons that **slides** to the active button's position/width. This is needed because the buttons can be different widths (content-based width on desktop, `flex: none`) — a fixed 50/50 split of the thumb would then land in the wrong place.

1. The thumb is measured/positioned with JS via the active button's `offsetLeft`/`offsetWidth` (not CSS `%`, see `moveSegmentThumb()` below).
2. The buttons themselves are transparent (`position: relative; z-index: 1`) and sit on top of the thumb — only the text color changes on `--active`.
3. Thumb transition: `transform`/`width` with **`var(--duration-medium-2) var(--ease-standard)`** (300ms, ease-in-out — calm start, fast middle, calm finish). This deliberately differs from the hover transitions (`--duration-fast-3`/`--ease-standard`, see the States table above) since the pill travels a visible distance and should feel smooth, not fast/hover-like.
4. Re-measure the thumb's position on `resize` (the buttons' width changes at the `md:` breakpoint) and on page load.

### CSS template (Large, Primary/Pill — mobile-first)

```css
.segment-control {
  position: relative;
  display: flex;
  width: 100%;                  /* fluid — breakpoint-xs (0–639px) only */
  height: 48px;                 /* mobile */
  padding: 4px;
  background: var(--color-surface-disabled);
  border-radius: 24px;
  box-sizing: border-box;
  transition: background-color var(--duration-fast-3) var(--ease-standard);
}
.segment-control:hover { background: var(--color-border-tertiary); }

@media (min-width: 640px) {
  /* sm+ (Tablet and up): the control stops being fluid here already and
     shrinks to its content — height/padding is still mobile-sized,
     though, until md: (769px). If the parent is a flex-column with
     align-items:stretch (default), align-self: flex-start is also
     required here, otherwise the control gets stretched out despite
     width:auto. */
  .segment-control { width: auto; }
}
@media (min-width: 769px) {
  .segment-control { height: 56px; padding: 5px; border-radius: 28px; }
}

/* The sliding pill — see "Interaction (sliding pill)" above.
   Width/position are set by moveSegmentThumb(), not by CSS. */
.segment-control__thumb {
  position: absolute;
  top: 4px;
  bottom: 4px;
  left: 0;
  width: 0;
  background: var(--color-surface-100);
  border-radius: 20px;
  box-shadow: 0px 4px 8px 0px rgba(48,49,51,0.10), 0px 1px 1px 0px rgba(48,49,51,0.24), 0px -1px 1px 0px rgba(0,0,0,0.03); /* elevation-input_control-switch */
  transition: transform var(--duration-medium-2) var(--ease-standard), width var(--duration-medium-2) var(--ease-standard);
  pointer-events: none;
}
@media (min-width: 769px) {
  .segment-control__thumb { top: 5px; bottom: 5px; border-radius: 23px; }
}
/* If the control already sits on a dark/gray surface (e.g. a filter
   inside another, larger segment-control — see .compare-filter-toggle),
   the pill should be white instead of black: */
.segment-control__thumb--light { background: var(--color-surface-raised-primary); }

.segment-control__btn {
  position: relative;
  z-index: 1;
  flex: 1;                       /* xs: fills the segments evenly */
  display: inline-flex;
  align-items: center;
  justify-content: center;
  height: 100%;
  padding: 0 20px;
  background: transparent;
  border: none;
  border-radius: 20px;
  cursor: pointer;
  font-family: 'Breuer Condensed', Arial, sans-serif;
  font-size: 16px;               /* label-lg Mobile */
  font-weight: 700;
  line-height: 16px;
  letter-spacing: 0.32px;
  text-transform: uppercase;
  color: var(--color-text-action-primary);
  white-space: nowrap;
  font-feature-settings: 'ss02' 1, 'ss03' 1;
  transition: color var(--duration-fast-3) var(--ease-standard);
}
@media (min-width: 640px) {
  .segment-control__btn { flex: none; }   /* sm+: content-based width, matches the control's width:auto */
}
@media (min-width: 769px) {
  .segment-control__btn { padding: 0 24px; border-radius: 23px; font-size: 18px; line-height: 18px; letter-spacing: 0.18px; }
}

/* Inactive segment — hover adds an underline */
.segment-control__btn:not(.segment-control__btn--active):hover { text-decoration: underline; }

/* Active segment — only the text color changes, the pill is already
   underneath (black pill → white text). With .segment-control__thumb--light
   (white pill) the text should NOT change — keep it black throughout. */
.segment-control__btn--active { color: var(--color-text-action-primary-inverted); }

/* Medium — medium-sized view switcher (e.g. in a drawer) */
.segment-control--md { height: 40px; padding: 4px; border-radius: 20px; }
.segment-control--md .segment-control__thumb { top: 4px; bottom: 4px; border-radius: 16px; }
.segment-control--md .segment-control__btn { padding: 0 16px; border-radius: 16px; font-size: 16px; line-height: 16px; letter-spacing: 0.32px; }
@media (min-width: 769px) {
  .segment-control--md { height: 48px; padding: 4px; border-radius: 24px; }
  .segment-control--md .segment-control__thumb { top: 4px; bottom: 4px; border-radius: 20px; }
  .segment-control--md .segment-control__btn { padding: 0 20px; border-radius: 20px; font-size: 18px; line-height: 18px; letter-spacing: 0.18px; }
}

/* Small — secondary filters (e.g. "Key features") */
.segment-control--sm { height: 32px; padding: 3px; border-radius: 16px; }
.segment-control--sm .segment-control__thumb { top: 3px; bottom: 3px; border-radius: 13px; }
.segment-control--sm .segment-control__btn { padding: 0 12px; border-radius: 13px; font-size: 14px; line-height: 14px; letter-spacing: 0.42px; }
@media (min-width: 769px) {
  .segment-control--sm { height: 40px; padding: 4px; border-radius: 20px; }
  .segment-control--sm .segment-control__thumb { top: 4px; bottom: 4px; border-radius: 16px; }
  .segment-control--sm .segment-control__btn { padding: 0 16px; border-radius: 16px; font-size: 16px; line-height: 16px; letter-spacing: 0.48px; }
}

/* XSmall — compact filters in a tight surface (e.g. a table toolbar).
   Same height on mobile and desktop — only pill padding and font change. */
.segment-control--xs { height: 32px; padding: 3px; border-radius: 16px; }
.segment-control--xs .segment-control__thumb { top: 3px; bottom: 3px; border-radius: 13px; }
.segment-control--xs .segment-control__btn { padding: 0 10px; border-radius: 13px; font-size: 12px; line-height: 12px; letter-spacing: 0.48px; }
@media (min-width: 769px) {
  .segment-control--xs .segment-control__btn { padding: 0 12px; font-size: 14px; line-height: 14px; letter-spacing: 0.56px; }
}
```

### HTML and JS example

```html
<div class="segment-control" role="group" aria-label="Select view">
  <span class="segment-control__thumb" aria-hidden="true"></span>
  <button type="button" class="segment-control__btn segment-control__btn--active" onclick="setView('roles', this)">User roles</button>
  <button type="button" class="segment-control__btn" onclick="setView('company', this)">Company plan</button>
</div>
```

```js
// Slides the pill to the active button's position/width — see
// "Interaction (sliding pill)" above for why offsetLeft/offsetWidth
// is used instead of a fixed CSS % split.
function moveSegmentThumb(thumb, activeBtn) {
  if (!thumb || !activeBtn) return;
  thumb.style.width = activeBtn.offsetWidth + 'px';
  thumb.style.transform = 'translateX(' + activeBtn.offsetLeft + 'px)';
}

function setView(view, btn) {
  btn.parentElement.querySelectorAll('.segment-control__btn').forEach(function (b) {
    b.classList.toggle('segment-control__btn--active', b === btn);
  });
  moveSegmentThumb(btn.parentElement.querySelector('.segment-control__thumb'), btn);
  // ... show/hide the respective view ...
}

// Initialize on page load and re-measure on resize (the buttons' width
// changes at the md: breakpoint, 769px).
function initSegmentThumb(control) {
  moveSegmentThumb(control.querySelector('.segment-control__thumb'), control.querySelector('.segment-control__btn--active'));
}
document.querySelectorAll('.segment-control').forEach(initSegmentThumb);
window.addEventListener('resize', function () {
  document.querySelectorAll('.segment-control').forEach(initSegmentThumb);
});
```

---
