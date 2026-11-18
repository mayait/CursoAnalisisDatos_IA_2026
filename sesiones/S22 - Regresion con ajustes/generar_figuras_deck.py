# -*- coding: utf-8 -*-
"""Gráficas del deck de regresión con ajustes. Todas salen de los datos y de cifras.json.

Uso: python generar_figuras_deck.py  -> img_deck/*.png, fondo blanco y anotación dentro de la imagen.
"""
import json
import warnings
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from matplotlib.colors import TwoSlopeNorm, LinearSegmentedColormap
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

warnings.filterwarnings("ignore")
AQUI = Path(__file__).resolve().parent
OUT = AQUI / "img_deck"
R = json.loads((AQUI / "cifras.json").read_text(encoding="utf-8"))
df = pd.read_csv(AQUI / "d2l" / "mercados-bebidas-cumbre.csv")
C = ["tv", "radio", "prensa"]
tr, te = train_test_split(df, test_size=0.25, random_state=42)
ROJO, NEGRO, AZUL, AZUL2, AMBAR, GRIS, CLARO = "#E11B22", "#111111", "#1F6FB2", "#7FB0DE", "#F2A900", "#7A7A7A", "#D9D9D9"
plt.rcParams.update({"font.family": "Helvetica Neue", "font.size": 22, "axes.spines.top": False, "axes.spines.right": False, "axes.edgecolor": NEGRO,
                     "axes.labelcolor": GRIS, "xtick.color": GRIS, "ytick.color": GRIS, "axes.labelsize": 22, "xtick.labelsize": 20, "ytick.labelsize": 20,
                     "figure.facecolor": "white", "axes.facecolor": "white", "savefig.facecolor": "white"})
coma = lambda v, d=2: f"{v:.{d}f}".replace(".", ",")


def guardar(fig, nombre):
    fig.savefig(OUT / f"{nombre}.png", dpi=110)
    plt.close(fig)


pl = smf.ols("ventas ~ tv + radio", df).fit()
cu = smf.ols("ventas ~ tv + radio + tv:radio + I(tv**2)", df).fit()
mapa = LinearSegmentedColormap.from_list("m", [ROJO, "#F7C9CB", "#F5F5F5", "#BCD6EE", AZUL])
norma = TwoSlopeNorm(vmin=-5, vcenter=0, vmax=5)

# 1. Mapa de errores del plano
fig, ax = plt.subplots(figsize=(15.1, 7.5), layout="constrained")
ax.scatter(df.tv, df.radio, c=pl.resid, cmap=mapa, norm=norma, s=210, edgecolor="#55555544", linewidth=0.6)
ax.scatter([50], [49], marker="X", s=620, color=NEGRO, zorder=5)
ax.annotate("El plan de Daniela", (50, 49), xytext=(92, 46.2), fontsize=26, fontweight="bold", color=NEGRO, va="center")
ax.text(8, 22, "Solo radio:\nel plano promete de más", fontsize=24, color=ROJO, fontweight="bold", va="center")
ax.text(205, 21.5, "Solo TV:\nel plano promete de más", fontsize=24, color=ROJO, fontweight="bold", ha="left", va="center")
ax.text(195, 44.5, "Los dos medios:\nse queda corto", fontsize=24, color=AZUL, fontweight="bold", va="center")
ax.set_xlabel("Inversión en TV (miles de USD)")
ax.set_ylabel("Inversión en radio (miles de USD)")
guardar(fig, "f1-mapa-errores")

# 2. Antes y después
n0, n1 = R["errores_grandes"]["plano_n_mayor_2"], R["errores_grandes"]["curva_n_mayor_2"]
fig, axs = plt.subplots(1, 2, figsize=(15.1, 6.4), layout="constrained", sharey=True)
for ax, res, t, n in ((axs[0], pl.resid, "Plano", n0), (axs[1], cu.resid, "Plano doblado", n1)):
    ax.scatter(df.tv, df.radio, c=res, cmap=mapa, norm=norma, s=130, edgecolor="#55555533", linewidth=0.5)
    ax.set_title(t, fontsize=30, fontweight="bold", color=NEGRO, loc="left", pad=46)
    ax.text(0, 1.03, f"{n} mercados con error mayor a 2 mil unidades", transform=ax.transAxes, fontsize=23, color=ROJO if t == "Plano" else AZUL, fontweight="bold")
    ax.set_xlabel("TV (miles de USD)")
axs[0].set_ylabel("Radio (miles de USD)")
guardar(fig, "f2-antes-despues")

