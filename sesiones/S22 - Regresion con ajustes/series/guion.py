# -*- coding: utf-8 -*-
"""Guion de la serie Una recta no se dobla. Es la fuente única: voces, escenas y montaje salen de aquí.

Cada episodio es una lista de tomas. Cada toma tiene un tipo visual y una lista de beats.
Un beat es una frase narrada: su audio marca cuánto dura ese momento de la animación.
Los números van en palabras para que la voz los lea bien.
"""


def N(t, r=None, pausa=0):
    return {"voz": "narrador", "texto": t, "rotulo": r, "pausa": pausa}


def D(t, r=None, pausa=0):
    return {"voz": "daniela", "texto": t, "rotulo": r, "pausa": pausa}


def A(t, r=None, pausa=0):
    return {"voz": "agencia", "texto": t, "rotulo": r, "pausa": pausa}


PAUSA = 4  # segundos en silencio donde se le pide al estudiante pausar o apostar

EPISODIOS = [
    {"id": "E01", "slug": "la-promesa", "titulo": "La promesa", "cuando": "Antes de todo", "tomas": [
        {"tipo": "portada", "n": 1, "beats": [N("Una recta no se dobla. Episodio uno: la promesa.")]},
        {"tipo": "ilus", "img": "comite", "beats": [
            D("El viernes le prometí al comité catorce mil cuatrocientas veinte unidades en el mercado nuevo.", "14.420\nunidades"),
            N("Daniela es gerente de marca de Bebidas Cumbre. Tiene datos de doscientos mercados: cuánto invirtió en televisión, en radio y en prensa, y cuánto vendió.", "200\nmercados"),
            N("Con ellos armó un modelo sencillo, un plano, y con ese plano defendió su plan: cincuenta mil dólares en televisión y cuarenta y nueve mil en radio.", "50 mil en TV\n49 mil en radio"),
            D("Mi duda es simple. ¿Esa cifra se sostiene?", "¿Se\nsostiene?"),
        ]},
        {"tipo": "apuesta", "beats": [
            N("Hagamos una apuesta. Hay veinte mercados que ya invierten parecido a su plan."),
            N("¿Cuánto venden en promedio, en miles de unidades? Pausa el video y escribe tu número.", pausa=PAUSA),
            N("El plano les pronostica doce coma cuarenta y tres."),
            N("Y vendieron diez coma dieciséis."),
            N("Son dos mil doscientas setenta unidades de más por mercado, y en los veinte se pasó hacia el mismo lado. Eso no es mala suerte."),
        ]},
        {"tipo": "clip", "base": "S1Ajuste", "titulo": "Cómo se ajusta una recta", "beats": [
            N("Para entender qué pasó, volvamos a lo básico. Cada punto es un mercado. El modelo más simple pronostica el promedio para todos: es la línea base."),
            N("Cada error se convierte en un cuadrado. Sumamos esos cuadrados y tenemos un solo número que dice qué tan mal vamos."),
            N("Si inclinamos la recta de más, algunos cuadrados se achican y otros crecen."),
            N("Si la inclinamos al revés, la suma sube todavía más."),
            N("Ajustar es mover la recta hasta llegar al punto más bajo. A eso se le llama mínimos cuadrados."),
            N("Fíjate en un detalle. El ajuste no elige la forma. Busca la mejor recta entre todas las rectas. Si el mundo se curva, igual te entrega una recta, y no te avisa."),
        ]},
        {"tipo": "mapa", "titulo": "El plano falla con un patrón", "beats": [
            N("Para saber si nos falló la forma, miramos los errores. Cada punto es un mercado, ubicado según lo que invirtió en televisión y en radio."),
            N("En rojo, los mercados donde el plano prometió de más. En azul, donde prometió de menos."),
            N("Si fuera ruido, los colores estarían mezclados. Pero el rojo se junta donde hay un solo medio."),
            N("Y el azul, arriba a la derecha, donde están los dos."),
            N("La equis es el plan de Daniela. Cayó en zona roja. El plano falla con un patrón, y un patrón se puede arreglar."),
        ]},
    ]},
    {"id": "E02", "slug": "doblar-el-plano", "titulo": "Doblar el plano", "cuando": "Después del episodio 1", "tomas": [
        {"tipo": "portada", "n": 2, "beats": [N("Episodio dos: doblar el plano.")]},
        {"tipo": "clip", "base": "S2Columnas", "titulo": "Doblar es agregar columnas", "beats": [
            N("Una recta no se dobla. Pero no hace falta un método nuevo. Empezamos con las dos columnas de siempre: televisión y radio."),
            N("Agregamos una columna que se calcula con una multiplicación: televisión por radio. Pregunta si un medio potencia al otro."),
            N("Agregamos otra: televisión al cuadrado. Pregunta si la televisión se satura cuando ya hay mucha."),
            N("Mírala bien. Sigue siendo una suma de columnas, y mínimos cuadrados funciona igual. Por eso se sigue llamando regresión lineal."),
        ]},
        {"tipo": "clip", "base": "S3Abanico", "titulo": "Dos medios juntos rinden distinto", "beats": [
            N("Veamos lo que cambia. En rojo, mercados con mucha radio. En negro, con poca."),
            N("El plano obliga a dibujar dos rectas paralelas: dice que la radio suma lo mismo con cualquier televisión."),
            N("Ahora le dejamos doblarse. Las líneas se curvan, se abren en abanico y se acercan a los puntos."),
            N("Con poca televisión, la radio separa unas dos mil unidades."),
            N("Con mucha televisión, separa once mil. La radio rinde según la televisión que ya hay."),
        ]},
        {"tipo": "ilus", "img": "radio-tv", "beats": [
            N("A eso se le llama interacción: el efecto de una variable depende de otra.", "Interacción"),
            N("Y a la curva que se aplana se le llama saturación: las primeras pautas rinden más que las últimas.", "Saturación"),
            N("Cuando las columnas nuevas son potencias, hablamos de ajuste polinomial. El grado es la potencia más alta.", "Ajuste\npolinomial"),
            N("Ahora te toca a ti. ¿Cuánto cambia la promesa de Daniela?", "Te toca"),
        ]},
    ]},
    {"id": "E02A", "slug": "como-separe-los-puntos", "titulo": "Cómo separé los puntos", "cuando": "Parte 1 de Doblar el plano", "tomas": [
        {"tipo": "portada", "n": "2.1", "beats": [N("Doblar el plano, parte uno: de dónde salieron los puntos rojos y negros.")]},
        {"tipo": "separar", "titulo": "De dónde salen el rojo y el negro", "beats": [
            N("Estos son los doscientos mercados: televisión en horizontal y ventas en vertical, todos del mismo color. Mira la forma. A medida que crece la televisión, la nube se abre."),
            N("¿Por qué se abre? Porque falta una variable. Cada mercado también invirtió en radio, y un gráfico plano no tiene otro eje para mostrarla."),
            N("Entonces usamos el color. Pintamos cada punto según su radio: más rojo, más radio. Más negro, menos radio. Ahora sí se ve: los rojos van arriba y los negros abajo."),
            N("A la derecha está la columna radio, ordenada. Para contar la historia con dos grupos fáciles de ver, puse dos cortes."),
            N("Rojo: los cincuenta y siete mercados con treinta y cinco mil dólares o más en radio. Negro: los sesenta y uno con doce mil o menos."),
            N("Los ochenta y dos del medio quedan en gris. Siguen existiendo: solo los saqué de la vista para que el contraste se note."),
            N("Esos cortes no salen de ninguna fórmula. Los elegí yo, mirando la distribución. Por eso hay que comprobar que el resultado no dependa de ellos."),
            N("Si muevo los cortes, los grupos cambian de tamaño, pero el abanico sigue ahí."),
            N("Un último cuidado. La televisión promedio de los dos grupos es casi igual: ciento cuarenta y seis y ciento cuarenta y un mil. La comparación es justa."),
        ]},
        {"tipo": "lineas", "titulo": "Una sola ecuación, tres líneas", "beats": [
            N("Ahora, las líneas. Aquí está lo que más confunde: el modelo no recibe grupos. Se entrena con los doscientos mercados y con la radio como número."),
            N("La ecuación es una sola: televisión, radio y su producto, cada uno con su coeficiente."),
            N("Para dibujar la línea roja, tomo el promedio de radio del grupo rojo, cuarenta y uno coma nueve, y lo reemplazo en la ecuación. Queda una recta que solo depende de la televisión."),
            N("Para la negra hago lo mismo, con radio de cinco coma siete."),
            N("Y con el grupo del medio, radio de veintitrés coma cuatro, la línea cae justo entre las dos. El abanico es continuo."),
            N("Comprobación. Si ajusto una recta aparte solo con los rojos, su pendiente es cero coma cero seis cinco seis. La del modelo, cero coma cero seis cuatro seis. Con los negros, casi idénticas. El modelo acertó sin conocer los grupos."),
            N("Aquí dejé solo la interacción, para verla pura. En el video anterior también estaba la televisión al cuadrado, y por eso aquellas líneas se curvaban."),
        ]},
    ]},
    {"id": "E02B", "slug": "que-es-una-interaccion", "titulo": "Qué es una interacción", "cuando": "Parte 2 de Doblar el plano", "tomas": [
        {"tipo": "portada", "n": "2.2", "beats": [N("Parte dos: qué es una interacción.")]},
        {"tipo": "ilus", "img": "finca", "beats": [
            N("Una interacción es cuando el efecto de una cosa depende de otra. Piensa en una finca de la parte alta de San Cristóbal.", "Una cosa\ndepende\nde otra"),
            N("El abono sirve mucho si la tierra tiene agua, y casi nada si está seca. Preguntar cuánto rinde el abono no tiene una sola respuesta.", "¿Cuánto\nrinde?\nDepende"),
            N("Con la publicidad pasa lo mismo. ¿Cuánto rinde la televisión? Depende de cuánta radio haya.", "Depende\nde la radio"),
        ]},
        {"tipo": "factor", "titulo": "La pendiente deja de ser un número fijo", "beats": [
            N("Mira la ecuación con interacción. Tiene cuatro términos."),
            N("Ahora juntamos todo lo que multiplica a la televisión."),
            N("Queda esto: la pendiente de la televisión ya no es un número fijo. Es cero coma cero uno nueve, más cero coma cero cero uno uno por la radio."),
            N("Por eso se dice que interactúan: una variable cambia la pendiente de la otra. Sin ese último término, la pendiente sería siempre la misma."),
        ]},
        {"tipo": "pendiente", "titulo": "La radio hace girar la recta", "beats": [
            N("Míralo en movimiento. Con la radio en cero, cada mil dólares en televisión traen diecinueve unidades."),
            N("Subimos la radio y la línea gira. Con veinte mil en radio, son cuarenta y una unidades."),
            N("Con cuarenta y cinco mil, sesenta y ocho."),
            N("Comparemos con el modelo sin interacción. La línea sube y baja, pero no gira: siempre cuarenta y seis unidades."),
        ]},
        {"tipo": "superficie", "titulo": "Torcer la hoja", "beats": [
            N("Si agregamos la radio como tercer eje, el modelo sin interacción es un plano: una hoja rígida."),
            N("Cortamos la hoja con radio baja y con radio alta, y salen dos rectas paralelas."),
            N("La interacción tuerce la hoja. Una esquina sube más que las otras."),
            N("Ahora los cortes ya no son paralelos. Eso, en tres dimensiones, es una interacción."),
            N("Por eso esta parte se llama doblar el plano."),
        ]},
    ]},
    {"id": "E02C", "slug": "mas-ejemplos-de-interaccion", "titulo": "Más ejemplos de interacción", "cuando": "Parte 3 de Doblar el plano", "tomas": [
        {"tipo": "portada", "n": "2.3", "beats": [N("Parte tres: más ejemplos de interacción.")]},
        {"tipo": "ejco2", "titulo": "Numérica por categoría: motores", "beats": [
            N("Primer ejemplo: motores. Para más de mil vehículos, consumo de combustible contra emisiones de CO dos."),
            N("Con gasolina, cada litro más a los cien kilómetros sube veintitrés gramos de CO dos por kilómetro."),
            N("Con diésel, veintisiete. Con etanol, dieciséis."),
            N("La pendiente depende del combustible: una variable numérica interactúa con una categoría. Es casi física, y por eso las líneas quedan tan limpias."),
        ]},
        {"tipo": "ilus", "img": "descuento", "beats": [N("Segundo ejemplo, con datos que ya conoces: Superstore. ¿Un descuento cuesta lo mismo en todas las categorías?", "¿Cuesta\nlo mismo?")]},
        {"tipo": "ejsuper", "titulo": "Numérica por categoría: descuentos", "beats": [
            N("Cada punto es el margen promedio para un nivel de descuento. Sin descuento, suministros de oficina deja el mejor margen."),
            N("Pero cada diez puntos de descuento le quitan veintiún puntos de margen. A muebles, diecisiete. A tecnología, doce."),
            N("Las líneas se cruzan. La categoría que más gana sin descuento es la que más pierde con él."),
        ]},
        {"tipo": "ejtitanic", "titulo": "Categoría por categoría: el Titanic", "beats": [
            N("Tercer ejemplo, con dos categorías: los pasajeros del Titanic, sobrevivencia por sexo y por clase."),
            N("La diferencia entre mujeres y hombres fue de sesenta puntos en primera clase, setenta y seis en segunda, y treinta y seis en tercera."),
            N("El efecto de ser mujer dependió de la clase. Eso también es una interacción, y por eso las líneas no van paralelas."),
        ]},
        {"tipo": "ejprensa", "titulo": "Cuando no hay interacción", "beats": [
            N("Y un ejemplo donde no hay. La radio cuando hay poca prensa, y la radio cuando hay mucha."),
            N("Las líneas van casi paralelas. El valor p del término de interacción es cero coma cinco: no hay evidencia."),
            N("No toda pareja interactúa. Hay que probarlo, no suponerlo."),
        ]},
    ]},
    {"id": "E02D", "slug": "interacciones-en-python", "titulo": "Interacciones en Python", "cuando": "Parte 4 de Doblar el plano", "tomas": [
        {"tipo": "portada", "n": "2.4", "beats": [N("Parte cuatro: interacciones en Python.")]},
        {"tipo": "python", "snip": "p1", "titulo": "A mano, con LinearRegression", "revela": [1, 3, 4], "beats": [
            N("La forma más directa es crear la columna a mano. Multiplicas televisión por radio, y ya tienes una columna nueva."),
            N("Esa columna entra al modelo junto con las otras dos: televisión, radio y su producto. Es la misma regresión lineal de siempre."),
            N("El modelo devuelve tres coeficientes. El último, cero coma cero cero uno uno, es el de la interacción."),
        ]},
        {"tipo": "python", "snip": "p2", "titulo": "Con fórmula, en statsmodels", "revela": [1, 2], "beats": [
            N("Con statsmodels hay un atajo. En la fórmula, el asterisco entre televisión y radio significa: cada una por separado, y además su producto."),
            N("Salen los mismos números, y con nombres. Si escribes dos puntos en vez del asterisco, te da solo el producto. Eso casi nunca es lo que quieres."),
        ]},
        {"tipo": "python", "snip": "p3", "titulo": "Leer la pendiente", "revela": [3, 4], "beats": [
            N("Ahora lo que de verdad importa: leerlo. La pendiente de la televisión es su coeficiente, más el de la interacción multiplicado por la radio de ese mercado."),
            N("Multiplicado por mil, son unidades por cada mil dólares: diecinueve sin radio, cuarenta y una con veinte mil, sesenta y ocho con cuarenta y cinco mil."),
        ]},
        {"tipo": "python", "snip": "p7", "titulo": "Todas las parejas de una vez", "revela": [3, 4], "beats": [
            N("Si tienes varias variables, scikit-learn crea todos los productos por ti. Con interaction only no agrega cuadrados, solo productos."),
            N("De tres medios salen seis columnas: los tres originales y sus tres parejas."),
        ]},
        {"tipo": "python", "snip": "p6", "titulo": "Con una categoría", "revela": [3, 4, 4], "salida_en": 1, "beats": [
            N("Con una categoría la idea es la misma. La letra C le dice a statsmodels que el tipo de combustible es una categoría."),
            N("Se lee contra la categoría de referencia, que aquí es diésel: veintisiete de pendiente."),
            N("Etanol es once menos: dieciséis. Gasolina, cuatro menos: veintitrés."),
        ]},
        {"tipo": "python", "snip": "p4", "titulo": "Así se separaron los puntos", "revela": [2, 4], "beats": [
            N("Y esta es exactamente la separación de los puntos rojos y negros: dos filtros sobre la columna radio."),
            N("Cincuenta y siete mercados, con radio promedio de cuarenta y uno coma nueve. Sesenta y uno, con cinco coma siete. Esos promedios son los que van en la ecuación."),
        ]},
        {"tipo": "python", "snip": "p5", "titulo": "Así se dibujan las líneas", "revela": [1, 6, 6], "imagen": True, "beats": [
            N("Para dibujarlas, primero se crea una rejilla de valores de televisión."),
            N("Luego, para cada grupo, se pintan sus puntos, se pronostica con el promedio de radio del grupo y se traza la línea."),
            N("Este es el gráfico que vas a obtener. Es el mismo de la animación, hecho por ti."),
        ]},
        {"tipo": "python", "snip": "p8", "titulo": "Medir si sirvió", "revela": [2, 5], "beats": [
            N("Falta lo más importante: medir si sirvió. Siempre con los mercados que el modelo no vio."),
            N("Con dos columnas, el error es uno coma treinta y nueve. Con la interacción, cero coma sesenta y cinco."),
        ]},
    ]},
    {"id": "E02E", "slug": "como-leer-una-interaccion", "titulo": "Cómo leer una interacción", "cuando": "Parte 5 de Doblar el plano, justo antes del ejercicio", "tomas": [
        {"tipo": "portada", "n": "2.5", "beats": [N("Parte cinco: cómo leer una interacción sin equivocarte.")]},
        {"tipo": "trampas", "titulo": "Cuatro errores comunes", "cartas": [("0,0191", "no es todo el efecto de la TV: es su efecto cuando la radio vale cero."), ("0,0011", "parece diminuto, pero se multiplica por TV y por radio."), ("0,90", "es el error si sacas las variables originales. Con ellas, 0,65."), ("ROJO Y NEGRO", "son para mirar. El modelo usa la radio como número.")], "beats": [
            N("Primer error: leer cero coma cero uno nueve como el efecto de la televisión. Ese número es su efecto solo cuando la radio vale cero, y casi ningún mercado está ahí."),
            N("Segundo error: despreciar la interacción porque su coeficiente es diminuto. Se multiplica por televisión y por radio, que son números grandes."),
            N("Tercer error: meter solo el producto y sacar las variables originales. El error de prueba sube de cero coma sesenta y cinco a cero coma noventa."),
            N("Cuarto error: creer que los grupos rojo y negro son parte del modelo. Los grupos solo sirven para ver. El modelo usa la radio como número."),
        ]},
        {"tipo": "guia", "titulo": "La receta, antes del ejercicio", "filas": [("1. Mira el mapa de errores", "¿Hay patrón?"), ("2. Piensa en el negocio", "¿Qué potencia a qué?"), ("3. Agrega la columna", "tv × radio"), ("4. Mide en prueba", "Contra el modelo anterior"), ("5. Tradúcelo a dólares", "Margen por unidad")], "beats": [
            N("Antes de ir al ejercicio, esta es la receta. Primero mira el mapa de errores: si hay patrón, falta algo."),
            N("Segundo, piensa en el negocio: qué variable podría potenciar a cuál."),
            N("Tercero, agrega la columna."),
            N("Cuarto, mide en los mercados de prueba, contra el modelo anterior."),
            N("Y quinto, tradúcelo a dólares. Un coeficiente solo no decide nada."),
        ]},
        {"tipo": "ilus", "img": "ejercicio", "beats": [N("Ahora sí, con todo esto, vamos al ejercicio.", "Al\nejercicio")]},
    ]},
    {"id": "E02F", "slug": "entrenar-y-probar", "titulo": "Entrenar y probar", "cuando": "Parte 6 de Doblar el plano, antes del ejercicio", "tomas": [
        {"tipo": "portada", "n": "2.6", "beats": [N("Parte seis: entrenar y probar.")]},
        {"tipo": "traintest", "titulo": "Train y test: entrenar y probar", "beats": [
            N("Hemos hablado de mercados de prueba sin explicar de dónde salen. Aquí están los doscientos."),
            N("Si estudias con el examen en la mano y sacas veinte, no sabes si aprendiste o si memorizaste. Un modelo tiene el mismo problema."),
            N("Por eso, antes de ajustar nada, barajamos los mercados al azar."),
            N("Ciento cincuenta van a entrenamiento: con ellos aprende el modelo."),
            N("Cincuenta se guardan bajo llave. Son la prueba."),
            N("El modelo solo ve los de entrenamiento. Los coeficientes, las columnas y hasta la fuerza del freno salen de ahí."),
            N("Al final, y una sola vez, abrimos la caja. El error en esos cincuenta es el que cuenta, porque el modelo nunca los vio."),
            N("Compara los dos errores. El plano se equivoca uno coma veintiuno en entrenamiento y uno coma treinta y nueve en prueba. Están cerca: aprendió algo real."),
            N("Si el error de entrenamiento es mucho mejor que el de prueba, memorizó. En inglés se llaman train y test: entrenar y probar."),
            N("Un detalle práctico: random state cuarenta y dos hace que el azar salga siempre igual. Por eso todos comparamos contra los mismos cincuenta."),
        ]},
    ]},
    {"id": "E03", "slug": "ejercicio-corrijan-la-promesa", "titulo": "Ejercicio: corrijan la promesa", "cuando": "Se trabaja en grupos", "tomas": [
        {"tipo": "portada", "n": 3, "beats": [N("Episodio tres. Ejercicio: corrijan la promesa.")]},
        {"tipo": "ilus", "img": "ejercicio", "beats": [
            N("Este episodio es para trabajar. Abre la página del curso, descarga el archivo de los doscientos mercados y el cuaderno de Colab.", "Descarga\nlos datos"),
            N("Puedes hacerlo con tu asistente de inteligencia artificial. Lo que se califica es que sepas qué te entregó y que lo hayas verificado.", "Tú\nverificas"),
            N("En grupo, repártanse tres roles: uno pide, otro verifica una fila a mano y otro escribe la decisión.", "Pide\nverifica\ndecide"),
        ]},
        {"tipo": "ejercicio", "etapa": 1, "nombre": "Dónde falla el plano", "pasos": [
            ("Ajusta el plano con los 200 mercados y calcula el error de cada uno.", 'plano = smf.ols(\n  "ventas ~ tv + radio", df).fit()\nerror = plano.resid'),
            ("Grafica TV contra radio, con color según el error.", 'plt.scatter(df.tv, df.radio,\n  c=error, cmap="RdBu",\n  vmin=-5, vmax=5)'),
            ("Promedia los mercados con TV hasta 90 y radio desde 35.", "vecinos = df[(df.tv <= 90)\n  & (df.radio >= 35)]"),
            None], "beats": [
            D("Antes de volver al comité quiero saber si el plano se equivoca parejo o siempre en el mismo tipo de mercado.", "Quiero saber si el plano se equivoca parejo o siempre en el mismo tipo de mercado."),
            N("Primero, ajusta el plano con los doscientos mercados y calcula el error de cada uno: real menos pronóstico."),
            N("Después haz un gráfico de televisión contra radio, con el color según ese error."),
            N("Por último, promedia los mercados con televisión hasta noventa y radio desde treinta y cinco."),
            N("Pausa aquí. Cuando tengas tu número, escríbelo en el candado de la página.", pausa=PAUSA),
        ]},
        {"tipo": "ejercicio", "etapa": 2, "nombre": "Doblar el plano", "pasos": [
            ("Separa 150 mercados para entrenar y 50 para probar.", "tr, te = train_test_split(\n  df, test_size=0.25,\n  random_state=42)"),
            ("Crea TV × radio y TV². Mide cada modelo en los 50 de prueba.", 'tr["tv_radio"] = tr.tv * tr.radio\ntr["tv2"] = tr.tv ** 2'),
            ("Compara con la línea base y con el plano.", "mae(te.ventas,\n    modelo.predict(te[cols]))"),
            None], "beats": [
            D("Quiero un modelo que entienda que televisión y radio juntas no son lo mismo que por separado.", "Quiero un modelo que entienda que TV y radio juntas no son lo mismo que por separado."),
            N("Separa ciento cincuenta mercados para entrenar y cincuenta para probar, con random state cuarenta y dos."),
            N("Crea la columna televisión por radio, y luego televisión al cuadrado. Mide cada modelo en los cincuenta de prueba."),
            N("Compáralos con la línea base y con el plano."),
            N("Pausa y hazlo. ¿Cuál de las dos columnas aportó más?", pausa=PAUSA),
        ]},
        {"tipo": "ejercicio", "etapa": 3, "nombre": "Corregir la promesa", "pasos": [
            ("Ajusta las cuatro columnas con los 200 mercados y pronostica los dos planes.", 'curva = smf.ols(\n  "ventas ~ tv + radio"\n  " + tv:radio + I(tv**2)",\n  df).fit()'),
            ("Utilidad: unidades por 12 USD de margen, menos la inversión.", "utilidad = ventas * 12 - tv - radio"),
            ("¿Cuánto trae cada mil USD en radio con TV de 50, 150 y 250?", 'u = (b["radio"]\n  + b["tv:radio"] * tv) * 1000'),
            None], "beats": [
            D("Necesito la cifra correcta de mi plan, la de la agencia, y saber dónde conviene el próximo dólar de radio.", "Necesito la cifra correcta de mi plan y saber dónde conviene el próximo dólar de radio."),
            N("Ajusta el modelo de cuatro columnas con los doscientos mercados y pronostica los dos planes."),
            N("Calcula la utilidad: unidades por doce dólares de margen, menos la inversión. Ojo, que todo está en miles."),
            N("Y calcula cuánto trae cada mil dólares en radio cuando la televisión vale cincuenta, ciento cincuenta y doscientos cincuenta."),
            N("Pausa. Escribe tu decisión con el número. Una frase sin número no vale.", pausa=PAUSA),
        ]},
    ]},
    {"id": "E04", "slug": "la-promesa-corregida", "titulo": "La promesa corregida", "cuando": "Después de las etapas 1 a 3", "tomas": [
        {"tipo": "portada", "n": 4, "beats": [N("Episodio cuatro: la promesa corregida. Si todavía no haces las etapas uno a tres, vuelve cuando las tengas.")]},
        {"tipo": "escalera", "titulo": "Dos columnas bajan el error", "beats": [
            N("Empecemos por el error, medido en los mismos cincuenta mercados de prueba. Pronosticar el promedio se equivoca en cuatro coma sesenta y ocho mil unidades."),
            N("El plano bajó a uno coma treinta y nueve."),
            N("Con la interacción, cero coma sesenta y cinco."),
            N("Y con la televisión al cuadrado, cero coma cuarenta y ocho. Dos columnas más, y el error es un tercio."),
        ]},
        {"tipo": "antesdespues", "titulo": "El patrón desaparece", "beats": [
            N("El mapa lo confirma. Este es el plano, con cuarenta mercados que fallan por más de dos mil unidades."),
            N("Y este es el plano doblado. El patrón desaparece: solo quedan dos."),
            N("Un mapa casi en blanco es la prueba que se le pide a cualquier ajuste antes de creerle."),
        ]},
        {"tipo": "radiotv", "titulo": "La radio depende de la TV", "beats": [
            N("Ahora, la consecuencia de negocio. La semana pasada la respuesta fue: los próximos mil dólares, a radio, en todas partes."),
            N("Esa es la línea gris. El plano dice que la radio rinde igual siempre."),
            N("Pero con cincuenta mil en televisión, cada mil dólares en radio deja sesenta y ocho dólares."),
            N("Con ciento cincuenta mil, mil trescientos sesenta."),
            N("Y con doscientos cincuenta mil, dos mil seiscientos cincuenta y dos."),
            N("Por debajo de cuarenta y cinco mil dólares en televisión, la radio no se paga."),
        ]},
        {"tipo": "promesacorr", "titulo": "La promesa corregida", "beats": [
            N("Y ahora, la cifra que importa."),
            N("El plan de Daniela no vende catorce mil cuatrocientas veinte unidades. Vende once mil setecientas setenta."),
            N("Son dos mil seiscientas cincuenta unidades que prometió de más."),
            N("¿Y la agencia? Sube a quince mil doscientas veinte, pero invierte setenta y seis mil dólares más."),
            N("Utilidad de Daniela: cuarenta y dos mil dólares. Utilidad de la agencia: siete mil setecientos."),
            D("La decisión se sostiene. La cifra no. Voy a tener que volver al comité."),
        ]},
    ]},
    {"id": "E05", "slug": "la-oferta-de-la-agencia", "titulo": "La oferta de la agencia", "cuando": "Después del episodio 4", "tomas": [
        {"tipo": "portada", "n": 5, "beats": [N("Episodio cinco: la oferta de la agencia.")]},
        {"tipo": "ilus", "img": "agencia", "beats": [
            A("Daniela, tu modelo de cuatro columnas está bien para empezar. Nosotros traemos uno de ochenta y tres.", "83\ncolumnas"),
            A("R cuadrado de cero coma nueve nueve ocho. Casi perfecto. Se equivoca en ciento cincuenta unidades.", "R² = 0,998"),
            D("¿Y en mercados nuevos?", "¿Y en\nmercados\nnuevos?"),
            N("Buena pregunta. Antes de seguir, apuesta. ¿Cuánto se equivoca en cincuenta mercados que no vio? Pausa y escribe tu número.", "Apuesta", pausa=PAUSA),
        ]},
        {"tipo": "clip", "base": "S4Grado", "titulo": "Más grado, menos verdad", "beats": [
            N("Para verlo con calma, tomemos solo trece mercados. Una recta, grado uno, no pasa por todos."),
            N("Subimos hasta el grado tres. Ya sigue mejor los puntos."),
            N("Seguimos: grado cinco, siete, nueve. La curva se retuerce y el error de entrenamiento sigue bajando."),
            N("Grado doce: pasa por sus puntos. El error de entrenamiento llega a cero."),
            N("Perfecto, ¿verdad? Ahora miremos los mercados que no vio."),
            N("El error de prueba, la línea roja, sube justo cuando el otro baja. El modelo se aprendió el ruido. Eso se llama sobreajuste."),
        ]},
        {"tipo": "grados", "titulo": "En el grado 5 la prueba se rompe", "beats": [
            N("Hagámoslo con los tres medios y los ciento cincuenta mercados. A la izquierda, el R cuadrado de entrenamiento sube con cada grado y nunca avisa."),
            N("A la derecha, el error de prueba baja hasta el grado tres."),
            N("En el grado cinco se rompe. En el seis, el de la agencia, llega a tres coma veinticinco."),
            N("Y en el grado siete, a casi cuarenta y tres. Peor que no tener modelo."),
        ]},
        {"tipo": "mercado", "titulo": "Pronostica ventas negativas", "beats": [
            N("¿Cómo se equivoca? Estos son los cincuenta mercados, de menor a mayor venta real. En negro, lo que vendieron."),
            N("En rojo, el pronóstico del grado seis. En cuarenta y cinco mercados el error es menor a dos mil. Se ve bien."),
            N("Y entonces aparece el mercado diecisiete."),
            N("El modelo le pronostica menos noventa y ocho mil unidades. Ventas negativas. Vendió doce mil quinientas."),
        ]},
        {"tipo": "ilus", "img": "mercado17", "beats": [
            N("Ese mercado tiene la inversión en prensa más alta de toda la base. Un sobreajuste no se equivoca parejo: se equivoca en los bordes, y no sabes de antemano en cuáles.", "Falla\nen los\nbordes"),
            D("No lo compro.", "No lo\ncompro"),
        ]},
    ]},
    {"id": "E06", "slug": "ridge-poner-un-precio", "titulo": "Ridge: poner un precio", "cuando": "Después del episodio 5", "tomas": [
        {"tipo": "portada", "n": 6, "beats": [N("Episodio seis. Ridge: poner un precio.")]},
        {"tipo": "freno", "titulo": "El modelo paga por usar coeficientes", "beats": [
            N("Las columnas de la agencia no son el problema. El problema es que nada le impide usarlas a lo loco. Hasta ahora el modelo tenía una sola meta: bajar el error."),
            N("Regularizar le agrega una segunda cosa: un precio por usar coeficientes grandes."),
            N("Ese precio lo controla una perilla que se llama lambda. En el código la vas a ver como alfa. Es lo mismo."),
            N("Con lambda cero, no hay freno: la cinta enredada de la agencia."),
            N("Con lambda enorme, todos los coeficientes valen cero y el modelo es el promedio. La respuesta buena está en el medio."),
        ]},
        {"tipo": "escala", "titulo": "El freno necesita una sola escala", "beats": [
            N("Antes de frenar, un detalle que parece menor. La televisión en miles de dólares tiene un coeficiente de cero coma cero cuatro cinco ocho."),
            N("Si la misma televisión estuviera en dólares, el coeficiente sería mil veces más chico."),
            N("El pronóstico es idéntico, pero ese coeficiente diminuto casi no pagaría. El freno castigaría la unidad, no la variable."),
            N("Por eso, antes de frenar, cada columna se pone en la misma escala: media cero, desviación uno."),
        ]},
        {"tipo": "clip", "base": "S5Ridge", "titulo": "Ridge encoge todas las columnas", "beats": [
            N("Volvamos a unos pocos mercados, con un polinomio de grado nueve. Sin freno, la curva se retuerce."),
            N("A la derecha, el tamaño de cada coeficiente. Son enormes, unos positivos y otros negativos, cancelándose entre sí."),
            N("Ridge cobra por el cuadrado de cada coeficiente. Esta es su cuenta: error más lambda por la suma de los cuadrados."),
            N("Subimos el freno. La curva se calma y todos los coeficientes se encogen a la vez."),
            N("Con mucho freno, la curva se aplana hasta el promedio. Frenamos de más."),
            N("En un punto intermedio queda lo mejor: la forma, sin las locuras."),
            N("Todas se encogen. Ninguna desaparece: por eso las nueve columnas siguen vivas."),
        ]},
        {"tipo": "ilus", "img": "ridge", "beats": [
            N("Piensa en Ridge como alguien que sostiene muchas correas. Las acerca todas, pero no suelta ninguna.", "Ridge\nno suelta\nninguna"),
            N("Por eso sirve cuando varias columnas dicen casi lo mismo: reparte el crédito entre ellas.", "Reparte\nel crédito"),
        ]},
    ]},
    {"id": "E07", "slug": "lasso-y-por-que-corta", "titulo": "Lasso y por qué corta", "cuando": "Después del episodio 6", "tomas": [
        {"tipo": "portada", "n": 7, "beats": [N("Episodio siete: Lasso, y por qué corta.")]},
        {"tipo": "clip", "base": "S6Lasso", "titulo": "Lasso apaga las que no pagan", "beats": [
            N("Lasso hace casi lo mismo, con una diferencia pequeña en la cuenta."),
            N("Mira las barras. Ya con muy poco freno hay columnas en cero."),
            N("Lasso cobra por el valor absoluto, no por el cuadrado."),
            N("Subimos el freno, y las columnas van cayendo a exactamente cero."),
            N("Al final quedan dos de nueve. Lasso eligió por su cuenta."),
            N("Las que no pagan su costo valen cero."),
        ]},
        {"tipo": "clip", "base": "S7Geometria", "titulo": "Por qué uno encoge y el otro corta", "beats": [
            N("¿Por qué uno encoge y el otro corta? La respuesta es una imagen. Cada elipse es un nivel de error, y el punto azul son los coeficientes sin freno."),
            N("El freno es un presupuesto: los coeficientes no se pueden salir de la zona. En Ridge la zona es un círculo. En Lasso, un rombo."),
            N("Al encoger el presupuesto, el mejor ajuste queda en el punto rojo, donde el error toca la zona."),
            N("El círculo no tiene esquinas, así que casi nunca toca un eje."),
            N("El rombo tiene las esquinas justo sobre los ejes. Y en una esquina, un coeficiente vale exactamente cero."),
        ]},
        {"tipo": "ilus", "img": "lasso", "beats": [
            N("Por eso Lasso es una tijera: corta los hilos que no sostienen nada.", "Lasso\ncorta"),
            N("Sirve cuando sospechas que casi todas las columnas sobran, y cuando necesitas decir cuáles importan.", "Dice\ncuáles\nimportan"),
        ]},
    ]},
    {"id": "E08", "slug": "ejercicio-contesten-la-oferta", "titulo": "Ejercicio: contesten la oferta", "cuando": "Se trabaja en grupos", "tomas": [
        {"tipo": "portada", "n": 8, "beats": [N("Episodio ocho. Ejercicio: contesten la oferta.")]},
        {"tipo": "ilus", "img": "validacion", "beats": [
            N("Falta una pregunta: ¿cuánto freno? Si lo eliges mirando los mercados de prueba, ya no son mercados que el modelo no vio.", "¿Cuánto\nfreno?"),
            N("La solución es hacer turnos.", "Turnos"),
        ]},
        {"tipo": "clip", "base": "S8Validacion", "titulo": "El freno se elige sin ver la prueba", "beats": [
            N("Partimos los ciento cincuenta mercados de entrenamiento en cinco grupos. Cada vez, cuatro entrenan y uno valida."),
            N("Un punto de la curva es el promedio de esos cinco turnos, para una fuerza de freno."),
            N("Repetimos con cada fuerza. Con demasiado freno, el error se dispara."),
            N("El punto más bajo es el alfa elegido. Y la prueba sigue guardada: se abre una sola vez, al final."),
        ]},
        {"tipo": "ejercicio", "etapa": 4, "nombre": "La oferta de la agencia", "pasos": [
            ("Ajusta polinomios de grado 1 a 7 con los tres medios.", "p = make_pipeline(\n  PolynomialFeatures(d,\n    include_bias=False),\n  StandardScaler(),\n  LinearRegression())"),
            ("Anota R² de entrenamiento, error de entrenamiento y error de prueba.", "p.score(tr[MEDIOS], tr.ventas)\nmae(te.ventas,\n    p.predict(te[MEDIOS]))"),
            ("Mira los errores del grado 6, mercado por mercado.", "abs(te.ventas\n    - p.predict(te[MEDIOS]))"),
            None], "beats": [
            D("La agencia me ofrece grado seis con R cuadrado de cero coma nueve nueve ocho. ¿Lo compro?", "La agencia me ofrece grado 6 con R² de 0,998. ¿Lo compro?"),
            N("Con los tres medios, ajusta polinomios de grado uno a siete en los ciento cincuenta de entrenamiento."),
            N("Para cada grado anota el R cuadrado de entrenamiento, el error de entrenamiento y el error de prueba."),
            N("Mira los errores del grado seis, mercado por mercado."),
            N("Pausa, y responde con el número que un comité entendería.", pausa=PAUSA),
        ]},
        {"tipo": "ejercicio", "etapa": 5, "nombre": "El freno", "pasos": [
            ("Grado 5 con 55 columnas. Para cada α, error con validación cruzada.", "cross_val_score(\n  freno(Lasso(alpha=a,\n    max_iter=300000)),\n  tr[MEDIOS], tr.ventas, cv=kf,\n  scoring=\"neg_mean_absolute_error\")"),
            ("Elige el mejor α de Lasso y de Ridge. Solo entonces mide en prueba.", "mae(te.ventas,\n    p.predict(te[MEDIOS]))"),
            ("Cuenta columnas vivas en Lasso. Mira qué pasa con α = 0,3.", "(p[-1].coef_ != 0).sum()"),
            None], "beats": [
            D("No descarto todas esas columnas todavía. Quiero ver si un freno las hace útiles.", "No descarto todas esas columnas. Quiero ver si un freno las hace útiles."),
            N("Toma el grado cinco, con cincuenta y cinco columnas. Para cada alfa de la lista, calcula el error con validación cruzada."),
            N("Elige el mejor alfa de Lasso y el mejor de Ridge. Solo entonces mide en los cincuenta de prueba."),
            N("Cuenta cuántas columnas quedan vivas en Lasso, y mira qué pasa con alfa cero coma tres."),
            N("Lasso tarda unos segundos. Pausa y decide: ¿la curva de cuatro columnas, o el Lasso?", pausa=PAUSA),
        ]},
    ]},
    {"id": "E09", "slug": "que-ajuste-se-queda", "titulo": "Qué ajuste se queda", "cuando": "Después de las etapas 4 y 5", "tomas": [
        {"tipo": "portada", "n": 9, "beats": [N("Episodio nueve: qué ajuste se queda. Mira este episodio cuando termines las etapas cuatro y cinco.")]},
        {"tipo": "rejilla", "titulo": "Lasso encontró la interacción sin ayuda", "beats": [
            N("Estos son los resultados. Arriba, cuántas de las cincuenta y cinco columnas sobreviven según la fuerza del freno."),
            N("Abajo, el error en validación. El mínimo está en alfa cero coma cero cero tres, con dieciséis columnas vivas."),
            N("Y mira lo que pasa con alfa cero coma tres. Quedan solo dos columnas: televisión, y televisión por radio."),
            N("Nadie se lo indicó. Lasso encontró por su cuenta la misma interacción que encontramos pensando en el negocio."),
        ]},
        {"tipo": "final", "conraiz": False, "titulo": "Error en los 50 mercados de prueba", "beats": [
            N("Comparemos en los cincuenta mercados de prueba. El plano: uno coma treinta y nueve."),
            N("El grado cinco sin freno: uno coma setenta."),
            N("Con Ridge, cero coma treinta y seis. Con Lasso, cero coma treinta y cinco. Los frenos rescataron las columnas."),
            N("La curva de cuatro columnas queda en cero coma cuarenta y ocho. Pierde por poco."),
            D("Con cuatro columnas puedo pararme frente al comité y explicar cada una."),
        ]},
        {"tipo": "ejercicio", "etapa": 6, "nombre": "En casa", "pasos": [
            ("Propón una columna con sentido de negocio y mide su error en los 50 de prueba.", 'tr["mi_columna"] = ...\n# en una frase: por qué tiene sentido'),
            ("Abre el dataset de CO₂ y toma seis mitades distintas.", 'mitad = co2.sample(frac=0.5,\n  random_state=seed)'),
            ("Sin freno, con Ridge y con Lasso: anota cuánto se mueve el consumo combinado.", "make_pipeline(StandardScaler(),\n  Ridge(alpha=50))\n# y Lasso(alpha=1)"),
            None], "beats": [
            D("Queda un último encargo. Propón una columna que tenga sentido de negocio y gánale a mi modelo. Y dime si el freno sirve cuando las columnas son casi copias.", "Propón una columna y gánale a mi modelo. Y dime si el freno sirve con columnas casi copias."),
            N("Piensa en cómo funciona la publicidad, escribe en una frase por qué tu columna tiene sentido, y mide el error en los mismos cincuenta mercados."),
            N("Luego abre el archivo de consumo de combustible, de un taller de años anteriores, y toma seis mitades distintas de los datos."),
            N("En cada una ajusta sin freno, con Ridge y con Lasso, y anota cuánto se mueve el coeficiente del consumo combinado."),
            N("Entrega tu memo, el enlace del cuaderno y tus prompts en la carpeta de la actividad.", pausa=2),
        ]},
    ]},
    {"id": "E10", "slug": "la-columna-pensada", "titulo": "La columna pensada", "cuando": "Después de entregar la etapa 6", "tomas": [
        {"tipo": "portada", "n": 10, "beats": [N("Episodio diez: la columna pensada. Míralo después de entregar la etapa seis.")]},
        {"tipo": "ilus", "img": "saturacion", "beats": [
            N("Si ya propusiste tu columna, comparemos. Piensa en la publicidad: las primeras pautas rinden mucho y las siguientes cada vez menos.", "Cada pauta\nrinde\nmenos"),
            N("Esa forma tiene nombre en matemáticas: raíz cuadrada.", "√TV"),
        ]},
        {"tipo": "raiz", "titulo": "La TV se satura rápido", "beats": [
            N("Estos son los mercados con poca radio. La curva gris usa televisión al cuadrado, y arranca demasiado alta."),
            N("La curva roja usa la raíz de la televisión: sube rápido, luego se aplana, y sigue los puntos desde el principio."),
        ]},
        {"tipo": "final", "conraiz": True, "titulo": "Cuatro columnas pensadas ganan", "beats": [
            N("Estos eran los modelos."),
            N("Con la raíz, el error de prueba baja a cero coma veintinueve."),
            N("Cuatro columnas pensadas le ganan a cincuenta y cinco. El freno es para cuando no sabes qué columnas importan. Si lo sabes, úsalo."),
        ]},
        {"tipo": "ilus", "img": "co2", "beats": [N("El segundo encargo. Consumo en ciudad, en carretera y combinado están correlacionados casi uno a uno.", "Casi\ncopias")]},
        {"tipo": "co2", "titulo": "Columnas casi copiadas", "beats": [
            N("Sin freno, el coeficiente del combinado va de menos ochenta y siete a más ciento noventa y ocho, según la mitad de datos que te toque."),
            N("Ridge reparte el crédito y se queda quieto, entre cinco y siete."),
            N("Lasso apaga unas y deja otras, y cuál apaga depende de la muestra."),
        ]},
        {"tipo": "guia", "titulo": "El síntoma elige el ajuste", "filas": [("Los errores forman un patrón", "Curva o transformación"), ("El efecto de una variable depende de otra", "Interacción"), ("Muchas columnas para pocas filas", "Ridge o Lasso"), ("Columnas casi copiadas", "Ridge"), ("Necesitas saber cuáles importan", "Lasso")], "beats": [
            N("Esto es lo que te llevas para tu proyecto. Si los errores forman un patrón, prueba una curva o una transformación."),
            N("Si el efecto de una variable depende de otra, una interacción."),
            N("Si hay muchas columnas para pocas filas, Ridge o Lasso."),
            N("Si las columnas son casi copias, Ridge."),
            N("Y si necesitas saber cuáles importan, Lasso."),
        ]},
        {"tipo": "ilus", "img": "experimento", "beats": [
            N("Y una advertencia. Un mejor ajuste no prueba causa. Los doscientos mercados se observaron: nadie asignó la radio al azar.", "No prueba\ncausa"),
            N("Además, Daniela pone cuarenta y nueve mil en radio, y el dato llega a cuarenta y nueve mil seiscientos. Ya está en el borde.", "Ya está\nen el borde"),
            N("Antes de mover la plata, hay que probar la radio en mercados elegidos al azar.", "Probar\nal azar"),
        ]},
        {"tipo": "cierre", "beats": [D("Voy a volver al comité con una cifra más baja, una razón clara y un experimento.", pausa=2)]},
    ]},
]


def todos_los_beats():
    for e in EPISODIOS:
        for t in e["tomas"]:
            for b in t["beats"]:
                yield b


def toma_por_id(sid):
    ep, i = sid.split("-")
    e = next(x for x in EPISODIOS if x["id"] == ep)
    return e, e["tomas"][int(i)]


def ids():
    return [f"{e['id']}-{i}" for e in EPISODIOS for i in range(len(e["tomas"]))]
