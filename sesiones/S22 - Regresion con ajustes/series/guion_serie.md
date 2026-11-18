# Una recta no se dobla · guion de la serie

Diez episodios y seis sub-videos de interacciones que cuentan la clase de regresión con ajustes. Daniela, la agencia y un narrador llevan la historia. Los episodios 3, 8 y la última parte del 9 son ejercicios: dicen qué hacer y no dan las respuestas. Los episodios que revelan resultados van después del ejercicio correspondiente.

| Episodio | Título | Cuándo verlo |
|---|---|---|
| 01 | La promesa | Antes de todo |
| 02 | Doblar el plano | Después del episodio 1 |
| 02.1 | Cómo separé los puntos | Parte 1 de Doblar el plano |
| 02.2 | Qué es una interacción | Parte 2 de Doblar el plano |
| 02.3 | Más ejemplos de interacción | Parte 3 de Doblar el plano |
| 02.4 | Interacciones en Python | Parte 4 de Doblar el plano |
| 02.5 | Cómo leer una interacción | Parte 5 de Doblar el plano, justo antes del ejercicio |
| 02.6 | Entrenar y probar | Parte 6 de Doblar el plano, antes del ejercicio |
| 03 | Ejercicio: corrijan la promesa | Se trabaja en grupos |
| 04 | La promesa corregida | Después de las etapas 1 a 3 |
| 05 | La oferta de la agencia | Después del episodio 4 |
| 06 | Ridge: poner un precio | Después del episodio 5 |
| 07 | Lasso y por qué corta | Después del episodio 6 |
| 08 | Ejercicio: contesten la oferta | Se trabaja en grupos |
| 09 | Qué ajuste se queda | Después de las etapas 4 y 5 |
| 10 | La columna pensada | Después de entregar la etapa 6 |

## 01. La promesa

*Antes de todo*

### Portada

**Narrador.** Una recta no se dobla. Episodio uno: la promesa.

### Ilustración · comite

**Daniela.** El viernes le prometí al comité catorce mil cuatrocientas veinte unidades en el mercado nuevo.

**Narrador.** Daniela es gerente de marca de Bebidas Cumbre. Tiene datos de doscientos mercados: cuánto invirtió en televisión, en radio y en prensa, y cuánto vendió.

**Narrador.** Con ellos armó un modelo sencillo, un plano, y con ese plano defendió su plan: cincuenta mil dólares en televisión y cuarenta y nueve mil en radio.

**Daniela.** Mi duda es simple. ¿Esa cifra se sostiene?

### Apuesta y revelación

**Narrador.** Hagamos una apuesta. Hay veinte mercados que ya invierten parecido a su plan.

**Narrador.** ¿Cuánto venden en promedio, en miles de unidades? Pausa el video y escribe tu número. *(pausa de 4 segundos)*

**Narrador.** El plano les pronostica doce coma cuarenta y tres.

**Narrador.** Y vendieron diez coma dieciséis.

**Narrador.** Son dos mil doscientas setenta unidades de más por mercado, y en los veinte se pasó hacia el mismo lado. Eso no es mala suerte.

### Animación · Cómo se ajusta una recta

**Narrador.** Para entender qué pasó, volvamos a lo básico. Cada punto es un mercado. El modelo más simple pronostica el promedio para todos: es la línea base.

**Narrador.** Cada error se convierte en un cuadrado. Sumamos esos cuadrados y tenemos un solo número que dice qué tan mal vamos.

**Narrador.** Si inclinamos la recta de más, algunos cuadrados se achican y otros crecen.

**Narrador.** Si la inclinamos al revés, la suma sube todavía más.

**Narrador.** Ajustar es mover la recta hasta llegar al punto más bajo. A eso se le llama mínimos cuadrados.

**Narrador.** Fíjate en un detalle. El ajuste no elige la forma. Busca la mejor recta entre todas las rectas. Si el mundo se curva, igual te entrega una recta, y no te avisa.

### Mapa de errores · El plano falla con un patrón

**Narrador.** Para saber si nos falló la forma, miramos los errores. Cada punto es un mercado, ubicado según lo que invirtió en televisión y en radio.

**Narrador.** En rojo, los mercados donde el plano prometió de más. En azul, donde prometió de menos.

**Narrador.** Si fuera ruido, los colores estarían mezclados. Pero el rojo se junta donde hay un solo medio.

**Narrador.** Y el azul, arriba a la derecha, donde están los dos.

**Narrador.** La equis es el plan de Daniela. Cayó en zona roja. El plano falla con un patrón, y un patrón se puede arreglar.

## 02. Doblar el plano

*Después del episodio 1*

### Portada

**Narrador.** Episodio dos: doblar el plano.

### Animación · Doblar es agregar columnas

**Narrador.** Una recta no se dobla. Pero no hace falta un método nuevo. Empezamos con las dos columnas de siempre: televisión y radio.

