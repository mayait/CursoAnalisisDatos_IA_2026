# -*- coding: utf-8 -*-
"""Calcula todas las cifras de la clase de regresión con ajustes. Es la fuente única: deck, página D2L y guía salen de aquí.

Uso: python generar_cifras.py  -> cifras.json y cifras_caso.txt
Misma división del caso Daniela: 150 mercados para entrenar y 50 para probar, random_state 42.
"""
import json
import warnings
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from sklearn.linear_model import Lasso, LassoCV, LinearRegression, Ridge, RidgeCV
from sklearn.metrics import mean_absolute_error as mae, r2_score as r2
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

warnings.filterwarnings("ignore")
AQUI = Path(__file__).resolve().parent
df = pd.read_csv(AQUI / "d2l" / "mercados-bebidas-cumbre.csv")
MARGEN = 12
C = ["tv", "radio", "prensa"]
tr, te = train_test_split(df, test_size=0.25, random_state=42)
kf = KFold(5, shuffle=True, random_state=42)
R = {}


def med(p, a, b):
    return dict(mae_tr=mae(tr.ventas, p.predict(a)), mae_te=mae(te.ventas, p.predict(b)),
                r2_tr=r2(tr.ventas, p.predict(a)), r2_te=r2(te.ventas, p.predict(b)))


def ext(d):
    return d.assign(tv_radio=d.tv * d.radio, tv2=d.tv ** 2, raiz_tv=np.sqrt(d.tv), raiz_tv_radio=np.sqrt(d.tv) * d.radio)


T, E = ext(tr), ext(te)
A = ext(df)
R["mae_base"] = mae(te.ventas, np.full(len(te), tr.ventas.mean()))

# Escalera de modelos con columnas a mano
esc = {"plano": ["tv", "radio"], "interaccion": ["tv", "radio", "tv_radio"], "curva": ["tv", "radio", "tv_radio", "tv2"],
       "raiz": ["raiz_tv", "radio", "raiz_tv_radio"], "raiz_tv": ["tv", "raiz_tv", "radio", "tv_radio"]}
R["escalera"] = {}
for k, v in esc.items():
    m = LinearRegression().fit(T[v], tr.ventas)
    R["escalera"][k] = dict(columnas=v, **med(m, T[v], E[v]), coef=dict(zip(v, m.coef_.tolist())), intercepto=float(m.intercept_))

# Modelos sobre los 200 mercados, para leer y prescribir
pl = smf.ols("ventas ~ tv + radio", df).fit()
cu = smf.ols("ventas ~ tv + radio + tv:radio + I(tv**2)", df).fit()
R["plano_200"] = pl.params.to_dict() | {"r2": pl.rsquared}
R["curva_200"] = cu.params.to_dict() | {"r2": cu.rsquared, "r2a": cu.rsquared_adj}
b = cu.params


def rad_marg(tv):  # unidades por 1.000 USD en radio
    return (b["radio"] + b["tv:radio"] * tv) * 1000


def tv_marg(tv, radio):
    return (b["tv"] + 2 * b["I(tv ** 2)"] * tv + b["tv:radio"] * radio) * 1000


R["marginal"] = {"radio_tv50": rad_marg(50), "radio_tv150": rad_marg(150), "radio_tv250": rad_marg(250),
                 "tv_50_10": tv_marg(50, 10), "tv_50_40": tv_marg(50, 40), "tv_250_10": tv_marg(250, 10), "tv_250_40": tv_marg(250, 40)}
R["ganancia_por_mil"] = {k: v * MARGEN - 1000 for k, v in R["marginal"].items()}
R["plano_ganancia"] = {"radio": pl.params["radio"] * 1000 * MARGEN - 1000, "tv": pl.params["tv"] * 1000 * MARGEN - 1000}

