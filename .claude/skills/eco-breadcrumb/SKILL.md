---
name: eco-breadcrumb
description: Use when building breadcrumbs for page-hierarchy navigation — placed directly under the header as the first element in `.page`.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Breadcrumb (ECO Design System)

**Figma – design:** https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=1986-64264
**Figma – responsive behavior per breakpoint:** https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=9071-123361

Breadcrumb is used to show the user's position in the page hierarchy and enable quick navigation upward through the structure (e.g. `Home / Category / Subpage`). Placed directly under the header, as the first element inside the page's content wrapper (`.page`).

### Used when
- The page sits more than one step down the navigation tree (PLP, PDP, landing pages, category pages).
- The user needs to be able to go back to a level above without using the browser's back button.

### NOT used when
- The page is the homepage or sits directly under Home with no meaningful intermediate level.
- Navigation is already covered by tabs or a clear back link in the same view (avoid duplication).

---

### Anatomy

```
[Home]  /  [Intermediate step]  /  [Current page]
```

- Each breadcrumb renders as a **bordered box** (`border: 1px solid` `border-action-3` = `var(--color-border-action-3)`), never as underlined text/a link.
- The separator between breadcrumbs is a `/` character, centered in a fixed `4px` width.
- The container has **no background color of its own** — it always sits against the page's `body` background. Which color that is depends on the page type (see rule 7).
- Every breadcrumb except the last is a clickable link (`Enabled` style). The **last** breadcrumb represents the current page (`Active` style) — bold, black text, not clickable.
- The component has built-in vertical spacing (padding) — see rule 1 below for how that affects the following section.

---

### Sizes per breakpoint

| Breakpoint | Height (bar) | Crumb padding | Text | Separator (height) | Container: horizontal padding | Container: extra bottom padding |
|---|---|---|---|---|---|---|
| `xs` Mobile (0–639px) | 56px | `6px 7px` | 12px/12px, 0.24px | 24px | `var(--px-page)` (16px) | 0px |
| `sm` Tablet (640–768px) | 56px | `6px 7px` | 12px/12px, 0.24px | 24px | `var(--px-page)` (32px) | 0px |
| `md` Desktop Small (769–1023px) | 72px | `9px 10px` | 14px/14px, 0.28px | 32px | `var(--px-page)` (32px) | 8px |
| `lg` / `xl` Desktop (1024px+) | 80px | `9px 10px` | 14px/14px, 0.28px | 32px | `var(--px-page)` (40px) | 16px |

> `xs` and `sm` are identical except for horizontal page margin. `md`, `lg`, and `xl` share the same crumb/text size — the only difference is how much extra bottom padding the container gets beyond the bar's own `16px` (top+bottom).
> **Always** use `var(--px-page)` (the grid margin per breakpoint) for horizontal padding — never a hardcoded pixel value or `var(--px-full)`, since the breadcrumb sits inside `.page`, which is already width-constrained.

---

### States

| State | Border | Text color | Underline | Font-weight | Cursor |
|---|---|---|---|---|---|
| **Enabled** (not last) | `1px solid border-action-3` | `text-tertiary` (var(--color-text-tertiary)) | No | Regular (400) | pointer |
| **Hover** (not last) | `1px solid border-action-3` | `text-action-primary` (var(--color-text-action-primary)) | **Yes** | Regular | pointer |
| **Active** (last/current page) | `1px solid border-action-3` | `text-primary` (var(--color-text-primary)) | No | Bold (700) | default |

> Hover **only** changes the text color (to `text-action-primary`) and adds an underline — the box's border and background (transparent) don't change.
> The `Active` breadcrumb **never** gets a hover underline — it isn't clickable and has no `href`/click handler.

---

### CSS template

