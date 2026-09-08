#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Figuras de la sesión 5 · La trampa del promedio.

Genera los PNG de img/ a partir de sitio/datos/superstore_2026.csv, para la
teoría de D2L y para los slides. Regla de la casa: TODO sobre fondo blanco,
identidad USFQ (rojo #A6192E, tinta #1e1e1e). Incluye s05_hapax_datos.png,
el "muro de datos" del deck. Toda cifra se calcula aquí; nada va a mano.
"""
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.patches import FancyArrowPatch, Rectangle

AQUI = Path(__file__).resolve().parent
DATOS = AQUI.parent.parent / "sitio" / "datos" / "superstore_2026.csv"

# Regla de la casa: fondo blanco siempre.
PALETA = dict(fondo="white", tinta="#1e1e1e", gris="#6b6b6b", acento="#A6192E",
              barra="#c9c9c9", borde_barra="white", caja="#efefef",
              caja_borde="#c9c9c9", mediana="#1e1e1e", sobre_acento="white",
              ejemplo_sobre_acento="#f3d2d8", borde_eje="#d6d6d6")

df = pd.read_csv(DATOS)


def aplicar(p):
    plt.rcParams.update({
        "font.family": "DejaVu Sans", "text.color": p["tinta"],
        "axes.edgecolor": p["borde_eje"], "axes.labelcolor": p["tinta"],
        "xtick.color": p["gris"], "ytick.color": p["gris"],
        "axes.spines.top": False, "axes.spines.right": False,
        "figure.facecolor": p["fondo"], "axes.facecolor": p["fondo"],
        "savefig.dpi": 165, "savefig.bbox": "tight",
        "savefig.facecolor": p["fondo"], "axes.grid": False,
    })


# ── Figura 1 · La escalera de la analítica ────────────────────────────────────
def fig_escalera(p, img):
    pasos = [
        ("1 · DESCRIPTIVO", "¿Qué pasó?", "ventas por mes,\nticket típico, top productos"),
        ("2 · DIAGNÓSTICO", "¿Por qué pasó?", "el descuento se comió\nel margen de Muebles"),
        ("3 · PREDICTIVO", "¿Qué va a pasar?", "pronóstico del trimestre,\nquién dejará de comprar"),
        ("4 · PRESCRIPTIVO", "¿Qué hacemos?", "a qué cliente llamar,\nqué precio poner"),
    ]
    fig, ax = plt.subplots(figsize=(9.6, 5.6))
    ancho, alto = 2.25, 1.34
    for i, (nombre, pregunta, ejemplo) in enumerate(pasos):
        x, y = i * ancho, i * alto
        hoy = i == 0
        ax.add_patch(Rectangle((x, 0), ancho - 0.12, y + alto,
                               facecolor=p["acento"] if hoy else p["caja"],
                               edgecolor=p["acento"] if hoy else p["caja_borde"],
                               linewidth=1.4, zorder=2))
        cx = x + (ancho - 0.12) / 2
        ax.text(cx, y + alto - 0.18, nombre, ha="center", va="top", zorder=3,
                fontsize=10.5, fontweight="bold",
                color=p["sobre_acento"] if hoy else p["tinta"])
        ax.text(cx, y + alto - 0.52, pregunta, ha="center", va="top", zorder=3,
                fontsize=12.5, fontstyle="italic", fontweight="bold",
                color=p["sobre_acento"] if hoy else p["acento"])
        ax.text(cx, y + alto - 0.90, ejemplo, ha="center", va="top", zorder=3,
                fontsize=8.6,
                color=p["ejemplo_sobre_acento"] if hoy else p["gris"])
    ax.annotate("HOY estás aquí", xy=(ancho / 2 - 0.06, alto + 0.07),
                xytext=(ancho / 2 - 0.06, alto + 0.85), ha="center",
                fontsize=11, fontweight="bold", color=p["acento"],
                arrowprops=dict(arrowstyle="-|>", color=p["acento"], lw=2))
    ax.add_patch(FancyArrowPatch((0.4, 4 * alto + 0.5), (4 * ancho - 1.4, 4 * alto + 0.5),
                                 arrowstyle="-|>", mutation_scale=18,
                                 color=p["gris"], lw=1.6))
    ax.text(0.4, 4 * alto + 0.66, "más valor para el negocio · más dificultad técnica",
            fontsize=9.5, color=p["gris"])
    ax.text(0, -0.34,
            "Cada escalón se apoya en el anterior: nadie predice bien lo que no supo describir.",
            fontsize=9.5, color=p["tinta"])
    ax.set_xlim(-0.15, 4 * ancho)
    ax.set_ylim(-0.62, 4 * alto + 1.15)
    ax.axis("off")
    fig.savefig(img / "s05_escalera.png")
    plt.close(fig)


# ── Figura 2 · ¿Cuánto vale un pedido típico? ────────────────────────────────
def fig_pedidos(p, img):
    ped = df.groupby("pedido_id")["venta"].sum()
    media, mediana = ped.mean(), ped.median()
    bajo = (ped < media).mean() * 100
    fig, ax = plt.subplots(figsize=(9.6, 4.6))
    ax.hist(ped.clip(upper=2500), bins=62, color=p["barra"],
            edgecolor=p["borde_barra"], zorder=2)
    ax.axvline(mediana, color=p["mediana"], ls="--", lw=2, zorder=3)
    ax.axvline(media, color=p["acento"], lw=2.6, zorder=3)
    caja = dict(facecolor=p["fondo"], edgecolor="none", alpha=0.85, pad=2)
    ax.text(mediana - 28, ax.get_ylim()[1] * 0.90, f"mediana\n\\${mediana:,.0f}",
            ha="right", va="top", fontsize=11, fontweight="bold",
            color=p["mediana"], bbox=caja)
    ax.text(media + 28, ax.get_ylim()[1] * 0.96,
            f"media  \\${media:,.0f}\n← el {bajo:.1f}% de los pedidos\n"
            "    queda debajo de ella",
            ha="left", va="top", fontsize=11, fontweight="bold",
            color=p["acento"], bbox=caja)
    ax.text(2490, ax.get_ylim()[1] * 0.40,
            f"la última barra apila los {int((ped > 2500).sum())} pedidos\n"
            f"sobre \\$2,500 · el máximo real es \\${ped.max():,.0f}",
            ha="right", fontsize=8.8, color=p["gris"])
    ax.set_xlabel("valor del pedido (USD)")
    ax.set_ylabel("número de pedidos")
    ax.set_title(f"Los {len(ped):,} pedidos de Superstore · la cola larga que infla la media",
                 fontsize=12, fontweight="bold", loc="left")
    ax.set_xlim(0, 2560)
    fig.savefig(img / "s05_hist_pedidos.png")
    plt.close(fig)


# ── Figura 3 · ¿Qué categoría es más rentable por línea? ─────────────────────
def fig_categorias(p, img):
    g = (df[df["categoria"] != "Tecnología"]
         .groupby("categoria")["utilidad"].agg(["mean", "median"]))
    fig, axes = plt.subplots(1, 2, figsize=(9.6, 3.7), sharey=True)
    for ax, col, titulo in [(axes[0], "mean", "Si miras la MEDIA…"),
                            (axes[1], "median", "…si miras la MEDIANA")]:
        vals = g[col].sort_values()
        ganador = vals.idxmax()
        colores = [p["acento"] if c == ganador else p["barra"] for c in vals.index]
        barras = ax.barh(vals.index, vals.values, color=colores, height=0.55)
        for b, v in zip(barras, vals.values):
            ax.text(v + 0.4, b.get_y() + b.get_height() / 2, f"\\${v:,.2f}",
                    va="center", fontsize=11, fontweight="bold",
                    color=p["acento"] if v == vals.max() else p["gris"])
        ax.set_title(titulo, fontsize=11.5, fontweight="bold", loc="left")
        ax.text(0.97, 0.55, f"gana\n{ganador}", transform=ax.transAxes,
                ha="right", va="center", fontsize=11, fontweight="bold",
                color=p["acento"])
        ax.set_xlim(0, 24)
        ax.set_xlabel("utilidad por línea de venta (USD)")
    fig.suptitle("La misma pregunta, dos respuestas opuestas", x=0.01, ha="left",
                 fontsize=12.5, fontweight="bold", color=p["tinta"])
    fig.tight_layout(rect=(0, 0, 1, 0.90))
    fig.savefig(img / "s05_categorias.png")
    plt.close(fig)


# ── Figura 4 · Libreros: la trampa inversa ───────────────────────────────────
def fig_libreros(p, img):
    lib = df.loc[df["subcategoria"] == "Libreros", "utilidad"]
    fig, ax = plt.subplots(figsize=(9.6, 4.3))
    ax.hist(lib, bins=48, color=p["barra"], edgecolor=p["borde_barra"], zorder=2)
    ax.axvline(lib.median(), color=p["mediana"], ls="--", lw=2, zorder=3)
    ax.axvline(lib.mean(), color=p["acento"], lw=2.6, zorder=3)
    ax.text(lib.median() + 14, ax.get_ylim()[1] * 0.95,
            f"mediana +\\${lib.median():,.2f}\nla venta típica gana plata",
            fontsize=10.5, fontweight="bold", color=p["mediana"], va="top")
    ax.text(lib.mean() - 14, ax.get_ylim()[1] * 0.60,
            f"media −\\${abs(lib.mean()):,.2f}", ha="right",
            fontsize=10.5, fontweight="bold", color=p["acento"], va="top")
    perd = lib[lib < -100]
    ax.annotate(f"{len(perd)} ventas pierden más de \\$100:\n"
                f"entre todas se comen \\${abs(perd.sum()):,.0f}",
                xy=(-700, 2), xytext=(-1450, 22), fontsize=9.5, color=p["acento"],
                arrowprops=dict(arrowstyle="-|>", color=p["acento"], lw=1.4))
    ax.set_xlabel("utilidad por línea de venta (USD)")
    ax.set_ylabel("número de líneas")
    ax.set_title(f"Libreros · {len(lib)} líneas de venta · total −\\${abs(lib.sum()):,.0f}",
                 fontsize=12, fontweight="bold", loc="left")
    fig.savefig(img / "s05_libreros.png")
    plt.close(fig)


# ── Figura 5 · El muro de datos (hapax de los slides) ────────────────────────
def fig_hapax(p, img):
    cols = ["pedido_id", "fecha_pedido", "cliente", "ciudad", "categoria",
            "subcategoria", "producto", "venta", "cantidad", "descuento", "utilidad"]
    filas = df.sample(46, random_state=42).sort_index()[cols]
    lineas = [" | ".join(f"{c[:14]:<14}" for c in cols)]
    for _, r in filas.iterrows():
        lineas.append(" | ".join(f"{str(v)[:14]:<14}" for v in r.values))
    fig, ax = plt.subplots(figsize=(12.6, 5.2))
    ax.text(0.005, 0.98, "\n".join(lineas), family="DejaVu Sans Mono",
            fontsize=4.6, color=p["gris"], va="top", linespacing=1.55)
    ax.text(0.005, 1.04, "superstore_2026.csv · 46 de 9,994 líneas",
            fontsize=8, color=p["gris"])
    ax.axis("off")
    fig.savefig(img / "s05_hapax_datos.png")
    plt.close(fig)


if __name__ == "__main__":
    img = AQUI / "img"
    img.mkdir(parents=True, exist_ok=True)
    aplicar(PALETA)
    fig_escalera(PALETA, img)
    fig_pedidos(PALETA, img)
    fig_categorias(PALETA, img)
    fig_libreros(PALETA, img)
    fig_hapax(PALETA, img)
    for f in sorted(img.glob("s05_*.png")):
        print(f"{f.name} {f.stat().st_size/1024:.0f} KB")
