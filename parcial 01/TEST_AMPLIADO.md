# Test ampliado · 66 preguntas nuevas

Banco de preguntas complementario a [PRACTICA.md](PRACTICA.md). **No repite** sus 20 preguntas de test: cubre conceptos de los cuatro bloques que allí no se preguntaban o se preguntan desde otro ángulo.

Preguntas originales elaboradas a partir de las presentaciones. **No son preguntas de exámenes anteriores.** Una sola respuesta correcta por pregunta. Las soluciones están al final de cada bloque, plegadas, con la referencia «B*n* p.*x*» al PDF original (portada = página 1).

**Cómo usarlo**

- Hazlo por bloques: unos 10–12 minutos por cada 15 preguntas, sin apuntes.
- Corrige al terminar cada bloque y apunta el número de las que fallas o aciertas por intuición.
- Vuelve al resumen o a la página citada solo para las falladas; repítelas al día siguiente.

| Bloque | Preguntas | Temas |
|---|---|---|
| B1 · Introducción y conceptos | 1–14 | Sistema, normas, complejidad, iceberg, ciclo de vida, decision gates |
| B2 · Stakeholders y requisitos | 15–33 | Stakeholders, NGO, SVN, ConOps/OpsCon, redacción y clasificación de requisitos, documentos |
| B3 · Definición y análisis de requisitos | 34–55 | SyRS, SRR, isoperformance, priorización, QFD, análisis funcional, lenguajes de modelado |
| B4 · Arquitectura y diseño conceptual | 56–66 | Arquitectura lógica, función/forma, concepto, valor, generación y selección |

---

## B1 · Introducción y conceptos

### 1. ¿Qué distingue un sistema de un simple montón de objetos?

- **A.** Que todos sus elementos son del mismo material.
- **B.** Que tiene más de siete elementos.
- **C.** Que si se elimina una parte, el resultado o la funcionalidad del conjunto se ve afectado.
- **D.** Que siempre es un sistema físico y cerrado.

### 2. ¿Qué norma define los procesos del ciclo de vida del sistema y se considera el estándar central de la disciplina?

- **A.** ISO/IEC/IEEE 15288.
- **B.** ISO/IEC/IEEE 29148.
- **C.** ISO/IEC/IEEE 42010.
- **D.** ISO/IEC/IEEE 15289.

### 3. ¿Qué norma introduce los conceptos de *stakeholders, concerns, viewpoints* y *views* para describir arquitecturas?

- **A.** ISO/IEC/IEEE 15288.
- **B.** ISO/IEC/IEEE 15289.
- **C.** ISO/IEC/IEEE 29148.
- **D.** ISO/IEC/IEEE 42010.

### 4. Según la ley de Miller, ¿para qué se descompone jerárquicamente un sistema?

- **A.** Para que cada nivel tenga exactamente siete subsistemas.
- **B.** Para que en cada nivel haya un número de elementos que una persona pueda comprender y gestionar.
- **C.** Para eliminar las interfaces entre subsistemas.
- **D.** Para reducir el número total de piezas del sistema.

### 5. Con la regla #niveles = log₇(#piezas), ¿cuántos niveles corresponden a un sistema de 2.401 piezas?

- **A.** 3
- **B.** 343
- **C.** 4
- **D.** 7

### 6. ¿Qué consecuencia tiene descomponer cada vez más un sistema?

- **A.** Es más sencillo diseñar, asignar responsabilidades y verificar, pero aumentan interfaces y dependencias.
- **B.** La complejidad desaparece.
- **C.** Disminuye el número de interfaces.
- **D.** Deja de ser necesaria la integración.

### 7. En el caso «la integración que siempre falla», ¿a qué nivel del iceberg corresponde «aparecen incidencias que ya habían surgido en proyectos anteriores»?

- **A.** Modelos mentales.
- **B.** Estructuras.
- **C.** Evento aislado.
- **D.** Patrones.

### 8. ¿Qué nivel del iceberg responde a la pregunta «¿qué creencias hay detrás?»?

- **A.** Eventos.
- **B.** Modelos mentales.
- **C.** Patrones.
- **D.** Estructuras.

### 9. Una sonda se pierde porque un subsistema trabaja en unidades imperiales y otro espera unidades métricas. ¿Qué fallo de ingeniería de sistemas ilustra?

