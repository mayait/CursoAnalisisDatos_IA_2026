#!/bin/bash
# Uso: bash ver.sh id1 id2 ... -> hoja de contacto en deck/_prueba.jpg
cd "$(dirname "$0")"
python3 deck_a_pdf.py "$@" >/dev/null && rm -f deck/_p-*.jpg && pdftoppm -r 40 -jpeg deck/_prueba.pdf deck/_p && n=$(ls deck/_p-*.jpg | wc -l | tr -d ' ') && c=2 && ins="" && for f in deck/_p-*.jpg; do ins="$ins -i $f"; done && if [ "$n" = "1" ]; then cp deck/_p-*.jpg deck/_prueba.jpg; else lay=""; k=0; for f in deck/_p-*.jpg; do x=$(( (k%c)*800 )); y=$(( (k/c)*450 )); lay="$lay${lay:+|}${x}_${y}"; k=$((k+1)); done; ffmpeg -y -loglevel error $ins -filter_complex "xstack=inputs=$n:layout=$lay:fill=white" -frames:v 1 deck/_prueba.jpg; fi; echo deck/_prueba.jpg
