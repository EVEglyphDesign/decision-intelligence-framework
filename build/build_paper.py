"""Build the EVEglyphDesign Decision Intelligence Framework peer-review paper.

Canon (per EgD-BOOT-001):
- Cream/orange palette; Fraunces (display) + Inter (body).
- EVEglyph rotated watermark on every page.
- Header line: "EVEglyphDesign · Controlled copy" + EgD-KEY-2026-07.
- Footer: SHA-256 (first 16), ISO-8601 UTC timestamp, "Page X of N",
  closing mark "Pour le bien-être du peuple".
- Two-pass build: pass one discovers the page count; pass two stamps it.
- Clickable links only.
"""

from __future__ import annotations

import hashlib
import sys
from datetime import datetime, timezone
from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    KeepTogether,
)

sys.path.insert(0, str(Path(__file__).resolve().parent))
from paper_content import (  # noqa: E402
    TITLE,
    SUBTITLE,
    AUTHOR,
    VERSION,
    ABSTRACT,
    KEYWORDS,
    SECTIONS,
)

# --- Canon --------------------------------------------------------------

CREAM = HexColor("#fdfaf4")
CREAM2 = HexColor("#f7f2e7")
INK = HexColor("#1a1a1a")
LINE = HexColor("#e7e1d3")
MUTE = HexColor("#6b665c")
ORANGE = HexColor("#e87722")

KEY_ID = "EgD-KEY-2026-07"
CLOSING = "Pour le bien-être du peuple"

OUT_DIR = Path(__file__).resolve().parent.parent / "docs"
OUT_DIR.mkdir(parents=True, exist_ok=True)
OUT_PATH = OUT_DIR / "EVEglyphDesign_Decision_Intelligence_Framework.pdf"
OUT_PATH_PHONE = OUT_DIR / "EVEglyphDesign_Decision_Intelligence_Framework_phone.pdf"

# Phone-first page: narrow enough that fit-to-width on a 390px phone
# renders body text around 14-16pt effective size. 100mm x 178mm is a
# tall, phone-aspect page with generous type. Margins are tighter than
# LETTER because the page is smaller; content column is ~85mm.
PHONE_PAGE = (100 * mm, 178 * mm)
PHONE_MARGIN_SIDE = 7.5 * mm
PHONE_MARGIN_TOP = 14 * mm
PHONE_MARGIN_BOTTOM = 14 * mm


# --- Fonts --------------------------------------------------------------

def _register_fonts() -> tuple[str, str, str, str]:
    """Register Fraunces + Inter if present, fall back to core PDF fonts."""
    candidates = {
        "Fraunces": [
            "/usr/share/fonts/truetype/fraunces/Fraunces-Regular.ttf",
        ],
        "Fraunces-Bold": [
            "/usr/share/fonts/truetype/fraunces/Fraunces-Bold.ttf",
        ],
        "Inter": [
            "/usr/share/fonts/truetype/inter/Inter-Regular.ttf",
        ],
        "Inter-Bold": [
            "/usr/share/fonts/truetype/inter/Inter-Bold.ttf",
        ],
    }
    resolved = {}
    for name, paths in candidates.items():
        for p in paths:
            if Path(p).exists():
                try:
                    pdfmetrics.registerFont(TTFont(name, p))
                    resolved[name] = name
                    break
                except Exception:
                    continue
    display = resolved.get("Fraunces", "Times-Roman")
    display_bold = resolved.get("Fraunces-Bold", "Times-Bold")
    body = resolved.get("Inter", "Helvetica")
    body_bold = resolved.get("Inter-Bold", "Helvetica-Bold")
    return display, display_bold, body, body_bold


DISPLAY, DISPLAY_BOLD, BODY, BODY_BOLD = _register_fonts()


# --- Styles -------------------------------------------------------------

