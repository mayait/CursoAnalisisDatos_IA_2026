#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera el sitio estático de Análisis de Datos con IA y Python · ADM 2003 · USFQ.

Lee el contenido docente de contenido.py y los datos de calendario/material de
datos_curso.py, y escribe todas las páginas HTML en la carpeta sitio/.

Uso:  python3 generar_sitio.py
"""
import html
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
SITIO = os.path.dirname(AQUI)
sys.path.insert(0, AQUI)

from contenido import (SEMANAS, EVALUACION, POLITICA_IA, DATACAMP_LINK,
                       DATACAMP_RUTA, DATACAMP_SUGERIDO, DATACAMP_PASOS, CONCURSO,
                       RUBRICAS, PROTOCOLO_DATOS, NIVELACION, RUTA_MINIMA, ACCESIBILIDAD)
from datos_curso import (SEM2, BLOQUE, SESIONES, CALENDARIO, MATERIAL,
                         MATERIAL_FUERA, CASOS, SIMULADORES, DATACAMP,
                         PENDIENTES, HEREDADO)

CURSO = "Análisis de Datos con IA y Python"
CODIGO = "ADM 2003"
PERIODO = "Primer Semestre 2026-2027 · USFQ Galápagos"
REPO = "CursoAnalisisDatos_IA_2026"

CASO_ARCHIVO = {
 1: "Caso_01_Segmentacion_Clientes_Retail.md", 2: "Caso_02_Sistema_Bancario_Ecuador.md",
 3: "Caso_03_Scouting_FIFA.md", 4: "Caso_04_Movilidad_NYC.md", 5: "Caso_05_Sismicidad_Ecuador.md",
 6: "Caso_06_Resenas_Amazon_NLP.md", 7: "Caso_07_Hits_Spotify.md", 8: "Caso_08_Fraude_Tarjetas.md",
 9: "Caso_09_OLIST_Ecommerce.md", 10: "Caso_10_Stack_Overflow_Tendencias.md",
}

# índice de bloque (color de familia) por semana
BLOQUE_N = {1:1,2:1,3:1,4:1,5:1, 6:2,7:2, 8:3, 9:4,10:4,11:4, 12:5,13:5,14:5, 15:6,16:6}
CASO_SEMANAS = {
 1: [8, 13], 2: [2, 5, 6], 3: [12, 13], 4: [5, 6], 5: [3, 6],
 6: [15], 7: [14], 8: [11, 14], 9: [5], 10: [3, 9],
}

BLOQUE_COLOR = {1:"#0F6E8C",2:"#7A4BA8",3:"#A6192E",4:"#0B6E4F",5:"#B26B00",6:"#3E5C8A"}

REPO_GITHUB = "mayait/CursoAnalisisDatos_IA_2026"

def colab(rel):
    """Badge de Colab para un cuaderno del repositorio."""
    url = f"https://colab.research.google.com/github/{REPO_GITHUB}/blob/main/sitio/{rel}"
    return (f'<a class="boton sec" href="{url}">Abrir en Colab</a>')

def ejercicios_del_lab(w):
    """Lee lab_NN.ipynb y devuelve [(icono, titulo, descripcion)] de sus ejercicios."""
    import json as _json
    ruta = os.path.join(SITIO, "labs", f"lab_{w:02d}.ipynb")
    if not os.path.exists(ruta):
        return []
    nb = _json.load(open(ruta, encoding="utf-8"))
    ICONOS = {"\U0001F336": "guiado", "\U0001F525": "desafio", "\U0001F3AF": "reto"}
    out = []
    for c in nb.get("cells", []):
        if c.get("cell_type") != "markdown":
            continue
        lineas = "".join(c["source"]).split("\n")
        for i, ln in enumerate(lineas):
            t = ln.strip()
            if not t.startswith("#"):
                continue
            icono = next((k for k in ICONOS if k in t), None)
            if not icono:
                continue
            titulo = re.sub(r"^#+\s*", "", t)
            desc = ""
            for sig in lineas[i + 1:]:
                sig = sig.strip()
                if sig and not sig.startswith("#"):
                    desc = re.sub(r"[*`]", "", sig)
                    break
            out.append((ICONOS[icono], titulo, desc[:190]))
    return out

def stats_lab(w):
    """Número de celdas de código y de texto del laboratorio."""
    import json as _json
    ruta = os.path.join(SITIO, "labs", f"lab_{w:02d}.ipynb")
    if not os.path.exists(ruta):
        return None
    nb = _json.load(open(ruta, encoding="utf-8"))
    cod = sum(1 for c in nb["cells"] if c["cell_type"] == "code")
    return dict(total=len(nb["cells"]), code=cod, md=len(nb["cells"]) - cod)

RUBRICA = [
    ("Pregunta y unidad de análisis", "La pregunta de negocio está escrita, la unidad de análisis es explícita y la comparación existe.", "20 %"),
    ("Corrección técnica", "El cuaderno corre completo, los números se reproducen y las decisiones de datos están justificadas.", "30 %"),
    ("Línea base y contraste", "Hay una alternativa declarada contra la cual se mide el resultado. Sin línea base, este criterio es cero.", "20 %"),
    ("Traducción a decisión", "El resultado está expresado en unidades de negocio y dice qué hacer el lunes.", "20 %"),
    ("Bitácora de IA", "Consta el prompt final y qué se verificó de la respuesta del asistente.", "10 %"),
]

def e(x):
    """Escapa HTML y convierte `código` de markdown a <code>."""
    t = html.escape(str(x), quote=False)
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", t)

def enlace(txt, url):
    return f'<a href="{html.escape(url, quote=True)}">{e(txt)}</a>'

# ── páginas fijas del menú ────────────────────────────────────
FIJAS = [("index.html", "Portada"), ("calendario.html", "Calendario"),
         ("proyecto.html", "Proyecto integrador"), ("evaluacion.html", "Evaluación y política de IA"),
         ("casos.html", "Casos de estudio"), ("datacamp.html", "DataCamp y concurso"),
         ("laboratorios.html", "Laboratorios"),
         ("rubricas.html", "Rúbricas"),
         ("apoyo.html", "Apoyo y accesibilidad"),
         ("recursos.html", "Recursos y datasets"),
         ("docente.html", "Guía del docente")]

def sidebar(actual):
    o = ['<nav id="sidebar" aria-label="Contenidos del curso">', '<div class="sb-sec">El curso</div>']
    for arch, nom in FIJAS:
        act = arch == actual
        cls = ' class="activo" aria-current="page"' if act else ''
        o.append(f'<a href="{arch}"{cls}>{e(nom)}</a>')
    o.append('<div class="sb-div"></div><div class="sb-sec">Semanas</div>')
    bloque_previo = None
    for w in sorted(SEM2):
        if BLOQUE[w] != bloque_previo:
            bloque_previo = BLOQUE[w]
            o.append(f'<div class="sb-sec b{BLOQUE_N[w]}">{e(bloque_previo)}</div>')
        arch = f"semana-{w:02d}.html"
        act = arch == actual
        cls = ' class="activo" aria-current="page"' if act else ''
        marca = ''
        if w == 8:
            marca = '<span class="marca">Corte</span>'
        elif w == 16:
            marca = '<span class="marca">Final</span>'
        nombre = SEM2[w][0]
        corto = nombre if len(nombre) <= 34 else nombre[:33].rstrip() + '…'
        tit = html.escape(f"Semana {w} · {nombre}", quote=True)
        o.append(f'<a href="{arch}"{cls} title="{tit}" aria-label="{tit}"><span class="num">{w:02d}</span><span class="txt">{e(corto)}</span>{marca}</a>')
    o.append('</nav>')
    return "\n".join(o)

def pagina(archivo, titulo, chip, cuerpo):
    doc = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{e(titulo)} — {e(CURSO)} · {e(CODIGO)}</title>
<meta name="description" content="{e(CURSO)} · {e(CODIGO)} · {e(PERIODO)}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Source+Sans+3:ital,wght@0,400;0,600;0,700;0,800;1,400&family=Source+Serif+4:wght@600;700&family=JetBrains+Mono:wght@400&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/estilos.css">
</head>
<body>
<a class="saltar" href="#contenido">Saltar al contenido</a>
<header id="topbar">
  <div class="topbar-left">
    <button id="menu-toggle" onclick="document.getElementById('sidebar').classList.toggle('abierto')" aria-label="Menú">&#9776;</button>
    <a href="index.html" class="brand"><span class="sigla">USFQ</span><span class="nombre">{e(CURSO)}</span></a>
  </div>
  <span class="chip">{e(chip)}</span>
</header>
<div id="layout">
{sidebar(archivo)}
<main id="contenido">
  <div class="envoltorio">
{cuerpo}
  </div>
</main>
</div>
<footer>
  <div class="linea">
    <span>{e(CURSO)} · {e(CODIGO)} · {e(PERIODO)}</span>
    <span>Repositorio del curso: <code>{e(REPO)}</code></span>
  </div>
</footer>
<script>
document.querySelectorAll('main a').forEach(function(a){{
  if (a.getAttribute('href') && a.getAttribute('href').startsWith('http')) {{
    a.setAttribute('target','_blank'); a.setAttribute('rel','noopener');
  }}
}});
</script>
</body>
</html>
"""
    with open(os.path.join(SITIO, archivo), "w", encoding="utf-8") as f:
        f.write(doc)

def recurso_html(rec):
    """Enlaza el recurso si vive dentro del sitio; si no, lo muestra como código."""
    if rec.startswith("casos/") or rec.startswith("simuladores/"):
        return f'<a href="{html.escape(rec, quote=True)}"><code>{e(rec)}</code></a>'
    if rec.startswith("Material Actual/"):
        return f'<a href="../{html.escape(rec, quote=True)}"><code>{e(rec)}</code></a>'
    return f'<code>{e(rec)}</code>'

def navpie(w):
    prev = f'<a href="semana-{w-1:02d}.html"><span class="e">Anterior</span><span class="t">Semana {w-1} · {e(SEM2[w-1][0][:38])}</span></a>' if w > 1 else '<a href="index.html"><span class="e">Anterior</span><span class="t">Portada</span></a>'
    sig = f'<a class="sig" href="semana-{w+1:02d}.html"><span class="e">Siguiente</span><span class="t">Semana {w+1} · {e(SEM2[w+1][0][:38])}</span></a>' if w < 16 else '<a class="sig" href="evaluacion.html"><span class="e">Siguiente</span><span class="t">Evaluación y política de IA</span></a>'
    return f'<div class="nav-pie">{prev}{sig}</div>'

