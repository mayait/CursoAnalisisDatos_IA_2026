# ADM 2003 Sesión 05. La trampa del promedio

## Ficha

| Duración | Modalidad | Tamaño de grupo | Materiales necesarios | Preparación previa del profesor (minutos) |
|---|---|---|---|---|
| 90 minutos (85 de contenido más 5 de holgura declarada) | Presencial, sala con proyector y luces plenas | 20 a 35 estudiantes | Proyector con `S5_Trampa_Promedio.pptx`; pizarra con 2 marcadores (uno rojo, uno negro); 1 dispositivo por estudiante o por pareja (laptop o celular: las páginas corren en cualquier navegador); las 7 páginas del taller (`brightspace/s05_p1..p7`) subidas a Brightspace como archivos en Contenido, Semana 3, en orden; `superstore_2026.csv` subido a la misma carpeta de Manage Files (el botón Descargar de la página 2 lo enlaza en relativo, sin mostrar el origen) | 20: subir las 7 páginas, abrirlas en el visor de Brightspace y probar los 6 candados de corrido, repasar los reveals en las slides 7, 9 y 11 por si falla el wifi |

Nota de publicación: los candados impiden ver las gráficas sin responder, pero no impiden que un curioso avance solo. Sube las 7 páginas con **fecha de disponibilidad a la hora de clase** (lunes 31, inicio de sesión) y quedas cubierto. La entrega es el reporte de la página 7 (El encargo de María, cinco diapositivas en PowerPoint): crea el buzón **Taller 5 · Reporte para María** antes de clase.

## Lo que el estudiante podrá hacer al salir

Dado un conjunto de datos de negocio, calcular media y mediana de la variable correcta en la unidad de análisis correcta, decidir cuál reportar mirando el histograma, y explicar la decisión en lenguaje de gerente en tres líneas escritas.

## La promesa de apertura

Léela casi literal, con la slide 1 proyectada, antes del minuto uno:

"Buenos días. Hoy no les voy a enseñar matemática nueva. El promedio lo aprendieron en el colegio y lo saben calcular desde los doce años. Lo que les voy a enseñar hoy es a desconfiar de él. Al salir de esta sala van a poder detectar, en tres minutos y con dos números, cuándo un promedio está mintiendo, y van a saber qué número pedir en su lugar. Eso, en una empresa real, vale una promoción entera: hoy van a ver un caso donde la diferencia es de tres a uno. Y lo van a ver apostando: en esta clase se apuesta antes de calcular. De hecho, las páginas del taller no les muestran ninguna gráfica hasta que apuesten."

Nada de chistes, agradecimientos ni disculpas antes de la promesa.

## Dónde se pierden

1. Confunden "la media engaña" con "la media está mal calculada". Señal: alguien pregunta si la página calculó mal o propone "recalcular bien el promedio". Maniobra: contraejemplo en pizarra con cinco sueldos, cuatro de $1,000 y uno de $21,000; la media es $5,000, la aritmética es perfecta y el resumen es pésimo. El problema nunca fue el cálculo, fue la elección del estadístico.

2. Tras las páginas 3 y 4 sobrecorrigen y coronan a la mediana como "el número bueno". Señal: en la página 5 responden "no firmo, la mediana debe ser positiva" en automático, antes de ver el total. Maniobra: no los corrijas en ese momento; esa confianza es la materia prima de la trampa inversa. Deja que el total de Libreros (−$3,473 con mediana positiva) haga el trabajo, y nómbralo: la mediana ignora los tamaños.

3. En la muestra de 9 pedidos de la página 3 calculan mal la mediana: promedian los dos del centro, toman el quinto sin ordenar, o dividen la suma para 2. Señal: medianas reportadas distintas de $125 (típico: $167, el quinto sin ordenar). Maniobra: no expliques de nuevo; pide que canten los 9 valores ordenados en voz alta y que señalen cuál parte la fila en dos mitades de cuatro.

## Minutado

