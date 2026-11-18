# -*- coding: utf-8 -*-
"""Página D2L de la sesión del lunes 16 de noviembre: lanzamiento del simulador «La fría cuesta más».

Uso: python generar_d2l.py  -> d2l/semana12-la-fria-cuesta-mas.html y d2l/caso-la-fria-cuesta-mas.pdf
Un solo HTML autocontenido: CSS dentro, sin JavaScript, viñetas en JPEG base64 y texto en entidades ASCII.
Toda cifra sale del caso (caso.md) o de los YAML del simulador. Si algo cambia, se regenera: no se corrige a mano.
"""
import base64
import io
import shutil
from pathlib import Path

from PIL import Image

# Lo que más puede cambiar, arriba.
SIMULADOR_URL = "https://regresion-simuladores.iahumana.org/login/"
CASO_ORIGEN = Path("/Users/julianmaya/orca/workspaces/simuladores_clases/Regresión/docs/regresion/materiales/estudiantes/01_Caso_La_fria_cuesta_mas.pdf")
CASO_PDF = "caso-la-fria-cuesta-mas.pdf"
NOMBRE = "semana12-la-fria-cuesta-mas.html"
ANCHO_IMG, CALIDAD_IMG = 1000, 82

AQUI = Path(__file__).resolve().parent
ARTE = AQUI / "arte"
OUT = AQUI / "d2l"
OUT.mkdir(exist_ok=True)
if CASO_ORIGEN.exists():
    shutil.copy(CASO_ORIGEN, OUT / CASO_PDF)
elif not (OUT / CASO_PDF).exists():
    raise SystemExit(f"Falta el PDF del caso: {CASO_ORIGEN}")

CSS = """
*{box-sizing:border-box}
body{margin:0;background:#fff;color:#232326;font-family:'Segoe UI',system-ui,-apple-system,Arial,sans-serif;font-size:16px;line-height:1.6}
.cab{border-bottom:5px solid #A6192E;background:#fff}
.cab div{max-width:760px;margin:0 auto;padding:24px 20px 18px}
.cab .serie{font-size:13px;letter-spacing:.04em;color:#A6192E;margin:0 0 4px;font-weight:600}
.cab h1{margin:0;font-size:28px;line-height:1.25;font-weight:700;color:#232326}
.cab .sub{margin:6px 0 0;color:#55555a;font-size:15px}
main{max-width:760px;margin:0 auto;padding:8px 20px 40px}
h2{color:#A6192E;font-size:21px;margin:38px 0 10px;padding-top:10px;border-top:1px solid #eee}
h3{font-size:17px;margin:24px 0 6px}
a{color:#A6192E}
p{margin:10px 0}
img{max-width:100%;height:auto;display:block;border:1px solid #eee;border-radius:4px}
figure{margin:18px 0}
figcaption{font-size:14px;color:#55555a;margin-top:6px}
.indice{background:#faf6f7;border:1px solid #efdfe2;border-radius:6px;padding:12px 18px;margin:20px 0}
.indice p{margin:0 0 6px;font-weight:600}
.indice ol{margin:0;padding-left:22px;columns:2;column-gap:28px}
.indice li{break-inside:avoid}
.volver{font-size:13px;margin:16px 0 0}
.nota{border:1px solid #e3e3e3;border-left:4px solid #A6192E;border-radius:6px;padding:10px 16px;margin:16px 0;background:#fcfcfc}
.nota b{color:#A6192E}
.pista{border:1px solid #efdfe2;border-radius:6px;padding:10px 16px;margin:14px 0;background:#fff}
.pista .t{font-weight:700;color:#A6192E;margin:2px 0 4px}
.pista p{margin:6px 0}
.memo{margin:12px 0;padding:10px 18px;border-left:4px solid #232326;background:#f7f7f7;border-radius:0 6px 6px 0}
.memo .firma{font-size:14px;color:#55555a}
.acceso{border:2px solid #A6192E;border-radius:6px;padding:8px 18px 12px;margin:16px 0}
.acceso code,td code,li code,p code{font-family:Consolas,'Courier New',monospace;font-size:15px;background:#f4f4f4;padding:1px 5px;border-radius:3px}
.tw{overflow-x:auto}
table{border-collapse:collapse;width:100%;margin:12px 0;font-size:15px}
th,td{border:1px solid #e1e1e1;padding:7px 10px;text-align:left;vertical-align:top}
th{background:#f4f4f4}
td.num,th.num{text-align:right;white-space:nowrap}
.pie-tabla{font-size:14px;color:#55555a;margin-top:0}
.btn{display:inline-block;background:#A6192E;color:#fff !important;text-decoration:none;padding:8px 16px;border-radius:4px;font-size:15px;font-weight:600;margin:4px 6px 4px 0}
.lab{font-size:13px;letter-spacing:.04em;color:#6b6b6b;margin:20px 0 2px;text-transform:uppercase;font-weight:600}
.pie{margin:40px 0 0;padding-top:12px;border-top:1px solid #eee;text-align:right;font-weight:600}
@media (max-width:560px){.indice ol{columns:1}.cab h1{font-size:23px}}
"""


