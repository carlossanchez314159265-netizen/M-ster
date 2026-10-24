import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "resumenes")); sys.path.insert(0, HERE)
from estilo import *
import figuras_examenes as fx

P("Oceanografía · Examen final ordinario — 1er Parcial", H1)
P("13 de enero de 2025 (así figura; el encabezado es del curso 2025-26, probablemente enero de 2026) · ETSIN-UPM · Parte de EJERCICIOS (3 × 2 puntos) · enunciados transcritos y resolución paso a paso", SUB)

note("<b>Cómo usar este PDF:</b> lee el enunciado, tapa la resolución y hazlo tú con calculadora (máx. 20 min por ejercicio). "
     "Los resultados se han recalculado; donde la solución del profesor redondea distinto se indica en ámbar.")

table(["Ej.", "Tema", "Qué tienes que saber", "Pts"], [
    ["1", "Dispersión: indefinidas → plataforma", "L₀ = gT²/2π da T; con L y T conocidos, la dispersión se despeja con arctanh (sin iterar)", "2"],
    ["2", "Rayleigh + H<sub>max</sub> + velocidad orbital", "N = duración/T<sub>p</sub>, ⟨H<sub>max,N</sub>⟩, η<sub>max</sub> = H/2, u<sub>max</sub> de la teoría lineal, R<sub>u</sub> = η<sub>max</sub> + u²/2g", "2"],
    ["3", "Espectro S(ω) por tramos", "m<sub>n</sub> = ∫ωⁿS dω por tramos, H<sub>m0</sub> = 4√m₀, E = ρgm₀, T<sub>p</sub> = 2π/ω<sub>p</sub>, T₀₂ = 2π√(m₀/m₂)", "2"],
], [10, 45, 105, 10])

# ------------------------------------------------------------------ EJ 1
h2("Ejercicio 1 — Profundidad y periodo de un tren de ondas (2 puntos)")
box("<b>Enunciado.</b> Un tren de ondas en profundidades indefinidas tiene una longitud de onda de 156 metros. No obstante, cuando llega a mi estructura, "
    "ya localizada en la plataforma continental, los registros observados indican que su longitud de onda es ahora de 140 metros. "
    "¿Cuál es la profundidad a la que se encuentra mi estructura? ¿Cuál es el periodo del tren de ondas?")
h3("Periodo (se conserva al propagarse)")
P("El periodo no cambia con la profundidad (lo que cambia es L). Se obtiene donde la profundidad es conocida, en indefinidas:")
fbox(["L₀ = gT² / 2π   →   T = √(2π·L₀/g) = √(2π·156/9,81) = 9,99 s ≈ <b>10 s</b>"])
terms([("L₀", "Longitud de onda en profundidades indefinidas = 156 m"), ("g", "Gravedad = 9,81 m/s²"),
       ("T", "Periodo de la onda [s]")])
h3("Profundidad (dispersión completa)")
P("En la estructura no sabemos si estamos en indefinidas, intermedias o reducidas → ecuación de dispersión completa, con ω = 2π/T y k = 2π/140:")
fbox(["ω² = gk·tanh(kh)   →   (2π/10)² = (9,81·2π/140)·tanh(2π·h/140)",
      "tanh(kh) = 0,3948 / 0,4403 = 0,8967   →   kh = arctanh(0,8967) = 1,455",
      "h = 1,455 / (2π/140) = <b>32,4 m</b>"])
terms([("ω", "Frecuencia angular = 2π/T = 0,628 rad/s"), ("k", "Número de onda en la estructura = 2π/140 = 0,0449 rad/m"),
       ("h", "Profundidad en la estructura [m]"), ("kh", "Profundidad relativa"),
       ("tanh, arctanh", "Tangente hiperbólica y su inversa")])
P("Comprobación de régimen: h/L = 32,4/140 = 0,23, entre 1/20 y 1/2 → <b>intermedias</b> (no valía ninguna simplificación).")
note("Con T = 9,996 s sin redondear sale h = 32,5 m. El profesor usa T = 10 s → 32,4 m.")
box("<b>Resultado:</b> T ≈ 10 s · h ≈ 32,4 m.")

