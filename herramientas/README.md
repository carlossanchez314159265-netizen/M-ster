# Herramientas

- `generar_test.py`: crea un test interactivo (HTML) y su versión Markdown a partir de un banco de preguntas en JSON. Comprueba que la opción más larga no delate la correcta.
- `plantilla_test.html`: diseño del test (el mismo que el de IINT) con filtro por temas e historial de fallos.
- `bancos/`: bancos de preguntas de los tests ya generados.

```bash
python3 herramientas/generar_test.py herramientas/bancos/elena_seco_2.json --html "Estudio/Elena Seco/test_elena_seco_2.html" --md "Estudio/Elena Seco/TEST_2.md"
```
