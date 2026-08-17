# Analítica de datos aplicada para la decisión de negocio
## Plan de 16 semanas, 32 sesiones de 90 minutos

---

## 1. Encuadre del curso

Esta no es una clase de programación ni una clase de machine learning. Es una clase de decisión con evidencia, donde Python y la inteligencia artificial son el instrumental y no el objeto de estudio. El estudiante de administración que termine el curso no será quien escribe el mejor código de la sala. Será quien sabe qué preguntar, qué exigirle a un análisis, cómo detectar cuándo está mal y cómo convertirlo en una recomendación que un directorio pueda firmar.

**Premisa operativa.** El asistente de IA se usa desde la primera sesión y para todo. Lo que se califica no es el código sino la calidad del encargo y el rigor de la verificación. Cada entrega incluye una bitácora corta de cómo se usó el asistente y qué se corrigió de lo que devolvió.

**Los seis pilares.**
1. Traducir una pregunta de negocio a una estructura de datos.
2. La gramática de la manipulación de datos tabulares.
3. Distinguir descripción, predicción y causalidad.
4. Tipos de modelos y cómo generan valor en el negocio.
5. Comunicar con visualizaciones.
6. Convertir el análisis en una decisión defendible.

**Ritmo semanal.** La primera sesión de cada semana es conceptual y demostrativa, con un caso que se discute antes de tocar el teclado. La segunda es laboratorio, con trabajo en grupos de tres sobre datos reales y una entrega corta al cierre. Ningún concepto se enseña sin un caso que lo motive y ningún laboratorio se hace sobre datos inventados.

**Columna vertebral de datos.** Un solo conjunto de datos operativos de un negocio real del contexto local, feo y con problemas de calidad genuinos, que atraviesa las dieciséis semanas. Sugerencia: la operación de un negocio turístico o gastronómico (transacciones, reservas, clientes, compras, costos, reseñas). Se complementa con dos conjuntos satélite que entran en bloques específicos, uno de cartera de crédito y uno de texto libre de reseñas.

---

## Bloque I. La pregunta antes del dato (semanas 1 y 2)

### Semana 1. Qué decide un dato

**Sesión 1. Por qué fracasan los análisis.**
Apertura con un informe real que llega a una conclusión inválida con datos correctos. Discusión sobre dónde estuvo la falla. Presentación de la escalera descriptivo, diagnóstico, predictivo y prescriptivo, con la advertencia de que la mayor parte del valor organizacional vive en los dos primeros peldaños y casi nadie los hace bien.

**Sesión 2. El taller y el contrato.**
Entorno de trabajo en cuaderno ejecutable. Primer recorrido guiado por un análisis completo de principio a fin, de veinte minutos, para que vean el destino antes del camino. Firma del protocolo de uso de IA del curso.

**Punto teórico.** Dato, información, decisión. La diferencia entre un indicador y una métrica accionable.
**Actividad grupal.** Cada grupo trae un indicador que su familia, su trabajo o la universidad reporta, y responde qué decisión cambia según su valor. Casi ninguno pasa la prueba, y ese es el punto.
**Problema.** Escribir en tres líneas qué decisión concreta permitiría tomar el dato asignado y quién la tomaría.

### Semana 2. La ficha de análisis

**Sesión 3. Unidad de análisis, métrica, comparación, decisión.**
Las cuatro preguntas que se responden antes de abrir cualquier archivo. Qué observación es una fila. Qué se mide y en qué unidad. Contra qué se compara el resultado. Qué acción cambia según lo que salga.

**Sesión 4. Clínica de definiciones.**
El trabajo sucio de acordar qué significa cada palabra. Qué es un cliente activo, qué cuenta como una venta, cuándo un cliente se considera perdido, qué es un mes en una operación con estacionalidad.

