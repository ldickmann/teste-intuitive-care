# Definição das rotas da API

from fastapi import APIRouter, Query
from app.services.search import operadora_service
from typing import List
from app.models.operadora import Operadora

router = APIRouter()


# Rota para buscar operadoras por nome, cidade ou CNPJ
@router.get("/buscar", response_model=List[Operadora])
def buscar_operadoras(
    nome: str = Query(None, min_length=3, description="Nome da operadora"),
    cidade: str = Query(None, description="Cidade da operadora"),
    cnpj: str = Query(None, description="CNPJ da operadora"),
):
    """Busca operadoras por nome, cidade ou CNPJ."""
    if not any([nome, cidade, cnpj]):
        return []  # Retorna lista vazia se nenhum parâmetro for fornecido

    termo = nome or cidade or cnpj
    return operadora_service.buscar_operadoras(termo)


# Rota para buscar operadoras relevantes
@router.get("/buscar_operadora_relevante", response_model=List[Operadora])
def buscar_operadoras_relevantes(
    nome: str = Query("", min_length=0, description="Nome da operadora (opcional)")
):
    """Busca operadoras e retorna as 10 mais relevantes.
    Se nome não for informado, retorna as 10 primeiras."""
    return operadora_service.buscar_operadoras_relevantes(nome)
