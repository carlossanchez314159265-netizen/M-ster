# Preguntas de desarrollo · definición de conceptos

24 preguntas largas para practicar el tipo «define y explica». Complementan los 8 desarrollos de [PRACTICA.md](PRACTICA.md) sin repetirlos: allí se trabajan casos y cálculos; aquí, sobre todo, **definir bien cada concepto, explicarlo y ponerle un ejemplo**.

Preguntas originales elaboradas a partir de las presentaciones. **No son preguntas de exámenes anteriores.** Las respuestas modelo sirven para aprender la estructura, no para memorizarlas palabra por palabra.

**Cómo usarlo**

1. Lee el enunciado y escribe tu respuesta en 8–12 líneas, sin apuntes. Unos 8 minutos por pregunta.
2. Sigue siempre el esquema **definición → explicación → ejemplo**, y añade una **diferencia con el concepto con el que se confunde**.
3. Abre la respuesta modelo y corrígete con la lista «Debe aparecer»: cuenta cuántos puntos tienes.
4. Repite al día siguiente las preguntas en las que te falten dos puntos o más.

| Bloque | Preguntas |
|---|---|
| B1 · Introducción y conceptos | 1–6 |
| B2 · Stakeholders y requisitos | 7–14 |
| B3 · Definición y análisis de requisitos | 15–19 |
| B4 · Arquitectura y diseño conceptual | 20–24 |

---

## B1 · Introducción y conceptos

### 1. Sistema

Define qué es un sistema. Explica qué lo diferencia de un conjunto de objetos y enumera sus características. Pon un ejemplo naval.

<details>
<summary>Respuesta modelo</summary>

Un **sistema** es un conjunto de elementos relacionados entre sí que, actuando juntos de forma organizada, producen un resultado o una funcionalidad que no proporcionan por separado. INCOSE lo define como una colección de elementos diferentes que juntos producen resultados que no se pueden obtener por separado; la NASA, como componentes que interactúan de forma organizada hacia un propósito establecido.

Lo que lo diferencia de un montón o colección de objetos es la **relación y el propósito**: si se quita una parte de un sistema, el resultado o la funcionalidad se ve afectado; si se quita una parte de un montón, solo queda un montón más pequeño. Por eso «un sistema no es una colección de partes: es una red de relaciones».

Sus características son: **composición, jerarquía, interacción, dinamismo, heterogeneidad y propósito definido**. Además, definir un sistema es una interpretación que depende de los intereses del observador, es decir, de dónde ponemos sus límites. Puede clasificarse por su naturaleza (social, natural, técnico), por sus condiciones de contorno (abierto o cerrado) o por su realidad (físico o abstracto).

**Ejemplo:** un buque es un sistema: casco, propulsión, generación eléctrica, navegación y tripulación interactúan para transportar carga de forma segura. Ninguno de esos elementos, por separado, transporta la carga. Si falla la generación eléctrica, se ve afectada la navegación y, con ella, la misión.

**Debe aparecer**
- Elementos relacionados que producen un resultado que no dan por separado.
- La diferencia con un montón: al quitar una parte se pierde funcionalidad.
- Al menos cuatro de las seis características.
- Un ejemplo con elementos e interacciones concretos.

**Error típico:** definir sistema como «conjunto de piezas» sin mencionar las relaciones ni el propósito.

*Fuentes: B1 pp.4–11.*

</details>

### 2. Ingeniería de sistemas

Define la ingeniería de sistemas. Explica en qué pone el foco y por qué aporta valor a un proyecto. Ilústralo con un fallo conocido.

<details>
<summary>Respuesta modelo</summary>

La **ingeniería de sistemas** es un enfoque transdisciplinar que gestiona la complejidad equilibrando las necesidades de los interesados e integrando personas, procesos, información y tecnología para proporcionar sistemas exitosos durante todo su ciclo de vida. La NASA lo resume como transformar las expectativas de los stakeholders en una solución equilibrada a lo largo de todo el ciclo de vida. Su marco de referencia es la norma ISO/IEC/IEEE 15288.

**Foco:** comprender el problema y el contexto operacional; identificar y equilibrar las necesidades de los stakeholders; definir y gestionar requisitos; desarrollar arquitectura y diseño; gestionar interfaces, riesgos y decisiones; integrar, verificar y validar; y mantener la coherencia técnica desde la concepción hasta la retirada. No consiste en diseñar componentes aislados.

**Valor:** no es un coste administrativo, sino una inversión para reducir incertidumbre, retrabajo, retrasos y sobrecostes. Aumenta la probabilidad de controlar el coste, aunque no lo garantiza por sí sola. Antes, los problemas de integración se descubrían con el diseño muy avanzado, cuando corregirlos era caro.

**Ejemplo:** en la pérdida de la sonda a Marte, una parte del sistema trabajaba en unidades imperiales y otra esperaba métricas. Cada parte podía estar bien hecha, pero fallaron la gestión de interfaces, la verificación entre subsistemas y la validación extremo a extremo: justo lo que cubre la ingeniería de sistemas.

**Debe aparecer**
- Enfoque transdisciplinar e integrador.
- Necesidades de los stakeholders y todo el ciclo de vida.
- Gestión de complejidad, interfaces y V&V.
- El valor como inversión, sin prometer que garantiza el resultado.
- Un ejemplo de fallo de integración.

**Error típico:** reducirla a «gestión del proyecto» o a «diseño de cada componente».

*Fuentes: B1 pp.7–8, 32–40.*

</details>

### 3. Complejidad y descomposición jerárquica

Explica por qué se descomponen los sistemas en niveles, qué dice la ley de Miller y qué consecuencias tiene descomponer. Relaciónalo con la integración.

<details>
<summary>Respuesta modelo</summary>

Los sistemas complejos superan nuestra capacidad cognitiva. La **ley de Miller** (1956) indica que en la memoria de trabajo manejamos unos **7 ± 2 elementos** a la vez; por encima de ese límite cometemos errores, nos cuesta ver relaciones y perdemos la visión global.

La solución es la **descomposición jerárquica**: el sistema de interés se divide en subsistemas, que a su vez se dividen hasta llegar a elementos individuales. El objetivo no es trocear «porque sí», sino que en cada nivel haya un número de elementos que una persona pueda comprender y gestionar. Como regla orientativa, #niveles ≈ log₇(#piezas): un destornillador necesita un nivel y un avión de 100.000 piezas, unos seis.

