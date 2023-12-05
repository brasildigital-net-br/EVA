import requests
import json
import os
import datetime
import pyperclip
import re
from dotenv import load_dotenv as env

env(".env")

def criar_pasta_atendimentos():
    documentos_dir = os.path.expanduser("~/Documents")
    atendimentos_dir = os.path.join(documentos_dir, "Atendimentos")
    if not os.path.exists(atendimentos_dir):
        os.makedirs(atendimentos_dir)
    return atendimentos_dir

# Cria uma arvore de logs Ano/mes/dia/Relatorio
def criar_pasta_data(atendimentos_dir):
    data_atual = datetime.datetime.now()
    ano = str(data_atual.year)
    mes = str(data_atual.month).zfill(2)
    dia = str(data_atual.day).zfill(2)
    pasta_data = os.path.join(atendimentos_dir, ano, mes, dia)
    if not os.path.exists(pasta_data):
        os.makedirs(pasta_data)
    return pasta_data

# Ler arquivo dentro de Documents/Ano/mes/dia/counter e adiciona uma linha nova baseada em quantos relatorios foi gerado naquele dia OS
def ler_contador(pasta_data):
    contador_file = os.path.join(pasta_data, "contador.txt")
    try:
        with open(contador_file, "r") as arquivo:
            return int(arquivo.read())
    except FileNotFoundError:
        return 0

# Ler arquivo dentro de Documents/Ano/mes/dia/counter e adiciona uma linha nova baseada em quantos relatorios foi gerado naquele dia OS
def atualizar_contador(pasta_data, contador):
    contador_file = os.path.join(pasta_data, "contador.txt")
    with open(contador_file, "w") as arquivo:
        arquivo.write(str(contador))

##############################################################

def get_client_data():
    client_data = input("Enter the client data here:")
    id = [a for a in client_data.split('.') if a]

    return client_data

def get_client_id(client_data):
    client_id = client_data
    id = [a for a in client_id.split('.') if a]
    print(id[0])
    client_id = id[0]
    #s.split('mango', 1)[1]
    return client_id


def get_client_base(client_data):
    client_base = client_data
    base = [a for a in client_base.split('.') if a]
    base = base[1]
    print(base)
    return base



############ GET DATA FROM IXC API ###########################

def get_radius_data_ixc_brasil(client_id):

    url = "https://ixc.brasildigital.net.br/webservice/v1/radusuarios"
        
    
    payload = json.dumps({
        "qtype": "radusuarios.id_cliente",
        "query": f"{client_id}",
        "page": "1"
    })

    headers = {
        'Authorization': '*',
        'Content-Type': 'application/json',
        'ixcsoft': 'listar',
        'Cookie': '*'
    }

    client_data_brasil = requests.request("GET", url, headers=headers, data=payload)

    #print(client_data.json())
    return client_data_brasil.json()


def data_client(client_data_brasil):
    mac_list = []
    registros = client_data_brasil['registros']
    for conexao in registros:
        mac_list.append(conexao['conexao'])
    return mac_list


def data_client_ip(client_data_brasil):
    mac_list = []
    registros = client_data_brasil['registros']
    for conexao in registros:
        mac_list.append(conexao['ip_aviso'])
    return mac_list



if __name__ == '__main__':


    client_data = get_client_data()
    client_id = get_client_id(client_data)
    client_base = get_client_base(client_data)
    client_data_brasil = get_radius_data_ixc_brasil(client_id)
    mac_list = data_client(client_data_brasil)
    ip = data_client_ip(client_data_brasil)
    print(f"The connection value for client {client_id} is {mac_list} and the ip is: {ip}")


 
