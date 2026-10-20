# Personas för designfeedback – Swedol och Tools

Tre personas som används för att granska prototyper, flöden och funktioner innan de går vidare. Varje persona har behov, acceptanskriterier (testbara) och ett sätt att ge feedback. Dokumentet är **underlag för granskning, inte ett designsystem** – personorna ger synpunkter på funktion, innehåll och begriplighet, aldrig på färg, typsnitt eller andra tokens (de styrs av ECO och `CLAUDE.md`).

*Status: första version 2026-10-15. Se "Antaganden och luckor" längst ned innan du drar långtgående slutsatser.*

## Filer

| Fil | Innehåll |
|---|---|
| `README.md` (den här) | Översikt, feedbackprotokoll, gemensamma kriterier, konflikter, Tools-anpassning, luckor |
| `fa-jobbet-gjort.md` | Persona 1 – kundtyp *Få jobbet gjort* |
| `effektivitet-och-sakerhet.md` | Persona 2 – kundtyp *Effektivitet och säkerhet* |
| `trygghet-och-inkopsstyrning.md` | Persona 3 – kundtyp *Trygghet och inköpsstyrning* |

## Översikt

| | 1. Mats – *Få jobbet gjort* | 2. Lars – *Effektivitet och säkerhet* | 3. Karin – *Trygghet och inköpsstyrning* |
|---|---|---|---|
| Profil | Budgetmedveten egenföretagare, allmän entreprenör | Traditionell senior snickare och arbetsledare | Teknikintegrerad platschef/arbetsledare |
| Källa (underlag) | *Budget-Conscious Small Contractor* | *Traditional Seasoned Craftsman* | *Tech-Integrated Site Supervisor* |
| Bolagsstorlek | 1–5 anställda | 10–50 anställda | 50–200 anställda |
| Kundtyp (försäljning Sverige) | Den rörliga kunden som handlar mest i butik | Kund med inköpsavdelning som väljer oss för service, kompetens och rådgivning | Kund med inköpsavdelning och avtalat sortiment som handlar nästan allt digitalt |
| Roll i köpet | Köper själv, betalar själv | Bedömer och påverkar vad laget använder, beställer via avtal | Beställare/attestant för platsen, standardiserar utrustning |
| Teknikvana (antagen) | Medel | Låg | Hög |
| Starkaste kanal | Butik + telefon | Telefon + butik/demo | Webb, e-post, plattformar |
| Frågar sig först | "Håller det, och är det billigare i längden?" | "Klarar det kraven, och kan jag fråga någon?" | "Går det att styra, följa upp och bevisa?" |
| Primärt värde i gränssnittet | Snabbhet, tydlig kvalitet, pris | Trygghet, klarspråk, rådgivning | Kontroll, spårbarhet, effektivitet |

Personernas namn är arbetsnamn. Byt dem gärna mot de namn ni redan använder internt.

## Så ger personorna feedback (protokoll)

Använd samma sex steg varje gång, så att feedback går att jämföra mellan prototyper.

1. **Sätt scenariot.** Skriv en mening om vad personen försöker göra i prototypen, t.ex. *"Mats står på bygget och behöver beställa tre par arbetsbyxor i rätt storlek för hämtning i morgon."* Utan scenario blir feedbacken allmän.
2. **Gå igenom som personen.** Gå flödet från ingången personen faktiskt använder (sök, kampanjlänk, Mina sidor) – inte från startsidan om personen aldrig börjar där. Notera var personen tvekar, backar eller hellre skulle ringa.
3. **Pricka av kriterierna.** Gå igenom de gemensamma kriterierna (G-xx nedan) och personens egna (FJG / EOS / TIS). Markera *Uppfyllt / Delvis / Ej uppfyllt / Ej relevant för ytan*.
4. **Sätt allvarlighet** på varje avvikelse (skala nedan).
5. **Kolla konflikter.** Skulle en åtgärd för en persona försämra upplevelsen för en annan? Se "Konflikter mellan personorna".
6. **Sammanfatta** med personens omdöme: *Skulle använda / Tveksam / Skulle inte använda – ringer eller åker till butik istället*, plus de tre viktigaste åtgärderna.

### Allvarlighetsskala

| Nivå | Betydelse |
|---|---|
| **Blocker** | Personen kan inte slutföra uppgiften eller väljer en annan kanal (ringer, åker till butik, köper hos konkurrent) |
| **Major** | Personen slutför men med påtaglig irritation, omväg eller risk för fel |
| **Minor** | Små hinder, otydlighet eller extra moment |
| **Bevara** | Något som fungerar bra för personen och inte får försvinna |

### Mall för en feedbackpunkt

