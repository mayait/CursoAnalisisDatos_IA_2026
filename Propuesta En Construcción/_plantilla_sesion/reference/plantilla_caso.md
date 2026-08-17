# Plantilla · casos/Caso_NN_{Nombre}.md

Los casos sostienen el proyecto grupal: cada equipo toma uno y lo arrastra por todo el curso.
Un caso no es un enunciado de ejercicio, es un encargo de empresa.

```markdown
# Caso {N} · {Título en clave de negocio}
### {Nombre del curso}
**Riesgo de complejidad:** {🟢 Bajo | 🟡 Medio | 🔴 Alto} · **Técnica principal:** {Técnica} · **Dominio:** {Dominio}

---

## 🏢 Antecedentes

{Dos o tres párrafos. Quién es la empresa, qué datos tiene, qué decisión no puede tomar hoy.
Menciona explícitamente las trampas del dataset: devoluciones marcadas con 'C', clientes sin
identificar, formatos multinivel de Excel. El estudiante debe toparse con ellas advertido.}

---

## 🎯 Objetivo

{Una frase larga: qué se construye, con qué técnica y para quién.}

---

## 📚 Actividades para el estudiante

**Resultado de aprendizaje:** {qué sabe hacer el estudiante al terminar el caso}

### Fase 1 – Comprensión del dominio
{Investigar el negocio y formular hipótesis ANTES de abrir los datos. Qué decisiones cambian
según el resultado.}

### Fase 2 – Preparación y exploración de datos
{Los problemas concretos de calidad que hay que resolver, en lista. Exigir justificación
escrita de cada decisión de limpieza.}

### Fase 3 – Modelado
{Qué modelos, con qué criterio se elige entre ellos, qué se documenta. Siempre ≥ 2 modelos
comparados con métricas apropiadas.}

### Fase 4 – Producto analítico

**Pipeline técnico:**
- {Paso}
- {Paso}

**API (FastAPI):**
- `GET /{ruta}` — {qué devuelve}
- `POST /{ruta}` — {qué recibe y qué devuelve}

**Dashboard (Streamlit):**
1. {Componente visual}
2. {Componente visual}
3. {Formulario donde el gerente obtiene una respuesta en tiempo real}

### Fase 5 – Comunicación
{Qué se defiende ante el tribunal y en cuántos minutos.}

---

## 📦 Dataset

**{Nombre}** — {url}
{Tamaño, formato, particularidades. Si hay que solicitarlo a una institución, dilo aquí con
el plazo estimado.}

---

## 📖 Lecturas recomendadas

- [{Título}]({url}) — {por qué}
```

## Reglas

- **El reto técnico del caso está declarado en el índice.** `casos/00_Indice_Casos.md`
  mantiene la tabla con dominio, técnica principal, reto específico y tamaño del dataset.
  Cada caso nuevo se agrega ahí.
- **Los casos se diferencian por el reto, no por el tema.** Uno tiene desbalance extremo,
  otro un join de ocho tablas, otro strings monetarios que hay que parsear. Dos casos con el
  mismo reto son el mismo caso.
- **Riesgo de complejidad honesto.** Si el dataset pesa 3 GB o hay que pedirlo a una
  institución, es 🔴 y se advierte.
- **Todo caso termina en producto**: API + dashboard, no un cuaderno con gráficos.
