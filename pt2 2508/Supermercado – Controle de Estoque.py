def mercado():
    produtos = [
        ['Arroz', 20, 7.50], 
        ['Feijão', 8, 9.80],
        ['Macarrão', 18, 6.20],
        ['Açúcar', 20, 5.00],
        ['Sal', 17, 4.50],
        ['Óleo', 3, 10.00],
        ['Leite', 4, 17.00],
        ['Pão', 3, 1.50],
        ['Manteiga', 8, 14.00],
        ['Café', 15, 25.00]
    ]

    
    valortotalestoque = sum(qtd * preco for nome, qtd, preco in produtos)
    print(f'Valor total em estoque: R$ {valortotalestoque:.2f}')
    
    produtomaisvalioso = max(produtos, key=lambda item: item[1] * item[2])
    nomemaisvalioso, qtdmaisvalioso, preco_mais_valioso = produtomaisvalioso
    valormaisvalioso = qtdmaisvalioso * preco_mais_valioso  
    print(f'Produto de maior valor total: {nomemaisvalioso} - R$ {valormaisvalioso:.2f}')
    
    produtos_estoque_baixo = [nome for nome, qtd, preco in produtos if qtd < 5]
    print('Produtos com estoque abaixo de 5 unidades:', produtos_estoque_baixo)
    
    nome_busca = input('Informe o nome do produto para busca: ')    
    produto_encontrado = next((item for item in produtos if item[0].lower() == nome_busca.lower()), None)
    if produto_encontrado:
        nome, qtd, preco = produto_encontrado
        print(f'Produto encontrado: {nome} - Quantidade: {qtd} - Preço unitário: R$ {preco:.2f}')

    else:
        print('Produto não encontrado.')
mercado()