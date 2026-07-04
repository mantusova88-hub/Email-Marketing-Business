# So baust du dein eigenes KI-Tool mit Claude (Hook Generator/Salespage Generator)

*Schritt-fuer-Schritt-Anleitung: Vom Konzept zum fertigen Tool — am Beispiel eines KI Hook Generators.*

Von Julia Trost | Stand: April 2026

## Inhaltsverzeichnis

1. Teil 1: Die Idee — Was soll dein Tool koennen?
2. Teil 2: Das Framework — Dein Wissen als KI-Anweisung
3. Teil 3: Das Frontend — Was der Nutzer sieht
4. Teil 4: Das Backend — Die sichere Verbindung zur KI
5. Teil 5: Online stellen — Dein Tool live auf Netlify
6. Teil 6: Testen und Optimieren
7. Teil 7: In deinen Kurs einbauen
8. Teil 8: Weitere Tool-Ideen fuer dein Business
9. Glossar — Alle Fachbegriffe einfach erklaert

## Ueberblick: Was bauen wir hier eigentlich?

In dieser Anleitung lernst du, wie du ein KI-Tool baust, das du in deinen Online-Kurs einbauen oder als eigenstaendiges Produkt verkaufen kannst.

Das fertige Tool besteht aus drei Teilen:

| Teil | Was ist das? | Alltagsvergleich |
|---|---|---|
| Frontend | Die Oberflaeche die der Nutzer sieht | Das Schaufenster eines Ladens |
| Backend | Die Logik die im Hintergrund laeuft | Die Kueche in einem Restaurant |
| KI-Prompt | Die Anweisung an die KI | Das Rezept fuer den Koch |

So funktioniert es aus Sicht des Nutzers:

1. Nutzer oeffnet dein Tool (eine Webseite).
2. Nutzer gibt Informationen ein (z.B. Nische, Thema, Erfahrung).
3. Nutzer klickt auf "Generieren".
4. Im Hintergrund schickt dein Tool die Eingaben an die KI (Claude API).
5. Die KI generiert Ergebnisse basierend auf DEINEM Framework.
6. Die Ergebnisse werden dem Nutzer schoen aufbereitet angezeigt.

*Der Clou: Die KI arbeitet nach DEINEN Regeln und DEINER Methode. Du verpackst dein Expertenwissen in ein KI-Prompt — und die KI liefert Ergebnisse so, wie du es deinen Kunden beibringen wuerdest.*

## Teil 1: Die Idee — Was soll dein Tool koennen?

Bevor du irgendetwas baust, musst du drei Fragen beantworten:

### Frage 1: Welches Problem loest dein Tool?

Das Tool muss ein konkretes, wiederkehrendes Problem deiner Zielgruppe loesen. Je spezifischer, desto besser.

| Zu vage | Gut spezifisch |
|---|---|
| "Hilft beim Content erstellen" | "Generiert 5 fertige Instagram-Hooks zu deinem Thema" |
| "Schreibt Texte" | "Schreibt eine 5-teilige E-Mail-Sequenz fuer dein Webinar" |
| "KI-Assistent" | "Beantwortet Kundenfragen basierend auf deinem Kurs-Inhalt" |

### Frage 2: Was gibt der Nutzer ein?

Definiere die Eingabefelder. Weniger ist mehr — der Nutzer soll nicht ueberfordert werden.

Beispiel Hook Generator:
- **Nische:** "In welcher Branche bist du?" (z.B. Fitness, Finanzen, Business)
- **Thema:** "Worueber soll der Post sein?" (z.B. Minikurs erstellen)
- **Persoenliche Erfahrung:** "Was hast du selbst erlebt?" (z.B. "Ich habe damit 10k gemacht")

TIPP: Starte mit maximal 3 Eingabefeldern. Du kannst spaeter immer noch welche hinzufuegen.

### Frage 3: Was bekommt der Nutzer zurueck?

Definiere das Ergebnis. Es muss sofort nutzbar sein — der Nutzer soll es kopieren und verwenden koennen.

Beispiel Hook Generator:
- 5 fertige Hooks
- Fuer jeden Hook: eine Erklaerung warum er funktioniert
- Kategorisiert nach Typ (Zahlen, Storytelling, Provokant, etc.)

## Teil 2: Das Framework — Dein Wissen als KI-Anweisung

Das ist das Herzstueck deines Tools. Hier verpackst du dein Expertenwissen in eine Anweisung, die der KI genau sagt, wie sie arbeiten soll.

