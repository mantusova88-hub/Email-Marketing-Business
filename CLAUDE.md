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

```
Email-Marketing-Business/
├── CLAUDE.md                    # Diese Datei — das Herzstück
├── .env                         # API-Keys (lokal, nicht in Git)
├── context/                     # Business-Wissen für Claude
│   ├── business-info.md         # Services, Markt, Angebote
│   ├── personal-info.md         # Wer du bist, deine Rolle
│   ├── stimme.md                # Deine Schreibstimme — Basis aller Texte
│   ├── strategy.md              # Ziele, Fokus, Prioritäten
│   ├── current-data.md          # Aktuelle KPIs und Zahlen
│   ├── zielgruppe-otoene.md     # Echte Zitate deiner Kundinnen
│   └── import/                  # Bestehende Dokumente zum Einlesen
├── profil/                      # Wer bin ich, Positionierung
├── inbox.md                     # Schnell-Notizen (via `capture`)
├── .claude/
│   ├── commands/                # Deine persönlichen Slash Commands
│   └── skills/                  # Deine Skills (siehe Abschnitt 4)
├── module-installs/             # Heruntergeladene Schichten (ZIPs)
├── plans/                       # Implementierungspläne
├── outputs/                     # Fertige Arbeitsergebnisse & Reports
├── reference/                   # Templates, Beispiele, Patterns
└── scripts/                     # Automatisierungs-Skripte
```

---

## 4. Verfügbare Skills

Skills starten von selbst, sobald das Thema passt — du kannst sie aber
auch direkt aufrufen (`/emails`, `/start`, …).

### Daily-Workflow

| Skill | Beschreibung |
|---|---|
| `start` | Session starten — Kontext laden, Fokus für heute vorschlagen |
| `capture` | Idee oder Aufgabe blitzschnell in `inbox.md` festhalten |
| `plan` | Tages- oder Wochenplanung — realistisch, mit Puffer |
| `review` | Rückblick mit Zahlen, Erfolgen und Inbox-Aufräumen |
| `shutdown` | Feierabend — Fortschritt sichern, Startpunkt für morgen setzen |

### Content & Copy

| Skill | Beschreibung |
|---|---|
| `emails` | Newsletter & Sequenzen in deiner Stimme — dein Kerngeschäft |
| `content` | Instagram-Captions, Karussells, Reel-Hooks |
| `werbeanzeigentext` | 5 Meta-Ads-Varianten + Headlines + Descriptions |
| `zielgruppe` | Sprache, Schmerzpunkte & Kauf-Trigger deiner Kundinnen |
| `tony-copy` | Copy nach Tony-Robbins-Techniken — **nur auf expliziten Wunsch** |
| `thumbnail` | Thumbnails, Reel-Cover, Pinterest-Pins (via Canva) |

### Verkauf & Webinare

| Skill | Beschreibung |
|---|---|
| `landingpage` | Opt-in- & Verkaufsseiten — Struktur, Texte, fertiges HTML |
| `funnel` | Funnel-Architektur, Value Ladder, Evergreen, Upsells |
| `webinar` | Webinar-Skripte mit 3-Phasen-Architektur (Framing/Methode/Pitch) |
| `direktverkauf` | Der Verkaufsteil im Live-Format — Pitch & Einwände |
| `mini-produkt` | Mini-Produkt von der Idee bis live (Netlify + Systeme.io) |

### Ads & System

| Skill | Beschreibung |
|---|---|
| `meta-ads-master` | Komplette Kampagnen-Strategie: Targeting, Budget, Audit |
| `pixel` | Meta Pixel einbauen, Events einrichten, testen |
| `wildmail` | Wild Mail / ActiveCampaign — Tags, Automationen, Kampagnen |
| `postfach` | Gmail sortieren, kategorisieren, Antwortentwürfe |
| `setup` | Kontext-Dateien füllen & neue Skills anlegen |

### Slash Commands (bestehend)

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
- **In meiner Stimme** — Bei allen Texten (E-Mails, Posts, Anzeigen, Verkaufsseiten)
  gilt immer `context/stimme.md` und der Skill `zielgruppe`. Keine Ausnahme.
