
import su_oss_chamado as su_os
import json
from datetime import date
import pandas as pd

today = date.today()
print(today)

chamados = su_os.get_client_data_ixc(today, '0001')


data = chamados

df = pd.DataFrame(data['registros'])

latitude = df.loc[:,"latitude"]
longitude = df.loc[:,"longitude"]


print(latitude)
print(longitude)