# Telegram Morning Briefing — Einrichtung

So richtest du dein persönliches "Kalender & Mails"-Bot ein.

---

## Schritt 1: Telegram Bot erstellen

1. Öffne Telegram und suche nach **@BotFather**
2. Schreibe `/newbot`
3. Wähle einen Namen, z.B. `Monika Business Bot`
4. Wähle einen Username, z.B. `monika_business_bot`
5. BotFather schickt dir einen **Token** — den brauchst du gleich

---

## Schritt 2: Deine Chat-ID herausfinden

1. Schreibe deinem neuen Bot irgendeine Nachricht
2. Öffne im Browser:
   ```
   https://api.telegram.org/bot[DEIN_TOKEN]/getUpdates
   ```
3. Suche nach `"chat":{"id":` — das ist deine **Chat-ID**

---

## Schritt 3: .env ausfüllen

Öffne die `.env`-Datei im Hauptordner und trage ein:

```env
TELEGRAM_BOT_TOKEN=1234567890:ABCdef...
TELEGRAM_CHAT_ID=987654321
SYSTEMEIO_API_KEY=dein-systeme-io-key  # optional, für Live-Subscriber-Zahlen
```

**Systeme.io API-Key** findest du unter:
Systeme.io → Einstellungen → API-Schlüssel

---

## Schritt 4: Briefing-Daten anpassen

Bearbeite `scripts/briefing-data.json`:

| Feld | Was du einträgst |
|---|---|
| `name` | Dein Vorname |
| `quick_tipps` | 7 tägliche Motivations-Tipps (Mo–So) |
| `automatisch_erledigt` | Was deine Automatisierungen täglich erledigen |
| `heute_noch` | Geplante Aufgaben nach Wochentag |
| `pruefen_freigeben` | Items die deine Freigabe brauchen |
| `offene_loops` | Aufgaben die schon länger offen sind (mit `seit`-Datum) |
| `diese_woche_fokus` | Deine 2–3 Top-Prioritäten diese Woche |

---

## Schritt 5: Testen

```bash
python3 scripts/telegram-morning-briefing.py
```

Die Nachricht wird im Terminal angezeigt. Wenn `.env` ausgefüllt ist, wird sie auch per Telegram geschickt.

---

## Schritt 6: Automatisch jeden Morgen senden

### Mac (Terminal):
```bash
crontab -e
```
Dann eintragen:
```
0 8 * * * /usr/bin/python3 /pfad/zu/Email-Marketing-Business/scripts/telegram-morning-briefing.py
```

### Windows (Task Planer):
1. Öffne "Aufgabenplanung"
2. Neue Aufgabe → täglich um 08:00
3. Aktion: `python scripts\telegram-morning-briefing.py`

---

## Offene Loops aktualisieren

Wenn du einen Loop erledigt hast, entferne ihn einfach aus der Liste in `briefing-data.json`. Neue Loops ergänzt du mit dem heutigen Datum:

```json
{
  "titel": "Neue offene Aufgabe beschreiben",
  "seit": "2026-05-31"
}
```

Loops älter als 14 Tage erscheinen automatisch im Abschnitt "Offene Loops ⚠️".

---

## Beispiel-Ausgabe

```
💡 Quick-Hinweis: Montag = Strategie-Tag: Plane die Woche, bevor der Alltag startet.

---

📋 Wochenübersicht KW 22 — 01.06.–07.06.

📬 Aktuelle Subscriber: 347

✅ Heute schon automatisch erledigt:
• Willkommens-Sequenz läuft automatisch für neue Subscriber
• Wild Mail hat Inbox gecheckt (Team-Adresse)

⏰ Kommt heute noch:
• 09:00 — Wochenplan durchgehen & Prioritäten setzen
• 10:00 — Newsletter-Thema für diese Woche festlegen

👀 Bitte prüfen & freigeben:
• Newsletter-Entwurf diese Woche — Betreffzeile prüfen
• Starter-Guide Landing Page — Opt-in-Formular testen

⚠️ Offene Loops (älter als 2 Wochen — bitte entscheiden):
• Testimonials von Kundinnen anfragen — noch 3 ausstehend

🎯 Diese Woche im Fokus:
• Subscriber-Wachstum: Freebie auf Instagram bewerben
• Öffnungsrate verbessern: 3 neue Betreffzeilen testen

Viel Erfolg in die neue Woche, Monika 💪
```
