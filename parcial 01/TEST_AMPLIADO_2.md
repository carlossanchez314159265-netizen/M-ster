# Test ampliado 2 · 80 preguntas nuevas

Tercer banco de preguntas, complementario a [PRACTICA.md](PRACTICA.md) y [TEST_AMPLIADO.md](TEST_AMPLIADO.md). **No repite** ninguna de sus 86 preguntas: cubre detalles de las presentaciones que aún no se preguntaban y añade casos aplicados (buque autónomo, salvamento, puerto) para practicar a reconocer los conceptos fuera del ejemplo de clase.

Preguntas originales elaboradas a partir de las presentaciones. **No son preguntas de exámenes anteriores.** Una sola respuesta correcta por pregunta. Las soluciones están al final de cada bloque, plegadas, con la referencia «B*n* p.*x*» al PDF original (portada = página 1). Los casos y cifras nuevos son supuestos de práctica.

Hay una versión autocorregible de este test en [test_interactivo_2.html](test_interactivo_2.html).

| Bloque | Preguntas | Temas |
|---|---|---|
| B1 · Introducción y conceptos | 1–17 | Tipos de sistema, SoS, procesos de la 15288, definiciones, ciclo de vida, optimización |
| B2 · Stakeholders y requisitos | 18–43 | Modelo en V, expectativas, SVN, CONOPS, generación, calidad y redacción de requisitos, medidas |
| B3 · Definición y análisis de requisitos | 44–66 | Actividades, SyRS, isoperformance, técnicas de análisis, QFD, análisis funcional, modelado |
| B4 · Arquitectura y diseño conceptual | 67–80 | Arquitectura lógica, proceso, función y forma, conceptos, valor, arquitectura frente a diseño |

---

## B1 · Introducción y conceptos

### 1. Un buque que intercambia energía, materia e información con su entorno es, por sus condiciones de contorno, un sistema…

- **A.** Cerrado.
- **B.** Abierto.
- **C.** Abstracto.
- **D.** Natural.

### 2. «Un sistema no es una colección de partes: es una red de relaciones». ¿Qué idea resume?

- **A.** La optimización local de cada pieza.
- **B.** La ley de Miller.
- **C.** La visión sistémica.
- **D.** El triángulo de hierro.

### 3. Se reparte un puzle de 500 piezas entre 500 personas que no se comunican y solo se monta al final. ¿Qué es lo esperable?

- **A.** Que encaje, si cada pieza está bien fabricada.
- **B.** Que baste con revisar cada pieza al final.
- **C.** Que aparezcan piezas que no encajan, repetidas o que faltan: fabricar una pieza no es construir un sistema.
- **D.** Que se resuelva añadiendo más personas.

### 4. «Si os toca fabricar la pieza 327, ¿qué necesitáis saber?». Al responder, en realidad estáis definiendo…

- **A.** El presupuesto del programa.
- **B.** Requisitos e interfaces.
- **C.** El CONOPS.
- **D.** Las MOE.

### 5. ¿Qué rasgo caracteriza a un sistema de sistemas (SoS)?

- **A.** Sus sistemas actúan de forma independiente y tienen ciclos de vida diferentes.
- **B.** Tiene límites fijos y bien definidos desde el inicio.
- **C.** Sus requisitos iniciales son siempre precisos.
- **D.** Lo controla y opera un único propietario.

### 6. Con #niveles = log₇(#piezas), ¿cuántos niveles corresponden a un equipo de 343 piezas?

- **A.** 2
- **B.** 3
- **C.** 49
- **D.** 7

### 7. Según la ley de Miller, ¿cuántos elementos manejamos a la vez en la memoria de trabajo?

- **A.** 3 ± 1.
- **B.** 12 ± 3.
- **C.** Un número ilimitado con entrenamiento.
- **D.** 7 ± 2, es decir, entre 5 y 9.

### 8. En los procesos de la ISO/IEC/IEEE 15288, «gestión de riesgos» y «gestión de configuración» pertenecen a…

- **A.** Procesos técnicos.
- **B.** Procesos de acuerdo.
- **C.** Procesos organizativos.
- **D.** Gestión técnica.

### 9. En la misma norma, «adquisición» y «suministro» son procesos de…

