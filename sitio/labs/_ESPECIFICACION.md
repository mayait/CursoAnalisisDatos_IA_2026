# Especificación de los laboratorios · Análisis de Datos con IA y Python

Todos los cuadernos de `sitio/labs/` siguen esta especificación. Es lo que hace que dieciséis
laboratorios escritos en distintos momentos se sientan como un solo curso.

## Nombre y ubicación

`sitio/labs/lab_NN.ipynb`, donde `NN` es el número de semana con dos dígitos (`lab_01.ipynb` … `lab_16.ipynb`).

## Los datos

Todo el curso trabaja sobre **Comercial Andina**, un distribuidor ecuatoriano ficticio con
tiendas en Quito, Guayaquil, Cuenca, Manta y Loja, más canal en línea. Los archivos están en
`sitio/datos/` y los genera `sitio/datos/generar_datos.py` con semilla fija.

| Archivo | Filas | Columnas |
|---|---|---|
| `ventas.csv` | 80 515 | `factura_id`, `fecha`, `cliente_id`, `sucursal_id`, `producto_id`, `cantidad`, `precio_unitario`, `descuento`, `es_devolucion` |
| `ventas_limpias.csv` | 79 482 | Las mismas. Es la versión ya depurada; **solo se usa a partir de la semana 5** |
| `clientes.csv` | 1 800 | `cliente_id`, `razon_social`, `ciudad`, `tipo_cliente`, `fecha_alta`, `canal_captacion` |
| `productos.csv` | 74 | `producto_id`, `nombre`, `categoria`, `subcategoria`, `costo_unitario`, `precio_lista` |
| `sucursales.csv` | 6 | `sucursal_id`, `ciudad`, `canal`, `fecha_apertura`, `metros_cuadrados` |
| `marketing_mensual.csv` | 31 | `mes`, `inversion_radio`, `inversion_digital`, `inversion_volantes`, `ventas_mes` |
| `experimento_reactivacion.csv` | 1 800 | `cliente_id`, `tipo_cliente`, `ciudad`, `grupo`, `convirtio` |

**Problemas de calidad deliberados en `ventas.csv`** (son el material de la semana 4, no errores
del curso): 7,8 % de líneas sin `cliente_id`; 1,1 % de filas duplicadas exactas; el 12 % de las
fechas en texto `dd/mm/aaaa` y el resto en `aaaa-mm-dd`; 0,6 % de cantidades negativas sin marca
de devolución; 0,4 % de precios ausentes; y un puñado de precios con un cero de más.
En `clientes.csv`, el 9 % de las ciudades está mal escrito (`quito`, `QUITO`, `Quito `, `Guayaquíl`)
y el 3 % no tiene fecha de alta.

**Fenómenos que los datos contienen a propósito:** el ticket es bimodal porque el 22 % de los
clientes son mayoristas (media 180,49 frente a mediana 30,22); hay estacionalidad con pico en
diciembre; el experimento de reactivación tiene una **paradoja de Simpson** (globalmente gana el
control con 21,8 % frente a 14,1 %, pero el tratamiento gana en minoristas y en mayoristas por
separado); y el 31 % de los clientes lleva más de 180 días sin comprar, que es la definición de
abandono del curso.

Datasets públicos que se usan además, siempre por URL:

- Advertising: `https://raw.githubusercontent.com/justmarkham/scikit-learn-videos/master/data/Advertising.csv`
- Titanic: `https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv`
- Pima Diabetes: `https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv`

## Estructura obligatoria del cuaderno

1. **Celda 0 · markdown.** Badge de Colab, `# Laboratorio {N} · {Tema}`, y un párrafo que conecta
   con la semana anterior y dice qué se desbloquea hoy.
2. **Celda 1 · markdown.** Blockquote con **Hoy haces** (qué se hace, cuánto dura) y **Entrega**.
3. **Celda 2 · code.** Setup exacto (ver abajo). Termina imprimiendo `Setup completo ✓`.
4. **Secciones numeradas** `## 1.`, `## 2.`… Cada bloque teórico cierra con una celda de código
   ejecutable que produce una salida visible (tabla, número o gráfico).
5. **Al menos tres ejercicios**, en este orden: `### 🌶️ Ejercicio 1 — Guiado`,
   `### 🔥 Desafío`, `### 🎯 Reto en clase (15 min)`. Cada uno deja una celda de código con
   `# TU CÓDIGO AQUÍ` y un comentario con la pista.
6. **Una sección `## La trampa de hoy`** que demuestra en código el error que la semana
   existe para evitar, con los dos números lado a lado (el equivocado y el correcto).
7. **Sección final `## Entregable`** con lo que se sube y **`## Para tu equipo`** con dos o tres
   viñetas sobre el caso del grupo.

Entre 25 y 45 celdas. Nada de celdas vacías.

## Celda de setup, literal

```python
# --- Setup del entorno ---
from pathlib import Path
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

SEED = 42
random.seed(SEED)
np.random.seed(SEED)

sns.set_theme(style="whitegrid", palette="deep")
plt.rcParams["figure.figsize"] = (10, 4)
pd.set_option("display.max_columns", 40)
pd.set_option("display.float_format", lambda v: f"{v:,.2f}")

# Los datos de Comercial Andina viven en sitio/datos/
CANDIDATOS = [Path("../datos"), Path("datos"), Path("sitio/datos"),
              Path("/content/CursoAnalisisDatos_IA_2026/sitio/datos")]
DATOS = next((p for p in CANDIDATOS if p.exists()), None)
if DATOS is None:
    raise FileNotFoundError(
        "No encuentro la carpeta de datos. En Colab ejecuta primero:\n"
        "  !git clone https://github.com/<usuario>/CursoAnalisisDatos_IA_2026.git")

print("Setup completo ✓")
print(f"pandas {pd.__version__} · datos en {DATOS.resolve()}")
```

## Reglas de escritura

- **Español, tuteo, segunda persona.** «Hoy calculas el margen por cliente», no «se calculará».
- **Cada sección abre con el porqué de negocio**, no con la sintaxis. Patrón: problema real →
  intuición → código → interpretación → trampa.
- **Toda cifra que aparezca en el texto sale de ejecutar el cuaderno.** Nada de números inventados.
- **Los gráficos llevan título con la conclusión**, no con el nombre del eje, y siempre
  `plt.tight_layout()` antes de mostrarlos.
- **Emojis solo en los marcadores establecidos**: 🌶️ ejercicio guiado · 🔥 desafío · 🎯 reto ·
  ⚠️ trampa · 📌 idea central. Nunca en prosa corrida.
- **Sin relleno.** Si una frase se puede borrar sin perder información, se borra.
- El cuaderno **corre de principio a fin sin errores**. Se verifica con `nbclient` antes de publicar.

## Metadatos del cuaderno

```json
"metadata": {
  "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
  "language_info": {"name": "python", "version": "3.11"}
}
```
`"nbformat": 4, "nbformat_minor": 5`
