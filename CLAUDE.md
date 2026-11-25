# Instrucciones para Claude en este repositorio

Repositorio de estudio del máster (UPM Navales). Cada asignatura vive en su propia rama.

## Cuando pida un test

Hazlo **siempre** con la herramienta del repositorio, nunca a mano:

1. Escribe el banco de preguntas en `herramientas/bancos/<nombre>.json` (formato explicado al principio de `herramientas/generar_test.py`; usa `herramientas/bancos/elena_seco_2.json` como ejemplo).
2. Genera el test:
   ```bash
   python3 herramientas/generar_test.py herramientas/bancos/<nombre>.json --html "<carpeta>/test_<nombre>.html" --md "<carpeta>/TEST_<NOMBRE>.md"
   ```
3. Si el script falla, corrige el banco. No uses `--forzar` para saltarte las comprobaciones.
4. Abre el HTML con Playwright (Chromium ya está instalado), responde alguna pregunta y comprueba que no hay errores antes de subirlo.

Requisitos que debe cumplir todo test:

- **Diseño del test de IINT** (rama `iint`, `parcial 01/test_interactivo.html`), que ya está en `herramientas/plantilla_test.html`: filtro por temas, barajar preguntas y opciones, corrección al momento con explicación y repetir falladas.
- **Historial de fallos** guardado en el navegador: «Repasar falladas», «Ver mis fallos», descargar la lista y borrar el historial. Ya viene en la plantilla.
- **La opción más larga no debe delatar la correcta.** Escribe las incorrectas plausibles y de longitud parecida a la correcta, y en bastantes preguntas haz que una incorrecta sea la más larga. El script rechaza el banco si la correcta es la más larga en más del 35 % de las preguntas.
- Una sola respuesta correcta y cuatro opciones distintas. La posición de la correcta se reparte al azar.
- Cada pregunta lleva una explicación breve de por qué es la correcta.
- Preguntas originales sacadas de los apuntes de la rama; di que no son de exámenes anteriores.
- No repitas preguntas de tests anteriores de la misma asignatura salvo que lo pida.
- Si pide un test «sin calculadora» o «sin ejercicios», solo preguntas de teoría.
- La `clave` del banco identifica el historial en el navegador: no la cambies al regenerar un test existente, o se perderán sus fallos guardados.

Después, añade el test al `README.md` de la carpeta de la asignatura y súbelo a la rama de esa asignatura.

## Otras preferencias

- Responde en español.
- Material de estudio en `Estudio/<Asignatura>/`.
