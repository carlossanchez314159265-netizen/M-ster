"""Formulario compacto del 1er parcial de Oceanografía: solo fórmulas, a dos columnas.

Uso: python3 formulario_compacto.py "../../parcial 1/12 - Formulario compacto 1er parcial.pdf"
"""
import sys
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Table, TableStyle, Spacer, KeepTogether
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.fonts import addMapping

FD = "/usr/share/fonts/truetype/dejavu/"
for n, f in [("DV", "DejaVuSans"), ("DVB", "DejaVuSans-Bold")]:
    pdfmetrics.registerFont(TTFont(n, FD + f + ".ttf"))
addMapping("DV", 0, 0, "DV"); addMapping("DV", 1, 0, "DVB"); addMapping("DV", 0, 1, "DV"); addMapping("DV", 1, 1, "DVB")

NAVY, TEAL, GRID, ZEBRA = (colors.HexColor(c) for c in ("#0B3954", "#0E7C86", "#B9D3D6", "#EAF4F5"))
H = ParagraphStyle("H", fontName="DVB", fontSize=8.6, leading=10.5, textColor=colors.white, backColor=NAVY,
                   borderPadding=(1.5, 3, 1.5, 3), spaceBefore=5, spaceAfter=3, keepWithNext=1)
S = ParagraphStyle("S", fontName="DVB", fontSize=7.4, leading=9, textColor=TEAL, spaceBefore=2.5, spaceAfter=0.5, keepWithNext=1)
F = ParagraphStyle("F", fontName="DV", fontSize=7.6, leading=11.2, leftIndent=6, firstLineIndent=-6, spaceAfter=0.6)
T = ParagraphStyle("T", fontName="DV", fontSize=6.9, leading=9.6)
TB = ParagraphStyle("TB", fontName="DVB", fontSize=6.9, leading=9.6, textColor=colors.white)

COLW = (A4[0] - 20 * mm - 6 * mm) / 2
story = []


def h(t): story.append(Paragraph(t, H))
def s(t): story.append(Paragraph(t, S))
def f(*ls):
    for l in ls:
        story.append(Paragraph(l, F))


def tab(head, rows, w):
    data = [[Paragraph(x, TB) for x in head]] + [[Paragraph(x, T) for x in r] for r in rows]
    t = Table(data, colWidths=[x * COLW for x in w])
    st = [("BACKGROUND", (0, 0), (-1, 0), TEAL), ("GRID", (0, 0), (-1, -1), 0.3, GRID), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
          ("TOPPADDING", (0, 0), (-1, -1), 1), ("BOTTOMPADDING", (0, 0), (-1, -1), 1.2),
          ("LEFTPADDING", (0, 0), (-1, -1), 2.5), ("RIGHTPADDING", (0, 0), (-1, -1), 2.5)]
    st += [("BACKGROUND", (0, i), (-1, i), ZEBRA) for i in range(2, len(data), 2)]
    t.setStyle(TableStyle(st))
    story.append(Spacer(1, 1.5)); story.append(KeepTogether(t)); story.append(Spacer(1, 2))


sub = lambda x: f"<sub>{x}</sub>"
sup = lambda x: f"<super>{x}</super>"

# ------------------------------------------------------------------ 0
h("0 · Constantes")
f("g = 9,81 m/s²  ·  ρ ≈ 1025 kg/m³ (dulce 1000)  ·  a = H/2  ·  ω = 2π/T = 2πf  ·  k = 2π/L  ·  c = L/T = ω/k",
  "z = 0 en superficie, −h en el fondo  ·  calculadora en <b>RAD</b>  ·  1 dbar ≈ 1 m")

# ------------------------------------------------------------------ 1
h("1 · Agua de mar")
f("σ = ρ − 1000  ·  ρ(S,T,p) = ρ(S,T,0) / [1 − p/K(S,T,p)]  ·  ρ(S,T,0) = A + BS + CS" + sup("3/2") + " + DS²",
  "ρ ↑ con S y p, ↓ con T",
  "Mezcla: T = (m₁T₁ + m₂T₂)/(m₁ + m₂)  ·  S = (m₁S₁ + m₂S₂)/(m₁ + m₂)  ·  %A = b/(a+b)·100",
  "Flotabilidad neutra: m" + sub("lastre") + " = ρ" + sub("agua") + "·V − m" + sub("cuerpo"))