def _styles(phone: bool = False):
    # Phone build uses larger type + tighter leading ratios so fit-to-width
    # on a 390px viewport renders body text around 14-16pt effective.
    scale = 1.55 if phone else 1.0
    return {
        "eyebrow": ParagraphStyle(
            "eyebrow", fontName=BODY_BOLD, fontSize=8 * scale, leading=10 * scale,
            textColor=ORANGE, spaceAfter=6, alignment=TA_LEFT,
        ),
        "title": ParagraphStyle(
            "title", fontName=DISPLAY_BOLD,
            fontSize=(20 if phone else 24), leading=(24 if phone else 28),
            textColor=INK, spaceAfter=6,
        ),
        "subtitle": ParagraphStyle(
            "subtitle", fontName=DISPLAY,
            fontSize=(12 if phone else 13), leading=(16 if phone else 17),
            textColor=MUTE, spaceAfter=18,
        ),
        "author": ParagraphStyle(
            "author", fontName=BODY, fontSize=9 * scale, leading=12 * scale,
            textColor=INK, spaceAfter=2,
        ),
        "version": ParagraphStyle(
            "version", fontName=BODY, fontSize=8.5 * scale, leading=11 * scale,
            textColor=MUTE, spaceAfter=14,
        ),
        "abstract_label": ParagraphStyle(
            "abstract_label", fontName=BODY_BOLD, fontSize=9 * scale, leading=11 * scale,
            textColor=ORANGE, spaceAfter=4,
        ),
        "abstract": ParagraphStyle(
            "abstract", fontName=BODY, fontSize=9.5 * scale, leading=13.5 * scale,
            textColor=INK, spaceAfter=10,
            alignment=(TA_LEFT if phone else TA_JUSTIFY),
            leftIndent=0, rightIndent=0,
        ),
        "keywords": ParagraphStyle(
            "keywords", fontName=BODY, fontSize=8.5 * scale, leading=11 * scale,
            textColor=MUTE, spaceAfter=12,
        ),
        "h2": ParagraphStyle(
            "h2", fontName=DISPLAY_BOLD,
            fontSize=(16 if phone else 15), leading=(20 if phone else 19),
            textColor=INK, spaceBefore=16, spaceAfter=6,
        ),
        "h3": ParagraphStyle(
            "h3", fontName=DISPLAY_BOLD,
            fontSize=(13 if phone else 11.5), leading=(17 if phone else 15),
            textColor=INK, spaceBefore=10, spaceAfter=3,
        ),
        "body": ParagraphStyle(
            "body", fontName=BODY, fontSize=10 * scale, leading=14 * scale,
            textColor=INK, spaceAfter=7,
            alignment=(TA_LEFT if phone else TA_JUSTIFY),
        ),
        "bullet": ParagraphStyle(
            "bullet", fontName=BODY, fontSize=9.5 * scale, leading=13 * scale,
            textColor=INK, leftIndent=(20 if phone else 14),
            bulletIndent=(4 if phone else 2), spaceAfter=3,
        ),
        "cellhead": ParagraphStyle(
            "cellhead", fontName=BODY_BOLD, fontSize=8.5 * scale, leading=11 * scale,
            textColor=INK,
        ),
        "cell": ParagraphStyle(
            "cell", fontName=BODY, fontSize=8.5 * scale, leading=11 * scale,
            textColor=INK,
        ),
        "stack_label": ParagraphStyle(
            "stack_label", fontName=BODY_BOLD, fontSize=10, leading=13,
            textColor=ORANGE, spaceBefore=6, spaceAfter=1,
        ),
        "stack_value": ParagraphStyle(
            "stack_value", fontName=BODY, fontSize=13, leading=17,
            textColor=INK, spaceAfter=6,
        ),
    }


# --- Story --------------------------------------------------------------

def _story(phone: bool = False, content_width: float = 7.0 * inch):
    s = _styles(phone=phone)
    story = []

    # Cover block
    story.append(Paragraph("EVEglyphDesign · Peer-review draft", s["eyebrow"]))
    story.append(Paragraph(TITLE, s["title"]))
    story.append(Paragraph(SUBTITLE, s["subtitle"]))
    story.append(Paragraph(AUTHOR, s["author"]))
    story.append(Paragraph(VERSION, s["version"]))

    # Abstract
    story.append(Paragraph("Abstract", s["abstract_label"]))
    story.append(Paragraph(ABSTRACT, s["abstract"]))
    story.append(Paragraph(
        "<b>Keywords:</b> " + "; ".join(KEYWORDS) + ".",
        s["keywords"],
    ))

    # Body sections
    for entry in SECTIONS:
        kind = entry[0]
        text = entry[1]
        payload = entry[2]

        if kind == "h2":
            story.append(Paragraph(text, s["h2"]))
        elif kind == "h3":
            story.append(Paragraph(text, s["h3"]))
        elif kind == "p":
            story.append(Paragraph(text, s["body"]))
        elif kind == "bul":
            items = payload
            for item in items:
                story.append(Paragraph(f"• {item}", s["bullet"]))
            story.append(Spacer(1, 4))
        elif kind == "tbl":
            headers, rows = payload
            if phone:
                # Phone: stack each row as label/value pairs so nothing has
                # to fit into a narrow column. One row = one card of paragraphs.
                for r_idx, row in enumerate(rows):
                    if r_idx > 0:
                        story.append(Spacer(1, 6))
                    for h, v in zip(headers, row):
                        story.append(Paragraph(h.upper(), s["stack_label"]))
                        story.append(Paragraph(v, s["stack_value"]))
                story.append(Spacer(1, 8))
            else:
                data = [[Paragraph(h, s["cellhead"]) for h in headers]]
                for row in rows:
                    data.append([Paragraph(c, s["cell"]) for c in row])
                n = len(headers)
                if n == 3:
                    col_widths = [1.15 * inch, 3.25 * inch, 2.6 * inch]
                else:
                    col_widths = [content_width / n] * n
                tbl = Table(data, colWidths=col_widths, repeatRows=1)
                tbl.setStyle(TableStyle([
                    ("BACKGROUND", (0, 0), (-1, 0), CREAM2),
                    ("LINEBELOW", (0, 0), (-1, 0), 0.6, LINE),
                    ("LINEBELOW", (0, 1), (-1, -1), 0.25, LINE),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 6),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                    ("TOPPADDING", (0, 0), (-1, -1), 4),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ]))
                story.append(Spacer(1, 4))
                story.append(tbl)
                story.append(Spacer(1, 8))

    return story


