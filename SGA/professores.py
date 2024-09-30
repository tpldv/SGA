from dados import salvar_dados_json, verificar_duplicacao, carregar_dados_json, codigo_existe_em_outra_entidade

# dados dos professores
dados_professores = carregar_dados_json('professores')

def incluir_professor():
    cod_professor = input("Código do Professor (somente números): ")

    if codigo_existe_em_outra_entidade(cod_professor):
        return

    nome_professor = input("Nome do Professor: ")
    cpf = input("CPF do Professor (somente números): ")

    if not verificar_duplicacao(dados_professores, 'cpf', cpf):
        professor = {
            "codigo": cod_professor,
            "nome": nome_professor,
            "cpf": cpf
        }
        dados_professores.append(professor)
        salvar_dados_json('professores', dados_professores)
        print(f"Professor {nome_professor} incluído com sucesso!")
    else:
        print(f"Erro: Já existe um professor com o CPF {cpf}.")

def listar_professores():
    if len(dados_professores) == 0:
        print("Não há professores cadastrados.")
    else:
        print("\n===== LISTAGEM DE PROFESSORES =====")
        for professor in dados_professores:
            if all(key in professor for key in ['codigo', 'nome', 'cpf']):
                print(f"Código: {professor['codigo']}, Nome: {professor['nome']}, CPF: {professor['cpf']}")
            else:
                print("Erro: Registro incompleto encontrado. Verifique os dados.")
        print()

def atualizar_professor():
    cod_professor = input("Informe o código do professor que deseja atualizar: ")
    
    professor_encontrado = None
    for professor in dados_professores:
        if 'codigo' in professor and professor['codigo'] == cod_professor:
            professor_encontrado = professor
            break

    if professor_encontrado:
        professor_encontrado['nome'] = input(f"Novo nome ({professor_encontrado['nome']}): ") or professor_encontrado['nome']
        professor_encontrado['cpf'] = input(f"Novo CPF ({professor_encontrado['cpf']}): ") or professor_encontrado['cpf']
        salvar_dados_json('professores', dados_professores)
        print("Dados atualizados com sucesso!")
    else:
        print("Erro: Professor não encontrado ou registro incompleto.")

def excluir_professor():
    cod_professor = input("Informe o código do professor que deseja excluir: ")
    
    professor_encontrado = None
    for professor in dados_professores:
        if 'codigo' in professor and professor['codigo'] == cod_professor:
            professor_encontrado = professor
            break

    if professor_encontrado:
        dados_professores.remove(professor_encontrado)
        salvar_dados_json('professores', dados_professores)
        print(f"Professor {cod_professor} excluído com sucesso!")
    else:
        print("Erro: Professor não encontrado.")
