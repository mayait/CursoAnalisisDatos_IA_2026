# Caso 6 · Análisis de Reseñas de E-Commerce y Predicción de Utilidad
### Seminario Análisis Exploratorio de Datos 
**Riesgo de complejidad:** 🟡 Medio · **Técnica principal:** Clasificación + NLP · **Dominio:** E-Commerce / Texto

---

## 🏢 Antecedentes

El dataset **Amazon Fine Food Reviews** contiene 568,000 reseñas de alimentos publicadas en Amazon con texto completo, calificación en estrellas (1–5) y contadores de utilidad percibida: cuántos usuarios encontraron útil la reseña (`HelpfulnessNumerator`) sobre cuántos la evaluaron (`HelpfulnessDenominator`).

La plataforma muestra primero las reseñas más valoradas como útiles, lo que impacta directamente en las decisiones de compra de millones de usuarios. El reto analítico es que la utilidad no puede predecirse solo con la calificación de estrellas — es necesario construir **características derivadas del texto** para capturar la calidad, extensión, sentimiento y coherencia de la reseña.

**Desafíos de calidad del dataset:**
- Reseñas con muy pocos votos producen tasas de utilidad poco representativas — filtrar a reseñas con ≥ 5 votos (`HelpfulnessDenominator >= 5`), reduciendo a ~100,000 reseñas
- Existen duplicados por usuario-producto-fecha que deben eliminarse con el criterio correcto

---

## 🎯 Objetivo

Construir un sistema que **prediga la utilidad percibida** de una reseña de e-commerce mediante ingeniería de características textuales, comparar un modelo interpretable con uno de mayor complejidad, y desarrollar una herramienta que ayude a los usuarios a mejorar la calidad de sus reseñas en tiempo real.

---

## 📚 Actividades para el estudiante

**Resultado de aprendizaje:** el estudiante aplica ingeniería de características sobre texto sin modelos de lenguaje, compara clasificadores con métricas apropiadas y construye un producto analítico de retroalimentación al usuario.

### Fase 1 – Comprensión del dominio
Investigar qué hace que una reseña en línea sea percibida como útil por otros compradores. Analizar ejemplos reales de reseñas con alta y baja utilidad. Formular hipótesis sobre qué características del texto — más allá de la nota — predicen la utilidad.

### Fase 2 – Preparación y exploración de datos
- Aplicar los filtros de calidad estadística (≥ 5 votos)
- Eliminar duplicados con el criterio correcto: mismo usuario, mismo producto, misma fecha
- Definir la variable objetivo binaria: tasa de utilidad ≥ 0.7 → útil (1), menor → no útil (0)
- Construir las características derivadas del texto:
  - Longitud en palabras y número de oraciones
  - Score de sentimiento con **VADER** (léxico sin entrenamiento)
  - Coherencia entre sentimiento del texto y calificación de estrellas (feature binario)
- Explorar la distribución de características entre reseñas útiles y no útiles

### Fase 3 – Modelado
Comparar dos clasificadores:
- **Modelo baseline:** Logistic Regression — interpretable, permite leer el peso de cada característica
- **Modelo principal:** Random Forest o LightGBM — mayor capacidad predictiva

Evaluar con Precisión, Recall, F1 y ROC-AUC. Fundamentar por escrito por qué la exactitud (accuracy) no es la métrica correcta aquí. Extraer e interpretar la importancia de las características del modelo principal.

### Fase 4 – Producto analítico

**Pipeline técnico:**
- Aplicar filtros: `df[df['HelpfulnessDenominator'] >= 5]`
- Eliminar duplicados: `drop_duplicates(subset=['UserId', 'ProductId', 'Time'])`
- Calcular score VADER: `SentimentIntensityAnalyzer().polarity_scores(text)['compound']`
- Variable de coherencia: ¿el sentimiento del texto coincide con la calificación de estrellas?

**API (FastAPI):**
- `POST /reviews/predict_helpfulness` — recibe texto y calificación de estrellas; devuelve probabilidad de utilidad y desglose de features calculados
- `GET /reviews/top_words` — palabras más asociadas a reseñas útiles vs. no útiles

**Dashboard (Streamlit):**
1. Área de texto + selector de estrellas; al analizar: probabilidad de utilidad con medidor visual y desglose de las características calculadas
2. Gráfico de importancia de variables con interpretación en lenguaje natural ("Las reseñas largas con sentimiento coherente son más útiles")
3. Tabla comparativa de métricas de los dos modelos entrenados (con curva ROC)

### Fase 5 – Interpretación y comunicación
¿Qué características del texto predicen más la utilidad? ¿Coincide con las hipótesis iniciales? ¿Qué consejo concreto daría a alguien que quiere escribir una reseña más útil para otros compradores?

---

## 🗂️ Dataset y recursos

| Recurso | Enlace |
|---|---|
| **Dataset principal** | [Amazon Fine Food Reviews — Kaggle](https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews) |

**Lecturas recomendadas:**
- Ingeniería de características para texto: longitud, estructura y coherencia
- Análisis de sentimiento con VADER: léxico basado en reglas sin entrenamiento
- Clasificación binaria: cuándo usar Precision, Recall y F1 en lugar de Accuracy
- Interpretabilidad de modelos: feature_importances_ y su lectura de negocio
- Filtrado estadístico de datos ruidosos en datasets de opiniones


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
