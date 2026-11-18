# -*- coding: utf-8 -*-
"""Páginas D2L de las semanas 9 y 10 (26 de octubre al 4 de noviembre de 2026).

Semana 9: qué es un modelo (lunes 26), qué es la IA (miércoles 28) y Deber 10 de Teachable Machine.
Semana 10: caso Daniela, seis decisiones con regresión lineal sobre 200 mercados.

Uso: ../../.venv/bin/python generar_d2l.py  -> escribe los HTML y el CSV en ./d2l/
Toda cifra del caso se calcula aquí sobre el CSV. Si cambia el dato, se regenera la página.
Convenciones D2L: un HTML autocontenido por tema, fondo blanco, sin JS, candados CSS,
nombres con guiones, descargas con href relativo y atributo download.
"""
import os
import html as H
import shutil
from pathlib import Path

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from sklearn.dummy import DummyRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[1]
OUT = AQUI / "d2l"
OUT.mkdir(exist_ok=True)

# ---------------------------------------------------------------- datos del caso
FUENTE = RAIZ / "Material Actual/Actividades Organizadas/06_Regresion_y_Pronostico/2024_Regresion_Lineal_Python/adjuntos/Advertising.csv"
CSV = "mercados-bebidas-cumbre.csv"
df = (pd.read_csv(FUENTE)
      .rename(columns={"id": "mercado", "periodico": "prensa"})[["mercado", "tv", "radio", "prensa", "ventas"]])
df.to_csv(OUT / CSV, index=False)

MARGEN = 12          # USD de margen por unidad de Bebidas Cumbre
PRESUPUESTO = 175    # miles de USD para el mercado nuevo
PLAN_A = (150, 25)   # TV, radio de la agencia
PLAN_B = (50, 49)    # radio al tope de lo observado y poca TV: coherente con la etapa 3


def n(x, d=2):
    """Número con coma decimal y punto de miles, como se escribe en Ecuador."""
    s = f"{x:,.{d}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".").replace("-", "\u2212")


def usd(x):
    s = n(abs(x), 0)
    return ("−" if x < 0 else "+") + s


C = {}
corr = df[["tv", "radio", "prensa", "ventas"]].corr()["ventas"]
for m in ["tv", "radio", "prensa"]:
    C[f"r_{m}"] = corr[m]
    fit = smf.ols(f"ventas ~ {m}", df).fit()
    b = fit.params[m]
    C[f"b_{m}"] = b
    C[f"a_{m}"] = fit.params["Intercept"]
    C[f"r2_{m}"] = fit.rsquared
    C[f"p_{m}"] = fit.pvalues[m]
    C[f"u_{m}"] = b * 1000                       # unidades por cada mil USD
    C[f"min_{m}"] = 1000 / (b * 1000)            # margen mínimo por unidad
    C[f"gana_{m}"] = b * 1000 * MARGEN - 1000    # USD por cada mil invertidos con el margen del caso

tr, te = train_test_split(df, test_size=0.25, random_state=42)
base = DummyRegressor().fit(tr[["tv"]], tr.ventas)
C["base_pred"] = base.predict(te[["tv"]])[0]
C["mae_base"] = mean_absolute_error(te.ventas, base.predict(te[["tv"]]))
for nombre, cols in {"tv": ["tv"], "radio": ["radio"], "prensa": ["prensa"],
                     "tvradio": ["tv", "radio"], "tres": ["tv", "radio", "prensa"]}.items():
    lr = LinearRegression().fit(tr[cols], tr.ventas)
    C[f"mae_{nombre}"] = mean_absolute_error(te.ventas, lr.predict(te[cols]))

tres = smf.ols("ventas ~ tv + radio + prensa", df).fit()
dos = smf.ols("ventas ~ tv + radio", df).fit()
C["b3_prensa"] = tres.params["prensa"]
C["p3_prensa"] = tres.pvalues["prensa"]
C["ic3_prensa"] = tres.conf_int().loc["prensa"].tolist()
C["r2_tres"] = tres.rsquared
C["r2_dos"] = dos.rsquared
C["r2a_tres"] = tres.rsquared_adj
C["r2a_dos"] = dos.rsquared_adj
C["dos"] = dos.params
C["corr_radio_prensa"] = df.radio.corr(df.prensa)


def pronostico(tv, radio):
    f = dos.get_prediction(pd.DataFrame({"tv": [tv], "radio": [radio]})).summary_frame(alpha=0.10).iloc[0]
    return f["mean"], f["obs_ci_lower"], f["obs_ci_upper"]


C["A"] = pronostico(*PLAN_A)
C["B"] = pronostico(*PLAN_B)
C["radio_max"] = df.radio.max()
C["tv_max"] = df.tv.max()
pct = lambda a, b: (b - a) / a * 100

