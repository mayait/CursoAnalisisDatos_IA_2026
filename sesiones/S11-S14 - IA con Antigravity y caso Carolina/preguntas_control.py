# -*- coding: utf-8 -*-
"""Preguntas de control de selección para el caso Carolina.

Cada pregunta: (enunciado, [(opción, es_correcta, retroalimentación)], prompt de revisión).
La opción correcta sale de la solución de referencia (Instructor_Unificar_Bases).
Las opciones incorrectas corresponden a los errores típicos del caso: la retroalimentación
dice cuál es el engaño y el prompt de revisión se muestra junto a ella.
"""

OK = "Cuadra. Anoten la cifra en contexto/CONTEXTO.md y sigan con la siguiente pregunta."

MC = {
1: [
 ("¿Cuántos VIN distintos hay en total y en cuántos contenedores?", [
   ("4.327 VIN en 1.080 contenedores", True, OK),
   ("4.386 VIN en 1.080 contenedores", False, "Hay VIN contados dos veces. El mismo chasis viene escrito con minúsculas, espacios, guiones o el prefijo «VIN:». Hay que limpiar el VIN antes de contar."),
   ("4.327 VIN en más de 1.200 contenedores", False, "Los VIN están bien, pero el contenedor no se normalizó: en el control de Suzuki viene con un espacio en medio y el mismo contenedor se cuenta dos veces."),
   ("Otro número, o aparecen filas con el nombre del buque o VIN sin ETA", False, "Antigravity leyó la cabecera de los packing lists de Toyota como si fueran datos. La tabla empieza en la fila 12 y la ETA solo está en la cabecera."),
  ], "¿Cómo limpiaste el VIN y el contenedor antes de contar? Muéstrame 10 ejemplos antes y después. ¿En qué fila empieza la tabla de cada packing list de Toyota y cómo sacaste la ETA de la cabecera?"),
 ("¿Cuántas marcas aparecen en la base de importaciones?", [
   ("Cinco: Toyota, Changan, Suzuki, Peugeot y Opel", True, OK),
   ("Tres: Toyota, Suzuki y Changan", False, "No leyeron todas las hojas del control de Nexumcorp. Changan, Peugeot y Opel vienen cada una en una hoja distinta del mismo archivo."),
   ("Dos: Toyota y Suzuki", False, "El control de importaciones de Nexumcorp no entró en la base. Revisen que el plan incluya los tres archivos de 01_importaciones."),
  ], "Lista todas las hojas de cada archivo de importaciones y cuántas filas leíste de cada una."),
 ("¿Cuántos VIN tiene Toyota y en cuántos contenedores?", [
   ("2.110 VIN en 544 contenedores", True, OK),
   ("Menos de 2.000 VIN", False, "Faltan packing lists o se perdieron filas al leerlos. Son 66 archivos, uno por embarque, y en todos la tabla empieza en la fila 12."),
   ("Más de 2.110 VIN", False, "Hay VIN repetidos por formato o se están contando filas de cabecera como vehículos."),
  ], "¿Cuántos packing lists de Toyota leíste y cuántas filas de vehículos sacaste de cada uno?"),
 ("¿Cuántos VIN tuvieron que limpiarse?", [
   ("59", True, OK),
   ("Cero", False, "Antigravity comparó el texto tal cual y no revisó el formato. Los 59 están escondidos: minúsculas, espacios, guiones o el prefijo «VIN:»."),
   ("Más de 500", False, "Está contando como «sucio» algo normal, por ejemplo convertir todo a mayúsculas aunque ya lo estuviera. Pidan solo los VIN que cambiaron."),
  ], "Muéstrame solo los VIN que cambiaron al limpiarlos, con el valor original, el limpio y el archivo de donde sale cada uno."),
 ("¿Cuántos vehículos son año modelo 2026 y cuántos 2027?", [
   ("3.612 de 2026 y 715 de 2027", True, OK),
   ("Cerca de 900 vehículos quedan sin año modelo", False, "Suzuki no trae la columna de año modelo. Se deduce del décimo carácter del VIN y nadie se lo pidió a Antigravity."),
   ("Todos son 2026", False, "El año se tomó de la fecha de embarque o de la ETA, no del vehículo. El año modelo es otra cosa."),
  ], "¿De dónde sacaste el año modelo de cada marca? Para Suzuki, explícame la regla del décimo carácter del VIN y muéstrame 5 ejemplos."),
 ("¿Qué mes de ETA tiene más unidades?", [
   ("Septiembre, con 925", True, OK),
   ("Hay unidades sin mes de ETA", False, "Las fechas de Suzuki vienen como texto con el mes en inglés y no se convirtieron."),
   ("Aparecen meses fuera de mayo a octubre", False, "Se intercambió el día con el mes al convertir alguna fecha. Revisen el formato de fecha de cada archivo."),
  ], "¿En qué formato venían las fechas de cada archivo y cómo las convertiste? ¿Cuántas no pudiste convertir? Dame el conteo de unidades por mes de ETA."),
],
2: [
 ("¿Cuántos contenedores aparecen en la liquidación de aduana, cuántos arribaron y cuántos tienen levante?", [
   ("876 aparecen, 787 arribaron y 763 tienen levante", True, OK + " Los 204 que no aparecen todavía no llegan."),
   ("Menos de 500 aparecen", False, "El contenedor no se normalizó. El agente de aduana lo escribe con espacios, guiones y el dígito de control separado, y el cruce no encuentra la pareja."),
   ("Los 1.080 tienen fecha de arribo", False, "Antigravity rellenó fechas que no existen. 204 contenedores no aparecen en aduana: no han llegado y su fecha debe quedar vacía."),
  ], "Muéstrame 10 contenedores tal como vienen en aduana y cómo quedaron después de normalizarlos. ¿Cuántos contenedores de importaciones no encontraste en aduana?"),
 ("¿Cuántos VIN están en agencia al 17 de septiembre?", [
   ("2.690 (y 1.309 en tránsito, 112 en aduana, 216 nacionalizados)", True, OK),
   ("Unos 2.000 en agencia y más de 800 nacionalizados", False, "Descartaron los VIN de traslados que vienen incompletos. Esas unidades ya llegaron a la agencia pero aparecen como si siguieran en el patio."),
   ("Más de 1.500 en tránsito", False, "El contenedor no se normalizó y muchos VIN quedaron sin fecha de arribo."),
  ], "¿Cuántos VIN de traslados leíste, cuántos encontraste en importaciones y cuántos descartaste? ¿Cómo separaste los VIN que vienen juntos en una misma celda?"),
 ("¿Cuántos VIN de traslados vienen incompletos y cómo se resuelven?", [
   ("645, con solo los últimos 8 caracteres; se reconstruyen buscándolos en importaciones", True, OK),
   ("Ninguno", False, "Antigravity los descartó en silencio o no separó las celdas que traen varios VIN con comas, saltos de línea o barras."),
   ("701", False, "Eso son las guías de traslado, no los VIN. Una guía puede llevar varios vehículos."),
  ], "Muéstrame 5 VIN de traslados que venían incompletos, cómo los reconstruiste y en qué archivo encontraste el VIN completo. ¿Alguno quedó ambiguo?"),
 ("De las 527 que Nexumcorp marca EN TRANSITO, ¿cuántas están mal marcadas?", [
   ("133: 38 ya están en aduana, 50 nacionalizadas y 45 en agencia", True, OK + " 95 de esas 133 ya tienen levante."),
   ("Ninguna, las 527 siguen en tránsito", False, "Antigravity copió la columna de estado de Nexumcorp, que se llena a mano. El estado se calcula con las fechas de aduana y traslados, no se copia."),
   ("Las 527", False, "La comparación falló por el texto, por ejemplo «EN TRANSITO» contra «En tránsito». Normalicen el texto antes de comparar."),
  ], "¿El estado de los VIN de Nexumcorp sale de su columna de estado o de las fechas de aduana y traslados? Recalcúlalo solo con fechas y compara."),
],
3: [
 ("¿Cuántas filas trae el ERP de Toyota y cuántas están repetidas?", [
   ("18.864 filas, de las cuales 922 están repetidas", True, OK),
   ("18.864 filas y ninguna repetida", False, "Agosto se exportó desde el 30 de julio y septiembre desde el 31 de agosto. Hay filas que aparecen en dos archivos."),
   ("Una sola columna o muy pocas filas", False, "El CSV se leyó mal: usa punto y coma como separador, coma decimal y codificación de Windows."),
  ], "¿Con qué separador, decimal y codificación leíste cada CSV de Toyota? ¿Qué rango de fechas trae cada uno y cuántas filas se repiten entre archivos?"),
 ("¿Cuántas facturas de vehículos nuevos hay y cuántas están anuladas?", [
   ("2.105 facturas, 33 anuladas (18 Toyota, 7 Nexumcorp, 8 Suzuki)", True, OK),
   ("Menos de 33 anuladas", False, "Cada sistema anula distinto: Toyota con una nota de crédito que apunta a la factura original en DOC_REFERENCIA, Nexumcorp con la columna Estado y Suzuki con EST en V o A. Si solo buscaron la palabra «anulada», se colaron algunas."),
   ("Ninguna anulada", False, "No se revisó cómo marca las anulaciones cada sistema."),
  ], "Explícame cómo marca las anulaciones cada sistema y muéstrame dos ejemplos de cada uno, con la factura original y lo que la anula."),
 ("¿Cuántos VIN nuevos tienen factura vigente?", [
   ("2.069: Casabaca 616, Toyocosta 420, Nexumcorp 607, Suzuki 426", True, OK),
   ("Más de 2.100, con unas 60 dobles facturaciones", False, "No se quitaron las filas repetidas por el solape entre los CSV de Toyota."),
   ("Unos 2.050", False, "Botaron las facturas cuyo VIN no aparece en importaciones. Carolina pidió corregirlas, no botarlas."),
   ("Más de 2.300", False, "Se colaron los seminuevos: 66 de Casabaca en el ERP y 237 de 1001Carros. No pasan por importación y no cuentan."),
  ], "¿Cuántas facturas vigentes de vehículos nuevos tienes por empresa antes y después de cruzar con importaciones? ¿Qué facturas quedaron sin VIN y por qué?"),
 ("¿Cuántos VIN mal digitados corrigieron?", [
   ("18: 9 en Toyota, 5 en Nexumcorp y 4 en Suzuki", True, OK),
   ("Ninguno", False, "No se revisaron las facturas que no cruzan con importaciones. Confunden 0 y O, 1 e I, 5 y S, 8 y B, 2 y Z o 6 y G, o traen dos dígitos transpuestos."),
   ("Más de 18, algunas con dudas", False, "Antigravity está forzando coincidencias. Cada corrección debe compartir los primeros once caracteres y cuadrar con el dígito verificador."),
  ], "Para cada corrección dime el VIN original, el propuesto, qué caracteres cambiaron, si comparten los primeros once caracteres y si el dígito verificador (noveno carácter) cuadra."),
 ("¿Cuántos colores facturados son distintos del importado?", [
   ("12", True, OK),
   ("Casi todas las facturas", False, "Compararon el nombre de fábrica en inglés con el nombre comercial. La hoja Colores del maestro traduce uno al otro."),
   ("Ninguno", False, "La comparación no se hizo o se hizo contra la misma columna."),
  ], "¿Cómo comparaste el color facturado con el importado? ¿Usaste la hoja Colores del maestro? Muéstrame los 12 casos."),
 ("¿Cuánto suma la facturación vigente de Suzuki?", [
   ("USD 8.523.120,25", True, OK),
   ("USD 8.669.196,17", False, "Incluyeron las facturas anuladas."),
   ("Más del doble", False, "Sumaron las filas de subtotal por mes y el total general que vienen entre los datos del reporte de Suzuki."),
  ], "¿Qué filas del reporte de Suzuki son subtotales o totales y cómo las excluiste? Suma solo las facturas vigentes."),
],
4: [
 ("¿Qué hay en los 166 PDF de actas escaneadas?", [
   ("144 actas de nuevos y 22 de seminuevos; 15 son copias de actas ya digitadas", True, OK),
   ("Antigravity no pudo leerlos", False, "Pidan que extraiga el texto de los PDF con una librería de Python. No hace falta abrirlos a mano."),
   ("166 actas de vehículos nuevos", False, "No separaron los seminuevos, que no cuentan para este análisis."),
  ], "¿Cómo leíste los PDF? Muéstrame el VIN, la fecha y la empresa de 5 actas escaneadas y dime cuáles ya estaban en el registro digitado."),
 ("¿Cuántos vehículos nuevos están por entregar?", [
   ("331", True, OK),
   ("462", False, "No leyeron los PDF. Hay 132 vehículos ya entregados cuya acta solo existe escaneada."),
   ("327, y aparecen 17 entregados sin factura", False, "No se usaron los 18 VIN corregidos de la parte 3 y esas facturas quedaron huérfanas."),
   ("Otro número", False, "Revisen la definición: factura vigente y sin acta, ni digitada ni escaneada. Las copias escaneadas no duplican entregas."),
  ], "¿Incluiste las actas escaneadas como entregas? ¿Usaste las facturas con el VIN corregido de la parte 3? Muéstrame cuántos por entregar tienes antes y después de cada paso."),
 ("¿Cuántos de los 331 están listos para entrega?", [
   ("154 (y 77 con PDI pendiente, 32 nacionalizados, 13 en aduana, 55 en tránsito)", True, OK + " Las 55 en tránsito no son un error: son ventas anticipadas."),
   ("Menos de 154 y más con PDI pendiente", False, "No se tomó la última inspección: 212 vehículos tienen más de una. O no se limpió el VIN del export de PDI, que trae 52 en minúsculas."),
   ("Ninguno está en tránsito", False, "Antigravity quitó las 55 facturadas en tránsito creyendo que eran un error. Son ventas anticipadas y cuentan."),
  ], "¿Qué inspección usaste cuando un vehículo tiene varias? ¿Limpiaste el VIN del export de PDI antes de cruzar?"),
 ("¿Cuántas actas siguen solo escaneadas?", [
   ("132: 127 dentro del rezago normal y 5 traspapeladas, con más de 10 días", True, OK),
   ("132 traspapeladas", False, "No aplicaron el umbral de 10 días del correo. La digitación normal tarda hasta 9."),
   ("147", False, "Contaron también las 15 copias de actas que ya estaban digitadas."),
  ], "¿Cuántos días pasaron entre la fecha de cada acta escaneada y el corte? Muéstrame solo las que pasan de 10 días."),
 ("¿Cuántos vehículos se entregaron sin factura vigente?", [
   ("3 (y además 6 sin PDI aprobado y 4 con acta anterior a la factura)", True, OK),
   ("17 o más", False, "Son las facturas con VIN mal digitado que no se corrigieron en la parte 3."),
   ("Ninguno", False, "No se cruzaron las entregas con las facturas vigentes, solo las pendientes."),
  ], "Para cada alerta dame el VIN, la empresa, las fechas que la disparan y el archivo de donde sale cada fecha."),
],
5: [
 ("¿Cuántos vehículos están atrasados según la regla?", [
   ("47, todos listos para entrega", True, OK),
   ("77", False, "Marcaron como atrasados los 30 cuya fecha cae justo hoy, viernes 18. Vencer hoy no es estar atrasado."),
   ("Más de 77", False, "Contaron días calendario en lugar de días hábiles de lunes a viernes sin feriados."),
  ], "¿Contaste días hábiles sin feriados? ¿Cómo tratas una fecha que cae exactamente el 18 de septiembre? Muéstrame 3 atrasados con cada fecha de la regla."),
 ("¿Hay fechas estimadas antes del viernes 18?", [
   ("No. 47 atrasadas y 30 a tiempo quedan con fecha 18", True, OK),
   ("Sí, varias", False, "Olvidaron el piso: ninguna fecha puede quedar antes de hoy. Si la regla da una fecha pasada, se marca atrasada y se pone el 18."),
  ], "¿Hay alguna fecha estimada antes del 18 de septiembre? Aplica el piso del correo y dime cuántas cambian."),
 ("¿Cuál es la fecha estimada más lejana?", [
   ("4 de noviembre", True, OK),
   ("Un día hábil antes", False, "No restaron un feriado del maestro. El 9 de octubre cae dentro del horizonte."),
   ("Varios días después", False, "Se sumaron días calendario o se contó algún paso de la regla dos veces."),
  ], "¿Qué feriados usaste y de qué hoja del maestro salen? Muéstrame paso por paso la fecha del vehículo más lejano."),
 ("¿Cuántas alertas tiene la hoja Alertas?", [
   ("81", True, OK),
   ("Más de 130", False, "Se colaron las dobles facturaciones falsas del solape de Toyota o los colores sin traducir. Vuelvan a las preguntas de la parte 3."),
   ("Menos de 81", False, "Faltan tipos de alerta. Revisen que las alertas de las partes 3 y 4 se hayan pasado al Excel."),
  ], "Cuenta las alertas por tipo en la hoja Alertas y compáralas con lo que reportaste en las partes 3 y 4."),
 ("Borren una fila de la hoja Por entregar. ¿Qué pasa con el Resumen?", [
   ("Los conteos bajan en uno", True, OK + " Deshagan el cambio antes de guardar."),
   ("No cambia nada", False, "Antigravity escribió los números como valores y no como fórmulas."),
  ], "Reescribe el Resumen con fórmulas CONTAR.SI y CONTAR.SI.CONJUNTO sobre las hojas Por entregar y Alertas. Muéstrame la fórmula de tres celdas."),
],
}


