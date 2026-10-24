import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "resumenes")); sys.path.insert(0, HERE)
from estilo import *
import figuras_examenes as fx

P("Oceanografía · 1er Examen Parcial", H1)
P("29 de octubre de 2025 · Curso 2025-26 · ETSIN-UPM · Parte de EJERCICIOS (3 ejercicios × 2 puntos) · enunciados transcritos y resolución paso a paso", SUB)

note("<b>Cómo usar este PDF:</b> lee el enunciado, tapa la resolución y hazlo tú con calculadora (máx. 20 min por ejercicio). "
     "Después corrige con la resolución. Los resultados se han recalculado; donde la solución del profesor redondea distinto se indica en ámbar.")

table(["Ej.", "Tema", "Qué tienes que saber", "Pts"], [
    ["1", "Análisis estadístico: Rayleigh y H<sub>max</sub>", "q = exp[−(H/H<sub>rms</sub>)²], H<sub>s</sub> = √2·H<sub>rms</sub>, N = duración/T<sub>m</sub>, ⟨H<sub>max,N</sub>⟩ (con la constante de Euler), cresta = H/2", "2"],
    ["2", "Teoría lineal: presión dinámica + dispersión", "p<sub>din</sub> = ρga·cosh k(h+z)/cosh kh, cociente p₁/p₂ → k, dispersión → h, p₁ → H", "2"],
    ["3", "Análisis espectral: SEA/SWELL", "m₀ = volumen del cono = ⅓·A<sub>b</sub>·S<sub>p</sub>, H<sub>m0</sub> = 4√m₀, E = ρgm₀, T<sub>p</sub> = 2π/ω<sub>p</sub>; se suman los m₀", "2"],
], [10, 45, 105, 10])

# ------------------------------------------------------------------ EJ 1
h2("Ejercicio 1 — Rebase de la cubierta de servicio (2 puntos)")
box("<b>Enunciado.</b> En un emplazamiento del Mar del Norte que diseñó una estructura offshore para eólica marina definió la cota de una "
    "cubierta de servicio a sentimiento (Z<sub>cubierta</sub> = 5 m). Sabiendo que el oleaje de diseño de acuerdo con el anejo meteo-oceánico es "
    "H<sub>s</sub> = 9,5 m y T<sub>m</sub> = 12 s, para un temporal de duración 3 horas:<br/>"
    "a) ¿Calcular la probabilidad de que tengan lugar fenómenos de rebase (i.e. que el oleaje supere la cota de la cubierta de servicio) durante el estado de mar de diseño?<br/>"
    "b) ¿A qué cota debería estar la cubierta de servicio para que no se produjesen fenómenos de rebase?<br/>"
    "<i>Hipótesis:</i> la estructura es lo suficientemente transparente como para que no modifique el patrón de propagación del oleaje; "
    "el oleaje incidente sigue una distribución Rayleigh.")

h3("a) Probabilidad de rebase")
P("<b>Idea:</b> hay rebase cuando la <b>cresta</b> de una ola llega a la cubierta. Con cresta y seno simétricos la cresta es H/2, "
  "así que la ola crítica es la que tiene H<sub>q</sub> = 2·Z<sub>cubierta</sub>.")
fbox(["H<sub>q</sub> = 2 · Z<sub>cubierta</sub> = 2 · 5 = 10 m"])
terms([("H<sub>q</sub>", "Altura de ola cuya cresta alcanza justo la cubierta [m]"),
       ("Z<sub>cubierta</sub>", "Cota de la cubierta sobre el nivel medio del mar [m]")])
P("Relación de Rayleigh entre la altura significante y la cuadrática media:")
fbox(["H<sub>s</sub> = √2 · H<sub>rms</sub>   →   H<sub>rms</sub> = 9,5 / √2 = 6,72 m"])
terms([("H<sub>s</sub>", "Altura de ola significante (≈ H<sub>1/3</sub>, media del tercio de olas más altas) [m]"),
       ("H<sub>rms</sub>", "Altura cuadrática media, parámetro de la distribución de Rayleigh [m]")])
P("Probabilidad de que una ola supere H<sub>q</sub> (función de excedencia de Rayleigh):")
fbox(["q = P(H &gt; H<sub>q</sub>) = 1 − F(H<sub>q</sub>) = exp[ −(H<sub>q</sub> / H<sub>rms</sub>)² ] = exp[ −(10 / 6,72)² ] = <b>0,109 ≈ 11 %</b>"])
terms([("q", "Probabilidad de que una ola cualquiera supere H<sub>q</sub> (tanto por uno)"),
       ("F(H)", "Función de distribución de Rayleigh: probabilidad de que una ola tenga altura ≤ H"),
       ("exp", "Función exponencial e<sup>x</sup>")])
