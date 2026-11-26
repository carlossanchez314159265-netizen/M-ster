# Ejercicio propio 2 · Naviera del Levante (con ETS)

Ejercicio original, no de examen. Casos A, B, C, I y EU ETS del esquema de ejercicios. Las trampas son distintas de las del ejercicio propio 1.

## Enunciado

A 1 de enero de 2025, Naviera del Levante S.A. opera el **Levante**, un granelero Handymax de **45.000 t** de capacidad de carga útil, que compró nuevo en **enero de 2021** por **32.000.000 $**. Financió el **65 %** con un préstamo al **7 %**, sistema alemán, a devolver en **10 años tras 1 de carencia**. El resto lo pagó con fondos propios.

El buque se amortiza linealmente en **25 años** con un valor residual del **10 %**.

De la contabilidad de 2024 se han extraído estas partidas ($/año). La naviera estima que sus **costes fijos de explotación** aumentarán un **4 %** en 2025:

| Concepto | $/año |
|---|---|
| Salarios de la tripulación | 1.050.000 |
| Derechos de emisión EU ETS entregados | 410.000 |
| Seguridad social de la tripulación | 240.000 |
| Devolución de principal del préstamo | 2.080.000 |
| Seguro de P&I | 150.000 |
| Ingresos por demoras | 95.000 |
| Seguro de casco y máquinas | 190.000 |
| Combustible consumido | 2.900.000 |
| Mantenimiento y reparaciones | 360.000 |
| Tasas y servicios portuarios | 720.000 |
| Pertrechos y respetos | 90.000 |
| Comisiones de fletamento | 140.000 |
| Lubricantes | 110.000 |
| Costes de estiba y desestiba | 310.000 |
| Administración y gestión técnica | 160.000 |

La naviera tributa por **tonnage tax**: 14.000 $/año. El buque está **operativo 350 días** al año.

La naviera ha firmado un **contrato de transporte (COA)** que empieza el 1 de marzo de 2025: **8 cargamentos de 43.000 t** de cereal entre **Gdańsk (Polonia)** y **Huelva (España)**, que distan **2.300 millas**. El contrato termina con la última descarga. Condiciones **FIOS**. Comisión del bróker: **2,5 %** sobre el flete bruto.

Datos del buque y de la ruta:
- Velocidad: **12 nudos en carga** y **13 en lastre**.
- Consumo en navegación: **22 t/día de VLSFO a 600 $/t**. En puerto: **2,5 t/día de MGO a 800 $/t**.
- Estancia en puerto: **3 días en Gdańsk** (carga) y **4 días en Huelva** (descarga).
- Tasas y servicios al buque: **45.000 €/escala en Gdańsk** y **50.000 €/escala en Huelva**.
- Costes de carga: 3 $/t; de descarga: 4 $/t.

Datos del EU ETS para 2025:
- Se entregan derechos por el **70 %** de las emisiones verificadas comprendidas en su ámbito.
- Factores de emisión: VLSFO 3,151 t CO₂/t; MGO 3,206 t CO₂/t. Considere solo el CO₂.
- Precio del derecho (EUA): **75 €/t CO₂**.
- Tipo de cambio: **1,10 $/€**.

**Se pide:**

1. CAPEX y pagos de capital del buque en 2025.
2. Duración del COA, costes de viaje y coste del EU ETS.
3. Flete bruto ($/t) que debe cobrar para obtener un **margen del 8 %** sobre los costes que tendría durante el contrato con su propio buque.
4. Con ese flete, ¿qué margen de tesorería genera el contrato?
5. Si en lugar de usar el Levante tomase otro buque similar en time charter para servir el COA, ¿qué flete T/C bruto máximo diario podría pagar para que el COA cubriese todos sus desembolsos?

---

## Solución

<details><summary>1. CAPEX y pagos de capital</summary>

- Préstamo = 0,65 × 32.000.000 = **20.800.000 $**
- Cuota de principal = 20.800.000 / 10 = **2.080.000 $**
- Años: 2021 (carencia), 2022 (1.ª cuota), 2023 (2.ª), 2024 (3.ª), **2025 (4.ª cuota)**
- Principal pendiente a 1-1-2025 = 20.800.000 − 3 × 2.080.000 = **14.560.000 $**
- Intereses 2025 = 0,07 × 14.560.000 = **1.019.200 $**
- Amortización = 32.000.000 × 0,90 / 25 = **1.152.000 $**

| | $ |
|---|---|
| **CAPEX** = amortización + intereses | **2.171.200** |
| **Pagos de capital** = principal + intereses | **3.099.200** |

⚠️ Trampa: con la carencia, en 2025 solo se han pagado 3 cuotas, no 4.

</details>

<details><summary>2. Duración, costes de viaje y EU ETS</summary>

**Duración**

| Concepto | Cálculo | Días |
|---|---|---|
| Navegación en carga | 8 × 2.300 / 12 / 24 | 63,89 |
| Navegación en lastre | **7** × 2.300 / 13 / 24 | 51,60 |
| Puerto de carga (Gdańsk) | 8 × 3 | 24 |
| Puerto de descarga (Huelva) | 8 × 4 | 32 |
| **Total** | | **171,49** |

