import pdfplumber
import logging


def setup_logging():
    """Configura o logging para o projeto."""
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )


def extract_table_data(pdf_path):
    """Extrai dados da tabela do PDF usando pdfplumber."""
    setup_logging()

    all_data = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                table = page.extract_table()
                if table:
                    for row in table:
                        # Remove linhas vazias ou com colunas None
                        row_clean = [col.strip() if col else "" for col in row]

                        # Verifica se o número de colunas está correto (13)
                        if len(row_clean) == 13:
                            all_data.append(row_clean)
                        else:
                            logging.warning(
                                f"Linha ignorada por estar incompleta: {row_clean}"
                            )

        logging.info(f"Total de linhas extraídas: {len(all_data)}")
    except Exception as e:
        logging.error(f"Erro ao processar o PDF: {e}")
        return None

    return all_data