def img(nombre, alt, pie):
    im = Image.open(ARTE / nombre).convert("RGB")
    if im.width > ANCHO_IMG:
        im = im.resize((ANCHO_IMG, round(im.height * ANCHO_IMG / im.width)), Image.LANCZOS)
    b = io.BytesIO()
    im.save(b, "JPEG", quality=CALIDAD_IMG, optimize=True)
    src = base64.b64encode(b.getvalue()).decode()
    return f'<figure><img alt="{alt}" width="{im.width}" height="{im.height}" src="data:image/jpeg;base64,{src}"><figcaption>{pie}</figcaption></figure>'


P = lambda t: f"<p>{t}</p>"
H3 = lambda t: f"<h3>{t}</h3>"
LAB = lambda t: f'<p class="lab">{t}</p>'
OL = lambda xs: "<ol>" + "".join(f"<li>{x}</li>" for x in xs) + "</ol>"
NOTA = lambda t: f'<div class="nota">{t}</div>'
BTN = lambda href, t, extra="": f'<a class="btn" href="{href}"{extra}>{t}</a>'


def tabla(cab, filas, num=()):
    th = "".join(f'<th{" class=num" if i in num else ""}>{c}</th>' for i, c in enumerate(cab))
    tr = "".join("<tr>" + "".join(f'<td{" class=num" if i in num else ""}>{c}</td>' for i, c in enumerate(f)) + "</tr>" for f in filas)
    return f'<div class="tw"><table><tr>{th}</tr>{tr}</table></div>'


def pista(titulo, pide, revisa):
    return f'<div class="pista"><p class="t">{titulo}</p><p>Pídele: <b>{pide}</b></p><p>Revisa: {revisa}</p></div>'


# ───────────────────────── Datos que vienen del caso y del simulador ─────────────────────────

# PLAN.md (sorteo) y Exhibit 3 del caso.
GRUPOS = [
    ["Grupo 1", "Red Bull", "Cusco", "La premium. Es la más cara fuera de Iquitos."],
    ["Grupo 2", "220V", "Arequipa", "Precio alto, poca promoción y clientes de rutina."],
    ["Grupo 3", "Monster", "Piura", "Formato grande, para la playa y el deporte."],
    ["Grupo 4", "Volt", "Iquitos", "La de casa: precio medio y la mejor cobertura."],
    ["Grupo 5", "Vive100", "Lima", "La barata, con promoción permanente."],
]

# Exhibit 4 del caso: semana, lunes, precio, promoción, temperatura, feriado, botellas.
EXHIBIT4 = [
    ["5", "27 ene", "4.00", "28,500", "27.3", "", "85,925"],
    ["6", "3 feb", "4.00", "27,500", "25.5", "", "63,926"],
    ["7", "10 feb", "3.20", "52,000", "25.4", "", "179,628"],
    ["8", "17 feb", "3.20", "45,000", "23.3", "", "174,538"],
    ["9", "24 feb", "3.20", "36,500", "24.0", "", "158,982"],
    ["10", "3 mar", "3.20", "37,000", "22.6", "", "154,464"],
    ["11", "10 mar", "3.20", "40,500", "24.2", "", "110,930"],
    ["12", "17 mar", "3.20", "36,500", "24.2", "", "111,675"],
    ["13", "24 mar", "3.20", "64,000", "22.9", "", "156,316"],
    ["14", "31 mar", "3.60", "42,500", "21.6", "", "80,398"],
    ["15", "7 abr", "4.00", "10,500", "23.1", "", "51,172"],
    ["16", "14 abr", "4.00", "18,000", "22.9", "Jueves y Viernes Santo", "71,796"],
    ["17", "21 abr", "4.00", "14,000", "21.1", "", "62,020"],
    ["18", "28 abr", "4.00", "17,500", "22.0", "1 de mayo", "69,577"],
    ["19", "5 may", "4.00", "18,500", "21.5", "", "52,180"],
]

