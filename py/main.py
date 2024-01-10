import json
import pandas as pd

with open('ip_in_use.json', 'r') as json_file:
    data = json.load(json_file)

    df = pd.DataFrame(data['prefixos'])


resultados = {"prefixos": [prefixo for prefixo in data["prefixos"] if prefixo["Disponibilidade"] is None]}

resultado_json = json.dumps(resultados, indent=2)
print(resultado_json)


print(df)