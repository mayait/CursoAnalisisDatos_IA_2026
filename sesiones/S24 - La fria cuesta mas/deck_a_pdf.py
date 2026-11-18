# -*- coding: utf-8 -*-
"""Exporta el deck (copia local en deck/project) a PDF con Chrome sin cabeza. Uso: python deck_a_pdf.py [ids...]

Con ids exporta solo esas slides a deck/_prueba.pdf (para revisar). Sin ids, el deck completo a La-fria-cuesta-mas.pdf.
Las animaciones y los pasos quedan en su estado final.
"""
import json, re, subprocess, sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
PROJ = AQUI / "deck" / "project"
BLOBS = {k: AQUI / v for k, v in json.loads((AQUI / "deck" / "blobs.json").read_text()).items()}
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
deck = json.loads((PROJ / "deck.json").read_text(encoding="utf-8"))
fuentes = "".join(f'<link rel="stylesheet" href="{f["href"]}">' for f in deck["faces"].values() if "href" in f)
ids = sys.argv[1:] or deck["order"]


def formas(h):
    h = re.sub(r'<x-shape[^>]*kind="ellipse"[^>]*style="([^"]*)"></x-shape>', r'<div style="\1;border-radius:50%"></div>', h)
    h = re.sub(r'<x-shape[^>]*kind="arrow-right"[^>]*style="([^"]*)"></x-shape>', r'<div style="\1;clip-path:polygon(0 30%,60% 30%,60% 0,100% 50%,60% 100%,60% 70%,0 70%)"></div>', h)
    return h


partes = []
for sid in ids:
    html = (PROJ / "slides" / f"{sid}.html").read_text(encoding="utf-8")
    html = re.sub(r"<aside>.*?</aside>", "", html, flags=re.S)
    html = re.sub(r"/_blob/([0-9a-f]{32})", lambda m: BLOBS[m.group(1)].as_uri(), html)
    partes.append(formas(html))
css = (PROJ / "deck.css").read_text(encoding="utf-8")
doc = f"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><title>{deck['title']}</title>{fuentes}
<style>
@page {{ size: 1920px 1080px; margin: 0 }}
html, body {{ margin: 0; padding: 0; background: #fff }}
* {{ box-sizing: border-box; margin: 0 }}
section {{ position: relative; width: 1920px; height: 1080px; overflow: hidden; page-break-after: always; break-after: page }}
h1, h2, h3 {{ font-size: inherit }}
table {{ border-collapse: collapse }}
td, th {{ padding: 0.35em 0.6em; border-bottom: 2px solid #D9D9D9; text-align: left }}
{css}
.sube, .aparece, .crece {{ animation: none !important }}
.fragment {{ opacity: 1 !important; transform: none !important }}
</style></head><body>{''.join(partes)}</body></html>"""
tmp = AQUI / "deck" / "_imprimir.html"
tmp.write_text(doc, encoding="utf-8")
salida = AQUI / ("La-fria-cuesta-mas.pdf" if not sys.argv[1:] else "deck/_prueba.pdf")
subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--allow-file-access-from-files", "--virtual-time-budget=15000", f"--print-to-pdf={salida}", tmp.as_uri()], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print(salida, len(ids), "slides")
