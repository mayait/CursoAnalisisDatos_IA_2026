# -*- coding: utf-8 -*-
"""Contenido docente de Análisis de Datos con IA y Python · ADM 2003 · USFQ.

Una entrada por semana. El generador del sitio (generar_sitio.py) lee esto y no
inventa nada: si un campo está vacío, la página lo dice.

Campos:
  intro        párrafo de apertura, en segunda persona
  objetivos    qué sabe hacer el estudiante al terminar
  contenidos   [(título, explicación)] en el orden en que se dictan
  trampa       el error que la gente comete y que la semana existe para evitar
  practica     pasos verificables del laboratorio
  proyecto     qué avanza el grupo en su caso
  ia           cómo se usa el asistente esta semana y qué se verifica
  datasets     [(nombre, url)]
  lecturas     [(título, url, por qué)]
"""

SEMANAS = {

1: dict(
 intro="El curso abre con un informe real que tiene los datos correctos y la conclusión equivocada. No vas a aprender a programar: vas a aprender a decidir con datos y a encargarle trabajo a un asistente de IA sin quedar a merced de lo que te responda.",
 objetivos=[
  "Distinguir los cuatro niveles de la analítica: descriptivo, diagnóstico, predictivo y prescriptivo.",
  "Ejecutar un cuaderno completo en Google Colab sin instalar nada.",
  "Explicar por qué un análisis con datos correctos puede llevar a una decisión equivocada.",
  "Aplicar el protocolo de uso de IA generativa del curso y abrir tu bitácora de prompts.",
 ],
 contenidos=[
  ("Qué es Business Analytics y qué no","La diferencia entre reportar lo que pasó y habilitar una decisión. Big data como problema de infraestructura, no de análisis."),
  ("La escalera de la analítica","Descriptivo, diagnóstico, predictivo y prescriptivo, con un ejemplo de negocio en cada peldaño y el costo de saltarse uno."),
  ("Cómo se rompe un análisis","Anatomía del informe de apertura: la muestra mal elegida, la comparación ausente y la métrica que nadie definió."),
  ("Colab y el cuaderno ejecutable","Celdas de texto y de código, orden de ejecución, sesión y reinicio. Por qué un cuaderno que no corre de arriba a abajo no vale."),
  ("Protocolo de uso de IA generativa","Qué se puede pedir, qué hay que verificar y qué se registra. La bitácora de prompts es parte de cada entrega."),
 ],
 trampa="Creer que el problema del análisis es la herramienta. El informe de apertura se hizo con software correcto y datos correctos.",
 practica=[
  "Abrir el cuaderno de la sesión en Colab y ejecutarlo completo hasta ver el gráfico final.",
  "Recorrer un análisis ya escrito e identificar en qué celda se toma la decisión que cambia la conclusión.",
  "Escribir tres prompts al asistente para la misma pregunta y comparar cuál produce un resultado verificable.",
 ],
 proyecto="Formación de equipos, firma del contrato de grupo y apertura del repositorio compartido con la bitácora de prompts.",
 ia="El asistente se usa desde hoy y para todo. Lo que se califica no es el código que devuelve sino la calidad del encargo y el rigor de la verificación: cada cuaderno entregado incluye el prompt final y una línea sobre qué se comprobó del resultado.",
 datasets=[],
 lecturas=[("Fundamentos de IA · USFQ","../Material Actual/Actividades Organizadas/99_Lecturas_y_Material_de_Apoyo/Fundamentos_IA_USFQ V1.pdf","Marco común sobre qué es y qué no es la IA generativa antes de firmar el protocolo del curso.")],
),

2: dict(
 intro="Antes del dato está la pregunta. La mitad de los análisis que fracasan lo hacen porque nadie definió qué es un cliente activo, qué cuenta como venta o cuál es la fila de la tabla.",
 objetivos=[
  "Definir la unidad de análisis de un problema de negocio y justificarla.",
  "Cargar datos desde CSV y Excel con pandas y auditarlos con cuatro métodos.",
  "Redactar una ficha de análisis que otro grupo pueda atacar.",
  "Distinguir una pregunta de negocio de una petición de reporte.",
 ],
 contenidos=[
  ("Unidad de análisis, métrica, comparación y decisión","Las cuatro preguntas que hay que contestar antes de abrir un archivo. Si falta la comparación, no hay análisis."),
  ("Clínica de definiciones ambiguas","Qué es un cliente activo, qué cuenta como venta, cuándo empieza un pedido. Cada definición cambia el número que llega al directorio."),
  ("Lectura de archivos con pandas","`read_csv` y `read_excel` con separador, codificación, fechas y columnas. Qué hacer cuando el archivo llega sucio de origen."),
  ("Primer contacto con una tabla","`head`, `info`, `shape` y `sample`. Los cinco minutos que se le dedican a un dataset nuevo antes de cualquier otra cosa."),
  ("La ficha de análisis","Pregunta, unidad, métrica, comparación, decisión y limitaciones conocidas. Una página, sin código."),
 ],
 trampa="Empezar a programar antes de poder decir en una frase qué decisión cambia según el resultado.",
 practica=[
  "Cargar la base del curso con los parámetros correctos de separador, codificación y fechas.",
  "Auditarla con `shape`, `info`, `head` y `describe` y anotar tres observaciones iniciales.",
  "Redactar la ficha de análisis del proyecto del grupo y entregarla a otro grupo para que la ataque.",
 ],
 proyecto="Cada grupo elige la empresa de su proyecto integrador y redacta la ficha de análisis de su caso.",
 ia="Pídele al asistente que critique tu ficha de análisis como si fuera el gerente que va a recibir el resultado. Registra su respuesta y anota cuáles de sus objeciones aceptaste y cuáles no.",
 datasets=[],
 lecturas=[("¿Qué es el análisis exploratorio de datos?","https://www.ibm.com/think/topics/exploratory-data-analysis","Marco conceptual sobre por qué la carga y la inspección son el primer paso de cualquier análisis empresarial.")],
),

3: dict(
 intro="El promedio es la estadística más usada y la que más decisiones arruina. Esta semana aprendes a describir un negocio con números que no mientan.",
 objetivos=[
  "Elegir entre media y mediana según la forma de la distribución.",
  "Leer una distribución con `describe`, `quantile` y `value_counts`.",
  "Cuantificar la dispersión y explicar por qué importa tanto como el centro.",
  "Establecer la línea base descriptiva contra la que se comparará todo lo demás.",
 ],
 contenidos=[
  ("La trampa del promedio","Distribuciones bimodales, colas largas y el ticket promedio que no le corresponde a ningún cliente real."),
  ("Medidas de centro y de dispersión","Media, mediana y moda. Desviación estándar, rango intercuartílico y coeficiente de variación."),
  ("Percentiles y su lectura de negocio","Qué significa que el 75 % de las ventas esté por debajo de Q3 y qué decisión habilita."),
  ("Frecuencias y categorías","`value_counts` con y sin normalizar. La categoría Otros y cuándo esconde el hallazgo."),
  ("Tamaño de muestra","Por qué un promedio sobre doce observaciones no es un promedio."),
 ],
 trampa="Reportar la media de una distribución con cola larga. Es el error que hace que dos áreas reporten ventas distintas del mismo mes.",
 practica=[
  "Perfilado descriptivo completo de la base del curso con `describe(include='all')`.",
  "Doce preguntas descriptivas de dificultad creciente contra reloj, en equipos.",
  "Para cada respuesta, decidir si el estadístico correcto es la media o la mediana y justificarlo con la forma de la distribución.",
 ],
 proyecto="Perfilado descriptivo del dataset del caso y primeras tres observaciones que un gerente podría accionar.",
 ia="Genera con el asistente las doce preguntas descriptivas sobre tu propio dataset, y luego verifica una por una que la respuesta que te dio coincide con lo que devuelve pandas. Al menos una no va a coincidir.",
 datasets=[("Banco de preguntas descriptivas (material de apoyo del docente)","../Material Actual/Actividades Organizadas/02_Primer_Contacto_con_Datos_y_EDA/2025_Taller_02_Ejercicio_Analisis_Individual_Pizza_Sales/adjuntos/EDA_Pizza_BancoPreguntas.docx")],
 lecturas=[],
),

4: dict(
 intro="Los datos reales llegan rotos. Esta semana aprendes a cuantificar cuán rotos están y a documentar cada decisión de limpieza, porque una limpieza sin bitácora no es reproducible.",
 objetivos=[
  "Diagnosticar la calidad de un dataset con métricas, no con impresiones.",
  "Distinguir ausente, cero y desconocido, y tratarlos de forma distinta.",
  "Detectar y decidir qué hacer con duplicados y valores extremos.",
  "Escribir una bitácora de limpieza que otra persona pueda auditar.",
 ],
 contenidos=[
  ("Granularidad y unidad de la fila","Qué representa una fila. El error de sumar una columna que ya viene agregada."),
  ("Tipos de dato","`dtypes` y `astype`. La fecha que llegó como texto y el identificador que llegó como número."),
  ("Nulos","`isna` y su conteo por columna. La diferencia entre no lo sabemos, no aplica y es cero."),
  ("Duplicados","`duplicated` con y sin subconjunto de columnas. Duplicado exacto frente a duplicado de negocio."),
  ("Valores extremos","Detección con rango intercuartílico. Cuándo un extremo es un error y cuándo es el cliente más importante."),
 ],
 trampa="Rellenar los nulos con cero por defecto. Un cliente sin identificador no compró cero: no sabemos quién es.",
 practica=[
  "Inventario de problemas de calidad de la base, con el porcentaje exacto que afecta cada uno.",
  "Decidir el tratamiento de cada problema y escribir la justificación en una línea.",
  "Producir la tabla limpia y demostrar con una cifra de control que no se perdió información por el camino.",
 ],
 proyecto="Bitácora de limpieza del dataset del caso y propuesta formal del proyecto final, con el diagnóstico de madurez analítica de la empresa elegida.",
 ia="Ejercicio de código con error incrustado: el docente entrega un fragmento de limpieza generado por IA que contiene un fallo silencioso. El grupo lo encuentra, lo explica y estima cuánto habría costado si llegaba a un informe.",
 datasets=[],
 lecturas=[],
),

5: dict(
 intro="Semana de doble carga y la más técnica del primer bloque. Agrupar y combinar son las dos operaciones que convierten tablas sueltas en un indicador de negocio, y también donde se cometen los errores más caros.",
 objetivos=[
  "Aplicar el patrón dividir, aplicar y recombinar con `groupby` y `agg`.",
  "Elegir el tipo de unión correcto y anticipar su cardinalidad.",
  "Construir una tabla de indicadores desde varias fuentes con granularidades distintas.",
  "Verificar un resultado agregado contra una cifra de control externa.",
 ],
 contenidos=[
  ("Filtrar y derivar","`query` y `assign`. Columnas calculadas vectorizadas en lugar de bucles."),
  ("Dividir, aplicar y recombinar","`groupby` con una y con varias claves. Agregaciones múltiples y renombrado de columnas."),
  ("Pérdida de información al agregar","Sube el ticket promedio y caen las transacciones. Qué pregunta contesta cada nivel de agregación."),
  ("Los cuatro tipos de unión","Interna, izquierda, derecha y externa, con el diagrama y el caso de negocio de cada una."),
  ("Cardinalidad","Uno a uno, uno a muchos y muchos a muchos. La unión que duplica filas e infla la facturación."),
  ("Reestructuración","`pivot_table` y `concat` para pasar de formato largo a ancho y consolidar periodos."),
 ],
 trampa="Unir dos tablas sin verificar el número de filas antes y después. Es el error que llega a un directorio convertido en una cifra de ventas inflada.",
 practica=[
  "Torneo de preguntas: cada grupo formula tres preguntas de negocio y otro las responde con `groupby` en quince minutos.",
  "Construir la tabla mensual de indicadores desde cuatro fuentes con granularidades distintas.",
  "Cuadrar el total contra una cifra de control y explicar cualquier diferencia.",
 ],
 proyecto="Tabla de indicadores del negocio del caso, reproducible y cuadrada.",
 ia="Pídele al asistente la unión de dos tablas y exígete a ti mismo comprobar tres cosas antes de aceptarla: filas antes, filas después y suma de la columna de control. Documenta las tres en el cuaderno.",
 datasets=[],
 lecturas=[("Comparación de pandas con SQL","https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sql.html","Si ya sabes SQL, esta tabla traduce cada join a su equivalente en pandas.")],
),

6: dict(
 intro="Un gráfico no es un adorno del análisis: es el análisis. Esta semana aprendes el repertorio mínimo y las reglas para no mentir con él, ni siquiera sin querer.",
 objetivos=[
  "Elegir el gráfico correcto según el tipo de variable y la pregunta.",
  "Construir línea, barras ordenadas, dispersión, histograma y caja con matplotlib y seaborn.",
  "Detectar y corregir las distorsiones visuales más frecuentes.",
  "Escribir un título que lleve la conclusión en lugar de nombrar el eje.",
 ],
 contenidos=[
  ("Explorar, verificar y comunicar","Los tres usos del gráfico. El de comunicar es el único que se muestra."),
  ("Cuarteto de Anscombe","Cuatro conjuntos con la misma media, varianza y correlación, y cuatro formas distintas."),
  ("Repertorio mínimo","Línea para el tiempo, barras ordenadas para comparar categorías, dispersión para relación, histograma y caja para distribución."),
  ("Honestidad visual","El eje truncado, la escala doble, el gráfico de pastel con doce categorías y el 3D decorativo."),
  ("El título que concluye","De Ventas por región a Tres regiones concentran el 80 % de la caída."),
 ],
 trampa="Empezar el eje vertical en un valor distinto de cero en un gráfico de barras. Duplica visualmente una diferencia del 3 %.",
 practica=[
  "Reproducir el cuarteto de Anscombe y comprobar que los estadísticos coinciden y las formas no.",
  "Clínica de rediseño: primero se empeora una figura del cuaderno a propósito para nombrar cada distorsión, y después se rehace bien justificando cada cambio.",
  "Producir tres gráficos anotados del negocio del proyecto, cada uno con su título-conclusión.",
 ],
 proyecto="Tres gráficos del caso con la conclusión escrita en el título y la fuente citada al pie.",
 ia="Genera el gráfico con el asistente y luego pídele que argumente en contra de tu propia conclusión usando el mismo gráfico. Si lo logra, la figura no está diciendo lo que crees.",
 datasets=[("Ejercicio 2.1 · Knaflic","../Material Actual/Actividades Organizadas/04_Visualizacion_de_Datos/2024_Data_visualization_I/adjuntos/2.1 EXERCISE.xlsx"),
           ("Ejercicio 2.2 · Knaflic","../Material Actual/Actividades Organizadas/04_Visualizacion_de_Datos/2024_Data_visualization_III/adjuntos/2.2 EXERCISE.xlsx"),
           ("Ejercicio 2.4 · Knaflic","../Material Actual/Actividades Organizadas/04_Visualizacion_de_Datos/2024_Data_visualization_II/adjuntos/2.4 EXERCISE.xlsx")],
 lecturas=[("Storytelling con datos · Cole Nussbaumer Knaflic","../Material Actual/Actividades Organizadas/99_Lecturas_y_Material_de_Apoyo/CONTEXTO - Storytelling con datos - Cole Nussbaumer Knaflic (1).pdf","Lectura previa obligatoria del lunes. De aquí salen los tres ejercicios del laboratorio.")],
),

7: dict(
 intro="Del gráfico suelto al tablero que contesta una pregunta gerencial. Aquí es donde el análisis deja de ser un cuaderno y empieza a ser un producto que alguien más puede usar.",
 objetivos=[
  "Construir gráficos interactivos con Plotly dentro del cuaderno.",
  "Componer un tablero con jerarquía visual y sin decoración.",
  "Decidir qué se elimina de un tablero, que es más difícil que decidir qué se pone.",
  "Contar un estado de resultados a una audiencia no financiera.",
 ],
 contenidos=[
  ("Qué agrega la interactividad y qué estorba","Filtro, detalle bajo demanda y zoom. Cuándo la interactividad es una excusa para no decidir el mensaje."),
  ("Plotly en el cuaderno","Figuras interactivas, anotaciones y exportación. Cascada para un estado de resultados."),
  ("Anatomía de un tablero","Una pregunta por tablero. La cifra principal arriba a la izquierda, el detalle abajo, el contexto al lado."),
  ("Streamlit como siguiente paso","Cómo el mismo cuaderno se convierte en una aplicación que el gerente abre sin pedirte permiso."),
  ("Qué se elimina","Fondo blanco, sin sombras, sin bordes, sin logotipos repetidos, sin leyendas redundantes."),
 ],
 trampa="Construir el tablero antes de escribir la pregunta que debe contestar. Se reconoce porque tiene siete filtros y ninguna conclusión.",
 practica=[
  "Convertir el estado de resultados de la sesión en una cascada interactiva legible por alguien sin formación financiera.",
  "Construir el tablero del negocio del proyecto alrededor de una sola pregunta gerencial.",
  "Presentarlo en tres minutos y recibir fuego cruzado del resto de grupos.",
  "Ensayo de RFM sin nota: calcular recencia, frecuencia y monto de la base en veinte minutos, sin nombrar segmentos todavía. Es el primer intento de lo que la semana 8 evalúa.",
 ],
 proyecto="Tablero interactivo del caso, entregado dentro del cuaderno, que contesta una pregunta gerencial explícita.",
 ia="Describe tu tablero al asistente sin mostrarle el código y pídele que te diga qué pregunta cree que contesta. Si no acierta, el tablero no comunica.",
 datasets=[],
 lecturas=[],
),

8: dict(
 intro="Corte de medio semestre. Todo lo aprendido hasta aquí se junta en un entregable grande: segmentar a los clientes de un negocio y escribir qué se le dice mañana a cada segmento. Sin machine learning todavía, con criterio comercial.",
 objetivos=[
  "Calcular recencia, frecuencia, monto y margen por cliente.",
  "Construir un puntaje RFM+P con `qcut` y traducirlo a segmentos con nombre.",
  "Evaluar si un segmento cumple los tres requisitos: accionable, medible y estable.",
  "Contrastar la segmentación por reglas con la que encuentra un algoritmo de agrupamiento.",
 ],
 contenidos=[
  ("Quién es un cliente valioso","Por qué el que más compra no siempre es el que más deja. La P de margen que casi nadie calcula."),
  ("Recencia, frecuencia y monto","Las tres dimensiones clásicas del retail, su cálculo y sus trampas: devoluciones, clientes sin identificar y cantidades negativas."),
  ("Del puntaje al segmento","Quintiles con `qcut`, matriz RFM y nombres que un gerente comercial entienda: VIP, leal, en riesgo, perdido."),
  ("Los tres requisitos de un segmento útil","Accionable, medible y estable. Un segmento que no cambia ninguna acción no es un segmento."),
  ("KMeans como contraste","La máquina encuentra los grupos que tú definiste a mano. Escalador robusto, método del codo y coeficiente de silueta. Qué gana y qué pierde frente a las reglas."),
 ],
 trampa="Nombrar los segmentos con letras o números. Si el segmento se llama Cluster 3, nadie en comercial va a hacer nada con él.",
 practica=[
  "Calcular RFM+P por cliente sobre la base del curso, resolviendo antes las devoluciones y los clientes sin identificar.",
  "Segmentar por quintiles, nombrar cada segmento y escribir su mensaje comercial en una frase.",
  "Correr KMeans sobre las mismas variables escaladas y comparar los grupos con los que definiste a mano.",
 ],
 proyecto="Proyecto de medio semestre: análisis RFM+P completo con recomendación comercial por segmento. Se presenta el 7 de octubre y se cierra durante el receso.",
 ia="El cuaderno debe incluir el prompt final que usaste con el asistente. No se permite pegar código sin entenderlo: en la defensa se pregunta por qué se eligió ese número de segmentos y hay que responder sin leer.",
 datasets=[("SuperStore · cuaderno RFM+P de 202410 (referencia del docente)","https://colab.research.google.com/github/mayait/ClaseAnalisisDatos/blob/main/RFM_SuperStore_Analisis_de_Datos.ipynb")],
 lecturas=[],
),

9: dict(
 intro="Comparado con qué. Esta es la pregunta que separa un dato de un hallazgo, y la semana donde se aprende a no confundir una coincidencia con una causa.",
 objetivos=[
  "Formular una hipótesis contrastable a partir de una pregunta de negocio.",
  "Aplicar prueba t, chi cuadrado y ANOVA según el tipo de variable.",
  "Distinguir significancia estadística de relevancia para el negocio.",
  "Diseñar una prueba A y B ejecutable con los recursos reales de la empresa.",
 ],
 contenidos=[
  ("Ruido frente a señal","Variación natural, regresión a la media y el hallazgo que desaparece al mes siguiente."),
  ("Variables de confusión y causalidad inversa","Los clientes del programa de fidelidad gastan el doble. ¿El programa los hizo gastar o los que gastaban se inscribieron?"),
  ("Paradoja de Simpson","La tendencia que se invierte al abrir por grupo, con un caso de negocio."),
  ("Las tres pruebas de uso diario","Prueba t para comparar dos grupos, chi cuadrado para variables categóricas, ANOVA para tres o más grupos."),
  ("Tamaño del efecto","Más allá del p-valor: cuánto cambia el número que le importa al negocio."),
  ("Diseño de una prueba A y B","Unidad de asignación, tamaño mínimo, duración, métrica primaria y criterio de parada."),
 ],
 trampa="Declarar un hallazgo porque el p-valor bajó de 0.05 sin mirar cuánto cambia la cifra de negocio. Con suficientes datos, todo es significativo.",
 practica=[
  "Aplicar las tres pruebas sobre la base del proyecto y traducir cada resultado a una frase de negocio.",
  "Encontrar en los datos un caso de paradoja de Simpson y explicarlo.",
  "Diseñar la prueba A y B del negocio del caso, con presupuesto y duración realistas.",
 ],
 proyecto="Diseño experimental de una página para el negocio del caso. Devolución del proyecto de medio semestre.",
 ia="Pídele al asistente que enumere todas las variables de confusión posibles de tu hipótesis. Descarta las que no apliquen y explica por escrito por qué; las que queden van en las limitaciones del proyecto.",
 datasets=[],
 lecturas=[],
),

10: dict(
 intro="Semana bisagra en clave de negocio. Antes de elegir un modelo hay que entender dónde nacen los datos dentro del proceso y qué decisiones se están tomando hoy a ciegas. Se hace con lápiz y papel antes que con código.",
 objetivos=[
  "Distinguir transformación digital de digitalización y de compra de software.",
  "Evaluar la madurez analítica de una organización con un marco explícito.",
  "Construir un customer journey map y un service blueprint de un proceso real.",
  "Ubicar sobre el blueprint los puntos de captura de datos y las decisiones sin evidencia.",
 ],
 contenidos=[
  ("De la eficiencia al modelo de negocio","Los tres niveles de la transformación digital: hacer lo mismo más rápido, hacerlo distinto, y vender otra cosa."),
  ("Madurez analítica","Dónde está la empresa: reportes manuales, tableros, modelos aislados o decisiones automatizadas. Autodiagnóstico con pymedigital.ec."),
  ("Customer journey map","Etapas de descubrimiento, consideración, compra, retención y recomendación. Emociones y puntos de dolor en cada una."),
  ("Service blueprint","Lo que ve el cliente, lo que hace el personal de contacto, lo que ocurre atrás y los sistemas que lo sostienen."),
  ("Dónde nacen los datos","Sobre el blueprint terminado se marca cada punto de captura, cada dato que se pierde y cada decisión que hoy se toma sin evidencia."),
 ],
 trampa="Confundir tener un tablero con haberse transformado. El tablero que nadie abre es un costo, no una capacidad.",
 practica=[
  "Mapear el journey del proceso central del negocio del caso, con etapas, emociones y puntos de dolor.",
  "Convertirlo en service blueprint con las cuatro capas.",
  "Marcar sobre el blueprint los puntos de captura de datos y las decisiones que hoy se toman a ciegas.",
 ],
 proyecto="Journey map y blueprint del caso, anotados con puntos de captura de datos. Es el insumo directo del catálogo de problemas de la semana 11.",
 ia="Usa el asistente para generar el journey map de un cliente tipo y luego contrástalo con lo que te diga una persona real del negocio. Anota las tres diferencias más grandes: ahí está el valor de la semana.",
 datasets=[],
 lecturas=[("Caso Banco Andino · Service Blueprint","https://julianmaya.notion.site/Service-Blue-Print-Caso-Banco-Andino-10b1bce9823f80b2a6bfc427fb9eba06","El caso que se resuelve en el laboratorio: la apertura de cuenta en línea que Juan Pérez no logra terminar.")],
),

11: dict(
 intro="Semana comprimida en una sola sesión de noventa minutos por el feriado del lunes. Es la bisagra del curso y casi no tiene código: instala la taxonomía de modelos, la línea base obligatoria y la ecuación de valor.",
 objetivos=[
  "Clasificar un problema de negocio en su familia de modelo.",
  "Nombrar la decisión concreta que cada familia habilita.",
  "Definir la línea base contra la que se juzgará cualquier modelo.",
  "Estimar el valor anual de resolver un problema antes de intentar resolverlo.",
 ],
 contenidos=[
  ("El mapa de los modelos","Pronóstico, propensión, segmentación, asociación y optimización. Qué decisión habilita cada familia y cuál no hace falta casi nunca."),
  ("La línea base obligatoria","`DummyRegressor` y `DummyClassifier`. Si el modelo no le gana a la regla ingenua, el modelo no existe."),
  ("La separación de datos","`train_test_split` y por qué el conjunto de prueba se aparta antes de tocar nada."),
  ("La ecuación de valor","Decisiones al año, por mejora esperada, por valor unitario, menos el costo de construir y mantener. Cuándo el resultado es negativo."),
  ("Elegir la métrica según la decisión","La métrica no se elige por costumbre: se deduce de qué error cuesta más caro."),
 ],
 trampa="Elegir el algoritmo antes que la decisión. Se reconoce cuando alguien dice quiero aplicar redes neuronales sin poder decir qué se hará distinto con el resultado.",
 practica=[
  "Catálogo de doce problemas de negocio: cada grupo asigna familia, decisión, línea base y valor anual estimado.",
  "Identificar cuáles de los doce no justifican ningún modelo y explicar por qué.",
  "Aplicar el mismo análisis al problema del proyecto propio.",
 ],
 proyecto="Evaluación intermedia sobre criterio de negocio: el problema del caso clasificado, con línea base y valor anual estimado.",
 ia="El asistente es bueno proponiendo algoritmos y malo diciendo que no hace falta ninguno. Pídele que resuelva tres de los doce problemas del catálogo y cuenta cuántas veces propone un modelo donde bastaba una regla.",
 datasets=[],
 lecturas=[("Harvard · Data-Driven Management of Blue Detergent","../Material Actual/Actividades Organizadas/09_Casos_y_Procesos_de_Negocio/2024_Harvard_Case_Data_Driven_Management_of_Blue_Detergent/adjuntos/HBP_DataAnalytics_case_generic (2).pdf","Lectura previa. El caso se resuelve en clase y alimenta el catálogo de problemas.")],
),

12: dict(
 intro="El primer modelo del curso. Una variable explica otra, y el coeficiente se lee en unidades del negocio, no en unidades de estadística.",
 objetivos=[
  "Ajustar una regresión lineal simple con scikit-learn y con statsmodels.",
  "Interpretar el coeficiente y el intercepto en el lenguaje del negocio.",
  "Comparar el modelo contra una línea base y cuantificar cuánto mejora.",
  "Leer el error de pronóstico entendiendo que sus dos lados no cuestan lo mismo.",
 ],
 contenidos=[
  ("De la correlación al modelo","Qué agrega ajustar una recta sobre lo que ya decía el gráfico de dispersión."),
  ("Mínimos cuadrados","Qué se está minimizando exactamente y por qué se elevan al cuadrado los residuos."),
  ("Lectura del coeficiente","Si el coeficiente de inversión en TV es 0.047, cada mil dólares adicionales mueven las ventas en tanto. Esa es la frase que va al informe."),
  ("R² y sus límites","Qué mide, qué no mide y por qué no sirve para decidir si el modelo se usa."),
  ("Error de pronóstico","Error absoluto medio y error porcentual. Quedarse sin producto y que sobre producto no cuestan lo mismo."),
  ("La línea base","`DummyRegressor` con la media. El modelo se reporta siempre junto a ella."),
 ],
 trampa="Reportar el R² como si fuera la calidad del modelo. Un R² alto con un error porcentual del 40 % no sirve para planificar inventario.",
 practica=[
  "Ajustar el modelo simple sobre Advertising y leer el coeficiente en dólares.",
  "Repetir con otra variable predictora y comparar cuál explica más por sí sola.",
  "Pronosticar la demanda del negocio del proyecto primero con una regla ingenua y luego con la regresión, y comparar honestamente.",
 ],
 proyecto="Pronóstico del negocio del caso con línea base declarada y error expresado en unidades de negocio.",
 ia="Pídele al asistente que interprete tu coeficiente. Casi siempre devuelve la interpretación estadística; reescríbela tú en términos de la decisión que se va a tomar y deja las dos versiones en el cuaderno.",
 datasets=[("Advertising.csv","https://raw.githubusercontent.com/justmarkham/scikit-learn-videos/master/data/Advertising.csv")],
 lecturas=[],
),

13: dict(
 intro="Varias variables a la vez. Aquí aparecen los problemas que no existen con una sola: predictores que se pisan entre ellos, curvas que parecen mejorar y residuos que delatan un modelo mal especificado.",
 objetivos=[
  "Ajustar y leer una regresión múltiple con variables numéricas y categóricas.",
  "Detectar multicolinealidad con el factor de inflación de la varianza.",
  "Distinguir un ajuste polinomial razonable de un sobreajuste.",
  "Diagnosticar los cuatro supuestos del método de mínimos cuadrados con los residuos.",
 ],
 contenidos=[
  ("Regresión múltiple","Varios predictores a la vez y el significado de manteniendo todo lo demás constante."),
  ("Variables categóricas","Codificación con variables indicadoras y la categoría de referencia."),
  ("El R² siempre sube","Por qué añadir variables nunca baja el R² de entrenamiento y qué mirar en su lugar."),
  ("Multicolinealidad y VIF","Síntomas, cálculo e interpretación por tramos. Qué hacer cuando el VIF supera 10."),
  ("Ajuste polinomial","Cuándo la curva es razonable, cuándo es sospechosa y cuándo es trampa pura. El grado 10 que hunde la validación."),
  ("Diagnóstico de residuos","Linealidad, independencia, normalidad y homocedasticidad, cada una con su gráfico."),
 ],
 trampa="Meter todas las variables disponibles porque el R² sube. El modelo queda inestable y los coeficientes cambian de signo con cualquier dato nuevo.",
 practica=[
  "Ajustar el modelo múltiple, calcular el VIF de cada predictor y decidir cuáles se quedan.",
  "Comparar lineal, cuadrático y grado alto por validación cruzada y ver dónde se rompe.",
  "Revisar los cuatro gráficos de residuos y declarar qué supuesto no se cumple.",
 ],
 proyecto="Modelo de pronóstico del caso documentado: variables, supuestos revisados y una frase accionable para el gerente.",
 ia="Pídele al asistente el modelo con todas las variables y luego oblígalo a justificar cada predictor. Elimina los que no sobrevivan al argumento y compara el error de los dos modelos.",
 datasets=[("Advertising.csv","https://raw.githubusercontent.com/justmarkham/scikit-learn-videos/master/data/Advertising.csv")],
 lecturas=[],
),

14: dict(
 intro="De predecir un número a estimar una probabilidad. La clasificación no sirve para acertar: sirve para ordenar la cartera y decidir a quién llamar primero con el presupuesto que hay.",
 objetivos=[
  "Ajustar una regresión logística y un árbol de decisión y compararlos.",
  "Leer una matriz de confusión traducida a dinero.",
  "Mover el umbral de decisión según el costo relativo de cada tipo de error.",
  "Producir una recomendación de focalización con retorno esperado.",
 ],
 contenidos=[
  ("Probabilidad en lugar de etiqueta","Por qué el modelo devuelve un número entre cero y uno y qué se hace con él."),
  ("Regresión logística","La sigmoide, los log-odds y la interpretación del coeficiente como cambio en la probabilidad."),
  ("Árbol de decisión","Ramificación, criterio de división, poda y la lectura del árbol como reglas de negocio."),
  ("Matriz de confusión en dinero","Falso positivo y falso negativo tienen precios distintos. Poner el precio antes de elegir la métrica."),
  ("El umbral como palanca gerencial","Mover el corte cambia a quién se llama. No es un detalle técnico, es una decisión de negocio."),
  ("Clases desbalanceadas","Por qué la exactitud engaña cuando solo el 2 % abandona, y qué mirar en su lugar."),
  ("Curva de ganancia","Si solo alcanza para el 20 % de la cartera, cuánto se captura y cuánto se pierde."),
 ],
 trampa="Optimizar la exactitud en un problema desbalanceado. Un modelo que dice que nadie abandona acierta el 98 % y no sirve para nada.",
 practica=[
  "Ajustar logística y árbol sobre el mismo problema y compararlos con validación cruzada.",
  "Construir la matriz de confusión y asignarle un valor en dólares a cada celda.",
  "Elegir el umbral que maximiza el retorno con presupuesto para el 20 % de la cartera y defender la elección.",
 ],
 proyecto="Recomendación de focalización del caso: a quiénes, por qué, con qué umbral y con qué retorno esperado.",
 ia="Ejercicio de código con error incrustado: el fragmento que entrega el docente entrena y evalúa sobre el mismo conjunto. El grupo lo detecta, lo corrige y estima cuánto habría exagerado el desempeño reportado.",
 datasets=[],
 lecturas=[],
),

15: dict(
 intro="Un modelo aprende del pasado y reproduce sus desigualdades. Esta semana no hay algoritmo nuevo: hay que responder por lo que el modelo hace cuando decide sobre personas.",
 objetivos=[
  "Identificar las fuentes de sesgo de un modelo, desde los datos hasta el despliegue.",
  "Auditar un modelo propio buscando disparidad entre grupos.",
  "Explicar una decisión automatizada a la persona afectada.",
  "Reconocer qué datos personales no deberían haber entrado al modelo.",
 ],
 contenidos=[
  ("De dónde viene el sesgo","Datos históricos, variable objetivo mal elegida, muestra no representativa y variables sustitutas de atributos protegidos."),
  ("Caso de riesgo crediticio","El modelo que niega crédito y no puede explicar por qué. Qué se le dice a quien recibe el no."),
  ("Privacidad","Qué dato personal se necesita de verdad, cuánto tiempo se guarda y quién lo puede ver."),
  ("Explicabilidad","Importancia de variables y explicación local. La diferencia entre explicar el modelo y explicar una decisión."),
  ("Gobernanza","Quién responde cuando el modelo se equivoca y cada cuánto se revisa."),
 ],
 trampa="Creer que quitar la variable sensible elimina el sesgo. El código postal suele ser un sustituto perfectamente eficaz.",
 practica=[
  "Auditar el modelo del proyecto propio: desempeño por subgrupo y disparidad encontrada.",
  "Redactar la explicación que recibiría una persona afectada por la decisión del modelo.",
  "Consultoría cruzada: cada grupo ataca los supuestos de otro y recibe el ataque de vuelta.",
 ],
 proyecto="Borrador completo del cuaderno reproducible, con la sección de limitaciones y sesgos escrita.",
 ia="Pídele al asistente que juegue el papel de la persona perjudicada por tu modelo y que reclame. Las objeciones que no puedas contestar van a la sección de limitaciones del proyecto.",
 datasets=[],
 lecturas=[],
),

16: dict(
 intro="La defensa. Diez minutos para convencer a un panel de que la recomendación se sostiene, y diez para aguantar las preguntas. El cuaderno importa; lo que decide es si la conclusión resiste.",
 objetivos=[
  "Estructurar una recomendación con la pirámide de Minto: conclusión primero.",
  "Producir gráficos listos para presentación, no para exploración.",
  "Anticipar las preguntas del panel y preparar la evidencia que las contesta.",
  "Entregar un cuaderno que otra persona pueda ejecutar de principio a fin.",
 ],
 contenidos=[
  ("Conclusión primero","La pirámide de Minto aplicada a diez minutos: recomendación, tres argumentos, evidencia de cada uno."),
  ("Gráficos de defensa","Menos elementos, más anotación, tamaño de fuente pensado para proyección."),
  ("Las preguntas del panel","Cómo elegiste la línea base, qué pasa si el supuesto no se cumple, cuánto vale esto al año, qué harías distinto con más datos."),
  ("El cuaderno reproducible","Orden, celdas ejecutadas, datos accesibles, bitácora de prompts y limitaciones declaradas."),
  ("Cierre y evaluación entre pares","Qué se aprendió y cómo funcionó cada equipo."),
 ],
 trampa="Contar el proceso en orden cronológico. El panel no quiere saber qué hiciste primero: quiere saber qué hay que hacer el lunes.",
 practica=[
  "Ensayo cronometrado de diez minutos con la conclusión en el primer minuto.",
  "Batería de preguntas cruzadas entre grupos antes de la defensa real.",
  "Revisión final del cuaderno: que corra completo en una máquina limpia.",
 ],
 proyecto="Proyecto final: recomendación de una página más cuaderno reproducible, defendido ante panel. Evaluación 360 entre pares.",
 ia="La bitácora de prompts completa se entrega con el proyecto. En la defensa se puede preguntar por cualquier decisión del cuaderno, y responder que lo generó el asistente no es una respuesta.",
 datasets=[],
 lecturas=[],
),
}

