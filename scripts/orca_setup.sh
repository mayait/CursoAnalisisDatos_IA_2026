#!/usr/bin/env bash
# Setup de un worktree nuevo de Orca para ADM 2003.
# 1. Trae el material local que no está en git (el repo es público).
# 2. Enlaza grabaciones/ desde la raíz, sin duplicar archivos pesados.
# 3. Crea .venv con las librerías de los cuadernos y los generadores.
# 4. Instala pptxgenjs para los crear_slides.js.
set -euo pipefail

WORKTREE_DIR="${ORCA_WORKTREE_PATH:-$(pwd)}"
ROOT_DIR="${ORCA_ROOT_PATH:-$(git -C "$WORKTREE_DIR" worktree list --porcelain | awk 'NR==1{sub(/^worktree /,""); print; exit}')}"
WORKSPACE_NAME="${ORCA_WORKSPACE_NAME:-local}"

echo "============================================================"
echo " Orca setup · ADM 2003 Análisis de Datos"
echo " Workspace : $WORKSPACE_NAME"
echo " Worktree  : $WORKTREE_DIR"
echo " Raíz      : $ROOT_DIR"
echo "============================================================"
cd "$WORKTREE_DIR"

# 1. Material local sin versionar: se copia solo lo que no existe en el worktree.
if [ "$ROOT_DIR" != "$WORKTREE_DIR" ] && [ -d "$ROOT_DIR" ]; then
  echo ">>> Copiando material local sin versionar desde la raíz"
  n=0
  while IFS= read -r -d '' f; do
    case "$f" in
      grabaciones/*|_rescate_worktrees/*) continue ;;
    esac
    if [ ! -e "$WORKTREE_DIR/$f" ]; then
      mkdir -p "$WORKTREE_DIR/$(dirname "$f")"
      cp -p "$ROOT_DIR/$f" "$WORKTREE_DIR/$f"
      n=$((n + 1))
    fi
  done < <(git -C "$ROOT_DIR" ls-files --others --exclude-standard -z)
  echo "    $n archivos copiados"

  # Claves locales (ignoradas por git): se copian con permisos restringidos.
  if [ -f "$ROOT_DIR/.env" ] && [ ! -e "$WORKTREE_DIR/.env" ]; then
    install -m 600 "$ROOT_DIR/.env" "$WORKTREE_DIR/.env"
    echo ">>> .env copiado desde la raíz"
  fi

  # 2. Grabaciones y transcripciones: enlace simbólico a la carpeta de la raíz.
  if [ -d "$ROOT_DIR/grabaciones" ] && [ ! -e "$WORKTREE_DIR/grabaciones" ]; then
    ln -s "$ROOT_DIR/grabaciones" "$WORKTREE_DIR/grabaciones"
    echo ">>> grabaciones/ enlazada desde la raíz"
  fi
fi

# 3. Entorno de Python.
if command -v uv >/dev/null 2>&1; then
  echo ">>> Preparando .venv con uv"
  [ -d .venv ] || uv venv --quiet .venv
  uv pip install --quiet --python .venv/bin/python -r requirements.txt
  .venv/bin/python -c "import pandas, sklearn, matplotlib; print(f'    pandas {pandas.__version__} · scikit-learn {sklearn.__version__}')"
else
  echo "!!! uv no está instalado: se omite el entorno de Python"
fi

# 4. Node para los decks en pptxgenjs.
if command -v npm >/dev/null 2>&1; then
  echo ">>> Instalando pptxgenjs"
  npm install --silent --no-audit --no-fund >/dev/null
else
  echo "!!! npm no está instalado: se omite pptxgenjs"
fi

echo "============================================================"
echo " Listo. Python: .venv/bin/python · Cuadernos: .venv/bin/jupyter nbconvert --execute"
echo "============================================================"
