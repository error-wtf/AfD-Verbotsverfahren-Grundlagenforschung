#!/usr/bin/env bash

# Setup script for OCR environment on Ubuntu (WSL)
# Installs all required system packages and creates a Python venv with necessary Python libraries

set -euo pipefail

# Update package lists
sudo apt-get update

# Enable universe repository (for jbig2enc, pngquant, unpaper)
sudo add-apt-repository universe -y
sudo apt-get update

# Install core build tools and libraries
sudo apt-get install -y \
    build-essential \
    autoconf automake libtool pkg-config \
    libpng-dev libjpeg-dev libtiff-dev zlib1g-dev liblcms2-dev libffi-dev \
    ghostscript qpdf poppler-utils unpaper \
    tesseract-ocr tesseract-ocr-deu \
    pngquant \
    libjbig-dev mupdf-tools

# Create and activate a Python virtual environment
env_dir="$HOME/ocr_env"
python3 -m venv "$env_dir"
source "$env_dir/bin/activate"

# Upgrade pip and install Python packages
pip install --upgrade pip setuptools wheel
pip install \
    ocrmypdf \
    pikepdf>=5.0.1 \
    PyMuPDF \
    pytesseract \
    pillow

# Check installations
echo "\nInstallation complete. Versions:" 
ocrmypdf --version
pdftoppm -v | head -n1
unpaper --help | head -n1
tesseract --version
pngquant --version
jbig2enc --version
mupdf --version

cat << 'EOF'
Next steps:
1. Activate your venv: source ~/ocr_env/bin/activate
2. Run your bulk OCR script again.
EOF
