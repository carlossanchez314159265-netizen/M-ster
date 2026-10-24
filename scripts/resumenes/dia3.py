import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from estilo import *

P("Oceanografía · Día 3", H1)
P("Tema 2 — Oleaje: Análisis del oleaje (1/3) · Análisis estadístico (Rayleigh, H<sub>max</sub>) · domingo 25/10 · 1er parcial 28/10/2026", SUB)

h2("0. Plan del día (1,5 h)")
table(["Bloque", "Qué hacer", "Tiempo"], [
    ["A", "Secciones 1–2: hipótesis (estocástico, estacionario, ergódico, gaussiano), estado de mar y paso por cero.", "20 min"],
    ["B", "Secciones 3–4: estadísticos (H<sub>max</sub>, H<sub>1/3</sub>, H<sub>1/10</sub>, H<sub>m</sub>, H<sub>rms</sub>, T<sub>z</sub>) y distribución de Rayleigh.", "25 min"],
    ["C", "Sección 5: H<sub>max</sub> en un estado de mar. <b>Rehaz el ejemplo de la diapo 42 sin mirar.</b>", "25 min"],
    ["D", "Sección 6 (ejercicios) + autoexamen de 15 min con las preguntas del final y el mazo Anki.", "20 min"],
], [16, 136, 18])
note("<b>Objetivo de cierre:</b> saber hacer, con calculadora, (1) los estadísticos de un registro de olas, (2) la altura superada por un q % de olas, "
     "H<sub>q</sub> = H<sub>rms</sub>√(−ln q), y (3) la H<sub>max</sub> más probable en N olas, H<sub>max,moda</sub> = H<sub>rms</sub>√(ln N) con N = duración/T<sub>m</sub>. "
     "Y contestar las preguntas tipo 7, 8 y 9 del planning (hipótesis, paso por cero y estadísticos, límites de Rayleigh y freak waves).")
terms([
    ("H<sub>q</sub>", "Altura de ola que solo superan una fracción q de las olas [m]"),
    ("q", "Fracción de olas que la superan (en tanto por uno: 1 % → q = 0,01)"),
    ("H<sub>rms</sub>", "Altura media cuadrática del registro (parámetro de Rayleigh) [m]"),
    ("ln", "Logaritmo neperiano"),
    ("H<sub>max,moda</sub>", "Altura máxima más probable en el estado de mar [m]"),
    ("N", "Número de olas del estado de mar = duración / T<sub>m</sub>"),
    ("T<sub>m</sub>", "Periodo medio de las olas [s]"),
])
P("El resto del domingo es para tu examen del lunes: esto está pensado para que quepa en hora y media.")

h2("1. Hipótesis de partida")
bl("<b>Oleaje</b>: oscilaciones de gravedad de 2–20 s generadas por el viento. Caótico → se trata estadística (dominio del tiempo/probabilidad, hoy) y espectralmente (dominio de la frecuencia, martes).",
   "<b>Corto plazo</b>: propiedades ola a ola de <b>un</b> estado de mar (H<sub>s</sub>, H<sub>max</sub>, H<sub>rms</sub>, T<sub>z</sub>, F(H), F(H,T)). <b>Largo plazo</b>: un <b>conjunto</b> de estados de mar durante años (regímenes medio y extremal).",
   "El oleaje se modela como proceso <b>estocástico</b> (aleatorio), <b>estacionario</b> (sus momentos estadísticos no cambian al trasladar el origen de tiempos → eso es un <b>estado de mar</b>) y <b>ergódico</b> (una sola muestra suficientemente larga representa al proceso entero).",
   "<b>Gaussiano de media cero</b> por el <b>teorema central del límite</b>: suma de muchos trenes de onda independientes (Pierson, 1958). Queda definido por media y varianza.",
   "<b>Estado de mar</b>: intervalo en que el proceso es estacionario. Compromiso: corto para que sea estacionario, largo para tener estadística. Hoy se usa <b>1 h</b>; mínimo ≈ 20–30 min (límite clásico de las boyas).",
   "<b>Limitaciones</b>: el océano real nunca es estacionario ni ergódico; se acepta en áreas y tiempos limitados. En indefinidas η es gaussiana; la normalidad empeora al <b>aumentar la amplitud y disminuir la profundidad</b> (en reducidas, no gaussiano).")
