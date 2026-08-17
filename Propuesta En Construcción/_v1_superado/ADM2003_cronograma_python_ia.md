# ADM 2003 Análisis de Datos
## Cronograma de actividades. Versión Python con apoyo de IA

---

## A. Tabla para el sílabo oficial

| Semana | Tema Principal | Enfoque Técnico (Librerías y Herramientas) |
|---|---|---|
| 1 | Introducción a Business Analytics y Big Data en la era de la IA | Google Colab y cuadernos ejecutables. Protocolo de uso de IAG y bitácora de prompts. Recorrido guiado de un análisis completo |
| 2 | Business Analytics en las organizaciones. La pregunta antes del dato | pandas: lectura de archivos, `read_csv`, `head`, `info`, `shape`. Ficha de análisis y definición de la unidad de análisis |
| 3 | Estadística descriptiva aplicada al negocio | pandas: `describe`, `value_counts`, `quantile`. Media frente a mediana, dispersión y línea base |
| 4 | Anatomía y calidad de los datos | pandas: `dtypes`, `isna`, `duplicated`, `astype`. Granularidad, nulos, duplicados y valores extremos |
| 5 | Manipulación de datos I. Filtrar, derivar, agrupar y agregar | pandas: `query`, `assign`, `groupby`, `agg`. Patrón dividir, aplicar y recombinar |
| 6 | Manipulación de datos II. Uniones, reestructuración y fuentes externas | pandas: `merge`, `concat`, `pivot_table`, `resample`. Lectura desde bases de datos y APIs con `read_sql` y `requests` |
| 7 | Visualización de datos | matplotlib y seaborn: línea, barras ordenadas, dispersión, histograma y caja. Reglas de honestidad visual |
| 8 | Visualización avanzada y tableros | Plotly para gráficos interactivos. Anotación, título con conclusión y composición de tableros en cuaderno |
| 9 | Comparación, variabilidad y causalidad | pandas: `crosstab` y comparaciones por grupo. Paradoja de Simpson, variables de confusión y diseño de pruebas A y B |
| 10 | Modelos analíticos. Tipos de modelos y creación de valor | scikit-learn: `train_test_split`, `DummyRegressor` y `DummyClassifier` como línea base obligatoria |
| 11 | Modelos de pronóstico. Regresión lineal y múltiple | scikit-learn y statsmodels: `LinearRegression`, residuos, `mean_absolute_error` y error porcentual |
| 12 | Modelos de propensión. Clasificación aplicada a decisiones | scikit-learn: `LogisticRegression`, `DecisionTreeClassifier`, `confusion_matrix`, umbral y curva de ganancia |
| 13 | Minería de datos. Segmentación y asociación | scikit-learn: `KMeans` y `StandardScaler`. Segmentación RFM y análisis de canasta de mercado |
| 14 | Anomalías, datos no estructurados y construcción de KPIs | Detección de anomalías. Uso de modelos generativos por API para clasificar texto libre y extraer datos. Tablero de KPIs |
| 15 | De la predicción a la decisión. Ética y gobernanza del dato | Auditoría de sesgo, privacidad y explicabilidad. Clínica de proyectos y revisión cruzada |
| 16 | Cierre del curso y presentación final | Entrega del cuaderno reproducible documentado y defensa del proyecto integrador |

---

## B. Plan de sesiones

Dos sesiones semanales de ochenta minutos, lunes y miércoles. La sesión de lunes es conceptual y demostrativa, con un caso que se discute antes de tocar el teclado. La de miércoles es laboratorio en salas de grupos, con entrega corta al cierre.