| Min | Bloque | Qué hace el profesor | Qué hace el estudiante | Señal verbal de cierre |
|---|---|---|---|---|
| 0–4 | Apertura y promesa (slides 1 y 2) | Lee la promesa casi literal; presenta los dos números de la portada sin explicarlos | Escucha | "Esa es la promesa. Primero, el mapa." |
| 4–12 | La escalera (slide 3 de respaldo) | Dibuja la escalera en la pizarra escalón por escalón, con un ejemplo de Superstore en cada uno; construye la cerca: descriptivo no es básico | Abre la página 1, responde su candado (clasificar la pregunta de María); preguntas rápidas 1 y 2 | "Ese es el mapa del semestre. Hoy, escalón uno. Conozcamos a María." |
| 12–17 | El caso (slide 4; páginas 1 y 2) | Teatraliza los mensajes de María; presenta la regla de casino: ninguna gráfica se abre sin apostar | Lee la llamada de María; responde el candado de la página 2 (el archivo) | "9,994 filas y María espera un número. Veamos qué le entregaron." |
| 17–20 | El muro de datos (slide 5, hapax) | Proyecta el muro y calla 20 segundos; luego: nadie ve los datos, por eso se resume | Observa; responde la pregunta rápida 3 | "Para eso existe la estadística descriptiva. Primera pregunta de María." |
| 20–26 | Microcaso 1, la muestra a mano (slide 6; página 3) | Corre el microcaso 1: todos calculan media y mediana de los 9 pedidos y los escriben en los campos; anota 3 o 4 resultados en la pizarra | Calcula a mano, llena los dos campos, apuesta el porcentaje | "Campos llenos. Abran el candado." |
| 26–32 | Reveal 1 (slide 7; página 3 abierta) | Proyecta el histograma al abrirse el candado; narra la cola larga, el pedido Cisco de $23,661 y la decisión del umbral (≈$200, no $459) | Compara sus números con los reales; responde la pregunta rápida 4 | "Primera trampa cazada: cola larga. Era la primera de tres." |
| 32–36 | Microcaso 2, el duelo (slide 8; página 4) | Corre el microcaso 2 con votación a mano alzada antes de que respondan el candado; anota los votos | Vota, defiende su voto en una frase, abre el candado | "Votos cerrados. Veamos el duelo con dos árbitros." |
| 36–44 | Reveal 2 (slide 9; página 4 abierta) | Proyecta el duelo; muestra en la página las encuadernadoras de $5,000 y la media sin las 20 mejores líneas; decisión: productos, no categorías | Lee el reveal; responde la pregunta rápida 5 | "Segunda trampa: los extremos mandan sobre la media. Queda la peor." |
| 44–48 | Microcaso 3, el memo (slide 10; página 5) | Lee el memo con voz de auditor; parejas 2 minutos; vota quién firma | Discute en pareja, decide su firma en el candado | "Las dos cifras del memo son correctas. Veamos si la conclusión también." |
| 48–58 | Reveal 3 y diagnóstico (slide 11; página 5 abierta) | Proyecta Libreros; narra la trampa inversa y la tabla por descuento de la página; guion del pivote y del puente a diagnóstico | Lee el reveal; propone hipótesis del porqué antes de mirar la tabla de descuentos | "La decisión no era matar Libreros, era revisar descuentos. Y acabamos de subir al escalón dos sin pedir permiso." |
| 58–62 | La regla de la casa (slide 12) | Presenta el eslogan y lo hace leer en voz alta; pregunta rápida 6 | Lee el eslogan; responde a mano alzada | "Esa es la regla. Ahora les toca a ustedes: página 6." |
| 62–70 | Página 6: la última apuesta | Circula; caza el error 3 de "Dónde se pierden" en los rezagados de la página 3 | Responde el candado del segmento de oro y lee el marcador de la mañana | "Cinco minutos y María entra al comité: le deben un memo." |
| 70–80 | El memo a María (slide 13) | Circula; recuerda: tres líneas, un número por pregunta, idioma de comité; presenta el encargo de la página 7 (reporte de 5 diapositivas para el VP, entrega el miércoles) | Escribe el memo en la página 6: será la primera diapositiva de su reporte | "Dejen el memo donde esté: quiero oír dos." |
| 80–85 | Puesta en común y cierre (slide 14) | Pide dos memos leídos en voz alta y los comenta contra la regla de la casa; proyecta contribuciones; lee el cierre | Dos personas leen su memo; el resto compara con el suyo | El guion del último minuto (sección Cierre) |
| 85–90 | Holgura declarada | Absorbe demoras de Brightspace y de la puesta en común | | |

La suma da 85 minutos de contenido más 5 de holgura. "Escucha" aparece en 1 de 14 bloques de contenido.

## Guion de los momentos difíciles

El pivote de la trampa inversa, decirlo con precisión al cerrar el reveal 3: "Ojo con lo que acaba de pasar. En las dos primeras preguntas la mentirosa era la media y la mediana los rescató. Aquí la mediana les dijo que la venta típica gana plata, y es verdad, y aun así la subcategoría pierde $3,473. Las dos cifras del memo eran correctas. Ningún número de centro es el bueno; el bueno es el que elijas después de mirar la distribución."

El puente a diagnóstico, inmediatamente después: "Y noten esto otro: para defender a Libreros tuvimos que preguntar por qué pierde. Esa pregunta ya no es descriptiva, es diagnóstica. Acabamos de subir un escalón sin darnos cuenta. Así se sube la escalera: no por ambición, por necesidad."

