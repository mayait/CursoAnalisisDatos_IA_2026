# -*- coding: utf-8 -*-
"""Genera las paginas D2L del bloque de IA (semanas 6 y 7) y del proyecto de medio semestre.

Uso: python generar_paginas_d2l.py  -> escribe los HTML en ./d2l/
Convenciones: un HTML autocontenido por tema, fondo blanco, rojo USFQ, sin JS,
caracteres no ASCII como entidades, descargas con href relativo y atributo download.
"""
import os, re, html

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "d2l")
os.makedirs(OUT, exist_ok=True)

CSS = """
*{box-sizing:border-box}
body{margin:0;background:#fff;color:#1e1e1e;font-family:'Segoe UI',system-ui,-apple-system,Arial,sans-serif;font-size:16px;line-height:1.6}
.cab{background:#111;color:#fff;border-bottom:5px solid #A6192E;padding:22px 20px 18px}
.cab .serie{font-size:13px;letter-spacing:.04em;color:#e8b4bc;margin:0 0 4px}
.cab h1{margin:0;font-size:26px;line-height:1.25;font-weight:600}
.cab .sub{margin:6px 0 0;color:#d6d6d6;font-size:15px}
main{max-width:760px;margin:0 auto;padding:8px 20px 40px}
h2{color:#A6192E;font-size:21px;margin:38px 0 10px;padding-top:6px;border-top:1px solid #eee}
h3{font-size:17px;margin:22px 0 6px}
a{color:#A6192E}
.indice{background:#faf6f7;border:1px solid #efdfe2;border-radius:6px;padding:12px 18px;margin:20px 0}
.indice p{margin:0 0 6px;font-weight:600}
.indice ol{margin:0;padding-left:20px}
.volver{font-size:13px;margin:14px 0 0}
.nota{border:1px solid #e3e3e3;border-radius:6px;padding:12px 16px;margin:16px 0;background:#fcfcfc}
.nota b{color:#A6192E}
.prompt{background:#f7f7f7;border:1px solid #e1e1e1;border-radius:6px;padding:12px 14px;margin:10px 0 14px;font-family:Consolas,'Courier New',monospace;font-size:14px;white-space:pre-wrap;line-height:1.5}
.prompt-t{font-size:13px;color:#6b6b6b;margin:14px 0 -4px}
table{border-collapse:collapse;width:100%;margin:12px 0;font-size:15px}
th,td{border:1px solid #e1e1e1;padding:7px 10px;text-align:left;vertical-align:top}
th{background:#f4f4f4}
.arbol{background:#f7f7f7;border:1px solid #e1e1e1;border-radius:6px;padding:12px 14px;font-family:Consolas,'Courier New',monospace;font-size:14px;white-space:pre;overflow-x:auto;line-height:1.5}
.btn{display:inline-block;background:#A6192E;color:#fff !important;text-decoration:none;padding:7px 14px;border-radius:4px;font-size:14px;margin:4px 6px 4px 0}
.etapa{border:1px solid #e3e3e3;border-left:0;border-radius:6px;padding:4px 18px 12px;margin:18px 0}
.etapa h3{color:#A6192E}
.check{list-style:none;padding-left:0}
.check li{padding-left:26px;position:relative;margin:4px 0}
.check li:before{content:'';position:absolute;left:2px;top:6px;width:13px;height:13px;border:2px solid #A6192E;border-radius:2px}
.apuesta{border:1px solid #efdfe2;border-radius:6px;padding:12px 16px;margin:18px 0}
.apuesta input{position:absolute;opacity:0}
.apuesta label{display:block;border:1px solid #ddd;border-radius:4px;padding:7px 10px;margin:6px 0;cursor:pointer}
.apuesta input:checked + label{border-color:#A6192E;background:#faf6f7}
.fb{display:none;margin-top:10px;padding:10px 12px;background:#f7f7f7;border-radius:4px}
#a1:checked ~ .fb1,#a2:checked ~ .fb2,#a3:checked ~ .fb3{display:block}
#b1:checked ~ .fb1,#b2:checked ~ .fb2,#b3:checked ~ .fb3{display:block}
.correo{border:1px solid #d9d9d9;border-radius:6px;margin:10px 0 18px;background:#fff}
.cab-correo{margin:0;border:0;font-size:14px;background:#f7f7f7}
.cab-correo td{border:0;border-bottom:1px solid #eee;padding:5px 12px}
.cab-correo .ck{width:90px;color:#6b6b6b}
.cuerpo-correo{padding:6px 16px 4px;font-size:15px}
.paso{margin:10px 0}
.paso p{margin:0 0 4px}
ol.control{padding-left:22px}
ol.control li{margin:0 0 18px}
ol.control .q{font-weight:600;margin:0 0 6px}
details{border:1px solid #e3e3e3;border-radius:4px;margin:6px 0;padding:0 12px}
details summary{cursor:pointer;padding:7px 0;color:#A6192E;font-size:14px}
details[open]{padding-bottom:10px}
.cifra{background:#faf6f7;border-left:0;padding:8px 12px;border-radius:4px}
.trampa p{margin:6px 0}
.mc .op{position:relative;margin:6px 0}
.mc input{position:absolute;opacity:0}
.mc label{display:block;border:1px solid #ddd;border-radius:4px;padding:8px 12px;cursor:pointer;background:#fff}
.mc label:hover{border-color:#A6192E}
.mc input:checked + label{border-color:#A6192E;background:#faf6f7;font-weight:600}
.mc input:focus-visible + label{outline:2px solid #A6192E}
.mc .fb{display:none;margin:6px 0 10px;padding:10px 12px;border-radius:4px}
.mc input:checked + label + .fb{display:block}
.mc .ok{background:#eef6ef;border:1px solid #cfe3d2}
.mc .mal{background:#fbf1f2;border:1px solid #efd3d7}
.foto{margin:14px 0}
.foto img{width:100%;height:auto;border-radius:6px;display:block}
.lamina{display:flex;gap:18px;align-items:flex-start;flex-wrap:wrap;margin:10px 0}
.lamina .wire{max-width:100%;height:auto;flex:0 0 auto}
.lamina div{flex:1 1 220px}
.critico{border:2px solid #A6192E;border-radius:6px;padding:12px 18px;margin:12px 0;background:#fff}
.critico .q{font-size:19px;font-weight:700;color:#A6192E;margin:4px 0 8px}
.pie{max-width:760px;margin:0 auto;padding:18px 20px 40px;border-top:1px solid #eee;font-size:14px;color:#6b6b6b}
@media (max-width:600px){.cab h1{font-size:22px}}
"""


def pagina(titulo, serie, sub, secciones, siguiente):
    idx = "".join(f'<li><a href="#s{i}">{t}</a></li>' for i, (t, _) in enumerate(secciones, 1))
    cuerpo = "".join(
        f'<section id="s{i}"><h2>{t}</h2>{c}<p class="volver"><a href="#indice">&uarr; Volver al &iacute;ndice</a></p></section>'
        for i, (t, c) in enumerate(secciones, 1))
    doc = f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo} · USFQ</title><style>{CSS}</style></head>
<body><header class="cab"><p class="serie">{serie}</p><h1>{titulo}</h1><p class="sub">{sub}</p></header>
<main><nav class="indice" id="indice"><p>En esta p&aacute;gina</p><ol>{idx}</ol></nav>{cuerpo}</main>
<footer class="pie">{siguiente}</footer></body></html>"""
    # no ASCII -> entidades (las ya escritas como entidad se respetan)
    return doc.encode("ascii", "xmlcharrefreplace").decode("ascii")


def P(t):
    return f'<div class="prompt">{html.escape(t.strip())}</div>'


def PT(titulo, t):
    return f'<p class="prompt-t">{titulo}</p>' + P(t)


def arbol(t):
    return f'<div class="arbol">{html.escape(t.strip(chr(10)))}</div>'


SERIE = "ADM 2003 · An&aacute;lisis de Datos · Semanas 6 y 7 · Analizar datos con IA"

# ---------------------------------------------------------------- 1. MARCO DE TRABAJO
marco = [
("Una carpeta por encargo", """
<p>Antigravity no trabaja sobre un chat, trabaja sobre una carpeta. Todo lo que el agente puede leer y todo lo que produce vive ah&iacute;. Por eso cada encargo empieza igual: se crea una carpeta, se abre completa en Antigravity (<i>File &gt; Open Folder</i>) y no se trabaja fuera de ella.</p>
<p>Si el grupo trabaja junto, la carpeta es la que se comparte. Lo que no est&aacute; en la carpeta no existe para el agente, y lo que el agente no dej&oacute; en la carpeta no se hizo.</p>
"""),
("Las seis carpetas", """
<p>Todos los trabajos del curso usan la misma estructura. As&iacute; cualquier persona del grupo, o el profesor, sabe d&oacute;nde buscar cada cosa.</p>
""" + arbol("""
mi-encargo/
  AGENTS.md          reglas que Antigravity lee al empezar
  entradas/          lo que se pide: correos, enunciados, preguntas
  datos/             archivos originales; nunca se modifican
  contexto/          CONTEXTO.md y PLAN.md
  procesamiento/     scripts y bases intermedias
  salidas/           lo que se entrega
  archivo/           versiones viejas; nada se borra
