---
name: instagram-planung
description: "Plant und terminiert die Social-Media-Woche (Karussells, Stories, Reels) für Instagram und Facebook — von der Idee über Canva bis zum geplanten Beitrag in Blotato. Nutze diesen Skill IMMER wenn es um Instagram-Planung, Wochenplanung, Beiträge einplanen, Karussell posten, Stories planen, Redaktionsplan oder Social-Media-Automation geht — auch dann, wenn nur ein einzelner Beitrag nachgeholt werden soll."
---

# Instagram-Planung — die Woche, die auch ohne dich durchläuft

Dieser Skill terminiert die Social-Media-Woche auf Instagram und Facebook. Er ist für einen ganz bestimmten Fehlerfall gebaut: **eine Sitzung bricht mittendrin ab, und hinterher weiß niemand mehr, was schon geplant war und was nicht.** Genau so ist schon ein Dienstag verlorengegangen.

Die Lösung ist keine Gedächtnisleistung, sondern eine Datei.

---

## Die eiserne Regel: erst die Wochenplan-Datei, dann der erste Tool-Call

**Bevor ein einziger Beitrag eingeplant wird, liegt der vollständige Wochenplan als Datei auf der Platte.** Sie ist die einzige Wahrheit über den Stand der Woche — nicht der Chatverlauf, nicht das Gedächtnis, nicht die Blotato-Oberfläche.

- **Pfad:** `outputs/instagram/YYYY-KW##-wochenplan.md` (z.B. `outputs/instagram/2026-KW33-wochenplan.md`)
- **Vorlage:** `references/wochenplan-vorlage.md`
- **Nach jedem einzelnen geplanten Beitrag** wird die Zeile in der Datei sofort aktualisiert — nicht gesammelt am Ende.

Bricht die Verbindung ab, sagt der nächste Blick in diese Datei auf die Sekunde genau, wo weitergemacht wird. Das ist der ganze Trick.

---

## Dein Setup — HIER AUSFÜLLEN

> Diese Angaben ändern sich selten. Einmal eintragen, dann fragt der Skill nie wieder danach.
> Steht hier noch ein `[Platzhalter]`, wird der Wert **einmal** zur Laufzeit ermittelt (siehe Klammer) und direkt hier eingetragen.

- **Zeitzone:** Europe/Berlin — Sommerzeit (Ende März bis Ende Oktober) = UTC+2, Winterzeit = UTC+1
- **Instagram-Account-ID (Blotato):** `52837` — `@emailsmitmonika_`
- **Facebook-Account-ID (Blotato):** `36536`
- **Facebook-Page-ID (Blotato-Subaccount):** `1142132035656393` — Seite „e-mails mit Monika". Ohne diesen Wert scheitert jeder Facebook-Beitrag.
- **Canva-Ordner:** KW-Karussells `FAHTNsWd1Rs` · KW-Stories `FAHTNup_p-o`
- **Feste Posting-Zeiten:** Karussell 21:00, Story Folie 1 um 21:15, Folie 2 um 21:17
- **Kanäle:** jeder Beitrag geht auf Instagram **und** Facebook

### Es gibt genau zwei Ziele — geprüft am 28.08.2026

`blotato_list_accounts` liefert **nur** diese beiden. Ein zweites Facebook-Ziel existiert nicht.

Der Facebook-Account trägt den Namen **„Monika Chancegeberin"**, weil dieses Profil die Seite besitzt. Das ist **kein** eigenes Ziel — es ist der Besitzername derselben Verbindung. Facebook zeigt ihn in manchen Ansichten neben der Seite an, was schon zweimal zu der Vermutung geführt hat, ein Beitrag sei auf dem falschen Konto gelandet. Ist er nicht: Auf Facebook gibt es genau ein Ziel, also kann von hier aus auch nichts doppelt erscheinen.

Ein weiteres Facebook-Profil lässt sich von hier aus **nicht** hinzufügen — dafür braucht Blotato eine Facebook-Anmeldung durch Monika. Außerdem erlaubt Facebook automatisches Posten nur auf **Seiten**, nicht auf persönliche Profile.

Erscheint ein Beitrag trotzdem doppelt, liegt es nicht an einem zweiten Konto, sondern an der fremden Quelle gegen 20:05 (siehe `outputs/instagram/2026-KW35-wochenplan.md`).

---

## Ablauf in sechs Schritten

### 1. Stand aufnehmen — niemals blind starten

Immer zuerst prüfen, was schon existiert. Zwei Quellen, beide lesen:

1. Die Wochenplan-Datei für die laufende Kalenderwoche, falls vorhanden.
2. `blotato_list_posts` mit `since`/`until` über das geplante Zeitfenster und `status: ["scheduled", "published", "failed"]`.

Weicht die Datei von Blotato ab, **gilt Blotato** — die Datei wird korrigiert. Was dort schon als `scheduled` steht, wird **nicht** noch einmal eingeplant. Doppelte Beiträge sind schlimmer als gar keine.

### 2. Content schreiben

Über den **`content`-Skill** — er kennt die Stimme und die Zielgruppe. Nie freihändig texten.

Pro Beitrag entstehen: Hook, Folientexte, Caption, Hashtags.

### 3. Design in Canva

Bestehendes Design finden (`search-designs`) oder aus einer Brand-Template erzeugen. Die Folienregeln stehen weiter unten — sie sind bewusst so entschieden und keine Geschmacksfrage.

### 4. Export als öffentliche Bild-URLs

Blotato braucht **öffentlich erreichbare URLs**, keine lokalen Dateien. Also `get-export-formats` → `export-design` als PNG, eine Datei pro Folie, Reihenfolge beibehalten. Die Export-URLs in die Wochenplan-Datei schreiben.

### 5. Plan zeigen, dann terminieren

**Erst die vollständige Tabelle aller geplanten Beiträge zeigen, dann terminieren.** Nicht Beitrag für Beitrag nachfragen — das erzeugt eine Kette von Rückfragen, bei der man irgendwann den Überblick verliert und aus Versehen das Falsche ablehnt.

Danach die Beiträge der Reihe nach über `blotato_create_post` einplanen, und **nach jedem einzelnen** die Zeile in der Wochenplan-Datei aktualisieren.

Details zu den Parametern: `references/tool-playbook.md`.

### 6. Abschlussprüfung

Zum Schluss noch einmal `blotato_list_posts` über das Fenster und mit der Datei abgleichen. Erst wenn beide übereinstimmen, ist die Woche fertig — und das wird auch so gesagt, mit der Anzahl geplanter Beiträge.

---

## Wenn etwas schiefgeht

**Ein Beitrag wurde abgelehnt.** Eine Ablehnung ist eine Entscheidung, kein Verbindungsfehler. Den identischen Aufruf **nicht** wiederholen. Stattdessen in der Datei als `abgelehnt` markieren, mit einem Satz nachfragen, was daran nicht gepasst hat, und den Rest der Woche normal weiterplanen. Ein abgelehnter Beitrag blockiert nie die übrigen.

**`blotato_create_post` meldet `failed`.** Die Fehlermeldung ist meist dauerhaft (abgelaufenes Token, nicht erreichbare Bild-URL, Formatproblem) — ein stumpfer zweiter Versuch bringt nichts. Fehlermeldung in die Datei schreiben, Ursache benennen, dann erst neu ansetzen.

**Die Sitzung bricht ab.** Beim nächsten Mal Schritt 1 ausführen. Die Datei plus `blotato_list_posts` ergeben zusammen den exakten Stand.

**Ein Tag ist bereits vorbei und nichts ist rausgegangen.** Nicht rückdatiert einplanen, das schlägt fehl. Offen ansprechen und zwei Wege anbieten: heute nachschieben oder in die kommende Woche ziehen.

---

## Regeln für die Folien

Diese Regeln sind bereits entschieden und werden nicht bei jedem Beitrag neu verhandelt:

- **Kein Wochentag auf den Folien.** Ein Karussell wird noch Wochen später gespeichert und weitergeschickt — steht „MITTWOCH" drauf, wirkt es alt.
- **Das Label oben links gehört dem Thema**, nicht dem Datum: `ERSCHÖPFUNG`, `TIPP 01`, `FEHLER 3`. Es ist der stärkste kleine Platz auf der Folie.
- **Die Wochentage stehen dort, wo sie gebraucht werden:** im Canva-Titel und in der Wochenplan-Datei.
- **Markenfarben:** Burgund `#800220`, Gold `#B59156`.
- **Die Hook steht auf Folie 1** und wird auf den Folgefolien nicht wiederholt. Jede Folie trägt einen eigenen Gedanken.

---

## Beigelegte Dateien

- `references/tool-playbook.md` — die konkreten Tool-Aufrufe für Blotato und Canva, inklusive Zeitzonen-Umrechnung und der Stolperfallen, die schon einmal Beiträge gekostet haben.
- `references/wochenplan-vorlage.md` — die Vorlage für die Wochenplan-Datei.
