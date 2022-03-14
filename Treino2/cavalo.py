
def bfs(moves,o,d):
    dist = {}
    vis = {o}
    queue = [o]
    while queue:
        v = queue.pop(0)
        if v == d:
            break
        
        if v not in dist:
                dist[v] = 0
        
        for move in moves:
            pos = (v[0]+move[0], v[1]+move[1])
            if pos not in vis:
                vis.add(pos)
                dist[pos] = dist[v] + 1
                queue.append(pos)
        
    return dist[d]
    
def saltos(o,d):
    if o == d:
        return 0
        
    moves = ((2, 1),(1, 2),(-2, 1),(2, -1),(-2, -1),(-1, 2),(1, -2),(-1, -2))
    return bfs(moves,o,d)