""") + """
<table><tr><th>Carpeta</th><th>Regla</th></tr>
<tr><td>entradas</td><td>Se lee. Es la pregunta del cliente con sus palabras.</td></tr>
<tr><td>datos</td><td>Se lee y nunca se toca. Si hay que limpiar, la versi&oacute;n limpia va a procesamiento.</td></tr>
<tr><td>contexto</td><td>Se escribe una vez y se actualiza al cerrar cada etapa.</td></tr>
<tr><td>procesamiento</td><td>Lo que el agente necesita para llegar al resultado: scripts, tablas intermedias.</td></tr>
<tr><td>salidas</td><td>Solo entregables. Si no lo mostrar&iacute;as al cliente, no va aqu&iacute;.</td></tr>
<tr><td>archivo</td><td>Lo que se reemplaz&oacute;, con la fecha en el nombre.</td></tr></table>
"""),
("El contexto se escribe una vez", """
<p>El chat se olvida. El archivo <b>contexto/CONTEXTO.md</b> no. Ah&iacute; va qui&eacute;n pide, qu&eacute; pregunta, la fecha de corte, las reglas del caso y cada decisi&oacute;n que se tom&oacute; con su raz&oacute;n. Cuando abres una conversaci&oacute;n nueva, el agente lo lee y sigue donde qued&oacute;.</p>
<p>El archivo <b>AGENTS.md</b>, en la ra&iacute;z de la carpeta, tiene las reglas de trabajo. Antigravity lo carga solo al empezar. Los ZIP del curso ya lo traen.</p>
""" + PT("Prompt para crear o completar el contexto", """
Lee entradas/ y contexto/CONTEXTO.md. Completa CONTEXTO.md con quién pide, qué pregunta, la fecha de corte y las reglas que salen del correo. No inventes nada que no esté en los archivos; si falta un dato, déjalo marcado como pendiente.
""")),
("Revisar los archivos antes de pedir nada", """
<p>El primer pedido nunca es &laquo;hazlo&raquo;. Es &laquo;dime qu&eacute; hay&raquo;. Cada archivo viene de un sistema distinto, con sus columnas, sus fechas y sus filas que sobran. Si el agente cruza sin mirar, el error aparece tres etapas despu&eacute;s y nadie sabe de d&oacute;nde vino.</p>
""" + PT("Prompt de reconocimiento", """
Revisa todo lo que hay en datos/. Para cada archivo dime qué sistema parece haberlo producido, en qué fila empieza la tabla, qué columnas trae, cuál es la llave para cruzarlo y en qué formato vienen las fechas. No escribas código todavía.
""")),
("Primero el plan, despu&eacute;s la ejecuci&oacute;n", """
<p>Usa el modo <b>Planning</b> de Antigravity. El agente escribe un plan antes de tocar nada: qu&eacute; archivo une con cu&aacute;l, por qu&eacute; campo y qu&eacute; va a dejar en salidas. El grupo lo lee, lo corrige con comentarios y solo entonces lo aprueba.</p>
""" + PT("Prompt de plan", """
Antes de ejecutar, escribe en contexto/PLAN.md el plan de esta etapa: qué archivos vas a leer, qué vas a unir con qué y por qué campo, qué decisiones de limpieza propones y qué archivo vas a dejar en salidas/. Espera mi visto bueno.
""") + """
<div class="nota"><b>Si la revisi&oacute;n falla, se corrige el encargo.</b> No basta con arreglar el archivo: se ajusta el plan o el contexto para que el error no vuelva en la siguiente etapa.</div>
"""),
("Cada etapa deja una salida parcial", """
<p>Un encargo grande se parte en etapas. Cada etapa termina con un archivo en <b>salidas/</b> que el grupo abre y revisa: una base, una tabla de conteos, una respuesta corta al cliente. El mensaje de &laquo;terminado&raquo; del agente es el inicio de la revisi&oacute;n, no el final.</p>
<ul class="check">
<li>Abrir el archivo de salida, no leer el resumen del chat.</li>
<li>Pedir las cifras de control: cu&aacute;ntas filas ley&oacute;, cu&aacute;ntas dej&oacute; fuera y por qu&eacute;.</li>
<li>Rastrear tres casos a mano en los archivos originales.</li>
<li>Anotar en CONTEXTO.md las decisiones y las cifras de la etapa.</li>
</ul>
""" + PT("Prompt de revisi&oacute;n", """
¿Cuántas filas leíste de cada archivo, cuántas descartaste y por qué? Dame tres casos con todos sus datos y el archivo del que sale cada uno para verificarlos a mano. Después actualiza contexto/CONTEXTO.md con las decisiones y las cifras de esta etapa.
""") + """
<div class="apuesta"><p><b>Antigravity te dice &laquo;Listo, encontr&eacute; 4.327 veh&iacute;culos&raquo;. &iquest;Qu&eacute; haces?</b></p>
<input type="radio" name="a" id="a1"><label for="a1">Copio la cifra en la respuesta al cliente.</label>
<input type="radio" name="a" id="a2"><label for="a2">Abro el archivo en salidas, pido cu&aacute;ntas filas ley&oacute; y descart&oacute;, y rastreo tres casos.</label>
<input type="radio" name="a" id="a3"><label for="a3">Le pregunto al agente si est&aacute; seguro.</label>
<div class="fb fb1">La cifra puede cuadrar y estar mal. Sin revisar la salida no sabes si cont&oacute; dos veces el mismo veh&iacute;culo.</div>
<div class="fb fb2">Eso. La revisi&oacute;n se hace sobre el archivo y sobre los originales, no sobre el resumen del chat.</div>
<div class="fb fb3">El agente casi siempre va a decir que s&iacute;. La seguridad no es evidencia.</div></div>
"""),
("El ciclo completo, en una tabla", """
<table><tr><th>Paso</th><th>Qu&eacute; haces</th><th>Qu&eacute; queda en la carpeta</th></tr>
<tr><td>1. Ordenar</td><td>Crear la carpeta con las seis subcarpetas y abrirla en Antigravity.</td><td>La estructura y AGENTS.md</td></tr>
<tr><td>2. Contexto</td><td>Pedir que lea entradas y complete el contexto.</td><td>contexto/CONTEXTO.md</td></tr>
<tr><td>3. Reconocer</td><td>Pedir el inventario de datos sin c&oacute;digo.</td><td>Nada nuevo, solo lectura</td></tr>
<tr><td>4. Planificar</td><td>Pedir el plan en modo Planning y aprobarlo.</td><td>contexto/PLAN.md</td></tr>
<tr><td>5. Ejecutar</td><td>Dejar que el agente trabaje.</td><td>procesamiento/ y salidas/</td></tr>
<tr><td>6. Revisar</td><td>Cifras de control y tres casos a mano.</td><td>CONTEXTO.md actualizado</td></tr></table>
"""),
]
open(os.path.join(OUT, "marco-de-trabajo-antigravity.html"), "w").write(pagina(
    "C&oacute;mo se trabaja con Antigravity", SERIE,
    "La carpeta, el contexto, el plan y las salidas parciales", marco,
    "Ve al siguiente tema &rarr; Caso Carolina"))

# ---------------------------------------------------------------- 2. CASO CAROLINA
Z = lambda f, t: f'<a class="btn" href="{f}" download>{t}</a>'


def etapa(n, titulo, pide, prompts, salida, revisar):
    ps = "".join(PT(a, b) for a, b in prompts)
    rv = "".join(f"<li>{r}</li>" for r in revisar)
    return (f'<div class="etapa"><h3>Etapa {n} &middot; {titulo}</h3>'
            f'<p><b>Qu&eacute; pide Carolina.</b> {pide}</p>{ps}'
            f'<p><b>Salida parcial en salidas/.</b> {salida}</p>'
            f'<p><b>Antes de pasar a la siguiente etapa</b></p><ul class="check">{rv}</ul></div>')


CORREOS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "correos")


def correo(n):
    """Muestra el correo tal cual llega, con sus encabezados."""
    t = open(os.path.join(CORREOS_DIR, f"correo-{n}.md"), encoding="utf-8").read().strip()
    lineas = t.split("\n")
    cab, cuerpo = [], []
    for l in lineas:
        if l.startswith("**") and not cuerpo:
            k, _, v = l.partition(":**")
            cab.append(f'<tr><td class="ck">{html.escape(k.strip("*"))}</td><td>{html.escape(v.strip())}</td></tr>')
        else:
            cuerpo.append(l)
    parrafos = [p.strip() for p in "\n".join(cuerpo).split("\n\n") if p.strip()]
    ps = "".join(f"<p>{html.escape(p).replace(chr(10), '<br>')}</p>" for p in parrafos)
    return f'<div class="correo"><table class="cab-correo">{"".join(cab)}</table><div class="cuerpo-correo">{ps}</div></div>'


def pasos(lista):
    """lista de (texto, prompt o None)."""
    out = []
    for i, (t, p) in enumerate(lista, 1):
        out.append(f'<div class="paso"><p><b>Paso {i}.</b> {t}</p>{P(p) if p else ""}</div>')
    return "".join(out)


def control(items):
    """items: (pregunta, cifra esperada, engaño, prompt de revisión)."""
    out = ['<ol class="control">']
    for q, cifra, trampa, rev in items:
        out.append(
            f'<li><p class="q">{q}</p>'
            f'<details><summary>Ver la cifra esperada</summary><div class="cifra">{cifra}</div></details>'
            f'<details><summary>No me da. &iquest;D&oacute;nde est&aacute; el enga&ntilde;o?</summary>'
            f'<div class="trampa"><p>{trampa}</p><p class="prompt-t">Prompt para revisar</p>{P(rev)}</div></details></li>')
    out.append("</ol>")
    return "".join(out)


from preguntas_control import MC, REV_PISTA


def control_mc(n):
    """Preguntas de selección con retroalimentación por opción, en CSS puro."""
    esc = html.escape
    out = ['<ol class="control">']
    for qi, (q, ops, rev) in enumerate(MC[n], 1):
        k = qi % len(ops)
        ops = ops[k:] + ops[:k]  # la correcta no queda siempre primera
        name = f"p{n}q{qi}"
        items = []
        for oi, (txt, ok, fb) in enumerate(ops, 1):
            oid = f"{name}o{oi}"
            if ok:
                cuerpo = f'<div class="fb ok"><b>Correcto.</b> {esc(fb)}</div>'
            else:
                if n == 1:
                    rv = f'<p class="prompt-t">Revisen el prompt con este pedido</p>{P(rev)}'
                else:
                    rv = f'<p class="prompt-t">Pista para su prompt de revisi&oacute;n</p><p>{esc(REV_PISTA[n][qi-1])}</p>'
                cuerpo = (f'<div class="fb mal"><b>No cuadra. El engaño:</b> {esc(fb)}{rv}</div>')
            items.append(f'<div class="op"><input type="radio" name="{name}" id="{oid}">'
                         f'<label for="{oid}">{esc(txt)}</label>{cuerpo}</div>')
        out.append(f'<li><p class="q">{esc(q)}</p><div class="mc">{"".join(items)}</div></li>')
    out.append("</ol>")
    return "".join(out)


from carolina_partes import img, IMAGEN, entrega, pistas, critico


def parte(n, zipf, zipt, pide, hacer, salida, ctrl):
    """Una parte del caso = una página D2L con cinco secciones."""
    foto, alt = IMAGEN[n]
    return [
        ("Qu&eacute; pide Carolina", img(foto, alt) + f'<p>{pide}</p><p>{Z(zipf, zipt)}</p>'
         '<p>Descompriman el ZIP sobre la misma carpeta donde est&aacute; <b>caso-carolina</b>. Los archivos nuevos se suman a los que ya tienen.</p>'),
        ("El correo", correo(n)),
        ("Qu&eacute; tienen que hacer", (pasos(hacer) if n == 1 else pistas(n)) + f'<div class="nota"><b>Salida parcial en salidas/.</b> {salida}</div>'),
        ("El punto cr&iacute;tico", critico(n)),
        ("Preguntas de control",
         '<p>Elijan la opci&oacute;n que coincide con lo que les dio Antigravity. Si no es la correcta, la respuesta les dice cu&aacute;l es el enga&ntilde;o y qu&eacute; pedirle a Antigravity para revisarlo. No corrijan el n&uacute;mero a mano: corrijan el prompt y el plan.</p>'
         + control_mc(n)),
        ("Qu&eacute; entregan de esta parte", entrega(n, P)),
    ]


carolina = [
("El caso", """
<p>Carolina Ruales es la Gerente Financiera Corporativa de un grupo automotriz ecuatoriano con varias marcas. En el comit&eacute; del viernes le hicieron una pregunta que nadie pudo contestar con un solo n&uacute;mero:</p>
<div class="nota"><b>&iquest;Cu&aacute;ntos veh&iacute;culos nuevos est&aacute;n facturados y todav&iacute;a no se entregan, en qu&eacute; estado est&aacute; cada uno y qu&eacute; fecha se le puede prometer a cada cliente?</b></div>
<p>La informaci&oacute;n est&aacute; repartida en cinco fuentes que no se hablan. Carolina la va pidiendo por partes y se la reenv&iacute;a a su equipo, que son ustedes, en cinco correos. El caso se trabaja en cinco partes, una por correo, y cada parte se apoya en la anterior. No pasen a la siguiente parte hasta que las preguntas de control de la anterior cuadren.</p>
<p>Los datos, las empresas y las personas del caso son ficticios. El corte de los datos es el jueves 17 de septiembre de 2026 y, para el caso, hoy es viernes 18.</p>
<table><tr><th>Parte</th><th>Correo</th><th>Pregunta</th></tr>
<tr><td>1</td><td>Importaciones</td><td>&iquest;Qu&eacute; tenemos importado?</td></tr>
<tr><td>2</td><td>Aduana y traslados</td><td>&iquest;D&oacute;nde est&aacute; cada unidad?</td></tr>
<tr><td>3</td><td>Facturaci&oacute;n</td><td>&iquest;Qu&eacute; est&aacute; facturado y vigente?</td></tr>
<tr><td>4</td><td>PDI y actas de entrega</td><td>&iquest;Qu&eacute; falta entregar?</td></tr>
<tr><td>5</td><td>Comit&eacute;</td><td>&iquest;Cu&aacute;ndo se entrega y qu&eacute; hay que corregir?</td></tr></table>
"""),
("Antes de empezar", """
<ol>
<li>Cada parte trae su ZIP. Descompr&iacute;manlos todos <b>en el mismo lugar</b>: cada uno suma sus archivos a la carpeta <b>caso-carolina</b>. Si ya ten&iacute;an el correo 1 de la clase anterior, desc&aacute;rguenlo de nuevo: ahora trae la estructura de carpetas del curso.</li>
<li>Abran la carpeta <b>caso-carolina</b> completa en Antigravity y lean LEEME.md.</li>
<li>Una conversaci&oacute;n nueva por parte. El contexto no vive en el chat, vive en contexto/CONTEXTO.md.</li>
<li>Usen el modo Planning: el plan se aprueba antes de ejecutar.</li>
</ol>
""" + arbol("""
caso-carolina/
  AGENTS.md
  LEEME.md
  entradas/        correo-1.md ... correo-5.md
  datos/           00_maestros, 01_importaciones, 02_logistica,
                   03_facturacion, 04_calidad, 05_entregas
  contexto/        CONTEXTO.md, PLAN.md
  procesamiento/
  salidas/
  archivo/
