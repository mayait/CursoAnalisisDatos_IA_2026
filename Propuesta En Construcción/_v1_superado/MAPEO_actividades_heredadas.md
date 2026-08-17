# ADM 2003 · Mapeo de actividades heredadas a la propuesta Python + IA

Generado a partir de los dos exports de D2L de la carpeta `Material Actual`: **202410.1.1029** (versión Python + Tableau, 24 actividades) y **202520.1.1961** (versión KNIME, 29 actividades). Total: **53 actividades**.

Los enunciados completos y los adjuntos están en `Material Actual/Actividades Organizadas/`, organizados en 13 bloques temáticos más una carpeta de lecturas.

**Advertencia sobre el export 202520.** D2L exportó ese curso sin el texto de las instrucciones: 26 de sus 29 actividades vienen con el enunciado vacío y solo conservan título, puntaje y adjuntos. Solo tres conservan texto: Predicción de Abandono Laboral, Proyecto Final · Aplicación y Proyecto Final · Diagnóstico. Donde existe la versión equivalente de 202410, el enunciado sí está completo. Las actividades de 202520 marcadas como ADAPTAR requieren redactar el enunciado de nuevo.

Estados: **REUTILIZABLE** = el enunciado sirve casi tal cual · **ADAPTAR** = la idea y los datos sirven, la herramienta o el entregable cambian · **DESCARTAR** = no entra en el curso nuevo.

---

## 1. Resumen por semana

| Semana | Tema | Actividades heredadas | Estado |
|---|---|---|---|
| 1 | Introducción a Business Analytics y Big Data en la era de la IA | Contrato de Grupo (202410)<br>Sin inteligencia artificial no te van a escuchar. ¿Valor o Humo? (202520) | ADAPTAR, REUTILIZABLE |
| 2 | Business Analytics en las organizaciones. La pregunta antes del dato | Taller 01 \| Introducción a KNIME con Pizza Sales (202520)<br>Caso Banco Andino - Journey Map (202410) | ADAPTAR, REUTILIZABLE |
| 3 | Estadística descriptiva aplicada al negocio | Taller 02 \| Ejercicio: Análisis Individual Pizza Sales (202520)<br>Python \| Estadística descriptiva con Pandas (202410) | ADAPTAR, REUTILIZABLE |
| 4 | Anatomía y calidad de los datos | Análisis exploratorio con KNIME (202520)<br>Diagnostico de la Analítica de Datos en Procesos Empresariales (202410)<br>Proyecto Final \| Diagnóstico de Analítica de Datos en la Empresa (202520) | ADAPTAR, REUTILIZABLE |
| 5 | Manipulación de datos I. Filtrar, derivar, agrupar y agregar | Participación \| Taller Grupal: Análisis Exploratorio SuperStore (202520) | ADAPTAR |
| 6 | Manipulación de datos II. Uniones, reestructuración y fuentes externas | _ninguna_ | **VACÍO** |
| 7 | Visualización de datos | Data visualization I (202410)<br>Data visualization II (202410)<br>Data visualization III (202410)<br>Lectura Data Storytelling (202520) | ADAPTAR, REUTILIZABLE |
| 8 | Visualización avanzada y tableros | Data Visualization IV (Resultados financieros) (202410)<br>Dashboard de Superstore en Tableau (202410) | ADAPTAR |
| 9 | Comparación, variabilidad y causalidad | _ninguna_ | **VACÍO** |
| 10 | Modelos analíticos. Tipos de modelos y creación de valor | Harvard Case - Data-Driven Management of Blue Detergent (202410) | REUTILIZABLE |
| 11 | Modelos de pronóstico. Regresión lineal y múltiple | Regresión Lineal Python (202410)<br>Regresión Lineal (2) Multiple (202410)<br>Regresión Lineal Parte 3 (202410)<br>Regresión publicidad, influencers y ventas 🦾🦾 en KNIME (202520)<br>Regresión Lineal con KNIME: Predicción de Emisiones CO2 🌍🚗 (202520)<br>Participación \| Actividad en Clase: Regresión Múltiple (202520) | ADAPTAR, REUTILIZABLE |
| 12 | Modelos de propensión. Clasificación aplicada a decisiones | Supervised Learning - KNN \| Telco Churn (202410)<br>Predicción de Abandono Laboral en KNIME 👨🏽‍🔧 (202520) | ADAPTAR |
| 13 | Minería de datos. Segmentación y asociación | Análisis RFM + P para Superstore (Individual) Primera parte. (202410)<br>Proyecto Grupal \| Análisis RFM+P: Clasificación de Clientes SuperStore (202520) | ADAPTAR, REUTILIZABLE |
| 14 | Anomalías, datos no estructurados y construcción de KPIs | _ninguna_ | **VACÍO** |
| 15 | De la predicción a la decisión. Ética y gobernanza del dato | _ninguna_ | **VACÍO** |
| 16 | Cierre del curso y presentación final | Evaluación 360 (202410)<br>Proyecto Final - Aplicación de la Analítica de Datos en Procesos Empresariales (EN VIDEO) (202410)<br>Proyecto Final - Aplicación de la Analítica de Datos en Procesos Empresariales (202520) | ADAPTAR |

