"""Genera el informe de la tarea MEF del submarino (DOCX editable + PDF).

Uso:  python3 generar_informe.py        (crea informe_submarino.docx y, con LibreOffice, informe_submarino.pdf)

Los huecos a rellenar con resultados de Femap van en amarillo entre corchetes.
"""
import pathlib, subprocess
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_COLOR_INDEX
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

HERE = pathlib.Path(__file__).resolve().parent
FIG = HERE.parent

doc = Document()
sec = doc.sections[0]
sec.page_height, sec.page_width = Cm(29.7), Cm(21.0)
for side in ("left_margin", "right_margin"):
    setattr(sec, side, Cm(2.2))
sec.top_margin = sec.bottom_margin = Cm(2.0)

st = doc.styles["Normal"]
st.font.name = "Calibri"; st.font.size = Pt(10.5)
st.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
st.paragraph_format.space_after = Pt(5)
st.paragraph_format.line_spacing = 1.12
for name, size, color in (("Heading 1", 15, "1F3864"), ("Heading 2", 12.5, "2E5597"), ("Heading 3", 11, "2E5597")):
    h = doc.styles[name]; h.font.name = "Calibri"; h.font.size = Pt(size); h.font.bold = True
    h.font.color.rgb = RGBColor.from_string(color)
    h.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
    h.paragraph_format.space_before = Pt(12 if name == "Heading 1" else 8); h.paragraph_format.space_after = Pt(4)


def rich(par, text):
    """Texto con [huecos] resaltados en amarillo y **negrita**."""
    import re
    for tok in re.split(r"(\[[^\]]+\]|\*\*[^*]+\*\*)", text):
        if not tok:
            continue
        if tok.startswith("["):
            r = par.add_run(tok); r.font.highlight_color = WD_COLOR_INDEX.YELLOW; r.bold = True
        elif tok.startswith("**"):
            r = par.add_run(tok[2:-2]); r.bold = True
        else:
            par.add_run(tok)
    return par


def P(text, style=None, align=None):
    p = doc.add_paragraph(style=style)
    rich(p, text)
    if align == "j":
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    return p


def B(text):
    return P(text, style="List Bullet")


def shade(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr(); s = OxmlElement("w:shd")
    s.set(qn("w:val"), "clear"); s.set(qn("w:color"), "auto"); s.set(qn("w:fill"), hexcolor); tcPr.append(s)


def T(header, rows, widths=None):
    t = doc.add_table(rows=1, cols=len(header)); t.style = "Table Grid"; t.alignment = WD_TABLE_ALIGNMENT.CENTER
    for i, h in enumerate(header):
        c = t.rows[0].cells[i]; c.text = ""; r = c.paragraphs[0].add_run(h); r.bold = True; r.font.size = Pt(9.5)
        shade(c, "DCE6F2")
    for row in rows:
        cells = t.add_row().cells
        for i, v in enumerate(row):
            cells[i].text = ""; p = cells[i].paragraphs[0]; rich(p, str(v))
            for r in p.runs:
                r.font.size = Pt(9.5)
    if widths:
        for row in t.rows:
            for i, w in enumerate(widths):
                row.cells[i].width = Cm(w)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)
    return t


def FIGURE(path, caption, width=16):
    if path and pathlib.Path(path).exists():
        doc.add_picture(str(path), width=Cm(width))
        doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
    else:
        t = doc.add_table(rows=1, cols=1); t.style = "Table Grid"; t.alignment = WD_TABLE_ALIGNMENT.CENTER
        c = t.rows[0].cells[0]; c.width = Cm(width); shade(c, "FFF9DB")
        p = c.paragraphs[0]; p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(f"\n[PEGAR CAPTURA DE FEMAP: {path}]\n\n"); r.bold = True
        r.font.highlight_color = WD_COLOR_INDEX.YELLOW
    cp = doc.add_paragraph(); cp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    r = cp.add_run(caption); r.italic = True; r.font.size = Pt(9)


