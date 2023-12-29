#!/bin/bash


h="10.200.1.200"
port=50022  
user="***"
pass="****"
ARQUIVO_SAIDA="output.txt"
ARQUIVO_IPS="ips.txt"
ip="45.179.86.0"
range="25"

no_page="screen-length 0 temporary"

cli="display ip routing-table "$ip" "$range" longer-match" 


#        "45.179.86.0/25", 
#        "168.205.124.0/25",
#        "168.205.125.0/25", 
#        "168.205.126.0/25", 
#        "177.221.57.0/25",
#        "187.236.239.128/25", 

sshpass -p "$pass" ssh -p "$port" "$user@$h" "$no_page" "$cli" | grep -E -o "([0-9]{1,3}[\.]){3}[0-9]{1,3}" > "$ARQUIVO_IPS"

if [ $? -eq 0 ]; then
  echo "Comando executado com sucesso. IPs filtrados salvos em $ARQUIVO_IPS"
else
  echo "Erro ao executar o comando via SSH ou ao filtrar IPs."
fi

# [] - Criar um foreach para todos os ips do json?
# [] - Devo executar primeiro o python ou o parsing.sh?
# []
#
#
#
#
#