# ---------------------------------------------------------------- plantilla
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
.nota{border:1px solid #e3e3e3;border-left:4px solid #A6192E;border-radius:6px;padding:12px 16px;margin:16px 0;background:#fcfcfc}
.nota b{color:#A6192E}
.prompt{background:#f7f7f7;border:1px solid #e1e1e1;border-radius:6px;padding:12px 14px;margin:10px 0 14px;font-family:Consolas,'Courier New',monospace;font-size:14px;white-space:pre-wrap;line-height:1.5}
table{border-collapse:collapse;width:100%;margin:12px 0;font-size:15px}
th,td{border:1px solid #e1e1e1;padding:7px 10px;text-align:left;vertical-align:top}
th{background:#f4f4f4}
td.num,th.num{text-align:right}
.btn{display:inline-block;background:#A6192E;color:#fff !important;text-decoration:none;padding:7px 14px;border-radius:4px;font-size:14px;margin:4px 6px 4px 0}
.check{list-style:none;padding-left:0}
.check li{padding-left:26px;position:relative;margin:4px 0}
.check li:before{content:'';position:absolute;left:2px;top:6px;width:13px;height:13px;border:2px solid #A6192E;border-radius:2px}
.apuesta{border:1px solid #efdfe2;border-radius:6px;padding:12px 16px;margin:18px 0;position:relative}
.apuesta .preg{font-weight:600;margin:0 0 6px}
.apuesta input[type=radio]{position:absolute;opacity:0}
.apuesta label{display:block;border:1px solid #ddd;border-radius:4px;padding:7px 10px;margin:6px 0;cursor:pointer}
.apuesta input:checked + label{border-color:#A6192E;background:#faf6f7}
.apuesta .fb,.apuesta .reveal{display:none}
.apuesta input[type=text]{width:100%;border:1px solid #ccc;border-radius:4px;padding:8px 10px;font-size:15px;font-family:inherit;margin:6px 0}
.apuesta input[type=text]:not(:placeholder-shown) ~ .reveal{display:block}
.fb{margin:8px 0;padding:8px 12px;border-radius:4px;background:#f4f4f4}
.reveal{margin-top:12px}
.etapa{border:1px solid #e3e3e3;border-radius:6px;padding:4px 18px 12px;margin:18px 0}
.etapa h3{color:#A6192E}
.lab{font-size:13px;letter-spacing:.04em;color:#6b6b6b;margin:14px 0 2px;text-transform:uppercase}
.decision{border:2px solid #A6192E;border-radius:6px;padding:10px 16px;margin:14px 0 6px;background:#fff}
.decision p{margin:4px 0}
.decision .q{font-size:18px;font-weight:700;color:#A6192E}
.linea{border-left:3px solid #A6192E;padding:2px 0 2px 14px;margin:10px 0}
.linea p{margin:2px 0}
.linea .anio{font-weight:700;color:#A6192E}
.pie{margin:40px 0 0;padding-top:12px;border-top:1px solid #eee;text-align:right;font-weight:600}
"""


def ent(s):
    """D2L a veces pierde el UTF-8 de los archivos subidos: todo lo no ASCII va como entidad."""
    return s.encode("ascii", "xmlcharrefreplace").decode("ascii")


def pagina(nombre, titulo, serie, sub, secciones, intro=""):
    idx = "".join(f'<li><a href="#s{i}">{t}</a></li>' for i, (t, _) in enumerate(secciones, 1))
    cuerpo = "".join(
        f'<h2 id="s{i}">{t}</h2>{c}<p class="volver"><a href="#indice">&uarr; volver al &iacute;ndice</a></p>'
        for i, (t, c) in enumerate(secciones, 1))
    doc = f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titulo}</title><style>{CSS}</style></head>
<body><header class="cab"><p class="serie">{serie}</p><h1>{titulo}</h1><p class="sub">{sub}</p></header>
<main>{intro}<nav class="indice" id="indice"><p>En esta p&aacute;gina</p><ol>{idx}</ol></nav>
{cuerpo}<p class="pie">Ve al siguiente tema &rarr;</p></main></body></html>"""
    (OUT / nombre).write_text(ent(doc), encoding="utf-8")
    return nombre


P = lambda t: f"<p>{t}</p>"
UL = lambda xs, cls="": f'<ul{f" class={chr(34)}{cls}{chr(34)}" if cls else ""}>' + "".join(f"<li>{x}</li>" for x in xs) + "</ul>"
OL = lambda xs: "<ol>" + "".join(f"<li>{x}</li>" for x in xs) + "</ol>"
NOTA = lambda t: f'<div class="nota">{t}</div>'


def tabla(cab, filas, num=()):
    th = "".join(f'<th{" class=num" if i in num else ""}>{c}</th>' for i, c in enumerate(cab))
    tr_ = "".join("<tr>" + "".join(f'<td{" class=num" if i in num else ""}>{c}</td>' for i, c in enumerate(f)) + "</tr>" for f in filas)
    return f"<table><tr>{th}</tr>{tr_}</table>"


_q = [0]


def apuesta_opciones(pregunta, opciones):
    """Apuesta de opción múltiple: cada opción revela su propia respuesta."""
    k = _q[0]; _q[0] += 1
    css, partes = [], []
    for i, (texto, fb) in enumerate(opciones):
        partes.append(f'<input type="radio" name="q{k}" id="q{k}o{i}"><label for="q{k}o{i}">{texto}</label>')
        css.append(f"#q{k}o{i}:checked ~ .fb-q{k}o{i}{{display:block}}")
    fbs = "".join(f'<div class="fb fb-q{k}o{i}">{fb}</div>' for i, (_, fb) in enumerate(opciones))
    return f'<style>{"".join(css)}</style><div class="apuesta"><p class="preg">{pregunta}</p>{"".join(partes)}{fbs}</div>'


def candado(pregunta, revelado, placeholder="Escribe tu n&uacute;mero antes de seguir"):
    """Candado de texto: la respuesta aparece solo cuando el estudiante escribe algo."""
    return (f'<div class="apuesta"><p class="preg">{pregunta}</p>'
            f'<input type="text" placeholder="{placeholder}"><div class="reveal">{revelado}</div></div>')


SERIE9 = "ADM 2003 &middot; An&aacute;lisis de Datos &middot; Semana 9 &middot; Modelos e inteligencia artificial"
SERIE10 = "ADM 2003 &middot; An&aacute;lisis de Datos &middot; Semana 10 &middot; Regresi&oacute;n lineal"
VIDEO = "https://www.youtube.com/watch?v=Sb8XVheowVQ"
TM = "https://teachablemachine.withgoogle.com/"

# ================================================================ 1. Qué es un modelo (lunes 26)
modelo = [
    ("Un modelo es una simplificaci&oacute;n que sirve", "".join([
        P("La realidad es ca&oacute;tica y llena de ruido. Un modelo es una versi&oacute;n simplificada de esa realidad que nos permite entenderla y usarla a nuestro favor. Un mapa es un modelo: deja fuera texturas y detalles y conserva lo que sirve para llegar. Una partitura tambi&eacute;n: no es la canci&oacute;n, pero permite tocarla igual cada vez."),
        P("Todo modelo busca un equilibrio entre parecerse a la realidad y ser lo bastante simple para usarlo. Si decimos que las aves vuelan, el modelo es simple pero falla con los polluelos, las aves heridas y los ping&uuml;inos. Si a&ntilde;adimos cada excepci&oacute;n, el modelo se vuelve inmanejable. La salida es la probabilidad: la mayor&iacute;a de las aves vuela. Un plato que cae se rompe en el 95 % de los casos, y esa frase es m&aacute;s &uacute;til que la f&iacute;sica completa de la ca&iacute;da."),
        f'<p><a class="btn" href="{VIDEO}" target="_blank">Ver el video de DotCSV &middot; 10 minutos</a></p>',
    ])),
    ("Las tres piezas de todo modelo: datos, par&aacute;metros y error", "".join([
        P("En el video hay posiciones de Marte registradas a ojo en el siglo XVI y la pregunta de qu&eacute; las explica. El modelo geoc&eacute;ntrico pone la Tierra al centro y &oacute;rbitas circulares. Se puede mover el radio de las &oacute;rbitas para acercarse a los datos, pero el error nunca baja lo suficiente. Cop&eacute;rnico pone el Sol al centro y el modelo se vuelve m&aacute;s simple, aunque con c&iacute;rculos perfectos el error sigue ah&iacute;. Kepler, en 1609, cambia los c&iacute;rculos por elipses y el error queda casi en cero."),
        tabla(["Pieza", "Qu&eacute; es", "En el ejemplo de Marte", "En una regresi&oacute;n lineal"], [
            ["Datos", "Las mediciones de la realidad. Cada fila es un punto en un espacio de muchas dimensiones.", "Las posiciones registradas de Marte", "Metros cuadrados y precio de cada casa vendida"],
            ["Par&aacute;metros", "Los valores que el modelo puede mover para ajustarse a los datos.", "El radio de las &oacute;rbitas, la distancia al Sol", "La pendiente y el intercepto de la recta"],
            ["Error", "La distancia entre lo que dice el modelo y lo que dicen los datos.", "La diferencia entre la &oacute;rbita te&oacute;rica y la observada", "La diferencia entre el precio real y el que predice la recta"],
        ]),
        P("Entrenar un modelo es eso: mover los par&aacute;metros hasta que el error sea el m&aacute;s bajo posible. Lo que no se mide no se puede mejorar, y por eso todo modelo empieza declarando c&oacute;mo se mide su error."),
        apuesta_opciones("El modelo geoc&eacute;ntrico nunca lleg&oacute; a error cero, por m&aacute;s que se movieran los radios. &iquest;Qu&eacute; estaba fallando?", [
            ("Faltaban datos de Marte", "No. Con m&aacute;s datos el error se habr&iacute;a medido mejor, pero no habr&iacute;a bajado. El problema estaba en la forma del modelo."),
            ("Los par&aacute;metros estaban mal ajustados", "No del todo. Se pod&iacute;an ajustar los radios, y aun as&iacute; quedaba error. Ning&uacute;n valor de los par&aacute;metros arregla una forma equivocada."),
            ("La forma del modelo era la equivocada", "Exacto. Cuando el error no baja por m&aacute;s que muevas los par&aacute;metros, hay que cambiar el modelo, no seguir ajust&aacute;ndolo. Es lo que hicieron Cop&eacute;rnico y Kepler."),
        ]),
    ])),
    ("La primera recta: el precio de una casa", "".join([
        P("En clase dibujamos una recta que predice el precio de una casa a partir de sus metros cuadrados, mirando el precio de las casas que ya se vendieron. La recta tiene dos par&aacute;metros: la pendiente, que dice cu&aacute;nto sube el precio por cada metro cuadrado adicional, y el intercepto, que es d&oacute;nde corta el eje cuando los metros son cero."),
        P("Ninguna casa cae exactamente sobre la recta. La distancia vertical entre cada casa y la recta es el residuo. La mejor recta es la que hace m&aacute;s peque&ntilde;a la suma de los residuos al cuadrado. Se elevan al cuadrado para que los de arriba no cancelen a los de abajo y para castigar m&aacute;s los errores grandes. Ese m&eacute;todo se llama m&iacute;nimos cuadrados y es el que usa Python cuando ajusta una regresi&oacute;n."),
        NOTA("<b>Lo que hay que retener.</b> Una regresi&oacute;n lineal es un modelo con datos (las casas), par&aacute;metros (pendiente e intercepto) y error (los residuos). Es uno de los modelos m&aacute;s simples y es la base de casi todo lo dem&aacute;s, incluidas las redes neuronales."),
    ])),
    ("Cinco familias de modelos y una sexta que no es modelo", "".join([
        P("Los modelos no se ordenan por algoritmo sino por la pregunta que contestan y la decisi&oacute;n que habilitan."),
        tabla(["Familia", "Qu&eacute; devuelve", "Qu&eacute; contesta", "Ejemplo en Comercial Andina"], [
            ["Pron&oacute;stico", "un n&uacute;mero", "&iquest;cu&aacute;nto?", "cu&aacute;ntas cajas de aceite pide Cuenca en diciembre"],
            ["Propensi&oacute;n", "una probabilidad", "&iquest;qui&eacute;n?", "qu&eacute; clientes dejan de comprar en 90 d&iacute;as"],
            ["Segmentaci&oacute;n", "un grupo", "&iquest;en qu&eacute; grupos?", "qu&eacute; clientes reciben trato distinto"],
            ["Asociaci&oacute;n", "una regla si-entonces", "&iquest;qu&eacute; va con qu&eacute;?", "qu&eacute; productos se ponen juntos en la g&oacute;ndola"],
            ["Optimizaci&oacute;n", "una asignaci&oacute;n", "&iquest;cu&aacute;nto de cada cosa?", "c&oacute;mo se reparte el presupuesto de marketing"],
        ]),
        P("La sexta familia es <b>ninguna</b>. &iquest;Cu&aacute;nto facturamos el mes pasado? no se predice: es un groupby y la respuesta exacta ya existe. Muchas preguntas no necesitan un modelo. Necesitan un reporte, una regla, un experimento o ir a buscar el dato que falta."),
    ])),
    ("Antes del algoritmo: la l&iacute;nea base", "".join([
        P("Todo modelo compite contra la regla simple que ya existe. En Comercial Andina, una regla que dice que nadie devuelve nada acierta en casi todas las ventas, porque las devoluciones son muy pocas."),
        candado("De cada 100 ventas, &iquest;en cu&aacute;ntas acierta la regla de que nadie devuelve nada? Escribe tu apuesta.",
                P("<b>En 97,65 de cada 100.</b> Y encuentra el 0 % de las devoluciones. Acierta casi siempre y no sirve para nada. Por eso la exactitud sola no dice nada: siempre se reporta contra la l&iacute;nea base y en la unidad del negocio.")),
        P("Antes de mirar los datos tambi&eacute;n se aparta una parte para el final, la prueba. Si eliges variables mirando la prueba, la prueba ya no mide nada."),
    ])),
    ("Cu&aacute;nto vale un modelo antes de construirlo", "".join([
        P("El valor de un modelo se calcula, no se describe:"),
        NOTA("<b>Valor anual</b> = decisiones al a&ntilde;o &times; mejora sobre la l&iacute;nea base &times; valor de acertar una vez &minus; costo de construirlo y mantenerlo"),
        P("Tres condiciones sin las cuales el valor es cero: que la predicci&oacute;n llegue antes de la decisi&oacute;n, que cambie la acci&oacute;n y que la organizaci&oacute;n pueda ejecutarla. El mismo modelo de abandono puede perder 6.600 USD al a&ntilde;o o ganar 3.577 USD. No cambia el algoritmo. Cambia que alguien tenga presupuesto para llamar a 300 clientes y la instrucci&oacute;n de hacerlo."),
        tabla(["", "Pregunta", "C&oacute;mo se responde"], [
            ["1", "&iquest;Qu&eacute; se decide?", "verbo, sujeto y frecuencia"],
            ["2", "&iquest;Cu&aacute;l es la l&iacute;nea base?", "calculada, no descrita"],
            ["3", "&iquest;Cu&aacute;nto vale ganarle?", "con la ecuaci&oacute;n y los supuestos escritos"],
        ]),
        P("El algoritmo es la cuarta pregunta, y la m&aacute;s f&aacute;cil."),
    ])),
]
p1 = pagina("semana9-que-es-un-modelo.html", "Qu&eacute; es un modelo y para qu&eacute; sirve", SERIE9,
            "Lunes 26 de octubre &middot; datos, par&aacute;metros, error y la primera recta", modelo)

# ================================================================ 2. Qué es la IA (miércoles 28)
def hito(anio, texto):
    return f'<div class="linea"><p class="anio">{anio}</p><p>{texto}</p></div>'


ia = [
    ("Qu&eacute; es la IA", "".join([
        P("La inteligencia artificial es la capacidad de las m&aacute;quinas para hacer funciones que cre&iacute;amos exclusivas de los humanos: percibir, razonar, aprender, interactuar con el entorno, resolver problemas y tomar decisiones."),
        P("Definirla es m&aacute;s dif&iacute;cil de lo que parece por tres motivos. Las definiciones son vagas. La ciencia ficci&oacute;n nos llen&oacute; la cabeza de robots que no existen. Y hay una paradoja: lo que es f&aacute;cil para nosotros es dif&iacute;cil para una m&aacute;quina, y al rev&eacute;s. La paradoja tiene su propia secci&oacute;n m&aacute;s abajo."),
    ])),
    ("Una historia de casi dos siglos", "".join([
        P("La idea de objetos que piensan es antigua: los griegos ya ten&iacute;an sus or&aacute;culos. La historia moderna empieza con m&aacute;quinas de engranajes."),
        hito("1837 a 1843 &middot; Babbage y Ada Lovelace", "Charles Babbage dise&ntilde;a la m&aacute;quina anal&iacute;tica, una calculadora mec&aacute;nica de engranajes. Ada Lovelace, hija de Lord Byron, traduce un art&iacute;culo sobre ella y a&ntilde;ade sus propias notas: una m&aacute;quina as&iacute; podr&iacute;a resolver cualquier problema si se le da un programa. Es la idea del software, un problema general escrito como instrucciones."),
        hito("Finales del siglo XIX &middot; Ram&oacute;n y Cajal", "Santiago Ram&oacute;n y Cajal observa al microscopio que el cerebro est&aacute; hecho de c&eacute;lulas separadas que se conectan entre s&iacute;, las neuronas. Pensar deja de ser un misterio y pasa a ser un proceso biol&oacute;gico. Sin copiar a la naturaleza no habr&iacute;a IA."),
        hito("1950 &middot; Alan Turing", "Turing ya hab&iacute;a ayudado a descifrar Enigma, el cifrado alem&aacute;n de la Segunda Guerra Mundial. En 1950 propone su prueba: si una persona conversa por escrito con una m&aacute;quina y no puede distinguirla de un humano, la m&aacute;quina se comporta de forma inteligente. Seguimos usando esa idea cada vez que intentamos adivinar si un texto lo escribi&oacute; ChatGPT."),
        hito("1951 a 1959 &middot; las primeras neuronas artificiales", "Marvin Minsky construye con tubos de vac&iacute;o una red que aprende a resolver un laberinto. Frank Rosenblatt crea el perceptr&oacute;n, una neurona electr&oacute;nica. Arthur Samuel acu&ntilde;a el t&eacute;rmino machine learning."),
        hito("1967 y 1980", "Aparece el clasificador de vecinos m&aacute;s cercanos, KNN, que usaremos en este curso. Kunihiko Fukushima crea una red para reconocer im&aacute;genes."),
        hito("Los inviernos de la IA", "Dos veces la emoci&oacute;n super&oacute; a lo que se pod&iacute;a hacer y la investigaci&oacute;n se estanc&oacute;, a mediados de los setenta y a finales de los ochenta. Ya hab&iacute;a modelos complejos. Faltaban computadoras potentes y, sobre todo, datos."),
        hito("1986 &middot; retropropagaci&oacute;n", "Rumelhart, Hinton y Williams publican c&oacute;mo una red puede ajustar sola los par&aacute;metros de miles de neuronas a partir de datos hist&oacute;ricos. A eso le llamamos entrenar. En 1989 una red ya reconoce d&iacute;gitos escritos a mano."),
        hito("1998 a 2012 &middot; internet se llena de datos", "Llegan Google en 1998 y las redes sociales a mediados de los dos mil, y llenamos internet de fotos, incluidas millones de gatos. Con esos datos se entrenan los primeros modelos que reconocen im&aacute;genes a escala. Nace el deep learning: redes neuronales de muchas capas que necesitan much&iacute;simos datos."),
        hito("2016 a hoy", "Una m&aacute;quina le gana al campe&oacute;n de Go en 2016. En 2017 se publica el art&iacute;culo que da origen a ChatGPT, Attention is all you need. Desde 2020 vivimos la era de los grandes modelos de lenguaje, que modelan el mundo a trav&eacute;s del lenguaje."),
    ])),
    ("C&oacute;mo aprende una red a reconocer un 8", "".join([
        P("Una neurona artificial copia a la biol&oacute;gica. Recibe varias entradas, multiplica cada una por un peso, las suma y pasa el resultado por una funci&oacute;n que decide si se activa o no. Los pesos son sus par&aacute;metros."),
        P("Para reconocer un 8 escrito a mano, la imagen se convierte en una matriz de n&uacute;meros: 0 donde el p&iacute;xel es blanco, 1 donde es negro, 0,5 donde es gris. Esa matriz entra a la red. Cada capa se especializa sola en un detalle: una neurona solo mira una curva de arriba, otra solo una esquina. Una curva as&iacute; la tienen el 3, el 6, el 9 y el 0, as&iacute; que esa neurona se activa con todos ellos. Al final se combinan todas las se&ntilde;ales y gana la salida que m&aacute;s se activa: es un 8."),
        NOTA("<b>Es el mismo esquema del lunes.</b> Datos (miles de im&aacute;genes etiquetadas), par&aacute;metros (los pesos de cada neurona) y error (cu&aacute;ntas veces se equivoca). ChatGPT es esto multiplicado por miles de millones de par&aacute;metros."),
    ])),
    ("Qu&eacute; cambia la IA en la empresa", "".join([
        tabla(["Rasgo", "Qu&eacute; significa"], [
            ["Acceso casi universal", "Cualquiera con computadora e internet puede usar modelos. Era m&aacute;s cierto antes: hoy pocos modelos de lenguaje son abiertos, y los que m&aacute;s liberan son los laboratorios chinos."],
            ["Costo marginal cercano a cero", "Lo caro es conseguir los datos, entrenar y dejar el modelo funcionando. En un modelo cl&aacute;sico, cada uso adicional cuesta casi nada. En los modelos de lenguaje cada uso todav&iacute;a se paga, aunque cada vez menos."],
            ["Escala sin rendimientos decrecientes", "En una cocina, el cuarto cocinero aporta menos que el tercero y, si se tropiezan, la producci&oacute;n hasta baja. Un modelo atiende a un cliente o a un mill&oacute;n sin tropezarse."],
            ["Ventaja doble", "Puede dar diferenciaci&oacute;n y liderazgo en costos al mismo tiempo, algo que casi solo logran las tecnolog&iacute;as digitales."],
        ]),
        P("La IA puede hacer tres cosas con los datos. <b>Describir</b> qu&eacute; pas&oacute;, que no necesita IA. <b>Predecir</b> qu&eacute; va a pasar. <b>Prescribir</b> qu&eacute; hacer, es decir, recomendar la acci&oacute;n."),
        P("En el ciclo de expectativas de la IA que vimos en clase, la IA generativa y los modelos fundacionales ya bajaron al punto de desilusi&oacute;n: sabemos lo que pueden y lo que no. En la cima est&aacute;n los agentes, como Antigravity, la IA multimodal y la ingenier&iacute;a de IA. A la IA general, una que resuelva cualquier problema como un humano, Gartner la ubica a m&aacute;s de diez a&ntilde;os."),
    ])),
    ("El mapa de la IA", "".join([
        P("Cuando alguien dice que us&oacute; IA, casi siempre quiere decir que us&oacute; un modelo de lenguaje. La IA es mucho m&aacute;s amplia."),
        tabla(["Rama", "Qu&eacute; hace", "Ejemplo"], [
            ["Aprendizaje supervisado", "Aprende de datos con etiqueta: la respuesta correcta ya se conoce", "Predecir el precio de una casa, detectar fraude"],
            ["Aprendizaje no supervisado", "Encuentra patrones sin etiquetas", "Agrupar clientes parecidos"],
            ["Aprendizaje por refuerzo", "Aprende probando en un entorno y recibiendo premios o castigos", "Un programa que aprende a jugar Go"],
            ["Deep learning", "Redes neuronales de muchas capas", "Reconocer im&aacute;genes y voz"],
            ["Procesamiento del lenguaje", "Clasificar, traducir, responder y generar texto", "ChatGPT, Claude, Gemini"],
        ]),
        P("Por tipo de problema, la IA resuelve visi&oacute;n (reconocer im&aacute;genes), voz (pasar audio a texto y al rev&eacute;s, como hace Whisper), rob&oacute;tica (sensores y actuadores, del carro aut&oacute;nomo a la aspiradora de casa), planificaci&oacute;n y modelos entrenados para un dominio concreto, como detectar fraude con tarjetas o pronosticar el clima."),
    ])),
    ("La paradoja de la camiseta", "".join([
        P("Un compa&ntilde;ero dobl&oacute; un saco en dos segundos y medio. El robot m&aacute;s avanzado que vimos tard&oacute; seis minutos en doblar una camiseta: tom&oacute; una foto, decidi&oacute; de qu&eacute; v&eacute;rtice agarrarla, la sacudi&oacute;, volvi&oacute; a mirar, la extendi&oacute; y reci&eacute;n despu&eacute;s la dobl&oacute;. Con botones, un cierre o una chompa, se pierde."),
        P("Lo f&aacute;cil para nosotros es dif&iacute;cil para una m&aacute;quina, sobre todo en el mundo f&iacute;sico. Y al rev&eacute;s: para una m&aacute;quina es trivial memorizar mil n&uacute;meros de tel&eacute;fono, pero inventar una historia le cuesta much&iacute;simo procesamiento. Por eso los robots de las demostraciones usan platos de pl&aacute;stico."),
    ])),
    ("&iquest;Es IA o no es IA?", "".join([
        P("Dos palabras permiten decidirlo. <b>Autonom&iacute;a</b>: ejecuta tareas en situaciones complejas sin que el usuario la dirija todo el tiempo. <b>Adaptabilidad</b>: mejora lo que hace aprendiendo de la experiencia y de los datos. Si tiene las dos, es IA."),
        apuesta_opciones("Una hoja de c&aacute;lculo que suma y aplica funciones predefinidas a unos datos.", [
            ("Es IA", "No. Hace exactamente lo que le programaste. Si llegan los datos de 2026, alguien tiene que actualizar las f&oacute;rmulas. No aprende ni se adapta."),
            ("No es IA", "Correcto. No es aut&oacute;noma ni adaptable: depende del humano para cualquier cambio."),
        ]),
        apuesta_opciones("Un sistema que predice el precio de una acci&oacute;n ajustando una curva a los precios hist&oacute;ricos y se reajusta solo cada d&iacute;a con los precios nuevos.", [
            ("Es IA", "Correcto. Nadie le program&oacute; la regla de si el d&oacute;lar sube, la acci&oacute;n baja tanto. La aprende de los datos y la recalcula cuando llegan datos nuevos, aunque en una crisis lo har&aacute; con m&aacute;s error."),
            ("No es IA", "Mira otra vez: aprende de los datos hist&oacute;ricos sin que nadie le escriba las reglas. Eso es adaptabilidad."),
        ]),
        apuesta_opciones("Spotify recomend&aacute;ndote canciones seg&uacute;n lo que escuchas.", [
            ("Es IA", "Correcto. Si ma&ntilde;ana aparece un g&eacute;nero que nunca existi&oacute;, igual te lo recomienda si se parece a lo que te gusta. Y si tu gusto cambia, el sistema cambia contigo."),
            ("No es IA, es un algoritmo", "Un algoritmo es solo una serie de pasos, y esos pasos pueden ser IA o no. Este aprende de tus h&aacute;bitos y se adapta, as&iacute; que s&iacute; es IA."),
        ]),
        apuesta_opciones("Un termostato que enciende el aire a las 7:00 porque as&iacute; lo programaste.", [
            ("Es IA", "No. Sigue una regla fija. Si cambias de horario, tienes que reprogramarlo t&uacute;."),
            ("No es IA", "Correcto. Ser autom&aacute;tico no es lo mismo que ser aut&oacute;nomo. Un termostato que aprende a qu&eacute; hora llegas y se ajusta solo, en cambio, s&iacute; ser&iacute;a IA."),
        ]),
    ])),
    ("Lo que sigue: entrenar un modelo con tus manos", "".join([
        P("Para la siguiente clase cada grupo entrena un modelo de verdad con Teachable Machine y lo presenta en vivo. El encargo completo est&aacute; en la p&aacute;gina del Deber 10."),
        tabla(["Grupo", "Tipo de modelo"], [["1", "Imagen"], ["2", "Audio"], ["3", "Posturas"], ["4", "Imagen"], ["5", "Audio"]]),
    ])),
]
p2 = pagina("semana9-que-es-la-ia.html", "Qu&eacute; es la IA y qu&eacute; no lo es", SERIE9,
            "Mi&eacute;rcoles 28 de octubre &middot; historia, empresa, paradoja y la prueba de autonom&iacute;a y adaptabilidad", ia)

# ================================================================ 3. Deber 10 · Teachable Machine
tmach = [
    ("Qu&eacute; hacen", "".join([
        P("En grupo entrenan con Teachable Machine un modelo que resuelva un problema de empresa y lo presentan funcionando en vivo en la clase del mi&eacute;rcoles 4 de noviembre. Teachable Machine es una herramienta de Google que entrena un modelo en el navegador con ejemplos que t&uacute; grabas, sin escribir c&oacute;digo."),
        f'<p><a class="btn" href="{TM}" target="_blank">Abrir Teachable Machine</a></p>',
        tabla(["Grupo", "Tipo de proyecto"], [["1", "Imagen"], ["2", "Audio"], ["3", "Posturas"], ["4", "Imagen"], ["5", "Audio"]]),
        UL(["El problema es de una empresa y alguien hace algo distinto cuando el modelo responde.",
            "El modelo tiene al menos cuatro clases. En audio, el ruido de fondo cuenta como una de ellas.",
            "Funciona en vivo con algo que no usaron al entrenar: otra persona, otro fondo u otra luz.",
            "No vale repetir los ejemplos de clase: si el profesor est&aacute; o no, la botella de alcohol, la tos o la campana."], "check"),
    ])),
    ("Etapa 1 &middot; El problema y la decisi&oacute;n", "".join([
        P("Antes de grabar nada, escriban en una frase qu&eacute; decide la empresa con este modelo. Por ejemplo: cuando la c&aacute;mara de la bodega ve una caja abierta, el supervisor la revisa antes del despacho. Si nadie hace algo distinto con la respuesta, el modelo no vale nada, aunque acierte siempre."),
        P("Elijan un problema que se pueda repetir en condiciones distintas. Un modelo entrenado con una sola luz, un solo fondo y una sola persona suele fallar apenas algo cambia, y en la presentaci&oacute;n les vamos a pedir justo eso."),
    ])),
    ("Etapa 2 &middot; Los datos", "".join([
        P("Graben muchas muestras de cada clase y en condiciones distintas: otra luz, otro fondo, otro &aacute;ngulo, otra persona. El modelo solo aprende lo que le muestran. Equilibren las clases: si una tiene 350 muestras y otra 100, el modelo se inclina hacia la grande."),
        P("En audio, la primera clase es siempre el ruido de fondo, como el aire acondicionado, la calle o gente hablando, porque el modelo compara cada sonido contra ese fondo. En posturas, var&iacute;en la distancia a la c&aacute;mara y la ropa."),
    ])),
    ("Etapa 3 &middot; Entrenar y buscar d&oacute;nde falla", "".join([
        P("Entrenen y prueben el modelo hasta encontrar sus fallas: en los bordes de la imagen, con poca luz, con dos objetos a la vez, con otra voz. Esa lista es parte de la presentaci&oacute;n. Un modelo que dice 50 % y 50 % est&aacute; confundido y les est&aacute; diciendo qu&eacute; datos le faltan."),
        NOTA("<b>Cuidado.</b> Si cierran la pesta&ntilde;a, el modelo se pierde. Guarden el proyecto en Drive desde el men&uacute; de Teachable Machine y, cuando est&eacute; listo, usen Exportar modelo y Subir mi modelo para obtener un enlace que cualquiera puede abrir."),
    ])),
    ("Etapa 4 &middot; La presentaci&oacute;n en vivo", "".join([
        P("Cinco minutos por grupo el mi&eacute;rcoles 4:"),
        OL(["El problema y la decisi&oacute;n que habilita, en una frase.",
            "Las clases y cu&aacute;ntas muestras tiene cada una.",
            "La demostraci&oacute;n en vivo.",
            "D&oacute;nde falla y qu&eacute; datos le agregar&iacute;an.",
            "Cu&aacute;nto valdr&iacute;a para la empresa: cu&aacute;ntas decisiones al a&ntilde;o toca y cu&aacute;nto vale acertar una vez."]),
    ])),
    ("Qu&eacute; entregan", "".join([
        P("Una entrega por grupo en la carpeta <b>Deber 10 &middot; Teachable Machine</b>, hasta el mi&eacute;rcoles 4 de noviembre a las 23:59. Un integrante sube el archivo <b>deber10-grupo-N.pptx</b> con un solo slide: el problema, las cuatro clases, d&oacute;nde falla y la decisi&oacute;n. En el comentario de la entrega pegan el enlace del modelo."),
        tabla(["Criterio", "Puntos"], [
            ["El problema es de empresa y la decisi&oacute;n es clara", "2"],
            ["Cuatro clases o m&aacute;s, con datos variados y equilibrados", "2"],
            ["Funciona en vivo con otra persona, fondo o luz", "3"],
            ["Explican d&oacute;nde falla y qu&eacute; datos faltan", "2"],
            ["Enlace del modelo y slide entregados", "1"],
            ["<b>Total</b>", "<b>10</b>"],
        ], num=(1,)),
    ])),
]
p3 = pagina("deber-10-teachable-machine.html", "Deber 10 &middot; Teachable Machine: un modelo para un problema de empresa", SERIE9,
            "Entrega grupal &middot; presentaci&oacute;n en vivo el mi&eacute;rcoles 4 de noviembre", tmach)

# ================================================================ 4. Caso Daniela (miércoles 4)
d = C["dos"]
A, B = C["A"], C["B"]
gA, gB = A[0] * MARGEN, B[0] * MARGEN
lowA, lowB = A[1] * MARGEN, B[1] * MARGEN


def etapa(num, titulo, pide, hacen, pista, control, decision):
    return (f"Etapa {num} &middot; {titulo}",
            f'<div class="etapa">'
            f'<p class="lab">Lo que pide Daniela</p>{P(pide)}'
            f'<p class="lab">Qu&eacute; hacen</p>{OL(hacen)}'
            f'{pista}{control}'
            f'<div class="decision"><p class="lab">Decisi&oacute;n para el memo</p><p class="q">{decision}</p></div></div>')
    # devuelve (título de sección, cuerpo)


PISTA = lambda t: f'<p class="lab">Pista</p>{P(t)}'

intro_caso = "".join([
    P("Daniela es gerente de marca de Bebidas Cumbre. El viernes presenta al comit&eacute; el plan de medios del a&ntilde;o y tiene seis preguntas que no puede contestar con intuici&oacute;n. Tiene los datos de los 200 mercados donde la marca ya vende: cu&aacute;nto se invirti&oacute; en televisi&oacute;n, radio y prensa, y cu&aacute;nto se vendi&oacute;."),
    f'<p><a class="btn" href="{CSV}" download>Descargar {CSV}</a></p>',
    tabla(["Columna", "Qu&eacute; es", "Unidad"], [
        ["mercado", "Identificador del mercado", "1 a 200"],
        ["tv, radio, prensa", "Inversi&oacute;n en cada medio durante el a&ntilde;o", "miles de USD"],
        ["ventas", "Unidades vendidas en el a&ntilde;o", "miles de unidades"],
    ]),
    NOTA(f"<b>Un dato que vas a necesitar.</b> Cada unidad vendida le deja a Bebidas Cumbre <b>{MARGEN} USD de margen</b>. Una inversi&oacute;n en publicidad se paga si las unidades adicionales por su margen superan lo que cost&oacute;."),
    P("Trabajen en Colab o en Antigravity con su asistente de IA. Cada etapa tiene una pregunta de control con un n&uacute;mero: escr&iacute;banlo antes de abrir la respuesta. Si su n&uacute;mero no cuadra, revisen el prompt y el c&oacute;digo, no copien la cifra. Copien sus prompts en <b>prompts.md</b>."),
])

caso = [
    ("Qu&eacute; es un R&sup2; y c&oacute;mo se lee una recta", "".join([
        P("Una regresi&oacute;n lineal simple devuelve tres n&uacute;meros y cada uno contesta una pregunta distinta."),
        tabla(["N&uacute;mero", "Qu&eacute; contesta", "C&oacute;mo se dice en una reuni&oacute;n"], [
            ["Pendiente", "Cu&aacute;nto cambia lo que se predice por cada unidad adicional de la variable", "Por cada metro cuadrado adicional, el precio de la casa sube 1.200 USD"],
            ["Intercepto", "Cu&aacute;nto vale lo que se predice cuando la variable es cero", "Es d&oacute;nde la recta corta el eje. Solo se lee si hay casas cerca de cero metros, y no las hay"],
            ["R&sup2;", "Qu&eacute; parte de las diferencias entre filas se explica con esa variable", "Los metros cuadrados explican el 70 % de por qu&eacute; unas casas cuestan m&aacute;s que otras"],
        ]),
        P("El R&sup2; va de 0 a 1. Un R&sup2; de 0,70 dice que si conoces los metros cuadrados de una casa, ya entiendes el 70 % de su diferencia de precio con las dem&aacute;s. El 30 % restante depende de otras cosas: el barrio, la vista, el estado de la casa."),
        NOTA("<b>Lo que el R&sup2; no dice.</b> No dice si una inversi&oacute;n se paga, no dice que la variable cause el resultado y no dice cu&aacute;nto se equivoca el modelo en d&oacute;lares. Para decidir hacen falta la pendiente, el margen y el error contra la l&iacute;nea base."),
    ])),
    ("La escalera de hoy", "".join([
        P("Las seis etapas suben la escalera que usamos desde la semana 3. En clase se suben los cuatro escalones con las etapas 1 a 4. En casa, las etapas 5 y 6 revisan dos de ellos con m&aacute;s cuidado."),
        tabla(["Escal&oacute;n", "Pregunta", "Etapa"], [
            ["Descriptivo", "&iquest;Qu&eacute; pas&oacute;?", "1 &middot; Mirar antes de ajustar"],
            ["Diagn&oacute;stico", "&iquest;Por qu&eacute;?", "2 &middot; La recta de la televisi&oacute;n &middot; y 6 en casa"],
            ["Predictivo", "&iquest;Qu&eacute; va a pasar?", "3 &middot; El mercado nuevo &middot; y 5 en casa"],
            ["Prescriptivo", "&iquest;Qu&eacute; hacemos?", "4 &middot; Mover el presupuesto"],
        ]),
    ])),
    *[
        etapa(1, "Mirar antes de ajustar",
              "Antes de hacer cuentas quiero ver qu&eacute; medio tiene que ver con las ventas.",
              ["Hagan tres gr&aacute;ficos de dispersi&oacute;n: ventas contra tv, contra radio y contra prensa.",
               "Calculen la correlaci&oacute;n de cada medio con las ventas."],
              '<p class="lab">Escal&oacute;n descriptivo &middot; un prompt para empezar</p><div class="prompt">Tengo un CSV con inversi&oacute;n en tv, radio y prensa (miles de USD) y ventas (miles de unidades) de 200 mercados. Haz tres gr&aacute;ficos de dispersi&oacute;n de ventas contra cada medio, con fondo blanco, y calcula la correlaci&oacute;n de cada medio con ventas. Expl&iacute;came qu&eacute; ves en cada gr&aacute;fico antes de darme los n&uacute;meros.</div>',
              candado("&iquest;Cu&aacute;l es la correlaci&oacute;n entre prensa y ventas?",
                      P(f"<b>{n(C['r_prensa'])}.</b> Televisi&oacute;n {n(C['r_tv'])}, radio {n(C['r_radio'])}. La televisi&oacute;n dibuja una banda clara que se abre en los mercados grandes. La radio tambi&eacute;n sube, con m&aacute;s dispersi&oacute;n. La prensa es una nube.")),
              "&iquest;Con qu&eacute; medios vale la pena construir una recta y con cu&aacute;l no?"),
        etapa(2, "La recta de la televisi&oacute;n",
              "&iquest;Por qu&eacute; unos mercados venden m&aacute;s que otros? La agencia dice que es la televisi&oacute;n.",
              ["Ajusten una regresi&oacute;n lineal de ventas contra tv.",
               "Anoten pendiente, intercepto y R&sup2;, y escriban cada uno en una frase de negocio.",
               f"Calculen cu&aacute;ntas unidades m&aacute;s acompa&ntilde;an a cada mil d&oacute;lares y cu&aacute;nto margen dejan a {MARGEN} USD por unidad."],
              PISTA("Escal&oacute;n diagn&oacute;stico. Las ventas est&aacute;n en miles de unidades y la inversi&oacute;n en miles de d&oacute;lares: una pendiente de 0,05 son 50 unidades por cada mil d&oacute;lares, no 0,05 unidades."),
              candado("&iquest;Cu&aacute;nto vale el R&sup2; de ventas contra tv?",
                      P(f"<b>{n(C['r2_tv'])}.</b> Pendiente {n(C['b_tv'], 4)}: cada mil d&oacute;lares m&aacute;s en televisi&oacute;n acompa&ntilde;a a {n(C['u_tv'], 1)} unidades m&aacute;s. Intercepto {n(C['a_tv'])}: unas {n(C['a_tv']*1000, 0)} unidades sin televisi&oacute;n.")
                      + P(f"Con {MARGEN} USD por unidad, esas {n(C['u_tv'], 1)} unidades dejan {n(C['u_tv']*MARGEN, 0)} USD por cada mil invertidos. Para que la televisi&oacute;n se pague, cada unidad tendr&iacute;a que dejar al menos {n(C['min_tv'])} USD.")),
              "&iquest;Qu&eacute; dice ese R&sup2; sobre por qu&eacute; unos mercados venden m&aacute;s, y qu&eacute; no dice?"),
        etapa(3, "El mercado nuevo",
              f"Bebidas Cumbre eval&uacute;a entrar a un mercado nuevo. La entrada vale la pena si el margen del primer a&ntilde;o cubre la publicidad. La agencia propone {PLAN_A[0]} mil en televisi&oacute;n y {PLAN_A[1]} mil en radio. Yo propongo {PLAN_B[0]} mil en televisi&oacute;n y {PLAN_B[1]} mil en radio. &iquest;Cu&aacute;nto vender&iacute;amos con cada plan?",
              ["Ajusten una regresi&oacute;n con tv y radio a la vez, con los 200 mercados.",
               "Pronostiquen las ventas de los dos planes.",
               f"Multipliquen las unidades por {MARGEN} USD y comp&aacute;renlas con la publicidad de cada plan."],
              PISTA("Escal&oacute;n predictivo. Las ventas pronosticadas est&aacute;n en miles de unidades y la publicidad en miles de d&oacute;lares: multipliquen antes de comparar."),
              candado("&iquest;Cu&aacute;ntos miles de unidades pronostica el modelo para el plan de la agencia?",
                      P(f"<b>{n(A[0])} miles de unidades.</b> El plan de Daniela: {n(B[0])}. El modelo es ventas = {n(d['Intercept'])} + {n(d['tv'], 4)} &middot; tv + {n(d['radio'], 4)} &middot; radio.")
                      + tabla(["Plan", "Publicidad (miles USD)", "Pron&oacute;stico (miles de unidades)", f"Margen a {MARGEN} USD (miles)"], [
                          [f"Agencia &middot; {PLAN_A[0]} tv, {PLAN_A[1]} radio", n(sum(PLAN_A), 0), n(A[0]), n(gA, 1)],
                          [f"Daniela &middot; {PLAN_B[0]} tv, {PLAN_B[1]} radio", n(sum(PLAN_B), 0), n(B[0]), n(gB, 1)],
                      ], num=(1, 2, 3))
                      + NOTA(f"<b>&iquest;Y si ponemos todo en radio?</b> El modelo nunca vio un mercado con m&aacute;s de {n(C['radio_max'], 1)} mil en radio. Fuera del rango de los datos la recta no sabe nada: puede que la radio se sature.")),
              "&iquest;Con qu&eacute; plan lanzan, o no lanzan? Escriban la frase con los n&uacute;meros."),
        etapa(4, "Mover el presupuesto",
              "Los dos planes venden casi lo mismo y el m&iacute;o cuesta 76 mil menos. &iquest;Por qu&eacute;? Y si tengo mil d&oacute;lares extra, &iquest;en qu&eacute; medio los pongo?",
              ["Ajusten la recta de ventas contra radio y la de ventas contra prensa.",
               f"Armen una tabla con los tres medios: unidades por cada mil d&oacute;lares, R&sup2; y cu&aacute;nto queda de cada mil invertidos a {MARGEN} USD por unidad."],
              PISTA("Escal&oacute;n prescriptivo. P&iacute;danle al asistente la tabla completa y verifiquen una fila a mano con la pendiente."),
              candado("&iquest;Cu&aacute;ntas unidades m&aacute;s acompa&ntilde;an a cada mil d&oacute;lares en radio?",
                      P(f"<b>{n(C['u_radio'], 1)} unidades.</b>")
                      + tabla(["Medio", "Unidades por 1.000 USD", "R&sup2;", f"Queda de cada 1.000 USD a {MARGEN} USD"], [
                          ["Televisi&oacute;n", n(C['u_tv'], 1), n(C['r2_tv']), usd(C['gana_tv'])],
                          ["Radio", n(C['u_radio'], 1), n(C['r2_radio']), usd(C['gana_radio'])],
                          ["Prensa", n(C['u_prensa'], 1), n(C['r2_prensa']), usd(C['gana_prensa'])],
                      ], num=(1, 2, 3))
                      + P("El R&sup2; contesta cu&aacute;nto de las diferencias entre mercados se explica. La pendiente contesta cu&aacute;nto rinde un d&oacute;lar. No son la misma pregunta.")),
              "&iquest;D&oacute;nde van los pr&oacute;ximos mil d&oacute;lares y por qu&eacute; no al medio con el R&sup2; m&aacute;s alto?"),
        etapa(5, "&iquest;Confiamos en el pron&oacute;stico?",
              "Antes de firmar el lanzamiento quiero saber cu&aacute;nto se equivoca el modelo. Acepto un pron&oacute;stico si se equivoca en menos de 2 mil unidades por mercado, en promedio. &iquest;Y mi plan aguanta el peor caso?",
              ["Separen 150 mercados para entrenar y 50 para probar, con random_state 42.",
               "Calculen el error medio absoluto en los 50 de prueba de la l&iacute;nea base (predice siempre el promedio), de la recta de tv y del modelo con tv y radio.",
               "Pidan el intervalo de predicci&oacute;n al 90 % de los dos planes de la etapa 3 y calculen el margen en el peor caso."],
              PISTA("En casa. DummyRegressor es la l&iacute;nea base. En statsmodels, get_prediction(...).summary_frame(alpha=0.10) trae las columnas obs_ci_lower y obs_ci_upper."),
              candado("&iquest;Cu&aacute;l es el error medio del modelo con tv y radio en los 50 mercados de prueba?",
                      P(f"<b>{n(C['mae_tvradio'])} miles de unidades.</b> La l&iacute;nea base predice siempre {n(C['base_pred'])} y se equivoca en {n(C['mae_base'])}. La recta de tv se equivoca en {n(C['mae_tv'])}.")
                      + tabla(["Plan", "Intervalo al 90 % (miles de unidades)", f"Margen en el peor caso (miles)", "Publicidad (miles)"], [
                          ["Agencia", f"{n(A[1])} a {n(A[2])}", n(lowA, 1), n(sum(PLAN_A), 0)],
                          ["Daniela", f"{n(B[1])} a {n(B[2])}", n(lowB, 1), n(sum(PLAN_B), 0)],
                      ], num=(2, 3))),
              "&iquest;El pron&oacute;stico cumple la tolerancia de Daniela? &iquest;Su plan resiste el peor caso?"),
        etapa(6, "&iquest;Sacamos la prensa?",
              "Me piden recortar un medio. La prensa parec&iacute;a funcionar sola. &iquest;La saco del plan?",
              ["Ajusten una regresi&oacute;n con los tres medios a la vez: ventas contra tv, radio y prensa.",
               "Comparen el coeficiente de prensa en este modelo con el que ten&iacute;a en su recta simple.",
               "Comparen el R&sup2; ajustado del modelo con los tres medios y el del modelo con tv y radio."],
              PISTA("En casa. En statsmodels, el resumen del modelo trae el coeficiente, el p-valor y el intervalo de confianza de cada medio."),
              candado("&iquest;Cu&aacute;nto vale el coeficiente de prensa en el modelo con los tres medios?",
                      P(f"<b>{n(C['b3_prensa'], 4)}</b>, con p-valor {n(C['p3_prensa'])} y un intervalo de {n(C['ic3_prensa'][0], 3)} a {n(C['ic3_prensa'][1], 3)}. Sola, la prensa parec&iacute;a traer {n(C['u_prensa'], 1)} unidades por cada mil d&oacute;lares.")
                      + P(f"R&sup2; ajustado: {n(C['r2a_tres'], 4)} con prensa y {n(C['r2a_dos'], 4)} sin ella. El R&sup2; simple siempre sube un poco al agregar una variable; el ajustado castiga las que no aportan. Correlaci&oacute;n entre radio y prensa: {n(C['corr_radio_prensa'])}.")
                      + P("Estos datos son observacionales: nadie reparti&oacute; la prensa al azar entre los mercados.")),
              "&iquest;Sacan la prensa del plan? &iquest;Por qu&eacute; parec&iacute;a funcionar y c&oacute;mo lo comprobar&iacute;an antes de sacarla de todos los mercados?"),
    ],
    ("Qu&eacute; entregas", "".join([
        P("Entrega individual en la carpeta <b>Actividad en clase &middot; Caso Daniela</b>, hasta el domingo 8 de noviembre a las 23:59. Las etapas 1 a 4 se trabajan en grupo en clase y las etapas 5 y 6 se terminan en casa. Cada uno entrega lo suyo."),
        P("Un PDF, <b>caso-daniela-apellido-nombre.pdf</b>. En la primera p&aacute;gina, un memo para Daniela con las seis decisiones: una o dos frases cada una, con el n&uacute;mero que la sostiene y por qu&eacute;. En la segunda p&aacute;gina, el contenido de tu prompts.md."),
        tabla(["Criterio", "Puntos"], [
            ["Seis decisiones con su n&uacute;mero y un razonamiento propio que la sostiene (1,5 cada una)", "9"],
            ["Prompts incluidos", "1"],
            ["<b>Total</b>", "<b>10</b>"],
        ], num=(1,)),
    ])),
]
p4 = pagina("semana10-caso-daniela-regresion.html", "Caso Daniela &middot; Seis decisiones con una recta", SERIE10,
            "Mi&eacute;rcoles 4 de noviembre &middot; regresi&oacute;n lineal simple y m&uacute;ltiple sobre 200 mercados", caso, intro=intro_caso)

# ---------------------------------------------------------------- cifras para la guía
with open(AQUI / "cifras_caso.txt", "w", encoding="utf-8") as f:
    for k, v in C.items():
        f.write(f"{k}: {v}\n")
for x in (p1, p2, p3, p4, CSV):
    print("escrito", OUT / x, os.path.getsize(OUT / x), "bytes")
