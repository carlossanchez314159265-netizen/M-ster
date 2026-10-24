import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "resumenes")); sys.path.insert(0, HERE)
from estilo import *
import figuras_examenes as fx

P("Oceanografía · Estructura del examen de ejercicios", H1)
P("Análisis de los dos exámenes disponibles (1er Parcial 29-10-2025 y Final ordinario 1er Parcial 13-01-2025) para estudiar lo que de verdad cae · 1er parcial 28/10/2026", SUB)

h2("1. Formato")
bl("Hoja de <b>EJERCICIOS</b> separada, con <b>3 ejercicios de 2 puntos</b> cada uno. Los dos exámenes tienen exactamente el mismo esqueleto.",
   "Se dan las fórmulas «raras» en el enunciado (ley de runup) y los datos ya masticados (L = 239,3 m, conos con área y altura): "
   "lo que puntúa es saber <b>qué fórmula toca y en qué orden</b>, no deducir.",
   "Los resultados son números redondos o casi (m₀ = 1; 0,25; 12 → H<sub>m0</sub> = 4; 2): si te sale algo raro, revisa unidades o un 2π.")
note("<b>Peso real:</b> la hoja de ejercicios suma <b>6 puntos</b> (3 × 2), así que lo más probable es <b>60 % ejercicios / 40 % teoría</b>, "
     "al revés de lo que ponía el planning inicial. No tengo la hoja de teoría para confirmarlo. El análisis sale de solo 2 exámenes: el patrón es claro, pero no es una garantía.")

h2("2. Qué cae en cada ejercicio")
figure(fx.mapa_examen(), "Figura 1. Los dos exámenes repiten los mismos tres bloques; solo cambia el orden y el «envoltorio».")
table(["Bloque", "Parcial 29-10-2025", "Final 13-01", "Peso en tu planning"], [
    ["<b>A. Teoría lineal + dispersión</b>", "Ej. 2: presión dinámica en 2 sensores → k, h, H, L", "Ej. 1: L₀ → T; L → h", "Vie 23 / Sáb 24 (Resumen Día 2)"],
    ["<b>B. Rayleigh + H<sub>max</sub></b>", "Ej. 1: rebase de cubierta (q y cota)", "Ej. 2: runup = η<sub>max</sub> + u²/2g", "Dom 25 (Resumen Día 3)"],
    ["<b>C. Espectral</b>", "Ej. 3: dos conos SEA/SWELL", "Ej. 3: S(ω) por tramos, momentos", "Mar 27 (Espectral)"],
], [38, 50, 42, 40])
P("<b>Conclusión:</b> 2 de 6 puntos son de estadística (Rayleigh + H<sub>max</sub>) y 2 de espectral, que en el planning eran lo «secundario». "
  "Y en ninguno de los dos han caído <b>grupos, estacionarias, tsunami ni trayectorias</b> como ejercicio (la velocidad orbital sí, como paso intermedio). "
  "Siguen pudiendo caer en teoría o en un ejercicio nuevo, pero con poco tiempo el orden de prioridad cambia (sección 5).")

h2("3. Recetas: el algoritmo de cada bloque")
h3("Receta A — Dispersión «al revés» (te dan k o L, piden h)")
bl("Si el dato está en indefinidas: <b>L₀ = gT²/2π</b> → T. El periodo se conserva al propagarse.",
   "Si te dan dos presiones: <b>p₁/p₂</b> elimina a y h → cosh(k·Δz) → k.",
   "Con k (o L) y T conocidos, <b>no hay que iterar</b>: tanh(kh) = ω²/(gk) → h = arctanh(·)/k.",
   "Para H: vuelve a una de las presiones con a = H/2.",
   "Cierra comprobando el régimen con h/L (1/20 y 1/2).")
fbox(["L₀ = gT²/2π      ω² = gk·tanh(kh)      h = arctanh[ω²/(gk)] / k      p<sub>din</sub> = ρg(H/2)·cosh k(h+z)/cosh kh"])
terms([("L₀", "Longitud de onda en indefinidas [m]"), ("T", "Periodo [s]"), ("ω", "2π/T [rad/s]"), ("k", "2π/L [rad/m]"),
       ("h", "Profundidad [m]"), ("z", "Cota del punto (0 en superficie, −h en el fondo) [m]"),
       ("p<sub>din</sub>", "Presión dinámica máxima [N/m²]"), ("ρ, g", "1025 kg/m³ y 9,81 m/s²")])

h3("Receta B — Cota de algo frente a la ola máxima (rebase, runup, cubierta)")
bl("<b>H<sub>rms</sub> = H<sub>s</sub>/√2.</b>",
   "Si preguntan probabilidad por ola: <b>q = exp[−(H<sub>q</sub>/H<sub>rms</sub>)²]</b>, con H<sub>q</sub> = 2·cota (la cresta es H/2).",
   "Si preguntan cota segura: <b>N = duración/T</b> (con el periodo que den), <b>⟨H<sub>max,N</sub>⟩</b> con la constante de Euler, y <b>cresta = ⟨H<sub>max</sub>⟩/2</b>.",
   "Si hay runup: suma u²/2g con u de la teoría lineal en superficie bajo la cresta (u = (Hω/2)·coth kh) usando H = ⟨H<sub>max</sub>⟩.")
fbox(["q = exp[−(H<sub>q</sub>/H<sub>rms</sub>)²]      ⟨H<sub>max,N</sub>⟩/H<sub>rms</sub> = √(ln N) + (C/2)(ln N)<sup>−1/2</sup>      u<sub>max</sub> = (Hω/2)·coth(kh)"])
terms([("q", "Probabilidad de que una ola supere H<sub>q</sub>"), ("H<sub>q</sub>", "Altura umbral = 2·cota [m]"),
       ("H<sub>rms</sub>", "Altura cuadrática media [m]"), ("⟨H<sub>max,N</sub>⟩", "Altura media de la máxima en N olas [m]"),
       ("N", "Número de olas = duración/periodo"), ("C", "Constante de Euler = 0,57722"),
       ("u<sub>max</sub>", "Velocidad orbital horizontal máxima en superficie [m/s]"), ("coth", "Cotangente hiperbólica = cosh/sinh")])