# ------------------------------------------------------------------ portada
for _ in range(5):
    doc.add_paragraph()
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("Análisis por elementos finitos de un submarino simplificado\nsometido a presión exterior (250 m)"); r.bold = True; r.font.size = Pt(20)
r.font.color.rgb = RGBColor.from_string("1F3864")
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = p.add_run("Análisis lineal en tensiones y desplazamientos, cambio dimensional e inestabilidad"); r.font.size = Pt(12.5)
for _ in range(3):
    doc.add_paragraph()
for line in ("Diseño de Estructuras Navales — 1.º MUINO, curso 2026-27",
             "ETSI Navales — Universidad Politécnica de Madrid",
             "Herramienta: Simcenter Femap 2412 con Nastran (licencia educativa)"):
    p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER; p.add_run(line).font.size = Pt(11.5)
doc.add_paragraph()
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
rich(p, "Autor: [Nombre y apellidos]")
p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p.add_run("Madrid, 26 de noviembre de 2026")
doc.add_page_break()

# ------------------------------------------------------------------ 1
doc.add_heading("1. Objeto y enunciado", 1)
P("Se analiza mediante el método de los elementos finitos una representación simplificada del casco resistente de un "
  "submarino sometido a la presión exterior correspondiente a 250 m de profundidad. Se piden: (a) análisis lineal en "
  "tensiones y desplazamientos, (b) cambio dimensional del objeto y (c) análisis de inestabilidad (pandeo).", align="j")
P("Datos del enunciado:")
T(["Elemento", "Definición"], [
    ["Casco", "Semiesfera de proa R = 5 m + cilindro de 15 m + tronco de cono de 6 m (R 5 → 2,5 m) + semiesfera de popa R = 2,5 m"],
    ["Material y espesor", "Acero HS56 o HY80, chapa de 35 mm"],
    ["Mamparo M1", "Plano, 25 mm, en la base mayor del cono, con orificio elíptico centrado de semiejes 1000 × 500 mm"],
    ["Mamparo M2", "Plano, 25 mm, una cuaderna a popa de la unión esfera–cilindro, orificio circular de radio 1000 mm"],
    ["Mamparo M3", "Plano, 25 mm, en la unión cono–semiesfera, orificio circular de radio 400 mm"],
    ["Cubierta", "Intermedia, 20 mm, con baos en las cuadernas"],
    ["Cuadernas", "Cinco equiespaciadas en el cilindro (la primera en la unión esfera–cilindro) y una en el cono; perfil en T 150 × 150 × 15 mm"],
    ["Escotilla", "Orificio de Ø 2000 mm en la parte superior, centrado en la 3.ª cuaderna, con brazola de 250 mm"],
    ["Carga", "Presión exterior a 250 m de profundidad"],
], widths=[3.5, 13])

# ------------------------------------------------------------------ 2
doc.add_heading("2. Hipótesis e interpretación del enunciado", 1)
P("El enunciado deja abiertos varios aspectos. Se adoptan las siguientes hipótesis, que condicionan el modelo:", align="j")
T(["Aspecto", "Hipótesis adoptada", "Justificación"], [
    ["Superficie de referencia", "Los radios 5000 y 2500 mm se toman como radios de la superficie media", "Modelo de láminas; error t/2R ≈ 0,35 %"],
    ["Cuadernas del cilindro", "x = 0, 3000, 6000, 9000 y 12000 mm (separación 3000 mm)", "Equiespaciadas, la 1.ª en la unión esfera–cilindro; el último vano lo cierra M1 (x = 15000)"],
    ["Cuaderna del cono", "x = 18000 mm (mitad del cono, r = 3750 mm)", "El enunciado no fija su posición"],
    ["Mamparos", "M2 en x = 3000 (coincide con la 2.ª cuaderna), M1 en x = 15000, M3 en x = 21000", "Según el enunciado"],
    ["Orificio de M1", "Elipse de semiejes 1000 mm (vertical) × 500 mm (horizontal)", "«r = 1000 × 500» se lee como semiejes; vertical como un paso de puerta"],
    ["Cubierta", "Plana, 1500 mm por debajo del eje, de x = 0 a x = 21000 (M3)", "Deja libres los orificios centrados de los mamparos; llega al cono porque se pide bao en su cuaderna"],
    ["Escotilla y brazola", "Orificio Ø 2000 centrado en x = 6000; brazola tubular de 35 mm, 250 mm de altura medidos desde el borde del orificio", "Espesor de brazola no especificado: se toma el del casco"],
    ["Material", "HY80: E = 210 000 MPa, ν = 0,3, ρ = 7850 kg/m³, σy ≈ 550 MPa", "HY80 = 80 ksi ≈ 552 MPa; HS56 ≈ 56 kp/mm² ≈ 549 MPa"],
    ["Presión", "p = ρgh = 1025 · 9,81 · 250 = 2,514 MPa, uniforme", "La variación entre quilla y techo (0,10 MPa, 4 %) es despreciable"],
    ["Simetría", "Se modela medio submarino respecto al plano diametral", "Geometría y carga simétricas; reduce el tamaño del modelo"],
], widths=[3.2, 7.2, 6.1])