La promesa y el último minuto están escritos en sus secciones; no los improvises.

## Pizarra

Tercio izquierdo, desde el minuto 4: la escalera, cuatro peldaños ascendentes con sus preguntas (¿qué pasó?, ¿por qué?, ¿qué va a pasar?, ¿qué hacemos?), en negro, con "HOY" en rojo sobre el primero. No se borra en toda la sesión.

Centro, desde el minuto 20: la tabla del marcador, tres filas (pedido típico, categoría, Libreros) por tres columnas (apuestas del grupo, media, mediana). Se llena en vivo en cada reveal, media en rojo, mediana en negro. Al final la tabla muestra sola la moraleja: en las filas 1 y 2 engaña la media, en la 3 la mediana. (La página 6 trae esta misma tabla impresa: que la comparen con la de la pizarra.)

Tercio derecho, minuto 58: el eslogan "Ningún promedio sin su distribución", en rojo, enmarcado. Queda visible hasta el final.

## Microcasos y preguntas en vivo

Los tres microcasos son los candados de las páginas 3, 4 y 5: la página obliga a comprometerse por escrito antes de ver nada, y tu trabajo es convertir ese compromiso individual en discusión pública.

### Microcaso 1. La muestra a mano
**Minuto:** 20
**Tipo:** predicción
**Formato:** individual en los campos de la página 3, 3 o 4 resultados en voz alta
**Tiempo:** 6 minutos, más el reveal en el bloque siguiente

**La situación.** María quiere lanzar "envío gratis desde $X" y pide el valor del pedido típico para fijar la X. Antes de calcular sobre los 5,009 pedidos, cada estudiante calcula a mano la media y la mediana de una muestra de 9 pedidos reales (la página los trae, con un pedido de $2,256: una oficina amoblándose entera), y apuesta qué porcentaje de los 5,009 queda bajo el promedio.

**La pregunta.** ¿Cuánto dan la media y la mediana de los 9, y qué porcentaje de los pedidos reales queda por debajo del promedio?

**Lo que se espera que digan:** media $365 y mediana $125 los que calculan bien; en el porcentaje, casi unánime "cincuenta por ciento, más o menos".
**El error productivo:** dos, y los dos sirven. La mediana mal calculada ($167, el quinto sin ordenar) enseña qué es ordenar; el "cincuenta por ciento" es la intuición de simetría que el 72.5 % va a romper.
**Qué hacer con cada una:** anota 3 o 4 pares (media, mediana) en la pizarra sin corregir. Si aparece $167, pide cantar los valores ordenados en voz alta. Al "cincuenta por ciento", sonríe y di "queda apuntado".
**El puente:** "Su muestra de 9 ya contenía la trampa completa. Abran el candado y mírenla a escala."

### Microcaso 2. El duelo de categorías
**Minuto:** 32
**Tipo:** predicción con decisión
**Formato:** votación a mano alzada antes de tocar la página 4, dos defensas orales de una frase
**Tiempo:** 4 minutos

**La situación.** Segunda pregunta de María: quiere duplicar el inventario de la categoría más rentable por línea de venta, y la pelea es entre Muebles y Suministros de Oficina. Quien gane se lleva el presupuesto de compras del trimestre. Ya vieron que el promedio puede engañar, así que esta vez el voto es con advertencia.

**La pregunta.** ¿Qué categoría deja más utilidad por línea de venta: Muebles o Suministros de Oficina?

**Lo que se espera que digan:** voto dividido, con ligera mayoría por Suministros (papel se vende siempre). Alguno elegirá la tercera opción de la página, "depende del estadístico": celébralo sin resolverlo.
**El error productivo:** votar por una categoría, cualquiera, sin preguntar con qué estadístico se decide el duelo. Ese es el punto: la respuesta cambia según el árbitro.
**Qué hacer con cada una:** cuenta los votos y anótalos. A las dos defensas orales, respóndeles solo "¿y eso lo mide la media o la mediana?". Deja la pregunta flotando y que abran el candado.
**El puente:** "Votos cerrados. Primero el duelo según la media... y después lo repetimos con otro árbitro."

### Microcaso 3. El memo de auditoría
**Minuto:** 44
**Tipo:** error plantado
**Formato:** parejas 2 minutos, luego votación a mano alzada, luego el candado de la página 5
**Tiempo:** 4 minutos

**La situación.** Proyecta la slide 10 y lee con voz de auditor: "Libreros acumuló una pérdida neta de $3,473 en cuatro años, con una utilidad media de −$15.23 por línea. Recomendación: descontinuarla." Advierte una sola cosa: las dos cifras son correctas, verificadas. El error del memo, si existe, no está en los números.

