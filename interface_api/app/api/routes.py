# Definição das rotas da API

from fastapi import APIRouter, Query
from app.services.search import operadora_service
from typing import List
from app.models.operadora import Operadora

router = APIRouter()


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
