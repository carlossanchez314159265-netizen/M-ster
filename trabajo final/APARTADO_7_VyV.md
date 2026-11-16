---
title: "7. VERIFICACIÓN Y VALIDACIÓN"
subtitle: "Proyecto fin de curso IINT · Embarcación multipropósito portuaria · Borrador del apartado 7"
---

***Verificación frente a validación***

La **verificación** comprueba que la embarcación cumple los requisitos definidos en el apartado 4 (*¿hemos construido el sistema correctamente?*). La **validación** comprueba que la embarcación resuelve la necesidad real de la autoridad portuaria en su entorno de operación (*¿hemos construido el sistema correcto?*).

***Estrategia de verificación***

Siguiendo el Modelo en V y el orden de integración del apartado 6, la verificación avanza de lo más sencillo a lo más complejo: **pruebas unitarias** de cada equipo en fábrica (FAT), **pruebas de integración** con la embarcación amarrada en puerto y **verificación del sistema completo** en pruebas de mar (SAT). Por último, la **validación con el usuario** se realiza con la tripulación en una operación piloto.

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

***Escenario de validación***

**Jornada piloto en el puerto:** la tripulación maniobra en la dársena, recoge residuos flotantes, contiene un pequeño vertido y apoya el mantenimiento de una baliza. Se valida si completa todas las tareas **sin ayuda externa, de forma segura y en un tiempo aceptable para la autoridad portuaria**. Su opinión se registra como primera información de operación (apartado 8).
