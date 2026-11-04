#!/usr/bin/env bash
# Archivo de un worktree de Orca para ADM 2003.
# Nada se borra: el material sin versionar que se creó o cambió en el worktree
# se rescata a <raíz>/_rescate_worktrees/<workspace>-<fecha>/ antes de que Orca lo elimine.
set -euo pipefail

WORKTREE_DIR="${ORCA_WORKTREE_PATH:-$(pwd)}"
ROOT_DIR="${ORCA_ROOT_PATH:-$(git -C "$WORKTREE_DIR" worktree list --porcelain | awk 'NR==1{sub(/^worktree /,""); print; exit}')}"
WORKSPACE_NAME="${ORCA_WORKSPACE_NAME:-$(basename "$WORKTREE_DIR")}"

[ "$ROOT_DIR" = "$WORKTREE_DIR" ] && { echo "[archive] Es la raíz del repo: no hay nada que rescatar."; exit 0; }

DEST="$ROOT_DIR/_rescate_worktrees/${WORKSPACE_NAME}-$(date +%Y%m%d-%H%M%S)"
n=0
while IFS= read -r -d '' f; do
  case "$f" in grabaciones|grabaciones/*) continue ;; esac
  if [ ! -e "$ROOT_DIR/$f" ] || ! cmp -s "$WORKTREE_DIR/$f" "$ROOT_DIR/$f"; then
    mkdir -p "$DEST/$(dirname "$f")"
    cp -p "$WORKTREE_DIR/$f" "$DEST/$f"
    n=$((n + 1))
  fi
done < <(git -C "$WORKTREE_DIR" ls-files --others --exclude-standard -z)

if [ "$n" -gt 0 ]; then
  echo "[archive] $n archivos sin versionar rescatados en $DEST"
else
  echo "[archive] Sin material sin versionar nuevo o modificado."
fi