# ------------------------------------------------------------------ EJ 2
h2("Ejercicio 2 — Cota de protección por runup (2 puntos)")
box("<b>Enunciado.</b> Eres el ingeniero responsable de una estructura offshore localizada a 40 m de profundidad que está a punto de sufrir el impacto de "
    "una ciclogénesis explosiva que va a generar oleajes extremos de H<sub>s</sub> = 8 m y T<sub>p</sub> = 14 s (L = 239,3 m) (estado de mar de 3 horas de duración). "
    "Dado que tienes que velar por la seguridad de la estructura, es preciso poner a resguardo todos aquellos elementos susceptibles de ser impactados por el oleaje. "
    "Asumiendo que el runup del oleaje en tu estructura sigue la ley R<sub>u</sub> = η<sub>max</sub> + u²/2g, donde η<sub>max</sub> es la cresta máxima del oleaje "
    "de diseño, u la velocidad orbital horizontal máxima del oleaje de diseño y g la aceleración de la gravedad: "
    "¿hasta qué cota sobre el nivel medio del mar debes proteger o retirar todos aquellos elementos que pueden ser afectados por el oleaje?")
fbox(["R<sub>u</sub> = η<sub>max</sub> + u² / 2g"])
terms([("R<sub>u</sub>", "Runup: cota que alcanza el agua sobre el nivel medio [m]"),
       ("η<sub>max</sub>", "Cresta máxima del oleaje de diseño [m]"),
       ("u", "Velocidad orbital horizontal máxima [m/s]"), ("u²/2g", "Altura cinética: lo que «sube» el agua al frenarse contra la estructura [m]")])
P("Los dos sumandos se calculan con la <b>ola máxima</b> del temporal, no con H<sub>s</sub>.")

h3("Paso 1 — Altura de la ola máxima (igual que el parcial)")
fbox(["N = 3 · 3600 / 14 = 771 olas",
      "⟨H<sub>max,N</sub>⟩ / H<sub>rms</sub> = √(ln 771) + (0,57722/2)·(ln 771)<sup>−1/2</sup> = 2,69",
      "H<sub>rms</sub> = H<sub>s</sub>/√2 = 8/√2 = 5,66 m   →   ⟨H<sub>max,771</sub>⟩ = 5,66 · 2,69 = <b>15,21 m</b>",
      "η<sub>max</sub> = ⟨H<sub>max</sub>⟩ / 2 = <b>7,6 m</b>   (cresta y seno simétricos)"])
terms([("N", "Número de olas en 3 h (aquí con T<sub>p</sub>, que es el periodo dado)"),
       ("⟨H<sub>max,N</sub>⟩", "Altura media de la ola máxima entre N olas [m]"), ("C = 0,57722", "Constante de Euler"),
       ("H<sub>rms</sub>", "Altura cuadrática media (Rayleigh) [m]"), ("H<sub>s</sub>", "Altura significante = 8 m")])

h3("Paso 2 — Velocidad orbital horizontal máxima (teoría lineal)")
fbox(["u = (Hω/2) · cosh k(h+z) / sinh kh · cos(kx − ωt)"])
terms([("H", "Altura de la ola de diseño = 15,21 m"), ("ω", "2π/T<sub>p</sub> = 0,449 rad/s"),
       ("k", "2π/L = 2π/239,3 = 0,0263 rad/m"), ("h", "Profundidad = 40 m"),
       ("z", "Cota del punto (0 en superficie)"), ("cos(kx−ωt)", "Fase: vale 1 bajo la cresta")])
P("El máximo está bajo la cresta (cos = 1) y en la superficie (z = 0) → cosh kh/sinh kh = coth kh:")
fbox(["u<sub>max</sub> = (15,21·π/14) · cosh(2π·40/239,3) / sinh(2π·40/239,3) = 3,413 · 1,280 = <b>4,37 m/s</b>"])
terms([("kh", "2π·40/239,3 = 1,05 (intermedias)"), ("coth kh", "cosh kh / sinh kh = 1,28"),
       ("Hω/2", "15,21·0,449/2 = 3,413 m/s")])

h3("Paso 3 — Runup")
fbox(["R<sub>u</sub> = 7,6 + 4,37² / (2·9,81) = 7,6 + 0,97 = <b>8,57 m</b>"])
terms([("R<sub>u</sub>", "Cota de protección sobre el nivel medio [m]")])
note("El profesor da u = 4,35 m/s y R<sub>u</sub> = 8,56 m (redondeo de u). Se comprobó además que L = 239,3 m sale de la dispersión con T = 14 s y h = 40 m.")
box("<b>Resultado:</b> proteger o retirar todo lo que esté por debajo de <b>≈ 8,6 m</b> sobre el nivel medio del mar.")

