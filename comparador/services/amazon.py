import requests
from bs4 import BeautifulSoup

def buscar_amazon(query):
    url = f"https://www.amazon.com.br/s?k={query}"

    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, "html.parser")

    produtos = []

    for item in soup.select(".s-result-item")[:5]:
        titulo = item.select_one("h2 span")
        preco = item.select_one(".a-price-whole")

        if titulo and preco:
            produtos.append({
                "site": "Amazon",
                "titulo": titulo.text,
                "preco": preco.text,
                "link": "https://amazon.com.br"
            })

    return produtos