- **A.** Acuerdo, porque regulan la relación entre cliente y proveedor.
- **B.** Gestión técnica.
- **C.** Realización y uso.
- **D.** Definición y diseño.

### 10. ¿Qué idea comparten las definiciones de ingeniería de sistemas de INCOSE, ISO 15288 y NASA?

- **A.** Se centran en diseñar componentes aislados.
- **B.** Consideran todo el ciclo de vida, desde la concepción hasta la retirada.
- **C.** Solo se aplican durante la integración.
- **D.** Son exclusivas del software.

### 11. ¿Por qué se sitúa al ingeniero de sistemas en el centro de *architects/designers*, *developers* y *operators*?

- **A.** Porque sustituye a los tres perfiles.
- **B.** Porque solo trata con los operadores.
- **C.** Porque decide el presupuesto de cada perfil.
- **D.** Porque necesita comprender las tres perspectivas a la vez.

### 12. «Hacer un buen diseño y no sólo hacer bien el diseño» significa sobre todo…

- **A.** Usar más herramientas de cálculo.
- **B.** Reducir el número de revisiones.
- **C.** Asegurar que el diseño resuelve la necesidad adecuada, no solo que esté bien ejecutado.
- **D.** Diseñar primero los componentes más caros.

### 13. ¿Cuál es un parámetro crítico del *business case* a lo largo del ciclo de vida?

- **A.** El ROI (retorno de la inversión).
- **B.** El número de stakeholders.
- **C.** El tejado de la matriz QFD.
- **D.** La sintaxis del lenguaje de modelado.

### 14. ¿Qué riesgo se cita al exigir un análisis completo y riguroso en una decision gate?

- **A.** Que se omitan los criterios de entrada.
- **B.** Que se reduzca la trazabilidad.
- **C.** Que desaparezcan los hitos.
- **D.** La parálisis por el análisis.

### 15. ¿Qué es la *Holistic Ship Design Optimisation*?

- **A.** Minimizar solo el coste de construcción del casco.
- **B.** Optimizar cada disciplina por separado.
- **C.** Optimización multiobjetivo del diseño de un buque considerando todos sus aspectos y todo su ciclo de vida.
- **D.** Un método para clasificar stakeholders.

### 16. ¿Qué cambio en los procesos de ingeniería describe B1?

- **A.** De descubrir tarde y caro los problemas de integración a definir desde el principio qué queremos y cómo lo verificaremos.
- **B.** De verificar al inicio a verificar solo al final.
- **C.** De trabajar con requisitos a trabajar sin ellos.
- **D.** De integrar disciplinas a separarlas en silos.

### 17. En un buque autónomo, los equipos de radar y de software trabajan en silos y no tienen un acuerdo de interfaces común. En el iceberg, esto es…

- **A.** Un evento.
- **B.** Una estructura.
- **C.** Un patrón.
- **D.** Un modelo mental.

### Soluciones B1

<details>
<summary>Abrir solo después de responder</summary>

**1. B.** B1 p.10 clasifica los sistemas por sus condiciones de contorno en abiertos y cerrados. Un sistema abierto intercambia con su entorno; la definición es la habitual.

**2. C.** B1 p.11; el resultado global depende de las decisiones de todos los actores, B1 p.12.

**3. C.** Encajarán mal, habrá piezas repetidas o que faltan y colores que no coinciden. B1 pp.24–26.

**4. B.** B1 p.26.

**5. A.** Actúan de forma independiente, tienen distintos ciclos de vida, límites indefinidos y cambiantes y requisitos iniciales probablemente ambiguos. B1 p.18.

**6. B.** 7³ = 343, así que log₇(343) = 3. Ejercicio nuevo; método de B1 p.23.

**7. D.** B1 p.21.

**8. D.** La gestión técnica planifica, controla y da coherencia al proyecto. B1 p.41.

**9. A.** B1 p.41.

**10. B.** B1 pp.32–34.

**11. D.** B1 p.43.

**12. C.** B1 p.44 lo menciona junto a «verificar requisitos» y «validar funcionalidad». Hacer bien el diseño es cumplir lo especificado; hacer un buen diseño, que sirva a la necesidad.

**13. A.** Tiempo hasta el *break even*, ROI y *delivery*. B1 p.47.

