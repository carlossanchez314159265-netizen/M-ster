"""Compendio de TODOS los ejercicios del 1er parcial de Oceanografía, resueltos y explicados.

Uso: python3 ejercicios_resueltos.py "../../parcial 1/10 - Ejercicios resueltos (todos).pdf"
(los exámenes anteriores resueltos se añaden al final como anexo con unir_anexo.py)
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "resumenes")); sys.path.insert(0, HERE)
from estilo import *
import figuras_ejercicios as fx

P("Oceanografía · Ejercicios resueltos del 1er parcial", H1)
P("Todos los ejercicios del material del 1er parcial (28/10/2026), resueltos paso a paso y explicados desde cero · "
  "teoría de ondas, análisis estadístico, análisis espectral e introducción · cada ecuación lleva su leyenda de términos", SUB)

note("<b>Cómo usar este PDF:</b> lee el enunciado (recuadro), tapa la resolución e inténtalo tú 10–15 min con calculadora. Luego corrige. "
     "Cada ejercicio sigue el mismo orden: <b>idea</b> → <b>planteamiento</b> → <b>cálculo</b> → <b>resultado</b> → <b>trampas</b>. "
     "Todos los números están recalculados; donde la solución del profesor tiene una errata o redondea distinto lo verás en ámbar.")

table(["Parte", "Ejercicio", "Tema", "Prioridad para el examen"], [
    ["A", "Teoría de ondas 1", "Dispersión: h a partir de L₀ y L", "<b>Máxima</b> (cae seguro un ejercicio de dispersión)"],
    ["A", "Teoría de ondas 2", "Órbitas elípticas → k, L, T, H", "Alta"],
    ["A", "Teoría de ondas 3", "Tsunami sobre un talud: t = ∫dx/√(gh)", "Media"],
    ["A", "Teoría de ondas 4", "Onda cuasi-estacionaria: H<sub>i</sub>, H<sub>r</sub>, transmisión, h", "Media"],
    ["A", "Teoría de ondas 5", "Grupo bicromático: portadora, modulante, c<sub>g</sub>", "Media"],
    ["A", "Ejemplo diapo 82", "Sentido físico de la dispersión (h = 10 m)", "Teoría"],
    ["B", "Paso por cero (diapos 22–25)", "H<sub>max</sub>, H<sub>1/3</sub>, H<sub>m</sub>, H<sub>rms</sub>, T<sub>1/3</sub>…", "Alta"],
    ["B", "Rayleigh (diapos 35–37)", "Altura superada por el 2 % de las olas", "<b>Máxima</b> (cae seguro Rayleigh + H<sub>max</sub>)"],
    ["B", "H<sub>max</sub> (diapos 42–43)", "Ola máxima en N olas (moda y media)", "<b>Máxima</b>"],
    ["C", "Espectral 1 (diapos 75–76)", "H<sub>m0</sub> de 5 componentes", "Alta"],
    ["C", "Espectral 2 (diapo 77)", "Espectro direccional: SEA o SWELL", "Alta (teoría + lectura de figura)"],
    ["C", "Espectral 2 (diapos 78–80)", "S(ω) por tramos: m<sub>n</sub>, H<sub>m0</sub>, E, T<sub>p</sub>, T<sub>01</sub>, T<sub>z</sub>, ε", "<b>Máxima</b> (cae seguro un espectral)"],
    ["D", "Introducción (diapos 53–54)", "Esfera de titanio: lastre y densidad del agua", "Baja (práctica de Matlab)"],
    ["Anexo", "Exámenes 29-10-2025 y 13-01-2025", "Los 6 ejercicios de examen ya resueltos", "<b>Máxima</b>: es el formato real"],
], [13, 42, 65, 50])
note("<b>Formulario:</b> va en un PDF aparte (<i>11 - Formulario 1er parcial</i>), con cada ecuación y sus términos. Tenlo al lado mientras haces estos ejercicios.")

P("<b>Datos y convenios que se usan en todo el PDF</b> (salvo que el enunciado diga otra cosa):")
terms([
    ("g", "Aceleración de la gravedad = 9,81 m/s²"),
    ("ρ", "Densidad del agua de mar = 1025 kg/m³"),
    ("H, a", "Altura de ola (seno a cresta) y amplitud a = H/2 [m]"),
    ("T, ω", "Periodo [s] y frecuencia angular ω = 2π/T [rad/s]"),
    ("L, k", "Longitud de onda [m] y número de onda k = 2π/L [rad/m]"),
    ("h, z", "Profundidad [m]; cota z: 0 en el nivel medio, −h en el fondo (negativa hacia abajo)"),
    ("c", "Celeridad c = L/T = ω/k [m/s]"),
    ("Calculadora", "Modo <b>RADIANES</b> siempre (tanh, cosh y cos con argumentos en rad)"),
])

# =========================================================================================== A
story.append(PageBreak())
P("PARTE A · Teoría de ondas", H1)
P("Los 5 ejercicios del repositorio (<i>ejercicios-teoria-de-ondas/</i>) y el ejemplo de la dispersión de la diapo 82. "
  "Todos giran alrededor de la <b>ecuación de la dispersión</b>; apréndete primero la idea clave:", SUB)
fbox(["<b>ω² = g·k·tanh(kh)</b>        L₀ = gT²/2π        c = L/T = ω/k"])
terms([
    ("ω", "Frecuencia angular = 2π/T [rad/s]. La fija el periodo, que <b>no cambia</b> cuando la ola se propaga"),
    ("k", "Número de onda = 2π/L [rad/m]"),
    ("h", "Profundidad [m]"),
    ("tanh(kh)", "Tangente hiperbólica: ≈ 1 en profundas (kh grande), ≈ kh en someras (kh pequeño)"),
    ("L₀", "Longitud de onda en profundidades indefinidas [m]"),
    ("c", "Celeridad (velocidad de la cresta) [m/s]"),
])
box("<b>Truco que resuelve medio examen:</b> la dispersión tiene 3 magnitudes (T, k, h). Si te dan <b>T y h</b> y piden k → hay que iterar (SOLVE de la calculadora). "
    "Si te dan <b>k (o L) y T</b> y piden h → <b>no se itera</b>: tanh(kh) = ω²/(gk) → h = arctanh[ω²/(gk)] / k. "
    "Si te dan <b>k y h</b> y piden T → directo: ω = √(gk·tanh kh).")

table(["Zona", "h/L", "tanh(kh)", "c", "L"], [
    ["Indefinidas (profundas)", "&gt; 1/2", "≈ 1", "c₀ = gT/2π", "L₀ = gT²/2π = 1,56·T²"],
    ["Intermedias", "1/20 – 1/2", "fórmula completa", "c = c₀·tanh(kh)", "L = L₀·tanh(kh)"],
    ["Reducidas (someras)", "&lt; 1/20", "≈ kh", "c = √(gh)", "L = T·√(gh)"],
], [38, 25, 32, 37, 38])

# ------------------------------------------------------------------ EJ 1
h2("Ejercicio 1 — Profundidad de la plataforma a partir de dos longitudes de onda")
box("<b>Enunciado.</b> A través de teledetección se ha observado que la longitud de onda en profundidades indefinidas de un tren de oleaje es de "
    "<b>312 m</b>, mientras que cuando se adentra en la plataforma continental es de <b>200 m</b>. Calcula la profundidad de la plataforma continental.")
figure(fx.ej1_esquema(), "Figura A1. El mismo tren de ondas (mismo T) se acorta al entrar en menos profundidad.")
h3("Idea")
P("El <b>periodo no cambia</b> al propagarse (cada cresta que entra en la plataforma sale de alta mar: el ritmo se conserva). "
  "Con L₀ saco T; con T y la L de la plataforma, la dispersión me da h. Como conozco k, <b>no hay que iterar</b>.")
h3("Paso 1 — Periodo a partir de L₀")
fbox(["L₀ = gT²/2π   →   T = √(2π·L₀/g) = √(2π·312/9,81) = √199,8 = <b>14,14 s</b>"])
terms([("L₀", "Longitud de onda en indefinidas = 312 m"), ("T", "Periodo del tren de ondas [s]"), ("g", "9,81 m/s²")])
h3("Paso 2 — Dispersión en la plataforma, despejando h")
P("Datos en la plataforma: L = 200 m → k = 2π/200 = 0,03142 rad/m; ω = 2π/14,14 = 0,4445 rad/s.")
fbox(["ω² = g·k·tanh(kh)   →   tanh(kh) = ω² / (g·k) = 0,4445² / (9,81 · 0,03142) = 0,1976 / 0,3082 = <b>0,6410</b>",
      "kh = arctanh(0,6410) = 0,7599      →      h = 0,7599 / 0,03142 = <b>24,2 m</b>"])
terms([("k", "Número de onda en la plataforma = 2π/L [rad/m]"), ("ω", "Frecuencia angular = 2π/T [rad/s]"),
       ("arctanh", "Inversa de la tangente hiperbólica (en la calculadora: hyp + tan⁻¹)"), ("h", "Profundidad de la plataforma [m]")])
P("Atajo elegante: como L = L₀·tanh(kh), directamente tanh(kh) = L/L₀ = 200/312 = 0,641 (mismo número, sin calcular T).")
fbox(["L / L₀ = tanh(kh)   →   tanh(2π·h/200) = 200/312"])
terms([("L/L₀", "Cociente entre la longitud de onda local y la de indefinidas: es directamente tanh(kh)")])
h3("Paso 3 — Comprobar la zona")
P("h/L = 24,2/200 = 0,121 → entre 1/20 y 1/2 → <b>intermedias</b>: había que usar la dispersión completa (bien hecho).")
box("<b>Resultado:</b> T = 14,1 s · h ≈ <b>24,2 m</b> (coincide con el profesor).")
note("<b>Trampa:</b> si usas la fórmula de someras (c = √(gh) → h = (L/T)²/g) sale h = (200/14,14)²/9,81 = 20,4 m: un 16 % de error, porque no estás en someras. "
     "Si redondeas T a 14,1 s antes de seguir sale 24,4 m; arrastra los decimales.")

# ------------------------------------------------------------------ EJ 2
h2("Ejercicio 2 — H, T y L a partir de la órbita de las partículas")
box("<b>Enunciado.</b> A partir de la observación del movimiento de las partículas de un tren de ondas regular de pequeña amplitud propagándose en un canal de "
    "<b>1 m de profundidad</b>, se han obtenido los siguientes resultados en la <b>mitad de la columna de agua</b>: semieje mayor del desplazamiento 0,1 m; "
    "semieje menor 0,05 m. Calcula la altura de ola H, el periodo T y la longitud de onda L.")
figure(fx.ej2_elipse(), "Figura A2. Las partículas describen elipses que se achatan hacia el fondo; los datos son los de la elipse roja (z = −0,5 m).")
h3("Idea")
P("En teoría lineal cada partícula recorre una elipse. Los semiejes dependen de a, k, h y z. "
  "<b>Dividiendo B entre A desaparece la amplitud</b> y queda solo k → con k saco L; con k y h, la dispersión da T; volviendo a A saco H.")
h3("Planteamiento — semiejes de la elipse")
fbox(["A = (H/2) · cosh k(h+z) / sinh kh          B = (H/2) · sinh k(h+z) / sinh kh          <b>B/A = tanh k(h+z)</b>"])
terms([("A", "Semieje horizontal (mayor) = 0,10 m"), ("B", "Semieje vertical (menor) = 0,05 m"),
       ("H/2", "Amplitud de la ola [m]"), ("h", "Profundidad = 1 m"),
       ("z", "Cota de la partícula = −0,5 m (mitad de la columna)"), ("h + z", "Distancia al fondo = 0,5 m")])
h3("Paso 1 — k y L del cociente")
fbox(["B/A = 0,05/0,10 = 0,5 = tanh(0,5k)   →   0,5k = arctanh(0,5) = 0,5493   →   <b>k = 1,099 rad/m</b>",
      "L = 2π/k = 2π/1,099 = <b>5,72 m</b>"])
terms([("tanh(0,5k)", "tanh k(h+z) con h+z = 0,5 m"), ("k", "Número de onda [rad/m]"), ("L", "Longitud de onda [m]")])
h3("Paso 2 — T con la dispersión (k y h conocidos → directo)")
fbox(["ω² = g·k·tanh(kh) = 9,81 · 1,099 · tanh(1,099) = 10,78 · 0,8000 = 8,622   →   ω = 2,936 rad/s",
      "T = 2π/ω = <b>2,14 s</b>"])
terms([("ω", "Frecuencia angular [rad/s]"), ("tanh(1,099)", "tanh(kh) con h = 1 m (= 0,8 exactamente, curiosidad del enunciado)"), ("T", "Periodo [s]")])
h3("Paso 3 — H con el semieje mayor")
fbox(["0,10 = (H/2) · cosh(1,099·0,5) / sinh(1,099) = (H/2) · 1,1547 / 1,3333 = (H/2) · 0,8660",
      "H = 2 · 0,10 / 0,8660 = <b>0,231 m</b>"])
terms([("cosh(0,549)", "= 1,1547"), ("sinh(1,099)", "= 1,3333"), ("H", "Altura de ola [m]")])
P("Comprobación con B: (0,231/2)·sinh(0,549)/sinh(1,099) = 0,1155·0,5774/1,3333 = 0,050 m ✓. Zona: h/L = 1/5,72 = 0,175 → intermedias (fórmulas completas correctas).")
box("<b>Resultado:</b> k = 1,099 rad/m · <b>L = 5,72 m · T = 2,14 s · H = 0,23 m</b> (coincide con el profesor).")
note("<b>Trampa:</b> z es <b>negativa</b> (−0,5 m) y en las fórmulas aparece h + z = 0,5 m, no h − z. Y la amplitud es H/2, no H: si te olvidas del 2, H sale la mitad.")

# ------------------------------------------------------------------ EJ 3
h2("Ejercicio 3 — Llegada de un tsunami sobre un talud")
box("<b>Enunciado.</b> Un sistema de alerta detecta la presencia de un tsunami a las <b>12:00 h</b> en el comienzo de la plataforma continental "
    "(profundidad <b>200 m</b>). La plataforma es un talud suave de pendiente <b>0,005</b> (1 vertical : 200 horizontal) hasta la costa. ¿A qué hora se espera que alcance la costa?")
figure(fx.ej3_tsunami(), "Figura A3. Izquierda: geometría del talud. Derecha: la celeridad cae a cero en la costa y el tiempo acumulado llega a 30 min.")
h3("Idea")
P("Un tsunami tiene una longitud de onda de decenas o cientos de km, muchísimo mayor que 200 m: es una <b>onda larga</b> → está en "
  "<b>someras</b> en todo el recorrido y su celeridad solo depende de la profundidad. Como h cambia con x, la velocidad cambia y hay que <b>integrar</b>: "
  "t = ∫ dx / c(x). No vale d = c·t con una c constante.")
h3("Planteamiento")
fbox(["c(x) = √(g·h(x))          h(x) = 200 − 0,005·x          longitud del talud: h = 0 → x = 200/0,005 = 40 000 m"])
terms([("c(x)", "Celeridad de onda larga en el punto x [m/s]"), ("h(x)", "Profundidad en x [m]: 200 m al inicio, 0 en la costa"),
       ("x", "Distancia recorrida desde el borde de la plataforma [m]"), ("0,005", "Pendiente del talud (m de bajada por m de avance)")])
h3("Cálculo — tiempo de viaje")
fbox(["t = ∫₀<super>40 000</super> dx / √(g(200 − 0,005x))",
      "Cambio u = 200 − 0,005x → dx = −du/0,005:   t = (1/0,005) · ∫₀<super>200</super> du / √(g·u) = (2 / (0,005·g)) · √(g·u) |₀<super>200</super>",
      "t = (2 / (0,005·9,81)) · √(9,81·200) = 40,77 · 44,29 = <b>1806 s ≈ 30,1 min</b>"])
terms([("t", "Tiempo de viaje del tsunami desde el borde de la plataforma hasta la costa [s]"),
       ("u", "Variable auxiliar = profundidad local h [m]"),
       ("∫ du/√u = 2√u", "Primitiva usada"),
       ("√(g·200)", "Celeridad al inicio del talud = 44,3 m/s (≈ 160 km/h)")])
P("Forma general útil para cualquier talud lineal de pendiente s que empieza en h₀: <b>t = 2·√h₀ / (s·√g)</b> = 2·√200/(0,005·3,132) = 1806 s.")
fbox(["t = 2·√h₀ / (s·√g)"])
terms([("h₀", "Profundidad al inicio del talud [m]"), ("s", "Pendiente del talud [−]")])
box("<b>Resultado:</b> t ≈ 30 min → el tsunami llega a la costa hacia las <b>12:30 h</b> (coincide con el profesor).")
note("<b>Trampa:</b> con la celeridad constante de 200 m (44,3 m/s) saldrían 40 000/44,3 = 903 s = 15 min: <b>la mitad</b>. La onda se va frenando, "
     "por eso tarda el doble. Aunque en x = 40 km la celeridad es 0, la integral es finita (la primitiva √u no explota).")

# ------------------------------------------------------------------ EJ 4
story.append(PageBreak())
h2("Ejercicio 4 — Reflexión y transmisión en una barrera (onda cuasi-estacionaria)")
box("<b>Enunciado.</b> En la figura se muestran las ondas registradas en un puerto protegido por una barrera fija. Fuera (barlomar) la envolvente de la superficie libre "
    "tiene 0,3 m en los antinodos y 0,1 m en los cuasi-nodos, separados <b>4,17 m</b>. Dentro (sotamar), 0,258 m y 0,122 m, separados <b>3,65 m</b>; "
    "la profundidad dentro es <b>2,0 m</b> y fuera es 2,0 + d. Calcula el oleaje reflejado fuera del puerto y el transmitido dentro. ¿Cómo cambia la profundidad dentro del puerto?")
figure(fx.ej4_envolventes(), "Figura A4. Envolventes a cada lado de la barrera (reconstruidas con los resultados). Fuera la onda incidente se refleja parcialmente en la barrera; "
       "dentro, la transmitida se refleja en la playa.")
h3("Idea")
P("A cada lado hay una onda <b>incidente</b> que va y otra <b>reflejada</b> que vuelve con distinta altura: se superponen en una onda <b>cuasi-estacionaria</b>. "
  "Su envolvente no se anula nunca: tiene <b>antinodos</b> (máximo) y <b>cuasi-nodos</b> (mínimo). Con las alturas de la envolvente saco H<sub>i</sub> y H<sub>r</sub>; "
  "con la distancia entre antinodo y cuasi-nodo saco L; con L y la profundidad conocida (2 m) saco T, y con T y la L de fuera, la profundidad de fuera.")
h3("Planteamiento — envolvente de la onda cuasi-estacionaria")
fbox(["η = (H<sub>i</sub>/2)·cos(kx − ωt) + (H<sub>r</sub>/2)·cos(kx + ωt + ε)",
      "Antinodo:  2·η<sub>max</sub> = H<sub>i</sub> + H<sub>r</sub>          Cuasi-nodo:  2·η<sub>min</sub> = H<sub>i</sub> − H<sub>r</sub>          antinodo ↔ cuasi-nodo = L/4"])
terms([("H<sub>i</sub>", "Altura de la onda incidente [m]"), ("H<sub>r</sub>", "Altura de la onda reflejada [m]"),
       ("η<sub>max</sub>, η<sub>min</sub>", "Semiancho de la envolvente en antinodo y en cuasi-nodo [m]"),
       ("ε", "Desfase de la reflexión [rad] (no hace falta aquí)"),
       ("L/4", "Distancia entre un antinodo y el cuasi-nodo contiguo (la envolvente se repite cada L/2)"),
       ("K<sub>r</sub>", "Coeficiente de reflexión = H<sub>r</sub>/H<sub>i</sub>")])
P("Los valores de la figura (0,3; 0,1; 0,258; 0,122) son el <b>ancho total</b> de la envolvente, es decir H<sub>i</sub> ± H<sub>r</sub>.")
h3("Paso 1 — Alturas incidente y reflejada")
fbox(["<b>Fuera:</b>   H<sub>i1</sub> + H<sub>r1</sub> = 0,3   y   H<sub>i1</sub> − H<sub>r1</sub> = 0,1   →   <b>H<sub>i1</sub> = 0,20 m,  H<sub>r1</sub> = 0,10 m</b>   (K<sub>r</sub> = 0,5)",
      "<b>Dentro:</b>   H<sub>i2</sub> + H<sub>r2</sub> = 0,258   y   H<sub>i2</sub> − H<sub>r2</sub> = 0,122   →   <b>H<sub>i2</sub> = 0,19 m,  H<sub>r2</sub> = 0,068 m</b>"])
terms([("H<sub>i1</sub>, H<sub>r1</sub>", "Incidente y reflejada fuera del puerto [m]"),
       ("H<sub>i2</sub>", "Onda que avanza dentro del puerto = <b>la transmitida</b> por la barrera [m]"),
       ("H<sub>r2</sub>", "Reflejada dentro del puerto (por la playa) [m]"),
       ("K<sub>t</sub>", "Coeficiente de transmisión = H<sub>t</sub>/H<sub>i1</sub> = 0,19/0,20 = 0,95")])
P("Truco: suma y resta. H<sub>i</sub> = (ancho máx + ancho mín)/2; H<sub>r</sub> = (ancho máx − ancho mín)/2.")
h3("Paso 2 — Longitudes de onda")
fbox(["Fuera: L₁/4 = 4,17 → L₁ = 16,68 m → k₁ = 0,3767 rad/m          Dentro: L₂/4 = 3,65 → L₂ = 14,6 m → k₂ = 0,4304 rad/m"])
terms([("L₁, k₁", "Longitud y número de onda fuera del puerto"), ("L₂, k₂", "Longitud y número de onda dentro del puerto")])
h3("Paso 3 — Periodo (dentro conozco h = 2 m)")
fbox(["ω² = g·k₂·tanh(k₂h₂) = 9,81·0,4304·tanh(0,861) = 4,222·0,6966 = 2,941   →   ω = 1,715 rad/s,   <b>T = 3,66 s</b>"])
terms([("h₂", "Profundidad dentro del puerto = 2,0 m"), ("T", "Periodo: es el mismo a ambos lados de la barrera")])
h3("Paso 4 — Profundidad fuera (mismo T, k₁ conocido → sin iterar)")
fbox(["tanh(k₁h₁) = ω² / (g·k₁) = 2,941 / (9,81·0,3767) = 0,7959   →   k₁h₁ = 1,087   →   <b>h₁ = 2,89 m</b>",
      "d = h₁ − h₂ = 2,89 − 2,0 = <b>0,89 m</b>"])
terms([("h₁", "Profundidad fuera del puerto (barlomar) [m]"), ("d", "Altura del escalón del fondo bajo la barrera [m]")])
box("<b>Resultado:</b> fuera, la barrera refleja H<sub>r</sub> = <b>0,10 m</b> (K<sub>r</sub> = 0,5) de una incidente de 0,20 m; dentro entra (se transmite) "
    "H<sub>t</sub> = <b>0,19 m</b> y la playa devuelve 0,068 m. T = 3,66 s. La profundidad <b>disminuye</b> de ≈ 2,9 m fuera a 2,0 m dentro "
    "(escalón d ≈ 0,9 m): por eso la ola se acorta de 16,7 m a 14,6 m con el mismo periodo.")
note("<b>Errata del profesor:</b> en la última línea escribe 0,43 en vez de 0,377 (k de fuera) y llama «sotamar» a lo que es barlomar; aun así su resultado "
     "h = 2,85 m → d = 0,85 m es el de fuera (con k₁ sin redondear sale 2,89 m → d ≈ 0,89 m). Cualquiera de los dos vale si explicas el razonamiento.")
note("Curiosidad: K<sub>r</sub>² + K<sub>t</sub>² = 0,25 + 0,90 &gt; 1, así que los datos del enunciado no cuadran exactamente en energía (son ilustrativos). "
     "No uses la conservación de energía para «comprobar» este ejercicio.")

# ------------------------------------------------------------------ EJ 5
h2("Ejercicio 5 — Grupo de ondas bicromático sobre una plataforma eólica")
box("<b>Enunciado.</b> Durante un ensayo de una plataforma eólica marina se somete la estructura a un oleaje bicromático (grupo de ondas): "
    "H₁ = 2 m, T₁ = 5,7 s; H₂ = 2 m, T₂ = 5,4 s; h = 102 m. Calcula: onda portadora (periodo, número de onda y celeridad); onda modulante (periodo); grupo (periodo y celeridad).")
figure(fx.ej5_grupo(), "Figura A5. Suma de las dos ondas en t = 0: la portadora (azul) vive dentro de la envolvente (roja), que avanza a la mitad de velocidad.")
h3("Idea")
P("Dos ondas de periodo parecido se suman y dan una onda <b>portadora</b> (frecuencia media) multiplicada por una <b>envolvente</b> lenta (frecuencia mitad de la diferencia). "
  "Las olas individuales viajan a c; la envolvente (y la energía) viaja a c<sub>g</sub>.")
fbox(["η = H·cos(kx − ωt) · cos[ ½(Δk·x − Δω·t) ]          ω = (ω₁ + ω₂)/2,  Δω = ω₂ − ω₁,  Δk = k₂ − k₁",
      "c = ω/k          c<sub>g</sub> = Δω/Δk          T<sub>modulante</sub> = 4π/Δω          T<sub>grupo</sub> = 2π/Δω"])
terms([("ω, k", "Frecuencia y número de onda medios: los de la <b>portadora</b>"),
       ("Δω, Δk", "Diferencias de frecuencia y de número de onda entre las dos componentes"),
       ("H", "Amplitud de la portadora = 2a = H₁ = H₂ = 2 m (en el centro del grupo la ola llega a 2H = 4 m)"),
       ("c", "Celeridad de la portadora (las olas) [m/s]"),
       ("c<sub>g</sub>", "Celeridad de grupo (la envolvente y la energía) [m/s]"),
       ("T<sub>modulante</sub>", "Periodo de la función cos[½(…)]: 2π/(Δω/2) = 4π/Δω"),
       ("T<sub>grupo</sub>", "Tiempo entre dos grupos consecutivos: la envolvente |cos| se repite el doble de rápido")])
h3("Paso 1 — Frecuencias")
fbox(["ω₁ = 2π/5,7 = 1,1023 rad/s     ω₂ = 2π/5,4 = 1,1636 rad/s     ω = 1,1329 rad/s     Δω = 0,06124 rad/s"])
terms([("ω₁, ω₂", "Frecuencias angulares de cada componente [rad/s]")])
h3("Paso 2 — Portadora")
P("Con h = 102 m: k·h ≈ 13 ≫ π → <b>indefinidas</b> (tanh = 1), así que la dispersión es directa: k = ω²/g.")
fbox(["T = 2π/ω = <b>5,55 s</b>      k = ω²/g = 1,1329²/9,81 = <b>0,1308 rad/m</b> (L = 48,0 m)      c = ω/k = <b>8,66 m/s</b>"])
terms([("k = ω²/g", "Dispersión en indefinidas (tanh kh = 1)"), ("L", "Longitud de la portadora = 2π/k [m]")])
h3("Paso 3 — Modulante y grupo")
fbox(["k₁ = ω₁²/g = 0,12386 (L₁ = 50,73 m)     k₂ = ω₂²/g = 0,13801 (L₂ = 45,53 m)     Δk = 0,01414 rad/m",
      "T<sub>modulante</sub> = 4π/Δω = <b>205,2 s</b>      T<sub>grupo</sub> = 2π/Δω = <b>102,6 s</b>      c<sub>g</sub> = Δω/Δk = 0,06124/0,01414 = <b>4,33 m/s</b>"])
terms([("k₁, k₂", "Números de onda de cada componente (cada uno con su dispersión)"), ("L₁, L₂", "Longitudes de onda de cada componente [m]")])
P("Comprobación teórica: en indefinidas c<sub>g</sub> = c/2 = 8,66/2 = 4,33 m/s ✓. Atajo para T<sub>grupo</sub>: T₁T₂/(T₁ − T₂) = 5,7·5,4/0,3 = 102,6 s ✓.")
box("<b>Resultado:</b> portadora T = 5,55 s, k = 0,131 rad/m, c = 8,66 m/s · modulante T = 205 s · grupo T<sub>g</sub> = 103 s, c<sub>g</sub> = 4,33 m/s.")
note("El profesor da k = 0,13112 y c = 8,64 m/s (pequeño error de redondeo) y escribe «tanh k·202» por «tanh k·102»; no cambia nada porque tanh = 1. "
     "<b>Trampa típica:</b> confundir T<sub>modulante</sub> (4π/Δω) con T<sub>grupo</sub> (2π/Δω). Si te piden «el periodo del grupo», es 2π/Δω; "
     "es el periodo con el que la estructura nota la llegada de olas grandes (deriva lenta).")

# ------------------------------------------------------------------ Ejemplo diapo 82
h2("Ejemplo de clase (diapo 82) — Sentido físico de la dispersión")
box("<b>Enunciado.</b> Calcular k, L y c para trenes de ondas de 2, 6, 12, 18 (y 24) s propagándose en h = 10 m.")
P("Aquí se conocen T y h, así que <b>sí hay que iterar</b> (SOLVE: ω² − g·X·tanh(10X) = 0, arrancando con X = ω²/g).")
fbox(["ω² = g·k·tanh(k·10)   →   k   →   L = 2π/k,   c = L/T"])
terms([("X", "Incógnita k en la calculadora"), ("10", "Profundidad h = 10 m")])
table(["T (s)", "k (rad/m)", "L (m)", "c (m/s)", "h/L", "Zona"], [
    ["2", "1,006", "6,25", "3,12", "1,60", "Indefinidas (c = c₀)"],
    ["6", "0,130", "48,4", "8,07", "0,21", "Intermedias"],
    ["12", "0,0555", "113,3", "9,44", "0,088", "Intermedias"],
    ["18", "0,0360", "174,6", "9,70", "0,057", "Intermedias (casi someras)"],
    ["24", "0,0267", "234,9", "9,79", "0,043", "Someras: c → √(gh) = 9,90"],
], [18, 25, 22, 22, 20, 63])
figure(fx.ej_dispersion_h10(), "Figura A6. A igual profundidad, más periodo → más celeridad, pero sin pasar nunca de √(gh).")
P("<b>Lectura física (pregunta de teoría):</b> a igual h, las olas de mayor periodo son más largas y más rápidas → un temporal lejano llega ordenado por periodos "
  "(primero los largos): eso es la <b>dispersión frecuencial</b>. Al bajar la profundidad todas se frenan hasta √(gh) y dejan de ser dispersivas.")

# =========================================================================================== B
story.append(PageBreak())
P("PARTE B · Análisis estadístico del oleaje", H1)
P("Los ejemplos resueltos de la presentación <i>Análisis del oleaje 1de3 – Estadístico</i>. En los dos exámenes anteriores ha caído un ejercicio de "
  "<b>Rayleigh + H<sub>max</sub></b> (2 puntos): domina estos tres.", SUB)

# ------------------------------------------------------------------ paso por cero
h2("Ejercicio B1 — Análisis de paso por cero de un registro de 22 olas (diapos 22–25)")
box("<b>Enunciado.</b> Realizar el análisis de paso por cero al registro de la superficie libre y evaluar el registro de olas. El análisis por pasos ascendentes da 22 olas "
    "(H<sub>i</sub>, T<sub>i</sub>): (0,09; 3,32) (0,15; 2,38) (0,19; 2,55) (0,42; 3,45) (1,03; 5,00) (0,61; 4,38) (0,44; 4,46) (0,68; 4,11) (0,50; 6,23) (1,09; 5,31) "
    "(1,20; 6,00) (1,09; 5,81) (0,56; 5,63) (0,06; 2,01) (0,05; 1,22) (0,97; 4,63) (0,71; 5,55) (0,28; 2,82) (0,99; 5,06) (0,88; 4,59) (0,13; 2,93) (0,62; 4,09). "
    "Calcula H<sub>max</sub>, T<sub>max</sub>, H<sub>1/3</sub>, T<sub>1/3</sub>, H<sub>m</sub>, T<sub>m</sub> y H<sub>rms</sub>.")
h3("Idea")
P("Cada ola va de un paso <b>ascendente</b> por cero al siguiente: su altura H es la distancia vertical máxima (cresta − seno) entre ellos y su periodo T el tiempo entre ellos. "
  "Con la lista de olas se calculan los estadísticos. <b>Para H<sub>1/3</sub> y T<sub>1/3</sub> se ordenan las olas por altura</b> (no por periodo).")
figure(fx.pasocero_barras(), "Figura B1. Las 22 olas del registro; en rojo, las 7 más altas (el tercio superior).")
fbox(["H<sub>1/n</sub> = (1/(N/n)) · Σ<sub>i=1</sub><super>N/n</super> H<sub>i</sub>  (olas ordenadas de mayor a menor H)          H<sub>m</sub> = (1/N)·Σ H<sub>i</sub>          H<sub>rms</sub> = √[(1/N)·Σ H<sub>i</sub>²]"])
terms([("N", "Número de olas del registro = 22"), ("n", "Fracción: n = 3 → tercio de olas más altas (N/3 = 7,3 → 7 olas)"),
       ("H<sub>1/3</sub>", "Altura significante: media del tercio de olas más altas [m]"), ("T<sub>1/3</sub>", "Media de los periodos <b>de esas mismas</b> olas [s]"),
       ("H<sub>m</sub>, T<sub>m</sub>", "Altura media y periodo medio de todas las olas"), ("H<sub>rms</sub>", "Altura cuadrática media (parámetro de Rayleigh) [m]")])
h3("Cálculo")
P("Ordenadas por altura, las 7 mayores son: 1,20 (6,00 s) · 1,09 (5,31 s) · 1,09 (5,81 s) · 1,03 (5,00 s) · 0,99 (5,06 s) · 0,97 (4,63 s) · 0,88 (4,59 s).")
table(["Estadístico", "Cálculo", "Resultado"], [
    ["H<sub>max</sub>, T<sub>max</sub>", "La ola más alta y su periodo", "<b>1,20 m · 6,00 s</b>"],
    ["H<sub>1/3</sub>", "(1,20 + 1,09 + 1,09 + 1,03 + 0,99 + 0,97 + 0,88)/7 = 7,25/7", "<b>1,04 m</b>"],
    ["T<sub>1/3</sub>", "(6,00 + 5,31 + 5,81 + 5,00 + 5,06 + 4,63 + 4,59)/7 = 36,40/7", "<b>5,20 s</b>"],
    ["H<sub>m</sub>", "Σ H<sub>i</sub>/22 = 12,74/22", "<b>0,58 m</b>"],
    ["T<sub>m</sub>", "Σ T<sub>i</sub>/22 = 91,53/22", "<b>4,16 s</b>"],
    ["H<sub>rms</sub>", "√(Σ H<sub>i</sub>²/22) = √(10,40/22)", "<b>0,69 m</b>"],
], [30, 100, 40])
P("Comprobación con Rayleigh: H<sub>1/3</sub> ≈ 1,416·H<sub>rms</sub> = 0,97 m y H<sub>m</sub> ≈ 0,886·H<sub>rms</sub> = 0,61 m: del orden de lo medido (con 22 olas la estadística es pobre; "
  "se recomiendan ≥ 100 olas, mejor 1000).")
note("<b>Discrepancias con la diapo:</b> la diapo da T<sub>1/3</sub> = 5,65 s y T<sub>max</sub> = 6,23 s porque toma los periodos <b>mayores</b>; según su propia definición (diapo 24) "
     "son los periodos <b>de las olas más altas</b> → 5,20 s y 6,00 s. En el examen escribe la definición que usas y no habrá duda.")

# ------------------------------------------------------------------ Rayleigh
h2("Ejercicio B2 — Altura superada por el 2 % de las olas (diapos 35–37)")
box("<b>Enunciado.</b> Calcular la altura de ola que es superada solo por el 2 % de las mayores olas de un estado de mar de H<sub>rms</sub> = 3 m.")
h3("Idea")
P("Las alturas de ola en banda estrecha siguen la <b>distribución de Rayleigh</b>, que depende solo de H<sub>rms</sub>. La probabilidad de que una ola supere H* "
  "(<b>excedencia</b>) es una exponencial: se despeja H*.")
fbox(["F(H) = 1 − exp[−(H/H<sub>rms</sub>)²]          q = P(H &gt; H<sub>q</sub>) = exp[−(H<sub>q</sub>/H<sub>rms</sub>)²]          <b>H<sub>q</sub> = H<sub>rms</sub>·√(−ln q)</b>"])
terms([("F(H)", "Función de distribución: probabilidad de que una ola tenga altura ≤ H"),
       ("q", "Probabilidad de excedencia (fracción de olas más altas que H<sub>q</sub>) = 0,02"),
       ("H<sub>q</sub>", "Altura superada solo por la fracción q de las olas [m]"),
       ("H<sub>rms</sub>", "Altura cuadrática media = 3 m"), ("ln", "Logaritmo neperiano (ln 0,02 = −3,912)")])
fbox(["H<sub>2%</sub> = 3 · √(−ln 0,02) = 3 · √3,912 = 3 · 1,978 = <b>5,93 m</b>"])
terms([("H<sub>2%</sub>", "Altura superada por el 2 % de las olas [m]")])
figure(fx.rayleigh_exced(), "Figura B2. Curva de excedencia de Rayleigh (escala logarítmica): se entra con q = 0,02 y se lee H.")
box("<b>Resultado:</b> H<sub>2%</sub> = 1,978·H<sub>rms</sub> = <b>5,93 m</b>.")
note("<b>Variante de examen (parcial 29-10-2025):</b> te dan H y piden q → q = exp[−(H/H<sub>rms</sub>)²]. Si te dan H<sub>s</sub> en vez de H<sub>rms</sub>: "
     "H<sub>rms</sub> = H<sub>s</sub>/1,416 ≈ H<sub>s</sub>/√2. Y si piden la probabilidad de que la <b>cresta</b> supere una cota Z, la ola crítica es H = 2Z.")

# ------------------------------------------------------------------ Hmax
h2("Ejercicio B3 — Altura de ola máxima en un estado de mar (diapos 42–43)")
box("<b>Enunciado.</b> Calcula la altura de ola máxima más probable para un estado de mar de una hora de duración (3600 s), H<sub>rms</sub> = 5 m (la solución usa 3 m) "
    "y periodo medio 7,2 s.")
h3("Idea")
P("Cuantas más olas tiene el temporal, más probable es encontrar una muy grande. Si las olas son independientes y siguen Rayleigh, la ola máxima de N olas tiene una "
  "distribución conocida (Longuet-Higgins) cuya <b>moda</b> (valor más probable) y <b>media</b> tienen fórmula cerrada para N &gt; 100.")
h3("Paso 1 — Número de olas")
fbox(["N = duración / T<sub>m</sub> = 3600 / 7,2 = <b>500 olas</b>          ln 500 = 6,215"])
terms([("N", "Número de olas del estado de mar"), ("T<sub>m</sub>", "Periodo medio = 7,2 s"), ("duración", "1 h = 3600 s")])
h3("Paso 2 — Ola máxima")
fbox(["<b>Moda (más probable):</b>  H<sub>max</sub>/H<sub>rms</sub> = √(ln N) = √6,215 = <b>2,493</b>",
      "<b>Media:</b>  H<sub>max</sub>/H<sub>rms</sub> = √(ln N) + (C/2)·(ln N)<super>−1/2</super> = 2,493 + 0,2886/2,493 = <b>2,609</b>"])
terms([("H<sub>max</sub>", "Altura de la ola máxima de las N olas [m]"), ("C", "Constante de Euler = 0,57722"),
       ("(ln N)<super>−1/2</super>", "1/√(ln N)"), ("H<sub>rms</sub>", "Altura cuadrática media [m]")])
table(["H<sub>rms</sub>", "Moda (más probable)", "Media"], [
    ["5 m (enunciado)", "2,493·5 = <b>12,46 m</b>", "2,609·5 = 13,04 m"],
    ["3 m (solución de la diapo)", "2,493·3 = <b>7,48 m</b>", "2,609·3 = 7,83 m ← resultado de la diapo"],
], [50, 60, 60])
box("<b>Resultado:</b> N = 500 olas; H<sub>max</sub> más probable = 2,49·H<sub>rms</sub> (12,5 m con H<sub>rms</sub> = 5 m; 7,5 m con 3 m). La media es 2,61·H<sub>rms</sub>.")
note("<b>Dos erratas en la diapo:</b> (1) el enunciado dice H<sub>rms</sub> = 5 y la solución usa 3 m; (2) pide la <b>más probable</b> (moda) y calcula la <b>media</b>. "
     "En los exámenes el profesor ha usado la <b>media</b> (con C). Si dudas, da las dos y di cuál es cada una.")
P("<b>Encadenado típico de examen:</b> H<sub>s</sub> → H<sub>rms</sub> = H<sub>s</sub>/√2 → N = duración/T<sub>m</sub> → H<sub>max</sub> → cresta = H<sub>max</sub>/2 → cota de la cubierta, "
  "o runup = η<sub>max</sub> + u²/2g. Mira el anexo.")

# =========================================================================================== C
story.append(PageBreak())
P("PARTE C · Análisis espectral del oleaje", H1)
P("Los ejercicios de la presentación <i>Análisis del oleaje 2de3 – Espectral</i> (diapos 75–80). En los dos exámenes ha caído un espectral de 2 puntos.", SUB)
P("Ideas clave antes de empezar:")
fbox(["m<sub>n</sub> = ∫₀<super>∞</super> ω<super>n</super>·S(ω) dω        m₀ = área = η<sub>rms</sub>²        H<sub>m0</sub> = 4√m₀        E = ρg·m₀"])
terms([("S(ω)", "Densidad espectral: cómo se reparte la varianza (energía) entre frecuencias [m²·s/rad]"),
       ("m<sub>n</sub>", "Momento espectral de orden n"), ("m₀", "Área bajo el espectro = varianza de la superficie libre [m²]"),
       ("η<sub>rms</sub>", "Desviación típica de la superficie libre [m]"),
       ("H<sub>m0</sub>", "Altura significante espectral [m]"), ("E", "Energía media por unidad de superficie [J/m²]")])

# ------------------------------------------------------------------ espectral 1
h2("Ejercicio C1 — H<sub>m0</sub> de un registro de 5 componentes (diapos 75–76)")
box("<b>Enunciado.</b> Un registro de la superficie libre se ha obtenido superponiendo cinco componentes sinusoidales: "
    "H = 0,91 m (T = 3,76 s); 1,83 m (5,04 s); 2,17 m (6,63 s); 4,18 m (8,69 s); 2,38 m (13,03 s). Determinar H<sub>m0</sub>.")
h3("Idea (teorema de Parseval)")
P("Cada componente aporta a la varianza de η su propia varianza, a<sub>i</sub>²/2 = H<sub>i</sub>²/8, <b>independientemente de las demás</b>. "
  "Se suman <b>energías (H²)</b>, nunca alturas. El periodo no interviene en m₀.")
fbox(["m₀ = Σ a<sub>i</sub>²/2 = Σ H<sub>i</sub>²/8 = Σ E<sub>i</sub>/(ρg)          H<sub>m0</sub> = 4√m₀"])
terms([("a<sub>i</sub>", "Amplitud de la componente i = H<sub>i</sub>/2 [m]"), ("H<sub>i</sub>²/8", "Varianza de una sinusoide de altura H<sub>i</sub> [m²]"),
       ("E<sub>i</sub>/(ρg)", "Energía de la componente dividida por ρg: es la misma H<sub>i</sub>²/8 [m²]")])
table(["Comp.", "H (m)", "T (s)", "H²/8 = E/ρg (m²)"], [
    ["1", "0,91", "3,76", "0,10"], ["2", "1,83", "5,04", "0,42"], ["3", "2,17", "6,63", "0,59"],
    ["4", "4,18", "8,69", "2,18"], ["5", "2,38", "13,03", "0,71"], ["<b>Σ</b>", "", "", "<b>4,00</b>"]], [25, 40, 40, 65])
fbox(["H<sub>m0</sub> = 4·√4,00 = 4·2,00 = <b>8,00 m</b>"])
terms([("√4,00", "η<sub>rms</sub> = 2,00 m")])
figure(fx.esp_componentes(), "Figura C1. Las 5 componentes como «espectro de líneas»: la componente de 8,69 s aporta más de la mitad de la energía.")
box("<b>Resultado:</b> m₀ = 4,00 m² → <b>H<sub>m0</sub> = 8,00 m</b>.")
note("<b>Trampas:</b> sumar alturas (0,91 + … + 2,38 = 11,47 m) está mal; H<sub>m0</sub> = √2·√(Σ H<sub>i</sub>²) = 8,0 m. Para una sola onda regular de altura H, H<sub>m0</sub> = 1,41·H.")

# ------------------------------------------------------------------ espectral 2 polar
h2("Ejercicio C2 — SEA o SWELL en un espectro direccional (diapo 77)")
box("<b>Enunciado.</b> En el espectro direccional de la figura (FPSO Norne, 01/01/1990) indica cuál de los dos picos corresponde al SEA y cuál al SWELL, explica "
    "las razones y determina el periodo de pico y la dirección de pico de ambas componentes. (Anillos de periodo: 6, 7, 9, 11 y 35 s; el periodo crece hacia el centro.)")
figure(fx.esp_polar(), "Figura C2. Esquema del espectro de la diapo 77: radio ∝ frecuencia (periodos largos en el centro); el ángulo es la dirección.")
h3("Cómo se lee")
bl("El <b>ángulo</b> da la dirección (N arriba, E a la derecha). La <b>distancia al centro</b> es la frecuencia: cerca del centro, periodos largos; fuera, cortos.",
   "El periodo de pico es el del punto más oscuro (más energía) de cada mancha, interpolando entre anillos; la dirección de pico, su ángulo.")
fbox(["T<sub>p</sub> = 1/f<sub>p</sub> = 2π/ω<sub>p</sub>          θ<sub>p</sub> = dirección del máximo de S(ω, θ)"])
terms([("T<sub>p</sub>", "Periodo de pico: el del máximo del espectro [s]"), ("f<sub>p</sub>, ω<sub>p</sub>", "Frecuencia de pico [Hz] y [rad/s]"),
       ("θ<sub>p</sub>", "Dirección de pico [°]"), ("S(ω, θ)", "Espectro direccional: energía por frecuencia y dirección")])
table(["", "Pico al SSE (grande)", "Pico al W (pequeño)"], [
    ["Posición", "Entre los anillos de 7 y 9 s, ≈ 150°", "Dentro del anillo de 11 s, ≈ 255–260°"],
    ["T<sub>p</sub> (lectura)", "<b>≈ 8 s</b>", "<b>≈ 13–14 s</b>"],
    ["Forma", "Ancho en dirección y en frecuencia, más energía", "Estrecho y compacto"],
    ["<b>Es…</b>", "<b>SEA</b> (oleaje de viento local)", "<b>SWELL</b> (mar de fondo)"],
], [32, 69, 69])
h3("Por qué")
bl("<b>SEA</b>: se está generando por el viento local → periodos <b>cortos</b>, energía repartida en un rango <b>ancho</b> de frecuencias y de direcciones "
   "(espectro tipo JONSWAP joven), y normalmente es el pico más energético.",
   "<b>SWELL</b>: se generó lejos y ha viajado; por dispersión llegan primero y separadas las olas largas → periodos <b>largos</b>, banda <b>estrecha</b> "
   "en frecuencia y en dirección (las componentes cortas se han disipado o quedado atrás).",
   "Las dos direcciones son distintas (≈ 105° de diferencia): no comparten generación → <b>espectro bimodal</b> (mar mixto). H<sub>m0</sub> total = √(H<sub>sea</sub>² + H<sub>swell</sub>²).")
note("Los valores son <b>lecturas aproximadas</b> de la figura (± 1 s y ± 10°); el profesor no da solución. Las direcciones se dan como ángulo náutico del pico en el gráfico; "
     "si en clase se dijo que el gráfico indica «de dónde viene» o «hacia dónde va», úsalo así y dilo en el examen.")

# ------------------------------------------------------------------ espectral 2 S(w)
h2("Ejercicio C3 — Parámetros de un espectro definido por tramos (diapos 78–80)")
box("<b>Enunciado.</b> Espectro unidimensional local: S(ω) = 2ω para 0 &lt; ω &lt; 0,8; S(ω) = 8/3 − 4ω/3 para 0,8 &lt; ω &lt; 2 (unidades habituales). Calcula: "
    "a) altura de momento de orden cero; b) densidad de energía; c) periodo de pico; d) periodo medio; e) periodo medio de cortes por cero; "
    "f) periodo medio entre crestas; g) parámetro ε de anchura de banda.")
figure(fx.esp_triangulo(), "Figura C3. El espectro es un triángulo: sube hasta ω = 0,8 (S = 1,6) y baja hasta ω = 2.")
h3("Idea")
P("Todo sale de los <b>momentos</b> m₀, m₁, m₂ y m₄: integrales de ω<super>n</super>·S(ω) por tramos. m₀ además es el <b>área del triángulo</b> (½·base·altura = ½·2·1,6 = 1,6): "
  "úsalo para comprobar.")
fbox(["m<sub>n</sub> = ∫₀<super>0,8</super> 2ω·ω<super>n</super> dω + ∫<sub>0,8</sub><super>2</super> (8/3 − 4ω/3)·ω<super>n</super> dω",
      "m<sub>n</sub> = 2·0,8<super>n+2</super>/(n+2) + (8/3)·(2<super>n+1</super> − 0,8<super>n+1</super>)/(n+1) − (4/3)·(2<super>n+2</super> − 0,8<super>n+2</super>)/(n+2)"])
terms([("m<sub>n</sub>", "Momento de orden n [m²·(rad/s)<super>n</super>]"), ("0,8 y 2", "Límites de los tramos [rad/s]"),
       ("∫ω<super>n+1</super>dω", "= ω<super>n+2</super>/(n+2)")])
table(["n", "Sustitución", "m<sub>n</sub>"], [
    ["0", "0,64 + 3,20 − 2,24", "<b>1,600 m²</b>"],
    ["1", "0,3413 + 4,4800 − 3,3280", "<b>1,493 m²·rad/s</b>"],
    ["2", "0,2048 + 6,6560 − 5,1968", "<b>1,664 m²·rad²/s²</b>"],
    ["4", "0,0874 + 16,8919 − 14,1640", "<b>2,815 m²·rad⁴/s⁴</b>"],
], [15, 95, 60])
h3("Resultados")
fbox(["a) H<sub>m0</sub> = 4√m₀ = 4√1,6 = <b>5,06 m</b>          b) E = ρg·m₀ = 1025·9,81·1,6 = <b>16 088 J/m²</b>",
      "c) T<sub>p</sub> = 2π/ω<sub>p</sub> = 2π/0,8 = <b>7,85 s</b>          d) T<sub>01</sub> = 2π·m₀/m₁ = 2π·1,6/1,493 = <b>6,73 s</b>",
      "e) T<sub>z</sub> = T<sub>02</sub> = 2π·√(m₀/m₂) = 2π·√(1,6/1,664) = <b>6,16 s</b>",
      "f) T<sub>c</sub> = T<sub>24</sub> = 2π·√(m₂/m₄) = 2π·√(1,664/2,815) = <b>4,83 s</b>",
      "g) ε = √[1 − m₂²/(m₀·m₄)] = √[1 − 1,664²/(1,6·2,815)] = <b>0,62</b>"])
terms([("H<sub>m0</sub>", "Altura de momento de orden cero [m]"), ("E", "Densidad (media) de energía [J/m²]"),
       ("ω<sub>p</sub>", "Frecuencia del máximo de S(ω) = 0,8 rad/s"), ("T<sub>p</sub>", "Periodo de pico o modal [s]"),
       ("T<sub>01</sub>", "Periodo medio (centro de gravedad del espectro) [s]"), ("T<sub>z</sub>", "Periodo medio de pasos por cero [s]"),
       ("T<sub>c</sub>", "Periodo medio entre crestas (máximos) [s]"), ("ε", "Anchura espectral: 0 banda estrecha, 1 banda ancha"),
       ("2π", "Aparece porque S está en ω (rad/s); si estuviera en f (Hz) no se pone")])
box("<b>Resultado:</b> H<sub>m0</sub> = 5,06 m · E = 16 088 J/m² · T<sub>p</sub> = 7,85 s · T<sub>01</sub> = 6,73 s · T<sub>z</sub> = 6,16 s · T<sub>c</sub> = 4,83 s · ε = 0,62 "
    "(banda bastante ancha → Rayleigh solo aproximado). Orden lógico: T<sub>c</sub> &lt; T<sub>z</sub> &lt; T<sub>01</sub> &lt; T<sub>p</sub> ✓.")
note("<b>Errata de la diapo 80:</b> da T<sub>24</sub> = 4,23 s porque eleva (m₂/m₄) a 3/4; con la fórmula general de su diapo 30, T<sub>ij</sub> = 2π·(m<sub>i</sub>/m<sub>j</sub>)<super>1/(j−i)</super>, "
     "el exponente es 1/2 → <b>4,83 s</b>. Escribe la fórmula en el examen para que se vea de dónde sale. El resto coincide con el profesor.")
note("<b>Trampa del 2π:</b> con S(ω) los periodos llevan 2π (T<sub>01</sub> = 2π·m₀/m₁); con S(f) no (T<sub>01</sub> = m₀/m₁). Si te sale un periodo 6 veces mayor de lo razonable, sobra un 2π.")

# =========================================================================================== D
story.append(PageBreak())
P("PARTE D · Introducción (propiedades del agua de mar)", H1)
P("El único ejercicio del Bloque 1 (diapos 53–54). En clase se pide como programa de Matlab; aquí va resuelto a mano y con la ecuación de estado UNESCO para que entiendas el razonamiento.", SUB)
h2("Ejercicio D1 — Lastre de una esfera de titanio en Menorca")
box("<b>Enunciado.</b> Sumergiremos cerca de la costa de Menorca una cápsula esférica de titanio (4507 kg/m³) de <b>2 m de diámetro</b> y <b>50 mm de espesor</b>. Calcular: "
    "1) el lastre inicial para que la esfera esté totalmente sumergida bajo la superficie del mar; 2) la variación de lastre necesaria para hacerla descender hasta 450 m. "
    "Datos (diapo 54): presión 0 / 50 / 100 / … / 400 / &gt; 450 dbar; temperatura potencial 24,5 / 23,5 / 22,5 / 21,8 / 21,0 / 20,0 / 19,0 / 18,2 / 17,4 / 16,0 °C; "
    "salinidad 37,8 / 37,7 / 37,6 / 37,5 / 37,4 / 37,3 / 37,2 / 36,9 / 36,7 / 36,5 g/kg.")
h3("Idea")
P("Para que la esfera quede sumergida y en equilibrio (flotabilidad neutra), su peso total (casco + lastre) debe igualar el empuje: ρ<sub>agua</sub>·V·g. "
  "Al bajar, el agua es <b>más fría y está más comprimida</b> → más densa → más empuje → hace falta <b>más lastre</b> para seguir bajando. "
  "Por eso importa la ecuación de estado ρ(S, T, p).")
h3("Paso 1 — Volumen y masa del casco")
fbox(["V = (4/3)·π·R³ = (4/3)·π·1³ = 4,189 m³          V<sub>int</sub> = (4/3)·π·0,95³ = 3,591 m³",
      "m<sub>casco</sub> = ρ<sub>Ti</sub>·(V − V<sub>int</sub>) = 4507 · 0,5974 = <b>2692,6 kg</b>"])
terms([("V", "Volumen exterior (desplazado) [m³]"), ("R", "Radio exterior = 1 m"), ("V<sub>int</sub>", "Volumen hueco interior, radio 1 − 0,05 = 0,95 m"),
       ("ρ<sub>Ti</sub>", "Densidad del titanio = 4507 kg/m³"), ("m<sub>casco</sub>", "Masa de la esfera vacía [kg]")])
h3("Paso 2 — Densidad del agua con la ecuación de estado (UNESCO)")
fbox(["ρ(S, T, p) = ρ(S, T, 0) / [1 − p / K(S, T, p)]          σ = ρ − 1000"])
terms([("ρ(S,T,0)", "Densidad a presión atmosférica (polinomio en S y T) [kg/m³]"), ("K(S,T,p)", "Módulo de compresibilidad secante [bar]"),
       ("p", "Presión [bar]; 1 dbar ≈ 1 m de profundidad, 450 dbar = 45 bar"), ("S", "Salinidad [g/kg ≈ PSU]"), ("T", "Temperatura [°C]"),
       ("σ", "Anomalía de densidad [kg/m³]")])
table(["Punto", "S (g/kg)", "T (°C)", "p (bar)", "ρ (kg/m³)", "σ"], [
    ["Superficie", "37,8", "24,5", "0", "<b>1025,61</b>", "25,6"],
    ["450 m", "36,5", "16,0", "45", "<b>1028,88</b> (1026,90 a p = 0; K = 23 419 bar)", "28,9"],
], [24, 20, 18, 18, 70, 20])
figure(fx.esfera_perfil(), "Figura D1. Perfil de T, S y densidad: el agua se hace más densa con la profundidad (por frío y por presión).")
h3("Paso 3 — Lastres")
fbox(["Equilibrio:  (m<sub>casco</sub> + m<sub>lastre</sub>)·g = ρ<sub>agua</sub>·V·g   →   m<sub>lastre</sub> = ρ<sub>agua</sub>·V − m<sub>casco</sub>",
      "1)  m<sub>lastre,0</sub> = 1025,61 · 4,189 − 2692,6 = <b>1603 kg</b>",
      "2)  m<sub>lastre,450</sub> = 1028,88 · 4,189 − 2692,6 = 1617 kg   →   <b>Δm ≈ +14 kg</b>"])
terms([("m<sub>lastre</sub>", "Masa de lastre dentro de la esfera para flotabilidad neutra [kg]"), ("ρ<sub>agua</sub>·V", "Masa de agua desplazada (empuje/g) [kg]"),
       ("Δm", "Lastre adicional para seguir descendiendo hasta 450 m [kg]")])
box("<b>Resultado:</b> lastre inicial ≈ <b>1603 kg</b>; para llegar a 450 m hace falta añadir ≈ <b>14 kg</b> más (la densidad sube 3,3 kg/m³ y V = 4,19 m³).")
note("<b>Hipótesis</b> (dilas si te lo preguntan): el lastre va dentro de la esfera (no añade volumen); la esfera no se comprime (titanio: ΔV/V ≈ 4·10⁻⁵ a 45 bar, ≈ 0,2 kg, despreciable); "
     "la temperatura potencial de la tabla se toma como temperatura in situ (difieren 0,07 °C a 450 m: ρ cambia 0,02 kg/m³). Con TEOS-10 (gsw) salen 1025,48 y 1028,73 kg/m³: mismo Δm.")

# ------------------------------------------------------------------ cierre
h2("Anexo — Exámenes anteriores resueltos")
P("A continuación se adjuntan, tal cual están en <i>examenes/</i>, los exámenes anteriores resueltos paso a paso: "
  "<b>1er Parcial 29-10-2025</b> (rebase + Rayleigh, sensores de presión, SEA/SWELL con conos), <b>Final ordinario 13-01-2025</b> "
  "(L₀ → T y L → h, runup con H<sub>max</sub> y u orbital, S(ω) por tramos) y la parte del 1er parcial del <b>2º Parcial 13-01-2026</b> "
  "(régimen extremal frente a medio, oleaje en indefinidas, dispersión en h = 20 m y asomeramiento). Sus páginas conservan su propia numeración.")
box("<b>Orden recomendado hoy (domingo) y el martes:</b> B3 y B2 → examen 29-10-2025 ej. 1 → C3 → examen 13-01-2025 ej. 3 → A1 → examen 13-01-2025 ej. 1. "
    "Si te sobra tiempo: A2, A5, A4, A3, C1, C2. D1 solo si ya lo tienes todo.")

out = sys.argv[1] if len(sys.argv) > 1 else "ejercicios_resueltos.pdf"
build(out, "Oceanografía · Ejercicios resueltos del 1er parcial · Carlos Sánchez Campos", "Oceanografía — Ejercicios resueltos del 1er parcial")
