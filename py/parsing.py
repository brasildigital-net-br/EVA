import paramiko
import time
import re
from dotenv import load_dotenv as env
import os

if __name__ == '__main__':
    env(".env")

    ip_h = os.getenv('huawei')
    port = os.getenv('port')
    id_login = os.getenv('id_login')
    passw = os.getenv('pass')



    ip_list = [

            "45.179.86.0", 
            "168.205.124.0",
            "168.205.125.0", 
            "168.205.126.0", 
            "177.221.57.0",
            "187.236.239.128",

        ]

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

        commands.send("display ip routing-table {} 25 longer-match\n".format(ip))
        time.sleep(.9)
        output = commands.recv(65535)
        output = output.decode("utf-8")

        pattern = re.compile(r'\b(\d+\.\d+\.\d+\.\d+/\d+)\b')

        matches = pattern.findall(output)

        matches_len = len(matches)

        if matches_len == 0:
            print("==========| Range {} se encontra sem ips em uso |==========".format(ip))
        else:
            with open("output.txt", 'a') as f:
                for match in matches:
                    f.write("{}\n".format(match))
    
