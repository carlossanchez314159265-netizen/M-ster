"""Respuestas a las preguntas clave que el profesor señaló para el 1er parcial (basado en las diapositivas).

Uso: python3 preguntas_clave.py "../../parcial 1/13 - Preguntas clave del profesor.pdf"
"""
import sys, os, tempfile
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse, FancyArrowPatch
from reportlab.platypus import Image

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from estilo import *

TMP = tempfile.mkdtemp()
AZ, NA, RO, VE, GR, NV = "#1f5fa8", "#e07b00", "#c0392b", "#1e8449", "#9aa5b1", "#0B3954"
plt.rcParams.update({"font.size": 9, "axes.spines.top": False, "axes.spines.right": False})


def img(fig, name, width_mm=170):
    p = os.path.join(TMP, name + ".png")
    fig.savefig(p, dpi=200, bbox_inches="tight"); plt.close(fig)
    from PIL import Image as PI
    w, h = PI.open(p).size
    return Image(p, width=width_mm * mm, height=width_mm * mm * h / w)


# ============================================================ FIGURAS
def fig_magnitudes():
    fig, ax = plt.subplots(figsize=(8, 3.2))
    x = np.linspace(0, 1.25, 400); a = 0.18
    ax.plot(x, a * np.cos(2 * np.pi * x), color=AZ, lw=2.2)
    ax.axhline(0, color="k", lw=0.8, ls="--"); ax.text(1.28, -0.025, "nivel en reposo (z = 0)", fontsize=8, va="top", ha="right")
    ax.fill_between(x, -0.62, -0.68, color="#c8b28a"); ax.text(1.0, -0.6, "fondo (z = −h)", fontsize=8)
    ax.annotate("", (0.03, -0.6), (0.03, 0), arrowprops=dict(arrowstyle="<->", color=GR)); ax.text(0.05, -0.32, "h", color="#555")
    ax.annotate("", (0, a), (1, a), arrowprops=dict(arrowstyle="<->", color=RO)); ax.text(0.5, a + 0.03, "L (de cresta a cresta)", color=RO, ha="center")
    ax.annotate("", (0.5, -a), (0.5, a), arrowprops=dict(arrowstyle="<->", color=VE, lw=1.5)); ax.text(0.53, -0.08, r"H = $A_c + A_s$", color=VE, bbox=dict(fc="white", ec="none", pad=1))
    ax.annotate("", (0.25, 0), (0.25, a), arrowprops=dict(arrowstyle="<->", color=NA)); ax.text(0.27, 0.09, r"$A_c$", color=NA)
    ax.annotate("", (0.75, 0), (0.75, -a), arrowprops=dict(arrowstyle="<->", color=NA)); ax.text(0.77, -0.1, r"$A_s$", color=NA)
    ax.text(0, a + 0.1, "cresta", ha="center", fontsize=8); ax.text(0.5, -a - 0.07, "seno", ha="center", fontsize=8)
    ax.annotate("", (1.2, 0.3), (1.0, 0.3), arrowprops=dict(arrowstyle="->", color=NV, lw=2)); ax.text(1.1, 0.33, "c = L/T", ha="center", color=NV)
    ax.plot([0.25, 0.75], [0, 0], "o", color="k", ms=3); ax.text(0.25, -0.06, "paso por cero", fontsize=7, ha="center")
    ax.set_ylim(-0.7, 0.45); ax.set_xlim(-0.05, 1.3); ax.axis("off")
    return img(fig, "magnitudes", 160)


def fig_ondas():
    fig, axs = plt.subplots(1, 2, figsize=(9, 2.6))
    x = np.linspace(0, 1, 300)
    for t, al in zip(np.linspace(0, 0.4, 5), np.linspace(1, 0.3, 5)):
        axs[0].plot(x, np.cos(2 * np.pi * (x - t)), color=AZ, alpha=al)
    axs[0].annotate("", (0.95, 1.25), (0.6, 1.25), arrowprops=dict(arrowstyle="->", color=AZ, lw=2))
    axs[0].set_title("Progresiva: η = a·cos(kx − ωt)\nla forma avanza", fontsize=9)
    for t in np.linspace(0, np.pi, 7):
        axs[1].plot(x, np.cos(2 * np.pi * x) * np.cos(t), color=VE, alpha=0.7)
    for xn in (0.25, 0.75):
        axs[1].plot(xn, 0, "o", color=RO); axs[1].text(xn, -1.35, "nodo", color=RO, ha="center", fontsize=8)
    for xa in (0, 0.5, 1):
        axs[1].text(xa, 1.12, "antinodo", color=VE, ha="center", fontsize=8)
    axs[1].set_title("Estacionaria: η = a·cos(kx)·cos(ωt)\nno avanza; nodo ↔ antinodo = L/4", fontsize=9)
    for ax in axs:
        ax.axhline(0, color="k", lw=0.5); ax.set_ylim(-1.5, 1.45); ax.set_xticks([]); ax.set_yticks([])
    return img(fig, "ondas", 165)