```
Persona:        Mats / Lars / Karin
Yta/steg:       t.ex. Produktsida, storleksväljare
Allvarlighet:   Blocker | Major | Minor | Bevara
Kriterium:      t.ex. FJG-08, G-04
Observation:    vad personen ser eller gör
Varför det spelar roll: kopplat till personens mål eller smärtpunkt
Förslag:        konkret åtgärd, uttryckt med ECO-komponenter (ingen ny styling)
Påverkar andra: ev. konflikt med annan persona
```

### Så ber du om feedback (färdiga formuleringar)

- *"Granska `mypages/users.html` som Karin enligt protokollet i `docs/personas/README.md`. Scenario: hon ska ge en ny arbetsledare rätt behörighet."*
- *"Kör alla tre personorna på den här prototypen och ge en sammanfattning med konflikter."*
- *"Vad skulle Lars inte förstå här? Svara bara med Blocker och Major."*
- *"Bygg acceptanskriterier för den här funktionen utifrån persona 1 och 3."*

### Hur feedbacken används

- Feedback från personorna är **förslag**. Du väljer vilka som genomförs; inget ändras av sig självt.
- Förslag som ändrar innehåll eller tar bort något markeras som sådana.
- Persona-feedback överstyr aldrig ECO. Saknas en komponent eller ett värde för ett förslag ska det flaggas, inte uppfinnas (se `CLAUDE.md`, kvalitetskontroll regel 7).
- Använd kriterierna som **acceptanskriterier** i specar och tickets: kopiera ID och text (t.ex. `TIS-04`) så går de att spåra från krav till granskning.

## Gemensamma kriterier (gäller alla tre)

| ID | Kriterium | Så testar du |
|---|---|---|
| G-01 | **Språk och ton.** Svenska (sv-SE), för Tools norska (nb-NO). Branschens egna ord, inga marknadsfraser utan belägg. | Läs texten högt: skulle en hantverkare säga så? |
| G-02 | **Mobil först.** Kärnflödet fungerar på ca 375 px (xs), ca 700 px (sm, ska se ut som mobil) och 1024 px och uppåt. | Mät `getComputedStyle` vid tre bredder enligt `CLAUDE.md` |
| G-03 | **Pris tydligt.** Pris, enhet (st/förpackning/meter) och momsläge (inkl./exkl.) framgår vid varje pris. Kampanj visar ordinarie pris och giltighet. | Jämför ett pris i lista, produktsida och varukorg |
| G-04 | **Tillgänglighet.** Kontrast och fokus enligt WCAG 2.2 AA, allt går att nå med tangentbord, inget fungerar bara vid hover, tryckytor minst 24 × 24 px (riktvärde 44 × 44 px för handskar). | Tabba igenom, zooma 200 %, testa på touch |
| G-05 | **Alla lägen finns.** Laddar, tomt, fel och lyckat är designade. Felmeddelande säger vad som hänt och vad man gör nu. | Provocera varje läge |
| G-06 | **Väg till människa.** Telefon, e-post eller chatt syns där man kan fastna (checkout, behörighet, retur). | Leta efter kontaktväg på varje feltillstånd |
| G-07 | **Ingen återvändsgränd.** Tillbaka fungerar, destruktiva åtgärder bekräftas och kan helst ångras, man ser var man är (breadcrumb, aktiv flik). | Backa och avbryt mitt i varje flöde |
| G-08 | **Tål dålig uppkoppling.** Innehåll och knappar flyttar sig inte när bilder laddas, och det syns om något pågår. | Strypt nätverk i devtools |
| G-09 | **Loggad in/ut tydligt.** Det framgår vad inloggning ger (pris, avtal, historik) och inloggning är snabb. | Gå som utloggad besökare |
| G-10 | **Rätt fokus i granskningen.** Feedback gäller funktion, innehåll och begriplighet, inte tokens eller komponentstil. | – |

## Vilken persona väger tyngst per yta

● primär, ○ viktig, tom ruta = lågt värde. Vid konflikt vinner den primära personan, om inte annat beslutas.

| Yta | Mats | Lars | Karin |
|---|---|---|---|
| Startsida, kampanjer, Outlet | ● | ○ | |
| Sök och produktlistning | ● | ○ | ○ |
| Produktsida (spec, storlek, certifikat, omdömen) | ● | ● | ○ |
| Jämförelse (`feature-comparison*`) | ● | | ● |
| Omdömen (`reviews`) | ● | ○ | |
| Varukorg, checkout, leverans | ● | ○ | ○ |
| Mina sidor: ordrar, historik, leveranssedlar | ○ | ○ | ● |
| Mina sidor: användare och roller | | ○ | ● |
| Inköpslistor, snabborder, Punchout/EDI | ○ | | ● |
| Tjänster (Smart Service, ReCare, omsömnad, tryck) | ○ | ● | ○ |
| Kundsupport, kontakt, butik | ○ | ● | ○ |