**Punto teórico.** Operacionalización de conceptos. Validez de constructo en versión gerencial, sin la jerga.
**Caso.** Dos áreas de una misma empresa reportan cifras de ventas distintas para el mismo mes y ambas tienen razón. Reconstruir por qué.
**Actividad grupal.** Cada grupo redacta la definición operativa de tres términos del negocio de la columna vertebral y luego intercambia con otro grupo para que la ataque.
**Entrega 1.** Ficha de análisis de una página, sin datos y sin código.

---

## Bloque II. La gramática de los datos (semanas 3 a 5)

### Semana 3. Anatomía de una tabla

**Sesión 5. Estructura y calidad.**
Datos ordenados en formato largo. Tipos de dato y por qué un código de sucursal no es un número. Nulos, y la diferencia entre ausente, cero y desconocido. Duplicados. Granularidad, que es el concepto más importante del bloque.

**Sesión 6. Laboratorio de perfilado.**
Primer contacto con la base sucia. Inventario de problemas, cuantificación de cada uno y decisión documentada sobre qué hacer con cada uno.

**Punto teórico.** Tidy data. La distinción entre error de medición, error de registro y valor legítimamente extremo.
**Problema.** El diez por ciento de las transacciones no tiene identificador de cliente. Decidir si se eliminan, se imputan o se analizan aparte, y defender la decisión en función de la pregunta de negocio, no del gusto estético.

### Semana 4. Filtrar, derivar, agrupar, agregar

**Sesión 7. Dividir, aplicar, recombinar.**
El patrón mental que resuelve la mayoría de las preguntas de negocio. Filtros, variables derivadas, agrupamientos y agregaciones. Se enseña como gramática, con el código generado por el asistente y verificado por el estudiante.

**Sesión 8. Laboratorio de preguntas encadenadas.**
Doce preguntas de negocio de dificultad creciente sobre la base común, resueltas contra reloj.

**Punto teórico.** Agregación y pérdida de información. Qué se destruye cada vez que se calcula un promedio.
**Caso.** El promedio de ticket subió y la gerencia celebra, pero el número de transacciones cayó más. Descomponer el efecto.
**Actividad grupal.** Torneo de preguntas: cada grupo formula tres preguntas para que otro grupo las responda con datos en quince minutos.

### Semana 5. Uniones y reestructuración

**Sesión 9. Uniones y el desastre de la duplicación.**
Los cuatro tipos de unión y qué significa cada uno en términos de negocio. El error que llega a un directorio: una unión mal hecha que duplica filas e infla la facturación. Se provoca deliberadamente en clase para que lo vean nacer.

**Sesión 10. Formato largo y ancho, tiempo y ventanas.**
Pivotar. Series de tiempo, agrupación por período, acumulados, promedios móviles, comparación contra el mismo período del año anterior.

**Punto teórico.** Cardinalidad de una relación entre tablas. Uno a uno, uno a muchos, muchos a muchos.
**Problema.** Construir la tabla mensual de indicadores del negocio a partir de cuatro fuentes con granularidades distintas, verificando que los totales cuadren contra una cifra de control conocida.
**Entrega 2.** Cuaderno reproducible de preparación de datos, con bitácora de decisiones de limpieza.

---

## Bloque III. Comparado con qué (semanas 6 y 7)

### Semana 6. Variabilidad, ruido y línea base

**Sesión 11. La señal y el ruido.**
Distribuciones, dispersión, valores extremos. Por qué dos meses consecutivos siempre son distintos y eso no significa nada. Qué es una línea base y por qué ningún resultado se interpreta sin ella.

**Sesión 12. La trampa del promedio.**
Distribuciones bimodales, asimetría, la mediana frente a la media, el tamaño de muestra como condición para creer.

**Punto teórico.** Variación común y variación especial. Regresión a la media.
**Caso.** La sucursal peor evaluada del trimestre recibió una intervención y mejoró. La sucursal mejor evaluada empeoró. Explicar por qué probablemente la intervención no hizo nada.
**Actividad grupal.** Simulación con moneda y hoja de cálculo para ver rachas que parecen tendencias.

### Semana 7. Causalidad para decisiones

