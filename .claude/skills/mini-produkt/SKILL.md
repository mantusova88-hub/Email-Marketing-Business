---
name: mini-produkt
description: Digitales Mini-Produkt von der Idee bis live bauen — Checklisten, Guides, KI-Tools für 7-17 Euro. Nutze diesen Skill bei "Mini-Produkt", "kleines Produkt", "Checkliste erstellen", "Freebie bauen", "Tool bauen", "Guide erstellen", "was kann ich verkaufen", "Produktidee". Deckt Konzept, HTML-Bau, Netlify-Deploy und Systeme.io-Verkauf ab.
---

# mini-produkt — Von der Idee bis zur Verkaufsseite

Monikas bewährtes Format. Bereits gebaut:
`nischengenerator.html`, `checkliste-business-start.html`,
`meal-prep-wochenplaner.html`, `mailerlite-setup-guide.html`

---

## 1. Was ein gutes Mini-Produkt ausmacht

| Kriterium | Konkret |
|---|---|
| **Ein Problem** | Löst genau eine Sache, nicht „alles rund um…" |
| **Schnelles Ergebnis** | In unter 60 Minuten anwendbar |
| **Sofort greifbar** | Am Ende hat sie etwas Fertiges in der Hand |
| **Preis 7–17 €** | Impulskauf-Schwelle. Kein Nachdenken nötig. |
| **Kein Support nötig** | Selbsterklärend, sonst frisst es Monikas Zeit |

**Der Zweck ist nicht der Umsatz.** Es ist die erste Kaufentscheidung —
der Sprung von „Freebie-Sammlerin" zu „Kundin". (→ Skill `funnel`)

---

## 2. Die vier Formate

| Format | Beispiel | Aufwand |
|---|---|---|
| **Checkliste / Workbook** | Business-Start Checkliste | ⭐ niedrig |
| **Schritt-für-Schritt-Guide** | MailerLite-Setup-Guide | ⭐⭐ mittel |
| **Vorlagen-Paket** | 10 E-Mail-Vorlagen | ⭐⭐ mittel |
| **Interaktives KI-Tool** | Nischengenerator | ⭐⭐⭐ hoch, aber stärkstes Verkaufsargument |

---

## 3. Ablauf

### Schritt 1 — Idee schärfen (3 Fragen)
1. Welches **eine** Problem löst es?
2. Was hat sie am Ende **in der Hand**?
3. Warum ist das **jetzt** dran? (Passt es zu Freebie und Angebot?)

> ⚠️ Wenn keine klare Antwort auf Frage 2 kommt: noch nicht bauen.
> „Sie versteht dann X besser" ist kein Ergebnis.

### Schritt 2 — Inhalt strukturieren
- Gliederung erstellen, von Monika absegnen lassen
- Faustregel: **weniger Inhalt, mehr Umsetzbarkeit**
- Jeder Abschnitt endet mit etwas Machbarem

### Schritt 3 — Bauen

**Als HTML-Datei** (Monikas Standard):
- Eine einzige Datei in `outputs/[name].html`
- Branding: Burgund `#800220`, Gold `#B59156`
- Mobile first, Fließtext mind. 17px
- Keine externen Abhängigkeiten (Netlify-tauglich, CSP-sicher)
- Bei Druck-Material: Print-Stylesheet mitliefern

**Bei KI-Tools zusätzlich:**
- API-Key **nie** im Frontend-Code
- Aufruf über Netlify Function (Vorlage: `netlify/functions/generate.js`)
- Aktuelles Modell verwenden — beim Bauen die `claude-api`-Referenz prüfen
- Fehlerfall abfangen: verständliche Meldung statt technischer Fehler

**Als PDF:** über den `pdf`-Skill, oder HTML → Druckansicht.

### Schritt 4 — Preis festlegen

| Format | Preis |
|---|---|
| Checkliste | 7 € |
| Guide / Workbook | 9–12 € |
| Vorlagen-Paket | 12–17 € |
| KI-Tool | 17 € |

Immer krumme Preise vermeiden — 7 €, nicht 6,99 €. Wirkt ehrlicher.

### Schritt 5 — Live bringen
1. **Netlify:** Datei per Drag & Drop hochladen (`reference/anleitungen-deployment.md`)
2. **Systeme.io:** Funnel + Produkt + Bestellseite (`reference/systeme-io-verkaufsseite.md`)
3. **Verkaufstext:** → Skill `landingpage`
4. **Auslieferung testen:** selbst kaufen, prüfen ob alles ankommt

> ⚠️ Schritt 4 wird am häufigsten vergessen — und kostet am meisten.

### Schritt 6 — Verkaufen
- E-Mail an die Liste → Skill `emails`
- Instagram-Posts → Skill `content`
- Als Upsell nach dem Freebie einbauen → Skill `funnel`

---

## 4. Rechtliches (Deutschland)

Bei digitalen Produkten Pflicht:
- **Impressum** und **Datenschutzerklärung** auf der Verkaufsseite
- **Widerrufsbelehrung** + Verzichtserklärung bei digitalen Inhalten
- **Kleinunternehmerregelung** korrekt ausweisen, falls zutreffend
- Preise inkl. MwSt. angeben

Systeme.io stellt dafür Felder bereit. Kein Rechtsrat von mir —
bei Unsicherheit an einen Anbieter für Rechtstexte verweisen.

---

## 5. Dokumentieren

Nach dem Launch anlegen: `outputs/[datum]-produkt-[name].md`

```markdown
# [Produktname]
**Preis:** X € · **Format:** … · **Live seit:** …
**URL:** …
**Löst:** [das eine Problem]
**Verkäufe:** [regelmäßig nachtragen]
**Learnings:** …
```

So entsteht über die Zeit ein echtes Produktportfolio mit Datenbasis.
