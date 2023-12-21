import paramiko
import time

host = "10.200.1.200"
port = 50022  
username = "**"
password = "**"
command = "display ip routing-table 45.179.86.0 25 longer-match"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port=port, username=username, password=password)

channel = ssh.invoke_shell()

channel.send(command + "\n")

time.sleep(0.5)

output = ""
while True:
    if channel.recv_ready():
        output += channel.recv(4096).decode("utf-8")
        if "---- More ----" in output:
            channel.send(" ")
        else:
            break

with open("output.txt", "w") as f:
    f.write(output)

channel.close()
ssh.close()

print("Comando executado com sucesso. Saída salva em output.txt")
