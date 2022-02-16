def apelidos(nomes):
    l = []
    for nome in nomes:
        l.append( (nome, nome.count(" ")) )
    l.sort(key=lambda t: t[0])
    l.sort(key=lambda t: t[1])
    return list(map(lambda t: t[0], l))
