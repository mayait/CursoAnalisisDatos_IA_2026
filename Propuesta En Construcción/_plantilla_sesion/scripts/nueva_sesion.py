#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Crea el esqueleto de una sesión del Seminario EDA.

Genera la carpeta S0X-CY - Tema con README.md, clase.md, clase_NN.ipynb y Lecturas.md,
ya enlazados entre sí y con las sesiones vecinas que existan en el repo.

El contenido pedagógico lo escribes tú encima: esto solo pone el andamio y la navegación,
que es lo que se rompe cuando se hace a mano.

Ejemplo:
    python nueva_sesion.py --raiz . --semana 5 --clase 1 --sesion 9 --total 17 \
        --tema "Regresión lineal, polinomial y multicolinealidad (VIF)" \
        --modulo "Módulo 3 · Modelado supervisado" \
        --repo we-human-centric/CursoPythonDatos_2026
"""
import argparse
import json
import os
import re
import sys
import unicodedata
from urllib.parse import quote


def carpetas_sesion(raiz):
    """Devuelve las carpetas de sesión ordenadas (S01-C1…, SF - …)."""
    def clave(n):
        m = re.match(r"S(\d\d)-C(\d)", n)
        return (int(m.group(1)), int(m.group(2))) if m else (99, 9)
    return sorted(
        [d for d in os.listdir(raiz)
         if os.path.isdir(os.path.join(raiz, d)) and re.match(r"^(S\d\d-C\d|SF) - ", d)],
        key=clave,
    )


def titulo_corto(carpeta):
    return carpeta.split(" - ", 1)[1].split(" - ENTREGA")[0]


def encabezado_nav(prev, sig, repo, carpeta, nn):
    izq = f"[← {titulo_corto(prev)}](../{quote(prev)}/)" if prev else "[← Índice](../README.md)"
    der = f"[{titulo_corto(sig)} →](../{quote(sig)}/)" if sig else "[Índice →](../README.md)"
    ruta = quote(carpeta)
    return (
        f"{izq} · [🏠 Índice](../README.md) · {der}\n\n"
        f'<a href="https://colab.research.google.com/github/{repo}/blob/main/{ruta}/clase_{nn}.ipynb" '
        f'target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" '
        f'alt="Open In Colab"/></a>  &nbsp; '
        f"[![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)]"
        f"(https://nbviewer.org/github/{repo}/blob/main/{ruta}/clase_{nn}.ipynb)\n\n---\n\n"
    )


def pie_nav(prev, sig, n):
    izq = f"[← Sesión {n-1}](../{quote(prev)}/)" if prev else "[← Índice](../README.md)"
    der = f"[Sesión {n+1} →](../{quote(sig)}/)" if sig else "[Índice →](../README.md)"
    return (
        f"\n---\n\n{izq} · [🏠 Índice](../README.md) · {der}\n\n"
        "> *Seminario EDA · [we-human-centric](https://github.com/we-human-centric)*\n"
    )


def cuerpo_clase(a):
    return f"""# Semana {a.semana} · Clase {a.clase} — {a.tema}

**Sesión:** Semana {a.semana} · Clase {a.clase} · sesión {a.sesion} de {a.total}
**Módulo:** {a.modulo}
**Duración:** {a.duracion}

---

## Introducción

<!-- Dos a cuatro frases: qué se desbloquea hoy y por qué importa fuera del aula. -->

## Objetivos de aprendizaje

Al terminar la sesión podrás:

- <!-- verbo + objeto concreto + herramienta -->
-
-

## Contenidos de la sesión

### 1.

### 2.

## Actividad práctica

En `clase_{a.nn}.ipynb`:

1.
2.
3.

## Trabajo en grupo sobre el caso asignado

En su dataset del caso:

-
-

## Entregable del día

<!-- Archivo concreto y dónde se sube. -->

## Recursos recomendados

