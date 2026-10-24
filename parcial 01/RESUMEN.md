# Resumen de emergencia · IINT

Lee para entender y después intenta explicar cada apartado sin mirar. Para ir directamente a los ejercicios: [práctica](PRACTICA.md).

## 1. La idea que une toda la asignatura

**Necesidad → expectativas y uso → requisitos → funciones → conceptos de solución → arquitectura → diseño → integración y comprobación.**

No es una cadena rígida: hay iteraciones y se revisan decisiones. La trazabilidad conserva las relaciones entre niveles.

Un **sistema** es un conjunto de elementos relacionados que produce un resultado que no ofrecen por separado. La ingeniería de sistemas coordina disciplinas, personas, procesos y tecnología para satisfacer necesidades durante todo el ciclo de vida. Optimizar cada pieza aisladamente no garantiza optimizar el conjunto.

**Ejemplo:** un radar detecta y una consola muestra datos, pero si sus formatos o tiempos son incompatibles, la vigilancia puede fallar. Descomponer facilita diseñar, asignar responsabilidades y verificar; también crea interfaces y dependencias que habrá que gestionar.

**Modelo en V:** a la izquierda se definen necesidades y requisitos y se descompone el diseño; en la base se implementa; a la derecha se integra y comprueba por niveles, relacionándolos con lo especificado. No significa esperar al final para pensar las pruebas.

- **Verificación:** ¿cumple los requisitos especificados?
- **Validación:** ¿resuelve la necesidad y sirve para el uso previsto?

Un sistema puede superar una prueba de alcance y aun así no cubrir la misión real. También se validan los requisitos: se comprueba que expresan adecuadamente las necesidades, no solo que estén bien redactados.

**Fuentes:** B1 pp.6–9, 21–23, 32–34; B2 pp.3–6; B3 p.7.

## 2. Stakeholders, SVN y CONOPS

**Stakeholder:** persona, grupo o entidad que afecta al sistema o resulta afectado por él. Piensa en cliente, operador, mantenedor, proveedor, autoridad y usuarios durante todo el ciclo de vida. Sus intereses pueden entrar en conflicto.

- **Necesidad:** problema que se quiere resolver.
- **Meta:** lo que se quiere conseguir para resolverlo.
- **Objetivo:** concreción de la meta que permite evaluar su consecución.

Una **SVN**, red de valor de stakeholders, representa quién aporta y recibe valor, incluyendo relaciones indirectas. Por ejemplo: operador → mantenedor, financiación e información; mantenedor → operador, servicio y disponibilidad. No es una arquitectura de equipos.

El **CONOPS** describe cómo se utilizará el sistema desde la perspectiva del usuario: quién, para qué, dónde, cuándo, escenarios, interacciones y condiciones. No debe confundirse con una lista de componentes.

**Caso de los apuntes: Blue Horizon.** Parque eólico con 60 aerogeneradores situado a 40 km de Barcelona. Los trabajos piden identificar stakeholders y sus intercambios, redactar un CONOPS y después derivar requisitos, medidas y trazabilidad.

**Ejemplo de CONOPS de práctica:** durante la operación del parque, el sistema vigila las aproximaciones, detecta posibles intrusiones y envía alertas al centro de control. El operador evalúa la situación y activa el procedimiento previsto. Deben definirse condiciones ambientales y operación degradada. Todavía no hemos elegido radar ni cámara.

**Fuentes:** B2 pp.10–16, 20–26 y 57.

## 3. Requisitos: el apartado que debes practicar escribiendo

Un requisito transforma una expectativa en una obligación formal que el sistema debe cumplir. Debe ser **claro, viable, verificable, consistente, apropiado al nivel y trazable**, sin redundancias y completo en su contexto.

**Plantilla útil:** «El sistema deberá [acción o prestación] [umbral] bajo [condiciones]». Es una ayuda, no una garantía automática de calidad.

**Mal:** «El sistema será rápido y empleará el mejor radar».

**Mejor, con cifras supuestas para practicar:** «El sistema deberá emitir una alarma en un máximo de 10 segundos desde la detección, bajo las condiciones operativas acordadas». Para cerrar la especificación habría que concretar dichas condiciones. La prueba mide el intervalo entre detección y emisión.

