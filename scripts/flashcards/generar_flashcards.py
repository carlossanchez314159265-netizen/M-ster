# -*- coding: utf-8 -*-
"""Genera las flashcards en Markdown (formato de la rama iint) y TSV para Anki.

- Días 1, 2 y 3: lee las tarjetas de los .apkg ya existentes, así son exactamente las mismas.
- Día 4 (espectral) y examen: tarjetas de nuevas_tarjetas.py; además genera su .apkg.

Uso (desde la raíz del repo):  python scripts/flashcards/generar_flashcards.py
"""
import os
import re
import sqlite3
import sys
import tempfile
import zipfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from nuevas_tarjetas import DIA4_ESPECTRAL, EXAMEN  # noqa: E402

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

INSTRUCCIONES = ("Intenta responder antes de desplegar la solución. Marca las falladas para el "
                 "último repaso. Son las mismas tarjetas del archivo de Anki")


def leer_apkg(ruta):
    with tempfile.TemporaryDirectory() as d:
        with zipfile.ZipFile(ruta) as z:
            z.extract("collection.anki2", d)
        con = sqlite3.connect(os.path.join(d, "collection.anki2"))
        filas = con.execute("select flds from notes order by id").fetchall()
        con.close()
    return [tuple(f[0].split("\x1f")[:2]) + ("",) for f in filas]


def a_markdown(html):
    s = re.sub(r"</?b>", "**", html)
    s = s.replace("<br>", "<br>\n")
    return s.strip()


def escribir(destino, titulo, tarjetas, fuente_txt, apkg_txt):
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    n = len(tarjetas)
    lineas = [f"# Flashcards · {titulo} · {n} preguntas", "",
              f"{INSTRUCCIONES} ({apkg_txt}).", "", fuente_txt, ""]
    for i, (q, a, ref) in enumerate(tarjetas, 1):
        resp = a_markdown(a) + (f" [{ref}]" if ref else "")
        lineas += [f"## {i}. {a_markdown(q)}", "", "<details>", "<summary>Ver respuesta</summary>",
                   "", resp, "", "</details>", ""]
    with open(destino + ".md", "w", encoding="utf-8") as f:
        f.write("\n".join(lineas))
    with open(destino + ".tsv", "w", encoding="utf-8") as f:
        for q, a, ref in tarjetas:
            resp = a + (f" [{ref}]" if ref else "")
            f.write(f"{q}\t{resp}\n".replace("\r", ""))
    print(f"{destino}: {n} tarjetas")


def generar_apkg(destino, nombre_mazo, id_mazo, tarjetas, etiquetas):
    import genanki
    modelo = genanki.Model(  # mismo tipo de nota que los mazos de los días 1-3
        1607392319, "Oceanografía básica",
        fields=[{"name": "Pregunta"}, {"name": "Respuesta"}],
        templates=[{"name": "Tarjeta",
                    "qfmt": "<div class='q'>{{Pregunta}}</div>",
                    "afmt": "<div class='q'>{{Pregunta}}</div><hr id=answer><div class='a'>{{Respuesta}}</div>"}],
        css=(".card{font-family:Arial;font-size:20px;text-align:center;color:#111;background:#fff}"
             ".q{font-weight:bold;color:#0B3954}.a{line-height:1.5}.nightMode .q{color:#7fc8d1}"
             ".nightMode.card{background:#1e1e1e;color:#eee}"))
    mazo = genanki.Deck(id_mazo, nombre_mazo)
    for q, a, ref in tarjetas:
        resp = a + (f"<br><small>[{ref}]</small>" if ref else "")
        mazo.add_note(genanki.Note(model=modelo, fields=[q, resp], tags=etiquetas,
                                   guid=genanki.guid_for(nombre_mazo, q)))
    os.makedirs(os.path.dirname(destino), exist_ok=True)
    genanki.Package(mazo).write_to_file(destino)
    print(f"{destino}: mazo Anki")


def main():
    r = lambda *p: os.path.join(RAIZ, *p)  # noqa: E731
    fuente_resumen = ("**Fuentes:** el resumen y las diapositivas de este bloque. Las tarjetas no llevan "
                      "número de diapositiva: si fallas una, búscala en el resumen del día.")

    dias = [
        (r("01-introduccion", "anki", "Oceanografia - Dia 1 - Introduccion.apkg"),
         r("01-introduccion", "flashcards", "Flashcards Dia 1 - Introduccion"),
         "Día 1 · Introducción", "mazo `anki/Oceanografia - Dia 1 - Introduccion.apkg`"),
        (r("02-mecanica-de-ondas", "anki", "Oceanografia - Dia 2 - Mecanica de ondas.apkg"),
         r("02-mecanica-de-ondas", "flashcards", "Flashcards Dia 2 - Mecanica de ondas"),
         "Día 2 · Mecánica de ondas", "mazo `anki/Oceanografia - Dia 2 - Mecanica de ondas.apkg`"),
        (r("03-analisis-del-oleaje", "anki", "Oceanografia - Dia 3 - Analisis estadistico.apkg"),
         r("03-analisis-del-oleaje", "flashcards", "Flashcards Dia 3 - Analisis estadistico"),
         "Día 3 · Análisis estadístico", "mazo `anki/Oceanografia - Dia 3 - Analisis estadistico.apkg`"),
    ]
    for apkg, destino, titulo, apkg_txt in dias:
        escribir(destino, titulo, leer_apkg(apkg), fuente_resumen, apkg_txt)

    escribir(r("03-analisis-del-oleaje", "flashcards", "Flashcards Dia 4 - Analisis espectral"),
             "Día 4 · Análisis espectral", DIA4_ESPECTRAL,
             "**Fuentes:** *Esp. d.X* = diapositiva X de [Análisis del oleaje 2de3 — Espectral]"
             "(<../Oceanografia - Bloque 2 - Analisis del oleaje 2de3 - Espectral.pdf>); "
             "*Cálc. d.X* = diapositiva X de [Cálculo de espectros]"
             "(<../Oceanografia - Bloque 2 -  Calculo_de_espectros.pdf>). "
             "Las 19 primeras son las que alimentan el ejercicio espectral; del 20 en adelante, teoría.",
             "mazo `anki/Oceanografia - Dia 4 - Analisis espectral.apkg`")
    generar_apkg(r("03-analisis-del-oleaje", "anki", "Oceanografia - Dia 4 - Analisis espectral.apkg"),
                 "Oceanografía::Día 4 - Análisis espectral", 2059400104, DIA4_ESPECTRAL,
                 ["oceanografia", "bloque2", "espectral"])

    escribir(r("examenes", "flashcards", "Flashcards - Recetas y trampas del examen"),
             "Recetas y trampas del examen", EXAMEN,
             "**Fuentes:** *Estructura §X* = sección X de [Análisis de la estructura del examen]"
             "(<../00 - Analisis de la estructura del examen.pdf>); *P25* = [1er Parcial 29-10-2025]"
             "(<../Examen 1er Parcial 29-10-2025 (resuelto).pdf>); *F25* = [Final 13-01-2025]"
             "(<../Examen Final ordinario 1er Parcial 13-01-2025 (resuelto).pdf>); *Esp. d.X* = diapositiva "
             "del Espectral.",
             "mazo `anki/Oceanografia - Examen - Recetas y trampas.apkg`")
    generar_apkg(r("examenes", "anki", "Oceanografia - Examen - Recetas y trampas.apkg"),
                 "Oceanografía::Examen - Recetas y trampas", 2059400105, EXAMEN,
                 ["oceanografia", "examen"])


if __name__ == "__main__":
    main()
