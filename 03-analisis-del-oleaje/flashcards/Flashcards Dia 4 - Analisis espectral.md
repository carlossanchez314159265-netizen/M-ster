# Flashcards · Día 4 · Análisis espectral · 36 preguntas

Intenta responder antes de desplegar la solución. Marca las falladas para el último repaso. Son las mismas tarjetas del archivo de Anki (mazo `anki/Oceanografia - Dia 4 - Analisis espectral.apkg`).

**Fuentes:** *Esp. d.X* = diapositiva X de [Análisis del oleaje 2de3 — Espectral](<../Oceanografia - Bloque 2 - Analisis del oleaje 2de3 - Espectral.pdf>); *Cálc. d.X* = diapositiva X de [Cálculo de espectros](<../Oceanografia - Bloque 2 -  Calculo_de_espectros.pdf>). Las 19 primeras son las que alimentan el ejercicio espectral; del 20 en adelante, teoría.

## 1. ¿Qué hipótesis permite describir el oleaje como suma de sinusoides?

<details>
<summary>Ver respuesta</summary>

Por el **teorema central del límite** es un proceso **gaussiano de media cero**: suma de muchas componentes con amplitud, frecuencia, dirección y fase aleatoria. Cada k<sub>i</sub> sale de la dispersión ω<sub>i</sub>² = gk<sub>i</sub>·tanh(k<sub>i</sub>h). [Esp. d.10]

</details>

## 2. Energía de cada componente y energía total del oleaje

<details>
<summary>Ver respuesta</summary>

E<sub>i</sub> = ρgH<sub>i</sub>²/8 = ρga<sub>i</sub>²/2 (J/m²). La total es la **suma de energías**, no de alturas. [Esp. d.11]

</details>

## 3. ¿Qué es el espectro S(ω)?

<details>
<summary>Ver respuesta</summary>

Una **densidad**: cómo se reparte la varianza de η entre las frecuencias (m²·s/rad). S(ω)dω = a²/2 de las componentes de esa banda; multiplicado por ρg da energía. [Esp. d.12–13]

</details>

## 4. Teorema de Parseval aplicado al oleaje

<details>
<summary>Ver respuesta</summary>

El **área del espectro es la varianza** del registro: m<sub>0</sub> = ∫S dω = σ<sub>η</sub>² = η<sub>rms</sub>². Primer control de cualquier cálculo: m<sub>0</sub>/var(η) = 1. [Esp. d.17; Cálc. d.6]

</details>

## 5. Momento espectral de orden n

<details>
<summary>Ver respuesta</summary>

m<sub>n</sub> = ∫<sub>0</sub><sup>∞</sup> ωⁿ S(ω) dω (n = −1, 0, 1, 2, 4). m<sub>0</sub> en m². [Esp. d.26]

</details>

## 6. Altura de ola de momento de orden cero

<details>
<summary>Ver respuesta</summary>

**H<sub>m0</sub> = 4√m<sub>0</sub> = 4σ<sub>η</sub>**. Es una definición; en banda estrecha (Rayleigh) H<sub>1/3</sub> = 4,004√m<sub>0</sub> ≈ H<sub>m0</sub>. [Esp. d.18–19, 26]

</details>

## 7. Energía media por unidad de superficie a partir del espectro

<details>
<summary>Ver respuesta</summary>

**Ē = ρg·m<sub>0</sub>** (J/m²). Ej.: m<sub>0</sub> = 1,6 m² → 1025·9,81·1,6 = 16 088 J/m². [Esp. d.18, 80]

</details>

## 8. Periodo de pico T<sub>p</sub>

<details>
<summary>Ver respuesta</summary>

Periodo del máximo del espectro: T<sub>p</sub> = 2π/ω<sub>p</sub> (en ω) = 1/f<sub>p</sub> (en f). [Esp. d.30, 80]

</details>

## 9. Periodos medios espectrales (espectro en ω)

<details>
<summary>Ver respuesta</summary>