# ══════════════════════════════════════════════════════════════
# PÁGINAS DE SEMANA
# ══════════════════════════════════════════════════════════════
def construir_semana(w):
    c = SEMANAS[w]
    tema, tecnica = SEM2[w]
    b = BLOQUE_N[w]
    ses = [s for s in CALENDARIO if s.get("curso") == w and s["estado"] == "Clase"]
    lunes = next((s for s in ses if s["d"] == "L"), None)
    miercoles = next((s for s in ses if s["d"] == "M"), None)
    st = stats_lab(w)
    ejs = ejercicios_del_lab(w)
    o = []

    # ── encabezado
    o.append(f'<div class="kicker">Semana {w} · {e(BLOQUE[w])}</div>')
    o.append(f'<h1>{e(tema)}</h1>')
    o.append(f'<p class="bajada">{e(c["intro"])}</p>')
    o.append('<div class="meta">')
    o.append(f'<span>{e(" y ".join(s["fecha"] for s in ses))}</span>')
    o.append(f'<span>{"2 sesiones" if len(ses) == 2 else "1 sesión"} de 1.5 h</span>')
    o.append(f'<span>{e(tecnica)}</span>')
    if st:
        o.append(f'<span>Laboratorio de {st["total"]} celdas</span>')
    if w == 8:
        o.append('<span class="destacado">Proyecto de medio semestre</span>')
    if w == 11:
        o.append('<span class="destacado">Semana comprimida por feriado</span>')
    o.append('</div>')

    # ── mapa de la semana
    o.append('<h2>Cómo se arma la semana</h2>')
    o.append('<div class="rejilla c3">')
    tarj = []
    if lunes:
        tl, dl, _ = SESIONES[(w, "L")]
        tarj.append(("Clase teórica", f'Lunes {lunes["fecha"]}', tl))
    if miercoles:
        tm, dm, _ = SESIONES[(w, "M")]
        tarj.append(("Taller en grupos", f'Miércoles {miercoles["fecha"]}', tm))
    ent_sem = next((SESIONES[(w, s["d"])][2] for s in ses if SESIONES[(w, s["d"])][2] != "\u2014"), None)
    if ent_sem:
        tarj.append(("Entregable", "Al cierre del taller", ent_sem.replace("**", "")))
    for n, f, t in tarj:
        o.append(f'<div class="tarjeta" data-b="{b}"><div class="n">{e(n)}</div><div class="t">{e(t)}</div><div class="d">{e(f)}</div></div>')
    o.append('</div>')

    # ── objetivos
    o.append('<h2>Objetivos de aprendizaje</h2>')
    o.append('<p>Al terminar la semana podrás:</p><ul>')
    for x in c["objetivos"]:
        o.append(f'<li>{e(x)}</li>')
    o.append('</ul>')

    # ── clase teórica
    if lunes:
        tl, dl, entl = SESIONES[(w, "L")]
        o.append('<h2>Clase teórica</h2>')
        o.append('<div class="sesion">')
        o.append(f'<div class="cab"><span class="dia">Lunes · concepto y caso</span>'
                 f'<span class="fecha">Sesión {lunes["ses"]} · {e(lunes["fecha"])} · 90 minutos</span></div>')
        o.append(f'<h3>{e(tl)}</h3><p>{e(dl)}</p>')
        if entl != "\u2014":
            o.append(f'<div class="caja entrega"><div class="titulo">Entrega de esta sesión</div><p>{e(entl.replace("**", ""))}</p></div>')
        o.append('</div>')
        o.append('<h3>Temas que se tratan</h3>')
        o.append('<table><thead><tr><th scope="col" class="num">#</th><th scope="col">Tema</th><th scope="col">Qué se cubre</th></tr></thead><tbody>')
        for i, (t, d) in enumerate(c["contenidos"], 1):
            o.append(f'<tr><td class="num">{i}</td><td><strong>{e(t)}</strong></td><td>{e(d)}</td></tr>')
        o.append('</tbody></table>')
        o.append(f'<div class="caja trampa"><div class="titulo">\u26a0\ufe0f La trampa de esta semana</div><p>{e(c["trampa"])}</p></div>')

    # ── taller / laboratorio
    o.append('<h2>Taller: laboratorio en grupos</h2>')
    if miercoles:
        tm, dm, entm = SESIONES[(w, "M")]
        o.append('<div class="sesion lab">')
        o.append(f'<div class="cab"><span class="dia">Miércoles · laboratorio</span>'
                 f'<span class="fecha">Sesión {miercoles["ses"]} · {e(miercoles["fecha"])} · 90 minutos</span></div>')
        o.append(f'<h3>{e(tm)}</h3><p>{e(dm)}</p>')
        o.append('</div>')
    else:
        o.append('<div class="caja aviso"><div class="titulo">Sesión única</div>'
                 '<p>Esta semana no tiene sesión de miércoles independiente: el feriado del lunes obliga a dictar '
                 'concepto y taller juntos, en noventa minutos.</p></div>')

    o.append('<h3>Pasos del taller</h3><ol class="pasos">')
    for x in c["practica"]:
        o.append(f'<li>{e(x)}</li>')
    o.append('</ol>')

    if st:
        o.append(f'<div class="caja"><div class="titulo">Cuaderno del laboratorio</div>'
                 f'<p><code>labs/lab_{w:02d}.ipynb</code> \u00b7 {st["total"]} celdas '
                 f'({st["code"]} de c\u00f3digo, {st["md"]} de texto). Corre completo sobre los datos de '
                 f'Comercial Andina sin instalar nada.</p>'
                 f'<p style="margin-top:.7rem"><a class="boton" href="lab-{w:02d}.html">Ver la gu\u00eda del laboratorio</a> '
                 f'{colab(f"labs/lab_{w:02d}.ipynb")} '
                 f'<a class="boton sec" href="labs/lab_{w:02d}.ipynb">Descargar .ipynb</a></p></div>')

    if ejs:
        o.append('<h3>Ejercicios del cuaderno</h3>')
        o.append('<table><thead><tr><th scope="col">Tipo</th><th scope="col">Ejercicio</th><th scope="col">De qué va</th></tr></thead><tbody>')
        etq = {"guiado": ('<span class="etiqueta inf">Guiado</span>', "Se resuelve en clase con el docente"),
               "desafio": ('<span class="etiqueta avi">Desaf\u00edo</span>', "Queda para casa si no da el tiempo"),
               "reto": ('<span class="etiqueta ok">Reto en clase</span>', "Quince minutos, se comparte en pantalla")}
        for tipo, titulo, desc in ejs:
            marca = etq.get(tipo, ('<span class="etiqueta">Ejercicio</span>', ""))[0]
            o.append(f'<tr><td>{marca}</td><td><strong>{e(titulo)}</strong></td><td>{e(desc)}</td></tr>')
        o.append('</tbody></table>')

    # ── proyecto e IA
    o.append('<h2>Proyecto y uso de IA</h2>')
    o.append(f'<div class="caja"><div class="titulo">Trabajo sobre el caso del grupo</div><p>{e(c["proyecto"])}</p></div>')
    o.append(f'<div class="caja ia"><div class="titulo">La IA en esta semana</div><p>{e(c["ia"])}</p></div>')

    # ── insumos
    o.append('<h2>Insumos</h2>')
    o.append('<h3>Datos que usa el laboratorio</h3><ul>')
    o.append('<li><strong>Comercial Andina</strong>, la base del curso: '
             '<a href="datos.html">ficha de los siete archivos</a></li>')
    for n, u in c["datasets"]:
        o.append(f'<li>{enlace(n, u)}</li>')
    o.append('</ul>')

    casos_rel = [n for n, ws in CASO_SEMANAS.items() if w in ws]
    if casos_rel:
        o.append('<h3>Casos que se apoyan en esta semana</h3><ul>')
        for n in casos_rel:
            nombre = next(cc[1] for cc in CASOS if cc[0] == n)
            o.append(f'<li><a href="caso-{n:02d}.html">Caso {n} \u00b7 {e(nombre)}</a></li>')
        o.append('</ul>')

    mat = MATERIAL.get(w, [])
    her = [h for h in HEREDADO if h["semana"] == str(w)]
    if mat:
        o.append('<h3>Material de apoyo</h3>')
        o.append('<table><thead><tr><th scope="col">Tipo</th><th scope="col">Recurso</th><th scope="col">C\u00f3mo se usa</th></tr></thead><tbody>')
        for tipo, rec, como in mat:
            o.append(f'<tr><td>{e(tipo.capitalize())}</td><td>{recurso_html(rec)}</td><td>{e(como)}</td></tr>')
        o.append('</tbody></table>')
    if her:
        o.append('<h3>Actividades heredadas que se reutilizan</h3>')
        o.append('<table><thead><tr><th scope="col">Actividad</th><th scope="col">Origen</th><th scope="col">Estado</th><th scope="col">Qu\u00e9 cambia</th></tr></thead><tbody>')
        for h in her:
            o.append(f'<tr><td><strong>{e(h["titulo"])}</strong></td><td>{e(h["curso"])}</td><td>{e(h["estado"])}</td><td>{e(h["nota"])}</td></tr>')
        o.append('</tbody></table>')

    if c["lecturas"]:
        o.append('<h3>Lecturas</h3><ul>')
        for t, u, por in c["lecturas"]:
            o.append(f'<li>{enlace(t, u)} \u2014 {e(por)}</li>')
        o.append('</ul>')

    pend = [p for p in PENDIENTES if p["semana"] == w]
    if pend:
        o.append('<div class="caja aviso"><div class="titulo">Pendiente de construir</div><ul>')
        for p in pend:
            o.append(f'<li><strong>{e(p["que"])}</strong> \u2014 {e(p["situacion"])} Fecha l\u00edmite: {e(p["limite"])}.</li>')
        o.append('</ul></div>')

    o.append(navpie(w))
    pagina(f"semana-{w:02d}.html", f"Semana {w} \u00b7 {tema}", f"Semana {w}", "\n".join(o))

