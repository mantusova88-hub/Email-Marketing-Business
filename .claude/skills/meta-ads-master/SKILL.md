---
name: meta-ads-master
description: Komplette Meta-Kampagnen-Strategie — Targeting, Budget, Kampagnenstruktur, Funnel und Audit bestehender Kampagnen. Nutze diesen Skill bei "Kampagne", "Meta Ads Strategie", "Targeting", "Zielgruppe einstellen", "Budget", "Ads laufen nicht", "Kampagne auswerten", "Ads Audit", "Retargeting". Für die reinen Anzeigentexte siehe werbeanzeigentext.
---

# meta-ads-master — Kampagnen-Strategie

`werbeanzeigentext` schreibt die Texte. Dieser Skill entscheidet,
**was überhaupt geschaltet wird, an wen und mit welchem Budget.**

---

## 1. Die Vorab-Prüfung (nicht überspringen)

Bevor auch nur ein Euro fließt:

- [ ] **Meta Pixel installiert und feuert?** → Skill `pixel`
- [ ] **Freebie-Strecke getestet?** Selbst eingetragen, Mail angekommen?
- [ ] **Opt-in-Seite am Handy geprüft?**
- [ ] **Willkommenssequenz steht?** → Skill `emails`
- [ ] **Etwas zu verkaufen?** Mindestens ein Mini-Produkt (7–17 €)

> ⚠️ **Wenn ein Punkt fehlt: nicht schalten.**
> Ads verstärken ein System. Ein kaputtes System wird durch Ads teurer kaputt.
> Das ehrlich sagen, auch wenn Monika loslegen will.

---

## 2. Kampagnen-Struktur

Nicht direkt auf ein Produkt werben. Drei Stufen:

```
STUFE 1 — Kalte Zielgruppe
  Ziel: Leads (Freebie)
  Budget: 70 %
        ↓
STUFE 2 — Retargeting Website-Besucher
  Ziel: Leads oder Mini-Produkt
  Budget: 20 %
        ↓
STUFE 3 — Retargeting Liste/Käuferinnen
  Ziel: Verkauf (Kurs)
  Budget: 10 %
```

**Für den Start:** Nur Stufe 1. Retargeting lohnt erst ab ca. 1.000
Website-Besuchern im Monat — darunter ist die Zielgruppe zu klein.

---

## 3. Targeting

### Kalte Zielgruppe

| Einstellung | Empfehlung |
|---|---|
| **Standort** | Deutschland, Österreich, Schweiz |
| **Alter** | 30–45 |
| **Geschlecht** | Frauen |
| **Sprache** | Deutsch |
| **Platzierungen** | Automatisch (Meta optimiert besser als wir) |

**Interessen (wenn überhaupt):**
Selbständigkeit, Online-Marketing, Etsy/Shopify, Coaching,
Mompreneur, Nebenberuflich selbständig

> 💡 **Weniger ist mehr.** Metas Algorithmus findet die Zielgruppe inzwischen
> meist besser über das Creative als über Interessen-Auswahl.
> Breit starten (nur Alter/Geschlecht/Land), dann anhand der Ergebnisse verengen.

### Lookalike Audiences
Ab **100 Kontakten** möglich, ab **500** wirklich gut.
Beste Quelle: Käuferinnen > Newsletter-Abonnentinnen > Website-Besucher.
Größe: 1 % (am ähnlichsten).

### Ausschließen
Bestehende Abonnentinnen und Käuferinnen von der kalten Kampagne
ausschließen — sonst zahlt Monika für Leute, die sie schon hat.

---

## 4. Budget

### Einstieg
| | Betrag |
|---|---|
| Testphase | **5–10 €/Tag** pro Anzeigengruppe |
| Testdauer | **mindestens 4–5 Tage** ohne Änderungen |
| Erstes Gesamtbudget | 150–300 € — als Lehrgeld einplanen |

> ⚠️ **Nicht täglich eingreifen.** Meta braucht ca. 50 Conversions pro Woche,
> um zu lernen. Wer nach 24 Stunden abschaltet, hat nichts gemessen.
> Diese Geduld ist der häufigste Fehler.

