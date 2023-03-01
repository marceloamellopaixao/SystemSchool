import datetime
from datetime import date

bdDados = []
linha = "|-----------------------------|--------------------------------|-----------------------------|"
lines = "|-----------------------------|"
nomeEscola = "Estácio Conceição"
enderecoEscola = "Rua do Metro"
telefoneEscola = "(11) 98888-1111"


# Esta Função constrói a linha do menu quando chamada.
def print_builder(text):
    print(linha)
    print(lines, text, lines, sep='')
    print(linha)


# Esta função vai ler o arquivo no início da execução
def file_reader():
    try:
        with open('bdschool.txt', 'r') as file:
            content = file.readlines()
        content = [x.strip('\n') for x in content]

        lenght = len(content)

        if lenght > 0:
            for i in range(lenght):
                bdDados.append(content[i])
    except:
        print('')
        print("Arquivo de Dados inexistente, está sendo criado um novo...")
        print('Criado com Sucesso!')
        print('')
        with open('bdschool.txt', 'w') as file:
            for bdNew in file:
                file.write(str(bdNew) + '\n')
    finally:
        return bdDados


# Função que Cálcula automaticamente a data de nascimento do aluno para descobrir sua idade atualmente
def calculate_age(birthday):
    today = date.today()
    age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))

    return age


# Função que constrói a data de nascimento de um modo que não ocorra erros no sistema
def build_birthday():
    print("Digite a data de nascimento do aluno")

    dia = int(input("Dia: "))
    mes = int(input("Mes: "))
    ano = int(input("Ano: "))
    data = datetime.datetime(ano, mes, dia)

    return data.date()


# Função Calcula a média do aluno, tento suas verificações se passou ou não com a média.
def calculate_grades():
    while True:
        print_builder("-------[Calculo de Média]-------")
        print('')
        print('Atenção! [Digite as notas com valores de 0 a 10]')
        print('')
        nota1 = float(input('Digite a primeira nota: '))
        nota2 = float(input('Digite a segunda nota: '))
        nota3 = float(input('Digite a terceira nota: '))
        nota4 = float(input('Digite a quarta nota: '))

        answer = float(nota1 + nota2 + nota3 + nota4) / 4

        if (answer >= 6) and (answer <= 10):
            print('')
            print('APROVADO')
            print('A média deste aluno é: ', answer)
            print('')
        elif (answer <= 4) and (answer >= 0):
            print('')
            print('REPROVADO')
            print('A média deste aluno é: ', answer)
            print('')
        elif answer == 5:
            print('')
            print('RECUPERAÇÃO')
            print('A média deste aluno é: ', answer)
            print('')
        else:
            print('')
            print('Erro! Tente novamente!')
            print('')
            calculate_grades()

        opcao = input('Deseja fazer um novo calculo de média? (S/N): ').strip().lower()
        if opcao == 's':
            continue
        else:
            main_menu()
            break


# Função para cadastro de alunos
def new_student():
    while True:
        # Váriaveis
        newStudents = []
        student = {}
        print_builder("------[Cadastro de Alunos]------")

        student['Nome'] = input("Digite o nome do aluno: ")
        x = build_birthday()
        student['Data de Nascimento'] = str(x.strftime("%d/%m/%Y"))
        student['Idade'] = calculate_age(x)
        bdDados.append(student)
        newStudents.append(student)

        opcao = input('Deseja fazer um novo cadastro? (S/N): ').strip().lower()
        if opcao == 's':
            with open('bdschool.txt', 'a+') as file:
                for studentInsert in newStudents:
                    file.write(str(studentInsert) + '\n')
            continue
        else:
            # Estes comandos salvam todos os dados no arquivo bdschool.txt
            with open('bdschool.txt', 'a+') as file:
                for studentInsert in newStudents:
                    file.write(str(studentInsert) + '\n')
            # Retorna ao menu inicial e trava a repetição deste atual
            main_menu()
            break


# Função mostra todos os registros de Alunos Matriculados
def show_students():
    while True:
        print_builder("-----[Alunos Matriculados]------")
        print('')

        # Váriavel dos seguintes.
        studentsLocal = len(bdDados)

        if studentsLocal == 0:
            print('Não há alunos no momento, tente cadastrar alguns!')
            print('')
            opcao = input('Deseja retornar ao Menu Inicial? (S/N): ').strip().lower()
            if opcao == 's':
                main_menu()
                break
            else:
                continue
        else:
            print("Número de alunos cadastrados: ", studentsLocal)
            print('')

            for i in range(studentsLocal):
                print(bdDados[i])
            print('')

            opcao = input('Deseja verificar novamente os dados? (S/N): ').strip().lower()
            if opcao == 's':
                continue
            else:
                main_menu()
                break


# Função para Deletar Alunos
def delete_student():
    while True:
        print_builder("--------[Excluir Aluno]---------")
        print('')

        # Váriaveis
        numero_de_alunos = len(bdDados)

        for i in range(numero_de_alunos):
            print(i + 1, bdDados[i], sep=" - ")
        print("")

        if numero_de_alunos == 0:
            print('Não há alunos disponíveis no momento, tente cadastrar alguns!')
            print('')
            opcao = input('Deseja retornar ao Menu Inicial? (S/N): ').strip().lower()
            if opcao == 's':
                main_menu()
                break
            else:
                continue
        else:
            numero = int(input("Escolha o Aluno a ser excluido pelo seu número: "))
            if (numero > numero_de_alunos) or (numero < 1):
                print('')
                print("Número inválido, tente novamente")
                print('')
                delete_student()
            else:
                index = numero - 1
                bdDados.pop(index)

                with open('bdschool.txt', 'w') as file:
                    for studentInsert in bdDados:
                        file.write(str(studentInsert) + '\n')

                print('')
                print("Aluno(a):", index + 1, "foi excluido com sucesso!")
                print('')

            opcao = input('Deseja excluir mais alunos? (S/N): ').strip().lower()
            if opcao == 's':
                continue
            else:
                main_menu()
                break


# Função que quando chamada mostra as informações da Escola.
def school_info():
    while True:
        print_builder("----[Informações da Escola]-----")
        print('')
        print("Nome da Escola: ", nomeEscola)
        print("Endereço: ", enderecoEscola)
        print("Telefone: ", telefoneEscola)
        print('')

        opcao = input('Deseja verificar novamente os dados? (S/N): ').strip().lower()
        if opcao == 's':
            continue
        else:
            main_menu()
            break


# Função do Menu Inicial - Juntamente com suas funcionalidades
def main_menu():
    print_builder("-------[Sistema Escolar]--------")
    print_builder("Escolha uma das opções a seguir:")
    print('')
    print("[1] - Calculo de Médias")
    print("[2] - Cadastro de Alunos")
    print("[3] - Registros de Alunos Matriculados")
    print("[4] - Excluir Alunos Matriculados")
    print("[5] - Informações da Escola")
    print("[0] - Sair do Sistema")
    print(linha)

file_reader()
main_menu()

while True:
    code = int(input("Digite a opção desejada: "))

    while code > 5 or code < 0:
        code = int(input("[Erro, Tente Novamente!] Digite uma opção válida: "))

    if (code == 1) and (code > 0) and (code < 2):
        calculate_grades()

    elif (code == 2) and (code > 1) and (code < 3):
        new_student()

    elif (code == 3) and (code > 2) and (code < 4):
        show_students()

    elif (code == 4) and (code > 3) and (code < 5):
        delete_student()

    elif (code == 5) and (code > 4) and (code < 6):
        school_info()

    else:
        print('')
        print('[Programa encerrado com Sucesso!]')
        print('')
        break