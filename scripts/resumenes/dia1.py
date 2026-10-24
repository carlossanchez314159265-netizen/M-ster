import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from estilo import *

P("Oceanografía · Día 1", H1)
P("Bloque 1 — Introducción a la Oceanografía (presentaciones 1/2 y 2/2) · 1er parcial 28/10/2026", SUB)

h2("0. Lo que te juegas (organización)")
bl("El 1er parcial vale <b>37,5 %</b> en evaluación progresiva; necesitas <b>mínimo 3/10</b> en cada parcial para que haga media.",
   "En evaluación global o extraordinaria: mínimo 5/10 y cada parcial vale 42,5 %.",
   "Prácticas: 15 % (canal, prácticas de clase y software).")

h2("1. Por qué le importa la oceanografía a un ingeniero naval")
P("Idea central del profesor: <b>sin buenos datos meteo-oceánicos no hay diseño fiable</b>.")
h3("Offshore frente a onshore")
table(["Ventajas del mar", "Desafíos"], [
    ["Más recurso · recurso de mejor calidad (menos turbulencia) · economías de escala · menos restricciones socioambientales",
     "Olas, corrientes, hielo, viento, visibilidad · profundidad · cargas de diseño mayores · corrosión · distancia a costa (complica la O&amp;M)"],
], [85, 85])
h3("Ciclo de vida de un parque eólico marino (vida mínima ≈ 35 años)")
table(["Fase", "Qué incluye"], [
    ["1. Desarrollo", "Factibilidad, permisos, estudios ambientales y geotécnicos, evaluación del recurso, condiciones de diseño, FEED"],
    ["2. Construcción", "Adaptación del puerto, cimentaciones, cables, instalación de turbinas y subestaciones"],
    ["3. Operación", "O&amp;M, sustitución de componentes, repotenciación"],
    ["4. Desmantelamiento", "Retirada y reciclaje"],
], [34, 136])
h3("Qué datos necesita cada fase")
bl("<b>Diseño</b>: series históricas largas (+25 años), calibradas, continuas, homogéneas y con resolución horaria.",
   "<b>Instalación y operación</b>: predicción (<i>forecast</i>) y <i>nowcast</i>.",
   "<b>Fuentes</b>: visuales, instrumentales (boyas, LiDAR flotante, mástiles), satelitales y numéricas (bases de mesoescala, reanálisis).",
   "<b>Base de diseño (DNV)</b>: datos del sitio, normas, condiciones de diseño, fabricación, instalación y O&amp;M. Buena base → pocos cambios; mala base → retrasos y sobrecostes.",
   "<b>Ejemplos reales</b>: agitación portuaria en el ensamblado de flotantes (movimientos de la plataforma amarrada, tensiones de amarras) y transporte e instalación (tiempos de espera, puertos refugio, aceleraciones de la carga).")

h2("2. Las ramas de la oceanografía")
P("Pregunta típica de test: saber qué estudia cada una.")
table(["Rama", "Qué estudia", "Aplicación para el ingeniero"], [
    ["<b>Física</b>", "T, S, densidad, presión, corrientes, oleaje, mareas, circulación termohalina, interacción con la atmósfera (Niño/Niña)",
     "Diseño offshore y costero, energías marinas, riesgos"],
    ["<b>Química</b>", "Composición del agua (Na⁺, Cl⁻…), pH, O₂ disuelto, ciclos biogeoquímicos, contaminación", "Calidad del agua, impacto ambiental, corrosión"],
    ["<b>Biológica</b>", "Organismos y su relación con el medio (también llamada <i>ecología oceánica</i>)", "Impacto ambiental, <i>biofouling</i>"],
    ["<b>Geológica</b>", "Fondo marino, sedimentos, tectónica", "Cimentaciones, anclajes, cables y oleoductos"],
    ["<b>Operacional</b>", "Observación continua y casi en tiempo real + modelos + difusión rápida (hindcast, nowcast, forecast)",
     "Navegación, operaciones marítimas, seguridad"],
], [24, 86, 60])
P("<b>Copernicus Marine Service (CMEMS)</b>: servicio europeo de oceanografía operacional. Datos gratuitos de hindcast, nowcast y forecast; "
  "publica el <i>Ocean State Report</i>; lo gestiona Mercator Ocean International.")

h2("3. Propiedades físicas del agua de mar")
box("<b>Lo más importante del día.</b> Conservativas (<b>T y S</b>): dentro del océano solo cambian por mezcla → sirven para identificar masas de agua. "
    "No conservativas (O₂, nutrientes): cambian también por procesos químicos y biológicos.")