**Consecuencias:** cuanto más descomponemos, más sencillo es diseñar, asignar responsabilidades y verificar cada parte. Pero también **aumentan las interfaces, las dependencias y los problemas de integración**. La complejidad no desaparece: se gestiona.

**Relación con la integración:** «la integración existe porque hemos dividido previamente el sistema». Descomponemos porque la complejidad nos supera; integramos porque el cliente necesita un todo que funcione. El ejemplo del puzle de 500 piezas hecho por 500 personas aisladas lo muestra: cada pieza puede estar bien, pero sin requisitos e interfaces compartidos el conjunto no encaja.

**Debe aparecer**
- Ley de Miller: 7 ± 2.
- Descomposición jerárquica y su objetivo.
- Ventajas y precio de descomponer (más interfaces y dependencias).
- Que la complejidad se gestiona y por qué existe la integración.

**Error típico:** decir que descomponer «elimina» la complejidad.

*Fuentes: B1 pp.19–26.*

</details>

### 4. Pensamiento sistémico y modelo del iceberg

Define el pensamiento sistémico. Explica los cuatro niveles del modelo del iceberg y aplícalo a un problema de integración que se repite.

<details>
<summary>Respuesta modelo</summary>

El **pensamiento sistémico** consiste en mirar las cosas desde un punto de vista holístico: ver el todo y entender cómo interactúan las partes y se afectan mutuamente, de forma que el resultado es más que la suma de cada una. Permite descomponer grandes conceptos en partes y, a la vez, abstraerse de los detalles para ver el panorama general y el impacto de los cambios pequeños.

El **modelo del iceberg** recuerda que en un sistema complejo solo vemos la parte visible. Tiene cuatro niveles:
1. **Eventos:** qué vemos; los hechos visibles.
2. **Patrones:** qué se repite; las tendencias.
3. **Estructuras:** qué genera esos patrones; cómo está organizado el sistema.
4. **Modelos mentales:** qué creencias hay detrás; qué asume la organización y qué comportamientos premia.

Si solo atacamos el evento, el problema suele volver a aparecer.

**Ejemplo** (buque autónomo de vigilancia): *evento*, el software recibe datos erróneos de un sensor y las pruebas se retrasan; *patrón*, las mismas incidencias ya surgieron en proyectos anteriores; *estructura*, los equipos trabajan en silos y no hay un acuerdo de interfaces común ni pruebas conjuntas tempranas; *modelo mental*, «cada equipo cumple si entrega su subsistema» o «la integración se arregla al final». Estas causas son hipótesis que hay que contrastar.

**Debe aparecer**
- Visión del todo y de las interacciones.
- Los cuatro niveles en orden, con su pregunta.
- Por qué no basta con atacar el evento.
- Un ejemplo con los cuatro niveles.

**Error típico:** confundir patrón (lo que se repite) con estructura (lo que lo provoca).

*Fuentes: B1 pp.11–17 y 56.*

</details>

### 5. Ciclo de vida y control del ciclo de vida

Define el ciclo de vida de un sistema. Explica cómo se controla mediante revisiones, hitos y decision gates y qué aspectos deben equilibrarse.

<details>
<summary>Respuesta modelo</summary>

El **ciclo de vida** son las etapas que atraviesa un sistema desde que se identifica la necesidad hasta su retirada: concepción, definición de requisitos, arquitectura, diseño, implementación e integración, verificación y validación, operación, mantenimiento y retirada. Considerarlo entero permite crear una solución técnica coherente con el presupuesto y el plazo, y no diseñar solo para la entrega.

Hay que equilibrar en todas las decisiones el **business case**: producto, presupuesto y plazo. Los parámetros críticos son el tiempo hasta el *break even*, el ROI y la entrega. Se actúa controlando el ciclo de vida y optimizando el **triángulo de hierro**: coste, funcionalidad y plazo.

El control se hace con **revisiones**: reuniones formales, convocadas con tiempo, con las personas adecuadas y documentadas, cada una con sus cuestiones. Se planifican como *control gates*, *milestones* y *decision gates*. Una **decision gate** es un evento de aprobación con criterios de entrada y salida que responde si el proyecto satisface el caso de negocio, si es abordable y si puede entregarse cuando se necesita. Sus resultados van de GO a KILL, pasando por GO WITH ACTIONS, HOLD, RECYCLE y SUSPEND. Toda DG es revisión e hito, pero no toda revisión o hito es una DG.

**Ejemplo:** en un patrullero, una DG al final del diseño preliminar comprobaría si los requisitos y la arquitectura están maduros y si el coste sigue siendo asumible antes de comprometer el diseño de detalle.

**Debe aparecer**
- Etapas desde la necesidad hasta la retirada.
- Equilibrio de coste, funcionalidad y plazo, y business case.
- Revisiones y decision gates, con criterios y resultados posibles.
- La relación entre DG, revisión e hito.

**Error típico:** creer que el ciclo de vida termina con la entrega.

*Fuentes: B1 pp.46–50; B2 p.4.*

</details>

### 6. Sistema de sistemas (SoS)

Define un sistema de sistemas. Explica qué lo hace especialmente difícil y pon un ejemplo marítimo.

<details>
<summary>Respuesta modelo</summary>

Un **sistema de sistemas (SoS)** es un problema o diseño de amplia escala y multidisciplinar en el que participan sistemas múltiples, heterogéneos y distribuidos que, a su vez, son sistemas completos.

**Qué lo hace difícil:** sus sistemas **actúan de forma independiente** y **tienen ciclos de vida diferentes**; los requisitos iniciales suelen ser ambiguos y cambiantes; los límites son indefinidos y cambiantes; la gestión tiende a ensombrecer la ingeniería. Además, el entorno aporta complejidad creciente, recursos decrecientes, tecnologías y requisitos cambiantes, multiculturalidad y largos ciclos de adquisición. Los productos están cada vez más conectados entre sí y las disciplinas son más difusas, lo que refuerza la necesidad de la ingeniería de sistemas.

**Ejemplo:** la vigilancia de un puerto integra el radar costero, el sistema AIS, los buques de salvamento, el centro de control y los sistemas de la autoridad portuaria. Cada uno tiene su propietario, su ciclo de vida y su misión, pero juntos deben producir una imagen común de la situación marítima. Un cambio en el formato de datos de uno de ellos puede afectar a todos.

**Debe aparecer**
- Varios sistemas independientes, heterogéneos y distribuidos.
- Ciclos de vida distintos y límites cambiantes.
- Requisitos ambiguos o cambiantes.
- Un ejemplo con varios propietarios o misiones.

