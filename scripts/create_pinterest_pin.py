#!/usr/bin/env python3
"""
Pinterest Pin Image Generator für E-Mails mit Monika
Erstellt professionelle Pinterest Pins mit Branding-Farben
"""

from PIL import Image, ImageDraw, ImageFont
import os

# ═══════════════════════════════════════════════
# BRAND FARBEN
# ═══════════════════════════════════════════════
BURGUNDY = (128, 0, 32)       # #800020
GOLD = (181, 145, 86)          # #B59156
GOLD_LIGHT = (220, 190, 130)   # Helles Gold für Akzente
CREAM = (245, 238, 225)        # Crème für Hintergrundtext
DARK_BG = (18, 8, 12)          # Fast schwarz mit Hauch Burgundy
WHITE = (255, 255, 255)

# ═══════════════════════════════════════════════
# CANVAS GRÖßE (Pinterest Standard)
# ═══════════════════════════════════════════════
WIDTH = 1000
HEIGHT = 1500

def wrap_text(text, font, draw, max_width):
    """Text auf mehrere Zeilen umbrechen"""
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + (" " if current_line else "") + word
        bbox = draw.textbbox((0, 0), test_line, font=font)
        if bbox[2] <= max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    return lines

def create_pin(pin_number, headline, subtext, website, output_path):
    """Erstellt einen Pinterest Pin"""

    # Bild erstellen
    img = Image.new('RGB', (WIDTH, HEIGHT), DARK_BG)
    draw = ImageDraw.Draw(img)

    # ─── HINTERGRUND DESIGN ───
    # Eleganter dunkler Hintergrund mit Farbverlauf-Effekt
    for y in range(HEIGHT):
        ratio = y / HEIGHT
        r = int(DARK_BG[0] + (BURGUNDY[0] - DARK_BG[0]) * ratio * 0.3)
        g = int(DARK_BG[1] + (BURGUNDY[1] - DARK_BG[1]) * ratio * 0.3)
        b = int(DARK_BG[2] + (BURGUNDY[2] - DARK_BG[2]) * ratio * 0.3)
        draw.line([(0, y), (WIDTH, y)], fill=(r, g, b))

    # Gold-Linie oben
    draw.rectangle([(0, 0), (WIDTH, 8)], fill=GOLD)

    # Dekorative Gold-Linien
    draw.rectangle([(60, 140), (WIDTH-60, 144)], fill=GOLD)
    draw.rectangle([(60, 148), (WIDTH-60, 150)], fill=GOLD_LIGHT)

    # Gold-Linie unten
    draw.rectangle([(60, HEIGHT-200), (WIDTH-60, HEIGHT-196)], fill=GOLD)
    draw.rectangle([(60, HEIGHT-204), (WIDTH-60, HEIGHT-202)], fill=GOLD_LIGHT)

    # Gold-Linie ganz unten
    draw.rectangle([(0, HEIGHT-8), (WIDTH, HEIGHT)], fill=GOLD)

    # ─── FONTS LADEN ───
    font_path = "PlayfairDisplay.ttf"
    fallback_bold = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
    fallback = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-BoldItalic.ttf"
    fallback_sans = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"

    try:
        font_headline = ImageFont.truetype(font_path, 82)
        font_subtext = ImageFont.truetype(font_path, 46)
        font_small = ImageFont.truetype(fallback_sans, 32)
        font_website = ImageFont.truetype(fallback_sans, 28)
        font_pin_num = ImageFont.truetype(fallback_sans, 24)
    except:
        font_headline = ImageFont.truetype(fallback_bold, 82)
        font_subtext = ImageFont.truetype(fallback_bold, 46)
        font_small = ImageFont.truetype(fallback_sans, 32)
        font_website = ImageFont.truetype(fallback_sans, 28)
        font_pin_num = ImageFont.truetype(fallback_sans, 24)

    # ─── KLEINES GOLD-LABEL OBEN ───
    label = "E-Mail Marketing"
    bbox = draw.textbbox((0, 0), label, font=font_pin_num)
    label_w = bbox[2] - bbox[0]
    draw.text(((WIDTH - label_w) // 2, 60), label, fill=GOLD, font=font_pin_num)

    # Kleine Sternchen links und rechts
    star_text = "✦"
    try:
        draw.text(((WIDTH - label_w) // 2 - 40, 58), star_text, fill=GOLD, font=font_pin_num)
        draw.text(((WIDTH + label_w) // 2 + 16, 58), star_text, fill=GOLD, font=font_pin_num)
    except:
        pass

    # ─── HAUPT-HEADLINE ───
    margin = 80
    max_text_width = WIDTH - (margin * 2)

    lines = wrap_text(headline, font_headline, draw, max_text_width)

    # Headline Startposition (vertikal zentriert leicht oben)
    total_headline_height = len(lines) * 100
    start_y = 220

    for i, line in enumerate(lines):
        bbox = draw.textbbox((0, 0), line, font=font_headline)
        line_w = bbox[2] - bbox[0]
        x = (WIDTH - line_w) // 2
        y = start_y + i * 100

        # Schatten-Effekt
        draw.text((x+3, y+3), line, fill=(0, 0, 0, 180), font=font_headline)
        # Haupttext in Crème
        draw.text((x, y), line, fill=CREAM, font=font_headline)

    # ─── GOLD TRENN-ORNAMENT ───
    headline_end_y = start_y + len(lines) * 100 + 30
    ornament = "— ✦ —"
    try:
        bbox = draw.textbbox((0, 0), ornament, font=font_subtext)
        orn_w = bbox[2] - bbox[0]
        draw.text(((WIDTH - orn_w) // 2, headline_end_y), ornament, fill=GOLD, font=font_subtext)
    except:
        draw.rectangle([(WIDTH//2 - 60, headline_end_y + 20), (WIDTH//2 + 60, headline_end_y + 24)], fill=GOLD)

    # ─── SUBTEXT ───
    sub_y = headline_end_y + 90
    sub_lines = wrap_text(subtext, font_subtext, draw, max_text_width)

    for i, line in enumerate(sub_lines):
        bbox = draw.textbbox((0, 0), line, font=font_subtext)
        line_w = bbox[2] - bbox[0]
        x = (WIDTH - line_w) // 2
        y = sub_y + i * 64
        draw.text((x, y), line, fill=GOLD_LIGHT, font=font_subtext)

    # ─── WEBSITE / CTA ───
    # Box für Website
    box_y = HEIGHT - 170
    draw.rectangle([(80, box_y), (WIDTH-80, box_y+70)], fill=BURGUNDY, outline=GOLD, width=2)

    bbox = draw.textbbox((0, 0), website, font=font_website)
    web_w = bbox[2] - bbox[0]
    draw.text(((WIDTH - web_w) // 2, box_y + 18), website, fill=GOLD_LIGHT, font=font_website)

    # ─── SPEICHERN ───
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, 'PNG', quality=95)
    print(f"✅ Pin erstellt: {output_path}")
    return output_path


# ═══════════════════════════════════════════════
# ALLE 7 PINS
# ═══════════════════════════════════════════════
pins = [
    {
        "number": 1,
        "headline": "Automatisch verkaufen — auch wenn das Kind krank ist.",
        "subtext": "So funktioniert E-Mail-Marketing für selbständige Mamas",
        "website": "emailsmitmonika.onepage.me"
    },
    {
        "number": 2,
        "headline": "Warum du keine Social-Media-Followerin brauchst, um online zu verkaufen.",
        "subtext": "E-Mail-Marketing für Mamas ohne Stress",
        "website": "emailsmitmonika.onepage.me"
    },
    {
        "number": 3,
        "headline": "Deine E-Mail-Liste — das einzige, das dir wirklich gehört.",
        "subtext": "So baust du dein Business auf sicherem Fundament",
        "website": "emailsmitmonika.onepage.me"
    },
    {
        "number": 4,
        "headline": "5 Fehler, die Mamas beim E-Mail-Marketing machen — und wie du sie vermeidest.",
        "subtext": "Kostenloser Starter-Guide wartet auf dich",
        "website": "emailsmitmonika.onepage.me"
    },
    {
        "number": 5,
        "headline": "Stell dir vor: Du schläfst — dein Business verkauft.",
        "subtext": "Automatisiertes E-Mail-Marketing mit Wild Mail",
        "website": "emailsmitmonika.onepage.me"
    },
    {
        "number": 6,
        "headline": "Kein Technik-Stress. Kein Kaltakquise. Nur ein System, das arbeitet.",
        "subtext": "E-Mail-Marketing einfach gemacht für selbständige Frauen",
        "website": "emailsmitmonika.onepage.me"
    },
    {
        "number": 7,
        "headline": "Bereit, dein erstes E-Mail-System aufzubauen?",
        "subtext": "Hol dir jetzt den kostenlosen Starter-Guide",
        "website": "emailsmitmonika.onepage.me"
    },
]

output_dir = "/home/user/Email-Marketing-Business/outputs/pinterest-pins/"

for pin in pins:
    output_file = f"{output_dir}pin-{pin['number']:02d}.png"
    create_pin(
        pin_number=pin["number"],
        headline=pin["headline"],
        subtext=pin["subtext"],
        website=pin["website"],
        output_path=output_file
    )

print("\n🎉 Alle 7 Pinterest Pins erstellt!")
