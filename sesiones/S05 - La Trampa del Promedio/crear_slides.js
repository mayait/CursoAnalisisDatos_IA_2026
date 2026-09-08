// Slides Sesión 5 · La trampa del promedio · ADM 2003
// Regla de la casa: fondo blanco siempre. Identidad USFQ: rojo A6192E sobre blanco.
// Estructura Winston: promesa → caso en tres actos (apuesta/reveal) → regla → contribuciones.
// Uso:  NODE_PATH=<node_modules> node crear_slides.js
const pptxgen = require("pptxgenjs");

const BG = "FFFFFF", TINTA = "1E1E1E", MUTED = "6B6B6B", ACC = "A6192E", CARD = "FBEDEF";
const F = "Arial";
const IMG = "img/";

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.33 x 7.5
pres.author = "ADM 2003 · USFQ Galápagos";
pres.title = "Sesión 5 · La trampa del promedio";

function nueva(kicker, nota) {
  const s = pres.addSlide();
  s.background = { color: BG };
  if (kicker) {
    s.addText(kicker, { x: 0.75, y: 0.52, w: 11.8, h: 0.4, fontFace: F, fontSize: 13,
      bold: true, color: ACC, charSpacing: 2, isTextBox: true, margin: 0 });
  }
  if (nota) s.addNotes(nota);
  return s;
}

// im: [wpx, hpx] reales del PNG → coloca centrado horizontal con ancho dado
function figura(s, file, wpx, hpx, w, y) {
  const h = w * hpx / wpx;
  s.addImage({ path: IMG + file, x: (13.33 - w) / 2, y: y, w: w, h: h });
  return y + h;
}

// ── 1 · Portada ──────────────────────────────────────────────────────────────
let s = nueva(null,
  "0-2 min. Luces plenas. Nada de chistes ni disculpas de apertura: saludo corto y directo a la promesa (siguiente slide). Los dos números de la derecha quedan sin explicar a propósito: son el anzuelo.");
s.addText("ADM 2003 · ANÁLISIS DE DATOS CON IA Y PYTHON · SESIÓN 5", { x: 0.75, y: 1.3,
  w: 11.5, h: 0.4, fontFace: F, fontSize: 13, bold: true, color: ACC, charSpacing: 2,
  isTextBox: true, margin: 0 });
s.addText("La trampa\ndel promedio", { x: 0.7, y: 1.85, w: 7.5, h: 2.75, fontFace: F,
  fontSize: 60, bold: true, color: TINTA, isTextBox: true, margin: 0, lineSpacing: 66 });
s.addText("Tres preguntas fáciles.\nTres decisiones a punto de arruinarse.", { x: 0.75,
  y: 4.85, w: 7.2, h: 1.1, fontFace: F, fontSize: 20, color: MUTED, isTextBox: true,
  margin: 0, lineSpacing: 28 });
s.addText("$459", { x: 8.75, y: 1.95, w: 3.9, h: 1.0, fontFace: F, fontSize: 64,
  bold: true, color: ACC, isTextBox: true, margin: 0 });
s.addText("lo que dice el promedio", { x: 8.8, y: 3.0, w: 3.9, h: 0.4, fontFace: F,
  fontSize: 14, color: MUTED, isTextBox: true, margin: 0 });
s.addText("$152", { x: 8.75, y: 3.75, w: 3.9, h: 1.0, fontFace: F, fontSize: 64,
  bold: true, color: TINTA, isTextBox: true, margin: 0 });
s.addText("lo que vale el pedido típico", { x: 8.8, y: 4.8, w: 3.9, h: 0.4, fontFace: F,
  fontSize: 14, color: MUTED, isTextBox: true, margin: 0 });
s.addText("Semana 3 · Lunes 31 de agosto de 2026 · USFQ Galápagos", { x: 0.75, y: 6.9,
  w: 11.5, h: 0.35, fontFace: F, fontSize: 12, color: MUTED, isTextBox: true, margin: 0 });

// ── 2 · La promesa ───────────────────────────────────────────────────────────
s = nueva("LA PROMESA",
  "2-4 min. Leer casi literal: 'Al salir de esta sala vas a poder detectar, en tres minutos y con dos números, cuándo un promedio está mintiendo, y vas a saber qué número pedir en su lugar. Eso vale un presupuesto entero.' Es la idea que se repite tres veces hoy (promesa, regla, contribuciones).");
