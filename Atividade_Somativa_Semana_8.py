# Maicon Vinicios P. Kaiser
# Análise e Desenv. Sistemas
# Polo Curitiba-PR

import json #Biblioteca para trabalhar com arquivos JSON.
from time import sleep #Adicionei essa biblioteca para dar pausas entre ações e não ficar tudo muito rápido ficando assim melhor de ler.
import os #Importei essa biblioteca para usar os aquivos JSON em qualquer computador.

def caminhoArquivo(nomeArquivo):
    return os.path.join(jsonRaiz, nomeArquivo)

#------Chamada de arquivos JSON-------------------------------------------------------
jsonRaiz = "C:/Users/kaise/Downloads/PUCPR/Raciocinio Computacional/Programas"
jsonEstudantes = caminhoArquivo("estudantes.json")
jsonProfessores = caminhoArquivo('professores.json')
jsonDisciplinas = caminhoArquivo('disciplinas.json')
jsonTurmas = caminhoArquivo('turmas.json')
jsonMatriculas = caminhoArquivo('matriculas.json')
#-------------------------------------------------------------------------------------
#----------MENUS----------------------------------------------------------------------
def menuInicial():
    print('----- MENU PRINCIPAL -----\n\n'
          '(1) Gerenciar estudantes.\n'
          '(2) Gerenciar professores.\n'
          '(3) Gerenciar disciplinas.\n'
          '(4) Gerenciar turmas.\n'
          '(5) Gerenciar matriculas.\n'
          '(9) Sair.\n')
    return int(input("Digite a opção desejada: "))

def menuAcoes():
    print('(1) Incluir.\n'
          '(2) Listar.\n'
          '(3) Atualizar.\n'
          '(4) Excluir.\n'
          '(9) Voltar ao menu principal.\n')
    return int(input("Informe a ação desejada: "))
#------------------------------------------------------------------------------------
#----------GENERICO------------------------------------------------------------------
def incluirElemento(arquivo, mensagem):
    print(f'===== INCLUIR {mensagem.upper()} =====\n')
    codigo = int(input(f'Digite o CÓDIGO do(a) {mensagem} a ser INCLUSO: '))
    achou = False
    dados = lerJson(arquivo)
    for elementoAtual in dados:
        if elementoAtual['codigo'] == codigo:
            sleep(0.2)
            print(f'\n!!! {mensagem.upper()} já CADASTRADO. !!!\n')
            sleep(0.2)
            achou = True
            print('Voltando ao MENU de AÇÕES...\n')
            sleep(0.5)
            break
    if not achou:
        nome = input(f'Digite o NOME do(a) {mensagem} a ser INCLUSO: ')
        cpf = input(f'Digite o CPF do(a) {mensagem} a ser INCLUSO: ')
        elemento = {
            'codigo': codigo,
            'nome': nome,
            'cpf': cpf
        }
        dados = lerJson(arquivo)
        dados.append(elemento)
        salvarJson(arquivo, dados)
        sleep(0.2)
        print('\n*** INCLUÍDO com SUCESSO! ***\n')
        sleep(0.2)
        print('Voltando ao MENU de AÇÕES...\n')
        sleep(0.5)

def listarElemento(arquivo, mensagem):
    print(f'===== LISTAR {mensagem.upper()} =====\n')
    dados = lerJson(arquivo)
    if len(dados) < 1:
        sleep(0.2)
        print(f'Nenhum(a) {mensagem.upper()} cadastrado(a)...\n')
        sleep(0.5)
        print('\nVoltando ao MENU de AÇÕES...\n')
        sleep(0.5)
    else:
        for elemento in dados:
            print(f" -> Código: {elemento['codigo']}\n")
            print(f" -> Nome: {elemento['nome']}\n")
            print(f" -> CPF: {elemento['cpf']}\n")
        print('\n-- FIM DA LISTA --\n')
        sleep(0.5)
        input('\nPressione ENTER para CONTINUAR...')
        sleep(0.2)

