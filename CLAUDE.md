# Projekt – Designriktlinjer för Claude Code

## Teknikstack
- **HTML + Vanilla JS**
- **Tailwind CSS** för all styling

---

## Breakpoints (ECO Design System)

ECO Design System har **5 breakpoints** som täcker Mobile, Tablet och Desktop.

| Token | Enhet | Bredd | Kolumner | Gutter | Margin |
|---|---|---|---|---|---|
| `breakpoint-xs` | Mobile | 0–639px *(min 375px)* | 4 | 8px | 16px |
| `breakpoint-sm` | Tablet | 640–768px | 8 | 16px | 32px |
| `breakpoint-md` | Desktop Small | 769–1023px | 12 | 24px | 32px |
| `breakpoint-lg` | Desktop | 1024–1280px | 12 | 24px | 40px |
| `breakpoint-xl` | Desktop XL | 1281px+ | 12 | 24px | ∞ |

> Mobile (`xs`) och Tablet (`sm`) använder *Mobile Base Styling*.
> Desktop Small, Desktop och Desktop XL använder *Desktop Base Styling*.

### Tailwind-konfiguration
```js
module.exports = {
  theme: {
    screens: {
      sm:  '640px',   // Tablet
      md:  '769px',   // Desktop Small
      lg:  '1024px',  // Desktop
      xl:  '1281px',  // Desktop XL
    },
  },
}
```

### Approach: Mobile-first

Skriv **alltid** mobilstilen först (utan prefix), bygg sedan upp med `sm:`, `md:`, `lg:`, `xl:`.

```html
<!-- Margin per breakpoint -->
<section class="px-[16px] sm:px-[32px] lg:px-[40px]">...</section>

<!-- Grid-kolumner per breakpoint -->
<div class="grid grid-cols-4 sm:grid-cols-8 md:grid-cols-12 gap-[8px] sm:gap-[16px] md:gap-[24px]">...</div>

<!-- Synlighet -->
<nav class="hidden md:block">...</nav>
<button class="block md:hidden">☰</button>
```

### Regler

1. **Mobile-first** – mobilstil utan prefix, sedan `sm:` → `md:` → `lg:` → `xl:`.
2. **Inline i HTML** – all styling med Tailwind-klasser direkt i markup.
3. **Komponenter** – knappar, typografi m.m. byter storlek vid `md:` (Desktop Small). Se komponent-sektionerna nedan.

---

## Knapp-styling (ECO Design System)

### Varianter

| Variant | Bakgrund | Text | Border |
|---|---|---|---|
| **Primary** | `#000` | `#fff` | — |
| **Primary Inverted** | `#fff` | `#000` | — |
| **Secondary** | transparent | `#000` | `1px solid #000` |
| **Secondary Inverted** | transparent | `#fff` | `1px solid #fff` |
| **Blank** | transparent | `#000` | — |
| **Blank Inverted** | transparent | `#fff` | — |
| **Destructive** | `#d90000` | `#fff` | — |
| **Accent** | `#c7d300` | `#000` | — |
| **Disabled** (alla varianter) | `#e5e5e5` | `#939595` | — |
| **Disabled Blank** | transparent | `#939595` | — |

### Storlekar — Desktop (`min-width: 769px` / breakpoint `lg-md`)

| Storlek | Höjd | Padding (button) | Inre padding (text) | Font |
|---|---|---|---|---|
| **lg** | 56px | `16px` | `px-8px py-3px` | label-lg: 18px Bold, 0.18px spacing |
| **md** | 48px | `12px` | `px-8px py-3px` | label-lg: 18px Bold, 0.18px spacing |
| **sm** | 40px | `8px` | `px-8px py-4px` | label-md: 16px Bold, 0.48px spacing |
| **xs** | 32px | `6px` | `px-4px py-3px` | label-sm: 14px Bold, 0.56px spacing |

### Storlekar — Mobil (default / breakpoint `sm-xs`)

| Storlek | Höjd | Padding (button) | Font |
|---|---|---|---|
| **lg** | 48px | `12px` | label-lg: 16px Bold, 0.32px spacing |
| **md** | 40px | `8px` | label-lg: 16px Bold, 0.32px spacing |
| **sm** | 32px | `6px` | label-md: 14px Bold, 0.48px spacing |
| **xs** | 32px | `6px` | label-sm: 14px Bold, 0.56px spacing |

### Tillstånd (States)

| Tillstånd | Visuell regel |
|---|---|
| **Enabled** | Grundstil per variant ovan |
| **Hover** | `background-image: linear-gradient(90deg, rgba(255,255,255,0.2), rgba(255,255,255,0.2)), linear-gradient(90deg, [basefärg], [basefärg])` |
| **Focus** | Samma bakgrund som Enabled + absolut fokusring: `border: 2px solid #455efb; position: absolute; inset: -2px` |
| **Disabled** | Bg `#e5e5e5`, text `#939595`, `cursor: not-allowed` |

> Fokusringen (`#455efb`) placeras **utanför** knappen via `inset: -2px` på ett absolut child-element. Knappens `position` måste vara `relative`.

### Typografi (alla knappar)
- Font: `Breuer Condensed Bold`, sans-serif
- `text-transform: uppercase`
- `white-space: nowrap`
- `font-feature-settings: 'ss02' 1, 'ss03' 1` (för label-lg/md)

### CSS-mall (Primary)
```css
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  position: relative;
  border: none;
  cursor: pointer;
  font-family: 'Breuer Condensed', Arial, sans-serif;
  font-weight: 700;
  text-transform: uppercase;
  white-space: nowrap;
}

/* Storlekar – Desktop */
.btn--lg { height: 56px; padding: 16px; font-size: 18px; letter-spacing: 0.18px; }
.btn--md { height: 48px; padding: 12px; font-size: 18px; letter-spacing: 0.18px; }
.btn--sm { height: 40px; padding: 8px;  font-size: 16px; letter-spacing: 0.48px; }
.btn--xs { height: 32px; padding: 6px;  font-size: 14px; letter-spacing: 0.56px; }

/* Storlekar – Mobil (default, override med desktop: om behövs) */
/* lg-mobil = 48px, md-mobil = 40px, sm/xs-mobil = 32px */

/* Varianter */
.btn--primary           { background: #000; color: #fff; }
.btn--secondary         { background: transparent; color: #000; border: 1px solid #000; }
.btn--destructive       { background: #d90000; color: #fff; }
.btn--accent            { background: #c7d300; color: #000; }
.btn--blank             { background: transparent; color: #000; }

/* Hover */
.btn--primary:hover     { background-image: linear-gradient(90deg,rgba(255,255,255,.2),rgba(255,255,255,.2)), linear-gradient(90deg,#000,#000); }
.btn--destructive:hover { background-image: linear-gradient(90deg,rgba(255,255,255,.2),rgba(255,255,255,.2)), linear-gradient(90deg,#d90000,#d90000); }

/* Focus */
.btn:focus-visible::after {
  content: '';
  position: absolute;
  inset: -2px;
  border: 2px solid #455efb;
  pointer-events: none;
}

/* Disabled */
.btn:disabled, .btn--disabled { background: #e5e5e5; color: #939595; cursor: not-allowed; border: none; }
.btn--blank:disabled           { background: transparent; }
```

