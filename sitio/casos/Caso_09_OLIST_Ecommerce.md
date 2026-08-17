# Caso 9 · Análisis del E-Commerce Latinoamericano: Entrega y Satisfacción del Cliente
### Seminario Análisis Exploratorio de Datos 
**Riesgo de complejidad:** 🟡 Medio · **Técnica principal:** Clasificación + Multi-tabla · **Dominio:** Logística / LatAm

---

## 🏢 Antecedentes

**OLIST** es el mayor marketplace de e-commerce de Brasil. Su dataset público contiene 100,000 pedidos realizados entre 2016 y 2018, distribuidos en **8 tablas relacionales**: pedidos, clientes, productos, vendedores, reseñas, pagos, ítems y geolocalización.

Este es el único caso de la matriz que requiere integración multi-tabla real — la habilidad más demandada en el mercado laboral de analítica de datos. Replica fielmente el trabajo diario de un analista en una empresa de e-commerce. La integración se construye encadenando merges siguiendo el esquema relacional:

```
orders → customers
orders → items → products
orders → reviews
orders → payments
customers → geolocation (vendedor y cliente)
```

La distancia aproximada entre vendedor y cliente, calculada a partir de coordenadas, resulta ser uno de los predictores más importantes del retraso en la entrega.

---

## 🎯 Objetivo

Construir un sistema predictivo de alertas de entrega que determine si un pedido llegará tarde a su destino, para que la plataforma emita **alertas proactivas al cliente** antes de que el retraso ocurra, analizando qué factores operativos y geográficos aumentan más el riesgo de demora.

---

## 📚 Actividades para el estudiante

**Resultado de aprendizaje:** el estudiante diseña y ejecuta una integración multi-tabla compleja, construye variables de ingeniería geoespacial y temporal, y desarrolla un sistema predictivo de logística con visualización geográfica.

### Fase 1 – Comprensión del dominio
Investigar el modelo de negocio de un marketplace de e-commerce y los costos operativos y de reputación de las entregas tardías. Analizar el esquema de las 8 tablas del dataset y **diseñar el diagrama de relaciones entre ellas** antes de escribir ninguna línea de código. Esto es obligatorio.

### Fase 2 – Preparación y exploración de datos
Construir el DataFrame analítico maestre siguiendo el diagrama diseñado. Justificar el tipo de join (inner, left) en cada paso. Calcular las variables de ingeniería clave:
- `dias_retraso` = diferencia entre fecha de entrega real y fecha estimada
- `entrego_tarde` = 1 si el retraso > 0 días (variable objetivo)
- `distancia_aprox` = distancia euclidiana en grados entre coordenadas del vendedor y del cliente

### Fase 3 – Modelado
- Cuantificar el desbalance de `entrego_tarde` y seleccionar la estrategia de manejo apropiada
- Comparar dos clasificadores: Random Forest y Gradient Boosting
- Evaluar con Precisión, Recall, F1 y ROC-AUC
- Extraer los factores más predictivos del retraso e interpretarlos en términos operativos

### Fase 4 – Producto analítico

**Pipeline técnico:**
- Encadenar merges: `orders → customers → items → products → reviews`
- `dias_retraso = (order_delivered_customer_date - order_estimated_delivery_date).dt.days`
- Distancia proxy: diferencia euclidiana entre lat/lon de vendedor y cliente
- `class_weight='balanced'` para el clasificador con el desbalance observado

**API (FastAPI):**
- `POST /orders/delay_risk` — recibe estado del vendedor, estado del cliente y categoría del producto; devuelve probabilidad de entrega tardía
- `GET /orders/top_risk_categories` — categorías de producto con mayor tasa histórica de retrasos

**Dashboard (Streamlit):**
1. Mapa coroplético de Brasil con tasa de entregas tardías por estado del cliente (`px.choropleth`)
2. Gráfico de barras de satisfacción promedio (score de reseña) por categoría de producto
3. Formulario donde el equipo de logística ingresa los datos de un nuevo pedido y obtiene la probabilidad de retraso con las principales variables de riesgo identificadas por el modelo

### Fase 5 – Interpretación y comunicación
¿Qué factores predicen más las entregas tardías? ¿Qué estados y categorías de producto representan mayor riesgo? ¿Qué recomendación haría al equipo de logística de OLIST para reducir la tasa de retrasos?

---

## 🗂️ Dataset y recursos

| Recurso | Enlace |
|---|---|
| **Dataset principal** | [Brazilian E-Commerce Public Dataset by Olist — Kaggle](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) |

**Tablas mínimas requeridas:**
- `olist_orders_dataset.csv`
- `olist_customers_dataset.csv`
- `olist_order_reviews_dataset.csv`
- `olist_order_items_dataset.csv`
- `olist_geolocation_dataset.csv`

**Lecturas recomendadas:**
- Diseño de esquemas relacionales: diagrama entidad-relación
- Joins avanzados con Pandas: inner vs. left join y sus implicaciones en el conteo de filas
- Ingeniería de características con fechas (`datetime`) y coordenadas geográficas
- Visualización geoespacial: mapas coropléticos con Plotly Express (`px.choropleth`)
- Clasificación con scikit-learn: pipeline de preprocesamiento y modelo


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