# --- Page frame ---------------------------------------------------------

def _draw_frame(c: canvas.Canvas, doc, total_pages: int, content_hash: str, ts_iso: str,
                page_size=LETTER, phone: bool = False):
    width, height = page_size
    current_page = c.getPageNumber()

    margin_side = PHONE_MARGIN_SIDE if phone else 0.75 * inch
    margin_top_rule = (height - 8 * mm) if phone else (height - 0.55 * inch)
    margin_top_text = (height - 6 * mm) if phone else (height - 0.45 * inch)
    margin_bottom_rule = 10 * mm if phone else 0.75 * inch
    margin_bottom_text = 7 * mm if phone else 0.58 * inch
    margin_closing = 4 * mm if phone else 0.42 * inch

    header_font_size = 6 if phone else 8
    footer_font_size = 6 if phone else 7.5
    closing_font_size = 7 if phone else 8
    watermark_font_size = 44 if phone else 82

    # Cream background
    c.setFillColor(CREAM)
    c.rect(0, 0, width, height, stroke=0, fill=1)

    # Watermark
    c.saveState()
    c.setFillColor(HexColor("#f2ecdc"))
    c.setFont(DISPLAY_BOLD, watermark_font_size)
    c.translate(width / 2, height / 2)
    c.rotate(28)
    c.drawCentredString(0, 0, "EVEglyphDesign")
    c.restoreState()

    # Top rule
    c.setStrokeColor(LINE)
    c.setLineWidth(0.5)
    c.line(margin_side, margin_top_rule, width - margin_side, margin_top_rule)

    # Header mark
    c.setFillColor(ORANGE)
    c.setFont(BODY_BOLD, header_font_size)
    header_left = "EVEglyphDesign · Peer-review draft" if phone else "EVEglyphDesign · Controlled copy · Peer-review draft"
    c.drawString(margin_side, margin_top_text, header_left)
    c.setFillColor(MUTE)
    c.drawRightString(width - margin_side, margin_top_text, KEY_ID)

    # Footer
    c.setStrokeColor(LINE)
    c.line(margin_side, margin_bottom_rule, width - margin_side, margin_bottom_rule)
    c.setFillColor(MUTE)
    c.setFont(BODY, footer_font_size)
    footer_left = (
        f"© 2026 · SHA-256 {content_hash[:10]}…" if phone
        else f"© 2026 EVEglyphDesign · SHA-256 {content_hash[:16]}… · {ts_iso}"
    )
    c.drawString(margin_side, margin_bottom_text, footer_left)
    total_label = f"Page {current_page} of {total_pages}" if total_pages else f"Page {current_page}"
    c.drawRightString(width - margin_side, margin_bottom_text, total_label)
    c.setFillColor(ORANGE)
    c.setFont(DISPLAY, closing_font_size)
    c.drawCentredString(width / 2, margin_closing, CLOSING)


def _build(total_pages: int, content_hash: str, ts_iso: str, path: Path,
           phone: bool = False) -> int:
    if phone:
        pagesize = PHONE_PAGE
        left = right = PHONE_MARGIN_SIDE
        top = PHONE_MARGIN_TOP
        bottom = PHONE_MARGIN_BOTTOM
    else:
        pagesize = LETTER
        left = right = 0.75 * inch
        top = 0.85 * inch
        bottom = 0.9 * inch

    doc = BaseDocTemplate(
        str(path),
        pagesize=pagesize,
        leftMargin=left, rightMargin=right,
        topMargin=top, bottomMargin=bottom,
        title=TITLE, author="EVEglyphDesign",
        subject=SUBTITLE, keywords=", ".join(KEYWORDS),
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin,
                  doc.width, doc.height, id="body")
    template = PageTemplate(
        id="canon", frames=[frame],
        onPage=lambda c, d: _draw_frame(
            c, d, total_pages, content_hash, ts_iso,
            page_size=pagesize, phone=phone,
        ),
    )
    doc.addPageTemplates([template])
    doc.build(_story(phone=phone, content_width=doc.width))
    return doc.page


def _build_variant(ts_iso: str, out_path: Path, phone: bool) -> tuple[int, str]:
    tmp = OUT_DIR / (".pass1_phone.pdf" if phone else ".pass1.pdf")
    total = _build(0, "0" * 64, ts_iso, tmp, phone=phone)
    content_hash = hashlib.sha256(tmp.read_bytes()).hexdigest()
    tmp.unlink(missing_ok=True)
    _build(total, content_hash, ts_iso, out_path, phone=phone)
    tag = "phone" if phone else "desktop"
    print(f"[ok] wrote {out_path}")
    print(f"     variant = {tag}")
    print(f"     pages   = {total}")
    print(f"     sha256  = {content_hash}")
    return total, content_hash


def main():
    ts_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    _build_variant(ts_iso, OUT_PATH, phone=False)
    _build_variant(ts_iso, OUT_PATH_PHONE, phone=True)
    print(f"     ts      = {ts_iso}")


if __name__ == "__main__":
    main()