h3("Temperatura")
bl("Rango habitual: de −2 °C a 30 °C. La superficial depende de la insolación y de los aportes de agua (lluvia, ríos).",
   "<b>Temperatura potencial (θ)</b>: la que tendría el agua subida adiabáticamente a la superficie. Sirve para comparar aguas a distinta profundidad.",
   "<b>Termoclina</b>: capa donde la temperatura cae rápido con la profundidad, bajo la capa de mezcla. El 90 % del océano está por debajo, entre 0 y 3 °C.")
terms([
    ("T", "Temperatura in situ: la medida en el punto [°C]"),
    ("θ", "Temperatura potencial: la que tendría si se subiera a la superficie sin intercambiar calor [°C]"),
    ("Adiabático", "Sin intercambio de calor con el entorno (al subir, el agua se expande y se enfría un poco)"),
])
h3("Salinidad")
bl("Media ≈ <b>35 g/kg</b> → 35 ‰ ≈ 35 ppt ≈ 35 PSU.",
   "<b>Aumenta</b>: evaporación, formación de hielo. <b>Disminuye</b>: lluvia, deshielo, aportes de ríos.")
terms([
    ("g/kg", "Gramos de sal disuelta por kilogramo de agua de mar"),
    ("‰", "Tanto por mil (lo mismo que g/kg)"),
    ("ppt", "<i>Parts per thousand</i>: partes por mil (= ‰)"),
    ("PSU", "<i>Practical Salinity Unit</i>: unidad de salinidad práctica (adimensional), calculada con la conductividad"),
])
table(["", "Salinidad práctica (SP)", "Salinidad absoluta (SA)"], [
    ["Unidad", "PSU, adimensional", "g/kg"],
    ["Basada en", "Conductividad eléctrica", "Masa de sales"],
    ["Sistema", "PSS-78", "TEOS-10"],
    ["Precisión", "Menor en condiciones extremas", "Alta"],
], [34, 68, 68])
terms([
    ("S<sub>P</sub>", "Salinidad práctica (adimensional, en PSU)"),
    ("S<sub>A</sub>", "Salinidad absoluta: masa de sales por masa de agua de mar [g/kg]"),
    ("PSS-78", "<i>Practical Salinity Scale 1978</i>: escala que define S<sub>P</sub> a partir de la conductividad"),
    ("TEOS-10", "<i>Thermodynamic Equation Of Seawater 2010</i>: estándar actual, trabaja con S<sub>A</sub>"),
])
bl("<b>Haloclina</b>: capa con cambio rápido de salinidad. Permanente (desembocadura de un río) o efímera (tras lluvia intensa).")
h3("Densidad")
bl("<b>ρ(S, T, p)</b> por la ecuación de estado: sube con S, sube con p y baja con T. Típico en superficie: <b>ρ ≈ 1025 kg/m³</b>.")
fbox(["<b>Anomalía de densidad:</b>  σ = ρ − 1000   (kg/m³)       Ej.: ρ = 1025 → σ = 25"])
terms([
    ("ρ", "Densidad del agua de mar [kg/m³]"),
    ("σ", "Anomalía de densidad (sigma) [kg/m³]: se quita 1000 para trabajar con números pequeños"),
    ("1000", "Densidad de referencia ≈ agua dulce [kg/m³]"),
    ("S, T, p", "Salinidad, temperatura y presión, de las que depende ρ"),
])
P("Ecuación de estado UNESCO (1983):")
fbox(["ρ(s, T, p) = ρ(s, T, 0) / [ 1 − p / K(s, T, p) ]",
      "ρ(s, T, 0) = A + B·s + C·s<super>3/2</super> + D·s²   (densidad a presión atmosférica)"])
