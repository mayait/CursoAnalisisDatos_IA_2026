// Slides Sesiones 7 y 8 fusionadas · Anatomía y calidad de los datos · ADM 2003
// Taller práctico de 90 minutos: las slides acompañan el trabajo en Colab sobre andina_market.csv.
// Regla de la casa: fondo blanco siempre. Identidad USFQ: rojo A6192E sobre blanco.
// Patrón de cada paso: apuesta → corre el código → lo que deberías ver → fila de bitácora.
// Uso:  node crear_slides.js
const pptxgen = require("pptxgenjs");

const BG = "FFFFFF", TINTA = "1E1E1E", MUTED = "6B6B6B", ACC = "A6192E", CARD = "FBEDEF";
const CODEBG = "F4F4F4", CODEFG = "1E1E1E", COMENT = "8A8A8A", VERDE = "2E7D32";
const F = "Arial", MONO = "Courier New";
const IMG = "img_deck/";  // figuras del deck (fig1 y fig2 con título plano); las de img/ son las de D2L

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.33 x 7.5
pres.author = "ADM 2003 · USFQ Galápagos";
pres.title = "Sesiones 7 y 8 · Anatomía y calidad de los datos";

// ── helpers ──────────────────────────────────────────────────────────────────
function nueva(kicker, nota, minutos) {
  const s = pres.addSlide();
  s.background = { color: BG };
  if (kicker) {
    s.addText(kicker, { x: 0.75, y: 0.52, w: 9.8, h: 0.4, fontFace: F, fontSize: 13,
      bold: true, color: ACC, charSpacing: 2, isTextBox: true, margin: 0 });
  }
  if (minutos) {
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x: 10.9, y: 0.45, w: 1.7, h: 0.5,
      fill: { color: CARD }, line: { color: ACC, width: 1 }, rectRadius: 0.25 });
    s.addText("MIN " + minutos, { x: 10.9, y: 0.45, w: 1.7, h: 0.5, fontFace: F,
      fontSize: 12, bold: true, color: ACC, align: "center", valign: "middle",
      isTextBox: true, margin: 0 });
  }
  if (nota) s.addNotes(nota);
  return s;
}

function titulo(s, t, y = 0.95) {
  s.addText(t, { x: 0.75, y: y, w: 11.8, h: 0.6, fontFace: F, fontSize: 27, bold: true,
    color: TINTA, isTextBox: true, margin: 0 });
}

// Bloque de código: comentarios (#) en gris, resto en tinta. h se calcula por líneas.
function codigo(s, texto, x, y, w, opts = {}) {
  const fs = opts.fontSize || 13;
  const lineas = texto.split("\n");
  const h = opts.h || (lineas.length * fs * 1.55 / 72 + 0.3);
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { x, y, w, h, fill: { color: CODEBG },
    line: { color: "E0E0E0", width: 0.75 }, rectRadius: 0.08 });
  const runs = [];
  lineas.forEach((ln, i) => {
    const k = ln.indexOf("#");
    const ult = i === lineas.length - 1;
    if (k === -1) {
      runs.push({ text: ln, options: { color: CODEFG, breakLine: !ult } });
    } else {
      if (k > 0) runs.push({ text: ln.slice(0, k), options: { color: CODEFG } });
      runs.push({ text: ln.slice(k), options: { color: COMENT, italic: true, breakLine: !ult } });
    }
  });
  s.addText(runs, { x: x + 0.18, y: y + 0.12, w: w - 0.36, h: h - 0.24, fontFace: MONO,
    fontSize: fs, valign: "top", isTextBox: true, margin: 0, lineSpacing: fs * 1.45 });
  return y + h;
}

// Etiqueta pequeña en mayúsculas sobre una columna
function etiqueta(s, t, x, y, w, color = ACC) {
  s.addText(t, { x, y, w, h: 0.32, fontFace: F, fontSize: 11.5, bold: true, color,
    charSpacing: 1.5, isTextBox: true, margin: 0 });
}

// Tarjeta de apuesta (fondo rosado)
function apuesta(s, pregunta, x, y, w, h, sub) {
  s.addShape(pres.shapes.RECTANGLE, { x, y, w, h, fill: { color: CARD } });
  s.addText("TU APUESTA", { x: x + 0.25, y: y + 0.18, w: w - 0.5, h: 0.3, fontFace: F,
    fontSize: 11, bold: true, color: ACC, charSpacing: 1.5, isTextBox: true, margin: 0 });
  s.addText(pregunta, { x: x + 0.25, y: y + 0.5, w: w - 0.5, h: h - (sub ? 1.15 : 0.7),
    fontFace: F, fontSize: 18, bold: true, color: TINTA, valign: "top", isTextBox: true,
    margin: 0, lineSpacing: 24 });
  if (sub) s.addText(sub, { x: x + 0.25, y: y + h - 0.65, w: w - 0.5, h: 0.5, fontFace: F,
    fontSize: 12.5, color: MUTED, valign: "bottom", isTextBox: true, margin: 0 });
}

// Fila de bitácora (lo que se anota al cerrar cada paso)
function bitacora(s, texto, y = 6.7) {
  s.addShape(pres.shapes.RECTANGLE, { x: 0.75, y, w: 0.12, h: 0.5, fill: { color: ACC } });
  s.addText([{ text: "BITÁCORA  ", options: { bold: true, color: ACC } },
    { text: texto, options: { color: TINTA } }], { x: 1.05, y, w: 11.5, h: 0.5, fontFace: F,
    fontSize: 13.5, valign: "middle", isTextBox: true, margin: 0 });
}

function pie(s, t) {
  s.addText(t, { x: 0.75, y: 6.9, w: 11.8, h: 0.4, fontFace: F, fontSize: 13, color: MUTED,
    align: "center", isTextBox: true, margin: 0 });
}

// im: [wpx, hpx] reales del PNG → coloca con ancho dado
function figura(s, file, wpx, hpx, w, x, y) {
  const h = w * hpx / wpx;
  s.addImage({ path: IMG + file, x, y, w, h });
  return y + h;
}

function tabla(s, filas, x, y, w, colW, opts = {}) {
  const fs = opts.fontSize || 13;
  const rows = filas.map((r, i) => r.map((c, j) => ({
    text: c, options: {
      fontFace: (opts.mono && opts.mono.includes(j) && i > 0) ? MONO : F,
      fontSize: i === 0 ? fs - 1.5 : fs, bold: i === 0 || (opts.boldCol === j),
      color: i === 0 ? ACC : TINTA, fill: { color: i === 0 ? CARD : "FFFFFF" },
      align: (opts.center && opts.center.includes(j)) ? "center" : "left", valign: "middle",
      margin: [4, 8, 4, 8],
    } })));
  s.addTable(rows, { x, y, w, colW, border: { type: "solid", color: "E6E6E6", pt: 0.75 },
    rowH: opts.rowH || 0.42 });
}

const URL = "https://raw.githubusercontent.com/mayait/CursoAnalisisDatos_IA_2026/main/sesiones/S07%20-%20Granularidad%20y%20Calidad/andina_market.csv";

// ── 1 · Portada ──────────────────────────────────────────────────────────────
let s = nueva(null,
  "0-2 min. Laptops abiertas. Saludo corto y directo al plan (slide 2). El 120 y el 9.0 % se explican en la slide 4, no aquí. Mientras entran, ya está proyectado el link de Colab (slide 3).");
