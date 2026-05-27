#!/usr/bin/env python3
"""
Pinterest Pin Image Generator für E-Mails mit Monika
Branding: Burgundy #800020 als Hauptfarbe, Gold #B59156 als Akzent
"""

from PIL import Image, ImageDraw, ImageFont
import os

# ═══════════════════════════════════════════════
# BRAND FARBEN (Monika's offizielle Markenfarben)
# ═══════════════════════════════════════════════
BURGUNDY      = (128, 0, 32)      # #800020 — Hauptfarbe
BURGUNDY_DARK = (90, 0, 20)       # Dunkleres Burgundy für Tiefe
GOLD          = (181, 145, 86)    # #B59156 — Akzentfarbe
GOLD_LIGHT    = (220, 195, 140)   # Helles Gold für Highlights
CREAM         = (252, 245, 232)   # Crème-Weiß für Text
WHITE         = (255, 255, 255)

# ═══════════════════════════════════════════════
# CANVAS GRÖßE (Pinterest Standard)
# ═══════════════════════════════════════════════
WIDTH  = 1000
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
    """Erstellt einen Pinterest Pin mit Monika's Branding"""

    img = Image.new('RGB', (WIDTH, HEIGHT), BURGUNDY)
    draw = ImageDraw.Draw(img)

    # ─── HINTERGRUND: Burgundy mit leichtem Verlauf ───
    for y in range(HEIGHT):
        ratio = y / HEIGHT
        r = int(BURGUNDY[0] * (1 - ratio * 0.25) + BURGUNDY_DARK[0] * ratio * 0.25)
        g = int(BURGUNDY[1] * (1 - ratio * 0.25) + BURGUNDY_DARK[1] * ratio * 0.25)
        b = int(BURGUNDY[2] * (1 - ratio * 0.25) + BURGUNDY_DARK[2] * ratio * 0.25)
        draw.line([(0, y), (WIDTH, y)], fill=(r, g, b))

    # ─── GOLD-RAHMEN (oben & unten) ───
    draw.rectangle([(0, 0),       (WIDTH, 10)],        fill=GOLD)
    draw.rectangle([(0, 10),      (WIDTH, 14)],        fill=GOLD_LIGHT)
    draw.rectangle([(0, HEIGHT-14),(WIDTH, HEIGHT-10)], fill=GOLD_LIGHT)
    draw.rectangle([(0, HEIGHT-10),(WIDTH, HEIGHT)],    fill=GOLD)

    # ─── GOLD SEITENLINIEN ───
    draw.rectangle([(0, 0), (10, HEIGHT)],       fill=GOLD)
    draw.rectangle([(WIDTH-10, 0), (WIDTH, HEIGHT)], fill=GOLD)

    # ─── DEKORATIVER GOLD-RAHMEN INNEN ───
    pad = 40
    line_w = 2
    draw.rectangle([(pad, pad), (WIDTH-pad, pad+line_w)],             fill=GOLD)
    draw.rectangle([(pad, HEIGHT-pad-line_w), (WIDTH-pad, HEIGHT-pad)], fill=GOLD)
    draw.rectangle([(pad, pad), (pad+line_w, HEIGHT-pad)],             fill=GOLD)
    draw.rectangle([(WIDTH-pad-line_w, pad), (WIDTH-pad, HEIGHT-pad)], fill=GOLD)

    # ─── FONTS LADEN ───
    # Überschrift: Bugaki (falls vorhanden) → sonst Playfair Display (ähnlicher Stil)
    # Normaler Text: Arial → Liberation Sans (identische Metriken zu Arial)
    bugaki_path      = "Bugaki.ttf"          # Falls Monika die Datei hinterlegt
    playfair_path    = "PlayfairDisplay.ttf"  # Fallback Überschrift
    arial_regular    = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
    arial_bold       = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"

    # Überschrift-Font (Bugaki oder Playfair Display)
    for headline_font_path in [bugaki_path, playfair_path]:
        try:
            font_headline = ImageFont.truetype(headline_font_path, 88)
            font_sub      = ImageFont.truetype(headline_font_path, 48)
            break
        except:
            continue
    else:
        font_headline = ImageFont.truetype(arial_bold, 88)
        font_sub      = ImageFont.truetype(arial_bold, 48)

    # Normaler Text: Arial (Liberation Sans)
    font_label   = ImageFont.truetype(arial_regular, 30)
    font_website = ImageFont.truetype(arial_regular, 28)

    # ─── LABEL OBEN (Gold-Text) ───
    label = "✦  E-Mail Marketing mit Monika  ✦"
    try:
        bbox = draw.textbbox((0, 0), label, font=font_label)
        lw = bbox[2] - bbox[0]
        draw.text(((WIDTH - lw) // 2, 70), label, fill=GOLD, font=font_label)
    except:
        label = "E-Mail Marketing mit Monika"
        bbox = draw.textbbox((0, 0), label, font=font_label)
        lw = bbox[2] - bbox[0]
        draw.text(((WIDTH - lw) // 2, 70), label, fill=GOLD, font=font_label)

    # ─── TRENNLINIE NACH LABEL ───
    draw.rectangle([(80, 118), (WIDTH-80, 121)], fill=GOLD)

    # ─── HAUPT-HEADLINE (Crème-Text auf Burgundy) ───
    margin       = 85
    max_text_w   = WIDTH - margin * 2
    lines        = wrap_text(headline, font_headline, draw, max_text_w)
    line_height  = 108
    total_h      = len(lines) * line_height
    start_y      = 180

    for i, line in enumerate(lines):
        bbox   = draw.textbbox((0, 0), line, font=font_headline)
        line_w = bbox[2] - bbox[0]
        x = (WIDTH - line_w) // 2
        y = start_y + i * line_height
        # Leichter Schatten
        draw.text((x+2, y+2), line, fill=(60, 0, 10), font=font_headline)
        # Haupttext Crème
        draw.text((x, y), line, fill=CREAM, font=font_headline)

    # ─── GOLD ORNAMENT ───
    ornament_y = start_y + len(lines) * line_height + 30
    orn = "— ✦ —"
    try:
        bbox = draw.textbbox((0, 0), orn, font=font_sub)
        ow   = bbox[2] - bbox[0]
        draw.text(((WIDTH - ow) // 2, ornament_y), orn, fill=GOLD, font=font_sub)
    except:
        draw.rectangle([(WIDTH//2-80, ornament_y+20), (WIDTH//2+80, ornament_y+24)], fill=GOLD)

    # ─── SUBTEXT (Gold-Text) ───
    sub_y      = ornament_y + 80
    sub_lines  = wrap_text(subtext, font_sub, draw, max_text_w)
    sub_lh     = 68

    for i, line in enumerate(sub_lines):
        bbox   = draw.textbbox((0, 0), line, font=font_sub)
        line_w = bbox[2] - bbox[0]
        x = (WIDTH - line_w) // 2
        y = sub_y + i * sub_lh
        draw.text((x, y), line, fill=GOLD_LIGHT, font=font_sub)

    # ─── WEBSITE BOX (Gold-Rahmen, Crème-Text) ───
    box_top = HEIGHT - 155
    box_bot = HEIGHT - 75
    draw.rectangle([(70, box_top), (WIDTH-70, box_bot)],
                   fill=BURGUNDY_DARK, outline=GOLD, width=3)

    bbox  = draw.textbbox((0, 0), website, font=font_website)
    web_w = bbox[2] - bbox[0]
    web_y = box_top + (box_bot - box_top - (bbox[3] - bbox[1])) // 2
    draw.text(((WIDTH - web_w) // 2, web_y), website, fill=GOLD_LIGHT, font=font_website)

    # ─── SPEICHERN ───
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    img.save(output_path, 'PNG', quality=95)
    print(f"✅ Pin #{pin_number:02d} erstellt: {output_path}")
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
        "headline": "Warum du keine Follower brauchst, um online zu verkaufen.",
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
        "headline": "5 Fehler beim E-Mail-Marketing — und wie du sie vermeidest.",
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
        "headline": "Kein Technik-Stress. Keine Kaltakquise. Nur ein System, das arbeitet.",
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
    create_pin(
        pin_number=pin["number"],
        headline=pin["headline"],
        subtext=pin["subtext"],
        website=pin["website"],
        output_path=f"{output_dir}pin-{pin['number']:02d}.png"
    )

print("\n🎉 Alle 7 Pinterest Pins mit Burgundy #800020 + Gold #B59156 erstellt!")