# --- Evaluación del curso
EVALUACION = [
 ("Deberes semanales (7)","25 %","Entregas cortas de los miércoles, cada una atada a la semana que la produce."),
 ("Proyecto de medio semestre · RFM+P","20 %","Segmentación completa con recomendación comercial por segmento. Semana 8."),
 ("Evaluación intermedia de criterio de negocio","10 %","Clasificación del problema propio con línea base y valor anual estimado. Semana 11."),
 ("Avances del proyecto integrador","15 %","Ficha de análisis, bitácora de limpieza, tablero, journey map y modelo documentado."),
 ("Proyecto final y defensa","25 %","Recomendación de una página, cuaderno reproducible y defensa ante panel."),
 ("Participación y evaluación 360","5 %","Trabajo en equipo, consultoría cruzada y evaluación entre pares."),
]

POLITICA_IA = [
 ("Se puede usar","Cualquier asistente de IA generativa, para cualquier parte del trabajo: explorar, escribir código, criticar tu análisis o redactar."),
 ("Se debe registrar","Cada entrega incluye el prompt final que produjo el resultado y una línea sobre qué se verificó de la respuesta."),
 ("Se califica el encargo","No se evalúa el código sino la calidad de la pregunta y el rigor de la verificación. Un buen resultado con un mal encargo no suma."),
 ("Se pregunta en la defensa","En cualquier entrega se puede preguntar por qué se tomó una decisión del cuaderno. Responder que lo generó el asistente no es una respuesta."),
 ("Error incrustado","En las semanas 4 y 14 el docente entrega código generado por IA con un fallo silencioso. El grupo lo encuentra, lo explica y estima el daño que habría causado."),
]

