import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent / "project"
(ROOT / "slides").mkdir(parents=True, exist_ok=True)

INK, MUTE, BG = "#1e1e1e", "#5f6368", "#ffffff"
R, F, M, P = "#1f5fa8", "#d9701a", "#2e8b57", "#a6192e"
PU, TE = "#7b4fa0", "#0e8a8a"
TINT = {R: "#e8f0fa", F: "#fdf0e3", M: "#e6f4ec", P: "#f8e6e9", PU: "#f1eaf7", TE: "#e3f4f4"}
HEAD = "font-family:'Rubik', Arial, sans-serif"
BODY = "font-family:'Nunito Sans', Arial, sans-serif"
SEC = f"background:{BG};color:{INK};{BODY};padding:128px;display:flex;flex-direction:column;gap:48px"


def h2(t):
    return f'<h2 style="{HEAD};font-size:72px;font-weight:700;line-height:1.1;color:{INK}">{t}</h2>'


def eyebrow(t, col=P):
    return f'<p style="{HEAD};font-size:28px;font-weight:600;letter-spacing:2px;text-transform:uppercase;color:{col}">{t}</p>'


def notes(t):
    return f"<aside>{t}</aside>"


slides = {}

# 1 portada
slides["cover"] = f'''<section id="cover" data-transition="fade" style="{SEC};justify-content:center;gap:40px">
<div style="display:flex;gap:20px">
<div style="width:120px;height:120px;background:{R};border-radius:24px;display:flex;align-items:center;justify-content:center"><p style="{HEAD};font-size:72px;font-weight:700;color:#ffffff;text-align:center">R</p></div>
<div style="width:120px;height:120px;background:{F};border-radius:24px;display:flex;align-items:center;justify-content:center"><p style="{HEAD};font-size:72px;font-weight:700;color:#ffffff;text-align:center">F</p></div>
<div style="width:120px;height:120px;background:{M};border-radius:24px;display:flex;align-items:center;justify-content:center"><p style="{HEAD};font-size:72px;font-weight:700;color:#ffffff;text-align:center">M</p></div>
<div style="width:120px;height:120px;background:{P};border-radius:24px;display:flex;align-items:center;justify-content:center"><p style="{HEAD};font-size:72px;font-weight:700;color:#ffffff;text-align:center">P</p></div>
</div>
<h1 style="{HEAD};font-size:120px;font-weight:700;line-height:1.05;color:{INK}">¿A qué clientes debe cuidar Superstore?</h1>
<p style="font-size:44px;color:{MUTE}">ADM 2003 · Proyecto de medio semestre</p>
{notes("Presentamos el proyecto de medio semestre. Primero el método con el que trabajamos, después la herramienta RFM+P, y al final las cuatro etapas del trabajo.")}
</section>'''

# 2 CRISP-DM
fases = [("Entender el negocio", R), ("Entender los datos", F), ("Preparar los datos", M),
         ("Modelar", P), ("Evaluar", PU), ("Desplegar", TE)]
cards = "".join(
    f'<div style="flex:1;background:{TINT[c]};border-radius:24px;padding:36px 28px;display:flex;flex-direction:column;gap:20px">'
    f'<div style="width:80px;height:80px;background:{c};border-radius:50%;display:flex;align-items:center;justify-content:center">'
    f'<p style="{HEAD};font-size:44px;font-weight:700;color:#ffffff;text-align:center">{i}</p></div>'
    f'<p style="{HEAD};font-size:32px;font-weight:600;line-height:1.15;color:{INK}">{n}</p></div>'
    for i, (n, c) in enumerate(fases, 1))
slides["crisp"] = f'''<section id="crisp" data-transition="fade" style="{SEC}">
{eyebrow("Cómo trabajamos")}
{h2("CRISP-DM: seis fases para cualquier proyecto de datos")}
<div style="display:flex;gap:24px">{cards}</div>
<p style="font-size:36px;color:{MUTE}">Se avanza en orden, y se vuelve atrás cada vez que los datos sorprenden.</p>
{notes("CRISP-DM es el estándar de la industria para proyectos de minería de datos. Seis fases. Lo importante: es un ciclo. Si al modelar descubrimos algo raro en los datos, volvemos a prepararlos.")}
</section>'''

