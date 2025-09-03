def evento():
    palestra = ["beatriz", "manuela", "nycolle"]
    workshop = ["manuela", "ana beatriz", "erica"]
    mesaredonda = ["manuela", "vitoria", "davi"]
    
    todosparticipantes = set(palestra) | set(workshop) | set(mesaredonda)
    todasatividades = set(palestra) & set(workshop) & set(mesaredonda)
    umatividade = (set(palestra) ^ set(workshop)) ^ set(mesaredonda)
    
    print(f'Participantes de todas as atividades: {", ".join(todasatividades)}')
    print(f'Participantes de apenas uma atividade: {", ".join(umatividade)}')
    print(f'Todos os participantes únicos: {", ".join(todosparticipantes)}')
    print(f'Número total de participantes distintos: {len(todosparticipantes)}')
evento()