# -*- coding: utf-8 -*-
"""Piezas de las páginas por parte del caso Carolina: imágenes, láminas y entregables.

Lo importa generar_paginas_d2l.py. Cada parte es una página D2L propia.
"""
import base64, os, html

IMG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "img")


def img(nombre, alt, ancho=760):
    b = base64.b64encode(open(os.path.join(IMG_DIR, nombre), "rb").read()).decode("ascii")
    return (f'<figure class="foto"><img src="data:image/jpeg;base64,{b}" alt="{html.escape(alt)}" '
            f'style="max-width:{ancho}px"></figure>')


IMAGEN = {
    1: ("parte-1-importaciones.jpg", "Patio del puerto con vehículos recién desembarcados y un inspector con su lista."),
    2: ("parte-2-traslados.jpg", "Camión niñera con vehículos saliendo del puerto hacia las agencias."),
    3: ("parte-3-facturacion.jpg", "Facturas de vehículos revisadas con una lupa sobre un escritorio."),
    4: ("parte-4-actas.jpg", "Actas y documentos revisados, uno de ellos aprobado."),
    5: ("parte-5-vin-une-todo.jpg", "El VIN conecta contenedor, aduana, factura, inspección y acta de entrega de un mismo vehículo."),
}


def wire(tipo, lado):
    """Boceto de la lámina en SVG: título, gráfico del tipo pedido y recuadro lateral."""
    R, G, T = "#A6192E", "#d9d9d9", "#6b6b6b"
    g = []
    if tipo == "h":      # barras horizontales
        for i, w in enumerate([250, 150, 120, 70, 40]):
            g.append(f'<rect x="30" y="{92+i*30}" width="{w}" height="18" fill="{R if i==0 else G}"/>')
    elif tipo == "v":    # barras verticales
        for i, h in enumerate([40, 150, 30, 60]):
            g.append(f'<rect x="{40+i*62}" y="{240-h}" width="40" height="{h}" fill="{R if i==1 else G}"/>')
    elif tipo == "s":    # barras apiladas
        for i in range(4):
            y = 240
            for j, h in enumerate([45, 25, 10, 6, 18]):
                col = [R, "#e7a3ad", G, "#bdbdbd", "#8c8c8c"][j]
                g.append(f'<rect x="{40+i*62}" y="{y-h}" width="40" height="{h}" fill="{col}"/>'); y -= h
    elif tipo == "t":    # línea de tiempo por semana
        for i, h in enumerate([80, 30, 140, 20, 12, 25]):
            g.append(f'<rect x="{30+i*42}" y="{240-h}" width="30" height="{h}" fill="{R if i==0 else G}"/>')
    g = "".join(g)
    return (f'<svg class="wire" viewBox="0 0 480 270" width="480" height="270" role="img" aria-label="Boceto de la lámina">'
            f'<rect x="0.5" y="0.5" width="479" height="269" fill="#fff" stroke="#bbb"/>'
            f'<rect x="30" y="24" width="300" height="14" fill="#1e1e1e"/><rect x="30" y="46" width="200" height="10" fill="{G}"/>'
            f'<text x="30" y="80" font-size="11" fill="{T}" font-family="Segoe UI, Arial">Título = la conclusión, no el tema</text>'
            f'{g}<line x1="28" y1="242" x2="300" y2="242" stroke="#999"/>'
            f'<rect x="320" y="90" width="135" height="150" fill="#faf6f7" stroke="#efdfe2"/>'
            f'<text x="330" y="110" font-size="11" fill="{R}" font-family="Segoe UI, Arial" font-weight="bold">{html.escape(lado)}</text>'
            f'<rect x="330" y="122" width="110" height="8" fill="{G}"/><rect x="330" y="138" width="90" height="8" fill="{G}"/><rect x="330" y="154" width="100" height="8" fill="{G}"/>'
            f'<text x="30" y="260" font-size="10" fill="{T}" font-family="Segoe UI, Arial">Fuente: archivo de salidas/ · corte 17/09/2026</text></svg>')


