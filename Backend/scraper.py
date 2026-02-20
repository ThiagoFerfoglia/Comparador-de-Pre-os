import requests
from database import SessionLocal
from models import Produto

def coletar_produtos():
    url = "https://api.mercadolibre.com/sites/MLB/search?q=iphone"
    response = requests.get(url)
    data = response.json()

    session = SessionLocal()

    for item in data["resultados..."]:
        produto = Produto(
            nome=item["Nome do produto"],
            preco=item["Preco"],
            loja="Mercado Livre"
        )
        session.add(produto)
    #apenas exemplo, mas funciona da
    #mesma forma que fizemos a
    #adição de produtos em java, lembra T?

    session.commit()
    session.close()