s.addText("ADM 2003 · ANÁLISIS DE DATOS CON IA Y PYTHON · SESIONES 7 Y 8", { x: 0.75, y: 1.3,
  w: 11.5, h: 0.4, fontFace: F, fontSize: 13, bold: true, color: ACC, charSpacing: 2,
  isTextBox: true, margin: 0 });
s.addText("Anatomía y calidad\nde los datos", { x: 0.7, y: 1.85, w: 8.0, h: 2.75, fontFace: F,
  fontSize: 56, bold: true, color: TINTA, isTextBox: true, margin: 0, lineSpacing: 62 });
s.addText("Taller en Colab sobre andina_market.csv:\ngranularidad, tipos, huecos, duplicados y el Deber 2.", { x: 0.75,
  y: 4.85, w: 7.6, h: 1.1, fontFace: F, fontSize: 20, color: MUTED, isTextBox: true,
  margin: 0, lineSpacing: 28 });
s.addText("120", { x: 9.2, y: 1.95, w: 3.6, h: 1.0, fontFace: F, fontSize: 64,
  bold: true, color: ACC, isTextBox: true, margin: 0 });
s.addText("líneas sin ID Cliente", { x: 9.25, y: 3.0, w: 3.6, h: 0.4, fontFace: F,
  fontSize: 14, color: MUTED, isTextBox: true, margin: 0 });
s.addText("9.0 %", { x: 9.2, y: 3.75, w: 3.6, h: 1.0, fontFace: F, fontSize: 64,
  bold: true, color: TINTA, isTextBox: true, margin: 0 });
s.addText("de las 1.335 líneas de la base", { x: 9.25, y: 4.8, w: 3.6, h: 0.4, fontFace: F,
  fontSize: 14, color: MUTED, isTextBox: true, margin: 0 });
s.addText("Semana 4 · Taller práctico en Colab · USFQ Galápagos", { x: 0.75, y: 6.9,
  w: 11.5, h: 0.35, fontFace: F, fontSize: 12, color: MUTED, isTextBox: true, margin: 0 });

// ── 2 · El plan de la sesión y las dos reglas ─────────────────────────────
s = nueva("EL PLAN",
  "2-5 min. Recorrer la tabla sin detenerse: ocho pasos, cada uno con su celda de Colab. Luego las dos reglas: (1) se apuesta antes de correr la celda; errar la apuesta no cuesta puntos, no apostar sí; (2) cada hallazgo se anota en la bitácora en el momento, porque la bitácora es el Deber 2.", "0–5");
titulo(s, "Un inventario de calidad de andina_market.csv, en ocho pasos");
tabla(s, [
  ["Paso", "Qué se hace", "Herramienta", "Min"],
  ["1", "Qué representa una fila", "head, nunique, filtro por pedido", "15–24"],
  ["2", "Tipos de dato", "dtypes, info", "24–32"],
  ["3", "Huecos declarados y huecos como texto", "isna, value_counts, isin, groupby", "32–45"],
  ["4", "Cero, vacío y centinela", "value_counts(dropna=False), describe", "45–52"],
  ["5", "Duplicados", "duplicated, drop", "52–58"],
  ["6", "Valores imposibles y categorías", "comparaciones, to_datetime", "58–65"],
  ["7", "Dos limpiezas con verificación", "astype, to_datetime, máscaras", "73–80"],
  ["8", "Resumen: filas y venta antes y después", "drop_duplicates, sum", "80–84"],
], 0.75, 1.7, 7.4, [0.6, 3.4, 2.6, 0.8], { fontSize: 11.5, mono: [2], center: [0, 3], rowH: 0.4 });
const reglas = [
  ["Se apuesta antes de correr la celda.", "Escribes tu número o tu opción, después ejecutas. Errar la apuesta no cuesta puntos; no apostar, sí."],
  ["Cada hallazgo es una fila de la bitácora.", "Problema, filas afectadas, evidencia, decisión, justificación. La bitácora de hoy es el Deber 2."],
];
reglas.forEach((r, i) => {
  const y = 1.7 + i * 2.0;
  s.addShape(pres.shapes.RECTANGLE, { x: 8.5, y, w: 4.1, h: 1.8, fill: { color: CARD } });
  s.addText(r[0], { x: 8.75, y: y + 0.15, w: 3.6, h: 0.55, fontFace: F, fontSize: 15, bold: true,
    color: ACC, isTextBox: true, margin: 0, lineSpacing: 19 });
  s.addText(r[1], { x: 8.75, y: y + 0.75, w: 3.6, h: 1.0, fontFace: F, fontSize: 12.5, color: TINTA,
    isTextBox: true, margin: 0, lineSpacing: 17 });
});
s.addText("Los pasos 1 a 6 cuentan problemas. Los pasos 7 y 8 deciden qué hacer con ellos.",
  { x: 0.75, y: 5.6, w: 7.4, h: 0.5, fontFace: F, fontSize: 13, color: MUTED, isTextBox: true, margin: 0 });

// ── 3 · Arranque: Colab y la base ────────────────────────────────────────────
s = nueva("ARRANQUE · ABRE COLAB Y CARGA LA BASE",
  "5-10 min. Todos corren esta celda antes de seguir; caminar por la sala y confirmar que a todos les da (1335, 19). Plan B sin GitHub: descargar andina-market.csv de D2L y subirlo con files.upload(). Mientras cargan, que abran una celda de texto con la cabecera de la bitácora (derecha). No explicar nada todavía de las columnas.", "5–10");
titulo(s, "Cargar la base");
etiqueta(s, "CORRE ESTO", 0.75, 1.7, 6);
codigo(s,
`import pandas as pd
url = "${URL}"
df = pd.read_csv(url)
df.shape            # (1335, 19)

# Plan B: subir el archivo desde D2L
# from google.colab import files
# files.upload()
# df = pd.read_csv("andina-market.csv")`, 0.75, 2.05, 7.4, { fontSize: 10.5, h: 2.55 });
etiqueta(s, "TU BITÁCORA ARRANCA AHORA · CELDA DE TEXTO", 8.5, 1.7, 4.3);
tabla(s, [
  ["Columna", "Qué va ahí"],
  ["Problema", "Nombre claro"],
  ["Filas", "El número exacto, contado con código"],
  ["Evidencia", "La línea de pandas que lo demuestra"],
  ["Decisión", "Corregir · excluir · imputar · documentar"],
  ["Justificación", "Una frase de negocio, no de pandas"],
], 8.5, 2.05, 4.1, [1.35, 2.75], { fontSize: 11.5, rowH: 0.4 });
s.addText("Andina Market: filial ecuatoriana ficticia de Superstore. 1.335 líneas de pedido, 19 columnas, septiembre 2025 a agosto 2026. Una fila es un producto dentro de un pedido.",
  { x: 0.75, y: 5.35, w: 7.4, h: 0.8, fontFace: F, fontSize: 13, color: MUTED, isTextBox: true,
    margin: 0, lineSpacing: 18 });
bitacora(s, "Vacía por ahora. Al final debería tener al menos nueve filas.");

