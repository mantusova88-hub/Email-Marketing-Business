#!/usr/bin/env python3
"""Baut aus allen Markdown-Dateien des Workspace ein lesbares PDF."""

import os
import re
import html

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether,
)

BASE = "/home/user/Email-Marketing-Business"
OUT = ("/tmp/claude-0/-home-user-Email-Marketing-Business/"
       "3358855f-df26-5510-9746-db651d38b815/scratchpad/Monika-Alles.pdf")

BURGUND = HexColor("#800220")
GOLD = HexColor("#B59156")
CREME = HexColor("#F4EDE4")
CREME2 = HexColor("#FBF7F2")
INK = HexColor("#2E1218")
SOFT = HexColor("#6B5257")
RULE = HexColor("#E2D4C6")

# ------------------------------------------------------------------ Stile
def S(name, **kw):
    base = dict(fontName="Helvetica", fontSize=10, leading=14.5, textColor=INK)
    base.update(kw)
    return ParagraphStyle(name, **base)

st_cover_t = S("ct", fontName="Helvetica-Bold", fontSize=32, leading=36, textColor=BURGUND)
st_cover_s = S("cs", fontSize=12, leading=17, textColor=SOFT)
st_part = S("part", fontName="Helvetica-Bold", fontSize=22, leading=26,
            textColor=BURGUND, spaceBefore=0, spaceAfter=4)
st_partsub = S("partsub", fontSize=10.5, leading=15, textColor=SOFT, spaceAfter=14)
st_h1 = S("h1", fontName="Helvetica-Bold", fontSize=15, leading=19,
          textColor=BURGUND, spaceBefore=14, spaceAfter=6)
st_h2 = S("h2", fontName="Helvetica-Bold", fontSize=11.5, leading=15,
          textColor=INK, spaceBefore=11, spaceAfter=4)
st_h3 = S("h3", fontName="Helvetica-Bold", fontSize=10.5, leading=14,
          textColor=SOFT, spaceBefore=9, spaceAfter=3)
st_body = S("body", spaceAfter=6)
st_li = S("li", leftIndent=11, bulletIndent=2, spaceAfter=3)
st_quote = S("quote", fontName="Helvetica-Oblique", fontSize=10, leading=14.5,
             textColor=SOFT, leftIndent=10, spaceAfter=6)
st_toc = S("toc", fontSize=10.5, leading=17)
st_cell = S("cell", fontSize=9, leading=12.5)
st_cellh = S("cellh", fontName="Helvetica-Bold", fontSize=8.5, leading=12, textColor=CREME)

PAGE_W = A4[0] - 40 * mm


def inline(t):
    """Markdown-Inline nach reportlab-Markup."""
    t = html.escape(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<!\*)\*([^*\n]+?)\*(?!\*)", r"<i>\1</i>", t)
    t = re.sub(r"`([^`]+?)`", r'<font face="Courier" color="#800220">\1</font>', t)
    t = re.sub(r"\[(.+?)\]\((.+?)\)", r"\1", t)
    t = t.replace("—", "&#8212;").replace("→", "&#8594;")
    return t


def make_table(rows):
    if not rows:
        return None
    ncol = max(len(r) for r in rows)
    rows = [r + [""] * (ncol - len(r)) for r in rows]
    widths = [PAGE_W / ncol] * ncol
    data = []
    for i, r in enumerate(rows):
        stl = st_cellh if i == 0 else st_cell
        data.append([Paragraph(inline(c), stl) for c in r])
    t = Table(data, colWidths=widths, hAlign="LEFT", repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), BURGUND),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [CREME, CREME2]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("LINEBELOW", (0, 0), (-1, -2), 0.35, RULE),
    ]))
    return t


def hrule():
    t = Table([[""]], colWidths=[PAGE_W], rowHeights=[1])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), GOLD)]))
    return t