| Semana | Lunes (concepto y caso) | Miércoles (laboratorio en grupos) | Entregable y certificación |
|---|---|---|---|
| 1 | Por qué fracasan los análisis. Un informe real con datos correctos y conclusión inválida. La escalera descriptivo, diagnóstico, predictivo y prescriptivo | Colab, primer cuaderno y recorrido de un análisis completo de principio a fin. Firma del protocolo de uso de IAG | DataCamp: Understanding Data Science |
| 2 | Unidad de análisis, métrica, comparación y decisión. Clínica de definiciones ambiguas: qué es un cliente activo, qué cuenta como venta | Carga y primer contacto con la base del curso. Cada grupo redacta la ficha de análisis y otro grupo la ataca | Deber 1: ficha de análisis de una página, sin código |
| 3 | La trampa del promedio. Distribuciones bimodales, mediana frente a media, tamaño de muestra. Caso: dos áreas reportan ventas distintas del mismo mes | Perfilado descriptivo de la base. Doce preguntas descriptivas de dificultad creciente contra reloj | DataCamp: Introduction to Python |
| 4 | Granularidad, tipos de dato y calidad. La diferencia entre ausente, cero y desconocido. Caso: el diez por ciento de transacciones sin identificador de cliente | Inventario de problemas de calidad, cuantificación de cada uno y decisión documentada | Deber 2: bitácora de limpieza. Propuesta de proyecto final |
| 5 | Dividir, aplicar y recombinar. Agregación y pérdida de información. Caso: sube el ticket promedio y caen las transacciones | Torneo de preguntas. Cada grupo formula tres preguntas de negocio y otro grupo las responde con datos en quince minutos | DataCamp: Data Manipulation with pandas |
| 6 | Los cuatro tipos de unión y la cardinalidad. El error que llega a un directorio: una unión que duplica filas e infla la facturación | Construir la tabla mensual de indicadores desde cuatro fuentes con granularidades distintas y cuadrar contra una cifra de control | DataCamp: Joining Data with pandas |
| 7 | Explorar, verificar y comunicar. Cuarteto de Anscombe. Repertorio mínimo, ejes, escalas y el título que lleva la conclusión | Clínica de rediseño. Cada grupo toma un gráfico malo publicado y lo rediseña justificando cada cambio | Deber 3: tres gráficos anotados del negocio |
| 8 | Del gráfico al tablero. Interactividad, jerarquía visual y qué se elimina. Fondo blanco y ausencia de decoración | Pitch del proyecto: cada grupo presenta su diagnóstico en tres figuras y recibe fuego cruzado | Pitch del proyecto final. DataCamp: Introduction to Data Visualization with Matplotlib |
| 9 | Comparado con qué. Ruido frente a señal, regresión a la media, confusión y causalidad inversa. Caso: los clientes del programa de fidelidad gastan el doble | Diseño de una prueba A y B ejecutable en el negocio del proyecto, con unidad de asignación, duración y presupuesto | Deber 4: diseño experimental de una página |
| 10 | El mapa de los modelos: pronóstico, propensión, segmentación, asociación, anomalías y optimización. Qué decisión habilita cada uno. La ecuación de valor | Catálogo de doce problemas de negocio. Cada grupo asigna familia, decisión, línea base y valor anual estimado. Se descubre cuáles no justifican ningún modelo | Evaluación intermedia sobre criterio de negocio |
| 11 | Tendencia, estacionalidad y horizonte. El error de pronóstico y su asimetría: quedarse sin producto y que sobre producto no cuestan lo mismo | Pronóstico de demanda del negocio, primero con una regla ingenua y luego con regresión. Comparación honesta entre ambas | DataCamp: Introduction to Regression with statsmodels |
| 12 | Probabilidad como recurso de focalización. Matriz de confusión traducida a dinero. El umbral como palanca gerencial. Clases desbalanceadas | Focalización con presupuesto limitado. Si solo alcanza para el veinte por ciento de la cartera, a quiénes y por qué | Deber 5: recomendación de focalización con retorno esperado. DataCamp: Supervised Learning with scikit-learn |
| 13 | Segmentación por comportamiento frente a demográfica. Los tres requisitos de un segmento útil: accionable, medible y estable. Qué va con qué | Segmentar la base de clientes, nombrar los segmentos y escribir el mensaje comercial de cada uno. Otro grupo evalúa si permite hacer algo distinto | DataCamp: Unsupervised Learning in Python |
| 14 | Lo que se sale del patrón y lo que no es un número. Clasificación de reseñas y extracción de datos de documentos con modelos generativos. De la métrica al KPI | Procesar el corpus de reseñas del negocio y construir el tablero de KPIs del proyecto | Avance de proyecto: modelo con línea base declarada |
| 15 | Un modelo aprende del pasado y reproduce sus desigualdades. Sesgo, privacidad y decisiones automatizadas sobre personas. Caso de riesgo crediticio | Consultoría entre grupos. Ataque a supuestos, auditoría del modelo propio y ensayo de la defensa | Borrador completo del cuaderno reproducible |
| 16 | Presentaciones finales ante panel. Diez minutos de exposición y diez de preguntas | Presentaciones finales y cierre del curso | Proyecto final: recomendación de una página más cuaderno reproducible |

---

## C. Notas de la reestructuración

**El puente KNIME a Python desaparece como semana.** En el sílabo actual la semana 15 servía de puente hacia Python con el asistente K-AI. Al pasar todo el curso a Python, esa semana se libera y se usa para ética y clínica de proyectos, que antes no tenían espacio propio.

**No hay semana de instalación.** Colab elimina el problema de las instalaciones locales, que en un curso virtual sincrónico consumía la primera semana entera. Eso libera tiempo real para el caso de apertura.

**La IA es transversal, no un tema.** El asistente se usa desde la sesión 1 y para todo. Lo que se califica no es el código sino la calidad del encargo y el rigor de la verificación. En las semanas 4, 8 y 12 se incluye un ejercicio de código generado por IA con un error incrustado, para que el grupo lo encuentre, lo explique y estime el daño que habría causado.

**Los modelos se ordenan por decisión de negocio y no por algoritmo.** La semana 10 es bisagra y no tiene casi código: instala la taxonomía de familias, la línea base obligatoria y la ecuación de valor. Sin esa semana, el bloque se convierte en una competencia por la métrica del modelo y el curso pierde su ventaja frente a un curso de programación.

**Compatibilidad con el sílabo aprobado.** Los nombres de tema principal se mantienen cercanos a los originales para que el cambio se lea como sustitución de herramienta y no como rediseño de curso, lo que simplifica la aprobación en coordinación académica.

**Certificaciones DataCamp.** Los nombres sugeridos deben verificarse contra el catálogo vigente antes de publicarse en D2L, porque las rutas cambian de nombre entre versiones.