# ── DataCamp ────────────────────────────────────────────────────
DATACAMP_LINK = "https://www.datacamp.com/groups/shared_links/5e64e5d1a48289eaada522b708249212c19b3fd72e1fe954fcb52ab662d01f5f"

# (n, semana, fecha, curso, url, horas, [(alternativa, url)])
DATACAMP_RUTA = [
 (1, 1, "19-ago-2026", "Understanding Data Science",
  "https://www.datacamp.com/courses/understanding-data-science", 2,
  [("Introduction to AI for Work", "https://www.datacamp.com/courses/introduction-to-ai-for-work"),
   ("Pista AI Fundamentals", "https://www.datacamp.com/tracks/ai-fundamentals")]),
 (2, 3, "02-sep-2026", "Introduction to Python",
  "https://www.datacamp.com/courses/intro-to-python-for-data-science", 4,
  [("Intermediate Python", "https://www.datacamp.com/courses/intermediate-python"),
   ("Pista Python Data Fundamentals", "https://www.datacamp.com/tracks/python-data-fundamentals")]),
 (3, 5, "16-sep-2026", "Data Manipulation with pandas",
  "https://www.datacamp.com/courses/data-manipulation-with-pandas", 4,
  [("Exploratory Data Analysis in Python", "https://www.datacamp.com/courses/exploratory-data-analysis-in-python")]),
 (4, 5, "16-sep-2026", "Joining Data with pandas",
  "https://www.datacamp.com/courses/joining-data-with-pandas", 4,
  [("Pista Data Manipulation in Python", "https://www.datacamp.com/tracks/data-manipulation-with-python")]),
 (5, 6, "23-sep-2026", "Introduction to Data Visualization with Matplotlib",
  "https://www.datacamp.com/courses/introduction-to-data-visualization-with-matplotlib", 4,
  [("Introduction to Data Visualization with Seaborn", "https://www.datacamp.com/courses/introduction-to-data-visualization-with-seaborn"),
   ("Intermediate Data Visualization with Seaborn", "https://www.datacamp.com/courses/intermediate-data-visualization-with-seaborn")]),
 (6, 8, "07-oct-2026", "Unsupervised Learning in Python",
  "https://www.datacamp.com/courses/unsupervised-learning-in-python", 4,
  [("Cluster Analysis in Python", "https://www.datacamp.com/courses/cluster-analysis-in-python")]),
 (7, 12, "11-nov-2026", "Introduction to Regression with statsmodels in Python",
  "https://www.datacamp.com/courses/introduction-to-regression-with-statsmodels-in-python", 4,
  [("Intermediate Regression with statsmodels in Python", "https://www.datacamp.com/courses/intermediate-regression-with-statsmodels-in-python")]),
 (8, 14, "25-nov-2026", "Supervised Learning with scikit-learn",
  "https://www.datacamp.com/courses/supervised-learning-with-scikit-learn", 4,
  [("Pista Associate Data Scientist in Python", "https://www.datacamp.com/tracks/associate-data-scientist-in-python")]),
]

