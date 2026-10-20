---
name: eco-action-link
description: Use when building a standalone clickable link with a leading icon, a trailing icon or both that is NOT in body text — e.g. "View all products →".
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Action Link (ECO Design System)

**Figma:** https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=1671-52811

A clickable link with a leading icon, a trailing icon or both. Used for navigation and downloads.

Figma description: "A standalone link with a leading icon, a trailing icon or both, for lightweight actions like downloads and “view all” navigation. Underlined on hover." At least one icon is required. In this design system the icons are named **leading** and **trailing**, never left and right.

---

### Anatomy

```
[Leading icon] [Link text] [Trailing icon (chevron)]   (at least one icon; leading, trailing or both)
```

- The link text is **not** underlined in the Enabled state — the underline shows **only** on hover.
- Trailing icon: `chevron_right` (Large: 24px, Medium/Small: 20px). Figma's link info: the action link "is paired with an icon, leading and trailing or both" and icons are always the same color as the link text. A link without an icon in a text is the **Inline link**, with `inline-link--reverse` (underline on hover only). **The CSS does not support it**: `.action-link:not(:has(.action-link__icon)) { all: revert; }` (last rule in `action-link.css`) drops all styling from an action link with no `.action-link__icon`, so it shows as a default browser link and the mistake is visible.
- Leading icon (e.g. `file_download`): Large: 24px, Medium/Small: 20px
- **IMPORTANT:** Icons must **never** get an underline on hover — only the link text. **Always wrap the text in `<span class="action-link__label">`** and put the underline on that span (`.action-link:hover .action-link__label`), never on `.action-link` itself. The link is a flex container, so its icons are flex items; `text-decoration` set on the link propagates to them and `text-decoration: none` on the icon cannot undo it. Bare text without the span means the icon gets underlined.

---

### Sizes

#### Desktop (`md:`, 769px+)

| Size | Typography token | Font-size | Line-height | Letter-spacing | Gap | Icon |
|---|---|---|---|---|---|---|
| **Large** | `body-lg` | 20px | 28px | 0.18px | 8px | 24px |
| **Medium** | `body-md` | 17px | 24px | 0.32px | 4px | 20px |
| **Small** | `body-sm` | 14px | 20px | 0.36px | 4px | 20px |

#### Mobile / Tablet (`xs`/`sm`, ≤768px)

| Size | Font-size | Line-height | Letter-spacing |
|---|---|---|---|
| **Large** | 18px | 24px | 0.18px |
| **Medium** | 16px | 22px | 0.32px |
| **Small** | 14px | 20px | 0.36px |

> Small has the same values on desktop and mobile.

---

### Variants

| Variant | Enabled color | Hover color |
|---|---|---|
| **Text Primary** | `var(--color-text-action-primary)` (`text-action-primary`) | `var(--color-text-action-secondary-hover)` (`text-action-secondary-hover`, same value as `text-action-primary-hover`) |
| **Text Primary Inverted** | `var(--color-text-action-primary-inverted)` (`text-primary-inverted`) | `var(--color-text-action-primary-inverted-hover)` (`text-action-primary-inverted-hover`) |

**Font-weight:** Regular (400) or Bold (600 in the CSS; 700 in Figma, which is 100 higher). Both variants exist in every size.

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

> **Shared file:** `<link rel="stylesheet" href="/components/css/action-link.css">`. This is the single source; the template below is a reference copy. Never copy the rules into a page. Documentation: three pages, `eco-design-system/components/action-link.html`, `action-link-specifications.html`, `action-link-code.html` (type of the Links guide hub). Icons are `<span class="action-link__icon">`, sizes mobile-first.


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
  transition: color var(--duration-fast-3) var(--ease-standard); /* duration-fast-3, ease-standard */
}

/* Sizes */
.action-link--large  { font-size: 20px; line-height: 28px; letter-spacing: 0.18px; font-feature-settings: 'ss02' 1, 'ss03' 1; }
.action-link--medium { font-size: 17px; line-height: 24px; letter-spacing: 0.32px; font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1; gap: 4px; }
.action-link--small  { font-size: 14px; line-height: 20px; letter-spacing: 0.36px; font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1; gap: 4px; }

/* Hover */
.action-link:hover { color: var(--color-text-action-primary-hover); }
.action-link:hover .action-link__label { text-decoration: underline; }   /* label only, never on .action-link */


/* Inverted (on a dark background) */
.action-link--inverted       { color: var(--color-text-action-primary-inverted); }
.action-link--inverted:hover { color: var(--color-text-action-primary-inverted-hover); }

/* Bold variant */
.action-link--bold { font-weight: 600; }

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
  <span class="action-link__label">Download document</span>
  <span class="material-symbols-outlined" style="font-size:24px">chevron_right</span>
</a>

