# Flashcards · Día 2 · Mecánica de ondas · 53 preguntas

Intenta responder antes de desplegar la solución. Marca las falladas para el último repaso. Son las mismas tarjetas del archivo de Anki (mazo `anki/Oceanografia - Dia 2 - Mecanica de ondas.apkg`).

**Fuentes:** el resumen y las diapositivas de este bloque. Las tarjetas no llevan número de diapositiva: si fallas una, búscala en el resumen del día.

## 1. ¿Qué periodos tienen las ondas gravitatorias generadas por el viento que interesan en ingeniería?

<details>
<summary>Ver respuesta</summary>

Entre **3 y 30 s** (en la tabla general: 1–30 s, L de 1 a 10³ m).

</details>

## 2. ¿Por qué se llama «onda gravitatoria» al oleaje de viento?

<details>
<summary>Ver respuesta</summary>

Porque la **fuerza restauradora** dominante es la **gravedad**. Si L es de pocos cm domina la tensión superficial → **ondas capilares**.

</details>

## 3. ¿De qué depende que crezca el oleaje generado por el viento?

<details>
<summary>Ver respuesta</summary>

Velocidad del viento (mayor que la de las crestas), **duración**, **fetch** y profundidad. Con fricción y rotura se llega al **oleaje completamente desarrollado**.

</details>

## 4. Diferencia entre oleaje y onda

<details>
<summary>Ver respuesta</summary>

**Oleaje**: real, aleatorio, irregular → estadística y espectros.<br>
**Onda**: modelo determinista, regular y monocromático → teoría de ondas.

</details>

## 5. ¿Cuándo H = 2a?

<details>
<summary>Ver respuesta</summary>

Solo si A<sub>cresta</sub> = A<sub>seno</sub>, es decir, en **teoría lineal**. En general H = A<sub>c</sub> + A<sub>s</sub>.

</details>

## 6. Definiciones de k, ω y C

<details>
<summary>Ver respuesta</summary>

k = 2π/L<br>
ω = 2π/T<br>
C = L/T = ω/k

</details>

## 7. Onda progresiva vs estacionaria (expresión de η)

<details>
<summary>Ver respuesta</summary>

Progresiva: η = a·cos(kx − ωt) (acopladas)<br>
Estacionaria: η = a·cos(kx)·cos(ωt) (desacopladas, nodos fijos)

</details>

## 8. ¿A qué distancia están un nodo y el antinodo contiguo?

<details>
<summary>Ver respuesta</summary>

**L/4** (dos nodos seguidos, L/2).

</details>

## 9. Peralte, altura relativa y profundidad relativa

<details>
<summary>Ver respuesta</summary>

ε = H/L (ka)<br>
δ = H/h<br>
μ = h/L (kh)

</details>

## 10. Límites de profundidades indefinidas, intermedias y reducidas

<details>
<summary>Ver respuesta</summary>

Indefinidas: h/L &gt; 1/2 (kh &gt; π)<br>
Intermedias: 1/20 &lt; h/L &lt; 1/2<br>
Reducidas: h/L &lt; 1/20 (kh &lt; π/10)

</details>

## 11. Peralte máximo antes de rotura en profundidades indefinidas

<details>
<summary>Ver respuesta</summary>

H/L = **0,142 ≈ 1/7**

</details>

## 12. Número de Ursell

<details>
<summary>Ver respuesta</summary>

U<sub>r</sub> = H·L²/h³ = δ/μ². Sirve para elegir la teoría: pequeño → lineal; grande → cnoidal / solitaria (umbral ≈ 26).

</details>

## 13. Ejes del ábaco de Le Méhauté

<details>
<summary>Ver respuesta</summary>

x = h/gT² (profundidad)<br>
y = H/gT² (peralte)

</details>

## 14. Régimen de Stokes vs régimen de onda larga

<details>
<summary>Ver respuesta</summary>

**Stokes**: kh ≥ 1 (indefinidas/intermedias) → lineal (Airy = Stokes 1er orden), Stokes II, III…<br>
**Onda larga**: kh ≪ 1 (reducidas) → cnoidal, solitaria.

</details>

## 15. Hipótesis de la teoría potencial de ondas

<details>
<summary>Ver respuesta</summary>

Fluido continuo, homogéneo, **incompresible** y **no viscoso**; solo gravedad; sin tensión superficial ni Coriolis; p<sub>a</sub> cte; flujo **irrotacional**; fondo impermeable.

</details>

## 16. ¿Por qué se puede despreciar la viscosidad?

<details>
<summary>Ver respuesta</summary>

Lejos de los contornos Re = UL/ν ≈ 10⁸.

</details>

## 17. ¿Por qué se puede despreciar Coriolis?

<details>
<summary>Ver respuesta</summary>

El periodo de la ola es despreciable frente a la rotación terrestre; Coriolis es ≈ 1000 veces menor que la inercia.

</details>

