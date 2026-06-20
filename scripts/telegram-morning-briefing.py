#!/usr/bin/env python3
"""
Telegram Morning Briefing Bot
Sendet jeden Morgen eine Wochenübersicht per Telegram — wie Julia's "Kalender & Mails" Bot.

Setup:
  1. .env ausfüllen (TELEGRAM_BOT_TOKEN + TELEGRAM_CHAT_ID)
  2. scripts/briefing-data.json anpassen
  3. Cron-Job einrichten: 0 8 * * 1 python3 /pfad/scripts/telegram-morning-briefing.py
"""

import json
import os
import sys
import urllib.request
import urllib.parse
import urllib.error
from datetime import datetime, timedelta
from pathlib import Path

# ---------------------------------------------------------------------------
# Konfiguration
# ---------------------------------------------------------------------------

BASE_DIR = Path(__file__).parent.parent
DATA_FILE = BASE_DIR / "scripts" / "briefing-data.json"
ENV_FILE = BASE_DIR / ".env"

def load_env():
    """Lädt Variablen aus .env-Datei."""
    env = {}
    if ENV_FILE.exists():
        for line in ENV_FILE.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                key, _, value = line.partition("=")
                env[key.strip()] = value.strip().strip('"').strip("'")
    return env

def load_data():
    """Lädt briefing-data.json."""
    if not DATA_FILE.exists():
        print(f"FEHLER: {DATA_FILE} nicht gefunden. Bitte briefing-data.json erstellen.")
        sys.exit(1)
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

# ---------------------------------------------------------------------------
# Systeme.io API (optionale Live-Daten)
# ---------------------------------------------------------------------------