h3("Receta C — Espectro (calcular m₀ y todo lo que cuelga de él)")
bl("m₀ = <b>área</b> (1D) o <b>volumen</b> (direccional). Figura geométrica → fórmula de área/volumen: triángulo ½·b·h, cono ⅓·A<sub>b</sub>·altura.",
   "Si S está por tramos: integra ωⁿS por tramos para m₁, m₂.",
   "<b>H<sub>m0</sub> = 4√m₀</b>, <b>E = ρg·m₀</b>, <b>T<sub>p</sub> = 2π/ω<sub>p</sub></b> (o 1/f<sub>p</sub>), <b>T₀₂ = 2π√(m₀/m₂)</b> si es en ω.",
   "SEA frente a SWELL: dirección (¿viene de tierra?), anchura (base mayor = SEA), periodo (mayor = SWELL).",
   "Oleaje compuesto: se <b>suman los m₀</b>, nunca las alturas.")
fbox(["m₀ = ∫S dω      H<sub>m0</sub> = 4√m₀      E = ρg m₀      T<sub>p</sub> = 2π/ω<sub>p</sub>      T₀₂ = 2π√(m₀/m₂)      T₀₁ = 2π m₀/m₁"])
terms([("m<sub>n</sub>", "Momento espectral de orden n = ∫ωⁿS dω"), ("S", "Densidad espectral [m²·s/rad]"),
       ("H<sub>m0</sub>", "Altura de momento de orden cero ≈ H<sub>s</sub> [m]"), ("E", "Densidad de energía [J/m²]"),
       ("ω<sub>p</sub>", "Frecuencia angular del pico [rad/s]"), ("T<sub>p</sub>", "Periodo de pico [s]"),
       ("T₀₂, T₀₁", "Periodos medios espectrales [s] (con f en Hz no llevan 2π)")])

h2("4. Trampas que el profesor repite")
table(["Trampa", "Cómo evitarla"], [
    ["Usar H<sub>s</sub> en vez de la ola máxima", "Cualquier cota «para que no pase nunca» va con ⟨H<sub>max,N</sub>⟩, no con H<sub>s</sub>."],
    ["Confundir H<sub>max</sub> media y moda", "Él usa la <b>media</b>: √(ln N) + (0,57722/2)(ln N)<sup>−1/2</sup>. La moda H<sub>rms</sub>√(ln N) da ~0,4 m menos de cota."],
    ["Comparar H con la cota", "Lo que llega a la cubierta es la <b>cresta = H/2</b>."],
    ["Sumar alturas de SEA y SWELL", "Se suman m₀: H = √(H₁² + H₂²) = 4,47 m, no 6 m."],
    ["Redondear k antes del arctanh", "arctanh es muy sensible cerca de 1: arrastra 4 cifras."],
    ["Olvidar el 2π", "Espectro en ω (rad/s): T = 2π/ω. En f (Hz): T = 1/f."],
    ["Recalcular T en aguas someras", "El periodo se conserva; lo que cambia es L."],
], [55, 115])

h2("5. Cómo cambia tu planning (lo que queda)")
P("Hoy es sábado 24 por la noche. Como los ejercicios pesan más que la teoría, practicar estos 6 ejercicios es lo más rentable que puedes hacer. Con lo que queda, el orden de rentabilidad pasa a ser: <b>B (estadística) = A (dispersión) = C (espectral) &gt; grupos/estacionarias &gt; tsunami</b>.")
table(["Día", "Qué haces con los exámenes", "Tiempo"], [
    ["<b>Dom 25</b>", "Resumen Día 3 (Rayleigh, H<sub>max</sub>) y, en vez del ejemplo de la diapo 42, <b>Ej. 1 del Parcial 2025</b> y <b>Ej. 2 del Final</b> sin mirar.", "1,5 h"],
    ["<b>Lun 26</b>", "Solo: leer las tres recetas de la sección 3 en el transporte.", "10 min"],
    ["<b>Mar 27</b>", "Bloque espectral del planning y, de práctica, <b>Ej. 3 de ambos</b>. Después <b>Ej. 2 del Parcial</b> y <b>Ej. 1 del Final</b> (dispersión). "
                      "Cierra con un <b>simulacro de 60 min</b>: un examen entero cronometrado, el que peor te haya salido.", "3 h"],
    ["<b>Mié 28</b>", "Recetas + tabla de trampas (secciones 3–4).", "30 min"],
], [20, 130, 20])
box("<b>Regla del examen:</b> antes de calcular, identifica el bloque (A, B o C) y escribe su receta. Cada ejercicio son 4–6 líneas de cálculo: "
    "si llevas más de media cara, te has metido por un camino que no es.")

h2("6. Dónde está cada cosa")
bl("<b>examenes/Examen 1er Parcial 29-10-2025 (resuelto).pdf</b> — enunciados transcritos + resolución con leyenda de términos.",
   "<b>examenes/Examen Final ordinario 1er Parcial 13-01-2025 (resuelto).pdf</b> — ídem.",
   "Teoría de apoyo: Resumen Día 2 (bloque A), Resumen Día 3 (bloque B), diapos del Espectral indicadas en el planning del martes (bloque C).")

build(sys.argv[1], "Oceanografía · Análisis de la estructura del examen · Carlos Sánchez Campos", "Oceanografía — Estructura del examen")
