# ADM 2003 Análisis de Datos con IA y Python · USFQ Galápagos

Instrucciones para cualquier agente que trabaje en este repositorio (Claude Code, Codex u otro lanzado desde Orca). `CLAUDE.md` es un enlace a este archivo. El objetivo del proyecto es preparar las mejores clases posibles a partir de las clases anteriores, los datos, el sílabo, la planificación y las grabaciones de clase.

Última actualización del contexto: 3 de noviembre de 2026.

## 1. Quién y qué

Julián Maya, Director de Sede de USFQ Galápagos, dicta ADM 2003 Análisis de Datos para el Colegio de Administración. Periodo 202610, NRC 2241, lunes y miércoles, del 17 de agosto al 9 de diciembre de 2026, virtual sincrónico. Menos de 20 estudiantes en cinco grupos. La duración de la sesión está sin resolver: la memoria de Cowork dice 10:00 a 11:20 (80 minutos) y el README dice hora y media.

La tesis del curso: sale KNIME, entra Python con IA generativa como condición de trabajo y no como tema. Se califica la calidad del encargo al asistente y el rigor de la verificación, no el código. Toda entrega con modelo compite contra una línea base (`DummyRegressor`, `DummyClassifier`) y se califica la decisión, no la métrica. Julián quiere menos sensación de código y más teoría y contexto de negocio.

Evaluación fija: participación, deberes, evaluaciones y certificaciones (DataCamp) y proyecto final, 25 % cada una. El sílabo está aprobado por coordinación académica.

## 2. El plan cambia. Cómo saber dónde va el curso

El cronograma escrito ya no manda. Julián cambia de plan rápido ("todo se mueve y cambia"). No defiendas el calendario: señala lo que se rompe y sigue. Antes de preparar una clase, pregunta qué se dio en la última sesión si no está registrado.

Fuentes, de la más fiable a la menos:

1. Lo que diga Julián en la conversación.
2. La sección 3 de este archivo (estado real).
3. `Propuesta En Construcción/ADM2003_calendario_S1_2026_LunMie.md`, que tiene los ajustes del 29 de septiembre pero no el salto del 26 de octubre.
4. El sitio (`sitio/`), que refleja el diseño original de agosto y está desactualizado desde la semana 6.

Cuando el estado real cambie, actualiza la sección 3 de este archivo.

## 3. Estado real del curso

**Agosto.** Rediseño de KNIME a Python: seis pilares y calendario de 16 semanas (`Propuesta En Construcción/nueva_propuesta/handoff_ADM2003_rediseno_curso.md`).

**Semana 3, S05 La trampa del promedio (31 de agosto).** Superstore, personaje María. Nace el patrón de páginas D2L con candados.

**Semana 4, S07 y S08 fusionadas (7 de septiembre).** 90 minutos con Andina Market, personaje Verónica. Discrepancias pendientes de confirmar contra el CSV en `generar_lecciones_brightspace.py` y `guia_profesor.md`: `isna()` de ID Cliente da 99, no 61, más 21 SIN-ID, total 120. La limpieza de Ventas debe usar máscara solo en las 43 filas con "$".

**Semanas 6 y 7.** Bloque de IA con Google Antigravity y caso Carolina (facturados no entregados), adaptado del taller de Casabaca y Grupo Baca. Deber 7 grupal: PowerPoint y ZIP. Material en `sesiones/S11-S14 - IA con Antigravity y caso Carolina/`.

**Medio semestre, RFM+P** con `superstore_2026.csv` (la P es Profit). Individual de 15 puntos el domingo 11 de octubre (tablas) y grupal de 25 puntos el domingo 18 de octubre (insights y decisiones en PowerPoint), con los grupos del caso Carolina. Marco de clase: CRISP-DM. Julián rechazó una versión de 28 preguntas y seis clientes testigo por compleja. Para él, un checkpoint es una pregunta de control con valor numérico. Material en `sesiones/S08 - Proyecto RFM+P/`.

