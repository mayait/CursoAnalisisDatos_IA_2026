# S22 · Regresión con ajustes

**Lunes 9 de noviembre de 2026.** Continúa el caso Daniela (Bebidas Cumbre, 200 mercados) con curvas, interacciones, Ridge y Lasso.

| Pieza | Archivo | En D2L |
|---|---|---|
| Deck, 63 slides con 39 animaciones sin sonido | https://claude.ai/artifact/EgbKwaBmR3s5HDjVRnZmTt, copia en `deck/` | no se sube |
| PDF del deck | `Una-recta-no-se-dobla.pdf` | opcional |
| PowerPoint con las animaciones | `Una-recta-no-se-dobla.pptx` (lo genera `deck_a_pptx.py`) | no se sube |
| Explicación y caso en seis etapas | `d2l/semana11-regresion-con-ajustes.html` | Semana 11, con fecha de disponibilidad |
| Datos | `d2l/mercados-bebidas-cumbre.csv`, `d2l/consumo-combustible-co2.csv` | misma carpeta |
| Cuaderno del estudiante | `d2l/taller-ajustes-daniela.ipynb` | misma carpeta |
| Nueve animaciones | `d2l/animacion-*.mp4` | misma carpeta |
| Simulador | `simulador-ajustes.html` | opcional |
| Solución ejecutada | `solucion/` | **nunca** |
| Guía del profesor | `guia_profesor.md` | no se sube |

## Serie de videos

Diez episodios y cinco sub-videos de interacciones (E02A a E02E, que van entre el episodio 2 y el 3), unos 27 minutos en total, en `series/videos/` con sus subtítulos `.srt`. El guion completo está en `series/guion_serie.md` y su fuente es `series/guion.py`. Los episodios 3 y 8, y el final del 9, son ejercicios y no dan respuestas. Los episodios 4, 5 en adelante revelan resultados: se publican después del ejercicio que corresponde.

```bash
cd series
python generar_voces.py                  # voz con Gemini, en bloques, por la cuota diaria
python alinear.py carpeta_modelo         # corta cada bloque en frases con reconocimiento de voz local
python render_serie.py carpeta_media 8   # las 52 tomas en 1080p (manim en el PATH)
python render_serie.py carpeta_media --seco 9   # mide los tiempos de cada frase
python montar.py                         # episodios y subtítulos
python generar_doc.py                    # guion_serie.md
```

Las claves viven en `.env` en la raíz (permisos 600, ignorado por git).

## Regenerar

```bash
python generar_cifras.py         # cifras.json, fuente única
python generar_figuras_deck.py   # img_deck/
bash animaciones/render.sh       # desde animaciones/, necesita manim
python generar_d2l.py            # página y copia de videos
python generar_cuaderno.py       # cuaderno y solución
python deck_a_pdf.py             # PDF
```

Este material contiene una solución y cifras de control: el repositorio es público, así que `solucion/` y `guia_profesor.md` no se versionan.

## Antes de clase

- Subir a D2L la página, los CSV, el cuaderno y los videos en una sola carpeta.
- Poner fecha de disponibilidad a la página y crear la carpeta de entrega (domingo 15 de noviembre, 23:59).
- Abrir el simulador y el deck en modo presentación.

## Cifras canónicas

Margen 12 USD por unidad. Ventas en miles de unidades. División 150 y 50 con `random_state=42`.

| Modelo | Columnas | Error en prueba |
|---|---|---|
| Promedio | 0 | 4,68 |
| TV y radio | 2 | 1,39 |
| Con TV × radio | 3 | 0,65 |
| Con TV × radio y TV² | 4 | 0,48 |
| Con TV, √TV, radio y TV × radio | 4 | 0,29 |
| Grado 5 sin freno | 55 | 1,70 |
| Grado 5 con Ridge (α 0,03) | 55 | 0,36 |
| Grado 5 con Lasso (α 0,003) | 16 vivas | 0,35 |
| Grado 6 de la agencia (R² 0,998) | 83 | 3,25 |

Plan de Daniela (50 TV, 49 radio): 14,42 con el plano, 11,77 con la curva, utilidad +42,2 mil. Plan de la agencia: 14,48 y 15,22, utilidad +7,7 mil. Radio por mil USD: 89 unidades con TV 50, 197 con TV 150, 304 con TV 250. Equilibrio en 45 mil de TV. Veinte mercados parecidos al plan: vendieron 10,16 y el plano pronosticó 12,43.
