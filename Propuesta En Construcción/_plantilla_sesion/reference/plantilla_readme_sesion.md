# Plantilla · README.md y clase.md de una sesión

`clase.md` es el cuerpo. `README.md` es el mismo cuerpo con la cabecera de navegación (líneas 1-5) y el pie (últimas 5 líneas). Sustituye lo que va entre `{}`.

---

## Cabecera de `README.md` (no va en `clase.md`)

```markdown
[← S{X-1}·C{Y} · {Tema anterior}](../{Carpeta%20anterior}/) · [🏠 Índice](../README.md) · [S{X}·C{Y+1} · {Tema siguiente} →](../{Carpeta%20siguiente}/)

<a href="https://colab.research.google.com/github/{repo}/blob/main/{Carpeta%20URL}/clase_{NN}.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>  &nbsp; [![nbviewer](https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg)](https://nbviewer.org/github/{repo}/blob/main/{Carpeta%20URL}/clase_{NN}.ipynb)

---
```

Los espacios de la carpeta van como `%20`. Las tildes no se escapan.

---

## Cuerpo (`clase.md` completo)

```markdown
# Semana {X} · Clase {Y} — {Tema}

**Sesión:** Semana {X} · Clase {Y} · sesión {N} de {M}
**Módulo:** Módulo {k} · {Nombre del módulo}
**Duración:** 2 horas 30 minutos sincrónicas

---

## Introducción

{Dos a cuatro frases. Conecta con la sesión anterior, dice qué se desbloquea hoy y por qué
importa fuera del aula. Sin listar el temario: eso viene abajo.}

## Objetivos de aprendizaje

Al terminar la sesión podrás:

- {Verbo en infinitivo + objeto concreto + herramienta. "Auditar un dataset nuevo con
  `.shape`, `.info()`, `.describe()` y `.isnull()`."}
- {Entre tres y cinco. Si son más, la sesión está sobrecargada.}

## Contenidos de la sesión

### 1. {Bloque}

{Explicación breve. Si hay sintaxis, va en línea con backticks o en bloque de código.}

### 2. {Bloque}

{...}

## Actividad práctica

En `clase_{NN}.ipynb`:

1. {Paso verificable}
2. {Paso verificable}
3. {Paso verificable}

## Trabajo en grupo sobre el caso asignado

En su dataset del caso:

- {Qué produce el equipo hoy, en términos del proyecto, no del tema}
- {Qué queda documentado por escrito}

## Entregable del día

{Archivo concreto y dónde se sube. Ej: Notebook `clase_06.ipynb` ejecutado + ficha de
exploración en `docs/ficha_dataset.md`.}

## Recursos recomendados

- {Título}: {URL}
- {Título}: {URL}
```

---

## Pie de `README.md` (no va en `clase.md`)

```markdown
---

[← Sesión {N-1}](../{Carpeta%20anterior}/) · [🏠 Índice](../README.md) · [Sesión {N+1} →](../{Carpeta%20siguiente}/)

> *Seminario EDA · [we-human-centric](https://github.com/we-human-centric)*
```

---

## Variante extendida (sesiones técnicas densas)

Las sesiones de modelado usan una versión más larga: numeración `## 1.` … `## 8.`, subsecciones `### 3.1`, y estos marcadores como encabezados `####` propios:

```markdown
#### 📌 Idea central
{Una o dos frases. Lo que hay que recordar si se olvida todo lo demás.}

#### 💡 Intuición visual
{Descripción de la figura o enlace al simulador HTML correspondiente.}

#### ⚠️ {La trampa}
{El error que la gente comete y por qué es caro.}

#### 🎯 Lectura de los coeficientes
{Cómo se traduce la salida del modelo a lenguaje de negocio.}
```

Los simuladores se enlazan así:

```markdown
### {n}.{m} Simulador interactivo — {Nombre}

<a href="../simuladores/simulador-{slug}.html" target="_blank">Abrir simulador ↗</a>
```

Las tablas comparativas de modelos usan píldoras de color:

```markdown
| Modelo | R² train | R² CV (test) | Interpretación |
| ------ | -------- | ------------ | -------------- |
| Lineal (d=1) | 0.612 | 0.594 | Subajuste leve, robusto |
| Grado 10 | 0.643 | **−0.12** | <span class="pill orange">Overfit puro</span> |
```

Cierre obligatorio de las sesiones extendidas:

```markdown
## {n}. Cierre y entregable parcial

### {n}.1 Lo que llevamos a la siguiente clase
### {n}.2 Entregable parcial E{k} (avance — la entrega completa es en Semana {X} · Clase {Y})
### {n}.3 Lecturas de cierre
```
