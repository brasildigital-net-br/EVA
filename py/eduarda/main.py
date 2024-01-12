import py.streamlit.validator_ip as validator_ip

ip = str("168.205.124.0")
data = validator_ip.validator_in_infra(ip)
print(data)

resultados = {"prefixos": [{"ip": prefixo["ip"]} for prefixo in data["prefixos"] if prefixo["Disponibilidade"] is None]}
        
if not resultados["prefixos"]:
    print("Pode usar")    
else:
    print("Cant use")
