# S24 · La fría cuesta más

**Lunes 16 de noviembre de 2026.** Lanzamiento del simulador de regresión por equipos y ronda 1 (regresión simple). El simulador vive en otro repositorio (`simuladores_clases`, carpeta `regresion/`).

| Pieza | Archivo | En D2L |
|---|---|---|
| Deck, 41 slides | https://claude.ai/artifact/JnbNV8sXxNeq3YS4pd3h2J, copia en `deck/project/` | no se sube |
| PDF y PowerPoint del deck | `La-fria-cuesta-mas.pdf` y `La-fria-cuesta-mas.pptx` (`deck_a_pdf.py`, `deck_a_pptx.py`) | nunca antes de la revelación: la slide 38 es la respuesta de la ronda 1 |
| Página para estudiantes | `d2l/semana12-la-fria-cuesta-mas.html` (la genera `generar_d2l.py`) | Semana 12 |
| Caso completo | `d2l/caso-la-fria-cuesta-mas.pdf` | misma carpeta |
| Guía del profesor | `guia_profesor.md` | **nunca** |
| Podcast del profesor, 10 min 27 s | `podcast/podcast-profesor-la-fria-cuesta-mas.mp3`, guion en `podcast/guion_podcast.md` | **nunca** |
| Plan de la sesión | `PLAN.md` | no se sube |

El simulador: https://regresion-simuladores.iahumana.org/login/ · partida `ADM2003`. Usuario: correo institucional. Clave: p más el código Banner. La lista de clase y el estado del despliegue están fuera de este repositorio, en `simuladores_clases/_privado_clase/`.

## Antes de clase

- Comprobar que el simulador responde y entrar como profesor.
- Abrir panel docente, proyector (`/proyector/ADM2003/`) y deck.
- Publicar la página de D2L y pegar en el chat el mensaje de ingreso (está en la guía).
- No abrir la ronda 1 hasta que todos estén dentro.

## Regenerar

```bash
python generar_figuras_deck.py          # img_deck/ (matplotlib; usa el .venv del checkout principal)
python generar_ilustraciones_gemini.py  # arte/n1 a n4, con GEMINI_API_KEY del .env de la raíz
python generar_d2l.py                   # página de D2L
python deck_a_pdf.py                    # PDF del deck desde deck/project
python podcast/generar_podcast.py       # audio con Gemini; no repite bloques ya generados
```

`deck/blobs.json` traduce cada imagen del artifact a su archivo en `deck/assets/`.

## Cifras de control

Exhibit 4 del caso: 74,926 botellas por semana antes del operativo, 149,505 durante, 61,349 después. Saldaña: S/ 248,000 a favor. Huamán: S/ 129,000 en contra con las semanas 14 a 19. Marca de demostración (no es la de ningún equipo): sin limpiar n 520, pendiente −31 y R² ajustado 0.001; limpia n 518, pendiente −6,463 y R² ajustado 0.18.

Este material contiene respuestas de la ronda 1. El repositorio es público: `guia_profesor.md`, `Guia-del-profesor.pdf`, `podcast/`, `PLAN.md`, `datos_demo/` y el deck no se versionan (están en el `.gitignore` de la raíz).
