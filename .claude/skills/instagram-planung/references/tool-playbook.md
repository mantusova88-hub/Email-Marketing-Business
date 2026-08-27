# Tool-Playbook — Blotato & Canva

Die konkreten Aufrufe. Alles hier ist an den echten Tool-Schemas geprüft, nicht geraten.

---

## Die Grundordnung — gilt vor allem anderen

| Format | Landet in | Bilder pro Aufruf |
|---|---|---|
| **Karussell** | Instagram Feed **und** Facebook Beiträge | alle sechs Folien in **einem** Aufruf |
| **Story** | Instagram Story **und** Facebook Story | **genau ein** Bild pro Aufruf |

**Das Ziel ist immer dasselbe:** Monika sieht in ihrem Konto ein vollständiges Karussell mit allen Folien und eine vollständige Story mit allen Folien. Nichts fehlt, nichts ist zerrissen.

**Der Weg dorthin ist bei den beiden Formaten verschieden** — und genau das war schon zweimal die Fehlerquelle:

- Ein **Karussell** entsteht aus einem Aufruf mit mehreren Bild-URLs. Mehrere Aufrufe ergeben mehrere Beiträge — falsch.
- Eine **Story** entsteht aus mehreren Aufrufen mit je einer Bild-URL. Mehrere Bild-URLs in einem Aufruf ergeben ein Karussell — und Karussells landen im Feed, nicht in der Story. Ebenfalls falsch.

Instagram und Facebook zeigen aufeinanderfolgende Story-Beiträge desselben Kontos als **einen Story-Ring mit mehreren Folien**. Für Monika ist das eine Story mit zwei Folien — genau wie gewünscht. Die zwei Übermittlungen sind reine Technik und für sie unsichtbar.

**Pro Tag gibt es genau ein Zeitfenster.** Aktuell: Karussell 21:00, Story-Folie 1 um 21:15, Story-Folie 2 um 21:17. Niemals dieselben Inhalte zu zwei verschiedenen Uhrzeiten.

---

## Zeitzone — die häufigste stille Fehlerquelle

Blotato erwartet `scheduledTime` als ISO-8601-Zeitstempel und rechnet in UTC. Deutsche Ortszeit ist **nicht** UTC:

| Zeitraum | Versatz | 21:00 Ortszeit entspricht |
|---|---|---|
| Ende März bis Ende Oktober (Sommerzeit, CEST) | UTC+2 | `19:00:00Z` |
| Ende Oktober bis Ende März (Winterzeit, CET) | UTC+1 | `20:00:00Z` |

Beispiel für Mittwoch, 12. August 2026, 21:00 Ortszeit:

```
scheduledTime: "2026-08-12T19:00:00Z"
```

Der Aufruf gibt die aufgelöste `scheduledTime` in UTC zurück. **Diese Rückgabe immer gegen die gewünschte Ortszeit prüfen**, bevor die Zeile im Wochenplan auf `geplant` gesetzt wird. Eine um zwei Stunden verschobene Story fällt sonst erst auf, wenn sie zur falschen Zeit erscheint.

---

## Blotato: Accounts ermitteln

`blotato_list_accounts` — einmal pro Setup, danach stehen die IDs im Abschnitt „Dein Setup" der SKILL.md.

Liefert je Account `id`, `platform` und die Subaccounts. **Die Facebook-Page-ID steckt in den Subaccounts** und ist für jeden Facebook-Beitrag Pflicht.

---

## Blotato: Karussell einplanen

Ein Karussell ist **ein einziger Aufruf mit mehreren Bild-URLs** — nicht ein Aufruf pro Folie. Die Reihenfolge im Array ist die Reihenfolge im Karussell.

Instagram:

```
blotato_create_post({
  accountId:     "<Instagram-Account-ID>",
  platform:      "instagram",
  text:          "<Caption inkl. Hashtags>",
  mediaUrls:     ["<URL Folie 1>", "<URL Folie 2>", "<URL Folie 3>"],
  scheduledTime: "2026-08-12T19:00:00Z",
  altText:       "<kurze Bildbeschreibung>"
})
```

Facebook — gleicher Inhalt, aber `pageId` ist Pflicht:

