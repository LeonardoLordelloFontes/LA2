def aloca(prefs):
    l = []
    d = {}
    for aluno in sorted(prefs):
        alocado = False
        for nota in prefs[aluno]:
            if nota not in d:
                d[nota] = True
                alocado = True
                break
        
        if not alocado:
            l.append(aluno)
            
    return l
