import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from estilo import *
from figuras import eta_figure

# ---------------------------------------------------------------- portada
P("Oceanografía · Día 2", H1)
P("Tema 2 — Oleaje: Mecánica de ondas (teoría lineal) + ejercicios 1–5 de teoría de ondas · 1er parcial 28/10/2026", SUB)

h2("0. Plan del día")
P("Hoy es el día más importante para el <b>40 % de ejercicios</b>: todo el bloque de problemas de teoría de ondas sale de aquí. "
  "Orden recomendado (≈ 5 h netas):")
table(["Bloque", "Qué hacer", "Tiempo"], [
    ["A", "Secciones 1–4: magnitudes, parámetros adimensionales, regímenes y teorías.", "1 h"],
    ["B", "Secciones 5–7: planteamiento, teoría lineal, <b>ecuación de la dispersión</b>, velocidades, órbitas y presiones.", "1 h 30"],
    ["C", "Secciones 8–9: superposición (estacionaria, cuasi-estacionaria, grupos, corriente) y energía.", "1 h"],
    ["D", "Sección 10: haz los ejercicios 1–5 <b>a mano, con calculadora y sin mirar la solución</b>. Luego compara.", "1 h 30"],
    ["E", "Mazo Anki del Día 2 (y repaso rápido del Día 1).", "20 min"],
], [16, 136, 18])
note("<b>Lo que no puedes salir de hoy sin saber:</b> (1) clasificar por h/L, (2) resolver ω² = gk·tanh(kh) con la calculadora, "
     "(3) las órbitas elípticas (semiejes), (4) envolvente de la cuasi-estacionaria → H<sub>i</sub> y H<sub>r</sub>, "
     "(5) grupos: C<sub>g</sub> = Δω/Δk = nC, (6) E = ρgH²/8 y F = E·C<sub>g</sub>.")
h3("Símbolos que se usan en todo el tema")
terms([
    ("η", "Superficie libre: elevación del agua respecto al nivel en reposo [m] (ver figura de la sección 2)"),
    ("h", "Profundidad: del nivel en reposo al fondo [m]"),
    ("H", "Altura de ola: de seno a cresta [m]"),
    ("a (A)", "Amplitud = H/2 en teoría lineal [m]"),
    ("L", "Longitud de onda [m]"),
    ("T", "Periodo [s]"),
    ("f", "Frecuencia = 1/T [Hz]"),
    ("k", "Número de onda = 2π/L [rad/m]"),
    ("ω", "Frecuencia angular = 2π/T [rad/s]"),
    ("C", "Celeridad (velocidad de fase) = L/T [m/s]"),
    ("C<sub>g</sub>", "Celeridad de grupo: velocidad de la energía [m/s]"),
    ("x, z", "x: dirección de avance; z: vertical, 0 en el nivel en reposo, positiva hacia arriba (fondo en z = −h) [m]"),
    ("t", "Tiempo [s]"),
    ("θ", "Fase = kx − ωt [rad] (en incidencia oblicua θ también es el ángulo de propagación)"),
    ("u, w", "Velocidad horizontal y vertical del agua [m/s]"),
    ("φ", "Potencial de velocidades: u = ∂φ/∂x, w = ∂φ/∂z [m²/s]"),
    ("p", "Presión [Pa]"),
    ("ρ", "Densidad del agua de mar ≈ 1025 kg/m³"),
    ("g", "Gravedad = 9,81 m/s²"),
    ("L<sub>0</sub>, C<sub>0</sub>", "Longitud y celeridad en profundidades indefinidas"),
], title="Glosario (cada ecuación lleva además su propia leyenda)")

# ---------------------------------------------------------------- 1
h2("1. Ondas frente a oleaje")
bl("<b>Oleaje real</b>: aleatorio e irregular → se trata con estadística y espectros (días 3–4).",
   "<b>Onda</b>: modelo matemático determinista; oscilación uniforme y periódica de la superficie (oleaje regular, monocromático) → <b>teoría de ondas</b> (hoy).",
   "En ingeniería costera/offshore importan las <b>ondas gravitatorias generadas por el viento: T ≈ 3–30 s</b>.")
h3("Tipos de ondas en el océano (de corto a largo periodo)")
table(["Tipo", "Periodo / L", "Genera", "Restaura / controla", "Ejemplo"], [
    ["Capilares", "0,1 s / 10⁻² m", "Viento", "Tensión superficial + gravedad", "Rizado"],
    ["Ultragravitatorias", "0,1–1 s / 10⁰ m", "Viento", "Fricción, gravedad", "Olas en una charca"],
    ["<b>Gravitatorias</b>", "<b>1–30 s / 1–10³ m</b>", "Viento", "Fricción, gravedad", "<b>Sea y swell</b>"],
    ["Infragravitatorias", "30–300 s", "Viento y ondas gravitatorias", "+ Coriolis", "Ondas de borde"],
    ["Ondas largas", "≈ 5 min / 10⁵–10⁶ m", "Borrascas, terremotos", "+ Coriolis", "Tsunamis, seiches"],
    ["Marea astronómica", "12–24 h / 10⁷ m", "Sistema Tierra-Luna-Sol", "+ Coriolis", "Marea"],
    ["Internas", "1 min–25 h", "Borrascas, ondas de gravedad", "+ Coriolis", "En la picnoclina"],
], [30, 32, 38, 38, 32])
bl("<b>¿Por qué «gravitatoria»?</b> Porque la fuerza restauradora dominante es la gravedad. Si L es de pocos cm, domina la tensión superficial → <b>capilar</b>.",
   "<b>Crecimiento del oleaje</b>: depende de la velocidad del viento (debe superar la de las crestas), su <b>duración</b>, el <b>fetch</b> (distancia libre) y la profundidad. "
   "Con pérdidas por fricción y rotura se llega a un equilibrio: <b>oleaje completamente desarrollado</b>.",
   "<b>Swell (mar de fondo)</b>: olas generadas lejos; más ordenadas, periodo más estable que el <i>sea</i> local.")

# ---------------------------------------------------------------- 2
h2("2. Magnitudes características")
table(["Magnitud", "Definición / fórmula"], [
    ["Altura H", "Distancia vertical cresta–seno: H = A<sub>c</sub> + A<sub>s</sub>. Solo si A<sub>c</sub> = A<sub>s</sub> → <b>H = 2a</b> (teoría lineal)."],
    ["Periodo T", "Tiempo en que se repite un punto idéntico en una posición fija."],
    ["Longitud L", "Distancia horizontal mínima entre dos puntos idénticos sucesivos."],
    ["Número de onda k", "k = 2π / L  [m⁻¹]"],
    ["Frecuencia angular ω", "ω = 2πf = 2π / T  [rad/s]"],
    ["Celeridad C", "C = L / T = ω / k (velocidad de fase)"],
    ["Niveles", "Nivel en reposo (SWL) ≠ nivel medio (MWL) cuando hay oleaje o corriente. En teoría lineal coinciden."],
], [34, 136])
terms([
    ("A<sub>c</sub>, A<sub>s</sub>", "Amplitud de cresta y de seno, medidas desde el nivel medio [m]"),
    ("a", "Amplitud de la onda lineal = H/2 [m]"),
    ("f", "Frecuencia: ciclos por segundo [Hz]"),
    ("2π", "Radianes de un ciclo completo: convierte ciclos en radianes"),
])
bl("Ejes: x en la dirección de propagación, z desde el nivel en reposo y positivo hacia arriba (el fondo está en z = −h).",
   "<b>Incidencia oblicua</b> (ángulo α con el eje x): L<sub>x</sub> = L/cos α, L<sub>y</sub> = L/sin α; k<sub>x</sub> = k cos α, k<sub>y</sub> = k sin α; "
   "|k| = √(k<sub>x</sub>² + k<sub>y</sub>²); α = arctan(k<sub>y</sub>/k<sub>x</sub>).")
