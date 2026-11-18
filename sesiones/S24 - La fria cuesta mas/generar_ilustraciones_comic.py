# -*- coding: utf-8 -*-
"""Ilustraciones nuevas del deck en el estilo de cómic pop de las viñetas del simulador (gpt-image-2).

Uso: python generar_ilustraciones_comic.py   (lee OPENAI_API_KEY del .env de la raíz; nunca la imprime)
"""
import base64, json, sys, urllib.error, urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[1]
PREFIJO = ("Bold pop-art comic book illustration: thick uniform black ink outlines, flat saturated colors, solid black block "
           "shadows, halftone dot texture in the shadows, radial speed lines in the background, slight printed-paper grain. "
           "Palette dominated by vermilion red, with deep petrol blue, bottle green, ochre yellow and cream. Medium shot, strong "
           "expressive faces, Peruvian people with warm brown skin tones. Energy drink bottles are plain colored glass bottles "
           "with blank labels. Absolutely no text, no letters, no numbers, no logos, no signage, no speech bubbles. Scene: ")
ESCENAS = [
    {"nombre": "n1-portada", "tamano": "1024x1536", "escena": "inside a small Peruvian neighborhood corner shop (bodega), a friendly middle-aged shopkeeper in an ochre apron pulls a frosty ice-cold glass bottle covered in frost and water droplets out of a red refrigerator full of colorful bottles; through the open door behind him a sun-drenched hot street in yellow light and a sweating customer wiping his forehead."},
    {"nombre": "n2-equipo", "tamano": "1536x1024", "escena": "four university students in their twenties working together as a team around one laptop at a table; the laptop screen shows a scatter cloud of colorful dots; one student points at the screen, another stamps a paper with a rubber stamp, a third holds a calculator and coins, the fourth writes in a notebook; concentrated and excited."},
    {"nombre": "n3-recta", "tamano": "1536x1024", "escena": "close view of a hand holding a thick red marker drawing one straight diagonal line across a large whiteboard completely covered with a messy cloud of small multicolored dots; a young woman in a red blazer, seen from the side, draws the line with determination."},
    {"nombre": "n4-cierre", "tamano": "1024x1536", "escena": "a confident young Peruvian woman brand manager in a red blazer with her dark hair in a bun stands in front of a boardroom table holding a single sheet of paper; five different colored glass bottles stand in a row on the table; silhouettes of executives listening; city skyline at sunset through the window."},
]


def clave():
    for l in (RAIZ / ".env").read_text().splitlines():
        if l.startswith("OPENAI_API_KEY="):
            return l.split("=", 1)[1].strip().strip("\"'")
    sys.exit("Falta OPENAI_API_KEY")


def generar(e, key):
    destino = AQUI / "arte" / f"{e['nombre']}.png"
    if destino.exists():
        return f"{e['nombre']}: ya existe"
    cuerpo = json.dumps({"model": "gpt-image-2", "prompt": PREFIJO + e["escena"], "size": e["tamano"], "quality": "high", "n": 1}).encode()
    req = urllib.request.Request("https://api.openai.com/v1/images/generations", data=cuerpo, headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=900) as r:
            datos = json.load(r)
    except urllib.error.HTTPError as err:
        return f"{e['nombre']}: error {err.code} {err.read()[:300].decode(errors='replace')}"
    destino.write_bytes(base64.b64decode(datos["data"][0]["b64_json"]))
    return f"{e['nombre']}: ok"


if __name__ == "__main__":
    key = clave()
    with ThreadPoolExecutor(4) as ex:
        for m in ex.map(lambda e: generar(e, key), ESCENAS):
            print(m, flush=True)
