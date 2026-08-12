# Tool-Playbook — Blotato & Canva

Die konkreten Aufrufe. Alles hier ist an den echten Tool-Schemas geprüft, nicht geraten.

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

Eine Story ist **ein Aufruf pro Folie**, mit `mediaType: "story"`:

```
blotato_create_post({
  accountId:     "<Instagram-Account-ID>",
  platform:      "instagram",
  mediaType:     "story",
  text:          "<Story-Text>",
  mediaUrls:     ["<URL dieser Folie>"],
  scheduledTime: "2026-08-12T19:15:00Z"
})
```

Stolperfallen:

- **`firstComment` funktioniert bei Stories nicht.** Nicht mitschicken.
- Folien brauchen **Abstand** — 3 Minuten haben sich bewährt (21:15, 21:18, 21:21 …). Gleichzeitig eingeplante Stories kommen nicht zuverlässig in der gedachten Reihenfolge an.
- Facebook-Stories brauchen zusätzlich zu `mediaType: "story"` weiterhin die `pageId`.

---

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