T<sub>01</sub> = 2π·m<sub>0</sub>/m<sub>1</sub> (frecuencia media)<br>
T<sub>02</sub> = 2π√(m<sub>0</sub>/m<sub>2</sub>) ≈ T<sub>z</sub> (pasos por cero)<br>
T<sub>−1,0</sub> = 2π·m<sub>−1</sub>/m<sub>0</sub> = T<sub>e</sub> (energético)<br>
T<sub>24</sub> = 2π√(m<sub>2</sub>/m<sub>4</sub>) ≈ T<sub>c</sub> (entre crestas)<br>
Orden: T<sub>01</sub> ≥ T<sub>z</sub> ≥ T<sub>c</sub> [Esp. d.27, 30]

</details>

## 10. Anchura espectral ε

<details>
<summary>Ver respuesta</summary>

ε = √(1 − m<sub>2</sub>²/(m<sub>0</sub>m<sub>4</sub>)). ε → 0: banda estrecha (swell); ε → 1: banda ancha (sea). [Esp. d.27]

</details>

## 11. Anchura espectral ν de Longuet-Higgins

<details>
<summary>Ver respuesta</summary>

ν² = m<sub>0</sub>m<sub>2</sub>/m<sub>1</sub>² − 1. ν → 0 si toda la energía está en una frecuencia; típico en temporales ν ≈ 0,3. [Esp. d.28]

</details>

## 12. Paso de S(f) a S(ω) y qué cambia

<details>
<summary>Ver respuesta</summary>

S(f)df = S(ω)dω con ω = 2πf → **S(f) = 2π·S(ω)**. m<sub>0</sub>, H<sub>m0</sub> y los periodos salen iguales si usas la fórmula de cada variable: en f no hay 2π (T<sub>01</sub> = m<sub>0</sub>/m<sub>1</sub>, T<sub>z</sub> = √(m<sub>0</sub>/m<sub>2</sub>)). m<sub>n</sub>(ω) = (2π)ⁿ·m<sub>n</sub>(f). [Esp. d.30]

</details>

## 13. Error más frecuente con f y ω

<details>
<summary>Ver respuesta</summary>

Calcular momentos en f y aplicar las fórmulas de ω (con 2π): los periodos salen **2π veces mayores**. Si el enunciado da ω en rad/s, T = 2π/ω; si da f en Hz, T = 1/f. [Esp. d.30; Cálc. d.17]

</details>

## 14. Espectro de banda ancha frente a banda estrecha

<details>
<summary>Ver respuesta</summary>

**Banda ancha**: SEA (mar de viento), energía repartida en muchas frecuencias.<br>
**Banda estrecha**: SWELL (mar de fondo), energía concentrada alrededor del pico. [Esp. d.20–21]

</details>

## 15. ¿Cómo distingues SEA y SWELL en un espectro con dos picos?

<details>
<summary>Ver respuesta</summary>

**Swell**: periodo mayor (pico a baja frecuencia), pico estrecho en frecuencia y dirección, viene de lejos.<br>
**Sea**: periodo más corto, pico ancho, dirección del viento local (¿viene de tierra? entonces no es swell). [Esp. d.20–23, 77; Estructura §3]

</details>

## 16. Espectro de una onda monocromática de altura H

<details>
<summary>Ver respuesta</summary>

Un único pico (delta) en ω<sub>0</sub> de área a²/2 = H²/8. Una bicromática da dos picos. [Esp. d.14]

</details>

## 17. Espectro escalar frente a direccional

<details>
<summary>Ver respuesta</summary>

S(ω, θ) reparte la energía en frecuencia y dirección; integrando en θ se obtiene el escalar: S(ω) = ∫S(ω, θ)dθ. m<sub>0</sub> es el área (escalar) o el volumen (direccional). [Esp. d.15–16, 19]

</details>

## 18. Ejercicio 1 espectral: cinco componentes con H y T. ¿Cómo sacas H<sub>m0</sub>?

<details>
<summary>Ver respuesta</summary>

