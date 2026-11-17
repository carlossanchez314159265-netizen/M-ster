"""Dibuja el perfil acotado del submarino según la interpretación del README (mm)."""
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, Circle

R, Lc, Lk, r2, zd = 5000, 15000, 6000, 2500, -1500
fig, (ax, bx) = plt.subplots(1, 2, figsize=(16, 6.2), gridspec_kw={"width_ratios": [3.2, 1]})

# casco (perfil, plano XZ)
th = [math.radians(a) for a in range(90, 271)]
ax.plot([R*math.cos(a) for a in th], [R*math.sin(a) for a in th], "k", lw=2)
ax.plot([0, Lc], [R, R], "k", lw=2); ax.plot([0, Lc], [-R, -R], "k", lw=2)
ax.plot([Lc, Lc+Lk], [R, r2], "k", lw=2); ax.plot([Lc, Lc+Lk], [-R, -r2], "k", lw=2)
th2 = [math.radians(a) for a in range(-90, 91)]
ax.plot([Lc+Lk + r2*math.cos(a) for a in th2], [r2*math.sin(a) for a in th2], "k", lw=2)
ax.axhline(0, color="0.6", lw=0.8, ls="-.")

# cuadernas
for x in (0, 3000, 6000, 9000, 12000):
    if x != 6000:  # C3 queda interrumpida por la escotilla en la parte alta
        ax.plot([x, x], [R-150, R], color="tab:blue", lw=3)
    ax.plot([x, x], [-R, -R+150], color="tab:blue", lw=3)
    ax.text(x, -R-650, f"C{x//3000+1}\nx={x}", ha="center", fontsize=8, color="tab:blue")
xk = 18000; rk = R - (R-r2)*(xk-Lc)/Lk
ax.plot([xk, xk], [rk-150, rk], color="tab:blue", lw=3); ax.plot([xk, xk], [-rk, -rk+150], color="tab:blue", lw=3)
ax.text(xk, -rk-650, f"C6\nx={xk}", ha="center", fontsize=8, color="tab:blue")

# mamparos
for x, r, lab, hole in ((3000, R, "M2 (25 mm)\nhueco Ø2000", (2000, 2000)),
                        (15000, R, "M1 (25 mm)\nelipse 2000×1000", (1000, 2000)),
                        (21000, r2, "M3 (25 mm)\nhueco Ø800", (800, 800))):
    hz = hole[1]/2
    ax.plot([x, x], [hz, r], color="tab:red", lw=2.2); ax.plot([x, x], [-r, -hz], color="tab:red", lw=2.2)
    ax.text(x+250, r*0.55, lab, color="tab:red", fontsize=8)

# cubierta
def half_width_r(x):
    if x <= Lc: return R
    return R - (R-r2)*(x-Lc)/Lk
ax.plot([0, 21000], [zd, zd], color="tab:green", lw=2)
ax.text(500, zd+200, "cubierta 20 mm, z = −1500 (hipótesis)", color="tab:green", fontsize=8)

# escotilla y brazola
ax.plot([5000, 5000], [R-100, R+250], color="tab:purple", lw=2.5)
ax.plot([7000, 7000], [R-100, R+250], color="tab:purple", lw=2.5)
ax.plot([5000, 7000], [R, R], color="white", lw=3)
ax.annotate("escotilla Ø2000 + brazola 250\ncentrada en C3 (x=6000)", (6000, R+250), (6500, R+1300),
            fontsize=8, color="tab:purple", arrowprops=dict(arrowstyle="->", color="tab:purple"))

# cotas
def dim(x1, x2, y, txt):
    ax.annotate("", (x1, y), (x2, y), arrowprops=dict(arrowstyle="<->", lw=0.8))
    ax.text((x1+x2)/2, y+150, txt, ha="center", fontsize=8)
dim(-R, 0, -R-1800, "5000"); dim(0, Lc, -R-1800, "15000 (cilindro)")
dim(Lc, Lc+Lk, -R-1800, "6000 (cono)"); dim(Lc+Lk, Lc+Lk+r2, -R-1800, "2500")
ax.text(Lc+Lk+r2/2, 1000, "R 2500", fontsize=8); ax.text(-R/2, 1000, "R 5000", fontsize=8)
ax.set_title("Perfil (plano XZ, y = 0). Origen en la unión semiesfera–cilindro, X hacia popa, Z hacia arriba", fontsize=10)
ax.set_aspect("equal"); ax.set_xlim(-5800, 24300); ax.set_ylim(-7600, 6700); ax.axis("off")

# sección por x = 15000 (mamparo M1)
c = [math.radians(a) for a in range(0, 361)]
bx.plot([R*math.cos(a) for a in c], [R*math.sin(a) for a in c], "k", lw=2)
bx.add_patch(Circle((0, 0), R, color="tab:red", alpha=0.12))
bx.add_patch(Ellipse((0, 0), 1000, 2000, fill=True, color="white", ec="tab:red", lw=1.5))
yd = math.sqrt(R**2 - zd**2)
bx.plot([-yd, yd], [zd, zd], color="tab:green", lw=2)
bx.text(0, zd-700, f"cubierta: ancho {2*yd:.0f}", ha="center", color="tab:green", fontsize=8)
bx.text(0, 2400, "elipse 1000 (Y) × 2000 (Z)\n(semiejes 500 × 1000)", ha="center", color="tab:red", fontsize=8)
bx.set_title("Sección x = 15000 (M1) vista desde proa", fontsize=10)
bx.set_aspect("equal"); bx.axis("off")

fig.tight_layout()
fig.savefig("geometria_submarino.png", dpi=160)