# 3 CRISP aplicado
rows = [("Entender el negocio", "¿A quién cuidar, recuperar o dejar de subsidiar?", "1", R),
        ("Entender los datos", "Qué es una fila y cuántos pedidos y clientes hay", "1", F),
        ("Preparar los datos", "Una tabla con una fila por cliente: R, F, M y P", "2", M),
        ("Modelar", "Notas de 1 a 5 y grupos con nombre", "3", P),
        ("Evaluar", "¿Tienen sentido los grupos? ¿Qué dice la utilidad?", "3 y 4", PU),
        ("Desplegar", "Recomendaciones que la gerencia pueda usar", "4", TE)]
filas = "".join(
    f'<div style="display:flex;gap:24px;align-items:center;background:{TINT[c]};border-radius:16px;padding:14px 28px">'
    f'<p style="{HEAD};width:380px;font-size:30px;font-weight:600;color:{c}">{a}</p>'
    f'<p style="flex:1;font-size:28px;color:{INK}">{b}</p>'
    f'<p style="width:150px;font-size:28px;color:{INK};text-align:right">Etapa {e}</p></div>'
    for a, b, e, c in rows)
slides["crisp-rfmp"] = f'''<section id="crisp-rfmp" data-transition="fade" style="{SEC};gap:32px">
{eyebrow("Cómo trabajamos")}
{h2("Las seis fases en este proyecto")}
<div style="display:flex;flex-direction:column;gap:14px">{filas}</div>
{notes("Cada fase de CRISP-DM tiene su lugar en el proyecto. Las cuatro etapas del trabajo recorren el ciclo completo, de la pregunta de negocio a la recomendación.")}
</section>'''

# 4 cuatro letras
letras = [("R", "Recencia", "¿Hace cuántos días compró por última vez?", R),
          ("F", "Frecuencia", "¿Cuántos pedidos ha hecho?", F),
          ("M", "Monto", "¿Cuánto ha comprado en total?", M),
          ("P", "Utilidad", "¿Cuánto ha ganado la empresa con él?", P)]
cols = "".join(
    f'<div style="flex:1;display:flex;flex-direction:column;gap:16px">'
    f'<p style="{HEAD};font-size:240px;font-weight:700;line-height:1;color:{c}">{l}</p>'
    f'<p style="{HEAD};font-size:44px;font-weight:600;color:{INK}">{w}</p>'
    f'<p style="font-size:32px;line-height:1.35;color:{MUTE}">{q}</p></div>'
    for l, w, q, c in letras)
slides["letras"] = f'''<section id="letras" data-transition="fade" style="{SEC}">
{eyebrow("La herramienta")}
{h2("Cuatro preguntas sobre cada cliente")}
<div style="display:flex;gap:48px">{cols}</div>
{notes("RFM viene del marketing directo de los años sesenta y lo popularizó Arthur Hughes en los noventa. Las tres primeras letras miden comportamiento. La P la agregamos nosotros, porque vender no es lo mismo que ganar.")}
</section>'''

# 5 Rosa
tiles = "".join(
    f'<div style="background:{c};border-radius:24px;padding:32px 36px;display:flex;flex-direction:column;gap:4px">'
    f'<p style="{HEAD};font-size:32px;font-weight:600;color:#ffffff">{l}</p>'
    f'<p style="{HEAD};font-size:72px;font-weight:700;color:#ffffff">{v}</p></div>'
    for l, v, c in [("R", "10 días", R), ("F", "3 pedidos", F), ("M", "$500", M), ("P", "$60", P)])
slides["rosa"] = f'''<section id="rosa" data-transition="fade" style="{SEC}">
{eyebrow("La herramienta")}
{h2("Un ejemplo: Rosa")}
<div style="display:flex;gap:64px;align-items:center">
<div style="flex:1;display:flex;flex-direction:column;gap:24px">
<p style="font-size:44px;line-height:1.35">Rosa compró tres veces.</p>
<p style="font-size:44px;line-height:1.35">La última fue hace 10 días.</p>
<p style="font-size:44px;line-height:1.35">En total gastó $500.</p>
<p style="font-size:44px;line-height:1.35">La tienda le ganó $60.</p>
</div>
<div style="width:760px;display:grid;grid-template-columns:1fr 1fr;gap:24px">{tiles}</div>
</div>
{notes("Rosa es inventada. Cada cliente de Superstore termina así: cuatro números. El proyecto empieza cuando tenemos esta tabla para los 793 clientes.")}
</section>'''

