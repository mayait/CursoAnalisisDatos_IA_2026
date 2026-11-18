# -*- coding: utf-8 -*-
"""Cifras y salidas de código de los sub-videos de interacciones. El código que se ve en pantalla se ejecuta aquí de verdad.

Uso: python generar_interacciones.py  -> cifras_inter.json
"""
import contextlib
import io
import json
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

warnings.filterwarnings("ignore")
AQUI = Path(__file__).resolve().parent
D2L = AQUI.parent / "d2l"
df = pd.read_csv(D2L / "mercados-bebidas-cumbre.csv")
R = {}
grupos = {"alto": df[df.radio >= 35], "bajo": df[df.radio <= 12], "medio": df[(df.radio > 12) & (df.radio < 35)]}
m = smf.ols("ventas ~ tv * radio", df).fit()
b = m.params
R["modelo"] = {k: float(v) for k, v in b.items()} | {"r2": float(m.rsquared)}
pl = smf.ols("ventas ~ tv + radio", df).fit()
R["plano"] = {k: float(v) for k, v in pl.params.items()}
R["grupos"] = {}
for k, g in grupos.items():
    s = smf.ols("ventas ~ tv", g).fit().params
    r = g.radio.mean()
    R["grupos"][k] = dict(n=len(g), radio=float(r), tv=float(g.tv.mean()), pend_sep=float(s.tv), pend_modelo=float(b.tv + b["tv:radio"] * r), int_sep=float(s.Intercept))
R["cortes"] = {f"{a}-{c}": [len(df[df.radio <= a]), len(df[df.radio >= c]), float(smf.ols("ventas ~ tv", df[df.radio <= a]).fit().params.tv), float(smf.ols("ventas ~ tv", df[df.radio >= c]).fit().params.tv)] for a, c in ((10, 40), (15, 30), (20, 25))}
R["corr_tv_radio"] = float(df.tv.corr(df.radio))
R["pend_por_radio"] = {str(r): float((b.tv + b["tv:radio"] * r) * 1000) for r in (0, 20, 45)}

# CO2: numérica por categórica
f = pd.read_csv(D2L / "consumo-combustible-co2.csv")
R["co2"] = {"n": len(f), "grupos": {}}
for t, g in f.groupby("FUELTYPE"):
    s = smf.ols("CO2EMISSIONS ~ FUELCONSUMPTION_COMB", g).fit().params
    R["co2"]["grupos"][t] = dict(n=len(g), b=float(s.FUELCONSUMPTION_COMB), a=float(s.Intercept), lo=float(g.FUELCONSUMPTION_COMB.min()), hi=float(g.FUELCONSUMPTION_COMB.max()))
mues = f.sample(240, random_state=4)
R["co2"]["puntos"] = [[float(a), float(c), t] for a, c, t in zip(mues.FUELCONSUMPTION_COMB, mues.CO2EMISSIONS, mues.FUELTYPE)]

# Superstore: descuento por categoría, sobre utilidad por línea
s_ = pd.read_csv(AQUI / "datos" / "superstore_2026.csv")
s_["margen"] = s_.utilidad / s_.venta
ms = smf.ols("margen ~ descuento * C(categoria)", s_).fit()
R["super"] = {"n": len(s_), "r2": float(ms.rsquared), "params": {k: float(v) for k, v in ms.params.items()}, "p": {k: float(v) for k, v in ms.pvalues.items()}, "cat": {}}
for c, g in s_.groupby("categoria"):
    q = smf.ols("margen ~ descuento", g).fit().params
    R["super"]["cat"][c] = dict(n=len(g), b=float(q.descuento), a=float(q.Intercept), medias={str(k): float(v) for k, v in g.groupby("descuento").margen.mean().items() if (g.descuento == k).sum() >= 15})

# Titanic: categórica por categórica
t = pd.read_csv(AQUI / "datos" / "titanic.csv")
R["titanic"] = {"tabla": {s: {str(c): float(v) for c, v in t[t.sex == s].groupby("pclass").survived.mean().items()} for s in ("female", "male")}, "n": len(t)}

# Sin interacción: radio por prensa
mp = smf.ols("ventas ~ tv + radio * prensa", df).fit()
R["radio_prensa"] = dict(p=float(mp.pvalues["radio:prensa"]), b=float(mp.params["radio:prensa"]), params={k: float(v) for k, v in mp.params.items()}, prensa_q=[float(df.prensa.quantile(0.1)), float(df.prensa.quantile(0.9))], tv=float(df.tv.mean()))

