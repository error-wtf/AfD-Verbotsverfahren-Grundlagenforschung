#!/usr/bin/env python3
# print_pdfs_from_link_list.py

import time
import base64
import datetime
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# === Einstellungen ===
LINK_LIST     = Path("/mnt/d/afd-verbot.de-scrape-link-liste.txt")
PDF_DIR       = Path("/mnt/d/afd_proofs")
SEL_PROFILE   = "/tmp/selenium_profile_pdfs"
DATE_STR      = datetime.date.today().isoformat()  # z.B. "2025-07-28"

# Wartezeiten
DELAY_PAGE    = 1.0     # s nach driver.get()
# PDF‑Druck-Optionen
PDF_OPTIONS = {
    "printBackground": True,
    "marginTop":       0.5,
    "marginBottom":    0.5,
    "marginLeft":      0.5,
    "marginRight":     0.5,
    "paperWidth":      8.27,   # A4 in Zoll
    "paperHeight":     11.69
}

# === Verzeichnisse anlegen ===
if not LINK_LIST.exists():
    raise FileNotFoundError(f"Linkliste nicht gefunden: {LINK_LIST}")
PDF_DIR.mkdir(parents=True, exist_ok=True)

# === Selenium/Chrome einrichten ===
opts = Options()
opts.headless = True
opts.add_argument("--no-sandbox")
opts.add_argument("--disable-dev-shm-usage")
# entfernt user-data-dir um Konflikte zu vermeiden
driver = webdriver.Chrome(options=opts)

# === Linkliste einlesen ===
with LINK_LIST.open("r", encoding="utf-8") as f:
    links = [line.strip() for line in f if line.strip()]
total = len(links)
print(f"ℹ️  {total} Links geladen aus {LINK_LIST}")

# === PDFs erzeugen ===
for idx, url in enumerate(links, start=1):
    print(f"[{idx:04d}/{total:04d}] Lade {url} …", end="", flush=True)
    try:
        driver.get(url)
    except Exception as e:
        print(f" ⚠️ Fehler beim Laden: {e}")
        continue
    time.sleep(DELAY_PAGE)

    try:
        data = driver.execute_cdp_cmd("Page.printToPDF", PDF_OPTIONS)["data"]
    except Exception as e:
        print(f" ⚠️ PDF-Druck fehlgeschlagen: {e}")
        continue

    pdf_bytes = base64.b64decode(data)
    filename = f"afd-verbot.de-{DATE_STR}-proof-{idx:05d}.pdf"
    out_path = PDF_DIR / filename
    with out_path.open("wb") as pdf_file:
        pdf_file.write(pdf_bytes)
    size_kb = len(pdf_bytes) // 1024
    print(f" saved ({size_kb} KB) → {out_path.name}")

driver.quit()
print(f"\n🎉 Fertig! Alle PDFs in {PDF_DIR}/")  
