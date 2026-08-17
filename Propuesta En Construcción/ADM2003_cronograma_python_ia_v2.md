# ADM 2003 · Análisis de Datos con IA y Python
## Cronograma de actividades · Versión 2

> Revisión de la versión 1 con cuatro cambios de fondo: regresión partida en dos semanas, semana nueva de estrategia y transformación digital con el customer journey map, eliminación de la semana de anomalías y KPIs, y el análisis RFM convertido en proyecto de medio semestre. El detalle de los cambios está en la sección D.

---

## A. Tabla para el sílabo oficial

| Semana | Tema Principal | Enfoque Técnico (Librerías y Herramientas) |
|---|---|---|
| 1 | Introducción a Business Analytics y Big Data en la era de la IA | Google Colab y cuadernos ejecutables. Protocolo de uso de IAG y bitácora de prompts. Recorrido guiado de un análisis completo |
| 2 | Business Analytics en las organizaciones. La pregunta antes del dato | pandas: lectura de archivos, `read_csv`, `head`, `info`, `shape`. Ficha de análisis y definición de la unidad de análisis |
| 3 | Estadística descriptiva aplicada al negocio | pandas: `describe`, `value_counts`, `quantile`. Media frente a mediana, dispersión y línea base |
| 4 | Anatomía y calidad de los datos | pandas: `dtypes`, `isna`, `duplicated`, `astype`. Granularidad, nulos, duplicados y valores extremos |
| 5 | Manipulación de datos. Agrupar, limpiar y combinar | pandas: `query`, `assign`, `groupby`, `agg`, `merge`, `concat`, `pivot_table`. Dividir, aplicar y recombinar; cardinalidad de las uniones |
| 6 | Visualización de datos | matplotlib y seaborn: línea, barras ordenadas, dispersión, histograma y caja. Reglas de honestidad visual |
| 7 | Visualización avanzada y tableros | Plotly para gráficos interactivos y Streamlit para el tablero. Anotación, título con conclusión y composición |
| 8 | ¿Quiénes son mis clientes y cuánto valen? | pandas: `quantile`, `groupby`, `qcut` para el puntaje RFM+P. `KMeans` con `RobustScaler` como contraste con la segmentación por reglas |
| 9 | Comparación, variabilidad y causalidad | pandas `crosstab` y `scipy.stats`: prueba t, chi cuadrado y ANOVA. Paradoja de Simpson, confusión y diseño de pruebas A y B |
| 10 | Estrategia, transformación digital y experiencia del cliente | Customer journey map y service blueprint. Diagnóstico de madurez digital. Dónde nacen los datos dentro del proceso de negocio |
| 11 | Modelos analíticos. Tipos de modelos y creación de valor | scikit-learn: `train_test_split`, `DummyRegressor` y `DummyClassifier` como línea base obligatoria |
| 12 | Modelos de pronóstico I. Regresión lineal simple | scikit-learn y statsmodels: `LinearRegression`, lectura del coeficiente, `mean_absolute_error` y error porcentual |
| 13 | Modelos de pronóstico II. Regresión múltiple y diagnóstico | statsmodels: múltiple, variables categóricas, `variance_inflation_factor`, residuos y ajuste polinomial |
| 14 | Modelos de propensión. Clasificación aplicada a decisiones | scikit-learn: `LogisticRegression`, `DecisionTreeClassifier`, `confusion_matrix`, umbral y curva de ganancia |
| 15 | De la predicción a la decisión. Ética y gobernanza del dato | Auditoría de sesgo, privacidad y explicabilidad. Clínica de proyectos y revisión cruzada |
| 16 | Cierre del curso y presentación final | Entrega del cuaderno reproducible documentado y defensa del proyecto integrador |

---

## B. Plan de sesiones

Dos sesiones semanales de hora y media, lunes y miércoles. La sesión de lunes es conceptual y demostrativa, con un caso que se discute antes de tocar el teclado. La de miércoles es laboratorio en salas de grupos, con entrega corta al cierre.

