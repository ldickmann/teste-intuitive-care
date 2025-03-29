# ...existing imports...
import pandas as pd
from app.core.config import settings
from app.models.operadora import Operadora
from typing import List
import unidecode
from fuzzywuzzy import process  # Biblioteca para buscas aproximadas


class OperadoraService:
    def __init__(self):
        self.df = self._carregar_dados()

    def _carregar_dados(self) -> pd.DataFrame:
        """Carrega o CSV e ajusta a formatação."""
        try:
            df = pd.read_csv(
                settings.DATA_PATH, delimiter=";", encoding="latin1", dtype=str
            )
            df.columns = [
                "registro_ans",
                "cnpj",
                "razao_social",
                "nome_fantasia",
                "modalidade",
                "logradouro",
                "numero",
                "complemento",
                "bairro",
                "cidade",
                "uf",
                "cep",
                "ddd",
                "telefone",
                "fax",
                "email",
                "representante",
                "cargo_representante",
                "regiao_comercializacao",
                "data_registro_ans",
            ]

            # Limpeza e normalização dos dados
            df = df.fillna("")
            df["nome_fantasia"] = df["nome_fantasia"].apply(unidecode.unidecode)
            df["cidade"] = df["cidade"].apply(unidecode.unidecode)  # Normalizar cidades
            df["uf"] = df["uf"].str.upper()
            return df
        except Exception as e:
            print(f"Erro ao carregar CSV: {e}")
            return pd.DataFrame()

    def buscar_operadoras(self, termo: str) -> List[Operadora]:
        """Busca operadoras que contenham o termo no nome, cidade ou CNPJ. Busca Geral."""
        termo_normalizado = unidecode.unidecode(termo).lower()
        resultados = self.df[
            self.df["nome_fantasia"]
            .str.lower()
            .str.contains(termo_normalizado, na=False)
            | self.df["razao_social"]
            .str.lower()
            .str.contains(termo_normalizado, na=False)
            | self.df["cnpj"].str.contains(termo_normalizado, na=False)
            | self.df["cidade"].str.lower().str.contains(termo_normalizado, na=False)
        ]
        return [Operadora(**row.to_dict()) for _, row in resultados.iterrows()]

    def buscar_operadoras_relevantes(self, termo: str) -> List[Operadora]:
        """Busca operadoras mais relevantes com base no nome fantasia.
        Se não houver termo, retorna as 10 primeiras operadoras."""
        if not termo:
            return [
                Operadora(**row.to_dict()) for _, row in self.df.head(10).iterrows()
            ]
        termo_normalizado = unidecode.unidecode(termo).lower()
        resultados = self.df[
            self.df["nome_fantasia"]
            .str.lower()
            .str.contains(termo_normalizado, na=False)
            | self.df["razao_social"]
            .str.lower()
            .str.contains(termo_normalizado, na=False)
            | self.df["cnpj"].str.contains(termo_normalizado, na=False)
            | self.df["cidade"].str.lower().str.contains(termo_normalizado, na=False)
        ]
        nomes_fantasia = resultados["nome_fantasia"].tolist()
        melhores_nomes = process.extract(termo_normalizado, nomes_fantasia, limit=10)
        operadoras_relevantes = resultados[
            resultados["nome_fantasia"].isin([nome[0] for nome in melhores_nomes])
        ]
        return [
            Operadora(**row.to_dict()) for _, row in operadoras_relevantes.iterrows()
        ]


# Instancia o serviço para uso nas rotas
operadora_service = OperadoraService()
