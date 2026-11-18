# -*- coding: utf-8 -*-
"""Monta cada episodio: une las tomas, coloca cada frase en su instante y escribe los subtítulos.

Uso: python montar.py [E01 E02 ...]  -> videos/E01-la-promesa.mp4 y su .srt
"""
import json
import re
import subprocess
import sys
import wave
from pathlib import Path

import numpy as np

import guion
import voces

AQUI = Path(__file__).resolve().parent
TOMAS = AQUI / "tomas"
OUT = AQUI / "videos"
OUT.mkdir(exist_ok=True)
RATE = 24000


def leer(p):
    with wave.open(str(p)) as w:
        assert w.getframerate() == RATE, p
        return np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32)


def duracion_video(p):
    return float(subprocess.check_output(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)]).strip())


def hhmmss(t):
    ms = int(round(t * 1000))
    return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


def frases(texto):
    return [f.strip() for f in re.split(r"(?<=[.?!:])\s+", texto) if f.strip()]


def montar(e):
    salida = OUT / f"{e['id']}-{e['slug']}.mp4"
    offset = 0.0
    total, srt, lista = [], [], []
    pistas = []
    for i, t in enumerate(e["tomas"]):
        sid = f"{e['id']}-{i}"
        v = TOMAS / f"{sid}.mp4"
        d = duracion_video(v)
        inicios = json.loads((AQUI / "tiempos" / f"{sid}.json").read_text())["inicios"]
        lista.append(f"file '{v}'")
        for b, ini in zip(t["beats"], inicios):
            p = voces.destino(b["voz"], b["texto"])
            x = leer(p)
            pistas.append((offset + ini, x))
            dur = len(x) / RATE
            trozos = frases(b["texto"])
            pesos = np.array([len(f) for f in trozos], float)
            c = offset + ini
            for f, w in zip(trozos, pesos / pesos.sum()):
                srt.append((c, c + dur * w, f))
                c += dur * w
        offset += d
    audio = np.zeros(int(offset * RATE) + RATE, np.float32)
    for ini, x in pistas:
        a = int(ini * RATE)
        audio[a:a + len(x)] += x[: len(audio) - a]
    audio = np.clip(audio, -32768, 32767).astype(np.int16)
    tmp_wav, tmp_list = OUT / f".{e['id']}.wav", OUT / f".{e['id']}.txt"
    with wave.open(str(tmp_wav), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(RATE); w.writeframes(audio[: int(offset * RATE)].tobytes())
    tmp_list.write_text("\n".join(lista))
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(tmp_list), "-i", str(tmp_wav), "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy",
                    "-af", "loudnorm=I=-16:TP=-1.5:LRA=9", "-ar", "48000", "-c:a", "aac", "-b:a", "160k", "-movflags", "+faststart", "-shortest", str(salida)], check=True)
    tmp_wav.unlink(); tmp_list.unlink()
    salida.with_suffix(".srt").write_text("".join(f"{i}\n{hhmmss(a)} --> {hhmmss(b)}\n{t}\n\n" for i, (a, b, t) in enumerate(srt, 1)), encoding="utf-8")
    print(salida.name, f"{offset / 60:.1f} min", salida.stat().st_size // 1048576, "MB", flush=True)


if __name__ == "__main__":
    elegidos = set(sys.argv[1:])
    for e in guion.EPISODIOS:
        if not elegidos or e["id"] in elegidos:
            montar(e)
