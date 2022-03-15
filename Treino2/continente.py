'''

O objectivo deste problema é determinar o tamanho do maior continente de um planeta.
Considera-se que pertencem ao mesmo continente todos os países com ligação entre si por terra. 
Irá receber uma descrição de um planeta, que consiste numa lista de fronteiras, onde cada fronteira
é uma lista de países que são vizinhos entre si. 
A função deverá devolver o tamanho do maior continente.

'''

def bfs(adj,o):
    vis = {o}
    queue = [o]
    while queue:
        v = queue.pop(0)
        for d in adj[v]:
            if d not in vis:
                vis.add(d)
                queue.append(d)
    return len(vis)

def maior(vizinhos):
    if vizinhos == []:
        return 0
        
    grafo = {}
    for vizinho in vizinhos:
        for p in vizinho:
            if p not in grafo:
                grafo[p] = set(vizinho)
            else:
                grafo[p] = grafo[p].union(set(vizinho))
            grafo[p].remove(p)
    
    return max([bfs(grafo, x) for x in grafo])
