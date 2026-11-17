---
title: "9. MODERNIZACIÓN Y EXTENSIÓN DE VIDA"
subtitle: "Proyecto fin de curso IINT · Embarcación multipropósito portuaria · Borrador del apartado 9"
---

***Cambio propuesto***

Diez años después de su entrada en servicio, la autoridad portuaria quiere **reducir las emisiones durante las operaciones interiores** y **mejorar la detección de residuos flotantes**. Para ello se plantea:

- Una **propulsión híbrida** con baterías, que permita navegar en modo eléctrico dentro de las dársenas y recargar en el muelle.
- Un **sistema de detección de residuos** mediante cámaras y sensores que localicen los residuos e indiquen al puente hacia dónde dirigirse.

***Funciones y bloques afectados***

- **Propulsión (B):** se añaden baterías y motores eléctricos junto a los motores principales. Se ve afectada la función *navegar y maniobrar en aguas portuarias*.
- **Control y comunicaciones (E):** debe gestionar la energía del sistema híbrido e integrar los nuevos sensores de detección.
- **Gestión de residuos y vertidos (C):** la función *recoger residuos flotantes* pasa a estar guiada por el sistema de detección.
- **Estructural (A):** debe alojar el peso y el espacio de las baterías y las bases de las nuevas cámaras y sensores.
- **Elevación y manejo de cargas (D):** no se ve afectado.

***Interfaces que habría que revisar***

- **Estructural – Propulsión (M):** peso, espacio y ventilación de las baterías en la cámara de máquinas.
- **Propulsión – Control (I):** nuevas señales de estado de carga de las baterías y de gestión de la energía.
- **Gestión de residuos – Control (I):** los datos del sistema de detección se suman a los de los sensores de nivel.
- **Nueva interfaz de energía:** la matriz DSM del apartado 5 solo distingue interfaces de material (M) e información (I). Con la propulsión híbrida aparece un intercambio de **energía eléctrica** entre propulsión, control y el resto de equipos, que habría que añadir.
- **Nueva interfaz externa con las instalaciones portuarias:** el punto de recarga en el muelle.

***Decisiones iniciales que facilitan o dificultan el cambio***

Facilitan el cambio:

- El **aislamiento de los subsistemas** (apartado 5) permite modificar la propulsión y añadir sensores sin rediseñar el casco ni los módulos de residuos y cargas.
- La **centralización de la información** en el subsistema de control permite conectar los nuevos sensores en un único punto.
- Los **anclajes estandarizados** de cubierta (RA1) y los **componentes ISO/DIN** (RM2) facilitan instalar nuevos equipos.
- El **espacio libre alrededor de los motores** (RM1) facilita el trabajo en la cámara de máquinas durante la modernización.

Dificultan el cambio:

- **No se reservó espacio, peso ni potencia eléctrica** para futuras modificaciones. Las baterías deben encajar en la cámara de máquinas existente, ya que en el apartado 5 se decidió mantener la posición de los motores principales.
- La centralización de la información convierte al subsistema de control en un **punto único de fallo** (apartado 8) y lo carga con más funciones. Se aprovecha la modernización para añadir el mando local de emergencia propuesto en el apartado 8.

***Qué debería actualizarse***

- **Requisitos:** añadir un requisito de operación sin emisiones en las dársenas y otro de detección de residuos, y revisar los afectados por el nuevo peso, como el radio de giro (RO1).
- **Pruebas:** repetir la verificación de los subsistemas modificados siguiendo el Modelo en V (FAT de baterías y sensores, pruebas de integración en puerto y pruebas de mar), comprobar que los requisitos ya cumplidos siguen cumpliéndose (RO1, RI1) y repetir la jornada piloto de validación con la tripulación.
- **Documentación:** actualizar la línea base *As Built*, los manuales, los SOPs (incluida la recarga en el muelle), el plan de mantenimiento y el inventario de materiales con las baterías, que tendrán una gestión específica al final de su vida (apartado 10).
- **Formación:** la tripulación, en el modo eléctrico, la recarga y el nuevo sistema de detección; el personal de mantenimiento, en los equipos eléctricos y las baterías.

***¿Permite extender la vida útil?***

Sí, siempre que el historial de mantenimiento y las inspecciones en varada (apartado 8) confirmen que el **casco de aluminio** y la estructura se encuentran en buen estado. La modernización actualiza los subsistemas que más envejecen (propulsión y electrónica) y adapta la embarcación a las nuevas exigencias ambientales, por lo que permitiría mantenerla en servicio más años con un coste menor que el de construir una embarcación nueva.