# ------------------------------------------------------------------ 3
doc.add_heading("3. Geometría", 1)
P("Unidades coherentes: mm, N, MPa (N/mm²) y t. En el modelo de Femap el eje del submarino es **X** (proa en x = −5000, "
  "popa en x = 23500), la vertical es **Y** (hacia arriba −Y; la escotilla queda en y = −5000) y el plano de simetría es **z = 0**. "
  "La figura 1 es un esquema acotado (dibujado con Z vertical).", align="j")
FIGURE(FIG / "geometria_submarino.png", "Figura 1. Perfil y sección acotados según las hipótesis adoptadas (esquema).", 16.5)
T(["Magnitud", "Valor"], [
    ["Eslora total", "28 500 mm"],
    ["Semiángulo del cono", "22,62° (generatriz 6500 mm)"],
    ["Ancho de cubierta", "9539 mm en el cilindro; 6874 mm en x = 18000; 4000 mm en M3"],
    ["Volumen encerrado", "1747,5 m³"],
], widths=[5, 11])
P("Procedimiento de construcción en Femap: superficies primitivas (esfera, cilindro y cono) recortadas por planos "
  "(x = 0, 3000, 6000, 9000, 12000, 15000, 18000, 21000 y el plano de cubierta), completadas por simetría; mamparos "
  "como superficies planas con su orificio; cubierta como superficie plana cuyos bordes en el cono siguen la intersección "
  "con el casco; orificio de escotilla por intersección con un cilindro auxiliar y brazola por extrusión del borde del orificio.", align="j")
FIGURE("vista isométrica del modelo geométrico (casco transparente, con mamparos, cubierta y brazola)",
       "Figura 2. Modelo geométrico en Femap.", 15)

# ------------------------------------------------------------------ 4
doc.add_heading("4. Modelo de elementos finitos", 1)
doc.add_heading("4.1 Material y propiedades", 2)
T(["Propiedad", "Tipo", "Espesor / sección", "Elementos"], [
    ["casco", "Plate (CQUAD4/CTRIA3)", "35 mm", "Semiesferas, cilindro y cono"],
    ["mamparo", "Plate", "25 mm", "M1, M2, M3"],
    ["cubierta", "Plate", "20 mm", "Cubierta"],
    ["brazola", "Plate", "35 mm", "Brazola de la escotilla"],
    ["cuaderna", "[Beam T 150×150×15 con offset hacia el eje / Plate 15 mm (alma de 150 mm)]", "T 150 × 150 × 15", "Cuadernas y baos"],
], widths=[2.4, 4.6, 3.8, 5.7])
P("Material HY-80 introducido manualmente (no figura en la librería de Femap): E = 210 000 MPa, ν = 0,3, ρ = 7,85·10⁻⁹ t/mm³.")
doc.add_heading("4.2 Malla", 2)
P("Elementos lámina lineales de cuatro nodos (con triángulos donde la geometría lo exige), situados en la superficie "
  "media, con tamaño general de **200 mm**. El tamaño se justifica por el pandeo esperado entre cuadernas, con unos "
  "n = 11 lóbulos: la media onda circunferencial (π·5000/11 ≈ 1430 mm) queda descrita por unos 7 elementos y la axial "
  "(3000 mm) por 15. Las mallas de casco, cubierta, mamparos y brazola se unen fusionando nodos coincidentes "
  "(tolerancia [0,5] mm) y se comprueba la ausencia de bordes libres en las uniones.", align="j")
