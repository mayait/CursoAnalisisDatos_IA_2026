#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Proyecto RFM+P · versión simple. Enunciado para estudiantes y clave docente.

Las dos páginas salen de la misma lista de preguntas. Las respuestas se
calculan con generar_informe.py sobre superstore_2026.csv.
La versión anterior, más larga, quedó en _v1/.

Uso:  python3 generar_checkpoints.py
"""
import html as H
import re
import runpy
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ns = runpy.run_path(str(AQUI / "generar_informe.py"))
d, c, g, T, N = ns["d"], ns["c"], ns["g"], ns["tab"], ns["N"]
usd, fecha, pct, MAPA = ns["usd"], ns["fecha"], ns["pct"], ns["MAPA"]
REF, HOY = ns["REF"], ns["HOY"]


def usd2(x):
    return ("−$" if x < 0 else "$") + f"{abs(x):,.2f}"


ab, sm = g.loc["AB-10105"], g.loc["SM-20320"]
lin_ab = int((d.cliente_id == "AB-10105").sum())
vc_ab = (d.venta * d.cantidad)[d.cliente_id == "AB-10105"].sum()
rhoy_ab = (HOY - c.loc["AB-10105", "ult"]).days
riesgo_P = g[g.lab.isin(["En riesgo", "No se pueden perder"])].P.sum()
sc = ns["segcom"]

# (pregunta, respuesta, qué significa una respuesta equivocada)
ETAPAS = [
 dict(titulo="Conocer los datos",
  idea="Antes de calcular nada, entiendan qué tienen en las manos. Cada fila del archivo es un producto dentro de un pedido, no un pedido completo.",
  hacer=["Cuenten filas, pedidos y clientes.",
         "Busquen problemas: datos vacíos, filas repetidas, fechas raras.",
         "Anoten cada problema y qué hicieron con él."],
  entregar="Una celda de texto que describa la base y una lista corta de los problemas que encontraron.",
  preguntas=[
   ("¿Cuántas filas, pedidos y clientes tiene la base?",
    f"{len(d):,} filas · {d.pedido_id.nunique():,} pedidos · {N} clientes",
    f"Si dicen {len(d):,} pedidos, creen que cada fila es un pedido."),
   ("¿Cuántas filas repetidas encontraron?",
    f"{ns['n_dup']}, en el pedido {ns['dup'].pedido_id}",
    "Si dicen cero, compararon incluyendo linea_id, que nunca se repite."),
  ]),
 dict(titulo="Calcular R, F, M y P",
  idea="Ahora pasan de filas a clientes. Al final de esta etapa tienen una tabla con una fila por cliente y cuatro números.",
  hacer=[f"Usen como fecha de hoy el {fecha(REF)}, el día después del último pedido.",
         "R: días desde la última compra. F: pedidos distintos. M: suma de ventas. P: suma de utilidad.",
         "Hagan un histograma de cada una y escriban qué ven."],
  entregar="La tabla de clientes y los cuatro histogramas con una frase cada uno.",
  preguntas=[
   ("¿Cuánto les dio R, F, M y P de Adrian Barton (AB-10105)?",
    f"R {int(ab.R)} · F {int(ab.F)} · M {usd2(ab.M)} · P {usd2(ab.P)}",
    f"F {lin_ab}: contaron filas en vez de pedidos. M {usd2(vc_ab)}: multiplicaron venta por cantidad. R {rhoy_ab}: usaron la fecha real de hoy."),
   ("¿Cuántos clientes tienen P negativa?",
    f"{int((c.P < 0).sum())}, el {pct((c.P < 0).sum(), N):.1f} % de la base", ""),
  ]),
 dict(titulo="Armar los grupos",
  idea="Cada cliente recibe una nota de 1 a 5 en cada letra, y con las notas de R y F se le asigna un grupo con nombre.",
  hacer=["Ordenen a los clientes en cada letra y pártanlos en cinco partes iguales. El 20 % mejor recibe 5. En R es al revés: quien compró más recientemente recibe 5.",
         "Con las notas de R y F, ubiquen a cada cliente en la tabla de grupos de abajo.",
         "Para cada grupo, calculen cuántos clientes tiene, cuánto vende y cuánto gana."],
  entregar="Una tabla con los grupos: número de clientes, % de ventas, % de utilidad.",
  preguntas=[
   ("¿Qué notas tiene Adrian Barton y en qué grupo quedó?",
    f"r {ab.r} · f {ab.f} · m {ab.m} · p {ab.p} · {ab.lab}",
    f"Si r = {6 - ab.r}, no dieron vuelta la nota de R."),
   ("¿Cuántos clientes quedaron en Campeones y cuántos en Hibernando?",
    f"{int(T.loc['Campeones','n'])} y {int(T.loc['Hibernando','n'])} (±5 según cómo resolvieron los empates)", ""),
   ("Sean Miller es el cliente que más compra. ¿Cuánto les dio su P?",
    f"{usd2(sm.P)}", "Es la razón de ser de la P: vender mucho no es lo mismo que ganar."),
  ]),
 dict(titulo="Explicar y recomendar",
  idea="Ya saben quién es quién. Ahora digan por qué pasa lo que vieron y qué haría la gerencia con cada grupo.",
  hacer=["Busquen qué tienen en común las ventas que pierden plata. Miren el descuento.",
         "Comparen los tres segmentos comerciales (Consumidor, Corporativo y Oficina en casa) usando la tabla de toda la base.",
         "Escriban para cada grupo una acción concreta y cómo sabrían si funcionó."],
  entregar="El informe final en el cuaderno y la defensa oral del grupo.",
  preguntas=[
   ("¿Qué porcentaje de la utilidad total aporta el 20 % de clientes más rentable?",
    f"{ns['top20_P']:.0f} %", f"{ns['top20_M']:.0f} %: ordenaron por ventas, no por utilidad."),
   ("¿Qué porcentaje de las filas con descuento mayor a 20 % pierde plata?",
    f"{ns['lin_desc'].loc['mas20','neg']:.0f} %, y entre todas restan {usd(ns['lin_desc'].loc['mas20','u'])}", ""),
   ("¿Cuánta utilidad suman los grupos En riesgo y No se pueden perder?",
    f"{usd(riesgo_P)}, el {T.loc['En riesgo','pp'] + T.loc['No se pueden perder','pp']:.1f} % del total", ""),
   ("¿Qué margen (utilidad entre ventas) tiene cada segmento comercial?",
    f"Consumidor {sc.loc['Consumidor','mg']:.1f} % · Corporativo {sc.loc['Corporativo','mg']:.1f} % · Oficina en casa {sc.loc['Oficina en casa','mg']:.1f} %",
    "Si las cifras no coinciden, promediaron márgenes por cliente. El margen se calcula con los totales del segmento."),
  ]),
]
NPREG = sum(len(e["preguntas"]) for e in ETAPAS)

# ---------------------------------------------------------------- tabla de grupos (R filas, F columnas)
COLOR = {"Campeones": "#f3d6da", "Leales": "#f8e6e8", "Potenciales leales": "#fbf0f1",
         "Nuevos": "#eef3ef", "Prometedores": "#e3ede6", "Necesitan atención": "#f6f1e4",
         "Por dormirse": "#efe9dc", "En riesgo": "#ebe7e5", "No se pueden perder": "#e0dad7",
         "Hibernando": "#f4f2f1"}


def grupo(r, f):
    k = f"{r}{f}"
    for rx, nom in MAPA:
        if re.fullmatch(rx, k):
            return nom


def tabla_grupos():
    o = ['<div class="scroll"><table class="grid"><thead><tr><th></th>']
    o += [f"<th>F = {f}</th>" for f in range(1, 6)]
    o.append("</tr></thead><tbody>")
    for r in range(5, 0, -1):
        o.append(f"<tr><th>R = {r}</th>")
        for f in range(1, 6):
            n = grupo(r, f)
            o.append(f'<td style="background:{COLOR[n]}">{n}</td>')
        o.append("</tr>")
    o.append("</tbody></table></div>")
    return "".join(o)


# ---------------------------------------------------------------- estilos
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
body { font-family: var(--f-body); font-size: 17px; line-height: 1.65; }
.wrap { max-width: 760px; margin: 0 auto; padding-inline: 20px; padding-block: 44px 90px; }
.eyebrow { font-family: var(--f-mono); font-size: 12px; letter-spacing: .08em; text-transform: uppercase; color: var(--acc); }
h1 { font-family: var(--f-display); font-weight: 600; font-size: clamp(32px, 6vw, 46px); line-height: 1.08; margin: 8px 0 16px; text-wrap: balance; }
h2 { font-family: var(--f-display); font-weight: 600; font-size: 27px; line-height: 1.2; margin: 0 0 8px; text-wrap: balance; }
h3 { font-size: 13px; font-family: var(--f-mono); font-weight: 500; text-transform: uppercase; letter-spacing: .06em; color: var(--mute); margin: 22px 0 6px; }
p { margin: 0 0 12px; }
.lede { font-size: 19px; }
section { margin-top: 52px; }
.ej { background: var(--wash); padding: 16px 20px; margin: 16px 0; }
.ej p:last-child { margin: 0; }
.letras { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px; margin: 18px 0; }
.letra { border-top: 3px solid var(--ink); padding-top: 8px; min-width: 0; }
.letra b { font-family: var(--f-display); font-size: 34px; color: var(--acc); line-height: 1; display: block; }
.letra span { font-size: 14.5px; display: block; margin-top: 4px; line-height: 1.4; }
.etapa { border-top: 1px solid var(--line); padding-top: 28px; margin-top: 44px; }
.eh { display: flex; gap: 18px; align-items: baseline; }
.n { font-family: var(--f-display); font-size: 52px; font-weight: 600; color: var(--acc); line-height: 1; flex: none; }
.cuando { font-size: 14px; color: var(--mute); }
ol { margin: 4px 0 8px; padding-left: 22px; }
li { margin-bottom: 6px; }
.preg { list-style: none; padding: 0; margin: 6px 0 0; }
.preg li { padding: 10px 0; border-bottom: 1px solid var(--line); display: grid; grid-template-columns: 38px minmax(0, 1fr); gap: 4px 10px; }
.preg li:first-child { border-top: 1px solid var(--line); }
.qid { font-family: var(--f-mono); font-size: 13px; color: var(--acc); padding-top: 3px; }
.resp { grid-column: 2; font-family: var(--f-mono); font-size: 14px; }
.mal { grid-column: 2; font-size: 14.5px; color: var(--mute); }
.scroll { overflow-x: auto; margin: 14px 0; }
table.grid { border-collapse: separate; border-spacing: 3px; width: 100%; min-width: 520px; font-size: 13.5px; }
table.grid th { font-weight: 600; font-size: 12.5px; color: var(--mute); padding: 4px 6px; text-align: center; }
table.grid tbody th { text-align: right; white-space: nowrap; }
table.grid td { padding: 12px 6px; text-align: center; color: var(--ink); line-height: 1.25; }
code { font-family: var(--f-mono); font-size: .88em; background: var(--wash); padding: 1px 5px; }
pre { background: var(--wash); padding: 14px 16px; overflow-x: auto; font-family: var(--f-mono); font-size: 13px; line-height: 1.5; }
button.copiar { font: inherit; font-size: 14px; background: var(--bg); color: var(--ink); border: 1px solid var(--ink); padding: 6px 14px; cursor: pointer; }
button.copiar:hover, button.copiar:focus-visible { color: var(--acc); border-color: var(--acc); outline: none; }
.nota { font-size: 14px; color: var(--mute); }
@media (max-width: 560px) { .letras { grid-template-columns: repeat(2, minmax(0, 1fr)); } .n { font-size: 40px; } }
"""