---

## Inputfält – Storlekar & Tillstånd (ECO Design System)

Inputfält används för att mata in fritext, nummer eller annan data. De kan kombineras med ikoner, ledtext och felmeddelanden.

> Alla inputfält delar: `font-family: 'Breuer Condensed', sans-serif`, `font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1` och `border-radius: 0` (raka hörn).

---

### Storlekar per breakpoint

#### Desktop (`md:`, 769px+)

| Storlek | Höjd | Padding | Ikon | Label | Input-text |
|---|---|---|---|---|---|
| **Large** | 48px | `12px` horiz, `8px` vert | 24px | `label-md`: 16px/16px, 0.48px, Bold, uppercase | `body-md`: 16px/24px, 0.32px, Regular |
| **Small** | 40px | `8px` alla sidor | 20px | `label-sm`: 14px/14px, 0.56px, Bold, uppercase | `body-sm`: 14px/20px, 0.28px, Regular |
| **XSmall** | 32px | `8px` alla sidor | 20px | `label-sm`: 14px/14px, 0.56px, Bold, uppercase | `body-sm`: 14px/20px, 0.28px, Regular |

#### Mobile / Tablet (`xs`/`sm`, 0–768px)

| Storlek | Höjd | Padding | Ikon | Label | Input-text |
|---|---|---|---|---|---|
| **Large** | 40px | `8px` alla sidor | 24px | `label-md` (mobil): 14px/14px, 0.42px, Bold, uppercase | `body-md` (mobil): 16px/22px, 0.32px, Regular |
| **Small** | 32px | `8px` alla sidor | 20px | `label-sm` (mobil): 12px/12px, 0.48px, Bold, uppercase | `body-sm`: 14px/20px, 0.28px, Regular |

> **Tumregel:** Desktop Large = 48px (standardformulär), Desktop Small = 40px (kompakta ytor), Mobile Large = 40px (standardformulär på mobil). Välj alltid den storlek som passar breakpointen.

**Hint/meddelande-text** (under inputfältet, alla storlekar):
- `body-sm`: 14px/20px, letter-spacing 0.28px, Regular
- Vänster-ikon: 20px (Material Symbols Outlined, wght 300)

---

### Tillstånd (States)

Alla tillstånd ska implementeras varje gång ett inputfält skapas. Tillstånden styr border, bakgrund, textfärg och hjälptexter.

#### 1. Enabled (standard)
| Egenskap | Värde |
|---|---|
| Border | `1px solid var(--color-border-input-default)` → `#939595` |
| Bakgrund | `var(--color-surface-raised-primary)` → `#ffffff` |
| Placeholder-text | `var(--color-text-tertiary)` → `#737373` |
| Hint/meddelande | `var(--color-text-tertiary)` → `#737373` |

#### 2. Hover
| Egenskap | Värde |
|---|---|
| Border | `1px solid var(--color-border-dark)` → `#333333` |
| Bakgrund | `var(--color-surface-raised-primary)` → `#ffffff` |
| Placeholder-text | `var(--color-text-tertiary)` → `#737373` |
| Hint/meddelande | `var(--color-text-tertiary)` → `#737373` |

#### 3. Active (ifyllt / focus med värde)
| Egenskap | Värde |
|---|---|
| Border | `1px solid var(--color-border-selected)` → `#000000` |
| Bakgrund | `var(--color-surface-raised-primary)` → `#ffffff` |
| Input-text | `var(--color-text-primary)` → `#000000` |
| Rensa-ikon | Visas (cancel-ikon fylld, 20px) + divider `1px, var(--color-border-tertiary)` |
| Hint/meddelande | `var(--color-text-tertiary)` → `#737373` |

#### 4. Focus (tangentbordsfokus, ingen ring på selekt)
| Egenskap | Värde |
|---|---|
| Border (inputruta) | `1px solid var(--color-border-input-default)` → `#939595` |
| Fokusring (utanför) | `2px solid var(--color-border-focus)` → `#455efb`, `inset: -3px` (offset utanför) |
| Bakgrund | `var(--color-surface-raised-primary)` → `#ffffff` |
| Placeholder-text | `var(--color-text-tertiary)` → `#737373` |

> Fokusringen placeras som ett absolut element `inset: -3px` utanför inputrutan – inte som `outline` på input-elementet självt.

#### 5. Error
| Egenskap | Värde |
|---|---|
| Border | `1px solid var(--color-border-danger-default)` → `#d90000` |
| Bakgrund | `var(--color-surface-raised-primary)` → `#ffffff` |
| Input-text | `var(--color-text-primary)` → `#000000` |
| Meddelande | `var(--color-text-danger-default)` → `#d90000` + felikon 20px (error) till vänster om texten |

#### 6. Success
| Egenskap | Värde |
|---|---|
| Border | `1px solid var(--color-border-success-default)` → `#248616` |
| Bakgrund | `var(--color-surface-raised-primary)` → `#ffffff` |
| Input-text | `var(--color-text-primary)` → `#000000` |
| Meddelande | `var(--color-text-success)` → `#248616` |

#### 7. Disabled
| Egenskap | Värde |
|---|---|
| Border | `1px solid var(--color-border-disabled)` → `#dad9d7` |
| Bakgrund | `var(--color-surface-raised-secondary)` → `#f6f6f6` |
| Placeholder-text | `var(--color-text-disabled)` → `#939595` |
| Meddelande | `var(--color-text-disabled)` → `#939595` |
| Cursor | `not-allowed` |

---

### Anatomi

```
[Label]                      ← label-md/sm, uppercase, text-primary
[Ikon] [Input-text...]  [✕|⊕] ← inputruta med valfri vänster-ikon + höger clear+divider+action
[Hint/felmeddelande]         ← body-sm, tertiary / danger / success
```

- **Label**: Alltid uppercase, font Bold. Placeras ovanför inputrutan med `gap: 4px`.
- **Vänster-ikon** (valfri): Material Symbols Outlined, wght 300, 24px (Large) / 20px (Small/XSmall).
- **Höger clear-ikon**: Visas enbart i `Active`-tillståndet. Ikonstorlek 20px (cancel filled). Separeras från övriga höger-ikoner av en 1px divider (`border-tertiary`, 16px hög).
- **Meddelande**: Alltid `body-sm` (14px), visas under inputrutan med `gap: 4px`.

---

### CSS-mall (Desktop Large – alla tillstånd)

