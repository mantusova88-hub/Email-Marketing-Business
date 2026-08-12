---
name: newsletter-schreiben
description: >-
  "Newsletter", "Newsletter schreiben", "E-Mail an meine Liste",
  "Mail an die Liste", "Kampagne", "Betreffzeile", "Preheader", "Broadcast".
  Nutze diesen Skill IMMER wenn "Newsletter", "Newsletter schreiben",
  "Mail an meine Liste" oder "Betreffzeile" gesagt wird.
  Liefert IMMER 3 Betreffzeilen + 1 Preheader + 1 vollständigen Newsletter
  passend zum genannten Thema.
---

# Newsletter-Skill

Generiert fertige Newsletter für deine E-Mail-Liste — in deiner Stimme, sofort
copy-paste-fähig für dein E-Mail-Tool. Der Skill ist eigenständig: Fülle einmal
den Abschnitt "Dein Business" aus, dann treffen die Newsletter deine Zielgruppe.

---

## So findet der Skill dein Business-Wissen (in dieser Reihenfolge)

1. **Eigene Definition vorhanden?** Prüfe zuerst, ob schon eine eigene Quelle
   existiert — z.B. `context/business-info.md`, `context/personal-info.md`,
   `context/strategy.md`, `zielgruppe.md` / `brand-voice.md` / `marke.md`
   oder ein Abschnitt in einer `CLAUDE.md`. **Falls ja: bevorzugt nutzen.**
2. **Sonst:** der ausgefüllte Abschnitt "Dein Business" unten.
3. **Noch nicht ausgefüllt?** Den Nutzer **einmalig** nach Zielgruppe,
   Schmerzpunkten, Einwänden und Tonalität fragen und die Antworten hier eintragen.

---

## Dein Business — HIER AUSFÜLLEN

> Ersetze jeden Platzhalter `[…]`. Löschen, was nicht passt.

### Zielgruppe
- **Wunschkundin (kurz):** [z.B. selbständige Mamas, die ihr Business neben der Familie aufbauen]
- **Die 3 größten Schmerzpunkte:** [in ihrer eigenen Sprache]
  1. [Schmerzpunkt 1]
  2. [Schmerzpunkt 2]
  3. [Schmerzpunkt 3]
- **Häufigste Einwände (+ Antwort):**
  - "[z.B. Ich habe keine Zeit für Newsletter]" → [Entkräftung]
  - "[z.B. Ich habe niemandem etwas zu sagen]" → [Entkräftung]
- **Lesesituation:** [z.B. am Handy, zwischen Tür und Angel, abends nach dem Zubettbringen]

### Stimme
- **Anrede:** [du / Sie / ihr]
- **Tonalität in 3–5 Worten:** [z.B. warmherzig, ermutigend, auf Augenhöhe]
- **Meine No-Gos:** [z.B. Fachjargon, künstliche Verknappung, Hustle-Rhetorik]
- **Absender-Name:** [Name]
- **Signatur:** [z.B. "Von Mama zu Mama, [Name]"]

### Angebot & Links
- **Hauptangebot:** [Kurs / Coaching / Produkt]
- **Link zum Angebot:** [URL]
- **Link zum Kennenlern-Gespräch:** [URL]
- **Branding:** Burgund `#800220`, Gold `#B59156`

---

# Standard-Output (IMMER alle drei Blöcke liefern)

Bei "Newsletter über [Thema]" → IMMER ohne Nachfragen:

### Block 1 — 3 Betreffzeilen
Je 30–50 Zeichen, jeweils aus einem anderen Muster:
1. **Neugier** — „Der Fehler, den ich 2 Jahre lang gemacht habe"
2. **Konkreter Nutzen** — „In 15 Minuten zur ersten Willkommens-Mail"
3. **Persönlich / Story** — „Gestern hat mein Sohn meinen Launch gerettet"

### Block 2 — 1 Preheader
60–90 Zeichen. Verstärkt die Neugier, wiederholt den Betreff **nicht**.

### Block 3 — 1 vollständiger Newsletter
Nach dem 7-Bausteine-Aufbau unten, 250–400 Wörter, fertig zum Kopieren.

