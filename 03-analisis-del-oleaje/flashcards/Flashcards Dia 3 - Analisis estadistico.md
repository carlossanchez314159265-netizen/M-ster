# Flashcards · Día 3 · Análisis estadístico · 34 preguntas

Intenta responder antes de desplegar la solución. Marca las falladas para el último repaso. Son las mismas tarjetas del archivo de Anki (mazo `anki/Oceanografia - Dia 3 - Analisis estadistico.apkg`).

**Fuentes:** el resumen y las diapositivas de este bloque. Las tarjetas no llevan número de diapositiva: si fallas una, búscala en el resumen del día.

## 1. ¿Qué diferencia hay entre análisis del oleaje a corto y a largo plazo?

<details>
<summary>Ver respuesta</summary>

**Corto plazo**: propiedades ola a ola de **un** estado de mar. **Largo plazo**: propiedades de un **conjunto** de estados de mar a lo largo de años (regímenes medio y extremal).

</details>

## 2. ¿Qué significa que el oleaje sea un proceso **estacionario**?

<details>
<summary>Ver respuesta</summary>

Que sus momentos estadísticos (media, varianza…) no cambian al trasladar el origen de tiempos. Ese intervalo es el **estado de mar**.

</details>

## 3. ¿Qué significa que el oleaje sea un proceso **ergódico**?

<details>
<summary>Ver respuesta</summary>

Que sus propiedades estadísticas promedio se pueden deducir de **una única muestra** suficientemente larga.

</details>

## 4. ¿Por qué se puede suponer que el oleaje es un proceso **gaussiano**?

<details>
<summary>Ver respuesta</summary>

Por el **teorema central del límite**: es la suma de muchos trenes de onda independientes (Pierson, 1958). Media cero; queda definido por la varianza.

</details>

## 5. ¿Cuánto dura un estado de mar?

<details>
<summary>Ver respuesta</summary>

Hoy se usa **1 h**; el mínimo por información estadística es ≈ **20–30 min** (límite clásico de las boyas). Compromiso entre estacionariedad y estadística suficiente.

</details>

## 6. ¿Cuándo deja de ser gaussiana la superficie libre?

<details>
<summary>Ver respuesta</summary>

Al **aumentar la amplitud** y **disminuir la profundidad**: en profundidades reducidas el proceso no es gaussiano.

</details>

## 7. En el análisis de paso por cero, ¿qué es una ola?

<details>
<summary>Ver respuesta</summary>

El tramo entre dos **pasos ascendentes por cero** (PAC) consecutivos. H<sub>i</sub> = distancia vertical máxima entre ellos; T<sub>i</sub> = tiempo entre ellos.

</details>

## 8. ¿Dan lo mismo el paso ascendente (PAC) y el descendente (PDC)?

<details>
<summary>Ver respuesta</summary>

Olas distintas pero **estadística equivalente** en registros largos, salvo en reducidas o rompientes: la asimetría de las crestas da periodos menores con PDC.

</details>

## 9. ¿Cuántas olas hacen falta para una estadística fiable?

<details>
<summary>Ver respuesta</summary>

Al menos **100**; recomendable **1000** (30 min – 1 h de registro; 3 h para 1000 olas con T ≈ 15 s).

</details>

## 10. Define H<sub>1/3</sub> (H<sub>s</sub>)

<details>
<summary>Ver respuesta</summary>

Media de las alturas del **tercio de olas más altas** del registro (N/3). Propuesta por Sverdrup y Munk (1947) para casar medidas con observación visual.

</details>

## 11. Define T<sub>1/3</sub>

<details>
<summary>Ver respuesta</summary>

Media de los periodos de las N/3 olas **más altas** (ordenadas por altura, no por periodo).

</details>

## 12. Define H<sub>rms</sub>

<details>
<summary>Ver respuesta</summary>

H<sub>rms</sub> = √[(1/N) Σ H<sub>i</sub>²]: altura media cuadrática. Es el parámetro de la distribución de Rayleigh.

</details>

## 13. ¿Qué distribución sigue la superficie libre η en indefinidas y qué limitación tiene?

<details>
<summary>Ver respuesta</summary>

**Normal** de media cero y σ = η<sub>rms</sub>. Da igual probabilidad a crestas y senos → solo vale para oleaje **lineal**.

</details>

## 14. ¿Qué indican el sesgo y la curtosis de η?

<details>
<summary>Ver respuesta</summary>

**No linealidades**. Sesgo: crestas cortas y peraltadas, senos largos y planos (reducidas). Curtosis: apuntamiento frente a la normal. Ambos nulos → normal.

</details>

## 15. Distribución de Rayleigh: F(H) y probabilidad de excedencia

<details>
<summary>Ver respuesta</summary>

F(H) = 1 − exp[−(H/H<sub>rms</sub>)²];  P(H > H*) = exp[−(H*/H<sub>rms</sub>)²]

</details>

## 16. ¿Cuándo es válida la distribución de Rayleigh para las alturas de ola?

<details>
<summary>Ver respuesta</summary>

Espectro de **banda estrecha** (swell), olas **independientes** y oleaje **lineal**.

</details>

## 17. Altura superada por una fracción q de las olas (Rayleigh)

<details>
<summary>Ver respuesta</summary>

