#!/usr/bin/env python3
"""
Instagram Karussell Automatisierung
=====================================
Dieses Script:
1. Findet automatisch deine Instagram Business Account ID
2. Erstellt ein Karussell-Design in Canva
3. Postet das fertige Karussell auf Instagram

Anleitung: Fülle nur den Abschnitt "DEINE ZUGANGSDATEN" aus — der Rest läuft automatisch!
"""

import requests
import json
import time
import sys

# ============================================================
# DEINE ZUGANGSDATEN — hier eintragen (aus Notion kopieren)
# ============================================================

META_ACCESS_TOKEN = "HIER_DEINEN_ACCESS_TOKEN_EINFÜGEN"
CANVA_CLIENT_ID   = "HIER_DEINE_CANVA_CLIENT_ID_EINFÜGEN"
CANVA_CLIENT_SECRET = "HIER_DEIN_CANVA_CLIENT_SECRET_EINFÜGEN"

# ============================================================
# SCHRITT 1 — Instagram Business Account ID automatisch finden
# ============================================================

def get_instagram_account_id(access_token):
    """Findet deine Instagram Business Account ID automatisch."""
    print("\n🔍 Suche deine Instagram Business Account ID...")

    # Zuerst: Facebook Pages abrufen
    url = "https://graph.facebook.com/v19.0/me/accounts"
    params = {"access_token": access_token}
    response = requests.get(url, params=params)
    data = response.json()

    if "data" in data and len(data["data"]) > 0:
        for page in data["data"]:
            page_id = page["id"]
            page_name = page.get("name", "Unbekannt")
            page_token = page.get("access_token", access_token)

            # Instagram Account der Page abrufen
            ig_url = f"https://graph.facebook.com/v19.0/{page_id}"
            ig_params = {
                "fields": "instagram_business_account",
                "access_token": page_token
            }
            ig_response = requests.get(ig_url, params=ig_params)
            ig_data = ig_response.json()

            if "instagram_business_account" in ig_data:
                ig_id = ig_data["instagram_business_account"]["id"]
                print(f"✅ Instagram Account gefunden!")
                print(f"   Facebook Page: {page_name}")
                print(f"   Instagram Business Account ID: {ig_id}")
                return ig_id, page_token

    # Falls keine Page gefunden: User-Token direkt probieren
    print("⚠️  Kein Facebook Page gefunden. Probiere direkten Zugriff...")
    url2 = "https://graph.facebook.com/v19.0/me"
    params2 = {"fields": "id,name", "access_token": access_token}
    r2 = requests.get(url2, params=params2)
    print(f"   Verbunden als: {r2.json().get('name', 'Unbekannt')}")
    print("\n❌ Instagram Business Account ID nicht gefunden.")
    print("   Lösung: Füge 'pages_show_list' Permission hinzu (siehe Anleitung)")
    return None, access_token


# ============================================================
# SCHRITT 2 — Canva Design erstellen
# ============================================================

def create_canva_design(client_id, client_secret, slide_texte, bildthema):
    """Erstellt ein Karussell-Design in Canva (Platzhalter — kommt in Version 2)."""
    print("\n🎨 Canva Design wird vorbereitet...")
    print(f"   Bildthema: {bildthema}")
    print(f"   Anzahl Slides: {len(slide_texte)}")
    print("   ⏳ Canva OAuth wird in Version 2 implementiert...")

    # Platzhalter — gibt Test-URL zurück
    test_bild_url = "https://via.placeholder.com/1080x1080.png?text=Karussell+Slide"
    print(f"   ✅ Test-Bild URL: {test_bild_url}")
    return [test_bild_url] * len(slide_texte)


# ============================================================
# SCHRITT 3 — Karussell auf Instagram posten
# ============================================================