# Lo que cada parte deja en salidas/ y la lámina que genera para la presentación final.
ENTREGA = {
1: dict(archivos=["salidas/etapa-1-importaciones.xlsx: una fila por VIN, sin repetidos",
                  "salidas/etapa-1-respuesta.md: la respuesta a Carolina en cinco líneas",
                  "salidas/lamina-parte-1.png: la lámina de esta parte",
                  "contexto/CONTEXTO.md con las cifras de control de la parte 1"],
        lamina="Lámina 2 de la presentación · Qué tenemos importado",
        grafico="Barras horizontales con los VIN por marca, de mayor a menor, y el número de contenedores como etiqueta de cada barra.",
        lado="Al costado: el total de VIN y de contenedores, y cuántos VIN hubo que limpiar.",
        tipo="h", recuadro="Total y limpieza",
        fuente="salidas/etapa-1-importaciones.xlsx"),
2: dict(archivos=["salidas/etapa-2-ubicacion.xlsx: el estado físico de cada VIN",
                  "salidas/etapa-2-respuesta.md: conteo por estado y la verificación de las 527",
                  "salidas/lamina-parte-2.png: la lámina de esta parte",
                  "contexto/CONTEXTO.md con las reglas de estado y las cifras de control"],
        lamina="Lámina 3 de la presentación · Dónde está cada unidad",
        grafico="Barras verticales con los cuatro estados físicos (en tránsito, en aduana, nacionalizado, en agencia), en porcentaje y en unidades.",
        lado="Al costado: el control de Nexumcorp, cuántas de las 527 «en tránsito» están mal marcadas y dónde están en realidad.",
        tipo="v", recuadro="Control Nexumcorp",
        fuente="salidas/etapa-2-ubicacion.xlsx"),
3: dict(archivos=["salidas/etapa-3-facturacion.xlsx: una fila por VIN con factura vigente",
                  "salidas/etapa-3-correcciones.xlsx: cada VIN corregido, con su razón",
                  "salidas/etapa-3-respuesta.md: conteo por empresa y rarezas",
                  "salidas/lamina-parte-3.png: la lámina de esta parte",
                  "contexto/CONTEXTO.md con cómo anula cada sistema y las cifras de control"],
        lamina="Lámina 4 de la presentación · Qué está facturado y vigente",
        grafico="Barras horizontales con los VIN nuevos con factura vigente por empresa.",
        lado="Al costado: las rarezas para Carolina (refacturas, VIN corregidos, dobles facturas, colores distintos), marcando cuáles tienen impacto contable.",
        tipo="h", recuadro="Rarezas",
        fuente="salidas/etapa-3-facturacion.xlsx"),
4: dict(archivos=["salidas/etapa-4-por-entregar.xlsx: una fila por VIN por entregar, con su estado",
                  "salidas/etapa-4-respuesta.md: conteo por estado y empresa, y las alertas de entregas",
                  "salidas/lamina-parte-4.png: la lámina de esta parte",
                  "contexto/CONTEXTO.md con la definición de por entregar y las cifras de control"],
        lamina="Lámina 5 de la presentación · Qué falta entregar",
        grafico="Barras apiladas: una barra por empresa, dividida por los cinco estados de lo que falta entregar, con «listo para entrega» en rojo.",
        lado="Al costado: las cuatro alertas sobre entregas ya hechas, con su número de casos.",
        tipo="s", recuadro="Alertas de entregas",
        fuente="salidas/etapa-4-por-entregar.xlsx"),
5: dict(archivos=["salidas/Vehiculos_por_entregar_2026-09-18.xlsx: Resumen, Por entregar, Alertas y Base unificada",
                  "salidas/etapa-5-respuesta.md: atrasados, fechas y alertas",
                  "salidas/lamina-parte-5.png: la lámina de esta parte",
                  "salidas/presentacion-comite.pptx: las ocho láminas para el comité",
                  "contexto/PROCESO.md y el script en procesamiento/ para correrlo el próximo lunes"],
        lamina="Lámina 6 de la presentación · Cuándo se entrega",
        grafico="Barras con las unidades por semana de fecha estimada de entrega, con los atrasados en rojo en la primera barra.",
        lado="Al costado: los atrasados por empresa y cuántos días llevan desde la factura.",
        tipo="t", recuadro="Atrasados",
        fuente="salidas/Vehiculos_por_entregar_2026-09-18.xlsx"),
}


