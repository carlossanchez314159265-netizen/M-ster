#!/usr/bin/env python3
"""Genera un test interactivo (HTML) y su versión Markdown a partir de un banco JSON.

Uso:
    python3 herramientas/generar_test.py herramientas/bancos/elena_seco_2.json \
        --html "Estudio/Elena Seco/test_elena_seco_2.html" \
        --md "Estudio/Elena Seco/TEST_2.md"

El HTML sale de herramientas/plantilla_test.html (diseño del test de IINT) e incluye:
filtro por temas, barajar preguntas/opciones, corrección al momento con explicación,
repetir falladas y el historial de fallos guardado en el navegador
(«Repasar falladas», «Ver mis fallos», descargar lista, borrar historial).

Formato del banco JSON:
{
  "titulo": "Test Elena Seco 2",
  "asignatura": "Economía y Gestión de Empresas Marítimas · UPM Navales",
  "descripcion": "Texto bajo el título",
  "etiqueta": "Test 2",
  "clave": "elena-seco-quiz-2",          # identifica el historial en el navegador: no la cambies
  "temas": {"1": "Nombre largo", ...},     # aparece en cada pregunta y en el resumen
  "temas_cortos": {"1": "Nombre corto", ...},  # texto de los botones de filtro
  "preguntas": [
    {"tema": 1, "pregunta": "...", "correcta": "...",
     "incorrectas": ["...", "...", "..."], "explicacion": "..."}
  ]
}

Comprobaciones (el script falla si no se cumplen, salvo --forzar):
- 4 opciones distintas por pregunta, tema existente, textos no vacíos.
- Sesgo de longitud: la correcta no puede ser la opción más larga en más del 35 %
  de las preguntas (por azar sería ~25 %). Lista las preguntas que lo provocan.
"""
import argparse, hashlib, html as _html, json, random, sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
MAX_SESGO = 0.35


def cargar(ruta):
    b = json.loads(Path(ruta).read_text(encoding="utf-8"))
    for k in ("titulo", "clave", "temas", "preguntas"):
        if k not in b:
            sys.exit(f"Falta la clave «{k}» en el banco")
    b.setdefault("asignatura", "")
    b.setdefault("descripcion", f"{len(b['preguntas'])} preguntas de práctica.")
    b.setdefault("etiqueta", "Test")
    b.setdefault("temas_cortos", b["temas"])
    return b


def validar(b, forzar):
    errores, largas = [], []
    vistos = set()
    for i, p in enumerate(b["preguntas"], 1):
        ops = [p.get("correcta", "")] + list(p.get("incorrectas", []))
        if len(ops) != 4 or len(set(ops)) != 4 or not all(o.strip() for o in ops):
            errores.append(f"#{i}: hacen falta 1 correcta y 3 incorrectas distintas")
        if str(p.get("tema")) not in b["temas"]:
            errores.append(f"#{i}: tema {p.get('tema')} no definido")
        if not p.get("pregunta", "").strip() or not p.get("explicacion", "").strip():
            errores.append(f"#{i}: falta enunciado o explicación")
        if p.get("pregunta") in vistos:
            errores.append(f"#{i}: pregunta repetida")
        vistos.add(p.get("pregunta"))
        if len(ops) == 4 and len(ops[0]) > max(len(o) for o in ops[1:]):
            largas.append(i)
    n = len(b["preguntas"])
    sesgo = len(largas) / n if n else 0
    print(f"{n} preguntas · la correcta es la más larga en {len(largas)} ({sesgo:.0%}; límite {MAX_SESGO:.0%})")
    if sesgo > MAX_SESGO:
        errores.append("Demasiadas preguntas con la correcta como opción más larga. "
                       "Alarga alguna incorrecta o acorta la correcta en: " + ", ".join(f"#{i}" for i in largas))
    if errores:
        print("\n".join(errores), file=sys.stderr)
        if not forzar:
            sys.exit(1)


def construir(b):
    rnd = random.Random(int(hashlib.sha1(b["clave"].encode()).hexdigest(), 16))
    orden = sorted(b["preguntas"], key=lambda p: int(p["tema"]))
    data = []
    for n, p in enumerate(orden, 1):
        ops = [p["correcta"]] + p["incorrectas"]
        idx = list(range(4)); rnd.shuffle(idx)
        data.append(dict(id=f"T{n}", n=n, s="T", b=int(p["tema"]), q=p["pregunta"],
                         o=[ops[i] for i in idx], a=idx.index(0), e=p["explicacion"]))
    return data


def html(b, data):
    t = (AQUI / "plantilla_test.html").read_text(encoding="utf-8")
    cnt = {k: sum(1 for d in data if d["b"] == int(k)) for k in b["temas"]}
    chips = "".join(
        f'\n      <button class="chip" id="b-{k}" data-b="{k}" aria-pressed="false">{_html.escape(b["temas_cortos"].get(k, v))} ({cnt[k]})</button>'
        for k, v in sorted(b["temas"].items(), key=lambda kv: int(kv[0])) if cnt[k])
    rep = {
        "{{TITULO}}": _html.escape(b["titulo"]),
        "{{ASIGNATURA}}": _html.escape(b["asignatura"]),
        "{{DESCRIPCION}}": _html.escape(b["descripcion"]),
        "{{N}}": str(len(data)),
        "{{CHIPS_TEMA}}": chips,
        "{{BNAMES}}": json.dumps({int(k): v for k, v in b["temas"].items()}, ensure_ascii=False),
        "{{ETIQUETA}}": b["etiqueta"].replace('"', "'"),
        "{{KEY}}": b["clave"].replace('"', ""),
        "{{DATA}}": json.dumps(data, ensure_ascii=False).replace("</", "<\\/"),
    }
    for k, v in rep.items():
        t = t.replace(k, v)
    return t


def markdown(b, data, nombre_html):
    L = [f"# {b['titulo']} · {len(data)} preguntas", "", b["descripcion"], ""]
    if nombre_html:
        L += [f"Versión autocorregible, con historial de fallos: [{nombre_html}]({nombre_html.replace(' ', '%20')}).", ""]
    L += ["| Tema | Preguntas |", "|---|---|"]
    for k, v in sorted(b["temas"].items(), key=lambda kv: int(kv[0])):
        c = sum(1 for d in data if d["b"] == int(k))
        if c:
            L.append(f"| {v} | {c} |")
    cur = None
    for d in data:
        if d["b"] != cur:
            cur = d["b"]; L += ["", "---", "", f"## {b['temas'][str(cur)]}", ""]
        L += [f"### {d['n']}. {d['q']}", ""] + [f"- **{l}.** {o}" for l, o in zip("ABCD", d["o"])]
        L += ["", "<details><summary>Solución</summary>", "", f"**{'ABCD'[d['a']]}.** {d['e']}", "", "</details>", ""]
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("banco")
    ap.add_argument("--html", required=True)
    ap.add_argument("--md")
    ap.add_argument("--forzar", action="store_true", help="genera aunque falle alguna comprobación")
    a = ap.parse_args()
    b = cargar(a.banco)
    validar(b, a.forzar)
    data = construir(b)
    Path(a.html).write_text(html(b, data), encoding="utf-8")
    print("HTML:", a.html)
    if a.md:
        Path(a.md).write_text(markdown(b, data, Path(a.html).name), encoding="utf-8")
        print("Markdown:", a.md)


if __name__ == "__main__":
    main()