**Semana 8, visualización tipo Knaflic (19 y 21 de octubre).** Deck de 103 slides, siete ejercicios y dos prácticas sin número, ruta de siete pasos (abre, mira, prototipa a mano, ruido, limpia, decide, compara). Cada ejercicio cierra con slide limpio, slide anotado y slide del prompt. Deber 8 (ejercicios 1 a 3) y Deber 9 (ejercicios 4 a 7), 10 puntos cada uno, individuales. La actividad en clase de prácticas de visualización está en Participación (decisión pendiente: puede pasar a Deberes).

**26 y 28 de octubre: salto del cronograma hacia modelos.** Deck "Del mapa de modelos a la primera regresión". Lunes 26: qué es un modelo, cinco familias más "ninguna", línea base, ecuación de valor y una primera recta a mano (precio de casa por metros cuadrados). Miércoles 28: no se dio la regresión del deck sino una clase teórica de IA (historia, empresa, hype cycle, paradoja, autonomía y adaptabilidad) y se dejó el Deber 10 de Teachable Machine. La grabación transcrita está en `grabaciones/2026-10-28 - IA teoria y Teachable Machine/`.

**Miércoles 4 de noviembre** (el lunes 2 fue feriado): presentaciones de Teachable Machine y caso Daniela, seis decisiones con regresión lineal sobre Advertising (Bebidas Cumbre). Material, guía del profesor y cifras en `sesiones/S21 - Modelos IA y regresion/`. En D2L: módulos Semana 9 (3625455) y Semana 10 (3625456), Deber 10 (carpeta 916722, grupal) y Actividad en clase Caso Daniela (carpeta 916723, Participación, entrega domingo 8) y Actividad en clase Cuatro rectas de Bebidas Cumbre (carpeta 916781, nota 2029173, Participación, visible, vence el mismo 4 a las 11:30 de Galápagos). Todo se subió oculto el 3 de noviembre.

**Temas saltados que siguen pendientes:** devolución del RFM+P y segmentación con KMeans, "comparado con qué" y pruebas estadísticas (`lab_12` secciones 5 y 6 se apoyan en esto), transformación digital con journey map y service blueprint.

**Numeración rota.** En D2L el último deber es el Deber 10 (Teachable Machine); el siguiente es el Deber 11. El sitio dice Deber 6 para pronóstico y los cuadernos hablan de semanas 9 y 11. Verifica antes de citar un número de deber o de semana. Las carpetas de `sesiones/` tampoco siguen una sola convención (S05 es la sesión 5, S07 cubre las sesiones 7 y 8, S08 es el proyecto de la semana 8, S11-S14 son las sesiones 11 a 14).

## 4. Dónde está cada cosa

| Ruta | Qué es |
|---|---|
| `sesiones/` | El material que de verdad se dictó, una carpeta por sesión o bloque, con generadores, guía del profesor y páginas D2L |
| `sitio/` | Sitio estático del diseño original. Se genera con `sitio/_datos/generar_sitio.py` desde `contenido.py` y `datos_curso.py`. No editar el HTML a mano |
| `sitio/labs/` | `lab_01` a `lab_16`, `lab_01_ia` y talleres. Reglas en `sitio/labs/_ESPECIFICACION.md` |
| `sitio/datos/` | Comercial Andina (`generar_datos.py`, semilla fija) y Superstore 2026 (`preparar_superstore.py`) |
| `sitio/simuladores/` | 8 simuladores HTML autocontenidos (el README dice 6) |
| `sitio/casos/` | 10 casos de estudio |
| `Propuesta En Construcción/` | Calendario con fechas, mapeo de material a semanas, syllabus de DataCamp, plantillas y handoff del rediseño |
| `Material Actual/` | Exports de D2L (`.imscc`) y las 53 actividades heredadas en `Actividades Organizadas/INDICE.md`. El caso Blue Detergent está en `09_Casos_y_Procesos_de_Negocio/` |
| `grabaciones/` | Grabaciones y transcripciones de clases anteriores. No se versiona (ver sección 9) |

D2L: `miusfv.usfq.edu.ec`, org unit 331555. A los estudiantes siempre se les dice D2L, nunca Brightspace.

Artifacts del curso en claude.ai (no asumas cuál de los de RFM+P es el vigente, pregunta):

- Del mapa de modelos a la primera regresión: https://claude.ai/artifact/6obQpcUqaGjfmKBgr3CpmJ
- Del ruido a la historia, taller Knaflic: https://claude.ai/artifact/ECcoHiDaZaH1MPxcyd2xxU
- Proyecto de medio semestre, guía de revisión y feedback: https://claude.ai/artifact/7ikdVzB969uQbqkGLBR5Wj
- Proyecto RFM+P Superstore: https://claude.ai/artifact/YQGf7xjAjAjfVrGQcHBRSz
- RFM+P Superstore: https://claude.ai/artifact/SCVAdApebXoR9cgcFYWCoy
- RFM+P Superstore 2026: https://claude.ai/artifact/Eqohxk7m3t2zYZ5QswT3Kq
- Checkpoints RFM+P: https://claude.ai/artifact/Sgq6k3cDcp9z185p5C1K5E
- Caso Carolina en Antigravity: https://claude.ai/artifact/9hhpRhuXhfST6HuAcyJxRE
- Caso Carolina, presentación al comité: https://claude.ai/artifact/M1jwfrNrxShycU8ENSkHp8
- We Want More Galápagos, lienzo de marca: https://claude.ai/artifact/5zyj8qx6fLXwquWKicKTRV

## 5. Entorno y comandos

Orca crea cada worktree con `scripts/orca_setup.sh` (declarado en `orca.yaml`): copia desde la raíz el material local que no está en git, enlaza `grabaciones/`, crea `.venv` con `requirements.txt` y instala `pptxgenjs`. Al archivar, `scripts/orca_archive.sh` rescata a `_rescate_worktrees/` el material sin versionar creado en el worktree. En la raíz, ejecuta `bash scripts/orca_setup.sh` una vez para tener el mismo entorno.

```bash
.venv/bin/python sitio/datos/generar_datos.py               # regenera Comercial Andina (imprime comprobaciones didácticas)
cd sitio/_datos && ../../.venv/bin/python generar_sitio.py  # regenera el sitio
.venv/bin/jupyter nbconvert --to notebook --execute --inplace sitio/labs/lab_12.ipynb   # verifica un cuaderno
node "sesiones/S07 - Granularidad y Calidad/crear_slides.js"  # decks viejos en pptxgenjs
```

Los estudiantes trabajan en Google Colab. Los cuadernos leen los datos por URL cruda de GitHub, así que un cambio de datos solo llega a Colab después de `git push`.

## 6. Cómo se construye una clase

Cada clase nace de una pregunta de negocio y un personaje con un encargo (María, Verónica, Carolina), no de una lista de funciones. La teoría se entreteje: apuesta, reveal, teoría, decisión. Toda cifra que aparezca en material se calcula sobre el dato real antes de escribirla, y los generadores son la fuente: si una cifra cambia, se regenera la pieza, no se corrige a mano.

Piezas habituales de una sesión en `sesiones/`: README con el inventario de piezas, el checklist antes de clase y las cifras canónicas verificadas; páginas D2L; deck; `guia_profesor.md` con minutado y plan B; figuras con su generador.

**Lección D2L.** Un solo HTML por sesión con índice de anclas y "volver al índice". Nombres con guiones, nunca guion bajo (excepción: los CSV del taller Knaflic). Imágenes en base64, CSS en el archivo, sin JS. Candado con input oculto antes de `.reveal` (`input:checked ~ .reveal` e `input:not(:placeholder-shown)`). Sin contadores de pasos, sellos ni emojis. Pie único: "Ve al siguiente tema →". Datasets con botón Descargar y href relativo, nunca URLs crudas. Las páginas que revelan respuestas llevan fecha de disponibilidad y se suben como archivo, nunca pegadas en el editor.

**Laboratorios.** Los manda `sitio/labs/_ESPECIFICACION.md`: setup literal, 25 a 45 celdas, tres ejercicios, La trampa de hoy, Entregable, Para tu equipo. El cuaderno se entrega ejecutado de principio a fin.

**Enunciados.** Muy simples y humanos, con etapas y entregables claros. Los estudiantes con IA se desconectan de lo que él espera, así que el pedido debe ser inequívoco.

**Feedback a estudiantes.** Muy corto y cercano, elogio breve y foco en lo que faltó.

