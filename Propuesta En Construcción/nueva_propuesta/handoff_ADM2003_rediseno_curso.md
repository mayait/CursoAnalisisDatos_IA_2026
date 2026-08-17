# Handoff. Rediseño de ADM 2003 Análisis de Datos

**Fecha:** 16 de agosto de 2026
**Para:** agente que continúa el trabajo
**Asunto:** rediseño del curso ADM 2003 Análisis de Datos, migración de KNIME a Python con apoyo de IA

---

## 1. Quién es el usuario y qué está haciendo

Julián Maya es Sub Director Académico y Director de Tecnologías en USFQ Galápagos. Dicta ADM 2003 Análisis de Datos para el Colegio de Administración de Empresas de la USFQ. El curso corre en el primer semestre 2026/2027, NRC 2241, en modalidad virtual sincrónica, lunes y miércoles de 10:00 a 11:20, es decir dos sesiones de ochenta minutos por semana durante dieciséis semanas.

Su sílabo aprobado está construido sobre KNIME. Quiere volver a Python, con la IA generativa como apoyo permanente y no como tema aislado. Pidió pensar la clase desde cero antes de reescribir el cronograma, y el trabajo avanzó en cuatro movimientos que se describen abajo.

---

## 2. Cómo llegó el diseño a donde está

**Movimiento 1. Los cuatro mínimos.** Preguntó cuáles serían las cuatro cosas mínimas que un estudiante de administración debe aprender de analítica aplicada en la era de la IA. La respuesta partió de una premisa que sostiene todo el resto: con modelos de lenguaje capaces de escribir código correcto, la escasez ya no está en la sintaxis sino en saber qué preguntar, cómo verificar y qué decidir. Los cuatro fueron traducir una pregunta de negocio a una estructura de datos, la gramática de la manipulación de datos tabulares, distinguir descripción de predicción y de causalidad, y convertir el análisis en una decisión defendible.

**Movimiento 2. Dos pilares más.** Pidió añadir comunicación con visualizaciones y una introducción a modelos predictivos. Se elevó la visualización a pilar propio y se ubicó el bloque predictivo justo después del pilar de causalidad, que es el que lo mantiene bajo control. Quedaron seis pilares.

**Movimiento 3. El reencuadre del bloque predictivo.** Aclaró que no quiere una clase de machine learning sino el contexto de negocio: qué tipos de modelos existen y cómo generan valor. El bloque se reorganizó por familia de decisión y no por algoritmo. Pronóstico responde cuánto habrá. Propensión responde quién. Segmentación responde cómo se divide el mercado. Asociación responde qué va con qué. Detección de anomalías responde qué se salió del patrón. Optimización responde qué hacer con la predicción. Los modelos generativos entran como familia transversal para datos no estructurados. El corazón conceptual del bloque es la ecuación de valor: el valor de un modelo es la mejora sobre la línea base, por el número de decisiones que toca, por el valor unitario de cada decisión, menos el costo de construirlo y operarlo, con tres condiciones sin las cuales el valor es cero, que la predicción llegue antes de la decisión, que cambie la acción y que la organización pueda ejecutarla.

**Movimiento 4. El cronograma real.** Compartió el sílabo vigente y pidió enfocarse solo en el cronograma. Se produjo la versión en Python, ajustada a las restricciones institucionales reales que antes no estaban a la vista.

---

## 3. Estado actual. Los seis pilares

1. Traducir una pregunta de negocio a una estructura de datos.
2. La gramática de la manipulación de datos tabulares.
3. Distinguir descripción, predicción y causalidad.
4. Tipos de modelos y cómo generan valor en el negocio.
5. Comunicar con visualizaciones.
6. Convertir el análisis en una decisión defendible.

La visualización tiene una semana ancla y después se vuelve estándar de evaluación en todas las entregas, no tema recurrente.

---

## 4. Restricciones institucionales que condicionan el diseño

Evaluación fija en cuatro categorías de veinticinco por ciento cada una: participación, deberes, evaluaciones y certificaciones, y proyecto final. La categoría de certificaciones se cubre con DataCamp usando el correo institucional, lo que obliga a anclar cada curso de DataCamp a la semana donde el contenido coincide.

Políticas del curso que ya están aprobadas: conexión obligatoria desde computadora, cámara encendida, trabajo en salas de grupos, no se aceptan proyectos individuales. El uso de IA generativa está autorizado durante todo el proceso de aprendizaje bajo libertad de cátedra.