def fig_orbitas():
    casos = [("Indefinidas  h/L = 0,6", 0.6), ("Intermedias  h/L = 0,15", 0.15), ("Reducidas  h/L = 0,04", 0.04)]
    fig, axs = plt.subplots(1, 3, figsize=(10, 6.2))
    niveles = [-0.08, -0.27, -0.46, -0.65, -0.84, -0.995]
    nota = {casos[0][0]: "círculos que se apagan", casos[1][0]: "elipses que se aplastan", casos[2][0]: "elipses planas, mismo ancho"}
    for ax, (tit, hl) in zip(axs, casos):
        kh = 2 * np.pi * hl
        al = lambda zh: np.cosh(kh * (1 + zh)) / np.sinh(kh)
        be = lambda zh: np.sinh(kh * (1 + zh)) / np.sinh(kh)
        s = min(0.14 / be(0), 0.33 / al(0))
        xs = np.linspace(-0.62, 0.62, 200)
        ax.plot(xs, 0.05 * np.cos(np.pi * xs), color=AZ, lw=1.5)
        ax.fill_between([-0.62, 0.62], -1.05, -1.0, color="#c8b28a")
        for zh in niveles:
            A, B = al(zh) * s, be(zh) * s
            if B < 0.004:
                ax.plot([-A, A], [zh, zh], color=NV, lw=1.6)
            else:
                ax.add_patch(Ellipse((0, zh), 2 * A, 2 * B, fill=False, color=NV, lw=1.4))
                ax.annotate("", (0.02, zh + B), (-0.02, zh + B), arrowprops=dict(arrowstyle="->", color=RO, lw=1.2))
            ax.text(-0.6, zh, f"z/h = {zh:.2f}".replace(".", ","), fontsize=7, ha="left", va="center", color="#666")
        ax.set_xlim(-0.62, 0.62); ax.set_ylim(-1.07, 0.15); ax.set_aspect("equal"); ax.axis("off")
        ax.set_title(tit + "\n" + nota[tit], fontsize=9.5)
    fig.tight_layout()
    return img(fig, "orbitas", 170)


def fig_perfiles():
    fig, axs = plt.subplots(1, 2, figsize=(8.5, 3.6), sharey=True)
    zh = np.linspace(-1, 0, 200)
    for hl, c, lab in [(0.6, AZ, "indefinidas (h/L = 0,6)"), (0.15, VE, "intermedias (h/L = 0,15)"), (0.04, NA, "reducidas (h/L = 0,04)")]:
        kh = 2 * np.pi * hl
        axs[0].plot(np.cosh(kh * (1 + zh)) / np.cosh(kh), zh, color=c, lw=2, label=lab)
        axs[1].plot(np.sinh(kh * (1 + zh)) / np.sinh(kh), zh, color=c, lw=2)
    axs[0].set_title("Velocidad horizontal máx.  u(z)/u(0)\n∝ cosh k(h+z)", fontsize=9)
    axs[1].set_title("Velocidad vertical máx.  w(z)/w(0)\n∝ sinh k(h+z)", fontsize=9)
    axs[0].set_ylabel("z/h   (0 = superficie, −1 = fondo)")
    for ax in axs:
        ax.set_xlim(0, 1.05); ax.axhline(-1, color="#c8b28a", lw=4); ax.grid(alpha=0.3)
    axs[0].legend(fontsize=7.5, loc="lower right")
    axs[1].text(0.05, -0.97, "w = 0 en el fondo siempre", fontsize=7.5, color=RO)
    axs[0].text(0.05, -0.97, "u ≠ 0 en el fondo (desliza)", fontsize=7.5, color=RO)
    fig.tight_layout()
    return img(fig, "perfiles", 160)


