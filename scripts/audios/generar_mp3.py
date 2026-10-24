"""Convierte los guiones de audio (.md) en MP3 con una voz española offline (Piper).

Uso: python3 generar_mp3.py VOZ.onnx guion1.md [guion2.md ...]
El MP3 se escribe junto al guion, con el mismo nombre.
Voz usada: es-mls_10246-low (github.com/rhasspy/piper, release v0.0.2).
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path


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
    return "\n".join(lineas)


def main():
    voz = sys.argv[1]
    for ruta in map(Path, sys.argv[2:]):
        texto = limpiar(ruta.read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as tmp:
            wav = Path(tmp) / "a.wav"
            subprocess.run(
                [sys.executable, "-m", "piper", "-m", voz, "-f", str(wav),
                 "--noise-w-scale", "0.5", "--sentence-silence", "0.35"],
                input=texto.encode("utf-8"), check=True)
            mp3 = ruta.with_suffix(".mp3")
            subprocess.run(
                ["ffmpeg", "-y", "-loglevel", "error", "-i", str(wav),
                 "-af", "silenceremove=stop_periods=-1:stop_duration=1.2:stop_threshold=-45dB:stop_silence=0.6",
                 "-ac", "1", "-b:a", "48k", str(mp3)], check=True)
        print(mp3)


if __name__ == "__main__":
    main()