**Sesión 13. Por qué correlación no basta.**
Variables de confusión, sesgo de selección, causalidad inversa. La paradoja de Simpson con un caso real y desagregable. El experimento como estándar de referencia y por qué una prueba A y B es la herramienta más subestimada de la gerencia.

**Sesión 14. Diseño de un experimento factible.**
Unidad de asignación, grupo de control, tamaño necesario, duración, qué se mide y qué se decide con el resultado.

**Punto teórico.** Contrafactual. La pregunta de qué habría pasado sin la intervención.
**Caso.** Los clientes del programa de fidelidad gastan el doble. ¿Cuánto de eso lo causa el programa?
**Problema.** Diseñar una prueba A y B real y ejecutable en el negocio de la columna vertebral, con presupuesto y calendario.

---

## Bloque IV. Comunicar con visualizaciones (semana 8)

### Semana 8. El gráfico como argumento

**Sesión 15. Explorar, verificar, comunicar.**
Los tres propósitos y por qué se confunden. El cuarteto de Anscombe como golpe inicial. Repertorio mínimo: línea para tiempo, barras ordenadas para comparación, dispersión para relación, histograma o caja para distribución, y el límite del gráfico de composición. Reglas de honestidad: ejes, escalas, agregación que oculta, tamaño de muestra visible. Fondo blanco, sin decoración, título que lleva la conclusión y no la descripción.

**Sesión 16. Clínica de rediseño y primera defensa.**
Cada grupo toma un gráfico malo publicado en un informe institucional o en prensa y lo rediseña justificando cada cambio. Luego presenta el diagnóstico de datos del negocio en tres figuras.

**Punto teórico.** Codificación visual y precisión perceptual. Por qué la posición se lee mejor que el área y el área mejor que el color.
**Entrega 3, evaluación parcial.** Diagnóstico del negocio en tres gráficos anotados y media página de texto.

> La visualización tiene aquí su semana ancla, pero a partir de este punto se evalúa en todas las entregas restantes. No vuelve a ser un tema, pasa a ser un estándar.

---

## Bloque V. Tipos de modelos y creación de valor (semanas 9 a 13)

> Este bloque no enseña a construir modelos. Enseña a reconocer qué familia de modelo corresponde a cada problema de negocio, qué decisión habilita, cuánto vale esa decisión y cuándo el modelo no vale la pena. El código lo escribe el asistente. El criterio lo pone el estudiante.

### Semana 9. El mapa de los modelos

**Sesión 17. Seis familias y la decisión que habilita cada una.**
Pronóstico responde cuánto habrá y habilita planificar compras, inventario, personal y caja. Propensión responde quién y habilita focalizar un recurso escaso en las personas correctas. Segmentación responde en cuántos grupos se divide el mercado y habilita diferenciar oferta, precio y mensaje. Asociación y recomendación responden qué va con qué y habilitan aumentar el ticket. Detección de anomalías responde qué se salió del patrón y habilita control, fraude y pérdida evitada. Optimización responde cuál es la mejor acción bajo restricciones y es la que convierte una predicción en una decisión. Se añade una familia transversal, los modelos generativos, que no predicen números sino que procesan lenguaje y documentos.

**Sesión 18. La ecuación de valor.**
El valor de un modelo es la mejora sobre la línea base, multiplicada por el número de decisiones que toca, multiplicada por el valor unitario de cada decisión, menos el costo de construirlo y operarlo. Tres condiciones sin las cuales el valor es cero: la predicción debe llegar antes de la decisión, debe cambiar la acción y la organización debe poder ejecutar esa acción.

**Punto teórico.** Línea base obligatoria. Todo modelo compite contra la regla simple que la organización ya usa, que suele ser la intuición de alguien con veinte años de oficio.
**Actividad grupal.** Catálogo de doce problemas de negocio reales. Cada grupo los clasifica por familia, nombra la decisión, propone la línea base y estima el valor anual con la ecuación. Se descubre que tres o cuatro no justifican ningún modelo.
**Problema.** Encontrar en el catálogo el caso donde la predicción llega después de que la decisión ya se tomó, y explicar por qué el proyecto está muerto antes de empezar.

