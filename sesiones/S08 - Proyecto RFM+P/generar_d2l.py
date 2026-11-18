#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Página del proyecto RFM+P para D2L (enunciado, dos entregas, rúbrica).

Toma las etapas y preguntas de generar_checkpoints.py para que el enunciado,
la clave docente y el deck digan lo mismo.
Salida: d2l/proyecto-medio-semestre-enunciado.html y d2l/superstore-2026.csv
"""
import html as H
import re
import runpy
import shutil
from pathlib import Path

AQUI = Path(__file__).resolve().parent
ns = runpy.run_path(str(AQUI / "generar_checkpoints.py"))
ETAPAS, MAPA = ns["ETAPAS"], ns["MAPA"]
OUT = AQUI / "d2l"
OUT.mkdir(exist_ok=True)
shutil.copy(AQUI.parents[1] / "sitio" / "datos" / "superstore_2026.csv", OUT / "superstore-2026.csv")
CSV = "superstore-2026.csv"


def e(s):
    return H.escape(s, quote=False)


def etapa(i, et):
    pasos = "".join(f"<li>{e(p)}</li>" for p in et["hacer"])
    preg = "".join(f"<li><b>{i}.{k}</b> {e(q)}</li>" for k, (q, _a, _m) in enumerate(et["preguntas"], 1))
    extra = tabla_grupos() if i == 3 else ""
    return (f'<h3>Etapa {i} · {e(et["titulo"])}</h3><p>{e(et["idea"])}</p>'
            f'<p class="lab">Qué hacen</p><ol>{pasos}</ol>{extra}'
            f'<div class="preg"><p class="lab">Respondan con un número</p><ul>{preg}</ul></div>')


COLOR = {"Campeones": "#a6192e", "Leales": "#e7a3ad", "Potenciales leales": "#f8e6e9", "Nuevos": "#e6f4ec",
         "Prometedores": "#b9e0c8", "Necesitan atención": "#fde3c8", "Por dormirse": "#f6c08e",
         "En riesgo": "#c9dbf2", "No se pueden perder": "#1f5fa8", "Hibernando": "#ececec"}
BLANCO = {"Campeones", "No se pueden perder"}


def tabla_grupos():
    def g(r, f):
        for rx, n in MAPA:
            if re.fullmatch(rx, f"{r}{f}"):
                return n
    filas = []
    for r in range(5, 0, -1):
        celdas = "".join(
            f'<td style="background:{COLOR[g(r,f)]};color:{"#fff" if g(r,f) in BLANCO else "#1e1e1e"}">{e(g(r,f))}</td>'
            for f in range(1, 6))
        filas.append(f"<tr><th>R = {r}</th>{celdas}</tr>")
    cab = "".join(f"<th>F = {f}</th>" for f in range(1, 6))
    return (f'<p class="lab">La tabla de grupos</p><div class="scroll"><table class="grid"><tr><th></th>{cab}</tr>'
            f'{"".join(filas)}</table></div>')


md1 = ["| # | Pregunta | Respuesta |", "|---|---|---|"]
for i, et in enumerate(ETAPAS[:3], 1):
    for k, (q, _a, _m) in enumerate(et["preguntas"], 1):
        md1.append(f"| {i}.{k} | {q} | |")
PLANTILLA = "\n".join(md1)

pagina = f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Proyecto de medio semestre</title>
<style>
*{{box-sizing:border-box}}
body{{margin:0;background:#fff;color:#1e1e1e;font-family:'Segoe UI',system-ui,-apple-system,Arial,sans-serif;font-size:16px;line-height:1.6}}
.cab{{background:#111;color:#fff;border-bottom:5px solid #A6192E;padding:22px 20px 18px}}
.cab .serie{{font-size:13px;letter-spacing:.04em;color:#e8b4bc;margin:0 0 4px}}
.cab h1{{margin:0;font-size:26px;line-height:1.25;font-weight:600}}
.cab .sub{{margin:6px 0 0;color:#d6d6d6;font-size:15px}}
main{{max-width:760px;margin:0 auto;padding:8px 20px 40px}}
h2{{color:#A6192E;font-size:21px;margin:38px 0 10px;padding-top:6px;border-top:1px solid #eee}}
h3{{font-size:17px;margin:26px 0 6px}}
a{{color:#A6192E}}
.indice{{background:#faf6f7;border:1px solid #efdfe2;border-radius:6px;padding:12px 18px;margin:20px 0}}
.indice p{{margin:0 0 6px;font-weight:600}}
.indice ol{{margin:0;padding-left:20px}}
.volver{{font-size:13px;margin:14px 0 0}}
.nota{{border:1px solid #e3e3e3;border-radius:6px;padding:12px 16px;margin:16px 0;background:#fcfcfc}}
.lab{{font-weight:600;margin:14px 0 4px}}
.preg{{background:#faf6f7;border-radius:6px;padding:4px 16px 8px;margin:12px 0}}
.preg ul{{list-style:none;padding:0;margin:0}}
.preg li{{padding:5px 0;border-bottom:1px solid #efdfe2}}
.preg li:last-child{{border-bottom:none}}
.preg b{{color:#A6192E;margin-right:4px}}
table{{border-collapse:collapse;width:100%;font-size:15px;margin:10px 0}}
th,td{{text-align:left;padding:7px 8px;border-bottom:1px solid #e6e2df;vertical-align:top}}
th{{font-size:13px;color:#6b6b6b}}
.scroll{{overflow-x:auto}}
table.grid{{border-collapse:separate;border-spacing:3px;min-width:560px}}
table.grid td{{text-align:center;font-size:13px;font-weight:600;border:none;border-radius:4px;padding:10px 4px}}
table.grid th{{text-align:center;border:none}}
.letras td:first-child{{font-weight:700;color:#A6192E;white-space:nowrap}}
.boton{{display:inline-block;background:#A6192E;color:#fff;text-decoration:none;padding:9px 18px;border-radius:5px;font-weight:600}}
pre{{background:#f6f6f6;padding:12px 14px;overflow-x:auto;font-size:13px;border-radius:5px}}
.entrega{{border:1px solid #e3e3e3;border-radius:8px;padding:4px 18px 12px;margin:14px 0}}
.entrega p.cuando{{color:#6b6b6b;margin:6px 0 0}}
.pie{{border-top:1px solid #eee;margin-top:40px;padding-top:12px;color:#6b6b6b;font-size:14px}}
</style></head><body>
<header class="cab">
<p class="serie">ADM 2003 · Análisis de Datos · Corte de medio semestre</p>
<h1>Proyecto de medio semestre: ¿a qué clientes debe cuidar Superstore?</h1>
<p class="sub">Segmentación RFM+P en dos entregas. Individual: domingo 11 de octubre, 23h59. Grupal: domingo 18 de octubre, 23h59.</p>
</header>
<main>
<nav class="indice" id="indice"><p>En esta página</p><ol>
<li><a href="#encargo">El encargo</a></li>
<li><a href="#rfmp">RFM+P en pocas palabras</a></li>
<li><a href="#como">Cómo vamos a trabajar</a></li>
<li><a href="#entrega1">Entrega 1 · Individual: las tablas</a></li>
<li><a href="#entrega2">Entrega 2 · Grupal: las decisiones</a></li>
<li><a href="#ia">Sobre la IA</a></li>
<li><a href="#rubrica">Rúbrica</a></li>
</ol></nav>

<h2 id="encargo">El encargo</h2>
<p>Superstore vende muebles, suministros de oficina y tecnología en Estados Unidos. Tiene 793 clientes y cuatro años de ventas. La gerencia comercial quiere saber a qué clientes cuidar primero, a quiénes vale la pena recuperar y con quiénes está perdiendo plata.</p>
<p>Ustedes lo van a responder con un análisis RFM+P, en dos partes. Primero cada uno, por su cuenta, construye las tablas. Después, en grupo, convierten esas tablas en decisiones.</p>
<p><a class="boton" href="{CSV}" download>Descargar</a> &nbsp;<code>{CSV}</code>, una fila por producto dentro de cada pedido.</p>
<p class="volver"><a href="#indice">↑ volver al índice</a></p>

<h2 id="rfmp">RFM+P en pocas palabras</h2>
<p>A cada cliente se le miden cuatro cosas.</p>
<table class="letras">
<tr><td>R · Recencia</td><td>Hace cuántos días compró por última vez. Menos es mejor.</td></tr>
<tr><td>F · Frecuencia</td><td>Cuántos pedidos distintos ha hecho.</td></tr>
<tr><td>M · Monto</td><td>Cuánto ha comprado en total.</td></tr>
<tr><td>P · Utilidad</td><td>Cuánto ha ganado la empresa con él.</td></tr>
</table>
<div class="nota"><b>Un ejemplo inventado.</b> Rosa compró tres veces. La última fue hace 10 días, en total gastó $500 y la tienda le ganó $60. Su RFM+P es R = 10, F = 3, M = $500, P = $60.</div>
<p>RFM viene del marketing directo de los años sesenta y lo popularizó Arthur Hughes en <i>Strategic Database Marketing</i> (1994). Fader, Hardie y Lee mostraron en 2005 que R, F y M bastan para estimar el valor futuro de un cliente. La P la agregamos en este curso, porque en Superstore vender no siempre es ganar.</p>
<p class="volver"><a href="#indice">↑ volver al índice</a></p>

<h2 id="como">Cómo vamos a trabajar</h2>
<p>Seguimos el ciclo CRISP-DM que vimos en la presentación. La entrega individual recorre las primeras fases: entender el negocio, entender los datos, prepararlos y modelar, que aquí significa poner notas y armar grupos. La entrega grupal recorre las últimas: evaluar si los grupos tienen sentido y desplegar el resultado como recomendaciones.</p>
<p>Cada etapa termina con preguntas que se responden con un número. En clase revisamos esos números juntos. Si coinciden con los míos, siguen. Si no, encuentran el error antes de avanzar.</p>
<p class="volver"><a href="#indice">↑ volver al índice</a></p>

<h2 id="entrega1">Entrega 1 · Individual: las tablas</h2>
<div class="entrega"><p class="cuando">15 puntos · domingo 11 de octubre, 23h59 · carpeta <b>Proyecto · Entrega 1 individual</b></p>
<p>Cada uno construye, por su cuenta, las tablas RFM+P completas y verificadas. Es la base sobre la que su grupo va a decidir.</p></div>
{etapa(1, ETAPAS[0])}
{etapa(2, ETAPAS[1])}
{etapa(3, ETAPAS[2])}
<h3>Qué entregan</h3>
<p>Un cuaderno <code>.ipynb</code> que corra de principio a fin, con estas partes en este orden:</p>
<ol>
<li>La hoja de respuestas de las etapas 1 a 3, en una celda de texto al inicio.</li>
<li>La lista de problemas que encontraron en los datos y qué hicieron con cada uno.</li>
<li>La tabla de clientes: una fila por cliente con R, F, M, P, sus cuatro notas y su grupo.</li>
<li>La tabla de grupos: clientes, % de clientes, % de ventas, % de utilidad y margen de cada grupo.</li>
<li>Los cuatro histogramas, con una frase cada uno.</li>
<li>Al final, el prompt que usaron con la IA.</li>
</ol>
<p class="lab">Hoja de respuestas para copiar en el cuaderno</p>
<pre>{e(PLANTILLA)}</pre>
<p class="volver"><a href="#indice">↑ volver al índice</a></p>

<h2 id="entrega2">Entrega 2 · Grupal: las decisiones</h2>
<div class="entrega"><p class="cuando">25 puntos · domingo 18 de octubre, 23h59 · carpeta <b>Proyecto · Entrega 2 grupal</b></p>
<p>Con las mismos grupos del caso Carolina. Comparen sus tablas individuales, quédense con una que pase todas las preguntas de control y úsenla para decidir.</p></div>
{etapa(4, ETAPAS[3])}
<h3>Qué entregan</h3>
<p>Un PowerPoint corto, de 6 a 8 láminas, para la gerencia comercial de Superstore. Cada título dice la conclusión y cada lámina muestra la cifra que la sostiene. Una guía:</p>
<ol>
<li>La pregunta y su respuesta en una frase.</li>
<li>Cómo se reparte la base: qué grupos hay y cuánto de la utilidad deja cada uno.</li>
<li>Dónde se pierde plata y por qué.</li>
<li>A quién cuidar primero.</li>
<li>Una acción concreta por grupo y cómo sabrían si funcionó.</li>
<li>Lo que estos datos no permiten decir.</li>
</ol>
<p>En una lámina final de anexo van las respuestas de la etapa 4. Sube el archivo un solo integrante. Después viene la defensa oral en clase: cualquiera del grupo puede recibir cualquier pregunta, y se responde sin leer.</p>
<p class="volver"><a href="#indice">↑ volver al índice</a></p>

<h2 id="ia">Sobre la IA</h2>
<p>Pueden usarla todo lo que quieran. Tres condiciones: los números salen de su cuaderno, no del chat. Cada decisión la explican con sus palabras. Y al final del cuaderno pegan el prompt que usaron.</p>
<p class="volver"><a href="#indice">↑ volver al índice</a></p>

<h2 id="rubrica">Rúbrica</h2>
<p>El proyecto vale 40 puntos: 15 la entrega individual y 25 la grupal. Es el 40 % de la categoría Proyectos, que pesa 25 %: el 10 % de la nota del curso.</p>
<h3>Entrega 1 · Individual (15 puntos)</h3>
<table>
<tr><th>Criterio</th><th>Qué se mira</th><th>Puntos</th></tr>
<tr><td>Respuestas de control</td><td>Las preguntas de las etapas 1 a 3 respondidas y correctas.</td><td>5</td></tr>
<tr><td>Las dos tablas</td><td>Tabla de clientes y tabla de grupos completas, con las columnas pedidas.</td><td>5</td></tr>
<tr><td>Decisiones explicadas</td><td>Qué hicieron con la fila repetida, qué fecha usaron y cómo resolvieron los empates.</td><td>3</td></tr>
<tr><td>Cuaderno y prompt</td><td>El cuaderno corre de principio a fin y trae el prompt final.</td><td>2</td></tr>
</table>
<h3>Entrega 2 · Grupal (25 puntos)</h3>
<table>
<tr><th>Criterio</th><th>Qué se mira</th><th>Puntos</th></tr>
<tr><td>Diagnóstico con la utilidad</td><td>Muestran dónde se gana y dónde se pierde, no solo dónde se vende.</td><td>7</td></tr>
<tr><td>Recomendaciones</td><td>Una acción concreta por grupo, pensada para Superstore, con su forma de medirla.</td><td>8</td></tr>
<tr><td>Láminas claras</td><td>Títulos que dicen la conclusión y una cifra que la sostiene. Anexo con las respuestas de la etapa 4.</td><td>5</td></tr>
<tr><td>Defensa oral</td><td>Cualquier integrante responde sin leer.</td><td>5</td></tr>
</table>
<p class="volver"><a href="#indice">↑ volver al índice</a></p>
<p class="pie">Ve al siguiente tema →</p>
</main></body></html>
"""
pagina = pagina.replace("Con las mismos grupos", "Con los mismos grupos")
(OUT / "proyecto-medio-semestre-enunciado.html").write_bytes(
    pagina.encode("ascii", "xmlcharrefreplace"))
print("ok")