---

## 2. Detalle semana por semana

### Semana 1 · Introducción a Business Analytics y Big Data en la era de la IA

*Colab, cuadernos ejecutables, protocolo de uso de IAG y bitácora de prompts*

| Actividad heredada | Curso | Estado | Qué hay que cambiar | Carpeta |
|---|---|---|---|---|
| **Contrato de Grupo** | 202410 Python+Tableau | REUTILIZABLE | Sirve tal cual. Añadir la firma del protocolo de uso de IA generativa que pide la semana 1. | `Material Actual/Actividades Organizadas/00_Gestion_de_Curso_y_Equipos/2024_Contrato_de_Grupo/` |
| **Sin inteligencia artificial no te van a escuchar. ¿Valor o Humo?** | 202520 KNIME | ADAPTAR | Debate sobre valor real frente a humo de la IA. Encaja con la apertura de la semana 1; hay que redactar el enunciado porque el export viene vacío. | `Material Actual/Actividades Organizadas/09_Casos_y_Procesos_de_Negocio/2025_Sin_inteligencia_artificial_no_te_van_a_escuchar_Valor_o_Humo/` |

### Semana 2 · Business Analytics en las organizaciones. La pregunta antes del dato

*pandas: read_csv, head, info, shape. Ficha de análisis y unidad de análisis*

| Actividad heredada | Curso | Estado | Qué hay que cambiar | Carpeta |
|---|---|---|---|---|
| **Taller 01 \| Introducción a KNIME con Pizza Sales** | 202520 KNIME | ADAPTAR | Excelente dataset de entrada. Reescribir el flujo KNIME como cuaderno Colab: read_csv, head, info, shape sobre pizza_sales.xlsx. | `Material Actual/Actividades Organizadas/02_Primer_Contacto_con_Datos_y_EDA/2025_Taller_01_Introduccion_a_KNIME_con_Pizza_Sales/` |
| **Caso Banco Andino - Journey Map** | 202410 Python+Tableau | REUTILIZABLE | Blueprint del proceso de apertura de cuenta. Es la mejor actividad para la semana 2: de dónde salen los datos y cuál es la unidad de análisis. Sin código. | `Material Actual/Actividades Organizadas/09_Casos_y_Procesos_de_Negocio/2024_Caso_Banco_Andino_Journey_Map/` |

### Semana 3 · Estadística descriptiva aplicada al negocio

*pandas: describe, value_counts, quantile*