def fig_campo():
    hl = 0.15; kh = 2 * np.pi * hl; k = 2 * np.pi; h = hl
    fig, ax = plt.subplots(figsize=(9, 3.2))
    x = np.linspace(0, 1, 300); a = 0.025
    ax.plot(x, a * np.cos(k * x), color=AZ, lw=2)
    ax.fill_between([0, 1], -h - 0.01, -h, color="#c8b28a")
    X, Z = np.meshgrid(np.linspace(0, 1, 17), np.linspace(-h * 0.97, -0.01, 5))
    U = np.cosh(k * (h + Z)) / np.sinh(kh) * np.cos(k * X)
    W = np.sinh(k * (h + Z)) / np.sinh(kh) * np.sin(k * X)
    ax.quiver(X, Z, U, W, color=NV, scale=22, width=0.003)
    for xx, t in [(0, "cresta: u máx. →"), (0.5, "seno: u máx. ←"), (0.25, "w máx. ↑"), (0.75, "w máx. ↓")]:
        ax.text(xx, 0.045, t, ha="center", fontsize=8, color=RO)
    ax.annotate("", (1.0, 0.075), (0.85, 0.075), arrowprops=dict(arrowstyle="->", color=AZ, lw=2)); ax.text(0.86, 0.085, "avance de la ola", fontsize=8, color=AZ)
    ax.set_xlim(-0.05, 1.05); ax.set_ylim(-h - 0.02, 0.1); ax.axis("off")
    return img(fig, "campo", 165)


def fig_rayleigh():
    Hr = 3.0
    H = np.linspace(0, 8, 400)
    f = 2 * H / Hr**2 * np.exp(-(H / Hr) ** 2)
    fig, ax = plt.subplots(figsize=(8, 3.2))
    ax.plot(H, f, color=NV, lw=2)
    H2 = Hr * np.sqrt(-np.log(0.02))
    m = H >= H2; ax.fill_between(H[m], f[m], color=RO, alpha=0.4)
    for v, lab, c in [(0.886 * Hr, "H̄ = 2,66", GR), (Hr, "Hrms = 3", AZ), (1.416 * Hr, "Hs = 4,25", VE), (H2, "H₂% = 5,93", RO)]:
        ax.axvline(v, color=c, ls="--", lw=1); ax.text(v + 0.05, 0.375, lab, color=c, fontsize=8, rotation=90, va="top")
    ax.annotate("área = 0,02\n(2 % de las olas)", (6.3, 0.012), (6.6, 0.12), arrowprops=dict(arrowstyle="->", color=RO), color=RO, fontsize=8)
    ax.set_xlabel("H [m]"); ax.set_ylabel("f(H) [1/m]"); ax.set_xlim(0, 8); ax.set_ylim(0, 0.38)
    ax.set_title("Rayleigh con Hrms = 3 m (ejemplo de la diapositiva)", fontsize=9)
    return img(fig, "rayleigh", 150)


def fig_sea_swell():
    rng = np.random.default_rng(3)
    f = np.linspace(0.02, 0.5, 600)

    def jonswap(fp, g):
        s = np.where(f <= fp, 0.07, 0.09)
        return f**-5 * np.exp(-1.25 * (f / fp) ** -4) * g ** np.exp(-(f - fp) ** 2 / (2 * s**2 * fp**2))
    Ssea = jonswap(1 / 5, 1.0); Ssw = jonswap(1 / 14, 7.0)
    Ssea /= np.trapezoid(Ssea, f) / (2.0 / 4) ** 2; Ssw /= np.trapezoid(Ssw, f) / (2.0 / 4) ** 2
    t = np.linspace(0, 180, 3000); df = f[1] - f[0]
    serie = lambda S: np.sum(np.sqrt(2 * S * df)[:, None] * np.cos(2 * np.pi * f[:, None] * t + rng.uniform(0, 2 * np.pi, len(f))[:, None]), axis=0)
    fig, axs = plt.subplots(2, 2, figsize=(9, 4.6))
    axs[0, 0].plot(t, serie(Ssea), color=NA, lw=0.8); axs[0, 0].set_title("SEA (mar de viento): desordenado, T corto", fontsize=9)
    axs[0, 1].plot(t, serie(Ssw), color=AZ, lw=0.8); axs[0, 1].set_title("SWELL (mar de fondo): regular, T largo", fontsize=9)
    axs[1, 0].fill_between(f, Ssea, color=NA, alpha=0.5); axs[1, 0].set_title("espectro ANCHO (Tp ≈ 5 s)", fontsize=9)
    axs[1, 1].fill_between(f, Ssw, color=AZ, alpha=0.5); axs[1, 1].set_title("espectro ESTRECHO (Tp ≈ 14 s)", fontsize=9)
    for ax in axs[0]:
        ax.set_xlabel("t [s]"); ax.set_ylabel("η [m]"); ax.set_ylim(-2.2, 2.2)
    for ax in axs[1]:
        ax.set_xlabel("f [Hz]"); ax.set_ylabel("S(f)"); ax.set_yticks([])
    fig.tight_layout()
    return img(fig, "seaswell", 165)