def atualizarElemento(arquivo, mensagem):
    print(f'===== ATUALIZAR {mensagem.upper()} =====\n')
    elemento = int(input(f'Insira o CÓDIGO do(a) {mensagem.upper()} que deseja ATUALIZAR: '))
    achou = False
    dados = lerJson(arquivo)
    for i, elementoAtual in enumerate(dados):
        if elementoAtual['codigo'] == elemento:
            print('\nENCONTRADO(A) no banco de dados!\n')
            sleep(0.2)
            codigo = int(input(f'Insira o novo(a) CÓDIGO do {mensagem.upper()}: '))
            nome = input(f'Insira o novo(a) NOME do {mensagem.upper()}: ')
            cpf = input(f'Insira o novo(a) CPF do {mensagem.upper()}: ')
            dicionario = {
                'codigo': codigo,
                'nome': nome,
                'cpf': cpf
            }
            dados[i] = dicionario
            salvarJson(arquivo, dados)
            sleep(0.2)
            print(f'\n*** {mensagem.upper()} ATUALIZADO(A) com SUCESSO! ***\n')
            achou = True
            input('Pressione ENTER para CONTINUAR...')
            sleep(0.5)
            break
    if not achou:
        naoEncontrado()

def excluirElemento(arquivo, mensagem):
    print(f'===== EXCLUIR {mensagem.upper()} =====\n')
    elemento = int(input(f'Insira o CÓDIGO do(a) {mensagem.upper()} que deseja EXCLUIR: '))
    achou = False
    dados = lerJson(arquivo)
    for elementoAtual in dados:
        if elementoAtual['codigo'] == elemento:
            print('\nENCONTRADO(A) no banco de dados!\n')
            sleep(0.2)
            print('Excluindo...')
            sleep(0.2)
            dados.remove(elementoAtual)
            salvarJson(arquivo, dados)
            print(f'\n{mensagem.upper()} EXCLUÍDO(A) com SUCESSO!!!\n')
            achou = True
            input('Pressione ENTER para CONTINUAR...')
            sleep(0.5)
            break
    if not achou:
        naoEncontrado()
#------------------------------------------------------------------------------------------
#----------DISCIPLINAS---------------------------------------------------------------------
def incluirDisciplinas(arquivo):
    print('===== INCLUIR DISCIPLINAS =====\n')
    codigo = int(input('Digite o CÓDIGO da DISCIPLINA a ser INCLUSA: '))
    achou = False
    dados = lerJson(arquivo)
    for elementoAtual in dados:
        if elementoAtual['codigo'] == codigo:
            sleep(0.2)
            print('\n!!! DISCIPLINA já CADASTRADA. !!!\n')
            sleep(0.2)
            achou = True
            print('Voltando ao MENU de AÇÕES...\n')
            sleep(0.5)
            break
    if not achou:
        nome = input('Digite o NOME da DISCIPLINA a ser INCLUSO: ')
        elemento = {
            'codigo': codigo,
            'nome': nome,
        }
        dados = lerJson(arquivo)
        dados.append(elemento)
        salvarJson(arquivo, dados)
        sleep(0.2)
        print('\n*** INCLUÍDO com SUCESSO! ***\n')
        sleep(0.2)
        print('Voltando ao MENU de AÇÕES...\n')
        sleep(0.5)

def listarDisciplinas(arquivo):
    print('===== LISTAR DISCIPLINAS =====\n')
    dados = lerJson(arquivo)
    if len(dados) < 1:
        sleep(0.2)
        print('Nenhuma DISCIPLINA cadastrada...\n')
        sleep(0.5)
        print('\nVoltando ao MENU de AÇÕES...\n')
        sleep(0.5)
    else:
        for elemento in dados:
            print(f" -> Código: {elemento['codigo']}\n")
            print(f" -> Nome: {elemento['nome']}\n")
        print('\n-- FIM DA LISTA --\n')
        sleep(0.5)
        input('\nPressione ENTER para CONTINUAR...')
        sleep(0.2)

