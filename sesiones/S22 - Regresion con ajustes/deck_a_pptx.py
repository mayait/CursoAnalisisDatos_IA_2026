# -*- coding: utf-8 -*-
"""PowerPoint de la clase: cada slide como imagen y las animaciones embebidas sin sonido. Conserva las notas.

Uso: python deck_a_pptx.py  (antes: deck_a_pdf.py) -> Una-recta-no-se-dobla.pptx
"""
import json
import re
import subprocess
import tempfile
from pathlib import Path

from pptx import Presentation
from pptx.util import Emu

AQUI = Path(__file__).resolve().parent
PROJ = AQUI / "deck" / "project"
BLOBS = {k: AQUI / v for k, v in json.loads((AQUI / "deck" / "blobs.json").read_text()).items()}
deck = json.loads((PROJ / "deck.json").read_text(encoding="utf-8"))
W, H = Emu(12192000), Emu(6858000)
tmp = Path(tempfile.mkdtemp())
subprocess.run(["pdftoppm", "-r", "96", "-jpeg", "-jpegopt", "quality=88", str(AQUI / "Una-recta-no-se-dobla.pdf"), str(tmp / "p")], check=True)
paginas = sorted(tmp.glob("p-*.jpg"))
assert len(paginas) == len(deck["order"]), (len(paginas), len(deck["order"]))
prs = Presentation()
prs.slide_width, prs.slide_height = W, H
vacio = prs.slide_layouts[6]
videos = 0
for sid, pag in zip(deck["order"], paginas):
    html = (PROJ / "slides" / f"{sid}.html").read_text(encoding="utf-8")
    s = prs.slides.add_slide(vacio)
    v = re.search(r'src="/_blob/([0-9a-f]{32})" data-video="/_blob/([0-9a-f]{32})"', html)
    if v:
        mudo = tmp / f"{sid}.mp4"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(BLOBS[v.group(2)]), "-an", "-c:v", "copy", "-movflags", "+faststart", str(mudo)], check=True)
        s.shapes.add_movie(str(mudo), 0, 0, W, H, poster_frame_image=str(BLOBS[v.group(1)]), mime_type="video/mp4")
        videos += 1
    else:
        s.shapes.add_picture(str(pag), 0, 0, W, H)
    n = re.search(r"<aside>(.*?)</aside>", html, re.S)
    if n:
        s.notes_slide.notes_text_frame.text = n.group(1).strip()
salida = AQUI / "Una-recta-no-se-dobla.pptx"
prs.save(salida)
r = Presentation(salida)
print(salida.name, salida.stat().st_size // 1048576, "MB,", len(r.slides), "slides,", videos, "animaciones sin sonido")
