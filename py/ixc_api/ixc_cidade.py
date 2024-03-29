import requests
import json
import os
from dotenv import load_dotenv as env

###################Logical information################

# Trata a url que vai ser usada para consulta do radius do cliente https://{ixc_host}/webservice/v1/radusuarios
def get_cidade_data_ixc(cidade_id, base):
    env("../.env")

     # Estrutura de decisão de base a partir do input get_client_data()
    if base == "0001": #Brasil Digital
        ixc_host = os.getenv('IXC_BRASILDIGITAL_URI')
        ixc_cidade = os.getenv('IXC_CIDADE')
        ixc_aut = os.getenv('Authorization_142')
    elif base == "0002": # Candeias
        ixc_host = os.getenv('IXC_CANDEIASNET_URI')
        ixc_cidade = os.getenv('IXC_CIDADE')
        ixc_aut = os.getenv('Authorization_142')
    elif base == "0003": #BR364
        ixc_host = os.getenv('IXC_BR364TELECOM_URI')
        ixc_cidade = os.getenv('IXC_CIDADE') 
        ixc_aut = os.getenv('Authorization_72')
    else:
        print("Não foi passado uma base valida.")       
        

    url = "https://{}/webservice/v1/{}".format(ixc_host, ixc_cidade)
            
    payload = json.dumps({
        "qtype": "cidade.id",
        "query": f"{cidade_id}",
        "oper": "=",
        "page": "1",
        "rp": "1",
        "sortname": "cidade.id",
        "sortorder": "asc"

        # "qtype": "cidade.id",
        # "query": f"{client_id}",
        # "page": "1"
    })

    headers = {
        'Authorization': ixc_aut,
        'Content-Type': 'application/json',
        'ixcsoft': 'listar',
    }

    client_data_brasil = requests.request("GET", url, headers=headers, data=payload).json()

    cidade_nome = []

    registros = client_data_brasil['registros']
    for nome in registros:
        cidade_nome.append(nome['nome'])
    cidade_nome = cidade_nome[0]
    
    return cidade_nome