```
blotato_create_post({
  accountId:     "<Facebook-Account-ID>",
  platform:      "facebook",
  pageId:        "<Facebook-Page-ID aus den Subaccounts>",
  text:          "<Caption>",
  mediaUrls:     [...],
  scheduledTime: "2026-08-12T19:00:00Z"
})
```

Für den Link zum Starter-Guide eignet sich `firstComment` — er wird direkt nach dem Veröffentlichen als erster Kommentar gesetzt und hält die Caption sauber.

---

## Blotato: Stories einplanen

**Ein Story-Beitrag enthält genau EIN Bild.** Instagram und Facebook lassen pro Story-Beitrag nur ein Bild zu. Zwei Bilder in einem Story-Aufruf werden als Karussell gewertet — und ein Karussell landet im Feed, nicht in der Story.

Eine Story mit zwei Folien besteht deshalb aus **zwei Aufrufen im Abstand von zwei Minuten**, Folie 1 zuerst:

```
blotato_create_post({
  accountId:     "<Account-ID>",
  platform:      "instagram",
  mediaType:     "story",
  text:          "",
  mediaUrls:     ["<URL Folie 1>"],
  scheduledTime: "2026-08-28T19:15:00Z"
})

blotato_create_post({
  accountId:     "<Account-ID>",
  platform:      "instagram",
  mediaType:     "story",
  text:          "",
  mediaUrls:     ["<URL Folie 2>"],
  scheduledTime: "2026-08-28T19:17:00Z"
})
```

Facebook genauso, zusätzlich mit `pageId`.

Im Konto erscheinen beide Folien danach als **ein** Story-Ring mit zwei Segmenten. Die Trennung ist nur technisch und für Monika nicht sichtbar.

Stolperfallen:

- **Niemals zwei Bild-URLs in einen Story-Aufruf.** Genau das ist am 27.08. passiert: auf Instagram wurde daraus ein Feed-Beitrag (`/p/…`), auf Facebook hat die Plattform die zweite Folie kommentarlos weggeworfen.
- **Mindestens zwei Minuten Abstand.** Bei Sekundenabstand hat Instagram die Folien schon einmal in umgekehrter Reihenfolge veröffentlicht (KW 33, Sa und So).
- **`firstComment` funktioniert bei Stories nicht.** Nicht mitschicken.
- **`text` bleibt leer.** Eine Bildunterschrift erhöht das Risiko, dass Blotato den Beitrag als Feed-Post behandelt.

## Blotato: Rückgabe richtig lesen

- **Geplante Beiträge** kommen sofort zurück, mit `postSubmissionId` und aufgelöster `scheduledTime`. **Kein Nachpollen nötig** — `blotato_get_post_status` ist hier überflüssig.
- **Sofort veröffentlichte Beiträge** pollen bis zu 20 Sekunden intern. Kommt danach noch `in-progress` zurück, mit `blotato_get_post_status` nachfassen, mindestens 10 Sekunden zwischen zwei Abfragen.
- **`failed`** enthält eine `errorMessage`. Die ist fast immer dauerhaft — dieselbe Übermittlung erneut zu schicken hilft nicht. Ursache lesen, beheben, neu einplanen.

---

## Blotato: Stand der Woche abfragen

```
blotato_list_posts({
  since:    "<Beginn des Fensters, ISO 8601>",
  until:    "<Ende des Fensters, ISO 8601>",
  platform: ["instagram", "facebook"],
  status:   ["scheduled", "published", "failed"]
})
```

Ohne `since`/`until` deckt der Aufruf nur 7 Tage rückwärts und 7 Tage vorwärts ab. Bei einer Antwort mit `cursor` gibt es weitere Seiten — die auch holen, sonst wirkt die Woche leerer als sie ist.

Dieser Aufruf steht am Anfang **und** am Ende jeder Planung: einmal um Doppelposts zu verhindern, einmal als Abschlussprüfung.

---

## Canva: Design finden und exportieren

1. **Finden:** `search-designs` mit `query` und `sort_by: "relevance"`. Für Vorlagen stattdessen `search-brand-templates` — `search-designs` findet keine Templates.
2. **Formate prüfen:** `get-export-formats` für die Design-ID. **Pflichtschritt.** Ein Export in einem Format, das das Design nicht unterstützt, schlägt fehl.
3. **Exportieren:** `export-design` als `png`. Über `format.pages` lassen sich einzelne Folien gezielt exportieren:

```
export-design({
  design_id: "D...",
  format: { type: "png", pages: [1], export_quality: "pro" }
})
```

`as_single_image: true` niemals für Karussells setzen — das klebt alle Folien zu einem Bild zusammen.

Die zurückgegebenen Download-URLs sind das, was in `mediaUrls` gehört. **Diese URLs laufen ab** — deshalb gehören Export und Einplanung in denselben Durchgang und nicht auf zwei Tage verteilt.

---

## ⛔ Die Story-Falle — hier ist schon alles schiefgegangen

**Story gehört in die Story. Karussell gehört in den Feed. Auf beiden Kanälen.** Diese Trennung ist nicht verhandelbar, und Blotato hält sie nicht von allein ein.

### Was passiert ist (KW 35, Mo–Mi)

`blotato_create_post` hat das mitgeschickte `mediaType: "story"` **stillschweigend verworfen**. Im gespeicherten Entwurf stand danach nur:

```
"content": { "text": "…", "platform": "instagram", "mediaUrls": [...] }
```

Kein `mediaType`. Folge: Alle Story-Folien sind drei Tage lang als **normale Feed-Beiträge** auf Instagram gelandet und haben das Raster zugemüllt. Zusätzlich hat Blotato alle Uhrzeiten auf seinen eigenen Queue-Slot (18:00 UTC) gezogen, wodurch die Abstände zwischen Karussell und Story verschwunden sind.

### Die Regel

**Nach dem Anlegen jedes Story-Beitrags mit `blotato_get_schedule` prüfen, ob `mediaType: "story"` im Entwurf steht.** Fehlt es, mit `blotato_update_schedule` nachziehen — dort wird es zuverlässig gespeichert.

Ein korrekter Story-Entwurf sieht so aus:

```
"target":  { "mediaType": "story", "targetType": "instagram" }
"content": { "text": "", "platform": "instagram", "mediaUrls": ["…genau eine URL…"] }
```

Drei Dinge daran sind wichtig:

- **`mediaType: "story"` muss im `target` stehen.** Ohne das Feld wird es ein Feed-Beitrag.
- **`text` bleibt leer.** Die funktionierenden Stories im Konto haben alle leeren Text. Eine Bildunterschrift erhöht das Risiko, dass Blotato den Beitrag als Feed-Post behandelt.
- **`mediaUrls` enthält genau eine URL.** Pro Folie ein eigener Beitrag, zwei Minuten Abstand.

### Der zweite Anlauf war auch falsch (Do 27.08.)

Nach der Korrektur oben standen beide Folien in **einem** Story-Beitrag. Das Ergebnis:

| Kanal | veröffentlichte URL | Ergebnis |
|---|---|---|
| Instagram | `instagram.com/p/Dcjg9wRiQJ3/` | Feed-Beitrag — zwei Bilder wurden als Karussell gewertet |
| Facebook | `facebook.com/stories/982899911438347` | Story, aber nur Folie 1 — Folie 2 verworfen |

Der Gegenbeweis stand in derselben Abfrage: Story-Beiträge mit **einer** Bild-URL sind sauber unter `instagram.com/stories/…` gelandet. Damit ist die Regel eindeutig — ein Bild pro Story-Beitrag.

### Auch die Uhrzeit prüfen

`blotato_create_post` bestätigt zwar die gewünschte `scheduledTime`, verschiebt sie aber danach auf den Queue-Slot des Kontos. Nach dem Anlegen die tatsächliche `scheduledAt` gegenprüfen und bei Bedarf mit `blotato_update_schedule` korrigieren.

### Kontrolle am Tag danach

Am Morgen nach dem ersten Posting-Abend `blotato_list_posts` mit `status: ["published"]` abfragen und die `postUrl` ansehen:

| URL enthält | Bedeutung |
|---|---|
| `instagram.com/stories/…` | Story ✓ |
| `facebook.com/stories/…` | Story ✓ |
| `instagram.com/p/…` | **Feed-Beitrag** — bei einer Story ist das ein Fehler |

Steht bei einer Story `/p/`, sofort alle noch geplanten Story-Beiträge korrigieren, bevor der nächste Abend kommt.