// ── 4 · El caso: el correo de auditoría ──────────────────────────────────────
s = nueva("EL CASO · EL CORREO DE AUDITORÍA",
  "10-15 min. Leer el mensaje de Verónica y la cita de auditoría. Apuesta a mano alzada: A, B, C o D. Casi todos eligen B (venta de mostrador). No revelar todavía: la respuesta es D y se cierra en la slide 11 con la gráfica por región.", "10–15");
titulo(s, "El correo de auditoría");
s.addShape(pres.shapes.RECTANGLE, { x: 0.75, y: 1.7, w: 7.0, h: 1.15, fill: { color: CARD } });
s.addText([{ text: "Verónica · gerente de Andina Market\n", options: { bold: true, color: ACC, fontSize: 12 } },
  { text: "Auditoría revisó la base de ventas del último año y me mandó esto. Necesito una explicación antes del viernes.", options: { color: TINTA } }],
  { x: 1.0, y: 1.78, w: 6.5, h: 1.0, fontFace: F, fontSize: 14, valign: "top", isTextBox: true,
    margin: 0, lineSpacing: 18 });
s.addShape(pres.shapes.RECTANGLE, { x: 0.75, y: 3.0, w: 7.0, h: 1.3, fill: { color: "FFFFFF" },
  line: { color: ACC, width: 1.25 } });
s.addText([{ text: "Auditoría interna\n", options: { bold: true, color: ACC, fontSize: 12 } },
  { text: "De las 1.335 líneas de venta del último año, 120 (9.0 %) no tienen identificador de cliente. Solicitamos confirmar si se trata de un error del sistema o de una práctica de registro.", options: { color: TINTA } }],
  { x: 1.0, y: 3.08, w: 6.5, h: 1.15, fontFace: F, fontSize: 14, valign: "top", isTextBox: true,
    margin: 0, lineSpacing: 18 });
s.addText("Según la respuesta, esas 120 líneas se borran, se rellenan o se reportan como un hallazgo del proceso de ventas.",
  { x: 0.75, y: 4.5, w: 7.0, h: 0.8, fontFace: F, fontSize: 14, color: MUTED, isTextBox: true,
    margin: 0, lineSpacing: 19 });
apuesta(s, "Sin mirar nada más: ¿qué significa que ID Cliente esté vacío en una línea de venta?", 8.25, 1.7, 4.35, 4.6, null);
const opc = ["A · El cliente no existe: son ventas falsas.", "B · Venta de mostrador: consumidor final sin registro.",
  "C · Alguien olvidó digitarlo.", "D · Todavía no se puede saber: hay que preguntar cómo se captura el campo."];
s.addText(opc.map((t, i) => ({ text: t, options: { breakLine: i < opc.length - 1 } })),
  { x: 8.5, y: 3.3, w: 3.9, h: 2.8, fontFace: F, fontSize: 13.5, color: TINTA, valign: "top",
    isTextBox: true, margin: 0, paraSpaceAfter: 10 });
pie(s, "Se vota a mano alzada. La respuesta sale de los datos en el paso 3.");

// ── 5 · Paso 1 · ¿Qué es una fila? ───────────────────────────────────────────
s = nueva("PASO 1 · ¿QUÉ ES UNA FILA?",
  "15-20 min. Corren head() y el filtro del pedido. Apuesta escrita en el cuaderno: ¿de cuántos dólares fue el pedido? La mitad suma Total Pedido (749.60) y la otra mitad Ventas (187.40). Pedir dos o tres números en voz alta antes de pasar a la siguiente slide. No corregir todavía.", "15–24");
titulo(s, "¿Qué representa una fila?");
etiqueta(s, "CORRE ESTO", 0.75, 1.7, 6);
codigo(s,
`df.head(3)                    # ¿qué representa una fila?
df["ID Pedido"].nunique()     # 430 pedidos en 1335 líneas

cols = ["Producto", "Cantidad", "Ventas", "Total Pedido"]
df[df["ID Pedido"] == "AM-2026-0042"][cols]`, 0.75, 2.05, 7.4, { fontSize: 12 });
etiqueta(s, "LO QUE DEBERÍAS VER · PEDIDO AM-2026-0042", 0.75, 3.85, 7);
tabla(s, [
  ["Producto", "Cantidad", "Ventas", "Total Pedido"],
  ["Resma papel A4 75g", "2", "74.90", "187.40"],
  ["Mouse Logitech M170", "2", "41.20", "187.40"],
  ["Cinta adhesiva Scotch x6", "1", "19.00", "187.40"],
  ["Cuaderno universitario Norma", "3", "52.30", "187.40"],
], 0.75, 4.2, 7.4, [3.2, 1.2, 1.4, 1.6], { fontSize: 12.5, center: [1, 2, 3], rowH: 0.4 });
apuesta(s, "¿De cuántos dólares fue el pedido AM-2026-0042?", 8.5, 1.7, 4.1, 2.3,
  "Escribe solo el número en tu cuaderno.");
s.addText("Hay dos columnas con dólares y no dicen lo mismo.",
  { x: 8.5, y: 4.2, w: 4.1, h: 0.9, fontFace: F, fontSize: 13.5, color: MUTED, isTextBox: true,
    margin: 0, lineSpacing: 19 });

// ── 6 · Reveal granularidad ──────────────────────────────────────────────────
s = nueva("PASO 1 · LA COLUMNA QUE VIVE EN OTRA GRANULARIDAD",
  "20-24 min. Reveal: 187.40 contra 749.60. Luego la escala: la misma confusión sobre toda la base infla la venta 3.8 veces. Nadie inventó un número, solo sumó una columna que vive en otro nivel. Cerrar con las dos preguntas ante una tabla nueva y anotar la primera fila de la bitácora.");
s.addText("$187.40", { x: 0.75, y: 1.0, w: 3.6, h: 0.9, fontFace: F, fontSize: 48, bold: true,
  color: ACC, isTextBox: true, margin: 0 });
s.addText("la suma de Ventas: lo que valió el pedido", { x: 0.75, y: 1.9, w: 3.6, h: 0.5,
  fontFace: F, fontSize: 13, color: MUTED, isTextBox: true, margin: 0 });
s.addText("$749.60", { x: 4.6, y: 1.0, w: 3.6, h: 0.9, fontFace: F, fontSize: 48, bold: true,
  color: TINTA, isTextBox: true, margin: 0 });
s.addText("la suma de Total Pedido: el total repetido cuatro veces", { x: 4.6, y: 1.9, w: 3.8,
  h: 0.5, fontFace: F, fontSize: 13, color: MUTED, isTextBox: true, margin: 0 });