# ══════════════════════════════════════════════════════════════
# PORTADA
# ══════════════════════════════════════════════════════════════
def construir_portada():
    o = []
    o.append('<div class="hero">')
    o.append(f'<div class="kicker">{e(CODIGO)} \u00b7 {e(PERIODO)}</div>')
    o.append(f'<h1>{e(CURSO)}</h1>')
    o.append('<p class="bajada">Un curso de decisiones, no de programaci\u00f3n. Diecis\u00e9is semanas para pasar de la pregunta de negocio a una recomendaci\u00f3n defendible, con pandas, scikit-learn y un asistente de IA al que hay que saber encargarle trabajo y verificarle el resultado.</p>')
    o.append('<div class="acciones">'
             '<a class="boton" href="semana-01.html">Empezar por la semana 1</a>'
             '<a class="boton sec" href="calendario.html">Ver el calendario</a>'
             '<a class="boton sec" href="laboratorios.html">Los 16 laboratorios</a></div>')
    o.append('<div class="datos">')
    for v, t in [("16", "semanas"), ("31", "sesiones de 1.5 h"), ("16", "laboratorios en Python"),
                 ("7", "deberes"), ("8", "certificaciones"), ("10", "casos de estudio")]:
        o.append(f'<div><div class="v">{v}</div><div class="e">{e(t)}</div></div>')
    o.append('</div></div>')

    # línea de tiempo del semestre
    o.append('<h2>El semestre de un vistazo</h2>')
    o.append('<div class="timeline">')
    for w in sorted(SEM2):
        tit = html.escape(f"Semana {w} · {SEM2[w][0]}", quote=True)
        o.append(f'<a href="semana-{w:02d}.html" data-b="{BLOQUE_N[w]}" title="{tit}" aria-label="{tit}">{w}</a>')
    o.append('</div>')
    o.append('<div class="timeline-leyenda">')
    vistos = []
    for w in sorted(SEM2):
        if BLOQUE[w] not in vistos:
            vistos.append(BLOQUE[w])
            o.append(f'<span><i style="background:{BLOQUE_COLOR[BLOQUE_N[w]]}"></i>{e(BLOQUE[w])}</span>')
    o.append('</div>')

    o.append('<h2>De qu\u00e9 se trata</h2>')
    o.append('<p>La mayor\u00eda de los an\u00e1lisis no fracasan por un error de c\u00e1lculo: fracasan porque nadie defini\u00f3 la pregunta, porque la comparaci\u00f3n estaba ausente o porque el modelo nunca se midi\u00f3 contra la alternativa de no hacer nada. Este curso ataca eso. Cada semana empieza con una decisi\u00f3n de negocio y termina con evidencia que la sostiene.</p>')
    o.append('<p>Todo el trabajo se hace en Google Colab, sin instalar nada, sobre un mismo negocio: <strong>Comercial Andina</strong>, un distribuidor ecuatoriano con tiendas en cinco ciudades. Los diecis\u00e9is laboratorios trabajan sobre sus datos, as\u00ed que lo que se aprende en una semana se usa en la siguiente.</p>')
    o.append('<p>La inteligencia artificial generativa se usa desde la primera sesi\u00f3n y para todo. Lo que se califica no es el c\u00f3digo sino la calidad del encargo y el rigor con que se verifica lo que el asistente devuelve.</p>')

    o.append('<h2>Las diecis\u00e9is semanas</h2>')
    bloques = {}
    for w in sorted(SEM2):
        bloques.setdefault(BLOQUE[w], []).append(w)
    for nombre, ws in bloques.items():
        b = BLOQUE_N[ws[0]]
        o.append(f'<div class="franja" data-b="{b}"><span class="etq">{e(nombre)}</span>'
                 f'<span class="barra"></span><span class="etq">Semanas {ws[0]}\u2013{ws[-1]}</span></div>')
        o.append('<div class="rejilla c2">')
        for w in ws:
            fechas = " \u00b7 ".join(s["fecha"] for s in CALENDARIO if s.get("curso") == w and s["estado"] == "Clase")
            st = stats_lab(w)
            pie = f'<div class="pie"><span>Lab {w:02d} \u00b7 {st["total"]} celdas</span>' if st else '<div class="pie">'
            ent = next((SESIONES[(w, s["d"])][2] for s in CALENDARIO
                        if s.get("curso") == w and s["estado"] == "Clase"
                        and SESIONES[(w, s["d"])][2] != "\u2014"), None)
            if ent:
                corto = ent.replace("**", "").split(".")[0][:44]
                pie += f'<span>{e(corto)}</span>'
            pie += '</div>'
            o.append(f'<a class="tarjeta" data-b="{b}" href="semana-{w:02d}.html">'
                     f'<div class="n">Semana {w} \u2014 {e(fechas)}</div>'
                     f'<div class="t">{e(SEM2[w][0])}</div>'
                     f'<div class="d">{e(SEM2[w][1])}</div>{pie}</a>')
        o.append('</div>')

    o.append('<h2>Los dos momentos que parten el semestre</h2>')
    o.append('<div class="rejilla c2">')
    o.append('<a class="tarjeta" data-b="3" href="semana-08.html"><div class="n">7 de octubre \u00b7 corte de medio semestre</div>'
             '<div class="t">\u00bfQui\u00e9nes son mis clientes y cu\u00e1nto valen?</div>'
             '<div class="d">Segmentaci\u00f3n RFM+P completa con recomendaci\u00f3n comercial por segmento. Se resuelve con pandas y criterio comercial, antes de que aparezca cualquier modelo predictivo.</div></a>')
    o.append('<a class="tarjeta" data-b="6" href="semana-16.html"><div class="n">7 y 9 de diciembre \u00b7 cierre</div>'
             '<div class="t">Defensa del proyecto integrador</div>'
             '<div class="d">Recomendaci\u00f3n de una p\u00e1gina y cuaderno reproducible, defendidos ante panel: diez minutos de exposici\u00f3n y diez de preguntas.</div></a>')
    o.append('</div>')

    o.append('<h2>Empieza por aqu\u00ed</h2>')
    o.append('<div class="rejilla c3">')
    for arch, nom, desc in [
        ("calendario.html", "Calendario", "Las 31 sesiones con fecha, tema y entrega."),
        ("laboratorios.html", "Laboratorios", "Los 16 cuadernos de Python, con sus ejercicios y r\u00fabrica."),
        ("datos.html", "Comercial Andina", "La base del curso: siete archivos y qu\u00e9 ense\u00f1a cada uno."),
        ("proyecto.html", "Proyecto integrador", "Qu\u00e9 se construye durante el semestre y cu\u00e1ndo se entrega."),
        ("evaluacion.html", "Evaluaci\u00f3n y pol\u00edtica de IA", "C\u00f3mo se califica y qu\u00e9 se le puede pedir al asistente."),
        ("casos.html", "Casos de estudio", "Los diez casos entre los que elige cada grupo."),
        ("datacamp.html", "DataCamp y concurso", "Las certificaciones, sus alternativas y el concurso de XP."),
        ("rubricas.html", "R\u00fabricas", "C\u00f3mo se califica cada entrega, publicado desde el primer d\u00eda."),
        ("apoyo.html", "Apoyo y accesibilidad", "Nivelaci\u00f3n, qu\u00e9 hacer si el grupo se atrasa y protocolo de datos."),
        ("recursos.html", "Recursos y datasets", "Simuladores, datos y material de apoyo."),
        ("docente.html", "Gu\u00eda del docente", "Qu\u00e9 material existe, qu\u00e9 falta y de d\u00f3nde sali\u00f3 cada pieza."),
    ]:
        o.append(f'<a class="tarjeta" href="{arch}"><div class="t">{e(nom)}</div><div class="d">{e(desc)}</div></a>')
    o.append('</div>')
    pagina("index.html", "Portada", "Portada", "\n".join(o))

# ══════════════════════════════════════════════════════════════
# CALENDARIO
# ══════════════════════════════════════════════════════════════
def construir_calendario():
    o = []
    o.append('<div class="kicker">Primer Semestre 2026-2027</div>')
    o.append('<h1>Calendario</h1>')
    o.append('<p class="bajada">Del 17 de agosto al 9 de diciembre de 2026. Lunes y miércoles, hora y media por sesión. Diecisiete semanas de calendario, 31 sesiones de clase.</p>')
    o.append('<div class="caja aviso"><div class="titulo">Dos ajustes del calendario académico</div><ul>'
             '<li><strong>Receso de medio semestre, 9 al 18 de octubre.</strong> Caen el lunes 12 y el miércoles 14. La última clase antes del corte es el 7 de octubre, así que el proyecto de medio semestre se entrega ahí y los grupos tienen doce días para cerrarlo.</li>'
             '<li><strong>Feriado del lunes 2 de noviembre</strong> (Día de Difuntos e Independencia de Cuenca). La semana 11, la del mapa de modelos, se dicta comprimida en una sola sesión el miércoles 4: treinta minutos de concepto y sesenta de taller.</li>'
             '</ul><p>La evaluación docente se abre del 7 al 10 de diciembre; la última clase es el miércoles 9.</p></div>')

    o.append('<table><thead><tr><th scope="col" class="num">Sesión</th><th scope="col" class="num">Fecha</th><th scope="col">Día</th>'
             '<th scope="col" class="num">Semana</th><th scope="col">Tema</th><th scope="col">Entrega</th></tr></thead><tbody>')
    for s in CALENDARIO:
        if s["estado"] in ("FERIADO", "RECESO"):
            o.append(f'<tr class="receso"><td class="num">—</td><td class="num">{e(s["fecha"])}</td><td>{e(s["dia"])}</td>'
                     f'<td class="num">—</td><td colspan="2">{e(s["estado"])} · {e(s["obs"])}</td></tr>')
            continue
        w = s["curso"]
        t, det, ent = SESIONES[(w, s["d"])]
        cls = ' class="hito"' if (w == 8 and s["d"] == "M") or w == 16 else ''
        ent_txt = "" if ent == "—" else ent.replace("**", "")
        o.append(f'<tr{cls}><td class="num">{s["ses"]}</td><td class="num">{e(s["fecha"])}</td><td>{e(s["dia"])}</td>'
                 f'<td class="num"><a href="semana-{w:02d}.html">{w}</a></td><td>{e(t)}</td><td>{e(ent_txt)}</td></tr>')
    o.append('</tbody></table>')

    o.append('<h2>Entregables por fecha</h2>')
    o.append('<table><thead><tr><th scope="col" class="num">Fecha</th><th scope="col" class="num">Semana</th><th scope="col">Entregable</th></tr></thead><tbody>')
    for s in CALENDARIO:
        if s["estado"] != "Clase":
            continue
        w = s["curso"]
        t, det, ent = SESIONES[(w, s["d"])]
        if ent == "—":
            continue
        cls = ' class="hito"' if w in (8, 16) else ''
        o.append(f'<tr{cls}><td class="num">{e(s["fecha"])}</td><td class="num">{w}</td><td>{e(ent.replace("**", ""))}</td></tr>')
    o.append('</tbody></table>')

    o.append('<h2>Certificaciones DataCamp</h2>')
    o.append('<table><thead><tr><th scope="col" class="num">Semana</th><th scope="col" class="num">Fecha límite</th><th scope="col">Curso</th></tr></thead><tbody>')
    for w, f, curso in DATACAMP:
        o.append(f'<tr><td class="num">{w}</td><td class="num">{e(f)}</td><td>{e(curso)}</td></tr>')
    o.append('</tbody></table>')
    o.append('<p>Ocho certificaciones repartidas en siete semanas. La semana 5 lleva dos porque fusiona agrupación y combinación. '
             'Las alternativas aceptadas, las instrucciones de registro y las reglas del concurso de XP están en la página de <a href="datacamp.html">DataCamp y concurso</a>.</p>')
    pagina("calendario.html", "Calendario", "Calendario", "\n".join(o))