terms([
    ("H<sub>s</sub>", "Altura de ola significante (= H<sub>1/3</sub>) [m]"),
    ("H<sub>max</sub>", "Altura de la mayor ola del registro [m]"),
    ("T<sub>z</sub>", "Periodo medio de paso por cero [s]"),
    ("F(H)", "Función de distribución de las alturas: probabilidad de que una ola tenga altura ≤ H"),
    ("F(H,T)", "Distribución conjunta de alturas y periodos"),
    ("η", "Superficie libre: elevación respecto al nivel medio [m]"),
])

h2("2. Identificar olas: análisis de paso por cero")
bl("Pasos: (1) serie de η y restar el nivel medio (media cero); (2) dividir en estados de mar; (3) <b>paso ascendente por cero (PAC)</b> para obtener cada ola; (4) estadística de H, T…",
   "<b>Ola</b> = tramo entre dos PAC consecutivos. <b>H<sub>i</sub></b> = distancia vertical máxima (cresta – seno) entre los PAC i e i+1; <b>T<sub>i</sub></b> = tiempo entre ellos.",
   "PAC y PDC (descendente) dan olas distintas pero <b>estadística equivalente</b> para registros largos, salvo en reducidas o rompientes: la asimetría de las crestas da periodos menores con PDC.",
   "Fiabilidad: al menos <b>100 olas</b> (recomendable <b>1000</b>) → con T<sub>m</sub> ≈ 15 s, registros de 30 min a 1 h (3 h para 1000 olas).")
terms([
    ("PAC", "Paso ascendente por cero: instante en que η cruza el nivel medio subiendo"),
    ("PDC", "Paso descendente por cero: η cruza el nivel medio bajando"),
    ("H<sub>i</sub>", "Altura de la ola i: cresta máxima − seno mínimo entre dos PAC [m]"),
    ("T<sub>i</sub>", "Periodo de la ola i: tiempo entre dos PAC consecutivos [s]"),
    ("i", "Índice que numera las olas del registro (1, 2, …, N)"),
    ("T<sub>m</sub>", "Periodo medio [s]"),
])

h2("3. Estadísticos principales")
table(["Estadístico", "Definición"], [
    ["H<sub>max</sub>, T<sub>max</sub>", "Altura de la mayor ola y su periodo (el de la mayor ola en altura)."],
    ["H<sub>1/n</sub>, T<sub>1/n</sub>", "Media de las N/n olas más altas (ordenadas por H) y media de <b>sus</b> periodos."],
    ["H<sub>s</sub> = H<sub>1/3</sub>, T<sub>1/3</sub>", "Media del tercio de olas más altas (Sverdrup y Munk, 1947: casa lo medido con lo observado a ojo)."],
    ["H<sub>m</sub> (H̄), T<sub>m</sub> (T<sub>z</sub>)", "Media de todas las alturas y de todos los periodos (T<sub>m</sub> por PAC ≈ T<sub>z</sub>)."],
    ["H<sub>rms</sub>", "√[(1/N) Σ H<sub>i</sub>²] — altura media cuadrática; es el parámetro de Rayleigh."],
], [40, 130])
terms([
    ("N", "Número total de olas del registro"),
    ("n", "Divisor que define la fracción: n = 3 → tercio de olas más altas; n = 10 → décima parte"),
    ("H<sub>i</sub>", "Altura de cada ola i [m]"),
    ("Σ H<sub>i</sub>²", "Suma de los cuadrados de todas las alturas [m²]"),
    ("(1/N)·Σ", "Media aritmética de esos cuadrados"),
    ("√", "Raíz cuadrada: devuelve la media cuadrática a metros"),
    ("H<sub>m</sub> (H̄)", "Altura media = (1/N)·Σ H<sub>i</sub> [m]"),
    ("T<sub>m</sub>, T<sub>z</sub>", "Periodo medio y periodo medio de paso por cero [s]"),
])
h3("Ejemplo de clase (diapos 22–25): 22 olas")
P("Ordenadas por H, las 7 mayores (22/3 → 7) son 1,20 · 1,09 · 1,09 · 1,03 · 0,99 · 0,97 · 0,88 m.")
table(["Estadístico", "Resultado", "Comentario"], [
    ["H<sub>max</sub>", "<b>1,20 m</b>", ""],
    ["H<sub>1/3</sub>", "7,25/7 = <b>1,03 m</b>", "Coincide con la diapo."],
    ["T<sub>1/3</sub>", "<b>5,20 s</b> (media de los T de esas 7 olas)",
     "⚠ La diapo da 5,65 s porque promedia los 7 <b>periodos</b> mayores; por su propia definición (diapo 24) es la media de los periodos de las olas más altas."],
    ["T<sub>max</sub>", "<b>6,00 s</b> (periodo de la ola de 1,20 m)", "⚠ La diapo da 6,23 s (el mayor periodo). Si sale, di qué definición usas."],
    ["H<sub>m</sub> y T<sub>m</sub>", "<b>0,58 m</b> y <b>4,16 s</b>", "Coinciden (0,57 m en la diapo por redondeo)."],
    ["H<sub>rms</sub>", "<b>0,69 m</b>", "Coincide (0,68). Comprueba: 1,416·0,69 = 0,97 ≈ H<sub>1/3</sub>."],
], [26, 58, 86])
terms([
    ("22/3 → 7", "Número de olas del tercio superior: N/3 redondeado"),
    ("7,25/7", "Suma de las 7 alturas mayores entre 7 → media del tercio superior"),
    ("1,416", "Cociente teórico H<sub>1/3</sub>/H<sub>rms</sub> de Rayleigh (sección 4)"),
])

