"""Cálculos analíticos de referencia para la tarea MEF del submarino (UPM, 2026-27).

Unidades coherentes: mm, N, MPa (N/mm^2), t, s.
Estos valores sirven para comprobar el orden de magnitud del modelo de Femap;
no lo sustituyen. Las hipótesis de interpretación están en README.md.

Ejecutar:  python3 calculos_analiticos.py
"""
import math

# ---------------------------------------------------------------- datos
E = 210000.0      # MPa (HY80: 207000 MPa; la diferencia es <2 %)
nu = 0.30
sy = 550.0        # MPa; HY80 = 80 ksi = 552 MPa; HS56 ~ 56 kp/mm2 = 549 MPa
rho_w = 1.025e-9  # t/mm3, agua de mar
g = 9810.0        # mm/s2
H = 250e3         # mm de profundidad

R = 5000.0        # radio de la superficie media del cilindro (se toma el "radio máximo")
t = 35.0          # casco
Lc = 15000.0      # eslora del cilindro
Lk = 6000.0       # eslora del tronco de cono
r2 = 2500.0       # radio final del cono = radio de la semiesfera de popa
s = 3000.0        # separación de cuadernas en el cilindro (5 cuadernas: x = 0, 3000, ... 12000)
LB = 12000.0      # distancia entre mamparos 2 (x=3000) y 1 (x=15000)
tb = 25.0         # mamparos
td = 20.0         # cubierta

# Cuaderna en T 150x150x15 (alma 150 x 15 + ala 150 x 15), por el interior
hw, tw, bf, tf = 150.0, 15.0, 150.0, 15.0

p = rho_w * g * H
out = []
def w(line=""):
    out.append(line)

w("=== CÁLCULOS ANALÍTICOS DE REFERENCIA — SUBMARINO A 250 m ===")
w(f"Presión exterior p = rho*g*h = {p:.4f} MPa  ({p*10:.2f} bar)")
w(f"Variación hidrostática entre quilla y cubierta (10 m): {rho_w*g*2*R:.4f} MPa "
  f"({rho_w*g*2*R/p*100:.1f} % de p) -> se puede usar p uniforme")
w()

# ---------------------------------------------------------------- geometría
alpha = math.atan((R - r2) / Lk)
V_h1 = 2/3 * math.pi * R**3
V_c = math.pi * R**2 * Lc
V_k = math.pi * Lk / 3 * (R**2 + R*r2 + r2**2)
V_h2 = 2/3 * math.pi * r2**3
V = V_h1 + V_c + V_k + V_h2
w("--- Geometría")
w(f"Eslora total = {R + Lc + Lk + r2:.0f} mm")
w(f"Semiángulo del cono alpha = {math.degrees(alpha):.2f} grados; generatriz = {math.hypot(Lk, R-r2):.1f} mm")
w(f"Volumen encerrado = {V/1e9:.1f} m3 (semiesfera proa {V_h1/1e9:.1f}, cilindro {V_c/1e9:.1f}, "
  f"cono {V_k/1e9:.1f}, semiesfera popa {V_h2/1e9:.1f})")
w()

# ---------------------------------------------------------------- tensiones de membrana
w("--- Tensiones de membrana (lejos de uniones, cuadernas y huecos); compresión")
sc_th = p*R/t; sc_x = p*R/(2*t)
vm = lambda a, b: math.sqrt(a*a - a*b + b*b)
w(f"Cilindro:   sigma_theta = pR/t = {sc_th:.1f}   sigma_x = pR/2t = {sc_x:.1f}   "
  f"von Mises = {vm(sc_th, sc_x):.1f} MPa  (ratio sy/vm = {sy/vm(sc_th, sc_x):.2f})")
ss = p*R/(2*t)
w(f"Semiesfera proa (R=5000): sigma = pR/2t = {ss:.1f} MPa (von Mises = {ss:.1f})")
w(f"Semiesfera popa (R=2500): sigma = pR/2t = {p*r2/(2*t):.1f} MPa")
for r in (R, (R + r2)/2, r2):
    th = p*r/(t*math.cos(alpha)); me = p*r/(2*t*math.cos(alpha))
    w(f"Cono r={r:.0f}: sigma_theta = pr/(t cos a) = {th:.1f}  sigma_meridiano = {me:.1f}  von Mises = {vm(th, me):.1f} MPa")
