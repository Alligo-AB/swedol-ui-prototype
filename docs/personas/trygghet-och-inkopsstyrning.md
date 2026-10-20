# Persona 3 – Karin, platschef och beställare (kundtyp *Trygghet och inköpsstyrning*)

> Underlag: *Tech-Integrated Site Supervisor*. Läs först `README.md` för protokoll, allvarlighetsskala och gemensamma kriterier (G-xx). Personens namn är ett arbetsnamn. Se README, "Antaganden och luckor" punkt 3 och 6 om hennes bolagsstorlek och om saknad administratörspersona.

## Kort om Karin

Senior platschef i kommersiellt byggande i Göteborg, 10–15 år i branschen, bolag med 50–200 anställda. Gift med barn. Hon förenar fysiskt arbete på plats med digital projektstyrning (BIM, mobil rapportering) och är ofta först med att pröva nya material och verktyg. Hon beslutar **analytiskt och datadrivet**. I köpsammanhanget är hon **beställare och attestant för platsen** och vill standardisera utrustning över hela företaget. Hon väljer helst den digitala vägen och förväntar sig avtalat sortiment, spårbarhet och rapporter.

| | |
|---|---|
| Plats | Göteborg |
| Bolag | 50–200 anställda, kommersiellt byggande |
| Ansvar | Daglig drift och säkerhet på plats, samordning av underentreprenörer via BIM, kvalitetsbesiktningar, utrustnings- och materialsaldo |
| Teknikvana | Hög (antagen) |
| Beslutsstil | Analytisk och datadriven |
| Påverkare | Certifieringsorgan, ingenjörsnätverk, tekniska produkttestare i sociala medier |
| Kanaler | Slack, e-post, LinkedIn. Teknikpoddar, tekniska YouTube-recensioner, branschtidningar. Specialiserade B2B-handelsplattformar och tillverkares webbplatser. |

## Mål, smärtor och drivkrafter (översatt till gränssnittet)

| Från profilen | Vad det betyder digitalt |
|---|---|
| 100 % efterlevnad av EN 14404 | Certifiering och dokumentation kan visas upp, filtreras och laddas ner |
| Standardisera ergonomisk utrustning i hela företaget | Företagsgemensamma inköpslistor och avtalat sortiment |
| Effektivisera besiktningar med mobila verktyg | Surfplatta/mobil fungerar fullt ut, utan skrivbordsberoende |
| Utvärdera hållbara lösningar | Produktdata om material och hållbarhet, med källa |
| Utrustning som tappar skydd efter industritvätt | Teknisk data om tvättbeständighet, för beslutsunderlag |
| Förseningar när utrustning inte fungerar eller kommer sent | Tydliga ordrar, leveransstatus och lagersaldo |
| Verktygsfickor som hänger upp sig, ingen plats för surfplatta | Specifikationer som går att jämföra och filtrera |

## Behov i uppgiftsform

- När jag beställer för min plats, vill jag att avtalat sortiment och pris gäller direkt och att jag ser vad som ligger utanför avtalet, så att inköpet följer reglerna utan extra arbete.
- När en order kräver godkännande, vill jag se status, vem som ska godkänna och få en notis, så att leveransen inte stannar.
- När jag ska bevisa efterlevnad, vill jag ladda ner certifikat, datablad och tvättinstruktioner till en produkt, så att det håller vid revision.
- När jag följer upp kostnader, vill jag filtrera ordrar på projekt, period och användare och exportera, så att jag kan rapportera.
- När jag standardiserar utrustning, vill jag samla godkända artiklar i en delad lista, så att alla beställer samma sak.
- När jag byter personal på plats, vill jag ändra behörighet utan att riskera att lägga till fel person i fel roll.

## Kontext

Surfplatta och mobil på plats, dator på kontoret. Hon arbetar på 640–768 px (surfplatta, som i ECO ska se ut som mobil) och i liggande läge lika ofta som på dator. Hon förväntar sig att något som fungerar i kontorssystemet också fungerar här: spår, export, integration. Hon testar gränsfall och läser felmeddelanden.

## Acceptanskriterier (TIS)

