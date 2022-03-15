'''

Implemente uma função que calcula a área de um mapa que é acessível por
um robot a partir de um determinado ponto.
O mapa é quadrado e representado por uma lista de strings, onde um '.' representa
um espaço vazio e um '*' um obstáculo.
O ponto inicial consistirá nas coordenadas horizontal e vertical, medidas a 
partir do canto superior esquerdo.
O robot só consegue movimentar-se na horizontal ou na vertical. 

'''

def moves(mapa, x, y):
    l = [(x+1,y), (x-1, y), (x, y+1), (x, y-1)]
    return list(filter(lambda t: t[0] >= 0 and t[0] < len(mapa) and t[1] >= 0 and t[1] < len(mapa) and mapa[t[1]][t[0]] == '.', l))

def area(p,mapa):
    vis = {p}
    queue = [p]
    while queue:
        v = queue.pop(0)
        for x,y in moves(mapa, v[0], v[1]):
            if (x,y) not in vis:
                vis.add((x,y))
                queue.append((x,y))
    return len(vis)
