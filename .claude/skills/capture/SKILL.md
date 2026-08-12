---
name: capture
description: Idee, Gedanke oder Aufgabe blitzschnell festhalten, ohne den Flow zu unterbrechen. Nutze diesen Skill bei "notier mal", "merk dir", "Idee:", "capture", "halt mal fest", "nicht vergessen" — oder wenn Monika mitten in einem anderen Thema etwas Unzusammenhängendes einwirft.
---

# capture — Schnell festhalten

Ziel: Gedanken rauslassen, ohne sie sortieren zu müssen. Sortiert wird später.

## Regel Nummer 1: Schnell sein

Kein Interview. Keine Rückfragen. Keine Kategorisierungs-Diskussion.
Monika wirft etwas rein → ich schreibe es weg → sie macht weiter.

**Antwort: maximal 2 Zeilen.**

## Ablauf

### 1. In `inbox.md` schreiben

Datei im Projekt-Root: `inbox.md`. Falls nicht vorhanden, anlegen mit:

```markdown
# Inbox

> Alles, was schnell festgehalten werden muss.
> Wird bei `/review` sortiert und geleert.

---
```

Neue Einträge **oben** anhängen (neueste zuerst):

```markdown
## [Datum, z.B. 2026-08-12]

- **[Typ]** Der Gedanke im O-Ton von Monika
```

### 2. Typ automatisch erkennen

Ich vergebe den Typ selbst — ohne zu fragen:

| Typ | Wann |
|---|---|
| `💡 Idee` | Produktidee, Content-Idee, „man könnte mal…" |
| `✅ Aufgabe` | Etwas Konkretes zu erledigen |
| `📧 E-Mail` | Newsletter-Idee, Betreffzeile, Sequenz-Gedanke |
| `📊 Zahl` | KPI, Umsatz, Subscriber-Zahl → gehört später in `current-data.md` |
| `💬 O-Ton` | Zitat einer Kundin, Formulierung, Schmerzpunkt → Gold für Texte! |
| `🔧 Technik` | Tool-Problem, Setup-Frage |
| `❓ Offen` | Passt in keine Kategorie |

### 3. Bestätigen — kurz

> „Notiert ✅ (💡 Idee)"

Fertig. Nicht mehr.

**Ausnahme:** Wenn es ein `📊 Zahl`-Eintrag ist, darf ich einen Halbsatz anhängen:
> „Notiert ✅ — soll ich das gleich in `current-data.md` eintragen?"

### 4. Mehrere Dinge auf einmal

Wenn Monika drei Sachen in einem Satz sagt: als drei getrennte Einträge speichern.
Trotzdem nur EINE kurze Bestätigung.

## Was ich NICHT mache

- ❌ Nachfragen, wie sie es meint
- ❌ Die Idee bewerten oder verbessern
- ❌ Vorschlagen, was sie damit tun könnte
- ❌ Einen Plan daraus machen

Das kommt bei `review` und `plan`. Jetzt zählt nur: **raus aus dem Kopf, rein in die Datei.**

## Wann `inbox.md` geleert wird

Beim Skill `review`. Dort wird jeder Eintrag durchgegangen und entweder
in einen Plan überführt, in `context/` einsortiert oder gelöscht.
