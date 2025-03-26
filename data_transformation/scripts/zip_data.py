# scripts/zip_data.py
import zipfile
import os
import logging


def zip_file(csv_path, zip_path, nome):
    """Compacta o arquivo CSV em um arquivo ZIP."""
    try:
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            zipf.write(csv_path, os.path.basename(csv_path))  # Adiciona o CSV ao ZIP
        logging.info(f"Arquivo ZIP criado: {zip_path}")
    except Exception as e:
        logging.error(f"Erro ao criar o arquivo ZIP: {e}")
        return False
    return True