| Tipo | Qué expresa | Ejemplo orientativo |
|---|---|---|
| Funcional | Qué hace | Generar una alarma al detectar una intrusión |
| Rendimiento | Cuánto o cómo de bien | Emitirla en un máximo de 10 segundos |
| Interfaz | Intercambio o conexión | Formato de los mensajes entre detector y consola |
| Operativo | Condiciones de utilización | Prestaciones exigidas en el entorno de operación |
| Mantenimiento | Condiciones para mantenerlo | Tiempo máximo de sustitución de un módulo |
| Seguridad | Protección frente a daños | Respuesta segura ante un fallo definido |
| Derivado | Consecuencia de requisitos o decisiones superiores | Necesidad de energía de un subsistema elegido |

Las categorías pueden relacionarse: explica qué aspecto estás clasificando. Evita introducir una solución concreta antes de tiempo, salvo que sea una restricción justificada. **Shall** expresa obligación; **should**, una meta o recomendación que no sustituye las obligaciones.

Métodos de verificación de los apuntes: **examen/inspección, prueba, demostración y análisis**. El método se elige según lo que deba comprobarse y se documenta junto con la fase.

**Fuentes:** B2 pp.21, 34, 36–38, 41–43; B3 pp.6–7.

## 4. MOE, MOP, TPM y trazabilidad

| Medida | Pregunta que responde | Ejemplo |
|---|---|---|
| MOE: efectividad | ¿Cumplimos el objetivo de la misión? | Porcentaje de intrusiones detectadas |
| MOP: prestación | ¿Qué rendimiento ofrece el sistema? | Alcance de detección o tiempo de alarma |
| TPM: medida técnica | ¿Qué parámetro técnico seguimos durante el desarrollo? | Potencia del radar, resolución de cámara |

**Trampa:** MOE no equivale necesariamente a medida cualitativa. Aunque B2 p.45 usa esa etiqueta, incluye porcentajes y tiempos como ejemplos. La diferencia útil es el propósito y el nivel de la medida.

La **trazabilidad** conecta necesidades, requisitos, funciones, elementos y pruebas. Permite comprobar cobertura, detectar omisiones y analizar el impacto de un cambio.

**Ejemplo orientativo:** necesidad de proteger el parque → R-01, detectar una embarcación de referencia a 2 km bajo condiciones definidas → función detectar → subsistema de detección → T-01, ensayo a esa distancia. Los 2 km proceden del ejemplo de los apuntes; las condiciones y criterios de aceptación deben completarse para una prueba real.

**Fuentes:** B2 pp.45, 51–55; B3 pp.3, 34–35.

## 5. QFD: saber interpretar y calcular

QFD traduce la voz del cliente a características técnicas y ayuda a priorizarlas.

- **Filas:** necesidades del cliente, los «qués», con importancia asignada.
- **Columnas:** descriptores técnicos, los «cómos».
- **Matriz central:** relación entre cada qué y cada cómo. En el ejemplo: fuerte **9**, media **3**, débil **1**, sin relación **0**.
- **Tejado:** relaciones entre características técnicas: apoyos y conflictos.

**Prioridad absoluta de una columna:** suma de `importancia de cada necesidad × relación con esa característica`.

Ejemplo de autonomía del dron, B3 p.33:

`5×9 + 5×9 + 5×1 + 3×1 = 98`.

Si se pide prioridad relativa: `100 × prioridad de la columna / suma de prioridades de todas las columnas`. No dividas entre el número de necesidades. No puedes calcular el porcentaje sin conocer el total.

**Ejemplo nuevo:** si una columna vale 59 y el total es 200, su prioridad relativa es 29,5 %.

Más batería puede aumentar autonomía y peso: es un compromiso del tejado. La matriz central expresa influencia sobre necesidades, no correlaciones entre características técnicas. Después se fijan objetivos, se comparan alternativas y se refinan los descriptores.

**Fuentes:** B3 pp.17, 22–33.

## 6. Análisis funcional: verbos antes que componentes

Un requisito expresa lo que se debe cumplir. Una **función** es una actividad o transformación necesaria: detectar, procesar, comunicar. El análisis funcional descompone funciones, asigna prestaciones y estudia interfaces antes de concretar la solución física.

| Herramienta | Pregunta que ayuda a responder |
|---|---|
| FFBD | ¿Qué funciones se realizan y en qué orden lógico? |
| IDEF0 | ¿Qué necesita una función, qué la controla, con qué se ejecuta y qué produce? |
| Diagrama de actividades | ¿Cuál es el flujo de trabajo, con decisiones y paralelismos? |
| Diagrama de estados | ¿En qué estados puede estar y qué provoca transiciones? |
| Diagrama de secuencia | ¿Quién intercambia mensajes con quién y en qué orden? |
| TLS | ¿Cuándo se ejecutan las funciones, cuánto duran y cuáles se solapan? |
| N² | ¿Qué intercambios e interfaces existen entre funciones o elementos? |
| Matriz de interfaces | ¿Cómo documentamos esos intercambios de forma estructurada? |

