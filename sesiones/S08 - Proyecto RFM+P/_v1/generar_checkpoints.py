#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Enunciado para estudiantes y clave docente del proyecto RFM+P.

Las dos páginas salen de la misma lista de preguntas de control, así que
siempre quedan alineadas. Las respuestas se calculan aquí sobre el dataset.

Uso:  python3 generar_checkpoints.py
Salida: proyecto_rfmp_estudiantes.html (sin respuestas)
        checkpoints_rfmp.html          (clave docente)
"""
import html as H
import runpy
from pathlib import Path

import pandas as pd

AQUI = Path(__file__).resolve().parent
ns = runpy.run_path(str(AQUI / "generar_informe.py"))
d, c, g, w, T, N = ns["d"], ns["c"], ns["g"], ns["w"], ns["tab"], ns["N"]
usd, fecha, pct, score, MAPA = ns["usd"], ns["fecha"], ns["pct"], ns["score"], ns["MAPA"]
REF, FMIN, FMAX, HOY = ns["REF"], ns["FMIN"], ns["FMAX"], ns["HOY"]


def usd2(x):
    return ("−$" if x < 0 else "$") + f"{abs(x):,.2f}"


# ---------------------------------------------------------------- cortes anuales
cortes = [REF - pd.DateOffset(years=k) for k in (3, 2, 1, 0)]


def foto(ref):
    h = d[d.fecha_pedido < ref]
    v = h[h.fecha_pedido >= ref - pd.Timedelta(days=365)]
    x = h.groupby("cliente_id").agg(R=("fecha_pedido", lambda s: (ref - s.max()).days))
    a = v.groupby("cliente_id").agg(F=("pedido_id", "nunique"), M=("venta", "sum"),
                                    P=("utilidad", "sum"))
    x = x.join(a).fillna(0)
    x["r"], x["f"] = score(x, "R", False), score(x, "F")
    x["lab"] = (x.r.astype(str) + x.f.astype(str)).replace({a: b for a, b in MAPA}, regex=True)
    return x


f25, f26 = foto(cortes[-2]), foto(cortes[-1])
j = f25[["lab"]].join(f26[["lab"]], rsuffix="2", how="inner")
mismo = pct((j.lab == j.lab2).sum(), len(j))

# ---------------------------------------------------------------- clientes testigo
TESTIGOS = [
    ("AB-10105", "Adrian Barton", "Compra muchos productos por pedido."),
    ("SM-20320", "Sean Miller", "El que más compra en toda la base."),
    ("LB-16795", "Laurel Beltran", "Tiene la fila duplicada."),
    ("BP-11185", "Ben Peterman", "Su último pedido todavía estaba en tránsito."),
    ("AD-10180", d.loc[d.cliente_id == "AD-10180", "cliente"].iloc[0], "Cambia de segmento según cómo se califique."),
    ("AH-10690", "Anna Häberlin", "Muy valiosa y lleva más de un año sin comprar."),
]
tv = {k: g.loc[k] for k, _, _ in TESTIGOS}
lin = d.groupby("cliente_id").agg(lineas=("linea_id", "count"))
vc = (d.venta * d.cantidad).groupby(d.cliente_id).sum()
Renv = (REF - d.groupby("cliente_id").fecha_envio.max()).dt.days
Rhoy = (HOY - c.ult).dt.days
dup = ns["dup"]
lb_M_sin = tv["LB-16795"].M - dup.venta
lb_P_sin = tv["LB-16795"].P - dup.utilidad
peor_lb = d[d.cliente_id == "LB-16795"].nsmallest(1, "utilidad").iloc[0]
max_ped = d.groupby("pedido_id").size()
ped_max_id, ped_max_n = max_ped.idxmax(), int(max_ped.max())
rank_M_sm = int(c.M.rank(ascending=False)["SM-20320"])
ofc_m5_g = int(((g.seg == "Oficina en casa") & (g.m == 5)).sum())
ofc_m5_w = int(((w.seg == "Oficina en casa") & (w.m == 5)).sum())
riesgo_P = g[g.lab.isin(["En riesgo", "No se pueden perder"])].P.sum()
ab = tv["AB-10105"]

# ---------------------------------------------------------------- entregas
# Cada pregunta: (texto para estudiantes, respuesta, respuestas equivocadas y su causa, avanzada)
ENTREGAS = [
 dict(nombre="Conocer la base",
  para="Antes de medir clientes hay que saber qué es cada fila. Casi todos los errores de este proyecto nacen aquí.",
  pasos=["Escriban en un párrafo la pregunta de negocio que van a responder.",
         "Describan la base: cuántas filas, pedidos y clientes, qué periodo cubre y qué representa una fila.",
         "Revisen la calidad: tipos de datos, nulos, duplicados, fechas raras. Anoten cada problema y qué decidieron hacer con él."],
  entregable="El cuaderno con la ficha de la base, la bitácora de limpieza y las respuestas de control de esta entrega.",
  preguntas=[
   ("¿Cuántas líneas, pedidos y clientes tiene la base?",
    f"{len(d):,} líneas · {d.pedido_id.nunique():,} pedidos · {N} clientes",
    f"{len(d):,} pedidos: tomaron cada fila como un pedido.", False),
   (f"¿Cuántas líneas tiene el pedido {ped_max_id}?", f"{ped_max_n}", "", False),
   ("¿En cuántos pedidos distintos compró Adrian Barton (AB-10105) y cuántas líneas tiene?",
    f"{int(ab.F)} pedidos · {int(lin.loc['AB-10105','lineas'])} líneas",
    f"{int(lin.loc['AB-10105','lineas'])} pedidos: contaron filas.", False),
   ("¿Cuántas filas duplicadas encontraron? ¿En qué pedido?",
    f"{ns['n_dup']} fila, pedido {dup.pedido_id}",
    "Cero: compararon incluyendo linea_id, que nunca se repite.", False),
   ("¿Cuántas líneas tienen fecha de envío posterior al último pedido registrado?",
    f"{ns['n_envio_post']}", "", False),
  ]),
 dict(nombre="La tabla RFM+P",
  para="Aquí la base pasa de líneas a clientes. Si esta tabla está bien, el resto del proyecto se apoya en terreno firme.",
  pasos=["Elijan la fecha de referencia y expliquen por qué.",
         "Construyan una tabla con una fila por cliente y cuatro columnas: R, F, M y P. Escriban cómo calcularon cada una.",
         "Miren las distribuciones de las cuatro métricas antes de seguir. Una gráfica por métrica y dos líneas de lectura."],
  entregable="La tabla de clientes, las gráficas de distribución y las respuestas de control.",
  preguntas=[
   ("¿Qué fecha de referencia usaron?", f"{fecha(REF)}, un día después del último pedido",
    f"Fecha de hoy: todas las R suben {(HOY-REF).days} días. Aceptable solo si lo justifican.", False),
   ("¿Cuánto les dio R, F, M y P de Adrian Barton (AB-10105)?",
    f"R {int(ab.R)} · F {int(ab.F)} · M {usd2(ab.M)} · P {usd2(ab.P)}",
    f"F {int(lin.loc['AB-10105','lineas'])}: contaron líneas. M {usd2(vc['AB-10105'])}: multiplicaron venta por cantidad. R {int(Rhoy['AB-10105'])}: usaron la fecha de hoy.", False),
   ("¿Cuánto les dio la R de Ben Peterman (BP-11185)?", f"{int(tv['BP-11185'].R)} días",
    f"{int(Renv['BP-11185'])}: usaron fecha_envio en vez de fecha_pedido.", False),
   ("¿Cuánto les dio M y P de Laurel Beltran (LB-16795)?",
    f"Con el duplicado: M {usd2(tv['LB-16795'].M)} · P {usd2(tv['LB-16795'].P)}. Sin él: M {usd2(lb_M_sin)} · P {usd2(lb_P_sin)}",
    "Las dos son correctas si la decisión está en la bitácora.", False),
   ("¿Cuál es la mediana de R y cuánto suma P en toda la base?",
    f"Mediana de R {c.R.median():.0f} días · suma de P {usd(c.P.sum())}", "", False),
   ("¿Cuántos clientes tienen utilidad total negativa?", f"{int((c.P<0).sum())} ({pct((c.P<0).sum(), N):.1f} %)", "", False),
  ]),
 dict(nombre="Segmentos y utilidad",
  para="Los números se convierten en grupos con nombre. La P es la que muestra que vender no es lo mismo que ganar.",
  pasos=["Califiquen cada métrica de 1 a 5 por quintiles. Recuerden que en R menos días es mejor. Expliquen cómo resolvieron los empates.",
         "Agrupen las combinaciones en segmentos con nombre y publiquen las reglas. Comprueben que cada nombre describe de verdad a sus clientes.",
         "Crucen los segmentos con la utilidad: cuánto aporta cada uno, cuántos clientes pierden plata y dónde están.",
         "Repitan la calificación dentro de cada segmento comercial (Consumidor, Corporativo, Oficina en casa) y expliquen cuándo sirve cada versión."],
  entregable="Tabla de segmentos con tamaño, % de ventas, % de utilidad y margen, el mapa de reglas y las respuestas de control.",
  preguntas=[
   ("¿Qué puntajes r, f, m y p tiene Adrian Barton?", f"{ab.r} · {ab.f} · {ab.m} · {ab.p}",
    f"r = {6-ab.r}: no invirtieron la recencia.", False),
   ("Sean Miller tiene F = 5. ¿Qué puntaje f le tocó y por qué?",
    "2 o 3, según el orden de desempate. Lo que se evalúa es que expliquen el empate.",
    "Error de bordes duplicados sin explicación.", False),
   ("¿En qué segmento quedan Ben Peterman, Anna Häberlin y Laurel Beltran?",
    f"{tv['BP-11185'].lab} · {tv['AH-10690'].lab} · {tv['LB-16795'].lab}",
    "Campeones en Anna Häberlin: no invirtieron la recencia.", False),
   ("¿Cuántos Campeones tienen y qué porcentaje de la utilidad aportan?",
    f"{int(T.loc['Campeones','n'])} clientes (±5) · {T.loc['Campeones','pp']:.1f} % de la utilidad (±1.5)", "", False),
   ("¿En qué puesto de ventas está Sean Miller y cuánto les dio su P?",
    f"Puesto {rank_M_sm} · P {usd2(tv['SM-20320'].P)}", "", False),
   ("¿Cuántos clientes con m = 5 tienen utilidad negativa?", f"{ns['m5_neg']} (±3)", "", False),
   ("¿Qué porcentaje de la utilidad aporta el 20 % de clientes más rentable?", f"{ns['top20_P']:.0f} %",
    f"{ns['top20_M']:.0f} %: ordenaron por ventas en vez de utilidad.", False),
   (f"¿En qué segmento queda {TESTIGOS[4][1]} (AD-10180) calificando sobre toda la base y calificando solo dentro de Oficina en casa?",
    f"{tv['AD-10180'].lab} global · {w.loc['AD-10180','lab']} dentro del segmento", "", False),
   ("¿Cuántos clientes de Oficina en casa tienen m = 5 en cada versión?",
    f"{ofc_m5_g} global · {ofc_m5_w} dentro del segmento",
    "Dentro del segmento siempre da cerca de 20 %: es por construcción, no un hallazgo.", False),
  ]),
 dict(nombre="Informe final y defensa",
  para="El cierre explica por qué pasa lo que encontraron y qué haría la gerencia con eso.",
  pasos=["Bajen de cliente a línea para explicar la utilidad negativa: descuento, subcategoría y estado.",
         "Escriban por cada segmento una acción, un mensaje comercial de una frase y la métrica que diría si funcionó.",
         "Cierren con las limitaciones del análisis y el prompt final que usaron con la IA.",
         "Para nota sobresaliente: repitan el RFM+P en cortes de 12 meses (septiembre a agosto) para ver cómo se mueven los clientes, o contrasten con KMeans."],
  entregable="Informe en el cuaderno, con las respuestas de control al inicio. Defensa oral del grupo.",
  preguntas=[
   ("¿Cuál es la peor línea de Laurel Beltran (utilidad, subcategoría y descuento) y cuánto sería su P sin ella?",
    f"{usd2(peor_lb.utilidad)} · {peor_lb.subcategoria} · {peor_lb.descuento*100:.0f} % · P sin ella {usd2(tv['LB-16795'].P - peor_lb.utilidad)}", "", False),
   ("¿Qué porcentaje de los clientes con pérdida sería rentable sin su peor línea?",
    f"{pct(ns['salvados'], (c.P<0).sum()):.0f} %", "", False),
   ("¿Cuánta utilidad dejan, en total, las líneas con descuento mayor a 20 %? ¿Cuántas son?",
    f"{usd(ns['lin_desc'].loc['mas20','u'])} en {int(ns['lin_desc'].loc['mas20','n']):,} líneas", "", False),
   ("¿Cuánta utilidad suman los segmentos En riesgo y No se pueden perder?",
    f"{usd(riesgo_P)} ({T.loc['En riesgo','pp']+T.loc['No se pueden perder','pp']:.1f} %)", "", False),
   ("Al corte del 30-ago-2026, con ventana de 12 meses, ¿cuánto les dio R y F de Anna Häberlin? ¿En qué segmento queda?",
    f"R {int(f26.loc['AH-10690','R'])} · F {int(f26.loc['AH-10690','F'])} · {f26.loc['AH-10690','lab']}",
    "Que en la foto acumulada sea No se pueden perder es justamente el hallazgo.", True),
   ("¿Cuánto les dio la P de Laurel Beltran en las ventanas que cierran el 30-ago-2025 y el 30-ago-2026?",
    f"{usd2(f25.loc['LB-16795','P'])} y {usd2(f26.loc['LB-16795','P'])}", "", True),
   ("¿Qué porcentaje de clientes conserva su segmento entre esos dos cortes?", f"{mismo:.0f} % (±3)", "", True),
   ("Con KMeans y k = 4 sobre variables transformadas, ¿qué silueta obtienen?",
    f"{ns['sil'][4]:.2f} (±0.03). Aparece un grupo de {int(ns['ktab'].loc[ns['k_loss'],'n'])} clientes casi todos con pérdida",
    "Un grupo de pocos clientes extremos: escalaron sin transformar las variables.", True),
  ]),
]
NPREG = sum(len(e["preguntas"]) for e in ENTREGAS)

# ---------------------------------------------------------------- estilos compartidos
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com">'
         '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Serif+4:opsz,wght@8..60,500;8..60,600&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">')
CSS = """
:root {
  --bg: #ffffff; --ink: #1e1e1e; --mute: #6b6b6b; --line: #e6e2df; --acc: #A6192E; --wash: #f7f4f3;
  --f-display: "Source Serif 4", Georgia, serif;
  --f-body: "IBM Plex Sans", "Helvetica Neue", Arial, sans-serif;
  --f-mono: "IBM Plex Mono", ui-monospace, Menlo, monospace;
  color-scheme: light;
}
html, body { background: var(--bg); color: var(--ink); }
body { font-family: var(--f-body); font-size: 16.5px; line-height: 1.6; }
.wrap { max-width: 900px; margin: 0 auto; padding-inline: 20px; padding-block: 40px 90px; }
.prose { max-width: 66ch; }
.eyebrow { font-family: var(--f-mono); font-size: 12px; letter-spacing: .08em; text-transform: uppercase; color: var(--acc); }
h1 { font-family: var(--f-display); font-weight: 600; font-size: clamp(30px, 5vw, 42px); line-height: 1.1; margin: 8px 0 14px; text-wrap: balance; }
h2 { font-family: var(--f-display); font-weight: 600; font-size: 26px; line-height: 1.2; margin: 52px 0 10px; text-wrap: balance; }
h3 { font-size: 16px; font-weight: 600; margin: 22px 0 6px; }
p { margin: 0 0 12px; }
header.top { border-bottom: 2px solid var(--ink); padding-bottom: 20px; }
.lede { font-size: 18px; }
code { font-family: var(--f-mono); font-size: .88em; background: var(--wash); padding: 1px 5px; }
.scroll { overflow-x: auto; margin: 12px 0 18px; }
table { border-collapse: collapse; width: 100%; min-width: 560px; font-size: 14.5px; font-variant-numeric: tabular-nums; }
th { text-align: left; font-size: 12px; font-weight: 600; color: var(--mute); border-bottom: 1.5px solid var(--ink); padding: 8px 12px 6px 0; }
td { border-bottom: 1px solid var(--line); padding: 9px 12px 9px 0; vertical-align: top; }
.qid { font-family: var(--f-mono); font-size: 12px; color: var(--acc); white-space: nowrap; }
.mono { font-family: var(--f-mono); font-size: 13px; }
.avz { font-family: var(--f-mono); font-size: 10.5px; text-transform: uppercase; letter-spacing: .05em; color: var(--acc); border: 1px solid currentColor; padding: 0 5px; margin-left: 6px; white-space: nowrap; }
.entrega { border-top: 1px solid var(--line); margin-top: 44px; padding-top: 8px; scroll-margin-top: 20px; }
.eh { display: grid; grid-template-columns: 64px minmax(0, 1fr); gap: 0 16px; align-items: start; }
.big { font-family: var(--f-display); font-size: 56px; font-weight: 600; color: var(--acc); line-height: 1; margin-top: 30px; }
.eh h2 { margin-top: 34px; }
ol.pasos { margin: 6px 0 14px; padding-left: 22px; max-width: 66ch; }
ol.pasos li { margin-bottom: 6px; }
.box { background: var(--wash); padding: 14px 18px; margin: 14px 0; max-width: 72ch; }
.box p:last-child { margin-bottom: 0; }
.mapa { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 14px; margin: 26px 0 8px; }
.mapa a { display: block; border-top: 3px solid var(--ink); padding-top: 10px; color: var(--ink); text-decoration: none; min-width: 0; }
.mapa a:hover .mt, .mapa a:focus-visible .mt { color: var(--acc); }
.mapa a:focus-visible { outline: 2px solid var(--acc); outline-offset: 3px; }
.mn { font-family: var(--f-display); font-size: 30px; font-weight: 600; color: var(--acc); line-height: 1; }
.mt { font-weight: 600; margin-top: 4px; }
.md { font-size: 13.5px; color: var(--mute); margin-top: 2px; }
button.copiar { font: inherit; font-size: 13.5px; background: var(--bg); color: var(--ink); border: 1px solid var(--ink); padding: 5px 12px; cursor: pointer; }
button.copiar:hover, button.copiar:focus-visible { color: var(--acc); border-color: var(--acc); outline: none; }
pre { background: var(--wash); padding: 14px 16px; overflow-x: auto; font-family: var(--f-mono); font-size: 12.5px; line-height: 1.5; max-height: 320px; }
.src { font-size: 13.5px; color: var(--mute); }
.src a { color: var(--ink); }
@media (max-width: 720px) { .mapa { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
@media (max-width: 460px) { .eh { grid-template-columns: minmax(0, 1fr); } .big { margin-top: 24px; font-size: 42px; } .eh h2 { margin-top: 4px; } }
"""


def esc(s):
    return H.escape(s, quote=False)


def mapa(desc_fn):
    o = ['<nav class="mapa" aria-label="Entregas">']
    for i, e in enumerate(ENTREGAS, 1):
        o.append(f'<a href="#entrega-{i}"><div class="mn">{i}</div><div class="mt">{e["nombre"]}</div><div class="md">{desc_fn(i, e)}</div></a>')
    o.append("</nav>")
    return "".join(o)


TABLA_TESTIGOS = ('<div class="scroll"><table><thead><tr><th>ID</th><th>Cliente</th><th>Por qué lo seguimos</th></tr></thead><tbody>'
                  + "".join(f'<tr><td class="mono">{k}</td><td>{esc(n)}</td><td>{esc(p)}</td></tr>' for k, n, p in TESTIGOS)
                  + "</tbody></table></div>")

# ---------------------------------------------------------------- plantilla markdown para el cuaderno
md = ["## Respuestas de control", "", "| # | Pregunta | Respuesta |", "|---|---|---|"]
for i, e in enumerate(ENTREGAS, 1):
    for k, (q, *_r, avz) in enumerate(e["preguntas"], 1):
        md.append(f"| {i}.{k} | {q}{' (opcional)' if avz else ''} | |")
PLANTILLA = "\n".join(md)

# ---------------------------------------------------------------- página de estudiantes
def entrega_est(i, e):
    filas = "".join(
        f'<tr><td class="qid">{i}.{k}</td><td>{esc(q)}{"<span class=avz>opcional</span>" if avz else ""}</td></tr>'
        for k, (q, _a, _w, avz) in enumerate(e["preguntas"], 1))
    pasos = "".join(f"<li>{esc(p)}</li>" for p in e["pasos"])
    return (f'<section class="entrega" id="entrega-{i}"><div class="eh"><div class="big">{i}</div><div>'
            f'<h2>{e["nombre"]}</h2><p class="prose">{esc(e["para"])}</p></div></div>'
            f'<h3>Qué hacen</h3><ol class="pasos">{pasos}</ol>'
            f'<h3>Qué entregan</h3><p class="prose">{esc(e["entregable"])}</p>'
            f'<h3>Preguntas de control</h3><p class="prose">Respondan con el número, no con un párrafo.</p>'
            f'<div class="scroll"><table><thead><tr><th>#</th><th>Pregunta</th></tr></thead><tbody>{filas}</tbody></table></div></section>')


est = f"""<meta charset="utf-8">
<title>Proyecto RFM+P Superstore</title>
{FONTS}
<style>
/* Enunciado de una columna: el caso, cómo funciona, cuatro entregas y las reglas. Fondo blanco siempre. */
{CSS}
</style>
<div class="wrap">
<header class="top">
  <div class="eyebrow">ADM 2003 · Análisis de Datos · Proyecto de medio semestre</div>
  <h1>Proyecto RFM+P: ¿qué clientes cuidar en Superstore?</h1>
  <p class="lede prose">Superstore vende muebles, suministros de oficina y tecnología en Estados Unidos. Tiene {N} clientes y cuatro años de historia en <code>superstore_2026.csv</code>. La gerencia comercial necesita responder tres preguntas: a qué clientes cuidar primero, a quiénes vale la pena recuperar y con quiénes está perdiendo plata. Ustedes las van a responder con un análisis RFM+P.</p>
</header>

<h2>RFM+P en pocas palabras</h2>
<div class="prose">
<p>A cada cliente se le miden cuatro cosas. <b>R</b>, recencia: cuántos días pasaron desde su última compra. <b>F</b>, frecuencia: cuántos pedidos hizo. <b>M</b>, monto: cuánto compró en total. <b>P</b>, utilidad: cuánto ganó la empresa con él. Con esas cuatro medidas se arman grupos de clientes parecidos y se decide qué hacer con cada grupo.</p>
<p>Las tres primeras son el RFM clásico del marketing. La P es la que agregamos en este curso, porque en Superstore hay clientes que compran mucho y dejan pérdidas.</p>
</div>

<h2>Cómo funciona el proyecto</h2>
<div class="prose">
<p>El trabajo es en grupo y tiene cuatro entregas. Las tres primeras son puntos de control: las revisamos en clase con las preguntas de control. Si sus números coinciden, siguen adelante. Si no coinciden, encuentran el error antes de avanzar, que es mucho más barato que encontrarlo al final. La cuarta entrega es el informe con la defensa oral del grupo.</p>
</div>
{mapa(lambda i, e: ["La base y su calidad", "Una fila por cliente", "Grupos con nombre y la P", "Causas, acciones y defensa"][i-1])}

<h2>Los clientes testigo</h2>
<div class="prose">
<p>Durante todo el proyecto van a seguir a seis clientes. Cada uno tiene algo particular que pone a prueba una parte del cálculo. Sus números son la forma más rápida de saber si van bien, para ustedes y para mí.</p>
</div>
{TABLA_TESTIGOS}

{"".join(entrega_est(i, e) for i, e in enumerate(ENTREGAS, 1))}

<h2>Las respuestas de control en su cuaderno</h2>
<div class="prose">
<p>Pongan esta tabla al inicio del cuaderno y llénenla a medida que avanzan. Es lo primero que voy a mirar en cada revisión. Las preguntas marcadas como opcionales son para quienes buscan la nota más alta.</p>
</div>
<p><button type="button" class="copiar" id="copiar">Copiar plantilla</button> <span id="copiado" class="src" role="status"></span></p>
<pre id="plantilla">{esc(PLANTILLA)}</pre>

<h2>Sobre el uso de IA</h2>
<div class="prose">
<p>Pueden usar IA en todo el proyecto, y les va a ahorrar tiempo con el código. Tres condiciones. Los números del informe salen de su cuaderno, no del chat; si la IA les da una cifra, verifíquenla con los clientes testigo. Cada decisión (qué hicieron con el duplicado, cómo resolvieron los empates, qué fecha de referencia usaron) la explican con sus palabras. Y al final del cuaderno va el prompt final que usaron.</p>
<p>En la defensa cualquier integrante del grupo puede recibir cualquier pregunta, y se responde sin leer. Por ejemplo: ¿por qué Sean Miller no es un buen cliente si es el que más compra?</p>
</div>

<h2>Qué cuenta en la nota</h2>
<div class="prose">
<p>Cuatro cosas, en este orden de importancia. Que los números sean correctos, y eso se ve en las respuestas de control. Que las decisiones estén escritas y justificadas. Que los hallazgos usen la utilidad y no solo las ventas. Y que las recomendaciones sean concretas para Superstore, no consejos que servirían para cualquier tienda, y que puedan defenderlas.</p>
</div>
</div>
<script>
(function () {{
  var b = document.getElementById('copiar'), pre = document.getElementById('plantilla'), msg = document.getElementById('copiado');
  function seleccionar() {{ var r = document.createRange(); r.selectNodeContents(pre); var s = window.getSelection(); s.removeAllRanges(); s.addRange(r); }}
  b.addEventListener('click', function () {{
    var t = pre.textContent;
    if (navigator.clipboard && navigator.clipboard.writeText) {{
      navigator.clipboard.writeText(t).then(function () {{ msg.textContent = 'Copiada. Péguenla en una celda de texto del cuaderno.'; }},
        function () {{ seleccionar(); msg.textContent = 'Texto seleccionado. Cópienlo con Ctrl+C o Cmd+C.'; }});
    }} else {{ seleccionar(); msg.textContent = 'Texto seleccionado. Cópienlo con Ctrl+C o Cmd+C.'; }}
  }});
}})();
</script>
"""
(AQUI / "proyecto_rfmp_estudiantes.html").write_text(est, encoding="utf-8")

# ---------------------------------------------------------------- clave docente
def entrega_doc(i, e):
    filas = "".join(
        f'<tr><td class="qid">{i}.{k}</td><td>{esc(q)}{"<span class=avz>opcional</span>" if avz else ""}</td>'
        f'<td class="mono">{esc(a)}</td><td>{esc(wr) if wr else "<span class=src>·</span>"}</td></tr>'
        for k, (q, a, wr, avz) in enumerate(e["preguntas"], 1))
    return (f'<section class="entrega" id="entrega-{i}"><div class="eh"><div class="big">{i}</div><div>'
            f'<h2>{e["nombre"]}</h2><p class="prose">{esc(e["entregable"])}</p></div></div>'
            f'<div class="scroll"><table style="min-width:760px"><thead><tr><th>#</th><th style="width:34%">Pregunta</th><th style="width:30%">Respuesta correcta</th>'
            f'<th>Si responde otra cosa</th></tr></thead><tbody>{filas}</tbody></table></div></section>')


tv_rows = "".join(
    f'<tr><td class="mono">{k}</td><td>{esc(n)}</td><td class="mono">{int(tv[k].R)}</td><td class="mono">{int(tv[k].F)}</td>'
    f'<td class="mono">{usd2(tv[k].M)}</td><td class="mono">{usd2(tv[k].P)}</td>'
    f'<td class="mono">{tv[k].r} {tv[k].f} {tv[k].m} {tv[k].p}</td><td>{tv[k].lab}</td></tr>'
    for k, n, _ in TESTIGOS)

doc = f"""<meta charset="utf-8">
<title>Checkpoints RFM+P</title>
{FONTS}
<style>
/* Clave docente: mismas entregas y preguntas que el enunciado, con respuesta y diagnóstico del error. Fondo blanco siempre. */
{CSS}
</style>
<div class="wrap">
<header class="top">
  <div class="eyebrow">ADM 2003 · Proyecto RFM+P · Clave docente</div>
  <h1>Checkpoints RFM+P: preguntas de control y respuestas</h1>
  <p class="lede prose">Las {NPREG} preguntas de control del enunciado, con la respuesta correcta y lo que significa cada respuesta equivocada frecuente. Sirve para revisar en clase en dos minutos por grupo: se mira la tabla de respuestas al inicio del cuaderno y se compara con esta página.</p>
</header>

{mapa(lambda i, e: f"{len(e['preguntas'])} preguntas")}

<h2>Clientes testigo</h2>
<p class="prose">Valores de referencia con fecha {fecha(REF)}, quintiles sobre <code>rank(method="first")</code> y el mapa estándar de segmentos sobre R y F. El puntaje f de Sean Miller depende del desempate (F = 5 cae en un borde), así que su segmento puede ser Por dormirse o Necesitan atención.</p>
<div class="scroll"><table><thead><tr><th>ID</th><th>Cliente</th><th>R</th><th>F</th><th>M</th><th>P</th><th>r f m p</th><th>Segmento</th></tr></thead><tbody>{tv_rows}</tbody></table></div>

{"".join(entrega_doc(i, e) for i, e in enumerate(ENTREGAS, 1))}

<h2>Cómo leer las diferencias</h2>
<div class="prose">
<p>Las entregas 1 y 2 tienen respuestas exactas. Si un grupo no coincide, hay un error de cálculo, y la columna de la derecha casi siempre dice cuál. Desde la entrega 3 las cifras dependen de decisiones del grupo (desempate, mapa de segmentos, duplicado). Si caen fuera de la tolerancia, la pregunta es si la decisión está escrita y justificada. Un grupo con números distintos y bien explicados está mejor que uno con los números exactos sin saber por qué.</p>
</div>

<h2>Por qué el proyecto está armado así</h2>
<div class="prose">
<p>El enunciado sigue el marco de transparencia de Winkelmes (TILT): cada entrega dice para qué sirve, qué hay que hacer y cómo se sabe que está bien. Los estudios de ese marco muestran mejoras en confianza académica y sentido de pertenencia, mayores en estudiantes de primera generación. El orden de diseño es el del diseño inverso de Wiggins y McTighe: primero las evidencias que demuestran que entendieron (las respuestas de control y la defensa), después las actividades.</p>
<p>Las preguntas con clientes testigo cumplen dos funciones. Para el grupo son una autoverificación inmediata. Para el docente son evidencia de proceso: una cifra puntual de un cliente concreto se obtiene corriendo el cuaderno, no pidiéndosela a un chat. Junto con la defensa oral sin lectura y la política explícita de uso de IA, son los pilares que la literatura reciente propone para evaluaciones resistentes a la IA.</p>
<p class="src">Fuentes: <a href="https://citl.indiana.edu/teaching-resources/evidence-based/transparency.html">Transparency in Learning and Teaching, Indiana University</a> · <a href="https://teaching.resources.osu.edu/examples/using-transparent-assignment">Using the Transparent Assignment Template, Ohio State</a> · <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC13422401/">Designing AI-resilient assessment in higher education: a four-pillar conceptual framework</a> · <a href="https://bokcenter.harvard.edu/courses-and-assignments-in-age-of-ai">Designing Courses and Assignments in the Age of AI, Harvard Bok Center</a> · Wiggins, G. y McTighe, J. (2005). <em>Understanding by Design</em>. ASCD.</p>
</div>
</div>
"""
(AQUI / "checkpoints_rfmp.html").write_text(doc, encoding="utf-8")
print("escrito", NPREG, "preguntas")
