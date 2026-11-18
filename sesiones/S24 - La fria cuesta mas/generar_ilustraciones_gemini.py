# -*- coding: utf-8 -*-
"""Ilustraciones nuevas del deck con Gemini (imagen), usando una viñeta del simulador como referencia de estilo.

Uso: python generar_ilustraciones_gemini.py   (lee GEMINI_API_KEY del .env de la raíz; nunca la imprime)
"""
import base64, json, sys, time, urllib.error, urllib.request
from pathlib import Path

from generar_ilustraciones_comic import ESCENAS, PREFIJO

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[1]
MODELOS = ["gemini-3-pro-image", "gemini-3.1-flash-image", "gemini-2.5-flash-image"]
REF = AQUI / "arte" / "comic_operativo.png"
RAZON = {"1024x1536": "2:3", "1536x1024": "3:2"}


def clave():
    for l in (RAIZ / ".env").read_text().splitlines():
        if l.startswith("GEMINI_API_KEY="):
            return l.split("=", 1)[1].strip().strip("\"'")
    sys.exit("Falta GEMINI_API_KEY")


def generar(e, key):
    destino = AQUI / "arte" / f"{e['nombre']}.png"
    if destino.exists():
        return f"{e['nombre']}: ya existe"
    partes = [{"inlineData": {"mimeType": "image/png", "data": base64.b64encode(REF.read_bytes()).decode()}},
              {"text": "Use the attached image ONLY as the art style reference (same ink line, palette and texture). Draw a NEW image. " + PREFIJO + e["escena"]}]
    for modelo in MODELOS:
        cuerpo = json.dumps({"contents": [{"parts": partes}], "generationConfig": {"responseModalities": ["IMAGE"], "imageConfig": {"aspectRatio": RAZON[e["tamano"]]}}}).encode()
        for intento in range(3):
            req = urllib.request.Request(f"https://generativelanguage.googleapis.com/v1beta/models/{modelo}:generateContent", data=cuerpo, headers={"x-goog-api-key": key, "Content-Type": "application/json"})
            try:
                with urllib.request.urlopen(req, timeout=300) as r:
                    d = json.load(r)
                for p in d["candidates"][0]["content"]["parts"]:
                    if "inlineData" in p:
                        destino.write_bytes(base64.b64decode(p["inlineData"]["data"]))
                        return f"{e['nombre']}: ok con {modelo}"
                break
            except urllib.error.HTTPError as err:
                msg = err.read()[:200].decode(errors="replace").replace("\n", " ")
                print(f"  {e['nombre']} {modelo}: {err.code} {msg}", flush=True)
                if err.code in (500, 502, 503, 504):
                    time.sleep(10); continue
                break
            except Exception as ex:  # noqa: BLE001
                print(f"  {e['nombre']} {modelo}: {type(ex).__name__}", flush=True); time.sleep(5)
    return f"{e['nombre']}: no se pudo"


if __name__ == "__main__":
    key = clave()
    for e in ESCENAS:
        print(generar(e, key), flush=True)
