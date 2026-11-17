"""Esquema: qué curvas seleccionar para crear el mamparo M2 (x = 3000) con Boundary Surface."""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

R = 5000
fig = plt.figure(figsize=(13, 8.5))
ax = fig.add_subplot(111, projection="3d")
ax.view_init(elev=18, azim=-58)
t = np.linspace(0, 2*np.pi, 361)

def circ(x, r, **kw):
    ax.plot(np.full_like(t, x), r*np.cos(t), r*np.sin(t), **kw)

grey = dict(color="0.65", lw=1.2)
# casco: semiesfera de proa (contornos) y cilindro hasta x=6000
for x in (0, 6000):
    circ(x, R, **grey)
for ang in (np.pi/2, -np.pi/2):           # líneas longitudinales (costuras) arriba y abajo
    ax.plot([0, 6000], [0, 0], [R*np.sin(ang)]*2, **grey)
ph = np.linspace(0, np.pi/2, 60)
for a in np.linspace(0, 2*np.pi, 9)[:-1]:
    ax.plot(-R*np.sin(ph[::-1])*0+(-R*np.cos(ph)), R*np.sin(ph)*np.cos(a), R*np.sin(ph)*np.sin(a), color="0.82", lw=0.8)

# curvas a seleccionar en x = 3000
up = (t >= np.pi/2) & (t <= 3*np.pi/2)
ax.plot(np.full(up.sum(), 3000), R*np.cos(t[up]), R*np.sin(t[up]), color="#e8590c", lw=4)
t2 = np.linspace(-np.pi/2, np.pi/2, 181)
ax.plot(np.full_like(t2, 3000), R*np.cos(t2), R*np.sin(t2), color="#f59f00", lw=4)
circ(3000, 1000, color="#1971c2", lw=4)
for z in (R, -R):
    ax.scatter([3000], [0], [z], color="yellow", edgecolor="k", s=40, zorder=5)

# etiquetas
ax.text(3000, -13500, 1500, "① arco del casco\nen x = 3000", color="#e8590c", fontsize=12, weight="bold")
ax.text(3000, 5600, -1000, "② el otro arco\ndel casco en x = 3000", color="#b07000", fontsize=12, weight="bold")
ax.text(3000, 1200, -3300, "③ circunferencia R1000\n(agujero)", color="#1971c2", fontsize=12, weight="bold")
ax.text(0, -5000, -6200, "NO: x = 0\n(unión con la esfera)", color="0.4", fontsize=10)
ax.text(6000, 4500, 3000, "NO: x = 6000", color="0.4", fontsize=10)
ax.text(4300, 0, 5500, "NO: líneas longitudinales", color="0.4", fontsize=10)

ax.set_box_aspect((11000, 16000, 10000))
ax.set_xlim(-5000, 6500); ax.set_ylim(-10000, 8000); ax.set_zlim(-5200, 5200)
ax.set_axis_off()
# triedro
for v, c, l in (((1500, 0, 0), "red", "X"), ((0, 1500, 0), "green", "Y"), ((0, 0, 1500), "blue", "Z")):
    ax.quiver(-5000, -5000, -5000, *v, color=c, arrow_length_ratio=0.25)
    ax.text(-5000+v[0]*1.25, -5000+v[1]*1.25, -5000+v[2]*1.25, l, color=c)
fig.suptitle("Boundary Surface → From Curves… para el mamparo M2 (x = 3000)\n"
             "Selecciona SOLO las curvas de color: ① + ② (contorno exterior, puede ser 1, 2 o 4 arcos) y ③ (agujero)",
             fontsize=13)
fig.text(0.5, 0.03, "Esquema ilustrativo, no captura de Femap. El número de arcos en que está partida la circunferencia depende de tu modelo:\n"
         "pasa el ratón por encima: cada arco se resalta por separado. Selecciónalos todos hasta cerrar la vuelta completa.",
         ha="center", fontsize=10, color="0.3")
fig.savefig("esquemas/seleccion_mamparo_m2.png", dpi=130, bbox_inches="tight")