h2("4. Distribuciones")
bl("<b>FDP</b> f(x): cómo se reparte la probabilidad (no da probabilidades de valores sueltos). <b>Función de distribución</b> F(x) = P(X ≤ x): probabilidad acumulada. "
   "Empírica con N olas ordenadas de mayor a menor: F(H ≤ H<sub>i</sub>) = (N + 1 − i)/N.")
terms([
    ("f(x)", "Función de densidad de probabilidad (FDP): su área entre a y b es la probabilidad de caer entre a y b"),
    ("F(x)", "Función de distribución: probabilidad acumulada de que X ≤ x (va de 0 a 1)"),
    ("P(X ≤ x)", "Probabilidad de que la variable aleatoria X no supere el valor x"),
    ("N", "Número de olas"),
    ("i", "Posición de la ola en la lista ordenada de mayor a menor (i = 1 es la más alta)"),
    ("(N + 1 − i)/N", "Fracción de olas con altura ≤ H<sub>i</sub>"),
])
P("<b>Superficie libre</b> (indefinidas): normal")
fbox(["f(η) = [1 / (η<sub>rms</sub>·√(2π))] · exp(−η² / 2η<sub>rms</sub>²)"])
terms([
    ("f(η)", "Densidad de probabilidad de la elevación η"),
    ("η", "Elevación de la superficie respecto al nivel medio [m]"),
    ("η<sub>rms</sub>", "Valor cuadrático medio de η [m]; con media cero coincide con la desviación típica σ"),
    ("exp( )", "Función exponencial (e elevado a lo que hay dentro)"),
    ("√(2π)", "Constante de normalización (área total = 1)"),
])
P("Da igual probabilidad a crestas y senos → solo vale para oleaje <b>lineal</b>.")
bl("<b>Momentos</b>: 1.º = media; 2.º central = varianza; 3.º = <b>asimetría</b> (sesgo: crestas cortas y peraltadas, senos largos y planos, típico de reducidas); "
   "4.º − 3 = <b>curtosis</b> (apuntamiento respecto a la normal). Sesgo y curtosis nulos → normal; si no, hay no linealidad.")
terms([
    ("Momento de orden n", "Media de (η − media)<super>n</super>: resume la forma de la distribución"),
    ("Varianza", "Momento central de orden 2 = σ² [m²]"),
    ("Asimetría (sesgo)", "Momento de orden 3 normalizado: 0 si es simétrica"),
    ("Curtosis", "Momento de orden 4 normalizado menos 3: 0 en la normal; &gt; 0 más apuntada"),
])
h3("Rayleigh: alturas de ola en banda estrecha (swell)")
fbox(["f(H) = (2H / H<sub>rms</sub>²) · exp[−(H/H<sub>rms</sub>)²]          F(H) = P(H ≤ H*) = 1 − exp[−(H/H<sub>rms</sub>)²]",
      "<b>Probabilidad de excedencia:</b>  P(H &gt; H*) = exp[−(H*/H<sub>rms</sub>)²]   →   <b>H<sub>q</sub> = H<sub>rms</sub>·√(−ln q)</b>"])
