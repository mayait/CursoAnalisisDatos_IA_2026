# -*- coding: utf-8 -*-
"""Corta cada bloque de voz en sus frases alineando el guion con lo que el reconocimiento de voz local oye palabra por palabra.

Uso: python alinear.py carpeta_modelo  -> reescribe audio/*.wav y deja audio/control.json con la coincidencia de cada frase.
"""
import difflib
import json
import os
import re
import sys
import unicodedata
import wave
from pathlib import Path

import numpy as np
from faster_whisper import WhisperModel
from scipy.signal import resample_poly

import generar_voces as gv
import voces

CTRL = voces.AUDIO / "control.json"


def norm(p):
    p = unicodedata.normalize("NFD", p.lower())
    return re.sub(r"[^a-z0-9ñ]", "", "".join(c for c in p if unicodedata.category(c) != "Mn"))


def leer(p):
    with wave.open(str(p)) as w:
        return np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16), w.getframerate()


modelo = WhisperModel("small", device="cpu", compute_type="int8", download_root=sys.argv[1])
control = json.loads(CTRL.read_text()) if CTRL.exists() else {}
for voz, textos in gv.bloques():
    if all(f"{voz}:{t[:60]}" in control for t in textos):
        continue
    raw = voces.AUDIO / "bloques" / voces.destino(voz, "|".join(textos)).name
    if not raw.exists():
        print("falta bloque", voz, len(textos), flush=True)
        continue
    x, rate = leer(raw)
    a16 = resample_poly(x.astype(np.float32) / 32768, 16000, rate).astype(np.float32)
    segs, _ = modelo.transcribe(a16, language="es", word_timestamps=True, vad_filter=False, beam_size=5)
    pal = [w for s in segs for w in s.words]
    oido = [norm(w.word) for w in pal]
    guion_t, de = [], []
    for k, t in enumerate(textos):
        for w in t.split():
            guion_t.append(norm(w)); de.append(k)
    m = difflib.SequenceMatcher(None, guion_t, oido, autojunk=False)
    a2b = {}
    for bl in m.get_matching_blocks():
        for j in range(bl.size):
            a2b[bl.a + j] = bl.b + j
    sil = gv.silencios(x, rate)
    cortes = [0.0]
    for k in range(len(textos) - 1):
        ult = max(i for i, d in enumerate(de) if d == k)
        ai = next((a2b[i] for i in range(ult, -1, -1) if i in a2b), None)
        bi = next((a2b[i] for i in range(ult + 1, len(guion_t)) if i in a2b), None)
        t0 = pal[ai].end if ai is not None else cortes[-1]
        t1 = pal[bi].start if bi is not None else len(x) / rate
        cand = [s for s in sil if t0 - 0.15 <= s[0] <= t1 + 0.15]
        cortes.append(max(cand, key=lambda s: s[1])[0] if cand else (t0 + t1) / 2)
    cortes.append(len(x) / rate)
    for k, t in enumerate(textos):
        y = voces.recortar(x[int(cortes[k] * rate):int(cortes[k + 1] * rate)], rate)
        with wave.open(str(voces.destino(voz, t)), "wb") as w:
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(rate); w.writeframes(y.tobytes())
        idx = [i for i, d in enumerate(de) if d == k]
        ok = sum(1 for i in idx if i in a2b)
        control[f"{voz}:{t[:60]}"] = dict(coincide=round(ok / len(idx), 2), seg=round(len(y) / rate, 2), cps=round(len(t) / (len(y) / rate), 1))
    print(voz, len(textos), "frases alineadas", flush=True)
CTRL.write_text(json.dumps(control, ensure_ascii=False, indent=0))
malos = {k: v for k, v in control.items() if v["coincide"] < 0.7 or not 9 <= v["cps"] <= 24}
print(len(control), "frases,", len(malos), "por revisar")
for k, v in list(malos.items())[:40]:
    print(v, k)
