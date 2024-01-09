
# import json

# #json file
# jf = open("ip_result.json")
# data = json.load(jf)

# #print(data)
# prefixos = data['prefixos']
# print(prefixos)
# for d in prefixos:
#     print(d)

# #{ip[ixc123,dispo],ip[ixc123,dispo]}

# # .txt file
# with open('sample.txt') as f:
#     lines = f.readlines()

# # reading the lines values from txt
# for  d in prefixos:
#     for i in lines:
#         i = i.split("\n", 1)[0]
#         if i == d["ip"]:
#             print(d)
#             print("oq ta rolando")
    
#     #print(i)
# import json

# with open('ip_result.json', 'r') as json_file:
#     data = json.load(json_file)

# with open('sample.txt', 'r') as txt_file:
#     ips_txt = txt_file.readlines()

# for item in data['prefixos']:
#     ip = item['ip']
#     if any(item[key] for key in item.keys() if key.startswith('ixc.')):
#         item['Disponibilidade'] = True

# with open('ip_in_use.json', 'w') as json_file:
#     json.dump(data, json_file, indent=2)



# import json

# with open('ip_result.json', 'r') as json_file:
#     data = json.load(json_file)

# with open('sample.txt', 'r') as txt_file:
#     ips_txt = txt_file.read().splitlines()

# for item in data['prefixos']:
#     ip = item['ip']
#     if any(item[key] for key in item.keys() if key.startswith('ixc.')):
#         item['Disponibilidade'] = True
#     elif ip in ips_txt:
#         item['Disponibilidade'] = True

# with open('ip_in_use.json', 'w') as json_file:
#     json.dump(data, json_file, indent=2)


import json

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

