# • Cada dia da semana terá uma lista com os nomes dos presentes.
# • No final, ela precisa:
# 1. Saber quais alunos estiveram presentes todos os dias.
# 2. Saber quais alunos faltaram em pelo menos um dia.
# 3. Saber o número total de presenças por aluno

dias = ['segunda', 'terça', 'quarta', 'quinta', 'sexta']
presencas = {}
for dia in dias:
    presentes = input(f'Quem esteve presente na {dia}? (separe os nomes por vírgula) \n >>>')
    lista_presentes = [nome.strip() for nome in presentes.split(',')]
    for nome in lista_presentes:
        if nome in presencas:
            presencas[nome] += 1
        else:
            presencas[nome] = 1
todos_os_dias = [nome for nome, count in presencas.items() if count == len(dias)]
faltaram_ao_menos_um_dia = [nome for nome, count in presencas.items() if count < len(dias)]
print(f'Alunos presentes todos os dias: {", ".join(todos_os_dias)}')
print(f'Alunos que faltaram ao menos um dia: {", ".join(faltaram_ao_menos_um_dia)}')