note("La solución del profesor redondea H<sub>rms</sub> = 6,71 m y da q = 0,1084; con 6,7175 m sale 0,1090. Ambas ≈ 11 %. "
     "En su texto pone «olas de más de 12 m», pero el cálculo correcto (y el suyo) usa 10 m.")
P("<b>Lectura:</b> 11 % <b>por ola</b>. Con 900 olas en el temporal (ver b) habría ≈ 100 rebases: la cota de 5 m no vale.")

h3("b) Cota de la cubierta para que no haya rebase")
P("Para que no haya rebase en <b>todo</b> el temporal se dimensiona con la ola máxima esperada de las N olas. "
  "Número de olas del estado de mar:")
fbox(["N = duración / T<sub>m</sub> = 3 · 3600 / 12 = 900 olas"])
terms([("N", "Número de olas del temporal"), ("T<sub>m</sub>", "Periodo medio [s]"),
       ("duración", "Duración del estado de mar: 3 h = 10 800 s")])
P("Altura de ola <b>media</b> máxima en N olas (función de distribución de H<sub>max</sub>, Longuet-Higgins):")
fbox(["⟨H<sub>max,N</sub>⟩ / H<sub>rms</sub> = √(ln N) + (C/2)·(ln N)<sup>−1/2</sup>",
      "⟨H<sub>max,900</sub>⟩ / H<sub>rms</sub> = √(ln 900) + (0,57722/2)·(ln 900)<sup>−1/2</sup> = 2,608 + 0,111 = 2,719",
      "⟨H<sub>max,900</sub>⟩ = 2,719 · 6,72 = <b>18,26 m</b>"])
terms([("⟨H<sub>max,N</sub>⟩", "Valor medio (esperado) de la ola máxima entre N olas [m]"),
       ("C", "Constante de Euler-Mascheroni = 0,57722"),
       ("ln", "Logaritmo neperiano"), ("H<sub>rms</sub>", "Altura cuadrática media [m]")])
fbox(["Z<sub>cubierta</sub> &gt; ⟨H<sub>max,900</sub>⟩ / 2 = 18,26 / 2 = <b>9,13 m</b>"], bg=ZEBRA)
terms([("Z<sub>cubierta</sub>", "Cota mínima de la cubierta sobre el nivel medio [m]"),
       ("⟨H<sub>max</sub>⟩/2", "Cresta de la ola máxima (cresta y seno simétricos) [m]")])
box("<b>Resultado:</b> a) q ≈ 0,109 (11 % de las olas rebasan). b) Cubierta por encima de <b>z ≈ 9,13 m</b> sobre el nivel medio.")
note("<b>Trampa:</b> el profesor usa la H<sub>max</sub> <b>media</b> (con C = 0,57722). La H<sub>max</sub> <b>más probable</b> (moda) del resumen del Día 3, "
     "H<sub>rms</sub>√(ln N) = 17,52 m, daría 8,76 m. Si el enunciado habla de «altura de ola media máxima», usa la fórmula con C.")

# ------------------------------------------------------------------ EJ 2
story.append(PageBreak())
h2("Ejercicio 2 — Sensores de presión: profundidad, altura y longitud de onda (2 puntos)")
box("<b>Enunciado.</b> La figura muestra la localización de dos sensores de presión. Para una onda progresiva de 12 s los sensores 1 y 2 han "
    "recogido una presión dinámica de 2,07·10⁴ N/m² y 2,13·10⁴ N/m² respectivamente. Calcula la profundidad del emplazamiento, la altura de "
    "ola y la longitud de la onda teniendo en cuenta que la densidad del agua es 1025 kg/m³.")
figure(fx.sensores(), "Figura 1. Sensor #1 en el fondo; sensor #2 a 7,62 m sobre el fondo (h + z₂ = 7,62 m).")

h3("Planteamiento")
P("Campo de presiones de la teoría lineal (hidrostática + dinámica):")
fbox(["p = −ρgz + ρgη · cosh k(h+z) / cosh kh"])
terms([("p", "Presión manométrica en el punto [N/m²]"), ("ρ", "Densidad del agua = 1025 kg/m³"),
       ("g", "Gravedad = 9,81 m/s²"), ("z", "Cota del punto (z = 0 en el nivel medio, negativa hacia abajo) [m]"),
       ("η", "Elevación de la superficie libre [m]"), ("k", "Número de onda = 2π/L [rad/m]"),
       ("h", "Profundidad [m]"), ("cosh k(h+z)/cosh kh", "Factor de respuesta de presión: atenuación con la profundidad")])
