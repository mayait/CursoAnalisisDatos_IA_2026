# 📦 Entregable Intermedio — Mitad del Seminario
### Punto de control de medio camino · Casos de Estudio · Seminario

---

## 🎯 Propósito de este punto de control

Este entregable busca asegurar que cada grupo llegue a la segunda mitad del seminario con su proyecto **estructurado, versionado y documentado**, no solo con código suelto en cuadernos sin contexto. La idea es construir desde aquí, sin reorganizaciones traumáticas, hacia el modelado, la comparación y el producto analítico final.

A diferencia de la entrega final, aquí no evaluamos sofisticación de algoritmos. Evaluamos **higiene del proyecto**, profundidad del entendimiento del negocio y calidad del análisis exploratorio inicial.

> 🟢 Aprobar este punto de control = la base sólida está. 🔴 Reprobarlo = el grupo arrastra deuda técnica que crecerá la última semana.

---

## 🗂️ Estructura de repositorio obligatoria

Cada grupo crea un repositorio en GitHub con esta estructura. Está pensada para sostener todo el ciclo del caso, desde la primera carga de datos hasta el dashboard final.

```
GRUPO_X/
├── 00_datos_crudos/             # Datos originales, intocables
├── 01_datos_procesados/         # Datos limpios, listos para modelar
├── 02_scripts/                  # Módulos .py reutilizables (utils, etl, viz)
├── 03_cuadernos/                # Jupyter notebooks numerados
├── 04_modelos/                  # Modelos entrenados, scalers, encoders (joblib)
├── 05_referencias/              # Papers, datasheets, capturas, fuentes externas
├── 06_archivo/                  # Experimentos antiguos que ya no se usan
├── 07_CONTEXTO/                 # Entendimiento del dominio
│   └── 01_RESUMEN_DEL_CASO.md
├── 08_PLAN_Y_EJECUCION/         # Planes y bitácoras
│   ├── readme.md                # Índice del plan general
│   ├── preparacion_datos.md     # Plan de limpieza y transformación
│   └── uso_de_ia.md             # Bitácora obligatoria de uso de IA
├── README.md                    # Portada del repo
├── requirements.txt             # Dependencias con versiones fijadas
└── .gitignore                   # Ignorar datos pesados, checkpoints, venv
```

> 💡 Es un esqueleto, no una camisa de fuerza. Si su caso requiere una carpeta extra (por ejemplo `09_geodata/` para Caso 4 o Caso 5, o `09_consultas_sql/` para casos con base de datos), agréguenla. Lo que **no** es negociable son las carpetas `07_CONTEXTO`, `08_PLAN_Y_EJECUCION` y los cuadernos numerados de `03_cuadernos/`.

---

## ⚠️ Antes de hacer push: el límite de tamaño de GitHub

GitHub bloquea archivos de más de **100 MB** y muestra advertencia para archivos > 50 MB. La regla práctica para este seminario es: **datos pesados nunca van al repo**. Si su dataset crudo supera el límite (lo cual ocurre en varios casos):

1. **No lo suban**. Añadan el patrón al `.gitignore` (`00_datos_crudos/*.csv`, `00_datos_crudos/*.parquet`, etc.)
2. Documenten en `00_datos_crudos/README.md` **cómo descargar** el dataset: link a la fuente, comando reproducible (`kaggle datasets download ...`, `wget ...`), y el tamaño esperado del archivo para verificar la descarga.
3. Si el dataset procesado también pesa demasiado, exporten una **muestra representativa** (ej. `muestra_5pct.parquet`, ~10–20 MB) que sí pueda versionarse, para que cualquiera pueda reproducir el EDA sin descargar el original completo.

> No vamos a usar Git LFS en este seminario. Añade fricción y no aporta para la entrega final.

---

## ✅ Checklist del entregable

