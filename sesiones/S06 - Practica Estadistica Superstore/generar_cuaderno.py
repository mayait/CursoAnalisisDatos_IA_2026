#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genera la práctica de estadística descriptiva sobre Superstore (v2).

Inspirada en EstadisticaDescriptivaPython.ipynb (Credit): misma caja de
herramientas y mismos ajíes 🌶 con bloque `Respuesta:`, pero:
  - TODO el análisis corre sobre `pedidos` (ventas agrupadas por pedido_id),
    porque las preguntas de María son sobre pedidos, no sobre líneas.
  - Ejemplos trabajados con su prompt de bitácora (🤖) donde la IA ayudó.
  - Cada resultado trabajado lleva su lectura («Qué significa»).
  - Un solo gráfico por celda de código.

Salidas:
  sitio/labs/taller_estadistica_superstore.ipynb    (estudiante, con 🌶️)
  ./taller_estadistica_superstore_SOLUCIONES.ipynb   (profesor)
"""
import json
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parent.parent
AJI = "\U0001F336️" * 7

BADGE = ("https://colab.research.google.com/github/mayait/"
         "CursoAnalisisDatos_IA_2026/blob/main/sitio/labs/"
         "taller_estadistica_superstore.ipynb")

celdas = []


def md(src):
    celdas.append(("markdown", src, None))


def code(src, sol=None):
    celdas.append(("code", src, sol))


def prompt(texto):
    md(f"""> 🤖 **El prompt de la bitácora** — Este ejemplo se escribió con ayuda de IA. El prompt exacto, tal como va registrado:
>
> *«{texto}»*""")


# ══ Portada ══════════════════════════════════════════════════════════════
md(f"""<a href="{BADGE}" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Abrir en Colab"/></a>

# Práctica · Estadística descriptiva con Python

La caja de herramientas completa —tendencia central, dispersión, posición, forma y correlación— sobre **Superstore**. María pregunta por **pedidos**, así que todo el análisis corre sobre las ventas **agrupadas por `pedido_id`**: la granularidad correcta para sus preguntas. Cada sección trae un ejemplo resuelto que corre tal cual (con el prompt de bitácora cuando la IA ayudó a escribirlo, y la lectura de qué significa el resultado) y un **ají 🌶** que resuelves tú. Donde veas {AJI} va tu código.""")

code('#@title Nombre del estudiante\nEstudiante = "" #@param {type:"string"}\nCodigo = "" #@param {type:"string"}')

md("""> **Hoy haces** · Seis encargos de María, la gerente regional Oeste. Los ejemplos resueltos son tuyos para ejecutar y leer; los ajíes 🌶 traen la respuesta esperada para que verifiques tu código.
>
> **Entrega** · El cuaderno ejecutado de principio a fin, con los seis ajíes resueltos y el memo final. Nombre: `practica_estadistica_apellido.ipynb`, al buzón de D2L. Si usaste IA en algún ají, el prompt va en tu bitácora — igual que hacemos aquí con los ejemplos.

---

## El caso · Miércoles, 16h40

> **[16h32] María** — El comité aprobó lo del pedido típico, y ahora quieren más: un **expediente descriptivo completo** para la junta del viernes. Ojo: a mí me facturan por **pedidos**, no por líneas de una tabla. Cada número que me mandes es sobre pedidos completos. Te paso los encargos numerados. — M.""")

# ══ 1 · Dataset y granularidad ════════════════════════════════════════════
md("""## 1. El dataset de trabajo — y la granularidad correcta

**Superstore:** cuatro años de ventas (sep-2022 a ago-2026) de una cadena minorista de EE. UU. En el archivo, cada fila es una **línea de venta** (un producto dentro de un pedido). Las columnas de hoy:

