---
name: eco-table
description: Use when building a data table (rows and columns of text, check icons or small controls) — row and header heights, cell padding, lines, header background and the card shadow. A first version: more variants and states (sorting, selection, sticky header, empty state) are added later. Not for layout, and not for a single key/value list.
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, template rules, breakpoints, and the quality checklist that always applies on top of this spec.

## Table (ECO Design System) — first version

> **Status:** a start. The values below come from the documentation pages in `eco-design-system/` (set by the design owner), **not yet from a Figma component**. When a Figma table component exists, re-extract it (see `eco-add-component`) and replace or confirm these values. Add sorting, selection, sticky header, empty/loading state and a documentation page (`eco-design-system/components/table.html`) later.

A table shows rows of comparable data. It sits in a **wrap** that gives it the elevation of a dashboard card and scrolls sideways when the window is too narrow.

### Used when
- Comparing the same properties across several items (permissions per role, tokens per state, specs per size).
- The data has real rows and columns. For one list of label/value pairs, use a description list instead.

### Dimensions

| Part | Value | Token / note |
|---|---|---|
| Header row height | 56px | `height` on `th` (a minimum: taller if the text wraps) |
| Body row height | 48px | `height` on `td` / `th` (a minimum) |
| Cell padding | 11px top and bottom, 24px left and right | The 1px row line brings the vertical padding to 12px; keeps a one-line row at exactly 48px |
| Wrap | no border, `overflow-x: auto` | Mobile: the table keeps its width and the wrap scrolls |

### Surfaces and lines

| Part | Token |
|---|---|
| Wrap background | `var(--color-surface-raised-primary)` |
| Wrap shadow | `var(--shadow-elevation-b-20)` (same as the dashboard stat cards) |
| Header background | `var(--color-surface-02)` by default, see "Header background" |
| Line between header and first row | `var(--color-border-primary)`, 1px |
| Lines between body rows | `var(--color-border-secondary)`, 1px |
| Last row | no bottom line |

### Header background
Default is `surface-02`. These are also allowed when the table needs more emphasis or a brand/status tone:
- `var(--color-accent-light)` (Swedol accent). For Tools: `var(--color-primitive-color-brand-tools-accent-light)` (a primitive, not in `tokens.json`).
- A weak status surface: `var(--color-surface-information-weaker)`, `-success-weaker`, `-warning-weaker`, `-danger-weaker`. Use these only when the table itself carries that status.

Pick one per page and never mix tones in the same table. Header text stays `var(--color-text-primary)`.

### Typography
Header cells: bold. Body cells: `body-sm` (14px/20px, 0.36px) from `eco-typography`; the first column (row header) is bold. Same on all breakpoints.

### HTML structure
```html
<div class="table-wrap">
  <table class="table">
    <thead>
      <tr><th scope="col">Permission</th><th scope="col">Standard</th><th scope="col">Administrator</th></tr>
    </thead>
    <tbody>
      <tr><th scope="row">View orders</th><td>Yes</td><td>Yes</td></tr>
      <tr><th scope="row">Manage users</th><td>No</td><td>Yes</td></tr>
    </tbody>
  </table>
</div>
```
Use real `th` with `scope`. Check icons use `eco-checkbox` (`.check-icon`, disabled): give the cell a block checkbox with a 4px margin so the row stays 48px (`input { display: block; margin: 4px auto; }`).

### CSS template
```css
.table-wrap {
  overflow-x: auto;
  background: var(--color-surface-raised-primary);
  box-shadow: var(--shadow-elevation-b-20);
}
.table { width: 100%; border-collapse: collapse; font-size: 14px; line-height: 20px; letter-spacing: 0.36px; } /* body-sm */
.table th, .table td {
  text-align: left; vertical-align: middle;
  padding: 11px 24px; height: 48px;
  border-bottom: 1px solid var(--color-border-secondary);
}
.table thead th {
  height: 56px; font-weight: 600; white-space: nowrap;
  background: var(--color-surface-02);
  border-bottom-color: var(--color-border-primary);
}
.table tbody th { font-weight: 600; white-space: nowrap; }
.table tbody tr:last-child > * { border-bottom: 0; }
```
The same rules are `.ds-table-wrap` / `.ds-table` in `eco-design-system/docs.css`.

### Rules
1. **Never** hardcode colors, shadow or spacing: `var(--…)` from `eco-tokens`.
2. **Never** put the `tr:last-child` "no line" rule on the header row: scope it to `tbody` (a bare `tr:last-child` also hits a one-row `thead` and removes the header line).
3. **Always** use `th` with `scope`; use `<caption>` or a nearby heading to name the table.
4. Text columns left-aligned; the doc pages center check-icon and matrix columns (page-local).
5. Header background: one tone per page, from the list above only. Anything else: ask first.
6. Breakpoint test: the table does not change at `md`; at ~375px and ~700px check that the wrap scrolls and the page does not (`scrollWidth == innerWidth`).

### Flags
- Values are not from Figma yet (see Status).
- `11px` vertical padding is a consequence of the 1px line (48px row); revisit if the line moves to a different mechanism (for example `box-shadow` lines).
- Not tested yet: dark mode, a sticky header, very long cell text, and rows with a control other than a checkbox.
