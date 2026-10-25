"""Figuras del compendio de ejercicios resueltos (matplotlib → PNG → ReportLab)."""
import os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon, Ellipse, Rectangle, Circle
from reportlab.platypus import Image
from reportlab.lib.units import mm

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_png")
os.makedirs(OUT, exist_ok=True)
NAVY, TEAL, RED, SAND, AMBER = "#0B3954", "#0E7C86", "#B23A2E", "#CBBFAE", "#E0A030"
WATER = "#E6F0F5"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 9})
g = 9.81


def _img(fig, name, width_mm):
    p = os.path.join(OUT, name)
    fig.savefig(p, dpi=220, bbox_inches="tight")
    plt.close(fig)
    im = Image(p)
    ratio = im.imageHeight / im.imageWidth
    return Image(p, width=width_mm * mm, height=width_mm * mm * ratio)


def _clean(ax):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)


# ------------------------------------------------------------------ Teoría de ondas
def ej1_esquema(width=150):
    fig, ax = plt.subplots(figsize=(7.4, 2.4))
    x = np.linspace(0, 10, 600)
    bed = np.where(x < 5.2, -3.0, -1.0) + np.where((x >= 4.6) & (x < 5.2), (x - 4.6) / 0.6 * 2.0, 0)
    bed = np.clip(bed, -3, -1)
    eta = 0.18 * np.where(x < 5, np.cos(2 * np.pi * x / 2.4), np.cos(2 * np.pi * x / 1.55))
    ax.fill_between(x, bed, eta, color=WATER)
    ax.plot(x, eta, color=NAVY, lw=1.4)
    ax.fill_between(x, -3.3, bed, color=SAND)
    ax.plot(x, bed, color="k", lw=1.2)
    ax.annotate("", (0.4, 0.45), (2.8, 0.45), arrowprops=dict(arrowstyle="<->", color=TEAL))
    ax.text(1.6, 0.55, "L₀ = 312 m (indefinidas)", ha="center", color=TEAL)
    ax.annotate("", (6.0, 0.45), (7.55, 0.45), arrowprops=dict(arrowstyle="<->", color=RED))
    ax.text(6.8, 0.55, "L = 200 m (plataforma)", ha="center", color=RED)
    ax.annotate("", (8.6, 0.0), (8.6, -1.0), arrowprops=dict(arrowstyle="<->"))
    ax.text(8.75, -0.55, "h = ?", fontsize=10, fontweight="bold")
    ax.text(0.3, -2.7, "T se conserva al propagarse", fontsize=8.5, style="italic")
    ax.set_xlim(0, 10); ax.set_ylim(-3.3, 0.9); ax.axis("off")
    return _img(fig, "ej1.png", width)


def ej2_elipse(width=120):
    k, h = 1.0986, 1.0
    a = 0.1155
    fig, ax = plt.subplots(figsize=(6, 3.2))
    ax.fill_between([-1.6, 1.6], -1, 0, color=WATER)
    ax.plot([-1.6, 1.6], [0, 0], color=NAVY, lw=1.2)
    ax.fill_between([-1.6, 1.6], -1.15, -1, color=SAND)
    ax.plot([-1.6, 1.6], [-1, -1], color="k", lw=1.4)
    for z in (-0.1, -0.5, -0.9):
        A = a * np.cosh(k * (h + z)) / np.sinh(k * h)
        B = a * np.sinh(k * (h + z)) / np.sinh(k * h)
        col = RED if z == -0.5 else TEAL
        ax.add_patch(Ellipse((0, z), 2 * A * 3, 2 * B * 3, fill=False, color=col, lw=1.6 if z == -0.5 else 1))
    ax.annotate("", (0.3, -0.5), (0, -0.5), arrowprops=dict(arrowstyle="<->", color=RED))
    ax.text(0.15, -0.46, "A = 0,10 m", color=RED, ha="center", fontsize=8.5, va="bottom")
    ax.annotate("", (0, -0.35), (0, -0.5), arrowprops=dict(arrowstyle="<->", color=RED))
    ax.text(-0.04, -0.42, "B = 0,05 m", color=RED, ha="right", fontsize=8.5)
    ax.text(1.0, -0.5, "z = −0,5 m\n(mitad de la columna)", fontsize=8, va="center")
    ax.annotate("", (-1.4, 0), (-1.4, -1), arrowprops=dict(arrowstyle="<->"))
    ax.text(-1.35, -0.5, "h = 1 m", fontsize=8.5)
    ax.text(1.0, -0.94, "elipses ×3 para verlas", fontsize=7, style="italic", color="grey")
    ax.set_xlim(-1.6, 1.6); ax.set_ylim(-1.15, 0.15); ax.set_aspect("equal"); ax.axis("off")
    return _img(fig, "ej2.png", width)