**Narrador.** Agregamos una columna que se calcula con una multiplicación: televisión por radio. Pregunta si un medio potencia al otro.

**Narrador.** Agregamos otra: televisión al cuadrado. Pregunta si la televisión se satura cuando ya hay mucha.

**Narrador.** Mírala bien. Sigue siendo una suma de columnas, y mínimos cuadrados funciona igual. Por eso se sigue llamando regresión lineal.

### Animación · Dos medios juntos rinden distinto

**Narrador.** Veamos lo que cambia. En rojo, mercados con mucha radio. En negro, con poca.

**Narrador.** El plano obliga a dibujar dos rectas paralelas: dice que la radio suma lo mismo con cualquier televisión.

**Narrador.** Ahora le dejamos doblarse. Las líneas se curvan, se abren en abanico y se acercan a los puntos.

**Narrador.** Con poca televisión, la radio separa unas dos mil unidades.

**Narrador.** Con mucha televisión, separa once mil. La radio rinde según la televisión que ya hay.

### Ilustración · radio-tv

**Narrador.** A eso se le llama interacción: el efecto de una variable depende de otra.

**Narrador.** Y a la curva que se aplana se le llama saturación: las primeras pautas rinden más que las últimas.

**Narrador.** Cuando las columnas nuevas son potencias, hablamos de ajuste polinomial. El grado es la potencia más alta.

**Narrador.** Ahora te toca a ti. ¿Cuánto cambia la promesa de Daniela?

## 02.1. Cómo separé los puntos

*Parte 1 de Doblar el plano*

### Portada

**Narrador.** Doblar el plano, parte uno: de dónde salieron los puntos rojos y negros.

### Separar los grupos · De dónde salen el rojo y el negro

**Narrador.** Estos son los doscientos mercados: televisión en horizontal y ventas en vertical, todos del mismo color. Mira la forma. A medida que crece la televisión, la nube se abre.

**Narrador.** ¿Por qué se abre? Porque falta una variable. Cada mercado también invirtió en radio, y un gráfico plano no tiene otro eje para mostrarla.

**Narrador.** Entonces usamos el color. Pintamos cada punto según su radio: más rojo, más radio. Más negro, menos radio. Ahora sí se ve: los rojos van arriba y los negros abajo.

**Narrador.** A la derecha está la columna radio, ordenada. Para contar la historia con dos grupos fáciles de ver, puse dos cortes.

**Narrador.** Rojo: los cincuenta y siete mercados con treinta y cinco mil dólares o más en radio. Negro: los sesenta y uno con doce mil o menos.

**Narrador.** Los ochenta y dos del medio quedan en gris. Siguen existiendo: solo los saqué de la vista para que el contraste se note.

**Narrador.** Esos cortes no salen de ninguna fórmula. Los elegí yo, mirando la distribución. Por eso hay que comprobar que el resultado no dependa de ellos.

**Narrador.** Si muevo los cortes, los grupos cambian de tamaño, pero el abanico sigue ahí.

**Narrador.** Un último cuidado. La televisión promedio de los dos grupos es casi igual: ciento cuarenta y seis y ciento cuarenta y un mil. La comparación es justa.

### Líneas desde una ecuación · Una sola ecuación, tres líneas

**Narrador.** Ahora, las líneas. Aquí está lo que más confunde: el modelo no recibe grupos. Se entrena con los doscientos mercados y con la radio como número.

**Narrador.** La ecuación es una sola: televisión, radio y su producto, cada uno con su coeficiente.

**Narrador.** Para dibujar la línea roja, tomo el promedio de radio del grupo rojo, cuarenta y uno coma nueve, y lo reemplazo en la ecuación. Queda una recta que solo depende de la televisión.

**Narrador.** Para la negra hago lo mismo, con radio de cinco coma siete.

**Narrador.** Y con el grupo del medio, radio de veintitrés coma cuatro, la línea cae justo entre las dos. El abanico es continuo.

**Narrador.** Comprobación. Si ajusto una recta aparte solo con los rojos, su pendiente es cero coma cero seis cinco seis. La del modelo, cero coma cero seis cuatro seis. Con los negros, casi idénticas. El modelo acertó sin conocer los grupos.

**Narrador.** Aquí dejé solo la interacción, para verla pura. En el video anterior también estaba la televisión al cuadrado, y por eso aquellas líneas se curvaban.

## 02.2. Qué es una interacción

*Parte 2 de Doblar el plano*

### Portada

**Narrador.** Parte dos: qué es una interacción.

### Ilustración · finca

**Narrador.** Una interacción es cuando el efecto de una cosa depende de otra. Piensa en una finca de la parte alta de San Cristóbal.

**Narrador.** El abono sirve mucho si la tierra tiene agua, y casi nada si está seca. Preguntar cuánto rinde el abono no tiene una sola respuesta.