| Actividad heredada | Curso | Estado | Qué hay que cambiar | Carpeta |
|---|---|---|---|---|
| **Taller 02 \| Ejercicio: Análisis Individual Pizza Sales** | 202520 KNIME | ADAPTAR | El banco de preguntas (EDA_Pizza_BancoPreguntas.docx) es estadística descriptiva pura (media frente a mediana, percentiles, dispersión, outliers) y se reutiliza casi íntegro como las doce preguntas contra reloj del laboratorio de la semana 3. Cambiar la herramienta a pandas. | `Material Actual/Actividades Organizadas/02_Primer_Contacto_con_Datos_y_EDA/2025_Taller_02_Ejercicio_Analisis_Individual_Pizza_Sales/` |
| **Python \| Estadística descriptiva con Pandas** | 202410 Python+Tableau | REUTILIZABLE | Cuaderno Colab con Credit.csv. Es el mejor calce directo del curso viejo. Solo actualizar el enunciado con media frente a mediana y la bitácora de prompts. | `Material Actual/Actividades Organizadas/03_Estadistica_Descriptiva/2024_Python_Estadistica_descriptiva_con_Pandas/` |

### Semana 4 · Anatomía y calidad de los datos

*pandas: dtypes, isna, duplicated, astype*

| Actividad heredada | Curso | Estado | Qué hay que cambiar | Carpeta |
|---|---|---|---|---|
| **Análisis exploratorio con KNIME** | 202520 KNIME | ADAPTAR | Rehacer como inventario de calidad de datos con dtypes, isna, duplicated y astype. Es la base del Deber 2 (bitácora de limpieza). | `Material Actual/Actividades Organizadas/02_Primer_Contacto_con_Datos_y_EDA/2025_Analisis_exploratorio_con_KNIME/` |
| **Diagnostico de la Analítica de Datos en Procesos Empresariales** | 202410 Python+Tableau | REUTILIZABLE | Hito del proyecto integrador, no contenido del tema de la semana: coincide con el entregable Propuesta de proyecto final de la semana 4. El diagnóstico de madurez organizacional (entrevistas, framework, oportunidades) se conserva tal cual. | `Material Actual/Actividades Organizadas/10_Proyecto_Integrador/2024_Diagnostico_de_la_Analitica_de_Datos_en_Procesos_Empresariales/` |
| **Proyecto Final \| Diagnóstico de Analítica de Datos en la Empresa** | 202520 KNIME | REUTILIZABLE | Hito del proyecto integrador que se entrega en la semana 4. Versión mejorada de la de 202410: añade la evaluación de madurez digital con pymedigital.ec. Usar esta como base. | `Material Actual/Actividades Organizadas/10_Proyecto_Integrador/2025_Proyecto_Final_Diagnostico_de_Analitica_de_Datos_en_la_Empresa/` |

### Semana 5 · Manipulación de datos I. Filtrar, derivar, agrupar y agregar

*pandas: query, assign, groupby, agg*

| Actividad heredada | Curso | Estado | Qué hay que cambiar | Carpeta |
|---|---|---|---|---|
| **Participación \| Taller Grupal: Análisis Exploratorio SuperStore** | 202520 KNIME | ADAPTAR | Encaja con el torneo de preguntas de la semana 5. Reescribir con groupby y agg; sin enunciado en el export, hay que redactarlo de nuevo. | `Material Actual/Actividades Organizadas/02_Primer_Contacto_con_Datos_y_EDA/2025_Participacion_Taller_Grupal_Analisis_Exploratorio_SuperStore/` |

### Semana 6 · Manipulación de datos II. Uniones, reestructuración y fuentes externas

*pandas: merge, concat, pivot_table, resample, read_sql, requests*

> ⚠️ **Sin material heredado.** No hay ninguna actividad heredada sobre uniones y cardinalidad. Es el hueco más grave: el error de la unión que duplica filas es justo el que llega a un directorio. Hay que crear el laboratorio de la tabla mensual de indicadores desde cuatro fuentes, cuadrada contra una cifra de control.

### Semana 7 · Visualización de datos

*matplotlib y seaborn*