codigo(s,
`df["Total Pedido"].sum()
# 704,623  ← la venta inflada 3.8x
df["Ventas"].sum()
# falla: hay texto (paso 2)`, 8.5, 1.05, 4.1, { fontSize: 10.5 });
figura(s, "fig2_doble_conteo.png", 924, 550, 6.0, 0.75, 2.55);
etiqueta(s, "TRES NIVELES SOBRE LA MISMA TABLA", 7.5, 2.6, 5);
tabla(s, [
  ["Nivel", "Pregunta típica", "Cómo se llega"],
  ["Línea", "¿Qué producto se vendió más?", "la tabla tal cual"],
  ["Pedido", "¿Cuánto vale el pedido típico?", 'groupby("ID Pedido")'],
  ["Cliente", "¿Cuánto gasta un cliente al año?", 'groupby("ID Cliente")'],
], 7.5, 2.95, 5.1, [1.0, 2.3, 1.8], { fontSize: 11.5, mono: [2], rowH: 0.4 });
s.addText("Dos preguntas de rigor ante una tabla nueva: ¿qué es una fila? y ¿qué columnas pertenecen a otra granularidad? Las repetidas no se suman: se usan con drop_duplicates(\"ID Pedido\") o se recalculan.",
  { x: 7.5, y: 4.75, w: 5.1, h: 1.3, fontFace: F, fontSize: 12.5, color: TINTA, isTextBox: true,
    margin: 0, lineSpacing: 17 });
bitacora(s, "Total Pedido repetido por línea · 1.335 filas · sumarla da $704.623 vs $185.389 reales · decisión: nunca sumar; recalcular.");

// ── 7 · Paso 2 · Tipos ───────────────────────────────────────────────────────
s = nueva("PASO 2 · TIPOS DE DATO",
  "24-28 min. Corren dtypes e info(). Apuesta: ¿cuántas columnas mienten sobre su tipo? Que anoten un número y cuáles. Dar dos minutos de silencio real para que las busquen; la mayoría encuentra Ventas (object) y se le escapa que Fecha Pedido y Fecha Envío también son object porque 'se ven bien'.", "24–32");
titulo(s, "dtypes: qué tipo tiene cada columna");
etiqueta(s, "CORRE ESTO", 0.75, 1.7, 6);
codigo(s,
`df.dtypes                 # ¿qué columnas mienten sobre su tipo?
df.info()                 # tipos y no-nulos de un vistazo

df["Ventas"].sum()        # ¿qué pasa aquí?`, 0.75, 2.05, 7.4, { fontSize: 12.5 });
etiqueta(s, "LO QUE ESPERAS VS LO QUE HAY", 0.75, 3.75, 6);
tabla(s, [
  ["Columna", "Lo que esperas", "Lo que dice dtypes"],
  ["Fecha Pedido", "datetime64", "?"],
  ["Fecha Envío", "datetime64", "?"],
  ["Ventas", "float64", "?"],
  ["Cantidad", "entero positivo", "?"],
  ["Descuento", "float64", "?"],
], 0.75, 4.1, 7.4, [2.4, 2.5, 2.5], { fontSize: 12.5, mono: [1, 2], rowH: 0.38 });
apuesta(s, "¿Cuántas columnas mienten sobre su tipo? ¿Cuáles?", 8.5, 1.7, 4.1, 2.3,
  "Un número y una lista. Dos minutos.");
s.addText("Regla: una sola celda con un símbolo de dólar vuelve object toda la columna. Y una columna object no se suma, no se promedia y no se ordena bien.",
  { x: 8.5, y: 4.2, w: 4.1, h: 1.4, fontFace: F, fontSize: 13, color: MUTED, isTextBox: true,
    margin: 0, lineSpacing: 18 });

// ── 8 · Reveal tipos ─────────────────────────────────────────────────────────
s = nueva("PASO 2 · LO QUE DICE dtypes",
  "28-32 min. Reveal con los conteos: 43 ventas con formato de factura, 35 fechas en dd/mm/yyyy, y Cantidad que es int pero trae 9 negativas (eso se resuelve en el paso 6). Insistir en el orden: los tipos van primero, porque un isna() sobre una columna rota cuenta mal. Tres filas a la bitácora (Ventas, fechas, cantidad negativa queda pendiente).");
titulo(s, "Tres columnas con tipo incorrecto, dos con valores sospechosos");
tabla(s, [
  ["Columna", "dtypes", "Síntoma", "Filas"],
  ["Fecha Pedido", "object", "35 filas vienen como dd/mm/yyyy, el resto yyyy-mm-dd", "35"],
  ["Fecha Envío", "object", "mismo problema: texto, dos formatos mezclados", "35"],
  ["Ventas", "object", "43 filas traen formato de factura: $201,45", "43"],
  ["Cantidad", "int64", "el tipo está bien, pero hay 9 valores negativos", "9"],
  ["Descuento", "float64", "el tipo está bien, pero 212 vacíos (paso 4)", "212"],
], 0.75, 1.7, 7.6, [1.6, 1.0, 4.2, 0.8], { fontSize: 12, mono: [1], center: [3], rowH: 0.48 });
etiqueta(s, "LA EVIDENCIA, CONTADA CON CÓDIGO", 8.7, 1.7, 4);
codigo(s,
`v = df["Ventas"]
v.str.startswith("$").sum()
# 43
v[v.str.startswith("$")].head(3)
# $201,45  $42,88  $37,68
f = df["Fecha Pedido"]
f.str.contains("/").sum()
# 35
(df["Cantidad"] < 0).sum()
# 9`, 8.7, 2.05, 3.9, { fontSize: 10.5 });
s.addShape(pres.shapes.RECTANGLE, { x: 0.75, y: 4.85, w: 11.85, h: 0.85, fill: { color: CARD } });
s.addText("Orden: primero corregir los tipos, después contar. isna() sobre una columna numérica guardada como texto cuenta mal.",
  { x: 1.0, y: 4.85, w: 11.4, h: 0.85, fontFace: F, fontSize: 15, bold: true, color: ACC,
    valign: "middle", isTextBox: true, margin: 0 });
s.addText("Los tipos se corrigen en el paso 7. Por ahora se anotan: contar viene antes que limpiar.",
  { x: 0.75, y: 5.85, w: 11.85, h: 0.5, fontFace: F, fontSize: 13, color: MUTED, isTextBox: true, margin: 0 });
bitacora(s, "Ventas como texto · 43 · Fechas en dd/mm/yyyy · 35 · decisión: corregir (astype, to_datetime) y verificar el dtype después.");

// ── 9 · Paso 3 · Huecos declarados ───────────────────────────────────────────
s = nueva("PASO 3 · HUECOS DECLARADOS",
  "32-37 min. Corren isna().sum(). ID Cliente da 99 (pandas ya convirtió las cadenas vacías en NaN al leer el CSV). Auditoría dijo 120. Apuesta: ¿cuántas líneas sin cliente encuentras tú? Que escriban el número y la línea de código con la que lo defienden. Pista si se traban: value_counts(dropna=False).", "32–45");
titulo(s, "isna(): los huecos declarados");
etiqueta(s, "CORRE ESTO", 0.75, 1.7, 6);
codigo(s,
`df.isna().sum()                     # huecos declarados por columna

df["ID Cliente"].isna().sum()       # 99
# Auditoría dijo 120. ¿Dónde están los otros 21?

df["ID Cliente"].value_counts(dropna=False).head()`, 0.75, 2.05, 7.4, { fontSize: 12.5 });
etiqueta(s, "LO QUE DEBERÍAS VER · isna().sum()", 0.75, 4.15, 6);
tabla(s, [
  ["Columna", "Nulos", "Columna", "Nulos"],
  ["ID Cliente", "99", "Provincia", "32"],
  ["Nombre Cliente", "120", "Descuento", "212"],
  ["Todo lo demás", "0", "", ""],
], 0.75, 4.5, 7.4, [2.3, 1.4, 2.3, 1.4], { fontSize: 12.5, center: [1, 3], rowH: 0.4 });
apuesta(s, "isna() dice 99. Auditoría dice 120. ¿Cuántas líneas SIN cliente encuentras tú?", 8.5, 1.7, 4.1, 2.6,
  "Tu número y la línea de código que lo defiende.");
