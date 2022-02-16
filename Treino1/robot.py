def robot(comandos):
    l = []
    dir = ((0,1),(1,0),(0,-1),(-1,0))
    pos_dir = 0
    pos = [0,0]
    path = []
    for comando in comandos:
        path.append(tuple(pos))
        if comando == 'A':
            pos[0] += dir[pos_dir % 4][0]
            pos[1] += dir[pos_dir % 4][1]
        
        elif comando == 'E':
            pos_dir -= 1
        
        elif comando == 'D':
            pos_dir += 1
        
        elif comando == 'H':
            l.append((min([x[0] for x in path]),
                      min([y[1] for y in path]),
                      max([x[0] for x in path]),
                      max([y[1] for y in path])))
            pos_dir = 0
            pos = [0,0]
            path.clear()
    
    return l
