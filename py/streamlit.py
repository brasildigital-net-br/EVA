import streamlit as st
import su_oss_chamado as su_os
import json
from datetime import date
import pandas as pd


st.set_page_config(page_title="Meu Site Streamlite")

with st.container():

    st.write("Hello Word!!!!")

    st.title("Dashboard de OS")


with st.container():
    st.write("----")
    today = date.today()
    print(today)

    chamados = su_os.get_client_data_ixc(today, '0001')

    data = chamados

    df = pd.DataFrame(data['registros'])
    

    latitude = df.loc[:,"latitude"]
    longitude = df.loc[:,"longitude"]

    st.dataframe(df)
    st.map(data=df, latitude=latitude, longitude=longitude, color=None, size=None, zoom=None, use_container_width=True)






'''with st.container():
    st.write("----")
    today = date.today()
    print(today)

    chamados = su_os.get_client_data_ixc(today, '0001')

    data = json.loads(chamados.text)

    df = pd.DataFrame(data['registros'])

    st.dataframe(df)'''

    # retornar todas as os com o setor == ID_DST[1...15]