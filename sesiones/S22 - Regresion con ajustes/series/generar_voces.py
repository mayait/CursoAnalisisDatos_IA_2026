# -*- coding: utf-8 -*-
"""Genera el audio del guion en pocos pedidos: cada bloque junta muchas frases y luego se corta por sus silencios.

El plan gratuito de Gemini da pocos pedidos diarios, por eso no se pide frase por frase.
Lo ya generado no se vuelve a pedir. Uso: python generar_voces.py
"""
import base64
import http.client
import io
import json
import time
import urllib.error
import urllib.request
import wave

import numpy as np

import guion
import voces

GRUPOS_NARRADOR = [["E01"], ["E02", "E03"], ["E04"], ["E05", "E06"], ["E07", "E08"], ["E09", "E10"], ["E02A"], ["E02B", "E02C"], ["E02D", "E02E"], ["E02F"]]


def bloques():
    for g in GRUPOS_NARRADOR:
        vistos, ts = set(), []
        for e in guion.EPISODIOS:
            if e["id"] in g:
                for t in e["tomas"]:
                    for b in t["beats"]:
                        if b["voz"] == "narrador" and b["texto"] not in vistos:
                            vistos.add(b["texto"]); ts.append(b["texto"])
        yield "narrador", ts
    for voz in ("daniela", "agencia"):
        vistos, ts = set(), []
        for b in guion.todos_los_beats():
            if b["voz"] == voz and b["texto"] not in vistos:
                vistos.add(b["texto"]); ts.append(b["texto"])
        yield voz, ts


def pedir(voz, textos):
    cuerpo = json.dumps({"contents": [{"parts": [{"text": "\n\n".join(textos)}]}],
                         "generationConfig": {"responseModalities": ["AUDIO"], "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": voces.VOCES[voz]}}}}}).encode()
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{voces.MODELO}:generateContent"
    for intento in range(5):
        req = urllib.request.Request(url, data=cuerpo, headers={"x-goog-api-key": voces.clave(), "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=400) as r:
                d = json.load(r)
            p = d["candidates"][0]["content"]["parts"][0]["inlineData"]
            crudo = base64.b64decode(p["data"])
            if crudo[:4] == b"RIFF":
                with wave.open(io.BytesIO(crudo)) as w:
                    return np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16), w.getframerate()
            return np.frombuffer(crudo, dtype=np.int16), int(p["mimeType"].split("rate=")[1].split(";")[0])
        except urllib.error.HTTPError as e:
            cuerpo_err = e.read()[:400].decode(errors="replace")
            if e.code == 429 and "per day" in cuerpo_err.lower():
                raise SystemExit("CUOTA DIARIA AGOTADA: " + cuerpo_err)
            print("  reintento", e.code, flush=True)
            time.sleep(25 * (intento + 1))
        except (urllib.error.URLError, http.client.HTTPException, TimeoutError, ConnectionError, KeyError):
            print("  reintento por conexión", flush=True)
            time.sleep(25 * (intento + 1))
    raise SystemExit("No se pudo generar el bloque")


def silencios(x, rate):
    v = int(0.02 * rate)
    e = np.array([np.abs(x[i:i + v]).mean() for i in range(0, len(x) - v, v)])
    th = max(60, np.percentile(e, 95) * 0.035)
    res, i = [], 0
    while i < len(e):
        if e[i] < th:
            j = i
            while j < len(e) and e[j] < th:
                j += 1
            if (j - i) * 0.02 >= 0.16:
                res.append(((i + j) / 2 * 0.02, (j - i) * 0.02))
            i = j
        else:
            i += 1
    return res


def partir(x, rate, textos):
    """Elige n-1 silencios: los que caen cerca del punto esperado por largo de texto y que además son largos."""
    sil = silencios(x, rate)
    total = len(x) / rate
    largos = np.array([len(t) + 12 for t in textos], float)
    esperado = np.cumsum(largos)[:-1] / largos.sum() * total
    n, m = len(esperado), len(sil)
    if m < n:
        raise SystemExit("Hay menos silencios que frases")
    INF = 1e18
    costo = np.full((n, m), INF)
    prev = np.zeros((n, m), int)
    pena = lambda i, j: ((sil[j][0] - esperado[i]) / 2.2) ** 2 - 2.5 * min(sil[j][1], 1.2)
    for j in range(m):
        costo[0, j] = pena(0, j)
    for i in range(1, n):
        mejor, arg = INF, -1
        for j in range(i, m):
            if costo[i - 1, j - 1] < mejor:
                mejor, arg = costo[i - 1, j - 1], j - 1
            costo[i, j], prev[i, j] = mejor + pena(i, j), arg
    j = int(np.argmin(costo[n - 1]))
    cortes = [0] * n
    for i in range(n - 1, -1, -1):
        cortes[i] = j
        j = prev[i, j]
    t = [0.0] + [sil[c][0] for c in cortes] + [total]
    return [x[int(t[i] * rate):int(t[i + 1] * rate)] for i in range(len(textos))]


if __name__ == "__main__":
    for voz, textos in bloques():
        faltan = [t for t in textos if not voces.destino(voz, t).exists()]
        if not faltan:
            print(voz, "bloque listo", flush=True)
            continue
        x, rate = pedir(voz, textos)
        voces.AUDIO.mkdir(exist_ok=True)
        (voces.AUDIO / "bloques").mkdir(exist_ok=True)
        nombre = voces.destino(voz, "|".join(textos)).name
        with wave.open(str(voces.AUDIO / "bloques" / nombre), "wb") as w:
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(rate); w.writeframes(x.tobytes())
        trozos = partir(x, rate, textos)
        vel = []
        for t, tr in zip(textos, trozos):
            y = voces.recortar(tr, rate)
            vel.append(len(t) / (len(y) / rate))
            with wave.open(str(voces.destino(voz, t)), "wb") as w:
                w.setnchannels(1); w.setsampwidth(2); w.setframerate(rate); w.writeframes(y.tobytes())
        print(voz, len(textos), "frases", round(len(x) / rate / 60, 1), "min, caracteres por segundo", round(min(vel), 1), "a", round(max(vel), 1), flush=True)
        time.sleep(24)
    print("FIN", flush=True)
