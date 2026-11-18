#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Resuelve el proyecto RFM+P sobre superstore_2026.csv y escribe el informe docente.

Todas las cifras del informe salen de este script. Si cambia el dataset, se
vuelve a correr y el HTML se regenera con los valores nuevos.

Uso:  python3 generar_informe.py
Salida: informe_docente_rfmp.html (en esta misma carpeta)
"""
from pathlib import Path
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

AQUI = Path(__file__).resolve().parent
DATOS = AQUI.parents[1] / "sitio" / "datos" / "superstore_2026.csv"
SALIDA = AQUI / "informe_docente_rfmp.html"

# ---------------------------------------------------------------- datos
d = pd.read_csv(DATOS, parse_dates=["fecha_pedido", "fecha_envio"])
cols_sin_id = [c for c in d.columns if c != "linea_id"]
n_dup = int(d.duplicated(cols_sin_id).sum())
dup = d[d.duplicated(cols_sin_id, keep=False)].iloc[0]
FMIN, FMAX = d.fecha_pedido.min(), d.fecha_pedido.max()
REF = FMAX + pd.Timedelta(days=1)
HOY = pd.Timestamp("2026-10-05")

c = d.groupby("cliente_id").agg(
    seg=("segmento", "first"), ult=("fecha_pedido", "max"), pri=("fecha_pedido", "min"),
    F=("pedido_id", "nunique"), lineas=("linea_id", "count"),
    M=("venta", "sum"), P=("utilidad", "sum"))
c["R"] = (REF - c.ult).dt.days
c["ant"] = (REF - c.pri).dt.days
c["desc_pond"] = (d.assign(dv=d.descuento * d.venta).groupby("cliente_id").dv.sum() / c.M)
N = len(c)


def score(x, col, asc=True):
    r = x[col].rank(method="first", ascending=asc)
    return pd.qcut(r, 5, labels=[1, 2, 3, 4, 5]).astype(int)


def puntuar(x):
    x = x.copy()
    x["r"] = score(x, "R", False)
    x["f"] = score(x, "F")
    x["m"] = score(x, "M")
    x["p"] = score(x, "P")
    return x


MAPA = [  # (regex sobre "rf", nombre)
    (r"[1-2][1-2]", "Hibernando"), (r"[1-2][3-4]", "En riesgo"),
    (r"[1-2]5", "No se pueden perder"), (r"3[1-2]", "Por dormirse"),
    (r"33", "Necesitan atención"), (r"[3-4][4-5]", "Leales"),
    (r"41", "Prometedores"), (r"51", "Nuevos"),
    (r"[4-5][2-3]", "Potenciales leales"), (r"5[4-5]", "Campeones")]
ORDEN = ["Campeones", "Leales", "Potenciales leales", "Nuevos", "Prometedores",
         "Necesitan atención", "Por dormirse", "En riesgo", "No se pueden perder",
         "Hibernando"]


def etiquetar(x):
    k = x.r.astype(str) + x.f.astype(str)
    return k.replace({a: b for a, b in MAPA}, regex=True)


g = puntuar(c)
g["lab"] = etiquetar(g)
w = pd.concat([puntuar(x) for _, x in c.groupby("seg")]).loc[g.index]
w["lab"] = etiquetar(w)

# ---------------------------------------------------------------- cifras
def pct(a, b=1):
    return 100 * a / b


tab = g.groupby("lab").agg(n=("R", "size"), R=("R", "median"), F=("F", "median"),
                           M=("M", "median"), P=("P", "median"), Msum=("M", "sum"),
                           Psum=("P", "sum"), neg=("P", lambda s: (s < 0).mean() * 100),
                           ant=("ant", "median")).reindex(ORDEN)
tab["pc"] = pct(tab.n, N)
tab["pm"] = pct(tab.Msum, tab.Msum.sum())
tab["pp"] = pct(tab.Psum, tab.Psum.sum())
tab["mg"] = pct(tab.Psum, tab.Msum)

P_TOTAL = c.P.sum()
P_NEG = c.P[c.P < 0].sum()
P_POS = c.P[c.P > 0].sum()
n_neg = int((c.P < 0).sum())
s_m = c.sort_values("M", ascending=False)
s_p = c.sort_values("P", ascending=False)
top20 = int(0.2 * N)
top20_M = pct(s_m.M.head(top20).sum(), c.M.sum())
top20_P = pct(s_p.P.head(top20).sum(), P_TOTAL)
cum = s_p.P.cumsum() / P_TOTAL
pico = cum.max() * 100
n_pico = int(cum.values.argmax()) + 1

peor = d.groupby("cliente_id").utilidad.min()
neg_ids = c.index[c.P < 0]
salvados = int(((c.P - peor)[neg_ids] > 0).sum())

rho = c[["R", "F", "M", "P"]].corr(method="spearman")
seller = c.loc[s_m.index[0]]
seller_name = d.loc[d.cliente_id == s_m.index[0], "cliente"].iloc[0]
seller_line = d[d.cliente_id == s_m.index[0]].nlargest(1, "venta").iloc[0]
peor_linea = d.nsmallest(1, "utilidad").iloc[0]

F_bins = pd.qcut(c.F, 5).value_counts().sort_index().tolist()
F_cut = pd.qcut(c.F, 5, retbins=True)[1]
empates = g.groupby("F").f.nunique()
empates = [int(v) for v in empates[empates > 1].index]
lin_vs_ped = c.lineas.mean() / c.F.mean()
infl = (d.venta * d.cantidad).sum() / d.venta.sum()
R_hoy = (HOY - c.ult).dt.days
Re = (REF - d.groupby("cliente_id").fecha_envio.max()).dt.days
n_Re = int((Re <= 0).sum())
n_envio_post = int((d.fecha_envio > FMAX).sum())

cambia = (g.lab != w.lab)
cambia_seg = cambia.groupby(g.seg).mean() * 100
m5_glob = (pd.crosstab(g.seg, g.m, normalize="index") * 100)[5]
m5_dent = (pd.crosstab(w.seg, w.m, normalize="index") * 100)[5]
segcom = g.groupby("seg").agg(n=("P", "size"), M=("M", "sum"), P=("P", "sum"),
                              Rm=("R", "median"), Fm=("F", "median"), Mm=("M", "median"),
                              Pm=("P", "median"), neg=("P", lambda s: (s < 0).mean() * 100))
segcom["pc"] = pct(segcom.n, N)
segcom["pp"] = pct(segcom.P, P_TOTAL)
segcom["mg"] = pct(segcom.P, segcom.M)
n_seg_min = int(segcom.n.min())

fy = d.fecha_pedido.apply(lambda x: x.year if x.month >= 9 else x.year - 1)
anual = d.groupby(fy).agg(v=("venta", "sum"), u=("utilidad", "sum"), cl=("cliente_id", "nunique"),
                          ped=("pedido_id", "nunique"))
cal = d.groupby(d.fecha_pedido.dt.year).agg(v=("venta", "sum"), ped=("pedido_id", "nunique"))
adq = ((c.pri - FMIN).dt.days // 365).clip(upper=3).value_counts().sort_index()
nuevos_12m = int((c.pri > FMAX - pd.Timedelta(days=365)).sum())
reg1 = int((d.groupby("cliente_id").region.nunique() == 1).sum())
ciud_med = d.groupby("cliente_id").ciudad.nunique().median()
cp4 = int((d.codigo_postal.astype(str).str.len() == 4).sum())
mismo_dia = int(d.groupby(["cliente_id", "pedido_id"]).fecha_pedido.first().reset_index()
                .duplicated(["cliente_id", "fecha_pedido"]).sum())

dbins = pd.cut(c.desc_pond, [-.01, .05, .10, .20, .30, 1],
               labels=["0 a 5 %", "5 a 10 %", "10 a 20 %", "20 a 30 %", "más de 30 %"])
desc_tab = c.groupby(dbins, observed=True).agg(n=("P", "size"),
                                               neg=("P", lambda s: (s < 0).mean() * 100),
                                               Psum=("P", "sum"), Pmed=("P", "median"))
lin_desc = d.groupby(pd.cut(d.descuento, [-.01, 0, .2, 1], labels=["sin", "hasta20", "mas20"]),
                     observed=True).agg(n=("utilidad", "size"), u=("utilidad", "sum"),
                                        neg=("utilidad", lambda s: (s < 0).mean() * 100))
subc = d.groupby("subcategoria").utilidad.sum().sort_values()
est = d.groupby("estado").agg(u=("utilidad", "sum"), de=("descuento", "mean")).sort_values("u")

mp = pd.crosstab(g.m, g.p).reindex(index=[1, 2, 3, 4, 5], columns=[1, 2, 3, 4, 5], fill_value=0)
m5_neg = int(((g.m == 5) & (g.P < 0)).sum())
camp_neg = int(((g.lab == "Campeones") & (g.P < 0)).sum())
n555 = int(((g.r == 5) & (g.f == 5) & (g.m == 5)).sum())
neg555 = int(((g.r == 5) & (g.f == 5) & (g.m == 5) & (g.P < 0)).sum())
p1_neg = pct(((g.p == 1) & (g.P < 0)).sum(), (g.p == 1).sum())
hib_neg = tab.loc["Hibernando", "neg"]

# KMeans de contraste
X = g[["R", "F", "M", "P"]].copy()
X["R"] = np.log1p(X.R)
X["M"] = np.log1p(X.M)
X["P"] = np.sign(X.P) * np.log1p(X.P.abs())
Z = StandardScaler().fit_transform(X)
sil = {k: silhouette_score(Z, KMeans(k, n_init=10, random_state=0).fit(Z).labels_)
       for k in range(2, 8)}
km = KMeans(4, n_init=10, random_state=0).fit(Z)
g["k"] = km.labels_
ktab = g.groupby("k").agg(n=("P", "size"), R=("R", "median"), F=("F", "median"),
                          M=("M", "median"), P=("P", "median"),
                          neg=("P", lambda s: (s < 0).mean() * 100))
k_loss = ktab.neg.idxmax()

# ---------------------------------------------------------------- formato
def n0(x):
    return f"{x:,.0f}"


def n1(x):
    return f"{x:,.1f}"


def usd(x):
    s = f"{abs(x):,.0f}"
    return ("−$" if x < 0 else "$") + s


def p1(x):
    return f"{x:.1f} %"


def fecha(t):
    meses = ["ene", "feb", "mar", "abr", "may", "jun", "jul", "ago", "sep", "oct", "nov", "dic"]
    return f"{t.day}-{meses[t.month - 1]}-{t.year}"


INK, MUTE, LINE, ACC, SOFT = "#1e1e1e", "#6b6b6b", "#e6e2df", "#A6192E", "#b9b4b0"

# ---------------------------------------------------------------- gráficos SVG
def svg_segmentos():
    rows = tab.reset_index()
    W, top, rh, lx, bx = 760, 46, 34, 190, 560
    H = top + rh * len(rows) + 20
    mx = max(rows.pc.max(), rows.pp.max(), rows.pm.max())
    sc = (bx - lx - 10) / mx
    o = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Participación de cada segmento RFM en clientes y en utilidad">']
    o.append(f'<rect x="{lx}" y="10" width="12" height="10" fill="{SOFT}"/>'
             f'<text x="{lx+18}" y="19" font-size="12" fill="{MUTE}">% de clientes</text>'
             f'<rect x="{lx+120}" y="10" width="12" height="10" fill="{ACC}"/>'
             f'<text x="{lx+138}" y="19" font-size="12" fill="{MUTE}">% de la utilidad total</text>'
             f'<text x="{bx+20}" y="19" font-size="12" fill="{MUTE}">margen</text>'
             f'<text x="{bx+110}" y="19" font-size="12" fill="{MUTE}">clientes con P &lt; 0</text>')
    for i, r in rows.iterrows():
        y = top + i * rh
        o.append(f'<text x="{lx-10}" y="{y+16}" font-size="13" text-anchor="end" fill="{INK}">{r.lab}</text>')
        o.append(f'<rect x="{lx}" y="{y+2}" width="{r.pc*sc:.1f}" height="11" fill="{SOFT}"/>')
        o.append(f'<rect x="{lx}" y="{y+15}" width="{max(r.pp,0)*sc:.1f}" height="11" fill="{ACC}"/>')
        o.append(f'<text x="{lx+r.pc*sc+5:.1f}" y="{y+12}" font-size="11" fill="{MUTE}">{r.pc:.1f}</text>')
        o.append(f'<text x="{lx+r.pp*sc+5:.1f}" y="{y+25}" font-size="11" fill="{ACC}">{r.pp:.1f}</text>')
        o.append(f'<text x="{bx+20}" y="{y+19}" font-size="12.5" fill="{INK}">{r.mg:.1f} %</text>')
        col = ACC if r.neg >= 20 else INK
        o.append(f'<text x="{bx+110}" y="{y+19}" font-size="12.5" fill="{col}">{r.neg:.1f} %</text>')
    o.append(f'<line x1="{lx}" y1="{top-4}" x2="{lx}" y2="{H-14}" stroke="{LINE}"/>')
    o.append("</svg>")
    return "".join(o)


def svg_pareto():
    W, H, L, B, T, Rr = 760, 300, 56, 40, 20, 20
    xs = np.arange(1, N + 1) / N * 100
    ys = cum.values * 100
    ymin, ymax = -0, 130
    fx = lambda v: L + (W - L - Rr) * v / 100
    fy = lambda v: T + (H - T - B) * (1 - (v - ymin) / (ymax - ymin))
    pts = " ".join(f"{fx(a):.1f},{fy(b):.1f}" for a, b in zip(xs, ys))
    o = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Utilidad acumulada por cliente ordenado de mayor a menor utilidad">']
    for v in [0, 25, 50, 75, 100, 125]:
        o.append(f'<line x1="{L}" x2="{W-Rr}" y1="{fy(v):.1f}" y2="{fy(v):.1f}" stroke="{LINE}"/>'
                 f'<text x="{L-8}" y="{fy(v)+4:.1f}" font-size="11" text-anchor="end" fill="{MUTE}">{v} %</text>')
    for v in [0, 20, 40, 60, 80, 100]:
        o.append(f'<text x="{fx(v):.1f}" y="{H-B+18}" font-size="11" text-anchor="middle" fill="{MUTE}">{v} %</text>')
    o.append(f'<text x="{(L+W-Rr)/2}" y="{H-4}" font-size="11.5" text-anchor="middle" fill="{MUTE}">clientes ordenados de mayor a menor utilidad</text>')
    o.append(f'<line x1="{L}" x2="{W-Rr}" y1="{fy(100):.1f}" y2="{fy(100):.1f}" stroke="{INK}" stroke-dasharray="4 4"/>')
    o.append(f'<polyline points="{pts}" fill="none" stroke="{ACC}" stroke-width="2.4"/>')
    px, py = fx(n_pico / N * 100), fy(pico)
    o.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="4.5" fill="{ACC}"/>')
    o.append(f'<text x="{px+10:.1f}" y="{py-8:.1f}" font-size="12.5" fill="{INK}">{pct(n_pico, N):.1f} % de los clientes ya generan el {pico:.0f} % de la utilidad</text>')
    x20 = fx(20)
    o.append(f'<line x1="{x20:.1f}" x2="{x20:.1f}" y1="{fy(0):.1f}" y2="{fy(top20_P):.1f}" stroke="{MUTE}" stroke-dasharray="2 3"/>')
    o.append(f'<text x="{x20-6:.1f}" y="{fy(top20_P)+16:.1f}" font-size="12" text-anchor="end" fill="{MUTE}">top 20 %: {top20_P:.0f} %</text>')
    o.append(f'<text x="{fx(99):.1f}" y="{fy(100)-8:.1f}" font-size="12" text-anchor="end" fill="{INK}">el último {pct(n_neg, N):.1f} % resta {pct(-P_NEG, P_TOTAL):.0f} puntos</text>')
    o.append("</svg>")
    return "".join(o)


def svg_heat():
    cell, L, T = 62, 90, 40
    W, H = L + cell * 5 + 30, T + cell * 5 + 50
    mx = mp.values.max()
    o = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Clientes por puntaje de monto y puntaje de utilidad">']
    o.append(f'<text x="{L+cell*2.5}" y="22" font-size="12" text-anchor="middle" fill="{MUTE}">puntaje P (utilidad)</text>')
    for j in range(5):
        o.append(f'<text x="{L+cell*j+cell/2}" y="{T-6}" font-size="12" text-anchor="middle" fill="{INK}">{j+1}</text>')
    for i, m in enumerate([5, 4, 3, 2, 1]):
        o.append(f'<text x="{L-10}" y="{T+cell*i+cell/2+4}" font-size="12" text-anchor="end" fill="{INK}">M {m}</text>')
        for j, p in enumerate([1, 2, 3, 4, 5]):
            v = int(mp.loc[m, p])
            a = 0.08 + 0.85 * v / mx
            o.append(f'<rect x="{L+cell*j}" y="{T+cell*i}" width="{cell-3}" height="{cell-3}" fill="{ACC}" fill-opacity="{a:.2f}"/>')
            tc = "#ffffff" if a > 0.5 else INK
            o.append(f'<text x="{L+cell*j+cell/2-1.5}" y="{T+cell*i+cell/2+4}" font-size="14" text-anchor="middle" fill="{tc}">{v}</text>')
    o.append(f'<rect x="{L-1}" y="{T-1}" width="{cell-1}" height="{cell-1}" fill="none" stroke="{INK}" stroke-width="2"/>')
    o.append(f'<text x="{L}" y="{H-14}" font-size="12" fill="{MUTE}">Recuadro: venden en el quintil más alto y dejan la utilidad más baja.</text>')
    o.append("</svg>")
    return "".join(o)


def svg_desc():
    rows = desc_tab.reset_index()
    W, H, L, B, T = 760, 250, 60, 46, 26
    bw = (W - L - 20) / len(rows)
    fy = lambda v: T + (H - T - B) * (1 - v / 100)
    o = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Porcentaje de clientes con utilidad negativa según su descuento promedio ponderado">']
    for v in [0, 25, 50, 75, 100]:
        o.append(f'<line x1="{L}" x2="{W-20}" y1="{fy(v):.1f}" y2="{fy(v):.1f}" stroke="{LINE}"/>'
                 f'<text x="{L-8}" y="{fy(v)+4:.1f}" font-size="11" text-anchor="end" fill="{MUTE}">{v} %</text>')
    for i, r in rows.iterrows():
        x = L + i * bw + bw * 0.2
        col = ACC if r.neg >= 50 else SOFT
        o.append(f'<rect x="{x:.1f}" y="{fy(r.neg):.1f}" width="{bw*0.6:.1f}" height="{fy(0)-fy(r.neg):.1f}" fill="{col}"/>')
        o.append(f'<text x="{x+bw*0.3:.1f}" y="{fy(r.neg)-6:.1f}" font-size="13" text-anchor="middle" fill="{INK}">{r.neg:.0f} %</text>')
        o.append(f'<text x="{x+bw*0.3:.1f}" y="{H-B+18}" font-size="12" text-anchor="middle" fill="{INK}">{r.desc_pond}</text>')
        o.append(f'<text x="{x+bw*0.3:.1f}" y="{H-B+34}" font-size="11" text-anchor="middle" fill="{MUTE}">{pct(r.n, N):.1f} % de clientes</text>')
    o.append("</svg>")
    return "".join(o)


def svg_global_vs_dentro():
    segs = list(m5_glob.index)
    W, H, L, B, T = 760, 230, 60, 40, 30
    gw = (W - L - 20) / len(segs)
    fy = lambda v: T + (H - T - B) * (1 - v / 25)
    o = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="Porcentaje de clientes en el quintil más alto de monto, calificando global y dentro de cada segmento">']
    o.append(f'<rect x="{L}" y="6" width="12" height="10" fill="{ACC}"/><text x="{L+18}" y="15" font-size="12" fill="{MUTE}">quintiles calculados sobre toda la base</text>'
             f'<rect x="{L+270}" y="6" width="12" height="10" fill="{SOFT}"/><text x="{L+288}" y="15" font-size="12" fill="{MUTE}">quintiles calculados dentro de cada segmento</text>')
    for v in [0, 5, 10, 15, 20, 25]:
        o.append(f'<line x1="{L}" x2="{W-20}" y1="{fy(v):.1f}" y2="{fy(v):.1f}" stroke="{LINE}"/>'
                 f'<text x="{L-8}" y="{fy(v)+4:.1f}" font-size="11" text-anchor="end" fill="{MUTE}">{v} %</text>')
    for i, s in enumerate(segs):
        x0 = L + i * gw + gw * 0.18
        bw = gw * 0.3
        for k, (val, col) in enumerate([(m5_glob[s], ACC), (m5_dent[s], SOFT)]):
            x = x0 + k * (bw + 6)
            o.append(f'<rect x="{x:.1f}" y="{fy(val):.1f}" width="{bw:.1f}" height="{fy(0)-fy(val):.1f}" fill="{col}"/>'
                     f'<text x="{x+bw/2:.1f}" y="{fy(val)-6:.1f}" font-size="12" text-anchor="middle" fill="{INK}">{val:.1f}</text>')
        o.append(f'<text x="{x0+bw+3:.1f}" y="{H-B+20}" font-size="12.5" text-anchor="middle" fill="{INK}">{s}</text>')
    o.append("</svg>")
    return "".join(o)


# ---------------------------------------------------------------- tablas HTML
def tabla_segmentos():
    h = ['<table><thead><tr><th>Segmento RFM</th><th>Regla (R F)</th><th>Clientes</th><th>% clientes</th>'
         '<th>R mediana (días)</th><th>F mediana</th><th>M mediana</th><th>P mediana</th>'
         '<th>% ventas</th><th>% utilidad</th><th>Margen</th><th>% con P &lt; 0</th></tr></thead><tbody>']
    reglas = {b: a for a, b in MAPA}
    for s, r in tab.iterrows():
        h.append(f"<tr><td>{s}</td><td class='mono'>{reglas[s]}</td><td>{int(r.n)}</td><td>{r.pc:.1f}</td>"
                 f"<td>{r.R:.0f}</td><td>{r.F:.0f}</td><td>{usd(r.M)}</td><td>{usd(r.P)}</td>"
                 f"<td>{r.pm:.1f}</td><td>{r.pp:.1f}</td><td>{r.mg:.1f}</td><td>{r.neg:.1f}</td></tr>")
    h.append("</tbody></table>")
    return "".join(h)


def tabla_segcom():
    h = ['<table><thead><tr><th>Segmento comercial</th><th>% clientes</th><th>R mediana</th><th>F mediana</th>'
         '<th>M mediana</th><th>P mediana</th><th>% utilidad total</th><th>Margen agregado</th>'
         '<th>% con P &lt; 0</th><th>Cambian de etiqueta al calificar dentro</th></tr></thead><tbody>']
    for s, r in segcom.iterrows():
        h.append(f"<tr><td>{s}</td><td>{r.pc:.1f}</td><td>{r.Rm:.0f}</td><td>{r.Fm:.0f}</td><td>{usd(r.Mm)}</td>"
                 f"<td>{usd(r.Pm)}</td><td>{r.pp:.1f}</td><td>{r.mg:.1f} %</td><td>{r.neg:.1f}</td>"
                 f"<td>{cambia_seg[s]:.1f} %</td></tr>")
    h.append("</tbody></table>")
    return "".join(h)


def tabla_kmeans():
    h = ['<table><thead><tr><th>Grupo KMeans</th><th>% clientes</th><th>R mediana</th><th>F mediana</th>'
         '<th>M mediana</th><th>P mediana</th><th>% con P &lt; 0</th></tr></thead><tbody>']
    for k, r in ktab.sort_values("P", ascending=False).iterrows():
        h.append(f"<tr><td>Grupo {k+1}</td><td>{pct(r.n, N):.1f}</td><td>{r.R:.0f}</td><td>{r.F:.0f}</td>"
                 f"<td>{usd(r.M)}</td><td>{usd(r.P)}</td><td>{r.neg:.0f}</td></tr>")
    h.append("</tbody></table>")
    return "".join(h)


qR = pd.qcut(c.R, 5, retbins=True)[1]
qM = pd.qcut(c.M, 5, retbins=True)[1]
qP = pd.qcut(c.P, 5, retbins=True)[1]
T = tab  # alias corto

# ---------------------------------------------------------------- HTML
html = f"""<meta charset="utf-8">
<title>RFM+P Superstore 2026</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,500;8..60,600&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>
/* Informe docente de una columna, ancho de lectura, tablas y gráficos a ancho completo. Fondo blanco siempre. */
:root {{
  --bg: #ffffff; --ink: #1e1e1e; --mute: #6b6b6b; --line: #e6e2df; --acc: #A6192E;
  --wash: #f7f4f3; --amber: #b7791f; --green: #3e7b4f;
  --f-display: "Source Serif 4", Georgia, "Times New Roman", serif;
  --f-body: "IBM Plex Sans", "Helvetica Neue", Arial, sans-serif;
  --f-mono: "IBM Plex Mono", ui-monospace, Menlo, Consolas, monospace;
  color-scheme: light;
}}
html, body {{ background: var(--bg); color: var(--ink); }}
body {{ font-family: var(--f-body); font-size: 16px; line-height: 1.6; }}
.wrap {{ max-width: 980px; margin: 0 auto; padding-inline: 20px; padding-block: 40px 80px; }}
.prose {{ max-width: 68ch; }}
header.top {{ border-bottom: 2px solid var(--ink); padding-bottom: 22px; margin-bottom: 8px; }}
.eyebrow {{ font-family: var(--f-mono); font-size: 12px; letter-spacing: .08em; text-transform: uppercase; color: var(--acc); }}
h1 {{ font-family: var(--f-display); font-weight: 600; font-size: clamp(30px, 5vw, 44px); line-height: 1.1; margin: 8px 0 12px; text-wrap: balance; }}
h2 {{ font-family: var(--f-display); font-weight: 600; font-size: 27px; line-height: 1.2; margin: 56px 0 10px; text-wrap: balance; }}
h3 {{ font-family: var(--f-body); font-weight: 600; font-size: 17px; margin: 28px 0 6px; }}
p {{ margin: 0 0 14px; }}
.lede {{ font-size: 18px; color: var(--ink); }}
.meta {{ display: flex; flex-wrap: wrap; gap: 8px 28px; font-family: var(--f-mono); font-size: 13px; color: var(--mute); margin-top: 14px; }}
.meta b {{ color: var(--ink); font-weight: 500; }}
nav.toc {{ display: flex; flex-wrap: wrap; gap: 6px 18px; font-size: 14px; padding: 14px 0; border-bottom: 1px solid var(--line); }}
nav.toc a {{ color: var(--ink); text-decoration: none; border-bottom: 1px solid var(--line); }}
nav.toc a:hover, nav.toc a:focus-visible {{ border-color: var(--acc); color: var(--acc); outline: none; }}
.kpis {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 0 18px; border-top: 1px solid var(--line); border-bottom: 1px solid var(--line); margin: 24px 0; }}
.kpi {{ padding: 16px 16px 14px 0; min-width: 0; }}
.kpi .v {{ font-family: var(--f-display); font-size: 34px; font-weight: 600; color: var(--acc); line-height: 1; font-variant-numeric: tabular-nums; }}
.kpi .l {{ font-size: 13.5px; color: var(--ink); margin-top: 6px; line-height: 1.4; }}
figure {{ margin: 22px 0 28px; }}
figure svg {{ width: 100%; height: auto; display: block; font-family: var(--f-body); }}
figure.narrow svg {{ max-width: 460px; }}
figcaption {{ font-size: 13.5px; color: var(--mute); margin-top: 8px; max-width: 75ch; }}
.fig-title {{ font-weight: 600; font-size: 15px; margin-bottom: 6px; }}
.scroll {{ overflow-x: auto; margin: 16px 0 24px; }}
table {{ border-collapse: collapse; font-size: 13.5px; font-variant-numeric: tabular-nums; min-width: 640px; width: 100%; }}
th {{ text-align: left; font-weight: 600; font-size: 12px; color: var(--mute); border-bottom: 1.5px solid var(--ink); padding: 8px 10px 6px 0; vertical-align: bottom; }}
td {{ border-bottom: 1px solid var(--line); padding: 7px 10px 7px 0; vertical-align: top; }}
td:first-child {{ font-weight: 500; }}
.mono, code {{ font-family: var(--f-mono); font-size: .9em; }}
code {{ background: var(--wash); padding: 1px 5px; border-radius: 3px; }}
pre {{ background: var(--wash); padding: 16px 18px; overflow-x: auto; font-family: var(--f-mono); font-size: 13px; line-height: 1.55; border-left: 3px solid var(--ink); }}
.trap {{ display: grid; grid-template-columns: 112px minmax(0, 1fr); gap: 4px 20px; padding: 18px 0; border-top: 1px solid var(--line); }}
.trap:last-of-type {{ border-bottom: 1px solid var(--line); }}
.trap h3 {{ margin: 0 0 4px; }}
.trap p {{ margin: 0 0 8px; }}
.sev {{ font-family: var(--f-mono); font-size: 11.5px; letter-spacing: .05em; text-transform: uppercase; display: inline-flex; align-items: center; gap: 7px; padding-top: 3px; }}
.sev::before {{ content: ""; width: 10px; height: 10px; border-radius: 50%; background: currentColor; }}
.sev.r {{ color: var(--acc); }} .sev.a {{ color: var(--amber); }} .sev.v {{ color: var(--green); }}
.num {{ font-family: var(--f-mono); font-size: 12px; color: var(--mute); display: block; margin-top: 4px; }}
.legend {{ display: flex; flex-wrap: wrap; gap: 8px 22px; font-size: 13.5px; margin: 10px 0 4px; }}
.cp {{ display: grid; grid-template-columns: 64px minmax(0, 1fr); gap: 0 20px; padding: 20px 0; border-top: 1px solid var(--line); }}
.cp .n {{ font-family: var(--f-display); font-size: 34px; font-weight: 600; color: var(--acc); line-height: 1; }}
.cp h3 {{ margin: 0 0 6px; }}
.cp dl {{ display: grid; grid-template-columns: 150px minmax(0, 1fr); gap: 6px 16px; margin: 10px 0 0; font-size: 14.5px; }}
.cp dt {{ color: var(--mute); font-size: 12.5px; font-family: var(--f-mono); text-transform: uppercase; letter-spacing: .04em; padding-top: 2px; }}
.cp dd {{ margin: 0; min-width: 0; }}
.insight {{ padding: 14px 0 14px 18px; border-left: 3px solid var(--acc); margin: 18px 0; }}
.insight p:last-child {{ margin-bottom: 0; }}
.src {{ font-size: 13.5px; color: var(--mute); }}
.src a {{ color: var(--ink); }}
@media (max-width: 640px) {{
  .trap, .cp {{ grid-template-columns: minmax(0, 1fr); }}
  .cp dl {{ grid-template-columns: minmax(0, 1fr); }}
  .cp dt {{ padding-top: 8px; }}
}}
@media (prefers-reduced-motion: reduce) {{ * {{ scroll-behavior: auto !important; }} }}
</style>