**14. D.** B1 p.49.

**15. C.** B1 p.54.

**16. A.** B1 p.40.

**17. B.** Es la forma en que está organizado el sistema la que genera los patrones; responde a «¿qué genera esos patrones?». Caso nuevo; niveles de B1 p.17.

</details>

---

## B2 · Stakeholders y requisitos

### 18. Según B2, ¿por qué es útil la metodología en V?

- **A.** Porque elimina la necesidad de iterar.
- **B.** Porque solo se aplica al software.
- **C.** Porque reduce errores detectándolos antes, mejora la trazabilidad y facilita la coordinación entre disciplinas.
- **D.** Porque permite integrar sin pruebas intermedias.

### 19. «El sistema debe ser fiable» pasa a «la disponibilidad operativa será superior al 95 %». ¿Qué ilustra?

- **A.** El paso del lenguaje del cliente al de la ingeniería: de la necesidad a un requisito técnico verificable.
- **B.** Un requisito derivado de una decisión de diseño.
- **C.** Un error de sobreespecificación.
- **D.** Un concepto de solución.

### 20. En la tabla de expectativas, ¿qué espera típicamente un subcontratista o proveedor?

- **A.** Respeto al medio ambiente.
- **B.** Seguridad en el trabajo y primas.
- **C.** Cumplir compromisos internos de coste y plazo.
- **D.** Requisitos bien definidos.

### 21. En un SVN, ¿qué es un bucle de valor?

- **A.** Una consecuencia que llega al proyecto a través de otro stakeholder.
- **B.** Una relación circular en la que varios stakeholders intercambian valor de forma continua.
- **C.** Un requisito que se repite en varias especificaciones.
- **D.** Una revisión periódica con el cliente.

### 22. ¿Qué aporta el SVN al resaltar los stakeholders y flujos de valor importantes (WSO y WVFO)?

- **A.** Elimina a los stakeholders indirectos del análisis.
- **B.** Sustituye a la matriz de trazabilidad.
- **C.** Permite construir un modelo más pequeño para analizar con detalle, reduciendo la complejidad.
- **D.** Fija el presupuesto de cada stakeholder.

### 23. En el proceso de expectativa a requisito, ¿qué paso va justo después de describir el uso del sistema (casos de uso, escenarios, CONOPS)?

- **A.** Formalizar los requisitos.
- **B.** Definir cómo se validarán.
- **C.** Identificar a los stakeholders.
- **D.** Diseñar la arquitectura física.

### 24. ¿Cuál **no** es un elemento clave de un CONOPS?

- **A.** Propósito y alcance.
- **B.** Interacciones del usuario.
- **C.** Entorno operativo.
- **D.** Lista de proveedores y precios de los equipos.

### 25. ¿Qué quiere decir que un CONOPS es «como el guion de una película»?

- **A.** Que debe incluir planos de cada elemento.
- **B.** Que cuenta qué ocurre durante la operación, no cómo está construido cada elemento.
- **C.** Que solo lo leen los usuarios finales.
- **D.** Que se escribe al final del proyecto.

### 26. El cliente de un sistema de vigilancia portuaria dice: «Quiero el radar del modelo X». ¿Qué conviene hacer?

- **A.** Copiarlo tal cual como requisito del sistema.
- **B.** Ignorarlo, porque el cliente no decide.
- **C.** Recoger la necesidad que hay detrás (qué detectar, a qué distancia, en qué condiciones) y fijar el modelo solo si es una restricción justificada.
- **D.** Pedir al fabricante del radar que redacte los requisitos.

### 27. ¿Por qué la generación de requisitos es iterativa y requiere varias revisiones?

- **A.** Porque los requisitos de más bajo nivel dependen de decisiones de diseño que se van tomando.
- **B.** Porque los stakeholders cambian cada semana.
- **C.** Porque la norma prohíbe cerrar los requisitos.
- **D.** Porque los requisitos se escriben después de fabricar.

### 28. «El sistema deberá operar 24/7» es un requisito…

- **A.** De rendimiento.
- **B.** Operativo.
- **C.** De interfaz.
- **D.** Derivado.

### 29. «El sistema deberá impedir accesos no autorizados» es un requisito…

