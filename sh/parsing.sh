#!/bin/bash


h="10.200.1.200"
port=50022  
user="***"
pass="***"
cli="display ip routing-table 45.179.86.13 32"
ARQUIVO_SAIDA="output.txt"
ARQUIVO_IPS="ips.txt"

sshpass -p "$pass" ssh -p "$port" "$user@$h" "$cli" | grep -E -o "([0-9]{1,3}[\.]){3}[0-9]{1,3}" > "$ARQUIVO_IPS"

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
'
matrix = {pref[ips], pref[ips], pref[ips]}

consulta o ip_json?



For each ip in data

'