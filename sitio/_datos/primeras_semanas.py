# -*- coding: utf-8 -*-
"""Casos de clase, material de estudio y guías del profesor · Semanas 1-4.

Alimenta las páginas nuevas de las primeras cuatro semanas de Análisis de
Datos con IA y Python (ADM 2003 · USFQ). Solo datos, sin lógica: el generador
del sitio lee estas estructuras y no inventa nada.

Estructuras:
  CASOS_CLASE      un caso de discusión por semana, para la sesión del lunes
  MATERIAL_ESTUDIO una lectura previa de 15 minutos por semana
  GUIAS            una guía minuto a minuto por sesión (1..8), 90 min exactos

Las cifras provienen de los laboratorios reales (labs/lab_01.ipynb a
labs/lab_04.ipynb) y se verifican contra sus celdas de comprobación.
"""

CASOS_CLASE = {

1: dict(
 titulo="La pizza que sale del menú",
 industria="Gastronomía",
 dataset="pizza_ventas.csv",
 sesion=1,
 gancho="El dueño quiere premiar a la pizza estrella y eliminar a la peor. Tiene un año completo de tickets sobre la mesa. ¿Alcanza con eso para decidir?",
 narrativa=[
  "Una pizzería de Estados Unidos cierra su año con todo registrado: 21 350 tickets, 49 574 pizzas vendidas de un menú de 32 y 817 860,05 dólares de ingresos. El dueño convoca una reunión con una sola orden del día: premiar a la mejor pizza con la campaña del próximo trimestre y sacar de la carta a la peor, porque la cocina no da abasto con 32 recetas.",
  "El administrador llega con el informe listo. La estrella es la Classic Deluxe, con 2 453 unidades en el año; la peor es la Brie Carre, con apenas 490: la líder vende cinco veces más. Recomendación firmada: retirar la Brie Carre y promocionar la Classic Deluxe. Los números son correctos y cualquiera puede verificarlos contra la tabla.",
  "Lo que está en juego no es un reporte: es qué receta desaparece de la carta y a qué producto se le dedica el presupuesto de promoción. El pizzero que inventó la Brie Carre está en la sala y pide la palabra. La discusión que sigue no es sobre pandas ni sobre datos sucios: los datos están perfectos. Es sobre una palabra que nadie definió antes de calcular.",
 ],
 datos_clave=[
  ("Ingresos del año", "817 860,05 USD en 21 350 tickets"),
  ("Pizzas vendidas", "49 574 unidades de un menú de 32"),
  ("Classic Deluxe", "2 453 unidades: la más vendida del año"),
  ("Thai Chicken", "43 434,25 USD: la que más factura, siendo 5.ª por unidades"),
  ("Brie Carre", "490 unidades, última en todo… y 23,65 USD por unidad, la más alta del menú"),
  ("Thai vs Deluxe", "13,8 % más ingresos con menos pizzas vendidas"),
 ],
 preguntas=[
  ("¿Se puede responder la pregunta del dueño con esta tabla de ventas? Votación a mano alzada antes de mostrar un solo número.",
   "Casi todos votarán que sí. No corrijas: anota el conteo en la pizarra y guárdalo. Ese sí es la materia prima del giro; se les devuelve al final, cuando la tabla haya producido dos estrellas distintas."),
  ("El ranking por unidades corona a la Classic Deluxe. ¿Le damos el premio?",
   "Deja que se comprometan en voz alta con la respuesta. Cuanto más se comprometan, más duele el giro. Si alguien pregunta «¿mejor en qué?», celébralo con nombre y apellido: acaba de hacer la pregunta de la semana 2."),
  ("¿Mejor en qué? ¿Qué significa exactamente «la pizza estrella»?",
   "Recoge definiciones: la que más se vende, la que más factura, la que más deja. Escríbelas como métricas distintas y muestra que cada una produce un ranking distinto. Aterriza: elegir la métrica es una decisión de negocio, no un cálculo."),
  ("¿Firmamos la eliminación de la Brie Carre?",
   "La mayoría dirá que sí por las 490 unidades. Revela el ingreso por unidad: 23,65 USD, primera del menú, 3,5 dólares sobre la siguiente (la Greek, 20,04). Lleva la discusión a que vender poco no es aportar poco: es otro producto jugando otro juego."),
  ("¿Qué dato falta para poder firmar cualquiera de las dos decisiones?",
   "La respuesta que buscas es el margen: cuánto cuesta producir cada una, y no está en la tabla. Cierra con la frase del curso: decir «esta pregunta no se contesta con estos datos» también es análisis, y separa un informe honesto de uno que solo parece completo."),
 ],
 roles=[
  ("Administrador", "Defiende su informe: las unidades miden la demanda real, la gente vota con el horno, y complicar la métrica es buscarle cinco patas al gato."),
  ("Pizzero creador de la Brie Carre", "Defiende su receta: cada Brie Carre deja 23,65 dólares, más que cualquier otra del menú, y sus clientes son los que más gastan. Eliminarla es echar al cliente premium."),
  ("Contadora", "Nadie deposita unidades en el banco: el ranking que importa es el de ingresos, y la conversación seria empieza cuando alguien traiga los costos."),
  ("Dueño", "Modera, hace preguntas incómodas y al final debe firmar una sola decisión. Su mejor jugada es negarse a firmar hasta que le definan «estrella»."),
 ],
 giro="Mismo archivo, otra métrica: la Thai Chicken, quinta por unidades con 2 371, es la número uno en ingresos con 43 434,25 USD, y la Classic Deluxe cae al cuarto puesto con 38 180,50. Nadie tocó los datos: cambió la definición de estrella. Y la «peor» resulta ser la primera del menú en ingreso por unidad.",
 conexion="El miércoles (labs/lab_01.ipynb) cada pareja reproduce este informe completo en Colab —carga, rankings, gráfico y corrección— con las mismas cifras como celdas de comprobación, y abre su bitácora de prompts pidiéndole al asistente las tres métricas alternativas. El entregable señala en qué celda exacta la conclusión se da vuelta.",
),

2: dict(
 titulo="Tres gerentes, tres números, una reunión",
 industria="Retail",
 dataset="superstore.csv",
 sesion=3,
 gancho="La dirección fijó la meta del año: superar las 10 000 ventas. Tres gerentes llegan al directorio con el mismo archivo y tres cifras de cumplimiento distintas. Ninguno se equivocó al calcular.",
 narrativa=[
  "Superstore es una cadena minorista estadounidense de muebles, material de oficina y tecnología, con cuatro años de pedidos registrados (2015-2018). En la planificación anual, la dirección escribió una meta que sonaba clarísima: «superar las 10 000 ventas». Nadie definió qué era una venta, porque parecía obvio.",
  "El día del corte, el gerente comercial abre el archivo, cuenta 10 800 filas y manda un correo de celebración: meta cumplida. El gerente de finanzas cuenta pedidos facturados y encuentra 5 009: la mitad del camino. La gerente de marketing sostiene que una venta sin cliente no existe, cuenta 793 compradores distintos y, si se pide que estén «activos», el número baja hasta 203 según la definición que se use.",
  "Los tres van al mismo directorio, el mismo día, con el mismo archivo. Lo que está en juego es el bono anual del equipo, la meta del año siguiente y la credibilidad de cualquier cifra que vuelva a presentarse en esa sala. Y hay algo peor que nadie ha visto: el archivo que todos usaron ni siquiera contiene solo ventas.",
 ],
 datos_clave=[
  ("Filas del archivo", "10 800, de las cuales 806 no son ventas"),
  ("Líneas de pedido reales", "9 994"),
  ("Pedidos distintos", "5 009 (Order ID)"),
  ("Clientes distintos", "793 (Customer ID)"),
  ("La «venta promedio»", "229,86 / 458,61 / 2 896,85 USD según la unidad elegida"),
  ("Clientes «activos»", "de 203 a 793 según la definición: factor 3,9"),
 ],
 preguntas=[
  ("¿Cuántas ventas hizo Superstore? Pide tres o cuatro cifras en voz alta y anótalas en la pizarra.",
   "Deja que digan un número cualquiera sin pistas. Casi seguro aparecen 10 800, 9 994 o 5 009: las tres saldrán del mismo archivo en diez minutos. La pizarra es tu evidencia de que la ambigüedad no es teórica: ya pasó en el aula."),
  ("¿Quién de los tres gerentes se equivocó? Votación.",
   "Habrá votos para cada uno. Revela: nadie se equivocó en el cálculo; la palabra «venta» nunca se definió. Lleva a la conclusión de que la pelea del directorio es una pelea de definiciones disfrazada de pelea de números."),
  ("El gerente pidió «el ticket promedio». ¿Cuál de los tres números le entregas: 229,86, 458,61 o 2 896,85?",
   "El que quería es el segundo: venta media por pedido. Si le entregas el primero (por línea), la cifra queda a la mitad; el tercero (por cliente) la infla 6,3 veces. Remata: ninguna está mal calculada, dos están mal elegidas."),
  ("¿Cuántos clientes «tiene» Superstore? ¿793 o menos?",
   "Vota primero, luego destapa la clínica: comprar alguna vez, en 365, 180, 90 o 30 días dan 793, 694, 594, 436 y 203. Pide definiciones equivalentes de sus trabajos (cliente activo, empleado activo). La regla: la definición se escribe antes de calcular y no cambia entre meses."),
  ("¿Cómo llegaron 806 filas de gerentes regionales y devoluciones a una tabla de ventas?",
   "Cuenta la historia del export: un libro de Excel con tres hojas pegadas una debajo de otra en un solo CSV, sin un solo error de lectura. No lo resuelvas más: el miércoles las destapan ellos con info(), sample() y tail(). Siembra la duda: ¿el final de tu archivo se parece al principio?"),
 ],
 roles=[
  ("Gerente comercial", "Meta cumplida: el archivo tiene 10 800 filas y la meta eran 10 000 ventas. Cambiar la definición ahora es moverle el arco al equipo que ya metió el gol."),
  ("Gerente de finanzas", "Solo existen 5 009 pedidos facturados: lo demás es inflar. Al 50 % de avance no se le paga bono, se le hace un plan de acción."),
  ("Gerente de marketing", "Las ventas las hacen personas: hay 793 clientes, y activos de verdad quizá 203. Celebrar filas es celebrar papel; el negocio se mide en compradores que vuelven."),
  ("Analista nueva", "Antes de discutir cifras exige definir «venta», «pedido» y «cliente activo» por escrito, y propone que toda meta futura nazca con su ficha de análisis al lado."),
 ],
 giro="Nadie se equivocó en el cálculo, y sin embargo todos reportaron mal: el archivo contra el que se midió la meta trae 806 filas que no son ventas —las otras dos hojas del Excel original, gerentes regionales y devoluciones, pegadas al final por un export descuidado—. La meta de «10 000 ventas» se celebró contando filas que incluían a los propios gerentes.",
 conexion="El miércoles (labs/lab_02.ipynb) el taller aplica los cinco minutos de auditoría —shape, head, info, sample, tail— para destapar las 806 filas, demuestra los tres conteos (9 994 · 5 009 · 793) y cierra con el ataque de fichas entre equipos. El deber 1, primera entrega con nota, es la ficha de análisis del proyecto: una página, sin código.",
),

3: dict(
 titulo="¿Qué es una canción normal?",
 industria="Música y streaming",
 dataset="spotify_canciones.csv",
 sesion=5,
 gancho="El comité editorial debe fijar dos reglas: cuánto puede durar una canción para entrar en las playlists de la casa, y qué cifra de popularidad del catálogo se lleva al directorio. Marketing dice 42; Auditoría, con el mismo archivo, dice 39.",
 narrativa=[
  "Una plataforma musical revisa su catálogo: 32 833 filas con duración, popularidad y género. La dirección de contenido quiere una regla editorial simple —«nada de más de cinco minutos»— porque los remixes largos rompen el ritmo de las playlists. El productor estrella de la casa, que factura con remixes de ocho y diez minutos, pide que la regla no se firme sin ver los datos.",
  "En paralelo, finanzas prepara el informe anual y pregunta qué tan popular es el catálogo. Marketing reporta una popularidad media de 42; Auditoría, con el mismo archivo y el mismo mes, calcula 39. Los dos usaron mean() sobre la misma columna. La reunión se detiene ahí: ¿quién miente?",
  "Debajo de las dos peleas hay un mismo problema: nadie ha mirado la forma de lo que está promediando. Hay una cola de temas larguísimos que estira la duración «típica», hay 2 703 canciones —el 8,2 % del catálogo— con popularidad exactamente cero que nadie reproduce, y hay canciones famosas que aparecen hasta diez veces porque viven en varias playlists. Cada uno de esos detalles cambia el número que llega al directorio, y con él, las regalías que se negocian y el catálogo que se depura.",
 ],
 datos_clave=[
  ("Catálogo", "32 833 filas · 28 356 canciones únicas"),
  ("Duración típica", "media 3,76 min contra mediana 3,60 min: la cola larga estira la media"),
  ("El formato canción", "48,7 % del catálogo dura entre 3 y 4 minutos"),
  ("El umbral con precio", "p90 = 5,00 min: la regla «nada de más de cinco» rechaza exactamente al 10 %"),
  ("Popularidad", "media 42,48 contra mediana 45; 2 703 canciones en cero (8,2 %)"),
  ("La media doble", "42,48 promediando filas contra 39,33 promediando canciones únicas"),
 ],
 preguntas=[
  ("¿Cuánto dura una canción normal? Votación por rangos antes de mostrar nada.",
   "La mayoría dirá «tres y pico» por intuición. Revela media 3,76 y mediana 3,60 y pregunta cuál de las dos es «lo normal». Lleva a la regla de la semana: antes de elegir el estadístico se mira la forma; el histograma tarda cuatro segundos."),
  ("¿Firmamos la regla «nada de más de cinco minutos»?",
   "Haz que el aula le ponga precio antes de votar: 5,00 min es el p90, así que la regla rechaza exactamente al 10 % del catálogo. La discusión buena no es sí o no, sino «¿qué porcentaje estamos dispuestos a rechazar?»: un umbral es una decisión con costo medible."),
  ("¿Aceptamos remixes de diez minutos?",
   "El p99 es 7,17: un tema de más de siete minutos es más raro que 99 de cada 100. Deja que el rol del productor defienda la cola —el género vive ahí— y contrasta percentil por percentil: rock corre más largo que rap en todo el recorrido, así que la regla única por catálogo castiga géneros enteros."),
  ("Marketing dice 42, Auditoría dice 39. ¿Quién miente? Votación.",
   "Nadie: 42,48 promedia filas (apariciones en playlists) y 39,33 promedia canciones únicas. Las famosas están hasta en diez playlists y votan diez veces: las repetidas promedian 60,2 y las de una sola aparición 37,1. Es la unidad de análisis de la semana 2 mordiendo otra vez."),
  ("El 8,2 % del catálogo tiene popularidad cero. ¿Se cuenta o se excluye del informe?",
   "Sin los ceros la media sube de 42,48 a 46,29. Ninguna versión es «la correcta»: «¿qué tan popular es lo que tenemos?» incluye los ceros, «¿qué tan popular es lo que suena?» no. Elegir sin decirlo es elegir el titular del directorio: la decisión se escribe al lado del número."),
 ],
 roles=[
  ("Directora de contenido", "Quiere la regla dura de los cinco minutos: las playlists editoriales viven del ritmo, y un catálogo sin reglas es un catálogo que no se puede programar."),
  ("Productor de remixes", "Los temas largos definen su género y su facturación: el p99 no es un error, es arte. Una regla única por catálogo mata al rock y al edm por igual."),
  ("Gerente de catálogo", "Las 2 703 canciones con popularidad cero son inventario muerto que cuesta dinero mantener: propone depurar antes de discutir promedios."),
  ("Auditora", "No firma ninguna cifra hasta que se declare la unidad: ¿fila o canción única? Su 39,33 contra el 42,48 de marketing es la prueba de que la unidad decide el titular."),
 ],
 giro="La media miente dos veces y en direcciones opuestas: en duración, la cola de temas largos la infla (3,76 contra 3,60 de mediana); en popularidad, el pico de 2 703 ceros la hunde (42,48 contra 45). Y todavía queda la tercera trampa: 42 contra 39 no era un error de nadie, sino canciones famosas votando hasta diez veces por estar en varias playlists.",
 conexion="El miércoles no hay taller normal: es el torneo de las doce preguntas descriptivas sobre este mismo catálogo, contra reloj y por equipos, donde cada respuesta vale por tres cosas —cifra, estadístico elegido y porqué—. El cuaderno con las doce respuestas justificadas es la entrega, y el perfilado descriptivo del dataset del proyecto usa exactamente el mismo método.",
),

4: dict(
 titulo="El catálogo que no sabe cuántos títulos tiene",
 industria="Streaming",
 dataset="netflix_titulos.csv",
 sesion=7,
 gancho="La pregunta más fácil del semestre: ¿cuántos títulos tiene el catálogo? El archivo dice 7 787. El becario preparó una versión «limpia» para el directorio del viernes. Nadie ha mirado qué borró.",
 narrativa=[
  "El equipo de contenido de una plataforma de streaming debe reportar al directorio el tamaño y la composición de su catálogo: cuántos títulos, qué mezcla de películas y series, cuánto se añadió por año. El archivo público tiene 7 787 filas y 12 columnas, y parece la tarea más sencilla del trimestre.",
  "Al abrirlo aparecen los problemas de todo archivo real: 2 389 títulos sin director (el 30,68 %), fechas guardadas como texto y algunas con un espacio delante, una columna de duración que mezcla «90 min» con «2 Seasons» como si fueran la misma cosa, y un título que existe dos veces separado por un espacio invisible que ningún ojo detecta en pantalla.",
  "El becario del equipo, con toda la buena intención, propuso la solución que le devolvió su asistente de IA: borrar las filas incompletas y los duplicados. El código corre sin un solo error y termina imprimiendo «impecable»: 4 804 títulos, ni un hueco. Lo que nadie ha medido es qué se llevó por delante: de las 2 410 series del catálogo sobreviven 131. La empresa está a punto de reportarle al directorio que casi no tiene series, y el duplicado real —el único que sí sobraba— sigue adentro.",
 ],
 datos_clave=[
  ("Filas del archivo", "7 787 · títulos reales: 7 786"),
  ("Sin director", "2 389 títulos (30,68 %), concentrados en el 92,4 % de las series"),
  ("duration", "5 377 valores en minutos (todas películas) y 2 410 en Seasons (todas series)"),
  ("Fechas con espacio inicial", "88 fechas reales que un errors='coerce' convierte en NaT sin avisar"),
  ("La limpieza del becario", "dropna() deja 4 804 títulos: borra el 38,3 % del catálogo y el 94,6 % de las series (quedan 131 de 2 410)"),
  ("Duplicado invisible", "«Consequences» dos veces (s1486 y s1487), separadas por un espacio no separable \\xa0"),
 ],
 preguntas=[
  ("¿Cuántos títulos tiene el catálogo? Votación: ¿7 787?",
   "La mayoría levantará la mano. Guarda el voto: tres láminas después nadie lo sostiene. La respuesta defendible es 7 786 —hay un duplicado invisible— y «títulos completos» son apenas 4 808: el 38,3 % tiene al menos un hueco. La pregunta fácil no existía."),
  ("El 30,68 % de los títulos no tiene director. ¿Es un desastre de captura de datos?",
   "Deja que condenen el dato y luego pregunta dónde vive el nulo: falta en el 92,4 % de las series y solo en el 3 % de las películas. Una serie tiene un director por episodio: el campo significa «no aplica», no «se perdió». Un nulo con estructura no se imputa ni se borra: se documenta."),
  ("El becario propone borrar las filas incompletas para tener la tabla perfecta. ¿Quién firma su limpieza? Votación.",
   "Deja que se comprometan con el «impecable» antes de revelar el daño. Luego haz que lo midan ellos: 7 787 menos 4 804 son 2 983 títulos borrados, y de 2 410 series quedan 131. El catálogo pasa de 30,9 % de series a 2,7 %. Sin un error, sin un warning."),
  ("¿Se puede promediar «90 min» con «2 Seasons»?",
   "La mezcla tiene estructura perfecta: 5 377 minutos = películas, 2 410 Seasons = series. No es ruido, es diseño: dos variables metidas en una columna. La decisión correcta es separarla en dos columnas numéricas, y el nulo resultante en cada mitad es diseño, no suciedad."),
  ("¿Cómo se demuestra que una limpieza no perdió información?",
   "«Quedó limpio» no es evidencia. Se responde con la bitácora —una fila por decisión, con justificación— y la cifra de control: invariantes antes y después (7 787 → 7 786 con la única baja identificada por su show_id; los 10 sin fecha siguen siendo 10). Frente a cualquier «impecable», la respuesta del curso es «demuéstralo»."),
 ],
 roles=[
  ("Becario", "Defiende su limpieza: la tabla quedó perfecta, sin un hueco ni un duplicado, y el código no dio un solo error. Si los datos incompletos no sirven, quitarlos es lo profesional."),
  ("Responsable de series", "Algo no cuadra: su área produce 2 410 series y el reporte nuevo casi no las muestra. Exige saber, fila por fila, qué se borró y por qué justo lo suyo."),
  ("Auditora de datos", "No firma nada sin bitácora de limpieza y cifra de control. Su lema: toda fila que desaparece necesita nombre, cifra y justificación escrita."),
  ("Directora de contenido", "Necesita una sola cifra defendible para el viernes y no le importa el método: que los técnicos se pongan de acuerdo, pero si el directorio detecta un error, la cara la pone ella."),
 ],
 giro="La limpieza «impecable» era una amputación: dropna() borró 2 983 títulos —el 94,6 % de las series— precisamente porque el nulo del director vivía en ellas, y el coerce de las fechas remató 88 fechas reales que solo tenían un espacio delante. Y el único registro que sí sobraba, el duplicado de «Consequences», sobrevivió: su espacio invisible lo hacía «distinto» para drop_duplicates().",
 conexion="El miércoles (labs/lab_04.ipynb) el taller produce el inventario de calidad con porcentajes exactos, la bitácora de limpieza de ocho filas y la cifra de control, y cierra con el ejercicio de error incrustado de la política de IA del curso: encontrar y cuantificar el fallo del fragmento del becario. El deber 2 —bitácora de limpieza del dataset del equipo más la propuesta de proyecto— cierra el primer bloque del curso.",
),
}


