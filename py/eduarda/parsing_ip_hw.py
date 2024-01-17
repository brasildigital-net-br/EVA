import sys

sys.path.append('../ixc_api/')

import paramiko
import time
import re
from dotenv import load_dotenv as env
import os
from alive_progress import alive_bar


with open("output.txt", 'w') as f:
    f.write("")


if __name__ == '__main__':
    env("../.env")

    ip_h = os.getenv('huawei')
    port = os.getenv('port')
    id_login = os.getenv('id_login')
    passw = os.getenv('pass')

    # ip_list = []
    # arg = sys.argv[1]
    # ip_list.append(arg)

    ip_list = [

            "45.179.86.0", 
            # "168.205.124.0",
            # "168.205.125.0", 
            # "168.205.126.0", 
            # "177.221.57.0",
            # "187.236.239.128",

        ]
    
    with alive_bar(len(ip_list), title='Reealizando o Parsin no huawei') as bar:  
        for i in ip_list:
            ip = i

            conn = paramiko.SSHClient()          
            conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())  
                                                                        
            conn.connect(ip_h, port, id_login, passw)        

            commands = conn.invoke_shell()       

            commands.send("screen-length 0 temporary\n")   
            time.sleep(.9)                       
            output = commands.recv(65535)        
            output = output.decode("utf-8")      

            #print(output)

            commands.send("display ip routing-table {} 25 longer-match\n".format(ip))
            time.sleep(.9)
            output = commands.recv(65535)
            output = output.decode("utf-8")

            #print(output)

            pattern = re.compile(r'\b(\d+\.\d+\.\d+\.\d+/\d+)\b')

            matches = pattern.findall(output)

            #matches = set(matches) 


            matches_len = len(matches)

            if matches_len == 0:
                print("==========| Range {} se encontra sem ips em uso |==========".format(ip))
            else:
                with open("../output/output.txt", 'a') as f:
                    for match in matches:
                        match = match.split("/", 1)[0]
                        #print(match)
                        f.write("{}\n".format(match))
                        
            bar()

        seen = set()
        with open('../output/output.txt') as infile:
            with open('../output/sample.txt', 'w') as outfile:
                for line in infile:
                    if line not in seen:
                        outfile.write(line)
                        seen.add(line)