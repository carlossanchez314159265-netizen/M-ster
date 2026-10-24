"""Estilo común de los resúmenes de Oceanografía (mismo aspecto que los PDF ya subidos)."""
import re
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer,
                                Table, TableStyle, KeepTogether, PageBreak)
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping

FD = "/usr/share/fonts/truetype/dejavu/"
pdfmetrics.registerFont(TTFont("DV", FD + "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DVB", FD + "DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DVI", FD + "DejaVuSans-Oblique.ttf"))
pdfmetrics.registerFont(TTFont("DVBI", FD + "DejaVuSans-BoldOblique.ttf"))
addMapping("DV", 0, 0, "DV"); addMapping("DV", 1, 0, "DVB")
addMapping("DV", 0, 1, "DVI"); addMapping("DV", 1, 1, "DVBI")

NAVY = colors.HexColor("#0B3954")
TEAL = colors.HexColor("#0E7C86")
ZEBRA = colors.HexColor("#EAF4F5")
GRID = colors.HexColor("#B9D3D6")
FBG = colors.HexColor("#F3F7F8")
WARN = colors.HexColor("#FFF4E0")
TBG = colors.HexColor("#FAFCFC")

H1 = ParagraphStyle("H1", fontName="DVB", fontSize=20, textColor=NAVY, leading=24, spaceAfter=2)
SUB = ParagraphStyle("SUB", fontName="DV", fontSize=9.5, textColor=colors.HexColor("#555555"), leading=12, spaceAfter=8)
H2 = ParagraphStyle("H2", fontName="DVB", fontSize=13.5, textColor=NAVY, leading=17, spaceBefore=10, spaceAfter=4, keepWithNext=1)
H3 = ParagraphStyle("H3", fontName="DVB", fontSize=10.5, textColor=TEAL, leading=13, spaceBefore=7, spaceAfter=3, keepWithNext=1)
B = ParagraphStyle("B", fontName="DV", fontSize=8.8, leading=12.2, spaceAfter=3)
BL = ParagraphStyle("BL", parent=B, leftIndent=11, bulletIndent=2, spaceAfter=1.5)
BL2 = ParagraphStyle("BL2", parent=B, leftIndent=24, bulletIndent=14, spaceAfter=1)
F = ParagraphStyle("F", fontName="DV", fontSize=9.6, leading=13.5, alignment=TA_CENTER)
TC = ParagraphStyle("TC", fontName="DV", fontSize=8, leading=10.4)
TH = ParagraphStyle("TH", fontName="DVB", fontSize=8, leading=10.4, textColor=colors.white)
TL = ParagraphStyle("TL", fontName="DVB", fontSize=7.6, leading=9.8, textColor=TEAL)
TS = ParagraphStyle("TS", fontName="DVB", fontSize=7.8, leading=10, textColor=NAVY)
TD = ParagraphStyle("TD", fontName="DV", fontSize=7.8, leading=10)
CAP = ParagraphStyle("CAP", fontName="DVI", fontSize=7.8, leading=10, alignment=TA_CENTER,
                     textColor=colors.HexColor("#555555"), spaceAfter=4)

story = []


def _heads():
    """Saca de la historia los títulos (H2/H3) inmediatamente anteriores para pegarlos al bloque siguiente."""
    out = []
    while story and isinstance(story[-1], Paragraph) and story[-1].style.name in ("H2", "H3", "BK"):
        out.insert(0, story.pop())
    return out


BK = ParagraphStyle("BK", parent=B, keepWithNext=1)


def P(t, s=B):
    if s is B and re.sub(r"<[^>]+>", "", t).rstrip().endswith(":"):
        s = BK   # una frase que presenta lo siguiente no se queda sola al final de página
    story.append(Paragraph(t, s))


def bl(*items):
    for t in items:
        story.append(Paragraph(t, BL, bulletText="•"))


def bl2(*items):
    for t in items:
        story.append(Paragraph(t, BL2, bulletText="–"))


def h2(t): story.append(Paragraph(t, H2))
def h3(t): story.append(Paragraph(t, H3))


def fbox(lines, bg=FBG):
    rows = [[Paragraph(re.sub(r" {2,}", "&nbsp;&nbsp;&nbsp;&nbsp;", l), F)] for l in lines]
    t = Table(rows, colWidths=[170 * mm])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), bg),
                           ("BOX", (0, 0), (-1, -1), 0.4, GRID),
                           ("TOPPADDING", (0, 0), (-1, -1), 2.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5)]))
    kt = KeepTogether(_heads() + [Spacer(1, 2), t, Spacer(1, 4)])
    kt._es_formula = True
    story.append(kt)


