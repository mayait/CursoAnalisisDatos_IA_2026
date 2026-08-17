# Caso 7 · Análisis de Atributos Musicales y Predicción de Popularidad de Canciones
### Seminario Análisis Exploratorio de Datos 
**Riesgo de complejidad:** 🟡 Medio · **Técnica principal:** Clasificación binaria · **Dominio:** Música / Analytics

---

## 🏢 Antecedentes

Spotify calcula para cada canción atributos de audio numéricos derivados del análisis de la señal musical:

| Atributo | Descripción |
|---|---|
| `danceability` | Qué tan adecuada es para bailar (0–1) |
| `energy` | Intensidad y actividad perceptiva (0–1) |
| `valence` | Positividad musical; valores altos = más alegre (0–1) |
| `acousticness` | Confianza de que la canción es acústica (0–1) |
| `tempo` | Pulsaciones por minuto estimadas |
| `loudness` | Volumen promedio en decibelios |

El dataset contiene más de **230,000 canciones** con estos atributos y su nivel de popularidad actual (0–100).

**El reto técnico central está en la definición del target:** usar un umbral arbitrario (ej. `popularity > 75`) genera un desbalance severo donde solo el 3–5 % de canciones son "hits", llevando a clasificadores triviales que predicen siempre "no hit" con 95 % de exactitud pero cero utilidad real. El umbral correcto debe basarse en la **distribución estadística real** de la popularidad.

---

## 🎯 Objetivo

Construir un sistema que clasifique canciones como "hit" o "no hit" y analice cuál es la **"fórmula de un éxito"**, exponiendo los resultados como un **Laboratorio de Hits** interactivo donde el usuario puede explorar combinaciones de atributos de audio en tiempo real.

---

## 📚 Actividades para el estudiante

**Resultado de aprendizaje:** el estudiante define correctamente variables objetivo con criterio estadístico, maneja el desbalance de clases con fundamentación técnica y construye un clasificador interpretable orientado a decisiones de negocio.

### Fase 1 – Comprensión del dominio
Investigar qué son los atributos de audio de Spotify y cómo son calculados por la plataforma. Reflexionar sobre si la popularidad de una canción puede predecirse con características musicales objetivas. Identificar qué valor tendría esta herramienta para un sello discográfico o productor musical.

### Fase 2 – Preparación y exploración de datos
- Analizar la distribución completa de la variable `popularity`
- Definir `hit = 1` si `popularity > percentil 75` de la distribución — esto produce clases ~25 %/75 %, manejable sin técnicas extremas
- Justificar por qué este criterio es superior a un umbral arbitrario
- Cuantificar el desbalance resultante y seleccionar la estrategia de manejo
- Realizar análisis comparativo de los atributos de audio entre hits y no-hits (boxplots, correlaciones)
- Explorar si el comportamiento varía por género musical

### Fase 3 – Modelado
Comparar dos clasificadores con `class_weight='balanced'`:
- **Baseline:** Logistic Regression
- **Modelo principal:** Random Forest

Evaluar con Precisión, Recall, F1 y ROC-AUC. Argumentar por escrito por qué la exactitud sola es una métrica engañosa en este contexto. Extraer e interpretar la importancia de los atributos de audio.

### Fase 4 – Producto analítico

**Pipeline técnico:**
- `hit = (popularity > np.percentile(popularity, 75)).astype(int)` — criterio estadístico
- `RandomForestClassifier(class_weight='balanced')` — manejo del desbalance
- Evaluar con `predict_proba`, no con `predict` binario — para el slider del dashboard

**API (FastAPI):**
- `POST /songs/predict_hit` — recibe atributos de audio; devuelve probabilidad de éxito (0–1)
- `GET /songs/feature_importance` — ranking de atributos más predictivos del éxito

**Dashboard (Streamlit):**
1. **Laboratorio de Hits:** sliders para cada atributo de audio (danceability, energy, valence, acousticness, tempo); la probabilidad de hit se actualiza en tiempo real al mover cualquier slider
2. Gráfico de barras horizontal de importancia de atributos ("¿qué hace exitosa a una canción?")
3. Comparación de distribuciones entre hits y no-hits con boxplots interactivos de Plotly

### Fase 5 – Interpretación y comunicación
¿Existe una fórmula musical para los éxitos? ¿Qué atributos son más relevantes y cuáles sorprenden? ¿Qué limitaciones tiene este modelo para predecir el éxito comercial real de una canción?

---

## 🗂️ Dataset y recursos

| Recurso | Enlace |
|---|---|
| **Dataset principal** | [Ultimate Spotify Tracks DB — Kaggle](https://www.kaggle.com/datasets/zaheenhamidani/ultimate-spotify-tracks-db) |

**Lecturas recomendadas:**
- Construcción estadística de variables objetivo: uso de percentiles vs. umbrales fijos
- Clasificación con clases desbalanceadas: `class_weight='balanced'` y sus implicaciones
- Métricas de clasificación: cuándo y por qué usar Precision, Recall, F1 y ROC-AUC
- `predict_proba`: diferencia entre clasificación binaria y probabilidad continua
- Seaborn para comparación de distribuciones entre grupos


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