# 6 notas 1 a 5
def barra(col, labels):
    def mix(a):
        h = col.lstrip("#"); rgb = [int(h[i:i+2], 16) for i in (0, 2, 4)]
        return "#" + "".join(f"{round(255 - (255 - v) * a):02x}" for v in rgb)
    alphas = [0.2, 0.4, 0.6, 0.8, 1.0]
    return "".join(
        f'<div style="flex:1;background:{mix(a)};border-radius:12px;padding:20px;display:flex;justify-content:center">'
        f'<p style="{HEAD};font-size:44px;font-weight:700;color:{INK if a < 0.6 else "#ffffff"};text-align:center">{n}</p></div>'
        for a, n in zip(alphas, labels))


slides["notas"] = f'''<section id="notas" data-transition="fade" style="{SEC};gap:36px">
{eyebrow("La herramienta")}
{h2("Cada letra se convierte en una nota de 1 a 5")}
<p style="font-size:32px;color:{MUTE}">Se ordena a los clientes y se parten en cinco partes iguales. Cada parte es el 20 %.</p>
<div style="display:flex;flex-direction:column;gap:12px">
<p style="font-size:32px;font-weight:700;color:{M}">F, M y P: más es mejor</p>
<div style="display:flex;gap:12px">{barra(M, [1, 2, 3, 4, 5])}</div>
<div style="display:flex;justify-content:space-between"><p style="font-size:28px;color:{MUTE}">compra poco</p><p style="font-size:28px;color:{MUTE}">compra mucho</p></div>
</div>
<div style="display:flex;flex-direction:column;gap:12px">
<p style="font-size:32px;font-weight:700;color:{R}">R: al revés, menos días es mejor</p>
<div style="display:flex;gap:12px">{barra(R, [1, 2, 3, 4, 5])}</div>
<div style="display:flex;justify-content:space-between"><p style="font-size:28px;color:{MUTE}">no compra hace mucho</p><p style="font-size:28px;color:{MUTE}">compró hace poco</p></div>
</div>
{notes("El error más común es olvidar dar vuelta la R. Si quien compró ayer recibe 1, todos los grupos quedan al revés.")}
</section>'''

# 7 tabla de grupos
MAPA = [(r"[1-2][1-2]", "Hibernando"), (r"[1-2][3-4]", "En riesgo"), (r"[1-2]5", "No se pueden perder"),
        (r"3[1-2]", "Por dormirse"), (r"33", "Necesitan atención"), (r"[3-4][4-5]", "Leales"),
        (r"41", "Prometedores"), (r"51", "Nuevos"), (r"[4-5][2-3]", "Potenciales leales"), (r"5[4-5]", "Campeones")]
import re
GC = {"Campeones": (P, "#ffffff"), "Leales": ("#e7a3ad", INK), "Potenciales leales": ("#f8e6e9", INK),
      "Nuevos": ("#e6f4ec", INK), "Prometedores": ("#b9e0c8", INK), "Necesitan atención": ("#fde3c8", INK),
      "Por dormirse": ("#f6c08e", INK), "En riesgo": ("#c9dbf2", INK), "No se pueden perder": (R, "#ffffff"),
      "Hibernando": ("#ececec", INK)}


def grupo(r, f):
    for rx, n in MAPA:
        if re.fullmatch(rx, f"{r}{f}"):
            return n


