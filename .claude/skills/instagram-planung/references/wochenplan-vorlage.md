# Wochenplan-Vorlage

Kopiere diese Struktur nach `outputs/instagram/YYYY-KW##-wochenplan.md`.

Die Datei entsteht **vollständig, bevor der erste Beitrag eingeplant wird** — mit allen Zeilen auf Status `offen`. Danach wandert je Beitrag genau eine Zeile auf `geplant`, sofort nach dem erfolgreichen Aufruf.

---

```markdown
# Social-Media-Woche KW ## / JJJJ

**Zeitraum:** Mo TT.MM. – So TT.MM.JJJJ
**Thema der Woche:** <Klammer, die alle Beiträge zusammenhält>
**Zuletzt aktualisiert:** JJJJ-MM-TT HH:MM

## Beiträge

| # | Tag | Zeit (Ortszeit) | Format | Kanal | Canva-Design | Status | Blotato-ID |
|---|---|---|---|---|---|---|---|
| 1 | Mi | 21:00 | Karussell | Instagram | <Titel> | offen | — |
| 2 | Mi | 21:00 | Karussell | Facebook | <Titel> | offen | — |
| 3 | Mi | 21:15 | Story Folie 1 | Instagram | <Titel> | offen | — |
| 4 | Mi | 21:15 | Story Folie 1 | Facebook | <Titel> | offen | — |
| 5 | Mi | 21:17 | Story Folie 2 | Instagram | <Titel> | offen | — |

**Status-Werte:** `offen` · `geplant` · `veröffentlicht` · `abgelehnt` · `fehlgeschlagen`

## Offene Punkte

<Was noch geklärt werden muss — abgelehnte Beiträge mit Grund, Fehlermeldungen, fehlende Designs.>

## Notizen

<Was diese Woche auffiel: was gut lief, was beim nächsten Mal anders gehört.>
```

---

## Wie die Status-Werte zu lesen sind

| Status | Bedeutung | Was als Nächstes passiert |
|---|---|---|
| `offen` | geplant im Kopf, noch nicht bei Blotato | einplanen |
| `geplant` | bei Blotato terminiert, Blotato-ID eingetragen | nichts — läuft |
| `veröffentlicht` | ist raus | nichts |
| `abgelehnt` | die Freigabe wurde bewusst verweigert | **nicht** unverändert wiederholen; nachfragen, was nicht gepasst hat |
| `fehlgeschlagen` | Blotato meldet `failed` | Fehlermeldung unter „Offene Punkte" notieren, Ursache beheben |

Die Spalte **Blotato-ID** trägt die `postSubmissionId` aus der Antwort. Ohne sie lässt sich später nicht nachvollziehen, welche Zeile zu welchem Beitrag gehört.
