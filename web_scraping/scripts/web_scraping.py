import os
import logging
from .utils import setup_logging, setup_driver, extract_pdf_links
from .download_pdfs import download_pdfs
from .zip_pdfs import zip_pdfs

# Define o diretório de PDFs relativo ao local deste script
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_DIR = os.path.join(CURRENT_DIR, "..", "pdfs")

# Configuração do logging
setup_logging()

# Inicialização do WebDriver
driver = setup_driver()

try:
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
    logging.info(f"Acessando a URL: {url}")
    driver.get(url)

    # Extração dos links dos PDFs
    pdf_links = extract_pdf_links(driver)

    logging.info(f"Total de links extraídos: {len(pdf_links)}")

finally:
    # Fechamento do WebDriver
    driver.quit()

# Download dos PDFs usando o diretório absoluto definido
pdf_files = download_pdfs(pdf_links, PDF_DIR)

# Compactação dos PDFs em um arquivo ZIP dentro da pasta pdfs
zip_filename = os.path.join(PDF_DIR, "anexos_pdfs.zip")
zip_pdfs(pdf_files, zip_filename)