cells = ['<div></div>'] + [f'<p style="font-size:28px;font-weight:700;color:{F};text-align:center">F = {f}</p>' for f in range(1, 6)]
for r in range(5, 0, -1):
    cells.append(f'<p style="font-size:28px;font-weight:700;color:{R};text-align:right">R = {r}</p>')
    for f in range(1, 6):
        n = grupo(r, f)
        bg, fg = GC[n]
        cells.append(f'<div style="background:{bg};border-radius:10px;padding:10px;display:flex;align-items:center;justify-content:center">'
                     f'<p style="font-size:24px;font-weight:600;line-height:1.15;color:{fg};text-align:center">{n}</p></div>')
slides["grupos"] = f'''<section id="grupos" data-transition="fade" style="{SEC};gap:28px">
{eyebrow("La herramienta")}
{h2("Con las notas de R y F, cada cliente cae en un grupo")}
<div style="display:grid;grid-template-columns:140px 1fr 1fr 1fr 1fr 1fr;grid-template-rows:44px 88px 88px 88px 88px 88px;gap:8px;align-items:center">{"".join(cells)}</div>
{notes("Esta tabla es una convención muy usada. Arriba a la derecha compraron hace poco y compran seguido: Campeones. Abajo a la derecha compraban mucho y desaparecieron: No se pueden perder. M y P se usan después para describir y priorizar cada grupo.")}
</section>'''

# 8 por qué la P
slides["por-que-p"] = f'''<section id="por-que-p" data-transition="fade" style="{SEC}">
{eyebrow("La herramienta")}
{h2("Vender mucho no es lo mismo que ganar")}
<div style="display:flex;gap:40px">
<div style="flex:1;background:{TINT[P]};border-radius:24px;padding:48px;display:flex;flex-direction:column;gap:16px">
<p style="{HEAD};font-size:44px;font-weight:700">Ana</p>
<p style="font-size:32px">Compra $10,000 con 50 % de descuento</p>
<p style="{HEAD};font-size:96px;font-weight:700;color:{P}">−$800</p>
<p style="font-size:32px;color:{MUTE}">La tienda pierde con ella</p>
</div>
<div style="flex:1;background:{TINT[M]};border-radius:24px;padding:48px;display:flex;flex-direction:column;gap:16px">
<p style="{HEAD};font-size:44px;font-weight:700">Luis</p>
<p style="font-size:32px">Compra $3,000 sin descuento</p>
<p style="{HEAD};font-size:96px;font-weight:700;color:{M}">+$600</p>
<p style="font-size:32px;color:{MUTE}">La tienda gana con él</p>
</div>
</div>
<p style="font-size:36px">Con RFM, Ana parece la mejor clienta. La P muestra lo contrario.</p>
{notes("Ana y Luis son inventados, pero en Superstore pasa lo mismo y lo van a encontrar. Por eso este curso trabaja RFM+P y no solo RFM.")}
</section>'''

# 9 cuatro etapas
etapas = [("Conocer los datos", "Descripción de la base y lista de problemas", R),
          ("Calcular R, F, M y P", "Tabla de clientes e histogramas", F),
          ("Armar los grupos", "Tabla de grupos con % de ventas y de utilidad", M),
          ("Explicar y recomendar", "Informe final y defensa oral", P)]
ec = "".join(
    f'<div style="flex:1;background:{TINT[c]};border-radius:24px;padding:40px 32px;display:flex;flex-direction:column;gap:20px">'
    f'<p style="{HEAD};font-size:96px;font-weight:700;line-height:1;color:{c}">{i}</p>'
    f'<p style="{HEAD};font-size:40px;font-weight:600;line-height:1.15">{t}</p>'
    f'<p style="font-size:28px;line-height:1.35;color:{MUTE}">Entregan: {e}</p></div>'
    for i, (t, e, c) in enumerate(etapas, 1))
slides["etapas"] = f'''<section id="etapas" data-transition="fade" style="{SEC}">
{eyebrow("El trabajo")}
{h2("Cuatro etapas, en grupo")}
<div style="display:flex;gap:24px">{ec}</div>
<p style="font-size:36px">Cada etapa termina con preguntas que se responden con un número. Las revisamos juntos en clase.</p>
{notes("Las tres primeras etapas son puntos de control: si sus números coinciden con los míos, siguen. Si no, encuentran el error antes de avanzar. La cuarta es el informe y la defensa.")}
</section>'''

