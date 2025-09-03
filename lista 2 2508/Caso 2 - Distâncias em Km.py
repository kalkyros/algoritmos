import math
distancias = []
for i in range(6):
    distancia = float(input(f'Informe a distância da viagem {i+1} em Km: '))
    distancias.append(distancia)
distanciatotal = sum(distancias)
maiordistancia = max(distancias)
menordistancia = min(distancias)
mediadistancias = math.ceil(distanciatotal / len(distancias))
print(f'Distância total percorrida: {distanciatotal} Km')
print(f'Maior distância: {maiordistancia} Km')