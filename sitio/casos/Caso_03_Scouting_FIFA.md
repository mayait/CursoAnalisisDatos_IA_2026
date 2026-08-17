# Caso 3 · Sistema de Scouting y Valoración de Jugadores de Fútbol
### Seminario Análisis Exploratorio de Datos 
**Riesgo de complejidad:** 🟡 Medio · **Técnica principal:** Regresión · **Dominio:** Deporte / Analytics

---

## 🏢 Antecedentes

El mercado de traspasos del fútbol profesional mueve miles de millones de dólares anuales. El dataset de **FIFA 21** contiene más de 18,000 jugadores con más de 100 atributos técnicos y económicos. Presenta tres retos de ingeniería de datos característicos de fuentes reales:

1. Las columnas de valor económico (`Value`, `Wage`, `Release Clause`) vienen en **formato texto con sufijos** como `"€2.5M"` o `"€550K"` — deben convertirse a numérico
2. Los ratings de posición (ej. `LS`, `ST`) vienen en **formato compuesto** como `"65+3"` — requieren extracción del valor base
3. Los atributos técnicos de FIFA están **altamente correlacionados** por diseño (velocidad con agilidad, visión con pases), lo que genera multicolinealidad que un modelo de regresión debe manejar explícitamente

La oportunidad de negocio: detectar jugadores cuyo valor predicho supera su precio de mercado actual (jugadores *infravalorados*). Los equipos con recursos limitados necesitan exactamente esta herramienta.

---

## 🎯 Objetivo

Construir un **Sistema de Scouting Inteligente** que prediga el valor de mercado de un jugador a partir de sus atributos, compare el desempeño de al menos dos modelos de regresión, e identifique a los jugadores infravalorados de la base de datos.

---

## 📚 Actividades para el estudiante

**Resultado de aprendizaje:** el estudiante diseña y compara modelos de regresión para un dominio real, aplica transformaciones de ingeniería de características y construye un sistema de recomendación analíticamente fundamentado.

### Fase 1 – Comprensión del dominio
Investigar cómo los clubes de fútbol determinan el valor de mercado de un jugador. Identificar qué variables del dataset son económicamente más relevantes. Formular hipótesis sobre qué atributos técnicos correlacionan más con el valor de mercado.

### Fase 2 – Preparación y exploración de datos
Identificar y resolver los desafíos de formato:
- Convertir columnas monetarias (texto con sufijos `€`, `M`, `K`) a valores numéricos
- Extraer el valor base de los ratings de posición en formato compuesto
- Analizar la distribución del valor de mercado (target): determinar si requiere transformación logarítmica y justificar la decisión

Explorar la estructura de correlación entre atributos técnicos del jugador. Identificar y documentar el problema de multicolinealidad.

### Fase 3 – Modelado
Comparar dos modelos con filosofías distintas:
- **Modelo baseline:** diseñado específicamente para manejar multicolinealidad (Ridge Regression)
- **Modelo principal:** de mayor expresividad y capacidad predictiva (Random Forest Regressor)

Evaluar ambos con métricas de error apropiadas para regresión (MAE y R²). Seleccionar el mejor y justificar la elección. Calcular la brecha entre valor predicho y valor real para cada jugador del conjunto de prueba e identificar los más infravalorados (predicho > real × 1.5).

### Fase 4 – Producto analítico

**Pipeline técnico:**
- Función de conversión monetaria: parsear texto con sufijos a float (€, M, K)
- Función de extracción de rating: obtener valor base de formato "65+3"
- Aplicar transformación logarítmica al target `Value` antes de entrenar
- Comparar Ridge Regression (baseline) vs. Random Forest Regressor (modelo principal)
- Evaluar con MAE y R² en test set; guardar el mejor modelo

**API (FastAPI):**
- `GET /players/search?position=ST&min_potential=80` — filtra jugadores por criterios combinables
- `GET /players/{id}/profile` — perfil completo con valor real, valor predicho y clasificación ("Infravalorado" / "Precio justo" / "Sobrevalorado")

**Dashboard (Streamlit):**
1. Panel de filtros con sliders de edad, potencial y valoración, más selectbox de posición y nacionalidad — tabla de resultados actualizada en tiempo real
2. Gráfico de importancia de variables del modelo con interpretación en lenguaje de negocio
3. Ranking de los 15 jugadores más infravalorados según el conjunto de prueba, con valor real vs. predicho

### Fase 5 – Interpretación y comunicación
¿Qué atributos definen más el valor de un jugador según el modelo? ¿Hay resultados sorprendentes entre los infravalorados detectados? ¿Qué recomendación haría a un director deportivo con presupuesto limitado?

---

## 🗂️ Dataset y recursos

| Recurso | Enlace |
|---|---|
| **Dataset principal** | [FIFA 21 Complete Player Dataset — Kaggle](https://www.kaggle.com/datasets/stefanoleone992/fifa-21-complete-player-dataset) |

**Lecturas recomendadas:**
- Regresión con variables numéricas mixtas: selección de features y diagnóstico
- Transformación logarítmica de variables con distribución sesgada (np.log1p / np.expm1)
- Ridge Regression: regularización como respuesta a la multicolinealidad
- Random Forest Regressor: importancia de variables e interpretabilidad
- Ingeniería de características: conversión de formatos de texto a numérico


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
