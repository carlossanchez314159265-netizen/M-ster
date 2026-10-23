# Martes 27 — Espectral mínimo + teoría tipo + repaso final (3 h)

**Objetivo de cierre:** escribir el formulario entero de memoria y resolver sin mirar un ejercicio de cada tipo (dispersión, trayectorias, grupos, Hmax y espectral).

> Pendiente: el resumen espectral todavía no está hecho. Hasta que esté, trabajas directamente con las diapos que se indican abajo, que son las únicas que hacen falta del PDF de 81.

**Material del día**

- [Análisis del oleaje 2de3 — Espectral](<../03-analisis-del-oleaje/Oceanografia - Bloque 2 - Analisis del oleaje 2de3 - Espectral.pdf>) (en adelante, *Espectral*)
- [Cálculo de espectros](<../03-analisis-del-oleaje/Oceanografia - Bloque 2 -  Calculo_de_espectros.pdf>)
- [Planning general](<00 - Planning general 1er parcial (28-10).pdf>): formulario (pág. 4) y 11 preguntas tipo (pág. 5)
- Tu formulario a mano de los días anteriores

## Horario (3 h)

Bloques algo más cortos que los de 50 min para que quepan cuatro en 3 h. Móvil fuera de la mesa.

| Bloque | Tiempo | Qué haces |
|---|---|---|
| 1 | 45 min | Teoría espectral mínima |
| — | 5 min | Descanso |
| 2 | 45 min | Ejercicios espectrales |
| — | 10 min | Descanso |
| 3 | 40 min | Preguntas tipo + Cálculo de espectros (solo concepto) |
| — | 5 min | Descanso |
| 4 | 30 min | Formulario de memoria + rehacer el peor ejercicio |

### Bloque 1 — Teoría espectral mínima (45 min)

Lee solo estas diapos del *Espectral*, en este orden, y pasa a tu formulario lo que esté en negrita:

1. **Diapos 10–14** (10 min): el oleaje como suma de muchas ondas aleatorias; qué es el espectro S(ω) o S(f) (cómo se reparte la energía entre frecuencias). Una onda monocromática da un pico único.
2. **Diapos 17–19** (10 min): el área bajo el espectro es m0 = varianza de η, y de ahí **Hm0 = 4√m0** (≈ H1/3).
3. **Diapos 26–30** (15 min): **momentos mn = ∫ fⁿ S(f) df**, **Tm01 = m0/m1**, **Tm02 = √(m0/m2)**, **Tp = 1/fp** (periodo del pico) y **anchura espectral ε**. Diapo 30: conversión entre S(f) y S(ω) (S(ω) = S(f)/2π); fíjate en qué variable da el enunciado.
4. **Diapos 37–40 y 45, 48** (10 min, en diagonal): qué es el **fetch**, oleaje totalmente desarrollado (**Pierson-Moskowitz**: no depende del fetch) frente a parcialmente desarrollado (**JONSWAP**: pico más afilado, factor γ). Diapo 23: sea frente a swell. No memorices las expresiones de los espectros, solo qué representa cada uno.

Si te sobra tiempo: diapos 67–69 (relación entre parámetros espectrales y estadísticos: Hm0 ≈ Hs, Tm02 ≈ Tz). Se salta sin pena: **bimodales (58–59)**, **dispersión direccional (60–65)**, TMA, Bretschneider.

### Bloque 2 — Ejercicios espectrales (45 min)

Primero lo intentas tú; la solución solo después de pelearlo 10 min.

1. **Ejercicio 1, diapos 75–76** (10 min). Cinco componentes con H y T; piden Hm0. Calienta: es sumar energías E/ρg = H²/8 de cada componente, que es m0, y aplicar Hm0 = 4√m0. Comprueba que te da 8,00 m.
2. **Ejercicio 2 analítico, diapos 78–80** (25 min). Espectro a trozos S(ω) = 2ω entre 0 y 0,8 y una recta decreciente entre 0,8 y 2. Integra a mano m0 (área de dos trozos), luego m1 y m2, y saca Hs, energía media y periodos. Comprueba que Hs = 5,06 m (m0 = 1,6 m²). Es el tipo de ejercicio espectral que más se presta a examen.
3. **Ejercicio 2 cualitativo, diapo 77** (10 min). Espectro con dos picos: di cuál es sea y cuál swell y por qué (el swell tiene periodo más largo y pico más estrecho; el sea, más corto y ancho), y lee periodo y dirección de pico de cada uno. Redáctalo como lo escribirías en el examen.

### Bloque 3 — Preguntas tipo + Cálculo de espectros (40 min)

1. **Cálculo de espectros, solo concepto** (10 min). Diapo 6 (**Parseval**: el área del espectro es la varianza del registro), diapo 8 (**periodograma**: FFT del registro entero, mucha resolución pero muy ruidoso) y diapos 9–10 (**Welch**: trocear, ventanear, solapar y promediar; más estable a cambio de perder resolución). Con eso respondes la pregunta 11. Es lo primero que se sacrifica si vas tarde.
2. **Las 11 preguntas tipo** (30 min). Sin mirar nada, contesta cada una en voz alta o en 3–4 líneas en una hoja, unos 2–3 min por pregunta. Marca las que no te salgan y repásalas en el resumen o la diapo correspondiente. Las de la diapo 56 del Tema 1, con las tarjetas Anki del Día 1.

### Bloque 4 — Cierre (30 min)

1. **Formulario de memoria** (15 min). Hoja en blanco, escribe el formulario completo de la pág. 4 del planning general: dispersión, superficie libre y velocidades, presión, tsunami, estacionarias, grupos y energía, Rayleigh y espectral. Compara con el original y corrige en rojo lo que falle.
2. **Rehacer el ejercicio que peor te salió** (15 min) de los 5 de teoría de ondas o el de Hmax (diapo 42 del Estadístico).

Autoexamen final: ¿podrías hacer ahora, sin mirar, un ejercicio de dispersión, uno de trayectorias, uno de grupos, uno de Hmax y uno espectral? Lo que dudes, al repaso del miércoles.

## Si vas tarde

- **Solo tienes 2 h:** recorta el Bloque 1 a las diapos 17–19 y 26–29 (Hm0 y momentos), haz solo el ejercicio 2 analítico y salta Cálculo de espectros. El formulario de memoria no se toca.
- **Solo tienes 1 h:** formulario de memoria (20 min), ejercicio 2 analítico (25 min) y las 6 preguntas de la diapo 56 (15 min). Lo espectral se reduce a Hm0 = 4√m0 y las definiciones de Tp, Tm01 y Tm02.
- Nunca sacrifiques la dispersión, las trayectorias, los grupos ni Rayleigh.

## Antes de dormir

Audio de repaso del sábado o del domingo (en sus carpetas `audios/`) si te apetece; deja el formulario y las tarjetas preparados para los 30 min del miércoles.
