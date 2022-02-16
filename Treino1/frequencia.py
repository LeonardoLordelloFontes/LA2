def frequencia(texto):
    d = {}
    palavras = texto.split()
    for palavra in palavras:
        if palavra not in d:
            d[palavra] = 0
        d[palavra] += 1
    
    l = list(d.items())
    l.sort(key=lambda t: t[0])
    l.sort(key=lambda t: t[1], reverse=True)
    return list(map(lambda t: t[0], l))