def post_karussell_instagram(instagram_id, page_token, bild_urls, caption):
    """Postet ein Karussell auf Instagram."""
    print(f"\n📸 Erstelle Instagram Karussell ({len(bild_urls)} Bilder)...")

    # Einzelne Media-Container für jedes Bild erstellen
    media_ids = []
    for i, bild_url in enumerate(bild_urls):
        url = f"https://graph.facebook.com/v19.0/{instagram_id}/media"
        params = {
            "image_url": bild_url,
            "is_carousel_item": "true",
            "access_token": page_token
        }
        response = requests.post(url, params=params)
        result = response.json()

        if "id" in result:
            media_ids.append(result["id"])
            print(f"   ✅ Slide {i+1} vorbereitet (ID: {result['id']})")
        else:
            print(f"   ❌ Fehler bei Slide {i+1}: {result}")
            return None

    # Karussell-Container erstellen
    print("\n🔗 Karussell wird zusammengestellt...")
    carousel_url = f"https://graph.facebook.com/v19.0/{instagram_id}/media"
    carousel_params = {
        "media_type": "CAROUSEL",
        "children": ",".join(media_ids),
        "caption": caption,
        "access_token": page_token
    }
    carousel_response = requests.post(carousel_url, params=carousel_params)
    carousel_data = carousel_response.json()

    if "id" not in carousel_data:
        print(f"   ❌ Fehler beim Karussell: {carousel_data}")
        return None

    carousel_id = carousel_data["id"]
    print(f"   ✅ Karussell-Container erstellt (ID: {carousel_id})")

    # Karussell veröffentlichen
    print("\n🚀 Karussell wird gepostet...")
    publish_url = f"https://graph.facebook.com/v19.0/{instagram_id}/media_publish"
    publish_params = {
        "creation_id": carousel_id,
        "access_token": page_token
    }
    publish_response = requests.post(publish_url, params=publish_params)
    publish_data = publish_response.json()

    if "id" in publish_data:
        print(f"   🎉 ERFOLGREICH GEPOSTET! Post ID: {publish_data['id']}")
        return publish_data["id"]
    else:
        print(f"   ❌ Fehler beim Posten: {publish_data}")
        return None


# ============================================================
# HAUPTPROGRAMM — alles zusammen
# ============================================================

def main():
    print("=" * 50)
    print("  Instagram Karussell Automatisierung")
    print("  by emailimitmonika. | E-Mail Marketing für Mamas")
    print("=" * 50)

    # Beispiel-Karussell Inhalt (später aus Notion geladen)
    karussell = {
        "titel": "Du bist gut genug — genau so",
        "bildthema": "Rosa Pastell, Blumen, warmes Licht",
        "slides": [
            "Du machst alles falsch — dachtest du es auch?",
            "Mama sein bedeutet nicht: perfekt sein",
            "Dein Business darf sich um dein Leben herum aufbauen",
            "3 Dinge die du heute loslassen darfst",
            "Du brauchst kein System das dich erschöpft",
            "Dein nächster Schritt muss sich LEICHT anfühlen",
            "Speicher das 🌸 wenn du das brauchst"
        ],
        "caption": "Du bist gut genug — genau so wie du bist 🌸\n\nAls selbständige Mama kennst du das Gefühl: nie genug, nie fertig, nie perfekt.\n\nAber was wäre wenn dein Business sich anders anfühlen darf?\n\n👇 Schreib mir in die Kommentare: Was darfst DU heute loslassen?\n\n#SelbständigeMama #EmailMarketing #BusinessMama #Selbstliebe #MamaUnternehmer"
    }

    # Schritt 1: Instagram ID finden
    instagram_id, page_token = get_instagram_account_id(META_ACCESS_TOKEN)

    if not instagram_id:
        print("\n⚠️  Script läuft im TEST-MODUS (ohne Instagram ID)")
        print("   Die Canva-Integration wird trotzdem getestet.\n")

    # Schritt 2: Canva Design erstellen
    bild_urls = create_canva_design(
        CANVA_CLIENT_ID,
        CANVA_CLIENT_SECRET,
        karussell["slides"],
        karussell["bildthema"]
    )

    # Schritt 3: Auf Instagram posten (nur wenn ID vorhanden)
    if instagram_id and bild_urls:
        post_id = post_karussell_instagram(
            instagram_id,
            page_token,
            bild_urls,
            karussell["caption"]
        )
        if post_id:
            print(f"\n🎊 FERTIG! Dein Karussell ist live auf Instagram!")
    else:
        print("\n📋 ZUSAMMENFASSUNG (Test-Modus):")
        print(f"   Titel: {karussell['titel']}")
        print(f"   Slides: {len(karussell['slides'])} Stück")
        print(f"   Caption: {karussell['caption'][:80]}...")
        print("\n   ➡️  Nächster Schritt: Access Token in Zeile 20 einfügen!")


if __name__ == "__main__":
    main()
