from dados import salvar_dados_json, verificar_duplicacao, carregar_dados_json, codigo_existe_em_outra_entidade

dados_disciplinas = carregar_dados_json('disciplinas')

def incluir_disciplina():
    cod_disciplina = input("Código da Disciplina (somente números): ")

    if codigo_existe_em_outra_entidade(cod_disciplina):
        return

    nome_disciplina = input("Nome da Disciplina: ")

    if not verificar_duplicacao(dados_disciplinas, 'codigo', cod_disciplina):
        disciplina = {
            "codigo": cod_disciplina,
            "nome": nome_disciplina
        }
        dados_disciplinas.append(disciplina)
        salvar_dados_json('disciplinas', dados_disciplinas)
        print(f"Disciplina {nome_disciplina} incluída com sucesso!")
    else:
        print(f"Erro: Já existe uma disciplina com o código {cod_disciplina}.")

def listar_disciplinas():
    if len(dados_disciplinas) == 0:
        print("Não há disciplinas cadastradas.")
    else:
        print("\n===== LISTAGEM DE DISCIPLINAS =====")
        for disciplina in dados_disciplinas:
            print(f"Código: {disciplina['codigo']}, Nome: {disciplina['nome']}")
        print()

def atualizar_disciplina():
    cod_disciplina = input("Informe o código da disciplina que deseja atualizar: ")
    for disciplina in dados_disciplinas:
        if disciplina['codigo'] == cod_disciplina:
            disciplina['nome'] = input(f"Novo nome ({disciplina['nome']}): ") or disciplina['nome']
            salvar_dados_json('disciplinas', dados_disciplinas)
            print("Dados da disciplina atualizados com sucesso!")
            return
    print("Disciplina não encontrada.")

def excluir_disciplina():
    cod_disciplina = input("Informe o código da disciplina que deseja excluir: ")
    for disciplina in dados_disciplinas:
        if disciplina['codigo'] == cod_disciplina:
            dados_disciplinas.remove(disciplina)
            salvar_dados_json('disciplinas', dados_disciplinas)
            print(f"Disciplina {cod_disciplina} excluída com sucesso!")
            return
    print("Disciplina não encontrada.")