def ej3_tsunami(width=160):
    x = np.linspace(0, 40000, 400)
    h = 200 - 0.005 * x
    c = np.sqrt(g * np.clip(h, 1e-9, None))
    t = 2 / (0.005 * g) * (np.sqrt(g * 200) - np.sqrt(g * np.clip(h, 0, None)))
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(8.4, 2.7))
    a1.fill_between(x / 1000, -h, 0, color=WATER)
    a1.fill_between(x / 1000, -h, -220, color=SAND)
    a1.plot(x / 1000, -h, color="k", lw=1.2)
    a1.text(3, -70, "h(x) = 200 − 0,005x", fontsize=8.5)
    a1.text(30, -20, "costa\n(h = 0)", fontsize=8, ha="center")
    a1.plot(0, -200, "o", color=RED); a1.text(1.5, -195, "detección 12:00", color=RED, fontsize=8, va="bottom")
    a1.set_xlabel("x [km]"); a1.set_ylabel("cota [m]"); a1.set_ylim(-220, 15); _clean(a1)
    a1.set_title("Talud de la plataforma", fontsize=9)
    ax2 = a2.twinx()
    a2.plot(x / 1000, t / 60, color=NAVY, lw=1.8, label="t(x) acumulado")
    ax2.plot(x / 1000, c, color=TEAL, lw=1.2, ls="--", label="c = √(gh)")
    a2.set_xlabel("x [km]"); a2.set_ylabel("t [min]", color=NAVY); ax2.set_ylabel("c [m/s]", color=TEAL)
    a2.axhline(30.1, color=RED, lw=0.7, ls=":"); a2.text(1, 31, "30,1 min", color=RED, fontsize=8)
    a2.set_title("Se frena al acercarse: el último tramo es el más lento", fontsize=8.5)
    a2.spines["top"].set_visible(False); ax2.spines["top"].set_visible(False)
    fig.tight_layout()
    return _img(fig, "ej3.png", width)