terms([
    ("α", "Ángulo entre la dirección de avance de la ola y el eje x [rad o °]"),
    ("L<sub>x</sub>, L<sub>y</sub>", "Distancia entre crestas medida a lo largo del eje x y del eje y [m]"),
    ("k<sub>x</sub>, k<sub>y</sub>", "Componentes del vector número de onda en x e y [rad/m]"),
    ("|k|", "Módulo del vector número de onda (= 2π/L) [rad/m]"),
])
h3("Qué es η (superficie libre)")
figure(eta_figure(440), "η es la distancia vertical entre el nivel en reposo (línea discontinua) y la superficie del agua en cada punto x y en cada "
       "instante t: positiva bajo las crestas (+H/2 en la cresta), negativa en los senos (−H/2) y nula en los pasos por cero. "
       "h (profundidad) y H (altura de ola) son fijos; η cambia al pasar la ola.")
fbox(["<b>Progresiva:</b>  η(x,t) = a·cos(kx − ωt)   (espacio y tiempo acoplados → avanza)",
      "<b>Estacionaria:</b>  η(x,t) = a·cos(kx)·cos(ωt)   (desacoplados → oscila entre nodos fijos)"])
terms([
    ("η(x,t)", "Elevación de la superficie en el punto x y el instante t [m]"),
    ("a", "Amplitud [m] (en la estacionaria es la amplitud máxima, en los antinodos)"),
    ("k", "Número de onda = 2π/L [rad/m]"),
    ("ω", "Frecuencia angular = 2π/T [rad/s]"),
    ("x, t", "Posición horizontal [m] y tiempo [s]"),
    ("kx − ωt", "Fase: el signo − indica que la onda avanza hacia x positivas"),
])
P("En la estacionaria, <b>nodo y antinodo contiguos están a L/4</b> (dos nodos seguidos a L/2). Esto se usa en el ejercicio 4.")

# ---------------------------------------------------------------- 3
h2("3. Parámetros adimensionales")
table(["Parámetro", "Fórmula", "Qué mide"], [
    ["Peralte ε", "ε = H/L  (o ka, kH)", "Movimiento vertical en una longitud de onda → linealidad"],
    ["Altura relativa δ", "δ = H/h  (o a/h)", "Oscilación vertical frente a la profundidad"],
    ["Profundidad relativa μ", "μ = h/L  (o kh)", "Cuánto penetra el movimiento → si la onda «siente» el fondo (dispersividad)"],
    ["Número de Ursell", "U<sub>r</sub> = H·L² / h³ = δ/μ²", "Régimen y teoría adecuada (lineal si U<sub>r</sub> pequeño; umbral ≈ 26)"],
    ["Peralte «de periodo»", "H / gT²", "Linealidad (eje vertical del ábaco de Le Méhauté)"],
    ["Prof. «de periodo»", "h / gT²", "Profundas / intermedias / someras (eje horizontal de Le Méhauté)"],
], [36, 46, 88])
terms([
    ("ε", "Peralte (adimensional): H/L, o también ka o kH según el autor"),
    ("δ", "Altura relativa (adimensional): H/h"),
    ("μ", "Profundidad relativa (adimensional): h/L, o kh"),
    ("U<sub>r</sub>", "Número de Ursell (adimensional) = HL²/h³"),
    ("H, L, h", "Altura de ola, longitud de onda y profundidad [m]"),
    ("g, T", "Gravedad [m/s²] y periodo [s]; gT² tiene unidades de longitud"),
])
h3("Clasificación por profundidad relativa — la tabla que más se usa")
table(["Zona", "h/L", "kh", "Qué pasa"], [
    ["<b>Indefinidas</b> (profundas)", "h/L > 1/2", "kh > π", "No siente el fondo: L y C dependen solo de T."],
    ["<b>Intermedias</b>", "1/20 < h/L < 1/2", "π/10 < kh < π", "Empieza a notar el fondo: L y C dependen de T y h."],
    ["<b>Reducidas</b> (someras)", "h/L < 1/20", "kh < π/10", "Gobernada por el fondo: C solo depende de h."],
], [38, 30, 30, 72])
terms([
    ("h/L", "Profundidad relativa: cuántas longitudes de onda caben en la profundidad"),
    ("kh", "Lo mismo multiplicado por 2π (kh = 2πh/L)"),
])
bl("H/L ≪ 1 → onda de <b>pequeña amplitud</b> (lineal). H/L ≈ 1 → amplitud finita (no lineal).",
   "<b>Peralte máximo antes de rotura en profundas: H/L = 0,142 ≈ 1/7.</b>")
h3("Ejemplo de clase (tres oleajes) — fíjate en cómo se razona")
table(["Oleaje", "T (s)", "h (m)", "H (m)", "L (m)", "h/L", "H/L", "H/h", "U<sub>r</sub>", "Zona → teoría"], [
    ["1 Swell oceánico", "14", "200", "4,0", "305,9", "0,654", "0,0131", "0,020", "0,047", "Indefinidas → lineal"],
    ["2 Plataforma (eólico)", "10", "15", "2,5", "109,1", "0,137", "0,0229", "0,167", "8,81", "Intermedias → lineal (cerca del límite)"],
    ["3 Antes de rompientes", "12", "3", "1,5", "64,2", "0,047", "0,0234", "0,500", "228,9", "Reducidas → cnoidal"],
], [27, 10, 11, 11, 13, 13, 14, 12, 13, 46])
bl("<b>Órbitas</b>: 1 casi circulares que se apagan antes del fondo; 2 elípticas, el semieje vertical decrece mucho con z; 3 muy achatadas, la componente horizontal casi uniforme en la vertical.",
   "<b>Simetría cresta–seno</b>: 1 sinusoidal simétrica; 2 ligera asimetría (crestas algo más picudas); 3 crestas altas y estrechas, senos largos y planos (→ onda solitaria cuando U<sub>r</sub> → ∞).")

# ---------------------------------------------------------------- 4
h2("4. Regímenes y teorías de ondas")
table(["Régimen", "Condición", "Teorías"], [
    ["<b>Stokes</b> (L no muy grande frente a h)", "h/L o kh ≥ 1 → indefinidas e intermedias",
     "Si δ ≪ 1 o ε ≪ 1 → <b>teoría lineal = Airy = Stokes 1er orden</b>. Si ε crece → Stokes II, III…"],
    ["<b>Onda larga</b> (L ≫ h)", "kh ≪ 1 → reducidas", "Cnoidal, onda solitaria, ondas largas (no lineales)"],
], [44, 52, 74])
P("El <b>ábaco de Le Méhauté</b> sitúa el oleaje con x = h/gT² e y = H/gT² y te dice la teoría. En el examen basta con saber leerlo y razonar como en el ejemplo anterior.")
terms([
    ("x = h/gT²", "Eje horizontal del ábaco: profundidad adimensionalizada con el periodo"),
    ("y = H/gT²", "Eje vertical del ábaco: altura de ola adimensionalizada con el periodo"),
])

# ---------------------------------------------------------------- 5
h2("5. Planteamiento del problema (teoría potencial)")
h3("Hipótesis — pregunta de teoría típica")
bl("Fluido continuo, homogéneo, <b>incompresible</b> (ρ cte) y <b>no viscoso</b> (Re ≈ UL/ν ≈ 10⁸ lejos de contornos).",
   "Única fuerza de volumen: la <b>gravedad</b>. Se desprecian <b>tensión superficial</b> y <b>Coriolis</b> (≈ 1000 veces menor que la inercia; T de la ola ≪ rotación terrestre).",
   "Presión en superficie uniforme y constante (p<sub>a</sub> = 0). Flujo <b>irrotacional</b> (∇×u = 0). Fondo impermeable.")
