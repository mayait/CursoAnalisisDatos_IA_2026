#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera las 6 páginas del taller-lección de la sesión 5 para Brightspace.

Un solo caso narrativo (María, gerente regional Oeste de Superstore, comité a
las 10h00) donde cada trampa es su siguiente pregunta. Teoría entretejida:
cada página tiene un CANDADO en CSS puro (sin JavaScript): el estudiante
responde antes de que aparezcan la gráfica y la teoría.

Reglas Brightspace: documentos HTML completos y autocontenidos (imágenes en
base64, todo carácter no ASCII como entidad), fondo blanco siempre, se suben
como ARCHIVOS a Contenido (no pegar en el editor, que despoja <style>).

Salida: brightspace/s05_p1..p6_*.html
"""
import base64
import shutil
from pathlib import Path

AQUI = Path(__file__).resolve().parent
SALIDA = AQUI / "brightspace"
SALIDA.mkdir(exist_ok=True)
# El botón "Descargar" de la página 2 enlaza superstore_2026.csv en RELATIVO:
# el CSV se sube a D2L en la misma carpeta que las páginas (copia lista aquí).
shutil.copy(AQUI.parent.parent / "sitio" / "datos" / "superstore_2026.csv",
            SALIDA / "superstore_2026.csv")

COLAB = ("https://colab.research.google.com/github/mayait/"
         "CursoAnalisisDatos_IA_2026/blob/main/sitio/labs/taller_05_superstore.ipynb")

PASOS = ["La llamada", "El archivo", "El pedido típico",
         "El inventario", "El memo de auditoría", "El comité",
         "El encargo de María"]

CSS = """
body { margin: 0; background: #ffffff; color: #1e1e1e;
  font-family: 'Segoe UI', Helvetica, Arial, sans-serif; font-size: 15px; line-height: 1.6; }
