# 1. Crie um dicionário chamado aluno com as chaves "nome", "idade" e "curso".
aluno = {
    "aluno" : "lindolfo",
    "idade" : 18,
    "curso" : "eng. de software"
}

print(aluno)

# Em seguida, exiba apenas o nome do aluno.
print(f'{aluno["aluno"]}')

print('\n' + '_'*70 + '\n')

# 2. Adicione uma nova chave "nota" com valor 9.5 ao dicionário aluno.
nota = {
    "nota" : 9.5
}

aluno.update(nota)

print(aluno)

# Depois, remova a chave "idade"
del aluno["idade"]

print(aluno)

print('\n' + '_'*70 + '\n')

# 3. Dado o dicionário abaixo, escreva um código que exiba cada produto e seu preço: produtos = {"Arroz": 15.90, "Feijão": 9.50, "Macarrão": 4.20}
produtos = {"Arroz": 15.90, "Feijão": 9.50, "Macarrão": 4.20}

for key, value in produtos.items():
    print(f'R${value:.2f} {key}')

print('\n' + '_'*70 + '\n')

# 4. Dado o dicionário aluno, verifique se existe a chave "curso".
if aluno["curso"]:
    print('chave existente')
else:
    print('vai estudar')

print('\n' + '_'*70 + '\n')

# 5. Crie um dicionário chamado turma que contenha dois alunos, cada um com nome e nota.
turma = {
    "nome1" : "manuela",
    "nome2" : "kauan",
    "nota1" : 9.5,
    "nota2" : 9
}

# Depois, exiba o nome do primeiro aluno e a nota do segundo aluno.
print(turma)
print(f'nome do primeiro aluno: {turma["nome1"]}')
print(f'nota do segundo aluno: {turma["nota2"]}')

print('\n' + '_'*70 + '\n')

# 6. Crie um dicionário representando um carro com as chaves: marca, modelo e ano.
carro = {
    'marca' : 'bmw',
    'modelo' : 'm3 gtr (most wanted)',
    'ano' : 2001
}
print(carro)

# a. Adicione ao dicionário do carro a chave 'cor'.
cor = {
    'cor' : 'prata com adesivos azul'
}

carro.update(cor)

print(carro)

print('\n' + '_'*70 + '\n')

# b. Crie um dicionário de notas de 3 alunos (nome como chave, nota como valor).
notas = {
    'ana luiza' : 9.2,
    'mariana' : 6.8,
    'paulo' : 8.5
}

print(notas)

# c. Acesse a nota de um dos alunos e exiba.
print(f'nota de um aluno expecifico: {notas["ana luiza"]}')

# d. Remova um aluno do dicionário de notas.
del notas["mariana"]

print(notas)

print('\n' + '_'*70 + '\n')