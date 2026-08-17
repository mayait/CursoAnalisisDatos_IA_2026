# ADM 2003 · Análisis de Datos con IA y Python
## Mapeo de material a las 16 semanas · versión 2

Cruza dos fuentes contra el cronograma `ADM2003_cronograma_python_ia_v2.md`:

- **Actividades heredadas de D2L** — 53 actividades de los cursos 202410 (Python + Tableau) y 202520 (KNIME), extraídas en `Material Actual/Actividades Organizadas/`.
- **Material del seminario de Python** — 17 cuadernos, 10 casos y 6 simuladores del repo `CursoPythonDatos_2026`.

Estados de lo heredado: **REUTILIZABLE** = el enunciado sirve casi tal cual · **ADAPTAR** = la idea y los datos sirven, la herramienta o el entregable cambian · **DESCARTAR** = no entra en el curso nuevo.

> Cambios de la versión 2: regresión partida en las semanas 12 y 13, semana 10 nueva de estrategia y transformación digital con el customer journey map, fuera la semana de anomalías y KPIs, manipulación fusionada en la semana 5, y el capítulo de segmentación renombrado a «¿Quiénes son mis clientes y cuánto valen?» y convertido en el proyecto de medio semestre de la semana 8.

---

## 1. Resumen por semana

| Semana | Tema | Heredado de D2L | Material del seminario de Python |
|---|---|---|---|
| 1 | Introducción a Business Analytics y Big Data en la era de la IA | Contrato de Grupo (202410)<br>Sin inteligencia artificial no te van a escuchar. ¿Valor o Humo? (202520) | 📓 S01-C1 |
| 2 | Business Analytics en las organizaciones. La pregunta antes del dato | Taller 01 \| Introducción a KNIME con Pizza Sales (202520) | 📓 S03-C2<br>📓 S02-C2 |
| 3 | Estadística descriptiva aplicada al negocio | Taller 02 \| Ejercicio: Análisis Individual Pizza Sales (202520)<br>Python \| Estadística descriptiva con Pandas (202410) | 📓 S04-C2 |
| 4 | Anatomía y calidad de los datos | Análisis exploratorio con KNIME (202520)<br>Diagnostico de la Analítica de Datos en Procesos Empresariales (202410)<br>Proyecto Final \| Diagnóstico de Analítica de Datos en la Empresa (202520) | 📓 S04-C1 |
| 5 | Manipulación de datos. Agrupar, limpiar y combinar | Participación \| Taller Grupal: Análisis Exploratorio SuperStore (202520) | 📓 S04-C1 |
| 6 | Visualización de datos | Data visualization I (202410)<br>Data visualization II (202410)<br>Data visualization III (202410)<br>Lectura Data Storytelling (202520) | 📓 S04-C2<br>📖 Material Actual/Actividades Organizadas/99_Lecturas_y_Material_de_Apoyo/CONTEXTO - Storytelling con datos - Cole Nussbaumer Knaflic (1).pdf |
| 7 | Visualización avanzada y tableros | Data Visualization IV (Resultados financieros) (202410)<br>Dashboard de Superstore en Tableau (202410) | 📓 S08-C1 |
| 8 | ¿Quiénes son mis clientes y cuánto valen? | Análisis RFM + P para Superstore (Individual) Primera parte. (202410)<br>Proyecto Grupal \| Análisis RFM+P: Clasificación de Clientes SuperStore (202520) | 📂 casos/Caso_01_Segmentacion_Clientes_Retail.md<br>📋 casos/Entregable_Intermedio_Mitad_Seminario.md |
| 9 | Comparación, variabilidad y causalidad | _ninguno_ | 📓 S07-C2 |
| 10 | Estrategia, transformación digital y experiencia del cliente | Caso Banco Andino - Journey Map (202410) | _ninguno_ |
| 11 | Modelos analíticos. Tipos de modelos y creación de valor | Harvard Case - Data-Driven Management of Blue Detergent (202410) | 📓 S06-C2<br>🎛️ simuladores/simulador-train-test.html |
| 12 | Modelos de pronóstico I. Regresión lineal simple | Regresión Lineal Python (202410)<br>Regresión publicidad, influencers y ventas 🦾🦾 en KNIME (202520) | 📓 S05-C1<br>🎛️ simuladores/simulador-regresion-lineal.html<br>🎛️ simuladores/simulador-regresion-3D-advertising.html |
| 13 | Modelos de pronóstico II. Regresión múltiple y diagnóstico | Regresión Lineal (2) Multiple (202410)<br>Regresión Lineal Parte 3 (202410)<br>Regresión Lineal con KNIME: Predicción de Emisiones CO2 🌍🚗 (202520)<br>Participación \| Actividad en Clase: Regresión Múltiple (202520) | 📓 S05-C1<br>🎛️ simuladores/simulador-vif.html<br>🎛️ simuladores/simulador-overfitting.html<br>📂 casos/Caso_03_Scouting_FIFA.md |
| 14 | Modelos de propensión. Clasificación aplicada a decisiones | Supervised Learning - KNN \| Telco Churn (202410)<br>Predicción de Abandono Laboral en KNIME 👨🏽‍🔧 (202520) | 📓 S05-C2<br>📓 S06-C1<br>📓 S06-C2<br>🎛️ simuladores/simulador-confusion-matrix.html<br>📂 casos/Caso_08_Fraude_Tarjetas.md |
| 15 | De la predicción a la decisión. Ética y gobernanza del dato | _ninguno_ | _ninguno_ |
| 16 | Cierre del curso y presentación final | Evaluación 360 (202410)<br>Proyecto Final - Aplicación de la Analítica de Datos en Procesos Empresariales (EN VIDEO) (202410)<br>Proyecto Final - Aplicación de la Analítica de Datos en Procesos Empresariales (202520) | 📓 SF |

