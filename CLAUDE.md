# Projekt – Designriktlinjer för Claude Code

## Teknikstack
- **HTML + Vanilla JS**
- **Tailwind CSS** för all styling

---

## Innan du bygger en ny sida

**Utgå aldrig från en befintlig, färdigbyggd sida som startpunkt** för en ny prototyp-sida — kopiera alltid rätt mall:

| Sidtyp | Startpunkt | Kännetecken |
|---|---|---|
| **Utloggad/publik sida** | Kopia av `template.html` (repo-rot) | Ingen inloggning krävs. `body`-bakgrund: `background-primary` (vit). |
| **Inloggad sida ("Mina sidor")** | Kopia av `mypages/mypages-template.html` | Kräver inloggning, visar account-nav-tabbar. `body`-bakgrund: `background-secondary` (grå) — det är avsiktligt, se Badge-sektionens regel 7 om `body`-bakgrund. |

Båda mallarna har header/footer/huvudmeny redan kopplade via delade partials (`mypages/partials/`) och samtliga design-tokens på plats — börja aldrig om från noll och kopiera aldrig en annan sidas färdiga innehåll rakt av, då följer sidspecifika CSS-/JS-hack med som inte hör hemma på den nya sidan.

Se `index.html` (repo-rot) för hela sitemap:n — den är en sidöversikt som länkar till samtliga sidor i prototypen och taggar vilken som är "ny"/"uppdaterad"/"pågående"/"arkiv" av varje sidtyp.

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

### Kvalitetskontroll — innan leverans

**IMPORTANT:** Gå igenom denna lista innan en ny eller ändrad sida/komponent rapporteras som klar. Gäller alla sidor i projektet, inte bara enskilda features.

1. **Brytpunkts-koll (viktigast)** — Verifiera att varje ny/ändrad komponent faktiskt växlar vid `769px` (`md`), inte vid `640px` (`sm`) eller någon annan gissad gräns. `sm` (640–768px) ska **alltid** se ut som mobil (Mobile Base Styling) — aldrig Desktop Base Styling. Anta aldrig att CSS:en är rätt bara för att den ser rimlig ut i koden: läs ut faktiska `getComputedStyle(...)`-värden (t.ex. via `javascript_tool` i Browser-panelen) vid minst tre bredder — en `xs` (~375px), en `sm` (~700px) och en `md`/`lg` (~1024px+) — innan du säger att det är klart.
2. **Återanvänd befintliga tokens/mönster** — Sök i filen efter en komponent som redan löser samma sak (knappstorlekar, drawer-chrome, collapsible, checkbox, etc.) innan en ny CSS-klass skapas. Utöka hellre en befintlig klass än att bygga en parallell variant.
3. **CSS-specificitet vid nästling** — När en ny komponent nästlas inuti en befintlig (t.ex. en ikon i en `.form-checkbox-item`-label), kontrollera att inga bredare regler (t.ex. `.form-checkbox-item span`) läcker igenom och stör typsnitt/färg på det nästlade elementet.
4. **Spacing-dubblering** — Om flera element som redan har egen marginal/padding/border staplas i en flex/grid-container med `gap`, kontrollera att gapet inte adderas ovanpå elementens egen spacing.
5. **Interaktion vid alla brytpunkter** — Testa öppna/stäng, hover, checkbox-/radioval etc. i minst mobil- och desktopbredd, inte bara ett fönsterläge, innan leverans.

---


## Komponent-bibliotek — skills-index

> **Saknad komponent?** Om du (eller Claude) stöter på en Figma-komponent eller ett mönster som INTE finns i tabellen nedan: flagga det och fråga innan en ny skill skapas under `.claude/skills/` — lägg aldrig till en ny skill utan att först stämma av. Gäller lika för nya komponenter som för större ändringar i en befintlig.

Varje komponent i ECO Design System är en egen skill under `.claude/skills/<namn>/SKILL.md`. De laddas automatiskt när de behövs — t.ex. laddas bara knapp-specen (`.claude/skills/button/`) när du faktiskt bygger en knapp — så håll den här filen tunn och lägg aldrig tillbaka komponentspecifika CSS-mallar här.

**Grundtokens**

| Skill | Används när |
|---|---|
| `typography` | Använd när du väljer eller granskar typografi/textstilar (Body, Alt-Label, Label, Title, Headline, Display) på Desktop respektive Mobil enligt ECO Design System. |
| `colors` | Använd när du väljer eller granskar färger/design-tokens — text-, ikon-, bakgrunds-, surface-, border- och statusfärger enligt ECO Design System. |
| `spacing` | Använd när du sätter marginal, padding eller gap — den fasta Spacing Scale (space-0…space-120) och de brytpunktsanpassade space-sm/space-md/space-lg-tokens. |
| `elevation` | Använd när du väljer skugga/elevation för kort, modaler, drawers, tooltips eller andra upphöjda ytor — Shadow Bottom/Top, Designated Level (drawers) och komponentspecifika skuggor. |
| `motion` | Använd när du animerar eller transitionerar något — easing-kurvor (decelerate/accelerate/standard) och duration-tokens (fast/medium/slow) enligt ECO Design System. |

**Formulärkomponenter**

