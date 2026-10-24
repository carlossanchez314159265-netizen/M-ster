# Flashcards · Día 1 · Introducción · 25 preguntas

Intenta responder antes de desplegar la solución. Marca las falladas para el último repaso. Son las mismas tarjetas del archivo de Anki (mazo `anki/Oceanografia - Dia 1 - Introduccion.apkg`).

**Fuentes:** el resumen y las diapositivas de este bloque. Las tarjetas no llevan número de diapositiva: si fallas una, búscala en el resumen del día.

## 1. ¿Qué mide la PSU?

<details>
<summary>Ver respuesta</summary>

La **salinidad práctica**: adimensional, calculada a partir de la conductividad (escala PSS-78).<br>
35 PSU ≈ 35 g/kg ≈ 35 ‰

</details>

## 2. ¿Qué corriente se genera por diferencias de temperatura y salinidad?

<details>
<summary>Ver respuesta</summary>

La **circulación termohalina** (termo = temperatura, halina = sal).

</details>

## 3. ¿Cómo se llama la capa donde la temperatura cae rápido con la profundidad?

<details>
<summary>Ver respuesta</summary>

**Termoclina**. Está bajo la capa de mezcla; el 90 % del océano queda por debajo (0–3 °C).<br>
Haloclina = salinidad · Picnoclina = densidad

</details>

## 4. ¿Qué es σ = ρ − 1000 kg/m³?

<details>
<summary>Ver respuesta</summary>

La **anomalía de densidad**. Ej.: ρ = 1025 → σ = 25

</details>

## 5. Densidad típica del agua de mar

<details>
<summary>Ver respuesta</summary>

≈ **1025 kg/m³** en superficie; hasta ≈ 1050 en el fondo.

</details>

## 6. Propiedad conservativa vs no conservativa

<details>
<summary>Ver respuesta</summary>

**Conservativa** (T, S): dentro del océano solo cambia por mezcla → identifica masas de agua.<br>
**No conservativa** (O₂, nutrientes): cambia también por procesos químicos y biológicos.

</details>

## 7. ¿Qué es la temperatura potencial (θ)?

<details>
<summary>Ver respuesta</summary>

La temperatura que tendría el agua llevada **adiabáticamente a la superficie** (p = 0). Sirve para comparar aguas a distinta profundidad; se usa en los diagramas T-S.

</details>

## 8. Factores que aumentan / disminuyen la salinidad

<details>
<summary>Ver respuesta</summary>

**Aumentan**: evaporación, formación de hielo.<br>
**Disminuyen**: lluvia, deshielo, ríos y escorrentía.

</details>

## 9. Salinidad práctica (SP) vs absoluta (SA)

<details>
<summary>Ver respuesta</summary>

**SP**: PSU, adimensional, conductividad, PSS-78.<br>
**SA**: g/kg, masa de sales, TEOS-10, más precisa.

</details>

## 10. ¿Qué es la haloclina?

<details>
<summary>Ver respuesta</summary>

Capa con cambio rápido de salinidad. Permanente (desembocadura de río) o efímera (tras lluvia intensa).

</details>

## 11. ¿Qué es la picnoclina?

<details>
<summary>Ver respuesta</summary>

Capa con cambio brusco de densidad. Barrera a la mezcla vertical → **estratificación**.

</details>

## 12. Ecuación de estado UNESCO (1983)

<details>
<summary>Ver respuesta</summary>

ρ(s,T,p) = ρ(s,T,0) / [1 − p / K(s,T,p)]<br>
ρ(s,T,0) = A + B·s + C·s^1.5 + D·s²<br>
K = módulo de compresibilidad secante

</details>

## 13. ¿Qué es TEOS-10?

<details>
<summary>Ver respuesta</summary>

Estándar actual de las propiedades termodinámicas del agua de mar (sustituye a EOS-80). En Matlab: toolbox GSW, p. ej. gsw_rho(SA,CT,p).

</details>

## 14. ¿Qué es la densidad potencial (σθ, σ₀, σ₂…)?

<details>
<summary>Ver respuesta</summary>

La densidad llevada adiabáticamente a una presión de referencia (normalmente 0 dbar). Quita el efecto de la presión → comparar aguas y estudiar estabilidad.

</details>

## 15. Agua Mediterránea: ¿dónde se forma y qué la hace densa?

<details>
<summary>Ver respuesta</summary>

Mediterráneo noroccidental en invierno: el **Mistral** la evapora y la enfría.<br>
Baja a ≈ 2000 m (T = 12,8 °C, S = 38,4), sale por Gibraltar bajo el agua atlántica y en el Atlántico se queda a ≈ 1000 m.

</details>

## 16. Procesos de formación de masas de agua

<details>
<summary>Ver respuesta</summary>

**Convección profunda** (zonas polares, se densifica y se hunde) · **Subducción** (subtropicales, convergencia) · **Mezcla**

</details>

## 17. ¿Qué es un agua tipo?

<details>
<summary>Ver respuesta</summary>

Masa de agua de T y S homogéneas → un **punto** en el diagrama T-S.

</details>

## 18. Mezcla de dos aguas tipo (m₁ de A, m₂ de B)

<details>
<summary>Ver respuesta</summary>

T = (m₁T₁ + m₂T₂)/(m₁+m₂) · S = (m₁S₁ + m₂S₂)/(m₁+m₂)<br>
Queda sobre la recta A–B. %A = b/(a+b)·100

</details>

## 19. ¿Qué es el cabbeling?

<details>
<summary>Ver respuesta</summary>

Mezclar dos aguas de **igual densidad** pero distinta T y S da un agua **más densa**, porque las isopicnas son curvas.

</details>

## 20. Estabilidad de la columna: dσθ/dz > 0, < 0, = 0

<details>
<summary>Ver respuesta</summary>

&gt; 0 → **estable** · &lt; 0 → **inestable** · = 0 → **neutra**<br>
En T-S: curva paralela a las isopicnas = neutra

</details>

## 21. Ramas de la oceanografía

<details>
<summary>Ver respuesta</summary>

Física · Química · Biológica (ecología oceánica) · Geológica · Operacional

</details>

## 22. ¿Qué es la oceanografía operacional?

<details>
<summary>Ver respuesta</summary>

Observación sistemática y casi en tiempo real + modelos + difusión rápida (hindcast, nowcast, forecast). Ej.: Copernicus Marine Service (CMEMS).

</details>

## 23. Fases del ciclo de vida de un parque eólico marino

<details>
<summary>Ver respuesta</summary>

1. Desarrollo · 2. Construcción · 3. Operación (O&amp;M) · 4. Desmantelamiento. Vida mínima ≈ 35 años.

</details>

## 24. Datos meteo-oceánicos ideales para diseño

<details>
<summary>Ver respuesta</summary>

Alta calidad, series largas (+25 años), homogéneas, continuas y con resolución espacial y temporal adecuada (horaria).

</details>

## 25. Esfera de titanio (Menorca): planteamiento del lastre

<details>
<summary>Ver respuesta</summary>

lastre = ρ_agua·V − m<br>
V = 4,189 m³ · m ≈ 2693 kg<br>
Superficie ≈ 1603 kg · 450 m ≈ 1617 kg → **+14 kg** (agua más densa: más fría y más comprimida)

</details>