DATACAMP_SUGERIDO = ("Hypothesis Testing in Python",
                     "https://www.datacamp.com/courses/hypothesis-testing-in-python",
                     "Complemento natural de la semana 9, donde se ven prueba t, chi cuadrado y ANOVA. No sustituye a ninguna certificación obligatoria, pero suma XP para el concurso.")

DATACAMP_PASOS = [
 ("Abre el enlace de invitación del grupo",
  "Es el enlace del grupo del curso. Al entrar por ahí tu cuenta queda con acceso completo a la plataforma mientras dure el semestre."),
 ("Crea tu cuenta con el correo @usfq.edu.ec",
  "Si ya tienes una cuenta personal, inicia sesión con ella y cambia el correo a tu correo institucional en Settings → Account, o crea una cuenta nueva con el correo de la USFQ."),
 ("Acepta la invitación al grupo",
  "Debes ver el nombre del curso en la esquina superior de tu perfil: esa es la señal de que quedaste dentro y de que tus XP cuentan."),
 ("Completa tu perfil con nombre y apellido reales",
  "El marcador del concurso y la verificación de certificados se hacen con ese nombre."),
 ("Empieza por Understanding Data Science",
  "Es la certificación de la primera semana y no requiere escribir código."),
]

CONCURSO = [
 ("Cómo se mide", "Con el marcador de XP del propio grupo del curso. No hay que llevar cuenta aparte ni reportar nada: la plataforma lo cuenta sola."),
 ("Qué cuenta", "Todos los XP que ganes en la plataforma, de cualquier curso, proyecto o práctica. Las ocho certificaciones obligatorias también suman, pero como todos las hacen, la diferencia se construye con lo que explores por tu cuenta."),
 ("Cuándo", "Desde la primera clase, el 17 de agosto, hasta el domingo 6 de diciembre a las 23:59. El marcador se congela ahí."),
 ("El premio", "Se anuncia en la primera clase y se entrega en la última sesión, el 9 de diciembre."),
 ("Empates", "Gana quien haya alcanzado ese puntaje primero."),
 ("Una regla", "Los XP se ganan aprendiendo. Cualquier intento de inflar el marcador con cuentas duplicadas o repitiendo ejercicios ya completados solo para acumular puntos deja fuera del concurso."),
]