Modalidad virtual sincrónica, que hace obligatorio Google Colab y elimina cualquier semana de instalación local.

El sílabo está aprobado por coordinación académica y cualquier cambio debe solicitarse allí. Por eso los nombres de tema principal del cronograma nuevo se mantuvieron deliberadamente cercanos a los originales, para que el cambio se lea como sustitución de herramienta y no como rediseño de curso.

---

## 5. Decisiones de diseño y su razón

**El asistente de IA es condición de trabajo, no tema.** Se usa desde la primera sesión y para todo. Lo que se califica es la calidad del encargo y el rigor de la verificación. Cada entrega incluye bitácora de prompts con lo que se pidió y lo que se corrigió. En las semanas 4, 8 y 12 hay un ejercicio de código generado por IA con un error incrustado, para que el grupo lo encuentre, lo explique y estime el daño que habría causado.

**Línea base obligatoria en toda entrega.** Todo modelo compite contra la regla simple que la organización ya usa. En Python esto se ancla en `DummyRegressor` y `DummyClassifier` de scikit learn, que hacen el concepto tangible.

**Se califica la decisión, no el desempeño del algoritmo.** Es la defensa principal contra el riesgo de que el curso derive en una competencia por la métrica.

**Ritmo semanal fijo.** Lunes conceptual y demostrativo, con un caso que se discute antes de tocar el teclado. Miércoles laboratorio en salas de grupos con entrega corta al cierre.

**Una sola columna vertebral de datos.** Un conjunto real, sucio y del contexto local, de un negocio turístico o gastronómico, que atraviesa las dieciséis semanas, más dos satélites, uno de cartera de crédito y uno de reseñas en texto libre.

**Lo que quedó fuera a propósito.** Redes neuronales, ajuste de hiperparámetros, dinámica de competencia tipo Kaggle, estadística inferencial formal y memorización de sintaxis.

---

## 6. Entregables ya producidos

`plan_clase_analitica_administracion_16_semanas.md`. Diseño pedagógico completo con los seis pilares, subtemas, casos, actividades grupales, problemas y puntos teóricos. Es el documento de fondo, no el sílabo.

`ADM2003_cronograma_python_ia.md`. Dos tablas. La primera replica el formato de tres columnas del cronograma aprobado y es la que se pega en el sílabo. La segunda es el plan de sesiones lunes y miércoles con entregables y certificaciones. Incluye notas de la reestructuración.

`ADM2003_syllabus_original_knime.md`. El sílabo vigente transcrito, con el cronograma KNIME original, para referencia y comparación.

---

## 7. Pendientes

Verificar los nombres de los cursos de DataCamp contra el catálogo vigente antes de publicarlos en D2L, porque las rutas se renombran entre versiones. Los nombres sugeridos se escribieron de memoria y no están confirmados.

Asegurar y perfilar la base de datos de la columna vertebral antes de que empiece el semestre. El curso entero depende de que exista y esté disponible desde la semana tres. Si se rompe a mitad de semestre el diseño obliga a improvisar.

Definir si el tablero de la semana 8 se queda en cuaderno con Plotly o escala a Streamlit, considerando que la clase es virtual y los estudiantes no instalan nada localmente.

Tramitar en coordinación académica el cambio de cronograma.

Falta redactar los materiales de aula: los doce problemas del catálogo de la semana 10, los casos de apertura de cada semana, las rúbricas de las cuatro entregas parciales y del proyecto final, y los tres ejercicios de código con error incrustado.

---

## 8. Cómo trabajar con él

Escribe y espera respuestas en español. Prefiere prosa humana y directa, sin listas largas, sin emojis y sin tono de IA. No usa el guion largo en los textos que le entregan y evita el uso excesivo del punto y coma.

No quiere frases de apertura tipo "aquí tienes" ni sugerencias o próximos pasos al final de la respuesta. Quiere el resultado final, listo para copiar y pegar.

Todo entregable visual va con fondo blanco, incluidos gráficos, mapas de calor y diagramas.

Valora salidas estructuradas y modulares, con formatos explícitos, convenciones de nombres y plantillas que se conecten directo con su flujo de trabajo. Suele pedir que el asistente adopte un rol experto específico.

Recibe bien el desacuerdo argumentado. En esta conversación pidió expresamente seguir una recomendación que iba en contra de su primera intuición sobre el peso del bloque de modelos, así que conviene señalar los costos de cada decisión en lugar de solo ejecutar.