T(["Dato de la malla", "Valor"], [
    ["Número de nodos", "[nodos]"], ["Número de elementos lámina", "[elementos]"],
    ["Número de elementos viga (si procede)", "[vigas]"], ["Tamaño de elemento", "200 mm"],
], widths=[7, 6])
FIGURE("malla completa en vista isométrica", "Figura 3. Malla de elementos finitos (medio modelo).", 15)

doc.add_heading("4.3 Cargas", 2)
B("**Presión exterior** de 2,514 MPa sobre el casco y la cara exterior de la brazola, dirigida hacia el interior. "
  "Mamparos y cubierta son interiores y no se cargan.")
B("**Tapa de la escotilla** (no modelada, cerrada): su carga p·π·r² = 2,514·π·1000² ≈ 7,90 MN se transmite a la brazola. "
  "En medio modelo se aplican **3,949 MN** repartidos en el medio borde superior de la brazola (≈ 1257 N/mm), hacia el interior (+Y). "
  "Sin esta carga el orificio dejaría una resultante neta espuria de ≈ 4 MN.")
doc.add_heading("4.4 Condiciones de contorno", 2)
B("**Simetría** en todos los bordes del plano z = 0: TZ = RX = RY = 0.")
B("**Sólido rígido**: polo de proa (−5000, 0, 0) con TX = TY = 0; polo de popa (23500, 0, 0) con TY = 0. "
  "Restricciones isostáticas: la presión está autoequilibrada y las reacciones en los polos deben ser prácticamente nulas.")
T(["Comprobación de equilibrio", "Resultado"], [
    ["Reacción en el polo de proa (FX, FY)", "[valor, ≈ 0]"],
    ["Reacción en el polo de popa (FY)", "[valor, ≈ 0]"],
], widths=[8, 6])
FIGURE("cargas y apoyos (flechas de presión hacia dentro, apoyos en el plano z = 0 y en los polos)",
       "Figura 4. Cargas y condiciones de contorno.", 15)

# ------------------------------------------------------------------ 5
doc.add_heading("5. Análisis lineal: tensiones y desplazamientos", 1)
P("Análisis estático lineal (Nastran SOL 101). Se comparan los resultados con las soluciones de membrana de láminas "
  "delgadas, válidas lejos de uniones, cuadernas y orificios:", align="j")
T(["Zona", "Expresión", "Analítico (MPa)", "MEF (MPa)"], [
    ["Cilindro, σθ", "pR/t", "359", "[ ]"],
    ["Cilindro, σx", "pR/2t", "180", "[ ]"],
    ["Cilindro, von Mises (centro de vano)", "—", "311", "[ ]"],
    ["Semiesfera de proa", "pR/2t", "180", "[ ]"],
    ["Semiesfera de popa", "pR/2t", "90", "[ ]"],
    ["Cono, base mayor, von Mises", "σθ = pr/(t cos α)", "337", "[ ]"],
    ["Unión cilindro–cono (pico de flexión)", "Empuje radial ≈ 2600 N/mm", "> 337", "[ ]"],
    ["Borde de la escotilla (pico)", "Concentración de tensiones", "> 311", "[ ]"],
    ["Mamparos (compresión en su plano)", "q/t, q ≈ 1230 N/mm", "≈ 49", "[ ]"],
], widths=[5.2, 4.3, 3.0, 3.0])
FIGURE("contorno de tensión de von Mises, cara superior (Plate Top VonMises)", "Figura 5. Tensión de von Mises, cara superior.", 15)
FIGURE("contorno de tensión de von Mises, cara inferior (Plate Bot VonMises)", "Figura 6. Tensión de von Mises, cara inferior.", 15)
FIGURE("deformada amplificada (Total Translation)", "Figura 7. Deformada (factor de amplificación [ ]).", 15)
P("Comentario: [Indicar dónde aparece el máximo de von Mises y su valor, si supera o no el límite elástico (≈ 550 MPa), "
  "y la diferencia entre la tensión general del casco y los picos locales en la escotilla y la unión cilindro–cono.]", align="j")