| Semana | Lunes (concepto y caso) | Miércoles (laboratorio en grupos) | Entregable y certificación |
|---|---|---|---|
| 1 | Por qué fracasan los análisis. Un informe real con datos correctos y conclusión inválida. La escalera descriptivo, diagnóstico, predictivo y prescriptivo | Colab, primer cuaderno y recorrido de un análisis completo de principio a fin. Firma del protocolo de uso de IAG | DataCamp: Understanding Data Science |
| 2 | Unidad de análisis, métrica, comparación y decisión. Clínica de definiciones ambiguas: qué es un cliente activo, qué cuenta como venta | Carga y primer contacto con la base del curso. Cada grupo redacta la ficha de análisis y otro grupo la ataca | Deber 1: ficha de análisis de una página, sin código |
| 3 | La trampa del promedio. Distribuciones bimodales, mediana frente a media, tamaño de muestra. Caso: dos áreas reportan ventas distintas del mismo mes | Perfilado descriptivo de la base. Doce preguntas descriptivas de dificultad creciente contra reloj | DataCamp: Introduction to Python |
| 4 | Granularidad, tipos de dato y calidad. La diferencia entre ausente, cero y desconocido. Caso: el diez por ciento de transacciones sin identificador de cliente | Inventario de problemas de calidad, cuantificación de cada uno y decisión documentada | Deber 2: bitácora de limpieza. Propuesta de proyecto final |
| 5 | Dividir, aplicar y recombinar. Los cuatro tipos de unión y la cardinalidad. El error que llega a un directorio: una unión que duplica filas e infla la facturación | Torneo de preguntas: cada grupo formula tres preguntas de negocio y otro las responde. Construcción de la tabla mensual de indicadores desde cuatro fuentes, cuadrada contra una cifra de control | Deber 3: tabla de indicadores reproducible. DataCamp: Data Manipulation with pandas y Joining Data with pandas |
| 6 | Explorar, verificar y comunicar. Cuarteto de Anscombe. Repertorio mínimo, ejes, escalas y el título que lleva la conclusión | Clínica de rediseño. Cada grupo toma un gráfico malo publicado y lo rediseña justificando cada cambio | Deber 4: tres gráficos anotados del negocio. DataCamp: Introduction to Data Visualization with Matplotlib |
| 7 | Del gráfico al tablero. Interactividad, jerarquía visual y qué se elimina. Fondo blanco y ausencia de decoración | Construcción del tablero del negocio del proyecto y contestación de una pregunta gerencial con él | Tablero interactivo entregado en el cuaderno |
| 8 | Quién es un cliente valioso. Recencia, frecuencia, monto y margen. Los tres requisitos de un segmento útil: accionable, medible y estable | Segmentar la base, nombrar los segmentos y escribir el mensaje comercial de cada uno. Contraste entre la segmentación por reglas y la que encuentra `KMeans` | **Proyecto de medio semestre: análisis RFM+P con recomendación comercial por segmento.** DataCamp: Unsupervised Learning in Python |
| 9 | Comparado con qué. Ruido frente a señal, regresión a la media, confusión y causalidad inversa. Caso: los clientes del programa de fidelidad gastan el doble | Prueba t, chi cuadrado y ANOVA sobre la base del proyecto. Diseño de una prueba A y B ejecutable, con unidad de asignación, duración y presupuesto | Deber 5: diseño experimental de una página |
| 10 | De la eficiencia al modelo de negocio. Qué es transformación digital y qué es comprar software. Madurez digital y dónde se rompe la experiencia del cliente | Customer journey map y service blueprint del proceso del negocio del proyecto. Marcar en el blueprint dónde se genera cada dato y qué decisión se toma a ciegas | Journey map y blueprint anotados con los puntos de captura de datos |
| 11 | El mapa de los modelos: pronóstico, propensión, segmentación, asociación y optimización. Qué decisión habilita cada uno. La ecuación de valor | Catálogo de doce problemas de negocio. Cada grupo asigna familia, decisión, línea base y valor anual estimado. Se descubre cuáles no justifican ningún modelo | Evaluación intermedia sobre criterio de negocio |
| 12 | Una variable explica otra. Mínimos cuadrados, lectura del coeficiente en unidades del negocio y error de pronóstico asimétrico: quedarse sin producto y que sobre producto no cuestan lo mismo | Pronóstico con una regla ingenua y luego con regresión simple. Comparación honesta entre ambas sobre los datos del proyecto | Deber 6: pronóstico con línea base declarada. DataCamp: Introduction to Regression with statsmodels |
| 13 | Varias variables a la vez. Variables categóricas, multicolinealidad y el factor VIF. Cuándo la curva es razonable y cuándo es trampa. Diagnóstico de residuos | Modelo múltiple del negocio, revisión de supuestos y presentación del resultado en una frase que un gerente pueda accionar | Avance de proyecto: modelo de pronóstico documentado |
| 14 | Probabilidad como recurso de focalización. Matriz de confusión traducida a dinero. El umbral como palanca gerencial. Clases desbalanceadas | Focalización con presupuesto limitado. Si solo alcanza para el veinte por ciento de la cartera, a quiénes y por qué | Deber 7: recomendación de focalización con retorno esperado. DataCamp: Supervised Learning with scikit-learn |
| 15 | Un modelo aprende del pasado y reproduce sus desigualdades. Sesgo, privacidad y decisiones automatizadas sobre personas. Caso de riesgo crediticio | Consultoría entre grupos. Ataque a supuestos, auditoría del modelo propio y ensayo de la defensa | Borrador completo del cuaderno reproducible |
| 16 | Presentaciones finales ante panel. Diez minutos de exposición y diez de preguntas | Presentaciones finales y cierre del curso | Proyecto final: recomendación de una página más cuaderno reproducible |

