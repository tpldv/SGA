import json

# salva dados JSON
def salvar_dados_json(entidade, dados):
    nome_arquivo = f'{entidade}.json'
    try:
        with open(nome_arquivo, 'w') as arquivo:
            json.dump(dados, arquivo)
        print(f"Dados de {entidade} salvos com sucesso.")
    except Exception as e:
        print(f"Erro ao salvar dados de {entidade}: {e}")

# carregar dados JSON (sem validação)
def carregar_dados_json(entidade):
    nome_arquivo = f'{entidade}.json'
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado. Criando novo arquivo.")
        return []
    except Exception as e:
        print(f"Erro ao carregar dados de {entidade}: {e}")
        return []

# JSON com validação
def carregar_dados_com_validacao(entidade, chaves_essenciais):
    nome_arquivo = f'{entidade}.json'
    try:
        with open(nome_arquivo, 'r') as arquivo:
            dados = json.load(arquivo)
            for item in dados:
                if not all(key in item for key in chaves_essenciais):
                    print(f"Erro: Registro incompleto encontrado em {nome_arquivo}. Verifique os dados.")
                    return []
            return dados
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado. Criando novo arquivo.")
        return []
    except Exception as e:
        print(f"Erro ao carregar dados de {entidade}: {e}")
        return []

# duplicação de um campo em uma lista de dados
def verificar_duplicacao(lista, campo, valor):
    for item in lista:
        if campo in item and item[campo] == valor:
            return True
    return False

# verifica se o código já existe em outra entidade
def codigo_existe_em_outra_entidade(codigo):
    todas_entidades = ['estudantes', 'professores', 'turmas', 'disciplinas']
    for entidade in todas_entidades:
        dados = carregar_dados_json(entidade)
        if verificar_duplicacao(dados, 'codigo', codigo):
            print(f"Erro: O código {codigo} já existe em outra entidade ({entidade}).")
            return True
    return False
