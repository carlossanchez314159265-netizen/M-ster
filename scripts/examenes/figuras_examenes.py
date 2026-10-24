"""Figuras de los exámenes resueltos (matplotlib → PNG → ReportLab)."""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Ellipse
from reportlab.platypus import Image
from reportlab.lib.units import mm

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_png")
os.makedirs(OUT, exist_ok=True)
NAVY, TEAL, RED, SAND = "#0B3954", "#0E7C86", "#B23A2E", "#CBBFAE"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9})


def _img(fig, name, width_mm):
    p = os.path.join(OUT, name)
    fig.savefig(p, dpi=220, bbox_inches="tight")
    plt.close(fig)
    w, h = fig.get_size_inches()
    im = Image(p)
    ratio = im.imageHeight / im.imageWidth
    return Image(p, width=width_mm * mm, height=width_mm * mm * ratio)


def sensores(width=140):
    fig, ax = plt.subplots(figsize=(7, 3.4))
    x = np.linspace(0, 10, 400)
    ax.fill_between(x, -4.6, 0.25 * np.sin(2.2 * x), color="#E6F0F5")
    ax.plot(x, 0.25 * np.sin(2.2 * x), color=NAVY, lw=1.6)
    ax.axhline(0, color="grey", ls="--", lw=0.7)
    ax.fill_between([0, 10], -5, -4.6, color=SAND)
    ax.plot([0, 10], [-4.6, -4.6], color="k", lw=1.6)
    ax.annotate("", (0.5, 1.2), (0.5, -0.1), arrowprops=dict(arrowstyle="->"))
    ax.text(0.6, 1.1, "z", fontsize=10)
    ax.text(9.5, 0.4, "x", fontsize=10)
    ax.plot(3, -4.6, "o", color="k", ms=8)
    ax.text(1.6, -4.25, "Sensor #1 (fondo, p₁)", fontsize=9)
    ax.plot(6, -2.6, "o", color=RED, ms=8)
    ax.text(6.25, -2.7, "Sensor #2 (p₂)", color=RED, fontsize=9)
    ax.annotate("", (5.6, -2.6), (5.6, -4.6), arrowprops=dict(arrowstyle="<->"))
    ax.text(4.55, -3.7, "7,62 m", fontsize=9)
    ax.annotate("", (5.6, 0), (5.6, -2.6), arrowprops=dict(arrowstyle="<->"))
    ax.text(5.0, -1.4, "|z₂|", fontsize=9)
    ax.annotate("", (8.6, 0), (8.6, -4.6), arrowprops=dict(arrowstyle="<->"))
    ax.text(8.75, -2.4, "h", fontsize=10)
    ax.text(0.9, 0.45, "superficie libre (z = 0)", color=NAVY, fontsize=8.5)
    ax.set_xlim(0, 10); ax.set_ylim(-5, 1.4); ax.axis("off")
    return _img(fig, "sensores.png", width)


def _cono(ax, cx, base_w, base_h, altura, color, label_top, label_base, titulo):
    ax.add_patch(Ellipse((cx, 0), base_w, base_h, fc=color, ec=NAVY, alpha=0.55, lw=1))
    ax.add_patch(Polygon([[cx - base_w / 2, 0], [cx + base_w / 2, 0], [cx, altura]], fc=color, ec=NAVY, alpha=0.75, lw=1))
    ax.text(cx, altura + 0.12, label_top, ha="center", fontsize=8.5)
    ax.text(cx, -base_h / 2 - 0.35, label_base, ha="center", fontsize=8.5)
    ax.text(cx, altura + 0.55, titulo, ha="center", fontsize=9.5, weight="bold", color=NAVY)