# ------------------------------------------------------------------ 2
h("2 · Dispersión")
f("<b>ω² = gk·tanh(kh)</b>  ·  L = (gT²/2π)·tanh(kh)  ·  c = (gT/2π)·tanh(kh)  ·  L/L₀ = c/c₀ = tanh(kh)")
tab(["Zona", "h/L", "Dispersión", "L", "c"], [
    ["Indefinidas", "&gt; 1/2", "ω² = gk", "L₀ = gT²/2π = 1,56T²", "gT/2π = 1,56T"],
    ["Intermedias", "1/20–1/2", "completa", "L₀·tanh(kh)", "c₀·tanh(kh)"],
    ["Reducidas", "&lt; 1/20", "ω² = gk²h", "T√(gh)", "√(gh)"],
], [0.18, 0.15, 0.19, 0.27, 0.21])
f("k, T → h:  <b>h = arctanh[ω²/(gk)] / k</b>   (ω²/gk ∈ (0,1))  ·  k, h → T:  ω = √(gk·tanh kh)",
  "T, h → k (Newton):  k" + sub("n+1") + " = k" + sub("n") + " − f/f'  ·  f = ω² − gk·tanh(kh)  ·  f' = −g·tanh(kh) − ghk·sech²(kh)  ·  k₀ = ω²/g",
  "Fenton-McKee: L ≈ L₀·[tanh((2πh/L₀)" + sup("3/4") + ")]" + sup("2/3"),
  "Guo: kh ≈ (ω²h/g)·[1 − exp(−(ω√(h/g))" + sup("5/2") + ")]" + sup("−2/5"),
  "Peralte ε = H/L (rotura ≈ 1/7)  ·  Ursell U = HL²/h³")
s("Problema de contorno")
f("∇²φ = 0  ·  u = ∂φ/∂x, w = ∂φ/∂z  ·  fondo w = 0  ·  w = ∂η/∂t  ·  ∂φ/∂t + gη = 0  (z = 0)",
  "φ = (gH/2ω)·cosh k(h+z)/cosh kh·sin(kx − ωt)  ·  η = (H/2)·cos(kx − ωt)")

# ------------------------------------------------------------------ 3
h("3 · Cinemática y presiones  (θ = kx − ωt)")
f("<b>u</b> = (H/2)ω·cosh k(h+z)/sinh kh·cos θ  ·  <b>w</b> = (H/2)ω·sinh k(h+z)/sinh kh·sin θ",
  "a" + sub("x") + " = (H/2)ω²·cosh k(h+z)/sinh kh·sin θ  ·  a" + sub("z") + " = −(H/2)ω²·sinh k(h+z)/sinh kh·cos θ",
  "u" + sub("max,sup") + " = (H/2)ω·coth kh  ·  u" + sub("max,fondo") + " = (H/2)ω/sinh kh",
  "<b>A</b> = (H/2)·cosh k(h+z)/sinh kh  ·  <b>B</b> = (H/2)·sinh k(h+z)/sinh kh  ·  B/A = tanh k(h+z)",
  "Indef.: círculos r = (H/2)e" + sup("kz") + "  ·  Red.: A = H/(2kh), B = (H/2)(1 + z/h)",
  "<b>p = −ρgz + ρg(H/2)·K" + sub("p") + "·cos θ</b>  ·  K" + sub("p") + " = cosh k(h+z)/cosh kh  ·  fondo K" + sub("p") + " = 1/cosh kh",
  "Dos sensores: p₁/p₂ = cosh k(h+z₁)/cosh k(h+z₂)",
  "Onda larga: c = √(g·h(x))  ·  <b>t = ∫dx/√(g·h(x))</b>  ·  talud lineal: t = 2√h₀/(s√g)")

