---
name: review
description: Wochen- oder Monatsrückblick mit Zahlen, Erfolgen und Learnings. Nutze diesen Skill bei "review", "Rückblick", "wie lief die Woche", "Wochenabschluss", "Monatsauswertung", "was hat funktioniert". Räumt außerdem die inbox.md auf und aktualisiert die KPIs.
---

# review — Rückblick & Auswertung

Ziel: Sehen, was wirklich passiert ist — nicht was sich so anfühlt.
Selbständige unterschätzen ihren Fortschritt fast immer.

## Ablauf

### 1. Daten sammeln (still)

- `plans/` — was war geplant?
- `outputs/` — was ist tatsächlich entstanden? (Dateidaten prüfen)
- `inbox.md` — was ist reingekommen?
- `context/current-data.md` — letzter KPI-Stand
- Git-Historie der letzten 7 Tage: `git log --since="7 days ago" --oneline`

### 2. Zahlen aktualisieren

Frage nach den drei KPIs aus `CLAUDE.md`:

1. **Listenwachstum** — neue Subscriber diesen Zeitraum?
2. **Engagement** — Öffnungs- und Klickrate der letzten Kampagne?
3. **Umsatz** — was ist reingekommen?

Wenn Wild Mail / ActiveCampaign angebunden ist, kann ich Kampagnen-Daten
direkt abrufen (`list_campaigns`, `list_contacts`) statt zu fragen.

> ⚠️ Aggregate wie Öffnungsraten-Durchschnitte kann die Schnittstelle nicht
> berechnen — die muss Monika ablesen. Nicht raten, nicht schätzen.

Danach `context/current-data.md` aktualisieren (mit Datum!).

### 3. Report ausgeben

```markdown
## Rückblick — [Zeitraum]

### 🎉 Das hast du geschafft
[Alles Erledigte auflisten — auch das Kleine.
Monika unterschätzt sich. Ich nicht.]

### 📊 Deine Zahlen

| KPI | Vorher | Jetzt | Δ |
|---|---|---|---|
| Subscriber | | | |
| Öffnungsrate | | | |
| Umsatz | | | |

### ✅ Was funktioniert hat
[Konkret: welche Betreffzeile, welcher Post, welches Angebot —
und wenn möglich WARUM]

### 🤔 Was nicht lief
[Sachlich, ohne Vorwurf. Immer mit einer Hypothese, warum.]

### ⬜ Nicht geschafft
[Ehrlich benennen. Dann entscheiden: verschieben, verkleinern oder streichen?]

### 🎯 Fokus für nächste Woche
[EIN Vorschlag, abgeleitet aus dem, was funktioniert hat]
```

### 4. Inbox aufräumen

Jeden Eintrag aus `inbox.md` durchgehen und einsortieren:

| Typ | Wohin |
|---|---|
| 💡 Idee | → `plans/ideen.md` oder direkt in einen Plan |
| ✅ Aufgabe | → in den Wochenplan |
| 📧 E-Mail-Idee | → `reference/email-ideen.md` |
| 📊 Zahl | → `context/current-data.md` |
| 💬 O-Ton | → `context/zielgruppe-otoene.md` (Gold für Texte!) |
| 🔧 Technik | → Aufgabe oder direkt lösen |
| ❓ Offen | → kurz nachfragen oder streichen |

Danach `inbox.md` leeren (Struktur behalten, Einträge raus).

### 5. Hooks in die Bibliothek übernehmen

**Der wichtigste Lernschritt.** Für jede Kampagne und jeden Post dieser Woche:

- Betreffzeile + Öffnungsrate → `reference/hooks-bibliothek.md`
- Instagram-Zeile 1 + Saves/Reichweite → dieselbe Datei
- Anzeigen-Haken + CTR → dieselbe Datei

Einsortieren nach **🏆 Gewinner** (über dem Durchschnitt) oder
**📉 Flop** (darunter) — beim Flop immer eine Vermutung notieren, warum.

> 💡 Das ist der Kreislauf, der den Skill `hooks` mit der Zeit trainiert.
> Ohne diesen Schritt bleibt er bei allgemeinen Formeln stehen.

Ab ~10 Einträgen: Muster auswerten und den Skill `hooks` überarbeiten.

### 6. Erfolge festhalten

Was funktioniert hat, kommt in `context/strategy.md` unter „Was gut läuft".
Das ist Prinzip 5 aus CLAUDE.md: **Feiern was funktioniert.**

Und: Bei echten Meilensteinen (erste 100 Subscriber, erster Verkauf,
bester Monat) das auch wirklich benennen. Nicht abhaken — feiern.

### 7. Speichern

`outputs/review-[datum].md`

## Haltung

- **Erst Erfolge, dann Lücken.** Immer in dieser Reihenfolge.
- **Keine Schuldzuweisung.** „Nicht geschafft" ist eine Info, kein Urteil.
  Wenn eine Woche schlecht lief, weil ein Kind krank war: das ist der Job,
  nicht das Versagen.
- **Muster suchen.** Nach 3–4 Reviews: „Dir fällt auf, dass Newsletter am
  Dienstag besser laufen?" Das ist der eigentliche Wert.