""") + """
<h3>El grupo y sus tres papeles</h3><p>El caso se trabaja con su grupo de D2L. En cada parte hay tres papeles y rotan con cada correo, para que todos pasen por los tres. En grupos de cinco, la quinta persona lleva la bit&aacute;cora de IA.</p>
<table><tr><th>Papel</th><th>Qu&eacute; hace</th></tr>
<tr><td>Opera Antigravity</td><td>Comparte pantalla, escribe los pedidos, lee el plan y lo aprueba o lo corrige.</td></tr>
<tr><td>Audita</td><td>Responde las preguntas de control y rastrea tres casos en los archivos originales.</td></tr>
<tr><td>Redacta a Carolina</td><td>Escribe la respuesta corta de la parte en salidas/: cifras y lo raro que encontraron, en cinco l&iacute;neas.</td></tr></table>
"""),
("Parte 1 &middot; Importaciones", parte(1, "correo-1-importaciones.zip", "Descargar correo 1 &middot; Importaciones",
 "Un solo listado de veh&iacute;culos nuevos importados o en camino, con una fila por VIN y sin repetidos, y el conteo de VIN y contenedores por marca.",
 [("Lean el correo y reconozcan los archivos sin escribir c&oacute;digo.", """Lee entradas/correo-1.md y revisa todo lo que hay en datos/. Para cada archivo dime qué sistema lo produjo, en qué fila empieza la tabla, qué columna trae el VIN y en qué formato vienen las fechas. No escribas código todavía."""),
  ("Completen el contexto.", """Completa contexto/CONTEXTO.md con quién pide, qué pregunta, la fecha de corte 17/09/2026 y que el VIN es la llave única que hay que limpiar antes de comparar."""),
  ("Pidan el plan y apru&eacute;benlo antes de ejecutar.", """Escribe en contexto/PLAN.md cómo vas a armar una base con una fila por VIN a partir de los tres archivos de importaciones: qué lees de cada uno, cómo limpias el VIN y cómo traduces los colores. Espera mi visto bueno."""),
  ("Ejecuten y guarden la base.", """Ejecuta el plan aprobado. Guarda la base en salidas/etapa-1-importaciones.xlsx y el conteo de VIN y contenedores por marca en salidas/etapa-1-respuesta.md. Dime cuántos VIN tuviste que limpiar y por qué."""),
  ("Respondan las preguntas de control y actualicen el contexto.", None)],
 "<b>etapa-1-importaciones.xlsx</b> (una fila por VIN) y <b>etapa-1-respuesta.md</b> (conteo por marca y lo raro).",
 [("&iquest;Cu&aacute;ntos VIN distintos hay en total y en cu&aacute;ntos contenedores?",
   "<b>4.327 VIN</b> en <b>1.080 contenedores</b> y 153 embarques.",
   "Si les da <b>m&aacute;s</b> de 4.327, el mismo carro est&aacute; contado dos veces porque el VIN viene con min&uacute;sculas, espacios, guiones o el prefijo &laquo;VIN:&raquo;. Si aparecen VIN raros, filas con el nombre del buque o VIN sin ETA, Antigravity ley&oacute; la cabecera de los packing lists como si fueran datos: la tabla empieza en la fila 12 y la ETA solo est&aacute; en la cabecera.",
   "¿Cómo limpiaste el VIN antes de contar? Muéstrame 10 VIN antes y después de limpiarlos. ¿En qué fila empieza la tabla de cada packing list de Toyota y cómo sacaste la ETA de la cabecera?"),
  ("&iquest;Cu&aacute;ntos VIN y contenedores hay por marca?",
   "Toyota <b>2.110</b> VIN en 544 contenedores &middot; Changan <b>949</b> en 243 &middot; Suzuki <b>906</b> en 197 &middot; Peugeot <b>248</b> en 67 &middot; Opel <b>114</b> en 29.",
   "Si faltan Changan, Peugeot u Opel, no leyeron todas las hojas del control de Nexumcorp: cada marca va en una hoja distinta. Si Suzuki no cuadra en contenedores, el contenedor trae un espacio en medio.",
   "Lista todas las hojas de cada archivo de importaciones y cuántas filas leíste de cada una. ¿Cómo normalizaste el número de contenedor?"),
  ("&iquest;Cu&aacute;ntos VIN tuvieron que limpiarse?",
   "<b>59 VIN</b> vienen con min&uacute;sculas, espacios, guiones o el prefijo &laquo;VIN:&raquo;.",
   "Si Antigravity dice cero, no revis&oacute; el formato: compar&oacute; el texto tal cual. Si dice cientos, est&aacute; contando como &laquo;sucio&raquo; algo que es normal.",
   "Muéstrame los VIN que cambiaron al limpiarlos, con el valor original, el limpio y el archivo de donde sale cada uno."),
  ("&iquest;Cu&aacute;ntos veh&iacute;culos son a&ntilde;o modelo 2026 y cu&aacute;ntos 2027?",
   "<b>3.612</b> de 2026 y <b>715</b> de 2027.",
   "Suzuki no trae la columna de a&ntilde;o modelo. Se deduce del d&eacute;cimo car&aacute;cter del VIN. Si Suzuki queda con el a&ntilde;o vac&iacute;o, no lo dedujeron.",
   "¿De dónde sacaste el año modelo de Suzuki? Explícame la regla y muéstrame 5 ejemplos."),
  ("&iquest;Cu&aacute;ntas unidades llegan por mes de ETA?",
   "Mayo 111 &middot; junio 672 &middot; julio 872 &middot; agosto 885 &middot; septiembre 925 &middot; octubre 862.",
   "Las fechas de Suzuki vienen como texto con el mes en ingl&eacute;s. Si hay fechas vac&iacute;as o meses fuera de mayo a octubre, no se convirtieron bien.",
   "¿En qué formato venían las fechas de cada archivo y cómo las convertiste? ¿Cuántas fechas no pudiste convertir?")])),
("Parte 2 &middot; Aduana y traslados", parte(2, "correo-2-aduana-y-traslados.zip", "Descargar correo 2 &middot; Aduana y traslados",
 "El estado f&iacute;sico de cada VIN al jueves 17 (en tr&aacute;nsito, en aduana, nacionalizado o en agencia) y si es cierto que Nexumcorp tiene 527 unidades en tr&aacute;nsito.",
 [("Lean el correo y reconozcan los dos archivos nuevos.", """Lee entradas/correo-2.md y revisa los dos archivos nuevos de datos/. Dime qué trae cada uno, en qué formato vienen el contenedor, las fechas y los VIN, y qué problemas ves. No escribas código todavía."""),
  ("Pidan el plan del cruce y apru&eacute;benlo.", """Antes de programar, escribe en contexto/PLAN.md el plan para asignar el estado físico: qué archivo une con cuál, por qué campo y con qué regla de fechas se decide cada estado. Espera mi visto bueno."""),
  ("Ejecuten y pidan los hu&eacute;rfanos.", """Ejecuta el plan. Guarda el estado de cada VIN en salidas/etapa-2-ubicacion.xlsx. Después dime cuántos contenedores de importaciones no aparecen en aduana, cuántos VIN de traslados no encontraste en importaciones y cómo resolviste los que vienen incompletos."""),
  ("Verifiquen el control de Nexumcorp y actualicen el contexto.", """Compara la columna de estado del control de Nexumcorp con el estado que calculaste. ¿Cuántas marcadas EN TRANSITO están mal y dónde están en realidad? Agrega a CONTEXTO.md las reglas de estado de este correo.""")],
 "<b>etapa-2-ubicacion.xlsx</b> (estado por VIN) y <b>etapa-2-respuesta.md</b> (conteo por estado y la verificaci&oacute;n de las 527).",
 [("&iquest;Cu&aacute;ntos contenedores aparecen en la liquidaci&oacute;n de aduana, cu&aacute;ntos arribaron y cu&aacute;ntos tienen levante?",
   "<b>876</b> de los 1.080 contenedores aparecen en aduana. <b>787</b> arribaron y <b>763</b> tienen levante. Los 204 que no aparecen todav&iacute;a no llegan.",
   "Si les salen muchos menos que 876, el contenedor no se normaliz&oacute;: el agente de aduana lo escribe con espacios, guiones y el d&iacute;gito de control separado.",
   "Muéstrame 10 contenedores tal como vienen en aduana y cómo quedaron después de normalizarlos. ¿Cuántos contenedores de aduana no encontraste en importaciones?"),
  ("&iquest;Cu&aacute;ntos VIN hay en cada estado al 17 de septiembre?",
   "En tr&aacute;nsito <b>1.309</b> &middot; en aduana <b>112</b> &middot; nacionalizado, en patio o en ruta <b>216</b> &middot; en agencia <b>2.690</b>. Total 4.327.",
   "Demasiados en tr&aacute;nsito: no normalizaron el contenedor. Demasiados nacionalizados: descartaron los VIN de traslados que vienen incompletos, y esas unidades aparecen fuera de la agencia cuando ya llegaron.",
   "¿Cuántos VIN de traslados leíste, cuántos encontraste en importaciones y cuántos descartaste? ¿Cómo separaste los VIN que vienen juntos en una misma celda?"),
  ("&iquest;Cu&aacute;ntas gu&iacute;as de traslado hay y cu&aacute;ntos VIN vienen incompletos?",
   "<b>701</b> gu&iacute;as. <b>645</b> VIN vienen solo con sus &uacute;ltimos 8 caracteres y se reconstruyen busc&aacute;ndolos en la base de importaciones.",
   "Si Antigravity no reporta VIN incompletos, los descart&oacute; en silencio. Tambi&eacute;n revisen c&oacute;mo separ&oacute; los VIN de una misma celda: vienen con comas, saltos de l&iacute;nea o barras.",
   "Muéstrame 5 VIN de traslados que venían incompletos, cómo los reconstruiste y en qué archivo encontraste el VIN completo. ¿Alguno quedó ambiguo?"),
  ("De las 527 que Nexumcorp marca EN TRANSITO, &iquest;cu&aacute;ntas est&aacute;n mal marcadas y d&oacute;nde est&aacute;n?",
   "<b>133</b> de 527 est&aacute;n mal marcadas: 38 ya est&aacute;n en aduana, 50 nacionalizadas y 45 en la agencia. <b>95</b> de esas 133 ya tienen levante. Siguen en tr&aacute;nsito 394.",
   "Si les da cero, Antigravity copi&oacute; la columna de estado de Nexumcorp en lugar de calcular el estado con las fechas de aduana y traslados. Esa columna se llena a mano.",
   "¿El estado de los VIN de Nexumcorp sale de su columna de estado o de las fechas de aduana y traslados? Recalcúlalo solo con fechas y compara.")])),
("Parte 3 &middot; Facturaci&oacute;n", parte(3, "correo-3-facturacion.zip", "Descargar correo 3 &middot; Facturaci&oacute;n",
 "Cu&aacute;ntos veh&iacute;culos nuevos tienen factura vigente, por empresa, sin facturas anuladas. Los chasis que no cruzan se corrigen y se anotan. Tambi&eacute;n los VIN con dos facturas vigentes y los colores facturados distintos del importado.",
 [("Lean el correo y reconozcan los seis archivos.", """Lee entradas/correo-3.md y revisa los archivos de datos/03_facturacion. Para cada uno dime separador, codificación, en qué fila empieza la tabla, cómo marca las anulaciones y qué filas no son vehículos nuevos. No escribas código todavía."""),
  ("Pidan el plan y apru&eacute;benlo.", """Escribe en contexto/PLAN.md cómo vas a quedarte solo con facturas vigentes de vehículos nuevos: qué descartas, cómo quitas las filas repetidas entre meses y cómo cruzas con importaciones. Espera mi visto bueno."""),
  ("Ejecuten y pidan las cifras de lectura.", """Ejecuta el plan. ¿Cuántas filas leíste de cada archivo, cuántas descartaste y por qué? Agrega a CONTEXTO.md cómo marca las anulaciones cada sistema."""),
  ("Pidan la evidencia de cada correcci&oacute;n de VIN y apru&eacute;benlas una por una.", """Muéstrame las facturas cuyo VIN no aparece en importaciones, con el VIN registrado, el VIN que propones y la razón. No apliques ninguna corrección que no puedas justificar. Guarda las aprobadas en salidas/etapa-3-correcciones.xlsx."""),
  ("Guarden la base de facturas vigentes.", """Guarda en salidas/etapa-3-facturacion.xlsx una fila por VIN con factura vigente y en salidas/etapa-3-respuesta.md el conteo por empresa y las rarezas.""")],
 "<b>etapa-3-facturacion.xlsx</b>, <b>etapa-3-correcciones.xlsx</b> y <b>etapa-3-respuesta.md</b>.",
 [("&iquest;Cu&aacute;ntas filas trae el ERP de Toyota y cu&aacute;ntas est&aacute;n repetidas?",
   "<b>18.864</b> filas en los tres CSV, de las cuales <b>922</b> est&aacute;n repetidas porque agosto se export&oacute; desde el 30 de julio y septiembre desde el 31 de agosto.",
   "Si Antigravity no encuentra repetidas, no compar&oacute; las fechas de corte de cada exportaci&oacute;n. Si el CSV se ley&oacute; con coma como separador, sale una sola columna: usa punto y coma, coma decimal y codificaci&oacute;n de Windows.",
   "¿Con qué separador, decimal y codificación leíste cada CSV de Toyota? ¿Qué rango de fechas trae cada uno y cuántas filas se repiten entre archivos?"),
  ("&iquest;Cu&aacute;ntas facturas de veh&iacute;culos nuevos hay y cu&aacute;ntas est&aacute;n anuladas?",
   "<b>2.105</b> facturas de nuevos: ERP Toyota 1.055, Nexumcorp 615, Suzuki 435. Anuladas <b>33</b>: 18, 7 y 8.",
   "Cada sistema anula distinto: Toyota con una nota de cr&eacute;dito que apunta a la factura original en DOC_REFERENCIA, Nexumcorp con la columna Estado y Suzuki con EST en V o A. Si solo buscaron la palabra &laquo;anulada&raquo;, se les col&oacute; alguna.",
   "Explícame cómo marca las anulaciones cada sistema y muéstrame dos ejemplos de cada uno, con la factura original y lo que la anula."),
  ("&iquest;Cu&aacute;ntos VIN tienen factura vigente, por empresa?",
   "<b>2.069</b>: Casabaca 616 &middot; Toyocosta 420 &middot; Nexumcorp 607 &middot; Suzuki Ecuador 426. Son 2.072 facturas vigentes, pero 3 VIN tienen dos.",
   "Si les salen muchas más de 2.072 facturas vigentes, no quitaron las filas repetidas de Toyota. Si les salen menos VIN, botaron las facturas cuyo VIN no cruza en lugar de corregirlas. Los seminuevos (303: 66 de Casabaca y 237 de 1001Carros) no cuentan.",
   "¿Cuántas facturas vigentes de vehículos nuevos tienes por empresa antes y después de cruzar con importaciones? ¿Qué facturas quedaron sin VIN y por qué?"),
  ("&iquest;Cu&aacute;ntos VIN mal digitados corrigieron?",
   "<b>18</b>: 9 en el ERP de Toyota, 5 en Nexumcorp y 4 en Suzuki. Ninguno queda ambiguo.",
   "Confunden caracteres parecidos (0 y O, 1 e I, 5 y S, 8 y B, 2 y Z, 6 y G) o traen dos d&iacute;gitos transpuestos al final. Si Antigravity propone m&aacute;s de 18 o alguno con dudas, est&aacute; forzando coincidencias: exijan la raz&oacute;n de cada una.",
   "Para cada corrección dime el VIN original, el propuesto, qué caracteres cambiaron, si ambos comparten los primeros once caracteres y si el dígito verificador (noveno carácter) cuadra."),
  ("&iquest;Cu&aacute;ntas rarezas anotaron para Carolina?",
   "<b>30</b> facturas anuladas y refacturadas (11 por cambio de titular, 10 por forma de pago y 9 por datos del cliente) &middot; <b>3</b> VIN con doble factura vigente &middot; <b>12</b> colores facturados distintos del importado.",
   "Unas 60 dobles facturaciones son falsas: salen de las filas repetidas de Toyota. Colores distintos en casi todas las facturas: compararon el nombre de f&aacute;brica en ingl&eacute;s con el nombre comercial sin pasar por la hoja Colores del maestro.",
   "¿Cómo comparaste el color facturado con el importado? ¿Usaste la hoja Colores del maestro? Muéstrame los VIN con doble factura vigente con ambas facturas."),
  ("Control de cuadre: &iquest;cu&aacute;nto suma la facturaci&oacute;n vigente de Suzuki?",
   "<b>USD 8.523.120,25</b>. Con las anuladas incluidas da 8.669.196,17.",
   "Si les da mucho m&aacute;s, sumaron los subtotales por mes y el total general que vienen entre las filas del reporte de Suzuki.",
   "¿Qué filas del reporte de Suzuki son subtotales o totales y cómo las excluiste? Suma solo las facturas vigentes.")])),
("Parte 4 &middot; PDI y actas de entrega", parte(4, "correo-4-calidad-y-entregas.zip", "Descargar correo 4 &middot; PDI y actas",
 "La lista de veh&iacute;culos por entregar: todo veh&iacute;culo nuevo con al menos una factura vigente y sin acta de entrega, ni digitada ni escaneada. El estado de agencia se parte en PDI pendiente y listo para entrega. Y las alertas sobre entregas ya hechas.",
 [("Lean el correo y reconozcan los archivos.", """Lee entradas/correo-4.md y revisa el export de PDI, el registro de actas y la carpeta de actas escaneadas. Dime qué trae cada hoja, qué nombres de columna y formatos de fecha usa y qué filas no son vehículos nuevos. No escribas código todavía."""),
  ("Lean los PDF.", """Lee las actas en PDF y dime cuántas son de vehículos nuevos, cuántas de seminuevos y cuántas son copias de actas que ya están en el registro digitado. Guarda la lista en procesamiento/."""),
  ("Pidan el plan y apru&eacute;benlo.", """Escribe en contexto/PLAN.md cómo vas a decidir qué vehículos están por entregar y en qué estado, usando la definición del correo y los estados de la parte 2. Espera mi visto bueno."""),
  ("Ejecuten y pidan la muestra para el auditor.", """Ejecuta el plan y guarda salidas/etapa-4-por-entregar.xlsx. Dame tres VIN de cada estado con todas sus fechas y el archivo del que sale cada una, para verificarlos a mano. Agrega a CONTEXTO.md la definición de por entregar."""),
  ("Revisen las entregas ya hechas.", """Revisa las entregas ya hechas: ¿algún vehículo entregado sin PDI aprobado, sin factura vigente o con acta fechada antes de la factura? ¿Hay actas que siguen solo escaneadas después de más de 10 días? Guarda las alertas en salidas/etapa-4-respuesta.md.""")],
 "<b>etapa-4-por-entregar.xlsx</b> (una fila por VIN y su estado) y <b>etapa-4-respuesta.md</b> (conteos y alertas).",
 [("&iquest;Qu&eacute; hay en los 166 PDF?",
   "<b>144</b> actas de veh&iacute;culos nuevos y <b>22</b> de seminuevos. <b>15</b> son copias de actas que ya est&aacute;n digitadas.",
   "Si Antigravity no ley&oacute; los PDF o dice que est&aacute;n vac&iacute;os, pidan que extraiga el texto con una librer&iacute;a de PDF. Las copias no deben contar como entregas nuevas.",
   "¿Cómo leíste los PDF? Muéstrame el VIN, la fecha y la empresa de 5 actas escaneadas y dime cuáles ya estaban en el registro digitado."),
  ("&iquest;Cu&aacute;ntos VIN nuevos tienen acta de entrega y cu&aacute;ntos solo escaneada?",
   "<b>1.741</b> VIN nuevos tienen acta. <b>132</b> solo tienen el acta escaneada: 127 dentro del rezago normal de digitaci&oacute;n y 5 traspapelados, con m&aacute;s de 10 d&iacute;as.",
   "Si todas las actas escaneadas salen como traspapeladas, no aplicaron el umbral de 10 d&iacute;as del correo.",
   "¿Cuántos días pasaron entre la fecha de cada acta escaneada y el corte? Muéstrame solo las que pasan de 10 días."),
  ("&iquest;Cu&aacute;ntos veh&iacute;culos est&aacute;n por entregar?",
   "<b>331</b>: Casabaca 104 &middot; Toyocosta 64 &middot; Nexumcorp 98 &middot; Suzuki 65.",
   "<b>462</b>: no leyeron los PDF y cuentan como pendientes 132 veh&iacute;culos ya entregados. <b>327</b> con 17 entregados sin factura: no corrigieron los 18 VIN de la parte 3 y esas facturas quedaron hu&eacute;rfanas.",
   "¿Incluiste las actas escaneadas como entregas? ¿Usaste las facturas con el VIN corregido de la parte 3? Muéstrame cuántos por entregar tienes antes y después de cada paso."),
  ("&iquest;En qu&eacute; estado est&aacute;n los 331?",
   "Listo para entrega <b>154</b> &middot; en agencia, PDI pendiente <b>77</b> &middot; nacionalizado, en patio o en ruta <b>32</b> &middot; en aduana <b>13</b> &middot; en tr&aacute;nsito <b>55</b>.",
   "Las 55 en tr&aacute;nsito no son un error: son ventas anticipadas. Si el PDI no cuadra, no tomaron la &uacute;ltima inspecci&oacute;n: 212 veh&iacute;culos tienen m&aacute;s de una. Ojo tambi&eacute;n con 52 VIN escritos en min&uacute;sculas en el export de PDI.",
   "¿Qué inspección usaste cuando un vehículo tiene varias? ¿Limpiaste el VIN del export de PDI antes de cruzar?"),
  ("&iquest;Qu&eacute; alertas hay sobre las entregas ya hechas?",
   "<b>6</b> entregados sin PDI aprobado &middot; <b>3</b> entregados sin factura vigente &middot; <b>4</b> actas con fecha anterior a la factura &middot; <b>5</b> actas solo escaneadas con m&aacute;s de 10 d&iacute;as.",
   "Si salen 17 o m&aacute;s entregados sin factura, son las facturas con VIN mal digitado que no corrigieron en la parte 3.",
   "Para cada alerta dame el VIN, la empresa, las fechas que la disparan y el archivo de donde sale cada fecha.")])),
("Parte 5 &middot; Comit&eacute;: fechas, Excel y presentaci&oacute;n", parte(5, "correo-5-comite.zip", "Descargar correo 5 &middot; Comit&eacute;",
 "Una fecha estimada de entrega para cada veh&iacute;culo con la regla del correo, en d&iacute;as h&aacute;biles y sin feriados; el Excel del comit&eacute; con cuatro hojas y el Resumen en f&oacute;rmulas; una presentaci&oacute;n corta; y el proceso listo para el pr&oacute;ximo lunes.",
 [("Lean el correo y escriban la regla en el contexto.", """Lee entradas/correo-5.md. Copia la regla de la fecha en contexto/CONTEXTO.md, paso por paso, y dime qué feriados del maestro caen entre el 18 de septiembre y fin de año."""),
  ("Pidan el plan del c&aacute;lculo de fechas y apru&eacute;benlo.", """Escribe en contexto/PLAN.md cómo vas a calcular la fecha estimada de cada vehículo por entregar con la regla del correo, en días hábiles sin feriados, y cómo marcas los atrasados. Espera mi visto bueno."""),
  ("Generen el Excel del comit&eacute;.", """Genera salidas/Vehiculos_por_entregar_2026-09-18.xlsx con las cuatro hojas que pide Carolina: Resumen, Por entregar, Alertas y Base unificada. En el Resumen usa fórmulas sobre las otras hojas, no valores escritos."""),
  ("Dejen el proceso listo para el lunes.", """Guarda el procedimiento: un script en procesamiento/ que reciba la carpeta de datos y la fecha de corte, y contexto/PROCESO.md con los pasos en orden y las preguntas de control de cada parte.""")],
 "<b>Vehiculos_por_entregar_2026-09-18.xlsx</b>, la presentaci&oacute;n y <b>etapa-5-respuesta.md</b>.",
 [("&iquest;Cu&aacute;ntos veh&iacute;culos est&aacute;n atrasados seg&uacute;n la regla?",
   "<b>47</b>, todos listos para entrega: Casabaca 13 &middot; Toyocosta 12 &middot; Nexumcorp 15 &middot; Suzuki 7. Llevan en promedio 17 d&iacute;as desde la factura y el m&aacute;s antiguo, 53.",
   "Si les da <b>77</b>, marcaron como atrasados los 30 cuya fecha cae justo hoy: vencer hoy no es estar atrasado. Si les da m&aacute;s, contaron d&iacute;as calendario en lugar de h&aacute;biles.",
   "¿Contaste días hábiles de lunes a viernes sin feriados? ¿Cómo tratas una fecha que cae exactamente el 18 de septiembre? Muéstrame 3 atrasados con cada fecha de la regla."),
  ("&iquest;C&oacute;mo se reparten las fechas estimadas de los 331?",
   "18 de septiembre, atrasadas: <b>47</b> &middot; 18 de septiembre, a tiempo: <b>30</b> &middot; del 21 al 25 de septiembre: <b>178</b> &middot; del 28 de septiembre al 2 de octubre: <b>21</b> &middot; despu&eacute;s del 2 de octubre: <b>55</b> (la &uacute;ltima, 4 de noviembre).",
   "Si hay fechas antes del 18, olvidaron el piso: ninguna fecha puede quedar antes de hoy. Si las fechas de octubre salen un d&iacute;a antes, no restaron el feriado del 9 de octubre.",
   "¿Hay alguna fecha estimada antes del 18 de septiembre? ¿Qué feriados usaste y de qué hoja del maestro salen?"),
  ("&iquest;Cu&aacute;ntas alertas tiene la hoja Alertas?",
   "<b>81</b>: 30 refacturas &middot; 18 VIN mal digitados &middot; 12 colores distintos &middot; 6 entregados sin PDI aprobado &middot; 5 actas solo escaneadas con m&aacute;s de 10 d&iacute;as &middot; 4 actas anteriores a la factura &middot; 3 entregados sin factura vigente &middot; 3 dobles facturaciones.",
   "Si les faltan tipos, revisen que las alertas de las partes 3 y 4 se hayan pasado al Excel. Si hay decenas de dobles facturaciones o de colores, vuelvan a las preguntas de control de la parte 3.",
   "Cuenta las alertas por tipo en la hoja Alertas y compáralas con lo que reportaste en las partes 3 y 4."),
  ("&iquest;El Resumen se recalcula solo?",
   "S&iacute;. Borren una fila de la hoja Por entregar: los conteos del Resumen deben bajar en uno. Luego deshagan el cambio.",
   "Si el Resumen no cambia, Antigravity escribi&oacute; los n&uacute;meros como valores y no como f&oacute;rmulas.",
   "Reescribe el Resumen con fórmulas CONTAR.SI y CONTAR.SI.CONJUNTO sobre las hojas Por entregar y Alertas. Muéstrame la fórmula de tres celdas."),
  ("&iquest;La presentaci&oacute;n usa solo cifras que est&aacute;n en salidas/?",
   "Cada cifra de la presentaci&oacute;n debe aparecer en el Excel o en una respuesta de salidas/: 331 por entregar, 47 atrasados, 81 alertas.",
   "Si aparece un n&uacute;mero que no encuentran en salidas/, Antigravity lo redonde&oacute;, lo calcul&oacute; aparte o lo invent&oacute;.",
   "Para cada lámina dime qué cifra usa y en qué archivo y celda de salidas/ está.")])),
("El pedido de Carolina", """
<div class="correo"><table class="cab-correo">
<tr><td class="ck">De</td><td>Carolina Ruales, Gerente Financiera Corporativa</td></tr>
<tr><td class="ck">Para</td><td>Equipo de Finanzas</td></tr>
<tr><td class="ck">Asunto</td><td>Lo que llevo al comit&eacute; del lunes</td></tr></table>
<div class="cuerpo-correo">
<p>Equipo:</p>
<p>Para el comit&eacute; del lunes necesito dos cosas. Las quiero el domingo en la noche para revisarlas antes.</p>
<p><b>1. La presentaci&oacute;n, en PowerPoint, de ocho l&aacute;minas.</b> El comit&eacute; tiene veinte minutos y va a leer los t&iacute;tulos antes que los gr&aacute;ficos, as&iacute; que cada t&iacute;tulo tiene que decir la conclusi&oacute;n, no el tema.</p>
<ol>
<li>Portada: la pregunta del comit&eacute; y la respuesta en un n&uacute;mero.</li>
<li>Qu&eacute; tenemos importado.</li>
<li>D&oacute;nde est&aacute; cada unidad, y qu&eacute; pasa con el control de Nexumcorp.</li>
<li>Qu&eacute; est&aacute; facturado y vigente, y lo raro que encontraron al facturar.</li>
<li>Qu&eacute; falta entregar, por estado y por empresa, y las alertas sobre entregas ya hechas.</li>
<li>Cu&aacute;ndo se entrega cada uno y cu&aacute;ntos est&aacute;n atrasados.</li>
<li>Qu&eacute; hacemos esta semana: tres acciones, cada una con responsable, fecha y la cifra que la justifica. D&iacute;ganme tambi&eacute;n qu&eacute; dejamos de hacer para poder hacerlas.</li>
<li>Lo que no sabemos: qu&eacute; supuestos pueden fallar, qu&eacute; riesgo trae cada uno y qu&eacute; dato necesitamos para el pr&oacute;ximo lunes.</li>
</ol>
<p>En las l&aacute;minas 2 a 6 quiero una l&iacute;nea al pie que empiece con «Lo que decidimos». Ah&iacute; me explican la decisi&oacute;n que cambia el n&uacute;mero: qu&eacute; cuenta como el mismo carro, a qu&eacute; fuente le creyeron, qu&eacute; corrigieron, qu&eacute; cuenta como entregado, qu&eacute; fecha prometemos. Si alguien del comit&eacute; pregunta por qu&eacute; ese n&uacute;mero y no otro, quiero poder contestar.</p>
<p>Ninguna cifra puede estar en la presentaci&oacute;n si no est&aacute; en el Excel.</p>
<p><b>2. La carpeta del caso completa, en un ZIP.</b> Auditor&iacute;a tiene que poder rehacer cualquier cifra, y el proceso tiene que correr el pr&oacute;ximo lunes sin ustedes. La carpeta debe traer:</p>
<ul>
<li>El Excel para el comit&eacute;, Vehiculos_por_entregar_2026-09-18.xlsx, con sus cuatro hojas y el Resumen en f&oacute;rmulas.</li>
<li>Las respuestas que me mandaron en cada parte y las bases de cada paso.</li>
<li>El contexto del caso, los planes que aprobaron y el proceso escrito paso por paso.</li>
<li>Los scripts que hacen el trabajo.</li>
<li>La bit&aacute;cora: qu&eacute; le pidieron a la herramienta, qu&eacute; cifra no cuadr&oacute; y c&oacute;mo lo corrigieron.</li>
<li>Los archivos originales, tal como llegaron.</li>
</ul>
<p>Voy a mirar tres cosas primero: si el n&uacute;mero de la portada coincide con el Excel, si las decisiones est&aacute;n explicadas y si la recomendaci&oacute;n se puede ejecutar esta semana.</p>
<p>Gracias,<br>Carolina</p>
</div></div>
<h3>La carpeta que se entrega</h3>
""" + arbol("""
caso-carolina/
  AGENTS.md
  entradas/                 los 5 correos, sin cambios
  datos/                    los archivos originales, sin cambios
  contexto/
    CONTEXTO.md             decisiones y cifras de control de cada parte
    PLAN.md                 los planes que aprobaron
    PROCESO.md              los pasos para correrlo el próximo lunes
  procesamiento/            los scripts
  salidas/
    etapa-1-importaciones.xlsx      etapa-1-respuesta.md
    etapa-2-ubicacion.xlsx          etapa-2-respuesta.md
    etapa-3-facturacion.xlsx        etapa-3-correcciones.xlsx
    etapa-3-respuesta.md
    etapa-4-por-entregar.xlsx       etapa-4-respuesta.md
    Vehiculos_por_entregar_2026-09-18.xlsx
    etapa-5-respuesta.md
    lamina-parte-1.png ... lamina-parte-5.png
    presentacion-comite.pptx        las 8 láminas
    bitacora-ia.md
  archivo/                  lo que reemplazaron