# 10-13 cada etapa
DET = [
 ("Conocer los datos", R, ["Cuenten filas, pedidos y clientes.", "Busquen problemas: datos vacíos, filas repetidas, fechas raras.", "Anoten cada problema y qué hicieron con él."],
  ["¿Cuántas filas, pedidos y clientes tiene la base?", "¿Cuántas filas repetidas encontraron?"],
  "Cada fila es un producto dentro de un pedido, no un pedido completo."),
 ("Calcular R, F, M y P", F, ["Usen como fecha de hoy el 30 de agosto de 2026.", "Una fila por cliente con R, F, M y P.", "Un histograma de cada letra y una frase sobre lo que ven."],
  ["¿Cuánto les dio R, F, M y P de Adrian Barton (AB-10105)?", "¿Cuántos clientes tienen P negativa?"],
  "F cuenta pedidos distintos, no filas."),
 ("Armar los grupos", M, ["Notas de 1 a 5 en cada letra. La R va al revés.", "Ubiquen a cada cliente en la tabla de grupos.", "Por grupo: cuántos clientes, cuánto vende, cuánto gana."],
  ["¿Qué notas tiene Adrian Barton y en qué grupo quedó?", "¿Cuántos clientes quedaron en Campeones y en Hibernando?", "¿Cuánto les dio la P de Sean Miller, el que más compra?"],
  "Expliquen cómo resolvieron los empates."),
 ("Explicar y recomendar", P, ["Busquen qué tienen en común las ventas que pierden plata.", "Comparen Consumidor, Corporativo y Oficina en casa.", "Para cada grupo, una acción y cómo sabrían si funcionó."],
  ["¿Qué % de la utilidad aporta el 20 % de clientes más rentable?", "¿Qué % de las filas con descuento mayor a 20 % pierde plata?", "¿Cuánta utilidad suman En riesgo y No se pueden perder?", "¿Qué margen tiene cada segmento comercial?"],
  "Recomendaciones para Superstore, no para cualquier tienda."),
]
for i, (t, c, hacer, preg, ojo) in enumerate(DET, 1):
    pasos = "".join(
        f'<div style="display:flex;gap:20px;align-items:center">'
        f'<div style="width:64px;height:64px;background:{c};border-radius:50%;display:flex;align-items:center;justify-content:center;flex:none">'
        f'<p style="{HEAD};font-size:32px;font-weight:700;color:#ffffff;text-align:center">{k}</p></div>'
        f'<p style="font-size:34px;line-height:1.3">{h}</p></div>' for k, h in enumerate(hacer, 1))
    qs = "".join(f'<p style="font-size:28px;line-height:1.35"><b style="color:{c}">{i}.{k}</b>  {q}</p>' for k, q in enumerate(preg, 1))
    slides[f"etapa{i}"] = f'''<section id="etapa{i}" data-transition="fade" style="{SEC};gap:40px">
<div style="display:flex;gap:32px;align-items:center">
<p style="{HEAD};font-size:160px;font-weight:700;line-height:1;color:{c}">{i}</p>
<div style="display:flex;flex-direction:column;gap:8px">{eyebrow("Etapa " + str(i), c)}{h2(t)}</div>
</div>
<div style="display:flex;gap:48px">
<div style="flex:1;display:flex;flex-direction:column;gap:28px">{pasos}
<p style="font-size:30px;color:{MUTE};line-height:1.35">{ojo}</p></div>
<div style="width:760px;background:{TINT[c]};border-radius:24px;padding:40px;display:flex;flex-direction:column;gap:18px">
<p style="{HEAD};font-size:32px;font-weight:700;color:{c}">Respondan con un número</p>{qs}</div>
</div>
{notes(f"Etapa {i}. Las preguntas de la derecha van en la hoja de respuestas al inicio del cuaderno. En clase las revisamos grupo por grupo.")}
</section>'''

# 14 IA
ia = [("Los números salen de su cuaderno, no del chat", R), ("Cada decisión, explicada con sus palabras", M), ("Al final del cuaderno, el prompt que usaron", F)]
iac = "".join(
    f'<div style="flex:1;background:{TINT[c]};border-radius:24px;padding:48px 40px;display:flex;flex-direction:column;gap:28px">'
    f'<x-icon name="Check" style="color:{c};width:72px;height:72px"></x-icon>'
    f'<p style="{HEAD};font-size:40px;font-weight:600;line-height:1.2">{t}</p></div>' for t, c in ia)