---

## C. Estructura del semestre

| Bloque | Semanas | Qué se construye |
|---|---|---|
| I · Leer datos | 1 – 5 | De la pregunta de negocio a una tabla limpia y agregada que se puede defender |
| II · Comunicar datos | 6 – 7 | Del gráfico honesto al tablero que contesta una pregunta gerencial |
| **Corte de medio semestre** | **8** | **Proyecto RFM+P: el primer entregable grande, todavía sin machine learning** |
| III · Decidir con datos | 9 – 11 | Comparación, causalidad, estrategia del negocio y criterio para elegir modelo |
| IV · Predecir | 12 – 14 | Pronóstico y propensión, siempre contra una línea base |
| V · Responder por el modelo | 15 – 16 | Ética, gobernanza y defensa del proyecto |

El proyecto RFM de la semana 8 parte el semestre en dos mitades con lógicas distintas. Antes de la semana 8 el curso enseña a leer y comunicar datos, y el grueso del proyecto grande se resuelve con pandas y criterio comercial: quién es un cliente valioso y qué le digo mañana. `KMeans` aparece al final de esa semana como contraste —la máquina encontrando los segmentos que el grupo ya definió a mano—, no como el tema central. Después de la semana 8 aparece la pregunta predictiva, y el bloque de modelos se apoya en que los grupos ya tienen una base limpia, un tablero y una segmentación que defender.

**La semana 11 es bisagra y casi no tiene código.** Instala la taxonomía de familias de modelos, la línea base obligatoria y la ecuación de valor. Sin esa semana, el bloque IV se convierte en una competencia por la métrica del modelo y el curso pierde su ventaja frente a un curso de programación. Las funciones de scikit-learn que declara el sílabo se demuestran ahí en tres celdas y se usan de verdad a partir de la semana 12.

---

## D. Cambios frente a la versión 1

**Regresión ocupa dos semanas (12 y 13).** En la versión 1 la regresión lineal y la múltiple compartían una sola semana, que es donde el curso se atragantaba: no daba tiempo para leer el coeficiente en unidades de negocio y además ver multicolinealidad, VIF, ajuste polinomial y diagnóstico de residuos. La semana 12 se queda en una variable y en el error de pronóstico; la 13 añade varias variables y los supuestos.

