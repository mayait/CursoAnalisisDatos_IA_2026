# Caso 5 · Análisis y Monitoreo de la Actividad Sísmica en Ecuador
### Seminario Análisis Exploratorio de Datos 
**Riesgo de complejidad:** 🟡 Medio · **Técnica principal:** Series de tiempo + Geo · **Dominio:** Geofísica / Ecuador

---

## 🏢 Antecedentes

Ecuador está ubicado en el **Cinturón de Fuego del Pacífico** y registra una de las actividades sísmicas más intensas de América del Sur, con eventos históricos devastadores como el terremoto de Pedernales (2016, Mw 7.8). El **Instituto Geofísico de la Escuela Politécnica Nacional (IG-EPN)** mantiene el catálogo sísmico oficial con decenas de miles de eventos registrados.

El archivo se distribuye en **formato de texto científico** con separadores variables y encabezados comentados con `#` — un estándar en geofísica que representa un reto real de ingestión de datos. Contiene columnas: `time_value`, `lat`, `lon`, `depth`, `magnitude`. Las autoridades de gestión de riesgos necesitan una herramienta de monitoreo visual e interactiva para explorar este catálogo.

> ⚠️ **Acción requerida el primer día:** el IG-EPN entrega el catálogo por correo electrónico en un plazo de 24–48 horas. Solicitar el período 2012–presente en `https://www.igepn.edu.ec/catalogos-sismicos/formulario-catalogos-sismicos` el **primer día del seminario**.

---

## 🎯 Objetivo

Construir un sistema interactivo de **Monitor Sísmico** que permita a analistas de gestión de riesgos explorar el catálogo histórico del IG-EPN, filtrar eventos por fecha, magnitud y profundidad, y visualizar los patrones temporales y geográficos de la actividad sísmica en el territorio ecuatoriano.

---

## 📚 Actividades para el estudiante

**Resultado de aprendizaje:** el estudiante procesa datos científicos de formato no estándar, construye un sistema de clasificación geográfica sin geocodificación externa y desarrolla un dashboard de monitoreo con vistas vinculadas.

### Fase 1 – Comprensión del dominio
Investigar la escala de magnitudes sísmicas, el sistema de clasificación por profundidad y la geografía sísmica del Ecuador. Comprender el rol del IG-EPN en el monitoreo nacional. Iniciar inmediatamente el trámite de solicitud del catálogo.

### Fase 2 – Preparación y exploración de datos
Examinar la estructura del archivo recibido: separadores variables (espacios múltiples), encabezados con caracteres `#`. Cargar, parsear y documentar cada decisión de ingestión. Realizar las siguientes categorizaciones:

| Variable | Categorías |
|---|---|
| Magnitud | Ligero (3.5–4.9) · Moderado (5.0–5.9) · Fuerte (≥ 6.0) |
| Profundidad | Superficial (< 70 km) · Intermedio (70–300 km) · Profundo (> 300 km) |
| Región geográfica | Sur · Centro · Norte — asignada por latitud sin geocodificación |

Calcular la frecuencia mensual de sismos por categoría de magnitud.

### Fase 3 – Análisis de patrones
Identificar los períodos de mayor actividad sísmica. Comparar la distribución de magnitudes y profundidades entre regiones. Analizar si existe tendencia en la frecuencia de eventos a lo largo de la serie histórica.

### Fase 4 – Producto analítico

**Pipeline técnico:**
- `pd.read_csv(file, sep='\s+', comment='#')` — parsear el formato no estándar
- Convertir `time_value` a datetime; extraer año, mes y categorías
- Asignar región: `pd.cut(df['lat'], bins=[-5, -2, 0, 2], labels=['Sur','Centro','Norte'])`
- Guardar catálogo procesado en Parquet; usar `@st.cache_data` en Streamlit

**API (FastAPI):**
- `GET /sismos/query?start_date=2020-01-01&end_date=2023-12-31&min_magnitude=4.5` — eventos filtrados
- `GET /sismos/stats?region=Centro` — estadísticas de la región (count, magnitud media, profundidad media)

**Dashboard (Streamlit):**
Todos los gráficos responden a los mismos filtros de fecha y magnitud simultáneamente:
1. Mapa interactivo (`px.scatter_mapbox`) — tamaño y color representan magnitud; filtros de fecha y magnitud
2. Gráfico de líneas de la frecuencia mensual por categoría de magnitud
3. Histograma de distribución de magnitudes con líneas verticales en los umbrales de categoría

### Fase 5 – Interpretación y comunicación
¿Qué zonas del Ecuador concentran la mayor actividad? ¿Existen períodos históricos con anomalías significativas? ¿Qué alertas tempranas podría emitir este sistema para la gestión de riesgos?

---

## 🗂️ Dataset y recursos

| Recurso | Enlace |
|---|---|
| **Dataset principal** | [Catálogo Sísmico IG-EPN — solicitar período 2012–presente](https://www.igepn.edu.ec/catalogos-sismicos/formulario-catalogos-sismicos) |

**Lecturas recomendadas:**
- Escala de Richter y Moment Magnitude: clasificación de sismos
- Lectura de archivos CSV con separadores no estándar y encabezados comentados
- Visualización geoespacial con Plotly: scatter_mapbox con datos de puntos
- Series de tiempo en Pandas: resampleo mensual y agregación por categoría
- Uso de `st.cache_data` en Streamlit para optimizar carga de datos


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