slides["ia"] = f'''<section id="ia" data-transition="fade" style="{SEC}">
{eyebrow("Reglas")}
{h2("Pueden usar IA todo lo que quieran, con tres condiciones")}
<div style="display:flex;gap:24px">{iac}</div>
<p style="font-size:36px">En la defensa cualquiera del grupo puede recibir cualquier pregunta, y se responde sin leer.</p>
{notes("La IA ayuda mucho con el código. Lo que evaluamos es que entiendan lo que hicieron. Las preguntas de control con clientes concretos solo se responden corriendo el cuaderno.")}
</section>'''

# 15 nota
crit = [("Números correctos", "Se ve en la hoja de respuestas", R), ("Decisiones explicadas", "Qué hicieron y por qué", F),
        ("Usan la utilidad", "No solo las ventas", M), ("Recomendaciones para Superstore", "Concretas y defendibles", P)]
cc = "".join(
    f'<div style="display:flex;flex-direction:column;gap:12px;background:{TINT[c]};border-radius:24px;padding:36px 40px">'
    f'<p style="{HEAD};font-size:44px;font-weight:700;color:{c}">{a}</p><p style="font-size:30px;color:{MUTE}">{b}</p></div>'
    for a, b, c in crit)
slides["nota"] = f'''<section id="nota" data-transition="fade" style="{SEC}">
{eyebrow("Reglas")}
{h2("Qué cuenta en la nota")}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:24px">{cc}</div>
{notes("Cuatro criterios, en orden de importancia.")}
</section>'''

# 16 cierre
slides["empezar"] = f'''<section id="empezar" data-transition="fade" style="{SEC};justify-content:center;gap:40px">
{eyebrow("Para empezar")}
<h1 style="{HEAD};font-size:96px;font-weight:700;line-height:1.1">Abran superstore_2026.csv y respondan la pregunta 1.1</h1>
<div style="display:flex;gap:20px">
<p style="font-size:36px;background:{R};color:#ffffff;padding:16px 32px;border-radius:40px">¿Cuántas filas?</p>
<p style="font-size:36px;background:{F};color:#ffffff;padding:16px 32px;border-radius:40px">¿Cuántos pedidos?</p>
<p style="font-size:36px;background:{M};color:#ffffff;padding:16px 32px;border-radius:40px">¿Cuántos clientes?</p>
</div>
{notes("Diez minutos en grupo y comparamos los números en voz alta.")}
</section>'''

order = ["cover", "crisp", "crisp-rfmp", "letras", "rosa", "notas", "grupos", "por-que-p", "etapas",
         "etapa1", "etapa2", "etapa3", "etapa4", "ia", "nota", "empezar"]
for k in order:
    (ROOT / "slides" / f"{k}.html").write_text(slides[k], encoding="utf-8")
deck = {"v": 4, "createdOnFiles": {"v": 1, "at": "2026-10-05T14:18:12Z"}, "lists": "css",
        "title": "RFM+P Superstore", "order": order,
        "sections": {"s1": {"description": "Cómo trabajamos: el ciclo CRISP-DM aplicado al proyecto", "start": "cover"},
                     "s2": {"description": "RFM+P: qué mide y cómo se arma", "start": "letras"},
                     "s3": {"description": "El trabajo: cuatro etapas con preguntas de control", "start": "etapas"}},
        "cover": "cover",
        "faces": {"rubik": {"family": "Rubik", "href": "https://fonts.googleapis.com/css2?family=Rubik:wght@400..700&display=swap"},
                  "nunito-sans": {"family": "Nunito Sans", "href": "https://fonts.googleapis.com/css2?family=Nunito+Sans:wght@400;600;700&display=swap"}},
        "designSystems": []}
(ROOT / "deck.json").write_text(json.dumps(deck, ensure_ascii=False, indent=1), encoding="utf-8")
print(len(order))
