# Crie um programa que:
# 1. Receba as temperaturas de 7 dias e armazene em uma lista.
# 2. Mostre a média das temperaturas da semana.
# 3. Informe o dia mais quente e o dia mais frio.
# 4. Mostre quantos dias ficaram acima da média.

temperaturas = []

for i in range(1, 8):
    temp = float(input(f'informe a temperatura do dia {i}: \n >>'))
    temperaturas.append(temp)

def temp_med(temperaturas):
    result = 0
    for n in temperaturas:
        result = n
    return result/len(temperaturas)

def tempmediaup(media, temperaturas):
    medup = 0
    for n in temperaturas:
        if n > media:
            medup += 1
    return medup

media = temp_med(temperaturas)
maior = max(temperaturas)
menor = min(temperaturas)
acima = tempmediaup(media, temperaturas)

print(f'a menor temperatura foi de {menor}')
print(f'a maior temperatura foi de {maior}')
print(f'a media das temperaturas foi de {media}')
print(f'os dias com temperaturas acima da media foram {acima}')