def conos_y_rosa(width=165):
    fig = plt.figure(figsize=(9, 3.9))
    ax = fig.add_axes([0.0, 0.05, 0.55, 0.9])
    _cono(ax, 1.4, 1.4, 0.35, 2.6, "#9DC3DE", "S$_p$ = 0,075 m²/(grd·s)",
          "A$_b$ = 40 grd·s ; ω$_p$ = 2π/16", "Pico 310°")
    _cono(ax, 4.3, 2.6, 0.6, 1.1, "#E8B996", "S$_p$ = 0,00938 m²/(grd·s)",
          "A$_b$ = 80 grd·s ; ω$_p$ = 2π/8", "Pico 230°")
    ax.set_xlim(0, 5.9); ax.set_ylim(-1, 3.4); ax.set_aspect("equal"); ax.axis("off")
    ax2 = fig.add_axes([0.58, 0.05, 0.4, 0.88], projection="polar")
    ax2.set_theta_zero_location("N"); ax2.set_theta_direction(-1)
    ax2.set_rlim(0, 18); ax2.set_rticks([4, 8, 12, 16])
    ax2.set_thetagrids(range(0, 360, 30), ["N", "30", "60", "E", "120", "150", "S", "210", "240", "W", "300", "330"])
    ax2.plot(np.radians(310), 16, "o", color=NAVY, ms=8)
    ax2.text(np.radians(328), 12.5, "310°, 16 s", color=NAVY, fontsize=8.5, ha="left")
    ax2.plot(np.radians(230), 8, "o", color=RED, ms=8)
    ax2.text(np.radians(210), 9.5, "230°, 8 s", color=RED, fontsize=8.5, ha="left")
    ax2.set_title("Rosa periodos (radio, s) – dirección", fontsize=8.5, pad=12)
    ax2.tick_params(labelsize=7.5)
    return _img(fig, "conos_rosa.png", width)


def espectro(width=140):
    fig, ax = plt.subplots(figsize=(7, 3.3))
    w = np.linspace(0, 9, 600)
    S = np.where(w < 2, 1.5 * w, np.where(w < 8, 4 - w / 2, 0))
    ax.fill_between(w, 0, S, color="#DCE8F1")
    ax.plot(w, S, color=NAVY, lw=1.8)
    ax.plot([2, 2], [0, 3], ls="--", color=RED, lw=1)
    ax.plot(2, 3, "o", color=RED)
    ax.annotate("pico: ω$_p$ = 2 rad/s → T$_p$ = 2π/2 = 3,14 s", (2, 3), (3.2, 3.25), color=RED,
                arrowprops=dict(arrowstyle="->", color=RED), fontsize=9)
    ax.text(0.45, 0.45, "S = 1,5ω", color=NAVY)
    ax.text(5.1, 1.9, "S = 4 − ω/2", color=NAVY, rotation=-17)
    ax.text(3.3, 0.6, "área = m₀ = ½·8·3 = 12", color=NAVY)
    ax.set_xlabel("ω (rad/s)"); ax.set_ylabel("S(ω)")
    ax.set_xlim(0, 9); ax.set_ylim(0, 3.7); ax.grid(alpha=0.3)
    return _img(fig, "espectro.png", width)


def mapa_examen(width=165):
    """Mapa visual: qué tema cae en cada ejercicio en los dos exámenes."""
    fig, ax = plt.subplots(figsize=(9, 2.5))
    filas = ["Dispersión / presión\n(teoría lineal)", "Rayleigh + H$_{max}$\n(estadístico)", "Espectro: m₀, H$_{m0}$, E, T$_p$\n(espectral)"]
    cols = ["Parcial 29-10-2025", "Final ordinario 13-01"]
    txt = [["Ej. 2: sensores de presión\n→ k, h, H, L", "Ej. 1: L₀ → T, L → h"],
           ["Ej. 1: rebase de cubierta\n(q y cota sin rebase)", "Ej. 2: runup = η$_{max}$ + u²/2g\n(+ u orbital lineal)"],
           ["Ej. 3: dos conos SEA/SWELL\n(m₀ = ⅓·A$_b$·S$_p$)", "Ej. 3: S(ω) por tramos\n(m₀, m₁, m₂, T$_p$, T₀₂)"]]
    cmap = ["#D6EAF0", "#FCE6D2", "#E3E0F3"]
    for i, f in enumerate(filas):
        ax.text(-0.05, 2 - i, f, ha="right", va="center", fontsize=8.5, weight="bold", color=NAVY)
        for j in range(2):
            ax.add_patch(plt.Rectangle((j * 1.05, 2 - i - 0.42), 1.0, 0.84, fc=cmap[i], ec="white"))
            ax.text(j * 1.05 + 0.5, 2 - i, txt[i][j], ha="center", va="center", fontsize=8)
    for j, c in enumerate(cols):
        ax.text(j * 1.05 + 0.5, 2.62, c, ha="center", fontsize=9, weight="bold", color=TEAL)
    ax.set_xlim(-1.0, 2.15); ax.set_ylim(-0.5, 2.8); ax.axis("off")
    return _img(fig, "mapa.png", width)
