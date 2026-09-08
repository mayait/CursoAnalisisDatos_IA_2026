#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Figuras de la S07/S08 sobre fondo blanco, acento USFQ #A6192E."""
import json
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

AQUI = Path(__file__).resolve().parent
IMG = AQUI / "img"
IMG.mkdir(exist_ok=True)
clave = json.loads((AQUI / "clave.json").read_text(encoding="utf-8"))

ROJO, GRIS, NEGRO = "#A6192E", "#B9B9B9", "#1e1e1e"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                     "figure.facecolor": "white", "axes.facecolor": "white",
                     "axes.edgecolor": "#D6D6D6", "axes.spines.top": False,
                     "axes.spines.right": False, "text.color": NEGRO,
                     "axes.labelcolor": NEGRO, "xtick.color": NEGRO, "ytick.color": NEGRO})


def guardar(fig, nombre):
    fig.savefig(IMG / nombre, dpi=160, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(nombre)


# 1 · % de líneas sin cliente por región
pr = clave["sin_cliente"]["por_region_pct"]
regs = sorted(pr, key=pr.get)
vals = [pr[r] for r in regs]
fig, ax = plt.subplots(figsize=(7.2, 3.4))
colores = [ROJO if v == max(vals) else GRIS for v in vals]
ax.barh(regs, vals, color=colores)
for i, v in enumerate(vals):
    ax.text(v + 0.15, i, f"{v:.1f}%", va="center", fontweight="bold")
ax.set_xlabel("Líneas sin ID Cliente (%)")
ax.set_xlim(0, max(vals) * 1.22)
ax.set_title("El vacío no cae parejo: % de líneas sin cliente por región",
             fontweight="bold", loc="left")
guardar(fig, "fig1_sin_cliente_region.png")

# 2 · Doble conteo por granularidad
real = clave["suma_ventas_real"]
doble = clave["suma_total_pedido_doble"]
fig, ax = plt.subplots(figsize=(7.2, 3.6))
barras = ax.bar(["Suma de Ventas\n(la cifra real)", 'Suma de "Total Pedido"\n(la trampa)'],
                [real, doble], color=[GRIS, ROJO], width=0.55)
for b, v in zip(barras, [real, doble]):
    ax.text(b.get_x() + b.get_width() / 2, v * 1.02, f"${v:,.0f}",
            ha="center", fontweight="bold")
ax.set_ylim(0, doble * 1.15)
ax.set_yticks([])
ax.set_title(f"Misma tabla, dos totales: sumar la columna equivocada infla la venta {doble/real:.1f}x",
             fontweight="bold", loc="left")
guardar(fig, "fig2_doble_conteo.png")

# 3 · Descuento: >0, =0 y no registrado
n = clave["filas"]
d_nan = clave["descuento_nan"]; d_cero = clave["descuento_cero"]
d_pos = n - d_nan - d_cero
fig, ax = plt.subplots(figsize=(7.2, 3.4))
cats = ["Con descuento\n(> 0)", "Sin descuento\n(= 0)", "No registrado\n(vacío)"]
vals = [d_pos, d_cero, d_nan]
barras = ax.bar(cats, vals, color=[GRIS, GRIS, ROJO], width=0.55)
for b, v in zip(barras, vals):
    ax.text(b.get_x() + b.get_width() / 2, v + 12, f"{v}", ha="center", fontweight="bold")
ax.set_ylim(0, max(vals) * 1.18)
ax.set_yticks([])
ax.set_title("Cero y vacío no son lo mismo: líneas por estado del descuento",
             fontweight="bold", loc="left")
guardar(fig, "fig3_descuento_cero_nan.png")

# 4 · Inventario de problemas (S08)
problemas = [
    ("Envío anterior al pedido", clave["envio_antes_pedido"]),
    ("Cantidad negativa", clave["cantidad_negativa"]),
    ("Utilidad = -9999", clave["utilidad_centinela"]),
    ("Duplicados exactos", clave["duplicados_exactos"]),
    ("Provincia vacía", clave["provincia_nan"]),
    ("Fechas en dd/mm/yyyy", clave["fechas_ddmm"]),
    ("Ventas como texto ($)", clave["ventas_texto"]),
    ("Sin ID Cliente", clave["sin_cliente"]["total"]),
    ("Descuento no registrado", clave["descuento_nan"]),
]
problemas.sort(key=lambda t: t[1])
et = [p[0] for p in problemas]; vv = [p[1] for p in problemas]
fig, ax = plt.subplots(figsize=(7.2, 4.6))
ax.barh(et, vv, color=[ROJO if v >= 100 else GRIS for v in vv])
for i, v in enumerate(vv):
    ax.text(v + 2.5, i, str(v), va="center", fontweight="bold")
ax.set_xlabel("Filas afectadas")
ax.set_xlim(0, max(vv) * 1.14)
ax.set_title(f"Inventario de calidad de andina_market.csv ({n} filas)",
             fontweight="bold", loc="left")
guardar(fig, "fig4_inventario.png")