# ------------------------------------------------------------------ 4
h("4 · Superposición y energía")
f("Estacionaria: η = H" + sub("i") + "·cos kx·cos ωt  ·  antinodo 2H" + sub("i") + ", nodo 0  ·  nodo↔antinodo L/4",
  "<b>Cuasi-estacionaria</b>: η = (H" + sub("i") + "/2)cos(kx − ωt) + (H" + sub("r") + "/2)cos(kx + ωt + ε)",
  "  ancho máx = H" + sub("i") + " + H" + sub("r") + "  ·  ancho mín = H" + sub("i") + " − H" + sub("r") + "  ·  máx↔mín = L/4  ·  K" + sub("r") + " = H" + sub("r") + "/H" + sub("i") + "  ·  K" + sub("t") + " = H" + sub("t") + "/H" + sub("i"),
  "Crestas cortas: η = 2A·cos(k sinθ·y)·cos(k cosθ·x − ωt)",
  "<b>Grupo</b>: η = H·cos(kx − ωt)·cos[½(Δk·x − Δω·t)]  ·  ω = (ω₁+ω₂)/2  ·  Δω = ω₂−ω₁  ·  Δk = k₂−k₁",
  "c = ω/k  ·  c" + sub("g") + " = Δω/Δk  ·  L" + sub("g") + " = 2π/Δk  ·  T" + sub("g") + " = 2π/Δω = T₁T₂/(T₁−T₂)  ·  T" + sub("mod") + " = 4π/Δω",
  "<b>n = ½[1 + 2kh/sinh 2kh]</b>  ·  c" + sub("g") + " = n·c  ·  indef. n = ½  ·  red. n = 1",
  "<b>E = ρgH²/8</b> [J/m²]  ·  E" + sub("c") + " = E" + sub("p") + " = ρgH²/16  ·  <b>F = E·c" + sub("g") + "</b> [W/m]  ·  indef. P = ρg²H²T/32π",
  "Asomeramiento: H₂/H₁ = √(c" + sub("g1") + "/c" + sub("g2") + ")  ·  flujo de masa M = ρgH²/(8c)",
  "Con corriente: (ω − kU cosθ)² = gk·tanh(kh)")

# ------------------------------------------------------------------ 5
h("5 · Estadística")
f("H" + sub("m") + " = ΣH" + sub("i") + "/N  ·  <b>H" + sub("1/3") + "</b> = media del 1/3 mayor  ·  <b>H" + sub("rms") + " = √(ΣH" + sub("i") + "²/N)</b>  ·  T" + sub("m") + " = ΣT" + sub("i") + "/N",
  "η normal: f(η) = exp(−η²/2η" + sub("rms") + "²) / (η" + sub("rms") + "√2π)  ·  η" + sub("rms") + " = √m₀",
  "<b>Rayleigh</b>: F(H) = 1 − exp[−(H/H" + sub("rms") + ")²]  ·  f(H) = (2H/H" + sub("rms") + "²)·exp[−(H/H" + sub("rms") + ")²]",
  "<b>q = exp[−(H" + sub("q") + "/H" + sub("rms") + ")²]</b>  ·  <b>H" + sub("q") + " = H" + sub("rms") + "√(−ln q)</b>")
tab(["Rayleigh", "/H" + sub("rms"), "Rayleigh", "Valor"], [
    ["H" + sub("m"), "0,886", "H" + sub("1/3") + "/H" + sub("rms"), "<b>1,416 ≈ √2</b>"],
    ["H" + sub("1/10"), "1,800", "H" + sub("1/3") + "/η" + sub("rms"), "4,004"],
    ["H" + sub("1/100"), "2,359", "H" + sub("rms") + "/η" + sub("rms"), "2√2 = 2,83"],
    ["H" + sub("1/3") + "/H" + sub("m"), "1,597", "H" + sub("1/10") + "/H" + sub("1/3"), "1,271"],
], [0.22, 0.2, 0.3, 0.28])
f("F(H" + sub("max") + ") = {1 − exp[−(H" + sub("max") + "/H" + sub("rms") + ")²]}" + sup("N") + "  ·  <b>N = duración/T" + sub("m") + "</b>",
  "Moda: H" + sub("max") + "/H" + sub("rms") + " = √(ln N)  ·  <b>Media: √(ln N) + (C/2)(ln N)" + sup("−1/2") + "</b>  ·  C = 0,5772")
tab(["N", "100", "500", "1000", "2000", "5000"], [
    ["media", "2,280", "2,609", "2,738", "2,862", "3,017"],
    ["moda", "2,146", "2,493", "2,628", "2,757", "2,918"],
], [0.2, 0.16, 0.16, 0.16, 0.16, 0.16])
f("Cresta = H/2  ·  rebase si H/2 &gt; Z" + sub("cub") + "  ·  R" + sub("u") + " = η" + sub("max") + " + u²/2g  ·  freak: H/H" + sub("s") + " &gt; 2 ó η" + sub("c") + "/H" + sub("s") + " &gt; 1,25")

