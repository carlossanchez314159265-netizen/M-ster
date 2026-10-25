"""Añade los exámenes resueltos de examenes/ al final del compendio de ejercicios.

Uso: python3 unir_anexo.py compendio.pdf salida.pdf
"""
import sys, os
from pypdf import PdfReader, PdfWriter

HERE = os.path.dirname(os.path.abspath(__file__))
EXAMENES = os.path.join(HERE, "..", "..", "examenes")
ANEXOS = [
    ("Anexo 1 · Examen 1er Parcial 29-10-2025 (resuelto)", "Examen 1er Parcial 29-10-2025 (resuelto).pdf"),
    ("Anexo 2 · Examen Final ordinario 1er Parcial 13-01-2025 (resuelto)", "Examen Final ordinario 1er Parcial 13-01-2025 (resuelto).pdf"),
]

src, out = sys.argv[1], sys.argv[2]
w = PdfWriter()
w.append(src)
for titulo, fichero in ANEXOS:
    start = len(w.pages)
    w.append(os.path.join(EXAMENES, fichero))
    w.add_outline_item(titulo, start)
w.add_metadata({"/Title": "Oceanografía — Ejercicios resueltos del 1er parcial", "/Author": "Carlos Sánchez Campos"})
with open(out, "wb") as f:
    w.write(f)
print("ok", out, len(w.pages), "páginas")
