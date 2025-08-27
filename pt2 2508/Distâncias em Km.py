# 1. Receba as distâncias percorridas em 6 viagens e armazene em uma lista.
# 2. Calcule a distância total percorrida.
# 3. Mostre a maior e a menor distância.
# 4. Calcule a média das distâncias arredondada para cima (use math.ceil).

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