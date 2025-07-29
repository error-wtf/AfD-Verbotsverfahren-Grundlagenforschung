#!/usr/bin/env bash
set -euo pipefail

ENV_DIR="$HOME/ocr_env"

echo "➤ 1. APT-Index aktualisieren"
sudo apt update

echo "➤ 2. System-Dependencies installieren"
sudo apt install -y \
  build-essential automake autoconf libtool pkg-config m4 git wget \
  poppler-utils ghostscript unpaper pngquant \
  tesseract-ocr tesseract-ocr-deu \
  libpng-dev libjpeg-dev libleptonica-dev \
  libssl-dev libffi-dev python3-dev python3-venv python3-distutils python3-pip

echo "➤ 3. jbig2enc aus Quellcode bauen"
TMPJ="$(mktemp -d)"
git clone https://github.com/agl/jbig2enc.git "$TMPJ/jbig2enc"
cd "$TMPJ/jbig2enc"
./autogen.sh
./configure
make -j"$(nproc)"
sudo make install
cd ~
rm -rf "$TMPJ"

echo "➤ 4. Python-Virtualenv anlegen unter $ENV_DIR"
python3 -m venv "$ENV_DIR"

echo "➤ 5. Virtualenv aktivieren & pip updaten"
# shellcheck disable=SC1090
source "$ENV_DIR/bin/activate"
pip install --upgrade pip setuptools wheel

echo "➤ 6. Python-Dependencies installieren"
pip install \
  ocrmypdf \
  pymupdf \
  pdf2image \
  pytesseract \
  pillow \
  opencv-python \
  numpy \
  cryptography \
  pyOpenSSL \
  "pikepdf>=5.0.1,<9.0.0"

deactivate

echo "✅ Fertig! Umgebung bereit."
echo "   Aktiviere sie mit: source $ENV_DIR/bin/activate"