s.addText("Fíjate en Nombre Cliente: ahí sí faltan 120. Dos columnas que deberían contar lo mismo y no lo hacen son una pista.",
  { x: 8.5, y: 4.5, w: 4.1, h: 1.3, fontFace: F, fontSize: 13, color: MUTED, isTextBox: true,
    margin: 0, lineSpacing: 18 });

// ── 10 · Reveal sin cliente ──────────────────────────────────────────────────
s = nueva("PASO 3 · HUECOS GUARDADOS COMO TEXTO",
  "37-41 min. Reveal: los 21 que faltan dicen 'SIN-ID', un texto que para pandas es un cliente perfectamente válido. La máscara da 120, igual que auditoría. Regla en voz alta: isna() encuentra lo declarado; lo inventado se caza con value_counts e isin. Que corran la máscara y la guarden: se usa en la slide siguiente.");
titulo(s, "Los 21 que faltaban se llaman \"SIN-ID\"");
etiqueta(s, "LO QUE DEBERÍAS VER", 0.75, 1.7, 6);
codigo(s,
`df["ID Cliente"].value_counts(dropna=False).head(4)
# NaN       99
# CL-124    35
# CL-154    30
# CL-170    29
df["ID Cliente"].isin(["SIN-ID"]).sum()
# 21`, 0.75, 2.05, 5.9, { fontSize: 12 });
etiqueta(s, "LA MÁSCARA QUE CUADRA CON AUDITORÍA", 7.0, 1.7, 6);
codigo(s,
`c = df["ID Cliente"]
sin_cliente = c.isna() | c.isin(["", "SIN-ID"])
sin_cliente.sum()
# 120
df["Nombre Cliente"].isna().sum()
# 120   ← la segunda columna lo confirma`, 7.0, 2.05, 5.6, { fontSize: 12 });
s.addShape(pres.shapes.RECTANGLE, { x: 0.75, y: 4.6, w: 11.85, h: 1.0, fill: { color: CARD } });
s.addText("isna() encuentra los huecos declarados como NaN. Los guardados como texto o como número (\"\", \"SIN-ID\", \"N/A\", -9999) se encuentran con value_counts(dropna=False) e isin().",
  { x: 1.0, y: 4.6, w: 11.4, h: 1.0, fontFace: F, fontSize: 15, bold: true, color: ACC,
    valign: "middle", isTextBox: true, margin: 0, lineSpacing: 21 });
s.addText("Sobre toda columna sospechosa, primero value_counts(dropna=False).",
  { x: 0.75, y: 5.8, w: 11.85, h: 0.5, fontFace: F, fontSize: 13, color: MUTED, isTextBox: true, margin: 0 });
bitacora(s, "Sin ID Cliente · 120 (99 NaN + 21 \"SIN-ID\") · evidencia: la máscara · decisión: pendiente, depende del paso siguiente.");

// ── 11 · El hueco como pista ─────────────────────────────────────────────────
s = nueva("PASO 3 · DÓNDE SE CONCENTRA EL HUECO",
  "41-45 min. Corren el groupby con la máscara. La gráfica cierra la apuesta de la slide 4: Costa 11.4 %, Galápagos 3.6 %, Amazonía 0. Un faltante concentrado en una región apunta a un proceso de captura distinto (cajas de mostrador que no piden cédula). La respuesta correcta era D. La tabla de los tres significados sirve para escribir la justificación en la bitácora.");
titulo(s, "El hueco se concentra en una región");
codigo(s,
`(df.assign(sin=sin_cliente)
   .groupby("Región")["sin"].mean()
   .mul(100).round(1))
# Amazonía     0.0
# Costa       11.4
# Galápagos    3.6
# Sierra       7.1`, 0.75, 1.7, 5.4, { fontSize: 12 });
figura(s, "fig1_sin_cliente_region.png", 1070, 560, 4.8, 0.75, 4.0);
etiqueta(s, "TEORÍA · LOS TRES SIGNIFICADOS DE UN HUECO", 6.6, 1.7, 6);
tabla(s, [
  ["Caso", "Qué es", "En Andina Market"],
  ["Ausente", "El valor existe en el mundo, nadie lo capturó.", "Provincia vacía de un pedido despachado."],
  ["Cero", "El valor es exactamente cero. Es un dato, no un hueco.", "Descuento = 0: hubo venta sin rebaja."],
  ["Desconocido", "Ni siquiera sabemos si existe un valor.", "ID Cliente vacío: ¿anónimo o perdido?"],
], 6.6, 2.05, 6.0, [1.3, 2.5, 2.2], { fontSize: 11.5, rowH: 0.62 });
s.addShape(pres.shapes.RECTANGLE, { x: 6.6, y: 4.75, w: 6.0, h: 1.0, fill: { color: CARD } });
s.addText("Un faltante concentrado en una región, canal o turno apunta a un proceso de captura distinto. Antes de imputar o borrar, preguntar cómo se captura el campo.",
  { x: 6.85, y: 4.75, w: 5.5, h: 1.0, fontFace: F, fontSize: 13.5, bold: true, color: ACC,
    valign: "middle", isTextBox: true, margin: 0, lineSpacing: 18 });
s.addText("Respuesta a la apuesta del correo: D. Con la tabla sola no se distingue una venta de mostrador de un olvido; hay que preguntar al proceso.",
  { x: 6.6, y: 5.9, w: 6.0, h: 0.6, fontFace: F, fontSize: 12.5, color: MUTED, isTextBox: true,
    margin: 0, lineSpacing: 17 });
bitacora(s, "Sin ID Cliente · 120 · concentrado en Costa (11.4 %) · decisión: documentar y preguntar a ventas cómo se captura en mostrador.");

// ── 12 · Paso 4 · Cero, vacío y centinela ────────────────────────────────────
s = nueva("PASO 4 · CERO, VACÍO Y CENTINELA",
  "45-52 min. Descuento: 658 ceros y 212 vacíos. Apuesta a mano alzada con las tres opciones; la correcta es el rango 658 a 870, porque la respuesta depende de la regla de captura y eso se pregunta. Luego el centinela: describe() da una utilidad media de -99 dólares, imposible. value_counts lo delata: 15 filas en -9999. Sin el centinela, la media es 13.41. isna() jamás lo ve. Dos filas a la bitácora.", "45–52");
titulo(s, "Descuento y Utilidad: tres valores que se confunden");
etiqueta(s, "A · DESCUENTO: CERO NO ES VACÍO", 0.75, 1.7, 6);
codigo(s,
`df["Descuento"].value_counts(dropna=False)
# 0.0    658   ← hubo venta, no hubo rebaja
# NaN    212   ← ¿sin rebaja o sin registro?
# 0.1    204 ...`, 0.75, 2.05, 5.9, { fontSize: 11.5 });
apuesta(s, "¿Cuántas líneas no tuvieron descuento?", 0.75, 3.55, 5.9, 2.1,
  "A · 658     B · 870     C · entre 658 y 870, y se pregunta");
