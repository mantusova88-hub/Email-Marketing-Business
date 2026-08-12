---
name: shutdown
description: Arbeitssession sauber beenden und Fortschritt sichern. Nutze diesen Skill bei "shutdown", "Feierabend", "ich hör auf für heute", "das war's", "bis morgen", "Session beenden". Sichert offene Punkte, committet Änderungen und gibt einen klaren Startpunkt für morgen.
---

# shutdown — Session sauber beenden

Ziel: Mit gutem Gefühl zuklappen — und morgen ohne Anlaufzeit weitermachen.

## Ablauf

### 1. Zusammenfassen, was passiert ist

Kurz. Maximal 5 Punkte. Nur was wirklich entstanden ist:

```
Heute erledigt:
✅ [Punkt 1]
✅ [Punkt 2]
```

Wenn nichts Greifbares entstanden ist: auch das ist okay.
Dann benennen, was gedacht/entschieden wurde. Denken ist auch Arbeit.

### 2. Offene Fäden sichern

Alles, was mitten in der Arbeit ist, kommt in `inbox.md`
(oder in den laufenden Plan in `plans/`):

- Halbfertige Texte → in `outputs/` speichern, auch unfertig
- Offene Entscheidungen → als `❓ Offen` in die Inbox
- Der nächste logische Schritt → als `✅ Aufgabe` in die Inbox

**Wichtig:** Nichts darf nur im Chat existieren. Der Chat ist morgen weg.

### 3. Pläne aktualisieren

Wenn an einem Plan aus `plans/` gearbeitet wurde:
erledigte Aufgaben auf ✅ setzen, Fortschritt speichern.

### 4. Änderungen sichern (Git)

```bash
git add -A
git status
```

Zeigen, was sich geändert hat. Dann committen mit einer klaren Nachricht
auf Deutsch, z. B. `Newsletter-Sequenz Willkommen erstellt`.

Danach pushen. Wenn kein Push möglich ist: Bescheid sagen, nicht still scheitern.

### 5. Startpunkt für morgen setzen

Das Wichtigste am ganzen Skill:

```
🌅 Morgen startest du hier:
[EINE konkrete Aufgabe — so konkret, dass man sofort loslegen kann.
Nicht "am Newsletter weiterarbeiten", sondern
"Betreffzeile für Mail 3 der Willkommenssequenz schreiben"]
```

### 6. Verabschieden

Warm, kurz, ohne Kitsch. Und wenn der Tag produktiv war: das sagen.

> „Schönen Feierabend, Monika. Heute hast du echt was bewegt. Bis morgen! 👋"

## Was ich NICHT mache

- ❌ Neue Aufgaben vorschlagen („du könntest noch schnell…")
- ❌ Auf Unerledigtes hinweisen
- ❌ Eine lange Liste für morgen aufmachen
- ❌ Fragen, ob sie noch etwas machen will

Feierabend heißt Feierabend. Der Skill soll **abschließen**, nicht öffnen.
