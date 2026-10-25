import numpy as np, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import animation

Hi, Hr, L = 0.20, 0.10, 16.68
ai, ar = Hi/2, Hr/2
k = 2*np.pi/L
x = np.linspace(-1.5, L*1.25, 800)
ts = np.linspace(0, 2*np.pi, 16, endpoint=False)
env = np.sqrt(ai**2 + ar**2 + 2*ai*ar*np.cos(2*k*x))
AZ, NA, RO, VE, GR = "#1f5fa8", "#e07b00", "#c0392b", "#1e8449", "#9aa5b1"

def flecha_v(ax, xx, y0, y1, txt, color, lado=1):
    ax.annotate("", xy=(xx, y1), xytext=(xx, y0),
                arrowprops=dict(arrowstyle="<->", color=color, lw=2))
    ax.text(xx + 0.35*lado, (y0+y1)/2, txt, color=color, fontsize=11, fontweight="bold",
            va="center", ha="left" if lado > 0 else "right")

def flecha_h(ax, x0, x1, y, txt, color):
    ax.annotate("", xy=(x1, y), xytext=(x0, y),
                arrowprops=dict(arrowstyle="<->", color=color, lw=2))
    ax.text((x0+x1)/2, y+0.012, txt, color=color, fontsize=11, fontweight="bold", ha="center", va="bottom")
    for xx in (x0, x1):
        ax.axvline(xx, color=color, ls=":", lw=1)

fig, axs = plt.subplots(2, 1, figsize=(12, 10))

# ---- Panel 1: una ola sola
ax = axs[0]
for t in ts:
    ax.plot(x, ai*np.cos(k*x - t), color=GR, lw=0.8, alpha=0.6)
ax.plot(x, ai*np.cos(k*x), color=AZ, lw=2.5, label="la ola en un instante")
ax.fill_between(x, -ai, ai, color=AZ, alpha=0.08)
ax.plot(x, ai+0*x, color="k", lw=2); ax.plot(x, -ai+0*x, "k", lw=2, label="envolvente (contorno de todos los instantes)")
flecha_v(ax, 2.1, -ai, ai, "H = 0,2 m\n(siempre igual)", AZ)
flecha_h(ax, 0, L, 0.135, "L = 16,7 m  (de cresta a cresta)", RO)
ax.set_title("1)  UNA OLA SOLA que avanza: si dibujo muchos instantes (gris), el contorno es una franja RECTA\n"
             "→ no hay partes anchas ni estrechas", fontsize=12, loc="left")
ax.legend(loc="lower right", fontsize=9)

# ---- Panel 2: incidente + reflejada
ax = axs[1]
for t in ts:
    ax.plot(x, ai*np.cos(k*x - t) + ar*np.cos(k*x + t), color=GR, lw=0.8, alpha=0.7)
ax.fill_between(x, -env, env, color=VE, alpha=0.08)
ax.plot(x, env, "k", lw=2.5); ax.plot(x, -env, "k", lw=2.5, label="envolvente (la «manguera» del dibujo del enunciado)")
amax, amin = ai+ar, ai-ar
flecha_v(ax, 0, -amax, amax, "ANCHO (antinodo)\nHi + Hr = 0,3 m", VE)
flecha_v(ax, L/4, -amin, amin, "ESTRECHO (cuasi-nodo)\nHi − Hr = 0,1 m", RO)
flecha_v(ax, L/2, -amax, amax, "ancho otra vez", VE)
flecha_h(ax, 0, L/4, 0.20, "L/4 = 4,17 m", RO)
flecha_h(ax, L/4, L/2, 0.20, "L/4", RO)
flecha_h(ax, 0, L/2, 0.245, "L/2 = 8,34 m  (de ancho a ancho)", NA)
flecha_h(ax, 0, L, 0.29, "L = 16,7 m  (una longitud de onda completa)", AZ)
ax.set_ylim(-0.2, 0.34)
ax.set_title("2)  INCIDENTE (0,2 m →) + REFLEJADA (0,1 m ←): las dos se suman y unas veces se ayudan y otras se restan\n"
             "→ el contorno se ensancha y se estrecha, y se repite cada L/2. De ancho a estrecho hay L/4", fontsize=12, loc="left")
ax.legend(loc="lower right", fontsize=9)

for ax in axs:
    ax.axhline(0, color="k", lw=0.6)
    ax.set_xlim(-1.5, L*1.25); ax.set_xlabel("x [m]"); ax.set_ylabel("η [m]")
    ax.spines[["top", "right"]].set_visible(False)
axs[0].set_ylim(-0.2, 0.2)
fig.tight_layout()
fig.savefig("croquis/Ejercicio 4 - croquis envolvente.png", dpi=130)

# ---- Animacion
fig, axs = plt.subplots(2, 1, figsize=(11, 7), sharex=True)
fr = 60
def draw(i):
    t = 2*np.pi*i/fr * 2
    for ax in axs: ax.cla()
    a = axs[0]
    a.plot(x, ai*np.cos(k*x - t), color=AZ, lw=2, label="incidente  H = 0,2 m  →")
    a.plot(x, ar*np.cos(k*x + t), color=NA, lw=2, label="reflejada  H = 0,1 m  ←")
    a.set_title("Las dos olas por separado (una va, otra vuelve)", loc="left")
    a.legend(loc="upper right", fontsize=9); a.set_ylim(-0.17, 0.2)
    b = axs[1]
    tt = np.linspace(0, t, int(i)+1)
    for s in tt[::2]:
        b.plot(x, ai*np.cos(k*x - s) + ar*np.cos(k*x + s), color=GR, lw=0.6, alpha=0.5)
    b.plot(x, ai*np.cos(k*x - t) + ar*np.cos(k*x + t), color=VE, lw=2.5, label="suma = lo que se ve en el agua")
    b.plot(x, env, "k--", lw=1.2); b.plot(x, -env, "k--", lw=1.2, label="envolvente")
    for xx, c, tx in [(0, VE, "ancho"), (L/4, RO, "estrecho"), (L/2, VE, "ancho"), (3*L/4, RO, "estrecho"), (L, VE, "ancho")]:
        b.axvline(xx, color=c, ls=":", lw=1); b.text(xx, 0.17, tx, color=c, ha="center", fontsize=9, fontweight="bold")
    b.set_title("La suma: el rastro gris va dibujando la envolvente", loc="left")
    b.legend(loc="lower right", fontsize=9); b.set_ylim(-0.2, 0.2); b.set_xlabel("x [m]")
    for ax in axs:
        ax.axhline(0, color="k", lw=0.5); ax.set_xlim(-1.5, L*1.25); ax.set_ylabel("η [m]")
        ax.spines[["top", "right"]].set_visible(False)
anim = animation.FuncAnimation(fig, draw, frames=fr, interval=120)
fig.tight_layout()
anim.save("croquis/Ejercicio 4 - animacion envolvente.gif", writer="pillow", fps=9)