**Semana nueva de estrategia y transformación digital (10).** Se ubica justo antes del bloque de modelos y ahí entra el customer journey map. El caso Banco Andino, que en el mapeo de la versión 1 caía en la semana 2 como ejercicio de proceso, pasa a ser el laboratorio de esta semana. El orden es deliberado: el grupo mapea el proceso del negocio y marca dónde nace cada dato y qué decisión se toma hoy a ciegas, y con ese mapa en la mano entra a la semana 11 a decidir qué familia de modelo tiene sentido. Sin ese paso, la elección del modelo se vuelve una preferencia técnica.

**Desaparece la semana de anomalías, datos no estructurados y KPIs.** Era la semana más cargada y la menos conectada con el proyecto: mezclaba detección de anomalías, clasificación de texto con modelos generativos y construcción de un tablero de KPIs. El tablero ya vivía en la semana de visualización avanzada, que ahora es la 7. Lo que se elimina de verdad es la detección de anomalías, el procesamiento de texto libre con modelos generativos y el paso explícito de la métrica al KPI: son la contrapartida de las dos semanas nuevas.

**Las dos semanas de manipulación se funden en una (5).** Es el ajuste que compensa las dos incorporaciones. El plan de la sesión Pandas II del seminario de Python ya trata agrupaciones, limpieza, pivot y combinación como una sola clase de dos horas y media, aunque su cuaderno se quedó en `groupby` y limpieza: las uniones hay que escribirlas. La cardinalidad no se pierde, se dicta el lunes junto con el patrón de dividir, aplicar y recombinar, y el laboratorio del miércoles obliga a cuadrar la tabla de indicadores contra una cifra de control, que es donde el error de la unión duplicada se hace visible. La semana se lleva dos certificaciones de DataCamp por esa razón.

**La semana 9 gana herramienta estadística.** En la versión 1 la comparación era `crosstab` y comparaciones por grupo. Ahora incorpora prueba t, chi cuadrado y ANOVA con `scipy.stats`, porque el seminario de Python aporta esa sesión completa. Es el único cambio que añade contenido sin costar una semana.

**El capítulo de minería de datos se llama ahora "¿Quiénes son mis clientes y cuánto valen?" y se convierte en el proyecto de medio semestre (8).** El nombre anterior nombraba la técnica; el nuevo nombra la pregunta de negocio, que es la línea del resto del cronograma. RFM+P no necesita machine learning: se calcula con `quantile` y `groupby`, lo que permite adelantarlo a la mitad del semestre y usarlo como el primer entregable grande. `KMeans` entra en la misma semana como contraste — la máquina encontrando los segmentos que el grupo ya definió a mano — y no como el tema central.

**Lo que se pierde y conviene tener presente.** Además de la semana eliminada, la fusión de manipulación se lleva por delante `resample` y la lectura desde bases de datos y APIs con `read_sql` y `requests`, que en la versión 1 vivían en la semana 6. Sumado a que la semana de regresión ya no abre con tendencia y estacionalidad, el curso se queda sin series de tiempo. El análisis de canasta de mercado también desaparece: la asociación se sigue nombrando como familia en el mapa de modelos de la semana 11, pero ya no se practica. Y el pitch del proyecto, que en la versión 1 era el entregable de la semana 8, queda absorbido por el proyecto de medio semestre.

**Compatibilidad con el sílabo aprobado.** Once de los dieciséis nombres de tema se mantienen cercanos a los originales. Los cinco que cambian son la fusión de manipulación, la semana de estrategia, el capítulo de segmentación renombrado, y las dos semanas en que se parte la regresión.

**Certificaciones DataCamp.** Ocho certificaciones repartidas en siete semanas: 1, 3, 5 (dos, por ser la semana fusionada), 6, 8, 12 y 14. Los nombres sugeridos deben verificarse contra el catálogo vigente antes de publicarse en D2L, porque las rutas cambian de nombre entre versiones.
