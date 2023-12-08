import ixc_ip
import ixc_client
from dotenv import load_dotenv as env
import os
import ixc_locked_ip

# 100.64.83.

##################################### E D U A R D A ###########################################


if __name__ == '__main__':
    env(".env")

    # VARS DE CONSULTA
    ixc_brd = os.getenv('IXC_BRASILDIGITAL_URI')
    ixc_cd = os.getenv('IXC_CANDEIASNET_URI')
    ixc_364 = os.getenv('IXC_BR364TELECOM_URI')

    aut_brd = os.getenv("Authorization_142")
    aut_cd = os.getenv("Authorization_142")
    aut_364 = os.getenv("Authorization_72")

    host = [ixc_brd, ixc_cd, ixc_364]
    aut = [aut_brd, aut_cd, aut_364]

    zip = list(zip(host, aut))

    # Input do ip para consulta
    ip = input("Insiria o ip para verificar a disponibilidade:")
    # host = ixc_364
    # print(ixc_364)
    # ixc_aut = aut_364
    #ip_locked = ixc_locked_ip.block_ip(ip)

    #print(ip_locked)

    for h, a in zip:

        ip_consulting = ixc_ip.get_radius_data_ixc_brasil(ip, h, a)
        mostra_ip = int(ixc_ip.ip_list(ip_consulting))
        
        if ixc_locked_ip.block_ip(ip) == True:

            print("IP RESEREVADO!")
        
        elif ip == "8.8.8.8":
            print("Deixa a Google em paz rapaz!")
        
        elif mostra_ip == 0 and ixc_locked_ip.block_ip(ip) == False:

            print("|-------------O IP SE ENCONTRA DISPONIVEL NA BASE: {}------------|".format(h))
            print("")

        elif mostra_ip > 0 and ixc_locked_ip.block_ip(ip) == False:

            print("|-------------IP EM USO NA BASE: {}---------------------|".format(h))
            get_contract = ixc_ip.client_id(ip_consulting)
            #contract = get_contract[0]
            # contract = int(contract)
            # get_name = ixc_client.client_name(contract)
            #print(type(get_contract))
            
            # for i in get_contract:
            #     get_name = ixc_client.client_name(get_contract)
            print("")
            # for i in get_contract:
            #     print(i)
            #print("\t\t\tCliente {}, contrato {}".format(get_contract))

        else:
            print("")


        #get_client_name = ixc_client.client_name(get_contract)





# 100.64.83.93
# 179.63.156.98
        