# La promesa al comité
planes = {"agencia": (150, 25), "daniela": (50, 49)}
R["planes"] = {}
for k, (tv, ra) in planes.items():
    x = pd.DataFrame({"tv": [tv], "radio": [ra]})
    p0 = pl.get_prediction(x).summary_frame(alpha=0.10).iloc[0]
    p1 = cu.get_prediction(x).summary_frame(alpha=0.10).iloc[0]
    inv = tv + ra
    R["planes"][k] = dict(tv=tv, radio=ra, inversion=inv, plano=p0["mean"], plano_lo=p0["obs_ci_lower"], plano_hi=p0["obs_ci_upper"],
                          curva=p1["mean"], curva_lo=p1["obs_ci_lower"], curva_hi=p1["obs_ci_upper"],
                          margen_plano=p0["mean"] * MARGEN, margen_curva=p1["mean"] * MARGEN, utilidad_plano=p0["mean"] * MARGEN - inv,
                          utilidad_curva=p1["mean"] * MARGEN - inv, utilidad_peor=p1["obs_ci_lower"] * MARGEN - inv)

# Dónde falla el plano: mercados por tercios de inversión
df["res_plano"] = pl.resid
df["res_curva"] = cu.resid
vec = df[(df.tv <= 90) & (df.radio >= 35)]
R["vecinos_daniela"] = dict(n=len(vec), real=vec.ventas.mean(), plano=pl.fittedvalues[vec.index].mean(), curva=cu.fittedvalues[vec.index].mean(),
                            res_plano=vec.res_plano.mean(), res_curva=vec.res_curva.mean(), tv=vec.tv.mean(), radio=vec.radio.mean())
alto = df[(df.tv >= 200) & (df.radio >= 35)]
R["ambos_altos"] = dict(n=len(alto), real=alto.ventas.mean(), plano=pl.fittedvalues[alto.index].mean(), res_plano=alto.res_plano.mean(), res_curva=alto.res_curva.mean())
bajo = df[(df.tv >= 200) & (df.radio <= 10)]
R["tv_sola"] = dict(n=len(bajo), real=bajo.ventas.mean(), plano=pl.fittedvalues[bajo.index].mean(), res_plano=bajo.res_plano.mean(), res_curva=bajo.res_curva.mean())
R["errores_grandes"] = {"plano_n_mayor_2": int((pl.resid.abs() > 2).sum()), "curva_n_mayor_2": int((cu.resid.abs() > 2).sum())}

# Grados con los tres medios
R["grados"] = []
for d in range(1, 8):
    p = make_pipeline(PolynomialFeatures(d, include_bias=False), StandardScaler(), LinearRegression()).fit(tr[C], tr.ventas)
    k = p[0].n_output_features_
    pred = p.predict(te[C])
    R["grados"].append(dict(grado=d, columnas=int(k), **med(p, tr[C], te[C]), mediana_te=float(np.median(np.abs(te.ventas - pred))),
                            max_err_te=float(np.max(np.abs(te.ventas - pred))), suma_abs_beta=float(np.abs(p[-1].coef_).sum()),
                            cv_mae=float(-cross_val_score(p, tr[C], tr.ventas, cv=kf, scoring="neg_mean_absolute_error").mean())))

# Frenos sobre el grado 5
G = 5
R["frenos"] = {"grado": G, "ridge": [], "lasso": []}
nombres = PolynomialFeatures(G, include_bias=False).fit(tr[C]).get_feature_names_out(C).tolist()
for a in [0.001, 0.01, 0.1, 1, 10, 100, 1000]:
    p = make_pipeline(PolynomialFeatures(G, include_bias=False), StandardScaler(), Ridge(alpha=a)).fit(tr[C], tr.ventas)
    R["frenos"]["ridge"].append(dict(alpha=a, **med(p, tr[C], te[C]), suma_abs_beta=float(np.abs(p[-1].coef_).sum()), vivas=int((np.abs(p[-1].coef_) > 1e-9).sum())))
for a in [0.0001, 0.001, 0.01, 0.1, 0.5, 1]:
    p = make_pipeline(PolynomialFeatures(G, include_bias=False), StandardScaler(), Lasso(alpha=a, max_iter=300000)).fit(tr[C], tr.ventas)
    viv = [n for n, c in zip(nombres, p[-1].coef_) if c != 0]
    R["frenos"]["lasso"].append(dict(alpha=a, **med(p, tr[C], te[C]), suma_abs_beta=float(np.abs(p[-1].coef_).sum()), vivas=len(viv), cuales=viv if len(viv) <= 12 else []))