**Narrador.** Con la publicidad pasa lo mismo. ¿Cuánto rinde la televisión? Depende de cuánta radio haya.

### Álgebra animada · La pendiente deja de ser un número fijo

**Narrador.** Mira la ecuación con interacción. Tiene cuatro términos.

**Narrador.** Ahora juntamos todo lo que multiplica a la televisión.

**Narrador.** Queda esto: la pendiente de la televisión ya no es un número fijo. Es cero coma cero uno nueve, más cero coma cero cero uno uno por la radio.

**Narrador.** Por eso se dice que interactúan: una variable cambia la pendiente de la otra. Sin ese último término, la pendiente sería siempre la misma.

### Recta que gira · La radio hace girar la recta

**Narrador.** Míralo en movimiento. Con la radio en cero, cada mil dólares en televisión traen diecinueve unidades.

**Narrador.** Subimos la radio y la línea gira. Con veinte mil en radio, son cuarenta y una unidades.

**Narrador.** Con cuarenta y cinco mil, sesenta y ocho.

**Narrador.** Comparemos con el modelo sin interacción. La línea sube y baja, pero no gira: siempre cuarenta y seis unidades.

### Superficie en 3D · Torcer la hoja

**Narrador.** Si agregamos la radio como tercer eje, el modelo sin interacción es un plano: una hoja rígida.

**Narrador.** Cortamos la hoja con radio baja y con radio alta, y salen dos rectas paralelas.

**Narrador.** La interacción tuerce la hoja. Una esquina sube más que las otras.

**Narrador.** Ahora los cortes ya no son paralelos. Eso, en tres dimensiones, es una interacción.

**Narrador.** Por eso esta parte se llama doblar el plano.

## 02.3. Más ejemplos de interacción

*Parte 3 de Doblar el plano*

### Portada

**Narrador.** Parte tres: más ejemplos de interacción.

### Ejemplo real · Numérica por categoría: motores

**Narrador.** Primer ejemplo: motores. Para más de mil vehículos, consumo de combustible contra emisiones de CO dos.

**Narrador.** Con gasolina, cada litro más a los cien kilómetros sube veintitrés gramos de CO dos por kilómetro.

**Narrador.** Con diésel, veintisiete. Con etanol, dieciséis.

**Narrador.** La pendiente depende del combustible: una variable numérica interactúa con una categoría. Es casi física, y por eso las líneas quedan tan limpias.

### Ilustración · descuento

**Narrador.** Segundo ejemplo, con datos que ya conoces: Superstore. ¿Un descuento cuesta lo mismo en todas las categorías?

### Ejemplo real · Numérica por categoría: descuentos

**Narrador.** Cada punto es el margen promedio para un nivel de descuento. Sin descuento, suministros de oficina deja el mejor margen.

**Narrador.** Pero cada diez puntos de descuento le quitan veintiún puntos de margen. A muebles, diecisiete. A tecnología, doce.

**Narrador.** Las líneas se cruzan. La categoría que más gana sin descuento es la que más pierde con él.

### Ejemplo real · Categoría por categoría: el Titanic

**Narrador.** Tercer ejemplo, con dos categorías: los pasajeros del Titanic, sobrevivencia por sexo y por clase.

**Narrador.** La diferencia entre mujeres y hombres fue de sesenta puntos en primera clase, setenta y seis en segunda, y treinta y seis en tercera.

**Narrador.** El efecto de ser mujer dependió de la clase. Eso también es una interacción, y por eso las líneas no van paralelas.

### Ejemplo real · Cuando no hay interacción

**Narrador.** Y un ejemplo donde no hay. La radio cuando hay poca prensa, y la radio cuando hay mucha.

**Narrador.** Las líneas van casi paralelas. El valor p del término de interacción es cero coma cinco: no hay evidencia.

**Narrador.** No toda pareja interactúa. Hay que probarlo, no suponerlo.

## 02.4. Interacciones en Python

*Parte 4 de Doblar el plano*

### Portada

**Narrador.** Parte cuatro: interacciones en Python.

### Código en pantalla · A mano, con LinearRegression

**Narrador.** La forma más directa es crear la columna a mano. Multiplicas televisión por radio, y ya tienes una columna nueva.

**Narrador.** Esa columna entra al modelo junto con las otras dos: televisión, radio y su producto. Es la misma regresión lineal de siempre.

**Narrador.** El modelo devuelve tres coeficientes. El último, cero coma cero cero uno uno, es el de la interacción.

### Código en pantalla · Con fórmula, en statsmodels

**Narrador.** Con statsmodels hay un atajo. En la fórmula, el asterisco entre televisión y radio significa: cada una por separado, y además su producto.

**Narrador.** Salen los mismos números, y con nombres. Si escribes dos puntos en vez del asterisco, te da solo el producto. Eso casi nunca es lo que quieres.

### Código en pantalla · Leer la pendiente

