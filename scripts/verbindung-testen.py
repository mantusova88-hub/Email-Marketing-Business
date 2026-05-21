#!/usr/bin/env python3
"""
Testet alle API-Verbindungen auf einmal.
Ausführen: python3 scripts/verbindung-testen.py
"""

import os
import sys

def load_env():
    """Lädt .env Datei manuell (ohne externe Abhängigkeiten)."""
    env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
    if not os.path.exists(env_path):
        print("❌ Keine .env Datei gefunden!")
        print("   → Kopiere .env.example zu .env und fülle die Werte aus")
        sys.exit(1)
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ.setdefault(key.strip(), value.strip())

def test_activecampaign():
    """Testet die ActiveCampaign-Verbindung."""
    try:
        import urllib.request
        import json

        url = os.environ.get('AC_API_URL', '').rstrip('/')
        key = os.environ.get('AC_API_KEY', '')

        if not url or not key or 'DEIN' in url or 'DEIN' in key:
            print("⚠️  ActiveCampaign: Noch nicht konfiguriert")
            return False

        req = urllib.request.Request(
            f"{url}/api/3/contacts?limit=1",
            headers={'Api-Token': key}
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
            count = data.get('meta', {}).get('total', '?')
            print(f"✅ ActiveCampaign: Verbunden! {count} Kontakte insgesamt")
            return True
    except Exception as e:
        print(f"❌ ActiveCampaign: Fehler — {e}")
        return False

def test_systeme():
    """Testet die Systeme.io-Verbindung."""
    try:
        import urllib.request
        import json

        key = os.environ.get('SYSTEME_API_KEY', '')

        if not key or 'DEIN' in key:
            print("⚠️  Systeme.io: Noch nicht konfiguriert")
            return False

        req = urllib.request.Request(
            "https://api.systeme.io/api/contacts?limit=1",
            headers={'X-API-Key': key, 'Accept': 'application/json'}
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
            count = data.get('totalItems', '?')
            print(f"✅ Systeme.io: Verbunden! {count} Kontakte insgesamt")
            return True
    except Exception as e:
        print(f"❌ Systeme.io: Fehler — {e}")
        return False

def test_notion():
    """Testet die Notion-Verbindung."""
    try:
        import urllib.request
        import json

        token = os.environ.get('NOTION_TOKEN', '')

        if not token or 'DEIN' in token:
            print("⚠️  Notion: Noch nicht konfiguriert")
            return False

        req = urllib.request.Request(
            "https://api.notion.com/v1/users/me",
            headers={
                'Authorization': f'Bearer {token}',
                'Notion-Version': '2022-06-28'
            }
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read())
            name = data.get('name', 'Unbekannt')
            print(f"✅ Notion: Verbunden als '{name}'")
            return True
    except Exception as e:
        print(f"❌ Notion: Fehler — {e}")
        return False

if __name__ == '__main__':
    print("=" * 50)
    print("   API-Verbindungstest")
    print("=" * 50)
    load_env()
    test_activecampaign()
    test_systeme()
    test_notion()
    print("=" * 50)
    print("Fertig! ⬆️  Grüne Haken = bereit für Routinen")