---

## 2. Detalle semana por semana

### Semana 1 · Introducción a Business Analytics y Big Data en la era de la IA

*Colab, cuadernos ejecutables, protocolo de uso de IAG y bitácora de prompts*

**Actividades heredadas de D2L**

| Actividad | Curso | Estado | Qué hay que cambiar | Carpeta |
|---|---|---|---|---|
| **Contrato de Grupo** | 202410 Python+Tableau | REUTILIZABLE | Sirve tal cual. Añadir la firma del protocolo de uso de IA generativa que pide la semana 1. | `Material Actual/Actividades Organizadas/00_Gestion_de_Curso_y_Equipos/2024_Contrato_de_Grupo/` |
| **Sin inteligencia artificial no te van a escuchar. ¿Valor o Humo?** | 202520 KNIME | ADAPTAR | Debate sobre valor real frente a humo de la IA. Encaja con la apertura de la semana 1; hay que redactar el enunciado porque el export viene vacío. | `Material Actual/Actividades Organizadas/09_Casos_y_Procesos_de_Negocio/2025_Sin_inteligencia_artificial_no_te_van_a_escuchar_Valor_o_Humo/` |

**Material del seminario de Python**

| Tipo | Recurso | Cómo se usa |
|---|---|---|
| 📓 cuaderno | `S01-C1 · Kick-off del seminario · clase_01.ipynb` | Formación de equipos, contrato y arranque del repo. Se le añade la firma del protocolo de uso de IA generativa. |

### Semana 2 · Business Analytics en las organizaciones. La pregunta antes del dato

*pandas: read_csv, head, info, shape. Ficha de análisis y unidad de análisis*

**Actividades heredadas de D2L**

| Actividad | Curso | Estado | Qué hay que cambiar | Carpeta |
|---|---|---|---|---|
| **Taller 01 \| Introducción a KNIME con Pizza Sales** | 202520 KNIME | ADAPTAR | Buen dataset de entrada. Reescribir el flujo KNIME como cuaderno Colab: read_csv, head, info y shape sobre pizza_sales.xlsx, que viene adjunto en la carpeta del Taller 02. | `Material Actual/Actividades Organizadas/02_Primer_Contacto_con_Datos_y_EDA/2025_Taller_01_Introduccion_a_KNIME_con_Pizza_Sales/` |

**Material del seminario de Python**

| Tipo | Recurso | Cómo se usa |
|---|---|---|
| 📓 cuaderno | `S03-C2 · Pandas I · clase_06.ipynb` | Series, DataFrames, read_csv, exploración rápida, loc/iloc y filtros booleanos. Es la sesión de la semana 2 casi tal cual. |
| 📓 cuaderno | `S02-C2 · Planteamiento del proyecto · clase_04.ipynb` | Pregunta de negocio, ficha del dataset, historias de usuario y limitaciones conocidas. Es exactamente el Deber 1. |

### Semana 3 · Estadística descriptiva aplicada al negocio

*pandas: describe, value_counts, quantile*

**Actividades heredadas de D2L**

| Actividad | Curso | Estado | Qué hay que cambiar | Carpeta |
|---|---|---|---|---|
| **Taller 02 \| Ejercicio: Análisis Individual Pizza Sales** | 202520 KNIME | ADAPTAR | El banco de preguntas (EDA_Pizza_BancoPreguntas.docx) es estadística descriptiva pura y se reutiliza casi íntegro como las doce preguntas contra reloj del laboratorio de la semana 3. Cambiar la herramienta a pandas. | `Material Actual/Actividades Organizadas/02_Primer_Contacto_con_Datos_y_EDA/2025_Taller_02_Ejercicio_Analisis_Individual_Pizza_Sales/` |
| **Python \| Estadística descriptiva con Pandas** | 202410 Python+Tableau | REUTILIZABLE | Cuaderno Colab con Credit.csv. Es el mejor calce directo del curso viejo. Solo actualizar el enunciado con media frente a mediana y la bitácora de prompts. | `Material Actual/Actividades Organizadas/03_Estadistica_Descriptiva/2024_Python_Estadistica_descriptiva_con_Pandas/` |

**Material del seminario de Python**

| Tipo | Recurso | Cómo se usa |
|---|---|---|
| 📓 cuaderno | `S04-C2 · Visualizaciones · clase_08.ipynb (secciones 1-3)` | Distribuciones, estadísticas, percentiles y detección de outliers con IQR. Se usa la mitad descriptiva; la parte gráfica queda para la semana 6. |

### Semana 4 · Anatomía y calidad de los datos

*pandas: dtypes, isna, duplicated, astype*

**Actividades heredadas de D2L**

