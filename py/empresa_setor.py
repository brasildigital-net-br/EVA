import requests
import json
import os
from dotenv import load_dotenv as env

############ GET DATA FROM IXC API ###########################

# Link de consulta para https://{ixc_host}/webservice/v1/cliente
def get_client_data_ixc(id, base):
    env(".env")

    # Estrutura de decisão de base a partir do input get_client_data()
    if base == "0001": #Brasil Digital
        ixc_host = os.getenv('IXC_BRASILDIGITAL_URI')
        ixc_setor = os.getenv('IXC_SETOR')
        ixc_aut = os.getenv('Authorization_142')
    elif base == "0002": # Candeias
        ixc_host = os.getenv('IXC_CANDEIASNET_URI')
        ixc_setor = os.getenv('IXC_SETOR')
        ixc_aut = os.getenv('Authorization_142')
    elif base == "0003": #BR364
        ixc_host = os.getenv('IXC_BR364TELECOM_URI')
        ixc_setor = os.getenv('IXC_SETOR') 
        ixc_aut = os.getenv('Authorization_72')
    else:
        print("Não foi passado uma base valida.")       
        

    url = "https://{}/webservice/v1/{}".format(ixc_host, ixc_setor)

            
    payload = json.dumps({
        "qtype": "empresa_setor.id_depto",
        "query": f"{id}",
        "oper": "=",
        "rp": "9999999"
    })

    headers = {
        'Authorization': ixc_aut,
        'Content-Type': 'application/json',
        'ixcsoft': 'listar',
    }

    client_info = requests.request("GET", url, headers=headers, data=payload)

  
    return client_info.json()


###
def client_name(client_data_brasil):
    info_name = []
    registros = client_data_brasil['registros']
    for setor in registros:
        info_name.append(setor['setor'])
    return info_name