**Error típico:** llamar SoS a cualquier sistema con muchos subsistemas que dependen de un único propietario.

*Fuentes: B1 pp.18 y 29.*

</details>

---

## B2 · Stakeholders y requisitos

### 7. Stakeholder

Define stakeholder. Explica cómo se clasifican según Kochan y Rubinstein y qué debe hacer el ingeniero de sistemas con ellos. Pon ejemplos para Blue Horizon.

<details>
<summary>Respuesta modelo</summary>

Un **stakeholder** es un grupo, individuo, entidad o regulación que puede afectar a los objetivos de una organización o sistema, o verse afectado por ellos. Suministra recursos, soporte, empleo, tecnología o actividad regulatoria, y se relaciona con otros jerárquica, contractualmente o de otras formas.

Según **Kochan y Rubinstein**, un actor es stakeholder cuando cumple tres condiciones: **tiene activos críticos** para el éxito de la misión, **los invierte** en ella y **tiene capacidad de influir** en el resultado. Los **directos o definitivos** cumplen las tres; los **indirectos o latentes** no, aunque puedan verse afectados o tener interés.

**El ingeniero de sistemas debe:** identificarlos en todas las fases del proyecto, distinguir los principales, saber quién tiene autoridad para resolver conflictos e identificar cómo pretenden usar el producto. Sus intereses pueden entrar en conflicto y hay que equilibrarlos.

**Ejemplo, Blue Horizon:** directos: WindOcean Energy como operador, el centro de control, el equipo de mantenimiento y los proveedores del sistema de vigilancia. La autoridad marítima, como regulador, influye de forma decisiva en el resultado. Indirectos o latentes: pescadores y navegantes de la zona, medios de comunicación o ciudadanía local, que pueden verse afectados aunque no aporten recursos al proyecto.

**Debe aparecer**
- Definición: afecta o se ve afectado.
- Los tres criterios y la clasificación directo/indirecto.
- Qué hace el ingeniero de sistemas con ellos.
- Ejemplos de los dos tipos.

**Error típico:** limitar los stakeholders al cliente y al usuario.

*Fuentes: B2 pp.10–12 y 26.*

</details>

### 8. Necesidades, metas y objetivos (NGO)

Define necesidad, meta y objetivo. Explica cómo se relacionan y por qué deben acordarse con los stakeholders. Pon un ejemplo encadenado.

<details>
<summary>Respuesta modelo</summary>

Las **NGO** son la base de acuerdo de un proyecto:
- **Need (necesidad):** lo que se quiere resolver; el problema.
- **Goal (meta):** lo que hay que conseguir para resolver la necesidad.
- **Objective (objetivo):** detalla la meta y proporciona un medio para documentarla y comprobar su consecución.

Deben estar **alineadas**: cada meta debe emparejarse con alguna necesidad y cada objetivo con alguna meta. Además, tienen que **documentarse y ser aceptadas por los stakeholders**, porque son el punto de partida de los requisitos; un desacuerdo aquí se arrastra a toda la especificación.

**Ejemplo:** *necesidad*: el parque Blue Horizon sufre intrusiones de embarcaciones que ponen en riesgo la infraestructura. *Meta*: detectar y gestionar a tiempo las aproximaciones no autorizadas. *Objetivo*: detectar al menos el 95 % de las intrusiones con aviso al centro de control con antelación suficiente para actuar (cifra supuesta para practicar). Del objetivo saldrán requisitos y medidas como la MOE de porcentaje de intrusiones detectadas.

**Debe aparecer**
- Las tres definiciones diferenciadas.
- La alineación necesidad → meta → objetivo.
- Documentación y aceptación por los stakeholders.
- Un ejemplo en cadena, con un objetivo evaluable.

**Error típico:** escribir un objetivo que no se puede evaluar («mejorar la seguridad»).

*Fuentes: B2 p.13.*

</details>

### 9. Red de valor de stakeholders (SVN)

Define una SVN. Explica qué son los efectos de segundo orden y los bucles de valor, y qué aporta este análisis. Pon un ejemplo de cada efecto.

<details>
<summary>Respuesta modelo</summary>

Una **SVN (*Stakeholder Value Network*)** es un modelo que representa a los stakeholders y los flujos de valor que intercambian, incluyendo las **relaciones indirectas** entre ellos. La mayoría de los modelos se centran solo en una organización focal e ignoran esas relaciones, lo que puede hacer fracasar un proyecto.

- **Efecto de segundo orden:** consecuencia que llega al proyecto a través de otro stakeholder. Ejemplo: el regulador introduce una exigencia → el astillero modifica el diseño → el proveedor cambia un equipo → mantenimiento necesita nueva formación.
- **Bucle de valor:** relación circular en la que varios stakeholders intercambian valor continuamente. Ejemplo: el operador aporta experiencia de uso → ingeniería mejora el diseño → mantenimiento reduce tiempos → aumenta la disponibilidad → el cliente obtiene más valor.

**Qué aporta:** un marco para entender el impacto de las relaciones indirectas; reducir la complejidad al resaltar los stakeholders y flujos de valor importantes y construir un modelo más pequeño; información estratégica sobre rutas de valor críticas; y una plataforma común entre equipos. En el caso BP, los medios y la opinión pública resultaron mucho más influyentes de lo previsto, algo que un SVN completo habría revelado antes.

**Diferencia:** una SVN no es una arquitectura de equipos ni un CONOPS; trata de quién da y recibe valor, no de cómo funciona el sistema.

**Debe aparecer**
- Stakeholders y flujos de valor, con relaciones indirectas.
- Definición y ejemplo de segundo orden.
- Definición y ejemplo de bucle de valor.
- Al menos dos beneficios.

**Error típico:** dibujar solo flechas del proyecto hacia cada stakeholder, sin relaciones entre ellos.

*Fuentes: B2 pp.14–20.*

</details>

### 10. CONOPS

Define el CONOPS. Explica sus elementos clave, para qué sirve en la definición de requisitos y en qué se diferencia del OpsCon. Escribe un CONOPS breve de un sistema distinto al de clase.

<details>
<summary>Respuesta modelo</summary>

El **CONOPS (concepto de operación)** es un documento que describe cómo se espera que funcione un sistema **desde la perspectiva del usuario final**: quién lo utilizará, para qué, dónde, cuándo y en qué condiciones. Es como el guion de una película: cuenta qué ocurre durante la operación, no cómo está construido cada elemento.

