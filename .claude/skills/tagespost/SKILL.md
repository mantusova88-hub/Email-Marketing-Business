---
name: tagespost
description: "Erstellt und terminiert EINEN Tag Social Media — Karussell und Story für Instagram und Facebook, von der Idee über Canva bis zum geplanten Beitrag in Blotato. Nutze diesen Skill wenn es um einen einzelnen Tag geht: Beitrag für morgen, Post für heute Abend, einen Tag nachholen, Tagespost. Für die ganze Woche auf einmal stattdessen instagram-planung."
---

# Tagespost — ein Tag, drei Schritte

Ein Abend. Ein Karussell, eine Story, zwei Kanäle. Kein Wochenplan, keine sieben Themen — nur der eine Tag.

```
1. content     →  Hook, sechs Folien, Call to Action, Story, Captions
2. Canva       →  Design bauen und als PNG exportieren
3. Einplanen   →  Karussell 21:00, Story 21:15 und 21:17, Instagram und Facebook
```

Für die ganze Woche auf einmal: **`instagram-planung`**. Dieser Skill hier ist die schnelle Variante für einen Tag.

---

## Setup

- **Instagram:** Account `52837` — `@emailsmitmonika_`
- **Facebook:** Account `36536`, `pageId` `1142132035656393` — Seite „e-mails mit Monika". **Ohne `pageId` scheitert jeder Facebook-Beitrag.**
- **Es gibt genau diese zwei Ziele.** „Monika Chancegeberin" ist der Besitzername derselben Facebook-Verbindung, kein eigenes Ziel.
- **Zeitzone:** Europe/Berlin. Sommerzeit (Ende März bis Ende Oktober) = UTC+2, sonst UTC+1.
- **Canva-Ordner:** Karussells `FAHTNsWd1Rs` · Stories `FAHTNup_p-o`
- **Vorlagen:** Karussell `DAHSAL0Neek` · Story `DAHSAM1jOEM`

| Ortszeit | UTC (Sommer) | Was |
|---|---|---|
| 21:00 | `19:00:00Z` | Karussell, alle sechs Folien in **einem** Beitrag |
| 21:15 | `19:15:00Z` | Story Folie 1 — eigener Beitrag, **ein** Bild |
| 21:17 | `19:17:00Z` | Story Folie 2 — eigener Beitrag, **ein** Bild |

---

## Schritt 0 — Erst nachsehen, dann planen

`blotato_list_posts` für den Zieltag, `platform: ["instagram", "facebook"]`, `status: ["scheduled", "published", "failed"]`.

Steht dort schon etwas für diesen Abend, **nicht** noch einmal einplanen. Doppelte Beiträge sind schlimmer als gar keine.

Zu wissen: Es gibt eine fremde Quelle, die gegen **20:05 Ortszeit** ein zweites Karussell und zwei Story-Folien veröffentlicht — erkennbar an KI-umgeschriebenem Text und den Hashtags `#emailsmitmonika #selbstliebe #grenzensetzen #mamaleben #selbstfürsorge`. Sie taucht weder in `blotato_list_schedules` noch in `blotato_list_automations` auf und ist über diese Verbindung nicht abschaltbar. **Nicht mit den eigenen Beiträgen verwechseln** und nicht versuchen, sie zu korrigieren.

---

## Schritt 1 — content

Den `content`-Skill nutzen. Er liefert in Monikas Stimme:

- **Hook** für Folie 1
- **Sechs Folien:** Folie 1 mit Bild und Hook, Folien 2–5 mit Text, Folie 6 mit Bild und Abschluss
- **Call to Action**
- **Zwei Story-Zeilen** — Folie 1 die Aussage, Folie 2 die Auflösung
- **Zwei Captions:** Instagram kurz mit fünf Hashtags, Facebook ausführlich mit „Dein Schritt für heute:" und **ohne** Hashtags

Regeln für die Folien:

- **Kein Wochentag auf der Folie.** Der gehört in den Canva-Titel.
- Das Label oben links trägt das **Thema**, nicht den Tag.
- Die Hook steht auf Folie 1 und wird nicht wiederholt. Jede Folie trägt einen eigenen Gedanken.
- Markenfarben Burgund `#800220`, Gold `#B59156`.

**Das Thema kommt aus Monikas Welt:** mentale Last, Grenzen, Erschöpfung, Selbstfürsorge, Mama-Alltag. **Kein E-Mail-Marketing, kein Business, kein Angebot** — es sei denn, Monika sagt ausdrücklich etwas anderes. Vor der Themenwahl im Archiv nachsehen (`blotato_list_posts` rückwärts), damit sich nichts wiederholt.

Alles in `outputs/instagram/YYYY-MM-DD-tagespost.md` festhalten, **bevor** Canva angefasst wird.

---

## Schritt 2 — Canva

1. **Kopieren:** `copy-design` von der Karussell-Vorlage `DAHSAL0Neek` und der Story-Vorlage `DAHSAM1jOEM`.
2. **Benennen:** `<Datum> Karussell <THEMA>` und `<Datum> Story <THEMA>` — sonst ist später nicht zuzuordnen, welches Design zu welchem Beitrag gehört.
3. **Texte setzen:** `read-design` mit `open_transaction`, dann `edit-design`, am Ende `finalize: "commit"`.
4. **Foto wählen:** Folie 1 und Folie 6 tragen ein echtes Bild. **Nie dasselbe Foto zweimal** — auch nicht an verschiedenen Tagen. Passt nichts, mit `generate-design` ein neues erzeugen.
5. **In den Ordner legen:** `move-item-to-folder` — Karussell nach `FAHTNsWd1Rs`, Story nach `FAHTNup_p-o`.
6. **Formate prüfen:** `get-export-formats` — Pflichtschritt vor jedem Export.
7. **Exportieren:** `export-design` als `png`. Story-Folien einzeln über `format.pages`. **Niemals `as_single_image: true`** bei einem Karussell.