terms([
    ("f(H)", "Densidad de probabilidad de las alturas de ola [1/m]"),
    ("F(H)", "Probabilidad de que una ola tenga altura ≤ H"),
    ("H", "Altura de ola (variable) [m]"),
    ("H*", "Altura umbral concreta que se estudia [m]"),
    ("H<sub>rms</sub>", "Altura media cuadrática: único parámetro de Rayleigh [m]"),
    ("P(H &gt; H*)", "Probabilidad de excedencia: fracción de olas más altas que H*"),
    ("q", "Probabilidad de excedencia elegida (tanto por uno)"),
    ("H<sub>q</sub>", "Altura superada solo por la fracción q de las olas [m]"),
    ("ln q", "Logaritmo neperiano de q (negativo, por eso −ln q &gt; 0)"),
    ("Banda estrecha", "Energía concentrada en un rango estrecho de periodos (swell)"),
])
table(["Relación (Rayleigh)", "Valor", "Relación", "Valor"], [
    ["H<sub>m</sub> / H<sub>rms</sub>", "0,886 (= √π/2)", "H<sub>1/3</sub> / H<sub>m</sub>", "1,597"],
    ["H<sub>1/3</sub> / H<sub>rms</sub>", "<b>1,416</b>", "H<sub>1/3</sub> / η<sub>rms</sub>", "4,004 (→ H<sub>m0</sub> ≈ 4√m<sub>0</sub>)"],
    ["H<sub>1/10</sub> / H<sub>rms</sub>", "1,800", "H<sub>1/10</sub> / H<sub>1/3</sub>", "1,271"],
    ["H<sub>1/100</sub> / H<sub>rms</sub>", "2,359", "H<sub>rms</sub> / η<sub>rms</sub>", "2√2 ≈ 2,83"],
], [40, 45, 40, 45])
terms([
    ("H<sub>1/10</sub>, H<sub>1/100</sub>", "Media de la décima y de la centésima parte de olas más altas [m]"),
    ("η<sub>rms</sub>", "Desviación típica de la superficie libre [m]"),
    ("H<sub>m0</sub>", "Altura significante espectral = 4√m<sub>0</sub> [m] (se ve el martes)"),
    ("m<sub>0</sub>", "Momento espectral de orden 0 = varianza de η = η<sub>rms</sub>² [m²]"),
])
P("También se escribe en función de H<sub>m</sub>: F(H) = 1 − exp[−(π/4)(H/H<sub>m</sub>)²], o de H<sub>s</sub>: F(H) = 1 − exp[−2,005(H/H<sub>s</sub>)²].")
terms([
    ("H<sub>m</sub>", "Altura media [m]"),
    ("H<sub>s</sub>", "Altura significante (= H<sub>1/3</sub>) [m]"),
    ("π/4 y 2,005", "Constantes que salen de sustituir H<sub>rms</sub> por H<sub>m</sub>/0,886 o por H<sub>s</sub>/1,416"),
])
P("Ejemplo (diapos 35–37): altura superada solo por el 2 % de las olas con H<sub>rms</sub> = 3 m: H<sub>2%</sub> = 3·√(−ln 0,02) = 3·1,978 = <b>5,93 m</b>.")

h2("5. Altura de ola máxima en un estado de mar")
bl("Olas independientes (Longuet-Higgins, 1952):")
fbox(["F(H<sub>max,N</sub>) = [F(H)]<super>N</super> = {1 − exp[−(H<sub>max</sub>/H<sub>rms</sub>)²]}<super>N</super>"])
terms([
    ("F(H<sub>max,N</sub>)", "Probabilidad de que la mayor de N olas no supere H<sub>max</sub>"),
    ("[F(H)]<super>N</super>", "Producto de N probabilidades iguales: todas las N olas por debajo (por eso exige olas independientes)"),
    ("N", "Número de olas del estado de mar"),
    ("H<sub>max</sub>", "Altura máxima [m]"),
    ("H<sub>rms</sub>", "Altura media cuadrática [m]"),
])
P("<b>Más olas (más duración) → más probable una ola mayor.</b> Para N &gt; 100, con C = 0,57722 (Euler):")
fbox(["<b>Moda (más probable):</b>  H<sub>max,moda</sub> / H<sub>rms</sub> = √(ln N)",
      "<b>Media:</b>  H<sub>max,media</sub> / H<sub>rms</sub> = √(ln N) + (C/2)·(ln N)<super>−1/2</super>"])