Sumas E<sub>i</sub>/ρg = H<sub>i</sub>²/8 de cada componente (= m<sub>0</sub> ≈ 4,0 m²) y aplicas H<sub>m0</sub> = 4√m<sub>0</sub> = **8,00 m**. El periodo no interviene. [Esp. d.75–76]

</details>

## 19. Ejercicio 2 espectral: S(ω) = 2ω (0–0,8) y 8/3 − 4ω/3 (0,8–2). Resultados

<details>
<summary>Ver respuesta</summary>

m<sub>0</sub> = 1,6 (dos triángulos) · m<sub>1</sub> = 1,493 · m<sub>2</sub> = 1,664 · m<sub>4</sub> = 2,815<br>
H<sub>s</sub> = 5,06 m · Ē = 16 088 J/m² · T<sub>p</sub> = 2π/0,8 = 7,85 s · T<sub>01</sub> = 6,73 s · T<sub>z</sub> = 6,16 s · ε = 0,62<br>
Ojo: la diapo da T<sub>c</sub> = 4,23 s con exponente 3/4; con la fórmula correcta √(m<sub>2</sub>/m<sub>4</sub>) sale **4,83 s**. [Esp. d.78–80; Cálc. d.17]

</details>

## 20. ¿Qué es el fetch y qué es la duración?

<details>
<summary>Ver respuesta</summary>

**Fetch**: zona (distancia X) sobre la que sopla un viento estacionario y uniforme; meteorológico (campo de vientos) o geográfico (zona de mar disponible).<br>
**Duración**: tiempo que sopla ese viento sobre el fetch. [Esp. d.37]

</details>

## 21. Oleaje totalmente desarrollado frente a parcialmente desarrollado

<details>
<summary>Ver respuesta</summary>

**OTD**: equilibrio entre lo que aporta el viento y lo que se pierde por rotura y rozamiento con la atmósfera.<br>
**OPD**: aún creciendo, limitado por fetch o por duración. [Esp. d.39–40]

</details>

## 22. ¿Cómo crece el espectro por la acción del viento?

<details>
<summary>Ver respuesta</summary>

Ondas capilares → captan energía → crece el peralte y rompen (whitecapping), que limita la alta frecuencia → el pico se desplaza a frecuencias bajas por interacciones no lineales → cuando c<sub>p</sub> ≈ 1,2U el viento deja de aportar → equilibrio (OTD). [Esp. d.38]

</details>

## 23. ¿Qué es el rango de saturación (o de equilibrio)?

<details>
<summary>Ver respuesta</summary>

Frecuencias por encima del pico donde el peralte límite fija un máximo de energía. Phillips: S(ω) = α·g²·ω<sup>−5</sup>. [Esp. d.38, 41–42]

</details>

## 24. Espectro de Pierson-Moskowitz: qué representa y de qué depende

<details>
<summary>Ver respuesta</summary>

Oleaje **totalmente desarrollado**; **no depende del fetch**, solo del viento U (a 19,5 m). ω<sub>p</sub> = 0,879·g/U; H<sub>m0</sub> ≈ 0,04·T<sub>p</sub>² (m<sub>0</sub> = 0,0001·T<sub>p</sub>⁴). [Esp. d.45–46]

</details>

## 25. Espectro JONSWAP: qué representa y en qué se diferencia del PM

<details>
<summary>Ver respuesta</summary>

Oleaje **parcialmente desarrollado** (fetch limitado). Es un PM multiplicado por el factor de intensificación de pico γ<sup>δ</sup>: **pico más afilado**. Medio: γ = 3,3 (1–7), σ<sub>a</sub> = 0,07, σ<sub>b</sub> = 0,09. [Esp. d.48, 51]

</details>

## 26. ¿Qué pasa con JONSWAP al aumentar el fetch o el viento?

<details>
<summary>Ver respuesta</summary>

Aumentan T<sub>p</sub> y H<sub>m0</sub>. Crece con el fetch hasta alcanzar el PM (≈ 175 km con U = 10 m/s); a partir de ahí se toma el PM. [Esp. d.49–50]

