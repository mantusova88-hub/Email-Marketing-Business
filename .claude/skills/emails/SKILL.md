---
name: emails
description: Newsletter, E-Mail-Sequenzen und einzelne Mails in Monikas Stimme schreiben. Nutze diesen Skill bei "E-Mail", "Newsletter", "Mail schreiben", "Sequenz", "Willkommensserie", "Betreffzeile", "Autoresponder", "an meine Liste schreiben". Das ist Monikas Kerngeschäft — hier zählt Qualität am meisten.
---

# emails — E-Mails in Monikas Stimme

Das ist der wichtigste Skill im Workspace. E-Mail ist Monikas Geschäft
und ihr Beweis: Wenn ihre eigenen Mails gut sind, verkauft das ihr Angebot mit.

**Immer zuerst lesen:** `context/stimme.md` und Skill `zielgruppe`.

---

## 1. Bevor ich schreibe — drei Fragen

Nur diese drei. Wenn die Antworten aus dem Kontext hervorgehen: nicht fragen, loslegen.

1. **Was soll die Leserin danach tun?** (Klicken / antworten / kaufen / nur lesen)
2. **Wo steht sie gerade?** (Neu auf der Liste / lange dabei / hat schon gekauft)
3. **Gibt es einen Anlass?** (Launch, Feiertag, Beobachtung, Kundinnen-Frage)

---

## 2. Der Aufbau einer Monika-Mail

### Betreffzeile
- **30–45 Zeichen** — sie liest am Handy
- Kleinschreibung ist erlaubt und wirkt persönlicher
- Neugier ODER konkreter Nutzen — nicht beides
- **Kein** Clickbait, der nicht eingelöst wird

**Funktioniert bei dieser Zielgruppe:**
| Typ | Beispiel |
|---|---|
| Alltagsszene | `gestern um 6:40 Uhr` |
| Bekenntnis | `das hab ich 2 Jahre falsch gemacht` |
| Direkte Frage | `wie oft schreibst du deiner Liste?` |
| Konkretes Ergebnis | `3 E-Mails, die für dich verkaufen` |
| Widerspruch | `warum ich nicht mehr täglich poste` |

**Immer 3 Varianten anbieten**, damit Monika wählen kann.

→ Formeln und bewährte Muster: Skill `hooks` + `reference/hooks-bibliothek.md`

### Vorschautext (Preheader)
35–90 Zeichen. **Ergänzt** die Betreffzeile, wiederholt sie nicht.
Wird oft vergessen — hier nie.

### Einstieg — die ersten zwei Zeilen
Das ist die eigentliche Betreffzeile. Wenn hier nichts passiert, ist die Mail weg.

**Bewährte Einstiege:**
- Szene: „Es war 6:40 Uhr. Das Kind hatte Fieber. Und ich…"
- Direkter Gedanke: „Ich muss dir was gestehen."
- Frage: „Kennst du das Gefühl, wenn…"

**Nie:** „Ich hoffe, es geht dir gut." / „In der heutigen Zeit…" / Begrüßungsfloskeln

### Hauptteil
- **Absätze: max. 3 Zeilen.** Am Handy sonst eine Wand.
- **Ein Gedanke pro Mail.** Nicht drei Tipps — einer, richtig.
- **Konkret statt abstrakt.** Zahlen, Namen, Uhrzeiten, echte Situationen.
- Persönliche Geschichte → Erkenntnis → Übertragung auf die Leserin

### Call-to-Action
- **Genau einer.** Nicht „antworte mir UND klick hier UND folge mir".
- Als eigener Absatz, nicht im Fließtext versteckt
- Niedrigschwellig formuliert: „Schau's dir an" statt „Jetzt kaufen"
- Bei Verkaufsmails: CTA 2× (Mitte + Ende), aber derselbe

### Abschluss
Monikas Name. Optional ein P.S.

> **Das P.S. wird fast immer gelesen.** Dort gehört das Wichtigste rein —
> nicht eine Nebensächlichkeit.

---

## 3. Länge

| Typ | Länge |
|---|---|
| Wert-Newsletter | 200–400 Wörter |
| Story-Mail | 300–500 Wörter |
| Verkaufsmail | 250–450 Wörter |
| Reine Info/Erinnerung | unter 150 Wörter |

Im Zweifel kürzer. Sabine liest um 22:30 Uhr auf dem Sofa.

---

## 4. Sequenzen

### Willkommenssequenz (5 Mails)
| # | Timing | Inhalt |
|---|---|---|
| 1 | sofort | Freebie liefern + kurz „wer bin ich" + Erwartung setzen |
| 2 | Tag 2 | Monikas Geschichte — warum sie das macht |
| 3 | Tag 4 | Konkreter Quick Win, sofort umsetzbar |
| 4 | Tag 6 | Das größte Missverständnis über E-Mail-Marketing |
| 5 | Tag 8 | Sanfter Übergang zum Angebot |

### Launch-Sequenz (6 Mails)
Problem benennen → Lösung zeigen → Angebot vorstellen → Einwände auflösen →
Beweis/Testimonial → Letzte Chance (ehrlich, mit echtem Enddatum)

### Reaktivierung (3 Mails)
Ehrlich fragen „liest du noch mit?" → Bestes Stück Content nochmal →
Abmelde-Angebot machen (bereinigt die Liste, hebt die Öffnungsrate)

---

## 5. Wild Mail / ActiveCampaign

Monikas Plattform ist **Wild Mail** (technisch = ActiveCampaign).

Wenn Mails direkt eingerichtet werden sollen:
- Kampagnen und Automationen können über die ActiveCampaign-Anbindung
  angelegt und bearbeitet werden
- Personalisierung: `%FIRSTNAME%` — **immer mit Fallback** („Hallo du" für Leere)
- Tags statt vieler Listen — sauberer zu segmentieren

→ Für Automationen und Setup: Skill `wildmail`

---

## 6. Ausgabeformat

```markdown
## Betreffzeilen (3 Varianten)
1. …
2. …
3. …

## Vorschautext
…

---

## Die Mail

[Vollständiger Text, fertig zum Kopieren]

---

**💡 Warum ich das so geschrieben habe:**
[2–3 Sätze — Monika soll daraus lernen, nicht nur kopieren]
```

Speichern in `outputs/email-[datum]-[thema].md`.

---

## 7. Qualitäts-Check vor der Ausgabe

- [ ] Klingt das nach `context/stimme.md`? (kurze Sätze, „du", kein Jargon)
- [ ] Ist ein Wort aus der Verbotsliste drin? → raus
- [ ] Ein Gedanke, ein CTA?
- [ ] Absätze unter 3 Zeilen?
- [ ] Würde Sabine um 22:30 denken „das bin ja ich"?
- [ ] Ist es ehrlich? Keine Versprechen, die Monika nicht halten kann?