| Columna | Qué es |
|---|---|
| `pedido_id` | El pedido al que pertenece la línea |
| `segmento` | Consumidor, Corporativo u Oficina en casa |
| `venta` | Ingreso de la línea en USD, con el descuento ya aplicado |
| `cantidad` | Unidades vendidas en la línea |
| `descuento` | Fracción descontada (0 = sin descuento, 0.7 = 70 %) |
| `utilidad` | Ganancia de la línea en USD (puede ser negativa) |""")

code("""# --- Setup del entorno ---
import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid", palette="deep")
plt.rcParams["figure.figsize"] = (10, 4)
pd.set_option("display.max_columns", 40)
pd.set_option("display.float_format", lambda v: f"{v:,.2f}")

URL = ("https://raw.githubusercontent.com/mayait/"
       "CursoAnalisisDatos_IA_2026/main/sitio/datos/superstore_2026.csv")
print("Setup completo \\u2713")""")

md("""### Importar el dataset
`pd.read_csv()` importa un archivo de texto a pandas. Recuerda del inventario de calidad: las fechas se declaran al cargar con `parse_dates`.""")

code(f"df = {AJI}\nprint(df.shape)   # debe imprimir: (9994, 21)",
     'df = pd.read_csv(URL, parse_dates=["fecha_pedido", "fecha_envio"])\nprint(df.shape)   # debe imprimir: (9994, 21)')

code("df.sample(4)")

md("""### De líneas a pedidos

María factura por pedidos. Si calculamos sobre las 9 994 líneas estaríamos respondiendo **otra pregunta** (¿cuánto vale una línea?). Construimos la tabla `pedidos`: una fila por pedido.""")

prompt("En pandas tengo un DataFrame df donde cada fila es una línea de venta, con columnas pedido_id, venta, utilidad, cantidad, descuento y segmento. Constrúyeme una tabla `pedidos` con una fila por pedido: venta, utilidad y cantidad sumadas, descuento promedio de sus líneas, número de líneas y el segmento del pedido.")

code("""# Una fila por pedido: la granularidad de las preguntas de María
pedidos = df.groupby("pedido_id").agg(
    venta=("venta", "sum"),
    utilidad=("utilidad", "sum"),
    cantidad=("cantidad", "sum"),
    descuento_medio=("descuento", "mean"),
    lineas=("venta", "size"),
    segmento=("segmento", "first"),   # un pedido pertenece a un solo cliente
)
print(f"{len(pedidos):,} pedidos, {pedidos['lineas'].mean():.1f} líneas por pedido en promedio")
pedidos.head(3)""")

md("""**Qué significa:** pasamos de 9 994 líneas a **5 009 pedidos** (~2 líneas por pedido). De aquí en adelante, cada media, cuartil o correlación se lee como «...por pedido». Si en tu proyecto la unidad de análisis está mal, todo lo que sigue estará bien calculado y mal respondido.""")

# ══ 2 · Tendencia central ════════════════════════════════════════════════
md("""## 2. Medidas de tendencia central

> **Encargo 1 de María** — «Para abrir el expediente: ¿cuánto vale un **pedido típico**? Quiero las tres medidas y cuál me recomiendas.»

Primero se mira la distribución; después se calcula. Siempre en ese orden.""")

prompt("Con seaborn, un histograma de la columna venta de la tabla pedidos con curva de densidad, y título que diga qué estoy viendo.")

code("""sns.histplot(pedidos["venta"], bins=100, kde=True)
plt.title("Distribución de la venta por pedido — rango completo")
plt.show()""")

code("""# El eje llega a $23,661 pero casi todo vive muy a la izquierda: zoom
sns.histplot(pedidos.loc[pedidos["venta"] < 2000, "venta"], bins=60, kde=True, color="darkred")
plt.title("La misma distribución, pedidos de menos de $2,000")
plt.show()""")

md("""**Qué significa:** la venta por pedido tiene una **cola derecha larguísima**: montones de pedidos chicos y unos pocos gigantes. Con esta forma ya sabes qué le va a pasar a la media.""")

code("""# Medidas de tendencia central de la venta por pedido (ejemplo resuelto)
media_venta   = pedidos["venta"].mean()
mediana_venta = pedidos["venta"].median()
moda_venta    = pedidos["venta"].mode()

