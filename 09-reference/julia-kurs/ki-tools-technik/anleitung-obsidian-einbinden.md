# Anleitung: Obsidian einbinden

*Wie du dein Claude-Code-System mit Obsidian sichtbar und bedienbar machst*

## Warum Obsidian und Claude Code zusammen Sinn machen

Claude Code arbeitet die ganze Zeit mit Dateien auf deinem Rechner — Markdown-Dateien, Notizen, Logs, Pläne. Das Problem: ohne ein zweites Tool siehst du diese Dateien nur, wenn du den Claude-Chat offen hast. Du hast keinen Überblick, du kannst nichts nachschlagen, du kannst keine Verbindungen ziehen.

Genau hier kommt Obsidian rein. Obsidian ist eine kostenlose Notiz-App, die direkt mit deinen Markdown-Dateien arbeitet. Du öffnest einfach deinen Claude-Code-Ordner als Vault — und ab dem Moment siehst du alles, was Claude für dich anlegt, in einer richtig schönen, durchsuchbaren Oberfläche. Mit Wikilinks, Tags, Graph-View und allem drum und dran.

### Was du dadurch gewinnst

- Du siehst dein komplettes System auch ohne Claude — alle Notizen, Pläne, Daily Logs, Projekte
- Du kannst durchsuchen, querverlinken, Tags setzen — Claude versteht und nutzt diese Links automatisch
- Du kannst auf dem Handy von unterwegs reinschauen und Notizen ergänzen, die Claude beim nächsten Mal liest
- Dein zweites Gehirn und dein KI-Assistent arbeiten am selben Datenbestand — keine Doppelablagen, keine Inkonsistenzen
- Wenn Claude einen Plan schreibt, kannst du ihn in Obsidian lesen, kommentieren, verschieben — und Claude findet ihn beim nächsten Mal trotzdem wieder
- Volle Datensouveränität: alles liegt als ganz normale .md-Datei auf deiner Festplatte, nichts in einer fremden Cloud

### Wichtig zu verstehen

Obsidian erstellt keine eigene Datenbank. Es liest die Markdown-Dateien, die in deinem Ordner liegen. Das heißt: Obsidian und Claude Code teilen sich denselben Ordner, sie schreiben in dieselben Dateien. Das ist genau der Trick — beide Tools sehen dasselbe.

## Voraussetzungen

- Ein bestehender Claude-Code-Workspace auf deinem Rechner (z.B. unter `~/Desktop/Claude Code/`)
- Mac, Windows oder Linux — Obsidian läuft überall
- Optional: iCloud, Dropbox oder Obsidian Sync, falls du auch vom Handy zugreifen willst

## Phase 1: Obsidian installieren (3 Minuten)

1. Gehe auf obsidian.md und lade die kostenlose Version für dein Betriebssystem herunter
2. Installiere Obsidian wie jedes andere Programm — Doppelklick, weiter, fertig
3. Öffne Obsidian. Beim ersten Start fragt es dich nach einem Vault — das machen wir im nächsten Schritt

## Phase 2: Deinen Claude-Code-Ordner als Vault öffnen (2 Minuten)

Ein Vault in Obsidian ist nichts anderes als ein Ordner. Wir öffnen einfach deinen bestehenden Claude-Code-Ordner — Obsidian macht aus dem, was schon da ist, automatisch deinen Wissensspeicher.

1. Klicke auf "Open folder as vault" (auf Deutsch: "Ordner als Vault öffnen")
2. Navigiere zu deinem Claude-Code-Ordner, z.B. `/Users/deinname/Desktop/Claude Code/`
3. Bestätige. Obsidian fragt einmal, ob es Plugins erlauben darf — sag ja
4. In der linken Seitenleiste siehst du jetzt deine komplette Ordnerstruktur

## Phase 3: Ordnerstruktur verstehen

Wenn du mit der Standard-Vorlage arbeitest, hast du diese Ordner — und Obsidian zeigt sie dir alle als saubere Hierarchie:

