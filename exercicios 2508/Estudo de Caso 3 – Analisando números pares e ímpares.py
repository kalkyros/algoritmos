pares = []
impares = []

def numero():
    for i in range(10):
        num = int(input(f'digite o {i+1}° numero: \n>> '))
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

    print(f'quantidade de numeros pares: {len(pares)}')
    print(f'quantidade de numeros impares: {len(impares)}')
numero()