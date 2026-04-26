#!/usr/bin/env python3
import sys, os
try:
    import fitz
except Exception:
    print("ERROR: PyMuPDF is not installed. Install with: python -m pip install pymupdf")
    sys.exit(2)

def extract_pages(path, start_page, end_page):
    doc = fitz.open(path)
    n = doc.page_count
    if start_page < 1 or end_page > n or start_page > end_page:
        print(f"ERROR: Page range invalid. Document has {n} pages.")
        sys.exit(2)
    for p in range(start_page-1, end_page):
        page = doc.load_page(p)
        text = page.get_text("text")
        if not text.strip():
            blocks = page.get_text("blocks")
            text = "\n".join(b[4] for b in blocks if len(b) > 4 and isinstance(b[4], str))
        print(f"---PAGE {p+1} START---")
        print(text)
        print(f"---PAGE {p+1} END---\n")

if __name__ == "__main__":
    if len(sys.argv) not in (4, 5):
        print("Usage: python extract_pdf_pages.py FILE START_PAGE END_PAGE [OUTFILE]")
        sys.exit(1)
    filepath = sys.argv[1]
    start = int(sys.argv[2])
    end = int(sys.argv[3])
    out = sys.argv[4] if len(sys.argv) == 5 else None
    extract_pages(filepath, start, end, out)
