from estudantes import incluir_estudante, listar_estudantes, atualizar_estudante, excluir_estudante
from professores import incluir_professor, listar_professores, atualizar_professor, excluir_professor
from disciplinas import incluir_disciplina, listar_disciplinas, atualizar_disciplina, excluir_disciplina
from turmas import incluir_turma, listar_turmas, atualizar_turma, excluir_turma
from matriculas import incluir_matricula, listar_matriculas, atualizar_matricula, excluir_matricula

def menu_principal():
    while True:
        print("\n===== MENU PRINCIPAL =====")
        print("1. Estudantes")
        print("2. Professores")
        print("3. Disciplinas")
        print("4. Turmas")
        print("5. Matrículas")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            menu_estudantes()
        elif opcao == "2":
            menu_professores()
        elif opcao == "3":
            menu_disciplinas()
        elif opcao == "4":
            menu_turmas()
        elif opcao == "5":
            menu_matriculas()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def menu_estudantes():
    while True:
        print("\n===== MENU ESTUDANTES =====")
        print("1. Incluir Estudante")
        print("2. Listar Estudantes")
        print("3. Atualizar Estudante")
        print("4. Excluir Estudante")
        print("9. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            incluir_estudante()
        elif opcao == "2":
            listar_estudantes()
        elif opcao == "3":
            atualizar_estudante()
        elif opcao == "4":
            excluir_estudante()
        elif opcao == "9":
            break

def menu_professores():
    while True:
        print("\n===== MENU PROFESSORES =====")
        print("1. Incluir Professor")
        print("2. Listar Professores")
        print("3. Atualizar Professor")
        print("4. Excluir Professor")
        print("9. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            incluir_professor()
        elif opcao == "2":
            listar_professores()
        elif opcao == "3":
            atualizar_professor()
        elif opcao == "4":
            excluir_professor()
        elif opcao == "9":
            break

def menu_disciplinas():
    while True:
        print("\n===== MENU DISCIPLINAS =====")
        print("1. Incluir Disciplina")
        print("2. Listar Disciplinas")
        print("3. Atualizar Disciplina")
        print("4. Excluir Disciplina")
        print("9. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            incluir_disciplina()
        elif opcao == "2":
            listar_disciplinas()
        elif opcao == "3":
            atualizar_disciplina()
        elif opcao == "4":
            excluir_disciplina()
        elif opcao == "9":
            break

def menu_turmas():
    while True:
        print("\n===== MENU TURMAS =====")
        print("1. Incluir Turma")
        print("2. Listar Turmas")
        print("3. Atualizar Turma")
        print("4. Excluir Turma")
        print("9. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            incluir_turma()
        elif opcao == "2":
            listar_turmas()
        elif opcao == "3":
            atualizar_turma()
        elif opcao == "4":
            excluir_turma()
        elif opcao == "9":
            break

def menu_matriculas():
    while True:
        print("\n===== MENU MATRÍCULAS =====")
        print("1. Incluir Matrícula")
        print("2. Listar Matrículas")
        print("3. Atualizar Matrícula")
        print("4. Excluir Matrícula")
        print("9. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            incluir_matricula()
        elif opcao == "2":
            listar_matriculas()
        elif opcao == "3":
            atualizar_matricula()
        elif opcao == "4":
            excluir_matricula()
        elif opcao == "9":
            break

if __name__ == "__main__":
    menu_principal()

# Desenvolvido por Túlio Vargas (https://www.linkedin.com/in/t%C3%BAlio-prot%C3%A1sio-573232277/).