- **A.** Operativo.
- **B.** De mantenimiento.
- **C.** De seguridad.
- **D.** De interfaz.

### 30. Que un conjunto de requisitos sea «completo» significa que…

- **A.** Tiene más de cien requisitos.
- **B.** Cada requisito incluye la solución técnica.
- **C.** Ya no puede modificarse.
- **D.** Contiene perfiles de misión, conceptos de operación y mantenimiento, entornos de utilización y restricciones.

### 31. Que un requisito sea «realizable» significa que…

- **A.** Admite una solución técnicamente viable con un coste asumible.
- **B.** Ya se ha fabricado un prototipo.
- **C.** Lo ha aprobado la autoridad marítima.
- **D.** No tiene restricciones.

### 32. ¿Puede un requisito tener un valor cualitativo, como «agradable a la mayoría»?

- **A.** No, nunca.
- **B.** Solo si es un requisito de interfaz.
- **C.** Sí, siempre que se pueda verificar.
- **D.** Solo en requisitos derivados.

### 33. «El software será amigable y minimizará el consumo». ¿Cuál es el principal defecto?

- **A.** Es un requisito derivado.
- **B.** Usa términos no verificables.
- **C.** Describe una interfaz.
- **D.** Está sobreespecificado.

### 34. En el documento de necesidades del cliente aparece «El casco será de acero S355 de 12 mm de espesor». ¿Qué error frecuente comete?

- **A.** Usar palabras vagas.
- **B.** Escribir un requisito para un primer uso.
- **C.** Ser redundante con otro requisito.
- **D.** Escribir la implementación (cómo) en lugar del requisito (qué) y sobreespecificar.

### 35. El suministro eléctrico del puerto no lo controlamos, pero el sistema lo necesita. ¿Cómo debe tratarse?

- **A.** Como un elemento externo con el que hay que identificar y definir la interfaz.
- **B.** Como parte de lo que diseñamos.
- **C.** Como una MOE.
- **D.** No hay que considerarlo porque no lo controlamos.

### 36. En el ejemplo naval WMSM, ¿qué diferencia los requisitos de segundo nivel de los de alto nivel?

- **A.** Los de segundo nivel son más vagos.
- **B.** Los de segundo nivel solo tratan las comunicaciones.
- **C.** Los de segundo nivel concretan características con rangos, como eslora, calado o velocidades.
- **D.** Los de segundo nivel sustituyen a los de alto nivel.

### 37. «Lluvia, niebla, salinidad y oleaje» y «cumplimiento de la normativa marítima» son, respectivamente…

- **A.** Restricciones externas y entornos de utilización.
- **B.** Requisitos de rendimiento y criterios de validación.
- **C.** Requisitos funcionales y requisitos derivados.
- **D.** Entornos de utilización y restricciones externas.

### 38. ¿Cuál es una herramienta de gestión de requisitos?

- **A.** IBM DOORS Next.
- **B.** Modelica.
- **C.** OPCloud.
- **D.** Un diagrama IDEF0.

### 39. ¿Cuál **no** es una utilidad de la especificación de requisitos?

- **A.** Ser la base del acuerdo entre cliente y desarrollador.
- **B.** Servir de referencia para estimar coste y plazo.
- **C.** Sustituir al diseño de detalle.
- **D.** Facilitar los planes de verificación y validación.

### 40. En Blue Horizon, «tiempo de indisponibilidad del parque por incidentes» es una…

- **A.** TPM.
- **B.** MOP.
- **C.** Restricción externa.
- **D.** MOE.

### 41. En el mismo caso, «ancho de banda del enlace» es una…

- **A.** MOE.
- **B.** TPM.
- **C.** MOP.
- **D.** Necesidad del stakeholder.

### 42. En el mismo caso, «cobertura de vigilancia» es una…

- **A.** TPM.
- **B.** MOE.
- **C.** MOP.
- **D.** Restricción.

### 43. ¿Qué tres entregables pide el Trabajo de Grupo II de Blue Horizon?

- **A.** SVN, CONOPS y lista de stakeholders.
- **B.** Lista de requisitos de alto nivel, tabla MOE-MOP-TPM y diagrama de trazabilidad.
- **C.** QFD, FFBD e IDEF0.
- **D.** Arquitectura física, planos y presupuesto.