**La pregunta.** ¿Firmas el memo, sí o no, y con qué evidencia adicional defenderías tu firma?

**Lo que se espera que digan:** mayoría "no firmo, la mediana debe ser positiva", que es correcto e insuficiente: la mediana ES positiva (+$4.13) y la subcategoría pierde de verdad. Una minoría firmará "porque el total es el total".
**El error productivo:** el "no firmo por la mediana". Aplaude el reflejo y déjalo caer: cuando el reveal muestre que aun con mediana positiva Libreros pierde $3,473, el grupo entiende que ningún centro basta solo. Los que firmaron también aciertan a medias: el total es real, la conclusión de matar la subcategoría es la que falla.
**Qué hacer con cada una:** haz explícitas las dos posturas antes de abrir el candado ("aquí hay quien confía en la mediana y quien confía en el total; los dos tienen medio argumento"). Tras el reveal, cierra con el guion del pivote.
**El puente:** "Ni la media ni la mediana: la distribución. Y la distribución apunta a los descuentos."

### Preguntas rápidas

1. Minuto 6: "En una palabra: ¿en qué escalón vive '¿cuántas unidades vendimos ayer?'?" (descriptivo; verifica que la escalera entró).
2. Minuto 11: "Mano alzada: ¿su proyecto de equipo ya tiene al menos una pregunta de escalón uno escrita?" (conecta con el caso grupal).
3. Minuto 19, frente al muro: "En una palabra: ¿qué sienten al ver esta tabla?" (busca "mareo", "nada"; es el pie para 'nadie ve los datos').
4. Minuto 30: "Mano alzada: ¿a quién la mediana de la muestra le dio $167 en vez de $125? ¿Qué faltó hacer?" (ordenar; sin vergüenza: es el error clásico).
5. Minuto 43: "En una palabra: ¿qué le hace una venta de $5,000 a la media de su categoría?" ("la arrastra", "la infla").
6. Minuto 57: "Mano alzada y con honestidad: ¿quién habría firmado el memo a las 8 de la mañana, antes de esta clase?" (la mayoría; nómbralo como progreso, no como vergüenza).

## Plan B

Si al minuto 20 no has terminado la escalera, corta el bloque del caso (12–17) a dos minutos: lee los mensajes de María sin teatro y deja que la página 2 haga el trabajo; el muro de datos (17–20) no se corta, es el hapax de la sesión.

Si al minuto 48 no has lanzado el microcaso 3, recorta el reveal 2 (36–44) a su mitad: proyecta el duelo, nombra a las encuadernadoras y salta la media sin las 20 mejores líneas (queda escrita en la página 4).

Si Brightspace o el wifi fallan, los tres reveals están en las slides 7, 9 y 11: corre los microcasos con pizarra y mano alzada, los campos de la página 3 se hacen en papel, y el memo a María se escribe en papel y el encargo de la página 7 se revisa en casa. La sesión pierde los candados, no pierde el arco.

Si sobra tiempo, en este orden: el bonus de la página 6 (líneas con descuento: media −$6.66 contra mediana +$3.34), una segunda ronda de memos leídos, o el desafío del cuaderno opcional de Colab (Mesas: media, mediana y total negativos, el contraste perfecto con Libreros).

## Cierre

Minuto 84, con la slide 14 proyectada y sin cambiarla durante las preguntas:

"Recuerden dónde empezamos: les prometí que hoy saldrían sabiendo detectar un promedio mentiroso en tres minutos. El detector ya lo tienen: pidan la media y la mediana, y si se alejan, pidan el histograma. La regla de la casa cabe en una línea: ningún promedio sin su distribución. María entró al comité con sus tres números buenos, y ya les dejó el encargo en la última página: el reporte de cinco diapositivas, con su memo de primera lámina, se entrega en el buzón antes del miércoles. Y el miércoles hacemos perfilado contra reloj, así que traigan la laptop. La próxima vez que un promedio los mire a los ojos, ya saben qué pedirle. Nos vemos el miércoles."

Anticipo ya incluido en el guion: miércoles, sesión 6, perfilado descriptivo contra reloj sobre Comercial Andina, con laptop obligatoria.

## Después de dictarla

(Espacio para tus notas: qué funcionó, qué no, qué cambiar.)

- Medias y medianas de la muestra que salieron en el microcaso 1:
- Votos del microcaso 2 (Muebles / Suministros / depende):
- Firmas del microcaso 3 (sí / no / distribución):
- Minuto real en que llegaron a la página 6:
- ¿Los candados funcionaron en el visor de Brightspace del aula?
- Cambios para la próxima vez:
