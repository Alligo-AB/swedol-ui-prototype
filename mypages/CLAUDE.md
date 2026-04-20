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

**Figma:** https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=2007-68126

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
| **System** | transparent | `#000` | `1px solid rgba(0,0,0,0.10)` = `border-action-3` |
| **System Selected** | `rgba(0,0,0,0.12)` | `#000` | `1px solid rgba(0,0,0,0.10)` = `border-action-3` |
| **Disabled** (alla varianter) | `#e5e5e5` | `#939595` | — |
| **Disabled Blank** | transparent | `#939595` | — |

> **System** används för knappar som agerar på systemnivå (t.ex. filter, sortering, verktygsval). Skiljer sig från Secondary genom den subtila semitransparenta bordern (`border-action-3`) istället för solid svart.
> **System Selected** är aktivt/valt läge av System — samma border men med `rgba(0,0,0,0.12)` bakgrund som markerar valt tillstånd.

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
| **Hover – Primary / Destructive / Accent** | `background-image: linear-gradient(90deg, rgba(255,255,255,0.2), rgba(255,255,255,0.2)), linear-gradient(90deg, [basefärg], [basefärg])` — white 20% overlay över solid bakgrundsfärg. |
| **Hover – Secondary** | `background: rgba(0,0,0,0.05)` — subtil mörk overlay på transparent bakgrund. |
| **Hover – Blank / ikonknappar på ljus bakgrund** | `background: rgba(0,0,0,0.05)` — samma som Secondary hover. Används på `Blank`-knappar och ikonknappar på vit/ljus bakgrund. |
| **Focus** | Fokusring visas **bara vid tangentbordsnavigering** (Tab). Samma mekanism som form-element: `body.keyboard-nav button:focus::after { opacity: 1 }`. Ring: `border: 2px solid #455efb`, `inset: -3px`, `border-radius: 0`, `opacity: 0` som default med transition. |
| **Disabled** | Bg `#e5e5e5`, text `#939595`, `cursor: not-allowed` |

> Fokusringen implementeras som en global `button::after`-regel med `opacity: 0` som default. `body.keyboard-nav` sätts via JS när användaren trycker Tab och tas bort vid `mousedown`/`touchstart`. Använd **aldrig** `:focus-visible` för knappar — använd alltid `body.keyboard-nav`-mönstret för konsekvent beteende med form-elementen.

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

/* Focus — outline-metoden, INTE ::after med inset.
   Orsak: ::after med inset positioneras från padding-kanten, inte border-kanten.
   Knappar med border (t.ex. Secondary 1px solid) tappar gapet (inset -3px - 1px border - 2px ring = 0px gap).
   outline mäter alltid från den yttre border-kanten → konsekvent 2px gap oavsett knappvariant. */
