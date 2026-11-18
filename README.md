# Análisis de Datos con IA y Python · ADM 2003

**Universidad San Francisco de Quito · Sede Galápagos · Primer Semestre 2026-2027**
Lunes y miércoles · 31 sesiones de hora y media · del 17 de agosto al 9 de diciembre de 2026

Rediseño del curso ADM 2003 Análisis de Datos: sale KNIME, entra Python sobre Google Colab, y la inteligencia artificial generativa deja de ser un tema para volverse transversal. Lo que se califica no es el código sino la calidad del encargo al asistente y el rigor de la verificación.

---

## Sitio del curso

El sitio completo está en [`sitio/index.html`](./sitio/index.html): ábrelo en el navegador. Son **55 páginas** y funciona sin conexión.

| Página | Qué contiene |
|---|---|
| [Portada](./sitio/index.html) | Los cinco bloques del semestre y las dieciséis semanas |
| [Calendario](./sitio/calendario.html) | Las 31 sesiones con fecha, tema y entregable |
| [Laboratorios](./sitio/laboratorios.html) | Los 16 cuadernos de Python, con sus ejercicios y rúbrica |
| [Comercial Andina](./sitio/datos.html) | La base de datos del curso: siete archivos y qué enseña cada uno |
| [Proyecto integrador](./sitio/proyecto.html) | Las cinco fases del proyecto y el cuaderno reproducible |
| [Evaluación y política de IA](./sitio/evaluacion.html) | Distribución de la nota y reglas de uso del asistente |
| [Rúbricas](./sitio/rubricas.html) | Los seis instrumentos de evaluación, publicados desde la semana 1 |
| [Apoyo y accesibilidad](./sitio/apoyo.html) | Nivelación, ruta mínima si el grupo se atrasa y protocolo de datos |
| [Casos de estudio](./sitio/casos.html) | Los diez casos entre los que elige cada grupo |
| [DataCamp y concurso](./sitio/datacamp.html) | Las ocho certificaciones, sus alternativas, el registro y el concurso de XP |
| [Recursos y datasets](./sitio/recursos.html) | Simuladores, datos y material de apoyo |
| [Guía del docente](./sitio/docente.html) | De dónde salió cada pieza y qué falta construir |

Más 16 páginas de semana, 16 guías de laboratorio y 10 páginas de caso.

---

## Los datos: un negocio distinto cada semana

Las primeras cuatro semanas cambian de industria cada lunes, con datasets reales en [`sitio/datos/publicos/`](./sitio/datos/publicos/):

| Semana | Industria | Dataset | El gancho |
|---|---|---|---|
| 1 | Gastronomía | `pizza_ventas.csv` (del Taller 01 del curso anterior) | La pizza estrella cambia según la definición |
| 2 | Retail | `superstore.csv` (el dataset insignia de la clase) | ¿9 994 líneas, 5 009 pedidos o 793 clientes? |
| 3 | Música | `spotify_canciones.csv` | La media persigue a los remixes; la mediana no |
| 4 | Streaming | `netflix_titulos.csv` | El `dropna()` que borraba el 94,6 % de las series |

Más ocho datasets de práctica por interés — videojuegos, café, aviación, cine, autos, telecom, RRHH y banca personal — varios heredados de los casos del curso anterior (Telco KNN, abandono laboral, CO2). El catálogo completo está en [`sitio/datos.html`](./sitio/datos.html) y se regenera con `descargar_publicos.py`.

Desde la semana 5 entra **Comercial Andina**, el negocio integrado que acompaña el curso hasta diciembre: lo genera [`sitio/datos/generar_datos.py`](./sitio/datos/generar_datos.py) con semilla fija y contiene a propósito los fenómenos de cada semana (uniones que duplican, estacionalidad, estructura RFM, una paradoja de Simpson real y abandono desbalanceado).

## Los laboratorios y el aula

Dieciséis cuadernos en [`sitio/labs/`](./sitio/labs/), verificados uno por uno: cada cual se ejecuta de principio a fin sin errores antes de publicarse.

Las **sesiones 1 a 8** además están listas para dictarse desde [`sitio/aula.html`](./sitio/aula.html): ocho presentaciones que se proyectan desde el navegador (flechas para avanzar, `N` notas del docente con minutos, `G` vista de rejilla), cuatro casos de clase con juego de roles y giro, cuatro lecturas de estudio, ocho guiones del docente minuto a minuto, y cuatro simuladores interactivos nuevos: la pizza estrella, la unidad de análisis, media contra mediana y el detective de datos.

---

## Estructura del semestre

