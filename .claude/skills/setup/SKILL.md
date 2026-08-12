---
name: setup
description: Workspace einrichten, Kontext-Dateien füllen und neue Skills anlegen. Nutze diesen Skill bei "setup", "einrichten", "Onboarding", "Kontext füllen", "neuer Skill", "Workspace anpassen", "was fehlt noch" — oder wenn Kontext-Dateien leer sind und die Arbeit dadurch blockiert.
---

# setup — Workspace einrichten & erweitern

Dieser Skill hält das Second Brain am Laufen. Zwei Aufgaben:
**Kontext füllen** und **neue Skills bauen**.

---

## Teil 1: Kontext-Dateien füllen

### Warum das zuerst kommt
Alle Text-Skills greifen auf `context/` zu. Leere Dateien = generische Texte.
Das ist der Unterschied zwischen „klingt nach KI" und „klingt nach Monika".

### Der Zustand prüfen

| Datei | Was drin sein muss | Priorität |
|---|---|---|
| `profil/01_wer-bin-ich.md` | Wer, Zielgruppe, Versprechen | ✅ vorhanden |
| `context/stimme.md` | Wortwahl, Rhythmus, Verbotsliste | ✅ vorhanden |
| `context/business-info.md` | Angebote, Preise, Tools, Links | 🔴 hoch |
| `context/personal-info.md` | Zeit, Tech-Level, Werte | 🟡 mittel |
| `context/strategy.md` | Fokus, 90-Tage-Ziele, Engpässe | 🔴 hoch |
| `context/current-data.md` | Subscriber, Öffnungsrate, Umsatz | 🔴 hoch |
| `context/zielgruppe-otoene.md` | Echte Zitate von Kundinnen | 🟡 wächst mit der Zeit |

### So gehe ich vor

**Nicht** alle Dateien auf einmal. Das überfordert.

1. **Eine** Datei auswählen — die mit der höchsten Priorität
2. Fragen stellen — **eine nach der anderen**, nicht als Fragebogen
3. Antworten direkt einarbeiten und in Monikas Sprache formulieren
4. Datei zeigen: „Passt das so?"
5. Erst dann die nächste anbieten

### Fragen, die funktionieren

**Für `business-info.md`:**
- „Was verkaufst du gerade konkret — und zu welchem Preis?"
- „Welche Tools bezahlst du im Monat?"
- „Wo findet man dich? (Website, Instagram, Systeme.io)"

**Für `strategy.md`:**
- „Wenn in 90 Tagen eine Sache erledigt wäre — welche?"
- „Was hält dich gerade am meisten auf?"
- „Was hat zuletzt richtig gut funktioniert?"

**Für `current-data.md`:**
- „Wie viele Leute sind aktuell auf deiner Liste?"
- „Was war die letzte Kampagne und wie lief sie?"
- Kampagnen-Daten kann ich über die Wild-Mail-Anbindung selbst holen (→ Skill `wildmail`)

---

## Teil 2: Neuen Skill anlegen

### Wann ein neuer Skill sinnvoll ist
Wenn Monika dieselbe Art von Aufgabe **zum dritten Mal** stellt und
jedes Mal dieselben Vorgaben wiederholen muss.

### Aufbau
```
.claude/skills/[name]/SKILL.md
```

```markdown
---
name: [kleinbuchstaben-mit-bindestrich]
description: [Was der Skill tut + wann er greifen soll.
Konkrete Auslöse-Wörter nennen, die Monika wirklich benutzt.]
---

# [name] — [Untertitel]

## Ablauf
## Regeln
## Ausgabeformat
## Check vor der Ausgabe
```

### Regeln für gute Skills
- **`description` ist entscheidend** — danach wird der Skill ausgewählt.
  Immer die echten Wörter aufnehmen, die Monika tippt.
- Auf `context/stimme.md` und Skill `zielgruppe` verweisen statt Inhalte zu kopieren
- Ein Skill = eine Aufgabe
- Konkrete Beispiele schlagen abstrakte Regeln
- Immer eine Checkliste am Ende

### Nach dem Anlegen
1. Skill in `CLAUDE.md` in die Tabelle eintragen
2. Committen und pushen
3. **Neue Session starten** — Skills werden beim Start geladen

---

## Teil 3: Was noch fehlt (Stand: Aufbau)

Ehrlicher Blick auf offene Punkte:

- [ ] `context/business-info.md` — Angebote & Preise fehlen
- [ ] `context/strategy.md` — aktueller Fokus fehlt
- [ ] `context/current-data.md` — keine Zahlen eingetragen
- [ ] `context/zielgruppe-otoene.md` — noch keine echten Kundinnen-Zitate
- [ ] Skill `webinar` — falls Monika Webinare plant
- [ ] Skill `pinterest` — falls Pinterest ein echter Kanal wird

**Nicht alles auf einmal.** Immer den einen Punkt vorschlagen,
der die nächste Aufgabe blockiert.