def md_to_flowables(text):
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    for a, b in (("\u251c", "+"), ("\u2514", "+"), ("\u2502", "|"),
                 ("\u2500", "-"), ("\u2564", "+"), ("\u252c", "+"),
                 ("\u2018", "'"), ("\u2019", "'"), ("\u2713", "+"),
                 ("\u2717", "x"), ("\u00a0", " ")):
        text = text.replace(a, b)
    text = "".join(
        ch if (ord(ch) < 128 or ch in "\u00e4\u00f6\u00fc\u00c4\u00d6\u00dc\u00df\u20ac\u00b0\u00b7"
                                     "\u2014\u2013\u201e\u201c\u201d\u2018\u2019\u2026\u2022\u2192\u00a7")
        else ("+" if ch in "\u2705\u25ba\u2713" else "")
        for ch in text)
    out = []
    lines = text.split("\n")
    i = 0
    tbl = []
    while i < len(lines):
        raw = lines[i]
        line = raw.rstrip()
        stripped = line.strip()

        # Tabelle sammeln
        if stripped.startswith("|") and stripped.endswith("|"):
            cells = [c.strip() for c in stripped.strip("|").split("|")]
            if not all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
                tbl.append(cells)
            i += 1
            continue
        elif tbl:
            t = make_table(tbl)
            if t:
                out.append(t)
                out.append(Spacer(1, 8))
            tbl = []

        if not stripped:
            i += 1
            continue

        if re.fullmatch(r"-{3,}", stripped) or re.fullmatch(r"={3,}", stripped):
            out.append(Spacer(1, 4))
            out.append(hrule())
            out.append(Spacer(1, 8))
        elif stripped.startswith("#### "):
            out.append(Paragraph(inline(stripped[5:]), st_h3))
        elif stripped.startswith("### "):
            out.append(Paragraph(inline(stripped[4:]), st_h2))
        elif stripped.startswith("## "):
            out.append(Paragraph(inline(stripped[3:]), st_h1))
        elif stripped.startswith("# "):
            out.append(Paragraph(inline(stripped[2:]), st_h1))
        elif stripped.startswith("> "):
            out.append(Paragraph(inline(stripped[2:]), st_quote))
        elif stripped == ">":
            pass
        elif re.match(r"^[-*] \[[ x]\] ", stripped):
            txt = re.sub(r"^[-*] \[([ x])\] ", "", stripped)
            mark = "\u2022"
            out.append(Paragraph(inline(txt), st_li, bulletText=mark))
        elif re.match(r"^[-*+] ", stripped):
            out.append(Paragraph(inline(stripped[2:]), st_li, bulletText="\u2022"))
        elif re.match(r"^\d+[.)] ", stripped):
            num = re.match(r"^(\d+)[.)] ", stripped).group(1)
            txt = re.sub(r"^\d+[.)] ", "", stripped)
            out.append(Paragraph(inline(txt), st_li, bulletText=num + "."))
        elif stripped.startswith("```"):
            i += 1
            block = []
            while i < len(lines) and not lines[i].strip().startswith("```"):
                block.append(lines[i])
                i += 1
            code = "<br/>".join(html.escape(b, quote=False).replace(" ", "&nbsp;")
                                for b in block)
            out.append(Paragraph(code, S("code", fontName="Courier", fontSize=8.5,
                                         leading=11.5, textColor=SOFT,
                                         backColor=CREME, borderPadding=6,
                                         spaceAfter=8)))
        else:
            out.append(Paragraph(inline(stripped), st_body))
        i += 1

    if tbl:
        t = make_table(tbl)
        if t:
            out.append(t)
    return out