**Elementos clave:** propósito y alcance; operaciones del sistema en distintos escenarios; interacciones del usuario; y entorno operativo, con sus restricciones y condiciones ambientales.

**Para qué sirve:** facilita la comunicación entre ingenieros, usuarios y gestores; comunica cualitativa y cuantitativamente las expectativas; junto con los casos de uso, revela requisitos y restricciones que podrían pasar inadvertidos; concreta la misión y da forma a los requisitos.

**Frente al OpsCon:** en sentido estricto, el ConOps describe las intenciones de uso, con el sistema como caja negra y a nivel estratégico; el OpsCon describe lo que el sistema hará, sin decir cómo, y por qué. Ninguno elige equipos.

**Ejemplo (salvamento):** ante un aviso de hombre al agua, el centro de coordinación recibe la alerta y la posición aproximada. El sistema ayuda al coordinador a definir la zona de búsqueda y a asignar medios disponibles. Las unidades de búsqueda reciben la zona asignada y comunican al centro lo que detectan. La operación debe mantenerse de día y de noche, con mala mar y con comunicaciones degradadas. Termina cuando la persona es localizada y evacuada o cuando la autoridad suspende la búsqueda.

**Debe aparecer**
- Perspectiva del usuario: quién, para qué, dónde, cuándo y condiciones.
- Los cuatro elementos clave.
- Su papel para obtener requisitos.
- La diferencia con el OpsCon o con un diseño.
- Un ejemplo sin componentes concretos.

**Error típico:** escribir un CONOPS que es una lista de equipos («radar + cámara + antena»).

*Fuentes: B2 pp.21–25 y 44.*

</details>

### 11. Requisito y requisito bien definido

Define qué es un requisito y en qué se diferencia de una expectativa. Explica las características de un requisito bien definido y transforma una expectativa en requisito.

<details>
<summary>Respuesta modelo</summary>

Una **expectativa** expresa lo que los stakeholders esperan conseguir, normalmente en lenguaje informal y desde su punto de vista. Un **requisito** es un enunciado formal, claro y estructurado que establece qué debe cumplir el sistema y que puede verificarse o validarse. Pasar de una a otro es pasar «del lenguaje del cliente al lenguaje de la ingeniería».

**Requisito bien definido:**
- **Realizable:** técnicamente viable con coste asumible.
- **Verificable:** permite una comprobación objetiva, preferiblemente cuantitativa. Por eso suele llevar **métrica + valor**.
- **Claro:** un solo significado.
- **Completo:** recoge perfiles de misión, operación, mantenimiento, entornos y restricciones.
- **Expresado como necesidad, no como solución:** el qué y el porqué, no el cómo.
- **Consistente** con los demás, **apropiado al nivel** y **no redundante**.

Debe usar *shall* (obligación) y evitar «etc.», «y/o», «pero no limitado a», «amigable» o «minimizará», así como sobreespecificar.

**Ejemplo:** expectativa: «el buque tiene que aguantar bien la mala mar». Requisito: «El buque deberá mantener una velocidad mínima de 12 nudos en estado de mar 5». Tiene métrica (velocidad), valor (12 nudos) y condición (estado de mar 5), y se verifica con ensayos o análisis de comportamiento en la mar.

**Debe aparecer**
- Diferencia entre expectativa y requisito.
- Al menos cinco características.
- Métrica y valor.
- Un ejemplo de transformación con condición.

**Error típico:** dar un «requisito» que en realidad elige la solución («llevará estabilizadores de aletas»).

*Fuentes: B2 pp.6, 21, 36–38 y 41–43.*

</details>

### 12. Clasificación de requisitos

Explica los principales tipos de requisitos con su pregunta clave y un ejemplo de cada uno. Explica qué es un requisito derivado.

<details>
<summary>Respuesta modelo</summary>

Los requisitos pueden clasificarse por muchos criterios: nivel (alto o detalle), etapa del ciclo de vida, origen (usuario o técnico), etc. La clasificación más útil en clase asocia cada tipo a una pregunta:

| Tipo | Pregunta | Ejemplo |
|---|---|---|
| Stakeholder | ¿Qué necesita el cliente? | Vigilar el parque eólico |
| Funcional | ¿Qué hace el sistema? | Detectar embarcaciones |
| Rendimiento | ¿Con qué prestaciones? | Detectarlas a 2 millas |
| Interfaz | ¿Con quién se conecta? | Enviar alertas al centro de control |
| Operativo | ¿En qué condiciones funciona? | Operar 24/7 |
| Mantenimiento | ¿Cómo se mantiene? | Sustituir el radar en menos de 30 min |
| Seguridad | ¿Cómo evitamos daños? | Impedir accesos no autorizados |
| Derivado | ¿Qué ha surgido de decisiones de diseño? | Si se añade un dron, una estación de carga |

Un **requisito derivado** no lo pide directamente el stakeholder: aparece como consecuencia de un requisito superior o de una decisión de diseño. Por eso los requisitos de bajo nivel dependen de las decisiones que se van tomando y el proceso es iterativo.

Si no sabes clasificar, hazle una pregunta al requisito: «qué hace» → funcional; «cuánto» → rendimiento; «con quién» → interfaz; «cómo se usa» → operativo. Un mismo enunciado puede tener varios aspectos; conviene separarlos.

**Debe aparecer**
- Al menos seis tipos con pregunta y ejemplo.
- Definición de derivado con su ejemplo.
- La regla de la pregunta para clasificar.

**Error típico:** confundir funcional y rendimiento: «detectar» es funcional; «detectar a 2 millas», rendimiento.

*Fuentes: B2 pp.31, 33–34.*

</details>

### 13. Proceso de definición de requisitos y sus salidas

Explica el proceso de definición de requisitos: entradas, controles, medios o capacitadores y salidas. Explica la diferencia entre requisitos y especificación.

<details>
<summary>Respuesta modelo</summary>

La **definición de requisitos** transforma necesidades y restricciones iniciales en requisitos claros, completos, verificables, trazables y gestionables, que sirven de base a todo el desarrollo. Puede describirse como una función con sus flechas:

