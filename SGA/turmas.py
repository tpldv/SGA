from dados import salvar_dados_json, verificar_duplicacao, carregar_dados_com_validacao, codigo_existe_em_outra_entidade

# dados das turmas
dados_turmas = carregar_dados_com_validacao('turmas', ['codigo', 'cod_professor', 'cod_disciplina'])

def incluir_turma():
    cod_turma = input("Código da Turma (somente números): ")

    # verificação do código
    if codigo_existe_em_outra_entidade(cod_turma):
        return

    cod_disciplina = input("Código da Disciplina (somente números): ")
    cod_professor = input("Código do Professor (somente números): ")

    # verificação de turma
    if not verificar_duplicacao(dados_turmas, 'codigo', cod_turma):
        turma = {
            "codigo": cod_turma,
            "cod_disciplina": cod_disciplina,
            "cod_professor": cod_professor
        }
        dados_turmas.append(turma)
        salvar_dados_json('turmas', dados_turmas)
        print(f"Turma {cod_turma} incluída com sucesso!")
    else:
        print(f"Erro: Já existe uma turma com o código {cod_turma}.")

def listar_turmas():
    if len(dados_turmas) == 0:
        print("Não há turmas cadastradas.")
    else:
        print("\n===== LISTAGEM DE TURMAS =====")
        for turma in dados_turmas:
            print(f"Código da Turma: {turma['codigo']}, Código da Disciplina: {turma['cod_disciplina']}, Código do Professor: {turma['cod_professor']}")
        print()

def atualizar_turma():
    cod_turma = input("Informe o código da turma a ser atualizada: ")
    for turma in dados_turmas:
        if turma['codigo'] == cod_turma:
            turma['cod_disciplina'] = input(f"Novo código da disciplina ({turma['cod_disciplina']}): ") or turma['cod_disciplina']
            turma['cod_professor'] = input(f"Novo código do professor ({turma['cod_professor']}): ") or turma['cod_professor']
            salvar_dados_json('turmas', dados_turmas)
            print(f"Turma {cod_turma} atualizada com sucesso!")
            return
    print("Turma não encontrada.")

def excluir_turma():
    cod_turma = input("Informe o código da turma a ser excluída: ")
    for turma in dados_turmas:
        if turma['codigo'] == cod_turma:
            dados_turmas.remove(turma)
            salvar_dados_json('turmas', dados_turmas)
            print(f"Turma {cod_turma} excluída com sucesso!")
            return
    print("Turma não encontrada.")