# El punto crítico de cada parte: una decisión de negocio, no de código.
# Su respuesta va en la lámina de la parte, en la línea «Lo que decidimos».
CRITICO = {
1: ("¿Cuándo dos filas son el mismo carro?",
    ["El VIN parece una llave perfecta, pero llega escrito de cinco maneras. Si lo limpian de menos, cuentan un carro dos veces. Si lo limpian de más, pueden juntar dos carros distintos.",
     "¿Qué regla de limpieza usarían y cómo comprobarían que no juntaron dos vehículos distintos?",
     "Y antes de contar: ¿un carro que todavía viene en el barco ya es inventario del grupo?"]),
2: ("¿A quién le creen cuando dos fuentes no coinciden?",
    ["Nexumcorp dice «en tránsito». La liquidación de aduana dice que el contenedor ya llegó. El control manual es el que la empresa usa hoy para hablar con sus clientes.",
     "¿Cuál es la fuente de verdad para cada estado y por qué?",
     "¿Qué le cuesta al negocio creerle al control manual? Piensen en el cliente al que le dicen que su carro no ha llegado cuando ya está en la agencia."]),
3: ("¿Hasta dónde se puede corregir un dato sin preguntar?",
    ["Carolina pidió no botar las facturas cuyo chasis no cruza. Antigravity puede proponer correcciones con mucha seguridad, y equivocarse.",
     "¿Qué evidencia necesitan para aceptar que un VIN mal digitado es en realidad otro? ¿Quién debería aprobar esa corrección dentro de la empresa?",
     "Una doble factura vigente tiene impacto contable. ¿A quién se escala y con qué urgencia?"]),
4: ("¿Qué cuenta como entregado?",
    ["Un acta escaneada que nadie ha digitado, ¿es una entrega? Si deciden que no, más de cien clientes que ya manejan su carro reciben una llamada ofreciéndoles una fecha.",
     "¿Qué evidencia es suficiente para dar un carro por entregado?",
     "¿Qué dice del control de las agencias que haya carros entregados sin PDI aprobado o sin factura vigente?"]),
5: ("¿Qué fecha se le puede prometer a un cliente?",
    ["La regla es simple y el comité la aceptó. Pero prometer una fecha que no se cumple cuesta más que prometer una fecha más tarde.",
     "¿Qué supuestos de la regla pueden fallar: el levante en cinco días, el traslado, el PDI, el tiempo que tarda el cliente en venir?",
     "¿Qué harían esta semana con los atrasados y qué dato pedirían para mejorar la regla el próximo lunes?"]),
}


# Desde la parte 2 ya no hay prompts escritos: solo pistas de qué revisar, qué pedir y cómo organizarse.
PISTAS = {
2: dict(revisar=["Abran la liquidación de aduana y comparen cómo viene escrito el número de contenedor con cómo viene en importaciones.",
                 "En las guías de traslado, miren una celda de VIN: ¿cuántos VIN trae, con qué separador y todos tienen 17 caracteres?",
                 "Busquen cómo aparece escrita una misma agencia de destino en varias guías.",
                 "Miren la columna de estado del control de Nexumcorp y pregúntense quién la llena."],
        pedir=["Que primero escriba en contexto/PLAN.md qué archivo une con cuál, por qué campo y con qué regla de fechas decide cada estado. Ustedes lo aprueban antes de ejecutar.",
               "Que les muestre los huérfanos de cada cruce: contenedores sin aduana, VIN de traslados sin pareja, y cómo resolvió los incompletos.",
               "Que calcule el estado solo con fechas y que la comparación con el control de Nexumcorp salga en una tabla aparte.",
               "Que al cerrar actualice CONTEXTO.md con las reglas de estado de esta parte."],
        organizar=["Conversación nueva en Antigravity, que empiece leyendo el correo 2 y el contexto.",
                   "Mientras Antigravity trabaja, quien audita abre la liquidación y los traslados. Quien redacta prepara la respuesta a Carolina."]),
3: dict(revisar=["Abran un CSV del ERP de Toyota en un editor de texto: separador, decimales, tildes.",
                 "Comparen la primera y la última fecha de cada CSV mensual. ¿Se solapan?",
                 "Busquen cómo se ve una factura anulada en cada sistema. No se ve igual en los tres.",
                 "En el reporte de Suzuki, miren qué hay arriba de la tabla y entre las filas."],
        pedir=["Un conteo de filas leídas y descartadas por archivo, con la razón, antes de cruzar nada.",
               "Una tabla con cada VIN que no cruza, el VIN propuesto y la evidencia. Ninguna corrección se aplica sin que ustedes la aprueben.",
               "Que CONTEXTO.md explique cómo anula cada sistema."],
        organizar=["Quien audita revisa cada corrección de VIN contra importaciones antes de aprobarla."]),
4: dict(revisar=["Abran dos o tres PDF de actas: ¿qué datos traen y dónde está el VIN?",
                 "Comparen los nombres de columna y los formatos de fecha de cada hoja del registro de actas.",
                 "En el export de PDI, busquen un VIN con varias inspecciones."],
        pedir=["Que escriba en CONTEXTO.md la definición exacta de «por entregar» del correo antes de calcular.",
               "Una muestra de vehículos por estado para verificar a mano, no solo el total."],
        organizar=["Divídanse: una parte del grupo revisa las entregas ya hechas y la otra la lista por entregar."]),
5: dict(revisar=["Busquen la hoja de feriados en el maestro.",
                 "Relean la regla del correo paso por paso y escríbanla con sus palabras antes de pedir nada."],
        pedir=["Ustedes escriben los prompts. Aseguren días hábiles, el piso del viernes 18, el Resumen con fórmulas y el proceso guardado para el lunes."],
        organizar=["Reserven tiempo para la presentación. Se arma con las láminas que ya tienen."]),
}


def lista(items):
    return "<ul>" + "".join(f"<li>{html.escape(x)}</li>" for x in items) + "</ul>"