| Actividad heredada | Curso | Estado | Qué hay que cambiar | Carpeta |
|---|---|---|---|---|
| **Data visualization I** | 202410 Python+Tableau | REUTILIZABLE | Ejercicio 2.1 de Knaflic, agnóstico de herramienta. Pedir el gráfico en matplotlib o seaborn en vez de PowerPoint. | `Material Actual/Actividades Organizadas/04_Visualizacion_de_Datos/2024_Data_visualization_I/` |
| **Data visualization II** | 202410 Python+Tableau | REUTILIZABLE | Bocetos en papel a slide. Mantener el boceto a mano y exigir que la versión final sea código. | `Material Actual/Actividades Organizadas/04_Visualizacion_de_Datos/2024_Data_visualization_II/` |
| **Data visualization III** | 202410 Python+Tableau | REUTILIZABLE | Ejercicio 2.2: mapa de calor, columnas y línea. Traducir los tres pasos a matplotlib y discutir cuál comunica mejor. | `Material Actual/Actividades Organizadas/04_Visualizacion_de_Datos/2024_Data_visualization_III/` |
| **Lectura Data Storytelling** | 202520 KNIME | ADAPTAR | El PDF de Cole Nussbaumer Knaflic está en 99_Lecturas_y_Material_de_Apoyo, pero el export no trae el enunciado: hay que redactar de nuevo las preguntas de la lectura previa de la semana 7. | `Material Actual/Actividades Organizadas/04_Visualizacion_de_Datos/2025_Lectura_Data_Storytelling/` |

### Semana 8 · Visualización avanzada y tableros

*Plotly, anotación y composición de tableros*

| Actividad heredada | Curso | Estado | Qué hay que cambiar | Carpeta |
|---|---|---|---|---|
| **Data Visualization IV (Resultados financieros)** | 202410 Python+Tableau | ADAPTAR | Contar un estado de resultados a no financieros. Tal cual es storytelling estático de la semana 7; para justificar la semana 8 hay que reescribirlo como cascada interactiva en Plotly con jerarquía visual. | `Material Actual/Actividades Organizadas/04_Visualizacion_de_Datos/2024_Data_Visualization_IV_Resultados_financieros/` |
| **Dashboard de Superstore en Tableau** | 202410 Python+Tableau | ADAPTAR | La pregunta de negocio (¿qué pasa con profit en el último año?) se conserva; el tablero se rehace en Plotly dentro del cuaderno. Tableau sale del curso. | `Material Actual/Actividades Organizadas/05_Dashboards_y_Tableros/2024_Dashboard_de_Superstore_en_Tableau/` |

### Semana 9 · Comparación, variabilidad y causalidad

*crosstab, Simpson, confusión y diseño de pruebas A/B*

> ⚠️ **Sin material heredado.** No hay ninguna actividad heredada sobre causalidad ni diseño experimental. Ninguno de los dos cursos anteriores tocaba pruebas A/B. Hay que crear el Deber 4 desde cero.

### Semana 10 · Modelos analíticos. Tipos de modelos y creación de valor

*train_test_split, DummyRegressor, DummyClassifier*

| Actividad heredada | Curso | Estado | Qué hay que cambiar | Carpeta |
|---|---|---|---|---|
| **Harvard Case - Data-Driven Management of Blue Detergent** | 202410 Python+Tableau | REUTILIZABLE | Caso HBP de decisión con datos. Encaja con la semana bisagra: asignar familia de modelo, decisión, línea base y valor anual estimado. | `Material Actual/Actividades Organizadas/09_Casos_y_Procesos_de_Negocio/2024_Harvard_Case_Data_Driven_Management_of_Blue_Detergent/` |

### Semana 11 · Modelos de pronóstico. Regresión lineal y múltiple

*LinearRegression, statsmodels, residuos, MAE*