""")),
("C&oacute;mo se entrega", """
<div class="nota"><b>Deber 7 &middot; grupal.</b> Domingo 4 de octubre, 23h59, en la carpeta de entrega &laquo;Deber 7 &middot; Caso Carolina&raquo;. Un integrante sube dos archivos: <b>presentacion-comite.pptx</b> y <b>deber7-grupo-N.zip</b> (N es el n&uacute;mero del grupo en D2L). La nota es la misma para todo el grupo.</div>
<p>La primera l&iacute;nea de bitacora-ia.md dice el n&uacute;mero del grupo, los integrantes y qu&eacute; papel tuvo cada uno en cada parte.</p>
<table><tr><th>Criterio</th><th>Qu&eacute; se mira</th><th>Puntos</th></tr>
<tr><td>Cifras de control</td><td>Las preguntas de control de cada parte cuadran y cada cifra dice de qu&eacute; archivo sale.</td><td>25</td></tr>
<tr><td>Decisiones</td><td>Cada l&iacute;nea «Lo que decidimos» responde el punto cr&iacute;tico de su parte con un argumento de negocio.</td><td>20</td></tr>
<tr><td>Presentaci&oacute;n</td><td>Ocho l&aacute;minas, t&iacute;tulos con conclusi&oacute;n, recomendaci&oacute;n ejecutable y riesgos honestos.</td><td>20</td></tr>
<tr><td>Excel y proceso</td><td>Cuatro hojas, fechas con la regla, Resumen con f&oacute;rmulas y PROCESO.md que otro puede seguir.</td><td>20</td></tr>
<tr><td>Carpeta y bit&aacute;cora</td><td>La estructura se respeta, datos/ est&aacute; intacto y la bit&aacute;cora dice qu&eacute; no cuadr&oacute; y c&oacute;mo se corrigi&oacute;.</td><td>15</td></tr>
<tr><td colspan="2"><b>Total</b></td><td><b>100</b></td></tr></table>
"""),
]

secc = dict(carolina)
PARTES = [k for k, _ in carolina if k.startswith("Parte")]
presentacion_final = """
<p>Cada parte termina con una l&aacute;mina. Al final las juntan en una presentaci&oacute;n de ocho l&aacute;minas en PowerPoint para el comit&eacute; de Carolina.</p>
<table><tr><th>L&aacute;mina</th><th>Qu&eacute; lleva</th><th>Sale de</th></tr>
<tr><td>1</td><td>Portada: la pregunta del comit&eacute; y la respuesta en un n&uacute;mero</td><td>Parte 5</td></tr>
<tr><td>2</td><td>Qu&eacute; tenemos importado</td><td>Parte 1</td></tr>
<tr><td>3</td><td>D&oacute;nde est&aacute; cada unidad</td><td>Parte 2</td></tr>
<tr><td>4</td><td>Qu&eacute; est&aacute; facturado y vigente</td><td>Parte 3</td></tr>
<tr><td>5</td><td>Qu&eacute; falta entregar</td><td>Parte 4</td></tr>
<tr><td>6</td><td>Cu&aacute;ndo se entrega</td><td>Parte 5</td></tr>
<tr><td>7</td><td>Qu&eacute; hacer esta semana y qu&eacute; se deja de hacer</td><td>Parte 5</td></tr>
<tr><td>8</td><td>Lo que no sabemos: supuestos, riesgos y el dato que falta</td><td>Parte 5</td></tr></table>
<p>Las l&aacute;minas 2 a 6 llevan al pie una l&iacute;nea «Lo que decidimos»: la respuesta del grupo al punto cr&iacute;tico de esa parte. Es lo que convierte un gr&aacute;fico en una decisi&oacute;n defendible ante el comit&eacute;.</p>
"""
inicio = [
    ("El caso", img("carolina.jpg", "Carolina, gerente financiera, revisando los correos del caso en su escritorio.") + secc["El caso"]),
    ("Antes de empezar", img("carpeta-de-trabajo.jpg", "Una carpeta con documentos y una lupa.", 360) + secc["Antes de empezar"]),
    ("La presentaci&oacute;n que arman", presentacion_final),
]
open(os.path.join(OUT, "carolina-inicio.html"), "w").write(pagina(
    "Caso Carolina: facturados y no entregados", SERIE,
    "El caso, la carpeta, el grupo y la presentaci&oacute;n final", inicio,
    "Sigue con la Parte 1 &middot; Importaciones &rarr;"))
for i, k in enumerate(PARTES, 1):
    sig = f"Sigue con la {PARTES[i]} &rarr;" if i < len(PARTES) else "Sigue con la entrega del Deber 7 &rarr;"
    open(os.path.join(OUT, f"carolina-parte-{i}.html"), "w").write(pagina(
        k, f"ADM 2003 &middot; Caso Carolina &middot; Parte {i} de 5", "Correo, pasos, preguntas de control y lo que se entrega", secc[k], sig))
open(os.path.join(OUT, "carolina-pedido-comite.html"), "w").write(pagina(
    "Deber 7: lo que pide Carolina", "ADM 2003 &middot; Caso Carolina &middot; Entrega",
    "Lo que Carolina necesita para el comit&eacute; del lunes", [("El pedido de Carolina", secc["El pedido de Carolina"]), ("C&oacute;mo se entrega", secc["C&oacute;mo se entrega"])],
    "Suban el ZIP en la carpeta de entrega &laquo;Deber 7 &middot; Caso Carolina&raquo;"))

# ---------------------------------------------------------------- 3. PROYECTO MEDIO SEMESTRE
SERIE2 = "ADM 2003 · An&aacute;lisis de Datos · Corte de medio semestre"
proyecto = [
("El encargo", """
<p>Andr&eacute;s Villac&iacute;s, Gerente Comercial de Comercial Andina, quiere dejar de tratar a todos sus clientes igual. Tiene 1.800 clientes en cinco ciudades y una tienda en l&iacute;nea, y siente que buena parte del presupuesto de promociones se va en descuentos para gente que igual iba a comprar.</p>
<div class="nota"><b>&iquest;Qui&eacute;nes son nuestros clientes, cu&aacute;nto valen y qu&eacute; le decimos a cada segmento el pr&oacute;ximo mes?</b></div>
<p>El proyecto se hace en grupo y con Antigravity, con el mismo marco de trabajo del caso Carolina: una carpeta ordenada, contexto escrito, plan aprobado antes de ejecutar y salidas parciales revisadas en cada etapa.</p>
<p>""" + Z("proyecto-medio-semestre.zip", "Descargar la carpeta del proyecto") + """</p>
""" + arbol("""
rfm-comercial-andina/
  AGENTS.md
  entradas/       encargo.md
  datos/          ventas.csv, clientes.csv, productos.csv, sucursales.csv
  contexto/       CONTEXTO.md, PLAN.md
  procesamiento/
  salidas/
  archivo/
