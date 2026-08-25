#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sustituye la celda de setup de los 16 cuadernos por una que se autoabastece en Colab."""
import glob
import io
import json

VIEJO = '''# Los datos de Comercial Andina viven en sitio/datos/
CANDIDATOS = [Path("../datos"), Path("datos"), Path("sitio/datos"),
              Path("/content/CursoAnalisisDatos_IA_2026/sitio/datos")]
DATOS = next((p for p in CANDIDATOS if p.exists()), None)
if DATOS is None:
    raise FileNotFoundError(
        "No encuentro la carpeta de datos. En Colab ejecuta primero:\\n"
        "  !git clone https://github.com/<usuario>/CursoAnalisisDatos_IA_2026.git")
'''

NUEVO = '''# Los datos de Comercial Andina viven en sitio/datos/
REPO = "https://github.com/mayait/CursoAnalisisDatos_IA_2026.git"
COPIA = Path("/content/CursoAnalisisDatos_IA_2026")
CANDIDATOS = [Path("../datos"), Path("datos"), Path("sitio/datos"),
              COPIA / "sitio" / "datos"]
DATOS = next((p for p in CANDIDATOS if p.exists()), None)
if DATOS is None:
    # En Colab el cuaderno llega solo: se trae el repositorio una sola vez.
    import subprocess
    subprocess.run(["git", "clone", "--depth", "1", REPO, str(COPIA)], check=True)
    DATOS = COPIA / "sitio" / "datos"
'''


def main():
    tocados = 0
    for ruta in sorted(glob.glob("sitio/labs/lab_*.ipynb")):
        with io.open(ruta, encoding="utf-8") as f:
            nb = json.load(f)
        cambiado = False
        for celda in nb["cells"]:
            fuente = "".join(celda["source"])
            if VIEJO not in fuente:
                continue
            nueva = fuente.replace(VIEJO, NUEVO)
            celda["source"] = nueva.splitlines(keepends=True)
            cambiado = True
        if not cambiado:
            print(f"  sin cambios: {ruta}")
            continue
        with io.open(ruta, "w", encoding="utf-8") as f:
            json.dump(nb, f, ensure_ascii=False, indent=1)
        tocados += 1
        print(f"  actualizado: {ruta}")
    print(f"{tocados} cuadernos actualizados")


if __name__ == "__main__":
    main()
