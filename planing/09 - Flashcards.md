# Flashcards — 163 preguntas en 5 mazos

Mismo formato que las de IINT: un Markdown por mazo con la respuesta plegada (se lee en GitHub, también desde el móvil) y un `.tsv` con las mismas tarjetas para Anki. Intenta responder antes de desplegar y marca las que falles para el repaso del martes y del miércoles.

| Orden | Mazo | Tarjetas | Markdown | Anki | Cuándo |
|---|---|---|---|---|---|
| 1 | Día 1 · Introducción | 25 | [Flashcards](<../01-introduccion/flashcards/Flashcards Dia 1 - Introduccion.md>) | [.apkg](<../01-introduccion/anki/Oceanografia - Dia 1 - Introduccion.apkg>) · [.tsv](<../01-introduccion/flashcards/Flashcards Dia 1 - Introduccion.tsv>) | Teoría corta (diapo 56) |
| 2 | Día 2 · Mecánica de ondas | 53 | [Flashcards](<../02-mecanica-de-ondas/flashcards/Flashcards Dia 2 - Mecanica de ondas.md>) | [.apkg](<../02-mecanica-de-ondas/anki/Oceanografia - Dia 2 - Mecanica de ondas.apkg>) · [.tsv](<../02-mecanica-de-ondas/flashcards/Flashcards Dia 2 - Mecanica de ondas.tsv>) | Vie 23 / Sáb 24 |
| 3 | Día 3 · Análisis estadístico | 34 | [Flashcards](<../03-analisis-del-oleaje/flashcards/Flashcards Dia 3 - Analisis estadistico.md>) | [.apkg](<../03-analisis-del-oleaje/anki/Oceanografia - Dia 3 - Analisis estadistico.apkg>) · [.tsv](<../03-analisis-del-oleaje/flashcards/Flashcards Dia 3 - Analisis estadistico.tsv>) | Dom 25 |
| 4 | Día 4 · Análisis espectral **(nuevo)** | 36 | [Flashcards](<../03-analisis-del-oleaje/flashcards/Flashcards Dia 4 - Analisis espectral.md>) | [.apkg](<../03-analisis-del-oleaje/anki/Oceanografia - Dia 4 - Analisis espectral.apkg>) · [.tsv](<../03-analisis-del-oleaje/flashcards/Flashcards Dia 4 - Analisis espectral.tsv>) | Mar 27 |
| 5 | Recetas y trampas del examen **(nuevo)** | 15 | [Flashcards](<../examenes/flashcards/Flashcards - Recetas y trampas del examen.md>) | [.apkg](<../examenes/anki/Oceanografia - Examen - Recetas y trampas.apkg>) · [.tsv](<../examenes/flashcards/Flashcards - Recetas y trampas del examen.tsv>) | Lun 26 (transporte) y Mié 28 |

**Qué hay de nuevo.** Los mazos 1–3 son exactamente las tarjetas de los `.apkg` que ya tenías, pasadas a Markdown. El espectral no tenía mazo: sus 36 tarjetas llevan la diapositiva de origen, y las 19 primeras son las que necesitas para el ejercicio C. El de recetas y trampas sale de los dos exámenes resueltos.

**Corrección que verás en la tarjeta 19 del espectral:** la diapo 80 da Tc = 4,23 s porque usa el exponente 3/4; con la fórmula correcta de la diapo 30, Tc = 2π√(m2/m4) = 4,83 s. La propia presentación de Cálculo de espectros (diapo 17) señala ese error.

**Si vas justo de tiempo:** el miércoles antes de entrar, el mazo 5 entero (5 min) y las 19 primeras del espectral.

**Anki.** Lo más cómodo es importar el `.apkg` (Archivo → Importar). Si prefieres el `.tsv`: texto UTF-8 separado por tabuladores, tipo de nota «Básico», primera columna anverso, segunda reverso y **activa «Permitir HTML»** (subíndices y negritas van en HTML).

Las flashcards se regeneran con `scripts/flashcards/generar_flashcards.py` (las nuevas se editan en `scripts/flashcards/nuevas_tarjetas.py`).
