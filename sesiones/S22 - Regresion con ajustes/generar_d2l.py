# -*- coding: utf-8 -*-
"""Página D2L de la sesión: explicación con animaciones y caso en seis etapas con candados.

Uso: python generar_d2l.py  -> d2l/semana11-regresion-con-ajustes.html y copia los videos a d2l/
Los números salen de cifras.json. Si una cifra cambia, se regenera: no se corrige a mano.
"""
import base64
import io
import json
import shutil
from pathlib import Path

from PIL import Image

AQUI = Path(__file__).resolve().parent
OUT = AQUI / "d2l"
R = json.loads((AQUI / "cifras.json").read_text(encoding="utf-8"))
NOMBRE = "semana11-regresion-con-ajustes.html"
ENTREGA = "domingo 15 de noviembre a las 23:59"
CSV, CO2, IPYNB = "mercados-bebidas-cumbre.csv", "consumo-combustible-co2.csv", "taller-ajustes-daniela.ipynb"
VIDEOS = {"S1Ajuste": "animacion-ajuste.mp4", "S2Columnas": "animacion-columnas.mp4", "S3Abanico": "animacion-interaccion.mp4", "S4Grado": "animacion-grado.mp4",
          "S5Ridge": "animacion-ridge.mp4", "S6Lasso": "animacion-lasso.mp4", "S7Geometria": "animacion-circulo-rombo.mp4", "S8Validacion": "animacion-validacion.mp4", "TrainTest": "animacion-train-test.mp4"}
