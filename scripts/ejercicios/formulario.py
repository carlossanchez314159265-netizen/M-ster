"""Formulario completo del 1er parcial de Oceanografía (cada ecuación con su leyenda de términos).

Uso: python3 formulario.py "../../parcial 1/11 - Formulario 1er parcial.pdf"
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "resumenes"))
from estilo import *
import re as _re

_fbox = fbox


def fbox(lines, bg=FBG):
    """Igual que estilo.fbox, pero parte las líneas largas por sus separadores para que no se corten a mitad de fórmula."""
    out = []
    for l in lines:
        vis = _re.sub(r"<[^>]+>", "", l)
        if len(vis) > 95 and _re.search(r" {6,}", l):
            cur = ""
            for x in [x.strip() for x in _re.split(r" {6,}", l) if x.strip()]:
                cand = (cur + "      " + x) if cur else x
                if cur and len(_re.sub(r"<[^>]+>", "", cand)) > 88:
                    out.append(cur); cur = x
                else:
                    cur = cand
            out.append(cur)
        else:
            out.append(l)
    _fbox(out, bg)


P("Oceanografía · Formulario del 1er parcial", H1)
P("Introducción · Mecánica de ondas (teoría lineal) · Análisis estadístico · Análisis espectral · cada ecuación con sus términos y unidades · "
  "examen 28/10/2026", SUB)
note("<b>Cómo usarlo:</b> el martes tienes que poder escribir de memoria lo marcado con ★ (es lo que ha salido en los exámenes). "
     "Cópialo a mano una vez: escribirlo es lo que lo fija. Si algo no coincide con la notación de la diapositiva, manda la diapositiva.")

h2("0. Convenios y constantes")
terms([
    ("g", "Gravedad = 9,81 m/s²"), ("ρ", "Densidad del agua de mar ≈ 1025 kg/m³ (dulce 1000)"),
    ("H", "Altura de ola: de seno a cresta [m]"), ("a", "Amplitud = H/2 [m]"),
    ("T", "Periodo [s]"), ("f", "Frecuencia = 1/T [Hz]"), ("ω", "Frecuencia angular = 2π/T = 2πf [rad/s]"),
    ("L", "Longitud de onda [m]"), ("k", "Número de onda = 2π/L [rad/m]"), ("c", "Celeridad = L/T = ω/k [m/s]"),
    ("h", "Profundidad (del nivel en reposo al fondo) [m]"), ("z", "Cota vertical: 0 en el nivel medio, −h en el fondo [m]"),
    ("η", "Elevación de la superficie libre sobre el nivel medio [m]"), ("θ", "Fase = kx − ωt [rad] (o dirección, según contexto)"),
    ("Calculadora", "Siempre en <b>radianes</b>"), ("1 dbar", "≈ 1 m de profundidad; 10 dbar = 1 bar"),
])

# =========================================================== 1
h2("1. Introducción: propiedades del agua de mar")
fbox(["σ = ρ − 1000          (anomalía de densidad, kg/m³)          ρ ≈ 1025 → σ ≈ 25"])
terms([("σ", "Anomalía de densidad respecto al agua pura [kg/m³]"), ("ρ", "Densidad del agua de mar [kg/m³]")])
fbox(["ρ(S, T, p) = ρ(S, T, 0) / [1 − p / K(S, T, p)]          ρ(S, T, 0) = A + B·S + C·S<super>3/2</super> + D·S²"])
terms([("ρ(S,T,0)", "Densidad a presión atmosférica (UNESCO 1981/83) [kg/m³]"), ("K(S,T,p)", "Módulo de compresibilidad secante [bar]"),
       ("S", "Salinidad [PSU ≈ g/kg ≈ ‰]; agua de mar típica ≈ 35"), ("T", "Temperatura [°C]"), ("p", "Presión [bar]"),
       ("A, B, C, D", "Polinomios en T (coeficientes UNESCO)")])
P("La densidad <b>aumenta</b> con S y con p y <b>disminuye</b> con T. Termoclina / haloclina / picnoclina: capas donde T / S / ρ cambian rápido con la profundidad.")
fbox(["Mezcla de dos masas de agua:   T = (m₁T₁ + m₂T₂)/(m₁ + m₂)      S = (m₁S₁ + m₂S₂)/(m₁ + m₂)      %A = b/(a + b)·100"])
terms([("m₁, m₂", "Masas (o proporciones) de cada agua"), ("T₁, S₁, T₂, S₂", "Temperatura y salinidad de cada agua tipo"),
       ("a, b", "Distancias del punto de mezcla a cada agua tipo en el diagrama T-S"), ("%A", "Porcentaje del agua A en la mezcla")])
fbox(["Flotabilidad neutra:   (m<sub>cuerpo</sub> + m<sub>lastre</sub>)·g = ρ<sub>agua</sub>·V·g   →   m<sub>lastre</sub> = ρ<sub>agua</sub>·V − m<sub>cuerpo</sub>"])
terms([("V", "Volumen desplazado [m³]"), ("ρ<sub>agua</sub>", "Densidad del agua a esa profundidad [kg/m³]"), ("m<sub>lastre</sub>", "Lastre necesario [kg]")])

# =========================================================== 2
h2("2. Mecánica de ondas: clasificación y dispersión")
table(["Zona", "h/L (o kh)", "tanh(kh)", "Dispersión", "c", "L"], [
    ["Indefinidas", "&gt; 1/2  (kh &gt; π)", "≈ 1", "ω² = gk", "c₀ = gT/2π = 1,56·T", "L₀ = gT²/2π = 1,56·T²"],
    ["Intermedias", "1/20 – 1/2", "completa", "ω² = gk·tanh(kh)", "c₀·tanh(kh)", "L₀·tanh(kh)"],
    ["Reducidas", "&lt; 1/20  (kh &lt; π/10)", "≈ kh", "ω² = gk²h", "√(gh)", "T·√(gh)"],
], [22, 30, 18, 32, 34, 34])
fbox(["★ <b>ω² = g·k·tanh(kh)</b>        L = (gT²/2π)·tanh(2πh/L)        c = (gT/2π)·tanh(kh)        L/L₀ = c/c₀ = tanh(kh)"])
terms([("ω", "Frecuencia angular [rad/s]: la fija T, que se conserva al propagarse"), ("k", "Número de onda [rad/m]"),
       ("tanh(kh)", "Efecto del fondo: 1 en profundas, kh en someras"), ("L₀, c₀", "Longitud y celeridad en indefinidas"),
       ("L/L₀", "Cociente local/indefinidas = tanh(kh) (atajo del ejercicio 1)")])
fbox(["★ Dato k y T, piden h:   <b>h = arctanh[ω²/(g·k)] / k</b>          Dato k y h, piden T:   ω = √(g·k·tanh kh)"])
terms([("arctanh", "Inversa de la tangente hiperbólica (hyp + tan⁻¹)"), ("ω²/(gk)", "Debe salir entre 0 y 1; si no, hay un error")])
fbox(["Dato T y h, piden k: iterar (Newton-Raphson):   k<sub>n+1</sub> = k<sub>n</sub> − f/f'",
      "f = ω² − gk·tanh(kh)      f' = −g·tanh(kh) − g·h·k·sech²(kh)      arranque k₀ = ω²/g"])
terms([("k₀ = ω²/g", "Arranque (valor de profundas)"), ("sech²", "1/cosh²"), ("SOLVE", "En la calculadora: ω² − g·X·tanh(X·h) = 0")])
fbox(["Explícitas: Fenton-McKee  L ≈ L₀·[tanh((2πh/L₀)<super>3/4</super>)]<super>2/3</super> (&lt;1,5 %)      Guo  kh ≈ (ω²h/g)·[1 − exp(−(ω√(h/g))<super>5/2</super>)]<super>−2/5</super> (&lt;0,7 %)"])
terms([("L₀", "gT²/2π"), ("ω√(h/g)", "Profundidad adimensional")])
fbox(["Peralte  ε = H/L      máximo en profundas H/L ≈ 0,142 ≈ 1/7      Profundidad relativa h/L      Número de Ursell  U = HL²/h³"])
terms([("ε", "Peralte: mide la no linealidad"), ("1/7", "Límite de rotura por peralte en profundas"),
       ("U", "Ursell: si es pequeño vale la teoría lineal (Airy); si es grande, cnoidal/solitaria")])

h3("Problema de contorno (teoría potencial)")
fbox(["∇²φ = ∂²φ/∂x² + ∂²φ/∂z² = 0   (Laplace)          u = ∂φ/∂x,  w = ∂φ/∂z",
      "Fondo (z = −h):  w = 0          Cinemática superficie:  w = ∂η/∂t          Dinámica superficie (Bernoulli lineal):  ∂φ/∂t + gη = 0",
      "Solución lineal:  φ = (gH/2ω)·cosh k(h+z)/cosh kh · sin(kx − ωt)          η = (H/2)·cos(kx − ωt)"])
terms([("φ", "Potencial de velocidades [m²/s]"), ("∇²", "Laplaciano"), ("u, w", "Velocidades horizontal y vertical [m/s]"),
       ("Hipótesis", "Fluido ideal, incompresible, irrotacional; pequeña amplitud (H/L, H/h pequeños); fondo fijo e impermeable")])

# =========================================================== 3
h2("3. Cinemática, trayectorias y presiones (onda progresiva)")
fbox(["★ u = (H/2)·ω · cosh k(h+z)/sinh kh · cos θ          w = (H/2)·ω · sinh k(h+z)/sinh kh · sin θ          θ = kx − ωt",
      "a<sub>x</sub> = (H/2)·ω² · cosh k(h+z)/sinh kh · sin θ          a<sub>z</sub> = −(H/2)·ω² · sinh k(h+z)/sinh kh · cos θ"])
terms([("u, w", "Velocidad horizontal y vertical de la partícula [m/s]"), ("a<sub>x</sub>, a<sub>z</sub>", "Aceleraciones [m/s²]"),
       ("h + z", "Distancia del punto al fondo [m]"), ("θ = 0", "Bajo la cresta: u máxima hacia delante"),
       ("u<sub>max</sub> en superficie", "(H/2)·ω·coth(kh); en el fondo (H/2)·ω/sinh(kh)")])
fbox(["★ A = (H/2)·cosh k(h+z)/sinh kh          B = (H/2)·sinh k(h+z)/sinh kh          <b>B/A = tanh k(h+z)</b>"])
terms([("A", "Semieje horizontal (mayor) de la órbita [m]"), ("B", "Semieje vertical (menor) [m]; B = H/2 en superficie y 0 en el fondo")])
table(["Zona", "Órbitas"], [
    ["Indefinidas", "Círculos de radio (H/2)·e<super>kz</super> (a z = −L/2 quedan al 4 %)"],
    ["Intermedias", "Elipses que se achatan hacia el fondo; en el fondo, segmento horizontal"],
    ["Reducidas", "A = (H/2)/(kh) constante en la vertical; B = (H/2)·(1 + z/h)"],
], [30, 140])
fbox(["★ p = −ρgz + ρg·(H/2)·K<sub>p</sub>·cos θ          K<sub>p</sub> = cosh k(h+z)/cosh kh          en el fondo: K<sub>p</sub> = 1/cosh kh"])
terms([("p", "Presión manométrica [Pa = N/m²]"), ("−ρgz", "Parte hidrostática (z &lt; 0 → positiva)"),
       ("ρg(H/2)K<sub>p</sub>", "Amplitud de la presión dinámica [Pa]"), ("K<sub>p</sub>", "Factor de respuesta de presión (≤ 1)"),
       ("Dos sensores", "p₁/p₂ = cosh k(h+z₁)/cosh k(h+z₂) → k sin conocer H ni h")])
fbox(["Tsunami / onda larga sobre fondo variable:   c = √(g·h(x))      ★ t = ∫ dx / √(g·h(x))      talud lineal desde h₀:  t = 2√h₀ / (s·√g)"])
terms([("h(x)", "Profundidad a lo largo del recorrido [m]"), ("s", "Pendiente del talud [−]"), ("t", "Tiempo de viaje [s]")])

# =========================================================== 4
h2("4. Superposición: estacionarias, grupos y energía")
fbox(["Estacionaria (reflexión total):  η = H<sub>i</sub>·cos(kx)·cos(ωt)  →  H = 2H<sub>i</sub> en antinodos, 0 en nodos;  nodo ↔ antinodo = L/4"])
terms([("H<sub>i</sub>", "Altura incidente [m]"), ("Nodos", "kx = (2n+1)π/2: no hay movimiento vertical"), ("Antinodos", "kx = nπ: oscilación máxima")])
fbox(["★ Cuasi-estacionaria:  η = (H<sub>i</sub>/2)cos(kx − ωt) + (H<sub>r</sub>/2)cos(kx + ωt + ε)",
      "envolvente:  H<sub>i</sub> + H<sub>r</sub> (antinodo)      H<sub>i</sub> − H<sub>r</sub> (cuasi-nodo)      K<sub>r</sub> = H<sub>r</sub>/H<sub>i</sub>      K<sub>t</sub> = H<sub>t</sub>/H<sub>i</sub>      separación L/4"])
terms([("H<sub>r</sub>", "Altura reflejada [m]"), ("H<sub>t</sub>", "Altura transmitida [m]"), ("K<sub>r</sub>, K<sub>t</sub>", "Coeficientes de reflexión y transmisión"),
       ("ε", "Desfase de la reflexión [rad]"), ("η<sub>max</sub>, η<sub>min</sub>", "= ½(H<sub>i</sub> + H<sub>r</sub>) y ½(H<sub>i</sub> − H<sub>r</sub>)")])
fbox(["Crestas cortas (oblicua):  η = 2A·cos(k·sinθ·y)·cos(k·cosθ·x − ωt)   → progresa en x, estacionaria en y"])
terms([("θ", "Ángulo de incidencia"), ("A", "Amplitud de cada tren [m]")])
fbox(["★ Grupo bicromático:  η = H·cos(kx − ωt)·cos[½(Δk·x − Δω·t)]      ω = (ω₁ + ω₂)/2      Δω = ω₂ − ω₁      Δk = k₂ − k₁",
      "★ c = ω/k      c<sub>g</sub> = Δω/Δk → dω/dk = n·c      L<sub>g</sub> = 2π/Δk      T<sub>g</sub> = 2π/Δω = T₁T₂/(T₁ − T₂)      T<sub>modulante</sub> = 4π/Δω"])
terms([("H", "= H₁ = H₂ (dos trenes iguales); la ola mayor del grupo mide 2H"), ("c", "Celeridad de la portadora (olas) [m/s]"),
       ("c<sub>g</sub>", "Celeridad de grupo: la de la envolvente y la energía [m/s]"), ("T<sub>g</sub>, L<sub>g</sub>", "Periodo y longitud del grupo"),
       ("T<sub>modulante</sub>", "Periodo de la función cos[½(…)]")])
fbox(["★ <b>n = ½·[1 + 2kh / sinh(2kh)]</b>        c<sub>g</sub> = n·c        profundas n = ½ (c<sub>g</sub> = c₀/2)        someras n = 1 (c<sub>g</sub> = c = √gh)"])
terms([("n", "Cociente c<sub>g</sub>/c"), ("2kh/sinh 2kh", "→ 0 en profundas, → 1 en someras")])
fbox(["★ <b>E = ρgH²/8</b> = ½ρga²   [J/m²]      E<sub>c</sub> = E<sub>p</sub> = ρgH²/16      ★ F = E·c<sub>g</sub>   [W/m]      profundas: P = ρg²H²T/(32π)"])
terms([("E", "Energía media por unidad de superficie [J/m²]; no depende de T ni de h"), ("E<sub>c</sub>, E<sub>p</sub>", "Cinética y potencial (iguales)"),
       ("F", "Flujo de energía (potencia por metro de frente) [W/m]")])
fbox(["Asomeramiento (sin refracción ni rotura): F = cte  →  H₂/H₁ = √(c<sub>g1</sub>/c<sub>g2</sub>)          Flujo de masa  M = ρgH²/(8c)"])
terms([("c<sub>g1</sub>, c<sub>g2</sub>", "Celeridades de grupo en los puntos 1 y 2"), ("M", "Flujo de masa medio (deriva de Stokes) [kg/(m·s)]")])
fbox(["Con corriente U:  (ω − k·U·cosθ)² = g·k·tanh(kh)   (σ = ω − k·U·cosθ, frecuencia intrínseca)"])
terms([("U", "Velocidad de la corriente [m/s]"), ("σ", "Frecuencia relativa al agua"), ("ω", "Frecuencia que mide un observador fijo")])

# =========================================================== 5
h2("5. Análisis estadístico (dominio del tiempo)")
fbox(["H<sub>max</sub> = max H<sub>i</sub>          ★ H<sub>1/3</sub> = (3/N)·Σ<sub>N/3 mayores</sub> H<sub>i</sub>          H<sub>m</sub> = (1/N)·Σ H<sub>i</sub>          ★ H<sub>rms</sub> = √[(1/N)·Σ H<sub>i</sub>²]          T<sub>m</sub> = (1/N)·Σ T<sub>i</sub>"])
terms([("H<sub>i</sub>, T<sub>i</sub>", "Altura y periodo de la ola i (entre dos pasos ascendentes por cero)"), ("N", "Número de olas (≥ 100, ideal 1000)"),
       ("H<sub>1/3</sub> = H<sub>s</sub>", "Altura significante: media del tercio de olas más altas"),
       ("T<sub>1/3</sub>", "Media de los periodos de esas mismas olas"), ("H<sub>1/n</sub>", "Media de las N/n olas más altas"),
       ("T<sub>max</sub>", "Periodo de la ola más alta")])
fbox(["η normal:  f(η) = [1/(η<sub>rms</sub>√2π)]·exp(−η²/2η<sub>rms</sub>²)          η<sub>rms</sub> = √m₀"])
terms([("η<sub>rms</sub>", "Desviación típica de la superficie libre [m]"), ("Validez", "Oleaje lineal (indefinidas); en someras η no es gaussiana")])
fbox(["★ Rayleigh:  F(H) = 1 − exp[−(H/H<sub>rms</sub>)²]      f(H) = (2H/H<sub>rms</sub>²)·exp[−(H/H<sub>rms</sub>)²]",
      "★ <b>q = P(H &gt; H<sub>q</sub>) = exp[−(H<sub>q</sub>/H<sub>rms</sub>)²]</b>      ★ <b>H<sub>q</sub> = H<sub>rms</sub>·√(−ln q)</b>"])
terms([("F(H)", "Probabilidad de que una ola sea ≤ H"), ("f(H)", "Densidad de probabilidad [1/m]"), ("q", "Probabilidad de excedencia (por ola)"),
       ("H<sub>q</sub>", "Altura superada por la fracción q de las olas [m]"), ("Validez", "Banda estrecha, olas independientes, lineal")])
table(["Relación (Rayleigh)", "Valor", "Relación", "Valor"], [
    ["H<sub>m</sub>/H<sub>rms</sub>", "0,886 = √π/2", "★ H<sub>1/3</sub>/H<sub>rms</sub>", "<b>1,416 ≈ √2</b>"],
    ["H<sub>1/10</sub>/H<sub>rms</sub>", "1,800", "H<sub>1/100</sub>/H<sub>rms</sub>", "2,359"],
    ["H<sub>rms</sub>/η<sub>rms</sub>", "2√2 = 2,83", "★ H<sub>1/3</sub>/η<sub>rms</sub>", "4,004 (→ H<sub>m0</sub> = 4√m₀)"],
    ["H<sub>1/3</sub>/H<sub>m</sub>", "1,597", "H<sub>1/10</sub>/H<sub>1/3</sub>", "1,271"],
], [42, 43, 42, 43])
fbox(["F(H<sub>max,N</sub>) = {1 − exp[−(H<sub>max</sub>/H<sub>rms</sub>)²]}<super>N</super>          ★ N = duración / T<sub>m</sub>",
      "★ Moda (más probable):  H<sub>max</sub>/H<sub>rms</sub> = √(ln N)          ★ Media:  H<sub>max</sub>/H<sub>rms</sub> = √(ln N) + (C/2)·(ln N)<super>−1/2</super>"])
terms([("N", "Número de olas del estado de mar"), ("C", "Constante de Euler = 0,57722"), ("duración", "En segundos (1 h = 3600 s)"),
       ("Regla rápida", "En 1–3 h: H<sub>max</sub> ≈ 1,8–2·H<sub>s</sub>")])
table(["N", "100", "500", "1000", "2000", "5000"], [
    ["H<sub>max</sub>/H<sub>rms</sub> media", "2,280", "2,609", "2,738", "2,862", "3,017"],
    ["H<sub>max</sub>/H<sub>rms</sub> moda", "2,146", "2,493", "2,628", "2,757", "2,918"],
], [50, 24, 24, 24, 24, 24])
fbox(["Cresta (lineal) = H/2      ★ rebase si H/2 &gt; Z<sub>cubierta</sub>      ★ runup  R<sub>u</sub> = η<sub>max</sub> + u²/(2g)      freak wave:  H/H<sub>s</sub> &gt; 2  ó  η<sub>cresta</sub>/H<sub>s</sub> &gt; 1,25"])
terms([("Z<sub>cubierta</sub>", "Cota de la cubierta sobre el nivel medio [m]"), ("R<sub>u</sub>", "Cota que alcanza el agua [m] (fórmula que da el enunciado)"),
       ("u", "Velocidad orbital horizontal en superficie [m/s]"), ("Freak (Haver, 2000)", "Ola anómala respecto al estado de mar")])

# =========================================================== 6
h2("6. Análisis espectral (dominio de la frecuencia)")
fbox(["★ <b>m<sub>n</sub> = ∫₀<super>∞</super> ω<super>n</super>·S(ω) dω</b>      ★ m₀ = área = η<sub>rms</sub>² = σ<sub>η</sub>²      ★ <b>H<sub>m0</sub> = 4√m₀</b>      ★ E = ρg·m₀  [J/m²]"])
terms([("S(ω)", "Espectro escalar de varianza [m²·s/rad]"), ("m<sub>n</sub>", "Momento de orden n"), ("H<sub>m0</sub>", "Altura significante espectral (≈ H<sub>1/3</sub> en banda estrecha)"),
       ("E", "Energía media por unidad de superficie [J/m²]")])
fbox(["Parseval (suma de componentes):  m₀ = Σ a<sub>i</sub>²/2 = Σ H<sub>i</sub>²/8      ★ mar mixto:  m₀ = m<sub>0,sea</sub> + m<sub>0,swell</sub>  →  H<sub>m0</sub> = √(H<sub>sea</sub>² + H<sub>swell</sub>²)"])
terms([("a<sub>i</sub>, H<sub>i</sub>", "Amplitud y altura de cada componente"), ("Regla", "Se suman varianzas (H²), nunca alturas"),
       ("Onda regular", "H<sub>m0</sub> = √2·H = 1,41·H")])
table(["Parámetro", "Con S(ω) [rad/s]", "Con S(f) [Hz]", "Qué es"], [
    ["★ T<sub>p</sub>", "2π/ω<sub>p</sub>", "1/f<sub>p</sub>", "Periodo de pico (máximo de S)"],
    ["★ T<sub>01</sub> = T<sub>m</sub>", "2π·m₀/m₁", "m₀/m₁", "Periodo medio (centro de gravedad)"],
    ["★ T<sub>02</sub> = T<sub>z</sub>", "2π·√(m₀/m₂)", "√(m₀/m₂)", "Periodo medio de pasos por cero"],
    ["T<sub>c</sub> = T<sub>24</sub>", "2π·√(m₂/m₄)", "√(m₂/m₄)", "Periodo medio entre crestas"],
    ["T<sub>e</sub> = T<sub>−10</sub>", "2π·m<sub>−1</sub>/m₀", "m<sub>−1</sub>/m₀", "Periodo energético (potencia)"],
    ["General", "T<sub>ij</sub> = 2π·(m<sub>i</sub>/m<sub>j</sub>)<super>1/(j−i)</super>", "sin 2π", ""],
], [32, 50, 34, 54])
terms([("ω<sub>p</sub>, f<sub>p</sub>", "Frecuencia del máximo del espectro"), ("m<sub>−1</sub>", "Momento de orden −1"),
       ("Orden habitual", "T<sub>c</sub> &lt; T<sub>z</sub> &lt; T<sub>01</sub> &lt; T<sub>e</sub> &lt; T<sub>p</sub>")])
fbox(["★ ε = √[1 − m₂²/(m₀·m₄)]   (0 banda estrecha … 1 ancha)          ν = √[m₀m₂/m₁² − 1]          S(f) = 2π·S(ω)      m<sub>n</sub>(ω) = (2π)<super>n</super>·m<sub>n</sub>(f)"])
terms([("ε", "Anchura espectral de Cartwright y Longuet-Higgins"), ("ν", "Anchura de Longuet-Higgins"),
       ("S(f) = 2πS(ω)", "Cambio de variable (m₀ es el mismo en ambas)")])
fbox(["Potencia del oleaje:  P = ρg·∫ c<sub>g</sub>(ω)·S(ω) dω      profundas:  P = ρg²·H<sub>m0</sub>²·T<sub>e</sub>/(64π) ≈ 0,49·H<sub>m0</sub>²·T<sub>e</sub>  [kW/m]"])
terms([("P", "Flujo de energía del estado de mar [kW/m]"), ("T<sub>e</sub>", "Periodo energético [s]")])
fbox(["Pierson-Moskowitz (totalmente desarrollado):  S(ω) = 0,0081·g²·ω<super>−5</super>·exp[−1,25·(ω/ω<sub>p</sub>)<super>−4</super>]      ω<sub>p</sub> = 0,879·g/U<sub>19,5</sub>      H<sub>m0</sub> ≈ 0,04·T<sub>p</sub>²"])
terms([("U<sub>19,5</sub>", "Velocidad del viento a 19,5 m [m/s]"), ("0,0081", "Constante de Phillips α"),
       ("Uso", "Mar abierto, fetch y duración ilimitados")])
fbox(["JONSWAP (en crecimiento, fetch limitado):  S(ω) = α·g²·ω<super>−5</super>·exp[−1,25·(ω/ω<sub>p</sub>)<super>−4</super>]·γ<super>δ</super>",
      "δ = exp[−(ω − ω<sub>p</sub>)²/(2σ₀²ω<sub>p</sub>²)]      γ = 3,3 (1–7)      σ₀ = 0,07 (ω ≤ ω<sub>p</sub>) / 0,09 (ω &gt; ω<sub>p</sub>)"])
terms([("γ", "Factor de apuntamiento del pico (γ = 1 → PM)"), ("δ", "Forma de la región del pico"), ("σ₀", "Anchura del pico"),
       ("α", "Constante de escala (depende del fetch)"), ("Fetch", "Longitud sobre la que sopla el viento uniforme [km]")])
fbox(["TMA (someras) = JONSWAP·φ(ω, h)      Goda (JONSWAP en H<sub>s</sub>, T<sub>p</sub>):  S(f) = β<sub>J</sub>·H<sub>s</sub>²·T<sub>p</sub><super>−4</super>·f<super>−5</super>·exp[−1,25(T<sub>p</sub>f)<super>−4</super>]·γ<super>δ</super>"])
terms([("φ(ω,h)", "Factor de profundidad de Kitaigorodskii"), ("β<sub>J</sub>", "Constante que depende de γ (≈ 0,0624/(0,23 + 0,0336γ − 0,185/(1,9+γ))·(1,094 − 0,01915·ln γ))")])
fbox(["Cálculo de espectros:  f<sub>Nyq</sub> = 1/(2Δt)      Δf = 1/T<sub>registro</sub>      Welch con K tramos: Δf = K/T<sub>registro</sub>, error relativo ∝ 1/√(nº de segmentos promediados)"])
terms([("Δt", "Paso de muestreo [s]"), ("f<sub>Nyq</sub>", "Frecuencia de Nyquist: la mayor que se puede resolver [Hz]"),
       ("Periodograma", "Un solo segmento: máxima resolución, error del 100 % en cada punto"),
       ("Welch", "Promedia K segmentos: menos ruido, peor resolución"), ("Parseval", "Comprobación: m₀ = var(η)")])

# =========================================================== 7
h2("7. Recetas de examen (lo que ha caído)")
table(["Bloque", "Pasos"], [
    ["A · Dispersión", "L₀ → T = √(2πL₀/g)  ·  k y T → h = arctanh[ω²/(gk)]/k  ·  presiones: p₁/p₂ → k → dispersión → h → H  ·  comprobar h/L"],
    ["B · Rayleigh + H<sub>max</sub>", "H<sub>s</sub> → H<sub>rms</sub> = H<sub>s</sub>/√2  ·  q = exp[−(H/H<sub>rms</sub>)²]  ·  N = duración/T<sub>m</sub>  ·  H<sub>max</sub> (media con C)  ·  cresta = H/2 o R<sub>u</sub> = η<sub>max</sub> + u²/2g"],
    ["C · Espectral", "m<sub>n</sub> por tramos (comprueba m₀ = área)  ·  H<sub>m0</sub> = 4√m₀  ·  E = ρgm₀  ·  T<sub>p</sub>, T<sub>01</sub>, T<sub>z</sub> con 2π si S(ω)  ·  ε  ·  mixtos: sumar m₀"],
], [35, 135])
note("<b>Fallos que más puntos cuestan:</b> calculadora en grados · olvidar que a = H/2 · z positiva en vez de negativa · sumar alturas en vez de H² · "
     "2π de más o de menos en los periodos espectrales · moda frente a media de H<sub>max</sub> · usar √(gh) fuera de someras.")

out = sys.argv[1] if len(sys.argv) > 1 else "formulario.pdf"
build(out, "Oceanografía · Formulario del 1er parcial · Carlos Sánchez Campos", "Oceanografía — Formulario del 1er parcial")