```css
/* Wrapper */
.form-field {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

/* Label */
.form-label {
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 16px;          /* Desktop Large: label-md */
  font-weight: 700;
  line-height: 16px;
  letter-spacing: 0.48px;
  text-transform: uppercase;
  color: var(--color-text-primary);
  font-feature-settings: 'ss02' 1, 'ss03' 1;
}

/* Input wrapper (position: relative för fokusring) */
.input-wrap { position: relative; }

/* Fokusring (absolut, utanför) — animeras med opacity */
.input-wrap::after {
  content: '';
  position: absolute;
  inset: -3px;
  border: 2px solid var(--color-border-focus);
  pointer-events: none;
  opacity: 0;
  transition: opacity var(--duration-fast-2) var(--ease-standard);
}
/* Ring visas bara vid tangentbordsnavigering — body.keyboard-nav sätts via JS */
body.keyboard-nav .input-wrap:focus-within::after { opacity: 1; }

/* Input */
.form-input {
  height: 48px;                  /* Desktop Large */
  padding: 8px 12px;
  border: 1px solid var(--color-border-input-default);
  background: var(--color-surface-raised-primary);
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 16px;               /* body-md */
  font-weight: 400;
  line-height: 24px;
  letter-spacing: 0.32px;
  color: var(--color-text-primary);
  font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1;
  width: 100%;
  box-sizing: border-box;
  outline: none;
}

/* Placeholder */
.form-input::placeholder {
  color: var(--color-text-tertiary);
}

/* Hover */
.form-input:hover { border-color: var(--color-border-dark); }

/* Active (har värde — placeholder visas ej) */
.form-input:not(:placeholder-shown) { border-color: var(--color-border-selected); }

/* Focus — inner border stays border-input-default; only the blue ring (::after) appears */
.form-input:focus { border-color: var(--color-border-input-default); }

/* Error */
.form-input--error { border-color: var(--color-border-danger-default); }

/* Success */
.form-input--success { border-color: var(--color-border-success-default); }

/* Disabled */
.form-input:disabled {
  background: var(--color-surface-raised-secondary);
  border-color: var(--color-border-disabled);
  color: var(--color-text-disabled);
  cursor: not-allowed;
}

/* Hint/meddelande */
.form-helper {
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 14px;               /* body-sm */
  font-weight: 400;
  line-height: 20px;
  letter-spacing: 0.28px;
  color: var(--color-text-tertiary);
  font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1;
}
.form-helper--error   { color: var(--color-text-danger-default); display: flex; align-items: center; gap: 4px; }
.form-helper--success { color: var(--color-text-success); }
.form-helper--disabled{ color: var(--color-text-disabled); }

/* Mobile Small override (32px) */
@media (max-width: 768px) {
  .form-input--sm {
    height: 32px;
    font-size: 14px;
    line-height: 20px;
    letter-spacing: 0.28px;
  }
  .form-label--sm {
    font-size: 12px;
    line-height: 12px;
    letter-spacing: 0.48px;
  }
}
```

---

## Checkbox-styling (ECO Design System)

Checkboxar följer ECO Design Systems specifikation: total yta **24×24px**, synlig ruta **16×16px**.

### Storleksmodell
- Synlig ruta: `16px × 16px` (`appearance: none`, custom border)
- Marginal: `4px` på alla sidor → total yta 24×24px
- Fokusring: `outline: 2px`, `outline-offset: 2px` → fyller exakt marginalen (2px gap + 2px ring = 4px)

### Tillstånd

| Tillstånd | Visuell regel |
|---|---|
| Enabled | 1.5px solid `#000` border, vit bakgrund |
| Hover | border-width: 2px |
| Focus | Blå fokusring `#0052CC`, 2px, offset 2px |
| Selected | Svart fill `#000`, vit bockmarkering (SVG) |
| Indeterminate | Svart fill `#000`, vit streck (SVG) |
| Disabled | Border `#dad9d7`, vit bakgrund, `cursor: not-allowed` |
| Disabled Selected | Fill `#939595`, border `#939595` |
| Disabled label | Text `#939595` via `:has(input:disabled) span` |

### HTML-struktur
```html
<label class="form-checkbox-item">
  <input type="checkbox" />
  <span>Label</span>
</label>
```

### CSS-mall
```css
.form-checkbox-item { display: flex; align-items: center; gap: 8px; cursor: pointer; }
.form-checkbox-item input[type="checkbox"] {
  appearance: none; width: 16px; height: 16px;
  border: 1.5px solid #000; background: #fff;
  cursor: pointer; flex-shrink: 0; margin: 4px;
}
.form-checkbox-item input[type="checkbox"]:hover { border-width: 2px; }
.form-checkbox-item input[type="checkbox"]:focus-visible { outline: 2px solid #0052CC; outline-offset: 2px; }
.form-checkbox-item input[type="checkbox"]:checked { background-color: #000; border-color: #000; /* + SVG checkmark */ }
.form-checkbox-item input[type="checkbox"]:indeterminate { background-color: #000; border-color: #000; /* + SVG dash */ }
.form-checkbox-item input[type="checkbox"]:disabled { border-color: #dad9d7; cursor: not-allowed; }
.form-checkbox-item input[type="checkbox"]:disabled:checked { background-color: #939595; border-color: #939595; }
.form-checkbox-item:has(input:disabled) { cursor: not-allowed; }
.form-checkbox-item:has(input:disabled) span { color: #939595; }
```

---

## Typografi – Desktop Base Styling (ECO Design System)

Gäller för **Desktop Small (`md:`, 769px+) och Desktop (`lg:`, 1024px+)**.
Font: `Breuer Condensed`, sans-serif. `font-feature-settings: 'ss02' 1, 'ss03' 1` gäller alla stilar.

### Body

| Token | Namn | Size | Line-height | Letter-spacing | Weight | Paragraph-spacing |
|---|---|---|---|---|---|---|
| `body-sm` | Body Small | 14px | 20px | 0.28px | 400 | 12px |
| `body-md` | Body Medium | 16px | 24px | 0.32px | 400 | 16px |
| `body-lg` | Body Large | 20px | 28px | 0px | 400 | 20px |
| `body-xl` | Body XLarge | 24px | 32px | 0px | 400 | 24px |

> Body används för längre textpassager. `body-xl` lämpar sig för kortare introtexter.

### Alt-Label (alternativa etiketter, uppercase)

| Token | Namn | Size | Line-height | Letter-spacing | Weight |
|---|---|---|---|---|---|
| `alt-label-sm` | Alt-Label Small | 14px | 14px | 0.56px | 500 |
| `alt-label-md` | Alt-Label Medium | 16px | 16px | 0.64px | 500 |
| `alt-label-lg` | Alt-Label Large | 18px | 18px | 0.36px | 500 |

> Alt-Label: `text-transform: uppercase`. Används för etikettering av formulärfält och UI-komponenter.

### Label (fetstil-etiketter, uppercase)

| Token | Namn | Size | Line-height | Letter-spacing | Weight |
|---|---|---|---|---|---|
| `label-sm` | Label Small | 14px | 14px | 0.56px | 600 |
| `label-md` | Label Medium | 16px | 16px | 0.48px | 600 |
| `label-lg` | Label Large | 18px | 18px | 0.18px | 600 |