def pistas(n):
    p = PISTAS[n]
    return ('<div class="nota"><b>Desde esta parte ya no hay prompts escritos.</b> Ustedes los escriben con estas pistas. '
            'Guarden en salidas/bitacora-ia.md los prompts que usaron.</div>'
            '<h3>Antes de pedir nada, revisen en los archivos</h3>' + lista(p["revisar"]) +
            '<h3>Lo que sus prompts deben pedir</h3>' + lista(p["pedir"]) +
            '<h3>C&oacute;mo organizarse</h3>' + lista(p["organizar"]))


def critico(n):
    q, parrafos = CRITICO[n]
    return (f'<div class="critico"><p class="q">{html.escape(q)}</p>'
            + "".join(f"<p>{html.escape(x)}</p>" for x in parrafos) +
            '<p><b>Discútanlo en grupo antes de cerrar la parte.</b> Su respuesta va en la lámina de esta parte, '
            'en una línea al pie que empiece con «Lo que decidimos».</p></div>')


def entrega(n, P):
    e = ENTREGA[n]
    arch = "".join(f"<li>{html.escape(a)}</li>" for a in e["archivos"])
    cuerpo = (f'<div class="nota"><b>Antes de pasar a la parte siguiente</b> tienen que tener esto en la carpeta. '
              f'Las preguntas de control de esta parte deben cuadrar.</div>'
              f'<ul class="check">{arch}</ul>'
              f'<h3>La l&aacute;mina que generan</h3><p><b>{html.escape(e["lamina"])}</b></p>'
              f'<div class="lamina">{wire(e["tipo"], e["recuadro"])}<div><p><b>Gr&aacute;fico:</b> {html.escape(e["grafico"])}</p>'
              f'<p>{html.escape(e["lado"])}</p><p><b>T&iacute;tulo:</b> la conclusi&oacute;n en una frase, con la cifra. '
              f'&laquo;Estado f&iacute;sico de las unidades&raquo; describe. &laquo;Seis de cada diez unidades ya est&aacute;n en agencia&raquo; informa.</p>'
              f'<p><b>Al pie:</b> «Lo que decidimos», la respuesta del grupo al punto cr&iacute;tico de esta parte, y la fuente.</p></div></div>')
    if n == 1:
        prompt = (f"Con los datos de {e['fuente']}, genera salidas/lamina-parte-1.png en formato 16:9 con fondo blanco. "
                  f"Título escrito como conclusión, no como tema. Gráfico: {e['grafico']} {e['lado']} "
                  "Destaca la cifra clave en rojo. Al pie, una línea que empiece con «Lo que decidimos:» con esta decisión: [la respuesta del grupo al punto crítico], y la fuente con la fecha de corte. "
                  "No uses ninguna cifra que no esté en salidas/. Muéstrame primero el título y la cifra que vas a destacar.")
        cuerpo += f'<p class="prompt-t">Prompt para la l&aacute;mina</p>{P(prompt)}'
    else:
        cuerpo += ('<p><b>El prompt de la l&aacute;mina lo escriben ustedes.</b> Debe decir de qu&eacute; archivo salen los datos, '
                   'qu&eacute; gr&aacute;fico quieren, que el t&iacute;tulo sea la conclusi&oacute;n, qu&eacute; cifra va en rojo y qu&eacute; dice la l&iacute;nea «Lo que decidimos». '
                   'Pidan ver primero el t&iacute;tulo y la cifra antes de que genere la imagen.</p>')
    if n == 5:
        cuerpo += ('<h3>La presentaci&oacute;n completa</h3>'
                   '<p>Con esta l&aacute;mina ya tienen las cinco de contenido. Faltan tres, y las tres las piensan ustedes:</p>'
                   '<ul><li><b>L&aacute;mina 1 · Portada:</b> la pregunta del comit&eacute; y la respuesta en un n&uacute;mero.</li>'
                   '<li><b>L&aacute;mina 7 · Qu&eacute; hacer esta semana:</b> tres acciones, cada una con responsable, fecha y la cifra que la justifica. '
                   'Digan tambi&eacute;n qu&eacute; dejan de hacer para poder hacerlas.</li>'
                   '<li><b>L&aacute;mina 8 · Lo que no sabemos:</b> los supuestos que pueden fallar, el riesgo de cada uno y el dato que pedir&iacute;an para el pr&oacute;ximo lunes.</li></ul>'
                   '<p>Pidan a Antigravity que junte las ocho en <b>salidas/presentacion-comite.pptx</b>, con fondo blanco y ninguna cifra que no est&eacute; en salidas/. '
                   'Revisen que las ocho cuenten una sola historia: si el comit&eacute; solo lee los t&iacute;tulos, debe entender la respuesta y qu&eacute; hacer.</p>')
    return cuerpo
