import sqlite3
from time import sleep
banco = sqlite3.connect('listaDeTarefas.db')
cursor = banco.cursor()
# cursor.execute("CREATE TABLE Tarefas ('tarefa' text ,'horário' integer , 'dia da semana' text ) ")
c = 0
def leiaInt(msg):


    while True:
        numero = input(msg)
        try:
            int_numero = int(numero)
            break
        except ValueError:
            print('Por favor digite um número para continuar!')

    return int_numero

while True:
    print('/='* 20)
    print(f"{'Lista de tarefas': ^40}")
    print('/=' * 20)
    print('''
[1]Adicionar uma tarefa
[2]Remover uma tarefa
[3]Ver suas tarefas
[4]Sair ''')
    print('/=' * 20)


    opcao = leiaInt('sua opção:')

    print('/=' * 20)
    if opcao >= 1 and opcao <=  3:
        while True:
            if opcao == 1:
                sleep(1)
                print('Nova tarefa')
                print('/=' * 20)
                tarefa = input('tarefa: ')
                horario = leiaInt('horario: ')
                semana = input('Dia da semana: ')
                cursor.execute("INSERT INTO Tarefas VALUES(?,?,?)",(tarefa,horario,semana))
                banco.commit()
                continua = 'adicionando sua tarefa'
            elif opcao == 2:
                sleep(1)
                print('Deletar tarefa')
                continua = 'deletando sua tarefa'

            elif opcao == 3:
                sleep(1)
                print('ver suas tarefas')
                print('/=' * 20)
                # print(f'{"N":< 2 }{"tarefa":< 10}{"horario":>10}{"dia da semana":> 10}')
                cursor.execute("SELECT * FROM Tarefas")
                for linha in cursor.fetchall():
                    for values in linha:
                        print(values , end=" ")
                    print()

                print('/=' * 20)
                sleep(1)
                continua = 'vendo suas tarefas'



            if opcao >= 1 and opcao <=3:
                continuar = input(f'deseja continuar {continua}:').upper()[0]
                if continuar == 'N':
                    break

    elif opcao == 4:
        print('saindo...')
        sleep(1)
        break

    else:
        print('Por favor digite uma opção valida!')

banco.close()