def ej4_envolventes(width=165):
    fig, ax = plt.subplots(figsize=(8.6, 3.2))
    # barlomar
    L1, Hi1, Hr1 = 16.68, 0.2, 0.1
    x1 = np.linspace(-26, -1, 500)
    env1 = 0.5 * np.sqrt(Hi1 ** 2 + Hr1 ** 2 + 2 * Hi1 * Hr1 * np.cos(2 * 2 * np.pi / L1 * (x1 + 1)))
    s = 6
    ax.fill_between(x1, -env1 * s, env1 * s, color=WATER)
    ax.plot(x1, env1 * s, color=NAVY); ax.plot(x1, -env1 * s, color=NAVY)
    # sotamar
    L2, Hi2, Hr2 = 14.6, 0.19, 0.068
    x2 = np.linspace(1, 24, 500)
    env2 = 0.5 * np.sqrt(Hi2 ** 2 + Hr2 ** 2 + 2 * Hi2 * Hr2 * np.cos(2 * 2 * np.pi / L2 * (x2 - 24)))
    ax.fill_between(x2, -env2 * s, env2 * s, color=WATER)
    ax.plot(x2, env2 * s, color=TEAL); ax.plot(x2, -env2 * s, color=TEAL)
    ax.add_patch(Rectangle((-0.6, -2.6), 1.2, 3.6, color="#888888"))
    ax.text(0, 1.15, "barrera", ha="center", fontsize=8.5)
    # bed
    ax.plot([-26, 0], [-2.886, -2.886], color="k"); ax.plot([0, 0], [-2.886, -2.0], color="k"); ax.plot([0, 24], [-2, -2], color="k")
    ax.fill_between([-26, 0], -3.2, -2.886, color=SAND); ax.fill_between([0, 24], -3.2, -2.0, color=SAND)
    ax.annotate("", (2, 0), (2, -2), arrowprops=dict(arrowstyle="<->")); ax.text(2.3, -1.75, "h₂ = 2,0 m", fontsize=8.5)
    ax.annotate("", (-2, 0), (-2, -2.886), arrowprops=dict(arrowstyle="<->")); ax.text(-9.5, -2.2, "h₁ = 2 + d = 2,89 m", fontsize=8.5)
    ax.text(-24, 1.05, "BARLOMAR: H₁ envolvente 0,3 / 0,1 m\nL₁/4 = 4,17 m → L₁ = 16,7 m", fontsize=8, color=NAVY)
    ax.text(5, 1.05, "SOTAMAR: H₂ envolvente 0,258 / 0,122 m\nL₂/4 = 3,65 m → L₂ = 14,6 m", fontsize=8, color=TEAL)
    ax.text(-13, -1.25, "Hᵢ₁ = 0,20 m  →     ←  Hᵣ₁ = 0,10 m", fontsize=8.5, color=RED, ha="center", fontweight="bold")
    ax.text(13, -1.25, "Hₜ = Hᵢ₂ = 0,19 m  →     ←  Hᵣ₂ = 0,068 m", fontsize=8.5, color=RED, ha="center", fontweight="bold")
    ax.set_xlim(-26, 24); ax.set_ylim(-3.2, 1.8); ax.axis("off")
    ax.text(-26, -3.15, "Envolventes dibujadas ×6 en vertical", fontsize=7, style="italic", color="grey")
    return _img(fig, "ej4.png", width)


def ej5_grupo(width=165):
    w1, w2 = 2 * np.pi / 5.7, 2 * np.pi / 5.4
    k1, k2 = 0.123863, 0.138008
    x = np.linspace(0, 900, 4000)
    eta = 1 * np.cos(k1 * x) + 1 * np.cos(k2 * x)
    dk = k2 - k1
    env = 2 * np.abs(np.cos(0.5 * dk * x))
    fig, ax = plt.subplots(figsize=(8.6, 2.5))
    ax.plot(x, eta, color=NAVY, lw=0.8)
    ax.plot(x, env, color=RED, lw=1.2, ls="--"); ax.plot(x, -env, color=RED, lw=1.2, ls="--")
    Lg = 2 * np.pi / dk
    ax.annotate("", (0, 2.55), (Lg, 2.55), arrowprops=dict(arrowstyle="<->", color=TEAL))
    ax.text(Lg / 2, 2.7, "longitud de grupo 2π/Δk = 444 m", ha="center", color=TEAL, fontsize=8.5)
    ax.text(470, -2.9, "portadora: L = 48 m, c = 8,66 m/s   ·   envolvente (grupo) avanza a c_g = Δω/Δk = 4,33 m/s", fontsize=8, ha="center")
    ax.set_xlabel("x [m]  (t = 0)"); ax.set_ylabel("η [m]"); ax.set_ylim(-3.2, 3.1); _clean(ax)
    return _img(fig, "ej5.png", width)


def ej_dispersion_h10(width=150):
    T = np.array([2, 6, 12, 18, 24.0])
    from scipy.optimize import brentq
    ks = [brentq(lambda k: (2 * np.pi / t) ** 2 - g * k * np.tanh(10 * k), 1e-6, 10) for t in T]
    c = 2 * np.pi / T / np.array(ks)
    Tc = np.linspace(1, 26, 200)
    kc = [brentq(lambda k: (2 * np.pi / t) ** 2 - g * k * np.tanh(10 * k), 1e-6, 50) for t in Tc]
    fig, ax = plt.subplots(figsize=(7, 2.6))
    ax.plot(Tc, 2 * np.pi / Tc / np.array(kc), color=NAVY, lw=1.6, label="c (dispersión, h = 10 m)")
    ax.plot(Tc, g * Tc / (2 * np.pi), color=TEAL, ls="--", lw=1, label="c₀ = gT/2π (indefinidas)")
    ax.axhline(np.sqrt(g * 10), color=RED, ls=":", lw=1, label="√(gh) = 9,90 m/s (someras)")
    ax.plot(T, c, "o", color=NAVY)
    ax.set_ylim(0, 14); ax.set_xlabel("T [s]"); ax.set_ylabel("c [m/s]"); ax.legend(fontsize=7.5, frameon=False); _clean(ax)
    return _img(fig, "disp_h10.png", width)