# ══════════════════════════════════════════════════════════════
# RÚBRICAS · una por instrumento de evaluación
# ══════════════════════════════════════════════════════════════
RUBRICAS = {

"Deberes semanales": dict(
 peso="25 % · siete entregas",
 cuando="Los miércoles al cierre del taller, semanas 2, 4, 5, 6, 9, 12 y 14",
 nota="Un deber tarde se recibe hasta 48 horas después con el 70 % del puntaje. Después de eso no se recibe, pero el grupo puede pedir retroalimentación sin nota.",
 criterios=[
  ("Pregunta y unidad de análisis", 20, "La pregunta de negocio está escrita, la unidad de análisis es explícita y hay una comparación declarada."),
  ("Corrección técnica", 30, "El cuaderno corre completo, los números se reproducen y cada decisión sobre los datos está justificada por escrito."),
  ("Línea base o contraste", 20, "Existe la alternativa contra la cual se mide el resultado. Sin línea base, este criterio es cero."),
  ("Traducción a decisión", 20, "El resultado está en unidades de negocio y dice qué hacer el lunes, no qué se calculó."),
  ("Bitácora de IA", 10, "Consta el prompt final y qué se verificó de la respuesta del asistente."),
 ]),

"Proyecto de medio semestre · RFM+P": dict(
 peso="20 %",
 cuando="Se presenta el 7 de octubre y se cierra durante el receso",
 nota="Es el primer entregable grande. El ensayo de la semana 7 no se califica, pero quien no lo hace llega a este sin haber calculado nunca una recencia.",
 criterios=[
  ("Preparación de los datos", 15, "Devoluciones netadas, clientes sin identificar tratados y decisión documentada. Se declara cuántas filas quedaron fuera y por qué."),
  ("Cálculo de R, F, M y P", 20, "Las cuatro métricas por cliente, con la definición de cada una escrita y el margen calculado desde costo y precio."),
  ("Segmentos con nombre de negocio", 20, "Los segmentos tienen nombre comercial, no número de cluster, y el criterio de corte está justificado."),
  ("Los tres requisitos", 15, "Se demuestra que cada segmento es accionable, medible y estable. Un segmento que no cambia ninguna acción se declara como tal."),
  ("Recomendación comercial", 20, "Un mensaje por segmento, con el costo estimado de la acción y el retorno esperado."),
  ("Reproducibilidad y bitácora", 10, "El cuaderno corre de arriba a abajo y la bitácora de prompts está completa."),
 ]),

"Evaluación intermedia de criterio de negocio": dict(
 peso="10 %",
 cuando="Se empieza en la sesión del 4 de noviembre y se entrega el lunes 9",
 nota="Es individual y sin código. Mide si el estudiante distingue qué problema justifica un modelo y cuál no.",
 criterios=[
  ("Clasificación en familia", 25, "Cada problema del catálogo queda asignado a su familia de modelo, o a ninguna, con el argumento."),
  ("Decisión que habilita", 25, "Se nombra la decisión concreta que cambia según el resultado. Si no cambia ninguna, se dice."),
  ("Línea base declarada", 25, "Para cada problema se propone la regla ingenua contra la que se mediría el modelo."),
  ("Valor anual estimado", 25, "Se estima el valor con la ecuación del curso y se identifican los problemas de valor negativo."),
 ]),

"Avances del proyecto integrador": dict(
 peso="15 %",
 cuando="Semanas 2, 4, 7, 10 y 13",
 nota="Se califica el avance acumulado, no cada pieza por separado: lo que se corrigió de la entrega anterior cuenta.",
 criterios=[
  ("Continuidad", 30, "Cada avance se apoya en el anterior y recoge las correcciones recibidas."),
  ("Contacto real con la empresa", 25, "Hay evidencia de conversación con quien toma decisiones, no solo datos descargados."),
  ("Documentación", 25, "Ficha de análisis, bitácora de limpieza y limitaciones conocidas al día."),
  ("Trabajo distribuido", 20, "Se ve el aporte de las distintas personas del grupo en el historial del repositorio."),
 ]),

"Proyecto final y defensa": dict(
 peso="25 %",
 cuando="7 y 9 de diciembre, ante panel",
 nota="Diez minutos de exposición y diez de preguntas. La recomendación de una página se entrega al inicio de la primera sesión.",
 criterios=[
  ("Recomendación de una página", 20, "Conclusión primero, tres argumentos, evidencia de cada uno. Nada de orden cronológico del análisis."),
  ("Cuaderno reproducible", 20, "Corre completo en una máquina limpia, los datos se leen de fuente accesible y las salidas están guardadas."),
  ("Línea base y honestidad", 15, "El modelo se reporta junto a su alternativa y el error en unidades de negocio."),
  ("Limitaciones y sesgos", 15, "Están declarados, incluidos los que no se pudieron resolver, y la auditoría por subgrupo está hecha."),
  ("Defensa oral", 20, "Se responde sin leer, se distingue lo que se sabe de lo que se supone y se sostiene bajo preguntas."),
  ("Bitácora de IA completa", 10, "El registro de prompts y verificaciones cubre todo el semestre."),
 ]),

"Evaluación 360 entre pares": dict(
 peso="5 %",
 cuando="Semana 8 (formativa, sin nota) y semana 16 (con nota)",
 nota="Cada persona evalúa a sus compañeros y a sí misma. El puntaje del grupo se ajusta por el promedio recibido, con un tope de más o menos 15 %. Las evaluaciones son confidenciales para el resto del grupo y el docente descarta la más alta y la más baja de cada persona.",
 criterios=[
  ("Cumplimiento", 20, "5: entregó lo acordado a tiempo, siempre. 3: cumplió con recordatorios. 1: el resto tuvo que rehacer su parte."),
  ("Aporte técnico", 20, "5: resolvió problemas que otros no podían. 3: hizo su parte correctamente. 1: dependió de otros para todo."),
  ("Aporte de criterio", 20, "5: hizo mejores preguntas que las que tenía el grupo. 3: participó en las decisiones. 1: se limitó a ejecutar."),
  ("Colaboración", 20, "5: ayudó a que otros entendieran. 3: trabajó bien con el equipo. 1: trabajó aislado o generó fricción."),
  ("Presencia", 20, "5: asistió y participó siempre. 3: faltó alguna vez avisando. 1: ausencias sin aviso."),
 ]),
}

