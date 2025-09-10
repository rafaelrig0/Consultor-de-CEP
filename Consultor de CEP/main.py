import requests
from requests import Timeout, ConnectionError

# Validação de CEP - verifica o tamanho e se é composto somente de números
def validar_cep(param):
    cep_modificado = param.replace("-", "")

    if len(cep_modificado) == 8 and cep_modificado.isnumeric():
        return True

    else:
        print(f"Erro! O CEP deve estar no formato: 12345-678 ou 12345678")
        return False

cep = input("Digite o CEP: ")

# Chama a função, se o cep estiver correto retorna true e o if é inicializado, começando a procura pelo CEP
if validar_cep(cep):

    try:
        cep_response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        cep_response.raise_for_status()
        dados = cep_response.json()

        #Verifica se existe algum erro com o CEP
        if dados.get("erro"):
            print("Erro! CEP Inexistente.")

        #Salva os dados desejados em um dicionário
        else:
            endereco = {
                "Cep": dados.get("cep", "Não informado"),
                "Bairro": dados.get("bairro", "Não informado"),
                "Logradouro": dados.get("logradouro", "Não informado"),
                "Cidade": dados.get("localidade", "Não informado"),
                "Estado": dados.get("uf", "Não informado"),
            }

            #Printa o endereço
            print("\n----- ENDEREÇO -----")
            for chave, valor in endereco.items():
                print(f"{chave}: {valor}")
            print("----- ENDEREÇO -----")

    #Captura de erros de API
    except requests.exceptions.HTTPError as e:
        print("Erro:", e)

    except Timeout as e:
        print("Erro:", e)

    except ConnectionError as e:
        print("Erro:", e)