def atualizarDisciplinas(arquivo):
    print('===== ATUALIZAR DISCIPLINAS =====\n')
    elemento = int(input('Insira o CÓDIGO da DISCIPLINA que deseja ATUALIZAR: '))
    achou = False
    dados = lerJson(arquivo)
    for i, elementoAtual in enumerate(dados):
        if elementoAtual['codigo'] == elemento:
            print('\nENCONTRADO(A) no banco de dados!\n')
            sleep(0.2)
            codigo = int(input('Insira o novo CÓDIGO da DISCIPLINA: '))
            nome = input('Insira o novo NOME da DISCIPLINA: ')
            dicionario = {
                'codigo': codigo,
                'nome': nome,
            }
            dados[i] = dicionario
            salvarJson(arquivo, dados)
            sleep(0.2)
            print('\n*** DISCIPLINA ATUALIZADA com SUCESSO! ***\n')
            achou = True
            input('Pressione ENTER para CONTINUAR...')
            sleep(0.5)
            break
    if not achou:
        naoEncontrado()
#----------------------------------------------------------------------------------------
#----------TURMAS------------------------------------------------------------------------
def incluirTurmas(arquivo):
    print('===== INCLUIR TURMAS =====\n')
    codigo = int(input("Digite o CÓDIGO da TURMA a ser INCLUSO: "))
    achou = False
    dados = lerJson(arquivo)
    for elementoAtual in dados:
        if elementoAtual['codigo'] == codigo:
            sleep(0.2)
            print('\n!!! TURMA já CADASTRADA. !!!\n')
            sleep(0.2)
            achou = True
            print('Voltando ao MENU de AÇÕES...\n')
            sleep(0.5)
            break
    if not achou:
        codigo2 = int(input("Digite o CÓDIGO do(a) PROFESSOR(A): "))
        codigo3 = int(input("Digite o CÓDIGO da DISCIPLINA: "))
        elemento = {
            'codigo': codigo,
            'codigo_professor': codigo2,
            'codigo_disciplina': codigo3
        }
        dados.append(elemento)
        salvarJson(arquivo, dados)
        sleep(0.2)
        print('\n*** INCLUÍDO com SUCESSO! ***\n')
        sleep(0.5)
        print('Voltando ao MENU de AÇÕES...\n')
        sleep(0.5)

def listarTurmas(arquivo):
    print('===== LISTAR TURMAS =====\n')
    dados = lerJson(arquivo)
    if len(dados) < 1:
        sleep(0.2)
        print('Nenhuma TURMA cadastrada...\n')
        sleep(0.5)
        print('\nVoltando ao MENU de AÇÕES...\n')
        sleep(0.5)
    else:
        for turma in dados:
            print(f" -> Código: {turma['codigo']}\n")
            print(f" -> Código do Professor: {turma['codigo_professor']}\n")
            print(f" -> Código da Disciplina: {turma['codigo_disciplina']}\n")
        print('\n-- FIM DA LISTA --\n')
        sleep(0.5)
        input('\nPressione ENTER para CONTINUAR...')
        sleep(0.2)

def atualizarTurmas(arquivo):
    print('===== ATUALIZAR TURMAS =====\n')
    turma = int(input('Insira o CÓDIGO da TURMA que deseja ATUALIZAR: '))
    achou = False
    dados = lerJson(arquivo)
    for i, elementoAtual in enumerate(dados):
        if elementoAtual['codigo'] == turma:
            print('\nENCONTRADO(A) no banco de dados!\n')
            sleep(0.2)
            codigo = int(input('Insira o novo CÓDIGO da TURMA: '))
            codigo2 = int(input('Insira o novo CÓDIGO do(a) PROFESSOR(A): '))
            codigo3 = int(input('Insira o novo CÓDIGO da DISCIPLINA: '))
            dicionario = {
                'codigo': codigo,
                'codigo_professor': codigo2,
                'codigo_disciplina': codigo3
            }
            dados[i] = dicionario
            salvarJson(arquivo, dados)
            sleep(0.2)
            print('\n*** TURMA ATUALIZADA com SUCESSO! ***\n')
            achou = True
            input('Pressione ENTER para CONTINUAR...')
            sleep(0.5)
            break
    if not achou:
        naoEncontrado()