# ------------------------------------------------------------------ 6
doc.add_heading("6. Cambio dimensional", 1)
P("La presión acorta el submarino y reduce su diámetro. La estimación analítica de membrana (sin cuadernas ni "
  "mamparos, por tanto cota superior) es:", align="j")
B("Cilindro: w = pR²(1 − ν/2)/(Et) = 7,27 mm hacia dentro → ΔD = −14,5 mm.")
B("Cilindro: εx = −pR(1/2 − ν)/(Et) = −3,42·10⁻⁴ → ΔL = −5,1 mm.")
B("Semiesferas: w = pR²(1 − ν)/(2Et) = 2,99 mm (proa) y 0,75 mm (popa).")
B("Eslora total: ΔL ≈ −8,4 mm. Volumen: ΔV ≈ −5,0 m³ (−0,29 %), es decir, unas 5 t de empuje perdido.")
T(["Magnitud", "Cómo se obtiene del MEF", "Analítico", "MEF"], [
    ["Δ eslora", "TX(polo popa) − TX(polo proa)", "≈ −8,4 mm", "[ ]"],
    ["Δ diámetro, centro de vano", "2 × desplazamiento radial", "≈ −14,5 mm", "[ ]"],
    ["Δ diámetro, en cuaderna", "2 × desplazamiento radial", "< 14,5 mm", "[ ]"],
    ["Δ radio semiesfera proa", "Desplazamiento radial", "≈ −3,0 mm", "[ ]"],
    ["Δ volumen / empuje", "Σ 2π r w̄ Δx por tramos", "≈ −5,0 m³ / 5 t", "[ ]"],
], widths=[3.8, 5.6, 3.3, 3.3])
P("El desplazamiento radial se lee en un sistema de coordenadas cilíndrico cuyo eje coincide con el eje X global. "
  "Se espera la deformada «en acordeón»: el casco se hunde más en el centro de cada vano que en las cuadernas y apenas en los mamparos.", align="j")

# ------------------------------------------------------------------ 7
doc.add_heading("7. Análisis de inestabilidad", 1)
P("Pandeo lineal por autovalores (Nastran SOL 105) con la carga del apartado 4.3. El autovalor λ multiplica la carga "
  "aplicada: p_cr = λ · 2,514 MPa y profundidad crítica ≈ λ · 250 m; λ < 1 indica pandeo antes de los 250 m. "
  "Al usar medio modelo con condiciones de simetría, solo se obtienen los modos simétricos respecto al plano diametral.", align="j")
doc.add_heading("7.1 Referencias analíticas", 2)
T(["Modo", "Referencia", "p_cr (MPa)", "λ"], [
    ["Mamparos planos sin refuerzos", "Placa circular, 25 mm, R 5000, compresión radial ≈ 1230 N/mm", "—", "0,04 – 0,14"],
    ["Cono", "Cilindro equivalente (R 4063, L 3250–6500)", "0,88 – 1,83", "0,35 – 0,73"],
    ["Inestabilidad general", "Bryant, L = 12 000, n = 5", "1,35", "0,54"],
    ["Entre cuadernas (lóbulos)", "von Mises, L = 3000, n = 11", "1,46", "0,58"],
    ["Semiesfera de proa", "Clásica 1,21E(t/R)² (×0,3 con imperfecciones)", "12,5 (3,7)", "4,95 (1,5)"],
    ["Semiesfera de popa", "Clásica", "49,8", "19,8"],
], widths=[3.8, 6.6, 2.8, 2.8])
doc.add_heading("7.2 Resultados del MEF", 2)
T(["Modo", "λ", "p_cr (MPa)", "Profundidad (m)", "Descripción"], [
    [str(i), "[ ]", "[ ]", "[ ]", "[mamparo / cubierta / cono / lóbulos / general]"] for i in range(1, 7)
], widths=[1.4, 2.0, 2.6, 3.0, 7.0])
FIGURE("primer modo de pandeo", "Figura 8. Primer modo de pandeo (λ = [ ]).", 14)
FIGURE("primer modo de pandeo del casco (lóbulos entre cuadernas o modo general)", "Figura 9. Primer modo del casco (λ = [ ]).", 14)
P("Comentario: [Describir qué elementos pandean primero. Se espera que los primeros modos sean locales de los mamparos "
  "planos sin refuerzos, que reciben del casco una compresión en su plano muy superior a su carga crítica, y que los "
  "modos del casco aparezcan con λ ≈ 0,5–0,6.]", align="j")