**Zusätzlich:** Ablegen unter `outputs/newsletter/JJJJ-MM-TT-thema.md`.

Wenn Angaben aus "Dein Business" fehlen: trotzdem liefern, dann am Ende **einen**
kurzen Hinweis, welche Angabe den Newsletter besser machen würde.

---

## Newsletter-Struktur

Jeder Newsletter folgt diesem Aufbau:

| # | Baustein | Länge | Zweck |
|---|---|---|---|
| 1 | Betreffzeile | 30–50 Zeichen | Öffnen lassen |
| 2 | Preheader | 60–90 Zeichen | Neugier verstärken |
| 3 | Persönlicher Einstieg | 2–4 Sätze | Andocken: eine Szene, ein Gefühl |
| 4 | Das Thema | 150–300 Wörter | Ein einziger Gedanke, klar erklärt |
| 5 | Konkreter Tipp | 3–5 Sätze | Heute in 10 Minuten umsetzbar |
| 6 | Call-to-Action | 1–2 Sätze | Genau EINE Handlung |
| 7 | Abschluss | 1–2 Sätze | Warm, persönlich, mit Namen |

### Das Gerüst

```
[EINSTIEG — eine konkrete Szene aus deinem Alltag, 2–4 Sätze.
Zeit, Ort, was du gerade getan hast. Keine Verallgemeinerung.]

[WENDEPUNKT — der eine Satz, an dem dir etwas klar wurde.
Steht allein als eigener Absatz.]

[THEMA — der eine Gedanke, 150–300 Wörter.
Erst die Einsicht, dann das Warum, dann ein Bild oder Vergleich,
der es greifbar macht. Kein zweites Thema.]

**Dein Schritt für heute:** [KONKRETER TIPP — was sie heute in
10 Minuten tun kann. Eine Handlung, kein Programm.]

[CALL-TO-ACTION — als Einladung, 1–2 Sätze.
Genau EINE Handlung: antworten ODER klicken. Nie beides.]

[SIGNATUR aus "Dein Business"]
```

### 3 verschiedene Angles für die 3 Betreffzeilen (immer mischen)

Nie drei Varianten desselben Satzes. Wähle **drei verschiedene** aus dieser Liste —
Angle 1 (Neugier) ist immer dabei, die beiden anderen passend zum Thema:

1. **Neugier-Angle** — offene Schleife oder Widerspruch
   „Meine erste Mail ging ohne Website raus"
2. **Zeit-/Effizienz-Angle** — knappe Zeit als Aufhänger
   „In 15 Minuten zur ersten Willkommens-Mail"
3. **Story-Angle** — eine Szene oder Person
   „Gestern hat mein Sohn meinen Launch gerettet"
4. **„Ich kann das nicht"-Angle** — hebt den Anfängerinnen-Einwand auf
   „Du brauchst kein Technik-Talent dafür"
5. **Fehler-/Umkehr-Angle** — was die meisten falsch machen
   „Der Fehler, den ich 2 Jahre lang gemacht habe"
6. **Zahlen-Angle** — ein konkretes Ergebnis
   „Von 40 auf 300 Subscriber in 90 Tagen"

**Regel:** Die gewählten Angles müssen sich im *Ansatz* unterscheiden, nicht nur
in der Formulierung. Zwei Betreffzeilen mit demselben Angle sind ein Fehler.

---

## Regeln