# ══════════════════════════════════════════════════════════════
# PROYECTO
# ══════════════════════════════════════════════════════════════
def construir_proyecto():
    o = []
    o.append('<div class="kicker">Hilo conductor del semestre</div>')
    o.append('<h1>Proyecto integrador</h1>')
    o.append('<p class="bajada">Cada grupo elige una empresa real a la que tenga acceso y la acompaña durante todo el semestre: diagnostica cómo usa hoy sus datos, identifica oportunidades, construye una solución y la defiende ante un panel.</p>')

    o.append('<h2>Las cinco fases</h2>')
    o.append('<div class="rejilla c2">')
    fases = [
        ("Fase 1 · Semanas 1 a 4", "Elegir y diagnosticar",
         "Selección de la empresa, entrevistas con quienes toman decisiones, diagnóstico de madurez analítica y ficha de análisis del problema elegido. Termina con la propuesta formal del proyecto."),
        ("Fase 2 · Semanas 4 a 7", "Construir la base",
         "Bitácora de limpieza, tabla de indicadores cuadrada contra una cifra de control y tablero que contesta una pregunta gerencial."),
        ("Fase 3 · Semana 8", "Conocer al cliente",
         "Segmentación RFM+P con recomendación comercial por segmento. Es el corte de medio semestre y el primer entregable grande."),
        ("Fase 4 · Semanas 9 a 14", "Decidir y predecir",
         "Diseño experimental, journey map con puntos de captura de datos, clasificación del problema en su familia de modelo, pronóstico y recomendación de focalización."),
        ("Fase 5 · Semanas 15 y 16", "Responder y defender",
         "Auditoría de sesgos del propio modelo, consultoría cruzada entre grupos, cuaderno reproducible y defensa ante panel."),
    ]
    for n, t, d in fases:
        o.append(f'<div class="tarjeta"><div class="n">{e(n)}</div><div class="t">{e(t)}</div><div class="d">{e(d)}</div></div>')
    o.append('</div>')

    o.append('<h2>Qué se entrega y cuándo</h2>')
    o.append('<table><thead><tr><th scope="col" class="num">Fecha</th><th scope="col" class="num">Semana</th><th scope="col">Entregable</th></tr></thead><tbody>')
    for s in CALENDARIO:
        if s["estado"] != "Clase":
            continue
        w = s["curso"]
        t, det, ent = SESIONES[(w, s["d"])]
        if ent == "—":
            continue
        cls = ' class="hito"' if w in (8, 16) else ''
        o.append(f'<tr{cls}><td class="num">{e(s["fecha"])}</td><td class="num"><a href="semana-{w:02d}.html">{w}</a></td><td>{e(ent.replace("**", ""))}</td></tr>')
    o.append('</tbody></table>')

    o.append('<h2>El cuaderno reproducible</h2>')
    o.append('<p>El entregable final no es una presentación: es un cuaderno que otra persona pueda abrir y ejecutar de principio a fin sin preguntarte nada. Debe cumplir cinco condiciones:</p><ol>'
             '<li>Corre completo, en orden, sin errores y con las salidas guardadas.</li>'
             '<li>Los datos se leen desde una fuente accesible, no desde una ruta de tu computadora.</li>'
             '<li>Cada modelo se reporta junto a su línea base y con el error expresado en unidades de negocio.</li>'
             '<li>Incluye la bitácora de prompts: qué se le pidió al asistente y qué se verificó de la respuesta.</li>'
             '<li>Declara las limitaciones y los sesgos conocidos, incluidos los que no pudiste resolver.</li></ol>')

    o.append('<h2>La recomendación de una página</h2>')
    o.append('<p>Acompaña al cuaderno y se escribe con la conclusión primero: qué hay que hacer, por qué, cuánto vale y qué pasa si el supuesto principal no se cumple. Nunca en orden cronológico del análisis.</p>')
    pagina("proyecto.html", "Proyecto integrador", "Proyecto", "\n".join(o))

# ══════════════════════════════════════════════════════════════
# EVALUACIÓN
# ══════════════════════════════════════════════════════════════
def construir_evaluacion():
    o = []
    o.append('<div class="kicker">Reglas del curso</div>')
    o.append('<h1>Evaluación y política de IA</h1>')
    o.append('<p class="bajada">La inteligencia artificial generativa se puede usar para todo. Lo que se evalúa es otra cosa: qué tan bien encargas el trabajo y con qué rigor verificas lo que recibes.</p>')

    o.append('<h2>Distribución de la nota</h2>')
    o.append('<table><thead><tr><th scope="col">Componente</th><th scope="col" class="num">Peso</th><th scope="col">Qué incluye</th></tr></thead><tbody>')
    for comp, peso, det in EVALUACION:
        o.append(f'<tr><td><strong>{e(comp)}</strong></td><td class="num">{e(peso)}</td><td>{e(det)}</td></tr>')
    o.append('</tbody></table>')

    o.append('<h2>Política de uso de IA generativa</h2>')
    o.append('<table><thead><tr><th scope="col">Regla</th><th scope="col">Qué significa</th></tr></thead><tbody>')
    for regla, det in POLITICA_IA:
        o.append(f'<tr><td><strong>{e(regla)}</strong></td><td>{e(det)}</td></tr>')
    o.append('</tbody></table>')

    o.append('<div class="caja ia"><div class="titulo">La bitácora de prompts</div>'
             '<p>Es un archivo del repositorio del grupo que crece toda la semana. Cada entrada tiene tres campos: qué le pediste al asistente, qué te devolvió y qué comprobaste antes de usarlo. '
             'Una bitácora con veinte entradas y ninguna verificación vale menos que una con cinco entradas verificadas.</p></div>')

    o.append('<h2>Qué cuenta como deshonestidad académica</h2>')
    o.append('<ul>'
             '<li>Entregar un resultado del asistente que no puedes explicar ni defender.</li>'
             '<li>Omitir el prompt que generó una parte sustancial de la entrega.</li>'
             '<li>Reportar un número que no sale de ejecutar tu propio cuaderno.</li>'
             '<li>Presentar como propio el trabajo de otro grupo, con o sin asistente de por medio.</li>'
             '<li>Usar una fuente, un cuaderno ajeno o un fragmento de c\u00f3digo de internet sin citarlo.</li>'
             '<li>Reutilizar un trabajo entregado en otro curso sin declararlo y sin acuerdo previo con el docente.</li>'
             '<li>Presentar como reales datos inventados o p\u00fablicos. Trabajar con datos inventados es aceptable; '
             'decir que vienen de una empresa cuando no es as\u00ed, no.</li>'
             '</ul>')
    o.append('<p>El <a href="apoyo.html">protocolo de datos del proyecto</a> completa esta secci\u00f3n: qu\u00e9 se puede '
             'extraer de la empresa, qu\u00e9 se anonimiza antes de subirlo al repositorio y qu\u00e9 no entra nunca en un '
             'asistente de IA.</p>')

    o.append('<h2>Los dos ejercicios de código con error incrustado</h2>')
    o.append('<p>En las semanas 4 y 14 el docente entrega un fragmento generado por IA que contiene un fallo silencioso: no lanza error, devuelve un resultado plausible y está mal. '
             'El grupo tiene que encontrarlo, explicar por qué falla y estimar cuánto habría costado si ese número llegaba a un informe. Es la evaluación más directa de si el curso funcionó.</p>')
    pagina("evaluacion.html", "Evaluación y política de IA", "Evaluación", "\n".join(o))

# ══════════════════════════════════════════════════════════════
# CASOS
# ══════════════════════════════════════════════════════════════
def construir_casos():
    o = []
    o.append('<div class="kicker">Proyecto grupal</div>')
    o.append('<h1>Casos de estudio</h1>')
    o.append('<p class="bajada">Cada grupo puede trabajar sobre la empresa que consiga o tomar uno de estos casos, que vienen con dataset, contexto y fases definidas. Se diferencian por el reto técnico, no por el tema.</p>')
    o.append('<div class="caja aviso"><div class="titulo">Ajuste obligatorio antes de repartirlos</div>'
             '<p>Estos casos vienen del seminario de Python, donde el entregable final era una API en FastAPI más un tablero en Streamlit. '
             'En este curso el entregable es un cuaderno reproducible: al adoptarlos hay que sustituir la API por una función documentada dentro del cuaderno y dejar el tablero como opcional.</p></div>')
    o.append('<table><thead><tr><th scope="col" class="num">#</th><th scope="col">Caso</th><th scope="col">Dominio</th><th scope="col">Técnica principal</th><th scope="col">Reto específico</th><th scope="col" class="num">Semanas</th><th scope="col">Uso en el curso</th></tr></thead><tbody>')
    for n, nombre, dominio, tecnica, reto, uso in CASOS:
        cls = ' class="hito"' if uso.startswith("Adoptado") else ''
        sem = CASO_SEMANAS.get(n, [])
        sem_html = " ".join(f'<a href="semana-{x:02d}.html">{x}</a>' for x in sem) or '<span class="etiqueta avi">sin semana</span>'
        o.append(f'<tr{cls}><td class="num">{n}</td><td><a href="caso-{n:02d}.html"><strong>{e(nombre)}</strong></a></td><td>{e(dominio)}</td>'
                 f'<td>{e(tecnica)}</td><td>{e(reto)}</td><td class="num">{sem_html}</td><td>{e(uso)}</td></tr>')
    o.append('</tbody></table>')
    o.append('<div class="caja aviso"><div class="titulo">Cuatro casos piden técnicas que este curso ya no enseña</div>'
             '<p>El rediseño dejó fuera las series de tiempo y el procesamiento de texto no estructurado. Los casos 5 (sismicidad) y 10 (Stack Overflow) se apoyan en series de tiempo, '
             'el 6 (reseñas de Amazon) en texto libre y el 4 (movilidad de Nueva York) en análisis geoespacial. Un grupo los puede tomar, pero tiene que saber que esa parte la resuelve por su cuenta '
             'y que el curso no la va a sostener.</p></div>')
    o.append('<h2>Las cinco fases de un caso</h2>')
    o.append('<ol>'
             '<li><strong>Comprensión del dominio.</strong> Investigar el negocio y formular hipótesis antes de abrir los datos.</li>'
             '<li><strong>Preparación y exploración.</strong> Resolver los problemas de calidad del dataset y justificar cada decisión por escrito.</li>'
             '<li><strong>Modelado.</strong> Comparar al menos dos alternativas con la métrica que corresponda a la decisión, siempre contra una línea base.</li>'
             '<li><strong>Producto analítico.</strong> Cuaderno reproducible con la función de decisión documentada y el tablero de apoyo.</li>'
             '<li><strong>Comunicación.</strong> Recomendación de una página y defensa de diez minutos ante panel.</li>'
             '</ol>')
    pagina("casos.html", "Casos de estudio", "Casos", "\n".join(o))

