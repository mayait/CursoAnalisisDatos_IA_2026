# -*- coding: utf-8 -*-
"""Renderiza las tomas en paralelo. Uso: python render_serie.py carpeta_media [--borrador] [hilos] [id id ...]"""
import os
import shutil
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import guion

AQUI = Path(__file__).resolve().parent
args = sys.argv[1:]
media = Path(args.pop(0))
borrador = "--borrador" in args
if borrador:
    args.remove("--borrador")
seco = "--seco" in args  # solo mide los tiempos, sin escribir video
if seco:
    args.remove("--seco")
hilos = int(args.pop(0)) if args and args[0].isdigit() else 8
ids = args or guion.ids()
destino = AQUI / ("tomas_borrador" if borrador else "tomas")
destino.mkdir(exist_ok=True)


def uno(sid):
    calidad = ["-ql"] if borrador else ["-r", "1920,1080", "--fps", "30"]
    if seco:
        calidad.append("--dry_run")
    m = media / sid
    r = subprocess.run(["manim", *calidad, "--media_dir", str(m), "--disable_caching", "-v", "WARNING", "--progress_bar", "none", "serie_escenas.py", "Toma"], cwd=AQUI,
                       env={**os.environ, "SHOT": sid}, capture_output=True, text=True)
    if r.returncode:
        return f"{sid} ERROR\n" + "\n".join(l for l in r.stdout.splitlines()[-25:])
    if seco:
        return f"{sid} ok"
    shutil.copy(next(m.glob("videos/serie_escenas/*/Toma.mp4")), destino / f"{sid}.mp4")
    return f"{sid} ok"


with ThreadPoolExecutor(hilos) as ex:
    for msg in ex.map(uno, ids):
        print(msg, flush=True)