### Soluciones B2

<details>
<summary>Abrir solo después de responder</summary>

**18. C.** B2 p.3.

**19. A.** «Pasamos del lenguaje del cliente al lenguaje de la ingeniería». B2 p.6.

**20. D.** Poderes públicos: medio ambiente; miembros del equipo: seguridad y primas; dirección de empresa: compromisos internos. B2 p.12.

**21. B.** Ejemplo: el operador aporta experiencia → ingeniería mejora el diseño → mantenimiento reduce tiempos → aumenta la disponibilidad → el cliente obtiene más valor. B2 p.14.

**22. C.** B2 p.20.

**23. A.** Comprender la necesidad → describir el uso → formalizar los requisitos → definir cómo se validarán. B2 p.21.

**24. D.** Elementos clave: propósito y alcance, operaciones del sistema, interacciones del usuario y entorno operativo. B2 p.23.

**25. B.** B2 p.25.

**26. C.** Uno de los riesgos citados es «¿cómo impedimos que sean ellos quienes diseñen el sistema?», y hay que evitar soluciones de diseño prematuras. Caso nuevo; B2 pp.21, 31 y 41.

**27. A.** B2 p.31.

**28. B.** Responde a «¿en qué condiciones funciona?». B2 p.34.

**29. C.** Responde a «¿cómo evitamos daños?». B2 p.34.

**30. D.** B2 p.36.

**31. A.** B2 p.36.

**32. C.** B2 p.37.

**33. B.** «Amigable» y «minimizará» son los ejemplos de requisitos no verificables. B2 p.41.

**34. D.** Un requisito de necesidad debe expresar el qué y el porqué, no el cómo. Caso nuevo; B2 pp.36 y 41.

**35. A.** Lo que diseñamos, lo que necesitamos y no controlamos, y la interacción entre ambos: las interfaces. Caso nuevo; B2 p.42.

**36. C.** B2 pp.48–49.

**37. D.** B2 p.52.

**38. A.** También Jama Connect, Polarion, Codebeamer y Visure. Modelica es simulación y OPCloud es OPM. B2 p.54; B3 p.54.

**39. C.** Es base del acuerdo, reduce el esfuerzo de desarrollo, sirve para estimar coste y plazo y es referencia para la V&V. B2 p.35.

**40. D.** Responde a «¿la misión se está cumpliendo?». B2 p.45.

**41. B.** Parámetro técnico que influye en las MOP. B2 p.45.

**42. C.** Mide si el sistema funciona con el rendimiento esperado. B2 p.45.

**43. B.** B2 p.57.

</details>

---

## B3 · Definición y análisis de requisitos

### 44. «Negociar modificaciones» y «establecer y mantener la trazabilidad» son actividades de…

- **A.** Gestionar los requisitos del sistema.
- **B.** Preparar la definición.
- **C.** Definir los requisitos del sistema.
- **D.** Diseñar la arquitectura física.

### 45. En una SyRS aparece «La alarma se implementará con un PLC del modelo Z». ¿Qué condición incumple?

- **A.** Ser trazable.
- **B.** Ser no redundante.
- **C.** No estar sesgado por una implementación concreta.
- **D.** Estar en el nivel L1.

### 46. Un alcance de detección de 10 km puede lograrse con más potencia de radar y la antena baja, o con menos potencia y la antena más alta. ¿Qué concepto ilustra?

- **A.** Volatilidad de requisitos.
- **B.** Isoperformance.
- **C.** Tejado del QFD.
- **D.** MoSCoW.

### 47. ¿Qué impacto tiene una volatilidad de requisitos elevada?

- **A.** Reduce el coste del proyecto.
- **B.** Elimina la necesidad de trazabilidad.
- **C.** Simplifica la verificación y validación.
- **D.** Aumenta coste, plazo y retrabajo, complica la V&V y genera riesgo de inconsistencias.

### 48. ¿Cuál es una causa típica de volatilidad de requisitos?

- **A.** La maduración del CONOPS.
- **B.** El uso de la palabra *shall*.
- **C.** La existencia de una matriz de trazabilidad.
- **D.** La celebración de la SRR.