### 1. Repositorio en GitHub funcional
- [ ] Repo creado, público (o privado con el docente como colaborador)
- [ ] Estructura de carpetas según el esqueleto anterior
- [ ] `README.md` raíz con: título del caso, integrantes, instrucciones para instalar dependencias y descargar los datos
- [ ] `.gitignore` correcto (datos pesados, `__pycache__/`, `.ipynb_checkpoints/`, `venv/`, `.DS_Store`)
- [ ] `requirements.txt` con versiones fijadas (`pandas==2.2.2`, no `pandas` a secas)
- [ ] Mínimo **3 commits por integrante** con mensajes descriptivos. Mensajes como `update`, `fix`, `final`, `final_v2` no cuentan.

### 2. Datos crudos disponibles (`00_datos_crudos/`)
- [ ] Si pesan < 100 MB: archivo en el repo
- [ ] Si pesan ≥ 100 MB: archivo `00_datos_crudos/README.md` con link, comando de descarga reproducible y tamaño/hash esperado del archivo

### 3. Datos procesados (`01_datos_procesados/`)
- [ ] Al menos un archivo `.parquet` (preferido) o `.csv` con los datos limpios
- [ ] Nombre claro: `transacciones_limpias.parquet`, no `df_v3_final_actualizado.csv`
- [ ] Schema documentado en el README de la carpeta o en el cuaderno de preparación

### 4. Contexto y entendimiento del negocio (`07_CONTEXTO/01_RESUMEN_DEL_CASO.md`)

Aquí demuestran que entendieron **el problema antes de tocar el código**. Mínimo:

- [ ] **Resumen del caso en sus propias palabras** (no copiado del enunciado): 1–2 párrafos
- [ ] **Contexto del dominio / industria**: ¿qué hace este negocio? ¿quién toma la decisión que ustedes apoyan? ¿qué incentivos tiene? Investigación con **mínimo 3 fuentes externas citadas** (no Wikipedia, no el enunciado).
- [ ] **Pregunta de negocio principal** y **2–3 preguntas secundarias** derivadas
- [ ] **Métrica de éxito**: ¿cómo sabremos si la solución sirve? ¿qué KPI cambia y en qué dirección?
- [ ] **Diccionario de variables** del dataset crudo en formato tabla: nombre, tipo, descripción, rango/valores posibles, % de nulos, observaciones. Todas las columnas, no las "interesantes".
- [ ] **Hipótesis iniciales** (mínimo 5) que el EDA validará o rechazará. Ejemplo: *"Los clientes que compran en diciembre tienen un valor promedio mayor que el resto del año"*, no *"hay estacionalidad"*.

### 5. Plan de preparación de datos (`08_PLAN_Y_EJECUCION/preparacion_datos.md`)
- [ ] Pasos de limpieza en orden, con justificación
- [ ] Decisiones explícitas sobre: nulos, duplicados, outliers, tipos de datos, encodings, parseo de fechas
- [ ] Variables nuevas que se construirán (feature engineering inicial) y por qué
- [ ] **Lo que se descarta y por qué se descarta**. Esa es la parte difícil: no es trivial justificar qué columnas quedan fuera.

### 6. Cuaderno de preparación de datos (`03_cuadernos/01_preparacion_datos.ipynb`)
- [ ] Ejecuta de principio a fin sin errores (Restart & Run All antes de comitear)
- [ ] Carga desde `00_datos_crudos/`, guarda en `01_datos_procesados/`
- [ ] Cada celda de código viene con celda de markdown explicativa: qué hace y por qué. No es un script disfrazado.
- [ ] **Validaciones explícitas** intercaladas: `assert df.shape[0] > 0`, `assert df['cliente_id'].notna().all()`, `assert df['fecha'].dtype == 'datetime64[ns]'`
- [ ] Implementa el plan declarado en `preparacion_datos.md`. Si en el camino cambian algo, actualizan el plan.