- **Entradas:** necesidades de los stakeholders, descripción del problema, datos, restricciones del proyecto y documentos previos.
- **Actividades:** identificar stakeholders, sonsacar requisitos, definir restricciones de uso, construir el CONOPS y escenarios, resolver problemas, confirmar y registrar requisitos y mantener la trazabilidad.
- **Controles** (lo que estoy obligado a cumplir): legislación, normas de la industria, acuerdos, procedimientos del proyecto y directivas.
- **Capacitadores o medios** (lo que me ayuda a hacerlo): infraestructura, políticas y procesos de la empresa, equipos de trabajo, herramientas y recursos.
- **Salidas:** especificación de requisitos y restricciones (funcionales, de rendimiento, restricciones externas y entornos de utilización), criterios de validación, documentos de concepto (CONOPS), MOE y la matriz de trazabilidad (RVTM).

**Requisitos frente a especificación:** los requisitos son la **entrada** del diseño; la especificación es el **resultado** y puede incluir, además de requisitos, esquemas de diseño, planes o planos. Documentos habituales: SRD (sistema), IRD (interfaces), SRS (software) y PRD (proyecto).

**Ejemplo:** en Blue Horizon, la normativa marítima sería un control; el software de gestión de requisitos y el equipo de ingeniería, capacitadores; la lista de requisitos de alto nivel con su tabla MOE-MOP-TPM y su diagrama de trazabilidad, salidas.

**Debe aparecer**
- Las cuatro clases de flechas con ejemplos.
- La diferencia entre control y capacitador.
- Las salidas principales.
- Requisito como entrada y especificación como resultado.

**Error típico:** poner la normativa como capacitador: es un control.

*Fuentes: B2 pp.8, 29, 50–55.*

</details>

### 14. Trazabilidad y matriz de trazabilidad

Define la trazabilidad. Explica qué relaciones conserva, para qué sirve durante el ciclo de vida y cómo se documenta. Pon un ejemplo.

<details>
<summary>Respuesta modelo</summary>

La **trazabilidad** es la capacidad de seguir las relaciones entre los elementos del desarrollo: de cada necesidad a los requisitos que la cubren, de cada requisito a sus requisitos hijos, a las funciones y elementos que lo realizan y a las pruebas que lo comprueban, y en sentido inverso.

**Para qué sirve:**
- Comprobar **cobertura**: demostrar que ningún requisito se ha olvidado y que todo requisito procede de una necesidad.
- Analizar el **impacto de un cambio**: localizar requisitos, elementos y pruebas afectados.
- Gestionar la **volatilidad** junto con el control de cambios.
- Validar cada nivel frente al superior en la descomposición jerárquica.
- Preparar la verificación y validación, conectando el lado izquierdo y derecho del modelo en V.

**Cómo se documenta:** con una **matriz de trazabilidad** (o RVTM, matriz de verificación y trazabilidad de requisitos), que vincula requisitos con casos de prueba, elementos de diseño y entregables, normalmente con identificadores únicos. En proyectos grandes se gestiona con herramientas como DOORS, Polarion o Jama.

**Ejemplo:** necesidad de proteger el parque → R-01: detectar una embarcación de referencia a 2 km en las condiciones definidas → función «detectar» → subsistema de detección → T-01: ensayo a esa distancia. Si el cliente pide 3 km, la matriz indica que hay que revisar R-01, el subsistema y T-01.

**Debe aparecer**
- Relaciones en los dos sentidos entre niveles.
- Cobertura e impacto de cambios.
- Matriz de trazabilidad con su contenido.
- Un ejemplo de cadena con identificadores.

**Error típico:** creer que la trazabilidad evita los cambios: solo permite gestionarlos.

*Fuentes: B2 pp.8, 51–55; B3 pp.4–5, 14–15 y 35.*

</details>

---

## B3 · Definición y análisis de requisitos

### 15. Especificación de requisitos del sistema (SyRS) y SRR

Define la SyRS y su línea base. Explica qué debe cumplir cada requisito, qué niveles debe recoger y qué es la SRR.

<details>
<summary>Respuesta modelo</summary>

La **SyRS (System Requirements Specification)** es el resultado de la definición de requisitos del sistema: el conjunto básico o **línea base** de requisitos, que debe ser completo, preciso y no ambiguo, junto con el conjunto acordado de medidas (MOE, MOP y TPM).

Para evitar ambigüedades, los requisitos se desmenuzan jerárquicamente hasta que **cada uno es una sentencia** clara, única, consistente, individual y verificable; trazable hasta su requisito origen; no redundante ni en conflicto con otro; y **no sesgada por una implementación concreta**.

**Niveles:** si L0 es el requisito de misión o el CONOPS del usuario, la SyRS debe dejar definidos claramente **L1** (sistemas principales) y **L2** (subsistemas principales).

La **SRR (System Requirements Review)** es la revisión que examina los requisitos tal como están escritos para encontrar los que faltan, son incorrectos, redundantes o insatisfactorios. Ocurre pronto, en la Fase A (concepto y tecnología), antes de la Fase B (diseño preliminar). Los requisitos deben estar escritos, validados y accesibles para todo el equipo. Tras ella quedan bajo **gestión de configuración**: añadir, eliminar o modificar requisitos exige aprobación de la dirección del proyecto.

**Ejemplo:** en un buque de vigilancia, L0 «vigilar una zona marítima de forma continua»; L1 «el sistema de sensores deberá…»; L2 «el radar de superficie deberá…». En la SRR se detecta que falta un requisito de operación nocturna y se añade antes del diseño preliminar.

**Debe aparecer**
- SyRS como línea base completa y no ambigua, con sus medidas.
- Propiedades de cada requisito.
- Niveles L1 y L2.
- SRR: objetivo, momento y gestión de configuración.

**Error típico:** confundir la SRR con una revisión de diseño.

*Fuentes: B3 pp.4–7 y 12.*

</details>

### 16. Volatilidad de requisitos e isoperformance

Define la volatilidad de requisitos y la isoperformance. Explica causas, impactos y gestión de la primera, y beneficios de la segunda.

<details>
<summary>Respuesta modelo</summary>

La **volatilidad de requisitos** es el grado en que los requisitos cambian a lo largo del desarrollo mediante **adiciones, modificaciones o eliminaciones**.
- **Causas:** evolución de las necesidades, cambios regulatorios, maduración del CONOPS, errores u omisiones iniciales y evolución tecnológica.
- **Impactos:** más coste y plazo, retrabajo, mayor complejidad de la V&V y riesgo de inconsistencias.
- **Gestión:** una cierta volatilidad es normal e incluso necesaria; el objetivo es **gestionarla** mediante control de cambios y trazabilidad, no eliminarla.

