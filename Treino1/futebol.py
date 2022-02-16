def tabela(jogos):
    d = {}
    for jogo in jogos:
        if jogo[0] not in d:
            d[jogo[0]] = [0,0,0]
        if jogo[2] not in d:
            d[jogo[2]] = [0,0,0]
        
        d[jogo[0]][1] += jogo[1]
        d[jogo[0]][2] += jogo[3]
        d[jogo[2]][1] += jogo[3]
        d[jogo[2]][2] += jogo[1]
        
        if jogo[1] > jogo[3]:
            d[jogo[0]][0] += 3
        
        elif jogo[3] > jogo[1]:
            d[jogo[2]][0] += 3
            
        else:
            d[jogo[0]][0] += 1
            d[jogo[2]][0] += 1
        
    l = list(d.items())
    l.sort(key=lambda t: t[0])
    l.sort(key=lambda t: t[1][1] - t[1][2], reverse=True)
    l.sort(key=lambda t: t[1][0], reverse=True)
    return list(map(lambda t: (t[0], t[1][0]),l))
