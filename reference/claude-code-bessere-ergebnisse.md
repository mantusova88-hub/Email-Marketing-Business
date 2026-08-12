# Bessere Ergebnisse mit Claude Code — Fehlermanagement & die 3 Erfolgsfaktoren

> **Quelle:** Kursmodul-Transkript (Fehlermanagement, allgemeiner Teil)
> **Status:** Punkt 1 (Kontext) vollständig erfasst. Das Transkript bricht mitten in
> Punkt 1 ab — Punkt 2 und 3 sind unten als offene Platzhalter markiert.
> **Hinweis zur Transkription:** „Nord Code", „Thought Coach", „Frau Code" sind
> Transkriptionsfehler und meinen immer **Claude Code**.

---

## 1. Für wen ist das relevant?

Für dich in **beiden** Situationen:

- Du warst mit deinen bisherigen Ergebnissen **unzufrieden** — irgendwas kam raus,
  aber nicht das, was du wolltest.
- Du bist **noch ganz am Anfang** und hattest überhaupt noch keine Ergebnisse.

In beiden Fällen gilt: Es gibt ein paar Fallstricke in der Zusammenarbeit mit Claude
Code, und du kannst **jetzt schon** etwas tun, um von Anfang an gute Ergebnisse zu
bekommen — bevor Frust entsteht.

Spezifischere Fehlermanagement-Themen (z. B. Karussellbeiträge aufbereiten, wo es
immer wieder Probleme gab) kommen in späteren Modulen.

---

## 2. Die Kernbotschaft: Der menschliche Faktor entscheidet

Claude Code ist ein Wunderwerk — die Kursleiterin arbeitet seit einem halben Jahr
praktisch ausschließlich damit und bearbeitet alles in ihrem Unternehmen darüber.
Ein großer Teil ihres Unternehmens läuft automatisiert.

**Aber:** Es braucht trotzdem menschlichen Input und ein Grundverständnis.

> **Du bestimmst, wie gut die Qualität des Outputs ist.**

Das ist keine Einschränkung, sondern die gute Nachricht: Die Qualität liegt in deiner
Hand — und sie ist lernbar. Genau darum geht es in den drei Punkten unten.

---

## 3. Die drei Erfolgsfaktoren

Diese drei Dinge tauchen im Kurs an mehreren Stellen auf. Das ist Absicht:
**Wiederholung ist wichtig**, weil diese drei Punkte essenziell für deinen Erfolg
mit Claude Code sind.

| # | Faktor | Status im Transkript |
|---|--------|----------------------|
| 1 | **Kontext** | ✅ vollständig erfasst (siehe unten) |
| 2 | _noch offen_ | ⏳ Transkript bricht vorher ab |
| 3 | _noch offen_ | ⏳ Transkript bricht vorher ab |

---

## 4. Faktor 1: Kontext

### Das Problem an einem Beispiel

Angenommen, du willst eine **Salespage** erstellen — also eine Seite, die dein
Produkt verkaufen soll. Du könntest schreiben:

> „Claude, bitte bau mir eine Salespage."

Klingt nach einem klaren Auftrag. Ist es aber nicht. Ohne Kontext weiß Claude nämlich
überhaupt nicht:

- Eine Seite **wozu**?
- Zu **welchem Produkt**?
- Zu **welchem Preis**?
- Welche **Links** soll er hinterlegen?
- Welche **Bilder** soll er hinterlegen?
- In welcher **Sprache** soll er sprechen — und in welchem Ton?
- Was ist die **Transformation** für deine Kunden?
- Worum geht's überhaupt?

Nichts davon ist gegeben. Deshalb funktioniert „bau mir eine Salespage" nicht.
**Du musst den Kontext liefern.** Claude muss auch das große Ganze verstehen.

### Die Mitarbeiter-Analogie

> **Claude Code ist dein Mitarbeiter.**

Und einem Mitarbeiter musst du auch das Verständnis dafür geben, wie er seine Aufgabe
zu bewerkstelligen hat. Du kannst einem Mitarbeiter ja auch nicht einfach sagen:

> „Fertige mal dieses Angebot an."

Er würde zurückfragen: *Wo? Für wen? Zu welchem Thema?*

Genau diese Rückfragen musst du bei Claude **vorwegnehmen** — indem du den Kontext
von Anfang an mitgibst.

### Die Lösung: `.md`-Dateien als Kontext-Speicher

Der Trick ist, den Kontext nicht jedes Mal neu zu tippen, sondern ihn **einmal
sauber aufzuschreiben** — in Markdown-Dateien (`.md`), die Claude lesen kann.