terms([
    ("Re", "Número de Reynolds = UL/ν (adimensional): inercia frente a viscosidad"),
    ("U", "Velocidad característica del agua ≈ 1 m/s"),
    ("L", "Longitud característica (longitud de onda) ≈ 100 m"),
    ("ν", "Viscosidad cinemática del agua ≈ 10⁻⁶ m²/s"),
    ("p<sub>a</sub>", "Presión atmosférica, que se toma como referencia (= 0)"),
    ("∇×u", "Rotacional del campo de velocidades (vorticidad); = 0 → irrotacional"),
])
P("Irrotacional ⇒ existe un <b>potencial de velocidades φ</b> con u = ∇φ. Con incompresibilidad, la continuidad queda:")
fbox(["<b>Ecuación de Laplace:</b>  ∇²φ = ∂²φ/∂x² + ∂²φ/∂z² = 0",
      "<b>Bernoulli no estacionario:</b>  ∂φ/∂t + ½|∇φ|² + p/ρ + gz = C(t)"])
terms([
    ("φ", "Potencial de velocidades [m²/s]; su gradiente da la velocidad: u = ∂φ/∂x, w = ∂φ/∂z"),
    ("∇²φ", "Laplaciano de φ: suma de segundas derivadas. = 0 equivale a continuidad (conservación de masa)"),
    ("∂/∂x, ∂/∂z, ∂/∂t", "Derivadas parciales respecto a x, z y t"),
    ("∂φ/∂t", "Término no estacionario (cambio del potencial en el tiempo) [m²/s²]"),
    ("½|∇φ|²", "Energía cinética por unidad de masa = ½(u² + w²) [m²/s²]"),
    ("p/ρ", "Término de presión por unidad de masa [m²/s²]"),
    ("gz", "Energía potencial gravitatoria por unidad de masa [m²/s²]"),
    ("C(t)", "Constante de Bernoulli: solo depende del tiempo; se puede tomar = 0"),
])
P("Ventajas: todas las condiciones de contorno se escriben en φ y el problema se reduce a dos incógnitas (p, φ). Desventaja: solo vale para fluido no viscoso.")
table(["Condición de contorno", "Expresión (fondo plano)", "Significado"], [
    ["Cinemática en el fondo", "∂φ/∂z = 0 en z = −h", "No hay flujo a través del fondo impermeable."],
    ["Cinemática en superficie libre", "∂η/∂t + u·∂η/∂x = w en z = η", "La partícula de la superficie sigue en ella (DF/Dt = 0 con F = z − η)."],
    ["Dinámica en superficie libre", "Bernoulli con p = p<sub>a</sub> = 0 en z = η", "Balance de presiones en la interfaz."],
    ["Laterales", "φ(x+L) = φ(x)", "Periodicidad espacial (o ∂φ/∂x = 0 si hay pared en x = 0)."],
    ["Temporal", "φ(t+T) = φ(t)", "Periodicidad en el tiempo."],
], [42, 56, 72])
terms([
    ("∂φ/∂z = w", "Velocidad vertical del agua; en el fondo plano tiene que ser 0"),
    ("∂η/∂t", "Velocidad a la que sube o baja la superficie en un punto fijo [m/s]"),
    ("u·∂η/∂x", "Corrección porque la partícula también se mueve en horizontal (a velocidad u) sobre una superficie inclinada (pendiente ∂η/∂x)"),
    ("w", "Velocidad vertical del agua en la superficie [m/s]"),
    ("F = z − η", "Función que vale 0 justo en la superficie libre; DF/Dt = 0 dice que la partícula no la abandona"),
    ("D/Dt", "Derivada material: siguiendo a la partícula (∂/∂t + u·∂/∂x + w·∂/∂z)"),
    ("p = p<sub>a</sub>", "En la superficie la presión del agua es la atmosférica"),
    ("φ(x+L) = φ(x)", "El movimiento se repite cada longitud de onda L"),
    ("φ(t+T) = φ(t)", "El movimiento se repite cada periodo T"),
])
P("<b>¿Por qué es difícil?</b> Las condiciones se imponen en η, que es incógnita, y tienen términos cuadráticos → problema <b>no lineal</b>. "
  "La teoría lineal lo arregla suponiendo pequeña amplitud (H/L ≪ 1, H/h ≪ 1): se imponen en <b>z = 0</b> y se tiran los productos de términos pequeños.")

# ---------------------------------------------------------------- 6
h2("6. Teoría lineal (Airy) y ecuación de la dispersión")
P("Ventajas: es la más sencilla, SWL = MWL, da soluciones analíticas y permite <b>superponer</b> (base del oleaje irregular). "
  "Se resuelve por <b>separación de variables</b>, φ = X(x − Ct)·Z(z) → X'' + k²X = 0 (senos/cosenos) y Z'' − k²Z = 0 (exponenciales → cosh con la condición del fondo).")
terms([
    ("X(x − Ct)", "Parte horizontal del potencial: depende de la posición respecto a la onda que avanza"),
    ("Z(z)", "Parte vertical del potencial: cómo cambia con la profundidad"),
    ("X'', Z''", "Segundas derivadas de X y de Z"),
    ("k²", "Constante de separación (resulta ser el número de onda al cuadrado)"),
])
fbox(["η = a·cos(kx − ωt),   a = H/2",
      "φ = (ag/ω) · [cosh k(z+h) / cosh kh] · sin(kx − ωt)   (el signo depende del convenio u = ±∇φ)"])
terms([
    ("η", "Superficie libre [m]"),
    ("a", "Amplitud = H/2 [m]"),
    ("φ", "Potencial de velocidades [m²/s]"),
    ("g", "Gravedad [m/s²]"),
    ("ω", "Frecuencia angular [rad/s]"),
    ("k", "Número de onda [rad/m]"),
    ("cosh k(z+h)", "Atenuación con la profundidad: z + h es la distancia del punto al fondo"),
    ("cosh kh", "Normaliza para que en superficie (z = 0) el cociente valga 1"),
    ("kx − ωt", "Fase de la onda progresiva"),
])
note("Las transparencias mezclan el signo del potencial (u = ∇φ en un sitio y −∂φ/∂z en otro). No te líes: lo que se pregunta son los "
     "resultados de velocidades, presiones y dispersión, que son los de las secciones 6–7.")
P("Imponiendo la condición cinemática de superficie a esa solución sale la <b>ecuación de la dispersión</b>, la que más vas a usar:")
fbox(["<b>ω² = g·k·tanh(kh)</b>",
      "L = (gT²/2π)·tanh(2πh/L)        C = (gT/2π)·tanh(kh)        L = L<sub>0</sub>·tanh(kh),  C = C<sub>0</sub>·tanh(kh)"])
