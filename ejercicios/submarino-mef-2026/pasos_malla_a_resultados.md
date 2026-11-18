# Del modelo mallado a los resultados: paso a paso

**Medio submarino · Femap 2412 · mm, N, MPa**

## Ejes de TU modelo (leídos de `submarino_4_DEN.modfem`)

Tu modelo no usa la orientación del README general. Todo lo que sigue está en **tus** ejes:

| Qué | En tu modelo |
|---|---|
| Eje del submarino | **X**: proa en x = −5000, popa en x = 23500 |
| Hacia **arriba** | **−Y**: la escotilla está en y = −5000 y la brazola llega a y = −5250 |
| Cubierta | Plano **y = +1500**, 1500 mm por debajo del eje |
| Mitad conservada | **z ≥ 0** |
| Plano de simetría | **z = 0** |

Guarda una copia antes de cada paso grande (**File → Save As…**).

---

## Paso 1. Unir las mallas: nodos coincidentes

1. **Tools → Check → Coincident Nodes…** (si no lo encuentras: **Alt+Q** → `coincident`).
2. Selección de nodos: **Select All** → OK.
3. Opciones:
   - **Tolerance: 1** (mm).
   - Acción: **Merge** (fusionar). Si pregunta qué nodo conservar, deja la opción por defecto (el de ID más bajo).
4. OK. En los mensajes debe aparecer cuántos nodos se han fusionado: cientos o miles, de las uniones casco–cubierta, casco–mamparos, cubierta–mamparos y casco–brazola.

## Paso 2. Comprobar que todo está unido: bordes libres

1. Abre **View → Select…** (**F5**). En **Model Style** elige **Free Edge**. OK.
2. Femap dibuja solo los **bordes libres**, es decir, los bordes de elemento que no comparten nada con otro elemento.
3. **Lo que DEBE salir:**
   - el borde del **plano de simetría z = 0**, porque ahí está cortado el modelo;
   - el **borde de los agujeros** de los mamparos (medio círculo en M2 y M3, media elipse en M1);
   - el **borde superior de la brazola**;
   - el **borde de proa de la cubierta** (x = 0).
4. **Lo que NO debe salir**, porque si sale esa unión está suelta:
   - líneas longitudinales en **y = +1500** a lo largo del casco (unión casco–cubierta);
   - los anillos de los mamparos contra el casco (x = 3000, 15000, 21000);
   - la línea de cubierta en cada mamparo;
   - el contorno del agujero de la escotilla, donde se unen casco y brazola.
5. Si alguna unión sale libre, vuelve al paso 1 con **Tolerance = 5**. Si sigue libre, mándame una captura.
6. Vuelve a **F5 → Model Style → Draw Model** para la vista normal.

## Paso 3. Normales de las láminas

Al reflejar superficies, Femap invierte sus normales. Si unos elementos tienen la normal hacia fuera y otros hacia dentro, la presión empujará en sentidos contrarios.

1. **View → Options…** (F6) → categoría **Labels, Entities and Color** → **Element - Directions** → marca **Normal / Shell normal** → OK.
2. Mira el casco: todas las flechas deben apuntar **hacia fuera** (o todas hacia dentro: lo importante es que sean iguales).
3. Para invertir las que estén al revés: **Modify → Update Elements → Reverse…** (o **Normal Direction…**, que alinea todas respecto a un elemento de referencia) y selecciona esos elementos.

## Paso 4. Cuadernas y baos (vigas)

### 4.1 Curvas donde van

| Elemento | x | Curva (medio modelo, z ≥ 0) |
|---|---|---|
| C1 | 0 | Media circunferencia del casco R 5000 (unión esfera–cilindro) |
| C2 | 3000 | Media circunferencia R 5000 (coincide con el M2) |
| C3 | 6000 | Media circunferencia R 5000, **sin** el tramo que cruza la escotilla |
| C4 | 9000 | Media circunferencia R 5000 |
| C5 | 12000 | Media circunferencia R 5000 |
| C6 | 18000 | Media circunferencia del cono R 3750 |
| Baos | 0, 3000, 6000, 9000, 12000, 18000 | Media línea transversal de la cubierta (y = 1500, de z = 0 al casco) |

