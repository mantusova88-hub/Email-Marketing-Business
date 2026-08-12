---
name: start
description: Session starten und Kontext laden. Nutze diesen Skill, wenn Monika die Arbeit beginnt — "start", "los geht's", "guten Morgen", "lass uns anfangen", "was steht heute an". Lädt alle Kontext-Dateien, zeigt offene Aufgaben und schlägt den Fokus für heute vor.
---

# start — Session starten

Ziel: In 60 Sekunden von „Laptop auf" zu „Ich weiß genau, was ich jetzt tue."

## Ablauf

### 1. Kontext laden (still, ohne Kommentar)

Lies in dieser Reihenfolge:
- `profil/01_wer-bin-ich.md` — wer Monika ist
- `context/stimme.md` — wie sie klingt
- `context/business-info.md`
- `context/strategy.md` — aktueller Fokus & 90-Tage-Ziele
- `context/current-data.md` — aktuelle Zahlen
- Alles in `context/import/`, falls vorhanden
- Die neuesten 2 Dateien in `outputs/` (was zuletzt entstanden ist)
- Offene Pläne in `plans/`
- `inbox.md` im Root, falls vorhanden (siehe Skill `capture`)

### 2. Kurzes Briefing geben

Maximal 8 Zeilen. Keine Romane. Struktur:

```
Guten Morgen, Monika! ☕

📍 Wo du stehst
[1 Satz: aktueller Fokus aus strategy.md]

✅ Zuletzt erledigt
[1–2 Punkte aus outputs/ oder plans/]

⬜ Offen
[max. 3 offene Punkte aus plans/ und inbox.md]

⚡ Mein Vorschlag für heute
[EINE konkrete Aufgabe — die, die am meisten bewegt]
```

### 3. Auf veraltete Daten hinweisen

Prüfe `context/current-data.md`:
- Steht dort noch `[Datum eintragen]` oder sind Felder leer? → freundlich ansprechen
- Ist der Stand älter als 30 Tage? → „Deine Zahlen sind vom [Datum] — wollen wir die kurz aktualisieren?"

**Aber:** Höchstens EIN Hinweis pro Session. Nicht nörgeln.

### 4. Abschlussfrage

Immer mit einer offenen Frage enden:
> „Klingt das gut — oder hast du was anderes im Kopf?"

## Wichtig

- **Nicht** alle Dateiinhalte wiederholen. Monika weiß, was in ihren Dateien steht.
- **Nicht** mit einer To-do-Liste von 10 Punkten starten. Das lähmt.
- Wenn `context/`-Dateien noch leer sind: nicht meckern, sondern anbieten,
  sie gemeinsam zu füllen (→ Skill `setup`).
- Wenn Monika direkt ein Thema nennt: Briefing überspringen, sofort loslegen.