.cont { max-width: 760px; margin: 0 auto; padding-bottom: 40px; }
.top { background: #111111; border-bottom: 5px solid #A6192E; padding: 24px 30px; }
.kicker { font-size: 12px; font-weight: bold; letter-spacing: 1.5px;
  text-transform: uppercase; color: #d98a96; }
.titulo { font-size: 24px; font-weight: bold; color: #ffffff; margin-top: 6px; }
.sub { font-size: 14px; color: #ffffff; opacity: .85; margin-top: 6px; }
.cuerpo { padding: 24px 30px; border: 1px solid #D6D6D6; border-top: none; background: #ffffff; }
p { margin: 0 0 14px 0; }
h2 { font-size: 18px; margin: 24px 0 10px 0; }
.divisor { border-top: 2px solid #A6192E; padding-top: 16px; margin: 26px 0 12px 0;
  font-size: 12px; font-weight: bold; letter-spacing: 1.5px; text-transform: uppercase; color: #a6192e; }
.chat { background: #F2F2F2; border: 1px solid #E2E2E2; border-radius: 10px;
  padding: 12px 16px; margin: 14px 0; }
.chat.mia { background: #FBEDEF; border-color: #EFC9CF; }
.chat .quien { font-size: 12px; font-weight: bold; color: #A6192E; margin-bottom: 4px; }
.chat p { margin: 0 0 8px 0; } .chat p:last-child { margin-bottom: 0; }
.memoq { background: #F7F7F7; border: 1px solid #D6D6D6; padding: 14px 18px;
  margin: 14px 0; font-style: italic; }
.caja { background: #FBEDEF; border-left: 5px solid #A6192E; padding: 14px 18px; margin: 16px 0; }
.caja .rot { font-weight: bold; color: #a6192e; margin-bottom: 6px; }
table.datos { width: 100%; border-collapse: collapse; font-size: 14px; margin: 12px 0; }
table.datos th { background: #F4F4F4; text-align: left; }
table.datos th, table.datos td { border: 1px solid #D6D6D6; padding: 7px 10px; }
.figura img { width: 100%; height: auto; border: 1px solid #E5E5E5; display: block; }
.figura .pie { font-size: 12px; color: #6b6b6b; margin: 6px 0 18px 0; }
pre.code { background: #F7F7F7; border: 1px solid #D6D6D6; padding: 12px 14px;
  font-family: Consolas, Menlo, monospace; font-size: 13px; overflow-x: auto; margin: 12px 0; }
.boton { display: inline-block; background: #A6192E; color: #ffffff !important;
  text-decoration: none; font-weight: bold; font-size: 14px; padding: 10px 20px;
  border-radius: 3px; margin: 4px 0; }
.boton.sec { background: #ffffff; color: #A6192E !important; border: 2px solid #A6192E; }
.footer { border-top: 1px solid #D6D6D6; margin-top: 26px; padding-top: 12px;
  font-size: 13px; color: #6b6b6b; }
.footer .sig { font-weight: bold; color: #A6192E; }

/* ── El candado (CSS puro) ─────────────────────────────────────────── */
.bloque { margin: 20px 0; }
.bloque > input.gate { position: absolute; left: -9999px; }
.bloque > input.num { display: block; width: 200px; padding: 10px 12px; margin: 6px 0 14px 0;
  border: 2px solid #D6D6D6; border-radius: 3px; font-size: 16px; font-weight: bold;
  color: #1e1e1e; background: #ffffff; }
.bloque > input.num:focus { border-color: #A6192E; outline: none; }
.apuesta { background: #FBEDEF; border-left: 5px solid #A6192E; padding: 16px 18px; }
.apuesta .rot { font-weight: bold; color: #a6192e; margin-bottom: 6px; }
.opt { display: block; border: 1px solid #D6D6D6; background: #ffffff; padding: 10px 14px;
  margin: 8px 0; border-radius: 3px; cursor: pointer; }
.opt:hover { border-color: #A6192E; }
.fb { display: none; border: 1px solid #D6D6D6; border-left: 4px solid #6b6b6b;
  background: #ffffff; padding: 10px 14px; margin: 10px 0; font-size: 14px; }
.fb.ok { border-left-color: #1a7a3c; }
.fb.meh { border-left-color: #A6192E; }
.hint { font-size: 13px; color: #a6192e; font-weight: bold; margin-top: 10px; }
.reveal { display: none; }
"""


def pagina(n, archivo, sub, cuerpo, extra_css=""):
    sig = ('<div class="sig">Ve al siguiente tema &rarr;</div>' if n < len(PASOS) else
           '<div class="sig">Eso es todo. Tu reporte va al buz&oacute;n antes del mi&eacute;rcoles.</div>')
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{PASOS[n-1]} · La trampa del promedio</title>
<style>{CSS}{extra_css}</style>
</head>
<body>
<div class="cont">
<div class="top">
<div class="kicker">La trampa del promedio</div>
<div class="titulo">{PASOS[n-1]}</div>
<div class="sub">{sub}</div>
</div>
<div class="cuerpo">
{cuerpo}
<div class="footer">{sig}</div>
</div>
</div>
</body>
</html>"""
    final = html.encode("ascii", "xmlcharrefreplace").decode("ascii")
    (SALIDA / archivo).write_text(final, encoding="ascii")
    print(f"{archivo}: {len(final)/1024:.0f} KB")


def img64(nombre, pie):
    dato = base64.b64encode((AQUI / "img" / nombre).read_bytes()).decode()
    return (f'<div class="figura"><img src="data:image/png;base64,{dato}" alt="{pie}">'
            f'<div class="pie">{pie}</div></div>')


def chat(quien, texto, mia=False):
    return (f'<div class="chat{" mia" if mia else ""}"><div class="quien">{quien}</div>'
            f'{texto}</div>')


def radios(name, opciones):
    """opciones: lista de (id, etiqueta, feedback, clase_fb). Devuelve (inputs, labels+fbs, css)."""
    inputs = "".join(f'<input class="gate" type="radio" name="{name}" id="{i}">'
                     for i, _, _, _ in opciones)
    labels = "".join(f'<label class="opt" for="{i}">{e}</label>' for i, e, _, _ in opciones)
    fbs = "".join(f'<div class="fb {c} fb-{i}">{f}</div>' for i, _, f, c in opciones)
    css = "".join(
        f"#{i}:checked ~ .apuesta label[for={i}] {{ border-color: #A6192E; "
        f"background: #FBEDEF; font-weight: 600; }}\n"
        f"#{i}:checked ~ .apuesta .fb-{i} {{ display: block; }}\n"
        for i, _, _, _ in opciones)
    css += (".bloque > input.gate:checked ~ .reveal { display: block; }\n"
            ".bloque > input.gate:checked ~ .apuesta .hint { display: none; }\n")
    return inputs, labels, fbs, css


ABIERTO = ""

# ══════════════════════════════ PÁGINA 1 · La llamada ══════════════════════════
inp, lab, fbs, css1 = radios("q1", [
    ("q1a", "Descriptivo: pide saber qu&eacute; pas&oacute;.",
     "<strong>Exacto.</strong> Mar&iacute;a pide un resumen de lo que ya ocurri&oacute;: "
     "escal&oacute;n 1. Parece el f&aacute;cil. Hoy vas a ver cu&aacute;nto rigor exige.", "ok"),
    ("q1b", "Diagn&oacute;stico: pide saber por qu&eacute; pas&oacute; algo.",
     "Casi. Diagn&oacute;stico ser&iacute;a &laquo;&iquest;por qu&eacute; cay&oacute; el ticket "
     "en julio?&raquo;. Mar&iacute;a solo quiere saber qu&eacute; pas&oacute;: escal&oacute;n 1, "
     "descriptivo. (Sp&oacute;iler: hoy vas a subir al 2 sin darte cuenta.)", "meh"),
    ("q1c", "Predictivo: pide saber qu&eacute; va a pasar.",
     "Todav&iacute;a no. Predictivo ser&iacute;a &laquo;&iquest;cu&aacute;nto valdr&aacute;n los "
     "pedidos en diciembre?&raquo;. Mar&iacute;a pregunta por lo que ya pas&oacute;: "
     "descriptivo, escal&oacute;n 1.", "meh"),
    ("q1d", "Prescriptivo: pide saber qu&eacute; hacer.",
     "Buen ojo, a medias: la <em>decisi&oacute;n</em> final (&iquest;qu&eacute; umbral pongo?) "
     "s&iacute; es prescriptiva. Pero el <em>n&uacute;mero</em> que te pide primero &mdash;el pedido "
     "t&iacute;pico&mdash; es descriptivo. Toda decisi&oacute;n de arriba se apoya en un escal&oacute;n 1 "
     "bien hecho.", "meh"),
])
cuerpo1 = f"""
{chat("Mar&iacute;a &middot; 8h02",
      "<p>&iexcl;Hola! Soy <strong>Mar&iacute;a</strong>, gerente regional Oeste de "
      "<strong>Superstore</strong>, una cadena minorista de Estados Unidos. Me pasaron tu "
      "contacto porque necesito ayuda con datos para unas decisiones del comit&eacute; "
      "de las <strong>10h00</strong>.</p>"
      "<p>La primera: voy a lanzar <strong>&laquo;env&iacute;o gratis desde $X&raquo;</strong> "
      "en mi regi&oacute;n y no s&eacute; a qu&eacute; precio poner la X. Para eso necesito "
      "saber <strong>cu&aacute;nto vale un pedido t&iacute;pico</strong>. &iquest;Me ayudas? "
      "En un rato te mando los datos. &iexcl;Gracias! &#128591;</p>")}
<p>Acabas de recibir tu primer encargo como analista. Antes de tocar un solo dato, los buenos
analistas hacen una cosa: <strong>ubican la pregunta</strong>. Toda pregunta que un negocio le
hace a sus datos vive en uno de cuatro escalones, y saber en cu&aacute;l est&aacute;s te dice
qu&eacute; herramientas necesitas y cu&aacute;nto te van a doler.</p>
<div class="bloque">
{inp}
<div class="apuesta">
<p>La pregunta de Mar&iacute;a &mdash;<em>&laquo;&iquest;cu&aacute;nto vale un pedido
t&iacute;pico?&raquo;</em>&mdash; &iquest;en qu&eacute; escal&oacute;n vive?</p>
{lab}{fbs}
<div class="hint">Elige una opci&oacute;n y seguimos.</div>
</div>
<div class="reveal">
{ABIERTO}
<h2>La escalera de la anal&iacute;tica</h2>
{img64("s05_escalera.png", "Los cuatro escalones. Este semestre los subes todos; hoy trabajas el primero.")}
<p><strong>Descriptivo</strong> (&iquest;qu&eacute; pas&oacute;?), <strong>diagn&oacute;stico</strong>
(&iquest;por qu&eacute; pas&oacute;?), <strong>predictivo</strong> (&iquest;qu&eacute; va a pasar?) y
<strong>prescriptivo</strong> (&iquest;qu&eacute; hacemos?). Subir un escal&oacute;n multiplica el
valor de la respuesta y la dificultad de obtenerla. Y cada escal&oacute;n se apoya en el anterior:
<strong>nadie predice bien lo que no supo describir</strong>.</p>
<div class="caja"><div class="rot">Lo que la escalera NO es</div>
<p style="margin:0;">El escal&oacute;n 1 no es &laquo;lo b&aacute;sico que se salta para llegar a la
inteligencia artificial&raquo;. La mayor&iacute;a de las decisiones reales de un negocio
&mdash;presupuestos, metas, inventarios, promociones como la de Mar&iacute;a&mdash; se toman con
estad&iacute;stica descriptiva. Un modelo entrenado sobre datos mal descritos automatiza el error.</p></div>
<div class="caja"><div class="rot">La promesa de este taller</div>
<p style="margin:0;">Al terminar las 6 p&aacute;ginas vas a poder <strong>detectar, en tres minutos y
con dos n&uacute;meros, cu&aacute;ndo un promedio est&aacute; mintiendo</strong>, y vas a saber
qu&eacute; n&uacute;mero pedir en su lugar. Mar&iacute;a te va a hacer tres preguntas. Las tres
parecen triviales. Las tres esconden una trampa.</p></div>
</div>
</div>
"""
pagina(1, "s05_p1_la_llamada.html", "Mar&iacute;a necesita un precio. T&uacute;, criterio.",
       cuerpo1, css1)

# ══════════════════════════════ PÁGINA 2 · El archivo ══════════════════════════
inp, lab, fbs, css2 = radios("q2", [
    ("q2a", "Abrirlo y leerlo con calma, para hacerme una idea &laquo;a ojo&raquo;.",
     "Int&eacute;ntalo abajo: 46 filas ya marean, y son el 0.5&nbsp;% del archivo. El ojo humano "
     "no promedia 9,994 filas; para eso inventamos la estad&iacute;stica descriptiva.", "meh"),
    ("q2b", "Resumirlo: convertir las 9,994 filas en pocos n&uacute;meros que no las traicionen.",
     "<strong>Eso es describir.</strong> Todo el arte est&aacute; en la parte final: "
     "<em>sin traicionarlas</em>. Hoy ver&aacute;s lo f&aacute;cil que es traicionar con un solo "
     "n&uacute;mero mal elegido.", "ok"),
    ("q2c", "Reenviarle el archivo a Mar&iacute;a tal cual: ah&iacute; est&aacute; todo.",
     "T&eacute;cnicamente cierto, profesionalmente fatal. Mar&iacute;a te contrat&oacute; "
     "exactamente para <em>no</em> tener que leer 9,994 filas antes del comit&eacute;.", "meh"),
])
cuerpo2 = f"""
{chat("Mar&iacute;a &middot; 8h10",
      "<p>&iexcl;Listo! Te adjunt&eacute; <strong>superstore_2026.csv</strong>: toda la venta de la "
      "cadena, cuatro a&ntilde;os, hasta el s&aacute;bado pasado. Son 9,994 l&iacute;neas de venta "
      "en 5,009 pedidos. Me dices el n&uacute;mero apenas puedas.</p>")}
<div class="bloque">
{inp}
<div class="apuesta">
<p>Tienes un archivo de 9,994 filas y una gerente esperando <em>un</em> n&uacute;mero.
&iquest;Cu&aacute;l es el plan?</p>
{lab}{fbs}
<div class="hint">Elige una opci&oacute;n y te muestro el archivo.</div>
</div>
<div class="reveal">
{ABIERTO}
<h2>As&iacute; llega la realidad</h2>
{img64("s05_hapax_datos.png", "46 de las 9,994 l&iacute;neas, tal cual salen del sistema. Nadie &laquo;ve&raquo; los datos: se resumen.")}
<p>Cada fila es una <strong>l&iacute;nea de venta</strong>: un producto dentro de un pedido
(un pedido junta 2 l&iacute;neas en promedio). Las columnas que usar&aacute;s con Mar&iacute;a:</p>
<table class="datos">
<tr><th>Columna</th><th>Qu&eacute; es</th></tr>
<tr><td><code>pedido_id</code></td><td>El pedido al que pertenece la l&iacute;nea</td></tr>
<tr><td><code>categoria &rarr; subcategoria &rarr; producto</code></td><td>Muebles, Suministros de Oficina o Tecnolog&iacute;a, y sus 17 subcategor&iacute;as</td></tr>
<tr><td><code>venta</code></td><td>Ingreso de la l&iacute;nea en USD, ya con descuento aplicado</td></tr>
<tr><td><code>descuento</code></td><td>Fracci&oacute;n descontada (0 = sin descuento, 0.7 = 70&nbsp;%)</td></tr>
<tr><td><code>utilidad</code></td><td>Ganancia de la l&iacute;nea en USD (negativa = p&eacute;rdida)</td></tr>
</table>
<p><strong>Ojo con esto:</strong> Mar&iacute;a pregunta por
<em>pedidos</em> y la tabla trae <em>l&iacute;neas</em>. Resumir la columna <code>venta</code> tal
cual responder&iacute;a otra pregunta. Habr&aacute; que agrupar l&iacute;neas en pedidos primero:
recuerda esto en la p&aacute;gina siguiente.</p>
<h2>Las cuatro preguntas del an&aacute;lisis descriptivo</h2>
<table class="datos">
<tr><th>La pregunta</th><th>Los estad&iacute;sticos</th><th>En pandas (mi&eacute;rcoles)</th></tr>
<tr><td>&iquest;Alrededor de qu&eacute; valor caen? (centro)</td><td>media &middot; mediana &middot; moda</td><td><code>.mean() .median() .mode()</code></td></tr>
<tr><td>&iquest;Qu&eacute; valor deja debajo al X&nbsp;%? (posici&oacute;n)</td><td>percentiles y cuartiles</td><td><code>.quantile(0.90)</code></td></tr>
<tr><td>&iquest;Qu&eacute; tan repartidos est&aacute;n? (dispersi&oacute;n)</td><td>desviaci&oacute;n est&aacute;ndar &middot; IQR &middot; coef. de variaci&oacute;n</td><td><code>.std()</code>, Q3&minus;Q1, std/media</td></tr>
<tr><td>&iquest;Cu&aacute;ntos hay de cada tipo? (frecuencia)</td><td>tablas de frecuencia</td><td><code>.value_counts()</code></td></tr>
</table>
<p>Con la muestra de esta p&aacute;gina ya viste algo m&aacute;s: hay una columna
<code>codigo_postal</code> perfectamente num&eacute;rica cuyo promedio es un n&uacute;mero
perfectamente absurdo. <strong>Que Python pueda calcularlo no lo vuelve un
estad&iacute;stico</strong>.</p>
<p><a class="boton" href="superstore_2026.csv" download="superstore_2026.csv">Descargar</a></p>
</div>
</div>
"""
pagina(2, "s05_p2_el_archivo.html", "9,994 filas y una gerente esperando un solo n&uacute;mero.",
       cuerpo2, css2)

# ══════════════════════════════ PÁGINA 3 · El pedido típico ════════════════════
MUESTRA = [("CA-2024-142454", 174), ("CA-2025-125794", 36), ("CA-2026-157987", 2256),
           ("CA-2023-121776", 125), ("CA-2025-163209", 49), ("US-2024-164238", 346),
           ("CA-2026-123351", 80), ("CA-2024-168956", 167), ("CA-2024-157343", 52)]
filas_muestra = "".join(f"<tr><td><code>{p}</code></td><td>${v:,}</td></tr>"
                        for p, v in MUESTRA)
inp3, lab3, fbs3, css3r = radios("q3", [
    ("q3a", "&asymp; 50&nbsp;%, m&aacute;s o menos la mitad.",
     "Es la intuici&oacute;n natural&hellip; y en tu muestra de 9 ya fall&oacute;: quedaron 7 de 9 "
     "debajo de la media. En los 5,009 reales pasa lo mismo, a lo grande. Mira el reveal.", "meh"),
    ("q3b", "&asymp; 60&nbsp;%.",
     "Vas en la direcci&oacute;n correcta, la realidad es a&uacute;n m&aacute;s torcida. "
     "En tu muestra de 9 quedaron 8 debajo (89En tu muestra de 9 quedaron 7 debajo (78&nbsp;%)nbsp;%). Mira lo que pasa con los 5,009.", "meh"),
    ("q3c", "&asymp; 72&nbsp;%: casi tres de cada cuatro.",
     "<strong>Exacto: 72.5&nbsp;%.</strong> Si lo intuiste por tu muestra (8 de 9 debajo), "
     "acabas de usar una muestra para calibrar el ojo. As&iacute; trabaja un analista.", "ok"),
])
css3 = css3r + """
/* En esta página el candado es doble: primero los dos números, luego el radio. */
.bloque3 > .apuesta-pct { display: none; }
.bloque3 > input.gate:checked ~ .reveal { display: none; }
.n1:not(:placeholder-shown) ~ .n2x:not(:placeholder-shown) ~ .pide-nums { display: none; }
.n1:not(:placeholder-shown) ~ .n2x:not(:placeholder-shown) ~ .apuesta-pct { display: block; }
.n1:not(:placeholder-shown) ~ .n2x:not(:placeholder-shown) ~ input.gate:checked ~ .reveal { display: block; }
"""
# La regla genérica de radios abriría el reveal con solo marcar un radio; la
# tercera línea la anula (misma especificidad, llega después) y la cadena final
# —más específica— exige números escritos Y radio marcado.
cuerpo3 = f"""
{chat("Mar&iacute;a &middot; 8h15",
      "<p>&iquest;Ya te lleg&oacute; el archivo? Dime: <strong>&iquest;cu&aacute;nto vale un pedido "
      "t&iacute;pico?</strong> Con eso fijo hoy mismo el umbral del env&iacute;o gratis.</p>")}
<p>Antes de soltarle un n&uacute;mero calculado sobre 5,009 pedidos, calibra el ojo con
<strong>9 pedidos reales</strong> del archivo (redondeados al d&oacute;lar). El de $2,256 existe de
verdad: una oficina amobl&aacute;ndose entera, con cinco sillas ejecutivas, mesa de conferencias y
tel&eacute;fonos.</p>
<table class="datos" style="max-width:380px;">
<tr><th>Pedido</th><th>Valor</th></tr>
{filas_muestra}
</table>
<div class="bloque bloque3">
<div class="apuesta">
<p>Calcula a mano &mdash;calculadora permitida&mdash; y escribe aqu&iacute;
<strong>la media</strong> de los 9 (suma todo y divide para 9):</p>
</div>
<input class="num n1" type="number" step="1" placeholder="$ tu media">
<div class="apuesta" style="border-top:none;">
<p><strong>La mediana</strong> de los 9 (ord&eacute;nalos y toma el quinto):</p>
</div>
<input class="num n2x" type="number" step="1" placeholder="$ tu mediana">
<div class="apuesta pide-nums" style="border-top:none;">
<div class="hint">Cuando tengas tus dos n&uacute;meros, seguimos.</div>
</div>
{inp3}
<div class="apuesta apuesta-pct" style="border-top:none;">
<p>En tu muestra la media sali&oacute; mucho m&aacute;s arriba que la mediana. Ahora, sobre los
<strong>5,009 pedidos reales</strong>: si calculamos el promedio de todos, &iquest;qu&eacute;
porcentaje de pedidos crees que queda <strong>por debajo del promedio</strong>?</p>
{lab3}{fbs3}
<div class="hint">Elige tu porcentaje y miramos los 5,009.</div>
</div>
<div class="reveal">
{ABIERTO}
<h2>Tu muestra ya conten&iacute;a la trampa</h2>
<p>Suma de los 9: <strong>$3,285</strong>. Media: 3,285 &divide; 9 = <strong>$365</strong>.
Ordenados (36, 49, 52, 80, <strong>125</strong>, 167, 174, 346, 2,256), la quinta posici&oacute;n es
la mediana: <strong>$125</strong>. &iquest;Te dieron esos? La media sali&oacute; <strong>casi el
triple</strong> de la mediana, y el culpable es un solo pedido: la oficina de $2,256. Ese pedido
arrastra la media hacia arriba; a la mediana ni la despeina, porque la mediana solo cuenta
<em>cu&aacute;ntos</em> quedan a cada lado, no <em>cu&aacute;nto pesan</em>.</p>
<h2>Y a escala completa, igual pero peor</h2>
<p>Los 5,009 pedidos: media <strong>$458.61</strong>, mediana <strong>$151.96</strong> (3 veces
menos), y <strong>el 72.5&nbsp;% de los pedidos vale menos que el promedio</strong>. El monstruo
mayor: el pedido <code>CA-2022-145317</code>, de $23,661, casi todo un equipo de videoconferencia
Cisco de $22,638.</p>
{img64("s05_hist_pedidos.png", "La forma m&aacute;s com&uacute;n del dinero: muchas transacciones chicas, pocas gigantes. Se llama distribuci&oacute;n de cola larga.")}
<p><strong>Tu detector de tres minutos:</strong> pide la media y la mediana. Si
coinciden, la distribuci&oacute;n es m&aacute;s o menos sim&eacute;trica y la media sirve. Si se
alejan &mdash;aqu&iacute; 3 a 1&mdash; hay cola larga o valores extremos, y el histograma decide.
En una distribuci&oacute;n sim&eacute;trica, bajo la media queda &asymp;50&nbsp;%; el 72.5&nbsp;%
es la alarma sonando.</p>
<h2>Los percentiles completan la historia</h2>
<table class="datos" style="max-width:420px;">
<tr><th>Percentil</th><th>Valor del pedido</th></tr>
<tr><td>p10</td><td>$13</td></tr><tr><td>p25</td><td>$38</td></tr>
<tr><td>p50 (mediana)</td><td>$152</td></tr><tr><td>p75</td><td>$512</td></tr>
<tr><td>p90</td><td>$1,154</td></tr><tr><td>p99</td><td>$4,209</td></tr>
<tr><td>m&aacute;ximo</td><td>$23,661</td></tr>
</table>
<div class="caja"><div class="rot">La decisi&oacute;n del umbral</div>
<p style="margin:0;">Un umbral de env&iacute;o gratis se fija <em>un poco por encima</em> del pedido
t&iacute;pico, para empujar el carrito. Si Mar&iacute;a ancla en el &laquo;promedio&raquo; de $459,
pone la meta donde el 72.5&nbsp;% de los pedidos ni llega: promoci&oacute;n muerta. Anclando en la
mediana ($152), un umbral de <strong>&asymp;$200</strong> (entre p50 y p75) deja a la mitad de los
pedidos a un empuj&oacute;n de distancia.</p></div>
{chat("T&uacute; &middot; 8h31", "<p>Mar&iacute;a: el pedido t&iacute;pico vale <strong>$152</strong>, "
      "no $459. El $459 es el promedio, y est&aacute; inflado por unos pocos pedidos gigantes: el "
      "72.5&nbsp;% de los pedidos queda por debajo de &eacute;l. Para el env&iacute;o gratis yo "
      "pondr&iacute;a el umbral cerca de <strong>$200</strong>: la mitad de tus pedidos queda a un "
      "paso de alcanzarlo.</p>", True)}
{chat("Mar&iacute;a &middot; 8h32",
      "<p>&iexcl;$200 me encanta! Qu&eacute; bueno que pregunt&eacute;&hellip; con $459 la "
      "promoci&oacute;n nac&iacute;a muerta. Oye, ya que est&aacute;s con el archivo abierto: "
      "<strong>otra cosita</strong> para el mismo comit&eacute;.</p>")}
<p>El mi&eacute;rcoles esto ser&aacute; una l&iacute;nea de Python:</p>
<pre class="code">pedidos = df.groupby("pedido_id")["venta"].sum()
pedidos.mean()     # 458.61  &larr; la media
pedidos.median()   # 151.96  &larr; la mediana
(pedidos &lt; pedidos.mean()).mean()   # 0.725</pre>
</div>
</div>
"""
pagina(3, "s05_p3_pedido_tipico.html",
       "Nueve pedidos, dos campos y tu primera trampa cazada.", cuerpo3, css3)

# ══════════════════════════════ PÁGINA 4 · El inventario ═══════════════════════
inp, lab, fbs, css4 = radios("q4", [
    ("q4a", "Suministros de Oficina: papel y carpetas se venden siempre.",
     "Eso dice <strong>la media</strong>: $20.33 contra $8.70, paliza de 2.3 a 1. Despu&eacute;s de "
     "la p&aacute;gina anterior, ya sabes que hay que preguntarle a la mediana antes de festejar.", "meh"),
    ("q4b", "Muebles: cada venta deja m&aacute;s margen.",
     "Eso dice <strong>la mediana</strong>: $7.77 contra $6.88. Interesante: acabas de apostar por "
     "el bando contrario al de la media. Uno de los dos &aacute;rbitros te enga&ntilde;a.", "meh"),
    ("q4c", "Depende de con qu&eacute; estad&iacute;stico se mida.",
     "<strong>Aprendiste r&aacute;pido.</strong> La respuesta se voltea seg&uacute;n el "
     "&aacute;rbitro: media dice Suministros, mediana dice Muebles. Ahora hay que entender "
     "<em>por qu&eacute;</em>, porque ah&iacute; vive la decisi&oacute;n.", "ok"),
])
cuerpo4 = f"""
{chat("Mar&iacute;a &middot; 8h40",
      "<p>El comit&eacute; tambi&eacute;n decide las <strong>compras del trimestre</strong>. Quiero "
      "duplicar el inventario de la categor&iacute;a m&aacute;s rentable por venta, y la pelea "
      "est&aacute; entre <strong>Muebles</strong> y <strong>Suministros de Oficina</strong>. "
      "&iquest;Cu&aacute;l? Un n&uacute;mero y ya.</p>")}
<p>&laquo;M&aacute;s rentable por venta&raquo; = m&aacute;s <code>utilidad</code> por l&iacute;nea
de venta. Otra pregunta descriptiva de una l&iacute;nea. Ya sabes que eso no la vuelve inocente.</p>
<div class="bloque">
{inp}
<div class="apuesta">
<p>&iquest;Qu&eacute; categor&iacute;a deja m&aacute;s utilidad por l&iacute;nea de venta?</p>
{lab}{fbs}
<div class="hint">Apuesta y te muestro el duelo.</div>
</div>
<div class="reveal">
{ABIERTO}
<h2>El duelo, con dos &aacute;rbitros</h2>
{img64("s05_categorias.png", "El mismo duelo con dos estad&iacute;sticos honestos y dos veredictos opuestos. Ninguno &laquo;miente&raquo;: miden cosas distintas.")}
<p>&iquest;Qui&eacute;n infla la media de Suministros de Oficina? Sus cinco l&iacute;neas m&aacute;s
rentables son <strong>encuadernadoras industriales</strong> de la subcategor&iacute;a Carpetas: una
GBC con $4,946 de utilidad, una Ibico con $4,630&hellip; Si quitas las 20 mejores l&iacute;neas
&mdash;el 0.3&nbsp;% de las 6,026&mdash; la media cae de $20.33 a <strong>$14.61</strong>. La
&laquo;superioridad&raquo; de toda la categor&iacute;a cuelga de un pu&ntilde;ado de ventas.</p>
<p><strong>La trampa: los extremos mandan sobre la media.</strong> Y es fractal:
dentro de Carpetas, media $19.84 contra mediana $3.98. El mismo patr&oacute;n, un piso m&aacute;s
abajo.</p>
<div class="caja"><div class="rot">La decisi&oacute;n del inventario</div>
<p style="margin:0;">&laquo;Duplicar Suministros de Oficina&raquo; por su media es duplicar papel,
sobres y material de arte esperando que rindan como encuadernadoras de $5,000. La pregunta correcta
no es qu&eacute; <em>categor&iacute;a</em> duplicar sino qu&eacute; <em>productos</em>.</p></div>
{chat("T&uacute; &middot; 9h02", "<p>Mar&iacute;a: por venta t&iacute;pica gana <strong>Muebles</strong> "
      "($7.77 contra $6.88). El promedio de Suministros ($20.33) lo inflan unas pocas encuadernadoras "
      "de casi $5,000. Yo no duplicar&iacute;a una categor&iacute;a entera: duplicar&iacute;a los "
      "<strong>productos</strong> que de verdad dejan margen. El mi&eacute;rcoles te paso ese top.</p>", True)}
{chat("Mar&iacute;a &middot; 9h04",
      "<p>O sea que casi lleno la bodega de papel y sobres pensando en encuadernadoras&hellip; "
      "Ok: productos, no categor&iacute;as. <strong>&Uacute;ltima y te dejo</strong>, esta es la "
      "inc&oacute;moda.</p>")}
<pre class="code">df.groupby("categoria")["utilidad"].agg(["mean", "median"])
df.nlargest(5, "utilidad")   # las encuadernadoras aparecen solas</pre>
</div>
</div>
"""
pagina(4, "s05_p4_inventario.html",
       "Duplicar inventario con el estad&iacute;stico equivocado sale caro.", cuerpo4, css4)

# ══════════════════════════════ PÁGINA 5 · El memo ═════════════════════════════
inp, lab, fbs, css5 = radios("q5", [
    ("q5a", "Firmo: la p&eacute;rdida total es real y la media lo confirma.",
     "Medio punto: las dos cifras son correctas y la p&eacute;rdida es real. Pero firmar sin mirar "
     "la distribuci&oacute;n es matar a un inocente por el crimen de unos pocos. Mira el reveal.", "meh"),
    ("q5b", "No firmo: apuesto a que la mediana de Libreros es positiva.",
     "Buen reflejo&hellip; y la mediana ES positiva (+$4.13). Pero cuidado: aun as&iacute; Libreros "
     "pierde $3,473 de verdad. Esta vez <em>la mediana tambi&eacute;n enga&ntilde;a</em>. Mira el "
     "reveal.", "meh"),
    ("q5c", "No firmo ni defiendo nada hasta ver la distribuci&oacute;n.",
     "<strong>Eso hace un analista.</strong> Ni la media ni la mediana bastan solas: la "
     "distribuci&oacute;n va a mostrar exactamente d&oacute;nde sangra Libreros.", "ok"),
])
cuerpo5 = f"""
{chat("Mar&iacute;a &middot; 9h15",
      "<p>Me lleg&oacute; esto de auditor&iacute;a y me piden confirmar <strong>hoy</strong>. "
      "T&uacute; ya viste los datos: &iquest;firmo?</p>")}
<div class="memoq">&laquo;La subcategor&iacute;a <strong>Libreros</strong> acumul&oacute; una
p&eacute;rdida neta de $3,473 en cuatro a&ntilde;os, con una utilidad media de
<strong>&minus;$15.23</strong> por l&iacute;nea. Recomendaci&oacute;n: descontinuarla.&raquo;
<div style="font-style:normal; font-size:12px; color:#6b6b6b; margin-top:8px;">Memo de
auditor&iacute;a &middot; cifras verificadas: las dos son correctas.</div></div>
<div class="bloque">
{inp}
<div class="apuesta">
<p>Las dos cifras del memo son correctas. &iquest;Firmas?</p>
{lab}{fbs}
<div class="hint">Decide tu firma y miramos la distribuci&oacute;n.</div>
</div>
<div class="reveal">
{ABIERTO}
<h2>La trampa inversa</h2>
<p>La venta t&iacute;pica de Libreros <strong>gana</strong> plata: mediana <strong>+$4.13</strong>.
Y la subcategor&iacute;a entera <strong>pierde</strong> $3,473, con media &minus;$15.23. Todo es
verdad al mismo tiempo. En las p&aacute;ginas anteriores la mentirosa era la media y la mediana
rescataba; aqu&iacute; la mediana es la que tranquiliza de m&aacute;s, porque <strong>ignora los
tama&ntilde;os</strong>: solo cuenta cu&aacute;ntas ventas ganan, no cu&aacute;nto pierden las que
pierden.</p>
{img64("s05_libreros.png", "228 l&iacute;neas de venta: 34 pierden m&aacute;s de $100 cada una y entre todas se comen $9,506, casi el triple de la p&eacute;rdida total.")}
<h2>&iquest;Y qu&eacute; tienen en com&uacute;n las 34?</h2>
<p>Pregunta descriptiva &rarr; respuesta diagn&oacute;stica. Utilidad media por l&iacute;nea
seg&uacute;n el descuento aplicado:</p>
<table class="datos" style="max-width:460px;">
<tr><th>Descuento</th><th>L&iacute;neas</th><th>Utilidad media</th></tr>
<tr><td>0&nbsp;%</td><td>60</td><td><strong>+$101.3</strong></td></tr>
<tr><td>15&nbsp;%</td><td>52</td><td>+$27.3</td></tr>
<tr><td>20&nbsp;%</td><td>46</td><td>+$2.8</td></tr>
<tr><td>30&ndash;32&nbsp;%</td><td>37</td><td>&minus;$55.6 a &minus;$88.6</td></tr>
<tr><td>50&nbsp;%</td><td>18</td><td><strong>&minus;$236.4</strong></td></tr>
<tr><td>70&nbsp;%</td><td>15</td><td><strong>&minus;$259.7</strong></td></tr>
</table>
<p>Sin descuento, Libreros es un buen negocio. Con 50&ndash;70&nbsp;% de descuento,
cada venta pierde m&aacute;s de $200. El problema no es el mueble: <strong>es la pol&iacute;tica de
descuentos</strong>. Y f&iacute;jate lo que acaba de pasar: para defender a Libreros preguntaste
<em>por qu&eacute;</em> pierde. Acabas de subir al escal&oacute;n 2 de la escalera &mdash;sin pedir
permiso. As&iacute; se sube: no por ambici&oacute;n, por necesidad.</p>
{chat("T&uacute; &middot; 9h38", "<p>Mar&iacute;a: <strong>no firmes</strong>. Las cifras del memo son "
      "correctas pero la conclusi&oacute;n no: la venta t&iacute;pica de Libreros gana $4; la "
      "p&eacute;rdida viene de 34 ventas con descuentos del 50&ndash;70&nbsp;% que se comen $9,506. "
      "Sin descuento, Libreros deja +$101 por venta. El memo correcto dice: <em>revisar qui&eacute;n "
      "autoriza descuentos del 50&nbsp;% en Libreros</em>.</p>", True)}
{chat("Mar&iacute;a &middot; 9h52",
      "<p>&iexcl;Me salvaste tres veces en una ma&ntilde;ana! Entro al comit&eacute; a las 10h00: "
      "m&aacute;ndame el resumen final en tres l&iacute;neas, uno por pregunta. Sin jerga, que ah&iacute; "
      "nadie sabe qu&eacute; es una mediana.</p>")}
<pre class="code">lib = df[df["subcategoria"] == "Libreros"]["utilidad"]
lib.median(), lib.mean(), lib.sum()   # +4.13, -15.23, -3,473
df[df["subcategoria"] == "Libreros"].groupby("descuento")["utilidad"].mean()</pre>
</div>
</div>
"""
pagina(5, "s05_p5_memo_auditoria.html",
       "Las dos cifras son correctas. La conclusi&oacute;n, no.", cuerpo5, css5)

# ══════════════════════════════ PÁGINA 6 · El comité ═══════════════════════════
inp, lab, fbs, css6 = radios("q6", [
    ("q6a", "Consumidor: son la mayor&iacute;a, ah&iacute; est&aacute; la plata.",
     "Son el 52&nbsp;% de los pedidos (dato &uacute;til para otra decisi&oacute;n), pero ni su media "
     "($449) ni su mediana ($155) lideran. Mira la tabla.", "meh"),
    ("q6b", "Corporativo: empresas compran m&aacute;s por pedido.",
     "<strong>Correcto por mediana</strong>: $158.3, el pedido t&iacute;pico m&aacute;s alto de los "
     "tres. La media dice otra cosa&hellip; a estas alturas ya sabes a cu&aacute;l creerle y por "
     "qu&eacute;.", "ok"),
    ("q6c", "Oficina en casa: el teletrabajo dispara los pedidos.",
     "Eso dice <strong>la media</strong> ($472.7, la m&aacute;s alta)&hellip; y por mediana es el "
     "<strong>&uacute;ltimo</strong> ($142.3). La trampa del promedio, una vez m&aacute;s: pocos "
     "pedidos gigantes de home office inflan su media.", "meh"),
])
cuerpo6 = f"""
{chat("Mar&iacute;a &middot; 9h45",
      "<p>Antes de entrar: marketing pregunta a qu&eacute; <strong>segmento</strong> apuntar la "
      "campa&ntilde;a del env&iacute;o gratis: &iquest;Consumidor, Corporativo u Oficina en casa? "
      "Quieren el que tenga el <strong>pedido t&iacute;pico m&aacute;s alto</strong>.</p>")}
<div class="bloque">
{inp}
<div class="apuesta">
<p>&iquest;Qu&eacute; segmento tiene el pedido t&iacute;pico m&aacute;s alto?</p>
{lab}{fbs}
<div class="hint">Apuesta y cerramos la ma&ntilde;ana.</div>
</div>
<div class="reveal">
{ABIERTO}
<h2>El marcador del segmento</h2>
<table class="datos" style="max-width:520px;">
<tr><th>Segmento</th><th>Pedidos</th><th>Media</th><th>Mediana</th></tr>
<tr><td>Consumidor</td><td>2,586</td><td>$449.1</td><td>$154.7</td></tr>
<tr><td>Corporativo</td><td>1,514</td><td>$466.4</td><td><strong>$158.3</strong></td></tr>
<tr><td>Oficina en casa</td><td>909</td><td><strong>$472.7</strong></td><td>$142.3</td></tr>
</table>
<p>La media corona a Oficina en casa; la mediana lo manda al &uacute;ltimo lugar. Cuatro veces en
una ma&ntilde;ana, la misma lecci&oacute;n. Y un bonus para la pr&oacute;xima pelea: las 5,196
l&iacute;neas vendidas <em>con descuento</em> tienen media <strong>&minus;$6.66</strong> (pierden) y
mediana <strong>+$3.34</strong> (ganan). Dos poblaciones mezcladas en una sola distribuci&oacute;n:
lo ver&aacute;s como histograma bimodal el mi&eacute;rcoles.</p>
<h2>El marcador de la ma&ntilde;ana</h2>
<table class="datos">
<tr><th>Pregunta de Mar&iacute;a</th><th>Dec&iacute;a la media</th><th>Dec&iacute;a la mediana</th><th>Qui&eacute;n enga&ntilde;aba</th></tr>
<tr><td>Umbral de env&iacute;o gratis</td><td>$459</td><td>$152</td><td>La media (cola larga)</td></tr>
<tr><td>Inventario: &iquest;qu&eacute; categor&iacute;a?</td><td>Suministros</td><td>Muebles</td><td>La media (extremos)</td></tr>
<tr><td>&iquest;Eliminar Libreros?</td><td>&minus;$15.23 &rarr; s&iacute;</td><td>+$4.13 &rarr; no</td><td>La mediana (ignora tama&ntilde;os)</td></tr>
</table>
<div class="caja"><div class="rot">La regla de la casa</div>
<p style="margin:0; font-size:17px;"><strong>Ning&uacute;n promedio sin su
distribuci&oacute;n.</strong> Media para distribuciones sim&eacute;tricas sin extremos; mediana
cuando hay colas o extremos; moda para categor&iacute;as; y ninguna de las tres sin haber visto el
histograma. Quien reporta un centro sin mirar la distribuci&oacute;n no est&aacute; resumiendo:
est&aacute; adivinando.</p></div>
<h2>Tu memo de las 10h00</h2>
<p>Escribe el mensaje final para Mar&iacute;a en <strong>m&aacute;ximo tres l&iacute;neas, un
n&uacute;mero por pregunta, cada uno con su advertencia</strong>, en idioma de comit&eacute;
(&laquo;el pedido t&iacute;pico&raquo;, &laquo;la mitad de los pedidos&raquo;, nada de
&laquo;mediana&raquo;). Gu&aacute;rdalo bien: va a ser la <strong>primera diapositiva</strong> de
tu reporte &mdash;el encargo completo est&aacute; en el siguiente tema. Esta caja no guarda tu
texto, as&iacute; que c&oacute;pialo a un lado.</p>
<textarea style="width:100%; min-height:120px; border:2px solid #D6D6D6; border-radius:3px;
padding:12px; font-family:inherit; font-size:14px;"
placeholder="Para: Maria - Asunto: Tus tres numeros para el comite&#10;1. ...&#10;2. ...&#10;3. ..."></textarea>
<h2>Para seguir</h2>
<p><strong>El mi&eacute;rcoles</strong>: perfilado descriptivo contra reloj sobre Comercial Andina,
con <code>describe</code>, <code>quantile</code> y <code>value_counts</code>. Hoy fue el criterio;
el mi&eacute;rcoles, la velocidad. Trae la laptop.</p>
<p><strong>Para tu equipo</strong>: corran la pregunta 1 de Mar&iacute;a sobre el dataset de su
caso: &iquest;la media y la mediana de su variable de dinero cuentan la misma historia? Traigan el
histograma.</p>
<p style="margin-bottom:6px;"><strong>Opcional</strong>, el mismo caso paso a paso en Python:</p>
<p><a class="boton sec" href="{COLAB}" target="_blank" rel="noopener">Abrir el cuaderno en Colab</a></p>
<h2>Si quieres m&aacute;s</h2>
<p style="margin-bottom:8px;"><strong><a href="https://es.khanacademy.org/math/probability/data-distributions-a1" target="_blank" rel="noopener" style="color:#A6192E;">Khan Academy &middot; Distribuciones de datos</a></strong> &mdash; media, mediana, percentiles e histogramas, con ejercicios, en espa&ntilde;ol.</p>
<p style="margin-bottom:8px;"><strong><a href="https://es.wikipedia.org/wiki/Cuarteto_de_Anscombe" target="_blank" rel="noopener" style="color:#A6192E;">El cuarteto de Anscombe</a></strong> &mdash; cuatro datasets con estad&iacute;sticos id&eacute;nticos y gr&aacute;ficos radicalmente distintos.</p>
<p><strong>Darrell Huff &middot; <em>C&oacute;mo mentir con estad&iacute;stica</em></strong> &mdash; el cap&iacute;tulo del &laquo;promedio bien escogido&raquo; es esta ma&ntilde;ana con corbata de 1954.</p>
</div>
</div>
"""
pagina(6, "s05_p6_el_comite.html",
       "Tres trampas cazadas, un memo por escribir.", cuerpo6, css6)


# ══════════════════════════════ PÁGINA 7 · El encargo ══════════════════════════
cuerpo7 = f"""
{chat("Mar&iacute;a &middot; 11h20",
      "<p>&iexcl;Sali&oacute; redondo! El comit&eacute; aprob&oacute; el umbral de $200 y fren&oacute; "
      "lo de Libreros. Y ahora los otros gerentes regionales quieren lo suyo: el VP me pidi&oacute; un "
      "<strong>reporte corto en PowerPoint</strong> para reenviar el lunes. Cinco diapositivas, no "
      "m&aacute;s. Elige <strong>una regi&oacute;n</strong> &mdash;Oeste, Este, Centro o Sur&mdash; y "
      "cu&eacute;ntame si tu detector tambi&eacute;n encuentra la trampa ah&iacute;.</p>")}
<p>Tu primer entregable como analista. Corto y al grano: <strong>cinco diapositivas</strong>, ni una
m&aacute;s.</p>
<table class="datos">
<tr><th style="width:36px;">1</th><td><strong>Tu memo del comit&eacute;</strong> &mdash; las tres
respuestas de la ma&ntilde;ana: un n&uacute;mero y su advertencia por pregunta, en idioma de gerente
(el que escribiste en la p&aacute;gina anterior).</td></tr>
<tr><th>2</th><td><strong>Tu regi&oacute;n, tus n&uacute;meros</strong> &mdash; para la regi&oacute;n
que elegiste: cu&aacute;ntos pedidos tiene, su media, su mediana y el porcentaje de pedidos por
debajo de la media. Calculados por ti.</td></tr>
<tr><th>3</th><td><strong>Tu histograma</strong> &mdash; el valor del pedido en esa regi&oacute;n,
con la media y la mediana marcadas como dos l&iacute;neas verticales. Hecho por ti, no el del
taller.</td></tr>
<tr><th>4</th><td><strong>Tu veredicto</strong> &mdash; &iquest;el promedio tambi&eacute;n miente en
tu regi&oacute;n? &iquest;Qu&eacute; umbral de env&iacute;o gratis le pondr&iacute;as y por
qu&eacute;?</td></tr>
<tr><th>5</th><td><strong>La pregunta que dejas abierta</strong> &mdash; un &laquo;&iquest;por
qu&eacute;...?&raquo; de escal&oacute;n 2 que valdr&iacute;a la pena investigar despu&eacute;s.</td></tr>
</table>
<div class="caja"><div class="rot">La &uacute;nica parte t&eacute;cnica</div>
<p style="margin:0;">La pregunta es por <em>pedidos</em> y el archivo trae <em>l&iacute;neas</em>
(son m&aacute;s de 800 pedidos por regi&oacute;n: con calculadora no se puede). En Excel o Google
Sheets: tabla din&aacute;mica con filas <code>pedido_id</code>, valores suma de <code>venta</code> y
filtro <code>region</code>; sobre esa columna usa PROMEDIO, MEDIANA y
CONTAR.SI(rango;"&lt;"&amp;promedio), y arma el gr&aacute;fico de histograma. En el cuaderno opcional
de Colab es una l&iacute;nea: <code>df[df.region == "Oeste"].groupby("pedido_id")["venta"].sum()</code>.</p></div>
<p>&iquest;Asistente de IA? Bienvenido: pega en la &uacute;ltima diapositiva el prompt que usaste y
qu&eacute; verificaste de lo que te devolvi&oacute;. Aqu&iacute; se califica el encargo y la
verificaci&oacute;n, no el tecleo.</p>
<p style="margin-bottom:6px;">&iquest;No tienes el archivo a la mano?</p>
<p><a class="boton" href="superstore_2026.csv" download="superstore_2026.csv">Descargar</a></p>
<h2>C&oacute;mo se califica (sobre 10)</h2>
<table class="datos" style="max-width:520px;">
<tr><td>N&uacute;meros correctos y verificables</td><td style="width:60px;"><strong>3</strong></td></tr>
<tr><td>Histograma propio, legible, con las dos l&iacute;neas</td><td><strong>3</strong></td></tr>
<tr><td>Veredicto en idioma de Mar&iacute;a</td><td><strong>2</strong></td></tr>
<tr><td>La pregunta de escal&oacute;n 2</td><td><strong>1</strong></td></tr>
<tr><td>Cinco diapositivas justas y prolijas</td><td><strong>1</strong></td></tr>
</table>
<div class="caja"><div class="rot">Entrega</div>
<p style="margin:0;">Individual. Archivo <code>s05_reporte_apellido.pptx</code> (PowerPoint o Google
Slides exportado) al buz&oacute;n <strong>Taller 5 &middot; Reporte para Mar&iacute;a</strong>, antes
de la clase del mi&eacute;rcoles.</p></div>
<p>Mar&iacute;a cuenta contigo. Nos vemos el mi&eacute;rcoles.</p>
"""
pagina(7, "s05_p7_encargo_maria.html",
       "Cinco diapositivas para el VP: tu primer entregable.", cuerpo7)

print("Listo: sube los 7 archivos a Brightspace como temas del m&oacute;dulo, en orden."
      .encode("ascii", "xmlcharrefreplace").decode())
