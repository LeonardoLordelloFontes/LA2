def formata(codigo):
    r = []
    indent = 0
    for c in codigo:
        if r == [] or c != ' ' or r[-1] != ' ': #lazy evaluation
            if c == '}':
                r.pop()
                r[-1] = '}'
            else:
                r.append(c)
        if c == ';' or c == '{' or c == '}':
            if c == '{':
                indent += 2
            elif c == '}':
                indent -= 2
            r.append('\n')
            for _ in range(indent):
                r.append(' ')
        
    return "".join(r[0:-1])
