# Caso 10 · Análisis del Ecosistema de Stack Overflow: Tendencias Tecnológicas
### Seminario Análisis Exploratorio de Datos 
**Riesgo de complejidad:** 🟡 Medio · **Técnica principal:** Series de tiempo + Análisis de tags · **Dominio:** Comunidad Tech

---

## 🏢 Antecedentes

**Stack Overflow** es la comunidad de programación más grande del mundo, con más de 58 millones de preguntas publicadas. El dataset público **stacksample** contiene una muestra representativa del 10 %:
- `Questions.csv` — ~3,600,000 preguntas con título, fecha, puntuación y tags
- `Tags.csv` — ~12,000,000 registros de etiquetas tecnológicas asociadas a cada pregunta

La relación entre ambas tablas es **muchos-a-muchos**: una pregunta puede tener varios tags (ej. `python`, `pandas`, `dataframe`) y un tag aparece en miles de preguntas. Al hacer el merge sin filtrado previo, el DataFrame resultante tiene hasta ~12 millones de filas — demasiado para trabajar cómodamente. La estrategia de filtrado antes del join es obligatoria.

Los datos de Stack Overflow son el **termómetro real de adopción tecnológica** en la industria del software. Los picos de preguntas sobre una tecnología indican creciente adopción; el declive sostenido señala obsolescencia.

---

## 🎯 Objetivo

Construir un dashboard de **"Pulso Tecnológico"** que permita analizar la popularidad y evolución de las tecnologías en la comunidad de desarrollo de software, comparar el crecimiento o declive de lenguajes y frameworks a lo largo del tiempo, e identificar cuáles son las preguntas mejor valoradas de cada tecnología.

---

## 📚 Actividades para el estudiante

**Resultado de aprendizaje:** el estudiante diseña una estrategia de manejo de grandes volúmenes con relaciones muchos-a-muchos, construye series temporales por categoría de texto y desarrolla un producto de inteligencia tecnológica orientado a decisiones de formación.

### Fase 1 – Comprensión del dominio
Investigar el rol de Stack Overflow como indicador de adopción tecnológica en la industria. Identificar qué tecnologías son actualmente más relevantes para el mercado laboral de software en Ecuador y América Latina. Formular hipótesis sobre tendencias esperadas: ¿Python vs. Java? ¿React vs. Angular? ¿Machine Learning vs. tecnologías tradicionales?

### Fase 2 – Preparación y exploración de datos
**El reto de la relación muchos-a-muchos:**

1. Documentar cuántas filas tiene `Questions.csv` y cuántas tiene `Tags.csv`
2. Explicar por qué hacer el merge directamente produce ~12 millones de filas
3. Diseñar la estrategia de filtrado: filtrar preguntas desde 2015 **antes** del join — `questions[questions['CreationDate'].dt.year >= 2015]`
4. Documentar cuántas filas tiene el DataFrame final tras el filtrado y el join

Luego:
- Limpiar y normalizar los tags: `str.lower().str.strip()`
- Construir la tabla de popularidad mensual por tag: número de preguntas por tag por mes
- Calcular el crecimiento porcentual anual de cada tag (año más reciente vs. año anterior)
- Identificar las 5 preguntas con mayor Score para cada tag de interés

### Fase 3 – Análisis de tendencias
- Identificar las 20 tecnologías más discutidas en el período 2015–2024
- Detectar las de mayor crecimiento y las de mayor declive
- Comparar la trayectoria temporal de tecnologías equivalentes (lenguajes de programación, frameworks web, bases de datos)
- ¿Coincide el ranking real con las hipótesis formuladas en la Fase 1?

### Fase 4 – Producto analítico

**Pipeline técnico:**
- Convertir `CreationDate` a datetime antes del filtrado
- Filtrar por año ≥ 2015 antes del merge para reducir el volumen
- Construir popularidad mensual: `groupby('Tag').resample('M')['Id'].count()`
- Calcular crecimiento porcentual anual por tag

**API (FastAPI):**
- `GET /tags/top?n=20` — ranking de las 20 tecnologías más discutidas en el período
- `GET /tags/{tag}/timeseries` — serie temporal mensual de preguntas de una tecnología específica

**Dashboard (Streamlit):**
1. Gráfico de barras del **Top 20 de tecnologías** más discutidas en el período seleccionado
2. Gráfico de líneas interactivo con **selectbox múltiple** para comparar la popularidad de varias tecnologías (Python, JavaScript, Java, etc.) en el mismo eje temporal
3. Tabla de las **preguntas con mayor puntuación** de la tecnología seleccionada, con enlace directo a Stack Overflow

### Fase 5 – Interpretación y comunicación
¿Qué tecnologías están en auge y cuáles en declive según la comunidad? ¿Coincide con las hipótesis iniciales? ¿Qué implicaciones tiene esto para el **diseño curricular de una carrera de software**? Formular tres recomendaciones concretas de actualización curricular basadas en los datos.

---

## 🗂️ Dataset y recursos

| Recurso | Enlace |
|---|---|
| **Dataset principal** | [Stacksample — 10% of Stack Overflow Q&A / Kaggle](https://www.kaggle.com/datasets/stackoverflow/stacksample) |
| Archivos requeridos | `Questions.csv` y `Tags.csv` |

**Lecturas recomendadas:**
- Relaciones muchos-a-muchos en bases de datos: diagnóstico y tratamiento en Pandas
- Series de tiempo con `resample()` y `groupby()` en Pandas
- Análisis de tendencias: crecimiento porcentual y comparación de series
- Visualización de múltiples series temporales con Plotly (multiline chart con selectbox)
- Estrategias de filtrado previo al join en datasets de gran volumen


---

## 📋 Rúbrica de evaluación

| Entregable | Semana | Peso | Criterios clave |
|---|---|---|---|
| Definición del problema | 1 | 10 % | Claridad de la pregunta de negocio, historias de usuario, ficha del dataset |
| Pipeline de datos | 2 | 20 % | Reproducibilidad, manejo del reto específico, validaciones documentadas |
| EDA + primer modelo | 3 | 25 % | Profundidad del análisis, rigor estadístico, pertinencia del modelo y métricas |
| Producto analítico completo | 4 | 30 % | Comparación de ≥ 2 modelos, API y dashboard funcionales, documentación |
| Defensa oral y trabajo en equipo | 4 | 15 % | Dominio técnico, claridad, manejo de preguntas, colaboración |

> **Modalidad:** grupos de 3 estudiantes · **Entrega final:** sesión final del seminario
