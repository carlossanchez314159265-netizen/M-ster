"""Convierte los guiones de audio (.md) en MP3 con una voz española offline (Piper).

Uso: python3 generar_mp3.py VOZ.onnx guion1.md [guion2.md ...]
El MP3 se escribe junto al guion, con el mismo nombre.

Voz usada: es_ES-davefx-medium (22 kHz). Se descarga de las versiones de sherpa-onnx en GitHub:
  https://github.com/k2-fsa/sherpa-onnx/releases/download/tts-models/vits-piper-es_ES-davefx-medium.tar.bz2
y necesita `pip install piper-tts`. La voz anterior (es-mls_10246-low, 16 kHz) se entendía bastante peor:
en una prueba con Whisper sobre 30 frases de los guiones fallaba el 36 % de las palabras, frente al 13 % de esta.
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

# Términos que la voz española lee mal: se reescriben como suenan (solo en el audio, el guion no cambia).
PRONUNCIACION = [
    (r"\bswell\b", "suel"),
    (r"(?<=\b(?:el|un|de|es) )sea\b|\bsea(?= y suel)", "si"),
    (r"\bRayleigh\b", "Réilei"),
    (r"\bPierson\b", "Píerson"),
    (r"\bMoskowitz\b", "Moscóvits"),
    (r"\bfetch\b", "fech"),
    (r"\bJONSWAP\b", "yónsuap"),
    (r"\bWelch\b", "Uelch"),
    (r"\brun-?up\b", "ránap"),
    (r"\bfreak\b", "fric"),
    (r"\bwaves\b", "ueivs"),
    (r"\bwave\b", "ueiv"),
    (r"\bEuler\b", "Óiler"),
    (r"\bFourier\b", "Furié"),
    (r"\bAiry\b", "Éri"),
    (r"\bNewton\b", "Niúton"),
    (r"\bRaphson\b", "Ráfson"),
    (r"\boffshore\b", "ofchor"),
    (r"\bseiches\b", "seches"),
    (r"\bLaplace\b", "Laplás"),
    (r"\bBernoulli\b", "Bernúli"),
    (r"\bFFT\b", "efe efe te"),
    (r"\bTEOS\b", "Teos"),
    (r"\bMP3\b", "eme pe tres"),
]


def limpiar(md: str) -> str:
    lineas = []
    for linea in md.splitlines():
        s = linea.strip()
        if s.startswith("*") and s.endswith("*") and len(s) > 2:
            continue  # nota en cursiva bajo el título (instrucciones de uso)
        s = re.sub(r"^#+\s*", "", s)
        s = s.replace("**", "").replace("*", "")
        s = s.replace("—", ", ").replace("–", ", ")
        if s and not s.endswith((".", ":", "?", "!")):
            s += "."  # títulos: pausa al final
        lineas.append(s)
    texto = "\n".join(lineas)
    for patron, sonido in PRONUNCIACION:
        texto = re.sub(patron, sonido, texto, flags=re.IGNORECASE)
    return texto


def main():
    voz = sys.argv[1]
    for ruta in map(Path, sys.argv[2:]):
        texto = limpiar(ruta.read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmp:
            wav = Path(tmp) / "a.wav"
            subprocess.run(
                [sys.executable, "-m", "piper", "-m", voz, "-f", str(wav), "--sentence-silence", "0.35"],
                input=texto.encode("utf-8"), check=True)
            mp3 = ruta.with_suffix(".mp3")
            subprocess.run(
                ["ffmpeg", "-y", "-loglevel", "error", "-i", str(wav),
                 "-af", "silenceremove=stop_periods=-1:stop_duration=1.2:stop_threshold=-45dB:stop_silence=0.6",
                 "-ac", "1", "-ar", "22050", "-b:a", "64k", str(mp3)], check=True)
        print(mp3)


if __name__ == "__main__":
    main()