# ══════════════════════════════════════════════════════════════
# DATACAMP
# ══════════════════════════════════════════════════════════════
def construir_datacamp():
    horas = sum(r[5] for r in DATACAMP_RUTA)
    semanas = sorted({r[1] for r in DATACAMP_RUTA})
    o = []
    o.append('<div class="kicker">Trabajo autónomo</div>')
    o.append('<h1>DataCamp y concurso de XP</h1>')
    o.append(f'<p class="bajada">Ocho certificaciones obligatorias, unas {horas} horas repartidas en {len(semanas)} semanas. '
             'Cada una refuerza la semana en la que se entrega. Y durante todo el semestre corre un concurso: gana quien acumule más XP.</p>')

    o.append('<div class="caja entrega"><div class="titulo">Cómo se acredita</div>'
             '<p>Subiendo a D2L el certificado o la captura de pantalla del <em>Statement of Accomplishment</em>, con la fecha visible. '
             'Las certificaciones son parte de los deberes semanales y sí afectan la nota; el concurso no.</p></div>')

    o.append('<h2>Certificaciones obligatorias</h2>')
    o.append('<table><thead><tr><th scope="col" class="num">#</th><th scope="col" class="num">Semana</th>'
             '<th scope="col" class="num">Fecha límite</th><th scope="col">Curso</th><th scope="col" class="num">Horas</th></tr></thead><tbody>')
    for n, w, f, curso, url, hrs, alt in DATACAMP_RUTA:
        o.append(f'<tr><td class="num">{n}</td><td class="num"><a href="semana-{w:02d}.html">{w}</a></td>'
                 f'<td class="num">{e(f)}</td><td>{enlace(curso, url)}</td><td class="num">{hrs}</td></tr>')
    o.append(f'<tr><td class="num">—</td><td class="num">—</td><td class="num">—</td><td><strong>Total</strong></td><td class="num"><strong>{horas}</strong></td></tr>')
    o.append('</tbody></table>')
    o.append('<p>La semana 5 lleva dos certificaciones porque fusiona agrupación y combinación de tablas. Conviene empezarla en la semana 4.</p>')

    o.append('<h2>Alternativas aceptadas</h2>')
    o.append('<p>Si ya completaste un curso obligatorio antes de que empiece el semestre, o si prefieres profundizar en otra dirección, '
             'puedes sustituirlo por alguna de estas alternativas. La sustitución se avisa por escrito antes de la fecha límite correspondiente.</p>')
    o.append('<table><thead><tr><th scope="col">Curso obligatorio</th><th scope="col">Alternativas aceptadas</th></tr></thead><tbody>')
    for n, w, f, curso, url, hrs, alt in DATACAMP_RUTA:
        alts = ' · '.join(enlace(a, u) for a, u in alt)
        o.append(f'<tr><td>{e(curso)}</td><td>{alts}</td></tr>')
    o.append('</tbody></table>')
    nom, url, por = DATACAMP_SUGERIDO
    o.append(f'<div class="caja"><div class="titulo">Curso sugerido, no obligatorio</div><p>{enlace(nom, url)} — {e(por)}</p></div>')

    o.append('<h2>Cómo registrarte</h2>')
    o.append('<p>El curso tiene un grupo propio en DataCamp. Al entrar por el enlace del grupo, tu cuenta queda con acceso completo a la plataforma '
             'mientras dure el semestre, y tu progreso y tus XP se ven en el marcador del curso.</p>')
    o.append(f'<div class="caja entrega"><div class="titulo">Enlace de invitación al grupo</div>'
             f'<p><a href="{html.escape(DATACAMP_LINK, quote=True)}">{e(DATACAMP_LINK)}</a></p></div>')
    o.append('<ol>')
    for t, d in DATACAMP_PASOS:
        o.append(f'<li><strong>{e(t)}.</strong> {e(d)}</li>')
    o.append('</ol>')
    o.append('<div class="caja aviso"><div class="titulo">Si algo falla</div>'
             '<p>Si el enlace dice que la invitación expiró o que el grupo está lleno, escríbeme antes de la siguiente clase: '
             'no es tu problema, es de licencias. No compres una suscripción personal.</p></div>')

    o.append('<h2>Concurso de XP</h2>')
    o.append('<p>Durante todo el semestre corre un concurso interno: <strong>gana quien acumule más XP en DataCamp</strong>, y hay un premio.</p>')
    o.append('<table><thead><tr><th scope="col">Regla</th><th scope="col">Detalle</th></tr></thead><tbody>')
    for t, d in CONCURSO:
        o.append(f'<tr><td><strong>{e(t)}</strong></td><td>{e(d)}</td></tr>')
    o.append('</tbody></table>')
    o.append('<p>El concurso no afecta la nota. Lo que sí afecta la nota son las ocho certificaciones obligatorias, que son parte de los deberes semanales.</p>')
    pagina("datacamp.html", "DataCamp y concurso", "DataCamp", "\n".join(o))

# ══════════════════════════════════════════════════════════════
# RECURSOS
# ══════════════════════════════════════════════════════════════
def construir_recursos():
    o = []
    o.append('<div class="kicker">Material de apoyo</div>')
    o.append('<h1>Recursos y datasets</h1>')
    o.append('<p class="bajada">Todo lo que se usa en clase, en un solo lugar. Los simuladores y los casos viven dentro de este sitio; los datasets grandes se leen desde su URL para que Colab funcione sin subir archivos, y los archivos pequeños de ejercicio están en el repositorio.</p>')

    o.append('<h2>Simuladores interactivos</h2>')
    o.append('<p>Seis páginas para manipular un parámetro y ver qué le pasa al modelo. Se usan en la sesión conceptual del lunes, proyectados, antes de escribir código.</p>')
    o.append('<table><thead><tr><th scope="col">Simulador</th><th scope="col" class="num">Semana</th><th scope="col">Qué muestra</th></tr></thead><tbody>')
    for arch, w, desc in SIMULADORES:
        o.append(f'<tr><td><a href="simuladores/{e(arch)}">{e(arch)}</a></td><td class="num"><a href="semana-{w:02d}.html">{w}</a></td><td>{e(desc)}</td></tr>')
    o.append('</tbody></table>')

    o.append('<h2>Datasets del curso</h2>')
    vistos = set()
    o.append('<table><thead><tr><th scope="col">Dataset</th><th scope="col" class="num">Semanas</th><th scope="col">Fuente</th></tr></thead><tbody>')
    porset = {}
    for w in sorted(SEMANAS):
        for n, u in SEMANAS[w]["datasets"]:
            porset.setdefault((n, u), []).append(w)
    for (n, u), ws in porset.items():
        semanas = ", ".join(f'<a href="semana-{w:02d}.html">{w}</a>' for w in ws)
        fuente = enlace(u, u) if u.startswith("http") else enlace("archivo del repositorio", u)
        o.append(f'<tr><td><strong>{e(n)}</strong></td><td class="num">{semanas}</td><td>{fuente}</td></tr>')
    o.append('</tbody></table>')

    o.append('<h2>Los laboratorios del curso</h2>')
    o.append('<p>Diecis\u00e9is cuadernos propios, escritos para este curso y verificados uno por uno: cada cual '
             'se ejecuta de principio a fin sin errores sobre los datos de Comercial Andina. '
             'El \u00edndice completo est\u00e1 en <a href="laboratorios.html">Laboratorios</a>.</p>')
    o.append('<table><thead><tr><th scope="col" class="num">Semana</th><th scope="col">Laboratorio</th>'
             '<th scope="col" class="num">Celdas</th><th scope="col">Archivo</th></tr></thead><tbody>')
    for w in sorted(SEM2):
        st = stats_lab(w)
        if not st:
            continue
        tm = (SESIONES.get((w, "M")) or SESIONES.get((w, "L")))[0]
        o.append(f'<tr><td class="num"><a href="lab-{w:02d}.html">{w}</a></td><td>{e(tm)}</td>'
                 f'<td class="num">{st["total"]}</td><td><a href="labs/lab_{w:02d}.ipynb">lab_{w:02d}.ipynb</a></td></tr>')
    o.append('</tbody></table>')

    o.append('<h2>Cuadernos heredados del seminario de Python</h2>')
    o.append('<table><thead><tr><th scope="col" class="num">Semana</th><th scope="col">Recurso</th><th scope="col">Contenido</th></tr></thead><tbody>')
    for w in sorted(MATERIAL):
        for tipo, rec, como in MATERIAL[w]:
            if tipo != "cuaderno":
                continue
            o.append(f'<tr><td class="num"><a href="semana-{w:02d}.html">{w}</a></td><td>{recurso_html(rec)}</td><td>{e(como)}</td></tr>')
    o.append('</tbody></table>')

    o.append('<h2>Certificaciones DataCamp</h2>')
    o.append('<table><thead><tr><th scope="col" class="num">Semana</th><th scope="col" class="num">Fecha límite</th><th scope="col">Curso</th><th scope="col" class="num">Horas</th></tr></thead><tbody>')
    for n, w, f, curso, url, hrs, alt in DATACAMP_RUTA:
        o.append(f'<tr><td class="num"><a href="semana-{w:02d}.html">{w}</a></td><td class="num">{e(f)}</td><td>{enlace(curso, url)}</td><td class="num">{hrs}</td></tr>')
    o.append('</tbody></table>')
    o.append('<p>Registro, alternativas aceptadas y reglas del concurso de XP en la página de <a href="datacamp.html">DataCamp y concurso</a>.</p>')

    o.append('<h2>Entorno de trabajo</h2>')
    o.append('<p>Todo corre en <strong>Google Colab</strong>: no hay que instalar nada y basta una cuenta de Google. Las librerías del curso son <code>pandas</code>, <code>numpy</code>, '
             '<code>matplotlib</code>, <code>seaborn</code>, <code>plotly</code>, <code>scikit-learn</code>, <code>statsmodels</code> y <code>scipy</code>, todas preinstaladas en Colab.</p>')
    o.append('<p>Cada cuaderno abre con la misma celda de configuración, que fija la semilla aleatoria en 42 para que los resultados sean reproducibles entre computadoras.</p>')
    o.append('<div class="caja aviso"><div class="titulo">De dónde vienen los cuadernos</div>'
             '<p>Los cuadernos <code>clase_NN.ipynb</code> viven en el repositorio del seminario de Python, <code>CursoPythonDatos_2026</code>, y hay que adaptarlos antes de dictarlos: '
             'esa adaptación es parte del trabajo pendiente que lista la <a href="docente.html">guía del docente</a>. Los simuladores y los casos ya están copiados dentro de este sitio.</p></div>')
    pagina("recursos.html", "Recursos y datasets", "Recursos", "\n".join(o))