s.addText([
  { text: "Al salir de esta sala vas a poder\n", options: { color: TINTA } },
  { text: "detectar en tres minutos\nun promedio que está mintiendo", options: { color: ACC } },
  { text: "\ny saber qué número pedir en su lugar.", options: { color: TINTA } },
], { x: 0.75, y: 1.85, w: 11.9, h: 3.6, fontFace: F, fontSize: 40, bold: true,
  isTextBox: true, margin: 0, lineSpacing: 54 });
s.addText("La diferencia de hoy vale una promoción entera: tres a uno.", { x: 0.75,
  y: 5.85, w: 11.5, h: 0.5, fontFace: F, fontSize: 16, color: MUTED, isTextBox: true,
  margin: 0 });

// ── 3 · La escalera ──────────────────────────────────────────────────────────
s = nueva("EL MAPA DEL SEMESTRE",
  "4-12 min. Dibuja la escalera EN LA PIZARRA mientras hablas (reflejo espejo); esta slide queda de respaldo. Un ejemplo por escalón con Superstore. Cerca: 'descriptivo no es lo básico que se salta; es donde el negocio decide a diario'. Señal verbal: 'Ese es el mapa. Hoy, escalón uno.'");
s.addText("Cuatro preguntas, cuatro escalones", { x: 0.75, y: 0.95, w: 11.8, h: 0.55,
  fontFace: F, fontSize: 28, bold: true, color: TINTA, isTextBox: true, margin: 0 });
figura(s, "s05_escalera.png", 1260, 744, 8.35, 1.7);
s.addText("Descriptivo no significa básico: es el escalón donde el negocio decide a diario.",
  { x: 0.75, y: 6.85, w: 11.8, h: 0.4, fontFace: F, fontSize: 14, color: MUTED,
    align: "center", isTextBox: true, margin: 0 });

// ── 4 · El caso ──────────────────────────────────────────────────────────────
s = nueva("EL CASO · LA LLAMADA DE LAS 8H02",
  "12-17 min. Teatraliza los mensajes de María (léelos como chat de WhatsApp; son los de la página 1 de D2L). Presenta la regla de casino: en este taller se apuesta antes de calcular; nadie pierde puntos por errar la apuesta, se pierde por no apostar.");
s.addText("María, gerente regional, necesita tres números", { x: 0.75, y: 0.95, w: 11.8,
  h: 0.55, fontFace: F, fontSize: 28, bold: true, color: TINTA, isTextBox: true, margin: 0 });
const preguntas = [
  ["¿Cuánto vale un pedido típico?", "Con él María fija el umbral de «envío gratis desde $X»."],
  ["¿Muebles o Suministros de Oficina?", "La categoría más rentable por venta duplica inventario."],
  ["¿Eliminamos Libreros?", "Auditoría dice que pierde plata. Hay que confirmarlo."],
];
preguntas.forEach((q, i) => {
  const y = 1.85 + i * 1.35;
  s.addShape(pres.shapes.OVAL, { x: 0.85, y: y, w: 0.62, h: 0.62, fill: { color: ACC } });
  s.addText(String(i + 1), { x: 0.85, y: y, w: 0.62, h: 0.62, fontFace: F, fontSize: 22,
    bold: true, color: "FFFFFF", align: "center", valign: "middle", isTextBox: true,
    margin: 0 });
  s.addText(q[0], { x: 1.75, y: y - 0.06, w: 10.8, h: 0.5, fontFace: F, fontSize: 22,
    bold: true, color: TINTA, isTextBox: true, margin: 0 });
  s.addText(q[1], { x: 1.75, y: y + 0.44, w: 10.8, h: 0.4, fontFace: F, fontSize: 15,
    color: MUTED, isTextBox: true, margin: 0 });
});
s.addShape(pres.shapes.RECTANGLE, { x: 0.85, y: 6.15, w: 11.6, h: 0.78,
  fill: { color: CARD } });
s.addText("Regla del taller: se apuesta antes de calcular.", { x: 0.85, y: 6.15, w: 11.6,
  h: 0.78, fontFace: F, fontSize: 17, bold: true, color: ACC, align: "center",
  valign: "middle", isTextBox: true, margin: 0 });

