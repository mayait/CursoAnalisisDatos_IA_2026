# -*- coding: utf-8 -*-
"""Prepara los clips con voz que van dentro del deck: toma + audio + 40 segundos de cuadro final para comentar antes de que vuelva a empezar.

Uso: python clips_deck.py  -> ../deck_clips/<id>.mp4 y su póster, y ../deck_clips/duraciones.json
"""
import json
import subprocess
from pathlib import Path

import numpy as np
import wave

import guion
import montar
import voces

AQUI = Path(__file__).resolve().parent
OUT = AQUI.parent / "deck_clips"
OUT.mkdir(exist_ok=True)
COLA = 40
TOMAS = ["E01-3", "E01-4", "E02-1", "E02-2", "E02A-1", "E02A-2", "E02B-1", "E02B-2", "E02B-3", "E02B-4", "E02C-1", "E02C-3", "E02C-4", "E02C-5", "E02F-1", "E02E-2",
         "E04-1", "E04-2", "E04-3", "E04-4", "E02E-1", "E05-2", "E05-3", "E05-4", "E06-1", "E06-2", "E06-3", "E07-1", "E07-2", "E08-2", "E09-1", "E09-2", "E10-6", "E10-2", "E10-3", "E10-5"]
EPISODIOS = {"E02D": "E02D-interacciones-en-python.mp4", "E03": "E03-ejercicio-corrijan-la-promesa.mp4", "E08": "E08-ejercicio-contesten-la-oferta.mp4"}
dur = {}


def poner_cola(entrada_v, entrada_a, salida):
    v = ["-vf", f"tpad=stop_mode=clone:stop_duration={COLA}", "-c:v", "libx264", "-preset", "medium", "-crf", "21", "-pix_fmt", "yuv420p", "-r", "30"]
    a = ["-af", f"loudnorm=I=-16:TP=-1.5:LRA=9,apad=pad_dur={COLA}", "-ar", "48000", "-c:a", "aac", "-b:a", "128k"]
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(entrada_v), "-i", str(entrada_a), "-map", "0:v:0", "-map", "1:a:0", *v, *a, "-shortest", "-movflags", "+faststart", str(salida)], check=True)


def poster(mp4, png, t):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(t), "-i", str(mp4), "-frames:v", "1", "-update", "1", str(png)], check=True)


for sid in TOMAS:
    e, t = guion.toma_por_id(sid)
    v = AQUI / "tomas" / f"{sid}.mp4"
    d = montar.duracion_video(v)
    ini = json.loads((AQUI / "tiempos" / f"{sid}.json").read_text())["inicios"]
    audio = np.zeros(int(d * montar.RATE) + 2, np.float32)
    for b, i in zip(t["beats"], ini):
        x = montar.leer(voces.destino(b["voz"], b["texto"]))
        a = int(i * montar.RATE)
        audio[a:a + len(x)] += x[: len(audio) - a]
    w_ = OUT / f".{sid}.wav"
    with wave.open(str(w_), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(montar.RATE); w.writeframes(np.clip(audio, -32768, 32767).astype(np.int16).tobytes())
    poner_cola(v, w_, OUT / f"{sid}.mp4")
    w_.unlink()
    poster(OUT / f"{sid}.mp4", OUT / f"{sid}.png", d + 1)
    dur[sid] = round(d, 1)
    print(sid, round(d, 1), flush=True)
for k, f in EPISODIOS.items():
    v = AQUI / "videos" / f
    d = montar.duracion_video(v)
    poner_cola(v, v, OUT / f"{k}.mp4")
    poster(OUT / f"{k}.mp4", OUT / f"{k}.png", 9)
    dur[k] = round(d, 1)
(OUT / "duraciones.json").write_text(json.dumps(dur, indent=0))
print("total", round(sum(dur.values()) / 60, 1), "min")