etiqueta(s, "B · UTILIDAD: EL CENTINELA", 7.0, 1.7, 6);
codigo(s,
`df["Utilidad"].describe().round(1)
# mean    -99.1   ← ¿pierde plata cada línea?
# min   -9999.0   ← ahí está

df["Utilidad"].value_counts().head(2)
# -9999.00    15
df.loc[df["Utilidad"] != -9999, "Utilidad"].mean()
# 13.41   ← la utilidad real por línea`, 7.0, 2.05, 5.6, { fontSize: 11.5 });
s.addText("Un sistema viejo usaba -9999 para decir \"desconocido\". Para pandas es un número válido: isna() jamás lo encuentra y arrastra la media de toda una región.",
  { x: 7.0, y: 4.85, w: 5.6, h: 0.9, fontFace: F, fontSize: 12.5, color: MUTED, isTextBox: true,
    margin: 0, lineSpacing: 17 });
bitacora(s, "Descuento no registrado · 212 · decisión: preguntar la regla de captura. Utilidad = -9999 · 15 · decisión: convertir a NaN.");

// ── 13 · Paso 5 · Duplicados ─────────────────────────────────────────────────
s = nueva("PASO 5 · DUPLICADOS",
  "52-58 min. Apuesta numérica antes de correr: ¿cuántas filas repetidas exactas? Corren duplicated().sum() y da 0. Segunda línea, sin ID Fila: 24. El consecutivo se lo puso el sistema a cada registro después de duplicarse, así dos filas idénticas parecen distintas. Regla: antes de buscar duplicados, quita los identificadores automáticos.", "52–58");
titulo(s, "duplicated() da cero por la columna ID Fila");
apuesta(s, "¿Cuántas filas repetidas exactas crees que hay en la base?", 0.75, 1.7, 5.4, 1.9,
  "Escribe tu número antes de correr la celda.");
etiqueta(s, "CORRE ESTO, EN ESTE ORDEN", 0.75, 3.85, 6);
codigo(s,
`df.duplicated().sum()
# 0    ← miente

sin_id = df.drop(columns=["ID Fila"])
sin_id.duplicated().sum()
# 24   ← la verdad

sin_id[sin_id.duplicated(keep=False)].head(6)`, 0.75, 4.2, 5.4, { fontSize: 11.5 });
s.addText("24", { x: 7.0, y: 1.55, w: 5.6, h: 1.4, fontFace: F, fontSize: 88, bold: true,
  color: ACC, isTextBox: true, margin: 0 });
s.addText("filas idénticas que ID Fila disfraza de distintas", { x: 7.0, y: 3.0, w: 5.6, h: 0.5,
  fontFace: F, fontSize: 15, color: MUTED, isTextBox: true, margin: 0 });
s.addShape(pres.shapes.RECTANGLE, { x: 7.0, y: 3.75, w: 5.6, h: 1.55, fill: { color: CARD } });
s.addText("ID Fila es un consecutivo que el sistema le puso a cada registro después de duplicarse. Para buscar duplicados reales, primero quita los identificadores automáticos: ID Fila, timestamps de carga, hashes.",
  { x: 7.25, y: 3.75, w: 5.1, h: 1.55, fontFace: F, fontSize: 13.5, bold: true, color: ACC,
    valign: "middle", isTextBox: true, margin: 0, lineSpacing: 19 });
s.addText("¿Cuántos dólares inflan? Se responde en el paso 8, cuando Ventas ya sea número.",
  { x: 7.0, y: 5.45, w: 5.6, h: 0.6, fontFace: F, fontSize: 12.5, color: MUTED, isTextBox: true,
    margin: 0, lineSpacing: 17 });
bitacora(s, "Duplicados exactos · 24 · evidencia: duplicated() sin ID Fila · decisión: excluir (drop_duplicates) y registrar cuántas filas quedan.");

// ── 14 · Paso 6 · Imposibles e inconsistentes ────────────────────────────────
s = nueva("PASO 6 · VALORES IMPOSIBLES Y CATEGORÍAS INCONSISTENTES",
  "58-65 min. Cuatro frentes en siete minutos; que cada uno corra los cuatro y anote las filas. Ciudad: cuatro grafías de Quito y dos de Santo Domingo; value_counts() las delata al final de la lista, no al principio. Provincia vacía: 32, y se puede deducir de la ciudad. Cantidad negativa: 9, no se decide todavía (slide 16). Envío antes del pedido: solo aparece después de convertir las fechas; si lo comparan como texto sale cualquier cosa.", "58–65");
titulo(s, "Ciudad, Provincia, Cantidad y fechas");
etiqueta(s, "A · CATEGORÍAS: MIRA EL FINAL DE LA LISTA", 0.75, 1.7, 6);
codigo(s,
`df["Ciudad"].value_counts().tail(4)
# QUITO           19
# Sto. Domingo    14
# quito           12
#  Quito          10   ← con espacio adelante`, 0.75, 2.05, 5.9, { fontSize: 11.5 });
etiqueta(s, "B · PROVINCIA VACÍA (SE PUEDE DEDUCIR)", 0.75, 3.95, 6);
codigo(s,
`df["Provincia"].isna().sum()
# 32
sin_prov = df["Provincia"].isna()
df.loc[sin_prov, "Ciudad"].value_counts().head(3)
# Guayaquil 9 · Quito 9 · Manta 5`, 0.75, 4.3, 5.9, { fontSize: 11 });
etiqueta(s, "C · CANTIDAD NEGATIVA (¿DEVOLUCIONES?)", 7.0, 1.7, 6);
codigo(s,
`neg = df["Cantidad"] < 0
neg.sum()
# 9
df.loc[neg, ["ID Pedido", "Producto", "Cantidad"]]`, 7.0, 2.05, 5.6, { fontSize: 11 });
etiqueta(s, "D · ENVÍOS QUE VIAJAN AL PASADO (FECHAS PRIMERO)", 7.0, 3.75, 6);
codigo(s,
`pedido = pd.to_datetime(df["Fecha Pedido"],
                        format="mixed", dayfirst=True)
envio  = pd.to_datetime(df["Fecha Envío"],
                        format="mixed", dayfirst=True)
(envio < pedido).sum()
# 6   ← comparadas como texto, sale mal`, 7.0, 4.1, 5.6, { fontSize: 11 });
bitacora(s, "Ciudad inconsistente · ~55 · Provincia vacía · 32 · Cantidad negativa · 9 · Envío anterior al pedido · 6.");

// ── 15 · Checkpoint: el inventario completo ──────────────────────────────────
s = nueva("CHECKPOINT · EL INVENTARIO COMPLETO",
  "65-68 min. Proyectar la gráfica y pedir que cuenten sus filas de bitácora. Quien tenga menos de siete revisa la lista contra la suya. Lo que sigue es decidir qué hacer con cada problema; cada decisión cambia una cifra.", "65–68");
