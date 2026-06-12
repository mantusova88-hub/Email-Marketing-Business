#!/usr/bin/env python3
"""
Setup-Script: Zugangsdaten einrichten & testen
================================================
Dieses Script führt dich durch die Einrichtung und
testet ob alles funktioniert — einfach ausführen!

Ausführen: python3 scripts/setup_zugangsdaten.py
"""

import os
import requests
import sys

def check_env_file():
    """Prüft ob .env Datei existiert und hilft beim Erstellen."""
    env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
    env_path = os.path.normpath(env_path)

    if not os.path.exists(env_path):
        print("\n📋 Keine .env Datei gefunden.")
        print("   Kopiere .env.example zu .env und fülle die Werte aus Notion ein.")
        print(f"   Pfad: {env_path}")
        return False

    # .env Datei laden
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ[key.strip()] = value.strip()
    return True


def test_meta_token():
    """Testet den Meta Access Token und findet Instagram Account ID."""
    token = os.environ.get('META_ACCESS_TOKEN', '')

    if not token or token == 'dein_access_token_hier':
        print("❌ META_ACCESS_TOKEN nicht gesetzt")
        return None, None

    print("\n🔍 Teste Meta Access Token...")
    r = requests.get(
        "https://graph.facebook.com/v19.0/me",
        params={"fields": "id,name", "access_token": token}
    )
    data = r.json()

    if "error" in data:
        print(f"❌ Token ungültig: {data['error'].get('message', '')}")
        print("   → Neuen Token im Graph API Explorer generieren")
        return None, None

    print(f"✅ Token gültig! Verbunden als: {data.get('name', 'Unbekannt')}")
    print(f"   Facebook User ID: {data.get('id', '')}")

    # Instagram Business Account ID suchen
    print("\n🔍 Suche Instagram Business Account...")
    ig_id = find_instagram_id(token)
    return token, ig_id


def find_instagram_id(token):
    """Versucht die Instagram Business Account ID zu finden."""

    # Versuch 1: Über Facebook Pages
    r = requests.get(
        "https://graph.facebook.com/v19.0/me/accounts",
        params={"access_token": token}
    )
    pages = r.json().get("data", [])

    for page in pages:
        page_id = page["id"]
        page_token = page.get("access_token", token)
        r2 = requests.get(
            f"https://graph.facebook.com/v19.0/{page_id}",
            params={"fields": "instagram_business_account,name", "access_token": page_token}
        )
        d = r2.json()
        if "instagram_business_account" in d:
            ig_id = d["instagram_business_account"]["id"]
            print(f"✅ Instagram ID gefunden über Seite '{d.get('name', '')}'")
            print(f"   Instagram Business Account ID: {ig_id}")

            # In .env Datei speichern
            save_instagram_id(ig_id)
            return ig_id

    # Versuch 2: Direkt über User
    r3 = requests.get(
        "https://graph.facebook.com/v19.0/me/instagram_accounts",
        params={"access_token": token}
    )
    accounts = r3.json().get("data", [])
    if accounts:
        ig_id = accounts[0]["id"]
        print(f"✅ Instagram ID direkt gefunden: {ig_id}")
        save_instagram_id(ig_id)
        return ig_id

    print("⚠️  Instagram Business Account ID nicht automatisch gefunden")
    print("   → Füge 'pages_show_list' Permission zum Token hinzu")
    print("   → Oder trage die ID manuell in .env ein")
    return None


def save_instagram_id(ig_id):
    """Speichert Instagram ID in .env Datei."""
    env_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '.env'))
    if not os.path.exists(env_path):
        return

    with open(env_path, 'r') as f:
        content = f.read()

    if 'INSTAGRAM_BUSINESS_ACCOUNT_ID=' in content:
        lines = content.split('\n')
        new_lines = []
        for line in lines:
            if line.startswith('INSTAGRAM_BUSINESS_ACCOUNT_ID='):
                new_lines.append(f'INSTAGRAM_BUSINESS_ACCOUNT_ID={ig_id}')
            else:
                new_lines.append(line)
        with open(env_path, 'w') as f:
            f.write('\n'.join(new_lines))
        print(f"   💾 ID automatisch in .env gespeichert!")


def test_canva():
    """Testet die Canva Credentials."""
    client_id = os.environ.get('CANVA_CLIENT_ID', '')
    client_secret = os.environ.get('CANVA_CLIENT_SECRET', '')

    if not client_id or client_id == 'deine_canva_client_id_hier':
        print("\n❌ CANVA_CLIENT_ID nicht gesetzt")
        return False

    print(f"\n✅ Canva Client ID: {client_id[:8]}...****")
    print(f"   Canva Client Secret: ****")
    print("   ℹ️  Canva OAuth wird beim ersten Karussell-Post gestartet")
    return True


def main():
    print("=" * 50)
    print("  Setup & Test — Instagram Automatisierung")
    print("=" * 50)

    # .env laden
    if not check_env_file():
        print("\n👉 NÄCHSTER SCHRITT:")
        print("   1. Kopiere .env.example zu .env")
        print("   2. Öffne .env und trage deine Zugangsdaten aus Notion ein")
        print("   3. Führe dieses Script erneut aus")
        sys.exit(1)

    # Tests durchführen
    token, ig_id = test_meta_token()
    canva_ok = test_canva()

    # Zusammenfassung
    print("\n" + "=" * 50)
    print("  ZUSAMMENFASSUNG")
    print("=" * 50)
    print(f"Meta Token:        {'✅' if token else '❌'}")
    print(f"Instagram Account: {'✅ ' + ig_id if ig_id else '⚠️  Nicht gefunden'}")
    print(f"Canva API:         {'✅' if canva_ok else '❌'}")

    if token and ig_id and canva_ok:
        print("\n🎉 ALLES BEREIT! Du kannst jetzt Karussells automatisch posten!")
        print("   Ausführen: python3 scripts/instagram_karussell_automatisierung.py")
    else:
        print("\n⚠️  Einige Zugangsdaten fehlen noch.")
        print("   Öffne .env und ergänze die fehlenden Werte aus Notion.")


if __name__ == "__main__":
    main()
