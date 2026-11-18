# Subir a D2L · Semana 12

No pude subirlo yo: la pestaña de D2L del navegador de Orca quedó en la pantalla de inicio de sesión de Microsoft y Chrome no acepta control externo. Quedan dos caminos.

## A mano (tres minutos)

1. D2L, curso ADM 2003, Contenido. Crea el módulo **Semana 12** si no existe.
2. Sube al módulo, como archivos, `semana12-la-fria-cuesta-mas.html` y `caso-la-fria-cuesta-mas.pdf`. Los dos en el mismo módulo: la página enlaza el PDF por nombre.
3. Agrega un enlace externo «Simulador La fría cuesta más» hacia https://regresion-simuladores.iahumana.org/login/ que abra en ventana nueva.
4. Publica cuando quieras que lo vean. La página no revela respuestas, así que no necesita fecha de disponibilidad.

## Prompt para el agente del navegador (Chrome con tu sesión de D2L)

```
En D2L (miusfv.usfq.edu.ec, org unit 331555) crea el módulo de contenido «Semana 12» si no existe, después del de la Semana 11, y déjalo oculto (IsHidden true). Usa fetch a /d2l/api/le/1.75/331555/content/ con el header X-Csrf-Token tomado de localStorage.getItem('XSRF.Token').
Dentro del módulo sube dos temas como archivo, con POST multipart/mixed a content/modules/ID/structure/ (parte JSON con Type 1, TopicType 1 y Url /content/enforced/331555-202610-2241/NOMBRE, y una parte con el archivo):
1. «La fría cuesta más: el simulador y la ronda 1» con el archivo semana12-la-fria-cuesta-mas.html
2. «Caso La fría cuesta más (PDF)» con el archivo caso-la-fria-cuesta-mas.pdf
Los archivos están en la carpeta sesiones/S24 - La fria cuesta mas/d2l/ del repositorio del curso. Conserva los nombres exactos: la página enlaza el PDF por nombre relativo.
Agrega un tercer tema de tipo enlace (TopicType 3) titulado «Abrir el simulador» con la URL https://regresion-simuladores.iahumana.org/login/ y que abra en ventana nueva.
Verifica comparando el tamaño del HTML servido sin las etiquetas script que inyecta D2L. No publiques ni borres nada: deja todo oculto y dime los IDs creados.
```