<div class="wrap">
<header class="top">
  <div class="eyebrow">ADM 2003 · Análisis de Datos · Proyecto de medio semestre · Guía docente</div>
  <h1>RFM+P sobre Superstore 2026: resolución, trampas y checkpoints</h1>
  <p class="lede prose">Resolución completa del proyecto sobre <code>superstore_2026.csv</code>. Incluye lo que el archivo esconde, los hallazgos que un buen informe debería encontrar y la secuencia de verificación con valores esperados para revisar el trabajo de los grupos.</p>
  <div class="meta">
    <span><b>{n0(len(d))}</b> líneas</span><span><b>{n0(d.pedido_id.nunique())}</b> pedidos</span>
    <span><b>{N}</b> clientes</span><span><b>{fecha(FMIN)}</b> a <b>{fecha(FMAX)}</b></span>
    <span>fecha de referencia <b>{fecha(REF)}</b></span>
  </div>
</header>
<nav class="toc" aria-label="Secciones">
  <a href="#metodo">El método</a><a href="#resolucion">Resolución</a><a href="#capa-p">La capa P</a>
  <a href="#segmentos">Global o por segmento</a><a href="#trampas">Trampas del archivo</a>
  <a href="#insights">Hallazgos que deben aparecer</a><a href="#checkpoints">Checkpoints</a>
  <a href="#acciones">Acciones por segmento</a><a href="#codigo">Código de referencia</a>
