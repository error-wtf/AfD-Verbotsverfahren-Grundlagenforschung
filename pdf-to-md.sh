#!/usr/bin/env bash
# convert_pdfs_to_md.sh

PDF_DIR="/mnt/d/afd_proofs"
MD_DIR="/mnt/d/afd_markdown"

mkdir -p "$MD_DIR"

for pdf in "$PDF_DIR"/afd-verbot.de-*.pdf; do
  base=$(basename "$pdf" .pdf)
  echo "Konvertiere $base.pdf → $base.md"
  # Text extrahieren in temporäre .txt
  pdftotext -layout "$pdf" "$MD_DIR/$base.txt"
  # nur umbenennen in .md
  mv "$MD_DIR/$base.txt" "$MD_DIR/$base.md"
done

echo "Fertig! Alle Markdown‑Dateien in $MD_DIR"