# ------------------------------------------------------------------ Inhalt
SECTIONS = [
    ("Teil 1", "Die Regeln fürs Gestalten",
     "Was auf jede Folie gehört. Farben, Schriftgrößen, Zeichensetzung.", [
         ("Markenregeln für Grafiken", "reference/markenregeln-gestaltung.md"),
         ("Was jeden Tag rausgeht", "reference/veroeffentlichungs-regel.md"),
     ]),
    ("Teil 2", "Die Regeln fürs Schreiben",
     "Wie eine erste Folie gebaut wird und was in die Story kommt.", [
         ("Hooks für das Deckblatt", "reference/hooks-deckblatt.md"),
         ("Story-Hooks und Link-Texte", "reference/story-hooks.md"),
         ("Das Content-System, abgeschaut", "reference/content-system-email-design-reveal.md"),
     ]),
    ("Teil 3", "Du und dein Business",
     "Wer du bist, wo du stehst, wohin du willst.", [
         ("Wer bin ich", "profil/01_wer-bin-ich.md"),
         ("Entwicklungsplan", "profil/02_entwicklungsplan.md"),
         ("Innerer Kompass", "profil/03_innerer-kompass.md"),
         ("Persönliche Angaben", "context/personal-info.md"),
         ("Business-Infos", "context/business-info.md"),
         ("Strategie", "context/strategy.md"),
         ("Aktuelle Zahlen", "context/current-data.md"),
     ]),
    ("Teil 4", "Was gebaut wurde",
     "Die Wochenübersicht und ältere Arbeitsergebnisse.", [
         ("Woche ab 5. August", "outputs/woche-05-08-2026.md"),
         ("Session Nischengenerator", "outputs/2026-06-01-session-nischengenerator.md"),
     ]),
    ("Teil 5", "Technisches zum Nachschlagen",
     "Brauchst du selten. Steht hier, damit es nicht verloren geht.", [
         ("Der Workspace", "CLAUDE.md"),
         ("Verkaufsseite systeme.io", "reference/systeme-io-verkaufsseite.md"),
         ("Anleitungen Deployment", "reference/anleitungen-deployment.md"),
     ]),
]

story = []

# Deckblatt
story.append(Spacer(1, 55 * mm))
story.append(Paragraph("Alles auf einen Blick", st_cover_t))
story.append(Spacer(1, 5))
story.append(Paragraph(
    "Jede Regel, jede Vorlage, jeder Plan, den wir zusammen aufgeschrieben haben.<br/>"
    "e-mails mit Monika &nbsp;·&nbsp; @emailsmitmonika_ &nbsp;·&nbsp; Stand 10. August 2026",
    st_cover_s))
story.append(Spacer(1, 10))
story.append(hrule())
story.append(Spacer(1, 14))

toc_rows = [["Teil", "Worum es geht", "Kapitel"]]
for num, name, sub, docs in SECTIONS:
    toc_rows.append([num + ": " + name, sub, str(len(docs))])
story.append(make_table(toc_rows))
story.append(Spacer(1, 12))
story.append(Paragraph(
    "Du musst das nicht am Stück lesen. Nimm dir das Kapitel, das du gerade brauchst.",
    st_quote))
story.append(PageBreak())

missing = []
for num, name, sub, docs in SECTIONS:
    story.append(Paragraph(num, st_partsub))
    story.append(Paragraph(name, st_part))
    story.append(Paragraph(sub, st_partsub))
    story.append(hrule())
    story.append(Spacer(1, 10))
    for i, (title, rel) in enumerate(docs):
        path = os.path.join(BASE, rel)
        if not os.path.exists(path):
            missing.append(rel)
            continue
        with open(path, encoding="utf-8") as f:
            txt = f.read()
        # erste H1-Zeile raus, wir setzen eigene Überschrift
        txt = re.sub(r"^#\s+.*\n", "", txt, count=1)
        story.append(Paragraph(title, st_h1))
        story.extend(md_to_flowables(txt))
        if i < len(docs) - 1:
            story.append(Spacer(1, 6))
            story.append(hrule())
            story.append(Spacer(1, 6))
    story.append(PageBreak())


def deco(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(SOFT)
    canvas.drawString(20 * mm, 12 * mm, "e-mails mit Monika  ·  @emailsmitmonika_")
    canvas.drawRightString(A4[0] - 20 * mm, 12 * mm, str(doc.page))
    canvas.setStrokeColor(GOLD)
    canvas.setLineWidth(0.5)
    canvas.line(20 * mm, 16 * mm, A4[0] - 20 * mm, 16 * mm)
    canvas.restoreState()


doc = BaseDocTemplate(
    OUT, pagesize=A4,
    leftMargin=20 * mm, rightMargin=20 * mm,
    topMargin=18 * mm, bottomMargin=22 * mm,
    title="Alles auf einen Blick", author="e-mails mit Monika",
)
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")
doc.addPageTemplates([PageTemplate(id="all", frames=[frame], onPage=deco)])
doc.build(story)

print("fertig:", OUT)
if missing:
    print("fehlend:", missing)
