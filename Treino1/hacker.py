def hacker(log):
    d = {}
    l = []
    for transaction in log:
        if transaction[1] not in d:
            d[transaction[1]] = ['*'] * 16
        
        for i in range(16):
          if transaction[0][i] != '*':
              d[transaction[1]][i] = transaction[0][i]
    
    
    for email in d:
        l.append(("".join(d[email]),email))
    
    l.sort(key=lambda t: t[1])
    l.sort(key=lambda t: 16 - t[0].count('*'), reverse=True)
    return l
