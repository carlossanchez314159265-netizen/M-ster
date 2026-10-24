# Flashcards · Recetas y trampas del examen · 15 preguntas

Intenta responder antes de desplegar la solución. Marca las falladas para el último repaso. Son las mismas tarjetas del archivo de Anki (mazo `anki/Oceanografia - Examen - Recetas y trampas.apkg`).

**Fuentes:** *Estructura §X* = sección X de [Análisis de la estructura del examen](<../00 - Analisis de la estructura del examen.pdf>); *P25* = [1er Parcial 29-10-2025](<../Examen 1er Parcial 29-10-2025 (resuelto).pdf>); *F25* = [Final 13-01-2025](<../Examen Final ordinario 1er Parcial 13-01-2025 (resuelto).pdf>); *Esp. d.X* = diapositiva del Espectral.

## 1. ¿Qué estructura tiene la hoja de ejercicios del 1er parcial?

<details>
<summary>Ver respuesta</summary>

3 ejercicios de 2 puntos: **A** dispersión/teoría lineal, **B** Rayleigh + H<sub>max</sub>, **C** espectral. Los ejercicios pesan ≈ 60 % (dato de solo 2 exámenes). [Estructura §1–2]

</details>

## 2. Regla antes de calcular

<details>
<summary>Ver respuesta</summary>

Identifica el bloque (A, B o C) y escribe su receta. Cada ejercicio son 4–6 líneas: si llevas media cara, vas por mal camino. Los resultados suelen ser casi redondos. [Estructura §1, §5]

</details>

## 3. Receta A: te dan L en indefinidas y L en la estructura. ¿h y T?

<details>
<summary>Ver respuesta</summary>

T de L<sub>0</sub> = gT²/2π (el periodo se conserva). Con k = 2π/L: tanh(kh) = ω²/(gk) → **h = arctanh(ω²/gk)/k**, sin iterar. Comprueba el régimen con h/L.<br>
(156 m y 140 m → T ≈ 10 s, h ≈ 32,4 m) [F25 Ej. 1]

</details>

## 4. Receta A: dos sensores de presión, uno en el fondo. ¿Cómo sacas k, h y H?

<details>
<summary>Ver respuesta</summary>

p<sub>din</sub> = ρg(H/2)·cosh k(h+z)/cosh kh. Dividiendo: p<sub>2</sub>/p<sub>1</sub> = cosh(k·Δz) → **k** (Δz = altura del sensor 2 sobre el fondo). Luego h con la dispersión (arctanh) y H volviendo a una presión. [P25 Ej. 2]

</details>

## 5. Receta B: probabilidad de que el oleaje alcance una cubierta a cota Z

<details>
<summary>Ver respuesta</summary>

H<sub>rms</sub> = H<sub>s</sub>/√2. La ola crítica es **H<sub>q</sub> = 2Z** (la cresta es H/2). q = exp[−(H<sub>q</sub>/H<sub>rms</sub>)²].<br>
(H<sub>s</sub> = 9,5 m, Z = 5 m → q ≈ 11 %) [P25 Ej. 1a]

</details>

## 6. Receta B: cota para que no haya rebase en todo el temporal

<details>
<summary>Ver respuesta</summary>

N = duración/T. ⟨H<sub>max,N</sub>⟩ = H<sub>rms</sub>·[√(ln N) + (0,57722/2)(ln N)<sup>−1/2</sup>]. Cota = **⟨H<sub>max</sub>⟩/2**.<br>
(3 h, T = 12 s, H<sub>s</sub> = 9,5 → N = 900, H<sub>max</sub> = 18,3 m, cota 9,13 m) [P25 Ej. 1b]

</details>

## 7. Receta B con runup: R<sub>u</sub> = η<sub>max</sub> + u²/2g

<details>
<summary>Ver respuesta</summary>

η<sub>max</sub> = ⟨H<sub>max,N</sub>⟩/2 y u = (Hω/2)·coth(kh) en superficie bajo la cresta, **con H = ⟨H<sub>max</sub>⟩**, no H<sub>s</sub>.<br>
(H<sub>s</sub> = 8 m, T<sub>p</sub> = 14 s, h = 40 m, 3 h → R<sub>u</sub> ≈ 8,6 m) [F25 Ej. 2]

</details>

## 8. Receta C: el espectro viene como figura (triángulos, conos)

<details>
<summary>Ver respuesta</summary>

m<sub>0</sub> = **área** (1D) o **volumen** (direccional). Triángulo ½·b·h; cono ⅓·A<sub>base</sub>·altura. Luego H<sub>m0</sub> = 4√m<sub>0</sub>, E = ρgm<sub>0</sub>, T<sub>p</sub> = 2π/ω<sub>p</sub>. [P25 Ej. 3; Estructura §3]

</details>

## 9. Receta C: S(ω) por tramos

<details>
<summary>Ver respuesta</summary>

Integra ωⁿS(ω) tramo a tramo para m<sub>0</sub>, m<sub>1</sub>, m<sub>2</sub>; comprueba m<sub>0</sub> con el área de la figura. T<sub>02</sub> = 2π√(m<sub>0</sub>/m<sub>2</sub>), T<sub>01</sub> = 2π·m<sub>0</sub>/m<sub>1</sub>: si piden «periodo medio», di cuál calculas.<br>
(1,5ω y 4 − ω/2 → m<sub>0</sub> = 12, H<sub>m0</sub> = 13,86 m, T<sub>p</sub> = 3,14 s) [F25 Ej. 3]

</details>

## 10. Oleaje compuesto SEA + SWELL: ¿cómo se combinan las alturas?

<details>
<summary>Ver respuesta</summary>

Se suman los **m<sub>0</sub>**, nunca las alturas: H = √(H<sub>1</sub>² + H<sub>2</sub>²). Con 4 m y 2 m → **4,47 m**, no 6 m. [P25 Ej. 3; Estructura §4]

</details>

## 11. Trampa: ¿H<sub>max</sub> media o más probable?

<details>
<summary>Ver respuesta</summary>

El profesor usa la **media**, con la constante de Euler C = 0,57722. La moda H<sub>rms</sub>√(ln N) da unos 0,4 m menos de cota. [Estructura §4; P25 Ej. 1b]

</details>

## 12. Trampa: comparar la ola con una cota

<details>
<summary>Ver respuesta</summary>

Lo que llega a la cubierta es la **cresta = H/2**, no H. Y para «que no pase nunca» se usa ⟨H<sub>max,N</sub>⟩, no H<sub>s</sub>. [Estructura §4]

</details>

## 13. Trampa: redondear k antes del arctanh

<details>
<summary>Ver respuesta</summary>

arctanh es muy sensible cerca de 1: arrastra **4 cifras** en k y en ω²/gk. [Estructura §4; P25 Ej. 2]

</details>

## 14. Trampa: el periodo al llegar a aguas someras

<details>
<summary>Ver respuesta</summary>

El **periodo se conserva**; lo que cambia es L (y C). No recalcules T en la estructura. [Estructura §4; F25 Ej. 1]

</details>

## 15. Trampa: el 2π del espectro

<details>
<summary>Ver respuesta</summary>

Espectro en ω (rad/s): T = 2π/ω y los periodos medios llevan 2π. En f (Hz): T = 1/f, sin 2π. Si un periodo sale absurdo, revisa esto. [Estructura §4; Esp. d.30]

</details>
