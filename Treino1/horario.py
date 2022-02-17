def horario(ucs,alunos):
    l = []
    for aluno in alunos:
        d = {}
        semanais = 0
        invalid = False
        for uc in alunos[aluno]:
            
            if uc in ucs and not invalid:
                if ucs[uc][0] not in d:
                    d[ucs[uc][0]] = set()
                    
                for n in range(ucs[uc][1]+1, ucs[uc][1]+ucs[uc][2]+1):
                    if n in d[ucs[uc][0]]:
                        invalid = True
                        break
                    
                    else:
                        d[ucs[uc][0]].add(n)
                        semanais += 1
            else:
                invalid = True
                break
        
        if not invalid:
            l.append((aluno, semanais))
    
    l.sort(key=lambda t: t[0])
    l.sort(key=lambda t: t[1], reverse=True)
    return l