**Combustible**

- VLSFO = (63,89 + 51,60) × 22 = 2.540,81 t × 600 = **1.524.487 $**
- MGO = (24 + 32) × 2,5 = 140 t × 800 = **112.000 $**

**Puertos**: 8 × (45.000 + 50.000) = 760.000 € × 1,10 = **836.000 $**

Carga y descarga: **0** (FIOS)

**EU ETS**. Gdańsk y Huelva son puertos de la UE, así que todo cuenta al 100 %: la navegación en carga y en lastre (UE ↔ UE) y las escalas en los dos puertos.

| | t combustible | Factor | t CO₂ |
|---|---|---|---|
| VLSFO (navegación, 100 %) | 2.540,81 | 3,151 | 8.006,10 |
| MGO (los dos puertos, 100 %) | 140 | 3,206 | 448,84 |
| **Total emisiones** | | | **8.454,94** |
| Derechos a entregar en 2025 (70 %) | | | **5.918,46** |

Coste ETS = 5.918,46 × 75 € × 1,10 = **488.273 $**

**Costes de viaje totales** = 1.524.487 + 112.000 + 836.000 + 488.273 = **2.960.760 $**

⚠️ Trampas:
- No es como el parcial (Argentina ↔ UE, al 50 %). Aquí es UE ↔ UE: la navegación cuenta al 100 % y las escalas en los dos puertos también.
- En 2025 se entregan derechos solo por el 70 %.

</details>

<details><summary>3. Flete bruto con margen del 8 %</summary>

**OPEX 2025**: salarios, seguridad social, P&I, casco y máquinas, mantenimiento, pertrechos, lubricantes y administración.

1.050.000 + 240.000 + 150.000 + 190.000 + 360.000 + 90.000 + 110.000 + 160.000 = 2.350.000 × 1,04 = **2.444.000 $**

⚠️ Fuera: derechos ETS (son coste de viaje), devolución de principal (no es coste), ingresos por demoras, combustible, tasas portuarias, comisiones, estiba y desestiba.

**Costes fijos prorrateados a los días del contrato** (anual / 350 × 171,49):

| | Anual | Por día | 171,49 días |
|---|---|---|---|
| CAPEX | 2.171.200 | 6.203,43 | 1.063.835 |
| OPEX + tonnage tax | 2.458.000 | 7.022,86 | 1.204.360 |

| | $ |
|---|---|
| CAPEX del contrato | 1.063.835 |
| OPEX + TT del contrato | 1.204.360 |
| Costes de viaje (con ETS) | 2.960.760 |
| **Coste total** | **5.228.955** |
| × 1,08 = **ingresos netos necesarios** | **5.647.271** |

- Toneladas = 8 × 43.000 = 344.000 t
- Flete neto = 5.647.271 / 344.000 = **16,42 $/t**
- **Flete bruto** = 16,42 / 0,975 = **16,84 $/t**

</details>

<details><summary>4. Margen de tesorería</summary>

Igual que el apartado 3, pero cambiando **CAPEX por pagos de capital**:

| | $ |
|---|---|
| Pagos de capital: 3.099.200 / 350 × 171,49 | 1.518.532 |
| OPEX + TT | 1.204.360 |
| Costes de viaje | 2.960.760 |
| **Total pagos** | **5.683.652** |
| Ingresos netos | 5.647.271 |
| **Margen de tesorería** | **−36.381 $ (negativo)** |

Aunque gana un 8 % sobre costes, **el contrato no genera caja**. La devolución de principal (2.080.000 $/año) es mayor que la amortización (1.152.000 $/año).

</details>

<details><summary>5. Time charter máximo</summary>

Con un buque en T/C la naviera ya no soporta CAPEX ni OPEX propios. Sigue pagando el tonnage tax y los costes de viaje, ETS incluido, porque el ETS lo paga quien opera el buque.

- Tonnage tax del contrato = 14.000 / 350 × 171,49 = 6.860 $
- Disponible para el T/C = 5.647.271 − 6.860 − 2.960.760 = **2.679.651 $**
- **T/C bruto máximo** = 2.679.651 / 171,49 = **15.625,57 $/día**
- (Si pidieran el neto que recibe el armador: 15.625,57 × 0,975 = 15.234,93 $/día)

</details>

### Qué pasa si caes en cada trampa (flete bruto del apartado 3)

| Error | Flete bruto que sale |
|---|---|
| **Correcto** | **16,84 $/t** |
| Restar carga y descarga (FIOS) | 24,59 $/t |
| 8 tramos en lastre en vez de 7 | 17,56 $/t |
| ETS al 100 % en vez del 70 % | 17,51 $/t |
| Navegación ETS al 50 % (como si fuera un tercer país) | 16,09 $/t |
| No convertir los € de puertos a $ | 16,59 $/t |
| Prorratear entre 365 días en vez de 350 | 16,54 $/t |
