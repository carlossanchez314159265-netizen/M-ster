# Preguntas de desarrollo · definición de conceptos

24 preguntas de «define y explica», con **respuestas cortas** para repasar rápido. Preguntas originales a partir de las presentaciones, **no de exámenes anteriores**.

**Cómo responder en el examen:** definición → 3 o 4 ideas clave → ejemplo → diferencia con lo que se confunde.

**Uso rápido:** lee la pregunta, di la respuesta en voz alta o en 4–5 líneas, y abre la solución para comprobarla.

---

## B1 · Introducción y conceptos

### 1. ¿Qué es un sistema?

<details><summary>Respuesta</summary>

Conjunto de elementos **relacionados** que, juntos, producen un resultado que **no dan por separado**.
- Si quitas una parte, se pierde funcionalidad; en un montón, solo quedan menos piezas.
- Características: composición, jerarquía, interacción, dinamismo, heterogeneidad y propósito definido.
- «No es una colección de partes: es una red de relaciones».

**Ejemplo:** un buque: casco, propulsión, energía y navegación solo transportan carga juntos.
**Ojo:** no lo definas solo como «conjunto de piezas». *B1 pp.5–11.*
</details>

### 2. ¿Qué es la ingeniería de sistemas?

<details><summary>Respuesta</summary>

Enfoque **transdisciplinar** que gestiona la complejidad equilibrando las necesidades de los stakeholders e integrando personas, procesos, información y tecnología **durante todo el ciclo de vida**. Su marco es la ISO/IEC/IEEE 15288.
- Foco: requisitos, arquitectura, interfaces, riesgos, integración, V&V.
- Es una inversión que reduce retrabajo, retrasos y sobrecostes, aunque no lo garantiza.

**Ejemplo:** la sonda perdida en Marte por mezclar unidades imperiales y métricas: fallo de interfaces y de validación extremo a extremo.
**Ojo:** no es diseñar componentes aislados. *B1 pp.7–8, 32–39.*
</details>

### 3. Complejidad y descomposición jerárquica

<details><summary>Respuesta</summary>