### 49. ¿Qué técnica agrupa necesidades o requisitos relacionados para organizarlos?

- **A.** Matriz ponderada.
- **B.** Diagrama de afinidad.
- **C.** Modelo Kano.
- **D.** Análisis de compensaciones.

### 50. ¿Qué técnica descompone requisitos de alto nivel y muestra relaciones padre-hijo?

- **A.** Modelo Kano.
- **B.** Diagrama de afinidad.
- **C.** Árbol de requisitos.
- **D.** Método de los 100 puntos.

### 51. ¿Según qué criterio clasifica los requisitos el modelo Kano?

- **A.** Su coste de implementación.
- **B.** Su orden temporal.
- **C.** El subsistema al que se asignan.
- **D.** Su influencia en la satisfacción del cliente.

### 52. ¿Cuál es el orden de dominios del diseño axiomático?

- **A.** Cliente → Funcional → Físico → Proceso.
- **B.** Físico → Funcional → Cliente → Proceso.
- **C.** Proceso → Físico → Funcional → Cliente.
- **D.** Funcional → Cliente → Proceso → Físico.

### 53. ¿Qué pide el axioma de información del diseño axiomático?

- **A.** Mantener independientes los requisitos funcionales.
- **B.** Documentar todas las decisiones.
- **C.** Minimizar la complejidad de la solución.
- **D.** Maximizar el número de parámetros de diseño.

### 54. ¿De qué metodología de calidad forma parte QFD?

- **A.** MBSE.
- **B.** TQM (Total Quality Management).
- **C.** SysML.
- **D.** TRIZ.

### 55. ¿Cuál es un beneficio de QFD citado en clase?

- **A.** Reduce el riesgo de diseñar funcionalidades que el cliente no necesita.
- **B.** Elimina la necesidad de entrevistar al cliente.
- **C.** Sustituye a la verificación.
- **D.** Fija automáticamente la arquitectura.

### 56. Importancias 5, 3 y 4; relaciones 3, 9 y 3. ¿Prioridad absoluta de la columna?

- **A.** 54
- **B.** 15
- **C.** 12
- **D.** 45

### 57. Tres columnas QFD valen 54, 90 y 36. ¿Cuál priorizas y con qué peso relativo?

- **A.** La de 54, con un 30 %.
- **B.** La de 90, con un 90 %.
- **C.** La de 90, con un 50 %.
- **D.** La de 36, con un 20 %.

### 58. Dos características técnicas muy prioritarias tienen una correlación negativa fuerte en el tejado. ¿Qué indica?

- **A.** Que una de ellas está mal calculada.
- **B.** Que hay que eliminar la de menor prioridad.
- **C.** Que la matriz central es incorrecta.
- **D.** Que existe un compromiso (*trade-off*) que hay que resolver, por ejemplo con análisis de compensaciones o TRIZ.

### 59. Según B3, la asignación de las funciones del sistema a sus componentes…

- **A.** No influye en el resultado.
- **B.** Determina la arquitectura del sistema.
- **C.** Es la última fase de fabricación.
- **D.** Sustituye al QFD.

### 60. ¿Cuál es una actividad del análisis funcional?

- **A.** Definir la detección de fallos y el comportamiento de recuperación.
- **B.** Elegir el proveedor de cada equipo.
- **C.** Negociar el precio con el cliente.
- **D.** Fabricar el prototipo.

### 61. ¿Cuándo queda definida la arquitectura funcional, según B3?

- **A.** En cuanto se dibuja el FFBD.
- **B.** Cuando se elige el material de cada componente.
- **C.** Al terminar la SRR.
- **D.** Cuando se completa con los requisitos de rendimiento y sus limitaciones.

### 62. ¿Qué puede incluir un FFBD?

- **A.** Solo secuencias lineales sin bifurcaciones.
- **B.** Componentes físicos y sus fabricantes.
- **C.** Ramificaciones, bucles y condiciones.
- **D.** Costes de cada función.

### 63. Quieres describir el procedimiento de una misión de salvamento, con decisiones y tareas en paralelo. ¿Qué herramienta usas?

- **A.** Diagrama de actividades.
- **B.** Matriz N².
- **C.** Árbol de requisitos.
- **D.** QFD.

