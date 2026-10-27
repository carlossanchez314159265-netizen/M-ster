# Tema 7: Roots (raíces de ecuaciones)

Métodos numéricos para encontrar raíces de f(x) = 0 con Python.

- `7.Roots.ipynb`: notebook de clase (bisección, secante, punto fijo, Newton, minimización).
- `raices.py`: versión limpia y probada de la gráfica, bisección y secante.

## Notas de clase

- `plt.axhline(color="k")` dibuja la recta y = 0 (eje x); `plt.axvline(color="k")` dibuja x = 0 (eje y). No vienen por defecto.
- `np.sign(v)` devuelve 1.0 si v > 0, -1.0 si v < 0 y 0.0 si v = 0.
- Bisección: si f(a) y f(b) tienen signos distintos, hay al menos una raíz entre a y b (Bolzano). Se parte el intervalo por la mitad hasta que mide menos que `xtol`.
- Secante: xn = x1 - f(x1) / (f(x1) - f(x0)) * (x1 - x0). Falla si f(x0) = f(x1).
- Raíz de f(x) = x + sin(x)/2 - 1: x ≈ 0.684037.
- En Jupyter, `In [*]` significa que el kernel sigue ocupado (p. ej. un bucle infinito). Se para con Kernel → Interrupt.