terms([
    ("H<sub>max,moda</sub>", "Valor más probable de la ola máxima [m]"),
    ("H<sub>max,media</sub>", "Valor medio (esperado) de la ola máxima [m]; algo mayor que la moda"),
    ("ln N", "Logaritmo neperiano del número de olas"),
    ("C", "Constante de Euler-Mascheroni = 0,57722"),
    ("(ln N)<super>−1/2</super>", "1/√(ln N)"),
])
table(["N", "100", "500", "1000", "2000", "5000"], [
    ["H<sub>max,moda</sub>/H<sub>rms</sub> (moda)", "2,146", "2,493", "2,628", "2,757", "2,918"],
    ["H<sub>max,media</sub>/H<sub>rms</sub> (media)", "2,280", "2,609", "2,738", "2,862", "3,017"],
    ["H<sub>max,moda</sub>/H<sub>s</sub> (moda)", "1,516", "1,761", "1,857", "1,948", "2,062"],
], [50, 24, 24, 24, 24, 24])
P("Regla rápida de diseño: en un estado de mar de 1–3 h, <b>H<sub>max</sub> ≈ 1,8–2·H<sub>s</sub></b>.")
h3("Ejemplo de la diapo 42 (el que tienes que rehacer)")
P("«H<sub>max</sub> más probable en un estado de mar de 1 h (3600 s), T<sub>m</sub> = 7,2 s y H<sub>rms</sub> = …»")
bl("N = 3600/7,2 = <b>500 olas</b>; ln 500 = 6,215.",
   "Moda: √6,215 = <b>2,493</b>. Media: 2,493 + 0,2886/2,493 = <b>2,609</b> (la diapo pone 2,61).",
   "Con <b>H<sub>rms</sub> = 3 m</b> (los datos de la solución): moda <b>7,48 m</b>; media 7,83 m (resultado de la diapo).",
   "Con <b>H<sub>rms</sub> = 5 m</b> (lo que dice el enunciado): moda <b>12,46 m</b>; media 13,04 m.")
terms([
    ("3600 s", "Duración del estado de mar (1 h)"),
    ("T<sub>m</sub> = 7,2 s", "Periodo medio"),
    ("N = duración/T<sub>m</sub>", "Número de olas que caben en el estado de mar"),
    ("0,2886", "C/2 = 0,57722/2"),
])
note("<b>Dos erratas en esta diapo:</b> (1) el enunciado dice H<sub>rms</sub> = 5 y la solución usa 3 m; (2) pregunta la <b>más probable</b> (moda, √ln N = 2,493) "
     "pero calcula la <b>media</b> (2,61). En el examen: lee qué piden y escribe la fórmula que usas. Si dudas, da las dos.")
h3("Límites de Rayleigh y otras distribuciones")
bl("Rayleigh <b>sobrestima</b> la probabilidad de las olas mayores (hasta ≈ 10 % en la cola). Causas: supone <b>banda estrecha</b> (falla con sea), <b>independencia</b> entre olas "
   "(hay correlación entre olas sucesivas: grupos) y <b>no considera no linealidades</b> (asimetrías en oleajes extremos, proximidad a rotura, rompientes).",
   "<b>Distribución conjunta H–T</b> de Longuet-Higgins (1975, 1983): depende de la anchura espectral ν² = m<sub>0</sub>m<sub>2</sub>/m<sub>1</sub>² − 1; la moda de los periodos decrece al aumentar ν.")
terms([
    ("ν", "Anchura espectral (adimensional): 0 → banda estrecha (swell); grande → banda ancha (sea)"),
    ("m<sub>0</sub>, m<sub>1</sub>, m<sub>2</sub>", "Momentos espectrales de orden 0, 1 y 2: m<sub>n</sub> = ∫ fⁿ·S(f) df (se ven el martes)"),
    ("S(f)", "Espectro de energía del oleaje [m²/Hz]"),
])
bl("<b>Freak/rogue waves</b>: olas anormales, muy peraltadas y mucho más altas que las de alrededor. Criterio de Haver (2000): <b>H<sub>max</sub>/H<sub>s</sub> &gt; 2</b> y/o "
   "<b>η<sub>max</sub>/H<sub>s</sub> &gt; 1,25</b>. Origen: concentración por interacción entre frecuencias, interacción ola–corriente e inestabilidades no lineales. "
   "Más probables en mares peraltados y de banda estrecha (en periodo o dirección); en sitios concretos se ha visto una cada ≈ 8 días.")