| Actividad | Curso | Estado | Qué hay que cambiar | Carpeta |
|---|---|---|---|---|
| **Análisis exploratorio con KNIME** | 202520 KNIME | ADAPTAR | Rehacer como inventario de calidad de datos con dtypes, isna, duplicated y astype. Es la base del Deber 2 (bitácora de limpieza). | `Material Actual/Actividades Organizadas/02_Primer_Contacto_con_Datos_y_EDA/2025_Analisis_exploratorio_con_KNIME/` |
| **Diagnostico de la Analítica de Datos en Procesos Empresariales** | 202410 Python+Tableau | REUTILIZABLE | Hito del proyecto integrador, no contenido del tema de la semana: coincide con el entregable Propuesta de proyecto final de la semana 4. El diagnóstico de madurez organizacional (entrevistas, framework, oportunidades) se conserva tal cual. | `Material Actual/Actividades Organizadas/10_Proyecto_Integrador/2024_Diagnostico_de_la_Analitica_de_Datos_en_Procesos_Empresariales/` |
| **Proyecto Final \| Diagnóstico de Analítica de Datos en la Empresa** | 202520 KNIME | REUTILIZABLE | Hito del proyecto integrador que se entrega en la semana 4. Versión mejorada de la de 202410: añade la evaluación de madurez digital con pymedigital.ec. Usar esta como base. | `Material Actual/Actividades Organizadas/10_Proyecto_Integrador/2025_Proyecto_Final_Diagnostico_de_Analitica_de_Datos_en_la_Empresa/` |

**Material del seminario de Python**

| Tipo | Recurso | Cómo se usa |
|---|---|---|
| 📓 cuaderno | `S04-C1 · Pandas II · clase_07.ipynb (bloque de limpieza)` | Flujo de limpieza con antes y después, y checkpoint. Base de la bitácora de limpieza del Deber 2. |

### Semana 5 · Manipulación de datos. Agrupar, limpiar y combinar

*pandas: query, assign, groupby, agg, merge, concat, pivot_table*

**Actividades heredadas de D2L**

| Actividad | Curso | Estado | Qué hay que cambiar | Carpeta |
|---|---|---|---|---|
| **Participación \| Taller Grupal: Análisis Exploratorio SuperStore** | 202520 KNIME | ADAPTAR | Pasa a la semana fusionada de manipulación: torneo de preguntas resueltas con groupby, agg y merge. Hay que redactar el enunciado porque el export viene vacío. | `Material Actual/Actividades Organizadas/02_Primer_Contacto_con_Datos_y_EDA/2025_Participacion_Taller_Grupal_Analisis_Exploratorio_SuperStore/` |

**Material del seminario de Python**

| Tipo | Recurso | Cómo se usa |
|---|---|---|
| 📓 cuaderno | `S04-C1 · Pandas II · clase_07.ipynb (bloque de agrupación)` | Groupby básico y agregaciones múltiples, ya implementados. Ojo: el plan de la sesión promete pivot, melt, merge y concat, pero el cuaderno no los implementa. Las uniones hay que escribirlas. |

### Semana 6 · Visualización de datos

*matplotlib y seaborn*

**Actividades heredadas de D2L**

| Actividad | Curso | Estado | Qué hay que cambiar | Carpeta |
|---|---|---|---|---|
| **Data visualization I** | 202410 Python+Tableau | REUTILIZABLE | Ejercicio 2.1 de Knaflic, agnóstico de herramienta. Pedir el gráfico en matplotlib o seaborn en vez de PowerPoint. | `Material Actual/Actividades Organizadas/04_Visualizacion_de_Datos/2024_Data_visualization_I/` |
| **Data visualization II** | 202410 Python+Tableau | REUTILIZABLE | Bocetos en papel a slide. Mantener el boceto a mano y exigir que la versión final sea código. | `Material Actual/Actividades Organizadas/04_Visualizacion_de_Datos/2024_Data_visualization_II/` |
| **Data visualization III** | 202410 Python+Tableau | REUTILIZABLE | Ejercicio 2.2: mapa de calor, columnas y línea. Traducir los tres pasos a matplotlib y discutir cuál comunica mejor. | `Material Actual/Actividades Organizadas/04_Visualizacion_de_Datos/2024_Data_visualization_III/` |
| **Lectura Data Storytelling** | 202520 KNIME | ADAPTAR | El PDF de Cole Nussbaumer Knaflic está en 99_Lecturas_y_Material_de_Apoyo, pero el export no trae el enunciado: hay que redactar de nuevo las preguntas de la lectura previa de la semana 6. | `Material Actual/Actividades Organizadas/04_Visualizacion_de_Datos/2025_Lectura_Data_Storytelling/` |

**Material del seminario de Python**

| Tipo | Recurso | Cómo se usa |
|---|---|---|
| 📓 cuaderno | `S04-C2 · Visualizaciones · clase_08.ipynb (secciones 4-7)` | Dashboard exploratorio, relación entre variables y el flujo de la exploración. Trae histograma, caja, dispersión y barras; faltan la serie de línea y las barras ordenadas que pide el repertorio mínimo. |
| 📖 lectura | `Material Actual/Actividades Organizadas/99_Lecturas_y_Material_de_Apoyo/CONTEXTO - Storytelling con datos - Cole Nussbaumer Knaflic (1).pdf` | Lectura previa del lunes. El PDF ya viene en el export de 202520. |

### Semana 7 · Visualización avanzada y tableros

*Plotly y Streamlit*

**Actividades heredadas de D2L**