</nav>

<div class="kpis">
  <div class="kpi"><div class="v">{top20_P:.0f} %</div><div class="l">de la utilidad viene del 20 % de clientes más rentable. En ventas, ese mismo corte es {top20_M:.0f} %.</div></div>
  <div class="kpi"><div class="v">{pct(n_neg, N):.1f} %</div><div class="l">de los clientes tiene utilidad acumulada negativa y resta {usd(P_NEG)} en cuatro años.</div></div>
  <div class="kpi"><div class="v">{T.loc['En riesgo','pp']+T.loc['No se pueden perder','pp']:.1f} %</div><div class="l">de la utilidad está en clientes que se están enfriando: En riesgo y No se pueden perder.</div></div>
  <div class="kpi"><div class="v">{pct(nuevos_12m, N):.1f} %</div><div class="l">de la base compró por primera vez en los últimos 12 meses. La base casi no se renueva.</div></div>
</div>

<section id="metodo">
<h2>El método</h2>
<div class="prose">
<p>RFM nace en el marketing directo. George Cullinan lo propuso en los años sesenta para separar a los clientes con más probabilidad de volver a comprar, y Arthur Hughes lo popularizó en <em>Strategic Database Marketing</em> (1994) con la versión que se usa hoy: cada dimensión se parte en quintiles y cada cliente recibe un puntaje de 1 a 5 en Recencia, Frecuencia y Monto. Cinco por cinco por cinco da 125 celdas, demasiadas para actuar, así que la práctica habitual las agrupa en una decena de segmentos con nombre a partir de R y F.</p>
<p>La lógica es conductual. Quien compró hace poco tiene más probabilidad de volver a comprar que quien no aparece hace un año; quien compra seguido está más vinculado; quien gasta más pesa más en ventas. Fader, Hardie y Lee mostraron en 2005 que R y F, junto con el monto, son estadísticos suficientes para estimar el valor de vida del cliente en modelos probabilísticos, lo que explica por qué un método tan simple sigue vigente.</p>
<p>La P es la parte que este curso agrega y la que hace interesante el caso. M mide cuánto vendemos, no cuánto ganamos. En una tienda que da descuentos de hasta 80 %, un cliente puede estar en el quintil más alto de ventas y destruir valor. Sumar la utilidad acumulada por cliente convierte una segmentación de actividad en una segmentación de rentabilidad.</p>
<p>Las cuatro métricas por cliente quedan así. <b>R</b>: días entre la última compra y la fecha de referencia ({fecha(REF)}, un día después del último pedido). <b>F</b>: número de pedidos distintos. <b>M</b>: suma de <code>venta</code>. <b>P</b>: suma de <code>utilidad</code>. R se califica al revés, porque menos días es mejor.</p>
</div>
</section>