> Label: `text-transform: uppercase`. Fetare version av Alt-Label. Används i knappar, formulär och UI-komponenter.

### Title (rubriker, normal case)

| Token | Namn | Size | Line-height | Letter-spacing | Weight |
|---|---|---|---|---|---|
| `title-sm` | Title Small | 16px | 18px | 0px | 600 |
| `title-md` | Title Medium | 20px | 24px | 0px | 600 |
| `title-lg` | Title Large | 24px | 28px | 0px | 600 |

> Title: kortare, medelstark text. Används för sekundära rubriker och H-taggar av mindre storlek.

### Headline (primära rubriker, normal case)

| Token | Namn | Size | Line-height | Letter-spacing | Weight |
|---|---|---|---|---|---|
| `headline-sm` | Headline Small | 28px | 32px | 0px | 600 |
| `headline-md` | Headline Medium | 32px | 36px | 0px | 600 |
| `headline-lg` | Headline Large | 36px | 40px | 0px | 600 |
| `headline-xl` | Headline XLarge | 46px | 52px | 0px | 600 |

> Headline: kort, högbetonad text. Primära textpassager och viktiga innehållsregioner. `headline-xl` lämpar sig för H1-innehåll (ej i kombination med `display-lg`).

### Display (kampanj/hero, uppercase)

| Token | Namn | Size | Line-height | Letter-spacing | Weight |
|---|---|---|---|---|---|
| `display-sm` | Display Small | 26px | 26px | 0px | 600 |
| `display-md` | Display Medium | 36px | 36px | 0px | 600 |
| `display-lg` | Display Large | 66px | 60px | 0px | 600 |

> Display: `text-transform: uppercase`. Reserverat för hero-banners, kampanjrubriker och numerärer. Använd sparsamt. `display-lg` = H1 på sida/artikel (aldrig tillsammans med `headline-xl`).

### Modified Styles (modifierade varianter)

| Token | Bas | Ändring | Användning |
|---|---|---|---|
| `label-lg--badge` | `label-sm` | 14px, 0.56px, 600, normal case | Badge-komponent |
| `label-sm--badge` | `label-sm` | 12px, 0.48px, 600, normal case | Liten badge |
| `label-lg--underline` | `label-lg` | + `text-decoration: underline` | Understruken etikett |

### CSS-regel (Desktop Base)

```css
/* Alla typografistilar delar: */
font-family: 'Breuer Condensed', Arial, sans-serif;
font-style: normal;
font-feature-settings: 'ss02' 1, 'ss03' 1;

/* Alt-Label och Label tillägger: */
text-transform: uppercase;

/* Display tillägger: */
text-transform: uppercase;
font-feature-settings: 'ss02' 1, 'ss03' 1; /* ej 'ss06' */
```

---

## Typografi – Mobile Base Styling (ECO Design System)

Gäller för **Mobile (`xs`, 0–639px) och Tablet (`sm`, 640–768px)**.
Font: `Breuer Condensed`, sans-serif. `font-feature-settings: 'ss02' 1, 'ss03' 1` gäller alla stilar.

### Body

| Token | Namn | Size | Line-height | Letter-spacing | Weight | Paragraph-spacing |
|---|---|---|---|---|---|---|
| `body-sm` | Body Small | 14px | 20px | 0.28px | 400 | 12px |
| `body-md` | Body Medium | 16px | 22px | 0.32px | 400 | 16px |
| `body-lg` | Body Large | 18px | 24px | 0px | 400 | 16px |
| `body-xl` | Body XLarge | 20px | 26px | 0px | 400 | — |

> Body används för längre textpassager. `body-xl` lämpar sig för kortare introtexter.

### Alt-Label (alternativa etiketter, uppercase)

| Token | Namn | Size | Line-height | Letter-spacing | Weight |
|---|---|---|---|---|---|
| `alt-label-sm` | Alt-Label Small | 12px | 12px | 0.48px | 500 |
| `alt-label-md` | Alt-Label Medium | 14px | 14px | 0.56px | 500 |
| `alt-label-lg` | Alt-Label Large | 16px | 16px | 0.32px | 500 |

> Alt-Label: `text-transform: uppercase`. Används för etikettering av formulärfält och UI-komponenter.

### Label (fetstil-etiketter, uppercase)

| Token | Namn | Size | Line-height | Letter-spacing | Weight |
|---|---|---|---|---|---|
| `label-sm` | Label Small | 12px | 12px | 0.48px | 600 |
| `label-md` | Label Medium | 14px | 14px | 0.42px | 600 |
| `label-lg` | Label Large | 16px | 16px | 0.32px | 600 |

> Label: `text-transform: uppercase`. Fetare version av Alt-Label. Används i knappar, formulär och UI-komponenter.

### Title (rubriker, normal case)

| Token | Namn | Size | Line-height | Letter-spacing | Weight |
|---|---|---|---|---|---|
| `title-sm` | Title Small | 16px | 18px | 0px | 600 |
| `title-md` | Title Medium | 18px | 22px | 0px | 600 |
| `title-lg` | Title Large | 20px | 24px | 0px | 600 |

> Title: kortare, medelstark text. Används för sekundära rubriker och H-taggar av mindre storlek.

### Headline (primära rubriker, normal case)

| Token | Namn | Size | Line-height | Letter-spacing | Weight |
|---|---|---|---|---|---|
| `headline-sm` | Headline Small | 22px | 24px | 0px | 600 |
| `headline-md` | Headline Medium | 26px | 28px | 0px | 600 |
| `headline-lg` | Headline Large | 28px | 32px | 0px | 600 |
| `headline-xl` | Headline XLarge | 30px | 36px | 0px | 600 |

> Headline: kort, högbetonad text. Primära textpassager och viktiga innehållsregioner. `headline-xl` lämpar sig för H1-innehåll (ej i kombination med `display-lg`).

### Display (kampanj/hero, uppercase)

| Token | Namn | Size | Line-height | Letter-spacing | Weight |
|---|---|---|---|---|---|
| `display-sm` | Display Small | 22px | 22px | 0px | 600 |
| `display-md` | Display Medium | 28px | 28px | 0px | 600 |
| `display-lg` | Display Large | 36px | 34px | 0px | 600 |

> Display: `text-transform: uppercase`. Reserverat för hero-banners, kampanjrubriker och numerärer. Använd sparsamt. `display-lg` = H1 på sida/artikel (aldrig tillsammans med `headline-xl`). OBS: `display-lg` har line-height (34px) som är lägre än font-size (36px) — avsiktligt för tät kampanjtext.

### CSS-regel (Mobile Base)

```css
/* Alla typografistilar delar: */
font-family: 'Breuer Condensed', Arial, sans-serif;
font-style: normal;
font-feature-settings: 'ss02' 1, 'ss03' 1;

/* Alt-Label och Label tillägger: */
text-transform: uppercase;

/* Display tillägger: */
text-transform: uppercase;
font-feature-settings: 'ss02' 1, 'ss03' 1; /* ej 'ss06' */
```