al_r = np.logspace(-3, 3, 61)
al_l = np.logspace(-4, 0, 41)
rc = make_pipeline(PolynomialFeatures(G, include_bias=False), StandardScaler(), RidgeCV(alphas=al_r, cv=kf)).fit(tr[C], tr.ventas)
lc = make_pipeline(PolynomialFeatures(G, include_bias=False), StandardScaler(), LassoCV(alphas=al_l, cv=kf, max_iter=300000)).fit(tr[C], tr.ventas)
R["cv"] = dict(ridge=dict(alpha=float(rc[-1].alpha_), **med(rc, tr[C], te[C])),
               lasso=dict(alpha=float(lc[-1].alpha_), **med(lc, tr[C], te[C]), vivas=int((lc[-1].coef_ != 0).sum())))
# La rejilla del ejercicio: se elige con validación cruzada dentro de los 150 mercados, medida en error absoluto
REJILLA = [0.0001, 0.0003, 0.001, 0.003, 0.01, 0.03, 0.1, 0.3, 1.0]
R["rejilla"] = {"ridge": [], "lasso": []}
for nom, cls, escala in (("ridge", Ridge, 100), ("lasso", Lasso, 1)):
    for a in REJILLA:
        kw = dict(alpha=a * escala)
        if nom == "lasso":
            kw["max_iter"] = 300000
        p = make_pipeline(PolynomialFeatures(G, include_bias=False), StandardScaler(), cls(**kw))
        cvm = float(-cross_val_score(p, tr[C], tr.ventas, cv=kf, scoring="neg_mean_absolute_error").mean())
        p.fit(tr[C], tr.ventas)
        R["rejilla"][nom].append(dict(alpha=a * escala, cv_mae=cvm, mae_te=mae(te.ventas, p.predict(te[C])), r2_te=r2(te.ventas, p.predict(te[C])), vivas=int((np.abs(p[-1].coef_) > 1e-9).sum()), suma_abs_beta=float(np.abs(p[-1].coef_).sum())))
    R["rejilla"][nom + "_mejor"] = min(R["rejilla"][nom], key=lambda r: r["cv_mae"])
# Mejor mezcla de 99 mil con la curva, sin salir del rango observado
mix = pd.DataFrame({"tv": np.arange(0, 99.01, 1.0)})
mix["radio"] = 99 - mix.tv
mix = mix[mix.radio <= df.radio.max()]
mix["ventas"] = cu.predict(mix)
mej = mix.loc[mix.ventas.idxmax()]
R["mejor_mezcla"] = dict(tv=float(mej.tv), radio=float(mej.radio), ventas=float(mej.ventas), utilidad=float(mej.ventas * MARGEN - 99))
cerca = df[(df.tv.sub(mej.tv).abs() <= 25) & (df.radio.sub(mej.radio).abs() <= 10)]
R["mejor_mezcla"]["mercados_cerca"] = len(cerca)
R["rangos"] = dict(tv_max=float(df.tv.max()), radio_max=float(df.radio.max()))

# Contraste CO2: variables casi copiadas
f = pd.read_csv(AQUI / "d2l" / "consumo-combustible-co2.csv")
FC = ["ENGINESIZE", "CYLINDERS", "FUELCONSUMPTION_CITY", "FUELCONSUMPTION_HWY", "FUELCONSUMPTION_COMB", "FUELCONSUMPTION_COMB_MPG"]
a_, b_ = train_test_split(f, test_size=0.25, random_state=42)
R["co2"] = {"n": len(f), "corr_ciudad_comb": float(f.FUELCONSUMPTION_CITY.corr(f.FUELCONSUMPTION_COMB)), "modelos": {}}
for d in (1, 3, 4):
    for n, mod in (("ols", LinearRegression()), ("ridge", RidgeCV(alphas=np.logspace(-3, 3, 61), cv=kf)), ("lasso", LassoCV(alphas=np.logspace(-3, 1, 41), cv=kf, max_iter=300000))):
        p = make_pipeline(PolynomialFeatures(d, include_bias=False), StandardScaler(), mod).fit(a_[FC], a_.CO2EMISSIONS)
        R["co2"]["modelos"][f"{n}_{d}"] = dict(mae_te=mae(b_.CO2EMISSIONS, p.predict(b_[FC])), r2_te=r2(b_.CO2EMISSIONS, p.predict(b_[FC])),
                                                mae_tr=mae(a_.CO2EMISSIONS, p.predict(a_[FC])), alpha=float(getattr(p[-1], "alpha_", 0)),
                                                vivas=int((np.abs(p[-1].coef_) > 1e-9).sum()), columnas=int(p[0].n_output_features_))