# simulador/juego.py, PASOS: los ocho pasos de la misión y su responsable.
PASOS = [
    ("Analista", "Descargar y limpiar los datos."),
    ("Analista", "Correr el modelo y llenar el borrador."),
    ("Auditor", "Replicar el modelo sin ver el borrador."),
    ("Auditor", "Revisar los supuestos y firmar."),
    ("Analista", "Enviar la entrega y aprobar la etapa."),
    ("Gerente", "Proponer precios, mezcla e intervalo de ventas."),
    ("Controller", "Declarar las tres cifras y aprobar la decisión."),
    ("Gerente", "Escribir la bitácora de la ronda."),
]

# simulador/dominio/datasets.py (COLUMNAS_PANEL) y simulador/exportar.py (_DICCIONARIO_PANEL).
DICCIONARIO = [
    ["obs_id", "Texto: ciudad, año y semana", "Llave de cada fila. Con ella reportas una fila sucia o la excluyes del modelo. Léela como texto."],
    ["fecha", "Lunes de la semana", "Fecha en que empieza la semana."],
    ["anio", "Año", "Cada año tiene 52 semanas."],
    ["trimestre", "Trimestre del año", "Cada ronda del simulador es un trimestre."],
    ["semana", "Semana del año", "Número de la semana dentro del año."],
    ["ciudad", "Lima, Arequipa, Cusco, Piura o Iquitos", "La ciudad de la fila."],
    ["marca", "Nombre de la marca", "Es la misma en todo el archivo de tu equipo."],
    ["precio", "S/ por unidad", "Precio registrado en bodega: el que se ve en el anaquel, con el recargo de la helada incluido."],
    ["promocion", "S/ por semana", "Gasto en promoción en bodega."],
    ["publicidad", "S/ por semana", "Gasto en publicidad digital."],
    ["distribucion", "Porcentaje, de 1 a 100", "Bodegas de la ruta que tienen el producto. Es la cobertura."],
    ["precio_competencia", "S/", "Promedio de los precios de las marcas rivales en esa ciudad y esa semana."],
    ["temporada_alta", "0 o 1", "Propia de cada ciudad: verano en Lima y Piura, de junio a agosto en Cusco, nunca en Arequipa ni en Iquitos."],
    ["ventas", "Unidades", "Botellas vendidas en la semana. La base llama botella a cada unidad, sea lata o botella."],
]

# PLAN.md, calendario propuesto.
CALENDARIO = [
    ["1", "Regresión simple", "Lunes 16 de noviembre, en clase", "Lunes 16 en clase, o miércoles 18 a las 09:30"],
    ["2", "Regresión múltiple", "Miércoles 18 de noviembre", "Lunes 23 de noviembre, 09:30"],
    ["3", "Indicadoras e interacción", "Lunes 23 de noviembre", "Miércoles 25 de noviembre, 09:30"],
    ["4", "Logaritmos y elasticidades", "Miércoles 25 de noviembre", "Lunes 30 de noviembre, 09:30"],
    ["5", "Diagnóstico", "Lunes 30 de noviembre", "Miércoles 2 de diciembre, 09:30"],
    ["6", "Validación y regularización", "Miércoles 2 de diciembre", "Lunes 7 de diciembre, 09:30"],
    ["7", "Regresión logística", "Lunes 7 de diciembre", "Miércoles 9 de diciembre, 09:30"],
    ["8", "Del modelo a la decisión", "Por definir", "Por definir"],
]

DESCARGA_CASO = BTN(CASO_PDF, "Descargar el caso completo (PDF)", " download")

