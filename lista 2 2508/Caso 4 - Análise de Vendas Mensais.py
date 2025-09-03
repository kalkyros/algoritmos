def loja():
    vendas = []
    for i in range(1, 31):
        venda = int(input(f'Informe o número de vendas do dia {i}: \n >>'))
        vendas.append(venda)
    totalvendas = sum(vendas)
    diamaisvendas = vendas.index(max(vendas)) + 1
    diamenosvendas = vendas.index(min(vendas)) + 1
    mediavendas = totalvendas / len(vendas)
    diasacimamedia = [i + 1 for i, v in enumerate(vendas) if v > mediavendas]
    print(f'Total de vendas no mês: {totalvendas}')
    print(f'Dia com mais vendas: {diamaisvendas} (Vendas: {max(vendas)})')
    print(f'Dia com menos vendas: {diamenosvendas} (Vendas: {min(vendas)})')
    print(f'Média de vendas por dia: {mediavendas:.2f}')
    print(f'Dias com vendas acima da média: {diasacimamedia}')
loja()