print("Media:  ", round(media_venta, 2))     # 458.61
print("Mediana:", round(mediana_venta, 2))   # 151.96
print("Moda:   ", round(moda_venta[0], 2))   # 12.96

pct_bajo_media = (pedidos["venta"] < media_venta).mean() * 100
print(f"Pedidos por debajo de la media: {pct_bajo_media:.1f}%")   # 72.5%""")

md("""**Qué significa:** el pedido «promedio» vale \\$458.61, pero el **72.5 % de los pedidos vale menos que eso** — la media viaja con los pedidos gigantes. La mediana (\\$151.96) sí parte a los pedidos en mitades y es la medida honesta del «típico». La moda (\\$12.96, apenas 14 pedidos) es anécdota: en variables continuas la moda casi nunca resume nada. **Recomendación para María: la mediana.** Es exactamente la trampa del Taller 5, ahora derivada con la granularidad correcta.""")

md("""# 🌶 1

**Encargo:** obtener el promedio, la mediana y la moda de la columna `cantidad` de la tabla **`pedidos`** (unidades por pedido).

```
Respuesta:
Media:   7.561
Mediana: 6.0
Moda:    3
```

**Pregunta de María:** aquí salió moda < mediana < media. ¿Qué te dice ese *orden* sobre la forma de la distribución de unidades por pedido? Contesta en un comentario.""")

code(f"""# Promedio, mediana y moda de `cantidad` en pedidos
media_cant   = {AJI}
mediana_cant = {AJI}
moda_cant    = {AJI}

print("Media:  ", round(media_cant, 4))
print("Mediana:", mediana_cant)
print("Moda:   ", moda_cant[0])

# Tu respuesta a María: ...""",
     """# Promedio, mediana y moda de `cantidad` en pedidos
media_cant   = pedidos["cantidad"].mean()
mediana_cant = pedidos["cantidad"].median()
moda_cant    = pedidos["cantidad"].mode()

print("Media:  ", round(media_cant, 4))
print("Mediana:", mediana_cant)
print("Moda:   ", moda_cant[0])

# Tu respuesta a María: moda < mediana < media es la firma de una cola derecha:
# lo más frecuente son pedidos de pocas unidades, y los pedidos grandes jalan
# la media hacia arriba. Cola moderada aquí (7.6 vs 6), no extrema como en venta.""")

# ══ 3 · Dispersión ═══════════════════════════════════════════════════════
md("""## 3. Medidas de dispersión

> **Encargo 2 de María** — «Ese pedido típico, ¿de fiar o de mentira? Necesito el *ancho* de los pedidos, no solo el centro.»

### Rango""")

code("""print("El pedido mínimo es:", round(pedidos["venta"].min(), 2))    # 0.56
print("El pedido máximo es:", round(pedidos["venta"].max(), 2))    # 23,661.23
print("El rango es:", round(pedidos["venta"].max() - pedidos["venta"].min(), 2))""")

md("""**Qué significa:** entre el pedido más chico (\\$0.56) y el más grande (\\$23,661) caben cuatro órdenes de magnitud. El rango usa solo dos observaciones —las más extremas—, así que es la medida de dispersión más frágil: un solo pedido raro lo dispara.

### Varianza y desviación estándar
* El argumento `ddof` define el denominador: `N - ddof`
* `ddof=0` si trabajas con la **población**
* `ddof=1` (el default de pandas) si trabajas con una **muestra**""")

code("""print("Varianza muestral:         ", round(pedidos["venta"].var(), 2))
print("Desv. estándar muestral:   ", round(pedidos["venta"].std(), 2))       # 954.73
print("Desv. estándar poblacional:", round(pedidos["venta"].std(ddof=0), 2)) # 954.64""")

md("""**Qué significa:** la desviación estándar (\\$954.73) mide el alejamiento «típico» respecto de la media — y aquí es **el doble de la media misma** (\\$458.61) y seis veces la mediana. Traducción: los pedidos no se parecen entre sí; cualquier promedio va acompañado de una nube enorme. (Con 5 009 pedidos, la versión muestral y la poblacional casi coinciden: el `ddof` importa en muestras chicas.)""")