| Actividad | Curso | Estado | Qué hay que cambiar | Carpeta |
|---|---|---|---|---|
| **Data Visualization IV (Resultados financieros)** | 202410 Python+Tableau | ADAPTAR | Contar un estado de resultados a no financieros. Reescribirlo como cascada interactiva en Plotly para que justifique la semana de tableros. | `Material Actual/Actividades Organizadas/04_Visualizacion_de_Datos/2024_Data_Visualization_IV_Resultados_financieros/` |
| **Dashboard de Superstore en Tableau** | 202410 Python+Tableau | ADAPTAR | La pregunta de negocio (¿qué pasa con profit en el último año?) se conserva; el tablero se rehace en Plotly o Streamlit dentro del cuaderno. Tableau sale del curso. | `Material Actual/Actividades Organizadas/05_Dashboards_y_Tableros/2024_Dashboard_de_Superstore_en_Tableau/` |

**Material del seminario de Python**

| Tipo | Recurso | Cómo se usa |
|---|---|---|
| 📓 cuaderno | `S08-C1 · Dashboards con Streamlit · clase_15.ipynb` | Widgets, dashboard mínimo, separación de datos, lógica y UI, y despliegue gratuito. Reemplaza a Tableau. |

### Semana 8 · ¿Quiénes son mis clientes y cuánto valen?

*pandas: qcut, quantile, groupby para RFM+P. KMeans y StandardScaler como contraste*

**Actividades heredadas de D2L**

| Actividad | Curso | Estado | Qué hay que cambiar | Carpeta |
|---|---|---|---|---|
| **Análisis RFM + P para Superstore (Individual) Primera parte.** | 202410 Python+Tableau | REUTILIZABLE | Núcleo del proyecto de medio semestre. Ya está en Colab y ya exige adjuntar el prompt final del LLM. Añadir el contraste con KMeans y la recomendación comercial por segmento. | `Material Actual/Actividades Organizadas/08_Segmentacion_RFM/2024_Analisis_RFM_P_para_Superstore_Individual_Primera_parte/` |
| **Proyecto Grupal \| Análisis RFM+P: Clasificación de Clientes SuperStore** | 202520 KNIME | ADAPTAR | Versión grupal: es el entregable calificado del corte de medio semestre. Nombrar los segmentos y escribir el mensaje comercial de cada uno. | `Material Actual/Actividades Organizadas/08_Segmentacion_RFM/2025_Proyecto_Grupal_Analisis_RFM_P_Clasificacion_de_Clientes_SuperStore/` |

**Material del seminario de Python**

| Tipo | Recurso | Cómo se usa |
|---|---|---|
| 📂 caso | `casos/Caso_01_Segmentacion_Clientes_Retail.md` | Caso completo de RFM y KMeans sobre Online Retail II, con fases, API y dashboard. Es el enunciado del proyecto de medio semestre. |
| 📋 rúbrica | `casos/Entregable_Intermedio_Mitad_Seminario.md` | Punto de control de mitad de seminario: estructura de repo, cuadernos mínimos y bitácora de uso de IA. Sirve de rúbrica del corte. |

### Semana 9 · Comparación, variabilidad y causalidad

*crosstab y scipy.stats: prueba t, chi cuadrado, ANOVA. Diseño de pruebas A/B*

**Actividades heredadas de D2L:** ninguna.

**Material del seminario de Python**

| Tipo | Recurso | Cómo se usa |
|---|---|---|
| 📓 cuaderno | `S07-C2 · Hipótesis y pruebas estadísticas · clase_14.ipynb` | Prueba t, chi cuadrado, ANOVA, tamaño del efecto y protocolo completo. Cubre el laboratorio entero de la semana 9. |

### Semana 10 · Estrategia, transformación digital y experiencia del cliente

*Customer journey map, service blueprint y diagnóstico de madurez digital*

**Actividades heredadas de D2L**

| Actividad | Curso | Estado | Qué hay que cambiar | Carpeta |
|---|---|---|---|---|
| **Caso Banco Andino - Journey Map** | 202410 Python+Tableau | REUTILIZABLE | Pieza central de la semana nueva de estrategia. Al blueprint se le añade una capa: marcar dónde nace cada dato y qué decisión se toma hoy a ciegas, para entrar a la semana 11 con el mapa hecho. | `Material Actual/Actividades Organizadas/09_Casos_y_Procesos_de_Negocio/2024_Caso_Banco_Andino_Journey_Map/` |

### Semana 11 · Modelos analíticos. Tipos de modelos y creación de valor

*train_test_split, DummyRegressor, DummyClassifier*

**Actividades heredadas de D2L**

| Actividad | Curso | Estado | Qué hay que cambiar | Carpeta |
|---|---|---|---|---|
| **Harvard Case - Data-Driven Management of Blue Detergent** | 202410 Python+Tableau | REUTILIZABLE | Caso de la semana bisagra: asignar familia de modelo, decisión, línea base y valor anual estimado a cada problema del catálogo. | `Material Actual/Actividades Organizadas/09_Casos_y_Procesos_de_Negocio/2024_Harvard_Case_Data_Driven_Management_of_Blue_Detergent/` |

**Material del seminario de Python**

| Tipo | Recurso | Cómo se usa |
|---|---|---|
| 📓 cuaderno | `S06-C2 · Métricas · clase_12.ipynb (sección 2)` | Elegir la métrica correcta según la decisión. Se adelanta a la semana bisagra para instalar el criterio antes del primer modelo. |
| 🎛️ simulador | `simuladores/simulador-train-test.html` | Muestra por qué se separa el conjunto de prueba antes de tocar nada. |

