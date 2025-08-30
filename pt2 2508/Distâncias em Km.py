def viagem():
    import math
    distancias = []
    for i in range(6):
        distancia = float(input(f'Informe a distância da viagem {i+1} em Km: '))
        distancias.append(distancia)
    distancia_total = sum(distancias)
    maior_distancia = max(distancias)
    menor_distancia = min(distancias)
    media_distancias = math.ceil(distancia_total / len(distancias))
    print(f'Distância total percorrida: {distancia_total} Km')
    print(f'Maior distância: {maior_distancia} Km')
viagem()