md("""# 🌶 2

**Encargo:** obtener el rango, la varianza muestral y la desviación estándar muestral de la columna `utilidad` de la tabla **`pedidos`**.

```
Respuesta:
Rango: 15654.76
Varianza muestral: 118982.05
Desv. estándar muestral: 344.94
```

**Pregunta de María:** la utilidad media por pedido es \\$57.18 y su desviación estándar \\$344.94. En una frase: ¿por qué ese par de números debería quitarle el sueño a un gerente?""")

code(f"""# Rango, varianza muestral y desviación estándar muestral de `utilidad` en pedidos
{AJI}

# Tu frase para María: ...""",
     """# Rango, varianza muestral y desviación estándar muestral de `utilidad` en pedidos
rango_util = pedidos["utilidad"].max() - pedidos["utilidad"].min()
var_util   = pedidos["utilidad"].var()
std_util   = pedidos["utilidad"].std()

print("Rango:", round(rango_util, 2))
print("Varianza muestral:", round(var_util, 2))
print("Desv. estándar muestral:", round(std_util, 2))

# Para María: el resultado "típico" de un pedido es +-345 alrededor de 57:
# un pedido cualquiera puede ganar o PERDER seis veces la utilidad promedio.
# El promedio solo, aquí, es propaganda.""")

md("""`jointplot` muestra el scatterplot y la distribución de cada variable a la vez — útil para ver la dispersión conjunta de dos columnas:""")

code("""sns.jointplot(data=pedidos, x="venta", y="utilidad", height=6, alpha=0.3)
plt.suptitle("Venta vs. utilidad por pedido", y=1.02)
plt.show()""")

md("""**Qué significa:** la nube sube hacia la derecha (vender más se asocia con ganar más) pero se **abre en abanico**: entre los pedidos grandes conviven ganancias y pérdidas enormes. Volvemos a esto en la sección 6 con un número.""")

# ══ 4 · Posición ═════════════════════════════════════════════════════════
md("""## 4. Medidas de posición

> **Encargo 3 de María** — «Envío gratis versión 2: quiero umbrales por *posición*. ¿Debajo de qué venta está el 90 % de los pedidos? ¿Y desde dónde un pedido es oficialmente raro?»

`describe()` muestra los cuartiles por defecto; `quantile()` te da cualquier percentil.""")

code("""pedidos["venta"].describe()""")

code("""# Percentil 90: nueve de cada diez pedidos valen menos que esto
print("P90 de la venta por pedido:", round(pedidos["venta"].quantile(0.90), 2))   # 1,153.83""")

md("""**Qué significa:** si María pone «envío gratis desde \\$1,150», le regala el envío a ~10 % de los pedidos — los más grandes. Los percentiles convierten una distribución entera en umbrales accionables: es la herramienta de negocio más directa de esta sección.

### Rango intercuartil (IQR)
La distancia entre Q1 y Q3: el ancho de la **mitad central** de los pedidos, inmune a los extremos.""")

code("""print("IQR con scipy: ", round(stats.iqr(pedidos["venta"]), 2))
print("IQR a mano:    ", round(pedidos["venta"].quantile(0.75) - pedidos["venta"].quantile(0.25), 2))""")

md("""**Qué significa:** la mitad central de los pedidos cabe en una franja de \\$474. Compárala con la desviación estándar (\\$954): cuando el IQR y la std cuentan historias tan distintas, es otra señal de cola larga — la std está inflada por los extremos y el IQR no.

### Box-plot y valores atípicos
Un box-plot dibuja exactamente estas medidas. Se consideran **atípicas** las observaciones fuera del rango
$$[Q_1 - 1.5 \\times IQR \\; ; \\; Q_3 + 1.5 \\times IQR]$$""")

code("""sns.boxplot(x=pedidos["venta"], color="pink")
plt.title("Box-plot de la venta por pedido: los atípicos aplastan la caja")
plt.show()""")