# 3. Escalera de error
e = R["escalera"]
et = ["Promedio", "TV + radio", "+ TV × radio", "+ TV²"]
va = [R["mae_base"], e["plano"]["mae_te"], e["interaccion"]["mae_te"], e["curva"]["mae_te"]]
fig, ax = plt.subplots(figsize=(15.1, 6.8), layout="constrained")
ba = ax.bar(et, va, color=[CLARO, GRIS, "#F08A8E", ROJO], width=0.62)
for b, v in zip(ba, va):
    ax.text(b.get_x() + b.get_width() / 2, v + 0.08, coma(v), ha="center", fontsize=36, fontweight="bold", color=NEGRO)
ax.axhline(2, color=NEGRO, linestyle=(0, (4, 4)), linewidth=2)
ax.text(3.42, 2.09, "Tolerancia de Daniela: 2", ha="right", fontsize=23, color=NEGRO)
ax.set_ylabel("Error medio en 50 mercados de prueba\n(miles de unidades)")
ax.set_ylim(0, 5.3)
ax.tick_params(axis="x", labelsize=26, colors=NEGRO, length=0)
ax.spines["bottom"].set_color(CLARO)
guardar(fig, "f3-escalera")

# 4. Cuánto gana la radio según la TV
b = cu.params
tvs = np.linspace(0, 296, 200)
gan = (b["radio"] + b["tv:radio"] * tvs) * 1000 * 12 - 1000
gpl = pl.params["radio"] * 1000 * 12 - 1000
eq = R["radio_equilibrio_tv"]
fig, ax = plt.subplots(figsize=(15.1, 7.0), layout="constrained")
ax.axhline(0, color=NEGRO, linewidth=2)
ax.plot(tvs, gan, color=ROJO, linewidth=7)
ax.plot([0, 296], [gpl, gpl], color=GRIS, linewidth=4, linestyle=(0, (5, 4)))
ax.text(292, gpl - 330, "Lo que decía el plano", color=GRIS, fontsize=24, ha="right", fontweight="bold")
ax.fill_between(tvs[tvs <= eq], gan[tvs <= eq], 0, color=ROJO, alpha=0.18)
ax.scatter([eq], [0], s=240, color=NEGRO, zorder=5)
ax.annotate(f"Se paga desde {eq:.0f} mil en TV", (eq, 0), xytext=(72, -610), fontsize=26, fontweight="bold", color=NEGRO, va="center")
for t in (50, 150, 250):
    g = (b["radio"] + b["tv:radio"] * t) * 1000 * 12 - 1000
    ax.scatter([t], [g], s=220, color=ROJO, zorder=5)
    txt = f"+{g:,.0f}".replace(",", ".")
    ax.annotate(txt, (t, g), xytext=(t - 3, g + 240), fontsize=30, fontweight="bold", color=ROJO, ha="right")
ax.set_xlabel("Lo que ese mercado ya invierte en TV (miles de USD)")
ax.set_ylabel("Ganancia por cada 1.000 USD\nadicionales en radio (USD)")
ax.yaxis.set_major_formatter(lambda v, _: f"{v:,.0f}".replace(",", "."))
guardar(fig, "f4-radio-segun-tv")

# 5. Grados
g = R["grados"]
gr = [x["grado"] for x in g]
fig, axs = plt.subplots(1, 2, figsize=(15.1, 6.7), layout="constrained")
ax = axs[0]
ax.plot(gr, [x["r2_tr"] for x in g], color=NEGRO, linewidth=6, marker="o", markersize=14)
ax.set_ylim(0.88, 1.005)
ax.set_title("R² con los datos de entrenamiento", fontsize=26, fontweight="bold", color=NEGRO, loc="left", pad=16)
ax.text(7, g[-1]["r2_tr"] - 0.013, coma(g[-1]["r2_tr"], 3), ha="right", fontsize=32, fontweight="bold", color=NEGRO)
ax.set_xlabel("Grado del polinomio")
ax.set_xticks(gr)
ax = axs[1]
ax.plot(gr, [x["mae_te"] for x in g], color=ROJO, linewidth=6, marker="o", markersize=14)
ax.plot(gr, [x["mae_tr"] for x in g], color=NEGRO, linewidth=4, marker="o", markersize=9)
ax.set_yscale("log")
ax.set_yticks([0.1, 0.3, 1, 3, 10, 40])
ax.yaxis.set_major_formatter(lambda v, _: coma(v, 1) if v < 1 else f"{v:.0f}")
ax.yaxis.set_minor_formatter(lambda v, _: "")
ax.set_title("Error medio, escala logarítmica", fontsize=26, fontweight="bold", color=NEGRO, loc="left", pad=16)
ax.text(6.55, 34, coma(g[-1]["mae_te"], 1), fontsize=32, fontweight="bold", color=ROJO, ha="right")
ax.text(2.4, 0.86, "Prueba", fontsize=26, fontweight="bold", color=ROJO)
ax.text(1, 0.105, "Entrenamiento", fontsize=26, fontweight="bold", color=NEGRO)
ax.set_xlabel("Grado del polinomio")
ax.set_xticks(gr)
guardar(fig, "f5-grados")