---

## Färger – Semantiska Tokens (ECO Design System)

Alla tokens har prefixet `color/` i Figma. I CSS används de som hex-värden eller CSS-variabler (`--color-[token]`).

### Accent

| Token | Hex | Beskrivning |
|---|---|---|
| `accent-default` | `#c7d300` | Primär accentfärg (limegul). Används i Accent-knappar. |
| `accent-light` | `#f4f6cc` | Ljus accentfärg. Bakgrund för accentmarkeringar. |
| `accent-dark` | `#8b9400` | Mörk accentfärg. Hover-tillstånd för accent. |

```html
<!-- Exempel: Accent-knapp -->
<button style="background:#c7d300; color:#000;">Köp nu</button>
```

### Text

| Token | Hex | Beskrivning |
|---|---|---|
| `text-primary` | `#000000` | Primär text. Rubriker och huvudinnehåll. |
| `text-primary-inverted` | `#ffffff` | Primär text på mörk/svart bakgrund. |
| `text-secondary` | `#4f4f4f` | Hög betoning på ljus bakgrund. Sekundärt innehåll – minskar kognitiv belastning bredvid text-primary. |
| `text-secondary-inverted` | `#ffffffc7` | Sekundär text på mörk bakgrund. |
| `text-tertiary` | `#737373` | Medium betoning och hinttexter på vit bakgrund. |
| `text-tertiary-inverted` | `#999999` | Tertiär text på mörk bakgrund. |
| `text-disabled` | `#939595` | Inaktiverad text. |
| `text-price-customer` | `#00838f` | Kundpris (inloggad). |
| `text-price-guest` | `#d90000` | Gästpris (ej inloggad). |
| `text-price-on-black` | `#eb0000` | Pris visad på svart bakgrund. |
| `text-action-primary` | `#000000` | Primär länk/klickbar text. |
| `text-action-primary-hover` | `#737373` | Hover för primär länk. |
| `text-action-secondary` | `#4f4f4f` | Sekundär länkfärg. Används tillsammans med text-secondary. |
| `text-action-secondary-hover` | `#737373` | Hover för sekundär länk. |
| `text-action-tertiary` | `#737373` | Tertiär länkfärg. Används tillsammans med text-tertiary. |
| `text-action-tertiary-hover` | `#939595` | Hover för tertiär länk. |
| `text-action-accent` | `#000000` | Text på accentfärgad yta. |
| `text-success` | `#248616` | Statustext – lyckat resultat. |
| `text-danger-default` | `#d90000` | Statustext – fel/fara. |
| `text-information-default` | `#0066ff` | Statustext – information. |

```html
<!-- Exempel: Textfärger -->
<p style="color:#000000;">Primär text</p>
<p style="color:#4f4f4f;">Sekundär text</p>
<span style="color:#d90000;">Felmeddelande</span>
<a href="#" style="color:#000000;">Länk</a>
```

### Ikon

| Token | Hex | Beskrivning |
|---|---|---|
| `icon-primary` | `#000000` | Primär ikonfärg. Standard för ikoner på ljus bakgrund. |
| `icon-inverted` | `#ffffff` | Ikon på mörk bakgrund. |

### Bakgrund

| Token | Hex | Beskrivning |
|---|---|---|
| `background-primary` | `#ffffff` | Primär sidbakgrund. |
| `background-secondary` | `#f6f6f6` | Sekundär bakgrund. Paneler, kort, sidofält. |

### Surface – Neutrala nivåer

Används för att bygga upp kontrast i gråskalan. Siffran anger ungefärlig opacitet/mörkhet (02 = ljusast, 100 = svart).

| Token | Hex | Beskrivning |
|---|---|---|
| `surface-02` | `#fafafa` | Mycket ljus yta. Navigations-hover. |
| `surface-05` | `#f6f6f6` | Lätt grå yta. |
| `surface-10` | `#e5e5e5` | Disabled-bakgrund, borders. |
| `surface-15` | `#dad9d7` | Mjuk separator. |
| `surface-20` | `#cccccc` | Svagare border-selected. |
| `surface-40` | `#939595` | Inaktiverad text/ikon. |
| `surface-50` | `#737373` | Mediumgrå yta. |
| `surface-60` | `#595959` | Mörk yta. |
| `surface-80` | `#333333` | Mörkare yta. |
| `surface-90` | `#222222` | Nästan svart yta. |
| `surface-100` | `#000000` | Svart yta. |
| `surface-raised-primary` | `#ffffff` | Upphöjd yta, primär (kort, modaler). |
| `surface-raised-secondary` | `#f6f6f6` | Upphöjd yta, sekundär. |
| `surface-disabled` | `#e5e5e5` | Bakgrund för inaktiverade element. |
| `surface-navigation-hover` | `#fafafa` | Navigations-hover bakgrund. |

### Surface – Semantiska statusfärger

| Token | Hex | Beskrivning |
|---|---|---|
| `surface-information-default` | `#0066ff` | Informationsyta, stark. |
| `surface-information-weak` | `#d0e9ff` | Informationsyta, svag. |
| `surface-information-weaker` | `#e2f1ff` | Informationsyta, mycket svag. Bakgrund för info-meddelanden. |
| `surface-success-default` | `#248616` | Framgångsyta, stark. |
| `surface-success-weak` | `#daf6d0` | Framgångsyta, svag. |
| `surface-success-weaker` | `#edffe7` | Framgångsyta, mycket svag. |
| `surface-warning-default` | `#fac000` | Varningsyta, stark. |
| `surface-warning-weak` | `#ffe167` | Varningsyta, svag. |
| `surface-warning-weaker` | `#fff5c2` | Varningsyta, mycket svag. |
| `surface-danger-default` | `#d90000` | Farlighetyta, stark. |
| `surface-danger-weak` | `#ffbdc0` | Farlighetyta, svag. |
| `surface-danger-weaker` | `#ffebeb` | Farlighetyta, mycket svag. Bakgrund för felmeddelanden. |

```html
<!-- Exempel: Statusmeddelanden -->
<div style="background:#edffe7; color:#248616;">Beställningen är bekräftad</div>
<div style="background:#ffebeb; color:#d90000;">Något gick fel</div>
<div style="background:#e2f1ff; color:#0066ff;">Hämtar information...</div>
<div style="background:#fff5c2; color:#000;">Lågt lagersaldo</div>
```

### Surface – Opacitetsnivåer

| Token | Hex | Beskrivning |
|---|---|---|
| `surface-opacity-black-05` | `#0000000d` | Svart 5% opacitet. |
| `surface-opacity-black-10` | `#0000001a` | Svart 10% opacitet. Subtil overlay. |
| `surface-opacity-black-20` | `#00000033` | Svart 20% opacitet. |
| `surface-opacity-black-50` | `#00000080` | Svart 50% opacitet. Modalbakgrund. |
| `surface-opacity-white-0` | `#ffffff00` | Vit, helt transparent. |
| `surface-opacity-white-20` | `#ffffff33` | Vit 20% opacitet. Subtil ljusning på mörk bakgrund. |

