---
name: eco-range
description: Use when the user picks one value from an ordered series of steps (easing, duration, size, density, a number between a minimum and a maximum) by dragging a thumb along a track, with the current value shown and optional tick labels. Not for choosing between two or three named options (use eco-pill-segment-control or eco-radio), not for an on/off setting (use eco-switch) and not for typing a number (use eco-input).
---

> Part of the design system in swedol-ui-prototype. See `CLAUDE.md` for tech stack, breakpoints and the quality checklist that always applies on top of this spec.

## Range (ECO Design System)

**Figma:** none. Designed in the repo (first uses: the "Auto-hide time" slider in the `toast.html` and `toast-ecom.html` playgrounds, 2–10 s numeric with `data-unit=" s"`, no `data-recommended`; and the Motion section of `eco-design-system/components/banner.html` and `inline.html`, via `DK.motion`). See Flags.

A native `<input type="range">` with a label, the current value as text and optional tick labels. Stepped by default (`step="1"` over a list of named steps), but a numeric range works too.

### Use it

```html
<link rel="stylesheet" href="/components/css/range.css">
<script src="/components/js/range.js"></script>   <!-- from docs pages: ../../components/js/range.js -->

<div class="form-range" data-range
     data-labels="Fast 2 · 100 ms|Fast 3 · 150 ms|Fast 4 · 200 ms"
     data-ticks="100|150|200" data-recommended="1">
  <div class="form-range__head">
    <label class="form-range__label" for="dur">Duration</label>
    <output class="form-range__value" for="dur"></output>
  </div>
  <input class="form-range__input" id="dur" type="range" min="0" max="2" step="1" value="1">
  <div class="form-range__ticks"></div>
</div>
```

| Attribute on `[data-range]` | Meaning |
|---|---|
| `data-labels="A\|B\|C"` | Value text per step, shown right of the label and set as `aria-valuetext`. Without it the number is shown (plus `data-unit`). |
| `data-ticks="a\|b\|c"` | Tick labels under the track, one per step, placed by position. Defaults to `data-labels`. Omit the `.form-range__ticks` div for no ticks. |
| `data-recommended="1"` | Step index that is the recommended default. Its tick gets a `*`. Explain the `*` in the text near the control. |
| `data-unit="px"` | Suffix for numeric ranges without `data-labels`. |

- Hide a range with the `hidden` attribute on the `.form-range` block: `.form-range[hidden] { display: none }` in `range.css` makes it work (without it `display: flex` overrides `hidden`).
- The input fires the normal `input` event on the `<input>`. Listen to it to apply the value.
- Blocks added after load: `ECO_RANGE.init(container)`.
- The label is always visible and linked with `for`/`id`. Tick labels are `aria-hidden`; the value is read through `aria-valuetext`.

### States

| State | Look |
|---|---|
| Enabled | 2px track `border-primary`, 16px round thumb `surface-100` |
| Hover | 4px halo around the thumb, `surface-opacity-black-12` |
| Focus (keyboard) | 2px `border-focus` ring around the input, 2px offset (`:focus-visible`, not on mouse click) |
| Disabled | Track `border-disabled`, thumb and texts `text-disabled`, `cursor: not-allowed` |

Typography: label = label-sm (14/20, 600), value = body-sm (14/20), ticks 12/16 `text-tertiary`. The same on every breakpoint.

### Rules

1. **Always the native `<input type="range">`.** Never a `<div>` imitation. Keyboard (arrows, Home/End, PageUp/PageDown) and screen readers then work for free.
2. **Link `components/css/range.css` and `components/js/range.js`.** Never copy the rules. Change the shared file to change every range.
3. Tokens only (`var(--…)`). The track and thumb pseudo-elements are the only place where the browser prefixes (`-webkit-`, `-moz-`) are needed.
4. Keep the number of steps small enough for the tick labels to fit (about 4–12 in a 480px control). Use fewer labels via `data-ticks` if they collide.
5. Never use it for two or three options, or for on/off: use `eco-pill-segment-control`, `eco-radio` or `eco-switch`.
6. Test: drag, click on the track, arrow keys, Tab focus ring, disabled not focusable.

### Flags

- No Figma component. Sizes (24px hit area, 2px track, 16px thumb, 4px halo) were decided in code. Touch size on mobile (24px) is smaller than the usual 44px target; raise `.form-range__input` height at `xs`/`sm` if design wants it.
- No dark-mode variant.
