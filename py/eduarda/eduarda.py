import sys
sys.path.append('../ixc_api/')
import ixc_ip
import ixc_client
import ixc_locked_ip
from dotenv import load_dotenv as env
import os
import json
from alive_progress import alive_bar
import socket,sys
import datetime


##################################### E D U A R D A ###########################################

if __name__ == '__main__':
    env("../.env")

    # VARS DE CONSULTA
    ixc_brd = os.getenv('IXC_BRASILDIGITAL_URI')
    ixc_cd = os.getenv('IXC_CANDEIASNET_URI')
    ixc_364 = os.getenv('IXC_BR364TELECOM_URI')

    aut_brd = os.getenv("Authorization_142")
    aut_cd = os.getenv("Authorization_142")
    aut_364 = os.getenv("Authorization_72")

    host = [ixc_brd, ixc_cd, ixc_364]
    aut = [aut_brd, aut_cd, aut_364]

    zip = list(zip(host, aut))

    # Passando os prefixo como argumento.
    # ip_list = []
    # arg = sys.argv[1]
    # ip_list.append(arg)
    

    ip_list = [

        "45.179.86.0/25", 
        "168.205.124.0/25",
        "168.205.125.0/25", 
        "168.205.126.0/25", 
        "177.221.57.0/25",
        "187.236.239.128/25", 

    ]

    #ip = input("Insiria o ip com o pref:")

    ip = ""

    ip_result = {"prefixos": []}



    for i in ip_list:
        ip = i

        range_ipv4 = ixc_locked_ip.const_prefix(ip)

        with alive_bar(len(range_ipv4), title='Consultando IPs do prefixo {}'.format(ip)) as bar:  
            print(" ")
            for ipv4 in range_ipv4:
            
                if ixc_locked_ip.block_ip(ipv4) == True:
                    print("IP {} RESERVADO!".format(ipv4))
                elif ipv4 == "8.8.8.8":
                    print("Deixa a Google em paz rapaz!")
                else:
                    for h, a in zip:
                        ip_consulting = ixc_ip.get_radius_data_ixc_brasil(ipv4, h, a)
                        mostra_ip = int(ixc_ip.ip_list(ip_consulting))
        
                        if mostra_ip == 0:
                            #print("IP LIVRE: {}  BASE {}".format(ipv4, h))
                            if h == "ixc.brasildigital.net.br":
                                brd = False
                            elif h == "ixc.candeiasnet.com.br":
                                cd = False 
                            elif h == "ixc.br364telecom.com.br":
                                br364 = False
                            else:
                                print("")
                        elif mostra_ip > 0:
                            #print("IP {} EM USO NA BASE {}".format(ipv4, h))
                            if h == "ixc.brasildigital.net.br":
                                brd = True
                            elif h == "ixc.candeiasnet.com.br":
                                cd = True
                            elif h == "ixc.br364telecom.com.br":
                                br364 = True
                            else:
                                print("")                
                bar()
                
                now = datetime.date.today()
                # Escreve as info dos ips em uso
                ip_result["prefixos"].append(
                    {
                    "ip": ipv4,
                    "Range": ip,
                    "huawei": "",
                    "ixc.brasildigital.net.br": brd,
                    "ixc.candeiasnet.com.br": cd,
                    "ixc.br364telecom.com.br": br364,
                    "Disponibilidade": None,
                    "LastTimeRunning": "{}".format(now)
                    }
                )
                
                with open('../json/ip_result.json', 'w') as f:
                    json.dump(ip_result, f, indent=3)





'''

1 - 177.221.57.0/25 
2 - 168.205.124.0/25 
3 - 168.205.125.0/25 
4 - 168.205.126.0/25 
5 - 45.179.86.0/25   
6 - 187.236.239.128/25
7 - 168.205.126.0/25



    ip_list = [

        "45.179.86.0/25", 
        "168.205.124.0/25",
        "168.205.125.0/25", 
        "168.205.126.0/25", 
        "177.221.57.0/25",
        "187.236.239.128/25", 

    ]

ip = ["177.221.57.0/25", "168.205.124.0/25", "168.205.125.0/25", "168.205.126.0/25", "45.179.86.0/25", "187.236.239.128/25", "168.205.126.0/25"]


log(2)2688 == 11

2688

Criar um json para cada prefixo 



177.221.57.0/25 - Vai do 177.221.57.0 até o 177.221.57.127 - usar em clientes cnpj
168.205.124.0/25 - vai do 168.205.124.0 até o 168.205.124.127 - usar em clientes cnpj
168.205.125.0/25 - vai do 168.205.125.0 até o 168.205.125.127 - usar em clientes cnpj
168.205.126.0/25 -  vai do 168.206.126.0 até o 168.205.126.126 - usar em clientes cpf
45.179.86.0/25   - vai do 45.179.86.0 até o 45.179.86.127 - usar em clientes cnpj
187.236.239.128/25 - vai do 187.63.239.128 até o 187.236.255 - usar em clientes cnpj


168.205.126.0/25 -  vai do 168.206.126.0 até o 168.205.126.126 - usar em clientes cpf



'''