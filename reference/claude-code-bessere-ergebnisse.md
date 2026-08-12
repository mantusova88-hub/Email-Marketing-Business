# Die 3 Regeln für beste Ergebnisse mit Claude Code

> **Quelle:** Kursmodul „3 Regeln für beste Ergebnisse" (Fehlermanagement, allgemeiner Teil)
> — Transkript + To-Do-Liste des Moduls.
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
Hand — und sie ist lernbar.

Diese drei Regeln tauchen im Kurs an mehreren Stellen auf. Das ist Absicht:
**Wiederholung ist wichtig**, weil sie essenziell für deinen Erfolg mit Claude Code
sind.

---

## 3. Regel 1: Kontext geben

> **To-Do aus dem Kurs:** Vor jeder Aufgabe vollen Kontext über `.md`-Dateien geben.

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

## 4. Regel 2: Immer das Output-Ziel nennen

> **To-Do aus dem Kurs:** Immer das Output-Ziel nennen (HTML oder online stellen).

Kontext allein reicht nicht. Claude muss auch wissen, **was am Ende dabei
herauskommen soll** — in welcher Form du das Ergebnis brauchst.

Dasselbe Thema kann nämlich völlig unterschiedliche Ergebnisse bedeuten:

| Du willst … | Output-Ziel, das du nennen musst |
|---|---|
| Eine Seite, die du selbst hochladen kannst | **eine HTML-Datei** in `outputs/` |
| Eine Seite, die sofort im Netz erreichbar ist | **online stellen** (z. B. Netlify) |
| Text, den du in Systeme.io einfügst | **reiner Text / Textbausteine** |
| Eine Anleitung für dich zum Nachmachen | **Markdown-Datei** in `reference/` |
| Eine E-Mail für deine Liste | **Betreff + Body**, fertig zum Einfügen |

Wenn du das Output-Ziel nicht sagst, rät Claude — und rät womöglich falsch. Dann hast
du eine schöne HTML-Datei, wolltest aber Text zum Einfügen. Oder umgekehrt.

**Ein Satz genügt.** Zum Beispiel:

> „Bau mir das als **einzelne HTML-Datei** in `outputs/`, die ich per Drag & Drop bei
> Netlify hochladen kann."

oder

> „Ich brauche das als **fertigen Text**, den ich direkt in Systeme.io einfügen kann —
> kein HTML."

**Merksatz:** Sag nicht nur *was* gebaut werden soll, sondern auch *in welcher Form
du es in der Hand halten willst*.

---

## 5. Regel 3: Iterieren — mit mehreren Runden rechnen

> **To-Do's aus dem Kurs:**
> Mit mehreren Iterationsrunden rechnen und gelassen bleiben.
> Verbesserungswünsche so spezifisch wie möglich formulieren.

### Der erste Wurf ist nicht das Ergebnis

Das ist der Punkt, an dem die meisten frustriert aussteigen: Der erste Versuch sieht
nicht so aus wie erhofft — und man denkt, „das funktioniert nicht".

Falsch. **Mehrere Runden sind der Normalfall, nicht das Scheitern.** Du arbeitest
nicht mit einem Automaten, der auf Knopfdruck das Fertige ausspuckt, sondern mit
einem Mitarbeiter, dem du Feedback gibst. Auch einem menschlichen Mitarbeiter gibst
du beim ersten Entwurf Anmerkungen.

**Also: gelassen bleiben.** Plane die Runden von Anfang an ein. Dann ist Runde 2
kein Rückschlag, sondern ein eingeplanter Schritt.

### Verbesserungswünsche so spezifisch wie möglich

Und hier entscheidet sich, ob Runde 2 wirklich besser wird. Vages Feedback erzeugt
vage Verbesserungen:

| ❌ So nicht | ✅ Sondern so |
|---|---|
| „Gefällt mir nicht." | „Die Überschrift ist zu sachlich — mach sie warm und persönlich, mit du-Anrede." |
| „Mach's besser." | „Der Preis fehlt. Setz €7 direkt unter den Button." |
| „Sieht komisch aus." | „Die Schrift auf dem Handy ist zu klein. Mindestens 18px im Fließtext." |
| „Zu lang." | „Kürze Abschnitt 2 auf maximal drei Sätze, der Rest bleibt." |