def esc(s):
    return H.escape(s, quote=False)


def etapa(i, e, docente):
    pasos = "".join(f"<li>{esc(p)}</li>" for p in e["hacer"])
    preg = []
    for k, (q, a, m) in enumerate(e["preguntas"], 1):
        extra = ""
        if docente:
            extra = f'<span class="resp">{esc(a)}</span>' + (f'<span class="mal">{esc(m)}</span>' if m else "")
        preg.append(f'<li><span class="qid">{i}.{k}</span><span>{esc(q)}</span>{extra}</li>')
    grupos = tabla_grupos() if i == 3 and not docente else ""
    return (f'<div class="etapa"><div class="eh"><span class="n">{i}</span><div><h2>{e["titulo"]}</h2>'
            '</div></div>'
            f'<p>{esc(e["idea"])}</p><h3>Qué hacen</h3><ol>{pasos}</ol>{grupos}'
            f'<h3>Qué entregan</h3><p>{esc(e["entregar"])}</p>'
            f'<h3>{"Preguntas y respuestas" if docente else "Respondan con un número"}</h3>'
            f'<ul class="preg">{"".join(preg)}</ul></div>')


md = ["| # | Pregunta | Respuesta |", "|---|---|---|"]
for i, e in enumerate(ETAPAS, 1):
    for k, (q, _a, _m) in enumerate(e["preguntas"], 1):
        md.append(f"| {i}.{k} | {q} | |")
