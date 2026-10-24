# Generadores de los resúmenes en PDF

Scripts (Python + ReportLab) que generan los resúmenes de `*/resumenes/`. Todos comparten `estilo.py`.

- `terms([...])` añade debajo de cada ecuación la leyenda **Términos** (símbolo → significado y unidades). Toda ecuación nueva debe llevar la suya.
- `figuras.py` dibuja la figura de η (superficie libre) del Día 2.

Uso: `python3 dia2.py "../../02-mecanica-de-ondas/resumenes/Resumen Dia 2 - Mecanica de ondas.pdf"`

Los PDF de `examenes/` se generan con `scripts/examenes/` (reutilizan este `estilo.py`):
`cd scripts/examenes && python3 parcial_29-10-2025.py "../../examenes/Examen 1er Parcial 29-10-2025 (resuelto).pdf"` (ídem `final_13-01-2025.py` y `analisis_estructura.py`).
