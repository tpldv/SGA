# Armazenamento de Dados Comum (inicialmente na memória, depois em arquivo)
data_store = {
    "estudantes": [],
    "professores": [],
    "disciplinas": [],
    "turmas": [],
    "matriculas": []
}

# Função para incluir uma nova entidade
def incluir_entidade(tipo_entidade, dados_entidade):
    if tipo_entidade in data_store:
        data_store[tipo_entidade].append(dados_entidade)
        print(f"\n{tipo_entidade.capitalize()} incluído com sucesso!\n")
    else:
        print(f"Tipo de entidade desconhecido: {tipo_entidade}")

# Função para listar entidades
def listar_entidade(tipo_entidade):
    if tipo_entidade in data_store:
        if len(data_store[tipo_entidade]) == 0:
            print(f"\nNão há {tipo_entidade} cadastrados.\n")
        else:
            print(f"\n===== LISTAGEM DE {tipo_entidade.upper()} =====")
            for entidade in data_store[tipo_entidade]:
                print(entidade)
            print()
    else:
        print(f"Tipo de entidade desconhecido: {tipo_entidade}")

# Função para atualizar uma entidade
def atualizar_entidade(tipo_entidade, id_entidade, novos_dados):
    if tipo_entidade in data_store:
        for i, entidade in enumerate(data_store[tipo_entidade]):
            if entidade['id'] == id_entidade:  # Assume que há um campo 'id'
                data_store[tipo_entidade][i].update(novos_dados)
                print(f"\n{tipo_entidade.capitalize()} atualizado com sucesso!\n")
                return
        print(f"{tipo_entidade.capitalize()} não encontrado.")
    else:
        print(f"Tipo de entidade desconhecido: {tipo_entidade}")

# Função para excluir uma entidade
def excluir_entidade(tipo_entidade, id_entidade):
    if tipo_entidade in data_store:
        for i, entidade in enumerate(data_store[tipo_entidade]):
            if entidade['id'] == id_entidade:  # Assume que há um campo 'id'
                del data_store[tipo_entidade][i]
                print(f"\n{tipo_entidade.capitalize()} excluído com sucesso!\n")
                return
        print(f"{tipo_entidade.capitalize()} não encontrado.")
    else:
        print(f"Tipo de entidade desconhecido: {tipo_entidade}")