#----------------------------------------------------------------------------------------
#----------MATRICULAS--------------------------------------------------------------------
def incluirMatriculas(arquivo):
    print('===== INCLUIR MATRICULAS =====\n')
    codigo = int(input("Digite o CÓDIGO da MATRICULA a ser INCLUSO: "))
    achou = False
    dados = lerJson(arquivo)
    for elementoAtual in dados:
        if elementoAtual['codigo'] == codigo:
            sleep(0.2)
            print('\n!!! MATRICULA já CADASTRADA. !!!\n')
            sleep(0.2)
            achou = True
            print('Voltando ao MENU de AÇÕES...\n')
            sleep(0.5)
            break
    if not achou:
        codigo2 = input("Digite o(s) CÓDIGO(S) da(s) TURMAS(S): ")
        codigo3 = input("Digite o(s) CÓDIGO(S) do(s) ESTUDANTE(S): ")
        matricula = {
            'codigo': codigo,
            'codigo_turma': codigo2,
            'codigo_estudante': codigo3
        }
        dados.append(matricula)
        salvarJson(arquivo, dados)
        sleep(0.2)
        print('\n*** INCLUÍDO com SUCESSO! ***\n')
        sleep(0.5)
        print('Voltando ao MENU de AÇÕES...\n')
        sleep(0.5)

def listarMatriculas(arquivo):
    print('===== LISTAR MATRICULAS =====\n')
    dados = lerJson(arquivo)
    if len(dados) < 1:
        sleep(0.2)
        print('Nenhuma MATRICULA cadastrada...\n')
        sleep(0.5)
        print('\nVoltando ao MENU de AÇÕES...\n')
        sleep(0.5)
    else:
        for matricula in dados:
            print(f" -> Código: {matricula['codigo']}\n")
            print(f" -> Código da(s) TURMA(S): {matricula['codigo_turma']}\n")
            print(f" -> Código do(s) ESTUDANTE(S): {matricula['codigo_estudante']}\n")
        print('\n-- FIM DA LISTA --\n')
        sleep(0.5)
        input('\nPressione ENTER para CONTINUAR...')
        sleep(0.2)

def atualizarMatriculas(arquivo):
    print('===== ATUALIZAR MATRICULAS =====\n')
    matricula = int(input('Insira o CÓDIGO da MATRICULA que deseja ATUALIZAR: '))
    achou = False
    dados = lerJson(arquivo)
    for i, elementoAtual in enumerate(dados):
        if elementoAtual['codigo'] == matricula:
            print('\nENCONTRADO(A) no banco de dados!\n')
            sleep(0.2)
            codigo = int(input('Insira o novo CÓDIGO da MATRICULA: '))
            codigo2 = input('Insira o(s) novo(s) CÓDIGO(S) da(s) TURMA(S): ')
            codigo3 = input('Insira o(s) novo(s) CÓDIGO(S) do(s) ESTUDANTE(S): ')
            dicionario = {
                'codigo': codigo,
                'codigo_turma': codigo2,
                'codigo_estudante': codigo3
            }
            dados[i] = dicionario
            salvarJson(arquivo, dados)
            sleep(0.2)
            print('\n*** MATRICULA ATUALIZADA com SUCESSO! ***\n')
            achou = True
            input('Pressione ENTER para CONTINUAR...')
            sleep(0.5)
            break
    if not achou:
        naoEncontrado()
#----------------------------------------------------------------------------------------
#----------JSON-------------------------------------------------------------------------------
def lerJson(arquivo):
    try:
        with open(arquivo, 'r', encoding="utf-8") as f:
            dados = json.load(f)
    except FileNotFoundError:
        dados = []
    except PermissionError:
        print(f"Erro de permissão: Você não tem permissão para acessar o arquivo {arquivo}.")
    return dados

def salvarJson(arquivo, dados):
    try:
        with open(arquivo, 'w', encoding="utf-8") as f:
            json.dump(dados, f)
    except Exception as e:
        print(f"Erro ao salvar arquivo: {str(e)}")
#----------------------------------------------------------------------------------------------

def erroOpcaoInexistente():
    print("\n*** ERRO!!! Digite apenas uma das opções listadas. ***\n")
    input('Pressione ENTER para CONTINUAR...')
    sleep(0.2)
    print('\nVoltando ao MENU ANTERIOR...\n')
    sleep(0.5)

def voltarMenuPrincipal():
    sleep(0.2)
    print('\nVoltando ao MENU PRINCIPAL...\n')
    sleep(0.5)

def naoEncontrado():
    sleep(0.2)
    print('\nNÃO ENCONTRADO no banco de dados!\n')
    sleep(0.2)
    print('Voltando ao MENU ANTERIOR...\n')
    sleep(0.5)

