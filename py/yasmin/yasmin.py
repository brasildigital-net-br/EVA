import sys
sys.path.append('../ixc_api/')

import ixc_radusuarios
import ixc_client
import ixc_cidade
import colocadinha
import ixc_uf



########################### Y A S M I N ###########################
if __name__ == '__main__':

    # DADOS BASE
    client_data = colocadinha.get_client_data() # Inicia a operação inserindo o contrato.base == 4173.0003

    client_id = colocadinha.get_client_id(client_data) # Pega o output do client_data em formato de lista e pega a primeira celula ID
    client_base = colocadinha.get_client_base(client_data) # Pega o output do client_data em formato de lista e pega a primeira celula BASE

    # TRATAMENTO PARA DADOS LOGICOS #
    client_data_brasil = ixc_radusuarios.get_radius_data_ixc_brasil(client_id,client_base) # Usa os dados de client_id e client_base para realizar a consulta
    mac_list = ixc_radusuarios.data_client(client_data_brasil) # Armazena o mac da onu do cliente
    ip = ixc_radusuarios.data_client_ip(client_data_brasil) # Armazena o ip do cliente 

    # TRATAMENTO DE INFO DE CLIENTE #
    client_info =  ixc_client.get_client_data_ixc(client_id,client_base)

    name = ixc_client.client_name(client_info) 

    contrato = ixc_client.client_id(client_info)

    cpf_cnpj = ixc_client.client_code(client_info)

    cell = ixc_client.client_cel(client_info)

    house_number = ixc_client.client_hnumber(client_info)

    postal_code = ixc_client.client_pc(client_info)

    client_bairro = ixc_client.client_bairro(client_info) 

    cidade_id = ixc_client.client_cidade(client_info)

    client_cidade = ixc_cidade.get_cidade_data_ixc(cidade_id, client_base)

    estado_id = ixc_client.client_estado(client_info)

    complemento = ixc_client.client_complemento(client_info)

    estado_nome = ixc_uf.get_estado_data_ixc(estado_id, client_base)

    print(mac_list)

    print("|------------ ATENDIMENTO -------------|")
    print("")
    print("----------- CLIENTE -----------")

    print("\tNOME: {}".format(name))
    print("\tCONTRATO: {}".format(contrato))
    print("\tCPF/CNPJ: {}".format(cpf_cnpj))
    print("\tNUMERO: {}".format(cell))
    print("\tENDEREÇO:")
    print("\t\tNUMERO: {}".format(house_number))
    print("\t\tCEP: {}".format(postal_code))
    print("\t\tBAIRRO: {}".format(client_bairro))
    print("\t\tCIDADE: {}".format(client_cidade))
    print("\t\tESTADO: {}".format(estado_nome))
    print("\t\tCOMPLEMENTO: {}".format(complemento))

    print("-- INFORMAÇÕES DO EQUIPAMENTO --")