### Semana 12 · Modelos de pronóstico I. Regresión lineal simple

*LinearRegression, lectura del coeficiente, MAE y error porcentual*

**Actividades heredadas de D2L**

| Actividad | Curso | Estado | Qué hay que cambiar | Carpeta |
|---|---|---|---|---|
| **Regresión Lineal Python** | 202410 Python+Tableau | REUTILIZABLE | Cuaderno de regresión simple con Advertising.csv. Añadir la línea base con DummyRegressor y el error porcentual. Es el cuaderno de la semana 12. | `Material Actual/Actividades Organizadas/06_Regresion_y_Pronostico/2024_Regresion_Lineal_Python/` |
| **Regresión publicidad, influencers y ventas 🦾🦾 en KNIME** | 202520 KNIME | ADAPTAR | El encuadre de negocio (influencers) es mejor que el del cuaderno viejo. Rescatar el enunciado para la semana de regresión simple y montarlo sobre scikit-learn. | `Material Actual/Actividades Organizadas/06_Regresion_y_Pronostico/2025_Regresion_publicidad_influencers_y_ventas_en_KNIME/` |

**Material del seminario de Python**

| Tipo | Recurso | Cómo se usa |
|---|---|---|
| 📓 cuaderno | `S05-C1 · Regresiones · clase_09.ipynb (secciones 1-2)` | Advertising.csv, regresión simple TV → Sales, lectura de coeficientes y reto de replicar con Radio. La sección 3 ya es múltiple: se deja para la semana 13. |
| 🎛️ simulador | `simuladores/simulador-regresion-lineal.html` | Manipular la recta y ver el error. Abre la sesión del lunes. |
| 🎛️ simulador | `simuladores/simulador-regresion-3D-advertising.html` | El plano de regresión sobre el mismo dataset. |

### Semana 13 · Modelos de pronóstico II. Regresión múltiple y diagnóstico

*statsmodels, variables categóricas, VIF, residuos, ajuste polinomial*

**Actividades heredadas de D2L**

| Actividad | Curso | Estado | Qué hay que cambiar | Carpeta |
|---|---|---|---|---|
| **Regresión Lineal (2) Multiple** | 202410 Python+Tableau | REUTILIZABLE | Pasa a la semana 13 junto con VIF y diagnóstico de residuos, que antes no cabían. | `Material Actual/Actividades Organizadas/06_Regresion_y_Pronostico/2024_Regresion_Lineal_2_Multiple/` |
| **Regresión Lineal Parte 3** | 202410 Python+Tableau | ADAPTAR | Ejercicio de cierre del bloque de regresión múltiple. Verificar que el cuaderno de GitHub siga vivo y reencuadrarlo hacia el pronóstico del negocio del proyecto. | `Material Actual/Actividades Organizadas/06_Regresion_y_Pronostico/2024_Regresion_Lineal_Parte_3/` |
| **Regresión Lineal con KNIME: Predicción de Emisiones CO2 🌍🚗** | 202520 KNIME | ADAPTAR | Dataset alterno para regresión múltiple. Reescribir el flujo en scikit-learn; sirve de práctica extra de la semana 13. | `Material Actual/Actividades Organizadas/06_Regresion_y_Pronostico/2025_Regresion_Lineal_con_KNIME_Prediccion_de_Emisiones_CO2/` |
| **Participación \| Actividad en Clase: Regresión Múltiple** | 202520 KNIME | ADAPTAR | Actividad de clase sin enunciado en el export. Redactar de nuevo como el laboratorio del miércoles de la semana 13, sobre el modelo múltiple del negocio del proyecto. | `Material Actual/Actividades Organizadas/06_Regresion_y_Pronostico/2025_Participacion_Actividad_en_Clase_Regresion_Multiple/` |

**Material del seminario de Python**

| Tipo | Recurso | Cómo se usa |
|---|---|---|
| 📓 cuaderno | `S05-C1 · Regresiones · clase_09.ipynb (secciones 3-6 y 8)` | Múltiple con statsmodels, ajuste polinomial, VIF, diagnóstico de residuos y la chuleta de los cuatro supuestos del OLS. |
| 🎛️ simulador | `simuladores/simulador-vif.html` | Mover la correlación entre predictores y ver saltar el VIF. |
| 🎛️ simulador | `simuladores/simulador-overfitting.html` | El grado 10 que sube el R² de entrenamiento y hunde el de validación. |
| 📂 caso | `casos/Caso_03_Scouting_FIFA.md` | Regresión con strings monetarios y multicolinealidad real. Práctica extra. |

### Semana 14 · Modelos de propensión. Clasificación aplicada a decisiones

*LogisticRegression, DecisionTreeClassifier, confusion_matrix, umbral*

**Actividades heredadas de D2L**

| Actividad | Curso | Estado | Qué hay que cambiar | Carpeta |
|---|---|---|---|---|
| **Supervised Learning - KNN \| Telco Churn** | 202410 Python+Tableau | ADAPTAR | Caso de churn muy alineado con propensión. Cambiar KNN por LogisticRegression y DecisionTreeClassifier, y añadir matriz de confusión traducida a dinero y curva de ganancia. | `Material Actual/Actividades Organizadas/07_Clasificacion_y_Propension/2024_Supervised_Learning_KNN_Telco_Churn/` |
| **Predicción de Abandono Laboral en KNIME 👨🏽‍🔧** | 202520 KNIME | ADAPTAR | El mejor enunciado heredado: ya pide comparativa de modelos, métricas y recomendación de una página, y ya admite IA generativa. Solo hay que portar el flujo a scikit-learn y sustituir SMOTE por manejo de umbral. | `Material Actual/Actividades Organizadas/07_Clasificacion_y_Propension/2025_Prediccion_de_Abandono_Laboral_en_KNIME/` |

