
# Input de dados contrato.base == 48679.0001
def get_client_data():
    client_data = input("Enter the client data here:")
    id = [a for a in client_data.split('.') if a]

    return client_data

# pega de forma unica o contrato para consulta
def get_client_id(client_data):
    client_id = client_data
    id = [a for a in client_id.split('.') if a]
    client_id = id[0]
    #s.split('mango', 1)[1]
    return client_id

# Pega de forma unica a base do cliente
def get_client_base(client_data):
    client_base = client_data
    base = [a for a in client_base.split('.') if a]
    base = base[1]
    return base

