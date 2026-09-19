---
name: eco-section
description: Use when building a new section/full-width block in a page layout, including My Pages page-title spacing (main-content/page-preamble) — padding per breakpoint, background (Surface Raised Primary/Secondary), page divider, and the zeroed-padding use case.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Section (ECO Design System)

A section is a modular, reusable full-width block that represents a distinct part of a page layout. It's used to divide content into clear sections with automatically adjusted padding values per breakpoint.

### Anatomy

1. **Section padding – Top**
2. **Section padding – Bottom**
3. **Surface** – background color: `Surface Raised Primary` (`var(--color-surface-raised-primary)`) or `Surface Raised Secondary` (`var(--color-surface-raised-secondary)`)
4. **Content container** – the content area inside the section

### Padding per breakpoint

Padding adjusts automatically depending on the current breakpoint.

#### First section

The first section on a page uses lower top padding.

| Breakpoint | Top (px) | Bottom (px) |
|---|---|---|
| `breakpoint-xs` | 16 | 40 |
| `breakpoint-sm` | 32 | 48 |
| `breakpoint-md` | 32 | 64 |
| `breakpoint-lg` | 40 | 80 |
| `breakpoint-xl` | 48 | 80 |

#### Other sections

These values apply to every section except the first.

| Breakpoint | Top (px) | Bottom (px) |
|---|---|---|
| `breakpoint-xs` | 32 | 40 |
| `breakpoint-sm` | 48 | 48 |
| `breakpoint-md` | 56 | 64 |
| `breakpoint-lg` | 72 | 80 |
| `breakpoint-xl` | 72 | 80 |

### CSS template

```css
/* Other sections */
.section {
  padding-top: 32px;    /* xs */
  padding-bottom: 40px; /* xs */
}

/* First section */
.section:first-of-type,
.section--first {
  padding-top: 16px;    /* xs */
  padding-bottom: 40px; /* xs */
}

@media (min-width: 640px) {  /* sm */
  .section { padding-top: 48px; padding-bottom: 48px; }
  .section--first { padding-top: 32px; padding-bottom: 48px; }
}

@media (min-width: 769px) {  /* md */
  .section { padding-top: 56px; padding-bottom: 64px; }
  .section--first { padding-top: 32px; padding-bottom: 64px; }
}

@media (min-width: 1024px) { /* lg */
  .section { padding-top: 72px; padding-bottom: 80px; }
  .section--first { padding-top: 48px; padding-bottom: 80px; }
}

@media (min-width: 1281px) { /* xl */
  .section { padding-top: 72px; padding-bottom: 80px; }
  .section--first { padding-top: 48px; padding-bottom: 80px; }
}
```

### Background color

The default color for sections is white (`surface-raised-primary`, `var(--color-surface-raised-primary)`). As a rule of thumb, a layout or page should either start with a white section, or use white as its only background color — this creates a stable structure and good consistency.

> Exceptions exist, e.g. the PLP page and My Pages.

By establishing `background-primary` as the UI's base color, a clean, sober feel is created, and it becomes clearer when a gray `surface-raised-secondary` section is used.

### Padding usage

The padding switch should normally always be on. The section's built-in padding creates the white space needed to divide content in a page layout.

It's possible to use sections **without** built-in padding and let the content itself act as the divider — use this with care and a clear purpose.

### Use cases – zeroed padding

5 cases where the section's padding is turned off:

1. **Divider inside a section** – Use a divider component inside a section with zero top & bottom padding in sections with the same background color, when you don't want to mark a clear separation but still want to give the content the section's padding values.

2. **Adjacent topic with an in-between section** – Use the section with zero bottom & top padding when the content of two sections covers the same topic, but you want to place a large semi-topic section between them for cross-sell or product placement.

3. **Fluid hero banner** – Use the section with zero top & bottom padding as a container for a fluid hero banner promoting new products or related campaigns.

4. **First section with an adjacent component that has built-in spacing** – Use the first section with zero top padding when the content starts with an image, heading, or text block next to a component with built-in spacing, e.g. a breadcrumb section.

5. **First section with a fluid banner as the first element** – Use the first section with zero top & bottom padding when the layout starts with a fluid banner or full-width image as the first component.

### Rules

1. **Mobile-first** – write xs padding with no prefix, then build up with `sm:` → `md:` → `lg:` → `xl:`.
2. **First section** – use the `.section--first` class (or `:first-of-type`) for reduced top padding.
3. **Surface** – always choose either `Surface Raised Primary` (`var(--color-surface-raised-primary)`) or `Surface Raised Secondary` (`var(--color-surface-raised-secondary)`) as the background. Never mix in other background colors without design approval.
4. **Horizontal padding** – the section's side margins follow the breakpoint margin defined in the grid system (`16px` xs, `32px` sm/md, `40px` lg+). Use `--px-full` or `px-[16px] sm:px-[32px] lg:px-[40px]`.
5. **Zeroed padding** – only turn off the built-in padding in the 5 defined use cases above. Never use zeroed padding without a clear purpose.

### Page Divider

A thin horizontal line that separates two `.section` blocks without marking a clear color change — used **between** two sections (not inside one, see use case 1 above), typically when both have the same background color and a full section boundary would feel too heavy. A standalone `<div>`, not a `<section>`.

```css
.page-divider { padding: 48px var(--px-full); }
.page-divider__line { height: 1px; background: var(--color-border-primary); }
```

```html
<div class="page-divider"><div class="page-divider__line"></div></div>
```

> `48px` top/bottom padding is the default when the divider replaces a section boundary outright (as in `mypages/users.html`, between `.fav-store-section` and `.contact-section`). If the divider is instead placed **between two `.section` blocks that already have their own top/bottom padding** (e.g. `.section.section--first` followed by the next `.section`), zero out `.page-divider`'s own padding (`padding: 0 var(--px-full);`) — otherwise two amounts of air stack on top of each other and you get needless extra whitespace.
>
> **Always use `--px-full`, never `--px-page`.** `--px-page` is just the margin value (16/32/40px) and lacks the `xl` breakpoint's centering against `max-w: 1200px` — a divider built on `--px-page` keeps extending to the screen edge on wide screens instead of stopping where the section content above/below it does. `--px-full` (`max(var(--px-page), calc((100vw - var(--max-w)) / 2))`) is the same token `.section` already uses, so the line respects the same margin and the same breakpoint boundary as the rest of the page.

---

## My Pages – Page Title section

Rules for spacing in the page-title section that must **always** be used on My Pages pages.

### main-content – top padding

| Breakpoint | padding-top |
|---|---|
| `breakpoint-xs` | 24px |
| `breakpoint-sm` | 24px |
| `breakpoint-md`+ | 40px |

### page-preamble – margin-bottom

| Breakpoint | margin-bottom |
|---|---|
| `breakpoint-xs` | 24px |
| `breakpoint-sm` | 32px |
| `breakpoint-md`+ | 40px |

### CSS template

```css
.main-content {
  padding-top: 24px; /* xs + sm */
}

.page-preamble {
  margin-bottom: 24px; /* xs */
}

@media (min-width: 640px) { /* sm */
  .page-preamble { margin-bottom: 32px; }
}

@media (min-width: 769px) { /* md+ */
  .main-content { padding-top: 40px; }
  .page-preamble { margin-bottom: 40px; }
}
```

---