### 4.2 Mallar las vigas

1. **Mesh → Geometry → Curve…** → selecciona las curvas de las **cuadernas**: todos los trozos de cada media circunferencia → OK.
2. **Property: 5..cuaderna**.
3. **Orientación** (cuadro *Vector Locate – Orientation*). Para un anillo hay que usar una orientación **radial**. Si en **Methods** o en el cuadro aparece **Radial** / *Locate – Radial*, elige como centro un punto del eje: **(x de esa cuaderna, 0, 0)**. Si no aparece, mállalas de una en una con el vector **(0, 0, 1)** y corrige después (paso 4.3).
4. OK. Repite para los **baos** con la misma propiedad y el vector de orientación **(0, 1, 0)**, hacia abajo en tu modelo.

### 4.3 Comprobar que el alma va hacia dentro

1. **View → Options…** → **Element - Orientation/Shape** → **Show Cross Section** (o *Shape*) → OK.
2. Debe verse la T: en las **cuadernas**, el alma hacia el **eje** y el ala en el extremo interior; en los **baos**, el alma hacia **abajo** (+Y) colgando de la cubierta.
3. Si alguna sale al revés o girada: **Modify → Update Elements → Line Element Orientation…** con otro vector, o **Line Element Reverse…**.
4. **Offset:** la T debe colgar de la chapa, no estar centrada en ella. Si en el cuadro de forma (*Shape*) de la propiedad hay **Ref Pt** (punto de referencia), ponlo en el **pie del alma**. Si no, usa **Modify → Update Elements → Line Element Offsets…** con unos **134 mm** hacia el eje (t/2 + distancia del pie del alma al centro de gravedad de la T = 17,5 + 116,3).

Pasa otra vez el **paso 1** (Coincident Nodes, tolerancia 1) para que las vigas compartan nodos con las láminas.

## Paso 5. Cargas

1. **Model → Load → Create/Manage Set…** (Ctrl+F2) → **New** → título `Presion 250 m` → OK.

### 5.1 Presión exterior

2. **Model → Load → On Surface…** → selecciona **todas las superficies del casco** (semiesferas, cilindro, cono) **y la brazola** → OK.
3. Tipo **Pressure**, valor **2,514** (MPa) → OK.
4. Comprueba las flechas: deben apuntar **hacia dentro del casco** y, en la brazola, hacia su eje. Si apuntan hacia fuera, edita la carga con **−2,514** o invierte las normales (paso 3).
5. **Mamparos y cubierta NO llevan presión**: son interiores.

### 5.2 Tapa de la escotilla (borde superior de la brazola)

La tapa cerrada empuja la brazola hacia abajo con p·π·r² = 2,514·π·1000² ≈ 7,90 MN. En medio modelo es la mitad: **3,95 MN**.

6. **Model → Load → On Curve…** → selecciona el **medio borde superior de la brazola** → OK.
7. Tipo **Force**, dirección **+Y** (hacia abajo en tu modelo):
   - si el cuadro pide **fuerza por unidad de longitud** (o tiene una opción de distribuir por longitud): **1257** N/mm;
   - si pide la **fuerza total** sobre la curva: **3 949 000** N.

   Lee bien qué pide: no pongas 1257 como fuerza total ni 3 949 000 por unidad de longitud.

## Paso 6. Apoyos

1. **Model → Constraint → Create/Manage Set…** (Shift+F2) → **New** → `Simetria + isostatico`.

### 6.1 Simetría en z = 0

2. **Model → Constraint → On Curve…** → selecciona **todas las curvas del plano z = 0**: los bordes de corte del casco, mamparos, cubierta y brazola (si llega a z = 0).
3. Marca **TZ, RX y RY**. Deja libres TX, TY y RZ → OK.