| Actividad heredada | Curso | Estado | Qué hay que cambiar | Carpeta |
|---|---|---|---|---|
| **Regresión Lineal Python** | 202410 Python+Tableau | REUTILIZABLE | Cuaderno Colab de regresión simple con Advertising.csv. Añadir la línea base con DummyRegressor y el error porcentual que exige el cronograma nuevo. | `Material Actual/Actividades Organizadas/06_Regresion_y_Pronostico/2024_Regresion_Lineal_Python/` |
| **Regresión Lineal (2) Multiple** | 202410 Python+Tableau | REUTILIZABLE | Cuaderno de regresión múltiple. Añadir análisis de residuos y comparación honesta contra la regla ingenua. | `Material Actual/Actividades Organizadas/06_Regresion_y_Pronostico/2024_Regresion_Lineal_2_Multiple/` |
| **Regresión Lineal Parte 3** | 202410 Python+Tableau | ADAPTAR | Ejercicio de cierre del bloque. Verificar que el cuaderno de GitHub siga vivo y reencuadrarlo hacia el pronóstico del negocio del proyecto. | `Material Actual/Actividades Organizadas/06_Regresion_y_Pronostico/2024_Regresion_Lineal_Parte_3/` |
| **Regresión publicidad, influencers y ventas 🦾🦾 en KNIME** | 202520 KNIME | ADAPTAR | El encuadre de negocio (influencers) es mejor que el del cuaderno viejo. Rescatar el enunciado y montarlo sobre scikit-learn. | `Material Actual/Actividades Organizadas/06_Regresion_y_Pronostico/2025_Regresion_publicidad_influencers_y_ventas_en_KNIME/` |
| **Regresión Lineal con KNIME: Predicción de Emisiones CO2 🌍🚗** | 202520 KNIME | ADAPTAR | Buen dataset alterno para regresión múltiple. Reescribir el flujo en scikit-learn; útil como ejercicio de práctica extra. | `Material Actual/Actividades Organizadas/06_Regresion_y_Pronostico/2025_Regresion_Lineal_con_KNIME_Prediccion_de_Emisiones_CO2/` |
| **Participación \| Actividad en Clase: Regresión Múltiple** | 202520 KNIME | ADAPTAR | Actividad de clase sin enunciado en el export. Redactar de nuevo como el laboratorio del miércoles de la semana 11. | `Material Actual/Actividades Organizadas/06_Regresion_y_Pronostico/2025_Participacion_Actividad_en_Clase_Regresion_Multiple/` |

### Semana 12 · Modelos de propensión. Clasificación aplicada a decisiones

*LogisticRegression, DecisionTreeClassifier, confusion_matrix, umbral*

| Actividad heredada | Curso | Estado | Qué hay que cambiar | Carpeta |
|---|---|---|---|---|
| **Supervised Learning - KNN \| Telco Churn** | 202410 Python+Tableau | ADAPTAR | Caso de churn muy alineado con propensión. Cambiar KNN por LogisticRegression y DecisionTreeClassifier, y añadir matriz de confusión traducida a dinero y curva de ganancia. | `Material Actual/Actividades Organizadas/07_Clasificacion_y_Propension/2024_Supervised_Learning_KNN_Telco_Churn/` |
| **Predicción de Abandono Laboral en KNIME 👨🏽‍🔧** | 202520 KNIME | ADAPTAR | El mejor enunciado heredado: ya pide comparativa de modelos, métricas y recomendación de una página, y ya admite IA generativa. Solo hay que portar el flujo a scikit-learn y sustituir SMOTE por manejo de umbral. | `Material Actual/Actividades Organizadas/07_Clasificacion_y_Propension/2025_Prediccion_de_Abandono_Laboral_en_KNIME/` |

### Semana 13 · Minería de datos. Segmentación y asociación

*KMeans, StandardScaler, RFM, canasta de mercado*

| Actividad heredada | Curso | Estado | Qué hay que cambiar | Carpeta |
|---|---|---|---|---|
| **Análisis RFM + P para Superstore (Individual) Primera parte.** | 202410 Python+Tableau | REUTILIZABLE | Ya está en Colab y ya exige incluir el prompt final usado con el LLM, que es exactamente la política de IA del curso nuevo. Añadir KMeans y StandardScaler. | `Material Actual/Actividades Organizadas/08_Segmentacion_RFM/2024_Analisis_RFM_P_para_Superstore_Individual_Primera_parte/` |
| **Proyecto Grupal \| Análisis RFM+P: Clasificación de Clientes SuperStore** | 202520 KNIME | ADAPTAR | Versión grupal del mismo análisis. Convertirla en el laboratorio de la semana 13: nombrar segmentos y escribir el mensaje comercial de cada uno. | `Material Actual/Actividades Organizadas/08_Segmentacion_RFM/2025_Proyecto_Grupal_Analisis_RFM_P_Clasificacion_de_Clientes_SuperStore/` |