# 6. Un mercado
p6 = make_pipeline(PolynomialFeatures(6, include_bias=False), StandardScaler(), LinearRegression()).fit(tr[C], tr.ventas)
pr = p6.predict(te[C])
g6 = R["grado6"]
fig, ax = plt.subplots(figsize=(15.1, 7.0), layout="constrained")
ax.axhline(0, color=CLARO, linewidth=2)
ord_ = np.argsort(te.ventas.values)
x = np.arange(len(te))
ax.vlines(x, te.ventas.values[ord_], pr[ord_], color=ROJO, linewidth=3)
ax.scatter(x, te.ventas.values[ord_], s=120, color=NEGRO, zorder=4, label="Real")
ax.scatter(x, pr[ord_], s=120, facecolor="white", edgecolor=ROJO, linewidth=3, zorder=4, label="Pronóstico")
k = int(np.where(te.mercado.values[ord_] == g6["peor_mercado"])[0][0])
ax.annotate(f"Mercado {g6['peor_mercado']}: el modelo pronostica\n−{coma(abs(g6['peor_pred']), 0)} mil unidades. Vendió {coma(g6['peor_real'], 1)} mil.", (k, g6["peor_pred"]), xytext=(k + 1.5, g6["peor_pred"] + 22), fontsize=28, fontweight="bold", color=ROJO, va="center")
ax.set_ylabel("Ventas (miles de unidades)")
ax.set_xlabel("Los 50 mercados de prueba, de menor a mayor venta real")
ax.set_xticks([])
ax.legend(frameon=False, loc="upper left", fontsize=24, ncol=2)
guardar(fig, "f6-un-mercado")

# 7. Lasso: columnas vivas y error de validación por alfa
L = R["rejilla"]["lasso"]
al = [x["alpha"] for x in L]
fig, axs = plt.subplots(2, 1, figsize=(15.1, 7.4), layout="constrained", sharex=True, gridspec_kw={"height_ratios": [1.15, 1]})
ax = axs[0]
bb = ax.bar(range(len(al)), [x["vivas"] for x in L], color=[ROJO if x["vivas"] == 2 else GRIS for x in L], width=0.66)
for i, x in enumerate(L):
    ax.text(i, x["vivas"] + 1.2, str(x["vivas"]), ha="center", fontsize=30, fontweight="bold", color=NEGRO)
ax.set_ylim(0, 47)
ax.set_title("Columnas que sobreviven, de 55", fontsize=26, fontweight="bold", color=NEGRO, loc="left")
ax.set_yticks([])
ax.spines["left"].set_visible(False)
ax = axs[1]
ax.plot(range(len(al)), [x["cv_mae"] for x in L], color=ROJO, linewidth=6, marker="o", markersize=14)
m = int(np.argmin([x["cv_mae"] for x in L]))
ax.scatter([m], [L[m]["cv_mae"]], s=720, facecolor="none", edgecolor=NEGRO, linewidth=3.5, zorder=5)
ax.text(m, L[m]["cv_mae"] + 0.13, "El mejor en validación", ha="center", fontsize=25, fontweight="bold", color=NEGRO)
ax.set_title("Error medio en validación cruzada", fontsize=26, fontweight="bold", color=NEGRO, loc="left")
ax.set_xticks(range(len(al)))
ax.set_xticklabels([f"{a:g}".replace(".", ",") for a in al], fontsize=22)
ax.set_xlabel("Fuerza del freno α")
ax.set_ylim(0.2, 1.2)
guardar(fig, "f7-lasso-rejilla")