titulo(s, "El inventario completo: ¿cuántas filas tiene tu bitácora?");
figura(s, "fig4_inventario.png", 1268, 706, 7.6, 0.75, 1.65);
etiqueta(s, "Y DOS QUE LA GRÁFICA NO MUESTRA", 8.7, 1.75, 4);
s.addText([
  { text: "Total Pedido repetido por línea: afecta a todas las filas, no se suma.", options: { bullet: { code: "2022", indent: 14 }, breakLine: true } },
  { text: "Ciudad con cuatro grafías de Quito y dos de Santo Domingo: unas 55 filas.", options: { bullet: { code: "2022", indent: 14 } } },
], { x: 8.7, y: 2.1, w: 3.9, h: 1.8, fontFace: F, fontSize: 13, color: TINTA, paraSpaceAfter: 10,
  isTextBox: true, margin: 0, lineSpacing: 18 });
s.addShape(pres.shapes.RECTANGLE, { x: 8.7, y: 4.1, w: 3.9, h: 1.5, fill: { color: CARD } });
s.addText("Lo que sigue es decidir qué hacer con cada problema. Cada decisión cambia una cifra del negocio.",
  { x: 8.95, y: 4.1, w: 3.4, h: 1.5, fontFace: F, fontSize: 14, bold: true, color: ACC,
    valign: "middle", isTextBox: true, margin: 0, lineSpacing: 19 });
pie(s, "Once problemas sembrados en la base. El Deber 2 pide al menos seis, con evidencia y decisión.");

// ── 16 · Las decisiones ──────────────────────────────────────────────────────
s = nueva("LAS DECISIONES",
  "68-73 min. Presentar los cuatro verbos con el ejemplo de esta base. Apuesta a mano alzada sobre las 9 cantidades negativas: borrar, valor absoluto, preguntar y documentar, o dejar. La correcta es preguntar y documentar: si son devoluciones reales, borrarlas infla la venta neta; ponerles valor absoluto convierte devoluciones en ventas. Documentar aplica siempre, también a lo que se decide no tocar.", "68–73");
titulo(s, "Cuatro decisiones posibles por problema");
tabla(s, [
  ["Verbo", "Cuándo", "En Andina Market"],
  ["Corregir", "La regla es conocida y reversible", "Unificar QUITO / quito / \" Quito\" con str.strip().str.title()"],
  ["Excluir", "La fila no puede ser verdad y no hay forma de repararla", "Envíos anteriores al pedido (6), si logística no los explica"],
  ["Imputar", "Hay un valor razonable y documentas el criterio", "Provincia vacía (32): se deduce de la ciudad"],
  ["Documentar", "Siempre. Los otros tres sin este no valen", "Toda la bitácora, incluidos los problemas que decides no tocar"],
], 0.75, 1.7, 7.6, [1.4, 2.7, 3.5], { fontSize: 12, boldCol: 0, rowH: 0.7 });
apuesta(s, "9 filas tienen Cantidad negativa. ¿Qué haces?", 8.7, 1.7, 3.9, 4.1, null);
const opc2 = ["A · Borrarlas: 9 en 1.335 no mueven nada.", "B · Valor absoluto: fue un signo mal digitado.",
  "C · Preguntar al negocio si son devoluciones y documentar la respuesta.", "D · Dejarlas: los datos no se tocan."];
s.addText(opc2.map((t, i) => ({ text: t, options: { breakLine: i < opc2.length - 1 } })),
  { x: 8.95, y: 3.25, w: 3.5, h: 2.4, fontFace: F, fontSize: 12.5, color: TINTA, valign: "top",
    isTextBox: true, margin: 0, paraSpaceAfter: 8 });
s.addText("Dejarlas tampoco es neutral: cualquier suma de cantidades ya las está restando. La decisión honesta se escribe, sea cual sea.",
  { x: 0.75, y: 5.6, w: 7.6, h: 0.8, fontFace: F, fontSize: 13, color: MUTED, isTextBox: true,
    margin: 0, lineSpacing: 18 });
bitacora(s, "Cantidad negativa · 9 · decisión: documentar la pregunta a ventas y la respuesta; no borrar ni cambiar el signo.");

// ── 17 · Paso 7 · Dos limpiezas resueltas ────────────────────────────────────
s = nueva("PASO 7 · DOS LIMPIEZAS RESUELTAS, CON SU VERIFICACIÓN",
  "73-80 min. Corren las dos limpiezas y las dos verificaciones. Ojo con Ventas: la conversión se aplica SOLO a las 43 filas con signo de dólar (máscara). Si se aplica el replace de puntos a toda la columna, 14.2 se vuelve 142 y se rompe todo lo que estaba bien. Ese es el error que más aparece en el Deber 2, vale la pena decirlo dos veces. Cada bloque genera una fila de bitácora con su evidencia de que quedó bien.", "73–80");
titulo(s, "Dos limpiezas, cada una con su verificación");
etiqueta(s, "A · VENTAS: DE \"$1.234,56\" A 1234.56, SOLO EN LAS 43 FILAS", 0.75, 1.7, 7);
codigo(s,
`mal = df["Ventas"].str.startswith("$")        # 43 filas
df.loc[mal, "Ventas"] = (df.loc[mal, "Ventas"]
    .str.replace("$", "", regex=False)
    .str.replace(".", "", regex=False)         # miles
    .str.replace(",", ".", regex=False))       # decimal
df["Ventas"] = df["Ventas"].astype(float)

df["Ventas"].dtype        # float64  ← la prueba
df["Ventas"].sum()        # 185,389.00`, 0.75, 2.05, 5.9, { fontSize: 11 });
etiqueta(s, "B · FECHAS: DOS FORMATOS EN UNA COLUMNA", 7.0, 1.7, 6);
codigo(s,
`for c in ["Fecha Pedido", "Fecha Envío"]:
    df[c] = pd.to_datetime(df[c], format="mixed",
                           dayfirst=True)

df.dtypes[["Fecha Pedido", "Fecha Envío"]]
# datetime64[ns]  ← la prueba
(df["Fecha Envío"] < df["Fecha Pedido"]).sum()
# 6`, 7.0, 2.05, 5.6, { fontSize: 11 });
s.addShape(pres.shapes.RECTANGLE, { x: 7.0, y: 4.35, w: 5.6, h: 1.3, fill: { color: CARD } });
s.addText("La máscara importa: si aplicas el replace de puntos a toda la columna, 14.2 se convierte en 142 y dañas las 1.292 filas que estaban bien. Limpia solo lo que está roto.",
  { x: 7.25, y: 4.35, w: 5.1, h: 1.3, fontFace: F, fontSize: 13, bold: true, color: ACC,
    valign: "middle", isTextBox: true, margin: 0, lineSpacing: 18 });
s.addText("Formato de la fila: qué había, cuántas filas, qué hiciste, por qué, y la evidencia de que quedó bien.",
  { x: 0.75, y: 5.85, w: 11.85, h: 0.5, fontFace: F, fontSize: 13, color: MUTED, isTextBox: true, margin: 0 });
bitacora(s, "Ventas como texto · 43 · corregido con máscara · prueba: dtype float64. Fechas · 35 · corregido · prueba: datetime64.");

// ── 18 · Paso 8 · Cierre del inventario ──────────────────────────────────────
s = nueva("PASO 8 · RESUMEN DE LA BITÁCORA",
  "80-84 min. Corren el drop_duplicates y comparan totales. Tres números que cuentan la historia entera: 704 mil si sumas la columna equivocada, 185 mil con Ventas limpia, 182 mil sin duplicados. Ese último es el que va al comité. Este es el cierre de la bitácora: filas iniciales, filas finales, y qué cifra del negocio cambió con tu limpieza.", "80–84");
