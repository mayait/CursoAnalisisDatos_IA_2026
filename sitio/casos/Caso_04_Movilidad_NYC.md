# Caso 4 · Análisis Geoespacial de la Movilidad Urbana en Nueva York
### Seminario Análisis Exploratorio de Datos 
**Riesgo de complejidad:** 🟡 Medio · **Técnica principal:** Análisis geoespacial · **Dominio:** Transporte urbano

---

## 🏢 Antecedentes

La ciudad de Nueva York publica los registros de viaje de todos los taxis amarillos a través de la **NYC Taxi & Limousine Commission (TLC)**. El archivo de enero de 2023 en formato **Parquet** contiene aproximadamente 3,000,000 de viajes con coordenadas geográficas de origen y destino, marcas de tiempo y tarifas.

Este caso presenta dos retos técnicos reales:
1. **Formato Parquet:** estándar columnar ampliamente utilizado en la industria para datos grandes — mucho más eficiente que CSV para este volumen
2. **Datos geoespaciales sucios:** el archivo contiene coordenadas anómalas fuera de los límites físicos de Nueva York (latitud: 40.4774–40.9176; longitud: -74.2591 a -73.7004) que deben filtrarse antes del análisis

Un planificador urbano necesita entender los **patrones de demanda por zona y horario** para optimizar la distribución de flota y las políticas de transporte.

---

## 🎯 Objetivo

Construir un sistema de análisis geoespacial que identifique los **hotspots de mayor demanda** de transporte en Nueva York y cómo varía la actividad a lo largo del día y la semana, usando visualizaciones cartográficas interactivas sin dependencias externas de tokens de API.

---

## 📚 Actividades para el estudiante

**Resultado de aprendizaje:** el estudiante procesa un dataset de gran volumen en formato optimizado, aplica filtrado geoespacial y construye visualizaciones cartográficas para análisis de movilidad urbana.

### Fase 1 – Comprensión del dominio
Investigar los desafíos de planificación del transporte urbano en megaciudades. Identificar qué preguntas puede responder el análisis de datos de taxi para un planificador urbano. Explorar el portal de datos abiertos de NYC TLC y comprender el esquema del dataset.

### Fase 2 – Preparación y exploración de datos
- Cargar el archivo Parquet y comparar los tiempos de carga frente a un CSV equivalente — documentar la diferencia
- Aplicar filtro geográfico con los límites de bounding box de NYC; documentar cuántos registros se descartan y por qué
- Filtrar viajes con tarifa negativa o duración imposible (negativos o superiores a 3 horas)
- Extraer variables temporales: hora del día y día de la semana
- Crear columnas de zona aproximada binificando las coordenadas a 2 decimales
- Construir tabla agregada de demanda por hora × día de semana

### Fase 3 – Análisis de patrones
Identificar los corredores y zonas de mayor demanda. Analizar cómo varía la actividad entre horas punta y valle, y entre días hábiles y fines de semana. Detectar patrones que revelen comportamiento recurrente vs. eventos excepcionales.

### Fase 4 – Producto analítico

**Pipeline técnico:**
- Cargar con `pd.read_parquet()` — verificar el ahorro de memoria vs. CSV
- Bounding box NYC: lat ∈ [40.4774, 40.9176], lon ∈ [-74.2591, -73.7004]
- Binificar coordenadas: `lat_bin = pickup_latitude.round(2)`, `lon_bin = pickup_longitude.round(2)`
- Guardar datos agregados en Parquet optimizado para el dashboard

**API (FastAPI):**
- `GET /trips/heatmap?hour=8` — puntos de recogida de una hora específica para el mapa de calor
- `GET /trips/demand_curve` — serie de demanda por hora del día

**Dashboard (Streamlit + Folium):**
1. Mapa de calor interactivo (`folium.plugins.HeatMap`) con slider de hora del día — sin token de Mapbox requerido
2. Gráfico de barras de viajes totales por hora del día
3. Heatmap de Seaborn con demanda por hora vs. día de semana — identifica picos y diferencias entre días hábiles y fines de semana

### Fase 5 – Interpretación y comunicación
¿En qué zonas y franjas horarias se concentra la mayor demanda? ¿Qué implicaciones tiene para la asignación de flota? ¿Qué zonas parecen sub-atendidas en horas punta?

---

## 🗂️ Dataset y recursos

| Recurso | Enlace |
|---|---|
| **Dataset principal** | [NYC TLC Trip Record Data — Yellow Taxi enero 2023 (Parquet)](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) |

**Lecturas recomendadas:**
- Formato Parquet: ventajas sobre CSV para datasets grandes
- Filtrado geoespacial con coordenadas de bounding box
- Visualización de mapas de calor con Folium (sin API token)
- Análisis temporal con groupby y agregaciones por hora y día
- Manejo eficiente de grandes volúmenes de datos en memoria


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