<!-- Medium, Regular -->
<a href="#" class="action-link action-link--medium">
  <span class="action-link__label">View all products</span>
  <span class="material-symbols-outlined" style="font-size:20px">chevron_right</span>
</a>

<!-- Small, Bold, Inverted -->
<a href="#" class="action-link action-link--small action-link--bold action-link--inverted">
  <span class="action-link__label">Read more</span>
  <span class="material-symbols-outlined" style="font-size:20px">chevron_right</span>
</a>
```

---

---

### Modifiers: weight

The variants are Breakpoint, State, Weight, Size (Large, Medium, Small) and Color (Primary, Text Primary Inverted). Figma weights are 100 higher than the CSS (see `eco-typography`).

| Modifier | Class | CSS |
|---|---|---|
| Regular | (none) | `font-weight: 400` |
| Medium | `action-link--weight-medium` | `font-weight: 500` |
| Bold | `action-link--bold` | `font-weight: 600` |

Use one weight in a group of links. **An action link is never italic.**

**Style and color rule:** an action link matches the type size of the content it follows; one that stands apart from other content matches the default body copy size of the page (Figma link info). **Do not up-size for emphasis: use the strong (Bold) variant, at most once per stack**. A group uses one size and equal spacing on the 8px grid. Colors: Primary on light surfaces, Inverted on dark ones (no Secondary or Tertiary in Figma); the icons always have the same color as the link text. Hover: `text-action-secondary-hover` (Primary) and `text-action-primary-inverted-hover`.

---

### Usage and content rules

**Definition:** a self-contained text link paired with icons that clarify what happens on activation. Link weight (lighter than a Button), a clear anchor outside body copy: under product descriptions, in specification sections, in resource lists. One line: a standalone iconized text link for lightweight actions and forward or backward navigation, placed outside running text.

**Use when:** downloadable resources (datasheets, manuals, certificates); a "see more / view all" step at the end of a section or list; several parallel resources as stacked rows; more anchoring than an Inline Link but less weight than a Button; a contact action outside body copy with a matching leading icon (`mailto:`, `tel:`).

**Do not use when:** in a sentence (Inline Link); the primary call to action (Button; never an action link and a Button side by side for the same action); a grid of peers (Tile Link); the chevron would open or close content in place (Button, Collapsible, Modal: action links navigate or download, they do not disclose).

**States:** Enabled has no underline (placement and icons are the affordance; the reverse of the Inline Link). Hover is a color shift, and the underline appears under the label (icons never underlined). **No disabled state**: hide the row or show plain text; if one must ship it needs `aria-disabled`, is exempt from the contrast minimum and must still be recognizable (no CSS for it).

**Best practices:** leading icon matches the outcome (download for files, chevron alone for navigation), no decorative icons; stacks are one column, one size, equal 8px-grid spacing; links can also sit on one row (Storyblok design) with a vertical Divider (Tertiary, `eco-divider`) between them, one size and equal space on both sides: without a divider they run together. **Layouts of a group (Storyblok):** `action-link-group--stacked` (also the default `action-link-group`) = one column, 8px between the links; `action-link-group--divided` = the links one after another on a row, wrapping where the row is full, with a vertical divider (`border-tertiary`, 1px, space-16 on each side) drawn by the group between two links on the same line: never at the start or the end of a line (the divider is a pseudo-element in the gap before each link, and the group has `overflow: hidden` with 4px padding and -4px margin so the focus ring is not cut off). The author chooses the layout on every breakpoint: a divided group does not turn into a column on mobile. The links must be direct children of the group (or wrapped one level, such as `li`); no `divider` element between them; the strong variant at most once per stack; the label states the object (no bare verbs when several links sit together); do not use the chevron as a disclosure icon.

**Content:** verb-first action phrases or destination nouns, two to five words; sentence case, no trailing punctuation; file type and size in the label ("Download manual (PDF, 2 MB)"), not in a tooltip; labels in a stack parallel; long labels: define truncation (ellipsis) or a two-line wrap at small widths.

**Accessibility:** `<a href>` (add `download` for same-origin files); a JS action with no navigation must be a `<button>`; accessible name is the visible label, extended per label-in-name (WCAG 2.5.3), both icons `aria-hidden`; file behavior announced in the name; 2px focus ring around the whole link (4.9:1 on white); label and icons at least 4.5:1 in default and hover; standalone target at least 24x24px (WCAG 2.5.8) and at least 8px between stacked links. **Hit area (2026-10-14):** `.action-link::after` is an invisible layer, at least 24px high (`min-height: 24px`, centered), so the clickable area of a Small link (20px) and a Medium link on mobile (22px) is 24px while the drawn size stays as in Figma; keep 8px between stacked links. **Open points (measured):** Inverted hover (`#ffffffc7`) on a mid-gray such as `#737373` is 2.8:1; Primary hover `#737373` is 4.7:1 on white but 4.4:1 on `#f6f6f6`.

