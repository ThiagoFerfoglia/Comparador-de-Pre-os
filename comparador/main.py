from fastapi import FastAPI, Query
from typing import List
import re

# IMPORTS DOS SERVIÇOS
from services.mercadolivre import buscar_mercadolivre
from services.amazon import buscar_amazon
from services.aliexpress import buscar_aliexpress
from services.shopee import buscar_shopee

app = FastAPI(title="API Comparador de Preços")

# -----------------------------------------
# FUNÇÃO PARA LIMPAR PREÇO
# -----------------------------------------
def limpar_preco(preco):
    try:
        if isinstance(preco, (int, float)):
            return float(preco)

        preco = str(preco)
        preco = preco.replace("R$", "").replace(".", "").replace(",", ".")
        preco = re.sub(r"[^\d.]", "", preco)

        return float(preco)
    except:
        return 9999999  # preço alto se falhar


# -----------------------------------------
# ROTA PRINCIPAL
# -----------------------------------------
@app.get("/")
def home():
    return {
        "status": "API rodando 🚀",
        "endpoint": "/buscar?produto=nome"
    }


# -----------------------------------------
# BUSCA DE PRODUTOS
# -----------------------------------------
@app.get("/buscar")
def buscar(produto: str = Query(..., description="Nome do produto")):

    resultados = []

    # MERCADO LIVRE
    try:
        resultados += buscar_mercadolivre(produto)
    except Exception as e:
        print("Erro Mercado Livre:", e)

    # AMAZON
    try:
        resultados += buscar_amazon(produto)
    except Exception as e:
        print("Erro Amazon:", e)

    # ALIEXPRESS
    try:
        resultados += buscar_aliexpress(produto)
    except Exception as e:
        print("Erro AliExpress:", e)

    # SHOPEE
    try:
        resultados += buscar_shopee(produto)
    except Exception as e:
        print("Erro Shopee:", e)

    # ORDENA POR PREÇO
    for item in resultados:
        item["preco_num"] = limpar_preco(item.get("preco"))

    resultados_ordenados = sorted(resultados, key=lambda x: x["preco_num"])

    # REMOVE CAMPO AUXILIAR
    for item in resultados_ordenados:
        del item["preco_num"]

    return {
        "produto": produto,
        "total_resultados": len(resultados_ordenados),
        "resultados": resultados_ordenados
    }