#!/bin/bash
# Render final a 1080p. Necesita manim en el PATH. MEDIA es una carpeta de trabajo por escena para no pisar la caché de textos.
MEDIA=${1:-/tmp/manim_s22}
for sc in S1Ajuste S2Columnas S3Abanico S4Grado S5Ridge S6Lasso S7Geometria S8Validacion; do
  ( manim -r 1920,1080 --fps 30 --media_dir "$MEDIA/$sc" --disable_caching -v WARNING escenas.py $sc && cp "$MEDIA/$sc/videos/escenas/1080p30/$sc.mp4" . ) &
done
wait