# ============================================================ DOCUMENTO
P("Oceanografía · Preguntas clave del profesor", H1)
P("Respuestas basadas en las diapositivas de R. Guanche (Bloque 2: Mecánica de ondas y Análisis del oleaje) · 1er parcial", SUB)
note("<b>Lista del profesor:</b> 1) Mecánica de ondas: celeridad, altura de ola, ondas características… · 2) Hipótesis de partida del resumen del "
     "problema general de ondas · 3) Campo de velocidades y aceleraciones: trayectoria de la partícula fluido · 4) Tsunamis: profundidad reducida · "
     "5) Rayleigh · 6) Altura superada por el 2 % de las mayores olas · 7) Sea frente a swell / mar de fondo frente a resaca.")

# ------------------------------------------------------------ 1
h2("1. Mecánica de ondas: magnitudes, celeridad y ondas características")
P("<b>Onda vs oleaje.</b> Una <i>onda</i> es un modelo matemático determinista: una oscilación uniforme y periódica de la superficie "
  "(oleaje regular, monocromático) → <b>teoría de ondas</b>. El <i>oleaje</i> real es aleatorio e irregular → se trata con "
  "<b>análisis estadístico y espectral</b>. El oleaje que importa en ingeniería es el generado por el viento (ondas gravitatorias, T ≈ 3–30 s): "
  "se llaman <b>gravitatorias</b> porque la fuerza que devuelve la superficie al equilibrio es la gravedad (en las capilares, L &lt; pocos cm, es la tensión superficial).")
h3("Magnitudes características")
figure(fig_magnitudes(), "Figura 1. Magnitudes de una onda progresiva. Eje x en la dirección de avance, z = 0 en el nivel en reposo y positivo hacia arriba.")
table(["Magnitud", "Definición (diapositivas)", "Fórmula"], [
    ["Altura H", "Distancia vertical entre cresta y seno", "H = A<sub>c</sub> + A<sub>s</sub>;  en teoría lineal A<sub>c</sub> = A<sub>s</sub> → <b>H = 2a</b>"],
    ["Amplitudes A<sub>c</sub>, A<sub>s</sub>", "Del nivel medio a la cresta y al seno", "a = H/2"],
    ["Periodo T", "Tiempo que tarda en repetirse un punto idéntico en una posición fija", "[s]"],
    ["Longitud L", "Distancia horizontal más corta entre dos puntos idénticos sucesivos", "[m]"],
    ["Número de onda k", "Cuántas veces se repite la onda por unidad de distancia", "k = 2π/L [rad/m]"],
    ["Frecuencia angular ω", "Rapidez con que avanza la fase en el tiempo", "ω = 2πf = 2π/T [rad/s]"],
    ["<b>Celeridad c</b>", "Velocidad de fase: a la que se propaga la forma de la onda", "<b>c = L/T = ω/k</b>"],
], [32, 78, 60])
P("Uno de los primeros objetivos de cualquier teoría de ondas es <b>determinar c conociendo H, L (o T) y h</b>; después, la cinemática "
  "(velocidades, aceleraciones, trayectorias) y las presiones.")
h3("Ondas características: progresiva y estacionaria")
figure(fig_ondas(), "Figura 2. En la progresiva el espacio y el tiempo van acoplados (kx − ωt); en la estacionaria van separados y la onda oscila entre nodos fijos.")
bl("<b>Progresiva:</b> η = a·cos(kx − ωt). Movimiento espacial y temporal <b>acoplado</b>: la forma se desplaza a velocidad c.",
   "<b>Estacionaria:</b> η = a·cos(kx)·cos(ωt). Evolución espacial y temporal <b>desacoplada</b>: no progresa, oscila entre <b>nodos</b> (η = 0 siempre) "
   "y <b>antinodos</b> (oscilación máxima). Nodo y antinodo contiguos están a <b>L/4</b>. Aparece con reflexión total (pared vertical).",
   "<b>Cuasi-estacionaria:</b> reflexión parcial (H<sub>r</sub> &lt; H<sub>i</sub>): la envolvente va de H<sub>i</sub> + H<sub>r</sub> a H<sub>i</sub> − H<sub>r</sub>, nunca se anula.")
