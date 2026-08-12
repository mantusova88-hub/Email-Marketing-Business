# Willkommens-Sequenz-Skill — Anleitung

Dieser Skill schreibt dir die komplette Mailstrecke, die neue Subscriber nach
der Anmeldung bekommen: 5 Mails mit Betreff, Preheader, Text und Timing —
in deiner Stimme, fertig zum Einfügen in dein E-Mail-Tool.

## Installation

1. Den Ordner `willkommens-sequenz` in deinen Skills-Ordner kopieren:
   `.claude/skills/` (in deinem Projektordner) oder `~/.claude/skills/`
   (dann gilt er für alle Projekte).
2. Claude einmal neu starten.

## Einrichtung (einmalig, ca. 10 Minuten)

`willkommens-sequenz/SKILL.md` öffnen und den Abschnitt
**"Dein Business — HIER AUSFÜLLEN"** ausfüllen. Alle `[Platzhalter]` durch
deine echten Angaben ersetzen.

Fünf Blöcke sind auszufüllen:
- **Freebie & Einstieg** — womit melden sich Leute an
- **Zielgruppe** — Wunschkundin, 3 Schmerzpunkte, häufigste Einwände
- **Stimme** — Anrede, Tonalität, No-Gos, Signatur
- **Deine Geschichte** — für Mail 2 (wo du angefangen hast, dein Wendepunkt)
- **Angebot** — für Mail 5

Der Block **"Deine Geschichte"** lohnt sich besonders. Mail 2 ist die Mail,
die aus einer Abonnentin eine Leserin macht — und sie lebt komplett von
deiner echten Geschichte.

- **Kein Bock zu tippen?** Leer lassen — beim ersten Mal fragt Claude einmal
  nach und trägt es selbst ein.
- **Schon eine eigene Zielgruppen- oder Markendatei?** Der Skill erkennt
  vorhandene Dateien im `context/`-Ordner automatisch und nutzt sie bevorzugt.
- **Schon den Skill `newsletter-schreiben` im Einsatz?** Dann übernimmt dieser
  Skill die Stimme von dort — beide klingen automatisch gleich.

## Nutzung

- „Bau mir eine Willkommenssequenz für mein Freebie [Name]"
- „Ich brauche Onboarding-Mails für neue Subscriber"
- „Schreib die Welcome-Serie für meinen Kurs [Name]"
- „Überarbeite Mail 4 meiner Sequenz — der Einwand sitzt noch nicht"

Der Skill greift automatisch, sobald es um Willkommenssequenzen,
Onboarding-Mails oder die ersten Mails nach der Anmeldung geht. Du kannst
ihn auch direkt beim Namen nennen: *„Nutze den Skill willkommens-sequenz für …"*

## Was du bekommst

- Eine **Übersichtstabelle** über alle 5 Mails (Versand, Ziel, Betreff)
- **5 vollständige Mails** mit Betreff, Preheader, Text und Timing
- Pro Mail genau **eine Aufgabe** und **einen** Call-to-Action
- Eine **Brücke** am Ende jeder Mail zur nächsten — das hält die Strecke zusammen
- Automatische Ablage unter `outputs/sequenzen/`

## Der Aufbau dahinter

| Mail | Versand | Ziel |
|---|---|---|
| 1 | sofort | Freebie liefern, Erwartung setzen |
| 2 | Tag 2 | Beziehung — deine Geschichte |
| 3 | Tag 4 | Quick Win — ein Ergebnis heute |
| 4 | Tag 6 | Den größten Einwand auflösen |
| 5 | Tag 8 | Angebot vorstellen |

Verkauft wird erst ab Mail 5. Wer in Mail 1 verkauft, verliert die Leserin,
bevor sie überhaupt weiß, wer da schreibt.

## Tipp: Den Skill besser machen

Ganz unten in der `SKILL.md` gibt es die Tabelle **„Was gut funktioniert hat"**.
Trag dort nach den ersten Wochen die Öffnungsraten je Mail ein. Du siehst
sofort, bei welcher Mail die Strecke abreißt — und genau die überarbeitest du
als nächstes.