terms([
    ("ω", "Frecuencia angular = 2π/T [rad/s]. La fija el periodo de la ola, que no cambia al propagarse"),
    ("g", "Aceleración de la gravedad = 9,81 m/s²"),
    ("k", "Número de onda = 2π/L [rad/m]. Es la incógnita habitual"),
    ("h", "Profundidad: del nivel en reposo al fondo [m]"),
    ("tanh(kh)", "Tangente hiperbólica de kh: vale ≈ 1 en profundas y ≈ kh en reducidas. Mete el efecto del fondo"),
    ("T", "Periodo [s]"),
    ("L", "Longitud de onda [m]"),
    ("C", "Celeridad = L/T = ω/k [m/s]"),
    ("L<sub>0</sub>, C<sub>0</sub>", "Valores en profundidades indefinidas: L<sub>0</sub> = gT²/2π, C<sub>0</sub> = gT/2π"),
])
P("Es <b>trascendente</b> (k aparece dentro y fuera de la tanh): se resuelve con tablas, gráficos o numéricamente (Newton-Raphson).")
h3("Límites asintóticos")
table(["Función", "Indefinidas (kh → ∞)", "Reducidas (kh → 0)"], [
    ["cosh kh", "e<super>kh</super>/2", "1"],
    ["sinh kh", "e<super>kh</super>/2", "kh"],
    ["tanh kh", "1", "kh"],
], [40, 65, 65])
table(["", "Indefinidas", "Reducidas"], [
    ["Dispersión", "ω² = gk", "ω² = gk²h"],
    ["Longitud de onda", "<b>L<sub>0</sub> = gT²/2π = 1,56·T²</b>", "L = T·√(gh)"],
    ["Celeridad", "<b>C<sub>0</sub> = gT/2π = 1,56·T</b>", "<b>C = √(gh)</b>"],
    ["Consecuencia", "Dispersiva: las olas de mayor T viajan más rápido. No hace falta iterar.",
     "No dispersiva: todas las olas van a la misma velocidad, solo depende de h."],
], [34, 68, 68])
terms([
    ("e<super>kh</super>", "Exponencial de kh (crece muy rápido: por eso tanh → 1 en profundas)"),
    ("1,56", "Valor de g/2π = 9,81/6,28 [m/s²]"),
    ("√(gh)", "Celeridad de onda larga: solo depende de la profundidad h [m/s]"),
])
h3("Sentido físico (tablas de clase)")
table(["h = 10 m: T (s)", "2", "6", "12", "18", "24"], [
    ["L (m)", "6,24", "48", "113,3", "174,6", "234,9"], ["C (m/s)", "3,12", "8,0", "9,44", "9,70", "9,79"]],
    [34, 27, 27, 27, 27, 28])
P("A igual h, <b>más T → más L y más C</b> → las olas se separan por frecuencias (<b>dispersión frecuencial</b>). Fíjate en que C tiende a √(gh) = 9,9 m/s.")
table(["T = 10 s: h (m)", "2", "6", "12", "18", "50"], [
    ["L (m)", "43,7", "73,1", "99,7", "116,8", "151,3"], ["C (m/s)", "4,36", "7,36", "9,97", "11,67", "15,13"]],
    [34, 27, 27, 27, 27, 28])
P("A igual T, <b>menos h → menos L y menos C</b>. Ese frenado al llegar a costa es el origen de la <b>refracción</b>.")
h3("Cómo resolver la dispersión en el examen")
bl("<b>Calculadora con SOLVE</b>: escribe ω² − g·X·tanh(X·h) = 0 y arranca con X = ω²/g. Es lo más rápido.",
   "<b>Newton-Raphson</b> (lo que hace la función de Matlab de clase): f(k) = ω² − gk·tanh(kh); f'(k) = −g·tanh(kh) − g·h·k·sech²(kh); "
   "k<sub>n+1</sub> = k<sub>n</sub> − f/f'; k<sub>0</sub> = ω²/g. Converge en 3–5 iteraciones.",
   "<b>Explícitas</b> (en clase solo se citan; las fórmulas son las de los artículos): "
   "Fenton y McKee (1990), error &lt; 1,5 %: L ≈ L<sub>0</sub>·[tanh((2πh/L<sub>0</sub>)<super>3/4</super>)]<super>2/3</super>. "
   "Guo (2002), error &lt; 0,7 %: kh ≈ (ω²h/g)·[1 − exp(−(ω√(h/g))<super>5/2</super>)]<super>−2/5</super>.",
   "<b>Si te dan L y quieres h o T, no hay que iterar</b>: despeja directamente (ver ejercicios 1 y 2).",
   "Siempre <b>comprueba la zona al final</b> (h/L) para ver si podías haber usado las simplificaciones.")
terms([
    ("f(k), f'(k)", "Función cuyo cero buscas y su derivada respecto a k"),
    ("sech²(kh)", "Secante hiperbólica al cuadrado = 1/cosh²(kh) (derivada de tanh)"),
    ("k<sub>n</sub>, k<sub>n+1</sub>", "Valor de k en la iteración n y en la siguiente"),
    ("k<sub>0</sub> = ω²/g", "Arranque: el k de profundidades indefinidas"),
    ("X", "En la calculadora, la incógnita k"),
    ("L<sub>0</sub>", "Longitud de onda en indefinidas = gT²/2π [m]"),
    ("ω√(h/g)", "Combinación adimensional de frecuencia y profundidad usada en la fórmula de Guo"),
])

# ---------------------------------------------------------------- 7
h2("7. Cinemática, órbitas y presiones (onda progresiva)")
P("Con θ = kx − ωt (fase) y a = H/2:")
fbox(["u = aω · cosh k(h+z) / sinh kh · cos θ           w = aω · sinh k(h+z) / sinh kh · sin θ",
      "a<sub>x</sub> ≈ ∂u/∂t = aω² · cosh k(h+z) / sinh kh · sin θ        a<sub>z</sub> ≈ ∂w/∂t = −aω² · sinh k(h+z) / sinh kh · cos θ"])
terms([
    ("u, w", "Velocidad horizontal y vertical de la partícula de agua [m/s]"),
    ("a<sub>x</sub>, a<sub>z</sub>", "Aceleración horizontal y vertical [m/s²]"),
    ("a", "Amplitud = H/2 [m]"),
    ("ω", "Frecuencia angular [rad/s]"),
    ("k", "Número de onda [rad/m]"),
    ("h", "Profundidad [m]"),
    ("z", "Cota del punto: 0 en el nivel en reposo, −h en el fondo [m]"),
    ("h + z", "Distancia del punto al fondo [m]"),
    ("cosh, sinh", "Funciones hiperbólicas: dan cómo se atenúa el movimiento con la profundidad"),
    ("θ", "Fase = kx − ωt [rad]: θ = 0 bajo la cresta, θ = π bajo el seno"),
])
P("(Se desprecian los términos convectivos: pequeña amplitud.) <b>Propiedades que caen en test:</b>")
bl("Velocidades y aceleraciones ∝ amplitud. <b>u máxima bajo crestas y senos</b> (θ = 0, π); <b>w máxima en los pasos por cero</b> (θ = π/2, 3π/2). u y w desfasadas π/2.",
   "En el fondo (z = −h): <b>w = 0</b> (condición de contorno) pero u ≠ 0 (hay deslizamiento: fluido ideal). a<sub>z</sub> = 0 en el fondo; a<sub>x</sub> no.",
   "Ambas velocidades <b>disminuyen con la profundidad</b> (funciones hiperbólicas de k(h+z)).",
   "a<sub>z</sub> máxima donde u es máxima; a<sub>x</sub> máxima donde w es máxima.",
   "<b>Reducidas</b>: u ≈ (ag/ωh)·cos θ <b>uniforme en la vertical</b>; w crece <b>linealmente</b> de 0 en el fondo al máximo en superficie; u<sub>máx</sub>/w<sub>máx</sub> = 1/kh.")
terms([
    ("ag/ωh", "Amplitud de la velocidad horizontal en reducidas [m/s]: no depende de z"),
    ("u<sub>máx</sub>, w<sub>máx</sub>", "Valores máximos de u y w en la superficie"),
])
h3("Trayectorias de las partículas — elipses (ejercicio 2)")
fbox(["Semieje <b>horizontal (mayor)</b>:  A = a · cosh k(h+z) / sinh kh",
      "Semieje <b>vertical (menor)</b>:  B = a · sinh k(h+z) / sinh kh",
      "<b>B / A = tanh k(h+z)</b>     ·     superficie (z = 0): B = a     ·     fondo (z = −h): B = 0 (vaivén horizontal)"])