### Border

| Token | Hex | Beskrivning |
|---|---|---|
| `border-primary` | `#e5e5e5` | Standard border. Kortseparatorer. |
| `border-secondary` | `#f6f6f6` | Ljus border. Subtila separatorer. |
| `border-tertiary` | `#dad9d7` | Mjuk border. Disabled-element. |
| `border-dark` | `#333333` | Mörk border. Hover-tillstånd. |
| `border-selected` | `#000000` | Vald/aktiv border. |
| `border-selected-hover` | `#737373` | Hover för vald border. |
| `border-selected-weaker` | `#cccccc` | Svagare vald border. |
| `border-hover` | `#333333` | Hover-border. |
| `border-disabled` | `#dad9d7` | Inaktiverad border. |
| `border-input-default` | `#939595` | Inputfält, standard. |
| `border-input_control-default` | `#737373` | Inputkontroller (checkbox, radio), standard. |
| `border-action-1` | `#000000` | Aktionsknapp border, primär. |
| `border-action-2` | `#ffffff` | Aktionsknapp border, inverterad. |
| `border-action-3` | `#0000001a` | Aktionsknapp border, subtil (10% svart). |
| `border-focus` | `#455efb` | Fokusring (blå). Används med `inset: -2px`. |
| `border-information-default` | `#0066ff` | Informationsborder, stark. |
| `border-information-weak` | `#d0e9ff` | Informationsborder, svag. |
| `border-success-default` | `#248616` | Framgångsborder, stark. |
| `border-success-weak` | `#daf6d0` | Framgångsborder, svag. |
| `border-warning-default` | `#fac000` | Varningsborder, stark. |
| `border-warning-weak` | `#ffe167` | Varningsborder, svag. |
| `border-danger-default` | `#d90000` | Farlighetborder, stark. |
| `border-danger-weak` | `#ffbdc0` | Farlighetborder, svag. |

```html
<!-- Exempel: Border-användning -->
<input style="border: 1px solid #939595;">
<input style="border: 2px solid #455efb;"> <!-- focus -->
<div style="border: 1px solid #d90000; background:#ffebeb;">Felmeddelande</div>
```

---

## Spacing (ECO Design System)

Spacing-tokens skapar ett förutsägbart och harmoniskt avståndssystem. Tokens appliceras på alla marginaler, padding och positionskoordinater – både horisontellt och vertikalt.

> Majoriteten av värdena är multipler av 8px. Värdena 1px, 2px och 4px används enbart för detaljnivå. 12px är ett komplement när det behövs.

### Spacing Scale

| Token | Värde | Användning |
|---|---|---|
| `space-0` | 0px | Nollställ avstånd |
| `space-1` | 1px | Detaljnivå – mycket fina justeringar |
| `space-2` | 2px | Detaljnivå – borders, fina justeringar |
| `space-4` | 4px | Detaljnivå – inre padding i täta komponenter |
| `space-8` | 8px | Bas-enhet. Inre padding, gap i täta layouter |
| `space-12` | 12px | Komplement. Paragraph-spacing, täta listor |
| `space-16` | 16px | Standard padding. Mobil sidmarginal |
| `space-24` | 24px | Medium spacing. Gutter på desktop |
| `space-32` | 32px | Tablet/desktop-marginal. Sektionsavstånd |
| `space-40` | 40px | Desktop sidmarginal (lg). Sektionsavstånd |
| `space-48` | 48px | Stora sektionsavstånd |
| `space-56` | 56px | Komponenthöjd lg-knapp på desktop |
| `space-64` | 64px | Stora layoutavstånd |
| `space-72` | 72px | Stora layoutavstånd |
| `space-80` | 80px | Hero-sektioner, stora vertikala avstånd |
| `space-112` | 112px | Extra stora layoutavstånd |
| `space-120` | 120px | Grid margin på desktop |

### Hur tokens används

Spacing appliceras genom att kombinera ett **token** (storlek) med en **konsumentklass** (var avståndet ska appliceras).

#### Konsumentklasser

**Margin**
| Klass | CSS-property |
|---|---|
| `mt-space` | `margin-top` |
| `mr-space` | `margin-right` |
| `mb-space` | `margin-bottom` |
| `ml-space` | `margin-left` |
| `mx-space` | `margin-left` + `margin-right` |
| `my-space` | `margin-top` + `margin-bottom` |

**Padding**
| Klass | CSS-property |
|---|---|
| `pt-space` | `padding-top` |
| `pr-space` | `padding-right` |
| `pb-space` | `padding-bottom` |
| `pl-space` | `padding-left` |
| `px-space` | `padding-left` + `padding-right` |
| `py-space` | `padding-top` + `padding-bottom` |

**Gap (layoutavstånd)**
| Klass | CSS-property |
|---|---|
| `gap-space` | `gap` (rad + kolumn) |
| `gap-x-space` | `column-gap` |
| `gap-y-space` | `row-gap` |

### Exempel

```css
/* Padding: space-16 */
.card { padding: 16px; }

/* Margin: space-24 vertikalt, space-8 horisontellt */
.item { margin: 24px 8px; }

/* Gap i grid: space-24 */
.grid { display: grid; gap: 24px; }
```

```html
<!-- Typiska kombinationer per breakpoint -->
<!-- xs: space-16 sidmarginal, space-8 gap -->
<section style="padding: 0 16px;">
  <div style="display:grid; gap:8px;">...</div>
</section>

<!-- sm/md: space-32 sidmarginal, space-16 gap -->
<section style="padding: 0 32px;">
  <div style="display:grid; gap:16px;">...</div>
</section>

<!-- lg: space-40 sidmarginal, space-24 gap -->
<section style="padding: 0 40px;">
  <div style="display:grid; gap:24px;">...</div>
</section>
```

---

## Elevation & Shadows (ECO Design System)

Shadows uttrycker graden av elevation mellan ytor – ju större och mjukare skugga, desto högre elevation.

### Grundbegrepp

| Begrepp | Definition |
|---|---|
| **Elevation** | Avståndet mellan två element längs z-axeln. |
| **Surface** | Den lägst synliga behållaren som komponenter, text m.m. placeras på. Motsvara `background-primary` (`#ffffff`). |
| **Background** | Applikationens bakgrundsfärg – den yta som allt vilar på under surface-nivån. |

### Välja rätt elevation

- **Öka elevation för prioriterade actions.** Användare uppmärksammar element som verkar ligga närmre – lyft det du vill att de ska fokusera på.
- **Liten och skarp skugga** = ytan ligger nära bakgrunden (låg elevation).
- **Stor och mjuk skugga** = ytan ligger långt från bakgrunden (hög elevation).
- **Efterlikna verkliga ljusförhållanden** – välj den elevationsnivå som känns naturlig för komponentens funktion.
- **Använd sparsamt.** Överdriven elevation distraherar och försämrar användarupplevelsen.