# ------------------------------------------------------------------ EJ 3
h2("Ejercicio 3 — Parámetros de un espectro unidimensional (2 puntos)")
box("<b>Enunciado.</b> Se considera un espectro unidimensional, local y continuo de densidad espectral de energía del oleaje, definido por tramos según "
    "la frecuencia angular ω: S(ω) = 1,5ω para 0 &lt; ω &lt; 2; S(ω) = 4 − ω/2 para 2 &lt; ω &lt; 8; S(ω) = 0 en otro caso, "
    "donde S(ω) se expresa en las unidades habituales del espectro de oleaje. Se pide, para el estado de mar definido por este espectro: "
    "a) momento de orden cero y altura de ola de momento de orden cero; b) densidad de energía del espectro; c) periodo modal o de pico; "
    "d) periodo medio espectral; e) dibuja el espectro e indica la localización del periodo de pico.")
h3("Momentos espectrales (integrar por tramos)")
fbox(["m<sub>n</sub> = ∫₀<sup>∞</sup> ωⁿ S(ω) dω = ∫₀² 1,5ω·ωⁿ dω + ∫₂⁸ (4 − ω/2)·ωⁿ dω",
      "m<sub>n</sub> = 3·2<sup>n+2</sup>/[2(n+2)] + 4·(8<sup>n+1</sup> − 2<sup>n+1</sup>)/(n+1) − (8<sup>n+2</sup> − 2<sup>n+2</sup>)/[2(n+2)]",
      "m₀ = 12 m²     m₁ = 40 m²·rad/s     m₂ = 168 m²·rad²/s²"])
terms([("m<sub>n</sub>", "Momento espectral de orden n"), ("S(ω)", "Densidad espectral de energía [m²·s/rad]"),
       ("ω", "Frecuencia angular [rad/s]"), ("n", "Orden del momento (0, 1, 2…)")])
P("<b>Atajo para m₀:</b> es el área bajo la curva, un triángulo de base 8 y altura 3 → ½·8·3 = 12. Úsalo para comprobar.")
h3("a) – d)")
fbox(["a) H<sub>m0</sub> = 4√m₀ = 4√12 = <b>13,86 m</b>",
      "b) E = ρg·m₀ = 1025·9,81·12 = <b>120 663 J/m²</b>",
      "c) máximo de S en ω<sub>p</sub> = 2 rad/s (S = 3)   →   T<sub>p</sub> = 2π/ω<sub>p</sub> = <b>3,14 s</b>",
      "d) T₀₂ = 2π√(m₀/m₂) = 2π√(12/168) = <b>1,68 s</b>"])
terms([("H<sub>m0</sub>", "Altura de momento de orden cero [m]"), ("E", "Densidad de energía [J/m²]"),
       ("ρ", "Densidad del agua = 1025 kg/m³"), ("ω<sub>p</sub>", "Frecuencia del pico del espectro [rad/s]"),
       ("T<sub>p</sub>", "Periodo de pico o modal [s]"), ("T₀₂", "Periodo medio de pasos por cero, con m₀ y m₂ [s]"),
       ("2π", "Aparece porque el espectro está en ω (rad/s) y no en f (Hz)")])
note("El profesor escribe H<sub>s</sub> = 13,85 m; el valor exacto es 4√12 = 13,856 → 13,86 m. "
     "«Periodo medio espectral» también podría ser T₀₁ = 2π·m₀/m₁ = 1,88 s; el profesor usó T₀₂. Si te lo piden, di cuál calculas.")
h3("e) Dibujo del espectro")
figure(fx.espectro(), "Figura 3. S(ω) del ejercicio 3: área sombreada m₀ = 12; pico en ω<sub>p</sub> = 2 rad/s (T<sub>p</sub> = 3,14 s).")
box("<b>Resultado:</b> m₀ = 12 m² · H<sub>m0</sub> = 13,86 m · E = 120 663 J/m² · T<sub>p</sub> = 3,14 s · T₀₂ = 1,68 s.")

build(sys.argv[1], "Oceanografía · Final ordinario 1er Parcial 13-01-2025 resuelto · Carlos Sánchez Campos", "Oceanografía — Final ordinario 13-01-2025 resuelto")
