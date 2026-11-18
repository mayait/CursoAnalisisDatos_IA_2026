#!/bin/bash
# Guía del profesor a PDF (pandoc + Chrome). Uso: bash guia_a_pdf.sh
cd "$(dirname "$0")"
cat > /tmp/_guia.css <<'CSS'
body{font-family:"Helvetica Neue",Arial,sans-serif;font-size:11pt;line-height:1.45;color:#111;max-width:720px;margin:0 auto;padding:8px}
h1{font-size:20pt;border-bottom:4px solid #E11B22;padding-bottom:6px}h2{font-size:14pt;margin-top:22px;color:#E11B22}
table{border-collapse:collapse;width:100%;margin:10px 0;font-size:9.5pt}th,td{border:1px solid #bbb;padding:5px 7px;text-align:left;vertical-align:top}th{background:#111;color:#fff}
code,pre{font-family:Menlo,monospace;font-size:9pt;background:#f2f2f2}pre{padding:10px;white-space:pre-wrap}
CSS
pandoc guia_profesor.md -f gfm -t html5 -s --metadata title=" " -c /tmp/_guia.css --embed-resources -o deck/_guia.html
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --disable-gpu --no-pdf-header-footer --print-to-pdf="Guia-del-profesor.pdf" "file://$PWD/deck/_guia.html" 2>/dev/null
ls -la Guia-del-profesor.pdf