- **A.** Falta de financiación del programa.
- **B.** Un requisito de rendimiento demasiado ambicioso.
- **C.** Mala gestión de interfaces y falta de validación extremo a extremo.
- **D.** Exceso de pruebas de integración.

### 10. ¿Qué afirmación sobre el valor de invertir en ingeniería de sistemas es correcta?

- **A.** Aumenta la probabilidad de controlar los costes, pero no garantiza por sí sola cumplir el presupuesto.
- **B.** Garantiza que el proyecto termine dentro del presupuesto.
- **C.** Es un coste administrativo sin efecto sobre retrabajo ni plazos.
- **D.** Solo aporta valor en proyectos de software.

### 11. En una decision gate, ¿qué resultado implica permanecer en la etapa actual y repetir la revisión cuando se completen las acciones?

- **A.** GO WITH ACTIONS.
- **B.** RECYCLE.
- **C.** KILL.
- **D.** HOLD.

### 12. ¿Qué significa el resultado RECYCLE en una decision gate?

- **A.** Terminar el proyecto.
- **B.** Volver a una etapa anterior.
- **C.** Continuar y responder a los ítems de actuación.
- **D.** Detener la actividad del proyecto.

### 13. ¿Qué tres aspectos forman el «triángulo de hierro» que hay que optimizar durante el ciclo de vida?

- **A.** Coste, funcionalidad y plazo.
- **B.** Riesgo, calidad y ROI.
- **C.** MOE, MOP y TPM.
- **D.** Cliente, operador y mantenedor.

### 14. ¿Cuál **no** figura entre las características de un sistema vistas en clase?

- **A.** Jerarquía.
- **B.** Interacción.
- **C.** Agrupación aleatoria de elementos.
- **D.** Propósito definido.

### Soluciones B1

<details>
<summary>Abrir solo después de responder</summary>

**1. C.** En un montón, quitar una parte solo deja menos elementos; en un sistema afecta al resultado. B1 p.5.

**2. A.** 15288 define los procesos del ciclo de vida; 29148 es requisitos; 42010, descripción de arquitectura; 15289, documentación. B1 pp.7–8.

**3. D.** ISO/IEC/IEEE 42010, *Architecture Description*. B1 p.8.

**4. B.** Manejamos unos 7 ± 2 elementos a la vez; el objetivo no es trocear «porque sí», sino que cada nivel sea abarcable. B1 p.21.

**5. C.** 7⁴ = 2.401, luego log₇(2.401) = 4. Ejercicio nuevo; método de B1 p.23.

**6. A.** La complejidad no desaparece, se gestiona: descomponer facilita el trabajo por partes, pero crea interfaces, dependencias y problemas de integración. B1 p.22.

**7. D.** Es algo que se repite: un patrón. B1 pp.16–17.

**8. B.** Eventos (qué vemos) → patrones (qué se repite) → estructuras (qué los genera) → modelos mentales (qué creencias hay detrás). B1 pp.15 y 17.

**9. C.** El caso de la sonda a Marte: mala gestión de interfaces, verificación insuficiente entre subsistemas y falta de validación extremo a extremo. B1 p.36.

**10. A.** B1 pp.38–39: es una inversión para reducir incertidumbre, retrabajo, retrasos y sobrecostes, pero no una garantía.

**11. D.** HOLD: no aceptable, retrabajo y nueva revisión. B1 p.50.

**12. B.** RECYCLE: vuelta a una etapa anterior. KILL termina; SUSPEND detiene; GO WITH ACTIONS continúa con acciones. B1 p.50.

**13. A.** B1 p.47.

**14. C.** Las características son composición, jerarquía, interacción, dinamismo, heterogeneidad y propósito definido. Un conjunto aleatorio no es un sistema. B1 pp.5 y 9.

</details>

---

## B2 · Stakeholders y requisitos

### 15. Según Kochan y Rubinstein, ¿cómo se clasifican habitualmente los medios de comunicación o la ciudadanía local?

- **A.** Stakeholders directos.
- **B.** Stakeholders definitivos.
- **C.** Proveedores críticos.
- **D.** Stakeholders indirectos o latentes.

### 16. ¿Cuál **no** es uno de los tres criterios para considerar a un actor stakeholder directo?

- **A.** Estar presente físicamente en las instalaciones del proyecto.
- **B.** Tener activos críticos para el éxito de la misión.
- **C.** Invertir esos activos en la misión.
- **D.** Tener capacidad para influir en el resultado.