<section id="resolucion">
<h2>Resolución</h2>
<div class="prose">
<p>La tabla de clientes tiene {N} filas. La recencia mediana es {c.R.median():.0f} días y la media {c.R.mean():.1f}, lo que ya avisa de una cola larga de clientes dormidos. La frecuencia mediana es {c.F.median():.0f} pedidos en cuatro años, con un rango de {c.F.min()} a {c.F.max()}. El monto mediano es {usd(c.M.median())} y la media {usd(c.M.mean())}. La utilidad mediana es {usd(c.P.median())}, la media {usd(c.P.mean())}, y va de {usd(c.P.min())} a {usd(c.P.max())}.</p>
<p>Los cortes de quintil son: R en {qR[1]:.0f}, {qR[2]:.0f}, {qR[3]:.0f} y {qR[4]:.0f} días; M en {usd(qM[1])}, {usd(qM[2])}, {usd(qM[3])} y {usd(qM[4])}; P en {usd(qP[1])}, {usd(qP[2])}, {usd(qP[3])} y {usd(qP[4])}. El primer corte de P cae prácticamente en cero, así que el puntaje P = 1 es casi idéntico a decir que el cliente pierde plata: el {p1_neg:.0f} % de ese quintil tiene utilidad negativa. F no se puede cortar limpio en quintiles por los empates; se resuelve calificando sobre el ranking (ver trampa 5).</p>
<p>Con el mapa de segmentos estándar sobre R y F el resultado es el siguiente. Las reglas se leen como expresión regular sobre el par de puntajes R F; por ejemplo, <code>[4-5][2-3]</code> es R de 4 o 5 con F de 2 o 3.</p>
</div>
<div class="scroll">{tabla_segmentos()}</div>
<figure>
  <div class="fig-title">Lo que pesa cada segmento en clientes y en utilidad</div>
  {svg_segmentos()}
  <figcaption>El porcentaje de clientes con P &lt; 0 va en rojo cuando llega a 20 % o más. Hibernando concentra el {T.loc['Hibernando','pc']:.1f} % de los clientes y solo el {T.loc['Hibernando','pp']:.1f} % de la utilidad. No se pueden perder es el caso inverso: {T.loc['No se pueden perder','pc']:.1f} % de los clientes, {T.loc['No se pueden perder','pp']:.1f} % de la utilidad y uno de los márgenes más altos.</figcaption>