// ── 5 · Hapax: el muro de datos ──────────────────────────────────────────────
s = nueva("LOS DATOS",
  "17-20 min. La única slide deliberadamente abrumadora de la sesión (hapax legomenon): déjala 20 segundos en silencio. Luego: 'esto es lo que el sistema le entrega a un analista; nadie VE los datos: por eso existe la estadística descriptiva'. Presenta columnas clave: pedido_id, venta, descuento, utilidad.");
s.addText("9,994 líneas · 5,009 pedidos · cuatro años", { x: 0.75, y: 0.95, w: 11.8,
  h: 0.55, fontFace: F, fontSize: 28, bold: true, color: TINTA, isTextBox: true, margin: 0 });
figura(s, "s05_hapax_datos.png", 1644, 797, 11.4, 1.62);
s.addText("Nadie “ve” los datos. Para eso existe la estadística descriptiva.",
  { x: 0.75, y: 6.9, w: 11.8, h: 0.42, fontFace: F, fontSize: 17, bold: true, color: ACC,
    align: "center", isTextBox: true, margin: 0 });

// ── 6 · Apuesta 1 ────────────────────────────────────────────────────────────
s = nueva("APUESTA 1 · SE APUESTA ANTES DE CALCULAR",
  "20-24 min. Microcaso de predicción. Cada estudiante escribe SU número en los campos de la página 3 (media y mediana de la muestra a mano). Pide 3 o 4 en voz alta y anótalos en la pizarra. Tolera los 7 segundos de silencio. Pregunta extra: ¿qué % queda debajo del promedio? La mayoría dirá ~50%: ese es el error productivo.");
s.addText("¿Cuánto vale un\npedido típico?", { x: 0.75, y: 2.05, w: 11.8, h: 2.3,
  fontFace: F, fontSize: 48, bold: true, color: TINTA, align: "center", isTextBox: true,
  margin: 0, lineSpacing: 56 });
s.addText("$ ______", { x: 0.75, y: 4.45, w: 11.8, h: 0.95, fontFace: F, fontSize: 44,
  bold: true, color: ACC, align: "center", isTextBox: true, margin: 0 });
s.addText("Y de paso: ¿qué porcentaje de los pedidos queda debajo del promedio?",
  { x: 0.75, y: 5.6, w: 11.8, h: 0.5, fontFace: F, fontSize: 17, color: MUTED,
    align: "center", isTextBox: true, margin: 0 });

// ── 7 · Reveal 1 ─────────────────────────────────────────────────────────────
s = nueva("LO QUE DICEN LOS 5,009 PEDIDOS",
  "24-32 min. Reveal: todos desbloquean el candado de la página 3 en su dispositivo (media y mediana de la muestra a mano + apuesta del %); proyecta esta slide al abrirse. La sorpresa es el 72.5%. Cuenta el pedido monstruo: $23,661, casi todo un equipo Cisco de videoconferencia. Señal verbal: 'primera trampa cazada: cola larga; vamos a la segunda pregunta'.");
s.addText("El 72.5 % de los pedidos vale menos que el promedio", { x: 0.75, y: 0.95,
  w: 11.8, h: 0.55, fontFace: F, fontSize: 27, bold: true, color: TINTA, isTextBox: true,
  margin: 0 });
figura(s, "s05_hist_pedidos.png", 1368, 724, 10.35, 1.72);

// ── 8 · Apuesta 2 ────────────────────────────────────────────────────────────
s = nueva("APUESTA 2",
  "32-36 min. Votación a mano alzada: ¿quién dice Muebles? ¿quién Suministros? Cuenta los votos en la pizarra. Pide a dos personas defender su voto en una frase.");
s.addText("¿Muebles o\nSuministros de Oficina?", { x: 0.75, y: 2.2, w: 11.8, h: 2.3,
  fontFace: F, fontSize: 48, bold: true, color: TINTA, align: "center", isTextBox: true,
  margin: 0, lineSpacing: 56 });
s.addText("Utilidad por línea de venta. La ganadora duplica inventario:\napuesta y defiéndela.",
  { x: 0.75, y: 4.9, w: 11.8, h: 0.85, fontFace: F, fontSize: 17, color: MUTED,
    align: "center", isTextBox: true, margin: 0, lineSpacing: 24 });

// ── 9 · Reveal 2 ─────────────────────────────────────────────────────────────
s = nueva("EL DUELO",
  "36-44 min. Reveal: candado de la página 4 (votación previa a mano alzada). Muestra en la página las encuadernadoras GBC/Ibico de ~$5,000. Frase clave: 'la media es tan sensible a los extremos que un puñado de ventas decide un plan de inventario'. Señal verbal: 'segunda trampa; queda la peor'.");