# Fallo común: el producto sin las variables originales
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error as mae
from sklearn.model_selection import train_test_split
tr, te = train_test_split(df, test_size=0.25, random_state=42)
def err(cols):
    tr2, te2 = tr.assign(tv_radio=tr.tv * tr.radio), te.assign(tv_radio=te.tv * te.radio)
    return float(mae(te2.ventas, LinearRegression().fit(tr2[cols], tr2.ventas).predict(te2[cols])))
R["fallo"] = dict(solo_producto=err(["tv_radio"]), completo=err(["tv", "radio", "tv_radio"]), plano=err(["tv", "radio"]))

SNIPS = {
    "p1": """df["tv_radio"] = df.tv * df.radio
X = df[["tv", "radio", "tv_radio"]]
m = LinearRegression().fit(X, df.ventas)
print(m.intercept_.round(3), m.coef_.round(5))""",
    "p2": """m = smf.ols("ventas ~ tv * radio", df).fit()
print(m.params.round(5))""",
    "p3": """b = m.params
for radio in (0, 20, 45):
    pendiente = b["tv"] + b["tv:radio"] * radio
    print(radio, round(pendiente * 1000, 1))""",
    "p4": """alta = df[df.radio >= 35]
baja = df[df.radio <= 12]
print(len(alta), round(alta.radio.mean(), 1))
print(len(baja), round(baja.radio.mean(), 1))""",
    "p5": """rej = pd.DataFrame({"tv": range(0, 300)})
for g, c in ((alta, "red"), (baja, "black")):
    plt.scatter(g.tv, g.ventas, color=c)
    r = g.radio.mean()
    y = m.predict(rej.assign(radio=r))
    plt.plot(rej.tv, y, color=c)""",
    "p6": """f = pd.read_csv("consumo-combustible-co2.csv")
c = smf.ols("CO2EMISSIONS ~ FUELCONSUMPTION_COMB"
            " * C(FUELTYPE)", f).fit()
print(c.params.filter(like="COMB").round(2).to_string())""",
    "p7": """pf = PolynomialFeatures(2, interaction_only=True,
                        include_bias=False)
pf.fit(df[["tv", "radio", "prensa"]])
print(pf.get_feature_names_out())""",
    "p8": """tr, te = train_test_split(df, test_size=0.25,
                          random_state=42)
for cols in (["tv", "radio"], ["tv", "radio", "tv_radio"]):
    p = LinearRegression().fit(tr[cols], tr.ventas)
    print(len(cols), round(mae(te.ventas, p.predict(te[cols])), 3))""",
}
from sklearn.preprocessing import PolynomialFeatures
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
ns = {"df": df.copy(), "plt": plt, "pd": pd, "smf": smf, "LinearRegression": LinearRegression, "PolynomialFeatures": PolynomialFeatures, "train_test_split": train_test_split, "mae": mae}
import os
os.chdir(D2L)
R["snips"] = {}
for k, c in SNIPS.items():
    b_ = io.StringIO()
    with contextlib.redirect_stdout(b_):
        if k == "p5":
            plt.figure(figsize=(5.8, 4.1), dpi=130)
        exec(c, ns)
        if k == "p5":
            plt.xlabel("tv"); plt.ylabel("ventas"); plt.tight_layout(); plt.savefig(AQUI / "datos" / "salida_p5.png"); plt.close()
    R["snips"][k] = {"codigo": c, "salida": b_.getvalue().rstrip()}
(AQUI / "cifras_inter.json").write_text(json.dumps(R, indent=1, ensure_ascii=False))
print(json.dumps({k: R[k] for k in ("grupos", "cortes", "pend_por_radio", "radio_prensa", "fallo", "titanic")}, ensure_ascii=False)[:1800])
print({c: (round(v["a"], 3), round(v["b"], 3), v["n"]) for c, v in R["super"]["cat"].items()}, round(R["super"]["r2"], 3), {k: round(v, 4) for k, v in R["super"]["p"].items()})
print({c: list(v["medias"].items())[:8] for c, v in R["super"]["cat"].items()})
for k, v in R["snips"].items():
    print("---", k); print(v["salida"])
