import sys
sys.path.append('../ixc_api/')
sys.path.append('../json/')
sys.path.append('../eduarda/')
import streamlit as st
import os
import json
import pandas as pd
import validator_ip


st.set_page_config(page_title="Brasil Digitel")

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

    st.write("----")

with st.container():
    ip = str(st.text_input('IP', ''))
    st.write('The current movie title is', ip)
    if ip:
        print(ip)
        data = validator_ip.validator_in_infra(ip)
        resultados = {"prefixos": [{"ip": prefixo["ip"]} for prefixo in data["prefixos"] if prefixo["Disponibilidade"] is None]}
        
        if not resultados["prefixos"]:
            print("IP em uso")
            st.write("Can't use")
        else:
            print("Pode usar")
            st.write("Can use")
    

    


# with st.container():

#     option = st.selectbox(
#     'Select one ip above:',

#     (   "45.179.86.0/25", 
#         "168.205.124.0/25",
#         "168.205.125.0/25", 
#         "168.205.126.0/25", 
#         "177.221.57.0/25",
#         "187.236.239.128/25"
#     ))

#     st.write('You selected:', option)

#     id = [a for a in option.split('/') if a]
#     costumer_ip = id[0]

#     print(costumer_ip)
    
#     if st.button('search'):
#         st.write('kawai vou procurar alguns ips livres no prefixo {}'.format(costumer_ip))
#         os.system("cd ../eduarda/ && python3 eduarda.py {} && python3 parsing_ip_hw.py {} && python3 trating_data_txt_json.py".format(option ,costumer_ip))

#         with open('../json/ip_in_use.json', 'r') as json_file:
#             data = json.load(json_file)
        

#         st.write("----")
#         #today = date.today()
#         #print(today)

#         resultados = {"prefixos": [{"ip": prefixo["ip"], "Range": prefixo["Range"]} for prefixo in data["prefixos"] if prefixo["Disponibilidade"] is None]}

#         df = pd.DataFrame(resultados['prefixos'])

#         st.dataframe(df)

#         st.write("----")



#with st.container():


    # match option:
    #     case "45.179.86.0/25":
    #         print(option)
    #     case "168.205.124.0/25":
    #         print(option)
    #     case "168.205.125.0/25":
    #         print(option)
    #     case "168.205.126.0/25":
    #         print(option)
    #     case "177.221.57.0/25":
    #         print(option)
    #     case "187.236.239.128/25":
    #         print(option)