</details>

## 27. ¿Cómo se representa el swell con JONSWAP?

<details>
<summary>Ver respuesta</summary>

Al propagarse fuera de la zona de generación el espectro se estrecha en frecuencia y dirección: se ajusta con JONSWAP de γ creciente con la distancia, de 3 hasta ≈ 10. [Esp. d.53]

</details>

## 28. Espectros bimodales

<details>
<summary>Ver respuesta</summary>

Swell lejano + sea local: dos picos. Ochi-Hubble (1976) o, más simple, superponer dos espectros unimodales manteniendo cada m<sub>0</sub>. [Esp. d.58–59]

</details>

## 29. Función de dispersión direccional

<details>
<summary>Ver respuesta</summary>

S(ω, θ) = S(ω)·D(θ, ω). Mitsuyasu: D ∝ cos<sup>2s</sup>[(θ−θ<sub>0</sub>)/2]; s<sub>max</sub> = 10 sea, 25 swell corto, 75 swell largo (más s = más concentrado). [Esp. d.60–61]

</details>

## 30. Relaciones entre parámetros espectrales y estadísticos

<details>
<summary>Ver respuesta</summary>

H<sub>m0</sub> ≈ H<sub>1/3</sub> (Rayleigh: 4,004√m<sub>0</sub>; medido en indefinidas ≈ 3,8√m<sub>0</sub>) · T<sub>02</sub> ≈ T<sub>z</sub> · T<sub>1/3</sub> no se obtiene teóricamente del espectro (JONSWAP γ = 3,3: T<sub>1/3</sub> ≈ 0,93·T<sub>p</sub>). [Esp. d.67–73]

</details>

## 31. Potencia (flujo de energía) del oleaje en indefinidas

<details>
<summary>Ver respuesta</summary>

P = ρg∫C<sub>g</sub>S dω; en indefinidas P = ρg²H<sub>m0</sub>²T<sub>e</sub>/(64π) ≈ **0,49·H<sub>m0</sub>²·T<sub>e</sub>** kW/m, con T<sub>e</sub> = T<sub>−1,0</sub>. [Esp. d.18]

</details>

## 32. ¿Qué fijan el paso de muestreo Δt y la duración T del registro?

<details>
<summary>Ver respuesta</summary>

Δt fija la frecuencia máxima f<sub>Nyq</sub> = 1/(2Δt) (por encima hay aliasing). T fija la resolución Δf = 1/T. [Esp. d.31; Cálc. d.7]

</details>

## 33. Periodograma: ventaja e inconveniente

<details>
<summary>Ver respuesta</summary>

FFT del registro completo: **máxima resolución** (Δf = 1/T) pero **error del 100 %** en cada punto. Alargar el registro da más puntos, no puntos más precisos. [Cálc. d.8]

</details>

## 34. Método de Welch

<details>
<summary>Ver respuesta</summary>

**Trocear** en K segmentos, **ventana** de Hann, **solape** del 50 % y **promediar**. Gana estabilidad (error ≈ 1/√N<sub>s</sub>, ≈ 18 % con K = 16) y pierde resolución (Δf = K/T). [Cálc. d.9–10]

</details>

## 35. ¿Por qué ε y T<sub>c</sub> son poco fiables en espectros medidos?

<details>
<summary>Ver respuesta</summary>

Usan m<sub>4</sub>, que no converge (cola en f<sup>−5</sup>): depende de la frecuencia de corte y del ruido. Para la anchura, mejor ν; para diseño, T<sub>p</sub>, T<sub>01</sub> y T<sub>z</sub>. [Esp. d.32]

</details>

## 36. Espectro de respuesta de un buque

<details>
<summary>Ver respuesta</summary>

Si la respuesta es lineal: S<sub>R</sub>(ω) = |RAO(ω)|²·S(ω). Respuesta significante = 4√m<sub>0R</sub>; con Rayleigh, probabilidad de superar un límite operativo. [Esp. d.33]

</details>
