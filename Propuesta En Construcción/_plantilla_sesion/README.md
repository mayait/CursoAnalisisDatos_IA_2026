---
name: seminario-eda-sesion
description: Crea, edita o migra sesiones de clase con el formato del Seminario de Análisis Exploratorio de Datos (repo CursoPythonDatos_2026) — carpeta S0X-CY, README.md con barra de navegación y badges de Colab, clase.md, cuaderno clase_NN.ipynb, index.html del sitio estático, Lecturas.md curadas y notas_profesor.md minuto a minuto. Úsalo siempre que se pida armar una clase, una sesión, un cuaderno de curso, un caso de estudio o material docente en ese estilo, o al portar material de otro curso (D2L, KNIME, Tableau) a este formato.
---

# Sesiones del Seminario EDA

Formato de material docente en español, orientado a negocio, con cuadernos ejecutables en Colab y sitio estático tipo ReadTheDocs.

## Antes de escribir nada

1. **Ubica el repo.** Todo cuelga de la raíz del curso (`CursoPythonDatos_2026` o equivalente). Si no existe, créala con `README.md`, `requirements.txt`, `index.html`, `casos/` y `simuladores/`.
2. **Averigua el número de sesión y el módulo.** El encabezado dice `sesión N de M`; si no sabes M, cuéntalo en el README raíz antes de escribir.
3. **Decide el caso de negocio y el dataset antes del contenido.** El material se construye alrededor de una pregunta de negocio, no de una lista de funciones.

## Anatomía de una sesión

Carpeta `S0X-CY - Tema` (semana X, clase Y; la sesión final es `SF - ...`). Si la sesión cierra una entrega, el nombre termina en ` - ENTREGA N`.

| Archivo | Qué es | Obligatorio |
|---|---|---|
| `README.md` | Guía de la sesión **con** barra de navegación arriba y abajo y badges de Colab/nbviewer | Sí |
| `clase.md` | El mismo cuerpo, **sin** navegación ni badges. Es la fuente canónica del texto | Sí |
| `clase_NN.ipynb` | Cuaderno ejecutable, numerado por sesión global (`clase_06.ipynb` = sesión 6) | Sí |
| `index.html` | Página del sitio estático, generada a partir de `clase.md` | Sí |
| `Lecturas.md` | Curaduría comentada: técnicas, de negocio y video | Sí |
| `lecturas/` | Copias locales en `.md` de las lecturas, cuando la licencia lo permite | Recomendado |
| `notas_profesor.md` | Guion minuto a minuto para dictar la clase | Solo si se pide |

`README.md` = 6 líneas de navegación + `clase.md` + pie de navegación. **Nunca los edites por separado**: cambia `clase.md` y reconstruye los otros dos. Si notas que `index.html` dice algo distinto a `clase.md`, el HTML está desincronizado — regenéralo.

Las plantillas literales están en `reference/`. Léelas antes de escribir el archivo correspondiente:

- `reference/plantilla_readme_sesion.md` — cabecera, metadatos, secciones y pie
- `reference/plantilla_notebook.md` — orden de celdas, celda de setup, marcadores de ejercicio
- `reference/plantilla_lecturas.md` — formato de la curaduría
- `reference/plantilla_notas_profesor.md` — guion minuto a minuto
- `reference/plantilla_caso.md` — casos de estudio de `casos/`
- `reference/sitio_estatico.md` — esqueleto de `index.html` (usa `assets/estilos_sesion.css`)

Para crear el esqueleto completo de una sesión nueva:

```bash
python scripts/nueva_sesion.py --raiz . --semana 5 --clase 1 --sesion 9 --total 17 \
  --tema "Regresión lineal, polinomial y multicolinealidad (VIF)" \
  --modulo "Módulo 3 · Modelado supervisado" --repo we-human-centric/CursoPythonDatos_2026
```

Genera la carpeta, `README.md`, `clase.md`, `clase_NN.ipynb` y `Lecturas.md` ya enlazados. El contenido lo escribes tú encima.

## Cómo se escribe el contenido

**Tuteo, segunda persona, presente.** "Hoy das el salto a Pandas", no "el estudiante aprenderá Pandas". El texto le habla a una persona que va a ejecutar código en 10 minutos.

**Cada sección empieza por el porqué de negocio.** Primero qué decisión se toma mal sin esto, después la sintaxis. El patrón que funciona: problema real → intuición → código → interpretación → trampa frecuente.

**Nombra la trampa.** Toda sesión declara explícitamente el error que la gente comete: `R²` que siempre sube al añadir variables, `loc` frente a `iloc`, promedio que esconde una distribución bimodal. Va en su propio subtítulo con `⚠️`.

**Ejemplos locales y concretos.** Quito, Guayaquil, Cuenca, Loja; ventas, facturas, clientes, churn. Nada de `foo`, `bar` ni `df1`.

**Números redondos y verificados.** Si el texto afirma que el R² de validación cae a −0.12, esa cifra sale de ejecutar el cuaderno, no de la imaginación.

**Sin relleno.** Ni "en el mundo actual de los datos" ni "como todos sabemos". Si una frase se puede borrar sin perder información, bórrala.

**Emojis con función, no decorativos.** Solo en marcadores establecidos: `📌` idea central · `💡` intuición visual · `⚠️` trampa · `🎯` lectura de resultados · `🌶️`/`🔥` ejercicio y desafío · `📺` video · `📂` carpeta. Nunca en prosa corrida.

**Tono de las notas del profesor.** Ahí sí hablas al docente, en imperativo, con tiempos reales y con la "energía interna" de la sesión: qué hacer si tres personas no lograron instalar nada, qué recortar si vas tarde, qué frase abre la clase.

## Reglas del cuaderno

- La primera celda lleva el badge de Colab, el `H1` `## Sesión N · Tema` y un párrafo que conecta con la sesión anterior.
- La segunda celda es un `blockquote` con **Hoy haces** (qué se hace y cuánto dura) y **Entrega** (qué se sube y cuándo).
- La celda de setup siempre fija `SEED = 42`, importa `numpy`/`pandas`/`matplotlib`/`seaborn`, llama a `sns.set_theme(style="whitegrid", palette="deep")` y termina imprimiendo `Setup completo ✓` con las versiones.
- Los datos se leen por URL cruda (`raw.githubusercontent.com`) para que Colab funcione sin subir archivos. Nada de rutas locales.
- Secciones numeradas `## 1.`, `## 2.`… en el mismo orden que `clase.md`.
- Cada bloque teórico cierra con una celda de código ejecutable; cada ejercicio deja una celda vacía marcada `# TU CÓDIGO AQUÍ`.
- El cuaderno cierra con el entregable parcial y una celda "Para tu equipo" que aterriza lo del día en el caso asignado.
- El cuaderno se entrega **ejecutado de principio a fin**: ejecútalo antes de dar por terminada la sesión.

## Al portar material de otro curso

Al traer un ejercicio de KNIME, Tableau, Excel o de un cuaderno suelto:

1. Conserva **el dataset y la pregunta de negocio**; son lo valioso. El flujo de la herramienta vieja no se traduce, se reescribe.
2. Vuelve a redactar el enunciado con la estructura de `clase.md`. Un enunciado de dos líneas del LMS no es una sesión.
3. Añade la línea base obligatoria (`DummyRegressor`/`DummyClassifier`) y la interpretación en dinero cuando haya un modelo.
4. Declara la política de IA: se puede usar asistente, pero el cuaderno incluye el prompt final y la verificación de lo que devolvió.
5. Registra en `casos/` el caso si el ejercicio va a sostener el proyecto grupal.

## Verificación antes de cerrar

- [ ] `clase.md` y `README.md` coinciden salvo la navegación; `index.html` refleja lo mismo.
- [ ] Los enlaces de Colab, nbviewer y GitHub apuntan a la ruta URL-encodeada correcta (`%20` por espacio).
- [ ] Los enlaces `←`/`→` de sesión anterior y siguiente existen en el disco.
- [ ] La sidebar de `index.html` marca `active` la sesión actual y ninguna otra.
- [ ] El cuaderno corre de arriba a abajo sin errores y con salidas guardadas.
- [ ] `Lecturas.md` tiene al menos dos técnicas, dos de negocio y un video, cada una con su "Por qué leerlo".
- [ ] El README raíz lista la sesión nueva en su semana, con badge de Colab y entregable si aplica.
