import paramiko
import time
import re
from dotenv import load_dotenv as env
import os
from alive_progress import alive_bar

if __name__ == '__main__':
    env(".env")

    ip = os.getenv('huawei')
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

        #with alive_bar(len(ip_list),title='Consultando IPs do prefixo {}'.format(ip)) as bar: 

        conn = paramiko.SSHClient()          # High-level representation of a session with an SSH server
        conn.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # When 1st connection, ask to trust this server or not
                                                                    # Change SSH key authentication as "Trust All". Add untrusted hosts
        conn.connect("10.200.1.200", 50022, "####", "#####")        # Initiate SSH connection with IP, Port, Username, Password

        commands = conn.invoke_shell()       # Request an interactive shell session on this channel.

        commands.send("screen-length 0 temporary\n")    # Send command to device
        time.sleep(.5)                       # Wait for 0.5seconds
        output = commands.recv(65535)        # .recv() - The maximum amount of data to be received at once is specified by nbytes
        output = output.decode("utf-8")      # Change file type from bytes to string
        #print (output)

        commands.send("display ip routing-table {} 25 longer-match\n".format(ip))
        time.sleep(.5)
        output = commands.recv(65535)
        output = output.decode("utf-8")
        #print (output)


        #file = open("output.txt", "a")


        pattern = re.compile(r'\b(\d+\.\d+\.\d+\.\d+/\d+)\b')

        matches = pattern.findall(output)

        print(len(matches))

        matches_len = len(matches)

        if matches_len == 0:
            print("qualfoifilho")
        else:
            with open("output.txt", 'a') as f:
                for match in matches:
                    f.write("{}\n".format(match))
    
    #file.close()




# commands.send("display alarm all \n")
# time.sleep(.5)
# output = commands.recv(65535)
# output = output.decode("utf-8")
# print (output)


# commands.send("sys \n")
# commands.send( "interface g0/1/3 \n")
# commands.send( "undo shutdown \n")
# commands.send( "di th \n")
# time.sleep(.5)
# output = commands.recv(65535)
# output = output.decode("utf-8")
# print (output)