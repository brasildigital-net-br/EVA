import ixc_ip
import ixc_client
from dotenv import load_dotenv as env
import os
import ixc_locked_ip
import json
from alive_progress import alive_bar
import time
import re
import paramiko

##################################### E D U A R D A ###########################################

if __name__ == '__main__':
    env(".env")

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

    ip_h = os.getenv('huawei')
    port = os.getenv('port')
    id_login = os.getenv('id_login')
    passw = os.getenv('pass')


    ip_list_s = [

            "45.179.86.0", 
            "168.205.124.0",
            "168.205.125.0", 
            "168.205.126.0", 
            "177.221.57.0",
            "187.236.239.128",

        ]

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
                
                # Escreve as info dos ips em uso
                ip_result["prefixos"].append(
                    {
                    "ip": ipv4,
                    "Range": ip,
                    "huawei": "",
                    "ixc.brasildigital.net.br": brd,
                    "ixc.candeiasnet.com.br": cd,
                    "ixc.br364telecom.com.br": br364,
                    "Disponibilidade": None
                    }
                )
                
                with open('ip_result.json', 'w') as f:
                    json.dump(ip_result, f, indent=3)

    ## Parsin

    for i in ip_list_s:
        ip = i

        conn = paramiko.SSHClient()          
        conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
                                                                    
        conn.connect(ip_h, port, id_login, passw)        

        commands = conn.invoke_shell()       

        commands.send("screen-length 0 temporary\n")   
        time.sleep(.9)                       
        output = commands.recv(65535)        
        output = output.decode("utf-8")      

        commands.send("display ip routing-table {} 25 longer-match\n".format(ip))
        time.sleep(.9)
        output = commands.recv(65535)
        output = output.decode("utf-8")

        pattern = re.compile(r'\b(\d+\.\d+\.\d+\.\d+/\d+)\b')

        matches = pattern.findall(output)

        #matches = set(matches) 


        matches_len = len(matches)

        if matches_len == 0:
            print("==========| Range {} se encontra sem ips em uso |==========".format(ip))
        else:
            with open("output.txt", 'a') as f:
                for match in matches:
                    match = match.split("/", 1)[0]
                    #print(match)
                    f.write("{}\n".format(match))
                    


    seen = set()
    with open('output.txt') as infile:
        with open('sample.txt', 'w') as outfile:
            for line in infile:
                if line not in seen:
                    outfile.write(line)
                    seen.add(line)


    #Main
    with open('ip_result.json', 'r') as json_file:
        data = json.load(json_file)

    with open('sample.txt', 'r') as txt_file:
        ips_txt = txt_file.read().splitlines()

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

    with open('ip_in_use.json', 'w') as json_file:
        json.dump(data, json_file, indent=2)







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