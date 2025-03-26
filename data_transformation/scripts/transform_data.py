import pandas as pd
import logging


def transform_and_save(data, output_path, nome):
    """Transforma os dados que foram extraídos, faz a substituição das abreviações e salva em um arquivo CSV."""
    try:
        # Log para verificar os dados antes da criação do DataFrame
        logging.info(f"Dados extraídos: {data}")

        # Cria um DataFrame com os dados extraídos
        df = pd.DataFrame(data)

        # (re)nomeia as colunas
        colunas = [
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

        # Verificação para saber se os dados têm o número correto de colunas
        if len(df.columns) != len(colunas):
            logging.error(
                f"Erro ao transformar os dados: número de colunas incorreto. Esperado {len(colunas)}, obtido {len(df.columns)}."
            )
            return False

        # Nomeação das colunas do DataFrame
        df.columns = colunas

        # Prita as colunas
        print("Colunas do DataFrame:", df.columns)

        # Printa as primeiras linhas do DataFrame para verificar a transformação
        print("Primeiras linhas do DataFrame:\n", df.head())

        # Remoção de linhas duplicadas do cabeçalho
        df = df[df["PROCEDIMENTO"] != "PROCEDIMENTO"]

        # Substituição das abreviações "OD" e "AMB" para as descrições completas, conforme legenda
        df["OD"] = df["OD"].replace({"OD": "Seg. Odontológica"})
        df["AMB"] = df["AMB"].replace({"AMB": "Seg. Ambulatorial"})

        # Salva o DataFrame em um arquivo CSV com separador ponto e vírgula e codificação UTF-8
        df.to_csv(
            output_path, index=False, sep=";", encoding="utf-8-sig", errors="replace"
        )

        logging.info(f"Dados transformados e arquivo CSV salvo: {output_path}")
        return True

    except Exception as e:
        logging.error(f"Erro ao transformar e salvar os dados: {e}")
        return False
