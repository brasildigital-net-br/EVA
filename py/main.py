import json
 


##################### Ambiente de Dev ######################
f = open('ip_result.json')

data = json.load(f)

print(data)
json_formatted_str = json.dumps(data, indent=2)

#print(json_formatted_str)
#print(json_formatted_str)


def filtrar_campos_true(json_data):
    resultados = []
    
    for prefixo in json_data["prefixos"]:
        for campo, valor in prefixo.items():
            if valor is True:
                resultados.append({campo: valor})
    
    return resultados

data = "caminho/do/seu/arquivo.json"  # Substitua pelo caminho real do seu arquivo JSON
with open(data, "r") as arquivo:
    dados_json = json.load(arquivo)

resultados_filtrados = filtrar_campos_true(dados_json)

print("Campos com valor True:")
for resultado in resultados_filtrados:
    print(resultado)






with open('ip_result.json') as f:
    data = json.load(f)
contem = False

for state in data["jquery"]:
    if (argumento[2] == state['version']):
        contem = True

if (contem):
    print(state['name'], state['version'] + "existe")
else:
    print("nao tem")



ip_livre = []
registros = data['prefixos']
for ip in registros:
    ip_livre.append(data["ixc.brasildigital.net.br"])
info_cidade = ip_livre[0]

print(info_cidade)



for i in data['prefixos']:
    if "ixc.brasildigital.net.br" == False and "ixc.candeiasnet.com.br"  == False and "ixc.br364telecom.com.br" == False:
        print(i)

f.close()