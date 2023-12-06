import requests
import json
import os
from dotenv import load_dotenv as env

############ GET DATA FROM IXC API ###########################

# Link de consulta para https://{ixc_host}/webservice/v1/cliente
def get_client_data_ixc(client_id, base):
    env(".env")

    # Estrutura de decisão de base a partir do input get_client_data()
    if base == "0001": #Brasil Digital
        ixc_host = os.getenv('IXC_BRASILDIGITAL_URI')
        ixc_clientes = os.getenv('IXC_CLIENTES')
        ixc_aut = os.getenv('Authorization_142')
    elif base == "0002": # Candeias
        ixc_host = os.getenv('IXC_CANDEIAS_URI')
        ixc_clientes = os.getenv('IXC_CLIENTES')
        ixc_aut = os.getenv('Authorization_142')
    elif base == "0003": #BR364
        ixc_host = os.getenv('IXC_BR364TELECOM_URI')
        ixc_clientes = os.getenv('IXC_CLIENTES') 
        ixc_aut = os.getenv('Authorization_72')
    else:
        print("Não foi passado uma base valida.")       
        

    url = "https://{}/webservice/v1/{}".format(ixc_host, ixc_clientes)

            
    payload = json.dumps({
        "qtype": "cliente.id",
        "query": f"{client_id}",
        "page": "1"
    })

    headers = {
        'Authorization': ixc_aut,
        'Content-Type': 'application/json',
        'ixcsoft': 'listar',
    }

    client_info = requests.request("GET", url, headers=headers, data=payload)
  
    return client_info.json()

# Gets the customer's name
def client_name(client_data_brasil):
    info_name = []
    registros = client_data_brasil['registros']
    for razao in registros:
        info_name.append(razao['razao'])
    info_name = info_name[0]
    return info_name

# Gets the customer`s contract ID
def client_id(client_data_brasil):
    info_contrato = []
    registros = client_data_brasil['registros']
    for id in registros:
        info_contrato.append(id['id'])
    info_contrato = info_contrato[0]
    return info_contrato

# Gets the costumer`s cnpj or cpf
def client_code(client_data_brasil):
    info_code = []
    registros = client_data_brasil['registros']
    for cnpj_cpf in registros:
        info_code.append(cnpj_cpf['cnpj_cpf'])
    info_code = info_code[0]
    return info_code

# Gets the customer's phone
def client_cel(client_data_brasil):
    info_cel = []
    registros = client_data_brasil['registros']
    for telefone_celular in registros:
        info_cel.append(telefone_celular['telefone_celular'])
    info_cel = info_cel[0]
    return info_cel

# Gets the costumer`s house number
def client_hnumber(client_data_brasil):
    info_hnumber = []
    registros = client_data_brasil['registros']
    for numero in registros:
        info_hnumber.append(numero['numero'])
    info_hnumber = info_hnumber[0]
    return info_hnumber

# Gets the costumer`s postal code
def client_pc(client_data_brasil):
    info_cep = []
    registros = client_data_brasil['registros']
    for cep in registros:
        info_cep.append(cep['cep'])
    info_cep = info_cep[0]
    return info_cep

# Gets the costumer`s bairro :)
def client_bairro(client_data_brasil):
    info_bairro = []
    registros = client_data_brasil['registros']
    for bairro in registros:
        info_bairro.append(bairro['bairro'])
    info_bairro = info_bairro[0]
    return info_bairro

def client_cidade(client_data_brasil):
    info_cidade = []
    registros = client_data_brasil['registros']
    for cidade in registros:
        info_cidade.append(cidade['cidade'])
    info_cidade = info_cidade[0]
    return info_cidade

def client_estado(client_data_brasil):
    info_estado = []
    registros = client_data_brasil['registros']
    for uf in registros:
        info_estado.append(uf['uf'])
    info_estado = info_estado[0]
    return info_estado


def client_complemento(client_data_brasil):
    info_complemento = []
    registros = client_data_brasil['registros']
    for complemento in registros:
        info_complemento.append(complemento['complemento'])
    info_complemento = info_complemento[0]
    return info_complemento








