# CLAUDE.md — Second Brain Workspace

## 1. Worum es hier geht

Dies ist der Workspace für ein **E-Mail-Marketing-Business für selbständige Mamas**.
Ziel ist es, ein vollständig aufgebautes, skalierbares Second Brain zu entwickeln, das mir hilft, mein Business strategisch zu führen, Aufgaben zu automatisieren und fokussiert zu wachsen.

---

## 2. Second Brain Mission

### Fünf Ebenen
1. **Kontext** — Wer bin ich, was ist mein Business, wo stehe ich gerade?
2. **Strategie** — Wohin will ich, was sind meine Prioritäten?
3. **Systeme** — Welche Prozesse und Automatisierungen brauche ich?
4. **Ausführung** — Wie setze ich Schritt für Schritt um?
5. **Wachstum** — Wie messe ich Erfolg und skaliere ich?

### Fünf Prinzipien
1. Klarheit vor Komplexität
2. Fortschritt vor Perfektion
3. Systeme statt Willenskraft
4. Daten als Entscheidungsgrundlage
5. Feiern was funktioniert

### Drei KPIs
- **Listenwachstum** — Neue Subscriber pro Monat
- **Engagement-Rate** — Öffnungs- und Klickrate
- **Umsatz** — Direkt aus E-Mail-Kampagnen generierter Umsatz

---

## 3. Ordnerstruktur

Jede Ebene ist eine eigene `.md`-freundliche Zone — Claude Code liest und schreibt fast ausschließlich `.md`-Dateien, keine `.docx`/`.pdf`. Die Nummerierung gibt die Reihenfolge vor, in der ein neuer Gedanke durch das Second Brain wandert: von **00-inbox** (roh, unsortiert) bis **09-reference** (fertig aufbereitetes Nachschlagewerk).

```
Email-Marketing-Business/
├── CLAUDE.md                    # Diese Datei — das Herzstück
├── .env                         # API-Keys (lokal, nicht in Git)
├── .claude/
│   └── commands/                # Deine persönlichen Slash Commands
├── 00-inbox/                    # Eingang: unsortierte Notizen, neue Uploads zum Einlesen
├── 01-context/                  # Wer bin ich, was ist mein Business, wo stehe ich gerade?
│   ├── business-info.md         # Services, Markt, Angebote
│   ├── personal-info.md         # Wer du bist, deine Rolle
│   ├── wer-bin-ich.md           # Persönlicher Hintergrund & Antrieb
│   └── current-data.md          # Aktuelle KPIs und Zahlen
├── 02-brand/                    # Markenstimme, Tonalität, Design-Richtlinien
├── 03-strategy/                 # Wohin will ich, was sind meine Prioritäten?
│   └── strategy.md              # Ziele, Fokus, Prioritäten
├── 04-projects/                 # Laufende Projekte & Implementierungspläne
├── 05-daily/                    # Tages-/Session-Notizen (datierte Dateien)
├── 06-team/                     # Team & Rollen (aktuell Solo-Business)
├── 07-intelligence/             # Automatisierungs-Skripte & Prozesse
├── 08-resources/                # Fertige Arbeitsergebnisse & Reports (Netlify-Deploy-Ordner)
└── 09-reference/                # Templates, Anleitungen, Patterns
    ├── module-installs/         # Heruntergeladene Schichten (ZIPs)
    └── julia-kurs/               # Sortierte Kurs-Unterlagen von Julia Trost
```

---

## 4. Verfügbare Commands

| Command | Beschreibung |
|---|---|
| `/prime` | Session-Start: Claude scannt alle Kontext-Dateien |
| `/install` | Neue Schicht installieren |
| `/create-plan` | Durchdachten Implementierungsplan erstellen |
| `/implement` | Plan Schritt für Schritt umsetzen |
| `/task-audit` | Aufgaben-Interview + Automatisierungs-Scoring |

---

## 5. Wie sich Claude verhalten soll

- **Geduldig und einsteigerfreundlich** — Erkläre Dinge klar und verständlich, ohne Fachjargon vorauszusetzen
- **Strukturiert** — Gib immer einen klaren nächsten Schritt vor
- **Motivierend** — Feiere Erfolge und Fortschritte aktiv mit
- **Proaktiv** — Weise auf Optimierungspotenziale hin, bevor sie zu Problemen werden
- **Kontextbewusst** — Lade immer zuerst alle Kontext-Dateien, bevor du mit Aufgaben beginnst
- **Auf Deutsch** — Kommuniziere standardmäßig auf Deutsch, es sei denn, ich wechsle die Sprache
