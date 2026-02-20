from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import SessionLocal
from models import Produto
from scraper import coletar_produtos

#antes certifiquem-se que estao no diretorio do backend, para isso, no terminal, digitem "cd Backend",
#e depois rodem o comando abaixo

# para rodar o back end entrem no terminal 
# e digitem o comando "uvicorn main:app --reload", 
# isso vai iniciar o servidor do fastapi, 
# e ele vai ficar rodando, entao para acessar a aplicação, 
# basta abrir o navegador e digitar "http://localhost:8000", 
# isso vai abrir a aplicação, e para atualizar os produtos, 
# basta clicar no botão "Atualizar Produtos", 
# isso vai chamar a função "atualizar" que vai coletar os produtos do mercado livre e salvar no banco de dados,
#e para listar os produtos,
# basta clicar no botão "Listar Produtos", 
# isso vai chamar a função "listar_produtos" que vai buscar os produtos no banco de dados e mostrar na tela.

#cansei de escrever essa buceta





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