# ══════════════════════════════════════════════════════════════
# GUÍA DEL DOCENTE
# ══════════════════════════════════════════════════════════════
def construir_docente():
    o = []
    o.append('<div class="kicker">Uso interno</div>')
    o.append('<h1>Guía del docente</h1>')
    o.append('<p class="bajada">De dónde salió cada pieza del curso, qué se puede dictar mañana y qué hay que escribir antes de llegar a esa semana.</p>')

    o.append('<h2>Las tres fuentes</h2>')
    o.append('<div class="rejilla c3">')
    for v, t in [("53", "actividades heredadas de los cursos 202410 y 202520 en D2L"),
                 ("29", "recursos del seminario de Python: cuadernos, casos y simuladores"),
                 ("16", "semanas del cronograma nuevo que hay que cubrir")]:
        o.append(f'<div class="tarjeta cifra"><div class="valor">{v}</div><div class="etq">{e(t)}</div></div>')
    o.append('</div>')

    o.append('<h2>Lo que falta construir</h2>')
    o.append('<table><thead><tr><th scope="col" class="num">Para el</th><th scope="col" class="num">Semana</th><th scope="col">Qué falta</th><th scope="col">Situación</th></tr></thead><tbody>')
    for p in sorted(PENDIENTES, key=lambda x: x["orden"]):
        o.append(f'<tr><td class="num">{e(p["limite"])}</td><td class="num"><a href="semana-{p["semana"]:02d}.html">{p["semana"]}</a></td>'
                 f'<td><strong>{e(p["que"])}</strong></td><td>{e(p["situacion"])}</td></tr>')
    o.append('</tbody></table>')

    o.append('<h2>Lo que no hay que rehacer</h2>')
    o.append('<ol>'
             '<li><strong>El cuaderno de RFM+P sobre SuperStore</strong> del curso 202410. Ya está en Colab y ya exige adjuntar el prompt final usado con el asistente, que es exactamente la política de IA de este curso.</li>'
             '<li><strong>El caso de segmentación de retail</strong> del seminario de Python: fases, criterio del codo y silueta, y perfiles de negocio ya escritos. Ojo: es RFM sin margen y corre sobre otro dataset.</li>'
             '<li><strong>La rúbrica del entregable intermedio</strong> del seminario, que incluye la bitácora obligatoria de uso de IA. Encaja tal cual con el corte de la semana 8.</li>'
             '<li><strong>El enunciado de predicción de abandono laboral</strong> del curso 202520: comparativa de modelos, tabla de métricas y una página de recomendaciones. Es el mejor enunciado heredado.</li>'
             '<li><strong>La sesión final de storytelling y defensa</strong> del seminario: pirámide de Minto, preguntas del tribunal y rúbrica. Cubre la semana 16 completa.</li>'
             '</ol>')

    o.append('<h2>Material del seminario de Python que no entra</h2>')
    o.append('<table><thead><tr><th scope="col">Recurso</th><th scope="col">Motivo</th></tr></thead><tbody>')
    for rec, mot in MATERIAL_FUERA:
        o.append(f'<tr><td><code>{e(rec)}</code></td><td>{e(mot)}</td></tr>')
    o.append('</tbody></table>')

    o.append('<h2>Actividades heredadas que se descartan</h2>')
    desc = [h for h in HEREDADO if h["estado"] == "DESCARTAR"]
    o.append(f'<p>Son {len(desc)} de las 53. Diez son duplicados entre los dos semestres, no material malo: cuando la misma actividad existe en las dos versiones se conserva la que trae enunciado.</p>')
    o.append('<table><thead><tr><th scope="col">Actividad</th><th scope="col">Origen</th><th scope="col">Motivo</th></tr></thead><tbody>')
    for h in desc:
        o.append(f'<tr><td>{e(h["titulo"])}</td><td>{e(h["curso"])}</td><td>{e(h["nota"])}</td></tr>')
    o.append('</tbody></table>')

    o.append('<h2>Para publicar en D2L</h2>')
    o.append('<p>La <a href="d2l_bienvenida.html">p\u00e1gina de bienvenida</a> est\u00e1 lista para pegarse como '
             'contenido HTML en el aula virtual: presenta el curso, el proyecto y las reglas de uso de IA sin depender '
             'de este sitio.</p>')
    o.append('<h2>Documentos de trabajo</h2>')
    o.append('<ul>'
             '<li><code>Propuesta En Construcción/ADM2003_cronograma_python_ia_v2.md</code> — el cronograma con la tabla del sílabo y el plan de sesiones.</li>'
             '<li><code>Propuesta En Construcción/ADM2003_calendario_S1_2026_LunMie.md</code> y su <code>.xlsx</code> — el calendario con fechas, en el formato de la guía del profesor.</li>'
             '<li><code>Propuesta En Construcción/MAPEO_material_a_semanas_v2.md</code> — de dónde sale el material de cada semana.</li>'
             '<li><code>Material Actual/Actividades Organizadas/</code> — las 53 actividades heredadas, con enunciado y adjuntos.</li>'
             '<li><code>sitio/_datos/contenido.py</code> — el contenido docente de este sitio. Se edita ahí y se regenera con <code>generar_sitio.py</code>.</li>'
             '</ul>')
    pagina("docente.html", "Guía del docente", "Docente", "\n".join(o))


