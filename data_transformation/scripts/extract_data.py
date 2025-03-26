import pdfplumber
import re
import logging


def setup_logging():
    """Configura o logging para o projeto."""
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )


def extract_table_data(pdf_path):
    """Extrai dados da tabela do PDF."""
    setup_logging()

    all_data = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                lines = text.split("\n")
                start_table = False
                for line in lines:
                    if "PROCEDIMENTO" in line and "VIGÊNCIA" in line:
                        start_table = True
                        continue

                    if start_table:
                        if "OD" in line and "AMB" in line:
                            continue

                        parts = re.split(r"\s{2,}", line.strip())

                        # Se houver mais de 13 colunas, tenta reagrupar
                        if len(parts) > 13:
                            parts[0] = " ".join(parts[:2])
                            parts = parts[:1] + parts[2:]

                        # Se houver menos de 13, adicione colunas vazias
                        if len(parts) < 13:
                            logging.warning(
                                f"Linha com número incorreto de colunas (antes do padding): {parts}"
                            )
                            parts.extend([""] * (13 - len(parts)))

                        # Se após o padding atingir 13 colunas, adiciona a linha
                        if len(parts) == 13:
                            all_data.append(parts)
                        else:
                            logging.warning(f"Linha descartada: {parts}")

        logging.info(f"Total de linhas extraídas: {len(all_data)}")
    except Exception as e:
        logging.error(f"Erro ao processar o PDF: {e}")
        return None

    return all_data
