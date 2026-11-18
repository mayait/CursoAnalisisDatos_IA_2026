# -*- coding: utf-8 -*-
"""Ilustraciones collage Galápagos con la API de OpenAI (gpt-image-2), estilo del skill ilustraciones-collage-galapagos.

Uso:
  .venv/bin/python scripts/generar_ilustraciones.py escenas.json carpeta_salida
escenas.json: [{"nombre": "portada", "tamano": "1536x1024", "escena": "..."}]
La clave se lee de OPENAI_API_KEY o del archivo .env de la raíz (ignorado por git). Nunca se imprime.
"""
import base64
import json
import os
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

PREFIJO = ("Contemporary editorial illustration made of hand-painted gouache and cut-paper collage, visible paper grain "
           "and slightly torn edges, flat shapes with soft texture, bold warm palette of sunflower yellow, cobalt blue, "
           "coral orange-red, soft lavender, cream and deep navy, a few leafy plant cutouts. Friendly expressive characters "
           "with warm brown and olive skin tones, Latin American people. Setting: the Galápagos Islands, San Cristóbal. "
           "Absolutely no text, no letters, no numbers, no logos, no signage. Scene: ")
RAIZ = Path(__file__).resolve().parents[1]


def clave():
    if os.environ.get("OPENAI_API_KEY"):
        return os.environ["OPENAI_API_KEY"]
    for linea in (RAIZ / ".env").read_text().splitlines():
        if linea.startswith("OPENAI_API_KEY="):
            return linea.split("=", 1)[1].strip()
    sys.exit("Falta OPENAI_API_KEY en .env")


def generar(e, salida, key):
    destino = salida / f"{e['nombre']}.png"
    if destino.exists():
        return f"{e['nombre']}: ya existe"
    cuerpo = json.dumps({"model": "gpt-image-2", "prompt": PREFIJO + e["escena"], "size": e["tamano"],
                         "quality": "high", "n": 1}).encode()
    req = urllib.request.Request("https://api.openai.com/v1/images/generations", data=cuerpo,
                                 headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=600) as r:
            datos = json.load(r)
    except urllib.error.HTTPError as err:
        return f"{e['nombre']}: error {err.code} {err.read()[:300].decode(errors='replace')}"
    destino.write_bytes(base64.b64decode(datos["data"][0]["b64_json"]))
    return f"{e['nombre']}: ok"


if __name__ == "__main__":
    escenas = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    salida = Path(sys.argv[2]); salida.mkdir(parents=True, exist_ok=True)
    key = clave()
    with ThreadPoolExecutor(max_workers=7) as ex:
        for msg in ex.map(lambda e: generar(e, salida, key), escenas):
            print(msg, flush=True)
