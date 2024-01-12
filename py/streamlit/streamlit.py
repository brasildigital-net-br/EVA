import sys
sys.path.append('../ixc_api/')
sys.path.append('../json/')

import streamlit as st
import ixc_su_oss_chamado as su_os
import json
from datetime import date
import pandas as pd
from streamlit_ttyd import terminal
import time 
import os


st.set_page_config(page_title="Meu Site Streamlite")

with st.container():

    st.write("Hello Word!!!!")

    st.title("Dashboard de OS")







with st.container():
    with open('../json/ip_in_use.json', 'r') as json_file:
        data = json.load(json_file)
    

    st.write("----")
    #today = date.today()
    #print(today)

    resultados = {"prefixos": [{"ip": prefixo["ip"], "Range": prefixo["Range"]} for prefixo in data["prefixos"] if prefixo["Disponibilidade"] is None]}

    df = pd.DataFrame(resultados['prefixos'])

    st.dataframe(df)


with st.container():

    option = st.selectbox(
    'Select one ip above:',

    (   "45.179.86.0/25", 
        "168.205.124.0/25",
        "168.205.125.0/25", 
        "168.205.126.0/25", 
        "177.221.57.0/25",
        "187.236.239.128/25",
        "ls -lha",
        "pwd"
    ))

    st.write('You selected:', option)


    os.system()

    match option:
        case "45.179.86.0/25":
            print(option)
        case "168.205.124.0/25":
            print(option)
        case "168.205.125.0/25":
            print(option)
        case "168.205.126.0/25":
            print(option)
        case "177.221.57.0/25":
            print(option)
        case "187.236.239.128/25":
            print(option)

        






    