# ───────────────────────────────────── Secciones ─────────────────────────────────────

sec = [
    ("De qué se trata", "".join([
        P("Desde hoy y durante ocho rondas, los cinco equipos del curso dirigen cinco marcas de bebidas energizantes que compiten en cinco ciudades del Perú: Lima, Arequipa, Cusco, Piura e Iquitos. Cada ronda es un trimestre. En cada una tu equipo recibe una pregunta de la gerencia, la responde con una regresión y después decide con qué precio, cuánta promoción, cuánta publicidad y cuánta cobertura sale al mercado. Los cinco equipos juegan en el mismo mercado, así que lo que decide uno le cambia el resultado a los demás."),
        P("Trabajas en el equipo de Valeria Chumpitaz, la gerente de marca. Ella tiene que presentar en enero el plan comercial de 2026 y carga con la pregunta que el gerente general dejó sobre la mesa: <b>¿qué pasa con las ventas si movemos el precio treinta céntimos?</b> Todo el simulador es el camino para contestarla bien."),
        P("Es un caso ficticio con marcas reales: las marcas y las ciudades existen, y todas las cifras, las personas y los hechos son inventados para la clase."),
    ])),
    ("Entrar al simulador", "".join([
        f'<p>{BTN(SIMULADOR_URL, "Abrir el simulador", " target=_blank rel=noopener")}</p>',
        '<div class="acceso">'
        + P("<b>Usuario:</b> tu correo institucional completo, escrito en minúsculas.")
        + P("<b>Clave:</b> la letra p minúscula seguida de tu código de estudiante (el de Banner) con todos sus ceros. Si tu código fuera 00123456, tu clave sería <code>p00123456</code>. Ese código es un ejemplo inventado.")
        + "</div>",
        P("El simulador solo funciona en computador. Necesita una pantalla ancha y no se puede jugar desde el teléfono."),
        P("Si revisaste el correo y la clave y aun así no puedes entrar, escríbele al profesor para que revise tu acceso."),
    ])),
    ("Tu grupo y tu marca", "".join([
        P("Son los mismos grupos de siempre. A cada uno le tocó una marca por sorteo, y cada marca tiene una ciudad donde manda, que el caso llama su plaza fuerte. Las cinco marcas venden en las cinco ciudades."),
        tabla(["Grupo", "Marca", "Plaza fuerte", "Cómo se posiciona"], GRUPOS),
        P("Al entrar, el Tablero te muestra tu marca, tu plaza fuerte y tu rol de la ronda."),
    ])),
    ("El caso en cinco minutos", "".join([
        H3("La llamada"),
        P("Un viernes de diciembre de 2025 la gerencia discutió veinte minutos el precio de 2026 y nadie cambió de opinión. Óscar Saldaña, el director comercial, quería repetir la rebaja del verano anterior. Rocío Huamán, la gerente de finanzas, le recordó que esa rebaja había dejado el peor abril en dos años. Jaime Ríos, de operaciones, dijo que los dos miraban el precio y ninguno las rutas. El gerente general, Hernán Dávila, cortó la discusión con una frase: “El directorio no quiere otra opinión. Quiere saber qué pasa con las ventas si movemos el precio treinta céntimos”. La pregunta le quedó a Valeria Chumpitaz."),
        img("comic_gerencia.png", "Cuatro personas de la gerencia discuten y señalan una nube de puntos proyectada en la pared", "Todos miran los mismos datos y cada uno ve otra cosa: Saldaña ve volumen, Huamán ve margen y Ríos ve cobertura."),
        H3("La nube de 520 puntos"),
        P("Valeria tiene algo mejor que un solo verano. Desde enero de 2024 cada marca guarda, por semana y por ciudad, el precio promedio de bodega, el gasto en promoción, el gasto en publicidad digital, el porcentaje de bodegas con producto y las botellas vendidas. Son 104 semanas en cinco ciudades, es decir 520 puntos. Los puso en una lámina, con el precio en el eje horizontal y las botellas en el vertical. No salió una línea ni una curva. Salió una nube."),
        img("comic_nube.png", "Valeria mira en su pantalla un gráfico de puntos dispersos sin forma clara", "Dos años de semanas por ciudad, precio contra ventas: 520 puntos que no forman una línea."),
        H3("La fría cuesta más"),
        P("Hay una regla que todos los bodegueros aplican y que le da el nombre al caso. La bebida helada se cobra por encima del precio sugerido: veinte céntimos en un día fresco y hasta un sol en Lima en los días más calientes. Por eso el precio que la base registra es el que la fuerza de ventas ve en el anaquel, no el que la marca decidió. Los precios, además, se mueven por escalones: se cobra 3.50, 3.80 o 4.00, nunca 3.73."),
        img("comic_fria.png", "Un bodeguero sostiene dos botellas, una al clima y una helada, mientras entra un cliente acalorado", "En la bodega la helada se cobra aparte: de veinte céntimos a un sol más."),
        H3("El Operativo Verano"),
        P("La rebaja que Saldaña quiere repetir tiene nombre y la hizo Volt. Desde la segunda semana de febrero hasta fines de marzo de 2025 la marca bajó su precio sugerido de S/ 4.00 a 3.20 en Lima y Piura, puso exhibidores en las bodegas y gastó más del doble en promoción. Toda la categoría discute todavía si fue un buen negocio."),
        img("comic_operativo.png", "Saldaña celebra frente a un refrigerador vacío mientras la gente sale con bebidas en la mano", "Saldaña lo resume así: “Bajas el precio, te llevas la cuadra”."),
        P("<b>La versión de Saldaña.</b> Las ventas semanales de Lima se duplicaron: pasaron de un promedio de 74,926 botellas en las dos semanas previas a 149,505 en las siete del operativo, con un pico de 179,628 en la primera. Según su cuenta, el operativo dejó S/ 248,000 a favor."),
        P("<b>La versión de Huamán.</b> Empieza donde termina la de Saldaña. En abril el precio volvió a 4.00 y las ventas no regresaron al nivel de antes: en las cinco semanas siguientes promediaron 61,349 botellas, un 18 % menos que antes del operativo. Con las semanas 14 a 19 dentro, el mismo cálculo da S/ 129,000 en contra."),
        P("<b>Lo que ninguno puede explicar.</b> El operativo empezó en vacaciones escolares, con calor y con la promoción casi duplicada. Y con el precio quieto en 3.20 las ventas se movieron solas: en las semanas 11 y 12 cayeron a unas 111,000 botellas y en la 13 volvieron a 156,316. Ximena Tafur, la analista, lo dijo así: “Se movieron el precio, la promoción y el calendario al mismo tiempo. Con esos datos no se puede saber quién hizo qué, ni cuánto se habría vendido sin tocar nada”."),
        LAB("Exhibit 4 · El Operativo Verano en Lima, semanas 5 a 19 de 2025"),
        tabla(["Semana", "Lunes", "Precio de bodega (S/)", "Promoción en bodega (S/)", "Temperatura media (°C)", "Feriado", "Botellas vendidas"], EXHIBIT4, (0, 2, 3, 4, 6)),
        '<p class="pie-tabla">Ventas de Volt en Lima. Cifras ficticias. La temperatura y el feriado no estaban en la base: Ximena Tafur los reconstruyó a mano para este periodo. El precio de Vive100 en Lima pasó de S/ 3.20 a 2.90 en la semana 12. Costo unitario puesto en bodega: S/ 1.70.</p>',
        H3("La meta del directorio"),
        P("El directorio pide para 2026 un <b>25 % más de utilidad</b> y <b>una decisión sobre Iquitos</b>, la plaza más cara de abastecer. Valeria y su equipo tienen dos años de datos, un presupuesto trimestral para repartir y una competencia que no se va a quedar quieta."),
        P("Este resumen deja fuera el detalle de las cinco ciudades, la discusión de Iquitos y la oferta de un proveedor de datos. Todo eso está en el caso completo, con sus cuatro exhibits."),
        f"<p>{DESCARGA_CASO}</p>",
    ])),
    ("Cómo se juega", "".join([
        P("Todas las rondas tienen los mismos cinco tiempos, siempre en este orden."),
        OL([
            "<b>Predicción.</b> Antes de tocar los datos, cada quien marca por su cuenta lo que cree que va a salir. Después el equipo conversa y registra una sola predicción, con su razón escrita y qué tan seguro está.",
            "<b>Modelo.</b> Descargan los datos, los limpian y corren la regresión fuera de la plataforma, en Colab y con tu asistente de IA. Al simulador solo se llevan los resultados.",
            "<b>Decisión.</b> Con el modelo aprobado, el equipo decide precio, promoción, publicidad y cobertura para cada ciudad.",
            "<b>Revelación.</b> El profesor cierra la ronda, el mercado se simula con las decisiones de las cinco marcas y todos ven cómo les fue.",
            "<b>Teoría.</b> Con el resultado a la vista, en clase se le pone nombre al concepto que acaban de usar.",
        ]),
        H3("Tres reglas que no cambian"),
        OL([
            "<b>La plataforma nunca corre la regresión.</b> Te entrega los datos, revisa tus números y simula el mercado. El análisis es tuyo.",
            "<b>Se califica la decisión con su evidencia.</b> Una frase sin número no vale. Los coeficientes se copian con cuatro cifras significativas y junto a cada uno va su error estándar, no el estadístico t ni el valor p.",
            "<b>Cada ronda se califica por separado.</b> El profesor la abre y la cierra. Antes de enviar, alguien más rehace el modelo sin mirar el borrador: si los números no coinciden, no se envía.",
        ]),
        P("El profesor abre y cierra cada ronda. Mientras la ronda está abierta pueden trabajar. Cuando se cierra, lo que no esté enviado y aprobado no cuenta, y una ronda cerrada no se vuelve a abrir."),
    ])),
    ("Los roles", "".join([
        P("Son los roles de siempre, quien pide y quien verifica, más uno nuevo que cuida la plata."),
        tabla(["Rol", "Qué hace"], [
            ["Analista", "Le pide el análisis al asistente, limpia los datos y llena el formulario con los resultados."],
            ["Auditor", "Rehace el modelo por su cuenta, sin ver el borrador del Analista, y firma si los números coinciden."],
            ["Gerente", "Escribe la interpretación, propone la decisión de la ronda y escribe la bitácora."],
            ["Controller", "Cuida la caja del equipo: aprueba los gastos y aprueba la decisión."],
        ]),
        P("En el grupo de tres, una persona lleva dos roles. En los grupos de cinco, dos personas comparten uno. No tienen que repartirlos ustedes: el Tablero le dice a cada quien el suyo, y los roles rotan cada dos rondas para que todos pasen por todos."),
        NOTA("<b>Regla para Zoom.</b> Quien pide no comparte pantalla hasta que quien verifica haya escrito su n. Si el Auditor ve el borrador antes de tener su propio número, la verificación ya no sirve."),
    ])),
    ("Ronda 1: la línea sobre la nube", "".join([
        LAB("Lo que pide Valeria"),
        '<div class="memo"><p>“Don Hernán quiere una sola cosa: saber qué pasa con las botellas si movemos el precio treinta céntimos. Pongan la primera línea sobre esa nube y díganme, en botellas, cuánto cambia la venta semanal por cada diez céntimos. No me importa todavía si la línea es perfecta: me importa que sea nuestra y saber qué tan lejos quedan los puntos”.</p><p class="firma">Valeria Chumpitaz, gerente de marca. Del memo de la ronda 1.</p></div>',
        LAB("Qué hacen"),
        P("La ronda empieza con la predicción: primero cada quien y luego el equipo. Después vienen los ocho pasos de la misión, que el Tablero muestra con su responsable. Si un paso no es tuyo, el Tablero te dice a quién esperas y qué puedes adelantar."),
        OL([f"<b>{rol}.</b> {paso}" for rol, paso in PASOS]),
        LAB("Qué pide el formulario"),
        P("El Analista elige la especificación de la ronda, <b>ventas = b<sub>0</sub> + b<sub>1</sub> · precio</b>, con las ventas en botellas y el precio en soles, sin transformar nada. Luego copia estos resultados."),
        tabla(["Casilla", "Qué va"], [
            ["Intercepto (b<sub>0</sub>)", "El valor, en botellas, y su error estándar."],
            ["Pendiente del precio (b<sub>1</sub>)", "El valor, en botellas por sol, y su error estándar."],
            ["R² ajustado", "El ajustado, no el R² simple."],
            ["n", "El número de filas con las que corrió el modelo."],
            ["Interpretación", "Un párrafo de 40 a 150 palabras que cite tus propios números."],
        ]),
        LAB("Tres pistas de prompt"),
        pista("1. Revisar antes de tocar",
              "este CSV sale de un sistema de ventas y trae errores. No borres ni corrijas nada todavía. Dame por columna el tipo de dato, mínimo, máximo, vacíos y valores distintos de cada texto, y cuántos obs_id se repiten. Luego lista las filas sospechosas con su obs_id.",
              "abre dos de esas filas y decide tú si el valor verdadero se puede recuperar o no. Anota cuántas filas quedan."),
        pista("2. La recta",
              "con las filas limpias ajusta ventas contra precio, sin transformar nada. Dame en una tabla intercepto, pendiente, sus errores estándar (no t ni p), R² ajustado y n, con cuatro cifras significativas.",
              "que el n sea igual a tus filas limpias y calcula a mano una semana con la ecuación."),
        pista("3. El párrafo lo escribes tú",
              "no lo reescribas. Dime si cito mi pendiente con signo y unidades, si explico el intercepto, si digo qué explica el R² y si recomiendo algo sobre el precio, y cuántas palabras tiene.",
              "don Hernán preguntó por treinta céntimos, ¿cuántas botellas son?"),
        NOTA("<b>No envíen para probar.</b> El primer envío es gratis, pero cada reintento le cuesta caja al equipo. El Auditor, por su parte, tiene solo tres intentos para que su réplica coincida con el borrador. Revisen antes de pulsar el botón."),
    ])),
    ("El archivo de datos", "".join([
        P("Cada marca descarga su propio archivo desde el simulador, en la pestaña de su rol. No es el mismo archivo para todos: cada marca tiene su propia historia, así que los números de otro equipo no te sirven. El archivo de la ronda 1 es el panel de dos años, con una fila por semana y ciudad y estas 14 columnas."),
        tabla(["Columna", "Unidad o valores", "Qué significa"], [[f"<code>{c}</code>", u, s] for c, u, s in DICCIONARIO]),
        P("El CSV usa coma como separador y punto decimal."),
        NOTA("<b>El archivo viene sucio a propósito,</b> como el de cualquier sistema de ventas real. Si corren el modelo sin limpiarlo, los números salen mal. Además, cada fila sucia que el equipo reporte en la pestaña “Limpieza de datos” suma puntos, y cualquier integrante puede reportar, sin importar su rol. Reportar una fila no la limpia en tu archivo: la limpieza la haces tú, en tu cuaderno, antes de correr el modelo."),
    ])),
    ("Doctor Beta y la nota", "".join([
        P("Dentro del simulador vas a encontrar al <b>Doctor Beta</b>, un tutor con IA. Funciona como un profesor que pasa por la mesa del equipo: hace preguntas y te orienta, pero no da las respuestas ni corre el modelo por ti. Es una IA y puede equivocarse, así que verifica lo que te diga. Ten presente también que el profesor puede leer la conversación."),
        P("Cada ronda cerrada tiene una nota de 0 a 100 que se arma con cuatro partes."),
        tabla(["Componente", "Peso", "De dónde sale"], [
            ["Análisis de la etapa", "60 %", "El mejor puntaje que el evaluador le dio a tu equipo en la etapa."],
            ["Resultado de la decisión", "15 %", "Cómo le fue a tu marca en el mercado con la decisión que tomaron."],
            ["Bitácora", "10 %", "La bitácora de la ronda que escribe el Gerente."],
            ["Participación individual", "15 %", "Cumplir tu rol, responder la predicción por tu cuenta y aportar al equipo."],
        ], (1,)),
        P("Las tres primeras partes son del equipo y la última es tuya. En la pestaña Resultados ves tu nota y de dónde sale."),
    ])),
    ("Calendario de rondas", "".join([
        P("Cada ronda se abre después de la clase que enseña su tema y se cierra a las 09:30 del día de clase siguiente. La revelación ocupa los primeros diez minutos de esa clase."),
        tabla(["Ronda", "Tema", "Se abre", "Se cierra"], CALENDARIO, (0,)),
        P("Estas fechas pueden moverse. Si cambian, el profesor avisa con tiempo por D2L."),
    ])),
    ("Qué leer antes del miércoles 18", "".join([
        P("Lee el caso completo, con sus cuatro exhibits, y vuelve a pasar por esta página. Son pocas páginas y todo lo que viene se apoya en ellas."),
        f"<p>{DESCARGA_CASO}</p>",
        P("Llega con estas dos preguntas pensadas. No hay que entregar nada, pero las vamos a conversar."),
        OL([
            "En la semana 7 de 2025, ¿qué tres cosas cambiaron a la vez? Búscalas en el Exhibit 4 y en el texto.",
            "¿Quién tiene razón, Saldaña o Huamán? ¿Y qué dato te haría cambiar de opinión?",
        ]),
    ])),
    ("Si algo falla", "".join([
        H3("No puedo entrar"),
        P("Revisa tres cosas: que el usuario sea tu correo institucional completo y en minúsculas, que la clave empiece con la p minúscula y lleve tu código con todos sus ceros, y que estés en un computador. Si sigue sin funcionar, escríbele al profesor."),
        H3("No veo el botón de descarga"),
        P("Solo el Analista y el Auditor descargan el panel de la ronda. Mira en el Tablero cuál es tu rol. Si eres Gerente o Controller, pídele a tu Analista que comparta el archivo con el equipo para que tú también puedas buscar filas sucias."),
        H3("El evaluador rechazó la entrega"),
        P("Lee primero lo que te devolvió: dice qué está bien y qué falta. Casi siempre el problema es que los números salieron de datos sin limpiar. Corrige fuera de la plataforma, vuelve a correr el modelo y recién entonces pide el reintento, que el Controller tiene que aprobar porque cuesta caja. Hay hasta cuatro intentos por ronda y cuenta el mejor."),
        H3("Mi n no coincide con el del Auditor"),
        P("Revisen que los dos usen el archivo de la misma ronda, la misma limpieza y la misma especificación. Una sola fila de más o de menos cambia el n y todo lo demás. Comparen cuántas filas descartó cada uno y por qué, sin mostrarse todavía los coeficientes."),
        H3("Me dice que espero a alguien"),
        P("Es normal: los pasos van en orden y cada uno tiene su responsable. La franja “Tu siguiente paso” te dice a quién esperas y qué puedes adelantar mientras tanto, por ejemplo buscar filas sucias o leer el caso. Si esa persona no está en clase, avísale al profesor, que puede reasignar el rol para esa ronda."),
    ])),
]

