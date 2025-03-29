# Models da API para representar os dados de operadoras

from pydantic import BaseModel


class Operadora(BaseModel):
    registro_ans: str
    cnpj: str
    razao_social: str
    nome_fantasia: str
    modalidade: str
    logradouro: str
    numero: str
    complemento: str
    bairro: str
    cidade: str
    uf: str
    cep: str
    ddd: str
    telefone: str
    fax: str
    email: str
    representante: str
    cargo_representante: str
    regiao_comercializacao: str
    data_registro_ans: str