""")),
("RFM+P en cinco minutos", """
<p>RFM+P describe a cada cliente con cuatro n&uacute;meros calculados a una fecha de corte, aqu&iacute; el 31 de diciembre de 2025.</p>
<table><tr><th>Letra</th><th>Qu&eacute; mide</th><th>C&oacute;mo se calcula</th></tr>
<tr><td>R &middot; Recencia</td><td>Qu&eacute; tan reciente es su &uacute;ltima compra.</td><td>D&iacute;as entre su &uacute;ltima compra y la fecha de corte. Menos es mejor.</td></tr>
<tr><td>F &middot; Frecuencia</td><td>Cu&aacute;ntas veces compra.</td><td>N&uacute;mero de facturas distintas.</td></tr>
<tr><td>M &middot; Monto</td><td>Cu&aacute;nto compra.</td><td>Ventas netas, restando devoluciones.</td></tr>
<tr><td>P &middot; Margen</td><td>Cu&aacute;nto deja.</td><td>Ventas netas menos costo (cantidad por costo unitario).</td></tr></table>
<p>Con esos cuatro n&uacute;meros se ordena a los clientes, por ejemplo en quintiles, y se arman pocos segmentos con nombre de negocio: VIP, leales, en riesgo, dormidos, nuevos. El que m&aacute;s compra no siempre es el que m&aacute;s deja: por eso va la P.</p>
<p>Un segmento sirve si cumple tres requisitos:</p>
<ul class="check"><li><b>Accionable</b>: cambia lo que se le dice o se le ofrece.</li><li><b>Medible</b>: se sabe qui&eacute;n est&aacute; adentro y cu&aacute;nto vale.</li><li><b>Estable</b>: no cambia por completo si se mueve un poco el corte.</li></ul>
<div class="apuesta"><p><b>Un segmento se llama &laquo;Cluster 3&raquo;. &iquest;Qu&eacute; pasa en el equipo comercial?</b></p>
<input type="radio" name="b" id="b1"><label for="b1">Lo usan igual, el nombre no importa.</label>
<input type="radio" name="b" id="b2"><label for="b2">Nadie sabe qu&eacute; hacer con &eacute;l.</label>
<input type="radio" name="b" id="b3"><label for="b3">Le piden al analista que lo explique cada vez.</label>
<div class="fb fb1">El nombre es la primera instrucci&oacute;n. Sin &eacute;l, el segmento no cambia ninguna acci&oacute;n.</div>
<div class="fb fb2">As&iacute; es. Un segmento sin nombre de negocio no es accionable.</div>
<div class="fb fb3">Pasa, y a la segunda vez dejan de usarlo. Ponle un nombre que se entienda solo.</div></div>
"""),
("Las etapas en Antigravity",
etapa(1, "Reconocer y limpiar",
 "Entender los cuatro archivos y decidir qu&eacute; se hace con devoluciones, ventas sin cliente, fechas en varios formatos, precios vac&iacute;os y ciudades mal escritas.",
 [("Reconocimiento", """Lee entradas/encargo.md y revisa los archivos de datos/. Para cada archivo dime qué representa una fila, qué columnas trae, cuál es la llave para cruzarlo y qué problemas de calidad encuentras, con cuántas filas afecta cada uno. No escribas código todavía."""),
  ("Plan de limpieza", """Escribe en contexto/PLAN.md qué propones hacer con cada problema y por qué. Espera mi visto bueno. Cuando lo apruebe, deja la base limpia en procesamiento/ y anota en CONTEXTO.md cuántas filas quedaron fuera y por qué.""")],
 "<b>etapa-1-calidad.md</b> con cada problema, cu&aacute;ntas filas afecta y la decisi&oacute;n tomada.",
 ["datos/ est&aacute; intacto.", "Las devoluciones restan, no se borran.", "Se sabe cu&aacute;ntas ventas quedaron fuera por no tener cliente."])
+ etapa(2, "Calcular R, F, M y P",
 "Una fila por cliente con sus cuatro m&eacute;tricas.",
 [("C&aacute;lculo", """Con la base limpia, calcula para cada cliente recencia, frecuencia, monto y margen según las definiciones de contexto/CONTEXTO.md. Muéstrame el plan antes. Guarda el resultado en salidas/etapa-2-rfmp.xlsx."""),
  ("Verificaci&oacute;n", """Dame tres clientes con todas sus facturas para verificar a mano sus cuatro métricas. ¿Cuántos clientes tienen margen negativo?""")],
 "<b>etapa-2-rfmp.xlsx</b> con una fila por cliente.",
 ["El margen sale de costo y precio, no se inventa.", "El auditor verific&oacute; tres clientes a mano."])
+ etapa(3, "Segmentar y nombrar",
 "Pocos segmentos con nombre comercial, con cu&aacute;ntos clientes y cu&aacute;nto margen tiene cada uno.",
 [("Propuesta", """Propón una segmentación de 4 a 6 grupos a partir de R, F, M y P. Explica el criterio de corte, ponle a cada segmento un nombre de negocio y dime cuántos clientes y qué porcentaje del margen tiene cada uno. Espera mi visto bueno antes de guardarla."""),
  ("Estabilidad", """Si muevo los cortes un poco, ¿cuántos clientes cambian de segmento? Muéstrame el resultado y dime si la segmentación es estable.""")],
 "<b>rfm-por-cliente.xlsx</b> con una fila por cliente y su segmento, y una hoja resumen por segmento.",
 ["Ning&uacute;n segmento se llama con n&uacute;mero o letra.", "Se prob&oacute; la estabilidad."])
+ etapa(4, "Recomendar y presentar",
 "Un mensaje comercial por segmento, con su costo estimado y el retorno esperado, y la presentaci&oacute;n para el comit&eacute; de Andr&eacute;s.",
 [("Recomendaci&oacute;n", """Para cada segmento propone una acción para el próximo mes, cuánto costaría y qué retorno esperamos, con los supuestos escritos. Separa lo que sale de los datos de lo que es supuesto."""),
  ("Presentaci&oacute;n", """Lee CONTEXTO.md y salidas/. Propón primero el guion de una presentación de 8 a 10 láminas con títulos que digan la conclusión y la cifra que sostiene cada uno. Espera mi visto bueno y después genérala en salidas/ con fondo blanco.""")],
 "<b>presentacion-comite</b> (PDF o PPTX) y <b>bitacora-ia.md</b>.",
 ["Cada cifra de la presentaci&oacute;n est&aacute; en salidas/.", "Los supuestos de costo y retorno est&aacute;n escritos."])),
("Qu&eacute; se entrega y cu&aacute;ndo", """
<table><tr><th>Fecha</th><th>Qu&eacute; pasa</th></tr>
<tr><td>Mi&eacute;rcoles 7 de octubre</td><td>Lanzamiento en clase. Los grupos arman la carpeta y cierran la etapa 1.</td></tr>
<tr><td>9 al 18 de octubre</td><td>Receso. Ventana de trabajo del proyecto.</td></tr>
<tr><td><b>Domingo 18 de octubre, 23h59</b></td><td><b>Entrega en D2L</b>: la carpeta rfm-comercial-andina comprimida en ZIP.</td></tr>
<tr><td>Lunes 19 y mi&eacute;rcoles 21 de octubre</td><td>Devoluci&oacute;n. La clase de RFM se arma sobre los segmentos de los grupos y se contrasta con KMeans.</td></tr></table>
<p>El ZIP debe traer:</p>
<ul class="check">
<li>contexto/CONTEXTO.md y contexto/PLAN.md al d&iacute;a.</li>
<li>salidas/etapa-1-calidad.md y salidas/etapa-2-rfmp.xlsx.</li>
<li>salidas/rfm-por-cliente.xlsx con el segmento de cada cliente y el resumen por segmento.</li>
<li>La presentaci&oacute;n para el comit&eacute;, de 8 a 10 l&aacute;minas, en salidas/.</li>
<li>salidas/bitacora-ia.md con los prompts de cada etapa y qu&eacute; se verific&oacute;.</li>
<li>Los scripts de procesamiento/, para que el an&aacute;lisis se pueda volver a correr.</li>
</ul>
"""),
("R&uacute;brica", """
<p>Vale el 40 % de la categor&iacute;a Proyectos, que pesa 25 %: es decir, el 10 % de la nota del curso. El proyecto final es el otro 60 % de esa categor&iacute;a.</p>
<table><tr><th>Criterio</th><th>Qu&eacute; se mira</th><th>Puntos</th></tr>
<tr><td>Preparaci&oacute;n de los datos</td><td>Devoluciones netadas, ventas sin cliente tratadas y cada decisi&oacute;n documentada. Se declara cu&aacute;ntas filas quedaron fuera y por qu&eacute;.</td><td>15</td></tr>
<tr><td>C&aacute;lculo de R, F, M y P</td><td>Las cuatro m&eacute;tricas por cliente, con la definici&oacute;n escrita y el margen calculado desde costo y precio.</td><td>20</td></tr>
<tr><td>Segmentos con nombre de negocio</td><td>Nombre comercial, no n&uacute;mero, y criterio de corte justificado.</td><td>20</td></tr>
<tr><td>Los tres requisitos</td><td>Se muestra que cada segmento es accionable, medible y estable.</td><td>15</td></tr>
<tr><td>Recomendaci&oacute;n comercial</td><td>Un mensaje por segmento, con costo estimado y retorno esperado.</td><td>20</td></tr>
<tr><td>Carpeta, reproducibilidad y bit&aacute;cora</td><td>La estructura se respeta, los scripts corren de nuevo y la bit&aacute;cora dice qu&eacute; se pidi&oacute; y qu&eacute; se verific&oacute;.</td><td>10</td></tr>
<tr><td colspan="2"><b>Total</b></td><td><b>100</b></td></tr></table>
<p>En la devoluci&oacute;n cualquier persona del grupo tiene que poder explicar, sin leer, por qu&eacute; eligieron esos segmentos y de d&oacute;nde sale cada cifra.</p>
"""),
]
open(os.path.join(OUT, "proyecto-medio-semestre-enunciado.html"), "w").write(pagina(
    "Proyecto de medio semestre: &iquest;qui&eacute;nes son nuestros clientes?", SERIE2,
    "Segmentaci&oacute;n RFM+P de Comercial Andina hecha con Antigravity", proyecto,
    "Ve al siguiente tema &rarr; Entrega del proyecto"))
print("ok", os.listdir(OUT))
