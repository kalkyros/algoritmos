produto = {}

while True:
    nome = input('insira o nome do produto: \n >')
    preco = float(input('insira o valor do produto: \n >'))
    estoque = int(input('insira a quantidade do produto em estoque: \n >'))
    parar = input('deseja adicionar mais algum produto? \n >')

    produto[nome] = {'preco':preco, 'estoque':estoque}

    if parar.lower() not in ['s', 'S', 'sim', 'Sim']:
        break

for nome, dados in produto.items():
    print(f'o produto {nome} custa R${dados['preco']} e possui {dados['estoque']} unidades em estoque')