### Semana 10. Pronóstico. Cuánto habrá

**Sesión 19. Anatomía de un pronóstico.**
Tendencia, estacionalidad, ciclo y ruido. Horizonte y su relación con el tiempo de reacción del negocio. El error de pronóstico y su asimetría: en una isla, quedarse sin producto y que sobre producto no cuestan lo mismo.

**Sesión 20. Laboratorio de demanda.**
Pronóstico de demanda del negocio de la columna vertebral, primero con una regla ingenua y luego con un modelo. Comparación honesta entre ambos.

**Punto teórico.** Error absoluto medio y error porcentual. Por qué un pronóstico perfecto no existe y qué nivel de error es tolerable según el costo de cada tipo de fallo.
**Caso.** Compras semanales con logística desde el continente y tiempos de reposición largos. El pronóstico define cuánto se pide y el error se paga en desperdicio o en venta perdida.
**Problema.** Con un error de pronóstico dado, calcular el nivel de inventario de seguridad y traducirlo a dólares inmovilizados.

### Semana 11. Propensión. Quién

**Sesión 21. Clasificación y probabilidad como recurso.**
Un modelo de propensión no dice sí o no, dice con qué probabilidad. Matriz de confusión traducida a dinero, con precio explícito para cada tipo de error. El umbral de decisión presentado como palanca gerencial y no como detalle técnico.

**Sesión 22. Focalización con presupuesto limitado.**
Curva de ganancia acumulada. Si solo alcanza para intervenir al veinte por ciento de la cartera, ¿a quiénes? Comparación contra la línea base de llamar a todos o de llamar al azar.

**Punto teórico.** Clases desbalanceadas y por qué la exactitud global engaña. Si el tres por ciento cae en mora, decir que nadie cae acierta el noventa y siete por ciento y no sirve de nada.
**Caso.** Cartera de crédito de una cooperativa local, o deserción estudiantil universitaria con un presupuesto acotado de tutorías.
**Problema.** Definir el umbral óptimo dado el costo de una llamada y la pérdida esperada de un incumplimiento. El resultado es un número y hay que defenderlo.
**Entrega 4.** Recomendación de focalización de una página con el número de personas a intervenir y el retorno esperado.

### Semana 12. Grupos y asociaciones

**Sesión 23. Segmentación.**
Agrupamiento sin variable objetivo. Segmentación por comportamiento frente a segmentación demográfica. Los tres requisitos de un segmento útil: accionable, medible y estable en el tiempo.

**Sesión 24. Qué va con qué.**
Análisis de canasta, reglas de asociación, sistemas de recomendación en su versión conceptual. Soporte, confianza y elevación explicados con productos reales.

**Punto teórico.** Un segmento no es un descubrimiento de la naturaleza, es una construcción sensible a las variables que se eligieron. Cambiar las variables cambia los segmentos.
**Caso.** Rediseño de la carta, del combo o del layout de un local a partir de lo que se compra junto.
**Actividad grupal.** Cada grupo nombra sus segmentos, escribe el mensaje comercial para cada uno y otro grupo evalúa si el segmento realmente permite hacer algo distinto.

### Semana 13. Anomalías, lenguaje y la decisión final

**Sesión 25. Lo que se sale del patrón y lo que no es un número.**
Detección de anomalías para fraude, error de facturación y falla operativa. Modelos generativos aplicados a datos no estructurados: clasificar cientos de reseñas por tema y sentimiento, extraer campos de facturas, resumir respuestas abiertas de una encuesta. Se conecta con el trabajo de satisfacción y voz del cliente.

**Sesión 26. De la predicción a la decisión, y sus límites.**
Reglas de decisión, restricciones y optimización simple. Y el cierre ético, que aquí no es un adorno: sesgo algorítmico heredado de datos históricos, privacidad, y qué significa automatizar una decisión que afecta la vida de una persona, como negar un crédito o marcar a un estudiante como riesgo.

