# 📂 Casos de Estudio — Seminario Análisis Exploratorio de Datos

---

## Cómo usar esta carpeta

Cada archivo contiene la descripción completa de un caso de estudio: antecedentes del problema, objetivo, actividades organizadas en 5 fases pedagógicas, especificaciones técnicas del pipeline, API y dashboard, enlace al dataset y lecturas recomendadas.

**Flujo de trabajo sugerido:**
1. Leer el caso completo antes de descargar datos
2. Formular hipótesis en la Fase 1 antes de abrir cualquier archivo de datos
3. Diseñar el esquema de datos (Fase 2) antes de programar
4. Comparar siempre ≥ 2 modelos con métricas apropiadas (Fase 3)
5. Entregar el producto analítico funcional (API + Dashboard) en la Fase 4

---

## 📋 Lista de casos

| # | Caso | Dominio | Técnica principal | Reto específico | Dataset (filas aprox.) |
|---|---|---|---|---|---|
| [1](Caso_01_Segmentacion_Clientes_Retail.md) | Segmentación de Clientes — Retail | Retail | K-Means / RFM | Normalización + selección de K + devoluciones | ~1,000,000 transacciones → ~4,000 clientes |
| [2](Caso_02_Sistema_Bancario_Ecuador.md) | Sistema Bancario Ecuatoriano | Finanzas / Ecuador | EDA + Rankings | Excel oficial multinivel + melt | 24 bancos × múltiples KPIs |
| [3](Caso_03_Scouting_FIFA.md) | Scouting y Valoración FIFA 21 | Deporte / Analytics | Regresión | Strings monetarios + multicolinealidad | 18,000 jugadores |
| [4](Caso_04_Movilidad_NYC.md) | Movilidad Urbana Nueva York | Transporte | Análisis geoespacial | Parquet + filtrado geográfico | ~3,000,000 viajes |
| [5](Caso_05_Sismicidad_Ecuador.md) | Actividad Sísmica Ecuador | Geofísica / Ecuador | Series de tiempo + Geo | Formato no estándar + solicitud institucional | ~100,000 eventos |
| [6](Caso_06_Resenas_Amazon_NLP.md) | Reseñas Amazon — Utilidad | NLP / E-Commerce | Clasificación + texto | Feature engineering textual + sesgo en target | ~100,000 reseñas (filtradas de 568k) |
| [7](Caso_07_Hits_Spotify.md) | Predicción de Hits de Spotify | Música / Analytics | Clasificación binaria | Umbral estadístico + desbalance | ~230,000 canciones |
| [8](Caso_08_Fraude_Tarjetas.md) | Detección de Fraude Financiero | Fintech | Clasificación desbalanceada | Desbalance extremo (0.17 %) + ajuste de umbral | 284,807 transacciones |
| [9](Caso_09_OLIST_Ecommerce.md) | E-Commerce OLIST Brasil | Logística / LatAm | Clasificación + multi-tabla | Join de 8 tablas relacionales | 100,000 pedidos |
| [10](Caso_10_Stack_Overflow_Tendencias.md) | Tendencias Tecnológicas Stack Overflow | Comunidad Tech | Series de tiempo + tags | Relación muchos-a-muchos + resampleo temporal | ~3,600,000 preguntas |

---

## 🗓️ Calendario de entregas

| Entrega | Momento | Entregable | Peso |
|---|---|---|---|
| E1 | Semana 2 · Clase 2 | Definición del problema: pregunta de negocio, historias de usuario, ficha del dataset | 10 % |
| E2 | Semana 4 · Clase 1 | Pipeline completo: carga, limpieza, ingeniería de características, EDA básico | 20 % |
| — | Semana 5 · Clase 1 | **[Punto de control intermedio](Entregable_Intermedio_Mitad_Seminario.md)**: repo estructurado, contexto del negocio, cuadernos de preparación y EDA con insights, bitácora de IA | — |
| E3 | Semana 6 · Clase 2 | EDA profundo + modelos comparados con métricas documentadas | 25 % |
| Final | Sesión final | Producto analítico completo: ≥ 2 modelos comparados, API + dashboard funcionales | 30 % |
| Final | Sesión final | Defensa oral (15 min por grupo) | 15 % |

> 🔎 El **[entregable intermedio de mitad del seminario](Entregable_Intermedio_Mitad_Seminario.md)** es transversal a todos los casos: define la estructura de repositorio, los cuadernos mínimos y la documentación obligatoria de uso de IA (Antigravity, Claude Code y similares).

---

## 🔧 Stack tecnológico del seminario

| Componente | Herramienta |
|---|---|
| Manipulación de datos | Python · NumPy · Pandas |
| Visualización | Matplotlib · Seaborn · Plotly |
| Machine Learning | scikit-learn · imbalanced-learn |
| API | FastAPI · joblib |
| Dashboard | Streamlit |
| Formato de datos | CSV · Excel · Parquet |