### 64. Varios grupos describen el mismo sistema con diagramas distintos. ¿Qué conclusión saca B3?

- **A.** Solo una descripción puede ser correcta.
- **B.** Todas son correctas y ninguna completa; para mantenerlas coherentes hace falta un lenguaje de modelado.
- **C.** La más larga es la completa.
- **D.** Basta con elegir el FFBD.

### 65. ¿Qué lenguaje de modelado es la norma ISO 19450?

- **A.** SysML.
- **B.** UML.
- **C.** OPM.
- **D.** Modelica.

### 66. En modelado acausal, ¿qué ocurre con la ley de Ohm V = R·I?

- **A.** Hay que fijar que V es la entrada e I la salida.
- **B.** Solo puede usarse en circuitos de una resistencia.
- **C.** Hay que reescribirla para cada posición en el circuito.
- **D.** Se declara la relación y el simulador decide qué variable calcular según el contexto.

### Soluciones B3

<details>
<summary>Abrir solo después de responder</summary>

**44. A.** B3 p.4.

**45. C.** Cada requisito de la SyRS debe ser «no sesgado por una determinada implementación». Caso nuevo; B3 p.5.

**46. B.** Distintas combinaciones de TPM que dan el mismo MOP. Cifras de práctica; B3 p.13.

**47. D.** B3 p.14.

**48. A.** Otras causas: evolución de necesidades, cambios regulatorios, errores u omisiones iniciales y evolución tecnológica. B3 p.14.

**49. B.** Técnica de «organizar y clasificar». B3 p.15.

**50. C.** Técnica de «descomponer y relacionar». B3 p.15.

**51. D.** B3 p.15.

**52. A.** B3 p.16.

**53. C.** El axioma de independencia es el que pide mantener independientes los requisitos funcionales. B3 p.16.

**54. B.** B3 p.17.

**55. A.** B3 p.18.

**56. A.** 5×3 + 3×9 + 4×3 = 15 + 27 + 12 = 54. Ejercicio nuevo; método de B3 p.33.

**57. C.** Total = 54 + 90 + 36 = 180; 100 × 90/180 = 50 %. Las demás: 30 % y 20 %. Ejercicio nuevo; B3 p.33.

**58. D.** El tejado identifica qué descriptores se apoyan y cuáles entran en conflicto; TRIZ busca resolver contradicciones sin quedarse solo en el compromiso. B3 pp.15–16, 27 y 33.

**59. B.** B3 p.36.

**60. A.** También definir estados y modos, interfaces, asignar rendimiento y analizar modos de fallo y criticidad. B3 p.37.

**61. D.** B3 p.37.

**62. C.** B3 p.41.

**63. A.** Actividades, decisiones, paralelismos y bucles. B3 p.43.

**64. B.** B3 p.49.

**65. C.** B3 p.51.

**66. D.** B3 p.58.

</details>

---

## B4 · Arquitectura y diseño conceptual

### 67. «Resolver conflictos, validar y establecer la línea base» corresponde, al pasar de requisitos a arquitectura lógica, a…

- **A.** Modelar.
- **B.** Asignar y derivar.
- **C.** Validar y consolidar.
- **D.** Fabricar e integrar.

### 68. Al desarrollar la arquitectura, «registrar las decisiones y criterios, mantener la trazabilidad y gestionar cambios» es parte de…

- **A.** Preparar.
- **B.** Generar y evaluar.
- **C.** Diseño detallado.
- **D.** Gestionar.

### 69. Y «establecer los criterios para evaluar y seleccionar alternativas» es parte de…

- **A.** Preparar.
- **B.** Generar y evaluar.
- **C.** Gestionar.
- **D.** Retirada.

### 70. Según B4, la arquitectura…

- **A.** Aumenta la ambigüedad del problema.
- **B.** Reduce la ambigüedad del problema mientras hace explícita la complejidad de la solución.
- **C.** Elimina la complejidad de la solución.
- **D.** Es la forma final del sistema.

### 71. ¿Qué puede formar parte de la «forma» de un sistema?

- **A.** Solo piezas mecánicas.
- **B.** Solo hardware y software.
- **C.** Únicamente lo que se compra a proveedores.
- **D.** Personas, equipos, software e información.

