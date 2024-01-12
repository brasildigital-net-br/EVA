import streamlit as st
import ixc_su_oss_chamado as su_os
import json
from datetime import date
import pandas as pd
from streamlit_ttyd import terminal
import time 


st.set_page_config(page_title="Meu Site Streamlite")

with st.container():

    st.write("Hello Word!!!!")

    st.title("Dashboard de OS")







with st.container():
    with open('ip_in_use.json', 'r') as json_file:
        data = json.load(json_file)
    

    st.write("----")
    #today = date.today()
    #print(today)

    resultados = {"prefixos": [{"ip": prefixo["ip"], "Range": prefixo["Range"]} for prefixo in data["prefixos"] if prefixo["Disponibilidade"] is None]}

    df = pd.DataFrame(resultados['prefixos'])

    st.dataframe(df)


with st.container():

    #st.text("Terminal showing processes running on your system using the top command")
    port = 7681
    # start the ttyd server and display the terminal on streamlit
    ttydprocess, port = terminal(cmd="./main.sh")

    st.text(f"ttyd server is running on port : {port}")





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
    #st.map(data=df, latitude=latitude, longitude=longitude, color=None, size=None, zoom=None, use_container_width=True)






'''with st.container():
    st.write("----")
    today = date.today()
    print(today)

    chamados = su_os.get_client_data_ixc(today, '0001')

    data = json.loads(chamados.text)

    df = pd.DataFrame(data['registros'])

    st.dataframe(df)'''

    # retornar todas as os com o setor == ID_DST[1...15]