**Material del seminario de Python**

| Tipo | Recurso | Cómo se usa |
|---|---|---|
| 📓 cuaderno | `S05-C2 · Regresión Logística · clase_10.ipynb` | Sigmoide, log-odds, umbral ajustado, regularización y validación cruzada. Su sección 5 es SMOTE: en ADM 2003 se sustituye por manejo de umbral y matriz de confusión traducida a dinero. |
| 📓 cuaderno | `S06-C1 · Árbol de Decisión · clase_11.ipynb` | Gini paso a paso, poda, GridSearchCV, importancia de variables y comparación contra logística. |
| 📓 cuaderno | `S06-C2 · Métricas · clase_12.ipynb` | Matriz de confusión, ROC-AUC y comparación robusta entre modelos. |
| 🎛️ simulador | `simuladores/simulador-confusion-matrix.html` | Mover el umbral y ver el efecto en falsos positivos y negativos. |
| 📂 caso | `casos/Caso_08_Fraude_Tarjetas.md` | Desbalance extremo y ajuste de umbral, para el ejercicio de focalización con presupuesto. |

### Semana 15 · De la predicción a la decisión. Ética y gobernanza del dato

*Auditoría de sesgo, privacidad, explicabilidad, clínica de proyectos*

**Actividades heredadas de D2L:** ninguna.

### Semana 16 · Cierre del curso y presentación final

*Cuaderno reproducible documentado y defensa del proyecto*

**Actividades heredadas de D2L**

| Actividad | Curso | Estado | Qué hay que cambiar | Carpeta |
|---|---|---|---|---|
| **Evaluación 360** | 202410 Python+Tableau | ADAPTAR | Formularios de Google por grupo. Rehacer los enlaces con los grupos nuevos del semestre. | `Material Actual/Actividades Organizadas/00_Gestion_de_Curso_y_Equipos/2024_Evaluacion_360/` |
| **Proyecto Final - Aplicación de la Analítica de Datos en Procesos Empresariales (EN VIDEO)** | 202410 Python+Tableau | ADAPTAR | Formato video de 8 minutos. El cronograma nuevo pide defensa ante panel: conservar la rúbrica y cambiar el formato de entrega. | `Material Actual/Actividades Organizadas/10_Proyecto_Integrador/2024_Proyecto_Final_Aplicacion_de_la_Analitica_de_Datos_en_Procesos_Empresa/` |
| **Proyecto Final - Aplicación de la Analítica de Datos en Procesos Empresariales** | 202520 KNIME | ADAPTAR | Enunciado más completo. Actualizar el entregable a cuaderno reproducible más recomendación de una página, y exigir línea base declarada. | `Material Actual/Actividades Organizadas/10_Proyecto_Integrador/2025_Proyecto_Final_Aplicacion_de_la_Analitica_de_Datos_en_Procesos_Empresa/` |

**Material del seminario de Python**

| Tipo | Recurso | Cómo se usa |
|---|---|---|
| 📓 cuaderno | `SF · Presentaciones finales · clase_17.ipynb` | Data storytelling, pirámide de Minto, presentación de diez minutos, preguntas del tribunal y rúbrica resumida. Se adopta completo. |

---

## 3. Actividades transversales y de nivelación

| Actividad | Curso | Estado | Nota |
|---|---|---|---|
| Certificaciones Datacamp | 202410 Python+Tableau | ADAPTAR | Ruta vieja: Excel, Tableau e Introduction to Python. Reemplazar por la ruta Python del cronograma nuevo (pandas, joining data, matplotlib, statsmodels, scikit-learn). |
| Certificado Datacamp 1 | 202520 KNIME | ADAPTAR | Contenedor de entrega genérico. Renombrar al curso concreto de cada semana. |
| Certificado datacamp 2 | 202520 KNIME | ADAPTAR | Contenedor de entrega genérico. Renombrar al curso concreto de cada semana. |
| Certificado datacamp 3 | 202520 KNIME | ADAPTAR | Contenedor de entrega genérico. Renombrar al curso concreto de cada semana. |
| Certificado 4 Datacamp | 202520 KNIME | ADAPTAR | Contenedor de entrega genérico. El cronograma nuevo pide ocho certificaciones y solo hay cinco carpetas de entrega: faltan tres. |
| Cuaderno Introducción a Python | 202410 Python+Tableau | ADAPTAR | Cuaderno Colab de fundamentos. En el cronograma nuevo no hay semana de sintaxis: pasa a material de nivelación opcional y no calificado de las semanas 1 a 3, junto a DataCamp Introduction to Python. |
| Python - Introducción a python, parte 2 | 202410 Python+Tableau | ADAPTAR | Estructuras básicas de datos. Igual que el anterior: material de nivelación opcional y no calificado de las semanas 1 a 3. |

