# -*- coding: utf-8 -*-
"""Gráficas del deck del miércoles 4 de noviembre (caso Daniela), sistema We Want More.

Fondo blanco, anotación dentro de la imagen, rojo #E11B22 para la marca, #1F6FB2 para la
contrahistoria, #7FB0DE secundario, gris para el resto. Todo sale de d2l/mercados-bebidas-cumbre.csv.
Uso: ../../.venv/bin/python generar_figuras_deck.py  -> img_deck/*.png
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

AQUI = Path(__file__).resolve().parent
OUT = AQUI / "img_deck"
OUT.mkdir(exist_ok=True)
df = pd.read_csv(AQUI / "d2l" / "mercados-bebidas-cumbre.csv")

ROJO, AZUL, CELESTE, AMBAR, GRIS, TINTA = "#E11B22", "#1F6FB2", "#7FB0DE", "#F2A900", "#9A9A9A", "#111111"
MARGEN = 12
plt.rcParams.update({
    "font.family": ["Arial", "Helvetica", "DejaVu Sans"], "font.size": 15, "axes.edgecolor": "#BBBBBB",
    "axes.labelcolor": TINTA, "xtick.color": "#555555", "ytick.color": "#555555", "axes.spines.top": False,
    "axes.spines.right": False, "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white",
})


def n(x, d=2):
    return f"{x:,.{d}f}".replace(",", "X").replace(".", ",").replace("X", ".").replace("-", "−")


def guardar(fig, nombre):
    fig.savefig(OUT / nombre, dpi=160, bbox_inches="tight", pad_inches=0.25)
    plt.close(fig)
    print("escrita", nombre)


# 1 · Describir: tres dispersiones
fig, axs = plt.subplots(1, 3, figsize=(16, 5.2), sharey=True)
for ax, (col, nombre, color) in zip(axs, [("tv", "Televisión", ROJO), ("radio", "Radio", AZUL), ("prensa", "Prensa", GRIS)]):
    r = df[col].corr(df.ventas)
    ax.scatter(df[col], df.ventas, s=22, color=color, alpha=0.75, edgecolor="none")
    ax.set_xlabel(f"Inversión en {nombre.lower()} (miles de USD)")
    ax.text(0.04, 0.95, f"{nombre}\ncorrelación {n(r)}", transform=ax.transAxes, va="top", fontsize=17,
            fontweight="bold", color=color)
axs[0].set_ylabel("Ventas (miles de unidades)")
guardar(fig, "d1-dispersiones.png")

# 2 · Predecir: la recta de TV
fit = smf.ols("ventas ~ tv", df).fit()
x = np.linspace(0, df.tv.max(), 50)
fig, ax = plt.subplots(figsize=(11, 6))
ax.scatter(df.tv, df.ventas, s=24, color=GRIS, alpha=0.7, edgecolor="none")
ax.plot(x, fit.params["Intercept"] + fit.params["tv"] * x, color=ROJO, lw=3)
ax.set_xlabel("Inversión en televisión (miles de USD)"); ax.set_ylabel("Ventas (miles de unidades)")
ax.text(0.03, 0.96, f"Pendiente {n(fit.params['tv'], 4)}: {n(fit.params['tv'] * 1000, 1)} unidades por cada mil USD\n"
        f"Intercepto {n(fit.params['Intercept'])} · R² {n(fit.rsquared)}", transform=ax.transAxes, va="top",
        fontsize=16, color=TINTA)
guardar(fig, "p1-recta-tv.png")

# 3 · Predecir: error contra la línea base
tr, te = train_test_split(df, test_size=0.25, random_state=42)
mae = {"Línea base": mean_absolute_error(te.ventas, DummyRegressor().fit(tr[["tv"]], tr.ventas).predict(te[["tv"]]))}
for nombre, cols in [("Prensa", ["prensa"]), ("Radio", ["radio"]), ("TV", ["tv"]), ("TV + radio", ["tv", "radio"])]:
    mae[nombre] = mean_absolute_error(te.ventas, LinearRegression().fit(tr[cols], tr.ventas).predict(te[cols]))
fig, ax = plt.subplots(figsize=(11, 6))
colores = [GRIS, GRIS, CELESTE, AZUL, ROJO]
b = ax.barh(list(mae.keys()), list(mae.values()), color=colores, height=0.6)
ax.invert_yaxis()
ax.axvline(2, color=TINTA, lw=2, ls="--")
ax.text(2.05, -0.65, "Tolerancia de Daniela: 2 mil unidades", fontsize=15, color=TINTA, va="center")
ax.set_ylim(4.5, -0.9)
for rect, v in zip(b, mae.values()):
    ax.text(v + 0.06, rect.get_y() + rect.get_height() / 2, n(v), va="center", fontsize=16, fontweight="bold")
ax.set_xlabel("Error medio en los 50 mercados de prueba (miles de unidades)")
ax.set_xlim(0, 5.6)
guardar(fig, "p2-linea-base.png")

# 4 · Prescribir: ganancia por cada mil USD
gan = {}
for col, nombre in [("tv", "Televisión"), ("radio", "Radio"), ("prensa", "Prensa")]:
    bb = smf.ols(f"ventas ~ {col}", df).fit().params[col]
    gan[nombre] = bb * 1000 * MARGEN - 1000
fig, ax = plt.subplots(figsize=(11, 5.6))
cols = [GRIS if v < 0 else ROJO for v in gan.values()]
b = ax.bar(list(gan.keys()), list(gan.values()), color=cols, width=0.55)
ax.axhline(0, color=TINTA, lw=1.2)
for rect, v in zip(b, gan.values()):
    ax.text(rect.get_x() + rect.get_width() / 2, v + (60 if v > 0 else -60), ("+" if v > 0 else "") + n(v, 0) + " USD",
            ha="center", va="bottom" if v > 0 else "top", fontsize=19, fontweight="bold")
ax.set_ylabel("Margen menos inversión, por cada mil USD")
ax.set_ylim(-800, 1800)
ax.text(0.98, 0.95, f"Margen de {MARGEN} USD por unidad", transform=ax.transAxes, ha="right", va="top", fontsize=15, color="#555555")
guardar(fig, "x1-ganancia.png")

# 5 · Diagnosticar: la prensa sola y acompañada
simple = smf.ols("ventas ~ prensa", df).fit()
tres = smf.ols("ventas ~ tv + radio + prensa", df).fit()
vals = [simple.params["prensa"] * 1000, tres.params["prensa"] * 1000]
ics = [simple.conf_int().loc["prensa"] * 1000, tres.conf_int().loc["prensa"] * 1000]
fig, ax = plt.subplots(figsize=(11, 5.6))
etiquetas = ["Prensa sola", "Prensa junto a TV y radio"]
for i, (v, ic, c) in enumerate(zip(vals, ics, [GRIS, ROJO])):
    ax.plot([ic[0], ic[1]], [i, i], color=c, lw=4)
    ax.scatter([v], [i], s=180, color=c, zorder=3)
    ax.text(ic[1] + 2, i, f"{n(v, 1)} unidades por cada mil USD", ha="left", va="center", fontsize=16, fontweight="bold", color=c) if i == 1 else ax.text(v, i - 0.22, f"{n(v, 1)} unidades por cada mil USD", ha="center", fontsize=16, fontweight="bold", color=c)
ax.axvline(0, color=TINTA, lw=1.2, ls="--")
ax.set_yticks([0, 1], etiquetas); ax.set_ylim(1.6, -0.6)
ax.set_xlabel("Unidades adicionales por cada mil USD en prensa, con intervalo de confianza al 95 %")
ax.text(0.98, 0.06, f"Correlación entre radio y prensa: {n(df.radio.corr(df.prensa))}", transform=ax.transAxes,
        ha="right", fontsize=15, color=AZUL)
guardar(fig, "g1-prensa.png")

# 6 · Prescribir: lanzar
dos = smf.ols("ventas ~ tv + radio", df).fit()
planes = [("Agencia\n150 TV + 25 radio", 150, 25), ("Daniela\n50 TV + 49 radio", 50, 49)]
fig, ax = plt.subplots(figsize=(11, 6))
for i, (nombre, tv, ra) in enumerate(planes):
    f = dos.get_prediction(pd.DataFrame({"tv": [tv], "radio": [ra]})).summary_frame(alpha=0.10).iloc[0]
    m, lo, hi = f["mean"] * MARGEN, f["obs_ci_lower"] * MARGEN, f["obs_ci_upper"] * MARGEN
    gasto = tv + ra
    ax.plot([lo, hi], [i, i], color=ROJO if m > gasto else GRIS, lw=6, solid_capstyle="butt", alpha=0.45)
    ax.scatter([m], [i], s=200, color=ROJO if m > gasto else GRIS, zorder=3)
    ax.scatter([gasto], [i], s=260, marker="|", color=TINTA, linewidths=4, zorder=4)
    ax.text(m, i - 0.25, f"margen esperado {n(m, 1)} mil", ha="center", fontsize=15, fontweight="bold")
    ax.text(gasto, i + 0.3, f"publicidad {gasto} mil", ha="center", fontsize=15, color=TINTA)
ax.set_yticks([0, 1], [p[0] for p in planes]); ax.set_ylim(1.7, -0.7)
ax.set_xlabel(f"Miles de USD · margen a {MARGEN} USD por unidad con su intervalo de predicción al 90 %")
ax.set_xlim(60, 230)
guardar(fig, "x2-lanzar.png")