P("Los sensores dan la presión <b>dinámica</b> máxima (η = a = H/2):")
fbox(["Sensor 1 (fondo, h+z = 0):   p₁ = 2,07·10⁴ = ρga · 1 / cosh kh",
      "Sensor 2 (h+z = 7,62 m):   p₂ = 2,13·10⁴ = ρga · cosh(7,62k) / cosh kh"])
terms([("a", "Amplitud de la onda = H/2 [m]"), ("p₁, p₂", "Presiones dinámicas medidas por los sensores [N/m²]"),
       ("7,62", "Altura del sensor 2 sobre el fondo, h + z₂ [m]")])

h3("Longitud de onda: dividir las dos ecuaciones")
P("Al dividir desaparecen a y h y queda solo k:")
fbox(["p₁/p₂ = 2,07/2,13 = 1 / cosh(7,62k)   →   k = arccosh(2,13/2,07) / 7,62 = 0,03152 rad/m",
      "L = 2π / k = <b>199,3 m</b>"])
terms([("arccosh", "Inversa del coseno hiperbólico"), ("L", "Longitud de onda [m]")])

h3("Profundidad: dispersión despejando h (sin iterar)")
P("Como k ya es conocido, la ecuación de dispersión se despeja directamente con arctanh:")
fbox(["ω² = gk·tanh(kh)   →   tanh(kh) = ω²/(gk) = (2π/12)² / (9,81·0,03152) = 0,8866",
      "h = arctanh(0,8866) / k = 1,4057 / 0,03152 = <b>44,6 m</b>"])
terms([("ω", "Frecuencia angular = 2π/T = 0,5236 rad/s"), ("T", "Periodo = 12 s"),
       ("tanh, arctanh", "Tangente hiperbólica y su inversa"), ("kh", "Profundidad relativa (1,41 → intermedias)")])
note("La solución del profesor redondea k = 0,0315 y obtiene h = 44,71 m y H = 8,92 m. arctanh es muy sensible cerca de 1: "
     "<b>no redondees k</b> antes de este paso. Ambos resultados se dan por buenos.")

h3("Altura de ola: volver a p₁")
fbox(["p₁ = ρg (H/2) / cosh kh   →   H = 2 · p₁ · cosh(kh) / (ρg) = 2 · 2,07·10⁴ · cosh(1,4057) / (1025·9,81) = <b>8,90 m</b>"])
terms([("H", "Altura de ola = 2a [m]"), ("cosh(kh)", "Coseno hiperbólico de la profundidad relativa = 2,16")])
box("<b>Resultado:</b> L ≈ 199,3 m · h ≈ 44,6 m · H ≈ 8,90 m (profesor: 199,33 m · 44,71 m · 8,92 m).<br/>"
    "<b>Comprobación:</b> con estos valores, ρga/cosh kh = 2,07·10⁴ y ρga·cosh(7,62k)/cosh kh = 2,13·10⁴ ✓")

# ------------------------------------------------------------------ EJ 3
story.append(PageBreak())
h2("Ejercicio 3 — Espectro direccional de la boya: SEA y SWELL (2 puntos)")
box("<b>Enunciado.</b> El espectro direccional medido por el sensor de oleaje de la boya que IDERMAR tiene instalada a 180 m de profundidad frente a "
    "Ubiarco, Cantabria, muestra dos picos, señalados por los puntos en la rosa de periodos-direcciones de la figura adjunta. "
    "El pico correspondiente a 310° se puede asimilar a un cono con una altura S<sub>p310</sub> = 0,075 m²/grd/s y un área en la base de "
    "A<sub>b310</sub> = 40 s·grd. El pico correspondiente a 230° se puede asimilar a un cono con altura S<sub>p230</sub> = 0,00938 m²/grd/s "
    "y un área en la base de A<sub>b230</sub> = 80 s·grd.<br/>Se pide:<br/>"
    "a) Determinar cuál de los picos corresponde al SEA y al SWELL e indicar las razones de la elección.<br/>"
    "b) Determinar para el oleaje de SEA y el de SWELL: momento de orden cero; altura de momento de orden cero; densidad de energía del espectro; periodo modal o de pico.<br/>"
    "c) Para el oleaje compuesto, determinar la altura del momento de orden cero del oleaje compuesto.")
