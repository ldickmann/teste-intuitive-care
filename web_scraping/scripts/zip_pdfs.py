import zipfile
import logging


# Função para zipar os PDFs
def zip_pdfs(pdf_files, zip_filename):
    """Zipa os PDFs em um arquivo."""
    with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
        for pdf in pdf_files:
            zipf.write(pdf, pdf.split("/")[-1])
    logging.info(f"Arquivo ZIP criado: {zip_filename}")
