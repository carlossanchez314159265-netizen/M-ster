# Herramientas

- `generar_test.py`: crea un test interactivo (HTML) y su versión Markdown a partir de un banco de preguntas en JSON. Comprueba que la opción más larga no delate la correcta.
- `plantilla_test.html`: diseño del test (el mismo que el de IINT) con filtro por temas e historial de fallos.
- `bancos/`: bancos de preguntas de los tests ya generados.

```bash
python3 herramientas/generar_test.py herramientas/bancos/ejemplo.json --html test_ejemplo.html --md TEST_EJEMPLO.md
```
