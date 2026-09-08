# Guía del profesor · Semana 4 · Sesiones 7 y 8
## Anatomía y calidad de los datos · Inventario de problemas

**Base:** `andina_market.csv` — filial ecuatoriana ficticia de Superstore. 1.335 líneas de pedido, 19 columnas, sep-2025 a ago-2026. Continúa la narrativa de María (S05). Todos los números salen de `clave.json` y se regeneran con `generar_dataset.py` (semilla fija 2003).

## Clave de los 11 problemas sembrados

| # | Problema | Filas | Cómo se detecta |
|---|---|---|---|
| P1 | Sin ID Cliente: 61 NaN + 38 `""` + 21 `"SIN-ID"` | **120 (9.0%)** | `isna()` solo da 61; el resto con `isin(["","SIN-ID"])` |
| P2 | Duplicados exactos | 24 | `drop(columns=["ID Fila"]).duplicated()` — con ID Fila da 0 |
| P3 | Fechas como texto, 35 en `dd/mm/yyyy` | 35 | `dtypes` → object; `to_datetime(format="mixed", dayfirst=True)` |
| P4 | Envío anterior al pedido | 6 | comparar fechas ya convertidas |
| P5 | Ventas como texto `$1.234,56` | 43 | `to_numeric(errors="coerce").isna()` |
| P6 | Ciudad inconsistente (QUITO/quito/&nbsp;Quito + Sto. Domingo ×14) | ~54 | `value_counts()` |
| P7 | Descuento NaN (no registrado) vs 0 legítimo | 212 vs 658 | `value_counts(dropna=False)` |
| P8 | Cantidad negativa (¿devoluciones?) | 9 | `df.Cantidad < 0` |
| P9 | Utilidad centinela -9999 | 15 | `value_counts()`; `isna()` no lo ve |
| P10 | Provincia nula | 32 | `isna()` |
| P11 | "Total Pedido" repetido por línea (granularidad) | todas | sumarla da $704.623 vs $185.389 reales (3.8x) |

Sin-cliente por región: Costa 11.4% · Sierra 7.1% · Galápagos 3.6% · Amazonía 0.0% (pista de proceso: cajas de mostrador).

Pedido ejemplo granularidad: **AM-2026-0042** = $187.40 (4 líneas); sumar "Total Pedido" da $749.60.

## Páginas D2L (carpeta `brightspace/` — 2 lecciones compactas + CSV, nombres sin underscores)

**Lunes · Sesión 7:** `lunes-granularidad-y-calidad.html` — una sola página con índice de anclas y 4 pasos: correo de auditoría + ausente/cero/desconocido (radio) → granularidad con AM-2026-0042 (apuesta numérica) → cero vs vacío vs centinela + tipos (radio) → descarga de la base y primer vistazo (radio).

**Miércoles · Sesión 8:** `miercoles-inventario-y-deber2.html` — 3 pasos: inventario con las dos trampas (duplicados/ID Fila y sin-cliente/isna, apuestas numéricas) → corregir/excluir/imputar/documentar + limpiezas resueltas (radio) → enunciado Deber 2 con rúbrica /10 y recordatorio de propuesta de proyecto.

El dataset de cara al estudiante se llama `andina-market.csv` (los botones "Descargar" y los ejemplos de código usan ese nombre).

Timing sugerido (90 min c/u): 15' caso y apuestas p1 · 25' p2 · 25' p3 · 25' p4 y arranque en vivo. Miércoles: 35' p1 · 30' p2 · 25' p3 y arranque del deber.

## Subida a D2L

1. Subir las 2 lecciones **y el CSV** a la misma carpeta (Manage Files → Upload), como archivos — no pegar en el editor.
2. Las páginas revelan respuestas: poner **fecha de disponibilidad** a la hora de clase (lunes / miércoles).
3. El buzón "Deber 2" define la fecha de entrega (las páginas remiten al buzón, no traen fecha).

## Regenerar

```bash
python3 generar_dataset.py     # andina_market.csv + clave.json
python3 generar_figuras.py     # img/fig1..fig4 (fondo blanco)
python3 generar_lecciones_brightspace.py  # brightspace/*.html + copia del CSV
```