h3("Parámetros adimensionales y clasificación por profundidad")
table(["Parámetro", "Expresión", "Qué mide"], [
    ["Peralte ε", "H/L  (o ka)", "No linealidad. H/L ≪ 1 → pequeña amplitud (lineal). Rotura en indefinidas: <b>H/L = 0,142 ≈ 1/7</b>"],
    ["Altura relativa δ", "H/h", "Importancia de la oscilación frente a la profundidad"],
    ["Profundidad relativa μ", "h/L  (o kh)", "Penetración del movimiento; si la celeridad depende del periodo (dispersividad)"],
    ["Ursell U<sub>r</sub>", "HL²/h³ = δ/μ²", "Régimen y teoría a usar (lineal si es pequeño; ≈ 26 límite)"],
], [34, 32, 104])
table(["Zona", "h/L", "kh", "¿Siente el fondo?", "Celeridad"], [
    ["Indefinidas", "&gt; 1/2", "&gt; π", "No: c y L independientes de h", "c₀ = gT/2π = <b>1,56·T</b>"],
    ["Intermedias", "1/20 – 1/2", "π/10 – π", "En parte", "c = c₀·tanh(kh)"],
    ["Reducidas", "&lt; 1/20", "&lt; π/10", "Totalmente: c y L solo dependen de h", "<b>c = √(gh)</b>"],
], [26, 22, 22, 56, 44])
h3("Celeridad: la ecuación de la dispersión")
fbox(["<b>ω² = g·k·tanh(kh)</b>        L = (gT²/2π)·tanh(2πh/L)        c = (gT/2π)·tanh(2πh/L)"])
bl("Es <b>trascendente</b>: con T y h se resuelve por iteración (Newton-Raphson, arranque k₀ = ω²/g) o con aproximaciones explícitas (Fenton-McKee &lt;1,5 %, Guo &lt;0,7 %).",
   "<b>Indefinidas</b> (tanh → 1): ω² = gk, L₀ = 1,56·T², c₀ = 1,56·T. Dependen solo de T: <b>las olas de mayor periodo viajan más rápido</b>.",
   "<b>Reducidas</b> (tanh kh → kh): c = √(gh). Todas las ondas viajan igual de rápido sea cual sea su periodo → <b>no dispersivas</b>.",
   "<b>Sentido físico</b> (diapositivas, h = 10 m): T = 2 s → c = 3,1 m/s; T = 12 s → 9,4 m/s; T = 24 s → 9,8 m/s. A igual profundidad, más periodo = "
   "más L y más c (<b>dispersión frecuencial</b>). Con T = 10 s fija, al bajar h de 50 a 2 m, c baja de 15,1 a 4,4 m/s (origen de la <b>refracción</b>).",
   "La energía no viaja a c sino a la <b>celeridad de grupo</b> c<sub>g</sub> = n·c, con n = ½[1 + 2kh/sinh 2kh] (½ en indefinidas, 1 en reducidas).")
h3("Regímenes y teorías")
bl("<b>Régimen de Stokes</b> (h/L o kh ≥ ~1; indefinidas e intermedias): si δ ≪ 1 o ε ≪ 1 → <b>teoría lineal o de Airy</b> (Stokes 1er orden); "
   "si ε crece → Stokes II, III…",
   "<b>Régimen de onda larga</b> (kh ≪ 1; reducidas): teorías cnoidal y de onda solitaria.",
   "El diagrama de Le Méhauté (h/gT² frente a H/gT²) indica qué teoría usar. Perfil lineal: simétrico, cresta y seno a H/2. "
   "Cnoidal: crestas altas y estrechas, senos largos y planos.")

# ------------------------------------------------------------ 2
h2("2. Hipótesis de partida del problema general de las ondas")
P("Diapositiva «Resumen del problema general de las ondas». Son las que convierten Navier-Stokes en el problema potencial (Laplace + condiciones de contorno):")
table(["", "Hipótesis", "Qué significa / por qué se puede"], [
    ["a)", "Fluido <b>continuo, homogéneo, incompresible y no viscoso</b>",
     "Densidad constante (∇·u = 0). Sin fricción interna entre capas: lejos de los contornos Re = UL/ν ~ 10⁸, la viscosidad no pinta nada"],
    ["b)", "Se desprecian los efectos de <b>Coriolis</b>", "T de las olas ≪ periodo de rotación terrestre; Coriolis es ~1000 veces menor que los términos inerciales"],
    ["c)", "Se desprecia la <b>tensión superficial</b>", "Solo importa en ondas capilares (L de centímetros)"],
    ["d)", "<b>Presión en la superficie uniforme y constante</b>", "p = p<sub>a</sub> = 0 en z = η → condición dinámica"],
    ["e)", "Flujo <b>irrotacional</b>", "∇×u = 0: sin remolinos, las partículas no giran sobre sí mismas → existe el potencial φ con u = ∇φ"],
    ["f)", "Fondo <b>variable e impermeable</b>", "No hay flujo a través del fondo → condición cinemática de fondo"],
], [8, 52, 110])
P("Además, la <b>única fuerza de volumen es la gravedad</b> (es la que controla el oleaje).")
h3("Qué se obtiene con ellas")
fbox(["Continuidad + irrotacional  →  <b>∇²φ = 0</b> (Laplace)          Euler + irrotacional  →  <b>Bernoulli</b>",
      "Fondo impermeable: ∂φ/∂z = 0 en z = −h          Cinemática en superficie: ∂φ/∂z = ∂η/∂t",
      "Dinámica en superficie: ∂φ/∂t + gη = 0          + periodicidad en x y en t"])