### 17. Dentro de las NGO, ¿qué elemento detalla las metas y proporciona un medio para documentarlas y alcanzarlas?

- **A.** Needs.
- **B.** Goals.
- **C.** Objectives.
- **D.** Constraints.

### 18. «El regulador introduce una exigencia → el astillero modifica el diseño → el proveedor cambia un equipo → mantenimiento necesita formación». ¿Qué ilustra?

- **A.** Un bucle de valor.
- **B.** Un efecto de segundo orden.
- **C.** Un modelo en V.
- **D.** Un concepto de operación.

### 19. ¿Cuál es la principal lección del caso BP analizado con SVN?

- **A.** Los medios y la opinión pública eran mucho más influyentes de lo estimado inicialmente.
- **B.** Los proveedores no influyen en el éxito de grandes proyectos.
- **C.** Basta con analizar la organización focal.
- **D.** El SVN sustituye al CONOPS.

### 20. «Vigilar el parque y detectar intrusiones» frente a «el sistema detectará embarcaciones que se aproximen al parque y alertará al operador» son, respectivamente…

- **A.** OpsCon y ConOps.
- **B.** MOE y MOP.
- **C.** ConOps y OpsCon.
- **D.** Requisito y especificación.

### 21. ¿Qué describe mejor la *Requirements Baseline*?

- **A.** El diseño detallado del sistema.
- **B.** Una lista abierta de deseos sin control de cambios.
- **C.** Únicamente los requisitos funcionales.
- **D.** Un conjunto de requisitos acordados, trazables, verificables y controlados, que todavía no es el diseño.

### 22. ¿Cuál de estos requisitos contiene un error de redacción típico?

- **A.** El sistema deberá enviar la alerta al centro de control en menos de 10 s en las condiciones definidas.
- **B.** El sistema detectará embarcaciones, boyas, etc.
- **C.** El sensor radar deberá poder sustituirse en menos de 30 minutos.
- **D.** El sistema deberá operar 24/7.

### 23. «Cumplir IMO 2008» como valor de un requisito es un valor…

- **A.** Discreto o lógico.
- **B.** Continuo.
- **C.** Probabilístico.
- **D.** Marginal.

### 24. «Reducir un 15 % el consumo respecto al buque actual» sigue una fórmula de métrica…

- **A.** Absoluta.
- **B.** Probabilística.
- **C.** Marginal.
- **D.** Cualitativa.

### 25. ¿Qué diferencia hay entre requisitos *shall* y *should*?

- **A.** Son sinónimos en una especificación.
- **B.** *Shall* delimita restricciones; *should* fija metas una vez cumplidos los *shall*.
- **C.** *Should* es obligatorio y *shall* opcional.
- **D.** *Shall* solo se usa para requisitos de software.

### 26. Los camarotes importan al cliente; las camas las decide el ingeniero. Las camas pertenecen al…

- **A.** Espacio objetivo.
- **B.** Diagrama SVN.
- **C.** CONOPS.
- **D.** Espacio de diseño.

### 27. ¿Cuál es un **capacitador**, y no un control, en la definición de requisitos?

- **A.** La legislación aplicable.
- **B.** Las normas de la industria.
- **C.** La estructura y los equipos de trabajo de la empresa.
- **D.** Los acuerdos contractuales.

### 28. ¿Qué documento recoge interfaces físicas, eléctricas, de datos y de comunicación?

- **A.** IRD.
- **B.** SRS.
- **C.** PRD.
- **D.** SRD.

### 29. ¿Qué relación hay entre requisitos y especificación?

- **A.** Son exactamente lo mismo.
- **B.** Los requisitos son la entrada al diseño; la especificación es el resultado y puede incluir planos o planes.
- **C.** La especificación es la entrada y los requisitos el resultado.
- **D.** La especificación solo contiene requisitos de interfaz.

### 30. En la tabla de clasificación del parque eólico, ¿qué tipo es «el sistema deberá enviar alertas al centro de control»?

- **A.** Rendimiento.
- **B.** Mantenimiento.
- **C.** Operativo.
- **D.** Interfaz.

### 31. Se decide añadir un dron y aparece la necesidad de una estación de carga. Ese nuevo requisito es…

- **A.** Derivado.
- **B.** De stakeholder.
- **C.** De rendimiento.
- **D.** De interfaz externa impuesta por el regulador.

### 32. En la clase Liberty, ¿qué requisito traduce la expectativa «construir muchos»?