# 8. Resultado final
Rj = R["rejilla"]
g5 = R["grados"][4]
et = ["Plano", "Grado 5\nsin freno", "Grado 5\ncon Ridge", "Grado 5\ncon Lasso", "Curva\ncon TV²", "Curva\ncon √TV"]
col = [2, 55, 55, Rj["lasso_mejor"]["vivas"], 4, 4]
va = [e["plano"]["mae_te"], g5["mae_te"], Rj["ridge_mejor"]["mae_te"], Rj["lasso_mejor"]["mae_te"], e["curva"]["mae_te"], e["raiz_tv"]["mae_te"]]
fig, ax = plt.subplots(figsize=(15.1, 6.9), layout="constrained")
ba = ax.bar(et, va, color=[GRIS, CLARO, "#F08A8E", "#F08A8E", NEGRO, ROJO], width=0.64)
for b, v, c in zip(ba, va, col):
    ax.text(b.get_x() + b.get_width() / 2, v + 0.03, coma(v), ha="center", fontsize=34, fontweight="bold", color=NEGRO)
    ax.text(b.get_x() + b.get_width() / 2, v + 0.17, f"{c} columnas", ha="center", fontsize=21, color=GRIS)
ax.set_ylabel("Error medio en prueba\n(miles de unidades)")
ax.set_ylim(0, 2.1)
ax.tick_params(axis="x", labelsize=23, colors=NEGRO, length=0)
ax.spines["bottom"].set_color(CLARO)
guardar(fig, "f8-final")

# 9. CO2: coeficiente de consumo combinado en seis mitades
m_ = R["co2"]["mitades"]
fig, ax = plt.subplots(figsize=(15.1, 5.4), layout="constrained")
vars_ = [("FUELCONSUMPTION_CITY", "Consumo ciudad"), ("FUELCONSUMPTION_HWY", "Consumo carretera"), ("FUELCONSUMPTION_COMB", "Consumo combinado")]
for j, (nom, col_) in enumerate((("ols", GRIS), ("ridge", ROJO), ("lasso", NEGRO))):
    for i, (v, _) in enumerate(vars_):
        lo, hi = m_[nom][v]
        y = i + (j - 1) * 0.24
        ax.plot([lo, hi], [y, y], color=col_, linewidth=11, solid_capstyle="round")
        if hi - lo < 1:
            ax.scatter([lo], [y], s=240, color=col_)
ax.set_yticks(range(3))
ax.set_yticklabels([n for _, n in vars_], fontsize=24, color=NEGRO)
ax.tick_params(axis="y", length=0)
ax.axvline(0, color=CLARO, linewidth=2)
ax.text(112, 1.28, "Sin freno", fontsize=26, color=GRIS, fontweight="bold", va="center")
ax.text(112, 1.0, "Ridge", fontsize=26, color=ROJO, fontweight="bold", va="center")
ax.text(112, 0.72, "Lasso", fontsize=26, color=NEGRO, fontweight="bold", va="center")
ax.set_xlabel("Rango del coeficiente en seis mitades distintas de los datos")
guardar(fig, "f9-co2")
print("figuras listas")

# 10. Saturación: √TV frente a TV²
e_c, e_r = R["escalera"]["curva"], R["escalera"]["raiz_tv"]
ba_ = df[df.radio <= 12]
rm = ba_.radio.mean()
x_ = np.linspace(0.7, 296, 300)
y_c = e_c["intercepto"] + e_c["coef"]["tv"] * x_ + e_c["coef"]["radio"] * rm + e_c["coef"]["tv_radio"] * x_ * rm + e_c["coef"]["tv2"] * x_ ** 2
y_r = e_r["intercepto"] + e_r["coef"]["tv"] * x_ + e_r["coef"]["raiz_tv"] * np.sqrt(x_) + e_r["coef"]["radio"] * rm + e_r["coef"]["tv_radio"] * x_ * rm
fig, ax = plt.subplots(figsize=(15.1, 7.0), layout="constrained")
ax.scatter(ba_.tv, ba_.ventas, s=110, color=NEGRO, zorder=3)
ax.plot(x_, y_c, color=GRIS, linewidth=5)
ax.plot(x_, y_r, color=ROJO, linewidth=6)
ax.text(118, 8.1, "Con TV²: arranca bajo y se dobla tarde", fontsize=26, color=GRIS, fontweight="bold")
ax.text(20, 14.2, "Con √TV: sube rápido y luego se aplana", fontsize=26, color=ROJO, fontweight="bold")
ax.set_xlabel("TV (miles de USD), mercados con poca radio")
ax.set_ylabel("Ventas (miles de unidades)")
ax.set_ylim(0, 16)
guardar(fig, "f10-saturacion")
print("f10 lista")