# CO2: tres columnas casi copiadas. Los coeficientes de cada mitad de los datos
Xf = f[FC]
fil = []
for seed in range(6):
    mitad = f.sample(frac=0.5, random_state=seed)
    for n, mod in (("ols", LinearRegression()), ("ridge", Ridge(alpha=50)), ("lasso", Lasso(alpha=1, max_iter=300000))):
        p = make_pipeline(StandardScaler(), mod).fit(mitad[FC], mitad.CO2EMISSIONS)
        fil.append(dict(seed=seed, modelo=n, **dict(zip(FC, p[-1].coef_.tolist()))))
fr = pd.DataFrame(fil)
R["co2"]["mitades"] = {n: {c_: [float(g[c_].min()), float(g[c_].max())] for c_ in FC} for n, g in fr.groupby("modelo")}
R["co2"]["mitades_ceros"] = {n: {c_: int((g[c_].abs() < 1e-9).sum()) for c_ in FC} for n, g in fr.groupby("modelo")}

(AQUI / "cifras.json").write_text(json.dumps(R, indent=1, ensure_ascii=False))
print(json.dumps({k: R[k] for k in ("rejilla",)}, ensure_ascii=False))
print(json.dumps(R["co2"]["mitades"], ensure_ascii=False))
print(R["co2"]["mitades_ceros"])

# Complementos para el deck y la guía (se reescribe cifras.json)
b_ = cu.params
R["radio_equilibrio_tv"] = float(((1000 / MARGEN) / 1000 - b_["radio"]) / b_["tv:radio"])
R["tv_techo_parabola_radio0"] = float(-b_["tv"] / (2 * b_["I(tv ** 2)"]))
R["tv_techo_parabola_radio25"] = float(-(b_["tv"] + b_["tv:radio"] * 25) / (2 * b_["I(tv ** 2)"]))
p6 = make_pipeline(PolynomialFeatures(6, include_bias=False), StandardScaler(), LinearRegression()).fit(tr[C], tr.ventas)
e6 = np.abs(te.ventas.values - p6.predict(te[C]))
i6 = int(e6.argmax())
R["grado6"] = dict(n_menor_1=int((e6 < 1).sum()), n_menor_2=int((e6 < 2).sum()), peor_error=float(e6[i6]), peor_pred=float(p6.predict(te[C])[i6]), peor_real=float(te.ventas.values[i6]),
                   peor_tv=float(te.tv.values[i6]), peor_radio=float(te.radio.values[i6]), peor_prensa=float(te.prensa.values[i6]), peor_mercado=int(te.mercado.values[i6]))
for a in (0.3,):
    p = make_pipeline(PolynomialFeatures(G, include_bias=False), StandardScaler(), Lasso(alpha=a, max_iter=300000)).fit(tr[C], tr.ventas)
    R["lasso_03_vivas"] = [n for n, c in zip(nombres, p[-1].coef_) if c != 0]
p = make_pipeline(PolynomialFeatures(G, include_bias=False), StandardScaler(), Lasso(alpha=R["rejilla"]["lasso_mejor"]["alpha"], max_iter=300000)).fit(tr[C], tr.ventas)
R["lasso_mejor_vivas"] = [n for n, c in zip(nombres, p[-1].coef_) if c != 0]
(AQUI / "cifras.json").write_text(json.dumps(R, indent=1, ensure_ascii=False))
print({k: R[k] for k in ("radio_equilibrio_tv", "tv_techo_parabola_radio0", "tv_techo_parabola_radio25", "grado6", "lasso_03_vivas", "lasso_mejor_vivas")})