- **A.** 9.000 t de peso muerto.
- **B.** 1.000 millas de autonomía.
- **C.** Diseño único, el mismo para todos los astilleros.
- **D.** Dos calderas y una máquina de vapor compuesta.

### 33. ¿Qué salida responde a «¿cómo demostramos que ningún requisito se ha olvidado?»?

- **A.** El diagrama SVN.
- **B.** La matriz de trazabilidad.
- **C.** El CONOPS.
- **D.** El tejado de la matriz QFD.

### Soluciones B2

<details>
<summary>Abrir solo después de responder</summary>

**15. D.** No cumplen los tres criterios; pueden verse afectados o tener interés, pero su implicación es menor. B2 p.11.

**16. A.** Los criterios son: tener activos críticos, invertirlos en la misión y tener capacidad de influir. B2 p.11.

**17. C.** Needs: lo que se quiere resolver; Goals: lo que hay que conseguir; Objectives: detallan las metas. B2 p.13.

**18. B.** Consecuencia que llega al proyecto a través de otro stakeholder. Un bucle de valor es una relación circular de intercambio continuo. B2 p.14.

**19. A.** Un SVN completo debería haberlo revelado antes. B2 p.19.

**20. C.** ConOps: intención de uso, sistema como caja negra. OpsCon: qué hará el sistema, no cómo, y por qué. B2 p.44.

**21. D.** «Establece la base para diseñar el sistema, pero todavía no es el diseño». B2 p.21.

**22. B.** Hay que evitar «etc.», «y/o» y «pero no limitado a». Las demás son ejemplos de los apuntes o están bien encaminadas. B2 pp.34 y 41.

**23. A.** Valores continuos (20 nudos), discretos/lógicos (cumplir IMO 2008) o cualitativos verificables. B2 p.37.

**24. C.** Marginal: «mejorar en xx %». Absoluto: valor mínimo o máximo; probabilístico: valor con un % de probabilidad. Cifra inventada para practicar. B2 p.38.

**25. B.** B2 p.43; véase también p.41 («usar *shall*»).

**26. D.** Espacio objetivo: lo que importa al cliente (camarotes). Espacio de diseño: lo que decidimos como ingenieros (camas). B2 p.43.

**27. C.** Controles: qué estoy obligado a cumplir (reglas, normas, restricciones). Capacitadores: qué me ayuda a hacerlo (personas, herramientas, recursos). B2 p.50.

**28. A.** IRD, Interface Requirements Document. SRS es software; PRD, proyecto; SRD, sistema completo. B2 p.55.

**29. B.** B2 p.54.

**30. D.** Responde a «¿con quién se conecta?». B2 p.34.

**31. A.** Surge de una decisión de diseño. Es el ejemplo de B2 p.34.

**32. C.** Las demás traducen capacidad de carga, llegar a Europa y combustible abundante. B2 p.40.

**33. B.** Vincula requisitos con pruebas, elementos de diseño y entregables. B2 pp.51 y 53.

</details>

---

## B3 · Definición y análisis de requisitos

### 34. Si L0 es el requisito de misión o CONOPS de usuario, ¿qué niveles debería dejar definidos claramente la SyRS?

- **A.** Solo L0.
- **B.** L3 y L4, componentes y piezas.
- **C.** L1, sistemas principales, y L2, subsistemas principales.
- **D.** Todos los niveles hasta la última pieza.

### 35. ¿Cuándo suele celebrarse la System Requirements Review (SRR)?

- **A.** Tras la integración del sistema.
- **B.** Después de las pruebas de aceptación.
- **C.** Durante la operación.
- **D.** Pronto: en la Fase A, de concepto y tecnología, antes de la Fase B, de diseño preliminar.

### 36. ¿Qué ocurre con los requisitos tras la SRR?

- **A.** Quedan congelados y no pueden cambiar nunca.
- **B.** Pasan a gestión de configuración; añadir, eliminar o modificar requiere aprobación de la dirección del proyecto.
- **C.** Cada ingeniero puede modificarlos libremente.
- **D.** Se sustituyen por la especificación de diseño.

### 37. ¿Qué es la isoperformance?

- **A.** El conjunto de combinaciones de parámetros de diseño que alcanzan un mismo nivel de rendimiento.
- **B.** Un requisito de rendimiento idéntico para todos los subsistemas.
- **C.** Una técnica para eliminar los compromisos entre prestaciones.
- **D.** Una medida de efectividad de la misión.