### 7. Cuaderno de Análisis Exploratorio (`03_cuadernos/02_eda.ipynb`)
- [ ] Ejecuta de principio a fin sin errores
- [ ] **Estadística univariada**: distribución, medidas de tendencia central y dispersión de cada variable relevante
- [ ] **Estadística bivariada**: relaciones entre variables, y de cada variable con la variable objetivo (si el caso es supervisado) o con las dimensiones clave del problema (si es no supervisado)
- [ ] Mínimo **8 visualizaciones** con título, ejes etiquetados, leyenda cuando aplique, y un comentario interpretativo en markdown debajo. Gráficas mudas no cuentan.
- [ ] **Sección final de Insights**: mínimo **5 hallazgos accionables**, cada uno estructurado como:
  - **Qué se observó** (con evidencia gráfica o numérica)
  - **Por qué importa para el negocio**
  - **Qué hipótesis confirma o rechaza**
  - **Qué decisión cambia o qué pregunta nueva abre**

### 8. Bitácora de uso de IA (`08_PLAN_Y_EJECUCION/uso_de_ia.md`)
> Sección **no opcional**. Detalle en el bloque siguiente.

---

## 🤖 Uso de IA: invitación con honestidad

**Sí, queremos que usen IA.** Antigravity, Claude Code, Cursor, Copilot, ChatGPT, Gemini — lo que prefieran. La realidad profesional actual es que un analista de datos que no usa IA está dejando productividad sobre la mesa, y este seminario los prepara para esa realidad, no para una versión nostálgica.

Pero el trato es claro: **toda interacción significativa con IA debe quedar registrada** en `08_PLAN_Y_EJECUCION/uso_de_ia.md`. Esto cumple varios objetivos a la vez:

1. Ustedes mismos aprenden qué prompts funcionan y cuáles no
2. Pueden volver atrás meses después y entender qué decisiones tomó la IA por ustedes
3. La evaluación distingue entre *"le pasé el caso a la IA y di copy-paste a todo"* vs. *"usé IA como copiloto y entendí cada línea"*
4. Es la práctica que se está estandarizando en la industria — anótenlo como una habilidad profesional

### Qué documentar en `uso_de_ia.md`

Por cada uso significativo de IA (no por cada autocompletar trivial), registren una entrada con esta estructura:

| Campo | Ejemplo |
|---|---|
| Entrega | Semana 5 · Clase 1 (antes de la sesión) |
| Integrante | María |
| Herramienta | Claude Code |
| Tarea | Entender por qué `pd.merge` duplicaba filas |
| Prompt resumido | "Tengo dos DataFrames con clave `cliente_id` y al hacer left join obtengo más filas que el izquierdo, ¿por qué?" |
| Salida que aceptamos | Aprendimos que había duplicados en la tabla derecha; agregamos `assert df_join.shape[0] == df_left.shape[0]` |
| Salida que rechazamos / corregimos | Sugirió `drop_duplicates()` ciego sobre toda la tabla derecha, pero perdíamos transacciones legítimas. Lo aplicamos solo sobre la tabla de catálogo. |
| Quién verificó | Carlos validó ejecutando con muestra controlada |

> 🚩 Si la bitácora no existe o es claramente posthoc (todas las entradas con la misma fecha, prompts genéricos), asumimos por defecto que **toda** la entrega fue generada por IA sin revisión humana y se evalúa en consecuencia.

### Buenas prácticas con Antigravity / Claude Code

- Usen los agentes para **tareas acotadas** (limpiar una columna, escribir una función de utilidad, sugerir un gráfico, explicar un error). No para *"haz todo el caso"*.
- **Lean el diff antes de aceptarlo.** Si no entienden una línea, pidan explicación a la IA o al docente; no la aceptan sin entenderla.
- Cuando la IA proponga un método estadístico (test de hipótesis, distancia, escalador), **verifiquen los supuestos** sobre su data antes de aplicarlo. Las IAs confunden supuestos con frecuencia y aplican métodos que no corresponden.
- Comiteen los cambios sustantivos generados por IA en commits separados con prefijo `[ia]:`. Ejemplo: `[ia]: limpieza inicial de columna InvoiceNo (revisada por Juan)`. Esto facilita la revisión y la trazabilidad.
- **No le entreguen datos sensibles** a herramientas externas. Si su caso involucra PII (nombres, cédulas, emails, geolocalización fina), anonimicen antes de pegar muestras en chats web. Para casos con datos públicos esto no aplica, pero acostúmbrense al reflejo.