# fuerza que la unión cilindro-cono debe absorber (componente radial de la membrana del cono)
Nm = p*R/(2*math.cos(alpha))
w(f"Unión cilindro-cono: empuje radial de la membrana del cono = N_mer*sin(a) = {Nm*math.sin(alpha):.0f} N/mm "
  "-> flexión local alta: revisar tensiones Top/Bottom en x=15000")
w()

# ---------------------------------------------------------------- cuaderna
A_f = hw*tw + bf*tf
w("--- Cuadernas T 150x150x15")
w(f"Área de la T = {A_f:.0f} mm2 frente a s*t = {s*t:.0f} mm2 de chapa por vano -> rigidizado muy ligero")
sig_f = p*R*s/(A_f + s*t)
w(f"Tensión circunferencial media (reparto por igual deformación) ~ {sig_f:.0f} MPa")
w()

# ---------------------------------------------------------------- cambio dimensional
w("--- Cambio dimensional (membrana, sin cuadernas ni mamparos: cota superior)")
k = p/(E*t)
w_c = k*R**2*(1 - nu/2)            # radial cilindro (hacia dentro)
ex_c = -k*R*(0.5 - nu)             # deformación axial cilindro
w_h1 = k*R**2*(1 - nu)/2           # radial semiesfera
w_h2 = k*r2**2*(1 - nu)/2
w(f"Cilindro: w radial = pR^2(1-nu/2)/(Et) = {w_c:.2f} mm hacia dentro "
  f"-> diámetro {2*R:.0f} -> {2*R-2*w_c:.1f} mm (Delta D = -{2*w_c:.1f} mm)")
w(f"Cilindro: eps_x = -pR(1/2-nu)/(Et) = {ex_c:.3e} -> Delta L = {ex_c*Lc:.2f} mm")
w(f"Semiesferas: w = pR^2(1-nu)/(2Et) = {w_h1:.2f} mm (proa), {w_h2:.2f} mm (popa)")
# cono: integración de las deformaciones meridionales
n = 2000; dL = 0.0; dV_k = 0.0
ds = math.hypot(Lk, R - r2)/n
def cone_strains(r):
    sth = -p*r/(t*math.cos(alpha)); sme = -p*r/(2*t*math.cos(alpha))
    return (sme - nu*sth)/E, (sth - nu*sme)/E
for i in range(n):
    r = R - (R - r2)*(i + 0.5)/n
    e_me, e_th = cone_strains(r)
    # u_r = r*e_th;  e_me = u_x' cos(a) - u_r' sin(a)  (s medido hacia popa, r decreciente)
    ra, rb = r + 0.5*(R - r2)/n, r - 0.5*(R - r2)/n
    dur = rb*cone_strains(rb)[1] - ra*cone_strains(ra)[1]
    dL += (e_me*ds + dur*math.sin(alpha))/math.cos(alpha)
    # volumen: dV = (2*e_th + e_x) * dV_elemental, con e_x = du_x/dx
    e_x = (e_me*ds + dur*math.sin(alpha))/math.cos(alpha)/(ds*math.cos(alpha))
    dV_k += (2*e_th + e_x) * math.pi * r**2 * ds*math.cos(alpha)
dL_total = ex_c*Lc + dL - w_h1 - w_h2
w(f"Cono: cambio de longitud axial aprox. = {dL:+.2f} mm (la contracción radial, mayor en la base grande, lo alarga)")
w(f"Eslora total: Delta L ~ {dL_total:.1f} mm  (cilindro + cono + retroceso de los dos polos)")
dV = ((2*(-w_c/R) + ex_c)*V_c + 3*(-w_h1/R)*V_h1 + 3*(-w_h2/r2)*V_h2 + dV_k)
w(f"Delta V ~ {dV/1e9:.2f} m3 ({dV/V*100:.2f} % del volumen) -> pérdida de empuje ~ {-dV/1e9*1.025:.2f} t")
w()

# ---------------------------------------------------------------- pandeo
w("--- Pandeo (elástico, lineal; comparar con los autovalores de SOL 105)")
def interframe(Rr, tt, L, nmax=60):
    lam = math.pi*Rr/L
    best = None
    for nn in range(2, nmax):
        num = lam**4/(nn**2 + lam**2)**2 + tt**2/(12*Rr**2*(1 - nu**2))*(nn**2 + lam**2)**2
        pc = E*tt/Rr*num/(nn**2 - 1 + 0.5*lam**2)
        if best is None or pc < best[0]:
            best = (pc, nn)
    return best