### Semana 14 · Anomalías, datos no estructurados y construcción de KPIs

*Detección de anomalías, LLM por API sobre texto libre, tablero de KPIs*

> ⚠️ **Sin material heredado.** No hay ninguna actividad heredada sobre anomalías, texto no estructurado ni KPIs. Lo más cercano es el dashboard de Tableau, que se reubicó en la semana 8. Hay que crear el corpus de reseñas y el tablero de KPIs.

### Semana 15 · De la predicción a la decisión. Ética y gobernanza del dato

*Auditoría de sesgo, privacidad, explicabilidad, clínica de proyectos*

> ⚠️ **Sin material heredado.** No hay ninguna actividad heredada sobre ética, sesgo o privacidad. En el curso viejo esta semana era el puente KNIME a Python. Hay que crear la auditoría de sesgo y la consultoría entre grupos.

### Semana 16 · Cierre del curso y presentación final

*Cuaderno reproducible documentado y defensa del proyecto*

| Actividad heredada | Curso | Estado | Qué hay que cambiar | Carpeta |
|---|---|---|---|---|
| **Evaluación 360** | 202410 Python+Tableau | ADAPTAR | Formularios de Google por grupo. Rehacer los enlaces con los grupos nuevos del semestre. | `Material Actual/Actividades Organizadas/00_Gestion_de_Curso_y_Equipos/2024_Evaluacion_360/` |
| **Proyecto Final - Aplicación de la Analítica de Datos en Procesos Empresariales (EN VIDEO)** | 202410 Python+Tableau | ADAPTAR | Formato video de 8 minutos. El cronograma nuevo pide defensa ante panel: conservar la rúbrica y cambiar el formato de entrega. | `Material Actual/Actividades Organizadas/10_Proyecto_Integrador/2024_Proyecto_Final_Aplicacion_de_la_Analitica_de_Datos_en_Procesos_Empresa/` |
| **Proyecto Final - Aplicación de la Analítica de Datos en Procesos Empresariales** | 202520 KNIME | ADAPTAR | Enunciado más completo. Actualizar el entregable a cuaderno reproducible más recomendación de una página, y exigir línea base declarada. | `Material Actual/Actividades Organizadas/10_Proyecto_Integrador/2025_Proyecto_Final_Aplicacion_de_la_Analitica_de_Datos_en_Procesos_Empresa/` |

---

## 3. Actividades transversales

| Actividad | Curso | Estado | Nota |
|---|---|---|---|
| Certificaciones Datacamp | 202410 Python+Tableau | ADAPTAR | Ruta vieja: Excel, Tableau e Introduction to Python. Reemplazar por la ruta Python del cronograma nuevo (pandas, joining data, matplotlib, statsmodels, scikit-learn). |
| Certificado Datacamp 1 | 202520 KNIME | ADAPTAR | Contenedor de entrega genérico. Renombrar al curso concreto de cada semana. |
| Certificado datacamp 2 | 202520 KNIME | ADAPTAR | Contenedor de entrega genérico. Renombrar al curso concreto de cada semana. |
| Certificado datacamp 3 | 202520 KNIME | ADAPTAR | Contenedor de entrega genérico. Renombrar al curso concreto de cada semana. |
| Certificado 4 Datacamp | 202520 KNIME | ADAPTAR | Contenedor de entrega genérico. El cronograma nuevo pide ocho certificaciones y solo hay cinco carpetas de entrega: faltan tres. |

