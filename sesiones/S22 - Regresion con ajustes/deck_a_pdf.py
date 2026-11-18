# -*- coding: utf-8 -*-
"""Convierte el deck (deck/project) a PDF con Chrome sin cabeza, una slide por página de 1920x1080.

Uso: python deck_a_pdf.py  -> Una-recta-no-se-dobla.pdf. Los videos quedan como su último cuadro.
"""
import json
import re
import subprocess
from pathlib import Path

AQUI = Path(__file__).resolve().parent
PROJ = AQUI / "deck" / "project"
BLOBS = {k: AQUI / v for k, v in json.loads((AQUI / "deck" / "blobs.json").read_text()).items()}
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
deck = json.loads((PROJ / "deck.json").read_text(encoding="utf-8"))
fuentes = "".join(f'<link rel="stylesheet" href="{f["href"]}">' for f in deck["faces"].values() if "href" in f)


def formas(h):
    h = re.sub(r'<x-shape[^>]*kind="ellipse" style="([^"]*)"></x-shape>', r'<div style="\1;border-radius:50%"></div>', h)
    return re.sub(r'<x-connector[^>]*x1="(\d+)" y1="(\d+)" x2="(\d+)"[^>]*></x-connector>', lambda m: f'<div style="position:absolute;left:{m[1]}px;top:{int(m[2]) - 4}px;width:{int(m[3]) - int(m[1])}px;height:8px;background:#D9D9D9"></div>', h)


partes = []
for sid in deck["order"]:
    html = (PROJ / "slides" / f"{sid}.html").read_text(encoding="utf-8")
    html = re.sub(r"<aside>.*?</aside>", "", html, flags=re.S)
    html = re.sub(r"/_blob/([0-9a-f]{32})", lambda m: BLOBS[m.group(1)].as_uri(), html)
    partes.append(formas(html))
doc = f"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><title>{deck['title']}</title>{fuentes}
<style>
@page {{ size: 1920px 1080px; margin: 0 }}
html, body {{ margin: 0; padding: 0; background: #fff }}
* {{ box-sizing: border-box; margin: 0 }}
section {{ position: relative; width: 1920px; height: 1080px; overflow: hidden; page-break-after: always; break-after: page }}
section > * {{ flex-shrink: 0 }}
h1, h2, h3, p {{ font-weight: inherit }}
table {{ border-collapse: collapse }}
td, th {{ padding: 0.35em 0.6em; border-bottom: 1px solid #ddd; text-align: left }}
</style></head><body>{''.join(partes)}</body></html>"""
tmp = AQUI / "deck" / "_imprimir.html"
tmp.write_text(doc, encoding="utf-8")
salida = AQUI / "Una-recta-no-se-dobla.pdf"
subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--allow-file-access-from-files", "--virtual-time-budget=15000", f"--print-to-pdf={salida}", tmp.as_uri()],
               check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print(salida.name, salida.stat().st_size // 1024, "KB")