figure(fx.conos_y_rosa(), "Figura 2. Los dos picos asimilados a conos (ω<sub>p</sub> = 2π/16 y 2π/8 rad/s) y su posición en la rosa. "
       "En el original el segundo cono está rotulado «270°», pero el texto y la rosa dan 230°.")

h3("a) ¿Cuál es SEA y cuál SWELL?")
P("<b>310° es el SWELL y 230° el SEA</b>, por tres razones:")
bl("<b>Dirección:</b> la costa cantábrica queda al sur de la boya, así que de esa dirección no puede llegar un swell (oleaje generado lejos, con mucho recorrido). "
   "El pico de 230° viene del lado de tierra → generado cerca por el viento local → SEA.",
   "<b>Anchura del espectro:</b> el área de la base del pico de 310° (40) es menor que la del de 230° (80). El swell es estrecho en frecuencias y direcciones; el sea, ancho.",
   "<b>Periodo de pico:</b> el swell suele tener T<sub>p</sub> mayor (las componentes de periodo corto pierden energía al viajar lejos): 16 s frente a 8 s.")

h3("b) Parámetros de cada pico")
P("El momento de orden cero es el volumen bajo el espectro direccional; si el pico es un cono, es ⅓ · área de la base · altura:")
fbox(["m₀ = ∬ S(ω,θ) dω dθ ≈ ⅓ · A<sub>b</sub> · S<sub>p</sub>      H<sub>m0</sub> = 4√m₀      E = ρg·m₀      T<sub>p</sub> = 2π/ω<sub>p</sub>"])
terms([("m₀", "Momento de orden cero = varianza de η [m²]"), ("S(ω,θ)", "Espectro direccional [m²/(grd·s)]"),
       ("θ", "Dirección [grados]"), ("A<sub>b</sub>", "Área de la base del cono [grd·s]"),
       ("S<sub>p</sub>", "Altura del cono = valor del espectro en el pico [m²/(grd·s)]"),
       ("H<sub>m0</sub>", "Altura de ola de momento de orden cero (≈ H<sub>s</sub>) [m]"),
       ("E", "Densidad de energía media por unidad de superficie [J/m²]"),
       ("ω<sub>p</sub>", "Frecuencia angular del pico [rad/s]"), ("T<sub>p</sub>", "Periodo de pico o modal [s]")])
table(["", "m₀ (m²)", "H<sub>m0</sub> (m)", "E (J/m²)", "T<sub>p</sub> (s)"], [
    ["<b>SWELL 310°</b>", "⅓·0,075·40 = <b>1,00</b>", "4√1 = <b>4</b>", "1025·9,81·1 = <b>10 055</b>", "2π/(2π/16) = <b>16</b>"],
    ["<b>SEA 230°</b>", "⅓·0,00938·80 = <b>0,25</b>", "4√0,25 = <b>2</b>", "1025·9,81·0,25 = <b>2 514</b>", "2π/(2π/8) = <b>8</b>"],
], [32, 38, 28, 42, 30])

h3("c) Oleaje compuesto")
P("SEA y SWELL son independientes: se suman las <b>energías</b> (los m₀), <b>no</b> las alturas:")
fbox(["m₀,total = 1,00 + 0,25 = 1,25 m²      H<sub>m0</sub> = 4√1,25 = <b>4,47 m</b>   (no 4 + 2 = 6 m)"])
terms([("m₀,total", "Momento de orden cero del oleaje compuesto [m²]"),
       ("H<sub>m0</sub>", "Altura de momento de orden cero del compuesto [m]: H<sub>m0</sub> = √(H<sub>sea</sub>² + H<sub>swell</sub>²)")])
box("<b>Resultado:</b> SWELL: m₀ = 1 m², H<sub>m0</sub> = 4 m, E = 10 055 J/m², T<sub>p</sub> = 16 s · SEA: m₀ = 0,25 m², H<sub>m0</sub> = 2 m, "
    "E = 2 514 J/m², T<sub>p</sub> = 8 s · Compuesto: m₀ = 1,25 m², <b>H<sub>m0</sub> = 4,47 m</b>.")

build(sys.argv[1], "Oceanografía · 1er Parcial 29-10-2025 resuelto · Carlos Sánchez Campos", "Oceanografía — 1er Parcial 29-10-2025 resuelto")
