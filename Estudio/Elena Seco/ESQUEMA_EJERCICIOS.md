# Esquema de ejercicios – Elena Seco

(Resumen de 9 casos; usa los datos de los PDFs de `Ejercicios/` y de la presentación «Modalidades de explotación del buque».)

Todos los ejercicios de la asignatura (ContSea, Océana, ejercicio de casa, parcial del 29 oct) son variaciones de **un mismo problema**: calcular qué le cuesta a una naviera operar un buque, y qué contrato le conviene.

## 0. Mapa mental: qué costes asume cada uno

| Modalidad | Cedente soporta | Quien toma soporta | Flete |
|---|---|---|---|
| **Casco desnudo** (arrendamiento) | CAPEX | OPEX (+ VOYEX si explota) | alquiler |
| **Time charter** (T/C) y trip charter | CAPEX + OPEX | VOYEX (combustible, puertos, canales…) | $/día |
| **Voyage charter** (V/C), viajes consecutivos, COA | CAPEX + OPEX + VOYEX | Carga/descarga si es **FIOS** | $/t |
| **Línea regular** (liner terms) | CAPEX + OPEX + VOYEX + carga/descarga | — | $/TEU |

> Regla rápida: **lee el contrato y tacha lo que paga la otra parte.** Los datos que no paga tu protagonista sobran (ej.: costes de carga/descarga en FIOS).

## 1. Vocabulario que hay que distinguir

| Concepto | ¿Es coste (cuenta de explotación)? | ¿Es pago (caja)? |
|---|---|---|
| Amortización | Sí | **No** |
| Intereses | Sí | Sí |
| Devolución de principal | **No** | Sí |
| OPEX, combustible, puertos | Sí | Sí |
| Tonnage tax | Sí | Sí |

- **CAPEX** = amortización + intereses.
- **Pagos de capital** = devolución de principal + intereses.
- **OPEX** = tripulación + técnicos (M+R+P+L) + seguros + administración.
- **VOYEX** = combustible + puertos/canales + comisiones (+ carga/descarga si no es FIOS).

## 2. Los casos tipo y cómo resolverlos

### Caso A – CAPEX y pagos de capital de un año concreto
Ejemplo: parcial 2026 (apartado 1), «Ejercicio CAPEX».

1. **Amortización anual** = precio × (1 − % residual) / años de vida. *(Siempre lineal.)*
2. **Préstamo** = precio × % financiado.
3. **Cuota de principal** (sistema alemán) = préstamo / años de devolución. Con **carencia**: los años de carencia no se devuelve principal y el reparto es entre los años restantes.
4. **Principal pendiente al inicio del año X** = préstamo − (años ya devueltos × cuota).
5. **Intereses del año** = tipo × principal pendiente al inicio.
6. CAPEX = amortización + intereses. Pagos de capital = cuota + intereses.

Comprobación (parcial): 30 M$ × 70 % = 21 M$, cuota 2,1 M$; en 2027 (7.º año desde 2021) quedan 8,4 M$; intereses 504.000 $; amortización 30 M × 0,9 / 20 = 1.350.000 $. CAPEX = 1.854.000 $; pagos = 2.604.000 $.

⚠️ Errores típicos: contar mal el año (¿es el 1.º, el 2.º…?), olvidar el valor residual, sumar la devolución de principal al CAPEX.

### Caso B – OPEX diario o de un periodo
1. Clasifica las partidas (sombrear solo tripulación, técnicos, seguros, administración). **Fuera:** combustible, puertos, canales, comisiones, ingresos.
2. Suma y aplica el incremento (`× 1,0x`).
3. Divide entre **350** (días operativos) para el coste por día. Si es un contrato de 30 días: 30 × OPEX/día.
4. Si el enunciado da OPEX diario sobre base 365, multiplica por 365 para el total anual.

### Caso C – Duración de un contrato y costes de viaje (VOYEX)
Tabla fija de cinco filas:

| Concepto | Fórmula |
|---|---|
| Navegación en carga | n.º viajes × millas / nudos_carga / 24 |
| Navegación en lastre | **(n − 1)** × millas / nudos_lastre / 24 |
| Puerto de carga | n × días por escala |
| Puerto de descarga | n × días por escala |
| **Total** | suma (en el parcial salía ≈ 350 días) |

> El último viaje termina tras la última descarga: **no hay retorno final** (n viajes con carga, n − 1 en lastre).

**Combustible**: consumo (t/día) × días × precio.
- Navegación: días de navegación en carga + en lastre. Si hay fuel y auxiliares (gasoil), calcula cada uno.
- Puerto: días de puerto × consumo en puerto (MGO/gasoil).

**Puertos**: nº escalas × (tasa y servicios al buque). Los costes de carga/descarga ($/t) **solo si no es FIOS**.

### Caso D – Comparar T/C frente a V/C (TCE)
1. **T/C neto por día** = flete bruto × (1 − comisión) (÷ días si te dan el total). Ojo: si el enunciado da el neto, bruto = neto / (1 − comisión).
2. **V/C**: ingresos brutos = n × carga × flete ($/t); netos = brutos × (1 − comisión).
3. **TCE** = (ingresos netos − combustible − puertos [− ETS]) / días del contrato.
4. Compara T/C neto por día con TCE. La opción con mayor valor conviene.


### Caso E – Resultado de explotación con time charter
```
Ingresos netos (flete × días operativos × (1 − comisión))
− OPEX
− Amortización
= Resultado de explotación (EBIT)
− Intereses
− Impuesto (tonnage tax, cifra fija)
= Resultado después de intereses e impuestos
```
(Con T/C el fletador paga combustible, puertos y ETS, así que el fletante no los resta.)

### Caso F – Línea regular: coste por TEU (ContSea)
Se pide «a cuánto cobrar el TEU para cubrir costes». Pasos:
1. **Con buque en T/C**: flete T/C bruto = neto / (1 − comisión); 6 meses = 180 días (30 d/mes).
2. Combustible: días navegación (viajes × 2 × millas / nudos / 24) y días en puerto (viajes × 2 escalas × días/escala).
3. Manipulación (liner terms): TEU transportados × 2 movimientos × €/TEU mov.
4. Tasas y servicios: escalas × €/escala.
5. Administración y tonnage tax prorrateados al periodo.
6. Convierte divisas (€/$).
7. **Coste/TEU** = suma / TEU transportados (viajes × 2 sentidos × TEU/sentido).
8. **Con buque propio**: sustituye el flete T/C por **CAPEX + OPEX del periodo** (año / 2 para un semestre).

### Caso G – Flete mínimo para cubrir todos los costes (ejercicio de casa)
1. Para **cada año** calcula: CAPEX_año + OPEX + costes de viaje + impuestos. (El CAPEX cambia entre años por los intereses: no lo multipliques por 3.)
2. Suma los 3 años y divide por las t totales → **flete neto** ($/t).
3. **Flete bruto** = neto / (1 − comisión). *(En clase se aceptó ×1,025; revisa qué pide el enunciado.)*
4. **Tesorería por año** = ingresos − pagos de capital − OPEX − costes de viaje − impuestos.
5. **Fondos mínimos iniciales** = pago inicial (fondos propios = % no financiado × precio) + déficit máximo acumulado de tesorería, si lo hay.

### Caso H – Alquiler a casco desnudo que cubre los pagos
Suma de los pagos de capital del año (devolución de principal + intereses) o CAPEX según pida «costes» o «pagos». Si la pregunta es «cubrir todos sus pagos de capital»: pagos de capital del año.

### Caso I – Contrato de transporte (COA) con margen, tesorería y T/C (ejercicio HLB de clase)
Tiene tres preguntas encadenadas; no empieces a calcular antes de decidir **qué piden, qué datos usa cada bloque y cuáles son trampa**.