terms([
    ("A", "Semieje horizontal (mayor) de la elipse que describe la partícula [m]"),
    ("B", "Semieje vertical (menor) [m]"),
    ("a", "Amplitud de la ola = H/2 [m]"),
    ("k", "Número de onda [rad/m]"),
    ("h + z", "Distancia de la partícula al fondo [m]"),
    ("tanh k(h+z)", "Cociente B/A: 1 en profundas (círculo), → 0 cerca del fondo (segmento)"),
])
table(["Zona", "Forma de la órbita"], [
    ["Indefinidas", "<b>Círculos</b> de radio a·e<super>kz</super>: se reducen exponencialmente; a z = −L/2 el radio es ≈ 4 % del de superficie."],
    ["Intermedias", "<b>Elipses</b> que se achatan hacia el fondo; en el fondo, segmento horizontal."],
    ["Reducidas", "Elipses muy achatadas: A ≈ a/(kh) <b>constante</b> en la vertical; B = a·(1 + z/h) lineal."],
], [30, 140])
terms([
    ("a·e<super>kz</super>", "Radio de la órbita circular en profundas: decae exponencialmente con la profundidad (z &lt; 0)"),
    ("a/(kh)", "Semieje horizontal en reducidas, igual en toda la columna [m]"),
    ("a·(1 + z/h)", "Semieje vertical en reducidas: a en superficie, 0 en el fondo [m]"),
])
h3("Campo de presiones")
fbox(["<b>p = −ρgz + ρg·a·K<sub>p</sub>·cos θ</b>,   con K<sub>p</sub> = cosh k(h+z) / cosh kh  (factor de respuesta de presión, ≤ 1)",
      "Parte hidrostática (−ρgz) + parte dinámica (la de la ola, que se atenúa con la profundidad)"])
terms([
    ("p", "Presión en el punto (manométrica, respecto a la atmosférica) [Pa]"),
    ("ρ", "Densidad del agua ≈ 1025 kg/m³"),
    ("g", "Gravedad [m/s²]"),
    ("z", "Cota del punto (negativa bajo el nivel en reposo) [m]"),
    ("−ρgz", "Presión hidrostática: la que habría sin ola"),
    ("ρg·a·K<sub>p</sub>·cos θ", "Presión dinámica: la que añade (o quita) la ola"),
    ("K<sub>p</sub>", "Factor de respuesta de presión (adimensional, entre 0 y 1)"),
    ("cos θ", "Fase: + bajo la cresta, − bajo el seno"),
])
bl("Por encima del nivel en reposo, bajo la cresta (0 &lt; z &lt; η): p = ρg(η − z) (desarrollo de Taylor).",
   "<b>Reducidas</b>: K<sub>p</sub> = 1 → p = ρg(η − z): <b>ley hidrostática (triangular)</b> respecto a la superficie instantánea.",
   "<b>Indefinidas</b>: p = −ρgz + ρga·e<super>kz</super>·cos θ: hidrostática + dinámica que decae exponencialmente.",
   "Aplicación: un sensor de presión en el fondo «ve» la ola atenuada por 1/cosh kh → hay que corregir con K<sub>p</sub> para obtener η.")
terms([
    ("η", "Superficie libre en ese instante [m]"),
    ("η − z", "Columna de agua real sobre el punto [m]"),
    ("e<super>kz</super>", "Atenuación exponencial con la profundidad (profundas)"),
])

# ---------------------------------------------------------------- 8
h2("8. Soluciones por superposición")
P("Como el problema es lineal, <b>la suma de soluciones es solución</b>. Así se construyen todos estos casos:")
table(["Tipo", "Se compone de", "Características"], [
    ["Estacionaria", "2 progresivas", "Misma dirección, sentido opuesto, misma H → <b>reflexión perfecta</b>"],
    ["Cuasi-estacionaria", "2 progresivas", "Misma dirección, sentido opuesto, H<sub>r</sub> &lt; H<sub>i</sub> → <b>reflexión parcial</b>"],
    ["Crestas cortas", "2 progresivas", "Distinta dirección (±θ), mismo sentido"],
    ["Grupos", "2 progresivas", "Misma dirección y sentido, <b>frecuencias ligeramente distintas</b>"],
    ["Oleaje irregular", "N progresivas", "Amplitudes, periodos, direcciones y fases distintos (aleatorios)"],
    ["Onda + corriente", "Progresiva + corriente uniforme", "Mismo o distinto sentido"],
], [34, 46, 90])
h3("Onda estacionaria (reflexión total en un dique vertical)")
fbox(["η = 2a · cos(kx) · cos(ωt)     → altura <b>doble</b> que la incidente (H<sub>est</sub> = 2H<sub>i</sub>)"])
terms([
    ("2a", "Amplitud máxima (en los antinodos): el doble de la de cada onda progresiva [m]"),
    ("cos(kx)", "Forma en el espacio: fija dónde están nodos y antinodos"),
    ("cos(ωt)", "Oscilación en el tiempo (todos los puntos suben y bajan a la vez)"),
    ("H<sub>est</sub>, H<sub>i</sub>", "Altura de la estacionaria y de la onda incidente [m]"),
])
bl("<b>Nodos</b> (sin movimiento vertical): kx = (2n+1)·π/2. <b>Antinodos</b> (oscilación máxima): kx = nπ.",
   "u máxima en los <b>nodos</b> y nula en los antinodos; w máxima en los <b>antinodos</b> y nula en los nodos.",
   "La dispersión es la misma que la de la progresiva (no cambian las condiciones de superficie).")
terms([
    ("n", "Número entero (0, 1, 2…) que numera los nodos o antinodos"),
    ("kx = (2n+1)π/2", "Posiciones donde cos(kx) = 0 → nodos"),
    ("kx = nπ", "Posiciones donde |cos(kx)| = 1 → antinodos"),
])
h3("Onda cuasi-estacionaria (reflexión parcial) — ejercicio 4")
fbox(["η = (H<sub>i</sub>/2)·cos(kx − ωt) + (H<sub>r</sub>/2)·cos(kx + ωt + ε)",
      "Envolvente:  η<sub>máx</sub> = ½(H<sub>i</sub> + H<sub>r</sub>) en antinodos      η<sub>mín</sub> = ½(H<sub>i</sub> − H<sub>r</sub>) en cuasi-nodos",
      "Coeficiente de reflexión:  K<sub>r</sub> = H<sub>r</sub>/H<sub>i</sub>      Separación cuasi-nodo ↔ antinodo = L/4"])
