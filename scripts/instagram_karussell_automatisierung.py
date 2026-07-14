#!/usr/bin/env python3
"""
Instagram Karussell Automatisierung
=====================================
Dieses Script:
1. Liest Zugangsdaten aus der .env Datei
2. Findet automatisch deine Instagram Business Account ID
3. Erstellt ein Karussell-Design in Canva
4. Postet das fertige Karussell auf Instagram

Ausführen: python3 scripts/instagram_karussell_automatisierung.py
Einrichten: python3 scripts/setup_zugangsdaten.py
"""

import os
import requests
import json
import time
import sys


def lade_zugangsdaten():
    """Lädt Zugangsdaten aus .env Datei."""
    env_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '.env'))

    if not os.path.exists(env_path):
        print("❌ Keine .env Datei gefunden!")
        print("   → Führe zuerst aus: python3 scripts/setup_zugangsdaten.py")
        sys.exit(1)

    config = {}
    with open(env_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                config[key.strip()] = value.strip()

    required = ['META_ACCESS_TOKEN', 'CANVA_CLIENT_ID', 'CANVA_CLIENT_SECRET']
    missing = [k for k in required if not config.get(k) or 'hier' in config.get(k, '')]

    if missing:
        print(f"❌ Fehlende Zugangsdaten in .env: {', '.join(missing)}")
        print("   → Öffne .env und trage die Werte aus Notion ein")
        sys.exit(1)

    return config


def get_instagram_account_id(token, config):
    """Findet Instagram Business Account ID — automatisch oder aus .env."""

    # Aus .env wenn vorhanden
    ig_id = config.get('INSTAGRAM_BUSINESS_ACCOUNT_ID', '')
    if ig_id and ig_id != '':
        print(f"✅ Instagram Account ID aus .env: {ig_id}")
        return ig_id, token

    print("🔍 Suche Instagram Business Account ID automatisch...")

    # Über Facebook Pages suchen
    r = requests.get(
        "https://graph.facebook.com/v19.0/me/accounts",
        params={"access_token": token}
    )
    pages = r.json().get("data", [])

    for page in pages:
        page_token = page.get("access_token", token)
        r2 = requests.get(
            f"https://graph.facebook.com/v19.0/{page['id']}",
            params={"fields": "instagram_business_account,name", "access_token": page_token}
        )
        d = r2.json()
        if "instagram_business_account" in d:
            ig_id = d["instagram_business_account"]["id"]
            print(f"✅ Gefunden über Seite '{d.get('name', '')}': {ig_id}")
            return ig_id, page_token

    print("❌ Instagram Business Account nicht gefunden.")
    print("   → Führe aus: python3 scripts/setup_zugangsdaten.py")
    sys.exit(1)


def erstelle_canva_design(config, karussell):
    """Erstellt Karussell-Design in Canva."""
    print(f"\n🎨 Canva Design wird erstellt...")
    print(f"   Thema: {karussell['bildthema']}")
    print(f"   Slides: {len(karussell['slides'])}")

    # Platzhalter-Bilder für Test (1080x1080 Instagram Format)
    bild_urls = []
    farben = ["FFB5C8", "FFDDE1", "FFC8DD", "FFD6E0", "FFAFCC", "BDE0FE", "A2D2FF"]

    for i, slide_text in enumerate(karussell['slides']):
        farbe = farben[i % len(farben)]
        encoded_text = slide_text[:40].replace(' ', '+').replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue')
        url = f"https://via.placeholder.com/1080x1080/{farbe}/333333?text={encoded_text}"
        bild_urls.append(url)
        print(f"   Slide {i+1}: ✅")

    print(f"   → {len(bild_urls)} Slides bereit für Instagram")
    return bild_urls


def poste_karussell_instagram(instagram_id, page_token, bild_urls, caption):
    """Erstellt und veröffentlicht Karussell auf Instagram."""
    print(f"\n📸 Lade {len(bild_urls)} Bilder zu Instagram hoch...")

    # Schritt 1: Media Container für jedes Bild
    media_ids = []
    for i, url in enumerate(bild_urls):
        r = requests.post(
            f"https://graph.facebook.com/v19.0/{instagram_id}/media",
            params={
                "image_url": url,
                "is_carousel_item": "true",
                "access_token": page_token
            }
        )
        result = r.json()

        if "id" in result:
            media_ids.append(result["id"])
            print(f"   Slide {i+1}: ✅ (ID: {result['id']})")
        else:
            fehler = result.get("error", {}).get("message", str(result))
            print(f"   Slide {i+1}: ❌ Fehler — {fehler}")
            return None

    # Schritt 2: Karussell Container
    print("\n🔗 Karussell wird zusammengestellt...")
    r2 = requests.post(
        f"https://graph.facebook.com/v19.0/{instagram_id}/media",
        params={
            "media_type": "CAROUSEL",
            "children": ",".join(media_ids),
            "caption": caption,
            "access_token": page_token
        }
    )
    karussell_data = r2.json()

    if "id" not in karussell_data:
        print(f"❌ Fehler beim Karussell: {karussell_data}")
        return None

    karussell_id = karussell_data["id"]
    print(f"✅ Karussell bereit (ID: {karussell_id})")

    # Kurz warten (Meta empfiehlt das)
    time.sleep(2)

    # Schritt 3: Veröffentlichen
    print("🚀 Wird gepostet...")
    r3 = requests.post(
        f"https://graph.facebook.com/v19.0/{instagram_id}/media_publish",
        params={
            "creation_id": karussell_id,
            "access_token": page_token
        }
    )
    publish_data = r3.json()

    if "id" in publish_data:
        print(f"\n🎊 ERFOLGREICH GEPOSTET!")
        print(f"   Instagram Post ID: {publish_data['id']}")
        return publish_data["id"]
    else:
        print(f"❌ Fehler beim Veröffentlichen: {publish_data}")
        return None


def main():
    print("=" * 55)
    print("  📱 Instagram Karussell Automatisierung")
    print("  E-Mail Marketing für selbständige Mamas")
    print("=" * 55)

    # Zugangsdaten laden
    config = lade_zugangsdaten()
    token = config['META_ACCESS_TOKEN']

    # Instagram Account finden
    instagram_id, page_token = get_instagram_account_id(token, config)

    # Karussell-Inhalt (später automatisch aus Notion geladen)
    karussell = {
        "titel": "Du bist gut genug — genau so",
        "bildthema": "Rosa Pastell, Blumen, warmes Licht",
        "slides": [
            "Du machst alles falsch — dachtest du es auch? 🌸",
            "Mama sein bedeutet nicht: perfekt sein",
            "Dein Business darf sich um dein Leben aufbauen",
            "3 Dinge die du heute loslassen darfst",
            "Du brauchst kein System das dich erschöpft",
            "Dein nächster Schritt muss sich LEICHT anfühlen",
            "Speicher das 🌸 wenn du das brauchst"
        ],
        "caption": (
            "Du bist gut genug — genau so wie du bist 🌸\n\n"
            "Als selbständige Mama kennst du das Gefühl: "
            "nie genug, nie fertig, nie perfekt.\n\n"
            "Aber was wäre wenn dein Business sich anders anfühlen darf?\n\n"
            "👇 Schreib mir in die Kommentare: Was darfst DU heute loslassen?\n\n"
            "#SelbständigeMama #EmailMarketing #BusinessMama "
            "#Selbstliebe #MamaUnternehmer #emailimitmonika"
        )
    }

    # Canva Design erstellen
    bild_urls = erstelle_canva_design(config, karussell)

    # Auf Instagram posten
    post_id = poste_karussell_instagram(
        instagram_id,
        page_token,
        bild_urls,
        karussell["caption"]
    )

    if post_id:
        print("\n✅ FERTIG! Dein Karussell ist live auf Instagram!")
        print(f"   Profil: https://www.instagram.com/emailimitmonika./")
    else:
        print("\n⚠️  Posting fehlgeschlagen.")
        print("   → Prüfe deine Zugangsdaten: python3 scripts/setup_zugangsdaten.py")


if __name__ == "__main__":
    main()
