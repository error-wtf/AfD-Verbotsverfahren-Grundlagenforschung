#!/usr/bin/env python3
# manual_scroll_and_export_links_fast.py

import time
import datetime
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# === Einstellungen ===
LIST_URL     = "https://afd-verbot.de/beweise"
LINKS_FILE   = Path("/mnt/d/afd_links.txt")

# Ordner sicherstellen
LINKS_FILE.parent.mkdir(parents=True, exist_ok=True)

# 1) Sichtbaren Browser starten
opts = Options()
opts.headless = False
opts.add_argument("--no-sandbox")
opts.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=opts)

print(f"[1] Öffne Seite: {LIST_URL}")
driver.get(LIST_URL)
time.sleep(2)

# 2) Manuelles Scrollen
print("\n➡️ Bitte scrolle manuell BIS ZUM ENDE der Seite.")
print("   Wenn du fertig bist, drücke ENTER im Terminal…")
input()

# 3) Schnelles Einsammeln aller Links per JavaScript
print("\n[2] Sammle alle „Zum Beweis“-Links per JavaScript …")
hrefs = driver.execute_script("""
  const items = Array.from(
    document.querySelectorAll('a[href*="/beweise/"]')
  ).filter(a => a.textContent.trim() === 'Zum Beweis')
   .map(a => a.href);
  return [...new Set(items)];
""")
print(f"[2] {len(hrefs)} eindeutige Links gefunden.")

# 4) In Datei schreiben
print(f"[3] Schreibe Linkliste nach {LINKS_FILE}")
with LINKS_FILE.open("w", encoding="utf-8") as f:
    f.write("\n".join(hrefs) + "\n")
print("✅ Linkliste gespeichert.")

driver.quit()
