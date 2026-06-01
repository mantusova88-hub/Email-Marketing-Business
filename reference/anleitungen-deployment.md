# Anleitung: Netlify + Systeme.io Deployment

---

## TEIL 1: Tool auf Netlify deployen (kostenlos, 5 Minuten)

### Was du brauchst
- Die Datei `outputs/nischengenerator.html`
- Einen kostenlosen Netlify-Account

### Schritt-für-Schritt

**Schritt 1 — Netlify-Account erstellen**
1. Gehe auf [netlify.com](https://netlify.com)
2. Klicke auf "Sign up" → mit Google oder E-Mail registrieren
3. Kostenloser Plan reicht vollständig aus

**Schritt 2 — Tool hochladen (Drag & Drop!)**
1. Nach dem Login siehst du das Netlify-Dashboard
2. Scrolle nach unten bis du siehst: *"Want to deploy a new site without connecting to Git? Drag and drop your site output folder here"*
3. Öffne den Ordner `outputs/` auf deinem Computer
4. Ziehe die Datei `nischengenerator.html` in dieses Feld
5. Netlify deployt automatisch — dauert 10 Sekunden!

**Schritt 3 — Eigenen Namen vergeben (optional)**
1. Nach dem Deploy siehst du eine automatische URL wie `random-words-12345.netlify.app`
2. Klicke auf "Site settings" → "Change site name"
3. Gib ein: z.B. `nischengenerator-mamas` → du bekommst `nischengenerator-mamas.netlify.app`

**Dein Tool ist jetzt live!** Teile diese URL mit deinen Kunden.

---

## TEIL 2: Claude API-Key einrichten

Damit das Tool funktioniert, braucht es einen Claude API-Key.

**Option A: Für deine eigene Nutzung**
1. Gehe auf [console.anthropic.com](https://console.anthropic.com)
2. Registrieren / einloggen
3. Links auf "API Keys" klicken
4. "Create Key" → Key kopieren (beginnt mit `sk-ant-...`)
5. Im Tool: ⚙️ unten rechts klicken → Key einfügen → Speichern

**Option B: Deine Kunden bringen ihren eigenen Key mit**
- Kunden bekommen die Netlify-URL nach dem Kauf
- Sie tragen einmalig ihren eigenen API-Key ein
- Vorteil: Du trägst keine API-Kosten für Kunden

**Option C: Du bezahlst die API-Kosten (Premium-Erlebnis)**
- Du baust ein Backend ein (technisch aufwändiger)
- Dann brauchen Kunden keinen eigenen API-Key
- Empfehlung: Erst mit Option B starten, später upgraden

---

## TEIL 3: Verkaufsseite in Systeme.io erstellen

### Was du bauen wirst
Eine einfache Verkaufsseite mit:
- Headline was das Tool ist
- Was es macht (Bullet Points)
- Kaufbutton mit Preis
- Nach dem Kauf: automatische E-Mail mit Netlify-Link

### Schritt-für-Schritt

**Schritt 1 — Neuen Funnel erstellen**
1. In Systeme.io: linkes Menü → "Funnels"
2. Klicke auf "+ Erstellen"
3. Name: "Nischengenerator" 
4. Funnel-Typ: "Verkauf eines Produkts"

**Schritt 2 — Verkaufsseite gestalten**
1. Klicke auf "Verkaufsseite bearbeiten"
2. Wähle ein Template (einfaches, cleanes Template)
3. Passe an:
   - **Headline:** "Finde deine perfekte Nische in 5 Minuten ✨"
   - **Subheadline:** "Der KI-Nischengenerator speziell für selbstständige Mamas"
   - **Bullet Points:**
     - ✅ 3 maßgeschneiderte Nischen-Vorschläge
     - ✅ Mit Marktpotenzial-Einschätzung
     - ✅ Passend zu deinen Stärken & Hobbys
     - ✅ Sofort loslegen — kein Download nötig
   - **Preis:** 7 € oder 17 €
   - **Kaufbutton:** "Jetzt meinen Nischengenerator kaufen →"

**Schritt 3 — Produkt verknüpfen**
1. Menü → "Produkte" → "+ Produkt erstellen"
2. Name: "Nischengenerator"
3. Preis: 7 € (oder dein Wunschpreis)
4. Produkt-Typ: "Digitales Produkt"

**Schritt 4 — Dankeseite / Zugang einrichten**
1. Nach dem Kauf-Seite bearbeiten
2. Text: "Dein Nischengenerator ist bereit! 🎉"
3. Link einfügen: deine Netlify-URL (z.B. `nischengenerator-mamas.netlify.app`)
4. ODER: Automatische E-Mail nach Kauf mit dem Link (empfohlen!)

**Schritt 5 — E-Mail nach Kauf automatisch versenden**
1. Im Funnel: "E-Mail-Sequenz" → hinzufügen
2. Auslöser: "Nach Kauf"
3. E-Mail schreiben:
   - Betreff: "Dein Nischengenerator ist bereit ✨"
   - Inhalt: Glückwunsch + Link + Hinweis zum API-Key

---

## Preisempfehlung

| Preis | Strategie |
|---|---|
| **7 €** | Impulskauf — maximale Reichweite, viele Verkäufe |
| **17 €** | Solider Preis für ein Tool mit Mehrwert |
| **27 €** | Wenn du zusätzlich eine Anleitung/Video beifügst |

---

## Checkliste vor dem Launch

- [ ] Tool auf Netlify deployen und testen
- [ ] API-Key einrichten und Funktion prüfen
- [ ] Verkaufsseite in Systeme.io fertigstellen
- [ ] Automatische E-Mail nach Kauf einrichten
- [ ] Testbestellung durchführen
- [ ] Preis festlegen
- [ ] Auf Instagram/Social Media ankündigen 🚀
