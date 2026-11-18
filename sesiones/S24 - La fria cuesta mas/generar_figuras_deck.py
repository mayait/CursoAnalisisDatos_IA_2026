# -*- coding: utf-8 -*-
"""Figuras del deck «La fría cuesta más». Uso: python generar_figuras_deck.py

La nube usa el panel de demostración ya limpio (datos_demo/). Es ilustrativa: cada marca descarga su propio archivo.
El Operativo Verano usa las cifras del Exhibit 4 del caso.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

AQUI = Path(__file__).resolve().parent
OUT = AQUI / "img_deck"
ROJO, NEGRO, AZUL, AZUL2, AMBAR, GRIS, CLARO = "#E11B22", "#111111", "#1F6FB2", "#7FB0DE", "#F2A900", "#7A7A7A", "#D9D9D9"
plt.rcParams.update({"font.family": "Helvetica Neue", "font.size": 22, "axes.spines.top": False, "axes.spines.right": False,
                     "axes.edgecolor": NEGRO, "axes.linewidth": 1.6, "figure.facecolor": "white", "axes.facecolor": "white"})


def miles(v, _=None):
    return f"{v/1000:,.0f} mil" if v else "0"


def nube():
    d = pd.read_csv(AQUI / "datos_demo" / "redbull_limpio_aprox.csv")
    fig, ax = plt.subplots(figsize=(15.2, 8.2), dpi=110)
    ax.scatter(d.precio, d.ventas, s=70, color=NEGRO, alpha=0.55, linewidth=0)
    ax.set_xlabel("Precio de bodega (S/)", labelpad=12)
    ax.set_ylabel("Botellas vendidas por semana", labelpad=12)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(miles))
    ax.set_ylim(0, None)
    ax.text(0.98, 0.95, "520 semanas-ciudad\nde una marca", transform=ax.transAxes, ha="right", va="top", fontsize=26, color=ROJO, fontweight="bold")
    fig.tight_layout()
    fig.savefig(OUT / "nube.png")
    plt.close(fig)


EX4 = pd.DataFrame({
    "semana": range(5, 20),
    "precio": [4.0, 4.0, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.2, 3.6, 4.0, 4.0, 4.0, 4.0, 4.0],
    "promo": [28500, 27500, 52000, 45000, 36500, 37000, 40500, 36500, 64000, 42500, 10500, 18000, 14000, 17500, 18500],
    "ventas": [85925, 63926, 179628, 174538, 158982, 154464, 110930, 111675, 156316, 80398, 51172, 71796, 62020, 69577, 52180],
})


def operativo(nombre, marcar):
    """marcar: 'nada', 'saldana' o 'huaman'."""
    e = EX4
    fig, ax = plt.subplots(figsize=(15.2, 8.2), dpi=110)
    en = e.precio == 3.2
    colores = [ROJO if x else CLARO for x in en]
    if marcar == "huaman":
        colores = [ROJO if 15 <= s <= 19 else ("#F3B2B5" if x else CLARO) for s, x in zip(e.semana, en)]
    ax.bar(e.semana, e.ventas, color=colores, width=0.78)
    ax.set_xticks(e.semana)
    ax.set_xlabel("Semana de 2025", labelpad=12)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(miles))
    ax.set_ylim(0, 215000)
    ax.text(5.5, 196000, "S/ 4.00", ha="center", fontsize=24, color=GRIS, fontweight="bold")
    ax.text(10, 196000, "Operativo Verano · S/ 3.20", ha="center", fontsize=24, color=ROJO, fontweight="bold")
    ax.text(17, 196000, "S/ 4.00", ha="center", fontsize=24, color=GRIS, fontweight="bold")
    ax.plot([6.5, 6.5], [0, 205000], color=NEGRO, lw=1.2, ls=(0, (4, 4)))
    ax.plot([13.5, 13.5], [0, 205000], color=NEGRO, lw=1.2, ls=(0, (4, 4)))
    if marcar == "saldana":
        ax.plot([4.6, 6.4], [74926, 74926], color=NEGRO, lw=3)
        ax.plot([6.6, 13.4], [149505, 149505], color=NEGRO, lw=3)
        ax.text(5.5, 92000, "74,926", ha="center", fontsize=24, fontweight="bold")
        ax.text(10, 183000, "149,505 por semana", ha="center", fontsize=24, fontweight="bold", color=NEGRO, bbox=dict(facecolor="white", edgecolor="none", pad=4))
    if marcar == "huaman":
        ax.plot([4.6, 6.4], [74926, 74926], color=NEGRO, lw=3)
        ax.plot([14.6, 19.4], [61349, 61349], color=NEGRO, lw=3)
        ax.text(5.5, 92000, "74,926", ha="center", fontsize=24, fontweight="bold")
        ax.text(17, 82000, "61,349 · 18 % menos", ha="center", fontsize=24, fontweight="bold", color=ROJO)
    fig.tight_layout()
    fig.savefig(OUT / nombre)
    plt.close(fig)


def tres_a_la_vez():
    e = EX4
    fig, axs = plt.subplots(3, 1, figsize=(15.2, 8.2), dpi=110, sharex=True, gridspec_kw={"height_ratios": [1, 1, 1.5], "hspace": 0.28})
    axs[0].step(e.semana, e.precio, where="mid", color=ROJO, lw=5)
    axs[0].set_ylim(2.9, 4.3); axs[0].set_yticks([3.2, 4.0]); axs[0].set_yticklabels(["3.20", "4.00"])
    axs[0].text(4.45, 4.38, "Precio (S/)", fontsize=24, fontweight="bold", color=ROJO, va="bottom")
    axs[1].bar(e.semana, e.promo, color=AZUL, width=0.78)
    axs[1].yaxis.set_major_formatter(plt.FuncFormatter(miles)); axs[1].set_yticks([0, 30000, 60000])
    axs[1].text(4.45, 66000, "Promoción en bodega (S/)", fontsize=24, fontweight="bold", color=AZUL, va="bottom")
    axs[2].bar(e.semana, e.ventas, color=NEGRO, width=0.78)
    axs[2].yaxis.set_major_formatter(plt.FuncFormatter(miles)); axs[2].set_yticks([0, 90000, 180000])
    axs[2].text(4.45, 190000, "Botellas vendidas", fontsize=24, fontweight="bold", color=NEGRO, va="bottom")
    axs[2].set_xticks(e.semana); axs[2].set_xlabel("Semana de 2025", labelpad=12)
    for a in axs:
        a.axvspan(6.5, 13.5, color="#F2F2F2", zorder=0)
        a.set_xlim(4.4, 19.6)
    fig.savefig(OUT / "tres-a-la-vez.png", bbox_inches="tight", pad_inches=0.25)
    plt.close(fig)


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    nube()
    operativo("operativo.png", "nada")
    operativo("operativo-saldana.png", "saldana")
    operativo("operativo-huaman.png", "huaman")
    tres_a_la_vez()
    print("figuras en", OUT)


def nube_ciudad():
    """Solo para después de la revelación: Iquitos en rojo, el resto en gris."""
    d = pd.read_csv(AQUI / "datos_demo" / "redbull_limpio_aprox.csv")
    iq = d.ciudad.str.lower().str.startswith("iqu")
    fig, ax = plt.subplots(figsize=(15.2, 8.2), dpi=110)
    ax.scatter(d.precio[~iq], d.ventas[~iq], s=70, color=GRIS, alpha=0.5, linewidth=0)
    ax.scatter(d.precio[iq], d.ventas[iq], s=90, color=ROJO, alpha=0.8, linewidth=0)
    ax.set_xlabel("Precio de bodega (S/)", labelpad=12)
    ax.set_ylabel("Botellas vendidas por semana", labelpad=12)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(miles))
    ax.set_ylim(0, None)
    ax.text(8.3, 26000, "Iquitos: cobra el doble\ny es la plaza que menos vende", ha="center", fontsize=26, color=ROJO, fontweight="bold")
    ax.text(4.3, 150000, "Lima, Arequipa,\nCusco y Piura", ha="center", fontsize=26, color=GRIS, fontweight="bold")
    fig.tight_layout()
    fig.savefig(OUT / "nube-ciudad.png")
    plt.close(fig)


if __name__ == "__main__":
    nube_ciudad()