```css
.breadcrumb { padding: 0 var(--px-page) 0; }
.breadcrumb__bar {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px;
  padding: 16px 0;
}
.breadcrumb-item {
  display: inline-flex;
  align-items: center;
  border: 1px solid var(--color-border-action-3);
  padding: 6px 7px;
  background: none;
  cursor: pointer;
  text-decoration: none;
  white-space: nowrap;
  font-family: 'Breuer Condensed', Arial, sans-serif;
  font-size: 12px;
  font-weight: 400;
  line-height: 12px;
  letter-spacing: 0.24px;
  color: var(--color-text-tertiary);
  font-feature-settings: 'ss02' 1, 'ss03' 1;
  transition: color var(--duration-fast-3) var(--ease-standard);
}
.breadcrumb-item:hover {
  color: var(--color-text-action-primary);
  text-decoration: underline;
}
.breadcrumb-item--active {
  font-weight: 700;
  color: var(--color-text-primary);
  cursor: default;
}
.breadcrumb-item--active:hover { text-decoration: none; }
.breadcrumb-sep {
  flex-shrink: 0;
  width: 4px;
  height: 24px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--color-text-tertiary);
  font-family: 'Breuer Condensed', Arial, sans-serif;
  font-size: 14px;
  font-weight: 400;
  letter-spacing: 0.28px;
}

/* md: Desktop Small */
@media (min-width: 769px) {
  .breadcrumb { padding-bottom: 8px; }
  .breadcrumb-item { padding: 9px 10px; font-size: 14px; line-height: 14px; letter-spacing: 0.28px; }
  .breadcrumb-sep { height: 32px; }
}
/* lg + xl: Desktop */
@media (min-width: 1024px) {
  .breadcrumb { padding-bottom: 16px; }
}

/* The component has built-in spacing — zero out the top padding on a
   directly following section/title block (see Section rule 4 below). */
.breadcrumb + .main-content,
.breadcrumb + .section,
.breadcrumb + .section--first {
  padding-top: 0;
}
```

### HTML example

```html
<!-- 2 levels -->
<nav class="breadcrumb" aria-label="Breadcrumb">
  <div class="breadcrumb__bar">
    <a href="#" class="breadcrumb-item">Home</a>
    <span class="breadcrumb-sep">/</span>
    <span class="breadcrumb-item breadcrumb-item--active" aria-current="page">Reviews</span>
  </div>
</nav>

<!-- Multiple levels (PLP/PDP) -->
<nav class="breadcrumb" aria-label="Breadcrumb">
  <div class="breadcrumb__bar">
    <a href="#" class="breadcrumb-item">Home</a>
    <span class="breadcrumb-sep">/</span>
    <a href="#" class="breadcrumb-item">Clothing and protective gear</a>
    <span class="breadcrumb-sep">/</span>
    <a href="#" class="breadcrumb-item">Work pants</a>
    <span class="breadcrumb-sep">/</span>
    <span class="breadcrumb-item breadcrumb-item--active" aria-current="page">Carpenter pants</span>
  </div>
</nav>
```

### Rules

1. **IMPORTANT — Placement & spacing:** The breadcrumb is always placed directly under the header, as the first element in `.page`, **before** the page's title block (`.main-content`) or first `.section`. Since the component has built-in vertical padding, the directly following element should zero out its top padding (`.breadcrumb + .main-content { padding-top: 0; }`) — per the Section component's rule on "First section with an adjacent component that has built-in spacing".
2. **IMPORTANT — Horizontal padding:** Always use `var(--px-page)`, never `var(--px-full)` or hardcoded pixels, since the breadcrumb sits inside the width-constrained `.page` wrapper.
3. Each breadcrumb is a **bordered box** — never underlined link text, never an icon/chevron between steps. The separator is always the `/` character.
4. Only the **last** breadcrumb gets `.breadcrumb-item--active` (bold, black, `aria-current="page"`, not clickable/no `href`). All preceding ones must be real links (`<a>`).
5. Size (crumb padding, text size, separator height) is controlled solely by breakpoint per the table above — never hardcode a different size for a single page.
6. `aria-label="Breadcrumb"` on the `<nav>` and `aria-current="page"` on the active breadcrumb are mandatory for accessibility.
7. **Background:** `.breadcrumb` sets **no** background color of its own — it sits against `body`'s background, which differs by page type: public/logged-out pages (`template.html`) have `background-primary` (white); pages under My Pages (`mypages-template.html`, same as other my-pages pages) have `background-secondary` (grey) by default — that's intentional, not a bug.

---
