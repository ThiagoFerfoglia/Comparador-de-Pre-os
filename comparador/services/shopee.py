import requests
from bs4 import BeautifulSoup

def buscar_shopee(query):
    url = f"https://shopee.com.br/search?keyword={query}"

    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    produtos = []

    for item in soup.select(".shopee-search-item-result__item")[:5]:
        titulo = item.select_one("div")
        preco = item.select_one("span")

        if titulo and preco:
            produtos.append({
                "site": "Shopee",
                "titulo": titulo.text,
                "preco": preco.text,
                "link": url
            })

    return produtos