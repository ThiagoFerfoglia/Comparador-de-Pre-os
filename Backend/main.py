from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import SessionLocal
from models import Produto
from scraper import coletar_produtos


# Criando aplicação
app = FastAPI()


# Configuração de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Rota para atualizar produtos
@app.get("/atualizar")
def atualizar():
    coletar_produtos()
    return {"msg": "Produtos coletados com sucesso"}


# Rota para listar produtos
@app.get("/produtos")
def listar_produtos():
    session = SessionLocal()
    produtos = session.query(Produto).all()

    resultado = []
    for p in produtos:
        resultado.append({
            "id": p.id,
            "nome": p.nome,
            "preco": p.preco
        })

    session.close()
    return resultado