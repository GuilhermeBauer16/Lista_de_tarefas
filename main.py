
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
    while True:
       opcao = input('Digite sua opção: ')
       try:
           int_opcao = int(opcao)
           break
       except ValueError:
           print('Por favor digite um número')

    if int_opcao == 1:
        print('Nova tarefa')

    elif int_opcao == 2:
        print('Deletar tarefa')
    
    elif int_opcao == 3:
        print('ver suas tarefas')

    elif int_opcao == 4:
        print('saindo...')
        break

    elif int_opcao == 0 or int_opcao > 4:
        print('Por favor digite uma opção valida!')
