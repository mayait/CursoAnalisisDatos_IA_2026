# Caso 8 · Detección de Fraude en Transacciones con Tarjetas de Crédito
### Seminario Análisis Exploratorio de Datos 
**Riesgo de complejidad:** 🟡 Medio · **Técnica principal:** Clasificación desbalanceada · **Dominio:** Fintech

---

## 🏢 Antecedentes

El fraude con tarjetas de crédito genera pérdidas globales superiores a **USD 30,000 millones anuales**. El dataset del Machine Learning Group de la Université Libre de Bruxelles contiene **284,807 transacciones reales** de dos días en Europa, de las cuales solo **492 son fraudulentas (0.17 %)**.

Por razones de confidencialidad, las variables originales fueron transformadas mediante PCA, resultando en 28 componentes anónimos (V1–V28) más tres columnas interpretables:
- `Time` — segundos desde la primera transacción del dataset
- `Amount` — monto de la transacción en euros
- `Class` — etiqueta: 0 = legítima, 1 = fraude

**Este es el caso más extremo de desbalance de clases de la matriz.** Un modelo que predice "legítima" para todas las transacciones obtiene 99.83 % de exactitud pero detecta **cero fraudes**. La decisión estratégica central es el ajuste del umbral de decisión: capturar más fraudes siempre implica más falsas alarmas, y ese equilibrio debe comunicarse a la gerencia como una decisión de negocio, no técnica.

---

## 🎯 Objetivo

Construir un sistema de detección de fraude que maneje el desbalance extremo con rigor técnico, compare múltiples estrategias de tratamiento, y **comunique visualmente la compensación Precisión-Recall** para que la gerencia tome la decisión de umbral con criterio de negocio.

---

## 📚 Actividades para el estudiante

**Resultado de aprendizaje:** el estudiante maneja el desbalance extremo de clases con múltiples estrategias, elige y fundamenta métricas de evaluación apropiadas, y construye una herramienta de apoyo a la decisión gerencial.

### Fase 1 – Comprensión del dominio
Investigar el impacto económico del fraude financiero. Explicar por qué la exactitud (accuracy) es una métrica engañosa en este problema. Analizar el **costo asimétrico de los dos tipos de error**: no detectar un fraude (falso negativo) vs. bloquear una transacción legítima (falso positivo). Definir qué métrica(s) debería optimizar este sistema y por qué.

### Fase 2 – Preparación y exploración de datos
- Cuantificar y documentar el desbalance de clases con gráficos claros
- Analizar si `Amount` y `Time` difieren estadísticamente entre fraudes y transacciones legítimas (boxplots)
- Diseñar el esquema de validación cruzada estratificada para evitar fuga de información con datos desbalanceados

### Fase 3 – Modelado
Comparar al menos **4 combinaciones**: 2 estrategias de manejo del desbalance × 2 clasificadores:

| Estrategia | Descripción |
|---|---|
| A — Pesos de clase | `class_weight='balanced'` en el modelo — más simple, sin modificar los datos |
| B — SMOTE | Sobremuestreo sintético del training set — genera nuevos ejemplos de fraude |

Clasificadores: Logistic Regression (baseline) y Random Forest (modelo principal).

Evaluar todas las combinaciones con Precisión, Recall, F1 y ROC-AUC. Seleccionar la mejor y analizar el efecto de mover el umbral de decisión sobre el equilibrio entre capturar fraudes y generar falsas alarmas.

### Fase 4 – Producto analítico

**Pipeline técnico:**
- Comparar `class_weight='balanced'` vs. SMOTE sobre el training set únicamente (nunca sobre test)
- Evaluar con `StratifiedKFold` para preservar la proporción de fraudes en cada fold
- Analizar la curva Precision-Recall (más informativa que ROC para desbalance extremo)
- Guardar el mejor modelo para el servicio de inferencia

**API (FastAPI):**
- `POST /transactions/evaluate` — recibe atributos (V1–V28 + Amount); devuelve clasificación y probabilidad de fraude
- `GET /transactions/threshold?value=0.3` — métricas proyectadas (Precisión, Recall estimados) para un umbral dado

**Dashboard (Streamlit):**
1. Simulación de flujo de transacciones recientes con indicadores verde/rojo
2. Matriz de confusión visual + curva Precisión-Recall del modelo seleccionado en el test set
3. **Slider interactivo de umbral de decisión** que actualiza en tiempo real: Precisión, Recall y número proyectado de fraudes capturados y falsas alarmas por día — la vista más valiosa para la toma de decisión gerencial

### Fase 5 – Interpretación y comunicación
¿Qué umbral recomendarían y por qué? ¿Cuál es el costo de equivocarse en cada dirección? Presentar a la gerencia la decisión de umbral como una **compensación explícita entre dos riesgos de negocio**, no como un problema técnico.

---

## 🗂️ Dataset y recursos

| Recurso | Enlace |
|---|---|
| **Dataset principal** | [Credit Card Fraud Detection — ULB / Kaggle](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) |

**Lecturas recomendadas:**
- Métricas para clasificación desbalanceada: Precision, Recall, F1 y ROC-AUC
- Curvas ROC y Precision-Recall: lectura e interpretación comparada
- SMOTE: sobremuestreo sintético con imbalanced-learn
- Ajuste de umbral de decisión en clasificadores probabilísticos
- Validación cruzada estratificada (StratifiedKFold) en datos desbalanceados


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
