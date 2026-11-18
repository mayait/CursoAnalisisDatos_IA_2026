# Guía del profesor · Miércoles 4 de noviembre de 2026

Sesión única de la semana (el lunes 2 fue feriado). La recta ya se explicó: no se repasa. La clase va de Teachable Machine directo al caso Daniela, y el caso sube la escalera del curso: describir, diagnosticar, predecir y prescribir. Diseño revisado con un asesor curricular independiente.

Deck: "Seis decisiones con una recta" (https://claude.ai/artifact/JvXAeJauqWYmtuhNTJUUEQ), 22 slides, copia local en `deck/`. Página del caso en D2L, Semana 10, con candados. Minutado para 80 minutos; si son 90, los diez extra van a la etapa 4 y a la plenaria final.

## Antes de clase (15 minutos)

1. Publica en D2L los módulos Semana 9 y Semana 10 cuando quieras. El Deber 10 conviene publicarlo antes de clase para que los grupos vean la rúbrica.
2. La página del caso tiene fecha de disponibilidad a las 10:00.
3. Salas de Zoom con los cinco grupos de siempre. Solo dos bloques de salas.
4. Cronómetro visible para Teachable Machine.

## Minutado

| Minuto | Slides | Qué pasa |
|---|---|---|
| 0 a 2 | 1 | Pregunta de apertura sin contestar: ¿quién va a hacer algo distinto el lunes gracias a su modelo? |
| 2 a 27 | 2 | Teachable Machine: cuatro minutos de demo y uno de preguntas por grupo. Corte duro a los cinco. |
| 27 a 29 | 3 y 4 | Puente: Teachable Machine vive en el escalón predictivo. No dice por qué (miles de parámetros) ni qué hacer. Una recta tiene dos parámetros que se leen en voz alta. |
| 29 a 32 | 5 y 6 | Daniela, unidades y margen. Tres roles por sala: pide, verifica, decide. Número escrito antes de abrir el candado. |
| 32 a 46 | 7 y 9 | Salas: etapas 1 (describir) y 2 (diagnosticar). |
| 46 a 51 | 8, 10 y 11 | Plenaria. Un grupo lee su frase del R². Slide 11: la pendiente en dólares, 47,5 × 12 = 570. |
| 51 a 69 | 12 y 14 | Salas: etapas 3 (predecir) y 4 (prescribir). |
| 69 a 77 | 13, 15, 16 y 17 | Plenaria. Dos grupos leen su decisión con el número. Escalera completa. |
| 77 a 80 | 18 y 19 | Etapas 5 y 6 en casa. Entrega el domingo 8 a las 23:59. |

Las slides 20 y 21 son respaldo de las etapas 5 y 6 para el lunes 9, después de la entrega.

## Las etapas y sus respuestas

Margen del caso: 12 USD por unidad. Ventas en miles de unidades, inversión en miles de USD.

| Etapa | Escalón | Pregunta de control | Respuesta | Decisión esperada |
|---|---|---|---|---|
| 1 Mirar | Descriptivo | Correlación prensa y ventas | 0,23 (TV 0,78, radio 0,58) | Rectas para TV y radio. La prensa es una nube. |
| 2 La recta de TV | Diagnóstico | R² de ventas contra TV | 0,61. Pendiente 0,0475: 47,5 unidades por mil USD | La TV explica el 61 % de las diferencias entre mercados. No dice si se paga ni que cause las ventas. |
| 3 El mercado nuevo | Predictivo | Pronóstico del plan de la agencia | 14,48 miles. Daniela: 14,42 | Agencia: 173,8 mil de margen contra 175 de publicidad, no se paga. Daniela: 173,0 contra 99. Lanzar con el plan de Daniela. |
| 4 Mover el presupuesto | Prescriptivo | Unidades por mil USD en radio | 202,5 | Radio +1.430 por cada mil, TV −430, prensa −344. Los próximos mil a radio. La TV explica más y rinde menos. |
| 5 ¿Confiamos? (casa) | Predictivo | Error de TV y radio en prueba | 1,39 (línea base 4,68, TV 2,27, tolerancia 2) | Cumple la tolerancia. Peor caso de Daniela: 139,2 mil contra 99, resiste. |
| 6 ¿Sacamos la prensa? (casa) | Diagnóstico | Coeficiente de prensa con los tres medios | −0,0010, p 0,86 | Sacarla, primero en mercados elegidos al azar. Se llevaba el crédito de la radio (correlación 0,35). R² ajustado 0,8956 con prensa y 0,8962 sin ella. |

## Qué decir en las salas

Una sola pregunta, la misma para todos: ¿cuántos dólares deja esa pendiente? Es donde se pierden. Una pendiente de 0,0475 son 47,5 unidades por cada mil dólares, no 0,0475 unidades. Si un grupo dice que la TV no vende nada, es esto.

En la etapa 3 el error típico es comparar miles de unidades con miles de dólares sin multiplicar por el margen. En la etapa 4, confundir el R² con rentabilidad: es la idea central del día. Si alguien propone poner todo en radio, el modelo nunca vio más de 49,6 mil en radio: fuera del rango la recta no sabe nada.

## Riesgos

**Teachable Machine se come el caso.** Si al minuto 30 no empezó el caso, la etapa 4 pasa a la casa y sus slides se proyectan el lunes.

**Las salas se quedan mudas mientras el asistente hace todo.** Roles fijos: uno pide, otro verifica una fila a mano, otro escribe la decisión. Mensaje a todas las salas con el tiempo restante.

**Leen la cifra y no la decisión.** En las plenarias se llama a un grupo al azar a leer su decisión con el número. Una frase sin número no vale.

## Sobre los datos

El CSV es el conjunto clásico Advertising (200 mercados), con columnas en español y presentado como Bebidas Cumbre, una marca ficticia. Es conocido y lab_12, que está en el repo público, trae varias de estas cifras: por eso la rúbrica califica el razonamiento y no solo el número. Gráficas del deck: `generar_figuras_deck.py`. Página D2L y cifras: `generar_d2l.py`.

El deck del 26 tenía mal la ecuación de TV y radio en la slide "Con dos variables, la recta es un plano". Quedó corregida: 2,92 + 0,0458 · TV + 0,188 · Radio, R² 0,90.