- `00-inbox/` — alles was schnell reinflattert, wird später sortiert
- `01-context/` — wer du bist, dein Business, dein Team
- `02-brand/` — deine Brand-Voice und Stil-Regeln
- `03-strategy/` — Prioritäten, offene Loops, strategische Themen
- `04-projects/` — laufende Projekte, jedes mit eigenem Unterordner
- `05-daily/` — tägliche Logs nach Datum
- `06-team/` — Team und Content Dashboard
- `07-intelligence/` — Entscheidungen, Meetings, Pläne
- `08-resources/` — Templates, Frameworks, Anleitungen
- `09-reference/` — Archiv

Du musst dir das nicht merken. Wichtig ist nur: du arbeitest immer im selben Ordner, egal ob über Claude oder direkt in Obsidian.

## Phase 4: Die wichtigsten Einstellungen (5 Minuten)

Obsidian funktioniert direkt nach der Installation. Aber drei Einstellungen lohnen sich, damit es sauber mit Claude zusammenarbeitet.

### Wikilinks aktivieren

Wikilinks sind die eckigen Klammern: `[[dateiname]]`. Sie verlinken zwischen Notizen — und Claude versteht und benutzt dieses Format selbst.

1. Settings → Files & Links
2. "Use [[Wikilinks]]" auf An stellen
3. "New link format" auf "Shortest path when possible"

### Standard-Speicherorte festlegen

Damit Claude und du an denselben Stellen schreiben:

1. Settings → Files & Links
2. "Default location for new notes" auf "Same folder as current file"
3. "Default location for new attachments" auf einen festen Ordner, z.B. `08-resources/attachments/`

### Auto-Save aktivieren

Standardmäßig speichert Obsidian automatisch — kontrolliere kurz, dass das so eingestellt ist, dann verlierst du nie etwas.

## Phase 5: Empfohlene Plugins (optional, 5 Minuten)

Obsidian hat hunderte Plugins. Du brauchst die wenigsten. Diese drei sind in der Praxis aber Gold wert:

### Calendar

Zeigt dir einen Kalender in der Seitenleiste. Klick auf ein Datum — und du landest direkt im Daily Log dieses Tages. Perfekt mit dem `05-daily/`-Ordner.

Installation: Settings → Community plugins → Browse → "Calendar" suchen → Install + Enable.

### Templater

Damit kannst du Vorlagen für neue Notizen anlegen, z.B. eine Daily-Log-Vorlage, die automatisch Datum und Struktur einsetzt.

Installation: Settings → Community plugins → Browse → "Templater" → Install + Enable.

### Dataview

Lässt dich deine Notizen wie eine Datenbank abfragen. Z.B. "alle Projekte mit Status offen" oder "alle Daily Logs der letzten Woche" als automatische Tabelle.

Installation: Settings → Community plugins → Browse → "Dataview" → Install + Enable.

Wenn du gerade erst anfängst: lass die Plugins erstmal weg. Du kannst sie jederzeit später nachinstallieren.

## Phase 6: Mobile (optional)

Wenn du auch unterwegs etwas reinschreiben willst, hast du zwei einfache Wege:

### Obsidian Sync (für alle Plattformen, kostenpflichtig)

Obsidian bietet einen eigenen Sync-Service an, ca. 4 € pro Monat. End-to-End verschlüsselt, läuft überall, keine Drittanbieter nötig.

Settings → Sync → Account anlegen → Vault aktivieren. Auf dem Handy denselben Account einloggen, fertig.

## Phase 7: Wie du im Alltag damit arbeitest

Jetzt der wichtigste Teil — wie sieht das im echten Leben aus?

- Du startest deinen Tag in Obsidian, öffnest dein Daily Log und schreibst rein, was ansteht
- Claude öffnest du, wenn du etwas umsetzen willst — Claude liest dein Daily Log automatisch und weiß, woran du arbeitest
- Wenn Claude einen Plan, ein Skript oder eine Notiz schreibt, landet sie als .md-Datei im Vault — du siehst sie sofort in Obsidian
- Du kannst die Datei in Obsidian umbenennen, verschieben, kommentieren — Claude akzeptiert das alles und nutzt die neuen Pfade weiter
- Wikilinks setzt du mit doppelten eckigen Klammern. Wenn du z.B. in einem Plan auf `[[brand-voice]]` verlinkst, kann Claude direkt nachschlagen, was deine Brand-Voice ist
- Auf dem Handy: kurze Idee notieren in `00-inbox/`, später am Rechner mit Claude verarbeiten