### 6.2 Quitar los movimientos de sólido rígido que quedan

4. **Model → Constraint → On Point…** → punto del **polo de proa (−5000, 0, 0)** → marca **TX y TY**.
5. **On Point…** → punto del **polo de popa (23500, 0, 0)** → marca **TY**.

**Cómo comprobarlo después:** las reacciones en los dos polos deben ser **casi cero**. Las reacciones en el plano de simetría sí son grandes, y es normal: representan la mitad que no está modelada.

## Paso 7. Análisis estático lineal (SOL 101)

1. **Model → Analysis…** → **New**.
2. **Analysis Program: NX Nastran** (o Simcenter Nastran). **Type: 1..Static**.
3. En los conjuntos del caso, comprueba que usa la carga `Presion 250 m` y los apoyos `Simetria + isostatico`.
4. En **Output Requests** marca **Displacement**, **SPC Forces**, **Stress** y **Force**.
5. **Analyze**. Al terminar, revisa los mensajes: si sale **FATAL**, cópiamelo. Si salen avisos de *AUTOSPC* o grados de libertad singulares, falta algún apoyo o alguna unión.

## Paso 8. Ver resultados del estático

1. **View → Select…** (F5) → **Deformed and Contour Data…**.
2. **Output Set**: el que acabas de calcular.
3. **Desplazamientos:** *Deform* = **Total Translation**. Pon la escala exagerada, por ejemplo 100×, para ver el «acordeón» entre cuadernas.
4. **Tensiones:** *Contour* = **Plate Top VonMises Stress** y luego **Plate Bot VonMises Stress**.
5. Valores de referencia para comparar:

| Zona | Referencia analítica |
|---|---|
| Cilindro, centro de vano | von Mises ≈ 311 MPa (σθ ≈ 359, σx ≈ 180) |
| Semiesfera de proa | ≈ 180 MPa |
| Cono, base mayor | von Mises ≈ 337 MPa |
| Unión cilindro–cono, escotilla | picos de flexión, por encima de lo anterior |
| Límite elástico HY80 | ≈ 550 MPa |

6. **Cambio dimensional:**
   - **Δ eslora** = desplazamiento **TX** del polo de popa − TX del polo de proa. Referencia: unos −8 mm.
   - **Δ diámetro:** crea un sistema **cilíndrico** con su eje a lo largo de X global (**Model → Coord Sys…**), y muestra el desplazamiento **radial** (*T1* en ese sistema). Referencia: unos 7 mm hacia dentro, Δ diámetro ≈ −14,5 mm, algo menos por las cuadernas.

## Paso 9. Pandeo (SOL 105)

1. **Model → Analysis…** → **New** (o copia el anterior) → **Type: 7..Buckling**.
2. **Number of Eigenvalues / Modes: 20** (Lanczos).
3. Mismos conjuntos de carga y apoyos. **Analyze**.
4. Resultados: cada *Output Set* es un modo, con su **autovalor λ**.
   - **Presión crítica** = λ × 2,514 MPa. **Profundidad crítica** ≈ λ × 250 m.
   - Muestra cada modo con *Deform* = Total Translation para ver **qué** pandea.
5. Qué esperar:

| Modo | λ aproximado |
|---|---|
| Mamparos planos (los primeros, casi seguro) | 0,04 – 0,14 |
| Cono | 0,35 – 0,73 |
| Inestabilidad general del casco | ≈ 0,54 |
| Pandeo entre cuadernas (lóbulos) | ≈ 0,58 |

6. En el informe: el **medio modelo solo da los modos simétricos** respecto a z = 0.

---

Si algún cuadro no coincide con lo descrito, haz una captura con el título visible y lo vemos. Las rutas de menú marcadas como «Alt+Q» o «si no lo encuentras» no se han visto todavía en tus capturas.