terms([
    ("ρ(s,T,p)", "Densidad a salinidad s, temperatura T y presión p [kg/m³]"),
    ("ρ(s,T,0)", "Densidad de esa misma agua a presión atmosférica (p = 0) [kg/m³]"),
    ("s", "Salinidad (práctica, PSU)"),
    ("T", "Temperatura [°C]"),
    ("p", "Presión manométrica, es decir, por encima de la atmosférica [bar]"),
    ("K(s,T,p)", "Módulo de compresibilidad secante [bar]: cuánto «se resiste» el agua a comprimirse"),
    ("A, B, C, D", "Coeficientes que son polinomios en T (de la tabla UNESCO). Hay más (hasta N) dentro de K"),
    ("1 − p/K", "Factor de compresión: al aumentar p, el denominador baja y ρ sube"),
])
bl("<b>TEOS-10</b>: estándar actual (sustituye a EOS-80). En Matlab, toolbox GSW: gsw_rho(SA,CT,p).")
terms([
    ("gsw_rho", "Función de la toolbox GSW (<i>Gibbs SeaWater</i>) que devuelve la densidad [kg/m³]"),
    ("SA", "Salinidad absoluta [g/kg]"),
    ("CT", "Temperatura conservativa [°C] (la que usa TEOS-10 en lugar de θ)"),
    ("p", "Presión del mar [dbar] (≈ profundidad en metros)"),
    ("EOS-80", "Ecuación de estado anterior (1980), la de UNESCO"),
])
bl("<b>Densidad potencial (σθ, σ₀, σ₂…)</b>: quita el efecto de la presión; sirve para comparar aguas y estudiar estabilidad.",
   "<b>Picnoclina</b>: cambio brusco de densidad; barrera a la mezcla vertical → <b>estratificación</b>.")
terms([
    ("σθ (σ₀)", "Anomalía de densidad potencial: la de esa agua llevada a la superficie (p = 0) con su θ [kg/m³]"),
    ("σ₂", "Ídem, pero llevada a 2000 dbar (útil para aguas profundas)"),
])

h3("Masas de agua")
bl("Volumen identificable por su T y S. Adquiere esos valores en superficie (clima local) y luego se hunde conservándolos.")
box("<b>Ejemplo que cae seguro: el Agua Mediterránea (AM)</b><br/>"
    "• Se forma en invierno en el Mediterráneo noroccidental: el Mistral la evapora y la enfría → más densa.<br/>"
    "• Baja hasta ≈ 2000 m con T = 12,8 °C y S = 38,4.<br/>"
    "• Sale por Gibraltar por debajo del agua atlántica que entra (fuerte mezcla en la interfase; AM menos mezclada: T = 11 °C, S = 36,5).<br/>"
    "• En el Atlántico se queda a ≈ 1000 m (flotabilidad neutra) y se detecta de lejos por su T y S altas.", "warn")
terms([
    ("T", "Temperatura del agua [°C]"),
    ("S", "Salinidad [PSU o g/kg]"),
    ("Flotabilidad neutra", "Profundidad a la que el agua tiene la misma densidad que la que la rodea: ni sube ni baja"),
])
P("<b>Procesos de formación</b>:")
bl("<b>Convección profunda</b>: zonas polares y subpolares (poca estratificación); se densifica por enfriamiento, evaporación o congelación y se hunde.",
   "<b>Subducción</b>: zonas subtropicales, por convergencia y lento hundimiento.",
   "<b>Mezcla</b> de dos o más masas de agua.")

h3("Diagramas T-S")
bl("Se representa T (mejor θ) frente a S, con las isopicnas (mejor σθ) dibujadas. Puntos unidos por profundidad creciente = curva T-S.",
   "<b>Agua tipo</b> = un punto del diagrama. La mezcla de dos aguas tipo queda sobre la recta que las une:")
fbox(["T = (m₁T₁ + m₂T₂) / (m₁ + m₂)          S = (m₁S₁ + m₂S₂) / (m₁ + m₂)"])
terms([
    ("T, S", "Temperatura [°C] y salinidad de la mezcla"),
    ("T₁, S₁", "Temperatura y salinidad del agua tipo 1"),
    ("T₂, S₂", "Temperatura y salinidad del agua tipo 2"),
    ("m₁, m₂", "Masas (o proporciones) de cada agua que se mezclan [kg o %]"),
    ("Isopicna", "Línea de igual densidad en el diagrama T-S"),
])
bl("Porcentajes por la regla de la palanca:")
fbox(["%A = b / (a + b) · 100          %B = a / (a + b) · 100"])
terms([
    ("%A, %B", "Porcentaje de cada agua tipo (A y B) en la mezcla"),
    ("a", "Distancia en el diagrama T-S del punto de mezcla al agua A"),
    ("b", "Distancia del punto de mezcla al agua B"),
    ("Idea", "Cuanto más cerca está la mezcla de A (a pequeña), más agua A tiene: por eso %A va con b"),
])
bl("<b>Cabbeling (densificación)</b>: mezclar dos aguas de igual densidad pero distinta T y S da un agua <b>más densa</b>, porque las isopicnas son curvas.")