| Bloque | Semanas | Qué se construye |
|---|---|---|
| I · Leer datos | 1 – 5 | De la pregunta de negocio a una tabla limpia y agregada que se puede defender |
| II · Comunicar datos | 6 – 7 | Del gráfico honesto al tablero que contesta una pregunta gerencial |
| **Corte de medio semestre** | **8** | **Proyecto RFM+P: el primer entregable grande, todavía sin machine learning** |
| III · Decidir con datos | 9 – 11 | Comparación, causalidad, estrategia del negocio y criterio para elegir modelo |
| IV · Predecir | 12 – 14 | Pronóstico y propensión, siempre contra una línea base |
| V · Responder por el modelo | 15 – 16 | Ética, gobernanza y defensa del proyecto |

Dos fechas mandan sobre el resto: el **7 de octubre**, última clase antes del receso, se entrega el proyecto de medio semestre; el **7 y 9 de diciembre** se defiende el proyecto final ante panel.

---

## Estructura del repositorio

```
CursoAnalisisDatos_IA_2026/
├── sitio/                          # Sitio web del curso (55 páginas HTML)
│   ├── index.html                  #   portada
│   ├── semana-01..16.html          #   una página por semana
│   ├── lab-01..16.html             #   una guía por laboratorio
│   ├── caso-01..10.html            #   una página por caso de estudio
│   ├── calendario · laboratorios · datos · proyecto · evaluacion · rubricas
│   │   · apoyo · casos · datacamp · recursos · docente .html
│   ├── labs/                       #   los 16 cuadernos .ipynb, verificados
│   ├── datos/                      #   Comercial Andina: 7 CSV y su generador
│   ├── casos/                      #   los 10 casos de estudio en Markdown
│   ├── simuladores/                #   6 simuladores interactivos en HTML
│   ├── assets/estilos.css          #   identidad USFQ: rojo sobre blanco
│   └── _datos/
│       ├── contenido.py            #   contenido docente, rúbricas y protocolos
│       ├── datos_curso.py          #   calendario, material y mapeo (generado)
│       └── generar_sitio.py        #   generador del sitio
│
├── Propuesta En Construcción/
│   ├── ADM2003_cronograma_python_ia_v2.md      # tabla del sílabo y plan de sesiones
│   ├── ADM2003_calendario_S1_2026_LunMie.md    # calendario con fechas reales
│   ├── ADM2003_calendario_S1_2026_LunMie.xlsx  # el mismo, en el formato de la guía del profesor
│   ├── MAPEO_material_a_semanas_v2.md / .xlsx  # de dónde sale el material de cada semana
│   ├── ADM2003_syllabus_datacamp.md            # bloque de DataCamp listo para pegar en el sílabo
│   ├── _plantilla_sesion/                      # plantillas para escribir sesiones nuevas
│   ├── nueva_propuesta/                        # sílabo original en KNIME y notas del rediseño
│   └── _v1_superado/                           # primera versión del cronograma, solo referencia
│
└── Material Actual/
    ├── *.imscc                                 # exports originales de D2L
    └── Actividades Organizadas/                # las 53 actividades heredadas, con adjuntos
        └── INDICE.md
```

---

## Regenerar el sitio

El contenido vive en Python y el HTML se genera. Para cambiar una semana se edita `sitio/_datos/contenido.py` y se ejecuta:

```bash
cd sitio/_datos
python3 generar_sitio.py
```

No hay dependencias: solo Python 3. El HTML se sobrescribe completo, así que no se edita a mano.

Para cambiar los colores institucionales basta con tocar las variables del inicio de `sitio/assets/estilos.css`. El rojo está aproximado a partir de la marca USFQ; si tienes el hex exacto del manual, cámbialo en `--rojo` y todo el sitio se actualiza.

---

## Estado del rediseño

Los dieciséis laboratorios están escritos y verificados, la base de datos existe y las rúbricas están publicadas. Lo que falta, con fecha límite, está en la [guía del docente](./sitio/docente.html):

| Para el | Semana | Qué falta |
|---|---|---|
| 17-ago-2026 | 1 | Publicar el material de nivelación de Python: el laboratorio 1 ya usa `groupby` el segundo día |
| 17-ago-2026 | 1 | Subir el repositorio a GitHub y fijar `REPO_GITHUB` para que los badges de Colab funcionen |
| 17-ago-2026 | 1 | Verificar los ocho cursos de DataCamp contra el catálogo vigente |
| 24-ago-2026 | 2 | Redactar la carta de consentimiento de la empresa, una página |
| 26-oct-2026 | 10 | La clase teórica del lunes sobre transformación digital |
| 30-nov-2026 | 15 | El caso de riesgo crediticio de la clase teórica |

Una auditoría pedagógica externa revisó las dieciséis unidades y sus hallazgos ya están aplicados: la semana 11 se vació de código que no le correspondía, se corrigió una fuga de información en el modelo de la semana 13, cinco laboratorios sobrecargados movieron su exceso a un apéndice opcional, se añadió un ensayo de RFM sin nota en la semana 7 antes del entregable grande, y se escribieron las rúbricas, el protocolo de datos y la página de apoyo que no existían.