# ══════════════════════════════════════════════════════════════
# PROTOCOLO DE DATOS DEL PROYECTO
# ══════════════════════════════════════════════════════════════
PROTOCOLO_DATOS = [
 ("Consentimiento de la empresa",
  "Antes de descargar un solo archivo, la empresa firma la carta de una página del curso: autoriza el uso académico, "
  "define qué se puede publicar y nombra a la persona de contacto. Sin esa carta el grupo no puede usar datos reales y "
  "trabaja sobre uno de los diez casos."),
 ("Anonimización antes del repositorio",
  "Nombres de personas, cédulas, correos, teléfonos y direcciones se reemplazan por identificadores antes de que el "
  "archivo entre al repositorio del grupo. La tabla de equivalencias no se sube: queda en la máquina de una sola persona."),
 ("Qué no entra nunca en un asistente de IA",
  "Datos personales identificables, información financiera no publicada y cualquier cosa que la carta de consentimiento "
  "excluya. Al asistente se le describe la estructura y se le pegan filas de ejemplo inventadas, no reales."),
 ("Mínimo necesario",
  "Se pide solo la información que la pregunta de análisis requiere. Si el proyecto es de pronóstico de demanda, no hacen "
  "falta los datos de nómina."),
 ("Qué pasa al terminar el semestre",
  "El repositorio se archiva en privado. Si la empresa lo pide, el grupo entrega el análisis y borra su copia de los datos. "
  "Nada se publica sin autorización escrita."),
 ("Si los datos son públicos o inventados",
  "Se declara en el cuaderno. Un proyecto sobre datos inventados es aceptable si el diseño del análisis es correcto; lo que "
  "no es aceptable es presentarlos como reales."),
]