h3("Estabilidad de la columna de agua")
table(["Condición", "Estabilidad", "En el diagrama T-S"], [
    ["dσθ/dz &gt; 0 (densidad crece hacia abajo)", "<b>Estable</b>", "Curva corta isopicnas: ángulo grande → muy estable/inestable"],
    ["dσθ/dz &lt; 0", "<b>Inestable</b>", "Ángulo pequeño → ligeramente estable/inestable"],
    ["dσθ/dz = 0", "<b>Neutra</b>", "Curva paralela a las isopicnas"],
], [58, 26, 86])
terms([
    ("σθ", "Anomalía de densidad potencial [kg/m³]"),
    ("z", "Profundidad, medida aquí <b>positiva hacia abajo</b> [m]"),
    ("dσθ/dz", "Cuánto cambia la densidad potencial al bajar 1 m [kg/m⁴]: si crece hacia abajo, el agua pesada está debajo → estable"),
])

h2("4. Ejercicio del tema (tipo examen): esfera de titanio en Menorca")
P("<b>Datos:</b> esfera de titanio (ρ = 4507 kg/m³), diámetro exterior 2 m, espesor 50 mm. Calcular el lastre para que quede totalmente sumergida "
  "y la variación de lastre para bajar a 450 m.")
P("<b>Planteamiento:</b>")
bl("Volumen de titanio: V<sub>Ti</sub> = 4/3·π·(1³ − 0,95³) ≈ 0,597 m³ → m ≈ <b>2693 kg</b>",
   "Volumen desplazado: V = 4/3·π·1³ ≈ <b>4,189 m³</b>",
   "Equilibrio sumergido: m + lastre = ρ<sub>agua</sub>·V → <b>lastre = ρ<sub>agua</sub>·V − m</b>")
terms([
    ("V<sub>Ti</sub>", "Volumen del casco de titanio = esfera exterior − esfera interior [m³]"),
    ("4/3·π·r³", "Volumen de una esfera de radio r [m³]"),
    ("1 y 0,95", "Radio exterior (2 m / 2) y radio interior (1 − 0,05 m de espesor) [m]"),
    ("m", "Masa de la esfera = ρ<sub>Ti</sub>·V<sub>Ti</sub> [kg]"),
    ("ρ<sub>Ti</sub>", "Densidad del titanio = 4507 kg/m³"),
    ("V", "Volumen exterior: el agua que desaloja la esfera [m³]"),
    ("ρ<sub>agua</sub>", "Densidad del agua de mar en ese punto (con la ecuación de estado) [kg/m³]"),
    ("ρ<sub>agua</sub>·V", "Empuje expresado en masa (Arquímedes) [kg]"),
    ("Lastre", "Masa que hay que añadir para que peso = empuje [kg]"),
])
table(["Situación", "Datos de entrada", "ρ agua", "Lastre"], [
    ["Superficie", "S = 37,8 · θ = 24,5 °C · p = 0", "≈ 1025,6 kg/m³", "<b>≈ 1603 kg</b>"],
    ["450 m", "p ≈ 45 bar · θ = 16 °C · S = 36,5", "≈ 1028,9 kg/m³", "<b>≈ 1617 kg</b>"],
], [26, 66, 40, 38])
terms([
    ("S", "Salinidad del agua en ese punto (PSU)"),
    ("θ", "Temperatura potencial [°C]"),
    ("p", "Presión manométrica: ≈ 1 bar por cada 10 m de profundidad [bar]"),
])
box("<b>Variación de lastre ≈ +14 kg.</b> A más profundidad el agua es más densa (más fría y más comprimida), así que la esfera flota más y hay "
    "que añadir lastre para seguir bajando. Se desprecia la compresión de la propia esfera.", "warn")

h2("5. Posibles preguntas de examen (las pone el profesor)")
table(["Pregunta", "Respuesta"], [
    ["¿Qué mide la PSU?", "La salinidad práctica: adimensional, calculada a partir de la conductividad"],
    ["¿Qué corriente se genera por diferencias de T y S?", "La circulación termohalina"],
    ["¿Qué estudia la oceanografía química?", "Composición química del agua de mar, ciclos biogeoquímicos y contaminación"],
    ["¿Capa con cambio rápido de temperatura en profundidad?", "Termoclina"],
    ["¿Qué es σ = ρ − 1000?", "La anomalía de densidad"],
    ["¿Densidad del agua de mar?", "≈ 1025 kg/m³ en superficie; hasta ≈ 1050 en el fondo"],
], [85, 85])
box("<b>Para cerrar el día:</b> plantea el ejercicio de la esfera sin mirar (es el puente con el 40 % de ejercicios) y contesta las seis preguntas de memoria.")

build(sys.argv[1], "Oceanografía (83000111) · Resumen Día 1 — Bloque 1: Introducción", "Resumen Día 1 - Introducción")