La **isoperformance** es la representación de todas las combinaciones de parámetros de diseño que alcanzan un **mismo nivel de rendimiento**. Parte de la idea de que hay muchas formas de cumplir un requisito de prestaciones. Actúa sobre todo a nivel de **TPM**, obteniendo varias combinaciones que satisfacen un mismo MOP o MOE.
- **Beneficios:** evita fijar soluciones demasiado pronto, explora el espacio de diseño, identifica compromisos, facilita la optimización coste-prestaciones, reduce sobreespecificaciones y ayuda a negociar requisitos entre subsistemas.

**Relación:** si un requisito cambia, la isoperformance ayuda a ver qué combinaciones siguen siendo válidas sin rehacer todo el diseño.

**Ejemplo:** para un alcance de detección dado, puede subirse la antena y usar un radar de menos potencia, o al revés. Si después cambia la altura máxima permitida del mástil (volatilidad por una nueva norma), se elige otra combinación de la curva de isoperformance.

**Debe aparecer**
- Definición de volatilidad, causas, impactos y gestión.
- Definición de isoperformance y su nivel (TPM).
- Al menos tres beneficios.
- Un ejemplo con dos combinaciones equivalentes.

**Error típico:** decir que hay que eliminar la volatilidad.

*Fuentes: B3 pp.13–14.*

</details>

### 17. QFD, diseño axiomático y TRIZ

Explica estas tres metodologías de apoyo, qué hace cada una y por qué son complementarias. Describe las partes de la House of Quality.

<details>
<summary>Respuesta modelo</summary>

Son metodologías complementarias: **QFD identifica y prioriza; el diseño axiomático estructura; TRIZ ayuda a innovar**.

- **QFD (*Quality Function Deployment*)** traduce la voz del cliente en características técnicas medibles y priorizadas, estableciendo trazabilidad entre los «qués» y los «cómos». Forma parte de la gestión de calidad total (TQM). Su herramienta es la **House of Quality**:
  - *Filas:* requisitos del cliente (CR, «qués») con su importancia.
  - *Columnas:* descriptores técnicos (DT o EC, «cómos»).
  - *Matriz central:* relación de cada cómo con cada qué (fuerte 9, media 3, débil 1, nada 0).
  - *Tejado:* apoyos y conflictos entre características técnicas.
  - *Base:* prioridad de cada característica (suma de importancia × relación), valores objetivo y evaluación competitiva.
- **Diseño axiomático** relaciona requisitos funcionales con parámetros de diseño buscando soluciones robustas y poco acopladas. Recorre los dominios cliente → funcional → físico → proceso, con dos axiomas: **independencia** (mantener independientes los requisitos funcionales) e **información** (minimizar la complejidad).
- **TRIZ** (Altshuller) ayuda a identificar y resolver **contradicciones técnicas** mediante principios inventivos, sin quedarse solo en soluciones de compromiso: contradicción → principios inventivos → solución.

**Ejemplo:** en un dron de vigilancia, QFD muestra que la autonomía es la característica más prioritaria; el tejado revela su conflicto con el peso; el diseño axiomático ayuda a que mejorar la autonomía no altere otras funciones; TRIZ busca una solución que aumente la autonomía sin el aumento de peso.

**Debe aparecer**
- Qué hace cada una, en una frase.
- Las partes de la House of Quality.
- Los dos axiomas.
- Contradicción como idea central de TRIZ.
- Por qué son complementarias.

**Error típico:** colocar los conflictos entre características en la matriz central en lugar del tejado.

*Fuentes: B3 pp.15–33.*

</details>

### 18. Análisis funcional

Define el análisis funcional. Explica su propósito, sus actividades y resultados, y por qué todavía no es diseño. Clasifica sus herramientas en sus cuatro grupos.

<details>
<summary>Respuesta modelo</summary>

El **análisis funcional** es la etapa final del análisis de requisitos en la que los requisitos se traducen en **funciones** que el sistema deberá realizar (FBSE, *Function Based Systems Engineering*). Se descompone de forma lógica y jerárquica en cada nivel de detalle. Indica a los diseñadores qué debe hacer el sistema, cómo de bien y qué restricciones limitan el diseño, y prepara la arquitectura.

**Por qué no es diseño:** define qué tendrá que hacer el sistema, no cómo será. «El sistema deberá proporcionar imágenes con resolución suficiente para identificar embarcaciones a 5 km» es análisis funcional; «una cámara 8K sobre una torreta giroestabilizada» ya es diseño.

**Actividades:** definir estados y modos, funciones e interfaces externas y funcionales; asignar requisitos de rendimiento a funciones; analizar rendimiento, tiempos y recursos; analizar modos de fallo y criticidad; definir detección de fallos y recuperación; e integrar funciones. Es **iterativo**.

**Resultados:** la **arquitectura funcional**, los elementos con sus funciones y requisitos trazados, y los requisitos de interfaz. La asignación de funciones a componentes determinará la arquitectura del sistema, que no queda definida hasta completarse con los requisitos de rendimiento.

**Herramientas:**
1. *Definición de funciones:* FFBD, IDEF0, IPO.
2. *Análisis del comportamiento:* diagramas de estados, de actividades y de secuencia.
3. *Análisis de interfaces:* N², matriz de interfaces, arquitecturas funcionales.
4. *Validación mediante modelos y simulación:* simulación, modelos ejecutables, escenarios.

Hoy muchos de estos artefactos se integran en modelos SysML y entornos MBSE.

**Ejemplo:** «el dron ha de vigilar 100 km²» se transforma en detectar objetivos, navegar por la zona, capturar imágenes, transmitir información y gestionar energía.

**Debe aparecer**
- Requisitos traducidos a funciones, sin decidir la solución.
- Ejemplo de diferencia entre función y diseño.
- Actividades y resultados principales.
- Los cuatro grupos de herramientas.

**Error típico:** hacer un «análisis funcional» con nombres de componentes.

*Fuentes: B3 pp.34–47.*

</details>

### 19. Lenguajes de modelado: SysML, OPM y Modelica

Explica por qué hace falta un lenguaje de modelado, sus componentes (ontología, semántica y sintaxis) y qué aporta cada uno de los tres lenguajes vistos en clase.

<details>
<summary>Respuesta modelo</summary>

Un sistema admite **múltiples vistas**: FFBD, IDEF0, TLS, diagramas de estados… Todas pueden ser correctas, pero ninguna es completa. Si son un conjunto de dibujos sueltos, aparecen inconsistencias, terminología distinta, relaciones implícitas y duplicación de información. Por eso hace falta un **lenguaje de modelado**, con el que hablar el mismo idioma, evitar ambigüedades, relacionar los elementos, mantener la coherencia y facilitar el análisis y la trazabilidad.

