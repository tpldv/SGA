from dados import salvar_dados_json, verificar_duplicacao, carregar_dados_json

dados_matriculas = carregar_dados_json('matriculas')

def incluir_matricula():
    cod_turma = input("Código da Turma (somente números): ")
    cod_estudante = input("Código do Estudante (somente números): ")

    # duplicação dados
    if not verificar_duplicacao(dados_matriculas, 'cod_turma', cod_turma) or not verificar_duplicacao(dados_matriculas, 'cod_estudante', cod_estudante):
        matricula = {
            "cod_turma": cod_turma,
            "cod_estudante": cod_estudante
        }
        dados_matriculas.append(matricula)
        salvar_dados_json('matriculas', dados_matriculas)
        print(f"Matrícula para o estudante {cod_estudante} na turma {cod_turma} incluída com sucesso!")
    else:
        print(f"Erro: Já existe uma matrícula para a turma {cod_turma} com o estudante {cod_estudante}.")

def listar_matriculas():
    if len(dados_matriculas) == 0:
        print("Não há matrículas cadastradas.")
    else:
        print("\n===== LISTAGEM DE MATRÍCULAS =====")
        for matricula in dados_matriculas:
            print(f"Código da Turma: {matricula['cod_turma']}, Código do Estudante: {matricula['cod_estudante']}")
        print()

def atualizar_matricula():
    cod_turma = input("Informe o código da turma da matrícula que deseja atualizar: ")
    cod_estudante = input("Informe o código do estudante: ")
    
    for matricula in dados_matriculas:
        if matricula['cod_turma'] == cod_turma and matricula['cod_estudante'] == cod_estudante:
            nova_turma = input(f"Novo código da turma ({cod_turma}): ") or cod_turma
            novo_estudante = input(f"Novo código do estudante ({cod_estudante}): ") or cod_estudante
            matricula['cod_turma'] = nova_turma
            matricula['cod_estudante'] = novo_estudante
            salvar_dados_json('matriculas', dados_matriculas)
            print("Dados da matrícula atualizados com sucesso!")
            return
    print("Matrícula não encontrada.")

def excluir_matricula():
    cod_turma = input("Informe o código da turma da matrícula que deseja excluir: ")
    cod_estudante = input("Informe o código do estudante: ")
    
    for matricula in dados_matriculas:
        if matricula['cod_turma'] == cod_turma and matricula['cod_estudante'] == cod_estudante:
            dados_matriculas.remove(matricula)
            salvar_dados_json('matriculas', dados_matriculas)
            print(f"Matrícula da turma {cod_turma} com o estudante {cod_estudante} excluída com sucesso!")
            return
    print("Matrícula não encontrada.")
