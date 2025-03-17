import os
from PyPDF2 import PdfReader, PdfWriter

def add_watermark(input_pdf, watermark_pdf, output_pdf):
    reader = PdfReader(input_pdf)
    watermark = PdfReader(watermark_pdf).pages[0]  # Première page du filigrane
    writer = PdfWriter()

    for page in reader.pages:
        page.merge_page(watermark)  # Appliquer le filigrane
        writer.add_page(page)

    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)
    print(f"✅ Filigrane ajouté : {output_pdf}")

# 📂 Dossiers contenant les fichiers PDF
input_folder = "pdf_input/"
output_folder = "pdf_output/"
watermark_file = "watermark.pdf"  # Ton fichier filigrane

# 🛠️ Création du dossier de sortie s'il n'existe pas
os.makedirs(output_folder, exist_ok=True)

# 🚀 Appliquer le filigrane à tous les fichiers PDF du dossier
for filename in os.listdir(input_folder):
    if filename.endswith(".pdf"):
        input_pdf_path = os.path.join(input_folder, filename)
        output_pdf_path = os.path.join(output_folder, filename)
        add_watermark(input_pdf_path, watermark_file, output_pdf_path)