## Konflikter mellan personorna

| Spänning | Vem vill vad | Rekommenderad lösning |
|---|---|---|
| **Snabbhet mot kontroll** | Mats vill köpa i få steg. Karin kräver referensfält och attest. | Kontrollmoment styrs av kundkontot och visas bara för konton som har dem. Mats får standardvärden och inga extra fält. |
| **Digitalt mot mänskligt** | Lars ringer hellre. Karin vill ha full självbetjäning. | Varje flöde är digitalt komplett *och* har en synlig mänsklig utväg. Den utvägen får inte kännas som ett nederlag. |
| **Datatäthet mot enkelhet** | Karin vill ha specifikationstabeller och exporter. Lars vill ha klarspråk. | Klarspråkssammanfattning först, detaljer bakom "Visa alla specifikationer". |
| **Smarta genvägar mot synlighet** | Mats och Karin gillar streckkod, artikelnummer och CSV. Lars hittar dem inte. | Genvägar är tillägg. Den vanliga vägen (sök, välj, köp) fungerar alltid utan dem. |
| **Marknadsföring mot belägg** | Kampanjer driver trafik. Alla tre misstror hype. | Kampanjtext med siffra, standard eller villkor. Inga superlativ utan stöd. |

## Tools (Norge)

Samma behov gäller, men granska med norsk kontext:

- Språk nb-NO, valuta NOK, begrepp som *Velg butikk*, *Følgeseddel*, *Bli kunde*, *Retur og reklamasjon*.
- På tools.no syns *EDI* och *Punchout* som egna sidor, så **Karin** (TIS-10) är sannolikt viktigare där än på swedol.se. Verifiera.
- Tools primära fokuskunder är företag med upp till 50 anställda inom transport, bygg och anläggning, service och verkstad samt tillverkningsindustri, med butik som primär inköpskanal. Sekundärt: jakt, fiske och jordbruk. **Personorna täcker bara byggbranschen**, se luckor nedan.
- Personerna är placerade i Göteborg. För Tools behövs minst ett norskt validerat scenario innan kriterierna används som krav.

## Antaganden och luckor

Läs detta innan du använder personorna som underlag för beslut.

1. **Personorna är inte forskningsbaserade.** De bygger på de tre uppladdade profilerna och dina tre kundtyper. De uppladdade profilerna är skrivna runt arbetskläder. Behoven är därför översatta till webbgränssnitt och köpflöden. Validera mot kunddata, intervjuer och butikspersonal.
2. **Koppling profil till kundtyp är mitt förslag.** Den bygger på bolagsstorlek, inköpssätt och kanaler i profilerna. Säg till om du kopplat dem annorlunda så justeras filerna.
   - *Budget-Conscious Small Contractor* → Få jobbet gjort
   - *Traditional Seasoned Craftsman* → Effektivitet och säkerhet
   - *Tech-Integrated Site Supervisor* → Trygghet och inköpsstyrning
3. **Karin ligger över fokuskundernas storlek** (50–200 anställda, medan fokuskunderna har upp till 50). Hon är med eftersom hon är den enda profilen med digital inköpsstyrning. Fundera på om hon ska justeras ned i storlek.
4. **Teknikvana är antagen.** Skalan (låg/medel/hög) var ikryssad i underlaget men valet följde inte med. Jag har satt Mats medel, Lars låg, Karin hög.
5. **Namn, ålder och exakta inkomster är inte med.** Ålder saknades i underlaget och inkomsten var i USD. Namnen är påhittade arbetsnamn.
6. **Administratören saknas.** Prototyperna i repot rör mycket användarhantering, roller och inköpsflöden (`mypages/users.html`, `feature-comparison-roles.html`). Den som på kundsidan lägger upp användare och behörigheter är inte en av de tre. Karin täcker det delvis (TIS-14), men en fjärde persona (inköpsansvarig/administratör) är motiverad.
7. **Andra branscher saknas** (transport, verkstad, tillverkning, jakt/jordbruk).
8. **Observationer från sajterna (hämtade 2026-10-15) som bör verifieras:** swedol.se anger att man behöver logga in för att se priser. Båda sajterna har streckkodsskanner, "Välj butik", Favoriter, Smart Service och ReCare. tools.no har Punchout, EDI och bedriftskund-registrering. Sökfunktionens beteende gick inte att utläsa.
