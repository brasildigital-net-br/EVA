import requests
import json
import os
from dotenv import load_dotenv as env
###################Logical information################

# Trata a url que vai ser usada para consulta do radius do cliente https://{ixc_host}/webservice/v1/radusuarios
def get_radius_data_ixc_brasil(ip, ixc_host, ixc_aut):
    env("../.env")

     # Estrutura de decisão de base a partir do input get_client_data()

    url = "https://{}/webservice/v1/radusuarios".format(ixc_host)
            
    payload = json.dumps({
        "rp": "9999999", # O ceu e o limite
        "qtype": "radusuarios.ip",
        "query": f"{ip}",
        "oper":"=",
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
def ip_list(client_data_brasil):
    ip_list = []
    total = client_data_brasil['total']
    ip_list = total
    return total

# Gets the total of ips in ixc
def total_ip(client_data_brasil):
    ip = []
    registros = client_data_brasil['registros']
    for ip in registros:
        ip.append(ip['ip'])
    return ip

# Gets the client id in ixc
def client_id(client_data_brasil):
    info_contrato = []
    registros = client_data_brasil['registros']
    for id_cliente in registros:
        info_contrato.append(id_cliente['id_cliente'])
    return info_contrato