**FFBD de práctica:** captar datos → procesar → clasificar → comunicar. «Cámara → ordenador → antena» enumera componentes, no funciones.

**IDEF0 de práctica: detectar un objetivo**

```text
                   Controles: reglas de detección
                                 ↓
Entradas: imágenes → [ DETECTAR OBJETIVO ] → Salidas: detección
                                 ↑
                 Mecanismos: procesador y software
```

Entrada a la izquierda, control arriba, salida a la derecha, mecanismo abajo. Una regla regula la ejecución; un mecanismo aporta recursos; una entrada es procesada por la función.

**Fuentes:** B3 pp.34–37, 40–47. La p.47 es el resumen visual más útil.

## 7. Función, concepto, arquitectura y diseño

| Concepto | Ejemplo con un dron |
|---|---|
| Función: qué hace | Inspeccionar aerogeneradores y transmitir información |
| Forma: elementos que lo materializan | Sensores, batería, motores, software, enlace |
| Concepto: enfoque general de solución | Dron autónomo con sensores visuales y térmicos para inspección marina |
| Arquitectura: organización, asignaciones e interfaces | Relación de plataforma, sensores, energía, navegación, comunicaciones y estación de control |
| Diseño: concreción detallada | Dimensiones, materiales, modelos de componentes y parámetros |

La **arquitectura lógica** describe funciones, flujos, comportamientos y relaciones. La **física** organiza los elementos que realizan esas funciones. No basta un dibujo: los modelos, relaciones y decisiones deben ser coherentes.

**Diseño directo:** partir de la función para definir la forma. **Ingeniería inversa:** partir de una solución existente para deducir funciones y organización.

**Generar conceptos:** ampliar alternativas, pensamiento divergente. **Seleccionar:** reducirlas mediante criterios, pensamiento convergente. Considerar necesidades, prestaciones, coste, riesgo, restricciones y ciclo de vida.

**Ejemplo del tren:** necesidad, reducir tiempo de viaje; concepto, permitir mayor velocidad en curvas inclinando la caja; arquitectura, organizar funciones, componentes e interfaces que detectan, controlan y producen esa inclinación. «Inclinar la caja» todavía no describe una arquitectura completa.

Una buena arquitectura estructura el sistema, asigna funciones, gestiona interfaces y complejidad, y permite operar, mantener y evolucionar la solución. El valor relaciona beneficios con costes durante el ciclo de vida.

**Fuentes:** B4 pp.7–10, 14, 16–31.

## 8. Vocabulario de repaso breve

- **Ciclo de vida:** considerar desarrollo, construcción, operación, mantenimiento y retirada; no solo la entrega.
- **Decision gate:** revisión de decisión con criterios de entrada/salida para autorizar o condicionar el avance. Toda DG es revisión e hito, pero no todo hito es una DG. Puede dar lugar a continuar, continuar con acciones, mantener en espera, reelaborar, suspender o cancelar.
- **SRR:** revisión temprana de requisitos para detectar ausencias, errores o redundancias y establecer su control.
- **Volatilidad de requisitos:** adiciones, modificaciones y eliminaciones. Se gestionan con control de cambios y trazabilidad.
- **Iceberg:** eventos → patrones → estructuras → modelos mentales. Los fallos visibles pueden tener causas organizativas profundas; son hipótesis que deben investigarse.
- **SysML:** lenguaje para modelar requisitos, estructura, comportamiento e interfaces; no es una marca de software.
- **OPM:** objetos, estados y procesos que transforman objetos o estados.
- **Modelica:** modelado y simulación física mediante ecuaciones, multidominio y acausal. No obliga a fijar de antemano qué variable es entrada o salida.
- **QFD / diseño axiomático / TRIZ:** traducir y priorizar necesidades / relacionar requisitos funcionales y parámetros buscando independencia y baja complejidad / apoyar la resolución inventiva de problemas. Son complementarios.

**Fuentes:** B1 pp.14–17, 41, 46–50; B3 pp.12–16, 50–52, 55–58.

## Última comprobación

Sin mirar, explica V y verificación/validación; escribe un requisito medible; distingue MOE/MOP/TPM; calcula una columna QFD; dibuja IDEF0; diferencia función, concepto, arquitectura y diseño. Si te atascas, vuelve a ese apartado y repite con otro ejemplo.