def valueErrorMsg():
    sleep(0.2)
    print("!!! Valor inválido !!!")
    sleep(0.2)
    input("Pressione ENTER para CONTINUAR...")
    sleep(0.5)

opc = 0
while True:
    try:
        opc = menuInicial()

        if opc == 1:
            print('***** [ESTUDANTES] MENU DE OPERAÇÕES *****\n')
            while True:
                opcEstudante = menuAcoes()
                if opcEstudante == 1:
                    incluirElemento(jsonEstudantes, "ESTUDANTES")
                elif opcEstudante == 2:
                    listarElemento(jsonEstudantes, "ESTUDANTES")
                elif opcEstudante == 3:
                    atualizarElemento(jsonEstudantes, "ESTUDANTES")
                elif opcEstudante == 4:
                    excluirElemento(jsonEstudantes, "ESTUDANTES")
                elif opcEstudante == 9:
                    voltarMenuPrincipal()
                    break
                else:
                    erroOpcaoInexistente()
                    continue

        elif opc == 2:
            print('***** [PROFESSORES] MENU DE OPERAÇÕES *****\n')
            while True:
                opcProfessores = menuAcoes()
                if opcProfessores == 1:
                    incluirElemento(jsonProfessores, "PROFESSORES")
                elif opcProfessores == 2:
                    listarElemento(jsonProfessores, "PROFESSORES")
                elif opcProfessores == 3:
                    atualizarElemento(jsonProfessores, "PROFESSORES")
                elif opcProfessores == 4:
                    excluirElemento(jsonProfessores, "PROFESSORES")
                elif opcProfessores == 9:
                    voltarMenuPrincipal()
                    break
                else:
                    erroOpcaoInexistente()
                    sleep(1)
                    continue

        elif opc == 3:
            print('***** [DISCIPLINAS] MENU DE OPERAÇÕES *****\n')
            while True:
                opcDisciplinas = menuAcoes()
                if opcDisciplinas == 1:
                    incluirDisciplinas(jsonDisciplinas)
                elif opcDisciplinas == 2:
                    listarDisciplinas(jsonDisciplinas)
                elif opcDisciplinas == 3:
                    atualizarDisciplinas(jsonDisciplinas)
                elif opcDisciplinas == 4:
                    excluirElemento(jsonDisciplinas, "DISCIPLINAS")
                elif opcDisciplinas == 9:
                    voltarMenuPrincipal()
                    break
                else:
                    erroOpcaoInexistente()
                    continue

        elif opc == 4:
            print('***** [TURMAS] MENU DE OPERAÇÕES *****\n')
            while True:
                opcTurmas = menuAcoes()
                if opcTurmas == 1:
                    incluirTurmas(jsonTurmas)
                elif opcTurmas == 2:
                    listarTurmas(jsonTurmas)
                elif opcTurmas == 3:
                    atualizarTurmas(jsonTurmas)
                elif opcTurmas == 4:
                    excluirElemento(jsonTurmas, "TURMAS")
                elif opcTurmas == 9:
                    voltarMenuPrincipal()
                    break
                else:
                    erroOpcaoInexistente()
                    continue

        elif opc == 5:
            print('***** [MATRÍCULAS] MENU DE OPERAÇÕES *****\n')
            while True:
                opcMatriculas = menuAcoes()
                if opcMatriculas == 1:
                    incluirMatriculas(jsonMatriculas)
                elif opcMatriculas == 2:
                    listarMatriculas(jsonMatriculas)
                elif opcMatriculas == 3:
                    atualizarMatriculas(jsonMatriculas)
                elif opcMatriculas == 4:
                    excluirElemento(jsonMatriculas, "MATRÍCULAS")
                elif opcMatriculas == 9:
                    voltarMenuPrincipal()
                    break
                else:
                    erroOpcaoInexistente()
                    continue

        elif opc == 9:
            print('Finalizando...')
            sleep(0.5)
            break

        else:
            erroOpcaoInexistente()
            continue
    except ValueError:
        valueErrorMsg()
    except TypeError as te:
        sleep(0.2)
        print("ERRO: ", te, "\n")
        sleep(0.5)
        input("Pressione ENTER para CONTINUAR...")

# FIM :)