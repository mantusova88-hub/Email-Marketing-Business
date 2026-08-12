---
name: willkommens-sequenz
description: >-
  "Willkommenssequenz", "Welcome-Serie", "Welcome-Sequenz", "Onboarding-Mails",
  "Freebie-Sequenz", "Autoresponder", "neue Subscriber", "Anmelde-Strecke",
  "erste Mails für neue Abonnentinnen".
  Nutze diesen Skill IMMER wenn "Willkommenssequenz", "Welcome-Serie",
  "Onboarding-Mails" oder "Sequenz für neue Subscriber" gesagt wird — auch
  wenn nur von "den ersten Mails nach der Anmeldung" die Rede ist.
  Liefert IMMER eine Übersichtstabelle + 5 vollständige Mails mit Betreff,
  Preheader, Text, Timing und Ziel je Mail.
---

# Willkommens-Sequenz-Skill

Schreibt die komplette Mailstrecke, die neue Subscriber nach der Anmeldung
bekommen — in deiner Stimme, sofort einsatzfähig in deinem E-Mail-Tool.

Diese Sequenz ist der wichtigste Text im ganzen Business: Sie läuft
automatisch, sie erreicht jede neue Leserin, und sie entscheidet, ob aus
einer Anmeldung eine Kundin wird. Deshalb lohnt sich hier Sorgfalt mehr
als bei jedem einzelnen Newsletter.

---

## So findet der Skill dein Business-Wissen (in dieser Reihenfolge)

1. **Eigene Definition vorhanden?** Prüfe zuerst, ob schon eine eigene Quelle
   existiert — z.B. `context/business-info.md`, `context/personal-info.md`,
   `context/strategy.md`, `zielgruppe.md` / `brand-voice.md` / `marke.md`
   oder ein Abschnitt in einer `CLAUDE.md`. **Falls ja: bevorzugt nutzen.**
2. **Sonst:** der ausgefüllte Abschnitt "Dein Business" unten.
3. **Noch nicht ausgefüllt?** Den Nutzer **einmalig** nach Freebie, Angebot,
   Zielgruppe und Tonalität fragen und die Antworten hier eintragen.

**Wichtig:** Wenn `newsletter-schreiben/SKILL.md` im Projekt existiert und dort
"Dein Business" ausgefüllt ist, nutze diese Angaben — die Stimme muss über
beide Skills hinweg dieselbe sein.

---

## Dein Business — HIER AUSFÜLLEN

> Ersetze jeden Platzhalter `[…]`. Löschen, was nicht passt.

### Freebie & Einstieg
- **Womit melden sich Leute an?** [z.B. Checkliste, Workbook, Mini-Kurs, Webinar]
- **Was verspricht das Freebie konkret?** [das eine Ergebnis]
- **Download-Link:** [URL]

### Zielgruppe
- **Wunschkundin (kurz):** [z.B. selbständige Mamas, die ihr Business neben der Familie aufbauen]
- **Die 3 größten Schmerzpunkte:** [in ihrer eigenen Sprache]
  1. [Schmerzpunkt 1]
  2. [Schmerzpunkt 2]
  3. [Schmerzpunkt 3]
- **Häufigste Einwände (+ Antwort):**
  - "[z.B. Ich habe keine Zeit]" → [Entkräftung]
  - "[z.B. Ich bin technisch nicht begabt]" → [Entkräftung]
  - "[z.B. Meine Liste ist zu klein]" → [Entkräftung]

### Stimme
- **Anrede:** [du / Sie / ihr]
- **Tonalität in 3–5 Worten:** [z.B. warmherzig, ermutigend, auf Augenhöhe]
- **Meine No-Gos:** [z.B. Fachjargon, künstliche Verknappung, Hustle-Rhetorik]
- **Absender-Name:** [Name]
- **Signatur:** [z.B. "Von Mama zu Mama, [Name]"]

### Deine Geschichte (für Mail 2)
- **Wo hast du angefangen?** [der Punkt, an dem deine Leserin heute steht]
- **Was war dein Wendepunkt?** [was sich geändert hat]
- **Warum machst du das heute?** [dein Warum in einem Satz]

### Angebot (für Mail 5)
- **Hauptangebot:** [Kurs / Coaching / Produkt]
- **Preis:** [Betrag — nur eintragen wenn gesichert, sonst leer lassen]
- **Link zum Angebot:** [URL]
- **Für wen ist es NICHT?** [Abgrenzung — schafft Vertrauen]