1. **Flete bruto del COA con margen del 10 %** sobre el coste de hacerlo con buque propio:
   - Duración del contrato (Caso C): ej. 6 × 14 + 5 × 13 + 48 = 197 días.
   - Costes fijos **por día** (anuales / 350) × días del contrato: CAPEX + (OPEX + tonnage tax).
   - + costes de viaje (combustible + puertos).
   - Total × 1,10 = ingresos netos necesarios → ÷ t transportadas = flete neto → ÷ (1 − comisión) = flete bruto.
2. **Margen de tesorería**: igual, pero sustituye el CAPEX por los **pagos de capital** (principal + intereses). Margen = ingresos netos − pagos totales. Un margen económico del 10 % no garantiza caja positiva.
3. **Tomar otro buque en T/C para cumplir el COA**: ya no hay CAPEX ni OPEX propios. Máximo T/C bruto por día = (ingreso neto del COA − tonnage tax − costes de viaje) / días del contrato. Si piden el neto: bruto × (1 − comisión).

**OPEX en este ejercicio** (ejemplo de «trampas»): sí entran P&I, seguridad social y salarios de tripulación, administración, mantenimiento, pertrechos, lubricantes y seguro de casco. **No entran**: mercaderías, comisiones, anticipos, ingresos por demoras, combustible a bordo, servicios de carga y descarga.

### Neto, bruto y comisión – tres variantes
| Redacción | Cálculo |
|---|---|
| «Flete bruto 18.000 $/día; el bróker cobra 2,5 % **sobre el bruto**» | neto = 18.000 × (1 − 0,025) |
| «Necesito 20 $/t **netos**; comisión 3 % sobre el bruto» | bruto = 20 / 0,97 |
| «Pago 15.000 $/día **y además** una comisión del 4 % sobre esos 15.000» | total = 15.000 × (1 + 0,04) |

## 3. Con EU ETS (parcial 2026)
1. **t de combustible** de la ruta: navegación (VLSFO) y puerto (MGO).
2. Emisiones ETS: **50 %** del CO₂ de la navegación UE ↔ tercer país + **100 %** del CO₂ en escalas en puertos de la UE. Las escalas en terceros países no cuentan.
3. t CO₂ = t combustible × factor de emisión (VLSFO 3,151; MGO 3,206) × % aplicable.
4. Coste = t CO₂ × €/t × tipo de cambio ($/€).
5. TCE con ETS = (netos − combustible − puertos − ETS) / días.
En el parcial: 17.130,80 $/día sin ETS → 14.266,14 $/día con ETS; el T/C neto era 16.087,50 → conviene A.

## 4. Lista de comprobación antes de entregar
- [ ] ¿Usé 350 días o 365 según lo que pide?
- [ ] ¿Pasé comisión de neto a bruto con `/(1 − c)`?
- [ ] ¿Nº de viajes en lastre = n − 1?
- [ ] ¿Descarté los datos que no paga mi protagonista (FIOS, T/C)?
- [ ] ¿Amortización con valor residual y sin sumar el principal al CAPEX?
- [ ] ¿Moneda unificada ($ o €)?
- [ ] ¿Escribí la conclusión (qué opción conviene)?

## 5. Mapa de ejercicios del repo

| Ejercicio | Casos | Dónde |
|---|---|---|
| Parcial 29 oct 2026 | A, E, D, ETS | `Ejercicios/Enunciados` + `Soluciones/…EXAMEN-SOLUCIÓN2` |
| Ejercicio casa oct 2026 | A, G | `Soluciones/…casa -oct 2026…` |
| Repaso 1 (ContSea) | F | `Soluciones/…repaso 1…` |
| Repaso 2 (Océana) | A, C, D, H | `Soluciones/…repaso 2…` |
| Clase sep 2026 (HLB, COA; y repaso Océana) | A, B, C, D, G, I | `Soluciones/…clase - sep 2026…` |
