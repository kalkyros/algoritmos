def aula():
    dias = ['segunda', 'terça', 'quarta', 'quinta', 'sexta']
    presencas = {}
    for dia in dias:
        presentes = input(f'Quem esteve presente na {dia}? (separe os nomes por vírgula) \n >>>')
        listapresenca = [nome.strip() for nome in presentes.split(',')]
        for nome in listapresenca:
            if nome in presencas:
                presencas[nome] += 1
            else:
                presencas[nome] = 1
    tododias = [nome for nome, count in presencas.items() if count == len(dias)]
    faltaumdia = [nome for nome, count in presencas.items() if count < len(dias)]
    print(f'Alunos presentes todos os dias: {", ".join(tododias)}')
    print(f'Alunos que faltaram ao menos um dia: {", ".join(faltaumdia)}')
aula()