# ------------------------------------------------------------------ Estadística
def pasocero_barras(width=150):
    H = np.array([0.09, 0.15, 0.19, 0.42, 1.03, 0.61, 0.44, 0.68, 0.50, 1.09, 1.20, 1.09, 0.56, 0.06, 0.05, 0.97, 0.71, 0.28, 0.99, 0.88, 0.13, 0.62])
    top = np.argsort(-H, kind="stable")[:7]
    cols = [RED if i in top else TEAL for i in range(len(H))]
    fig, ax = plt.subplots(figsize=(7.4, 2.3))
    ax.bar(np.arange(1, 23), H, color=cols)
    ax.axhline(H.mean(), color=NAVY, ls="--", lw=0.9); ax.text(22.6, H.mean(), "H_m = 0,58", fontsize=7.5, va="center")
    ax.axhline(np.sqrt((H ** 2).mean()), color=AMBER, ls=":", lw=1); ax.text(22.6, 0.70, "H_rms = 0,69", fontsize=7.5, va="bottom")
    ax.axhline(1.0357, color=RED, ls="-", lw=0.8); ax.text(22.6, 1.04, "H_1/3 = 1,04", fontsize=7.5, color=RED, va="bottom")
    ax.set_xlabel("ola i (orden del registro)"); ax.set_ylabel("H [m]"); ax.set_xticks(range(1, 23)); ax.tick_params(labelsize=7); _clean(ax)
    return _img(fig, "pasocero.png", width)


def rayleigh_exced(width=140):
    Hr = 3.0
    H = np.linspace(0, 10, 300)
    q = np.exp(-(H / Hr) ** 2)
    fig, ax = plt.subplots(figsize=(6.6, 2.4))
    ax.semilogy(H, q, color=NAVY, lw=1.6)
    ax.axhline(0.02, color=RED, ls=":", lw=1); ax.axvline(5.93, color=RED, ls=":", lw=1)
    ax.plot(5.93, 0.02, "o", color=RED); ax.text(6.1, 0.03, "H₂% = 5,93 m", color=RED, fontsize=8.5)
    ax.set_ylim(1e-4, 1.2); ax.set_xlabel("H* [m]"); ax.set_ylabel("P(H > H*)"); _clean(ax)
    ax.set_title("Excedencia de Rayleigh con H_rms = 3 m", fontsize=8.5)
    return _img(fig, "rayleigh.png", width)


# ------------------------------------------------------------------ Espectral
def esp_componentes(width=150):
    H = np.array([0.91, 1.83, 2.17, 4.18, 2.38]); T = np.array([3.76, 5.04, 6.63, 8.69, 13.03])
    E = H ** 2 / 8
    fig, ax = plt.subplots(figsize=(7, 2.3))
    ax.bar(2 * np.pi / T, E, width=0.06, color=TEAL)
    for w, e, h in zip(2 * np.pi / T, E, H):
        ax.text(w, e + 0.05, f"H={h}\nE/ρg={e:.2f}", ha="center", fontsize=7)
    ax.set_xlabel("ω = 2π/T [rad/s]"); ax.set_ylabel("aᵢ²/2 = Hᵢ²/8 [m²]"); ax.set_ylim(0, 2.8); _clean(ax)
    ax.set_title("Espectro «de líneas»: m₀ = Σ Hᵢ²/8 = 4,00 m²", fontsize=8.5)
    return _img(fig, "esp_comp.png", width)