### 38. ¿Cuál es el objetivo respecto a la volatilidad de requisitos?

- **A.** Eliminarla por completo.
- **B.** Ignorarla hasta la integración.
- **C.** Gestionarla mediante control de cambios y trazabilidad.
- **D.** Prohibir las adiciones de requisitos tras la SRR.

### 39. MoSCoW, el modelo Kano y el método de los 100 puntos son técnicas para…

- **A.** Descomponer requisitos en árbol.
- **B.** Priorizar requisitos.
- **C.** Relacionar necesidades con parámetros técnicos.
- **D.** Documentar interfaces.

### 40. En diseño axiomático, ¿qué establece el axioma de independencia?

- **A.** Minimizar la complejidad de la solución.
- **B.** Traducir la voz del cliente a características técnicas.
- **C.** Resolver contradicciones mediante principios inventivos.
- **D.** Mantener independientes los requisitos funcionales.

### 41. ¿Qué describe mejor TRIZ?

- **A.** Contradicción → principios inventivos → solución, sin recurrir solo a compromisos.
- **B.** Matriz que relaciona qués y cómos.
- **C.** Técnica de priorización Must/Should/Could/Won't.
- **D.** Lenguaje de modelado basado en ecuaciones.

### 42. En QFD, ¿cuál es un descriptor técnico (un «cómo») y no un requisito del cliente?

- **A.** Alta disponibilidad del sistema.
- **B.** Fácil mantenimiento.
- **C.** MTBF ≥ 5.000 h.
- **D.** Bajo coste de operación.

### 43. ¿Cómo se refina un QFD cuando los descriptores aún no permiten actuar?

- **A.** Se elimina el tejado.
- **B.** Se crean nuevas matrices en las que los «cómos» pasan a ser los «qués».
- **C.** Se suman todas las importancias del cliente.
- **D.** Se sustituyen las relaciones 9/3/1 por porcentajes.

### 44. ¿Para qué sirve la evaluación competitiva en la House of Quality?

- **A.** Para calcular la prioridad absoluta de cada columna.
- **B.** Para identificar conflictos entre características técnicas.
- **C.** Para listar los stakeholders del producto.
- **D.** Para situar el producto frente a los competidores en cada requisito del cliente.

### 45. Importancias 4, 3, 5 y 2; relaciones 3, 9, 1 y 0. ¿Prioridad absoluta de la columna?

- **A.** 18
- **B.** 44
- **C.** 13
- **D.** 52

### 46. Tres columnas QFD valen 98, 60 y 42. ¿Prioridad relativa de la de 98?

- **A.** 49 %
- **B.** 98 %
- **C.** 33,3 %
- **D.** 32,7 %

### 47. ¿Cuál está correctamente planteado como resultado del análisis funcional?

- **A.** El sistema dispondrá de una cámara 8K sobre una torreta giroestabilizada.
- **B.** El dron usará un procesador concreto con IA embarcada.
- **C.** El sistema deberá proporcionar imágenes con resolución suficiente para identificar embarcaciones a 5 km.
- **D.** La antena será de un fabricante determinado.

### 48. ¿Qué grupo de herramientas incluye FFBD, IDEF0 e IPO?

- **A.** Análisis de interfaces.
- **B.** Validación mediante simulación.
- **C.** Análisis del comportamiento.
- **D.** Definición de funciones.

### 49. En el IDEF0 «Detectar objetivo» del dron, ¿qué son «imágenes EO/IR, posición GPS y datos AIS»?

- **A.** Controles.
- **B.** Entradas.
- **C.** Mecanismos.
- **D.** Salidas.

### 50. Quieres representar «preparado, en vuelo, vigilando, retornando» y qué provoca cada cambio. ¿Qué herramienta usas?

- **A.** Diagrama de estados.
- **B.** Matriz de interfaces.
- **C.** QFD.
- **D.** FFBD.

### 51. Para analizar el protocolo de mensajes petición-respuesta entre el dron y la estación de control, en orden temporal, usarías…

- **A.** Un FFBD.
- **B.** Un QFD.
- **C.** Un diagrama de secuencia.
- **D.** Un árbol de requisitos.

### 52. ¿Qué afirmación sobre N² y matriz de interfaces es correcta?

