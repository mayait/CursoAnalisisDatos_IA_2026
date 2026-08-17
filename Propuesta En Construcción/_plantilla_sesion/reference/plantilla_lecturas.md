# Plantilla · Lecturas.md y carpeta lecturas/

Curaduría en español, comentada. Nunca un listado de enlaces pelados: cada entrada dice
**por qué** vale la pena.

```markdown
# Lecturas adicionales · Semana {X} · Clase {Y} · {Tema}

Curaduría de material en español para profundizar después de la clase. Las copias locales están en la subcarpeta `lecturas/` cuando la fuente lo permite.

## Artículos técnicos

1. **[{Título}]({url})** — {Autor} ({dominio})
   *Por qué leerlo:* {Una frase. Qué aporta que no esté en la clase.}

2. **[{Título}]({url})** — {Autor} ({dominio})
   *Por qué leerlo:* {...}

## Artículos de negocios y aplicación

1. **[{Título}]({url})** — {Fuente}
   *Por qué leerlo:* {Cómo se usa esto en una empresa de verdad.}

2. **[{Título}]({url})** — {Fuente}
   *Por qué leerlo:* {...}

## Video recomendado

- **[{Título}]({url})** — {Canal}
  *Por qué verlo:* {Qué muestra que el texto no puede.}
  *Incrustado en el cuaderno `clase_{NN}.ipynb`.*
```

## Reglas

- Mínimo dos técnicas, dos de negocio y un video. El equilibrio técnico/negocio es lo que
  distingue este curso de un tutorial de programación.
- Prioriza fuentes en español. Si la mejor fuente está en inglés (IBM, documentación oficial),
  úsala pero dilo en el comentario.
- El video de la lista es el mismo que se incrusta en la celda `📺` del cuaderno.

## Carpeta `lecturas/`

Copia local en Markdown de cada artículo, para que el material sobreviva a los enlaces rotos.
Nomenclatura:

```
lecturas/
├── tecnico-1-{slug-del-titulo}.md
├── tecnico-2-{slug-del-titulo}.md
├── negocios-1-{slug-del-titulo}.md
└── negocios-2-{slug-del-titulo}.md
```

El slug va en minúsculas, con tildes conservadas y guiones en lugar de espacios. Cada copia
abre con el título, la fuente y la URL original.
