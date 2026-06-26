pip install pypdf

from pathlib import Path
from pypdf import PdfWriter

pdf_folder = Path("pdfs")
output_file = "merged.pdf"

writer = PdfWriter()

# Merge PDFs in alphabetical order
pdf_files = sorted(pdf_folder.glob("*.pdf"))

for pdf in pdf_files:
    writer.append(str(pdf))

with open(output_file, "wb") as file:
    writer.write(file)

print(f"Merged {len(pdf_files)} PDFs into {output_file}.")