ECO Design System har **4 kategorier** av elevation:

| Kategori | Prefix | Beskrivning |
|---|---|---|
| Shadow Bottom | `elevation-b-*` | Ljuskälla uppifrån. Vanligast förekommande. |
| Shadow Top | `elevation-t-*` | Ljuskälla nedifrån. Används sparsamt. |
| Designated Level | `elevation-drawer-*` | Globala komponenter på separat lager (navigation, drawers). |
| Component Specific | `elevation-*` | Exklusivt för specifika komponenter. |

---

### Shadow Bottom (`elevation-b-*`)

Simulerar ljuskälla uppifrån. Skuggan faller nedåt. **Vanligast förekommande** i hela UI:t.

Varje nivå består av två lager: en mjuk huvudskugga + en skarp konturskugga (`0px 0px 1px 0px rgba(0,0,0,0.05)`).

| Token | CSS `box-shadow` | Nivå | Används för |
|---|---|---|---|
| `elevation-b-20` | `0px 1px 3px 0px rgba(0,0,0,0.10), 0px 0px 1px 0px rgba(0,0,0,0.05)` | 20% | Variant Tables (PDP/PLP), Data tables |
| `elevation-b-40` | `0px 2px 4px 0px rgba(0,0,0,0.10), 0px 0px 1px 0px rgba(0,0,0,0.05)` | 40% | Tooltip |
| `elevation-b-60` | `0px 4px 8px 0px rgba(0,0,0,0.10), 0px 0px 1px 0px rgba(0,0,0,0.05)` | 60% | Overflow menu, Notification |
| `elevation-b-80` | `0px 8px 16px 0px rgba(0,0,0,0.10), 0px 0px 1px 0px rgba(0,0,0,0.05)` | 80% | Site header, Menu, Dropdowns, Exposed Dropdowns |
| `elevation-b-100` | `0px 16px 24px 0px rgba(0,0,0,0.10), 0px 0px 1px 0px rgba(0,0,0,0.05)` | 100% | Modaler |

```css
/* Exempel: Kort med elevation-b-20 */
.card {
  box-shadow: 0px 1px 3px 0px rgba(0,0,0,0.10),
              0px 0px 1px 0px rgba(0,0,0,0.05);
}

/* Exempel: Modal med elevation-b-100 */
.modal {
  box-shadow: 0px 16px 24px 0px rgba(0,0,0,0.10),
              0px 0px 1px 0px rgba(0,0,0,0.05);
}
```

---

### Shadow Top (`elevation-t-*`)

Simulerar ljuskälla nedifrån. Skuggan faller uppåt. **Används sparsamt.**

| Token | CSS `box-shadow` | Nivå |
|---|---|---|
| `elevation-t-20` | `0px -1px 3px 0px rgba(0,0,0,0.10), 0px 0px 1px 0px rgba(0,0,0,0.05)` | 20% |
| `elevation-t-40` | `0px -2px 4px 0px rgba(0,0,0,0.10), 0px 0px 1px 0px rgba(0,0,0,0.05)` | 40% |
| `elevation-t-60` | `0px -4px 8px 0px rgba(0,0,0,0.10), 0px 0px 1px 0px rgba(0,0,0,0.05)` | 60% |
| `elevation-t-80` | `0px -8px 16px 0px rgba(0,0,0,0.10), 0px 0px 1px 0px rgba(0,0,0,0.05)` | 80% |
| `elevation-t-100` | `0px -16px 24px 0px rgba(0,0,0,0.10), 0px 0px 1px 0px rgba(0,0,0,0.05)` | 100% |

---

### Designated Level – Drawers & Navigation

Avsett för essentiella globala komponenter (navigationsmeny, drawers) som måste ligga på ett separat lager och sällan hindras av andra element.

| Token | CSS `box-shadow` | Beskrivning |
|---|---|---|
| `elevation-drawer-left` | `25px 0px 25px 0px rgba(0,0,0,0.03)` | Drawer från vänster – skugga på höger sida |
| `elevation-drawer-right` | `-25px 0px 25px 0px rgba(0,0,0,0.03)` | Drawer från höger – skugga på vänster sida |
| `elevation-drawer-left-menu-sublevel` | `4px 0px 10px 0px rgba(0,0,0,0.05)` | Inline drawer, sub-menynivåer (nivå 2+) |

```css
/* Drawer från vänster */
.drawer-left {
  box-shadow: 25px 0px 25px 0px rgba(0,0,0,0.03);
}

/* Drawer från höger */
.drawer-right {
  box-shadow: -25px 0px 25px 0px rgba(0,0,0,0.03);
}
```

---

### Component Specific

Skuggor som enbart används för specifika komponenter. Specificeras i detalj inom respektive komponentbeskrivning.

| Token | CSS `box-shadow` | Används för |
|---|---|---|
| `elevation-input_control-switch` | `0px 4px 8px 0px rgba(48,49,51,0.10), 0px 1px 1px 0px rgba(48,49,51,0.24), 0px -1px 1px 0px rgba(0,0,0,0.03)` | Toggle switch – indikerar upphöjd nivå |
| `elevation-table-overflow-right` | `-5px 0px 10px 0px rgba(0,0,0,0.05), -1px 0px 5px 0px rgba(0,0,0,0.10)` | Tabell-overflow höger – skugga inuti tabell där innehåll överskrider bredden |
| `elevation-table-overflow-left` | `5px 0px 10px 0px rgba(0,0,0,0.05), 1px 0px 5px 0px rgba(0,0,0,0.10)` | Tabell-overflow vänster – skugga inuti tabell där innehåll överskrider bredden |

---

### Regler för elevation

1. **Välj alltid lägsta möjliga nivå** – använd `elevation-b-20` som default för kortliknande ytor.
2. **Öka elevation för prioriterade actions** – modaler och kritiska overlays ska alltid ligga på `elevation-b-100`.
3. **Blanda inte Bottom och Top** på samma komponent (undantag: `elevation-input_control-switch`).
4. **Drawers och navigation** ska alltid använda `elevation-drawer-*`, aldrig `elevation-b-*`.
5. **Component Specific tokens** används aldrig utanför sin avsedda komponent.
6. **Surface ≠ Background** – Surface (`background-primary: #ffffff`) är den synliga behållaren; Background är underliggande sidbakgrund. Elevation skiljer dessa åt visuellt.
7. **Liten/skarp skugga** signalerar nära yta (låg nivå). **Stor/mjuk skugga** signalerar hög elevation – välj därefter.

---

## Motion – Easing & Duration (ECO Design System)

Animationer förmedlar funktionalitet, intention och samband. Använd dessa tokens för att skapa sammanhängande och realistiska övergångar.

> Principerna gäller som riktlinjer. De kan variera på komponentnivå men ska alltid följas så nära som möjligt för att säkerställa konsekvens.

### Tre grundbegrepp

