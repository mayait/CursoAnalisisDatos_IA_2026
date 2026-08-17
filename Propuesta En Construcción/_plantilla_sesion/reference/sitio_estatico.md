# Plantilla · index.html de una sesión

Página del sitio estático, tema tipo ReadTheDocs. Se genera a partir de `clase.md`: mismo
texto, convertido a HTML, envuelto en este esqueleto. El CSS completo está en
`assets/estilos_sesion.css` — pégalo dentro de `<style>` (el sitio no usa hoja externa: cada
página es autocontenida).

Paleta: `--blue #2980b9` · `--navy #232936` · `--sidebar-bg #f8f8f8`. Tipografía Lato desde
Google Fonts, resaltado de código con highlight.js 11.9.0 (tema github).

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Semana {X} · Clase {Y} — {Tema} — {Nombre del curso}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github.min.css">
  <style>
  /* … contenido de assets/estilos_sesion.css … */
  </style>
</head>
<body>
  <header id="topbar">
    <div class="topbar-left">
      <button id="menu-toggle" onclick="document.getElementById('sidebar').classList.toggle('open')" aria-label="Menú">&#9776;</button>
      <a href="index.html" class="brand">🐍 {Curso} <span class="sep">·</span> <span class="sub">{Subtítulo}</span></a>
    </div>
    <div class="topbar-right"><span class="week-chip">Semana {X} · Clase {Y}</span></div>
  </header>

  <div id="layout">
    <nav id="sidebar">
      <div class="sb-header">Contenidos</div>
      <a href="../index.html" class="sb-index-link">📋 Índice del curso</a>

      <!-- un bloque por semana, TODAS las semanas en TODAS las páginas -->
      <div class="sb-week">
        <div class="sb-week-hdr">
          <span class="sb-week-label">Semana {X}</span>
          <span class="sb-week-sub">{Tema de la semana}</span>
        </div>
        <ul>
          <li class="sb-item"><a href="../{Carpeta%20URL}/index.html"><span class="dnum">C1</span><span class="dtitle">{Título corto}</span></a></li>
          <li class="sb-item active"><a href="./index.html"><span class="dnum">C2</span><span class="dtitle">{Título corto}</span><span class="sb-badge">E2</span></a></li>
        </ul>
      </div>
      <!-- … -->
    </nav>

    <main id="main">
      <div class="content-wrap">
        <div class="breadcrumb">
          <a href="../index.html">{Curso}</a><span class="sep">›</span>
          <a href="../index.html#sesiones">Semana {X}</a><span class="sep">›</span>
          <span>Clase {Y} · {Tema}</span>
        </div>

        <div class="action-bar">
          <span class="action-label">Notebook:</span>
          <a href="https://colab.research.google.com/github/{repo}/blob/main/{Carpeta%20URL}/clase_{NN}.ipynb" target="_blank"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"></a>
          <a href="https://nbviewer.org/github/{repo}/blob/main/{Carpeta%20URL}/clase_{NN}.ipynb" target="_blank"><img src="https://raw.githubusercontent.com/jupyter/design/master/logos/Badges/nbviewer_badge.svg" alt="nbviewer"></a>
          <a href="https://github.com/{repo}/blob/main/{Carpeta%20URL}/clase_{NN}.ipynb" target="_blank" style="color:#2980b9;font-size:.8rem">Ver en GitHub ↗</a>
        </div>

        <h1>Semana {X} · Clase {Y} — {Tema}</h1>
        <p><strong>Sesión:</strong> Semana {X} · Clase {Y} · sesión {N} de {M}<br>
           <strong>Módulo:</strong> {Módulo}<br>
           <strong>Duración:</strong> 2 horas 30 minutos sincrónicas</p>
        <hr>

        <!-- cuerpo de clase.md convertido a HTML -->

        <hr>
        <p><a href="../{Carpeta%20anterior}/">← Sesión {N-1}</a> · <a href="../README.md">🏠 Índice</a> · <a href="../{Carpeta%20siguiente}/">Sesión {N+1} →</a></p>
        <blockquote><p><em>{Curso} · {Año}</em></p></blockquote>

        <nav class="page-nav">
          <a href="../{Carpeta%20anterior}/index.html" class="pn-btn prev"><span class="pn-label">Anterior</span><span class="pn-title">S{X}·C{Y-1} · {Título corto}</span></a>
          <a href="../{Carpeta%20siguiente}/index.html" class="pn-btn next"><span class="pn-label">Siguiente</span><span class="pn-title">S{X}·C{Y+1} · {Título corto}</span></a>
        </nav>
      </div>
    </main>
  </div>

  <footer id="footer">
    <span>{Nombre completo del curso} </span>
    <span><a href="https://github.com/{repo}" target="_blank">github.com/{repo}</a></span>
  </footer>

  <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
  <script>
    document.addEventListener('DOMContentLoaded', function () {
      document.querySelectorAll('pre code').forEach(function (block) { hljs.highlightElement(block); });
      document.getElementById('main').addEventListener('click', function () {
        document.getElementById('sidebar').classList.remove('open');
      });
    });
  </script>
</body>
</html>
```

## Reglas

- **La sidebar lista el curso entero en todas las páginas.** Al añadir una sesión hay que
  tocar la sidebar de todas las demás. Hazlo con un script, no a mano.
- **Una sola `li.sb-item.active`** por página: la sesión actual, enlazada a `./index.html`.
- `sb-badge` marca entregas: `E1`, `E2`, `E3`, `FINAL`.
- Los espacios de carpeta van `%20` en todos los `href`.
- Elementos de apoyo dentro del cuerpo: `<span class="pill green|orange">` para veredictos en
  tablas comparativas, `<iframe>` para videos de YouTube.
- Los simuladores viven en `simuladores/simulador-{slug}.html` y se enlazan con
  `target="_blank"`.
