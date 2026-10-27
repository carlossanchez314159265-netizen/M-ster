"""Examen del 2º parcial (13-01-2026), solo la parte que entra en el 1er parcial (dispersión, celeridad de grupo y asomeramiento).

Uso: python3 final_p2_13-01-2026.py "../../examenes/Examen 2o Parcial 13-01-2026 - parte del 1er parcial (resuelto).pdf"
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "resumenes")); sys.path.insert(0, HERE)
from estilo import *

P("Oceanografía · Examen del 2º Parcial — parte del 1er parcial", H1)
P("13 de enero de 2026 · ETSIN-UPM · Ejercicio 1, apartados a), b) y c) · resolución paso a paso con la solución del profesor recalculada", SUB)

note("<b>Qué hay aquí y qué no.</b> El examen es del 2º parcial. Solo entra en el 1er parcial lo que usa la <b>dispersión, la celeridad de grupo, "
     "el asomeramiento y los regímenes de clima marítimo</b>. Se quedan fuera: la <b>refracción</b> (ley de Snell y K<sub>r</sub>) del apartado c), "
     "los apartados d) y e) (dibujar la dirección de las cargas) y todo el <b>Ejercicio 2</b> (tensiones en el lecho marino y círculo de Mohr).")

table(["Apdo.", "Tema", "Qué tienes que saber", "Pts"], [
    ["a)", "Régimen de oleaje", "Dimensionar (fiabilidad, ELU) → régimen <b>extremal</b>; operar (ELO) → régimen <b>medio</b>", "0,75"],
    ["b)", "Oleaje en indefinidas", "L₀ = gT²/2π, C₀ = L₀/T, C<sub>g0</sub> = C₀/2; H y T se conservan", "0,75"],
    ["c)", "Oleaje en el monopilote", "Dispersión en h = 20 m, C = L/T, C<sub>g</sub> = n·C y asomeramiento K<sub>s</sub> = √(C<sub>g0</sub>/C<sub>g</sub>)", "0,75"],
], [15, 35, 108, 12])

box("<b>Enunciado.</b> Se proyecta la instalación de un parque eólico de cimentación fija empleando estructuras tipo monopilote en Dogger Bank (Mar del Norte). "
    "El emplazamiento se caracteriza por una batimetría rectilínea, con isobatas aproximadamente paralelas en dirección E–W, de modo que la profundidad aumenta hacia el Norte. "
    "Las turbinas se van a colocar a una profundidad de unos 20 m (h = 20 m) y se desea realizar un predimensionamiento de los monopilotes.<br/>"
    "a) ¿Qué régimen de oleaje debe usarse para el dimensionamiento de la estructura? (0,75 puntos)<br/>"
    "Oleaje de cálculo en indefinidas: dirección NE, H = 7 m, T = 16 s.<br/>"
    "b) Calcula las características del oleaje de cálculo en indefinidas: H₀, T, θ₀, L₀, C₀, C<sub>g0</sub>. (0,75 puntos)<br/>"
    "c) Calcula las características del oleaje en el monopilote: H<sub>m</sub>, T, θ<sub>m</sub>, L<sub>m</sub>, C<sub>m</sub>, C<sub>gm</sub>. "
    "Como aproximación, puede asumir que el punto objetivo está en profundidades reducidas. (0,75 puntos)")

# ------------------------------------------------------------------ a
h2("a) Régimen de oleaje para dimensionar")
P("Según las Recomendaciones de Obras Marítimas (ROM), una obra marítima debe cumplir requisitos de <b>fiabilidad</b>, <b>funcionalidad</b> y <b>operatividad</b>, "
  "y cada uno se estudia con un régimen distinto del clima marítimo:")
table(["Requisito", "Régimen", "Estado límite", "Pregunta que responde"], [
    ["<b>Fiabilidad</b>: sobrevivir a condiciones extremas", "<b>Extremal</b>", "ELU (último): rotura, vuelco, colapso", "¿Aguanta el monopilote el peor temporal de su vida útil?"],
    ["Funcionalidad y operatividad: trabajar en condiciones habituales", "Medio", "ELS (servicio) y ELO (parada operativa)", "¿Cuántas horas al año se puede acceder u operar?"],
], [44, 22, 44, 60])
box("<b>Respuesta:</b> para <b>dimensionar</b> los monopilotes (que no rompan ni vuelquen) se usa el <b>régimen extremal</b>, con el estado límite último (ELU). "
    "El régimen medio sirve para la operatividad, no para dimensionar la estructura.")
note("El enunciado llama al oleaje de los apartados siguientes «oleaje de cálculo para asegurar la operatividad». Aun así, la pregunta a) es sobre el "
     "<b>dimensionamiento</b>, y eso se hace con el régimen extremal.")

# ------------------------------------------------------------------ b
h2("b) Oleaje en profundidades indefinidas")
P("En indefinidas tanh(kh) → 1 y la dispersión queda ω² = gk₀: todo sale directamente de T.")
fbox(["L₀ = gT²/2π = 9,81·16²/2π = <b>399,7 m</b>          C₀ = L₀/T = 399,7/16 = <b>24,98 m/s</b>",
      "C<sub>g0</sub> = C₀/2 = <b>12,49 m/s</b>   (en indefinidas n = ½)",
      "H₀ = <b>7 m</b>      T = <b>16 s</b>      θ₀ = <b>45°</b>"])
terms([("L₀, C₀", "Longitud de onda y celeridad en indefinidas"), ("C<sub>g0</sub>", "Celeridad de grupo en indefinidas = C₀/2"),
       ("θ₀", "Ángulo entre la dirección del oleaje y la normal a las isobatas"), ("T", "Periodo: se conserva en toda la propagación")])
P("<b>Por qué θ₀ = 45°:</b> las isobatas van E–W, así que su normal es la dirección N–S. El oleaje viene del NE, que forma 45° con el Norte.")

# ------------------------------------------------------------------ c
h2("c) Oleaje en el monopilote (h = 20 m)")
P("El periodo se conserva (T = 16 s, ω = 2π/16 = 0,3927 rad/s). Lo que cambia con la profundidad es k, L, C y C<sub>g</sub>.")
h3("Versión 1 — aproximación de reducidas (la que propone el enunciado)")
fbox(["ω² = g·h·k²   →   k = ω/√(gh) = 0,3927/√(9,81·20) = <b>0,02804 rad/m</b>",
      "L = 2π/k = <b>224,1 m</b>          C = √(gh) = <b>14,01 m/s</b>          en reducidas n = 1  →  C<sub>g</sub> = C = <b>14,01 m/s</b>"])
P("<b>Comprobación de la hipótesis:</b> h/L = 20/224,1 = 0,089, que es <b>mayor que 1/20 = 0,05</b>. No estamos en reducidas, sino en <b>intermedias</b>: "
  "la aproximación vale solo para hacerse una idea. Hay que resolver la dispersión completa.")
h3("Versión 2 — dispersión completa (la correcta)")
fbox(["ω² = g·k·tanh(kh)   →   Newton-Raphson desde k₀ = ω²/g = 0,01572   →   <b>k = 0,02959 rad/m</b>   (kh = 0,592)",
      "L = 2π/k = <b>212,3 m</b>          C = L/T = <b>13,27 m/s</b>          h/L = 0,094 → intermedias ✓",
      "n = ½·[1 + 2kh/sinh(2kh)] = 0,900          C<sub>g</sub> = n·C = <b>11,94 m/s</b>"])
terms([("k₀ = ω²/g", "Valor de arranque (el de indefinidas)"), ("n", "Cociente C<sub>g</sub>/C: ½ en indefinidas, 1 en reducidas"),
       ("kh = 0,592", "Entre π/10 = 0,31 y π = 3,14: intermedias")])
h3("Altura en el monopilote: asomeramiento")
P("El flujo de energía E·C<sub>g</sub> se conserva entre dos rayos de oleaje. Sin refracción (frente paralelo a las isobatas), H solo cambia por asomeramiento:")
fbox(["H₀²·C<sub>g0</sub> = H<sub>m</sub>²·C<sub>gm</sub>   →   <b>K<sub>s</sub> = √(C<sub>g0</sub>/C<sub>gm</sub>)</b> = √(12,49/11,94) = <b>1,023</b>",
      "Solo asomeramiento:   H = 7 · 1,023 = 7,16 m"])
terms([("K<sub>s</sub>", "Coeficiente de asomeramiento"), ("C<sub>g0</sub>, C<sub>gm</sub>", "Celeridad de grupo en indefinidas y en el monopilote")])
note("<b>2º parcial (para que te suene):</b> como el oleaje llega oblicuo (45°), también hay <b>refracción</b>. Con la ley de Snell, sin θ₀/C₀ = sin θ<sub>m</sub>/C<sub>m</sub>, "
     "sale θ<sub>m</sub> = 22,1° y K<sub>r</sub> = √(cos θ₀/cos θ<sub>m</sub>) = 0,873. La altura final es H<sub>m</sub> = 7 · 1,023 · 0,873 = <b>6,25 m</b>. "
     "No hace falta para el 1er parcial.")
box("<b>Resultado (1er parcial):</b> T = 16 s · k = 0,0296 rad/m · L<sub>m</sub> = 212,3 m · C<sub>m</sub> = 13,27 m/s · C<sub>gm</sub> = 11,94 m/s · "
    "K<sub>s</sub> = 1,023. Con la refracción del 2º parcial: θ<sub>m</sub> = 22,1° y H<sub>m</sub> = 6,25 m.")
note("<b>Erratas de la solución del profesor:</b><br/>"
     "· En la versión de reducidas calcula C<sub>g</sub> con la fórmula de intermedias (12,72 m/s). En reducidas n = 1 y C<sub>g</sub> = C = 14,01 m/s.<br/>"
     "· Escribe «H<sub>0</sub>·K<sub>s</sub>·K<sub>r</sub> = 7,0 · 0,873 · 1,023»: el 0,873 es K<sub>r</sub> y el 1,023 es K<sub>s</sub> (están cambiados). "
     "En la versión de reducidas pasa lo mismo: 0,877 es K<sub>r</sub>.<br/>"
     "· Su resultado final, H<sub>m</sub> = 6,25 m con la dispersión completa, sí es correcto.")

build(sys.argv[1], "Oceanografía · 2º Parcial 13-01-2026 (parte del 1er parcial) resuelto · Carlos Sánchez Campos",
      "Oceanografía — 2º Parcial 13-01-2026, parte del 1er parcial")
