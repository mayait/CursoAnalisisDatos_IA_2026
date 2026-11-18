# -*- coding: utf-8 -*-
"""Convierte el deck (deck/project) a PDF con Chrome sin cabeza, una slide por página de 1920x1080.

Uso: ../../.venv/bin/python deck_a_pdf.py  -> Seis-decisiones-con-una-recta.pdf
Las imágenes /_blob/<id> del artifact se reemplazan por los archivos locales de img_deck/.
"""
import json
import re
import subprocess
from pathlib import Path

AQUI = Path(__file__).resolve().parent
PROJ = AQUI / "deck" / "project"
IMG = AQUI / "img_deck"
BLOBS = {
    "677f088ded0f23e244983d27e6f061f1": IMG / "d1-dispersiones.png",
    "8beabd7d91c5f7b16693556c6d370265": IMG / "p1-recta-tv.png",
    "e2933800edefff83d1d0fcd2acf70d9a": IMG / "p2-linea-base.png",
    "74b6210d8216dec83a6da676f9c72ed5": IMG / "x1-ganancia.png",
    "2d34a4be796b2301991686a1628d02f0": IMG / "g1-prensa.png",
    "504ffe1fb26084b5077cf41adc90010d": IMG / "x2-lanzar.png",
    "7740993ef00a7c7b0ca8ea4a3367a143": IMG / "ilus" / "portada.jpg",
    "d25665f13a8bdf99a34dede0b30d6913": IMG / "ilus" / "teachable.jpg",
    "eed8d302d504b781199b462b04f156da": IMG / "ilus" / "daniela.jpg",
    "ffa7620c7e5bca2ae010bc76b9815491": IMG / "ilus" / "mercado.jpg",
    "b26cca8d0cddce2c55acb9cc1db694ee": IMG / "ilus" / "prensa.jpg",
    "4d19854f613fbebd68877de43bf1cf65": IMG / "ilus" / "escalera.jpg",
    "407857d49805aeab98364315277214df": IMG / "ilus" / "casa.jpg",
}
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

deck = json.loads((PROJ / "deck.json").read_text(encoding="utf-8"))
fuentes = "".join(f'<link rel="stylesheet" href="{f["href"]}">' for f in deck["faces"].values() if "href" in f)
partes = []
for sid in deck["order"]:
    html = (PROJ / "slides" / f"{sid}.html").read_text(encoding="utf-8")
    html = re.sub(r"<aside>.*?</aside>", "", html, flags=re.S)
    html = re.sub(r"/_blob/([0-9a-f]{32})", lambda m: BLOBS[m.group(1)].as_uri(), html)
    partes.append(html)
doc = f"""<!DOCTYPE html><html lang="es"><head><meta charset="utf-8"><title>{deck['title']}</title>{fuentes}
<style>
@page {{ size: 1920px 1080px; margin: 0 }}
html, body {{ margin: 0; padding: 0; background: #fff }}
* {{ box-sizing: border-box; margin: 0 }}
section {{ position: relative; width: 1920px; height: 1080px; overflow: hidden; page-break-after: always; break-after: page }}
section > * {{ flex-shrink: 0 }}
h1, h2, h3, p {{ font-weight: inherit }}
table {{ border-collapse: collapse }}
</style></head><body>{''.join(partes)}</body></html>"""
tmp = AQUI / "deck" / "_imprimir.html"
tmp.write_text(doc, encoding="utf-8")
salida = AQUI / "Seis-decisiones-con-una-recta.pdf"
subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--allow-file-access-from-files",
                "--virtual-time-budget=15000", f"--print-to-pdf={salida}", tmp.as_uri()], check=True,
               stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
print(salida, salida.stat().st_size, "bytes")
