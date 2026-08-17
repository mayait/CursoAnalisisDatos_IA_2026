# Plantilla · notas_profesor.md

Guion para dictar la sesión. Le habla al docente, en imperativo, con minutos reales.
No repite el contenido de `clase.md`: dice **cómo** se dicta y **qué sale mal**.

```markdown
# Semana {X} · Clase {Y} — {Tema} · Notas del profesor

**Duración:** 2h30 sincrónicas (150 min)

---

## Antes de empezar (15 min antes)

{Qué abrir y en qué orden. Qué revisar de la clase pasada: quién quedó en riesgo, qué
equipos tienen problemas. Si hay que tener un plan B listo, dilo aquí.}

**Energía interna:** {Cómo se siente hoy la clase y qué priorizar. Ej: "hoy hacen las
primeras líneas de código; es el día más importante del curso para la motivación. Si alguien
sale pensando que Python no es para él, es muy difícil recuperarlo después".}

---

## Arco general del día

{Qué se cubre y por qué en ese orden.}

**La trampa de hoy:** {El error de dictado, no el del estudiante. Ej: pasar por encima
porque "es básico"; querer cubrir demasiado.}

Objetivo al cierre:
- {Estado observable, no objetivo de aprendizaje. "Todos han ejecutado Python en su máquina,
  no solo leído".}
- {...}

---

## Minuto a minuto

### 0–10 min · Apertura y conexión con la clase pasada

{Frase textual de apertura, entre comillas y en blockquote. Preguntas rápidas al grupo y qué
hacer según la respuesta.}

### 10–15 min · {Bloque}

{Instrucciones. Errores comunes con su mensaje literal y la solución:}

Errores comunes:
- `{Mensaje de error textual}` → {Qué responder y qué hacer}

### 15–45 min · {Bloque} (live coding)

{Qué se escribe en vivo y qué se lee del cuaderno. Cuándo compartir pantalla.}

### {…} min · {Bloque}

### 140–150 min · Cierre

{Qué se deja tarea, qué se sube, con qué frase se cierra.}

---

## Si vas tarde

{Qué recortar, en orden de sacrificio. Siempre hay algo que se puede dejar para casa.}

## Alertas para la próxima clase

{Qué anotar hoy sobre estudiantes o equipos en riesgo.}
```

## Reglas

- Los tramos horarios suman 150 minutos. Si no suman, el guion está mal.
- **Se programa frente a ellos.** Cuando hay código nuevo, la nota indica live coding y no
  lectura de celdas ya escritas.
- Cada error frecuente aparece con su mensaje textual de Python. Es lo que el docente va a
  ver en el chat.
- Mejor profundo y lento que rápido y confuso: si sobra contenido, el guion dice qué se cae.