**Ruta DataCamp del cronograma v2** — ocho certificaciones contra cinco carpetas de entrega existentes, faltan tres: Understanding Data Science (s1), Introduction to Python (s3), Data Manipulation with pandas y Joining Data with pandas (s5, que lleva dos por ser la semana fusionada), Introduction to Data Visualization with Matplotlib (s6), Unsupervised Learning in Python (s8), Introduction to Regression with statsmodels (s12) y Supervised Learning with scikit-learn (s14). Verificar los nombres contra el catálogo vigente antes de publicarlos en D2L.

---

## 4. Actividades heredadas que NO se pueden reutilizar

Son **16** de las 53. Diez son duplicados entre los dos semestres, no material malo.

| Actividad | Curso | Motivo | Carpeta |
|---|---|---|---|
| Contrato de Grupo | 202520 KNIME | Duplicado del de 202410 y sin enunciado en el export. Conservar solo una versión. | `Material Actual/Actividades Organizadas/00_Gestion_de_Curso_y_Equipos/2025_Contrato_de_Grupo/` |
| Evaluación 360 | 202520 KNIME | Duplicado sin enunciado. Conservar la versión 202410. | `Material Actual/Actividades Organizadas/00_Gestion_de_Curso_y_Equipos/2025_Evaluacion_360/` |
| Giveaway Club de Casos | 202410 Python+Tableau | Actividad promocional de un club estudiantil, sin objetivo de aprendizaje. | `Material Actual/Actividades Organizadas/00_Gestion_de_Curso_y_Equipos/2024_Giveaway_Club_de_Casos/` |
| Giveaway Club de Casos | 202520 KNIME | Actividad promocional, sin objetivo de aprendizaje. | `Material Actual/Actividades Organizadas/00_Gestion_de_Curso_y_Equipos/2025_Giveaway_Club_de_Casos/` |
| Punto Extra \| Asistencia: Jornadas de Salud Mental | 202520 KNIME | Punto extra administrativo, no es contenido del curso. | `Material Actual/Actividades Organizadas/00_Gestion_de_Curso_y_Equipos/2025_Punto_Extra_Asistencia_Jornadas_de_Salud_Mental/` |
| Sin título | 202410 Python+Tableau | Carpeta de entrega vacía en el export, sin título ni enunciado. | `Material Actual/Actividades Organizadas/00_Gestion_de_Curso_y_Equipos/2024_Sin_titulo/` |
| Sistema bancario en Python | 202410 Python+Tableau | Ejercicio de programación pura (diccionarios, listas, funciones). El curso nuevo es de análisis con pandas, no de fundamentos de programación. Guardar como reto opcional. | `Material Actual/Actividades Organizadas/01_Fundamentos_de_Python/2024_Sistema_bancario_en_Python/` |
| Taller 03 \| Estadística Descriptiva en KNIME | 202520 KNIME | Versión KNIME del mismo contenido y sin enunciado en el export. Queda cubierto por el cuaderno de pandas de 202410. | `Material Actual/Actividades Organizadas/03_Estadistica_Descriptiva/2025_Taller_03_Estadistica_Descriptiva_en_KNIME/` |
| Data visualization I | 202520 KNIME | Duplicado del de 202410, mismo adjunto 2.1 EXERCISE.xlsx. | `Material Actual/Actividades Organizadas/04_Visualizacion_de_Datos/2025_Data_visualization_I/` |
| Participación \| Data Visualization II – Diseño y Proceso | 202520 KNIME | Duplicado en formato participación, sin enunciado en el export. | `Material Actual/Actividades Organizadas/04_Visualizacion_de_Datos/2025_Participacion_Data_Visualization_II_Diseno_y_Proceso/` |
| Participación \| Data Visualization III – Estado de Resultados | 202520 KNIME | Duplicado, mismo adjunto 2.2 EXERCISE.xlsx. | `Material Actual/Actividades Organizadas/04_Visualizacion_de_Datos/2025_Participacion_Data_Visualization_III_Estado_de_Resultados/` |
| Dashboard de Superstore en Tableau | 202520 KNIME | Duplicado sin enunciado. | `Material Actual/Actividades Organizadas/05_Dashboards_y_Tableros/2025_Dashboard_de_Superstore_en_Tableau/` |
| Regresión Lineal Simple KNIME | 202520 KNIME | Mismo dataset Advertising.csv en KNIME. Cubierto por el cuaderno de 202410. | `Material Actual/Actividades Organizadas/06_Regresion_y_Pronostico/2025_Regresion_Lineal_Simple_KNIME/` |
| Harvard Case - Data-Driven Management of Blue Detergent | 202520 KNIME | Duplicado exacto, mismo PDF. | `Material Actual/Actividades Organizadas/09_Casos_y_Procesos_de_Negocio/2025_Harvard_Case_Data_Driven_Management_of_Blue_Detergent/` |
| Use Strategic Thinking to Create the Life You Want | 202410 Python+Tableau | Artículo de desarrollo personal (BCG/HBR). No tiene espacio temático en el cronograma nuevo; conservar como actividad opcional de cierre si se quiere. | `Material Actual/Actividades Organizadas/12_Desarrollo_Personal/2024_Use_Strategic_Thinking_to_Create_the_Life_You_Want/` |
| Use Strategic Thinking to Create the Life You Want | 202520 KNIME | Duplicado de la anterior. | `Material Actual/Actividades Organizadas/12_Desarrollo_Personal/2025_Use_Strategic_Thinking_to_Create_the_Life_You_Want/` |

### Lectura de los descartes