code("""sns.boxplot(data=pedidos, x="venta", y="segmento", showfliers=False)
plt.title("Por segmento y sin dibujar atípicos, la caja respira (¡anótalo en el pie!)")
plt.show()""")

md("""**Qué significa:** en el primer gráfico la caja es una astilla contra el eje — los pedidos gigantes se comen la escala. En el segundo, ocultar los atípicos (`showfliers=False`) deja **comparar las cajas** entre segmentos: las medianas de los tres segmentos son parecidas. Ocultar atípicos para *ver* es legítimo **solo si el pie de la figura lo dice**; ocultarlos para *decidir* ya es maquillaje.""")

prompt("Calcula los límites de Tukey (1.5 por IQR) para la columna venta de la tabla pedidos, cuenta cuántos pedidos quedan fuera y qué porcentaje son, e imprime todo con dos decimales.")

code("""IQR  = stats.iqr(pedidos["venta"])
Q1   = pedidos["venta"].quantile(0.25)
Q3   = pedidos["venta"].quantile(0.75)
lim_inf = Q1 - 1.5 * IQR
lim_sup = Q3 + 1.5 * IQR

atipicos = pedidos[(pedidos["venta"] < lim_inf) | (pedidos["venta"] > lim_sup)]
print(f"Límites: [{lim_inf:.2f}, {lim_sup:.2f}]")            # [-674.02, 1,223.72]
print(f"Pedidos atípicos: {len(atipicos)} de {len(pedidos)}"
      f" ({len(atipicos)/len(pedidos)*100:.1f}%)")            # 459 (9.2%)""")

md("""**Qué significa:** «raro» empieza en \\$1,223.72 (el límite inferior queda en negativo: ningún pedido puede ser atípico por chico). 459 pedidos —casi 1 de cada 10— superan ese umbral. La regla del 1.5×IQR **describe** la distribución; no dice que esos pedidos sean errores: aquí son, probablemente, los clientes que más importan.""")

md("""# 🌶 3

**Encargo:** para la columna `utilidad` de la tabla **`pedidos`**, encuentre los **quintiles**, el **rango intercuartil**, los **límites de valores atípicos** y **cuántos pedidos** quedan fuera.

```
Respuesta:
Quintiles:
0.20   -1.16
0.40    8.76
0.60   28.26
0.80   91.97
Name: utilidad, dtype: float64

IQR utilidad: 66.63
Límites: [-97.90, 168.64]
Pedidos atípicos: 868
```

**Pregunta de María:** mira el quintil 0.20: es **negativo**. Tradúcelo a una frase de negocio (empieza por «Al menos uno de cada cinco pedidos...»).""")

code(f"""# Quintiles, IQR, límites y conteo de atípicos de `utilidad` en pedidos
{AJI}

# Tu frase para María: ...""",
     """# Quintiles, IQR, límites y conteo de atípicos de `utilidad` en pedidos
print("Quintiles:")
print(pedidos["utilidad"].quantile([0.2, 0.4, 0.6, 0.8]))

iqr_u = stats.iqr(pedidos["utilidad"])
q1_u  = pedidos["utilidad"].quantile(0.25)
q3_u  = pedidos["utilidad"].quantile(0.75)
li_u, ls_u = q1_u - 1.5 * iqr_u, q3_u + 1.5 * iqr_u
n_atip = ((pedidos["utilidad"] < li_u) | (pedidos["utilidad"] > ls_u)).sum()

print("\\nIQR utilidad:", round(iqr_u, 2))
print(f"Límites: [{li_u:.2f}, {ls_u:.2f}]")
print("Pedidos atípicos:", n_atip)

# Para María: «Al menos uno de cada cinco pedidos se despacha con pérdida:
# el quintil 0.20 de la utilidad es -$1.16, y la mitad central del negocio
# gana entre casi nada y $92 por pedido. La utilidad grande (y la pérdida
# grande) vive en los 868 pedidos atípicos (17.3%).»""")