- **A.** Son la misma herramienta con distinto nombre.
- **B.** La N² solo sirve para componentes físicos.
- **C.** La matriz de interfaces sustituye al análisis funcional.
- **D.** La N² identifica interfaces; la matriz las documenta con identificador, origen, destino e información.

### 53. En un lenguaje de modelado, ¿qué es el conjunto de reglas que gobierna cómo construir «frases» correctas?

- **A.** Ontología.
- **B.** Sintaxis.
- **C.** Semántica.
- **D.** Taxonomía.

### 54. En OPM, «Despegar» es…

- **A.** Un objeto.
- **B.** Un estado.
- **C.** Un proceso.
- **D.** Una forma.

### 55. ¿Qué afirmación sobre SysML y Modelica es correcta?

- **A.** SysML ayuda a describir el sistema (requisitos, arquitectura, interfaces); Modelica, a simular su comportamiento físico.
- **B.** Ambos son herramientas comerciales de gestión de requisitos.
- **C.** Modelica es una extensión de UML para requisitos.
- **D.** SysML obliga a resolver ecuaciones diferenciales.

### Soluciones B3

<details>
<summary>Abrir solo después de responder</summary>

**34. C.** B3 p.5.

**35. D.** B3 p.12.

**36. B.** Gestión de configuración formal, es decir, control de versiones. No quedan congelados: los cambios se aprueban. B3 p.12.

**37. A.** Actúa principalmente a nivel de TPM y ayuda a evitar soluciones prematuras y sobreespecificaciones. B3 p.13.

**38. C.** Una cierta volatilidad es normal e incluso necesaria. B3 p.14.

**39. B.** Bloque 3 de técnicas de análisis: priorizar. Árbol y matrices sirven para descomponer y relacionar. B3 p.15.

**40. D.** El axioma de información es el que pide minimizar la complejidad. B3 p.16.

**41. A.** Asociado a Genrich Altshuller. B3 p.16.

**42. C.** Las otras son voz del cliente («qués»). B3 p.19.

**43. B.** B3 p.29.

**44. D.** B3 p.28. Los conflictos entre características técnicas van al tejado.

**45. B.** 4×3 + 3×9 + 5×1 + 2×0 = 12 + 27 + 5 + 0 = 44. Ejercicio nuevo; método de B3 p.33.

**46. A.** Total = 98 + 60 + 42 = 200; 100 × 98/200 = 49 %. No se divide entre el número de columnas. B3 p.33.

**47. C.** Expresa qué debe hacerse y con qué prestación; las otras ya son diseño. B3 p.36.

**48. D.** Cuatro bloques: definición de funciones, análisis del comportamiento, análisis de interfaces y validación mediante modelos. B3 p.40.

**49. B.** Son lo que la función procesa. Los mecanismos son cámara, procesador y software; los controles, normativa y reglas de misión. B3 p.42.

**50. A.** Modos de operación, estados de fallo y transiciones. B3 p.44.

**51. C.** Mensajes, peticiones, respuestas y orden temporal. B3 p.44.

**52. D.** «La N² identifica interfaces. La matriz las documenta». B3 p.46.

**53. B.** Ontología: qué entidades pueden existir; semántica: su significado; sintaxis: reglas de construcción. B3 p.50.

**54. C.** Un proceso transforma objetos o modifica sus estados y se asocia a un verbo. B3 p.52.

**55. A.** «SysML nos ayuda a describir el sistema. Modelica nos ayuda a comprender su comportamiento físico». B3 pp.55 y 58.

</details>

---

## B4 · Arquitectura y diseño conceptual

### 56. ¿Qué produce la descomposición lógica?

- **A.** La lista de materiales del sistema.
- **B.** Una arquitectura lógica que describe cómo debe funcionar el sistema: funciones, flujos, comportamientos, estados y modos.
- **C.** El plan de fabricación.
- **D.** El presupuesto definitivo.

### 57. ¿Qué afirmación sobre la arquitectura es correcta según los apuntes?

- **A.** Es el dibujo de bloques principal del sistema.
- **B.** Es la elección del fabricante de cada componente.
- **C.** Es un conjunto coherente de modelos, relaciones, decisiones y requisitos derivados.
- **D.** Es el documento de requisitos del cliente.

### 58. Ante un mismo conjunto de necesidades y requisitos…

- **A.** Pueden existir varias arquitecturas válidas que hay que comparar y seleccionar.
- **B.** Solo existe una arquitectura válida.
- **C.** La arquitectura queda determinada por el CONOPS.
- **D.** La arquitectura más barata es siempre la correcta.

