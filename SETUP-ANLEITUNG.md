# Setup-Anleitung — API-Verbindungen

## Schritt 1 — .env Datei erstellen

1. Kopiere `.env.example` und benenne die Kopie `.env`
2. Öffne `.env` und fülle die Werte aus (Anleitung unten)

---

## Schritt 2 — ActiveCampaign API-Key holen

1. Geh zu deinem ActiveCampaign-Account
2. Klick unten links auf **Einstellungen** (Zahnrad)
3. Wähle **Entwickler**
4. Dort siehst du:
   - **API-URL** → sieht aus wie `https://deinname.api-us1.com`
   - **API-Key** → langer Schlüssel aus Buchstaben und Zahlen
5. Kopiere beide in deine `.env` Datei:
   ```
   AC_API_URL=https://deinname.api-us1.com
   AC_API_KEY=abc123...
   ```

---

## Schritt 3 — Systeme.io API-Key holen

1. Geh zu deinem Systeme.io-Account
2. Klick oben rechts auf dein Profil → **Einstellungen**
3. Wähle **Öffentliche API**
4. Klick auf **API-Key generieren** (falls noch keiner vorhanden)
5. Kopiere den Key in deine `.env` Datei:
   ```
   SYSTEME_API_KEY=dein_key_hier
   ```

---

## Schritt 4 — Notion Integration erstellen

1. Geh zu **notion.so/my-integrations**
2. Klick auf **+ Neue Integration**
3. Name: "E-Mail-Marketing-Assistant"
4. Wähle deinen Workspace
5. Klick **Senden / Speichern**
6. Kopiere den **Internen Integrationstoken** (beginnt mit `secret_`)
7. Füge ihn in `.env` ein:
   ```
   NOTION_TOKEN=secret_abc123...
   ```

### Notion-Datenbank verbinden:
Für JEDE Notion-Datenbank die du nutzen willst:
1. Öffne die Datenbank in Notion
2. Klick oben rechts auf **...** → **Verbindungen**
3. Füge deine Integration hinzu
4. Kopiere die Datenbank-ID aus der URL:
   - URL sieht so aus: `notion.so/abc123def456...?v=...`
   - Die ID ist der Teil vor dem `?`: `abc123def456...`

---

## Schritt 5 — Verbindung testen

Führe das Test-Script aus:
```bash
python3 scripts/verbindung-testen.py
```

Du solltest sehen:
```
✅ ActiveCampaign: Verbunden! X Kontakte insgesamt
✅ Systeme.io: Verbunden!
✅ Notion: Verbunden als 'Dein Name'
```

---

## Schritt 6 — Erste Routine einrichten

Öffne Claude Code → Routines → Neue Routine erstellen
Verwende die Prompt-Dateien aus `.claude/routines/`:
- `weekly-ac-report.md` → Wöchentlich, Montag
- `morning-briefing.md` → Täglich, 08:00 Uhr
- `listenhygiene-check.md` → Wöchentlich, Sonntag