---

# Standard-Output (IMMER beide Blöcke liefern)

Bei "Willkommenssequenz für [Freebie/Angebot]" → IMMER ohne Nachfragen:

### Block 1 — Übersichtstabelle
Vorweg, damit die Strecke auf einen Blick sichtbar ist:

| Mail | Versand | Ziel | Betreff |
|---|---|---|---|
| 1 | sofort | … | … |
| … | … | … | … |

### Block 2 — 5 vollständige Mails
Je Mail: **Betreff · Preheader · Volltext · Timing**, fertig zum Kopieren.

**Zusätzlich:** Ablegen unter `outputs/sequenzen/JJJJ-MM-TT-willkommenssequenz.md`.

Wenn Angaben aus "Dein Business" fehlen: trotzdem liefern, dann am Ende **einen**
kurzen Hinweis, welche Angabe die Sequenz besser machen würde.

---

## Die 5 Mails — Aufbau und Ziel

Jede Mail hat **genau eine Aufgabe**. Das ist der Grund, warum die Sequenz
funktioniert: Sie verkauft nicht sofort, sondern baut in vier Schritten das
Vertrauen auf, das den fünften Schritt überhaupt erst möglich macht.

| # | Versand | Ziel | Call-to-Action |
|---|---|---|---|
| 1 | sofort | Freebie liefern, Erwartung setzen | Freebie herunterladen |
| 2 | Tag 2 | Beziehung — deine Geschichte | Antworten auf die Mail |
| 3 | Tag 4 | Quick Win — ein Ergebnis heute | Den Tipp umsetzen |
| 4 | Tag 6 | Den größten Einwand auflösen | Antworten oder weiterlesen |
| 5 | Tag 8 | Angebot vorstellen | Zum Angebot |

**Mail 1 muss sofort raus** — die Aufmerksamkeit ist nie wieder so hoch wie in
der Minute nach der Anmeldung.

**Erst ab Mail 5 wird verkauft.** Wer in Mail 1 verkauft, verliert die Leserin,
bevor sie überhaupt weiß, wer da schreibt.

---

## Das Gerüst pro Mail

```
Betreff: [30–50 Zeichen]
Preheader: [60–90 Zeichen, wiederholt den Betreff nicht]

[EINSTIEG — 2–3 Sätze. Bei Mail 1: direkt das Versprochene liefern.
Bei Mail 2–5: eine konkrete Szene oder eine direkte Frage.]

[HAUPTTEIL — 100–200 Wörter. Genau die eine Aufgabe dieser Mail,
nichts anderes. Absätze maximal 3 Zeilen.]

[BRÜCKE — 1 Satz: was in der nächsten Mail kommt.
Das hält die Sequenz zusammen und erhöht die Öffnungsrate der Folgemail.]

[CALL-TO-ACTION — genau EINER, als Einladung formuliert.]

[SIGNATUR aus "Dein Business"]
```

### Länge pro Mail

Eine pauschale Wortzahl passt hier nicht — jede Mail hat eine andere Aufgabe,
und die Aufgabe bestimmt, wie viel Raum sie braucht:

| Mail | Ziel-Länge | Warum |
|---|---|---|
| 1 | 80–150 Wörter | Liefern, nicht erklären. Sie will das Freebie, nicht deine Gedanken. |
| 2 | 200–300 Wörter | Deine Geschichte braucht Raum, sonst bleibt sie behauptet statt erlebt. |
| 3 | 150–250 Wörter | Ein Tipp, klar erklärt, sofort umsetzbar. |
| 4 | 200–300 Wörter | Einen Einwand auflösen heißt: erst ernst nehmen, dann widerlegen. |
| 5 | 250–350 Wörter | Angebot, Abgrenzung und Vertrauen — die längste Mail der Strecke. |

**Achtung beim Zählen:** Solange Platzhalter wie `[Dein Wendepunkt]` im Entwurf
stehen, liegt die Wortzahl unter dem Ziel. Erst nach dem Ausfüllen ist sie
aussagekräftig — nicht künstlich auffüllen, um die Zahl zu treffen.

---

## Stil-Regeln (nicht verhandelbar)

