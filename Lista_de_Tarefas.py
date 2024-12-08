import time
import os

def Adicionar_Tarefa(Lista_Tarefas):

    os.system('cls')
    Tarefa = str(input('Digite a tarefa que deseja adicionar\nExemplo "Ir ao mercado"\nR: '))
    Prazo = str(input('\nDigite o prazo para terminar a tarefa\nExemplo "10 dias" ou "10/05/2023"\nR: '))
    Lista_Tarefas.append([Tarefa,Prazo])
    print('Tarefa adicionada com sucesso!')
    time.sleep(3)


def Excluir_Tarefa(Lista_Tarefas,Lista_Tarefas_Excluidas):

    os.system('cls')
    if len(Lista_Tarefas) == 0:
            print('Adicione pelo menos uma tarefa para excluir!')
            time.sleep(3)
            return

    Tarefa = int(input('Digite o numero da tarefa que deseja excluir\nR: '))
    while Tarefa > len(Lista_Tarefas) or Tarefa <= 0:
        Tarefa = int(input('\nNumero invalido! Digite novamente o numero da tarefa que deseja excluir\nR: '))

    Continuar = int(input(f'\nDeseja realmente excluir a tarefa "{Lista_Tarefas[Tarefa-1][0]}"?\n1- Sim\n2- Não\nR: '))
    while Continuar != 1 and Continuar != 2:
        Continuar = int(input(f'\nOpção Invalida!\nDeseja realmente excluir a tarefa "{Lista_Tarefas[Tarefa-1][0]}"?\n1- Sim\n2- Não\nR: '))


    if Continuar == 1:
        Lista_Tarefas_Excluidas.append(Lista_Tarefas[Tarefa-1])
        Lista_Tarefas.pop(Tarefa-1)

        print('Tarefa excluida com sucesso!')
        time.sleep(3)


def Concluir_Tarefa(Lista_Tarefas,Lista_Tarefas_Concluidas):

    os.system('cls')
    if len(Lista_Tarefas) == 0:
        print('Adicione pelo menos uma tarefa para concluir!')
        time.sleep(3)
        return

    Tarefa = int(input('Digite o nome da tarefa que deseja concluir: '))
    while Tarefa > len(Lista_Tarefas) or Tarefa <= 0:
        Tarefa = int(input('Numero invalido! Digite novamente o numero da tarefa que deseja concluir\nR: '))

    Continuar = int(input(f'\nDeseja realmente concluir a tarefa "{Lista_Tarefas[Tarefa-1][0]}"?\n1- Sim\n2- Não\nR: '))
    while Continuar != 1 and Continuar != 2:
        Continuar = int(input(f'\nOpção Invalida!\nDeseja realmente concluir a tarefa "{Lista_Tarefas[Tarefa-1][0]}"?\n1- Sim\n2- Não\nR: '))
    
    if Continuar == 1:
        Lista_Tarefas_Concluidas.append(Lista_Tarefas[Tarefa-1])
        Lista_Tarefas.pop(Tarefa-1)

        print('Tarefa concluida com sucesso!')
        time.sleep(3)


def Ver_Tarefas(Lista_Tarefas):
    
    os.system('cls')
    if len(Lista_Tarefas) == 0:
        print('Adicione pelo menos um tarefa para conseguir ver ela!')
        time.sleep(3)
        return

    print('* Lista de Tarefas em Andamento *')

    for i in range(len(Lista_Tarefas)):
        print(f'{i+1}) Nome: {Lista_Tarefas[i][0]} | Prazo: {Lista_Tarefas[i][1]}')
    
    Continuar = int(input('\nDigite 1 para voltar\nR: '))
    while Continuar != 1:
        Continuar = int(input('\nOpcao invalida! Digite 1 para voltar\nR: '))


def Ver_Tarefas_Excluidas(Lista_Tarefas_Excluidas):

    os.system('cls')
    if len(Lista_Tarefas_Excluidas) == 0:
        print('Exclua pelo menos um tarefa para conseguir ver ela!')
        time.sleep(3)
        return

    print('* Lista de Tarefas Excluidas *')

    for i in range(len(Lista_Tarefas_Excluidas)):
        print(f'{i+1}) {Lista_Tarefas_Excluidas[i][0]}')
    
    Continuar = int(input('\nDigite 1 para voltar\nR: '))
    while Continuar != 1:
        Continuar = int(input('\nOpcao invalida! Digite 1 para voltar\nR: '))


def Ver_Tarefas_Concluidas(Lista_Tarefas_Concluidas):

    os.system('cls')
    if len(Lista_Tarefas_Concluidas) == 0:
        print('Conclua pelo menos um tarefa para conseguir ver ela!')
        time.sleep(3)
        return

    print('* Lista de Tarefas Concluidas *')

    for i in range(len(Lista_Tarefas_Concluidas)):
        print(f'{i+1}) {Lista_Tarefas_Concluidas[i][0]}')
    
    Continuar = int(input('\nDigite 1 para voltar\nR: '))
    while Continuar != 1:
        Continuar = int(input('\nOpcao invalida! Digite 1 para voltar\nR: '))


