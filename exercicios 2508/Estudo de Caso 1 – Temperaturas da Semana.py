temperaturas = []

for i in range(1, 8):
    temp = float(input(f'informe a temperatura do dia {i}: \n >>'))
    temperaturas.append(temp)

def tempmed(temperaturas):
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

media = tempmed(temperaturas)
maior = max(temperaturas)
menor = min(temperaturas)
acima = tempmediaup(media, temperaturas)

print(f'a menor temperatura foi de {menor}')
print(f'a maior temperatura foi de {maior}')
print(f'a media das temperaturas foi de {media}')
print(f'os dias com temperaturas acima da media foram {acima}')