### Erlaubt + erwünscht
- Längere Sätze mit Haupt- und Nebensätzen — es soll gesprochen klingen
- Persönliche Story-Hooks („Vor 2 Jahren habe ich…", „Neulich saß ich…")
- Konkrete Zahlen und echte Beispiele statt vager Versprechen
- Direkte Ansprache (gemäß deiner Angabe unter „Stimme")
- Die Brücke zur nächsten Mail — sie ist das, was die Sequenz zur Sequenz macht

### Verboten
- „Hier ist, was…" / „Hier ist die…" (KI-Floskel)
- „Nicht weil X, sondern weil Y." (KI-Floskel)
- „Lass uns eintauchen", „In der heutigen schnelllebigen Welt" (KI-Floskeln)
- „easy peasy", Buzzwords ohne Substanz
- Übertriebene Versprechen („verdopple dein Einkommen in 7 Tagen")
- **Stakkato-Sätze. Kurz. Wie. Das.**
- `ae` / `oe` / `ue` / `ss` im Fließtext — echte Umlaute und ß nutzen
- Künstliche Verknappung in einer Sequenz, die dauerhaft läuft
  („nur noch heute" ist gelogen, wenn die Mail jede Woche neu ausgelöst wird)
- **Features, Preise, Termine oder Teilnehmerzahlen frei erfinden**
  (z.B. „lebenslanger Zugriff", „Geld-zurück-Garantie", „über 500 Teilnehmerinnen").
  Steht es nicht unter „Dein Business", kommt es nicht in die Mail.
  Im Zweifel weglassen oder einmal nachfragen.

### Checkliste vor der Ausgabe
- [ ] Hat jede Mail genau eine Aufgabe und einen Call-to-Action?
- [ ] Wird erst ab Mail 5 verkauft?
- [ ] Hat jede Mail außer der letzten eine Brücke zur nächsten?
- [ ] Jede Mail in ihrer Ziel-Länge (siehe Tabelle), Absätze maximal 3 Zeilen?
- [ ] Ist Mail 5 die längste und Mail 1 die kürzeste der Strecke?
- [ ] Keine KI-Floskel aus der Verboten-Liste drin?
- [ ] Keine Zahl, kein Preis, kein Feature erfunden?
- [ ] Klingt die Stimme wie im Skill `newsletter-schreiben`?

---

## Beispiel — Mail 3 (Quick Win)

**Eingabe:** „Bau mir eine Willkommenssequenz für mein Freebie ‚Die 5-Minuten-Newsletter-Checkliste'."

**Ausgabe (Auszug, Mail 3 von 5):**

> **Versand:** Tag 4
> **Ziel:** Quick Win — ein Ergebnis noch heute
>
> **Betreff:** Der Satz, der alles verändert hat
> **Preheader:** Er steht in fast jeder Mail von mir — hier ist er.
>
> Als ich angefangen habe, hat mich eine Frage jedes Mal blockiert: Worüber
> soll ich denn schreiben?
>
> Ich habe wirklich vor dem leeren Bildschirm gesessen und überlegt, was
> wichtig genug wäre. Und weil mir nichts wichtig genug erschien, habe ich
> gar nichts geschrieben.
>
> Was mich da rausgeholt hat, war ein einziger Satz: Schreib die Mail, die
> du selbst vor einem Jahr gebraucht hättest.
>
> Das funktioniert, weil du diese Frau kennst. Du weißt, wo sie feststeckt,
> weil du dort selbst gestanden hast. Und du brauchst keine neue Idee — du
> brauchst nur die Erinnerung.
>
> **Dein Schritt für heute:** Schreib dir drei Dinge auf, die du vor einem
> Jahr gern gewusst hättest. Das sind deine nächsten drei Newsletter. Zehn
> Minuten, mehr braucht es nicht.
>
> Übermorgen erzähle ich dir, warum die meisten trotzdem nicht anfangen —
> und was wirklich dahintersteckt.
>
> Antworte mir gern kurz mit deinem ersten Thema. Ich lese jede Antwort.
>
> Von Mama zu Mama,
> [Name]

---

## Was gut funktioniert hat

<!-- Nach den ersten Auswertungen eintragen. Öffnungsraten je Mail zeigen
     schnell, wo die Sequenz abreißt — genau dort lohnt sich die Überarbeitung. -->

| Mail | Öffnungsrate | Klickrate | Beobachtung |
|---|---|---|---|
| 1 | — | — | — |
| 2 | — | — | — |
| 3 | — | — | — |
| 4 | — | — | — |
| 5 | — | — | — |
