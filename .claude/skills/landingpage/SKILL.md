---
name: landingpage
description: Landingpages, Opt-in-Seiten und Verkaufsseiten bauen — Struktur, Texte und fertiges HTML. Nutze diesen Skill bei "Landingpage", "Verkaufsseite", "Salespage", "Opt-in-Seite", "Freebie-Seite", "Bestellseite", "Seite bauen". Kennt Monikas Branding und die Systeme.io/Netlify-Strecke.
---

# landingpage — Seiten, die konvertieren

**Immer zuerst lesen:** `context/stimme.md` und Skill `zielgruppe`.

---

## 1. Erst klären: welcher Seitentyp?

| Typ | Ziel | Länge |
|---|---|---|
| **Opt-in-Seite** | E-Mail-Adresse für ein Freebie | kurz — eine Bildschirmhöhe |
| **Verkaufsseite** | Kauf eines Produkts | lang — alle Einwände auflösen |
| **Danke-Seite** | Bestätigen + nächster Schritt | sehr kurz |

> **Wichtigste Regel:** Eine Seite, ein Ziel, ein Button-Text.
> Keine Navigation. Keine Links, die wegführen. Kein „mehr über mich".

---

## 2. Opt-in-Seite — Pflicht-Struktur

```
1. Überschrift      → Das Ergebnis in einem Satz
2. Unterüberschrift → Für wen + wie schnell
3. Bild             → Das Freebie sichtbar machen (Mockup)
4. 3 Bullet Points  → Was genau drin ist
5. Formular         → NUR E-Mail. Vorname optional.
6. Button           → Ergebnis-orientiert, nicht "Absenden"
7. Vertrauenszeile  → "Kein Spam. Jederzeit abmeldbar."
```

**Alles davon über der Falz** (ohne Scrollen sichtbar) — am **Handy**.

### Button-Texte
✅ „Ja, ich will den Guide" · „Schick mir die Checkliste" · „Kostenlos herunterladen"
❌ „Absenden" · „Anmelden" · „Eintragen" · „Jetzt starten"

---

## 3. Verkaufsseite — Pflicht-Sektionen

In dieser Reihenfolge:

| # | Sektion | Inhalt |
|---|---|---|
| 1 | **Headline** | Das Ergebnis, konkret. Nicht der Produktname. → Skill `hooks` |
| 2 | **Subheadline** | Für wen + in welcher Zeit + ohne was |
| 3 | **Problem** | So beschreiben, dass sie denkt „das bin ich" |
| 4 | **Wendepunkt** | „Es liegt nicht an dir. Es liegt daran, dass…" |
| 5 | **Lösung** | Das Produkt vorstellen — was es IST |
| 6 | **Inhalt** | Was genau drin ist, als Liste mit Nutzen je Punkt |
| 7 | **Für wen / nicht für wen** | Schafft Vertrauen durch Abgrenzung |
| 8 | **Über Monika** | Kurz. Warum ausgerechnet sie. Mama-Bezug. |
| 9 | **Testimonials** | Wenn vorhanden. Andere Mamas > Experten. |
| 10 | **Preis** | Klar, ohne Versteckspiel. Wert einordnen. |
| 11 | **FAQ** | Die Einwände aus Skill `zielgruppe` auflösen |
| 12 | **Letzter CTA** | Zusammenfassung + Button |

**CTA-Buttons:** nach Sektion 6, nach 10 und nach 12. Immer **derselbe Text**.

---

## 4. Die No-Gos

| ❌ Nie | Warum |
|---|---|
| Falsche Verknappung („nur noch 3 Plätze") | Sabine ist misstrauisch, riecht das sofort |
| Countdown, der beim Neuladen neu startet | Zerstört Vertrauen komplett |
| Einkommensversprechen | Unseriös + rechtlich riskant |
| „Ganz einfach!" / „Kinderleicht!" | Trigger-Wörter — erzeugen Scham |
| Fremdwörter-Marketing (Conversion, Funnel-Stack) | Ihre Zielgruppe steigt aus |
| Wall of Text | Sie liest am Handy |
| Mehrere Angebote auf einer Seite | Verwirrung tötet Verkäufe |
| Erfundene Testimonials | Nicht verhandelbar |

---

## 5. Technisch

### Monikas Strecke (bereits etabliert)
- **HTML-Seiten & Tools** → Netlify (`outputs/*.html`, siehe `reference/anleitungen-deployment.md`)
- **Verkauf & Zahlung** → Systeme.io (siehe `reference/systeme-io-verkaufsseite.md`)
- **E-Mail-Einsammeln** → Wild Mail

### Beim HTML-Bauen
- **Mobile first.** Über 80 % der Zielgruppe liest am Handy.
- Branding: Burgund `#800220`, Gold `#B59156`
- Schriftgröße Fließtext: mind. 17px
- Buttons: mind. 48px hoch (Daumen-tauglich)
- Alles in **eine** HTML-Datei — keine externen Abhängigkeiten
- In `outputs/` speichern, dann per Drag & Drop auf Netlify

### Bestehende Beispiele als Vorlage
`outputs/checkliste-business-start.html`, `outputs/nischengenerator.html`,
`outputs/mailerlite-setup-guide.html`

---

## 6. Ausgabeformat

Bei reinen Texten:

```markdown
# Verkaufsseite: [Produkt]

## Headline
## Subheadline
## Sektion 3: Problem
[…alle Sektionen mit fertigem Text…]

## Button-Text
## FAQ
```

Bei HTML: fertige Datei in `outputs/[name].html` + kurze Deploy-Anleitung.

---

## 7. Check vor der Ausgabe

- [ ] Ein Ziel, ein Button-Text?
- [ ] Am Handy ohne Scrollen: Headline + Button sichtbar?
- [ ] Alle Einwände aus `zielgruppe` beantwortet?
- [ ] Kein No-Go aus Abschnitt 4 drin?
- [ ] Klingt es nach `context/stimme.md` — oder nach Verkaufsseiten-Deutsch?
- [ ] Impressum & Datenschutz verlinkt? (Pflicht in Deutschland!)
