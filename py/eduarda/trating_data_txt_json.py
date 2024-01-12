import sys

sys.path.append('../ixc_api/')


import json
from alive_progress import alive_bar


if __name__ == '__main__':
    with open('../json/ip_result.json', 'r') as json_file:
        data = json.load(json_file)

    with open('../output/sample.txt', 'r') as txt_file:
        ips_txt = txt_file.read().splitlines()

    huawei_ips = [
        "ixc.brasildigital.net.br",
        "ixc.candeiasnet.com.br",
        "ixc.br364telecom.com.br"
    ]

    with alive_bar(title='Reealizando o Parsin no huawei') as bar:  

        for item in data['prefixos']:
            ip = item['ip']

            if any(item[key] for key in item.keys() if key.startswith('ixc.')):
                item['Disponibilidade'] = True

            for huawei_ip in huawei_ips:
                if item.get(huawei_ip, False) == True or ip in ips_txt:
                    item['huawei'] = ip
                    item['Disponibilidade'] = True
                    break
            bar()

        with open('../json/ip_in_use.json', 'w') as json_file:
            json.dump(data, json_file, indent=2)