**Narrador.** Ahora lo que de verdad importa: leerlo. La pendiente de la televisión es su coeficiente, más el de la interacción multiplicado por la radio de ese mercado.

**Narrador.** Multiplicado por mil, son unidades por cada mil dólares: diecinueve sin radio, cuarenta y una con veinte mil, sesenta y ocho con cuarenta y cinco mil.

### Código en pantalla · Todas las parejas de una vez

**Narrador.** Si tienes varias variables, scikit-learn crea todos los productos por ti. Con interaction only no agrega cuadrados, solo productos.

**Narrador.** De tres medios salen seis columnas: los tres originales y sus tres parejas.

### Código en pantalla · Con una categoría

**Narrador.** Con una categoría la idea es la misma. La letra C le dice a statsmodels que el tipo de combustible es una categoría.

**Narrador.** Se lee contra la categoría de referencia, que aquí es diésel: veintisiete de pendiente.

**Narrador.** Etanol es once menos: dieciséis. Gasolina, cuatro menos: veintitrés.

### Código en pantalla · Así se separaron los puntos

**Narrador.** Y esta es exactamente la separación de los puntos rojos y negros: dos filtros sobre la columna radio.

**Narrador.** Cincuenta y siete mercados, con radio promedio de cuarenta y uno coma nueve. Sesenta y uno, con cinco coma siete. Esos promedios son los que van en la ecuación.

### Código en pantalla · Así se dibujan las líneas

**Narrador.** Para dibujarlas, primero se crea una rejilla de valores de televisión.

**Narrador.** Luego, para cada grupo, se pintan sus puntos, se pronostica con el promedio de radio del grupo y se traza la línea.

**Narrador.** Este es el gráfico que vas a obtener. Es el mismo de la animación, hecho por ti.

### Código en pantalla · Medir si sirvió

**Narrador.** Falta lo más importante: medir si sirvió. Siempre con los mercados que el modelo no vio.

**Narrador.** Con dos columnas, el error es uno coma treinta y nueve. Con la interacción, cero coma sesenta y cinco.

## 02.5. Cómo leer una interacción

*Parte 5 de Doblar el plano, justo antes del ejercicio*

### Portada

**Narrador.** Parte cinco: cómo leer una interacción sin equivocarte.

### Errores comunes · Cuatro errores comunes

**Narrador.** Primer error: leer cero coma cero uno nueve como el efecto de la televisión. Ese número es su efecto solo cuando la radio vale cero, y casi ningún mercado está ahí.

**Narrador.** Segundo error: despreciar la interacción porque su coeficiente es diminuto. Se multiplica por televisión y por radio, que son números grandes.

**Narrador.** Tercer error: meter solo el producto y sacar las variables originales. El error de prueba sube de cero coma sesenta y cinco a cero coma noventa.

**Narrador.** Cuarto error: creer que los grupos rojo y negro son parte del modelo. Los grupos solo sirven para ver. El modelo usa la radio como número.

### Guía de síntomas · La receta, antes del ejercicio

**Narrador.** Antes de ir al ejercicio, esta es la receta. Primero mira el mapa de errores: si hay patrón, falta algo.

**Narrador.** Segundo, piensa en el negocio: qué variable podría potenciar a cuál.

**Narrador.** Tercero, agrega la columna.

**Narrador.** Cuarto, mide en los mercados de prueba, contra el modelo anterior.

**Narrador.** Y quinto, tradúcelo a dólares. Un coeficiente solo no decide nada.

### Ilustración · ejercicio

**Narrador.** Ahora sí, con todo esto, vamos al ejercicio.

## 02.6. Entrenar y probar

*Parte 6 de Doblar el plano, antes del ejercicio*

### Portada

**Narrador.** Parte seis: entrenar y probar.

### Entrenar y probar · Train y test: entrenar y probar

**Narrador.** Hemos hablado de mercados de prueba sin explicar de dónde salen. Aquí están los doscientos.

**Narrador.** Si estudias con el examen en la mano y sacas veinte, no sabes si aprendiste o si memorizaste. Un modelo tiene el mismo problema.

**Narrador.** Por eso, antes de ajustar nada, barajamos los mercados al azar.

**Narrador.** Ciento cincuenta van a entrenamiento: con ellos aprende el modelo.

**Narrador.** Cincuenta se guardan bajo llave. Son la prueba.

**Narrador.** El modelo solo ve los de entrenamiento. Los coeficientes, las columnas y hasta la fuerza del freno salen de ahí.

**Narrador.** Al final, y una sola vez, abrimos la caja. El error en esos cincuenta es el que cuenta, porque el modelo nunca los vio.

**Narrador.** Compara los dos errores. El plano se equivoca uno coma veintiuno en entrenamiento y uno coma treinta y nueve en prueba. Están cerca: aprendió algo real.

