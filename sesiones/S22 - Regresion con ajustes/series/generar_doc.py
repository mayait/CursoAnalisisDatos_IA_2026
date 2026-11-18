# -*- coding: utf-8 -*-
"""Escribe guion_serie.md a partir de guion.py: organización de la serie y narración completa."""
from pathlib import Path

import guion

VOZ = {"narrador": "Narrador", "daniela": "Daniela", "agencia": "Agencia"}
TIPO = {"portada": "Portada", "ilus": "Ilustración", "apuesta": "Apuesta y revelación", "clip": "Animación", "mapa": "Mapa de errores", "ejercicio": "Ejercicio guiado", "escalera": "Barras de error", "antesdespues": "Mapa antes y después",
        "radiotv": "Línea que se dibuja", "promesacorr": "Contador y utilidad", "grados": "Curvas por grado", "mercado": "Pronóstico por mercado", "freno": "Ecuación y perilla", "escala": "Tarjetas de escala", "rejilla": "Columnas vivas por α",
        "final": "Comparación final", "raiz": "Curvas de saturación", "co2": "Rangos de coeficientes", "guia": "Guía de síntomas", "cierre": "Cierre", "separar": "Separar los grupos", "lineas": "Líneas desde una ecuación", "factor": "Álgebra animada", "pendiente": "Recta que gira", "superficie": "Superficie en 3D", "ejco2": "Ejemplo real", "ejsuper": "Ejemplo real", "ejtitanic": "Ejemplo real", "ejprensa": "Ejemplo real", "python": "Código en pantalla", "trampas": "Errores comunes", "traintest": "Entrenar y probar"}
L = ["# Una recta no se dobla · guion de la serie", "", "Diez episodios y seis sub-videos de interacciones que cuentan la clase de regresión con ajustes. Daniela, la agencia y un narrador llevan la historia. Los episodios 3, 8 y la última parte del 9 son ejercicios: dicen qué hacer y no dan las respuestas. Los episodios que revelan resultados van después del ejercicio correspondiente.", "", "| Episodio | Título | Cuándo verlo |", "|---|---|---|"]
for e in guion.EPISODIOS:
    L.append(f"| {e['id'][1:].replace('A', '.1').replace('B', '.2').replace('C', '.3').replace('D', '.4').replace('E', '.5').replace('F', '.6')} | {e['titulo']} | {e['cuando']} |")
L.append("")
for e in guion.EPISODIOS:
    L += [f"## {e['id'][1:].replace('A', '.1').replace('B', '.2').replace('C', '.3').replace('D', '.4').replace('E', '.5').replace('F', '.6')}. {e['titulo']}", "", f"*{e['cuando']}*", ""]
    for t in e["tomas"]:
        nombre = t.get("titulo") or t.get("nombre") or t.get("img") or ""
        L += [f"### {TIPO[t['tipo']]}" + (f" · {nombre}" if nombre else ""), ""]
        for b in t["beats"]:
            L.append(f"**{VOZ[b['voz']]}.** {b['texto']}" + (f" *(pausa de {b['pausa']} segundos)*" if b.get("pausa") else ""))
            L.append("")
Path(__file__).with_name("guion_serie.md").write_text("\n".join(L), encoding="utf-8")
print(len(L), "líneas")
