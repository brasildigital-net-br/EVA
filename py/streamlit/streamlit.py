import sys
sys.path.append('../ixc_api/')
sys.path.append('../json/')
sys.path.append('../eduarda/')
import streamlit as st
import os
import json
import pandas as pd
import validator_ip
from streamlit_elements import elements, mui, html


st.set_page_config(page_title="Brasil Digitel")

with st.container():

    st.write("Hello Word!!!!")

    st.title("Dashboard de OS")

with st.container():

    ip = str(st.text_input('IP', ''))
    #st.write('The current movie title is', ip)
    if ip:
        print(ip)
        data = validator_ip.validator_uniq(ip)
        resultados = {"prefixos": [{"ip": prefixo["ip"]} for prefixo in data["prefixos"] if prefixo["Disponibilidade"] is None]}
        
        if not resultados["prefixos"]:
            print("IP em uso")
            st.write("Can't use the ip: {}".format(ip))
        else:
            print("Pode usar")
            st.write("Can use the ip: {}".format(ip))
    
with st.container():
    st.write("Validação de 2 elementos por range")
    data = validator_ip.validate_range()
    resultados = {"prefixos": [{"ip": prefixo["ip"]} for prefixo in data["prefixos"] if prefixo["Disponibilidade"] is None]}
    df = pd.DataFrame(resultados['prefixos'])
    st.dataframe(df)

with st.container():

    with open('../json/ip_in_use.json', 'r') as json_file:
        data = json.load(json_file)
        
    st.write("----")
        #today = date.today()
        #print(today)

    resultados = {"prefixos": [{"ip": prefixo["ip"], "Range": prefixo["Range"], "LastTimeRunning": prefixo["LastTimeRunning"]} for prefixo in data["prefixos"] if prefixo["Disponibilidade"] is None]}
    # criar uma variavel q pega os 3 primeiros ips livres de cada prefixo e já realizar uma validação em cima deles
    # e expor isso em um dataframe

    df = pd.DataFrame(resultados['prefixos'])

    st.dataframe(df)

    st.write("----")


# with elements("dashboard"):

#     # You can create a draggable and resizable dashboard using
#     # any element available in Streamlit Elements.

#     from streamlit_elements import dashboard

#     # First, build a default layout for every element you want to include in your dashboard

#     layout = [
#         # Parameters: element_identifier, x_pos, y_pos, width, height, [item properties...]
#         dashboard.Item("first_item", 0, 0, 2, 2),
#         dashboard.Item("second_item", 2, 0, 2, 2),
#         dashboard.Item("third_item", 0, 2, 1, 1),
#     ]

#     # Next, create a dashboard layout using the 'with' syntax. It takes the layout
#     # as first parameter, plus additional properties you can find in the GitHub links below.

#     with dashboard.Grid(layout):
#         mui.Paper("First item", key="first_item")
#         mui.Paper("Second item (cannot drag)", key="second_item")
#         mui.Paper("Third item (cannot resize)", key="third_item")

#     # If you want to retrieve updated layout values as the user move or resize dashboard items,
#     # you can pass a callback to the onLayoutChange event parameter.

#     def handle_layout_change(updated_layout):
#         print(updated_layout)

#     with dashboard.Grid(layout, onLayoutChange=handle_layout_change):
#         mui.Paper("First item", key="first_item")
#         mui.Paper("Second item (cannot drag)", key="second_item")
#         mui.Paper("Third item (cannot resize)", key="third_item")



