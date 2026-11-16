---
title: "7. VERIFICACIÓN Y VALIDACIÓN"
subtitle: "Proyecto fin de curso IINT · Embarcación multipropósito portuaria · Borrador del apartado 7"
---

***Verificación frente a validación***

La **verificación** comprueba que la embarcación cumple los requisitos definidos en el apartado 4 (*¿hemos construido el sistema correctamente?*). La **validación** comprueba que la embarcación resuelve la necesidad real de la autoridad portuaria en su entorno de operación (*¿hemos construido el sistema correcto?*).

***Estrategia de verificación***

Siguiendo el Modelo en V y el orden de integración definido en el apartado 6, la verificación se realiza en tres etapas, de lo más sencillo a lo más complejo:

1. **FAT (Factory Acceptance Test):** cada equipo se comprueba por separado en fábrica o taller antes de instalarse a bordo (cesta recolectora, grúa, sensores).
2. **Pruebas en puerto (embarcación amarrada):** se comprueban los subsistemas ya integrados, en el mismo orden de integración: primero estructural y propulsión (A + B), después gestión de residuos y cargas (C + D) y, por último, control y comunicaciones (E).
3. **SAT (Sea Acceptance Test o pruebas de mar):** se comprueba la embarcación completa navegando en aguas portuarias.

***Requisitos seleccionados para la verificación***

En el apartado 4 se han definido 18 requisitos para cubrir todas las necesidades del sistema (N1–N10). De ellos, se consideran **fundamentales los 8 siguientes**, ya que están directamente ligados a las misiones principales de la embarcación y cubren todos los tipos de requisito exigidos: operación, seguridad, mantenimiento, adaptabilidad, gestión de la información y retirada. Los 10 requisitos restantes se verificarán siguiendo el mismo procedimiento.

***Matriz de verificación de los requisitos fundamentales***

| Cód. | Requisito | Necesidad | Subsistema | Método | Etapa | Criterio de aceptación |
|----|------------------------|-----|-----|---------|------|-------------|
| RF1 | La cesta recolectora hidráulica debe izar cargas de hasta 500 kg | N1 | C | **Prueba** | FAT | Iza 500 kg sin pérdidas ni deformaciones |
| RF3 | La cubierta debe disponer de 15 m² homologados para 4 operarios y 1000 kg de carga útil | N2 | A | **Inspección** + **prueba** | Puerto | Superficie medida ≥ 15 m² y soporta 1000 kg |
| RO1 | La hélice de proa debe permitir un radio de giro ≤ 1,2 veces la eslora | N7 | B | **Prueba** | SAT | Radio de giro medido ≤ 1,2 esloras |
| RS1 | Las grúas deben incorporar válvulas de retención de carga | N1, N3, N4 | C, D | **Prueba** | FAT | La carga no cae al simular una pérdida de presión hidráulica |
| RM1 | Debe haber ≥ 500 mm libres alrededor de bombas y motores principales | N8 | A, B | **Inspección** + **demostración** | Puerto | Distancia medida ≥ 500 mm y un operario accede y desmonta un equipo |
| RA1 | La cubierta debe tener anclajes estandarizados para módulos de equipos | N2, N3 | A | **Demostración** | Puerto | Se instala y desinstala un módulo sin modificar la estructura |
| RI1 | Los sensores deben mostrar el nivel de llenado de los tanques con latencia ≤ 1 s | N1, N4 | C, E | **Prueba** | Puerto / SAT | Latencia medida en el puente ≤ 1 s |
| RR1 | El casco debe ser de aluminio con reciclabilidad estructural > 90 % | N10 | A | **Análisis** | Diseño | El inventario de materiales confirma > 90 % de material reciclable |

***Justificación de los métodos elegidos***

- **Prueba:** para los requisitos que se pueden medir con el sistema funcionando (cargas, radio de giro, latencia, seguridad ante fallo).
- **Inspección:** para dimensiones, espacios y cumplimiento normativo, que se comprueban midiendo o revisando.
- **Demostración:** para las tareas que hay que ver realizar (desmontar un equipo, cambiar un módulo).
- **Análisis:** para lo que no se puede probar en la entrega. La reciclabilidad del casco solo se comprobará realmente en la retirada, por lo que se verifica sobre el inventario de materiales.

***Escenario de validación: una jornada de trabajo en el puerto***

La validación se realiza mediante una operación piloto en el puerto real, con la tripulación y el personal de mantenimiento que van a utilizar la embarcación:

1. **Salida y maniobra en la dársena** (subsistema B). La tripulación valora si la embarcación maniobra con facilidad entre muelles y otras embarcaciones (N7).
2. **Recogida de residuos flotantes** con la cesta recolectora (C). Al llenarse la bodega, los sensores avisan al puente (E). La tripulación valora si la información llega a tiempo y es útil.
3. **Aviso de un pequeño vertido.** La tripulación contiene y bombea el vertido al tanque de aguas oleosas (C), comprobando que la maniobra se realiza con seguridad.
4. **Apoyo al mantenimiento de una baliza** con la grúa (D), con operarios trabajando en la cubierta (A, N2).
5. **Regreso a puerto**, descarga de los residuos al gestor autorizado y registro de la jornada.

**Criterio de validación:** la tripulación completa todas las tareas de la jornada **sin ayuda externa, de forma segura y en un tiempo aceptable para la autoridad portuaria**. Además, el personal de mantenimiento valora la facilidad de acceso a los equipos críticos (N8).

Los resultados se comparan con los MOE de la matriz de trazabilidad del apartado 6. La opinión de la tripulación y del personal de mantenimiento se registra y se conserva, ya que será la primera información de operación del apartado 8.