button { position: relative; outline: 2px solid transparent; outline-offset: 2px; transition: outline-color 100ms cubic-bezier(.35,0,.35,1); /* duration-fast-2, ease-standard */ }
body.keyboard-nav button:focus { outline-color: #455efb; /* border-focus */ }

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

## Select – Storlekar & Tillstånd (ECO Design System)

Select används för att låta användaren välja ett alternativ ur en lista. Komponentens storlek och tillstånd följer samma system som inputfält.

> Alla select-fält delar: `font-family: 'Breuer Condensed', sans-serif`, `font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1`, `border-radius: 0` (raka hörn), `appearance: none` (dold native pil), och en custom dropdown-pil (24px, Material Symbols `arrow_drop_down`).

---

### Storlekar per breakpoint

#### Desktop (`md:`, 769px+)

| Storlek | Höjd | Padding | Pil-ikon | Label | Select-text |
|---|---|---|---|---|---|
| **Large** | 48px | `8px` vert, `12px` horiz | 24px | `label-md`: 16px/16px, 0.48px, Bold, uppercase | `body-md`: 16px/24px, 0.32px, Regular |
| **Small** | 40px | `8px` alla sidor | 24px | `label-sm`: 14px/14px, 0.56px, Bold, uppercase | `body-sm`: 14px/20px, 0.28px, Regular |
| **XSmall** | 32px | `8px` alla sidor | 24px | `label-sm`: 14px/14px, 0.56px, Bold, uppercase | `body-sm`: 14px/20px, 0.28px, Regular |

#### Mobile / Tablet (`xs`/`sm`, 0–768px)

| Storlek | Höjd | Padding | Pil-ikon | Label | Select-text |
|---|---|---|---|---|---|
| **Large** | 40px | `8px` alla sidor | 24px | `label-md` (mobil): 14px/14px, 0.42px, Bold, uppercase | `body-md` (mobil): 16px/22px, 0.32px, Regular |
| **Small** | 32px | `8px` alla sidor | 24px | `label-sm` (mobil): 12px/12px, 0.48px, Bold, uppercase | `body-sm`: 14px/20px, 0.28px, Regular |

> Dropdown-pilen är placerad absolut: `right: 12px`, `top: 50%`, `transform: translateY(-50%)`. Höger padding på select måste vara minst `40px` för att ge utrymme åt pilen.

---

### Tillstånd (States)

Alla tillstånd ska implementeras varje gång ett select-fält skapas.

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

#### 3. Active (alternativ valt)
| Egenskap | Värde |
|---|---|
| Border | `1px solid var(--color-border-selected)` → `#000000` |
| Bakgrund | `var(--color-surface-raised-primary)` → `#ffffff` |
| Select-text | `var(--color-text-primary)` → `#000000` |

> **Active state för select** kan inte detekteras med `:not(:placeholder-shown)`. Använd JS för att lägga till klassen `.is-active` på `.form-select-wrap` när ett icke-default alternativ väljs: `select.addEventListener('change', e => wrap.classList.toggle('is-active', e.target.selectedIndex !== 0))`.

#### 4. Focus (tangentbordsfokus)
| Egenskap | Värde |
|---|---|
| Border (selectruta) | `1px solid var(--color-border-input-default)` → `#939595` |
| Fokusring (utanför) | `2px solid var(--color-border-focus)` → `#455efb`, `inset: -3px` |
| Bakgrund | `var(--color-surface-raised-primary)` → `#ffffff` |

> Fokusringen visas **enbart** vid tangentbordsnavigering (Tab). Implementeras via `body.keyboard-nav .input-wrap:focus-within::after { opacity: 1; }`. Klick öppnar dropdown utan ring.

#### 5. Error
| Egenskap | Värde |
|---|---|
| Border | `1px solid var(--color-border-danger-default)` → `#d90000` |
| Bakgrund | `var(--color-surface-raised-primary)` → `#ffffff` |
| Meddelande | `var(--color-text-danger-default)` → `#d90000` + felikon 20px (`error`, filled) till vänster |

#### 6. Success
| Egenskap | Värde |
|---|---|
| Border | `1px solid var(--color-border-success-default)` → `#248616` |
| Bakgrund | `var(--color-surface-raised-primary)` → `#ffffff` |
| Meddelande | `var(--color-text-success)` → `#248616` |

#### 7. Disabled
| Egenskap | Värde |
|---|---|
| Border | `1px solid var(--color-border-disabled)` → `#dad9d7` |
| Bakgrund | `var(--color-surface-raised-secondary)` → `#f6f6f6` |
| Select-text | `var(--color-text-disabled)` → `#939595` |
| Cursor | `not-allowed` |

---

### Hint/meddelande-text (alla storlekar)
- `body-sm`: 14px/20px, letter-spacing 0.28px, Regular
- `font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1`
- Vänster-ikon vid fel: 20px Material Symbols `error` (filled, wght 300)

---

### CSS-mall (Desktop Large – alla tillstånd)

```css
/* Wrapper — hanterar fokusring och pil-ikon */
.form-select-wrap {
  position: relative;
}

/* Fokusring (se input-sektion — samma mekanism) */
.input-wrap.form-select-wrap::after {
  content: '';
  position: absolute;
  inset: -3px;
  border: 2px solid var(--color-border-focus);
  pointer-events: none;
  opacity: 0;
  transition: opacity var(--duration-fast-2) var(--ease-standard);
}
body.keyboard-nav .input-wrap.form-select-wrap:focus-within::after { opacity: 1; }

/* Select */
.form-select {
  height: 48px;                   /* Desktop Large */
  padding: 8px 40px 8px 12px;     /* extra höger-padding för pil */
  border: 1px solid var(--color-border-input-default);
  background: var(--color-surface-raised-primary);
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 16px;                /* body-md */
  font-weight: 400;
  line-height: 24px;
  letter-spacing: 0.32px;
  color: var(--color-text-primary);
  font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1;
  appearance: none;
  cursor: pointer;
  width: 100%;
  box-sizing: border-box;
  outline: none;
  transition: border-color var(--duration-fast-3) var(--ease-standard);
}

/* Dropdown-pil */
.form-select-arrow {
  position: absolute;
  right: 12px;
  top: 50%;
  transform: translateY(-50%);
  pointer-events: none;
  width: 24px;
  height: 24px;
}

/* Hover */
.form-select:hover { border-color: var(--color-border-dark); }

/* Active (alternativ valt) — togglad via JS */
.form-select-wrap.is-active .form-select { border-color: var(--color-border-selected); }

/* Focus (cursor i fält) */
.form-select:focus { border-color: var(--color-border-selected); }

/* Error */
.form-select--error { border-color: var(--color-border-danger-default) !important; }

/* Success */
.form-select--success { border-color: var(--color-border-success-default) !important; }

/* Disabled */
.form-select:disabled {
  background: var(--color-surface-raised-secondary);
  border-color: var(--color-border-disabled);
  color: var(--color-text-disabled);
  cursor: not-allowed;
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
| `text-action-primary` | `#000000` | Primär länk/klickbar text (på ljus bakgrund). |
| `text-action-primary-hover` | `#737373` | Hover för primär länk (på ljus bakgrund). |
| `text-action-primary-inverted` | `#ffffff` | Primär länk på mörk bakgrund. |
| `text-action-primary-inverted-hover` | `rgba(255,255,255,0.78)` | Hover för primär länk på mörk bakgrund. |
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
8. **Drawer-overlay** – bakgrundsöverlagringen bakom en öppen drawer ska ha `background: rgba(0,0,0,0.2)`. Använd aldrig `surface-opacity-black-50` (50%) för drawers.
9. **Drawer-skugga** – en drawer som öppnas från höger ska alltid ha `box-shadow: var(--elevation-drawer-right)`. En drawer från vänster ska ha `box-shadow: var(--elevation-drawer-left)`. Skuggan appliceras direkt på drawer-panelen, inte på overlay.
10. **Drawer-bredd** – en standard drawer ska alltid ha `width: min(500px, 100%)`. Detta ger fast 500px bredd på större skärmar och fyller hela bredden automatiskt när fönstret/enheten är smalare än 500px. Använd aldrig separata media queries för att sätta `width: 100%` eller `width: 500px` på drawer-panelen.
11. **Drawer – responsiva komponentstorlekar** – vid `max-width: 768px` (xs + sm breakpoints) ska alla komponenter inuti drawern använda Mobile Base Styling. Applicera följande `@media (max-width: 768px)`-block på varje drawer:

```css
@media (max-width: 768px) {
  /* Header */
  .drawer-header { padding: 16px 24px; }
  .drawer-title {
    font-size: 22px;       /* display-sm Mobile */
    line-height: 22px;
  }

  /* Content & footer */
  .drawer-content { padding: 0 24px 24px; gap: 16px; }
  .drawer-footer { padding: 16px 24px; }

  /* Spara-knapp — mobile lg: padding 12px */
  .drawer-save-btn { padding: 12px 16px; }

  /* Labels — label-md Mobile: 14px/14px, 0.42px */
  .form-label {
    font-size: 14px;
    line-height: 14px;
    letter-spacing: 0.42px;
  }

  /* Inputs & selects — Large Mobile: 40px, 8px padding, body-md mobile 16px/22px */
  .form-input,
  .form-select {
    height: 40px;
    padding: 8px;
    line-height: 22px;
  }
  .form-select { padding-right: 40px; }   /* behåll utrymme för dropdown-pil */

  /* Checkbox-text — body-md Mobile: 16px/22px */
  .form-checkbox-item span {
    font-size: 16px;
    line-height: 22px;
    letter-spacing: 0.32px;
  }

  /* form-row staplas vertikalt på mobil */
  .form-row { flex-direction: column; gap: 16px; }
}
```

**Sammanfattning av Mobile Base Styling för drawer-komponenter:**

| Komponent | Desktop (`769px+`) | Mobile (`≤768px`) |
|---|---|---|
| Drawer-titel | `display-sm` 26px/26px | 22px/22px |
| Header-padding | `24px 32px` | `16px 24px` |
| Content-padding | `0 32px 32px`, gap 24px | `0 24px 24px`, gap 16px |
| Footer-padding | `24px 32px` | `16px 24px` |
| Label (`label-md`) | 16px/16px, 0.48px | 14px/14px, 0.42px |
| Input / Select | 48px, padding `8px 12px`, line-height 24px | 40px, padding `8px`, line-height 22px |
| Checkbox-text | `body-md` 16px/24px, 0.32px | 16px/22px, 0.32px |
| Spara-knapp | `padding: 16px` | `padding: 12px 16px` |
| form-row | `flex-direction: row` | `flex-direction: column`, gap 16px |

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

## Checkbox-styling (ECO Design System)

Figma-referens: `node-id=6408-8453`

Implementera alltid checkboxar med `<input type="checkbox">` + CSS — aldrig med `<img>` eller SVG-filer.

### States

| State | Bakgrund | Border | Bock |
|---|---|---|---|
| **Default (unchecked)** | `--color-background-primary` | `1.5px solid --color-border-selected` | — |
| **Checked** | `--color-surface-100` (svart) | `--color-border-selected` | Vit (`stroke="white"`) |
| **Hover (unchecked)** | — | `2px solid --color-border-selected` | — |
| **Hover (checked)** | `--color-text-disabled` (#939595) | `--color-text-disabled` (#939595) | Vit |
| **Disabled unchecked** | `--color-background-primary` | `--color-border-disabled` (#dad9d7) | — |
| **Disabled checked** | `--color-surface-disabled` (#e5e5e5) | ingen (matchar bakgrund) | Grå (`stroke="#939595"`) |
| **Indeterminate** | `--color-surface-100` (svart) | `--color-border-selected` | Vit horisontell linje |

> **OBS:** `disabled:checked` = ljusgrå bakgrund (#e5e5e5) + grå bock (#939595).  
> **Inte** mörk grå bakgrund + vit bock — det är hover-selected-stilen.

### Tabellens check-ikoner

I tabeller används samma `<input type="checkbox">` + CSS med klassen `.check-icon`:

```html
<!-- Aktiv behörighet -->
<td class="check-icon"><input type="checkbox" checked disabled /></td>

<!-- Ingen behörighet -->
<td class="check-icon"><input type="checkbox" disabled /></td>
```

---

## Section (ECO Design System)

En section är ett modulärt och återanvändbart fullbreddsblock som representerar en distinkt del av en sidlayout. Den används för att dela upp innehåll i tydliga sektioner med automatiskt justerade padding-värden per breakpoint.

### Anatomi

1. **Section padding – Top**
2. **Section padding – Bottom**
3. **Surface** – bakgrundsfärg: `Surface Raised Primary` (`#ffffff`) eller `Surface Raised Secondary` (`#f6f6f6`)
4. **Content container** – innehållsytan inuti sektionen

### Padding per breakpoint

Padding justeras automatiskt beroende på aktuell breakpoint.

#### Första sektionen (first section)

Den första sektionen på en sida använder lägre top-padding.

| Breakpoint | Top (px) | Bottom (px) |
|---|---|---|
| `breakpoint-xs` | 16 | 40 |
| `breakpoint-sm` | 32 | 48 |
| `breakpoint-md` | 32 | 64 |
| `breakpoint-lg` | 40 | 80 |
| `breakpoint-xl` | 48 | 80 |

#### Övriga sektioner

Dessa värden gäller alla sektioner utom den första.

| Breakpoint | Top (px) | Bottom (px) |
|---|---|---|
| `breakpoint-xs` | 32 | 40 |
| `breakpoint-sm` | 48 | 48 |
| `breakpoint-md` | 56 | 64 |
| `breakpoint-lg` | 72 | 80 |
| `breakpoint-xl` | 72 | 80 |

### CSS-mall

```css
/* Övriga sektioner */
.section {
  padding-top: 32px;    /* xs */
  padding-bottom: 40px; /* xs */
}

/* Första sektionen */
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

### Bakgrundsfärg

Standardfärgen för sektioner är vit (`surface-raised-primary`, `#ffffff`). En layout eller sida bör som tumregel börja med en vit sektion, eller ha vitt som enda bakgrundsfärg — detta skapar en stabil struktur och god konsekvens.

> Undantag finns, t.ex. PLP-sidan och My Pages.

Genom att etablera `background-primary` som basens färg i UI:t skapas en ren och sober känsla, och det blir tydligare när en grå `surface-raised-secondary`-sektion används.

### Paddinganvändning

Padding-switchen bör normalt alltid vara påslagen. Sektionens inbyggda padding skapar det vita utrymme som behövs för att dela upp innehåll i en sidlayout.

Det går att använda sektioner **utan** inbyggd padding och låta innehållet i sig fungera som avdelare — använd detta med försiktighet och med tydligt syfte.

### Use cases – nollad padding

5 fall där sektionens padding stängs av:

1. **Avdelare inuti sektion** – Använd en divider-komponent inuti en sektion med noll top & bottom-padding i sektioner med samma bakgrundsfärg, när du inte vill markera en tydlig separation men ändå ge innehållet sektionens padding-värden.

2. **Angränsande ämne med mellanliggande sektion** – Använd sektionen med noll bottom & top-padding när innehållet i två sektioner behandlar samma ämne, men du vill placera en stor semi-topic-sektion däremellan för cross-sell eller produktplacering.

3. **Fluid hero banner** – Använd sektionen med noll top & bottom-padding som behållare för en fluid hero banner som marknadsför nya produkter eller relaterade kampanjer.

4. **Första sektionen med angränsande komponent med inbyggd spacing** – Använd den första sektionen med noll top-padding när innehållet börjar med en bild, rubrik eller textblock intill en komponent med inbyggd spacing, t.ex. en brödsmulerad sektion (breadcrumb).

5. **Första sektionen med fluid banner som förstaelement** – Använd den första sektionen med noll top & bottom-padding när layouten börjar med en fluid banner eller fullbreddsbild som första komponent.

### Regler

1. **Mobile-first** – skriv xs-padding utan prefix, bygg sedan upp med `sm:` → `md:` → `lg:` → `xl:`.
2. **Första sektionen** – använd klassen `.section--first` (eller `:first-of-type`) för reducerad top-padding.
3. **Surface** – välj alltid antingen `Surface Raised Primary` (`#ffffff`) eller `Surface Raised Secondary` (`#f6f6f6`) som bakgrund. Blanda aldrig andra bakgrundsfärger utan designgodkännande.
4. **Horisontell padding** – sektionens sidmarginaler följer breakpoint-marginalen definierad i grid-systemet (`16px` xs, `32px` sm/md, `40px` lg+). Använd `--px-full` eller `px-[16px] sm:px-[32px] lg:px-[40px]`.
5. **Nollad padding** – stäng av inbyggd padding enbart i de 5 definierade use-casen ovan. Använd aldrig nollad padding utan tydligt syfte.

---

## My Pages – Page Title-sektion

Regler för spacing i page title-sektionen som **alltid** ska användas på My Pages-sidor.

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

### CSS-mall

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



## Notifikationer – Användningsriktlinjer (ECO Design System)

**Figma:** https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=6709-216647

---

### Vilken status ska användas?

| Status | Användning | Varaktighet | Färg |
|---|---|---|---|
| **E-Com** | Produkthantering: kundvagn, favoriter, urklipp | Ej obligatorisk — kan auto-stänga eller ligga kvar | Brand (svart/vit) |
| **Informational E-Com** | Kampanjinfo relevant för användaren | — | Info (`#0066ff`) |
| **Informational** | Tilläggsinfo, ej nödvändigtvis kopplad till aktiv uppgift | — | Info (`#0066ff`) |
| **Success** | Bekräftar att uppgift slutförts med förväntat resultat | Löser sig ofta automatiskt | Success (`#248616`) |
| **Warning** | Informerar om att aktuell åtgärd kanske inte är optimal | Kvarstår tills avfärdad eller uppgift genomförd | Warning (`#fac000`) |
| **Error** | Kritiskt fel, kan blockera framsteg tills löst eller avfärdad | Kvarstår tills löst eller avfärdad | Danger (`#d90000`) |

---

### Vilken komponenttyp ska användas?

| Typ | Användning | Varaktighet / Interaktion |
|---|---|---|
| **Inline Default** | Icke-störande feedback/status som är relevant för aktuell uppgift | Kvarstår tills löst |
| **Toast** | Kortlivade, tidsbaserade meddelanden — glider in/ut | Auto-stänger eller stängs av användaren |
| **Inline Actionable** | Interaktiva komponenter i inline- eller toast-stil | Kvarstår eller tas bort automatiskt |
| **Banner** | Globala/systemnotiser, full bredd, överst på sidan | Kan vara kampanjlång eller permanent |
| **Notification panel** | Systemgenererade meddelanden om kontot | Öppnas/stängs av användaren (drawer) |
| **Modal** | Hög störningsgrad — kräver omedelbar uppmärksamhet eller åtgärd | Blockerar UI tills avfärdad |

---

### Notifieringskategorier

ECO Design System skiljer på **task-generated** och **system-generated** notiser:

- **Task-generated**: utlöses av en direkt användaråtgärd (spara, skicka, ta bort). Visas i Toast eller Inline.
- **System-generated**: utlöses av systemhändelser utan direkt användarinteraktion (avisering om nytt meddelande, kontostatus). Visas i Notification panel eller Banner.

---

### Ikonanvändning

Reserverade ikoner per status — använd alltid rätt ikon och variant:

| Status | Material Symbol | Variant |
|---|---|---|
| **Informational** | `info` | Outlined / wght 300 / Filled |
| **Error** | `error` | Outlined / wght 300 / Filled |
| **Success** | `check_circle` | Outlined / wght 300 / Filled |
| **Warning** | `warning_amber` | Outlined / wght 300 / Filled |
| **E-Com Informational** | Valfri från galleri | Outlined / wght 300 |

> Ikonerna är reserverade per status och ska **inte** bytas ut mot andra ikoner för System-notifikationer. E-Com Informational är det enda undantaget.

---

### Avfärdning (Dismiss)

Alla notifikationer som kan stängas av användaren ska stödja minst ett av följande:

| Metod | Används i |
|---|---|
| **× (stäng-knapp)** | Toast, Inline, Banner, Modal |
| **Klick utanför** | Modal (klick på overlay stänger) |
| **ESC-tangent** | Modal |
| **Auto-dismiss** | Toast (Success, E-Com) |

> Modal ska **alltid** ha × i header, stödja ESC och stänga vid klick på overlay — dessa tre dismiss-mekanismer är obligatoriska.

---

### Mobil – höjd och position

- En toast på mobil ska använda `width: 375px` (eller `100%` om viewport är smalare).
- En inline-notifikation kan ha `height: auto` baserat på innehållet.
- En banner upptar alltid `width: 100%` och placeras överst på sidan.
- En modal på mobil kan ha `height: 100%` av skärmen eller anpassa sig efter innehållet och hålla sig fast längs nederkanten.

---

## Notifikation – System Toast (ECO Design System)

**Figma:** https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=13377-29321

### Används när
- Svar på en användaråtgärd (spara, skicka, radera)
- Systemhändelse som kräver användarens uppmärksamhet
- Kortlivat meddelande som inte blockerar gränssnittet

### Används INTE när
- Felmeddelande gäller ett enskilt formulärfält → använd `form-helper--error` istället
- Meddelandet är permanent → använd inline-notifikation eller banner
- Åtgärden kräver bekräftelse → använd Modal

---

### Varianter

#### Emphasis
| Emphasis | Bakgrund | Vänster border |
|---|---|---|
| **System Strong** | Statusfärgens svaga bakgrund (se tabell nedan) | `2px solid [statusfärg]` |
| **System Weak** | `#ffffff` (`surface-raised-primary`) | `2px solid [statusfärg]` |

#### Status + färger

| Status | Border / Ikon-färg | Strong-bakgrund | Material Symbol |
|---|---|---|---|
| **Informational** | `#0066ff` | `#e2f1ff` (`surface-information-weaker`) | `info` |
| **Error** | `#d90000` | `#ffebeb` (`surface-danger-weaker`) | `error` |
| **Success** | `#248616` | `#edffe7` (`surface-success-weaker`) | `check_circle` |
| **Warning** | `#fac000` | `#fff5c2` (`surface-warning-weaker`) | `warning_amber` |

#### Layout-varianter
| Variant | Innehåll |
|---|---|
| **Default** | Statusikon + [Titel (valfri) + Brödtext] + Stäng-knapp |
| **Actionable** | Som Default + en eller flera Blank-knappar under texten |

---

### Anatomi

```
[Statusikon 24px] [Titel (valfri) — title-sm]   [✕ stäng 20px]
                  [Brödtext — body-md           ]
                  [Blank-knapp (endast Actionable)]
```

- **Vänster border**: `2px solid [statusfärg]`, full höjd
- **Padding**: `16px` inuti, `8px` gap mellan ikon och textblock
- **Stäng-knapp**: Blank xs, `close`-ikon 20px, `padding: 2px`
- **Shadow**: `elevation-b-80` = `0px 0px 1px rgba(0,0,0,0.05), 0px 8px 16px rgba(0,0,0,0.10)`

---

### Typografi

| Element | Token | Värde |
|---|---|---|
| Titel (valfri) | `title-sm` | 16px/18px, Bold, 0px tracking, `text-primary` (#000) |
| Brödtext | `body-md` | 16px/24px, Regular, 0.32px tracking, `text-primary` (#000) |

---

### CSS-mall

```css
.toast {
  display: flex;
  flex-direction: column;
  width: 375px;
  box-shadow: 0px 8px 16px rgba(0,0,0,0.10), 0px 0px 1px rgba(0,0,0,0.05); /* elevation-b-80 */
}

.toast__inner {
  display: flex;
  align-items: flex-start;
  padding: 16px;
  gap: 8px;
  border-left: 2px solid var(--status-color);
  position: relative;
}

/* System Strong — färgad bakgrund */
.toast--strong.toast--info    { background: var(--color-surface-information-weaker); --status-color: var(--color-surface-information-default); }
.toast--strong.toast--error   { background: var(--color-surface-danger-weaker);      --status-color: var(--color-surface-danger-default); }
.toast--strong.toast--success { background: var(--color-surface-success-weaker);     --status-color: var(--color-surface-success-default); }
.toast--strong.toast--warning { background: var(--color-surface-warning-weaker);     --status-color: var(--color-surface-warning-default); }

/* System Weak — vit bakgrund */
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

Toasten är `position: fixed`. Glider alltid in från höger — utom på `xs` där den kommer uppifrån.

| Breakpoint | Top | Höger | Vänster | Bredd |
|---|---|---|---|---|
| `lg` (1024px+) | `40px` | `40px` | auto | `375px` |
| `md` (769–1023px) | `32px` | `32px` | auto | `375px` |
| `sm` (640–768px) | `32px` | `32px` | auto | `375px` |
| `xs` (0–639px) | `0px` | `0px` | `0px` | `100vw` (fyller hela viewport-bredden) |

> På `xs` animeras toasten in uppifrån istället för från höger. Bredden är alltid `375px` på sm och uppåt, och fyller hela viewport-bredden på xs.

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

| Egenskap | Värde |
|---|---|
| Riktning in | Från höger (`xs`: uppifrån) |
| Easing in | `cubic-bezier(0.16, 0, 0.16, 1)` (`ease-decelerate-emphasized`) |
| Riktning ut | Till höger (`xs`: uppåt) |
| Easing ut | `cubic-bezier(0.36, 0.09, 1, 0.58)` (`ease-accelerate-generic`) |
| Duration | `300ms` |
| Auto-hide | `4000ms` |

**Dismiss-triggers:** stäng-knapp, klick utanför toasten, auto-hide. Alla tre ska köra exit-animationen — anropa aldrig `remove()` direkt utan att animera ut.

> Starta click-outside-lyssnaren med `setTimeout(..., 0)` så att klicket som skapade toasten (t.ex. bekräfta-knapp i modal) inte stänger den omedelbart.

```css
/* Enter — från höger (lg/md/sm), ingen fade */
@keyframes toast-slide-in {
  from { transform: translateX(calc(100% + 40px)); }
  to   { transform: translateX(0); }
}
/* Exit — till höger (lg/md/sm), ingen fade */
@keyframes toast-slide-out {
  from { transform: translateX(0); }
  to   { transform: translateX(calc(100% + 40px)); }
}

/* Enter — uppifrån (xs), ingen fade */
@keyframes toast-slide-in-top {
  from { transform: translateY(-100%); }
  to   { transform: translateY(0); }
}
/* Exit — uppåt (xs), ingen fade */
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

  // Skapa och positionera toast...
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

## Notifikation – System Inline (ECO Design System)

**Figma:** https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=13377-35659

### Används när
- Feedback eller statusinformation hör direkt till ett specifikt avsnitt, formulär eller innehållsblock på sidan
- Meddelandet ska vara synligt tills användaren agerar eller tillståndet förändras (försvinner **inte** automatiskt)
- Kontextuell information som inte blockerar resten av gränssnittet

### Används INTE när
- Kortlivat svar på en användaråtgärd → använd **Toast** istället
- Åtgärden kräver bekräftelse → använd **Modal**
- Meddelandet gäller ett enskilt formulärfält → använd `form-helper--error`

---

### Storlekar

| Storlek | Höjd | Padding | Ikon |
|---|---|---|---|
| **Medium** | 48px | `12px` alla sidor | 24px |
| **Small** | 32px | `4px` alla sidor | 20px |

---

### Varianter

#### Emphasis
| Emphasis | Bakgrund | Vänster border | Övriga borders |
|---|---|---|---|
| **System Strong** | Statusfärgens svaga bakgrund (se tabell) | `2px solid [statusfärg]` | `1px solid [statusfärg-weak]` |
| **System Weak** | `#ffffff` (`surface-raised-primary`) | `2px solid [statusfärg]` | `1px solid [statusfärg-weak]` |

#### Status + färger

| Status | Vänster border / Ikon | Strong-bakgrund | Höger/topp/botten border | Material Symbol |
|---|---|---|---|---|
| **Informational** | `#0066ff` | `#e2f1ff` (`surface-information-weaker`) | `#d0e9ff` | `info` |
| **Error** | `#d90000` | `#ffebeb` (`surface-danger-weaker`) | `#ffbdc0` | `error` |
| **Success** | `#248616` | `#edffe7` (`surface-success-weaker`) | `#daf6d0` | `check_circle` |
| **Warning** | `#fac000` | `#fff5c2` (`surface-warning-weaker`) | `#ffe167` | `warning` |
| **Informational E-Com** | `#0066ff` | — (alltid Weak, `#ffffff`) | **ingen** | Valfri (ex. `local_shipping`) |

> **Informational E-Com** har alltid vit bakgrund (`surface-raised-primary`, `#ffffff`) och **ingen** höger/topp/botten-border — bara den 2px vänstra blå. Ikonen är ej reserverad och väljs kontextuellt från galleri.

#### Layout-varianter
| Variant | Innehåll |
|---|---|
| **Default** | Statusikon + [Titel (valfri) + Brödtext] + Stäng-knapp |
| **Actionable** | Som Default + knappar och/eller text-länk under texten (indrag `32px`) |

---

### Anatomi

```
[2px border] [Statusikon] [TITEL (VALFRI): Brödtext.]   [✕ stäng 20px]
             [Secondary-knapp] [Primary-knapp]            ← Actionable
             [Text link]                                   ← Actionable
```

- **Vänster border**: `2px solid [statusfärg]`, full höjd
- **Höger/topp/botten border**: `1px solid [statusfärg-weak]`
- **Padding**: `12px` (Medium) / `4px` (Small)
- **Ikon**: Material Symbols Outlined, 24px (Medium) / 20px (Small), färg = statusfärg
- **Gap** mellan ikon och text: `8px`
- **Titel** (valfri): `label-sm` — 14px, Bold, uppercase, `#000`, `letter-spacing: 0.56px`
- **Brödtext**: `body-sm` — 14px/20px, Regular, `#000`, `letter-spacing: 0.28px`
- **Stäng-knapp**: Blank xs, `close`-ikon 20px, `padding: 2px`
- **Shadow**: `elevation-b-20` = `0px 1px 3px 0px rgba(0,0,0,0.10), 0px 0px 1px 0px rgba(0,0,0,0.05)`

#### Actionable — Action Group
- Indrag: `padding-left: 32px`
- Knappar: `gap: 8px`, `padding-top: 16px` från texten
- Knappstorlek: xs (höjd 32px)
- Text-länk: `body-sm` understruken, `padding-top: 8px` under knapparna

---

### CSS-mall

```css
/* Wrapper */
.inline-notification {
  display: flex;
  align-items: stretch;
  box-shadow: 0px 1px 3px 0px rgba(0,0,0,0.10),
              0px 0px 1px 0px rgba(0,0,0,0.05); /* elevation-b-20 */
}

/* Base — vänster border + bakgrund */
.inline-notification__base {
  display: flex;
  align-items: center;
  overflow: hidden;
  position: relative;
  width: 100%;
}

.inline-notification__left-border {
  width: 2px;
  align-self: stretch;
  flex-shrink: 0;
}

/* Container med höger/topp/botten border */
.inline-notification__container {
  flex: 1;
  border-width: 1px 1px 1px 0;
  border-style: solid;
}

.inline-notification__inner {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: 12px;        /* Medium */
  width: 100%;
  box-sizing: border-box;
}

/* Small */
.inline-notification--small .inline-notification__inner {
  padding: 4px;
}

/* Header-rad: ikon + text + stäng */
.inline-notification__header {
  display: flex;
  gap: 8px;
  align-items: flex-start;
  width: 100%;
}

.inline-notification__icon {
  font-size: 24px;        /* Medium */
  flex-shrink: 0;
}
.inline-notification--small .inline-notification__icon {
  font-size: 20px;
}

.inline-notification__text {
  flex: 1;
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 14px;        /* body-sm */
  font-weight: 400;
  line-height: 20px;
  letter-spacing: 0.28px;
  color: var(--color-text-primary);
  font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1;
  padding-top: 2px;
}

.inline-notification__title {
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.56px;
  font-feature-settings: 'ss02' 1, 'ss03' 1;
}

.inline-notification__close {
  flex-shrink: 0;
  background: transparent;
  border: none;
  cursor: pointer;
  padding: 2px;
  font-size: 20px;
  color: var(--color-text-primary);
}

/* Actionable — Action Group */
.inline-notification__actions {
  padding-left: 32px;
  width: 100%;
  box-sizing: border-box;
}

.inline-notification__btn-group {
  display: flex;
  gap: 8px;
  align-items: center;
  padding-top: 16px;
  width: 100%;
}

.inline-notification__link {
  padding-top: 8px;
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 14px;
  font-weight: 400;
  line-height: 20px;
  letter-spacing: 0.28px;
  color: var(--color-text-primary);
  text-decoration: underline;
  cursor: pointer;
}

/* Status — Informational */
.inline-notification--info.inline-notification--strong { background: var(--color-surface-information-weaker); }
.inline-notification--info .inline-notification__left-border { background: var(--color-surface-information-default); }
.inline-notification--info .inline-notification__container { border-color: var(--color-border-information-weak); }
.inline-notification--info .inline-notification__icon { color: var(--color-surface-information-default); }

/* Status — Error */
.inline-notification--error.inline-notification--strong { background: var(--color-surface-danger-weaker); }
.inline-notification--error .inline-notification__left-border { background: var(--color-surface-danger-default); }
.inline-notification--error .inline-notification__container { border-color: var(--color-border-danger-weak); }
.inline-notification--error .inline-notification__icon { color: var(--color-surface-danger-default); }

/* Status — Success */
.inline-notification--success.inline-notification--strong { background: var(--color-surface-success-weaker); }
.inline-notification--success .inline-notification__left-border { background: var(--color-surface-success-default); }
.inline-notification--success .inline-notification__container { border-color: var(--color-border-success-weak); }
.inline-notification--success .inline-notification__icon { color: var(--color-surface-success-default); }

/* Status — Warning */
.inline-notification--warning.inline-notification--strong { background: var(--color-surface-warning-weaker); }
.inline-notification--warning .inline-notification__left-border { background: var(--color-surface-warning-default); }
.inline-notification--warning .inline-notification__container { border-color: var(--color-border-warning-weak); }
.inline-notification--warning .inline-notification__icon { color: var(--color-surface-warning-default); }

/* Weak — vit bakgrund */
.inline-notification--weak { background: var(--color-surface-raised-primary); }

/* Informational E-Com — vit bakgrund, ingen höger/topp/botten-border */
.inline-notification--ecom .inline-notification__container {
  border: none;
}
.inline-notification--ecom .inline-notification__left-border { background: var(--color-surface-information-default); }
.inline-notification--ecom .inline-notification__icon { color: var(--color-surface-information-default); }
```

### HTML-exempel (Default, Informational, System Strong, Medium)

```html
<div class="inline-notification inline-notification--info inline-notification--strong">
  <div class="inline-notification__base">
    <div class="inline-notification__left-border"></div>
    <div class="inline-notification__container">
      <div class="inline-notification__inner">
        <div class="inline-notification__header">
          <span class="material-symbols-outlined inline-notification__icon">info</span>
          <p class="inline-notification__text">
            <span class="inline-notification__title">Titel (valfri):</span> Brödtext.
          </p>
          <button class="inline-notification__close" aria-label="Stäng">
            <span class="material-symbols-outlined">close</span>
          </button>
        </div>
      </div>
    </div>
  </div>
</div>
```

---

## Notifikation – System Banner (ECO Design System)

**Figma:** https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=13377-41997

### Används när
- Sidövergripande meddelanden som rör hela sidan eller systemet (underhåll, driftstörning, kampanj)
- Meddelandet ska vara synligt tills användaren stänger det eller tillståndet förändras — försvinner **inte** automatiskt
- Placeras högst upp på sidan, **ovanför** allt sidinnehåll

### Används INTE när
- Feedback på en specifik handling → använd **Toast** (kortlivad) eller **System Inline** (kontextuell)
- Meddelandet gäller ett enskilt formulärfält → använd `form-helper--error`
- Blockerar åtgärden och kräver bekräftelse → använd **Modal**

---

### Storlek och layout

Bannern har **en storlek (1-Size)** och sträcker sig alltid till **full bredd** av sin behållare eller viewport. Ingen fast bredd sätts — bannern är `width: 100%`.

| Egenskap | Desktop (`md:` 769px+) | Mobile/Tablet (`xs`/`sm` ≤768px) |
|---|---|---|
| Padding | `12px` alla sidor | `8px` alla sidor |
| Ikon | 24px | 24px |
| Titel-text | `label-sm` Desktop: 14px, 0.56px, Bold, uppercase | `label-sm` Mobile: 12px, 0.48px, Bold, uppercase |
| Brödtext | `body-sm` Desktop: 14px/20px, 0.28px, Regular | Mobile: 12px/18px, 0.24px, Regular |

---

### Varianter

#### Emphasis — System-varianter

| Emphasis | Bakgrund | Vänster border | Övriga borders | Textfärg | Layout |
|---|---|---|---|---|---|
| **System Strong** | Statusfärgens svaga bakgrund | `2px solid [statusfärg]` | `1px solid [statusfärg-weak]` | `#000` | Vänsterjusterad |
| **System Weak** | `#ffffff` | `2px solid [statusfärg]` | `1px solid [statusfärg-weak]` | `#000` | Vänsterjusterad |
| **System Extra Strong** | Statusfärgen (solid) | — ingen border — | — ingen border — | `#ffffff` | Centrerad |

> **System Extra Strong** används för bannrar med hög prioritet som måste synas direkt — t.ex. adminimpersonation ("Du agerar som [användare]") eller kritiska driftvarningar. Hela bakgrunden fylls med statusfärgen och texten är vit. Innehållet centreras horisontellt. Kan innehålla en textlänk (understruken, vit).
>
> **Type: Banner** (inte System Inline). Höjd: `48px` desktop (`min-height`), `40px` mobil/tablet (`min-height`). Padding: `8px` desktop, `8px` vertikalt / `16px` horisontellt mobil. Ikon: `info` (FILL 1, filled), 24px, vit. Mobil: vänsterjusterat, text radbryts, gap text↔länk `16px`. Desktop: centrerat, `white-space: nowrap`, gap text↔länk `4px`. "LOGGA UT"-länk: `body-sm--bold-underline` (Bold 700, understruken).

#### Status + färger (identiska med System Inline och Toast)

| Status | Solid (Extra Strong) | Svag (Strong bakgrund) | Border-weak | Ikon-färg | Material Symbol |
|---|---|---|---|---|---|
| **Informational** | `#0066ff` | `#e2f1ff` | `#d0e9ff` | `#0066ff` | `info` |
| **Error** | `#d90000` | `#ffebeb` | `#ffbdc0` | `#d90000` | `error` |
| **Success** | `#248616` | `#edffe7` | `#daf6d0` | `#248616` | `check_circle` |
| **Warning** | `#fac000` | `#fff5c2` | `#ffe167` | `#fac000` | `warning_amber` |

---

#### E-Com Action (kampanjbanner)

Används **enbart** för varumärkesdrivna kampanjbanners — inte för systemstatus. Inget statusikon-system, ingen vänsterborder. Innehållet centreras horisontellt med en varumärkesikon (24px), etikett och valfri textlänk.

| Emphasis | Bakgrund | Textfärg | Ikon |
|---|---|---|---|
| **Brand Strong – Tools** | `#cd1125` (brand röd) | `#ffffff` | Varumärkesikon, vit |
| **Brand Strong – Swedol** | `#c7d300` (brand lime) | `#000000` | Varumärkesikon, svart |
| **Brand B/W** | `#000000` | `#ffffff` | Varumärkesikon, vit |
| **Brand W/B** | `#ffffff` | `#000000` | Varumärkesikon, svart |
| **Brand Weak – Tools** | Ljus brand-bakgrund | `#000000` | Varumärkesikon, svart |
| **Brand Weak – Swedol** | Ljus lime-bakgrund | `#000000` | Varumärkesikon, svart |

- **Typografi**: Titel = `label-md` desktop (16px/16px, 0.48px, Bold, uppercase). Textlänk = `body-md` (16px/24px, 0.32px, Regular, underline).
- **Gap** ikon–text: `8px`. Gap titel–länk: `4px`.
- **Padding**: `8px` alla sidor (desktop och mobil).
- **Höjd**: 40px (desktop och mobil).

---

### Anatomi

**System Strong / System Weak:**
```
[2px border] [Statusikon 24px] [TITEL (VALFRI): Brödtext...]   [✕ stäng 20px]
```

**System Extra Strong:**
```
          [Statusikon 24px] [Brödtext...  ETIKETT  Textlänk]   [✕ stäng 20px]
          ← hela bakgrunden är statusfärgen, allt är centrerat →
```

**E-Com Action:**
```
          [Varumärkesikon 24px] [TITEL - Textlänk]             [✕ stäng 20px]
          ← hela bakgrunden är brandfärgen, allt är centrerat →
```

- **System Strong/Weak**: vänster border `2px solid [statusfärg]`, övriga borders `1px solid [statusfärg-weak]`
- **System Extra Strong**: ingen border alls — bakgrundsblocket är hela statusfärgen
- **Gap** ikon–text: `8px`. Gap titel–länk (E-Com/Extra Strong): `4px`
- **Stäng-knapp**: Blank xs, `close`-ikon 20px, `padding: 2px`
- **Shadow**: `elevation-b-20` = `0px 1px 3px 0px rgba(0,0,0,0.10), 0px 0px 1px 0px rgba(0,0,0,0.05)`

---

### CSS-mall

```css
.banner-notification {
  display: flex;
  align-items: stretch;
  width: 100%;
  box-shadow: 0px 1px 3px 0px rgba(0,0,0,0.10),
              0px 0px 1px 0px rgba(0,0,0,0.05); /* elevation-b-20 */
}

.banner-notification__base {
  display: flex;
  align-items: center;
  width: 100%;
  overflow: hidden;
}

.banner-notification__left-border {
  width: 2px;
  align-self: stretch;
  flex-shrink: 0;
}

.banner-notification__container {
  flex: 1;
  border-width: 1px 1px 1px 0;
  border-style: solid;
}

.banner-notification__inner {
  display: flex;
  gap: 8px;
  align-items: flex-start;
  padding: 12px;
  width: 100%;
  box-sizing: border-box;
}

@media (max-width: 768px) {
  .banner-notification__inner { padding: 8px; }
}

.banner-notification__content {
  display: flex;
  gap: 8px;
  align-items: flex-start;
  flex: 1;
}

.banner-notification__icon {
  font-size: 24px;
  flex-shrink: 0;
  padding-top: 2px;
}

.banner-notification__text {
  flex: 1;
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 14px;
  font-weight: 400;
  line-height: 20px;
  letter-spacing: 0.28px;
  color: var(--color-text-primary);
  font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1;
}

.banner-notification__title {
  font-weight: 700;
  font-size: 14px;
  line-height: 14px;
  letter-spacing: 0.56px;
  text-transform: uppercase;
  font-feature-settings: 'ss02' 1, 'ss03' 1;
}

@media (max-width: 768px) {
  .banner-notification__text { font-size: 12px; line-height: 18px; letter-spacing: 0.24px; }
  .banner-notification__title { font-size: 12px; line-height: 12px; letter-spacing: 0.48px; }
}

.banner-notification__close {
  flex-shrink: 0;
  background: transparent;
  border: none;
  cursor: pointer;
  padding: 2px;
  font-size: 20px;
  color: var(--color-text-primary);
}

/* Status — Informational */
.banner-notification--info.banner-notification--strong { background: var(--color-surface-information-weaker); }
.banner-notification--info .banner-notification__left-border { background: var(--color-surface-information-default); }
.banner-notification--info .banner-notification__container { border-color: var(--color-border-information-weak); }
.banner-notification--info .banner-notification__icon { color: var(--color-surface-information-default); }

/* Status — Error */
.banner-notification--error.banner-notification--strong { background: var(--color-surface-danger-weaker); }
.banner-notification--error .banner-notification__left-border { background: var(--color-surface-danger-default); }
.banner-notification--error .banner-notification__container { border-color: var(--color-border-danger-weak); }
.banner-notification--error .banner-notification__icon { color: var(--color-surface-danger-default); }

/* Status — Success */
.banner-notification--success.banner-notification--strong { background: var(--color-surface-success-weaker); }
.banner-notification--success .banner-notification__left-border { background: var(--color-surface-success-default); }
.banner-notification--success .banner-notification__container { border-color: var(--color-border-success-weak); }
.banner-notification--success .banner-notification__icon { color: var(--color-surface-success-default); }

/* Status — Warning */
.banner-notification--warning.banner-notification--strong { background: var(--color-surface-warning-weaker); }
.banner-notification--warning .banner-notification__left-border { background: var(--color-surface-warning-default); }
.banner-notification--warning .banner-notification__container { border-color: var(--color-border-warning-weak); }
.banner-notification--warning .banner-notification__icon { color: var(--color-surface-warning-default); }

/* Weak — vit bakgrund */
.banner-notification--weak { background: var(--color-surface-raised-primary); }

/* Extra Strong — solid statusfärg, vit text, centrerat */
.banner-notification--extra-strong {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  padding: 8px;
  gap: 8px;
  box-sizing: border-box;
  box-shadow: 0px 1px 3px 0px rgba(0,0,0,0.10),
              0px 0px 1px 0px rgba(0,0,0,0.05); /* elevation-b-20 */
}

.banner-notification--extra-strong .banner-notification__content {
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
}

.banner-notification--extra-strong .banner-notification__message {
  display: flex;
  align-items: center;
  gap: 4px;
}

.banner-notification--extra-strong .banner-notification__icon,
.banner-notification--extra-strong .banner-notification__text,
.banner-notification--extra-strong .banner-notification__close { color: var(--color-text-primary-inverted); }

.banner-notification--extra-strong .banner-notification__text {
  font-size: 14px;
  line-height: 20px;
  letter-spacing: 0.28px;
  white-space: nowrap;
}

.banner-notification--extra-strong .banner-notification__title {
  font-weight: 700;
  font-size: 14px;
  line-height: 14px;
  letter-spacing: 0.56px;
  text-transform: uppercase;
}

.banner-notification--extra-strong .banner-notification__link {
  color: var(--color-text-primary-inverted);
  text-decoration: underline;
  font-size: 14px;
  line-height: 20px;
  letter-spacing: 0.28px;
  cursor: pointer;
}

/* Extra Strong — status-bakgrunder */
.banner-notification--extra-strong.banner-notification--info    { background: var(--color-surface-information-default); }
.banner-notification--extra-strong.banner-notification--error   { background: var(--color-surface-danger-default); }
.banner-notification--extra-strong.banner-notification--success { background: var(--color-surface-success-default); }
.banner-notification--extra-strong.banner-notification--warning { background: var(--color-surface-warning-default); }

/* E-Com Action — kampanjbanner, centrerat, ingen border */
.banner-notification--ecom-action {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 40px;
  padding: 8px;
  gap: 8px;
  box-sizing: border-box;
  box-shadow: 0px 1px 3px 0px rgba(0,0,0,0.10),
              0px 0px 1px 0px rgba(0,0,0,0.05); /* elevation-b-20 */
}

.banner-notification--ecom-action .banner-notification__content {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  flex: 1;
}

.banner-notification--ecom-action .banner-notification__message {
  display: flex;
  align-items: center;
  gap: 4px;
}

.banner-notification--ecom-action .banner-notification__title {
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 16px;   /* label-md */
  font-weight: 700;
  line-height: 16px;
  letter-spacing: 0.48px;
  text-transform: uppercase;
  white-space: nowrap;
}

.banner-notification--ecom-action .banner-notification__link {
  font-size: 16px;   /* body-md */
  font-weight: 400;
  line-height: 24px;
  letter-spacing: 0.32px;
  text-decoration: underline;
  white-space: nowrap;
  font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1;
}

/* Variantfärger (E-Com Action) */
.banner-notification--ecom-tools-strong { background: var(--color-accent-default); color: var(--color-text-primary-inverted); } /* brand-specific: Tools */
.banner-notification--ecom-tools-strong .banner-notification__link { color: var(--color-text-primary-inverted); }
.banner-notification--ecom-swedol-strong { background: var(--color-accent-default); color: var(--color-text-primary); } /* brand-specific: Swedol */
.banner-notification--ecom-bw { background: var(--color-surface-100); color: var(--color-text-primary-inverted); }
.banner-notification--ecom-bw .banner-notification__link { color: var(--color-text-primary-inverted); }
.banner-notification--ecom-wb { background: var(--color-surface-raised-primary); color: var(--color-text-primary); }
```

### HTML-exempel (Informational, System Strong)

```html
<div class="banner-notification banner-notification--info banner-notification--strong">
  <div class="banner-notification__base">
    <div class="banner-notification__left-border"></div>
    <div class="banner-notification__container">
      <div class="banner-notification__inner">
        <div class="banner-notification__content">
          <span class="material-symbols-outlined banner-notification__icon">info</span>
          <p class="banner-notification__text">
            <span class="banner-notification__title">Titel (valfri):</span> Brödtext.
          </p>
        </div>
        <button class="banner-notification__close" aria-label="Stäng">
          <span class="material-symbols-outlined">close</span>
        </button>
      </div>
    </div>
  </div>
</div>
```

### HTML-exempel (System Extra Strong — admin-impersonation)

```html
<div class="banner-notification banner-notification--extra-strong banner-notification--info">
  <div class="banner-notification__content">
    <span class="material-symbols-outlined banner-notification__icon">info</span>
    <div class="banner-notification__message">
      <p class="banner-notification__text">
        Din roll är <span class="banner-notification__title">Administratör</span>
        och du agerar tillfälligt som <strong>Alban Beluli</strong>.
      </p>
      <a href="#" class="banner-notification__link">LOGGA UT</a>
    </div>
  </div>
  <button class="banner-notification__close" aria-label="Stäng">
    <span class="material-symbols-outlined">close</span>
  </button>
</div>
```

### HTML-exempel (E-Com Action, Brand Strong – Tools)

```html
<div class="banner-notification banner-notification--ecom-action banner-notification--ecom-tools-strong">
  <div class="banner-notification__content">
    <span class="material-symbols-outlined banner-notification__icon">tools_power_drill</span>
    <div class="banner-notification__message">
      <p class="banner-notification__title">Kampanjtitel -</p>
      <a href="#" class="banner-notification__link">Textlänk</a>
    </div>
  </div>
  <button class="banner-notification__close" aria-label="Stäng">
    <span class="material-symbols-outlined">close</span>
  </button>
</div>
```

---

## Notifikation – E-Com Modal (ECO Design System)

**Figma:** https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=13377-48335

### Används när
- Åtgärden kräver bekräftelse eller ett aktivt val innan användaren kan fortsätta
- Viktig information måste presenteras utan att användaren kan missa den
- Innehållet kräver fokus och inte kan visas inline utan risk för missförstånd

### Används INTE när
- Kortlivad feedback på en handling → använd **Toast**
- Statusinformation i sidkontext → använd **System Inline**
- Sidövergripande meddelande → använd **System Banner**
- Felmeddelande gäller ett enskilt formulärfält → använd `form-helper--error`

---

### Storlekar och bredder per breakpoint

Desktop och Tablet: Modalen centreras i viewporten. Bakgrundsöverlagringen är `rgba(0,0,0,0.2)`.

| Storlek | Desktop (`md:` 769px+) | Tablet (`sm:` 640–768px) | Mobile (`xs:` 0–639px) |
|---|---|---|---|
| **Small** | `440px` | `440px` | Fyller hela viewporten |
| **Medium** | `600px` | `576px` | Fyller hela viewporten |
| **Large** | `705px` | `576px` | Fyller hela viewporten |

> Välj storlek utifrån mängden innehåll. Small för enkla bekräftelser, Medium/Large för mer komplex information.

> **xs (Mobile):** Modalen är **inte** centrerad. Den fyller hela viewporten: `position: fixed; top: 0; left: 0; width: 100%; height: 100dvh; padding: 16px`. Header+body-sektionen har `flex: 1` så knappar pinnas i botten. Stäng-knapp (`×`) visas i överkant.

---

### Anatomi

```
[LABEL (VALFRI)]                          [✕ stäng]
Title

Body text

[Avbryt]   [Primär åtgärd               ]
```

- **Overlay**: `position: fixed; inset: 0; background: rgba(0,0,0,0.2); z-index: 9998`
- **Modal-panel**: `position: fixed; z-index: 9999`, centrerad med `transform: translate(-50%, -50%); top: 50%; left: 50%`
- **Bakgrund**: `#ffffff` (`surface-raised-primary`)
- **Shadow**: `elevation-b-100` = `0px 16px 24px 0px rgba(0,0,0,0.10), 0px 0px 1px 0px rgba(0,0,0,0.05)`
- **Gap** header-sektion: `8px` vertikalt
- **Header**: `gap: 12px` mellan Label+Title och stäng-knapp
- **Stäng-knapp**: Blank xs, `close`-ikon 20px, `padding: 2px`
- **Knappar i footer**: `gap: 8px`, Avbryt (Secondary xs, fast bredd) + Primär (Primary xs, `flex: 1`)

---

### Typografi per breakpoint

| Element | Desktop (`md:` 769px+) | Tablet + Mobile (`sm-xs` ≤768px) |
|---|---|---|
| **Label** (valfri) | `alt-label-sm`: 14px/14px, 0.56px, Medium(500), uppercase, `text-secondary` #4f4f4f | 12px/12px, 0.48px |
| **Title** | `title-md`: 20px/24px, 0px, Bold | `title-md`: 18px/22px, 0px, Bold |
| **Body text** | `body-md`: 16px/24px, 0.32px, Regular, `text-secondary` #4f4f4f | 16px/22px, 0.32px |
| **Knapp-text** | `label-sm`: 14px/14px, 0.56px, Bold, uppercase | `label-md`: 14px/14px, 0.48px, Bold, uppercase |

---

### Knappar per breakpoint

Knapparna i modalen följer **alltid** ECO Design Systems knappstorlekar:
- **Desktop (lg-md, ≥769px):** knappstorlek **xs** → `height: 32px`, `padding: 6px`, `label-sm` 14px, 0.56px
- **Tablet + Mobile (sm-xs, ≤768px):** knappstorlek **sm** → `height: 32px`, `padding: 6px`, `label-md` 14px, 0.48px

Båda varianter (Avbryt och Primär) är **alltid 32px höga** — oavsett breakpoint och knappvariant.

| | Desktop (`md:` 769px+) | Tablet + Mobile (`sm-xs` ≤768px) |
|---|---|---|
| Modal padding | `24px` | Tablet: `24px` / Mobile xs: `16px` |
| Button group top-gap | `pt-32px` | `pt-24px` |
| Knapp höjd (båda) | `32px` (xs-knapp) | `32px` (sm-knapp) |
| Knapp padding (båda) | `6px` | `6px` |
| Knapp letter-spacing | `0.56px` (label-sm) | `0.48px` (label-md) |

---

### CSS-mall

```css
/* Overlay */
.modal-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0,0,0,0.2);
  z-index: 9998;
}

/* Modal-panel */
.modal {
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 9999;
  background: #ffffff;
  padding: 24px;
  display: flex;
  flex-direction: column;
  box-shadow: 0px 16px 24px 0px rgba(0,0,0,0.10),
              0px 0px 1px 0px rgba(0,0,0,0.05); /* elevation-b-100 */
  width: 440px;       /* Small — default */
  max-width: 800px;
  min-width: 440px;
  box-sizing: border-box;
}

/* Storlekar */
.modal--medium { width: 600px; }
.modal--large  { width: 705px; }

/* Tablet */
@media (min-width: 640px) and (max-width: 768px) {
  .modal--medium,
  .modal--large { width: 576px; }
  .modal { padding: 24px; }
}

/* Mobile */
@media (max-width: 639px) {
  .modal,
  .modal--medium,
  .modal--large {
    width: 375px;
    min-width: 375px;
    max-width: calc(100vw - 32px);
    padding: 16px;
  }
}

/* Header */
.modal__header {
  display: flex;
  gap: 12px;
  align-items: flex-start;
  width: 100%;
}

.modal__header-text {
  display: flex;
  flex-direction: column;
  gap: 8px;
  flex: 1;
  padding-top: 2px;
}

/* Label (valfri) */
.modal__label {
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 14px;          /* alt-label-sm Desktop */
  font-weight: 500;
  line-height: 14px;
  letter-spacing: 0.56px;
  text-transform: uppercase;
  color: #4f4f4f;           /* text-secondary */
  font-feature-settings: 'ss02' 1, 'ss03' 1;
}

@media (max-width: 768px) {
  .modal__label { font-size: 12px; line-height: 12px; letter-spacing: 0.48px; }
}

/* Title */
.modal__title {
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 20px;          /* title-md Desktop */
  font-weight: 700;
  line-height: 24px;
  letter-spacing: 0px;
  color: #000;
  font-feature-settings: 'ss02' 1, 'ss03' 1;
}

@media (max-width: 768px) {
  .modal__title { font-size: 18px; line-height: 22px; }
}

/* Stäng-knapp */
.modal__close {
  flex-shrink: 0;
  background: transparent;
  border: none;
  cursor: pointer;
  padding: 2px;
  font-size: 20px;
  color: #000;
}

/* Body */
.modal__body {
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 16px;          /* body-md */
  font-weight: 400;
  line-height: 24px;
  letter-spacing: 0.32px;
  color: #4f4f4f;           /* text-secondary */
  font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1;
  margin-top: 8px;
}

@media (max-width: 768px) {
  .modal__body { line-height: 22px; }
}

/* Button group */
.modal__footer {
  display: flex;
  gap: 8px;
  align-items: center;
  padding-top: 32px;
  width: 100%;
}

@media (max-width: 768px) {
  .modal__footer { padding-top: 24px; }
}

/* Avbryt — Secondary xs */
.modal__btn-cancel {
  flex-shrink: 0;
  background: transparent;
  border: 1px solid #000;
  cursor: pointer;
  padding: 6px;
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 14px;
  font-weight: 700;
  line-height: 14px;
  letter-spacing: 0.56px;
  text-transform: uppercase;
  color: #000;
  white-space: nowrap;
  font-feature-settings: 'ss02' 1, 'ss03' 1;
}

@media (max-width: 768px) {
  .modal__btn-cancel { padding: 8px; font-size: 16px; line-height: 16px; letter-spacing: 0.32px; }
}

@media (max-width: 639px) {
  .modal__btn-cancel { padding: 4px; font-size: 14px; line-height: 14px; letter-spacing: 0.42px; }
}

/* Primär åtgärd — Primary xs, flex: 1 */
.modal__btn-primary {
  flex: 1;
  background: #000;
  border: none;
  cursor: pointer;
  padding: 6px;
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 14px;
  font-weight: 700;
  line-height: 14px;
  letter-spacing: 0.56px;
  text-transform: uppercase;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  font-feature-settings: 'ss02' 1, 'ss03' 1;
}

@media (max-width: 768px) {
  .modal__btn-primary { padding: 4px; font-size: 14px; line-height: 14px; letter-spacing: 0.42px; }
}
```

### HTML-exempel (Small, Desktop)

```html
<!-- Overlay -->
<div class="modal-overlay" onclick="closeModal()"></div>

<!-- Modal -->
<div class="modal" role="dialog" aria-modal="true" aria-labelledby="modal-title">
  <div class="modal__header">
    <div class="modal__header-text">
      <p class="modal__label">Label (valfri)</p>
      <h2 class="modal__title" id="modal-title">Title</h2>
    </div>
    <button class="modal__close" aria-label="Stäng" onclick="closeModal()">
      <span class="material-symbols-outlined">close</span>
    </button>
  </div>
  <p class="modal__body">Body text.</p>
  <div class="modal__footer">
    <button class="modal__btn-cancel" onclick="closeModal()">Avbryt</button>
    <button class="modal__btn-primary">Bekräfta</button>
  </div>
</div>
```

---

## Notifikation – E-Com Toast (ECO Design System)

**Figma:** https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=13377-22983

### Används när
- En e-handelsåtgärd bekräftas utan att blockera sidan: produkt lagd i varukorg, produkt lagd i favoritlista
- Kortlivad feedback direkt kopplad till produktinteraktion

### Används INTE när
- Systemfel eller statusmeddelanden → använd **System Toast** (med statusfärg)
- Åtgärden kräver bekräftelse → använd **E-Com Modal**

---

### Två varianter

| Variant | Bakgrund | Användning |
|---|---|---|
| **Add to cart** | `#ffffff` vit | Produkt lagd i varukorg — visar produktbild + två CTA-knappar |
| **Informational** | `#000000` svart | Kortlivad info, t.ex. "lagd i favoritlistan" — text + valfri länk |

> Position, animation och auto-hide följer **samma regler som System Toast** (slides in från höger, `cubic-bezier(0.16, 0, 0.16, 1)`, 300ms, auto-hide 3000ms, `position: fixed`).

---

### Bredd och padding per breakpoint

| | Desktop (`md:` 769px+) | Tablet/Mobile (≤768px) |
|---|---|---|
| **Add to cart** bredd | `440px` | `375px` |
| **Informational** bredd | `375px` | `375px` |
| Padding | `24px` | `16px` |

---

### Add to cart — Anatomi

```
[Produktbild 40×40px]  [Produktnamn Bold] brödtext Regular   [✕ stäng]

[Välj tillbehör      ] [Gå till Varukorgen                 ]
```

- Produktbild: `40×40px`, `object-fit: contain`
- Gap bild–text: `16px`
- **Produktnamn**: Bold, `body-md` 16px/18px, `#000`
- **Brödtext**: Regular, `body-md` 16px/24px, `0.32px`, `#000`
- **Stäng-knapp**: `close`-ikon 20px, `padding: 2px`, svart
- **Knappar** (`pt-16px` under texten, `gap: 8px`, båda `flex: 1`):
  - Secondary ("Välj tillbehör"): `border: 1px solid #000`, transparent
  - Primary ("Gå till Varukorgen"): `background: #000`, vit text
  - Desktop: `label-sm` 14px, 0.56px / Tablet+Mobile: `label-md` 14px, 0.42px
  - Desktop knapp-padding: `6px` / Tablet+Mobile: `4px`
- **Shadow**: `elevation-b-80` = `0px 8px 16px 0px rgba(0,0,0,0.10), 0px 0px 1px 0px rgba(0,0,0,0.05)`

---

### Informational — Anatomi

```
[Produktnamn Bold] brödtext Regular         [Visa]  [✕]
```

- Bakgrund: `#000000`
- Border: `1px solid #f6f6f6` (`border-secondary`) — subtil kant på svart yta
- Alla textelement: `color: #ffffff` (`text-primary-inverted`)
- **Text**: Bold produktnamn + Regular beskrivning, `body-md` 16px/24px desktop, 16px/22px mobil
- **"Visa"-länk** (valfri): understruken, `body-md` Regular, `#ffffff`
- **Stäng-knapp**: `close`-ikon 20px, `padding: 2px`, vit
- Gap text–länk–stäng: `12px`
- **Shadow**: `elevation-b-80`

---

### CSS-mall

```css
/* Gemensam bas */
.ecom-toast {
  position: relative;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.10),
              0px 0px 1px 0px rgba(0,0,0,0.05); /* elevation-b-80 */
  width: 440px;        /* Add to cart desktop */
}

/* Add to cart */
.ecom-toast--cart {
  background: #ffffff;
  padding: 24px;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

/* Informational */
.ecom-toast--info {
  background: #000000;
  border: 1px solid #f6f6f6;
  padding: 24px;
  display: flex;
  align-items: flex-start;
  gap: 12px;
  width: 375px;
}

/* Mobile/Tablet */
@media (max-width: 768px) {
  .ecom-toast--cart { padding: 16px; width: 375px; }
  .ecom-toast--info { padding: 16px; }
}

/* --- Add to cart header --- */
.ecom-toast__header {
  display: flex;
  gap: 12px;
  align-items: flex-start;
  width: 100%;
}

.ecom-toast__image-text {
  display: flex;
  gap: 16px;
  align-items: flex-start;
  flex: 1;
}

.ecom-toast__img {
  width: 40px;
  height: 40px;
  object-fit: contain;
  flex-shrink: 0;
}

.ecom-toast__product-text {
  flex: 1;
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 16px;
  color: #000;
  font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1;
}

.ecom-toast__product-name {
  font-weight: 700;
  line-height: 18px;
  font-feature-settings: 'ss02' 1, 'ss03' 1;
}

.ecom-toast__product-desc {
  font-weight: 400;
  line-height: 24px;
  letter-spacing: 0.32px;
}

/* --- Add to cart footer --- */
.ecom-toast__footer {
  display: flex;
  gap: 8px;
  align-items: center;
  padding-top: 16px;
  width: 100%;
}

.ecom-toast__btn-secondary {
  flex: 1;
  background: transparent;
  border: 1px solid #000;
  cursor: pointer;
  padding: 6px;
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 14px;
  font-weight: 700;
  line-height: 14px;
  letter-spacing: 0.56px;
  text-transform: uppercase;
  color: #000;
  white-space: nowrap;
  font-feature-settings: 'ss02' 1, 'ss03' 1;
}

.ecom-toast__btn-primary {
  flex: 1;
  background: #000;
  border: none;
  cursor: pointer;
  padding: 6px;
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 14px;
  font-weight: 700;
  line-height: 14px;
  letter-spacing: 0.56px;
  text-transform: uppercase;
  color: #fff;
  white-space: nowrap;
  font-feature-settings: 'ss02' 1, 'ss03' 1;
}

---

## Tooltip (ECO Design System)

**Figma:** https://www.figma.com/design/42MgqJjV9vfplwQnrUB62r/ECO-Design-System?node-id=316-14656

Tooltips visas vid hover på ikontextlösa knappar och ger en kort etikett som förklarar knappens funktion. Används för **alla** breakpoints.

---

### Storlekar

| Storlek | Padding | Font | Line-height | Letter-spacing |
|---|---|---|---|---|
| **Small** | `8px 12px` | 14px, Regular | 20px | 0.28px |
| **Large** | `16px 24px` | 18px, Regular | 26px | 0.36px |

> Använd alltid **Small** för ikonknappar i verktygsrader och tabellrader.

---

### Utseende

| Egenskap | Värde |
|---|---|
| Bakgrund | `rgba(0,0,0,0.9)` (`surface-100` 90% opacitet) |
| Textfärg | `#ffffff` (`text-primary-inverted`) |
| Font | `Breuer Condensed Regular` |
| `font-feature-settings` | `'ss02' 1, 'ss03' 1, 'ss06' 1` |
| `white-space` | `nowrap` |
| Shadow | `elevation-b-40`: `0px 2px 4px rgba(0,0,0,0.10), 0px 0px 1px rgba(0,0,0,0.05)` |
| Beak | CSS-triangel, 6px hög, ~12.7px bred |

---

### Positioner

| Typ | Beskrivning | Beak-riktning |
|---|---|---|
| **Top** | Tooltip ovanför elementet | Beak pekar nedåt (under tooltip-blocket) |
| **Bottom** | Tooltip nedanför elementet | Beak pekar uppåt (ovanför tooltip-blocket) |
| **Left** | Tooltip till vänster | Beak pekar höger (höger sida av tooltip) |
| **Right** | Tooltip till höger | Beak pekar vänster (vänster sida av tooltip) |
| **Left side top/bottom** | Tooltip vänsterjusterad med offset | Beak vid topp/botten |
| **Right side top/bottom** | Tooltip högerjusterad med offset | Beak vid topp/botten |

> Välj position baserat på var det finns utrymme. Standardval: **Bottom** för knappar i verktygsrader (utrymme nedanför), **Top** för knappar i tabellrader (utrymme ovanför).

---

### Interaktion

- Tooltip visas vid **hover** (CSS `opacity: 1` via `.tooltip-wrap:hover .tooltip`).
- Easing: `motion-ease-standard` (`cubic-bezier(.35,0,.35,1)`), `duration-fast-2` (`100ms`).
- Aldrig synlig vid tangentbordsnavigering (`:focus`) — enbart hover.
- `pointer-events: none` på tooltip-elementet så det inte stör musinteraktion.

---

### HTML-struktur

```html
<!-- Knapp med Bottom-tooltip -->
<div class="tooltip-wrap">
  <button class="action-btn" aria-label="Lägg till användare">
    <span class="ms">person_add</span>
  </button>
  <span class="tooltip tooltip--bottom">Lägg till användare</span>
</div>

<!-- Knapp med Top-tooltip -->
<div class="tooltip-wrap">
  <button class="btn-row-action" aria-label="Redigera">
    <span class="ms">edit</span>
  </button>
  <span class="tooltip tooltip--top">Redigera</span>
</div>
```

> `aria-label` på knappen är obligatorisk och ska ha samma text som tooltip-innehållet.

---

### CSS-mall

```css
.tooltip-wrap {
  position: relative;
  display: inline-flex;
}

.tooltip {
  position: absolute;
  z-index: 300;
  background: rgba(0,0,0,0.9);
  color: #fff;
  font-family: 'Breuer Condensed', Arial, sans-serif;
  font-size: 14px;        /* Small */
  font-weight: 400;
  line-height: 20px;
  letter-spacing: 0.28px;
  white-space: nowrap;
  pointer-events: none;
  opacity: 0;
  transition: opacity 100ms cubic-bezier(.35,0,.35,1); /* duration-fast-2, ease-standard */
  box-shadow: 0px 2px 4px rgba(0,0,0,0.10), 0px 0px 1px rgba(0,0,0,0.05); /* elevation-b-40 */
  font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1;
}

/* Beak — delad bas för alla positioner */
.tooltip::before {
  content: '';
  position: absolute;
  width: 0;
  height: 0;
  border-left: 6.35px solid transparent;
  border-right: 6.35px solid transparent;
}

.tooltip-wrap:hover .tooltip { opacity: 1; }

/* Bottom — tooltip nedanför, beak pekar uppåt */
.tooltip--bottom {
  top: calc(100% + 8px);
  left: 50%;
  transform: translateX(-50%);
  padding: 8px 12px;
}
.tooltip--bottom::before {
  bottom: 100%;
  left: 50%;
  transform: translateX(-50%);
  border-bottom: 6px solid rgba(0,0,0,0.9);
}

/* Top — tooltip ovanför, beak pekar nedåt */
.tooltip--top {
  bottom: calc(100% + 8px);
  left: 50%;
  transform: translateX(-50%);
  padding: 8px 12px;
}
.tooltip--top::before {
  top: 100%;
  left: 50%;
  transform: translateX(-50%);
  border-top: 6px solid rgba(0,0,0,0.9);
}
```

@media (max-width: 768px) {
  .ecom-toast__btn-secondary,
  .ecom-toast__btn-primary { padding: 4px; letter-spacing: 0.42px; }
}

/* --- Informational content --- */
.ecom-toast__info-content {
  flex: 1;
}

.ecom-toast__info-text {
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 16px;
  color: #ffffff;
  font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1;
}

.ecom-toast__info-name {
  font-weight: 700;
  line-height: 18px;
  font-feature-settings: 'ss02' 1, 'ss03' 1;
}

.ecom-toast__info-desc {
  font-weight: 400;
  line-height: 24px;
  letter-spacing: 0.32px;
}

@media (max-width: 768px) {
  .ecom-toast__info-desc { line-height: 22px; }
}

.ecom-toast__info-link {
  font-family: 'Breuer Condensed', sans-serif;
  font-size: 16px;
  font-weight: 400;
  line-height: 24px;
  letter-spacing: 0.32px;
  color: #ffffff;
  text-decoration: underline;
  cursor: pointer;
  white-space: nowrap;
  font-feature-settings: 'ss02' 1, 'ss03' 1, 'ss06' 1;
}

.ecom-toast__close {
  flex-shrink: 0;
  background: transparent;
  border: none;
  cursor: pointer;
  padding: 2px;
  font-size: 20px;
}

/* Svart stäng-knapp (Add to cart) */
.ecom-toast--cart .ecom-toast__close { color: #000; }
/* Vit stäng-knapp (Informational) */
.ecom-toast--info .ecom-toast__close { color: #ffffff; }
```

### HTML-exempel

**Add to cart:**
```html
<div class="ecom-toast ecom-toast--cart">
  <div class="ecom-toast__header">
    <div class="ecom-toast__image-text">
      <img class="ecom-toast__img" src="product.jpg" alt="Produktnamn" />
      <p class="ecom-toast__product-text">
        <span class="ecom-toast__product-name">Carpenter soul hantverksbyxa stretch svart</span>
        <span class="ecom-toast__product-desc"> har lagts till i varukorgen.</span>
      </p>
    </div>
    <button class="ecom-toast__close" aria-label="Stäng">
      <span class="material-symbols-outlined">close</span>
    </button>
  </div>
  <div class="ecom-toast__footer">
    <button class="ecom-toast__btn-secondary">Välj tillbehör</button>
    <button class="ecom-toast__btn-primary">Gå till Varukorgen</button>
  </div>
</div>
```

**Informational:**
```html
<div class="ecom-toast ecom-toast--info">
  <div class="ecom-toast__info-content">
    <p class="ecom-toast__info-text">
      <span class="ecom-toast__info-name">Bälte stretch svart</span>
      <span class="ecom-toast__info-desc"> lades till i favoritlistan.</span>
    </p>
    <a class="ecom-toast__info-link" href="#">Visa</a>
  </div>
  <button class="ecom-toast__close" aria-label="Stäng">
    <span class="material-symbols-outlined">close</span>
  </button>
</div>
```

---

