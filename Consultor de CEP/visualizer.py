try:
    cep_response = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    cep_response.raise_for_status()
    dados = cep_response.json()

    # Verifica se existe algum erro com o CEP
    if dados.get("erro"):
        print("Erro! CEP Inexistente.")