### 59. ¿Por qué es importante tomar bien las decisiones de arquitectura?

- **A.** Porque se toman al final y apenas afectan al ciclo de vida.
- **B.** Porque sustituyen a la verificación.
- **C.** Porque eliminan la necesidad de interfaces.
- **D.** Porque se toman pronto, condicionan gran parte del ciclo de vida y es más barato cambiar un bloque en el modelo que en la integración.

### 60. ¿Qué es la ingeniería inversa?

- **A.** Partir de la función para definir la forma.
- **B.** Verificar el sistema empezando por los componentes.
- **C.** Partir de una solución existente, identificar sus elementos y deducir sus funciones.
- **D.** Redactar los requisitos después de construir el sistema.

### 61. ¿Qué estructura propone B4 para expresar un concepto de solución?

- **A.** Función + forma + coste.
- **B.** Tipo de solución + característica diferenciadora + finalidad.
- **C.** Necesidad + meta + objetivo.
- **D.** Entrada + control + mecanismo + salida.

### 62. «Dron eléctrico de despegue vertical, con cámara visual y térmica, navegación autónoma y enlace de datos con una estación de control» es…

- **A.** Un concepto desarrollado.
- **B.** Un concepto inicial.
- **C.** Un diseño detallado de fabricación.
- **D.** Una necesidad del stakeholder.

### 63. En el caso del refrigerador, «comida» es el…

- **A.** Atributo.
- **B.** Valor.
- **C.** Transformación.
- **D.** Operando.

### 64. ¿Qué afirmación sobre el valor en ingeniería de sistemas es correcta?

- **A.** La mejor arquitectura es la de menor coste de adquisición.
- **B.** Hay que maximizar prestaciones sin considerar el coste.
- **C.** Una buena arquitectura maximiza el beneficio con un coste asumible, incluyendo operación y mantenimiento.
- **D.** El valor depende solo de la funcionalidad proporcionada.

### 65. En el ejemplo de RENFE, ¿qué es «un tren basculante/pendular»?

- **A.** La necesidad.
- **B.** El concepto de solución.
- **C.** El sistema físico resultante.
- **D.** La arquitectura lógica.

### 66. Brainstorming, mapas mentales y matriz morfológica se usan sobre todo para…

- **A.** Generar conceptos de solución con pensamiento divergente.
- **B.** Seleccionar el concepto final con pensamiento convergente.
- **C.** Verificar requisitos.
- **D.** Calcular prioridades QFD.

### Soluciones B4

<details>
<summary>Abrir solo después de responder</summary>

**56. B.** «Comprender cómo debe funcionar el sistema antes de decidir cómo implementarlo». B4 pp.7 y 10.

**57. C.** «La arquitectura no es un dibujo». B4 p.8.

**58. A.** Se evalúan según prestaciones, coste, riesgo, plazo y capacidad de evolución. B4 p.14.

**59. D.** B4 p.12.

**60. C.** El diseño directo parte de la función para definir la forma. En ingeniería naval se combinan ambos caminos. B4 p.18.

**61. B.** Ejemplo: dron aéreo autónomo + con sensores visuales y térmicos + para inspeccionar aerogeneradores marinos. B4 p.21.

**62. A.** Especifica características principales y tecnologías; el concepto inicial solo expresa la idea principal. B4 p.20.

**63. D.** Operando: comida; atributo: estado de conservación; transformación: ralentizar el deterioro; valor: conservar más tiempo. B4 p.27.

**64. C.** El coste incluye desarrollo y adquisición, operación y mantenimiento, recursos y tiempo. B4 p.26.

**65. C.** Necesidad: reducir el tiempo de viaje; concepto: inclinar la caja; arquitectura: funciones, componentes e interfaces para detectar, controlar y producir la inclinación. B4 p.25.

**66. A.** Primero se amplía el espacio de soluciones; después se reduce con criterios. B4 pp.29 y 31.

</details>

---

## Qué hacer con los resultados

- Anota los números fallados y localiza el bloque. Si fallas varias de un bloque, vuelve primero a esa sección de [RESUMEN.md](RESUMEN.md).
- En las de cálculo (5, 45 y 46), escribe la operación completa antes de mirar la solución.
- Las preguntas de «cuál **no**» castigan la lectura rápida: subraya la negación antes de responder.
- La puntuación es solo diagnóstica: no predice la nota del examen.
