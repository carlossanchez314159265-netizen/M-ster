"""Tema 7: Roots. Código de clase de Ampliación de matemáticas."""
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x + np.sin(x) / 2 - 1


def dibujar(f, xmin=-5, xmax=5):
    xs = np.linspace(xmin, xmax, 200)
    ys = f(xs)
    plt.figure(figsize=(8, 8))
    plt.plot(xs, ys)
    plt.title("Graph of f")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.axhline(color="k")  # eje x (y = 0)
    plt.axvline(color="k")  # eje y (x = 0)
    plt.show()


def bisection(f, a, b, xtol):
    # comprobar que f(a) y f(b) tienen signos opuestos
    if f(a) * f(b) > 0:
        print("error en el intervalo")
        return None
    # si un extremo ya es raíz, lo devolvemos
    if f(a) == 0:
        return a
    if f(b) == 0:
        return b

    xleft = a
    xright = b
    sleft = np.sign(f(xleft))
    j = 1
    # iterar hasta que el intervalo sea menor que xtol
    while xright - xleft > xtol:
        xmed = (xleft + xright) / 2
        smed = np.sign(f(xmed))
        if smed == 0:  # justo hemos caído en la raíz
            return xmed
        if smed == sleft:
            xleft = xmed  # la raíz está en la mitad derecha
        else:
            xright = xmed  # la raíz está en la mitad izquierda
        j = j + 1
    return (xleft + xright) / 2


def secante(f, x0, x1, xtol=1e-6):
    Nmax = 100
    j = 1
    while np.abs(x1 - x0) > xtol and j <= Nmax:
        if f(x1) == f(x0):
            print("No se puede seguir: f(x0) = f(x1)")
            return None
        xn = x1 - f(x1) / (f(x1) - f(x0)) * (x1 - x0)
        x0 = x1
        x1 = xn
        j = j + 1
    if j > Nmax:
        print("No ha convergido en", Nmax, "iteraciones")
    return x1


if __name__ == "__main__":
    print("Bisección:", bisection(f, -5, 5, 1e-6))
    print("Secante:  ", secante(f, -1, 4))
    bisection(f, 2, 5, 1e-6)  # debe dar "error en el intervalo"
    dibujar(f)
