# Configurações globais da API


from pathlib import Path


class Settings:
    """Classe de configuração global da API."""

    BASE_DIR = Path(__file__).resolve().parent.parent
    APP_NAME: str = "API Operadoras"
    VERSION: str = "1.0.0"
    DATA_PATH = BASE_DIR / "data" / "relatorio_operadoras.csv"


settings = Settings()
