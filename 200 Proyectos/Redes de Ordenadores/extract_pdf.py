import fitz  # PyMuPDF
import sys
import os

def extract_pdf_content(pdf_path, output_txt_path):
    try:
        doc = fitz.open(pdf_path)
        with open(output_txt_path, "w", encoding="utf-8") as f:
            for i, page in enumerate(doc):
                f.write(f"--- PAGE {i+1} ---\n")
                f.write(page.get_text())
                f.write("\n\n")
        print(f"Successfully extracted {pdf_path} to {output_txt_path}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python extract.py <input_pdf> <output_txt>")
    else:
        extract_pdf_content(sys.argv[1], sys.argv[2])
