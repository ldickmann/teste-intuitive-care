import logging
import os
import scripts.extract_data as extract_table_data
import scripts.extract_data as setup_logging
import scripts.transform_data as transform_and_save
import scripts.zip_data as zip_file


def main():
    """Função principal do script de transformação e extração de dados."""
    setup_logging()
    nome = "Lucas Elias Dickmann"
    pdf_path = "data/anexo_1.pdf"  # Especifica o caminho do arquivo PDF
    csv_path = "data/rol_procedimentos.csv"
    zip_path = f"data/Teste_{nome}.zip"  # Caminho e nome do arquivo ZIP de saída

    # Extrai dados da tabela do PDF
    logging.info("Extraindo dados da tabela do PDF...")
    data = extract_table_data(pdf_path)
    if not data:
        logging.error("Erro ao extrair dados da tabela do PDF.")
        return

    # Transformação e salvamento dos dados extraídos
    logging.info("Transformando e salvando os dados extraídos...")
    if not transform_and_save(data, csv_path, nome):
        logging.error("Erro ao transformar e salvar os dados extraídos.")
        return

    # Compacta o arquivo CSV em um arquivo ZIP
    logging.info("Compactando o arquivo CSV em um arquivo ZIP...")
    if not zip_file(csv_path, zip_path, nome):
        logging.error("Erro na compactação do arquivo CSV.")
        return

    logging.info("Processo de transformação e extração de dados concluído com sucesso.")

    if __name__ == "__main__":
        main()