# ══════════════════════════════════════════════════════════════
# APOYO AL ESTUDIANTE
# ══════════════════════════════════════════════════════════════
NIVELACION = [
 ("Antes de la semana 1", "Cuenta de Google activa y prueba de que Colab abre y ejecuta una celda.",
  "Quince minutos. Si esto falla el primer día, se pierde la sesión entera."),
 ("Semanas 1 a 3", "DataCamp: Introduction to Python. Variables, tipos, listas y diccionarios.",
  "Cuatro horas. Es la nivelación oficial y la certificación de la semana 3."),
 ("Semanas 1 a 3", "Cuadernos de fundamentos de Python del curso anterior, opcionales y sin nota.",
  "Para quien nunca programó. Están en Material Actual, bloque 01."),
 ("Cuando aparezca el bloqueo", "Horario de consulta del docente y foro del curso.",
  "El curso asume cero programación previa: preguntar temprano es parte del método, no una señal de atraso."),
]

RUTA_MINIMA = [
 (2, "Ficha de análisis", "Prerrequisito duro. Sin pregunta definida no hay proyecto."),
 (4, "Bitácora de limpieza y propuesta", "Prerrequisito duro. Todo lo demás corre sobre esta tabla."),
 (8, "Proyecto RFM+P", "Se puede entregar con la segmentación por reglas solamente, sin contraste algorítmico."),
 (13, "Modelo documentado", "Se puede entregar con un solo modelo bien hecho y su línea base, sin comparativa."),
 (16, "Cuaderno y defensa", "Prerrequisito duro. No hay forma de aprobar sin defender."),
]

ACCESIBILIDAD = [
 ("Ejercicios cronometrados",
  "Los retos de quince minutos son de práctica, no de evaluación. Quien necesite más tiempo lo toma, y quien tenga una "
  "adaptación registrada dispone del tiempo extendido que corresponda en cualquier actividad con nota."),
 ("Paleta segura",
  "Los gráficos del curso usan paletas distinguibles con daltonismo. Los que producen los estudiantes también: se pide "
  "no codificar información solo por color, sino apoyarla con forma, posición o etiqueta."),
 ("Texto alternativo",
  "Toda figura de una entrega lleva una línea que describe lo que muestra. Sirve para lectores de pantalla y, de paso, "
  "obliga a saber qué dice el gráfico."),
 ("Material descargable",
  "Todo el sitio funciona sin conexión y los cuadernos se pueden ejecutar en una máquina local: nadie depende de tener "
  "buen internet en el aula."),
]