1. **Ein Newsletter = ein Thema = ein Call-to-Action.** Zwei Themen → zwei Newsletter.
2. **250–400 Wörter.** Lieber zu kurz als zu lang.
3. **Absätze maximal 3 Zeilen** — wird am Handy gelesen.
4. **Kein Fachjargon ohne Erklärung** („Funnel", „Lead Magnet", „Conversion").
5. **Keine Spam-Trigger** im Betreff: „gratis", „garantiert", „100 %", „Jetzt kaufen".
   Maximal ein Emoji, oft besser gar keins. Kein CAPS LOCK.
6. **Der Betreff muss halten, was die Mail liefert.** Sonst leidet die Öffnungsrate langfristig.
7. **CTA als Einladung, nicht als Befehl.** Die Beziehung ist wichtiger als der einzelne Klick.
8. **Kein Druck, keine künstliche Verknappung, keine Perfektions-Rhetorik.**

---

## Stil-Regeln (nicht verhandelbar)

### Erlaubt + erwünscht
- Längere Sätze mit Haupt- und Nebensätzen — es soll gesprochen klingen
- Persönliche Story-Hooks („Vor 2 Jahren habe ich…", „Neulich saß ich…")
- Konkrete Zahlen und echte Beispiele statt vager Versprechen
- Direkte Ansprache (gemäß deiner Angabe unter „Stimme")
- Ein klarer Call-to-Action, als Einladung formuliert
- Emojis sparsam — im Fließtext eines Newsletters eher nicht, im Betreff maximal eins

### Verboten
- „Hier ist, was…" / „Hier ist die…" (KI-Floskel)
- „Nicht weil X, sondern weil Y." (KI-Floskel)
- „Lass uns eintauchen", „In der heutigen schnelllebigen Welt" (KI-Floskeln)
- „easy peasy", Buzzwords ohne Substanz
- Übertriebene Versprechen („verdopple dein Einkommen in 7 Tagen")
- **Stakkato-Sätze. Kurz. Wie. Das.**
- `ae` / `oe` / `ue` / `ss` im Fließtext — echte Umlaute und ß nutzen
- **Features oder Konditionen frei erfinden** (z.B. „lebenslanger Zugriff",
  „jederzeit kündbar", „Geld-zurück-Garantie"), die nicht wirklich existieren.
  Im Zweifel weglassen oder einmal nachfragen.
- Preise, Termine, Zahlen oder Teilnehmerzahlen erfinden — dasselbe Prinzip

### Checkliste vor der Ausgabe
- [ ] Nur ein Thema, nur ein Call-to-Action?
- [ ] Unter 400 Wörtern?
- [ ] Alle Absätze maximal 3 Zeilen?
- [ ] Kein unerklärter Fachjargon?
- [ ] Keine KI-Floskel aus der Verboten-Liste drin?
- [ ] Keine Zahl, kein Preis, kein Feature erfunden?
- [ ] Betreff hält, was die Mail liefert?
- [ ] Klingt es wie ein Mensch, der einer Freundin schreibt?

---

## Beispiel

**Eingabe:** „Schreib mir einen Newsletter darüber, dass man nicht auf die perfekte Website warten muss, um mit E-Mail-Marketing zu starten."

**Ausgabe:**

**Betreffzeilen**
1. *(Neugier)* Meine erste Mail ging ohne Website raus
2. *(Nutzen)* Starten ohne Website — so geht's
3. *(Story)* 2 Jahre gewartet. Auf nichts.

**Preheader**
Du brauchst weniger, als du denkst — versprochen.

**Newsletter**

Neulich saß ich um kurz nach zehn am Küchentisch. Die Kinder endlich im Bett, der Laptop auf, und ich habe wieder an meiner Website herumgeschraubt.

Zum gefühlt hundertsten Mal.

Und dann ist mir aufgefallen: Ich hatte in zwei Jahren keine einzige E-Mail an meine Liste geschickt. Weil die Website ja noch nicht fertig war.

Die Wahrheit ist: Deine Leserinnen sehen deine Website vielleicht einmal. Deine E-Mails sehen sie jede Woche. Die Website ist das Schaufenster — deine E-Mails sind das Gespräch. Und das Gespräch verkauft.

Was du wirklich brauchst, um zu starten: eine E-Mail-Adresse, ein Anmeldeformular und etwas, das du zu sagen hast. Das war's.

**Dein Schritt für heute:** Öffne dein E-Mail-Tool und schreib eine einzige Mail an deine Liste. Erzähl, woran du gerade arbeitest. Drei Absätze reichen. Nicht schön machen — abschicken.

Wenn du magst, antworte mir kurz und erzähl mir, worüber du geschrieben hast. Ich lese jede Antwort.

Von Mama zu Mama,
[Name]

---

## Was gut funktioniert hat

<!-- Nach jedem Versand eintragen. Der Skill wird dadurch mit jedem
     Newsletter besser — das ist der eigentliche Hebel. -->

| Datum | Betreff | Öffnungsrate | Was war anders? |
|---|---|---|---|
| — | — | — | — |