| ID | Kriterium | Så testar du |
|---|---|---|
| TIS-01 | **Avtalat sortiment tydligt.** Avtalsprodukter är märkta och filtrerbara. Produkter utanför avtalet markeras (eller döljs/blockeras enligt kundens regler) med förklaring. | Sök efter en avtalad och en icke avtalad artikel |
| TIS-02 | **Avtalspris mot listpris.** Avtalspris syns tydligt, med momsläge och enhet. | Jämför pris i lista, produktsida och order |
| TIS-03 | **Behörighet begripliga.** Vem som får beställa, godkänna och se pris framgår. Åtgärder man inte får göra förklarar *varför* i stället för att bara vara inaktiva. | Logga in som användare med begränsad roll |
| TIS-04 | **Godkännandeflöde med status.** Väntar på godkännande, Godkänd, Avvisad, med vem, när och notis. | Följ en order genom alla statusar |
| TIS-05 | **Referensfält.** Projekt, kostnadsställe eller referens kan vara obligatoriskt (styrt av kontot), minns senaste värdet och går att ändra efter order där det är rimligt. | Lägg order med och utan krav |
| TIS-06 | **Historik som går att använda.** Orderhistorik kan filtreras på period, användare, projekt och status, och exporteras (CSV/Excel). Leveranssedlar och fakturor kan nås från ordern. | Hämta en kvartalsrapport per projekt |
| TIS-07 | **Orderstatus tydlig.** Mottagen, plockad, skickad, levererad, med spårning. | Följ en order på mobil |
| TIS-08 | **Dokumentation går att ladda ner.** Certifikat, datablad, tvättinstruktioner och bruksanvisning är nedladdningsbara från produktsidan. | Samla underlag för tre produkter |
| TIS-09 | **Snabb återbeställning.** Delade inköpslistor och favoriter i organisationen. Snabborder via artikelnummer, streckkod eller filuppladdning. | Lägg 20 artiklar på order |
| TIS-10 | **Integration synlig.** Punchout och EDI är tydligt beskrivna (var finns de, vem sätter upp, vad kräver det). Det går alltid att beställa manuellt som reserv. | Hitta och förstå integrationssidan |
| TIS-11 | **Surfplatta fungerar.** Kärnflöden fungerar vid 640–768 px och i liggande läge. Inloggning håller under ett arbetspass. | Testa vid 700 px, bägge lägen |
| TIS-12 | **Jämförbara specifikationer.** Specifikationer i tabell, hållbarhetsdata (material, återvunnet, tvättbarhet) med källa, aldrig påståenden utan belägg. | Jämför tre produkter på fem egenskaper |
| TIS-13 | **Företagsstandard.** En lista med "godkänd standardutrustning" går att skapa, dela och uppdatera. | Skapa och dela en lista |
| TIS-14 | **Säker användarhantering.** Lägga till, ta bort och ändra roll (även flera åt gången) visar konsekvensen innan bekräftelse, går att ångra och loggas. | Ändra roll för tre användare och ångra |

## Röda flaggor (Karin lägger beställningen i ett annat system eller kräver manuell hantering)

- Ingen export, ingen filtrering, ingen historik att gå på.
- Roller och behörigheter som är otydliga så att fel person kan göra fel sak, eller rätt person blockeras utan förklaring.
- Order som "försvinner" utan status eller notis.
- Produktdokumentation som saknas eller är svår att hitta.
- Marknadsföringsspråk om hållbarhet utan källa.
- Tvingas upprepa referensuppgifter på varje order.
- Plattformen fungerar på dator men inte på surfplatta.

## Så reagerar och ger Karin feedback

**Ton:** strukturerad, saklig, lösningsorienterad. Hon beskriver problem som processer och föreslår mått ("hur många klick, hur lång tid?"). Hon testar gränsfall: vad händer om användaren saknar behörighet, om artikeln är slutsåld, om två personer godkänner samtidigt?

**Första frågorna hon ställer:** Vad händer med avtalspriset? Vem kan göra vad? Hur får jag ut det här i Excel? Vad ser jag om något går fel?

**Bevarar och lovordar:** tydlig status, konsekvent logik mellan roller och sidor, export, data som går att jämföra.

**Illustrativa exempel (fiktiva):**

- *"Jag kan ändra rollen men får ingen sammanfattning av vad som ändras. Jag vågar inte klicka."* → TIS-14, Major
- *"Jag vet inte vilka artiklar som ingår i avtalet. Jag måste jämföra mot listan i ett annat dokument."* → TIS-01, Blocker
- *"Filter på projekt och period direkt i orderhistoriken, och export. Bra."* → TIS-06, Bevara

## Frågor att ställa en prototyp som Karin

| Yta | Fråga |
|---|---|
| Sök och lista | Ser jag direkt vad som är avtalat och vad det kostar för oss? |
| Produktsida | Finns dokumentationen jag behöver för revision, och kan jag jämföra? |
| Checkout | Kan jag lägga projekt/kostnadsställe, och går ordern vidare till rätt godkännare? |
| Mina sidor, ordrar | Kan jag filtrera, följa status och exportera? |
| Mina sidor, användare och roller | Förstår jag konsekvensen av varje ändring innan jag bekräftar, och kan jag ångra? |
| Integration | Hittar och förstår jag Punchout/EDI utan att kontakta support? |
| Surfplatta | Fungerar allt vid 700 px och i liggande läge? |

## Exempel på granskning (mall)

```
Persona:        Karin
Yta/steg:       Mina sidor, användare, byt roll för flera användare
Allvarlighet:   Major
Kriterium:      TIS-14, TIS-03, G-07
Observation:    Rollen ändras direkt vid val, utan bekräftelse eller sammanfattning
Varför det spelar roll: Fel behörighet kan ge åtkomst till inköp utanför budget eller blockera en kollega
Förslag:        Bekräftelse (eco-modal-ecom) som listar vad som ändras per användare, och ett "Ångra"-läge i toast (eco-toast-system)
Påverkar andra: Mats påverkas inte (ingen användarhantering). Lars (EOS-06) får en tydlig primär åtgärd.
```
