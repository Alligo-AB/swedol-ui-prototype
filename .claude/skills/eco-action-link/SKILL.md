---
name: eco-action-link
description: Use when building a standalone clickable link with an optional left/right icon that is NOT in body text — e.g. "View all products →".
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Action Link (ECO Design System)

**Figma:** https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=1671-52811

A clickable link with an optional left icon and a right arrow. Used for navigation and downloads.

---

### Anatomy

```
[Left icon (optional)] [Link text] [→ chevron icon]
```

- The link text is **not** underlined in the Enabled state — the underline shows **only** on hover.
- Right icon: `chevron_right` (Large: 24px, Medium/Small: 20px)
- Left icon (optional, e.g. `file_download`): Large: 24px, Medium/Small: 20px
- **IMPORTANT:** Icons must **never** get an underline on hover — only the link text should be underlined. Set `text-decoration: none` explicitly on the icon element (`.action-link .ms`), otherwise the icon inherits `text-decoration: underline` from the hovered link.

---

### Sizes

#### Desktop (`md:`, 769px+)

| Size | Typography token | Font-size | Line-height | Letter-spacing | Gap | Icon |
|---|---|---|---|---|---|---|
| **Large** | `body-lg` | 20px | 28px | 0px | 8px | 24px |
| **Medium** | `body-md` | 16px | 24px | 0.32px | 4px | 20px |
| **Small** | `body-sm` | 14px | 20px | 0.28px | 4px | 20px |

#### Mobile / Tablet (`xs`/`sm`, ≤768px)

| Size | Font-size | Line-height | Letter-spacing |
|---|---|---|---|
| **Large** | 18px | 24px | 0px |
| **Medium** | 16px | 22px | 0.32px |
| **Small** | 14px | 20px | 0.28px |

> Small has the same values on desktop and mobile.

---

### Variants

| Variant | Enabled color | Hover color |
|---|---|---|
| **Text Primary** | `var(--color-text-action-primary)` (`text-action-primary`) | `var(--color-text-action-secondary-hover)` (`text-action-secondary-hover`) |
| **Text Primary Inverted** | `var(--color-text-action-primary-inverted)` (`text-primary-inverted`) | `var(--color-text-action-primary-inverted-hover)` (`text-action-primary-inverted-hover`) |

**Font-weight:** Regular (400) or Bold (700). Both variants exist in every size.

---

### States

| State | Underline | Text color |
|---|---|---|
| **Enabled** | None | `text-action-primary` / `text-primary-inverted` |
| **Hover** | `text-decoration: underline` | `text-action-secondary-hover` / `text-action-primary-inverted-hover` |

> Transition: `color` and `text-decoration-color` with `duration-fast-3` (150ms) and `ease-standard`.

---

### font-feature-settings

| Size | Value |
|---|---|
| Large (`body-lg`) | `'ss02' 1, 'ss03' 1` |
| Medium (`body-md`) | `'ss02' 1, 'ss03' 1, 'ss06' 1` |
| Small (`body-sm`) | `'ss02' 1, 'ss03' 1, 'ss06' 1` |

---

### CSS template

```css
.action-link {
  display: inline-flex;
  align-items: center;
  gap: 8px;                /* Large */
  text-decoration: none;
  color: var(--color-text-action-primary);          /* text-action-primary */
  font-family: 'Breuer Condensed', Arial, sans-serif;
  font-weight: 400;
  cursor: pointer;
  transition: color 150ms cubic-bezier(.35,0,.35,1); /* duration-fast-3, ease-standard */
}

/* Sizes */
.action-link--large  { font-size: 20px; line-height: 28px; letter-spacing: 0px;    font-feature-settings: 'ss02' 1, 'ss03' 1; }
.action-link--medium { font-size: 16px; line-height: 24px; letter-spacing: 0.32px; font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1; gap: 4px; }
.action-link--small  { font-size: 14px; line-height: 20px; letter-spacing: 0.28px; font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1; gap: 4px; }

/* Hover */
.action-link:hover { color: var(--color-text-action-primary-hover); text-decoration: underline; }

/* Icons must never get an underline, only the link text */
.action-link .ms { text-decoration: none; }

/* Inverted (on a dark background) */
.action-link--inverted       { color: var(--color-text-action-primary-inverted); }
.action-link--inverted:hover { color: var(--color-text-action-primary-inverted-hover); }

/* Bold variant */
.action-link--bold { font-weight: 700; }

/* Mobile */
@media (max-width: 768px) {
  .action-link--large  { font-size: 18px; line-height: 24px; }
  .action-link--medium { font-size: 16px; line-height: 22px; }
}
```

### HTML example

```html
<!-- Large, Regular, with icon -->
<a href="#" class="action-link action-link--large">
  <span class="material-symbols-outlined" style="font-size:24px">file_download</span>
  Download document
  <span class="material-symbols-outlined" style="font-size:24px">chevron_right</span>
</a>

<!-- Medium, Regular -->
<a href="#" class="action-link action-link--medium">
  View all products
  <span class="material-symbols-outlined" style="font-size:20px">chevron_right</span>
</a>

<!-- Small, Bold, Inverted -->
<a href="#" class="action-link action-link--small action-link--bold action-link--inverted">
  Read more
  <span class="material-symbols-outlined" style="font-size:20px">chevron_right</span>
</a>
```

---