### 72. En el dron de vigilancia, «transmitir información» y «enlace de comunicaciones» son, respectivamente…

- **A.** Función y forma.
- **B.** Forma y función.
- **C.** Concepto y arquitectura.
- **D.** Requisito y especificación.

### 73. «Plataforma flotante tripulada para el transporte de personas sobre el agua» describe, sin nombrarlo…

- **A.** Una grúa portuaria.
- **B.** Un surtidor de combustible.
- **C.** Una embarcación de pasaje.
- **D.** Un aerogenerador.

### 74. «Dron aéreo autónomo para inspección de aerogeneradores marinos» es un…

- **A.** Concepto desarrollado.
- **B.** Concepto inicial.
- **C.** Diseño detallado.
- **D.** Requisito de interfaz.

### 75. Una buena arquitectura gestiona la complejidad porque…

- **A.** Se queda con la primera solución que funciona.
- **B.** Evita cualquier interfaz.
- **C.** Identifica qué debe ser modular y relaciona adecuadamente forma y función.
- **D.** Concentra todas las funciones en un único elemento.

### 76. En el caso de RENFE, ¿por qué se decidió actuar sobre el vehículo?

- **A.** Porque rehacer la infraestructura era caro y lento, y optimizar la operación tenía un margen limitado.
- **B.** Porque la normativa prohibía cambiar la vía.
- **C.** Porque el tren era la opción más barata de cualquier proyecto.
- **D.** Porque los pasajeros pedían trenes nuevos.

### 77. En el caso del refrigerador, ¿qué papel tiene «ralentizar el deterioro»?

- **A.** Operando.
- **B.** Valor.
- **C.** Atributo.
- **D.** Transformación.

### 78. «Definir los parámetros principales y las restricciones» corresponde a…

- **A.** La arquitectura.
- **B.** El diseño detallado.
- **C.** La generación de conceptos.
- **D.** La SVN.

### 79. ¿Cuál es el orden propuesto en el resumen de B4?

- **A.** Diseño → arquitectura → conceptos → necesidad.
- **B.** Generar conceptos → entender la necesidad → diseño → arquitectura.
- **C.** Entender la necesidad → generar conceptos → seleccionar → definir arquitectura → diseño.
- **D.** Seleccionar → generar → diseño → arquitectura.

### 80. En un buque autónomo, «organizar sensores, navegación, comunicaciones, energía y control remoto, asignarles funciones y definir sus interfaces» es…

- **A.** El concepto inicial.
- **B.** El CONOPS.
- **C.** El diseño detallado.
- **D.** La arquitectura.

### Soluciones B4

<details>
<summary>Abrir solo después de responder</summary>

**67. C.** Modelar → asignar y derivar → validar y consolidar. B4 p.8.

**68. D.** B4 p.11.

**69. A.** Preparar incluye revisar necesidades y restricciones, definir alcance y vistas, seleccionar métodos y fijar criterios de evaluación. B4 p.11.

**70. B.** B4 p.13. La arquitectura es la organización fundamental, no la forma final, B4 p.14.

**71. D.** B4 p.16.

**72. A.** B4 p.17.

**73. C.** Ejercicio de describir un concepto sin nombrarlo. B4 p.22.

**74. B.** Expresa la idea principal; el concepto desarrollado añade tecnologías y características. B4 p.20.

**75. C.** B4 p.23.

**76. A.** B4 p.24.

**77. D.** Operando: comida; atributo: estado de conservación; valor: conservar más tiempo. B4 p.27.

**78. A.** El diseño concreta dimensiones, componentes, materiales y valores detallados y optimiza. B4 p.30.

**79. C.** B4 p.31.

**80. D.** Identificar elementos, asignar funciones y definir interfaces. Caso nuevo; B4 p.19.

</details>

---

## Qué hacer con los resultados

- Anota los números fallados y localiza el bloque; vuelve a esa sección de [RESUMEN.md](RESUMEN.md).
- En las de cálculo (6, 56 y 57), escribe la operación completa antes de mirar la solución.
- Las preguntas de «cuál **no**» castigan la lectura rápida: subraya la negación antes de responder.
- La puntuación es solo diagnóstica: no predice la nota del examen.
