import socket
import re

# Configurações do servidor

# 172.30.0.201 9833 netnumem casesensiteve uppercase

# 172.30.0.200 3337 UNM minusculo 1024
host = '172.30.0.200'  # endereço do servidor
port = 3337  # porta do servidor
#ZTEGc44dca49 ZTEGd103853b  ZTEGD103853B
# Comandos a serem enviados
# Exemplo de lista de comandos, substitua pelos comandos desejados
#LOGIN:::CTAG::UN=marcusteixeira,PWD=BRD$1455;
#LOGIN:::CTAG::UN=admin,PWD=admin;
commands = ['LOGIN:::CTAG::UN=admin,PWD= ;',
            'QUERY-ONUINFO::ONUIDTYPE=MAC,ONUID=ZTEGd1e63066:CTAG::;']

# Criação do socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conexão com o servidor
client_socket.connect((host, port))

# Envio dos comandos em sequência
for command in commands:
    # Envio do comando
    client_socket.send(command.encode())

    # Recebimento da resposta do servidor
    response = client_socket.recv(1024).decode()
   
    # Exibição da resposta
    print('Resposta do servidor:', response)    

# Fechamento do socket
client_socket.close()


##################################################################################################

# Extrair o nome da OLT baseado na var commands
padrao_olt = r"(NOVA-MUTUM|NOVA MAMORE|PLANALTO GM|SAO-FRANCISCO|DOMPEDRO|BAIRRO-NOVO|UNIAO-BANDEIRANTE|GLOBOFIBER|GLOBOFIBER-II?|CANDEIAS|ECOVILE|ECOVILE-II?|ECOVILE-III?|ELDORADO|VILA-VERDE|VILA-VERDE-II?|JMB|TRANSAMAZONICA|ITAPUA|NOVO HORIZONTE)"
resultado_olt = re.search(padrao_olt, response)
olt = resultado_olt.group(0).strip() if resultado_olt else None

# Extrair o MAC
padrao_mac = r"(?:FHTT|ZTEG|MKPG)[A-Za-z0-9]+"
resultado_mac = re.findall(padrao_mac, response)
mac = resultado_mac[0] if resultado_mac else None

# Extrair o SLOT
padrao_slot = r"\s+(\d+)\s+\d+\s+\d+\s+" + re.escape(mac)
resultado_slot = re.search(padrao_slot, response)
slot = resultado_slot.group(1) if resultado_slot else None

# Extrair o PON
padrao_pon = r"\s+\d+\s+(\d+)\s+\d+\s+" + re.escape(mac)
resultado_pon = re.search(padrao_pon, response)
pon = resultado_pon.group(1) if resultado_pon else None

# Extrair o OLTID
padrao_oltid = r"(?<=_)\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}(?=-)"
resultado_oltid = re.search(padrao_oltid, response)
oltid = resultado_oltid.group(0) if resultado_oltid else None


# Imprimir os resultados
print("OLT:", olt)
print("MAC EQ:", mac)
print("SLOT:", slot)
print("PON:", pon)
print("OLTID:", oltid)

############################################################################################################
# PEGA O SINAL DA FIBRA E DE RETORNO
commands = ['LOGIN:::CTAG::UN=admin,PWD=admin;',
            f'QUERY-ONUINFO::ONUIDTYPE=MAC,ONUID={mac}:CTAG::;',f'LST-OMDDM::OLTID={oltid},PONID=NA-NA-{slot}-{pon},ONUIDTYPE=MAC,ONUID={mac},PEERFLAG=True:CTAG::;']

# Criação do socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conexão com o servidor
client_socket.connect((host, port))

# Envio dos comandos em sequência
for command in commands:
    # Envio do comando
    client_socket.send(command.encode())

    # Recebimento da resposta do servidor
    response = client_socket.recv(1024).decode()
   
    # Exibição da resposta
    print('Resposta do servidor:', response)    

# Fechamento do socket
client_socket.close()

print(response)

padrao = r"-\d+\.\d+"

valores = re.findall(padrao, response)

##################### ONU FIBER SIGNAL 
if len(valores) >= 2:
    rx_value = valores[0]
    tx_value = valores[1]
    print("Rx:", rx_value)
    print("Tx:", tx_value)
else:
    print("Não foi possível encontrar os valores de Rx e Tx na entrada.")


#teste1 ZTEGc4486082 
#teste2 ZTEGd282a9c2
#BN ZTEGcf2395e0

#teste ONU ALARMADA ZTEGcf234008

#LST-CATVOPTPOWER::OLTID=10.171.0.106,PONID=NA-NA-12-9,ONUIDTYPE=MAC,ONUID=FHTT91fbe7c0:CTAG::;
#LST-CATVOPTPOWER::OLTID={oltid},PONID=NA-NA-{slot}-{pon},ONUIDTYPE=MAC,ONUID={mac}:CTAG::;
#LST-ONUSTATE::OLTID={oltid},PONID=NA-NA-{slot}-{pon},ONUIDTYPE=MAC,ONUID={mac}:CTAG::;' // pego o status, los, off e online
# PEGAR O Alarm Level

#PEGA O STATUS (LOS, UP, Power-Off)
commands = ['LOGIN:::CTAG::UN=admin,PWD=admin;',
            f'QUERY-ONUINFO::ONUIDTYPE=MAC,ONUID={mac}:CTAG::;',
            f'LST-ONUSTATE::OLTID={oltid},PONID=NA-NA-{slot}-{pon},ONUIDTYPE=MAC,ONUID={mac}:CTAG::;']

# Criação do socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conexão com o servidor
client_socket.connect((host, port))

# Envio dos comandos em sequência
for command in commands:
    # Envio do comando
    client_socket.send(command.encode())

    # Recebimento da resposta do servidor
    response = client_socket.recv(1024).decode()
   
    # Exibição da resposta
    print('Resposta do servidor:', response)    

# Fechamento do socket
client_socket.close()

print(response)

padrao_status = r"UP\s+(\w+-\w+|\w+)"

resultado = re.search(padrao_status, response)

if resultado:
    palavra = resultado.group(1)
    print("Palavra encontrada:", palavra)
else:
    print("Não foi possível encontrar a palavra na entrada.")