s.addText("El veredicto depende del árbitro que elijas", { x: 0.75, y: 0.95, w: 11.8,
  h: 0.55, fontFace: F, fontSize: 27, bold: true, color: TINTA, isTextBox: true, margin: 0 });
figura(s, "s05_categorias.png", 1576, 606, 11.5, 1.75);
s.addText("A la media de Suministros de Oficina la sostienen unas pocas encuadernadoras de casi $5,000 por venta.",
  { x: 0.75, y: 6.5, w: 11.8, h: 0.4, fontFace: F, fontSize: 14, color: MUTED,
    align: "center", isTextBox: true, margin: 0 });

// ── 10 · Apuesta 3 ───────────────────────────────────────────────────────────
s = nueva("APUESTA 3 · EL MEMO DE AUDITORÍA",
  "44-48 min. Microcaso de error plantado: el memo es correcto en sus cifras y equivocado en su conclusión. Lee el memo con voz de auditor. Vota: ¿quién firma? El grupo, escarmentado por los actos 1 y 2, dirá 'la mediana debe ser positiva, no firmo'... y esta vez la mediana también engaña.");
s.addShape(pres.shapes.RECTANGLE, { x: 1.2, y: 1.95, w: 10.9, h: 2.1,
  fill: { color: CARD } });
s.addText("«Libreros acumuló una pérdida neta de $3,473 en cuatro años, con una utilidad media de −$15.23 por línea. Recomendación: descontinuarla.»",
  { x: 1.7, y: 1.95, w: 9.9, h: 2.1, fontFace: F, fontSize: 22, italic: true, color: TINTA,
    isTextBox: true, margin: 0, lineSpacing: 32, valign: "middle" });
s.addText("Las dos cifras son correctas. ¿Firmas?", { x: 0.75, y: 4.7, w: 11.8, h: 0.6,
  fontFace: F, fontSize: 22, bold: true, color: ACC, align: "center", isTextBox: true,
  margin: 0 });
s.addText("Pista: ¿la venta típica de Libreros gana o pierde plata?", { x: 0.75, y: 5.6,
  w: 11.8, h: 0.5, fontFace: F, fontSize: 16, color: MUTED, align: "center",
  isTextBox: true, margin: 0 });

// ── 11 · Reveal 3 ────────────────────────────────────────────────────────────
s = nueva("LA TRAMPA INVERSA",
  "48-58 min. Reveal: candado de la página 5. Mediana +$4.13 (la venta típica gana) y aun así el total es -$3,473: 34 ventas pierden más de $100 y se comen $9,506. La tabla por descuento de la página cierra el diagnóstico: sin descuento +$101, con 50-70% pierde $236-260. La decisión no es matar Libreros: es la política de descuentos. Nota que la pregunta descriptiva empujó sola al escalón diagnóstico.");
s.addText("Aquí la que engaña es la mediana (+$4.13)", { x: 0.75, y: 0.95, w: 11.8,
  h: 0.55, fontFace: F, fontSize: 27, bold: true, color: TINTA, isTextBox: true, margin: 0 });
figura(s, "s05_libreros.png", 1337, 686, 9.95, 1.68);
s.addText("El problema no es el mueble: son los descuentos del 50 y del 70 por ciento.",
  { x: 0.75, y: 6.9, w: 11.8, h: 0.4, fontFace: F, fontSize: 14, color: MUTED,
    align: "center", isTextBox: true, margin: 0 });

// ── 12 · La regla de la casa ─────────────────────────────────────────────────
s = nueva("LA REGLA DE LA CASA",
  "58-62 min. El eslogan de la sesión, segunda de las tres repeticiones de la idea central. Que lo lean en voz alta. 'Si la semana que viene alguien les muestra un promedio, la pregunta automática es: ¿me enseñas la distribución?'");
s.addText("Ningún promedio\nsin su distribución.", { x: 0.75, y: 2.05, w: 11.8, h: 2.4,
  fontFace: F, fontSize: 52, bold: true, color: ACC, align: "center", isTextBox: true,
  margin: 0, lineSpacing: 60 });
s.addText("Media: para distribuciones simétricas y sin extremos.\nMediana: cuando hay colas o valores extremos.\nHistograma: siempre, y primero.",
  { x: 0.75, y: 4.85, w: 11.8, h: 1.4, fontFace: F, fontSize: 17, color: MUTED,
    align: "center", isTextBox: true, margin: 0, lineSpacing: 28 });

