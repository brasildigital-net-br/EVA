import json

with open("ip_in_use.json", encoding='utf-8') as f:
    dados = json.load(f)

dados = dados['prefixos']
for i in dados:
    if i["Disponibilidade"] == None:
        print("can use " + i["ip"])

