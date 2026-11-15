---
title: "Proyecto fin de curso IINT — Análisis del trabajo del equipo y base común para las partes 7–10"
subtitle: "Embarcación multipropósito portuaria · Curso 2026/2027"
---

# 1. Estado del trabajo del equipo

| Parte | Contenido | Estado |
|---|---|---|
| 1 | Misión y alcance | Hecha |
| 2 | Mapa de stakeholders (8 stakeholders, Tabla 1.1) | Hecha |
| 3 | Diagrama de valor | Hecha |
| 4 | Necesidades y requisitos principales | **Pendiente** |
| 5 | Arquitectura funcional y de alto nivel | **Pendiente** |
| 6 | Construcción, integración y entrada en servicio | **Pendiente** |
| 7–10 | V&V, operación y mantenimiento, modernización, retirada | Mis partes |

Las partes 4 y 5 son las que definen los **requisitos (R)** y los **bloques (B)** que las partes 7–10 deben citar. Hasta que estén, se propone la base provisional de la sección 4.

# 2. Qué se aprovecha de las partes 1–3

**Stakeholders → en qué parte intervienen**

| Stakeholder | Influencia | Dónde aparece en las partes 7–10 |
|---|---|---|
| Autoridad portuaria | Muy alta | Validación final (7), decisión de modernizar (9) y de retirar (10) |
| Tripulación | Alta | Escenario de validación (7), misión habitual (8), formación (8, 9) |
| Personal de mantenimiento | Alta | Mantenibilidad, accesibilidad, equipos estandarizados (8) |
| Astillero de construcción | Alta | Información generada en construcción que se conserva (8, 10) |
| Proveedores y fabricantes | Media | Repuestos y sustitución (8), nuevos equipos (9) |
| Autoridades y organismos reguladores | Media | Verificación normativa (7), gestión de residuos (10) |
| Otras embarcaciones del puerto | Media | Feedback de incidencias como información de operación (8) |
| Empresas de desguace y reciclaje | Media | Toda la parte 10: desmontaje, reutilización, reciclaje |

**Del diagrama de valor**

- La tensión *Autoridades ↔ Desguace* por la **gestión de los residuos** enlaza con la parte 10.
- El *feedback e información sobre incidencias* de otras embarcaciones es información de operación a conservar (parte 8).
- La tensión *Tripulación ↔ Mantenimiento* por la **disponibilidad de la embarcación** justifica el diseño para mantenimiento rápido (parte 8).

**De los límites del sistema (parte 1)**

Capacidad de almacenamiento de residuos, autonomía y capacidad del equipo de recogida son candidatos directos a **pruebas** en la parte 7. El equipo de recogida es además el bloque que se moderniza en la parte 9 (mejor detección de residuos).

# 3. Puntos a comentar con el grupo

1. **Sociedades de clasificación** y **gestores autorizados de residuos** aparecen como elementos externos en la parte 1, pero no en el mapa de stakeholders. Aclarar si están incluidos en "Autoridades" y "Desguace y reciclaje", porque se citan en las partes 7 y 10.
2. Los **escenarios de operación** no mencionan la respuesta a pequeños vertidos, aunque sí está en la misión. Conviene añadirla para poder validarla en la parte 7.

# 4. Base común provisional (propuesta para aprobar o modificar)

## 4.1 Requisitos de alto nivel

| ID | Requisito | Tipo exigido | Procede de |
|---|---|---|---|
| R1 | La embarcación debe recoger y almacenar a bordo residuos flotantes en aguas portuarias | Operación | Autoridad portuaria, otras embarcaciones |
| R2 | Debe poder operarse por una tripulación reducida con formación básica | Operación | Tripulación |
| R3 | Debe garantizar la seguridad de tripulación y personal en las maniobras de carga, boyas y vertidos | Seguridad | Autoridades, tripulación |
| R4 | Los equipos críticos deben ser accesibles y sustituibles sin desmontar estructura | Mantenimiento | Personal de mantenimiento, proveedores |
| R5 | Debe admitir la incorporación de nuevos equipos o sistemas de energía sin rediseño del casco | Adaptabilidad | Autoridad portuaria |
| R6 | Debe registrar y conservar la información de operación, mantenimiento y materiales | Materiales e información | Mantenimiento, autoridades |
| R7 | Debe facilitar al final de su vida el desmontaje, la reutilización de equipos y el reciclaje de materiales | Retirada y reciclaje | Desguace y reciclaje, autoridades |

## 4.2 Bloques o subsistemas

| ID | Bloque | Funciones principales |
|---|---|---|
| B1 | Casco y cubierta modular | Flotar, soportar cargas, alojar módulos intercambiables |
| B2 | Propulsión y energía | Desplazarse, maniobrar, suministrar energía a bordo |
| B3 | Recogida y almacenamiento de residuos | Captar residuos flotantes, almacenarlos, descargarlos en puerto |
| B4 | Manipulación de carga y boyas | Izar boyas y balizas, cargar equipos, transportar personal |
| B5 | Respuesta a vertidos | Contener y recoger pequeños vertidos (barreras, skimmer) |
| B6 | Navegación, control y comunicaciones | Gobernar, vigilar, comunicar y registrar datos |

## 4.3 Decisiones clave de diseño

Deben ser las mismas en todo el trabajo (apartado 5 del enunciado):

| ID | Decisión inicial | Motivo | Ventaja esperada | Posible consecuencia negativa | Impacto posterior |
|---|---|---|---|---|---|
| D1 | Cubierta con módulos intercambiables (B3, B4, B5) | Varias misiones con un solo barco | Cambiar de misión rápido, modernizar por módulos | Más peso y coste inicial, interfaces a controlar | Partes 8, 9 y 10 |
| D2 | Equipos accesibles y estandarizados | Disponibilidad y mantenimiento sencillo | Menos tiempo de parada, repuestos comunes | Más espacio ocupado, menos optimización | Partes 8 y 9 |
| D3 | Inventario de materiales y registro digital desde la construcción | Trazabilidad durante toda la vida | Mantenimiento informado, desmontaje y reciclaje planificados | Esfuerzo de actualización continuo | Partes 8, 9 y 10 |

# 5. Lo que me falta para cerrar las partes 7–10

- Que el grupo **apruebe o modifique** R1–R7, B1–B6 y D1–D3.
- Las **partes 4 y 5** definitivas, para ajustar los códigos.
- Formato final: **máximo 10 diapositivas de contenido** para todo el trabajo, así que las partes 7–10 deben caber en unas 4 diapositivas, una por parte.
