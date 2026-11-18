# -*- coding: utf-8 -*-
"""Síntesis de voz con Gemini. La clave se lee del .env de la raíz y va en cabecera: nunca se imprime ni va en la URL."""
import base64
import hashlib
import io
import json
import sys
import time
import urllib.error
import urllib.request
import wave
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import numpy as np

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[2]
MODELO = "gemini-2.5-flash-preview-tts"  # el 3.8 solo da 10 pedidos diarios en el plan gratuito
AUDIO = AQUI / "audio"
VOCES = {"narrador": "Charon", "daniela": "Aoede", "agencia": "Puck"}
# Este modelo lee en voz alta cualquier instrucción de estilo escrita en prosa y no acepta instrucción de sistema. Solo se usan etiquetas de audio.
ETIQUETA = {"narrador": "", "daniela": "", "agencia": ""}


def clave():
    for l in (RAIZ / ".env").read_text().splitlines():
        if l.startswith("GEMINI_API_KEY="):
            return l.split("=", 1)[1].strip().strip("\"'")
    sys.exit("Falta GEMINI_API_KEY en .env")


def destino(voz, texto):
    return AUDIO / f"{voz}-{hashlib.sha1((MODELO + voz + texto).encode()).hexdigest()[:14]}.wav"


def recortar(x, rate):
    """Quita silencios del inicio y del final para que el ritmo lo marque el guion."""
    th = max(200, np.abs(x).max() * 0.02)
    i = np.where(np.abs(x) > th)[0]
    if len(i) == 0:
        raise ValueError("audio sin voz")
    a, b = max(0, i[0] - int(0.02 * rate)), min(len(x), i[-1] + int(0.08 * rate))
    return x[a:b]


def sintetizar(voz, texto, key):
    d = destino(voz, texto)
    if d.exists():
        return d
    cuerpo = json.dumps({"contents": [{"parts": [{"text": f"{ETIQUETA[voz]}{texto}"}]}],
                         "generationConfig": {"responseModalities": ["AUDIO"], "speechConfig": {"voiceConfig": {"prebuiltVoiceConfig": {"voiceName": VOCES[voz]}}}}}).encode()
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{MODELO}:generateContent"
    for intento in range(8):
        req = urllib.request.Request(url, data=cuerpo, headers={"x-goog-api-key": key, "Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                datos = json.load(r)
            p = datos["candidates"][0]["content"]["parts"][0]["inlineData"]
            crudo = base64.b64decode(p["data"])
            if crudo[:4] == b"RIFF":
                with wave.open(io.BytesIO(crudo)) as w0:
                    rate = w0.getframerate()
                    x = np.frombuffer(w0.readframes(w0.getnframes()), dtype=np.int16)
                    if w0.getnchannels() == 2:
                        x = x[::2]
            else:
                rate = int(p["mimeType"].split("rate=")[1].split(";")[0])
                x = np.frombuffer(crudo, dtype=np.int16)
            x = recortar(x, rate)
            with wave.open(str(d), "wb") as w:
                w.setnchannels(1); w.setsampwidth(2); w.setframerate(rate); w.writeframes(x.tobytes())
            return d
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504):
                time.sleep(min(60, 6 * (intento + 1)))
                continue
            raise SystemExit(f"Error {e.code} de Gemini: {e.read()[:300].decode(errors='replace')}")
        except (KeyError, ValueError, TimeoutError, urllib.error.URLError):
            time.sleep(5 * (intento + 1))
    raise SystemExit(f"No se pudo sintetizar: {texto[:50]}")


def duracion(p):
    with wave.open(str(p)) as w:
        return w.getnframes() / w.getframerate()


def sintetizar_todo(pares, hilos=4):
    key = clave()
    AUDIO.mkdir(exist_ok=True)
    with ThreadPoolExecutor(hilos) as ex:
        return list(ex.map(lambda p: sintetizar(p[0], p[1], key), pares))


def transcribir(ruta):
    """Devuelve lo que Gemini oye en un audio, para comparar con el guion."""
    b = base64.b64encode(Path(ruta).read_bytes()).decode()
    cuerpo = json.dumps({"contents": [{"parts": [{"inlineData": {"mimeType": "audio/wav", "data": b}}, {"text": "Transcribe este audio palabra por palabra y luego, en una línea que empiece con ACENTO:, di el idioma y el acento."}]}]}).encode()
    req = urllib.request.Request("https://generativelanguage.googleapis.com/v1beta/models/gemini-3.8-flash:generateContent", data=cuerpo, headers={"x-goog-api-key": clave(), "Content-Type": "application/json"})
    for intento in range(6):
        try:
            with urllib.request.urlopen(urllib.request.Request(req.full_url, data=cuerpo, headers=dict(req.header_items())), timeout=180) as r:
                return json.load(r)["candidates"][0]["content"]["parts"][0]["text"]
        except urllib.error.HTTPError as e:
            if e.code not in (429, 500, 502, 503, 504):
                raise
            time.sleep(8 * (intento + 1))
    return ""
