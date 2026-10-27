"""Hoja de fórmulas que da el profesor en el examen (2º parcial, 13-01-2026), solo las filas del 1er parcial.

Uso: python3 formulario_examen_profesor.py "../../parcial 1/14 - Formulario del profesor (hoja del examen).pdf"
"""
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "resumenes"))
from estilo import *

P("Oceanografía · Hoja de fórmulas del profesor", H1)
P("Transcrita del examen del 2º parcial (13-01-2026) · solo las filas que entran en el 1er parcial · teoría lineal de ondas", SUB)
note("Es la tabla que acompaña al enunciado en el examen. Las filas de <b>propagación</b> (ley de Snell, refracción K<sub>r</sub>, número de Iribarren y "
     "criterios de rotura de Michell, Yamada y Goda) son del 2º parcial y no aparecen aquí. He ordenado las columnas de menos a más profundidad; "
     "en la hoja original el orden es reducidas, profundas, intermedias.")

table(["Magnitud", "Reducidas", "Intermedias", "Profundas (indefinidas)"], [
    ["Profundidad relativa", "h/L &lt; 0,05", "0,05 &lt; h/L &lt; 0,5", "h/L &gt; 0,5"],
    ["Número de onda [m⁻¹]", "k = 2π/L = 2π/(T√(gh))", "k = 2π/L", "k₀ = 2π/L₀ = 4π²/(gT²)"],
    ["Término de profundidad δ", "—", "δ = k(z + h)", "—"],
    ["Fase φ", "φ = kx − ωt", "φ = kx − ωt", "φ₀ = k₀x − ωt"],
    ["<b>Relación de dispersión</b>", "<b>ω² = ghk²</b>", "<b>ω² = gk·tanh(kh)</b>", "<b>ω² = gk₀</b>"],
    ["Longitud de onda [m]", "L = T√(gh)", "L = L₀·tanh(kh)", "L₀ = gT²/2π"],
    ["Celeridad [m/s]", "C = √(gh)", "C = C₀·tanh(kh)", "C₀ = gT/2π"],
    ["<b>Celeridad de grupo</b> [m/s]", "C<sub>g</sub> = C = √(gh)", "C<sub>g</sub> = n·C,  n = ½·[1 + 2kh/sinh(2kh)]", "C<sub>g0</sub> = C₀/2"],
    ["Potencial de velocidades [m²/s]", "ϕ = (gH/2ω)·sin φ", "ϕ = (gH/2ω)·cosh(δ)/cosh(kh)·sin φ", "ϕ = (gH/2ω)·e<super>k₀z</super>·sin φ₀"],
    ["Superficie libre [m]", "η = (H/2)·cos φ", "η = (H/2)·cos φ", "η = (H/2)·cos φ₀"],
], [36, 38, 56, 40])

h3("Asomeramiento (vale en cualquier profundidad)")
fbox(["H₁²·C<sub>g,1</sub> = H₂²·C<sub>g,2</sub>   →   <b>H₂ = H₁·√(C<sub>g,1</sub>/C<sub>g,2</sub>)</b>   (K<sub>s</sub> = √(C<sub>g,1</sub>/C<sub>g,2</sub>))"])
terms([("H₁, H₂", "Altura de ola en los puntos 1 y 2 [m]"), ("C<sub>g,1</sub>, C<sub>g,2</sub>", "Celeridad de grupo en los puntos 1 y 2 [m/s]"),
       ("Hipótesis", "Se conserva el flujo de energía E·C<sub>g</sub>, sin refracción, rotura ni fricción")])

h3("Cosas a tener en cuenta de la hoja")
bl("La hoja original pone «Profundas: h/L &lt; 0,5». Es una errata: profundas es <b>h/L &gt; 0,5</b> (kh &gt; π).",
   "La hoja escribe la celeridad de grupo de intermedias como C<sub>g</sub> = (C/2)·n con n = 1 + 2kh/sinh(2kh). Es lo mismo que C<sub>g</sub> = n·C con n = ½·[1 + 2kh/sinh(2kh)].",
   "La hoja <b>no trae</b>: velocidades u y w, trayectorias, presiones, energía, Rayleigh, H<sub>max</sub> ni nada espectral. Eso tienes que llevarlo sabido "
   "(está en el formulario del 1er parcial, el 11, y en el compacto, el 12).",
   "El potencial ϕ da todo lo demás: u = ∂ϕ/∂x, w = ∂ϕ/∂z y la presión dinámica sale de −ρ·∂ϕ/∂t.")

build(sys.argv[1], "Oceanografía · Hoja de fórmulas del profesor (1er parcial) · Carlos Sánchez Campos", "Oceanografía — Hoja de fórmulas del profesor")
