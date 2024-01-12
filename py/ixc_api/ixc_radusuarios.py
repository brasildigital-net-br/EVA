import requests
import json
import os
from dotenv import load_dotenv as env
###################Logical information################

# Trata a url que vai ser usada para consulta do radius do cliente https://{ixc_host}/webservice/v1/radusuarios
def get_radius_data_ixc_brasil(client_id, base):
    env("../.env")

     # Estrutura de decisão de base a partir do input get_client_data()
    if base == "0001": #Brasil Digital
        ixc_host = os.getenv('IXC_BRASILDIGITAL_URI')
        ixc_login = os.getenv('IXC_LOGIN')
        ixc_aut = os.getenv('Authorization_142')
    elif base == "0002": # Candeias
        ixc_host = os.getenv('IXC_CANDEIASNET_URI')
        ixc_login = os.getenv('IXC_LOGIN')
        ixc_aut = os.getenv('Authorization_142')
    elif base == "0003": #BR364
        ixc_host = os.getenv('IXC_BR364TELECOM_URI')
        ixc_login = os.getenv('IXC_LOGIN') 
        ixc_aut = os.getenv('Authorization_72')
    else:
        print("Não foi passado uma base valida.")       
        

    url = "https://{}/webservice/v1/{}".format(ixc_host, ixc_login)
            
    payload = json.dumps({
        "qtype": "radusuarios.id_cliente",
        "query": f"{client_id}",
        "page": "1"
    })

    headers = {
        'Authorization': ixc_aut,
        'Content-Type': 'application/json',
        'ixcsoft': 'listar',
    }

    client_data_brasil = requests.request("GET", url, headers=headers, data=payload)
  
    return client_data_brasil.json()

# Gets the customer's MAC ADDRESS
def data_client(client_data_brasil):
    mac_list = []
    registros = client_data_brasil['registros']
    for conexao in registros:
        mac_list.append(conexao['conexao'])
    mac_list = mac_list[0]
    return mac_list

# Gets the customer's IP
def data_client_ip(client_data_brasil):
    mac_list = []
    registros = client_data_brasil['registros']
    for conexao in registros:
        mac_list.append(conexao['ip'])
    mac_list = mac_list[0]
    return mac_list


