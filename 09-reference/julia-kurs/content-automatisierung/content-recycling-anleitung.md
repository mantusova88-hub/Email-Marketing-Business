# Starter Kit: Monthly Reposting — Top-Performer automatisch nochmal posten

*Dieses Kit analysiert jeden Monat deine Instagram-Performance, identifiziert die Top-Performer und postet sie automatisch nochmal — 1:1, ohne Aenderungen. Gleiche Caption, gleiche Bilder, gleicher Post.*

## Was du am Ende hast

1. Monatliche Analyse deiner Instagram Insights (Saves, Kommentare, Aufrufe, neue Follower)
2. Top-Performer werden automatisch identifiziert
3. Exakt derselbe Post wird nochmal ueber Blotato eingeplant — zeitversetzt um 4 Wochen
4. Null Aufwand: Kein Umschreiben, kein Redesign, einfach nochmal posten

## Warum das funktioniert

- Nur 10–20% deiner Follower sehen einen Post beim ersten Mal
- Der Algorithmus bevorzugt Content der bereits gut performt hat
- Nach 4 Wochen erinnert sich niemand — fuer die meisten ist es neu
- Du hast den Beweis, dass der Post funktioniert (Saves, Kommentare, Reichweite)

## Voraussetzungen

- Claude Code (Max Plan empfohlen)
- Instagram Business Account (fuer Meta Business Suite Insights)
- Blotato-Account mit Instagram verbunden
- Blotato MCP Server in Claude Code verbunden
- Claude in Chrome Extension installiert (fuer Meta Business Suite)

## Teil 1: Posting-Log einrichten

Damit Claude weiss, welche Medien zu welchem Post gehoeren, brauchst du ein Posting-Log. Erstelle die Datei `posting-log.md`:

```
# Posting-Log

## Format
Pro Post ein Eintrag:

### YYYY-MM-DD | [Post-Titel oder Hook]
- Caption: [die komplette Caption]
- Medien-URLs: [Blotato/Canva Export URLs]
- Typ: Karussell / Reel / Single
- Blotato-ID: [falls vorhanden]
---
```

Tipp: Wenn du das Content-System Starter Kit nutzt, wird das Posting-Log automatisch vom Posting-Queue-Task befuellt. Jeder Post, der ueber Blotato eingeplant wird, wird mit Caption und Medien-URLs im Log erfasst.

## Teil 2: Schwellenwerte festlegen

Definiere, ab wann ein Post als Top-Performer gilt. Erstelle die Datei `repost-schwellenwerte.md`:

```
# Repost-Schwellenwerte

Ein Post wird repostet wenn er MINDESTENS EINEN
dieser Werte erreicht:

- Ueber [40] Kommentare
- Ueber [10.000] Aufrufe
- Ueber [10] neue Follower durch den Post

## Zusaetzliche Regeln
- Mindestabstand zum Original: 4 Wochen
- Posts die bereits repostet wurden: Nicht erneut reposten
- Maximal [5] Reposts pro Monat
```

Passe die Zahlen in den eckigen Klammern an deine Account-Groesse an. Kleiner Account = niedrigere Schwellenwerte.

## Teil 3: Scheduled Task — Monthly Repost

Dieser Task laeuft einmal im Monat, schaut in die Meta Business Suite, findet Top-Posts und postet sie nochmal.

Erstelle einen Scheduled Task mit folgenden Einstellungen:
- Name: `monthly-repost-top-content`
- Cron: 1. des Monats 10:00 (`0 10 1 * *`)
- Modell: Sonnet
- Prompt:

```
Monatlicher Instagram Repost der Top-Performer.

## Schritt 1: Meta Business Suite oeffnen
Oeffne die Meta Business Suite im Browser und navigiere
zu den Content Insights der letzten 30 Tage.
Sortiere nach "Gespeichert" (Saves).

## Schritt 2: Top-Performer identifizieren
Lies repost-schwellenwerte.md fuer die Kriterien.
Finde alle Beitraege die mindestens EINEN dieser
Schwellenwerte erreichen:
- Ueber [DEIN KOMMENTAR-SCHWELLENWERT] Kommentare ODER
- Ueber [DEIN AUFRUFE-SCHWELLENWERT] Aufrufe ODER
- Ueber [DEIN FOLLOWER-SCHWELLENWERT] neue Follower

## Schritt 3: Posting-Log abgleichen
Lies posting-log.md und finde fuer jeden Top-Post
die zugehoerigen Medien-URLs und die Original-Caption.

WICHTIG: Nur Posts reposten, fuer die Medien-URLs
im Posting-Log vorhanden sind. Bei fehlenden URLs:
Als offenen Punkt notieren, NICHT raten.

## Schritt 4: Repost planen
Jeden Top-Post ueber Blotato erneut posten:
- accountId: [DEINE BLOTATO INSTAGRAM ACCOUNT-ID]
- platform: instagram
- text: Caption 1:1 uebernehmen (NICHT veraendern!)
- mediaUrls: Exakt die gleichen Medien-URLs aus dem Log
- scheduledTime: 4 Wochen nach dem Originaldatum
  Wenn das Datum schon vergangen ist: Naechsten
  sinnvollen Zeitpunkt waehlen (morgens 9-11 Uhr)
  Nicht mehrere Reposts am gleichen Tag.

## Schritt 5: Ergebnis loggen
Ins Daily Log schreiben:
- Welche Posts als Top-Performer identifiziert wurden
  (mit Saves/Kommentare/Aufrufe-Zahlen)
- Welche Reposts geplant wurden (mit Datum)
- Falls ein Post nicht repostet werden konnte:
  Als offenen Punkt notieren (fehlende Medien-URL etc.)

WICHTIG:
- Caption NICHT veraendern — exakt 1:1 uebernehmen
- Nur Posts reposten fuer die Medien-URLs vorhanden sind
- Bereits im Vormonat repostete Posts nicht erneut reposten
- Maximal [DEIN LIMIT, z.B. 5] Reposts pro Monat
```

## Teil 4: Erster Testlauf

1. Stelle sicher, dass dein Posting-Log mindestens 10 Posts mit Medien-URLs enthaelt
2. Stelle sicher, dass du in Chrome bei Meta Business Suite eingeloggt bist
3. Erstelle die Datei `repost-schwellenwerte.md` mit deinen Werten
4. Starte den Task manuell: Sidebar → monthly-repost-top-content → Run now
5. Klicke alle Tool-Berechtigungen durch
6. Pruefe in Blotato ob die Reposts korrekt eingeplant wurden
7. Pruefe ob die Caption exakt uebernommen wurde

## So nutzt du das System im Alltag

| Wann | Was passiert |
|---|---|
| Laufend | Deine Posts werden automatisch im Posting-Log erfasst (wenn Content-System Kit aktiv) |
| 1. des Monats | Claude oeffnet Meta Business Suite, findet Top-Performer, plant Reposts |
| Naechste 4 Wochen | Reposts erscheinen automatisch auf Instagram — exakt wie das Original |
| Du | Nichts. Null Aufwand. |

## Posting-Log automatisch befuellen

Falls du das Content-System Starter Kit nutzt, wird das Posting-Log bereits automatisch befuellt. Falls nicht, fuege diese Zeilen am Ende deines Posting-Queue Task-Prompts hinzu:

```
Nach erfolgreichem Scheduling:
Schreibe einen Eintrag in posting-log.md:

### [DATUM] | [Design-Name oder Hook]
- Caption: [die komplette Caption]
- Medien-URLs: [die Export-URLs]
- Typ: Karussell
- Blotato-ID: [Submission-ID]
```

## Haeufige Probleme

| Problem | Loesung |
|---|---|
| Keine Top-Performer gefunden | Schwellenwerte in repost-schwellenwerte.md senken |
| Medien-URLs fehlen im Log | Posting-Log manuell ergaenzen oder Content-System Kit einrichten |
| Meta Business Suite laed nicht | In Chrome manuell einloggen, dann Task erneut starten |
| Caption wurde veraendert | Im Prompt nochmal betonen: Caption 1:1 uebernehmen, NICHT veraendern |
| Post wurde doppelt repostet | Pruefe ob der Vormonats-Check im Task funktioniert |
| Blotato lehnt Post ab | Medien-URL pruefen — Canva-Export-URLs laufen nach einiger Zeit ab, dann muss das Design neu exportiert werden |

## Kosten

| Service | Kosten |
|---|---|
| Claude Code (Max Plan) | $100-200/Monat (geteilt mit anderen Tasks) |
| Blotato | Bereits vorhanden |
| Zusaetzliche Kosten | Keine |

*Null Aufwand, null Extra-Kosten. Dein bester Content arbeitet einfach doppelt fuer dich.*
