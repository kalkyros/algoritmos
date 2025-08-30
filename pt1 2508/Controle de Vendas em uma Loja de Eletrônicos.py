vendas = []
total = 0
mais_caro = 0
mais_barato = float('inf')
produto_mais_caro = ''
produto_mais_barato = ''
produto_procurado = input('Qual produto você quer procurar? \n >>>')
encontrado = False
while True:
    nome = input('Nome do produto (ou "sair" para encerrar): \n >>>')
    if nome.lower() == 'sair':
        break
    try:
        preco = float(input('Preço do produto: \n >>>'))
    except ValueError:
        print('Preço inválido. Tente novamente.')
        continue

    vendas.append((nome, preco))
    total += preco

    if preco > mais_caro:
        mais_caro = preco
        produto_mais_caro = nome

    if preco < mais_barato:
        mais_barato = preco
        produto_mais_barato = nome

    if nome.lower() == produto_procurado.lower():
        encontrado = True
    if encontrado:
        print(f'O produto "{produto_procurado}" foi vendido.')
    else:  
        print(f'O produto "{produto_procurado}" não foi vendido.')