---

## 📋 Rúbrica del entregable intermedio

| Criterio | Peso | Qué evaluamos |
|---|---|---|
| Estructura del repositorio y disciplina de commits | 15 % | Estructura limpia, `.gitignore` correcto, commits descriptivos repartidos entre integrantes |
| Calidad del entendimiento del negocio (`07_CONTEXTO`) | 20 % | Profundidad de la investigación, calidad del diccionario de variables, hipótesis bien formuladas |
| Plan de preparación de datos | 10 % | Decisiones justificadas, orden lógico, sin pasos "porque sí" |
| Cuaderno de preparación de datos | 15 % | Reproducibilidad, validaciones, claridad de las celdas |
| Cuaderno de EDA + insights finales | 25 % | Profundidad del análisis, calidad de las visualizaciones, **insights accionables** |
| Bitácora de uso de IA | 10 % | Trazabilidad real, verificación humana visible, criticidad ante salidas |
| Datos correctamente versionados o referenciados | 5 % | Sin archivos pesados en el repo, instrucciones de descarga claras |

> Un grupo con código brillante pero sin `07_CONTEXTO` o sin bitácora de IA **no aprueba este punto de control**, aunque su EDA sea espectacular. Aprenden a entregar un proyecto, no solo a programar.

---

## 🚦 Errores comunes (vistos cada semestre)

- **Rutas absolutas** dentro del notebook. *"El cuaderno solo me corre a mí porque tengo el dataset en mi `Downloads/`."* Usen rutas relativas a la raíz del repo (`../00_datos_crudos/...`) o `pathlib` con anclaje al repo.
- **Diccionario de variables construido a ojo** sobre las primeras filas. Verifiquen tipos, nulos y rangos con código antes de redactarlo.
- **Investigación de contexto que es Wikipedia reescrita.** Citen al menos una fuente del sector (informe institucional, paper, reporte de la industria) que no sea Wikipedia ni el enunciado del caso.
- **"Insights" del EDA que son descripciones de gráficas.** *"Vemos que la distribución de X es sesgada a la derecha"* no es un insight, es una observación. Un insight es: *"La distribución sesgada de X implica que la mediana, no la media, es el indicador reportable a la gerencia, y eso cambia la métrica del KPI Y que veníamos calculando."*
- **Bitácora de IA escrita a última hora** con prompts inventados. Llévenla en vivo desde la primera sesión de trabajo, dos minutos por sesión de trabajo.
- **Repos llamados `proyecto`, `final`, `tarea`.** Usen `seminario-grupo-X-caso-YY-segmentacion-retail` o equivalente.
- **Datos de prueba subidos por error**. Antes del primer push: `git status` y revisar que no haya CSVs gigantes en stage. Una vez en el historial, sacarlos es más complicado.

---

## 📅 Fecha y forma de entrega

- **Entrega:** Semana 5 · Clase 1, antes del inicio de la sesión.
- **Cómo entregar:** subir el link del repositorio a la plataforma del curso. El último commit relevante debe ser anterior a la hora de inicio de la clase. Commits posteriores no se evalúan.
- **Defensa breve en clase:** los primeros 30–40 minutos de esa sesión son una revisión rápida en vivo. El docente puede pedirle a **cualquier integrante** del grupo (no solo al "líder") que ejecute un cuaderno o explique un insight. Si todos hicieron commits y entendieron lo entregado, este momento es trivial.

---

## 🔁 Cómo continúa el caso después de este punto

Lo que entreguen en este punto de control no se vuelve a tocar como "tarea cerrada", sino que se vuelve la **base viva** del resto del seminario:

- El cuaderno `02_eda.ipynb` se profundizará en la semana de hipótesis y pruebas estadísticas.
- El plan de preparación se versiona y se ajusta cuando aparecen problemas en modelado.
- El diccionario de variables se actualiza cada vez que se construya una variable nueva.
- La bitácora de IA crece; no se reinicia.

Por eso vale la pena entregar bien este punto: lo que dejen mal armado aquí lo arrastran el resto del seminario.
