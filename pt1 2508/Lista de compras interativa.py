# Faça um programa que:
# 1. Permita ao usuário adicionar itens a uma lista de compras.
# 2. Caso o usuário digite "sair", o programa encerra.
# 3. Mostre a lista final de compras organizada em ordem alfabética.

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