# Prompts für KI-Tools

## Zum Testen (Artifact in Claude.ai)

Baue mir ein interaktives, voll funktionsfähiges HTML-Tool als Artifact (rechts anzeigen).

```
## Was das Tool tun soll:
[BESCHREIBE HIER DEIN TOOL – z.B. "Der Nutzer gibt eine Branche ein und
bekommt 5 Tool-Ideen die er für seine Kunden bauen kann"]

## Design:
- Hintergrundfarbe: [HEX z.B. #e98b9e]
- Akzentfarbe: [HEX z.B. #950032]
- Button-Farbe: [HEX z.B. #950032]
- Schriftart Überschrift: Playfair Display (serif, von Google Fonts)
- Schriftart Fließtext: DM Sans (von Google Fonts)
- Überschrift und Unterüberschrift zentriert, gleiche Positionierung wie
  beim Heading-Bereich
- Input-Bereich: dunkler, leicht transparenter Hintergrund
  (z.B. rgba(30,0,12,0.55)) mit weißer Schrift für guten Kontrast ohne
  zu hartem Bruch
- Result-Cards: leicht transparenter Hintergrund, passend zur Gesamtpalette

## Technische Anforderungen – KRITISCH, alle Punkte einhalten:
1. API-Call direkt im HTML – rufe https://api.anthropic.com/v1/messages auf.
   KEIN x-api-key Header – Claude.ai übernimmt die Authentifizierung
   automatisch im Artifact-Kontext.
2. Kein web_search Tool – das verursacht einen "Failed to fetch" Fehler im
   Artifact. Nutze ausschließlich Claudes eigenes Wissen.
3. Model: claude-sonnet-4-6, max_tokens: 3000
4. Retry-Logik – fange HTTP 529 und 503 (API überlastet) ab und versuche es
   automatisch bis zu 3x mit 2,5 Sekunden Pause. Zeige dem Nutzer
   "Versuch 2/3…" im Ladetext.
5. JSON-Antwort – der System-Prompt soll Claude anweisen, NUR ein valides
   JSON-Array zurückzugeben, kein Markdown, keine Backticks, kein Text
   davor oder danach. Parse mit .match(/\[[\s\S]*\]/) um JSON sicher zu
   extrahieren.
6. Error Handling – zeige Fehlermeldungen immer als lesbaren deutschen Text
   an, nie den rohen API-Response.
7. Enter-Key – Eingabefeld soll bei Enter absenden.
8. Reset-Button – nach dem Ergebnis soll ein "← Zurück" Button erscheinen
   der alles zurücksetzt.
9. Animationen – Ergebnis-Cards mit animation-delay gestaffelt einblenden
   (fadeUp).
10. Keine Netlify Function, kein Backend – alles läuft im Frontend. Das
    Artifact ist zum direkten Testen hier in Claude.ai.

## Output-Format der KI-Antwort:
[BESCHREIBE WIE DIE ERGEBNISSE AUSSEHEN SOLLEN – z.B. JSON-Array mit
Feldern: name, beschreibung, zielgruppe, marktpotenzial, monetarisierung,
schwierigkeit]

## Wichtig:
- Zeige das fertige Tool sofort als HTML-Artifact an (rechts im Panel)
- Kein Netlify, kein ZIP, kein separater Code – direkt testbar
- Alle Texte auf Deutsch
```

## ZIP-Datei (deploybares Netlify-Projekt)

Baue mir ein vollständiges, sofort deployable Netlify-Projekt als ZIP-Datei.

```
Was das Tool tun soll:
[BESCHREIBE HIER DEIN TOOL]

Design:
- Hintergrundfarbe: [HEX]
- Akzentfarbe: [HEX]
- Button-Farbe: [HEX]
- Schriftart Überschrift: Playfair Display (serif, Google Fonts)
- Schriftart Fließtext: DM Sans (Google Fonts)
- Input-Bereich: solider dunkler Hintergrund (z.B. #6b0028) mit weißer Schrift
- Result-Cards: leicht transparenter Hintergrund passend zur Palette

Technische Anforderungen – KRITISCH, jeden Punkt einhalten:

Dateistruktur der ZIP (genau so, nicht anders):
index.html
netlify.toml
netlify/
└── functions/
    └── claude.js

⚠️ WICHTIG ZIP-STRUKTUR: Die Dateien müssen direkt im Root der ZIP liegen –
KEIN übergeordneter Unterordner. Beim Erstellen der ZIP immer cd in den
Projektordner und dann `zip -r ../mein-tool.zip .` ausführen – niemals
`zip -r mein-tool.zip mein-tool/`. Netlify erwartet index.html direkt im
ZIP-Root, sonst erscheint „Page not found".

netlify.toml (exakt so):
[build]
  functions = "netlify/functions"
  publish = "."

netlify/functions/claude.js – KRITISCHE REGELN:
1. Lies den API Key aus process.env.ANTHROPIC_API_KEY – niemals hardcoden
2. Setze in JEDEM Response-Objekt (auch OPTIONS, Fehler, Erfolg) den Header
   "Content-Type": "application/json" → Fehlt dieser Header, gibt Netlify
   HTML zurück statt JSON → „Unexpected token < is not valid JSON"
3. KEIN web_search Tool verwenden → verursacht 504 Timeout
   (Netlify limit: 10 Sek.)
4. Nutze model: "claude-sonnet-4-6", max_tokens: 2000
5. System-Prompt soll Claude anweisen, NUR ein valides JSON-Array
   zurückzugeben
6. Parse Antwort mit .match(/\[[\s\S]*\]/) um JSON sicher zu extrahieren
7. Gib bei Fehlern immer { error: "lesbarer Text" } zurück – niemals rohen
   API-Response

index.html – KRITISCHE REGELN:
1. Rufe NUR /.netlify/functions/claude auf – NIEMALS api.anthropic.com
   direkt → Direkter API-Call funktioniert nicht im Browser (CORS) →
   „Failed to fetch"
2. Kein x-api-key Header im Frontend – der Key gehört nur in die Function
3. Fange HTTP 504 explizit ab mit: „Server Timeout – bitte nochmal versuchen"
4. Fange HTTP 529/503 ab mit Retry-Logik: max 3 Versuche, 2,5 Sek. Pause,
   zeige „Versuch 2/3…"
5. Zeige alle Fehlermeldungen auf Deutsch als lesbaren Text – niemals
   rohen HTML oder JSON
6. Enter-Key im Inputfeld löst Submit aus
7. Reset-Button nach Ergebnis der alles zurücksetzt
8. Result-Cards mit gestaffeltem animation-delay einblenden (fadeUp)

Output-Format der KI-Antwort:
[BESCHREIBE DEIN JSON-FORMAT – z.B.:
[{"nummer":1,"name":"...","beschreibung":"...","zielgruppe":"...",
"marktpotenzial":"...","monetarisierung":"...",
"schwierigkeit":"Einfach|Mittel|Komplex"}] ]

Wichtig:
- Erstelle eine saubere ZIP mit Dateien direkt im Root (kein Unterordner!)
- Verifiziere die ZIP-Struktur nach dem Erstellen mit `unzip -l mein-tool.zip`
  – index.html muss in der ersten Ebene erscheinen, nicht als
  mein-tool/index.html
- Teste die Logik gedanklich durch: Browser → index.html →
  /.netlify/functions/claude → Anthropic API → JSON zurück → Cards rendern
- Alle Texte auf Deutsch
- Kein node_modules, kein package.json nötig – Netlify Functions brauchen
  das nicht für einfache fetch-Calls
```