intro = P("Hoy empieza el simulador de regresión que nos acompaña hasta el final del semestre. En esta página está todo lo que necesitas para entrar, entender el caso y jugar la primera ronda con tu equipo.")
idx = "".join(f'<li><a href="#s{i}">{t}</a></li>' for i, (t, _) in enumerate(sec, 1))
cuerpo = "".join(f'<h2 id="s{i}">{t}</h2>{c}<p class="volver"><a href="#indice">&uarr; volver al índice</a></p>' for i, (t, c) in enumerate(sec, 1))
TIT = "Semana 12 · La fría cuesta más"
doc = f"""<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{TIT}</title><style>{CSS}</style></head>
<body><header class="cab"><div><p class="serie">ADM 2003 · Análisis de Datos · Lunes 16 de noviembre</p><h1>{TIT}</h1><p class="sub">Simulador de regresión por equipos</p></div></header>
<main>{intro}<nav class="indice" id="indice"><p>En esta página</p><ol>{idx}</ol></nav>
{cuerpo}<p class="pie">Ve al siguiente tema &rarr;</p></main></body></html>"""

for prohibido in ("—", "«", "»", "<script"):
    assert prohibido not in doc, f"El HTML contiene algo prohibido: {prohibido!r}"
salida = doc.encode("ascii", "xmlcharrefreplace").decode("ascii")
(OUT / NOMBRE).write_text(salida, encoding="ascii")
print(NOMBRE, f"{len(salida) / 1024:.0f} KB", "|", CASO_PDF, f"{(OUT / CASO_PDF).stat().st_size / 1024:.0f} KB")