pc, nlob = interframe(R, t, s)
wt = 2.42*E*(t/(2*R))**2.5/((1 - nu**2)**0.75*(s/(2*R) - 0.45*(t/(2*R))**0.5))
w(f"Entre cuadernas, cilindro (von Mises, L=s=3000): p_cr = {pc:.3f} MPa con n = {nlob} lóbulos "
  f"-> lambda = {pc/p:.3f} -> {pc/p*250:.0f} m")
w(f"   (Windenburg-Trilling aproximada: {wt:.3f} MPa)")
w(f"   Tensión de pandeo p_cr R/t = {pc*R/t:.0f} MPa < sy -> elástico")
# cono: cilindro equivalente
r_eq = ((R + r2)/2)/math.cos(alpha)
for Lbay, lab in ((3000/math.cos(alpha), "con cuaderna en x=18000"), (Lk/math.cos(alpha), "sin cuaderna")):
    pk, nk = interframe(r_eq, t, Lbay)
    w(f"Cono (cilindro equivalente R={r_eq:.0f}, L={Lbay:.0f}, {lab}): p_cr ~ {pk:.3f} MPa, n={nk} -> lambda ~ {pk/p:.2f}")
# esferas
for Rs, lab in ((R, "proa R=5000"), (r2, "popa R=2500")):
    pcl = 2*E/math.sqrt(3*(1 - nu**2))*(t/Rs)**2
    w(f"Semiesfera {lab}: clásico p_cr = {pcl:.2f} MPa (lambda={pcl/p:.2f}); "
      f"con factor 0.3 por imperfecciones ~ {0.3*pcl:.2f} MPa")
# inestabilidad general (Bryant) con chapa colaborante
Le = min(s, 1.56*math.sqrt(R*t))
parts = [(Le*t, 0.0, Le*t**3/12),
         (hw*tw, t/2 + hw/2, tw*hw**3/12),
         (bf*tf, t/2 + hw + tf/2, bf*tf**3/12)]
A = sum(a for a, _, _ in parts); zc = sum(a*z for a, z, _ in parts)/A
Ie = sum(i + a*(z - zc)**2 for a, z, i in parts)
Rc = R - zc
lamB = math.pi*R/LB
gi = []
for nn in range(2, 12):
    pn = E*t/R*lamB**4/((nn**2 + lamB**2/2 - 1)*(nn**2 + lamB**2)**2) + (nn**2 - 1)*E*Ie/(Rc**3*s)
    gi.append((pn, nn))
pg, ng = min(gi)
w(f"Inestabilidad general (Bryant, L_mamparos={LB:.0f}, chapa colaborante {Le:.0f} mm, "
  f"I_e={Ie/1e6:.1f}e6 mm4): p_cr = {pg:.2f} MPa con n={ng} -> lambda = {pg/p:.2f}")
w()

# ---------------------------------------------------------------- mamparos y cubierta
w("--- Mamparos planos y cubierta (aviso para interpretar SOL 105)")
D = E*tb**3/(12*(1 - nu**2))
beta = (3*(1 - nu**2))**0.25/math.sqrt(R*t)
kb = E*tb/(R*(1 - nu))
Q = w_c/(beta*R**2/(2*E*t) + 1/kb)
w(f"Empuje radial del casco sobre el borde del mamparo de R=5000: q ~ {Q:.0f} N/mm "
  f"-> compresión en su plano ~ {Q/tb:.0f} MPa")
for kk, lab in ((4.20, "borde apoyado"), (14.68, "borde empotrado")):
    Ncr = kk*D/R**2
    w(f"Pandeo de placa circular 25 mm, R=5000, {lab}: N_cr = {Ncr:.0f} N/mm -> lambda ~ {Ncr/Q:.2f}")
w("=> Es de esperar que los PRIMEROS modos de SOL 105 sean de los mamparos planos sin refuerzos")
w("   (y quizá de la cubierta), con lambda << 1, antes que los modos del casco.")
Dd = E*td**3/(12*(1 - nu**2))
w(f"Cubierta 20 mm entre baos (b=3000): sigma_cr placa (k=4) = {4*math.pi**2*Dd/(s**2*td):.1f} MPa "
  f"frente a la compresión axial del casco ~ {abs(ex_c)*E:.0f} MPa + compresión transversal")

text = "\n".join(out)
print(text)
if __name__ == "__main__":
    import pathlib
    pathlib.Path(__file__).with_name("resultados_analiticos.txt").write_text(text + "\n", encoding="utf-8")
