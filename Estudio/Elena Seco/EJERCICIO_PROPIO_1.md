# Ejercicio propio 1 · Naviera Cantábrica (con trampas)

Ejercicio original, no de examen. Casos A, B, C, D, E y H del [esquema](ESQUEMA_EJERCICIOS.md).

## Enunciado

A 1 de enero de 2026, Naviera Cantábrica S.A. explota el **Cantábrico**, un granelero Supramax de 58.000 tpm y **55.000 t** de capacidad de carga útil, que compró nuevo en **enero de 2022** por **28.000.000 $**. Financió el **75 %** con un préstamo al **6 %**, sistema alemán, a devolver en **8 años tras 2 de carencia**. El resto lo pagó con fondos propios.

El buque se amortiza linealmente en **20 años** con un valor residual del **12 %**.

De la contabilidad de 2025 se han extraído estas partidas ($/año). La naviera estima que sus **costes fijos de explotación** aumentarán un **3 %** en 2026:

| Concepto | $/año |
|---|---|
| Salarios de la tripulación | 1.150.000 |
| Ingresos por fletes | 9.800.000 |
| Seguridad social de la tripulación | 290.000 |
| Amortización del buque | 1.232.000 |
| Seguro de casco y máquinas | 210.000 |
| Combustible consumido | 2.400.000 |
| Seguro de P&I | 160.000 |
| Intereses del préstamo | 1.010.000 |
| Mantenimiento y reparaciones | 380.000 |
| Tasas portuarias | 610.000 |
| Pertrechos y respetos | 120.000 |
| Comisiones de bróker | 180.000 |
| Lubricantes | 140.000 |
| Costes de estiba y desestiba | 350.000 |
| Administración y gestión técnica | 150.000 |

La naviera tributa por **tonnage tax**: 12.000 $/año. El buque estará **operativo 350 días** al año.

Velocidades: **13,5 nudos en carga** y **14,5 en lastre**. Consumo en navegación: **24 t/día de VLSFO a 560 $/t**. En puerto: **3 t/día de MGO a 780 $/t**.

Para 2026 tiene dos ofertas:

- **Opción A – Time charter de 12 meses** a **15.800 $/día**. El armador pagará sobre esa cifra una **comisión total del 3,75 %** (address commission + bróker).
- **Opción B – Viajes consecutivos en condiciones FIOS**: **7 cargamentos de 52.000 t** de grano entre dos puertos que distan **4.200 millas**, a **19 $/t**, con una comisión del **2,5 %**. El contrato termina con la última descarga.
  - Estancia en puerto: 4 días en carga y 5 en descarga.
  - Tasas y servicios al buque: **65.000 $/escala** en el puerto de carga y **60.000 €/escala** en el de descarga.
  - Costes de carga: 3,5 $/t; de descarga: 4 $/t.

Tipo de cambio: **1,10 $/€**.

**Se pide:**

1. CAPEX y pagos de capital del buque en 2026.
2. OPEX de 2026 y resultado después de intereses e impuestos si acepta la opción A.
3. Duración de la opción B, sus costes de viaje y su TCE. ¿Qué opción le conviene?
4. Si en lugar de fletarlo lo arrendase a casco desnudo, ¿qué alquiler anual mínimo debería pedir en 2026 para cubrir todos sus pagos de capital?

---

## Solución

<details><summary>1. CAPEX y pagos de capital</summary>

- Préstamo = 0,75 × 28.000.000 = **21.000.000 $**
- Cuota de principal = 21.000.000 / 8 = **2.625.000 $**
- Años: 2022 (1.º, carencia), 2023 (2.º, carencia), 2024 (1.ª cuota), 2025 (2.ª cuota), **2026 (3.ª cuota)**
- Principal pendiente a 1-1-2026 = 21.000.000 − 2 × 2.625.000 = **15.750.000 $**
- Intereses 2026 = 0,06 × 15.750.000 = **945.000 $**
- Amortización = 28.000.000 × 0,88 / 20 = **1.232.000 $**

| | $ |
|---|---|
| **CAPEX** = amortización + intereses | **2.177.000** |
| **Pagos de capital** = principal + intereses | **3.570.000** |

⚠️ Trampa: los intereses de la tabla (1.010.000) son de 2025. Hay que recalcularlos para 2026.

</details>

<details><summary>2. OPEX y resultado con time charter</summary>

**OPEX**: solo salarios, seguridad social, casco y máquinas, P&I, mantenimiento, pertrechos, lubricantes y administración.

1.150.000 + 290.000 + 210.000 + 160.000 + 380.000 + 120.000 + 140.000 + 150.000 = 2.600.000 × 1,03 = **2.678.000 $**

⚠️ Fuera: ingresos por fletes, amortización e intereses (son CAPEX), combustible y tasas portuarias (VOYEX), comisiones, estiba y desestiba.

**Cuenta de explotación con T/C** (el fletador paga combustible y puertos):

| | $ |
|---|---|
| Ingresos netos = 15.800 × 350 × (1 − 0,0375) | 5.322.625 |
| − OPEX | −2.678.000 |
| − Amortización | −1.232.000 |
| **Resultado de explotación** | **1.412.625** |
| − Intereses | −945.000 |
| − Tonnage tax | −12.000 |
| **Resultado después de intereses e impuestos** | **455.625** |

⚠️ Trampa: 350 días, no 365 (los 15 restantes está off-hire y no cobra).

</details>

<details><summary>3. Opción B: duración, costes de viaje y TCE</summary>

**Duración**

| Concepto | Cálculo | Días |
|---|---|---|
| Navegación en carga | 7 × 4.200 / 13,5 / 24 | 90,74 |
| Navegación en lastre | **6** × 4.200 / 14,5 / 24 | 72,41 |
| Puerto de carga | 7 × 4 | 28 |
| Puerto de descarga | 7 × 5 | 35 |
| **Total** | | **226,15** |

**Ingresos**
- Brutos = 7 × **52.000** × 19 = 6.916.000 $
- Netos = 6.916.000 × 0,975 = **6.743.100 $**

**Costes de viaje**
- VLSFO = (90,74 + 72,41) × 24 × 560 = **2.192.797 $**
- MGO = 63 × 3 × 780 = **147.420 $**
- Puertos = 7 × (65.000 + 60.000 × 1,10) = 7 × 131.000 = **917.000 $**
- Carga y descarga: **0** (FIOS)

**TCE** = (6.743.100 − 2.192.797 − 147.420 − 917.000) / 226,15 = **15.413,72 $/día**

**Comparación**: T/C neto = 15.800 × (1 − 0,0375) = **15.207,50 $/día**

**Conviene la opción B (viajes consecutivos)**, por unos 206 $/día.

⚠️ Cada trampa cambia la decisión o el resultado:

| Error | TCE que sale | Decisión |
|---|---|---|
| Comparar con el T/C **bruto** (15.800) | 15.413,72 | A (mal) |
| Restar carga y descarga (FIOS) | 3.342,33 | A (mal) |
| 7 tramos en lastre en vez de 6 | 13.951,92 | A (mal) |
| Usar 55.000 t (capacidad) en vez de 52.000 | 17.133,90 | B, pero con el TCE mal |
| No convertir los 60.000 € a $ | 15.599,44 | B, pero con el TCE mal |

</details>

<details><summary>4. Casco desnudo</summary>

Pide cubrir los **pagos de capital** (no el CAPEX): **3.570.000 $/año** (2.625.000 de principal + 945.000 de intereses).

⚠️ Trampa: si pones el CAPEX (2.177.000) cubres los costes, pero no la devolución del préstamo.

</details>
