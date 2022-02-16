def cruzamentos(ruas):
    d = {}
    for rua in ruas:
        if rua[0] not in d:
            d[rua[0]] = 0
        
        if rua[-1] not in d:
            d[rua[-1]] = 0
    
        if rua[0] == rua[-1]:
            d[rua[0]] += 1
        else:
            d[rua[0]] += 1
            d[rua[-1]] += 1
            
    l = list(d.items())
    l.sort(key=lambda t: t[0])
    l.sort(key=lambda t: t[1])
    return l