MATERIAL_ESTUDIO = {

1: dict(
 titulo="Decidir con datos no es calcular bien",
 minutos=15,
 secciones=[
  ("Los cuatro peldaños de la analítica", [
   "Antes de tocar un archivo conviene saber qué tipo de respuesta buscas. La analítica tiene cuatro niveles y cada uno contesta una pregunta distinta: el descriptivo dice qué pasó (vendimos 49 574 pizzas en un año), el diagnóstico explica por qué (la Brie Carre vende poco porque es la más cara), el predictivo anticipa qué va a pasar (este viernes saldrán unas 140 pizzas del horno) y el prescriptivo recomienda qué hacer (retirar dos pizzas y subir un precio).",
   "No es una escalera de dificultad técnica sino de compromiso: cada peldaño te obliga a decidir algo más. Y saltarse peldaños sale caro: nadie predice bien un negocio que todavía no sabe describir. Las primeras semanas del curso viven en los dos primeros peldaños a propósito, porque el descriptivo mal hecho contamina todo lo que viene después.",
  ]),
  ("Cómo se rompe un análisis con datos correctos", [
   "El caso que abre el curso es un informe real con datos perfectos y conclusión inválida. Un administrador midió «la mejor pizza» con el ranking más natural del mundo —unidades vendidas— y recomendó eliminar la que menos vende. El problema: la pregunta del dueño era cuál pizza es más valiosa, y lo que se midió fue cuál sale más veces del horno.",
   "Ninguna versión más nueva del software y ningún modelo de IA más grande habrían salvado ese informe, porque el error no estaba en el cálculo sino en la métrica que nadie definió. Esa es la idea que sostiene el semestre: los análisis no suelen fallar por la herramienta, fallan por una palabra que nadie acordó antes de calcular.",
  ]),
  ("El cuaderno que corre de arriba a abajo", [
   "La herramienta del curso es Google Colab: un cuaderno en el navegador que mezcla celdas de texto con celdas de código, sin instalar nada. Lo único que necesitas entender el primer día es que el cuaderno tiene memoria y orden: las celdas se ejecutan una tras otra y cada una recuerda lo que hicieron las anteriores.",
   "De ahí sale la regla de oro de todas las entregas: un cuaderno que no corre de arriba a abajo sin errores no vale. Antes de entregar, siempre: Entorno → Reiniciar y ejecutar todo. Si sobrevive a eso, es reproducible; si no, tiene celdas ejecutadas fuera de orden y su resultado es un accidente.",
  ]),
  ("El asistente trabaja para ti, no al revés", [
   "En este curso la IA generativa se usa desde el primer día y para todo: explorar, escribir código, criticar tu razonamiento. Lo que se califica no es el código que te devuelve sino la calidad de tu encargo y el rigor de tu verificación. El protocolo tiene tres verbos: puedes pedir lo que quieras, tienes que verificar todo número contra una ejecución tuya, y tienes que registrar el prompt final y qué comprobaste.",
   "Ese registro es la bitácora de prompts y acompaña cada entrega del semestre. Una pista de lo que significa verificar: si aceptas todo lo que el asistente te devuelve, no lo estás verificando. En la defensa final se puede preguntar por cualquier línea del cuaderno, y «lo generó el asistente» no es una respuesta.",
  ]),
 ],
 ideas=[
  "Un análisis puede tener datos correctos, software correcto y aritmética correcta, y aun así llevar a la decisión equivocada: la métrica es una decisión de negocio, no un cálculo.",
  "Los cuatro niveles de la analítica se distinguen por la pregunta que contestan, y saltarse el descriptivo es la causa de la mitad de los proyectos abandonados.",
  "Un cuaderno vale si corre completo de arriba a abajo tras reiniciar; lo demás es un accidente afortunado.",
  "Con el asistente de IA se califica el encargo y la verificación, no el código: pedir bien y comprobar es la habilidad del curso.",
 ],
 glosario=[
  ("Analítica descriptiva", "El nivel que responde qué pasó, con conteos, sumas y promedios sobre lo ya registrado."),
  ("Métrica", "La fórmula exacta con la que se mide algo; cambiarla puede invertir un ranking sin tocar los datos."),
  ("Cuaderno (notebook)", "Documento ejecutable que mezcla texto y código en celdas ordenadas; el formato de todas las entregas del curso."),
  ("Celda", "La unidad mínima de un cuaderno; se ejecuta una a una y recuerda lo que hicieron las anteriores."),
  ("Bitácora de prompts", "Registro de cada encargo al asistente de IA: el prompt final, qué devolvió, cómo lo verificaste y tu veredicto."),
  ("Prompt", "El texto con el que le encargas trabajo a un asistente de IA; su calidad es lo que este curso evalúa."),
 ],
 antes_de_clase=[
  "Comprueba que tu cuenta de Google funciona y que Colab abre y ejecuta una celda: escribe 2 + 2 y presiona Shift+Enter. Son quince minutos que salvan la primera sesión.",
  "Lee esta página completa (15 minutos) y trae por escrito un ejemplo de tu vida donde un ranking cambie según cómo se mida «mejor»: el mejor jugador, el mejor restaurante, la mejor materia.",
  "Trae laptop el miércoles: la sesión 2 es taller y se trabaja en parejas sobre el cuaderno de la pizzería.",
 ],
),

2: dict(
 titulo="La pregunta antes del dato",
 minutos=15,
 secciones=[
  ("Una consulta no es un análisis", [
   "«Pásame las ventas de California» es una petición de reporte: se contesta con una consulta y no exige decidir nada. «¿Al segmento Corporate le mantenemos el descuento el próximo trimestre?» es una pregunta de negocio: obliga a definir cuatro cosas antes de escribir una línea de código. Unidad de análisis: qué representa una fila del resultado. Métrica: qué número mide eso exactamente. Comparación: contra qué. Decisión: qué cambia según el resultado.",
   "La comparación es la que más se olvida y la que más duele: «Corporate compró 706 146,37» no es ni bueno ni malo hasta que digas contra qué. Y la decisión es el filtro definitivo: si ningún resultado posible cambia lo que se hará el lunes, la pregunta está mal hecha, por interesante que parezca.",
  ]),
  ("La unidad de análisis decide el número", [
   "Esta semana el negocio es Superstore, cuatro años de pedidos de un retail. La pregunta «¿cuál es la venta promedio?» tiene tres respuestas correctas en el mismo archivo: 229,86 por línea de pedido, 458,61 por pedido y 2 896,85 por cliente. Los tres números son «la venta promedio» y ninguno está mal calculado: cada uno contesta una pregunta distinta.",
   "No hay regla de tres que convierta un nivel en otro, porque un pedido tiene entre 1 y 14 líneas y un cliente entre 1 y 17 pedidos. Elegir la unidad de análisis es elegir a quién le das voz: el cliente de 17 pedidos pesa 17 veces más cuando promedias por línea y exactamente igual que los demás cuando promedias por cliente.",
  ]),
  ("Definiciones que mueven titulares", [
   "«¿Cuántos clientes tenemos?» parece pregunta de una cifra y admite cinco respuestas defendibles: 793 si cuenta quien compró alguna vez en cuatro años, y 203 si exige compra en los últimos 30 días. Un factor de 3,9 entre la definición más generosa y la más exigente, sin tocar un dato.",
   "Quien elige la definición sin decirlo, elige el titular de la reunión. La regla del curso: la definición se escribe antes de calcular, se publica al lado del número y se mantiene igual todos los meses. Un indicador cuya definición cambia entre trimestres no es un indicador: es una negociación.",
  ]),
  ("Los cinco minutos de auditoría", [
   "A todo dataset nuevo se le dedican cinco minutos antes de cualquier cálculo, con cuatro métodos en orden fijo: shape dice el tamaño, head muestra el principio, info cuenta cuántos valores reales hay por columna y sample enseña filas al azar. El quinto gesto es tail: mirar el final.",
   "En Superstore ese ritual destapa una sorpresa: el archivo tiene 10 800 filas pero solo 9 994 son ventas. Las otras 806 son dos hojas del Excel original —gerentes regionales y devoluciones— pegadas al final por un export descuidado. head() no las muestra porque el principio del archivo está impecable; por eso la auditoría tiene cinco pasos y no uno.",
  ]),
 ],
 ideas=[
  "Antes de abrir el archivo se contestan cuatro preguntas: unidad, métrica, comparación y decisión. Si falta una, todavía no hay análisis.",
  "La misma pregunta sobre el mismo archivo puede tener varias respuestas correctas; la unidad de análisis decide cuál corresponde.",
  "Toda definición (cliente activo, venta, pedido) se escribe antes de calcular y viaja pegada al número que produce.",
  "Un CSV puede traer pegado lo que no es de la tabla: los cinco minutos de auditoría —incluido tail()— van antes de cualquier suma.",
  "La ficha de análisis de una página, sin código, es el primer entregable del proyecto y el que decide si el caso sirve.",
 ],
 glosario=[
  ("Unidad de análisis", "Lo que representa una fila del resultado: una línea, un pedido, un cliente. Cambiarla cambia todos los números."),
  ("Petición de reporte", "Encargo que se contesta con una consulta y no habilita ninguna decisión; lo opuesto a una pregunta de negocio."),
  ("Comparación", "El contra qué de todo análisis: otro periodo, otro grupo, una meta. Sin ella, un número no es ni bueno ni malo."),
  ("Ficha de análisis", "Página única con pregunta, unidad, métrica, comparación, decisión, fuente y limitaciones; se escribe antes de programar."),
  ("Auditoría inicial", "Los cinco minutos con shape, head, info, sample y tail que se le dedican a todo archivo antes de usarlo."),
  ("Granularidad", "El nivel de detalle de la tabla de origen: qué representa exactamente cada fila del archivo."),
 ],
 antes_de_clase=[
  "Lee esta página (15 minutos) y trae una definición ambigua de tu propio trabajo o carrera: qué es un cliente activo, un estudiante activo, un producto vigente. Se usa en la clínica del lunes.",
  "Con tu equipo, avancen la elección de la empresa del proyecto: esta semana se confirma y no se cambia. Comprueben que pueden conseguir un archivo real con al menos mil filas.",
  "Si ya tienen un archivo candidato, pregúntense qué representa una fila y miren el final con tail(): cuesta cinco segundos y esta semana entenderás por qué.",
 ],
),

3: dict(
 titulo="El promedio que arruina decisiones",
 minutos=15,
 secciones=[
  ("Mira la forma antes que el número", [
   "El promedio es la estadística más usada del mundo y la que más decisiones arruina, porque resume bien solo cierto tipo de distribuciones. Esta semana el negocio es la música: 32 833 canciones del catálogo de Spotify. La duración tiene una cola de temas de 6, 7 y 8 minutos que arrastra la media hacia arriba: media 3,76, mediana 3,60, y el 57,9 % del catálogo queda por debajo de «la media».",
   "La popularidad miente en la dirección contraria: 2 703 canciones —el 8,2 % del catálogo— tienen popularidad exactamente cero, y ese montón hunde la media (42,48) por debajo de la mediana (45). La regla de la semana: antes de elegir el estadístico, mira la forma. Un histograma tarda cuatro segundos y te ahorra el ridículo.",
  ]),
  ("Media o mediana: un criterio, no una costumbre", [
   "La mediana es el valor del medio: la mitad de los casos queda abajo y la mitad arriba, y por eso no la mueven los extremos. La media reparte el total entre todos, y por eso un solo remix de diez minutos o un millar de canciones en cero la arrastran. Si media y mediana coinciden, casi cualquier resumen sirve; si se separan, la forma manda y hay que explicar por qué.",
   "Elegir también es una decisión de negocio. «¿Qué tan popular es lo que tenemos?» incluye las canciones en cero; «¿qué tan popular es lo que suena?» las excluye y la media sube a 46,29. Ninguna versión es la correcta por defecto: la elección se escribe al lado del número, como las definiciones de la semana pasada.",
  ]),
  ("Percentiles: umbrales con precio", [
   "Un percentil no es un adorno: es un umbral operativo. El p90 de la duración es 5,00 minutos: una regla editorial del tipo «nada de más de cinco minutos» rechaza exactamente al 10 % del catálogo. El p99 es 7,17: un tema de más de siete minutos es más raro que 99 de cada 100. Dicho así, la regla deja de ser una opinión y pasa a ser una decisión con costo conocido.",
   "Los percentiles también evitan comparaciones injustas entre grupos: el rock corre más largo que el rap en todo el recorrido, y su mediana roza el p75 del catálogo completo. Pedirle al rock canciones de tres minutos «porque es la media del catálogo» es no haber mirado los percentiles por género.",
  ]),
  ("La dispersión es la otra mitad", [
   "El centro sin la dispersión es media información. La desviación estándar vive en las unidades del dato (minutos, puntos) y no sirve para comparar variables distintas; el coeficiente de variación —desviación entre media— no tiene unidades y sí compara: 0,27 la duración, 0,59 la popularidad. Traducción de negocio: el formato canción existe y es disciplinado; el éxito no tiene formato, y planificar ingresos con «la popularidad típica» es planificar con humo.",
   "Para las categorías no hay media que valga: value_counts cuenta y value_counts(normalize=True) da la proporción, que casi siempre es lo que se reporta. Y ojo con juntar presencia y desempeño: edm tiene más filas del catálogo (6 043, el 18,4 %) y a la vez la popularidad mediana más baja (36); pop tiene menos filas y la mediana más alta (52). Tener mucho de algo y que ese algo funcione son dos indicadores distintos.",
  ]),
 ],
 ideas=[
  "Antes de elegir media o mediana se mira la forma de la distribución: cola a la derecha infla la media, pico en cero la hunde.",
  "Un percentil es un umbral de negocio con precio: el p90 de duración convierte «nada de más de cinco minutos» en «rechazamos al 10 %».",
  "El centro sin dispersión es media información: acompaña toda media o mediana con una medida de dispersión y el número de observaciones.",
  "Presencia no es desempeño: la categoría con más filas puede ser la de peor resultado, y reportarlas juntas evita el ranking engañoso.",
  "Si una fila no es la unidad que crees (una canción repetida en varias playlists), el promedio por fila ya viene sesgado de fábrica.",
 ],
 glosario=[
  ("Media", "El total repartido entre todos los casos; sensible a valores extremos y a montones en un extremo."),
  ("Mediana", "El valor del medio: la mitad de los casos queda por debajo. No la mueven las colas."),
  ("Percentil", "El valor por debajo del cual cae un porcentaje dado de los casos; se lee como umbral operativo."),
  ("Rango intercuartílico (IQR)", "La distancia entre el percentil 25 y el 75: el ancho de la mitad central de los datos."),
  ("Coeficiente de variación", "Desviación estándar dividida por la media; al no tener unidades permite comparar dispersiones de variables distintas."),
  ("Distribución", "La forma en que se reparten los valores de una variable; se ve en un histograma antes de resumirla con un número."),
 ],
 antes_de_clase=[
  "Lee esta página (15 minutos) y juega dos rondas con simuladores/simulador-media-mediana.html: arrastra un punto hacia la cola y mira a la media perseguirlo mientras la mediana ni se inmuta.",
  "Repasa las doce preguntas del reto del laboratorio 3: el miércoles son el torneo por equipos, contra reloj, y cada respuesta exige cifra, estadístico y porqué.",
  "Calcula del dataset de tu equipo una media y una mediana de la misma columna. Si se parecen, anota por qué; si se separan, trae el histograma: es tu primer diagnóstico de forma.",
 ],
),

4: dict(
 titulo="Datos rotos y decisiones documentadas",
 minutos=15,
 secciones=[
  ("Cuantificar en lugar de opinar", [
   "«Los datos están sucios» no es un diagnóstico: un diagnóstico dice qué problema, cuántas filas y qué porcentaje, porque de ahí sale la decisión. Un problema que afecta al 0,1 % se trata distinto que uno que afecta al 30 %. Esta semana el negocio es el catálogo público de Netflix: 7 787 títulos tal cual salieron al mundo, sin que nadie los ensuciara a propósito, con todo lo que un archivo real te va a hacer.",
   "El inventario de esa tabla cabe en una pantalla: 30,68 % sin director, 9,2 % sin reparto, 6,5 % sin país, 88 fechas con un espacio escondido, una columna de duración que mezcla dos unidades y un duplicado invisible. En total, el 38,3 % de los títulos tiene al menos un hueco. Ese número solo ya decide la semana: quien «borre las filas incompletas» borra cuatro de cada diez.",
  ]),
  ("Ausente, cero y «no aplica» son tres cosas distintas", [
   "Antes de tratar un nulo hay que preguntar dónde vive. El del director tiene estructura: falta en el 92,4 % de las series y solo en el 3 % de las películas, porque una serie tiene un director por episodio y quien diseñó la tabla dejó el campo vacío. Ese nulo significa «no aplica», y un nulo que significa «no aplica» no se imputa ni se borra: se documenta.",
   "El del país es otra especie: el país existe pero no se registró. Ahí sí cabe un centinela como «Desconocido», que evita que un conteo por país esconda 507 títulos en silencio. Y el del reparto se queda como está y pasa a limitaciones conocidas, porque no hay fuente para imputarlo. Tres nulos, tres tratamientos, mismo archivo: esa es la madurez que la semana entrena.",
  ]),
  ("Tipos que mienten y duplicados invisibles", [
   "Once de las doce columnas llegan como texto. Algunas deben serlo (s1486 es una etiqueta, no una cantidad), otras mienten: la fecha como texto no se puede ordenar ni restar, y la duración dice «90 min» para películas y «2 Seasons» para series en la misma columna. Noventa minutos y dos temporadas no se pueden promediar: son dos variables disfrazadas de una, y la solución es separarlas en dos columnas numéricas.",
   "Los duplicados tampoco se ven a simple vista: la película «Consequences» existe dos veces, idéntica en todo, separada por un espacio no separable (\\xa0) al final del título, invisible en pantalla y suficiente para burlar cualquier comprobación ingenua. La caza seria normaliza el texto antes de comparar, y decide con criterio: se elimina la copia porque las diez columnas de negocio coinciden, no «porque los duplicados se borran».",
  ]),
  ("La bitácora y la cifra de control", [
   "Una limpieza sin bitácora no es reproducible: es una opinión. La bitácora tiene una fila por decisión —problema, filas afectadas, decisión y justificación— y la justificación es la columna que casi nadie escribe y la que este curso califica. Al final, la cifra de control contesta la única pregunta que importa: ¿perdí información? No con una sensación, sino con invariantes: qué tenía que quedar igual y qué cambio está explicado hasta la última fila.",
   "El contraejemplo de la semana es un fragmento de limpieza generado por IA que corre sin errores y termina imprimiendo «impecable»: su dropna() borra el 38,3 % del catálogo y el 94,6 % de las series —quedan 131 de 2 410—, porque el nulo del director vivía justo ahí. Y el único registro que sí sobraba, el duplicado invisible, sobrevive. Frente a cualquier «impecable», la respuesta profesional es «demuéstralo».",
  ]),
 ],
 ideas=[
  "Un diagnóstico de calidad dice qué problema, cuántas filas y qué porcentaje; sin cifras solo hay impresiones.",
  "Pregunta dónde viven los nulos antes de tratarlos: un hueco con estructura significa «no aplica» y se documenta, no se borra ni se imputa.",
  "dropna() sin subset es la línea más peligrosa del pandas generado por IA: no falla nunca y decide por ti que toda fila incompleta sobra.",
  "Una columna que necesita un if para saber qué significa son dos columnas disfrazadas: una unidad por columna.",
  "La limpieza se defiende con dos artefactos: la bitácora con justificación por decisión y la cifra de control con invariantes antes y después.",
 ],
 glosario=[
  ("Nulo estructural", "Ausencia que significa «no aplica» y sigue un patrón (el director de las series); se documenta en lugar de tratarse."),
  ("Centinela", "Valor explícito («Desconocido») que reemplaza a un nulo para que los conteos no escondan filas en silencio."),
  ("Duplicado de negocio", "Dos filas que representan lo mismo aunque no sean idénticas carácter a carácter; se detecta normalizando antes de comparar."),
  ("dtype", "El tipo de dato de una columna; cuando miente (fecha como texto, número como texto), todo cálculo posterior es falso o imposible."),
  ("Bitácora de limpieza", "Tabla con una fila por decisión de limpieza: problema, filas afectadas, decisión y justificación auditable."),
  ("Cifra de control", "Invariante que se compara antes y después de limpiar para demostrar que no se perdió información sin explicación."),
 ],
 antes_de_clase=[
  "Lee esta página (15 minutos) y juega una ronda de simuladores/simulador-detective-datos.html: un dataset con problemas escondidos y el reloj corriendo. Afila el ojo antes del taller.",
  "Corre describe(include='all') sobre el dataset de tu equipo y trae anotadas tres sospechas: mínimos imposibles, counts desiguales, columnas que mienten su tipo.",
  "Guarda las cifras de partida de tu dataset —filas, claves distintas, conteos por categoría— antes de limpiar nada: sin ellas no habrá cifra de control posible.",
 ],
),
}


