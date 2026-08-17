# Plantilla · clase_NN.ipynb

Numeración global: `clase_06.ipynb` es la sesión 6 del curso, aunque viva en la carpeta `S03-C2`.

Metadatos mínimos del cuaderno:

```json
"metadata": {
  "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
  "language_info": {"name": "python", "version": "3.11.0"}
}
```

## Orden de celdas

| # | Tipo | Contenido |
|---|---|---|
| 0 | markdown | Badge de Colab + `# Sesión {N} · {Tema}` + párrafo de conexión con la sesión anterior |
| 1 | markdown | Blockquote con **Hoy haces** y **Entrega** |
| 2 | markdown | `## 📺 Video de referencia` (opcional pero habitual) |
| 3 | code | Setup |
| 4+ | md/code alternados | Secciones numeradas `## 1.`, `## 2.`… |
| −3 | md + code | Ejercicios y desafíos |
| −2 | markdown | Entregable parcial |
| −1 | markdown | Para tu equipo |

## Celda 0

```markdown
<a href="https://colab.research.google.com/github/{repo}/blob/main/{Carpeta%20URL}/clase_{NN}.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# Sesión {N} · {Tema}

{Un párrafo: qué sabía hacer el estudiante hasta ayer, qué le faltaba, y qué desbloquea hoy.
Ejemplo real: "Hasta la clase pasada trabajaste con objetos y con listas/diccionarios de
Python. Hoy das el salto a Pandas, la librería con la que vas a vivir el resto del curso."}
```

## Celda 1

```markdown
> **Hoy haces** · La teoría comentada, **{n} ejercicios guiados** ({temas entre paréntesis}), **{m} desafíos de profundización** y un checkpoint final. ~2h30.
>
> **Entrega** · El notebook ejecutado de principio a fin, con tus respuestas en las celdas marcadas, subido al repo del equipo antes de la próxima clase.
```

## Celda de video

```markdown
## 📺 Video de referencia

Antes de empezar, mira los primeros {n} minutos de este video. Cubre exactamente los conceptos de hoy con ejemplos visuales:

**[{Título del video}]({url})**

[![{Título}](https://img.youtube.com/vi/{id}/0.jpg)]({url})

> *Video en español, ritmo pausado. Si ya dominas el tema, sáltalo.*
```

## Celda de setup (literal, no la cambies salvo por librerías nuevas)

```python
# --- Setup del entorno ---
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

print("Setup completo ✓")
print(f"pandas {pd.__version__} · numpy {np.__version__}")
```

## Carga de datos

Siempre por URL cruda, para que Colab funcione sin subir archivos:

```python
URL = "https://raw.githubusercontent.com/{owner}/{repo}/{rama}/{ruta}.csv"
df = pd.read_csv(URL)
print(f"{df.shape[0]:,} filas × {df.shape[1]} columnas")
df.head()
```

Datasets ya usados en el curso, reutilízalos antes de buscar otros:

| Dataset | URL | Sesiones |
|---|---|---|
| Titanic (seaborn) | `https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv` | Pandas I |
| Titanic (datasciencedojo) | `https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv` | Streamlit, FastAPI, defensa |
| Advertising | `https://raw.githubusercontent.com/justmarkham/scikit-learn-videos/master/data/Advertising.csv` | Regresiones |
| Pima Diabetes | `https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv` | Logística, árbol, ensembles |
| Penguins / Iris | `https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv` | Planteamiento del proyecto |

Mantener el mismo dataset a lo largo de un bloque es deliberado: permite comparar modelos entre sesiones con una tabla acumulativa.

## Ejercicios

Tres niveles, siempre en este orden:

```markdown
### 🌶️ Ejercicio {n} — Guiado · {Título}
{Enunciado con los pasos ya desglosados. Se resuelve en clase.}

### 🔥 Desafío extra {n} · {Título}
{Enunciado sin pasos. Queda para casa si no da el tiempo.}

### 🎯 Reto en clase (15 min)
{Replicar lo que acaba de hacer el docente cambiando una variable. Se comparte en pantalla.}
```

Cada ejercicio deja su celda de código lista:

```python
# TU CÓDIGO AQUÍ

```

## Cierre

```markdown
## {n}. Entregable parcial E{k} (avance)

{Qué se sube hoy y cómo encaja en la entrega grande. Recuerda la fecha de la entrega completa.}

## Para tu equipo

{Cómo se aplica lo de hoy al caso asignado. Dos o tres viñetas accionables, no un resumen
de la sesión.}
```

## Antes de guardar

Ejecuta el cuaderno completo y guárdalo con las salidas. Un cuaderno con celdas sin ejecutar
o con un `NameError` a mitad no se publica.
