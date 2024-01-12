import json
import os
from dotenv import load_dotenv as env
import sys
sys.path.append('../ixc_api/')
sys.path.append('../streamlit/')
import ixc_ip
import paramiko
import time
import re
import requests


def validator_in_base():
    with open("../json/ip_in_use.json", encoding='utf-8') as f:
        dados = json.load(f)


    dados = dados['prefixos']
    for i in dados:
        if i["Disponibilidade"] == None:
            print("can use " + i["ip"])


def validator_in_infra(i):
    ip = i

    env("../.env")

    # VARS DE CONSULTA DO IXC
    ixc_brd = os.getenv('IXC_BRASILDIGITAL_URI')
    ixc_cd = os.getenv('IXC_CANDEIASNET_URI')
    ixc_364 = os.getenv('IXC_BR364TELECOM_URI')

    aut_brd = os.getenv("Authorization_142")
    aut_cd = os.getenv("Authorization_142")
    aut_364 = os.getenv("Authorization_72")

    host = [ixc_brd, ixc_cd, ixc_364]
    aut = [aut_brd, aut_cd, aut_364]

    # VAR DE CONSULTA DO HW

    ip_h = os.getenv('huawei')
    port = os.getenv('port')
    id_login = os.getenv('id_login')
    passw = os.getenv('pass')


    #ip = "168.205.124.66"

    ip_result = {"prefixos": []}

    zip_data = zip(host, aut)

    # VALIDACAO NAS BASES DO IXC

    for h, a in zip_data:
        ip_consult = ixc_ip.get_radius_data_ixc_brasil(ip, h, a)
        mostra_ip = int(ixc_ip.ip_list(ip_consult))
        if mostra_ip == 0:
            if h == "ixc.brasildigital.net.br":
                brd = False
            elif h == "ixc.candeiasnet.com.br":
                cd = False 
            elif h == "ixc.br364telecom.com.br":
                br364 = False
            else:
                print("")
        elif mostra_ip > 0:
            if h == "ixc.brasildigital.net.br":
                brd = True
            elif h == "ixc.candeiasnet.com.br":
                cd = True
                print("alo")
            elif h == "ixc.br364telecom.com.br":
                br364 = True
            else:
                print("") 


    ip_result["prefixos"].append(
        {
        "ip": ip,
        "huawei": "",
        "ixc.brasildigital.net.br": brd,
        "ixc.candeiasnet.com.br": cd,
        "ixc.br364telecom.com.br": br364,
        "Disponibilidade": None
        }
    )

    # VALIDACAO NO HW

    conn = paramiko.SSHClient()          
    conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
                                                                
    conn.connect(ip_h, port, id_login, passw)        

    commands = conn.invoke_shell()       

    commands.send("screen-length 0 temporary\n")   
    time.sleep(.9)                       
    output = commands.recv(65535)        
    output = output.decode("utf-8")      

    commands.send("display ip routing-table {} \n".format(ip))
    time.sleep(.9)
    output = commands.recv(65535)
    output = output.decode("utf-8")

    pattern = re.compile(r'\b(\d+\.\d+\.\d+\.\d+/\d+)\b')

    matches = pattern.findall(output)




    matches_len = len(matches)


    print(ip_result)

    print(matches)




    # validate the ip:
    data = ip_result

    ips_txt = matches

    huawei_ips = [
        "ixc.brasildigital.net.br",
        "ixc.candeiasnet.com.br",
        "ixc.br364telecom.com.br"
    ]


    for item in data['prefixos']:
            ip = item['ip']

            if any(item[key] for key in item.keys() if key.startswith('ixc.')):
                item['Disponibilidade'] = True

            for huawei_ip in huawei_ips:
                if item.get(huawei_ip, False) == True or ip in ips_txt:
                    item['huawei'] = ip
                    item['Disponibilidade'] = True
                    break

    #print(data)
    return data




# if __name__ == '__main__':
#     env("../.env")

#     # VARS DE CONSULTA DO IXC
#     ixc_brd = os.getenv('IXC_BRASILDIGITAL_URI')
#     ixc_cd = os.getenv('IXC_CANDEIASNET_URI')
#     ixc_364 = os.getenv('IXC_BR364TELECOM_URI')

#     aut_brd = os.getenv("Authorization_142")
#     aut_cd = os.getenv("Authorization_142")
#     aut_364 = os.getenv("Authorization_72")

#     host = [ixc_brd, ixc_cd, ixc_364]
#     aut = [aut_brd, aut_cd, aut_364]

#     # VAR DE CONSULTA DO HW

#     ip_h = os.getenv('huawei')
#     port = os.getenv('port')
#     id_login = os.getenv('id_login')
#     passw = os.getenv('pass')


#     #ip = "168.205.124.66"

#     ip_result = {"prefixos": []}

#     #zip_data = zip(host, aut)