# ------------------------------------------------------------------ 6
h("6 · Espectral")
f("<b>m" + sub("n") + " = ∫ω" + sup("n") + "S(ω)dω</b>  ·  m₀ = área = η" + sub("rms") + "²  ·  <b>H" + sub("m0") + " = 4√m₀</b>  ·  E = ρg·m₀",
  "Parseval: m₀ = Σa" + sub("i") + "²/2 = ΣH" + sub("i") + "²/8  ·  mar mixto: m₀ = m" + sub("0,sea") + " + m" + sub("0,swell") + " → H" + sub("m0") + " = √(H" + sub("sea") + "² + H" + sub("swell") + "²)",
  "Onda regular: H" + sub("m0") + " = √2·H")
tab(["", "S(ω)", "S(f)"], [
    ["T" + sub("p"), "2π/ω" + sub("p"), "1/f" + sub("p")],
    ["T" + sub("01") + " = T" + sub("m"), "2π·m₀/m₁", "m₀/m₁"],
    ["T" + sub("02") + " = T" + sub("z"), "2π·√(m₀/m₂)", "√(m₀/m₂)"],
    ["T" + sub("c") + " = T" + sub("24"), "2π·√(m₂/m₄)", "√(m₂/m₄)"],
    ["T" + sub("e") + " = T" + sub("−10"), "2π·m" + sub("−1") + "/m₀", "m" + sub("−1") + "/m₀"],
    ["T" + sub("ij"), "2π(m" + sub("i") + "/m" + sub("j") + ")" + sup("1/(j−i)"), "sin 2π"],
], [0.3, 0.4, 0.3])
f("T" + sub("c") + " &lt; T" + sub("z") + " &lt; T" + sub("01") + " &lt; T" + sub("e") + " &lt; T" + sub("p"),
  "<b>ε = √[1 − m₂²/(m₀m₄)]</b>  ·  ν = √(m₀m₂/m₁² − 1)  ·  S(f) = 2π·S(ω)  ·  m" + sub("n") + "(ω) = (2π)" + sup("n") + "m" + sub("n") + "(f)",
  "P = ρg∫c" + sub("g") + "S dω  ·  indef. P = ρg²H" + sub("m0") + "²T" + sub("e") + "/64π ≈ 0,49·H" + sub("m0") + "²T" + sub("e") + " [kW/m]",
  "<b>PM</b>: S(ω) = 0,0081g²ω" + sup("−5") + "·exp[−1,25(ω/ω" + sub("p") + ")" + sup("−4") + "]  ·  ω" + sub("p") + " = 0,879g/U" + sub("19,5") + "  ·  H" + sub("m0") + " ≈ 0,04T" + sub("p") + "²",
  "<b>JONSWAP</b>: S" + sub("PM") + "(α)·γ" + sup("δ") + "  ·  δ = exp[−(ω−ω" + sub("p") + ")²/(2σ₀²ω" + sub("p") + "²)]  ·  γ = 3,3  ·  σ₀ = 0,07 / 0,09",
  "TMA = JONSWAP·φ(ω,h)  ·  Goda: S(f) = β" + sub("J") + "H" + sub("s") + "²T" + sub("p") + sup("−4") + "f" + sup("−5") + "·exp[−1,25(T" + sub("p") + "f)" + sup("−4") + "]·γ" + sup("δ"),
  "f" + sub("Nyq") + " = 1/(2Δt)  ·  Δf = 1/T" + sub("reg") + "  ·  Welch K tramos: Δf = K/T" + sub("reg") + ", error ∝ 1/√K")


def pie(c, d):
    c.saveState()
    c.setFont("DVB", 9.5); c.setFillColor(NAVY)
    c.drawString(10 * mm, A4[1] - 9 * mm, "Oceanografía · Formulario compacto 1er parcial")
    c.setFont("DV", 6.5); c.setFillColor(colors.grey)
    c.drawRightString(A4[0] - 10 * mm, A4[1] - 9 * mm, f"pág. {d.page}")
    c.setStrokeColor(GRID); c.line(A4[0] / 2, 8 * mm, A4[0] / 2, A4[1] - 12 * mm)
    c.restoreState()


out = sys.argv[1] if len(sys.argv) > 1 else "formulario_compacto.pdf"
doc = BaseDocTemplate(out, pagesize=A4, title="Oceanografía — Formulario compacto 1er parcial", author="Carlos Sánchez Campos")
fr = [Frame(10 * mm, 8 * mm, COLW, A4[1] - 21 * mm, id="c1", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0),
      Frame(16 * mm + COLW, 8 * mm, COLW, A4[1] - 21 * mm, id="c2", leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)]
doc.addPageTemplates([PageTemplate(frames=fr, onPage=pie)])
doc.build(story)
