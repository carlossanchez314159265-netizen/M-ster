# Femap: chuleta para la clase

**Femap Student · Sistema internacional: m, N, Pa, kg, s.**

Guía completa: [placas, cilindros y conos](guia-femap-placas-y-laminas.md). Las rutas de menú son orientativas; confirma nombres en la ayuda de tu versión.

## Orden de trabajo

**Geometría → material → propiedad/espesor → malla → apoyos → cargas → análisis → resultados → comprobación.**

| Quiero… | Qué buscar / hacer |
|---|---|
| Crear una placa | Puntos → líneas de contorno → superficie por curvas cerradas |
| Crear un cilindro | Línea de `(R,0,0)` a `(R,0,L)` → superficie por revolución 360° alrededor de Z |
| Crear un tronco de cono | Línea de `(R1,0,0)` a `(R2,0,H)` → revolución 360° alrededor de Z |
| Dar material | Model → Material; acero de ejemplo: E = 2.10e11 Pa, ν = 0.3 |
| Dar espesor | Model → Property → Plate/Shell → material y Thickness en m (10 mm → 0.01 m) |
| Crear malla | Mesh Control → Size On Surface/Curve; después Mesh → Geometry → Surface |
| Afinar malla | Cambiar tamaño y remallar; revisar de nuevo cargas, apoyos y conectividad |
| Empotrar borde shell | Constraint Set; restringir TX, TY, TZ, RX, RY, RZ del borde |
| Apoyar simplemente placa XY | TZ en los bordes apoyados; A: TX+TY; B sobre X desde A: TY; giros libres |
| Poner rodillo | Impedir sólo desplazamiento normal al plano de apoyo; estabilizar lo que falte |
| Poner presión | Load Set → carga sobre superficie/elementos → Pressure; comprobar flechas y normales |
| Poner fuerza puntual | Carga nodal; comprobar si el valor es por nodo o total |
| Poner peso propio | Densidad coherente + Gravity/Acceleration; g = 9.81 m/s² |
| Resolver | Model → Analysis; Linear Static/SOL 101; asignar cargas y apoyos; pedir salidas |
| Ver flecha | Output Set correcto → deformada + desplazamiento Z para placa XY |
| Ver esfuerzos shell | Membrane Force, Bending Moment y Transverse Shear; comprobar ejes |
| Encontrar extremos | Data Table/listado → ordenar máximo y mínimo → localizar ID |
| Obtener esfuerzo total de corte | Freebody/Section Cut; integrar en ejes comunes y comprobar equilibrio |

## Unidades SI: m–N–Pa–kg–s

- Geometría en **m**: un lado de 1000 mm se introduce como **1**; un espesor de 10 mm, como **0.01**.
- Presión y tensión: **Pa = N/m²**. 1 MPa = 1000000 Pa.
- Young de acero de ejemplo: **2.10e11 Pa**; densidad: **7850 kg/m³**.
- Esfuerzos shell $N_x,N_y,N_{xy},Q_x,Q_y$: **N/m**.
- Momentos shell $M_x,M_y,M_{xy}$: **N·m/m**, por unidad de longitud.
- Fuerzas de viga: **N**. Momentos de viga: **N·m**.
- Consulta el límite de nodos/elementos de tu edición Student antes de refinar.

## Cinco comprobaciones antes de entregar

1. ¿El caso utiliza mis cargas y apoyos actuales?
2. ¿La deformada tiene sentido y conozco su escala?
3. ¿Las reacciones equilibran fuerzas y momentos aplicados?
4. ¿Sé las unidades, ejes, cara y ubicación de cada máximo y mínimo?
5. ¿Los resultados relevantes se estabilizan al refinar la malla?

**Recuerda:** bloquear radialmente un cilindro requiere direcciones nodales cilíndricas correctas; activar un sistema para dibujar no basta. En un cono, radial no es normal a la pared. La costura de una lámina cerrada debe estar conectada. Un pico singular puede crecer al refinar y no ser un esfuerzo de diseño utilizable.
