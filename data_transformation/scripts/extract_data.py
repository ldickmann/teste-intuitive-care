import pdfplumber
import re
import logging
import pandas as pd


def setup_logging():
    """Configura o logging para o projeto."""
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )


def extract_table_data(pdf_path):
    """
    Extrai dados da tabela do PDF
    """
    setup_logging()

    all_data = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                lines = text.split("\n")

                # Encontra o início da tabela procurando por um cabeçalho ou linha chave
                start_table = False
                for line in lines:
                    if "PROCEDIMENTO" in line and "VIGÊNCIA" in line:
                        start_table = True
                        continue

                    if start_table:
                        # Ignora linhas de cabeçalho
                        if "OD" in line and "AMB" in line:
                            continue

                        # Procura por linhas que parecem dados da tabela
                        if re.match(r"^\s*\d+", line):
                            # Divide a linha em colunas
                            parts = line.split()

                            # Agrup as colunas, considerando os padrões da tabela
                            if len(parts) > 9:
                                parts[1] = " ".join(parts[1:-7])
                                parts = parts[:2] + parts[-7:]

                            if len(parts) == 13:
                                all_data.append(parts)
                            else:
                                logging.warning(
                                    f"Linha com número incorreto de colunas: {parts}"
                                )

        logging.info(f"Total de linhas extraídas: {len(all_data)}")
    except Exception as e:
        logging.error(f"Erro ao processar o PDF: {e}")
        return None

    return all_data
