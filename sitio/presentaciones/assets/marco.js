/* Marco de presentaciones · navegación, fragmentos, notas del docente.
   Teclas: → ␣ avanzar · ← retroceder · G rejilla · N notas · F pantalla completa · ? ayuda */
(function () {
  "use strict";
  var diapos = Array.prototype.slice.call(document.querySelectorAll(".diapo"));
  if (!diapos.length) return;
  var i = 0;

  // cromo
  var barra = document.createElement("div"); barra.id = "progreso"; document.body.appendChild(barra);
  var cont = document.createElement("div"); cont.id = "contador"; document.body.appendChild(cont);
  var marca = document.createElement("div"); marca.id = "marca";
  marca.textContent = document.body.getAttribute("data-marca") || "ADM 2003 · USFQ";
  document.body.appendChild(marca);
  var notas = document.createElement("div"); notas.id = "notas";
  notas.innerHTML = '<div class="titulo">Notas del docente · tecla N para ocultar</div><div id="notas-texto"></div>';
  document.body.appendChild(notas);
  var ayuda = document.createElement("div"); ayuda.id = "ayuda";
  ayuda.innerHTML = '<div class="caja"><h3>Controles</h3><table>' +
    "<tr><td><kbd>→</kbd> <kbd>espacio</kbd> <kbd>clic</kbd></td><td>avanzar (revela fragmentos)</td></tr>" +
    "<tr><td><kbd>←</kbd></td><td>retroceder</td></tr>" +
    "<tr><td><kbd>G</kbd></td><td>ver todas las láminas</td></tr>" +
    "<tr><td><kbd>N</kbd></td><td>notas del docente</td></tr>" +
    "<tr><td><kbd>F</kbd></td><td>pantalla completa</td></tr>" +
    "<tr><td><kbd>1</kbd>…<kbd>9</kbd></td><td>ir a la lámina</td></tr>" +
    "<tr><td><kbd>?</kbd> <kbd>Esc</kbd></td><td>abrir y cerrar esta ayuda</td></tr>" +
    "</table></div>";
  document.body.appendChild(ayuda);

  var acento = document.body.getAttribute("data-acento");
  if (acento) document.documentElement.style.setProperty("--acento", acento);

  function frags(d) { return Array.prototype.slice.call(d.querySelectorAll(".frag")); }

  function pinta() {
    diapos.forEach(function (d, k) { d.classList.toggle("activa", k === i); });
    barra.style.width = ((i + 1) / diapos.length) * 100 + "%";
    cont.textContent = (i + 1) + " / " + diapos.length;
    var t = diapos[i].getAttribute("data-notas") || "Sin notas para esta lámina.";
    document.getElementById("notas-texto").textContent = t;
    if (location.hash !== "#" + (i + 1)) history.replaceState(null, "", "#" + (i + 1));
  }

  function avanza() {
    var f = frags(diapos[i]).filter(function (x) { return !x.classList.contains("visible"); });
    if (f.length) { f[0].classList.add("visible"); return; }
    if (i < diapos.length - 1) { i++; pinta(); }
  }
  function retrocede() {
    var f = frags(diapos[i]).filter(function (x) { return x.classList.contains("visible"); });
    if (f.length) { f[f.length - 1].classList.remove("visible"); return; }
    if (i > 0) { i--; frags(diapos[i]).forEach(function (x) { x.classList.add("visible"); }); pinta(); }
  }
  function irA(k) { i = Math.max(0, Math.min(diapos.length - 1, k)); pinta(); }

  document.addEventListener("keydown", function (ev) {
    if (ev.target.tagName === "INPUT" || ev.target.tagName === "TEXTAREA") return;
    var k = ev.key;
    if (k === "ArrowRight" || k === " " || k === "PageDown") { ev.preventDefault(); avanza(); }
    else if (k === "ArrowLeft" || k === "PageUp") { ev.preventDefault(); retrocede(); }
    else if (k === "Home") irA(0);
    else if (k === "End") irA(diapos.length - 1);
    else if (k === "g" || k === "G") document.body.classList.toggle("rejilla");
    else if (k === "n" || k === "N") notas.classList.toggle("visible");
    else if (k === "f" || k === "F") {
      if (document.fullscreenElement) document.exitFullscreen();
      else document.documentElement.requestFullscreen();
    }
    else if (k === "?") ayuda.classList.toggle("visible");
    else if (k === "Escape") { ayuda.classList.remove("visible"); document.body.classList.remove("rejilla"); }
    else if (/^[1-9]$/.test(k)) irA(parseInt(k, 10) - 1);
  });

  document.addEventListener("click", function (ev) {
    if (ayuda.classList.contains("visible")) { ayuda.classList.remove("visible"); return; }
    if (document.body.classList.contains("rejilla")) {
      var d = ev.target.closest(".diapo");
      if (d) { document.body.classList.remove("rejilla"); irA(diapos.indexOf(d)); }
      return;
    }
    if (ev.target.closest("a, button, input, iframe")) return;
    avanza();
  });

  var h = parseInt((location.hash || "").replace("#", ""), 10);
  if (h && h >= 1 && h <= diapos.length) i = h - 1;
  pinta();
})();