**Ruta DataCamp del cronograma nuevo** (8 certificaciones, contra 5 carpetas de entrega existentes: faltan 3): Understanding Data Science (s1), Introduction to Python (s3), Data Manipulation with pandas (s5), Joining Data with pandas (s6), Introduction to Data Visualization with Matplotlib (s8), Introduction to Regression with statsmodels (s11), Supervised Learning with scikit-learn (s12), Unsupervised Learning in Python (s13). Verificar los nombres contra el catálogo vigente antes de publicarlos en D2L.


### Material de nivelación opcional (no calificado)

| Actividad | Curso | Nota |
|---|---|---|
| Cuaderno Introducción a Python | 202410 Python+Tableau | Cuaderno Colab de fundamentos. En el cronograma nuevo no hay semana de sintaxis: pasa a material de nivelación opcional y no calificado de las semanas 1 a 3, junto a DataCamp Introduction to Python. |
| Python - Introducción a python, parte 2 | 202410 Python+Tableau | Estructuras básicas de datos. Igual que el anterior: material de nivelación opcional y no calificado de las semanas 1 a 3. |

---

## 4. Actividades que NO se pueden reutilizar

Son **16** de las 53. La mayoría son duplicados entre los dos semestres, no material malo.

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

**Herramientas que salen del curso.** Los flujos de KNIME no son portables: se rescata el enunciado, el dataset y la pregunta de negocio, y el flujo se reescribe como cuaderno. Lo mismo con Tableau en el dashboard de SuperStore. Las certificaciones DataCamp de Excel y de Tableau del semestre 202410 quedan reemplazadas por la ruta de Python.

**Contenido fuera de alcance (5).** Sistema bancario en Python es programación pura y el cronograma nuevo no tiene semana de sintaxis. Use Strategic Thinking es desarrollo personal. Los dos Giveaway del Club de Casos y el punto extra por Jornadas de Salud Mental son administrativos. Diez más un cinco más una carpeta vacía suman las dieciséis.

**Carpeta vacía (1).** La actividad Sin título de 202410 se exportó sin título, sin enunciado y sin adjuntos.

---

## 5. Lo que hay que construir desde cero

Cuatro de las dieciséis semanas no tienen ningún antecedente en los cursos anteriores, y son justamente las que dan la ventaja competitiva del rediseño frente a un curso de programación:

| Semana | Qué falta | Por qué importa |
|---|---|---|
| 6 | Uniones, cardinalidad y fuentes externas | Es el error técnico que más caro sale en la práctica: una unión que duplica filas e infla la facturación. Ningún curso anterior lo tocaba. |
| 9 | Causalidad y diseño de pruebas A/B | Sin esto el curso enseña a describir y a predecir, pero no a comparar. Es el Deber 4 completo. |
| 14 | Anomalías, texto no estructurado y KPIs | Es la única semana donde la IA generativa se usa como herramienta de procesamiento y no como asistente de código. |
| 15 | Ética, sesgo y gobernanza | En el sílabo viejo esta semana era el puente KNIME a Python; al desaparecer el puente, el espacio queda libre pero vacío de material. |

Además, la semana 10 (mapa de modelos y ecuación de valor) solo cuenta con el caso Harvard de Blue Detergent. Falta armar el catálogo de doce problemas de negocio que pide el laboratorio del miércoles.

## 6. Lo mejor del material heredado

Tres piezas se pueden llevar casi intactas y conviene no rehacerlas:

1. **Análisis RFM + P para SuperStore** (202410). Ya está en Colab y ya exige adjuntar el prompt final usado con el LLM, que es exactamente la política de IA del curso nuevo. Solo falta añadir KMeans.
2. **Predicción de Abandono Laboral** (202520). El enunciado ya pide comparativa de modelos, tabla de métricas y una página de recomendaciones, y ya admite resolverlo con IA generativa entregando la carpeta del proyecto. Es el enunciado mejor escrito de los dos cursos.
3. **Proyecto Final · Diagnóstico de Analítica de Datos** (202520). Añade la evaluación de madurez digital con pymedigital.ec sobre la versión de 202410. Es la base del proyecto integrador.