**Punto teórico.** Un modelo aprende del pasado y por lo tanto reproduce sus desigualdades. La pregunta no es si el modelo es neutral, porque no lo es.
**Caso.** Un modelo de riesgo crediticio que penaliza sistemáticamente a un grupo por razones históricas y no de solvencia.
**Actividad grupal.** Auditoría rápida de uno de los modelos construidos en el bloque, buscando a quién perjudica y qué pasaría si esa persona pidiera una explicación.

---

## Bloque VI. La decisión defendible (semanas 14 a 16)

### Semana 14. Del hallazgo a la recomendación

**Sesión 27. La página que se firma.**
Estructura de una recomendación: situación, hallazgo, recomendación, impacto cuantificado, supuestos, riesgos y qué haría cambiar de opinión. Cuantificación del efecto en dinero o en unidades de negocio. Reproducibilidad como requisito, no como virtud.

**Sesión 28. Taller de escritura y revisión cruzada.**
Cada grupo escribe y otro grupo la revisa con una lista de ataque: dónde está el salto de correlación a causa, dónde falta la línea base, qué gráfico miente, qué supuesto no está declarado.

**Punto teórico.** La diferencia entre lo que el análisis muestra y lo que la recomendación afirma. Casi siempre hay un salto y hay que declararlo.

### Semana 15. Clínica de proyectos

**Sesión 29. Consultoría entre grupos.**
Cada grupo presenta su proyecto en estado de borrador y recibe fuego cruzado de los demás y del docente.

**Sesión 30. Ensayo de defensa.**
Preparación de la presentación final y anticipación de las preguntas difíciles.

### Semana 16. Defensa final

**Sesiones 31 y 32. Presentaciones ante panel.**
Diez minutos de presentación y diez de preguntas por grupo, con un invitado externo del sector en el panel si es posible. Las preguntas apuntan a los supuestos, a la línea base y a la diferencia entre lo que el modelo predice y lo que la recomendación afirma que va a causar.

---

## 2. Proyecto final

Una recomendación de negocio de una página, respaldada por un cuaderno reproducible de principio a fin, que contenga:

Una ficha de análisis con la pregunta, la unidad de análisis y la decisión que se busca informar. Un diagnóstico de datos con las decisiones de limpieza documentadas. Al menos un modelo de alguna de las familias del bloque V, que supere una línea base declarada explícitamente. Dos gráficos anotados con la conclusión en el título. El impacto cuantificado en dinero o en unidades del negocio. Los supuestos, los límites y una declaración honesta de qué no se puede concluir con estos datos.

## 3. Evaluación sugerida

Cuatro entregas parciales suman el cuarenta por ciento, con peso creciente. Laboratorios semanales cortos y participación en las clínicas, veinte por ciento. Proyecto final y defensa, cuarenta por ciento. Dentro de cada entrega, la calidad de la figura y la honestidad de la declaración de límites tienen puntaje explícito.

## 4. Protocolo de uso de inteligencia artificial

El asistente se usa sin restricción y sin necesidad de pedir permiso. A cambio se exigen tres cosas. Bitácora de prompts en cada entrega, con lo que se pidió y lo que se corrigió. Verificación obligatoria, porque el estudiante responde por el resultado aunque no haya escrito la línea. Y un ejercicio recurrente en varias semanas, donde se entrega código generado por un modelo con un error sutil incrustado y el grupo debe encontrarlo, explicarlo y estimar el daño que habría causado si nadie lo notaba.

## 5. Riesgos del diseño

El bloque V es el que más seduce y el que más rápido puede desviar el curso. Si los estudiantes empiezan a competir por la métrica del modelo, el curso perdió. La defensa es mantener siempre visible la línea base y la ecuación de valor, y calificar la decisión y no el desempeño del algoritmo.

El segundo riesgo es la calidad de los datos de la columna vertebral. Conviene asegurarla y perfilarla antes de que empiece el semestre, porque un conjunto de datos que se rompe en la semana cuatro obliga a improvisar el resto del curso.