P("El problema sigue siendo <b>no lineal</b> (las condiciones se aplican en η, que es incógnita). La <b>teoría lineal</b> añade:")
bl("<b>Pequeña amplitud:</b> H/L ≪ 1, A/h ≪ 1 → se desprecian los productos de términos pequeños y las condiciones se aplican en z = 0.",
   "Problema <b>bidimensional</b> (crestas largas) y <b>fondo plano</b> e impermeable.")
P("Ventajas de la teoría lineal: es la más simple, el nivel medio coincide con el de reposo, da soluciones analíticas y permite "
  "<b>superponer</b> (base del oleaje irregular).")

# ------------------------------------------------------------ 3
h2("3. Campo de velocidades y aceleraciones: trayectoria de la partícula")
fbox(["<b>u</b> = a·ω · cosh k(h+z)/sinh kh · cos(kx − ωt)", "<b>w</b> = a·ω · sinh k(h+z)/sinh kh · sin(kx − ωt)",
      "a<sub>x</sub> ≈ ∂u/∂t = a·ω² · cosh k(h+z)/sinh kh · sin(kx − ωt)", "a<sub>z</sub> ≈ ∂w/∂t = −a·ω² · sinh k(h+z)/sinh kh · cos(kx − ωt)"])
terms([("a", "Amplitud = H/2 [m]"), ("h + z", "Altura del punto sobre el fondo [m]"),
       ("a<sub>x</sub>, a<sub>z</sub>", "Aceleraciones: se desprecian los términos convectivos (pequeña amplitud), salvo en aguas muy someras")])
figure(fig_campo(), "Figura 3. Campo de velocidades bajo la ola (intermedias) en un instante: hacia delante bajo la cresta, hacia atrás bajo el seno, "
       "subiendo delante de la cresta y bajando detrás. Las flechas se acortan con la profundidad.")
P("<b>Propiedades (las 8 de la diapositiva):</b>")
bl("Velocidades y aceleraciones son <b>proporcionales a la amplitud</b>.",
   "u máxima en crestas y senos (fase 0, π); w máxima en los pasos por cero (π/2, 3π/2): <b>u y w desfasadas π/2</b>.",
   "En el fondo w = 0 (condición de contorno), pero <b>u ≠ 0</b> (la teoría potencial deja deslizar).",
   "Ambas <b>disminuyen con la profundidad</b> por las funciones hiperbólicas de k(h+z).",
   "a<sub>z</sub> es máxima donde u es máxima, y a<sub>x</sub> donde w es máxima. En el fondo a<sub>z</sub> = 0 pero a<sub>x</sub> ≠ 0.")
figure(fig_perfiles(), "Figura 4. Perfil vertical de las velocidades máximas. En reducidas u es casi uniforme en toda la columna y w crece linealmente desde 0 en el fondo.")
h3("Trayectoria de la partícula")
P("Integrando las velocidades en el tiempo, cada partícula describe una <b>elipse cerrada</b> alrededor de su posición media (no se lleva el agua, solo la energía):")
fbox(["ζ = α·sin(kx − ωt)          ξ = −β·cos(kx − ωt)",
      "<b>α = a·cosh k(h+z)/sinh kh</b> (semieje horizontal)          <b>β = a·sinh k(h+z)/sinh kh</b> (semieje vertical)",
      "β/α = tanh k(h+z) ≤ 1          en superficie β = a: el desplazamiento vertical nunca supera la amplitud"])
figure(fig_orbitas(), "Figura 5. Órbitas a distintas profundidades en las tres zonas (mismo a). La flecha roja marca el sentido de giro: arriba la partícula avanza con la ola.")
table(["Zona", "Forma de la órbita", "Semiejes"], [
    ["Indefinidas", "<b>Círculos</b> cuyo radio decae exponencialmente; a z = −L/2 queda ~4 %: no llegan al fondo", "α = β = a·e<super>kz</super>"],
    ["Intermedias", "<b>Elipses</b> que se aplastan hacia el fondo; en el fondo, un <b>segmento horizontal</b> (β = 0)", "β/α = tanh k(h+z)"],
    ["Reducidas", "<b>Elipses muy planas</b>: el movimiento horizontal es igual en toda la columna, el vertical va de a (superficie) a 0 (fondo)", "α = a/(kh);  β = a(1 + z/h)"],
], [24, 104, 42])
P("<b>Matiz (flujo de masa):</b> la teoría lineal da órbitas cerradas, pero la velocidad arriba (bajo la cresta) es algo mayor que abajo, así que la partícula "
  "avanza un poco en cada ciclo → <b>transporte neto de masa</b> en el sentido de la ola (deriva de Stokes).")