Dieses Framework heisst "System-Prompt" — es ist wie ein Briefing fuer einen Mitarbeiter, der genau weiss, was er tun soll, bevor der Kunde ueberhaupt etwas sagt.

### Was gehoert in dein Framework?

**1. Wer bist du? (Kontext fuer die KI)**

Erklaere der KI, in welcher Rolle sie antwortet.

> "Du bist ein Content-Experte, spezialisiert auf Instagram-Hooks fuer Online-Unternehmer. Du arbeitest nach dem bewährten Framework von [dein Name]."

**2. Was sind die Regeln? (Dos und Don'ts)**

Je klarer die Regeln, desto besser die Ergebnisse.

```
REGELN:
- Hooks muessen in den ersten 3 Sekunden packen
- Maximal 2 Saetze pro Hook
- Verwende konkrete Zahlen wenn moeglich
- NIEMALS mit einer Frage anfangen
- NIEMALS "Hier ist..." oder "Warum ich..." verwenden
- Sprache: direkt, selbstbewusst, kein Weichspueler
```

**3. Welche Typen/Kategorien gibt es?**

Wenn deine Methode verschiedene Typen hat, erklaere sie.

```
HOOK-TYPEN:
1. Zahlen-Hook: "100.000€ im Monat mit einem Kurs."
2. Kontrast-Hook: "Alle sagen X. Ich mache Y."
3. Story-Hook: "2021: 0€. 2026: 100k/Monat."
4. Provokant-Hook: "Dein Kurs bringt kein Geld? Hier ist warum."
5. Kurz-Hook: Maximal 8 Woerter, wie eine Schlagzeile.
```

**4. Beispiele! (Das Wichtigste)**

Gib der KI konkrete Beispiele fuer gute UND schlechte Ergebnisse.

GUTES BEISPIEL: "1.000 Menschen kaufen jeden Monat meinen 100€-Kurs. Das sind 100.000€. Automatisch."

SCHLECHTES BEISPIEL: "Hier sind meine besten Tipps fuer Online-Marketing" → Zu generisch, kein Interesse, kein Mehrwert.

**5. Output-Format definieren**

Sag der KI genau, wie das Ergebnis aussehen soll.

```
AUSGABE-FORMAT (als JSON):
{
  "hooks": [
    {
      "text": "Der Hook-Text",
      "type": "Zahlen-Hook",
      "why": "Warum dieser Hook funktioniert"
    }
  ]
}
```

**WICHTIG:** Das Framework ist der wichtigste Teil deines Tools! Nimm dir genuegend Zeit dafuer. Ein mittelmaeßiges Framework = mittelmaeßige Ergebnisse. Ein starkes Framework = Ergebnisse, die deine Kunden begeistern.

**TIPP:** Nutze deine bestehenden Inhalte! Wenn du Transkripte, Kursmaterial, Blogartikel oder Instagram-Posts hast, in denen du deine Methode erklärst — gib sie Claude Code und sag: "Erstelle aus diesen Materialien ein detailliertes System-Prompt fuer ein KI-Tool, das Hooks generiert." Claude Code extrahiert dein Wissen und formuliert es als Prompt.

## Teil 3: Das Frontend — Was der Nutzer sieht

Das Frontend ist die Oberflaeche deines Tools — das, was der Nutzer sieht und bedient. Es besteht aus drei Dateien:

| Datei | Wofuer | Vergleich |
|---|---|---|
| index.html | Struktur der Seite (Texte, Felder, Buttons) | Der Grundriss eines Hauses |
| style.css | Design (Farben, Schriften, Layout) | Die Inneneinrichtung |
| script.js | Funktionen (was passiert beim Klicken) | Die Haustechnik (Licht, Heizung) |

Du musst diese Dateien NICHT selbst schreiben! Das macht Claude Code fuer dich.

### So laesst du das Frontend bauen

Gib Claude Code folgende Anweisung (angepasst an dein Tool):

> "Erstelle mir ein Frontend fuer mein Hook-Generator-Tool. Der Nutzer soll folgende Felder ausfuellen koennen: Nische (Dropdown mit 10 Optionen), Thema (Textfeld), persoenliche Erfahrung (optionales Textfeld). Es soll einen Button geben 'Hooks generieren'. Die Ergebnisse sollen als Karten angezeigt werden, jeweils mit Hook-Text, Typ-Badge und einer aufklappbaren Erklaerung. Brand-Farben: Hintergrund #100012, Akzent #e98b9e, Buttons #950032. Schrift: modern, clean."

Was Claude Code dann macht:
- Erstellt alle drei Dateien (HTML, CSS, JavaScript)
- Baut die Eingabefelder, Buttons und Ergebnis-Anzeige
- Wendet deine Brand-Farben an
- Macht das Tool mobilfreundlich (responsive)

TIPP: Beschreibe auch, was du NICHT willst: "Kein ueberladenes Design, keine Animationen, keine Cookie-Banner. Halte es einfach und clean."

### Aenderungen sind einfach

- "Mach den Button groesser und aendere den Text zu 'Jetzt Hooks erstellen'"
- "Fuege einen zweiten Tab hinzu fuer Marktrecherche"
- "Die Karten sollen einen Schatten haben"
- "Fuege unten einen Hinweis hinzu: 'Powered by [dein Name]'"

## Teil 4: Das Backend — Die sichere Verbindung zur KI

Jetzt wird es kurz etwas technischer — aber keine Sorge, Claude Code macht die Arbeit.

### Warum brauche ich ein Backend?

Dein Tool muss mit der KI (Claude API) kommunizieren. Dafuer braucht es einen API-Key — das ist wie ein Passwort fuer den KI-Dienst.

**WICHTIG:** Der API-Key darf NIEMALS im Frontend stehen! Wenn er dort sichtbar waere, koennte jeder ihn kopieren und auf deine Kosten die KI nutzen. Deshalb brauchen wir ein Backend.

Was das Backend macht:
1. Empfaengt die Eingaben vom Nutzer (aus dem Frontend).
2. Fuegt deinen API-Key hinzu (sicher, unsichtbar).
3. Schickt alles an die Claude API (zusammen mit deinem Framework/System-Prompt).
4. Empfaengt die Antwort von der KI.
5. Schickt die Antwort zurueck ans Frontend.

*Vergleich: Das Backend ist wie ein Kellner im Restaurant. Der Gast (Nutzer) gibt seine Bestellung (Eingaben) ab. Der Kellner (Backend) bringt sie in die Kueche (Claude API), wo das Essen (Ergebnis) zubereitet wird. Der Kellner bringt es zurueck — der Gast sieht die Kueche nie.*

### So laesst du das Backend bauen

Wir nutzen Netlify Functions — das ist ein kostenloser Service, der dein Backend hostet.

Gib Claude Code folgende Anweisung:

> "Erstelle eine Netlify Function (netlify/functions/claude.js), die Anfragen vom Frontend entgegennimmt, den API-Key aus den Umgebungsvariablen liest (ANTHROPIC_API_KEY), die Anfrage an die Claude API schickt (mit meinem System-Prompt), und die Antwort zurueckgibt. Verwende das Modell claude-sonnet-4-6."

Claude Code erstellt dann:
- **netlify/functions/claude.js** — Die Backend-Funktion
- **netlify.toml** — Die Konfigurationsdatei fuer Netlify

In der Backend-Funktion ist auch dein System-Prompt eingebaut — also dein komplettes Framework aus Teil 2.

## Teil 5: Online stellen — Dein Tool live auf Netlify

Netlify ist ein kostenloser Hosting-Service. Du lädst deinen Ordner hoch und bekommst eine URL — fertig, dein Tool ist live.

### Schritt fuer Schritt

1. Gehe auf netlify.com und erstelle einen kostenlosen Account.
2. Klicke auf "Add new site" → "Deploy manually".
3. Ziehe deinen Tool-Ordner per Drag & Drop in das Upload-Feld.
4. Warte ca. 30 Sekunden — Netlify stellt dein Tool online.
5. Du bekommst eine URL (z.B. mein-hook-tool.netlify.app).

### API-Key sicher eintragen

1. In Netlify: Gehe zu "Site configuration" → "Environment variables".
2. Klicke auf "Add a variable".
3. Name: `ANTHROPIC_API_KEY`
4. Wert: Dein API-Key von console.anthropic.com
5. Speichern und neu deployen ("Deploys" → "Trigger deploy").

**WICHTIG:** Gib deinen API-Key NUR in den Netlify-Umgebungsvariablen ein — niemals direkt in den Code schreiben!

### In deinen Kurs einbauen

Du kannst dein Tool als iFrame in jede Kursplattform einbetten:

```html
<iframe
  src="https://dein-tool.netlify.app"
  width="100%"
  height="800"
  frameborder="0">
</iframe>
```

Oder einfach den Link teilen — der Nutzer oeffnet das Tool im Browser.

TIPP: Du kannst auch eine eigene Domain verbinden (z.B. tool.juliatrost.de). Das geht in Netlify unter "Domain management".

## Teil 6: Testen und Optimieren

Dein Tool ist live — jetzt geht die eigentliche Arbeit los. Die ersten Ergebnisse sind selten perfekt. Das Optimieren macht den Unterschied.

### Was du testen solltest

1. Teste verschiedene Eingaben (unterschiedliche Nischen, Themen, Erfahrungen).
2. Pruefe: Klingen die Ergebnisse wie DU? Oder wie generisches ChatGPT?
3. Teste auf dem Handy — sieht alles gut aus?
4. Lass 2-3 andere Personen testen und frag nach Feedback.

### Typische Optimierungen

| Problem | Loesung |
|---|---|
| Ergebnisse klingen zu generisch | Mehr Beispiele ins Framework einbauen |
| KI ignoriert deine Regeln | Regeln fett markieren und wiederholen im Prompt |
| Ergebnisse kommen nicht an | JSON-Format pruefen, robusteres Parsing einbauen |
| Hooks sind zu lang | Maximale Wortanzahl im Framework definieren |
| Nutzer versteht Eingabefelder nicht | Platzhalter-Texte und Beispiele hinzufuegen |
| Zu viele Eingabefelder | Auf das Wesentliche reduzieren (max. 3) |

So optimierst du das Framework: Gib Claude Code echte Beispiele von schlechten Outputs:

> "Wenn ich 'Fitness' als Nische und 'Abnehmen' als Thema eingebe, kommt dieser Hook: 'Hier sind 5 Tipps zum Abnehmen'. Das ist schlecht — es soll provokanter und mit Zahlen sein. Passe das System-Prompt an, sodass die KI solche generischen Hooks vermeidet."

TIPP: Plane 2-3 Optimierungsrunden ein. Jede Runde machst du die Ergebnisse ein Stueck besser. Nach 3 Runden ist das Tool meistens richtig gut.

## Teil 7: In deinen Kurs einbauen

Dein KI-Tool ist ein enormer Mehrwert fuer deinen Kurs — es macht deine Methode fuer Kunden sofort anwendbar.

### Positionierung im Kurs

| Position | Warum | Beispiel |
|---|---|---|
| Am Anfang | Sofortiger Aha-Moment, Kunde sieht sofort Ergebnisse | "Probier es aus: Gib deine Nische ein und sieh, was rauskommt" |
| Nach der Theorie | Kunde kann das Gelernte sofort anwenden | "Du kennst jetzt die 5 Hook-Typen — lass sie dir generieren" |
| Als Bonus | Exklusiver Mehrwert, den es nur bei dir gibt | "Dein exklusives Tool — unbegrenzt nutzbar" |

### Wie du das Tool praesentierst

- **Nicht:** "Hier ist ein KI-Tool."
- **Sondern:** "Ich habe mein komplettes Hook-Framework in dieses Tool eingebaut. Es generiert Hooks genau so, wie ich es dir beibringe — nur in Sekunden statt Stunden."

### Wichtig fuer die Kommunikation

- Das Tool ersetzt den Kurs nicht — es ergaenzt ihn.
- Der Kurs bringt das Verstaendnis, das Tool die Umsetzung.
- Betone, dass DEIN Framework dahintersteckt — nicht "irgendeine KI".
- Kunden sollen verstehen: Die Qualitaet kommt von deiner Methode, nicht vom Tool.

## Teil 8: Weitere Tool-Ideen fuer dein Business

Der Hook Generator ist nur der Anfang. Das gleiche Prinzip funktioniert fuer viele andere Tools:

| Tool | Was es macht | Eingabefelder | Fuer welchen Kurs |
|---|---|---|---|
| Caption Creator | Generiert komplette Instagram-Captions | Thema, Ziel (Saves/Kommentare/DMs), Ton | Content-Kurs |
| E-Mail-Sequenz-Generator | Schreibt eine 5-7 teilige E-Mail-Serie | Produkt, Zielgruppe, Preis, Launch-Datum | Launch-Kurs |
| Reel-Skript-Schreiber | Erstellt 30-60s Reel-Skripte | Thema, Hook-Typ, Call-to-Action | Video-Content-Kurs |
| Funnel-Texter | Schreibt Landingpage-Texte | Produkt, Zielgruppe, Hauptversprechen | Funnel-Kurs |
| Angebots-Konfigurator | Entwickelt ein Angebotskonzept | Expertise, Zielgruppe, Budget der Zielgruppe | Business-Aufbau-Kurs |
| KI-Chatbot | Beantwortet Kundenfragen 24/7 | Kundenfrage (Freitext) | Jeder Kurs (als Support-Bonus) |

Jedes dieser Tools folgt dem gleichen Prozess:

1. Konzept definieren (Eingaben → Ausgaben)
2. Framework schreiben (dein Wissen als System-Prompt)
3. Frontend bauen lassen (Claude Code)
4. Backend einrichten (Netlify Function)
5. Online stellen und testen

TIPP: Starte mit einem Tool. Wenn das gut funktioniert, kannst du das gleiche Geruest fuer weitere Tools wiederverwenden — du musst nur das Framework und die Eingabefelder anpassen.

## Glossar — Alle Fachbegriffe einfach erklaert

**API (Application Programming Interface)** — Eine Schnittstelle, ueber die Programme miteinander reden koennen. Dein Tool "ruft" die Claude API an und bekommt eine Antwort zurueck. Wie ein Telefon zwischen deinem Tool und der KI.

**API-Key** — Dein persoenliches Passwort fuer die KI-Schnittstelle. Damit weiss der KI-Dienst, dass du berechtigt bist und stellt dir die Nutzung in Rechnung. Muss IMMER geheim bleiben.

**Anthropic** — Die Firma hinter Claude (der KI). Vergleichbar mit OpenAI (ChatGPT). Du brauchst einen Anthropic-Account fuer den API-Key.

**Backend** — Der unsichtbare Teil deines Tools. Hier wird der API-Key sicher aufbewahrt und die Kommunikation mit der KI abgewickelt. Der Nutzer sieht das Backend nie.

**Brand-Farben** — Die Farben deiner Marke, angegeben als Hex-Code (z.B. #D4549A fuer Pink). Werden im CSS definiert, damit dein Tool zu deinem Branding passt.

**Claude API** — Der KI-Dienst von Anthropic, den dein Tool im Hintergrund nutzt. Kostet ca. 1-5 Cent pro Anfrage — je nach Laenge der Antwort.

**CSS (Cascading Style Sheets)** — Die Datei die das Design definiert: Farben, Schriften, Abstände, Layout. Wie die Inneneinrichtung eines Hauses. Du schreibst es nicht selbst — Claude Code macht das.

**Deploy / Deployment** — Dein Tool im Internet verfuegbar machen. Bei Netlify: Ordner hochladen → fertig.

**Drag & Drop** — Etwas mit der Maus anfassen, ziehen und an einer anderen Stelle loslassen. So lädst du deinen Tool-Ordner bei Netlify hoch.

**Frontend** — Der sichtbare Teil deines Tools — das was der Nutzer sieht und bedient. Besteht aus HTML (Struktur), CSS (Design) und JavaScript (Funktionen).

**HTML (HyperText Markup Language)** — Die Datei die die Struktur der Seite definiert: Ueberschriften, Texte, Eingabefelder, Buttons. Wie der Grundriss eines Hauses.

**iFrame** — Ein "Fenster" in einer Webseite, das eine andere Webseite anzeigt. Damit kannst du dein Tool direkt in deiner Kursplattform einbetten, ohne dass der Nutzer die Seite verlassen muss.

**JavaScript (JS)** — Die Datei die die Funktionen definiert: Was passiert beim Klicken? Wohin werden die Daten geschickt? Wie werden Ergebnisse angezeigt? Wie die Haustechnik (Licht, Heizung).

**JSON (JavaScript Object Notation)** — Ein Format, in dem Daten strukturiert uebertragen werden. Wie ein Formular mit beschrifteten Feldern. Die KI gibt ihre Antwort oft als JSON zurueck, damit dein Tool die Teile richtig anzeigen kann.

**Netlify** — Ein kostenloser Hosting-Service. Du lädst deinen Ordner hoch und bekommst eine URL. Netlify kann auch Backend-Funktionen ausfuehren (Netlify Functions).

**Netlify Function** — Eine kleine Programmier-Funktion, die auf Netlify laeuft. In deinem Fall: Sie empfaengt die Nutzereingaben, fuegt den API-Key hinzu und schickt alles an die Claude API.

**Responsive** — Eine Website/Tool die sich automatisch an verschiedene Bildschirmgroessen anpasst — sieht auf dem Handy genauso gut aus wie auf dem Computer.

**System-Prompt** — Die Grundanweisung an die KI — wird bei JEDER Anfrage mitgeschickt, noch bevor der Nutzer etwas eingibt. Hier steckt dein komplettes Framework: Regeln, Beispiele, Stil, Dos & Don'ts.

**Umgebungsvariable (Environment Variable)** — Ein geheimer Wert, der auf dem Server gespeichert ist — nicht im Code. Dein API-Key wird als Umgebungsvariable gespeichert, damit er sicher ist.