**Narrador.** Si el error de entrenamiento es mucho mejor que el de prueba, memorizó. En inglés se llaman train y test: entrenar y probar.

**Narrador.** Un detalle práctico: random state cuarenta y dos hace que el azar salga siempre igual. Por eso todos comparamos contra los mismos cincuenta.

## 03. Ejercicio: corrijan la promesa

*Se trabaja en grupos*

### Portada

**Narrador.** Episodio tres. Ejercicio: corrijan la promesa.

### Ilustración · ejercicio

**Narrador.** Este episodio es para trabajar. Abre la página del curso, descarga el archivo de los doscientos mercados y el cuaderno de Colab.

**Narrador.** Puedes hacerlo con tu asistente de inteligencia artificial. Lo que se califica es que sepas qué te entregó y que lo hayas verificado.

**Narrador.** En grupo, repártanse tres roles: uno pide, otro verifica una fila a mano y otro escribe la decisión.

### Ejercicio guiado · Dónde falla el plano

**Daniela.** Antes de volver al comité quiero saber si el plano se equivoca parejo o siempre en el mismo tipo de mercado.

**Narrador.** Primero, ajusta el plano con los doscientos mercados y calcula el error de cada uno: real menos pronóstico.

**Narrador.** Después haz un gráfico de televisión contra radio, con el color según ese error.

**Narrador.** Por último, promedia los mercados con televisión hasta noventa y radio desde treinta y cinco.

**Narrador.** Pausa aquí. Cuando tengas tu número, escríbelo en el candado de la página. *(pausa de 4 segundos)*

### Ejercicio guiado · Doblar el plano

**Daniela.** Quiero un modelo que entienda que televisión y radio juntas no son lo mismo que por separado.

**Narrador.** Separa ciento cincuenta mercados para entrenar y cincuenta para probar, con random state cuarenta y dos.

**Narrador.** Crea la columna televisión por radio, y luego televisión al cuadrado. Mide cada modelo en los cincuenta de prueba.

**Narrador.** Compáralos con la línea base y con el plano.

**Narrador.** Pausa y hazlo. ¿Cuál de las dos columnas aportó más? *(pausa de 4 segundos)*

### Ejercicio guiado · Corregir la promesa

**Daniela.** Necesito la cifra correcta de mi plan, la de la agencia, y saber dónde conviene el próximo dólar de radio.

**Narrador.** Ajusta el modelo de cuatro columnas con los doscientos mercados y pronostica los dos planes.

**Narrador.** Calcula la utilidad: unidades por doce dólares de margen, menos la inversión. Ojo, que todo está en miles.

**Narrador.** Y calcula cuánto trae cada mil dólares en radio cuando la televisión vale cincuenta, ciento cincuenta y doscientos cincuenta.

**Narrador.** Pausa. Escribe tu decisión con el número. Una frase sin número no vale. *(pausa de 4 segundos)*

## 04. La promesa corregida

*Después de las etapas 1 a 3*

### Portada

**Narrador.** Episodio cuatro: la promesa corregida. Si todavía no haces las etapas uno a tres, vuelve cuando las tengas.

### Barras de error · Dos columnas bajan el error

**Narrador.** Empecemos por el error, medido en los mismos cincuenta mercados de prueba. Pronosticar el promedio se equivoca en cuatro coma sesenta y ocho mil unidades.

**Narrador.** El plano bajó a uno coma treinta y nueve.

**Narrador.** Con la interacción, cero coma sesenta y cinco.

**Narrador.** Y con la televisión al cuadrado, cero coma cuarenta y ocho. Dos columnas más, y el error es un tercio.

### Mapa antes y después · El patrón desaparece

**Narrador.** El mapa lo confirma. Este es el plano, con cuarenta mercados que fallan por más de dos mil unidades.

**Narrador.** Y este es el plano doblado. El patrón desaparece: solo quedan dos.

**Narrador.** Un mapa casi en blanco es la prueba que se le pide a cualquier ajuste antes de creerle.

### Línea que se dibuja · La radio depende de la TV

**Narrador.** Ahora, la consecuencia de negocio. La semana pasada la respuesta fue: los próximos mil dólares, a radio, en todas partes.

**Narrador.** Esa es la línea gris. El plano dice que la radio rinde igual siempre.

**Narrador.** Pero con cincuenta mil en televisión, cada mil dólares en radio deja sesenta y ocho dólares.

**Narrador.** Con ciento cincuenta mil, mil trescientos sesenta.

**Narrador.** Y con doscientos cincuenta mil, dos mil seiscientos cincuenta y dos.

**Narrador.** Por debajo de cuarenta y cinco mil dólares en televisión, la radio no se paga.

### Contador y utilidad · La promesa corregida

**Narrador.** Y ahora, la cifra que importa.

**Narrador.** El plan de Daniela no vende catorce mil cuatrocientas veinte unidades. Vende once mil setecientas setenta.