terms([
    ("H<sub>i</sub>", "Altura de la onda incidente (la que va hacia el obstáculo) [m]"),
    ("H<sub>r</sub>", "Altura de la onda reflejada (la que vuelve) [m]"),
    ("kx − ωt / kx + ωt", "Fases de la onda que avanza hacia +x y de la que vuelve hacia −x"),
    ("ε", "Desfase entre incidente y reflejada [rad]"),
    ("η<sub>máx</sub>", "Semialtura de la envolvente en los antinodos [m]"),
    ("η<sub>mín</sub>", "Semialtura de la envolvente en los cuasi-nodos [m]"),
    ("K<sub>r</sub>", "Coeficiente de reflexión (adimensional): 1 = reflexión total, 0 = nada"),
])
P("Cuasi-nodos: kx = [(2n+1)π − ε]/2; antinodos: kx = nπ − ε/2. Parte de la energía se transmite o se disipa, por eso H<sub>r</sub> &lt; H<sub>i</sub>.")
terms([
    ("n", "Número entero que numera cuasi-nodos y antinodos"),
    ("ε", "Desfase de la reflejada: desplaza la posición de nodos y antinodos"),
])
h3("Ondas de crestas cortas (incidencia oblicua + reflejada)")
fbox(["η = 2A · cos(k·sinθ·y) · cos(k·cosθ·x − ωt)  → progresa en x y es estacionaria en y"])
terms([
    ("A", "Amplitud de cada uno de los dos trenes [m]"),
    ("θ", "Ángulo de cada tren respecto al eje x (uno a +θ y otro a −θ) [rad]"),
    ("k·sinθ", "Componente y del número de onda: da la parte estacionaria en y"),
    ("k·cosθ", "Componente x del número de onda: da la parte que avanza en x"),
    ("x, y", "Coordenadas horizontales [m]"),
])
h3("Grupos de ondas — ejercicio 5")
P("Dos trenes de igual H, misma dirección, con ω<sub>1,2</sub> = ω ∓ Δω/2 y k<sub>1,2</sub> = k ∓ Δk/2:")
terms([
    ("ω<sub>1</sub>, ω<sub>2</sub>", "Frecuencias angulares de los dos trenes [rad/s]"),
    ("k<sub>1</sub>, k<sub>2</sub>", "Números de onda de los dos trenes (cada uno con su dispersión) [rad/m]"),
    ("ω, k", "Valores medios: ω = (ω<sub>1</sub> + ω<sub>2</sub>)/2, k ≈ (k<sub>1</sub> + k<sub>2</sub>)/2"),
    ("Δω, Δk", "Diferencias: Δω = ω<sub>2</sub> − ω<sub>1</sub>, Δk = k<sub>2</sub> − k<sub>1</sub>"),
])
fbox(["η = H · cos(kx − ωt) · cos[ ½·(Δk·x − Δω·t) ]",
      "onda <b>portadora</b> (ω, k medios, celeridad C = ω/k)   ×   <b>envolvente / modulante</b> (viaja a C<sub>g</sub>)",
      "<b>C<sub>g</sub> = Δω/Δk → dω/dk = n·C</b>,    n = ½·[1 + 2kh / sinh(2kh)]",
      "L<sub>g</sub> = 2π/Δk     T<sub>g</sub> = 2π/Δω     (T de la función modulante = 4π/Δω)"])
terms([
    ("H", "Altura de cada tren [m] (en el centro del grupo se suman: 2H)"),
    ("cos(kx − ωt)", "Onda portadora: las olas individuales que se ven"),
    ("cos[½(Δk·x − Δω·t)]", "Envolvente (modulante): hace crecer y decrecer las olas"),
    ("C = ω/k", "Celeridad de las olas individuales [m/s]"),
    ("C<sub>g</sub>", "Celeridad de grupo: a la que viaja la envolvente y la energía [m/s]"),
    ("dω/dk", "Derivada de ω respecto a k (límite de Δω/Δk)"),
    ("n", "Cociente C<sub>g</sub>/C (adimensional): ½ en profundas, 1 en reducidas"),
    ("sinh(2kh)", "Seno hiperbólico de 2kh"),
    ("L<sub>g</sub>, T<sub>g</sub>", "Longitud [m] y periodo [s] del grupo"),
])
bl("<b>Indefinidas</b>: n = ½ → C<sub>g</sub> = C<sub>0</sub>/2. Las ondas nacen por detrás del grupo, lo atraviesan a velocidad C y desaparecen por delante.",
   "<b>Reducidas</b>: n = 1 → C<sub>g</sub> = C = √(gh).",
   "<b>Ojo con 4π/Δω frente a 2π/Δω</b>: la función cos(½·…) tarda 4π/Δω en repetirse, pero un grupo es medio periodo de esa función (la envolvente se ve en valor absoluto). "
   "Por eso <b>T<sub>grupo</sub> = 2π/Δω</b> = T<sub>1</sub>T<sub>2</sub>/(T<sub>1</sub> − T<sub>2</sub>). Es el periodo al que responde una estructura flotante (deriva lenta en surge).")
terms([
    ("T<sub>1</sub>, T<sub>2</sub>", "Periodos de los dos trenes [s]"),
    ("C<sub>0</sub>", "Celeridad en indefinidas = gT/2π [m/s]"),
])
h3("Oleaje irregular y corriente")
bl("Irregular: η(x,y,t) = ΣΣ A<sub>mn</sub>·cos(k<sub>m</sub>cosθ<sub>n</sub>·x + k<sub>m</sub>sinθ<sub>n</sub>·y − ω<sub>m</sub>t + ε<sub>mn</sub>), con A y ε aleatorios → puente al análisis espectral (día 4).",
   "Con corriente uniforme (U<sub>0</sub>, V<sub>0</sub>) la dispersión cambia: <b>σ² = (ω − U<sub>0</sub>k cosθ − V<sub>0</sub>k sinθ)² = gk·tanh(kh)</b>, "
   "con σ = frecuencia <b>intrínseca</b> (relativa al agua) y ω = frecuencia <b>absoluta</b> (la que mide un observador fijo).")
terms([
    ("A<sub>mn</sub>", "Amplitud de cada componente (m: frecuencia, n: dirección) [m]"),
    ("ε<sub>mn</sub>", "Fase aleatoria de cada componente [rad]"),
    ("k<sub>m</sub>, ω<sub>m</sub>", "Número de onda y frecuencia de la componente m"),
    ("θ<sub>n</sub>", "Dirección de la componente n [rad]"),
    ("ΣΣ", "Suma sobre todas las frecuencias (m) y direcciones (n)"),
    ("U<sub>0</sub>, V<sub>0</sub>", "Componentes x e y de la corriente uniforme [m/s]"),
    ("θ", "Dirección de la ola respecto al eje x [rad]"),
    ("σ", "Frecuencia intrínseca: la que «ve» alguien que se mueve con el agua [rad/s]"),
    ("ω", "Frecuencia absoluta: la que mide un observador fijo [rad/s]"),
])