</figure>
<div class="prose">
<p>Tres lecturas sobresalen. Primero, los Leales son el segmento que más vende ({T.loc['Leales','pm']:.1f} % de las ventas) y el de menor margen entre los grandes ({T.loc['Leales','mg']:.1f} %). Su lealtad se paga. Segundo, En riesgo y No se pueden perder suman el {T.loc['En riesgo','pc']+T.loc['No se pueden perder','pc']:.1f} % de los clientes y el {T.loc['En riesgo','pp']+T.loc['No se pueden perder','pp']:.1f} % de la utilidad, con márgenes de {T.loc['En riesgo','mg']:.1f} % y {T.loc['No se pueden perder','mg']:.1f} %. Es la plata que se está yendo y es rentable. Tercero, el segmento Nuevos no contiene clientes nuevos: su antigüedad mediana es {T.loc['Nuevos','ant']:.0f} días (trampa 9).</p>
</div>
</section>

<section id="capa-p">
<h2>La capa P</h2>
<div class="prose">
<p>La correlación de rangos entre M y P es {rho.loc['M','P']:.2f}. Vender más se asocia con ganar más, pero lejos de ser lo mismo. El cruce de puntajes lo hace visible: {int(mp.loc[5,1])} clientes están en el quintil más alto de ventas y en el más bajo de utilidad, y {m5_neg} de los {int((g.m==5).sum())} clientes con M = 5 tienen utilidad negativa.</p>
</div>
<figure class="narrow">
  <div class="fig-title">Clientes por puntaje de monto y de utilidad</div>
  {svg_heat()}
</figure>
<div class="prose">
<p>El caso emblemático es {seller_name}, el cliente que más compra en toda la base: {usd(seller.M)} en {int(seller.F)} pedidos y una utilidad acumulada de {usd(seller.P)}. Casi todo viene de una sola línea, un equipo de la subcategoría {seller_line.subcategoria} vendido en {usd(seller_line.venta)} con {seller_line.descuento*100:.0f} % de descuento, que dejó {usd(seller_line.utilidad)}. Un RFM clásico lo pondría arriba en monto; RFM+P lo muestra como lo que es.</p>
<p>La curva de utilidad acumulada resume la capa P mejor que cualquier tabla. Ordenando a los clientes de más a menos rentable, el {pct(n_pico, N):.1f} % de la base ya genera el {pico:.0f} % de la utilidad total. Todo lo que viene después resta.</p>
</div>
<figure>
  <div class="fig-title">Utilidad acumulada por cliente</div>
  {svg_pareto()}
  <figcaption>La curva pasa de 100 % porque {n_neg} clientes tienen utilidad negativa. Entre todos restan {usd(P_NEG)}, el equivalente al {pct(-P_NEG, P_POS):.1f} % de la utilidad que generan los clientes rentables.</figcaption>
</figure>
<div class="insight prose">
<p><b>La pérdida es de transacciones, no de personas.</b> De los {n_neg} clientes con P negativa, {salvados} ({pct(salvados, n_neg):.0f} %) tendrían utilidad positiva si se quitara su peor línea. La línea más costosa de toda la base deja {usd(peor_linea.utilidad)}: una venta de {peor_linea.subcategoria.lower()} con {peor_linea.descuento*100:.0f} % de descuento en {peor_linea.estado}. La recomendación correcta para estos clientes rara vez es dejar de atenderlos; casi siempre es dejar de venderles con ese descuento.</p>
</div>
<figure>
  <div class="fig-title">Clientes con utilidad negativa según su descuento promedio ponderado</div>
  {svg_desc()}
  <figcaption>Descuento promedio ponderado por venta. Por encima de 20 % la mayoría de los clientes pierde plata. A nivel de línea, el {lin_desc.loc['mas20','neg']:.0f} % de las líneas con descuento mayor a 20 % tiene utilidad negativa y en conjunto restan {usd(lin_desc.loc['mas20','u'])}.</figcaption>
</figure>
<div class="prose">
<p>Las fuentes de la pérdida están concentradas. Por subcategoría, {subc.index[0]} ({usd(subc.iloc[0])}), {subc.index[1]} ({usd(subc.iloc[1])}) e {subc.index[2]} ({usd(subc.iloc[2])}) son las únicas con utilidad total negativa. Por estado, {est.index[0]} ({usd(est.u.iloc[0])}), {est.index[1]} ({usd(est.u.iloc[1])}), {est.index[2]} ({usd(est.u.iloc[2])}) e {est.index[3]} ({usd(est.u.iloc[3])}) encabezan las pérdidas, con descuentos promedio por línea entre {est.de.iloc[:4].min()*100:.0f} % y {est.de.iloc[:4].max()*100:.0f} %. Un grupo que llega hasta aquí ya tiene recomendaciones concretas de política comercial.</p>
</div>
</section>

<section id="segmentos">
<h2>Global o por segmento comercial</h2>
<div class="prose">
<p>La columna <code>segmento</code> tiene tres valores: Consumidor, Corporativo y Oficina en casa. Cada cliente pertenece a uno solo, así que se puede calcular RFM+P de dos maneras. Con quintiles sobre toda la base, un 5 en M significa lo mismo para cualquier cliente. Con quintiles dentro de cada segmento, un 5 significa estar entre el 20 % más alto de su propio grupo.</p>
<p>La diferencia práctica en etiquetas es pequeña: el {pct(cambia.sum(), N):.1f} % de los clientes cambia de segmento RFM al pasar de una a otra. La diferencia conceptual es grande. Si se califica dentro de cada segmento, todos los segmentos quedan por construcción con 20 % de clientes en cada quintil, y cualquier comparación entre Consumidor, Corporativo y Oficina en casa basada en esos puntajes es una tautología. El gráfico lo muestra para el quintil más alto de M.</p>
</div>
<figure>
  <div class="fig-title">% de clientes con M = 5 en cada segmento comercial</div>
  {svg_global_vs_dentro()}
  <figcaption>Calificando global aparecen diferencias reales, aunque modestas. Calificando dentro, desaparecen porque el método las borra.</figcaption>
</figure>
<div class="scroll">{tabla_segcom()}</div>
<div class="prose">
<p>Lo que deben concluir es doble. Para comparar segmentos comerciales se usa la calificación global. Hecha así, los tres segmentos se parecen mucho por cliente: medianas de R, F, M y P muy cercanas. La diferencia está en el tamaño (Consumidor es el {segcom.loc['Consumidor','pc']:.1f} % de los clientes y el {segcom.loc['Consumidor','pp']:.1f} % de la utilidad) y en el margen agregado, que sube de {segcom.loc['Consumidor','mg']:.1f} % en Consumidor a {segcom.loc['Oficina en casa','mg']:.1f} % en Oficina en casa. El segmento comercial no es lo que separa a los clientes valiosos de los demás; lo que los separa es el descuento y la mezcla de productos.</p>
<p>La calificación dentro del segmento sí tiene un uso: ordenar la cartera de un equipo que solo atiende a un segmento, por ejemplo el de cuentas corporativas. Ahí conviene advertir que Oficina en casa tiene {n_seg_min} clientes, quintiles de unos {n_seg_min//5}, y es donde más etiquetas cambian ({cambia_seg['Oficina en casa']:.1f} %). Con grupos pequeños los cortes son menos estables.</p>
</div>
</section>

<section id="trampas">
<h2>Trampas del archivo</h2>
<p class="prose">El semáforo indica el daño. Rojo: cambia las conclusiones. Ámbar: distorsiona cifras o etiquetas. Verde: detalle de calidad que un buen informe documenta.</p>

<div class="trap"><div><span class="sev r">Rojo</span><span class="num">Trampa 1</span></div><div>
<h3>Frecuencia contada por líneas en vez de pedidos</h3>
<p>Cada fila es una línea de producto, no un pedido. Un pedido tiene en promedio {len(d)/d.pedido_id.nunique():.1f} líneas. Contar filas con <code>count</code> en lugar de <code>nunique</code> sobre <code>pedido_id</code> da una frecuencia media de {c.lineas.mean():.1f} en vez de {c.F.mean():.1f}, {lin_vs_ped:.1f} veces más, y premia a quien compra muchos productos distintos en un solo pedido.</p></div></div>

<div class="trap"><div><span class="sev r">Rojo</span><span class="num">Trampa 2</span></div><div>
<h3>Monto calculado como venta por cantidad</h3>
<p><code>venta</code> ya es el total de la línea, después del descuento. Multiplicarla por <code>cantidad</code> infla el monto total {infl:.1f} veces. Es el error más frecuente cuando se asume que la columna es precio unitario.</p></div></div>

<div class="trap"><div><span class="sev r">Rojo</span><span class="num">Trampa 3</span></div><div>
<h3>RFM sin P, o P mirada solo en promedio</h3>
<p>Sin la P, {m5_neg} clientes con utilidad negativa quedan en el quintil más alto de monto y {camp_neg} de los {int(T.loc['Campeones','n'])} Campeones pierden plata. Con la P en promedio por segmento, la media se ve positiva en todos lados y se pierde que {pct(n_neg, N):.1f} % de los clientes resta valor. La P se mira por cliente y como distribución.</p></div></div>

<div class="trap"><div><span class="sev r">Rojo</span><span class="num">Trampa 4</span></div><div>
<h3>Calificar dentro de cada segmento y luego comparar segmentos</h3>
<p>Ver la sección anterior. Calificando dentro, cada segmento tiene 20 % de clientes por quintil por construcción. Afirmar que Corporativo tiene tantos Campeones como Consumidor a partir de esa calificación no dice nada sobre los datos. Las conclusiones entre segmentos van con la calificación global.</p></div></div>

<div class="trap"><div><span class="sev a">Ámbar</span><span class="num">Trampa 5</span></div><div>
<h3>Empates en la frecuencia</h3>
<p>F toma solo {c.F.nunique()} valores distintos. <code>pd.qcut(F, 5)</code> corta en {', '.join(f'{v:g}' for v in F_cut[1:-1])} y deja grupos de {', '.join(str(v) for v in F_bins)} clientes, lejos de quintiles iguales; en otras versiones de pandas o con otros datos lanza error por bordes duplicados. La salida habitual es calificar sobre <code>rank(method="first")</code>, que da grupos de {N//5} o {N//5+1}, con un costo que el informe debe declarar: clientes con la misma F (por ejemplo F = {', '.join(str(v) for v in empates)}) reciben puntajes distintos según su orden en la tabla. La alternativa defendible es fijar umbrales de negocio para F.</p></div></div>

<div class="trap"><div><span class="sev a">Ámbar</span><span class="num">Trampa 6</span></div><div>
<h3>Recencia calificada en la dirección equivocada</h3>
<p>En R, menos días es mejor. Si se usa <code>qcut</code> con etiquetas 1 a 5 sin invertir, los clientes más recientes quedan con 1 y el mapa de segmentos se voltea entero: los Campeones pasan a Hibernando.</p></div></div>

<div class="trap"><div><span class="sev a">Ámbar</span><span class="num">Trampa 7</span></div><div>
<h3>Fecha de referencia: hoy o el último dato</h3>
<p>Calcular R contra la fecha de hoy ({fecha(HOY)}) suma {(HOY-REF).days} días a todos los clientes: la recencia media pasa de {c.R.mean():.0f} a {R_hoy.mean():.0f}. Los quintiles no cambian porque dependen del orden, pero cualquier regla absoluta, como inactivo después de 90 días, sí. La convención es el día siguiente al último pedido y debe declararse.</p></div></div>

<div class="trap"><div><span class="sev a">Ámbar</span><span class="num">Trampa 8</span></div><div>
<h3>Recencia con la fecha de envío</h3>
<p>{n_envio_post} líneas se envían después del último pedido registrado (envíos en tránsito). Si R se calcula con <code>fecha_envio</code>, {n_Re} clientes quedan con recencia cero o negativa. La recencia es de compra, se usa <code>fecha_pedido</code>.</p></div></div>

<div class="trap"><div><span class="sev a">Ámbar</span><span class="num">Trampa 9</span></div><div>
<h3>El segmento Nuevos no tiene clientes nuevos</h3>
<p>El mapa estándar llama Nuevos a R = 5 con F = 1. Aquí esos {int(T.loc['Nuevos','n'])} clientes tienen una antigüedad mediana de {T.loc['Nuevos','ant']:.0f} días: son clientes antiguos que compran poco y compraron hace poco. Solo {nuevos_12m} clientes de toda la base hicieron su primera compra en los últimos 12 meses, y el {pct(adq.iloc[0], N):.0f} % llegó en el primer año del registro. Los nombres del mapa se validan contra los datos antes de usarlos.</p></div></div>

<div class="trap"><div><span class="sev a">Ámbar</span><span class="num">Trampa 10</span></div><div>
<h3>La columna segmento y los segmentos RFM</h3>
<p>La palabra segmento significa dos cosas en este trabajo: la columna comercial con tres valores y los grupos que resultan del RFM. Un informe que no las nombra distinto confunde al lector. Sugerencia: segmento comercial para la columna y perfil RFM, o el nombre de cada grupo, para el resultado.</p></div></div>

<div class="trap"><div><span class="sev a">Ámbar</span><span class="num">Trampa 11</span></div><div>
<h3>Años calendario incompletos</h3>
<p>Los datos van del {fecha(FMIN)} al {fecha(FMAX)}. Agrupando por año calendario, 2022 tiene {int(cal.loc[2022,'ped'])} pedidos y 2026 solo ocho meses, lo que fabrica un salto de crecimiento en 2023 y una caída en 2026. Con ventanas de 12 meses de septiembre a agosto las ventas pasan de {usd(anual.v.iloc[0])} a {usd(anual.v.iloc[-1])} ({pct(anual.v.iloc[-1]/anual.v.iloc[0]-1):.0f} % más) y los clientes activos de {int(anual.cl.iloc[0])} a {int(anual.cl.iloc[-1])}.</p></div></div>

<div class="trap"><div><span class="sev a">Ámbar</span><span class="num">Trampa 12</span></div><div>
<h3>Región y estado no son atributos del cliente</h3>
<p><code>region</code>, <code>estado</code> y <code>ciudad</code> describen el destino de cada pedido. Solo {reg1} clientes ({pct(reg1, N):.1f} %) compran en una sola región y la mediana es de {ciud_med:.0f} ciudades por cliente. Tomar la primera región para asignar cada cliente a un mapa produce una geografía inventada. El análisis geográfico se hace a nivel de línea o de pedido.</p></div></div>

<div class="trap"><div><span class="sev v">Verde</span><span class="num">Trampa 13</span></div><div>
<h3>Una fila duplicada</h3>
<p>Hay {n_dup} fila idéntica en todo menos <code>linea_id</code> (pedido {dup.pedido_id}, cliente {dup.cliente}). Puede ser un error de carga o el mismo producto pedido dos veces. El efecto es mínimo; lo que se evalúa es que la detecten, decidan y lo dejen escrito.</p></div></div>

<div class="trap"><div><span class="sev v">Verde</span><span class="num">Trampa 14</span></div><div>
<h3>Pedidos del mismo día y códigos postales sin cero inicial</h3>
<p>{mismo_dia} veces un cliente hizo dos pedidos distintos el mismo día. Contar días de compra en vez de pedidos cambia F levemente; cualquiera de las dos es defendible si se declara. Además, {cp4} líneas tienen código postal de cuatro dígitos porque se leyó como número y perdió el cero inicial (estados del noreste). No afecta al RFM, pero sí a cualquier cruce geográfico.</p></div></div>

<div class="trap"><div><span class="sev v">Verde</span><span class="num">Trampa 15</span></div><div>
<h3>KMeans sin transformar las variables</h3>
<p>M y P tienen colas largas y P tiene negativos. Escalando sin transformar, KMeans arma un grupo con los pocos clientes extremos. Con logaritmo en R y M, logaritmo con signo en P y estandarización, la silueta es baja para cualquier k (entre {min(sil.values()):.2f} y {max(sil.values()):.2f}): no hay grupos naturales marcados y el número de segmentos es una decisión de negocio. Con k = 4, el algoritmo aísla un grupo de {int(ktab.loc[k_loss,'n'])} clientes donde el {ktab.loc[k_loss,'neg']:.0f} % pierde plata, algo que el mapa por reglas sobre R y F no separa.</p></div></div>
<div class="scroll">{tabla_kmeans()}</div>
</section>

<section id="insights">
<h2>Hallazgos que deben aparecer en el informe</h2>
<div class="prose">
<p>Un informe sobresaliente encuentra la mayoría de estos ocho puntos y los conecta con una acción. Están en el orden en que suelen aparecer al trabajar el caso.</p>
<h3>1. La utilidad está mucho más concentrada que las ventas</h3>
<p>El 20 % de clientes más rentable aporta el {top20_P:.0f} % de la utilidad; el 20 % que más compra aporta el {top20_M:.0f} % de las ventas. Retener a pocos clientes vale más de lo que sugiere el monto.</p>
<h3>2. Uno de cada cinco clientes destruye valor</h3>
<p>{n_neg} clientes ({pct(n_neg, N):.1f} %) restan {usd(P_NEG)}, el {pct(-P_NEG, P_POS):.1f} % de lo que ganan los demás.</p>
<h3>3. La causa es el descuento, y está en pocas transacciones</h3>
<p>Con descuento ponderado sobre 30 %, el {desc_tab.neg.iloc[-1]:.0f} % de los clientes pierde. El {pct(salvados, n_neg):.0f} % de los clientes con pérdida sería rentable sin su peor línea. Mesas, Libreros e Insumos son las subcategorías con pérdida, y Texas, Ohio, Pennsylvania e Illinois los estados.</p>
<h3>4. El cliente que más vende pierde plata</h3>
<p>{seller_name}: primero en ventas, {usd(seller.P)} de utilidad. Es el ejemplo que justifica la P.</p>
<h3>5. La plata en riesgo es rentable</h3>
<p>En riesgo y No se pueden perder concentran el {T.loc['En riesgo','pp']+T.loc['No se pueden perder','pp']:.1f} % de la utilidad con márgenes sobre el promedio ({pct(P_TOTAL, c.M.sum()):.1f} %). Es la prioridad de retención.</p>
<h3>6. Los Leales venden mucho y ganan poco</h3>
<p>{T.loc['Leales','pm']:.1f} % de las ventas, margen de {T.loc['Leales','mg']:.1f} % y {T.loc['Leales','neg']:.1f} % de clientes con pérdida. Hay margen por recuperar sin perder volumen.</p>
<h3>7. Reactivar con descuento a los Hibernando agrava el problema</h3>
<p>El {hib_neg:.1f} % de los Hibernando ya tiene utilidad negativa, la proporción más alta de todos los segmentos. Una campaña de reactivación con cupón, la recomendación de manual, se aplica solo a los que tienen P positiva.</p>
<h3>8. La base no se renueva y el segmento comercial no discrimina</h3>
<p>Solo el {pct(nuevos_12m, N):.1f} % de los clientes es nuevo en el último año, así que el crecimiento viene de vender más a los mismos. Y Consumidor, Corporativo y Oficina en casa tienen perfiles RFM+P casi iguales por cliente: segmentar por esa columna no reemplaza al RFM.</p>
</div>
</section>

<section id="checkpoints">
<h2>Checkpoints</h2>
<p class="prose">Secuencia para el informe de cada grupo. Cada checkpoint tiene un valor de control que permite verificar en minutos si van bien, el error típico que lo rompe y la pregunta que el informe debe contestar en ese punto. Los valores salen del procedimiento de este documento; diferencias pequeñas en los conteos por segmento son aceptables si el grupo declaró otro manejo de empates.</p>

<div class="cp"><div class="n">1</div><div>
<h3>Pregunta de negocio y unidad de análisis</h3>
<p>Antes de tocar código, el informe dice qué decisión va a apoyar (a quién retener, a quién reactivar, dónde cortar descuentos) y que la unidad de análisis es el cliente.</p>
<dl><dt>Control</dt><dd>{n0(len(d))} líneas, {n0(d.pedido_id.nunique())} pedidos, {N} clientes. Cada pedido pertenece a un solo cliente y tiene una sola fecha.</dd>
<dt>Error típico</dt><dd>Creer que cada fila es un pedido.</dd>
<dt>Pregunta</dt><dd>¿Qué representa una fila y cuántas filas tiene un pedido en promedio?</dd></dl></div></div>

<div class="cp"><div class="n">2</div><div>
<h3>Bitácora de calidad</h3>
<p>Tipos de datos, nulos, duplicados, rango de fechas y valores imposibles, con la decisión tomada en cada caso.</p>
<dl><dt>Control</dt><dd>Sin nulos. {n_dup} fila duplicada. Ventas y cantidades positivas. Fechas del {fecha(FMIN)} al {fecha(FMAX)}. {n_envio_post} envíos posteriores al último pedido. {cp4} códigos postales de cuatro dígitos.</dd>
<dt>Error típico</dt><dd>No convertir las fechas a datetime y calcular días sobre texto.</dd>
<dt>Pregunta</dt><dd>¿Qué hicieron con la fila duplicada y por qué?</dd></dl></div></div>

<div class="cp"><div class="n">3</div><div>
<h3>Fecha de referencia</h3>
<dl><dt>Control</dt><dd>{fecha(REF)}, un día después del último pedido.</dd>
<dt>Error típico</dt><dd>Usar la fecha de hoy o la fecha de envío.</dd>
<dt>Pregunta</dt><dd>¿Qué pasaría con una regla de 90 días si usaran la fecha de hoy?</dd></dl></div></div>

<div class="cp"><div class="n">4</div><div>
<h3>Tabla RFM+P por cliente</h3>
<dl><dt>Control</dt><dd>{N} filas. Medianas: R {c.R.median():.0f} días, F {c.F.median():.0f}, M {usd(c.M.median())}, P {usd(c.P.median())}. Medias: R {c.R.mean():.1f}, F {c.F.mean():.2f}, M {usd(c.M.mean())}, P {usd(c.P.mean())}. Suma de M = {usd(c.M.sum())}, suma de P = {usd(P_TOTAL)}.</dd>
<dt>Error típico</dt><dd>F media de {c.lineas.mean():.1f} (contaron líneas) o suma de M cercana a {usd((d.venta*d.cantidad).sum())} (multiplicaron por cantidad).</dd>
<dt>Pregunta</dt><dd>¿Por qué la media de M es mayor que la mediana y qué implica para el corte por quintiles?</dd></dl></div></div>

<div class="cp"><div class="n">5</div><div>
<h3>Exploración antes de calificar</h3>
<p>Histogramas de las cuatro métricas y correlaciones. Deben notar la cola larga de R, los pocos valores de F y los negativos de P.</p>
<dl><dt>Control</dt><dd>{n_neg} clientes con P &lt; 0 ({pct(n_neg, N):.1f} %). Correlación de rangos M y P = {rho.loc['M','P']:.2f}; R y F = {rho.loc['R','F']:.2f}.</dd>
<dt>Error típico</dt><dd>Saltar directo al scoring sin mirar la distribución de P.</dd>
<dt>Pregunta</dt><dd>¿Es lo mismo un cliente grande que un cliente rentable? Muestren un ejemplo.</dd></dl></div></div>

<div class="cp"><div class="n">6</div><div>
<h3>Puntajes por quintil</h3>
<dl><dt>Control</dt><dd>Cada puntaje de 1 a 5 con {N//5} o {N//5+1} clientes. R invertida: el 5 corresponde a {qR[1]:.0f} días o menos. P = 1 corresponde a utilidad de {usd(qP[1])} o menos.</dd>
<dt>Error típico</dt><dd>R sin invertir; <code>qcut</code> sobre F con grupos desiguales o error de bordes duplicados.</dd>
<dt>Pregunta</dt><dd>¿Cómo resolvieron los empates en F y qué costo tiene esa decisión?</dd></dl></div></div>

<div class="cp"><div class="n">7</div><div>
<h3>Segmentos con nombre</h3>
<p>Mapa explícito de reglas, tabla con tamaño, medianas y participación en ventas y utilidad de cada segmento.</p>
<dl><dt>Control</dt><dd>Con el mapa estándar: Campeones {int(T.loc['Campeones','n'])} ({T.loc['Campeones','pc']:.1f} %), Leales {int(T.loc['Leales','n'])}, En riesgo {int(T.loc['En riesgo','n'])}, Hibernando {int(T.loc['Hibernando','n'])} ({T.loc['Hibernando','pc']:.1f} %).</dd>
<dt>Error típico</dt><dd>Copiar los nombres del mapa sin revisar si describen a los clientes (Nuevos).</dd>
<dt>Pregunta</dt><dd>¿Los clientes del segmento Nuevos son nuevos? ¿Cómo lo comprobaron?</dd></dl></div></div>

<div class="cp"><div class="n">8</div><div>
<h3>La capa P</h3>
<p>Cruce de M con P, porcentaje de clientes con pérdida por segmento y curva de utilidad acumulada.</p>
<dl><dt>Control</dt><dd>{m5_neg} clientes con M = 5 y P &lt; 0. {camp_neg} Campeones con pérdida. Top 20 % por utilidad = {top20_P:.0f} % de la utilidad. Pico de la curva en {pico:.0f} %.</dd>
<dt>Error típico</dt><dd>Reportar solo la P media por segmento.</dd>
<dt>Pregunta</dt><dd>¿Qué segmento tiene la mayor proporción de clientes que pierden plata y qué significa eso para una campaña con descuento?</dd></dl></div></div>

<div class="cp"><div class="n">9</div><div>
<h3>Global frente a por segmento comercial</h3>
<p>Calcular las dos versiones y explicar cuál sirve para qué.</p>
<dl><dt>Control</dt><dd>{pct(cambia.sum(), N):.1f} % de clientes cambia de etiqueta; {cambia_seg['Oficina en casa']:.1f} % en Oficina en casa. Calificando dentro, cada segmento comercial tiene 20 % por quintil. Margen agregado: {segcom.loc['Consumidor','mg']:.1f} %, {segcom.loc['Corporativo','mg']:.1f} % y {segcom.loc['Oficina en casa','mg']:.1f} %.</dd>
<dt>Error típico</dt><dd>Concluir que los segmentos comerciales son iguales usando la calificación interna.</dd>
<dt>Pregunta</dt><dd>¿Por qué no se pueden comparar segmentos comerciales con puntajes calculados dentro de cada uno?</dd></dl></div></div>

<div class="cp"><div class="n">10</div><div>
<h3>Diagnóstico de la pérdida</h3>
<p>Bajar de cliente a línea: descuento, subcategoría y estado de las transacciones que explican la P negativa.</p>
<dl><dt>Control</dt><dd>{pct(salvados, n_neg):.0f} % de los clientes con pérdida sería rentable sin su peor línea. {lin_desc.loc['mas20','neg']:.0f} % de las líneas con descuento sobre 20 % pierde. Subcategorías con pérdida: {', '.join(subc.index[:3])}.</dd>
<dt>Error típico</dt><dd>Recomendar dejar de atender a los clientes con pérdida.</dd>
<dt>Pregunta</dt><dd>¿El problema es el cliente o la transacción? Justifiquen con datos.</dd></dl></div></div>

<div class="cp"><div class="n">11</div><div>
<h3>Contraste con KMeans</h3>
<p>Opcional para aprobar, según la condición mínima del proyecto. Variables transformadas y escaladas, codo y silueta, comparación con los segmentos por reglas.</p>
<dl><dt>Control</dt><dd>Silueta entre {min(sil.values()):.2f} y {max(sil.values()):.2f} para k de 2 a 7. Con k = 4 aparece un grupo de {int(ktab.loc[k_loss,'n'])} clientes casi todos con pérdida.</dd>
<dt>Error típico</dt><dd>Escalar sin transformar y presentar un grupo de pocos clientes extremos como hallazgo.</dd>
<dt>Pregunta</dt><dd>¿Qué encontró el algoritmo que las reglas no separaban? ¿Por qué eligieron ese k?</dd></dl></div></div>

<div class="cp"><div class="n">12</div><div>
<h3>Recomendación por segmento y limitaciones</h3>
<p>Una acción y un mensaje comercial de una frase por segmento, con la métrica que mediría su éxito. Cierra con las limitaciones del análisis y el prompt final usado con el asistente.</p>
<dl><dt>Control</dt><dd>Cada acción usa la P: a quién no se le ofrece descuento, a quién se retiene primero, qué subcategorías se revisan.</dd>
<dt>Error típico</dt><dd>Recomendaciones de manual que servirían para cualquier tienda.</dd>
<dt>Pregunta</dt><dd>Si solo pudieran financiar una acción, ¿cuál sería y cuánta utilidad protege?</dd></dl></div></div>
</section>

<section id="acciones">
<h2>Acciones por segmento</h2>
<p class="prose">Referencia para evaluar las recomendaciones. La columna de P es la que distingue un informe RFM+P de uno RFM.</p>
<div class="scroll"><table><thead><tr><th>Segmento</th><th>Acción</th><th>Lo que cambia la P</th><th>Métrica de éxito</th></tr></thead><tbody>
<tr><td>Campeones</td><td>Reconocimiento, acceso anticipado, atención preferente. Sin descuentos generalizados.</td><td>Revisar los {camp_neg} Campeones con pérdida antes de cualquier beneficio.</td><td>Retención a 12 meses y margen.</td></tr>
<tr><td>Leales</td><td>Venta cruzada hacia subcategorías de mayor margen.</td><td>Margen de {T.loc['Leales','mg']:.1f} %: subir margen sin perder frecuencia.</td><td>Margen del segmento.</td></tr>
<tr><td>Potenciales leales</td><td>Programa de frecuencia con beneficios no monetarios.</td><td>{T.loc['Potenciales leales','neg']:.1f} % con pérdida: no usar descuento como gancho.</td><td>F a 6 meses.</td></tr>
<tr><td>Nuevos y Prometedores</td><td>Segunda compra guiada.</td><td>Son pocos y antiguos: reformular como clientes ocasionales recientes.</td><td>Pedidos en 90 días.</td></tr>
<tr><td>Necesitan atención y Por dormirse</td><td>Contacto personalizado con recomendación de producto.</td><td>Por dormirse tiene el margen más bajo ({T.loc['Por dormirse','mg']:.1f} %).</td><td>Recencia.</td></tr>
<tr><td>En riesgo</td><td>Retención activa, prioridad comercial.</td><td>{T.loc['En riesgo','pp']:.1f} % de la utilidad con margen de {T.loc['En riesgo','mg']:.1f} %.</td><td>Clientes recuperados y utilidad protegida.</td></tr>
<tr><td>No se pueden perder</td><td>Contacto directo de un ejecutivo.</td><td>Margen de {T.loc['No se pueden perder','mg']:.1f} %, el mejor de los segmentos grandes.</td><td>Utilidad protegida.</td></tr>
<tr><td>Hibernando</td><td>Reactivación de bajo costo solo para quienes tienen P positiva.</td><td>{hib_neg:.1f} % ya pierde: excluirlos de cupones.</td><td>Costo por cliente reactivado.</td></tr>
<tr><td>Transversal</td><td>Tope de descuento y revisión de Mesas, Libreros e Insumos en los cuatro estados con más pérdida.</td><td>Ataca el origen de los {usd(P_NEG)}.</td><td>Utilidad de líneas con descuento.</td></tr>
</tbody></table></div>
</section>

<section id="codigo">
<h2>Código de referencia</h2>
<pre>import pandas as pd

d = pd.read_csv("superstore_2026.csv", parse_dates=["fecha_pedido", "fecha_envio"])
ref = d["fecha_pedido"].max() + pd.Timedelta(days=1)

rfmp = d.groupby("cliente_id").agg(
    segmento=("segmento", "first"),
    R=("fecha_pedido", lambda s: (ref - s.max()).days),
    F=("pedido_id", "nunique"),          # pedidos, no líneas
    M=("venta", "sum"),                  # venta ya es total de la línea
    P=("utilidad", "sum"),
)

def quintil(s, ascendente=True):
    rango = s.rank(method="first", ascending=ascendente)
    return pd.qcut(rango, 5, labels=[1, 2, 3, 4, 5]).astype(int)

rfmp["r"] = quintil(rfmp["R"], ascendente=False)   # menos días = mejor
for col in ["F", "M", "P"]:
    rfmp[col.lower()] = quintil(rfmp[col])

mapa = {{r"[1-2][1-2]": "Hibernando", r"[1-2][3-4]": "En riesgo",
        r"[1-2]5": "No se pueden perder", r"3[1-2]": "Por dormirse",
        r"33": "Necesitan atención", r"[3-4][4-5]": "Leales",
        r"41": "Prometedores", r"51": "Nuevos",
        r"[4-5][2-3]": "Potenciales leales", r"5[4-5]": "Campeones"}}
rfmp["perfil"] = (rfmp["r"].astype(str) + rfmp["f"].astype(str)).replace(mapa, regex=True)

# versión por segmento comercial (solo para ordenar carteras internas)
por_seg = rfmp.groupby("segmento", group_keys=False).apply(
    lambda x: x.assign(r=quintil(x["R"], False), f=quintil(x["F"]),
                       m=quintil(x["M"]), p=quintil(x["P"])))</pre>
</section>

<section>
<h2>Fuentes</h2>
<p class="src prose">Hughes, A. M. (1994). <em>Strategic Database Marketing</em>. Probus. · Fader, P. S., Hardie, B. G. S. y Lee, K. L. (2005). RFM and CLV: Using iso-value curves for customer base analysis. <em>Journal of Marketing Research</em>, 42(4), 415–430. <a href="https://faculty.wharton.upenn.edu/wp-content/uploads/2013/08/RFM_CLV-JMR-2005.pdf">PDF</a> · Wei, J.-T., Lin, S.-Y. y Wu, H.-H. (2010). A review of the application of RFM model. <em>African Journal of Business Management</em>, 4(19). <a href="https://www.researchgate.net/publication/228399859_A_review_of_the_application_of_RFM_model">Enlace</a> · Heldt, R., Silveira, C. S. y Luce, F. B. (2021). Predicting customer value per product: From RFM to RFM/P. <em>Journal of Business Research</em>, 127. <a href="https://www.sciencedirect.com/science/article/abs/pii/S0148296319303030">Enlace</a>. Todas las cifras del informe se calculan con <code>generar_informe.py</code> sobre <code>sitio/datos/superstore_2026.csv</code>.</p>
</section>
</div>
"""

SALIDA.write_text(html, encoding="utf-8")
print("escrito", SALIDA)
