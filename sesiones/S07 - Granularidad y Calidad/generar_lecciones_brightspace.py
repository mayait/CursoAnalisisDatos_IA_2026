#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera las páginas D2L de las sesiones 7 y 8 (semana 4, ADM 2003).

Serie s07 (lunes): Anatomía y calidad de los datos — 4 páginas.
Serie s08 (miércoles): Inventario de problemas de calidad — 3 páginas.

Mismo patrón que S05: HTML autocontenido, fondo blanco, candados en CSS puro
(el estudiante apuesta ANTES de ver gráfica y teoría), imágenes en base64,
todo carácter no ASCII como entidad. Se suben como ARCHIVOS a D2L.
"""
import base64
import json
import shutil
from pathlib import Path

AQUI = Path(__file__).resolve().parent
SALIDA = AQUI / "brightspace"
SALIDA.mkdir(exist_ok=True)
K = json.loads((AQUI / "clave.json").read_text(encoding="utf-8"))
# Nombre sin underscores de cara al estudiante
shutil.copy(AQUI / "andina_market.csv", SALIDA / "andina-market.csv")

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

/* El candado (CSS puro) */
.bloque { margin: 20px 0; }
.bloque > input.gate { position: absolute; left: -9999px; }
.bloque > input.num { display: block; width: 200px; padding: 10px 12px; margin: 6px 0 14px 0;
  border: 2px solid #D6D6D6; border-radius: 3px; font-size: 16px; font-weight: bold;
  color: #1e1e1e; background: #ffffff; }
.bloque > input.num:focus { border-color: #A6192E; outline: none; }
.bloque > input.num:not(:placeholder-shown) ~ .reveal { display: block; }
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

SERIES = {
    "s07": {"kicker": "Semana 4 &middot; Sesi&oacute;n 7",
            "titulo": "Anatom&iacute;a y calidad de los datos",
            "sub": "Granularidad, tipos de dato y lo que un vac&iacute;o puede significar",
            "archivo": "lunes-granularidad-y-calidad.html",
            "pasos": ["El correo de auditor&iacute;a", "La fila y el pedido",
                      "Cero no es vac&iacute;o", "El encargo"],
            "cierre": "Eso es todo por hoy. El mi&eacute;rcoles seguimos con el inventario completo."},
    "s08": {"kicker": "Semana 4 &middot; Sesi&oacute;n 8",
            "titulo": "Inventario de problemas de calidad",
            "sub": "dtypes, isna, duplicated &mdash; y el Deber 2",
            "archivo": "miercoles-inventario-y-deber2.html",
            "pasos": ["El inventario", "Las decisiones", "El Deber 2"],
            "cierre": "Eso es todo. Tu bit&aacute;cora va al buz&oacute;n de D2L."},
}
_secciones = {"s07": [], "s08": []}
_css_extra = {"s07": "", "s08": ""}

CSS_SECCION = """
.indice { background: #F7F7F7; border: 1px solid #D6D6D6; padding: 14px 18px; margin: 0 0 8px 0; }
.indice .rot { font-size: 12px; font-weight: bold; letter-spacing: 1.5px;
  text-transform: uppercase; color: #a6192e; margin-bottom: 6px; }
.indice a { display: block; color: #1e1e1e; text-decoration: none; padding: 3px 0; }
.indice a:hover { color: #A6192E; }
.indice .num { color: #A6192E; font-weight: bold; }
.seccion { border-top: 2px solid #A6192E; margin-top: 34px; padding-top: 6px; }
.seccion .pasonum { font-size: 12px; font-weight: bold; letter-spacing: 1.5px;
  text-transform: uppercase; color: #a6192e; margin-top: 10px; }
.seccion h1 { font-size: 22px; margin: 4px 0 16px 0; }
.subir { font-size: 12px; margin-top: 8px; }
.subir a { color: #6b6b6b; text-decoration: none; }
.subir a:hover { color: #A6192E; }
"""


def pagina(serie, n, archivo, sub, cuerpo, extra_css=""):
    """Acumula la sección n de la serie (se compacta todo en un archivo por sesión)."""
    _secciones[serie].append((n, sub, cuerpo))
    _css_extra[serie] += extra_css


def emitir(serie):
    S = SERIES[serie]
    indice = "".join(
        f'<a href="#paso{n}"><span class="num">{n}.</span> {S["pasos"][n-1]} &mdash; {sub}</a>'
        for n, sub, _ in _secciones[serie])
    cuerpo = f'<div class="indice"><div class="rot">En esta p&aacute;gina</div>{indice}</div>'
    for n, sub, c in _secciones[serie]:
        cuerpo += (f'<div class="seccion" id="paso{n}">'
                   f'<div class="pasonum">Paso {n} de {len(S["pasos"])}</div>'
                   f'<h1>{S["pasos"][n-1]} &mdash; {sub}</h1></div>{c}'
                   f'<div class="subir"><a href="#top">&uarr; volver al &iacute;ndice</a></div>')
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{S['titulo']} &middot; ADM 2003</title>
<style>{CSS}{CSS_SECCION}{_css_extra[serie]}</style>
</head>
<body>
<div class="cont" id="top">
<div class="top">
<div class="kicker">{S['kicker']}</div>
<div class="titulo">{S['titulo']}</div>
<div class="sub">{S['sub']}</div>
</div>
<div class="cuerpo">
{cuerpo}
<div class="footer"><div class="sig">{S['cierre']}</div></div>
</div>
</div>
</body>
</html>"""
    final = html.encode("ascii", "xmlcharrefreplace").decode("ascii")
    (SALIDA / S["archivo"]).write_text(final, encoding="ascii")
    print(f"{S['archivo']}: {len(final)/1024:.0f} KB · {len(_secciones[serie])} pasos")


def img64(nombre, pie):
    dato = base64.b64encode((AQUI / "img" / nombre).read_bytes()).decode()
    return (f'<div class="figura"><img src="data:image/png;base64,{dato}" alt="{pie}">'
            f'<div class="pie">{pie}</div></div>')


def chat(quien, texto, mia=False):
    return (f'<div class="chat{" mia" if mia else ""}"><div class="quien">{quien}</div>'
            f'{texto}</div>')


def radios(name, opciones):
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


def bloque_radio(rot, pregunta, inputs, labels, fbs):
    return f"""<div class="bloque">
{inputs}
<div class="apuesta"><div class="rot">{rot}</div>
<p>{pregunta}</p>
{labels}{fbs}
<div class="hint">Elige una opci&oacute;n y seguimos.</div>
</div>"""


def bloque_num(rot, pregunta, placeholder="Escribe tu apuesta"):
    return f"""<div class="bloque">
<div class="apuesta"><div class="rot">{rot}</div>
<p>{pregunta}</p>
</div>
<input class="num" type="number" step="any" placeholder="{placeholder}">"""


SC = K["sin_cliente"]
PR = SC["por_region_pct"]
FILAS = K["filas"]

# ══════════════════════════════ S07 · P1 ══════════════════════════════
i1, l1, f1, c1 = radios("q1", [
    ("q1a", "El cliente no existe: son ventas falsas.",
     "Es la hip&oacute;tesis m&aacute;s grave y la menos probable. No saltes a fraude sin haber descartado las explicaciones aburridas: casi siempre gana el proceso, no el crimen.", "meh"),
    ("q1b", "Es venta de mostrador: consumidor final que no se registra.",
     "Muy plausible en retail. Pero f&iacute;jate en lo que acabas de hacer: convertiste un vac&iacute;o en un hecho. Sigue siendo una hip&oacute;tesis hasta que alguien del negocio la confirme.", "meh"),
    ("q1c", "Alguien olvid&oacute; digitarlo en el sistema.",
     "Tambi&eacute;n plausible. Pregunta inc&oacute;moda: &iquest;c&oacute;mo distinguir&iacute;as ese olvido de una venta de mostrador leg&iacute;tima mirando solo la tabla? Exacto: no puedes.", "meh"),
    ("q1d", "Todav&iacute;a no se puede saber: hay que preguntar c&oacute;mo se captura ese campo.",
     "Esa es la respuesta profesional. Un vac&iacute;o no se interpreta: se investiga. La tabla no trae la respuesta; el proceso que la genera, s&iacute;.", "ok"),
])
cuerpo = (
    chat("Mar&iacute;a &middot; gerente regional", "<p>El comit&eacute; aprob&oacute; el an&aacute;lisis del promedio. Ahora tengo otro problema: auditor&iacute;a revis&oacute; la base de nuestra filial ecuatoriana, <b>Andina Market</b>, y me mand&oacute; esto. Necesito una explicaci&oacute;n antes del viernes.</p>", True)
    + '<div class="memoq">De las '
    + f'{FILAS:,}'.replace(",", ".")
    + f' l&iacute;neas de venta del &uacute;ltimo a&ntilde;o, <b>{SC["total"]} ({SC["pct"]}%) no tienen identificador de cliente</b>. Solicitamos confirmar si se trata de un error del sistema o de una pr&aacute;ctica de registro. &mdash; Auditor&iacute;a interna</div>'
    + "<p>Hoy trabajamos la pregunta que est&aacute; antes de cualquier limpieza: <b>&iquest;qu&eacute; significa un vac&iacute;o?</b> No es un tecnicismo. De la respuesta depende si esas 120 l&iacute;neas se borran, se rellenan o se convierten en un hallazgo del negocio.</p>"
    + bloque_radio("Tu apuesta", "Sin mirar nada m&aacute;s: &iquest;qu&eacute; significa que <b>ID Cliente</b> est&eacute; vac&iacute;o en una l&iacute;nea de venta?", i1, l1, f1)
    + '<div class="reveal">'
    + '<div class="divisor">Lo que dicen los datos</div>'
    + img64("fig1_sin_cliente_region.png",
            f"Porcentaje de l&iacute;neas sin cliente por regi&oacute;n. Costa: {PR['Costa']}%. Sierra: {PR['Sierra']}%. Gal&aacute;pagos: {PR['Gal&aacute;pagos']}%.".replace("Gal&aacute;pagos'", "Galápagos'") if False else
            f"Porcentaje de l&iacute;neas sin cliente por regi&oacute;n.")
    + f"<p>El vac&iacute;o <b>no cae parejo</b>: en la Costa falta el {PR['Costa']}% de los clientes; en Gal&aacute;pagos, el {PR['Galápagos']}%. Cuando un faltante se concentra en una regi&oacute;n, un canal o un turno, deja de ser ruido y se vuelve una pista: hay un <i>proceso</i> distinto captur&aacute;ndolo &mdash;quiz&aacute; cajas de mostrador que no piden c&eacute;dula frente a facturaci&oacute;n corporativa que s&iacute;.</p>"
    + '<div class="divisor">Teor&iacute;a &middot; los tres significados de un hueco</div>'
    + '<table class="datos"><tr><th>Caso</th><th>Qu&eacute; es</th><th>Ejemplo en Andina Market</th></tr>'
      '<tr><td><b>Ausente</b></td><td>El valor existe en el mundo, pero nadie lo captur&oacute;.</td><td>La provincia de un pedido despachado: el pedido lleg&oacute; a alguna parte.</td></tr>'
      '<tr><td><b>Cero</b></td><td>El valor es exactamente cero. Es un dato, no un hueco.</td><td>Descuento = 0: hubo venta y no hubo rebaja.</td></tr>'
      '<tr><td><b>Desconocido</b></td><td>Ni siquiera sabemos si existe un valor.</td><td>ID Cliente vac&iacute;o: &iquest;venta an&oacute;nima o registro perdido? A&uacute;n no se sabe.</td></tr></table>'
    + '<div class="caja"><div class="rot">La regla de la sesi&oacute;n</div>Un dato faltante es un mensaje sobre el proceso que lo genera. Antes de imputar o borrar, pregunta <b>c&oacute;mo</b> se captura el campo y <b>d&oacute;nde</b> se concentra el hueco.</div>'
    + "</div></div>")
pagina("s07", 1, "s07_p1_el_correo.html",
       "Lo que un vac&iacute;o puede significar", cuerpo, c1)

# ══════════════════════════════ S07 · P2 ══════════════════════════════
PE = K["pedido_ejemplo"]
cuerpo = (
    "<p>Antes de contar huecos hay que saber qu&eacute; est&aacute;s contando. Abre los ojos con esta tabla: son las l&iacute;neas del pedido <b>AM-2026-0042</b> tal como vienen en la base de Andina Market.</p>"
    + '<table class="datos"><tr><th>ID Pedido</th><th>Producto</th><th>Cantidad</th><th>Ventas</th><th>Total Pedido</th></tr>'
      '<tr><td>AM-2026-0042</td><td>Resma papel A4 75g</td><td>2</td><td>74.90</td><td>187.40</td></tr>'
      '<tr><td>AM-2026-0042</td><td>Cuaderno universitario Norma</td><td>3</td><td>52.30</td><td>187.40</td></tr>'
      '<tr><td>AM-2026-0042</td><td>Mouse Logitech M170</td><td>2</td><td>41.20</td><td>187.40</td></tr>'
      '<tr><td>AM-2026-0042</td><td>Cinta adhesiva Scotch x6</td><td>1</td><td>19.00</td><td>187.40</td></tr></table>'
    + bloque_num("Tu apuesta", "&iquest;De cu&aacute;ntos d&oacute;lares fue el pedido AM-2026-0042? Escribe solo el n&uacute;mero.")
    + '<div class="reveal">'
    + f'<p>El pedido fue de <b>${PE["total"]:.2f}</b>: la suma de la columna <b>Ventas</b> de sus cuatro l&iacute;neas. Si tu instinto fue sumar &quot;Total Pedido&quot; (${PE["suma_total_pedido_mal"]:.2f}), acabas de cuadruplicar la venta: esa columna repite el total del pedido <i>en cada l&iacute;nea</i>.</p>'
    + '<div class="divisor">La trampa a escala de toda la empresa</div>'
    + img64("fig2_doble_conteo.png", "La misma base, dos totales: la columna equivocada infla la venta 3.8x.")
    + f'<p>Sumar &quot;Total Pedido&quot; sobre las {FILAS:,} l&iacute;neas da <b>${K["suma_total_pedido_doble"]:,.0f}</b>. La venta real del a&ntilde;o es <b>${K["suma_ventas_real"]:,.0f}</b>. Nadie invent&oacute; un n&uacute;mero: solo se sum&oacute; una columna que vive en otra <b>granularidad</b>.</p>'.replace(",", "&#8239;")
    + '<div class="divisor">Teor&iacute;a &middot; granularidad</div>'
    + '<p>La <b>granularidad</b> es lo que representa una fila. En esta base, una fila = <b>una l&iacute;nea de pedido</b> (un producto dentro de un pedido). Sobre esa misma tabla conviven tres niveles de pregunta:</p>'
    + '<table class="datos"><tr><th>Nivel</th><th>Pregunta t&iacute;pica</th><th>C&oacute;mo se llega</th></tr>'
      '<tr><td>L&iacute;nea</td><td>&iquest;Qu&eacute; producto se vendi&oacute; m&aacute;s?</td><td>La tabla tal cual</td></tr>'
      '<tr><td>Pedido</td><td>&iquest;Cu&aacute;nto vale el pedido t&iacute;pico?</td><td><code>groupby(&quot;ID Pedido&quot;)</code></td></tr>'
      '<tr><td>Cliente</td><td>&iquest;Cu&aacute;nto gasta un cliente al a&ntilde;o?</td><td><code>groupby(&quot;ID Cliente&quot;)</code></td></tr></table>'
    + '<div class="caja"><div class="rot">Las dos preguntas de rigor ante una tabla nueva</div>Primera: <b>&iquest;qu&eacute; es una fila?</b> Segunda: <b>&iquest;qu&eacute; columnas pertenecen a otra granularidad?</b> Las columnas repetidas (como &quot;Total Pedido&quot;) no se suman: se usan con <code>drop_duplicates(&quot;ID Pedido&quot;)</code> o se recalculan.</div>'
    + "</div></div>")
pagina("s07", 2, "s07_p2_la_fila_y_el_pedido.html",
       "Granularidad: qu&eacute; representa exactamente una fila", cuerpo)

# ══════════════════════════════ S07 · P3 ══════════════════════════════
DC = K["descuento_cero"]; DN = K["descuento_nan"]
i3, l3, f3, c3 = radios("q3", [
    ("q3a", f"{DC} l&iacute;neas: las que tienen descuento igual a 0.",
     f"Solo si el vac&iacute;o NO significa &quot;sin descuento&quot;. &iquest;Y si las cajas de mostrador dejan el campo en blanco justamente cuando no aplican rebaja? Entonces ser&iacute;an {DC + DN}.", "meh"),
    ("q3b", f"{DC + DN} l&iacute;neas: los ceros m&aacute;s los vac&iacute;os.",
     f"Solo si el vac&iacute;o SIEMPRE significa &quot;sin descuento&quot;. &iquest;Y si a veces significa &quot;no se registr&oacute;&quot;? Entonces ser&iacute;an {DC}. No lo sabes todav&iacute;a.", "meh"),
    ("q3c", f"Entre {DC} y {DC + DN}: depende de qu&eacute; significa el vac&iacute;o, y eso se pregunta, no se adivina.",
     "Exacto. El rango es lo honesto mientras no conozcas la regla de captura. Y fija el tama&ntilde;o del problema: la respuesta puede moverse en 212 l&iacute;neas.", "ok"),
])
cuerpo = (
    f"<p>En Andina Market, la columna <b>Descuento</b> tiene {DC} l&iacute;neas con valor 0 y {DN} l&iacute;neas vac&iacute;as.</p>"
    + bloque_radio("Tu apuesta", "&iquest;Cu&aacute;ntas l&iacute;neas <b>no tuvieron</b> descuento?", i3, l3, f3)
    + '<div class="reveal">'
    + img64("fig3_descuento_cero_nan.png", "Tres estados distintos que se parecen demasiado cuando alguien los promedia sin mirar.")
    + '<div class="divisor">El tercer impostor: el centinela</div>'
    + f'<p>Hay huecos que ni siquiera parecen huecos. En esta base, {K["utilidad_centinela"]} l&iacute;neas tienen <b>Utilidad = -9999</b>: alg&uacute;n sistema viejo usaba ese n&uacute;mero para decir &quot;desconocido&quot;. Si lo promedias sin darte cuenta, arrastra la utilidad media de toda una regi&oacute;n. <code>isna()</code> jam&aacute;s lo va a encontrar: para pandas, -9999 es un n&uacute;mero perfectamente v&aacute;lido.</p>'
    + '<div class="divisor">Y los tipos tampoco son lo que parecen</div>'
    + "<p>El tercer frente de esta sesi&oacute;n son los <b>tipos de dato</b>. En esta base:</p>"
    + f'<table class="datos"><tr><th>Columna</th><th>Lo que esperas</th><th>Lo que hay</th><th>S&iacute;ntoma</th></tr>'
      f'<tr><td>Fecha Pedido</td><td>datetime</td><td>texto (object)</td><td>{K["fechas_ddmm"]} filas vienen como <code>dd/mm/yyyy</code> y el resto como <code>yyyy-mm-dd</code></td></tr>'
      f'<tr><td>Ventas</td><td>float</td><td>texto (object)</td><td>{K["ventas_texto"]} filas traen formato de factura: <code>$1.234,56</code></td></tr>'
      f'<tr><td>Cantidad</td><td>entero positivo</td><td>int64</td><td>{K["cantidad_negativa"]} filas negativas: &iquest;devoluciones o error?</td></tr></table>'
    + '<pre class="code">df.dtypes          # el primer vistazo honesto\ndf[&quot;Ventas&quot;].sum() # TypeError: no puedes sumar texto\n                   # una sola celda con &quot;$&quot; vuelve object TODA la columna</pre>'
    + '<div class="caja"><div class="rot">La regla de la sesi&oacute;n</div>Antes de describir, revisa <code>dtypes</code>. Si una fecha o una venta aparecen como <code>object</code>, todo c&aacute;lculo posterior hereda el error &mdash;o revienta, que es mejor, porque al menos lo ves.</div>'
    + "</div></div>")
pagina("s07", 3, "s07_p3_cero_no_es_vacio.html",
       "Cero, vac&iacute;o y centinela: los tres impostores", cuerpo, c3)

# ══════════════════════════════ S07 · P4 ══════════════════════════════
i4, l4, f4, c4 = radios("q4", [
    ("q4a", "Los duplicados: filas repetidas inflan todo.",
     "Importan, pero hay un problema anterior: si los tipos est&aacute;n rotos, hasta el conteo de duplicados puede enga&ntilde;arte. Ve primero a <code>dtypes</code>.", "meh"),
    ("q4b", "Los tipos de dato: dtypes antes que nada.",
     "Ese es el orden profesional. Un <code>isna()</code> sobre una columna que deber&iacute;a ser num&eacute;rica y es texto te miente; primero endereza los tipos, despu&eacute;s cuenta.", "ok"),
    ("q4c", "Los nulos: isna() de arriba a abajo.",
     "Los nulos son el plato fuerte, pero <code>isna()</code> sobre columnas con tipos rotos (o con centinelas como -9999) cuenta mal. Los tipos van primero.", "meh"),
])
cuerpo = (
    chat("Mar&iacute;a", "<p>Ya entend&iacute; que el vac&iacute;o es una pregunta y no un dato. Ahora necesito lo concreto: <b>el viernes quiero un inventario de calidad</b> de la base de Andina Market. Cada problema, cu&aacute;ntas filas afecta, y qu&eacute; decides hacer con &eacute;l.</p>", True)
    + '<div class="divisor">La base</div>'
    + f'<table class="datos"><tr><th>Archivo</th><td>andina-market.csv</td></tr>'
      f'<tr><th>Filas</th><td>{str(FILAS)[0]}.{str(FILAS)[1:]} l&iacute;neas de pedido &middot; sep-2025 a ago-2026</td></tr>'
      f'<tr><th>Una fila es</th><td>un producto dentro de un pedido (ya sabes por qu&eacute; importa)</td></tr>'
      f'<tr><th>Columnas</th><td>{K["columnas"]}: pedido, fechas, cliente, ubicaci&oacute;n, producto, montos</td></tr></table>'
    + '<p><a class="boton" href="andina-market.csv" download>Descargar</a></p>'
    + "<p>&Aacute;brela hoy con lo m&iacute;nimo &mdash;cinco comandos, en este orden:</p>"
    + '<pre class="code">import pandas as pd\ndf = pd.read_csv(&quot;andina-market.csv&quot;)\n\ndf.head()      # &iquest;qu&eacute; es una fila?\ndf.info()      # tipos y no-nulos de un vistazo\ndf.dtypes      # &iquest;qu&eacute; columnas mienten sobre su tipo?\ndf.isna().sum()        # huecos declarados\ndf.duplicated().sum()  # filas repetidas (&iquest;seguro?)</pre>'
    + bloque_radio("&Uacute;ltima apuesta del d&iacute;a", "De todo lo que viste hoy, &iquest;qu&eacute; revisas <b>primero</b> el mi&eacute;rcoles?", i4, l4, f4)
    + '<div class="reveal">'
    + '<div class="divisor">El plan de ataque del mi&eacute;rcoles</div>'
    + '<table class="datos"><tr><th>Orden</th><th>Frente</th><th>Herramienta</th></tr>'
      '<tr><td>1</td><td>Tipos que mienten</td><td><code>dtypes</code>, <code>astype</code>, <code>to_datetime</code></td></tr>'
      '<tr><td>2</td><td>Huecos declarados y disfrazados</td><td><code>isna</code>, <code>isin</code>, centinelas</td></tr>'
      '<tr><td>3</td><td>Duplicados</td><td><code>duplicated</code> (con una sorpresa)</td></tr>'
      '<tr><td>4</td><td>Valores imposibles</td><td>cantidades negativas, env&iacute;os que viajan al pasado</td></tr></table>'
    + '<p>De ese inventario sale el <b>Deber 2: la bit&aacute;cora de limpieza</b>. Y recuerda que este mi&eacute;rcoles tambi&eacute;n se entrega la <b>propuesta de proyecto final</b> de tu grupo.</p>'
    + "</div></div>")
pagina("s07", 4, "s07_p4_el_encargo.html",
       "Descarga la base y arma el primer vistazo", cuerpo, c4)

# ══════════════════════════════ S08 · P1 ══════════════════════════════
cuerpo = (
    "<p>El lunes dejamos la base abierta y un encargo: el inventario de calidad para Mar&iacute;a. Hoy lo construimos completo. Empieza por cargar y mirar tipos:</p>"
    + '<pre class="code">import pandas as pd\ndf = pd.read_csv(&quot;andina-market.csv&quot;)\ndf.dtypes</pre>'
    + bloque_num("Apuesta 1 &middot; duplicados", "&iquest;Cu&aacute;ntas filas repetidas exactas crees que hay en la base? Escribe tu n&uacute;mero.")
    + '<div class="reveal">'
    + f'<p>Hay <b>{K["duplicados_exactos"]}</b>. Pero si corriste <code>df.duplicated().sum()</code> te dio <b>0</b>, y esa es la sorpresa de hoy:</p>'
    + '<pre class="code">df.duplicated().sum()\n# 0  &larr; miente\n\ndf.drop(columns=[&quot;ID Fila&quot;]).duplicated().sum()\n# 24  &larr; la verdad</pre>'
    + '<p>La columna <b>ID Fila</b> es un consecutivo que el sistema le puso a cada registro <i>despu&eacute;s</i> de duplicarse: hace que dos filas id&eacute;nticas parezcan distintas. Para buscar duplicados reales, primero quita los identificadores autom&aacute;ticos.</p>'
    + "</div></div>"
    + bloque_num("Apuesta 2 &middot; los sin-cliente",
                 f"<code>df[&quot;ID Cliente&quot;].isna().sum()</code> devuelve <b>{SC['nan']}</b>. Auditor&iacute;a dijo que eran {SC['total']}. &iquest;Cu&aacute;ntas l&iacute;neas SIN cliente encuentras t&uacute;? Escribe tu n&uacute;mero.")
    + '<div class="reveal">'
    + f'<p>Las {SC["total"]} de auditor&iacute;a est&aacute;n bien contadas. <code>isna()</code> solo ve los {SC["nan"]} vac&iacute;os <i>declarados</i> (NaN). Los otros se esconden en dos disfraces: {SC["vacio"]} cadenas vac&iacute;as <code>&quot;&quot;</code> y {SC["sin_id"]} con el texto <code>&quot;SIN-ID&quot;</code>.</p>'
    + '<pre class="code">mask = (df[&quot;ID Cliente&quot;].isna()\n        | df[&quot;ID Cliente&quot;].isin([&quot;&quot;, &quot;SIN-ID&quot;]))\nmask.sum()\n# 120</pre>'
    + '<div class="caja"><div class="rot">Regla</div><code>isna()</code> encuentra los huecos que el sistema declara. Los huecos que la gente inventa (&quot;&quot;, &quot;SIN-ID&quot;, &quot;N/A&quot;, -9999) se cazan con <code>value_counts()</code> y <code>isin()</code>. Siempre corre <code>value_counts(dropna=False)</code> sobre una columna sospechosa.</div>'
    + '<div class="divisor">El inventario completo</div>'
    + img64("fig4_inventario.png", "Los nueve problemas de andina-market.csv, contados. Este es el mapa del Deber 2.")
    + '<p>Cada barra es una fila de tu bit&aacute;cora. En la siguiente p&aacute;gina decidimos qu&eacute; hacer con cada una &mdash;porque contar no es limpiar.</p>'
    + "</div></div>")
pagina("s08", 1, "s08_p1_el_inventario.html",
       "dtypes, isna, duplicated y las trampas de cada uno", cuerpo)

# ══════════════════════════════ S08 · P2 ══════════════════════════════
i5, l5, f5, c5 = radios("q5", [
    ("q5a", "Borrarlas: 9 filas en 1.335 no mueven nada.",
     "Mueven poco en el total y mucho en la confianza: si son devoluciones reales, borrarlas infla la venta neta. Primero entiende, despu&eacute;s decide.", "meh"),
    ("q5b", "Ponerles valor absoluto: seguro fue un signo mal digitado.",
     "Acabas de convertir 9 posibles devoluciones en 9 ventas. Es la correcci&oacute;n m&aacute;s peligrosa: cambia el negocio sin evidencia.", "meh"),
    ("q5c", "Preguntar al negocio si son devoluciones y documentar la respuesta.",
     "Correcto. La cantidad negativa es un cl&aacute;sico &quot;dato imposible que en realidad es un proceso sin documentar&quot;. La bit&aacute;cora registra la pregunta y la respuesta.", "ok"),
    ("q5d", "Dejarlas como est&aacute;n: los datos no se tocan.",
     "No tocarlas sin documentarlas tampoco es neutral: cualquier suma de cantidades ya las est&aacute; restando. La decisi&oacute;n honesta se escribe, sea cual sea.", "meh"),
])
cuerpo = (
    "<p>Contar problemas es la mitad f&aacute;cil. La otra mitad es decidir, y toda decisi&oacute;n cambia una cifra del negocio. Cuatro verbos posibles por problema:</p>"
    + '<table class="datos"><tr><th>Verbo</th><th>Cu&aacute;ndo</th><th>Ejemplo aqu&iacute;</th></tr>'
      '<tr><td><b>Corregir</b></td><td>La regla es conocida y reversible</td><td>Unificar <code>QUITO / quito / &#8239;Quito</code> con <code>str.strip().str.title()</code></td></tr>'
      '<tr><td><b>Excluir</b></td><td>La fila no puede ser verdad y no hay forma de repararla</td><td>Env&iacute;os anteriores al pedido (6 filas), si log&iacute;stica no explica</td></tr>'
      '<tr><td><b>Imputar</b></td><td>Hay valor razonable y documentas el criterio</td><td>Provincia vac&iacute;a (32): se deduce de la ciudad</td></tr>'
      '<tr><td><b>Documentar</b></td><td>Siempre. Las otras tres sin esta no valen</td><td>Toda la bit&aacute;cora</td></tr></table>'
    + bloque_radio("Tu apuesta", f"{K['cantidad_negativa']} filas tienen <b>Cantidad negativa</b>. &iquest;Qu&eacute; haces?", i5, l5, f5)
    + '<div class="reveal">'
    + '<div class="divisor">Dos limpiezas resueltas, para que veas el formato</div>'
    + '<pre class="code"># Ventas: de &quot;$1.234,56&quot; (texto) a 1234.56 (float)\ndf[&quot;Ventas&quot;] = (df[&quot;Ventas&quot;].astype(str)\n    .str.replace(&quot;$&quot;, &quot;&quot;, regex=False)\n    .str.replace(&quot;.&quot;, &quot;&quot;, regex=False)   # miles\n    .str.replace(&quot;,&quot;, &quot;.&quot;, regex=False)   # decimal\n    .astype(float))\n\n# Fechas: dos formatos mezclados en una columna\ndf[&quot;Fecha Pedido&quot;] = pd.to_datetime(\n    df[&quot;Fecha Pedido&quot;], format=&quot;mixed&quot;, dayfirst=True)</pre>'
    + '<p>Cada bloque as&iacute; genera una fila de bit&aacute;cora: qu&eacute; hab&iacute;a, cu&aacute;ntas filas, qu&eacute; hiciste, por qu&eacute;, y la evidencia de que qued&oacute; bien (<code>df[&quot;Ventas&quot;].dtype</code> ahora es <code>float64</code>).</p>'
    + '<div class="caja"><div class="rot">Por qu&eacute; importa m&aacute;s que la limpieza misma</div>La semana que viene construyes la tabla de indicadores del Deber 3 sobre esta misma base. Si tu bit&aacute;cora no dice qu&eacute; filas exclu&iacute;ste, tu total no va a cuadrar con el de nadie &mdash;ni con el tuyo de la semana pasada.</div>'
    + "</div></div>")
pagina("s08", 2, "s08_p2_las_decisiones.html",
       "Corregir, excluir, imputar &mdash;y documentarlo todo", cuerpo, c5)

# ══════════════════════════════ S08 · P3 ══════════════════════════════
cuerpo = (
    "<p>El Deber 2 es tu inventario convertido en documento profesional: la <b>bit&aacute;cora de limpieza</b> de <code>andina-market.csv</code>. Es individual y se entrega en el buz&oacute;n <b>Deber 2</b> de D2L (la fecha exacta est&aacute; en el buz&oacute;n).</p>"
    + '<div class="divisor">Qu&eacute; entregas</div>'
    + '<p>Una p&aacute;gina (PDF o el propio cuaderno) con una tabla de <b>al menos 6 problemas</b>, uno por fila:</p>'
    + '<table class="datos"><tr><th>Columna de tu bit&aacute;cora</th><th>Qu&eacute; va ah&iacute;</th></tr>'
      '<tr><td>Problema</td><td>Nombre claro: &quot;Ventas almacenadas como texto&quot;</td></tr>'
      '<tr><td>Filas afectadas</td><td>El n&uacute;mero exacto, contado con c&oacute;digo</td></tr>'
      '<tr><td>Evidencia</td><td>La l&iacute;nea de pandas que lo demuestra</td></tr>'
      '<tr><td>Decisi&oacute;n</td><td>Corregir / excluir / imputar / documentar &mdash;y el c&oacute;digo si aplica</td></tr>'
      '<tr><td>Justificaci&oacute;n</td><td>Una frase en t&eacute;rminos del negocio, no de pandas</td></tr></table>'
    + '<p>Cierra con <b>tres l&iacute;neas de resumen</b>: filas iniciales, filas finales, y qu&eacute; cifra del negocio cambi&oacute; con tu limpieza (la venta total es la m&aacute;s obvia).</p>'
    + '<div class="divisor">R&uacute;brica &middot; 10 puntos</div>'
    + '<table class="datos"><tr><th>Criterio</th><th>Puntos</th></tr>'
      '<tr><td>Detecci&oacute;n: encuentra al menos 6 problemas reales (hay m&aacute;s de 9)</td><td>3</td></tr>'
      '<tr><td>Evidencia reproducible: cada conteo tiene su c&oacute;digo</td><td>2.5</td></tr>'
      '<tr><td>Decisi&oacute;n y justificaci&oacute;n de negocio por problema</td><td>3</td></tr>'
      '<tr><td>Claridad de la bit&aacute;cora y resumen final</td><td>1.5</td></tr></table>'
    + '<div class="caja"><div class="rot">Mismo buz&oacute;n, segunda entrega</div>Tu grupo tambi&eacute;n sube esta semana la <b>propuesta de proyecto final</b>: medio p&aacute;rrafo con el dataset elegido, la pregunta de negocio y la decisi&oacute;n que habilita. Formato libre; lo discutimos en clase la pr&oacute;xima semana.</div>'
    + '<p><a class="boton" href="andina-market.csv" download>Descargar la base</a> <a class="boton sec" href="#paso1">Volver al inventario</a></p>')
pagina("s08", 3, "s08_p3_deber2.html",
       "Bit&aacute;cora de limpieza &middot; individual", cuerpo)

emitir("s07")
emitir("s08")
print("Listo: 2 lecciones + andina-market.csv en brightspace/")