Descomponemos porque la complejidad supera nuestra capacidad: **ley de Miller**, manejamos **7 ± 2** elementos a la vez.
- Se divide en niveles para que cada uno sea abarcable (#niveles ≈ log₇ #piezas).
- Ventaja: es más fácil diseñar, repartir trabajo y verificar.
- Precio: más **interfaces, dependencias y problemas de integración**. La complejidad no desaparece, se gestiona.

**Ejemplo:** puzle de 500 piezas hecho por 500 personas aisladas: no encaja.
*B1 pp.21–26.*
</details>

### 4. Pensamiento sistémico y modelo del iceberg

<details><summary>Respuesta</summary>

Ver el **todo** y cómo interactúan las partes, no solo los problemas visibles.
- **Eventos:** qué vemos.
- **Patrones:** qué se repite.
- **Estructuras:** qué los genera (organización).
- **Modelos mentales:** qué creencias hay detrás.

Si solo atacas el evento, el problema vuelve.
**Ejemplo:** fallos de datos en integración (evento) → se repiten en cada proyecto (patrón) → equipos en silos (estructura) → «la integración se arregla al final» (modelo mental).
*B1 pp.14–17.*
</details>

### 5. Ciclo de vida y decision gates

<details><summary>Respuesta</summary>

**Ciclo de vida:** etapas desde la necesidad hasta la **retirada** (requisitos, diseño, integración, V&V, operación, mantenimiento, retirada).
- Hay que equilibrar coste, funcionalidad y plazo (**triángulo de hierro**).
- Se controla con revisiones, hitos y **decision gates**.
- **DG:** revisión formal con criterios de entrada y salida para decidir si se avanza. Resultados: GO, GO WITH ACTIONS, HOLD, RECYCLE, SUSPEND, KILL.
- Toda DG es revisión e hito, pero no todo hito es una DG.

*B1 pp.46–50.*
</details>

### 6. Sistema de sistemas (SoS)

<details><summary>Respuesta</summary>

Conjunto de sistemas **independientes, heterogéneos y distribuidos** que colaboran en una misión mayor.
- Cada uno tiene su propietario y su **ciclo de vida**.
- Límites cambiantes y requisitos ambiguos o cambiantes.

**Ejemplo:** vigilancia de un puerto: radar costero + AIS + salvamento + centro de control.
*B1 p.18.*
</details>

---

## B2 · Stakeholders y requisitos

### 7. ¿Qué es un stakeholder?

<details><summary>Respuesta</summary>

Persona, grupo, entidad o regulación que **afecta o se ve afectada** por el sistema.
- Kochan y Rubinstein: **tiene activos críticos, los invierte y puede influir**.
- **Directos:** cumplen los tres (cliente, operador, astillero). **Indirectos o latentes:** no (medios, ciudadanía).
- Hay que identificarlos en todas las fases y equilibrar sus conflictos.

**Ejemplo Blue Horizon:** operador, centro de control, mantenimiento, autoridad marítima, navegantes.
*B2 pp.10–12.*
</details>

### 8. Necesidades, metas y objetivos (NGO)

<details><summary>Respuesta</summary>

- **Necesidad:** lo que se quiere resolver.
- **Meta:** lo que hay que conseguir para resolverlo.
- **Objetivo:** concreta la meta de forma evaluable.

Deben alinearse y ser aceptadas por los stakeholders.
**Ejemplo:** intrusiones en el parque → detectar a tiempo las aproximaciones → detectar el 95 % de intrusiones (cifra de práctica).
*B2 p.13.*
</details>

### 9. SVN (red de valor de stakeholders)

<details><summary>Respuesta</summary>

Modelo de **quién da y recibe valor**, incluidas las relaciones **indirectas**.
- **Efecto de segundo orden:** te llega a través de otro (regulador → astillero → proveedor → mantenimiento).
- **Bucle de valor:** intercambio circular continuo (operador → ingeniería → mantenimiento → disponibilidad → cliente).
- Sirve para ver stakeholders y flujos importantes y reducir complejidad.

**Ejemplo:** caso BP: los medios influyeron más de lo previsto.
**Ojo:** no es una arquitectura de equipos. *B2 pp.14–20.*
</details>

### 10. CONOPS

<details><summary>Respuesta</summary>

Documento que describe **cómo se usará el sistema desde el punto de vista del usuario**: quién, para qué, dónde, cuándo y en qué condiciones.
- Elementos: propósito y alcance, operaciones, interacciones del usuario, entorno operativo.
- Sirve para comunicar expectativas y descubrir requisitos.
- Es como el **guion de una película**: qué pasa, no cómo está construido.
- **ConOps** = intención de uso (caja negra); **OpsCon** = qué hará el sistema, sin decir cómo.

**Ejemplo:** el sistema vigila el parque y alerta al centro de control, que activa el protocolo.
**Ojo:** no elige equipos. *B2 pp.23–25, 44.*
</details>

### 11. Requisito y requisito bien definido

<details><summary>Respuesta</summary>

**Expectativa:** lo que quiere el stakeholder, en lenguaje informal. **Requisito:** enunciado formal de lo que **debe cumplir** el sistema y que se puede **verificar**.
- Bien definido: realizable, verificable, claro, completo, consistente, apropiado al nivel, no redundante y **expresado como necesidad, no como solución**.
- Lleva **métrica + valor** y usa *shall*.

**Ejemplo:** «que aguante la mala mar» → «mantendrá 12 nudos en estado de mar 5».
**Ojo:** evitar «etc.», «y/o», «amigable». *B2 pp.6, 21, 36–41.*
</details>

### 12. Tipos de requisitos

<details><summary>Respuesta</summary>

| Tipo | Pregunta | Ejemplo |
|---|---|---|
| Funcional | ¿Qué hace? | Detectar embarcaciones |
| Rendimiento | ¿Cuánto? | A 2 millas |
| Interfaz | ¿Con quién se conecta? | Enviar alertas al centro de control |
| Operativo | ¿En qué condiciones? | Operar 24/7 |
| Mantenimiento | ¿Cómo se mantiene? | Cambiar el radar en < 30 min |
| Seguridad | ¿Cómo evitamos daños? | Impedir accesos no autorizados |
| Derivado | ¿Qué sale de decisiones de diseño? | Dron → estación de carga |

*B2 p.34.*
</details>

### 13. Proceso de definición de requisitos

<details><summary>Respuesta</summary>

Convierte necesidades y restricciones en requisitos claros, verificables y trazables.
- **Entradas:** necesidades, problema, restricciones.
- **Controles** (lo que debo cumplir): leyes, normas, acuerdos.
- **Capacitadores** (lo que me ayuda): personas, herramientas, recursos.
- **Salidas:** especificación de requisitos, criterios de validación, CONOPS, MOE, matriz de trazabilidad.

**Requisitos ≠ especificación:** los requisitos son la entrada del diseño; la especificación es el resultado.
*B2 pp.8, 50–55.*
</details>

### 14. Trazabilidad

<details><summary>Respuesta</summary>

Capacidad de seguir las relaciones **necesidad → requisito → función → elemento → prueba**, en los dos sentidos.
- Comprueba **cobertura**: que no falta ningún requisito.
- Permite analizar el **impacto de un cambio**.
- Se documenta en la **matriz de trazabilidad**.

**Ejemplo:** proteger el parque → R-01: detectar a 2 km → función detectar → subsistema de detección → ensayo T-01.
**Ojo:** no evita cambios, ayuda a gestionarlos. *B2 pp.51–55.*
</details>

---

## B3 · Definición y análisis de requisitos

### 15. SyRS y SRR

<details><summary>Respuesta</summary>

**SyRS:** especificación de requisitos del sistema; la **línea base**, completa, precisa y no ambigua, con sus MOE, MOP y TPM.
- Cada requisito: claro, verificable, trazable, sin conflictos y sin implementación concreta.
- Define los niveles L1 (sistemas) y L2 (subsistemas).

**SRR:** revisión temprana de requisitos (Fase A) para encontrar los que faltan, sobran o están mal. Después, los requisitos pasan a **gestión de configuración**.
*B3 pp.5, 12.*
</details>

### 16. Volatilidad e isoperformance

<details><summary>Respuesta</summary>

**Volatilidad:** cuánto cambian los requisitos (añadir, modificar, eliminar).
- Causas: nuevas necesidades, normativa, CONOPS que madura, errores.
- Impacto: coste, plazo, retrabajo.
- Se **gestiona** con control de cambios y trazabilidad; no se elimina.

**Isoperformance:** combinaciones de parámetros de diseño que dan el **mismo rendimiento**. Evita fijar soluciones pronto.
**Ejemplo:** mismo alcance con más potencia de radar o con la antena más alta.
*B3 pp.13–14.*
</details>

### 17. QFD, diseño axiomático y TRIZ

<details><summary>Respuesta</summary>

- **QFD:** traduce la **voz del cliente** a características técnicas y las **prioriza**. House of Quality: filas = qués, columnas = cómos, centro = relaciones (9/3/1), tejado = conflictos entre cómos.
- **Diseño axiomático:** relaciona requisitos funcionales con parámetros de diseño. Axiomas de **independencia** y de **información** (mínima complejidad).
- **TRIZ:** resuelve **contradicciones técnicas** con principios inventivos.

QFD prioriza, el axiomático estructura, TRIZ innova.
*B3 pp.16–33.*
</details>

### 18. Análisis funcional

<details><summary>Respuesta</summary>

Traduce requisitos en **funciones** que el sistema debe realizar, sin decidir todavía cómo.
- Define funciones, estados y modos, interfaces y asigna rendimiento a funciones.
- Su resultado es la **arquitectura funcional**.
- Herramientas: FFBD e IDEF0 (funciones), estados, actividades y secuencia (comportamiento), N² y matriz de interfaces (interfaces).

**Ejemplo:** «vigilar 100 km²» → detectar, navegar, capturar imágenes, transmitir.
**Ojo:** «cámara 8K» ya es diseño. *B3 pp.36–47.*
</details>

### 19. Lenguajes de modelado

<details><summary>Respuesta</summary>

Hacen falta para que todas las vistas describan **el mismo sistema** sin incoherencias.
- Partes: **ontología** (qué entidades existen), **semántica** (qué significan), **sintaxis** (reglas).
- **SysML:** extensión de UML; modela requisitos, estructura, comportamiento e interfaces.
- **OPM:** objetos, estados y procesos (ISO 19450).
- **Modelica:** simula sistemas físicos con ecuaciones, de forma acausal.

SysML **describe**; Modelica **simula**.
*B3 pp.49–58.*
</details>

---

## B4 · Arquitectura y diseño conceptual

### 20. Arquitectura

<details><summary>Respuesta</summary>

**Organización fundamental** de la solución: elementos, **funciones asignadas**, relaciones e **interfaces**.
- **Lógica:** cómo debe funcionar (funciones, flujos, estados). **Física:** qué elementos lo hacen.
- No es un dibujo: son modelos, decisiones y requisitos derivados.
- Se decide pronto y condiciona todo el ciclo de vida. Puede haber varias válidas.

**Ejemplo:** dron: plataforma, sensores, energía, navegación, comunicaciones y estación de control, con sus conexiones.
**Ojo:** una lista de piezas no es una arquitectura. *B4 pp.7–14.*
</details>

### 21. Función y forma

<details><summary>Respuesta</summary>

- **Función:** qué hace el sistema (verbos: detectar, transmitir).
- **Forma:** con qué lo hace (cámara, batería, software, personas).
- La arquitectura une funciones con elementos.
- **Diseño directo:** de la función a la forma. **Ingeniería inversa:** de una forma existente a sus funciones.

*B4 pp.16–18.*
</details>

### 22. Concepto de solución

<details><summary>Respuesta</summary>

Idea general de cómo satisfacer la necesidad, sin definir todos los elementos.
- Fórmula: **tipo de solución + característica diferenciadora + finalidad**.
- **Inicial:** la idea. **Desarrollado:** añade tecnologías y parámetros.
- El concepto es el **enfoque**; la arquitectura, **cómo se organiza**.

**Ejemplo RENFE:** necesidad, reducir el tiempo de viaje; concepto, inclinar la caja en curvas; arquitectura, funciones y elementos que detectan, controlan y producen la inclinación.
*B4 pp.20–25.*
</details>

### 23. Valor

<details><summary>Respuesta</summary>

Relación entre **beneficio** (necesidades satisfechas, funcionalidad, valor percibido) y **coste** (adquisición, operación, mantenimiento, tiempo).
- Una buena arquitectura maximiza el beneficio con un coste asumible en **todo el ciclo de vida**.
- Para concretar la necesidad: **operando → atributo → transformación → valor** (comida → conservación → ralentizar el deterioro → conservar más tiempo).

**Ojo:** valor no es «lo más barato». *B4 pp.26–27.*
</details>

### 24. Generar y seleccionar conceptos; arquitectura frente a diseño

<details><summary>Respuesta</summary>

- **Generar:** abrir alternativas, **pensamiento divergente** (brainstorming, matriz morfológica).
- **Seleccionar:** elegir con criterios, **pensamiento convergente** (valor, coste, riesgo).
- **Arquitectura:** bloques, funciones asignadas, interfaces, parámetros principales.
- **Diseño:** dimensiones, materiales, componentes y valores detallados.

**Orden:** entender la necesidad → generar → seleccionar → arquitectura → diseño.
*B4 pp.28–31.*
</details>
