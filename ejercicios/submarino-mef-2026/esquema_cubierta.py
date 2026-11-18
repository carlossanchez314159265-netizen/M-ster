"""Esquema de la posición de la cubierta (z = -1500) con cotas, en mm."""
import math
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

R, r2, zd = 5000, 2500, -1500
def r_hull(x):
    return R if x <= 15000 else R - (R - r2)*(x - 15000)/6000
def half_w(x):
    return math.sqrt(r_hull(x)**2 - zd**2)

fig = plt.figure(figsize=(15, 11))
gs = fig.add_gridspec(2, 2, height_ratios=[1, 1.15], width_ratios=[2.3, 1])
ax1 = fig.add_subplot(gs[0, :]); ax2 = fig.add_subplot(gs[1, 0]); ax3 = fig.add_subplot(gs[1, 1])
deck = "#2f9e44"; hull = "0.25"

# --- 1. Perfil XZ
th = np.linspace(np.pi/2, 3*np.pi/2, 100)
ax1.plot(R*np.cos(th), R*np.sin(th), color=hull, lw=1.8)
ax1.plot([0, 15000, 21000], [R, R, r2], color=hull, lw=1.8); ax1.plot([0, 15000, 21000], [-R, -R, -r2], color=hull, lw=1.8)
th = np.linspace(-np.pi/2, np.pi/2, 100)
ax1.plot(21000 + r2*np.cos(th), r2*np.sin(th), color=hull, lw=1.8)
for x, r in ((3000, R), (15000, R), (21000, r2)):
    ax1.plot([x, x], [-r, r], color="#e03131", lw=1.2, alpha=0.6)
ax1.plot([0, 21000], [zd, zd], color=deck, lw=4)
ax1.axhline(0, color="0.6", ls="-.", lw=0.8)
ax1.annotate("CUBIERTA  z = −1500\nde x = 0 a x = 21000", (10500, zd), (10500, -3900), ha="center",
             color=deck, fontsize=12, weight="bold", arrowprops=dict(arrowstyle="->", color=deck))
ax1.annotate("", (-5800, 0), (-5800, zd), arrowprops=dict(arrowstyle="<->"))
ax1.text(-6000, zd/2, "1500", ha="right", va="center", fontsize=10)
ax1.text(-6000, 300, "eje (z = 0)", ha="right", fontsize=9, color="0.4")
for x, l in ((3000, "M2"), (15000, "M1"), (21000, "M3")):
    ax1.text(x, R + 300 if x < 21000 else r2 + 300, l, ha="center", color="#e03131", fontsize=10)
ax1.set_title("1 · Perfil (vista lateral, plano XZ): la cubierta está 1500 mm POR DEBAJO del eje", fontsize=12)
ax1.set_aspect("equal"); ax1.set_xlim(-8500, 24500); ax1.set_ylim(-6000, 6000); ax1.axis("off")

# --- 2. Planta de la cubierta (vista desde arriba, plano XY)
xs = np.linspace(0, 21000, 400)
yw = np.array([half_w(x) for x in xs])
ax2.fill_between(xs, -yw, yw, color=deck, alpha=0.25)
ax2.plot(xs, yw, color=deck, lw=2.5); ax2.plot(xs, -yw, color=deck, lw=2.5)
ax2.plot([0, 0], [-half_w(0), half_w(0)], color=deck, lw=2.5); ax2.plot([21000, 21000], [-2000, 2000], color=deck, lw=2.5)
ax2.plot(xs, [r_hull(x) for x in xs], color=hull, lw=1, ls="--"); ax2.plot(xs, [-r_hull(x) for x in xs], color=hull, lw=1, ls="--")
for x in (3000, 6000, 9000, 12000, 15000, 18000):
    ax2.plot([x, x], [-half_w(x), half_w(x)], color=deck, lw=1, ls=":")
    ax2.text(x, -half_w(x) - 650, f"x={x}", ha="center", fontsize=8, color="0.3")
ax2.text(0, -half_w(0) - 650, "x=0", ha="center", fontsize=8, color="0.3"); ax2.text(21000, -2000 - 650, "x=21000", ha="center", fontsize=8, color="0.3")
for x, y in ((0, half_w(0)), (15000, half_w(15000)), (18000, half_w(18000)), (21000, 2000)):
    ax2.plot(x, y, "o", color="k", ms=5); ax2.plot(x, -y, "o", color="k", ms=5)
    ax2.text(x + 150, y + 250, f"({x}, ±{y:.1f}, −1500)", fontsize=8.5)
ax2.text(7500, 0, "rectángulo exacto\n(Surface → Corners)", ha="center", va="center", fontsize=11, color=deck, weight="bold")
ax2.text(18000, 0, "borde curvo\n(se estrecha\ncon el cono)", ha="center", va="center", fontsize=9.5, color=deck, weight="bold")
ax2.text(500, 5300, "- - - casco a la altura del eje (radio máximo)", fontsize=8.5, color="0.35")
ax2.set_title("2 · Planta de la cubierta (vista desde arriba) con las coordenadas de sus esquinas", fontsize=12)
ax2.set_aspect("equal"); ax2.set_xlim(-800, 24800); ax2.set_ylim(-6200, 6200); ax2.axis("off")

# --- 3. Sección transversal YZ
t = np.linspace(0, 2*np.pi, 300)
for x, ls, lab in ((0, "-", "cilindro (x = 0…15000)"), (18000, "--", "x = 18000"), (21000, ":", "x = 21000")):
    rr = r_hull(x); hw = half_w(x)
    ax3.plot(rr*np.cos(t), rr*np.sin(t), color=hull, lw=1.5, ls=ls, label=f"casco en {lab}")
    ax3.plot([-hw, hw], [zd, zd], color=deck, lw=4 if x == 0 else 2.5, ls=ls)
ax3.annotate("", (-half_w(0), zd - 900), (half_w(0), zd - 900), arrowprops=dict(arrowstyle="<->", color=deck))
ax3.text(0, zd - 1350, "9539 en el cilindro", ha="center", color=deck, fontsize=10, va="top")
ax3.text(0, zd + 200, "6874 en x=18000 · 4000 en x=21000", ha="center", color=deck, fontsize=8.5)
ax3.plot(0, 0, "+", color="k"); ax3.text(150, 150, "eje", fontsize=8)
ax3.legend(loc="upper center", fontsize=8, frameon=False, bbox_to_anchor=(0.5, 1.02))
ax3.set_title("3 · Sección vista desde proa (plano YZ)", fontsize=12, pad=28)
ax3.set_aspect("equal"); ax3.set_xlim(-5800, 5800); ax3.set_ylim(-6200, 5600); ax3.axis("off")

fig.text(0.5, 0.01, "Esquema ilustrativo (no captura de Femap). Ejes: X a lo largo del submarino hacia popa, Y a babor, Z hacia arriba; "
         "origen en la unión semiesfera de proa – cilindro.", ha="center", fontsize=9.5, color="0.35")
fig.tight_layout(rect=(0, 0.025, 1, 1))
fig.savefig("esquemas/posicion_cubierta.png", dpi=130)
