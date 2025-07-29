#!/usr/bin/env python3
"""
bulk_improved_ocr_to_md.py

Robuste Bulk-OCR für gescannte PDFs:
 1. Primär: OCRmyPDF (mit Deskew, Optimize, Rotate und Clean, falls verfügbar)
 2. Fallback: pdf2image → OpenCV-Preprocessing → Tesseract mit LSTM und angepasstem PSM/Whitelist

Ziel: Minimale Erkennungsfehler auf schlechten Scans.

Voraussetzungen:
  pip install ocrmypdf pymupdf pdf2image pytesseract pillow opencv-python numpy
  Unpaper, pdftoppm, pngquant, jbig2 (optional) im PATH für OCRmyPDF
"""

import subprocess, sys
from pathlib import Path
import argparse
from shutil import which

import fitz                         # PyMuPDF
from pdf2image import convert_from_path
import pytesseract
from PIL import Image
import cv2
import numpy as np

def has_cmd(cmd):
    return which(cmd) is not None

def build_ocrmypdf_cmd(inp, out, lang, use_clean):
    cmd = [
        "ocrmypdf",
        "--deskew",
        "--rotate-pages",
        "--optimize", "3",
        "-l", lang,
        str(inp), str(out)
    ]
    if use_clean:
        cmd.insert(2, "--clean")
    return cmd

def ocrmypdf_stage(input_pdf, tmp_pdf, lang, use_clean):
    cmd = build_ocrmypdf_cmd(input_pdf, tmp_pdf, lang, use_clean)
    subprocess.run(cmd, check=True)

def extract_text_with_pymupdf(pdf_path):
    doc = fitz.open(str(pdf_path))
    pages = [page.get_text("text") for page in doc]
    doc.close()
    return pages

def preprocess_image(pil_img):
    # 1) Graustufen
    img = np.array(pil_img.convert("L"))
    # 2) CLAHE (kontrastverstärkend)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    img = clahe.apply(img)
    # 3) Rauschunterdrückung
    img = cv2.fastNlMeansDenoising(img, h=15, templateWindowSize=7, searchWindowSize=21)
    # 4) Bilateralfilter (Kanten schonen)
    img = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)
    # 5) Adaptives Thresholding
    img = cv2.adaptiveThreshold(
        img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, blockSize=31, C=10
    )
    # 6) Morphologische Opening (Rauschartefakte entfernen)
    kernel = np.ones((1,1), np.uint8)
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    return img

def fallback_ocr(input_pdf, lang):
    pages = convert_from_path(str(input_pdf), dpi=400)
    texts = []
    tesseract_config = (
        r"--oem 1 "                # LSTM-Engine
        r"--psm 3 "                # Vollseiten-Layout
        r"-c tessedit_char_whitelist="
        r"ÄÖÜäöüßABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    )
    for pil in pages:
        proc = preprocess_image(pil)
        txt = pytesseract.image_to_string(proc, lang=lang, config=tesseract_config)
        texts.append(txt)
    return texts

def write_markdown(pages, md_path, title):
    with md_path.open("w", encoding="utf-8") as f:
        for i, txt in enumerate(pages, 1):
            f.write(f"# {title} – Seite {i}\n\n")
            f.write(txt.strip() + "\n\n")
            f.write("---\n\n")

def process_pdf(pdf_path, out_dir, lang, use_clean):
    stem = pdf_path.stem
    tmp_pdf = out_dir / f"{stem}.searchable.pdf"
    md_file = out_dir / f"{stem}.md"

    print(f"[→] Bearbeite {stem}")
    try:
        ocrmypdf_stage(pdf_path, tmp_pdf, lang, use_clean)
        pages = extract_text_with_pymupdf(tmp_pdf)
        tmp_pdf.unlink(missing_ok=True)
        print("   ✓ OCRmyPDF erfolgreich")
    except Exception as e:
        print(f"   ⚠️ OCRmyPDF fehlgeschlagen ({e}), Fallback-OCR läuft …")
        pages = fallback_ocr(pdf_path, lang)

    write_markdown(pages, md_file, stem)
    print(f"   ✓ Markdown geschrieben: {md_file.name}")

def main():
    parser = argparse.ArgumentParser(
        description="Bulk-OCR mit erweiterten Preprocessing-Stufen"
    )
    parser.add_argument(
        "--output-dir", "-o",
        help="Ausgabeverzeichnis (Standard: aktuelles Verzeichnis)"
    )
    parser.add_argument(
        "--lang", "-l", default="deu",
        help="OCR-Sprache (z.B. 'deu' für Deutsch)"
    )
    args = parser.parse_args()

    cwd = Path.cwd()
    out_dir = Path(args.output_dir) if args.output_dir else cwd
    out_dir.mkdir(parents=True, exist_ok=True)

    use_clean = has_cmd("unpaper")
    if not has_cmd("ocrmypdf"):
        print("⚠️  ocrmypdf nicht gefunden – nur Fallback-OCR wird genutzt\n")

    for pdf in sorted(cwd.glob("*.pdf")):
        process_pdf(pdf, out_dir, args.lang, use_clean)

if __name__ == "__main__":
    main()
