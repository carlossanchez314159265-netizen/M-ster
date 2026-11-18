"""Esquema: qué borrar y qué conservar al rehacer la cubierta en el cono (vista en planta)."""
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

zd = -1500
EXAG = 12.0  # exageración de la curvatura para que se vea el hueco
def r(x): return 5000 if x <= 15000 else 5000 - 2500*(x - 15000)/6000
def yt(x): return math.sqrt(r(x)**2 - zd**2)
def chord(x):
    if x <= 18000: a, b = 15000, 18000
    else: a, b = 18000, 21000
    return yt(a) + (yt(b) - yt(a))*(x - a)/(b - a)
def yexag(x): return chord(x) + EXAG*(yt(x) - chord(x))

fig, ax = plt.subplots(figsize=(14, 8.6))
GREEN, RED, BLUE, ORANGE = "#2f9e44", "#e03131", "#1971c2", "#f08c00"

# rectángulo del cilindro (se conserva) — sólo el tramo final
ax.fill([12000, 15000, 15000, 12000], [-yt(0), -yt(0), yt(0), yt(0)], color=GREEN, alpha=0.18)
ax.plot([12000, 15000], [yt(0)]*2, color=GREEN, lw=2); ax.plot([12000, 15000], [-yt(0)]*2, color=GREEN, lw=2)
ax.text(13300, 0, "Rectángulo\ndel cilindro\nSE CONSERVA", ha="center", va="center", color=GREEN, fontsize=12, weight="bold")

# trapecios viejos (superficies a borrar)
for a, b in ((15000, 18000), (18000, 21000)):
    ax.fill([a, b, b, a], [-yt(a), -yt(b), yt(b), yt(a)], color=RED, alpha=0.13, hatch="///", edgecolor=RED, lw=0)
ax.text(16500, 0, "Trapecio viejo B\nBORRAR superficie", ha="center", va="center", color=RED, fontsize=11, weight="bold")
ax.text(19500, 0, "Trapecio viejo C\nBORRAR superficie", ha="center", va="center", color=RED, fontsize=11, weight="bold")

# bordes inclinados rectos (curvas a borrar)
for a, b in ((15000, 18000), (18000, 21000)):
    for s in (1, -1):
        ax.plot([a, b], [s*yt(a), s*yt(b)], color=RED, lw=3, ls=(0, (6, 3)))
ax.annotate("4 bordes RECTOS inclinados\nBORRAR estas curvas", (16500, chord(16500)), (14200, 2400),
            color=RED, fontsize=10.5, weight="bold", arrowprops=dict(arrowstyle="->", color=RED))
ax.annotate("", (19500, -chord(19500)), (16200, -2600), arrowprops=dict(arrowstyle="->", color=RED))
ax.text(14200, -2900, "(y los otros dos del costado −)", color=RED, fontsize=9.5)

# splines nuevas (se conservan)
for a, b in ((15000, 18000), (18000, 21000)):
    xs = np.linspace(a, b, 60)
    for s in (1, -1):
        ax.plot(xs, [s*yexag(x) for x in xs], color=ORANGE, lw=3.2)
ax.text(16550, yexag(16500) + 330, "spline 1", color=ORANGE, fontsize=11, weight="bold", ha="center")
ax.text(19550, yexag(19500) + 330, "spline 2", color=ORANGE, fontsize=11, weight="bold", ha="center")
ax.text(16550, -yexag(16500) - 520, "spline 3", color=ORANGE, fontsize=11, weight="bold", ha="center")
ax.text(19550, -yexag(19500) - 520, "spline 4", color=ORANGE, fontsize=11, weight="bold", ha="center")

# líneas transversales (se conservan)
ax.plot([15000, 15000], [-yt(15000), yt(15000)], color=GREEN, lw=3)
ax.text(14950, -yt(15000) - 420, "borde x=15000\n(del rectángulo)\nCONSERVAR", color=GREEN, fontsize=9, ha="center", va="top")
for x in (18000, 21000):
    ax.plot([x, x], [-yt(x), yt(x)], color=BLUE, lw=3)
    ax.text(x, -yt(x) - 420, f"línea x={x}\nCONSERVAR", color=BLUE, fontsize=9.5, ha="center", va="top", weight="bold")

# casco a la altura de la cubierta (referencia)
ax.text(21250, 2300, "Las splines nuevas (naranja)\nsiguen el casco.\nLos bordes rojos rectos se\nseparan de él (hueco).",
        fontsize=10, color="0.25", va="top")

ax.set_title("Cubierta en el cono, vista desde arriba (z = −1500)\n"
             "Rojo = BORRAR  ·  Verde / azul / naranja = CONSERVAR", fontsize=13)
ax.set_aspect("equal"); ax.set_xlim(11800, 24300); ax.set_ylim(-6800, 6000); ax.axis("off")
fig.text(0.5, 0.02, f"Esquema ilustrativo, no captura de Femap. La curvatura de las splines está exagerada ×{EXAG:.0f} "
         "para que se vea la diferencia: en la realidad el hueco es de 7–23 mm.", ha="center", fontsize=9.5, color="0.35")
fig.savefig("esquemas/cubierta_cono_borrar.png", dpi=130, bbox_inches="tight")
