# Definição das rotas da API

from fastapi import APIRouter, Query
from typing import List
from app.models.operadora import Operadora

router = APIRouter()
