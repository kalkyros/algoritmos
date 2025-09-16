pedidos = [
    {
        "cliente":"ana",
        "itens": [
            {"prato":"lasanha", "preco": 30},
            {"prato":"suco de laranja", "preco": 8}
        ]
    },
    {
        "cliente":"bruno",
        "itens": [
            {"prato":"pizza", "preco": 40},
            {"prato":"refrigerante", "preco": 6},
            {"prato":"sobremesa", "preco": 12}
        ]
    },
    {
        "cliente":"carla",
        "itens": [
            {"prato":"pizza", "preco": 40},
            {"prato":"suco de laranja", "preco": 8}
        ]
    }
]

def valortotal(cliente):
    
    for pedido in pedidos:
        if pedido["cliente"] == cliente:
            total = 0
            for item in pedido["itens"]:
                total += item["preco"]
            return total

def pratomaisvendido():
    contagem = {}
    for pedido in pedidos:
        for item in pedido["itens"]:
            prato = item["prato"]
            if prato in contagem:
                contagem[prato] += 1
            else:
                contagem[prato] = 1
    maisvendido = max(contagem, key=contagem.get)
    return maisvendido

def ranking():
    lista = []
    for pedido in pedidos:
        cliente = pedido["cliente"]
        total = 0
        for item in pedido["itens"]:
            total += item["preco"]
        lista.append((cliente, total))
    lista.sort(key=lambda x: x[1], reverse=True)
    return lista[:3]

print(valortotal("ana"))
print(pratomaisvendido())
print(ranking())