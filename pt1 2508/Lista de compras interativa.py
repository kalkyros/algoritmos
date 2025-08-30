estoque = []

def armazenamento(estoque):
    while True:
        adicionar = input('deseja adicionar algo? \n >>')
        estoque.append(adicionar)
        quest = input('deseja adicionar mais alguma coisa meo? \n >>>>')

        if quest == 's':
            continue

        elif quest == 'n':
            break
        
        else:
            print('COMANDO INVALIDO')
            

    print(estoque)
armazenamento(estoque)