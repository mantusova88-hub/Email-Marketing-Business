# Starter Kit: Automatisiertes Instagram Content-System

*Dieses Kit gibt dir ein vollautomatisches Content-System: Jede Woche werden Karussell-Entwuerfe generiert, und sobald du ein fertiges Design in einen Canva-Ordner legst, wird es automatisch auf Instagram gepostet.*

## Was du am Ende hast

1. Woechentlicher Content-Batch — Jeden Montag erstellt Claude automatisch 10 Karussell-Entwuerfe mit Hooks, Slides und Captions
2. Automatische Posting Queue — Design in Canva-Ordner legen → Caption wird generiert → Post wird fuer den naechsten Tag eingeplant → Design wird archiviert

## Voraussetzungen

- Claude Code (Max Plan empfohlen)
- Canva-Account (kostenlos reicht)
- Blotato-Account mit verbundenem Instagram (blotato.com)
- Canva MCP Server verbunden in Claude Code
- Blotato MCP Server verbunden in Claude Code

### MCP Server verbinden

In Claude Code: Einstellungen → MCP Servers → Canva und Blotato hinzufuegen. Falls du nicht weisst wie: Frage Claude Code "Wie verbinde ich den Canva MCP Server?"

## Teil 1: Brand Voice & Content-Vorlagen

Erstelle folgende Dateien in deinem Arbeitsordner. Diese sind die Grundlage fuer alles, was Claude fuer dich schreibt.

### Datei 1: brand-voice.md

Passe das an deine Stimme an:

```
# Brand Voice

## Tonalitaet
- Wie klingst du? [z.B. Direkt, motivierend, nahbar]
- Nicht: [z.B. Aufgeblasen, salesy, distanziert]

## Schreibregeln
- Direkte Ansprache: "du"
- Echte Umlaute: ae, oe, ue, ss
- [Weitere Regeln die zu dir passen]

## Kernbotschaft
[Was soll jeder Post implizit vermitteln?]

## Beispieltexte
[Fuege 2-3 echte Texte von dir ein, die deinen Stil zeigen]
```

### Datei 2: caption-formeln.md

Fuenf bewaehrte Caption-Strukturen:

```
## Formel 1: Provokante Behauptung + Beweis
[Starke Aussage mit Zahl]
Die meisten denken, das geht nicht. Geht es aber.
[1-2 Saetze Kontext]
[Punkt 1], [Punkt 2], [Punkt 3]
Das ist kein Zufall. Das ist System.
[CTA]

## Formel 2: Schritt-fuer-Schritt Anleitung
So [Ergebnis] in [Zeitraum]:
Schritt 1-5: [Aktionen]
Das ist alles. Kein Geheimnis, nur Umsetzung.

## Formel 3: Kontrast (Vorher / Nachher)
## Formel 4: Storytelling (kurz)
## Formel 5: Liste / Listicle

## CTA-Varianten
- Saves: "Speicher das, du wirst es brauchen."
- Kommentare: "Kommentiere [KEYWORD]"
- DM: "Schreib mir [KEYWORD]"
- Link in Bio / Shares / Folgen
```

### Datei 3: hook-framework.md

```
## Zahlen-Hooks
"Ich mache [Zahl] im Monat — mit [Detail]."

## Anleitungs-Hooks
"Die exakte [Strategie] hinter meinen [Ergebnis]:"

## Provokante Hooks
"Du brauchst keine [was alle denken]. Du brauchst [was hilft]."

## Neugier-Hooks
"Was ich an einem [Tag] mache, der spaeter [Ergebnis] bringt:"
```

## Teil 2: Canva-Ordner einrichten

Fuehre das in Claude Code aus:

```
Erstelle in meinem Canva-Account folgende Ordnerstruktur:
1. Einen Ordner "Instagram Karussells" (falls nicht vorhanden)
2. Darin einen Unterordner "Posting Queue"
3. Darin einen Unterordner "Gepostete Beitraege"

Gib mir die Ordner-IDs zurueck.
```

Notiere dir die drei Ordner-IDs — du brauchst sie im naechsten Schritt.

## Teil 3: Blotato Account-ID ermitteln

Fuehre in Claude Code aus:

```
Zeige mir meine verbundenen Blotato-Accounts.
```

Notiere dir die accountId fuer Instagram (z.B. "40962").

## Teil 4: Scheduled Task — Woechentlicher Content-Batch

Kopiere den folgenden Prompt und erstelle damit einen Scheduled Task in Claude Code. Passe die markierten Stellen an:

```
Erstelle einen Scheduled Task mit folgenden Einstellungen:
- Name: woechentliche-karussells
- Cron: Montag 07:00
- Modell: Sonnet
- Prompt:

Erstelle 10 Instagram-Karussell-Entwuerfe fuer diese Woche.

SCHREIBREGELN:
- Echte Umlaute
- Direkt, motivierend, nahbar
- Hook nicht in der Caption wiederholen
- Echter Mehrwert auf jeder Slide

Schritt 1: Kontext laden
- Lies brand-voice.md fuer meine Stimme
- Lies hook-framework.md fuer Hook-Regeln
- Lies caption-formeln.md fuer Caption-Strukturen

Schritt 2: Themen recherchieren
- Recherchiere ueber WebSearch nach aktuellen Trends in:
  [DEINE THEMEN, z.B. KI, Online-Business, digitale Produkte]

Schritt 3: 10 Karussells erstellen
Pro Karussell eine eigene Datei mit:
- Cover-Slide: Headline (Hook) + Subtext + "Swipe -->"
- Slide 2-6: Headline + Erklaerungstext mit echtem Mehrwert
- CTA-Slide: "Speicher dir das." + CTA
- Caption: Basierend auf caption-formeln.md + 5-10 Hashtags

Meine Zielgruppe: [DEINE ZIELGRUPPE BESCHREIBEN]
Kernbotschaft: [DEINE KERNBOTSCHAFT]
```

## Teil 5: Scheduled Task — Automatische Posting Queue

Dies ist der Task, der fertige Designs automatisch auf Instagram postet. Passe die markierten Stellen an:

```
Erstelle einen Scheduled Task mit folgenden Einstellungen:
- Name: instagram-posting-queue
- Cron: Taeglich 12:00
- Modell: Sonnet
- Prompt:

Du bist meine Instagram-Posting-Automatisierung.
Pruefe meinen Canva-Ordner "Posting Queue" und plane neue
Beitraege ueber Blotato ein.

1. Ordner pruefen
   list-folder-items mit folder_id [DEINE POSTING-QUEUE ORDNER-ID]
   Wenn leer: nichts tun, Session beenden.

2. Fuer jedes Design:
   a) Kommentare lesen (list-comments) = Caption
      Falls kein Kommentar: Slide-Texte lesen + KI-Caption
      generieren (Brand Voice + Caption-Formeln)
   b) Design als PNG exportieren (export-design)
   c) Post ueber Blotato einplanen:
      accountId: [DEINE BLOTATO INSTAGRAM ACCOUNT-ID]
      platform: instagram
      scheduledTime: Morgen 14:00 Uhr (ISO 8601 + Zeitzone)
   d) Design verschieben nach "Gepostete Beitraege"
      folder_id: [DEINE GEPOSTETE-BEITRAEGE ORDNER-ID]

Wichtig:
- Nur Designs, KEINE Unterordner
- Max 3 Posts pro Tag
- Bei Fehler: Design in Queue lassen + Fehler loggen
```

## Teil 6: Erster Testlauf

1. Erstelle ein Test-Karussell in Canva (oder nimm ein bestehendes)
2. Lege es in den Posting Queue Ordner
3. Optional: Fuege einen Kommentar auf dem Design hinzu mit deiner gewuenschten Caption
4. Gehe in Claude Code → Sidebar → Scheduled → instagram-posting-queue → Run now
5. Klicke alle Tool-Berechtigungen durch (Canva lesen, exportieren, Blotato posten)
6. Pruefe ob der Post in Blotato eingeplant wurde

Ab jetzt laeuft alles automatisch.

## So nutzt du das System im Alltag

| Wann | Was passiert |
|---|---|
| Montag | Claude generiert 10 Karussell-Entwuerfe |
| Unter der Woche | Du setzt die besten Entwuerfe in Canva um |
| Wenn fertig | Design in "Posting Queue" legen, optional Caption als Kommentar |
| Taeglich 12:00 | Claude prueft die Queue, generiert Caption falls noetig, plant Post fuer morgen 14:00 ein |
| Nach dem Posten | Design wird automatisch in "Gepostete Beitraege" archiviert |

## Haeufige Probleme

| Problem | Loesung |
|---|---|
| Task laeuft nicht | Beim ersten Mal "Run now" klicken fuer Tool-Berechtigungen |
| Caption klingt nicht nach mir | Brand Voice in brand-voice.md anpassen, mehr Beispieltexte hinzufuegen |
| Falscher Instagram-Account | Account-ID in Blotato pruefen (blotato_list_accounts) |
| Design wird nicht erkannt | Pruefen ob es im richtigen Ordner liegt (Posting Queue, nicht uebergeordnet) |
| Zu viele/wenige Hashtags | Im Task-Prompt die Anzahl anpassen |

## Kosten

| Service | Kosten |
|---|---|
| Claude Code (Max Plan) | $100-200/Monat |
| Canva | Kostenlos (Free Plan reicht) |
| Blotato | Ab $0/Monat (Free Plan fuer 1 Plattform) |
| Gesamt | ~$100-200/Monat |

*Zum Vergleich: Ein Social Media Manager kostet 500-2.000€/Monat fuer denselben Output.*