def esp_polar(width=105):
    """Esquema del espectro direccional de la diapo 77 (radio ∝ frecuencia, periodo largo en el centro)."""
    fig = plt.figure(figsize=(4.3, 4.3))
    ax = fig.add_subplot(111, projection="polar")
    ax.set_theta_zero_location("N"); ax.set_theta_direction(-1)
    rings = {6: 1 / 6, 7: 1 / 7, 9: 1 / 9, 11: 1 / 11, 35: 1 / 35}
    th = np.linspace(0, 2 * np.pi, 300)
    for T, f in rings.items():
        ax.plot(th, np.full_like(th, f), color="grey", lw=0.8)
        ax.text(np.radians(8), f + 0.004, f"{T} s", fontsize=7, color="grey")
    # swell (W, ~14 s)
    def blob(dir_deg, T, dth, dr, col, lab, lab_dir, lab_r):
        tt = np.radians(dir_deg) + dth * np.cos(th)
        rr = 1 / T + dr * np.sin(th)
        ax.fill(tt, rr, color=col, alpha=0.75)
        ax.text(np.radians(lab_dir), lab_r, lab, ha="center", va="center", fontsize=8.5, color=col, fontweight="bold",
                bbox=dict(boxstyle="round,pad=0.2", fc="white", ec=col, lw=0.6))
    blob(257, 13.7, np.radians(8), 0.012, NAVY, "SWELL\n≈14 s · 257°", 300, 0.135)
    blob(150, 8.3, np.radians(25), 0.02, RED, "SEA\n≈8 s · 150°", 100, 0.13)
    ax.set_rlim(0, 0.19); ax.set_yticklabels([])
    ax.set_xticks(np.radians([0, 90, 180, 270])); ax.set_xticklabels(["N", "E", "S", "W"])
    return _img(fig, "esp_polar.png", width)


def esp_triangulo(width=130):
    w = np.linspace(0, 2.2, 400)
    S = np.where(w < 0.8, 2 * w, np.where(w < 2, 8 / 3 - 4 * w / 3, 0))
    fig, ax = plt.subplots(figsize=(6.2, 2.3))
    ax.fill_between(w, S, color=WATER); ax.plot(w, S, color=NAVY, lw=1.6)
    ax.plot([0.8, 0.8], [0, 1.6], color=RED, ls=":"); ax.text(0.83, 1.55, "ω_p = 0,8 rad/s → T_p = 7,85 s", color=RED, fontsize=8)
    ax.text(0.45, 0.3, "0,64", ha="center", fontsize=8); ax.text(1.2, 0.3, "0,96", ha="center", fontsize=8)
    ax.text(1.5, 1.2, "m₀ = área = 1,6 m²", fontsize=9)
    ax.set_xlabel("ω [rad/s]"); ax.set_ylabel("S(ω) [m²·s/rad]"); ax.set_ylim(0, 1.85); _clean(ax)
    return _img(fig, "esp_tri.png", width)


# ------------------------------------------------------------------ Introducción
def esfera_perfil(width=150):
    import seawater as sw
    p = np.array([0, 50, 100, 150, 200, 250, 300, 350, 400, 450])
    T = np.array([24.5, 23.5, 22.5, 21.8, 21.0, 20.0, 19.0, 18.2, 17.4, 16.0])
    S = np.array([37.8, 37.7, 37.6, 37.5, 37.4, 37.3, 37.2, 36.9, 36.7, 36.5])
    rho = sw.dens(S, T, p)
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(7.6, 2.8), sharey=True)
    a1.plot(T, -p, "o-", color=RED, ms=3, label="T [°C]")
    a1b = a1.twiny(); a1b.plot(S, -p, "s-", color=TEAL, ms=3); a1b.set_xlabel("S [g/kg]", color=TEAL)
    a1.set_xlabel("θ [°C]", color=RED); a1.set_ylabel("−p [dbar] ≈ −profundidad [m]")
    a2.plot(rho - 1000, -p, "o-", color=NAVY, ms=3); a2.set_xlabel("σ = ρ − 1000 [kg/m³]")
    a2.text(26.0, -25, "ρ(0) = 1025,61", fontsize=7.5); a2.text(27.3, -440, "ρ(450) = 1028,88", fontsize=7.5)
    _clean(a2)
    fig.tight_layout()
    return _img(fig, "esfera.png", width)