| Begrepp | Förklaring |
|---|---|
| **Timing** | Hur lång tid en action tar. Välj alltid med omsorg. |
| **Spacing** | Mellanrummet mellan frames i ett rörligt objekt. Varierad spacing ger mjuka övergångar. |
| **Ease** | Kombinationen av timing och spacing. Styr hur en rörelse flödar – objekt ska accelerera och decelerate mjukt. |

---

### Easing-tokens

Välj easing beroende på hur en transition rör sig i relation till skärmen:

- **Liten förändring, kort distans** → snabb fade
- **Medium förändring, medium distans** → medium fade
- **Stor förändring, lång distans** → långsam fade

| Token | Kurva | Typ | Beskrivning | Används för |
|---|---|---|---|---|
| `motion-ease-decelerate-generic` | `cubic-bezier(.16,.38,.58,1)` | Ease Out – Generic | Börjar snabbt, bromsar in gradvis. Mindre betonad variant. | onClick, enter selected states. Form elements, Tabs, Toggled buttons, Tooltip. |
| `motion-ease-decelerate-emphasized` | `cubic-bezier(.16,0,.16,1)` | Ease Out – Emphasized ★ | Tydligare inbromsning. Standardval för att föra in element från utanför skärmen. | Drawers (alla varianter), Main/Account menu, Product menu, Notifications. |
| `motion-ease-accelerate-generic` | `cubic-bezier(.36,.09,1,.58)` | Ease In – Generic | Börjar långsamt, ökar hastighet. Likt ett föremål som faller. | Ta bort element från skärmen (exit-animationer). |
| `motion-ease-standard` | `cubic-bezier(.35,0,.35,1)` | Ease InOut – Standard | Startar långsamt, ökar, bromsar in. Allround-easing. | Hover states (majoriteten). Button, Product Card, Text Link, Breadcrumb, Collapsible, Overflow menu, Form elements, Tab bar, Drawer Link. |

> ★ `motion-ease-decelerate-emphasized` är förstahandsvalet för enter-animationer. `motion-ease-decelerate-generic` används när en mindre betoning önskas.

```css
/* Exempel: Element glider in från utanför skärmen (drawer) */
.drawer {
  transition: transform 350ms cubic-bezier(.16,0,.16,1);
}

/* Exempel: Hover-tillstånd på knapp */
.btn {
  transition: background-color 200ms cubic-bezier(.35,0,.35,1);
}

/* Exempel: Element lämnar skärmen */
.toast-exit {
  transition: opacity 150ms cubic-bezier(.36,.09,1,.58);
}
```

---

### Duration-tokens

Duration delas in i tre grupper — **Fast**, **Medium** och **Slow** — med fyra steg vardera.

> Använd tokens i enlighet med distance- och fade-principerna nedan. Vid vertikala rörelser kan valfri duration inom rätt grupp användas.

#### Fast (50–200ms) – Små, snabba interaktioner

| Token | Värde | Används för |
|---|---|---|
| `motion-duration-fast-1` | 50ms | Mikro-interaktioner, omedelbar feedback |
| `motion-duration-fast-2` | 100ms | Snabba hover-övergångar, focus-indikatorer |
| `motion-duration-fast-3` | 150ms | Standard hover, snabba exit-animationer |
| `motion-duration-fast-4` | 200ms | Lätta enter-animationer, korta state-ändringar |

#### Medium (250–400ms) – Mediumstora interaktioner

| Token | Värde | Används för |
|---|---|---|
| `motion-duration-medium1` | 250ms | Dropdowns, tooltips, kortare slide-ins |
| `motion-duration-medium2` | 300ms | Standard för de flesta UI-övergångar |
| `motion-duration-medium3` | 350ms | Drawers, panels, medelstora ytor |
| `motion-duration-medium4` | 400ms | Komplexa komponent-övergångar |

#### Slow (450–600ms) – Stora, tyngre rörelser

| Token | Värde | Används för |
|---|---|---|
| `motion-duration-slow-1` | 450ms | Stora enter-animationer, sidövergångar |
| `motion-duration-slow-2` | 500ms | Hero-element, fullwidth-animationer |
| `motion-duration-slow-3` | 550ms | Empty states, loading-faser |
| `motion-duration-slow-4` | 600ms | Längsta tillåtna duration – sparsamt |

---

### Distances – distans styr duration

Rörelsens distans avgör vilken duration-grupp som ska användas.

| Distans | Viewport-andel | Duration-grupp | Beskrivning |
|---|---|---|---|
| **Short** | ≤ 25% av vyn | Fast | Täcker liten del av skärmen. Använd fast-tokens. |
| **Medium** | 26–50% av vyn | Medium | Halva skärmen. Använd medium-tokens. |
| **Long** | 51–100% av vyn | Slow | Hela eller större delen av skärmen. Använd slow-tokens. |

---

### Fades – opacitet och färgövergångar

Fades är en sofistikerad metod för att övergå mellan färger och/eller opacitetsnivåer.

| Typ | Duration-grupp | Beskrivning | Komponenter |
|---|---|---|---|
| **Fast fade** | Fast | Standardinteraktioner i liten skala. | Buttons, list items, form elements |
| **Medium fade** | Medium | Medelstora interaktioner. Element som lyfts från ytan. | Cards, elevated surfaces |
| **Slow fade** | Slow | Viktiga tillståndsskiften. | Empty states, loading phases |

---

### Kombinationsregel: distans + fade

| Scenario | Distans | Fade | Easing |
|---|---|---|---|
| Knapp-hover | Short | Fast fade | `motion-ease-standard` |
| Dropdown öppnas | Short–Medium | Fast–Medium fade | `motion-ease-decelerate-generic` |
| Drawer glider in | Medium–Long | Medium fade | `motion-ease-decelerate-emphasized` |
| Modal visas | Medium | Medium fade | `motion-ease-decelerate-emphasized` |
| Element försvinner | Valfri | Fast fade | `motion-ease-accelerate-generic` |
| Loading/empty state | — | Slow fade | `motion-ease-standard` |

```css
/* CSS custom properties för hela projektet */
:root {
  /* Easing */
  --ease-decelerate-generic:    cubic-bezier(.16,.38,.58,1);
  --ease-decelerate-emphasized: cubic-bezier(.16,0,.16,1);
  --ease-accelerate-generic:    cubic-bezier(.36,.09,1,.58);
  --ease-standard:              cubic-bezier(.35,0,.35,1);

  /* Duration */
  --duration-fast-1:   50ms;
  --duration-fast-2:   100ms;
  --duration-fast-3:   150ms;
  --duration-fast-4:   200ms;
  --duration-medium-1: 250ms;
  --duration-medium-2: 300ms;
  --duration-medium-3: 350ms;
  --duration-medium-4: 400ms;
  --duration-slow-1:   450ms;
  --duration-slow-2:   500ms;
  --duration-slow-3:   550ms;
  --duration-slow-4:   600ms;
}
```

---