titulo(s, "Filas iniciales, filas finales, y la cifra que cambió");
codigo(s,
`limpio = df.drop(columns=["ID Fila"]).drop_duplicates()
len(df), len(limpio)
# (1335, 1311)

df["Total Pedido"].sum()   # la columna equivocada
limpio["Ventas"].sum()     # la venta del año, limpia`, 0.75, 1.7, 6.0, { fontSize: 12 });
const cifras = [["$704,623", "sumando Total Pedido", TINTA], ["$185,389", "Ventas limpia, con duplicados", TINTA], ["$182,325", "Ventas limpia, sin duplicados", ACC]];
cifras.forEach((c, i) => {
  const y = 1.65 + i * 1.45;
  s.addText(c[0], { x: 7.3, y, w: 3.2, h: 0.9, fontFace: F, fontSize: 40, bold: true, color: c[2],
    isTextBox: true, margin: 0 });
  s.addText(c[1], { x: 10.4, y: y + 0.25, w: 2.3, h: 0.6, fontFace: F, fontSize: 12.5, color: MUTED,
    isTextBox: true, margin: 0, lineSpacing: 16 });
});
s.addShape(pres.shapes.RECTANGLE, { x: 0.75, y: 4.35, w: 6.0, h: 1.4, fill: { color: CARD } });
s.addText("Tu bitácora cierra con tres líneas: 1.335 filas iniciales, 1.311 finales, y la venta del año pasó de $185.389 a $182.325 al excluir duplicados.",
  { x: 1.0, y: 4.35, w: 5.5, h: 1.4, fontFace: F, fontSize: 13.5, bold: true, color: ACC,
    valign: "middle", isTextBox: true, margin: 0, lineSpacing: 19 });
s.addText("Y el problema siguiente ya está a la vista: la utilidad todavía tiene 15 centinelas y las cantidades negativas siguen ahí. Eso también se escribe.",
  { x: 0.75, y: 5.9, w: 11.85, h: 0.6, fontFace: F, fontSize: 13, color: MUTED, isTextBox: true,
    margin: 0, lineSpacing: 17 });
bitacora(s, "Resumen · 1.335 → 1.311 filas · venta del año: $182.325 · cifra que va al informe para Verónica.");

// ── 19 · Deber 2 y propuesta de proyecto ─────────────────────────────────────
s = nueva("EL DEBER 2 · BITÁCORA DE LIMPIEZA",
  "84-87 min. El deber es lo que ya hicieron, ordenado. Individual, buzón Deber 2 en D2L, fecha en el buzón. Mínimo seis problemas (hay once). Recordar la segunda entrega del mismo buzón: la propuesta de proyecto final del grupo, medio párrafo. Y la razón de fondo: la semana que viene la tabla de indicadores del Deber 3 se construye sobre esta misma base; sin bitácora, ningún total cuadra con el de nadie.", "84–87");
titulo(s, "La bitácora, ordenada y entregada");
etiqueta(s, "QUÉ ENTREGAS · INDIVIDUAL · BUZÓN DEBER 2 EN D2L", 0.75, 1.7, 7);
s.addText([
  { text: "Una página (PDF o el propio cuaderno) con una tabla de al menos 6 problemas, uno por fila: problema, filas afectadas, evidencia en código, decisión y justificación de negocio.", options: { bullet: { code: "2022", indent: 14 }, breakLine: true } },
  { text: "Cierre de tres líneas: filas iniciales, filas finales y qué cifra del negocio cambió con tu limpieza.", options: { bullet: { code: "2022", indent: 14 }, breakLine: true } },
  { text: "Mismo buzón, segunda entrega del grupo: la propuesta de proyecto final, medio párrafo con dataset, pregunta de negocio y decisión que habilita.", options: { bullet: { code: "2022", indent: 14 } } },
], { x: 0.75, y: 2.1, w: 7.2, h: 3.2, fontFace: F, fontSize: 14, color: TINTA, paraSpaceAfter: 12,
  isTextBox: true, margin: 0, lineSpacing: 20 });
etiqueta(s, "RÚBRICA · 10 PUNTOS", 8.5, 1.7, 4);
tabla(s, [
  ["Criterio", "Pts"],
  ["Detección: al menos 6 problemas reales", "3"],
  ["Evidencia reproducible: cada conteo con su código", "2.5"],
  ["Decisión y justificación de negocio por problema", "3"],
  ["Claridad de la bitácora y resumen final", "1.5"],
], 8.5, 2.1, 4.1, [3.3, 0.8], { fontSize: 12, center: [1], rowH: 0.55 });
s.addShape(pres.shapes.RECTANGLE, { x: 0.75, y: 5.35, w: 11.85, h: 0.95, fill: { color: CARD } });
s.addText("La semana que viene la tabla de indicadores se construye sobre esta misma base. Sin bitácora, los totales no cuadran entre compañeros ni con los de hoy.",
  { x: 1.0, y: 5.35, w: 11.4, h: 0.95, fontFace: F, fontSize: 14, bold: true, color: ACC,
    valign: "middle", isTextBox: true, margin: 0, lineSpacing: 19 });

// ── 20 · Contribuciones (queda visible en preguntas) ─────────────────────────
s = nueva("RESUMEN",
  "87-90 min. Slide final: se queda proyectada durante las preguntas. Recordar la entrega del Deber 2 y la propuesta de proyecto en el mismo buzón, y que el lunes se trabaja sobre esta misma base.");
const logros = [
  "Orden de trabajo: qué es una fila, tipos, huecos, duplicados. En otro orden los conteos salen mal.",
  "Cero es un dato, vacío es una pregunta y -9999 es un hueco guardado como número. isna() solo ve el segundo.",
  "Antes de buscar duplicados, quitar los identificadores automáticos. Una columna de otra granularidad no se suma: aquí infla la venta 3.8 veces.",
  "Un faltante se investiga por dónde se concentra y cómo se captura. No se borra ni se rellena sin documentarlo.",
];
logros.forEach((t, i) => {
  const y = 1.55 + i * 1.22;
  s.addShape(pres.shapes.OVAL, { x: 0.85, y, w: 0.55, h: 0.55, fill: { color: ACC } });
  s.addText(String(i + 1), { x: 0.85, y, w: 0.55, h: 0.55, fontFace: F, fontSize: 18,
    bold: true, color: "FFFFFF", align: "center", valign: "middle", isTextBox: true, margin: 0 });
  s.addText(t, { x: 1.7, y: y - 0.12, w: 10.8, h: 1.05, fontFace: F, fontSize: 16.5,
    color: TINTA, isTextBox: true, margin: 0, lineSpacing: 23 });
});
s.addText("Lunes 14 · Uniones y cardinalidad sobre esta misma base. Trae tu bitácora.",
  { x: 0.85, y: 6.6, w: 11.6, h: 0.5, fontFace: F, fontSize: 13, color: MUTED, isTextBox: true, margin: 0 });

pres.writeFile({ fileName: "S7-S8_Anatomia_y_Calidad.pptx" })
  .then((f) => console.log("OK →", f));