# ══ 5 · Forma ════════════════════════════════════════════════════════════
md("""## 5. Medidas de forma

> **Encargo 4 de María** — «Cada vez que digo "promedio" en el comité, alguien pregunta "¿y la cola?". Quiero el número de la cola.»

* **Asimetría** (`skew`): 0 = simétrica; > 0 = cola derecha larga; < 0 = cola izquierda.
* **Curtosis** (`kurt`): qué tan pesadas son las colas frente a una normal (0 en pandas = como la normal).

[Asimetría](https://es.wikipedia.org/wiki/Asimetr%C3%ADa_estad%C3%ADstica) · [Curtosis](https://es.wikipedia.org/wiki/Curtosis)""")

code("""print("Asimetría de la venta por pedido:", round(pedidos["venta"].skew(), 2))  # 8.33
print("Curtosis de la venta por pedido: ", round(pedidos["venta"].kurt(), 2))  # 128.07""")

code("""sns.histplot(pedidos["venta"], bins=100, kde=True, color="darkblue")
plt.title("skew 8.33, curtosis 128: la cola derecha manda")
plt.show()""")

md("""**Qué significa:** una normal tiene asimetría 0 y curtosis 0; la venta por pedido tiene **8.33 y 128**. La asimetría positiva confirma la cola derecha (media > mediana, el 72.5 % bajo la media). La curtosis dice además que las colas son *pesadas*: los pedidos extremos ocurren mucho más de lo que una campana permitiría. Es la firma estadística de la trampa del promedio — ahora con números, no con sospechas.""")

md("""# 🌶 4

**Encargo:** obtenga el coeficiente de asimetría y la curtosis de la columna `utilidad` de la tabla **`pedidos`**.

```
Respuesta:
Coeficiente de asimetría: 5.12
Curtosis: 187.71
```

**Pregunta de María:** la utilidad por pedido tiene mínimo −\\$6,892 (pérdidas enormes) y aun así la asimetría salió **positiva**. ¿Hacia qué lado está la cola dominante y qué significa eso para el negocio? Una frase.""")

code("# Tu magia aquí\n",
     """# Asimetría y curtosis de la utilidad por pedido
print("Coeficiente de asimetría:", round(pedidos["utilidad"].skew(), 2))
print("Curtosis:", round(pedidos["utilidad"].kurt(), 2))

# Para María: aunque existen pérdidas brutales, la cola LARGA está a la derecha:
# las ganancias extremas llegan más lejos de lo que caen las pérdidas extremas.
# Con curtosis ~188, los pedidos extremos (en ambos sentidos) son parte
# estructural del negocio, no rarezas ignorables.""")

# ══ 6 · Covarianza y correlación ═════════════════════════════════════════
md("""## 6. Covarianza y correlación

> **Encargo 5 de María** — «Última: mercadeo jura que el descuento "impulsa el negocio". Quiero saber qué dicen los datos por pedido — y qué NO pueden decir.»

* **Covarianza**: da el *signo* de la relación lineal entre dos variables, pero su magnitud depende de las escalas.
* **Correlación de Pearson**: dirección **e** intensidad en [−1, 1], sin unidades.

Y el clásico: correlación no es causalidad — [correlaciones espurias](https://www.tylervigen.com/spurious-correlations).""")

code("""numericas = pedidos[["venta", "cantidad", "descuento_medio", "utilidad"]]

# Matriz de varianzas y covarianzas
numericas.cov().round(2)""")

code("""# Matriz de correlaciones
numericas.corr().round(2)""")

md("""**Qué significa:** en la covarianza solo puedes leer los signos (venta-utilidad +, descuento-utilidad −); los números no son comparables porque arrastran las unidades de cada variable. La correlación normaliza todo a [−1, 1]: `venta`-`utilidad` = **0.49** (positiva, moderada: vender más se asocia con ganar más, lejos de garantizarlo) y `venta`-`cantidad` = 0.41 (pedidos con más unidades venden más, sin sorpresa).""")

prompt("Mapa de calor de la matriz de correlaciones de la tabla numericas con anotaciones, escala fija de -1 a 1 y una paleta divergente, con seaborn.")