**Duplicados entre semestres (10).** Casi todo lo de 202520 es la misma actividad de 202410 rehecha en KNIME y sin enunciado exportado. Se conserva la versión con texto y se descarta la otra. No se pierde contenido.

**Herramientas que salen del curso.** Los flujos de KNIME no son portables: se rescata el enunciado, el dataset y la pregunta de negocio, y el flujo se reescribe como cuaderno. Lo mismo con Tableau en el dashboard de SuperStore, que ahora se rehace en Plotly o Streamlit. Las certificaciones DataCamp de Excel y de Tableau quedan reemplazadas por la ruta de Python.

**Contenido fuera de alcance (5).** Sistema bancario en Python es programación pura y el cronograma no tiene semana de sintaxis. Use Strategic Thinking es desarrollo personal. Los dos Giveaway del Club de Casos y el punto extra por Jornadas de Salud Mental son administrativos.

**Carpeta vacía (1).** La actividad Sin título de 202410 se exportó sin título, sin enunciado y sin adjuntos.

> **Los cinco casos adoptados hay que recortarlos.** Los casos del seminario de Python cierran con una Fase 4 que exige una API en FastAPI y un tablero en Streamlit. ADM 2003 no enseña FastAPI y su entregable es un cuaderno reproducible: al adoptar los casos 01, 03 y 08 hay que sustituir la API por una función documentada dentro del cuaderno y dejar el tablero como opcional.

---

## 5. Material del seminario de Python que no entra

| Recurso | Motivo |
|---|---|
| `S01-C2 · Fundamentos de Python I · clase_02.ipynb` | Sintaxis y tipos primitivos. ADM 2003 no tiene semana de fundamentos: pasa a material de nivelación opcional. |
| `S02-C1 · Fundamentos de Python II · clase_03.ipynb` | Control de flujo, colecciones y funciones. Nivelación opcional. |
| `S03-C1 · OOP · clase_05.ipynb` | Programación orientada a objetos. Fuera de alcance para un curso de análisis de negocio. |
| `S07-C1 · Ensembles y Random Forest · clase_13.ipynb` | Bagging, boosting y OOB. Excede el bloque de propensión de ADM 2003; queda como lectura de ampliación. |
| `S08-C2 · APIs con FastAPI · clase_16.ipynb` | Poner un modelo en producción. El entregable de ADM 2003 es un cuaderno reproducible, no un servicio. |
| `Casos 04, 05, 07, 09 y 10` | Movilidad NYC, sismicidad, Spotify, OLIST y Stack Overflow. Buenos casos, pero sin encaje en las semanas de ADM 2003; quedan como banco alterno para el proyecto integrador. |

---

## 6. Lo que queda por construir

Después de cruzar las dos fuentes, ninguna semana se queda sin material, pero tres siguen cojas:

| Semana | Qué falta | Con qué se arma |
|---|---|---|
| 10 · Estrategia y transformación digital | Es la semana nueva: no existe en ninguno de los tres cursos como sesión completa, y el seminario de Python no aporta nada | El caso Banco Andino aporta el journey map y el Diagnóstico con pymedigital.ec aporta la madurez digital. Falta entera la sesión conceptual del lunes sobre transformación digital y modelo de negocio |
| 11 · Mapa de modelos y creación de valor | El catálogo de doce problemas de negocio del laboratorio | El caso Harvard de Blue Detergent y la sección de elección de métrica del cuaderno de métricas. El catálogo hay que escribirlo |
| 15 · Ética y gobernanza | Es la semana más desabastecida: ni actividad heredada, ni cuaderno, ni caso. Ninguno de los diez casos del seminario menciona sesgo, equidad ni privacidad | Hay que escribirla completa: el caso de riesgo crediticio, la auditoría del modelo propio y la clínica de consultoría entre grupos |

Las semanas 5, 9 y 16, que en la versión 1 estaban vacías o flojas, quedaron cubiertas por el seminario de Python: Pandas II para agrupar y combinar, la sesión de hipótesis y pruebas estadísticas para causalidad, y la sesión final de storytelling y defensa con su rúbrica.

## 7. Las cinco piezas que no hay que rehacer

1. **`casos/Caso_01_Segmentacion_Clientes_Retail.md`** — el enunciado del proyecto de medio semestre casi escrito: fases, criterio del codo y silueta para elegir K, y perfiles de negocio. Dos ajustes obligatorios: es RFM sin la P (no calcula margen) y corre sobre Online Retail II, no sobre SuperStore. O se adopta su dataset y se añade la dimensión de margen, o se conserva SuperStore del cuaderno de 202410 y se le trasplanta la estructura de fases de este caso. Escala con `RobustScaler`, que es la elección correcta con las colas de RFM.
2. **`casos/Entregable_Intermedio_Mitad_Seminario.md`** — rúbrica del corte de mitad de semestre, incluida la bitácora obligatoria de uso de IA. Encaja exactamente con la semana 8.
3. **`SF · clase_17.ipynb`** — data storytelling, pirámide de Minto, preguntas del tribunal y rúbrica de defensa. La semana 16 completa.
4. **Predicción de Abandono Laboral** (202520) — el enunciado mejor escrito de los cursos de D2L: comparativa de modelos, tabla de métricas y una página de recomendaciones, y ya admite resolverlo con IA generativa.
5. **Los seis simuladores HTML** — regresión lineal, regresión 3D, VIF, overfitting, train-test y matriz de confusión. Son exactamente los conceptos donde el curso viejo perdía a la gente.
