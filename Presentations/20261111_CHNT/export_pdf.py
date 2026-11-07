"""Export the rendered presentation (index.html) as a PDF, one page per slide.

Usage (from this folder, after `quarto render index.qmd`):
    pip install playwright
    python export_pdf.py [output.pdf]

Uses the Chrome that is installed on the machine (no browser download).
Set CHROME_PATH to the chrome executable if Chrome is installed somewhere unusual.
"""
import os
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

here = Path(__file__).resolve().parent
html = here / "index.html"
out = Path(sys.argv[1]) if len(sys.argv) > 1 else here / "SpaceTimeArc_CHNT31.pdf"

if not html.exists():
    sys.exit("index.html not found: run `quarto render index.qmd` first.")

with sync_playwright() as p:
    chrome = os.environ.get("CHROME_PATH")
    browser = (
        p.chromium.launch(executable_path=chrome, args=["--no-sandbox"])
        if chrome
        else p.chromium.launch(channel="chrome")
    )
    page = browser.new_page()
    # ?print-pdf makes Reveal.js lay the slides out one per page
    page.goto(html.as_uri() + "?print-pdf")
    page.wait_for_function("document.querySelectorAll('.pdf-page').length > 0", timeout=60000)
    page.wait_for_timeout(3000)  # images, fonts
    n = page.evaluate("document.querySelectorAll('.pdf-page').length")
    page.pdf(path=str(out), prefer_css_page_size=True, print_background=True)
    browser.close()

print(f"{n} slides -> {out}")