# ------------------------------------------------------------------ 8
doc.add_heading("8. Conclusiones", 1)
B("En tensiones, el casco trabaja a [ ] MPa (von Mises) en el centro de los vanos, frente a ≈ 311 MPa analíticos y un límite "
  "elástico de ≈ 550 MPa. Los máximos locales aparecen en [la escotilla / la unión cilindro–cono] con [ ] MPa.")
B("Cambio dimensional: el submarino se acorta [ ] mm y su diámetro disminuye [ ] mm, con una pérdida de volumen de "
  "[ ] m³ (≈ [ ] t de empuje).")
B("Inestabilidad: el primer autovalor es λ = [ ], es decir, p_cr = [ ] MPa (≈ [ ] m). La estructura [resiste / no resiste] "
  "la presión de 250 m frente a pandeo, aunque resista en tensiones.")
B("La separación de cuadernas de 3000 mm es grande para un casco resistente: según la fórmula de von Mises, el pandeo "
  "entre cuadernas solo supera los 250 m (λ > 1) con separaciones de unos 1500 mm o menos (λ ≈ 1,28 con 1500 mm, "
  "≈ 2,1 con 1000 mm). Los mamparos planos de 25 mm necesitarían refuerzos.")
T(["Separación de cuadernas (mm)", "3000", "2500", "2000", "1500", "1000", "750"], [
    ["p_cr entre cuadernas (MPa)", "1,46", "1,78", "2,29", "3,22", "5,34", "7,94"],
    ["λ", "0,58", "0,71", "0,91", "1,28", "2,13", "3,16"],
])
B("Limitaciones: análisis lineal sin imperfecciones (sobrestima la carga de pandeo real), medio modelo (solo modos "
  "simétricos) y uniones modeladas sin soldaduras ni detalles locales.")

doc.add_heading("Anexo. Expresiones utilizadas", 1)
for f in ("Presión: p = ρ g h.",
          "Membrana del cilindro: σθ = pR/t, σx = pR/2t. Esfera: σ = pR/2t. Cono: σθ = pr/(t cos α), σm = pr/(2t cos α).",
          "Pandeo entre cuadernas (von Mises): p_cr = (Et/R)·{λ⁴/(n² + λ²)² + t²(n² + λ²)²/(12R²(1 − ν²))}/(n² − 1 + λ²/2), λ = πR/L, mínimo en n.",
          "Inestabilidad general (Bryant): p_n = (Et/R)·λ⁴/{(n² + λ²/2 − 1)(n² + λ²)²} + (n² − 1)·E·Ie/(R³·s), λ = πR/L_B.",
          "Esfera (clásica): p_cr = 2E(t/R)²/√(3(1 − ν²)).",
          "Cambio radial del cilindro: w = pR²(1 − ν/2)/(Et); de la esfera: w = pR²(1 − ν)/(2Et)."):
    B(f)

out = HERE / "informe_submarino.docx"
doc.save(out)
print("DOCX:", out)
try:
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", str(HERE), str(out)],
                   check=True, capture_output=True, timeout=180)
    print("PDF:", HERE / "informe_submarino.pdf")
except Exception as e:
    print("No se pudo convertir a PDF:", e)