// ── 13 · Ahora tú ────────────────────────────────────────────────────────────
s = nueva("AHORA TÚ",
  "62-83 min. Trabajo individual en las páginas de D2L: cierran los candados que falten (página 6: el segmento de oro) y escriben el memo a María. Circula entre los equipos. Cierra pidiendo dos memos leídos en voz alta. La página 7 trae el encargo: reporte de 5 diapositivas para el VP, entrega el miércoles. El cuaderno de Colab queda como práctica opcional.");
s.addText("El taller vive en D2L", { x: 0.75, y: 0.95, w: 11.8, h: 0.55,
  fontFace: F, fontSize: 28, bold: true, color: TINTA, isTextBox: true, margin: 0 });
s.addText("D2L → Contenido → Semana 3 →\nTaller · páginas 1 a 6", { x: 0.85, y: 2.05,
  w: 7.5, h: 1.05, fontFace: F, fontSize: 20, bold: true, color: ACC, isTextBox: true,
  margin: 0, lineSpacing: 28 });
s.addText([
  { text: "Seis páginas, seis candados: se apuesta antes de ver cada gráfica.",
    options: { bullet: { code: "2022", indent: 18 }, breakLine: true } },
  { text: "La última pregunta de María te espera en la página 6.",
    options: { bullet: { code: "2022", indent: 18 }, breakLine: true } },
  { text: "Entrega: el reporte para María, 5 diapositivas, miércoles.",
    options: { bullet: { code: "2022", indent: 18 } } },
], { x: 0.85, y: 3.45, w: 7.5, h: 2.4, fontFace: F, fontSize: 17, color: TINTA,
  paraSpaceAfter: 14, isTextBox: true, margin: 0 });
s.addShape(pres.shapes.OVAL, { x: 9.35, y: 2.5, w: 2.7, h: 2.7, fill: { color: CARD },
  line: { color: ACC, width: 1.5 } });
s.addText("≈ 50\nmin", { x: 9.35, y: 2.5, w: 2.7, h: 2.7, fontFace: F, fontSize: 30,
  bold: true, color: ACC, align: "center", valign: "middle", isTextBox: true, margin: 0,
  lineSpacing: 34 });

// ── 14 · Contribuciones (queda visible en preguntas) ─────────────────────────
s = nueva("LO QUE TE LLEVAS HOY",
  "83-90 min. Slide final: se queda proyectada durante las preguntas (nunca 'Gracias' ni '¿Preguntas?'). Espeja la promesa. Palabras finales, marcando el cierre: 'La próxima vez que un promedio te mire a los ojos, ya sabes qué pedirle. Nos vemos el miércoles.'");
const logros = [
  "La escalera: toda pregunta de negocio vive en un escalón, y se sube por necesidad, no por ambición.",
  "El detector de tres minutos: si la media y la mediana se alejan, hay cola larga o poblaciones mezcladas.",
  "La regla de la casa: ningún promedio sin su distribución — el histograma decide qué número usar.",
  "Tres decisiones salvadas hoy: un umbral de promoción muerto, el inventario equivocado y una subcategoría inocente.",
];
logros.forEach((t, i) => {
  const y = 1.7 + i * 1.2;
  s.addShape(pres.shapes.OVAL, { x: 0.85, y: y, w: 0.55, h: 0.55, fill: { color: ACC } });
  s.addText(String(i + 1), { x: 0.85, y: y, w: 0.55, h: 0.55, fontFace: F, fontSize: 18,
    bold: true, color: "FFFFFF", align: "center", valign: "middle", isTextBox: true,
    margin: 0 });
  s.addText(t, { x: 1.7, y: y - 0.12, w: 10.8, h: 1.0, fontFace: F, fontSize: 17.5,
    color: TINTA, isTextBox: true, margin: 0, lineSpacing: 24 });
});
s.addText("Miércoles · Perfilado descriptivo contra reloj sobre Comercial Andina — trae la laptop.",
  { x: 0.85, y: 6.75, w: 11.6, h: 0.4, fontFace: F, fontSize: 13, color: MUTED,
    isTextBox: true, margin: 0 });

pres.writeFile({ fileName: "S5_Trampa_Promedio.pptx" })
  .then((f) => console.log("OK →", f));