def Modificar_Tarefa(Lista_Tarefas):

    os.system('cls')
    if len(Lista_Tarefas) == 0:
        print('Adicione pelo menos um tarefa para conseguir modificar ela!')
        time.sleep(3)
        return

    Tarefa = int(input('Digite o numero da tarefa que deseja modificiar\nR: '))
    while Tarefa > len(Lista_Tarefas) or Tarefa <= 0:
        Tarefa = int(input('\nNumero invalido! Digite novamente o numero da tarefa que deseja modificar\nR: '))

    Continuar = int(input(f'\nDeseja realmente modificar a tarefa "Nome: {Lista_Tarefas[Tarefa-1][0]} | Prazo: {Lista_Tarefas[Tarefa-1][1]}"?\n1- Sim\n2- Não\nR: '))
    while Continuar != 1 and Continuar != 2:
        Continuar = int(input(f'\nOpção Invalida!\nDeseja realmente modificar a tarefa "Nome: {Lista_Tarefas[Tarefa-1][0]} | Prazo:{Lista_Tarefas[Tarefa-1][1]}"?\n1- Sim\n2- Não\nR: '))

    if Continuar == 2:
        return
    
    Tipo = int(input('\nOque você deseja modificar\n1- Nome\n2- Prazo\nR: '))
    while Tipo != (1 and 2):
        Tipo = int(input('\nOpção invalida!\nDigite novamente oque você deseja modificar\n1- Nome\n2- Prazo\nR: '))
    
    if Tipo == 1:
        Mod = str(input('\nDigite o novo nome da tarefa\nExemplo: "Ir ao mercado"\nR: '))
        Lista_Tarefas[Tarefa-1][0] = Mod
    else:
        Mod = str(input('\nDigite o novo prazo da tarefa\nExemplo: "10 dias" ou "10/05/2023"\nR: '))
        Lista_Tarefas[Tarefa-1][1] = Mod

    print('Tarefa modificada com sucesso!')
    time.sleep(3)


def Recuperar_Tarefa_Excluida(Lista_Tarefas,Lista_Tarefas_Excluidas):
    
    os.system('cls')
    if len(Lista_Tarefas) == 0:
        print('Adicione uma tarefa primeiro!')
        time.sleep(3)
        return
    
    if len(Lista_Tarefas_Excluidas) == 0:
        print('Exclua uma tarefa primeiro para recuperar!')
        time.sleep(3)
        return

    Tarefa = int(input('Digite o numero da tarefa excluida que deseja recuperar\nR: '))
    while Tarefa > Lista_Tarefas_Excluidas or Lista_Tarefas_Excluidas <= 0:
        Tarefa = int(input('\nNumero Invalido! Digite novamente o numero da tarefa excluida que deseja recuperar\nR: '))

    Lista_Tarefas.append(Lista_Tarefas_Excluidas[Tarefa-1])
    Lista_Tarefas.pop(Tarefa-1)

    print('Tarefa recuperada com sucesso!')
    time.sleep(3)


def Recuperar_Tarefa_Concluidas(Lista_Tarefas,Lista_Tarefas_Concluidas):

    os.system('cls')
    if len(Lista_Tarefas) == 0:
        print('Adicione uma tarefa primeiro!')
        time.sleep(3)
        return
    
    if len(Lista_Tarefas_Concluidas) == 0:
        print('Conclua uma tarefa primeiro para recuperar!')
        time.sleep(3)
        return

    Tarefa = int(input('Digite o numero da tarefa concluida que deseja recuperar\nR: '))
    while Tarefa > Lista_Tarefas_Concluidas or Lista_Tarefas_Concluidas <= 0:
        Tarefa = int(input('\nNumero Invalido! Digite novamente o numero da tarefa excluida que deseja recuperar\nR: '))

    Lista_Tarefas.append(Lista_Tarefas_Concluidas[Tarefa-1])
    Lista_Tarefas.pop(Tarefa-1)

    print('Tarefa recuperada com sucesso!')
    time.sleep(3)


def Main():
    Lista_Tarefas = []
    Lista_Tarefas_Concluidas = []
    Lista_Tarefas_Excluidas = []

    while True:
        os.system('cls')
        Opcao = int(input('* Menu *\n1- Adicionar tarefa\n2- Excluir tarefa\n3- Concluir uma tarefa\n4- Ver tarefas ativas\n5- Ver tarefas excluidas\n6- Ver tarefas concluidas\n7- Modificar uma tarefa\n8- Recuperar uma tarefa excluida\n9- Recuperar uma tarefa concluida\n10- Sair\nR: '))

        if Opcao == 10:
            print('Programa encerrado!')
            break
        elif Opcao == 1:
            Adicionar_Tarefa(Lista_Tarefas)
        elif Opcao == 2:
            Excluir_Tarefa(Lista_Tarefas,Lista_Tarefas_Excluidas)
        elif Opcao == 3:
            Concluir_Tarefa(Lista_Tarefas,Lista_Tarefas_Concluidas)
        elif Opcao== 4:
            Ver_Tarefas(Lista_Tarefas)
        elif Opcao == 5:
            Ver_Tarefas_Excluidas(Lista_Tarefas_Excluidas)
        elif Opcao == 6:
            Ver_Tarefas_Concluidas(Lista_Tarefas_Concluidas)
        elif Opcao == 7:
            Modificar_Tarefa(Lista_Tarefas)
        elif Opcao == 8: 
            Recuperar_Tarefa_Excluida(Lista_Tarefas,Lista_Tarefas_Excluidas)
        elif Opcao == 9:
            Recuperar_Tarefa_Concluidas(Lista_Tarefas,Lista_Tarefas_Concluidas)


Main()
        