# ------------------------------------------------------------ 4
h2("4. Tsunamis (anotación)")
box("<b>Para recordar:</b> en tsunamis, como dato, la profundidad es <b>reducida</b>.")

# ------------------------------------------------------------ 5
h2("5. Distribución de Rayleigh")
P("<b>De dónde viene.</b> El oleaje se trata como un proceso <b>estocástico, estacionario y ergódico</b> (estado de mar ≈ 1 h). Por el teorema central del límite, "
  "la suma de muchos trenes independientes hace que η sea <b>gaussiana</b> de media 0 (válido para oleaje lineal en indefinidas). Si además el espectro es de "
  "<b>banda estrecha</b> (swell), las alturas de ola siguen <b>Rayleigh</b>, con H<sub>rms</sub> como único parámetro.")
fbox(["<b>f(H) = (2H/H<sub>rms</sub>²)·exp[−(H/H<sub>rms</sub>)²]</b>   (densidad de probabilidad)",
      "<b>F(H) = 1 − exp[−(H/H<sub>rms</sub>)²]</b> = prob(altura ≤ H)   (distribución acumulada)",
      "Con H<sub>s</sub>:  F(H) = 1 − exp[−2,005·(H/H<sub>s</sub>)²]          Con H̄:  F(H) = 1 − exp[−(π/4)·(H/H̄)²]"])
P("<b>Alturas características</b> (H<sub>1/N</sub> = media del 1/N de olas más altas):")
bl("H̄ = media de todas  ·  H<sub>rms</sub> = √(ΣH<sub>i</sub>²/N)  ·  <b>H<sub>1/3</sub> = H<sub>s</sub></b> = media del tercio más alto  ·  H<sub>1/10</sub>, H<sub>1/100</sub>  ·  H<sub>max</sub> = la mayor  ·  η<sub>rms</sub> = √m₀")
table(["N", "1 (H̄)", "3 (H<sub>s</sub>)", "10", "100", "Lectura rápida"], [
    ["H<sub>1/N</sub> / H<sub>rms</sub>", "0,886", "<b>1,416</b>", "1,800", "2,359", "H<sub>s</sub> ≈ √2·H<sub>rms</sub>"],
    ["H<sub>1/N</sub> / H̄", "1,000", "1,597", "2,030", "2,662", "H<sub>s</sub> ≈ 1,6·H̄"],
    ["H<sub>1/N</sub> / η<sub>rms</sub>", "2,505", "<b>4,004</b>", "5,090", "6,671", "H<sub>s</sub> ≈ 4·√m₀ = H<sub>m0</sub>"],
], [30, 20, 20, 20, 20, 60])
P("<b>Ola máxima</b> de un estado de mar de N olas (olas independientes, Longuet-Higgins): F(H<sub>max,N</sub>) = F(H)<super>N</super>, con N = duración/T<sub>m</sub>. "
  "Moda: H<sub>max</sub>/H<sub>rms</sub> = √(ln N); media: √(ln N) + 0,5772/(2√(ln N)). Para 1000 olas, H<sub>max</sub> ≈ 2,74·H<sub>rms</sub> ≈ 1,93·H<sub>s</sub>.")
P("<b>Límites:</b> en someras el oleaje deja de ser gaussiano (crestas picudas, senos planos: aparecen sesgo y curtosis) y Rayleigh sobreestima un poco las alturas.")

# ------------------------------------------------------------ 6
h2("6. Altura superada por el 2 % de las mayores olas")
P("Ejemplo de la diapositiva: <i>calcular la altura de ola que es superada solo por el 2 % de las mayores olas de un estado de mar de H<sub>rms</sub> = 3 m.</i>")
fbox(["Probabilidad de excedencia:   q = P(H &gt; H<sub>q</sub>) = 1 − F(H<sub>q</sub>) = <b>exp[−(H<sub>q</sub>/H<sub>rms</sub>)²]</b>",
      "Despejando:   <b>H<sub>q</sub> = H<sub>rms</sub>·√(−ln q)</b>",
      "q = 0,02:   H<sub>2%</sub> = H<sub>rms</sub>·√(−ln 0,02) = 1,978·H<sub>rms</sub> = 1,978·3 = <b>5,93 m</b>"])