# Desde la parte 2 la retroalimentación no trae el prompt escrito: trae una pista de qué pedir.
REV_PISTA = {
2: ["Pidan ejemplos del contenedor antes y después de normalizarlo, y cuántos contenedores de importaciones quedaron sin pareja en aduana.",
    "Pidan cuántos VIN de traslados leyó, cuántos cruzó y cuántos descartó, y cómo separó los VIN que vienen juntos en una celda.",
    "Pidan ejemplos de VIN incompletos, cómo se reconstruyeron y si alguno quedó ambiguo.",
    "Pregunten de dónde sale el estado de los VIN de Nexumcorp, si de su columna o de las fechas, y pidan recalcularlo solo con fechas."],
3: ["Pidan el separador, el decimal, la codificación y el rango de fechas de cada CSV, y cuántas filas se repiten entre archivos.",
    "Pidan que explique cómo anula cada sistema, con dos ejemplos de cada uno.",
    "Pidan el conteo de facturas vigentes por empresa antes y después del cruce, y qué facturas quedaron sin VIN.",
    "Pidan, para cada corrección, el VIN original, el propuesto, qué caracteres cambiaron y si el dígito verificador cuadra.",
    "Pregunten con qué compararon el color y si usaron la hoja Colores del maestro.",
    "Pregunten qué filas del reporte de Suzuki son subtotales o totales y cómo las excluyó."],
4: ["Pregunten cómo leyó los PDF y pidan cinco actas con su VIN, fecha y empresa.",
    "Pidan el número de por entregar antes y después de sumar las actas escaneadas y los VIN corregidos.",
    "Pregunten qué inspección usa cuando un vehículo tiene varias y si limpió el VIN del export de PDI.",
    "Pidan los días entre cada acta escaneada y el corte, y solo las que pasan de 10.",
    "Pidan cada alerta con el VIN, las fechas que la disparan y el archivo de donde sale cada fecha."],
5: ["Pregunten si contó días hábiles sin feriados y cómo trata una fecha que cae justo el 18.",
    "Pidan cuántas fechas quedan antes del 18 y que aplique el piso.",
    "Pidan el cálculo paso a paso del vehículo más lejano y qué feriados usó.",
    "Pidan el conteo de alertas por tipo y compárenlo con lo que reportaron en las partes 3 y 4.",
    "Pidan que el Resumen use fórmulas sobre las otras hojas y que les muestre tres de ellas."],
}