H<sub>q</sub> = H<sub>rms</sub>·√(−ln q)

</details>

## 18. Altura superada por el 2 % de las olas con H<sub>rms</sub> = 3 m

<details>
<summary>Ver respuesta</summary>

H<sub>2%</sub> = 3·√(−ln 0,02) = 3·1,978 = **5,93 m**

</details>

## 19. Rayleigh: H<sub>1/3</sub> en función de H<sub>rms</sub>

<details>
<summary>Ver respuesta</summary>

H<sub>1/3</sub> = **1,416**·H<sub>rms</sub>

</details>

## 20. Rayleigh: H<sub>m</sub> (media) en función de H<sub>rms</sub>

<details>
<summary>Ver respuesta</summary>

H<sub>m</sub> = 0,886·H<sub>rms</sub> (= √π/2·H<sub>rms</sub>);  H<sub>1/3</sub>/H<sub>m</sub> = 1,597

</details>

## 21. Rayleigh: H<sub>1/10</sub> en función de H<sub>rms</sub> y de H<sub>1/3</sub>

<details>
<summary>Ver respuesta</summary>

H<sub>1/10</sub> = 1,800·H<sub>rms</sub> = 1,271·H<sub>1/3</sub>

</details>

## 22. Relación entre H<sub>1/3</sub> y la desviación típica de η (Rayleigh)

<details>
<summary>Ver respuesta</summary>

H<sub>1/3</sub> = 4,004·η<sub>rms</sub> = 4,004√m<sub>0</sub> (de ahí H<sub>m0</sub> = 4√m<sub>0</sub>)

</details>

## 23. Distribución de H<sub>max</sub> en un estado de mar de N olas (Longuet-Higgins, 1952)

<details>
<summary>Ver respuesta</summary>

F(H<sub>max,N</sub>) = [F(H)]<sup>N</sup> = {1 − exp[−(H<sub>max</sub>/H<sub>rms</sub>)²]}<sup>N</sup>. Más olas (más duración) → más probable una ola mayor.

</details>

## 24. H<sub>max</sub> **más probable** (moda) en N olas

<details>
<summary>Ver respuesta</summary>

H<sub>max,moda</sub> = H<sub>rms</sub>·√(ln N)

</details>

## 25. H<sub>max</sub> **media** en N olas

<details>
<summary>Ver respuesta</summary>

H<sub>max,media</sub> = H<sub>rms</sub>·[√(ln N) + (C/2)(ln N)<sup>−1/2</sup>], C = 0,57722 (Euler)

</details>

## 26. ¿Cómo se calcula N para la H<sub>max</sub>?

<details>
<summary>Ver respuesta</summary>

N = duración del estado de mar / periodo medio. Ej.: 3600 s / 7,2 s = 500 olas.

</details>

## 27. Ejemplo diapo 42: 1 h, T<sub>m</sub> = 7,2 s, H<sub>rms</sub> = 3 m. H<sub>max</sub> más probable y media

<details>
<summary>Ver respuesta</summary>

N = 500; √ln 500 = 2,493 → **moda 7,48 m**; media 2,609·3 = 7,83 m (la diapo da la media). Ojo: el enunciado dice H<sub>rms</sub> = 5 → 12,46 m.

</details>

## 28. Regla rápida: H<sub>max</sub> frente a H<sub>s</sub> en 1–3 h

<details>
<summary>Ver respuesta</summary>

H<sub>max</sub> ≈ 1,8–2·H<sub>s</sub> (1,76 con N = 500; 1,86 con N = 1000)

</details>

## 29. Limitaciones de Rayleigh

<details>
<summary>Ver respuesta</summary>

**Sobrestima** las olas mayores (hasta ≈ 10 % en la cola) porque supone banda estrecha, independencia entre olas (hay grupos) y no considera no linealidades (asimetrías, rotura, rompientes).

</details>

## 30. ¿Qué es una freak (rogue) wave y su criterio?

<details>
<summary>Ver respuesta</summary>

Ola anormal, muy peraltada y mucho mayor que las que la rodean. Haver (2000): **H<sub>max</sub>/H<sub>s</sub> > 2** y/o **η<sub>max</sub>/H<sub>s</sub> > 1,25**.

</details>

## 31. ¿De qué surgen las freak waves y cuándo son más probables?

<details>
<summary>Ver respuesta</summary>

Concentración por interacción entre frecuencias, interacción ola–corriente, inestabilidades no lineales. Más probables en mares **peraltados y de banda estrecha**.

</details>

## 32. Distribución conjunta H–T de Longuet-Higgins: ¿de qué depende?

<details>
<summary>Ver respuesta</summary>

De la anchura espectral ν² = m<sub>0</sub>m<sub>2</sub>/m<sub>1</sub>² − 1; la moda de los periodos decrece al aumentar ν.

</details>

## 33. Frecuencia acumulada empírica de N olas ordenadas de mayor a menor

<details>
<summary>Ver respuesta</summary>

F(H ≤ H<sub>i</sub>) = (N + 1 − i)/N

</details>

## 34. ¿Qué fracción de olas supera H<sub>s</sub> según Rayleigh?

<details>
<summary>Ver respuesta</summary>

exp(−1,416²) ≈ **13,5 %**

</details>
