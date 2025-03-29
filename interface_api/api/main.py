from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.routes import router as api_router
from core.config import settings

# Configuração de inicialização do FastAPI
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description="API para consulta de operadoras",
    docs_url="/docs",
    redoc_url="/redoc",
)

# Configurações do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos os métodos HTTP
    allow_headers=["*"],  # Permitir todos os cabeçalhos
)

# Incluindo as rotas da API
app.include_router(api_router, prefix="/api")


# Health check endpoint para verificação de status da API
@app.get("/health", tags=["Health Check"])
def health_check():
    """Verifica se a API está funcionando."""
    return {"status": "API está funcionando", "version": settings.VERSION}