# ---------------------------------------------------------------- 9
h2("9. Magnitudes promediadas: masa y energía")
P("Son promedios en un periodo o en una longitud de onda de los productos de términos lineales (de segundo orden en la amplitud).")
table(["Magnitud", "Fórmula", "Comentario"], [
    ["Flujo de masa", "M = ρgH²/(8C) = ρgA²k/(2ω);  U<sub>m</sub> = M/(ρh)",
     "Las órbitas son cerradas, pero bajo la cresta la velocidad es algo mayor → transporte neto en el sentido de avance."],
    ["Energía cinética media", "E<sub>c</sub> = ρgH²/16 = ¼ρgA²", "Por unidad de superficie [J/m²]"],
    ["Energía potencial media", "E<sub>p</sub> = ρgH²/16 = ¼ρgA²", "Igual a la cinética (equipartición)"],
    ["<b>Energía total media</b>", "<b>E = ρgH²/8 = ½ρgA²</b>", "Solo depende de H: <b>no depende ni de T ni de h</b>. Por longitud de onda: E·L."],
    ["<b>Flujo de energía</b>", "<b>F = E·C<sub>g</sub> = E·n·C</b>  [W/m]", "Lo transmite el trabajo de la presión dinámica. Es la potencia por metro de frente."],
], [36, 56, 78])
terms([
    ("M", "Flujo de masa medio por metro de frente [kg/(m·s)]"),
    ("U<sub>m</sub>", "Velocidad media equivalente de ese transporte, repartida en la vertical [m/s]"),
    ("E<sub>c</sub>, E<sub>p</sub>", "Energía cinética y potencial medias por m² de superficie [J/m²]"),
    ("E", "Energía total media por m² de superficie (densidad de energía) [J/m²]"),
    ("F", "Flujo de energía medio: potencia por metro de frente de ola [W/m]"),
    ("ρ, g", "Densidad del agua [kg/m³] y gravedad [m/s²]"),
    ("H, A", "Altura de ola y amplitud (A = H/2) [m]"),
    ("C, C<sub>g</sub>, n", "Celeridad, celeridad de grupo [m/s] y n = C<sub>g</sub>/C"),
    ("k, ω, h", "Número de onda, frecuencia angular y profundidad"),
])
table(["", "Reducidas", "Indefinidas", "Intermedias"], [
    ["C", "√(gh)", "C<sub>0</sub> = gT/2π", "C<sub>0</sub>·tanh kh"],
    ["C<sub>g</sub>", "C = √(gh)", "C<sub>0</sub>/2", "n·C"],
    ["F (W/m)", "(ρgH²/8)·√(gh)", "<b>ρg²H²T/(32π)</b>", "(ρgH²/8)·n·C"],
], [30, 46, 46, 48])
terms([
    ("ρg²H²T/(32π)", "Potencia del oleaje en profundas: sale de E·C<sub>0</sub>/2 con C<sub>0</sub> = gT/2π"),
    ("T", "Periodo [s]"),
])
bl("<b>La energía viaja a C<sub>g</sub>, no a C</b>: por los nodos del grupo no pasa energía (allí H = 0 y la presión dinámica es nula).",
   "Tensor de radiación (para rotura, set-up y corrientes de costa): S<sub>xx</sub> = E[n·cos²θ + (n − ½)], S<sub>xy</sub> = E·n·sinθ·cosθ, S<sub>yy</sub> = E[n·sin²θ + (n − ½)].",
   "Las olas producen un ligero descenso del nivel medio (<i>set-down</i>) y de la presión media respecto a la hidrostática.")
terms([
    ("S<sub>xx</sub>", "Flujo de cantidad de movimiento en x transportado en dirección x [N/m]"),
    ("S<sub>yy</sub>", "Ídem en y [N/m]"),
    ("S<sub>xy</sub>", "Flujo de cantidad de movimiento en x transportado en y (y viceversa) [N/m]"),
    ("θ", "Ángulo de la ola respecto al eje x [rad]"),
    ("E, n", "Energía media [J/m²] y n = C<sub>g</sub>/C"),
])

# ---------------------------------------------------------------- 10
h2("10. Ejercicios de teoría de ondas resueltos (los 5 del repositorio)")
note("<b>Receta para casi todos:</b> 1) mira qué te dan de (T, L, h); 2) con dos de ellos sacas el tercero con ω² = gk·tanh(kh); "
     "3) clasifica con h/L; 4) aplica la fórmula del apartado (órbitas, celeridad, envolventes, grupo…). "
     "Usa g = 9,81 m/s² y trabaja en <b>radianes</b>.", bg=ZEBRA)

h3("Ejercicio 1 — Profundidad de la plataforma a partir de dos longitudes de onda")
P("<i>Teledetección: L = 312 m en indefinidas y L = 200 m sobre la plataforma. ¿h?</i>")
bl("El periodo no cambia al propagarse. En indefinidas: L<sub>0</sub> = gT²/2π → T = √(2π·312/9,81) = <b>14,14 s</b> → ω = 0,444 rad/s.",
   "En la plataforma conoces L y T: k = 2π/200 = 0,0314 m⁻¹. Despeja h de ω² = gk·tanh(kh): tanh(kh) = ω²/(gk) = 0,641 → kh = atanh(0,641) = 0,760.",
   "<b>h = 0,760/0,0314 ≈ 24,2 m</b>. Comprobación: h/L = 0,12 → intermedias (correcto no haber usado ninguna simplificación).")
P("Truco: aquí <b>no hay que iterar</b> porque la incógnita es h y sale con un atanh.")
terms([
    ("L<sub>0</sub> = 312 m", "Longitud de onda en indefinidas (dato)"),
    ("L = 200 m", "Longitud de onda sobre la plataforma (dato)"),
    ("T, ω", "Periodo [s] y frecuencia angular [rad/s]: iguales en los dos sitios"),
    ("k", "Número de onda en la plataforma = 2π/L [rad/m]"),
    ("atanh", "Tangente hiperbólica inversa (en la calculadora: tanh⁻¹)"),
    ("h", "Profundidad de la plataforma (incógnita) [m]"),
])

h3("Ejercicio 2 — H, T y L a partir de la órbita de las partículas")
P("<i>Canal de h = 1 m; a media profundidad (z = −0,5 m) el semieje mayor es 0,1 m y el menor 0,05 m.</i>")
bl("Divide los semiejes: B/A = tanh k(h+z) → 0,5 = tanh(0,5k) → 0,5k = atanh(0,5) = 0,549 → <b>k = 1,099 m⁻¹ → L = 5,72 m</b>.",
   "Dispersión directa (sin iterar, ya conoces k y h): ω² = 9,81·1,099·tanh(1,099) = 8,62 → ω = 2,94 rad/s → <b>T = 2,14 s</b>.",
   "Semieje mayor: 0,1 = (H/2)·cosh(1,099·0,5)/sinh(1,099) → <b>H ≈ 0,23 m</b>.",
   "Comprobación: h/L = 0,175 → intermedias. H/L = 0,04 → pequeña amplitud razonable.")
terms([
    ("A = 0,1 m", "Semieje mayor (horizontal) de la órbita a z = −0,5 m"),
    ("B = 0,05 m", "Semieje menor (vertical) de la órbita a z = −0,5 m"),
    ("h = 1 m; z = −0,5 m", "Profundidad del canal y cota del punto observado"),
    ("h + z = 0,5 m", "Distancia del punto al fondo"),
    ("k, L, T, ω, H", "Incógnitas: número de onda, longitud, periodo, frecuencia angular y altura de ola"),
])

h3("Ejercicio 3 — Llegada de un tsunami sobre un talud")
P("<i>Detectado a las 12:00 al inicio de la plataforma (h = 200 m); el fondo sube con pendiente 0,005 hasta la costa.</i>")
bl("Un tsunami es onda muy larga → <b>siempre reducidas</b>: C = √(gh). El fondo es h(x) = 200 − 0,005x, así que la distancia hasta la costa (h = 0) es 200/0,005 = 40 000 m.",
   "Como C cambia con x, no vale t = d/C: hay que integrar <b>t = ∫ dx / C(x) = ∫₀⁴⁰⁰⁰⁰ dx / √(g(200 − 0,005x))</b>.",
   "Resultado: t = [2/(0,005·g)]·√(g·200) = 1806 s ≈ <b>30 min → llega hacia las 12:30</b>.",
   "Comprobación rápida: es el doble de lo que daría usando la velocidad inicial (40 000/44,3 = 903 s), lógico porque se frena hasta pararse.")
terms([
    ("h(x) = 200 − 0,005x", "Profundidad en cada punto del talud [m]; 0,005 es la pendiente"),
    ("x", "Distancia recorrida desde el inicio de la plataforma [m]"),
    ("C(x) = √(g·h(x))", "Celeridad de onda larga en cada punto [m/s]"),
    ("dx / C(x)", "Tiempo que tarda en recorrer un tramo dx [s]"),
    ("t", "Tiempo total de llegada [s]"),
])

