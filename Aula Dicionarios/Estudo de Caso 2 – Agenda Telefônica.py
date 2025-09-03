agenda = {}

while True:
    nome = input('insira o nome do contato: \n >')
    telefone = input('insira o telefone do contato: \n >')
    parar = input('deseja adicionar mais algum contato? \n >')

    agenda[nome] = telefone

    if parar.lower() not in ['s', 'S', 'sim', 'Sim']:
        break

print(agenda)
for nome, telefone in agenda.items():
    print(f'o contato {nome} possui o telefone {telefone}')