# ══════════════════════════════════════════════════════════════
# MARKDOWN MÍNIMO (para las páginas de caso)
# ══════════════════════════════════════════════════════════════
def md_a_html(texto):
    """Conversor suficiente para los archivos de caso: encabezados, listas,
    tablas, negritas, código, enlaces y separadores."""
    out, i = [], 0
    lineas = texto.split("\n")
    en_lista = None
    ultimo_h = [1]   # el h1 lo pone la página, no el markdown
    def cerrar():
        nonlocal en_lista
        if en_lista:
            out.append(f"</{en_lista}>")
            en_lista = None
    def inline(t):
        t = html.escape(t, quote=False)
        t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
        t = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", t)
        t = re.sub(r"`([^`]+)`", r"<code>\1</code>", t)
        t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', t)
        return t
    while i < len(lineas):
        ln = lineas[i].rstrip()
        if not ln.strip():
            cerrar(); i += 1; continue
        if ln.startswith("|") and i + 1 < len(lineas) and re.fullmatch(r"\|[\s\-:|]+\|", lineas[i+1].strip() or "x"):
            cerrar()
            cabecera = [c.strip() for c in ln.strip("|").split("|")]
            out.append("<table><thead><tr>" + "".join(f'<th scope="col">{inline(c)}</th>' for c in cabecera) + "</tr></thead><tbody>")
            i += 2
            while i < len(lineas) and lineas[i].strip().startswith("|"):
                celdas = [c.strip() for c in lineas[i].strip().strip("|").split("|")]
                out.append("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in celdas) + "</tr>")
                i += 1
            out.append("</tbody></table>"); continue
        m = re.match(r"^(#{1,4})\s+(.*)$", ln)
        if m:
            cerrar()
            n = min(len(m.group(1)) + 1, 4)
            n = min(n, ultimo_h[0] + 1)      # nunca saltar un nivel
            ultimo_h[0] = n
            out.append(f"<h{n}>{inline(m.group(2))}</h{n}>"); i += 1; continue
        if re.match(r"^\s*[-*]\s+", ln):
            if en_lista != "ul": cerrar(); out.append("<ul>"); en_lista = "ul"
            txt = re.sub(r"^\s*[-*]\s+", "", ln)
            out.append("<li>" + inline(txt) + "</li>"); i += 1; continue
        if re.match(r"^\s*\d+[.)]\s+", ln):
            if en_lista != "ol": cerrar(); out.append("<ol>"); en_lista = "ol"
            txt = re.sub(r"^\s*\d+[.)]\s+", "", ln)
            out.append("<li>" + inline(txt) + "</li>"); i += 1; continue
        if re.fullmatch(r"-{3,}", ln.strip()):
            cerrar(); i += 1; continue
        if ln.startswith(">"):
            cerrar(); out.append('<div class="caja"><p>' + inline(ln.lstrip("> ")) + '</p></div>'); i += 1; continue
        cerrar(); out.append(f"<p>{inline(ln)}</p>"); i += 1
    cerrar()
    return "\n".join(out)

# ══════════════════════════════════════════════════════════════
# ÍNDICE DE LABORATORIOS
# ══════════════════════════════════════════════════════════════
def construir_laboratorios():
    o = []
    o.append('<div class="kicker">Los diecis\u00e9is talleres</div>')
    o.append('<h1>Laboratorios</h1>')
    o.append('<p class="bajada">Un cuaderno de Python por semana, todos sobre el mismo negocio. '
             'Corren en Google Colab sin instalar nada y est\u00e1n verificados: cada uno se ejecuta de '
             'principio a fin sin errores antes de publicarse.</p>')
    tot = sum(stats_lab(w)["total"] for w in sorted(SEM2) if stats_lab(w))
    cod = sum(stats_lab(w)["code"] for w in sorted(SEM2) if stats_lab(w))
    o.append('<div class="rejilla c4">')
    for v, t in [("16", "cuadernos"), (str(tot), "celdas en total"), (str(cod), "celdas de c\u00f3digo"),
                 ("48", "ejercicios")]:
        o.append(f'<div class="tarjeta cifra"><div class="valor">{v}</div><div class="etq">{e(t)}</div></div>')
    o.append('</div>')

    o.append('<div class="caja ia"><div class="titulo">C\u00f3mo se trabaja</div>'
             '<p>Cada laboratorio abre con el mismo bloque de configuraci\u00f3n, fija la semilla en 42 y localiza '
             'la carpeta de datos sola. Los tres ejercicios van siempre en el mismo orden: uno <strong>guiado</strong> '
             'que se resuelve con el docente, un <strong>desaf\u00edo</strong> que queda para casa y un '
             '<strong>reto de quince minutos</strong> que se comparte en pantalla.</p></div>')

    o.append('<h2>Los cuadernos</h2>')
    o.append('<table><thead><tr><th scope="col" class="num">Sem</th><th scope="col">Laboratorio</th>'
             '<th scope="col">Qu\u00e9 se construye</th><th scope="col" class="num">Celdas</th>'
             '<th scope="col">Archivos</th></tr></thead><tbody>')
    for w in sorted(SEM2):
        st = stats_lab(w)
        if not st:
            continue
        tm = (SESIONES.get((w, "M")) or SESIONES.get((w, "L")))[0]
        cls = ' class="hito"' if w in (8, 16) else ''
        o.append(f'<tr{cls}><td class="num"><a href="semana-{w:02d}.html">{w}</a></td>'
                 f'<td><a href="lab-{w:02d}.html"><strong>{e(tm)}</strong></a></td>'
                 f'<td>{e(SEMANAS[w]["proyecto"][:120])}</td>'
                 f'<td class="num">{st["total"]}</td>'
                 f'<td><a href="labs/lab_{w:02d}.ipynb">.ipynb</a></td></tr>')
    o.append('</tbody></table>')

    o.append('<h2>La r\u00fabrica com\u00fan</h2>')
    o.append('<p>Todos los entregables de laboratorio se califican con los mismos cinco criterios. '
             'El tercero es el que m\u00e1s gente pierde.</p>')
    o.append('<table><thead><tr><th scope="col">Criterio</th><th scope="col">Qu\u00e9 se mira</th>'
             '<th scope="col" class="num">Peso</th></tr></thead><tbody>')
    for crit, det, peso in RUBRICA:
        o.append(f'<tr><td><strong>{e(crit)}</strong></td><td>{e(det)}</td><td class="num">{e(peso)}</td></tr>')
    o.append('</tbody></table>')
    pagina("laboratorios.html", "Laboratorios", "Laboratorios", "\n".join(o))

# ══════════════════════════════════════════════════════════════
# GUÍA DE CADA LABORATORIO
# ══════════════════════════════════════════════════════════════
def construir_lab(w):
    c = SEMANAS[w]
    st = stats_lab(w)
    if not st:
        return
    b = BLOQUE_N[w]
    ses = [s for s in CALENDARIO if s.get("curso") == w and s["estado"] == "Clase"]
    mi = next((s for s in ses if s["d"] == "M"), ses[0] if ses else None)
    tm = SESIONES.get((w, "M")) or SESIONES.get((w, "L"))
    o = []
    o.append(f'<div class="kicker">Laboratorio {w:02d} \u00b7 {e(BLOQUE[w])}</div>')
    o.append(f'<h1>{e(tm[0])}</h1>')
    o.append(f'<p class="bajada">{e(tm[1])}</p>')
    o.append('<div class="meta">')
    if mi:
        o.append(f'<span>{e(mi["fecha"])}</span>')
    o.append('<span>90 minutos</span>')
    o.append(f'<span>{st["total"]} celdas \u00b7 {st["code"]} de c\u00f3digo</span>')
    o.append(f'<span><a href="semana-{w:02d}.html">Semana {w}</a></span>')
    o.append('</div>')

    o.append(f'<p><a class="boton" href="labs/lab_{w:02d}.ipynb">Descargar el cuaderno</a> '
             f'{colab(f"labs/lab_{w:02d}.ipynb")} '
             f'<a class="boton sec" href="datos.html">Ver los datos</a></p>')

    o.append('<h2>Qu\u00e9 vas a poder hacer al terminar</h2><ul>')
    for x in c["objetivos"]:
        o.append(f'<li>{e(x)}</li>')
    o.append('</ul>')

    o.append('<h2>Pasos</h2><ol class="pasos">')
    for x in c["practica"]:
        o.append(f'<li>{e(x)}</li>')
    o.append('</ol>')

    ejs = ejercicios_del_lab(w)
    if ejs:
        o.append('<h2>Ejercicios</h2>')
        nombres = {"guiado": ("Guiado \u00b7 se resuelve en clase", "inf"),
                   "desafio": ("Desaf\u00edo \u00b7 queda para casa", "avi"),
                   "reto": ("Reto \u00b7 quince minutos en clase", "ok")}
        for tipo, titulo, desc in ejs:
            etq, cls = nombres.get(tipo, ("Ejercicio", ""))
            o.append(f'<div class="sesion lab"><div class="cab">'
                     f'<span class="etiqueta {cls}">{e(etq)}</span></div>'
                     f'<h3>{e(titulo)}</h3><p>{e(desc)}</p></div>')

    o.append(f'<div class="caja trampa"><div class="titulo">\u26a0\ufe0f La trampa que este laboratorio desarma</div>'
             f'<p>{e(c["trampa"])}</p></div>')

    ent = next((SESIONES[(w, s["d"])][2] for s in ses if SESIONES[(w, s["d"])][2] != "\u2014"), None)
    if ent:
        o.append(f'<h2>Entregable</h2><div class="caja entrega"><div class="titulo">Se sube al cierre del taller</div>'
                 f'<p>{e(ent.replace("**", ""))}</p></div>')

    o.append(f'<div class="caja ia"><div class="titulo">Uso del asistente en este laboratorio</div><p>{e(c["ia"])}</p></div>')

    o.append('<h2>C\u00f3mo se califica</h2>')
    o.append('<table><thead><tr><th scope="col">Criterio</th><th scope="col">Qu\u00e9 se mira</th>'
             '<th scope="col" class="num">Peso</th></tr></thead><tbody>')
    for crit, det, peso in RUBRICA:
        o.append(f'<tr><td><strong>{e(crit)}</strong></td><td>{e(det)}</td><td class="num">{e(peso)}</td></tr>')
    o.append('</tbody></table>')

    prev = f'<a href="lab-{w-1:02d}.html"><span class="e">Laboratorio anterior</span><span class="t">Lab {w-1:02d} \u00b7 {e((SESIONES.get((w-1,"M")) or SESIONES.get((w-1,"L")) or ("","",""))[0][:34])}</span></a>' if w > 1 else '<a href="laboratorios.html"><span class="e">\u00cdndice</span><span class="t">Todos los laboratorios</span></a>'
    sig = f'<a class="sig" href="lab-{w+1:02d}.html"><span class="e">Siguiente</span><span class="t">Lab {w+1:02d} \u00b7 {e((SESIONES.get((w+1,"M")) or SESIONES.get((w+1,"L")) or ("","",""))[0][:34])}</span></a>' if w < 16 else '<a class="sig" href="laboratorios.html"><span class="e">\u00cdndice</span><span class="t">Todos los laboratorios</span></a>'
    o.append(f'<div class="nav-pie">{prev}{sig}</div>')
    pagina(f"lab-{w:02d}.html", f"Laboratorio {w:02d} \u00b7 {tm[0]}", f"Lab {w:02d}", "\n".join(o))

# ══════════════════════════════════════════════════════════════
# FICHA DE DATOS
# ══════════════════════════════════════════════════════════════
ARCHIVOS_DATOS = [
 ("ventas.csv", "80 515", "factura_id, fecha, cliente_id, sucursal_id, producto_id, cantidad, precio_unitario, descuento, es_devolucion",
  "La tabla principal, con los problemas de calidad sin resolver. Es el material de las semanas 2 a 4."),
 ("ventas_limpias.csv", "79 482", "Las mismas nueve columnas",
  "La versi\u00f3n ya depurada. Se entrega despu\u00e9s de la semana 4 para que nadie arrastre su propia limpieza el resto del curso."),
 ("clientes.csv", "1 800", "cliente_id, razon_social, ciudad, tipo_cliente, fecha_alta, canal_captacion",
  "El 22 % son mayoristas: de ah\u00ed sale la bimodalidad del ticket. El 9 % de las ciudades est\u00e1 mal escrito."),
 ("productos.csv", "74", "producto_id, nombre, categoria, subcategoria, costo_unitario, precio_lista",
  "Trae costo y precio, que es lo que permite calcular margen y la P del an\u00e1lisis RFM+P."),
 ("sucursales.csv", "6", "sucursal_id, ciudad, canal, fecha_apertura, metros_cuadrados",
  "Cinco tiendas y el canal en l\u00ednea. Es la tabla peque\u00f1a con la que se practican las uniones."),
 ("marketing_mensual.csv", "31", "mes, inversion_radio, inversion_digital, inversion_volantes, ventas_mes",
  "Serie mensual de inversi\u00f3n y ventas. Es el insumo de la regresi\u00f3n de las semanas 12 y 13."),
 ("experimento_reactivacion.csv", "1 800", "cliente_id, tipo_cliente, ciudad, grupo, convirtio",
  "Campa\u00f1a de reactivaci\u00f3n con una paradoja de Simpson dentro. Es el laboratorio de la semana 9."),
]

FENOMENOS = [
 ("Ticket bimodal", 3, "El 22 % de clientes mayoristas arrastra la media a 180,49 mientras la mediana se queda en 30,22. La media no describe a ning\u00fan cliente real."),
 ("Problemas de calidad", 4, "7,8 % de l\u00edneas sin cliente, 1,1 % de duplicados exactos, dos formatos de fecha conviviendo, cantidades negativas que no son devoluciones y precios con un cero de m\u00e1s."),
 ("Uniones que duplican", 5, "El padr\u00f3n de contactos tiene m\u00e1s de una fila por cliente. Unir sin mirar la cardinalidad infla la facturaci\u00f3n un 25 %."),
 ("Estacionalidad", 6, "Diciembre pesa un 30 % m\u00e1s que un mes medio y febrero un 18 % menos. Se ve en cuanto se grafica la serie."),
 ("Estructura RFM", 8, "Clientes VIP, leales, en riesgo y perdidos aparecen solos al calcular recencia, frecuencia y monto. El 31 % lleva m\u00e1s de 180 d\u00edas sin comprar."),
 ("Paradoja de Simpson", 9, "En el experimento, el control convierte m\u00e1s que el tratamiento globalmente, pero pierde en minoristas y en mayoristas por separado."),
 ("Relaci\u00f3n publicidad\u2013ventas", 12, "La inversi\u00f3n en volantes correlaciona con las ventas del mes, con la trampa de la causalidad inversa incluida."),
 ("Abandono desbalanceado", 14, "Un tercio de los clientes abandona. La exactitud de un modelo que dice que nadie se va ya supera el 65 %."),
]

def construir_datos():
    o = []
    o.append('<div class="kicker">La base del curso</div>')
    o.append('<h1>Comercial Andina</h1>')
    o.append('<p class="bajada">Un distribuidor ecuatoriano con tiendas en Quito, Guayaquil, Cuenca, Manta y Loja, '
             'm\u00e1s canal en l\u00ednea. Los diecis\u00e9is laboratorios trabajan sobre este mismo negocio: lo que '
             'limpias en la semana 4 es lo que modelas en la 14.</p>')
    o.append('<div class="caja"><div class="titulo">Datos sint\u00e9ticos, fen\u00f3menos reales</div>'
             '<p>Los datos los genera <code>datos/generar_datos.py</code> con semilla fija, as\u00ed que son id\u00e9nticos '
             'en cualquier computadora. Son sint\u00e9ticos, pero est\u00e1n construidos para que aparezcan de forma natural '
             'los fen\u00f3menos que cada semana necesita ense\u00f1ar. Nada de lo que vas a encontrar es un accidente.</p></div>')

    o.append('<h2>Los siete archivos</h2>')
    o.append('<table><thead><tr><th scope="col">Archivo</th><th scope="col" class="num">Filas</th>'
             '<th scope="col">Columnas</th><th scope="col">Para qu\u00e9 sirve</th></tr></thead><tbody>')
    for arch, filas, cols, uso in ARCHIVOS_DATOS:
        o.append(f'<tr><td><a href="datos/{arch}"><code>{e(arch)}</code></a></td><td class="num">{e(filas)}</td>'
                 f'<td><code>{e(cols)}</code></td><td>{e(uso)}</td></tr>')
    o.append('</tbody></table>')

    o.append('<h2>Qu\u00e9 ense\u00f1a cada fen\u00f3meno</h2>')
    o.append('<div class="rejilla c2">')
    for nombre, w, desc in FENOMENOS:
        o.append(f'<a class="tarjeta" data-b="{BLOQUE_N[w]}" href="semana-{w:02d}.html">'
                 f'<div class="n">Semana {w}</div><div class="t">{e(nombre)}</div>'
                 f'<div class="d">{e(desc)}</div></a>')
    o.append('</div>')

    o.append('<h2>C\u00f3mo se cargan</h2>')
    o.append('<p>Todos los laboratorios abren con el mismo bloque, que encuentra la carpeta de datos sola tanto '
             'en local como en Colab:</p>')
    o.append('<pre style="background:var(--papel-3);border:1px solid var(--linea);border-radius:var(--r-s);'
             'padding:1rem;overflow-x:auto;font-size:.82rem;font-family:var(--mono)">'
             'from pathlib import Path\n'
             'import pandas as pd\n\n'
             'CANDIDATOS = [Path("../datos"), Path("datos"), Path("sitio/datos")]\n'
             'DATOS = next((p for p in CANDIDATOS if p.exists()), None)\n\n'
             'ventas = pd.read_csv(DATOS / "ventas.csv")\n'
             'clientes = pd.read_csv(DATOS / "clientes.csv")</pre>')

    o.append('<h2>Regenerarlos</h2>')
    o.append('<p>Si hace falta cambiar el tama\u00f1o del negocio o la intensidad de alg\u00fan fen\u00f3meno, se edita '
             '<code>datos/generar_datos.py</code> y se ejecuta. El script imprime al final las comprobaciones did\u00e1cticas: '
             'si la bimodalidad o la paradoja de Simpson dejan de aparecer, avisa.</p>')
    pagina("datos.html", "Comercial Andina \u00b7 la base del curso", "Datos", "\n".join(o))

# ══════════════════════════════════════════════════════════════
# PÁGINA POR CASO
# ══════════════════════════════════════════════════════════════
def construir_caso(n):
    arch = CASO_ARCHIVO[n]
    ruta = os.path.join(SITIO, "casos", arch)
    if not os.path.exists(ruta):
        return
    texto = open(ruta, encoding="utf-8").read()
    fila = next(c for c in CASOS if c[0] == n)
    _, nombre, dominio, tecnica, reto, uso = fila
    semanas = CASO_SEMANAS.get(n, [])
    o = []
    o.append(f'<div class="kicker">Caso {n} \u00b7 {e(dominio)}</div>')
    o.append(f'<h1>{e(nombre)}</h1>')
    o.append('<div class="meta">')
    o.append(f'<span>{e(tecnica)}</span><span>Reto: {e(reto)}</span>')
    o.append(f'<span class="{"destacado" if uso.startswith("Adoptado") else ""}">{e(uso)}</span>')
    o.append('</div>')
    if semanas:
        o.append('<div class="caja ia"><div class="titulo">Semanas del curso que sostienen este caso</div><p>')
        o.append(" \u00b7 ".join(f'<a href="semana-{w:02d}.html">Semana {w} \u00b7 {e(SEM2[w][0])}</a>' for w in semanas))
        o.append('</p></div>')
    else:
        o.append('<div class="caja aviso"><div class="titulo">Sin semana que lo sostenga</div>'
                 '<p>Este caso usa t\u00e9cnicas que el curso no dicta. Un grupo lo puede tomar, pero esa parte la '
                 'resuelve por su cuenta.</p></div>')
    o.append('<div class="caja aviso"><div class="titulo">Ajuste obligatorio</div>'
             '<p>El caso viene del seminario de Python, donde el entregable era una API en FastAPI m\u00e1s un tablero '
             'en Streamlit. Aqu\u00ed el entregable es un cuaderno reproducible: la API se sustituye por una funci\u00f3n '
             'documentada dentro del cuaderno y el tablero queda como opcional.</p></div>')
    o.append(md_a_html(texto))
    o.append(f'<div class="nav-pie">'
             f'<a href="casos.html"><span class="e">\u00cdndice</span><span class="t">Todos los casos</span></a>'
             f'<a class="sig" href="caso-{(n % 10) + 1:02d}.html"><span class="e">Siguiente</span>'
             f'<span class="t">Caso {(n % 10) + 1}</span></a></div>')
    pagina(f"caso-{n:02d}.html", f"Caso {n} \u00b7 {nombre}", f"Caso {n}", "\n".join(o))


# ══════════════════════════════════════════════════════════════
# RÚBRICAS
# ══════════════════════════════════════════════════════════════
def construir_rubricas():
    o = []
    o.append('<div class="kicker">C\u00f3mo se califica cada cosa</div>')
    o.append('<h1>R\u00fabricas</h1>')
    o.append('<p class="bajada">Los seis instrumentos de evaluaci\u00f3n del curso, con sus criterios y pesos. '
             'Est\u00e1n publicados desde la primera semana a prop\u00f3sito: saber c\u00f3mo se corrige es parte '
             'de saber qu\u00e9 se espera.</p>')
    o.append('<div class="rejilla c3">')
    for nombre, r in RUBRICAS.items():
        o.append(f'<a class="tarjeta" href="#{e(nombre.split(chr(183))[0].strip().lower().replace(" ", "-"))}">'
                 f'<div class="n">{e(r["peso"])}</div><div class="t">{e(nombre)}</div>'
                 f'<div class="d">{e(r["cuando"])}</div></a>')
    o.append('</div>')
    for nombre, r in RUBRICAS.items():
        anc = nombre.split("\u00b7")[0].strip().lower().replace(" ", "-")
        o.append(f'<h2 id="{e(anc)}">{e(nombre)}</h2>')
        o.append(f'<div class="meta"><span class="destacado">{e(r["peso"])}</span><span>{e(r["cuando"])}</span></div>')
        o.append('<table><thead><tr><th scope="col">Criterio</th><th scope="col">Qu\u00e9 se mira</th>'
                 '<th scope="col" class="num">Puntos</th></tr></thead><tbody>')
        for crit, pts, det in r["criterios"]:
            o.append(f'<tr><td><strong>{e(crit)}</strong></td><td>{e(det)}</td><td class="num">{pts}</td></tr>')
        o.append(f'<tr class="hito"><td colspan="2"><strong>Total</strong></td>'
                 f'<td class="num"><strong>{sum(c[1] for c in r["criterios"])}</strong></td></tr>')
        o.append('</tbody></table>')
        o.append(f'<div class="caja"><div class="titulo">Nota</div><p>{e(r["nota"])}</p></div>')
    o.append('<h2>Escala com\u00fan</h2>')
    o.append('<table><thead><tr><th scope="col" class="num">Nivel</th><th scope="col">Qu\u00e9 significa</th>'
             '<th scope="col" class="num">Proporci\u00f3n del criterio</th></tr></thead><tbody>')
    for niv, desc, prop in [
        ("Excelente", "Cumple el criterio y adem\u00e1s anticipa la objeci\u00f3n que le har\u00edan.", "100 %"),
        ("Competente", "Cumple el criterio sin huecos. Es el nivel esperado.", "80 %"),
        ("En desarrollo", "Cumple parcialmente; falta una pieza identificable.", "55 %"),
        ("Insuficiente", "No se puede verificar el criterio con lo entregado.", "25 %"),
        ("Ausente", "El criterio no aparece.", "0 %")]:
        o.append(f'<tr><td class="num"><strong>{e(niv)}</strong></td><td>{e(desc)}</td><td class="num">{e(prop)}</td></tr>')
    o.append('</tbody></table>')
    pagina("rubricas.html", "R\u00fabricas", "R\u00fabricas", "\n".join(o))

# ══════════════════════════════════════════════════════════════
# APOYO Y ACCESIBILIDAD
# ══════════════════════════════════════════════════════════════
def construir_apoyo():
    o = []
    o.append('<div class="kicker">Para que nadie se quede fuera</div>')
    o.append('<h1>Apoyo y accesibilidad</h1>')
    o.append('<p class="bajada">El curso asume cero programaci\u00f3n previa y estudiantes de administraci\u00f3n, '
             'no de ingenier\u00eda. Esta p\u00e1gina re\u00fane lo que existe para cuando algo se complica.</p>')

    o.append('<h2>Si nunca programaste</h2>')
    o.append('<table><thead><tr><th scope="col">Cu\u00e1ndo</th><th scope="col">Qu\u00e9 hacer</th>'
             '<th scope="col">Cu\u00e1nto toma</th></tr></thead><tbody>')
    for cuando, que, tiempo in NIVELACION:
        o.append(f'<tr><td><strong>{e(cuando)}</strong></td><td>{e(que)}</td><td>{e(tiempo)}</td></tr>')
    o.append('</tbody></table>')
    o.append('<div class="caja ia"><div class="titulo">El asistente tambi\u00e9n sirve para esto</div>'
             '<p>Cuando una l\u00ednea de c\u00f3digo no se entiende, p\u00eddele al asistente que la explique '
             'l\u00ednea por l\u00ednea en lenguaje de negocio. Eso s\u00ed cuenta como uso leg\u00edtimo: lo que no '
             'cuenta es entregar c\u00f3digo que no puedes explicar.</p></div>')

    o.append('<h2>Si tu grupo se atrasa</h2>')
    o.append('<p>El proyecto tiene cinco fases encadenadas. Dos son prerrequisito duro: sin ellas no se puede seguir. '
             'Las otras admiten una versi\u00f3n m\u00ednima que mantiene al grupo en carrera.</p>')
    o.append('<table><thead><tr><th scope="col" class="num">Semana</th><th scope="col">Entrega</th>'
             '<th scope="col">Versi\u00f3n m\u00ednima viable</th></tr></thead><tbody>')
    for w, ent, minimo in RUTA_MINIMA:
        duro = "Prerrequisito duro" in minimo
        cls = ' class="hito"' if duro else ''
        o.append(f'<tr{cls}><td class="num"><a href="semana-{w:02d}.html">{w}</a></td>'
                 f'<td><strong>{e(ent)}</strong></td><td>{e(minimo)}</td></tr>')
    o.append('</tbody></table>')
    o.append('<div class="caja aviso"><div class="titulo">Entregas tard\u00edas</div>'
             '<p>Un deber semanal se recibe hasta 48 horas despu\u00e9s con el 70 % del puntaje. Los dos entregables '
             'grandes (semana 8 y semana 16) no admiten retraso, porque el calendario no tiene d\u00f3nde moverlos: '
             'uno cierra contra el receso y el otro contra el fin del semestre. Un grupo que prevea un problema lo '
             'habla antes, no despu\u00e9s.</p></div>')

    o.append('<h2>Accesibilidad</h2>')
    o.append('<table><thead><tr><th scope="col">Aspecto</th><th scope="col">C\u00f3mo se maneja</th></tr></thead><tbody>')
    for asp, como in ACCESIBILIDAD:
        o.append(f'<tr><td><strong>{e(asp)}</strong></td><td>{e(como)}</td></tr>')
    o.append('</tbody></table>')

    o.append('<h2>Protocolo de datos del proyecto</h2>')
    o.append('<p>Cada grupo trabaja diecis\u00e9is semanas con datos de una empresa real. La semana 15 ense\u00f1a '
             'privacidad y gobernanza: el curso se las aplica a s\u00ed mismo desde la semana 1.</p>')
    o.append('<table><thead><tr><th scope="col">Regla</th><th scope="col">Qu\u00e9 implica</th></tr></thead><tbody>')
    for regla, det in PROTOCOLO_DATOS:
        o.append(f'<tr><td><strong>{e(regla)}</strong></td><td>{e(det)}</td></tr>')
    o.append('</tbody></table>')
    o.append('<div class="caja trampa"><div class="titulo">\u26a0\ufe0f Lo que m\u00e1s se olvida</div>'
             '<p>Pegar una tabla real en un asistente de IA para que la explique. En ese momento los datos salieron de '
             'la empresa y del curso. Al asistente se le describe la estructura y se le pegan filas de ejemplo '
             'inventadas, nunca las reales.</p></div>')
    pagina("apoyo.html", "Apoyo y accesibilidad", "Apoyo", "\n".join(o))

# ══════════════════════════════════════════════════════════════
def main():
    os.makedirs(SITIO, exist_ok=True)
    construir_portada()
    construir_calendario()
    construir_proyecto()
    construir_evaluacion()
    construir_casos()
    construir_datacamp()
    construir_recursos()
    construir_docente()
    construir_laboratorios()
    construir_datos()
    construir_rubricas()
    construir_apoyo()
    for w in sorted(SEM2):
        construir_semana(w)
        construir_lab(w)
    for n in sorted(CASO_ARCHIVO):
        construir_caso(n)
    n = len([f for f in os.listdir(SITIO) if f.endswith(".html")])
    print(f"Sitio generado en {SITIO}: {n} páginas HTML.")

if __name__ == "__main__":
    main()
