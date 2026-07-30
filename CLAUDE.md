# CLAUDE.md — Second Brain Workspace

## 1. Worum es hier geht

Dies ist der Workspace für ein **E-Mail-Marketing-Business für selbständige Mamas**.
Ziel ist es, ein vollständig aufgebautes, skalierbares Second Brain zu entwickeln, das mir hilft, mein Business strategisch zu führen, Aufgaben zu automatisieren und fokussiert zu wachsen.

Praktisch ist dieses Repo zweierlei:

1. **Wissensspeicher** — Kontext-, Strategie- und Profil-Dateien, damit Claude das Business versteht.
2. **Produktions-Repo** — hier entstehen die verkaufsfertigen Mini-Produkte (einzelne HTML-Seiten), die über **Netlify** live gehen und über **Systeme.io** verkauft werden.

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
├── README.md                    # Kurzbeschreibung des Repos
├── .env                         # API-Keys (lokal, per .gitignore ausgeschlossen)
├── netlify.toml                 # Netlify-Config: publish = outputs/, functions = netlify/functions/
│
├── profil/                      # Gepflegtes Persönlichkeits-/Positionierungsprofil
│   └── 01_wer-bin-ich.md        # Name, Zielgruppe, Kernversprechen, Angebot  ← ausgefüllt
│
├── context/                     # Business-Wissen für Claude (Templates, teils noch leer)
│   ├── business-info.md         # Services, Markt, Angebote, Branding-Farben
│   ├── personal-info.md         # Wer du bist, deine Rolle
│   ├── strategy.md              # Ziele, Fokus, Prioritäten
│   ├── current-data.md          # Aktuelle KPIs und Zahlen
│   └── import/                  # Bestehende Dokumente zum Einlesen
│
├── .claude/
│   └── commands/                # Persönliche Slash Commands (prime, install, …)
│
├── outputs/                     # Fertige Arbeitsergebnisse — zugleich Netlify-Publish-Ordner!
│   ├── index.html               # Startseite der Netlify-Site (= Nischengenerator)
│   ├── nischengenerator.html    # KI-Tool: 3 Nischen-Vorschläge (Claude API)
│   ├── checkliste-business-start.html
│   ├── mailerlite-setup-guide.html
│   ├── meal-prep-wochenplaner.html
│   └── 2026-06-01-session-nischengenerator.md   # Session-Protokoll
│
├── netlify/
│   └── functions/
│       └── generate.js          # Serverless-Proxy zur Claude API (CORS-sicher)
│
├── reference/                   # Anleitungen, Templates, Patterns
│   ├── anleitungen-deployment.md      # Netlify + Systeme.io Schritt für Schritt
│   └── systeme-io-verkaufsseite.md    # Verkaufsseite für die Checkliste
│
├── plans/                       # Implementierungspläne (aktuell leer)
├── module-installs/             # Heruntergeladene Schichten (ZIPs)
└── scripts/                     # Automatisierungs-Skripte (aktuell leer)
```

> **Wichtig:** `outputs/` ist kein reiner Ablage-Ordner. Netlify veröffentlicht genau diesen
> Ordner (`netlify.toml` → `publish = "outputs"`). Alles, was hier landet, ist nach dem
> Deploy öffentlich unter `https://<site>.netlify.app/<dateiname>.html` erreichbar.

---

## 4. Verfügbare Commands

| Command | Beschreibung |
|---|---|
| `/prime` | Session-Start: Claude scannt alle Kontext-Dateien |
| `/install` | Neue Schicht aus `module-installs/` installieren |
| `/create-plan` | Durchdachten Implementierungsplan erstellen → `plans/plan-[datum]-[thema].md` |
| `/implement` | Plan Schritt für Schritt umsetzen und Fortschritt zurückschreiben |
| `/task-audit` | Aufgaben-Interview + Automatisierungs-Scoring → `outputs/task-audit-[datum].md` |

Die Definitionen liegen als Markdown in `.claude/commands/`. Jeder Command beschreibt einen
Interview-Ablauf plus das Zielformat der Ausgabe — halte dich beim Ausführen an diese Struktur.

---

## 5. Die Produkte (aktueller Stand)

Alle Produkte sind **eigenständige, in sich geschlossene HTML-Dateien** — kein Build-Schritt,
kein Framework, keine externen Assets. Öffnen per Doppelklick funktioniert, Deployment per
Netlify auch.

| Datei | Was es ist | Besonderheit |
|---|---|---|
| `outputs/nischengenerator.html` | KI-Tool, 4-Schritt-Formular → 3 Nischen-Vorschläge | Ruft die Claude API über die Netlify-Function auf |
| `outputs/index.html` | Startseite der Netlify-Site | **Kopie** des Nischengenerators |
| `outputs/checkliste-business-start.html` | Business-Start-Checkliste, 7 € Mini-Produkt | Statisch, abhakbar |
| `outputs/mailerlite-setup-guide.html` | „Deine erste E-Mail-Liste in 5 Tagen" | Statischer Guide |
| `outputs/meal-prep-wochenplaner.html` | Wochenplaner für Selbstständige Mamas | Speichert Wochen in `localStorage` |

> **Fallstrick:** `index.html` und `nischengenerator.html` sind fast identisch (aktuell nur eine
> Zeile Unterschied in der Fehlerbehandlung). Änderungen am Nischengenerator **immer in beiden
> Dateien** spiegeln — sonst driften Startseite und Direktlink auseinander.

---

## 6. Technik: wie der Nischengenerator funktioniert

