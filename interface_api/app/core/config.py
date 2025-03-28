# Configurações globais da API

import os


class Settings:
    APP_NAME: str = "API Operadoras"
    VERSION: str = "1.0.0"
    DATA_PATH: str = os.path.join(
        os.path.dirname(__file__), "../data/relatorio_operadoras.csv"
    )


settings = Settings()
