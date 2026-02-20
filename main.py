from fastapi import FastAPI
from database import SessionLocal
from models import Produto
from scraper import coletar_produtos

app = FastAPI()

@app.get("/atualizar")
def atualizar():
    coletar_produtos()
    return {"msg": "Produtos coletados"}

@app.get("/produtos")
def listar_produtos():
    session = SessionLocal()
    produtos = session.query(Produto).all()
    return produtos