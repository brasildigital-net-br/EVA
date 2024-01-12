import requests
import json
import os
from dotenv import load_dotenv as env
import yasmin

###################Logical information################

# Trata a url que vai ser usada para consulta do radius do cliente https://{ixc_host}/webservice/v1/radusuarios
def get_estado_data_ixc(estado_id, base):
    env("../.env")

     # Estrutura de decisão de base a partir do input get_client_data()
    if base == "0001": #Brasil Digital
        ixc_host = os.getenv('IXC_BRASILDIGITAL_URI')
        ixc_estado = os.getenv('IXC_ESTADO')
        ixc_aut = os.getenv('Authorization_142')
    elif base == "0002": # Candeias
        ixc_host = os.getenv('IXC_CANDEIAS_URI')
        ixc_estado = os.getenv('IXC_ESTADO')
        ixc_aut = os.getenv('Authorization_142')
    elif base == "0003": #BR364
        ixc_host = os.getenv('IXC_BR364TELECOM_URI')
        ixc_ESTADO = os.getenv('IXC_ESTADO') 
        ixc_aut = os.getenv('Authorization_72')
    else:
        print("Não foi passado uma base valida.")       
        

    url = "https://{}/webservice/v1/{}".format(ixc_host, ixc_estado)
            
    payload = json.dumps({

        "qtype": "uf.id",
        "query": f"{estado_id}",
        "oper": "=",
        "page": "1",
        "rp": "1",
        "sortname": "uf.id",
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

    client_estado = requests.request("GET", url, headers=headers, data=payload).json()

    estado_nome = []

    # Gets the costumers Estado
    registros = client_estado['registros']
    for sigla in registros:
        estado_nome.append(sigla['sigla'])
    estado_nome = estado_nome[0]
    return estado_nome




