"""Figura de la superficie libre η (vectorial, para incrustar en el PDF)."""
from math import cos, pi
from reportlab.graphics.shapes import Drawing, Line, PolyLine, String, Polygon, Circle
from reportlab.lib import colors

BLUE = colors.HexColor("#378ADD")
RED = colors.HexColor("#D85A30")
GREY = colors.HexColor("#444444")
LIGHT = colors.HexColor("#888888")


def _arrow(d, x, y0, y1, col, w=1.6, both=False):
    d.add(Line(x, y0, x, y1, strokeColor=col, strokeWidth=w))
    s = 1 if y1 > y0 else -1
    d.add(Polygon([x, y1, x - 3, y1 - 6 * s, x + 3, y1 - 6 * s], fillColor=col, strokeColor=col, strokeWidth=0.5))
    if both:
        d.add(Polygon([x, y0, x - 3, y0 + 6 * s, x + 3, y0 + 6 * s], fillColor=col, strokeColor=col, strokeWidth=0.5))


def eta_figure(width=480):
    W, Hh = 480.0, 230.0
    d = Drawing(W, Hh)
    swl, a, bot = 140.0, 42.0, 30.0   # coordenadas reportlab: y hacia arriba
    x0, x1, L = 20.0, 400.0, 190.0
    # nivel en reposo
    d.add(Line(x0, swl, 450, swl, strokeColor=GREY, strokeWidth=0.8, strokeDashArray=[5, 4]))
    # ola η = a cos(k(x - x0))
    pts = []
    n = 200
    for i in range(n + 1):
        x = x0 + (x1 - x0) * i / n
        pts += [x, swl + a * cos(2 * pi * (x - x0) / L)]
    d.add(PolyLine(pts, strokeColor=BLUE, strokeWidth=2.2))
    # fondo
    d.add(Line(x0, bot, 460, bot, strokeColor=GREY, strokeWidth=1.6))
    for xi in range(int(x0), 460, 12):
        d.add(Line(xi, bot, xi - 7, bot - 7, strokeColor=LIGHT, strokeWidth=0.5))
    # η en la cresta (x = x0 + L) y en el seno (x = x0 + 1.5L)
    xc, xs = x0 + L, x0 + 1.5 * L
    _arrow(d, xc, swl, swl + a - 1, RED)
    d.add(String(xc, swl + a + 8, "η = +H/2", fontName="DVB", fontSize=9, fillColor=RED, textAnchor="middle"))
    _arrow(d, xs, swl, swl - a + 1, RED)
    d.add(String(xs, swl - a - 14, "η = −H/2", fontName="DVB", fontSize=9, fillColor=RED, textAnchor="middle"))
    # η genérica en un punto intermedio
    xg = x0 + 0.62 * L
    yg = swl + a * cos(2 * pi * 0.62)
    _arrow(d, xg, swl, yg + 1, RED, w=1.2)
    d.add(String(xg + 5, (swl + yg) / 2 - 3, "η(x,t)", fontName="DVB", fontSize=8, fillColor=RED))
    # paso por cero
    xz = x0 + 1.25 * L
    d.add(Circle(xz, swl, 2.6, fillColor=RED, strokeColor=RED))
    d.add(String(xz + 5, swl + 5, "η = 0", fontName="DV", fontSize=7.5, fillColor=RED))
    # etiquetas
    d.add(String(x0, 210, "Superficie libre η(x,t) = (H/2)·cos(kx − ωt)", fontName="DV", fontSize=8, fillColor=BLUE))
    d.add(String(x0 + 0.45 * L, swl - 62, "Nivel en reposo: z = 0  (η = 0)", fontName="DV", fontSize=7.5, fillColor=GREY))
    d.add(Line(x0 + 0.5 * L + 10, swl - 53, x0 + 0.5 * L + 10, swl - 2, strokeColor=LIGHT, strokeWidth=0.5, strokeDashArray=[2, 2]))
    d.add(String(x0, bot - 20, "Fondo: z = −h", fontName="DV", fontSize=7.5, fillColor=GREY))
    # H (cota)
    d.add(Line(x1, swl + a, 428, swl + a, strokeColor=LIGHT, strokeWidth=0.5, strokeDashArray=[2, 2]))
    d.add(Line(xs, swl - a, 428, swl - a, strokeColor=LIGHT, strokeWidth=0.5, strokeDashArray=[2, 2]))
    _arrow(d, 420, swl - a + 1, swl + a - 1, GREY, w=0.9, both=True)
    d.add(String(425, swl + 14, "H", fontName="DVB", fontSize=10, fillColor=GREY))
    # h (cota)
    _arrow(d, 448, swl - 1, bot + 1, GREY, w=0.9, both=True)
    d.add(String(453, (swl + bot) / 2, "h", fontName="DVB", fontSize=10, fillColor=GREY))
    # z
    _arrow(d, 8, swl, swl + 34, GREY, w=0.8)
    d.add(String(1, swl + 38, "z", fontName="DVI", fontSize=8, fillColor=GREY))
    s = width / W
    d.scale(s, s)
    d.width, d.height = W * s, Hh * s
    return d