code("""plt.figure(figsize=(7, 5))
sns.heatmap(numericas.corr(), vmin=-1, vmax=1, annot=True, cmap="vlag_r")
plt.title("Correlaciones entre variables del pedido — Superstore")
plt.show()""")

md("""# 🌶 5

**Encargo:** obtenga el coeficiente de correlación entre `descuento_medio` y `utilidad` de la tabla **`pedidos`**.

```
Respuesta:
Correlación descuento-utilidad: -0.26
```

**Pregunta de María:** el número salió negativo. Escribe la frase para el comité con las dos partes: (a) qué se observa, en dirección e intensidad, y (b) por qué este número por sí solo **no** prueba que el descuento cause pérdidas.""")

code(f"""# Correlación entre descuento_medio y utilidad (pedidos)
{AJI}

# Tu frase para María (a + b): ...""",
     """# Correlación entre descuento_medio y utilidad (pedidos)
print("Correlación descuento-utilidad:",
      round(pedidos["descuento_medio"].corr(pedidos["utilidad"]), 2))

# (a) Se observa una asociación negativa débil-moderada (-0.26): los pedidos
#     con más descuento tienden a dejar menos utilidad.
# (b) Es una asociación observacional, no un experimento: el descuento se
#     aplica más en productos o temporadas difíciles, así que la causa puede
#     estar en otra parte. Para causalidad: diseño experimental (semana 9).""")

# ══ Cierre ═══════════════════════════════════════════════════════════════
md("""# 🌶 6 · El memo de María

Junta el expediente en **tres frases con cifras** (máximo 60 palabras), como respuesta directa a María — todo en términos de **pedidos**:

1. Cuánto vale un pedido típico y con qué medida lo defiendes.
2. Qué tan anchos/raros son los pedidos (una cifra de dispersión, posición o forma).
3. Qué le respondes a mercadeo sobre el descuento — sin confundir correlación con causalidad.

Escribe tu memo en la celda siguiente (doble clic para editar).""")

md("""**Memo para María — tu nombre aquí**

1. ...
2. ...
3. ...""")

md("""---

## Antes de entregar

* `Entorno de ejecución → Reiniciar y ejecutar todo`: el cuaderno corre de arriba a abajo sin errores.
* Los seis ajíes 🌶 resueltos y tus respuestas a María escritas donde se piden.
* Si usaste IA en algún ají: el prompt registrado en tu bitácora, como en los ejemplos 🤖 de este cuaderno.
* Nombre del archivo: `practica_estadistica_apellido.ipynb` → buzón de D2L.""")


# ══ Ensamblar ════════════════════════════════════════════════════════════
def notebook(usar_solucion):
    cells = []
    for tipo, src, sol in celdas:
        fuente = sol if (usar_solucion and sol is not None) else src
        cell = {"cell_type": tipo, "metadata": {}, "source": fuente.splitlines(keepends=True)}
        if tipo == "code":
            cell.update({"outputs": [], "execution_count": None})
        cells.append(cell)
    return {"cells": cells,
            "metadata": {"colab": {"provenance": []},
                         "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
                         "language_info": {"name": "python"}},
            "nbformat": 4, "nbformat_minor": 0}


est = REPO / "sitio" / "labs" / "taller_estadistica_superstore.ipynb"
sol = AQUI / "taller_estadistica_superstore_SOLUCIONES.ipynb"
est.write_text(json.dumps(notebook(False), ensure_ascii=False, indent=1), encoding="utf-8")
sol.write_text(json.dumps(notebook(True), ensure_ascii=False, indent=1), encoding="utf-8")
graficos = sum(("plt.show()" in (s or "")) + ("plt.show()" in (src or ""))
               for _, src, s in celdas if _ == "code")
multi = [i for i, (t, src, sol_) in enumerate(celdas)
         if t == "code" and (src.count("plt.show()") > 1 or (sol_ or "").count("plt.show()") > 1)]
print("estudiante:", est)
print("soluciones:", sol)
print("celdas:", len(celdas), "| celdas con >1 gráfico:", multi or "ninguna")