**Die Regel dahinter:** Sag *was genau*, *wo genau* und *wie es stattdessen sein
soll*. Je konkreter dein Wunsch, desto genauer das Ergebnis — und desto weniger
Runden brauchst du.

### Extra-Tipp für die Praxis

Wenn du dieselbe Anmerkung dreimal machst, ist es keine Korrektur mehr, sondern eine
**Regel**. Dann gehört sie nach `CLAUDE.md` oder in eine Kontext-Datei — damit du sie
nie wieder tippen musst. So macht Regel 3 mit der Zeit Regel 1 immer stärker.

---

## 6. So setzt du die 3 Regeln in diesem Workspace um

Die gute Nachricht: Dein Second Brain ist genau dafür schon gebaut.

| Was | Wohin | Zweck |
|-----|-------|-------|
| Wer du bist, deine Rolle, dein Tech-Level | `context/personal-info.md` | Claude versteht **dich** |
| Services, Markt, Angebote | `context/business-info.md` | Claude versteht dein **Business** |
| Ziele, Fokus, Prioritäten | `context/strategy.md` | Claude versteht **wohin** du willst |
| Aktuelle KPIs und Zahlen | `context/current-data.md` | Claude versteht **wo du stehst** |
| Bestehende Dokumente zum Einlesen | `context/import/` | Altes Material einspeisen |
| Verhalten, Mission, Prinzipien | `CLAUDE.md` | Wird **automatisch** immer geladen |
| Fertige Arbeitsergebnisse (HTML etc.) | `outputs/` | Das Output-Ziel aus Regel 2 |
| Anleitungen, Templates, Beispiele | `reference/` | Referenz für „im Stil von …" |

**Dein nächster Schritt:** In `context/personal-info.md` und `context/strategy.md`
stehen aktuell nur die Fragen als Kommentare — noch keine Antworten. Genau das ist
der fehlende Kontext aus Regel 1. Fülle diese beiden Dateien aus, dann arbeitet
Claude sofort deutlich präziser.

**Und am Session-Start:** `/prime` ausführen. Damit scannt Claude alle
Kontext-Dateien, bevor die Arbeit losgeht — statt dass du den Kontext jedes Mal neu
erklärst.

---

## 7. Briefing-Vorlage (zum Kopieren)

Deckt Regel 1 und Regel 2 in einem Schritt ab:

```
Produkt:        [Name]
Preis:          [€ XX]
Zielgruppe:     [z. B. selbständige Mamas, die ...]
Transformation: [Von welchem Zustand → in welchen Zustand?]
Sprache/Ton:    [z. B. Deutsch, du-Form, warm und ermutigend]
Links:          [Checkout-Link, Impressum, ...]
Bilder:         [welche, wo liegen sie?]
Referenz:       [Datei oder Beispiel, das den Stil zeigt]

OUTPUT-ZIEL:    [z. B. einzelne HTML-Datei in outputs/, die ich bei
                Netlify hochladen kann]
```

Und für Runde 2+ (Regel 3):

```
Was passt nicht: [konkret: welches Element?]
Wo genau:        [Abschnitt / Überschrift / Button ...]
Wie stattdessen: [der gewünschte Zustand]
Was bleibt:      [damit nicht versehentlich Gutes überschrieben wird]
```

---

## 8. Die Kurs-To-Do-Liste

- [ ] Vor jeder Aufgabe vollen Kontext über `.md`-Dateien geben
- [ ] Immer das Output-Ziel nennen (HTML oder online stellen)
- [ ] Mit mehreren Iterationsrunden rechnen und gelassen bleiben
- [ ] Verbesserungswünsche so spezifisch wie möglich formulieren

### Daraus abgeleitet für diesen Workspace

- [ ] `context/personal-info.md` ausfüllen
- [ ] `context/strategy.md` ausfüllen
- [ ] `context/business-info.md` und `context/current-data.md` ausfüllen
- [ ] Eigene `.md`-Dateien anlegen: **Brand Voice**, **Firmengeschichte**,
      je eine Datei **pro Produkt**
- [ ] Späteres Modul nachtragen: spezifisches Fehlermanagement, u. a.
      **Karussellbeiträge aufbereiten**
