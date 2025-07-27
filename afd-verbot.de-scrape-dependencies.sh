#!/usr/bin/env python3
# incremental_scroll_and_link_export.py

import time
import datetime
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# === Einstellungen ===
LIST_URL     = "https://afd-verbot.de/beweise"
LINKS_FILE   = Path("/mnt/d/afd_links.txt")
PDF_DIR      = Path("/mnt/d/afd_proofs")    # unverändert, falls du später PDFs erzeugst
SEL_PROFILE  = "/tmp/selenium_profile"
DATE_STR     = datetime.date.today().isoformat()

SCROLL_STEP     = 100      # Pixel pro Scroll
DELAY_SCROLL    = 0.5      # Pause nach jedem Scroll
STABLE_LIMIT    = 100      # wie viele Scrolls ohne neue Links zulässig
MIN_LINKS       = 3600     # Mindestzahl, ab der Stable-Limit greift
MAX_ITERATIONS  = 10000    # absolutes Maximum an Scroll-Durchläufen

# === Setup: Ordner & Datei initialisieren ===
LINKS_FILE.parent.mkdir(parents=True, exist_ok=True)
if LINKS_FILE.exists():
    LINKS_FILE.unlink()  # alte Liste löschen
# Wir öffnen die Datei gleich im Append-Modus
links_fp = LINKS_FILE.open("a", encoding="utf-8")

# === Headless Chrome starten ===
opts = Options()
opts.headless = True
opts.add_argument("--no-sandbox")
opts.add_argument("--disable-dev-shm-usage")
opts.add_argument(f"--user-data-dir={SEL_PROFILE}")
driver = webdriver.Chrome(options=opts)

print(f"[1] Öffne Übersichtsseite: {LIST_URL}")
driver.get(LIST_URL)
time.sleep(2)

print("[1] Sehr langsames Scrollen + inkrementelles Link‑Export …")
seen      = set()
stable    = 0
iteration = 0

while iteration < MAX_ITERATIONS:
    iteration += 1
    # scrollen
    driver.execute_script(f"window.scrollBy(0, {SCROLL_STEP});")
    time.sleep(DELAY_SCROLL)

    # alle „Zum Beweis“-Links im aktuellen DOM finden
    elems = driver.find_elements(
        By.XPATH,
        "//a[contains(normalize-space(.), 'Zum Beweis') and contains(@href,'/beweise/')]"
    )

    new_count = 0
    for a in elems:
        href = a.get_attribute("href")
        if href and href not in seen:
            # sofort in Datei schreiben
            links_fp.write(href + "\n")
            links_fp.flush()
            seen.add(href)
            new_count += 1

    total = len(seen)
    print(f"  Iter {iteration}: {total} Links gefunden, {new_count} neu", end="")

    if new_count > 0:
        stable = 0
        print("  (+)")
    else:
        stable += 1
        print(f"  (- {stable}/{STABLE_LIMIT})")

    # Abbruch: MIN_LINKS erreicht + STABLE_LIMIT hintereinander keine neuen
    if total >= MIN_LINKS and stable >= STABLE_LIMIT:
        print(f"  → {stable}× ohne Neuzugang & ≥{MIN_LINKS} Links, Stop.")
        break
else:
    print(f"  → Max‑Iteration ({MAX_ITERATIONS}) erreicht, Stop.")

print(f"[1] Inkrementeller Export beendet: {len(seen)} Links in {LINKS_FILE}")

# cleanup
links_fp.close()
driver.quit()
print("🎉 Linkliste fertig!")  