-
"""


def notebook(a, carpeta):
    ruta = quote(carpeta)
    badge = (
        f'<a href="https://colab.research.google.com/github/{a.repo}/blob/main/{ruta}/'
        f'clase_{a.nn}.ipynb" target="_parent">'
        f'<img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>'
    )
    def md(src):
        return {"cell_type": "markdown", "metadata": {}, "source": src.splitlines(keepends=True)}
    def code(src):
        return {"cell_type": "code", "execution_count": None, "metadata": {},
                "outputs": [], "source": src.splitlines(keepends=True)}

    setup = (
        "# --- Setup del entorno ---\n"
        "import random\n"
        "import numpy as np\n"
        "import pandas as pd\n"
        "import matplotlib.pyplot as plt\n"
        "import seaborn as sns\n\n"
        "SEED = 42\n"
        "random.seed(SEED)\n"
        "np.random.seed(SEED)\n\n"
        'sns.set_theme(style="whitegrid", palette="deep")\n'
        'plt.rcParams["figure.figsize"] = (10, 4)\n\n'
        'print("Setup completo ✓")\n'
        'print(f"pandas {pd.__version__} · numpy {np.__version__}")'
    )
    celdas = [
        md(f"{badge}\n\n# Sesión {a.sesion} · {a.tema}\n\n<!-- Conecta con la sesión anterior. -->"),
        md("> **Hoy haces** · <!-- qué se hace y cuánto dura -->. ~2h30.\n>\n"
           "> **Entrega** · El notebook ejecutado de principio a fin, con tus respuestas en las "
           "celdas marcadas, subido al repo del equipo antes de la próxima clase."),
        code(setup),
        md("---\n\n## 1. "),
        code("# TU CÓDIGO AQUÍ\n"),
        md("### 🌶️ Ejercicio 1 — Guiado · "),
        code("# TU CÓDIGO AQUÍ\n"),
        md(f"## Entregable parcial\n\n<!-- Qué se sube hoy. -->\n\n## Para tu equipo\n\n- "),
    ]
    return {
        "cells": celdas,
        "metadata": {
            "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
            "language_info": {"name": "python", "version": "3.11.0"},
        },
        "nbformat": 4,
        "nbformat_minor": 5,
    }


def lecturas(a):
    return f"""# Lecturas adicionales · Semana {a.semana} · Clase {a.clase} · {a.tema}

Curaduría de material en español para profundizar después de la clase. Las copias locales están en la subcarpeta `lecturas/` cuando la fuente lo permite.

## Artículos técnicos

1. **[Título](url)** — Autor (dominio)
   *Por qué leerlo:*

2. **[Título](url)** — Autor (dominio)
   *Por qué leerlo:*

## Artículos de negocios y aplicación

1. **[Título](url)** — Fuente
   *Por qué leerlo:*

2. **[Título](url)** — Fuente
   *Por qué leerlo:*

## Video recomendado

- **[Título](url)** — Canal
  *Por qué verlo:*
  *Incrustado en el cuaderno `clase_{a.nn}.ipynb`.*
"""


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--raiz", default=".", help="raíz del repo del curso")
    p.add_argument("--semana", type=int, required=True)
    p.add_argument("--clase", type=int, required=True)
    p.add_argument("--sesion", type=int, required=True, help="número global de sesión")
    p.add_argument("--total", type=int, default=17)
    p.add_argument("--tema", required=True)
    p.add_argument("--modulo", default="")
    p.add_argument("--entrega", default="", help="N si la sesión cierra la ENTREGA N")
    p.add_argument("--duracion", default="2 horas 30 minutos sincrónicas")
    p.add_argument("--repo", default="we-human-centric/CursoPythonDatos_2026")
    p.add_argument("--force", action="store_true", help="sobrescribe si la carpeta existe")
    a = p.parse_args()
    a.nn = f"{a.sesion:02d}"

    # El repo nombra las carpetas sin tildes ni signos raros: "S05-C2 - Regresion Logistica".
    slug = unicodedata.normalize("NFKD", a.tema).encode("ascii", "ignore").decode()
    slug = re.sub(r"[^\w ()-]", "", slug).strip()
    carpeta = f"S{a.semana:02d}-C{a.clase} - {slug}"
    if a.entrega:
        carpeta += f" - ENTREGA {a.entrega}"
    destino = os.path.join(a.raiz, carpeta)
    if os.path.exists(destino) and not a.force:
        sys.exit(f"Ya existe {destino}. Usa --force para sobrescribir.")

    existentes = carpetas_sesion(a.raiz)
    prev = next((d for d in reversed(existentes) if d < carpeta), None)
    sig = next((d for d in existentes if d > carpeta), None)

    os.makedirs(os.path.join(destino, "lecturas"), exist_ok=True)
    cuerpo = cuerpo_clase(a)
    with open(os.path.join(destino, "clase.md"), "w", encoding="utf-8") as f:
        f.write(cuerpo)
    with open(os.path.join(destino, "README.md"), "w", encoding="utf-8") as f:
        f.write(encabezado_nav(prev, sig, a.repo, carpeta, a.nn) + cuerpo + pie_nav(prev, sig, a.sesion))
    with open(os.path.join(destino, f"clase_{a.nn}.ipynb"), "w", encoding="utf-8") as f:
        json.dump(notebook(a, carpeta), f, ensure_ascii=False, indent=1)
    with open(os.path.join(destino, "Lecturas.md"), "w", encoding="utf-8") as f:
        f.write(lecturas(a))

    print(f"Creada: {destino}")
    print(f"  anterior: {prev or '—'}")
    print(f"  siguiente: {sig or '—'}")
    print("\nFalta a mano:")
    print("  1. Escribir el contenido en clase.md y replicarlo en README.md (cuerpo idéntico).")
    print("  2. Generar index.html con el esqueleto de reference/sitio_estatico.md.")
    print("  3. Añadir la sesión a la sidebar de TODAS las páginas y al README raíz.")
    if sig:
        print(f"  4. Actualizar la navegación de {sig} para que apunte a esta sesión.")


if __name__ == "__main__":
    main()