## 18. ¿Qué ecuación da la continuidad en función del potencial?

<details>
<summary>Ver respuesta</summary>

La **ecuación de Laplace**: ∇²φ = 0

</details>

## 19. Condiciones de contorno del problema de ondas

<details>
<summary>Ver respuesta</summary>

Cinemática en el fondo (∂φ/∂z = 0 en z = −h), cinemática en superficie libre, dinámica en superficie libre (Bernoulli con p = p<sub>a</sub>), laterales (periodicidad) y temporal.

</details>

## 20. ¿Por qué el problema completo es no lineal y cómo se linealiza?

<details>
<summary>Ver respuesta</summary>

Las condiciones se imponen en η (incógnita) y tienen términos cuadráticos.<br>
Pequeña amplitud (H/L ≪ 1): se imponen en **z = 0** y se desprecian los productos de términos pequeños.

</details>

## 21. Ecuación de la dispersión

<details>
<summary>Ver respuesta</summary>

**ω² = g·k·tanh(kh)**<br>
L = (gT²/2π)·tanh(2πh/L)

</details>

## 22. L₀ y C₀ en profundidades indefinidas

<details>
<summary>Ver respuesta</summary>

L₀ = gT²/2π = **1,56·T²**<br>
C₀ = gT/2π = **1,56·T**

</details>

## 23. Celeridad en profundidades reducidas

<details>
<summary>Ver respuesta</summary>

C = √(gh): **no dispersiva**, todas las olas van igual de rápido.

</details>

## 24. ¿Qué significa que el oleaje sea dispersivo?

<details>
<summary>Ver respuesta</summary>

Que C depende del periodo: las olas de **mayor T viajan más rápido** y se separan (dispersión frecuencial).

</details>

## 25. Si baja la profundidad con T fijo, ¿qué pasa con L y C?

<details>
<summary>Ver respuesta</summary>

Disminuyen ambas → origen de la **refracción**.

</details>

## 26. ¿Cómo se resuelve la ecuación de la dispersión?

<details>
<summary>Ver respuesta</summary>

Es trascendente: tablas, gráficos o numérico (**Newton-Raphson**, arranque k₀ = ω²/g) o explícitas (Fenton-McKee &lt; 1,5 %, Guo &lt; 0,7 %). En examen: SOLVE.

</details>

## 27. Límites de tanh, sinh y cosh

<details>
<summary>Ver respuesta</summary>

kh → ∞: tanh → 1; sinh, cosh → e<sup>kh</sup>/2<br>
kh → 0: tanh → kh; sinh → kh; cosh → 1

</details>

## 28. Velocidades u y w en teoría lineal

<details>
<summary>Ver respuesta</summary>

u = aω·cosh k(h+z)/sinh kh·cos θ<br>
w = aω·sinh k(h+z)/sinh kh·sin θ<br>
(θ = kx − ωt)

</details>

## 29. ¿Dónde son máximas u y w en una onda progresiva?

<details>
<summary>Ver respuesta</summary>

u: bajo **crestas y senos** (θ = 0, π)<br>
w: en los **pasos por cero** (θ = π/2, 3π/2). Desfasadas π/2.

</details>

## 30. ¿Qué pasa con u y w en el fondo?

<details>
<summary>Ver respuesta</summary>

w = 0 (condición de contorno) pero **u ≠ 0** (deslizamiento, fluido ideal). a<sub>z</sub> = 0, a<sub>x</sub> ≠ 0.

</details>

## 31. Velocidades en profundidades reducidas

<details>
<summary>Ver respuesta</summary>

u **uniforme** en la vertical; w crece **linealmente** desde 0 en el fondo; u<sub>máx</sub>/w<sub>máx</sub> = 1/kh.

</details>

## 32. Semiejes de la órbita de una partícula

<details>
<summary>Ver respuesta</summary>

Horizontal (mayor): A = a·cosh k(h+z)/sinh kh<br>
Vertical (menor): B = a·sinh k(h+z)/sinh kh<br>
**B/A = tanh k(h+z)**

</details>

## 33. Forma de las órbitas según la profundidad

<details>
<summary>Ver respuesta</summary>

Indefinidas: **círculos** de radio a·e<sup>kz</sup><br>
Intermedias: **elipses** que se achatan<br>
Reducidas: elipses muy planas, semieje horizontal constante

</details>

## 34. Campo de presiones en teoría lineal

<details>
<summary>Ver respuesta</summary>

p = −ρgz + ρga·K<sub>p</sub>·cos θ<br>
K<sub>p</sub> = cosh k(h+z)/cosh kh (factor de respuesta de presión)

</details>

## 35. Ley de presiones en reducidas

<details>
<summary>Ver respuesta</summary>

K<sub>p</sub> = 1 → p = ρg(η − z): **hidrostática (triangular)**.

</details>

## 36. Onda estacionaria: expresión y altura

