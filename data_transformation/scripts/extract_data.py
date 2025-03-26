import pdfplumber
import logging
import unicodedata


def setup_logging():
    """Configura o logging para o projeto."""
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
    )


def fix_encoding(text):
    """Corrige a codificação do texto."""
    try:
        return text.encode("latin1").decode("utf-8")
    except Exception:
        return text


def extract_table_data(pdf_path):
    """Extrai dados da tabela do PDF usando pdfplumber."""
    setup_logging()

    all_data = []
    seen_headers = False  # Variável para verificar se o cabeçalho já foi visto

    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                table = page.extract_table()
                if table:
                    for row in table:
                        # Correção de caracteres, normaliza acentos e remoção de espaços extras
                        row_clean = [
                            (
                                fix_encoding(unicodedata.normalize("NFC", col.strip()))
                                if col
                                else ""
                            )
                            for col in row
                        ]

                        # Definição do cabeçalho
                        header_ref = [
                            "PROCEDIMENTO",
                            "RN (alteração)",
                            "VIGÊNCIA",
                            "OD",
                            "AMB",
                            "HCO",
                            "HSO",
                            "REF",
                            "PAC",
                            "DUT",
                            "SUBGRUPO",
                            "GRUPO",
                            "CAPÍTULO",
                        ]

                        # Não adiciona cabeçalho duplicado
                        if not seen_headers and row_clean == header_ref:
                            seen_headers = True
                            continue

                        # Verifica se a linha tem o número correto de colunas
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