Todo lenguaje tiene:
- **Ontología:** qué entidades pueden existir y describirse, y cómo se agrupan y relacionan.
- **Semántica:** el significado de esas entidades.
- **Sintaxis:** las reglas para construir «frases» correctas.

**Lenguajes vistos:**
- **SysML:** lenguaje visual del OMG, extensión de UML para ingeniería de sistemas. Modela requisitos, funciones, comportamiento, interfaces, arquitectura y verificación. Es independiente de la metodología y las herramientas, y es un habilitador fundamental de MBSE. UML, en cambio, se pensó sobre todo para software.
- **OPM (*Object-Process Methodology*, ISO 19450):** representa todo con un único conjunto de conceptos: **objetos** (lo que existe), **estados** (situaciones de un objeto) y **procesos** (lo que transforma objetos o cambia sus estados, asociado a un verbo). La forma es la suma de los objetos; la función surge de un proceso.
- **Modelica:** lenguaje orientado a objetos para **simular sistemas físicos**, multidominio y basado en ecuaciones. Es **acausal**: se declara la relación (por ejemplo, V = R·I) y el simulador decide qué variable calcular según el contexto. No es propietario.

**Resumen:** SysML ayuda a describir el sistema; Modelica, a comprender su comportamiento físico. Juntos son pilares del MBSE y de los gemelos digitales.

**Debe aparecer**
- Por qué no bastan diagramas sueltos.
- Ontología, semántica y sintaxis.
- Una frase correcta de cada lenguaje.
- El contraste describir frente a simular.

**Error típico:** decir que SysML es una herramienta comercial o que Modelica sirve para redactar requisitos.

*Fuentes: B3 pp.48–58.*

</details>

---

## B4 · Arquitectura y diseño conceptual

### 20. Arquitectura del sistema

Define la arquitectura de un sistema. Explica la diferencia entre arquitectura lógica y física, por qué es importante y qué la hace buena.

<details>
<summary>Respuesta modelo</summary>

La **arquitectura** es la **organización fundamental de la solución**: define los elementos principales, la asignación de funciones a esos elementos, sus relaciones e interfaces, y los parámetros principales y restricciones. No es la forma final ni un dibujo: es un conjunto coherente de **modelos, relaciones, decisiones y requisitos derivados**. Los requisitos definen qué debe conseguirse; la arquitectura decide cómo organizar la solución para conseguirlo.

- **Arquitectura lógica:** resultado de la descomposición lógica; describe cómo debe funcionar el sistema mediante funciones, flujos de información, energía y materia, comportamientos, estados y modos, y requisitos derivados.
- **Arquitectura física:** organiza los elementos que realizan esas funciones (equipos, software, personas) y sus interfaces.

**Por qué importa:** las decisiones de arquitectura se toman pronto pero condicionan gran parte del ciclo de vida. Reduce la complejidad, permite comparar alternativas y ver compromisos entre prestaciones, coste, plazo y riesgo, facilita la evolución y condiciona el valor. Es más barato cambiar un bloque en un modelo que descubrir en la integración que dos subsistemas no se comunican. Reduce la ambigüedad del problema mientras hace explícita la complejidad de la solución.

**Buena arquitectura:** explora alternativas; está bien estructurada y asigna funciones a los elementos adecuados; gestiona la complejidad con modularidad; y piensa en todo el ciclo de vida (desarrollo, construcción, operación, mantenimiento y retirada). Un mismo conjunto de requisitos puede admitir varias arquitecturas válidas.

**Ejemplo:** para un dron de inspección, la arquitectura organiza plataforma aérea, sensores, energía, navegación, comunicaciones y estación de control, qué función hace cada uno y cómo se conectan.

**Debe aparecer**
- Organización fundamental: elementos, funciones asignadas e interfaces.
- No es un dibujo ni la forma final.
- Diferencia entre lógica y física.
- Importancia y rasgos de una buena arquitectura.

**Error típico:** presentar una lista de componentes como si fuera la arquitectura.

*Fuentes: B4 pp.7–14, 19 y 23.*

</details>

### 21. Función y forma

Define función y forma. Explica cómo se relacionan a través de la arquitectura y los dos caminos para pasar de una a otra. Pon un ejemplo de cada camino.

<details>
<summary>Respuesta modelo</summary>

- **Función:** lo que hace el sistema; las actividades y transformaciones que realiza. Responde a «¿qué hace?», puede descomponerse en subfunciones y es, inicialmente, independiente de una solución concreta.
- **Forma:** los elementos que componen la solución y la estructura y relaciones entre ellos. Responde a «¿con qué y cómo se realiza?» y puede incluir personas, equipos, software e información.

La **arquitectura relaciona las funciones** que debe realizar el sistema **con los elementos de forma que las implementan**.

**Dos caminos:**
1. **Diseño directo:** partimos de la función para definir la forma. Sabemos qué debe hacer el sistema, buscamos elementos capaces de hacerlo y combinamos y optimizamos. Ejemplo: necesitamos «mantener la posición del buque frente al viento y la corriente» y buscamos soluciones (propulsores azimutales, hélices transversales, control de posicionamiento dinámico).
2. **Ingeniería inversa:** partimos de la forma de una solución existente para deducir sus funciones. Observamos el sistema, identificamos sus elementos físicos y deducimos qué hace cada uno y para qué. Ejemplo: analizar un remolcador existente para entender qué función cumple cada elemento antes de proyectar uno nuevo.

En ingeniería naval se **combinan ambos**: se parte de funciones conocidas y de soluciones existentes, que hay que adaptar, integrar y optimizar para cada nuevo sistema.

**Ejemplo dron:** funciones: detectar, capturar imágenes, transmitir, mantener el vuelo. Forma: cámara, sensores, hélices y motores, batería, software de control y enlace.

**Debe aparecer**
- Las dos definiciones con su pregunta.
- La arquitectura como unión entre ambas.
- Diseño directo e ingeniería inversa con ejemplo.
- Que en naval se combinan.

**Error típico:** expresar funciones con sustantivos de componentes («radar») en lugar de verbos («detectar»).

*Fuentes: B4 pp.16–18.*

</details>

### 22. Concepto de solución