Die Export-URLs laufen ab — deshalb gehören Export und Einplanen in **denselben Durchgang**.

---

## Schritt 3 — Einplanen

### Karussell — ein Aufruf, sechs Bilder

```
blotato_create_post({
  accountId:     "52837",
  platform:      "instagram",
  text:          "<Instagram-Caption>",
  mediaUrls:     [<sechs URLs in Folienreihenfolge>],
  scheduledTime: "<Datum>T19:00:00Z"
})
```

Facebook identisch, aber mit `accountId: "36536"`, `platform: "facebook"`, `pageId: "1142132035656393"` und der langen Caption.

### Story — zwei Aufrufe, je EIN Bild

**Instagram und Facebook erlauben pro Story-Beitrag genau ein Bild.** Zwei Bilder in einem Story-Aufruf werden als Karussell gewertet und landen im **Feed**. Genau so sind schon Story-Folien im Raster gelandet.

```
blotato_create_post({
  accountId:     "52837",
  platform:      "instagram",
  mediaType:     "story",
  text:          "<Zeile von Folie 1>",
  mediaUrls:     ["<URL Folie 1>"],
  scheduledTime: "<Datum>T19:15:00Z"
})
```

Danach derselbe Aufruf für Folie 2 mit `19:17:00Z`. Facebook genauso, zusätzlich mit `pageId`.

Im Konto erscheinen beide Folien als **ein** Story-Ring mit zwei Segmenten — genau wie gewünscht. Die zwei Aufrufe sind reine Technik und für Monika unsichtbar.

- **Text gehört dazu.** Jede Folie trägt ihre Zeile. Das stört die Story nicht.
- **Mindestens zwei Minuten Abstand.** Bei Sekundenabstand hat Instagram die Folien schon in umgekehrter Reihenfolge veröffentlicht.
- **`firstComment` funktioniert bei Stories nicht.** Nicht mitschicken.

---

## Die zwei Fallen, die schon dreimal zugeschlagen haben

### 1. `mediaType` verschwindet beim Anlegen

`blotato_create_post` verwirft `mediaType: "story"` manchmal stillschweigend. Der Beitrag wird dann ein Feed-Post.

**Nach jedem Story-Beitrag mit `blotato_get_schedule` prüfen**, ob im Entwurf steht:

```
"target": { "mediaType": "story", "targetType": "instagram" }
```

Fehlt es, mit `blotato_update_schedule` nachziehen — dort wird es zuverlässig gespeichert.

### 2. `blotato_update_schedule` ohne `scheduledTime` zerstört die Uhrzeit

**Jeden `blotato_update_schedule`-Aufruf mit `scheduledTime` schicken** — auch wenn sich die Zeit nicht ändern soll. Fehlt das Feld, zieht Blotato den Beitrag auf den Queue-Slot des Kontos (18:00 UTC = 20:00 Ortszeit) und wirft die eingestellte Zeit weg.

Danach mit `blotato_get_schedule` prüfen, ob `scheduledAt` noch stimmt.

---

## Abschluss

Nach dem Einplanen alle sechs Beiträge einmal mit `blotato_list_schedules` durchsehen:

| Prüfen | Soll |
|---|---|
| Anzahl | 6 — Karussell IG, Karussell FB, Story F1 IG, Story F1 FB, Story F2 IG, Story F2 FB |
| Uhrzeiten | 19:00 / 19:15 / 19:17 UTC, nicht 18:00 |
| Story-Entwürfe | `mediaType: "story"` und **genau eine** URL in `mediaUrls` |
| Karussell-Entwürfe | sechs URLs in der richtigen Reihenfolge |
| Facebook | `pageId` gesetzt |

Dann die Datei `outputs/instagram/YYYY-MM-DD-tagespost.md` mit den Schedule-IDs ergänzen und committen.

**Am Abend danach kontrollieren:** `blotato_list_posts` mit `status: ["published"]` und die `postUrl` ansehen.

| URL enthält | Bedeutung |
|---|---|
| `instagram.com/stories/…` · `facebook.com/stories/…` | Story ✓ |
| `instagram.com/p/…` | Feed-Beitrag — bei einer Story ist das ein Fehler |

Veröffentlichte Beiträge lassen sich über Blotato **nicht** löschen. Ein Fehler muss deshalb vor dem Posten auffallen, nicht danach.

---

## Wie du mit Monika sprichst

- **Kurz.** Ergebnis zuerst, Erklärung nur wenn sie hilft. Keine langen Berichte.
- **Keine Hausaufgaben.** Monika macht keine Plattform-Einstellungen. Was nicht über diese Verbindung geht, wird als Grenze benannt — einmal, sachlich, ohne Aufforderung.
- **Erst prüfen, dann antworten.** Bei jeder Frage nach dem Stand zuerst `blotato_list_posts` aufrufen. Blotato gilt, nicht die Notizen und nicht das Gedächtnis.
