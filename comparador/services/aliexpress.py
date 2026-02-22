import requests
from bs4 import BeautifulSoup

def buscar_aliexpress(query):
    url = f"https://www.aliexpress.com/wholesale?SearchText={query}"

    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    produtos = []

    for item in soup.select(".manhattan--container--1lP57Ag")[:5]:
        titulo = item.select_one("h1, h3")
        preco = item.select_one(".price")

        if titulo and preco:
            produtos.append({
                "site": "AliExpress",
                "titulo": titulo.text,
                "preco": preco.text,
                "link": url
            })

    return produtos