Define un concepto de solución. Explica cómo se expresa, la diferencia entre concepto inicial y desarrollado, y en qué se diferencia de la arquitectura. Usa el ejemplo del tren.

<details>
<summary>Respuesta modelo</summary>

Un **concepto de solución** es una idea general sobre cómo satisfacer una necesidad, sin definir todavía todos sus elementos. Se expresa como **tipo de solución + característica diferenciadora + finalidad**; por ejemplo: dron aéreo autónomo + con sensores visuales y térmicos + para inspeccionar aerogeneradores marinos.

- **Concepto inicial:** expresa la idea principal, relaciona la forma general con la función y permite imaginar y comparar alternativas. «Dron aéreo autónomo para inspección de aerogeneradores marinos».
- **Concepto desarrollado:** especifica las características principales, tecnologías y parámetros que condicionan el diseño, y es el punto de partida de la arquitectura. «Dron eléctrico de despegue vertical, con cámara visual y térmica, navegación autónoma y enlace de datos con una estación de control».

**Frente a la arquitectura:** el concepto define el **enfoque** de la solución; la arquitectura define **cómo se organiza**, con elementos, funciones asignadas e interfaces.

**Ejemplo del tren (RENFE):** la necesidad era reducir el tiempo de viaje sin rehacer las líneas. Rehacer la infraestructura era caro y lento, y optimizar la operación tenía poco margen, así que se actuó sobre el vehículo. El **concepto** fue permitir más velocidad en curva inclinando la caja. «Inclinar la caja» todavía no es arquitectura: la **arquitectura** aparece al decidir qué funciones, elementos e interfaces detectan la curva, controlan y producen la inclinación. El sistema físico resultante es un tren basculante o pendular.

**Debe aparecer**
- Definición de concepto.
- Fórmula tipo + característica + finalidad.
- Diferencia entre inicial y desarrollado.
- Diferencia entre concepto y arquitectura con el tren.

**Error típico:** considerar que «inclinar la caja» ya es la arquitectura.

*Fuentes: B4 pp.20–25.*

</details>

### 23. Valor y reducción de la ambigüedad

Define el valor en ingeniería de sistemas. Explica cómo se reduce la ambigüedad de una necesidad con operando, atributo, transformación y valor, y aplícalo a un ejemplo distinto del refrigerador.

<details>
<summary>Respuesta modelo</summary>

El **valor** relaciona el **beneficio** que proporciona el sistema con el **coste** necesario para obtenerlo.
- *Beneficio:* necesidades satisfechas, funcionalidad proporcionada y valor percibido por los beneficiarios.
- *Coste:* desarrollo y adquisición, operación y mantenimiento, y recursos y tiempo.

Una buena arquitectura **maximiza el beneficio dentro de un coste asumible** considerando todo el ciclo de vida, no solo el precio de compra.

Para pasar de una necesidad general a un propósito concreto, se **reduce la ambigüedad** definiendo el cambio deseado:
1. **Operando:** ¿sobre qué actúa el sistema?
2. **Atributo:** ¿qué característica queremos modificar?
3. **Transformación:** ¿qué cambio debe producirse?
4. **Valor:** ¿qué beneficio genera ese cambio?

En el refrigerador: comida → estado de conservación → ralentizar el deterioro → conservar los alimentos más tiempo.

**Ejemplo nuevo (desalinizadora de un buque):** operando, agua de mar; atributo, contenido de sal; transformación, reducirlo hasta hacerla potable; valor, autonomía de agua dulce para la tripulación sin depender del puerto. Definir así la necesidad no presupone la solución (ósmosis inversa o evaporación) y permite comparar conceptos por su beneficio y su coste a lo largo de la vida del buque.

**Debe aparecer**
- Valor como beneficio frente a coste, con sus componentes.
- Ciclo de vida en el coste.
- Los cuatro pasos con su pregunta.
- Un ejemplo nuevo que no fije la solución.

**Error típico:** igualar valor a «menor precio».

*Fuentes: B4 pp.26–27.*

</details>

### 24. Generación y selección de conceptos; arquitectura frente a diseño

Explica la diferencia entre generar y seleccionar conceptos y el tipo de pensamiento de cada fase. Después distingue arquitectura y diseño y ordena todo el proceso de B4.

<details>
<summary>Respuesta modelo</summary>

Cuando ya sabemos qué queremos conseguir pero no cómo, empieza la búsqueda de conceptos de solución. Primero se **amplía** el espacio de soluciones y después se **reduce** mediante criterios.

- **Generar conceptos:** abrir el espacio de alternativas con **pensamiento divergente**, apoyándose en brainstorming, mapas mentales o la matriz morfológica. No hay que quedarse con la primera idea.
- **Seleccionar un concepto:** comparar alternativas con **pensamiento convergente**, considerando valor, coste, riesgo y restricciones, y justificar la elección.

**Arquitectura frente a diseño:**
- *Arquitectura:* define los bloques principales, asigna funciones a elementos, establece relaciones e interfaces y fija parámetros principales y restricciones.
- *Diseño:* concreta dimensiones, selecciona componentes y materiales, define valores detallados y optimiza la solución.

**Proceso de B4:** 1) entender antes de solucionar: identificar la necesidad y el cambio deseado, sin partir de una solución preconcebida; 2) generar conceptos; 3) seleccionar un concepto; 4) definir la arquitectura; 5) después, el diseño.

**Ejemplo:** para reducir emisiones de un ferri en puerto se generan conceptos (conexión eléctrica a tierra, baterías, hidrógeno, motores más eficientes) y se seleccionan con criterios de coste, madurez y riesgo. Elegida la conexión a tierra, la arquitectura organiza conexión, conversión, cuadro eléctrico y control con sus interfaces; el diseño fija la potencia, el cable y el modelo del convertidor.

**Debe aparecer**
- Divergente frente a convergente, con técnicas y criterios.
- Cuatro rasgos de arquitectura y cuatro de diseño.
- Los cinco pasos en orden.
- Un ejemplo que recorra el proceso.

**Error típico:** saltar directamente al diseño sin generar alternativas.

*Fuentes: B4 pp.28–31.*

</details>

---

## Plantilla para cualquier pregunta de definición

1. **Definición** en una o dos frases, con las palabras clave del tema.
2. **Explicación**: partes, tipos, pasos o características.
3. **Diferencia** con el concepto con el que se suele confundir.
4. **Ejemplo** concreto, mejor naval o del caso Blue Horizon.
5. **Por qué importa** en la ingeniería de sistemas, en una frase.