**Narrador.** Son dos mil seiscientas cincuenta unidades que prometió de más.

**Narrador.** ¿Y la agencia? Sube a quince mil doscientas veinte, pero invierte setenta y seis mil dólares más.

**Narrador.** Utilidad de Daniela: cuarenta y dos mil dólares. Utilidad de la agencia: siete mil setecientos.

**Daniela.** La decisión se sostiene. La cifra no. Voy a tener que volver al comité.

## 05. La oferta de la agencia

*Después del episodio 4*

### Portada

**Narrador.** Episodio cinco: la oferta de la agencia.

### Ilustración · agencia

**Agencia.** Daniela, tu modelo de cuatro columnas está bien para empezar. Nosotros traemos uno de ochenta y tres.

**Agencia.** R cuadrado de cero coma nueve nueve ocho. Casi perfecto. Se equivoca en ciento cincuenta unidades.

**Daniela.** ¿Y en mercados nuevos?

**Narrador.** Buena pregunta. Antes de seguir, apuesta. ¿Cuánto se equivoca en cincuenta mercados que no vio? Pausa y escribe tu número. *(pausa de 4 segundos)*

### Animación · Más grado, menos verdad

**Narrador.** Para verlo con calma, tomemos solo trece mercados. Una recta, grado uno, no pasa por todos.

**Narrador.** Subimos hasta el grado tres. Ya sigue mejor los puntos.

**Narrador.** Seguimos: grado cinco, siete, nueve. La curva se retuerce y el error de entrenamiento sigue bajando.

**Narrador.** Grado doce: pasa por sus puntos. El error de entrenamiento llega a cero.

**Narrador.** Perfecto, ¿verdad? Ahora miremos los mercados que no vio.

**Narrador.** El error de prueba, la línea roja, sube justo cuando el otro baja. El modelo se aprendió el ruido. Eso se llama sobreajuste.

### Curvas por grado · En el grado 5 la prueba se rompe

**Narrador.** Hagámoslo con los tres medios y los ciento cincuenta mercados. A la izquierda, el R cuadrado de entrenamiento sube con cada grado y nunca avisa.

**Narrador.** A la derecha, el error de prueba baja hasta el grado tres.

**Narrador.** En el grado cinco se rompe. En el seis, el de la agencia, llega a tres coma veinticinco.

**Narrador.** Y en el grado siete, a casi cuarenta y tres. Peor que no tener modelo.

### Pronóstico por mercado · Pronostica ventas negativas

**Narrador.** ¿Cómo se equivoca? Estos son los cincuenta mercados, de menor a mayor venta real. En negro, lo que vendieron.

**Narrador.** En rojo, el pronóstico del grado seis. En cuarenta y cinco mercados el error es menor a dos mil. Se ve bien.

**Narrador.** Y entonces aparece el mercado diecisiete.

**Narrador.** El modelo le pronostica menos noventa y ocho mil unidades. Ventas negativas. Vendió doce mil quinientas.

### Ilustración · mercado17

**Narrador.** Ese mercado tiene la inversión en prensa más alta de toda la base. Un sobreajuste no se equivoca parejo: se equivoca en los bordes, y no sabes de antemano en cuáles.

**Daniela.** No lo compro.

## 06. Ridge: poner un precio

*Después del episodio 5*

### Portada

**Narrador.** Episodio seis. Ridge: poner un precio.

### Ecuación y perilla · El modelo paga por usar coeficientes

**Narrador.** Las columnas de la agencia no son el problema. El problema es que nada le impide usarlas a lo loco. Hasta ahora el modelo tenía una sola meta: bajar el error.

**Narrador.** Regularizar le agrega una segunda cosa: un precio por usar coeficientes grandes.

**Narrador.** Ese precio lo controla una perilla que se llama lambda. En el código la vas a ver como alfa. Es lo mismo.

**Narrador.** Con lambda cero, no hay freno: la cinta enredada de la agencia.

**Narrador.** Con lambda enorme, todos los coeficientes valen cero y el modelo es el promedio. La respuesta buena está en el medio.

### Tarjetas de escala · El freno necesita una sola escala

**Narrador.** Antes de frenar, un detalle que parece menor. La televisión en miles de dólares tiene un coeficiente de cero coma cero cuatro cinco ocho.

**Narrador.** Si la misma televisión estuviera en dólares, el coeficiente sería mil veces más chico.

**Narrador.** El pronóstico es idéntico, pero ese coeficiente diminuto casi no pagaría. El freno castigaría la unidad, no la variable.

**Narrador.** Por eso, antes de frenar, cada columna se pone en la misma escala: media cero, desviación uno.

### Animación · Ridge encoge todas las columnas

**Narrador.** Volvamos a unos pocos mercados, con un polinomio de grado nueve. Sin freno, la curva se retuerce.

