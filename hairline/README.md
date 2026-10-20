# Hairline-figurer för component-korten

Experiment: isometriska linjefigurer (skillen `hairline-create`) som möjlig ersättning för bilderna på component-korten på ECO-overview-sidorna. Inget är lagt på korten eller i `index.html` ännu; användaren avgör det efter att flera figurer gjorts.

## Filer (referens: Button)

- `button-pair.js` – figuren. Förebild för nya komponenter.
- `hairline-button-pair.html` – ren, validerad sida (bygg med skillens `build.mjs`, kontrollera med `look.mjs`).
- `button-pair.eco.css` – ECO-färger, typsnitt och kantiga kontroller. Figuren märker sina delar med `data-part`; CSS-filen färgar dem.
- `hairline-button-pair.eco.html` – kopia av den rena sidan med ECO-CSS och unpkg-länkarna (`fonts.css`, `index.css`) inklistrade. Gör den efter varje ombyggnad:
  `</head>` ersätts med de två `<link>`-raderna + `<style>` med CSS-filen.
- `button.js` – första versionen (pillknapp), behålls.

## Arbetsregler

1. Rör inga riktiga sidor (kort, `index.html`, komponentsidor) utan att användaren ber om det.
2. Validatorn avvisar sidan om egna färger/fyllningar eller ändrad bänk finns i den: färger hör hemma i `.eco.css`, den inklistrade kopian är en separat fil.
3. Färger kommer från ECO-tokens (`var(--color-…, #hex)`): Primary `surface-100` (#000), hover på toppen `surface-90` (#222), Secondary-text svart, vit text på Primary.
4. Stil: skarpa 90°-hörn (inga rundningar, inte heller på plattan), Primary och Secondary lika höga och låga (6 enheter), text som kondenserade, tjocka Breuer-lika versaler ritade som slutna konturer (hål vänds, så fyllning lämnar dem öppna). Läsfältet visar namn eller `rest`.
5. Fyllning görs med kärnans klasser (`dot` svart, `fo` fyllnad i bakgrundsfärg), aldrig egna `fill`/`style`.
6. Läs skillens `rules.md` och `look.md`; kör `look.mjs` med `--answer` och `--edge` som världspunkter. Titta på bilden, inte bara på kontrollerna.
7. Svara på svenska, kort. Fråga innan en komponent läggs på ett kort.

Hela förfarandet för en ny komponent står i skillen `eco-card-animation` (`.claude/skills/eco-card-animation/SKILL.md`). Verktyg: `node hairline/make-eco.mjs <namn>` (bygger `.eco.html`) och `node hairline/tools/card-check.mjs <komponent> <prefix>` (Chrome-kontroll av kortet).

## På korten (Button, Switch, Checkbox)

- Button-kortet i `eco-design-system/components-overview.html` visar figuren. Markup: `<div class="ds-card__visual ds-card__visual--hairline"><div data-hairline-card="button-pair" data-src="../hairline/button-pair.js"></div></div>`, plus `hairline/hairline-card.css` i `<head>` och två klassiska skript sist i `<body>` i ordning: `hairline/kernel.js` (kopia av skillens, med ett enda patch: `tour(..., delay)` så play-knappen startar direkt; skillens egen kärna är orörd) och `hairline/embed.js`. `embed.js` hämtar varje figurs `.js` och kör den i en egen funktion, så flera figurer på samma sida delar inga namn (inget behöver ändras i figurerna). Sidan måste köras via server (`npx serve .`), inte file://.
- Scenen måste vara 5:4 (kärnan mappar pekaren på 400 × 320): `hairline-card.css` gör den 300 px bred och förskjuten uppåt, kortets visual (160 px) klipper resten. `hairline-card.css` har ECO-färgerna; håll den i synk med `<figur>.eco.css`.
- Gamla kortbilder arkiveras i `eco-design-system/card-visuals-archive/` (en fil per kort, med instruktion för att byta tillbaka). Button: `button.html`, Switch: `switch.html`.
- Switch-kortet i `components-overview.html` använder `data-hairline-card="switch"`; `index.html` har fortfarande CSS-switcharna. `hairline-card.css` skiljer Switchs gröna `ink` från Buttons svarta via `[data-hairline="switch"]`.
- Select-kortet i `components-overview.html` använder `data-hairline-card="select"` (gammal visual i `card-visuals-archive/select.html`); `overview.html` har fortfarande CSS-selecten.
- Nästa kort: arkivera den gamla visualen där först, lägg sedan till figuren på samma sätt.

## Önskemål för nya figurer

- **Pekare ritad i figuren:** en liten markörpil, byggd av figuren själv (kärnans klasser, svart fyllning med `dot`), som följer pekaren på en spring och följer även turens osynliga pekare. Den kan sänkas eller luta när något trycks. Frågor att avgöra per figur: syns pilen i vila (t.ex. vilande ovanför komponenten, så miniatyren förklarar sig) eller först när pekaren kommer in? Detta bryter mot skillens regel 10 (inga ikoner/pilar) på användarens uttryckliga önskemål; säg det i överlämningen.
- Be användaren om en skärmdump av den riktiga komponenten (helst av/på-lägen och storlekar) innan bygget, och fråga vilken gest figuren ska ha.

## Öppet

- Swedol-accent på Primary (token ej vald; frågan var om bara Primary eller båda).
- Mörkt läge är inte provat (ECO har inget mörkt tema).
- Fler komponenter: Checkbox, Radio, Input, Tabs, Tooltip föreslagna, ingen vald.

- **Radio button** (`radio.js`, `radio.eco.css`, kort-CSS i `hairline-card.css`): tre brunnar i en platta, en vald (svart prick). Tryck flyttar pricken. Inte bytt in på korten än (väntar på OK).
- Checkbox-kortet i `components-overview.html` använder `data-hairline-card="checkbox"` (ikryssad + två tomma rutor, tryck sänker rutan och ritar bocken, 150 ms). Gammal visual: `card-visuals-archive/checkbox.html`. `overview.html` oförändrad.
- Range (`range.js`, `range.eco.css`, `hairline-range.html`/`.eco.html`): efter riktiga komponenten (skärmdump): platta med titel DURATION, värde, tunn linje, svart tumme och stegetiketter 100–450; hover ger halo, drag snäpper steg för steg. Kortet i `components-overview.html` är utbytt (2026-10-20); `overview.html` har fortfarande CSS-versionen.
- Button group (`button-group.js`, `button-group.eco.css`, `hairline-button-group.html`/`.eco.html`): tre sammanfogade knappar S M L på en platta, M vald (sänkt, grå topp = komponentens black-12). Hover sänker och tonar, tryck sänker den tryckta och den förra valda poppar upp (Button-figurens DOWN/UP-springs). Kortet i `components-overview.html` är utbytt (2026-10-20, gammal visual i `card-visuals-archive/button-group.html`); `eco-design-system/index.html` har fortfarande CSS-versionen.
- Tour speed per card: `data-travel` / `data-dwell` (ms) on the `data-hairline-card` div (kernel `tour(..., delay, pace)`); Button group uses 450/450 and presses S, M, L.
- Button group: the last pressed button stays selected after the tour ends (no reset to M); the next lap starts on S.
- Textarea (`textarea.js`, `textarea.eco.css`, `hairline-textarea.html`/`.eco.html`): härledd från Input. Hög textruta i platta, etikett COMMENT, hint; hover skriver tre rader med textmarkör, tryck fokuserar, hörnet (två streck, resizer) sträcker rutan 12 enheter. Tur: fält → hörn. Kortet i `components-overview.html` är utbytt (2026-10-20, gammal visual i `card-visuals-archive/textarea.html`); `eco-design-system/index.html` har samma kort utbytt.
- Tabs (`tabs.js`, `tabs.eco.css`, `hairline-tabs.html`/`.eco.html`): Primary-flik-rad på en platta (OVERVIEW aktiv, DETAILS, REVIEWS med röd räknare, SUPPORT, efter riktiga komponenten). Hover gråar etiketten och växer en ljus linje; tryck glider den svarta aktiva linjen (300 ms `ease-standard`, `--duration-medium-2`). Kortet i `components-overview.html` är utbytt (2026-10-20), gammal visual i `card-visuals-archive/tabs.html`; `index.html` har fortfarande CSS-versionen. `card-check.mjs` tar `PORT=…` om 4173 är upptagen.
- Pill segment control (`pill.js`, `pill.eco.css`, `hairline-pill.html`/`.eco.html`): stadium track recessed in a slab, two segments (ALL, NEW) and a black pill. Hover darkens the track and underlines the inactive label; press slides the pill (300 ms `ease-standard`, the component's own) and the labels swap (grey on floor, white on the pill). Kortet i `components-overview.html` är utbytt (2026-10-20, gammal visual i `card-visuals-archive/pill-segment-control.html`); `overview.html` har fortfarande CSS-versionen. Turen visas bara när pekaren är på kortets text, inte över själva figuren (då tar riktig pekare över).
