# -*- coding: utf-8 -*-
"""Genera el cuaderno del taller en dos versiones: la del estudiante y la solución local (no se sube a D2L ni a GitHub).

Uso: python generar_cuaderno.py  -> d2l/taller-ajustes-daniela.ipynb y solucion/taller-ajustes-daniela-SOLUCION.ipynb
La solución comprueba con assert que sus números coinciden con cifras.json.
"""
import json
from pathlib import Path

import nbformat as nbf

AQUI = Path(__file__).resolve().parent
(AQUI / "solucion").mkdir(exist_ok=True)
R = json.loads((AQUI / "cifras.json").read_text(encoding="utf-8"))

M, C = "m", "c"
# Celda tipo C con dos variantes: (estudiante, solución)
CELDAS = [
    (M, """# Taller · Una recta no se dobla

El viernes Daniela prometió 14.420 unidades al comité de Bebidas Cumbre usando el plano de TV y radio. Hoy revisas esa cifra, le enseñas al modelo a doblarse y aprendes a frenarlo cuando se dobla de más. Este cuaderno sigue las seis etapas de la página de D2L. No necesitas escribir Python: pídele cada celda a Claude, Gemini o Antigravity. Lo que se califica es que sepas qué te dio y lo hayas verificado."""),
    (M, """> **Hoy haces** · Encuentras dónde falla el plano, agregas curvas e interacciones, corriges la promesa, contestas la oferta de la agencia y pruebas Ridge y Lasso.
>
> **Entrega** · Enlace público de este cuaderno con todo ejecutado, memo de una página y `prompts.md`.
>
> **Antes de empezar** · En Colab, arrastra `mercados-bebidas-cumbre.csv` y `consumo-combustible-co2.csv` al panel de archivos de la izquierda."""),
    (C, """# --- Setup ---
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import Lasso, LinearRegression, Ridge
from sklearn.metrics import mean_absolute_error as mae, r2_score
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

df = pd.read_csv("mercados-bebidas-cumbre.csv")
MARGEN = 12  # USD de margen por unidad. Ventas en miles de unidades, inversión en miles de USD.

# Train y test: siempre la misma división, la del caso anterior
tr, te = train_test_split(df, test_size=0.25, random_state=42)
MEDIOS = ["tv", "radio", "prensa"]
print(df.shape, tr.shape, te.shape)"""),
    (M, """## Etapa 1 · Dónde falla el plano

Ajusta el plano `ventas ~ tv + radio` con los 200 mercados. Calcula el error de cada mercado (real menos pronóstico), dibújalo en un gráfico de TV contra radio y promedia los mercados con `tv <= 90` y `radio >= 35`."""),
    (C, ("""# Pega aquí el código que te entregue Claude, Gemini o Antigravity.
# Pista de prompt: ajusta ventas contra tv y radio con los 200 mercados, calcula el error de cada uno
# y dibuja tv contra radio con el color según ese error. Luego promedia los mercados con tv <= 90 y radio >= 35.
""", """plano = smf.ols("ventas ~ tv + radio", df).fit()
df["error_plano"] = plano.resid
plt.figure(figsize=(9, 4.5))
plt.scatter(df.tv, df.radio, c=df.error_plano, cmap="RdBu", vmin=-5, vmax=5, s=60)
plt.colorbar(label="error (real menos pronóstico)")
plt.xlabel("TV"); plt.ylabel("Radio")
plt.title("El plano promete de más donde hay un solo medio")
plt.tight_layout(); plt.show()
vecinos = df[(df.tv <= 90) & (df.radio >= 35)]
print(len(vecinos), vecinos.ventas.mean(), plano.fittedvalues[vecinos.index].mean(), vecinos.error_plano.mean())
assert abs(vecinos.error_plano.mean() - (%(vec)r)) < 1e-6
""" % {"vec": R["vecinos_daniela"]["res_plano"]})),
    (M, """**Decisión para el memo.** ¿El error del plano es ruido o patrón? Si es patrón, ¿en qué tipo de mercado promete de más?

## Etapa 2 · Doblar el plano

Agrega `tv × radio` y después `tv²`. Mide cada modelo con los 50 mercados de prueba y compáralo con la línea base."""),
    (C, ("""def medir(modelo, cols, nombre):
    \"\"\"Entrena con tr, mide error medio absoluto en te.\"\"\"
    modelo.fit(tr[cols], tr.ventas)
    print(f"{nombre:28s} error prueba {mae(te.ventas, modelo.predict(te[cols])):.3f}")

for parte in (tr, te):
    parte.loc[:, "tv_radio"] = parte.tv * parte.radio

# Pega aquí el código que te entregue tu asistente.
# Pista de prompt: usa las variables tr (train) y te (test). Crea tv al cuadrado y mide con la función medir
# cuatro modelos: el promedio, tv y radio, con tv por radio, y con tv por radio y tv al cuadrado.
""", """def medir(modelo, cols, nombre):
    modelo.fit(tr[cols], tr.ventas)
    err = mae(te.ventas, modelo.predict(te[cols]))
    print(f"{nombre:28s} error prueba {err:.3f}")
    return err

tr, te = tr.copy(), te.copy()
for parte in (tr, te):
    parte["tv_radio"] = parte.tv * parte.radio
    parte["tv2"] = parte.tv ** 2

base = medir(DummyRegressor(), ["tv"], "promedio")
pl = medir(LinearRegression(), ["tv", "radio"], "tv + radio")
it = medir(LinearRegression(), ["tv", "radio", "tv_radio"], "con interacción")
cu = medir(LinearRegression(), ["tv", "radio", "tv_radio", "tv2"], "con interacción y curva")
assert abs(cu - (%(cu)r)) < 1e-6 and abs(pl - (%(pl)r)) < 1e-6
""" % {"cu": R["escalera"]["curva"]["mae_te"], "pl": R["escalera"]["plano"]["mae_te"]})),
    (M, """**Decisión para el memo.** ¿Cuál de las dos columnas aportó más? ¿Por qué tiene sentido de negocio?

## Etapa 3 · Corregir la promesa

Ajusta el modelo de cuatro columnas con los 200 mercados. Pronostica los dos planes y calcula la utilidad: unidades por margen menos inversión. Luego calcula cuánto rinde la radio cuando la TV vale 50, 150 y 250."""),
    (C, ("""# Pega aquí el código que te entregue tu asistente.
# Pista de prompt: ajusta el modelo de cuatro columnas con los 200 mercados y pronostica TV 150 con radio 25,
# y TV 50 con radio 49. Todo está en miles y cada unidad deja 12 USD. Dame unidades, margen, inversión y utilidad.
# Luego dime cuántas unidades trae cada mil USD en radio con TV de 50, 150 y 250.
""", """curva = smf.ols("ventas ~ tv + radio + tv:radio + I(tv**2)", df).fit()
planes = pd.DataFrame({"tv": [150, 50], "radio": [25, 49]}, index=["agencia", "daniela"])
planes["ventas"] = curva.predict(planes)
planes["utilidad"] = planes.ventas * MARGEN - planes.tv - planes.radio
print(planes.round(2))
b = curva.params
for t in (50, 150, 250):
    u = (b["radio"] + b["tv:radio"] * t) * 1000
    print(f"TV {t}: {u:.0f} unidades por mil USD en radio, ganancia {u * MARGEN - 1000:,.0f} USD")
assert abs(planes.loc["daniela", "ventas"] - (%(d)r)) < 1e-6
""" % {"d": R["planes"]["daniela"]["curva"]})),
    (M, """**Decisión para el memo.** ¿Cambia la decisión de lanzar con el plan de Daniela? ¿Qué cifra le dices al comité y cómo explicas que bajó?

## Etapa 4 · La oferta de la agencia

Ajusta polinomios de grado 1 a 7 con los tres medios y mira el R² de entrenamiento junto al error de prueba."""),
    (C, ("""# Pega aquí el código que te entregue tu asistente.
# Pista de prompt: con los tres medios, ajusta polinomios de grado 1 a 7 usando solo train. Dame una tabla con
# columnas, R² de train, error de train y error de test. Luego el error del grado 6 mercado por mercado.
""", """filas = []
for d in range(1, 8):
    p = make_pipeline(PolynomialFeatures(d, include_bias=False), StandardScaler(), LinearRegression())
    p.fit(tr[MEDIOS], tr.ventas)
    filas.append({"grado": d, "columnas": p[0].n_output_features_, "r2_entrenamiento": p.score(tr[MEDIOS], tr.ventas),
                  "error_entrenamiento": mae(tr.ventas, p.predict(tr[MEDIOS])), "error_prueba": mae(te.ventas, p.predict(te[MEDIOS]))})
tabla = pd.DataFrame(filas)
print(tabla.round(3).to_string(index=False))
assert abs(tabla.loc[5, "error_prueba"] - (%(g6)r)) < 1e-4
""" % {"g6": R["grados"][5]["mae_te"]})),
    (M, """**Decisión para el memo.** ¿Compran el modelo de la agencia? Respondan con el número que un comité entendería.

## Etapa 5 · El freno

Grado 5 con los tres medios. Elige α con validación cruzada dentro de los 150 de entrenamiento. Recién después abre los 50 de prueba."""),
    (C, ("""kf = KFold(5, shuffle=True, random_state=42)
ALPHAS_LASSO = [0.0001, 0.0003, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0]
ALPHAS_RIDGE = [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30, 100]

def freno(modelo):
    return make_pipeline(PolynomialFeatures(5, include_bias=False), StandardScaler(), modelo)

# Pega aquí el código que te entregue tu asistente.
# Pista de prompt: para cada alfa de las listas, calcula el error absoluto medio con validación cruzada de cinco
# partes, solo dentro de train. Elige el mejor alfa de Lasso y de Ridge. Al final mide en test y dime cuántas
# columnas quedan vivas. Revisa: pregúntale si usó test para elegir alfa.
""", """kf = KFold(5, shuffle=True, random_state=42)
ALPHAS_LASSO = [0.0001, 0.0003, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0]
ALPHAS_RIDGE = [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30, 100]

def freno(modelo):
    return make_pipeline(PolynomialFeatures(5, include_bias=False), StandardScaler(), modelo)

def rejilla(alphas, crear):
    filas = []
    for a in alphas:
        p = freno(crear(a))
        cv = -cross_val_score(p, tr[MEDIOS], tr.ventas, cv=kf, scoring="neg_mean_absolute_error").mean()
        p.fit(tr[MEDIOS], tr.ventas)
        filas.append({"alpha": a, "error_validacion": cv, "columnas_vivas": int((abs(p[-1].coef_) > 1e-9).sum()), "error_prueba": mae(te.ventas, p.predict(te[MEDIOS]))})
    return pd.DataFrame(filas)

la = rejilla(ALPHAS_LASSO, lambda a: Lasso(alpha=a, max_iter=300000))
ri = rejilla(ALPHAS_RIDGE, lambda a: Ridge(alpha=a))
print(la.round(3).to_string(index=False)); print(); print(ri.round(3).to_string(index=False))
mejor = la.loc[la.error_validacion.idxmin()]
print("mejor Lasso", mejor.to_dict())
assert mejor.alpha == %(a)r and int(mejor.columnas_vivas) == %(v)r
""" % {"a": R["rejilla"]["lasso_mejor"]["alpha"], "v": R["rejilla"]["lasso_mejor"]["vivas"]})),
    (M, """**Decisión para el memo.** ¿Con cuál se queda Daniela: la curva de cuatro columnas o el Lasso? Argumenten con error y con lo que se puede explicar.

## Etapa 6 · En casa

Primero propón una columna con sentido de negocio y gánale al modelo de cuatro columnas en los mismos 50 mercados. Luego abre el dataset de CO₂ de años anteriores y mira qué le pasa a un coeficiente cuando las columnas son casi copias."""),
    (C, ("""# Pega aquí el código que te entregue tu asistente.
# Pista de prompt: quiero probar una columna nueva porque [tu razón de negocio]. Agrégala al modelo de cuatro
# columnas, entrena con train y mide en los mismos 50 de test. No pruebes otras columnas por tu cuenta.
""", """for parte in (tr, te):
    parte["raiz_tv"] = np.sqrt(parte.tv)
r4 = medir(LinearRegression(), ["tv", "raiz_tv", "radio", "tv_radio"], "tv, raíz de tv, radio, tv × radio")
assert abs(r4 - (%(r)r)) < 1e-6
""" % {"r": R["escalera"]["raiz_tv"]["mae_te"]})),
    (C, ("""co2 = pd.read_csv("consumo-combustible-co2.csv")
COLS = ["ENGINESIZE", "CYLINDERS", "FUELCONSUMPTION_CITY", "FUELCONSUMPTION_HWY", "FUELCONSUMPTION_COMB", "FUELCONSUMPTION_COMB_MPG"]

# Pega aquí el código que te entregue tu asistente.
# Pista de prompt: toma seis mitades distintas (random_state de 0 a 5), estandariza, y ajusta sin freno, con
# Ridge alpha 50 y con Lasso alpha 1. Dame una tabla con el coeficiente de FUELCONSUMPTION_COMB en cada mitad.
""", """co2 = pd.read_csv("consumo-combustible-co2.csv")
COLS = ["ENGINESIZE", "CYLINDERS", "FUELCONSUMPTION_CITY", "FUELCONSUMPTION_HWY", "FUELCONSUMPTION_COMB", "FUELCONSUMPTION_COMB_MPG"]
print(co2[COLS].corr().round(3))
filas = []
for seed in range(6):
    mitad = co2.sample(frac=0.5, random_state=seed)
    for n, m in (("sin freno", LinearRegression()), ("ridge", Ridge(alpha=50)), ("lasso", Lasso(alpha=1, max_iter=300000))):
        p = make_pipeline(StandardScaler(), m).fit(mitad[COLS], mitad.CO2EMISSIONS)
        filas.append({"seed": seed, "modelo": n, "coef_comb": p[-1].coef_[4]})
res = pd.DataFrame(filas).pivot(index="seed", columns="modelo", values="coef_comb")
print(res.round(1))
assert abs(res["sin freno"].min() - (%(lo)r)) < 1e-4 and abs(res["sin freno"].max() - (%(hi)r)) < 1e-4
""" % {"lo": R["co2"]["mitades"]["ols"]["FUELCONSUMPTION_COMB"][0], "hi": R["co2"]["mitades"]["ols"]["FUELCONSUMPTION_COMB"][1]})),
    (M, """**Decisión para el memo.** ¿Cuándo le recomendarías a Daniela Ridge, cuándo Lasso y cuándo ninguno?"""),
]


def construir(sol):
    nb = nbf.v4.new_notebook()
    nb.metadata = {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}, "language_info": {"name": "python", "version": "3.11"}}
    for t, s in CELDAS:
        if t == M:
            nb.cells.append(nbf.v4.new_markdown_cell(s))
        else:
            txt = s if isinstance(s, str) else (s[1] if sol else s[0])
            nb.cells.append(nbf.v4.new_code_cell(txt.strip()))
    return nb


nbf.write(construir(False), AQUI / "d2l" / "taller-ajustes-daniela.ipynb")
nbf.write(construir(True), AQUI / "solucion" / "taller-ajustes-daniela-SOLUCION.ipynb")
print("cuadernos listos")
