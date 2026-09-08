# Narrativa de la sesión 5. La trampa del promedio

Material para ensayar en voz alta y contra cronómetro. No es un guion completo de los 90 minutos, es lo que se dice palabra por palabra en los momentos que deciden la sesión, más el mapa que sostiene el resto. El minutado operativo está en `guia_profesor.md`.

## La promesa

En una frase: al salir de esta sala vas a poder detectar, en tres minutos y con dos números, cuándo un promedio está mintiendo, y vas a saber qué número pedir en su lugar.

Anclaje de pasión: esta trampa no es teórica. Con este mismo dataset, el promedio le pone el umbral de una promoción donde siete de cada diez pedidos ni llegan. Es la clase de error que uno comete con toda la aritmética correcta.

Guion de los primeros sesenta segundos, para leer creyéndolo:

"Buenos días. Hoy no les voy a enseñar matemática nueva. El promedio lo aprendieron en el colegio y lo saben calcular desde los doce años. Lo que les voy a enseñar hoy es a desconfiar de él. Al salir de esta sala van a poder detectar, en tres minutos y con dos números, cuándo un promedio está mintiendo, y van a saber qué número pedir en su lugar. Eso, en una empresa real, vale una promoción entera: hoy van a ver un caso donde la diferencia es de tres a uno. Y lo van a ver apostando: en esta clase se apuesta antes de calcular."

Lo que se corta de la apertura y por qué: nada de repasar la sesión anterior (la página 1 del taller la conecta sola), nada de agenda del día (el arco se descubre, no se anuncia), nada de anécdotas personales de apertura (la pasión va en el caso, no antes).

## El arco

Tensión: María, gerente regional de Superstore, pide tres números "fáciles" para su comité de las 10h00. El grupo apuesta sus respuestas en los candados de las páginas y los datos las contradicen las tres veces, cada vez por una razón distinta.

Demostración: caso Superstore en tres actos, cada uno con el ciclo apuesta, cálculo en vivo, sorpresa, decisión. Acto 1, el pedido típico para el umbral del envío gratis ($459 contra $152, 72.5 % bajo la media). Acto 2, la categoría estrella (el duelo se voltea al cambiar de estadístico). Acto 3, la trampa inversa (la mediana defiende a Libreros y el total la desmiente).

Resolución: la regla de la casa, ningún promedio sin su distribución, la página 6 donde cada estudiante escribe el memo que María lleva al comité, y el encargo final: un reporte de cinco diapositivas para el VP, donde cada quien repite el detector en una región elegida.

Distribución del tiempo: apertura y tensión, minutos 0 a 20 (incluye escalera y muro de datos). Demostración, minutos 20 a 62, en bloques de menos de doce minutos, cada uno cerrado con señal verbal. Resolución, minutos 62 a 90, que es el taller más el cierre.

## El marco STAR

Símbolo: el histograma con las dos líneas verticales, la roja (media) lejos de la punteada (mediana). Está en la slide 7, en la página 3 del taller y en el cuaderno opcional de Colab. Quien vea dos líneas separadas sobre un histograma debe recordar esta clase.

Eslogan: "Ningún promedio sin su distribución." Alternativas si esa no prende: "El promedio es un resumen, no la verdad" y "Si media y mediana pelean, mira el histograma". La primera es la oficial, pasa la prueba del pasillo y cabe en un memo.

Sorpresa: el 72.5 % de los pedidos vale menos que el pedido "promedio". Rompe el supuesto de que el promedio parte al grupo por la mitad. La sorpresa de respaldo es el acto 3: la mediana también sabe mentir.

Idea saliente, una sola: un estadístico de centro sin su distribución no resume, adivina. Todo lo demás de la sesión (percentiles, dispersión, moda) orbita esa idea.

Narrativa: María, gerente regional, te llama a las 8h02 porque a las 10h00 decide un precio, una compra y una subcategoría. Personal (tiene nombre, hora y chat pendiente) y universal (todo el que trabaje con datos recibirá ese mensaje alguna vez).

## El cierre

La diapositiva final es la 14, contribuciones, y se queda proyectada durante las preguntas. Espeja la promesa: prometí que detectarías promedios mentirosos, te llevas el detector (media contra mediana), la regla (ningún promedio sin su distribución), el mapa (la escalera) y tres decisiones salvadas.

Guion del último minuto:

"Recuerden dónde empezamos: les prometí que hoy saldrían sabiendo detectar un promedio mentiroso en tres minutos. El detector ya lo tienen: pidan la media y la mediana, y si se alejan, pidan el histograma. La regla de la casa cabe en una línea: ningún promedio sin su distribución. María ya les dejó el encargo en la última página: el reporte de cinco diapositivas se entrega en el buzón antes del miércoles, y el miércoles mismo hacemos perfilado contra reloj, así que traigan la laptop. La próxima vez que un promedio los mire a los ojos, ya saben qué pedirle. Nos vemos el miércoles."

Palabras finales, tres opciones con recomendación: la recomendada es la frase que marca el final ("La próxima vez que un promedio los mire a los ojos, ya saben qué pedirle. Nos vemos el miércoles."), porque cierra el círculo con el caso. Segunda opción, el chiste, que al cierre sí se permite ("Desde hoy, cuando alguien les diga 'en promedio', ustedes contestan 'muéstrame el histograma'. Van a perder amigos, pero tomarán mejores decisiones."). Tercera, el saludo específico ("Que Galápagos les dé esta semana mejores distribuciones que promedios."), solo si el ambiente del grupo lo pide.

## Dónde puede fallar esto

La apuesta 1 puede caer cerca del promedio real y desinflar la sorpresa. Mitigación: la sorpresa no es el valor sino el 72.5 % bajo la media; pivota ahí, esa segunda apuesta casi siempre sale "cincuenta por ciento".

El grupo escarmentado puede oler la trampa del acto 3 y responder "mediana" sin pensar. Mitigación: esa es exactamente la trampa; pide que firmen o no firmen el memo antes de mostrar el total, y deja que el total los contradiga.

Brightspace puede fallar con el wifi. Mitigación: los tres reveals están en las slides 7, 9 y 11; la sesión corre completa con pizarra, mano alzada y slides, y el memo se escribe en papel.
