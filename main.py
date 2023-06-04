import sqlite3
from time import sleep

banco = sqlite3.connect('listaDeTarefas.db')
cursor = banco.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Tarefas'")
tabela_existe = cursor.fetchone()

if not tabela_existe:
    cursor.execute("CREATE TABLE Tarefas ('tarefa' text ,'horário' text , 'dia_da_semana' text ) ")

def leiaInt(msg):


    while True:
        numero = input(msg)
        try:
            int_numero = int(numero)
            break
        except ValueError:
            print('Por favor digite um número para continuar!')

    return int_numero


def mostraTabela(msg):
    cursor.execute("SELECT rowid , tarefa , horário ,dia_da_semana  FROM Tarefas ORDER BY dia_da_semana")
    print('/=' * 35)
    print(msg)
    print('/=' * 35)
    print(f'{"N":<2}{"tarefa":<25}{"horário":>6}{"dia da semana":>32}')
    for linha in cursor.fetchall():

        print(f'{linha[0]:<2}{linha[1]:<25} {linha[2]:>6} {linha[3]:>32}  ')
    print('/=' * 35)
    sleep(1)




        

while True:
    print('/='* 35)
    print(f"{'Lista de tarefas': ^70}")
    print('/=' * 35)
    print(f'{"[1]Adicionar uma tarefa": <30}')
    print(f'{"[2]Remover uma tarefa": <30}')
    print(f'{"[3]Ver suas tarefas": <30}')
    print(f'{"[4]Edita tarefa": <30}')
    print(f'{"[5]Sair": <30}')
    print('/=' * 35)

    opcao = leiaInt('sua opção: ')

    print('/='* 35)
    if opcao >= 1 and opcao <=  4:
        while True:
            if opcao == 1:
                sleep(1)
                print(f'{"Nova tarefa": ^70}')
                print('/='* 35)
                tarefa = input('tarefa: ')

                horario = input('horario: ')
                semana = input('Dia da semana: ')
                cursor.execute("INSERT INTO Tarefas VALUES(?,?,?)",(tarefa,horario,semana))
                banco.commit()
                continua = 'adicionando sua tarefa'
            elif opcao == 2:
                sleep(1)
                mostraTabela(f'{"Deletar tarefa": ^70}')
                valor = leiaInt('Digite o número da tarefa que deseja deletar[0 para voltar ]: ')
                if valor == 0:
                    break
                cursor.execute("SELECT rowid FROM Tarefas")
                row = cursor.fetchone()
                if row:
                    rowid = row[0]
                    cursor.execute("DELETE FROM Tarefas WHERE rowid= ?",(rowid,))
                    if cursor.rowcount > 0:
                        print('Tarefa deletada com sucesso!')
                        banco.commit()
                        cursor.execute("SELECT rowid , * FROM Tarefas ")
                        row = cursor.fetchall()
                        for i , row in enumerate( row , start=1):
                            cursor.execute("UPDATE Tarefas SET rowid = ? WHERE rowid= ? " , (i , row[0]))
                        banco.commit()

                    else :
                        print("erro ao deletar a tarefa")
                else: 
                    print('numero da tarefa invalida!')
                continua = 'deletando sua tarefa'

            elif opcao == 3:
                sleep(1)
                mostraTabela(f'{"Suas tarefas": ^70}')
                continua = 'vendo suas tarefas'
                
            elif opcao == 4:
                mostraTabela('Editar tarefa')
                tarefa_id = leiaInt('Numero da tarefa que desaja editar[0 para voltar ao Menu]: ')
                if tarefa_id == 0:
                    break
                
                cursor.execute('SELECT * FROM Tarefas WHERE rowid= ?', (tarefa_id,))
                tarefa = cursor.fetchone()

                if tarefa:
                    nova_tarefa = input('Nova tarefa: ')
                    novo_horario = input('Novo horario: ')
                    nova_semana = input('Novo Dia da semana: ')
                    cursor.execute("UPDATE tarefas SET tarefa= ? , horário= ? , dia_da_semana= ? WHERE rowid= ?",
                                (nova_tarefa , novo_horario ,nova_semana, tarefa_id))
                    banco.commit()
                    print('Tarefa atualizada com sucesso!')

                else:
                    print('Numero da tarefa invalida!')

                continua = 'editando tarefa'
                
            if opcao >= 1 and opcao <=4:
                continuar = input(f'deseja continuar {continua}: ').upper()[0]
                if continuar == 'N':
                    break

    elif opcao == 5:
        print('saindo...')
        sleep(1)
        break

    else:
        print('Por favor digite uma opção valida!')

banco.close()