def fetch_systemeio_subscribers(api_key: str) -> dict:
    """Ruft Subscriber-Zahlen von Systeme.io ab."""
    try:
        url = "https://api.systeme.io/api/contacts?itemsPerPage=1"
        req = urllib.request.Request(
            url,
            headers={"X-API-Key": api_key, "Accept": "application/json"},
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
            total = data.get("pagination", {}).get("totalItems", "?")
            return {"total": total}
    except Exception as e:
        print(f"Systeme.io Abruf fehlgeschlagen: {e}")
        return {"total": "?"}

# ---------------------------------------------------------------------------
# Datum & Kalender-Wochen-Helpers
# ---------------------------------------------------------------------------

def get_week_range(date: datetime) -> str:
    """Gibt 'DD.MM.–DD.MM.' für die aktuelle KW zurück."""
    monday = date - timedelta(days=date.weekday())
    sunday = monday + timedelta(days=6)
    return f"{monday.strftime('%d.%m.')}–{sunday.strftime('%d.%m.')}"

def get_kw(date: datetime) -> int:
    return date.isocalendar()[1]

def is_older_than_weeks(date_str: str, weeks: int = 2) -> bool:
    """Prüft ob ein ISO-Datum älter als X Wochen ist."""
    try:
        d = datetime.fromisoformat(date_str)
        return (datetime.now() - d).days > (weeks * 7)
    except Exception:
        return False

# ---------------------------------------------------------------------------
# Nachrichten-Aufbau
# ---------------------------------------------------------------------------

def build_message(data: dict, today: datetime, subscribers: dict) -> str:
    kw = get_kw(today)
    week_range = get_week_range(today)
    name = data.get("name", "")
    is_monday = today.weekday() == 0

    lines = []

    # Quick-Hinweis
    tipps = data.get("quick_tipps", [])
    if tipps:
        tipp = tipps[today.weekday() % len(tipps)]
        lines.append(f"**💡 Quick-Hinweis:** {tipp}")
        lines.append("")
        lines.append("---")
        lines.append("")

    # Wochen-Header
    lines.append(f"📋 Wochenübersicht KW {kw} — {week_range}")
    lines.append("")

    # Subscriber-Zahl (wenn verfügbar)
    if subscribers.get("total") and subscribers["total"] != "?":
        lines.append(f"📬 Aktuelle Subscriber: **{subscribers['total']}**")
        lines.append("")

    # Automatisch erledigt
    auto_done = data.get("automatisch_erledigt", [])
    if auto_done:
        lines.append("✅ **Heute schon automatisch erledigt:**")
        for item in auto_done:
            lines.append(f"• {item}")
        lines.append("")

    # Kommt heute noch
    heute_noch = data.get("heute_noch", {}).get(today.strftime("%A").lower(), [])
    if heute_noch:
        lines.append("⏰ **Kommt heute noch:**")
        for item in heute_noch:
            lines.append(f"• {item['zeit']} — {item['aufgabe']}")
        lines.append("")

    # Prüfen & freigeben
    pruefen = data.get("pruefen_freigeben", [])
    if pruefen:
        lines.append("👀 **Bitte prüfen & freigeben:**")
        for item in pruefen:
            lines.append(f"• {item}")
        lines.append("")

    # Offene Loops (älter als 2 Wochen)
    alle_loops = data.get("offene_loops", [])
    alte_loops = [
        loop for loop in alle_loops
        if is_older_than_weeks(loop.get("seit", ""), weeks=2)
    ]
    if alte_loops:
        lines.append("⚠️ **Offene Loops (älter als 2 Wochen — bitte entscheiden):**")
        for loop in alte_loops:
            lines.append(f"• {loop['titel']}")
        lines.append("")

    # Wochenfokus (nur montags oder wenn immer anzeigen)
    fokus = data.get("diese_woche_fokus", [])
    if fokus and (is_monday or data.get("fokus_taeglich", False)):
        lines.append("🎯 **Diese Woche im Fokus:**")
        for item in fokus:
            lines.append(f"• {item}")
        lines.append("")

    # Abschluss
    lines.append(f"Viel Erfolg in die neue Woche, {name} 💪")

    return "\n".join(lines)

# ---------------------------------------------------------------------------
# Telegram senden
# ---------------------------------------------------------------------------

def send_telegram(bot_token: str, chat_id: str, text: str) -> bool:
    """Sendet Nachricht via Telegram Bot API."""
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = json.dumps({
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown",
    }).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            result = json.loads(resp.read())
            return result.get("ok", False)
    except urllib.error.HTTPError as e:
        print(f"Telegram-Fehler {e.code}: {e.read().decode()}")
        return False
    except Exception as e:
        print(f"Telegram-Verbindungsfehler: {e}")
        return False

# ---------------------------------------------------------------------------
# Hauptprogramm
# ---------------------------------------------------------------------------

def main():
    env = load_env()
    data = load_data()
    today = datetime.now()

    # Systeme.io Daten (optional)
    systemeio_key = env.get("SYSTEMEIO_API_KEY", "")
    subscribers = fetch_systemeio_subscribers(systemeio_key) if systemeio_key else {"total": None}

    # Nachricht aufbauen
    message = build_message(data, today, subscribers)

    # Ausgabe im Terminal (zum Testen)
    print("=" * 50)
    print(message)
    print("=" * 50)

    # Telegram senden
    bot_token = env.get("TELEGRAM_BOT_TOKEN", "")
    chat_id = env.get("TELEGRAM_CHAT_ID", "")

    if not bot_token or not chat_id:
        print("\nHINWEIS: TELEGRAM_BOT_TOKEN und TELEGRAM_CHAT_ID in .env eintragen.")
        print("Nachricht wurde NICHT gesendet (nur Terminal-Ausgabe).")
        return

    success = send_telegram(bot_token, chat_id, message)
    if success:
        print(f"\nNachricht erfolgreich gesendet an Chat {chat_id}")
    else:
        print("\nFEHLER: Nachricht konnte nicht gesendet werden.")
        sys.exit(1)

if __name__ == "__main__":
    main()
