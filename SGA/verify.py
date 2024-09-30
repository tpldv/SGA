import json

# carregar dados
def carregar_dados_com_validacao(entidade):
    nome_arquivo = f'{entidade}.json'
    try:
        with open(nome_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
            for item in dados:
                if not all(key in item for key in ['cod_turma', 'cod_professor', 'cod_disciplina']):
                    print(f"Erro: Registro incompleto encontrado em {nome_arquivo}. Verifique os dados.")
                    return []
            return dados
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado. Criando novo arquivo.")
        return []