<details>
<summary>Ver respuesta</summary>

η = 2a·cos(kx)·cos(ωt): **altura doble** que la incidente. Reflexión perfecta.

</details>

## 37. Estacionaria: ¿dónde son máximas u y w?

<details>
<summary>Ver respuesta</summary>

u máxima en los **nodos**; w máxima en los **antinodos**.

</details>

## 38. Posición de nodos y antinodos de la estacionaria

<details>
<summary>Ver respuesta</summary>

Nodos: kx = (2n+1)π/2<br>
Antinodos: kx = nπ

</details>

## 39. Envolvente de la onda cuasi-estacionaria

<details>
<summary>Ver respuesta</summary>

η<sub>máx</sub> = ½(H<sub>i</sub> + H<sub>r</sub>) (antinodos)<br>
η<sub>mín</sub> = ½(H<sub>i</sub> − H<sub>r</sub>) (cuasi-nodos)<br>
K<sub>r</sub> = H<sub>r</sub>/H<sub>i</sub>

</details>

## 40. ¿Qué superposición da ondas de crestas cortas?

<details>
<summary>Ver respuesta</summary>

Dos progresivas de igual T y amplitud, **distinta dirección (±θ)** y mismo sentido: progresa en x y es estacionaria en y.

</details>

## 41. Grupo de ondas: expresión de η

<details>
<summary>Ver respuesta</summary>

η = H·cos(kx − ωt)·cos[½(Δk·x − Δω·t)]<br>
portadora × envolvente

</details>

## 42. Celeridad de grupo

<details>
<summary>Ver respuesta</summary>

C<sub>g</sub> = Δω/Δk → dω/dk = **n·C**, n = ½[1 + 2kh/sinh 2kh]

</details>

## 43. Valor de n en profundas y reducidas

<details>
<summary>Ver respuesta</summary>

Profundas: n = ½ → C<sub>g</sub> = C/2<br>
Reducidas: n = 1 → C<sub>g</sub> = C = √(gh)

</details>

## 44. Periodo y longitud del grupo

<details>
<summary>Ver respuesta</summary>

T<sub>g</sub> = 2π/Δω = T₁T₂/(T₁ − T₂)<br>
L<sub>g</sub> = 2π/Δk<br>
(función modulante: 4π/Δω)

</details>

## 45. Dispersión con corriente uniforme

<details>
<summary>Ver respuesta</summary>

σ² = (ω − U₀k cosθ − V₀k sinθ)² = gk·tanh kh<br>
σ = intrínseca; ω = absoluta

</details>

## 46. Energía total media del oleaje

<details>
<summary>Ver respuesta</summary>

**E = ρgH²/8** (J/m²); mitad cinética, mitad potencial (ρgH²/16 cada una). **No depende de T ni de h.**

</details>

## 47. Flujo de energía

<details>
<summary>Ver respuesta</summary>

**F = E·C<sub>g</sub> = E·n·C** (W/m)<br>
Profundas: F = ρg²H²T/(32π)

</details>

## 48. ¿A qué velocidad viaja la energía del oleaje y por qué?

<details>
<summary>Ver respuesta</summary>

A **C<sub>g</sub>**: por los nodos del grupo no pasa energía (allí H = 0 y la presión dinámica es nula).

</details>

## 49. ¿Por qué hay transporte neto de masa si las órbitas son cerradas?

<details>
<summary>Ver respuesta</summary>

La velocidad bajo la cresta es algo mayor que bajo el seno → flujo neto en el sentido de avance: M = ρgH²/(8C).

</details>

## 50. Ejercicio tipo: te dan L en indefinidas y L sobre la plataforma. ¿Cómo sacas h?

<details>
<summary>Ver respuesta</summary>

T de L₀ = gT²/2π; con k = 2π/L despejas: tanh(kh) = ω²/(gk) → h = atanh(…)/k. Sin iterar.<br>
(312 m y 200 m → T = 14,1 s, h ≈ 24,2 m)

</details>

## 51. Ejercicio tipo: te dan los semiejes de la órbita a una profundidad z. ¿Primer paso?

<details>
<summary>Ver respuesta</summary>

B/A = tanh k(h+z) → k. Luego T con la dispersión y H con el semieje mayor.

</details>

## 52. Tiempo de viaje de un tsunami sobre un talud h(x)

<details>
<summary>Ver respuesta</summary>

Onda larga: C = √(gh(x)) → t = ∫ dx / √(g·h(x)).<br>
(200 m, pendiente 0,005 → ≈ 30 min)

</details>

## 53. Cómo sacar H<sub>i</sub> y H<sub>r</sub> de una envolvente medida

<details>
<summary>Ver respuesta</summary>

H<sub>i</sub> + H<sub>r</sub> = altura en el antinodo<br>
H<sub>i</sub> − H<sub>r</sub> = altura en el cuasi-nodo<br>
(distancia entre ambos = L/4)

</details>
