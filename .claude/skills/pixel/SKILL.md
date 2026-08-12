---
name: pixel
description: Meta Pixel auf Landingpages, Netlify-Seiten und Systeme.io einbauen und testen. Nutze diesen Skill bei "Pixel", "Meta Pixel", "Facebook Pixel", "Tracking", "Conversion messen", "Events einrichten", "Pixel testen", "Tracking funktioniert nicht".
---

# pixel — Meta Pixel einbauen

**Ohne Pixel kein Tracking. Ohne Tracking kein sinnvolles Ads-Budget.**
Meta kann dann nicht lernen, wer kauft — und Monika weiß nicht, was funktioniert.

---

## 1. Pixel-ID besorgen

1. [business.facebook.com](https://business.facebook.com) öffnen
2. Links im Menü auf **Events Manager**
3. **Datenquellen** → dein Pixel auswählen (oder **+ Datenquelle hinzufügen** → **Web**)
4. Die **Pixel-ID** kopieren — eine 15–16-stellige Zahl

Die ID gehört in `context/business-info.md`, damit sie nicht jedes Mal
gesucht werden muss.

---

## 2. Einbau in eine HTML-Seite (Netlify)

Der Code kommt in den `<head>`, **direkt vor `</head>`**:

```html
<!-- Meta Pixel Code -->
<script>
!function(f,b,e,v,n,t,s)
{if(f.fbq)return;n=f.fbq=function(){n.callMethod?
n.callMethod.apply(n,arguments):n.queue.push(arguments)};
if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';
n.queue=[];t=b.createElement(e);t.async=!0;
t.src=v;s=b.getElementsByTagName(e)[0];
s.parentNode.insertBefore(t,s)}(window,document,'script',
'https://connect.facebook.net/en_US/fbevents.js');
fbq('init', 'DEINE_PIXEL_ID');
fbq('track', 'PageView');
</script>
<noscript><img height="1" width="1" style="display:none"
src="https://www.facebook.com/tr?id=DEINE_PIXEL_ID&ev=PageView&noscript=1"
/></noscript>
<!-- End Meta Pixel Code -->
```

`DEINE_PIXEL_ID` an **beiden** Stellen ersetzen.

> ⚠️ **Wichtig für Monikas Seiten:** Der Pixel lädt von einer externen Domain.
> Auf Netlify ist das kein Problem. Bei Seiten mit strenger Content-Security-Policy
> muss `connect.facebook.net` erlaubt sein.

### In welche Dateien
Alle Seiten in `outputs/`, die beworben werden — Opt-in-Seiten,
Verkaufsseiten, Danke-Seiten. Ich kann das direkt einbauen.

---

## 3. Einbau in Systeme.io

1. **Einstellungen** (Zahnrad oben rechts) → **Tracking-Codes**
2. Feld **Header-Code** (`<head>`)
3. Kompletten Code von oben einfügen
4. **Speichern**

Alternativ pro Funnel-Seite: Seite bearbeiten → **Einstellungen** →
**Tracking-Codes** → Header.

---

## 4. Die wichtigen Events

`PageView` allein reicht nicht. Meta muss wissen, **was gut ist.**

### Lead — beim Eintragen ins Formular

Im Bestätigungs- oder Danke-Bereich:
```html
<script>fbq('track', 'Lead');</script>
```

Besser: direkt beim Absenden. Auf der **Danke-Seite** einbauen —
das ist der einfachste zuverlässige Weg.

### Purchase — beim Kauf

Auf der Danke-Seite nach dem Kauf:
```html
<script>
fbq('track', 'Purchase', {value: 7.00, currency: 'EUR'});
</script>
```

`value` an den echten Preis anpassen.

### ViewContent — auf der Verkaufsseite
```html
<script>fbq('track', 'ViewContent');</script>
```

Damit lässt sich später gezielt an Leute ausspielen, die die
Verkaufsseite gesehen, aber nicht gekauft haben.

---

## 5. Testen — Pflicht

**Nie ungetestet Geld ausgeben.**

### Variante A: Meta Pixel Helper
1. Chrome-Erweiterung **Meta Pixel Helper** installieren
2. Die eigene Seite aufrufen
3. Auf das Symbol klicken → grün + Pixel-ID sichtbar = korrekt

### Variante B: Events Manager
1. Events Manager → Pixel → **Testereignisse**
2. Eigene URL eingeben → **Website öffnen**
3. Die Seite normal durchklicken (eintragen, kaufen)
4. Events müssen live in der Liste erscheinen

**Checkliste:**
- [ ] PageView feuert auf allen Seiten
- [ ] Lead feuert nach dem Eintragen
- [ ] Purchase feuert nach dem Kauf, mit korrektem Betrag
- [ ] Keine doppelten Events (Pixel-Code nur einmal pro Seite!)

---

## 6. Häufige Fehler

| Problem | Ursache |
|---|---|
| Pixel feuert gar nicht | Code im `<body>` statt `<head>`, oder ID falsch |
| Events doppelt | Code zweimal eingebaut (z. B. global + pro Seite) |
| Lead wird nie gemessen | Danke-Seite fehlt oder leitet auf externe Domain |
| Purchase ohne Wert | `value` und `currency` vergessen |
| Nichts im Events Manager | Adblocker im eigenen Browser aktiv |

---

## 7. Datenschutz — nicht optional

In Deutschland ist der Meta Pixel **einwilligungspflichtig** (DSGVO/TTDSG).

Das bedeutet konkret:
- **Cookie-Banner** mit echter Wahlmöglichkeit — Pixel lädt erst nach „Zustimmen"
- **Datenschutzerklärung** muss den Meta Pixel und die Datenübermittlung
  in die USA benennen
- Kein vorangekreuztes Kästchen, ablehnen muss genauso leicht sein

> Das ist kein Rechtsrat. Für die Texte gibt es Anbieter für Rechtstexte
> (z. B. eRecht24, IT-Recht Kanzlei). Bei Unsicherheit dorthin verweisen —
> nicht selbst formulieren.

**Praktische Folge:** Ohne Einwilligung fehlen Daten. Deshalb misst der Pixel
in Deutschland typischerweise 20–40 % weniger als real passiert.
Das ist normal — die Zahlen sind trotzdem vergleichbar untereinander.