h3("Ejercicio 4 — Reflexión y transmisión en una barrera (envolventes)")
P("<i>Figura: fuera del puerto (barlomar) envolvente entre 0,3 m y 0,1 m con distancia nodo–antinodo 4,17 m; "
  "dentro (sotamar, h = 2,0 m) entre 0,258 m y 0,122 m con distancia 3,65 m. Fuera, el fondo está d metros más bajo.</i>")
bl("Son ondas <b>cuasi-estacionarias</b>. La distancia cuasi-nodo ↔ antinodo es L/4: L<sub>1</sub> = 4·4,17 = 16,67 m (k<sub>1</sub> = 0,377 m⁻¹); L<sub>2</sub> = 4·3,65 = 14,6 m (k<sub>2</sub> = 0,430 m⁻¹).",
   "Periodo con la zona donde conoces h (dentro, h = 2 m): ω² = 9,81·0,430·tanh(0,430·2) → ω = 1,71 rad/s → <b>T = 3,66 s</b> (el mismo a ambos lados).",
   "Fuera: H<sub>i</sub> + H<sub>r</sub> = 0,3 y H<sub>i</sub> − H<sub>r</sub> = 0,1 → <b>H<sub>i1</sub> = 0,20 m (incidente), H<sub>r1</sub> = 0,10 m (reflejado fuera)</b> → K<sub>r</sub> = 0,5.",
   "Dentro: H<sub>i</sub> + H<sub>r</sub> = 0,258 y H<sub>i</sub> − H<sub>r</sub> = 0,122 → <b>H<sub>i2</sub> = 0,19 m (transmitido)</b>, H<sub>r2</sub> = 0,068 m (lo que devuelve la playa interior).",
   "Profundidad fuera, con k<sub>1</sub> y el mismo ω: ω² = 9,81·0,377·tanh(0,377·h<sub>1</sub>) → <b>h<sub>1</sub> ≈ 2,85–2,88 m</b> → el fondo dentro del puerto es <b>≈ 0,85 m más somero</b> (d ≈ 0,85 m).")
note("En el PDF de la solución, el último paso dice «zona de sotamar» y escribe 0,43, pero para que salga 2,85 m hay que usar k<sub>1</sub> = 0,377 "
     "(barlomar). Es una errata de la solución; el resultado es el bueno (yo obtengo 2,88 m con más decimales).")
terms([
    ("Barlomar / sotamar", "Lado del mar (fuera del puerto) / lado protegido (dentro)"),
    ("L<sub>1</sub>, k<sub>1</sub>", "Longitud y número de onda fuera del puerto"),
    ("L<sub>2</sub>, k<sub>2</sub>", "Longitud y número de onda dentro del puerto"),
    ("H<sub>i1</sub>, H<sub>r1</sub>", "Altura incidente y reflejada fuera [m]"),
    ("H<sub>i2</sub>, H<sub>r2</sub>", "Altura transmitida (incidente dentro) y reflejada por la playa interior [m]"),
    ("h<sub>1</sub>", "Profundidad fuera del puerto [m]"),
    ("d", "Diferencia de profundidad entre fuera y dentro = h<sub>1</sub> − 2,0 [m]"),
    ("K<sub>r</sub>", "Coeficiente de reflexión = H<sub>r</sub>/H<sub>i</sub>"),
])

h3("Ejercicio 5 — Grupo de ondas bicromático sobre una plataforma eólica")
P("<i>H<sub>1</sub> = H<sub>2</sub> = 2 m; T<sub>1</sub> = 5,7 s; T<sub>2</sub> = 5,4 s; h = 102 m. Portadora (T, k, C), modulante (T) y grupo (T, C<sub>g</sub>).</i>")
bl("ω<sub>1</sub> = 1,1023 y ω<sub>2</sub> = 1,1636 rad/s → ω = 1,1329 rad/s (<b>T = 5,55 s</b>), Δω = 0,0612 rad/s.",
   "Portadora: kh ≫ π (profundas) → k ≈ ω²/g = <b>0,1308 m⁻¹</b>, <b>C = ω/k = 8,66 m/s</b> (L ≈ 48 m).",
   "k<sub>1</sub> = 0,1239 (L<sub>1</sub> = 50,73 m) y k<sub>2</sub> = 0,1380 (L<sub>2</sub> = 45,53 m) → Δk = 0,0141 m⁻¹.",
   "Modulante: T<sub>mod</sub> = 4π/Δω = <b>205 s</b>. Grupo: <b>T<sub>g</sub> = 2π/Δω = 102,6 s</b>; <b>C<sub>g</sub> = Δω/Δk = 4,33 m/s</b> (= C/2, como toca en profundas); L<sub>g</sub> = 2π/Δk ≈ 444 m.",
   "En la versión de la diapositiva se pregunta el periodo de oscilación en <i>surge</i> de la flotante: es el del grupo, ≈ 103 s.")
note("En la solución aparece «tanh k·202»: es una errata (h = 102 m). Da igual porque con kh ≈ 13 la tanh vale 1.")
terms([
    ("H<sub>1</sub>, H<sub>2</sub>", "Altura de cada tren (2 m)"),
    ("T<sub>1</sub>, T<sub>2</sub>", "Periodos de los dos trenes (5,7 y 5,4 s)"),
    ("ω, k, C", "Frecuencia, número de onda y celeridad de la onda portadora"),
    ("Δω, Δk", "Diferencias de frecuencia y de número de onda entre los dos trenes"),
    ("T<sub>mod</sub>", "Periodo de la función modulante = 4π/Δω [s]"),
    ("T<sub>g</sub>, C<sub>g</sub>, L<sub>g</sub>", "Periodo [s], celeridad [m/s] y longitud [m] del grupo"),
    ("Surge", "Movimiento de avance-retroceso (longitudinal) de la plataforma flotante"),
])

h3("Ejercicios de la presentación (sin enunciado aparte)")
bl("<b>Números adimensionales y Le Méhauté</b> (tres oleajes): están resueltos en la sección 3. Practica calcular h/L, H/L, H/h, U<sub>r</sub>, h/gT² y H/gT² y razonar órbitas, si siente el fondo y la simetría.",
   "<b>Dispersión con h = 10 m (T = 2…24 s) y con T = 10 s (h = 2…50 m)</b>: repite dos o tres casos de las tablas de la sección 6 con la calculadora para coger soltura.")

# ---------------------------------------------------------------- 11
h2("11. Chuleta de teoría (lo que más cae en el 60 %)")
bl("Hipótesis de la teoría potencial y por qué cada una (sección 5).",
   "Ecuación de Laplace, Bernoulli y las cinco condiciones de contorno; por qué el problema es no lineal y cómo se linealiza.",
   "Clasificación h/L con sus límites (1/2 y 1/20) y qué depende de qué en cada zona.",
   "Dispersiva vs no dispersiva: en profundas C ∝ T; en reducidas C = √(gh).",
   "Órbitas: círculos (profundas) → elipses (intermedias) → elipses muy planas (reducidas); w = 0 en el fondo pero u no.",
   "Presión: hidrostática + dinámica; K<sub>p</sub>; triangular en reducidas.",
   "Estacionaria (H doble, nodos/antinodos, dónde son máximas u y w) y cuasi-estacionaria (envolventes, K<sub>r</sub>).",
   "Grupos: C<sub>g</sub> = nC; n = ½ en profundas y 1 en reducidas; la energía viaja con el grupo.",
   "E = ρgH²/8 (solo depende de H) y F = E·C<sub>g</sub>.",
   "Peralte máximo en profundas 1/7; Ursell y Le Méhauté para elegir teoría (lineal, Stokes, cnoidal, solitaria).")




build(sys.argv[1], "Oceanografía (83000111) · Resumen Día 2 — Tema 2: Mecánica de ondas", "Resumen Día 2 - Mecánica de ondas")