Beispiele für Kontext, den du in `.md`-Dateien ablegst:

- **Deine Brand Voice** — wie du sprichst, welche Wörter du benutzt, welche nicht
- **Deine Firmengeschichte** — wer du bist, wie du dahin gekommen bist, was dein
  Hintergrund ist
- **Pro Produkt eine eigene Datei** — für jedes deiner Produkte eine `.md`-Datei mit
  allen Details, die du bei Bedarf mitgeben kannst

Claude nimmt das als Kontext und weiß dann, **wie du sprichst, wer du bist und was
dein Hintergrund ist**.

---

## 5. So setzt du Faktor 1 in diesem Workspace um

Die gute Nachricht: Dein Second Brain ist genau dafür schon gebaut. Der Kontext
gehört an diese Stellen:

| Was | Wohin | Zweck |
|-----|-------|-------|
| Wer du bist, deine Rolle, dein Tech-Level | `context/personal-info.md` | Claude versteht **dich** |
| Services, Markt, Angebote | `context/business-info.md` | Claude versteht dein **Business** |
| Ziele, Fokus, Prioritäten | `context/strategy.md` | Claude versteht **wohin** du willst |
| Aktuelle KPIs und Zahlen | `context/current-data.md` | Claude versteht **wo du stehst** |
| Bestehende Dokumente zum Einlesen | `context/import/` | Altes Material einspeisen |
| Verhalten, Mission, Prinzipien | `CLAUDE.md` | Wird **automatisch** immer geladen |

**Dein nächster Schritt:** In `context/personal-info.md` und `context/strategy.md`
stehen aktuell nur die Fragen als Kommentare — noch keine Antworten. Genau das ist
der fehlende Kontext. Fülle diese beiden Dateien aus, dann arbeitet Claude sofort
deutlich präziser.

**Und am Session-Start:** `/prime` ausführen. Damit scannt Claude alle
Kontext-Dateien, bevor die Arbeit losgeht — statt dass du den Kontext jedes Mal neu
erklärst.

### Kontext-Briefing-Vorlage (zum Kopieren)

Wenn du etwas Konkretes bauen lässt — Salespage, E-Mail, Angebot —, gib dieses
Briefing mit:

```
Produkt:        [Name]
Preis:          [€ XX]
Zielgruppe:     [z. B. selbständige Mamas, die ...]
Transformation: [Von welchem Zustand → in welchen Zustand?]
Sprache/Ton:    [z. B. Deutsch, du-Form, warm und ermutigend]
Links:          [Checkout-Link, Impressum, ...]
Bilder:         [welche, wo liegen sie?]
Ziel der Seite: [z. B. Direktkauf für €7, kein Erstgespräch]
Referenz:       [Datei oder Beispiel, das den Stil zeigt]
```

---

## 6. Ergänzung aus der Praxis: Was tun, wenn ein Ergebnis nicht passt?

> ⚠️ Dieser Abschnitt stammt **nicht** aus dem Transkript, sondern ist eine
> praktische Ergänzung. Wenn das Kursmodul später eigene Anweisungen dazu liefert,
> haben die Vorrang.

1. **Nicht neu starten, sondern nachschärfen.** Sag konkret, was nicht passt
   („der Ton ist zu sachlich", „der Preis fehlt") — nicht „mach's besser".
2. **Prüfe zuerst den Kontext, nicht den Prompt.** Fehlt die Info in
   `context/`, wird kein Prompt sie ersetzen.
3. **Was einmal gut war, wird zum Kontext.** Ein gelungener Text gehört als
   Referenz nach `reference/` — dann kannst du beim nächsten Mal sagen:
   „im Stil von dieser Datei".
4. **Wiederkehrende Korrekturen gehören in `CLAUDE.md`.** Wenn du dieselbe
   Anmerkung dreimal machst, ist es keine Korrektur mehr, sondern eine Regel.

---

## 7. Offene Punkte

- [ ] **Faktor 2** aus dem Kursmodul ergänzen (Transkript bricht vorher ab)
- [ ] **Faktor 3** aus dem Kursmodul ergänzen (Transkript bricht vorher ab)
- [ ] Späteres Modul: spezifisches Fehlermanagement, u. a. **Karussellbeiträge
      aufbereiten**
- [ ] `context/personal-info.md` ausfüllen
- [ ] `context/strategy.md` ausfüllen
- [ ] Eigene `.md`-Dateien anlegen: **Brand Voice**, **Firmengeschichte**,
      je eine Datei **pro Produkt**
