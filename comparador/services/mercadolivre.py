import requests

def buscar_mercadolivre(query):
    url = f"https://api.mercadolibre.com/sites/MLB/search?q={query}"

    response = requests.get(url)
    data = response.json()

    results = []
    for item in data.get("results", [])[:5]:
        results.append({
            "site": "Mercado Livre",
            "titulo": item["title"],
            "preco": item["price"],
            "link": item["permalink"],
            "imagem": item["thumbnail"]
        })

    return results