| Skill | Används när |
|---|---|
| `button` | Använd när du bygger, ändrar eller granskar knappar (<button>, CTA:er) i swedol-ui-prototype — alla varianter (Primary/Secondary/Blank/Destructive/Accent/System), storlekar och states (hover/focus/disabled) enligt ECO Design System. |
| `input` | Använd när du bygger eller granskar textinputfält — storlekar (Large/Small/XSmall), samtliga states (enabled/hover/active/focus/error/success/disabled) och label/hint-mönster enligt ECO Design System. |
| `select` | Använd när du bygger eller granskar select-fält/dropdowns — storlekar, states och dropdown-pil enligt ECO Design System. |
| `segment-control` | Använd när du bygger eller granskar en segmenterad kontroll (pill toggle) för att växla mellan två relaterade vyer/filter i samma yta — storlekar, den glidande pill-interaktionen och states. Ersätter aldrig Tabs eller Radio-knappar. |
| `checkbox` | Använd när du bygger eller granskar checkboxar — ljusläge (standard och detaljerad tabell-ikon-variant) och mörkt läge (dark mode), inklusive samtliga states (enabled/hover/focus/selected/indeterminate/disabled). |

**Layout**

| Skill | Används när |
|---|---|
| `section` | Använd när du bygger en ny sektion/fullbreddsblock i en sidlayout, inklusive My Pages sidtitel-spacing (main-content/page-preamble) — padding per brytpunkt, bakgrund (Surface Raised Primary/Secondary), page divider och use case för nollad padding. |

**Notifikationer**

| Skill | Används när |
|---|---|
| `notifications-guide` | Använd INNAN du bygger en notifikation, för att avgöra vilken status (Informational/Success/Warning/Error/E-Com) och komponenttyp (Toast/Inline/Banner/Modal/Notification panel) som passar situationen. Läs sedan skillen för den specifika komponenttypen (toast-system, inline-notification, banner-notification, modal-ecom eller toast-ecom). |
| `toast-system` | Använd när du bygger en systemgenererad Toast-notifikation — kortlivad, tidsbaserad feedback på en användaråtgärd (spara/skicka/radera) som glider in/ut och auto-stänger. |
| `inline-notification` | Använd när du bygger en inline-notifikation som ska ligga kvar i sidkontext tills användaren agerar eller tillståndet förändras — inte kortlivad feedback (använd toast-system för det). |
| `banner-notification` | Använd när du bygger en sidövergripande banner-notifikation längst upp på sidan (drift/underhåll/kampanj), inklusive System Extra Strong (admin-impersonation) och E-Com Action (kampanjbanner). |
| `modal-ecom` | Använd när du bygger en modal (E-Com Modal) som kräver bekräftelse eller ett aktivt val innan användaren kan fortsätta — inte för kortlivad feedback eller statusinformation i sidkontext. |
| `toast-ecom` | Använd när du bygger en e-handelstoast — t.ex. "produkt tillagd i varukorgen" (Add to cart-variant med produktbild) eller "lades till i favoritlistan" (Informational-variant, svart bakgrund). |

**Länkar**

| Skill | Används när |
|---|---|
| `links-guide` | Använd INNAN du bygger en länk, för att avgöra om det ska vara en Inline Link (i löptext), Action Link (fristående) eller Tile Link (grafisk/prominent). Läs sedan skillen för den specifika länktypen. |
| `action-link` | Använd när du bygger en fristående klickbar länk med valfri vänster-/höger-ikon som INTE ligger i löptext — t.ex. "Visa alla produkter →". |
| `inline-link` | Använd när du bygger en länk inuti en mening eller ett textblock — alltid understruken i enabled-läge, aldrig med ikon. |
| `tile-link` | Använd när du bygger en grafisk/prominent länk som presenteras som ett kort eller en knapp — varumärkeslogotyper, ikon+label-plattor. Ersätter inte vanliga knappar eller länktyper i löptext. |

**Övriga komponenter**

| Skill | Används när |
|---|---|
| `tooltip` | Använd när du lägger till en tooltip på en ikonknapp eller annat element utan synlig text — visas vid hover, aldrig vid tangentbordsfokus. |
| `collapsible` | Använd när du bygger en radbaserad expanderbar komponent/ackordion, t.ex. en "Vanliga frågor"-sektion (FAQ) — header + animerat innehåll. |
| `role-tier-card` | Använd när du bygger ett rollkort/tier card-par som introducerar två nivåer inom samma kategori (t.ex. Standard/Administratör) sida vid sida och länkar vidare ner till en fullständig jämförelsetabell. |
| `badge` | Använd när du bygger en icke-interaktiv status- eller etikett-indikator (Badge) — t.ex. "Ny", "Uppdaterad", "Arkiv", rollnamn. Inte att förväxla med Tag (interaktiv filtrering) eller kundvagns-räknarens .badge-klass. |
| `breadcrumb` | Använd när du bygger brödsmulor för sidhierarki-navigering — placeras direkt under headern som första element i .page. |
| `pagination` | Använd när du bygger ett "visa fler"-mönster för att stegvis ladda in fler resultat i en lista (recensioner, produkter, orderhistorik) — inte numrerad sidnavigering. |

## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

Rules:
- For codebase questions, first run `graphify query "<question>"` when graphify-out/graph.json exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).
