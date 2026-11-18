# Guía del profesor · Lunes 9 de noviembre de 2026

Regresión con ajustes. La clase retoma el caso Daniela donde quedó el miércoles 4 y usa los mismos 200 mercados y la misma división de 150 y 50. La pregunta de negocio es una sola: la cifra que Daniela llevó al comité, ¿se sostiene?

Deck: "Una recta no se dobla" (https://claude.ai/artifact/EgbKwaBmR3s5HDjVRnZmTt), 57 slides de clase y 6 de respaldo, con 39 animaciones sin sonido, copia local en `deck/` y PDF en `Una-recta-no-se-dobla.pdf`. Página de D2L: `d2l/semana11-regresion-con-ajustes.html`. Minutado para 80 minutos. Si son 90, los diez extra van a las salas B y a la plenaria final.

El calendario de agosto pone regresión simple hoy y polinomios el 16 de noviembre. Esta clase adelanta polinomios y agrega Ridge y Lasso, que no estaban en el sílabo. Las slides 20 y 21 del deck del 4 de noviembre (etapas 5 y 6 de Daniela) no entran en este minutado: si quieres cerrar esa entrega, salen de los 3 minutos iniciales de la etapa de salas.

## Antes de clase (15 minutos)

1. Sube a D2L la página, los dos CSV, el cuaderno y los ocho videos `animacion-*.mp4`, todos en la misma carpeta. La página los busca por nombre relativo.
2. Pon fecha de disponibilidad a la página, porque trae respuestas.
3. Crea la carpeta de entrega. La fecha propuesta es el domingo 15 a las 23:59 y sale de una constante en `generar_d2l.py`.
4. Abre `simulador-ajustes.html` en una pestaña. Presenta el deck en modo presentación: las animaciones arrancan solas al llegar a la slide, sin sonido, y un clic las pausa.
5. Salas de Zoom con los cinco grupos de siempre. Dos bloques de salas.

## Minutado

Las animaciones van sin sonido: las narras tú y el guion resumido está en las notas de cada slide. Cada una dura lo que indica su nota, queda quieta 40 segundos al final y un clic la pausa. Suman 17 minutos dentro de la clase.

| Minuto | Slides | Qué pasa |
|---|---|---|
| 0 a 5 | 1 a 4 | La promesa, apuesta y revelación |
| 5 a 9 | 5 a 8 | Cómo se ajusta una recta, mapa de errores, columnas y abanico |
| 9 a 14 | 9 a 13 | Cómo se separan las líneas, las cinco cosas de un prompt y los dos prompts |
| 14 a 18 | 14 a 21 | Qué es una interacción y cuatro ejemplos |
| 18 a 23 | 22 a 25 | Train y test: concepto, animación, cómo leer los dos errores y prompt |
| 23 a 24 | 26 a 29 | La receta y las pistas de prompt de las etapas 1 a 3, sin leerlas |
| 24 a 39 | 30 | Salas A: etapas 1, 2 y 3 |
| 39 a 46 | 31 a 35 | Plenaria: error, patrón, radio según TV, promesa corregida y errores de lectura |
| 46 a 50 | 36 a 39 | La agencia, el sobreajuste y el mercado 17 |
| 50 a 56 | 40 a 45 | Freno, escala, Ridge, Lasso, círculo y rombo |
| 56 a 58 | 46 a 49 | Validación cruzada, train, validación y test, y pistas de las etapas 4 y 5 |
| 58 a 70 | 50 | Salas B: etapas 4 y 5 |
| 70 a 75 | 51 a 54 | Resultados, guía de síntomas y límites |
| 75 a 80 | 55 a 57 | Etapa 6 en casa, su pista de prompt y cierre |

Las pistas de prompt también están en la página de D2L: en las salas los estudiantes las leen ahí.

Si no alcanza el tiempo, recorta en este orden: los ejemplos de las slides 19 y 20, el círculo y rombo de la slide 44, y los errores de la slide 35. No recortes las slides 22 a 25: train y test sostiene el resto de la clase.

Slides 58 a 60: respaldo (código y recorrido de ejercicios). Slides 61 a 63: raíz de TV y CO₂, se muestran solo después de entregar la etapa 6.

## Las etapas y sus respuestas

Margen 12 USD por unidad. Ventas en miles de unidades, inversión en miles de USD.

| Etapa | Pregunta de control | Respuesta | Decisión esperada |
|---|---|---|---|
| 1 Dónde falla | Exceso del plano en 20 mercados parecidos | 2,27 (vendieron 10,16, pronóstico 12,43, se pasó en los 20) | Es patrón: promete de más con un solo medio y se queda corto con los dos |
| 2 Doblar | Error de prueba con cuatro columnas | 0,48 (plano 1,39, solo interacción 0,65, línea base 4,68) | La interacción aporta más, la curva termina el trabajo |
| 3 La promesa | Pronóstico del plan de Daniela | 11,77 (plano decía 14,42). Agencia 15,22 | Sigue siendo mejor plan: utilidad +42,2 contra +7,7. Hay que bajar la cifra ante el comité |
| 4 La agencia | Error de prueba del grado 6 | 3,25 con R² de 0,998 en entrenamiento | No se compra: peor que el plano |
| 5 El freno | Columnas vivas con el mejor Lasso | 16 (α 0,003, error 0,35). Ridge α 0,03, 55 vivas, error 0,36. Sin freno 1,70 | Rescatan el grado 5, pero explicar 16 columnas cuesta. La curva de 4 pierde por poco y se explica sola |
| 6 En casa | Rango del coeficiente de CO₂ sin freno | −87 a +198. Ridge 5,4 a 7,2. Lasso lo apaga en 4 de 6 mitades | Ridge para copias, Lasso para seleccionar, ninguno si ya sabes qué columnas importan |

Columna que gana la etapa 6: raíz de TV. Con tv, raíz de tv, radio y tv × radio el error de prueba es 0,29.

Con α 0,3 Lasso deja solo tv y tv × radio, con error de 0,61. Es el momento más fuerte de la clase: encontró solo la misma interacción que encontramos pensando. Radio por cada mil USD: 89 unidades con TV 50, 197 con TV 150, 304 con TV 250. Equilibrio en 45 mil de TV.

## Qué decir en las salas

Una sola pregunta para todos en las salas A: ¿en qué unidad está tu respuesta? Es donde se pierden. Si un grupo dice que la radio rinde 0,09, son 89 unidades por cada mil dólares. En las salas B, la pregunta es: ¿viste la prueba antes de elegir α? Si la respuesta es sí, hay que elegir de nuevo con validación.

Un error típico en la etapa 3 es pronosticar con el modelo entrenado en 150 mercados. Para la promesa se usa el de 200, porque es la cifra que va al comité. El de 150 es el que se mide.

Si alguien propone poner más radio en el plan de Daniela: ya está en 49 mil y el dato llega a 49,6. Fuera de ese rango el modelo no sabe nada.

## Riesgos

**La teoría de Ridge se come las salas B.** Si al minuto 53 no llegaste a la slide 43, salta la 44 (círculo y rombo). La idea central es la 40.

**Las salas se quedan mudas mientras el asistente hace todo.** Roles fijos: uno pide, otro verifica una fila a mano, otro escribe la decisión.

**Lasso tarda o avisa que no converge.** Con `max_iter=300000` tarda segundos en Colab y converge. Si alguien usa el valor por defecto, verá una advertencia y números algo distintos.

**Las animaciones no cargan.** El PDF tiene el último cuadro de cada una y los mp4 están sueltos en `animaciones/`.

**El simulador con Lasso, pocos mercados y freno mínimo.** Con 20 mercados o menos y λ cerca de 0,001, Lasso no alcanza a converger y la curva puede verse más tranquila de lo que debería. Desde λ 0,01 se comporta bien. El error de prueba aparece como signo de pregunta hasta que marcas Mostrar mercados que no vio.

## Sobre los datos

Revisé cinco candidatos con el mismo procedimiento: línea base, polinomios de grado 1 a 7, Ridge y Lasso, con validación cruzada.

| Dataset | Veredicto | Por qué |
|---|---|---|
| Bebidas Cumbre (Advertising, 200 mercados) | **Se usa** | La curvatura y la interacción son reales: el error cae a un tercio. El grado 5 se rompe y el freno lo rescata. Continúa el caso |
| Consumo de combustible CO₂ (taller de 2024 y 2025) | Se usa en casa | Columnas correlacionadas 0,996: es el trabajo natural de Ridge |
| Influencers (`advertising_and_sales_clean`) | Descartado | TV correlaciona 0,999 con ventas. No hay nada que mejorar |
| `marketing_mensual` de Comercial Andina | Descartado | 31 filas y causalidad inversa ya conocida. Se rompe desde el grado 2 |
| FIFA 21 (Caso 3) | Queda para el proyecto | Sirve para Ridge, pero la limpieza se comería la clase |

Limitación honesta del dataset principal: solo tiene tres medios y poca correlación entre ellos (máximo 0,35). Ridge y Lasso solo importan cuando se expanden las columnas. Por eso la etapa 6 trae un dataset donde las columnas ya vienen casi copiadas.

Sobre la cifra del grado 6: el error medio de 3,25 lo infla un solo mercado, el 17, con la prensa más alta de la base (114 mil). En 45 de los 50 mercados el error es menor a 2 mil. Dilo así, porque es la forma real en que falla un sobreajuste.

## Qué se tomó de años anteriores

Del cuaderno `LinearRegEjercicio_AnalisisDatos` (2024) vienen la normalización antes de ajustar, el ajuste polinómico y el dataset de CO₂, con sus columnas casi copiadas. De `reg_lineal_multiple` viene el gráfico del plano y la pregunta por la prensa. De `lab_13` vienen los grados que hunden la validación, el experimento de las mitades que cambian el signo del coeficiente y la lectura de que al plano le falta un término. El encuadre de negocio sigue el caso Daniela de la semana pasada.

## Animaciones y skills

Se buscaron skills de animación en el registro abierto y se usaron como referencia `manim-composer` y `manimce-best-practices`, de `adithya-s-k/manim_skill`. No se instalaron en el proyecto. Las escenas están en `animaciones/escenas.py` y se regeneran con `animaciones/render.sh`, que necesita Manim en el `PATH`.