```
Browser (outputs/index.html)
   │  POST { prompt, apiKey }
   ▼
/.netlify/functions/generate   (netlify/functions/generate.js)
   │  https-Request, Header x-api-key + anthropic-version: 2023-06-01
   ▼
https://api.anthropic.com/v1/messages
```

Konventionen dabei:

- **Kein `fetch` in der Function** — sie nutzt bewusst das Node-`https`-Modul (siehe Commit
  „Fix: Netlify function mit https-Modul statt fetch"). Beim Bearbeiten dabei bleiben.
- **Der API-Key kommt vom Nutzer**, nicht aus dem Repo. Er wird im Browser unter dem
  `localStorage`-Schlüssel `claudeKey` gespeichert und pro Request mitgeschickt. Nie einen
  echten Key in eine Datei schreiben oder committen.
- **Direkter Browser-Aufruf der Anthropic-API ist nicht möglich** (CORS) — deshalb existiert der
  Function-Proxy. Nicht auf einen Direktaufruf zurückbauen.
- Das in der Function gesetzte Modell (`model` in `netlify/functions/generate.js`) ist die
  einzige Stelle, an der die Modellwahl steht — dort ändern, nicht im HTML.
- Node-Bundler ist `esbuild`, es gibt **keine** `package.json` und keine Dependencies. Die
  Function muss mit reinen Node-Builtins auskommen.

---

## 7. Konventionen für neue Produkte

- **Branding-Farben** (definiert in `context/business-info.md`, als CSS-Variablen in jedem Produkt):
  - Burgund `#800220` · dunkel `#5c0118` · Hover `#a0032a`
  - Gold `#B59156` · hell `#d4a96a`
  - Creme-Hintergrund `#fdf8f3`, Text `#2c1810` / `#5a3a2a` / `#9a7a6a`
- **Schrift:** Georgia / Serif — warm, persönlich, kein Tech-Look.
- **Aufbau:** Header mit Verlauf (Burgund → dunkles Burgund) plus goldene Radial-Glows,
  darunter Karten-Sektionen auf Creme.
- **Sprache:** durchgehend Deutsch, `<html lang="de">`, du-Ansprache, Emojis sparsam als Akzent.
- **Responsiv:** muss auf dem Handy funktionieren — die Zielgruppe liest mobil.
- **Ein File, keine Abhängigkeiten:** CSS und JS inline, keine CDN-Links, keine Build-Tools.
- **Dateinamen:** kleingeschrieben, mit Bindestrichen, sprechend (`checkliste-business-start.html`).
- **Session-Protokolle** in `outputs/` nach dem Muster `YYYY-MM-DD-session-[thema].md`.
- **Anleitungen für die Nutzerin** gehören nach `reference/`, nicht nach `outputs/` — `outputs/`
  ist öffentlich.

---

## 8. Deployment & Verkauf

- **Hosting:** Netlify (kostenloser Plan). `netlify.toml` liegt im Root, `outputs/` wird publiziert.
- **Live-Site:** `https://nischegenerator-mamas.netlify.app/` — einzelne Produkte darunter,
  z. B. `/checkliste-business-start.html`.
- **Verkauf:** Systeme.io — Funnel + Produkt + Bestellseite, Auslieferung per E-Mail mit dem
  Netlify-Link nach dem Kauf. Ablauf komplett in `reference/systeme-io-verkaufsseite.md` und
  `reference/anleitungen-deployment.md`.
- **Preisrahmen der Mini-Produkte:** 7 € (Impulskauf) bis 27 € (mit Zusatzmaterial).

---

## 9. Git-Workflow

- Default-Branch ist `main`.
- Arbeit passiert auf Feature-Branches nach dem Muster `claude/<thema>-<id>`, danach Pull Request
  gegen `main`.
- Commit-Messages sind kurz und beschreiben das Ergebnis (Deutsch oder Englisch, beides ist im
  Verlauf vorhanden) — z. B. „Add Business-Start Checkliste für Mamas mini product".
- **Niemals committen:** `.env`, API-Keys, echte Kundendaten. `.gitignore` deckt `.env*`,
  Editor- und OS-Dateien ab — verlass dich aber nicht blind darauf.

---

## 10. Wie sich Claude verhalten soll

- **Geduldig und einsteigerfreundlich** — Erkläre Dinge klar und verständlich, ohne Fachjargon vorauszusetzen
- **Strukturiert** — Gib immer einen klaren nächsten Schritt vor
- **Motivierend** — Feiere Erfolge und Fortschritte aktiv mit
- **Proaktiv** — Weise auf Optimierungspotenziale hin, bevor sie zu Problemen werden
- **Kontextbewusst** — Lade immer zuerst `profil/` und `context/`, bevor du mit Aufgaben beginnst.
  `profil/01_wer-bin-ich.md` ist aktuell die inhaltlich gefüllteste Quelle; die Dateien in
  `context/` sind noch weitgehend leere Templates — weise darauf hin, statt zu raten.
- **Auf Deutsch** — Kommuniziere standardmäßig auf Deutsch, es sei denn, ich wechsle die Sprache

---

## 11. Offene Baustellen

- `context/business-info.md`, `personal-info.md`, `strategy.md`, `current-data.md` sind noch
  Templates ohne Inhalt (außer den Branding-Farben). KPIs sind entsprechend nicht befüllt.
- `plans/` und `scripts/` sind leer — noch kein Plan über `/create-plan` erstellt.
- `index.html` / `nischengenerator.html` sind Duplikate und driften bereits leicht auseinander.