**Narrador.** A la derecha, el tamaño de cada coeficiente. Son enormes, unos positivos y otros negativos, cancelándose entre sí.

**Narrador.** Ridge cobra por el cuadrado de cada coeficiente. Esta es su cuenta: error más lambda por la suma de los cuadrados.

**Narrador.** Subimos el freno. La curva se calma y todos los coeficientes se encogen a la vez.

**Narrador.** Con mucho freno, la curva se aplana hasta el promedio. Frenamos de más.

**Narrador.** En un punto intermedio queda lo mejor: la forma, sin las locuras.

**Narrador.** Todas se encogen. Ninguna desaparece: por eso las nueve columnas siguen vivas.

### Ilustración · ridge

**Narrador.** Piensa en Ridge como alguien que sostiene muchas correas. Las acerca todas, pero no suelta ninguna.

**Narrador.** Por eso sirve cuando varias columnas dicen casi lo mismo: reparte el crédito entre ellas.

## 07. Lasso y por qué corta

*Después del episodio 6*

### Portada

**Narrador.** Episodio siete: Lasso, y por qué corta.

### Animación · Lasso apaga las que no pagan

**Narrador.** Lasso hace casi lo mismo, con una diferencia pequeña en la cuenta.

**Narrador.** Mira las barras. Ya con muy poco freno hay columnas en cero.

**Narrador.** Lasso cobra por el valor absoluto, no por el cuadrado.

**Narrador.** Subimos el freno, y las columnas van cayendo a exactamente cero.

**Narrador.** Al final quedan dos de nueve. Lasso eligió por su cuenta.

**Narrador.** Las que no pagan su costo valen cero.

### Animación · Por qué uno encoge y el otro corta

**Narrador.** ¿Por qué uno encoge y el otro corta? La respuesta es una imagen. Cada elipse es un nivel de error, y el punto azul son los coeficientes sin freno.

**Narrador.** El freno es un presupuesto: los coeficientes no se pueden salir de la zona. En Ridge la zona es un círculo. En Lasso, un rombo.

**Narrador.** Al encoger el presupuesto, el mejor ajuste queda en el punto rojo, donde el error toca la zona.

**Narrador.** El círculo no tiene esquinas, así que casi nunca toca un eje.

**Narrador.** El rombo tiene las esquinas justo sobre los ejes. Y en una esquina, un coeficiente vale exactamente cero.

### Ilustración · lasso

**Narrador.** Por eso Lasso es una tijera: corta los hilos que no sostienen nada.

**Narrador.** Sirve cuando sospechas que casi todas las columnas sobran, y cuando necesitas decir cuáles importan.

## 08. Ejercicio: contesten la oferta

*Se trabaja en grupos*

### Portada

**Narrador.** Episodio ocho. Ejercicio: contesten la oferta.

### Ilustración · validacion

**Narrador.** Falta una pregunta: ¿cuánto freno? Si lo eliges mirando los mercados de prueba, ya no son mercados que el modelo no vio.

**Narrador.** La solución es hacer turnos.

### Animación · El freno se elige sin ver la prueba

**Narrador.** Partimos los ciento cincuenta mercados de entrenamiento en cinco grupos. Cada vez, cuatro entrenan y uno valida.

**Narrador.** Un punto de la curva es el promedio de esos cinco turnos, para una fuerza de freno.

**Narrador.** Repetimos con cada fuerza. Con demasiado freno, el error se dispara.

**Narrador.** El punto más bajo es el alfa elegido. Y la prueba sigue guardada: se abre una sola vez, al final.

### Ejercicio guiado · La oferta de la agencia

**Daniela.** La agencia me ofrece grado seis con R cuadrado de cero coma nueve nueve ocho. ¿Lo compro?

**Narrador.** Con los tres medios, ajusta polinomios de grado uno a siete en los ciento cincuenta de entrenamiento.

**Narrador.** Para cada grado anota el R cuadrado de entrenamiento, el error de entrenamiento y el error de prueba.

**Narrador.** Mira los errores del grado seis, mercado por mercado.

**Narrador.** Pausa, y responde con el número que un comité entendería. *(pausa de 4 segundos)*

### Ejercicio guiado · El freno

**Daniela.** No descarto todas esas columnas todavía. Quiero ver si un freno las hace útiles.

**Narrador.** Toma el grado cinco, con cincuenta y cinco columnas. Para cada alfa de la lista, calcula el error con validación cruzada.

**Narrador.** Elige el mejor alfa de Lasso y el mejor de Ridge. Solo entonces mide en los cincuenta de prueba.

**Narrador.** Cuenta cuántas columnas quedan vivas en Lasso, y mira qué pasa con alfa cero coma tres.

**Narrador.** Lasso tarda unos segundos. Pausa y decide: ¿la curva de cuatro columnas, o el Lasso? *(pausa de 4 segundos)*

## 09. Qué ajuste se queda

*Después de las etapas 4 y 5*