**Agente de los estudiantes: Google Antigravity.** Carpeta de trabajo compartida con el agente (entradas, datos, salidas, procesamiento, archivo, contexto). Siempre generar `CONTEXTO.md`, revisar archivos y planificar antes de ejecutar. Los resultados parciales se revisan como entregables parciales. Los prompts se copian en `contexto/prompts.md`, que se entrega. Si el resultado no cuadra se corrige el prompt, no la imagen. Desde la parte 2 de un caso, menos prompts y solo pistas de qué deben tener, cómo organizarse y qué revisar. Preguntas de control con cifras esperadas y qué revisar si no cuadran. Cada etapa tiene un punto crítico para pensar. Agentes para tareas acotadas, no para hacer todo el caso.

### Cifras canónicas de lab_11 y lab_12 (cuadernos ejecutados completos)

TV: 0,0475 unidades por dólar, es decir 47,5 por cada mil, margen mínimo 21,04 USD. Línea base contra regresión en TV: de 4,68 a 2,27 miles (menos 51 %). Comercial Andina, volantes: error de 4,90 % contra 14,04 % de la línea base. Coeficiente 38,34, que no es un retorno de 3.734 % por causalidad inversa. Pedir 7,5 % de más por error asimétrico. Clasificador base: 97,65 % de exactitud y 0 % de devoluciones encontradas. Mismo modelo de abandono: menos 6.600 o más 3.577 USD al año. Punto de equilibrio con 300 llamadas: 7,78 %.

## 7. Sistemas visuales

Conviven tres. No los mezcles sin preguntar. Todo entregable visual va con fondo blanco, incluidos gráficos, mapas de calor y diagramas.

**A. Sitio y lecciones D2L, identidad USFQ clásica** (`sitio/assets/estilos.css`). Rojo #A6192E, tinta #232326, papel #FFFFFF. Source Sans 3, Source Serif 4 y JetBrains Mono. Colores por bloque: b1 #0F6E8C, b2 #7A4BA8, b3 #A6192E, b4 #0B6E4F, b5 #B26B00, b6 #3E5C8A. Las lecciones D2L usan contenedor de unos 760 px y Segoe UI. La cabecera #111 con borde rojo es una excepción heredada, no la extiendas.

**B. Decks actuales, We Want More** (skill `marca-usfq-galapagos-we-want-more`). Rojo #E11B22, negro y blanco. Zalando Sans Expanded 900 en mayúsculas para titulares, cuerpo Arial o Helvetica, etiqueta en bloque negro. El pie WE WANT MORE más palabra en bloque solo en portada y slides clave. Cierre tipo MORE EVIDENCE, MORE DRAGONS. Nunca azul ni turquesa de marca como color principal. Técnica: artifact tipo Slides con `deck.json` (order, sections) y `project/slides/*.html`, un section de 1920x1080 con estilos inline, padding 128 y aside como notas del orador. Gráficas en PNG de matplotlib, fondo blanco, anotación dentro de la imagen, nunca texto HTML encima. Rojo #E11B22 para la marca, #1F6FB2 para la contrahistoria, #7FB0DE secundario, #F2A900 acento raro, gris el resto. El skill pide fotografía, pero Julián pidió collage: gana Julián.

**C. Ilustraciones** (skill `ilustraciones-collage-galapagos`). gpt-image-2 en calidad alta, prefijo fijo de gouache y papel recortado, escena en inglés con gente local y un lugar real de San Cristóbal, sin texto en la imagen.

