# -*- coding: utf-8 -*-
"""PowerPoint del deck: cada slide como imagen a pantalla completa, con las notas del orador.

Uso: python deck_a_pptx.py  (antes: python deck_a_pdf.py) -> La-fria-cuesta-mas.pptx
La slide oculta del plan B va al final, también oculta.
"""
import json, re, subprocess, tempfile
from pathlib import Path

from pptx import Presentation
from pptx.util import Emu

AQUI = Path(__file__).resolve().parent
PROJ = AQUI / "deck" / "project"
deck = json.loads((PROJ / "deck.json").read_text(encoding="utf-8"))
W, H = Emu(12192000), Emu(6858000)
tmp = Path(tempfile.mkdtemp())


def paginas(pdf, pref):
    subprocess.run(["pdftoppm", "-r", "110", "-jpeg", "-jpegopt", "quality=90", str(pdf), str(tmp / pref)], check=True)
    return sorted(tmp.glob(f"{pref}-*.jpg"))


htmls = {sid: (PROJ / "slides" / f"{sid}.html").read_text(encoding="utf-8") for sid in deck["order"]}
ocultas = [s for s in deck["order"] if re.search(r"<section[^>]*\shidden", htmls[s])]
visibles = [s for s in deck["order"] if s not in ocultas]
pags = dict(zip(visibles, paginas(AQUI / "La-fria-cuesta-mas.pdf", "p")))
assert len(pags) == len(visibles), (len(pags), len(visibles))
for sid in ocultas:  # se renderizan aparte, quitando el atributo hidden
    copia = PROJ / "slides" / f"_tmp_{sid}.html"
    copia.write_text(re.sub(r"(<section[^>]*)\shidden", r"\1", htmls[sid]).replace(f'id="{sid}"', f'id="_tmp_{sid}"'), encoding="utf-8")
    subprocess.run(["python3", str(AQUI / "deck_a_pdf.py"), f"_tmp_{sid}"], check=True, stdout=subprocess.DEVNULL)
    pags[sid] = paginas(AQUI / "deck" / "_prueba.pdf", f"o{sid}")[0]
    copia.unlink()
prs = Presentation()
prs.slide_width, prs.slide_height = W, H
for sid in deck["order"]:
    s = prs.slides.add_slide(prs.slide_layouts[6])
    s.shapes.add_picture(str(pags[sid]), 0, 0, W, H)
    n = re.search(r"<aside>(.*?)</aside>", htmls[sid], re.S)
    if n:
        s.notes_slide.notes_text_frame.text = n.group(1).strip()
    if sid in ocultas:
        s._element.set("show", "0")
salida = AQUI / "La-fria-cuesta-mas.pptx"
prs.save(salida)
print(salida.name, round(salida.stat().st_size / 1048576, 1), "MB,", len(Presentation(salida).slides), "slides,", len(ocultas), "oculta")
