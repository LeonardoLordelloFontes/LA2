'''

Implemente uma função que calcula o menor custo de atravessar uma região de
Norte para Sul. O mapa da região é rectangular, dado por uma lista de strings,
onde cada digito representa a altura de cada ponto. Só é possível efectuar 
movimentos na horizontal ou na vertical, e só é possível passar de um ponto
para outro se a diferença de alturas for inferior ou igual a 2, sendo o custo 
desse movimento 1 mais a diferença de alturas. O ponto de partida (na linha
mais a Norte) e o ponto de chegada (na linha mais a Sul) não estão fixados à
partida, devendo a função devolver a coordenada horizontal do melhor
ponto para iniciar a travessia e o respectivo custo. No caso de haver dois pontos
com igual custo, deve devolver a coordenada mais a Oeste.

'''

def possibleMoves(mapa, x, y):
    l = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    return list(filter(lambda t: t[0] >= 0 and t[0] < len(mapa[0]) and t[1] >= 0 and t[1] < len(mapa) and abs(int(mapa[y][x]) - int(mapa[t[1]][t[0]])) <= 2, l))

def dijkstra(mapa, adj, o):
    dist = {o: 0}
    orla = {o}
    while orla:
        v = min(orla,key=lambda x:dist[x])
        if v[1] == len(mapa) - 1:
            break
        orla.remove(v)
        for d in adj[v]:
            if d not in dist:
                orla.add(d)
                dist[d] = float("inf")
            if dist[v] + adj[v][d] < dist[d]:
                dist[d] = dist[v] + adj[v][d]
    
    return v[1], dist[v]
 
def travessia(mapa):
    adj = {}
    menores = []
    for i in range(len(mapa)):
        for j in range(len(mapa[0])):
            for x,y in possibleMoves(mapa, j, i):
                if (j,i) not in adj:
                    adj[(j,i)] = {}
                if (x,y) not in adj:
                    adj[(x,y)] = {}
                adj[(j,i)][(x,y)] = abs(int(mapa[i][j]) - int(mapa[y][x])) + 1
                adj[(x,y)][(j,i)] = abs(int(mapa[i][j]) - int(mapa[y][x])) + 1
    
    for j in range(len(mapa[0])):
        if (j, 0) not in adj:
            continue 
        y, dist = dijkstra(mapa, adj,(j, 0))
        if y == len(mapa) - 1:
            menores.append((j, dist))
    
    if menores == []:
        return (0,0)
        
    return min(menores, key=lambda t: t[1])
