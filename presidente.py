import requests
import json


def buscar_dados():
    request = requests.get(
        "https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json")
    todos = json.loads(request.content)
    valor = todos["cand"]
    for item in valor:
        print(item['nm'])
        print("Votos:"+item['vap'])
        print(item['pvap']+"%\n")


buscar_dados()