**Simuladores**, sin sistema único: 4v-bigdata usa la identidad A; regresión lineal, train-test, overfitting y regresión 3D usan un flujo por pasos (Segoe UI, #1e293b, #2563eb, #059669); confusion-matrix usa Tailwind y Chart.js; vif usa Plotly y PapaParse. Son HTML sin backend. GitHub Pages da 404, así que se proyectan desde local o se suben a D2L.

## 8. Reglas de Julián

- Escribe y responde en español. Sin frases de apertura ni sugerencias o próximos pasos al final. La entrega va lista para copiar.
- En textos: sin rayas largas, pocos punto y coma, frases completas, sin comillas angulares, sin emojis, tono humano y pocas viñetas.
- Slides de clase: título directo con el hecho e insights planos. Nada de "Hoy aprenderemos", "Al salir de esta sala", "Miente", "la trampa de" ni "los tres impostores" en material nuevo, salvo que él lo pida.
- Slide final de datos: la gráfica habla, una marca, sin bloques de historia ni etiquetas de insight, leyendas simples solo si hacen falta.
- Nunca eliminar archivos: se mueven a una carpeta `Eliminar` o `Archivo`.
- Nunca mencionar UNIANDES.
- Si pide algo en una app que no se puede ejecutar desde aquí, entrega el prompt listo para el agente del navegador.
- Recibe bien el desacuerdo argumentado: señala el costo de cada decisión en lugar de solo ejecutar.

## 9. Repo público, datos y seguridad

El repositorio `github.com/mayait/CursoAnalisisDatos_IA_2026` es público. Nunca se suben soluciones, informes docentes, notas, correos o datos de estudiantes, ni grabaciones o transcripciones de clase. `grabaciones/` y `_rescate_worktrees/` están en `.gitignore`. Antes de un commit, revisa que no entre material de ese tipo y pregunta si hay duda. Hay material local sin versionar en `sesiones/`: revisa `git status` antes de confiar en lo que hay en GitHub.

La clave de OpenAI para imágenes vive en `.env` en la raíz (`OPENAI_API_KEY`, ignorado por git, permisos 600; el setup de Orca lo copia a cada worktree). Nunca la imprimas, la copies en otro archivo ni la pegues en material o mensajes. Las ilustraciones se generan con `.venv/bin/python scripts/generar_ilustraciones.py escenas.json carpeta`, que aplica el prefijo del skill `ilustraciones-collage-galapagos`.

Todo deck lleva ilustraciones, diagramas y animaciones: visual sobre texto, una idea por slide y el mínimo de palabras.

## 10. D2L

Se opera desde el Chrome de Julián (skill `chrome-browser`) con la sesión iniciada. Para subir un HTML como tema: POST multipart/mixed a `content/modules/ID/structure/` con una parte JSON (Type 1, TopicType 1, Url `/content/enforced/331555-202610-2241/archivo`) y una parte con el archivo; para pasar archivos grandes al navegador, gzip más base64 y `DecompressionStream`. D2L inyecta sus scripts al servir el HTML, así que para verificar se comparan los tamaños sin los `<script>`. Las carpetas se enlazan al módulo por la interfaz: Agregar, Asignación, Agregar existente. La salida de `javascript_tool` se bloquea si contiene `?`, `&` o `=`: reemplázalos antes de devolver texto. Con `javascript_tool`, fetch a `/d2l/api/le/1.75/331555/` (`content/toc`, `content/modules/ID/structure/`, `dropbox/folders/`, `grades/`, `grades/categories/`). Para escribir, header `X-Csrf-Token` con `localStorage.getItem('XSRF.Token')`. Los archivos se sirven desde `/content/enforced/331555-202610-2241/`. Primero el ítem de nota y luego la carpeta, con `IsHidden: true`. Los deberes se enlazan a contenido por la interfaz (Add existing, Deberes). Publicar solo cuando Julián lo pida. Nunca borrar en D2L. IDs vistos: Deber 7 carpeta 912597 y nota 2019190; Deber 8 carpeta 914638 y nota 2025203; actividad de prácticas, nota 2026321.

## 11. Grabaciones de clase

Cuando Julián pase grabaciones de clases anteriores, van en `grabaciones/AAAA-MM-DD - tema/` con el archivo original y una `transcripcion.md`. De cada grabación interesa qué funcionó, dónde se perdieron los estudiantes, qué preguntaron y qué improvisó Julián, para alimentar la siguiente versión de la clase. Las conclusiones útiles se pasan a la guía del profesor de la sesión correspondiente, nunca citas de estudiantes con nombre.

## 12. Skills útiles

`marca-usfq-galapagos-we-want-more` (decks), `ilustraciones-collage-galapagos` (imágenes), `chrome-browser` (D2L), `pptx` (si pide archivo PowerPoint; los decks viejos usan pptxgenjs), `hubi-reporte-estudiantes-por-nrc` (lista de estudiantes), `data:*` y `dataviz` (análisis y gráficas). `seminario-eda-sesion` describe el formato de otro curso: úsalo solo si se pide, porque D2L sigue el patrón de la sección 6. Los skills de Orca (`orca-cli`, `orchestration`) están instalados en el proyecto.