terms([
    ("H<sub>max</sub>", "Altura de la ola candidata (de seno a cresta) [m]"),
    ("H<sub>s</sub>", "Altura significante del estado de mar en que aparece [m]"),
    ("η<sub>max</sub>", "Altura de su cresta sobre el nivel medio [m]"),
])

h2("6. Ejercicios para hoy (intenta 10 min antes de mirar)")
bl("<b>E1.</b> Estado de mar de 3 h con H<sub>s</sub> = 4 m y T<sub>m</sub> = 8 s. (a) H<sub>rms</sub>, H<sub>m</sub> y H<sub>1/10</sub>; (b) altura superada por el 1 % de las olas; "
   "(c) cuántas olas superan 5 m; (d) H<sub>max</sub> más probable; (e) ¿sería freak una ola de 8,5 m?",
   "<b>E2.</b> En el registro de 22 olas, ¿cuántas superan 1 m según Rayleigh con H<sub>rms</sub> = 0,69 m? Compáralo con las que hay realmente (4). ¿Qué te dice?",
   "<b>E3.</b> ¿Qué fracción de olas supera la altura significante? (Rayleigh)")
table(["", "Solución"], [
    ["E1", "H<sub>rms</sub> = 4/1,416 = 2,82 m; H<sub>m</sub> = 0,886·2,82 = 2,50 m; H<sub>1/10</sub> = 1,800·2,82 = 5,08 m. H<sub>1%</sub> = 2,82·√(ln 100) = 6,06 m. "
           "N = 10 800/8 = 1350; P(H &gt; 5) = exp[−(5/2,82)²] = 0,044 → ≈ 59 olas. H<sub>max,moda</sub> = 2,82·√(ln 1350) = 2,82·2,686 = 7,58 m (≈ 1,9H<sub>s</sub>). "
           "8,5/4 = 2,1 &gt; 2 → sí, por el criterio de Haver."],
    ["E2", "P(H &gt; 1) = exp[−(1/0,69)²] ≈ 0,12 → 22·0,12 ≈ 2,7 olas, frente a 4 reales. Con 22 olas la estadística no es fiable (hace falta ≥ 100): por eso se piden registros largos."],
    ["E3", "P(H &gt; H<sub>s</sub>) = exp(−1,416²) = 0,135 ≈ 13,5 %."],
], [14, 156])
terms([
    ("10 800 s", "3 h expresadas en segundos"),
    ("√(ln 100)", "√(−ln 0,01): para q = 1 %, −ln q = ln(1/q) = ln 100"),
    ("P(H &gt; 5)", "Fracción de olas que superan 5 m; × N da el número de olas"),
    ("1,416", "H<sub>s</sub>/H<sub>rms</sub> de Rayleigh: por eso P(H &gt; H<sub>s</sub>) = exp(−1,416²)"),
])

h2("7. Autoexamen (15 min, en voz alta o por escrito)")
table(["Pregunta", "Respuesta corta"], [
    ["¿Estocástico, estacionario, ergódico?", "Aleatorio · momentos invariantes en el tiempo (estado de mar) · una muestra representa al proceso"],
    ["¿Por qué gaussiano?", "Teorema central del límite: suma de muchas ondas independientes"],
    ["¿Cuánto dura un estado de mar?", "1 h habitual; mínimo 20–30 min"],
    ["¿Qué es una ola en el análisis PAC?", "El tramo entre dos pasos ascendentes por cero consecutivos"],
    ["¿Cuántas olas para estadística fiable?", "≥ 100; recomendable 1000"],
    ["Define H<sub>1/3</sub>", "Media del tercio de olas más altas"],
    ["¿Cuándo vale Rayleigh?", "Banda estrecha (swell), olas independientes, oleaje lineal en indefinidas"],
    ["H<sub>1/3</sub> en función de H<sub>rms</sub>", "1,416·H<sub>rms</sub>"],
    ["H<sub>max</sub> más probable en N olas", "H<sub>rms</sub>√(ln N)"],
    ["¿Qué es una freak wave?", "H<sub>max</sub>/H<sub>s</sub> &gt; 2 o η<sub>max</sub>/H<sub>s</sub> &gt; 1,25 (Haver)"],
    ["¿Qué indican sesgo y curtosis ≠ 0?", "No linealidad (crestas peraltadas, reducidas)"],
], [70, 100])

build(sys.argv[1], "Oceanografía (83000111) · Resumen Día 3 — Tema 2: Análisis estadístico del oleaje", "Resumen Día 3 - Análisis estadístico")