### Beispiel-Workflow

So sieht ein typischer Tag aus:

1. Morgens auf dem Handy in Obsidian: "Idee für neuen Reel: 3 Fehler beim Launch" — in `00-inbox/` als Notiz
2. Mittags am Rechner: Claude öffnen, sagen "verarbeite die Inbox" — Claude liest die Notiz, schlägt einen Reel-Aufbau vor und legt ihn in `04-projects/` ab
3. Abends: in Obsidian kurz drüberlesen, kleine Korrekturen direkt machen, fertig

Du wechselst die ganze Zeit zwischen den beiden Tools, aber du arbeitest immer am selben Datenbestand. Das ist der Punkt.

## Tipps aus der Praxis

- Lege dir mit Cmd+P die Befehlspalette an, dann findest du jede Aktion über die Tastatur
- Cmd+O öffnet den Datei-Schnellzugriff — schneller als jede Suche
- Mit Cmd+Klick auf einen Wikilink öffnest du die Datei in einem neuen Tab — perfekt zum parallelen Lesen
- Schalte den Graph-View einmal ein (linkes Icon) — du siehst dein komplettes System als Netzwerk
- Alles was Claude im Vault ändert, kannst du in Obsidian sofort sehen — auch live, während Claude arbeitet
- Nie gleichzeitig in Obsidian und Claude an derselben Datei schreiben — die Änderungen können sich gegenseitig überschreiben. Wenn Claude eine Datei bearbeitet, wartest du kurz, bis er fertig ist

## Backup über Git (empfohlen)

Wenn du nichts verlieren willst, leg deinen Vault als privates Git-Repo an. Klingt technisch, ist aber kostenlos und einmalig in 10 Minuten erledigt.

1. Auf github.com ein neues privates Repository anlegen
2. Im Terminal in deinen Claude-Code-Ordner gehen

```
git init
git remote add origin https://github.com/dein-name/dein-repo.git
git add . && git commit -m "erstes commit" && git push -u origin main
```

3. Optional: Plugin "Obsidian Git" installieren — pusht dann automatisch alle 5 Minuten in dein Repo

Damit hast du eine vollständige Versionierung. Du kannst jederzeit zurückspringen, falls du etwas ausversehen löschst.

## Troubleshooting

- Obsidian zeigt nicht alle Dateien — Settings → Files & Links → "Detect all file extensions" aktivieren
- Wikilinks funktionieren nicht — prüfe in Settings → Files & Links, dass Wikilinks aktiviert sind
- Doppelte Dateien nach iCloud-Sync — passiert manchmal bei zeitgleichem Bearbeiten. Lösung: kurz warten bis iCloud durch ist, dann eine Version löschen
- Claude findet eine Datei nicht, die du in Obsidian umbenannt hast — sag Claude einfach den neuen Namen, er findet sie

## Checkliste

- [ ] Obsidian von obsidian.md heruntergeladen und installiert
- [ ] Claude-Code-Ordner als Vault geöffnet
- [ ] Wikilinks aktiviert
- [ ] Default-Speicherorte gesetzt
- [ ] Mindestens das Calendar-Plugin installiert (optional)
- [ ] Mobile-Variante eingerichtet (optional)
- [ ] Git-Backup eingerichtet (optional, aber empfohlen)
- [ ] Ersten Wikilink getestet (z.B. `[[brand-voice]]` in einer Notiz)

*Wenn du diese Schritte einmal durch hast, hast du ein System, das wirklich rund läuft: Claude als Assistent, Obsidian als dein zweites Gehirn — beide arbeiten am selben Datenbestand, und du verlierst nie wieder den Überblick.*
