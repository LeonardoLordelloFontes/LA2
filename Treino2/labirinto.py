'''

Implemente uma função que calcula um dos caminhos mais curtos para atravessar
um labirinto. O mapa do labirinto é quadrado e representado por uma lista 
de strings, onde um ' ' representa um espaço vazio e um '#' um obstáculo.
O ponto de entrada é o canto superior esquerdo e o ponto de saída o canto
inferior direito. A função deve devolver uma string com as instruções para
atravesar o labirinto. As instruções podem ser 'N','S','E','O'.

'''

def moves(mapa, x, y):
    l = [(x+1,y), (x-1, y), (x, y+1), (x, y-1)]
    return list(filter(lambda t: t[0] >= 0 and t[0] < len(mapa) and t[1] >= 0 and t[1] < len(mapa) and mapa[t[1]][t[0]] == ' ', l))

def bfs(mapa):
    pai = {}
    dist = {(0,0): 0}
    queue = [(0,0)]
    while queue:
        v = queue.pop(0)
        if v == (len(mapa)-1, len(mapa)-1):
            break
        
        for move in moves(mapa, v[0], v[1]):
            if move not in pai:
                dist[move] = dist[v] + 1
                pai[move] = v
                queue.append(move)
            
            elif dist[v] + 1 < dist[move]:
                dist[move] = dist[v] + 1
                pai[move] = v
    return pai

def caminho(mapa):
    r = ""
    dir = {(0,-1): 'N', (0,1): 'S', (1,0): 'E', (-1,0): 'O'}
    pai = bfs(mapa)
    d = (len(mapa)-1, len(mapa)-1)
    while d != (0,0):
        r = dir[(d[0]-pai[d][0], d[1]-pai[d][1])] + r
        d = pai[d]
    return r
