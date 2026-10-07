---
name: eco-icon-picker
description: Use when a field must hold a Material Symbols icon name (icon for a banner, notification, menu item, tile, category, button content in a prototype, back-office form or docs playground) — click/Tab into the field and a panel opens on top of it with instant search over all ~6,100 icons, Recent and Popular. Not for showing an icon (use the `material-symbols-outlined` span) and not for choosing between a few fixed options (use eco-select or eco-radio).
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, breakpoints and the quality checklist that always applies on top of this spec.

## Icon picker (ECO Design System)

**Figma:** none. The pattern was designed in the repo (first use: `eco-design-system/components/banner.html`). See Flags.

A text field with `data-icon-picker`. The value is the Material Symbols name (`local_shipping`). The picker is for choosing the name: it adds nothing to the markup of the page that shows the icon.

### Use it

```html
<label for="icon">Icon</label>
<input id="icon" type="text" data-icon-picker placeholder="Icon name">
<script src="/components/icon-picker/icon-picker.js"></script>   <!-- from docs pages: ../../components/icon-picker/icon-picker.js -->
```

- One script tag. `icon-picker.js` loads `icon-picker-data.js` (all names + search tags, sorted by popularity) from its own folder, starting 0.5 s after page load. Never add the data file by hand.
- The page needs the Material Symbols Outlined font (already in `template.html` and `mypages/mypages-template.html`).
- The input fires `input` when an icon is picked. Listen to `input` to re-render a preview or save the value.
- Style the input itself with `eco-input`. Inside an eco-input field (`.input-wrap > .input-box > input`) the picker uses the `.input-wrap` as its anchor, so the panel covers the whole field. Otherwise it wraps the bare `<input>` in `.ip-wrap` and makes it 100% wide.

### Behavior (same everywhere)

| Moment | What happens |
|---|---|
| Click or Tab into the field | A panel opens **on top of the field** (`top:0`, same width, 12px padding). Search box first, focused. |
| Search box empty | **Recent** (last 8 picks, `localStorage`, shared by all pages) and **Popular** (top 60). |
| Typing | Instant search over all icons. Ranked: name starts with > a name word starts with > a tag word starts with; each group by popularity. Max 60 shown, header says `Results (n)`. No match: "No icons match …". |
| Click an icon | Name goes into the field, `input` event fires, panel closes, focus back on the field. |
| Esc / click outside | Closes without changing the value. |
| Focus ring on the search box | Hidden when opened with the mouse, shown when opened with Tab. |

Icons in the grid are shown Outlined, Fill 0, Weight 300, Grade 0, 24px, the same as icons in the components.

### Rules

1. **Always use this for a Material Symbols name field.** Never a plain text input, a hand-made list or a second picker.
2. **Never fork the look or behavior on one page.** Change `components/icon-picker/icon-picker.js` instead; every page gets it.
3. Colors, shadow and spacing in the picker are tokens only (`var(--…)`). Keep it that way when editing.
4. The picker stores a name, not a rendering. Validate or fall back where the icon is shown (empty = the component's default icon).
5. Needs the server to run from the repo root (`npx serve .`) for the root-absolute script path.

### Flags

- No Figma component. Dimensions (42px search, 40px icon cells, 176px grid height, 60 results) are decided in code. If design wants a Figma version, replace this section.
- `icon-picker-data.js` is a 1.4 MB copy of the Google Fonts Material Symbols metadata (August 2026 snapshot). Refresh by re-downloading `https://fonts.google.com/metadata/icons?key=material_symbols&incomplete=true` and rewriting the file as `window.ECO_ICONS=[[name,"tags"],...]` sorted by `popularity`.
- The 1.4 MB file is fine for a prototype. For production, serve a smaller list or search server-side.