### Wann skalieren
Erst wenn die Zahlen stimmen (siehe unten): Budget alle 3–4 Tage
um **max. 20 %** erhöhen. Größere Sprünge werfen die Kampagne zurück in die Lernphase.

---

## 5. Die Kennzahlen

| Kennzahl | Gut für Monikas Markt | Wenn schlecht → |
|---|---|---|
| **Kosten pro Lead (CPL)** | 1–3 € | Creative oder Opt-in-Seite prüfen |
| **CTR (Link)** | über 1 % | Creative/Hook zu schwach |
| **Opt-in-Rate der Seite** | 25–45 % | Seite, nicht die Anzeige |
| **CPM** | 8–20 € | Zielgruppe zu eng |
| **Frequenz** | unter 2,5 | Anzeige ist ausgelutscht → neues Creative |

### Die Diagnose-Regel

```
Niedrige CTR          → Problem ist das CREATIVE (Bild/Video/Hook)
Gute CTR, teurer Lead → Problem ist die SEITE (Skill: landingpage)
Gute Leads, kein Kauf → Problem ist die E-MAIL-STRECKE (Skill: emails)
```

**Immer die früheste schwache Stelle zuerst reparieren.**

---

## 6. Audit bestehender Kampagnen

Wenn Monika sagt „meine Ads laufen nicht", in dieser Reihenfolge prüfen:

1. **Pixel** — feuert er? Werden Leads überhaupt gemessen?
2. **Frequenz** — über 2,5? Dann ist die Zielgruppe verbrannt, nicht die Anzeige.
3. **Lernphase** — steckt die Kampagne fest? (zu wenig Budget oder zu viele Änderungen)
4. **Zahlen einzeln durchgehen** — nach der Diagnose-Regel oben
5. **Creative-Alter** — läuft dieselbe Anzeige länger als 3–4 Wochen?
6. **Zielseite am Handy** — lädt sie schnell? Ist der Button ohne Scrollen sichtbar?

Ergebnis als Report in `outputs/ads-audit-[datum].md` mit
**genau einer** priorisierten Empfehlung, nicht zehn.

---

## 7. Creative-Strategie

**Wichtiger als jedes Targeting.** Bei Monikas Zielgruppe funktioniert:

| Format | Was |
|---|---|
| **Selfie-Video** | Monika spricht direkt in die Kamera, ungeschminkt, echt |
| **Alltagsfoto** | Laptop am Küchentisch, Kind im Hintergrund |
| **Text-Grafik** | Ein starker Satz auf Burgund, Gold als Akzent |
| **Freebie-Mockup** | Das Ergebnis sichtbar machen |

**Was nicht funktioniert:** Stockfotos, Hochglanz-Business-Optik,
Frauen im Blazer vor Glasfassade. Das ist nicht Sabines Welt.

**Immer 3–4 Creatives gleichzeitig testen.** Das Creative entscheidet
über 80 % des Ergebnisses.

---

## 8. Ausgabeformat

```markdown
# Meta-Kampagne: [Ziel]

## Voraussetzungs-Check
## Struktur
| Stufe | Ziel | Zielgruppe | Budget/Tag |

## Targeting im Detail
## Creatives (3–4 Ideen)
## Anzeigentexte → Skill werbeanzeigentext
## Budget & Zeitplan
## Was ich nach 5 Tagen prüfe
## Abbruchkriterium
[Ab wann wird gestoppt — vorher festlegen!]
```

Speichern als `plans/ads-[datum]-[kampagne].md`.

---

## 9. Haltung

- **Ehrlich sein, wenn Ads noch nicht dran sind.** Wenn organisch nichts
  konvertiert, konvertiert bezahlt auch nicht.
- **Abbruchkriterium vorher festlegen.** „Wenn der Lead nach 200 € über 5 €
  kostet, stoppen wir." Sonst wird aus Testbudget schleichend Verlust.
- Ads sind **kein Ersatz** für die Liste. Sie sind ein Beschleuniger für ein
  System, das schon funktioniert.
