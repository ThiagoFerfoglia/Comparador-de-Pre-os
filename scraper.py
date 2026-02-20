import requests
from database import SessionLocal
from models import Produto

def coletar_produtos():
    url = "https://api.mercadolibre.com/sites/MLB/search?q=iphone"
    response = requests.get(url)
    data = response.json()

    session = SessionLocal()

    for item in data["results"]:
        produto = Produto(
            nome=item["title"],
            preco=item["price"],
            loja="Mercado Livre"
        )
        session.add(produto)

    session.commit()
    session.close()