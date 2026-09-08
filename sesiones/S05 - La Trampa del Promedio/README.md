# Sesión 5 · La trampa del promedio

**Lunes 31 de agosto de 2026 · Semana 3 · Bloque I · 90 minutos**

Un solo caso: **María, gerente regional Oeste de Superstore**, te llama a las 8h02 con tres preguntas para su comité de las 10h00 — el umbral de «envío gratis desde $X», qué inventario duplicar y si eliminar Libreros. Cada trampa es su siguiente pregunta. El taller vive en **Brightspace** como 7 páginas HTML con candado: nadie ve una gráfica sin apostar primero, y la última página es el encargo que se entrega.

| Pieza | Archivo | Para qué |
|---|---|---|
| **Taller + teoría + encargo (7 páginas)** | `brightspace/s05_p1..p7_*.html` | Subir a Brightspace → Contenido → Semana 3, en orden. Autocontenidas, CSS puro, sin JS |
| Slides (14, con notas del orador) | `S5_Trampa_Promedio.pptx` | Proyectar. Las notas traen el guion, los minutos y qué candado abre cada reveal |
| Guía del profesor | `guia_profesor.md` | Minutado 0–90, microcasos (= los candados 3, 4 y 5), dónde se pierden, plan B |
| Narrativa para ensayar | `narrativa.md` | Promesa y cierre palabra por palabra, arco, STAR |
| Cuaderno opcional (Colab) | `../../sitio/labs/taller_05_superstore.ipynb` | El mismo caso en Python, para práctica; enlazado desde la página 6 |
| Dataset 2026 | `../../sitio/datos/superstore_2026.csv` (y `.xlsx`) | Fechas sep-2022 → 29-ago-2026, columnas en español; botón de descarga en la página 2 |
| Figuras | `img/` + `generar_figuras.py` | 5 PNG fondo blanco (escalera, histograma, duelo, Libreros, muro de datos) |
| Generadores | `generar_lecciones_brightspace.py`, `crear_slides.js`, `preparar_superstore.py` (en `sitio/datos/`) | Regenerar cualquier pieza; toda cifra sale del CSV |

## Las 7 páginas

1. **La llamada** — María y su primera decisión · candado: clasificar la pregunta en la escalera → revela la escalera.
2. **El archivo** — 9,994 filas · candado: ¿cómo se responde con esto? → revela el muro de datos y las 4 preguntas descriptivas.
3. **El pedido típico** — muestra de 9 pedidos reales a mano · candado doble: campos de **media y mediana** + apuesta del % → revela el histograma y la trampa 1 (umbral ≈$200, no $459).
4. **El inventario** — ¿Muebles o Suministros? · candado: la apuesta → revela el duelo (el veredicto depende del árbitro).
5. **El memo de auditoría** — ¿firmas? · candado: la firma → revela la trampa inversa y el diagnóstico por descuento.
6. **El comité** — última apuesta (segmento), marcador de la mañana, regla de la casa y el memo de 3 líneas (primera diapositiva del reporte).
7. **El encargo de María** — la asignación: reporte de **5 diapositivas en PowerPoint** para el VP. Memo + una región a elección (Oeste/Este/Centro/Sur) con media, mediana, % bajo la media e histograma propio + veredicto + una pregunta de escalón 2. Rúbrica sobre 10 en la misma página. Entrega individual: `s05_reporte_apellido.pptx` al buzón, miércoles antes de clase.

## Checklist antes de clase (20 min)

1. Sube los 7 HTML **y** `superstore_2026.csv` (todo está junto en `brightspace/`) a la **misma carpeta** de Manage Files, y agrega las páginas a Contenido → Semana 3 en orden (nunca pegarlas en el editor: despoja el `<style>` y mata los candados). El botón "Descargar" de la página 2 enlaza el CSV en relativo — así no se ve de dónde viene el archivo.
2. **`git push`** — solo lo necesita el cuaderno opcional de Colab, que lee el CSV desde el repo.
3. Ponles **fecha de disponibilidad** a la hora de clase: los candados frenan las gráficas, no a un curioso con tiempo.
4. Crea el **buzón** "Taller 5 · Reporte para María" (entrega: miércoles antes de clase).
5. Abre las 7 páginas en el visor de Brightspace y prueba los candados de corrido (2 min).
6. Pizarra: dos marcadores, rojo y negro.

## Cifras canónicas (verificadas contra `superstore_2026.csv`)

Muestra a mano (página 3): 9 pedidos reales, suma $3,285 → media **$365**, mediana **$125**, 8 de 9 bajo la media. Escala completa: media **$458.61**, mediana **$151.96**, **72.5 %** bajo la media, p75 $512, p90 $1,154, máximo $23,661 (pedido `CA-2022-145317`, equipo Cisco de $22,638); umbral sugerido ≈$200. Utilidad por línea: Suministros de Oficina media $20.33 / mediana $6.88; Muebles $8.70 / $7.77; sin las 20 mejores líneas la media de Suministros cae a $14.61 (encuadernadoras GBC $4,946 e Ibico $4,630); Carpetas 19.84 / 3.98. Libreros: mediana +$4.13, media −$15.23, total −$3,473; 34 líneas < −$100 suman −$9,506; por descuento: 0 % → +$101.3, 50 % → −$236.4, 70 % → −$259.7. Con descuento (global): media −$6.66, mediana +$3.34 (5,196 líneas). Segmentos (pedido): Consumidor 449.1/154.7, Corporativo 466.4/**158.3**, Oficina en casa **472.7**/142.3. Desafío del Colab: Mesas −55.6/−31.4/−17,725.

**Para corregir el reporte (valor de pedido por región):** Oeste 1,611 pedidos, media $450.32, mediana $163.39, 72.2 % bajo la media · Este 1,401, $484.50, $150.76, 73.1 % · Centro 1,175, $426.59, $133.54, 72.9 % · Sur 822, $476.55, $159.98, 72.6 %. En las cuatro regiones la trampa aparece (ratio media/mediana 2.8–3.2): cualquier elección del estudiante debe concluir que el promedio también miente ahí.

Si cambias el dataset, corre `python3 ../../sitio/datos/preparar_superstore.py`, luego `python3 generar_figuras.py` y `python3 generar_lecciones_brightspace.py`; las comprobaciones didácticas avisan si alguna trampa se pierde.
