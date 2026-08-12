# Newsletter-Skill — Anleitung

Dieser Skill liefert auf Zuruf einen fertigen Newsletter für deine Liste —
inklusive 3 Betreffzeilen + Preheader + Text + Call-to-Action, in deiner Stimme.

## Installation

1. Den Ordner `newsletter-schreiben` in deinen Skills-Ordner kopieren:
   `.claude/skills/` (in deinem Projektordner) oder `~/.claude/skills/`
   (dann gilt er für alle Projekte).
2. Claude einmal neu starten.

## Einrichtung (einmalig, ca. 5 Minuten)

`newsletter-schreiben/SKILL.md` öffnen und **Abschnitt 4 „Dein Business"** sowie
die Pain Points in **Abschnitt 3** ausfüllen. Alle `[Platzhalter]` durch deine
echten Angaben ersetzen.

- **Kein Bock zu tippen?** Leer lassen — beim ersten Mal fragt Claude einmal nach
  und trägt es selbst ein.
- **Schon eine eigene Zielgruppen- oder Markendatei?** Der Skill erkennt vorhandene
  Dateien im `context/`-Ordner automatisch und nutzt sie bevorzugt.

## Nutzung

- „Schreib mir einen Newsletter über [Thema]"
- „Ich brauche eine Mail an meine Liste zum Thema [Thema], CTA ist [Angebot]"
- „Gib mir 3 Betreffzeilen für den Newsletter über [Thema]"
- „Überarbeite diesen Newsletter nach meinen Regeln: [Text einfügen]"

Der Skill greift automatisch, sobald es um Newsletter, E-Mails an die Liste,
Kampagnen oder Betreffzeilen geht. Du kannst ihn aber auch direkt beim Namen
nennen: *„Nutze den Skill newsletter-schreiben für …"*

## Was du bekommst

- 3 Betreffzeilen nach 3 verschiedenen Mustern (Neugier / Nutzen / Story)
- 1 Preheader
- Newsletter-Text nach festem 7-Bausteine-Aufbau, 250–400 Wörter
- Genau **einen** Call-to-Action
- Automatische Ablage unter `outputs/newsletter/JJJJ-MM-TT-thema.md`

## Tipp: Den Skill besser machen

Ganz unten in der `SKILL.md` gibt es die Tabelle **„Was gut funktioniert hat"**.
Trage dort nach jedem Versand Betreff und Öffnungsrate ein. Der Skill lernt so
mit jedem Newsletter dazu — das ist der eigentliche Hebel.
