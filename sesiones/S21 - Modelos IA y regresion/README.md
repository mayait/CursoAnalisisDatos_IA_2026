# Semanas 9 y 10 · Modelos, IA y regresión lineal

**Lunes 26 de octubre, miércoles 28 de octubre y miércoles 4 de noviembre de 2026.** El lunes 2 de noviembre fue feriado.

El 26 se dio el mapa de modelos y la primera recta (precio de una casa por metros cuadrados). El 28 la clase fue de teoría de IA y se dejó el encargo de Teachable Machine. El 4 los grupos presentan Teachable Machine y el caso Daniela pasa a decisiones con regresión lineal.

| Pieza | Archivo | En D2L |
|---|---|---|
| Teoría del lunes 26 | `d2l/semana9-que-es-un-modelo.html` | Semana 9 |
| Teoría del miércoles 28 | `d2l/semana9-que-es-la-ia.html` | Semana 9 |
| Deber 10, Teachable Machine (grupal, Deberes, 10 puntos) | `d2l/deber-10-teachable-machine.html` | Semana 9 + carpeta 916722, nota 2029090 |
| Caso Daniela, seis decisiones con regresión | `d2l/semana10-caso-daniela-regresion.html` | Semana 10 |
| Datos del caso | `d2l/mercados-bebidas-cumbre.csv` | Semana 10 |
| Actividad en clase, caso Daniela (individual, Participación, 10 puntos) | instrucciones en la carpeta | carpeta 916723, nota 2029091 |
| Guía del profesor del 4 de noviembre | `guia_profesor.md` | no se sube |
| Generador | `generar_d2l.py` | escribe todo `d2l/` y `cifras_caso.txt` |

Módulos D2L: Semana 9 es el 3625455, Semana 10 el 3625456. Todo se creó oculto.

```bash
../../.venv/bin/python generar_d2l.py
```

## Fuentes

- Deck del 26: "Del mapa de modelos a la primera regresión" (artifact https://claude.ai/artifact/6obQpcUqaGjfmKBgr3CpmJ).
- Video de apoyo: DotCSV, Modelos para entender una realidad caótica (https://www.youtube.com/watch?v=Sb8XVheowVQ): datos, parámetros, error y el ejemplo de Marte.
- Grabación del 28 transcrita con Whisper en `grabaciones/2026-10-28 - IA teoria y Teachable Machine/` (no se versiona).
- Datos del caso: Advertising (200 mercados), el mismo del deck y de lab_12, con columnas en español.

## Cifras canónicas del caso Daniela

Margen 12 USD por unidad. Ventas en miles de unidades, inversión en miles de USD. Todas salen de `generar_d2l.py`.

| | TV | Radio | Prensa |
|---|---|---|---|
| Correlación con ventas | 0,78 | 0,58 | 0,23 |
| Unidades por 1.000 USD | 47,5 | 202,5 | 54,7 |
| R² | 0,61 | 0,33 | 0,05 |
| Margen mínimo por unidad | 21,04 | 4,94 | 18,28 |
| Ganancia por 1.000 USD a 12 USD | −430 | +1.430 | −344 |
| Error medio en prueba (línea base 4,68) | 2,27 | 3,52 | 4,45 |

Modelo con los tres medios: prensa −0,0010 (p 0,86), R² 0,897 con o sin prensa, R² ajustado 0,8956 con prensa y 0,8962 sin ella. Correlación radio y prensa 0,35. Error en prueba de TV y radio juntos: 1,39 (tolerancia de Daniela: 2).
Modelo TV y radio sobre 200 mercados: ventas = 2,92 + 0,0458 · TV + 0,188 · radio.
Plan de la agencia (150 TV, 25 radio): 14,48 miles de unidades, intervalo 90 % de 11,70 a 17,27, margen 173,8 mil contra 175 de inversión.
Plan de Daniela (50 TV, 49 radio, 99 mil): 14,42 miles, intervalo de 11,60 a 17,24, margen 173,0 mil, peor caso 139,2.
