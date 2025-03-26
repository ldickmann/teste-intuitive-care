import logging
from scripts.utils import setup_logging, setup_driver, extract_pdf_links
from scripts.download_pdfs import download_pdfs
from scripts.zip_pdfs import zip_pdfs

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

# Download dos PDFs
pdf_files = download_pdfs(pdf_links, "pdfs")

# Compactação dos PDFs em um arquivo ZIP
zip_filename = "anexos_pdfs.zip"
zip_pdfs(pdf_files, zip_filename)
