# Caso 1 · Segmentación de Clientes para una Cadena de Retail
### Seminario Análisis Exploratorio de Datos 
**Riesgo de complejidad:** 🟡 Medio · **Técnica principal:** Clustering K-Means · **Dominio:** Retail

---

## 🏢 Antecedentes

Una cadena de comercio electrónico con sede en el Reino Unido posee el historial completo de transacciones entre 2009 y 2011, distribuido en dos períodos que deben consolidarse. La empresa vende principalmente artículos para el hogar y regalos a clientes mayoristas. La gerencia no dispone de un criterio basado en datos para distinguir a sus clientes más valiosos de aquellos en riesgo de abandono, lo que impide personalizar sus acciones de marketing y retención.

El dataset **Online Retail II** contiene más de 1,000,000 de transacciones organizadas en dos hojas de Excel. Cada fila es una línea de factura con el código del cliente, el producto, la cantidad, el precio y la fecha. Las facturas que comienzan con `'C'` son devoluciones y deben tratarse correctamente antes de calcular el valor por cliente.

---

## 🎯 Objetivo

Construir un sistema de segmentación que agrupe a los clientes en perfiles coherentes —**Clientes VIP, Leales, En Riesgo y Perdidos**— a partir de su comportamiento de compra usando el modelo **RFM** (Recencia, Frecuencia, Valor Monetario), y exponerlo como un servicio analítico interactivo para la gerencia.

---

## 📚 Actividades para el estudiante

**Resultado de aprendizaje:** el estudiante diseña un sistema de segmentación no supervisada, interpreta los grupos resultantes en clave de negocio y lo expone como producto analítico.

### Fase 1 – Comprensión del dominio
Investigar qué es el análisis RFM y por qué es el estándar de segmentación en retail. Formular hipótesis sobre cuántos tipos de clientes existen y cómo se diferencian. Identificar qué decisiones de negocio cambian según el segmento (campañas de email, descuentos, programas de fidelización).

### Fase 2 – Preparación y exploración de datos
Consolidar ambos períodos del dataset en una sola tabla. Identificar y resolver tres desafíos de calidad:
- Facturas de devolución (InvoiceNo que comienza con `'C'`) — netearlas contra sus facturas originales
- Transacciones sin cliente identificado (`Customer ID` nulo)
- Registros con cantidades negativas no asociadas a devoluciones

Justificar por escrito cada decisión de limpieza. Construir las métricas RFM por cliente y analizar su distribución estadística.

### Fase 3 – Modelado
Determinar el número óptimo de segmentos utilizando dos criterios complementarios: el **método del codo** (inercia vs. número de clusters) y el **coeficiente de Silhouette**. Documentar el análisis y justificar la elección final. Entrenar el modelo de agrupamiento. Asignar etiquetas de negocio descriptivas a cada segmento. Reducir dimensiones a 3 componentes principales para producir una visualización tridimensional de los grupos.

### Fase 4 – Producto analítico

**Pipeline técnico:**
- Concatenar las dos hojas del Excel con una sola operación
- Calcular Recencia (días desde la última compra), Frecuencia (número de facturas únicas) y Valor Monetario (suma de `Quantity × UnitPrice`) por cliente
- Normalizar las métricas RFM con un escalador robusto a outliers
- Entrenar K-Means con el K seleccionado; guardar modelo, escalador y transformador PCA

**API (FastAPI):**
- `GET /segments/summary` — estadísticas descriptivas (media y mediana de R, F, M) por segmento
- `POST /segments/classify` — recibe última compra, número de facturas y monto total; devuelve el segmento asignado con descripción del perfil

**Dashboard (Streamlit):**
1. Gráfico de dispersión 3D interactivo en espacio PCA con los clusters coloreados
2. Gráfico de barras comparando las medias de R, F y M por segmento
3. Formulario donde el gerente ingresa los datos de un cliente y obtiene en tiempo real su segmento con perfil descriptivo (ej. "Cliente VIP: alta frecuencia y alto valor monetario")

### Fase 5 – Interpretación y comunicación
Responder con datos: ¿qué estrategia de marketing corresponde a cada segmento? ¿Cuál representa el mayor riesgo de pérdida de ingresos? ¿Qué acción concreta recomendaría la gerencia para el segmento más crítico identificado?

---

## 🗂️ Dataset y recursos

| Recurso | Enlace |
|---|---|
| **Dataset principal** | [Online Retail II — UCI / Kaggle](https://www.kaggle.com/datasets/mashlyn/online-retail-ii-uci) |

**Lecturas recomendadas:**
- Análisis RFM: fundamentos y aplicaciones en retail
- Algoritmo K-Means: parámetros, inicialización y convergencia
- Selección del número de clusters: método del codo y Silhouette Score
- Reducción de dimensionalidad con PCA para visualización
- RobustScaler en scikit-learn: cuándo y por qué usarlo


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