figure(fig_rayleigh(), "Figura 6. H₂% deja a su derecha el 2 % del área bajo la curva de Rayleigh.")
bl("Paso a paso: (1) escribir q = exp[−(H<sub>q</sub>/H<sub>rms</sub>)²]; (2) ln q = −(H<sub>q</sub>/H<sub>rms</sub>)²; (3) H<sub>q</sub> = H<sub>rms</sub>√(−ln q).",
   "Si te dan H<sub>s</sub>: primero H<sub>rms</sub> = H<sub>s</sub>/1,416, o directamente H<sub>2%</sub> = 1,978/1,416·H<sub>s</sub> = <b>1,40·H<sub>s</sub></b>.",
   "<b>No confundir:</b> H<sub>2%</sub> es la altura que solo superan 2 de cada 100 olas; H<sub>1/50</sub> sería la <i>media</i> de esas 2 olas (algo mayor).",
   "Comprobaciones útiles: P(H &gt; H<sub>rms</sub>) = e<super>−1</super> = 37 %;  P(H &gt; H<sub>s</sub>) = e<super>−2,005</super> = 13,5 %.")

# ------------------------------------------------------------ 7
h2("7. Sea frente a swell · mar de fondo frente a resaca")
figure(fig_sea_swell(), "Figura 7. Arriba, registros de superficie libre simulados con la misma H<sub>m0</sub>; abajo, sus espectros.")
table(["", "SEA (mar de viento)", "SWELL (mar de fondo, mar tendida)"], [
    ["Origen", "Viento local que <b>sigue soplando</b> en la zona", "Olas generadas por una borrasca <b>lejana</b> que han salido de la zona de generación"],
    ["Aspecto", "Irregular, crestas cortas, desordenado", "Regular, crestas largas, «peinado», forma más definida"],
    ["Periodo", "Corto", "Largo (frecuencia más estable)"],
    ["Espectro", "<b>Banda ancha</b> en frecuencias y direcciones", "<b>Banda estrecha</b> → aquí vale Rayleigh; H<sub>m0</sub> ≈ 1,05·H<sub>1/3</sub>"],
    ["Modelo espectral", "JONSWAP (fetch limitado, en crecimiento)", "Pico estrecho (JONSWAP con γ alto)"],
    ["Dirección", "La del viento local", "La de la tormenta lejana: mar abierto"],
], [24, 68, 78])
P("<b>Por qué el swell es largo y estrecho:</b> por dispersión. En indefinidas las olas largas viajan más rápido (c = 1,56·T), así que al alejarse de la tormenta "
  "se separan por periodos y las cortas se disipan antes. Llega un oleaje filtrado: periodo largo y casi uniforme. "
  "Un mismo registro puede tener los dos a la vez (<b>mar mixto</b>): se suman las energías, m₀ = m<sub>0,sea</sub> + m<sub>0,swell</sub>.")
h3("Mar de fondo frente a resaca")
note("<b>Ojo:</b> «resaca» no aparece en las diapositivas que hay en el repositorio; lo que sigue es la definición habitual en costas. Si el profesor la explicó "
     "en clase con otro matiz, manda lo que dijo él.")
table(["", "Mar de fondo (swell)", "Resaca"], [
    ["Qué es", "Un <b>oleaje</b>: ondas que se propagan", "Una <b>corriente</b>: agua que se mueve hacia mar adentro"],
    ["Dónde se genera", "Lejos, en una borrasca; llega a la costa sin viento", "En la propia playa, por la rotura de las olas"],
    ["Mecanismo", "Propagación de ondas generadas por el viento", "Las olas que rompen acumulan agua en la orilla; esa agua vuelve al mar por el fondo "
     "o concentrada en canales estrechos (corrientes de retorno, <i>rip currents</i>)"],
    ["Qué transporta", "Energía (el agua solo describe órbitas)", "Masa de agua (y arena, y bañistas): peligrosa"],
], [28, 66, 76])
P("<b>Relación entre ambos:</b> el mar de fondo suele <b>provocar</b> resaca fuerte, porque sus olas largas y energéticas rompen con fuerza y meten mucha agua en la "
  "orilla. Es habitual tener un día de sol, sin viento y sin oleaje local (sin sea) pero con mar de fondo y resaca peligrosa. "
  "En ingeniería portuaria también se llama «resaca» a la agitación del agua dentro de un puerto por ondas largas que entran en resonancia.")

out = sys.argv[1] if len(sys.argv) > 1 else "preguntas_clave.pdf"
build(out, "Oceanografía · Preguntas clave del profesor · Carlos Sánchez Campos", "Oceanografía — Preguntas clave del profesor")