GUIAS = {

1: dict(
 titulo="Por qué fracasan los análisis · Caso de la pizzería",
 fecha="17-ago-2026",
 tipo="teoría",
 antes=[
  "Proyector probado y presentaciones/sesion-01.html abierto en pantalla completa (N oculta las notas, ? muestra los controles).",
  "simuladores/simulador-pizza-estrella.html abierto en otra pestaña: es el informe engañoso jugable, por si el aula pide ver el ranking moverse en vivo.",
  "Plantilla del contrato de grupo a mano (está en el sitio) y lista del curso impresa para armar equipos mezclando quien programó con quien no.",
  "Ten el caso fresco: las cifras que vas a decir de memoria son 2 453 (Deluxe), 43 434,25 (Thai), 490 y 23,65 (Brie Carre), 817 860,05 (año).",
  "No te presentes al entrar: la sesión abre con la pregunta del caso, no contigo.",
 ],
 energia="Es la primera impresión del curso y el día más rentable del semestre en motivación: si hoy sienten que esto va de criterio y no de sintaxis, te siguen dieciséis semanas. Hay gente en el aula que viene con miedo a programar; tu mensaje implícito de hoy es que el error de la sesión no lo comete el que no sabe Python, lo comete el que no define la palabra «estrella». Cuida especialmente el momento de la votación inicial: que se equivoquen en público sin castigo es lo que compra la confianza del resto del curso.",
 arco="La sesión va del caso al mapa y del mapa a las reglas: primero la pizzería completa (votación, ranking, giro, la peor pizza), porque la anécdota instala la idea de que la métrica es una decisión; después la escalera de la analítica y los tres agujeros, que le ponen nombre a lo que acaban de vivir; y al final las reglas del juego —arco del semestre, protocolo de IA, equipos— cuando ya están convencidos de que el curso vale la pena. Invertir el orden (reglas primero) mata la sesión.",
 objetivos_salida=[
  "Todos votaron al menos dos veces (¿alcanza la tabla?, ¿premiamos a la Deluxe?) y vieron su voto darse vuelta.",
  "Todos pueden decir la frase de la semana: los datos eran correctos, lo que faltaba era la definición de estrella.",
  "Todos conocen las cuatro reglas del protocolo de IA y saben que la bitácora de prompts se entrega con cada cuaderno.",
  "Cada estudiante salió con equipo formado, contrato de grupo firmado o por firmar esta semana, y sabe que el miércoles trae laptop.",
  "Al menos tres estudiantes dieron ejemplos propios de métrica cómoda frente a métrica correcta (material para la semana 2).",
 ],
 minuto=[
  ("0–8", "Apertura con el caso, sin presentarte", [
   "Cuenta la situación con calma: una pizzería, un año de tickets, el dueño quiere premiar a la mejor y eliminar a la peor.",
   "Votación a mano alzada ANTES de mostrar números: ¿se puede responder con la tabla de ventas? Anota el conteo: casi todos dirán que sí y ese sí se cobra en el minuto 20.",
  ]),
  ("8–20", "Dos rankings, dos estrellas", [
   "Muestra el ranking por unidades: la Classic Deluxe gana con 2 453. Pregunta «¿le damos el premio?» y deja que se comprometan.",
   "El giro: mismo dato, otra pregunta —¿cuál trae más dinero?—. La Thai Chicken, quinta por unidades, gana con 43 434,25 y la Deluxe cae a cuarta. Deja un silencio después de revelar.",
   "Remata: nadie tocó los datos; cambió la definición de estrella.",
  ]),
  ("20–30", "La «peor» pizza y la idea del curso", [
   "Segunda vuelta: la Brie Carre, última con 490 unidades. ¿La eliminamos? Revela el ingreso por unidad: 23,65, primera del menú. Vender poco no es aportar poco.",
   "Nadie preguntó por el margen: esa decisión necesita un dato que la tabla no trae, y decirlo también es análisis.",
   "Devuélveles el voto del minuto 0: los datos eran correctos, completos y limpios; faltaba la definición. Esta frase vuelve todas las semanas.",
  ]),
  ("30–48", "La escalera de la analítica y qué es Business Analytics", [
   "Revela los cuatro peldaños con la pizzería como ejemplo en cada uno: qué vendimos, por qué cayó agosto, cuántas masas para diciembre, qué precio a la Brie Carre.",
   "En cada peldaño pregunta al aula qué haría falta saber; el costo de saltarse peldaños: pedir un modelo predictivo sin descriptivo.",
   "Cierra con la definición honesta: habilitar decisiones con evidencia. Python es el medio; el curso entrena el criterio.",
  ]),
  ("48–56", "Cómo se rompe un análisis con datos correctos", [
   "Los tres agujeros: muestra torcida, comparación ausente, métrica sin definir. Pide un ejemplo propio de cada uno.",
   "Anota los ejemplos del aula en la pizarra o en tu cuaderno: son material de apertura para la semana 2.",
  ]),
  ("56–72", "Reglas del juego y demo del protocolo de IA", [
   "El arco del semestre en un vistazo: cinco bloques, RFM el 7 de octubre, defensa el 7 y 9 de diciembre, una industria distinta por semana en este primer bloque.",
   "Demo en vivo del protocolo: pide al asistente «¿cuál es la mejor pizza?» (respuesta genérica) y luego el prompt bueno con definición, periodo, métrica y verificación. La diferencia ES la lección.",
   "Lo que se califica: el encargo y la verificación, no el código.",
  ]),
  ("72–78", "Las cuatro reglas que firman hoy", [
   "Recorre el protocolo: se puede pedir todo, se verifica todo, se registra todo, y en la defensa «lo generó el asistente» no es una respuesta.",
   "Adelanta la regla de datos: nada real de una empresa entra a un asistente; llega formalizada con el proyecto en la semana 2.",
  ]),
  ("78–90", "Equipos, contrato y cierre", [
   "Equipos de cuatro mezclando quien ya programó con quien no. Hoy: nombre, contrato firmado (incluye la regla de la bitácora) y repositorio creado. Recuerda la evaluación 360.",
   "Cierre operativo: el miércoles es taller con laptop y cuenta de Google funcionando; lectura previa: el material de la semana 1 del sitio (15 minutos).",
   "Despídete con el teaser de la semana 2 y deja la última lámina proyectada mientras salen.",
  ]),
 ],
 errores=[
  ("«Yo nunca he programado, ¿voy a poder con este curso?»",
   "Respuesta pública, no privada: el curso asume cero programación previa, la nivelación existe (DataCamp y cuadernos opcionales) y el error de hoy lo cometió alguien que sabía calcular perfectamente. Anota quién lo preguntó para seguirlo de cerca el miércoles."),
  ("«¿Entonces podemos usar ChatGPT en los deberes?»",
   "Sí, desde hoy y para todo, y no es trampa: es la política del curso. Lo que convierte el uso en nota es la bitácora: prompt final más qué se verificó. Aprovecha para repetir que aceptar todo lo que devuelve el asistente es no verificarlo."),
 ],
 si_tarde=[
  "Recorta primero la demo de IA en vivo: muestra solo los dos prompts en pantalla, sin ejecutarlos, y promete la demo completa para el miércoles.",
  "Comprime la escalera a un ejemplo por peldaño sin preguntas al aula; el laboratorio 1 la retoma entera.",
  "La formación de equipos no se recorta pero puede reducirse a armar los grupos y dejar contrato y repositorio como tarea de la semana; el caso y el protocolo son intocables.",
 ],
 alertas=[
  "Anota quién no tiene laptop o cuenta de Google funcionando: el miércoles esa persona necesita pareja con máquina desde el minuto cero.",
  "Detecta los equipos cojos (cuatro personas que no se conocen o todos sin experiencia): reequilibra antes del miércoles, después cuesta el doble.",
  "Guarda los ejemplos del aula de los tres agujeros: abren la sesión 3 y demuestran que escuchas.",
 ],
),

2: dict(
 titulo="Colab y el primer cuaderno · Taller de la pizzería",
 fecha="19-ago-2026",
 tipo="taller",
 antes=[
  "labs/lab_01.ipynb abierto en Colab con la primera celda YA ejecutada: la sesión tarda en arrancar y ese minuto muerto al inicio desconcentra.",
  "presentaciones/sesion-02.html abierto: hoy el deck ocupa unos 35 minutos repartidos; el resto es taller puro.",
  "Verifica al entrar quién trae laptop; quien no, se sienta desde el arranque con alguien que sí.",
  "Revisa tus alertas del lunes: los equipos cojos y quien preguntó si podría con el curso se atienden primero en las rondas por mesas.",
  "Ten a mano las cifras de control del cuaderno: 48 620 líneas, 21 350 pedidos, 817 860,05 de ingresos; son los asserts de las comprobaciones.",
 ],
 energia="Hoy ejecutan sus primeras celdas y es el día más importante del curso para la motivación: si alguien sale pensando que Python no es para él, es muy difícil recuperarlo después. El enemigo de hoy no es la dificultad —el cuaderno está escrito—, es el pánico ante el primer mensaje rojo. Tu trabajo emocional es normalizar el error: cada NameError de hoy es una oportunidad de mostrar que reiniciar y ejecutar todo arregla el 80 % de los males. Celebra en voz alta la primera comprobación superada de cada mesa.",
 arco="Primero se desbloquea la herramienta (demo de Colab con un error provocado a propósito), luego se instalan las reglas del taller que valen todo el semestre (parejas, rotación de teclado, celdas de comprobación), después la demo de la bitácora con el asistente —que es la pieza nueva de verdad—, y solo entonces 45 minutos de trabajo por parejas sobre el arco completo pregunta-carga-describe-gráfico-conclusión. El cierre con checklist es sagrado: define qué significa entregar en este curso.",
 objetivos_salida=[
  "Todos ejecutaron el cuaderno completo hasta el gráfico final, no solo lo leyeron.",
  "Todas las parejas pasaron la Comprobación 1 (48 620 líneas, 21 350 pedidos) y la mayoría la Comprobación 2 (dos métricas, dos estrellas).",
  "Todos saben recuperarse de una sesión muerta de Colab con Entorno → Reiniciar y ejecutar todo.",
  "Cada estudiante registró al menos una fila propia en la bitácora de prompts con la función registrar().",
  "Todos saben que la entrega es lab_01_apellido.ipynb, ejecutado de arriba a abajo, con tres filas de bitácora.",
 ],
 minuto=[
  ("0–5", "Votación y armado de parejas", [
   "Pregunta quién ha programado alguna vez y cuenta las manos: ese conteo arma las parejas, un sí con un no.",
   "Insiste: hoy nadie instala nada y el curso asume cero programación previa. Arma las parejas antes de pasar de lámina.",
  ]),
  ("5–11", "Demo en vivo de Colab, con error incluido", [
   "Crea una celda de texto y una de código; ejecuta una celda que usa una variable definida más abajo y muestra el error sin dramatismo.",
   "Explica sesión y memoria: el cuaderno recuerda lo ejecutado y la sesión se muere sola tras un rato; reiniciar es normal, no un accidente.",
   "La regla que se llevan: antes de entregar, Entorno → Reiniciar y ejecutar todo.",
  ]),
  ("11–17", "Las reglas del taller (valen todo el semestre)", [
   "Parejas con rotación de teclado; anuncia que vas a pasar mirando quién teclea. El que mira no descansa: dicta, cuestiona y anota.",
   "Un año completo de un negocio real cabe en el navegador: es la misma tabla del lunes, hoy dejan de mirarla y empiezan a tocarla.",
  ]),
  ("17–25", "El arco del análisis y los puntos de control", [
   "Revela el esqueleto de cinco pasos: pregunta, carga, describe, gráfico, conclusión. Es el esqueleto de todos los labs y del proyecto final.",
   "Presenta las celdas con ✅: son asserts que gritan solos si el número no da. Si no cuadran, se rompió algo y se vuelve atrás; seguir sin corregir es perder la hora.",
  ]),
  ("25–35", "Demo de la bitácora con el asistente", [
   "En vivo y sin ensayo: pide al asistente tres métricas alternativas para elegir la mejor pizza, muestra la respuesta y registra la fila con registrar() delante de todos.",
   "Enseña la fila de ejemplo resuelta del cuaderno y haz repetir la regla: si aceptas todo lo que devuelve el asistente, no lo estás verificando.",
  ]),
  ("35–80", "Bloque de trabajo por parejas", [
   "Suelta a las parejas con la lámina de hitos proyectada y circula por las mesas; primero las mesas de tus alertas del lunes.",
   "Atascos típicos: sesión muerta de Colab (reiniciar y volver a correr) y celdas fuera de orden (NameError). Resuélvelos en voz alta la primera vez.",
   "A los 60 minutos avisa cuánto falta; a los 78 pide manos arriba de quién pasó la Comprobación 2.",
  ]),
  ("80–86", "Checklist de salida", [
   "Recorre la checklist punto por punto y da dos minutos para el Reiniciar y ejecutar todo final.",
   "Lo que no alcanzó (ejercicios 🌶️/🔥, las otras filas de bitácora) se termina en casa: la entrega es el cuaderno completo, nombre lab_01_apellido.ipynb.",
  ]),
  ("86–90", "Cierre y teaser", [
   "Deja proyectada la lámina final mientras salen: el lunes llega Superstore, 10 800 filas de un retail donde tres gerentes cuentan y les salen números distintos.",
   "Lectura previa: el material de la semana 2 del sitio (15 minutos).",
  ]),
 ],
 errores=[
  ("FileNotFoundError: No encuentro la carpeta de datos",
   "Es el error diseñado del setup: en Colab no clonaron el repositorio. Ejecutar la celda del git clone que el propio mensaje indica y volver a correr el setup. Si pasa en local, están parados fuera de la carpeta del curso."),
  ("NameError: name 'pizzas' is not defined",
   "Celdas ejecutadas fuera de orden o sesión nueva sin memoria. Entorno → Reiniciar y ejecutar todo. Aprovecha el primero que aparezca para mostrarlo al aula entera: es la lección de reproducibilidad en vivo."),
  ("«Se me desconectó la sesión» / el entorno se reinicia solo",
   "Normal en Colab tras inactividad: la sesión se muere y olvida todo. Reconectar y Reiniciar y ejecutar todo. Repite que por eso el cuaderno debe correr de arriba a abajo: la sesión se pierde, el cuaderno queda."),
  ("AssertionError en la Comprobación 1 con menos de 48 620 filas",
   "Filtraron o alteraron algo sin querer antes del assert. Volver a ejecutar desde la celda de carga sin modificaciones y avanzar de nuevo; el mensaje del assert dice exactamente qué cifra se esperaba."),
 ],
 si_tarde=[
  "Los ejercicios 🌶️ y 🔥 se van a casa completos: el bloque de trabajo protege el arco principal hasta la Comprobación 2.",
  "El reto 🎯 se reduce a escribir las tres frases con cifras, sin el ataque del asistente (queda como parte de la entrega).",
  "La bitácora en clase baja a una fila mínima registrada por pareja; las otras dos se completan en casa.",
 ],
 alertas=[
  "Lista de quién NO pasó la Comprobación 2 al cierre: son los candidatos a quedarse atrás en la semana 2 y a quienes revisas primero el lunes.",
  "Parejas donde una persona no soltó el teclado: sepáralas o márcalas para rotación forzada el próximo taller.",
  "Quién no entregó o entregó sin ejecutar completo: el deber 1 (semana 2) es con nota y conviene avisarle antes.",
 ],
),

3: dict(
 titulo="Unidad de análisis y ficha · Caso Superstore",
 fecha="24-ago-2026",
 tipo="teoría",
 antes=[
  "presentaciones/sesion-03.html y simuladores/simulador-unidad-analisis.html abiertos en pestañas separadas.",
  "Pizarra despejada: vas a anotar las cifras que el aula diga en la apertura y las necesitas visibles hasta el minuto 19.",
  "Revisa las alertas del taller: quién no pasó la Comprobación 2 del lab 1 recibe una pregunta fácil hoy para reengancharlo.",
  "Cifras de memoria: 10 800 filas, 9 994 líneas, 5 009 pedidos, 793 clientes, 229,86 / 458,61 / 2 896,85, activos de 203 a 793.",
  "Recupera los ejemplos de métrica ambigua que el aula dio en la sesión 1: úsalos al presentar la clínica de definiciones.",
 ],
 energia="Hoy se dicta el concepto más importante del primer bloque: la unidad de análisis. No tiene código y por eso el riesgo es que suene a filosofía; el antídoto es que cada idea aterrice en una cifra concreta de Superstore y en una votación. La sesión funciona si duele: si en la clínica de definiciones alguien defiende con vehemencia que los clientes son 793 y otro que son 203, ganaste. El segundo riesgo es el alivio equivocado —«esto es obvio»—: recuérdales que tres gerentes reales fueron al directorio con tres números y ninguno era tonto.",
 arco="Apertura con la pregunta del gerente y cifras del aula en la pizarra (el compromiso público primero), revelación de los tres conteos y las tres ventas promedio (el asombro), luego el método que ordena el asombro: las cuatro preguntas de la ficha, la clínica de cliente activo, y la sorpresa de las 806 filas que deja sembrado el taller. Se cierra con la ficha de análisis como entregable y el simulador jugado en vivo. El orden importa: asombro antes que método, método antes que entregable.",
 objetivos_salida=[
  "Todos pueden nombrar las cuatro preguntas previas: unidad, métrica, comparación y decisión.",
  "Todos vieron que 229,86, 458,61 y 2 896,85 son «la venta promedio» y saben cuál pedía el gerente.",
  "Todos saben que «cliente activo» admite definiciones defendibles entre 203 y 793 y que la definición se escribe antes de calcular.",
  "Cada equipo sale sabiendo que el miércoles trae el borrador de su ficha de análisis y la empresa del proyecto decidida.",
  "Nadie sabe todavía CÓMO se destapan las 806 filas (eso es del taller), pero todos saben que existen.",
 ],
 minuto=[
  ("0–7", "La pregunta de primer día de gerente", [
   "Presenta el negocio en dos frases: Superstore, cuatro años de pedidos, el dataset con el que medio mundo aprendió Tableau.",
   "«¿Cuántas ventas hicimos?» Pide tres o cuatro cifras en voz alta y anótalas en la pizarra sin dar pistas: cualquier número sirve.",
  ]),
  ("7–19", "Tres barras y tres promedios", [
   "Revela las tres barras una a una: 9 994 líneas, 5 009 pedidos, 793 clientes. Las tres salen del mismo archivo y las tres son correctas. Compara con la pizarra.",
   "Segunda vuelta: la venta promedio también es triple (229,86 / 458,61 / 2 896,85). El gerente quería la segunda. Remata: ninguna está mal calculada, dos están mal elegidas.",
   "Deja el silencio después del factor 12,6 entre la respuesta más chica y la más grande.",
  ]),
  ("19–28", "De la consulta al análisis", [
   "La distancia 229,86 → 2 896,85 sin un error de cálculo es la razón de ser de la semana.",
   "Distinción que ordena todo: «pásame las ventas de California» (consulta) contra «¿mantenemos el descuento a Corporate?» (análisis). Pide un ejemplo de cada tipo sacado de sus trabajos y clasifícalos en vivo.",
  ]),
  ("28–42", "Las cuatro preguntas", [
   "Unidad de análisis a fondo: un pedido tiene de 1 a 14 líneas, un cliente de 1 a 17 pedidos con mediana 6; por eso no hay regla de tres entre niveles. La frase para llevarse: elegir la unidad es elegir a quién le das voz.",
   "Las otras tres más rápido. Comparación: «Corporate compró 706 146,37, ¿bien o mal?» — no se puede saber sin el contra qué. Decisión: si nada cambia con el resultado, la pregunta está mal hecha.",
  ]),
  ("42–54", "Clínica: ¿cuántos clientes tenemos?", [
   "Pregunta con cara seria y vota: ¿793 o menos? Luego destapa qué significa «tener» un cliente.",
   "Revela las cinco barras: de 203 a 793, factor 3,9, todas defendibles. Quien elige la definición sin decirlo, elige el titular del directorio.",
   "Regla del curso: la definición se escribe antes de calcular, va al lado del número y no cambia entre meses.",
  ]),
  ("54–60", "La sorpresa sembrada: las 806 filas", [
   "Cuenta que para contar los 9 994 hubo que limpiar primero: el archivo trae 10 800 filas y 806 son otras dos hojas del Excel pegadas debajo (gerentes y devoluciones).",
   "head() no las muestra porque el principio está impecable. No resuelvas más: el miércoles las destapan ellos con info(), sample() y tail().",
  ]),
  ("60–72", "La ficha de análisis y el simulador", [
   "Recorre los siete campos de la ficha con el ejemplo del cuaderno (campaña de reactivación de enero). El campo que más cuesta: decisión que cambia; el que más olvidan: limitaciones conocidas.",
   "Abre el simulador de unidad de análisis y juega dos rondas en vivo: pide a alguien que prediga el número antes de cambiar la unidad. Queda enlazado en el sitio.",
  ]),
  ("72–90", "Miércoles, deber 1, proyecto y cierre", [
   "El miércoles: los cinco minutos de auditoría sobre Superstore, separar las 806 filas y el ataque de fichas entre equipos. El deber 1 —primera entrega con nota— se entrega al cierre del taller.",
   "La decisión de la semana para el proyecto: la empresa se elige ahora y no se cambia; comprobar que existe un archivo real con al menos mil filas.",
   "Cierra con la frase de la semana proyectada y, si sobra tiempo, haz recitar al aula: unidad, métrica, comparación, decisión. El miércoles, laptop obligatoria.",
  ]),
 ],
 errores=[
  ("«¿Pero cuál de los tres números es el correcto?»",
   "La pregunta trae la trampa incorporada: ninguno es «el» correcto en abstracto; cada uno contesta una pregunta distinta. Devuélvela al aula: ¿correcto para decidir qué? Si la decisión es el bono por ticket, 458,61; si es cuánto vale un cliente, 2 896,85."),
  ("«Mi empresa no nos va a dar datos» (aparece al hablar del proyecto)",
   "Respuesta en dos partes: existe la carta de consentimiento de una página del protocolo del curso, y si aun así no hay datos, hay diez casos alternos publicados. Lo que no existe es proyecto sin datos: un caso brillante sin archivo es un ensayo, y el curso no califica ensayos."),
 ],
 si_tarde=[
  "El simulador en vivo se cae primero: queda enlazado en el sitio y el concepto ya quedó demostrado con las barras.",
  "La clínica de cliente activo se comprime a revelar las cinco barras sin recoger definiciones del aula.",
  "El bloque final se reduce a tres avisos secos: taller el miércoles con laptop, deber 1 al cierre, empresa confirmada esta semana. La ficha y las cuatro preguntas no se recortan.",
 ],
 alertas=[
  "Anota qué equipos no tienen empresa candidata: el miércoles el ataque de fichas los agarra sin material y hay que asignarles caso alterno antes.",
  "Guarda las definiciones ambiguas que dio el aula en la clínica: son ejemplos para abrir la sesión 5 (¿qué es una canción «normal»?).",
 ],
),

4: dict(
 titulo="Auditoría de Superstore y ataque de fichas · Taller",
 fecha="26-ago-2026",
 tipo="taller",
 antes=[
  "labs/lab_02.ipynb abierto en Colab con la primera celda ejecutada; presentaciones/sesion-04.html en la otra pestaña (el deck ocupa ~20 min al inicio y ~35 al final).",
  "Verifica al entrar que cada equipo trae su ficha de análisis borrador y la empresa decidida: sin eso el ataque de fichas se cae. Ten casos alternos listos para los equipos de tu alerta del lunes.",
  "Cifras del árbitro a mano: 806 filas ajenas, 9 994 · 5 009 · 793, los 6 pedidos intrusos (5 015 contra 5 009) y los 296 pedidos devueltos (5,9 % de 5 009).",
  "Ten preparado el ejemplo de CSV en español (sep=';', latin-1, coma decimal) por si algún equipo ya trajo el archivo de su empresa: es la ocasión de oro.",
  "Revisa quién no pasó la Comprobación 2 del lab 1: hoy circula primero por esas mesas.",
 ],
 energia="Hoy pasan de ejecutar un cuaderno a auditar un archivo, y la primera entrega con nota (deber 1) cierra la sesión: hay nervios de nota por primera vez. El momento de máxima energía debe ser el ataque de fichas: es la primera vez que un equipo critica el trabajo de otro en voz alta, y de cómo lo modules depende que la consultoría cruzada del resto del semestre sea deportiva y no personal. Modela tú el primer ataque con dureza sobre la ficha de ejemplo —nunca sobre la de un equipo— y celebra el mejor ataque, no la mejor defensa.",
 arco="Apertura con la votación de head() (que conecta con la siembra del lunes), los cinco métodos y la historia de las 806 filas resuelta, el peaje de los CSV en español —que les va a pasar con su propia empresa este mes—, y de ahí 31 minutos de taller sobre el cuaderno. La segunda mitad cambia de músculo: ataque de fichas entre equipos (la actividad estrella), checklist del deber 1 y confirmación de empresa. El orden protege lo importante: si algo se sacrifica, es del medio, nunca el ataque ni el deber.",
 objetivos_salida=[
  "Todos separaron las 806 filas con Sales.notna() y pasaron la Comprobación 1 (9 994 líneas, 2 297 200,86 en ventas, 793 clientes).",
  "Todos demostraron los tres conteos (9 994 · 5 009 · 793) y saben cuál responde a «ticket promedio».",
  "Cada equipo entregó su ficha al equipo de al lado, recibió dos ataques sobre unidad y decisión, y anotó qué reescribe.",
  "El deber 1 quedó entregado o con checklist clara para completarlo en 48 horas (lab_02_apellido.ipynb).",
  "Cada equipo confirmó empresa del proyecto o quedó asignado a un caso alterno con fecha.",
 ],
 minuto=[
  ("0–6", "Votación: ¿head() habría bastado?", [
   "Retoma el lunes: el archivo trae 806 filas que no son ventas. Votación: ¿quién las encontraría mirando head()? Deja que digan que sí y pídeles cómo.",
   "Revela: imposible, head() enseña el principio y el principio está impecable; la basura vive al final. Por eso la auditoría tiene cinco pasos y no uno.",
  ]),
  ("6–19", "Los cinco métodos y el misterio resuelto", [
   "Recorre la tabla de la sesión: shape, head, info, sample, tail, en este orden, siempre. La lección incómoda: head() no delató nada y por eso existe el resto.",
   "Cuenta la costura: hasta la fila 9 993 tabla de ventas; después una fila Person/Region, cuatro gerentes con nombre, una fila Returned/Order ID y 800 «Yes». Un Excel de tres hojas exportado a un CSV. Nadie recibió un error.",
   "La cifra del día: quien sume Sales no se equivoca; quien cuente filas y las llame ventas, sí.",
  ]),
  ("19–24", "Dialectos del CSV: el peaje de los archivos reales", [
   "Tres síntomas y su parámetro: todo en una columna con punto y coma → sep=';'. Caracteres Ã± donde iba la ñ → encoding='latin-1'. Números 1.234,56 como texto → decimal=',' y thousands='.'.",
   "El Excel en español exporta así por defecto: no es un archivo roto, es otro dialecto y se declara al cargar. Les va a pasar con el archivo de su empresa, probablemente este mes.",
  ]),
  ("24–55", "Bloque de trabajo: lab_02 por parejas", [
   "Suelta a las parejas (teclado rota) con la lámina de hitos proyectada: cinco minutos de auditoría, separar las 806 con Sales.notna(), los tres conteos, la clínica de activos.",
   "Chuleta para tus rondas: los 6 pedidos intrusos salen de comparar 5 015 contra 5 009; los pedidos devueltos son 296, el 5,9 % de los 5 009.",
   "A los 50 avisa que quedan cinco minutos de código; a los 55 corta para el ataque de fichas aunque falten ejercicios: se terminan en casa.",
  ]),
  ("55–75", "El ataque de fichas", [
   "Demo primero: proyecta la ficha de ejemplo (reactivación de enero) y atácala tú en vivo: ¿por qué 180 días y no 90? ¿quién ejecuta la campaña? ¿qué pasa con los clientes del borde del archivo?",
   "Intercambio: cada equipo entrega su ficha al de al lado; cinco minutos de ataque concentrado en dos campos —unidad de análisis y decisión que cambia—.",
   "Devolución en voz alta de los dos mejores ataques. Si un ataque demuestra que la respuesta no cambia ninguna decisión, la ficha vuelve y se reescribe.",
  ]),
  ("75–81", "Checklist del deber 1", [
   "Recorre la checklist: cuaderno ejecutado con las 806 identificadas, tres ejercicios, tres observaciones con cifra, ficha completa en la última celda, fila nueva de bitácora (el asistente critica tu ficha como gerente).",
   "Primera entrega con nota: los siete deberes suman el 25 %. Tarde: hasta 48 horas con el 70 %. Nombre: lab_02_apellido.ipynb.",
  ]),
  ("81–90", "Empresa confirmada y cierre", [
   "La empresa se confirma hoy y no se cambia. Protocolo de datos: lo real jamás entra a un asistente de IA; se describe la estructura con filas inventadas. La carta de consentimiento está en el sitio.",
   "Teaser del lunes proyectado mientras salen: cambiamos de industria otra vez — Spotify, 32 833 canciones y un promedio que miente dos veces en direcciones opuestas.",
  ]),
 ],
 errores=[
  ("UnicodeDecodeError: 'utf-8' codec can't decode byte 0xf1",
   "Aparece cuando un equipo prueba con el archivo de su propia empresa exportado de Excel en español. Es el momento pedagógico del día: encoding='latin-1' al leer, y de paso revisar sep y decimal. Muéstralo al aula aunque solo le pase a una mesa."),
  ("«El archivo se cargó pero todo quedó en una sola columna»",
   "Separador punto y coma: read_csv(..., sep=';'). Suele venir junto con la coma decimal: si después los números salen como texto '1.234,56', añadir decimal=',' y thousands='.'. No es un archivo roto, es un dialecto: se declara al cargar."),
  ("AssertionError: Deberían quedar 9 994 líneas de pedido…",
   "Filtraron por la columna equivocada (Row ID u Order Date) o borraron ventas reales junto con la basura. La referencia es Sales.notna(): las 806 filas ajenas no tienen venta. Volver a la celda del filtro y releer el mensaje del assert: dice la cifra esperada."),
  ("«Se me murió la sesión en pleno taller y perdí todo»",
   "No se perdió nada: el cuaderno queda, la memoria no. Reconectar, Entorno → Reiniciar y ejecutar todo, y en dos minutos está de vuelta donde iba. Repite la moraleja: por eso el cuaderno debe correr de arriba a abajo.",
  ),
 ],
 si_tarde=[
  "La clínica de activos dentro del cuaderno se deja para casa: los tres conteos y la separación de las 806 son el corazón técnico y no se tocan.",
  "El ataque de fichas no se recorta (es la actividad estrella); si hay que ganar minutos, la devolución en voz alta baja a un solo ataque por equipo.",
  "El bloque de dialectos del CSV puede comprimirse a la lámina de tres síntomas sin demo: reaparece solo cuando algún equipo traiga su archivo real.",
 ],
 alertas=[
  "Fichas cuya «decisión que cambia» quedó vacía o retórica: esos equipos van a la deriva en el proyecto; agenda cinco minutos con cada uno el lunes.",
  "Equipos que salieron sin empresa confirmada: asígnales caso alterno esta semana o la semana 4 los encuentra sin propuesta que presentar.",
  "Quién no entregó el deber 1 al cierre: recordatorio antes de las 48 horas del descuento.",
 ],
),

5: dict(
 titulo="La trampa del promedio · Caso Spotify",
 fecha="31-ago-2026",
 tipo="teoría",
 antes=[
  "presentaciones/sesion-05.html y simuladores/simulador-media-mediana.html abiertos en pestañas separadas.",
  "Cifras de memoria: 32 833 filas / 28 356 canciones, duración 3,76 contra 3,60, popularidad 42,48 contra 45, los 2 703 ceros (8,2 %), p90 = 5,00, p99 = 7,17, y el caso 42,48 contra 39,33.",
  "Revisa las definiciones ambiguas que el aula dio en la semana 2: la apertura conecta «cliente activo» con «canción normal».",
  "Trae la energía del anuncio: al final se presenta el torneo del miércoles y debe sonar a evento, no a tarea.",
  "Revisa quién viene flojo de los labs 1 y 2: el torneo del miércoles es en equipos y conviene repartir a los rezagados entre equipos fuertes.",
 ],
 energia="Esta sesión tiene el material más agradecido del bloque: la media miente dos veces, en direcciones opuestas, con música de por medio. El riesgo es la comodidad —«ya entendí, cola larga infla»— justo antes del segundo giro, así que administra el asombro en dos tiempos y no reveles la popularidad hasta que la duración esté cerrada. El cierre importa emocionalmente: el anuncio del torneo es la primera competencia del curso y define si el miércoles llegan con hambre o con pereza. Véndelo por la gloria, no por la nota.",
 arco="Primero la duración (media que infla), luego la popularidad (media que desinfla), y de las dos sale la regla de la semana: mirar la forma antes de elegir el estadístico. Con la regla instalada entran las herramientas que la operacionalizan —percentiles como umbrales con precio, dispersión y CV, categorías con value_counts— y la sesión culmina con el caso 42 contra 39, que reactiva la unidad de análisis de la semana 2 en versión estadística. El simulador y el anuncio del torneo cierran. La secuencia es de doble giro: no adelantes el segundo.",
 objetivos_salida=[
  "Todos pueden explicar con las manos por qué la cola larga infla la media y el pico de ceros la hunde.",
  "Todos saben leer p90 = 5,00 como una regla con precio: «nada de más de cinco minutos» rechaza exactamente al 10 %.",
  "Todos entienden el caso 42,48 contra 39,33: nadie mintió, cambió la unidad (fila contra canción única).",
  "Todos salen sabiendo las reglas esenciales del torneo: equipos, cifra + estadístico + porqué, IA permitida pero verificada.",
  "Nadie salió creyendo que «la mediana es siempre mejor»: la elección es un criterio según forma y pregunta, no una costumbre nueva.",
 ],
 minuto=[
  ("0–6", "El negocio y la votación de apertura", [
   "Presenta el catálogo: 32 833 canciones con duración, popularidad y género. La pregunta parece trivial y mueve dinero: radios, playlists, regalías.",
   "Votación por rangos: ¿cuánto dura una canción normal? Anota el rango ganador antes de mostrar nada.",
  ]),
  ("6–16", "La media que infla y el montón de ceros", [
   "Dos respuestas del mismo archivo: media 3,76, mediana 3,60. La cola de remixes de 6, 7 y 8 minutos arrastra la media; el 57,9 % queda por debajo de «la típica» si eliges la media.",
   "El dato que un programador quiere de verdad: el 48,7 % del catálogo cae entre 3 y 4 minutos — el formato canción existe y se ve en un histograma.",
   "El giro anunciado: ahora la popularidad. 2 703 canciones con popularidad exactamente cero, el 8,2 %: música que nadie reproduce. Pregunta retórica: ¿qué le hace ese montón a la media?",
  ]),
  ("16–28", "La media que desinfla y la regla de la forma", [
   "Revela: media 42,48, mediana 45 — la media también miente hacia abajo. Sin los ceros sube a 46,29.",
   "El remate es de negocio: «¿qué tan popular es lo que tenemos?» incluye los ceros; «¿qué tan popular es lo que suena?» no. Elegir sin decirlo es elegir el titular.",
   "La regla de la semana con los dos casos lado a lado: antes de elegir el estadístico, mirar la forma. El histograma tarda cuatro segundos y ahorra el ridículo.",
  ]),
  ("28–43", "Percentiles y dispersión", [
   "Un percentil es un umbral operativo con precio: p90 = 5,00 (la regla de los cinco minutos rechaza al 10 %), p99 = 7,17 (más raro que 99 de cada 100). Por grupos: rock corre más largo que rap en todo el recorrido.",
   "El centro sin dispersión es media información: la desviación vive en las unidades del dato; el CV compara sin unidades — duración 0,27, popularidad 0,59. El formato canción es disciplinado; el éxito no tiene formato.",
  ]),
  ("43–56", "Categorías y los promedios que no describen a nadie", [
   "Para categorías: value_counts, casi siempre con normalize=True. La tabla junta presencia y desempeño a propósito: edm tiene más filas (6 043, 18,4 %) y la peor mediana de popularidad (36); pop menos filas y la mejor (52).",
   "Bimodalidad: dos poblaciones en la misma columna y la media cae en el valle, un valor que no le corresponde a nadie. Ejemplo clásico: el ticket promedio cuando conviven minoristas y mayoristas.",
  ]),
  ("56–66", "El caso: Marketing 42, Auditoría 39", [
   "Votación: ¿quién se equivocó? Revela: nadie — 42,48 promedia filas (apariciones en playlists), 39,33 promedia canciones únicas.",
   "Las famosas están hasta en diez playlists y votan diez veces: repetidas 60,2 contra 37,1 las de una sola aparición. Es la unidad de análisis mordiendo en versión estadística.",
  ]),
  ("66–71", "Simulador en vivo", [
   "Abre el simulador media-mediana y arrastra un punto hacia la cola: la media lo persigue, la mediana ni se inmuta. Pide predicciones antes de cada arrastre.",
   "Queda enlazado en el sitio para practicar antes del torneo.",
  ]),
  ("71–82", "El anuncio del torneo", [
   "Sube la energía: es la primera competencia del curso. El contrato: doce preguntas sobre este catálogo, contra reloj, respuesta por equipo con cifra + estadístico + porqué.",
   "La IA está permitida —es la política del curso— pero el número que no coincida con pandas resta: verificar o perder.",
   "Se juega por la gloria y un sticker; la nota sale del cuaderno con las doce respuestas justificadas, no del marcador.",
  ]),
  ("82–90", "Cierre y ronda relámpago", [
   "Cierra con la frase de la semana proyectada. Si sobra tiempo, ronda relámpago: ¿duración típica?, ¿género dominante?, ¿popularidad del catálogo? — para cada una, el estadístico correcto y su porqué.",
   "Es el calentamiento oficial del torneo: que salgan con las tres respuestas dichas en voz alta.",
  ]),
 ],
 errores=[
  ("«¿Entonces la media está mal y hay que usar siempre la mediana?»",
   "El péndulo clásico. No: es un criterio, no una moda. Si media y mediana coinciden, casi cualquier resumen sirve; si se separan, la forma manda y se explica. Y a veces la media es exactamente lo que quieres: para proyectar ingresos totales, la media por el número de casos recupera el total; la mediana no."),
  ("«¿El torneo tiene nota? ¿Y si nuestro equipo pierde?»",
   "El marcador vale cero en la nota: se juega por la gloria y el sticker. Lo que se califica es el cuaderno con las doce respuestas, cada una con estadístico y justificación — un equipo puede perder el torneo y sacar la nota completa. Repítelo: baja la ansiedad y sube la participación."),
 ],
 si_tarde=[
  "La ronda relámpago del cierre desaparece primero; el anuncio del torneo se comprime a las tres reglas esenciales (equipo, tres partes, IA verificada).",
  "El simulador en vivo se cae y queda como tarea enlazada: el arrastre de la media ya quedó demostrado con los dos histogramas.",
  "El bloque de bimodalidad se reduce a una frase con el ejemplo del ticket minorista/mayorista; el caso 42 contra 39 no se recorta jamás: es el corazón de la sesión.",
 ],
 alertas=[
  "Arma esta noche los equipos del torneo repartiendo a los rezagados de los labs entre equipos fuertes: el miércoles no hay tiempo de armarlos en vivo.",
  "Anota quién confundió sistemáticamente media y mediana en la ronda relámpago: son las mesas que visitas primero durante el torneo.",
 ],
),

6: dict(
 titulo="Torneo de las doce preguntas · Taller Spotify",
 fecha="02-sep-2026",
 tipo="taller",
 antes=[
  "Marcador dibujado en la pizarra antes de que entren: equipos en filas, doce casillas de preguntas en columnas. Stickers del premio en el bolsillo.",
  "labs/lab_03.ipynb abierto con el reto de las doce preguntas a mano, y presentaciones/sesion-06.html en la otra pestaña (el deck ocupa ~30 min; el torneo, 55).",
  "Chuleta del árbitro impresa o en segunda pantalla: (1) 32 833 filas / 28 356 únicas; (2) mediana 3,60; (3) más de 5 min = 10,0 %, menos de 2 = 1,3 %; (4) edm 6 043, 18,4 %; (5) IQR de duración; (6) pop lidera por mediana (52); (9) 5:00 = p90 global, p83 en rock, p88 en edm; (10) 8,2 % en cero; (11) repetidas 60,2 contra 37,1.",
  "Los equipos definidos anoche se publican al entrar y se sientan juntos desde el arranque.",
  "Cronómetro visible (proyectado o en la pizarra): el torneo vive del reloj.",
 ],
 energia="Hoy el aula compite por primera vez y el ambiente lo es todo: el torneo debe sentirse como juego serio, no como examen disfrazado. Tu papel cambia: eres árbitro, no profesor —cantas puntos, no explicas—, y la explicación llega después de cada revelación, en veinte segundos, no en cinco minutos. Vigila a los equipos que van perdiendo desde la tercera pregunta: el sistema de puntos premia el criterio sobre la cifra precisamente para que nadie quede fuera por un decimal. Y protege el final: la ceremonia de dos minutos con sticker es ridícula y por eso funciona.",
 arco="Calentamiento con la pregunta del lunes (media o mediana, con la vara de puntuación ya aplicada), reglas y sistema de puntos sin prisa —el torneo vive de ellas—, gestión de expectativas (nota cero, gloria total), y una ronda de ejemplo de tres preguntas de fácil a endiablada que calibra qué es una respuesta completa antes de que el marcador duela. Después, 55 minutos de torneo con las doce preguntas del lab, de una en una, y ceremonia relámpago. La estructura es un embudo: reglas claras primero para que el juego corra solo después.",
 objetivos_salida=[
  "Todos los equipos respondieron las doce preguntas y vieron el marcador completo en la pizarra.",
  "Todas las respuestas del cuaderno llevan las tres partes: cifra, estadístico elegido y porqué basado en la forma.",
  "Al menos un equipo perdió puntos por confiar en una cifra del asistente sin verificarla contra pandas, y el aula vio por qué.",
  "El cuaderno con las doce respuestas justificadas quedó entregado o con plazo claro (lab_03_apellido.ipynb).",
  "El campeón recibió su sticker y el aula sabe que el lunes llega Netflix con una pregunta trampa: ¿cuántos títulos tiene el catálogo?",
 ],
 minuto=[
  ("0–6", "Calentamiento con la vara puesta", [
   "La pregunta del lunes, ahora con puntuación: ¿media o mediana para la duración? Quien conteste «3,76» a secas pierde un punto imaginario: la respuesta completa es mediana 3,60, porque la cola de remixes infla la media.",
   "Esa es exactamente la vara con la que se puntúa todo el torneo: dilo explícito.",
  ]),
  ("6–16", "Reglas y sistema de puntos", [
   "Sin prisa, el torneo vive de ellas: una respuesta escrita por equipo, unos 5 minutos por pregunta, tres partes obligatorias (cifra + estadístico + porqué).",
   "La IA está permitida, pero el número se verifica contra pandas antes de cantarlo: cifra que no coincide, resta.",
   "Puntos: 3 la respuesta completa, 1 la cifra con porqué flojo, 0 la cifra equivocada aunque el porqué suene bonito, 2 para el que roba el porqué que el primero no dio. El marcador vive en la pizarra.",
  ]),
  ("16–19", "Expectativas: gloria, no nota", [
   "El torneo vale cero en la nota: se juega por la gloria, el sticker y el derecho a presumir hasta diciembre.",
   "Lo que se califica es el cuaderno con las doce respuestas justificadas: un equipo puede perder el torneo y sacar la nota completa.",
  ]),
  ("19–33", "Ronda de ejemplo: tres preguntas sin puntos", [
   "Fácil: ¿género con más filas? edm, 6 043, el 18,4 % — y la parte que puntúa: es un conteo con value_counts, variable categórica, no hay media ni mediana que valga.",
   "Media: ¿una canción de 5:00 es «larga»? El giro: es pregunta de posición, no de promedio — p90 del catálogo, pero p83 dentro de rock y p88 dentro de edm. La respuesta completa nombra el grupo de referencia.",
   "Endiablada: ¿Marketing (42) o Auditoría (39)? Nadie miente: filas contra canciones únicas, y las famosas votan hasta diez veces. Calibrado el nivel, arranca el torneo.",
  ]),
  ("33–88", "El torneo: doce preguntas", [
   "Las preguntas salen del reto del lab 3, de una en una, con el cronómetro visible. Recoge las respuestas escritas antes de revelar cada solución.",
   "Canta puntos y explica en veinte segundos, no en cinco minutos; usa la chuleta del árbitro para no depurar código ajeno en vivo.",
   "Administra el reloj: las preguntas 7 (artistas para acumular el 50 %) y 11 (una playlist contra varias) son las largas — anúncialo y da un minuto extra solo ahí.",
   "Pasada la pregunta 6, canta el marcador parcial en voz alta para reactivar a los que van atrás.",
  ]),
  ("88–90", "Ceremonia relámpago", [
   "Anuncia al campeón, entrega el sticker, foto si quieren. Recuerda la entrega del cuaderno hoy.",
   "Teaser del lunes: Netflix, 7 787 títulos… ¿o no? La pregunta trae trampa y la trampa es la semana entera.",
  ]),
 ],
 errores=[
  ("Un equipo canta la cifra del asistente y no coincide con pandas",
   "No lo salves: aplica la regla (resta) y convierte el momento en la lección del día — pide que muestren la celda que la produce y compárala en vivo. Es la demostración de la política de IA del curso que ninguna lámina logra."),
  ("«Se nos murió la sesión de Colab en plena pregunta»",
   "El equipo sigue con la pregunta en papel (cifra estimada + estadístico + porqué valen puntos parciales) mientras uno reconecta y corre Reiniciar y ejecutar todo. El torneo no se detiene por un kernel: esa también es una lección."),
  ("Un equipo se atasca calculando percentiles por género y pide más tiempo",
   "El reloj manda: 5 minutos por pregunta para todos. Recuérdales la forma corta (quantile sobre el subconjunto filtrado) sin escribirla tú, y si no llegan, que entreguen estadístico y porqué: el sistema de puntos premia el criterio precisamente para estos casos."),
 ],
 si_tarde=[
  "El torneo se juega con 8 a 10 preguntas: se recortan la 7 y la 11 (las más largas) y se anuncia que van al cuaderno como tarea.",
  "La ronda de ejemplo baja a una sola pregunta (la de 5:00, que calibra mejor que ninguna).",
  "La ceremonia no se recorta nunca: dos minutos de sticker valen una semana de energía.",
 ],
 alertas=[
  "Anota qué equipos respondieron cifras sin justificación: la vara del torneo es la misma del deber siguiente y conviene decírselo por escrito.",
  "Registra el marcador final: el campeón se menciona en la apertura del lunes y la rivalidad sana se reutiliza en el torneo de groupby de la semana 5.",
  "Quién no entregó el cuaderno al salir: el lunes empieza la semana 4 y arrastrar dos labs es la señal de riesgo más fiable del bloque.",
 ],
),

7: dict(
 titulo="Anatomía y calidad de los datos · Caso Netflix",
 fecha="07-sep-2026",
 tipo="teoría",
 antes=[
  "presentaciones/sesion-07.html y simuladores/simulador-detective-datos.html abiertos en pestañas separadas.",
  "Cifras de memoria: 7 787 filas / 7 786 títulos, 2 389 sin director (30,68 %, el 92,4 % de las series), 5 377 min contra 2 410 Seasons, 88 fechas con espacio, y el daño del dropna: 4 804 títulos, 131 series de 2 410 (94,6 % borradas).",
  "Menciona al campeón del torneo en la apertura: treinta segundos de continuidad que compran atención.",
  "Repasa la historia del duplicado para contarla como cuento: «Consequences», s1486 y s1487, y el espacio no separable \\xa0 invisible en pantalla.",
  "Revisa qué equipos arrastran labs sin entregar: esta semana cierra el bloque y el deber 2 es prerrequisito duro del proyecto.",
 ],
 energia="Esta sesión es una autopsia con clímax: todo el guion converge al fragmento del becario que borra el 94,6 % de las series imprimiendo «impecable». No lo adelantes: la primera media hora debe construir el cariño por los datos (el nulo que significa «no aplica», el duplicado escondido) para que el dropna() duela como se merece. El público objetivo emocional de hoy es el estudiante diligente que confía en la IA: cuando vote «yo firmo esa limpieza» y vea el daño, habrá entendido el curso entero. Trátalo con humor, nunca con burla: el becario es cualquiera de nosotros con prisa.",
 arco="Se abre con la pregunta más fácil del semestre (¿cuántos títulos?) que se desarma en tres láminas —duplicado invisible, 38,3 % con huecos—, sigue el nulo con estructura y los tres tratamientos distintos, la autopsia técnica (dtypes que mienten, duration con dos unidades, fechas con espacio y el coerce que calla), y recién entonces el clímax del fragmento IA con votación previa. El cierre instala las dos defensas —bitácora y cifra de control— y el simulador detective. El orden es una trampa deliberada: primero confían en el archivo, luego en nada, y al final reciben el método para volver a confiar.",
 objetivos_salida=[
  "Nadie sostiene ya que el catálogo tiene 7 787 títulos: todos saben que son 7 786 y por qué.",
  "Todos pueden distinguir los tres nulos —no aplica (director), no se registró (país), sin fuente (reparto)— y su tratamiento distinto.",
  "Todos vieron el daño del dropna() cuantificado: 2 983 títulos, el 94,6 % de las series, sin un error ni un warning.",
  "Todos saben qué exigir frente a un «impecable»: bitácora con justificación y cifra de control con invariantes.",
  "Cada equipo sabe que el miércoles trae su dataset además del laboratorio, y que el deber 2 (bitácora de limpieza más propuesta) cierra la semana.",
 ],
 minuto=[
  ("0–6", "La pregunta más fácil del semestre", [
   "Presenta el dataset en una frase: el catálogo público de Netflix, películas y series, 12 columnas, tal cual salió al mundo.",
   "Votación: ¿cuántos títulos? ¿7 787? La mayoría levantará la mano. Guarda el voto: en tres láminas nadie lo sostiene.",
  ]),
  ("6–20", "7 787 no es la respuesta", [
   "Revela fila a fila: 7 787 filas, 7 786 títulos reales — hay un duplicado que ningún duplicated() ingenuo ve. Y «completos» solo 4 808: el 38,3 % tiene al menos un hueco.",
   "La historia del duplicado como cuento: «Consequences» dos veces, s1486 y s1487, idénticas en todo; la segunda lleva un espacio no separable (\\xa0) al final del título — invisible en pantalla, suficiente para burlar la comprobación.",
  ]),
  ("20–37", "El nulo con estructura y los tres tratamientos", [
   "El nulo más grande: 2 389 títulos sin director, el 30,68 %. Pausa dramática y adelanto: va a resultar el problema más explicable, no el más grave.",
   "¿Dónde vive? Falta en el 92,4 % de las series y el 3 % de las películas: una serie tiene un director por episodio. Significa «no aplica», no «se perdió».",
   "Tres huecos, tres tratamientos: director se conserva y documenta; país lleva centinela «Desconocido» (para que ningún conteo esconda 507 títulos); reparto se queda nulo y pasa a limitaciones. Mismo archivo, tres decisiones.",
  ]),
  ("37–57", "Autopsia técnica: tipos, duration y fechas", [
   "dtypes antes que nada: once de doce columnas como texto. El matiz que separa al analista del robot: show_id como texto es CORRECTO — s1486 es etiqueta, no cantidad.",
   "El problema de tipos perfecto: «90 min» y «2 Seasons» en la misma columna, con estructura perfecta (5 377 películas / 2 410 series). No es ruido, es diseño: dos variables disfrazadas — se separa en dos columnas numéricas.",
   "Las fechas: 88 traen un espacio delante. Con formato explícito la conversión explota — bien, el error avisa. La salida cómoda, errors='coerce', convierte y calla: 98 NaT donde solo 10 eran nulos reales. El coerce borró 88 fechas verdaderas sin decirlo.",
  ]),
  ("57–68", "El clímax: el fragmento del becario", [
   "Proyecta las tres líneas del fragmento IA (to_datetime con coerce, dropna, drop_duplicates) y cuenta que corre sin errores y termina en «impecable». Votación: ¿quién lo firma? Deja que se comprometan.",
   "Revela la cifra de la sesión: de 2 410 series sobreviven 131 — el dropna() global borró el 94,6 % de las series, porque el nulo del director vivía justo ahí. Quedan 4 804 títulos de 7 787.",
   "El remate doble: borró 2 983 filas que no debía y conservó la única que sobraba — el duplicado de «Consequences» sobrevivió porque su espacio invisible lo hacía «distinto».",
  ]),
  ("68–79", "Las defensas y el simulador", [
   "La bitácora de limpieza: una fila por decisión —problema, filas, decisión, justificación—; la justificación es la columna que casi nadie escribe y la que se califica.",
   "La cifra de control: invariantes antes y después (7 787 → 7 786 con la baja identificada por show_id; los 10 sin fecha siguen siendo 10). Frente a un «impecable»: demuéstralo.",
   "Abre el simulador detective y juega una ronda en vivo: el aula canta los problemas a medida que los ve. Queda enlazado para afilar el ojo antes del miércoles.",
  ]),
  ("79–90", "Cierre operativo del bloque", [
   "El miércoles: inventario con porcentajes exactos, bitácora, cifra de control y el ejercicio del error incrustado (está en la política de IA del curso). El deber 2 se entrega al cierre.",
   "Semana grande de proyecto: bitácora de limpieza del dataset propio más la propuesta formal con diagnóstico de madurez. Recuérdales traer su dataset el miércoles.",
   "Deja la última lámina proyectada mientras salen: el miércoles se cierra el primer bloque del curso.",
  ]),
 ],
 errores=[
  ("«¿Y por qué no rellenamos también el director con 'Desconocido', como el país?»",
   "Es la pregunta buena de la sesión: porque significan cosas distintas. El país existe y no se registró (centinela); el director de una serie no existe como dato único (no aplica: se documenta). Imputar un «no aplica» es fabricar 2 389 datos falsos. Si nadie la hace, plántala tú."),
  ("«¿Pero dropna() no es lo estándar? Lo he visto en todos los tutoriales»",
   "Cierto, y por eso es la línea más peligrosa del pandas generado por IA: no falla nunca y decide por ti que toda fila incompleta sobra. La versión honesta lleva subset y una decisión previa por columna. El miércoles lo van a medir ellos mismos: 2 983 títulos por una línea de tutorial."),
 ],
 si_tarde=[
  "El simulador detective se cae primero: queda enlazado como preparación del taller.",
  "La autopsia de fechas se comprime: muestra solo el contraste 98 contra 10 NaT sin recorrer el error completo; el lab del miércoles la repite entera.",
  "El clímax del fragmento no se recorta ni se apura jamás: si vas muy tarde, sacrifica la ronda del simulador y parte del cierre operativo, y manda los avisos por el foro.",
 ],
 alertas=[
  "Anota quiénes votaron «yo firmo» la limpieza del becario: son tus aliados pedagógicos del miércoles — pídeles en el taller que cuenten qué los convenció.",
  "Equipos que aún no traen dataset propio: el miércoles necesitan uno para la bitácora del deber 2; resuélvelo hoy con un caso alterno.",
  "Quien arrastra labs sin entregar llega al cierre del bloque en riesgo real: mensaje individual hoy, no el viernes.",
 ],
),

8: dict(
 titulo="Inventario, bitácora y error incrustado · Taller Netflix",
 fecha="09-sep-2026",
 tipo="taller",
 antes=[
  "labs/lab_04.ipynb abierto en Colab con la primera celda ejecutada; presentaciones/sesion-08.html en la otra pestaña (el deck ocupa ~20 min al inicio y ~30 al final).",
  "Cifras del árbitro: 30,68 % sin director, 88 fechas con espacio (98 NaT con coerce, 10 reales), 5 377/2 410 en duration, duplicado s1487, y el daño del fragmento: 4 804 títulos, 131 series, 2 983 borrados.",
  "Ten localizados a los que votaron «yo firmo» el lunes: hoy abren el bloque del error incrustado contando qué los convenció.",
  "Verifica que cada equipo trae su dataset propio: la bitácora del deber 2 se escribe hoy sobre datos reales del proyecto.",
  "Prepara la transición final: el anuncio de Comercial Andina (ventas.csv, 80 515 líneas, seis sucursales) es el puente al resto del curso.",
 ],
 energia="Hoy cierra el primer bloque y la sesión debe dejar la sensación de método completo: cuatro industrias, cuatro lecciones, un protocolo. El pico emocional es el error incrustado —está anunciado en la política de IA del curso y es la primera vez que cazan un fallo de la IA con cronómetro—: adminístralo como caza, no como demostración tuya; el daño lo miden ellos y tú solo revelas cuando todos tienen cifras. Cuida al equipo que no encuentra el fallo: la pista mínima es «¿cuántas series quedaron?», y con eso llega cualquiera. El anuncio final de Comercial Andina debe sonar a graduación: se acabó el entrenamiento, empieza el negocio.",
 arco="Apertura conceptual corta («los datos están sucios» no es diagnóstico), el plan de trabajo con las respuestas a la vista —los ocho problemas y sus porcentajes son control de calidad, no spoiler—, bitácora y cifra de control como contrato de la sesión, y 33 minutos de taller sobre el cuaderno. La segunda mitad es el error incrustado en dos tiempos (medir, luego reportar con plantilla), la checklist del deber 2 y el cierre de bloque con el recuento de las cuatro industrias y el anuncio de Comercial Andina. El taller va antes que el error incrustado a propósito: solo quien ya limpió bien puede medir lo que la limpieza mala destruye.",
 objetivos_salida=[
  "Todos produjeron el inventario de calidad con porcentajes exactos y pasaron la Comprobación 1 (7 786 títulos, 10 NaT, columnas por unidad).",
  "Todas las parejas cuantificaron el daño del fragmento IA: 2 983 títulos, 94,6 % de las series, 88 fechas rematadas por el coerce.",
  "Cada equipo dejó iniciada la bitácora de limpieza de su propio dataset con al menos tres filas justificadas.",
  "El deber 2 quedó entregado o con checklist clara (lab_04_apellido.ipynb más bitácora del proyecto).",
  "Todos pueden recitar la lección de cada industria del bloque: métrica (pizzería), unidad (retail), forma (música), auditoría (streaming).",
 ],
 minuto=[
  ("0–6", "«Los datos están sucios» no es un diagnóstico", [
   "Abre con la frase que van a escuchar toda la vida profesional y vota: ¿es un diagnóstico? Revela: no — un diagnóstico dice qué problema, cuántas filas y qué porcentaje.",
   "Un problema del 0,1 % se trata distinto que uno del 30 %: del porcentaje sale la decisión.",
  ]),
  ("6–13", "El plan con las respuestas a la vista", [
   "Proyecta los ocho problemas y sus porcentajes exactos. No es spoiler, es control de calidad: si al equipo no le cuadran estos números, su inventario está mal — o encontró algo nuevo, y ambas cosas se discuten.",
   "Recuerda las cifras de partida: se guardan ANTES de tocar nada, porque sin ellas no hay cifra de control al final.",
  ]),
  ("13–22", "Bitácora y cifra de control: el contrato de hoy", [
   "El contraste que explica la bitácora solo: «se limpiaron los nulos» (¿cuáles, cuántos, por qué así?) contra la fila auditable con problema, filas, decisión y justificación. La justificación es la columna que se califica.",
   "La cifra de control con invariantes: 7 787 → 7 786 con la única baja identificada (s1487); películas y series intactas; los 10 sin fecha siguen siendo 10 — si ves 98, convertiste sin strip.",
  ]),
  ("22–55", "Bloque de trabajo: lab_04 por parejas", [
   "Suelta a las parejas (teclado rota) con los hitos proyectados: radiografía y cifras de partida, fechas con strip (verificar 10 NaT, ni uno más), separar duration en dos columnas, tres nulos con tres tratamientos, cazar el duplicado con normalización.",
   "En tus rondas exige leer los mensajes de error en voz alta antes de ayudar: a esta altura del curso el mensaje casi siempre trae la solución.",
   "A los 45 avisa que quedan diez minutos; a los 55 corta aunque falte el guiado de rating y listed_in: se termina en casa.",
  ]),
  ("55–68", "El error incrustado: la caza", [
   "Proyecta el fragmento del becario y da diez minutos de caza con una sola consigna: no me digan qué está mal, díganme cuánto cuesta. Pista mínima para mesas atascadas: ¿cuántas series quedaron?",
   "Pide cifras a dos o tres mesas ANTES de revelar. Luego confirma: 2 983 títulos borrados (38,3 %), 131 series de 2 410 (94,6 %), 88 fechas reales fabricadas como NaT por el coerce y rematadas por el dropna. Y el duplicado sobrevivió.",
  ]),
  ("68–78", "El reporte del daño con plantilla", [
   "Recorre la plantilla punto por punto: la línea culpable (dropna sin subset), lo que borró, lo que fabricó el coerce, qué análisis quedan sesgados para siempre (mix películas/series, títulos por año) y la corrección honesta (subset tras decidir por columna, strip antes de convertir).",
   "Cierra con la moraleja de la política de IA: el fragmento venía de un asistente, corría perfecto y decía «impecable» — la defensa no es no usar IA, es bitácora y cifra de control.",
  ]),
  ("78–84", "Checklist del deber 2", [
   "Recorre la checklist: inventario con porcentajes, bitácora de ocho filas más las del guiado, cifra de control cuadrada, daño del fragmento cuantificado, y la fila de bitácora de prompts (el asistente revisa tu limpieza).",
   "La parte de proyecto: bitácora de limpieza del dataset propio más la propuesta formal con diagnóstico de madurez. Es prerrequisito duro: todo lo demás corre sobre esta tabla. Nombre: lab_04_apellido.ipynb.",
  ]),
  ("84–90", "Cierre de bloque y el gran anuncio", [
   "El recuento con el aula completando cada frase: ¿qué enseñó la pizzería? (la métrica decide el ranking) ¿el retail? (la unidad decide el conteo) ¿la música? (la forma decide el estadístico) ¿el streaming? (nada sobrevive a datos sin auditar).",
   "El anuncio, proyectado mientras salen: se acabó el circuito de entrenamiento — desde el lunes entra Comercial Andina, el distribuidor ecuatoriano con seis sucursales y 80 515 líneas de venta, con todos los problemas de estas cuatro semanas juntos en los mismos archivos.",
  ]),
 ],
 errores=[
  ("ValueError: time data ' August 4, 2017' doesn't match format '%B %d, %Y'",
   "Es el error pedagógico central del lab: el espacio inicial delante de la fecha. La solución correcta es str.strip() antes de to_datetime con formato explícito — NO errors='coerce', que convierte y calla. Verificación obligatoria: deben quedar 10 NaT; si ven 98, convirtieron sin strip."),
  ("«Me salen 98 NaT en fecha_agregado en vez de 10»",
   "Convirtieron sin strip: el coerce se tragó 88 fechas reales. Es exactamente el fallo sutil del fragmento del becario, así que no lo arregles tú — señala la celda de verificación y deja que lo descubran: les sirve entero para el desafío."),
  ("IntCastingNaNError: Cannot convert non-finite values (NA or inf) to integer",
   "Intentaron astype(int) sobre duracion_min o temporadas, que por diseño tienen nulos (la mitad que no aplica). La salida del cuaderno usa where() sobre el extract; si insisten en enteros, el tipo es Int64 con mayúscula. Aprovecha para repetir: ese nulo es diseño, no suciedad."),
  ("«Se me reinició el kernel y perdí las cifras de partida»",
   "Nada se perdió: N_TITULOS_0 y compañía se definen en una celda al inicio, antes de cualquier cambio. Reiniciar y ejecutar todo las reconstruye en segundos. Moraleja en voz alta: por eso las cifras de partida viven en el cuaderno y no en la memoria de nadie."),
 ],
 si_tarde=[
  "El reto 🎯 (la trampa entre equipos) se cae primero y el guiado de rating y listed_in se va a casa.",
  "El bloque de trabajo puede comprimirse a 25 minutos cortando la caza del duplicado (queda demostrada en el deck del lunes).",
  "El error incrustado NO se recorta: está comprometido en la política de IA del curso (semanas 4 y 14). Si el tiempo aprieta, la plantilla de reporte se llena a dos voces contigo escribiendo.",
 ],
 alertas=[
  "Bitácoras sin justificación escrita: es la columna que se califica en el deber 2; avisa por escrito a los equipos que la dejaron vacía.",
  "Equipos sin propuesta de proyecto o sin diagnóstico de madurez: la semana 5 arranca sobre Comercial Andina y el proyecto queda sin cimiento si esto no cierra ya.",
  "Anota qué parejas encontraron el fallo sin pista: son candidatas a liderar la consultoría cruzada de la semana 15, y el dato sirve para armar los equipos del torneo de groupby.",
 ],
),
}
