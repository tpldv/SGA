from dados import salvar_dados_json, verificar_duplicacao, carregar_dados_json, codigo_existe_em_outra_entidade

dados_estudantes = carregar_dados_json('estudantes')

def incluir_estudante():
    cod_estudante = input("Código do Estudante (somente números): ")
    
    if codigo_existe_em_outra_entidade(cod_estudante):
        return

    nome_estudante = input("Nome do Estudante: ")
    cpf = input("CPF do Estudante (somente números): ")

    if not verificar_duplicacao(dados_estudantes, 'cpf', cpf):
        estudante = {
            "codigo": cod_estudante,
            "nome": nome_estudante,
            "cpf": cpf
        }
        dados_estudantes.append(estudante)
        salvar_dados_json('estudantes', dados_estudantes)
        print(f"Estudante {nome_estudante} incluído com sucesso!")
    else:
        print(f"Erro: Já existe um estudante com o CPF {cpf}.")

def listar_estudantes():
    if len(dados_estudantes) == 0:
        print("Não há estudantes cadastrados.")
    else:
        print("\n===== LISTAGEM DE ESTUDANTES =====")
        for estudante in dados_estudantes:
            print(f"Código: {estudante['codigo']}, Nome: {estudante['nome']}, CPF: {estudante['cpf']}")
        print()

def atualizar_estudante():
    cod_estudante = input("Informe o código do estudante que deseja atualizar: ")
    for estudante in dados_estudantes:
        if estudante['codigo'] == cod_estudante:
            estudante['nome'] = input(f"Novo nome ({estudante['nome']}): ") or estudante['nome']
            estudante['cpf'] = input(f"Novo CPF ({estudante['cpf']}): ") or estudante['cpf']
            salvar_dados_json('estudantes', dados_estudantes)
            print("Dados atualizados com sucesso!")
            return
    print("Estudante não encontrado.")

def excluir_estudante():
    cod_estudante = input("Informe o código do estudante que deseja excluir: ")
    for estudante in dados_estudantes:
        if estudante['codigo'] == cod_estudante:
            dados_estudantes.remove(estudante)
            salvar_dados_json('estudantes', dados_estudantes)
            print(f"Estudante {cod_estudante} excluído com sucesso!")
            return
    print("Estudante não encontrado.")