### Portada

**Narrador.** Episodio nueve: qué ajuste se queda. Mira este episodio cuando termines las etapas cuatro y cinco.

### Columnas vivas por α · Lasso encontró la interacción sin ayuda

**Narrador.** Estos son los resultados. Arriba, cuántas de las cincuenta y cinco columnas sobreviven según la fuerza del freno.

**Narrador.** Abajo, el error en validación. El mínimo está en alfa cero coma cero cero tres, con dieciséis columnas vivas.

**Narrador.** Y mira lo que pasa con alfa cero coma tres. Quedan solo dos columnas: televisión, y televisión por radio.

**Narrador.** Nadie se lo indicó. Lasso encontró por su cuenta la misma interacción que encontramos pensando en el negocio.

### Comparación final · Error en los 50 mercados de prueba

**Narrador.** Comparemos en los cincuenta mercados de prueba. El plano: uno coma treinta y nueve.

**Narrador.** El grado cinco sin freno: uno coma setenta.

**Narrador.** Con Ridge, cero coma treinta y seis. Con Lasso, cero coma treinta y cinco. Los frenos rescataron las columnas.

**Narrador.** La curva de cuatro columnas queda en cero coma cuarenta y ocho. Pierde por poco.

**Daniela.** Con cuatro columnas puedo pararme frente al comité y explicar cada una.

### Ejercicio guiado · En casa

**Daniela.** Queda un último encargo. Propón una columna que tenga sentido de negocio y gánale a mi modelo. Y dime si el freno sirve cuando las columnas son casi copias.

**Narrador.** Piensa en cómo funciona la publicidad, escribe en una frase por qué tu columna tiene sentido, y mide el error en los mismos cincuenta mercados.

**Narrador.** Luego abre el archivo de consumo de combustible, de un taller de años anteriores, y toma seis mitades distintas de los datos.

**Narrador.** En cada una ajusta sin freno, con Ridge y con Lasso, y anota cuánto se mueve el coeficiente del consumo combinado.

**Narrador.** Entrega tu memo, el enlace del cuaderno y tus prompts en la carpeta de la actividad. *(pausa de 2 segundos)*

## 10. La columna pensada

*Después de entregar la etapa 6*

### Portada

**Narrador.** Episodio diez: la columna pensada. Míralo después de entregar la etapa seis.

### Ilustración · saturacion

**Narrador.** Si ya propusiste tu columna, comparemos. Piensa en la publicidad: las primeras pautas rinden mucho y las siguientes cada vez menos.

**Narrador.** Esa forma tiene nombre en matemáticas: raíz cuadrada.

### Curvas de saturación · La TV se satura rápido

**Narrador.** Estos son los mercados con poca radio. La curva gris usa televisión al cuadrado, y arranca demasiado alta.

**Narrador.** La curva roja usa la raíz de la televisión: sube rápido, luego se aplana, y sigue los puntos desde el principio.

### Comparación final · Cuatro columnas pensadas ganan

**Narrador.** Estos eran los modelos.

**Narrador.** Con la raíz, el error de prueba baja a cero coma veintinueve.

**Narrador.** Cuatro columnas pensadas le ganan a cincuenta y cinco. El freno es para cuando no sabes qué columnas importan. Si lo sabes, úsalo.

### Ilustración · co2

**Narrador.** El segundo encargo. Consumo en ciudad, en carretera y combinado están correlacionados casi uno a uno.

### Rangos de coeficientes · Columnas casi copiadas

**Narrador.** Sin freno, el coeficiente del combinado va de menos ochenta y siete a más ciento noventa y ocho, según la mitad de datos que te toque.

**Narrador.** Ridge reparte el crédito y se queda quieto, entre cinco y siete.

**Narrador.** Lasso apaga unas y deja otras, y cuál apaga depende de la muestra.

### Guía de síntomas · El síntoma elige el ajuste

**Narrador.** Esto es lo que te llevas para tu proyecto. Si los errores forman un patrón, prueba una curva o una transformación.

**Narrador.** Si el efecto de una variable depende de otra, una interacción.

**Narrador.** Si hay muchas columnas para pocas filas, Ridge o Lasso.

**Narrador.** Si las columnas son casi copias, Ridge.

**Narrador.** Y si necesitas saber cuáles importan, Lasso.

### Ilustración · experimento

**Narrador.** Y una advertencia. Un mejor ajuste no prueba causa. Los doscientos mercados se observaron: nadie asignó la radio al azar.

**Narrador.** Además, Daniela pone cuarenta y nueve mil en radio, y el dato llega a cuarenta y nueve mil seiscientos. Ya está en el borde.

**Narrador.** Antes de mover la plata, hay que probar la radio en mercados elegidos al azar.

### Cierre

**Daniela.** Voy a volver al comité con una cifra más baja, una razón clara y un experimento. *(pausa de 2 segundos)*