PLANTILLA = "\n".join(md)

# ---------------------------------------------------------------- estudiantes
est = f"""<meta charset="utf-8">
<title>Proyecto RFM+P Superstore</title>
{FONTS}
<style>
/* Una sola columna angosta, frases cortas, cuatro etapas. Fondo blanco siempre. */
{CSS}
</style>
<div class="wrap">
<div class="eyebrow">ADM 2003 · Proyecto de medio semestre</div>
<h1>¿A qué clientes debe cuidar Superstore?</h1>
<p class="lede">Superstore tiene {N} clientes y cuatro años de ventas en el archivo <code>superstore_2026.csv</code>. Quiere saber a quiénes cuidar, a quiénes recuperar y con quiénes está perdiendo plata. Ese es su trabajo.</p>

<section>
<h2>La herramienta: RFM+P</h2>
<p>Para cada cliente se miden cuatro cosas.</p>
<div class="letras">
  <div class="letra"><b>R</b><span>Hace cuántos días compró por última vez</span></div>
  <div class="letra"><b>F</b><span>Cuántos pedidos ha hecho</span></div>
  <div class="letra"><b>M</b><span>Cuánto ha comprado en total</span></div>
  <div class="letra"><b>P</b><span>Cuánto ha ganado la empresa con él</span></div>
</div>
<div class="ej"><p><b>Un ejemplo inventado.</b> Rosa compró tres veces. La última fue hace 10 días, en total gastó $500 y la tienda le ganó $60. Su RFM+P es R = 10, F = 3, M = $500, P = $60.</p></div>
<p>Con esos cuatro números se forman grupos de clientes parecidos. Después se decide qué hacer con cada grupo.</p>
</section>

<section>
<h2>Cómo vamos a trabajar</h2>
<p>En grupo y en cuatro etapas. Cada etapa termina con unas preguntas que se responden con un número. En clase revisamos esos números juntos. Si coinciden con los míos, siguen. Si no, encuentran el error antes de avanzar.</p>
</section>

{"".join(etapa(i, e, False) for i, e in enumerate(ETAPAS, 1))}

<section>
<h2>Su hoja de respuestas</h2>
<p>Copien esta tabla en una celda de texto al inicio del cuaderno y llénenla a medida que avanzan.</p>
<p><button type="button" class="copiar" id="copiar">Copiar la tabla</button> <span id="msg" class="nota" role="status"></span></p>
<pre id="plantilla">{esc(PLANTILLA)}</pre>
</section>

<section>
<h2>Sobre la IA</h2>
<p>Pueden usarla todo lo que quieran. Tres condiciones: los números salen de su cuaderno, no del chat. Cada decisión la explican con sus palabras. Y al final del cuaderno pegan el prompt que usaron.</p>
<p>En la defensa cualquiera del grupo puede recibir cualquier pregunta, y se responde sin leer.</p>
</section>

<section>
<h2>Qué cuenta en la nota</h2>
<p>Que los números estén bien. Que expliquen sus decisiones. Que usen la utilidad, no solo las ventas. Y que sus recomendaciones sirvan para Superstore y no para cualquier tienda.</p>
<p class="nota">Si quieren ir más allá: repitan el análisis solo con el último año y comparen quién cambió de grupo, o prueben un modelo de agrupamiento como KMeans.</p>
</section>
</div>
<script>
(function () {{
  var b = document.getElementById('copiar'), pre = document.getElementById('plantilla'), msg = document.getElementById('msg');
  function sel() {{ var r = document.createRange(); r.selectNodeContents(pre); var s = window.getSelection(); s.removeAllRanges(); s.addRange(r); msg.textContent = 'Tabla seleccionada. Cópienla con Ctrl+C o Cmd+C.'; }}
  b.addEventListener('click', function () {{
    if (navigator.clipboard && navigator.clipboard.writeText) {{
      navigator.clipboard.writeText(pre.textContent).then(function () {{ msg.textContent = 'Copiada.'; }}, sel);
    }} else {{ sel(); }}
  }});
}})();
</script>
"""
(AQUI / "proyecto_rfmp_estudiantes.html").write_text(est, encoding="utf-8")

# ---------------------------------------------------------------- docente
doc = f"""<meta charset="utf-8">
<title>Checkpoints RFM+P</title>
{FONTS}
<style>
/* Clave docente: las mismas cuatro etapas, con la respuesta y lo que revela un error. Fondo blanco siempre. */
{CSS}
</style>
<div class="wrap">
<div class="eyebrow">ADM 2003 · Proyecto RFM+P · Clave docente</div>
<h1>Respuestas de control</h1>
<p class="lede">Las {NPREG} preguntas del enunciado con su respuesta. En gris, lo que significa la respuesta equivocada más común. Con esto se revisa un grupo en dos minutos.</p>
<p class="nota">Fecha de referencia {fecha(REF)}. Notas por quintiles sobre <code>rank(method="first")</code>. Las etapas 1 y 2 tienen respuesta exacta. En las etapas 3 y 4 se aceptan diferencias pequeñas si el grupo explica su decisión. La resolución completa y las trampas del archivo están en el informe docente.</p>
{"".join(etapa(i, e, True) for i, e in enumerate(ETAPAS, 1))}
</div>
"""
(AQUI / "checkpoints_rfmp.html").write_text(doc, encoding="utf-8")
print("escrito", NPREG, "preguntas")