def terms(pairs, title="Términos"):
    """Leyenda de una ecuación: lista de (símbolo, significado [unidades]) en dos columnas."""
    cells = [[Paragraph(s, TS), Paragraph(d, TD)] for s, d in pairs]
    half = (len(cells) + 1) // 2
    left, right = cells[:half], cells[half:]
    rows = []
    for i in range(half):
        r = left[i] + (right[i] if i < len(right) else [Paragraph("", TD), Paragraph("", TD)])
        rows.append(r)
    data = [[Paragraph(title, TL), "", "", ""]] + rows
    t = Table(data, colWidths=[25 * mm, 60 * mm, 25 * mm, 60 * mm])
    t.setStyle(TableStyle([("SPAN", (0, 0), (-1, 0)),
                           ("BACKGROUND", (0, 0), (-1, -1), TBG),
                           ("BOX", (0, 0), (-1, -1), 0.4, GRID),
                           ("LINEBEFORE", (0, 0), (0, -1), 2.5, TEAL),
                           ("VALIGN", (0, 0), (-1, -1), "TOP"),
                           ("TOPPADDING", (0, 0), (-1, -1), 1.4), ("BOTTOMPADDING", (0, 0), (-1, -1), 1.4),
                           ("LEFTPADDING", (0, 0), (-1, -1), 5)]))
    if story and getattr(story[-1], "_es_formula", False):
        prev = story.pop()
        story.append(KeepTogether(prev._content + [t, Spacer(1, 5)]))
    elif (len(story) >= 2 and isinstance(story[-1], Spacer) and isinstance(story[-2], Table)
          and len(story[-2]._cellvalues) == 1):
        sp = story.pop(); prev = story.pop()
        story.append(KeepTogether(_heads() + [prev, t, Spacer(1, 5)]))
    elif story and not isinstance(story[-1], (Spacer, PageBreak)):
        prev = story.pop()
        story.append(KeepTogether(_heads() + [prev, t, Spacer(1, 5)]))
    else:
        story.append(KeepTogether([t, Spacer(1, 5)]))


def note(text, bg=WARN):
    t = Table([[Paragraph(text, B)]], colWidths=[170 * mm])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), bg), ("LEFTPADDING", (0, 0), (-1, -1), 6),
                           ("LINEBEFORE", (0, 0), (0, -1), 2.5, colors.HexColor("#E0A030")),
                           ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4)]))
    story.append(Spacer(1, 2)); story.append(t); story.append(Spacer(1, 4))


def table(head, rows, widths):
    data = [[Paragraph(h, TH) for h in head]] + [[Paragraph(c, TC) for c in r] for r in rows]
    t = Table(data, colWidths=[w * mm for w in widths], repeatRows=1)
    st = [("BACKGROUND", (0, 0), (-1, 0), TEAL), ("GRID", (0, 0), (-1, -1), 0.4, GRID),
          ("VALIGN", (0, 0), (-1, -1), "TOP"),
          ("TOPPADDING", (0, 0), (-1, -1), 2.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 2.5)]
    for i in range(2, len(data), 2):
        st.append(("BACKGROUND", (0, i), (-1, i), ZEBRA))
    t.setStyle(TableStyle(st))
    if not (story and isinstance(story[-1], Paragraph) and story[-1].style.name in ("H2", "H3")):
        story.append(Spacer(1, 2))
    story.append(t)
    story.append(Spacer(1, 5))


def figure(flowable, caption=None):
    items = [flowable]
    items = _heads() + items
    if caption:
        items.append(Paragraph(caption, CAP))
    story.append(KeepTogether(items))


def build(path, footer_text, title):
    def footer(c, d):
        c.saveState()
        c.setFont("DV", 7); c.setFillColor(colors.HexColor("#666666"))
        c.drawString(20 * mm, 12 * mm, footer_text)
        c.drawRightString(190 * mm, 12 * mm, str(d.page))
        c.setStrokeColor(GRID); c.setLineWidth(0.4); c.line(20 * mm, 15 * mm, 190 * mm, 15 * mm)
        c.restoreState()
    doc = BaseDocTemplate(path, pagesize=A4, leftMargin=20 * mm, rightMargin=20 * mm, topMargin=16 * mm,
                          bottomMargin=20 * mm, title=title, author="Carlos Sánchez Campos")
    fr = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")
    doc.addPageTemplates([PageTemplate(id="p", frames=[fr], onPage=footer)])
    doc.build(story)
    print("ok", path)


def box(text, kind="tip"):
    """Recuadro con borde completo: 'tip' (verde azulado) o 'warn' (ámbar)."""
    bg, bd = (ZEBRA, TEAL) if kind == "tip" else (WARN, colors.HexColor("#E0A030"))
    t = Table([[Paragraph(text, B)]], colWidths=[170 * mm])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), bg), ("BOX", (0, 0), (-1, -1), 0.8, bd),
                           ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7),
                           ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]))
    story.append(Spacer(1, 3)); story.append(t); story.append(Spacer(1, 5))
