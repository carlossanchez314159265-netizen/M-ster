---
title: "8. OPERACIÓN Y MANTENIMIENTO"
subtitle: "Proyecto fin de curso IINT · Embarcación multipropósito portuaria · Borrador del apartado 8"
---

***Misión habitual***

Una jornada típica comienza con la **revisión previa a la salida** (niveles, presión hidráulica de la grúa y la cesta, estado de los sensores en el puente). La embarcación sale del muelle y realiza la **ruta de limpieza** por las dársenas, recogiendo residuos flotantes con la cesta recolectora hasta que los sensores de nivel avisan de que la bodega está llena. Durante la jornada puede recibir avisos de la autoridad portuaria para **apoyar el mantenimiento de una boya o baliza**, **transportar personal o equipos** o **contener un pequeño vertido**. Al regresar, descarga los residuos al gestor autorizado y la tripulación **registra la jornada** y las incidencias detectadas.

***Actividades básicas de mantenimiento***

| Tipo | Actividad | Subsistema | Quién |
|-----|--------------------------|-----|------------|
| Diario | Revisión previa a la salida, limpieza de la cesta y de la cubierta | C, D, A | Tripulación |
| Periódico | Revisión de motores, hélice de proa y circuito hidráulico de la grúa y la cesta | B, C, D | Personal de mantenimiento |
| Periódico | Vaciado y limpieza de la bodega y del tanque de aguas oleosas | C | Personal de mantenimiento + gestor autorizado |
| Periódico | Comprobación y calibración de los sensores de nivel, GPS y AIS | E | Personal de mantenimiento |
| Varada | Inspección del casco de aluminio, la defensa de caucho y la protección contra la corrosión | A | Astillero |
| Reglamentario | Reconocimientos de la sociedad de clasificación y revisión de equipos salvavidas y contraincendios | A | Sociedad de clasificación |
| Correctivo | Sustitución de equipos averiados | Todos | Personal de mantenimiento + proveedores |

***Equipos accesibles, sustituibles o desmontables***

- **Accesibles:** bombas y motores principales, con al menos 500 mm libres a su alrededor (RM1).
- **Sustituibles:** válvulas y filtros, con al menos un 75 % de componentes estandarizados ISO/DIN (RM2), y los sensores, que pueden cambiarse sin reprogramar la propulsión gracias al aislamiento de subsistemas (apartado 5).
- **Desmontables:** la cesta recolectora, la grúa y los módulos de cubierta, fijados mediante los anclajes estandarizados (RA1).

***Documentación, formación, repuestos y herramientas***

- **Documentación:** manuales de usuario del sistema integrado, SOPs de las maniobras conjuntas (apartado 6) y plan de mantenimiento con la frecuencia de cada actividad.
- **Formación:** tripulación formada en los equipos de carga y en la actuación ante fallos y emergencias; personal de mantenimiento formado en el sistema hidráulico y en el sistema de control.
- **Repuestos:** stock inicial de componentes críticos y fácilmente dañables (cableado, fusibles, filtros, juntas hidráulicas), aprovechando la estandarización de componentes.
- **Herramientas:** herramientas estándar para los componentes ISO/DIN y equipos de diagnóstico para la red de sensores.

***Información de operación y mantenimiento que debe conservarse***

- **Registro de operación:** horas de funcionamiento, residuos recogidos, vertidos atendidos e incidencias, incluido el *feedback* de otras embarcaciones del puerto (apartado 3).
- **Historial de mantenimiento:** actividades realizadas, averías, equipos sustituidos y repuestos consumidos.
- **Línea base *As Built* actualizada** (apartado 6) con todos los cambios realizados durante el servicio.
- **Certificados e inspecciones** de la sociedad de clasificación y de las autoridades.

Esta información permite planificar el mantenimiento, justificar una futura modernización (apartado 9) y facilitar la retirada y el reciclaje (apartado 10).

***Problema en servicio***

**Problema:** durante una jornada de limpieza falla la unidad del sistema de control y comunicaciones (E). El puente deja de recibir el nivel de la bodega y las señales de la grúa y la cesta. Por seguridad, la tripulación suspende la recogida y la embarcación queda inoperativa hasta su reparación, aunque la cesta, la grúa y la propulsión funcionan correctamente.

**Decisión de arquitectura relacionada:** en el apartado 5 se decidió **centralizar todo el intercambio de información en un único punto**, el subsistema de control (E). Esta decisión simplifica la integración y el diagnóstico, pero convierte al subsistema E en un **punto único de fallo** del que dependen las operaciones de los demás subsistemas.

**Lección aprendida:** habría sido conveniente prever desde el diseño un **mando local de emergencia** en la grúa y la cesta, o redundancia en la unidad de control, para que un fallo de información no detenga toda la misión. Esta mejora puede incorporarse en la modernización del apartado 9.
