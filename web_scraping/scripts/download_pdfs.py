import os
import requests
import logging
from tqdm import tqdm


# Função para download dos PDFs
def download_pdfs(pdf_links, download_path="pdfs"):
    """Download dos PDFs para o diretório especificado."""
    os.makedirs(download_path, exist_ok=True)

    pdf_files = []
    for index, pdf_url in enumerate(pdf_links, start=1):
        pdf_path = os.path.join(download_path, f"Anexo_{index}.pdf")

        # Impede de baixar o arquivo novamente
        if os.path.exists(pdf_path):
            logging.info(f"Arquivo já existe, pulando: {pdf_path}")
            pdf_files.append(pdf_path)
            continue

        logging.info(f"Baixando {pdf_url}...")
        response = requests.get(pdf_url, stream=True)
        response.raise_for_status()

        tamanho_total = int(response.headers.get("content-length", 0))
        with open(pdf_path, "wb") as file, tqdm(
            total=tamanho_total, unit="B", unit_scale=True, desc=f"Baixando {pdf_path}"
        ) as barra:
            for chunk in response.iter_content(chunk_size=1024):
                file.write(chunk)
                barra.update(len(chunk))

        pdf_files.append(pdf_path)
        logging.info(f"Download concluído: {pdf_path}")

    return pdf_files
