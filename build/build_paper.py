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

def _styles():
    return {
        "eyebrow": ParagraphStyle(
            "eyebrow", fontName=BODY_BOLD, fontSize=8, leading=10,
            textColor=ORANGE, spaceAfter=6, alignment=TA_LEFT,
        ),
        "title": ParagraphStyle(
            "title", fontName=DISPLAY_BOLD, fontSize=24, leading=28,
            textColor=INK, spaceAfter=6,
        ),
        "subtitle": ParagraphStyle(
            "subtitle", fontName=DISPLAY, fontSize=13, leading=17,
            textColor=MUTE, spaceAfter=18,
        ),
        "author": ParagraphStyle(
            "author", fontName=BODY, fontSize=9, leading=12,
            textColor=INK, spaceAfter=2,
        ),
        "version": ParagraphStyle(
            "version", fontName=BODY, fontSize=8.5, leading=11,
            textColor=MUTE, spaceAfter=14,
        ),
        "abstract_label": ParagraphStyle(
            "abstract_label", fontName=BODY_BOLD, fontSize=9, leading=11,
            textColor=ORANGE, spaceAfter=4,
        ),
        "abstract": ParagraphStyle(
            "abstract", fontName=BODY, fontSize=9.5, leading=13.5,
            textColor=INK, spaceAfter=10, alignment=TA_JUSTIFY,
            leftIndent=0, rightIndent=0,
        ),
        "keywords": ParagraphStyle(
            "keywords", fontName=BODY, fontSize=8.5, leading=11,
            textColor=MUTE, spaceAfter=12,
        ),
        "h2": ParagraphStyle(
            "h2", fontName=DISPLAY_BOLD, fontSize=15, leading=19,
            textColor=INK, spaceBefore=16, spaceAfter=6,
        ),
        "h3": ParagraphStyle(
            "h3", fontName=DISPLAY_BOLD, fontSize=11.5, leading=15,
            textColor=INK, spaceBefore=10, spaceAfter=3,
        ),
        "body": ParagraphStyle(
            "body", fontName=BODY, fontSize=10, leading=14,
            textColor=INK, spaceAfter=7, alignment=TA_JUSTIFY,
        ),
        "bullet": ParagraphStyle(
            "bullet", fontName=BODY, fontSize=9.5, leading=13,
            textColor=INK, leftIndent=14, bulletIndent=2, spaceAfter=3,
        ),
        "cellhead": ParagraphStyle(
            "cellhead", fontName=BODY_BOLD, fontSize=8.5, leading=11,
            textColor=INK,
        ),
        "cell": ParagraphStyle(
            "cell", fontName=BODY, fontSize=8.5, leading=11,
            textColor=INK,
        ),
    }


# --- Story --------------------------------------------------------------

def _story():
    s = _styles()
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
            data = [[Paragraph(h, s["cellhead"]) for h in headers]]
            for row in rows:
                data.append([Paragraph(c, s["cell"]) for c in row])
            # Column widths for 7.0" content width (LETTER minus 1.5" margins)
            n = len(headers)
            if n == 3:
                col_widths = [1.15 * inch, 3.25 * inch, 2.6 * inch]
            else:
                col_widths = [7.0 * inch / n] * n
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

def _draw_frame(c: canvas.Canvas, doc, total_pages: int, content_hash: str, ts_iso: str):
    width, height = LETTER
    current_page = c.getPageNumber()

    # Cream background
    c.setFillColor(CREAM)
    c.rect(0, 0, width, height, stroke=0, fill=1)

    # Watermark
    c.saveState()
    c.setFillColor(HexColor("#f2ecdc"))
    c.setFont(DISPLAY_BOLD, 82)
    c.translate(width / 2, height / 2)
    c.rotate(28)
    c.drawCentredString(0, 0, "EVEglyphDesign")
    c.restoreState()

    # Top rule
    c.setStrokeColor(LINE)
    c.setLineWidth(0.5)
    c.line(0.75 * inch, height - 0.55 * inch, width - 0.75 * inch, height - 0.55 * inch)

    # Header mark
    c.setFillColor(ORANGE)
    c.setFont(BODY_BOLD, 8)
    c.drawString(0.75 * inch, height - 0.45 * inch,
                 "EVEglyphDesign · Controlled copy · Peer-review draft")
    c.setFillColor(MUTE)
    c.drawRightString(width - 0.75 * inch, height - 0.45 * inch, KEY_ID)

    # Footer
    c.setStrokeColor(LINE)
    c.line(0.75 * inch, 0.75 * inch, width - 0.75 * inch, 0.75 * inch)
    c.setFillColor(MUTE)
    c.setFont(BODY, 7.5)
    c.drawString(0.75 * inch, 0.58 * inch,
                 f"© 2026 EVEglyphDesign · SHA-256 {content_hash[:16]}… · {ts_iso}")
    total_label = f"Page {current_page} of {total_pages}" if total_pages else f"Page {current_page}"
    c.drawRightString(width - 0.75 * inch, 0.58 * inch, total_label)
    c.setFillColor(ORANGE)
    c.setFont(DISPLAY, 8)
    c.drawCentredString(width / 2, 0.42 * inch, CLOSING)


def _build(total_pages: int, content_hash: str, ts_iso: str, path: Path) -> int:
    doc = BaseDocTemplate(
        str(path),
        pagesize=LETTER,
        leftMargin=0.75 * inch,
        rightMargin=0.75 * inch,
        topMargin=0.85 * inch,
        bottomMargin=0.9 * inch,
        title=TITLE,
        author="EVEglyphDesign",
        subject=SUBTITLE,
        keywords=", ".join(KEYWORDS),
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin,
                  doc.width, doc.height, id="body")
    template = PageTemplate(
        id="canon",
        frames=[frame],
        onPage=lambda c, d: _draw_frame(c, d, total_pages, content_hash, ts_iso),
    )
    doc.addPageTemplates([template])
    doc.build(_story())
    return doc.page


def main():
    ts_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    # Pass 1
    tmp = OUT_DIR / ".pass1.pdf"
    total = _build(0, "0" * 64, ts_iso, tmp)
    content_hash = hashlib.sha256(tmp.read_bytes()).hexdigest()
    tmp.unlink(missing_ok=True)

    # Pass 2
    _build(total, content_hash, ts_iso, OUT_PATH)

    print(f"[ok] wrote {OUT_PATH}")
    print(f"     pages  = {total}")
    print(f"     sha256 = {content_hash}")
    print(f"     ts     = {ts_iso}")


if __name__ == "__main__":
    main()