for k, v in VIDEOS.items():
    shutil.copy(AQUI / "series" / "tomas" / "E02F-1.mp4" if k == "TrainTest" else AQUI / "animaciones" / f"{k}.mp4", OUT / v)

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
img,video{max-width:100%;height:auto;display:block;margin:12px 0;border:1px solid #eee}
.indice{background:#faf6f7;border:1px solid #efdfe2;border-radius:6px;padding:12px 18px;margin:20px 0}
.indice p{margin:0 0 6px;font-weight:600}
.indice ol{margin:0;padding-left:20px}
.volver{font-size:13px;margin:14px 0 0}
.nota{border:1px solid #e3e3e3;border-left:4px solid #A6192E;border-radius:6px;padding:12px 16px;margin:16px 0;background:#fcfcfc}
.nota b{color:#A6192E}
table{border-collapse:collapse;width:100%;margin:12px 0;font-size:15px}
th,td{border:1px solid #e1e1e1;padding:7px 10px;text-align:left;vertical-align:top}
th{background:#f4f4f4}
td.num,th.num{text-align:right}
.btn{display:inline-block;background:#A6192E;color:#fff !important;text-decoration:none;padding:7px 14px;border-radius:4px;font-size:14px;margin:4px 6px 4px 0}
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
.lab{font-size:13px;letter-spacing:.04em;color:#6b6b6b;margin:14px 0 2px;text-transform:uppercase}
.decision{border:2px solid #A6192E;border-radius:6px;padding:10px 16px;margin:14px 0 6px;background:#fff}
.decision p{margin:4px 0}
.decision .q{font-size:18px;font-weight:700;color:#A6192E}
.pie{margin:40px 0 0;padding-top:12px;border-top:1px solid #eee;text-align:right;font-weight:600}
"""


def n(x, d=2):
    return f"{x:,.{d}f}".replace(",", "§").replace(".", ",").replace("§", ".")


def img(nombre, alt):
    im = Image.open(AQUI / "img_deck" / nombre).convert("RGB")
    im.thumbnail((1100, 1100))
    b = io.BytesIO()
    im.save(b, "JPEG", quality=84)
    return f'<img alt="{alt}" src="data:image/jpeg;base64,{base64.b64encode(b.getvalue()).decode()}">'


def vid(k, alt):
    return f'<video controls preload="metadata" src="{VIDEOS[k]}" aria-label="{alt}"></video>'


P = lambda t: f"<p>{t}</p>"
OL = lambda xs: "<ol>" + "".join(f"<li>{x}</li>" for x in xs) + "</ol>"
NOTA = lambda t: f'<div class="nota">{t}</div>'


def tabla(cab, filas, num=()):
    th = "".join(f'<th{" class=num" if i in num else ""}>{c}</th>' for i, c in enumerate(cab))
    tr = "".join("<tr>" + "".join(f'<td{" class=num" if i in num else ""}>{c}</td>' for i, c in enumerate(f)) + "</tr>" for f in filas)
    return f"<table><tr>{th}</tr>{tr}</table>"


_q = [0]


def apuesta(pregunta, opciones):
    k = _q[0]
    _q[0] += 1
    css, partes = [], []
    for i, (texto, fb) in enumerate(opciones):
        partes.append(f'<input type="radio" name="q{k}" id="q{k}o{i}"><label for="q{k}o{i}">{texto}</label>')
        css.append(f"#q{k}o{i}:checked ~ .fb-q{k}o{i}{{display:block}}")
    fbs = "".join(f'<div class="fb fb-q{k}o{i}">{fb}</div>' for i, (_, fb) in enumerate(opciones))
    return f'<style>{"".join(css)}</style><div class="apuesta"><p class="preg">{pregunta}</p>{"".join(partes)}{fbs}</div>'


def candado(pregunta, revelado):
    return f'<div class="apuesta"><p class="preg">{pregunta}</p><input type="text" placeholder="Escribe tu n&uacute;mero antes de seguir"><div class="reveal">{revelado}</div></div>'


def etapa(pide, hacen, pista, control, decision):
    return (f'<div class="etapa"><p class="lab">Lo que pide Daniela</p>{P(pide)}<p class="lab">Qu&eacute; hacen</p>{OL(hacen)}<p class="lab">Pista de prompt</p>{P(pista)}{control}'
            f'<div class="decision"><p class="lab">Decisi&oacute;n para el memo</p><p class="q">{decision}</p></div></div>')


e = R["escalera"]
g = {x["grado"]: x for x in R["grados"]}
pa, pb = R["planes"]["agencia"], R["planes"]["daniela"]
m, gm = R["marginal"], R["ganancia_por_mil"]
rj = R["rejilla"]
L, Rd = rj["lasso_mejor"], rj["ridge_mejor"]
c2 = R["co2"]

teoria = [
    ("Ajustar es bajar hasta el fondo", "".join([
        P("Una regresi&oacute;n busca los coeficientes que dejan la menor suma de errores al cuadrado. La m&aacute;quina no sabe nada de TV ni de radio: prueba, mide y baja hasta el punto donde el error ya no puede bajar m&aacute;s. A eso se le llama m&iacute;nimos cuadrados."),
        vid("S1Ajuste", "Una recta gira hasta alcanzar la menor suma de cuadrados"),
        P("El detalle que importa hoy: el ajuste elige la mejor recta <b>entre las rectas</b>. Si el mundo tiene otra forma, entrega igual la mejor recta posible y no avisa. El aviso hay que buscarlo en los errores."),
    ])),
    ("Curvas e interacciones son columnas nuevas", "".join([
        P("Para que el modelo se doble no hace falta otro m&eacute;todo. Se le agregan columnas que se calculan con una multiplicaci&oacute;n y m&iacute;nimos cuadrados sigue funcionando igual. Por eso se sigue llamando regresi&oacute;n lineal: lineal en los coeficientes."),
        vid("S2Columnas", "Una tabla recibe las columnas TV por radio y TV al cuadrado"),
        tabla(["Columna", "La pregunta de negocio que hace"], [["tv &times; radio", "&iquest;Un medio potencia al otro?"], ["tv&sup2;", "&iquest;La TV se satura cuando ya hay mucha?"], ["&radic;tv", "&iquest;Las primeras pautas rinden mucho y las siguientes cada vez menos?"]]),
        vid("S3Abanico", "Dos rectas paralelas se abren en abanico sobre mercados con mucha y poca radio"),
        P("Esto se llama <b>ajuste polinomial</b> cuando las columnas son potencias e <b>interacci&oacute;n</b> cuando son productos entre variables. El grado es la potencia m&aacute;s alta permitida."),
    ])),
    ("M&aacute;s columnas no siempre es mejor", "".join([
        P("Cada grado adicional le da al modelo m&aacute;s libertad para pasar cerca de sus puntos. El error de entrenamiento baja siempre. El error en mercados que el modelo no vio baja un rato y despu&eacute;s se dispara. Eso se llama <b>sobreajuste</b>: el modelo aprendi&oacute; el ruido de sus datos."),
        vid("S4Grado", "Un polinomio sube de grado hasta pasar por todos los puntos y falla en los mercados nuevos"),
    ])),
    ("Ridge y Lasso: un precio por los coeficientes grandes", "".join([
        P("Regularizar cambia lo que el modelo minimiza. Ya no busca solo el menor error: paga un precio por tener coeficientes grandes."),
        P("<b>costo = error + &lambda; &middot; tama&ntilde;o de los coeficientes</b>"),
        P("&lambda; (en scikit-learn se llama <b>alpha</b>) es la fuerza del freno. Con &lambda; = 0 no hay freno. Con &lambda; enorme todos los coeficientes valen cero y el modelo es el promedio. <b>Ridge</b> cobra por el cuadrado de cada coeficiente y los encoge a todos sin eliminar ninguno."),
        vid("S5Ridge", "Al subir lambda los coeficientes se encogen sin llegar a cero"),
        P("<b>Lasso</b> cobra por el valor absoluto. Con ese precio, a las columnas d&eacute;biles les conviene valer exactamente cero: Lasso selecciona variables por su cuenta."),
        vid("S6Lasso", "Al subir lambda los coeficientes caen a cero uno por uno"),
        P("La raz&oacute;n se ve en una imagen. El freno es un presupuesto para los coeficientes. El presupuesto de Ridge es un c&iacute;rculo y el de Lasso un rombo, que tiene esquinas justo sobre los ejes. En una esquina un coeficiente vale cero."),
        vid("S7Geometria", "Un c&iacute;rculo y un rombo encogen hasta tocar las curvas de error"),
        NOTA("<b>Antes de frenar, todas las columnas en la misma escala.</b> Si la TV estuviera en d&oacute;lares y no en miles, su coeficiente ser&iacute;a mil veces m&aacute;s chico y casi no pagar&iacute;a. Por eso cada columna se estandariza a media 0 y desviaci&oacute;n 1 con StandardScaler, dentro de un pipeline, para que solo aprenda de los datos de entrenamiento."),
    ])),
    ("Train y test: estudiar y rendir el examen", "".join([
        P("Antes de ajustar cualquier cosa, los datos se separan en dos. <b>Train</b> (entrenamiento) son 150 mercados: con ellos aprende el modelo. <b>Test</b> (prueba) son 50 mercados que se guardan bajo llave y se abren una sola vez, al final."),
        vid("TrainTest", "Doscientos mercados se barajan, 150 van a train y 50 quedan bajo llave como test"),
        tabla(["Si ves esto", "Quiere decir"], [["Error de train cerca del de test", "Aprendi&oacute; algo real"], ["Error de train mucho mejor que el de test", "Memoriz&oacute;: es sobreajuste"], ["Los dos errores altos", "Le falta forma al modelo"]]),
        NOTA("<b>C&oacute;mo ped&iacute;rselo a tu asistente.</b> Separa 150 mercados para train y 50 para test, con random_state 42. Entrena solo con train. Mu&eacute;strame el error en train y en test. Revisa la l&iacute;nea donde separa y que test no se use para nada m&aacute;s."),
    ])),
    ("El freno se elige con validaci&oacute;n cruzada", "".join([
        P("Si eliges &lambda; mirando los mercados de prueba, ya no son mercados que el modelo no vio. Validaci&oacute;n cruzada divide el entrenamiento en cinco partes, entrena con cuatro y valida con la quinta, cinco veces. La prueba se abre una sola vez, al final."),
        vid("S8Validacion", "Cinco turnos de validaci&oacute;n dibujan el error seg&uacute;n la fuerza del freno"),
        tabla(["Si ves esto", "Prueba con"], [["Los errores forman un patr&oacute;n", "Curva o transformaci&oacute;n"], ["El efecto de una variable depende de otra", "Interacci&oacute;n"], ["Muchas columnas para pocas filas", "Ridge o Lasso"], ["Columnas casi copiadas", "Ridge"], ["Necesitas saber cu&aacute;les importan", "Lasso"]]),
    ])),
]

etapas = [
    ("C&oacute;mo pedirle el trabajo a tu asistente", "".join([
        P("Sirve igual en Claude, Gemini o Antigravity. Un buen prompt lleva cinco cosas."),
        OL(["<b>Los datos y sus unidades.</b> Ventas en miles de unidades, inversi&oacute;n en miles de USD.", "<b>Una tarea por prompt.</b> Primero el gr&aacute;fico, despu&eacute;s el modelo.", "<b>Lo que no debe hacer.</b> No borres filas. No uses test para elegir.", "<b>Lo que debe mostrarte.</b> La ecuaci&oacute;n, la tabla y las cifras para verificar.", "<b>Que te lo explique.</b> Qu&eacute; hizo y qu&eacute; significa para Daniela."]),
        NOTA("<b>Para separar las l&iacute;neas.</b> Pinta cada mercado seg&uacute;n su radio: rojo si es 35 o m&aacute;s, negro si es 12 o menos, gris el resto, sin borrar filas. Luego ajusta una sola regresi&oacute;n con tv, radio y tv por radio, con la radio como n&uacute;mero, y dibuja una l&iacute;nea por grupo con esa misma ecuaci&oacute;n. No ajustes un modelo por grupo."),
    ])),
    ("Etapa 1 &middot; D&oacute;nde falla el plano", etapa(
        "Prometí 14.420 unidades con el plan de 50 mil en TV y 49 mil en radio. Antes de volver al comité quiero saber si el plano se equivoca parejo o se equivoca siempre en el mismo tipo de mercado.",
        ["Ajusten el plano con los 200 mercados: ventas contra tv y radio.", "Calculen el error de cada mercado: real menos pron&oacute;stico.", "Hagan un gr&aacute;fico de tv contra radio con el color seg&uacute;n ese error.", "Filtren los mercados con tv de hasta 90 y radio desde 35, los que se parecen al plan de Daniela, y promedien real y pron&oacute;stico."],
        "P&iacute;dele: <b>ajusta ventas contra tv y radio con los 200 mercados, calcula el error de cada uno y dibuja tv contra radio con el color seg&uacute;n ese error, en una escala centrada en cero. Antes de proponer nada, expl&iacute;came qu&eacute; patr&oacute;n ves.</b> Revisa: calcula un mercado a mano con la ecuaci&oacute;n que te dio.",
        candado("En esos 20 mercados, &iquest;cu&aacute;nto se pasa el plano en promedio, en miles de unidades?", P(f"<b>{n(abs(R['vecinos_daniela']['res_plano']))} miles de m&aacute;s.</b> Vendieron {n(R['vecinos_daniela']['real'])} y el plano les pronostic&oacute; {n(R['vecinos_daniela']['plano'])}. En los 20 se pas&oacute;, ninguno se salv&oacute;.") + img("f1-mapa-errores.png", "Mapa de errores del plano por inversi&oacute;n en TV y radio")),
        "&iquest;El error del plano es ruido o patr&oacute;n? Si es patr&oacute;n, &iquest;en qu&eacute; tipo de mercado promete de m&aacute;s?")),
    ("Etapa 2 &middot; Doblar el plano", etapa(
        "Quiero un modelo que entienda que TV y radio juntas no son lo mismo que TV y radio por separado.",
        ["Separen 150 mercados para entrenar y 50 para probar, con random_state 42, como en el caso anterior.", "Agreguen la columna tv &times; radio y midan el error medio en los 50 de prueba.", "Agreguen tambi&eacute;n tv&sup2; y midan otra vez.", "Comparen con la l&iacute;nea base y con el plano."],
        "P&iacute;dele: <b>con los 150 de train agrega la columna tv por radio y mide el error en los 50 de test. Despu&eacute;s agrega tv al cuadrado y mide otra vez. Dame una tabla con cada modelo, sus columnas y su error en train y en test.</b> Revisa: multiplica t&uacute; una fila y comprueba esa columna.",
        candado("&iquest;Cu&aacute;l es el error medio en prueba del modelo con tv, radio, tv &times; radio y tv&sup2;?", tabla(["Modelo", "Columnas", "Error en prueba"], [["Promedio (l&iacute;nea base)", "0", n(R["mae_base"])], ["tv + radio", "2", n(e["plano"]["mae_te"])], ["+ tv &times; radio", "3", n(e["interaccion"]["mae_te"])], ["+ tv&sup2;", "4", f"<b>{n(e['curva']['mae_te'])}</b>"]], (1, 2))),
        "&iquest;Cu&aacute;l de las dos columnas nuevas aport&oacute; m&aacute;s? &iquest;Por qu&eacute; tiene sentido de negocio?")),
    ("Etapa 3 &middot; Corregir la promesa", etapa(
        "Vuelvo al comité. Necesito la cifra correcta de mi plan, la del plan de la agencia y saber dónde conviene el próximo dólar de radio.",
        ["Ajusten el modelo de cuatro columnas con los 200 mercados.", "Pronostiquen el plan de la agencia (TV 150, radio 25) y el de Daniela (TV 50, radio 49).", "Calculen la utilidad de cada plan: unidades por 12 USD de margen menos la inversi&oacute;n.", "Calculen cu&aacute;ntas unidades trae cada mil USD adicionales en radio cuando la TV vale 50, 150 y 250."],
        "P&iacute;dele: <b>ajusta el modelo de cuatro columnas con los 200 mercados y pronostica dos planes. Todo est&aacute; en miles y cada unidad deja 12 USD. Dame unidades, margen, inversi&oacute;n y utilidad de cada plan. Luego dime cu&aacute;ntas unidades trae cada mil USD en radio con TV de 50, 150 y 250.</b> Revisa: rehaz un plan a mano y mira que unidades y d&oacute;lares est&eacute;n en miles.",
        candado("&iquest;Cu&aacute;ntas miles de unidades pronostica ahora el modelo para el plan de Daniela?", P(f"<b>{n(pb['curva'])} miles</b>, no {n(pb['plano'])}.") + tabla(["Plan", "Inversi&oacute;n", "Plano", "Curva", "Utilidad (miles USD)"], [["Agencia", "175", n(pa["plano"]), n(pa["curva"]), "+" + n(pa["utilidad_curva"], 1)], ["Daniela", "99", n(pb["plano"]), n(pb["curva"]), "+" + n(pb["utilidad_curva"], 1)]], (1, 2, 3, 4)) + tabla(["TV del mercado", "Unidades por mil USD en radio", "Ganancia por mil USD"], [[str(t), n(m[f"radio_tv{t}"], 0), ("+" if gm[f"radio_tv{t}"] > 0 else "") + n(gm[f"radio_tv{t}"], 0) + " USD"] for t in (50, 150, 250)], (0, 1, 2)) + P(f"La radio empieza a pagarse cuando la TV pasa de {n(R['radio_equilibrio_tv'], 0)} mil.")),
        "&iquest;Cambia la decisi&oacute;n de lanzar con el plan de Daniela? &iquest;Qu&eacute; cifra le dices al comit&eacute; y c&oacute;mo explicas que baj&oacute;?")),
    ("Etapa 4 &middot; La oferta de la agencia", etapa(
        "La agencia me ofrece un modelo de grado 6 con R² de 0,998. Dice que es mucho mejor que el mío. ¿Lo compro?",
        ["Con los tres medios, ajusten polinomios de grado 1 a 7 en los 150 de entrenamiento.", "Para cada grado anoten el R&sup2; de entrenamiento, el error de entrenamiento y el error de prueba.", "Miren los errores del grado 6 mercado por mercado."],
        "P&iacute;dele: <b>con los tres medios, ajusta polinomios de grado 1 a 7 usando solo los 150 de train. Dame una tabla con columnas, R&sup2; de train, error de train y error de test. Luego mu&eacute;strame el error del grado 6 mercado por mercado. No corrijas ni elimines nada por tu cuenta.</b> Revisa: si un error de test se ve absurdo, pide ver ese mercado.",
        candado("&iquest;Cu&aacute;l es el error medio en prueba del grado 6?", tabla(["Grado", "Columnas", "R&sup2; entrenamiento", "Error entrenamiento", "Error prueba"], [[str(d), str(g[d]["columnas"]), n(g[d]["r2_tr"], 3), n(g[d]["mae_tr"]), n(g[d]["mae_te"])] for d in range(1, 8)], (0, 1, 2, 3, 4)) + P(f"En el grado 6, {R['grado6']['n_menor_2']} de 50 mercados tienen error menor a 2 mil. El mercado {R['grado6']['peor_mercado']} recibe un pron&oacute;stico de {n(R['grado6']['peor_pred'], 0)} mil unidades y vendi&oacute; {n(R['grado6']['peor_real'], 1)} mil.")),
        "&iquest;Compran el modelo de la agencia? Respondan con el n&uacute;mero que un comit&eacute; entender&iacute;a.")),
    ("Etapa 5 &middot; El freno", etapa(
        "No descarto todas esas columnas todavía. Quiero ver si un freno las hace útiles y saber cuáles importan.",
        ["Tomen el grado 5 con los tres medios: 55 columnas.", "Para cada &alpha; de la lista calculen el error medio con validaci&oacute;n cruzada de cinco partes, solo con los 150 de entrenamiento.", "Elijan el mejor &alpha; de Lasso y el mejor de Ridge. Reci&eacute;n ah&iacute; midan en los 50 de prueba.", "Cuenten cu&aacute;ntas columnas quedan vivas en Lasso y miren qu&eacute; pasa con &alpha; = 0,3."],
        "P&iacute;dele: <b>con grado 5, estandariza las columnas y prueba Lasso con alfa 0,0001, 0,0003, 0,001, 0,003, 0,01, 0,03, 0,1, 0,3 y 1, y Ridge con alfa 0,01, 0,03, 0,1, 0,3, 1, 3, 10, 30 y 100. Elige alfa con validaci&oacute;n cruzada de cinco partes con shuffle y random_state 42, solo dentro de los 150 de train y por error absoluto medio. Al final mide en test y dime cu&aacute;ntas columnas quedan vivas. Usa suficientes iteraciones para que Lasso converja.</b> Revisa: preg&uacute;ntale si us&oacute; test para elegir alfa y que te muestre d&oacute;nde.",
        candado("&iquest;Cu&aacute;ntas columnas deja vivas Lasso con el &alpha; que gana en validaci&oacute;n?", tabla(["Modelo", "&alpha;", "Columnas vivas", "Error en prueba"], [["Grado 5 sin freno", "", "55", n(g[5]["mae_te"])], ["Ridge", n(Rd["alpha"], 2), str(Rd["vivas"]), n(Rd["mae_te"])], ["Lasso", n(L["alpha"], 3), f"<b>{L['vivas']}</b>", n(L["mae_te"])]], (1, 2, 3)) + P(f"Con &alpha; = 0,3 Lasso deja dos columnas: tv y tv &times; radio. Nadie se lo indic&oacute;, y con esas dos columnas el error es {n(rj['lasso'][7]['mae_te'])}, contra {n(e['plano']['mae_te'])} del plano.")),
        "&iquest;Con cu&aacute;l se queda Daniela: la curva de cuatro columnas o el Lasso? Argumenten con error y con lo que se puede explicar.")),
    ("Etapa 6 &middot; En casa: la columna que t&uacute; propones y un dataset distinto", etapa(
        "Dos encargos finales. Uno: propón una columna que tenga sentido de negocio y gánale a mi modelo de cuatro columnas. Dos: quiero saber si el freno sirve también cuando las columnas son casi copias.",
        ["Propongan una transformaci&oacute;n propia, expliquen en una frase por qu&eacute; tiene sentido y midan el error en los mismos 50 mercados.", f"Con el archivo de consumo de combustible, usen ENGINESIZE, CYLINDERS y las cuatro columnas FUELCONSUMPTION para predecir CO2EMISSIONS.", "Tomen seis mitades distintas de los datos (random_state de 0 a 5). En cada una ajusten sin freno, con Ridge (alpha 50) y con Lasso (alpha 1), y anoten el rango del coeficiente de FUELCONSUMPTION_COMB."],
        "Para tu columna, p&iacute;dele: <b>quiero probar una columna nueva porque [tu raz&oacute;n de negocio]. Agr&eacute;gala al modelo de cuatro columnas, entrena con train y mide en los mismos 50 de test. No pruebes otras columnas por tu cuenta.</b> Piensa en c&oacute;mo funciona la publicidad: &iquest;la mil&eacute;sima pauta rinde igual que la primera? Para el CO2, p&iacute;dele que estandarice antes de ajustar y que te devuelva una tabla con el coeficiente en cada mitad. Este dataset viene de un taller de a&ntilde;os anteriores.",
        candado("&iquest;Entre qu&eacute; valores se mueve el coeficiente de FUELCONSUMPTION_COMB sin freno?", P(f"De <b>{n(c2['mitades']['ols']['FUELCONSUMPTION_COMB'][0], 0)} a +{n(c2['mitades']['ols']['FUELCONSUMPTION_COMB'][1], 0)}</b>. Con Ridge, de {n(c2['mitades']['ridge']['FUELCONSUMPTION_COMB'][0], 1)} a {n(c2['mitades']['ridge']['FUELCONSUMPTION_COMB'][1], 1)}. Lasso lo deja en cero en {c2['mitades_ceros']['lasso']['FUELCONSUMPTION_COMB']} de las 6 mitades: reparte el trabajo como le toca. Ciudad y combinado correlacionan {n(c2['corr_ciudad_comb'], 3)}.") + P(f"Una columna que funciona: <b>&radic;tv</b>. Con tv, &radic;tv, radio y tv &times; radio el error de prueba baja a {n(e['raiz_tv']['mae_te'])}, con cuatro columnas.")),
        "&iquest;Cu&aacute;ndo le recomendar&iacute;as a Daniela Ridge, cu&aacute;ndo Lasso y cu&aacute;ndo ninguno?")),
    ("Qu&eacute; entregas", "".join([
        P(f"Entrega individual en la carpeta de la actividad, hasta el <b>{ENTREGA}</b>."),
        OL(["Un memo de una p&aacute;gina para Daniela con las seis decisiones, cada una con su n&uacute;mero.", "El enlace p&uacute;blico del cuaderno de Colab con todo ejecutado.", "El archivo prompts.md con lo que le pediste al asistente y qu&eacute; verificaste."]),
        NOTA("<b>Lo que se califica.</b> La decisi&oacute;n y el razonamiento, no solo la cifra. Si tu n&uacute;mero no cuadra con el candado, revisa el prompt y el c&oacute;digo y cuenta en el memo qu&eacute; estaba mal."),
    ])),
]

intro = "".join([
    P("El viernes Daniela le prometi&oacute; al comit&eacute; de Bebidas Cumbre 14.420 unidades en el mercado nuevo. Lo calcul&oacute; con el plano de TV y radio que armaron en el caso anterior. Hoy revisamos esa cifra, le ense&ntilde;amos al modelo a doblarse y aprendemos a frenarlo cuando se dobla de m&aacute;s."),
    f'<p><a class="btn" href="{CSV}" download>Descargar {CSV}</a><a class="btn" href="{IPYNB}" download>Descargar el cuaderno</a><a class="btn" href="{CO2}" download>Descargar {CO2}</a></p>',
    P("Trabajen con Claude, Gemini o Antigravity. No necesitan escribir Python: le piden el trabajo al asistente y verifican lo que entrega. Cada etapa trae una pista de prompt. Cada etapa tiene una pregunta de control con un n&uacute;mero: escr&iacute;banlo antes de abrir la respuesta. Copien sus prompts en <b>prompts.md</b>. Margen: <b>12 USD por unidad</b>. Inversi&oacute;n en miles de USD, ventas en miles de unidades."),
    apuesta("Antes de empezar: &iquest;qu&eacute; crees que le pasa a la cifra de Daniela con un modelo mejor?", [("Sube", "Vamos a verlo en la etapa 3."), ("Baja", "Vamos a verlo en la etapa 3."), ("Queda igual", "Vamos a verlo en la etapa 3.")]),
])
sec = teoria + etapas
idx = "".join(f'<li><a href="#s{i}">{t}</a></li>' for i, (t, _) in enumerate(sec, 1))
cuerpo = "".join(f'<h2 id="s{i}">{t}</h2>{c}<p class="volver"><a href="#indice">&uarr; volver al &iacute;ndice</a></p>' for i, (t, c) in enumerate(sec, 1))
TIT = "Una recta no se dobla &middot; Regresi&oacute;n con ajustes"
doc = f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TIT}</title><style>{CSS}</style></head>
<body><header class="cab"><p class="serie">ADM 2003 &middot; An&aacute;lisis de Datos &middot; Semana 11 &middot; Regresi&oacute;n con ajustes</p><h1>{TIT}</h1><p class="sub">Lunes 9 de noviembre &middot; curvas, interacciones, Ridge y Lasso sobre 200 mercados</p></header>
<main>{intro}<nav class="indice" id="indice"><p>En esta p&aacute;gina</p><ol>{idx}</ol></nav>
{cuerpo}<p class="pie">Ve al siguiente tema &rarr;</p></main></body></html>"""
(OUT / NOMBRE).write_text(doc.encode("ascii", "xmlcharrefreplace").decode("ascii"), encoding="utf-8")
print(NOMBRE, len(doc) // 1024, "KB")
